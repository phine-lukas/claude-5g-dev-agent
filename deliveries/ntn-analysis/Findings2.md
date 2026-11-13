<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# NTN analysis, part 2: follow-up questions

**Type:** analysis only, no patches.
**Date:** 2026-11-10
**Builds on:** `FINDINGS.md` in this folder.
**Setup assumed:** LEO, transparent (bent-pipe) payload, gNB on the ground next
to the gateway, one CU (= one gNB) per satellite, so satellite-to-satellite
handover is always inter-gNB.

Code references are against the local checkout
`~/Projects/projects/frq-adsat-phine/openairinterface5g` at `3e4fcd5d7b`
(branch `mbs-phase-a`). Line numbers differ by a few dozen lines from
`FINDINGS.md`, which used upstream `develop` at `88245ba8`.

All effort figures are my estimates for one engineer who knows OAI, working
AI-supported, including RFsimulator tests. They are not measured. Coding is the
smaller part; most of the time goes into end-to-end testing and debugging.

---

## Short answers

| # | Question | Answer |
|---|---|---|
| 1 | Is CHO feasible? | Yes, if you limit it to what your setup needs: **time-based CHO over N2**, about 3–5 weeks. Full CHO (several candidates, measurement and location triggers) needs Xn handover first and is a 3–4 month feature. |
| 2 | Effort for control function → CU → DU? | About 1 week for a feed straight into the DU. About 2–3 weeks if the CU must be the single entry point and relay to the DU. Add about 1 week if SIB19 should also carry neighbour satellites and `t-Service`. |
| 2b | Is CU → DU transport of SIB19 data standardised? | **No.** 3GPP only says "O&M provides ephemeris to the gNB" and "the DU generates SIB19". How the data gets to the DU is not specified. F1AP has no IE for it. You have to define it yourself; F1AP's *Private Message* is the sanctioned container for that. |
| 3 | Can we live with N2? | **Yes.** N2 handover is explicitly allowed for NTN, including the time-based variant. The packet loss is an **OAI gap** (no data forwarding), not an NTN or N2 property. Xn would not fix it: OAI has no Xn handover at all, and the missing forwarding work is the same for both. |

One correction to `FINDINGS.md`: it said "NGAP has no conditional handover at
all". That is too strong. Since Rel-18 there is a **time-based handover over
NG** for NTN (details in §1.2). This makes your case easier.

---

## 1. Conditional handover: feasible or very big?

### 1.1 It depends on which CHO

| Variant | What it is | Needs Xn? | Size |
|---|---|---|---|
| **A. Time-based CHO over N2** | One target cell, prepared with the normal N2 handover. The UE gets the handover command early and executes it at a configured time (`condEventT1`). | No | **3–5 weeks** |
| **B. Full CHO** | Several candidate cells, triggers A3/A4/A5, location (`condEventD1`), cancel/replace of candidates. | **Yes** | **3–4 months** (Xn handover 6–10 weeks, then CHO 4–6 weeks) |

For bent-pipe LEO with a known constellation, variant A is the one that
matters: the network knows from the orbit when satellite B takes over, so one
candidate and a time trigger are enough.

### 1.2 Variant A is standard-conformant

- TS 38.300 V18.11.0 clause 9.2.3.4.1 says in general: "CHO is not supported
  for NG-C based handover in this release of the specification."
- For NTN, clause 16.14.3.2.2 makes the exception: "When a time-based trigger
  condition is used, the source gNB may signal the corresponding parameters to
  a target gNB in an NG-C based handover, see TS 23.502, or Xn based handover."
- TS 23.502 V18.14.0 clause 4.9.1.3.1 (N2 handover, general): "NTN NR
  supports additional trigger conditions i.e. time-based trigger condition,
  upon which UE may execute conditional handover to a candidate cell."
- TS 38.413 V18.11.0 clause 9.3.1.29: the *Source NG-RAN Node to Target NG-RAN
  Node Transparent Container* carries an optional *Time Based Handover
  Information* IE (*Handover Window Start*, *Handover Window Duration*), marked
  "This IE only applies to NTN". Clause 8.4.2.2: the target "may use this
  information to allocate necessary resources".
- This IE is **not** in TS 38.413 V17.10.0, so it is a Rel-18 addition. OAI
  compiles NGAP 15.8.0. The IE is optional with criticality "ignore", so a
  first version can leave it out and still be conformant.

Verify:

```bash
grep -n "time-based trigger" specs/38.300/18.11.0/clauses/16.14.md
```

```bash
grep -n "Time Based Handover Information" -A2 specs/38.413/18.11.0/clauses/9.3.1.29.md
```

### 1.3 What variant A consists of

| Part | Work | Estimate |
|---|---|---|
| gNB RRC (CU), source side | Run the existing N2 preparation. Instead of sending the target's handover command directly, wrap it in `ConditionalReconfiguration-r16` with one `CondReconfigToAddMod` whose execution condition is a `condEventT1-r17` (TS 38.331 V17.3.0 clause 6.3.2). The types are already in the RRC 17.3.0 grammar OAI compiles. | 1–1.5 weeks |
| nrUE RRC | Implement TS 38.331 V17.3.0 clause 5.3.5.13 for T1 only: store the candidate, evaluate the time condition, execute the stored reconfiguration. Nothing of this exists today. | 1.5–2 weeks |
| Time source at the UE | `t1-Threshold` is absolute UTC in 10 ms units since 1900-01-01 (TS 38.331 V17.3.0 clause 6.3.2). The UE needs UTC. The nrUE only notes that SIB9 was received (`openair2/RRC/NR_UE/rrc_UE.c:332-334`) and does not use its time. In RFsim the host clock can stand in. | 2–3 days |
| Trigger input | The CU needs the switch time from the NTN control function. This is the same feed as in §2. | shared with §2 |
| Tests | RFsim scenario with two gNBs plus unit tests for the new RRC encode/decode. | about 1 week |

Risks I could not close by reading code:

- **Core timers.** Between HANDOVER COMMAND and the UE arriving at the target,
  the source gNB and the AMF run supervision timers. With CHO the gap is longer
  than usual. Prepare only a few seconds before the switch time and test
  against your AMF.
- **Commercial UEs.** If you test with a real NTN modem instead of the OAI
  nrUE, it must support Rel-17 `condEventT1`. That is a UE capability, and I
  have not checked any device.

### 1.4 Do you need CHO at all?

Not to get a working, loss-free handover. In your setup the gNB is on the
ground and knows the switch time, so it can send a normal handover command at
the right moment. OAI already has the trigger
(`nr_HO_N2_trigger_telnet()`, `openair2/RRC/NR/rrc_gNB_mobility.c:658`).

CHO adds two things: the command is delivered early, while the source link is
still good, and the handover of many UEs is not squeezed into one instant.
That matters with many UEs or a hard switch. For a first testbed it is an
optimisation. I would do it after data forwarding (§3.4).

---

## 2. Ephemeris from the NTN control function via the CU to the DU

### 2.1 What exists

- The DU already has the complete update path: `nr_update_sib19()`
  (`openair2/LAYER2/NR_MAC_gNB/config.c:1185`) rewrites `ntn-Config` and
  re-encodes SIB19 for all cells.
- An ITTI message `GNB_SAT_POSITION_UPDATE` is handled in
  `openair2/GNB_APP/gnb_app.c:204-206`, but nothing sends it.
- The only caller today is the RFsimulator
  (`radio/rfsimulator/apply_channelmod.c:155`).

What is missing is a way in from outside, and, if the CU should be in the
path, a way from the CU to the DU.

### 2.2 Effort

| Step | Work | Estimate |
|---|---|---|
| 1. External feed into the DU | A small listener (UDP or telnet command) in the DU that turns a message from the control function into `GNB_SAT_POSITION_UPDATE`. Includes unit conversion and choosing the epoch time (see below). | 3–5 days |
| 2. CU as entry point, relay to DU | The same listener in the CU, plus a new F1AP message CU → DU (§2.3), encoder/decoder in `openair2/F1AP/lib/` with unit tests, and a DU handler that calls `nr_update_sib19()`. | 1–2 weeks more |
| 3. More SIB19 content | `ntn-NeighCellConfigList`, `t-Service`, `referenceLocation`, `distanceThresh`. OAI's SIB19 carries only `ntn-Config` today. The neighbour satellite's ephemeris is what the UE needs to measure and synchronise to the next satellite. | about 1 week |

In a monolithic gNB (no F1 split) step 2 disappears.

One point is harder than it looks: **epoch time.** `nr_update_sib19()` expects
the caller to say for which SFN and subframe of the DU's cell the position is
valid (`config.c:1124-1125`). The RFsimulator knows that, because it owns the
sample clock. An external control function works in UTC. So either the DU maps
UTC to its own SFN, or it propagates the received state vector to the next
frame boundary itself. Neither the CU nor the control function can do this
correctly, because only the DU knows its frame timing. This is also the
practical reason why 3GPP puts SIB19 in the DU.

### 2.3 What the standard says (question 2b)

Three separate facts:

1. **Where the data comes from: standardised as a requirement only.**
   TS 38.300 V18.11.0 clause 16.14.7: "The following NTN related parameters
   shall be provided by O&M to the gNB", then ephemeris (state vectors or
   orbital elements), epoch time, gateway locations, and "additional
   information to enable gNB operation for feeder/service link switch overs",
   "on a regular basis or upon demand". Annex B.4: the NTN control function
   "provides control data, e.g. Ephemeris, to the non-NTN infrastructure gNB
   functions". The interface is called O&M. No protocol or message format is
   given in the RAN specifications. I did not check the 3GPP management
   specifications (TS 28.541, the network resource model), which is where a
   data model for this would be. They are not converted in this toolkit.

2. **Who builds SIB19: standardised, it is the DU.**
   TS 38.470 V18.5.0 clause 5.2.2, NOTE: "The SIB19 is generated by the
   gNB-DU."

3. **How the data gets from the CU to the DU: not standardised.**
   TS 38.473 (F1AP) has no NTN, ephemeris or SIB19 content up to V18.11.0. I
   have not checked Rel-19 (V19.x). The 3GPP view is that "the gNB" receives
   the data from O&M, and that the DU has its own management connection. In
   O-RAN terms that is O1 to the O-DU. The data does not travel via the CU.

So the chain "control function → CU → DU" is your own architecture choice. It
does not violate the standard, but the CU → DU hop has to be defined by you.

Options for that hop:

| Option | Conformant? | Comment |
|---|---|---|
| **F1AP Private Message** carrying your own ephemeris IE | Yes. This is the mechanism F1AP provides for non-standard content. | TS 38.473 V18.11.0 clause 9.4.2: for "operator- (and/or vendor) specific features" and "research purposes". The message is in the F1AP 16.21.0 grammar OAI compiles. OAI has no handler for it yet (`openair2/F1AP/f1ap_handlers.c:44`). A third-party DU would ignore it. **This is what I recommend if the CU must relay.** |
| Control function sends to CU and DU separately | Yes. This is the closest to the 3GPP picture. | Least work (step 1 only, done twice). The CU uses its copy for handover timing, the DU for SIB19. |
| CU encodes SIB19 and sends it in *gNB-CU System Information* | No. | Excluded by TS 38.470 clause 5.2.2 and TS 38.473 clause 9.3.1.42. See `FINDINGS.md` §2.5 option A. |
| Your own extension IE inside a standard F1AP message | No. | It changes standard messages, and a foreign DU may reject them. |

**Is the update of SIB19 itself standardised?** Towards the UE, yes. The
content is defined in TS 38.331 V17.3.0 clause 6.3.2 (`NTN-Config`). The
ephemeris, epoch time and common TA fields may change without an SI change
notification and without a `valueTag` change. The UE re-reads SIB19 before its
validity timer (T430, `ntn-UlSyncValidityDuration`) runs out. Inside the
network (who triggers the DU, and how often) nothing is standardised.

---

## 3. Is N2 handover enough for LEO bent-pipe?

### 3.1 Is it legitimate to use N2 in NTN?

Yes. TS 38.300 V18.11.0 clause 16.14.4.3 names both for the transfer between
two gNBs: "either NG based or Xn based handover, and it depends on the gNBs'
implementation and configuration information provided to the gNBs by the NTN
Control function". Xn is not mandatory. As §1.2 shows, 3GPP even added the
time-based variant specifically to the NG handover.

### 3.2 Is the packet loss normal for NTN?

No. It is specific to OAI's current implementation.

A standard N2 handover does not lose packets on acknowledged-mode bearers. Two
mechanisms ensure that (TS 23.502 V18.14.0 clauses 4.9.1.3.2 and 4.9.1.3.3; TS 38.300
V18.11.0 clause 9.2.3.2.3):

1. **Status transfer.** The source tells the target the PDCP sequence state.
   OAI implements this.
2. **Data forwarding.** Packets that arrive at the source gNB after the
   handover command are sent on to the target gNB and delivered there. **OAI
   does not implement this**, in either direction (evidence in `FINDINGS.md`
   §3.3; the source still sends an empty Handover Required Transfer,
   `openair3/NGAP/ngap_gNB_mobility_management.c:75-77`).

With forwarding, packets during the handover are delayed by the interruption
time. They are not lost. Unacknowledged-mode bearers can still lose the few
packets that were in the air; that is true in terrestrial networks too.

What NTN changes is how often it happens, not the mechanism. A LEO UE is
handed over every few minutes or faster (TR 38.821 V16.2.0 Table 7.3.2.1.4-1:
6.6 s to 132 s per cell), so a loss per handover that nobody notices
terrestrially becomes a permanent problem.

### 3.3 Would Xn solve the loss and the timing?

| Aspect | N2 | Xn | Does Xn help you? |
|---|---|---|---|
| Packet loss | Lossless with data forwarding | Lossless with data forwarding | **No.** The forwarding work (forwarding tunnel, PDCP packets with sequence numbers, end marker, ordering at the target) is the same, and OAI has it for neither. |
| Radio interruption (handover command until the UE is on the target) | Set by the radio link | Set by the radio link | **No.** Identical. For LEO 600 km it is tens of milliseconds plus random access (`FINDINGS.md` §3.2). |
| Preparation time | Via AMF, and SMF/UPF | Direct gNB to gNB | A little. Your gNBs and the core are on the ground, so this is milliseconds either way. With a time-based handover the preparation is done in advance and is not time critical. |
| Bulk handover of all UEs of a satellite | Loads AMF and SMF | Core only sees a path switch | Yes, with many UEs. Not relevant for a testbed. |
| CHO | Time-based only (Rel-18) | All variants | Only if you need variant B from §1.1. |
| State in OAI | **Implemented** (without forwarding) | **Not implemented.** Only Xn Setup exists; the message encoders are there, but RRC never calls them. | Xn means building a new handover first. |

So Xn is not a must, and it does not fix the two problems you named. It is the
right step later, if you need multi-candidate CHO or have many UEs per
satellite.

### 3.4 Recommendation

Stay on N2 and close the gaps in this order:

| Step | What | Estimate |
|---|---|---|
| 1 | **Data forwarding for N2 handover.** Downlink first, acknowledged-mode bearers, direct forwarding path (your gNBs are both on the ground and can reach each other). Touches NGAP, RRC, the CU-UP, GTP-U and PDCP. The needed IEs are in the NGAP 15.8.0 grammar OAI compiles. | 3–5 weeks |
| 2 | **Time-triggered N2 handover** driven by the control function, instead of the RSRP/A3 trigger, which works poorly between satellite beams. | a few days on top of §2 |
| 3 | **Contention-free random access and configurable T304** in the handover command. Both are fixed today (`openair2/LAYER2/NR_MAC_gNB/nr_radio_config.c:4350-4351`: T304 = 2000 ms, no dedicated RACH). | about 1 week |
| 4 | **Time-based CHO over N2** (§1, variant A). | 3–5 weeks |
| 5 | Xn handover and full CHO, only if needed. | 3–4 months |

Steps 1 to 3 give a loss-free, well-timed satellite handover on N2. Step 4
makes it robust for hard switches and many UEs.

Not verified: whether your core supports what step 1 needs. Direct forwarding
only needs the AMF and SMF to pass the forwarding information through.
Indirect forwarding (via the UPF) needs active SMF/UPF support. I did not
check Open5GS or the OAI core for either.

---

## 4. What I did not verify

- TS 38.473 Rel-19 (V19.x): whether NTN content was added to F1AP after
  V18.11.0.
- TS 28.541 and other management specifications: whether an O&M data model for
  ephemeris exists.
- Core network behaviour: handover supervision timers with a delayed (time-based)
  execution, and data-forwarding support.
- Commercial UE support for `condEventT1`.
- Nothing was built or run for this document. All statements about OAI come
  from reading the code.
