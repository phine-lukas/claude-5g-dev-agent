# O.1 A PDU Session with multiple QoS Flows for different groups

In case the UE Application sends individual copies of data to different receivers, 5GS allows UE to simultaneously send data to different groups with different QoS policy via the following:

\- If different groups (IP or Ethernet multicast groups) are associated to the same DNN and S-NSSAI combination used for a 5G VN group, then different QoS Flows of a single PDU Session may be used to transfer the data copy sent to different groups.

Figure O.1-1 shows a PDU Session with multiple QoS Flows for different groups as an example.

\- Group1 (G1): a group of multicast address 1 with members UE1 and UE2 is associated with 5GVN.A group. The QoS for multicast address 1 is set to QoS1. For G1, its members, multicast address 1 and corresponding QoS1 are provisioned as part of the AF requested QoS information as described in clause 6.1.3.28 of TS 23.503 \[45\].

\- Group2 (G2): a group of multicast address 2 with members UE1 and UE3 is associated with 5GVN.A group. The QoS for multicast address 2 is set to QoS2. For G2, its members, multicast address 2 and corresponding QoS2 are provisioned as part of the AF requested QoS information as described in clause 6.1.3.28 of TS 23.503 \[45\].

\- During establishment or modification procedure for PDU Sessions targeting to DNN and S-NSSAI for 5GVN.A group, or upon detection of the UE joining a multicast address, the SMF and PCF can jointly use the AF requested QoS information for 5GVN.A group to set up the QoS flow in respective member's PDU Session. As a result:

\- There will have two QoS flows in UE1's PDU Session targeting to DNN and S-NSSAI for 5GVN.A group, one QoS flow (QoS Flow 1.1) is used to carry data destined to multicast address 1 with QoS1, the other one (QoS Flow 1.2) is used to carry data destined to multicast address 2 with QoS2.

\- There will have one QoS flow (QoS Flow 2) in UE2's PDU Session targeting to DNN and S-NSSAI for 5GVN.A group, this QoS flow is used to carry data destined to multicast address 1 with QoS1.

\- There will have one QoS flow (QoS Flow 3) in UE3's PDU Session targeting to DNN and S-NSSAI for 5GVN.A group, this QoS flow is used to carry data destined to multicast address 2 with QoS2.

\- UE1 sends data with multicast address 1 (MA.1) to a UPF via QoS Flow 1.1 of UE1's PDU session for 5GVN.A group. The UPF forwards the packet to UE2 as it is a member of multicast group represented by multicast address 1 via QoS Flow 2 of UE2's PDU Session for 5GVN.A group.

\- UE1 also sends the same data with multicast address 2 (MA.2) to the UPF via QoS Flow 1.2 of the same PDU Session for 5GVN.A group. The UPF forwards the packet to UE3 as it is a member of multicast group represented by multicast address 2 via QoS Flow 3 of UE3'sPDU Session for 5GVN.A group.

[figure]

Figure O.1-1: A PDU Session with multiple QoS Flows for different groups
