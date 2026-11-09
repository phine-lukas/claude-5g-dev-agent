# D.1 General

This Annex applies to PDU sessions involving an Intermediate SMF (I-SMF), when the I-SMF has inserted an Uplink Classifier (UL CL) or Banching Point (BP) into the data path of the PDU session and a local PDU Session Anchor (PSA) further called PSA2 in this Annex, for local traffic offload.

For such PDU sessions, PFCP session related messages shall be exchanged between the SMF and I-SMF for:

\- the SMF to provide N4 information to the I-SMF regarding how the traffic shall be detected, enforced and monitored in the UPF(s) controlled by the I-SMF;

\- the I-SMF to forward N4 information with traffic usage reporting to the SMF.

See clause 5.34.6 of 3GPP TS 23.501 \[28\].

Whether the UL CL or BP and PSA2 are supported by the same UPF or not shall be transparent to the SMF.

When exchanging N4 information over N16a, the SMF and I-SMF shall assume the model in Figure D.1-1 where the UL CL or BP and PSA2 are supported by separate UPFs, i.e. separate PFCP session related messages shall be exchanged over N4 for the UL CL/BP and for the PSA2.

NOTE 1: This allows the SMF and I-SMF to exchange unambiguous information on whether N4 information exchanged over N16a relates to the UL CL/BP or the PSA2, e.g. whether a QER is to be enforced in the UL CL/BP or PSA2.

NOTE 2: The UL CL/BP and PSA2 inserted by the I-SMF can be co-located or located on different UPFs, regardless of the model assumed over N16a for the exchange of N4 information.

NOTE 3: Only one local PSA (i.e. PSA2) is shown in this figure; in real deployment, more than one local PSAs can be inserted.

[figure]

Figure D.1-1: UL CL/BP and PSA2 model for N4 information exchanged over N16a

The I-SMF shall translate the N4 information received from the SMF into appropriate N4 rules towards the UL CL/BP and the PSA2; the I-SMF shall merge the N4 information received for the UL CL/BP and the PSA2 if the UL CL/BP and PSA2 are located on the same UPF.

The N4 information exchanged over N16a shall only include the rules related to the UL and DL traffic to offload via PSA2, and not include the rules to the non-offload UL and DL traffic via PSA1. The I-SMF shall generate on its own N4 rules towards the UL CL/BP for UL and DL traffic exchanged between the AN and PSA1. The PDR, FAR, URR, QER ID(s) allocated by the I-SMF and the SMF for the PFCP sessions between I-SMF and UL CL and between I-SMF and PSA2 shall be distinct; the Precedence of the PDRs set by the I-SMF and the SMF shall also be distinct (see clause D.2.1).

All the PFCP session related messages specified in clause 7.5 shall be supported over N16a. Unless specified otherwise in this Annex, the requirements specified in the rest of this specification for PFCP session related procedures and messages are also applicable to N16a.

None of the PFCP Node related messages specified in clause 7.4 shall be sent over N16a. PFCP Load and Overload control information shall not be exchanged over N16a.

Data forwarding procedures (see clause 5.3) shall not be used over N16a.

PFCP session related messages shall be sent over N16a in a binary body part of an HTTP multipart message using the Nsmf_PDUSession as specified in 3GPP TS 29.502 \[50\]. The Json body part of a HTTP multipart message shall indicate whether a given PFCP session related message relates to the UL CL/BP or to the PSA2. Presence of the DNAI IE indicates the PFCP session message relates to PSA2 and absence of the DNAI IE indicates the PFCP session message relates to UL CL/BP.
