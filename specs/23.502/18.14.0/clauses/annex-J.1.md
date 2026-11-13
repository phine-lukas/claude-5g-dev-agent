# J.1 Procedure for PIN service

[figure]

Figure J.1-1: Procedure for PIN service

PIN is a subscribed service, and a user needs to coordinate with the Mobile Network Operator to subscribe for PIN service. When a user subscribes for a PIN, the subscription data includes the (DNN, S NSSAI) combination allocated by the MNO for the PIN service. The PEGC(s) are then provisioned with appropriate URSP rules to enable the PEGC UE to route the PIN traffic using the (DNN, S NSSAI) combination allocated for the PIN. Figure J.1-1 provides a high level procedure for PIN service.

Step 1: Step 1 is performed using O&M.

A user subscribes to the Mobile Network Operator (MNO) for PIN service. The user provides the list of PEGC(s) that are part of the PIN. The MNO verifies the request, performs necessary checks e.g. whether the UEs are allowed to act as PEGC, whether all the requested PEGC are part of the same UDM group etc. If the request is authorized by the MNO, the MNO:

\- allocates a dedicated (DNN, S NSSAI) combination for the PIN;

\- if the PIN has a single PEGC, then updates the PEGC subscription with the (DNN, S NSSAI) combination allocated for the PIN;

\- if the PIN has more than one PEGC and 5G VN Group is used for a PIN, then creates a group subscription following the 5G VN group management principles as specified in clause 5.29.2 of TS 23.501 \[2\]. The information on the External Group ID and associated (DNN, S-NSSAI) combination is provided to the AF for PIN;

\- if local switching is required, configures in the SMF set and/or in the NRF that the DNN allocated for the PIN is served by a specific SMF set.

NOTE: It is assumed that all PEGCs that are members of a PIN are part of the same UDM Group ID. If the PEGCs requested by the user for PIN creation are not part of the same UDM Group ID, the MNO migrates all the PEGCs into a single UDM Group ID for creating the group subscription.

Step 2: For routing PIN traffic by the PEGC, the AF for PIN provides guidance for URSP generation to the 5GC. The AF for PIN uses a UE ID (i.e. GPSI) as the target UE if the PIN contains a single PEGC. If the PIN contains more than one PEGC and 5G VN Group is used for a PIN, then the AF uses External Group ID as the target UEs for providing URSP guidance to the 5GC. The AF request contains (DNN, S NSSAI) combination allocated to the user for the PIN service and the traffic descriptor components in the URSP rule request from the AF for PIN contains the PIN ID.

The NEF authorizes the request received from the AF for PIN and stores the information in the UDR as "Application Data".

The NEF can use the procedure for authorization of service specific parameter provisioning as specified in clause 4.15.6.7a to authorize the AF request by the UDM. In this case:

\- if the request is for an individual UE, the UDM checks if the (DNN, S NSSAI) combination in the AF request is allowed for the UE;

\- if the request is for a group of UEs and 5G VN Group is used for a PIN, the UDM checks whether the group related data (e.g. (DNN, S-NSSAI) combination group related data, see table 4.15.6.3b-1) is authorized for the group.

If the AF request is authorized, the NEF stores the AF requested information in the UDR as the "Application Data" (Data Subset setting to "Service specific information").

Step 3: The PCF receives a Nudr_DM_Notify notification of data change from the UDR, generates the URSP rules and initiates UE Policy delivery as specified in clause 4.2.4.3 to provision the URSP rules in the PEGC(s). For routing of PIN traffic by the PEGC(s), the URSP policies provided to the PEGC UE(s) contain URSP rule with PIN ID as traffic descriptor.

Step 4: The AF for PIN provides QoS requirements for the PIN traffic following procedures for AF requested QoS for a UE or group of UEs not identified by a UE address as specified in clause 4.15.6.14.

Step 5: When the PEGC(s) detect PIN traffic, it uses the provisioned URSP rules to identify PDU session to route the traffic as specified in clause 6.6.2.3 of TS 23.503 \[20\]. The 5GC further performs session management and user plane management as described in Annex P, clause P.2 of TS 23.501 \[2\].

When 5G VN Group is not used for a PIN and if the PIN contains more than one PEGCs, then the AF request for URSP guidance and QoS requirements is targeted to each individual PEGCs that are part of the PIN.

########  Annex K (informative): Change history

<!-- table -->
| Change history (x8) |
| Date | Meeting | TDoc | CR | Rev | Cat | Subject/Comment | New version |
| 2017-09 | SP#77 | SP-170735 | - | - | - | MCC Editorial Update for presentation to TSG SA#77 for information | 1.0.0 |
| 2017-09 | SA2#122E |  |  |  |  | Correcting implementation issues of S2-176821 and additional clean-up. | 1.2.0 |
| 2017-12 | SP-78 | SP-170932 | - | - | - | MCC Editorial Update for presentation to TSG SA#78 for Approval | 2.0.0 |
| 2017-12 | SP-78 | - | - | - | - | MCC Editorial Update after TSG SA#78 Approval | 15.0.0 |
| 2018-03 | SP-79 | SP-180092 | 0001 | 5 | F | Corrections on the specification of Network Exposure services | 15.1.0 |
| 2018-03 | SP-79 | SP-180101 | 0002 | 2 | F | Corrections to PDU session establishment / modification procedure | 15.1.0 |
| 2018-03 | SP-79 | SP-180101 | 0003 | 1 | F | Clean-up of the registration procedure | 15.1.0 |
| 2018-03 | SP-79 | SP-180090 | 0005 | 3 | F | Using NRF for UPF discovery | 15.1.0 |
| 2018-03 | SP-79 | SP-180101 | 0006 | 4 | F | Allowed NSSAI and Access Type | 15.1.0 |
| 2018-03 | SP-79 | SP-180101 | 0008 | 2 | F | Corrections to the Inter-system mobility procedures | 15.1.0 |
| 2018-03 | SP-79 | SP-180101 | 0009 | 1 | F | QoS clarifications for EPC interworking | 15.1.0 |
| 2018-03 | SP-79 | SP-180101 | 0010 | - | F | EPS bearer ID allocation update | 15.1.0 |
| 2018-03 | SP-79 | SP-180090 | 0011 | 1 | F | Correction of Npcf_BDTPolicyControl service operation (Backbround data transfer) | 15.1.0 |
| 2018-03 | SP-79 | SP-180095 | 0012 | - | C | Multiple request of Location Reporting for Area of Interest | 15.1.0 |
| 2018-03 | SP-79 | SP-180101 | 0013 | 1 | F | SMF behaviour based on LADN notification | 15.1.0 |
| 2018-03 | SP-79 | SP-180101 | 0014 | - | F | Clarification on Internal Event Exposure | 15.1.0 |
| 2018-03 | SP-79 | SP-180101 | 0015 | - | F | Clarification on 5G-GUTI in EPS to 5GS Mobility Registration Procedure using N26 | 15.1.0 |
| 2018-03 | SP-79 | SP-180101 | 0016 | - | F | Adding missing text about UE policies related to Service Request including the List Of Allowed PDU Sessions | 15.1.0 |
| 2018-03 | SP-79 | SP-180101 | 0019 | 1 | F | Update of NEF service for background data transfer | 15.1.0 |
| 2018-03 | SP-79 | SP-180101 | 0020 | 1 | F | Update of NEF service for PFD management | 15.1.0 |
| 2018-03 | SP-79 | SP-180101 | 0021 | - | F | Clarification on handover applicability between 3GPP and non-3GPP accesses | 15.1.0 |
| 2018-03 | SP-79 | SP-180101 | 0022 | - | F | Clarification on paging when it is related with both 3GPP and non-3GPP PDU Session | 15.1.0 |
| 2018-03 | SP-79 | SP-180101 | 0023 | 1 | F | Sending EBI to the NG-RAN | 15.1.0 |
| 2018-03 | SP-79 | SP-180101 | 0024 | 1 | F | Indirect data forwarding in home routed roaming case | 15.1.0 |
| 2018-03 | SP-79 | SP-180101 | 0025 | 1 | F | Interaction between SMF and UPF during the inter-system change | 15.1.0 |
| 2018-03 | SP-79 | SP-180101 | 0026 | 1 | F | Direct forwarding flag for handover from EPS to 5GS | 15.1.0 |
| 2018-03 | SP-79 | SP-180101 | 0027 | 1 | F | Update to N2 Handover procedure | 15.1.0 |
| 2018-03 | SP-79 | SP-180101 | 0029 | 1 | F | Clarification on keeping NAS signalling connection | 15.1.0 |
| 2018-03 | SP-79 | SP-180093 | 0030 | 1 | F | Clarification on SMS related Subscription data | 15.1.0 |
| 2018-03 | SP-79 | SP-180101 | 0032 | - | F | Clarification related to Subscription data type | 15.1.0 |
| 2018-03 | SP-79 | SP-180101 | 0033 | 2 | F | Clarification on PCF association | 15.1.0 |
| 2018-03 | SP-79 | SP-180101 | 0034 | - | F | Slicing handling for EPS to 5GS Mobility without N26 | 15.1.0 |
| 2018-03 | SP-79 | SP-180101 | 0035 | - | F | Keeping EBI transfer alignment | 15.1.0 |
| 2018-03 | SP-79 | SP-180101 | 0036 | - | F | Clarification on the Emergency HO indication for EPS fallback | 15.1.0 |
| 2018-03 | SP-79 | SP-180102 | 0037 | - | F | Alignment of Namf_MT_EnableUEReachability service operation | 15.1.0 |
| 2018-03 | SP-79 | SP-180102 | 0038 | - | F | Mobility from EPC to 5GC | 15.1.0 |
| 2018-03 | SP-79 | SP-180095 | 0040 | - | C | Clarification on PDU Session Release timer provided to the UE for 'SSC mode 3' | 15.1.0 |
| 2018-03 | SP-79 | SP-180102 | 0041 | 1 | F | Generalize exposure of Mobility Events from AMF | 15.1.0 |
| 2018-03 | SP-79 | SP-180102 | 0042 | 2 | F | Align the UE location presence status of LADN Session into Network Triggered Service Request procedure | 15.1.0 |
| 2018-03 | SP-79 | SP-180102 | 0043 | - | F | Correction on AF influence on traffic routing | 15.1.0 |
| 2018-03 | SP-79 | SP-180102 | 0044 | - | F | Correction to RAN Initiated QoS Flow Mobility Procedure for Dual Connectivity | 15.1.0 |
| 2018-03 | SP-79 | SP-180102 | 0045 | - | F | Clarification on UDM service consumption order of UECM and SDM | 15.1.0 |
| 2018-03 | SP-79 | SP-180102 | 0046 | - | F | Cleanup of the service request procedure | 15.1.0 |
| 2018-03 | SP-79 | SP-180091 | 0047 | - | F | UE-specific DRX parameter negotiation between UE and AMF | 15.1.0 |
| 2018-03 | SP-79 | SP-180102 | 0048 | - | F | Update of handover cancel procedure | 15.1.0 |
| 2018-03 | SP-79 | SP-180091 | 0049 | 1 | F | Control of the Messages triggering Paging at AMF | 15.1.0 |
| 2018-03 | SP-79 | SP-180102 | 0050 | - | F | Clarification for Area of validity in NW triggered SR procedure | 15.1.0 |
| 2018-03 | SP-79 | SP-180091 | 0051 | 2 | F | Revision on Service Request procedure | 15.1.0 |
| 2018-03 | SP-79 | SP-180093 | 0052 | 1 | F | Correction on Notification control for GBR QoS flow | 15.1.0 |
| 2018-03 | SP-79 | SP-180093 | 0053 | - | F | Reflective QoS Timer transmission during PDU Session establishment | 15.1.0 |
| 2018-03 | SP-79 | SP-180102 | 0054 | - | F | Correction on Policy association procedure during AMF relocation | 15.1.0 |
| 2018-03 | SP-79 | SP-180102 | 0055 | - | F | PCF selection for AMF during inter NG-RAN node N2 based handover | 15.1.0 |
| 2018-03 | SP-79 | SP-180102 | 0056 | 1 | F | Correction on PCF selection in SMF | 15.1.0 |
| 2018-03 | SP-79 | SP-180091 | 0057 | - | F | Update Paging Policy Differentiation in Network triggered Service Request procedure | 15.1.0 |
| 2018-03 | SP-79 | SP-180102 | 0058 | 3 | F | NEF service definitions for AF influence | 15.1.0 |
| 2018-03 | SP-79 | SP-180102 | 0059 | 2 | F | Update Handover procedures in clause 4.11.1.2 | 15.1.0 |
| 2018-03 | SP-79 | SP-180102 | 0060 | 2 | F | Clean up of FFSs in 4.11.1.2.2 | 15.1.0 |
| 2018-03 | SP-79 | SP-180102 | 0061 | 3 | F | A new annex for generating EPS PDN Connection parameters from 5G PDU Session parameters | 15.1.0 |
| 2018-03 | SP-79 | SP-180102 | 0062 | - | F | SMSF address deactivation and activation in AMF | 15.1.0 |
| 2018-03 | SP-79 | SP-180102 | 0063 | - | F | Correction on SMSF Nsmsf_SMService_Activate service operation | 15.1.0 |
| 2018-03 | SP-79 | SP-180102 | 0065 | - | F | Resolution of ENs in Service Request procedures | 15.1.0 |
| 2018-03 | SP-79 | SP-180096 | 0066 | - | D | Editorial correction to clause 4.12.8 | 15.1.0 |
| 2018-03 | SP-79 | SP-180102 | 0067 | - | F | Nudm SDM service Subscription Data types updates | 15.1.0 |
| 2018-03 | SP-79 | SP-180102 | 0068 | - | F | Replace PUI with GPSI | 15.1.0 |
| 2018-03 | SP-79 | SP-180102 | 0069 | - | F | Traffic mapping information that disallows UL packets | 15.1.0 |
| 2018-03 | SP-79 | SP-180093 | 0070 | 1 | F | Add Nocs_SpendingLimitControl service, service operations and information flows | 15.1.0 |
| 2018-03 | SP-79 | SP-180102 | 0071 | - | F | Correction/cleanup of IMS Emergency support | 15.1.0 |
| 2018-03 | SP-79 | SP-180091 | 0072 | - | F | Idle and connected state terminology cleanup | 15.1.0 |
| 2018-03 | SP-79 | SP-180102 | 0073 | 1 | F | LCS Correction of identities | 15.1.0 |
| 2018-03 | SP-79 | SP-180103 | 0074 | - | F | Slice selection cleanup | 15.1.0 |
| 2018-03 | SP-79 | SP-180103 | 0075 | 1 | F | Proposed resolution of Editor's Notes on clause 4.16 | 15.1.0 |
| 2018-03 | SP-79 | SP-180103 | 0076 | 1 | F | Alignment of terminology and general cleanup | 15.1.0 |
| 2018-03 | SP-79 | SP-180103 | 0078 | 1 | F | Application Trigger procedure updates | 15.1.0 |
| 2018-03 | SP-79 | SP-180103 | 0079 | - | F | Specification of AN Parameters for Non-3GPP Access | 15.1.0 |
| 2018-03 | SP-79 | SP-180103 | 0080 | - | F | Clarifying inclusion of TAU messages in Registration Request | 15.1.0 |
| 2018-03 | SP-79 | SP-180103 | 0082 | 2 | F | Call flow for the PDU session setup for emergency with Emergency Service Support indicator | 15.1.0 |
| 2018-03 | SP-79 | SP-180103 | 0083 | 1 | F | NF Service Discovery | 15.1.0 |
| 2018-03 | SP-79 | SP-180103 | 0085 | 1 | F | Update 5GS and EPS handover procedures | 15.1.0 |
| 2018-03 | SP-79 | SP-180103 | 0087 | 1 | F | Operation type in Nsmf_PDUSession_UpdateSMContext Request | 15.1.0 |
| 2018-03 | SP-79 | SP-180103 | 0088 | 1 | F | Corrections of PDU session establishment procedure | 15.1.0 |
| 2018-03 | SP-79 | SP-180103 | 0089 | 1 | F | Correction on Secondary authorization/authentication procedure | 15.1.0 |
| 2018-03 | SP-79 | SP-180103 | 0090 | 1 | F | N4 reporting for PDU Session Inactivity | 15.1.0 |
| 2018-03 | SP-79 | SP-180103 | 0091 | 1 | F | Update PDU Session Modification procedures | 15.1.0 |
| 2018-03 | SP-79 | SP-180103 | 0092 | 1 | F | Correction on DNN management | 15.1.0 |
| 2018-03 | SP-79 | SP-180103 | 0094 | 1 | F | Mobility Restrictions when Roaming | 15.1.0 |
| 2018-03 | SP-79 | SP-180103 | 0097 | 1 | F | Change to Required Inputs for Update service operation | 15.1.0 |
| 2018-03 | SP-79 | SP-180103 | 0098 | 3 | F | Delivery of UE Access and PDU session related information by the PCF to the UE | 15.1.0 |
| 2018-03 | SP-79 | SP-180093 | 0099 | 3 | F | Interworking without N26 corrections | 15.1.0 |
| 2018-03 | SP-79 | SP-180103 | 0100 | 1 | F | Different Corrections of text and references | 15.1.0 |
| 2018-03 | SP-79 | SP-180103 | 0101 | 2 | F | Cleaning up binding in BSF after PDU session termination | 15.1.0 |
| 2018-03 | SP-79 | SP-180103 | 0104 | 1 | F | Updates of NSSF Services | 15.1.0 |
| 2018-03 | SP-79 | SP-180090 | 0105 | 4 | F | Selection mode transfer over N11 and N16 (wildcard DNN) | 15.1.0 |
| 2018-03 | SP-79 | SP-180103 | 0106 | 7 | F | Update to PCF-SMF interface ( Npcf_SMPolicyControl service) | 15.1.0 |
| 2018-03 | SP-79 | SP-180092 | 0107 | 1 | F | Correcting the support of charging Characteristics | 15.1.0 |
| 2018-03 | SP-79 | SP-180103 | 0108 | 1 | F | Handling of mapped EPS QoS parameters in IWK with EPC | 15.1.0 |
| 2018-03 | SP-79 | SP-180103 | 0109 | 3 | F | Alignment of non-3GPP &amp; 3GPP registration procedures | 15.1.0 |
| 2018-03 | SP-79 | SP-180090 | 0110 | 1 | F | Network sharing PLMN handling | 15.1.0 |
| 2018-03 | SP-79 | SP-180103 | 0111 | 3 | F | Move 5GS related impact from TS 23.401 to TS 23.502 | 15.1.0 |
| 2018-03 | SP-79 | SP-180104 | 0112 | - | F | Fixes for Emergency Services using Fallback procedure | 15.1.0 |
| 2018-03 | SP-79 | SP-180104 | 0113 | 1 | F | Fixes for UDM/UDR services | 15.1.0 |
| 2018-03 | SP-79 | SP-180104 | 0114 | 1 | F | EPS Interworking - Fixes for 5GS to EPS Mobility | 15.1.0 |
| 2018-03 | SP-79 | SP-180104 | 0115 | 1 | F | EPS Interworking - EPS Bearer ID allocation for HR session | 15.1.0 |
| 2018-03 | SP-79 | SP-180104 | 0116 | 1 | F | EPS Interworking - Fixes for 5GS-&gt;EPS HO | 15.1.0 |
| 2018-03 | SP-79 | SP-180104 | 0117 | 1 | F | EPS Interworking - Fixes for EPS-&gt;5GS HO | 15.1.0 |
| 2018-03 | SP-79 | SP-180104 | 0118 | 2 | F | EPS Interworking - Fixes for EPS to 5GS Mobility | 15.1.0 |
| 2018-03 | SP-79 | SP-180104 | 0121 | 1 | F | Update Nnrf_NFDiscovery service based on the UE IP address | 15.1.0 |
| 2018-03 | SP-79 | SP-180104 | 0122 | 3 | F | Update of Npcf_SMPolicyControl service | 15.1.0 |
| 2018-03 | SP-79 | SP-180104 | 0125 | 3 | F | Update to PCF-AMF interface and Npcf_AMPolicyControl service | 15.1.0 |
| 2018-03 | SP-79 | SP-180104 | 0127 | 1 | F | Correction on 5GS to EPS handover using N26 interface | 15.1.0 |
| 2018-03 | SP-79 | SP-180104 | 0128 | 2 | F | Nudm SDM service operations input parameter update | 15.1.0 |
| 2018-03 | SP-79 | SP-180092 | 0129 | 2 | F | Nudr_DM service operations input parameter update | 15.1.0 |
| 2018-03 | SP-79 | SP-180104 | 0131 | - | F | Nudm_SDM 'Access and Mobility Subscription data' update | 15.1.0 |
| 2018-03 | SP-79 | SP-180104 | 0132 | 1 | F | MME and AMF registration in HSS+UDM | 15.1.0 |
| 2018-03 | SP-79 | SP-180104 | 0136 | - | F | Clarification on SMSF registration/deregistration with UDM | 15.1.0 |
| 2018-03 | SP-79 | SP-180104 | 0137 | 1 | F | Clarification on AMF registration with UDM for Registration procedure for untrusted non-3GPP access | 15.1.0 |
| 2018-03 | SP-79 | SP-180104 | 0138 | 2 | F | Clarification on Location reporting procedures | 15.1.0 |
| 2018-03 | SP-79 | SP-180104 | 0139 | 1 | F | Correction to handovers between 3GPP and non-3GPP | 15.1.0 |
| 2018-03 | SP-79 | SP-180104 | 0140 | 1 | F | Clarification and alignment on the NG-RAN behavoir for EPS/RAT fallback | 15.1.0 |
| 2018-03 | SP-79 | SP-180104 | 0142 | 2 | F | Clarification on how the AMF initiates inter or intra system handover to E-UTRAN connect to both EPC and 5GC. | 15.1.0 |
| 2018-03 | SP-79 | SP-180104 | 0143 | 1 | F | Clarification on the SM EPS bearer context from v-SMF | 15.1.0 |
| 2018-03 | SP-79 | SP-180104 | 0144 | 1 | F | Modification on the EBI revocation and ARP change | 15.1.0 |
| 2018-03 | SP-79 | SP-180104 | 0147 | - | F | Fixing the wrong usage of 'relocation' | 15.1.0 |
| 2018-03 | SP-79 | SP-180104 | 0148 | - | F | Corrections to NRF and NSSF services | 15.1.0 |
| 2018-03 | SP-79 | SP-180104 | 0149 | 1 | F | Correction of handover procedure from 4G to 5G in Single Registration mode | 15.1.0 |
| 2018-03 | SP-79 | SP-180105 | 0151 | - | F | Correction to UE Registration | 15.1.0 |
| 2018-03 | SP-79 | SP-180105 | 0152 | - | F | Corrections to SMF selection | 15.1.0 |
| 2018-03 | SP-79 | SP-180092 | 0153 | 1 | F | UE support for Multi-homed IPv6 PDU Session | 15.1.0 |
| 2018-03 | SP-79 | SP-180105 | 0154 | - | F | Adding the missing GPSI parameter in SMF | 15.1.0 |
| 2018-03 | SP-79 | SP-180105 | 0155 | 2 | F | Transparent relay between V-SMF and H-SMF in case of different feature support | 15.1.0 |
| 2018-03 | SP-79 | SP-180105 | 0156 | - | F | Preservation of GBR QoS Flows upon redirection | 15.1.0 |
| 2018-03 | SP-79 | SP-180093 | 0157 | 2 | F | Handling of UE Core Network Capability and indication of UE support for Handover Attach to NG-RAN | 15.1.0 |
| 2018-03 | SP-79 | SP-180105 | 0158 | 3 | F | Clarification on NSSAI configuration | 15.1.0 |
| 2018-03 | SP-79 | SP-180093 | 0159 | 1 | F | UE assisted UE policies calculation in PCF | 15.1.0 |
| 2018-03 | SP-79 | SP-180105 | 0160 | 1 | F | Correction of used Registration Type | 15.1.0 |
| 2018-03 | SP-79 | SP-180105 | 0163 | 1 | F | Re-use of definitions and abbreviations specified in TS 23.503. | 15.1.0 |
| 2018-03 | SP-79 | SP-180105 | 0166 | 1 | F | Correction to the UE Requested PDU Session Establishment via Untrusted non-3GPP Access Procedure | 15.1.0 |
| 2018-03 | SP-79 | SP-180105 | 0167 | 1 | F | Correction for UE location in Xn based HO procedure | 15.1.0 |
| 2018-03 | SP-79 | SP-180105 | 0168 | 3 | F | Clarification of UDR usage in policy related procedures | 15.1.0 |
| 2018-03 | SP-79 | SP-180105 | 0170 | 2 | F | Correction of UDR usage in MM related procedures | 15.1.0 |
| 2018-03 | SP-79 | SP-180105 | 0171 | 2 | F | Correction of UDR usage in specific service related procedures | 15.1.0 |
| 2018-03 | SP-79 | SP-180105 | 0172 | 2 | F | Correction for the invocation of Nudm_UECM_Deregistration service operation | 15.1.0 |
| 2018-03 | SP-79 | SP-180105 | 0175 | 2 | F | Correction of UDR usage in SM related procedures | 15.1.0 |
| 2018-03 | SP-79 | SP-180105 | 0176 | 1 | F | Clarification on handover procedure for home-routed roaming scenario | 15.1.0 |
| 2018-03 | SP-79 | SP-180105 | 0177 | - | F | Correction to inter NG-RAN node N2 based handover | 15.1.0 |
| 2018-03 | SP-79 | SP-180105 | 0179 | 1 | F | Correction on N4 Session Modification Request in Handover procedure | 15.1.0 |
| 2018-03 | SP-79 | SP-180105 | 0180 | 1 | F | Correction on Service Request procedure when UE establishes a signalling connection only | 15.1.0 |
| 2018-03 | SP-79 | SP-180105 | 0181 | 1 | F | Clarify how to send end marker during HO procedure | 15.1.0 |
| 2018-03 | SP-79 | SP-180105 | 0183 | - | F | Aligning TS 23.502 onto TS 29.244 about PPD. | 15.1.0 |
| 2018-03 | SP-79 | SP-180092 | 0184 | 2 | F | User plane security policy | 15.1.0 |
| 2018-03 | SP-79 | SP-180105 | 0185 | - | F | Service Request procedure corrections | 15.1.0 |
| 2018-03 | SP-79 | SP-180105 | 0186 | 1 | F | New cause for UP reactivation failure in Service Request procedure | 15.1.0 |
| 2018-03 | SP-79 | SP-180105 | 0187 | 2 | F | Rejection of UP activation during the Registration procedure | 15.1.0 |
| 2018-03 | SP-79 | SP-180105 | 0188 | 2 | F | Activating a Background Data Transfer Policy | 15.1.0 |
| 2018-03 | SP-79 | SP-180106 | 0189 | 1 | F | P-CSCF Discovery for IMS in 5GC using IP-CAN method | 15.1.0 |
| 2018-03 | SP-79 | SP-180106 | 0191 | - | F | Clarification on modification of the set of network slices for a UE | 15.1.0 |
| 2018-03 | SP-79 | SP-180106 | 0192 | 1 | F | Location reporting procedure for LADN in RRC Inactive state - TS 23.502 | 15.1.0 |
| 2018-03 | SP-79 | SP-180106 | 0193 | 3 | F | Exposure of Mobility Events from AMF | 15.1.0 |
| 2018-03 | SP-79 | SP-180106 | 0195 | 1 | F | Clarification on AMF behaviour due to Subscriber Data Change in UDM | 15.1.0 |
| 2018-03 | SP-79 | SP-180095 | 0199 | 1 | B | Supporting 3GPP PS Data Off in 5GS | 15.1.0 |
| 2018-03 | SP-79 | SP-180106 | 0203 | 1 | F | Clarifications on EPS to 5GS handover procedure using N26 | 15.1.0 |
| 2018-03 | SP-79 | SP-180106 | 0204 | 1 | F | Request Type in PDN connectivity request for SRM interworking | 15.1.0 |
| 2018-03 | SP-79 | SP-180106 | 0205 | 1 | F | Alignment CR for Application Function influence on traffic routing procedure | 15.1.0 |
| 2018-03 | SP-79 | SP-180106 | 0206 | 1 | F | PDU session ID in PDU session management procedure | 15.1.0 |
| 2018-03 | SP-79 | SP-180106 | 0209 | 1 | F | UE context removal in UDM during deregistration procedure | 15.1.0 |
| 2018-03 | SP-79 | SP-180096 | 0210 | 1 | D | Correction on non-3GPP Service request procedure | 15.1.0 |
| 2018-03 | SP-79 | SP-180106 | 0211 | 2 | F | Indication for Non-geographically selected AMF | 15.1.0 |
| 2018-03 | SP-79 | SP-180106 | 0212 | 1 | F | Updating Network Triggered Service Request to support selective re-activation of PDU session over non-3GPP access | 15.1.0 |
| 2018-03 | SP-79 | SP-180106 | 0213 | 1 | F | Editorial corrections in clause 4.2.3.3 Network Triggered Service Request | 15.1.0 |
| 2018-03 | SP-79 | SP-180090 | 0215 | 1 | F | Capturing impacts to 23.401 procedure for interworking with 5GC | 15.1.0 |
| 2018-03 | SP-79 | SP-180106 | 0216 | 1 | F | Clean up for PCC related flows | 15.1.0 |
| 2018-03 | SP-79 | SP-180106 | 0219 | - | F | Editorial modifications in procedures related to PDU session anchor addition or removal | 15.1.0 |
| 2018-03 | SP-79 | SP-180106 | 0223 | 1 | F | S-NSSAI in the PDU Session Establishment Accept for roaming scenario | 15.1.0 |
| 2018-03 | SP-79 | SP-180106 | 0226 | - | F | Clarification on Nnwdaf_EventsSubscription_Unsubscribe service operation | 15.1.0 |
| 2018-03 | SP-79 | SP-180106 | 0227 | - | F | Clarification on Network data analytics procedure | 15.1.0 |
| 2018-03 | SP-79 | SP-180106 | 0228 | 2 | F | Slicing configuration update | 15.1.0 |
| 2018-03 | SP-79 | SP-180125 | 0229 | 1 | B | Addition of PDU Session type IPv4v6 | 15.1.0 |
| 2018-03 | SP-79 | SP-180106 | 0230 | 1 | F | Update of Reachability procedures | 15.1.0 |
| 2018-03 | SP-79 | SP-180093 | 0234 | 2 | C | EPS Fallback for voice further enhancements | 15.1.0 |
| 2018-03 | SP-79 | SP-180106 | 0235 | 1 | F | Clarification on Use of List of Parameter Values to Match in Event Filters | 15.1.0 |
| 2018-03 | SP-79 | SP-180106 | 0236 | 2 | F | Clarification on the services for External Parameter Provisioning | 15.1.0 |
| 2018-03 | SP-79 | SP-180106 | 0237 | - | F | Correction to PDU Session Establishment procedure | 15.1.0 |
| 2018-03 | SP-79 | SP-180106 | 0238 | 1 | F | EPS bearer context handling for N26 case | 15.1.0 |
| 2018-06 | SP-80 | SP-180491 | 0182 | 3 | F | TS 23.502: Xn handover and slice unavailability | 15.2.0 |
| 2018-06 | SP-80 | SP-180482 | 0241 | 1 | F | Correction of description related to PFD management | 15.2.0 |
| 2018-06 | SP-80 | SP-180484 | 0245 | - | F | Deregistration procedure correction | 15.2.0 |
| 2018-06 | SP-80 | SP-180480 | 0247 | 1 | F | Clarification on NG-RAN location reporting procedure | 15.2.0 |
| 2018-06 | SP-80 | SP-180489 | 0249 | - | F | TS 23.502: Perform authentication before Context Acknowledgement during 5GS to EPS Idle mode mobility using N26 interface | 15.2.0 |
| 2018-06 | SP-80 | SP-180482 | 0251 | 6 | F | Correction of UE configuration update procedure | 15.2.0 |
| 2018-06 | SP-80 | SP-180481 | 0254 | 2 | F | Clarifications on Nudr interactions between PCF and UDR | 15.2.0 |
| 2018-06 | SP-80 | SP-180484 | 0255 | - | F | Editorial corrections | 15.2.0 |
| 2018-06 | SP-80 | SP-180484 | 0258 | 1 | F | EPS to 5GS Mobility - Handling PDN connections that are not subject to service continuity | 15.2.0 |
| 2018-06 | SP-80 | SP-180487 | 0259 | 1 | F | P-GW-C+SMF Registration in the UDM for the purpose of EPS interworking | 15.2.0 |
| 2018-06 | SP-80 | SP-180482 | 0261 | 1 | F | Context retrieval for the purpose of EPS interworking | 15.2.0 |
| 2018-06 | SP-80 | SP-180491 | 0262 | - | F | Voice fallback during roaming scenarios | 15.2.0 |
| 2018-06 | SP-80 | SP-180486 | 0263 | 1 | F | NF Discovery via the NRF | 15.2.0 |
| 2018-06 | SP-80 | SP-180487 | 0265 | - | F | Nudm_UEAuthentication Service clarification | 15.2.0 |
| 2018-06 | SP-80 | SP-180483 | 0266 | - | D | Correction to figure caption errors in handover procedures | 15.2.0 |
| 2018-06 | SP-80 | SP-180479 | 0268 | 3 | F | Propose to add the network Requested PDU Session Release procedure via Untrusted non-3GPP access | 15.2.0 |
| 2018-06 | SP-80 | SP-180483 | 0269 | - | F | Correction to NEF service | 15.2.0 |
| 2018-06 | SP-80 | SP-180481 | 0270 | 2 | F | Clarify related description for Network Sharing and Interworking | 15.2.0 |
| 2018-06 | SP-80 | SP-180481 | 0271 | 2 | F | Clarifications to Registration and UE triggered Service Request procedure | 15.2.0 |
| 2018-06 | SP-80 | SP-180489 | 0273 | 1 | F | The interaction between PCF and AF | 15.2.0 |
| 2018-06 | SP-80 | SP-180480 | 0274 | 1 | F | Clarification on MT SMS domain selection by SMSF | 15.2.0 |
| 2018-06 | SP-80 | SP-180483 | 0275 | 2 | F | Correction to CN-initiated selective deactivation of UP connection of an existing PDU Session | 15.2.0 |
| 2018-06 | SP-80 | SP-180479 | 0276 | 3 | F | Clarification of the mapping releation between PDU session ID and access type in the AMF. | 15.2.0 |
| 2018-06 | SP-80 | SP-180489 | 0277 | 1 | F | TS 23.502: Clean-up for the RRC Inactive related procedure | 15.2.0 |
| 2018-06 | SP-80 | SP-180482 | 0279 | 2 | F | Cleanup to PCF selection in AMF and SMF | 15.2.0 |
| 2018-06 | SP-80 | SP-180484 | 0280 | 1 | F | Description of Policy Association | 15.2.0 |
| 2018-06 | SP-80 | SP-180489 | 0281 | 2 | F | Wildcard DNN management | 15.2.0 |
| 2018-06 | SP-80 | SP-180479 | 0284 | - | F | Clarification on HO procedure | 15.2.0 |
| 2018-06 | SP-80 | SP-180479 | 0285 | - | F | Clarification of Data Notification in service request procedure | 15.2.0 |
| 2018-06 | SP-80 | SP-180484 | 0286 | 5 | F | Correlation between EBI and QFI | 15.2.0 |
| 2018-06 | SP-80 | SP-180479 | 0287 | 3 | F | Clarification on Data Keys for Application data | 15.2.0 |
| 2018-06 | SP-80 | SP-180491 | 0288 | 1 | F | Updates on Subscribe Service Operation | 15.2.0 |
| 2018-06 | SP-80 | SP-180489 | 0289 | - | F | Alignment on the IMS voice over PS session supported indication | 15.2.0 |
| 2018-06 | SP-80 | SP-180480 | 0290 | 1 | F | Clarification on RAT fallback | 15.2.0 |
| 2018-06 | SP-80 | SP-180479 | 0293 | - | F | Clarification on AMF deregistration by UDM in N26 based interworking from 5GS to EPS | 15.2.0 |
| 2018-06 | SP-80 | SP-180480 | 0296 | - | F | Clarification on Network-initiated Deregistration | 15.2.0 |
| 2018-06 | SP-80 | SP-180488 | 0297 | - | F | Selective deactivation of UP connection for non-3GPP PDU Session | 15.2.0 |
| 2018-06 | SP-80 | SP-180485 | 0300 | 5 | F | Lack of S-NSSAI or DNN in the PDU Session Establishment Request | 15.2.0 |
| 2018-06 | SP-80 | SP-180485 | 0302 | 1 | F | Interactions with the DN-AAA that are not for authentication | 15.2.0 |
| 2018-06 | SP-80 | SP-180481 | 0303 | 1 | F | Clarification to handling of packet filters at PDU Session Modification | 15.2.0 |
| 2018-06 | SP-80 | SP-180485 | 0304 | 1 | F | LADN Signalling to SMF | 15.2.0 |
| 2018-06 | SP-80 | SP-180484 | 0305 | 2 | F | Corrections on UE configuration update procedure. | 15.2.0 |
| 2018-06 | SP-80 | SP-180482 | 0308 | 2 | F | CN tunnel handling during IRAT handover | 15.2.0 |
| 2018-06 | SP-80 | SP-180489 | 0310 | 1 | F | Subscription status notification for Event Exposure service | 15.2.0 |
| 2018-06 | SP-80 | SP-180487 | 311 | 1 | F | Removal of editor's notes in clause 4.12 | 15.2.0 |
| 2018-06 | SP-80 | SP-180480 | 0312 | - | F | Clarification on SMF selection | 15.2.0 |
| 2018-06 | SP-80 | SP-180480 | 0313 | 2 | F | Clarification on policy provision in roaming case | 15.2.0 |
| 2018-06 | SP-80 | SP-180479 | 0317 | 1 | F | Authentication related services. | 15.2.0 |
| 2018-06 | SP-80 | SP-180486 | 0318 | 5 | F | Network slicing information as the service input parameter of BSF service operations | 15.2.0 |
| 2018-06 | SP-80 | SP-180490 | 0319 | 1 | F | Mobility Event Subscribe Service operation correction | 15.2.0 |
| 2018-06 | SP-80 | SP-180491 | 0320 | 6 | F | Update on AMF service operation to support query for terminating domain selection for IMS voice | 15.2.0 |
| 2018-06 | SP-80 | SP-180483 | 0322 |  | F | Correction on Nsmsf_SMService_Activate service operation | 15.2.0 |
| 2018-06 | SP-80 | SP-180482 | 0323 | 1 | F | Correction of Provision parameters flow | 15.2.0 |
| 2018-06 | SP-80 | SP-180482 | 0325 | 2 | F | Consolidation of UE Network Capabilities | 15.2.0 |
| 2018-06 | SP-80 | SP-180488 | 0326 | - | F | Removal of one step SMS procedure | 15.2.0 |
| 2018-06 | SP-80 | SP-180481 | 0327 | 1 | F | Clarifications on Nudr interactions between PCF and UDR | 15.2.0 |
| 2018-06 | SP-80 | SP-180491 | 0328 | 2 | F | Update Nudr_DataManagement (DM) service for data subscription | 15.2.0 |
| 2018-06 | SP-80 | SP-180489 | 0329 | - | F | Terminology cleanup | 15.2.0 |
| 2018-06 | SP-80 | SP-180484 | 0331 | 1 | F | Corrections to Service Request procedure | 15.2.0 |
| 2018-06 | SP-80 | SP-180481 | 0334 | 1 | F | Clarification on the use of shared AMF Pointer value | 15.2.0 |
| 2018-06 | SP-80 | SP-180480 | 0335 | 3 | F | Clarification on NGAP UE-TNLA-binding per UE Release procedure | 15.2.0 |
| 2018-06 | SP-80 | SP-180488 | 0336 | 1 | F | ReAuthentication by an external DN-AAA server | 15.2.0 |
| 2018-06 | SP-80 | SP-180491 | 0337 | 5 | F | Updates to SMF Event Exposure | 15.2.0 |
| 2018-06 | SP-80 | SP-180487 | 0340 | 1 | F | Policy related update in the PDU Session Establishment procedure | 15.2.0 |
| 2018-06 | SP-80 | SP-180488 | 0341 | 1 | F | Remove PCF as the consumer of Namf_EventExposure and Nsmf_EventExposure services | 15.2.0 |
| 2018-06 | SP-80 | SP-180485 | 0342 | 3 | F | Indirect Data forwarding for N2 HO | 15.2.0 |
| 2018-06 | SP-80 | SP-180486 | 0345 | 1 | F | N4 modification inserted during PDU Session Modification procedure | 15.2.0 |
| 2018-06 | SP-80 | SP-180490 | 0347 | - | F | Update of PDU Session Establishment Procedure | 15.2.0 |
| 2018-06 | SP-80 | SP-180483 | 0349 |  | F | Correction to N2 handover preparation | 15.2.0 |
| 2018-06 | SP-80 | SP-180488 | 0352 | 2 | F | Setting indirect data forwarding flag | 15.2.0 |
| 2018-06 | SP-80 | SP-180478 | 0353 | - | F | 23.502: Alignment of terminologies regarding PDU Session | 15.2.0 |
| 2018-06 | SP-80 | SP-180489 | 0354 | 2 | F | TS 23.502 Clarification on Internal-Group identifier | 15.2.0 |
| 2018-06 | SP-80 | SP-180489 | 0355 | 2 | F | TS 23.502 Clarification on Access and mobility related policy | 15.2.0 |
| 2018-06 | SP-80 | SP-180489 | 0356 | 1 | F | TS 23.502 Clarification on AMF Subscription Correlation ID | 15.2.0 |
| 2018-06 | SP-80 | SP-180478 | 0357 | 6 | F | Additional DataSet and Datakey | 15.2.0 |
| 2018-06 | SP-80 | SP-180489 | 0359 | 2 | F | TS23.502 Remove access independent event trigger in Nsmf_EventExposure Service | 15.2.0 |
| 2018-06 | SP-80 | SP-180488 | 0360 | 4 | F | S-NSSAI check in Network Triggered Service Request | 15.2.0 |
| 2018-06 | SP-80 | SP-180483 | 0362 | 1 | F | Correction to User Plane Security Enforcement | 15.2.0 |
| 2018-06 | SP-80 | SP-180483 | 0363 | 1 | F | Correction to handover procedures | 15.2.0 |
| 2018-06 | SP-80 | SP-180477 | 0365 | - | D | Corrections on namings of SMF Service Operations | 15.2.0 |
| 2018-06 | SP-80 | SP-180484 | 0366 | 1 | F | Corrections to the selective deactivation of UP connection | 15.2.0 |
| 2018-06 | SP-80 | SP-180481 | 0369 | 4 | F | Clarification on the EBI assignment, PDU session ID list in Registration and PDU session correlation. | 15.2.0 |
| 2018-06 | SP-80 | SP-180486 | 0370 | 1 | F | Mofification on SMF registration afer EPS to 5GS mobility | 15.2.0 |
| 2018-06 | SP-80 | SP-180487 | 0371 | 2 | F | Proposal on the EPS Qos parameters on N7 | 15.2.0 |
| 2018-06 | SP-80 | SP-180483 | 0374 | - | F | Correction to Nnwdaf_EventsSubscription_Notify (related to nw slice) | 15.2.0 |
| 2018-06 | SP-80 | SP-180480 | 0376 | 1 | F | Clarification on Nbsf_Management_Deregister service operation | 15.2.0 |
| 2018-06 | SP-80 | SP-180481 | 0377 | 2 | F | Clarification on Nnwdaf_Analytics_Info service | 15.2.0 |
| 2018-06 | SP-80 | SP-180483 | 0378 | 1 | F | Correction to indirect forwarding at intra 5GS N2 HO | 15.2.0 |
| 2018-06 | SP-80 | SP-180485 | 0380 | 1 | F | Local deactivation of MICO mode | 15.2.0 |
| 2018-06 | SP-80 | SP-180484 | 0382 | 1 | F | Dual registration interworking procedure | 15.2.0 |
| 2018-06 | SP-80 | SP-180484 | 0383 | 8 | F | EBI allocation and slicing interworking with EPS | 15.2.0 |
| 2018-06 | SP-80 | SP-180490 | 0384 | 2 | F | Tunnel Info reservation at the UPF for sessions interworked with EPC | 15.2.0 |
| 2018-06 | SP-80 | SP-180483 | 0388 | 1 | F | Correction to Nnef_TrafficInfluence service description | 15.2.0 |
| 2018-06 | SP-80 | SP-180487 | 0389 | 3 | F | Relaying of Nnef_TrafficInfluence requests to the PCF | 15.2.0 |
| 2018-06 | SP-80 | SP-180484 | 0392 | 1 | F | Corrections to PFD management | 15.2.0 |
| 2018-06 | SP-80 | SP-180487 | 0393 | 2 | F | Registration procedure update | 15.2.0 |
| 2018-06 | SP-80 | SP-180485 | 0394 | 2 | F | Handling of maximum supported data rate per UE for integrity protection | 15.2.0 |
| 2018-06 | SP-80 | SP-180486 | 0395 | 1 | F | NF/NF service Discovery across PLMNs | 15.2.0 |
| 2018-06 | SP-80 | SP-180486 | 0396 | 1 | F | NF/NF service Status Subscribe/Notify Flows | 15.2.0 |
| 2018-06 | SP-80 | SP-180487 | 0397 | - | F | Nudm service update to support Steering of Roaming | 15.2.0 |
| 2018-06 | SP-80 | SP-180484 | 0400 | 2 | F | Deregistration procedure for SMS over NAS | 15.2.0 |
| 2018-06 | SP-80 | SP-180487 | 0401 | - | F | Nudm service update to support P-CSCF Restoration | 15.2.0 |
| 2018-06 | SP-80 | SP-180482 | 0402 | 1 | F | Correction on Location continuity procedure | 15.2.0 |
| 2018-06 | SP-80 | SP-180485 | 0403 | 1 | F | IPsec SAs in tunnel mode | 15.2.0 |
| 2018-06 | SP-80 | SP-180481 | 0404 | 1 | F | Clarify GUTI aspects for single-registration mode UEs for interworking without N26 | 15.2.0 |
| 2018-06 | SP-80 | SP-180489 | 0406 | 1 | F | Transaction reference ID usage in NEF NBI | 15.2.0 |
| 2018-06 | SP-80 | SP-180483 | 0407 | 2 | F | Correction to UE Radio Capability handling | 15.2.0 |
| 2018-06 | SP-80 | SP-180488 | 0408 | - | F | Resolving EN related to subscription data | 15.2.0 |
| 2018-06 | SP-80 | SP-180488 | 0409 | - | F | Resolving EN related to paging priority | 15.2.0 |
| 2018-06 | SP-80 | SP-180485 | 0410 | 1 | F | Handling of Configured NSSAIs in Roaming Scenarios - 23.502 | 15.2.0 |
| 2018-06 | SP-80 | SP-180488 | 0411 | 1 | F | Slicing information and RFSP | 15.2.0 |
| 2018-06 | SP-80 | SP-180487 | 0412 | 1 | F | QoS rule structure improvement | 15.2.0 |
| 2018-06 | SP-80 | SP-180476 | 0415 | 3 | B | Exposure Data | 15.2.0 |
| 2018-06 | SP-80 | SP-180484 | 0416 | - | F | EPS to 5GS Mobility | 15.2.0 |
| 2018-06 | SP-80 | SP-180485 | 0417 | 1 | F | Fixes for HO Procedure - Handling MT Signalling from SMF. | 15.2.0 |
| 2018-06 | SP-80 | SP-180478 | 0418 | 3 | F | AMF Context Retrieval upon relocation | 15.2.0 |
| 2018-06 | SP-80 | SP-180487 | 0419 | - | F | NRF Service Operations | 15.2.0 |
| 2018-06 | SP-80 | SP-180484 | 0420 | 2 | F | EPS Bearer ID allocation for Home routed case | 15.2.0 |
| 2018-06 | SP-80 | SP-180490 | 0422 | 1 | F | UDM-AUSF Discovery | 15.2.0 |
| 2018-06 | SP-80 | SP-180479 | 0423 | 2 | F | AS Security Setup | 15.2.0 |
| 2018-06 | SP-80 | SP-180481 | 0425 | 2 | F | Clarification on the roaming aspects of SMF related policy | 15.2.0 |
| 2018-06 | SP-80 | SP-180479 | 0428 | 2 | F | Clarification on AN parameter in Service Request | 15.2.0 |
| 2018-06 | SP-80 | SP-180482 | 0431 | 1 | F | Correction on Non-3GPP Registration procedure | 15.2.0 |
| 2018-06 | SP-80 | SP-180490 | 0432 | 4 | F | UE presence of Area Of Interest (Restructuring) | 15.2.0 |
| 2018-06 | SP-80 | SP-180486 | 0439 | 1 | F | Missing S-NSSAI and the associated NSI ID in Nnrf_NFManagement_service | 15.2.0 |
| 2018-06 | SP-80 | SP-180488 | 0440 | 1 | F | Removing Editor's note about How NWDAF services work while roaming | 15.2.0 |
| 2018-06 | SP-80 | SP-180482 | 0445 | 3 | F | CN type indicator in Emergency Service Fallback procedure | 15.2.0 |
| 2018-06 | SP-80 | SP-180482 | 0446 | 2 | F | Correct Nudr_DM service operation usage by NEF | 15.2.0 |
| 2018-06 | SP-80 | SP-180488 | 0447 | - | F | Resolving EN related to Exposure with bulk subscription | 15.2.0 |
| 2018-06 | SP-80 | SP-180486 | 0448 | 1 | F | Mobility restrictions | 15.2.0 |
| 2018-06 | SP-80 | SP-180488 | 0449 | 2 | F | S-NSSAI of VPLMN when HO from 4G to 5G | 15.2.0 |
| 2018-06 | SP-80 | SP-180485 | 0451 | 2 | F | How Peer CP NF sends notification to target/new AMF after AMF planned removal | 15.2.0 |
| 2018-06 | SP-80 | SP-180478 | 0452 | 1 | F | AF influence on traffic routing for Ethernet type PDU Session | 15.2.0 |
| 2018-06 | SP-80 | SP-180479 | 0457 | 1 | F | Clarification of maximum number of reports and maximum duration of reporting | 15.2.0 |
| 2018-06 | SP-80 | SP-180478 | 0458 | 1 | F | Align Namf_Communication_N1N2TransferFailure service operation | 15.2.0 |
| 2018-06 | SP-80 | SP-180490 | 0460 | 2 | F | UDR storage for Nnef_TrafficInfluence from AF | 15.2.0 |
| 2018-06 | SP-80 | SP-180491 | 0461 | 2 | F | Update to AMF policy association modification procedure | 15.2.0 |
| 2018-06 | SP-80 | SP-180489 | 0463 | 1 | F | Support for UAC Access Identity in Visited PLMNs | 15.2.0 |
| 2018-06 | SP-80 | SP-180488 | 0464 | - | F | SMF exemption to NAS level congestion control for high priority access | 15.2.0 |
| 2018-06 | SP-80 | SP-180488 | 0465 | - | F | SMF Selection Subscriber Data clarification | 15.2.0 |
| 2018-06 | SP-80 | SP-180479 | 0466 | 1 | F | Clarification on Emergency services Fallback | 15.2.0 |
| 2018-06 | SP-80 | SP-180490 | 0467 | 1 | F | Update of the Handover procedure considering the ongoing inter NG-RAN node handover | 15.2.0 |
| 2018-06 | SP-80 | SP-180491 | 0468 | - | F | Update of the Network Triggered Service Request procedure for some clarifications | 15.2.0 |
| 2018-06 | SP-80 | SP-180485 | 0469 | 2 | F | Including GUAMI in RRC message of related procedures | 15.2.0 |
| 2018-06 | SP-80 | SP-180480 | 0470 | 3 | F | Clarification on Mobility related parameters of UE Context in AMF | 15.2.0 |
| 2018-06 | SP-80 | SP-180482 | 0473 | 2 | F | CN tunnel handling for IRAT Idle mobility | 15.2.0 |
| 2018-06 | SP-80 | SP-180480 | 0474 | 2 | F | Clarification on SMSF checking SMS management subscription data | 15.2.0 |
| 2018-06 | SP-80 | SP-180481 | 0476 | 1 | F | Clarification on UE configuration update procedure | 15.2.0 |
| 2018-06 | SP-80 | SP-180487 | 0477 | 2 | F | PCF selection during the AMF relocation | 15.2.0 |
| 2018-06 | SP-80 | SP-180486 | 0480 | 5 | F | MT-SMS over NAS re-transmission upon delivery failure on one Access Type | 15.2.0 |
| 2018-06 | SP-80 | SP-180478 | 0481 | 1 | F | Allowed NSSAI RAN awareness | 15.2.0 |
| 2018-06 | SP-80 | SP-180490 | 0486 | 2 | F | UE radio capability handling in the 5GS | 15.2.0 |
| 2018-06 | SP-80 | SP-180478 | 0487 | 1 | F | Adding number of supported packet filters in PDU Session Modification | 15.2.0 |
| 2018-06 | SP-80 | SP-180491 | 0492 | 1 | F | Update Registration procedures | 15.2.0 |
| 2018-06 | SP-80 | SP-180482 | 0496 | 1 | F | Correction of having multiple S-NSSAIs for a single PDU session | 15.2.0 |
| 2018-06 | SP-80 | SP-180486 | 0497 | 3 | F | Network slicing subsription change and update of UE configuration | 15.2.0 |
| 2018-06 | SP-80 | SP-180490 | 0498 | 2 | F | UE support of SMS and SMS subscription | 15.2.0 |
| 2018-06 | SP-80 | SP-180488 | 0499 | 2 | F | Removal of RAT Type from UE-associated N2 signalling | 15.2.0 |
| 2018-06 | SP-80 | SP-180482 | 0501 | 2 | F | Clarifying use-cases of network triggered service request | 15.2.0 |
| 2018-06 | SP-80 | SP-180481 | 0502 | 1 | F | Clarifying UE Reachability Notification Procedure | 15.2.0 |
| 2018-06 | SP-80 | SP-180483 | 0505 | 2 | F | Correction to identifiers in Registration procedure | 15.2.0 |
| 2018-06 | SP-80 | SP-180483 | 0506 | - | F | Correction to Figure 4.3.5.7-1: Simultaneous change of Branching Point or UL CL and additional PSA for a PDU Session | 15.2.0 |
| 2018-06 | SP-80 | SP-180483 | 0507 | - | F | Correction to UDR Data Set Identifiers considered in this release | 15.2.0 |
| 2018-06 | SP-80 | SP-180490 | 0508 | - | F | UE Policies in a UE Policy Container | 15.2.0 |
| 2018-06 | SP-80 | SP-180480 | 0509 | - | F | Clarification on single outstanding Service Request | 15.2.0 |
| 2018-09 | SP-81 | SP-180717 | 0390 | 5 | F | Discovering SMF instance at EPS to 5GS interworking | 15.3.0 |
| 2018-09 | SP-81 | SP-180717 | 0489 | 4 | F | AMF-PCF Association termination | 15.3.0 |
| 2018-09 | SP-81 | SP-180717 | 0512 | 1 | F | Change OCS to CHF in TS 23.502 | 15.3.0 |
| 2018-09 | SP-81 | SP-180717 | 0513 | 1 | F | Correction to SMF registration of PDU Session ID | 15.3.0 |
| 2018-09 | SP-81 | SP-180717 | 0514 | - | F | Correction to handling of DNNs not supported by the network | 15.3.0 |
| 2018-09 | SP-81 | SP-180717 | 0516 | - | F | Mandatory valid lifetime configuration for old IP prefix in multi-homing | 15.3.0 |
| 2018-09 | SP-81 | SP-180717 | 0517 | 4 | F | Temporary identitier usage at interworking | 15.3.0 |
| 2018-09 | SP-81 | SP-180717 | 0518 | 1 | F | Requested NSSAI in Network Initiated Change of Network slices | 15.3.0 |
| 2018-09 | SP-81 | SP-180717 | 0519 | 1 | F | Network Slicing Subscription Change Indication | 15.3.0 |
| 2018-09 | SP-81 | SP-180717 | 0520 | 2 | F | Triggers for Network Triggered Service Request and UE Activity procedure | 15.3.0 |
| 2018-09 | SP-81 | SP-180717 | 0521 | - | F | 5GS to EPS Mobility without N26 | 15.3.0 |
| 2018-09 | SP-81 | SP-180717 | 0522 | 1 | F | EPS to 5GS mobility with N26 | 15.3.0 |
| 2018-09 | SP-81 | SP-180717 | 0525 | 7 | F | Handling of subscription restrictions for mobility from EPS to 5GS | 15.3.0 |
| 2018-09 | SP-81 | SP-180717 | 0526 | 2 | F | Update of parameter in call flow and service operation for NSI ID | 15.3.0 |
| 2018-09 | SP-81 | SP-180717 | 0527 | - | F | Corrections to AF influence on traffic routing | 15.3.0 |
| 2018-09 | SP-81 | SP-180724 | 0530 | 2 | B | Support of tracing in 5GS signalling: SM related signalling and data | 15.3.0 |
| 2018-09 | SP-81 | SP-180724 | 0531 | 2 | B | Support of tracing in 5GS signalling: SMSF related signalling and data | 15.3.0 |
| 2018-09 | SP-81 | SP-180717 | 0532 | 1 | B | User Location Information added in N2 UE Context Release Complete | 15.3.0 |
| 2018-09 | SP-81 | SP-180717 | 0533 | 1 | F | Clarification to UE Configuration Update | 15.3.0 |
| 2018-09 | SP-81 | SP-180717 | 0534 | - | F | Clarification on CN-initiated selective deactivation of UP connection | 15.3.0 |
| 2018-09 | SP-81 | SP-180717 | 0535 | 1 | F | Clarification on UE configuration update procedure | 15.3.0 |
| 2018-09 | SP-81 | SP-180717 | 0539 | - | F | Alignment on Namf_EventExposure_Subscribe service operation | 15.3.0 |
| 2018-09 | SP-81 | SP-180718 | 0540 | 7 | F | PCF added as consumer of EventExposure service of AMF and SMF | 15.3.0 |
| 2018-09 | SP-81 | SP-180718 | 0543 | 2 | F | Correction on Connection Resume procedure | 15.3.0 |
| 2018-09 | SP-81 | SP-180718 | 0544 | 1 | F | Correction on signalling message holding during HO | 15.3.0 |
| 2018-09 | SP-81 | SP-180718 | 0546 | 1 | F | Clarification on UE Capability Match Request procedure | 15.3.0 |
| 2018-09 | SP-81 | SP-180717 | 0547 | - | D | Fixing clause number | 15.3.0 |
| 2018-09 | SP-81 | SP-180718 | 0548 | 1 | F | Service Accept to complete Service Request | 15.3.0 |
| 2018-09 | SP-81 | SP-180718 | 0549 | 3 | F | TS 23.502 Clarification on N2 based handover | 15.3.0 |
| 2018-09 | SP-81 | SP-180718 | 0550 | 4 | F | TS23.502 Clarifications on Xn based handover | 15.3.0 |
| 2018-09 | SP-81 | SP-180717 | 0555 | - | D | Editorial Fixes to the UECM Text | 15.3.0 |
| 2018-09 | SP-81 | SP-180718 | 0557 | 2 | F | Termination of the AM Policy Association | 15.3.0 |
| 2018-09 | SP-81 | SP-180718 | 0561 | 2 | F | Adding N28 session termination procedure and updates to CHF services | 15.3.0 |
| 2018-09 | SP-81 | SP-180718 | 0563 | - | F | Update to Registration procedure with AMF relocation | 15.3.0 |
| 2018-09 | SP-81 | SP-180717 | 0565 | 2 | D | Correction of UE configuration update procedure | 15.3.0 |
| 2018-09 | SP-81 | SP-180717 | 0569 | 1 | C | Indirect data forwarding for interworking with N26 | 15.3.0 |
| 2018-09 | SP-81 | SP-180718 | 0576 | 2 | F | UE Context in SMSF data | 15.3.0 |
| 2018-09 | SP-81 | SP-180718 | 0577 | 1 | F | UE context in SMF data | 15.3.0 |
| 2018-09 | SP-81 | SP-180718 | 0579 | - | F | TS 23.502: Mobility Restriction List Clean up | 15.3.0 |
| 2018-09 | SP-81 | SP-180718 | 0582 | 5 | F | Default S-NSSAI correction and NSSF service update | 15.3.0 |
| 2018-09 | SP-81 | SP-180718 | 0585 | 2 | F | Subscription of selecting the same SMF and UPF | 15.3.0 |
| 2018-09 | SP-81 | SP-180718 | 0586 | 2 | F | N16 communication failure | 15.3.0 |
| 2018-09 | SP-81 | SP-180718 | 0587 | 4 | F | Clarification on UPF tunnel change | 15.3.0 |
| 2018-09 | SP-81 | SP-180718 | 0588 | 3 | F | Data handling in UPF during IRAT handover | 15.3.0 |
| 2018-09 | SP-81 | SP-180718 | 0590 | 1 | F | 5GS to EPS Mobility | 15.3.0 |
| 2018-09 | SP-81 | SP-180718 | 0591 | 1 | F | Registration type for Nudm_UECM_Registration | 15.3.0 |
| 2018-09 | SP-81 | SP-180718 | 0592 | 1 | F | Correction to AS Security Context | 15.3.0 |
| 2018-09 | SP-81 | SP-180718 | 0594 | 1 | F | Peer NF association of GUAMI with a given UE | 15.3.0 |
| 2018-09 | SP-81 | SP-180718 | 0595 | 1 | F | 23.502: 5G AN Parameters sent during Service Request | 15.3.0 |
| 2018-09 | SP-81 | SP-180718 | 0597 | 2 | F | Correction on AMF and UDM service table | 15.3.0 |
| 2018-09 | SP-81 | SP-180718 | 0599 | 1 | F | RRC Inactive to EPC mobility | 15.3.0 |
| 2018-09 | SP-81 | SP-180719 | 0600 | 1 | F | Homogeneous Support of IMS Voice over PS Sessions indication | 15.3.0 |
| 2018-09 | SP-81 | SP-180719 | 0601 | 2 | F | Clarification on the PDU session handling in EPS to 5GS handover with N26 | 15.3.0 |
| 2018-09 | SP-81 | SP-180719 | 0602 | 1 | F | Clarification on the target MME capability from AMF to SMF for 5GS to EPS mobility | 15.3.0 |
| 2018-09 | SP-81 | SP-180719 | 0604 | 1 | F | Handling LADN service area during handovers | 15.3.0 |
| 2018-09 | SP-81 | SP-180719 | 0605 | 1 | F | Clarification on N3IWF key delivery during registration procedure | 15.3.0 |
| 2018-09 | SP-81 | SP-180719 | 0606 | 1 | F | Clarification on representation of AoI for NG-RAN location reporting procedure | 15.3.0 |
| 2018-09 | SP-81 | SP-180719 | 0607 | 2 | F | MT SMS failure recovery | 15.3.0 |
| 2018-09 | SP-81 | SP-180719 | 0608 | 1 | F | Add monitoring event cancellation call flows | 15.3.0 |
| 2018-09 | SP-81 | SP-180719 | 0609 | 1 | F | Nudm_EventExposure_Subscribe and unsubscribe service operation correction | 15.3.0 |
| 2018-09 | SP-81 | SP-180719 | 0610 | - | F | Time stamp in Namf, Nsmf and Nnef EventExposure_Notify service operations | 15.3.0 |
| 2018-09 | SP-81 | SP-180719 | 0611 | 1 | F | Corrections to NRF services description | 15.3.0 |
| 2018-09 | SP-81 | SP-180719 | 0612 | 9 | F | SBI friendly UE policy delivery procedure | 15.3.0 |
| 2018-09 | SP-81 | SP-180719 | 0613 | 1 | F | Correction to handover from 5GS to EPS | 15.3.0 |
| 2018-09 | SP-81 | SP-180719 | 0615 | 2 | F | Correction on inter-PLMN mobility | 15.3.0 |
| 2018-09 | SP-81 | SP-180719 | 0616 | 1 | F | Update to PDN connection establishment | 15.3.0 |
| 2018-09 | SP-81 | SP-180719 | 0617 | 3 | F | Clarification on Nbsf_Management_Update service operation | 15.3.0 |
| 2018-09 | SP-81 | SP-180719 | 0618 | - | F | Nudm service update to support protection of Steering of Roaming | 15.3.0 |
| 2018-09 | SP-81 | SP-180719 | 0619 | - | F | 5GS-EPS interworking for Multi-homed IPv6 PDU Session | 15.3.0 |
| 2018-09 | SP-81 | SP-180719 | 0620 | 2 | F | Clafication on retrievial of the security context from old AMF | 15.3.0 |
| 2018-09 | SP-81 | SP-180717 | 0621 | 2 | B | Missing NEF services. | 15.3.0 |
| 2018-09 | SP-81 | SP-180719 | 0623 | - | F | Clarifications about MOBIKE and N3IWF certificate | 15.3.0 |
| 2018-09 | SP-81 | SP-180719 | 0626 | - | F | Corrections to N4 session and N4 node procedures | 15.3.0 |
| 2018-09 | SP-81 | SP-180719 | 0627 | 1 | F | Solving wrong references, service names or service operation names in NF services description | 15.3.0 |
| 2018-09 | SP-81 | SP-180719 | 0628 | - | F | Incorrect service operation names for NEF services | 15.3.0 |
| 2018-09 | SP-81 | SP-180719 | 0630 | 2 | F | Correction to NRF service operations and procedures | 15.3.0 |
| 2018-09 | SP-81 | SP-180719 | 0631 | 1 | F | Correction to Event Exposure operations | 15.3.0 |
| 2018-09 | SP-81 | SP-180720 | 0633 | 1 | F | Clarifications on AF influence on traffic routing procedures | 15.3.0 |
| 2018-09 | SP-81 | SP-180720 | 0634 | 2 | F | Corrections to UE Requested PDU Session Establishment | 15.3.0 |
| 2018-09 | SP-81 | SP-180720 | 0635 | - | F | Corrections related to SM on Hand-Over procedures | 15.3.0 |
| 2018-09 | SP-81 | SP-180720 | 0636 | 1 | F | Replace wrong Figure 4.16.4-1: SM Policy Association Establishment | 15.3.0 |
| 2018-09 | SP-81 | SP-180720 | 0637 | - | F | Optionality of Network area information | 15.3.0 |
| 2018-09 | SP-81 | SP-180720 | 0638 | - | F | Location Service, alignment procedures and NF Services | 15.3.0 |
| 2018-09 | SP-81 | SP-180720 | 0639 | 1 | F | Core Network type restriction on EPC in 5GS subscription data | 15.3.0 |
| 2018-09 | SP-81 | SP-180720 | 0640 | 2 | F | Indirect Forwarding Flag | 15.3.0 |
| 2018-09 | SP-81 | SP-180720 | 0641 | 1 | F | Storing FQDN for S5/S8 interface of the SMF+PGW-C in UDM | 15.3.0 |
| 2018-09 | SP-81 | SP-180720 | 0644 | 1 | F | Impacts on Update Location in 5GS to EPS Interworking without N26 | 15.3.0 |
| 2018-09 | SP-81 | SP-180720 | 0646 | - | F | Resolving Editor's notes related to N2 messages | 15.3.0 |
| 2018-09 | SP-81 | SP-180720 | 0647 | - | F | Resolving Editor's note related to Session Management | 15.3.0 |
| 2018-09 | SP-81 | SP-180720 | 0648 | - | F | Resolving Editor's note related to Security | 15.3.0 |
| 2018-09 | SP-81 | SP-180720 | 0651 | - | F | Correction for UE requested LADN Information | 15.3.0 |
| 2018-09 | SP-81 | SP-180720 | 0653 | - | F | Clarification on ANDSP support | 15.3.0 |
| 2018-09 | SP-81 | SP-180720 | 0654 | 1 | F | Clarification on N26 based interworking procedures | 15.3.0 |
| 2018-09 | SP-81 | SP-180720 | 0655 | 1 | F | Corrections on Area Of Interest | 15.3.0 |
| 2018-09 | SP-81 | SP-180720 | 0657 | 3 | F | Signalling Configured NSSAIs valid for any PLMN usage in the Registration procedure | 15.3.0 |
| 2018-09 | SP-81 | SP-180720 | 0658 | 1 | F | SMS support used in different meanings | 15.3.0 |
| 2018-09 | SP-81 | SP-180720 | 0660 | 2 | F | NEF notification event correction | 15.3.0 |
| 2018-09 | SP-81 | SP-180720 | 0662 | 1 | F | Exposure with bulk subscription correction | 15.3.0 |
| 2018-09 | SP-81 | SP-180720 | 0663 | - | F | Removal of duplicated call flow | 15.3.0 |
| 2018-09 | SP-81 | SP-180720 | 0664 | 1 | F | NEF service operation correction | 15.3.0 |
| 2018-09 | SP-81 | SP-180720 | 0667 | 1 | F | Updates to NF service framework and NRF services for CHF discovery and selection | 15.3.0 |
| 2018-09 | SP-81 | SP-180721 | 0668 | - | F | Correction to service name for UE Subscriber Data Update Notification | 15.3.0 |
| 2018-09 | SP-81 | SP-180721 | 0670 | 1 | F | Correction to the procedure of PFD Retrieval by the SMF | 15.3.0 |
| 2018-09 | SP-81 | SP-180721 | 0671 | 2 | F | Removal of Binding information storage in UDR | 15.3.0 |
| 2018-09 | SP-81 | SP-180721 | 0673 | 2 | F | Further corrections to identifiers in Registration procedure | 15.3.0 |
| 2018-09 | SP-81 | SP-180721 | 0674 | - | F | Correction to Configured NSSAI for the HPLMN | 15.3.0 |
| 2018-09 | SP-81 | SP-180721 | 0675 | 1 | F | Correction to emergency registered | 15.3.0 |
| 2018-09 | SP-81 | SP-180721 | 0676 | - | F | Correction of wrong reference | 15.3.0 |
| 2018-09 | SP-81 | SP-180721 | 0678 | 1 | F | Corrections to Service Request | 15.3.0 |
| 2018-09 | SP-81 | SP-180721 | 0679 | 1 | F | Core Network assistance information in N2 message | 15.3.0 |
| 2018-09 | SP-81 | SP-180721 | 0682 | 3 | F | Correction to unsubscribe the monitoring event for a group | 15.3.0 |
| 2018-09 | SP-81 | SP-180721 | 0683 | 2 | F | OAuth2 Authorization Service | 15.3.0 |
| 2018-09 | SP-81 | SP-180721 | 0686 | - | F | 23.502: UDM Service Operations | 15.3.0 |
| 2018-09 | SP-81 | SP-180721 | 0689 | 1 | F | 23.502: N2 Tracing Requirements | 15.3.0 |
| 2018-09 | SP-81 | SP-180721 | 0690 | 2 | F | 23.502: AMF-AMF Tracing Requirements | 15.3.0 |
| 2018-09 | SP-81 | SP-180721 | 0691 | 1 | F | 23.502: AUSF, UDM, UDR Discovery | 15.3.0 |
| 2018-09 | SP-81 | SP-180721 | 0692 | 2 | F | 23.502: UE Context removal correction | 15.3.0 |
| 2018-09 | SP-81 | SP-180721 | 0693 | 1 | F | 23.502: NRF in different domains | 15.3.0 |
| 2018-09 | SP-81 | SP-180721 | 0694 | 4 | F | Default IPsec tunnel for a PDU Session | 15.3.0 |
| 2018-09 | SP-81 | SP-180721 | 0695 | 2 | F | Clarification on List Of PDU Sessions To Be Activated | 15.3.0 |
| 2018-09 | SP-81 | SP-180721 | 0697 | 3 | F | Correction to Service Request QoS when changing between non-3GPP and 3GPP accesses | 15.3.0 |
| 2018-09 | SP-81 | SP-180721 | 0699 | 4 | F | Clarification for QoS flow associated with the default QoS rule | 15.3.0 |
| 2018-09 | SP-81 | SP-180721 | 0702 | 3 | F | Update to registration procedure with AMF relocation | 15.3.0 |
| 2018-09 | SP-81 | SP-180721 | 0704 | 1 | F | The interaction between AF and PCF | 15.3.0 |
| 2018-09 | SP-81 | SP-180721 | 0705 | 2 | F | Storage of UE Policy in VPLMN | 15.3.0 |
| 2018-09 | SP-81 | SP-180721 | 0706 | 2 | F | TS 23.502 Clarification on Namf_Communication_N2InfoNotify | 15.3.0 |
| 2018-09 | SP-81 | SP-180722 | 0707 | 2 | F | TS23.502 Removal of Nnef_PFDManagement_Create service operation | 15.3.0 |
| 2018-09 | SP-81 | SP-180722 | 0708 | - | F | Clarifications on Registration, UE triggered SR and UCU procedures | 15.3.0 |
| 2018-09 | SP-81 | SP-180722 | 0709 | 2 | F | Clarifications on Registration and SR procedures | 15.3.0 |
| 2018-09 | SP-81 | SP-180722 | 0710 | 2 | F | Update Registration procedures for SMS over NAS | 15.3.0 |
| 2018-09 | SP-81 | SP-180722 | 0712 | 1 | F | Correction on the PDN connection IE and S-NSSAI during 4G-&gt;5G interorking with N26. | 15.3.0 |
| 2018-09 | SP-81 | SP-180722 | 0715 | 2 | F | EBI allocation for interworking | 15.3.0 |
| 2018-09 | SP-81 | SP-180722 | 0718 | 1 | F | NGAP session management procedure handling | 15.3.0 |
| 2018-09 | SP-81 | SP-180722 | 0720 | - | F | Correction on security for interworking | 15.3.0 |
| 2018-09 | SP-81 | SP-180722 | 0721 | 2 | F | Registration triggered by UE Configuration Update | 15.3.0 |
| 2018-09 | SP-81 | SP-180722 | 0722 | 2 | F | UE Configuration for MM policy | 15.3.0 |
| 2018-09 | SP-81 | SP-180722 | 0723 | 2 | F | LMF Service Update | 15.3.0 |
| 2018-09 | SP-81 | SP-180722 | 0724 | 3 | F | Clarification on terminology in NF service framework procedures | 15.3.0 |
| 2018-09 | SP-81 | SP-180722 | 0726 | - | F | Update Network-initiated Deregistration | 15.3.0 |
| 2018-09 | SP-81 | SP-180791 | 0714 | 2 | F | Clarification on the AMF store the DNN and SMF+PGW-C to UDM+HSS without N26 | 15.3.0 |
| 2018-12 | SP-82 | SP-181088 | 0642 | 6 | F | Handling of AMF registration in UDM for non-3GPP access | 15.4.0 |
| 2018-12 | SP-82 | SP-181088 | 0643 | 1 | F | Handling of Notify Request in EPC | 15.4.0 |
| 2018-12 | SP-82 | SP-181091 | 0645 | 2 | F | Use of Nudm service operations in EPS to 5GS mobility without N26 | 15.4.0 |
| 2018-12 | SP-82 | SP-181087 | 0652 | 3 | F | Correction for Registration procedure for LADN – Triggering Condition | 15.4.0 |
| 2018-12 | SP-82 | SP-181089 | 0661 | 4 | F | IWK support for handover of PDU sessions without UP | 15.4.0 |
| 2018-12 | SP-82 | SP-181091 | 0730 | 5 | C | Update of Default Configured NSSAI and other UE parameters via Control Plane Solution from UDM to AMF with Direct NAS Transport to UE | 15.4.0 |
| 2018-12 | SP-82 | SP-181090 | 0731 | 3 | C | Support for partial ciphering of initial NAS messages | 15.4.0 |
| 2018-12 | SP-82 | SP-181084 | 0734 | 2 | F | Aligning Nnrf_NFManagement with 23.501 and stage 3, 29.510 | 15.4.0 |
| 2018-12 | SP-82 | SP-181084 | 0735 | 1 | F | Aligning discovery with stage 3 | 15.4.0 |
| 2018-12 | SP-82 | SP-181084 | 0736 | - | F | Alignment of AMF identity transfer in LCS procedures | 15.4.0 |
| 2018-12 | SP-82 | SP-181088 | 0737 | 2 | F | EPS Fallback, RAT Fallback and PCC | 15.4.0 |
| 2018-12 | SP-82 | SP-181087 | 0738 | 1 | F | Correction to UE context transfer upon registration via another access type | 15.4.0 |
| 2018-12 | SP-82 | SP-181088 | 0739 | 3 | F | Handover from 5GC-N3IWF to EPS | 15.4.0 |
| 2018-12 | SP-82 | SP-181088 | 0740 | 3 | F | Handover from EPC/ePDG to 5GS | 15.4.0 |
| 2018-12 | SP-82 | SP-181088 | 0741 | 1 | F | Corrections to EPS to 5GS mobility for idle-mode mobility | 15.4.0 |
| 2018-12 | SP-82 | SP-181087 | 0742 | 3 | F | Corrections to 5GS to EPS handover using N26 | 15.4.0 |
| 2018-12 | SP-82 | SP-181087 | 0743 | 3 | F | Corrections to EPS to 5GS handover | 15.4.0 |
| 2018-12 | SP-82 | SP-181084 | 0745 | 4 | F | Npcf_EventExposure service for bulk subscription | 15.4.0 |
| 2018-12 | SP-82 | SP-181088 | 0746 | 1 | F | Interactions with PCF - Interworking | 15.4.0 |
| 2018-12 | SP-82 | SP-181086 | 0749 | 1 | F | Correcting the interaction needed for the NSSF service | 15.4.0 |
| 2018-12 | SP-82 | SP-181087 | 0752 | - | F | Correction on TAU during 5GS to EPS handover using N26 interface | 15.4.0 |
| 2018-12 | SP-82 | SP-181089 | 0753 | 1 | F | PCF interaction during IWK when UE is in EPS | 15.4.0 |
| 2018-12 | SP-82 | SP-181085 | 0755 | 1 | F | Clarification on signalling connection release condition in Registration procedure | 15.4.0 |
| 2018-12 | SP-82 | SP-181085 | 0756 | 2 | F | Clarification on PDU Session activation and deactivation | 15.4.0 |
| 2018-12 | SP-82 | SP-181090 | 0757 | 2 | F | TS23.502 Clarification on UE policy service and AM policy service | 15.4.0 |
| 2018-12 | SP-82 | SP-181091 | 0759 | 1 | F | Using TCP for reliable NAS transport between UE and N3IWF | 15.4.0 |
| 2018-12 | SP-82 | SP-181090 | 0762 | 2 | F | RRC Inactive state assistance information provisioning to NG-RAN | 15.4.0 |
| 2018-12 | SP-82 | SP-181084 | 0765 | 1 | F | Adding RAN Status Transfer to N2 HO | 15.4.0 |
| 2018-12 | SP-82 | SP-181089 | 0767 | 5 | F | Network controlled NSSAI for SR-related Access Stratum connection establishment | 15.4.0 |
| 2018-12 | SP-82 | SP-181090 | 0768 | 1 | F | Replace PCRF+PCF with PCF in interworking with EPC scenarios | 15.4.0 |
| 2018-12 | SP-82 | SP-181089 | 0770 | 1 | F | Priority indication over SBA interfaces via Message Priority header | 15.4.0 |
| 2018-12 | SP-82 | SP-181086 | 0772 | - | F | Correcting known consumers of Namf service | 15.4.0 |
| 2018-12 | SP-82 | SP-181091 | 0773 | 2 | F | Updates from UEPolicyControl introduction | 15.4.0 |
| 2018-12 | SP-82 | SP-181090 | 0774 | 1 | F | Secondary Re-authentication update | 15.4.0 |
| 2018-12 | SP-82 | SP-181085 | 0775 | 3 | F | Clarification on interworking with N26 interface | 15.4.0 |
| 2018-12 | SP-82 | SP-181087 | 0777 | 1 | F | Correction to the monitoring event subscription to a group | 15.4.0 |
| 2018-12 | SP-82 | SP-181087 | 0779 | 1 | F | Correction to UE Policy Association procedure | 15.4.0 |
| 2018-12 | SP-82 | SP-181086 | 0782 | 5 | F | Clarification on the delivery of EBI to UE and RAN | 15.4.0 |
| 2018-12 | SP-82 | SP-181085 | 0783 | 4 | F | CHF Selection | 15.4.0 |
| 2018-12 | SP-82 | SP-181084 | 0784 | 1 | F | AF subscribed events | 15.4.0 |
| 2018-12 | SP-82 | SP-181087 | 0785 | 2 | F | Correction to AM Policy Association Termination in registration procedure | 15.4.0 |
| 2018-12 | SP-82 | SP-181084 | 0786 | 3 | F | Alignment for always-on PDU sessions | 15.4.0 |
| 2018-12 | SP-82 | SP-181084 | 0788 | - | F | Adding Subscribed DNN list in Access and Mobility subscription data | 15.4.0 |
| 2018-12 | SP-82 | SP-181088 | 0790 | 4 | F | EPS Interworking: Single versus Dual Registration with the UDM | 15.4.0 |
| 2018-12 | SP-82 | SP-181088 | 0791 | 1 | F | EPS bearer mapping for 5GS to EPS mobility with N26 | 15.4.0 |
| 2018-12 | SP-82 | SP-181090 | 0792 | 1 | F | Registration Procedure – fix UDM registration | 15.4.0 |
| 2018-12 | SP-82 | SP-181086 | 0793 | 3 | F | Clarification on the PDU Session handover procedure with the User Plane Security Enforcement | 15.4.0 |
| 2018-12 | SP-82 | SP-181091 | 0795 | 3 | F | Update the UCU procedure with operator-defined access category definitions | 15.4.0 |
| 2018-12 | SP-82 | SP-181086 | 0796 | 1 | F | Clarification on the AMF store the DNN and SMF+PGW-C to UDM+HSS | 15.4.0 |
| 2018-12 | SP-82 | SP-181088 | 0799 | 2 | F | Efficient delivery of UE Policies | 15.4.0 |
| 2018-12 | SP-82 | SP-181091 | 0800 | 1 | F | Update the general description of Nnef_PFDManagement service | 15.4.0 |
| 2018-12 | SP-82 | SP-181089 | 0801 | 1 | F | Monitoring input parameter correction | 15.4.0 |
| 2018-12 | SP-82 | SP-181091 | 0802 | 1 | F | Update of SMS service operation parameters for 3GPP specific encoding | 15.4.0 |
| 2018-12 | SP-82 | SP-181089 | 0803 | - | F | NRF Service Update | 15.4.0 |
| 2018-12 | SP-82 | SP-181087 | 0806 | 4 | F | Correction of UE Configuration Update | 15.4.0 |
| 2018-12 | SP-82 | SP-181088 | 0807 | 1 | F | Handling of NF location during discovery | 15.4.0 |
| 2018-12 | SP-82 | SP-181088 | 0808 | 1 | F | Corrections to event exposure information flows and Nudm_EventExposure service description | 15.4.0 |
| 2018-12 | SP-82 | SP-181089 | 0809 | 2 | C | MCS Access and Mobility Subscription Data | 15.4.0 |
| 2018-12 | SP-82 | SP-181089 | 0813 | 1 | F | PDU Session Modification due to QoS Flow creation | 15.4.0 |
| 2018-12 | SP-82 | SP-181090 | 0814 | 2 | F | SMF storing FQDN for the S5/S8 interface of the SMF+PGW-C for N3GPP PDU Session | 15.4.0 |
| 2018-12 | SP-82 | SP-181088 | 0815 | 2 | F | Handling of N3GPP access registration in interworking between EPS and 5GS using N26. | 15.4.0 |
| 2018-12 | SP-82 | SP-181090 | 0816 | 2 | F | UE Identifier provided during Registration Procedure | 15.4.0 |
| 2018-12 | SP-82 | SP-181090 | 0817 | 1 | F | Selective deactivation for always-on PDU sessions | 15.4.0 |
| 2018-12 | SP-82 | SP-181084 | 0818 | 3 | F | 5G-TMSI reallocation and RRC Inactive | 15.4.0 |
| 2018-12 | SP-82 | SP-181089 | 0819 | 1 | F | QoS Flow deletion | 15.4.0 |
| 2018-12 | SP-82 | SP-181090 | 0823 | 1 | F | Registration procedure with different Registration types | 15.4.0 |
| 2018-12 | SP-82 | SP-181088 | 0824 | 2 | F | EPS to 5GS with network slices | 15.4.0 |
| 2018-12 | SP-82 | SP-181084 | 0825 | 3 | F | AUSF and UDM selection in 5GC NFs | 15.4.0 |
| 2018-12 | SP-82 | SP-181090 | 0827 | 3 | F | Registration procedure updates due to UE Policy Control Service | 15.4.0 |
| 2018-12 | SP-82 | SP-181088 | 0828 | 1 | F | Include GPSI in Npcf-SMPolicyControl Create message | 15.4.0 |
| 2018-12 | SP-82 | SP-181085 | 0830 | 2 | F | Clarification on DNN not subscribed in AMF | 15.4.0 |
| 2018-12 | SP-82 | SP-181085 | 0831 | - | F | Clarification on ANDSP support indication in UE Policy Container | 15.4.0 |
| 2018-12 | SP-82 | SP-181085 | 0832 | 1 | F | Clarification on rejected S-NSSAIs and cause in Registration and UCU procedure | 15.4.0 |
| 2018-12 | SP-82 | SP-181085 | 0835 | 1 | F | Clarification on Event Reporting information for Npcf_PolicyAuthorization service | 15.4.0 |
| 2018-12 | SP-82 | SP-181086 | 0836 | 1 | F | Clarification on UE Policy Control Request Triggers | 15.4.0 |
| 2018-12 | SP-82 | SP-181087 | 0837 | 1 | F | Correction to interworking procedures without N26 | 15.4.0 |
| 2018-12 | SP-82 | SP-181089 | 0838 | - | F | Indirect forwarding timer for N2 HO | 15.4.0 |
| 2018-12 | SP-82 | SP-181085 | 0841 | 1 | F | Clarification on Registration with AMF re-allocation | 15.4.0 |
| 2018-12 | SP-82 | SP-181089 | 0842 | 1 | F | PDN Disconnection handling | 15.4.0 |
| 2018-12 | SP-82 | SP-181086 | 0843 | 2 | F | Clarification on SMF registration to UDM+HSS | 15.4.0 |
| 2018-12 | SP-82 | SP-181089 | 0845 | 1 | F | OSID storage | 15.4.0 |
| 2018-12 | SP-82 | SP-181085 | 0846 | 1 | F | Clarification on PDU Session procedures (AMF awareness of N2 information type) | 15.4.0 |
| 2018-12 | SP-82 | SP-181085 | 0847 | 1 | F | Clarification on ID provision to RAN in registration procedure | 15.4.0 |
| 2018-12 | SP-82 | SP-181088 | 0848 | - | F | Deletion of AN tunnel info from Handover Notify message in the EPS-to-5GS handover procedure | 15.4.0 |
| 2018-12 | SP-82 | SP-181090 | 0849 | - | F | Removal of PPI from N2 SM information | 15.4.0 |
| 2018-12 | SP-82 | SP-181087 | 0850 | 1 | F | Correction to handover from EPS to 5GS | 15.4.0 |
| 2018-12 | SP-82 | SP-181089 | 0852 | 1 | F | Non-accepted PDU session in N2 based HO | 15.4.0 |
| 2018-12 | SP-82 | SP-181086 | 0854 | 2 | F | Clarification on the PDN connection release during N26 mobility | 15.4.0 |
| 2018-12 | SP-82 | SP-181090 | 0857 | - | F | Storing SMSF address in the UDR | 15.4.0 |
| 2018-12 | SP-82 | SP-181084 | 0859 | 2 | F | Addition of URRP in UE context in the MM context | 15.4.0 |
| 2018-12 | SP-82 | SP-181088 | 0860 | 1 | F | Event subscription clarification | 15.4.0 |
| 2018-12 | SP-82 | SP-181085 | 0861 | 1 | F | Charging related information in Nsmf_PDUSession_Create service operation | 15.4.0 |
| 2018-12 | SP-82 | SP-181087 | 0862 | 1 | F | Correction to network requested PDU Session Release due to a change of the set of network slices for a UE | 15.4.0 |
| 2018-12 | SP-82 | SP-181088 | 0863 | - | B | Data Volume Reporting for Option 4/7 - Procedure updates | 15.4.0 |
| 2019-01 | - | - | - | - | - | Editorial correction to replace '-' with 'o' due to CR implementation error. | 15.4.1 |
| 2019-03 | SP-83 | SP-190157 | 0868 | 1 | F | Avoiding unnecessary authentication for SR-mode UEs during EPS-5GS mobility | 15.5.0 |
| 2019-03 | SP-83 | SP-190157 | 0869 | 3 | F | PDU Session Release with User Plane Deactivated | 15.5.0 |
| 2019-03 | SP-83 | SP-190157 | 0870 | 1 | F | DL Data Buffering in the SMF for the PDU Session with UP Deactivated | 15.5.0 |
| 2019-03 | SP-83 | SP-190157 | 0871 | 4 | F | Registration Procedure Update with Inter PLMN AMF Reallocation | 15.5.0 |
| 2019-03 | SP-83 | SP-190157 | 0873 | 1 | F | Data Types for parameters within UE Parameter Update via Control Plane Solution | 15.5.0 |
| 2019-03 | SP-83 | SP-190157 | 0874 | 1 | F | Adding SM Context ID in relevant clauses | 15.5.0 |
| 2019-03 | SP-83 | SP-190157 | 0876 | 1 | F | Corrections to N4 procedure for PFD management | 15.5.0 |
| 2019-03 | SP-83 | SP-190157 | 0879 | 1 | F | Support of piggybacking of NAS SM message while configuring a DRB | 15.5.0 |
| 2019-03 | SP-83 | SP-190157 | 0880 | 1 | F | SMF register in UDM | 15.5.0 |
| 2019-03 | SP-83 | SP-190157 | 0881 | 3 | F | Alignment with stage 3 for EPS interworking indications | 15.5.0 |
| 2019-03 | SP-83 | SP-190157 | 0884 | - | F | Correction to UECM_Update service operation for status change of EPS interworking support | 15.5.0 |
| 2019-03 | SP-83 | SP-190157 | 0886 | 6 | F | EBI allocation when access type of PDU Session is changed from N3GPP to 3GPP. Revocation of EBI when access type of PDU Session is changed from 3GPP to N3GPP | 15.5.0 |
| 2019-03 | SP-83 | SP-190157 | 0888 | 3 | F | Remove PEI from the required input of Npcf_AMPolicyControl service operations | 15.5.0 |
| 2019-03 | SP-83 | SP-190157 | 0889 | 2 | F | Correction to UE parameters update procedure | 15.5.0 |
| 2019-03 | SP-83 | SP-190157 | 0893 | 1 | F | Clarification on Policy related procedures | 15.5.0 |
| 2019-03 | SP-83 | SP-190157 | 0901 | - | F | AMF awareness of N2 information type (LMF case) | 15.5.0 |
| 2019-03 | SP-83 | SP-190157 | 0904 | 1 | F | List of equivalent PLMNs in Registration accept missing | 15.5.0 |
| 2019-03 | SP-83 | SP-190157 | 0907 | 2 | F | Retrieval of Policy Control Subscription information for validation of URSP rules | 15.5.0 |
| 2019-03 | SP-83 | SP-190157 | 0909 | 1 | F | Events subscribed using the Npcf_PolicyAuthorization Service | 15.5.0 |
| 2019-03 | SP-83 | SP-190157 | 0910 | 2 | F | Correction to the Initial NAS message protection | 15.5.0 |
| 2019-03 | SP-83 | SP-190157 | 0911 | - | F | Remove BSF from the UDR consumer list | 15.5.0 |
| 2019-03 | SP-83 | SP-190157 | 0913 | - | F | Add AMF as consumer for UpdateNotify Service Operation for Npcf_UEPolicyControl Service | 15.5.0 |
| 2019-03 | SP-83 | SP-190157 | 0914 | 1 | F | Corrections to UE Policy Association Establishment procedure | 15.5.0 |
| 2019-03 | SP-83 | SP-190157 | 0915 | 1 | F | Corrections to UE Policy Association Modification initiated by the AMF procedure | 15.5.0 |
| 2019-03 | SP-83 | SP-190157 | 0916 | - | F | Corrections to UE Policy Association Modification initiated by the PCF procedure | 15.5.0 |
| 2019-03 | SP-83 | SP-190158 | 0923 | 6 | F | Procedure for DN authorization profile index | 15.5.0 |
| 2019-03 | SP-83 | SP-190158 | 0925 | 1 | F | Correction on current HO procedures | 15.5.0 |
| 2019-03 | SP-83 | SP-190158 | 0927 | 1 | F | Presence of Reference ID in Location Reporting Control | 15.5.0 |
| 2019-03 | SP-83 | SP-190158 | 0930 | 1 | F | Clarification on missing condition of UE Policy Association Establishment | 15.5.0 |
| 2019-03 | SP-83 | SP-190158 | 0933 | 2 | F | Network Slice update clarification | 15.5.0 |
| 2019-03 | SP-83 | SP-190158 | 0934 | 3 | F | Clarification on Mobility Restriction | 15.5.0 |
| 2019-03 | SP-83 | SP-190158 | 0935 | 2 | F | Clarification of the PDU Session establishment and release procedure | 15.5.0 |
| 2019-03 | SP-83 | SP-190158 | 0936 | - | F | IP address/Prefix(es) kept for 5G to 4G mobility | 15.5.0 |
| 2019-03 | SP-83 | SP-190158 | 0939 | 1 | F | Correction on UE policy delivery | 15.5.0 |
| 2019-03 | SP-83 | SP-190158 | 0943 | 1 | F | Correction to UE initiated service request procedure | 15.5.0 |
| 2019-03 | SP-83 | SP-190158 | 0944 | 1 | F | Correction to Xn handover for network sharing | 15.5.0 |
| 2019-03 | SP-83 | SP-190158 | 0947 | - | F | Clarification on the UE Capability Match Request procedure | 15.5.0 |
| 2019-03 | SP-83 | SP-190158 | 0953 | 1 | F | Correcting references for routing rules configuration | 15.5.0 |
| 2019-03 | SP-83 | SP-190158 | 0954 | - | F | Correction for EPS to 5GS Mobility | 15.5.0 |
| 2019-03 | SP-83 | SP-190158 | 0956 | 1 | F | Correction on monitoring event for 'availability after DDN failure'. | 15.5.0 |
| 2019-03 | SP-83 | SP-190158 | 0960 | 3 | F | Fixes for DC secondary RAT charging report procedure | 15.5.0 |
| 2019-03 | SP-83 | SP-190158 | 0961 | 1 | F | Selection of a combo PGW+SMF at EPC attachment via WLAN access | 15.5.0 |
| 2019-03 | SP-83 | SP-190158 | 0981 | 4 | F | Correction of the handling of QoS flows at 5GS to EPS mobility | 15.5.0 |
| 2019-03 | SP-83 | SP-190158 | 0982 | 1 | F | UE presence in restricted area indication during inter NG-RAN node N2 based handover | 15.5.0 |
| 2019-03 | SP-83 | SP-190158 | 0988 | 1 | F | Correction for Annex C | 15.5.0 |
| 2019-03 | SP-83 | SP-190158 | 0995 | 2 | F | Informing EPS about Emergency case during Emergency Service Fallback | 15.5.0 |
| 2019-03 | SP-83 | SP-190158 | 0996 | - | F | Corrections to PDUSession_SMContexStatusNotify and PDUSession_StatusNotify | 15.5.0 |
| 2019-03 | SP-83 | SP-190158 | 0997 | 2 | F | Corrections to N3GPP handover scenarios | 15.5.0 |
| 2019-03 | SP-83 | SP-190158 | 1000 | - | F | UE Identity during the Registration procedure | 15.5.0 |
| 2019-03 | SP-83 | SP-190158 | 1006 | 2 | F | Clarification on Location continuity for handover of emergency session | 15.5.0 |
| 2019-03 | SP-83 | SP-190159 | 1010 | 4 | F | Correction of the change of access in home routed roaming scenario | 15.5.0 |
| 2019-03 | SP-83 | SP-190159 | 1025 | 2 | F | Correction on UE Requested PDU Session Establishment for Home Routed roaming | 15.5.0 |
| 2019-03 | SP-83 | SP-190159 | 1030 | 4 | F | UE Configuration Update Procedure Correction | 15.5.0 |
| 2019-03 | SP-83 | SP-190159 | 1032 | 2 | F | Handling proposal in case of UPF selection failure | 15.5.0 |
| 2019-03 | SP-83 | SP-190159 | 1034 | 1 | F | Correction to Exposure with bulk subscription procedure | 15.5.0 |
| 2019-03 | SP-83 | SP-190159 | 1037 | 3 | F | Slice interworking HR mode update | 15.5.0 |
| 2019-03 | SP-83 | SP-190159 | 1038 | 2 | F | Clarificaiton on UE Behaviour for PDN Connection Handover Failure to 5GS | 15.5.0 |
| 2019-03 | SP-83 | SP-190159 | 1042 | 1 | F | UE identifier during Initial Registration | 15.5.0 |
| 2019-03 | SP-83 | SP-190159 | 1045 | - | F | Target ID in Nsmf_PDUSession_CreateSMContext for EPS to 5GS handover | 15.5.0 |
| 2019-03 | SP-83 | SP-190159 | 1063 | 1 | F | Correction the terms on Secondary authentication/authorization of the PDU Session Establishment | 15.5.0 |
| 2019-03 | SP-83 | SP-190159 | 1065 | 1 | F | Xn based handover with I-UPF insertion | 15.5.0 |
| 2019-03 | SP-83 | SP-190159 | 1067 | 3 | F | EPS bearer synchronization when move from EPC to 5GC(UE deletes the bearer locally) | 15.5.0 |
| 2019-03 | SP-83 | SP-190159 | 1069 | 2 | F | Register SMF+PGW-C to HSS+UDM | 15.5.0 |
| 2019-03 | SP-83 | SP-190159 | 1075 | 2 | F | Clarification on missing condition of UE Policy Association Termination | 15.5.0 |
| 2019-03 | SP-83 | SP-190159 | 1076 | 1 | F | Clarification on missing condition of AM Policy Association Establishement and Termination | 15.5.0 |
| 2019-03 | SP-83 | SP-190159 | 1084 | 1 | F | Correction on SMSF address registration in UDM | 15.5.0 |
| 2019-03 | SP-83 | SP-190159 | 1087 | 1 | F | Clarification on NG-RAN behaviour on Periodic RNAU procedure | 15.5.0 |
| 2019-03 | SP-83 | SP-190159 | 1088 | 2 | F | Clarification on PDU Session modification and release procedure | 15.5.0 |
| 2019-03 | SP-83 | SP-190159 | 1099 | 1 | F | Corrections on routing rule | 15.5.0 |
| 2019-03 | SP-83 | SP-190159 | 1100 | - | F | Correction to AM policy association related procedure | 15.5.0 |
| 2019-03 | SP-83 | SP-190159 | 1101 | 3 | F | Correction to policy related defintion in the registration procedure | 15.5.0 |
| 2019-03 | SP-83 | SP-190159 | 1103 | 1 | F | EPS Fallback Initial Context Setup | 15.5.0 |
| 2019-03 | SP-83 | SP-190159 | 1108 | 1 | F | Update the procedure for the change of SSC mode 3 PDU Session Anchor with multiple PDU sessions | 15.5.0 |
| 2019-03 | SP-83 | SP-190230 | 1119 | - | F | Removal of UPF_Management Service | 15.5.0 |
| 2019-03 | SP-83 | SP-190173 | 0866 | 9 | B | Introduction of ATSSS Procedures including Multi-Access PDU Session Establishment | 16.0.0 |
| 2019-03 | SP-83 | SP-190166 | 0872 | 3 | B | Small Data over NAS PDU Session Management | 16.0.0 |
| 2019-03 | SP-83 | SP-190171 | 0877 | 6 | B | Procedure updates for solution 1 in 23.725 for user plane redundancy | 16.0.0 |
| 2019-03 | SP-83 | SP-190171 | 0878 | 2 | B | Procedure for solution 11 in 23.725 for Ethernet anchor relocation | 16.0.0 |
| 2019-03 | SP-83 | SP-190167 | 0894 | 2 | B | Procedures for Trusted Non-3GPP Access | 16.0.0 |
| 2019-03 | SP-83 | SP-190199 | 0895 | 1 | F | eNS IDLE mobility | 16.0.0 |
| 2019-03 | SP-83 | SP-190174 | 0903 | 2 | B | eSBA communication schemas related to discovery and selection | 16.0.0 |
| 2019-03 | SP-83 | SP-190171 | 0905 | 2 | B | Update procedure of 23.502 to adopt solution 4 in 23.725 | 16.0.0 |
| 2019-03 | SP-83 | SP-190171 | 0906 | 2 | B | Introduction of TR 23.725 solution 6 for UL CL relocation | 16.0.0 |
| 2019-03 | SP-83 | SP-190166 | 0918 | 4 | B | Procedures for CIoT Management of Enhanced Coverage | 16.0.0 |
| 2019-03 | SP-83 | SP-190166 | 0924 | 2 | B | Introduction of the MSISDN-less MO SMS Service | 16.0.0 |
| 2019-03 | SP-83 | SP-190166 | 0928 | 3 | B | Enhance Idle mode mobility using N26 interface procedure to support NAS-SM data transfer via SCEF+NEF | 16.0.0 |
| 2019-03 | SP-83 | SP-190172 | 0929 | 3 | B | Adding reference to new TS 23.288 in TS 23.502 | 16.0.0 |
| 2019-03 | SP-83 | SP-190168 | 0932 | 2 | F | Update to LCS related definitions | 16.0.0 |
| 2019-03 | SP-83 | SP-190164 | 0937 | 2 | B | Procedures related to ETSUN | 16.0.0 |
| 2019-03 | SP-83 | SP-190166 | 0942 | 3 | B | Extended connected time value for enhancing MICO mode | 16.0.0 |
| 2019-03 | SP-83 | SP-190162 | 0946 | 2 | B | Adding 5G SRVCC description to 23.502 | 16.0.0 |
| 2019-03 | SP-83 | SP-190174 | 0957 | 5 | B | eSBA communication schema Model C | 16.0.0 |
| 2019-03 | SP-83 | SP-190170 | 0962 | 3 | B | NEF service for service specific parameter provisioning | 16.0.0 |
| 2019-03 | SP-83 | SP-190166 | 0964 | 4 | B | Procedures for solution 14 to key issue 9 | 16.0.0 |
| 2019-03 | SP-83 | SP-190164 | 0967 | 2 | B | KI-#5 specific AF influence on traffic routing | 16.0.0 |
| 2019-03 | SP-83 | SP-190174 | 0968 | 4 | B | Bindings between the consumer and producer | 16.0.0 |
| 2019-03 | SP-83 | SP-190172 | 0970 | 5 | B | Use of analytics for background data transfer | 16.0.0 |
| 2019-03 | SP-83 | SP-190166 | 0971 | 8 | B | Introduction of small data transfer in Control Plane CIoT 5GS Optmisation | 16.0.0 |
| 2019-03 | SP-83 | SP-190166 | 0972 | 10 | B | Procedure of NEF based Non-IP Data Delivery | 16.0.0 |
| 2019-03 | SP-83 | SP-190166 | 0973 | 2 | B | Expected UE Behaviour parameters for CIoT | 16.0.0 |
| 2019-03 | SP-83 | SP-190166 | 0974 | 5 | B | MICO Mode Management for Expected Application Behaviour | 16.0.0 |
| 2019-03 | SP-83 | SP-190166 | 0975 | 2 | B | Procedures for Inter-RAT mobility support to and from NB-IoT | 16.0.0 |
| 2019-03 | SP-83 | SP-190166 | 0976 | 2 | B | CIoT Procedures for CN Selection and Steering | 16.0.0 |
| 2019-03 | SP-83 | SP-190166 | 0977 | 5 | B | External parameters provisioning to the 5GS | 16.0.0 |
| 2019-03 | SP-83 | SP-190166 | 0978 | 4 | B | Extend existing procedures for external parameters provisioning in 5GS | 16.0.0 |
| 2019-03 | SP-83 | SP-190169 | 0987 | 2 | B | 5GLAN group management procedures | 16.0.0 |
| 2019-03 | SP-83 | SP-190172 | 0992 | 2 | B | Update of TS 23.502 for BDT notification | 16.0.0 |
| 2019-03 | SP-83 | SP-190173 | 0993 | 1 | B | Updates to Nnrf services to include MA PDU session capability | 16.0.0 |
| 2019-03 | SP-83 | SP-190171 | 1001 | 2 | B | PDU Session Management Procedure to support URLLC | 16.0.0 |
| 2019-03 | SP-83 | SP-190166 | 1002 | 2 | B | Session Management Procedure for Control Plane CIoT 5GS Optimisation | 16.0.0 |
| 2019-03 | SP-83 | SP-190164 | 1003 | 2 | B | Nsmf_PDUSession_ContextRequest service operation Update | 16.0.0 |
| 2019-03 | SP-83 | SP-190167 | 1009 | 2 | B | PDU Session establishment for Trusted Non-3GPP Access | 16.0.0 |
| 2019-03 | SP-83 | SP-190172 | 1013 | 3 | B | Addition of Event Reporting Information Parameters for network data analytics | 16.0.0 |
| 2019-03 | SP-83 | SP-190166 | 1015 | 2 | F | Application function notification of downlink data delivery status (HLCom) | 16.0.0 |
| 2019-03 | SP-83 | SP-190166 | 1016 | 2 | F | Including MICO with Extended Connected time in relevant procedures | 16.0.0 |
| 2019-03 | SP-83 | SP-190166 | 1017 | 2 | B | Introducing eDRX parameters to procedures | 16.0.0 |
| 2019-03 | SP-83 | SP-190193 | 1023 | 2 | B | TS 23.502: Introducing Non-public network - CAG | 16.0.0 |
| 2019-03 | SP-83 | SP-190169 | 1024 | 2 | B | TS 23.502: Introducing Non-public network | 16.0.0 |
| 2019-03 | SP-83 | SP-190175 | 1027 | 2 | B | Support PDN type Ethernet at 5GS to EPS mobility with N26 | 16.0.0 |
| 2019-03 | SP-83 | SP-190167 | 1039 | 2 | B | Support of full Frame Routing feature | 16.0.0 |
| 2019-03 | SP-83 | SP-190168 | 1043 | 2 | F | LCS Event Exposure using NEF | 16.0.0 |
| 2019-03 | SP-83 | SP-190168 | 1046 | - | F | Remove LMF Service Descriptions | 16.0.0 |
| 2019-03 | SP-83 | SP-190166 | 1055 | 2 | B | Support for Reliable Data Service | 16.0.0 |
| 2019-03 | SP-83 | SP-190164 | 1056 | 1 | B | Addition of UE IP address Allocation by UPF | 16.0.0 |
| 2019-03 | SP-83 | SP-190172 | 1060 | 2 | B | NEF service for NWDAF analytics | 16.0.0 |
| 2019-03 | SP-83 | SP-190171 | 1064 | 2 | B | Update HO procedure of 23.502 to adopt solution 4 in 23.725 | 16.0.0 |
| 2019-03 | SP-83 | SP-190164 | 1071 | 4 | B | ETSUN: N2 based handover procedures | 16.0.0 |
| 2019-03 | SP-83 | SP-190164 | 1072 | 3 | B | ETSUN: UL CL/BP Insertion, AN release, Selective deactivation procedures | 16.0.0 |
| 2019-03 | SP-83 | SP-190199 | 1074 | 1 | B | eNS: Update handover from 4G to 5G via N26 | 16.0.0 |
| 2019-03 | SP-83 | SP-190167 | 1078 | 2 | B | UDM data for wireline access characteristics | 16.0.0 |
| 2019-03 | SP-83 | SP-190172 | 1080 | 2 | B | CR for TS 23.502 Updating NRF Services | 16.0.0 |
| 2019-03 | SP-83 | SP-190164 | 1092 | 2 | B | ETSUN Xn handover | 16.0.0 |
| 2019-03 | SP-83 | SP-190162 | 1093 | 1 | B | Adding AMF reporting UE SRVCC capability | 16.0.0 |
| 2019-03 | SP-83 | SP-190171 | 1107 | 3 | B | Activating UP path based on AF response | 16.0.0 |
| 2019-03 | SP-83 | SP-190166 | 1110 | 2 | B | Procedures for Service Gap Control | 16.0.0 |
| 2019-03 | SP-83 | SP-190166 | 1115 | 2 | B | Procedure of availability after DDN failure notification for multiple AFs | 16.0.0 |
| 2019-03 | SP-83 | SP-190171 | 1116 | 3 | B | Updates to 4.3.6, based on TR Sol#13 | 16.0.0 |
| 2019-04 | - | - | - | - | - | MCC editorial style and formatting corrections | 16.0.1 |
| 2019-04 | - | - | - | - | - | MCC correction moving clause 4.21.2 to 4.17.11 and renaming clause 4.17.11 to 4.17.12 for readability purposes | 16.0.2 |
| 2019-06 | SP-84 | SP-190420 | 0979 | 5 | B | Adding network status exposure capability with optional use of analytics | 16.1.0 |
| 2019-06 | SP-84 | SP-190410 | 1073 | 4 | F | eSBA NF Registration via SCP | 16.1.0 |
| 2019-06 | SP-84 | SP-190408 | 1111 | 2 | B | Introduction of inter-UE QoS differentiation for NB-IoT using NB-IoT UE Priority | 16.1.0 |
| 2019-06 | SP-84 | SP-190410 | 1120 | 9 | F | Resolving the EN in Bindings between the consumer and producer | 16.1.0 |
| 2019-06 | SP-84 | SP-190416 | 1124 | 7 | B | Update ATSSS performance measurement Procedures | 16.1.0 |
| 2019-06 | SP-84 | SP-190425 | 1128 | 3 | B | Introduction of RACS: UCMF services | 16.1.0 |
| 2019-06 | SP-84 | SP-190419 | 1129 | 1 | B | SMF discovery of P-CSCF | 16.1.0 |
| 2019-06 | SP-84 | SP-190419 | 1130 | 3 | B | HSS instances registration and discovery in NRF | 16.1.0 |
| 2019-06 | SP-84 | SP-190420 | 1131 | 3 | F | Correction for background data transfer in TS 23.502 | 16.1.0 |
| 2019-06 | SP-84 | SP-190400 | 1133 | 2 | A | Corrections of Npcf_UEPolicyControl Service | 16.1.0 |
| 2019-06 | SP-84 | SP-190400 | 1135 | 4 | A | UE Policy association procedures correction | 16.1.0 |
| 2019-06 | SP-84 | SP-190408 | 1136 | 2 | C | Header Compression for CP CIoT 5GS Optimisation | 16.1.0 |
| 2019-06 | SP-84 | SP-190412 | 1138 | 5 | B | UP connection Deactivation for URLLC PDU Session | 16.1.0 |
| 2019-06 | SP-84 | SP-190420 | 1140 | 6 | B | Removal of Editor's note and update the specification for BDT warning notification in TS 23.502 | 16.1.0 |
| 2019-06 | SP-84 | SP-190422 | 1141 | 5 | B | Transfer of N4 information for local traffic switching from SMF to I-SMF | 16.1.0 |
| 2019-06 | SP-84 | SP-190430 | 1144 | 1 | F | Procedure updates for 5G LAN group management | 16.1.0 |
| 2019-06 | SP-84 | SP-190413 | 1145 | 2 | F | SMF determining support of Ethernet PDN Type | 16.1.0 |
| 2019-06 | SP-84 | SP-190400 | 1148 | - | A | Corrections to procedure of 5GS to EPS Mobility without N26 | 16.1.0 |
| 2019-06 | SP-84 | SP-190413 | 1149 | 2 | F | SMF determining EPS interworking support | 16.1.0 |
| 2019-06 | SP-84 | SP-190400 | 1150 | 2 | C | EPS interworking support indication from AMF to SMF for N3GPP PDU Session | 16.1.0 |
| 2019-06 | SP-84 | SP-190406 | 1151 | 2 | F | PFD provisioning procedure | 16.1.0 |
| 2019-06 | SP-84 | SP-190410 | 1152 | - | F | Network Slicing and delegated discovery | 16.1.0 |
| 2019-06 | SP-84 | SP-190400 | 1156 | 2 | A | Remove note on skipping subscription for UE Policy Delivery Result | 16.1.0 |
| 2019-06 | SP-84 | SP-190415 | 1158 | 2 | B | Registration Procedure Update for Trusted non-3GPP access | 16.1.0 |
| 2019-06 | SP-84 | SP-190416 | 1161 | 2 | F | Clarificaiton on MA PDU Session Establishment for HR roaming | 16.1.0 |
| 2019-06 | SP-84 | SP-190408 | 1164 | 2 | F | TS23.502, Clarification of header compression and other editorial update | 16.1.0 |
| 2019-06 | SP-84 | SP-190400 | 1167 | 3 | A | Correction to N2 AMF Mobility Request | 16.1.0 |
| 2019-06 | SP-84 | SP-190410 | 1168 | 2 | F | Update of NRF services for supporting indirect communication | 16.1.0 |
| 2019-06 | SP-84 | SP-190412 | 1171 | 1 | F | Correction to the user plane redundancy handling | 16.1.0 |
| 2019-06 | SP-84 | SP-190410 | 1172 | 1 | F | NF/NF service status subscribe/notify update | 16.1.0 |
| 2019-06 | SP-84 | SP-190415 | 1173 | 1 | B | Session binding information in wireline access | 16.1.0 |
| 2019-06 | SP-84 | SP-190419 | 1174 | 1 | B | Support for IMS functionality using Npcf services | 16.1.0 |
| 2019-06 | SP-84 | SP-190416 | 1176 | - | B | Adding ATSSS steering capabilities to UPF provisioning information | 16.1.0 |
| 2019-06 | SP-84 | SP-190408 | 1179 | 3 | B | MTC Provider Information clarification | 16.1.0 |
| 2019-06 | SP-84 | SP-190408 | 1180 | 1 | B | NEF based NIDD procedure with home routed traffic | 16.1.0 |
| 2019-06 | SP-84 | SP-190408 | 1182 | 2 | C | Report count per Event type | 16.1.0 |
| 2019-06 | SP-84 | SP-190408 | 1183 | 2 | B | Service Gap corrections | 16.1.0 |
| 2019-06 | SP-84 | SP-190408 | 1184 | 7 | B | Updates of CP and UP CIoT 5GS optimisation procedures | 16.1.0 |
| 2019-06 | SP-84 | SP-190415 | 1185 | 2 | F | PDU Session establishment and modification via trusted non-3GPP access | 16.1.0 |
| 2019-06 | SP-84 | SP-190416 | 1190 | 2 | F | UE Requested PDU Session Establishment with Network Modification to MA PDU Session | 16.1.0 |
| 2019-06 | SP-84 | SP-190427 | 1191 | 1 | F | Correction of not resolved non-normative statements | 16.1.0 |
| 2019-06 | SP-84 | SP-190409 | 1194 | - | B | Extension of AMF Services Operations for eLCS | 16.1.0 |
| 2019-06 | SP-84 | SP-190409 | 1196 | 4 | B | UDM SM Data for eLCS | 16.1.0 |
| 2019-06 | SP-84 | SP-190400 | 1198 | 1 | A | Correction to the provisioning of the UE Integrity Protection Data Rate capability | 16.1.0 |
| 2019-06 | SP-84 | SP-190427 | 1202 | 2 | F | S-NSSAIs of UE Context transfer during inter PLMN mobility | 16.1.0 |
| 2019-06 | SP-84 | SP-190412 | 1203 | 5 | C | Update procedures related to redundant transmission | 16.1.0 |
| 2019-06 | SP-84 | SP-190400 | 1207 | 1 | A | Add missing description on UE Policy Information | 16.1.0 |
| 2019-06 | SP-84 | SP-190400 | 1209 | 1 | A | Correction to UCU procedure and Policy related service | 16.1.0 |
| 2019-06 | SP-84 | SP-190400 | 1214 | 1 | F | Clarification on PDU Session deactivation | 16.1.0 |
| 2019-06 | SP-84 | SP-190416 | 1215 | 6 | B | PDU Session Modification for ATSSS | 16.1.0 |
| 2019-06 | SP-84 | SP-190416 | 1216 | 2 | B | Registration and Service Request for ATSSS | 16.1.0 |
| 2019-06 | SP-84 | SP-190416 | 1217 | 1 | B | PDU Session Release for ATSSS | 16.1.0 |
| 2019-06 | SP-84 | SP-190408 | 1223 | - | B | Update to NIDD configuration service and procedures | 16.1.0 |
| 2019-06 | SP-84 | SP-190421 | 1224 | 5 | B | Slice Specific Authentication and Authorization with multiple registrations in the same PLMN | 16.1.0 |
| 2019-06 | SP-84 | SP-190400 | 1225 | 1 | A | Clarification on Mobility Restriction | 16.1.0 |
| 2019-06 | SP-84 | SP-190427 | 1226 | 1 | F | Correction to UE Activity Procedure | 16.1.0 |
| 2019-06 | SP-84 | SP-190400 | 1227 | 1 | A | EPS bearer synchronization when move from EPC to 5GC(Network deletes bearer locally) | 16.1.0 |
| 2019-06 | SP-84 | SP-190400 | 1228 | 3 | A | Resource released at the V-SMF/V-UPF | 16.1.0 |
| 2019-06 | SP-84 | SP-190400 | 1229 | 1 | A | Correction to EPS to 5GS mobility procedure without N26 | 16.1.0 |
| 2019-06 | SP-84 | SP-190422 | 1230 | 1 | B | LADN PDU Session handling in ETSUN scenario | 16.1.0 |
| 2019-06 | SP-84 | SP-190421 | 1231 | 5 | B | eNS IDLE mobility for AMF reallocation | 16.1.0 |
| 2019-06 | SP-84 | SP-190408 | 1232 | 1 | F | Update to NIDD delivery service and procedures | 16.1.0 |
| 2019-06 | SP-84 | SP-190408 | 1233 | 2 | B | Adding NIDD authorization update service and procedures | 16.1.0 |
| 2019-06 | SP-84 | SP-190408 | 1234 | 1 | B | Adding NIDD SMF-NEF Connection Release service and procedures | 16.1.0 |
| 2019-06 | SP-84 | SP-190427 | 1236 | 1 | F | Correction on unsuccessful MT SMS delivery attempt and UE Activity Notification | 16.1.0 |
| 2019-06 | SP-84 | SP-190422 | 1237 | 7 | B | I-SMF relocation with I-UPF as an ULCL or BP | 16.1.0 |
| 2019-06 | SP-84 | SP-190420 | 1239 | 1 | B | Adding NF load information inside NFprofile | 16.1.0 |
| 2019-06 | SP-84 | SP-190400 | 1243 | 1 | F | Correction on Non-3GPP Registration procedure | 16.1.0 |
| 2019-06 | SP-84 | SP-190401 | 1245 | 2 | A | Correction for 5GS AM Policy Framework | 16.1.0 |
| 2019-06 | SP-84 | SP-190401 | 1247 | 2 | A | Correction for 5GS SM Policy Framework | 16.1.0 |
| 2019-06 | SP-84 | SP-190401 | 1249 | 2 | A | Correction for 5GS UE Policy Framework | 16.1.0 |
| 2019-06 | SP-84 | SP-190401 | 1251 | 3 | A | Clarification on the PDU session re-establish without N26 | 16.1.0 |
| 2019-06 | SP-84 | SP-190401 | 1253 | 4 | A | Clarification on the 5G to 4G idle mobility with N26 for sync | 16.1.0 |
| 2019-06 | SP-84 | SP-190420 | 1256 | 6 | B | CR for adding Naf_EventExposure services | 16.1.0 |
| 2019-06 | SP-84 | SP-190430 | 1258 | 9 | B | Provisioning of 5G LAN group configuration parameters | 16.1.0 |
| 2019-06 | SP-84 | SP-190410 | 1260 | 2 | F | Indirect communication without delegated discovery - corrections | 16.1.0 |
| 2019-06 | SP-84 | SP-190531 | 1262 | 1 | A | Correcting AMF behaviour for Service Request that is not integrity protected | 16.1.0 |
| 2019-06 | SP-84 | SP-190413 | 1263 | 3 | F | Registration Update with complete attach | 16.1.0 |
| 2019-06 | SP-84 | SP-190408 | 1264 | - | F | Correction to the NIDD Configuration procedure | 16.1.0 |
| 2019-06 | SP-84 | SP-190412 | 1265 | 2 | C | Update PDU Session Establishment procedure regarding solution 4 in 23.725 | 16.1.0 |
| 2019-06 | SP-84 | SP-190413 | 1278 | 3 | F | Corrections on some MM procedures | 16.1.0 |
| 2019-06 | SP-84 | SP-190401 | 1279 | 5 | A | SMF actions on rejection of PDU Session session or QoS flows during Handover and Service Request procedures | 16.1.0 |
| 2019-06 | SP-84 | SP-190408 | 1282 | 2 | F | Correction of NEF service operation information flow | 16.1.0 |
| 2019-06 | SP-84 | SP-190408 | 1285 | 1 | B | Service Gap Control Capability Indication in UE's MM Core Network Capability | 16.1.0 |
| 2019-06 | SP-84 | SP-190408 | 1286 | 5 | F | Correction of Control Plane CIoT 5GS Optimisation | 16.1.0 |
| 2019-06 | SP-84 | SP-190422 | 1289 | 4 | B | Removal invalid NOTE in Registration procedure | 16.1.0 |
| 2019-06 | SP-84 | SP-190410 | 1292 | 5 | F | SCP and NRF interaction | 16.1.0 |
| 2019-06 | SP-84 | SP-190412 | 1294 | 2 | F | Clarification on Nsmf_EventExposure_AppRelocationInfo service operation | 16.1.0 |
| 2019-06 | SP-84 | SP-190401 | 1296 | 3 | A | Correction to change of SSC mode 3 PDU session anchor | 16.1.0 |
| 2019-06 | SP-84 | SP-190420 | 1298 | 3 | C | Updating TS 23.502 with extensions to NRF Services | 16.1.0 |
| 2019-06 | SP-84 | SP-190427 | 1302 | - | F | NW Slicing Subscription Change Indication during AMF Relocation | 16.1.0 |
| 2019-06 | SP-84 | SP-190410 | 1305 | 8 | B | NF Service Context Transfer Procedures | 16.1.0 |
| 2019-06 | SP-84 | SP-190408 | 1306 | 4 | B | Extended buffering for HLCom | 16.1.0 |
| 2019-06 | SP-84 | SP-190404 | 1307 | 3 | A | Updating LCS procedures for location reporting for multiple cells | 16.1.0 |
| 2019-06 | SP-84 | SP-190401 | 1309 | - | A | Removing unnecessary PDU release during inter-system handover | 16.1.0 |
| 2019-06 | SP-84 | SP-190413 | 1310 | 1 | C | Introduce Nbsf_Management_Update service operation | 16.1.0 |
| 2019-06 | SP-84 | SP-190425 | 1313 | 1 | B | Introducing RACS for handover procedure | 16.1.0 |
| 2019-06 | SP-84 | SP-190430 | 1316 | 1 | C | Network sharing aspects for SNPNs | 16.1.0 |
| 2019-06 | SP-84 | SP-190401 | 1318 | 1 | A | AF session with required QoS procedure | 16.1.0 |
| 2019-06 | SP-84 | SP-190417 | 1321 | 1 | C | Adding Support for Indicating Serialization Format in RDS | 16.1.0 |
| 2019-06 | SP-84 | SP-190412 | 1323 | 1 | F | Generalized text for redundant user planes in RAN | 16.1.0 |
| 2019-06 | SP-84 | SP-190413 | 1324 | 3 | C | DNN replacement | 16.1.0 |
| 2019-06 | SP-84 | SP-190410 | 1325 | 3 | B | SMF context transfer | 16.1.0 |
| 2019-06 | SP-84 | SP-190410 | 1326 | 1 | F | NF Set ID, NF Service Set ID in 23.502 | 16.1.0 |
| 2019-06 | SP-84 | SP-190413 | 1328 | 3 | F | Serving 4G only UEs by SMF+PGW-C | 16.1.0 |
| 2019-06 | SP-84 | SP-190420 | 1329 | 1 | C | Adding new event in Namf_EventExposure for Network Performance Analysis | 16.1.0 |
| 2019-06 | SP-84 | SP-190401 | 1331 | 2 | A | Corrections to 3GPP and N3GPP Emergency Sessions Handover Procedures | 16.1.0 |
| 2019-06 | SP-84 | SP-190422 | 1339 | 1 | C | I-SMF notification of Access Type change to the SMF | 16.1.0 |
| 2019-06 | SP-84 | SP-190422 | 1340 | - | C | Service area of SMF(s) not transferred between AMF(s) | 16.1.0 |
| 2019-06 | SP-84 | SP-190418 | 1342 | 2 | C | S6b optional for ePDG connected to 5GS | 16.1.0 |
| 2019-06 | SP-84 | SP-190401 | 1344 | - | A | Release EPS bearer resources in SGW when EPS to 5GS handover finished | 16.1.0 |
| 2019-06 | SP-84 | SP-190408 | 1345 | 2 | F | Correction to the Release Assistance Information use | 16.1.0 |
| 2019-06 | SP-84 | SP-190401 | 1349 | 1 | A | Correction to the provisioning of the Number Of Packet Filters | 16.1.0 |
| 2019-06 | SP-84 | SP-190425 | 1350 | 2 | B | Introduction of RACS | 16.1.0 |
| 2019-06 | SP-84 | SP-190430 | 1351 | 2 | F | Adding 5GLAN N19 tunnel management | 16.1.0 |
| 2019-06 | SP-84 | SP-190422 | 1353 | 2 | F | Clarification on V-SMF changes in Roaming scenario and NRF Service update | 16.1.0 |
| 2019-06 | SP-84 | SP-190416 | 1355 | 2 | F | Network Triggered Service Request for MA PDU Session | 16.1.0 |
| 2019-06 | SP-84 | SP-190408 | 1360 | 4 | B | Introduction of UP CIoT 5GS optimisation procedures | 16.1.0 |
| 2019-06 | SP-84 | SP-190427 | 1361 | 1 | F | Use of IMEI and IMEISV | 16.1.0 |
| 2019-06 | SP-84 | SP-190427 | 1364 | 1 | F | Correction of optional parameters in Registration Request | 16.1.0 |
| 2019-06 | SP-84 | SP-190416 | 1366 | 3 | B | Reporting of Access Availability | 16.1.0 |
| 2019-06 | SP-84 | SP-190425 | 1369 | 2 | B | Assignment of UE Radio Capability ID using NAS | 16.1.0 |
| 2019-06 | SP-84 | SP-190408 | 1370 | 1 | F | Update to the UE Subscription Data Types Keys for MSISDN-less MO SMS | 16.1.0 |
| 2019-06 | SP-84 | SP-190420 | 1371 | 2 | B | Description regarding NEF support of data retrieval from external party | 16.1.0 |
| 2019-06 | SP-84 | SP-190427 | 1374 | 1 | F | Subscription Segmentation in PCF and UDR | 16.1.0 |
| 2019-06 | SP-84 | SP-190427 | 1375 | 1 | C | Serving PLMN UE-AMBR control | 16.1.0 |
| 2019-06 | SP-84 | SP-190420 | 1376 | 1 | C | NWDAF-assisted expected UE behavioural parameters provisioning | 16.1.0 |
| 2019-06 | SP-84 | SP-190415 | 1378 | 2 | B | Procedures for devices not supporting NAS over WLAN access | 16.1.0 |
| 2019-06 | SP-84 | SP-190415 | 1379 | 1 | B | Remaining procedures for trusted Non-3GPP access | 16.1.0 |
| 2019-06 | SP-84 | SP-190408 | 1383 | 1 | B | Procedure for Enhanced Coverage Restriction Control via NEF | 16.1.0 |
| 2019-06 | SP-84 | SP-190431 | 1386 | 2 | B | Adding Support for Delivering Background Data Transfer Polices to the UE | 16.1.0 |
| 2019-06 | SP-84 | SP-190408 | 1388 | 1 | B | Establishing N3 data transfer when Control Plane Optimisation is enabled | 16.1.0 |
| 2019-06 | SP-84 | SP-190419 | 1389 | 3 | B | Adding NF Group ID association functionality to UDR | 16.1.0 |
| 2019-06 | SP-84 | SP-190408 | 1396 | 1 | B | Extended buffered data forwarding for Idle mode mobility between EPS and 5GS | 16.1.0 |
| 2019-06 | SP-84 | SP-190401 | 1398 | 2 | A | Non-allowed area exemption for PS data off status change | 16.1.0 |
| 2019-06 | SP-84 | SP-190402 | 1404 | 1 | A | Fallback to CS domain if VoNR and VoLTE emergency calls not supported | 16.1.0 |
| 2019-06 | SP-84 | SP-190420 | 1405 | - | F | CR to update Nnef_EventExposure services | 16.1.0 |
| 2019-06 | SP-84 | SP-190419 | 1406 | 2 | B | NRF service enhancement to support P-CSCF discovery | 16.1.0 |
| 2019-06 | SP-84 | SP-190402 | 1408 | 1 | A | Correction to Registration with AMF relocation | 16.1.0 |
| 2019-06 | SP-84 | SP-190422 | 1409 | 2 | B | Service operation clarification and resource release | 16.1.0 |
| 2019-06 | SP-84 | SP-190422 | 1410 | 1 | C | Xn based inter NG-RAN handover clarification and removal of intermediate SMF | 16.1.0 |
| 2019-06 | SP-84 | SP-190422 | 1411 | 2 | C | Branching Point or UL CL controlled by I-SMF | 16.1.0 |
| 2019-06 | SP-84 | SP-190421 | 1412 | 1 | B | AMF reallocation for the mobility from EPS to 5GS | 16.1.0 |
| 2019-06 | SP-84 | SP-190425 | 1413 | 2 | B | PLMN-assigned capability ID deletion | 16.1.0 |
| 2019-06 | SP-84 | SP-190412 | 1416 | 2 | F | Correction on the late notification procedures of simultaneous change of Branching Point/ULCL and additional PSA for a PDU session | 16.1.0 |
| 2019-06 | SP-84 | SP-190412 | 1417 | 2 | F | Update procdures related with always-on PDU session for URLLC service | 16.1.0 |
| 2019-06 | SP-84 | SP-190420 | 1420 | 2 | C | Updating NEF and NRF Services to Support AF Available Data Registration as described in TS23.288 | 16.1.0 |
| 2019-06 | SP-84 | SP-190431 | 1422 | 2 | B | PDU session management for Background Data Transfer | 16.1.0 |
| 2019-06 | SP-84 | SP-190402 | 1424 | 3 | A | Correction to background data transfer policy procedure and related services | 16.1.0 |
| 2019-06 | SP-84 | SP-190408 | 1425 | - | B | Removal of editor's notes on new service operation for data transport in CIoT CP 5GS Optimisation | 16.1.0 |
| 2019-06 | SP-84 | SP-190408 | 1426 | 3 | B | AS RAI Handling at AN release procedure | 16.1.0 |
| 2019-06 | SP-84 | SP-190408 | 1428 | 1 | B | Procedures for Small Data Rate Control | 16.1.0 |
| 2019-06 | SP-84 | SP-190415 | 1431 | 1 | B | Sending Location information for trusted N3GPP from TNAP to TNGF | 16.1.0 |
| 2019-06 | SP-84 | SP-190413 | 1433 | 3 | F | Clarification on Network-initiated Deregistration | 16.1.0 |
| 2019-06 | SP-84 | SP-190408 | 1435 | 1 | F | Resolution of Editor's Note on classification of Suggested Number of Downlink Packets | 16.1.0 |
| 2019-06 | SP-84 | SP-190412 | 1437 | 1 | C | Update PDU Session Modification procedure regarding solution 4 | 16.1.0 |
| 2019-06 | SP-84 | SP-190408 | 1438 | 1 | B | Missing Monitoring Event functionality | 16.1.0 |
| 2019-06 | SP-84 | SP-190408 | 1439 | 2 | B | monitoring procedures involving I-NEF | 16.1.0 |
| 2019-06 | SP-84 | SP-190402 | 1441 | - | A | Clarification on event ID of NEF event exposure service operation | 16.1.0 |
| 2019-06 | SP-84 | SP-190427 | 1447 | 1 | F | Clarification to mapping of non-GBR QoS Flows to EPS Bearers | 16.1.0 |
| 2019-06 | SP-84 | SP-190408 | 1449 | 1 | F | Control Plane Only Indication during PDU session establishment | 16.1.0 |
| 2019-06 | SP-84 | SP-190402 | 1450 | 1 | F | Capturing 23.402 impacts for 5GS interworking | 16.1.0 |
| 2019-06 | SP-84 | SP-190402 | 1452 | 1 | A | Correction on usage of Direct Forwarding Path Availability during handovers | 16.1.0 |
| 2019-06 | SP-84 | SP-190402 | 1455 | - | A | Missing operations for Nnssf_NSSAIAvailability service | 16.1.0 |
| 2019-06 | SP-84 | SP-190402 | 1456 | - | A | Clarification on S-NSSAI for PDU session | 16.1.0 |
| 2019-06 | SP-84 | SP-190402 | 1457 | - | A | Corrections to data forwarding during inter-system HO | 16.1.0 |
| 2019-06 | SP-84 | SP-190463 | 1457 | - | A | Correction for NF authorized to request notification for UE reachability | 16.1.0 |
| 2019-06 | SP-84 | REMOVED | 1324 | 3 | C | Removal of postponed CR from v16.1.0, added in error. DNN replacement | 16.1.1 |
| 2019-06 | SP-84 | SP-190413 | 1415 | 1 | A | Addition of CR missed in error in v16.1.0: Correction on procedure of simultaneous change of BP/ULCL and additional PSA | 16.1.1 |
| 2019-09 | SP-85 | MCC | 1234 | 1 | B | Correction of implementation of clauses 5.2.6.15.3 and 5.2.6.15.4 | 16.2.0 |
| 2019-09 | SP-85 | SP-190608 | 1126 | 4 | B | QoS Monitoring to assist URLLC Service | 16.2.0 |
| 2019-09 | SP-85 | SP-190618 | 1322 | 2 | F | Removing NID from 5GS to EPS handover procedure description | 16.2.0 |
| 2019-09 | SP-85 | SP-190621 | 1324 | 7 | C | DNN replacement | 16.2.0 |
| 2019-09 | SP-85 | SP-190605 | 1373 | 2 | F | NIDD Configuration Procedure Update for RDS and Maximum Packet Size | 16.2.0 |
| 2019-09 | SP-85 | SP-190607 | 1382 | 4 | B | Procedures and call flows for SMF Delegated Discovery and Selection in HR and specific SMF Service Areas scenarios and PCF Delegated Discovery and Selection | 16.2.0 |
| 2019-09 | SP-85 | SP-190621 | 1391 | 4 | F | Clarification on the target CN handling in Emergency Service Fallback | 16.2.0 |
| 2019-09 | SP-85 | SP-190610 | 1392 | 2 | F | MA-PDU Session Management | 16.2.0 |
| 2019-09 | SP-85 | SP-190607 | 1393 | 10 | B | Service Context Transfer Support via indirect Transfer | 16.2.0 |
| 2019-09 | SP-85 | SP-190605 | 1429 | 1 | F | Stateless IPv6 Address Autoconfiguration for Control Plane CIoT 5GS Optimisation | 16.2.0 |
| 2019-09 | SP-85 | SP-190610 | 1442 | 3 | B | Update the MA PDU session establishment procedure | 16.2.0 |
| 2019-09 | SP-85 | SP-190615 | 1445 | 7 | B | Enhancements to QoS Handling for V2X Communication Over Uu Reference Point | 16.2.0 |
| 2019-09 | SP-85 | SP-190612 | 1459 | - | F | Removal of Level of aggregation from Event Reporting Information Parameters | 16.2.0 |
| 2019-09 | SP-85 | SP-190605 | 1461 | 2 | F | NAS RAI corrections | 16.2.0 |
| 2019-09 | SP-85 | SP-190617 | 1463 | 3 | F | PLMN assigned Radio Capability ID transfer during Inter PLMN mobility | 16.2.0 |
| 2019-09 | SP-85 | SP-190618 | 1464 | 3 | C | Introducing support for Ethernet port management | 16.2.0 |
| 2019-09 | SP-85 | SP-190618 | 1466 | 1 | F | 5G LAN group management procedure corrections | 16.2.0 |
| 2019-09 | SP-85 | SP-190622 | 1468 | 1 | F | Specification of SMF behaviour at PDU Session setup and modification failure | 16.2.0 |
| 2019-09 | SP-85 | SP-190607 | 1469 | 3 | F | On set identifiers at Nnrf_NFDiscovery_Request | 16.2.0 |
| 2019-09 | SP-85 | SP-190606 | 1473 | - | C | MO-LR Subscription data to AMF at registration | 16.2.0 |
| 2019-09 | SP-85 | SP-190606 | 1475 | - | C | Location privacy setting from AF | 16.2.0 |
| 2019-09 | SP-85 | SP-190621 | 1479 | 3 | F | Replacement of VPLMN by serving PLMN where appropriate | 16.2.0 |
| 2019-09 | SP-85 | SP-190605 | 1481 | 3 | F | Update to downlink data delivery status event to support PCC and HR roaming | 16.2.0 |
| 2019-09 | SP-85 | SP-190621 | 1483 | 2 | F | Clarification on UE context removal and PDU Session release in General Registration | 16.2.0 |
| 2019-09 | SP-85 | SP-190621 | 1484 | 2 | F | DNN Configuration for interworking with EPS | 16.2.0 |
| 2019-09 | SP-85 | SP-190605 | 1485 | - | F | Aligning Terminology referring to the CIoT 5GS Optimisations | 16.2.0 |
| 2019-09 | SP-85 | SP-190617 | 1486 | 1 | C | Corrections of PLMN assigned Capability signalling | 16.2.0 |
| 2019-09 | SP-85 | SP-190621 | 1487 | 3 | F | UEs not supporting 5GC NAS connected to SMF+PGW-C | 16.2.0 |
| 2019-09 | SP-85 | SP-190621 | 1488 | 1 | F | Handover from EPC/ePDG to 5GS | 16.2.0 |
| 2019-09 | SP-85 | SP-190621 | 1493 | 2 | B | CN identifier coordination | 16.2.0 |
| 2019-09 | SP-85 | SP-190622 | 1494 | - | F | Correction of AN Release procedure | 16.2.0 |
| 2019-09 | SP-85 | SP-190621 | 1495 | 1 | F | Correction of Network Slice selection information | 16.2.0 |
| 2019-09 | SP-85 | SP-190605 | 1496 | - | F | Follow-on indication in initial registration for Service Gap | 16.2.0 |
| 2019-09 | SP-85 | SP-190601 | 1498 | - | A | Discrepancy with TS 33.501 with respect to Secondary Authentication | 16.2.0 |
| 2019-09 | SP-85 | SP-190608 | 1499 | 2 | F | Failure handling for redundancy based on dual connectivity | 16.2.0 |
| 2019-09 | SP-85 | SP-190617 | 1501 | 1 | B | Optimised sending of PEI in 5GS | 16.2.0 |
| 2019-09 | SP-85 | SP-190621 | 1504 | 1 | F | Erroneous implementation of CR1263R3 and further clarification | 16.2.0 |
| 2019-09 | SP-85 | SP-190864 | 1659 | - | F | Clarifications to Slice-Specific Authentication and Authorisation | 16.2.0 |
| 2019-09 | SP-85 | SP-190622 | 1507 | 1 | F | S6b optional for ePDG connected to 5GS | 16.2.0 |
| 2019-09 | SP-85 | SP-190605 | 1510 | 3 | F | UE Indication of support for the User Plane CIoT Optimisation in RRC Message when RAT Type is not NR | 16.2.0 |
| 2019-09 | SP-85 | SP-190605 | 1511 | - | F | Corrections on setting the Invoke NEF Flag during PDU Session Establishment | 16.2.0 |
| 2019-09 | SP-85 | SP-190621 | 1512 | 2 | F | Correction on Intra-5GC HO description | 16.2.0 |
| 2019-09 | SP-85 | SP-190622 | 1514 | 1 | F | Avoiding EPS to 5GS handover for voice | 16.2.0 |
| 2019-09 | SP-85 | SP-190622 | 1518 | 1 | F | End Marker for the PDU session of HR roaming | 16.2.0 |
| 2019-09 | SP-85 | SP-190614 | 1519 | 1 | F | ETSUN: End Marker handling | 16.2.0 |
| 2019-09 | SP-85 | SP-190614 | 1520 | - | F | UL-CL/BP change control | 16.2.0 |
| 2019-09 | SP-85 | SP-190621 | 1523 | 2 | F | Correction on emergency service fallback | 16.2.0 |
| 2019-09 | SP-85 | SP-190617 | 1524 | 2 | F | NB-IoT and other RATs capabilities coexistence | 16.2.0 |
| 2019-09 | SP-85 | SP-190601 | 1528 | 3 | A | Correction to setting up an AF session with required QoS | 16.2.0 |
| 2019-09 | SP-85 | SP-190619 | 1529 | 2 | F | Correction to the Background Data Transfer policy determination and usage | 16.2.0 |
| 2019-09 | SP-85 | SP-190608 | 1530 | 1 | F | Update of AN release procedure for URLLC service | 16.2.0 |
| 2019-09 | SP-85 | SP-190622 | 1532 | 1 | F | Correction on NRF Service Consumer | 16.2.0 |
| 2019-09 | SP-85 | SP-190614 | 1535 | 3 | F | Corrections to clause 4.23 (ETSUN) | 16.2.0 |
| 2019-09 | SP-85 | SP-190607 | 1539 | 4 | F | Update SM context transfer procedure | 16.2.0 |
| 2019-09 | SP-85 | SP-190612 | 1541 | 3 | F | Clarifications to AMF and SMF Event Exposure Services | 16.2.0 |
| 2019-09 | SP-85 | SP-190611 | 1545 | 1 | F | NF Group resolution by SCP | 16.2.0 |
| 2019-09 | SP-85 | SP-190601 | 1551 | 2 | A | Location Reporting signalling load | 16.2.0 |
| 2019-09 | SP-85 | SP-190621 | 1554 | 1 | F | Correction of optional parameters | 16.2.0 |
| 2019-09 | SP-85 | SP-190605 | 1556 | 1 | F | Conditions to use CP or UP CIoT | 16.2.0 |
| 2019-09 | SP-85 | SP-190621 | 1557 | 1 | F | Nudm_SDM_Get consumer NFs | 16.2.0 |
| 2019-09 | SP-85 | SP-190614 | 1559 | 2 | F | IWK IDLE mode mobility using N26 interface with I-SMF/I-UPF | 16.2.0 |
| 2019-09 | SP-85 | SP-190621 | 1561 | 1 | F | Enabling AF data synchronization | 16.2.0 |
| 2019-09 | SP-85 | SP-190601 | 1563 | 1 | A | Update CN-initiated selective deactivation of UP connection of an existing PDU Session procedure | 16.2.0 |
| 2019-09 | SP-85 | SP-190605 | 1565 | 2 | F | Corrections to N3 data transfer establishment procedures | 16.2.0 |
| 2019-09 | SP-85 | SP-190621 | 1570 | 1 | F | N2 AMF Mobility: Alignment with TS 29.413 | 16.2.0 |
| 2019-09 | SP-85 | SP-190610 | 1572 | 1 | F | N2 AMF Mobility: Alignment with TS 29.413 | 16.2.0 |
| 2019-09 | SP-85 | SP-190619 | 1573 | 1 | F | New Nnef_ApplyPolicy service operation | 16.2.0 |
| 2019-09 | SP-85 | SP-190622 | 1581 | 1 | F | UDR information for network functions authorized to request notifications on UE's reachability | 16.2.0 |
| 2019-09 | SP-85 | SP-190605 | 1583 | 3 | F | Clarification on NEF discovery by an AF | 16.2.0 |
| 2019-09 | SP-85 | SP-190618 | 1591 | 1 | F | Adding NID as input for policy decisions | 16.2.0 |
| 2019-09 | SP-85 | SP-190612 | 1595 | 2 | D | CR for editorial corrections on Nnf_EventExposure_Subscribe service | 16.2.0 |
| 2019-09 | SP-85 | SP-190607 | 1597 | 2 | F | Update of context transfer procedures | 16.2.0 |
| 2019-09 | SP-85 | SP-190618 | 1600 | 3 | B | TSC Update to Service Operations to Support TSC | 16.2.0 |
| 2019-09 | SP-85 | SP-190622 | 1603 | 1 | F | PDU Session Establishment for TSC | 16.2.0 |
| 2019-09 | SP-85 | SP-190609 | 1605 | 1 | F | Clarification on QoS resource release in trusted non-3GPP access | 16.2.0 |
| 2019-09 | SP-85 | SP-190610 | 1607 | 2 | F | Handling of access addition - Option 2 | 16.2.0 |
| 2019-09 | SP-85 | SP-190610 | 1611 | 4 | B | EPS interworking for MA PDU | 16.2.0 |
| 2019-09 | SP-85 | SP-190601 | 1614 | 1 | A | Corrections for support of Static IP Address | 16.2.0 |
| 2019-09 | SP-85 | SP-190605 | 1620 | - | F | Clarification of Service Gap Control Capability indication | 16.2.0 |
| 2019-09 | SP-85 | SP-190610 | 1622 | 1 | F | De-activating user-plane resources over one access | 16.2.0 |
| 2019-09 | SP-85 | SP-190614 | 1624 | 1 | F | Correction on PDU Session Release/Modification related to ETSUN | 16.2.0 |
| 2019-09 | SP-85 | SP-190608 | 1625 | 1 | F | Clarification and correction to AF response | 16.2.0 |
| 2019-09 | SP-85 | SP-190608 | 1626 | - | F | Correction on the AF subscribed notification procedures of session &amp; service cotinuity and UP path management scenarios | 16.2.0 |
| 2019-09 | SP-85 | SP-190605 | 1629 | - | F | Update the SMF discovery and selection regarding the Contorl Plane/User Plane CIoT 5GS Optimisations | 16.2.0 |
| 2019-09 | SP-85 | SP-190605 | 1630 | 1 | F | Clarification on the buffered data delivery | 16.2.0 |
| 2019-09 | SP-85 | SP-190609 | 1633 | 2 | F | Deregistration procedure for trusted non-3GPP access | 16.2.0 |
| 2019-09 | SP-85 | SP-190618 | 1639 | 3 | B | Burst Arrival Time Clock Reference Adjustment Procedure | 16.2.0 |
| 2019-09 | SP-85 | SP-190618 | 1642 | 4 | B | Procedures for 5GS Bridge information reporting and configuration | 16.2.0 |
| 2019-09 | SP-85 | SP-190605 | 1643 | 1 | F | Clarification on Preferred Network Behaviour for CIoT 5GS Optimisations | 16.2.0 |
| 2019-09 | SP-85 | SP-190605 | 1644 | 1 | F | RAI Terminology Alignment on CIoT 5GS Optimisations | 16.2.0 |
| 2019-09 | SP-85 | SP-190605 | 1646 | - | F | Clarification on Service Operation for Extended Buffering Support | 16.2.0 |
| 2019-09 | SP-85 | SP-190612 | 1652 | 2 | F | Updating the inputs related to BSF discovery | 16.2.0 |
| 2019-09 | SP-85 | SP-190614 | 1655 | - | F | Correction to clause 4.23.9.3 | 16.2.0 |
| 2019-09 | SP-85 | SP-190613 | 1656 | - | B | MCC implementation correction CR: Slice Specific Authentication and Authorization with multiple registrations in the same PLMN | 16.2.0 |
| 2019-12 | SP-86 | SP-191069 | 1372 | 2 | B | Identification of LTE-M (eMTC) traffic | 16.3.0 |
| 2019-12 | SP-86 | SP-191075 | 1380 | 4 | F | Aligning Trusted and Untrusted Non-3GPP Access with respect to the Additional QoS Information | 16.3.0 |
| 2019-12 | SP-86 | SP-191076 | 1465 | 2 | F | Registration procedure updates for W-AGF interactions | 16.3.0 |
| 2019-12 | SP-86 | SP-191071 | 1470 | 5 | F | Binding when a consumer later becomes a producer | 16.3.0 |
| 2019-12 | SP-86 | SP-191070 | 1474 | 1 | F | Add VGMLC ID to UE context data in Nudm_CM_Registration | 16.3.0 |
| 2019-12 | SP-86 | SP-191080 | 1477 | 6 | F | BDT renegotiation upon expected network performance change | 16.3.0 |
| 2019-12 | SP-86 | SP-191069 | 1482 | 8 | F | Corrections to Availability after DDN Failure event | 16.3.0 |
| 2019-12 | SP-86 | SP-191069 | 1516 | 3 | F | Monitoring Event Subscription and Network Configuration correction | 16.3.0 |
| 2019-12 | SP-86 | SP-191088 | 1546 | 3 | F | Correction to deletion of PLMN-assigned UE Radio Capability ID | 16.3.0 |
| 2019-12 | SP-86 | SP-191069 | 1555 | 2 | F | Group reporting guard time correction | 16.3.0 |
| 2019-12 | SP-86 | SP-191069 | 1587 | 3 | F | Support for PDN Connectivity Status monitoring event | 16.3.0 |
| 2019-12 | SP-86 | SP-191071 | 1601 | 1 | F | UDR Group ID Mapping service | 16.3.0 |
| 2019-12 | SP-86 | SP-191077 | 1616 | 2 | F | Subscription information check for ATSSS | 16.3.0 |
| 2019-12 | SP-86 | SP-191080 | 1617 | 3 | F | Nnef_NetworkStatus service | 16.3.0 |
| 2019-12 | SP-86 | SP-191080 | 1627 | 4 | F | Support of abnormal behaviour analytics | 16.3.0 |
| 2019-12 | SP-86 | SP-191076 | 1635 | 1 | F | NULL encryption for trusted non-3GPP access | 16.3.0 |
| 2019-12 | SP-86 | SP-191069 | 1645 | 3 | F | Corrections to Small Data Rate Control and Exception Reporting | 16.3.0 |
| 2019-12 | SP-86 | SP-191071 | 1647 | 1 | F | NRF Discovery Service Update | 16.3.0 |
| 2019-12 | SP-86 | SP-191075 | 1661 | 1 | F | Correction of PEI(IMEISV) in Registration procedures | 16.3.0 |
| 2019-12 | SP-86 | SP-191069 | 1668 | 1 | F | Clarification on provisionning of NIDD related identifiers | 16.3.0 |
| 2019-12 | SP-86 | SP-191082 | 1670 | 3 | F | Correction to N16a for the transfer of N4 requests from SMF / responses from local UPF | 16.3.0 |
| 2019-12 | SP-86 | SP-191075 | 1675 | 4 | F | Clarification on Registration with AMF re-allocation | 16.3.0 |
| 2019-12 | SP-86 | SP-191075 | 1678 |  | F | Rename of Accumulated Usage data | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1679 | 3 | F | Clarification on DNN replacement | 16.3.0 |
| 2019-12 | SP-86 | SP-191075 | 1680 | 2 | F | Missing Date subset in UDR | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1682 | 1 | F | clarification on N6 traffic routing information for Ethernet type PDU Session | 16.3.0 |
| 2019-12 | SP-86 | SP-191077 | 1686 | 2 | F | ATSSS Capability for PCF | 16.3.0 |
| 2019-12 | SP-86 | SP-191077 | 1687 | 2 | F | Update on Home-Routed roaming | 16.3.0 |
| 2019-12 | SP-86 | SP-191073 | 1691 | 1 | C | Update on services/procedures for QoS Monitoring | 16.3.0 |
| 2019-12 | SP-86 | SP-191075 | 1697 | - | F | Corrections on Registration, UCU and AN release procedures | 16.3.0 |
| 2019-12 | SP-86 | SP-191082 | 1698 | 2 | F | Clarification on IPv6 Router Advertisement message in ETSUN | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1701 | 1 | F | Corrections on Nsmf_PDUSession Notify services | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1703 | - | F | End marker in service request procedure | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1704 | 2 | F | Correction to Service Request procedure | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1705 | 1 | F | Correction of message in EBI allocation | 16.3.0 |
| 2019-12 | SP-86 | SP-191077 | 1708 | 1 | F | 23502 Clarification of Access Availability report via N4 | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1709 | 1 | F | Add secondary authentication parameter in subscription data | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1710 | 2 | F | Corrections to N26 based Interworking Procedures | 16.3.0 |
| 2019-12 | SP-86 | SP-191080 | 1712 | - | F | Correction of NEF Event Exposure | 16.3.0 |
| 2019-12 | SP-86 | SP-191080 | 1713 | - | F | UDM Discovery by Internal Group ID | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1715 | 4 | F | SMS Correction to handle SMS-Termination when a UE is not able to receive SMS | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1716 | 1 | F | SMS Clarification | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1718 | 1 | F | UEs not supporting 5GC NAS connected to SMF+PGW-C | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1719 | - | F | Correction on UDM registration and deregistrion service operations by SMF and alignment with stage 3 | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1720 | 2 | F | PCF selection for multiple PDU Sessions to the same DNN and S-NSSAI | 16.3.0 |
| 2019-12 | SP-86 | SP-191069 | 1721 | 2 | F | Correction of UDM subscription to Nsmf_EventExposure | 16.3.0 |
| 2019-12 | SP-86 | SP-191073 | 1726 | - | F | Establish redundant N3/N9 transmission for an existing QoS Flow | 16.3.0 |
| 2019-12 | SP-86 | SP-191069 | 1727 | 1 | F | Extended NAS timers for CE mode B | 16.3.0 |
| 2019-12 | SP-86 | SP-191069 | 1728 | 2 | F | NIDD procedure corrections | 16.3.0 |
| 2019-12 | SP-86 | SP-191092 | 1729 | 3 | F | Addressing open issues for Ethernet port management | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1735 | 1 | F | Session activation in registration procedure | 16.3.0 |
| 2019-12 | SP-86 | SP-191082 | 1736 | 4 | F | ETSUN:SM Context | 16.3.0 |
| 2019-12 | SP-86 | SP-191082 | 1737 | 1 | F | ETSUN: Update procedures | 16.3.0 |
| 2019-12 | SP-86 | SP-191071 | 1738 | - | F | Correction of PCF discovery via BSF to consider eSBA binding principles | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1739 | 1 | F | Update to Clause 5.2.5.2.2 Npcf_AMPolicyControl_Create service operation | 16.3.0 |
| 2019-12 | SP-86 | SP-191078 | 1762 | - | F | UDR service for mapping IMS Public Identity to HSS Group ID for HSS selection | 16.3.0 |
| 2019-12 | SP-86 | SP-191071 | 1766 | 1 | F | Correction on SM context transfer procedure | 16.3.0 |
| 2019-12 | SP-86 | SP-191077 | 1767 | 4 | F | Updating AMF/SMF/PCF service operations for ATSSS | 16.3.0 |
| 2019-12 | SP-86 | SP-191075 | 1768 | 1 | F | Clarification on fallback procedures | 16.3.0 |
| 2019-12 | SP-86 | SP-191077 | 1769 | 5 | F | Corrections for MA PDU session handling | 16.3.0 |
| 2019-12 | SP-86 | SP-191077 | 1770 | 2 | F | Corrections to interworking with EPS for ATSSS | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1771 | 2 | F | PCF selection for DNN replacement | 16.3.0 |
| 2019-12 | SP-86 | SP-191071 | 1774 | - | F | Update to delegated discovery procedure with binding indication | 16.3.0 |
| 2019-12 | SP-86 | SP-191069 | 1775 | 2 | F | Clarification on MAC AS RAI in 5GC | 16.3.0 |
| 2019-12 | SP-86 | SP-191069 | 1779 | 2 | F | Correction to DDD status event with SMF buffering | 16.3.0 |
| 2019-12 | SP-86 | SP-191080 | 1782 | 2 | F | List the Event IDs in the AF services and the NEF services | 16.3.0 |
| 2019-12 | SP-86 | SP-191084 | 1784 | 2 | F | Update to service specific parameter provisioning procedure | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1785 | 2 | F | AF session with QoS - Flow description | 16.3.0 |
| 2019-12 | SP-86 | SP-191069 | 1791 | 2 | F | N3 tunnel info handling during Suspend and Resume procedure | 16.3.0 |
| 2019-12 | SP-86 | SP-191086 | 1793 | 1 | F | IAB node Registration procedure | 16.3.0 |
| 2019-12 | SP-86 | SP-191092 | 1799 | 1 | F | Removing NID from Xn based inter NG-RAN handover procedure | 16.3.0 |
| 2019-12 | SP-86 | SP-191081 | 1801 | - | F | TS 23.502: Correction of UE Identity in NSSAA role | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1803 | 1 | F | Clarification on the CN tunnel information in relocation response. | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1804 | 3 | F | adding direct forwarding during HO between EPS and 5GS | 16.3.0 |
| 2019-12 | SP-86 | SP-191069 | 1807 | 1 | F | AMF and SMF merging subscription parameters | 16.3.0 |
| 2019-12 | SP-86 | SP-191069 | 1808 | 4 | F | Correction of Small Data Rate Control interworking | 16.3.0 |
| 2019-12 | SP-86 | SP-191069 | 1809 | 2 | F | Group NIDD corrections | 16.3.0 |
| 2019-12 | SP-86 | SP-191069 | 1810 | 2 | F | Monitoring event triggers | 16.3.0 |
| 2019-12 | SP-86 | SP-191092 | 1812 | 1 | F | Implement traffic correlation indicaiton of AF influence | 16.3.0 |
| 2019-12 | SP-86 | SP-191088 | 1814 | 4 | F | removing requirement that TAC+SV is used to identify UE model in manufacturer assigned ID | 16.3.0 |
| 2019-12 | SP-86 | SP-191081 | 1815 | 4 | F | On NSSAA | 16.3.0 |
| 2019-12 | SP-86 | SP-191071 | 1817 | 1 | F | Correction of the SMF Context Transfer procedure and services | 16.3.0 |
| 2019-12 | SP-86 | SP-191071 | 1819 | 3 | F | Update of the binding procedures | 16.3.0 |
| 2019-12 | SP-86 | SP-191080 | 1824 | 3 | F | Event Id on QFI allocation | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1826 | 3 | F | Clarification on handover failure between 3GPP and non-3GPP accesses | 16.3.0 |
| 2019-12 | SP-86 | SP-191057 | 1834 | 2 | A | UE IPv4 Address/IPv6 Prefix as query parameters for UPF discovery using NRF | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1835 | 2 | F | Incorrect service reference for SMF provisioning | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1836 | - | F | Missing AUSF Service | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1837 | - | F | Missing reference to UE Parameters Update via UDM Control Plane Procedure | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1842 | 2 | F | Correcting small issues in failure cases at UE mobility | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1846 | 2 | F | SMS transmission in Expected UE Behaviour parameters | 16.3.0 |
| 2019-12 | SP-86 | SP-191073 | 1847 | 1 | F | 5G URLLC Handling PDU Session Failure - 23.502 | 16.3.0 |
| 2019-12 | SP-86 | SP-191071 | 1849 | 1 | F | Clarification on SMF identifier in HR roaming | 16.3.0 |
| 2019-12 | SP-86 | SP-191088 | 1853 | 3 | F | RAC ID during inter-PLMN handover case | 16.3.0 |
| 2019-12 | SP-86 | SP-191071 | 1855 | 5 | C | Consumer/Producer binding for subscribe/notify | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1859 | 2 | F | Correction to the access authentication for untrusted non-3GPP access | 16.3.0 |
| 2019-12 | SP-86 | SP-191076 | 1860 | 2 | F | TWIF co-located with UPF | 16.3.0 |
| 2019-12 | SP-86 | SP-191076 | 1861 | 2 | F | TNGF co-located with UPF | 16.3.0 |
| 2019-12 | SP-86 | SP-191082 | 1865 | 1 | F | Relation between mobility events and control local offload in ETSUN cases | 16.3.0 |
| 2019-12 | SP-86 | SP-191059 | 1867 | 2 | F | MO EDT for User Plane CIoT 5GS Optimisation | 16.3.0 |
| 2019-12 | SP-86 | SP-191069 | 1868 | 3 | F | Enforcing maximum UP resources activation of 2 PDU sessions for NB-IoT | 16.3.0 |
| 2019-12 | SP-86 | SP-191092 | 1870 | 2 | F | 5G LAN group management procedure corrections | 16.3.0 |
| 2019-12 | SP-86 | SP-191075 | 1871 | 2 | D | SMF IP Change Event Clarification | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1872 | 4 | F | SoR support for different registration types | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1874 | 2 | F | Event Id for SMSF Registration Notification Events | 16.3.0 |
| 2019-12 | SP-86 | SP-191115 | 1875 | 2 | F | Correction to EPS-5GS idle mobility with N26 | 16.3.0 |
| 2019-12 | SP-86 | SP-191077 | 1880 | 2 | F | Applicability of UP Security Policy to a MA PDU Session | 16.3.0 |
| 2019-12 | SP-86 | SP-191081 | 1881 | 2 | F | Correction on pending NSSAA indication to UE | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1883 | 2 | F | NR-U secondary RAT usage report | 16.3.0 |
| 2019-12 | SP-86 | SP-191072 | 1885 | - | F | Clarification on SRVCC indication during PDU session release | 16.3.0 |
| 2019-12 | SP-86 | SP-191073 | 1887 | 2 | F | Clarification on URLLC support in Session Modification Procedure | 16.3.0 |
| 2019-12 | SP-86 | SP-191082 | 1888 | 1 | F | Clarification on the L-PSA handling during HO/SR in ETSUN case. | 16.3.0 |
| 2019-12 | SP-86 | SP-191080 | 1889 | 1 | F | Add NWDAF as consumer of NF Services | 16.3.0 |
| 2019-12 | SP-86 | SP-191088 | 1890 | 2 | F | Clarification on UCMF service | 16.3.0 |
| 2019-12 | SP-86 | SP-191088 | 1891 | 2 | F | Supporting bulk dictionary entries creation and deletion for UCMF service | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1893 | - | F | Correction to NAI used for registration via trusted non-3GPP access | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1894 | 3 | F | EBI management for QoS flow | 16.3.0 |
| 2019-12 | SP-86 | SP-191082 | 1897 | 2 | F | IRAT Mobility procedure with I-SMF involved | 16.3.0 |
| 2019-12 | SP-86 | SP-191093 | 1899 | - | F | Propose updated to Application Data in UDR | 16.3.0 |
| 2019-12 | SP-86 | SP-191092 | 1900 | 2 | F | Group Subscription Data and Group Identifiers in Nudm and Nudr services | 16.3.0 |
| 2019-12 | SP-86 | SP-191077 | 1902 | - | F | Reporting of Access Availability | 16.3.0 |
| 2019-12 | SP-86 | SP-191080 | 1905 | - | F | Update to Naf_EventExposure_Subscribe service operation | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1907 | 3 | F | Clarification on Policy Control Request Triggers | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1908 | 2 | F | SMF selection for Static IP address | 16.3.0 |
| 2019-12 | SP-86 | SP-191071 | 1909 |  | F | PCF Set support | 16.3.0 |
| 2019-12 | SP-86 | SP-191085 | 1911 | - | F | Event Id for UserStatus Retrieval Events | 16.3.0 |
| 2019-12 | SP-86 | SP-191069 | 1916 | 1 | F | Small Data transfer for CP CIoT | 16.3.0 |
| 2019-12 | SP-86 | SP-191084 | 1917 | 1 | F | Corrections to handling of Alternative QoS Profiles | 16.3.0 |
| 2019-12 | SP-86 | SP-191063 | 1918 | 2 | F | Enhancements to QoS Handling for V2X Communication Over Uu Reference Point | 16.3.0 |
| 2019-12 | SP-86 | SP-191073 | 1923 | - | F | Correction on Xn-based HO procedure regarding N3/N9 redundant transmission | 16.3.0 |
| 2019-12 | SP-86 | SP-191084 | 1924 | 2 | F | Revoke Alternative Service Requirement request | 16.3.0 |
| 2019-12 | SP-86 | SP-191069 | 1927 | 1 | F | Corrections to Small Data Rate Control in PDU Session Establishment Procedure | 16.3.0 |
| 2019-12 | SP-86 | SP-191069 | 1929 | 1 | F | Corrections to RDS Configuration in the PDU Session Establishment procedure | 16.3.0 |
| 2019-12 | SP-86 | SP-191060 | 1931 | - | F | Availability after DDN Failure event with UPF buffering procedure | 16.3.0 |
| 2019-12 | SP-86 | SP-191081 | 1934 | 3 | F | Service used for slice-specific re-authentication and revocation | 16.3.0 |
| 2019-12 | SP-86 | SP-191081 | 1936 | 2 | F | Addition of NSSAA Services | 16.3.0 |
| 2019-12 | SP-86 | SP-191092 | 1940 | 2 | F | Support for Untrusted Non-3GPP access for SNPN | 16.3.0 |
| 2019-12 | SP-86 | SP-191091 | 1941 | 4 | F | Use of EPS/RAT fallback for VoWiFi session | 16.3.0 |
| 2019-12 | SP-86 | SP-191063 | 1943 | 1 | C | Signalling updated QoS parameters to the UE | 16.3.0 |
| 2019-12 | SP-86 | SP-191081 | 1944 | 2 | F | NSSAA at mobility | 16.3.0 |
| 2019-12 | SP-86 | SP-191080 | 1946 | - | F | Corrections to Nnrf service operations for NWDAF | 16.3.0 |
| 2019-12 | SP-86 | SP-191082 | 1947 | 2 | F | Minor corrections related with ETSUN | 16.3.0 |
| 2019-12 | SP-86 | SP-191075 | 1950 | - | F | Adding missing interactions in PDU session release | 16.3.0 |
| 2019-12 | SP-86 | SP-191070 | 1952 | - | F | Add AMF as consumer for Nudm_ParametereProvision_Update Service Operation | 16.3.0 |
| 2020-03 | SP-87E | SP-200077 | 1582 | 2 | F | 23.502 Supporting for AF providing UE IP address(es) for 5G VN group PDU sessions | 16.4.0 |
| 2020-03 | SP-87E | SP-200063 | 1590 | 6 | F | Idle mode mobility with data fowarding | 16.4.0 |
| 2020-03 | SP-87E | SP-200063 | 1667 | 3 | F | Corrections on Extended Buffering | 16.4.0 |
| 2020-03 | SP-87E | SP-200077 | 1673 | 7 | F | UPF reporting the time comparison | 16.4.0 |
| 2020-03 | SP-87E | SP-200060 | 1685 | 4 | A | Correction on UE Policy Association Establishment procedure | 16.4.0 |
| 2020-03 | SP-87E | SP-200077 | 1763 | 2 | F | Adding Information about serving network to Nsmf_PDUSession service | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 1773 | 4 | F | UE IDLE over N3GPP responding to indication of DL data when access is available | 16.4.0 |
| 2020-03 | SP-87E | SP-200063 | 1776 | 2 | F | Correction to UE context in AMF for Power Saving Function | 16.4.0 |
| 2020-03 | SP-87E | SP-200077 | 1792 | 4 | F | Adding Information about serving network to Nudm and Nudr services | 16.4.0 |
| 2020-03 | SP-87E | SP-200077 | 1796 | 7 | F | Support of CAG ID privacy | 16.4.0 |
| 2020-03 | SP-87E | SP-200077 | 1797 | 4 | F | NID parameter for SNPN N3IWF deployments | 16.4.0 |
| 2020-03 | SP-87E | SP-200072 | 1825 | 6 | F | IWK IDLE mode mobility using N26 interface with I-SMF/I-UPF and data forwarding | 16.4.0 |
| 2020-03 | SP-87E | SP-200069 | 1840 | 4 | F | Correction on MA PDU Session Release | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 1878 | 3 | F | AMF registering in UDM and HSS+UDM cancelling the old serving node at initial Registration | 16.4.0 |
| 2020-03 | SP-87E | SP-200069 | 1906 | 2 | F | Clarification on Access type for ATSSS | 16.4.0 |
| 2020-03 | SP-87E | SP-200063 | 1930 | 6 | F | DDD status event with UPF buffering procedure | 16.4.0 |
| 2020-03 | SP-87E | SP-200068 | 1950 | 2 | F | Access type and RAT type per Non-3GPP accesses | 16.4.0 |
| 2020-03 | SP-87E | SP-200071 | 1953 | 5 | F | Release PDU sessions due to revocation from AAA server or re-auth failure | 16.4.0 |
| 2020-03 | SP-87E | SP-200077 | 1956 | 4 | F | PNI-NPN CAG Configuration Update | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 1957 | 2 | F | Update to Emergency Services Fallback | 16.4.0 |
| 2020-03 | SP-87E | SP-200065 | 1959 | 3 | F | Binding for notification reselection corrections | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 1960 | 3 | F | Update Alternative Service Requirement request | 16.4.0 |
| 2020-03 | SP-87E | SP-200065 | 1961 | 4 | F | Applicability of binding indication | 16.4.0 |
| 2020-03 | SP-87E | SP-200065 | 1962 | 4 | F | Additional Usage scenarios for binding when a consumer later becomes a producer | 16.4.0 |
| 2020-03 | SP-87E | SP-200072 | 1963 | 1 | F | Clean up of I/V/SMF selection | 16.4.0 |
| 2020-03 | SP-87E | SP-200072 | 1964 | 1 | F | ETSUN corrections | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 1966 | 2 | F | Correction on EPS Fallback procedure | 16.4.0 |
| 2020-03 | SP-87E | SP-200069 | 1969 | 2 | F | AMF decision for the network convert MA PDU | 16.4.0 |
| 2020-03 | SP-87E | SP-200069 | 1970 | 3 | F | Corrections on interworking with EPS | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 1973 | 2 | F | Missing Non-UE N2 Message Services Operations | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 1976 | 3 | F | Alignment with stage 3 on Immediate Report for Nudm_SDM_Subscribe | 16.4.0 |
| 2020-03 | SP-87E | SP-200060 | 1978 | 2 | F | Emergency service at EPC-5GC interworking | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 1980 | 5 | F | Not supporting 15 EPS bearers at 5GS to EPS mobility | 16.4.0 |
| 2020-03 | SP-87E | SP-200072 | 1981 | 2 | F | Correction to Handover Procedures | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 1982 | 1 | F | AMF awareness of emergency Registration/PDU Session at inter-CN node change | 16.4.0 |
| 2020-03 | SP-87E | SP-200063 | 1983 | 3 | F | Availability after DDN Failure in 5GC | 16.4.0 |
| 2020-03 | SP-87E | SP-200063 | 1984 | 1 | F | Availability after DDN Failure event with UPF buffering | 16.4.0 |
| 2020-03 | SP-87E | SP-200063 | 1985 | 2 | F | NEF service update for NIDD | 16.4.0 |
| 2020-03 | SP-87E | SP-200065 | 1986 | 4 | F | Correction of PCF discovery via BSF to consider eSBA producer binding indication principles - BSF Services (23.502) | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 1987 | 1 | F | Adding the N4 association setup procedure initiated by UPF | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 1988 | 3 | F | Use of EPS/RAT fallback for VoWiFi session | 16.4.0 |
| 2020-03 | SP-87E | SP-200072 | 1989 | - | F | Correction of 5GS to EPS Idle mode mobility using N26 interface with I-SMF removal | 16.4.0 |
| 2020-03 | SP-87E | SP-200067 | 1992 | 1 | F | Update dynamic CN PDB to NG-RAN during Xn handover | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 1994 | 1 | F | Update to Network triggered SR procedure | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 1995 | 1 | F | Corrections on registration with AMF relocation | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 1996 | 1 | F | Correction of the CN tunnel info at the target side | 16.4.0 |
| 2020-03 | SP-87E | SP-200065 | 1997 | 2 | F | Update the binding indication for subscription | 16.4.0 |
| 2020-03 | SP-87E | SP-200072 | 1998 | 1 | F | Different N3/N9 tunnel information | 16.4.0 |
| 2020-03 | SP-87E | SP-200063 | 2001 | 1 | F | Small Data Rate Control enforcement corrections | 16.4.0 |
| 2020-03 | SP-87E | SP-200063 | 2003 | 1 | F | Addition of eDRX parameter to subscription data types | 16.4.0 |
| 2020-03 | SP-87E | SP-200063 | 2004 | 1 | F | Correction of Nsmf_SendMOData parameter list | 16.4.0 |
| 2020-03 | SP-87E | SP-200067 | 2007 | 2 | F | Alternative QoS Profile corrections | 16.4.0 |
| 2020-03 | SP-87E | SP-200070 | 2008 | 2 | F | Clarification of the BDT policy re-negotiation procedure | 16.4.0 |
| 2020-03 | SP-87E | SP-200063 | 2013 | - | F | Extended Buffering Control in the SMF | 16.4.0 |
| 2020-03 | SP-87E | SP-200069 | 2015 | 3 | F | Corrections for ATSSS support when roaming | 16.4.0 |
| 2020-03 | SP-87E | SP-200069 | 2016 | 1 | F | Corrections to SMF service operations for ATSSS | 16.4.0 |
| 2020-03 | SP-87E | SP-200069 | 2017 | - | F | Corrections to PCF service operations for ATSSS | 16.4.0 |
| 2020-03 | SP-87E | SP-200069 | 2018 | 1 | F | Corrections for SMF-PCF interactions for ATSSS | 16.4.0 |
| 2020-03 | SP-87E | SP-200072 | 2019 | 1 | F | Non N26 based Interworking Procedures with I-SMF | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 2021 | 2 | F | Add AMF Charging Characteristics | 16.4.0 |
| 2020-03 | SP-87E | SP-200060 | 2023 | 2 | A | Corrections on SMF Charging Characteristics | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 2024 | - | F | Correction about the DN Information | 16.4.0 |
| 2020-03 | SP-87E | SP-200063 | 2025 | 1 | B | WUS assistance information procedures | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 2026 | 2 | F | Clarification on the EPS fallback reporting | 16.4.0 |
| 2020-03 | SP-87E | SP-200077 | 2030 | 2 | F | Item#4 Update the Annex F.2 5GS Bridge configuration. | 16.4.0 |
| 2020-03 | SP-87E | SP-200074 | 2034 | - | F | RAC ID during inter-PLMN handover case | 16.4.0 |
| 2020-03 | SP-87E | SP-200063 | 2035 | - | F | Update to Nnef_SMContext_Create service operation | 16.4.0 |
| 2020-03 | SP-87E | SP-200072 | 2039 | - | F | End marker indication in SR procedure | 16.4.0 |
| 2020-03 | SP-87E | SP-200077 | 2041 | 4 | F | #1_Procedures for support of 5G VN group communication | 16.4.0 |
| 2020-03 | SP-87E | SP-200267 | 2043 | 4 | F | Procedure udpate for PDU Session establishment and Bridge based information reporting | 16.4.0 |
| 2020-03 | SP-87E | SP-200069 | 2045 | 2 | F | Service operation to notify unavailability of non-3GPP access | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 2047 | 1 | F | Clarification on the result of Namf_Communication_N1N2MessageTransfer service | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 2048 | 3 | F | EBI revocation of QoS flow of default QoS rule | 16.4.0 |
| 2020-03 | SP-87E | SP-200063 | 2049 | 1 | F | NAS signalling of CP Relocation Indication Truncated 5G-S-TMSI Parameters Procedures | 16.4.0 |
| 2020-03 | SP-87E | SP-200063 | 2050 | 2 | F | Correction for non MO-Exception Data cause signalling | 16.4.0 |
| 2020-03 | SP-87E | SP-200063 | 2052 | 1 | F | Add Serving PLMN rate control in the PDU Session Establishment | 16.4.0 |
| 2020-03 | SP-87E | SP-200063 | 2054 | - | F | Clarification on Enhanced Coverage Restriction | 16.4.0 |
| 2020-03 | SP-87E | SP-200064 | 2055 | 1 | F | UE LCS Privacy Profile Update | 16.4.0 |
| 2020-03 | SP-87E | SP-200064 | 2056 | 1 | F | NEF service to support location transfer | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 2059 | 6 | F | Correction to UE configuration update procedure conditions for re-registration | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 2063 | 1 | F | Correction on the usage of SUPI and PDU Session ID | 16.4.0 |
| 2020-03 | SP-87E | SP-200067 | 2064 | 1 | F | Correction on PDU Session Modification procedure regarding redundant transmission | 16.4.0 |
| 2020-03 | SP-87E | SP-200074 | 2066 | 2 | F | UCMF provisioning correction | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 2068 | 1 | D | Correction on PDU Session Modification procedure | 16.4.0 |
| 2020-03 | SP-87E | SP-200065 | 2069 | 2 | F | Update of the binding procedures with Routing Binding Indication | 16.4.0 |
| 2020-03 | SP-87E | SP-200063 | 2072 | 1 | F | Update to AMF exposure of mobility events for extended buffering in NEF | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 2082 | - | F | Clarification on the CN tunnel info allocation and release | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 2083 | 1 | F | QoS Flows reestablished during EPS Fallback | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 2084 | - | F | Reachability Event Correction | 16.4.0 |
| 2020-03 | SP-87E | SP-200070 | 2088 |  | F | Adding two new event IDs for AMF event exposure. | 16.4.0 |
| 2020-03 | SP-87E | SP-200070 | 2089 | - | F | Updates to AMF event exposure and event filters | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 2090 | - | F | Incorrect service operation Namf_Communication_RegistrationCompleteNotify | 16.4.0 |
| 2020-03 | SP-87E | SP-200077 | 2091 | 1 | F | Updating the UE with new CAG information | 16.4.0 |
| 2020-03 | SP-87E | SP-200077 | 2092 | 1 | F | Correct the transfer of the bridge delay related parameters | 16.4.0 |
| 2020-03 | SP-87E | SP-200077 | 2093 | 1 | F | Correct the-the NW-TT port related | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 2095 | 1 | F | Corrections on EPS fallback and RAT fallback for IMS voice | 16.4.0 |
| 2020-03 | SP-87E | SP-200069 | 2096 | 1 | F | Indication of network ATSSS capability in Registration procedures | 16.4.0 |
| 2020-03 | SP-87E | SP-200069 | 2098 | 1 | F | MA PDU Session Modification when UE is registered to different PLMNs over 3GPP access and non-3GPP access | 16.4.0 |
| 2020-03 | SP-87E | SP-200070 | 2099 | - | F | SMF services for data collection | 16.4.0 |
| 2020-03 | SP-87E | SP-200069 | 2100 | - | D | Rapporteur Submission - Editorial update for ATSSS | 16.4.0 |
| 2020-03 | SP-87E | SP-200069 | 2104 | 1 | F | Correction on Network Modification to MA PDU Session | 16.4.0 |
| 2020-03 | SP-87E | SP-200074 | 2107 | 1 | D | Editorial updates in RACS clauses | 16.4.0 |
| 2020-03 | SP-87E | SP-200077 | 2108 | 1 | F | Clarification on CAG ID provided by NG-RAN to AMF. | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 2109 | - | F | Clarification on the EPS fallback reporting during Transfer of PDU session used for IMS voice from non-3GPP access to 5GS. | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 2113 | 1 | F | Corrections for CN tunnel info allocation and release | 16.4.0 |
| 2020-03 | SP-87E | SP-200072 | 2115 | 1 | F | Corrections for Registration and Service Request | 16.4.0 |
| 2020-03 | SP-87E | SP-200065 | 2117 | 1 | F | Updated resource information alignment with CT4 | 16.4.0 |
| 2020-03 | SP-87E | SP-200072 | 2118 | 1 | F | ETSUN related CR for non-FASMO corrections | 16.4.0 |
| 2020-03 | SP-87E | SP-200067 | 2121 | - | F | Clarification on the target AF for late notification | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 2122 | 1 | F | AFsessionWithQoS update | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 2123 | - | F | Updates to the AFsessionWithQoS setup | 16.4.0 |
| 2020-03 | SP-87E | SP-200081 | 2127 | 1 | F | Support of inter-RAT HO from NR SA to EN-DC | 16.4.0 |
| 2020-03 | SP-87E | SP-200063 | 2129 | 1 | F | corrections for handling of I-NEF routing configuration during inter PLMN mobility | 16.4.0 |
| 2020-03 | SP-87E | SP-200063 | 2130 | 1 | F | N4 session level reporting for discard and buffered DL traffic detection | 16.4.0 |
| 2020-03 | SP-87E | SP-200068 | 2134 | - | F | Adding procedures for devices that do not support 5G NAS over WLAN access | 16.4.0 |
| 2020-03 | SP-87E | SP-200077 | 2137 | 1 | F | clarification on Port Management Information Container toward SMF | 16.4.0 |
| 2020-03 | SP-87E | SP-200065 | 2138 | 1 | F | Routing binding indication correction | 16.4.0 |
| 2020-03 | SP-87E | SP-200072 | 2139 | 1 | F | Local PSA release correction | 16.4.0 |
| 2020-03 | SP-87E | SP-200077 | 2142 | 1 | F | Correcting procedure of NEF service operations information flow and adding parameters of 5G VN group data | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 2145 | - | F | Update of steering of roaming information for different registration types | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 2146 | 1 | F | NSSAI in the HO request during inter RAT/EPS interworking | 16.4.0 |
| 2020-03 | SP-87E | SP-200077 | 2150 | 1 | F | Update for Bridge Delay information reporting and QoS mapping | 16.4.0 |
| 2020-03 | SP-87E | SP-200065 | 2151 | 1 | F | Updating NRF services based on NF profile | 16.4.0 |
| 2020-03 | SP-87E | SP-200065 | 2152 | 1 | F | Update of NF Status Subscribe/Unsubscribe services with PLMN ID | 16.4.0 |
| 2020-03 | SP-87E | SP-200065 | 2153 | - | F | Update of context transfer procedures | 16.4.0 |
| 2020-03 | SP-87E | SP-200069 | 2155 | 1 | F | Supporting EPS interworking with ATSSS | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 2157 | 1 | F | Procedures update due to removal of TEID allocation by SMF | 16.4.0 |
| 2020-03 | SP-87E | SP-200071 | 2160 | 1 | F | NSSAA procedure clarification | 16.4.0 |
| 2020-03 | SP-87E | SP-200081 | 2162 | 1 | F | Addition of PSCell information in PDU Session modification | 16.4.0 |
| 2020-03 | SP-87E | SP-200079 | 2163 | 1 | F | Inclusion of Requested NSSAI in AN Parameters | 16.4.0 |
| 2020-03 | SP-87E | SP-200069 | 2166 | - | F | User-plane resources establishment over the second access for Home-routed Roaming MA PDU session establishment | 16.4.0 |
| 2020-07 | SP-88E | SP-200433 | 2081 | 2 | F | Support of ETSUN and ATSSS | 16.5.0 |
| 2020-07 | SP-88E | SP-200428 | 2097 | 2 | F | MA PDU Session Release when UE is registered to different PLMNs over 3GPP access and non-3GPP access | 16.5.0 |
| 2020-07 | SP-88E | SP-200552 | 2110 | 1 | F | Corrections on known consumers of AMF related services | 16.5.0 |
| 2020-07 | SP-88E | SP-200433 | 2112 | 1 | F | Handover of a PDU Session procedure between untrusted non-3GPP and 3GPP access | 16.5.0 |
| 2020-07 | SP-88E | SP-200433 | 2174 | 1 | F | Support of ETSUN within and between PLMN(s) | 16.5.0 |
| 2020-07 | SP-88E | SP-200551 | 2175 | 1 | F | V-SMF may apply VPLMN policies related with the SLA with the HPLMN | 16.5.0 |
| 2020-07 | SP-88E | SP-200551 | 2176 | - | F | Remove un-necessary End Marker Indication in invocations of Nsmf_PDUSession_Update Request | 16.5.0 |
| 2020-07 | SP-88E | SP-200422 | 2177 | 1 | F | Corrections for Availability after DDN Failure event with UPF buffering | 16.5.0 |
| 2020-07 | SP-88E | SP-200437 | 2178 | - | F | Common Network Exposure | 16.5.0 |
| 2020-07 | SP-88E | SP-200424 | 2182 | - | F | Update of PCF address(es) for a PDU session in the BSF | 16.5.0 |
| 2020-07 | SP-88E | SP-200427 | 2183 | 1 | F | Handover of a PDU Session procedure between 3GPP and trusted non-3GPP access | 16.5.0 |
| 2020-07 | SP-88E | SP-200422 | 2184 | 1 | F | Specify the new service Nsmf_PDUSession_MessageTransfer | 16.5.0 |
| 2020-07 | SP-88E | SP-200552 | 2186 | - | F | Corrections for AF Session with QoS procedure | 16.5.0 |
| 2020-07 | SP-88E | SP-200428 | 2188 | - | F | Handling of mobility in case ATSSS is not supported in target AMF | 16.5.0 |
| 2020-07 | SP-88E | SP-200436 | 2190 | 1 | F | UE radio capability for 5GS and IWK | 16.5.0 |
| 2020-07 | SP-88E | SP-200439 | 2194 | 1 | F | QoS container vs. TSCAI input container | 16.5.0 |
| 2020-07 | SP-88E | SP-200439 | 2195 | 1 | F | Removing NID from Xn based inter NG-RAN HO procedure | 16.5.0 |
| 2020-07 | SP-88E | SP-200439 | 2196 | 1 | F | Correct the transfer of the NW-TT port's Port Management Container | 16.5.0 |
| 2020-07 | SP-88E | SP-200431 | 2197 | 1 | F | Support of data collection for any UE | 16.5.0 |
| 2020-07 | SP-88E | SP-200428 | 2199 | - | F | Clarification on MA PDU Session re-activation | 16.5.0 |
| 2020-07 | SP-88E | SP-200551 | 2203 | 1 | F | Clarification on PDU session establishment without S-NSSAI indication | 16.5.0 |
| 2020-07 | SP-88E | SP-200422 | 2204 | - | F | Correction to handling of Service Gap timer for regulatory prioritzed services | 16.5.0 |
| 2020-07 | SP-88E | SP-200428 | 2205 | 1 | F | MPTCP functionality information | 16.5.0 |
| 2020-07 | SP-88E | SP-200425 | 2206 | - | F | Packet delay of RAN for QoS Monitoring | 16.5.0 |
| 2020-07 | SP-88E | SP-200424 | 2208 | 2 | F | Enablers for multiple SCPs (23.502) | 16.5.0 |
| 2020-07 | SP-88E | SP-200432 | 2210 | 1 | F | Removal of service area for UE registration with empty Allowed NSSAI due to pending NSSAA | 16.5.0 |
| 2020-07 | SP-88E | SP-200439 | 2211 | 1 | F | Adding CAG information in Registration Accept message | 16.5.0 |
| 2020-07 | SP-88E | SP-200551 | 2212 | 1 | F | Nudm_UECM_Get input parameter correction | 16.5.0 |
| 2020-07 | SP-88E | SP-200551 | 2213 | - | F | UE reachability for SMS | 16.5.0 |
| 2020-07 | SP-88E | SP-200432 | 2214 | 1 | F | Correction of NSSAA procedure and Registration procedure | 16.5.0 |
| 2020-07 | SP-88E | SP-200422 | 2216 | - | F | Small data rate control enforcement of normal and exception data | 16.5.0 |
| 2020-07 | SP-88E | SP-200424 | 2217 | 1 | F | Corrections to Binding for Indirect Communication without delegated discovery | 16.5.0 |
| 2020-07 | SP-88E | SP-200551 | 2218 | 1 | F | Emergency call enhancements for 4G only UE | 16.5.0 |
| 2020-07 | SP-88E | SP-200609 | 2219 | 3 | F | Update PDU Session release when Control Plane Only indication is not applicable | 16.5.0 |
| 2020-07 | SP-88E | SP-200422 | 2220 | 1 | F | Change of the restriction of enhanced coverage in UE Configuration Update procedure | 16.5.0 |
| 2020-07 | SP-88E | SP-200439 | 2224 | 1 | F | Bridge Delay Clarification | 16.5.0 |
| 2020-07 | SP-88E | SP-200428 | 2225 | 1 | F | Corrections on ATSSS capabilities | 16.5.0 |
| 2020-07 | SP-88E | SP-200428 | 2227 | 1 | F | Clarifications on Network initiated service request procedure | 16.5.0 |
| 2020-07 | SP-88E | SP-200431 | 2228 | 1 | F | Event filters for data collection | 16.5.0 |
| 2020-07 | SP-88E | SP-200440 | 2230 | 1 | F | URSP info provision for xBDT | 16.5.0 |
| 2020-07 | SP-88E | SP-200436 | 2231 | - | F | Support of multiple coding formats | 16.5.0 |
| 2020-07 | SP-88E | SP-200431 | 2232 | 1 | F | Correction on AMF TAC event for newly detected UEs | 16.5.0 |
| 2020-07 | SP-88E | SP-200428 | 2234 | 1 | F | MA PDU session establishment in home-routed roaming | 16.5.0 |
| 2020-07 | SP-88E | SP-200431 | 2236 | 1 | F | Remove the Nnef_NetworkStatus service | 16.5.0 |
| 2020-07 | SP-88E | SP-200431 | 2239 | 1 | F | Updates to AMF event exposure and event filters | 16.5.0 |
| 2020-07 | SP-88E | SP-200552 | 2242 | 1 | F | Clarification on Npcf_BDTPolicyControl | 16.5.0 |
| 2020-07 | SP-88E | SP-200433 | 2243 | - | F | Xn based handover for home routed roaming scenario | 16.5.0 |
| 2020-07 | SP-88E | SP-200422 | 2244 | 1 | F | Correction of NEF-based NIDD procedures | 16.5.0 |
| 2020-07 | SP-88E | SP-200552 | 2247 | 1 | F | EBI of default EPS bearer | 16.5.0 |
| 2020-07 | SP-88E | SP-200552 | 2248 | 2 | F | CN tunnel info allocation for non roaming and LBO case | 16.5.0 |
| 2020-07 | SP-88E | SP-200433 | 2250 | - | F | PDU Session release and Deregistration procedure correction | 16.5.0 |
| 2020-07 | SP-88E | SP-200433 | 2251 | 1 | F | Pause of Charging | 16.5.0 |
| 2020-07 | SP-88E | SP-200433 | 2252 | - | F | Correction to Policy Update Procedures with I-SMF | 16.5.0 |
| 2020-07 | SP-88E | SP-200551 | 2256 | 1 | F | Fix the incorrect figure and description in 5GS - EPS HO. | 16.5.0 |
| 2020-07 | SP-88E | SP-200433 | 2257 | 1 | F | Clarification on CN tunnel for EPS during the I-SMF insertion | 16.5.0 |
| 2020-07 | SP-88E | SP-200439 | 2258 | 1 | F | Alignment on the Trigger for SMF and clarification on the NW-TT port(s) for PDU session | 16.5.0 |
| 2020-07 | SP-88E | SP-200439 | 2259 | 1 | F | Removing the duplication and incorrect part in the Annex F | 16.5.0 |
| 2020-07 | SP-88E | SP-200439 | 2261 | 1 | F | Corrections for 5GS Bridge information reporting and configuration | 16.5.0 |
| 2020-07 | SP-88E | SP-200436 | 2263 | - | F | Use correct term for IMEI/TAC in UCMF Services | 16.5.0 |
| 2020-07 | SP-88E | SP-200423 | 2267 | 1 | F | Update Nudm_UECM_Get and Nudm_EventExposure_Subscribe service operation | 16.5.0 |
| 2020-07 | SP-88E | SP-200432 | 2271 | 1 | F | Defer Network Slice-Specific Re-authentication and Re-authorization procedure for UE in CM-IDLE | 16.5.0 |
| 2020-07 | SP-88E | SP-200551 | 2272 | 1 | F | Correction on List Of PDU Sessions To Be Activated | 16.5.0 |
| 2020-07 | SP-88E | SP-200432 | 2276 | - | F | Correction on the value of S-NSSAIs for NSSAA | 16.5.0 |
| 2020-07 | SP-88E | SP-200420 | 2279 | 1 | A | Correction on Deregistration procedures for SMS over NAS | 16.5.0 |
| 2020-07 | SP-88E | SP-200551 | 2280 | 1 | F | Reordering DL data during SR procedure | 16.5.0 |
| 2020-07 | SP-88E | SP-200552 | 2282 | 1 | F | Correction on deregistration procedure | 16.5.0 |
| 2020-07 | SP-88E | SP-200437 | 2283 | 1 | F | User State Information in 5GS | 16.5.0 |
| 2020-07 | SP-88E | SP-200425 | 2287 | 1 | F | Clarification on the late notifcation for the target AF | 16.5.0 |
| 2020-07 | SP-88E | SP-200432 | 2289 | 1 | F | Usage of NSSAA status at N2 based handover | 16.5.0 |
| 2020-07 | SP-88E | SP-200420 | 2291 | 1 | F | 5G-GUTI in the Access Network parameters | 16.5.0 |
| 2020-07 | SP-88E | SP-200424 | 2292 | 1 | F | Update of Nnrf_NFManagement_NFRegister service operation | 16.5.0 |
| 2020-07 | SP-88E | SP-200427 | 2293 | - | F | Sending the IP address of TNGF to UE | 16.5.0 |
| 2020-07 | SP-88E | SP-200432 | 2296 | 1 | F | PDU session release in NSSAA procedure | 16.5.0 |
| 2020-07 | SP-88E | SP-200439 | 2298 | - | F | Notify the information of the detected bridge and detected port to the TSN AF | 16.5.0 |
| 2020-07 | SP-88E | SP-200422 | 2300 | 1 | F | UE specific DRX for NB-IoT in 5GC | 16.5.0 |
| 2020-07 | SP-88E | SP-200422 | 2301 | - | F | PDU session modificaiton when Restriction of use of Enhanced Coverage changes | 16.5.0 |
| 2020-07 | SP-88E | SP-200431 | 2303 | - | F | AF event filter for service experience area of interest | 16.5.0 |
| 2020-07 | SP-88E | SP-200431 | 2304 | - | F | NEF event exposure correction | 16.5.0 |
| 2020-07 | SP-88E | SP-200439 | 2305 | 1 | F | Updating call flow with Ethernet Filters | 16.5.0 |
| 2020-07 | SP-88E | SP-200551 | 2306 | 1 | F | Clarification of TEID allocation by UPF | 16.5.0 |
| 2020-07 | SP-88E | SP-200439 | 2307 | 1 | F | SMF to request the UE IP address from the DN-AAA server based on subscription information | 16.5.0 |
| 2020-07 | SP-88E | SP-200431 | 2237 | 2 | F | Correction of BDT policy re-negotiation procedure | 16.5.0 |
| 2020-07 | SP-88E | SP-200439 | 2297 | 3 | F | Missing important assumptions on how Npcf_PolicyAuthorization_Notify is used in TSN context | 16.5.0 |
| 2020-07 | SP-88E | SP-200420 | 2311 | 1 | A | Presence of PEI in Nudm_UECM_Registration Request | 16.5.0 |
| 2020-07 | SP-88E | SP-200422 | 2312 | 1 | F | Network Parameters Configuration by Parameter Provisioning and Event Exposure Subscription | 16.5.0 |
| 2020-07 | SP-88E | SP-200434 | 2313 | - | F | Alignment with RAN stage 3 on Alternative QoS Profile | 16.5.0 |
| 2020-07 | SP-88E | SP-200432 | 2316 | - | F | Replacing AUSF by NSSAAF to support NSSAA | 16.5.0 |
| 2020-07 | SP-88E | SP-200516 | 2317 | 1 | F | Clarification on Registration with AMF re-allocation | 16.5.0 |
| 2020-07 | SP-88E | SP-200551 | 2318 | 1 | B | Alignment CR for DAPS HO | 16.5.0 |
| 2020-07 | SP-88E | SP-200427 | 2319 | 1 | F | Correction on Framed Route information reporting | 16.5.0 |
| 2020-07 | SP-88E | SP-200422 | 2320 | - | F | Removal of I-NEF | 16.5.0 |
| 2020-07 | SP-88E | SP-200551 | 2321 | 1 | F | Missing parameters in Namf_Communication_NonUeN2MessageTransfer | 16.5.0 |
| 2020-07 | SP-88E | SP-200433 | 2322 | 1 | F | Interworking between ETSUN and URLLC/TSN | 16.5.0 |
| 2020-08 | SP-88E | - | - | - | - | Removal of postponed CR2317R1: Clarification on Registration with AMF re-allocation | 16.5.1 |
| 2020-09 | SP-89E | SP-200685 | 2326 | 1 | F | Registration procedure across ePLMNs | 16.6.0 |
| 2020-09 | SP-89E | SP-200680 | 2328 | - | F | Missing N2 SM information from initial AMF to target AMF | 16.6.0 |
| 2020-09 | SP-89E | SP-200686 | 2330 | 1 | F | Remove un-necessary End Marker Indication in invocations of Nsmf_PDUSession_Update Request (missing part) | 16.6.0 |
| 2020-09 | SP-89E | SP-200680 | 2331 | - | F | removal of editor's note | 16.6.0 |
| 2020-09 | SP-89E | SP-200680 | 2333 | 1 | F | GPSI for NSSAA | 16.6.0 |
| 2020-09 | SP-89E | SP-200682 | 2334 | - | F | V2X Subscription Data | 16.6.0 |
| 2020-09 | SP-89E | SP-200671 | 2336 | 1 | A | SMF aware of UE Reachability after N1N2MessageTransfer error due to UE unreachable | 16.6.0 |
| 2020-09 | SP-89E | SP-200688 | 2338 | 1 | F | Addressing wording comments from IEEE LS response on TSN support | 16.6.0 |
| 2020-09 | SP-89E | SP-200673 | 2340 | - | F | Clarification on use of N2 message in PDU Session establishment for Control Plane CIoT 5GS Optimization | 16.6.0 |
| 2020-09 | SP-89E | SP-200686 | 2341 | - | F | UE user plane integrity protection mandatory at full rate | 16.6.0 |
| 2020-09 | SP-89E | SP-200679 | 2342 | 1 | F | Re-ordering of interactions in the BDT policy re-negotiation procedure | 16.6.0 |
| 2020-09 | SP-89E | SP-200689 | 2344 | 1 | F | Correction to the procedure for future background data transfer procedure | 16.6.0 |
| 2020-09 | SP-89E | SP-200686 | 2345 | - | F | WUS system support for 5GC | 16.6.0 |
| 2020-09 | SP-89E | SP-200679 | 2346 | 1 | F | Time in trajectories of Expected UE Behaviour | 16.6.0 |
| 2020-09 | SP-89E | SP-200674 | 2349 | 1 | F | Routing Binding indication without delegated discovery | 16.6.0 |
| 2020-09 | SP-89E | SP-200682 | 2356 | - | F | Clarification on UE policy related description | 16.6.0 |
| 2020-09 | SP-89E | SP-200688 | 2357 | 1 | F | Removal of HO triggered by MRL | 16.6.0 |
| 2020-09 | SP-89E | SP-200681 | 2361 | 1 | F | Clarification on End marker | 16.6.0 |
| 2020-09 | SP-89E | SP-200681 | 2362 | - | F | Corrections on link local address and CN tunnel info provision | 16.6.0 |
| 2020-09 | SP-89E | SP-200676 | 2364 | - | F | Correcting UE Id in the Access Network parameters | 16.6.0 |
| 2020-09 | SP-89E | SP-200686 | 2367 | - | F | Corrections on DAPS HO Procedure | 16.6.0 |
| 2020-09 | SP-89E | SP-200671 | 2368 | 1 | A | Correction on Deregistration procedures for SMS over NAS | 16.6.0 |
| 2020-09 | SP-89E | SP-200673 | 2370 | - | F | Procedure Clarifications for multiple UP resource support for an NB-IoT UE | 16.6.0 |
| 2020-09 | SP-89E | SP-200673 | 2371 | 1 | F | Procedure Clarifications for CIoT optimisations during mobility to and from non-3GPP access | 16.6.0 |
| 2020-09 | SP-89E | SP-200673 | 2372 | 1 | F | Correction to interaction between the SMF and UPF for Availability after DDN failure event | 16.6.0 |
| 2020-09 | SP-89E | SP-200673 | 2373 | 1 | F | Procedures to Redirect UE via service reject to align with CT1 | 16.6.0 |
| 2020-09 | SP-89E | SP-200676 | 2374 | - | F | Adding emergency registration procedure for trusted non-3GPP access | 16.6.0 |
| 2020-09 | SP-89E | SP-200676 | 2375 | 1 | F | Adding handover procedure between EPS and 5GC-TNGF | 16.6.0 |
| 2020-09 | SP-89E | SP-200676 | 2376 | 1 | F | Clarification on Identifiers of N5CW devices | 16.6.0 |
| 2020-09 | SP-89E | SP-200671 | 2380 | 1 | A | Stage 3 alignment on UE reachability event | 16.6.0 |
| 2020-09 | SP-89E | SP-200688 | 2382 | - | F | Alignment with RAN specification on adding PLMN+CAG information in paging message | 16.6.0 |
| 2020-09 | SP-89E | SP-200688 | 2386 | 1 | F | GUTI clarification for UE registration in an SNPN | 16.6.0 |
| 2020-09 | SP-89E | SP-200688 | 2388 | 1 | F | Clarify Ethernet Frames handling for Ethernet PDU session | 16.6.0 |
| 2020-09 | SP-89E | SP-200674 | 2389 | 1 | F | Clarifications on SCP registration and discovery procedures | 16.6.0 |
| 2020-09 | SP-89E | SP-200688 | 2390 | - | F | 23.502 - Resolution of open items related to IEEE LS | 16.6.0 |
| 2020-09 | SP-89E | SP-200686 | 2392 | 1 | F | Correction of NSSAI in the Registration procedure and Service Request procedure | 16.6.0 |
| 2020-09 | SP-89E | SP-200679 | 2393 | - | F | Location event filter for trusted AF | 16.6.0 |
| 2020-09 | SP-89E | SP-200674 | 2394 | 1 | F | Correction on Nnrf_NFManagement_NFStatusSubscribe service operation | 16.6.0 |
| 2020-09 | SP-89E | SP-200674 | 2395 | 1 | F | Correction on Nnrf_NFManagement_NFStatusNotify service operation | 16.6.0 |
| 2020-09 | SP-89E | SP-200688 | 2396 | 1 | F | Moving NW-TT ports from BMI into BMIC | 16.6.0 |
| 2020-09 | SP-89E | SP-200673 | 2398 | 1 | F | PCC control for DDD status and availability after DDN failure events | 16.6.0 |
| 2020-12 | SP-90E | SP-200946 | 2332 | - | F | Handling of AAA-S address in NSSAA | 16.7.0 |
| 2020-12 | SP-90E | SP-200951 | 2358 | 2 | F | QoS related parameters to be updated during Handover | 16.7.0 |
| 2020-12 | SP-90E | SP-200958 | 2383 | 2 | F | NSAAA re-authentication by AAA-S | 16.7.0 |
| 2020-12 | SP-90E | SP-200959 | 2400 | 2 | F | Corrections to MME Emergency Configuration Data for enable the selection of diffrent emergency gateways based on UE capabilities | 16.7.0 |
| 2020-12 | SP-90E | SP-200945 | 2405 | 1 | A | Clarification on Emergency Services Fallback | 16.7.0 |
| 2020-12 | SP-90E | SP-200959 | 2406 | 1 | F | Correction on EPS fallback with emergency service | 16.7.0 |
| 2020-12 | SP-90E | SP-200959 | 2407 | 1 | F | Correction on EPS fallback for voice service | 16.7.0 |
| 2020-12 | SP-90E | SP-200953 | 2411 | 1 | F | Replacing Bridge Address with Bridge ID | 16.7.0 |
| 2020-12 | SP-90E | SP-200958 | 2412 | - | F | Correction to Nnssaaf_NSSAA_Notify service | 16.7.0 |
| 2020-12 | SP-90E | SP-200959 | 2414 | 1 | F | QoS control in V-SMF | 16.7.0 |
| 2020-12 | SP-90E | SP-200959 | 2415 | - | F | UE Context in AMF Data | 16.7.0 |
| 2020-12 | SP-90E | SP-200947 | 2419 | 1 | F | Correction on Enhanced Coverage Restriction | 16.7.0 |
| 2020-12 | SP-90E | SP-200947 | 2421 | - | F | Event Configuration Synchronization between 4G&amp;5G | 16.7.0 |
| 2020-12 | SP-90E | SP-200959 | 2424 | 1 | F | Clarification on Registration with AMF re-allocation | 16.7.0 |
| 2020-12 | SP-90E | SP-200957 | 2425 | - | F | Clarifications for the BDT policy negotiation procedure | 16.7.0 |
| 2020-12 | SP-90E | SP-200959 | 2426 | - | F | Correction of Registration procedure for untrusted non-3GPP access | 16.7.0 |
| 2020-12 | SP-90E | SP-200959 | 2428 | 1 | F | Handling of UE parameters update and Steering of Roaming procedure when UE is not reachable or when acknowledgement from UE is not received | 16.7.0 |
| 2020-12 | SP-90E | SP-200959 | 2430 | 1 | F | S-NSSAI handling at the Inter PLMN mobility | 16.7.0 |
| 2020-12 | SP-90E | SP-200959 | 2431 | 1 | F | Correction on Location Report | 16.7.0 |
| 2020-12 | SP-90E | SP-200947 | 2433 | 1 | F | Correction on header compression for CP Optimisation | 16.7.0 |
| 2020-12 | SP-90E | SP-200953 | 2434 | 1 | F | Clarification on UPF report Bridge ID | 16.7.0 |
| 2020-12 | SP-90E | SP-200959 | 2435 | 1 | F | Corrections for PDU Session Release Procedure in 5GC | 16.7.0 |
| 2020-12 | SP-90E | SP-200959 | 2438 | 1 | F | Voice fallback triggered by PDU session resource setup | 16.7.0 |
| 2020-12 | SP-90E | SP-201100 | 2439 | 2 | A | Removal of SMSF registration notification flag | 16.7.0 |
| 2020-12 | SP-90E | SP-200945 | 2442 | 1 | A | Stage 3 alignment on correction of UE Context Transfer payload in case of UE initial registration | 16.7.0 |
| 2020-12 | SP-90E | SP-200945 | 2444 | 1 | A | Correction of Network Triggered Service Request for UE in CM-CONNECTED | 16.7.0 |
| 2020-12 | SP-90E | SP-200945 | 2446 | 1 | A | Stage 3 alignment on clarification of Registration Status Update for PCF for UE Policy | 16.7.0 |
| 2020-12 | SP-90E | SP-200947 | 2448 | 1 | F | Clarifications for GUTI re-allocation | 16.7.0 |
| 2020-12 | SP-90E | SP-200959 | 2449 | 1 | F | Correction to AN Release procedure | 16.7.0 |
| 2020-12 | SP-90E | SP-201127 | 2450 | 2 | F | Fixing Redirection for EPS Fallback indication | 16.7.0 |
| 2020-12 | SP-90E | SP-200953 | 2451 | 1 | F | Use of NSSF Services for SNPN | 16.7.0 |
| 2020-12 | SP-90E | SP-200954 | 2452 | - | F | Correction on Trusted Non-3GPP access | 16.7.0 |
| 2020-12 | SP-90E | SP-201141 | 2453 | 2 | F | QoS parameter handling for PDU session transfer between 3GPP and non-3GPP access | 16.7.0 |
| 2020-12 | SP-90E | SP-200959 | 2454 | 1 | F | General cleanup of specification | 16.7.0 |
| 2021-01 | SP-90E | - | - | - | - | MCC correction: Removal of postponed 23.502 CR2413R1 from implementation | 16.7.1 |
| 2021-03 | SP-91E | - | - | - | - | MCC clean-up of numerous typos before CR Implementation | 16.8.0 |
| 2021-03 | SP-91E | SP-210055 | 2418 | 2 | F | UE availability after DDN failure and DDD status events handling with V-SMF and I-SMF | 16.8.0 |
| 2021-03 | SP-91E | SP-210055 | 2422 | 2 | F | Correction to Network Configuration Parameter handling | 16.8.0 |
| 2021-03 | SP-91E | SP-210075 | 2456 | 1 | F | Corrections on EPS to 5GS Handover with AMF re-allocation | 16.8.0 |
| 2021-03 | SP-91E | SP-210082 | 2457 | - | F | EBI allocation for Emergency PDU Sessions | 16.8.0 |
| 2021-03 | SP-91E | SP-210082 | 2458 | 1 | F | Correcting AMF specifications related with the FQDN for the S5/S8 interface of the SMF+PGW-C | 16.8.0 |
| 2021-03 | SP-91E | SP-210082 | 2459 | 1 | F | Add steps for releasing resources for indirect forwarding in Handover Cancel | 16.8.0 |
| 2021-03 | SP-91E | SP-210082 | 2460 | - | F | Corrections on Inter NG-RAN node N2 Handover Procedure description | 16.8.0 |
| 2021-03 | SP-91E | SP-210082 | 2473 | 1 | F | Uplink packet filter handling to avoid packet drops | 16.8.0 |
| 2021-03 | SP-91E | SP-210082 | 2475 | 2 | F | Handling of DN-AAA interactions in case of EPS IWK | 16.8.0 |
| 2021-03 | SP-91E | SP-210053 | 2480 | 1 | A | Supplement DNN to the input parameter of Nnrf_NFManagement_NFRegister service operation | 16.8.0 |
| 2021-03 | SP-91E | SP-210055 | 2483 | 1 | F | Roaming status monitoring event clarification | 16.8.0 |
| 2021-03 | SP-91E | SP-210082 | 2485 | 1 | F | Correction of Inter-AMF mobility with group monitoring | 16.8.0 |
| 2021-03 | SP-91E | SP-210082 | 2487 | 1 | F | QoS control in the VPLMN | 16.8.0 |
| 2021-03 | SP-91E | SP-210075 | 2488 | 1 | F | PDU Session ID and Configured S-NSSAI handling during EPS to 5GS HO with AMF reallocation | 16.8.0 |
| 2021-03 | SP-91E | SP-210055 | 2489 | 1 | F | MTC Provider Information handling | 16.8.0 |
| 2021-03 | SP-91E | SP-210082 | 2492 | 1 | F | Configuration of SMF+PGW-C identity in Emergency Configuration Data | 16.8.0 |
| 2021-03 | SP-91E | SP-210082 | 2493 | 1 | F | Correction to handling of alternative H-SMF in home routed roaming | 16.8.0 |
| 2021-03 | SP-91E | SP-210243 | 2495 | - | F | PFD provisioning correction to exclude pre-configuration | 16.8.0 |
| 2021-03 | SP-91E | SP-210245 | 2515 | 1 | F | Clarification on MA PDU session for LADN | 16.8.0 |
| 2021-03 | SP-91E | SP-210244 | 2516 | - | F | Correction on switching an existing PDU Session between non-3GPP access and 3GPP access | 16.8.0 |
| 2021-03 | SP-91E | SP-210243 | 2524 | - | F | Delete the duplicated SoR item in UE Subscription data | 16.8.0 |
| 2021-03 | SP-91E | SP-210082 | 2535 | 1 | F | Home Routed PDU Session Establishment | 16.8.0 |
| 2021-03 | SP-91E | SP-210082 | 2537 | - | F | NGAP TNLA Binding correction | 16.8.0 |
| 2021-03 | SP-91E | SP-210082 | 2544 | 1 | F | Alignment with stage 3 for location reporting | 16.8.0 |
| 2021-03 | SP-91E | SP-210082 | 2545 | 1 | F | NGAP UE-TNLA-binding update | 16.8.0 |
| 2021-03 | SP-91E | SP-210057 | 2546 | - | F | Remove EN for authorization in Indirect Communication and Delegated Discovery | 16.8.0 |
| 2021-03 | SP-91E | SP-210076 | 2548 | 1 | F | QoS parameter handling for PDU session transfer between 3GPP and non-3GPP access | 16.8.0 |
| 2021-03 | SP-91E | SP-210055 | 2556 | - | F | Clarification on session transfer between non-3GPP access and 3GPP access during the CPSR | 16.8.0 |
| 2021-03 | SP-91E | SP-210079 | 2561 | 1 | F | Immediate Suspension | 16.8.0 |
| 2021-03 | SP-91E | SP-210055 | 2574 | 1 | F | Downlink data report by UPF | 16.8.0 |
| 2021-03 | SP-91E | SP-210056 | 2576 | 1 | F | Update of AMF event exposure service | 16.8.0 |
| 2021-03 | SP-91E | SP-210243 | 2598 | 1 | F | Incorrect linkage of unreachable to lack of paging response | 16.8.0 |
| 2021-03 | SP-91E | SP-210088 | 2455 | - | B | Support of different slices over different Non 3GPP access | 17.0.0 |
| 2021-03 | SP-91E | SP-210085 | 2472 | 1 | B | Multimedia Priority Service (MPS) Phase 2 support for Data Transport Service | 17.0.0 |
| 2021-03 | SP-91E | SP-210068 | 2589 | 1 | B | MA PDU sessions with connectivity over E-UTRAN/EPC and non-3GPP access to 5GC | 17.0.0 |
| 2021-03 | SP-91E | SP-210083 | 2590 | 1 | B | TS23.502 KI#1 Network Slice Admission Control Function (NSACF) services and procedures | 17.0.0 |
| 2021-03 | SP-91E | SP-210065 | 2482 | 1 | B | Network selection for NR satellite access | 17.0.0 |
| 2021-03 | SP-91E | SP-210065 | 2575 | - | B | Intra NG-RAN handover via CN for NR satellite access | 17.0.0 |
| 2021-03 | SP-91E | SP-210088 | 2478 | 1 | B | Update NF services provided by PCF to support DCAMP in the 5GC | 17.0.0 |
| 2021-03 | SP-91E | SP-210088 | 2496 | 1 | B | 5G system procedures updates to support Dynamically Changing Policies in the 5GC | 17.0.0 |
| 2021-03 | SP-91E | SP-210088 | 2497 | - | B | DCAMP related update of BSF services (23.502) | 17.0.0 |
| 2021-03 | SP-91E | SP-210088 | 2569 | 1 | B | Procedure to allow dynamic changes of AM Policies based on the application in use | 17.0.0 |
| 2021-03 | SP-91E | SP-210069 | 2461 | 1 | B | Support of AF guidance to PCF determination of proper URSP rules | 17.0.0 |
| 2021-03 | SP-91E | SP-210069 | 2462 | 1 | B | EC KI2 Target PSA buffering | 17.0.0 |
| 2021-03 | SP-91E | SP-210069 | 2486 | 1 | B | ECS Address Provisioning | 17.0.0 |
| 2021-03 | SP-91E | SP-210069 | 2549 | 1 | B | (I-)SMF discovery based on DNAI | 17.0.0 |
| 2021-03 | SP-91E | SP-210069 | 2552 | 1 | B | KI #5, I-SMF selection | 17.0.0 |
| 2021-03 | SP-91E | SP-210069 | 2560 | - | B | Edge relocation considering user plane latency requirements | 17.0.0 |
| 2021-03 | SP-91E | SP-210069 | 2573 | 1 | B | Procedure of ECS Address Provisioning by AF | 17.0.0 |
| 2021-03 | SP-91E | SP-210084 | 2474 | - | B | KI#5-1: Impact due to Survival Time | 17.0.0 |
| 2021-03 | SP-91E | SP-210084 | 2525 | 1 | B | KI#2 Procedure impacts for UE-UE TSC | 17.0.0 |
| 2021-03 | SP-91E | SP-210084 | 2533 | 1 | B | KI#1 - Adding BMCA procedure | 17.0.0 |
| 2021-03 | SP-91E | SP-210084 | 2534 | 1 | B | IP PDU session type impacts for TSC | 17.0.0 |
| 2021-03 | SP-91E | SP-210084 | 2539 | 1 | B | Exposure of Time synchronization as a service - procedure | 17.0.0 |
| 2021-03 | SP-91E | SP-210084 | 2540 | 1 | B | AF Support for TSC QoS | 17.0.0 |
| 2021-03 | SP-91E | SP-210088 | 2476 | - | C | IP index from UDM | 17.0.0 |
| 2021-03 | SP-91E | SP-210087 | 2506 | - | D | Inclusive language review | 17.0.0 |
| 2021-03 | SP-91E | SP-210088 | 2563 | 1 | B | 23502 Selecting the same PCF for AMF and SMF | 17.0.0 |
| 2021-03 | SP-91E | SP-210088 | 2577 | 1 | B | Registration procedure for trusted non-3GPP access with TNGF relocation | 17.0.0 |
| 2021-03 | SP-91E | SP-210064 | 2519 | 1 | B | AF Services operation for 5G ProSe | 17.0.0 |
| 2021-03 | SP-91E | SP-210064 | 2554 | - | B | Addition of 5G ProSe subscription data | 17.0.0 |
| 2021-03 | SP-91E | SP-210064 | 2564 | - | B | NRF Services Update for ProSe 5G DDNMF Operations | 17.0.0 |
| 2021-03 | SP-91E | SP-210064 | 2565 | - | B | UDM Services Consumer Update for ProSe Direct Discovery Authorization | 17.0.0 |
| 2021-03 | SP-91E | SP-210073 | 2463 | 1 | B | Event Exposure in support of Dispersion Analytics | 17.0.0 |
| 2021-03 | SP-91E | SP-210073 | 2464 | 1 | B | Update AM, SM and UE Policy control procedures to add NWDAF interaction | 17.0.0 |
| 2021-03 | SP-91E | SP-210073 | 2467 | 1 | B | Enhancements for supporting Supported Analytics Delay mechanism | 17.0.0 |
| 2021-03 | SP-91E | SP-210073 | 2471 | 1 | B | Survivability of Event Exposure Subscription via UDM | 17.0.0 |
| 2021-03 | SP-91E | SP-210073 | 2481 | - | B | Adding 'Information on PDU session for WLAN' event to the Nsmf_EventExposure Service to support WLAN performance analytics | 17.0.0 |
| 2021-03 | SP-91E | SP-210073 | 2499 | 1 | B | New SMF event to support N4 data collection | 17.0.0 |
| 2021-03 | SP-91E | SP-210073 | 2503 | 1 | B | NWDAF discovery and selection | 17.0.0 |
| 2021-03 | SP-91E | SP-210073 | 2504 | 1 | B | Re-selection of NWDAF at change of AMF | 17.0.0 |
| 2021-03 | SP-91E | SP-210073 | 2505 | 1 | B | Structure of specification of DCCF, MFAF, ADRF | 17.0.0 |
| 2021-03 | SP-91E | SP-210073 | 2507 | - | B | New SMF event for Session Management Congestion Control Experience | 17.0.0 |
| 2021-03 | SP-91E | SP-210073 | 2508 | 1 | B | Adding the usage of Redundant Transmission Experience analytics for URLLC service | 17.0.0 |
| 2021-03 | SP-91E | SP-210073 | 2509 | 1 | B | Adding the usage of extended UE Mobility analytics for LADN service | 17.0.0 |
| 2021-03 | SP-91E | SP-210073 | 2510 | 1 | B | Extensions of NRF, SMF to support conclusions on Discovering and Tracking Entities Serving area of interest in TS 23.502 | 17.0.0 |
| 2021-03 | SP-91E | SP-210073 | 2511 | 1 | B | Extensions of Event Reporting Information in TS23.502 | 17.0.0 |
| 2021-03 | SP-91E | SP-210073 | 2512 | 1 | B | NWDAF discovery and selection based on provided ML models | 17.0.0 |
| 2021-03 | SP-91E | SP-210073 | 2513 | 1 | B | UP path selection enhancement based on analytics info provided by NWDAF | 17.0.0 |
| 2021-03 | SP-91E | SP-210073 | 2514 | 1 | B | KI#11: Extension of Event exposure parameters | 17.0.0 |
| 2021-03 | SP-91E | SP-210073 | 2530 | 1 | B | NWDAF registration and discovery for model sharing | 17.0.0 |
| 2021-03 | SP-91E | SP-210073 | 2541 | 1 | B | Clarification of additional input data collected by NWDAF from AF | 17.0.0 |
| 2021-03 | SP-91E | SP-210073 | 2557 | 1 | B | Introducing partitioning criteria in event reporting information | 17.0.0 |
| 2021-03 | SP-91E | SP-210073 | 2586 | 1 | B | KI#4: NSSF services update | 17.0.0 |
| 2021-03 | SP-91E | SP-210073 | 2597 | 1 | B | Gathering trends in AMF and SMF event exposure | 17.0.0 |
| 2021-06 | SP-92E | SP-210341 | 2490 | 2 | C | Application Identifier for NEF API ChargebleParty and AF Session with QoS | 17.1.0 |
| 2021-06 | SP-92E | SP-210341 | 2491 | 2 | C | DNN and S-NSSAI for NEF API ChargebleParty and AF Session with QoS | 17.1.0 |
| 2021-06 | SP-92E | SP-210362 | 2502 | 5 | B | Introduction of Paging Cause feature | 17.1.0 |
| 2021-06 | SP-92E | SP-210362 | 2558 | 5 | B | Introduction of Reject Paging Indication response to paging using SR | 17.1.0 |
| 2021-06 | SP-92E | SP-210362 | 2568 | 5 | B | Introduction of MUSIM capability exchage | 17.1.0 |
| 2021-06 | SP-92E | SP-210356 | 2591 | 2 | B | TS23.502 KI#2 Network Slice Admission Control Function (NSACF) services and procedures | 17.1.0 |
| 2021-06 | SP-92E | SP-210346 | 2602 | 1 | B | Support for L2TP on N6 | 17.1.0 |
| 2021-06 | SP-92E | SP-210343 | 2603 | 4 | B | Solving interworking to 5GS with N26 issue due to UE's N1 mode capability disabling/enabling | 17.1.0 |
| 2021-06 | SP-92E | SP-210352 | 2604 | 1 | B | NWDAF registering into UDM | 17.1.0 |
| 2021-06 | SP-92E | SP-210352 | 2606 | 2 | B | Updates to Selection of NWDAF at change of AMF | 17.1.0 |
| 2021-06 | SP-92E | SP-210352 | 2607 | 1 | B | Providing information on NWDAF for UE related Analytics to PCF | 17.1.0 |
| 2021-06 | SP-92E | SP-210347 | 2609 | 2 | B | Support for Service Specific Authorization | 17.1.0 |
| 2021-06 | SP-92E | SP-210340 | 2610 | 1 | B | Update of 5G ProSe subscription data | 17.1.0 |
| 2021-06 | SP-92E | SP-210356 | 2611 | 1 | B | KI#1 : (NSACF) services and procedures Architectural Update | 17.1.0 |
| 2021-06 | SP-92E | SP-210356 | 2614 | 3 | B | Support for UE-Slice-MBR | 17.1.0 |
| 2021-06 | SP-92E | SP-210356 | 2615 | 1 | B | Default Subscribed S-NSSAIs for Network Slice Admission Control | 17.1.0 |
| 2021-06 | SP-92E | SP-210324 | 2618 | - | A | Delete NSI ID via N7 interface | 17.1.0 |
| 2021-06 | SP-92E | SP-210352 | 2620 | 1 | B | Adding the usage of UE Communication analytics extended for PDU Session Inactivity Timer optimization | 17.1.0 |
| 2021-06 | SP-92E | SP-210352 | 2621 | 1 | D | Editorial Note Removal | 17.1.0 |
| 2021-06 | SP-92E | SP-210342 | 2623 | 1 | B | PDU session establishment for NR satellite access | 17.1.0 |
| 2021-06 | SP-92E | SP-210354 | 2625 | 1 | B | Service discovery between SNPN and Credential Holder | 17.1.0 |
| 2021-06 | SP-92E | SP-210538 | 2626 | 3 | B | Support of 5GC assisted cell selection to access network slice | 17.1.0 |
| 2021-06 | SP-92E | SP-210338 | 2630 | - | C | Add GMLC as a potential consumer of AMF event exposure service | 17.1.0 |
| 2021-06 | SP-92E | SP-210354 | 2632 | 3 | B | Registration Procedure for UE Onboarding | 17.1.0 |
| 2021-06 | SP-92E | SP-210356 | 2633 | 2 | B | NSACF discovery and selection | 17.1.0 |
| 2021-06 | SP-92E | SP-210347 | 2635 | 2 | F | ECS Address Provisioning in Interworking Scenarios | 17.1.0 |
| 2021-06 | SP-92E | SP-210549 | 2636 | 2 | F | Nsmf_EventExposure supports RAT Type Change Event | 17.1.0 |
| 2021-06 | SP-92E | SP-210345 | 2637 | 1 | B | Non-IP type PDN Connection support as 3GPP access leg of MA PDU Session | 17.1.0 |
| 2021-06 | SP-92E | SP-210354 | 2641 | 1 | B | SNPN - SNPN Mobility and Registration procedure | 17.1.0 |
| 2021-06 | SP-92E | SP-210352 | 2645 | 1 | F | Clarification on Real-Time Communication Indication | 17.1.0 |
| 2021-06 | SP-92E | SP-210347 | 2648 | 3 | B | AF Influence enhancement for EAS IP replacement | 17.1.0 |
| 2021-06 | SP-92E | SP-210344 | 2649 | 1 | B | Enhanced NRF services for MBS | 17.1.0 |
| 2021-06 | SP-92E | SP-210347 | 2650 | 2 | B | EC KI2 Target PSA buffering for SSC mode 3 | 17.1.0 |
| 2021-06 | SP-92E | SP-210352 | 2651 | 1 | B | Updating AMF exposed events in TS 23.502. | 17.1.0 |
| 2021-06 | SP-92E | SP-210347 | 2655 | - | B | Adding EASDF services | 17.1.0 |
| 2021-06 | SP-92E | SP-210359 | 2656 | - | B | Update for Survival Time | 17.1.0 |
| 2021-06 | SP-92E | SP-210359 | 2657 | - | B | Update for BMCA procedure | 17.1.0 |
| 2021-06 | SP-92E | SP-210363 | 2658 | 4 | B | UE providing PDU Session Pair ID based on URSP rules | 17.1.0 |
| 2021-06 | SP-92E | SP-210359 | 2665 | 1 | C | Updating IP PDU session type impacts for TSC | 17.1.0 |
| 2021-06 | SP-92E | SP-210329 | 2667 | 2 | A | Support of AF change | 17.1.0 |
| 2021-06 | SP-92E | SP-210356 | 2669 | 5 | B | Service Operations of NSAC for Roaming UEs | 17.1.0 |
| 2021-06 | SP-92E | SP-210347 | 2670 | 1 | F | DNS configuration to SMF | 17.1.0 |
| 2021-06 | SP-92E | SP-210363 | 2672 | 1 | B | Support GERAN/UTRAN access in SMF+PGW-C | 17.1.0 |
| 2021-06 | SP-92E | SP-210356 | 2674 | 1 | C | Add AMF behaviour when EAC is deactive | 17.1.0 |
| 2021-06 | SP-92E | SP-210356 | 2676 | 3 | B | PDU Session establishment and modification admission control based on network Slice maximum data rate | 17.1.0 |
| 2021-06 | SP-92E | SP-210338 | 2677 | 1 | B | Introduce local location in AMF service operation | 17.1.0 |
| 2021-06 | SP-92E | SP-210340 | 2678 | - | B | NRF service update | 17.1.0 |
| 2021-06 | SP-92E | SP-210356 | 2683 | 3 | B | eNS_502_KI#3_Update of Registration Procedures | 17.1.0 |
| 2021-06 | SP-92E | SP-210347 | 2687 | 2 | B | The introduction of UPF Service | 17.1.0 |
| 2021-06 | SP-92E | SP-210352 | 2688 | 1 | C | Update to Nnssf_NSRestriction service | 17.1.0 |
| 2021-06 | SP-92E | SP-210352 | 2689 | - | F | Corrections to partitioning criteria | 17.1.0 |
| 2021-06 | SP-92E | SP-210352 | 2690 | 1 | B | eNA KI#8 mapping between UE IP address and UE ID -23.502 | 17.1.0 |
| 2021-06 | SP-92E | SP-210337 | 2691 | 1 | F | AF session setup and update with required QoS procedure for trusted domain | 17.1.0 |
| 2021-06 | SP-92E | SP-210352 | 2692 |  | B | Addressing EN on Binding | 17.1.0 |
| 2021-06 | SP-92E | SP-210352 | 2698 | - | B | Update to NRF NF Discovery request | 17.1.0 |
| 2021-06 | SP-92E | SP-210352 | 2699 | 1 | B | Update to AF Event Exposure service | 17.1.0 |
| 2021-06 | SP-92E | SP-210359 | 2704 | 1 | B | Termnology on the TSC MIC and Bridge ID | 17.1.0 |
| 2021-06 | SP-92E | SP-210344 | 2705 | 1 | B | MBS subscription in UDM | 17.1.0 |
| 2021-06 | SP-92E | SP-210356 | 2706 | 2 | B | Introduction of support of NG.116 attribute Simultaneous Use of a Network Slice | 17.1.0 |
| 2021-06 | SP-92E | SP-210352 | 2708 | - | C | AMF service for transfer of NWDAF association information | 17.1.0 |
| 2021-06 | SP-92E | SP-210356 | 2715 | 1 | B | TS 23.502 KI#4 NSACF event notification services and procedures | 17.1.0 |
| 2021-06 | SP-92E | SP-210347 | 2716 | 2 | C | ECS Address Configuration in UDM | 17.1.0 |
| 2021-06 | SP-92E | SP-210345 | 2718 | 1 | F | Mobility from EPC to 5GC for MA PDU Session | 17.1.0 |
| 2021-06 | SP-92E | SP-210345 | 2719 | 1 | F | UE initiated PDN connection modification after 5GS to EPS handover with MA PDU session | 17.1.0 |
| 2021-06 | SP-92E | SP-210334 | 2722 | 2 | A | New service operation of Namf_Communication_CancelRelocateUEContext | 17.1.0 |
| 2021-06 | SP-92E | SP-210362 | 2724 | 4 | B | Introduction of Leaving procedure - 5GS | 17.1.0 |
| 2021-06 | SP-92E | SP-210360 | 2726 | 1 | B | NSAC in case of mobility with AMF change | 17.1.0 |
| 2021-06 | SP-92E | SP-210352 | 2731 | - | B | Analytics subscription transfer triggered by AMF reallocation | 17.1.0 |
| 2021-06 | SP-92E | SP-210356 | 2732 | - | F | Correction of the Number of UEs per network slice availability check and update procedure | 17.1.0 |
| 2021-06 | SP-92E | SP-210340 | 2734 | 1 | B | Reporting Change of PDUID by the PCF | 17.1.0 |
| 2021-06 | SP-92E | SP-210544 | 2738 | 2 | F | NSSAA procedures for the UE when it is served by two different AMFs | 17.1.0 |
| 2021-06 | SP-92E | SP-210347 | 2740 | - | B | Spatial Validity Conditions in AF Guidance to URSP Rules | 17.1.0 |
| 2021-06 | SP-92E | SP-210347 | 2741 | - | B | Notification on the outcome of UE Policies delivery due to service specific parameter provisioning | 17.1.0 |
| 2021-06 | SP-92E | SP-210363 | 2743 | 1 | B | Dynamic management of group based event monitoring | 17.1.0 |
| 2021-06 | SP-92E | SP-210326 | 2745 | 1 | A | Group event clarification and event transfer between AMFs | 17.1.0 |
| 2021-06 | SP-92E | SP-210347 | 2749 | - | C | Using the UE Location to Decide what ECS Addresses are Sent | 17.1.0 |
| 2021-06 | SP-92E | SP-210344 | 2756 | 1 | B | NRF extensions for 5MBS | 17.1.0 |
| 2021-06 | SP-92E | SP-210359 | 2761 | 1 | F | PMIC and BMIC in PCF | 17.1.0 |
| 2021-06 | SP-92E | SP-210591 | 2762 | 4 | B | AF Session Setup and Update with Required QoS Procedure for Trusted Domain | 17.1.0 |
| 2021-06 | SP-92E | SP-210331 | 2764 | 1 | A | Removal of Notification Control from the Additional QoS Information | 17.1.0 |
| 2021-06 | SP-92E | SP-210345 | 2765 | 1 | B | Partial ATSSS rule update capability | 17.1.0 |
| 2021-06 | SP-92E | SP-210329 | 2767 | - | A | N9 forwarding tunnel between source and target ULCL | 17.1.0 |
| 2021-06 | SP-92E | SP-210330 | 2769 | 1 | A | CHF discovery via NRF | 17.1.0 |
| 2021-06 | SP-92E | SP-210341 | 2776 | 1 | F | Clean-up for AF related identifier | 17.1.0 |
| 2021-06 | SP-92E | SP-210354 | 2783 | 1 | B | UE context retrieval during registration procedure considering SNPN involved. | 17.1.0 |
| 2021-06 | SP-92E | SP-210339 | 2785 | 1 | F | SM policy control update due to SMF relocation | 17.1.0 |
| 2021-06 | SP-92E | SP-210359 | 2788 | 1 | F | Clarification on support of PTP GM function in TT | 17.1.0 |
| 2021-06 | SP-92E | SP-210333 | 2793 | 1 | A | Clarify the BDT warning procedure with degraded Network performance | 17.1.0 |
| 2021-06 | SP-92E | SP-210336 | 2795 | 1 | B | Updates to AF requests to influence traffic routing | 17.1.0 |
| 2021-06 | SP-92E | SP-210347 | 2796 | 1 | B | I-SMF selection for subsequent PDU session | 17.1.0 |
| 2021-06 | SP-92E | SP-210354 | 2804 | 1 | B | NF Management for SNPN | 17.1.0 |
| 2021-06 | SP-92E | SP-210546 | 2807 | 2 | F | Allowed NSSAI when NSSAA fails | 17.1.0 |
| 2021-06 | SP-92E | SP-210334 | 2811 | 1 | A | Simultaneous change of ULCL/BP and PSA | 17.1.0 |
| 2021-06 | SP-92E | SP-210347 | 2814 | 1 | B | UE capability to support EAS rediscovry | 17.1.0 |
| 2021-06 | SP-92E | SP-210338 | 2818 |  | B | UE positioning capability storage in AMF | 17.1.0 |
| 2021-06 | SP-92E | SP-210354 | 2820 | 1 | C | Add a new NSSAAF service to support interaction between AUSF and AAA Server | 17.1.0 |
| 2021-06 | SP-92E | SP-210334 | 2826 |  | A | Add NG-RAN N3 Tunnel information in SM context | 17.1.0 |
| 2021-06 | SP-92E | SP-210347 | 2827 | 1 | F | Add N3 tunnel information in SM context for I-SMF reselection per DNAI | 17.1.0 |
| 2021-06 | SP-92E | SP-210342 | 2829 | 1 | B | SMF reports satellite backhaul information to PCF during the PDU session establishment procedure | 17.1.0 |
| 2021-06 | SP-92E | SP-210347 | 2830 | 1 | B | Clarification on target DNAI Information stored in AMF | 17.1.0 |
| 2021-06 | SP-92E | SP-210347 | 2831 | 1 | F | Updates on uplink traffic buffering | 17.1.0 |
| 2021-06 | SP-92E | SP-210352 | 2834 | 1 | C | NWDAF assisted DNAI selection at SMF | 17.1.0 |
| 2021-06 | SP-92E | SP-210356 | 2835 | 1 | B | NSAC with consideration of access type | 17.1.0 |
| 2021-06 | SP-92E | SP-210359 | 2839 | 1 | C | Alt-QoS for TSC | 17.1.0 |
| 2021-06 | SP-92E | SP-210347 | 2841 | 1 | B | Clarifications on User Plane Latency Requirement | 17.1.0 |
| 2021-06 | SP-92E | SP-210327 | 2843 | 1 | A | NIDD configuration correction | 17.1.0 |
| 2021-06 | SP-92E | SP-210342 | 2844 | 1 | C | Satellite backhaul with long delay notification to the SMF | 17.1.0 |
| 2021-06 | SP-92E | SP-210354 | 2849 | 1 | B | Registration procedure for UE onboarding SNPN | 17.1.0 |
| 2021-06 | SP-92E | SP-210356 | 2850 | - | B | TS23.502 KI#4 NSACF status notification on request | 17.1.0 |
| 2021-06 | SP-92E | SP-210352 | 2851 | 1 | B | Update to NRF service - NWDAF registration and discovery | 17.1.0 |
| 2021-06 | SP-92E | SP-210359 | 2854 | 1 | C | Time synchronization service exposure | 17.1.0 |
| 2021-06 | SP-92E | SP-210356 | 2856 | 1 | B | NSACF update in case of inter-AMF mobility with no UE context transfer | 17.1.0 |
| 2021-06 | SP-92E | SP-210328 | 2870 | 1 | A | Handling of UTRAN UE radio capabilities | 17.1.0 |
| 2021-06 | SP-92E | SP-210352 | 2873 | - | F | Corrections to UE behaviour trends | 17.1.0 |
| 2021-06 | SP-92E | SP-210352 | 2874 | 1 | B | UE IP address usage in Naf_EventExposure service | 17.1.0 |
| 2021-06 | SP-92E | SP-210331 | 2879 | - | A | Handover of a PDU Session procedure between 3GPP and trusted non-3GPP access in deployments topologies with specific SMF Service Areas | 17.1.0 |
| 2021-06 | SP-92E | SP-210352 | 2880 | - | C | SMF event exposure updates | 17.1.0 |
| 2021-06 | SP-92E | SP-210589 | 2881 | 1 | A | Registration with AMF relocation considering CAG | 17.1.0 |
| 2021-09 | SP-93E | SP-210902 | 2752 | 2 | A | Correction to EPS bearer ID transfer | 17.2.0 |
| 2021-09 | SP-93E | SP-210924 | 2801 | 2 | C | Additional parameters using UE Parameters Update via UDM Control Plane Procedure | 17.2.0 |
| 2021-09 | SP-93E | SP-210909 | 2813 | 3 | A | L-PSA release during mobiity procedure with I-SMF removal | 17.2.0 |
| 2021-09 | SP-93E | SP-210915 | 2858 | 2 | B | 4G &lt;-&gt; 5GS mobility corrections to cope with areas of GERAN/UTRAN-only coverage | 17.2.0 |
| 2021-09 | SP-93E | SP-210916 | 2875 | 1 | C | Support of Mobility Registration Update for 5G Satellite Access | 17.2.0 |
| 2021-09 | SP-93E | SP-210917 | 2878 | 2 | B | service extensions for 5MBS | 17.2.0 |
| 2021-09 | SP-93E | SP-210915 | 2882 | 1 | F | Clarification on selection of the hNRF | 17.2.0 |
| 2021-09 | SP-93E | SP-210925 | 2883 | - | F | clarification on NSSRG info sent to NSSF | 17.2.0 |
| 2021-09 | SP-93E | SP-210925 | 2884 | 1 | F | Clarification on the interaction of the AMF with NSSF when NSSRG information is provided by UDM | 17.2.0 |
| 2021-09 | SP-93E | SP-210915 | 2886 | - | F | Nnssf_NSSAIAvailability service clarification | 17.2.0 |
| 2021-09 | SP-93E | SP-210925 | 2887 | 1 | D | editorial CR on NSSRG related aspects | 17.2.0 |
| 2021-09 | SP-93E | SP-210925 | 2888 | 1 | F | missing indication of UE support of NSSRG functionality in NSSF services | 17.2.0 |
| 2021-09 | SP-93E | SP-210924 | 2889 | 1 | F | Update of Credentials Holder controlled prioritized lists of preferred SNPNs and GINs using SoR | 17.2.0 |
| 2021-09 | SP-93E | SP-210910 | 2891 | 1 | A | Handling of UE Radio Capability for Paging | 17.2.0 |
| 2021-09 | SP-93E | SP-210937 | 2900 | - | F | BSF related update of NRF services (23.502) | 17.2.0 |
| 2021-09 | SP-93E | SP-210922 | 2901 | 1 | F | Event ID Number of UEs served by the AMF and located in Area Of Interest | 17.2.0 |
| 2021-09 | SP-93E | SP-210937 | 2902 | - | F | Nnef_AMPolicyAuthorization clarifications | 17.2.0 |
| 2021-09 | SP-93E | SP-210937 | 2903 | 1 | F | AM influence request for multiple applications | 17.2.0 |
| 2021-09 | SP-93E | SP-210937 | 2904 | 1 | F | Corrections to BSF subscription | 17.2.0 |
| 2021-09 | SP-93E | SP-210937 | 2905 | 1 | F | Notification of SM Policy Association Establishment | 17.2.0 |
| 2021-09 | SP-93E | SP-210925 | 2909 | 1 | B | KI#2_Support-For-Accurate-Count-for-MaxPDUSessions | 17.2.0 |
| 2021-09 | SP-93E | SP-210922 | 2910 | - | F | Support for internal group ID in Naf services | 17.2.0 |
| 2021-09 | SP-93E | SP-210922 | 2911 | 1 | F | Data Collection parameters | 17.2.0 |
| 2021-09 | SP-93E | SP-210928 | 2915 | 1 | F | UE subscription data types to support UAS | 17.2.0 |
| 2021-09 | SP-93E | SP-210928 | 2916 | - | F | Update to UE context in AMF to support UAS | 17.2.0 |
| 2021-09 | SP-93E | SP-210928 | 2917 | - | F | Update to Event Filters for AMF exposure events to support UAS | 17.2.0 |
| 2021-09 | SP-93E | SP-210928 | 2918 | 1 | F | NEF discovery and selection based on AF address | 17.2.0 |
| 2021-09 | SP-93E | SP-211131 | 2920 | 3 | F | Exception #1: Enabling of paging reception for 5GS | 17.2.0 |
| 2021-09 | SP-93E | SP-210932 | 2921 | 1 | F | Exception #2: On alignment with RAN2 regarding Rejection of RAN paging | 17.2.0 |
| 2021-09 | SP-93E | SP-210930 | 2924 | - | F | Trusted AF notify or response directly from PCF or TSCTSF | 17.2.0 |
| 2021-09 | SP-93E | SP-210930 | 2925 | 1 | F | UE-DS-TT Residence Time and calculation of Required PDB | 17.2.0 |
| 2021-09 | SP-93E | SP-210920 | 2927 | 1 | B | New NEF service to support EAS deployment info | 17.2.0 |
| 2021-09 | SP-93E | SP-210920 | 2928 | - | F | AF Request for Simultaneous Connectivity over Source and Target PSA at Edge Relocation | 17.2.0 |
| 2021-09 | SP-93E | SP-210920 | 2929 | - | F | Service Specific Authorization for Group of UEs | 17.2.0 |
| 2021-09 | SP-93E | SP-210919 | 2931 | 1 | F | Corrections to L2TP call flow | 17.2.0 |
| 2021-09 | SP-93E | SP-210930 | 2935 | 1 | F | Updates for TSC and time synchronization text - procedure | 17.2.0 |
| 2021-09 | SP-93E | SP-210930 | 2936 | 1 | C | Control of the 5G reference time distribution | 17.2.0 |
| 2021-09 | SP-93E | SP-210903 | 2941 | - | A | Correction of the Notification of User Plane Management Events procedure | 17.2.0 |
| 2021-09 | SP-93E | SP-210925 | 2943 | - | F | Aligning TR conclusion of adding back-off timer to KI#2 | 17.2.0 |
| 2021-09 | SP-93E | SP-210915 | 2947 | - | F | Correction to UE or network requested PDU Session Release for Home-routed Roaming | 17.2.0 |
| 2021-09 | SP-93E | SP-210915 | 2948 | 1 | C | N1 mode capability disabled/enabled and interworking between EPC/ePDG and 5GS | 17.2.0 |
| 2021-09 | SP-93E | SP-210928 | 2952 | - | B | Update NEF Monitoring Events to Support Area of Interest event | 17.2.0 |
| 2021-09 | SP-93E | SP-210932 | 2953 | - | F | MUSIM Terminology Alignment | 17.2.0 |
| 2021-09 | SP-93E | SP-210922 | 2954 | - | F | Remove the target of analytics reporting during the NWDAF(MTLF) registration | 17.2.0 |
| 2021-09 | SP-93E | SP-210922 | 2955 | 1 | F | Remove the roaming information for the slice association information | 17.2.0 |
| 2021-09 | SP-93E | SP-210936 | 2957 | 1 | B | Update on Supporting UP Integrity Protection Policy Handling for Interworking from 5GS to EPS | 17.2.0 |
| 2021-09 | SP-93E | SP-210936 | 2958 | 1 | F | Corrections on the AF related identifier | 17.2.0 |
| 2021-09 | SP-93E | SP-210936 | 2959 | 1 | F | Clarification on Session Management Policy Data per PLMN | 17.2.0 |
| 2021-09 | SP-93E | SP-210937 | 2960 | 1 | F | Corrections on geographical area | 17.2.0 |
| 2021-09 | SP-93E | SP-210937 | 2961 | - | F | Clarifications on AM influence requests for multiple applications | 17.2.0 |
| 2021-09 | SP-93E | SP-210930 | 2962 | - | F | Update related services for interaction between TSCTSF and PCF | 17.2.0 |
| 2021-09 | SP-93E | SP-210925 | 2963 | 1 | F | Clarification to the operation of network slice status reporting | 17.2.0 |
| 2021-09 | SP-93E | SP-210925 | 2964 | 1 | F | Redirection to dedicated frequency band(s) at the end of NSSAA | 17.2.0 |
| 2021-09 | SP-93E | SP-210930 | 2965 | 1 | C | Corrections to the Time Synchronization service procedures | 17.2.0 |
| 2021-09 | SP-93E | SP-210920 | 2968 | 1 | F | ECS Address Configuration in UDM | 17.2.0 |
| 2021-09 | SP-93E | SP-210926 | 2970 | 1 | F | KI#1KI#2 - NSACF Service operation name update | 17.2.0 |
| 2021-09 | SP-93E | SP-210909 | 2972 | 1 | A | Source I-SMF release for PDU Session not requested for handover | 17.2.0 |
| 2021-09 | SP-93E | SP-210926 | 2973 | - | F | Clarification on NSACF registration to support roaming | 17.2.0 |
| 2021-09 | SP-93E | SP-210926 | 2976 | 1 | B | Status Exposure for multiple NSACF instances | 17.2.0 |
| 2021-09 | SP-93E | SP-210926 | 2977 | 1 | F | TS23.502 Correction to the NSAC related to the EAC mode | 17.2.0 |
| 2021-09 | SP-93E | SP-210922 | 2978 | - | F | Event Filters for Collective Behaviour of multiple UEs | 17.2.0 |
| 2021-09 | SP-93E | SP-210922 | 2979 | - | F | Update to AF Profile Registration and Discovery | 17.2.0 |
| 2021-09 | SP-93E | SP-211012 | 2981 | 3 | F | ATSSS_update target access type during secondary reauth | 17.2.0 |
| 2021-09 | SP-93E | SP-210924 | 2982 | 1 | C | DCS providing PVS address to ONN | 17.2.0 |
| 2021-09 | SP-93E | SP-210936 | 2987 | - | C | Event subscription parameters With DNN and S-NSSAI | 17.2.0 |
| 2021-09 | SP-93E | SP-210932 | 2988 | 1 | F | Connection Release procedure correction | 17.2.0 |
| 2021-09 | SP-93E | SP-210931 | 2990 | 1 | B | Introduction of MINT support | 17.2.0 |
| 2021-09 | SP-93E | SP-210903 | 2993 | 1 | A | Initial event reporting during subscription | 17.2.0 |
| 2021-09 | SP-93E | SP-210924 | 2994 | 1 | B | IMSI based SUPI support when access an SNPN using credentials owned by CH | 17.2.0 |
| 2021-09 | SP-93E | SP-210924 | 2995 | 1 | C | Registration procedure for Onboarding SNPN | 17.2.0 |
| 2021-09 | SP-93E | SP-210922 | 2998 | 1 | B | User consent for network analytics | 17.2.0 |
| 2021-09 | SP-93E | SP-210926 | 2999 | - | F | Undo wrongly implemented changes | 17.2.0 |
| 2021-09 | SP-93E | SP-210926 | 3000 | 1 | F | NSACF receiving update requests from multiple consumer NFs | 17.2.0 |
| 2021-09 | SP-93E | SP-210937 | 3012 | 1 | F | Correction on dynamic updates of AM Policy | 17.2.0 |
| 2021-09 | SP-93E | SP-210932 | 3017 | - | F | Correction of Reject Paging Indication in Service Request | 17.2.0 |
| 2021-09 | SP-93E | SP-210937 | 3018 | 1 | F | Update PCF services table and NEF services table | 17.2.0 |
| 2021-09 | SP-93E | SP-210915 | 3019 | - | F | Removal of ATSSS Rule ID indication | 17.2.0 |
| 2021-09 | SP-93E | SP-210920 | 3024 | 1 | F | Registration of local NEF to NRF | 17.2.0 |
| 2021-09 | SP-93E | SP-210920 | 3025 | 1 | F | Update the procedure and details in ECS Configuration Information provision | 17.2.0 |
| 2021-09 | SP-93E | SP-210926 | 3026 | 1 | B | NSAC support for EPC interworking | 17.2.0 |
| 2021-09 | SP-93E | SP-210924 | 3033 | 1 | F | AMF relocation for UE registered for onboarding | 17.2.0 |
| 2021-09 | SP-93E | SP-211081 | 3035 | 2 | F | Update UE subscription to contain information indicating authentication towards AAA server | 17.2.0 |
| 2021-09 | SP-93E | SP-210920 | 3040 | 1 | B | Updates on transferring AF request to PCF | 17.2.0 |
| 2021-09 | SP-93E | SP-210920 | 3043 | - | F | Correction on NEF related services | 17.2.0 |
| 2021-09 | SP-93E | SP-211015 | 3045 | 2 | C | Update NSAC for interworking | 17.2.0 |
| 2021-09 | SP-93E | SP-210930 | 3048 | 1 | B | KI#1, update the BMCA procedure | 17.2.0 |
| 2021-09 | SP-93E | SP-210922 | 3051 | 1 | F | Allowing NRF to provides S-NSSAI/DNN to NEF corresponding to an untrusted AF | 17.2.0 |
| 2021-09 | SP-93E | SP-210913 | 3053 | - | F | Update AMF location service operation to add the multiple QoS class | 17.2.0 |
| 2021-09 | SP-93E | SP-210926 | 3056 | 1 | F | Update the UE context in AMF | 17.2.0 |
| 2021-09 | SP-93E | SP-210903 | 3058 | 1 | A | Session Management Subscription data for EPS/5GS interworking | 17.2.0 |
| 2021-09 | SP-93E | SP-210903 | 3060 | 1 | A | Inter-AMF mobility with group monitoring | 17.2.0 |
| 2021-09 | SP-93E | SP-210902 | 3063 | 1 | A | Dual Access Type SMS registration | 17.2.0 |
| 2021-09 | SP-93E | SP-210904 | 3065 | - | A | 5GS Idle Status Indication | 17.2.0 |
| 2021-09 | SP-93E | SP-210904 | 3067 | - | A | Device Triggering parameter correction | 17.2.0 |
| 2021-09 | SP-93E | SP-210915 | 3069 | 1 | B | AUSF/UDM discovery based SUCI information | 17.2.0 |
| 2021-09 | SP-93E | SP-210924 | 3070 | 1 | F | Clarification on NRF service in case of SNPN | 17.2.0 |
| 2021-09 | SP-93E | SP-210926 | 3071 | 1 | F | Correction of NSACF service with AF consumer | 17.2.0 |
| 2021-09 | SP-93E | SP-210926 | 3072 | 1 | F | Update of NSACF Report Information and Event Trigger | 17.2.0 |
| 2021-09 | SP-93E | SP-210930 | 3073 | 1 | F | Updating a trusted AF for time synchronization service | 17.2.0 |
| 2021-09 | SP-93E | SP-210903 | 3075 | - | A | Update on EventExposure Subscribe services | 17.2.0 |
| 2021-09 | SP-93E | SP-210920 | 3077 | - | B | Support for EASDF registration and discovery | 17.2.0 |
| 2021-09 | SP-93E | SP-210920 | 3078 | 1 | F | update of Nudm_ServiceSpecificAuthorisation service operations | 17.2.0 |
| 2021-09 | SP-93E | SP-210920 | 3079 | 1 | B | Support of I-SMF removal | 17.2.0 |
| 2021-09 | SP-93E | SP-210930 | 3081 | 1 | F | Update on accessing the UDR data for time synchronization | 17.2.0 |
| 2021-09 | SP-93E | SP-210926 | 3084 | 1 | F | KI#5 Correction on Data subset name for Network Slice Specific Control Data | 17.2.0 |
| 2021-09 | SP-93E | SP-210932 | 3088 | 1 | F | Clarification on MUSIM capability exchange | 17.2.0 |
| 2021-09 | SP-93E | SP-210926 | 3090 | - | F | Resolve EN on signalling restriction when the maximum number of UEs has been reached for prolonged time | 17.2.0 |
| 2021-09 | SP-93E | SP-210926 | 3091 | - | B | Completion of NSAC per access type | 17.2.0 |
| 2021-09 | SP-93E | SP-210926 | 3094 | 1 | F | KI#1KI#2 - Resolve EN for NSAC procedure | 17.2.0 |
| 2021-09 | SP-93E | SP-210930 | 3096 | - | F | clarification for 5GS Bridge available event | 17.2.0 |
| 2021-09 | SP-93E | SP-210937 | 3106 | - | F | Update Configuration for Group Monitoring Event with adding Users | 17.2.0 |
| 2021-09 | SP-93E | SP-210915 | 3110 | 1 | F | Updating AMF with new Routing Indicator Data if re-registration is not triggered | 17.2.0 |
| 2021-09 | SP-93E | SP-210932 | 3111 | - | F | Clarification on registration procedure and access type | 17.2.0 |
| 2021-09 | SP-93E | SP-210920 | 3113 | 1 | F | Correction of ECS Address Configuration Information - Option 2 | 17.2.0 |
| 2021-09 | SP-93E | SP-210903 | 3118 | - | A | RAN-triggered PDU Session Release | 17.2.0 |
| 2021-09 | SP-93E | SP-210922 | 3122 | - | F | Correction on NWDAF information for Namf CreateUEContext service | 17.2.0 |
| 2021-09 | - | - | - | - | - | Correction to implementation of Table 5.2.6.25.8-1 (CRs 2965R1, 2936R1) | 17.2.1 |
| 2021-12 | SP-94E | SP-211289 | 2926 | 4 | B | AF specific UE ID retrieval | 17.3.0 |
| 2021-12 | SP-94E | SP-211284 | 2930 | 1 | F | UE location verification handling | 17.3.0 |
| 2021-12 | SP-94E | SP-211295 | 2944 | 1 | F | NSAC procedure in planned AMF removal case | 17.3.0 |
| 2021-12 | SP-94E | SP-211294 | 3008 | 2 | F | Correct the NRF services between SNPN and DCS | 17.3.0 |
| 2021-12 | SP-94E | SP-211288 | 3013 | 2 | F | PMF information transported via N4 | 17.3.0 |
| 2021-12 | SP-94E | SP-211302 | 3123 | - | F | MUSIM and CIoT in 5GS | 17.3.0 |
| 2021-12 | SP-94E | SP-211151 | 3124 | 3 | F | MUSIM capabilities in Emergency Registration | 17.3.0 |
| 2021-12 | SP-94E | SP-211305 | 3125 | - | F | Use of the Application Identifier in the AF influence on AM policies procedure | 17.3.0 |
| 2021-12 | SP-94E | SP-211295 | 3128 | 2 | F | Using Immediate reply in conjunction with NSACF related events | 17.3.0 |
| 2021-12 | SP-94E | SP-211301 | 3134 | - | F | Clarification on Disaster Roaming registration | 17.3.0 |
| 2021-12 | SP-94E | SP-211294 | 3138 | - | D | Rapporteur's editorial cleanup for eNPN | 17.3.0 |
| 2021-12 | SP-94E | SP-211286 | 3140 | 1 | F | Handling of MBS subscription data | 17.3.0 |
| 2021-12 | SP-94E | SP-211302 | 3141 | - | F | Removal of MUSIM mode | 17.3.0 |
| 2021-12 | SP-94E | SP-211305 | 3142 | - | F | Corrections to procedure for AF influence on AM policies | 17.3.0 |
| 2021-12 | SP-94E | SP-211301 | 3146 | 2 | C | Registration procedure improvement for MINT | 17.3.0 |
| 2021-12 | SP-94E | SP-211287 | 3148 | 1 | F | Introduction of NR RedCap Indication in UE context | 17.3.0 |
| 2021-12 | SP-94E | SP-211295 | 3152 | 1 | D | Editorial Changes on eNS_Ph2 | 17.3.0 |
| 2021-12 | SP-94E | SP-211290 | 3155 | 4 | B | Correction of UE Policies delivery notification | 17.3.0 |
| 2021-12 | SP-94E | SP-211300 | 3156 | 1 | F | Time synchronization - procedure review | 17.3.0 |
| 2021-12 | SP-94E | SP-211300 | 3157 | 1 | F | Alternative QoS and TSC fixes | 17.3.0 |
| 2021-12 | SP-94E | SP-211300 | 3158 | 1 | D | Rapporteur CR for editorial fixes | 17.3.0 |
| 2021-12 | SP-94E | SP-211284 | 3161 | 2 | F | Editorial correction in TS 23.502 | 17.3.0 |
| 2021-12 | SP-94E | SP-211290 | 3162 | 1 | F | Updates on I-SMF selection | 17.3.0 |
| 2021-12 | SP-94E | SP-211300 | 3164 | 1 | F | Updates on TSCTSF discovery and selection | 17.3.0 |
| 2021-12 | SP-94E | SP-211290 | 3166 | - | F | AF Coordination Information | 17.3.0 |
| 2021-12 | SP-94E | SP-211300 | 3167 | - | F | Addition of time synchronization service parameters | 17.3.0 |
| 2021-12 | SP-94E | SP-211302 | 3170 | 1 | F | Clean up about paging cause support indication in N2 message | 17.3.0 |
| 2021-12 | SP-94E | SP-211295 | 3172 | 1 | F | Clarification on EAC Mode Threshold and the Procedures | 17.3.0 |
| 2021-12 | SP-94E | SP-211295 | 3173 | - | F | Update of the Monitoring Event Description. | 17.3.0 |
| 2021-12 | SP-94E | SP-211301 | 3174 | 1 | F | MINT and EPC interworking. | 17.3.0 |
| 2021-12 | SP-94E | SP-211305 | 3175 | 1 | F | updates for service parameters regarding addition of UEs for group based event subscription | 17.3.0 |
| 2021-12 | SP-94E | SP-211294 | 3176 | 1 | F | Clarification for UE onboarding and UE access with CH credentials | 17.3.0 |
| 2021-12 | SP-94E | SP-211290 | 3179 | 1 | F | NEF service to support EAS deployment info and updated DNS server address | 17.3.0 |
| 2021-12 | SP-94E | SP-211280 | 3180 | - | F | Add the Scheduled Location Time | 17.3.0 |
| 2021-12 | SP-94E | SP-211295 | 3181 | 1 | F | EAC mode status notification | 17.3.0 |
| 2021-12 | SP-94E | SP-211290 | 3185 | 3 | F | Update Nnef_EASDeployment services | 17.3.0 |
| 2021-12 | SP-94E | SP-211295 | 3187 | 1 | F | Clarification of NSAC and exposure service | 17.3.0 |
| 2021-12 | SP-94E | SP-211286 | 3188 | 1 | F | Service operation for MBS session activation | 17.3.0 |
| 2021-12 | SP-94E | SP-211305 | 3189 | 2 | F | Correction to AF-triggered dynamically changing AM policies | 17.3.0 |
| 2021-12 | SP-94E | SP-211286 | 3192 | 1 | F | Correction on NRF service operations for MBS | 17.3.0 |
| 2021-12 | SP-94E | SP-211282 | 3193 | 1 | F | Service correction on 5G ProSe usage | 17.3.0 |
| 2021-12 | SP-94E | SP-211293 | 3196 | 3 | F | Miscellaneous correction for eNA_Ph2 | 17.3.0 |
| 2021-12 | SP-94E | SP-211303 | 3205 | - | F | EPS User Plane Integrity Protection corrections for Service Request and mixed eNB UPIP support; etc in TS 23.502. | 17.3.0 |
| 2021-12 | SP-94E | SP-211294 | 3206 | 3 | F | Adding PVS information as input to SMF and PCF service operation. | 17.3.0 |
| 2021-12 | SP-94E | SP-211300 | 3210 | 1 | F | Clarification on the Setting up and update AF session with required QoS procedure | 17.3.0 |
| 2021-12 | SP-94E | SP-211290 | 3211 | 1 | F | UE authorization for 5GC assisted EAS discovery | 17.3.0 |
| 2021-12 | SP-94E | SP-211290 | 3212 | 2 | F | Correction of ECS Address Configuration Information | 17.3.0 |
| 2021-12 | SP-94E | SP-211295 | 3215 | - | F | Threshold reporting mode | 17.3.0 |
| 2021-12 | SP-94E | SP-211623 | 3216 | 4 | B | Support of Paging subgrouping | 17.3.0 |
| 2021-12 | SP-94E | SP-211300 | 3217 | 1 | D | Rapporteur CR for editorial fixes - Inclusive Terminology | 17.3.0 |
| 2021-12 | SP-94E | SP-211290 | 3219 | 1 | F | Correction to AF provided ECS Address Configuration Information related details | 17.3.0 |
| 2021-12 | SP-94E | SP-211283 | 3223 | 1 | F | Missing UDM service operations | 17.3.0 |
| 2021-12 | SP-94E | SP-211276 | 3227 | 1 | A | V-SMF change at inter-PLMN mobility | 17.3.0 |
| 2021-12 | SP-94E | SP-211301 | 3228 | 1 | C | UE configuration procedure update for MINT | 17.3.0 |
| 2021-12 | SP-94E | SP-211283 | 3229 | - | F | NG-RAN location report clarification in RRC Inactive | 17.3.0 |
| 2021-12 | SP-94E | SP-211282 | 3232 | 1 | F | Update to Nnrf_NFManagement_NFRegister service operation | 17.3.0 |
| 2021-12 | SP-94E | SP-211304 | 3233 | 1 | F | Update to Nnrf_NFManagement_NFRegister service operation | 17.3.0 |
| 2021-12 | SP-94E | SP-211300 | 3235 | 1 | F | Adding Trusted AF in Time Synchronization procedures | 17.3.0 |
| 2021-12 | SP-94E | SP-211302 | 3239 | 1 | F | MUSIM features for Emergency Registration | 17.3.0 |
| 2021-12 | SP-94E | SP-211298 | 3240 | 1 | F | UASNF registration and discovery | 17.3.0 |
| 2021-12 | SP-94E | SP-211278 | 3242 | 1 | A | RID Update for SNPN UEs | 17.3.0 |
| 2021-12 | SP-94E | SP-211300 | 3246 | 1 | F | 23.502: TSCTSF Discovery and Selection | 17.3.0 |
| 2021-12 | SP-94E | SP-211300 | 3247 | 1 | F | 23.502: Time Sync exposure procedure | 17.3.0 |
| 2021-12 | SP-94E | SP-211300 | 3248 | 1 | F | Fixes for AF session with required QoS update procedure | 17.3.0 |
| 2021-12 | SP-94E | SP-211284 | 3250 | - | B | Indicating a last visited TAI in a Registration for NR Satellite Access | 17.3.0 |
| 2021-12 | SP-94E | SP-211284 | 3251 | - | B | Support of NG-RAN Location Reporting for NR Satellite Access | 17.3.0 |
| 2021-12 | SP-94E | SP-211295 | 3252 | 1 | F | NSAC clarification | 17.3.0 |
| 2021-12 | SP-94E | SP-211278 | 3256 | 1 | A | correction for CAG restrictions with emergency services | 17.3.0 |
| 2021-12 | SP-94E | SP-211293 | 3258 | - | F | Update to NF services for UE data collection | 17.3.0 |
| 2021-12 | SP-94E | SP-211295 | 3260 | 1 | F | Clarification on Access Type for NSAC | 17.3.0 |
| 2021-12 | SP-94E | SP-211304 | 3263 | 1 | A | AMF re-allocation during inter PLMN mobility | 17.3.0 |
| 2021-12 | SP-94E | SP-211300 | 3269 | 1 | F | Clarifications on the use of DS-TT port MAC address | 17.3.0 |
| 2021-12 | SP-94E | SP-211304 | 3272 | 1 | F | Tunnel info release for inter system mobility with N26 | 17.3.0 |
| 2021-12 | SP-94E | SP-211304 | 3276 | 1 | C | The update for Nnrf_NFDiscovery_Request service operation | 17.3.0 |
| 2021-12 | SP-94E | SP-211290 | 3277 | 1 | F | I-SMF removal triggered by removal of target DNAI | 17.3.0 |
| 2021-12 | SP-94E | SP-211294 | 3280 | 1 | F | 23.502 Clarification on NF discovery by NRF in Onboarding or external authentication scenario | 17.3.0 |
| 2021-12 | SP-94E | SP-211625 | 3281 | 3 | F | 23.502 Update procedure of Registration with Onboarding SNPN | 17.3.0 |
| 2021-12 | SP-94E | SP-211302 | 3287 | 1 | F | Clarification on paging restrictions | 17.3.0 |
| 2021-12 | SP-94E | SP-211302 | 3288 | 1 | F | Paging Cause Indication for Voice Services Supported in the RRC Inactive AI | 17.3.0 |
| 2021-12 | SP-94E | SP-211300 | 3291 | - | F | Clarification on the Ntsctsf_QoSandTSCAssistance related service operation | 17.3.0 |
| 2021-12 | SP-94E | SP-211274 | 3295 | 1 | A | Providing UE's address to AMF during registration via trusted Non-3GPP access | 17.3.0 |
| 2021-12 | SP-94E | SP-211279 | 3299 | 1 | A | Layer below IPsec to enable NAT traversal for TNGF/N3IWF access | 17.3.0 |
| 2021-12 | SP-94E | SP-211304 | 3301 | 1 | F | TAU with active flag in case the entire PDU session is rejected | 17.3.0 |
| 2021-12 | SP-94E | SP-211278 | 3303 | 1 | A | Include TSN time domain into bridge information reporting procedure | 17.3.0 |
| 2021-12 | SP-94E | SP-211295 | 3304 | 1 | F | Correct the UDM indication and RFSP index in UE Context in AMF table | 17.3.0 |
| 2021-12 | SP-94E | SP-211295 | 3309 | 1 | F | Clarification on the NSACF result parameter sent to AMF | 17.3.0 |
| 2021-12 | SP-94E | SP-211304 | 3311 | - | A | Corrections to Handover of a PDU Session procedure between 3GPP and untrusted non-3GPP access / NOTE: CR Cover shows CR 3310. | 17.3.0 |
| 2021-12 | SP-94E | SP-211305 | 3312 | 1 | F | Support of GERAN/UTRAN access: Annex G alignment to CR 2970r1 to TS 23.501 | 17.3.0 |
| 2021-12 | SP-94E | SP-211273 | 3316 | - | A | Update the location service operations to add service identity and service type | 17.3.0 |
| 2022-03 | SP-95E | SP-220066 | 3102 | 2 | F | AMF relocation in connected state | 17.4.0 |
| 2022-03 | SP-95E | SP-220066 | 3150 | 4 | F | Clarification on rerouted Registration Request message | 17.4.0 |
| 2022-03 | SP-95E | SP-220041 | 3135 | 4 | F | SMF+PGW-C assigned PDU Session ID / (Working Agreement #43) | 17.4.0 |
| 2022-03 | SP-95E | SP-220047 | 3225 | 2 | A | Mapping TSCAI between TSN GM clock and 5GS clock | 17.4.0 |
| 2022-03 | SP-95E | SP-220045 | 3231 | 3 | A | Service Request and PCF interaction | 17.4.0 |
| 2022-03 | SP-95E | SP-220066 | 3271 | 2 | F | Inter PLMN handover procedure | 17.4.0 |
| 2022-03 | SP-95E | SP-220066 | 3273 | 2 | F | N9 forwarding tunnel between ULCLs controlled by I-SMF | 17.4.0 |
| 2022-03 | SP-95E | SP-220058 | 3318 | 1 | F | Clarification on indication of NSSRG support | 17.4.0 |
| 2022-03 | SP-95E | SP-220057 | 3321 | 1 | F | Remove the CP based remote provisioning | 17.4.0 |
| 2022-03 | SP-95E | SP-220055 | 3322 | - | F | Corrections on notification of user plane management event procedure | 17.4.0 |
| 2022-03 | SP-95E | SP-220057 | 3323 | 1 | F | DN-AAA server selection when the DCS is not involved during primary authentication | 17.4.0 |
| 2022-03 | SP-95E | SP-220056 | 3324 | 1 | F | Cleanup for NRF service operations usage for analytics | 17.4.0 |
| 2022-03 | SP-95E | SP-220066 | 3325 | 1 | F | Correction related to EPS to 5GC HO. | 17.4.0 |
| 2022-03 | SP-95E | SP-220055 | 3327 | 1 | F | Correction related to EDI | 17.4.0 |
| 2022-03 | SP-95E | SP-220062 | 3330 | 1 | B | Authentication and Subscription information checking for Disaster Roaming service | 17.4.0 |
| 2022-03 | SP-95E | SP-220062 | 3332 | 1 | F | Delete the EN on disaster roaming revoking | 17.4.0 |
| 2022-03 | SP-95E | SP-220060 | 3333 | 1 | F | Correction on 5G access stratum time distribution | 17.4.0 |
| 2022-03 | SP-95E | SP-220054 | 3335 | 1 | F | Internal 23.502 alignment on UE addressing information that an AF can provide | 17.4.0 |
| 2022-03 | SP-95E | SP-220046 | 3337 | 1 | A | Handover of a PDU Session from 3GPP to untrusted non-3GPP access (I-SMF case) | 17.4.0 |
| 2022-03 | SP-95E | SP-220060 | 3338 | 1 | F | Alignment of the 5G AS time distribution management procedure | 17.4.0 |
| 2022-03 | SP-95E | SP-220060 | 3339 | - | F | Clarifying the 5G AS time distribution parameter delivery to NG-RAN | 17.4.0 |
| 2022-03 | SP-95E | SP-220060 | 3340 | - | F | Correcting the naming and/or description of some BSF service operations | 17.4.0 |
| 2022-03 | SP-95E | SP-220066 | 3341 | 1 | F | Correction to UE Configuration Update procedure for transparent UE Policy delivery | 17.4.0 |
| 2022-03 | SP-95E | SP-220045 | 3345 | 1 | A | Data forwarding indication during HO | 17.4.0 |
| 2022-03 | SP-95E | SP-220066 | 3346 | 1 | F | Updating AMF with new Routing Indicator Data if re-registration is not triggered | 17.4.0 |
| 2022-03 | SP-95E | SP-220066 | 3353 | 1 | F | Handling of VPLMN QoS constraints during mobility | 17.4.0 |
| 2022-03 | SP-95E | SP-220067 | 3355 | - | F | Correction to Nnef_AMInfluence_Create | 17.4.0 |
| 2022-03 | SP-95E | SP-220055 | 3358 | - | F | Correction on notification on the outcome of UE Policies delivery due to service specific parameter provisioning | 17.4.0 |
| 2022-03 | SP-95E | SP-220057 | 3359 | 1 | F | UE SM context fetch in registration procedure during inter-network mobility | 17.4.0 |
| 2022-03 | SP-95E | SP-220052 | 3361 | 1 | F | NRF service operations for MBS | 17.4.0 |
| 2022-03 | SP-95E | SP-220066 | 3362 | 1 | F | Secondary reauthentication | 17.4.0 |
| 2022-03 | SP-95E | SP-220067 | 3363 | - | F | Clarification on non-3gpp AN selection | 17.4.0 |
| 2022-03 | SP-95E | SP-220055 | 3366 | 1 | F | Add UE capability to SMF decision for ECS address delivery | 17.4.0 |
| 2022-03 | SP-95E | SP-220055 | 3367 | 1 | F | Add UPF event exposure that supports direct QoS monitoring | 17.4.0 |
| 2022-03 | SP-95E | SP-220060 | 3369 | 1 | F | Multiple NW-TTs associated with a single UPF | 17.4.0 |
| 2022-03 | SP-95E | SP-220060 | 3370 | 1 | F | Clarifications and clean-ups for TSC | 17.4.0 |
| 2022-03 | SP-95E | SP-220057 | 3371 | 1 | F | terms alignments and clean-ups for eNPN | 17.4.0 |
| 2022-03 | SP-95E | SP-220066 | 3373 | 1 | F | Alignment of PCC input parameter documentation | 17.4.0 |
| 2022-03 | SP-95E | SP-220045 | 3376 | 1 | A | UP path change notification to the AF | 17.4.0 |
| 2022-03 | SP-95E | SP-220059 | 3377 | 1 | F | Correction on UAS NF discovery | 17.4.0 |
| 2022-03 | SP-95E | SP-220067 | 3379 | - | F | Correction to Management of AM Policies at SM policy association establishment and termination | 17.4.0 |
| 2022-03 | SP-95E | SP-220067 | 3380 | 1 | F | Correction to Processing AF requests to influence AM policies | 17.4.0 |
| 2022-03 | SP-95E | SP-220062 | 3383 | 1 | F | Applicability of lists provided by VPLMN | 17.4.0 |
| 2022-03 | SP-95E | SP-220062 | 3385 | - | F | Disaster roaming registration type | 17.4.0 |
| 2022-03 | SP-95E | SP-220046 | 3387 | 1 | A | Mobility between HPLMN and VPLMN | 17.4.0 |
| 2022-03 | SP-95E | SP-220050 | 3389 | - | F | Corrections for 5G ProSe | 17.4.0 |
| 2022-03 | SP-95E | SP-220058 | 3392 | - | F | Remove the Editor's Note about Multiple NSACFs | 17.4.0 |
| 2022-03 | SP-95E | SP-220060 | 3396 | 1 | F | Clean up of the time synchronization procedures. | 17.4.0 |
| 2022-03 | SP-95E | SP-220056 | 3397 | 1 | F | Removal of Nnssf_NSRestriction service | 17.4.0 |
| 2022-03 | SP-95E | SP-220280 | 3398 | 1 | F | SBI Message Priority for MPS | 17.4.0 |
| 2022-03 | SP-95E | SP-220063 | 3399 | 1 | F | UE Configuration Update support for MPS. | 17.4.0 |
| 2022-03 | SP-95E | SP-220066 | 3400 | 1 | F | Enforcement of VPLMN QoS policies | 17.4.0 |
| 2022-03 | SP-95E | SP-220066 | 3402 | 1 | F | Registration type to the UDM for SoR | 17.4.0 |
| 2022-03 | SP-95E | SP-220060 | 3407 | 1 | F | Update to AF session with required QoS procedures | 17.4.0 |
| 2022-03 | SP-95E | SP-220057 | 3408 | 1 | F | SNPN with CH Subscription profile prohibits HR | 17.4.0 |
| 2022-03 | SP-95E | SP-220058 | 3411 | 1 | F | NSAC for maximum number of PDU Sessions and MA PDU Session | 17.4.0 |
| 2022-03 | SP-95E | SP-220060 | 3414 | 1 | F | Clarification on the TSCTSF discovery | 17.4.0 |
| 2022-03 | SP-95E | SP-220058 | 3416 | 1 | F | Clarification on support of roaming for NSAC | 17.4.0 |
| 2022-03 | SP-95E | SP-220066 | 3417 | 1 | F | Paging Early Indication: Removal of Editor's note | 17.4.0 |
| 2022-03 | SP-95E | SP-220055 | 3419 | 1 | F | Corrections of EDC functionality description | 17.4.0 |
| 2022-06 | SP-96 | SP-220406 | 3147 | 5 | F | Session procedure improvement for MINT | 17.5.0 |
| 2022-06 | SP-96 | SP-220412 | 3300 | 4 | B | Enabling configuration of Network Slice AS Groups | 17.5.0 |
| 2022-06 | SP-96 | SP-220391 | 3320 | 2 | A | AMF interaction with GMLC at SRVCC for an Emergency session | 17.5.0 |
| 2022-06 | SP-96 | SP-220401 | 3391 | 2 | F | Clarification of NSAC about the Access Type | 17.5.0 |
| 2022-06 | SP-96 | SP-220410 | 3403 | 2 | F | Inter-AMF Xn handover | 17.5.0 |
| 2022-06 | SP-96 | SP-220401 | 3405 | 2 | F | Correction on NSACF exposure | 17.5.0 |
| 2022-06 | SP-96 | SP-220394 | 3420 | - | F | RAN indication that UE has moved out of PLMN serving area | 17.5.0 |
| 2022-06 | SP-96 | SP-220406 | 3421 | 1 | F | Network-initiated Deregistration if disaster condition is no longer being applicable | 17.5.0 |
| 2022-06 | SP-96 | SP-220398 | 3423 | 1 | F | Outcome of UE Policies delivery procedure | 17.5.0 |
| 2022-06 | SP-96 | SP-220399 | 3426 | 1 | F | Correction to Naf_EventExposure service | 17.5.0 |
| 2022-06 | SP-96 | SP-220397 | 3427 | - | F | AF specific UE ID retrieval procedure correction | 17.5.0 |
| 2022-06 | SP-96 | SP-220410 | 3430 | 2 | F | Number of TFT filters exceeding allowed limit for 5GS to EPS interworking | 17.5.0 |
| 2022-06 | SP-96 | SP-220404 | 3433 | 1 | F | Cleaning up the time synchronization procedures | 17.5.0 |
| 2022-06 | SP-96 | SP-220404 | 3434 | 1 | F | Correcting the 5G AS time distribution procedure | 17.5.0 |
| 2022-06 | SP-96 | SP-220394 | 3436 | 1 | F | Correction of last visited TAI requirement | 17.5.0 |
| 2022-06 | SP-96 | SP-220406 | 3437 | 1 | F | Session related subscription information | 17.5.0 |
| 2022-06 | SP-96 | SP-220404 | 3439 | - | F | Terminology Alignment for AF session with required QoS procedures | 17.5.0 |
| 2022-06 | SP-96 | SP-220404 | 3440 | 1 | F | Corrections to time synchronization procedures | 17.5.0 |
| 2022-06 | SP-96 | SP-220394 | 3442 | - | F | TAIs reporting corresponding to the Selected PLMN | 17.5.0 |
| 2022-06 | SP-96 | SP-220400 | 3445 | 1 | F | SMF UP remote provisioning capability | 17.5.0 |
| 2022-06 | SP-96 | SP-220404 | 3447 | 1 | F | corrections for 5GS Bridge Information reporting and subscription | 17.5.0 |
| 2022-06 | SP-96 | SP-220404 | 3448 | 1 | F | 23.502 Term Changes for IIoT | 17.5.0 |
| 2022-06 | SP-96 | SP-220399 | 3450 | 1 | F | Adding NWDAF as service consumer of NSACF | 17.5.0 |
| 2022-06 | SP-96 | SP-220409 | 3451 | 1 | F | Alignment of terminology for PCF related procedures | 17.5.0 |
| 2022-06 | SP-96 | SP-220399 | 3453 | - | F | Corrections to Redundant Transmission Experience for SMF event exposure | 17.5.0 |
| 2022-06 | SP-96 | SP-220400 | 3457 | 2 | F | Clarification on the FQDN(s) and IP address(es) of PVS for remote provisioning | 17.5.0 |
| 2022-06 | SP-96 | SP-220404 | 3458 | 1 | F | Clarification on the PCF service operation consumer | 17.5.0 |
| 2022-06 | SP-96 | SP-220404 | 3459 | 2 | F | Clarification on 5G access stratum distribution in mobility | 17.5.0 |
| 2022-06 | SP-96 | SP-220398 | 3460 | 1 | F | Clarification for Edge Relocation Triggered by AF | 17.5.0 |
| 2022-06 | SP-96 | SP-220406 | 3462 | 1 | F | Clarification on MINT support and end of disaster | 17.5.0 |
| 2022-06 | SP-96 | SP-220398 | 3464 | - | F | Correction to the Service Specific Authorization procedure | 17.5.0 |
| 2022-06 | SP-96 | SP-220410 | 3465 | - | F | AMF relocation in connected state | 17.5.0 |
| 2022-06 | SP-96 | SP-220406 | 3467 | - | C | UE capabilities indication for UPU with Disaster Roaming information | 17.5.0 |
| 2022-06 | SP-96 | SP-220391 | 3469 | 1 | A | Clarification of NIDD Authorization | 17.5.0 |
| 2022-06 | SP-96 | SP-220394 | 3471 | 1 | F | Removal of indication of country of UE location | 17.5.0 |
| 2022-06 | SP-96 | SP-220411 | 3475 | 1 | F | Correction related to roaming | 17.5.0 |
| 2022-06 | SP-96 | SP-220410 | 3476 | - | F | NRF discovery and selection | 17.5.0 |
| 2022-06 | SP-96 | SP-220389 | 3479 | 1 | A | Correction on N2 based handover procedure | 17.5.0 |
| 2022-06 | SP-96 | SP-220391 | 3487 | 1 | A | Correction of the Signalling Based Tracing support | 17.5.0 |
| 2022-06 | SP-96 | SP-220410 | 3488 | 1 | F | GBR QoS flow preservation when N2 signalling re-established from another RAN | 17.5.0 |
| 2022-06 | SP-96 | SP-220410 | 3489 | 1 | F | S-NSSAI of PDU Session registered to UDM | 17.5.0 |
| 2022-06 | SP-96 | SP-220411 | 3490 | - | F | Correction on N9 forwarding tunnel between ULCLs controlled by I-SMF | 17.5.0 |
| 2022-06 | SP-96 | SP-220410 | 3493 | 1 | F | UDR storing of non-subscriber related data | 17.5.0 |
| 2022-06 | SP-96 | SP-220410 | 3494 |  | F | Alignment of UDR data sets | 17.5.0 |
| 2022-06 | SP-96 | SP-220410 | 3495 | 1 | F | Emergency service continuity and interworking without n26 | 17.5.0 |
| 2022-06 | SP-96 | SP-220410 | 3497 | 1 | F | Correction of UE Configuration Update procedure conditions for Registration Required and NAS Release | 17.5.0 |
| 2022-06 | SP-96 | SP-220398 | 3498 | 1 | F | Alignment of ECS Address Configuration Information to SA6's definition | 17.5.0 |
| 2022-09 | SP-97E | SP-220779 | 3463 | 3 | F | DN-AAA server selection during UE onboarding | 17.6.0 |
| 2022-09 | SP-97E | SP-220777 | 3470 | 2 | F | Clarification on Authorization of Service Specific parameter provisioning | 17.6.0 |
| 2022-09 | SP-97E | SP-220789 | 3500 | 1 | F | Correction to N2 based HO in ETSUN case | 17.6.0 |
| 2022-09 | SP-97E | SP-220788 | 3501 | 1 | B | TS23.502 Alignment of SBI-based SMS | 17.6.0 |
| 2022-09 | SP-97E | SP-220789 | 3502 | - | F | Clarification on UE reachability for SMS event subscription by NEF | 17.6.0 |
| 2022-09 | SP-97E | SP-220780 | 3503 | - | F | Correction on NSSRG information | 17.6.0 |
| 2022-09 | SP-97E | SP-220789 | 3504 | 1 | F | Correction to PLMN ID used in Nudm services | 17.6.0 |
| 2022-09 | SP-97E | SP-220785 | 3506 | - | F | UCU procedure for MINT update | 17.6.0 |
| 2022-09 | SP-97E | SP-220789 | 3507 | 1 | F | UE presence in AoI clarification | 17.6.0 |
| 2022-09 | SP-97E | SP-220769 | 3508 | 1 | C | Periodic update time from UE | 17.6.0 |
| 2022-09 | SP-97E | SP-220777 | 3512 | - | F | Adding the EAS rediscovery indication on the PDU session modification procedure | 17.6.0 |
| 2022-09 | SP-97E | SP-220789 | 3513 | - | F | Clarification on NSSAA related mobility restrictions | 17.6.0 |
| 2022-09 | SP-97E | SP-220789 | 3514 | 1 | F | Handover capability detection | 17.6.0 |
| 2022-09 | SP-97E | SP-220789 | 3515 | 1 | F | Missing UDSF timer service | 17.6.0 |
| 2022-09 | SP-97E | SP-220783 | 3516 | 1 | F | Mapping GPSIs and Group Identifiers to a SUPI list | 17.6.0 |
| 2022-09 | SP-97E | SP-220783 | 3517 | - | F | Clarification that NEF uses time sync services provided by TSCTSF | 17.6.0 |
| 2022-09 | SP-97E | SP-220771 | 3522 | 1 | A | Clarification on RAN sharing in case of SNPN | 17.6.0 |
| 2022-09 | SP-97E | SP-220786 | 3526 | 1 | F | Clarifications on Priority Subscription | 17.6.0 |
| 2022-09 | SP-97E | SP-220783 | 3531 | - | F | Clarification on 5G access stratum distribution in mobility and AM policy modification | 17.6.0 |
| 2022-09 | SP-97E | SP-220774 | 3535 | 1 | F | AMF sends forbidden TAI(s) to UE | 17.6.0 |
| 2022-09 | SP-97E | SP-220769 | 3536 | 1 | A | Clarification on NAS PDU delivery during PDU Session modification | 17.6.0 |
| 2022-09 | SP-97E | SP-220780 | 3539 | 1 | F | UE context transferring between AMF | 17.6.0 |
| 2022-09 | SP-97E | SP-220771 | 3541 | 1 | A | Correction on 5G VN group management | 17.6.0 |
| 2022-09 | SP-97E | SP-220893 | 3543 | 1 | A | Removal of EAP Re-authentication | 17.6.0 |
| 2022-12 | SP-98E | SP-221079 | 3431 | 5 | F | Traffic Identification using ToS/TC for 5G Media Streaming | 17.7.0 |
| 2022-12 | SP-98E | SP-221076 | 3527 | 2 | F | Alignment of IIoT related parameter description | 17.7.0 |
| 2022-12 | SP-98E | SP-221080 | 3551 | - | F | Alignment of TS 23.502 with SBI-based SMS | 17.7.0 |
| 2022-12 | SP-98E | SP-221067 | 3552 | 1 | F | Correction to Nnef_UEId_Get | 17.7.0 |
| 2022-12 | SP-98E | SP-221063 | 3560 | 1 | A | 3GPP PS Data Off status in PDU Session Establishment | 17.7.0 |
| 2022-12 | SP-98E | SP-221079 | 3562 | - | F | Release of emergency PDU Session without data transfer for a period | 17.7.0 |
| 2022-12 | SP-98E | SP-221073 | 3563 | 1 | F | Clarification on EAC Mode for NSAC | 17.7.0 |
| 2022-12 | SP-98E | SP-221076 | 3573 | 1 | F | Clarification on time synchronization error budget provisioning and ASTI management | 17.7.0 |
| 2022-12 | SP-98E | SP-221079 | 3587 | 1 | F | Update service operation used in AMF relocation in Inter PLMN handover procedure | 17.7.0 |
| 2022-12 | SP-98E | SP-221076 | 3589 | - | F | Adding SUPI in BSF-DISCOVER output | 17.7.0 |
| 2022-12 | SP-98E | SP-221078 | 3600 | 1 | F | PLMN with disaster condition | 17.7.0 |
| 2022-12 | SP-98E | SP-221079 | 3635 | 3 | F | Correction to UE Policy Association Establishment procedure for roaming scenario | 17.7.0 |
| 2022-12 | SP-98E | SP-221332 | 3657 | 1 | F | Aerial Service Availability Update using UCU | 17.7.0 |
| 2022-12 | SP-98E | SP-221094 | 3553 | 5 | B | Secondary DN authentication and authorization in EPS IWK case | 18.0.0 |
| 2022-12 | SP-98E | SP-221090 | 3555 | 1 | B | Support of RRC_INACTIVE with long eDRX | 18.0.0 |
| 2022-12 | SP-98E | SP-221085 | 3557 | 1 | C | RFSP index in use at 5GS to EPS mobility | 18.0.0 |
| 2022-12 | SP-98E | SP-221085 | 3564 | 1 | B | RFSP index during interworking | 18.0.0 |
| 2022-12 | SP-98E | SP-221087 | 3565 | 1 | B | Support of Non-3GPP access for SNPN | 18.0.0 |
| 2022-12 | SP-98E | SP-221087 | 3569 | 1 | B | Equivalent SNPN support | 18.0.0 |
| 2022-12 | SP-98E | SP-221092 | 3574 | 1 | B | AF provides PER to NEF/PCF (as concluded for 23.700-25, KI#4) | 18.0.0 |
| 2022-12 | SP-98E | SP-221089 | 3575 | 1 | B | Enhance group status event reporting | 18.0.0 |
| 2022-12 | SP-98E | SP-221093 | 3576 | 1 | B | UPF service update in 23.502 according to the conclusion in UPEAS | 18.0.0 |
| 2022-12 | SP-98E | SP-221084 | 3578 | 1 | B | Introduction to N3IWF selection to support the slices needed by the UE | 18.0.0 |
| 2022-12 | SP-98E | SP-221093 | 3583 | 1 | B | UPF event exposure service to NWDAF in TS 23.502 | 18.0.0 |
| 2022-12 | SP-98E | SP-221092 | 3584 | 3 | B | RAN feedback for burst sending time adjustment | 18.0.0 |
| 2022-12 | SP-98E | SP-221091 | 3598 | 1 | B | Support of unavailability period | 18.0.0 |
| 2022-12 | SP-98E | SP-221092 | 3610 | 2 | B | Support for coverage area filters for time synchronization service - procedures | 18.0.0 |
| 2022-12 | SP-98E | SP-221092 | 3611 | 2 | B | Introduction of subscription-based distribution of timing information - procedures | 18.0.0 |
| 2022-12 | SP-98E | SP-221139 | 3621 | 3 | B | Enhance NRF services for trained ML model sharing | 18.0.0 |
| 2022-12 | SP-98E | SP-221139 | 3622 | 1 | B | NRF service enhancements for Federated Learning | 18.0.0 |
| 2022-12 | SP-98E | SP-221086 | 3625 | 2 | B | KI#4 23.502 AF traffic influence for common EAS, DNAI selection | 18.0.0 |
| 2022-12 | SP-98E | SP-221083 | 3629 | 2 | B | Support of Satellite Edge Computing via UPF deployed on satellite | 18.0.0 |
| 2022-12 | SP-98E | SP-221096 | 3630 | 3 | B | Enhancements of PCF Services and NEF Services | 18.0.0 |
| 2022-12 | SP-98E | SP-221086 | 3642 | 1 | B | SMF Selection data for HR SBO in VPLMN | 18.0.0 |
| 2022-12 | SP-98E | SP-221092 | 3645 | 2 | B | Interworking with TSN network deployed in the transport network | 18.0.0 |
| 2022-12 | SP-98E | SP-221096 | 3654 | 3 | B | AIMLsys: KI#1 - 23.502 Solution for 5GC assistance to support Group-MBR Monitoring via NEF Event Exposure Extensions | 18.0.0 |
| 2023-03 | SP-99 | SP-230080 | 3432 | 1 | D | RRC state and CM state terminology alignment | 18.1.0 |
| 2023-03 | SP-99 | SP-230070 | 3595 | 2 | B | MPS when access to 5GC is WLAN | 18.1.0 |
| 2023-03 | SP-99 | SP-230058 | 3603 | 4 | C | Introducing selection of more granular set of UEs | 18.1.0 |
| 2023-03 | SP-99 | SP-230058 | 3619 | 5 | B | EAS Re-discovery with EASDF for HR PDU session | 18.1.0 |
| 2023-03 | SP-99 | SP-230052 | 3644 | 3 | B | Reporting the RAN timing synchronization status change from AMF to TSCTSF | 18.1.0 |
| 2023-03 | SP-99 | SP-230058 | 3656 | 4 | B | Edge Relocation within the same hosting PLMN's EHEs | 18.1.0 |
| 2023-03 | SP-99 | SP-230063 | 3658 | 2 | B | N5CW device access to SNPN services | 18.1.0 |
| 2023-03 | SP-99 | SP-230077 | 3665 | 1 | B | Data Exposure by UPF via SBI aligned with TS 23.502 | 18.1.0 |
| 2023-03 | SP-99 | SP-230372 | 3666 | 8 | B | Support of NAT exposure in 23.502 according to the conclusion in UPEAS | 18.1.0 |
| 2023-03 | SP-99 | SP-230075 | 3667 | 1 | B | Support for AF influence on Service Function Chaining | 18.1.0 |
| 2023-03 | SP-99 | SP-230044 | 3669 | 1 | A | Correction of subscribed User Plane Security Policy when UE is in EPC | 18.1.0 |
| 2023-03 | SP-99 | SP-230054 | 3672 | 6 | B | 23.502 Solution for new service to support QoS Resource Allocation and QoS Monitoring operation for group of AF Sessions | 18.1.0 |
| 2023-03 | SP-99 | SP-230054 | 3673 | 5 | B | AIMLsys: KI#5 - Planned Data Transfer with QoS Policy (PDTQ) Negotiation and Activation for future PDU session to support Application AI/ML data transfer | 18.1.0 |
| 2023-03 | SP-99 | SP-230054 | 3674 | 6 | B | AIMLsys: KI#7 - NEF services description for assistance to member selection | 18.1.0 |
| 2023-03 | SP-99 | SP-230058 | 3676 | 7 | B | HR-SBO support SM subscription data and SMF services | 18.1.0 |
| 2023-03 | SP-99 | SP-230057 | 3683 | 4 | B | Support of integration with IETF Deterministic Networking | 18.1.0 |
| 2023-03 | SP-99 | SP-230081 | 3684 | 2 | B | 23.502 - Spending Limits for UE Policies in the 5GC | 18.1.0 |
| 2023-03 | SP-99 | SP-230072 | 3685 | 1 | C | Update of CN based MT handling | 18.1.0 |
| 2023-03 | SP-99 | SP-230078 | 3688 | 1 | B | MBSR Location Reporting to update Warning Area List for PWS | 18.1.0 |
| 2023-03 | SP-99 | SP-230048 | 3689 | 1 | B | Introducing 5G ProSe ph2 function for KI#5: Authorizing multi-path transmission via direct Uu and L2 U2N Relay | 18.1.0 |
| 2023-03 | SP-99 | SP-230081 | 3690 | 1 | F | IPv6 prefix delegation in 5GS | 18.1.0 |
| 2023-03 | SP-99 | SP-230080 | 3691 | - | F | Correcting the step of H-SMF providing Always-On PDU Session granted indication | 18.1.0 |
| 2023-03 | SP-99 | SP-230042 | 3701 | 1 | A | Clarify the procedure when the NEF reject the AF update request | 18.1.0 |
| 2023-03 | SP-99 | SP-230051 | 3705 | 5 | B | RRC_INACTIVE UE receiving multicast MBS data, provisioning UE level MBS assistance information | 18.1.0 |
| 2023-03 | SP-99 | SP-230056 | 3707 | 1 | B | Non-3GPP access path switching | 18.1.0 |
| 2023-03 | SP-99 | SP-230068 | 3708 | 1 | B | Exposure of Service Area and Default QoS for a DNN/S-NSSAI and group of UEs | 18.1.0 |
| 2023-03 | SP-99 | SP-230068 | 3710 | 1 | B | Exposure of traffic characteristics and performance monitoring for a group of UEs, using new NEF service | 18.1.0 |
| 2023-03 | SP-99 | SP-230065 | 3712 | 7 | B | Service Parameters for URSP in VPLMN | 18.1.0 |
| 2023-03 | SP-99 | SP-230052 | 3716 | 1 | F | Corrections to time synchronization based on subscription KI3 | 18.1.0 |
| 2023-03 | SP-99 | SP-230052 | 3717 | 1 | C | RAN feedback for periodicity adjustment KI6 | 18.1.0 |
| 2023-03 | SP-99 | SP-230062 | 3727 | 1 | B | PFD Determination by NEF (PFDF) | 18.1.0 |
| 2023-03 | SP-99 | SP-230247 | 3734 | 1 | B | Procedures update to support policy control enhancements for multi-modal flows | 18.1.0 |
| 2023-03 | SP-99 | SP-230055 | 3735 | - | F | Missing part in approved S2-2209611 from SA2#153E | 18.1.0 |
| 2023-03 | SP-99 | SP-230247 | 3736 | 1 | B | Introduction of KI#6 conclusion: uplink-downlink transmission coordination | 18.1.0 |
| 2023-03 | SP-99 | SP-230247 | 3738 | 1 | B | AF Session procedures update to support PDU Set QoS Parameters | 18.1.0 |
| 2023-03 | SP-99 | SP-230065 | 3740 | 1 | B | Support URSP provisioning in EPS | 18.1.0 |
| 2023-03 | SP-99 | SP-230080 | 3742 | 1 | F | TS23.502: Clarification of handling of the non-3GPP PDU session in Non-allowed service area | 18.1.0 |
| 2023-03 | SP-99 | SP-230056 | 3748 | 1 | B | Support non-3GPP access leg of MA-PDU Session with PDN connection in EPC | 18.1.0 |
| 2023-03 | SP-99 | SP-230069 | 3757 | 1 | B | Identifier availability for Lawful Interception during MME-5GS handover | 18.1.0 |
| 2023-03 | SP-99 | SP-230050 | 3760 | 1 | B | Procedures update to support of dynamic satellite backhaul | 18.1.0 |
| 2023-03 | SP-99 | SP-230050 | 3761 | 1 | B | Procedures update to support of Satellite Edge Computing | 18.1.0 |
| 2023-03 | SP-99 | SP-230053 | 3762 | 1 | B | TNGF selection enhancement for support of S-NSSAI needed by UE | 18.1.0 |
| 2023-03 | SP-99 | SP-230040 | 3767 | 1 | A | S-NSSAI correction for the roaming case | 18.1.0 |
| 2023-03 | SP-99 | SP-230068 | 3774 | 1 | B | KI#3, NEF exposure for handling PDU Session Type change and managing temporal invalidity/validity condition for a group of UEs | 18.1.0 |
| 2023-03 | SP-99 | SP-230081 | 3777 | 1 | B | Spending Limits for AM Policies in the 5GC | 18.1.0 |
| 2023-03 | SP-99 | SP-230054 | 3780 | 4 | B | External parameter provisioning enhancements for AI/ML-based services | 18.1.0 |
| 2023-03 | SP-99 | SP-230056 | 3784 | 1 | B | Introduction of the MPQUIC Steering Functionality | 18.1.0 |
| 2023-03 | SP-99 | SP-230054 | 3786 | 4 | B | NEF monitoring events to assist application AI/ML operation | 18.1.0 |
| 2023-03 | SP-99 | SP-230052 | 3788 | 1 | F | Update for controlling time synchronization service based on Subscription | 18.1.0 |
| 2023-03 | SP-99 | SP-230058 | 3789 | 8 | B | NEF and UDR service update to support for DNAI mapping | 18.1.0 |
| 2023-03 | SP-99 | SP-230046 | 3790 | - | F | Update AMF service operation to support UE user plane connection to and LCS Client or AF | 18.1.0 |
| 2023-03 | SP-99 | SP-230046 | 3791 | - | F | Update AMF service operation to support UE unaware indication | 18.1.0 |
| 2023-03 | SP-99 | SP-230058 | 3792 | 4 | B | KI#4 23.502 AF traffic influence for common EAS, DNAI selection | 18.1.0 |
| 2023-03 | SP-99 | SP-230054 | 3795 | 4 | B | Support of Group QoS request | 18.1.0 |
| 2023-03 | SP-99 | SP-230055 | 3799 | 1 | F | Clarification for the need of RFSP Index in Use Validity Time in Namf_Communication_UEContextTransfer service operation | 18.1.0 |
| 2023-03 | SP-99 | SP-230065 | 3807 | 1 | B | UE policy association handling from EPS to 5GS | 18.1.0 |
| 2023-03 | SP-99 | SP-230058 | 3808 | 1 | B | ECS Address Configuration Information delivery in roaming | 18.1.0 |
| 2023-03 | SP-99 | SP-230077 | 3810 | 1 | B | Update of Information flow for UPF event exposure service to NWDAF for any UE | 18.1.0 |
| 2023-03 | SP-99 | SP-230056 | 3816 | 1 | B | Introducing Redundant Steering Mode | 18.1.0 |
| 2023-03 | SP-99 | SP-230080 | 3822 | 1 | F | UE Triggered Connection Resume in RRC Inactive procedure alignment with RAN | 18.1.0 |
| 2023-03 | SP-99 | SP-230058 | 3828 | - | C | Edge relocation with common DNAI | 18.1.0 |
| 2023-03 | SP-99 | SP-230050 | 3829 | - | F | Correction on AMF Reporting Satellite Category to PCF | 18.1.0 |
| 2023-03 | SP-99 | SP-230058 | 3831 | - | B | Common EAS/DNAI selection by AF | 18.1.0 |
| 2023-03 | SP-99 | SP-230080 | 3833 | 1 | F | Alignment with stage 3 on handling of UDM deregistration of SMF | 18.1.0 |
| 2023-03 | SP-99 | SP-230071 | 3837 | - | B | Enhancements to NRF servives to support DCSF discovery and selection | 18.1.0 |
| 2023-03 | SP-99 | SP-230080 | 3838 | 1 | F | Generalization of QoS monitoring control description | 18.1.0 |
| 2023-03 | SP-99 | SP-230052 | 3841 | 5 | B | Clarification on registration area impacted by the requested or subscribed coverage area. | 18.1.0 |
| 2023-03 | SP-99 | SP-230063 | 3844 | 3 | B | support for SoR enhancement for enabling automatic selection of SNPN as hosting network | 18.1.0 |
| 2023-03 | SP-99 | SP-230062 | 3847 | 3 | B | Support for ML Model Interoperability Indicator - Resolve EN | 18.1.0 |
| 2023-03 | SP-99 | SP-230046 | 3851 | - | F | Adding LMF ID in Namf_Location_ProvidePositioningInfo | 18.1.0 |
| 2023-03 | SP-99 | SP-230068 | 3853 | 1 | B | KI#1: Support the enhancement of group attribute management | 18.1.0 |
| 2023-03 | SP-99 | SP-230052 | 3856 | 4 | F | Clarification for Controlling time synchronization service based on the Subscription | 18.1.0 |
| 2023-03 | SP-99 | SP-230062 | 3864 | - | C | Managing of Event Muting Impact on NFp | 18.1.0 |
| 2023-03 | SP-99 | SP-230078 | 3866 | 1 | B | CAG enhancement for UE access control via MBSR | 18.1.0 |
| 2023-03 | SP-99 | SP-230040 | 3870 | 1 | A | Clarification on Number of PDU session slice availability check | 18.1.0 |
| 2023-03 | SP-99 | SP-230065 | 3871 | 3 | B | URSP rule enforcement report to 5GC | 18.1.0 |
| 2023-03 | SP-99 | SP-230063 | 3877 | - | B | Support of N5CW device accessing SNPN with credentials owned by Credentials Holder | 18.1.0 |
| 2023-03 | SP-99 | SP-230063 | 3878 | - | B | Clarification of SNPN access mode for non-3GPP access | 18.1.0 |
| 2023-03 | SP-99 | SP-230054 | 3893 | 3 | B | AIMLsys - QoS filtering criteria in assistance to UE member selection | 18.1.0 |
| 2023-03 | SP-99 | SP-230063 | 3894 | - | F | Correcting Equivalent SNPN support | 18.1.0 |
| 2023-03 | SP-99 | SP-230058 | 3904 | 2 | B | Common EAS re-discovery initiated by SMF | 18.1.0 |
| 2023-03 | SP-99 | SP-230054 | 3905 | 2 | B | AIMLsys: KI#7 - Adding member selection filtering criteria | 18.1.0 |
| 2023-03 | SP-99 | SP-230058 | 3909 | 2 | B | AF influence on traffic routing via interacting with VPLMN | 18.1.0 |
| 2023-03 | SP-99 | SP-230065 | 3913 | 2 | B | Service Parameters update for URSP in VPLMN | 18.1.0 |
| 2023-03 | SP-99 | SP-230059 | 3914 | 2 | B | Edge relocation with common DNAI | 18.1.0 |
| 2023-03 | SP-99 | SP-230054 | 3915 | 2 | B | AIMLsys: KI#7 - UE latency performance filtering criterion supported by the NEF | 18.1.0 |
| 2023-03 | SP-99 | SP-230054 | 3916 | 2 | B | AIMLsys: KI#7 - UE location related filtering criteria supported by the NEF | 18.1.0 |
| 2023-03 | SP-99 | SP-230073 | 3917 | 1 | B | Non-3GPP QoS and delay budget - 23.502 | 18.1.0 |
| 2023-03 | SP-99 | SP-230081 | 3919 | 3 | B | Event exposure for bulk subscription from the PCF to the AF in TS 23.502 | 18.1.0 |
| 2023-03 | SP-99 | SP-230076 | 3924 | 1 | B | A2X subscription data in UDM and UDR | 18.1.0 |
| 2023-03 | SP-99 | SP-230076 | 3925 | - | B | PCF A2X capability indication during NF registration and discovery to NRF | 18.1.0 |
| 2023-03 | SP-99 | SP-230063 | 3926 | 1 | B | Changes to subscription data in UDM and UE context in AMF to support Allowed CAG list enhancement | 18.1.0 |
| 2023-03 | SP-99 | SP-230054 | 3931 | 3 | B | Procedure for direct member selection assistance to AF | 18.1.0 |
| 2023-04 | SP-99 | - | - | - | - | MCC Correction of clause numbering (4.15.4.6.3 -&gt; 4.15.4.5.3) | 18.1.1 |
| 2023-06 | SP-100 | SP-230490 | 3601 | 2 | F | Support for 5QI Priority Level in QoS constraints | 18.2.0 |
| 2023-06 | SP-100 | SP-230480 | 3678 | 3 | A | Handling of radio capabilities across TN (in 5GS) and NTN IoT (in EPS) | 18.2.0 |
| 2023-06 | SP-100 | SP-230496 | 3686 | 5 | B | Mobile IAB authorization | 18.2.0 |
| 2023-06 | SP-100 | SP-230498 | 3718 | 3 | B | Update TS23.502 to reflect conclusion of KI#3 for XRM in TR23.700-60 for the API based congestion exposure option | 18.2.0 |
| 2023-06 | SP-100 | SP-230495 | 3726 | 2 | B | UPF event exposure service to NWDAF for AOI in TS 23.502 | 18.2.0 |
| 2023-06 | SP-100 | SP-230498 | 3729 | 3 | B | AF Session procedure update to support 5GS Packet Delay Variation monitoring | 18.2.0 |
| 2023-06 | SP-100 | SP-230469 | 3743 | 2 | B | NRF service enhancements for Analytics Accuracy Monitoring | 18.2.0 |
| 2023-06 | SP-100 | SP-230473 | 3769 | 4 | B | Enhancement of NSAC for roaming case | 18.2.0 |
| 2023-06 | SP-100 | SP-230466 | 3794 | 1 | A | NEF service used in correlating UE data collection and NWDAF request | 18.2.0 |
| 2023-06 | SP-100 | SP-230451 | 3823 | 7 | B | Procedures for support of discontinuous coverage | 18.2.0 |
| 2023-06 | SP-100 | SP-230473 | 3825 | 8 | B | Introduction of Alternative S-NSSAI replacement determined by NSSF | 18.2.0 |
| 2023-06 | SP-100 | SP-230473 | 3848 | 3 | B | Support of reduced network slice availability | 18.2.0 |
| 2023-06 | SP-100 | SP-230473 | 3849 | 6 | B | Support of partly rejected/allowed S-NSSAIs | 18.2.0 |
| 2023-06 | SP-100 | SP-230473 | 3857 | 3 | B | Alternative S-NSSAI provision to the UE | 18.2.0 |
| 2023-06 | SP-100 | SP-230455 | 3875 | 1 | A | Clarification on roaming scenario of N5CW device | 18.2.0 |
| 2023-06 | SP-100 | SP-230484 | 3881 | 4 | B | PDU session control related PIN service support | 18.2.0 |
| 2023-06 | SP-100 | SP-230469 | 3883 | 2 | B | TS 23.502 enhancements for federated learning. | 18.2.0 |
| 2023-06 | SP-100 | SP-230469 | 3885 | 1 | B | Roaming capability in NWDAF registration and discovery services | 18.2.0 |
| 2023-06 | SP-100 | SP-230482 | 3895 | 2 | B | KI4 Enhancements to NRF services to support IMS-MRF registration and discovery | 18.2.0 |
| 2023-06 | SP-100 | SP-230469 | 3903 | 2 | B | KI#1: Update of Nnef_AnalyticsExposure service | 18.2.0 |
| 2023-06 | SP-100 | SP-230482 | 3906 | 2 | B | Enhancements to NRF services to support DCMF discovery and selection | 18.2.0 |
| 2023-06 | SP-100 | SP-230475 | 3918 | 5 | B | Event exposure enhancement for enhanced NSACF architecture | 18.2.0 |
| 2023-06 | SP-100 | SP-230474 | 3930 | 2 | B | Hierarchical NSACF architecture procedures | 18.2.0 |
| 2023-06 | SP-100 | SP-230483 | 3944 | 5 | C | Co-existence of Small Data Transmission and CN based MT communication handling for UE in RRC_INACTIVE | 18.2.0 |
| 2023-06 | SP-100 | SP-230474 | 3946 | 1 | B | KI#4: Support for Centralized NSACF in multi-service PLMN in non-roaming cases. | 18.2.0 |
| 2023-06 | SP-100 | SP-230489 | 3950 | 1 | A | Correction to procedures for AF-triggered dynamically changing AM policies | 18.2.0 |
| 2023-06 | SP-100 | SP-230491 | 3948 | 1 | B | Dynamically changing AM policies for inbound roamers using LBO | 18.2.0 |
| 2023-06 | SP-100 | SP-230476 | 3952 | 7 | B | KI#3 - 5GS to EPS mobility | 18.2.0 |
| 2023-06 | SP-100 | SP-230457 | 3953 | 4 | F | AIMLsys - QoS filtering criteria corrections | 18.2.0 |
| 2023-06 | SP-100 | SP-230457 | 3954 | 7 | B | Solving ENs in the Procedures for Consolidated-MBR Monitoring | 18.2.0 |
| 2023-06 | SP-100 | SP-230458 | 3955 | 1 | B | Update to external parameter provisioning for expected UE behaviour | 18.2.0 |
| 2023-06 | SP-100 | SP-230476 | 3959 | 4 | B | Forwarding of UE reporting of URSP rule enforcement between SM-PCF and UE-PCF | 18.2.0 |
| 2023-06 | SP-100 | SP-230495 | 3962 | 1 | C | Updates to UPF Event Exposure | 18.2.0 |
| 2023-06 | SP-100 | SP-230459 | 3963 | 1 | C | Updates to non-3GPP access path switching | 18.2.0 |
| 2023-06 | SP-100 | SP-230478 | 3965 | 4 | C | Addressing Editor's note related to AF requested QoS for a group of UEs | 18.2.0 |
| 2023-06 | SP-100 | SP-230450 | 3970 | 1 | F | KI#5: Update related to EN resolution in TS 23.304 for term of multi-path via Uu and via U2N Relay | 18.2.0 |
| 2023-06 | SP-100 | SP-230476 | 3979 | 3 | B | Support URSP provisioning in EPS | 18.2.0 |
| 2023-06 | SP-100 | SP-230476 | 3980 | 3 | D | Clarification on URSP rule enforcement | 18.2.0 |
| 2023-06 | SP-100 | SP-230458 | 3981 | 4 | F | R18 AIMLsys_KI1_23502 CR_SingleSO_for_QoS | 18.2.0 |
| 2023-06 | SP-100 | SP-230458 | 3982 | 4 | B | R18 AIMLsys_KI4_23502 CR for clarification on parameter provisioning | 18.2.0 |
| 2023-06 | SP-100 | SP-230476 | 3985 | 1 | C | UE capability for supporting applying PSIs in a specific PLMN | 18.2.0 |
| 2023-06 | SP-100 | SP-230458 | 3986 | 3 | B | Updates to assistance for UE member selection | 18.2.0 |
| 2023-06 | SP-100 | SP-230458 | 3987 | - | B | E2E data volume transfer time information event ID of AF | 18.2.0 |
| 2023-06 | SP-100 | SP-230498 | 3989 | 9 | B | Procedure to acquire jitter information | 18.2.0 |
| 2023-06 | SP-100 | SP-230461 | 3990 | 1 | F | Selection of Common DNAI | 18.2.0 |
| 2023-06 | SP-100 | SP-230488 | 3992 | - | A | On correcting the clause number in SMS over NAS procedure | 18.2.0 |
| 2023-06 | SP-100 | SP-230487 | 3997 | 2 | A | SMS memory available | 18.2.0 |
| 2023-06 | SP-100 | SP-230498 | 3999 | 1 | B | PDU Set information provisioning | 18.2.0 |
| 2023-06 | SP-100 | SP-230469 | 4003 | 1 | B | Variable periodicity in event reporting | 18.2.0 |
| 2023-06 | SP-100 | SP-230483 | 4007 | 6 | B | Support of Paging Policy Differentiation for CN based MT communication handling | 18.2.0 |
| 2023-06 | SP-100 | SP-230478 | 4008 | 1 | F | KI#1 Solve the EN about 5G VN group data parameter | 18.2.0 |
| 2023-06 | SP-100 | SP-230478 | 4009 | 1 | C | KI#1 Address EN for LADN aspects for SMF | 18.2.0 |
| 2023-06 | SP-100 | SP-230469 | 4013 | 2 | B | Update to Enhance NRF services for DCCF relocation in TS 23.502 | 18.2.0 |
| 2023-06 | SP-100 | SP-230456 | 4015 | 7 | B | AMF/PCF interactions to support TNGF/N3IWF selection enhancement for support of S-NSSAI needed by UE | 18.2.0 |
| 2023-06 | SP-100 | SP-230471 | 4017 | 1 | B | CH controlled list of preferred SNPNs and GINs for access for localized services in SNPN | 18.2.0 |
| 2023-06 | SP-100 | SP-230496 | 4018 | 1 | F | Correction on CAG information in UE subscription and UE context | 18.2.0 |
| 2023-06 | SP-100 | SP-230471 | 4019 | 1 | B | Support for N5CW device using decorated NAI | 18.2.0 |
| 2023-06 | SP-100 | SP-230471 | 4020 | 1 | B | Support for onboarding via untrusted non-3GPP access | 18.2.0 |
| 2023-06 | SP-100 | SP-230456 | 4022 | 1 | B | 5G-RG ID provided in Trusted Non-3GPP access procedure | 18.2.0 |
| 2023-06 | SP-100 | SP-230485 | 4023 | - | B | Ranging Sidelink Positioning Subscription data | 18.2.0 |
| 2023-06 | SP-100 | SP-230474 | 4024 | 4 | B | Change of Network Slice instance for PDU sessions | 18.2.0 |
| 2023-06 | SP-100 | SP-230488 | 4029 | 1 | A | PCRT during EPS interworking | 18.2.0 |
| 2023-06 | SP-100 | SP-230458 | 4031 | 5 | B | Service Experience filtering criteria in assistance to UE member selection | 18.2.0 |
| 2023-06 | SP-100 | SP-230459 | 4033 | - | F | Clarification on old access release during non-3GPP switching | 18.2.0 |
| 2023-06 | SP-100 | SP-230471 | 4034 | 1 | C | Modification of AN release condition due to update of Allowed CAG list | 18.2.0 |
| 2023-06 | SP-100 | SP-230478 | 4037 | 1 | B | Add the DNN and S-NSSAI specific Group Parameters in related group data | 18.2.0 |
| 2023-06 | SP-100 | SP-230458 | 4039 | 1 | B | AIMLsys: KI#7 - Adding maximum number of UEs as a member selection filtering criterion | 18.2.0 |
| 2023-06 | SP-100 | SP-230458 | 4040 | 4 | B | AIMLsys: KI#7 - additional information provided by NEF | 18.2.0 |
| 2023-06 | SP-100 | SP-230498 | 4041 | 1 | B | Signalling procedures to support ECN marking for L4S. | 18.2.0 |
| 2023-06 | SP-100 | SP-230458 | 4042 | 3 | B | Update to UE Member Filtering Criteria | 18.2.0 |
| 2023-06 | SP-100 | SP-230452 | 4044 | 1 | F | Correction on Satellite Backhaul Category clause info | 18.2.0 |
| 2023-06 | SP-100 | SP-230498 | 4045 | 1 | B | Procedures update to support policy control enhancements for multi-modal flows | 18.2.0 |
| 2023-06 | SP-100 | SP-230461 | 4046 | 1 | C | Update on SMF/UPF selection based on common DNAI | 18.2.0 |
| 2023-06 | SP-100 | SP-230478 | 4048 | - | F | Clarification on Nnef_ParameterProvision service operation | 18.2.0 |
| 2023-06 | SP-100 | SP-230476 | 4051 | 3 | B | Principle of PCC rule generation based on URSP rule and URSP rule enforcement delivery procedure. | 18.2.0 |
| 2023-06 | SP-100 | SP-230461 | 4053 | 1 | B | Authorization of AF traffic influence in roaming | 18.2.0 |
| 2023-06 | SP-100 | SP-230495 | 4054 | - | B | Add NWDAF as consumer of DNAI Mapping service | 18.2.0 |
| 2023-06 | SP-100 | SP-230458 | 4057 | 1 | B | PDTQ policy renegotiation, PDTQ storage and parameter enhancement in PDTQ create request | 18.2.0 |
| 2023-06 | SP-100 | SP-230474 | 4059 | 1 | B | Support of determining alternative S-NSSAI | 18.2.0 |
| 2023-06 | SP-100 | SP-230461 | 4060 | 4 | B | KI#1 PCF and SMF service enhancement to support HR-SBO | 18.2.0 |
| 2023-06 | SP-100 | SP-230461 | 4061 | 1 | B | KI#1 Update on AF influence via VPLMN | 18.2.0 |
| 2023-06 | SP-100 | SP-230461 | 4062 | 1 | B | KI#1 EACI provisioning from VPLMN | 18.2.0 |
| 2023-06 | SP-100 | SP-230474 | 4064 | 3 | C | Update of the reasons to invoke the CN-initiated selective deactivation of UP connection of an existing PDU Session. | 18.2.0 |
| 2023-06 | SP-100 | SP-230474 | 4067 | 1 | B | Support of slice replacement for new PDU Sessions | 18.2.0 |
| 2023-06 | SP-100 | SP-230450 | 4070 | 3 | F | U2U relay subscription | 18.2.0 |
| 2023-06 | SP-100 | SP-230452 | 4071 | 1 | B | Update SMF events exposure service to support dynamic satellite backhaul | 18.2.0 |
| 2023-06 | SP-100 | SP-230486 | 4078 | 1 | F | Corrections and alignments of SFC terminology | 18.2.0 |
| 2023-06 | SP-100 | SP-230446 | 4080 | - | F | Update of the Namf_Communication_N1MessageNotify service operation | 18.2.0 |
| 2023-06 | SP-100 | SP-230458 | 4084 | 5 | F | Update the procedures for PDTQ policy | 18.2.0 |
| 2023-06 | SP-100 | SP-230469 | 4085 | 1 | B | Update the user consent for UDM and UDR services | 18.2.0 |
| 2023-06 | SP-100 | SP-230459 | 4087 | 1 | B | Clarifications on Network initiated service request procedure | 18.2.0 |
| 2023-06 | SP-100 | SP-230496 | 4099 | 3 | B | Providing user location information of MBSR to the AMF | 18.2.0 |
| 2023-06 | SP-100 | SP-230495 | 4104 | 1 | B | Clarifications to UPF event exposure service for TSC management | 18.2.0 |
| 2023-06 | SP-100 | SP-230455 | 4108 | 1 | F | User location when 5G-RG is a TNAP | 18.2.0 |
| 2023-06 | SP-100 | SP-230461 | 4110 | 7 | C | Corrections on handling the AF traffic influencing request for HR-SBO PDU Sessions | 18.2.0 |
| 2023-06 | SP-100 | SP-230481 | 4111 | 1 | F | MPS when access to 5GC is WLAN corrections | 18.2.0 |
| 2023-06 | SP-100 | SP-230474 | 4113 | 1 | B | Support of network slice replacement for non roaming case | 18.2.0 |
| 2023-06 | SP-100 | SP-230493 | 4118 | 1 | F | Modification to the UE time synchronization subscription | 18.2.0 |
| 2023-06 | SP-100 | SP-230498 | 4121 | 1 | C | Procedures update to support QoS monitoring for the correlated multi-modal flows | 18.2.0 |
| 2023-06 | SP-100 | SP-230495 | 4124 | 1 | C | Improving AF specific UE ID retrieval | 18.2.0 |
| 2023-06 | SP-100 | SP-230447 | 4126 | 1 | A | Reinstating definition of Nnrf_NFManagement_NFStatusUnsubscribe service operation | 18.2.0 |
| 2023-06 | SP-100 | SP-230493 | 4130 | 10 | C | Revision on the procedures to support network timing synchronization status and reporting | 18.2.0 |
| 2023-06 | SP-100 | SP-230452 | 4137 | 1 | B | Update to support reporting of satellite backhaul category change | 18.2.0 |
| 2023-06 | SP-100 | SP-230459 | 4138 | 1 | B | Update SMF Service Operations for indication of non-3GPP path switching | 18.2.0 |
| 2023-06 | SP-100 | SP-230464 | 4144 | 1 | A | Fixing an Incorrect Reference in the Application guidance for URSP determination Section | 18.2.0 |
| 2023-06 | SP-100 | SP-230454 | 4148 | 1 | B | MBS assistance information in UDM | 18.2.0 |
| 2023-06 | SP-100 | SP-230458 | 4157 | 1 | F | 23.502 - Member UE terminology update | 18.2.0 |
| 2023-06 | SP-100 | SP-230461 | 4160 | 3 | B | Common EAS/DNAI determination for a set of UEs | 18.2.0 |
| 2023-06 | SP-100 | SP-230461 | 4161 | - | B | NEF and UDR service update for geographic are to support for DNAI mapping | 18.2.0 |
| 2023-06 | SP-100 | SP-230458 | 4163 | 3 | B | NEF MemberUESelectionAssistance_Notify input extension | 18.2.0 |
| 2023-06 | SP-100 | SP-230469 | 4172 | 2 | C | Clarification of ADRF registration and discovery | 18.2.0 |
| 2023-06 | SP-100 | SP-230458 | 4174 | 3 | B | NEF discovery for multi NEF capability | 18.2.0 |
| 2023-06 | SP-100 | SP-230458 | 4176 | 2 | B | Procedures for Multi-member AF Session Revoke | 18.2.0 |
| 2023-06 | SP-100 | SP-230493 | 4177 | 1 | F | Update the references to the new IEEE Std 802.1Q-2022, in regards to KI#5 | 18.2.0 |
| 2023-06 | SP-100 | SP-230495 | 4180 | - | B | DCCF/MFAF may use Nupf_EventExposure | 18.2.0 |
| 2023-06 | SP-100 | SP-230483 | 4182 | 2 | F | NGAP message clarification | 18.2.0 |
| 2023-06 | SP-100 | SP-230476 | 4185 | - | B | Addition of Indication of UE reporting URSP rule enforcement as a condition to report URSP rule enforcement | 18.2.0 |
| 2023-06 | SP-100 | SP-230458 | 4186 | 2 | B | R18 AIMLsys_KI6_23502 CR for adding timing info for AF QoS | 18.2.0 |
| 2023-06 | SP-100 | SP-230484 | 4189 | 2 | C | Clarifying SMF behaviour for non-3GPP delay budget and non-3GPP QoS Assistance Information | 18.2.0 |
| 2023-06 | SP-100 | SP-230474 | 4193 | 2 | B | Improved network control of a network slice - without roaming | 18.2.0 |
| 2023-06 | SP-100 | SP-230458 | 4194 | 2 | B | AIMLsys: KI#5 - Applying PDTQ Policy | 18.2.0 |
| 2023-06 | SP-100 | SP-230484 | 4196 | 1 | B | PIN solution description in informative Annex | 18.2.0 |
| 2023-06 | SP-100 | SP-230458 | 4204 | 2 | B | Update the Member-UE selection criteria | 18.2.0 |
| 2023-06 | SP-100 | SP-230461 | 4210 | 1 | B | Add Parameters in SM Context for EAS re-discovery | 18.2.0 |
| 2023-06 | SP-100 | SP-230458 | 4212 | 2 | B | Updates to filtering criteria for UE member selection | 18.2.0 |
| 2023-06 | SP-100 | SP-230474 | 4214 | 2 | B | Support EPS counting for Hierarchial NSAC and Centralized NSAC Architecture | 18.2.0 |
| 2023-06 | SP-100 | SP-230462 | 4215 | 1 | F | Update on Nnef_DNAIMapping service | 18.2.0 |
| 2023-06 | SP-100 | SP-230458 | 4217 | - | F | ENs removal for UE Member Filtering Criteria for 5GS assistance to UE member selection in TS 23.502 | 18.2.0 |
| 2023-06 | SP-100 | SP-230474 | 4219 | 1 | B | Network Slice Replacement in roaming | 18.2.0 |
| 2023-06 | SP-100 | SP-230475 | 4222 | 3 | B | Introduction of the Support of Counting of UEs with at least one PDU sessions in the 5GS option 1 | 18.2.0 |
| 2023-06 | SP-100 | SP-230476 | 4223 | 3 | C | Update to the Reporting the Outcome of the UE Policies Provisioning procedure to account for VPLMN Specific URSP Rules | 18.2.0 |
| 2023-06 | SP-100 | SP-230474 | 4227 | 2 | B | Support of network slice replacement for roaming case | 18.2.0 |
| 2023-06 | SP-100 | SP-230493 | 4234 | 2 | B | Clarification on the AMF and NEF subscribe and notification | 18.2.0 |
| 2023-06 | SP-100 | SP-230446 | 4236 | - | B | Indoor/Outdoor Sync in AMF LCS Interface | 18.2.0 |
| 2023-06 | SP-100 | SP-230484 | 4238 | 2 | B | Update the PCF for generating URSP rules for PIN service | 18.2.0 |
| 2023-06 | SP-100 | SP-230476 | 4239 | 2 | B | Including in PCO the URSP capability in EPS during idle mobility with no N26 support | 18.2.0 |
| 2023-09 | SP-101 | SP-230836 | 4077 | 3 | A | Clarification of invocation of TSCTSF | 18.3.0 |
| 2023-09 | SP-101 | SP-230841 | 4246 | 2 | F | Time based handover for NTN NR | 18.3.0 |
| 2023-09 | SP-101 | SP-230838 | 4250 | 1 | A | Update of subscribed NSSAI when UE is not registered in network | 18.3.0 |
| 2023-09 | SP-101 | SP-230844 | 4251 | 1 | F | Updates to AI/ML procedures | 18.3.0 |
| 2023-09 | SP-101 | SP-230847 | 4256 | 2 | F | Correct PFD management based on PFD Determination analytics | 18.3.0 |
| 2023-09 | SP-101 | SP-230838 | 4266 | 1 | A | UE Policy Association(s) for 3GPP and non-3GPP accesses | 18.3.0 |
| 2023-09 | SP-101 | SP-230851 | 4271 | 2 | F | Provision VPLMN specific URSP rules | 18.3.0 |
| 2023-09 | SP-101 | SP-230846 | 4283 | 3 | F | NEF determination of the HR-SBO condition when receiving an AF request targeting an individual UE address | 18.3.0 |
| 2023-09 | SP-101 | SP-230858 | 4284 | 5 | F | Support of ECN Marking Indication for L4S | 18.3.0 |
| 2023-09 | SP-101 | SP-230856 | 4286 | 2 | F | Updates on the procedures for the support of network timng synchronization status and reporting | 18.3.0 |
| 2023-09 | SP-101 | SP-230844 | 4292 | 2 | F | Support for confidence and/or accuracy level associated with Application-Specific Expected UE Behaviour | 18.3.0 |
| 2023-09 | SP-101 | SP-230859 | 4300 | 1 | F | General corrections and alignment for TS23.502 | 18.3.0 |
| 2023-09 | SP-101 | SP-230850 | 4303 | 3 | F | Handling UE number with at least one PDU Session under Hierarchical NSAC architecture | 18.3.0 |
| 2023-09 | SP-101 | SP-230844 | 4312 | 1 | F | Corrections to external parameter provisioning by AI/ML application | 18.3.0 |
| 2023-09 | SP-101 | SP-230845 | 4314 | 1 | F | Meaning of availability for 3GPP access | 18.3.0 |
| 2023-09 | SP-101 | SP-230851 | 4315 | 1 | F | Alignment of 23.502 with regards to LBO information exchange between AMF and PCF | 18.3.0 |
| 2023-09 | SP-101 | SP-230860 | 4317 | 1 | F | Correction on SLAMUP procedure | 18.3.0 |
| 2023-09 | SP-101 | SP-230846 | 4319 | 1 | F | Service correction related to traffic correlation | 18.3.0 |
| 2023-09 | SP-101 | SP-230843 | 4321 | 2 | F | Alignment with stage 3 on Parameter Provisioning of MBS Assistance Information | 18.3.0 |
| 2023-09 | SP-101 | SP-230853 | 4322 | 1 | F | Provision of eDRX for RRC_INACTIVE with PTW | 18.3.0 |
| 2023-09 | SP-101 | SP-230859 | 4324 | 2 | F | SMF service operations for SR procedure in Suspend mode | 18.3.0 |
| 2023-09 | SP-101 | SP-230860 | 4325 | 1 | F | Correction of EAP-based secondary authentication in EPC | 18.3.0 |
| 2023-09 | SP-101 | SP-230858 | 4335 | 3 | F | Correction of PDU Set QoS parameters and Protocol Description | 18.3.0 |
| 2023-09 | SP-101 | SP-230859 | 4344 | 2 | F | Clarification on network initiated Service Request procedure for MA PDU Session | 18.3.0 |
| 2023-09 | SP-101 | SP-230845 | 4346 | - | F | Removing UE capability report on non-3GPP access leg over EPC | 18.3.0 |
| 2023-09 | SP-101 | SP-230845 | 4347 | 1 | F | Removal of non-3GPP path switching capability between V-SMF and H-SMF | 18.3.0 |
| 2023-09 | SP-101 | SP-230845 | 4348 | - | F | Clarification on status of PDU Sessions that are not requested to be moved to the new non-3GPP access | 18.3.0 |
| 2023-09 | SP-101 | SP-230845 | 4353 | 1 | F | Clarification on the N3GPP path switching | 18.3.0 |
| 2023-09 | SP-101 | SP-230847 | 4357 | 1 | F | Clarification on the SMF event exposure and muting enhancements | 18.3.0 |
| 2023-09 | SP-101 | SP-230844 | 4361 | 3 | F | Clarifications for procedures and services related to Multi-member AF session | 18.3.0 |
| 2023-09 | SP-101 | SP-230856 | 4365 | 2 | F | Clarification on the time synchronization status reporting related procedure | 18.3.0 |
| 2023-09 | SP-101 | SP-230856 | 4366 | 1 | F | Clarification on time synchronization service based on the subscription | 18.3.0 |
| 2023-09 | SP-101 | SP-230844 | 4367 | - | F | Correction the UPF service operation | 18.3.0 |
| 2023-09 | SP-101 | SP-230844 | 4373 | 2 | F | Proposed definition for Multi-member AF Session With QoS | 18.3.0 |
| 2023-09 | SP-101 | SP-230858 | 4380 | 4 | F | Non-homogeneous support of PDU set handling in NG-RAN | 18.3.0 |
| 2023-09 | SP-101 | SP-230832 | 4391 | 4 | A | Clarification on subscription for ProSe roles | 18.3.0 |
| 2023-09 | SP-101 | SP-230841 | 4393 | 3 | F | Procedure alignment to 23.501 for supporting discontinuous coverage | 18.3.0 |
| 2023-09 | SP-101 | SP-230845 | 4394 | 2 | F | Clarification on MA PDU session operation | 18.3.0 |
| 2023-09 | SP-101 | SP-230856 | 4397 | 2 | F | Updates on timing synchronization status reporting | 18.3.0 |
| 2023-09 | SP-101 | SP-230852 | 4399 | 2 | F | Clarification of IP address and IP range used for MF registration and discovery | 18.3.0 |
| 2023-09 | SP-101 | SP-230859 | 4400 | 1 | F | Nudr parameter correction | 18.3.0 |
| 2023-09 | SP-101 | SP-230829 | 4412 | 2 | A | AF influence data key correction | 18.3.0 |
| 2023-09 | SP-101 | SP-230847 | 4415 | 1 | F | Clarification on the capability of NWDAF and ADRF in NRF service operation in TS 23.502 | 18.3.0 |
| 2023-09 | SP-101 | SP-230859 | 4418 | 2 | F | NSAC back-off timer correction | 18.3.0 |
| 2023-09 | SP-101 | SP-230856 | 4422 | 3 | F | Modification to AMF and TSCTSF service operation for time synchronization | 18.3.0 |
| 2023-09 | SP-101 | SP-230856 | 4423 | 3 | F | Update the procedures for time synchronization service monitoring | 18.3.0 |
| 2023-09 | SP-101 | SP-230859 | 4428 | 2 | F | Clarifications for N2 inter-PLMN handover | 18.3.0 |
| 2023-09 | SP-101 | SP-230850 | 4429 | 3 | F | Clarification on NSAC for maximum number of UE with at least one PDU session/PDN connection | 18.3.0 |
| 2023-09 | SP-101 | SP-230853 | 4433 | 3 | F | Small Data Transmission for Redcap UE in RRC inactive with eDRX&gt;10.24s | 18.3.0 |
| 2023-09 | SP-101 | SP-230849 | 4434 | 3 | F | Usage of existing NG-RAN resource of the replaced S-NSSAI | 18.3.0 |
| 2023-09 | SP-101 | SP-230844 | 4441 | 3 | F | Corrections on Planned Data Transfer with QoS (PDTQ) Policy | 18.3.0 |
| 2023-09 | SP-101 | SP-230841 | 4446 | 1 | F | Loss Of Connectivity event reporting to AF | 18.3.0 |
| 2023-12 | SP-102 | SP-231277 | 4181 | 3 | F | Signalling procedures to support policy control enhancements for multi-modal services | 18.4.0 |
| 2023-12 | SP-102 | SP-231276 | 4195 | 3 | F | Providing both ULI and Additional ULI to other NFs | 18.4.0 |
| 2023-12 | SP-102 | SP-231236 | 4255 | 5 | F | Correction to UPF anchored Mobile Terminated Data Transport in Control Plane CIoT 5GS Optimisation | 18.4.0 |
| 2023-12 | SP-102 | SP-231261 | 4262 | 2 | F | KI#4: Clarification on Hierarchical NSACF architecture procedures | 18.4.0 |
| 2023-12 | SP-102 | SP-231263 | 4269 | 3 | F | URSP rule delivery via EPS | 18.4.0 |
| 2023-12 | SP-102 | SP-231768 | 4276 | 4 | F | Clarification of the discovery and selection of NSACF | 18.4.0 |
| 2023-12 | SP-102 | SP-231261 | 4296 | 3 | F | Clarification on the Hierarchical NSACF procedures | 18.4.0 |
| 2023-12 | SP-102 | SP-231269 | 4305 | 2 | F | Complement of service parameters for PIN | 18.4.0 |
| 2023-12 | SP-102 | SP-231269 | 4306 | 3 | F | Handling of service parameters with PIN ID | 18.4.0 |
| 2023-12 | SP-102 | SP-231269 | 4307 | 2 | F | Correction to SMF behaviour for non-3GPP delay budget | 18.4.0 |
| 2023-12 | SP-102 | SP-231253 | 4311 | 4 | F | Corrections on assistance for member UE selection | 18.4.0 |
| 2023-12 | SP-102 | SP-231248 | 4327 | 4 | F | Handling of EPS interworking due to NS-AoS | 18.4.0 |
| 2023-12 | SP-102 | SP-231256 | 4338 | 3 | F | Configuration of ECS address in roaming | 18.4.0 |
| 2023-12 | SP-102 | SP-231254 | 4359 | 3 | F | ATSSS_Secondary re-auth for MAPDU session when one access is in 5GC and other in EPC | 18.4.0 |
| 2023-12 | SP-102 | SP-231277 | 4363 | 3 | F | Clarification on the NEF service operation | 18.4.0 |
| 2023-12 | SP-102 | SP-231261 | 4392 | 5 | F | Clarification for temporary slices having validity time information | 18.4.0 |
| 2023-12 | SP-102 | SP-231261 | 4439 | 2 | F | Partially Allowed NSSAI and S-NSSAIs used at NGAP | 18.4.0 |
| 2023-12 | SP-102 | SP-231248 | 4449 | 2 | F | SMF handling when UE is handed over outside UPF coverage | 18.4.0 |
| 2023-12 | SP-102 | SP-231261 | 4451 | 3 | F | Sending Alternative S-NSSAI to the PCF during PDU Session Establishment | 18.4.0 |
| 2023-12 | SP-102 | SP-231275 | 4454 | 3 | C | Update AF specific UE ID retrieval | 18.4.0 |
| 2023-12 | SP-102 | SP-231241 | 4456 | 3 | A | Missing NEF service input for EACI provisioning | 18.4.0 |
| 2023-12 | SP-102 | SP-231245 | 4463 | - | A | PMIC and UMIC Table Reference | 18.4.0 |
| 2023-12 | SP-102 | SP-231275 | 4464 | 2 | F | Correction to information flow for UPF event exposure service for any UE | 18.4.0 |
| 2023-12 | SP-102 | SP-231276 | 4465 | 2 | F | Update of MBSR authorization | 18.4.0 |
| 2023-12 | SP-102 | SP-231252 | 4466 | 2 | F | Cleaning up the definition of the TNAP ID | 18.4.0 |
| 2023-12 | SP-102 | SP-231275 | 4467 | - | F | Adding Achieved sampling ratio in Nupf_EventExposure_Notify to align to 23.288 | 18.4.0 |
| 2023-12 | SP-102 | SP-231273 | 4477 | 6 | F | AMF discovery and subscription by TSCTSF for Time Synchronization Coverage Area | 18.4.0 |
| 2023-12 | SP-102 | SP-231248 | 4481 | 2 | F | MT SMS handling for UE in power saving | 18.4.0 |
| 2023-12 | SP-102 | SP-231248 | 4483 | - | F | MICO capability synchronization | 18.4.0 |
| 2023-12 | SP-102 | SP-231248 | 4484 | 1 | F | ODB parameters synchronization | 18.4.0 |
| 2023-12 | SP-102 | SP-231239 | 4487 | 2 | A | Miscellaneous corrections in PDU session modification and handover procedures | 18.4.0 |
| 2023-12 | SP-102 | SP-231259 | 4488 | - | F | Clarification on Registration procedure for Onboarding SNPN | 18.4.0 |
| 2023-12 | SP-102 | SP-231253 | 4490 | 5 | F | Clarification for list of UEs parameter handling | 18.4.0 |
| 2023-12 | SP-102 | SP-231258 | 4491 | 2 | F | Add the source of the PFD as the subkey in the UDR. | 18.4.0 |
| 2023-12 | SP-102 | SP-231264 | 4496 | 2 | F | clarify the change of PDU session type in SPP procedure | 18.4.0 |
| 2023-12 | SP-102 | SP-231264 | 4498 | 2 | F | Complete the support for maximum group data rate | 18.4.0 |
| 2023-12 | SP-102 | SP-231248 | 4502 | 2 | F | EPS to 5GS Mobility Registration (Idle and Connected State) using N26 interface | 18.4.0 |
| 2023-12 | SP-102 | SP-231275 | 4504 | 3 | F | Corrections to UPF Services | 18.4.0 |
| 2023-12 | SP-102 | SP-231275 | 4505 | 3 | F | Correction to UPF Data Collection with QoS Monitoring event | 18.4.0 |
| 2023-12 | SP-102 | SP-231277 | 4511 | 5 | F | Clarification on procedures for scenarios to enable/disable PDU Set based handling | 18.4.0 |
| 2023-12 | SP-102 | SP-231258 | 4515 | 2 | F | Correction to Nnrf_NFDiscovery_Request service operation input parameters for NWDAF with FL capability | 18.4.0 |
| 2023-12 | SP-102 | SP-231258 | 4516 | - | F | Add Relative Proximity analytics description to the AF event exposure service. | 18.4.0 |
| 2023-12 | SP-102 | SP-231255 | 4517 | 1 | F | Correction to DetNet specific response from UPF | 18.4.0 |
| 2023-12 | SP-102 | SP-231273 | 4519 | 4 | F | Updates and clarifications related to PDU Session procedures in context to get and set messages for KI#5 | 18.4.0 |
| 2023-12 | SP-102 | SP-231250 | 4520 | 2 | F | Update to support reporting of satellite backhaul category change and GEO Satellite ID change | 18.4.0 |
| 2023-12 | SP-102 | SP-231267 | 4523 | - | F | Correction on UE triggered connection resume call flow | 18.4.0 |
| 2023-12 | SP-102 | SP-231267 | 4524 | 2 | F | Update on support of CN based MT communication handling | 18.4.0 |
| 2023-12 | SP-102 | SP-231264 | 4527 | 2 | F | LADN information in subscription information | 18.4.0 |
| 2023-12 | SP-102 | SP-231258 | 4530 | - | F | Wrong reference number of UPF data collection | 18.4.0 |
| 2023-12 | SP-102 | SP-231275 | 4532 | 2 | F | Resolving unclear description of UPF event exposure service related with AOI | 18.4.0 |
| 2023-12 | SP-102 | SP-231593 | 4539 | 4 | F | Clarification on the Handling of the UE number with at least one PDU Session under Hierarchical NSAC architecture | 18.4.0 |
| 2023-12 | SP-102 | SP-231276 | 4543 | 1 | F | Clarification on deregistration procedure | 18.4.0 |
| 2023-12 | SP-102 | SP-231272 | 4545 | 3 | F | Unavailability Period in Deregistration | 18.4.0 |
| 2023-12 | SP-102 | SP-231263 | 4546 | 5 | F | URSP delivery via EPS | 18.4.0 |
| 2023-12 | SP-102 | SP-231253 | 4550 | 2 | F | Clarification on external parameters updates by AF | 18.4.0 |
| 2023-12 | SP-102 | SP-231253 | 4551 | 1 | F | Clarification on the time window(s) for selecting the candidate UE(s) | 18.4.0 |
| 2023-12 | SP-102 | SP-231263 | 4555 | 1 | F | Adding 'URSP delivery over EPS' capability in PCF profile in NRF (23.502) | 18.4.0 |
| 2023-12 | SP-102 | SP-231261 | 4562 | 2 | F | KI#1: Corrections to Support Alternative Slices. | 18.4.0 |
| 2023-12 | SP-102 | SP-231253 | 4566 | - | F | R18 AIMLsys_KI5_23502_CR for clarification on PDTQ procedures | 18.4.0 |
| 2023-12 | SP-102 | SP-231253 | 4567 | 1 | F | R18 AIMLsys_KI6_23502 CR for timing info in PCF API | 18.4.0 |
| 2023-12 | SP-102 | SP-231269 | 4575 | 2 | F | Clarification on subscribed S-NSSAI and DNN for PIN service | 18.4.0 |
| 2023-12 | SP-102 | SP-231253 | 4579 | 1 | F | Clarification on the procedure for PDTQ warning notification | 18.4.0 |
| 2023-12 | SP-102 | SP-231254 | 4581 | 2 | F | Adding QoS Support for MA PDU with N3GPP access connected to EPC and 3GPP access connected to 5GC | 18.4.0 |
| 2023-12 | SP-102 | SP-231254 | 4582 | 2 | F | Correction on MA PDU with N3GPP access via EPC and 3GPP access via 5GC | 18.4.0 |
| 2023-12 | SP-102 | SP-231248 | 4585 | 1 | F | Clarification on NAS IP ADDRESS for untursted non-3GPP access | 18.4.0 |
| 2023-12 | SP-102 | SP-231253 | 4588 | 2 | F | Correction of Application-Specific external parameter provisioning services | 18.4.0 |
| 2023-12 | SP-102 | SP-231273 | 4600 | 1 | F | Reinstating Namf_Communication_NonUeN2MessageTransfer for TSS reporting | 18.4.0 |
| 2023-12 | SP-102 | SP-231239 | 4603 | 1 | A | Requesting Configured NSSAI from NSSF | 18.4.0 |
| 2023-12 | SP-102 | SP-231263 | 4604 | 2 | F | Selection of the PDN connection to use for the delivery of URSP updates in EPS | 18.4.0 |
| 2023-12 | SP-102 | SP-231263 | 4605 | 3 | F | Corrections for URSP provisioning in EPS | 18.4.0 |
| 2023-12 | SP-102 | SP-231249 | 4617 | - | F | Corrections to Registration Procedure for Discontinous coverage | 18.4.0 |
| 2023-12 | SP-102 | SP-231253 | 4618 | - | F | Clarification for Access Type and/or RAT Type of PDU Session filtering criteria | 18.4.0 |
| 2023-12 | SP-102 | SP-231764 | 4622 | 4 | F | Clarification on Access type for NSAC for maximum number of UE with at least one PDU session/PDN connection | 18.4.0 |
| 2023-12 | SP-102 | SP-231248 | 4623 | 5 | B | Adding DL data size in DL Notification message | 18.4.0 |
| 2023-12 | SP-102 | SP-231261 | 4626 | 2 | F | Validity information awareness at AMF | 18.4.0 |
| 2023-12 | SP-102 | SP-231249 | 4629 | 1 | F | Update on support of discontinuous coverage for satellite access | 18.4.0 |
| 2023-12 | SP-102 | SP-231253 | 4632 | - | F | Addition of UE IP address to Nnef_MemberUESelectionAssistance service | 18.4.0 |
| 2023-12 | SP-102 | SP-231261 | 4638 | 1 | F | Update of definition of NSAC Service area. | 18.4.0 |
| 2023-12 | SP-102 | SP-231253 | 4646 | 2 | F | Clarification on flow description information for multi-member AF session | 18.4.0 |
| 2023-12 | SP-102 | SP-231253 | 4647 | 2 | F | Clarification on multi-member AF session with required QoS | 18.4.0 |
| 2023-12 | SP-102 | SP-231253 | 4654 | 3 | F | Clarification of AF requested update Member UE filtering criteria update | 18.4.0 |
| 2023-12 | SP-102 | SP-231253 | 4655 | 2 | F | Nnef_MemberUESelectionAssistance_Unsubscribe service operation information flow | 18.4.0 |
| 2023-12 | SP-102 | SP-231273 | 4658 | 1 | F | Clarifications of Event ID broadcast in SIB9 | 18.4.0 |
| 2023-12 | SP-102 | SP-231256 | 4661 | 2 | F | KI#1 Correction on PLMN ID in AF influence | 18.4.0 |
| 2023-12 | SP-102 | SP-231276 | 4666 | 2 | F | MBSR authorization information clarification | 18.4.0 |
| 2024-03 | SP-103 | SP-240102 | 4282 | 3 | F | UE-PCF stores UE indication of support of URSP delivery in EPS in UDR | 18.5.0 |
| 2024-03 | SP-103 | SP-240114 | 4293 | 5 | F | Update for QoS monitoring and network exposure | 18.5.0 |
| 2024-03 | SP-103 | SP-240114 | 4295 | 4 | F | Update for UE power saving management | 18.5.0 |
| 2024-03 | SP-103 | SP-240101 | 4326 | 4 | F | Congestion handling with Alternative S-NSSAI | 18.5.0 |
| 2024-03 | SP-103 | SP-240102 | 4336 | 2 | F | Correction of PCF for session receives PCF (PCF for UE) binding information | 18.5.0 |
| 2024-03 | SP-103 | SP-240102 | 4337 | 3 | F | URSP rule enforcement from roaming UE | 18.5.0 |
| 2024-03 | SP-103 | SP-240101 | 4452 | 3 | F | Clarification on on-demand slice | 18.5.0 |
| 2024-03 | SP-103 | SP-240086 | 4499 | 3 | A | Support of QMC configuration information | 18.5.0 |
| 2024-03 | SP-103 | SP-240115 | 4509 | 8 | F | Corrections to remove Nnef_UEId Service restrictions | 18.5.0 |
| 2024-03 | SP-103 | SP-240114 | 4512 | 5 | F | Clarification on Service Request Procedure for PDU Set based handling | 18.5.0 |
| 2024-03 | SP-103 | SP-240108 | 4513 | 5 | F | Updates to NEF service | 18.5.0 |
| 2024-03 | SP-103 | SP-240114 | 4514 | 5 | F | Clarification on PDU Set based handling during UE states transition | 18.5.0 |
| 2024-03 | SP-103 | SP-240101 | 4528 | 6 | F | Handling of UE initiated request when not present in area where slice is supported | 18.5.0 |
| 2024-03 | SP-103 | SP-240098 | 4569 | 2 | F | Configuration of DNS server address delivery from HPLMN to VPLMN | 18.5.0 |
| 2024-03 | SP-103 | SP-240098 | 4570 | 2 | F | Notification of serving PLMN change to AF | 18.5.0 |
| 2024-03 | SP-103 | SP-240107 | 4583 | 1 | F | Clarification on procedure for PIN service | 18.5.0 |
| 2024-03 | SP-103 | SP-240110 | 4598 | 2 | F | Correcting the ASTI procedure | 18.5.0 |
| 2024-03 | SP-103 | SP-240191 | 4615 | 1 | F | Data collection for Location Accuracy Analytics via AF | 18.5.0 |
| 2024-03 | SP-103 | SP-240102 | 4641 | 1 | F | Correction on URSP rule enforcement reporting | 18.5.0 |
| 2024-03 | SP-103 | SP-240114 | 4642 | 7 | F | Update on Support of UL PDU Set based QoS Handling | 18.5.0 |
| 2024-03 | SP-103 | SP-240098 | 4644 | 2 | F | KI#1 Corrections on Offload Identifier and misalignments in services | 18.5.0 |
| 2024-03 | SP-103 | SP-240107 | 4649 | 2 | F | Correction for terminologies | 18.5.0 |
| 2024-03 | SP-103 | SP-240094 | 4652 | 5 | F | Correction of direct event notification in multi-member AF session with required QoS | 18.5.0 |
| 2024-03 | SP-103 | SP-240093 | 4670 | 1 | F | Clarification on how to obtain N3IWF information | 18.5.0 |
| 2024-03 | SP-103 | SP-240106 | 4671 | 1 | F | Various fixes to RRC_INACTIVE with CN based MT communication handling | 18.5.0 |
| 2024-03 | SP-103 | SP-240106 | 4672 | 1 | F | Clarification on DL data size | 18.5.0 |
| 2024-03 | SP-103 | SP-240102 | 4673 | 1 | F | PDN Selection for URSP delivery in EPS | 18.5.0 |
| 2024-03 | SP-103 | SP-240110 | 4674 | 3 | F | Reinstating Namf_Communication_NonUeN2MessageTransfer for TSS reporting | 18.5.0 |
| 2024-03 | SP-103 | SP-240101 | 4675 | 1 | F | Clarification on Slice Replacement | 18.5.0 |
| 2024-03 | SP-103 | SP-240091 | 4676 | 1 | F | Clarification on satellite backhaul category change indication | 18.5.0 |
| 2024-03 | SP-103 | SP-240438 | 4677 | 6 | F | Clarifications on processing AF request for HR-SBO session | 18.5.0 |
| 2024-03 | SP-103 | SP-240096 | 4678 | 1 | F | Corrections on support for EPC IWK with MA PDU Sessions | 18.5.0 |
| 2024-03 | SP-103 | SP-240102 | 4679 | - | F | Corrections in Nnef_ServiceParameter_Notify operation | 18.5.0 |
| 2024-03 | SP-103 | SP-240111 | 4680 | 1 | F | Correction of UPF exposure service | 18.5.0 |
| 2024-03 | SP-103 | SP-240114 | 4681 | 1 | F | UPF activation of PDU Set Identification and marking for DL only | 18.5.0 |
| 2024-03 | SP-103 | SP-240094 | 4682 | 1 | F | Clarification on filtering criteria of member UE selection | 18.5.0 |
| 2024-03 | SP-103 | SP-240106 | 4684 | - | F | Data size handling in AMF update | 18.5.0 |
| 2024-03 | SP-103 | SP-240094 | 4687 | 1 | F | Corrections to MemberUESelectionAssistance for updating the list of target member UEs | 18.5.0 |
| 2024-03 | SP-103 | SP-240095 | 4688 | 1 | D | Cleaning up the term of RFSP Index in Use Validity Time | 18.5.0 |
| 2024-03 | SP-103 | SP-240104 | 4689 | 1 | F | LADN provisioning when there is existing PDU session | 18.5.0 |
| 2024-03 | SP-103 | SP-240110 | 4690 | 2 | F | CQRCI check issue when there are both AF requests and subscriptions | 18.5.0 |
| 2024-03 | SP-103 | SP-240110 | 4691 | 1 | F | Clarification on the on the UE Time Synchronization Subscription data for (g)PTP and TSCTSF checking | 18.5.0 |
| 2024-03 | SP-103 | SP-240102 | 4693 | 1 | F | Update to the PDU Session Modification Procedure for PCC Rule Generation when Connection Capabilities are Reported | 18.5.0 |
| 2024-03 | SP-103 | SP-240101 | 4694 | 1 | F | Clarification on subscription retrieval during slice replacement | 18.5.0 |
| 2024-03 | SP-103 | SP-240102 | 4696 | 1 | F | PCF discovery for URSP rule provision in EPS | 18.5.0 |
| 2024-03 | SP-103 | SP-240111 | 4697 | 1 | F | Clarification of usage of AoI | 18.5.0 |
| 2024-03 | SP-103 | SP-240112 | 4698 | 1 | F | Deregistration of MBSR based on the NGAP indication from IAB-donor | 18.5.0 |
| 2024-03 | SP-103 | SP-240102 | 4699 | - | F | Correction to PDU Session Establishment and Modification procedure for URSP rule enforcement reporting | 18.5.0 |
| 2024-03 | SP-103 | SP-240080 | 4700 | 3 | A | Correction on the AMF service operation for 5MBS | 18.5.0 |
| 2024-03 | SP-103 | SP-240097 | 4701 | 1 | F | Clarification on the Handling of the UE number with at least one PDU Session under Hierarchical NSAC architecture | 18.5.0 |
| 2024-03 | SP-103 | SP-240104 | 4704 | - | F | AF requested QoS for a UE or group of UEs | 18.5.0 |
| 2024-03 | SP-103 | SP-240114 | 4707 | 1 | F | Procedures for UPF relocation considering congestion exposure | 18.5.0 |
| 2024-03 | SP-103 | SP-240096 | 4708 | 1 | F | Clarifications on interworking with EPS | 18.5.0 |
| 2024-03 | SP-103 | SP-240100 | 4709 | - | F | Correction on validity information for SNPN | 18.5.0 |
| 2024-03 | SP-103 | SP-240100 | 4710 | - | F | Correction on validity information for CAG | 18.5.0 |
| 2024-03 | SP-103 | SP-240101 | 4712 | 1 | F | Clarification on Network Slice usage control timer | 18.5.0 |
| 2024-03 | SP-103 | SP-240115 | 4716 | 1 | B | Update to Support Network Controlled Repeater | 18.5.0 |
| 2024-03 | SP-103 | SP-240101 | 4717 | 1 | F | Support of Network Slice Replacement and area restrictions at UE mobility | 18.5.0 |
| 2024-03 | SP-103 | SP-240110 | 4719 | 3 | F | Clock status indication from RAN to TSCTSF | 18.5.0 |
| 2024-03 | SP-103 | SP-240106 | 4724 | 1 | F | MT-SDT term alignment | 18.5.0 |
| 2024-03 | SP-103 | SP-240101 | 4725 | 4 | F | Clarification on Network based monitoring and enforcement for NS-AoS and partially Allowed NSSAI | 18.5.0 |
| 2024-03 | SP-103 | SP-240111 | 4726 | - | F | Nupf_EventExposure_Notify service operation subscribed implicitly or explicitly | 18.5.0 |
| 2024-03 | SP-103 | SP-240114 | 4731 | - | F | Clarifications on applicability of Protocol Description for EoDB identification in DL | 18.5.0 |
| 2024-03 | SP-103 | SP-240098 | 4732 | 3 | F | Clarifications on the case AF interacts with HPLMN to influence HR-SBO traffic at VPLMN | 18.5.0 |
| 2024-03 | SP-103 | SP-240110 | 4734 | 1 | F | TSCTSF subscribing to RAN TSS based on list of TAs, correction to ASTI without AF request | 18.5.0 |
| 2024-03 | SP-103 | SP-240096 | 4736 | 1 | F | Error fix to MA PDU Session establishment with non-3GPP access connected to EPC | 18.5.0 |
| 2024-03 | SP-103 | SP-240112 | 4742 | 2 | F | MBSR mobility | 18.5.0 |
| 2024-03 | SP-103 | SP-240082 | 4744 | 1 | A | Application guidance for SSC mode | 18.5.0 |
| 2024-03 | SP-103 | SP-240078 | 4747 | 1 | A | Adding GPSI to 5GC-MT-LR Procedure without UDM Query procedure | 18.5.0 |
| 2024-03 | SP-103 | SP-240108 | 4748 | - | F | Add missing impacts from Ranging feature | 18.5.0 |
| 2024-03 | SP-103 | SP-240102 | 4752 | 2 | F | Forwarding of URSP Rule Enforcement Information for LBO roaming | 18.5.0 |
| 2024-03 | SP-103 | SP-240191 | 4753 | 1 | F | Correction to the FL capability type | 18.5.0 |
| 2024-03 | SP-103 | SP-240115 | 4755 | 3 | F | Determination of how to release the PDU Session when S-NSSAI is not supported | 18.5.0 |
| 2024-03 | SP-103 | SP-240115 | 4756 | 2 | F | Clarification on PDU Session Request when NAS message does not contain a DNN. | 18.5.0 |
| 2024-03 | SP-103 | SP-240102 | 4758 | 2 | F | Several corrections of URSP rule delivery in EPS | 18.5.0 |
| 2024-03 | SP-103 | SP-240115 | 4759 | 1 | F | Clarifications for PFD management service operations | 18.5.0 |
| 2024-03 | SP-103 | SP-240115 | 4760 | 1 | F | Corrections for QFI allocation event in Nsmf_EventExposure Service | 18.5.0 |
| 2024-03 | SP-103 | SP-240108 | 4764 | - | F | Correction to AMF service operation for Ranging/SL positioning. | 18.5.0 |
| 2024-03 | SP-103 | SP-240115 | 4767 | 2 | F | EPC interworking for PDU Sessions with SSC mode 2 or SSC mode 3 | 18.5.0 |
| 2024-06 | SP-104 | SP-240603 | 4703 | 5 | F | Corrections for the Nupf_EventExposure Service | 18.6.0 |
| 2024-06 | SP-104 | SP-240594 | 4771 | 2 | F | EAS Configuration Address Information provisioning in roaming | 18.6.0 |
| 2024-06 | SP-104 | SP-240606 | 4772 | 2 | F | Policy Association Termination Procedure update for policy counters stored in UDR | 18.6.0 |
| 2024-06 | SP-104 | SP-240606 | 4773 | 2 | F | Policy Association Establishment Procedure Update for SLAMUP | 18.6.0 |
| 2024-06 | SP-104 | SP-240601 | 4775 | 2 | F | Support for UE Ranging/SL Positioning privacy profile | 18.6.0 |
| 2024-06 | SP-104 | SP-240594 | 4777 | 3 | F | Security for EASDF discovery procedure via (V-) EASDF | 18.6.0 |
| 2024-06 | SP-104 | SP-240594 | 4779 | 2 | F | Clean up of the AF request for HR-SBO PDU Session | 18.6.0 |
| 2024-06 | SP-104 | SP-240591 | 4780 | - | F | Refer to TS 23.003 for the NAI to be used by the UE for TNGF access | 18.6.0 |
| 2024-06 | SP-104 | SP-240600 | 4782 | 1 | F | Clarification on CN based MT communication handling request | 18.6.0 |
| 2024-06 | SP-104 | SP-240599 | 4785 | 2 | F | Clarifications regarding DCMF | 18.6.0 |
| 2024-06 | SP-104 | SP-240598 | 4788 | 1 | F | Corrections on the clause reference and ID mapping | 18.6.0 |
| 2024-06 | SP-104 | SP-240592 | 4797 | 1 | F | Corrections and alignments for member UE selection assistance | 18.6.0 |
| 2024-06 | SP-104 | SP-240589 | 4798 | 2 | F | Alignment with CT1 to support Unavailability Period | 18.6.0 |
| 2024-06 | SP-104 | SP-240600 | 4799 | 1 | F | Activation of DL data size reporting for support of MT-SDT | 18.6.0 |
| 2024-06 | SP-104 | SP-240592 | 4800 | 3 | F | Corrections to assistance for member UE selection functionality and service | 18.6.0 |
| 2024-06 | SP-104 | SP-240602 | 4805 | 6 | F | Corrections to Nnef_UEId Service | 18.6.0 |
| 2024-06 | SP-104 | SP-240601 | 4812 | 1 | F | Corrections to GPSI and Application Layer ID mapping | 18.6.0 |
| 2024-06 | SP-104 | SP-240594 | 4815 | 2 | F | Corrections to Nnef_UEId service | 18.6.0 |
| 2024-06 | SP-104 | SP-240591 | 4817 | 2 | F | Correction about the UE indication of the support of slice based N3IWF/TNGF selection | 18.6.0 |
| 2024-06 | SP-104 | SP-240602 | 4823 | 3 | D | Editorial cleanup | 18.6.0 |
| 2024-09 | SP-105 | SP-241244 | 4789 | 4 | F | Handling of the slice deregistration inactivity timer in the inter AMF mobility | 18.7.0 |
| 2024-09 | SP-105 | SP-241278 | 4794 | 4 | F | Correction related to discovery and selection over roaming interface | 18.7.0 |
| 2024-09 | SP-105 | SP-241278 | 4813 | 3 | F | Session level priority realization in AMF | 18.7.0 |
| 2024-09 | SP-105 | SP-241278 | 4820 | 2 | F | Correcting the trigger for SM Policy Association Modification | 18.7.0 |
| 2024-09 | SP-105 | SP-241246 | 4833 | 1 | F | Incorrect PCF registration parameters | 18.7.0 |
| 2024-09 | SP-105 | SP-241254 | 4840 | 2 | F | Adding specification reference in description | 18.7.0 |
| 2024-09 | SP-105 | SP-241246 | 4846 | 1 | F | Update on reported Connection Capabilities and awareness of URSP Rule Enforcement | 18.7.0 |
| 2024-09 | SP-105 | SP-241252 | 4851 | 2 | F | Subscriptions to UPF event Exposure targeting an individual UE for non IP PDU Sessions | 18.7.0 |
| 2024-09 | SP-105 | SP-241246 | 4852 | 1 | F | Correction to Awareness of URSP Rule Enforcement - 23.502 | 18.7.0 |
| 2024-09 | SP-105 | SP-241278 | 4855 | 2 | F | Align H-PCF selection with H-SMF selection in 23.502 R18 | 18.7.0 |
| 2024-09 | SP-105 | SP-241239 | 4858 | 1 | A | Mapping between NSAGs and S-NSSAIs - 23.502 R18 | 18.7.0 |
| 2024-09 | SP-105 | SP-241251 | 4900 | 1 | F | Clarification on subscription during the ASTI create and update | 18.7.0 |
| 2024-09 | SP-105 | SP-241252 | 4923 | 3 | F | Subscription of UPF event via I-SMF | 18.7.0 |
| 2024-09 | SP-105 | SP-241242 | 4941 | - | F | Update UE context in AMF to include LCS-UP context for user plane positioning | 18.7.0 |
| 2024-09 | SP-105 | SP-241245 | 4949 | 2 | F | Clarification on Access Type for UE counting | 18.7.0 |
| 2024-09 | SP-105 | SP-241260 | 4959 | - | F | EAS rediscovery indication alignment | 18.7.0 |
| 2024-09 | SP-105 | SP-241244 | 4966 | 2 | F | Correction the slice usage policy information in the SM subscription data | 18.7.0 |
| 2024-09 | SP-105 | SP-241251 | 4977 | 1 | F | Correction to timing syncronization status reporting from RAN to TSCTSF | 18.7.0 |
| 2024-09 | SP-105 | SP-241260 | 4986 | 1 | F | Corrections on AF request related to Edge Computing | 18.7.0 |
| 2024-12 | SP-106 | SP-241480 | 5051 | 2 | F | Subscription of UPF event via SMF in deployments with I-SMF | 18.8.0 |
| 2024-12 | SP-106 | SP-241468 | 5068 | 1 | F | UDR Application Data Subtypes for IPTV | 18.8.0 |
| 2024-12 | SP-106 | SP-241470 | 5074 | - | F | R18 AIMLsys_ 23502_CR for clarification on PDTQ procedures | 18.8.0 |
| 2024-12 | SP-106 | SP-241473 | 5076 | 2 | F | Transfer of slice deregistration inactivity timer between AMFs | 18.8.0 |
| 2024-12 | SP-106 | SP-241474 | 5105 | 2 | F | NSAC handling in Hierarchical architecture | 18.8.0 |
| 2024-12 | SP-106 | SP-241480 | 5108 | 2 | F | Subscription of UPF event via I-SMF for the Any UE case | 18.8.0 |
| 2025-03 | SP-107 | SP-250033 | 5020 | 3 | F | Correction on DCAMP | 18.9.0 |
| 2025-03 | SP-107 | SP-250046 | 5214 | 1 | F | Correction to Awareness of URSP Rule Enforcement - 23.502 | 18.9.0 |
| 2025-03 | SP-107 | SP-250053 | 5246 | - | F | UL Protocol Description provisioning to SMF from PCF | 18.9.0 |
| 2025-03 | SP-107 | SP-250051 | 5258 | 1 | F | Corrections for Group UE and Any UE cases | 18.9.0 |
| 2025-03 | SP-107 | SP-250028 | 5263 | 1 | A | SM context release in the IRAT handover procedure | 18.9.0 |
| 2025-03 | SP-107 | SP-250052 | 5283 | 1 | F | PDU Session Modification for Port Management Information | 18.9.0 |
| 2025-03 | SP-107 | SP-250047 | 5307 | - | F | Fix wrong implementation of approved TDoc S2-2301807 | 18.9.0 |
| 2025-03 | SP-107 | SP-250051 | 5313 | 1 | F | Avoiding duplication of SMF notifications for SMF&amp;UPF event reporting targeting Any UE | 18.9.0 |
| 2025-03 | SP-107 | SP-250036 | 5326 | - | F | Correction on HR-SBO allowed indication and AF TI container transfer | 18.9.0 |
| 2025-03 | SP-107 | SP-250028 | 5344 | - | A | Update of Routing Indicator in SMF, SMSF | 18.9.0 |
| 2025-03 | SP-107 | SP-250051 | 5358 | 1 | F | Clarification on the UPF event subscription | 18.9.0 |
| 2025-03 | SP-107 | SP-250051 | 5364 | 2 | F | Correction on the UPF event subscription via I-SMF | 18.9.0 |
| 2025-03 | SP-107 | SP-250033 | 5377 | 1 | F | Handling of handover cancel during 5GS to EPS mobility | 18.9.0 |
| 2025-06 | SP-108 | SP-250451 | 5380 | 2 | F | Correction for BSF invocation in URSP Rule Enforcement Information procedure | 18.10.0 |
| 2025-06 | SP-108 | SP-250457 | 5416 | 1 | F | Removal of text for PWS | 18.10.0 |
| 2025-06 | SP-108 | SP-250458 | 5430 | 3 | F | N2 SM information to NG-RAN | 18.10.0 |
| 2025-06 | SP-108 | SP-250451 | 5440 | 3 | F | Registration handling during the mobility from non-3GPP access to 3GPP access | 18.10.0 |
| 2025-06 | SP-108 | SP-250453 | 5486 | 1 | F | HR SBO request indication in inter PLMN mobility case | 18.10.0 |
| 2025-09 | SP-109 | SP-250941 | 5571 | - | F | Correction on Nsmf_PDUSession_Create request for HR-SBO scenario | 18.11.0 |
| 2025-12 | SP-110 | SP-251319 | 5339 | 4 | A | Clarification on emergency PDU session release | 18.12.0 |
| 2025-12 | SP-110 | SP-251322 | 5601 | 2 | F | Correction of PDU Session Establishment procedure for Network Slice Replacement support | 18.12.0 |
| 2026-03 | SP-111 | SP-260080 | 5603 | 1 | F | Correction on DNAI Mapping info | 18.13.0 |
| 2026-06 | SP-112 | SP-260427 | 5732 | 1 | F | AF requested QoS for UE not identified by UE address | 18.14.0 |
| 2026-06 | SP-112 | SP-260425 | 5751 | 3 | F | Making UDR interaction in PDTQ procedure optional | 18.14.0 |
<!-- /table -->
