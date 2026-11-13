# F.2 5GS Bridge configuration

For 5GS integrating with fully-centralized model TSN network, the CNC provides TSN information to the AF.

[figure]

Figure F.2-1: 5GS Bridge information configuration

1\. CNC provides per-stream filtering and policing parameters according to clause 8.6.5.2.1 of IEEE Std 802.1Q \[66\] to AF and the AF uses them to derive TSN QoS information and related flow information. The CNC provides the forwarding rule to AF according to clause 8.8.1 of IEEE Std 802.1Q \[66\]. The TSN AF uses this information to identify the DS-TT MAC address of corresponding PDU session.

The AF determines if the stream is UE-UE TSC and divides the stream into UL and DL streams for PDU Sessions corresponding to ingress DS-TT Ethernet port and egress DS-TT port(s) as specified in clause 5.28.2 of TS 23.501 \[2\] and separately triggers following procedures for the UL and DL streams.

2\. The AF determines the MAC address of a PDU Session based on the previous stored associations, then triggers an AF request procedure. The AF request includes the DS-TT MAC address of the PDU session.

Based on the information received from the CNC, 5GS bridge delay information and the UE-DS-TT residence time, the TSN AF determines the TSN QoS information and TSC Assistance Container for one or more TSN streams and sends them to the PCF. The TSN AF also provides Service Data Flow Filter containing Flow description also includes Ethernet Packet Filters.

3\. When PCF receives the AF request, the PCF finds the correct SMF based on the DS-TT MAC address of the PDU session and notifies the SMF via Npcf_SMPolicyControl_UpdateNotify message.

After mapping the received TSN QoS parameters for TSN streams to 5GS QoS, the PCF triggers Npcf_SMPolicyControl_UpdateNotify message to update the PCC rule to the SMF. The PCC rule includes the Ethernet Packet Filters, the 5GS QoS profile along with TSC Assistance Container.

4\. SMF may trigger the PDU Session Modification procedure to establish/modify a QoS Flow to transfer the TSN streams. During this procedure, the SMF provides the information received in PCC rules to the UPF via N4 Session Modification procedure.

Upon reception of the TSC Assistance Container, the SMF determine the TSCAI for QoS flow and sends the TSCAI along with the QoS profile to the NG RAN.

5\. If needed, the CNC provides additional information (e.g. the gate control list as defined in clause 8.6.8.4 of IEEE Std 802.1Q \[66\]) to the TSN AF.

6\. The AF determines the MAC address of a PDU Session for the configured port based on the previous stored associations, this is used to deliver the Port Management information to the correct SMF that manages the port via PCF. The AF triggers an AF request procedure. The AF request includes the DS-TT MAC address (i.e. the MAC address of the PDU Session), TSN QoS Parameters, Port Management information Container and the related port number as defined in clause 5.28.3 of TS 23.501 \[2\]. The port number is used by SMF to decide whether the configured port is in DS-TT or NW-TT.

NOTE: When TSN AF needs to convey 5GS Bridge- or NW-TT port-specific information to the NW-TT/UPF, the TSN AF chooses an arbitrary AF Session related to the corresponding 5GS bridge and sends the 5GS Bridge-specific information inside a User plane node Management Information Container (UMIC) or NW-TT Port Management Information Container (NW-TT PMIC) as specified in TS 23.501 \[2\].

7\. The PCF determines the SMF based on the MAC address received in the AF request, the PCF maps the TSN QoS information provided by the AF to PCC rules as described in clause 5.28.4 of TS 23.501 \[2\]. The PCF includes the TSC Assistance Container received from the AF with the PCC rules and forwards it to the SMF. The PCF transparently transports the received Port Management information Container and related port number to SMF via Npcf_SMPolicyControl_UpdateNotify message.

8a. If the SMF decides the port is on DS-TT based on the received port number, the SMF transports the received Port Management information Container to the UE/DS-TT in PDU Session Modification Request message.

8b. If the SMF decides the port is on NW-TT based on the received port number, the SMF transports the received Port Management information Container to the UPF/NW-TT in N4 Session Modification Request message. SMF provides the Ethernet Packet Filters as part of the N4 Packet Detection rule to the UPF/NW-TT.

If the UPF sends a Clock Drift Report to the SMF as described in clause 5.27.2 of TS 23.501 \[2\], the SMF adjusts the Burst Arrival Time, Periodicity and Survival Time (if present) from a TSN grandmaster clock to the 5G clock and sends the updated TSCAI to NG-RAN.
