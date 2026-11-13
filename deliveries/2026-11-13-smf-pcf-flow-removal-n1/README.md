# Delivery 2026-11-13-smf-pcf-flow-removal-n1

Date: 2026-11-13 · Profile: none · Status: **complete** (cloud tiers T0/T1 only)

A PCF-initiated QoS flow removal never reached the gNB or the UE. Of the four
defects reported, the first was already fixed on the base branch (`f086910`);
this delivery closes the other three. The N1 PDU Session Modification Command
was encoded without the IEIs of its optional IEs, so the UE could not parse it
and rejected it on create. The removal case failed to encode at all — the root
cause is not where the task description suspected: `ENCODE_U8`/`U16`/`U32` are
multi-statement macros with no `do { } while (0)`, so under an unbraced `if`
only the store was skipped while the size counter advanced anyway, making a
4-octet delete rule report 6 and leaving two uninitialised octets in the buffer.
And an N1 encode failure was ignored, so the empty container made the AMF drop
the valid N2 release list with it. A reviewer should expect three small NAS
library fixes, two SMF fixes, a submodule bump, and 11 new unit tests — plus
three further length bugs in `QosRule` found along the way.

## Repos

| Repo | Role | Base branch | Base SHA | Patches |
|---|---|---|---|---|
| `oai-cn5g-common-src` | target (submodule `src/common-src`) | pinned by the SMF | `f725043c` | 3 |
| `oai-cn5g-smf` | target | `fix/qfi-reuse` | `f086910` | 4 |

Apply `common-src` first — the SMF's last patch bumps the submodule onto it.

Total: **7** patch(es).

## Test summary

| Tier | Result |
|---|---|
| T0 build | **PASSED** — clean build, no warnings (33:32) |
| T1 unit | **PASSED** — 57/57, 11 new |
| T2 integration | **SKIPPED** — `oai-cn5g-fed` not in the session, needs a live deployment |
| T3 container E2E | **SKIPPED** — no docker daemon in the VM; not opted in (`E2E` absent) |
| T4 testbed / hardware | LOCAL ONLY |

> The end-to-end claim — gNB releases the DRBs, UE deletes the QoS rules — is
> **not verified by this delivery**. TESTING.md L1 has the exact local steps and
> the log lines to watch, including the before/after N1 payload.

Details, including everything still to run locally, are in [TESTING.md](TESTING.md).

## Files

- [APPLY.md](APPLY.md) — how to apply the patch series, per repo
- [CHANGES.md](CHANGES.md) — what changed, mapped to spec clauses, with the traceability table
- [TESTING.md](TESTING.md) — tier table, cloud results, and the local steps that remain
- [OPEN_ISSUES.md](OPEN_ISSUES.md) — assumptions, untested parts, known gaps
- [PR_DESCRIPTION.md](PR_DESCRIPTION.md) — draft PR text for when you push
- [PLAN.md](PLAN.md) — the approved plan this was built from

## Repo details


### oai-cn5g-smf

- Remote: https://github.com/openairinterface/oai-cn5g-smf
- Agent branch: `agent/2026-11-13-smf-pcf-flow-removal-n1` (local only, never pushed) — HEAD `664ce87fec256b060fead29ab36612245d569588`
- Base commit: `f086910b62964497f6a38dc1e78489dc02348efe`
- Patches: `patches/oai-cn5g-smf/` (4)

Commits:

```
    664ce87 build(smf): bump common-src for the NAS encoding fixes
    6803a00 test(smf): cover the NAS encoding of the Modification Command
    709549c fix(smf): do not send an N1N2 transfer with a failed container
    4bb06a4 fix(smf): build spec-compliant delete QoS rules
```

Diffstat:

```
     src/common-src                                     |   2 +-
     src/smf_app/session_handler.cpp                    |  59 ++--
     src/smf_app/smf_context.cpp                        |  83 ++++--
     src/smf_app/test/CMakeLists.txt                    |   1 +
     src/smf_app/test/test_nas_modification_command.cpp | 310 +++++++++++++++++++++
     src/smf_app/test/test_session_handler.cpp          |  79 ++++++
     6 files changed, 470 insertions(+), 64 deletions(-)
```

### common-src

- Remote: https://github.com/openairinterface/oai-cn5g-common-src.git
- Agent branch: `agent/2026-11-13-smf-pcf-flow-removal-n1` (local only, never pushed) — HEAD `249a61033156dd2b2ba19dbb463ba1dacc783731`
- Base commit: `f725043cc3694f29c5ea91b0d244a868f5d4179a`
- Patches: `patches/common-src/` (3)

Commits:

```
    249a6103 fix(nas): set the IEI of the Modification Command's optional IEs
    02c83fa8 fix(nas): keep the QoS rule length indicator in sync
    b4a79b91 fix(nas): make the ENCODE macros single statements
```

Diffstat:

```
     common/common_defs.h                            | 18 ++++---
     nas/5gsm-msgs/PduSessionModificationCommand.cpp |  4 ++
     nas/ies/QosRule.cpp                             | 63 +++++++++++++++----------
     nas/ies/_5gsNetworkFeatureSupport.cpp           |  3 +-
     4 files changed, 57 insertions(+), 31 deletions(-)
```
