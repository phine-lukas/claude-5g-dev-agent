# F.4 5GS interworking with TSN deployed in the transport network

For 5GS to control the IEEE TSN features deployed in the transport network, the SMF/CUC interacts with the CNC in the transport network (TN CNC).

[figure]

Figure F.4-1: 5GS Bridge information configuration

1\. The UE establishes a PDU Session as described in clause 4.3.2.2.1.

2\. During the PDU Session Establishment procedure, the SMF/CUC requests the UPF to assign the N3 tunnel information via N4 Session Establishment or Modification procedure. If interworking with TSN deployed in the transport network is supported (see clause 4.4.8 of TS 23.501 \[2\]), and the UPF supports CN-TL, the SMF/CUC includes a TL-Container to the N4 Session Establishment or Modification request including a get-request to the TL-Container, as described in clause 5.28a.2 of TS 23.501 \[2\].

The UPF responds with a N4 Session Establishment or Modification response. If the UPF supports CN-TL, the UPF includes a TL-Container to the response. The TL-Container includes a get-response as described in clause 5.28a.2 of TS 23.501 \[2\]. The SMF/CUC stores the information provided in the get-response.

3\. During the PDU Session Establishment procedure, the SMF/CUC requests the NG-RAN to assign the N3 tunnel information by invoking the Namf_Communication_N1N2MessageTransfer request. The SMF/CUC includes a TL-Container to the N2 SM information in the request, the TL-Container contains a get-request as described in clause 5.28a.2 of TS 23.501 \[2\].

The NG-RAN responds with a N2 SM information. If the NG-RAN supports AN-TL, the NG-RAN includes a TL-Container to the N2 SM information. The TL-Container includes a get-response as described in clause 5.28a.2 of TS 23.501 \[2\]. The SMF/CUC stores the information provided in the get-response.

4\. The AF (TSCTSF, AF, NEF or TSN AF) invokes the Npcf_PolicyAuthorization_Create/Update request. This may be due to reception of Ntsctsf_QoSandTSCAssistance_Create/Update request by the TSCTSF as described in clause 4.15.6.6 or clause 4.15.6.6.a, or due to reception of 5GS Bridge configuration by the TSN AF as described in clause F.2. The TSN AF or TSCTSF determines the TSC Assistance Container for one or more TSC streams and sends them to the PCF.

5-6.When PCF receives the request, the PCF initiates an SM Policy Association Modification procedure. The PCF notifies the corresponding SMF/CUC via Npcf_SMPolicyControl_UpdateNotify message as described in clause 4.16.5.2. The PCF updates the PCC rule to the SMF/CUC. The PCC rule includes the 5GS QoS profile along with TSC Assistance Container.

SMF/CUC triggers the PDU Session Modification procedure as described in clause 4.3.3.2 to establish a QoS Flow to transfer the TSC streams.

7\. During the PDU Session Modification procedure, the SMF/CUC provides the information received in PCC rules to the UPF via N4 Session Modification procedure. The SMF/CUC may instruct the UPF to assign a distinct N3 tunnel end point address for the QoS Flow as described in clause M.1 of TS 23.501 \[2\].

The UPF responds with a N4 Session Modification response.

8\. During the PDU Session Modification procedure, the SMF/CUC provides the information received in PCC rules to the NG-RAN by invoking the Namf_Communication_N1N2MessageTransfer request. The SMF also determines the TSCAI for the QoS Flow(s) and sends the TSCAI along with the QoS profile(s) to the NG-RAN. The SMF/CUC may instruct the NG-RAN to assign a distinct N3 tunnel end point address for the QoS Flow as described in clause M.1 of TS 23.501 \[2\].

The NG-RAN responds with a N2 SM information.

9\. The SMF/CUC determines the merged stream requirements in the TSN UNI towards the TN CNC as described in Annex M of TS 23.501 \[2\]. The TN CNC uses the merged stream requirements as input to select respective path(s) and calculate schedules in TN.

10\. Based on the results, the TN CNC provides a Status group that contains the merged end station communication-configuration back to the SMF/CUC.

11\. \[Conditional\] If the response from TN CNC includes InterfaceConfiguration, the SMF/CUC triggers the PDU Session Modification procedure as described in clause 4.3.3.2 to modify the QoS Flow to transfer the TSC streams.

12\. \[Conditional\] During the PDU Session Modification procedure, if the UPF supports CN-TL, the SMF/CUC invokes N4 Session Modification procedure and includes TL-Container(s) to the N4 Session Modification request including a set-request to the TL-Container as described in clause 5.28a.2 of TS 23.501 \[2\].

The UPF responds with a N4 Session Modification response. If the UPF supports CN-TL, the UPF includes a TL-Container to the response. The TL-Container includes a set-response as described in clause 5.28a.2 of TS 23.501 \[2\].

13\. \[Conditional\] During the PDU Session Modification procedure, if the NG-RAN supports AN-TL, the SMF/CUC invokes the Namf_Communication_N1N2MessageTransfer request. The SMF/CUC includes TL-Container(s) to the N2 SM information in the request, the TL-Container contains a set-request as described in clause 5.28a.2 of TS 23.501 \[2\]. The SMF/CUC may also update the TSCAI in the NG-RAN for the BAT in DL direction as described in Annex M, clause M.1 of TS 23.501 \[2\], if the SMF/CUC received a TimeAwareOffset or AccumulatedLatency from TN CNC for a downlink stream (i.e. for a Talker in the UPF/CN-TL) in step 7.

The NG-RAN responds with a N2 SM information. If the NG-RAN supports AN-TL, the NG-RAN includes TL-Container(s) to the N2 SM information. The TL-Container includes a set-response as described in clause 5.28a.2 of TS 23.501 \[2\].

NOTE: TL-Containers and related Gate Control information as described in clause M.1 of TS 23.501 \[2\] are removed during PDU Session Release or QoS Flow(s) Release.
