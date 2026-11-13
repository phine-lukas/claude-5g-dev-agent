# F.1 5GS Bridge information reporting

[figure]

Figure F.1-1: 5GS Bridge information reporting

Identities of 5GS Bridge and UPF/NW-TT ports are pre-configured on the UPF based on deployment. The SMF requests the UPF/NW-TT to measure and report the clock drift between the TSN GM time and 5GS GM time for one or more TSN time domains.

1\. PDU Session Establishment as defined clause 4.3.2.2.1-1 is used to establish a PDU Session serving for TSC.

During this procedure, the SMF selects a UPF, which supports functions as defined in clause 5.28.1 of TS 23.501 \[2\], for the PDU Session.

During this procedure, the SMF receives the UE-DS-TT residence time, DS-TT MAC address for this PDU Session and port management capabilities from the DS-TT/UE in PDU Session Establishment request and receives the allocated port number for DS-TT Ethernet port and user-plane Node ID in N4 Session Establishment Response message. The UPF allocates the port number for DS-TT, user-plane Node ID after receiving N4 Session Establishment Request message.

2\. The SMF sends the information received in step 1 to the TSN AF via PCF to establish/modify the 5GS Bridge. The Npcf_PolicyAuthorization_Notify message in step 2b is delivered via the pre-configured AF session as described in clause 4.16.5.1. The TSN AF stores the binding relationship between 5GS user-plane Node ID, MAC address of the DS-TT Ethernet port and also updates 5GS bridge delay as defined in clause 5.27.5 of TS 23.501 \[2\] for future configuration. The TSN AF requests creation of a new AF session associated with the MAC address of the DS-TT Ethernet port using the Npcf_PolicyAuthorization_Create operation (step 2c) and subscribes for TSN events over the newly created AF session using the Npcf_PolicyAuthorization_Subscribe operation (step 2d).

In the case of TSN AF support for direct notification from UPF for PMIC and UMIC, the subscription in step 2d has following additional information: "Notification Target Address for PMIC/UMIC UPF event" and "Correlation ID for PMIC/UMIC UPF event".

Using the 5GS user-plane Node ID received in step 2b the TSN AF subscribes with the NW-TT for receiving user plane node management information changes for the 5GS bridge indicated by the 5GS user-plane Node ID as described in clause 5.28.3.1 of TS 23.501 \[2\].

After receiving a User plane node Management Information Container (UMIC) containing the NW-TT port numbers, the TSN AF subscribes with the NW-TT for receiving NW-TT port management information changes for the NW-TT port indicated by each of the NW-TT port numbers as described in clause 5.28.3.1 of TS 23.501 \[2\].

The TSN AF can use any PDU Session to subscribe with the NW-TT for bridge or port management information notifications. Similarly, the UPF can use any PDU Session to send bridge or port management information notifications.

3\. If DS-TT has indicated support for the TSN Time domain number in the port management capabilities, TSN AF provides the TSN Time domain number to DS-TT. Optionally, TSN AF provides the TSN Time domain number to NW-TT.

4\. If supported according to the port management capabilities received from DS-TT, TSN AF retrieves txPropagationDelay and Traffic Class table from DS-TT. TSN AF also retrieves txPropagationDelay and Traffic Class table from NW-TT.

NOTE: It is assumed that distribution of TSN GM time towards NW-TT and DS-TT for the TSN time domain is activated before TSN AF retrieves txPropagationDelay so that DS-TT and NW-TT can convert txPropagationDelay from 5GS time to TSN time before reporting txPropagationDelay to TSN AF.

5\. If DS-TT supports neighbor discovery according to the port management capabilities received from DS-TT, then TSN AF:

\- provides DS-TT port neighbor discovery configuration to DS-TT to configure and activate the LLDP agent in DS-TT;

\- subscribes to receive Neighbor discovery information for each discovered neighbor of DS-TT (see Table K.1-1 in TS 23.501 \[2\].

If DS-TT does not support neighbor discovery, then TSN AF:

\- provides DS-TT port neighbor discovery configuration to NW-TT to configure and activate the LLDP agent in NW-TT to perform neighbor discovery on behalf of DS-TT;

\- subscribes to receive Neighbor discovery information for each discovered neighbor of DS-TT from NW-TT (see Table K.1-1 in TS 23.501 \[2\].

TSN AF:

\- writes NW-TT port neighbor discovery configuration to NW-TT to configure and activate the LLDP agent in NW-TT;

\- subscribes to receive Neighbor discovery information for each discovered neighbor of NW-TT (see Table K.1-1 in TS 23.501 \[2\]).

6\. TSN AF receives notifications from DS-TT (If DS-TT supports neighbour discovery) and NW-TT on discovered neighbors of DS-TT and NW-TT.

7\. The TSN AF constructs the above received information as 5GS Bridge information and sends them to the CNC to register a new TSN Bridge or update an existing TSN Bridge.
