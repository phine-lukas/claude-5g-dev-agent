# O.2 Multiple PDU Sessions for different groups

In the case that the UE Application sends individual copies of data to different receivers, 5GS allows UE to simultaneously send data to different groups with different QoS policy via the following:

\- If different groups (IP or Ethernet multicast groups) are associated to different DNN and S-NSSAI combinations used for different 5G VN groups, then different PDU Sessions are used to transfer the data copy sent to different groups. As a result, the UE sends the same data to different groups using the QoS Flow of the respective PDU Sessions.

Figure O.2-1 shows multiple PDU sessions used for different groups as an example.

\- Group1 (G1): a group of multicast address 1 with members UE1 and UE2 is associated with 5GVN.1 group. The QoS for multicast address 1 is set to QoS1. For G1, its members, multicast address 1 and corresponding QoS1 are provisioned as part of the AF requested QoS information as described in clause 6.1.3.28 of TS 23.503 \[45\].

\- Group2 (G2): a group of multicast address 2 with members UE1 and UE3 is associated with 5GVN.2 group. The QoS for multicast address 2 is set to QoS2. For G2, its members, multicast address 2 and corresponding QoS2 are provisioned as part of the AF requested QoS information as described in clause 6.1.3.28 of TS 23.503 \[45\].

\- During establishment or modification procedure for PDU Sessions targeting to DNN and S-NSSAI for 5GVN.1 group, or upon detection of the UE joining a multicast address, the SMF and PCF can jointly use the AF requested QoS information for 5GVN.1 group to set up the QoS flow in respective member's PDU Session. During establishment or modification procedure for PDU Sessions targeting to DNN and S-NSSAI for 5GVN.2 group, or upon detection of the UE joining a multicast address, the SMF and PCF can jointly use the AF requested QoS information for 5GVN.2 group to set up the QoS flow in respective member's PDU Session. As a result:

\- There will have two PDU Sessions for UE1: one PDU Session is targeting to DNN and S-NSSAI for 5GVN.1 group and there will have one QoS flow setup to carry data destined to multicast address 1 with QoS1; the other PDU Session is targeting to DNN and S-NSSAI for 5GVN.2 group and there will have one QoS flow setup to carry data destined to multicast address 2 with QoS2.

\- There will have one PDU Session for UE2: this PDU Session is targeting to DNN and S-NSSAI for 5GVN.1 group and there will have one QoS flow setup to carry data destined to multicast address 1 with QoS1.

\- There will have one PDU Session for UE3: this PDU Session is targeting to DNN and S-NSSAI for 5GVN.2 group and there will have one QoS flow setup to carry data destined to multicast address 2 with QoS2.

\- UE1 sends data with multicast address 1 (MA.1) to a UPF via the QoS Flow of UE1's PDU session for 5GVN.1 group. The UPF forwards the packet to UE2 as it is a member of multicast group represented by multicast address 1 via the QoS Flow of UE2's PDU Session for 5GVN.1 group.

\- UE1 also sends the same data with multicast address 2 (MA.2) to the UPF via the QoS Flow of UE1's PDU Session for 5GVN.2 group. The UPF forwards the packet to UE3 as it is a member of multicast group represented by multicast address 2 via the QoS Flow of UE3's PDU Session for 5GVN.2 group.

[figure]

Figure O.2-1: Multiple PDU Sessions for different groups
