# P.2 Session management and traffic routing for PIN

The general session management principles as described in clause 5.6, the QoS model as defined in clause 5.7 and the User Plane management for 5GS as defined in clause 5.8 are applicable to PIN-DN communication and PIN indirect communication.

If a PIN has multiple PEGCs, 5G VN group communication mechanisms can be used for PIN indirect communication. In this case a dedicated SMF set is used for managing the PIN related PDU Sessions from all the PEGCs of that PIN and the PDU session management principles for 5G VN-LAN-type services as specified in clause 5.29.3 are applicable. The user plane handling for 5G LAN-type services as specified in 5.29.4 are applicable with following differences:

\- For PIN indirect communication N19-based traffic forwarding is not used i.e. the PIN traffic is forwarded using:

\- N6-based traffic forwarding method, where the UL/DL traffic for the PIN communication is forwarded to/from the DN;

\- local switching as depicted in Figure P.2-1 below, following the principles of local switching of traffic for 5G VN LAN-type service.

[figure]

Figure P.2-1: Local-switch based user plane architecture for PIN

NOTE: Figure P.2-1 does not show traffic from a PEMC.

The SMF configures the UPF(s) to apply N6-based traffic forwarding to route traffic between PDU Sessions of different PEGCs of a PIN as specified in clause 5.8.2.13. The SMF can apply local switching as specified in clause 5.8.2.13 in order to enable UPF locally forward uplink stream from one PDU session of one PEGC of a PIN as downlink stream of PDU session of one or more PEGC(s) of the same PIN. For local switching of PIN traffic between PIN related PDU sessions from different PEGCs of a single PIN, based on the (DNN, S-NSSAI) combination that is used for the PDU session related to PIN, the SMF provides a Network Instance to the UPF in FAR and/or PDR via N4 Session Establishment/Modification procedures.

######## Annex Q (informative): Satellite coverage availability information

The protocol and format of satellite coverage availability information to be provisioned to the UE via PDU session or SMS is not defined in this release of the specification, but this annex provides some examples on the information that constitutes input to the source of satellite coverage availability information e.g. external server and the output it provides to the UE. Satellite coverage availability information can be indicated to the UE by indications corresponding to whether or not coverage is available for a specific satellite RAT Type for a particular location and time, where:

\- These indications can be Boolean "True" (e.g. coverage available) and "False" (coverage not available);

\- locations can correspond to grid points in a fixed array (e.g. rectangular, hexagonal);

\- Coverage availability times may occur at fixed periodic intervals; and

\- Coverage availability information is per RAT Type. The information provisioned to the UE can include coverage information on only one PLMN or multiple PLMNs.

If Satellite coverage availability information indicates coverage is available then additional information on whether PLMN is allowed to operate in that location can be provided to the UE.

In order for the source of satellite coverage availability information to provide accurate information to the UE, a UE might indicate for example the following information to a source of satellite coverage availability information (e.g. an external server):

\- Serving PLMN ID (if not already known or implied).

\- One or more satellite RAT Types (where satellite coverage availability information is then expected for these one or more RAT Types).

\- List of supported satellite frequency bands (if not implied by the particular RAT Types).

\- Present UE location (e.g. latitude and longitude) for a reference grid point (e.g. the most Southerly and then most Westerly grid point).

\- Type of Array (e.g. rectangular or hexagonal).

\- Minimum elevation angle.

Based on the above information provided by the UE, satellite coverage availability information could be delivered to the UE as a sequence of time durations for each grid point where each time duration includes an indication of coverage availability or unavailability one example of many alternatives as illustrated below for a particular grid point with N different durations:

Satellite coverage availability information at a given grid point = \<N\> \<Binary 0 or 1\>\<Duration 1\> \<Binary 0 or 1\>\<Duration 2\> . . . . \<Binary 0 or 1\>\<Duration N\>

The above would be concatenated for all of the grid points to produce the satellite coverage availability information.

When SMS is used to deliver the satellite coverage availability information, the UE input and satellite coverage availability information output can be delivered in a series of concatenated SMS messages using possibly the same format.

########  Annex R (informative): Change history

<!-- table -->
| Change history (x8) |
| Date | Meeting | TDoc | CR | Rev | Cat | Subject/Comment | New version |
| 06-2017 | SP#76 | SP-170384 | - | - | - | MCC Editorial Update for presentation to TSG SA#76 for Information | 1.0.0 |
| 12-2017 | SP#78 | - | - | - | - | MCC Editorial Update | 2.0.0 |
| 12-2017 | SP#78 | SP-170931 | - | - | - | Correction of Annex A figure numbers for presentation to TSG SA#78 for Approval | 2.0.1 |
| 12-2017 | SP#78 | - | - | - | - | MCC Editorial Update after TSG SA#78 Approval | 15.0.0 |
| 03-2018 | SP#79 | SP-180090 | 0002 | 2 | F | Using NRF for UPF discovery | 15.1.0 |
| 03-2018 | SP#79 | SP-180097 | 0003 | 2 | F | Configuration information the UE may exchange with the SMF during the lifetime of a PDU Session | 15.1.0 |
| 03-2018 | SP#79 | SP-180097 | 0004 | - | F | Handling of MM back-off timer for N3GPP Access | 15.1.0 |
| 03-2018 | SP#79 | SP-180097 | 0005 | - | F | Correction of the definitions of Allowed NSSAI and Configured NSSAI | 15.1.0 |
| 03-2018 | SP#79 | SP-180097 | 0006 | 4 | F | Allowed NSSAI and Access Type | 15.1.0 |
| 03-2018 | SP#79 | SP-180097 | 0007 | 1 | F | Correction to rejected S-NSSAI | 15.1.0 |
| 03-2018 | SP#79 | SP-180097 | 0008 | 2 | F | Corrections to Emergency Services | 15.1.0 |
| 03-2018 | SP#79 | SP-180096 | 0009 | - | D | Clarification of SUCI | 15.1.0 |
| 03-2018 | SP#79 | SP-180096 | 0010 | - | D | Miscellaneous editorial corrections (capitalization, messages, procedures etc.) | 15.1.0 |
| 03-2018 | SP#79 | SP-180097 | 0011 | - | F | Corrections to RQoS logic when receiving DL packet with RQI | 15.1.0 |
| 03-2018 | SP#79 | SP-180097 | 0013 | - | F | Paging Policy Differentiation correction | 15.1.0 |
| 03-2018 | SP#79 | SP-180097 | 0014 | - | F | Clarification on UE specific DRX parameter from old AMF to new AMF | 15.1.0 |
| 03-2018 | SP#79 | SP-180097 | 0015 | - | F | Clarification on PCF selection | 15.1.0 |
| 03-2018 | SP#79 | SP-180093 | 0016 | - | F | Adding the new clause about SMSF selection | 15.1.0 |
| 03-2018 | SP#79 | SP-180090 | 0017 | - | F | Use of identifiers for mobility between GERAN/UTRAN and 5GS | 15.1.0 |
| 03-2018 | SP#79 | SP-180090 | 0018 | 1 | F | Remaining IP address/prefix lifetime with SSC mode 3 | 15.1.0 |
| 03-2018 | SP#79 | SP-180097 | 0020 | 1 | F | Correction to handling of S-NSSAI mapping information | 15.1.0 |
| 03-2018 | SP#79 | SP-180090 | 0021 | 3 | F | Wildcard DNN subscription | 15.1.0 |
| 03-2018 | SP#79 | SP-180097 | 0022 | 4 | F | Clarification in LADN clause 5.6.5 - TS 23.501 | 15.1.0 |
| 03-2018 | SP#79 | SP-180097 | 0023 | - | F | Clean up on the interworking without 26 indication | 15.1.0 |
| 03-2018 | SP#79 | SP-180097 | 0024 | - | F | TS 23.501 mobility from EPC to 5GC | 15.1.0 |
| 03-2018 | SP#79 | SP-18009 | 0025 | 2 | F | AMF Load Re-Balancing For CONNECTED mode UE | 15.1.0 |
| 03-2018 | SP#79 | SP-180097 | 0026 | - | F | Update on Traffic Detection Information | 15.1.0 |
| 03-2018 | SP#79 | SP-180097 | 0027 | - | F | Proposal of Specifying Packet Detection Rule | 15.1.0 |
| 03-2018 | SP#79 | SP-180097 | 0028 | 1 | F | Relation between the SSC mode 3 and the PDU type | 15.1.0 |
| 03-2018 | SP#79 | SP-180091 | 0031 | - | F | UE-specific DRX parameter negotiation between UE and AMF | 15.1.0 |
| 03-2018 | SP#79 | SP-180091 | 0033 | - | F | Control of the Messages triggering Paging at AMF | 15.1.0 |
| 03-2018 | SP#79 | SP-180091 | 0034 | 2 | F | Alignment with TS 23.502 on Service Request procedure | 15.1.0 |
| 03-2018 | SP#79 | SP-180097 | 0035 | - | F | Corrections and clarifications for the usage of Packet Filter Set | 15.1.0 |
| 03-2018 | SP#79 | SP-180091 | 0036 | - | F | Update Paging Policy Differentiation | 15.1.0 |
| 03-2018 | SP#79 | SP-180097 | 0037 | 1 | F | Correction to AF influence on traffic routing | 15.1.0 |
| 03-2018 | SP#79 | SP-180097 | 0038 | - | F | Clarifications to AF influence on traffic routing | 15.1.0 |
| 03-2018 | SP#79 | SP-180097 | 0039 | - | F | Clarify NSSF discovery | 15.1.0 |
| 03-2018 | SP#79 | SP-180090 | 0040 | 1 | F | Change subscribed S-NSSAI in UE to configured NSSAI of HPLMN | 15.1.0 |
| 03-2018 | SP#79 | SP-180097 | 0041 | 1 | F | UDM discovery clarifications | 15.1.0 |
| 03-2018 | SP#79 | SP-180097 | 0044 | - | F | Corrections to UPF selection and resolution of related Editor's Note | 15.1.0 |
| 03-2018 | SP#79 | SP-180097 | 0045 | 1 | F | Updates to the Security Edge Protection Proxy description | 15.1.0 |
| 03-2018 | SP#79 | SP-180098 | 0046 | - | F | Homogeneous support for IMS voice over PS Session supported indication | 15.1.0 |
| 03-2018 | SP#79 | SP-180098 | 0047 | 1 | F | Slice selection cleanup | 15.1.0 |
| 03-2018 | SP#79 | SP-180091 | 0048 | - | F | Resource reservation for services sharing priority | 15.1.0 |
| 03-2018 | SP#79 | SP-180098 | 0049 | - | F | Replace PUI with GPSI | 15.1.0 |
| 03-2018 | SP#79 | SP-180091 | 0050 | - | F | Idle and connected state terminology cleanup | 15.1.0 |
| 03-2018 | SP#79 | SP-180098 | 0051 | - | F | NAS congestion control update | 15.1.0 |
| 03-2018 | SP#79 | SP-180098 | 0052 | - | F | Complete of IMS Emergency support in 5G including slice and local numbers | 15.1.0 |
| 03-2018 | SP#79 | SP-180098 | 0053 | 1 | F | Traffic mapping information that disallows UL packets | 15.1.0 |
| 03-2018 | SP#79 | SP-180098 | 0054 | 1 | F | Clean-up of Characteristics signalling | 15.1.0 |
| 03-2018 | SP#79 | SP-180093 | 0055 | - | F | EPS Fallback for voice | 15.1.0 |
| 03-2018 | SP#79 | SP-180098 | 0056 | 1 | F | Network sharing prioritised PLMN handling | 15.1.0 |
| 03-2018 | SP#79 | SP-180098 | 0057 | 2 | F | Corrections to Combined N3IWF/ePDG Selection | 15.1.0 |
| 03-2018 | SP#79 | SP-180091 | 0058 | 1 | F | Moving Network Analytics functionality into 23.501 | 15.1.0 |
| 03-2018 | SP#79 | SP-180098 | 0061 | 1 | F | Clarification on UDR | 15.1.0 |
| 03-2018 | SP#79 | SP-180098 | 0062 | - | F | QFI in N9 | 15.1.0 |
| 03-2018 | SP#79 | SP-180098 | 0063 | 1 | F | NF Service Discovery Corrections | 15.1.0 |
| 03-2018 | SP#79 | SP-180098 | 0064 | 3 | F | UE mobility event notification | 15.1.0 |
| 03-2018 | SP#79 | SP-180092 | 0066 | 4 | C | Architectural solution for User Plane (UP) Security policy and User Plane Integrity Protection | 15.1.0 |
| 03-2018 | SP#79 | SP-180098 | 0068 | - | F | CN assistance information enhancement | 15.1.0 |
| 03-2018 | SP#79 | SP-180098 | 0070 | - | F | Inter-PLMN mobility when N26 is not used | 15.1.0 |
| 03-2018 | SP#79 | SP-180093 | 0071 | 3 | F | Interworking without N26 corrections | 15.1.0 |
| 03-2018 | SP#79 | SP-180098 | 0072 | 1 | F | Clarification for S-NSSAI based congestion Control | 15.1.0 |
| 03-2018 | SP#79 | SP-180098 | 0073 | - | F | Non-roaming Architecture for Network Exposure Function in reference point representation | 15.1.0 |
| 03-2018 | SP#79 | SP-180098 | 0074 | 1 | F | NSSF service update | 15.1.0 |
| 03-2018 | SP#79 | SP-180092 | 0075 | 1 | F | Correcting the support of charging Characteristics | 15.1.0 |
| 03-2018 | SP#79 | SP-180098 | 0076 | - | F | Non-Allowed Area as criterion for Cell Reselection or trigger for PLMN Selection | 15.1.0 |
| 03-2018 | SP#79 | SP-180098 | 0077 | 1 | F | Correction to the use of Redirection in EPS fallback for emergency services | 15.1.0 |
| 03-2018 | SP#79 | SP-180098 | 0078 | 2 | F | Network Provided Location for non-3GPP access | 15.1.0 |
| 03-2018 | SP#79 | SP-180098 | 0082 | 1 | F | Updates to TS 23.501 Scope | 15.1.0 |
| 03-2018 | SP#79 | SP-180098 | 0083 | 1 | F | Fixes for CP protocol stack | 15.1.0 |
| 03-2018 | SP#79 | SP-180098 | 0084 | 1 | F | EPC to 5GC Migration fixes for Option 7 | 15.1.0 |
| 03-2018 | SP#79 | SP-180098 | 0085 | 1 | F | EPS Interworking: 5G-S-TMSI derivation and context retrieval | 15.1.0 |
| 03-2018 | SP#79 | SP-180099 | 0086 | 1 | F | Fixes for Emergency Services and Emergency Services using Fallback | 15.1.0 |
| 03-2018 | SP#79 | SP-180099 | 0087 | 2 | F | 5G QoS fixes for URLLC services related attributes - PDB, PER, MDB, 5QI | 15.1.0 |
| 03-2018 | SP#79 | SP-180099 | 0088 | 4 | F | QoS Notification control and Release | 15.1.0 |
| 03-2018 | SP#79 | SP-180095 | 0089 | 4 | C | GUTI unique across AMFs in an AMF SET | 15.1.0 |
| 03-2018 | SP#79 | SP-180099 | 0090 | 1 | F | Partitioning of Identifier space to ensure success of Context retrieval for EPS Interworking | 15.1.0 |
| 03-2018 | SP#79 | SP-180099 | 0091 | 1 | F | UDM Discovery with SUPI as input | 15.1.0 |
| 03-2018 | SP#79 | SP-180099 | 0095 | 5 | F | Clarifications of Subscribed and Configured S-NSSAI update | 15.1.0 |
| 03-2018 | SP#79 | SP-180099 | 0102 | 4 | F | Sending of congested S-NSSAI during AN signalling connection Establishment | 15.1.0 |
| 03-2018 | SP#79 | SP-180099 | 0104 | 3 | F | Clarification on modification of the set of network slices for a UE | 15.1.0 |
| 03-2018 | SP#79 | SP-180092 | 0105 | 1 | F | UE support for Multi-homed IPv6 PDU Session | 15.1.0 |
| 03-2018 | SP#79 | SP-180099 | 0106 | 1 | F | 5GS support for network slicing | 15.1.0 |
| 03-2018 | SP#79 | SP-180093 | 0107 | 2 | F | UE Core Network Capability handling | 15.1.0 |
| 03-2018 | SP#79 | SP-180099 | 0108 | - | F | eCall over IMS supported over E-UTRA only | 15.1.0 |
| 03-2018 | SP#79 | SP-180090 | 0109 | 2 | F | Domain selection for UE in Dual Registration mode | 15.1.0 |
| 03-2018 | SP#79 | SP-180099 | 0110 | 2 | F | MICO and interworking with EPC | 15.1.0 |
| 03-2018 | SP#79 | SP-180099 | 0115 | 2 | F | Correction of NSSAI handling | 15.1.0 |
| 03-2018 | SP#79 | SP-180099 | 0116 | 1 | F | Slice Availability update | 15.1.0 |
| 03-2018 | SP#79 | SP-180099 | 0122 | 2 | F | User Plane management to support interworking with EPS | 15.1.0 |
| 03-2018 | SP#79 | SP-180099 | 0124 | 3 | F | Supporting Common API framework for NEF | 15.1.0 |
| 03-2018 | SP#79 | SP-180099 | 0126 | 1 | F | Clarification on NAS recovery procedure in RRC Inactive | 15.1.0 |
| 03-2018 | SP#79 | SP-180099 | 0129 | 2 | F | Correction for congestion control | 15.1.0 |
| 03-2018 | SP#79 | SP-180096 | 0133 | - | D | Correction for the usage of RQI bit | 15.1.0 |
| 03-2018 | SP#79 | SP-180099 | 0134 | 5 | F | Clarifications for QoS Framework | 15.1.0 |
| 03-2018 | SP#79 | SP-180099 | 0135 | 2 | F | DL signalling handling for non-3GPP PDU Session | 15.1.0 |
| 03-2018 | SP#79 | SP-180099 | 0136 | 1 | F | Clarification on location reporting for LADN in RRC Inactive clause 5.3.3.2.5 - TS 23.501 | 15.1.0 |
| 03-2018 | SP#79 | SP-180099 | 0137 | 2 | F | Network Sharing and Interworking with EPS- TS 23.501 | 15.1.0 |
| 03-2018 | SP#79 | SP-180099 | 0138 | - | F | Edge Computing Clarification | 15.1.0 |
| 03-2018 | SP#79 | SP-180095 | 0141 | 1 | B | Supporting 3GPP PS Data Off in 5GS | 15.1.0 |
| 03-2018 | SP#79 | SP-180099 | 0144 | 2 | F | Management of service area restriction information | 15.1.0 |
| 03-2018 | SP#79 | SP-180099 | 0145 | 2 | F | Clarification on TAI list assignment for different 5G RATs | 15.1.0 |
| 03-2018 | SP#79 | SP-180099 | 0146 | - | F | Network sharing for supporting RRC redirection procedure | 15.1.0 |
| 03-2018 | SP#79 | SP-180095 | 0147 | 2 | C | Selection of NAS procedures for E-UTRA connected to both EPC and 5GC | 15.1.0 |
| 03-2018 | SP#79 | SP-180100 | 0149 | 1 | F | Clarification of SM congestion control | 15.1.0 |
| 03-2018 | SP#79 | SP-180100 | 0150 | 1 | F | Updates to AF influence on traffic routing | 15.1.0 |
| 03-2018 | SP#79 | SP-180100 | 0151 | 2 | F | Updates to description of CN Tunnel Info | 15.1.0 |
| 03-2018 | SP#79 | SP-180100 | 0152 | - | F | Clarification on RRM desciption | 15.1.0 |
| 03-2018 | SP#79 | SP-180100 | 0153 | 1 | F | Editorial corrections in clause 5.3.2.4 Support of a UE registered over both 3GPP and Non-3GPP access | 15.1.0 |
| 03-2018 | SP#79 | SP-180100 | 0154 | 2 | F | Clarification on the association of an S-NSSAI to a given application | 15.1.0 |
| 03-2018 | SP#79 | SP-180100 | 0155 | 2 | F | Update of UE Network slicing configuration | 15.1.0 |
| 03-2018 | SP#79 | SP-180100 | 0157 | 2 | F | SBA Scope Clarification | 15.1.0 |
| 03-2018 | SP#79 | SP-180092 | 0158 | 2 | F | Clean up for BSF | 15.1.0 |
| 03-2018 | SP#79 | SP-180092 | 0160 | 3 | F | Clarification on Area of Interest for Presence Area Reporting | 15.1.0 |
| 03-2018 | SP#79 | SP-180100 | 0161 | 3 | F | Correction to Providing AF request to multiple PCFs | 15.1.0 |
| 03-2018 | SP#79 | SP-180100 | 0165 | 1 | F | Usage of Unified access control in priority mechanisms | 15.1.0 |
| 03-2018 | SP#79 | SP-180100 | 0166 | - | F | Update Roaming reference architectures | 15.1.0 |
| 03-2018 | SP#79 | SP-180100 | 0168 | 5 | F | Clarification of UE Requested NSSAI | 15.1.0 |
| 03-2018 | SP#79 | SP-180100 | 0170 | 1 | F | Emergency Services Support indication per RAT | 15.1.0 |
| 03-2018 | SP#79 | SP-180100 | 0171 | 2 | F | N4 User Plane Path | 15.1.0 |
| 03-2018 | SP#79 | SP-180100 | 0173 | 1 | F | SSC Mode Selection | 15.1.0 |
| 03-2018 | SP#79 | SP-180100 | 0174 | 2 | F | Proposal of QER, URR and FAR | 15.1.0 |
| 03-2018 | SP#79 | SP-180100 | 0177 | 1 | F | UE specific DRX parameters for CM-CONNECTED with Inactive state | 15.1.0 |
| 03-2018 | SP#79 | SP-180100 | 0179 | 6 | F | Slicing configuration update | 15.1.0 |
| 03-2018 | SP#79 | SP-180100 | 0180 | 1 | F | Update of Mobility Restrictions | 15.1.0 |
| 03-2018 | SP#79 | SP-180125 | 0181 | 1 | B | Addition of PDU Session type IPv4v6 | 15.1.0 |
| 03-2018 | SP#79 | SP-180100 | 0183 | 1 | F | Mapping of Requested NSSAI clarification | 15.1.0 |
| 03-2018 | SP#79 | SP-180100 | 0184 | 2 | F | Clarification of the interworking between 5G and GERAN/UTRAN/E-UTRAN when UE is in RRC-inactive state | 15.1.0 |
| 03-2018 | SP#79 | SP-180100 | 0187 | 5 | F | Select the same SMF+UPF for PDU sessions of the same DNN within one slice | 15.1.0 |
| 03-2018 | SP#79 | SP-180100 | 0189 | 2 | F | Subscription Permanent Identifier | 15.1.0 |
| 03-2018 | SP#79 | SP-180100 | 0192 | 1 | F | Clarification of interworking procedures without N26 interface | 15.1.0 |
| 03-2018 | SP#79 | SP-180100 | 0194 | 1 | F | Clarification on the use of the indicator for the support of interworking without N26 | 15.1.0 |
| 06-2018 | SP#80 | SP-180482 | 0067 | 6 | F | Controlled support of (AF) session binding for Ethernet PDU Session Type | 15.2.0 |
| 06-2018 | SP#80 | SP-180491 | 0117 | 7 | F | Use of Priority parameters for scheduling | 15.2.0 |
| 06-2018 | SP#80 | SP-180489 | 0169 | 8 | F | Temporary restriction of Reflective QoS | 15.2.0 |
| 06-2018 | SP#80 | SP-180478 | 0196 | 1 | F | 5_16_6_Mission Critical Services - Reference Update | 15.2.0 |
| 06-2018 | SP#80 | SP-180478 | 0197 | 1 | F | 5_16_6_Mission Critical Services - Editorial Changes | 15.2.0 |
| 06-2018 | SP#80 | SP-180477 | 0198 | - | D | Fixing Incorrect References to the Service Request Procedures | 15.2.0 |
| 06-2018 | SP#80 | SP-180489 | 0199 | 2 | F | SUPI based paging | 15.2.0 |
| 06-2018 | SP#80 | SP-180486 | 0201 | 2 | F | Mobile Terminated SMS over NAS: 5GS Access Selection | 15.2.0 |
| 06-2018 | SP#80 | SP-180483 | 0203 | 1 | F | Discovery and Topology Hiding | 15.2.0 |
| 06-2018 | SP#80 | SP-180479 | 0206 | 3 | F | Changed length and mapping of 5GS Temporary Identifiers | 15.2.0 |
| 06-2018 | SP#80 | SP-180488 | 0207 | 5 | F | Slice configuration change | 15.2.0 |
| 06-2018 | SP#80 | SP-180483 | 0209 | 1 | F | Defining NWDAF in 23.501 | 15.2.0 |
| 06-2018 | SP#80 | SP-180484 | 0210 | 3 | F | Corrections to PFD management | 15.2.0 |
| 06-2018 | SP#80 | SP-180491 | 0212 | 2 | F | Update on UE mobility event notification | 15.2.0 |
| 06-2018 | SP#80 | SP-180485 | 0214 | 1 | F | Identification and update of UE derived QoS rule | 15.2.0 |
| 06-2018 | SP#80 | SP-180479 | 0216 | 2 | F | Clarification of traffic steering control in the case of interworking | 15.2.0 |
| 06-2018 | SP#80 | SP-180491 | 0217 | 2 | F | Updates to System Enablers for Priority Mechanism | 15.2.0 |
| 06-2018 | SP#80 | SP-180478 | 0219 | 2 | F | AMF Selection aspects | 15.2.0 |
| 06-2018 | SP#80 | SP-180478 | 0220 | 1 | F | AMF functionality clarification - to add SUCI | 15.2.0 |
| 06-2018 | SP#80 | SP-180484 | 0222 | 1 | F | EPS Interworking Principles - SR mode with N26 | 15.2.0 |
| 06-2018 | SP#80 | SP-180490 | 0224 | 1 | F | UDM services - addition to Nudm_UEAuthentication | 15.2.0 |
| 06-2018 | SP#80 | SP-180490 | 0225 | 0 | F | UDM functionality support for SUCI | 15.2.0 |
| 06-2018 | SP#80 | SP-180486 | 0226 | 3 | F | MFBR Enforcement for GBR QoS Flows | 15.2.0 |
| 06-2018 | SP#80 | SP-180486 | 0227 | 1 | F | NF Registration via the NRF | 15.2.0 |
| 06-2018 | SP#80 | SP-180478 | 0229 | - | F | Abbreviations supplement | 15.2.0 |
| 06-2018 | SP#80 | SP-180478 | 0231 | 1 | F | 3GPP PS Data Off Clarification | 15.2.0 |
| 06-2018 | SP#80 | SP-180477 | 0232 | - | D | Network Sharing and Interworking Clarification | 15.2.0 |
| 06-2018 | SP#80 | SP-180480 | 0237 | 3 | F | Clarification on MT SMS domain selection by SMSF | 15.2.0 |
| 06-2018 | SP#80 | SP-180489 | 0239 | 1 | F | TS 23.501: Clean-up for the RRC Inactive related procedure | 15.2.0 |
| 06-2018 | SP#80 | SP-180489 | 0240 | - | F | Correction on Control Plane protocol stacks | 15.2.0 |
| 06-2018 | SP#80 | SP-180480 | 0241 | 2 | F | Clarification on NSSAI related functionality in 5G RAN | 15.2.0 |
| 06-2018 | SP#80 | SP-180489 | 0242 | 2 | F | Clarification on Application data | 15.2.0 |
| 06-2018 | SP#80 | SP-180479 | 0244 | 3 | F | AMF UE area of interest reporting in RRC inactive state | 15.2.0 |
| 06-2018 | SP#80 | SP-180480 | 0245 | - | F | Clarification on RAT fallback | 15.2.0 |
| 06-2018 | SP#80 | SP-180480 | 0248 | 1 | F | Clarification on notification message | 15.2.0 |
| 06-2018 | SP#80 | SP-180477 | 0250 | - | D | Editorial correction in clause 5.9.2 Subscription Permanent Identifier | 15.2.0 |
| 06-2018 | SP#80 | SP-180481 | 0251 | 8 | F | Correction to DNN subscription | 15.2.0 |
| 06-2018 | SP#80 | SP-180481 | 0254 | 4 | F | Clarification on the support of Delay Critical resource type | 15.2.0 |
| 06-2018 | SP#80 | SP-180486 | 0255 | 7 | F | Network slicing clause cleanup | 15.2.0 |
| 06-2018 | SP#80 | SP-180490 | 0261 | 1 | F | UE and network shall override the Core Network type restriction for regulatory prioritized services | 15.2.0 |
| 06-2018 | SP#80 | SP-180481 | 0262 | 1 | F | Clarification to the usage of Internal-Group Identifier | 15.2.0 |
| 06-2018 | SP#80 | SP-180484 | 0264 | 5 | F | Different types of Ethernet services and N4 | 15.2.0 |
| 06-2018 | SP#80 | SP-180487 | 0265 | 3 | F | Providing AF with information on the N6 User Plane tunnelling information | 15.2.0 |
| 06-2018 | SP#80 | SP-180488 | 0266 | 4 | F | SMF getting UE location from the AMF for NPLI when no QoS Flow to create/Update/modify | 15.2.0 |
| 06-2018 | SP#80 | SP-180487 | 0267 | - | F | Removal of network restriction for eight concurrent S-NSSAIs when serving a UE | 15.2.0 |
| 06-2018 | SP#80 | SP-180487 | 0268 | - | F | Removal of duplicated requirements for Allowed/Configured NSSAI | 15.2.0 |
| 06-2018 | SP#80 | SP-180482 | 0269 | 2 | F | Correction to AMF and S-NSSAI overload control | 15.2.0 |
| 06-2018 | SP#80 | SP-180478 | 0270 | - | F | AMF Name and AMF N2AP UE ID | 15.2.0 |
| 06-2018 | SP#80 | SP-180482 | 0271 | 2 | F | Correction for support of the Ethernet Type PDU Session | 15.2.0 |
| 06-2018 | SP#80 | SP-180484 | 0272 | 1 | F | Correction on aspects for LADN | 15.2.0 |
| 06-2018 | SP#80 | SP-180489 | 0273 | 1 | F | Subscription status notification for Event Exposure service | 15.2.0 |
| 06-2018 | SP#80 | SP-180480 | 0275 | 1 | F | Clarification on SMF selection | 15.2.0 |
| 06-2018 | SP#80 | SP-180480 | 0276 | 2 | F | Clarification on SMSF selection | 15.2.0 |
| 06-2018 | SP#80 | SP-180490 | 0280 | 1 | F | Update for providing policy requirements to multiple UEs | 15.2.0 |
| 06-2018 | SP#80 | SP-180481 | 0282 | 2 | F | Clarifying handling of reachability state | 15.2.0 |
| 06-2018 | SP#80 | SP-180484 | 0283 | 6 | F | Dual Registration mode of operation from E-UTRA cell connecting to both EPC and 5GC | 15.2.0 |
| 06-2018 | SP#80 | SP-180482 | 0284 | 2 | F | Consolidation of UE Network Capabilities | 15.2.0 |
| 06-2018 | SP#80 | SP-180486 | 0285 | 1 | F | NAS level congestion control for emergency and high priority access | 15.2.0 |
| 06-2018 | SP#80 | SP-180476 | 0286 | 1 | C | Coexistence of RRC Inactive and Dual Connectivity | 15.2.0 |
| 06-2018 | SP#80 | SP-180486 | 0287 | 3 | F | Mapped parameters in case of No N26 | 15.2.0 |
| 06-2018 | SP#80 | SP-180481 | 0289 | 2 | F | Clarification on the use of shared AMF Pointer value | 15.2.0 |
| 06-2018 | SP#80 | SP-180488 | 0290 | 1 | F | ReAuthentication by an external DN-AAA server | 15.2.0 |
| 06-2018 | SP#80 | SP-180484 | 0292 | 6 | F | LADN configuration of UE | 15.2.0 |
| 06-2018 | SP#80 | SP-180479 | 0295 | 1 | F | Clarification of S-NSSAI based congestion control | 15.2.0 |
| 06-2018 | SP#80 | SP-180478 | 0296 | 4 | F | Add indication of Notification Control to QoS rules sent to UE | 15.2.0 |
| 06-2018 | SP#80 | SP-180485 | 0297 | 1 | F | Local deactivate MICO for emergency service | 15.2.0 |
| 06-2018 | SP#80 | SP-180484 | 0298 | 4 | F | How the SMF validates UE location when requested for LADN PDU Session establishment | 15.2.0 |
| 06-2018 | SP#80 | SP-180479 | 0302 | 1 | F | AUSF clarification and alignment | 15.2.0 |
| 06-2018 | SP#80 | SP-180477 | 0303 | - | D | Correction to references | 15.2.0 |
| 06-2018 | SP#80 | SP-180480 | 0304 | 3 | F | Clarification on N3GPP TAI | 15.2.0 |
| 06-2018 | SP#80 | SP-180482 | 0305 | 6 | F | Correction on capability negotiation on "SMS over NAS" | 15.2.0 |
| 06-2018 | SP#80 | SP-180478 | 0306 | 1 | F | Alignment of the name of the network function | 15.2.0 |
| 06-2018 | SP#80 | SP-180482 | 0308 | 3 | F | Correction on NAS level congestion control | 15.2.0 |
| 06-2018 | SP#80 | SP-180479 | 0310 | 2 | F | Clarification on AMF management | 15.2.0 |
| 06-2018 | SP#80 | SP-180488 | 0311 | 4 | F | S-NSSAI check for activation of UP connection of PDU Session | 15.2.0 |
| 06-2018 | SP#80 | SP-180481 | 0313 | 3 | F | Clarifications required resulting from 6-bit QFI limit | 15.2.0 |
| 06-2018 | SP#80 | SP-180486 | 0314 | 1 | F | Missing "redirection" to E-UTRA connected to 5GC | 15.2.0 |
| 06-2018 | SP#80 | SP-180479 | 0319 | 1 | F | Clarification of high priority access | 15.2.0 |
| 06-2018 | SP#80 | SP-180476 | 0323 | 3 | F | Dual connectivity support for network slices | 15.2.0 |
| 06-2018 | SP#80 | SP-180481 | 0325 | - | F | Clarification to the NRF Roaming architecture | 15.2.0 |
| 06-2018 | SP#80 | SP-180488 | 0326 | 2 | F | Slicing information and RFSP | 15.2.0 |
| 06-2018 | SP#80 | SP-180490 | 0327 | - | F | TS 23.501: UE DL Signalling handling in RRC Inactive State | 15.2.0 |
| 06-2018 | SP#80 | SP-180489 | 0331 | 1 | F | Some TADs fix's | 15.2.0 |
| 06-2018 | SP#80 | SP-180485 | 0334 | 1 | F | Handling of maximum supported data rate per UE for integrity protection | 15.2.0 |
| 06-2018 | SP#80 | SP-180486 | 0335 | - | F | NF/NF service registration and status subscribe/notify description updates | 15.2.0 |
| 06-2018 | SP#80 | SP-180491 | 0336 | 1 | F | Use of results of NF/NF service discovery for NF/NF service selection | 15.2.0 |
| 06-2018 | SP#80 | SP-180489 | 0338 | 4 | F | Subscribed SMSF address | 15.2.0 |
| 06-2018 | SP#80 | SP-180488 | 0339 | - | F | SEPP fully redundant and next-hop IPX proxy | 15.2.0 |
| 06-2018 | SP#80 | SP-180488 | 0342 | 1 | F | SMF selection factor | 15.2.0 |
| 06-2018 | SP#80 | SP-180485 | 0344 | - | F | IPsec SAs in tunnel mode | 15.2.0 |
| 06-2018 | SP#80 | SP-180484 | 0345 | 1 | F | Determining interworking support for PDU sessions in case of interworking without N26 | 15.2.0 |
| 06-2018 | SP#80 | SP-180485 | 0346 | 1 | F | Fixing the definition of signalled QoS rule | 15.2.0 |
| 06-2018 | SP#80 | SP-180481 | 0349 | 2 | F | Clarify GUTI aspects for single-registration mode UEs for interworking without N26 | 15.2.0 |
| 06-2018 | SP#80 | SP-180486 | 0351 | - | F | N9 missing in some figures | 15.2.0 |
| 06-2018 | SP#80 | SP-180486 | 0352 | 2 | F | NF instance and NF service instance definitions | 15.2.0 |
| 06-2018 | SP#80 | SP-180483 | 0353 | 2 | F | Correction to UE Radio Capability handling | 15.2.0 |
| 06-2018 | SP#80 | SP-180485 | 0355 | 1 | F | Further QoS clean-up | 15.2.0 |
| 06-2018 | SP#80 | SP-180482 | 0356 | 1 | F | Coordination of reference point allocation | 15.2.0 |
| 06-2018 | SP#80 | SP-180485 | 0359 | 2 | F | Handling of Configured NSSAIs in Roaming Scenarios - 23.501 | 15.2.0 |
| 06-2018 | SP#80 | SP-180490 | 0363 | 1 | F | Update and correction of table for AMF, UDM, UDR, NSSF, UDSF and BSF services | 15.2.0 |
| 06-2018 | SP#80 | SP-180490 | 0365 | 1 | F | Update of FAR | 15.2.0 |
| 06-2018 | SP#80 | SP-180486 | 0367 | 1 | F | NEF Services | 15.2.0 |
| 06-2018 | SP#80 | SP-180477 | 0368 | 2 | D | Editor's note clean-up | 15.2.0 |
| 06-2018 | SP#80 | SP-180482 | 0370 | 3 | F | Compute - Storage split principles | 15.2.0 |
| 06-2018 | SP#80 | SP-180484 | 0371 | - | F | Emergency Services Fallback Support indicator validity in the Registration Area | 15.2.0 |
| 06-2018 | SP#80 | SP-180485 | 0372 | - | F | LMF Services | 15.2.0 |
| 06-2018 | SP#80 | SP-180490 | 0375 | 2 | F | UDM-AUSF Discovery | 15.2.0 |
| 06-2018 | SP#80 | SP-180481 | 0383 | 2 | F | Clarification on usage of PLMN ID received via PCO during PDN connection establishment | 15.2.0 |
| 06-2018 | SP#80 | SP-180483 | 0385 | - | F | Correction to the mapping to the Subscribed S-NSSAI(s) | 15.2.0 |
| 06-2018 | SP#80 | SP-180487 | 0386 | 2 | F | Provisioning NSSP | 15.2.0 |
| 06-2018 | SP#80 | SP-180489 | 0389 | 1 | F | Tracking Area in 5GS | 15.2.0 |
| 06-2018 | SP#80 | SP-180483 | 0390 | 1 | F | Correction to S-NSSAI congestion | 15.2.0 |
| 06-2018 | SP#80 | SP-180481 | 0391 | 1 | F | Clarification to PDU Session Types: MTU | 15.2.0 |
| 06-2018 | SP#80 | SP-180478 | 0394 | 3 | F | Alignment of radio capabilities procedure | 15.2.0 |
| 06-2018 | SP#80 | SP-180482 | 0396 | 2 | F | CN type indicator in AS signalling | 15.2.0 |
| 06-2018 | SP#80 | SP-180483 | 0397 | 1 | F | Correction to eCall Support by NR | 15.2.0 |
| 06-2018 | SP#80 | SP-180479 | 0398 | 1 | F | Bit rate enforcement | 15.2.0 |
| 06-2018 | SP#80 | SP-180480 | 0399 | - | F | Clarification on TAC format at inter-system handover | 15.2.0 |
| 06-2018 | SP#80 | SP-180478 | 0401 | 1 | F | Add table of CHF Spending Limit Control service in 7.2.x | 15.2.0 |
| 06-2018 | SP#80 | SP-180488 | 0402 | 2 | F | S-NSSAI of VPLMN when HO from 4G to 5G | 15.2.0 |
| 06-2018 | SP#80 | SP-180489 | 0403 | - | F | SSC Mode Selection clarification | 15.2.0 |
| 06-2018 | SP#80 | SP-180485 | 0404 | 1 | F | How Peer CP NF sends notification to target/new AMF after AMF planned removal | 15.2.0 |
| 06-2018 | SP#80 | SP-180478 | 0405 | 1 | F | AF influence on traffic routing for Ethernet type PDU Session | 15.2.0 |
| 06-2018 | SP#80 | SP-180479 | 0406 | 2 | F | Avoid the case the one UE MAC shared by multiple Ethernet PDU Sessions | 15.2.0 |
| 06-2018 | SP#80 | SP-180485 | 0407 | 1 | F | How AMF provides LADN Information to UE | 15.2.0 |
| 06-2018 | SP#80 | SP-180477 | 0410 | - | D | Non-3GPP access node selection information | 15.2.0 |
| 06-2018 | SP#80 | SP-180496 | 0411 | - | F | Clarify RAT restrictions are not provided to the UE | 15.2.0 |
| 06-2018 | SP#80 | SP-180485 | 0414 | 1 | F | Including GUAMI in RRC message of related procedures | 15.2.0 |
| 06-2018 | SP#80 | SP-180479 | 0415 | 1 | F | Clarification on CN assistance information | 15.2.0 |
| 06-2018 | SP#80 | SP-180481 | 0416 | 2 | F | Clarify the relationship between GFBR and MDBV | 15.2.0 |
| 06-2018 | SP#80 | SP-180480 | 0417 | 2 | F | Clarification on support of MFBR greater than GFBR | 15.2.0 |
| 06-2018 | SP#80 | SP-180480 | 0418 | 1 | F | Clarification on requested NSSAI usage by RAN | 15.2.0 |
| 06-2018 | SP#80 | SP-180480 | 0422 | - | F | Clarification on SMSF checking subscription data | 15.2.0 |
| 06-2018 | SP#80 | SP-180488 | 0423 | - | F | S-NSSAI back off timer for UE requested PDU session release | 15.2.0 |
| 06-2018 | SP#80 | SP-180479 | 0424 | 2 | F | Clarification on AF influence on traffic routing | 15.2.0 |
| 06-2018 | SP#80 | SP-180482 | 0425 | 2 | F | Combined SMF+PGW-C Selection | 15.2.0 |
| 06-2018 | SP#80 | SP-180488 | 0430 | - | F | Resume procedure in the equivalent PLMN | 15.2.0 |
| 06-2018 | SP#80 | SP-180478 | 0433 | - | F | Alignment of selective activation of UP connection of existing PDU Session | 15.2.0 |
| 06-2018 | SP#80 | SP-180478 | 0435 | 1 | F | Alignment of PCF selection description | 15.2.0 |
| 06-2018 | SP#80 | SP-180487 | 0436 | 4 | F | QNC during Handover | 15.2.0 |
| 06-2018 | SP#80 | SP-180487 | 0437 | 3 | F | Reflective QoS in interworking | 15.2.0 |
| 06-2018 | SP#80 | SP-180491 | 0438 | 2 | F | Use of Network Instance | 15.2.0 |
| 06-2018 | SP#80 | SP-180490 | 0439 | 3 | F | Update of N4 Parameter Descriptions and Tables | 15.2.0 |
| 06-2018 | SP#80 | SP-180480 | 0441 | 3 | F | Clarification on LADN 5.6.5 | 15.2.0 |
| 06-2018 | SP#80 | SP-180486 | 0444 | 3 | F | Network slicing subsription change and update of UE configuration | 15.2.0 |
| 06-2018 | SP#80 | SP-180479 | 0446 | 2 | F | Clarification note on Network Slice limitation | 15.2.0 |
| 06-2018 | SP#80 | SP-180478 | 0447 | 1 | F | Adding default value for Averaging Window | 15.2.0 |
| 06-2018 | SP#80 | SP-180486 | 0448 | 1 | F | Mobility restrictions | 15.2.0 |
| 06-2018 | SP#80 | SP-180479 | 0451 | 2 | F | Capturing subsequent mobility to and from GERAN/UTRAN | 15.2.0 |
| 06-2018 | SP#80 | SP-180485 | 0453 | - | F | GFBR is applicable only for GBR QoS Flows | 15.2.0 |
| 06-2018 | SP#80 | SP-180556 | 0454 | 2 | F | NSSAI handling in PDU Session Establishment procedures in roaming | 15.2.0 |
| 06-2018 | SP#80 | SP-180483 | 0456 | 1 | F | Correction to identifiers in Registration procedure | 15.2.0 |
| 06-2018 | SP#80 | SP-180487 | 0459 | 1 | F | Radio capabilities after 5GS registration | 15.2.0 |
| 09-2018 | SP#81 | SP-180713 | 0455 | 3 | F | Storage of structured proprietory data in UDSF | 15.3.0 |
| 09-2018 | SP#81 | SP-180713 | 0460 | 3 | F | Missing TADs behaviour | 15.3.0 |
| 09-2018 | SP#81 | SP-180713 | 0463 | - | F | Correcting handling of RAT restriction and Forbidden Areas | 15.3.0 |
| 09-2018 | SP#81 | SP-180713 | 0464 | 3 | F | Clarification on LADN | 15.3.0 |
| 09-2018 | SP#81 | SP-180713 | 0465 | 3 | F | Clarification on a wildcard DNN | 15.3.0 |
| 09-2018 | SP#81 | SP-180713 | 0466 | 3 | F | Correcting use of identifiers during registration in equivalent PLMNs | 15.3.0 |
| 09-2018 | SP#81 | SP-180713 | 0470 | 1 | F | Clarification on UE context exchanged on N26 interface | 15.3.0 |
| 09-2018 | SP#81 | SP-180713 | 0471 | 1 | F | Correction to AF influence on traffic routing | 15.3.0 |
| 09-2018 | SP#81 | SP-180713 | 0472 | 2 | F | Clarification on UE Registration type with only PDU Session for Emergency Services | 15.3.0 |
| 09-2018 | SP#81 | SP-180713 | 0473 | 7 | F | The resource type of QoS Flow associated with the default QoS rule | 15.3.0 |
| 09-2018 | SP#81 | SP-180724 | 0474 | 5 | B | Support of tracing in 5GS signalling: overview | 15.3.0 |
| 09-2018 | SP#81 | SP-180713 | 0475 | - | F | MCC implementation correction of 23.501 CR0255R7 | 15.3.0 |
| 09-2018 | SP#81 | SP-180713 | 0480 | 3 | F | 5QI-QCI alignment | 15.3.0 |
| 09-2018 | SP#81 | SP-180713 | 0481 | 2 | F | Number of packet filters supported by UE | 15.3.0 |
| 09-2018 | SP#81 | SP-180713 | 0482 | 2 | F | Paging policy differentiation for RRC inactive | 15.3.0 |
| 09-2018 | SP#81 | SP-180713 | 0485 | 4 | F | Application detection report when the PFDs are removed | 15.3.0 |
| 09-2018 | SP#81 | SP-180713 | 0487 | 5 | F | Correction to Configured NSSAI for the HPLMN | 15.3.0 |
| 09-2018 | SP#81 | SP-180713 | 0488 | 1 | F | Correction to TAI list generation | 15.3.0 |
| 09-2018 | SP#81 | SP-180713 | 0493 | 1 | F | Network Exposure in Roaming Situations | 15.3.0 |
| 09-2018 | SP#81 | SP-180713 | 0494 | 1 | F | Handling of UP Security Policy when IWK with EPS | 15.3.0 |
| 09-2018 | SP#81 | SP-180713 | 0497 | 2 | F | Clarification on handling of Ethernet frames at UPF | 15.3.0 |
| 09-2018 | SP#81 | SP-180713 | 0498 | 4 | F | Completion of description on Configured NSSAIs | 15.3.0 |
| 09-2018 | SP#81 | SP-180713 | 0499 | - | F | LADN Clarification | 15.3.0 |
| 09-2018 | SP#81 | SP-180713 | 0500 | 1 | F | DNN Usage Clarification | 15.3.0 |
| 09-2018 | SP#81 | SP-180713 | 0501 | 4 | F | Clarification for pre-configured QoS rule | 15.3.0 |
| 09-2018 | SP#81 | SP-180714 | 0502 | 1 | F | Clarification for QoS handling at UPF | 15.3.0 |
| 09-2018 | SP#81 | SP-180714 | 0504 | 3 | F | DL signalling handling for non-3GPP PDU Session | 15.3.0 |
| 09-2018 | SP#81 | SP-180714 | 0508 | 2 | F | Emergency call and eCall support when the ng-eNode is connected to EPC and 5GC | 15.3.0 |
| 09-2018 | SP#81 | SP-180714 | 0509 | 1 | F | Mobility Restriction List clean up | 15.3.0 |
| 09-2018 | SP#81 | SP-180714 | 0515 | 1 | F | Subscription of selecting the same SMF and UPF | 15.3.0 |
| 09-2018 | SP#81 | SP-180714 | 0516 | 3 | F | GUAMI Definition Correction | 15.3.0 |
| 09-2018 | SP#81 | SP-180714 | 0518 | 1 | F | Merging Network Slice with regular EPS Interworking | 15.3.0 |
| 09-2018 | SP#81 | SP-180714 | 0520 | 2 | F | Notification Control applicability | 15.3.0 |
| 09-2018 | SP#81 | SP-180714 | 0521 | 1 | F | 23.501: 5G AN Parameters sent during Service Request | 15.3.0 |
| 09-2018 | SP#81 | SP-180714 | 0524 | - | F | Null interworking with GERAN/UTRAN CS domain | 15.3.0 |
| 09-2018 | SP#81 | SP-180714 | 0525 | - | F | Correction on mobility management back-off timer | 15.3.0 |
| 09-2018 | SP#81 | SP-180714 | 0527 | - | F | 5G-TMSI should map to M-TMSI | 15.3.0 |
| 09-2018 | SP#81 | SP-180714 | 0529 | 1 | F | Clarification on Homogeneous Support of IMS Voice over PS Sessions indication | 15.3.0 |
| 09-2018 | SP#81 | SP-180714 | 0530 | 3 | F | Clarification on the non-IP PDU session type for EPS to 5GS interworking | 15.3.0 |
| 09-2018 | SP#81 | SP-180714 | 0531 | 2 | F | Clarification on the PDU session handling in EPS to 5GS handover with N26 | 15.3.0 |
| 09-2018 | SP#81 | SP-180714 | 0532 | 1 | F | Incorrect text implying slicing is optional | 15.3.0 |
| 09-2018 | SP#81 | SP-180714 | 0533 | - | F | Update of SMSF selection function | 15.3.0 |
| 09-2018 | SP#81 | SP-180714 | 0534 | 1 | F | Corrections to NF profile description | 15.3.0 |
| 09-2018 | SP#81 | SP-180714 | 0535 | 1 | F | Corrections to NF services names and references | 15.3.0 |
| 09-2018 | SP#81 | SP-180714 | 0536 | - | F | Update on AUSF service operation to support Steering of Roaming | 15.3.0 |
| 09-2018 | SP#81 | SP-180714 | 0538 | 3 | F | Correction to interworking with EPC with N3GPP PDU Sessions | 15.3.0 |
| 09-2018 | SP#81 | SP-180714 | 0539 | 3 | F | Emergency Services Support indicator for non-3GPP access | 15.3.0 |
| 09-2018 | SP#81 | SP-180714 | 0540 | 1 | F | Clarification of the AMF Set definition | 15.3.0 |
| 09-2018 | SP#81 | SP-180714 | 0542 | 1 | F | Clarification on priority service | 15.3.0 |
| 09-2018 | SP#81 | SP-180715 | 0543 | 1 | F | Unified Access Control for UE configured for EAB | 15.3.0 |
| 09-2018 | SP#81 | SP-180715 | 0544 | 2 | F | UE configuration of NSSAI and associated mapping | 15.3.0 |
| 09-2018 | SP#81 | SP-180715 | 0545 | - | F | Corrections to NEF functionalities description | 15.3.0 |
| 09-2018 | SP#81 | SP-180715 | 0546 | 2 | F | Update of N4 Parameter Descriptions and Tables/ Ethernet PDU Session Type | 15.3.0 |
| 09-2018 | SP#81 | SP-180715 | 0547 | 1 | F | Miscellaneous Corrections to SM specifications (SSC mode, PCFP reference, etc.) | 15.3.0 |
| 09-2018 | SP#81 | SP-180715 | 0548 | 2 | F | Specify AUSF selection by UDM | 15.3.0 |
| 09-2018 | SP#81 | SP-180715 | 0551 | - | F | Obsolete reference to Lawful Interception specifications | 15.3.0 |
| 09-2018 | SP#81 | SP-180715 | 0555 | 2 | F | Clearification on UE's configuraiton update | 15.3.0 |
| 09-2018 | SP#81 | SP-180715 | 0558 | 2 | F | Corrections to AF influence (5.6.7) based on CT WG3 LS on AF influence on traffic routing | 15.3.0 |
| 09-2018 | SP#81 | SP-180715 | 0559 | 2 | F | Alignment with CT WG1 on the QoS Flow Description | 15.3.0 |
| 09-2018 | SP#81 | SP-180715 | 0562 | - | F | UDM procedures in EPS-5GS interworking without N26 | 15.3.0 |
| 09-2018 | SP#81 | SP-180715 | 0563 | - | F | Update of NEF service table (7.2.8) for Chargeable party and AFsessionWithQoS | 15.3.0 |
| 09-2018 | SP#81 | SP-180715 | 0564 | 1 | F | Radio Capabilities for DRM in emergency services | 15.3.0 |
| 09-2018 | SP#81 | SP-180715 | 0565 | 3 | F | Selection of S-NSSAIs used in the Requested NSSAI | 15.3.0 |
| 09-2018 | SP#81 | SP-180715 | 0566 | 3 | F | Temporary identifier usage at interworking | 15.3.0 |
| 09-2018 | SP#81 | SP-180715 | 0567 | 1 | F | Temporary identifier coordination | 15.3.0 |
| 09-2018 | SP#81 | SP-180715 | 0569 | 1 | F | Updating radio capabilities from RRC_Inactive | 15.3.0 |
| 09-2018 | SP#81 | SP-180715 | 0573 | 1 | F | SMS support used in different meanings | 15.3.0 |
| 09-2018 | SP#81 | SP-180715 | 0575 | - | F | Exposure function reference correction | 15.3.0 |
| 09-2018 | SP#81 | SP-180715 | 0583 | 3 | F | Consistent Description of 5QI | 15.3.0 |
| 09-2018 | SP#81 | SP-180715 | 0584 | - | F | Corrections to N4 and UP tunnel protocol descriptions | 15.3.0 |
| 09-2018 | SP#81 | SP-180715 | 0585 | 1 | F | Handling of pending DL NAS signalling (related to LS In S2-187632) | 15.3.0 |
| 09-2018 | SP#81 | SP-180715 | 0586 | - | F | Alignment of Slice Selection logic in the AMF and NSSF | 15.3.0 |
| 09-2018 | SP#81 | SP-180715 | 0587 | 3 | F | Missing requirements to trigger Notification Control | 15.3.0 |
| 09-2018 | SP#81 | SP-180716 | 0588 | 2 | F | OAuth2 Authorization Service | 15.3.0 |
| 09-2018 | SP#81 | SP-180716 | 0589 | 2 | F | Clarification of the service area restriction and NSSAIs to EPLMNs | 15.3.0 |
| 09-2018 | SP#81 | SP-180716 | 0591 | 1 | F | 23.501: Reference Point and Services correction | 15.3.0 |
| 09-2018 | SP#81 | SP-180716 | 0592 | 1 | F | 23.501: UDM Services | 15.3.0 |
| 09-2018 | SP#81 | SP-180716 | 0593 | 2 | F | 23.501: Subscription for EPS IWK | 15.3.0 |
| 09-2018 | SP#81 | SP-180716 | 0594 | - | F | 23.501: AUSF, UDM, UDR Discovery | 15.3.0 |
| 09-2018 | SP#81 | SP-180716 | 0595 | 2 | F | Voice centric UE behaviour in non-allowed area | 15.3.0 |
| 09-2018 | SP#81 | SP-180716 | 0597 | 5 | F | Update to PCF discovery and selection | 15.3.0 |
| 09-2018 | SP#81 | SP-180716 | 0598 | 3 | F | Clarification to IMS emergency procedure | 15.3.0 |
| 09-2018 | SP#81 | SP-180716 | 0604 | 1 | F | Clarification on reporting of PS Data Off status change | 15.3.0 |
| 09-2018 | SP#81 | SP-180716 | 0605 | 4 | F | TAI List provision to RAN by AMF for RRC Inactive UE | 15.3.0 |
| 09-2018 | SP#81 | SP-180716 | 0606 | 2 | F | Clarifications for signalled QoS characteristics | 15.3.0 |
| 09-2018 | SP#81 | SP-180716 | 0608 | 1 | F | IPv6 multi-homed routing rule | 15.3.0 |
| 09-2018 | SP#81 | SP-180716 | 0609 | 1 | F | Clarification on priority of URSP and configuration of association between application and LADN DNN | 15.3.0 |
| 09-2018 | SP#81 | SP-180716 | 0616 | 2 | F | Update N4 principles and parameters | 15.3.0 |
| 09-2018 | SP#81 | SP-180716 | 0617 | - | F | Clarification on NF profile parameters | 15.3.0 |
| 09-2018 | SP#81 | SP-180716 | 0618 | - | F | Update to service area restriction | 15.3.0 |
| 09-2018 | SP#81 | SP-180791 | 0611 | 3 | F | Clarification on the AMF store the DNN and PGW-C+SMF to UDM/HSS without N26. | 15.3.0 |
| 2018-12 | SP#82 | SP-181084 | 0576 | 6 | F | CHF discovery and selection | 15.4.0 |
| 2018-12 | SP#82 | SP-181085 | 0590 | 2 | F | Clarification to the slice based congestion control handling at NG-RAN | 15.4.0 |
| 2018-12 | SP#82 | SP-181085 | 0607 | 11 | F | Clarifications for 5QI priority level | 15.4.0 |
| 2018-12 | SP#82 | SP-181090 | 0621 | 2 | F | Using preconfigured 5QI for QoS Flow associated with the default QoS rule | 15.4.0 |
| 2018-12 | SP#82 | SP-181090 | 0622 | 3 | F | Update of Default Configured NSSAI | 15.4.0 |
| 2018-12 | SP#82 | SP-181086 | 0625 | 2 | F | Clarifying the boundaries of an NF instance | 15.4.0 |
| 2018-12 | SP#82 | SP-181086 | 0626 | - | F | Correcting discovery and selection | 15.4.0 |
| 2018-12 | SP#82 | SP-181089 | 0628 | 3 | F | Reporting PS Data Off status change when SM back off timer is running | 15.4.0 |
| 2018-12 | SP#82 | SP-181086 | 0629 | 1 | F | Correction of the indication of UE 5GSM capabilities after intersystem change | 15.4.0 |
| 2018-12 | SP#82 | SP-181090 | 0630 | 1 | F | UE unable to use N3IWF identifier configuration in stand-alone N3IWF selection | 15.4.0 |
| 2018-12 | SP#82 | SP-181089 | 0633 | 2 | F | Removal of Editor's Note re mandatoriness of RRC_Inactive | 15.4.0 |
| 2018-12 | SP#82 | SP-181084 | 0634 | 3 | F | Avoiding mandatory MME impacts from 3-byte TAC | 15.4.0 |
| 2018-12 | SP#82 | SP-181084 | 0637 | 1 | F | Alignment of NF Profile with adding priority parameter | 15.4.0 |
| 2018-12 | SP#82 | SP-181084 | 0638 | 2 | F | Clarification on RQ Timer | 15.4.0 |
| 2018-12 | SP#82 | SP-181088 | 0639 | 2 | F | Interactions with PCF - Updates to reference architecure for interworking | 15.4.0 |
| 2018-12 | SP#82 | SP-181089 | 0641 | 1 | F | Registration Area and Service Restriction Area in relation to multiple PLMNs | 15.4.0 |
| 2018-12 | SP#82 | SP-181086 | 0645 | 1 | F | Correcting the interaction needed for the NSSF service | 15.4.0 |
| 2018-12 | SP#82 | SP-181086 | 0648 | - | F | Connections on Default Configured NSSAI | 15.4.0 |
| 2018-12 | SP#82 | SP-181086 | 0651 | 1 | F | Correction and clarification for CM-CONNECTED with RRC Inactive state | 15.4.0 |
| 2018-12 | SP#82 | SP-181089 | 0653 | 2 | F | SUPI definition and NAI format | 15.4.0 |
| 2018-12 | SP#82 | SP-181084 | 0655 | 1 | F | Addition of abbreviations | 15.4.0 |
| 2018-12 | SP#82 | SP-181088 | 0656 | 8 | F | Network controlled NSSAI for SR-related Access Stratum connection establishment | 15.4.0 |
| 2018-12 | SP#82 | SP-181195 | 0660 | 8 | F | Unified Access Control clarification and triggers | 15.4.0 |
| 2018-12 | SP#82 | SP-181087 | 0661 | 3 | B | Data Volume Reporting for Option 4/7 | 15.4.0 |
| 2018-12 | SP#82 | SP-181086 | 0662 | 4 | F | Configuration Transfer Procedure | 15.4.0 |
| 2018-12 | SP#82 | SP-181084 | 0666 | 3 | F | Avoiding overloading the target of AMF Load Re-Balancing | 15.4.0 |
| 2018-12 | SP#82 | SP-181090 | 0667 | 1 | F | UE storage of NSSAI and associated mapping | 15.4.0 |
| 2018-12 | SP#82 | SP-181085 | 0668 | 1 | F | Clarification of PS Voice Support for 3GPP and non-3GPP | 15.4.0 |
| 2018-12 | SP#82 | SP-181089 | 0669 | 1 | F | Secondary authentication update | 15.4.0 |
| 2018-12 | SP#82 | SP-181087 | 0671 | 1 | F | Emergency registration in a normally camped cell | 15.4.0 |
| 2018-12 | SP#82 | SP-181088 | 0672 | 1 | F | Priority indication over SBA interfaces via Message Priority header | 15.4.0 |
| 2018-12 | SP#82 | SP-181088 | 0675 | 3 | F | MME/AMF registration in HSS+UDM | 15.4.0 |
| 2018-12 | SP#82 | SP-181086 | 0676 | 1 | F | Completion of 5QI characteristics table | 15.4.0 |
| 2018-12 | SP#82 | SP-181086 | 0677 | - | F | Consistent usage of terminology in QoS notification control description | 15.4.0 |
| 2018-12 | SP#82 | SP-181084 | 0679 | 3 | F | Alignment for always-on PDU sessions | 15.4.0 |
| 2018-12 | SP#82 | SP-181089 | 0680 | 1 | C | PS Data Off supporting non-IP data packet | 15.4.0 |
| 2018-12 | SP#82 | SP-181089 | 0682 | 3 | F | Clarification on the PDU Session handover procedure with the User Plane Security Enforcement | 15.4.0 |
| 2018-12 | SP#82 | SP-181089 | 0683 | 1 | F | Clean up congestion control | 15.4.0 |
| 2018-12 | SP#82 | SP-181089 | 0685 | 3 | F | Correction on SSCMSP | 15.4.0 |
| 2018-12 | SP#82 | SP-181089 | 0686 | 4 | F | Clarification on the AMF store the DNN and PGW-C+SMF to UDM+HSS | 15.4.0 |
| 2018-12 | SP#82 | SP-181085 | 0687 | 1 | F | Clarification on NPLI for EPS Fallback | 15.4.0 |
| 2018-12 | SP#82 | SP-181087 | 0688 | 1 | F | Correction on UE inclusion of UE's usage setting | 15.4.0 |
| 2018-12 | SP#82 | SP-181090 | 0690 | 3 | F | UE radio capability for paging information with NR and eLTE connected to the CN | 15.4.0 |
| 2018-12 | SP#82 | SP-181087 | 0691 | 2 | F | Correction to traffic steering control | 15.4.0 |
| 2018-12 | SP#82 | SP-181090 | 0692 | - | F | Using TCP for reliable NAS transport between UE and N3IWF | 15.4.0 |
| 2018-12 | SP#82 | SP-181084 | 0693 | 1 | C | 5GS Support for MCS Subscription | 15.4.0 |
| 2018-12 | SP#82 | SP-181091 | 0695 | 1 | F | UE sending UE Integrity Protection Data Rate capability over any access | 15.4.0 |
| 2018-12 | SP#82 | SP-181087 | 0696 | 1 | F | Correction on Subscribed 5QI | 15.4.0 |
| 2018-12 | SP#82 | SP-181089 | 0699 | - | F | Selective deactivation for always-on PDU sessions | 15.4.0 |
| 2018-12 | SP#82 | SP-181091 | 0701 | 1 | F | Use of emergency DNN when Emergency Registered | 15.4.0 |
| 2018-12 | SP#82 | SP-181090 | 0703 | 3 | F | Requirements on 5G-TMSI randomness | 15.4.0 |
| 2018-12 | SP#82 | SP-181087 | 0707 | 1 | F | Emergency registration over two accesses | 15.4.0 |
| 2018-12 | SP#82 | SP-181090 | 0708 | 1 | F | Registration procedure with different Registration types | 15.4.0 |
| 2018-12 | SP#82 | SP-181088 | 0709 | 2 | F | EPS to 5GS with network slices | 15.4.0 |
| 2018-12 | SP#82 | SP-181084 | 0710 | 2 | F | AUSF and UDM selection | 15.4.0 |
| 2018-12 | SP#82 | SP-181089 | 0712 | 2 | F | Providing a threshold to UPF while waiting for quota | 15.4.0 |
| 2018-12 | SP#82 | SP-181088 | 0713 | 1 | F | Corrections to usage of IP index | 15.4.0 |
| 2018-12 | SP#82 | SP-181085 | 0716 | 2 | F | Clarification on OVERLOAD behaviour for the EUTRA connected to 5GC | 15.4.0 |
| 2018-12 | SP#82 | SP-181085 | 0719 | 2 | F | Clarification on Registration with AMF re-allocation | 15.4.0 |
| 2018-12 | SP#82 | SP-181089 | 0720 | 1 | F | PDN Disconnection handling | 15.4.0 |
| 2018-12 | SP#82 | SP-181084 | 0721 | 3 | F | Always on Setting for the EBI allocated PDU Session | 15.4.0 |
| 2018-12 | SP#82 | SP-181085 | 0722 | 2 | F | Clarification on packet filter handling | 15.4.0 |
| 2018-12 | SP#82 | SP-181086 | 0723 | 4 | F | Clarify for PDB of dynamically assigned 5QI | 15.4.0 |
| 2018-12 | SP#82 | SP-181091 | 0724 | 2 | F | Update the UCU procedure with operator-defined access category definitions | 15.4.0 |
| 2018-12 | SP#82 | SP-181087 | 0725 | - | F | Correction of VLAN ID | 15.4.0 |
| 2018-12 | SP#82 | SP-181085 | 0726 | 1 | F | Clarification on DN authorization data between PCF and SMF | 15.4.0 |
| 2018-12 | SP#82 | SP-181084 | 0730 | 2 | F | Addition of URRP-AMF definition | 15.4.0 |
| 2019-03 | SP#83 | SP-190154 | 0700 | 3 | F | Use of S-NSSAI at interworking from EPS to 5GS | 15.5.0 |
| 2019-03 | SP#83 | SP-190154 | 0733 | 2 | F | Slice interworking HR mode update | 15.5.0 |
| 2019-03 | SP#83 | SP-190154 | 0741 | 1 | F | UDR selection | 15.5.0 |
| 2019-03 | SP#83 | SP-190154 | 0742 | 2 | F | Fixing text related to discovery and selection | 15.5.0 |
| 2019-03 | SP#83 | SP-190154 | 0743 | 1 | F | Change of the term confidence level | 15.5.0 |
| 2019-03 | SP#83 | SP-190154 | 0756 | 2 | F | Correction to NSSAI logic | 15.5.0 |
| 2019-03 | SP#83 | SP-190154 | 0758 | 2 | F | UL Session-AMBR enforcement in UPF | 15.5.0 |
| 2019-03 | SP#83 | SP-190154 | 0759 | 1 | F | Alignment with stage 3 for EPS interworking indications | 15.5.0 |
| 2019-03 | SP#83 | SP-190154 | 0762 | 2 | F | Clarification of user plane security enforcement between NG-RAN and SMF in Dual Connectivity scenario | 15.5.0 |
| 2019-03 | SP#83 | SP-190154 | 0767 | 2 | F | QoS Notification Control during handover | 15.5.0 |
| 2019-03 | SP#83 | SP-190154 | 0773 | 1 | F | Correction to traffic steering control | 15.5.0 |
| 2019-03 | SP#83 | SP-190154 | 0774 | 3 | F | Configurable time for subsequent notification that the GFBR cannot be fulfilled | 15.5.0 |
| 2019-03 | SP#83 | SP-190154 | 0775 | 1 | F | Clarification for default values | 15.5.0 |
| 2019-03 | SP#83 | SP-190154 | 0784 | 4 | F | 5GC emergency calls over non-3GPP | 15.5.0 |
| 2019-03 | SP#83 | SP-190154 | 0786 | 1 | F | Adding UE Local Configuration as an additional option to the URSP | 15.5.0 |
| 2019-03 | SP#83 | SP-190154 | 0789 | - | F | Update of network slicing text on NSSAI inclusion in RRC | 15.5.0 |
| 2019-03 | SP#83 | SP-190154 | 0791 | 3 | C | Supporting early trace in AUSF | 15.5.0 |
| 2019-03 | SP#83 | SP-190154 | 0792 | 1 | F | IMS voice over PS Session Supported Indication in roaming cases. | 15.5.0 |
| 2019-03 | SP#83 | SP-190154 | 0793 | 2 | F | Introduce Charging Function in overall architecture | 15.5.0 |
| 2019-03 | SP#83 | SP-190155 | 0797 | 2 | F | Update of configured NSSAI handling | 15.5.0 |
| 2019-03 | SP#83 | SP-190155 | 0806 | 3 | F | Corrections to AMF overlad control procedure | 15.5.0 |
| 2019-03 | SP#83 | SP-190155 | 0808 | - | F | TS 23.501 Update to Network Slice availability | 15.5.0 |
| 2019-03 | SP#83 | SP-190155 | 0818 | - | F | No services defined for Ngmlc | 15.5.0 |
| 2019-03 | SP#83 | SP-190155 | 0824 | 6 | F | Clarification on DN authorization data | 15.5.0 |
| 2019-03 | SP#83 | SP-190155 | 0833 | - | F | Clarification on Establishing a PDU Session in a Network Slice | 15.5.0 |
| 2019-03 | SP#83 | SP-190155 | 0834 | 8 | F | Clarification on NAS level congestion control | 15.5.0 |
| 2019-03 | SP#83 | SP-190155 | 0853 | 6 | F | PS Data Off status update when congestion control is applied in AMF | 15.5.0 |
| 2019-03 | SP#83 | SP-190155 | 0857 | 1 | F | Correction to Mobility Restrictions (for non-3GPP access) | 15.5.0 |
| 2019-03 | SP#83 | SP-190155 | 0860 | 3 | F | Clarification on the UE behaviours under NAS level congestion control | 15.5.0 |
| 2019-03 | SP#83 | SP-190155 | 0875 | - | F | Permanent identifier with IMEISV format | 15.5.0 |
| 2019-03 | SP#83 | SP-190155 | 0876 | 2 | F | Removing a superfluous NOTE about the need for ultra-low latency QCI/5Qis | 15.5.0 |
| 2019-03 | SP#83 | SP-190155 | 0877 | 7 | F | Allowed Area and Non-Allowed Area encoding | 15.5.0 |
| 2019-03 | SP#83 | SP-190155 | 0901 | 2 | F | Alignment of Emergency Registered definition with Stage 3 | 15.5.0 |
| 2019-03 | SP#83 | SP-190155 | 0904 | - | F | Addition of PCF services Npcf_UEPolicyControl and Npcf_EventExposure | 15.5.0 |
| 2019-03 | SP#83 | SP-190155 | 0910 | 3 | F | Clarification on ARP Proxy | 15.5.0 |
| 2019-03 | SP#83 | SP-190155 | 0913 | 2 | F | PS Data Off status update when UE in non-allowed area or out of LADN area | 15.5.0 |
| 2019-03 | SP#83 | SP-190155 | 0915 | 2 | F | Non-roaming reference architecture correction | 15.5.0 |
| 2019-03 | SP#83 | SP-190155 | 0922 | 2 | F | TS 23.501: correction for enforcement of user plane integrity protection | 15.5.0 |
| 2019-03 | SP#83 | SP-190156 | 0932 | 2 | F | Clarification on the PDU Session parameter | 15.5.0 |
| 2019-03 | SP#83 | SP-190156 | 0942 | 2 | F | Transport Level Packet Marking | 15.5.0 |
| 2019-03 | SP#83 | SP-190156 | 0943 | 2 | F | Support of baseline Frame Routing feature | 15.5.0 |
| 2019-03 | SP#83 | SP-190156 | 0945 | 1 | F | Disabling E-UTRA connected to EPC radio capability | 15.5.0 |
| 2019-03 | SP#83 | SP-190156 | 0949 | 2 | F | Correction of slicing terminology | 15.5.0 |
| 2019-03 | SP#83 | SP-190156 | 0958 | 1 | F | Adding a new 5G-GUTI allocation condition | 15.5.0 |
| 2019-03 | SP#83 | SP-190156 | 0968 | 2 | F | Clarify on Network Slice availability change | 15.5.0 |
| 2019-03 | SP#83 | SP-190156 | 0969 | 2 | F | Correction the terms on Secondary authentication/authorization of the PDU Session Establishment | 15.5.0 |
| 2019-03 | SP#83 | SP-190156 | 0975 | 1 | F | Clarificaiton on Core Network type Restriction | 15.5.0 |
| 2019-03 | SP#83 | SP-190156 | 0976 | 3 | F | Clarification on AMF planned removal | 15.5.0 |
| 2019-03 | SP#83 | SP-190156 | 0979 | 1 | F | Correction of UE 5GSM Core Network Capability | 15.5.0 |
| 2019-03 | SP#83 | SP-190156 | 0982 | 2 | F | Clarification on QoS Notification control | 15.5.0 |
| 2019-03 | SP#83 | SP-190156 | 0988 | 0 | F | Correction on reference | 15.5.0 |
| 2019-03 | SP#83 | SP-190156 | 0992 | 3 | F | Slice interworking HR mode update | 15.5.0 |
| 2019-03 | SP#83 | SP-190156 | 0996 | 2 | F | Clarification on PCF selection | 15.5.0 |
| 2019-03 | SP#83 | SP-190156 | 1006 | - | F | Corrections on routing rule | 15.5.0 |
| 2019-03 | SP#83 | SP-190156 | 1012 | 2 | F | Clarification on GTP-u protocol | 15.5.0 |
| 2019-03 | SP#83 | SP-190175 | 0704 | 4 | C | New 5QIs for Enhanced Framework for Uplink Streaming | 16.0.0 |
| 2019-03 | SP#83 | SP-190169 | 0734 | 8 | B | TS 23.501: Introducing Non-public network | 16.0.0 |
| 2019-03 | SP#83 | SP-190169 | 0747 | 12 | B | Support for 5G LAN | 16.0.0 |
| 2019-03 | SP#83 | SP-190194 | 0757 | 8 | B | Introducing support for Non-Public Networks | 16.0.0 |
| 2019-03 | SP#83 | SP-190169 | 0903 | 2 | B | Introduction of 5G LAN-type service | 16.0.0 |
| 2019-03 | SP#83 | SP-190169 | 1007 | 2 | B | Introducing support TSC Deterministic QoS | 16.0.0 |
| 2019-03 | SP#83 | SP-190169 | 1008 | 2 | B | Introducing support Hold and Forward Buffers for TSC Deterministic QoS | 16.0.0 |
| 2019-03 | SP#83 | SP-190169 | 1002 | 3 | B | 5GS Logical TSN bridge management | 16.0.0 |
| 2019-03 | SP#83 | SP-190165 | 0748 | 3 | B | CIoT High Level Description in 23.501 | 16.0.0 |
| 2019-03 | SP#83 | SP-190165 | 0751 | 3 | B | High Latency Overall Description | 16.0.0 |
| 2019-03 | SP#83 | SP-190165 | 0752 | 4 | B | Introducing Rate Control for 5G CIoT | 16.0.0 |
| 2019-03 | SP#83 | SP-190165 | 0768 | 6 | B | Introduction of eDRX in 5GS | 16.0.0 |
| 2019-03 | SP#83 | SP-190165 | 0819 | 1 | B | CIoT Monitoring Events | 16.0.0 |
| 2019-03 | SP#83 | SP-190165 | 0820 | 4 | B | Restriction of use of Enhanced Coverage in 5GC | 16.0.0 |
| 2019-03 | SP#83 | SP-190165 | 0825 | 2 | B | Introduction to Reliable Data Service | 16.0.0 |
| 2019-03 | SP#83 | SP-190165 | 0889 | 7 | B | Introduction of data transfer in Control Plane CIoT 5GS Optimisation | 16.0.0 |
| 2019-03 | SP#83 | SP-190165 | 0890 | 6 | B | Introduction of NEF based infrequent small data transfer via NAS | 16.0.0 |
| 2019-03 | SP#83 | SP-190165 | 0893 | 7 | B | Introduction of Power Saving Functions for CIoT | 16.0.0 |
| 2019-03 | SP#83 | SP-190165 | 0894 | 5 | B | CIoT Introduction of Overload Control | 16.0.0 |
| 2019-03 | SP#83 | SP-190165 | 0895 | 2 | B | Introduction of Inter-RAT mobility support to and from NB-IoT | 16.0.0 |
| 2019-03 | SP#83 | SP-190165 | 0896 | 2 | B | CIoT Introduction of CN Selection and Steering | 16.0.0 |
| 2019-03 | SP#83 | SP-190165 | 1014 | 2 | B | Introduction of Service Gap Control | 16.0.0 |
| 2019-03 | SP#83 | SP-190173 | 0735 | 11 | B | Introduction of ATSSS Support | 16.0.0 |
| 2019-03 | SP#83 | SP-190173 | 0740 | 7 | B | Support of Steering Functions for ATSSS | 16.0.0 |
| 2019-03 | SP#83 | SP-190173 | 0770 | 4 | B | QoS for Multi-Access PDU Session | 16.0.0 |
| 2019-03 | SP#83 | SP-190173 | 0921 | 3 | B | Access Network Performance Measurements | 16.0.0 |
| 2019-03 | SP#83 | SP-190171 | 0810 | 2 | B | New clause for URLLC supporting | 16.0.0 |
| 2019-03 | SP#83 | SP-190171 | 0753 | 8 | B | General description of solution 1 in 23.725 for user plane redundancy | 16.0.0 |
| 2019-03 | SP#83 | SP-190171 | 0811 | 6 | B | Add description of solution 4 in 23.725 to 23.501 | 16.0.0 |
| 2019-03 | SP#83 | SP-190171 | 0872 | 3 | B | Description of solution 7 in 23.725 as replication framework | 16.0.0 |
| 2019-03 | SP#83 | SP-190164 | 0732 | 2 | B | ETSUN - Architecture conclusion | 16.0.0 |
| 2019-03 | SP#83 | SP-190164 | 0848 | 5 | B | UL CL/BP controlled by I-SMF | 16.0.0 |
| 2019-03 | SP#83 | SP-190175 | 0704 | 4 | C | New 5QIs for Enhanced Framework for Uplink Streaming | 16.0.0 |
| 2019-03 | SP#83 | SP-190171 | 0755 | 2 | B | Description of solution 11 in 23.725 for Ethernet anchor relocation | 16.0.0 |
| 2019-03 | SP#83 | SP-190169 | 0734 | 8 | B | Introducing Non-public network | 16.0.0 |
| 2019-03 | SP#83 | SP-190215 | 0736 | 10 | B | Introduction of indirect communication between NF services and implicit discovery | 16.0.0 |
| 2019-03 | SP#83 | SP-190167 | 0744 | 4 | B | SUPI and SUCI for wireline access | 16.0.0 |
| 2019-03 | SP#83 | SP-190167 | 0745 | 6 | B | Mobility restrictions for wireline access | 16.0.0 |
| 2019-03 | SP#83 | SP-190167 | 0746 | 2 | B | IP addressing enhancements | 16.0.0 |
| 2019-03 | SP#83 | SP-190169 | 0747 | 12 | B | Support for 5G LAN | 16.0.0 |
| 2019-03 | SP#83 | SP-190171 | 0754 | 2 | B | Description of solution 2 in 23.725 for redundancy as an informational annex | 16.0.0 |
| 2019-03 | SP#83 | SP-190173 | 0761 | 1 | B | ATSSS-SMF and UPF selection | 16.0.0 |
| 2019-03 | SP#83 | SP-190165 | 0776 | 3 | B | CIoT Introduction of extended DRX in CM-CONNECTED with RRC Inactive state | 16.0.0 |
| 2019-03 | SP#83 | SP-190167 | 0781 | 2 | B | Support of Trusted non-3GPP access | 16.0.0 |
| 2019-03 | SP#83 | SP-190167 | 0783 | 2 | B | Trusted non-3GPP Access Network Selection | 16.0.0 |
| 2019-03 | SP#83 | SP-190173 | 0785 | 5 | B | Updating 5.8.2.11 for N4 Rules to support ATSSS | 16.0.0 |
| 2019-03 | SP#83 | SP-190174 | 0799 | 10 | B | eSBA communication schemas related to general discovery and selection | 16.0.0 |
| 2019-03 | SP#83 | SP-190174 | 0800 | 3 | B | eSBA communication schemas related to UDM and UDR discovery and selection | 16.0.0 |
| 2019-03 | SP#83 | SP-190172 | 0940 | 3 | B | Use of analytics for SMF selection | 16.0.0 |
| 2019-03 | SP#83 | SP-190174 | 0801 | 7 | B | eSBA communication schemas related to SMF discovery and selection | 16.0.0 |
| 2019-03 | SP#83 | SP-190174 | 0802 | 3 | B | eSBA communication schemas related to PCF discovery and selection | 16.0.0 |
| 2019-03 | SP#83 | SP-190174 | 0803 | 5 | B | eSBA communication schemas related to AUSF discovery and selection | 16.0.0 |
| 2019-03 | SP#83 | SP-190174 | 0804 | 4 | B | eSBA communication schemas related to AMF discovery and selection | 16.0.0 |
| 2019-03 | SP#83 | SP-190165 | 0826 | 2 | B | Introduction of the MSISDN-less MO SMS Service | 16.0.0 |
| 2019-03 | SP#83 | SP-190165 | 0828 | 1 | B | Introduction of the SCEF+NEF | 16.0.0 |
| 2019-03 | SP#83 | SP-190172 | 0831 | 6 | B | CR for TS 23.501 based on conclusion of eNA TR 23.791 | 16.0.0 |
| 2019-03 | SP#83 | SP-190172 | 0837 | 3 | B | Use of NWDAF analytics for decision of MICO mode parameters | 16.0.0 |
| 2019-03 | SP#83 | SP-190169 | 0841 | 2 | B | FQDN format of N3IWF in a standalone non-public network | 16.0.0 |
| 2019-03 | SP#83 | SP-190168 | 0843 | 2 | F | Update to LCS related definitions | 16.0.0 |
| 2019-03 | SP#83 | SP-190238 | 0844 | 8 | B | Network reliability support with Sets | 16.0.0 |
| 2019-03 | SP#83 | SP-190199 | 0850 | 1 | B | Enhancement on slice interworking--501 | 16.0.0 |
| 2019-03 | SP#83 | SP-190162 | 0859 | 2 | B | Adding 5G SRVCC description to 23.501 | 16.0.0 |
| 2019-03 | SP#83 | SP-190167 | 0862 | 7 | B | UPF Selection influenced by the indication of the identity/identities of 5G AN N3 User Plane capability | 16.0.0 |
| 2019-03 | SP#83 | SP-190167 | 0863 | 8 | B | Architecture and reference points for Wireline AN | 16.0.0 |
| 2019-03 | SP#83 | SP-190167 | 0866 | 8 | B | Clarification of RM and CM for 5G-RG | 16.0.0 |
| 2019-03 | SP#83 | SP-190169 | 0870 | 3 | B | TSC definitions | 16.0.0 |
| 2019-03 | SP#83 | SP-190169 | 0871 | 4 | B | TSC Architecture | 16.0.0 |
| 2019-03 | SP#83 | SP-190174 | 0873 | 8 | B | eSBA communication schema co-existence | 16.0.0 |
| 2019-03 | SP#83 | SP-190170 | 0878 | 2 | B | NEF service for service specific parameter provisioning | 16.0.0 |
| 2019-03 | SP#83 | SP-190165 | 0886 | 5 | B | Introduction for solution 14 to key issue 9 | 16.0.0 |
| 2019-03 | SP#83 | SP-190171 | 0897 | 7 | B | Sol#6 specific updates to 5.6.4.2 | 16.0.0 |
| 2019-03 | SP#83 | SP-190165 | 0898 | 6 | B | External parameters provisioning to the 5GS | 16.0.0 |
| 2019-03 | SP#83 | SP-190172 | 0899 | 1 | B | Use of analytics for user plane function selection | 16.0.0 |
| 2019-03 | SP#83 | SP-190172 | 0900 | 1 | B | Use of analytics for UE mobility procedures | 16.0.0 |
| 2019-03 | SP#83 | SP-190169 | 0909 | 3 | B | Control of traffic forwarding in 5G-LAN | 16.0.0 |
| 2019-03 | SP#83 | SP-190165 | 0916 | 1 | B | User Plane Forwarding with Control Plane CIoT 5GS Optimisation | 16.0.0 |
| 2019-03 | SP#83 | SP-190174 | 0926 | 2 | B | Update the support of virtualized deployment with SCP distribution and the NF/NF service instance Set | 16.0.0 |
| 2019-03 | SP#83 | SP-190174 | 0927 | 1 | C | Update of NRF functionalities | 16.0.0 |
| 2019-03 | SP#83 | SP-190164 | 0931 | 2 | B | UE IP address Allocation by UPF: N4 impacts | 16.0.0 |
| 2019-03 | SP#83 | SP-190164 | 0933 | 1 | B | ETSUN - Conclusion alignment | 16.0.0 |
| 2019-03 | SP#83 | SP-190167 | 0934 | 2 | B | Support of full Frame Routing feature | 16.0.0 |
| 2019-03 | SP#83 | SP-190174 | 0941 | 4 | B | Location information | 16.0.0 |
| 2019-03 | SP#83 | SP-190164 | 0954 | 2 | B | Addition of UE IP address Allocation by UPF | 16.0.0 |
| 2019-03 | SP#83 | SP-190167 | 0961 | 1 | B | Protocol stack for W-5GAN support | 16.0.0 |
| 2019-03 | SP#83 | SP-190167 | 0962 | 3 | C | Session Management of 5G-RG/FN-RG connection to 5GC in the Wireline ANs | 16.0.0 |
| 2019-03 | SP#83 | SP-190172 | 0964 | 2 | B | NEF service for NWDAF analytics | 16.0.0 |
| 2019-03 | SP#83 | SP-190171 | 0972 | 3 | B | Add description of solution 13 in 23.725 to TS 23.501 | 16.0.0 |
| 2019-03 | SP#83 | SP-190167 | 0981 | 2 | B | Extension of the QoS model for wireline access | 16.0.0 |
| 2019-03 | SP#83 | SP-190172 | 0983 | 2 | B | Update of TS 23.501 for Rel.16 BDT Notification | 16.0.0 |
| 2019-03 | SP#83 | SP-190168 | 0984 | 2 | F | Update the description and the reference of LMF service | 16.0.0 |
| 2019-03 | SP#83 | SP-190172 | 0987 | 3 | B | CR for TS 23.501 Clarifications NWDAF Discovery and Selection | 16.0.0 |
| 2019-03 | SP#83 | SP-190171 | 0989 | 2 | B | Introduction of E2E PDB Division | 16.0.0 |
| 2019-03 | SP#83 | SP-190169 | 1003 | 2 | B | QoS parameters mapping between TSN characters and 5G QoS | 16.0.0 |
| 2019-03 | SP#83 | SP-190174 | 1010 | 3 | B | Introducing NF Set and NF Service Set | 16.0.0 |
| 2019-03 | SP#83 | SP-190175 | 1022 | 2 | B | Introduction of Dedicated Bearer for Ethernet support in EPC | 16.0.0 |
| 2019-04 | - | - | - | - | - | MCC correction of clause 5.29.3 (to 5.30.3) and position of clause 5.31.7.2. Editorial style and formatting corrections | 16.0.1 |
| 2019-04 | - | - | - | - | - | MCC correction swapping clause 5.28 to 5.29 and clause 5.29 to 5.28 for readability purposes | 16.0.2 |
| 2019-06 | SP#84 | SP-190407 | 0892 | 4 | B | Introduction of inter-UE QoS differentiation for NB-IoT using NB-IoT UE Priority | 16.1.0 |
| 2019-06 | SP#84 | SP-190407 | 1019 | 3 | B | Support of EPC interworking for CIoT Monitoring Events | 16.1.0 |
| 2019-06 | SP#84 | SP-190428 | 1028 | 1 | D | Proper naming of the reference point between two UPFs for direct routing | 16.1.0 |
| 2019-06 | SP#84 | SP-190416 | 1033 | 2 | B | Clarification on MA PDU session | 16.1.0 |
| 2019-06 | SP#84 | SP-190416 | 1034 | 5 | B | Determination of access availability | 16.1.0 |
| 2019-06 | SP#84 | SP-190419 | 1035 | 4 | B | NRF based P-CSCF discovery | 16.1.0 |
| 2019-06 | SP#84 | SP-190425 | 1037 | 3 | B | Introduction of RACS: UCMF services | 16.1.0 |
| 2019-06 | SP#84 | SP-190514 | 1042 | 6 | A | Correcting factors to consider for PCF selection | 16.1.0 |
| 2019-06 | SP#84 | SP-190399 | 1044 | 2 | A | QoS Notification Control | 16.1.0 |
| 2019-06 | SP#84 | SP-190407 | 1047 | 3 | F | MICO mode and Periodic Registration Timer Control | 16.1.0 |
| 2019-06 | SP#84 | SP-190422 | 1050 | 4 | B | Transfer of N4 information for local traffic switching from SMF to I-SMF | 16.1.0 |
| 2019-06 | SP#84 | SP-190428 | 1015 | 2 | B | Proposed update to 5G LAN terminology | 16.1.0 |
| 2019-06 | SP#84 | SP-190428 | 1052 | 8 | B | Further detailing of 5G LAN group management | 16.1.0 |
| 2019-06 | SP#84 | SP-190413 | 1055 | 2 | F | Correction of SMF selecting UPF for a particular PDU Session supporting EPS IWK | 16.1.0 |
| 2019-06 | SP#84 | SP-190410 | 1056 | 2 | F | Network Slicing and delegated discovery | 16.1.0 |
| 2019-06 | SP#84 | SP-190407 | 1059 | 1 | F | UE specific DRX parameter use for NB-IOT | 16.1.0 |
| 2019-06 | SP#84 | SP-190399 | 1062 | 1 | A | Congestion control exception for reporting 5GSM Core Network Capability and Always-on PDU Session Requested indication | 16.1.0 |
| 2019-06 | SP#84 | SP-190399 | 1064 | 1 | A | Data volume reporting granularity | 16.1.0 |
| 2019-06 | SP#84 | SP-190399 | 1066 | - | A | Removal of restriction of using UE requested PDU modification request for Emergency PDU | 16.1.0 |
| 2019-06 | SP#84 | SP-190427 | 1067 | 6 | F | Return to NR from EPS/RAT fallback | 16.1.0 |
| 2019-06 | SP#84 | SP-190427 | 1068 | 2 | F | Clarification on PRA | 16.1.0 |
| 2019-06 | SP#84 | SP-190412 | 1070 | 3 | F | Clarification to support associating URLLC traffic to redundant PDU sessions | 16.1.0 |
| 2019-06 | SP#84 | SP-190425 | 1071 | 5 | B | Introduction of Radio Capabilities Signalling Optimisation feature | 16.1.0 |
| 2019-06 | SP#84 | SP-190428 | 1073 | 4 | B | Support of emergency services in public network integrated NPNs | 16.1.0 |
| 2019-06 | SP#84 | SP-190407 | 1075 | 3 | F | Clarification on MICO and eDRX during CN node changes | 16.1.0 |
| 2019-06 | SP#84 | SP-190416 | 1078 | 1 | F | Correction and clarifications for QoS Flow in MA PDU Session | 16.1.0 |
| 2019-06 | SP#84 | SP-190416 | 1079 | 2 | F | Correction related to ATSSS Rule | 16.1.0 |
| 2019-06 | SP#84 | SP-190416 | 1080 | 2 | F | Clear ENs about Measurement Assistance Information for ATSSS | 16.1.0 |
| 2019-06 | SP#84 | SP-190428 | 1083 | 6 | B | Clarification of Inserting and Removing VLAN tags for 5G-VN | 16.1.0 |
| 2019-06 | SP#84 | SP-190410 | 1091 | 2 | F | Update of the NF/NF service discovery result | 16.1.0 |
| 2019-06 | SP#84 | SP-190410 | 1092 | 3 | C | Update of NRF function and services | 16.1.0 |
| 2019-06 | SP#84 | SP-190410 | 1093 | 2 | F | Update of network reliability support | 16.1.0 |
| 2019-06 | SP#84 | SP-190420 | 1094 | 1 | C | Back-off timers handling for scheduled communication | 16.1.0 |
| 2019-06 | SP#84 | SP-190428 | 1095 | 5 | C | Addressing Editor's notes on TSN | 16.1.0 |
| 2019-06 | SP#84 | SP-190428 | 1098 | 1 | F | Access Control for PLMN Integrated NPN | 16.1.0 |
| 2019-06 | SP#84 | SP-190407 | 1101 | 9 | B | Establishing UP connection during CP Data Transfer | 16.1.0 |
| 2019-06 | SP#84 | SP-190416 | 1103 | 1 | F | Corrections for SMF, UPF and PCF selection for an MA PDU session | 16.1.0 |
| 2019-06 | SP#84 | SP-190416 | 1104 | 1 | F | Corrections for N4 rules for ATSSS | 16.1.0 |
| 2019-06 | SP#84 | SP-190407 | 1109 | 2 | B | Service Gap corrections | 16.1.0 |
| 2019-06 | SP#84 | SP-190399 | 1116 | 2 | F | Local cache information for ARP proxy | 16.1.0 |
| 2019-06 | SP#84 | SP-190416 | 1118 | 1 | F | UE Requested PDU Session Establishment with Network Modification to MA PDU Session | 16.1.0 |
| 2019-06 | SP#84 | SP-190428 | 1119 | 2 | C | Granularity of TSN bridge | 16.1.0 |
| 2019-06 | SP#84 | SP-190412 | 1120 | 1 | C | Filtering own address for Ethernet PDU Sessions | 16.1.0 |
| 2019-06 | SP#84 | SP-190428 | 1123 | 3 | B | TSN QoS mapping and 802.1Qbv parameters | 16.1.0 |
| 2019-06 | SP#84 | SP-190415 | 1128 | 3 | B | Access to 5GC from UEs not supporting NAS over non-3GPP access | 16.1.0 |
| 2019-06 | SP#84 | SP-190399 | 1130 | 1 | A | Validity of LADN information and LADN discovery/storage in the UE per-PLMN | 16.1.0 |
| 2019-06 | SP#84 | SP-190399 | 1131 | 3 | A | Conclusions on applicability of Allowed NSSAI to E-PLMNs | 16.1.0 |
| 2019-06 | SP#84 | SP-190399 | 1132 | 1 | A | Correction to the provisioning of the UE Integrity Protection Data Rate capability | 16.1.0 |
| 2019-06 | SP#84 | SP-190419 | 1134 | 3 | B | Allowing IMS to use N5 interface to interact with PCF | 16.1.0 |
| 2019-06 | SP#84 | SP-190428 | 1135 | 3 | F | Correction regarding legacy UE and non-NPN UE | 16.1.0 |
| 2019-06 | SP#84 | SP-190427 | 1139 | 3 | F | AMF selection during inter PLMN mobility | 16.1.0 |
| 2019-06 | SP#84 | SP-190412 | 1142 | 6 | C | Update description for E2E PDB division | 16.1.0 |
| 2019-06 | SP#84 | SP-190412 | 1144 | 2 | C | Explicit indication of AF response to be expected for runtime coordination with AF | 16.1.0 |
| 2019-06 | SP#84 | SP-190407 | 1149 | 9 | B | Roaming support for service exposure | 16.1.0 |
| 2019-06 | SP#84 | SP-190399 | 1152 | 1 | A | Corrections for the activation of usage reporting in the UPF | 16.1.0 |
| 2019-06 | SP#84 | SP-190399 | 1159 | 2 | A | Clarification on NAS level congestion control | 16.1.0 |
| 2019-06 | SP#84 | SP-190399 | 1161 | 3 | A | Correction of UE 5GSM Core Network Capability | 16.1.0 |
| 2019-06 | SP#84 | SP-190423 | 1162 | 1 | B | Introduce a new standardized SST value dedicated for V2X services | 16.1.0 |
| 2019-06 | SP#84 | SP-190412 | 1163 | 1 | F | Clarification on the CN PDB configured in each NG-RAN node | 16.1.0 |
| 2019-06 | SP#84 | SP-190416 | 1164 | 2 | B | Clarification on GBR QoS Flow establishment | 16.1.0 |
| 2019-06 | SP#84 | SP-190416 | 1168 | 5 | C | RTT measurements with TCP | 16.1.0 |
| 2019-06 | SP#84 | SP-190416 | 1169 | 2 | F | MA PDU QoS Aspects On Link-Specific Multipath and MPTCP Proxy Addresses | 16.1.0 |
| 2019-06 | SP#84 | SP-190422 | 1170 | 1 | F | ETSUN Architecture Update | 16.1.0 |
| 2019-06 | SP#84 | SP-190410 | 1171 | 4 | F | SCP Function Update | 16.1.0 |
| 2019-06 | SP#84 | SP-190412 | 1173 | 2 | F | Redundant PDU session handling | 16.1.0 |
| 2019-06 | SP#84 | SP-190421 | 1174 | 6 | B | Introduction of Slice-Specific Authentication and Authorisation | 16.1.0 |
| 2019-06 | SP#84 | SP-190399 | 1176 | 1 | A | Association between the GUAMI and AMF instance | 16.1.0 |
| 2019-06 | SP#84 | SP-190422 | 1177 | 5 | B | LADN handling in ETSUN scenario | 16.1.0 |
| 2019-06 | SP#84 | SP-190422 | 1179 | 7 | B | Traffic offload by UPF controlled by the I-SMF | 16.1.0 |
| 2019-06 | SP#84 | SP-190422 | 1180 | 1 | B | UE IP address Allocation by AAA/DHCP | 16.1.0 |
| 2019-06 | SP#84 | SP-190428 | 1183 | 3 | C | SNPN deployment scenarios | 16.1.0 |
| 2019-06 | SP#84 | SP-190407 | 1186 | 8 | B | Introducing 5GS UP optimization | 16.1.0 |
| 2019-06 | SP#84 | SP-190420 | 1187 | 1 | B | Adding NF load information inside NFprofile | 16.1.0 |
| 2019-06 | SP#84 | SP-190428 | 1190 | 2 | C | Resolving editor's note on eSBA | 16.1.0 |
| 2019-06 | SP#84 | SP-190416 | 1191 | 3 | F | ATSSS support for Unstructured Data | 16.1.0 |
| 2019-06 | SP#84 | SP-190428 | 1194 | 3 | F | Removing the EN on the DNN and 5G LAN group mapping | 16.1.0 |
| 2019-06 | SP#84 | SP-190428 | 1198 | 8 | C | Resolving the EN on traffic pattern to the TT | 16.1.0 |
| 2019-06 | SP#84 | SP-190428 | 1199 | 3 | F | Clarification on the CAG ID and slicing | 16.1.0 |
| 2019-06 | SP#84 | SP-190420 | 1201 | 2 | B | CR for adding Naf_EventExposure services | 16.1.0 |
| 2019-06 | SP#84 | SP-190428 | 1202 | 2 | F | Clarification on PDU Session management for 5G-LAN multicast | 16.1.0 |
| 2019-06 | SP#84 | SP-190409 | 1205 | - | B | Add new Reference points | 16.1.0 |
| 2019-06 | SP#84 | SP-190428 | 1207 | 3 | F | 5G-LAN Service continuity | 16.1.0 |
| 2019-06 | SP#84 | SP-190428 | 1212 | 1 | B | Update to Support TSAI for TSC Deterministic QoS | 16.1.0 |
| 2019-06 | SP#84 | SP-190428 | 1214 | 10 | B | Introducing support for UE and UPF Residence Time for TSC Deterministic QoS | 16.1.0 |
| 2019-06 | SP#84 | SP-190412 | 1217 | 4 | C | 5G URLLC: Optimizing Redundancy | 16.1.0 |
| 2019-06 | SP#84 | SP-190428 | 1218 | 2 | F | Standalone NPN - NID Management | 16.1.0 |
| 2019-06 | SP#84 | SP-190428 | 1219 | 1 | F | Standalone NPN - EPS Interworking support | 16.1.0 |
| 2019-06 | SP#84 | SP-190410 | 1222 | 12 | B | NF Set and NF Service Set - Open items resolution | 16.1.0 |
| 2019-06 | SP#84 | SP-190413 | 1226 | - | F | AMF Failure - Other CP NF Behaviour | 16.1.0 |
| 2019-06 | SP#84 | SP-190399 | 1228 | 1 | A | Correction on home-routed roaming architecture for EPC interworking | 16.1.0 |
| 2019-06 | SP#84 | SP-190428 | 1230 | 4 | C | Dedicated SMF selection for a 5G LAN group | 16.1.0 |
| 2019-06 | SP#84 | SP-190415 | 1233 | 4 | F | Requirements on the Ta interface | 16.1.0 |
| 2019-06 | SP#84 | SP-190399 | 1235 | 2 | A | Configuration transfer between NG-RAN and eNodeB | 16.1.0 |
| 2019-06 | SP#84 | SP-190399 | 1237 | 1 | A | Cleanup of NAS Congestion Control | 16.1.0 |
| 2019-06 | SP#84 | SP-190415 | 1239 | 4 | B | Removal of roaming support from Rel-16 for W-5GAN | 16.1.0 |
| 2019-06 | SP#84 | SP-190407 | 1243 | - | B | Update to NEF description by adding NIDD support | 16.1.0 |
| 2019-06 | SP#84 | SP-190399 | 1249 | 2 | A | Correction of SM congestion control override | 16.1.0 |
| 2019-06 | SP#84 | SP-190407 | 1250 | 2 | B | Corrections to MICO mode with Active Time | 16.1.0 |
| 2019-06 | SP#84 | SP-190407 | 1251 | 1 | B | Subscription Information Influence on PDU Session Rate Control | 16.1.0 |
| 2019-06 | SP#84 | SP-190407 | 1252 | 2 | B | Handling of Stored Small Data Rate Control Status at Subsequent PDU Session Establishment | 16.1.0 |
| 2019-06 | SP#84 | SP-190407 | 1256 | 4 | F | Corrections to CN assisted RAN parameters tuning | 16.1.0 |
| 2019-06 | SP#84 | SP-190413 | 1257 | 3 | F | Corrections to Network Slice Registration | 16.1.0 |
| 2019-06 | SP#84 | SP-190420 | 1258 | 2 | B | CR for TS 23.501 Clarifications NWDAF Discovery and Selection | 16.1.0 |
| 2019-06 | SP#84 | SP-190407 | 1262 | 1 | F | RRC Inactive information for eDRX | 16.1.0 |
| 2019-06 | SP#84 | SP-190427 | 1263 | 2 | F | AMF utilizes NRF to discover NSSF | 16.1.0 |
| 2019-06 | SP#84 | SP-190428 | 1264 | 3 | F | QoS differentiation for access to SNPN (PLMN) services via PLMN (SNPN) | 16.1.0 |
| 2019-06 | SP#84 | SP-190422 | 1265 | - | D | Fixing clause number reference | 16.1.0 |
| 2019-06 | SP#84 | SP-190427 | 1266 | 2 | F | Correction of description of the IMS voice over PS Session Supported Indication | 16.1.0 |
| 2019-06 | SP#84 | SP-190410 | 1271 | 13 | D | SCP: Service-mesh-based deployment options | 16.1.0 |
| 2019-06 | SP#84 | SP-190427 | 1274 | 2 | F | Clarification on the UE operates in SR mode in case the NW does not support IWK | 16.1.0 |
| 2019-06 | SP#84 | SP-190399 | 1275 | - | A | Removing unnecessary PDU release during inter-system handover | 16.1.0 |
| 2019-06 | SP#84 | SP-190399 | 1277 | 1 | A | Definition of LPP | 16.1.0 |
| 2019-06 | SP#84 | SP-190399 | 1278 | 2 | A | UE's usage setting indicating UE capability of supporting voice over E-UTRA | 16.1.0 |
| 2019-06 | SP#84 | SP-190399 | 1279 | - | A | Clarification for interface identifier allocation in IPv6 Multi-homing | 16.1.0 |
| 2019-06 | SP#84 | SP-190407 | 1283 | 3 | F | Interaction between MICO mode with active time and eDRX | 16.1.0 |
| 2019-06 | SP#84 | SP-190407 | 1287 | - | F | Update reference to TS 24.250 | 16.1.0 |
| 2019-06 | SP#84 | SP-190426 | 1291 | 1 | B | Introduction of UDICOM | 16.1.0 |
| 2019-06 | SP#84 | SP-190417 | 1296 | 2 | C | Adding Support for Indicating Serialization Format in RDS | 16.1.0 |
| 2019-06 | SP#84 | SP-190428 | 1297 | 2 | F | CAG and Network Slice Selection | 16.1.0 |
| 2019-06 | SP#84 | SP-190428 | 1298 | 3 | F | Unified Access Control with NPN | 16.1.0 |
| 2019-06 | SP#84 | SP-190399 | 1301 | 1 | A | Configuring Transport Level Marking values | 16.1.0 |
| 2019-06 | SP#84 | SP-190427 | 1303 | 1 | F | Alignment of Network Slice selection logic | 16.1.0 |
| 2019-06 | SP#84 | SP-190413 | 1305 | 2 | F | Enforcement of UP integrity protection | 16.1.0 |
| 2019-06 | SP#84 | SP-190429 | 1306 | 2 | F | Ethernet support clarification | 16.1.0 |
| 2019-06 | SP#84 | SP-190412 | 1307 | 2 | F | Generalized text for redundant user planes in RAN | 16.1.0 |
| 2019-06 | SP#84 | SP-190413 | 1308 | 3 | C | DNN replacement in 5GC | 16.1.0 |
| 2019-06 | SP#84 | SP-190410 | 1312 | 1 | B | Extending the significance of the locality parameter | 16.1.0 |
| 2019-06 | SP#84 | SP-190399 | 1315 | 2 | A | Correcting AMF selection | 16.1.0 |
| 2019-06 | SP#84 | SP-190422 | 1316 | 1 | C | Clarify which parameters are (not) applicable for I-SMF selection. | 16.1.0 |
| 2019-06 | SP#84 | SP-190412 | 1320 | 3 | F | Clarification on redundant N3 tunnel solution | 16.1.0 |
| 2019-06 | SP#84 | SP-190427 | 1321 | - | F | Clarification on IWK without N26 | 16.1.0 |
| 2019-06 | SP#84 | SP-190418 | 1323 | 1 | C | S6b optional for ePDG connected to 5GS | 16.1.0 |
| 2019-06 | SP#84 | SP-190429 | 1328 | 2 | F | Data forwarding for 5G-LAN multicast | 16.1.0 |
| 2019-06 | SP#84 | SP-190410 | 1331 | 3 | B | Support of Service Context Transfer in TS23.501 | 16.1.0 |
| 2019-06 | SP#84 | SP-190413 | 1333 | 1 | B | Alignment of IMS Voice Service via EPS Fallback with RAN specifications | 16.1.0 |
| 2019-06 | SP#84 | SP-190407 | 1337 | 1 | B | Update to High Latency Overall Description | 16.1.0 |
| 2019-06 | SP#84 | SP-190429 | 1338 | 2 | F | NPN: Corrections to handling of Allowed CAG list and CAG-only indication | 16.1.0 |
| 2019-06 | SP#84 | SP-190429 | 1339 | 2 | F | NPN: Correction to CAG-only indication | 16.1.0 |
| 2019-06 | SP#84 | SP-190429 | 1341 | 2 | F | NPN: Update and enforcement of new Allowed CAG list and CAG-only indication | 16.1.0 |
| 2019-06 | SP#84 | SP-190407 | 1346 | 2 | F | CIoT scope clarification | 16.1.0 |
| 2019-06 | SP#84 | SP-190404 | 1350 | 2 | A | Location Reporting of secondary cell | 16.1.0 |
| 2019-06 | SP#84 | SP-190416 | 1351 | 2 | B | Network request re-activation of user-plane resources | 16.1.0 |
| 2019-06 | SP#84 | SP-190416 | 1352 | 2 | B | Clarification on Access Network Performance Measurements | 16.1.0 |
| 2019-06 | SP#84 | SP-190399 | 1358 | 1 | A | Emergency Fallback from non-3GPP/ePDG | 16.1.0 |
| 2019-06 | SP#84 | SP-190407 | 1360 | 1 | F | NIDD related indications | 16.1.0 |
| 2019-06 | SP#84 | SP-190420 | 1362 | 2 | B | Description regarding NEF support of data retrieval from external party | 16.1.0 |
| 2019-06 | SP#84 | SP-190427 | 1366 | 3 | F | Subscription Segmentation in PCF and UDR | 16.1.0 |
| 2019-06 | SP#84 | SP-190427 | 1367 | 2 | C | Serving PLMN UE-AMBR control | 16.1.0 |
| 2019-06 | SP#84 | SP-190415 | 1372 | 1 | B | Access network selection for devices that do not support NAS over WLAN | 16.1.0 |
| 2019-06 | SP#84 | SP-190415 | 1374 | - | B | AMF overload control for trusted non-3GPP access | 16.1.0 |
| 2019-06 | SP#84 | SP-190413 | 1375 | 2 | B | 23.501 part of PCF selection for PDU sessions with same DNN and S-NSSAI | 16.1.0 |
| 2019-06 | SP#84 | SP-190407 | 1376 | 1 | B | Support for Enhanced Coverage Restriction Control via NEF | 16.1.0 |
| 2019-06 | SP#84 | SP-190413 | 1378 | 1 | F | Support for Dynamic Port Management in RDS | 16.1.0 |
| 2019-06 | SP#84 | SP-190429 | 1381 | 2 | B | Introduction of TSN Sync soln #28A | 16.1.0 |
| 2019-06 | SP#84 | SP-190429 | 1382 | 1 | F | Update to Survival time EN | 16.1.0 |
| 2019-06 | SP#84 | SP-190419 | 1384 | 3 | B | Adding UDR NF Group ID association functionality | 16.1.0 |
| 2019-06 | SP#84 | SP-190413 | 1390 | 2 | F | Correction of use of PEI/IMEI for non-3GPP only UEs | 16.1.0 |
| 2019-06 | SP#84 | SP-190416 | 1395 | 1 | F | Clarifications on Reflective QoS for MPTCP | 16.1.0 |
| 2019-06 | SP#84 | SP-190429 | 1396 | 1 | B | NW selection considering RAN sharing for SNPNs | 16.1.0 |
| 2019-06 | SP#84 | SP-190421 | 1404 | 1 | F | Target AMF Selection during mobility from EPS to 5GS | 16.1.0 |
| 2019-06 | SP#84 | SP-190420 | 1405 | - | F | Corrections to analytics used by AMF for MICO mode and SMF for UPF selection | 16.1.0 |
| 2019-06 | SP#84 | SP-190420 | 1406 | 1 | B | Update NRF descriptions to support AF Available Data Registration as described in TS23.288 | 16.1.0 |
| 2019-06 | SP#84 | SP-190427 | 1408 | 2 | F | Corrections and alignments for the 5QI characteristics table | 16.1.0 |
| 2019-06 | SP#84 | SP-190410 | 1413 | 2 | B | NF Set concept for SMF | 16.1.0 |
| 2019-06 | SP#84 | SP-190407 | 1417 | 2 | B | Stateless IPv6 Address Autoconfiguration for Control Plane CIoT 5GS Optimisation | 16.1.0 |
| 2019-06 | SP#84 | SP-190407 | 1418 | 2 | B | Introduction of Small Data Rate Control Interworking with APN Rate Control | 16.1.0 |
| 2019-06 | SP#84 | SP-190415 | 1420 | 2 | B | Location information for trusted N3GPP | 16.1.0 |
| 2019-06 | SP#84 | SP-190429 | 1423 | 2 | B | TSC Burst Arrival Time usage and Clock Reference | 16.1.0 |
| 2019-06 | SP#84 | SP-190413 | 1424 | 2 | F | Correction on Location reporting procedure | 16.1.0 |
| 2019-06 | SP#84 | SP-190429 | 1425 | 3 | C | Address editor's notes for 5GS Bridge management and QoS mapping | 16.1.0 |
| 2019-06 | SP#84 | SP-190429 | 1426 | 4 | C | clarifications on SNPN | 16.1.0 |
| 2019-06 | SP#84 | SP-190429 | 1427 | 2 | C | Support for unicast traffic forwarding within a 5G VN group | 16.1.0 |
| 2019-06 | SP#84 | SP-190429 | 1430 | 2 | C | implementation of 5G-VN related interfaces | 16.1.0 |
| 2019-06 | SP#84 | SP-190407 | 1431 | 1 | B | Support of User Plane Optimisations in Preferred and Supported Network Behaviour | 16.1.0 |
| 2019-06 | SP#84 | SP-190429 | 1432 | 1 | B | Ingress timestamp signalling | 16.1.0 |
| 2019-06 | SP#84 | SP-190413 | 1436 | - | F | Align CHF service for offline only charging | 16.1.0 |
| 2019-06 | SP#84 | SP-190419 | 1438 | 2 | B | HSS discovery via NRF | 16.1.0 |
| 2019-06 | SP#84 | SP-190429 | 1443 | 1 | B | AF influence for traffic forwarding in 5G-VN | 16.1.0 |
| 2019-06 | SP#84 | SP-190431 | 1445 | 2 | B | Update of TS23.501 to finalize xBDT feature | 16.1.0 |
| 2019-06 | SP#84 | SP-190429 | 1448 | - | D | Vertical_LAN - Editorial clean up | 16.1.0 |
| 2019-06 | SP#84 | SP-190399 | 1449 | 1 | A | Applicability of Allowed NSSAI to PLMNs whose TAIs are in the RA TAI list | 16.1.0 |
| 2019-06 | SP#84 | SP-190399 | 1451 | - | A | Clarification on S-NSSAI for PDU session in Requested NSSAI | 16.1.0 |
| 2019-09 | SP#85 | SP-190608 | 0990 | 6 | B | Introduction of QoS Monitoring to assist URLLC Service | 16.2.0 |
| 2019-09 | SP#85 | SP-190618 | 1097 | 3 | F | Support of Standalone Non-Public Networks | 16.2.0 |
| 2019-09 | SP#85 | SP-190618 | 1240 | 5 | F | Clarification of support of dual radio UE | 16.2.0 |
| 2019-09 | SP#85 | SP-190610 | 1329 | 3 | F | IP Address Accessibility for MA PDU Session | 16.2.0 |
| 2019-09 | SP#85 | SP-190610 | 1330 | 2 | F | N3/N9 Tunnels for the MA-PDU Session | 16.2.0 |
| 2019-09 | SP#85 | SP-190605 | 1347 | 6 | F | Introducing of UP CIoT 5GS Optimisation capability | 16.2.0 |
| 2019-09 | SP#85 | SP-190605 | 1364 | 1 | F | NIDD Description Update for Maximum Packet Size | 16.2.0 |
| 2019-09 | SP#85 | SP-190618 | 1371 | 3 | F | Clarification for the related CAG identifier | 16.2.0 |
| 2019-09 | SP#85 | SP-190618 | 1379 | 2 | F | Support for access to PLMN services via SNPN and SNPN services via PLMN | 16.2.0 |
| 2019-09 | SP#85 | SP-190608 | 1414 | 3 | B | QoS monitoring based on GTP-U paths | 16.2.0 |
| 2019-09 | SP#85 | SP-190615 | 1440 | 8 | B | Enhancements to QoS Handling for V2X Communication Over Uu Reference Point | 16.2.0 |
| 2019-09 | SP#85 | SP-190607 | 1453 | 4 | F | Completion of the PCF Group | 16.2.0 |
| 2019-09 | SP#85 | SP-190622 | 1454 | 2 | F | Inter Core Network Roaming | 16.2.0 |
| 2019-09 | SP#85 | SP-190609 | 1455 | 3 | F | Align PLMN selection with service requirements | 16.2.0 |
| 2019-09 | SP#85 | SP-190605 | 1457 | 2 | F | NAS RAI corrections | 16.2.0 |
| 2019-09 | SP#85 | SP-190605 | 1461 | 2 | F | Clarifications to QoS support for NB-IoT | 16.2.0 |
| 2019-09 | SP#85 | SP-190617 | 1463 | 3 | F | Correction on support of RACS | 16.2.0 |
| 2019-09 | SP#85 | SP-190618 | 1464 | 3 | C | Completing Ethernet port management | 16.2.0 |
| 2019-09 | SP#85 | SP-190605 | 1465 | 2 | F | Adding N4 Notification about buffered packets being dropped | 16.2.0 |
| 2019-09 | SP#85 | SP-190609 | 1466 | - | F | PEI for 5G-RG and FN-RG | 16.2.0 |
| 2019-09 | SP#85 | SP-190618 | 1467 | 1 | F | Corrections to general 5G LAN description | 16.2.0 |
| 2019-09 | SP#85 | SP-190618 | 1468 | 3 | F | 5G LAN user plane corrections | 16.2.0 |
| 2019-09 | SP#85 | SP-190610 | 1469 | 4 | F | Awareness of UE PMF port number and MAC address in UPF | 16.2.0 |
| 2019-09 | SP#85 | SP-190607 | 1470 | 4 | F | Clarification of the Locality of a NF Instance | 16.2.0 |
| 2019-09 | SP#85 | SP-190621 | 1476 | 2 | F | Replacement of VPLMN by serving PLMN where appropriate | 16.2.0 |
| 2019-09 | SP#85 | SP-190621 | 1477 | 1 | F | Clarification on the misalignment of service area restriction between UE and Network | 16.2.0 |
| 2019-09 | SP#85 | SP-190611 | 1478 | 1 | F | Correction of P-CSCF selection to consider proximity to UPF | 16.2.0 |
| 2019-09 | SP#85 | SP-190605 | 1479 | 1 | F | Aligning Terminology referring to the CIoT 5GS Optimisations | 16.2.0 |
| 2019-09 | SP#85 | SP-190617 | 1480 | 1 | F | Corrections of PLMN assigned Capability signalling | 16.2.0 |
| 2019-09 | SP#85 | SP-190621 | 1483 | 1 | F | Correction of Network Slice selection with NSSF | 16.2.0 |
| 2019-09 | SP#85 | SP-190621 | 1487 | 3 | C | DNN replacement in 5GC | 16.2.0 |
| 2019-09 | SP#85 | SP-190608 | 1489 | 1 | F | Failure handling for redundancy based on dual connectivity | 16.2.0 |
| 2019-09 | SP#85 | SP-190608 | 1490 | 1 | F | Clarification on reordering requirement with GTP-U redundancy | 16.2.0 |
| 2019-09 | SP#85 | SP-190601 | 1494 | 1 | A | Discrepancy with TS 33.501 with respect to Secondary Authentication | 16.2.0 |
| 2019-09 | SP#85 | SP-190610 | 1500 | 2 | F | Clarification of traffic switching for GBR QoS Flow in MA PDU session | 16.2.0 |
| 2019-09 | SP#85 | SP-190618 | 1501 | 3 | F | N19 Tunnel management | 16.2.0 |
| 2019-09 | SP#85 | SP-190618 | 1504 | 3 | C | TSN Time Synchronization Traffic Handling | 16.2.0 |
| 2019-09 | SP#85 | SP-190618 | 1507 | 3 | F | TSC Assistance Information update | 16.2.0 |
| 2019-09 | SP#85 | SP-190605 | 1509 | 1 | F | Handling of CIoT optimisations not supported over NR | 16.2.0 |
| 2019-09 | SP#85 | SP-190617 | 1517 | 2 | C | Handling of NB-IOT radio capabilities and RACS in 5GS | 16.2.0 |
| 2019-09 | SP#85 | SP-190601 | 1519 | 2 | A | Allowed NSSAI and TAI list from (previous) UE Configuration Update | 16.2.0 |
| 2019-09 | SP#85 | SP-190622 | 1521 | 1 | F | Use of the URSP rules when UE attaches to EPS | 16.2.0 |
| 2019-09 | SP#85 | SP-190624 | 1522 | 1 | B | Introduction of the IAB support in 5GS | 16.2.0 |
| 2019-09 | SP#85 | SP-190621 | 1540 | 2 | F | Clarification on the meaning of Emergency Services Support indicator | 16.2.0 |
| 2019-09 | SP#85 | SP-190605 | 1541 | 2 | F | Addition of missing CIoT services | 16.2.0 |
| 2019-09 | SP#85 | SP-190606 | 1543 | 1 | F | Addition of missing GMLC and its service | 16.2.0 |
| 2019-09 | SP#85 | SP-190614 | 1544 | 3 | F | Mobility event management | 16.2.0 |
| 2019-09 | SP#85 | SP-190608 | 1547 | - | F | Improvement for support of redundant transmission on N3/N9 interfaces | 16.2.0 |
| 2019-09 | SP#85 | SP-190621 | 1548 | 1 | F | Clarification on S-NSSAI(s) for PDU session | 16.2.0 |
| 2019-09 | SP#85 | SP-190622 | 1556 | 2 | D | Adding Policy Charging and Control related reference points | 16.2.0 |
| 2019-09 | SP#85 | SP-190621 | 1557 | 2 | F | Update to NEF related reference points | 16.2.0 |
| 2019-09 | SP#85 | SP-190611 | 1563 | 1 | F | NF Group resolution by SCP | 16.2.0 |
| 2019-09 | SP#85 | SP-190610 | 1570 | 1 | F | Corrections about default QoS rule | 16.2.0 |
| 2019-09 | SP#85 | SP-190610 | 1571 | 3 | B | Interworking for MA PDU Session | 16.2.0 |
| 2019-09 | SP#85 | SP-190605 | 1573 | 2 | F | Conditions to use CP or UP CIoT | 16.2.0 |
| 2019-09 | SP#85 | SP-190621 | 1578 | 1 | F | Correction of NAS transport for LCS | 16.2.0 |
| 2019-09 | SP#85 | SP-190605 | 1580 | 2 | F | Corrections to Control Plane CIoT 5GS Optimisation description | 16.2.0 |
| 2019-09 | SP#85 | SP-190605 | 1581 | - | F | Alignment of the term Early Data Transmission | 16.2.0 |
| 2019-09 | SP#85 | SP-190610 | 1586 | 3 | B | Network request re-activation of user-plane resources | 16.2.0 |
| 2019-09 | SP#85 | SP-190610 | 1587 | 1 | F | PMF message delivery | 16.2.0 |
| 2019-09 | SP#85 | SP-190613 | 1588 | 3 | F | AMF capability of Network Slice-Specific Authentication and Authorization | 16.2.0 |
| 2019-09 | SP#85 | SP-190622 | 1589 | 3 | F | Priority of CHF selection | 16.2.0 |
| 2019-09 | SP#85 | SP-190605 | 1596 | 1 | B | Clarify short DRX cycle length CM-CONNECTED with RRC inactive for eMTC | 16.2.0 |
| 2019-09 | SP#85 | SP-190605 | 1598 | 3 | F | Clarification on NEF discovery by an AF | 16.2.0 |
| 2019-09 | SP#85 | SP-190618 | 1604 | - | F | Exclusive Gating Mechanism | 16.2.0 |
| 2019-09 | SP#85 | SP-190611 | 1607 | 1 | F | Update P-CSCF Discovery using NRF | 16.2.0 |
| 2019-09 | SP#85 | SP-190618 | 1608 | 1 | F | GUAMI allocation for standalone non-public network | 16.2.0 |
| 2019-09 | SP#85 | SP-190607 | 1622 | - | F | Relation between Group and Set | 16.2.0 |
| 2019-09 | SP#85 | SP-190607 | 1624 | 3 | F | Network Function/NF Service Context | 16.2.0 |
| 2019-09 | SP#85 | SP-190605 | 1632 | 3 | F | Clarification on strictly periodic timer in relation to MICO mode. | 16.2.0 |
| 2019-09 | SP#85 | SP-190610 | 1636 | 2 | F | Mandatory support of ATSSS-LL for PDU Sessions of type Ethernet | 16.2.0 |
| 2019-09 | SP#85 | SP-190618 | 1637 | 3 | F | Update of 5G LAN-type service feature description | 16.2.0 |
| 2019-09 | SP#85 | SP-190608 | 1643 | 2 | C | Clarifications on URLLC support | 16.2.0 |
| 2019-09 | SP#85 | SP-190608 | 1644 | 1 | F | Clarification and correction to AF response | 16.2.0 |
| 2019-09 | SP#85 | SP-190610 | 1646 | 1 | F | MA PDU IP Address/Prefix Handling in UPF | 16.2.0 |
| 2019-09 | SP#85 | SP-190618 | 1647 | 1 | F | Use of NW instance for N19 interface | 16.2.0 |
| 2019-09 | SP#85 | SP-190609 | 1650 | 1 | F | Corrections for devices that do not support 5GC NAS over WLAN access | 16.2.0 |
| 2019-09 | SP#85 | SP-190610 | 1652 | - | F | Correction to protocol stacks for RTT measurements | 16.2.0 |
| 2019-09 | SP#85 | SP-190610 | 1653 | 3 | F | Clarification about an MA PDU Session using only MPTCP functionality | 16.2.0 |
| 2019-09 | SP#85 | SP-190618 | 1659 | 2 | C | Support of forwarding of broadcast and multicast packets | 16.2.0 |
| 2019-09 | SP#85 | SP-190618 | 1660 | 2 | C | Address editor's notes for TSN | 16.2.0 |
| 2019-09 | SP#85 | SP-190607 | 1664 | 4 | F | eSBA SMF and PCF selection-option 2 | 16.2.0 |
| 2019-09 | SP#85 | SP-190605 | 1665 | 1 | F | Clarification on Preferred Network Behaviour for CIoT 5GS Optimisations | 16.2.0 |
| 2019-09 | SP#85 | SP-190605 | 1669 | 1 | F | Removal of eDRX support with RRC_INACTIVE for NB-IoT | 16.2.0 |
| 2019-09 | SP#85 | SP-190605 | 1670 | 2 | F | UPF Service Area awareness for keeping UL N3 Tunnel available | 16.2.0 |
| 2019-09 | SP#85 | SP-190612 | 1671 | 3 | F | Correction on data collection from an AF | 16.2.0 |
| 2019-09 | SP#85 | SP-190618 | 1675 | 2 | C | Modification to the QoS parameters mapping for 5GS Bridge configuration | 16.2.0 |
| 2019-09 | SP#85 | SP-190612 | 1677 | 1 | F | Updating the stored information in NRF to support BSF discovery | 16.2.0 |
| 2019-09 | SP#85 | SP-190622 | 1678 | 5 | C | On the usage of rateRatio, one-step vs two-step sync operation and dedicated QoS Flow | 16.2.0 |
| 2019-12 | SP#86 | SP-191068 | 1363 | 3 | B | Identification of LTE-M (eMTC) traffic | 16.3.0 |
| 2019-12 | SP#86 | SP-191076 | 1373 | 2 | F | Corrections to Trusted Non-3GPP Access Network selection | 16.3.0 |
| 2019-12 | SP#86 | SP-191090 | 1459 | 3 | F | Correcting AMF selection | 16.3.0 |
| 2019-12 | SP#86 | SP-191071 | 1472 | 2 | F | Correcting behavior if binding indication is not provided | 16.3.0 |
| 2019-12 | SP#86 | SP-191071 | 1473 | 4 | F | Correcting delegated discovery and selection and the use of IDs in binding | 16.3.0 |
| 2019-12 | SP#86 | SP-191068 | 1485 | 3 | F | Service Gap Control at IWK | 16.3.0 |
| 2019-12 | SP#86 | SP-191068 | 1486 | 1 | F | Serving PLMN rate control parameters in modification procedure | 16.3.0 |
| 2019-12 | SP#86 | SP-191071 | 1527 | 3 | F | SMF Set and UPF | 16.3.0 |
| 2019-12 | SP#86 | SP-191076 | 1553 | 2 | F | Completing the introduction of TNGF in 23.501 | 16.3.0 |
| 2019-12 | SP#86 | SP-191088 | 1564 | 3 | F | Correction to deletion of PLMN-assigned UE Radio Capability ID | 16.3.0 |
| 2019-12 | SP#86 | SP-191090 | 1576 | 2 | F | Correction of UE Radio Capability Update IE encoding | 16.3.0 |
| 2019-12 | SP#86 | SP-191088 | 1592 | 10 | F | Resolution of Editor's Note on UCMF-AMF interaction | 16.3.0 |
| 2019-12 | SP#86 | SP-191068 | 1594 | 3 | F | I-NEF in Interworking Scenarios | 16.3.0 |
| 2019-12 | SP#86 | SP-191071 | 1623 | 2 | F | NRF use of UDR Group ID Mapping service | 16.3.0 |
| 2019-12 | SP#86 | SP-191080 | 1654 | 2 | F | UE related analytics for UPF selection | 16.3.0 |
| 2019-12 | SP#86 | SP-191068 | 1666 | 8 | F | Corrections to Small Data Rate Control and Exception Reporting | 16.3.0 |
| 2019-12 | SP#86 | SP-191068 | 1667 | 4 | B | Introduction of RRC Connection Re-Establishment for CP | 16.3.0 |
| 2019-12 | SP#86 | SP-191071 | 1679 | 2 | F | Clarification on target address in service request message | 16.3.0 |
| 2019-12 | SP#86 | SP-191074 | 1687 | 1 | A | Condition for the UE to provide a Requested NSSAI | 16.3.0 |
| 2019-12 | SP#86 | SP-191076 | 1688 | - | F | Network slicing impacts of Wireless and Wireline Convergence | 16.3.0 |
| 2019-12 | SP#86 | SP-191068 | 1689 | 2 | F | Support of TAs with heterogeneous support of eDRX | 16.3.0 |
| 2019-12 | SP#86 | SP-191068 | 1690 | 2 | F | Control Plane CIoT 5GS Optimisations restriction on NR | 16.3.0 |
| 2019-12 | SP#86 | SP-191068 | 1692 | 1 | F | Addition of I-NEF to Network Functions | 16.3.0 |
| 2019-12 | SP#86 | SP-191068 | 1693 | 1 | F | Service Exposure in Interworking Scenarios | 16.3.0 |
| 2019-12 | SP#86 | SP-191090 | 1695 | 2 | F | Correction to PPI setting control over N4 | 16.3.0 |
| 2019-12 | SP#86 | SP-191082 | 1697 | - | F | Interaction between ETSUN and CIoT. | 16.3.0 |
| 2019-12 | SP#86 | SP-191082 | 1698 | 1 | F | Clarifications to ETSUN specification | 16.3.0 |
| 2019-12 | SP#86 | SP-191077 | 1702 | 3 | F | Clarification on QoS Support for ATSSS | 16.3.0 |
| 2019-12 | SP#86 | SP-191090 | 1703 | 3 | F | Clarification on DNN replacement | 16.3.0 |
| 2019-12 | SP#86 | SP-191090 | 1710 | 4 | F | Clarification on N6 traffic routing information for Ethernet type PDU Session | 16.3.0 |
| 2019-12 | SP#86 | SP-191092 | 1711 | 1 | F | clarification on N6-based traffic forwarding of 5G-VN | 16.3.0 |
| 2019-12 | SP#86 | SP-191077 | 1714 | 2 | F | MA PDU Upgrade in modification procedure | 16.3.0 |
| 2019-12 | SP#86 | SP-191071 | 1715 | 1 | F | Delegated discovery and selection in SCP for CHF and SMSF | 16.3.0 |
| 2019-12 | SP#86 | SP-191073 | 1716 | 1 | C | Update N4 rules for QoS Monitoring | 16.3.0 |
| 2019-12 | SP#86 | SP-191088 | 1717 | 2 | F | Clarification on UE capability update | 16.3.0 |
| 2019-12 | SP#86 | SP-191068 | 1721 | 2 | F | Removal of ENs for control plane congestion control | 16.3.0 |
| 2019-12 | SP#86 | SP-191090 | 1722 | 2 | F | Multicast forwarding for Ethernet type PDU Session | 16.3.0 |
| 2019-12 | SP#86 | SP-191081 | 1723 | 2 | F | Alignments to support Network Slice-Specific Authentication and Authorization | 16.3.0 |
| 2019-12 | SP#86 | SP-191082 | 1726 | 2 | F | Clarification on IPv6 Router Advertisement message in ETSUN | 16.3.0 |
| 2019-12 | SP#86 | SP-191090 | 1728 | 1 | F | SMF selection clarification | 16.3.0 |
| 2019-12 | SP#86 | SP-191071 | 1729 | 4 | F | Group ID and Set ID | 16.3.0 |
| 2019-12 | SP#86 | SP-191081 | 1730 | 1 | F | AMF redirection at handover from 4G to 5G | 16.3.0 |
| 2019-12 | SP#86 | SP-191077 | 1733 | 1 | F | Clarification of Access Availability report via N4 | 16.3.0 |
| 2019-12 | SP#86 | SP-191090 | 1734 | 1 | F | Clarification of terms in secondary authentication | 16.3.0 |
| 2019-12 | SP#86 | SP-191084 | 1735 | 1 | B | Extension of standardized 5QI to QoS characteristics mapping table to accommodate enhanced V2X requirements | 16.3.0 |
| 2019-12 | SP#86 | SP-191090 | 1736 | 2 | F | Determination of Emergency Services Fallback support in the AMF | 16.3.0 |
| 2019-12 | SP#86 | SP-191080 | 1737 | - | F | UDM Discovery by Internal Group ID | 16.3.0 |
| 2019-12 | SP#86 | SP-191074 | 1738 | 3 | F | UE may provide NSSAI in AS for initial registration | 16.3.0 |
| 2019-12 | SP#86 | SP-191090 | 1739 | 5 | F | No impact on IMS voice session by a change of the IMS voice over PS session indicator during fallback | 16.3.0 |
| 2019-12 | SP#86 | SP-191090 | 1740 | 1 | F | Clarification of Homogeneous Support of IMS Voice over PS Sessions | 16.3.0 |
| 2019-12 | SP#86 | SP-191073 | 1742 | 1 | F | Enhancement of UP path management based on the coordination with AFs | 16.3.0 |
| 2019-12 | SP#86 | SP-191090 | 1743 | 2 | F | PCF selection for multiple PDU Sessions to the same DNN and S-NSSAI | 16.3.0 |
| 2019-12 | SP#86 | SP-191068 | 1745 | - | F | Extended NAS timers for CE mode B | 16.3.0 |
| 2019-12 | SP#86 | SP-191068 | 1746 | 1 | F | Correcting AMF decision to set CP only indicator | 16.3.0 |
| 2019-12 | SP#86 | SP-191092 | 1747 | 7 | F | 5GS Bridge Management | 16.3.0 |
| 2019-12 | SP#86 | SP-191092 | 1750 | 3 | F | Completing QoS and TSCAI mapping | 16.3.0 |
| 2019-12 | SP#86 | SP-191092 | 1751 | 3 | F | Clarifying N3IWF access to SNPN | 16.3.0 |
| 2019-12 | SP#86 | SP-191092 | 1752 | 3 | F | Clarifying CAG handling during RRC resume procedure | 16.3.0 |
| 2019-12 | SP#86 | SP-191090 | 1754 | 1 | F | Update to Clause 4.2.7 Reference Points | 16.3.0 |
| 2019-12 | SP#86 | SP-191090 | 1755 | 3 | F | Corrections on Session-AMBR setting and enforcement | 16.3.0 |
| 2019-12 | SP#86 | SP-191074 | 1757 | 1 | A | Correction on PCF selection and discovery | 16.3.0 |
| 2019-12 | SP#86 | SP-191078 | 1759 | - | F | UDR service for mapping IMS Public Identity to HSS Group ID for HSS selection | 16.3.0 |
| 2019-12 | SP#86 | SP-191071 | 1765 | 3 | F | Notification receiver information in a subscription | 16.3.0 |
| 2019-12 | SP#86 | SP-191071 | 1766 | 3 | F | Correcting delegated discovery for PCF | 16.3.0 |
| 2019-12 | SP#86 | SP-191090 | 1767 | 2 | F | 23.501:PCF provides PCC rule to SMF based on Local routing indication in subscription information | 16.3.0 |
| 2019-12 | SP#86 | SP-191073 | 1768 | 2 | F | Delivery of SMF waiting time to AF for session continuity | 16.3.0 |
| 2019-12 | SP#86 | SP-191077 | 1769 | 3 | F | Corrections for performance measurements | 16.3.0 |
| 2019-12 | SP#86 | SP-191074 | 1770 | 2 | F | Correction on TNLA binding | 16.3.0 |
| 2019-12 | SP#86 | SP-191077 | 1771 | 3 | F | General corrections for MA PDU sessions | 16.3.0 |
| 2019-12 | SP#86 | SP-191077 | 1772 | 2 | F | Corrections to interworking with EPS for ATSSS | 16.3.0 |
| 2019-12 | SP#86 | SP-191077 | 1773 | 2 | F | N4 impacts due to ATSSS | 16.3.0 |
| 2019-12 | SP#86 | SP-191077 | 1774 | 3 | F | Corrections to steering functionalities description | 16.3.0 |
| 2019-12 | SP#86 | SP-191090 | 1775 | 2 | F | PCF selection for DNN replacement | 16.3.0 |
| 2019-12 | SP#86 | SP-191074 | 1778 | 2 | F | Remote Interference Management support | 16.3.0 |
| 2019-12 | SP#86 | SP-191084 | 1785 | 2 | F | Corrections to handling of Alternative QoS Profiles | 16.3.0 |
| 2019-12 | SP#86 | SP-191080 | 1787 | 7 | F | Consistency on Definitions related to NWDAF | 16.3.0 |
| 2019-12 | SP#86 | SP-191068 | 1792 | 2 | F | EDT support for UP CIoT Optimisation | 16.3.0 |
| 2019-12 | SP#86 | SP-191092 | 1797 | 3 | F | Support of PLMN managed NIDs | 16.3.0 |
| 2019-12 | SP#86 | SP-191092 | 1798 | 2 | F | Support of NG-RAN sharing options for NPN | 16.3.0 |
| 2019-12 | SP#86 | SP-191074 | 1801 | 2 | F | TS 23.501: PEI format for non-3GPP devices | 16.3.0 |
| 2019-12 | SP#86 | SP-191092 | 1802 | 2 | F | TSN 5QI clarification and static TSC QoS Flow establishment | 16.3.0 |
| 2019-12 | SP#86 | SP-191092 | 1804 | 3 | F | 5GS bridge model interpretation | 16.3.0 |
| 2019-12 | SP#86 | SP-191092 | 1806 | 5 | F | Revision on MDBV mapping | 16.3.0 |
| 2019-12 | SP#86 | SP-191092 | 1815 | 2 | F | clarification on the Qos parameters mapping and TSCAI creation | 16.3.0 |
| 2019-12 | SP#86 | SP-191073 | 1816 | - | F | Clarification on the Standardized or pre-configured 5QI parameters modification | 16.3.0 |
| 2019-12 | SP#86 | SP-191068 | 1817 | 1 | F | Expected UE behaviour data contents | 16.3.0 |
| 2019-12 | SP#86 | SP-191068 | 1818 | 2 | F | Correction of Small Data Rate Control interworking | 16.3.0 |
| 2019-12 | SP#86 | SP-191090 | 1819 | 1 | F | Network selection correction | 16.3.0 |
| 2019-12 | SP#86 | SP-191092 | 1821 | 3 | F | Clarification of SMF management of 5G-VN PDU sessions | 16.3.0 |
| 2019-12 | SP#86 | SP-191092 | 1822 | 3 | F | Clarification of UPF selection for 5G-VN communication | 16.3.0 |
| 2019-12 | SP#86 | SP-191092 | 1823 | 1 | F | Clarification of use of AF influence in 5G-VN | 16.3.0 |
| 2019-12 | SP#86 | SP-191088 | 1828 | 3 | F | Misleading RACS architecture pictures | 16.3.0 |
| 2019-12 | SP#86 | SP-191088 | 1829 | 6 | F | removing requirement that TAC+SV is used to identify UE model in manufacturer assigned ID | 16.3.0 |
| 2019-12 | SP#86 | SP-191086 | 1833 | 3 | F | changing IAB-MT to IAB-UE | 16.3.0 |
| 2019-12 | SP#86 | SP-191074 | 1837 | 2 | F | Correction on applicability of slicing to more than 3GPP access | 16.3.0 |
| 2019-12 | SP#86 | SP-191074 | 1839 | 2 | F | Incorrect reference to clause in specification | 16.3.0 |
| 2019-12 | SP#86 | SP-191090 | 1840 | 1 | F | Alignment with SA5 on Charging for 5G connection and mobility domain | 16.3.0 |
| 2019-12 | SP#86 | SP-191082 | 1842 | 3 | F | PDU Session with SSC mode 2/3 | 16.3.0 |
| 2019-12 | SP#86 | SP-191090 | 1845 | 3 | C | General description and data volume reporting for NR in unlicensed bands | 16.3.0 |
| 2019-12 | SP#86 | SP-191090 | 1847 | 2 | B | Access restrictions for primary and secondary RAT | 16.3.0 |
| 2019-12 | SP#86 | SP-191090 | 1849 | 1 | B | Introduction of UE specific DRX for NB-IOT | 16.3.0 |
| 2019-12 | SP#86 | SP-191074 | 1853 | 1 | A | Correction of QFI value in QER | 16.3.0 |
| 2019-12 | SP#86 | SP-191073 | 1854 | 5 | F | Management of GBR QoS Flows at handover | 16.3.0 |
| 2019-12 | SP#86 | SP-191092 | 1857 | 5 | F | Updates to the 5G VN broadcast solution | 16.3.0 |
| 2019-12 | SP#86 | SP-191090 | 1859 | 4 | F | PDU session anchor terminology clarification | 16.3.0 |
| 2019-12 | SP#86 | SP-191074 | 1860 | 4 | F | Remove incorrect reasoning of default MDBV value setting | 16.3.0 |
| 2019-12 | SP#86 | SP-191077 | 1868 | 5 | F | ATSSS Link-Specific Multipath IP Address Configuration | 16.3.0 |
| 2019-12 | SP#86 | SP-191077 | 1869 | 10 | F | ATSSS Steering of non-MPTCP Traffic | 16.3.0 |
| 2019-12 | SP#86 | SP-191077 | 1870 | 3 | F | ATSSS PMF Protocol over UDP | 16.3.0 |
| 2019-12 | SP#86 | SP-191077 | 1875 | 2 | F | Interworking with EPS for the MA PDU Session | 16.3.0 |
| 2019-12 | SP#86 | SP-191073 | 1878 | 2 | F | 5G URLLC Handling PDU Session Failure | 16.3.0 |
| 2019-12 | SP#86 | SP-191092 | 1879 | 2 | F | UPF selection for 5G URLLC PDU Sessions | 16.3.0 |
| 2019-12 | SP#86 | SP-191092 | 1881 | 3 | F | UE identifier for SNPN | 16.3.0 |
| 2019-12 | SP#86 | SP-191092 | 1887 | 2 | F | N4 Impacts - Bridge Management | 16.3.0 |
| 2019-12 | SP#86 | SP-191092 | 1888 | 5 | F | Clarification for TSC QoS Mapping clause | 16.3.0 |
| 2019-12 | SP#86 | SP-191092 | 1889 | 2 | F | TSC PDU Session Restrictions | 16.3.0 |
| 2019-12 | SP#86 | SP-191092 | 1890 | 7 | F | TSCAI granularity | 16.3.0 |
| 2019-12 | SP#86 | SP-191092 | 1893 | 3 | F | UPF functional update for TSC | 16.3.0 |
| 2019-12 | SP#86 | SP-191071 | 1895 | - | F | Clarification on SMF identifier in HR roaming | 16.3.0 |
| 2019-12 | SP#86 | SP-191068 | 1899 | 2 | F | Clarifications on CN assistance information sent to the RAN | 16.3.0 |
| 2019-12 | SP#86 | SP-191086 | 1901 | 1 | B | Handling of IAB-indication to 5GC | 16.3.0 |
| 2019-12 | SP#86 | SP-191086 | 1902 | 1 | B | Handling of OAM traffic for IAB-node | 16.3.0 |
| 2019-12 | SP#86 | SP-191086 | 1903 | 1 | B | Support of IAB operation in EN-DC mode | 16.3.0 |
| 2019-12 | SP#86 | SP-191086 | 1905 | 1 | F | Mobility support limitation for IAB | 16.3.0 |
| 2019-12 | SP#86 | SP-191078 | 1912 | - | F | Including IMS related interfaces in list of 5G interfaces | 16.3.0 |
| 2019-12 | SP#86 | SP-191090 | 1918 | - | F | Clarification on UE mobility event notification | 16.3.0 |
| 2019-12 | SP#86 | SP-191076 | 1920 | 1 | F | Avoid specifying SUPI / SUCI and PEI used for FN RG both in 23.501 and 23.316 | 16.3.0 |
| 2019-12 | SP#86 | SP-191077 | 1923 | 2 | F | Corrections to ATSSS capabilities of a MA PDU Session | 16.3.0 |
| 2019-12 | SP#86 | SP-191077 | 1924 | 1 | F | Applicability of UP Security Policy to a MA PDU Session | 16.3.0 |
| 2019-12 | SP#86 | SP-191082 | 1929 | 3 | F | (I)SMF notifications: which SMF events need to be supported by ISMF | 16.3.0 |
| 2019-12 | SP#86 | SP-191092 | 1932 | 2 | F | Clarification on the PDU session management for VN | 16.3.0 |
| 2019-12 | SP#86 | SP-191074 | 1934 | 1 | F | Correction on SMSF change | 16.3.0 |
| 2019-12 | SP#86 | SP-191074 | 1935 | 2 | F | Correction on UE context handling during inter system mobility | 16.3.0 |
| 2019-12 | SP#86 | SP-191088 | 1936 | 2 | F | Inclusion of Version Identifier in PLMN assigned ID | 16.3.0 |
| 2019-12 | SP#86 | SP-191077 | 1937 | 1 | F | Corrections for link-specific multipath address/prefix and MPTCP proxy IP address | 16.3.0 |
| 2019-12 | SP#86 | SP-191074 | 1940 | 3 | F | Selecting SMF that support static IP address | 16.3.0 |
| 2019-12 | SP#86 | SP-191090 | 1941 | 4 | F | Number of EBIs | 16.3.0 |
| 2019-12 | SP#86 | SP-191071 | 1942 | 2 | F | Notification URI | 16.3.0 |
| 2019-12 | SP#86 | SP-191082 | 1943 | 2 | F | I-SMF handling of N4 Information | 16.3.0 |
| 2019-12 | SP#86 | SP-191090 | 1945 | - | F | Correction of implementation of CR #1321 | 16.3.0 |
| 2019-12 | SP#86 | SP-191074 | 1949 | 1 | F | Clarification on the PCF selection | 16.3.0 |
| 2019-12 | SP#86 | SP-191074 | 1956 | - | A | Removal of wrongly implemented Network Slicing CR #1031 and mirror CR #1131 | 16.3.0 |
| 2019-12 | SP#86 | SP-191073 | 1971 | - | F | Correction on support of redundant transmission on N3/N9 interfaces | 16.3.0 |
| 2019-12 | SP#86 | SP-191068 | 1972 | - | F | Clarification on Control Plane Only Indicator | 16.3.0 |
| 2019-12 | SP#86 | SP-191073 | 1973 | 1 | F | Correction and clarification to AF influence in URLLC | 16.3.0 |
| 2019-12 | SP#86 | SP-191074 | 1976 | 2 | F | ULCL/BP based on the local routing policy | 16.3.0 |
| 2019-12 | SP#86 | SP-191081 | 1979 | 2 | F | On NSSAA Services | 16.3.0 |
| 2019-12 | SP#86 | SP-191092 | 1981 | 5 | F | Applying Per-Stream Filtering and Policing | 16.3.0 |
| 2019-12 | SP#86 | SP-191074 | 1985 | 1 | A | S-NSSAI setting for emergency service | 16.3.0 |
| 2019-12 | SP#86 | SP-191074 | 1986 | 2 | B | Solution on support of NAT in 5GS | 16.3.0 |
| 2019-12 | SP#86 | SP-191080 | 1992 | 1 | F | Corrections to NWDAF discovery and selection | 16.3.0 |
| 2019-12 | SP#86 | SP-191068 | 1993 | - | F | UE support of CP optimization over NB-IoT | 16.3.0 |
| 2019-12 | SP#86 | SP-191071 | 1994 | 1 | F | Correction of CHF discovery to consider eSBA binding principles | 16.3.0 |
| 2019-12 | SP#86 | SP-191092 | 1997 | 3 | F | PNI-NPN - Reusing NSSAI for AMF selection when NPN isolation is needed | 16.3.0 |
| 2019-12 | SP#86 | SP-191084 | 2001 | - | F | Correction on the support of V2X in 5GS | 16.3.0 |
| 2019-12 | SP#86 | SP-191086 | 2003 | - | F | Remove protocol stack diagrams for IAB | 16.3.0 |
| 2019-12 | SP#86 | SP-191086 | 2004 | 1 | F | Remove Editor's Notes for IAB related clauses | 16.3.0 |
| 2019-12 | SP#86 | SP-191081 | 2005 | 1 | F | Correction on pending NSSAA indication to UE | 16.3.0 |
| 2019-12 | SP#86 | SP-191082 | 2006 | - | F | ETSUN: correction for I-SMF trace | 16.3.0 |
| 2020-03 | SP#87E | SP-200075 | 1482 | 7 | F | Alignments and corrections to Non-Public Network functionality | 16.4.0 |
| 2020-03 | SP#87E | SP-200075 | 1520 | 4 | F | PLMN+CAG information - minimum, maximum storage and survival of power cycle | 16.4.0 |
| 2020-03 | SP#87E | SP-200075 | 1595 | 2 | F | 23.501 Supporting for AF providing UE IP address(es) for 5G VN group PDU sessions | 16.4.0 |
| 2020-03 | SP#87E | SP-200062 | 1668 | 4 | F | Clarification to MICO mode and Periodic Registration Timer Control | 16.4.0 |
| 2020-03 | SP#87E | SP-200062 | 1691 | 3 | F | Alignment with TS 23.502 and clarification on Extended Buffering | 16.4.0 |
| 2020-03 | SP#87E | SP-200075 | 1749 | 7 | F | Item#4: Apply StaticFilteringEntry information in 5GS | 16.4.0 |
| 2020-03 | SP#87E | SP-200069 | 1782 | 4 | F | Applicability of PS data off to ATSSS and MA PDU sessions | 16.4.0 |
| 2020-03 | SP#87E | SP-200078 | 1783 | 6 | F | UE IDLE over N3GPP responding to indication of DL data when access is available | 16.4.0 |
| 2020-03 | SP#87E | SP-200075 | 1799 | 7 | F | Support of CAG ID privacy | 16.4.0 |
| 2020-03 | SP#87E | SP-200078 | 1848 | 14 | F | Introduction of the Inter PLMN UP functionality in the architecture | 16.4.0 |
| 2020-03 | SP#87E | SP-200075 | 1882 | 4 | F | UDM - AUSF Discovery &amp; Selection in an SNPN | 16.4.0 |
| 2020-03 | SP#87E | SP-200069 | 1947 | 3 | F | Corrections to general MA PDU session handling | 16.4.0 |
| 2020-03 | SP#87E | SP-200075 | 1951 | 4 | F | Clarifying gPTP message forwarding for multiple TSN PDU sessions | 16.4.0 |
| 2020-03 | SP#87E | SP-200069 | 1957 | 2 | F | Adding ATSSS functionality into the UPF | 16.4.0 |
| 2020-03 | SP#87E | SP-200075 | 1980 | 3 | F | MDBV mapping and configuration for TSC QoS Flow | 16.4.0 |
| 2020-03 | SP#87E | SP-200075 | 2007 | 1 | F | Correction on TSCAI: TSN open issue #1 | 16.4.0 |
| 2020-03 | SP#87E | SP-200075 | 2009 | 1 | F | Correct errors in Port Management information table | 16.4.0 |
| 2020-03 | SP#87E | SP-200071 | 2011 | 1 | F | Re-allowing UE for services after the NSSAA revocation | 16.4.0 |
| 2020-03 | SP#87E | SP-200078 | 2015 | 2 | F | CN component of the PDB is configured per UL and DL | 16.4.0 |
| 2020-03 | SP#87E | SP-200078 | 2017 | 1 | F | Correcting AMF selection | 16.4.0 |
| 2020-03 | SP#87E | SP-200075 | 2019 | 2 | F | Procedures for handover between SNPN and PLMN | 16.4.0 |
| 2020-03 | SP#87E | SP-200078 | 2020 | 3 | F | MTU size considerations | 16.4.0 |
| 2020-03 | SP#87E | SP-200065 | 2021 | 4 | F | Binding for notification reselection corrections | 16.4.0 |
| 2020-03 | SP#87E | SP-200065 | 2022 | 3 | F | Correcting delegated discovery for PCF | 16.4.0 |
| 2020-03 | SP#87E | SP-200075 | 2026 | 1 | F | Correction of current context and using 5GS bridge to refer to 5GS functions act as TSN bridge | 16.4.0 |
| 2020-03 | SP#87E | SP-200068 | 2027 | 2 | F | Support of Wireline access requires both N1 signalling and N2 signalling | 16.4.0 |
| 2020-03 | SP#87E | SP-200075 | 2028 | 3 | F | Clarification on the 5G VN usage of IP Multicast mechanisms from TS 23.316 | 16.4.0 |
| 2020-03 | SP#87E | SP-200075 | 2029 | 4 | F | Usage of Ethernet PDU Session Information to support 5G VN Group point to point Ethernet traffic | 16.4.0 |
| 2020-03 | SP#87E | SP-200072 | 2030 | 1 | F | Criteria for I-SMF (and V-SMF) selection and change including also ATSSS cases | 16.4.0 |
| 2020-03 | SP#87E | SP-200078 | 2031 | 1 | F | Support of TNAP identifier when the Trusted Access does not correspond to WLAN | 16.4.0 |
| 2020-03 | SP#87E | SP-200069 | 2032 | 3 | F | ATSSS capabilities cooperation between the UE and UPF | 16.4.0 |
| 2020-03 | SP#87E | SP-200068 | 2033 | 4 | F | Access type and RAT type per Non-3GPP accesses | 16.4.0 |
| 2020-03 | SP#87E | SP-200062 | 2035 | - | F | Service Gap Control handling at UE side during IWK | 16.4.0 |
| 2020-03 | SP#87E | SP-200069 | 2036 | 2 | F | Corrections for handling of serving networks not supporting ATSSS | 16.4.0 |
| 2020-03 | SP#87E | SP-200078 | 2038 | 2 | F | Requested NSSAI provided at the AS layer | 16.4.0 |
| 2020-03 | SP#87E | SP-200071 | 2040 | 1 | F | Clarification on pending NSSAI in Network Slice-Specific Authentication and Authorization | 16.4.0 |
| 2020-03 | SP#87E | SP-200075 | 2042 | 4 | F | Item #5 Support of emergency services for Rel-16 UE not supporting CAG in CAG cells | 16.4.0 |
| 2020-03 | SP#87E | SP-200069 | 2044 | 1 | F | Clarification the deregistration in single access | 16.4.0 |
| 2020-03 | SP#87E | SP-200075 | 2046 | 2 | F | Clarification of N2 based handover considering CAG IDs supported by the target NG-RAN node | 16.4.0 |
| 2020-03 | SP#87E | SP-200068 | 2047 | 1 | F | TS23.501 - Correction on User Location Information | 16.4.0 |
| 2020-03 | SP#87E | SP-200072 | 2048 | - | F | Paging Policy Differentiation | 16.4.0 |
| 2020-03 | SP#87E | SP-200075 | 2050 | 2 | F | TSN CN PDB | 16.4.0 |
| 2020-03 | SP#87E | SP-200069 | 2051 | - | F | Access availability report configuration in the UPF | 16.4.0 |
| 2020-03 | SP#87E | SP-200062 | 2053 | 3 | B | Assistance indication for WUS grouping | 16.4.0 |
| 2020-03 | SP#87E | SP-200078 | 2054 | 2 | F | Correction on MDBV and CN PDB | 16.4.0 |
| 2020-03 | SP#87E | SP-200078 | 2056 | 2 | F | Default ARP values for dedicated QoS Flows | 16.4.0 |
| 2020-03 | SP#87E | SP-200078 | 2057 | 1 | F | Correction of ARP description | 16.4.0 |
| 2020-03 | SP#87E | SP-200078 | 2060 | 4 | F | Clarification on the EBI context if target MME does not support EBI extension during 5GS to EPS mobility | 16.4.0 |
| 2020-03 | SP#87E | SP-200075 | 2064 | 3 | F | Item#4: Clarification on the PSFP and Qbv for TSC traffic | 16.4.0 |
| 2020-03 | SP#87E | SP-200075 | 2067 | 1 | F | Clarifying TSCAI based on TSN clock used by PSFP gate operation | 16.4.0 |
| 2020-03 | SP#87E | SP-200075 | 2069 | 5 | F | Clarifying UL configuration issue | 16.4.0 |
| 2020-03 | SP#87E | SP-200075 | 2070 | 2 | F | Traffic Forwarding issue at UPF side | 16.4.0 |
| 2020-03 | SP#87E | SP-200075 | 2073 | 2 | F | #1_Clarification for supporting 5G VN group communication | 16.4.0 |
| 2020-03 | SP#87E | SP-200076 | 2074 | 3 | F | #2_clarification on N6-based traffic forwarding of 5G-VN | 16.4.0 |
| 2020-03 | SP#87E | SP-200069 | 2079 | 1 | F | Clarification on multiple PDU Session anchors for a MA PDU Session | 16.4.0 |
| 2020-03 | SP#87E | SP-200076 | 2084 | 3 | F | Correction to Emergency services support by SNPN | 16.4.0 |
| 2020-03 | SP#87E | SP-200076 | 2085 | 4 | F | Correction to TSN stream aggregation and QoS parameter mapping guidelines | 16.4.0 |
| 2020-03 | SP#87E | SP-200078 | 2087 | 1 | F | Clarification on the use of reference points N14 and N26 | 16.4.0 |
| 2020-03 | SP#87E | SP-200062 | 2088 | 1 | F | NAS signalling of CP Relocation Indication Truncated 5G-S-TMSI Parameters | 16.4.0 |
| 2020-03 | SP#87E | SP-200062 | 2089 | 3 | F | Correction for MO Exception Data Rate and its inclusion in charging information | 16.4.0 |
| 2020-03 | SP#87E | SP-200076 | 2097 | 2 | F | Correction to Access SNPN via PLMN | 16.4.0 |
| 2020-03 | SP#87E | SP-200060 | 2100 | 1 | A | Alignment with SA5 on Charging for SMS over NAS | 16.4.0 |
| 2020-03 | SP#87E | SP-200064 | 2102 | 1 | F | NEF service to support location transfer | 16.4.0 |
| 2020-03 | SP#87E | SP-200074 | 2106 | 2 | F | UCMF provisioning correction | 16.4.0 |
| 2020-03 | SP#87E | SP-200078 | 2108 | 3 | F | Clarification on the CN tunnel info allocation and release | 16.4.0 |
| 2020-03 | SP#87E | SP-200078 | 2109 | 2 | F | Clarification on internal group ID usage | 16.4.0 |
| 2020-03 | SP#87E | SP-200065 | 2111 | 2 | F | Update of the binding related descriptions | 16.4.0 |
| 2020-03 | SP#87E | SP-200074 | 2116 | 1 | F | On UCMF discovery | 16.4.0 |
| 2020-03 | SP#87E | SP-200074 | 2117 | - | F | RACS and NB-IoT corrections | 16.4.0 |
| 2020-03 | SP#87E | SP-200067 | 2122 | 2 | F | Correction for the wrongly implemented CR1785r8 | 16.4.0 |
| 2020-03 | SP#87E | SP-200067 | 2123 | 5 | F | Corrections of Alternative QoS Profiles - proper TS version | 16.4.0 |
| 2020-03 | SP#87E | SP-200062 | 2128 | 1 | F | Sending EPS APN rate control information during PDU session establishment | 16.4.0 |
| 2020-03 | SP#87E | SP-200078 | 2132 | - | F | Correction to Reference Points for Non-3GPP Access | 16.4.0 |
| 2020-03 | SP#87E | SP-200076 | 2133 | 1 | F | Clarification of TSN stream and traffic class | 16.4.0 |
| 2020-03 | SP#87E | SP-200078 | 2136 | 1 | F | Correction to UE configuration update procedure conditions for re-registration | 16.4.0 |
| 2020-03 | SP#87E | SP-200076 | 2137 | 1 | F | Selecting network for Emergency services | 16.4.0 |
| 2020-03 | SP#87E | SP-200070 | 2140 | 1 | F | Corrections to UE mobility event notification | 16.4.0 |
| 2020-03 | SP#87E | SP-200069 | 2141 | - | F | QoS handling of MA PDU Session for interworking with N26 | 16.4.0 |
| 2020-03 | SP#87E | SP-200076 | 2143 | 1 | F | Correct the transfer and determination of the bridge delay related parameters | 16.4.0 |
| 2020-03 | SP#87E | SP-200062 | 2147 | 1 | F | PDU Session release when Control Plane Only indication becomes not applicable | 16.4.0 |
| 2020-03 | SP#87E | SP-200062 | 2148 | 1 | F | Correction on PTW determincation | 16.4.0 |
| 2020-03 | SP#87E | SP-200069 | 2150 | - | F | Correction on MA PDU Session request indication | 16.4.0 |
| 2020-03 | SP#87E | SP-200067 | 2154 | 1 | F | Update N4 rules to support QoS Monitoring and ATSSS | 16.4.0 |
| 2020-03 | SP#87E | SP-200081 | 2157 | - | F | Subscription based access restriction for E-UTRA in unlicensed | 16.4.0 |
| 2020-03 | SP#87E | SP-200062 | 2158 | 1 | F | Subscription based access restriction for LTE-M | 16.4.0 |
| 2020-03 | SP#87E | SP-200070 | 2159 | 1 | F | Clarification on NWDAF information maintained in NRF | 16.4.0 |
| 2020-03 | SP#87E | SP-200062 | 2160 | 1 | F | Missing capabilities in 5GMM Capability IE | 16.4.0 |
| 2020-03 | SP#87E | SP-200074 | 2161 | - | D | Editorial updates in RACS clauses | 16.4.0 |
| 2020-03 | SP#87E | SP-200062 | 2163 | - | D | Mega CR on editorial corrections for 5G_CIoT | 16.4.0 |
| 2020-03 | SP#87E | SP-200076 | 2164 | 1 | F | Correction to network selection with multiple subscribed SNPNs | 16.4.0 |
| 2020-03 | SP#87E | SP-200076 | 2165 | 1 | F | Clarification for Support for multiple TSN working domains | 16.4.0 |
| 2020-03 | SP#87E | SP-200072 | 2169 | 1 | F | ETSUN related CR for non-FASMO corrections | 16.4.0 |
| 2020-03 | SP#87E | SP-200076 | 2171 | - | F | Adding reference points in the Architecture to support Time Sensitive Communication | 16.4.0 |
| 2020-03 | SP#87E | SP-200076 | 2172 | 1 | F | UPF selection based on traffic classes and VLAN | 16.4.0 |
| 2020-03 | SP#87E | SP-200060 | 2175 | 1 | A | UE capability match request during the registration procedure | 16.4.0 |
| 2020-03 | SP#87E | SP-200076 | 2178 | - | F | Replace IEEE802.1Qbv with IEEE802.1Q | 16.4.0 |
| 2020-03 | SP#87E | SP-200076 | 2183 | 1 | F | Correction on QoS Flow Binding about TSN | 16.4.0 |
| 2020-03 | SP#87E | SP-200068 | 2186 | - | F | Correction for support of N5CW devices to access 5GC via trusted WLAN access networks | 16.4.0 |
| 2020-03 | SP#87E | SP-200065 | 2190 | 1 | F | Endpoint Address correction | 16.4.0 |
| 2020-03 | SP#87E | SP-200078 | 2191 | 1 | F | Clarification on PS Data Off for non-3GPP access PDU Session | 16.4.0 |
| 2020-03 | SP#87E | SP-200071 | 2192 | 1 | F | Handling of NSSAA during N2 handover procedure | 16.4.0 |
| 2020-03 | SP#87E | SP-200076 | 2194 | 1 | F | Clear description of Access to an SNPN | 16.4.0 |
| 2020-03 | SP#87E | SP-200078 | 2195 | 1 | F | AMF Management | 16.4.0 |
| 2020-03 | SP#87E | SP-200076 | 2197 | 1 | F | Vertical_LAN 5G-VN related CR for non-FASMO corrections | 16.4.0 |
| 2020-03 | SP#87E | SP-200076 | 2198 | 1 | F | Vertical_LAN TSN related CR for non-FASMO corrections | 16.4.0 |
| 2020-03 | SP#87E | SP-200076 | 2199 | - | F | Vertical_LAN NPN related CR for non-FASMO corrections | 16.4.0 |
| 2020-03 | SP#87E | SP-200078 | 2201 | 1 | F | Correction on area of interest used by SMF | 16.4.0 |
| 2020-03 | SP#87E | SP-200076 | 2202 | 1 | F | TSN working domain and aggregation | 16.4.0 |
| 2020-03 | SP#87E | SP-200076 | 2204 | 1 | F | Updates for Bridge Delay information reporting and QoS mapping | 16.4.0 |
| 2020-03 | SP#87E | SP-200076 | 2205 | - | F | Incorrect reference to IEEE 1588 Timestamp data type in normative Annex H.2 | 16.4.0 |
| 2020-03 | SP#87E | SP-200078 | 2209 | 1 | F | Clarification on network instance determination | 16.4.0 |
| 2020-03 | SP#87E | SP-200076 | 2212 | 1 | F | UPF selection based on TSN parameters and context correction | 16.4.0 |
| 2020-03 | SP#87E | SP-200068 | 2214 | 1 | F | Inclusion of Requested NSSAI in AN Parameters for non-3GPP access | 16.4.0 |
| 2020-03 | SP#87E | SP-200068 | 2216 | 1 | F | 5WWC related CR for non-FASMO corrections | 16.4.0 |
| 2020-03 | SP#87E | SP-200293 | 2179 | 3 | F | Change of the restriction of enhanced coverage | 16.4.0 |
| 2020-07 | SP#88E | SP-200433 | 2131 | 2 | F | Support of ETSUN and ATSSS | 16.5.0 |
| 2020-07 | SP#88E | SP-200424 | 2138 | 2 | F | Selection of direct vs indirect communication | 16.5.0 |
| 2020-07 | SP#88E | SP-200428 | 2153 | 1 | F | Steering modes for GBR traffic | 16.5.0 |
| 2020-07 | SP#88E | SP-200438 | 2170 | 2 | F | QoS container vs. TSCAI input container | 16.5.0 |
| 2020-07 | SP#88E | SP-200438 | 2217 | 1 | F | Fix terminology on maximum number of CAGs per cell instead of per NG-RAN node | 16.5.0 |
| 2020-07 | SP#88E | SP-200425 | 2222 | 1 | F | Update of QoS monitoring for URLLC based on RAN WG3 decision | 16.5.0 |
| 2020-07 | SP#88E | SP-200438 | 2223 | 1 | F | Clarification on the supported and non-supported features and services for SNPN | 16.5.0 |
| 2020-07 | SP#88E | SP-200438 | 2224 | 1 | F | SMF to request the UE IP address from the DN-AAA server based on subscription information | 16.5.0 |
| 2020-07 | SP#88E | SP-200433 | 2225 | 1 | F | Support of ETSUN within and between PLMN(s) | 16.5.0 |
| 2020-07 | SP#88E | SP-200438 | 2227 | 1 | F | TSN QoS information for DL traffic | 16.5.0 |
| 2020-07 | SP#88E | SP-200437 | 2232 | - | F | Common Network Exposure | 16.5.0 |
| 2020-07 | SP#88E | SP-200438 | 2234 | 1 | F | Alignment of traffic forwarding information | 16.5.0 |
| 2020-07 | SP#88E | SP-200436 | 2236 | 1 | F | Missing the Radio Capability Filtering linkage to the UE Radio Capability ID | 16.5.0 |
| 2020-07 | SP#88E | SP-200552 | 2238 | 1 | F | ARP values for additional QoS Flows | 16.5.0 |
| 2020-07 | SP#88E | SP-200428 | 2240 | - | F | Handling of mobility when target does not support ATSSS | 16.5.0 |
| 2020-07 | SP#88E | SP-200420 | 2242 | - | A | UE radio capability retrieval | 16.5.0 |
| 2020-07 | SP#88E | SP-200438 | 2246 | 1 | F | QoS parameters mapping: GFBR, ARP | 16.5.0 |
| 2020-07 | SP#88E | SP-200438 | 2247 | 1 | F | UPF selection criteria | 16.5.0 |
| 2020-07 | SP#88E | SP-200438 | 2248 | - | F | Missing change in Annex I | 16.5.0 |
| 2020-07 | SP#88E | SP-200438 | 2251 | 1 | F | Correction on the derived MDBV | 16.5.0 |
| 2020-07 | SP#88E | SP-200436 | 2254 | - | F | Correction on the interface N58 b/w NEF and AF | 16.5.0 |
| 2020-07 | SP#88E | SP-200436 | 2255 | 1 | F | Support of multiple radio capability formats | 16.5.0 |
| 2020-07 | SP#88E | SP-200436 | 2257 | 1 | F | Clarification on Version ID | 16.5.0 |
| 2020-07 | SP#88E | SP-200428 | 2258 | 1 | F | Corrections to steering modes | 16.5.0 |
| 2020-07 | SP#88E | SP-200438 | 2263 | 1 | F | NF selection in SNPN 5GC | 16.5.0 |
| 2020-07 | SP#88E | SP-200432 | 2268 | 1 | F | Handling of pending NSSAI | 16.5.0 |
| 2020-07 | SP#88E | SP-200424 | 2269 | 2 | F | Enablers for multiple SCPs (23.501) | 16.5.0 |
| 2020-07 | SP#88E | SP-200432 | 2270 | 1 | F | Removal of service area for UE registration with empty Allowed NSSAI due to pending NSSAA | 16.5.0 |
| 2020-07 | SP#88E | SP-200424 | 2271 | 1 | F | Corrections to Principles for Binding, Selection and Reselection | 16.5.0 |
| 2020-07 | SP#88E | SP-200432 | 2274 | 1 | F | Clarification for the NSSAI in NSSAA procedure of roaming scenario | 16.5.0 |
| 2020-07 | SP#88E | SP-200428 | 2276 | 1 | F | MA-PDU Session establishment in Non-allowed Area | 16.5.0 |
| 2020-07 | SP#88E | SP-200422 | 2277 | 1 | F | Small data rate control enforcement of normal and exception data | 16.5.0 |
| 2020-07 | SP#88E | SP-200438 | 2278 | 1 | F | Correcting 5GS TSN bridge delays | 16.5.0 |
| 2020-07 | SP#88E | SP-200430 | 2279 | 1 | F | Corrections to HSS Discovery | 16.5.0 |
| 2020-07 | SP#88E | SP-200438 | 2285 | - | F | Annex I Clarification | 16.5.0 |
| 2020-07 | SP#88E | SP-200438 | 2287 | 1 | F | Bridge Management Clarification | 16.5.0 |
| 2020-07 | SP#88E | SP-200428 | 2292 | 1 | F | Correction on ATSSS rule generation | 16.5.0 |
| 2020-07 | SP#88E | SP-200425 | 2293 | 1 | F | Correction of RAN part of packet delay for QoS monitoring | 16.5.0 |
| 2020-07 | SP#88E | SP-200420 | 2299 | 1 | A | Incorrect NOTE 14 for 5QI 3 | 16.5.0 |
| 2020-07 | SP#88E | SP-200422 | 2302 | 1 | F | Corrections to restriction of use of Enhanced Coverage | 16.5.0 |
| 2020-07 | SP#88E | SP-200428 | 2303 | 1 | F | Corrections related to UPF support of RTT measurements without PMF | 16.5.0 |
| 2020-07 | SP#88E | SP-200438 | 2305 | 1 | F | Correction on RAN sharing for NPN networks | 16.5.0 |
| 2020-07 | SP#88E | SP-200427 | 2308 | 1 | F | Correction on RAT type | 16.5.0 |
| 2020-07 | SP#88E | SP-200427 | 2309 | - | F | Correction on wireline access and reference point between N5CW device and TWAP | 16.5.0 |
| 2020-07 | SP#88E | SP-200552 | 2311 | 1 | C | Remove restriction for support of eCall over NR | 16.5.0 |
| 2020-07 | SP#88E | SP-200433 | 2315 | 1 | F | Pause of Charging | 16.5.0 |
| 2020-07 | SP#88E | SP-200438 | 2319 | 1 | F | Alignment on Identifying PDU session in TSN AF | 16.5.0 |
| 2020-07 | SP#88E | SP-200438 | 2321 | 1 | F | Clarification on the bridge delay | 16.5.0 |
| 2020-07 | SP#88E | SP-200428 | 2327 | - | F | Correction of reference to mptcp RFC8684 | 16.5.0 |
| 2020-07 | SP#88E | SP-200438 | 2334 | 1 | F | Clarify the 5GS Bridge ID | 16.5.0 |
| 2020-07 | SP#88E | SP-200432 | 2336 | - | F | Correction on the value of S-NSSAIs for NSSAA | 16.5.0 |
| 2020-07 | SP#88E | SP-200551 | 2338 | 1 | F | Correction on description about area of interest | 16.5.0 |
| 2020-07 | SP#88E | SP-200551 | 2339 | 1 | F | Reordering DL data during SR procedure | 16.5.0 |
| 2020-07 | SP#88E | SP-200438 | 2340 | 1 | F | Correction for TSCAI Calculation | 16.5.0 |
| 2020-07 | SP#88E | SP-200551 | 2341 | - | F | Correction on QoS handling for priority sessions | 16.5.0 |
| 2020-07 | SP#88E | SP-200438 | 2344 | 1 | F | Correction of the gPTP domain and the selection of UPF | 16.5.0 |
| 2020-07 | SP#88E | SP-200438 | 2346 | 1 | F | Update on 5G VN group subscription data retrieval | 16.5.0 |
| 2020-07 | SP#88E | SP-200551 | 2347 | 1 | F | Update on IPUPS functionality | 16.5.0 |
| 2020-07 | SP#88E | SP-200438 | 2348 | 1 | F | Support of 5G LAN-type service under ETSUN architecture | 16.5.0 |
| 2020-07 | SP#88E | SP-200551 | 2350 | - | F | Correction on AF influence on traffic routing | 16.5.0 |
| 2020-07 | SP#88E | SP-200551 | 2351 | 1 | F | Correction on Control and User Plane Protocol Stacks | 16.5.0 |
| 2020-07 | SP#88E | SP-200438 | 2352 | 1 | F | Support of emergency services for Rel-15 UE in CAG cells | 16.5.0 |
| 2020-07 | SP#88E | SP-200424 | 2353 | 1 | F | Update of NF profile | 16.5.0 |
| 2020-07 | SP#88E | SP-200438 | 2363 | 1 | F | VLAN Information configuration and information exchange | 16.5.0 |
| 2020-07 | SP#88E | SP-200433 | 2365 | 1 | F | MA PDU Session not supported in ETSUN case | 16.5.0 |
| 2020-07 | SP#88E | SP-200515 | 2230 | 2 | F | Splitting port management information into port- and bridge-specific information | 16.5.0 |
| 2020-07 | SP#88E | SP-200438 | 2135 | 5 | F | Updating the UE with new CAG information | 16.5.0 |
| 2020-07 | SP#88E | SP-200588 | 2370 | 2 | F | Alignment on Alternative QoS Profile (This CR was noted, corrected to implement CR2730R1 in v16.5.1) | 16.5.0 |
| 2020-07 | SP#88E | SP-200420 | 1732 | 5 | A | Reflective QoS | 16.5.0 |
| 2020-07 | SP#88E | SP-200422 | 2243 | 3 | F | Service Area Restriction clarification | 16.5.0 |
| 2020-07 | SP#88E | SP-200610 | 2361 | 3 | F | PDU Session release when Control Plane Only indication is not available | 16.5.0 |
| 2020-07 | SP#88E | SP-200432 | 2368 | 1 | F | PCO support for DNS over (D)TLS (avoiding attacks against DNS traffic) | 16.5.0 |
| 2020-07 | SP#88E | SP-200427 | 2369 | 1 | F | Clarification of the Support of the Frame Routing Feature | 16.5.0 |
| 2020-07 | SP#88E | SP-200433 | 2371 | 1 | F | URLLC - TSN interworking with ETSUN | 16.5.0 |
| 2020-07 | SP#88E | SP-200432 | 2372 | - | F | Replacing AUSF by NSSAAF to support NSSAA | 16.5.0 |
| 2020-07 | SP#88E | SP-200422 | 2374 | - | F | Removal of I-NEF | 16.5.0 |
| 2020-07 | SP#88E | SP-200422 | 2378 | 1 | F | UE specific DRX for NB-IoT RAN support clarification based on LS R2-2004057 | 16.5.0 |
| 2020-07 | SP#88E | SP-200434 | 2379 | 1 | F | Capability for HPLMN to understand whether or not the NG-RAN node supports Alternative QoS Profiles | 16.5.0 |
| 2020-07 | SP#88E | SP-200438 | 2380 | 2 | F | Handling manipulation of CAG by VPLMN -Sol 1 | 16.5.0 |
| 2020-07 | SP#88E | SP-200435 | 2382 | 1 | F | IAB support in NPN deployment | 16.5.0 |
| 2020-08 | SP#88E | SP-200434 | 2370 | 1 | F | Alignment on Alternative QoS Profile (Correction to implementation of CR2730R2 from v16.5.0) | 16.5.1 |
| 2020-09 | SP#89E | SP-200688 | 2266 | 2 | F | Human readable name for SNPN | 16.6.0 |
| 2020-09 | SP#89E | SP-200685 | 2387 | - | F | Correction for URLLC GTP-U Path Monitoring | 16.6.0 |
| 2020-09 | SP#89E | SP-200687 | 2390 | - | F | HSS NF profile Update | 16.6.0 |
| 2020-09 | SP#89E | SP-200678 | 2391 | 1 | F | HSS Selection Update | 16.6.0 |
| 2020-09 | SP#89E | SP-200688 | 2392 | 1 | F | PSFP clarifications including IEEE LS response on TSN support | 16.6.0 |
| 2020-09 | SP#89E | SP-200688 | 2393 | 1 | F | Addressing technical comments from IEEE LS response on TSN support | 16.6.0 |
| 2020-09 | SP#89E | SP-200688 | 2394 | 1 | F | Addressing wording comments from IEEE LS response on TSN support | 16.6.0 |
| 2020-09 | SP#89E | SP-200688 | 2395 | 2 | F | Delay clarifications including IEEE LS input clarifications | 16.6.0 |
| 2020-09 | SP#89E | SP-200688 | 2396 | 1 | F | Solving Synchronization issues, addressing IEEE LS response | 16.6.0 |
| 2020-09 | SP#89E | SP-200688 | 2398 | 1 | F | Mapping GBR and Averaging Window | 16.6.0 |
| 2020-09 | SP#89E | SP-200686 | 2400 | 1 | C | UE user plane integrity protection mandatory at full rate | 16.6.0 |
| 2020-09 | SP#89E | SP-200688 | 2403 | 1 | F | Correction to TSN stream identification in PSFP information | 16.6.0 |
| 2020-09 | SP#89E | SP-200688 | 2404 | 1 | F | Correction and clarification related to the choice of PDU Session when exchanging BMIC or PMIC between TSN AF and NW-TT | 16.6.0 |
| 2020-09 | SP#89E | SP-200688 | 2405 | 1 | F | 5GS BMCA support and PTP port state configuration | 16.6.0 |
| 2020-09 | SP#89E | SP-200686 | 2407 | 1 | F | WUS system support for 5GC | 16.6.0 |
| 2020-09 | SP#89E | SP-200674 | 2409 | 1 | F | Routing Binding indication without delegated discovery | 16.6.0 |
| 2020-09 | SP#89E | SP-200688 | 2410 | 1 | F | Clarify the Announce message handling | 16.6.0 |
| 2020-09 | SP#89E | SP-200671 | 2420 | - | A | Clarification on concurrency of AS rekeying handling and Emergency Fallback procedure for R16 | 16.6.0 |
| 2020-09 | SP#89E | SP-200688 | 2421 | 1 | F | correction on the bridge model and NW-TT ports | 16.6.0 |
| 2020-09 | SP#89E | SP-200673 | 2424 | - | F | Overview Clarifications for multiple UP resource support for an NB-IoT UE | 16.6.0 |
| 2020-09 | SP#89E | SP-200673 | 2425 | - | F | Overview Clarifications about the CIoT optimisations during mobility to and from non-3GPP access | 16.6.0 |
| 2020-09 | SP#89E | SP-200673 | 2426 | - | F | Overview Clarifications for handling Control Plane CIoT optimisation during interworking between EPS and 5GS | 16.6.0 |
| 2020-09 | SP#89E | SP-200673 | 2427 | 1 | F | Drop downlink packets with notification of the discarded downlink packet | 16.6.0 |
| 2020-09 | SP#89E | SP-200673 | 2428 | - | F | Overview of redirecting UE via service reject to align with CT1 | 16.6.0 |
| 2020-09 | SP#89E | SP-200688 | 2430 | 1 | F | 23.501: Revision on PNI-NPN CAG Configuration Update | 16.6.0 |
| 2020-09 | SP#89E | SP-200674 | 2431 | 1 | F | Correction for NF instance set | 16.6.0 |
| 2020-09 | SP#89E | SP-200688 | 2435 | - | F | remove bridge name to align with CT3 | 16.6.0 |
| 2020-09 | SP#89E | SP-200688 | 2437 | 1 | F | Clarify Ethernet Frames handling for Ethernet PDU session | 16.6.0 |
| 2020-09 | SP#89E | SP-200688 | 2438 | 1 | F | dedicated SMF selection clarification | 16.6.0 |
| 2020-09 | SP#89E | SP-200688 | 2439 | 1 | F | 5G-VN clarifications | 16.6.0 |
| 2020-09 | SP#89E | SP-200688 | 2440 | 1 | F | Clarification on the 5G VN usage of IP Multicast mechanisms | 16.6.0 |
| 2020-09 | SP#89E | SP-200686 | 2442 | 1 | F | Support for DTLS | 16.6.0 |
| 2020-09 | SP#89E | SP-200673 | 2443 | 1 | F | Extended Connected Timer in mobility messages | 16.6.0 |
| 2020-09 | SP#89E | SP-200674 | 2444 | 1 | F | Clarifications on SCP registration and discovery procedures | 16.6.0 |
| 2020-09 | SP#89E | SP-200688 | 2446 | 1 | F | Resolution of open items related to IEEE LS | 16.6.0 |
| 2020-09 | SP#89E | SP-200674 | 2447 | 1 | F | Clarification on SCP selection to support multi-SCPs | 16.6.0 |
| 2020-09 | SP#89E | SP-200688 | 2449 | - | F | Change the Default QoS Flow to the QoS Flow with the default QoS rule | 16.6.0 |
| 2020-09 | SP#89E | SP-200688 | 2451 | 1 | F | Moving NW-TT ports from BMI into BMIC | 16.6.0 |
| 2020-09 | SP#89E | SP-200683 | 2452 | 1 | C | New 5QIs for OAM traffic over IAB | 16.6.0 |
| 2020-09 | SP#89E | SP-200677 | 2453 | - | F | RFC for draft-ietf-tcpm-converters | 16.6.0 |
| 2020-09 | SP#89E | SP-200688 | 2455 | 1 | F | Clarification of network sharing for NPN | 16.6.0 |
| 2020-09 | SP#89E | SP-200802 | 2383 | 2 | F | Signalling of UE Radio Capability ID in Registration procedure | 16.6.0 |
| 2020-12 | SP#90E | SP-200950 | 2228 | 4 | F | Correction of Alternative QoS Profile handling | 16.7.0 |
| 2020-12 | SP#90E | SP-200946 | 2389 | 1 | F | Handling of AAA-S address in NSSAA | 16.7.0 |
| 2020-12 | SP#90E | SP-200951 | 2408 | 2 | F | Indication of redundancy transmission | 16.7.0 |
| 2020-12 | SP#90E | SP-200953 | 2416 | 1 | F | TSCAI update during Handover procedure | 16.7.0 |
| 2020-12 | SP#90E | SP-200949 | 2456 | 1 | F | Correction on SMF change with eSBA | 16.7.0 |
| 2020-12 | SP#90E | SP-200953 | 2465 | 1 | F | Reject UE access to SNPN service via a PLMN to align with CT1 | 16.7.0 |
| 2020-12 | SP#90E | SP-200953 | 2466 | 1 | F | Clarification on gPTP handling at NW-TT acting as the GM | 16.7.0 |
| 2020-12 | SP#90E | SP-200953 | 2468 | 1 | F | 5G-VN clarifications | 16.7.0 |
| 2020-12 | SP#90E | SP-200953 | 2470 | - | F | Correction to inaccurate and misleading NOTE4 in the BMIC table | 16.7.0 |
| 2020-12 | SP#90E | SP-200953 | 2472 | - | F | Clarification of TSN AF role | 16.7.0 |
| 2020-12 | SP#90E | SP-200945 | 2474 | 1 | A | Correcting Xn handover at network sharing | 16.7.0 |
| 2020-12 | SP#90E | SP-200951 | 2475 | 1 | F | Correction to QoS monitoring for URLLC on GTP-U | 16.7.0 |
| 2020-12 | SP#90E | SP-200947 | 2476 | - | F | Exception data reporting and connected state | 16.7.0 |
| 2020-12 | SP#90E | SP-200959 | 2477 | - | F | V-SMF selection | 16.7.0 |
| 2020-12 | SP#90E | SP-200947 | 2481 | - | F | Correction on Enhanced Coverage Restriction | 16.7.0 |
| 2020-12 | SP#90E | SP-200947 | 2482 | - | F | Event Configuration Synchronization between 4G&amp;5G | 16.7.0 |
| 2020-12 | SP#90E | SP-200949 | 2483 | 1 | F | Group Id from AMF to SMF removal when SCP is responsible for reselection | 16.7.0 |
| 2020-12 | SP#90E | SP-200959 | 2485 | 1 | F | Continuation of PDU sessions upon mobility to a target PLMN | 16.7.0 |
| 2020-12 | SP#90E | SP-200953 | 2486 | 1 | F | Clarification of CAG information | 16.7.0 |
| 2020-12 | SP#90E | SP-200958 | 2487 | - | F | Removal of NSSAA related statements | 16.7.0 |
| 2020-12 | SP#90E | SP-200953 | 2488 | 1 | F | Alignment with CT specification on updating the UE with new CAG information | 16.7.0 |
| 2020-12 | SP#90E | SP-200959 | 2490 | 1 | F | Correction on AMF discovery and selection | 16.7.0 |
| 2020-12 | SP#90E | SP-200959 | 2499 | 1 | F | S-NSSAI handling at the Inter PLMN mobility | 16.7.0 |
| 2020-12 | SP#90E | SP-200959 | 2500 | - | F | Correction on mobility restriction | 16.7.0 |
| 2020-12 | SP#90E | SP-200959 | 2502 | 1 | F | Correction of AF use of Internal Group Identifier | 16.7.0 |
| 2020-12 | SP#90E | SP-200953 | 2504 | 1 | F | Clarification on UPF report Bridge ID | 16.7.0 |
| 2020-12 | SP#90E | SP-200954 | 2510 | - | F | Clarification on the construction of prioritized list of WLAN access networks for trusted access network selection | 16.7.0 |
| 2020-12 | SP#90E | SP-200953 | 2511 | 1 | F | Updates to N4 for NW-TT port number reporting | 16.7.0 |
| 2020-12 | SP#90E | SP-200953 | 2512 | 1 | F | TSN QoS determination | 16.7.0 |
| 2020-12 | SP#90E | SP-200953 | 2521 | 1 | F | N3IWF selection procedure when accessing SNPN via PLMN | 16.7.0 |
| 2020-12 | SP#90E | SP-200959 | 2523 | 1 | F | Mega CR to clean up | 16.7.0 |
| 2021-03 | SP#91E | SP-210243 | 2463 | 2 | F | Correction on Ethernet Type PDU session and MAC address association | 16.8.0 |
| 2021-03 | SP#91E | SP-210245 | 2531 | 1 | F | Clarification on LADN support for an MA PDU Session | 16.8.0 |
| 2021-03 | SP#91E | SP-210242 | 2532 | 1 | F | Correction of packet delay calculation for QoS monitoring | 16.8.0 |
| 2021-03 | SP#91E | SP-210081 | 2534 | 1 | F | Correction on the determination of S-NSSAI for interworking | 16.8.0 |
| 2021-03 | SP#91E | SP-210055 | 2535 | - | F | Correction on UE Radio Capability Handling during suspend | 16.8.0 |
| 2021-03 | SP#91E | SP-210243 | 2540 | 2 | F | Correction on gap analysis on charging for 5G service based architecture | 16.8.0 |
| 2021-03 | SP#91E | SP-210081 | 2546 | 1 | F | Correction of UE radio capability handling | 16.8.0 |
| 2021-03 | SP#91E | SP-210243 | 2555 | 1 | F | 5G-EIR Discovery and Selection | 16.8.0 |
| 2021-03 | SP#91E | SP-210242 | 2557 | 1 | F | Removal of erroneous RAN requirements | 16.8.0 |
| 2021-03 | SP#91E | SP-210081 | 2559 | 1 | F | Correction to Mobility Restrictions and Access Restrictions | 16.8.0 |
| 2021-03 | SP#91E | SP-210054 | 2569 | 1 | F | Support for IMS emergency from CAG non-supporting UE | 16.8.0 |
| 2021-03 | SP#91E | SP-210080 | 2570 | 1 | F | Handling of UTRAN UE radio capabilities | 16.8.0 |
| 2021-03 | SP#91E | SP-210244 | 2589 | - | F | Correction on reference to BBF | 16.8.0 |
| 2021-03 | SP#91E | SP-210243 | 2600 | 1 | F | IMS voice over PS Session Supported Indication taking into account UE S1 mode status | 16.8.0 |
| 2021-03 | SP#91E | SP-210054 | 2603 | 1 | F | clarification on the determination of the egress port for DL traffic | 16.8.0 |
| 2021-03 | SP#91E | SP-210054 | 2604 | - | F | Correction for reporting of 5GS Bridge information | 16.8.0 |
| 2021-03 | SP#91E | SP-210054 | 2605 | - | F | Clarification for the stream filter instance | 16.8.0 |
| 2021-03 | SP#91E | SP-210081 | 2622 | 1 | F | S-NSSAI for emergency services | 16.8.0 |
| 2021-03 | SP#91E | SP-210081 | 2623 | 1 | F | Inter PLMN mobility for emergency services | 16.8.0 |
| 2021-03 | SP#91E | SP-210081 | 2632 | 1 | F | NGAP UE-TNLA-binding update | 16.8.0 |
| 2021-03 | SP#91E | SP-210081 | 2636 | 1 | F | AMF reallocation during EPS to 5GS handover using N26 | 16.8.0 |
| 2021-03 | SP#91E | SP-210055 | 2641 | - | F | Clarification on support of QoS for Control Plane CIoT 5GS Optimisation | 16.8.0 |
| 2021-03 | SP#91E | SP-210242 | 2655 | 1 | F | Correction on QoS monitoring for URLLC | 16.8.0 |
| 2021-03 | SP#91E | SP-210055 | 2657 | 1 | F | Downlink data report by UPF | 16.8.0 |
| 2021-03 | SP#91E | SP-210081 | 2664 | - | F | Provide recommended cells for paging information in NGAP UE CONTEXT RESUME REQUEST message | 16.8.0 |
| 2021-03 | SP#91E | SP-210078 | 2665 | - | F | Remove the remaining editor's note for IAB descriptions | 16.8.0 |
| 2021-03 | SP#91E | SP-210077 | 2683 | 1 | F | Alternative QoS Profiles and Handover to Congested Cells | 16.8.0 |
| 2021-03 | SP#91E | SP-210067 | 2457 | 1 | B | Introduction of AKMA into the reference architecture | 17.0.0 |
| 2021-03 | SP#91E | SP-210088 | 2525 | 1 | B | Support of different slices over different Non 3GPP access | 17.0.0 |
| 2021-03 | SP#91E | SP-210068 | 2527 | 1 | B | MA PDU sessions with connectivity over E-UTRAN/EPC and non-3GPP access to 5GC | 17.0.0 |
| 2021-03 | SP#91E | SP-210072 | 2530 | 1 | B | Enchantments for supporting Supported Analytics Delay mechanism | 17.0.0 |
| 2021-03 | SP#91E | SP-210085 | 2536 | 1 | B | Multimedia Priority Service (MPS) Phase 2 support for Data Transport Service | 17.0.0 |
| 2021-03 | SP#91E | SP-210065 | 2537 | - | C | Selection of CN node by NG-RAN node providing satellite access across multiple countries | 17.0.0 |
| 2021-03 | SP#91E | SP-210065 | 2538 | 1 | C | Identification and mobility restrictions for satellite access | 17.0.0 |
| 2021-03 | SP#91E | SP-210084 | 2542 | 1 | B | KI#2-1: Capturing the FS_IIoT conclusions on static filtering entries | 17.0.0 |
| 2021-03 | SP#91E | SP-210088 | 2544 | 1 | C | IP index from UDM | 17.0.0 |
| 2021-03 | SP#91E | SP-210084 | 2549 | 1 | C | KI#1-4: Control of PTP functionality in DS-TT and NW-TT | 17.0.0 |
| 2021-03 | SP#91E | SP-210074 | 2550 | 1 | C | SNPN selection for access to SNPNs using credentials from an entity separate from the SNPN | 17.0.0 |
| 2021-03 | SP#91E | SP-210074 | 2551 | 1 | D | Informative guideline on how to keep the UE in CM-CONNECTED state in overlay network using existing release 16 mechanisms. | 17.0.0 |
| 2021-03 | SP#91E | SP-210088 | 2560 | 1 | B | 5G system architecture updates to support Dynamically Changing Policies in the 5GC | 17.0.0 |
| 2021-03 | SP#91E | SP-210088 | 2561 | - | B | DCAMP related update of BSF services (23.501) | 17.0.0 |
| 2021-03 | SP#91E | SP-210074 | 2563 | 1 | B | Informative guideline on supporting session/service continuity between SNPN and PLMN when using N3IWF | 17.0.0 |
| 2021-03 | SP#91E | SP-210072 | 2567 | 1 | B | Network Slice restriction based on NWDAF analytics | 17.0.0 |
| 2021-03 | SP#91E | SP-210087 | 2571 | 1 | C | New SST for High-Performance Machine-Type Communications (HMTC) | 17.0.0 |
| 2021-03 | SP#91E | SP-210084 | 2573 | 1 | B | Introduction of the architectures for Time Sensing Communication other than TSN. | 17.0.0 |
| 2021-03 | SP#91E | SP-210086 | 2574 | 1 | B | Introduction of Paging Cause feature | 17.0.0 |
| 2021-03 | SP#91E | SP-210072 | 2575 | 1 | B | NWDAF discovery and selection | 17.0.0 |
| 2021-03 | SP#91E | SP-210072 | 2576 | 1 | B | DCCF Discovery | 17.0.0 |
| 2021-03 | SP#91E | SP-210072 | 2577 | 1 | B | NWDAF Discovery | 17.0.0 |
| 2021-03 | SP#91E | SP-210072 | 2581 | 1 | B | Adding the usage of Redundant Transmission Experience analytics for URLLC service | 17.0.0 |
| 2021-03 | SP#91E | SP-210072 | 2582 | 1 | B | Adding the usage of extended UE Mobility analytics for LADN service | 17.0.0 |
| 2021-03 | SP#91E | SP-210068 | 2583 | 1 | B | PMF enhancements to support per QoS Flow measurements | 17.0.0 |
| 2021-03 | SP#91E | SP-210072 | 2584 | 1 | B | Extensions of NWDAF services | 17.0.0 |
| 2021-03 | SP#91E | SP-210072 | 2585 | 1 | B | NWDAF discovery and selection based on provided ML models | 17.0.0 |
| 2021-03 | SP#91E | SP-210072 | 2586 | 1 | B | UP path selection enhancement based on analytics info provided by NWDAF | 17.0.0 |
| 2021-03 | SP#91E | SP-210068 | 2587 | 1 | B | Packet Loss Rate measurements | 17.0.0 |
| 2021-03 | SP#91E | SP-210068 | 2590 | 1 | B | Applying thresholds to Load-Balancing steering mode in ATSSS | 17.0.0 |
| 2021-03 | SP#91E | SP-210064 | 2596 | 1 | B | AF Services for 5G ProSe | 17.0.0 |
| 2021-03 | SP#91E | SP-210084 | 2606 | 1 | B | KI#2 Supporting UE-UE TSC | 17.0.0 |
| 2021-03 | SP#91E | SP-210074 | 2611 | 1 | B | SNPN support AAA Server for primary authentication and authorization | 17.0.0 |
| 2021-03 | SP#91E | SP-210072 | 2614 | 1 | B | NWDAF discovery and selection for model sharing | 17.0.0 |
| 2021-03 | SP#91E | SP-210072 | 2615 | 1 | B | Triggers for network analytics | 17.0.0 |
| 2021-03 | SP#91E | SP-210084 | 2618 | 1 | B | KI#2 BMIC and PMIC for TSC without IEEE TSN network | 17.0.0 |
| 2021-03 | SP#91E | SP-210084 | 2619 | 1 | B | KI#3A - TSC Assistance container determined by NEF | 17.0.0 |
| 2021-03 | SP#91E | SP-210084 | 2620 | 1 | B | KI#1-3, UL Sync including New QoS Flow establishment for the gPTP | 17.0.0 |
| 2021-03 | SP#91E | SP-210084 | 2621 | 1 | C | KI#3 Updating AF functional description | 17.0.0 |
| 2021-03 | SP#91E | SP-210087 | 2624 | 1 | D | 23.501 Inclusive language review | 17.0.0 |
| 2021-03 | SP#91E | SP-210074 | 2625 | 1 | B | SNPN with separate entity hosting subscription | 17.0.0 |
| 2021-03 | SP#91E | SP-210084 | 2627 | 1 | C | Generalizing TSC clause 5.27 | 17.0.0 |
| 2021-03 | SP#91E | SP-210084 | 2628 | 1 | C | TSCAI applicability | 17.0.0 |
| 2021-03 | SP#91E | SP-210084 | 2629 | 1 | B | KI#3B-1: Exposure of Time synchronization as a service | 17.0.0 |
| 2021-03 | SP#91E | SP-210069 | 2634 | 1 | B | KI #1-1, I-SMF selection | 17.0.0 |
| 2021-03 | SP#91E | SP-210064 | 2637 | 1 | B | 5G Architecture reference model for ProSe | 17.0.0 |
| 2021-03 | SP#91E | SP-210072 | 2642 | 1 | B | Architectural changes to increasing efficiency of data collection | 17.0.0 |
| 2021-03 | SP#91E | SP-210088 | 2644 | 1 | B | Selecting the same PCF for AMF and SMF | 17.0.0 |
| 2021-03 | SP#91E | SP-210069 | 2646 | 1 | B | EC KI2 Target PSA buffering | 17.0.0 |
| 2021-03 | SP#91E | SP-210074 | 2648 | 1 | C | Support for normal IMS voice over SNPN | 17.0.0 |
| 2021-03 | SP#91E | SP-210065 | 2651 | 1 | C | 5QIs for satellite access | 17.0.0 |
| 2021-03 | SP#91E | SP-210089 | 2653 | 1 | B | Service Assistance Information for 3GPP Advanced Interactive Service | 17.0.0 |
| 2021-03 | SP#91E | SP-210068 | 2654 | 1 | B | Introduction of steering mode indicator | 17.0.0 |
| 2021-03 | SP#91E | SP-210069 | 2656 | 1 | B | Adding some parameters for local NEF selection | 17.0.0 |
| 2021-03 | SP#91E | SP-210072 | 2659 | 1 | B | Principle for logical decomposition of NWDAF | 17.0.0 |
| 2021-03 | SP#91E | SP-210088 | 2662 | 1 | B | Update to N3IWF selection for N3SLICE | 17.0.0 |
| 2021-03 | SP#91E | SP-210084 | 2668 | 1 | B | Support for PTP in time synchronization service and BMCA | 17.0.0 |
| 2021-03 | SP#91E | SP-210072 | 2670 | 1 | B | NWDAF new abbreviation | 17.0.0 |
| 2021-03 | SP#91E | SP-210069 | 2672 | 1 | B | AF Influence enhancement for EAS IP replacement | 17.0.0 |
| 2021-03 | SP#91E | SP-210064 | 2673 | - | B | Add general 5G ProSe support to 5GS | 17.0.0 |
| 2021-03 | SP#91E | SP-210065 | 2674 | 1 | C | Detection of satellite backhaul based on configuration information | 17.0.0 |
| 2021-03 | SP#91E | SP-210072 | 2677 | 1 | C | NWDAF discovery and selection for KI#2 NWDAF Reselection | 17.0.0 |
| 2021-03 | SP#91E | SP-210064 | 2678 | - | B | Introducing 5G DDNMF services for ProSe support | 17.0.0 |
| 2021-03 | SP#91E | SP-210083 | 2679 | 1 | B | TS23.501 KI#1 Network Slice Admission Control Function (NSACF) definition | 17.0.0 |
| 2021-03 | SP#91E | SP-210074 | 2684 | 1 | B | General introduction of Enhancements to Support SNPN along with credentials owned by an entity separate from the SNPN | 17.0.0 |
| 2021-03 | SP#91E | SP-210271 | 0254 | 3 | B | Network selection for NR satellite access | 17.0.0 |
| 2021-06 | SP#92E | SP-210323 | 2553 | 5 | B | Function Description for Multi-SIM devices | 17.1.0 |
| 2021-06 | SP#92E | SP-210353 | 2562 | 7 | B | UE onboarding | 17.1.0 |
| 2021-06 | SP#92E | SP-210359 | 2635 | 2 | B | KI #1-1, Update for supporting UL time sync with gPTP message | 17.1.0 |
| 2021-06 | SP#92E | SP-210345 | 2647 | 2 | B | PMF extensions for sending UE-assistance data to UPF | 17.1.0 |
| 2021-06 | SP#92E | SP-210354 | 2649 | 3 | C | Support for IMS emergency services over SNPN | 17.1.0 |
| 2021-06 | SP#92E | SP-210355 | 2680 | 3 | B | TS23.501 KI#2 Network Slice Admission Control Function (NSACF) definition | 17.1.0 |
| 2021-06 | SP#92E | SP-210344 | 2689 | 2 | B | 5MBS architecture | 17.1.0 |
| 2021-06 | SP#92E | SP-210359 | 2690 | 3 | B | Support for IEEE 1588 Boundary Clocks in time synchronization service | 17.1.0 |
| 2021-06 | SP#92E | SP-210346 | 2691 | 1 | B | Support for L2TP on N6 | 17.1.0 |
| 2021-06 | SP#92E | SP-210342 | 2693 | 1 | C | UE location verification for NR satellite access | 17.1.0 |
| 2021-06 | SP#92E | SP-210344 | 2696 | 4 | B | N4 extensions for 5MBS | 17.1.0 |
| 2021-06 | SP#92E | SP-210345 | 2697 | 1 | C | Handling of Ethernet PDU Session type for MA PDU Session with a 3GPP EPC leg | 17.1.0 |
| 2021-06 | SP#92E | SP-210337 | 2701 | 2 | B | New 5QI values to support Advance Interactive Services (AIS) in 5G | 17.1.0 |
| 2021-06 | SP#92E | SP-210351 | 2702 | 2 | B | Discover NWDAF for UE related Analytics using UDM | 17.1.0 |
| 2021-06 | SP#92E | SP-210351 | 2705 | 1 | B | CR to update NWDAF discovery and selection for MTLF | 17.1.0 |
| 2021-06 | SP#92E | SP-210355 | 2706 | 3 | B | Support for UE-Slice-MBR | 17.1.0 |
| 2021-06 | SP#92E | SP-210347 | 2707 | 1 | B | EASDF discovery and selection and update of edge computing description | 17.1.0 |
| 2021-06 | SP#92E | SP-210351 | 2708 | 1 | B | Adding the usage of Session Management Congestion Control Experience analytics | 17.1.0 |
| 2021-06 | SP#92E | SP-210353 | 2709 | 1 | B | Enabling restricted PDU Session for remote provisioning of UE via User Plane | 17.1.0 |
| 2021-06 | SP#92E | SP-210572 | 2714 | 4 | B | Remote provisioning of credentials for NSSAA or secondary authentication/authorisation | 17.1.0 |
| 2021-06 | SP#92E | SP-210353 | 2717 | 1 | B | Network access control by Credential Holder | 17.1.0 |
| 2021-06 | SP#92E | SP-210353 | 2718 | 4 | B | KI#2 T2: Informative guideline for mapping QoS parameters and DSCP marking | 17.1.0 |
| 2021-06 | SP#92E | SP-210355 | 2719 | 2 | B | Support of 5GC assisted cell selection to access network slice | 17.1.0 |
| 2021-06 | SP#92E | SP-210345 | 2720 | 1 | B | Decision to apply measurements per QoS Flow | 17.1.0 |
| 2021-06 | SP#92E | SP-210345 | 2721 | 5 | B | Send PMF messages to a target QoS Flow | 17.1.0 |
| 2021-06 | SP#92E | SP-210330 | 2723 | - | A | Correction to the N3IWF selection procedure | 17.1.0 |
| 2021-06 | SP#92E | SP-210355 | 2727 | 2 | B | NSACF functional descriptions | 17.1.0 |
| 2021-06 | SP#92E | SP-210355 | 2728 | 4 | B | Updates of NSACF discovery and selection | 17.1.0 |
| 2021-06 | SP#92E | SP-210355 | 2729 | 1 | B | NSAC support in roaming | 17.1.0 |
| 2021-06 | SP#92E | SP-210363 | 2736 | 4 | B | Clarification on UE provides PDU Session Pair ID based on URSP rules | 17.1.0 |
| 2021-06 | SP#92E | SP-210337 | 2740 | 2 | B | New standardized 5QI values for Advanced Interactive Services | 17.1.0 |
| 2021-06 | SP#92E | SP-210345 | 2743 | 3 | B | Introduction of UE-assistance operation | 17.1.0 |
| 2021-06 | SP#92E | SP-210345 | 2744 | 1 | B | Thresholds for Priority-based mode | 17.1.0 |
| 2021-06 | SP#92E | SP-210345 | 2746 | 3 | B | QoS Flow recognition for per QoS Flow measurements | 17.1.0 |
| 2021-06 | SP#92E | SP-210353 | 2755 | 3 | B | De-registration for onboarding registered UE | 17.1.0 |
| 2021-06 | SP#92E | SP-210347 | 2757 | 4 | B | AF Influence enhancement for EAS IP replacement | 17.1.0 |
| 2021-06 | SP#92E | SP-210351 | 2758 | 1 | B | Updating AMF exposed events in TS 23.501. | 17.1.0 |
| 2021-06 | SP#92E | SP-210351 | 2759 | 1 | B | Alignment of NWDAF discovery of data exposure capability in TS 23.501. | 17.1.0 |
| 2021-06 | SP#92E | SP-210351 | 2760 | 1 | F | Clarify the Supported Analytics Delay | 17.1.0 |
| 2021-06 | SP#92E | SP-210351 | 2761 | 4 | B | Update the NWDAF profile for ML Model | 17.1.0 |
| 2021-06 | SP#92E | SP-210347 | 2762 | 1 | B | SMF function update to support Edge computing enhancement | 17.1.0 |
| 2021-06 | SP#92E | SP-210347 | 2763 | 1 | B | Update of Edge Computing | 17.1.0 |
| 2021-06 | SP#92E | SP-210347 | 2765 | 1 | B | Adding EASDF services | 17.1.0 |
| 2021-06 | SP#92E | SP-210359 | 2768 | 1 | B | Update for support of TSC other than TSN | 17.1.0 |
| 2021-06 | SP#92E | SP-210359 | 2769 | 2 | B | Correction for Survival Time | 17.1.0 |
| 2021-06 | SP#92E | SP-210359 | 2773 | 3 | B | Update for PTP in time synchronization service and BMCA | 17.1.0 |
| 2021-06 | SP#92E | SP-210342 | 2781 | 1 | B | Support of new RATs in 5GS integrating satellite access | 17.1.0 |
| 2021-06 | SP#92E | SP-210363 | 2783 | 2 | F | (Mirror)Correct the NOTE for N6 | 17.1.0 |
| 2021-06 | SP#92E | SP-210355 | 2789 | 5 | B | Roaming support for NSAC | 17.1.0 |
| 2021-06 | SP#92E | SP-210363 | 2790 | 1 | B | Support GERAN/UTRAN access in SMF+PGW-C | 17.1.0 |
| 2021-06 | SP#92E | SP-210359 | 2791 | 1 | B | KI#3B, Resolving EN for Future PDU Session | 17.1.0 |
| 2021-06 | SP#92E | SP-210351 | 2795 | 1 | C | Add a use case for network slice load analytics | 17.1.0 |
| 2021-06 | SP#92E | SP-210353 | 2799 | 1 | B | Homogeneously support SNPN connectivity for UEs with credentials owned by Credentials Holder | 17.1.0 |
| 2021-06 | SP#92E | SP-210354 | 2801 | 2 | D | Correction to UE identifier sent to AMF by UE | 17.1.0 |
| 2021-06 | SP#92E | SP-210353 | 2802 | 1 | B | User Plane Remote Provisioning of UEs if PLMN as ON | 17.1.0 |
| 2021-06 | SP#92E | SP-210347 | 2804 | 3 | B | Edge relocation considering user plane lantecy requirement | 17.1.0 |
| 2021-06 | SP#92E | SP-210351 | 2805 | 1 | C | Use of TAI(s) for slice restriction based on analytics | 17.1.0 |
| 2021-06 | SP#92E | SP-210337 | 2806 | 1 | F | Packet size for PDB | 17.1.0 |
| 2021-06 | SP#92E | SP-210351 | 2807 | - | F | Corrections for ADRF services | 17.1.0 |
| 2021-06 | SP#92E | SP-210351 | 2808 | - | F | Reference to DCCF and MFAF Services description clause | 17.1.0 |
| 2021-06 | SP#92E | SP-210337 | 2809 | 1 | F | TSC Assistance Container Determination by PCF | 17.1.0 |
| 2021-06 | SP#92E | SP-210345 | 2811 | 2 | C | Introducing threshold conditions for priority-based steering mode in TS 23.501 | 17.1.0 |
| 2021-06 | SP#92E | SP-210355 | 2813 | 4 | B | Introduction of support of NG.116 attribute Simultaneous Use of a Network Slice | 17.1.0 |
| 2021-06 | SP#92E | SP-210341 | 2814 | 3 | F | The impact of UE N1 mode change in EPS | 17.1.0 |
| 2021-06 | SP#92E | SP-210353 | 2815 | 3 | B | KI#1 - T5, Enable mobility between networks | 17.1.0 |
| 2021-06 | SP#92E | SP-210359 | 2817 | 1 | B | Terminology on the TSC MIC and Bridge ID | 17.1.0 |
| 2021-06 | SP#92E | SP-210359 | 2820 | - | B | Fix the description on the ethernet port | 17.1.0 |
| 2021-06 | SP#92E | SP-210355 | 2822 | 4 | B | Introduction of support of GSMA NG.116 attributes Maximum DL/UL throughput per slice/UE | 17.1.0 |
| 2021-06 | SP#92E | SP-210353 | 2826 | 1 | B | Mobility support between SNPNs and between SNPN and PLMN | 17.1.0 |
| 2021-06 | SP#92E | SP-210353 | 2832 | 1 | B | UE configuration for remote provisioning | 17.1.0 |
| 2021-06 | SP#92E | SP-210359 | 2833 | 2 | B | Introduction of architecture for AF requested support of Time Sensitive Communication and Time Synchronization | 17.1.0 |
| 2021-06 | SP#92E | SP-210355 | 2837 | 3 | B | Support of Emergency and Priority Services in Network Slice Admission Control | 17.1.0 |
| 2021-06 | SP#92E | SP-210355 | 2838 | 2 | B | TS23.501 KI#4 NSACF event notification definition | 17.1.0 |
| 2021-06 | SP#92E | SP-210345 | 2840 | 1 | F | Packet Loss Rate Measurements | 17.1.0 |
| 2021-06 | SP#92E | SP-210363 | 2848 | 1 | F | FQDNs for N3IWF selection for emergency services | 17.1.0 |
| 2021-06 | SP#92E | SP-210347 | 2856 | 3 | B | Newly added parameters for Local NEF discovery | 17.1.0 |
| 2021-06 | SP#92E | SP-210341 | 2858 | 1 | F | Consistent handling of NF documentation | 17.1.0 |
| 2021-06 | SP#92E | SP-210340 | 2861 | 1 | B | ProSe related functional description | 17.1.0 |
| 2021-06 | SP#92E | SP-210347 | 2862 | - | B | EASDF functional description | 17.1.0 |
| 2021-06 | SP#92E | SP-210330 | 2865 | 1 | A | UE radio capability clarification | 17.1.0 |
| 2021-06 | SP#92E | SP-210358 | 2870 | 1 | B | UAV support feature inclusion | 17.1.0 |
| 2021-06 | SP#92E | SP-210341 | 2874 | 1 | F | Correction to the reference document for charging related reference points | 17.1.0 |
| 2021-06 | SP#92E | SP-210344 | 2880 | 1 | B | PCF impacts of 5MBS | 17.1.0 |
| 2021-06 | SP#92E | SP-210351 | 2881 | 1 | B | KI#8 - AF discovery and selection | 17.1.0 |
| 2021-06 | SP#92E | SP-210345 | 2886 | 1 | B | Partial ATSSS rule update by using ATSSS rule ID | 17.1.0 |
| 2021-06 | SP#92E | SP-210330 | 2888 | 1 | A | Subscription data updates for EPS/5GS interworking | 17.1.0 |
| 2021-06 | SP#92E | SP-210329 | 2889 | - | A | Updates on PCC rule triggered GTP-U path monitoring | 17.1.0 |
| 2021-06 | SP#92E | SP-210354 | 2892 | 1 | F | SNPN UE configuration and subscription aspects | 17.1.0 |
| 2021-06 | SP#92E | SP-210353 | 2893 | 1 | B | SNPN - SNPN Mobility - AMF selection impacts | 17.1.0 |
| 2021-06 | SP#92E | SP-210354 | 2894 | 1 | F | SNPN GIN Encoding | 17.1.0 |
| 2021-06 | SP#92E | SP-210359 | 2896 | 1 | C | Exposure of Time synchronization as a service - description | 17.1.0 |
| 2021-06 | SP#92E | SP-210347 | 2899 | 1 | B | N4 interface enhancement for local notification | 17.1.0 |
| 2021-06 | SP#92E | SP-210347 | 2900 | 1 | B | UPF function update to support network information exposure | 17.1.0 |
| 2021-06 | SP#92E | SP-210354 | 2902 | 1 | F | Simultaneous data service from PNI-NPN and PLMN | 17.1.0 |
| 2021-06 | SP#92E | SP-210354 | 2903 | 1 | F | IMS voice over overlay network | 17.1.0 |
| 2021-06 | SP#92E | SP-210359 | 2904 | 1 | F | KI#3A Support QoS mapping based on priority for TSC exposure | 17.1.0 |
| 2021-06 | SP#92E | SP-210359 | 2905 | 1 | F | Clarification on support of PTP GM function in TT | 17.1.0 |
| 2021-06 | SP#92E | SP-210359 | 2908 | 1 | F | Resolving EN for Hold and Forward mechanism | 17.1.0 |
| 2021-06 | SP#92E | SP-210355 | 2909 | 1 | B | Support multiple NSACFs for one S-NSSAI during UE mobility | 17.1.0 |
| 2021-06 | SP#92E | SP-210340 | 2910 | 1 | B | Update of reference points for 5G ProSe | 17.1.0 |
| 2021-06 | SP#92E | SP-210359 | 2911 | 1 | B | KI#3B, Temporal Validity Condition Description | 17.1.0 |
| 2021-06 | SP#92E | SP-210347 | 2913 | 1 | B | Updates to AF requests to influence traffic routing | 17.1.0 |
| 2021-06 | SP#92E | SP-210347 | 2914 | - | F | Update on I-SMF selection per DNAI | 17.1.0 |
| 2021-06 | SP#92E | SP-210353 | 2918 | 1 | B | KI#2 T1: Informative guideline for QoS Notification between overlay network and underlay network | 17.1.0 |
| 2021-06 | SP#92E | SP-210545 | 2923 | 2 | F | Allowed NSSAI when NSSAA fails | 17.1.0 |
| 2021-06 | SP#92E | SP-210355 | 2924 | 1 | B | Network Slice Admission Control in EPC | 17.1.0 |
| 2021-06 | SP#92E | SP-210354 | 2926 | 1 | C | Interaction between AUSF and AAA Server | 17.1.0 |
| 2021-06 | SP#92E | SP-210362 | 2927 | 1 | B | Introduction of MUSIM capability exchange | 17.1.0 |
| 2021-06 | SP#92E | SP-210330 | 2931 | 1 | A | Support for UPIP for other than NR | 17.1.0 |
| 2021-06 | SP#92E | SP-210347 | 2934 | 1 | F | Update on uplink traffic buffering | 17.1.0 |
| 2021-06 | SP#92E | SP-210347 | 2935 | 1 | F | AF Influence enhancement for EAS Rediscovery at Edge Relocation | 17.1.0 |
| 2021-06 | SP#92E | SP-210355 | 2937 | 1 | B | NSAC with consideration of access type | 17.1.0 |
| 2021-06 | SP#92E | SP-210351 | 2938 | 1 | C | NWDAF assisted DNAI and UPF selection at SMF | 17.1.0 |
| 2021-06 | SP#92E | SP-210354 | 2939 | 1 | F | Correction to scenarios of external authentication | 17.1.0 |
| 2021-06 | SP#92E | SP-210353 | 2940 | 1 | B | Clarification on NID | 17.1.0 |
| 2021-06 | SP#92E | SP-210341 | 2945 | 1 | F | Clarification on the number of Subscribed S-NSSAIs | 17.1.0 |
| 2021-06 | SP#92E | SP-210359 | 2946 | - | C | Definition of the UE-DS-TT residence time | 17.1.0 |
| 2021-06 | SP#92E | SP-210327 | 2947 | 1 | A | NIDD configuration correction | 17.1.0 |
| 2021-06 | SP#92E | SP-210342 | 2948 | 1 | C | Removal of UPF indication of backhaul QoS to SMF | 17.1.0 |
| 2021-06 | SP#92E | SP-210353 | 2952 | 1 | B | HRNN in manual network selection for SNPNs | 17.1.0 |
| 2021-06 | SP#92E | SP-210341 | 2953 | 1 | F | Clarification on the Standardized SST values | 17.1.0 |
| 2021-06 | SP#92E | SP-210353 | 2955 | 1 | B | AMF selection to support UE onboarding SNPN | 17.1.0 |
| 2021-06 | SP#92E | SP-210359 | 2959 | - | F | Grandmaster candidate enabled management information per PTP instance | 17.1.0 |
| 2021-06 | SP#92E | SP-210359 | 2960 | 1 | C | Time Synchronization service exposure | 17.1.0 |
| 2021-06 | SP#92E | SP-210371 | 2962 | 2 | F | Clarification of applicability of port/bridge management information | 17.1.0 |
| 2021-06 | SP#92E | SP-210336 | 2963 | 1 | A | Clarification for Visited Country FQDN DNS query for SNPNs with locally assigned NIDs | 17.1.0 |
| 2021-06 | SP#92E | SP-210354 | 2965 | 1 | C | AUSF selection for an Onboarding UE | 17.1.0 |
| 2021-06 | SP#92E | SP-210353 | 2969 | 1 | B | Definition of SNPN-related terms | 17.1.0 |
| 2021-06 | SP#92E | SP-210341 | 2970 | 1 | B | 4G &lt;-&gt; 5GS mobility corrections to cope with areas of GERAN/UTRAN-only coverage | 17.1.0 |
| 2021-06 | SP#92E | SP-210361 | 2971 | 1 | B | Additional authorization functionality in support of MPS for Data Transport Service | 17.1.0 |
| 2021-06 | SP#92E | SP-210346 | 2973 | 1 | B | L2TP information provision | 17.1.0 |
| 2021-06 | SP#92E | SP-210359 | 2977 | 1 | B | Clarification on TSCAI for the non TSC service | 17.1.0 |
| 2021-06 | SP#92E | SP-210330 | 2982 | 1 | A | AMF to consider S1 mode capability into account when setting EMF and EMC | 17.1.0 |
| 2021-06 | SP#92E | SP-210335 | 2984 | 1 | A | Correction to trigger for UE Radio Capability Update procedure | 17.1.0 |
| 2021-06 | SP#92E | SP-210331 | 2990 | - | A | Correction on non-3GPP access type | 17.1.0 |
| 2021-06 | SP#92E | SP-210331 | 2991 | 1 | F | Adding PDU session limitation and protocol stacks for trusted WLAN access for N5CW device | 17.1.0 |
| 2021-06 | SP#92E | SP-210354 | 2992 | - | F | UE configuration for remote provisioning | 17.1.0 |
| 2021-06 | SP#92E | - | - | - | - | MCC Correction to move 5.15.11.14 to 5.15.11.5 | 17.1.1 |
| 2021-09 | SP#93E | SP-210916 | 2748 | 3 | C | Support of Mobility Registration Update for 5G Satellite Access | 17.2.0 |
| 2021-09 | SP#93E | SP-210923 | 2919 | 2 | B | IMSI based SUPI support when access an SNPN using credentials owned by CH | 17.2.0 |
| 2021-09 | SP#93E | SP-210923 | 2921 | 2 | B | UE onboarding architecture | 17.2.0 |
| 2021-09 | SP#93E | SP-210915 | 2993 | 1 | F | Clarifying that at least one default S-NSSAI is mandatory | 17.2.0 |
| 2021-09 | SP#93E | SP-210925 | 2994 | 1 | F | correction to the re-configuration requirements for NSSRG non-supporting UEs | 17.2.0 |
| 2021-09 | SP#93E | SP-210925 | 2995 | - | F | clarification on obtaining the Configured NSSAI from NSSF when NSSRG for UE changes | 17.2.0 |
| 2021-09 | SP#93E | SP-210911 | 2998 | 1 | A | Enforcing CAG restrictions during E-UTRAN to NG-RAN connected mode mobility | 17.2.0 |
| 2021-09 | SP#93E | SP-210923 | 2999 | 1 | F | Update of Credentials Holder controlled prioritized lists of preferred SNPNs and GINs using SoR | 17.2.0 |
| 2021-09 | SP#93E | SP-210922 | 3001 | 1 | F | TS 23.288 reference update for ADRF services | 17.2.0 |
| 2021-09 | SP#93E | SP-210922 | 3002 | 1 | F | Resolving editor's note for ADRF discovery and selection | 17.2.0 |
| 2021-09 | SP#93E | SP-210910 | 3003 | 1 | A | Handling of UE Radio Capability for Paging | 17.2.0 |
| 2021-09 | SP#93E | SP-210925 | 3004 | 1 | F | Missing Definition of Target NSSAI | 17.2.0 |
| 2021-09 | SP#93E | SP-210935 | 3009 | 1 | B | EPS User Plane Integrity Protection using SMF+PGW-C | 17.2.0 |
| 2021-09 | SP#93E | SP-210919 | 3010 | 1 | C | Allowing usage of S-NSSAI and Network Instance for internal UPF resource allocation | 17.2.0 |
| 2021-09 | SP#93E | SP-210937 | 3011 | - | F | BSF related update of NRF services (23.501) | 17.2.0 |
| 2021-09 | SP#93E | SP-210928 | 3018 | 1 | F | NEF discovery and selection based on AF address | 17.2.0 |
| 2021-09 | SP#93E | SP-210931 | 3019 | 1 | B | Adding the functionality on MINT | 17.2.0 |
| 2021-09 | SP#93E | SP-210920 | 3025 | 1 | B | NEF service to support EAS deployment info | 17.2.0 |
| 2021-09 | SP#93E | SP-210920 | 3026 | - | F | AF Request for Simultaneous Connectivity over Source and Target PSA at Edge Relocation | 17.2.0 |
| 2021-09 | SP#93E | SP-210918 | 3027 | 1 | F | UE-assistance operation on traffic aggregate granularity | 17.2.0 |
| 2021-09 | SP#93E | SP-210916 | 3029 | 1 | C | PDB value for 5QI 10 | 17.2.0 |
| 2021-09 | SP#93E | SP-210906 | 3033 | 1 | F | ATSSS Rule ID | 17.2.0 |
| 2021-09 | SP#93E | SP-210914 | 3034 | 1 | F | Update the naming convention for the reference points for 5G ProSe | 17.2.0 |
| 2021-09 | SP#93E | SP-210937 | 3035 | 1 | F | 5G URLLC Redundant PDU Session correction for NGAP parameters | 17.2.0 |
| 2021-09 | SP#93E | SP-210923 | 3036 | 1 | F | GIN Encoding | 17.2.0 |
| 2021-09 | SP#93E | SP-210929 | 3038 | 1 | F | TSN AF functional description and reference point | 17.2.0 |
| 2021-09 | SP#93E | SP-210929 | 3039 | 1 | F | Updates for time synchronization text - description | 17.2.0 |
| 2021-09 | SP#93E | SP-210929 | 3040 | 1 | F | Architecture to enable Time Sensitive Communication and Time Synchronization | 17.2.0 |
| 2021-09 | SP#93E | SP-210929 | 3041 | 1 | F | Updates for TSCTSF text - description | 17.2.0 |
| 2021-09 | SP#93E | SP-210929 | 3042 | 1 | C | Exposure of Time synchronization as a service - description | 17.2.0 |
| 2021-09 | SP#93E | SP-210937 | 3043 | - | F | Correction on Redundant PDU Session | 17.2.0 |
| 2021-09 | SP#93E | SP-210915 | 3044 | 1 | F | Updates to enable mobility between GERAN/UTRAN and E-UTRAN in 5GS | 17.2.0 |
| 2021-09 | SP#93E | SP-210923 | 3045 | 1 | F | Handling of SUPI/SUCI format when accessing to a SNPN | 17.2.0 |
| 2021-09 | SP#93E | SP-210932 | 3048 | - | F | Update Paging Cause Feature in 5GS | 17.2.0 |
| 2021-09 | SP#93E | SP-210923 | 3049 | 1 | F | KI#4-SNPN UE Onboarding using existing DNN | 17.2.0 |
| 2021-09 | SP#93E | SP-210929 | 3051 | 1 | D | Correcting the usage of Survival Time | 17.2.0 |
| 2021-09 | SP#93E | SP-210923 | 3052 | 1 | B | Informative guidelines for usage of QoS related exposure capabilities to leverage between underlay network and overlay network | 17.2.0 |
| 2021-09 | SP#93E | SP-210915 | 3054 | 1 | F | Correction on Charging | 17.2.0 |
| 2021-09 | SP#93E | SP-210903 | 3057 | 1 | A | Derivation of UL Packet Filter from DL encapsulated IPsec protected packet | 17.2.0 |
| 2021-09 | SP#93E | SP-210936 | 3062 | 1 | C | Explicit indication for ATC | 17.2.0 |
| 2021-09 | SP#93E | SP-210936 | 3064 | - | F | Corrections on the AF related identifier | 17.2.0 |
| 2021-09 | SP#93E | SP-210937 | 3065 | 1 | F | Corrections on geographical area | 17.2.0 |
| 2021-09 | SP#93E | SP-210925 | 3066 | 1 | F | Addition of NSACF services | 17.2.0 |
| 2021-09 | SP#93E | SP-210925 | 3067 | 1 | F | Redirection to dedicated frequency band(s) at the end of NSSAA | 17.2.0 |
| 2021-09 | SP#93E | SP-210925 | 3072 | 1 | F | KI#5 UE-Slice-MBR enforcement in PCF | 17.2.0 |
| 2021-09 | SP#93E | SP-210925 | 3074 | 1 | B | Roaming support for NSAC in VPLMN | 17.2.0 |
| 2021-09 | SP#93E | SP-210925 | 3077 | 1 | F | Support of multiple NSACF instance | 17.2.0 |
| 2021-09 | SP#93E | SP-210922 | 3079 | - | F | Update to AF Discovery and Selection | 17.2.0 |
| 2021-09 | SP#93E | SP-210923 | 3084 | - | F | Interaction between PVS and SO-SNPN | 17.2.0 |
| 2021-09 | SP#93E | SP-210923 | 3085 | - | C | DCS providing PVS address to ONN | 17.2.0 |
| 2021-09 | SP#93E | SP-210932 | 3088 | 1 | B | 5GS Connection release support for 5GC/NR | 17.2.0 |
| 2021-09 | SP#93E | SP-210917 | 3091 | - | D | Update clause number for MB-UPF, MBSF and MBSTF in clause 6.2 | 17.2.0 |
| 2021-09 | SP#93E | SP-210923 | 3095 | - | B | Reference point AUSF - NSSAAF | 17.2.0 |
| 2021-09 | SP#93E | SP-210923 | 3097 | 1 | B | Format of SUCI/SUPI used for Onboarding | 17.2.0 |
| 2021-09 | SP#93E | SP-210923 | 3098 | - | C | SNPN support for emergency | 17.2.0 |
| 2021-09 | SP#93E | SP-210922 | 3101 | 1 | F | Resolve Editor's Note on analytics metadata provisioning capability | 17.2.0 |
| 2021-09 | SP#93E | SP-210937 | 3108 | - | F | Update BSF NF profile to support SUPI and GPSI | 17.2.0 |
| 2021-09 | SP#93E | SP-210918 | 3111 | 1 | F | Termination on UE assistance mode | 17.2.0 |
| 2021-09 | SP#93E | SP-210929 | 3112 | - | F | Classification of NEF or TSCTSF | 17.2.0 |
| 2021-09 | SP#93E | SP-210918 | 3114 | - | F | Removal of 5G-RG limitation on 3GPP access leg support in EPC | 17.2.0 |
| 2021-09 | SP#93E | SP-210918 | 3116 | 1 | F | Clarification on source and destination addresses setting for PMF messages | 17.2.0 |
| 2021-09 | SP#93E | SP-210916 | 3119 | 1 | F | Remove Editor's note in clause 5.4.11.1 in TS 23.501 | 17.2.0 |
| 2021-09 | SP#93E | SP-210920 | 3124 | 1 | F | Update of ECS address in External Exposure of Network Capability | 17.2.0 |
| 2021-09 | SP#93E | SP-211133 | 3126 | 3 | B | Resolve ENs in NSAC support for EPC interworking | 17.2.0 |
| 2021-09 | SP#93E | SP-210923 | 3136 | - | F | Terminology correction for UE onboarding | 17.2.0 |
| 2021-09 | SP#93E | SP-210923 | 3137 | 1 | F | AMF relocation for UE registered for onboarding | 17.2.0 |
| 2021-09 | SP#93E | SP-210923 | 3139 | - | F | selection of AUSF supporting primary authentication towards AAA server | 17.2.0 |
| 2021-09 | SP#93E | SP-210929 | 3142 | - | F | Clarify distribution of Announce message | 17.2.0 |
| 2021-09 | SP#93E | SP-210929 | 3143 | - | F | Clarify interworking with EPS is not supported for TSC or time synchronization | 17.2.0 |
| 2021-09 | SP#93E | SP-210929 | 3144 | 1 | F | Granularity of TSCTSF | 17.2.0 |
| 2021-09 | SP#93E | SP-210923 | 3146 | 1 | F | Correction on remote provisioning of credentials for NSSAA or secondary authentication/authorization | 17.2.0 |
| 2021-09 | SP#93E | SP-210920 | 3149 | 1 | F | Updates on edge computing | 17.2.0 |
| 2021-09 | SP#93E | SP-210929 | 3150 | 1 | F | Updates on PTP instance type | 17.2.0 |
| 2021-09 | SP#93E | SP-210933 | 3155 | 1 | B | Support RedCap UEs differentiation in 5GC | 17.2.0 |
| 2021-09 | SP#93E | SP-210911 | 3157 | 1 | A | Clarification on the Bridge delay calculating | 17.2.0 |
| 2021-09 | SP#93E | SP-210929 | 3160 | 1 | F | KI#3, clarification on the TSCTSF functionality and configuration for transport protocols | 17.2.0 |
| 2021-09 | SP#93E | SP-210929 | 3161 | 1 | B | KI#3, clarification on the exposure of time sync service | 17.2.0 |
| 2021-09 | SP#93E | SP-210929 | 3162 | 1 | F | Clean up on the BMIC and bridge Management Information Container | 17.2.0 |
| 2021-09 | SP#93E | SP-210923 | 3165 | - | F | Clarification of the AMF Onboarding Configuration Data | 17.2.0 |
| 2021-09 | SP#93E | SP-210904 | 3169 |  | A | 5GS Idle Status Indication | 17.2.0 |
| 2021-09 | SP#93E | SP-210915 | 3170 | 1 | B | AUSF/UDM discovery based SUCI information | 17.2.0 |
| 2021-09 | SP#93E | SP-210923 | 3173 | 1 | F | Clarification on NF profile in case of SNPN | 17.2.0 |
| 2021-09 | SP#93E | SP-210923 | 3175 | 1 | F | Clarification on functionality of NF in SNPN | 17.2.0 |
| 2021-09 | SP#93E | SP-210912 | 3178 | - | A | Emergency services for non-3GPP access | 17.2.0 |
| 2021-09 | SP#93E | SP-210918 | 3179 | 1 | F | Clarification on threshold values | 17.2.0 |
| 2021-09 | SP#93E | SP-210920 | 3186 | - | B | Use UPF to transfer DNS message between EASDF and DNS server | 17.2.0 |
| 2021-09 | SP#93E | SP-210920 | 3187 | - | F | Add Nudm_ServiceSpecificAuthorisation service | 17.2.0 |
| 2021-09 | SP#93E | SP-210929 | 3189 | 1 | F | Update for (g)PTP messages forwarding in UPF/NW-TT | 17.2.0 |
| 2021-09 | SP#93E | SP-210908 | 3190 | 2 | A | No empty allowed NSSAI at REGISTRATION ACCEPT | 17.2.0 |
| 2021-09 | SP#93E | SP-210932 | 3192 | 1 | F | MUSIM Terminology Alignment | 17.2.0 |
| 2021-09 | SP#93E | SP-210932 | 3196 | - | F | Terminology correction | 17.2.0 |
| 2021-09 | SP#93E | SP-210929 | 3198 | 1 | C | Correcting the residence time calculation for the delay measurements | 17.2.0 |
| 2021-09 | SP#93E | SP-210916 | 3199 | 1 | F | SMF subscribes Satellite backhaul category backhaul change from AMF | 17.2.0 |
| 2021-09 | SP#93E | SP-210925 | 3201 | 1 | B | Completion of NSAC per access type | 17.2.0 |
| 2021-09 | SP#93E | SP-210911 | 3204 | 2 | A | Mapping scheduled traffic information, PSFP information and propagation delays between TSN GM clock and 5GS clock | 17.2.0 |
| 2021-09 | SP#93E | SP-210903 | 3208 | - | A | Correction of N26 message relaying between S1 and N26 messages | 17.2.0 |
| 2021-09 | SP#93E | SP-210933 | 3209 | 1 | C | Extended DRX for NR (RedCap) | 17.2.0 |
| 2021-09 | SP#93E | SP-210915 | 3213 | 1 | F | Update Reference architecture with UPF SBI | 17.2.0 |
| 2021-09 | SP#93E | SP-210925 | 3220 | 1 | F | NSAC procedure in EPS when APN maps to more than one S-NSSAI. | 17.2.0 |
| 2021-09 | SP#93E | SP-210915 | 3222 | - | F | Indicate the number of supported packet filters for signalled QoS rules only if the UE supports more than 16 packet filters for the PDU session | 17.2.0 |
| 2021-09 | SP#93E | SP-210932 | 3228 | - | F | Clarification related to access type | 17.2.0 |
| 2021-09 | SP#93E | SP-210915 | 3230 | 1 | F | Overlapping LADN Service area | 17.2.0 |
| 2021-09 | SP#93E | SP-210911 | 3231 | - | A | Clarification on support of CAG in SNPN | 17.2.0 |
| 2021-09 | SP#93E | SP-210925 | 3232 | - | F | clarification on S-NSSAI mapping | 17.2.0 |
| 2021-12 | SP#94E | SP-211289 | 2385 | 8 | C | Support of the mapping from IP addressing information provided to an AF to the user identity | 17.3.0 |
| 2021-12 | SP#94E | SP-211284 | 3030 | 4 | F | UE location verification handling | 17.3.0 |
| 2021-12 | SP#94E | SP-211286 | 3055 | 3 | F | MBS Packet detection and forwarding | 17.3.0 |
| 2021-12 | SP#94E | SP-211286 | 3092 | 3 | F | Add NF services for 5G MBS | 17.3.0 |
| 2021-12 | SP#94E | SP-211302 | 3094 | 2 | F | MUSIM support for SNPN access mode | 17.3.0 |
| 2021-12 | SP#94E | SP-211299 | 3107 | 4 | F | QoS parameter handling for TSC | 17.3.0 |
| 2021-12 | SP#94E | SP-211288 | 3110 | 2 | F | PMF information transported via N4 | 17.3.0 |
| 2021-12 | SP#94E | SP-211304 | 3172 | 5 | C | NSSAAF Discovery and Selection based on S-NSSAI or UE ID Range | 17.3.0 |
| 2021-12 | SP#94E | SP-211295 | 3205 | 2 | F | Update to NSSRG procedure | 17.3.0 |
| 2021-12 | SP#94E | SP-211302 | 3229 | 2 | F | Deleting PRs in non allowed area | 17.3.0 |
| 2021-12 | SP#94E | SP-211302 | 3235 | 4 | F | Enabling of paging reception for 5GS | 17.3.0 |
| 2021-12 | SP#94E | SP-211550 | 3237 | 3 | F | MUSIM capabilities in Emergency Registration | 17.3.0 |
| 2021-12 | SP#94E | SP-211295 | 3240 | 2 | F | Network Slicing scope in relation to SNPNs | 17.3.0 |
| 2021-12 | SP#94E | SP-211294 | 3241 | 1 | F | Network slice admission control for SNPN onboarding | 17.3.0 |
| 2021-12 | SP#94E | SP-211299 | 3242 | 3 | F | Improved PTP instance configuration management | 17.3.0 |
| 2021-12 | SP#94E | SP-211299 | 3243 | - | F | Correction of the TSCTSF functionality description | 17.3.0 |
| 2021-12 | SP#94E | SP-211299 | 3244 | 1 | F | Revisions related Time Synchronization | 17.3.0 |
| 2021-12 | SP#94E | SP-211299 | 3245 | 1 | F | Clarifications on TSN AF and TSCTSF parameter handling | 17.3.0 |
| 2021-12 | SP#94E | SP-211304 | 3246 | - | C | Update of clause 6.3.1.0 related to binding | 17.3.0 |
| 2021-12 | SP#94E | SP-211288 | 3247 | 1 | F | Access performance measurements applicability to QoS Flows | 17.3.0 |
| 2021-12 | SP#94E | SP-211288 | 3248 | 1 | F | Corrections to UE assistance operation | 17.3.0 |
| 2021-12 | SP#94E | SP-211288 | 3250 | 1 | F | Clarification on threshold condition | 17.3.0 |
| 2021-12 | SP#94E | SP-211301 | 3251 | 1 | B | Authentication and Subscription information checking for Disaster Roaming service | 17.3.0 |
| 2021-12 | SP#94E | SP-211301 | 3252 | - | F | Clarification for Disaster Roaming service | 17.3.0 |
| 2021-12 | SP#94E | SP-211304 | 3253 | 1 | F | Reserving some reference point numbers | 17.3.0 |
| 2021-12 | SP#94E | SP-211294 | 3254 | 1 | F | Clarification on Remote provisioning of credentials - User Plane | 17.3.0 |
| 2021-12 | SP#94E | SP-211294 | 3255 | 1 | F | UE Configuration Data for UP Remote Provisioning provided by ONN | 17.3.0 |
| 2021-12 | SP#94E | SP-211627 | 3256 | 6 | F | UE onboarding architecture | 17.3.0 |
| 2021-12 | SP#94E | SP-211294 | 3257 | 3 | D | Rapporteur's editorial cleanup for eNPN | 17.3.0 |
| 2021-12 | SP#94E | SP-211299 | 3260 | 1 | F | Link delay measurement for the end-to-end Transparent Clock | 17.3.0 |
| 2021-12 | SP#94E | SP-211295 | 3261 | 2 | F | NSAC clarification | 17.3.0 |
| 2021-12 | SP#94E | SP-211301 | 3264 | 3 | F | MINT Updates | 17.3.0 |
| 2021-12 | SP#94E | SP-211287 | 3265 | - | C | NR RedCap Indication during IRAT handover procedure | 17.3.0 |
| 2021-12 | SP#94E | SP-211304 | 3267 | - | F | GBA Reference points | 17.3.0 |
| 2021-12 | SP#94E | SP-211295 | 3268 | 1 | D | Editorial Changes on eNS_Ph2 | 17.3.0 |
| 2021-12 | SP#94E | SP-211295 | 3269 | 2 | F | Clarification on Access Type for NSAC | 17.3.0 |
| 2021-12 | SP#94E | SP-211294 | 3274 | 3 | F | eNPN corrections to clarify use of DNN and S-NSSAI for onboarding, AUSF discovery | 17.3.0 |
| 2021-12 | SP#94E | SP-211299 | 3275 | 1 | F | Time synchronization - description review | 17.3.0 |
| 2021-12 | SP#94E | SP-211299 | 3276 | 1 | D | Rapporteur CR for editorial fixes | 17.3.0 |
| 2021-12 | SP#94E | SP-211294 | 3277 | 1 | F | Correction on remote provisioning of credentials for NSSAA or secondary authentication/authorization | 17.3.0 |
| 2021-12 | SP#94E | SP-211298 | 3280 | - | F | UAS NF selection based on the NEF capability | 17.3.0 |
| 2021-12 | SP#94E | SP-211294 | 3281 | 1 | F | KI#4- Restricted Onboarding PDU session when PLMN is ON | 17.3.0 |
| 2021-12 | SP#94E | SP-211284 | 3284 | 3 | F | Editorial correction in TS 23.501 | 17.3.0 |
| 2021-12 | SP#94E | SP-211299 | 3285 | 1 | F | Clarify the interaction between AF and TSCTSF | 17.3.0 |
| 2021-12 | SP#94E | SP-211301 | 3287 | 1 | F | Clarification on MINT | 17.3.0 |
| 2021-12 | SP#94E | SP-211284 | 3290 | 1 | D | Clarification on RTD and Terminology Alignment | 17.3.0 |
| 2021-12 | SP#94E | SP-211290 | 3293 | - | F | Corrections on DNAI based I-SMF selection and removal | 17.3.0 |
| 2021-12 | SP#94E | SP-211301 | 3294 | 1 | F | Applicability of states of non-3GPPA and clarifications. | 17.3.0 |
| 2021-12 | SP#94E | SP-211295 | 3295 | 1 | F | Update of the Early Admission Control (EAC) mode | 17.3.0 |
| 2021-12 | SP#94E | SP-211295 | 3296 | - | F | Update of the Functional Description Related to NSAC | 17.3.0 |
| 2021-12 | SP#94E | SP-211294 | 3297 | 1 | F | Clarification for UE onboarding and UE access with CH credentials | 17.3.0 |
| 2021-12 | SP#94E | SP-211290 | 3299 | 2 | F | 501 EASDF Service correction | 17.3.0 |
| 2021-12 | SP#94E | SP-211295 | 3300 | 1 | F | The decision of target NSSAI based on NSSRG | 17.3.0 |
| 2021-12 | SP#94E | SP-211624 | 3302 | 2 | A | Correction on PMF protocol stack for non-3GPP access | 17.3.0 |
| 2021-12 | SP#94E | SP-211294 | 3303 | 1 | F | 23.501 clarification on eNPN | 17.3.0 |
| 2021-12 | SP#94E | SP-211301 | 3311 | 1 | F | Deregistration for UE not eligible for disaster roaming service | 17.3.0 |
| 2021-12 | SP#94E | SP-211299 | 3312 | 1 | F | Update for Time Synchronization Information in PMIC and UMIC | 17.3.0 |
| 2021-12 | SP#94E | SP-211299 | 3313 | 2 | F | Corrections on TSCTSF selection and residence time calculation | 17.3.0 |
| 2021-12 | SP#94E | SP-211592 | 3314 | 3 | F | Support for emergency calls in limited service state | 17.3.0 |
| 2021-12 | SP#94E | SP-211287 | 3316 | 2 | B | eDRX enhancement for 10.24s cycle for RedCap | 17.3.0 |
| 2021-12 | SP#94E | SP-211284 | 3318 | 2 | F | Limited service PLMN selection for emergency | 17.3.0 |
| 2021-12 | SP#94E | SP-211628 | 3319 | 6 | B | Support for Paging Early Indication | 17.3.0 |
| 2021-12 | SP#94E | SP-211293 | 3320 | 4 | F | Miscellaneous correction for eNA_Ph2 | 17.3.0 |
| 2021-12 | SP#94E | SP-211299 | 3321 | 1 | F | Multiple TSCTSFs associated with a single UPF | 17.3.0 |
| 2021-12 | SP#94E | SP-211299 | 3322 | 2 | F | Processing (g)PTP messages for domain numbers and while in Disabled state | 17.3.0 |
| 2021-12 | SP#94E | SP-211284 | 3323 | 2 | C | Support multiple TACs for satellite access | 17.3.0 |
| 2021-12 | SP#94E | SP-211287 | 3324 | 2 | B | Capabilities for NR RedCap UE | 17.3.0 |
| 2021-12 | SP#94E | SP-211303 | 3327 | - | F | EPS User Plane Integrity Protection corrections for Service Request and mixed eNB UPIP support; etc in TS 23.501. | 17.3.0 |
| 2021-12 | SP#94E | SP-211294 | 3328 | 1 | F | Clarification on the UE remote provisioning. | 17.3.0 |
| 2021-12 | SP#94E | SP-211299 | 3330 | 1 | F | Clarification on the time synchronization | 17.3.0 |
| 2021-12 | SP#94E | SP-211416 | 3331 | 2 | F | clarification on definition of NSSRG | 17.3.0 |
| 2021-12 | SP#94E | SP-211302 | 3334 | 1 | F | On Paging restrictions handling | 17.3.0 |
| 2021-12 | SP#94E | SP-211536 | 3335 | 3 | F | On Connection Release and Paging Restriction during a Mobility Registration Update in a TA outside the current Registration Area | 17.3.0 |
| 2021-12 | SP#94E | SP-211288 | 3338 | 1 | F | Change term default QoS Flow to the QoS Flow associated with default QoS rule in TS 23.501 | 17.3.0 |
| 2021-12 | SP#94E | SP-211293 | 3339 | - | F | Update to NEF Discovery and Selection | 17.3.0 |
| 2021-12 | SP#94E | SP-211294 | 3340 | 1 | F | Clarification on roaming description for SNPN | 17.3.0 |
| 2021-12 | SP#94E | SP-211294 | 3342 | 1 | Release: | Clarification on network selection for ON-SNPN | 17.3.0 |
| 2021-12 | SP#94E | SP-211626 | 3345 | 4 | F | Clarifications of NSAC and NSAC for roaming cases | 17.3.0 |
| 2021-12 | SP#94E | SP-211287 | 3346 | - | F | Correction on Paging for extended idle mode DRX in E-UTRA and NR connected to 5GC | 17.3.0 |
| 2021-12 | SP#94E | SP-211287 | 3349 | - | B | Support of Access Restriction for RedCap | 17.3.0 |
| 2021-12 | SP#94E | SP-211299 | 3351 | 1 | D | Rapporteur CR for editorial fixes - Inclusive terminology | 17.3.0 |
| 2021-12 | SP#94E | SP-211299 | 3352 | 1 | F | Addressing Rel-17 DS-TT backwards incompatibility for time synchronization | 17.3.0 |
| 2021-12 | SP#94E | SP-211299 | 3357 | 1 | F | Deletion of selected enrties in UMIC/PMIC data structures | 17.3.0 |
| 2021-12 | SP#94E | SP-211300 | 3358 | 1 | F | Clarification on Static Filtering Entries | 17.3.0 |
| 2021-12 | SP#94E | SP-211305 | 3362 | - | F | Align BSF NF profile in NRF (23.501) with BSF related information in NRF services (23.502) | 17.3.0 |
| 2021-12 | SP#94E | SP-211284 | 3364 | 1 | F | TA handling for moving cells in satellite access | 17.3.0 |
| 2021-12 | SP#94E | SP-211276 | 3366 | - | A | V-SMF change at inter-PLMN mobility | 17.3.0 |
| 2021-12 | SP#94E | SP-211283 | 3367 | - | F | NG-RAN location report clarification in RRC Inactive | 17.3.0 |
| 2021-12 | SP#94E | SP-211294 | 3373 | 1 | F | Corrections for CH using AUSF/UDM | 17.3.0 |
| 2021-12 | SP#94E | SP-211294 | 3374 | 1 | F | Correction to AMF Onboarding Configuration Data | 17.3.0 |
| 2021-12 | SP#94E | SP-211299 | 3375 | 2 | F | 23.501: TSCTSF Discovery and Selection | 17.3.0 |
| 2021-12 | SP#94E | SP-211284 | 3376 | - | F | Clarification on IAB support for NR satellite access | 17.3.0 |
| 2021-12 | SP#94E | SP-211282 | 3378 | 1 | F | Fix reference for Naf_ProSe | 17.3.0 |
| 2021-12 | SP#94E | SP-211284 | 3379 | - | B | Indicating a last visited TAI in a Registration for NR Satellite Access | 17.3.0 |
| 2021-12 | SP#94E | SP-211304 | 3382 | 1 | F | Supplementation of L2TP tunnel applicable scenario | 17.3.0 |
| 2021-12 | SP#94E | SP-211299 | 3386 | 1 | F | Update the correction field for the end-to-end Transparent Clock | 17.3.0 |
| 2021-12 | SP#94E | SP-211301 | 3389 | 1 | F | Handling of DC is no longer applicable | 17.3.0 |
| 2021-12 | SP#94E | SP-211278 | 3393 | 1 | A | correction for CAG restrictions with emergency services | 17.3.0 |
| 2021-12 | SP#94E | SP-211294 | 3394 | 1 | F | clarification for QoS differentiation for User Plane IPsec Child SA in underlay network | 17.3.0 |
| 2021-12 | SP#94E | SP-211295 | 3400 | - | F | Removal of Editor's Note on Configured NSSAI | 17.3.0 |
| 2021-12 | SP#94E | SP-211295 | 3401 | 1 | F | Clarification on Multiple NSACFs for S-NSSAI | 17.3.0 |
| 2021-12 | SP#94E | SP-211299 | 3405 | 1 | F | Relationship between Sync Exposure and Time Distribution | 17.3.0 |
| 2021-12 | SP#94E | SP-211299 | 3406 | 1 | F | Correction on 5G access stratum time distribution | 17.3.0 |
| 2021-12 | SP#94E | SP-211301 | 3407 | 1 | F | Alignment on system information extensions for minimization of service interruption | 17.3.0 |
| 2021-12 | SP#94E | SP-211301 | 3408 | 1 | F | Emergency Services for Disaster Inbound Roamers | 17.3.0 |
| 2021-12 | SP#94E | SP-211295 | 3410 | - | F | Corrections on Nnsacf_SliceStatus and Nnef_SliceStatus services | 17.3.0 |
| 2021-12 | SP#94E | SP-211284 | 3415 | 1 | C | Mobility Registration Update trigger clarification | 17.3.0 |
| 2021-12 | SP#94E | SP-211298 | 3416 | 1 | F | Correction on UAS NF discovery and update UAS related AF and NEF service | 17.3.0 |
| 2021-12 | SP#94E | SP-211290 | 3418 | 1 | F | I-SMF removal triggered by removal of target DNAI | 17.3.0 |
| 2021-12 | SP#94E | SP-211288 | 3421 | 1 | F | Clarification on threshold values | 17.3.0 |
| 2021-12 | SP#94E | SP-211305 | 3422 | 1 | F | Clarification on support of slicing in TWIF scenario | 17.3.0 |
| 2021-12 | SP#94E | SP-211295 | 3428 | - | F | Correction for External Exposure of Network Capability | 17.3.0 |
| 2021-12 | SP#94E | SP-211302 | 3430 | 1 | F | Adding Paging Cause Indication for Voice Service Supported in the RRC Inactive AI | 17.3.0 |
| 2021-12 | SP#94E | SP-211294 | 3431 | 1 | F | Correction for switching 3GPP access between SNPN and PLMN | 17.3.0 |
| 2021-12 | SP#94E | SP-211299 | 3438 | 1 | F | Multiple PTP instances supported in 5GS | 17.3.0 |
| 2021-12 | SP#94E | SP-211300 | 3439 | - | F | Update on configuration for Sync and Announce reception timeouts | 17.3.0 |
| 2021-12 | SP#94E | SP-211305 | 3440 | 1 | F | Removal of a now obsolete sentence about non-3GPP Access being forbidden in a PLMN | 17.3.0 |
| 2021-12 | SP#94E | SP-211279 | 3442 | 1 | A | Layer below IPsec to enable NAT traversal for TNGF/N3IWF access | 17.3.0 |
| 2021-12 | SP#94E | SP-211278 | 3443 | - | A | Adding AdminCycleTimeExtension and PSFPAdminCycleTimeExtension to PMIC | 17.3.0 |
| 2021-12 | SP#94E | SP-211278 | 3447 | 1 | A | Bridge delay calculation and TSCAI calculation if UE-DS-TT residence time has not been provided | 17.3.0 |
| 2021-12 | SP#94E | SP-211302 | 3449 | 1 | F | Clarification on paging restrictions | 17.3.0 |
| 2021-12 | SP#94E | SP-211287 | 3454 | - | F | RAT type determination on AMF for NR Redcap | 17.3.0 |
| 2021-12 | SP#94E | SP-211305 | 3455 | 1 | F | Support of GERAN/UTRAN access: Annex L alignment to CR 2970r1 to TS 23.501 | 17.3.0 |
| 2021-12 | SP#94E | SP-211279 | 3462 | 1 | F | Clarifications on SEPP | 17.3.0 |
| 2022-03 | SP#95E | SP-220047 | 3414 | 2 | F | Mapping TSCAI between TSN GM clock and 5GS clock | 17.4.0 |
| 2022-03 | SP#95E | SP-220055 | 3464 | 1 | F | Aligning 23.501 and 23.548 wording about the DN accessed via a L-UPF | 17.4.0 |
| 2022-03 | SP#95E | SP-220065 | 3465 | 1 | F | Adding NSWO NF in the architecture | 17.4.0 |
| 2022-03 | SP#95E | SP-220057 | 3466 | 1 | F | Remove the CP based remote provisioning | 17.4.0 |
| 2022-03 | SP#95E | SP-220064 | 3467 | 1 | F | Correct the MUSIM Connection Release feature | 17.4.0 |
| 2022-03 | SP#95E | SP-220064 | 3468 | 1 | F | Correction on MUSIM Paging Cause feature | 17.4.0 |
| 2022-03 | SP#95E | SP-220064 | 3469 | 1 | F | Correct PEI used for MUSIM and network subscriptions | 17.4.0 |
| 2022-03 | SP#95E | SP-220057 | 3470 | 1 | F | DN-AAA server selection when the DCS is not involved during primary authentication | 17.4.0 |
| 2022-03 | SP#95E | SP-220056 | 3471 | - | F | Cleanup for NWDAF, DCCF, MFAF and ADRF services | 17.4.0 |
| 2022-03 | SP#95E | SP-220055 | 3472 | 1 | F | Clarify FQDN in Traffic Influence | 17.4.0 |
| 2022-03 | SP#95E | SP-220066 | 3473 | 1 | F | 5G-EIR clarification | 17.4.0 |
| 2022-03 | SP#95E | SP-220062 | 3474 | 1 | F | Clarification on Authentication and Subscription information checking | 17.4.0 |
| 2022-03 | SP#95E | SP-220062 | 3479 | - | F | Delete the EN on disaster roaming revoking | 17.4.0 |
| 2022-03 | SP#95E | SP-220060 | 3480 | 1 | F | Correction on 5G access stratum time distribution | 17.4.0 |
| 2022-03 | SP#95E | SP-220068 | 3481 | 1 | F | Correction on the MME handling for UPIP during interworking | 17.4.0 |
| 2022-03 | SP#95E | SP-220047 | 3487 | 1 | A | Scheduled Traffic not used for TSCAI | 17.4.0 |
| 2022-03 | SP#95E | SP-220282 | 3489 | 2 | F | Clarifications on NSAC for Emergency and Priority Services | 17.4.0 |
| 2022-03 | SP#95E | SP-220066 | 3491 | - | F | Number of CN paging subgroups | 17.4.0 |
| 2022-03 | SP#95E | SP-220066 | 3492 | - | F | Reference Architecture Editorial Correction | 17.4.0 |
| 2022-03 | SP#95E | SP-220066 | 3495 | 1 | F | Correction for Restriction of use of Enhanced Coverage | 17.4.0 |
| 2022-03 | SP#95E | SP-220051 | 3498 | 1 | F | NR NTN: Correction to TA Handling | 17.4.0 |
| 2022-03 | SP#95E | SP-220053 | 3501 | 1 | F | MA PDU sessions with connectivity over E-UTRAN/EPC and non-3GPP access to 5GC | 17.4.0 |
| 2022-03 | SP#95E | SP-220042 | 3505 | 1 | A | SSC mode support by the UEs | 17.4.0 |
| 2022-03 | SP#95E | SP-220066 | 3507 | 1 | F | Handling of VPLMN QoS constraints during mobility | 17.4.0 |
| 2022-03 | SP#95E | SP-220058 | 3508 | 1 | F | Clarification on the Registration area when Target NSSAI is indicated | 17.4.0 |
| 2022-03 | SP#95E | SP-220057 | 3510 | 1 | F | Correction for remote provisioning | 17.4.0 |
| 2022-03 | SP#95E | SP-220057 | 3511 | 1 | F | CH architecture update | 17.4.0 |
| 2022-03 | SP#95E | SP-220057 | 3512 | 1 | F | Correction for UE onboarding | 17.4.0 |
| 2022-03 | SP#95E | SP-220057 | 3514 | 1 | F | Correction in AAA selection procedure | 17.4.0 |
| 2022-03 | SP#95E | SP-220057 | 3515 | - | F | Support for emergency calls when no PLMN acceptable cell is available | 17.4.0 |
| 2022-03 | SP#95E | SP-220056 | 3517 | 1 | F | Clarifications for NWDAF profile and NWDAF discovery | 17.4.0 |
| 2022-03 | SP#95E | SP-220067 | 3518 | - | F | Clarification on non-3gpp AN selection | 17.4.0 |
| 2022-03 | SP#95E | SP-220047 | 3522 | 1 | F | Clarification for Routing Indicator on SNPN-enabled UE | 17.4.0 |
| 2022-03 | SP#95E | SP-220060 | 3523 | 1 | F | Multiple NW-TTs associated with a single UPF | 17.4.0 |
| 2022-03 | SP#95E | SP-220060 | 3524 | 1 | F | Clarifications and clean-ups for TSC | 17.4.0 |
| 2022-03 | SP#95E | SP-220057 | 3525 | 1 | F | Clarifications for SNPN onboarding service | 17.4.0 |
| 2022-03 | SP#95E | SP-220057 | 3526 | 1 | F | Corrections for UE access with CH credentials | 17.4.0 |
| 2022-03 | SP#95E | SP-220057 | 3527 | 1 | D | terms alignments and clean-ups for eNPN | 17.4.0 |
| 2022-03 | SP#95E | SP-220062 | 3530 | 1 | F | Disaster roaming disable handling | 17.4.0 |
| 2022-03 | SP#95E | SP-220060 | 3534 | 1 | F | Time Synchronization of the 5GS as IEEE 1588 Boundary Clock | 17.4.0 |
| 2022-03 | SP#95E | SP-220060 | 3535 | 1 | F | Correction for the end-to-end Transparent Clock | 17.4.0 |
| 2022-03 | SP#95E | SP-220059 | 3537 | 1 | F | Correction on UAS NF discovery | 17.4.0 |
| 2022-03 | SP#95E | SP-220045 | 3538 | 1 | A | Corrections to combined N3IWF/ePDG Selection | 17.4.0 |
| 2022-03 | SP#95E | SP-220058 | 3540 | 1 | F | Registration with AMF re-allocation in connected state | 17.4.0 |
| 2022-03 | SP#95E | SP-220062 | 3543 | - | F | Disaster roaming registration type | 17.4.0 |
| 2022-03 | SP#95E | SP-220055 | 3548 | 1 | F | Add missing EASDF descriptions | 17.4.0 |
| 2022-03 | SP#95E | SP-220051 | 3549 | 1 | F | TAIs reporting corresponding to the Selected PLMN | 17.4.0 |
| 2022-03 | SP#95E | SP-220056 | 3552 | 1 | F | Removal of Nnssf_NSRestriction service | 17.4.0 |
| 2022-03 | SP#95E | SP-220281 | 3553 | 2 | F | Correction of Subscription-related Priority Mechanism | 17.4.0 |
| 2022-03 | SP#95E | SP-220066 | 3554 | 1 | F | Inter-system configuration transfer | 17.4.0 |
| 2022-03 | SP#95E | SP-220051 | 3555 | 1 | F | Correction of Mobility Restrictions handling for emergency calls | 17.4.0 |
| 2022-03 | SP#95E | SP-220067 | 3556 | 1 | F | Clarification on TAI configured for Non 3GPP access | 17.4.0 |
| 2022-03 | SP#95E | SP-220048 | 3558 | 1 | A | LLDP neighbour discovery information fixes | 17.4.0 |
| 2022-03 | SP#95E | SP-220057 | 3559 | 1 | F | Clarification of ProSe support in SNPN | 17.4.0 |
| 2022-03 | SP#95E | SP-220062 | 3563 | 1 | F | Alignment with use of Disaster Roaming Enabled Configuration | 17.4.0 |
| 2022-03 | SP#95E | SP-220057 | 3567 | 1 | F | Clean-up the clause on UP onboarding via ON-SNPN | 17.4.0 |
| 2022-03 | SP#95E | SP-220047 | 3568 | 1 | A | Handling of untagged frames in TSN scenarios | 17.4.0 |
| 2022-03 | SP#95E | SP-220047 | 3570 | 1 | A | Add missing SupportedListMax for gate control information in PMIC and UMIC | 17.4.0 |
| 2022-03 | SP#95E | SP-220058 | 3571 | 1 | F | Clarification on support of multiple NSACFs | 17.4.0 |
| 2022-03 | SP#95E | SP-220066 | 3577 | 1 | F | Completing description of NF profile | 17.4.0 |
| 2022-03 | SP#95E | SP-220066 | 3578 | 1 | F | Paging Early Indication: Removal of Editor's notes | 17.4.0 |
| 2022-06 | SP#96 | SP-220412 | 3317 | 7 | B | Enabling slice priority and slice groups for RRM purposes | 17.5.0 |
| 2022-06 | SP#96 | SP-220404 | 3485 | 2 | F | Correcting the 5G AS time distribution procedure | 17.5.0 |
| 2022-06 | SP#96 | SP-220412 | 3539 | 4 | B | Enabling configuration of Network Slice AS Groups | 17.5.0 |
| 2022-06 | SP#96 | SP-220406 | 3580 | 3 | F | Disaster Roaming service indication | 17.5.0 |
| 2022-06 | SP#96 | SP-220400 | 3581 | 1 | F | Role of Credential Holder | 17.5.0 |
| 2022-06 | SP#96 | SP-220401 | 3582 | 1 | F | Removal of NSACF from HPLMN in LBO Model | 17.5.0 |
| 2022-06 | SP#96 | SP-220401 | 3584 | 1 | F | Clarification on determination of Registration Area | 17.5.0 |
| 2022-06 | SP#96 | SP-220400 | 3589 | 1 | F | Network Slicing Support in SNPN | 17.5.0 |
| 2022-06 | SP#96 | SP-220411 | 3591 | 1 | F | Alignment to BBF LS 512 (Frame route, BBF references) | 17.5.0 |
| 2022-06 | SP#96 | SP-220411 | 3593 | 1 | F | Handling of ARP for IMS voice service in home routed roaming | 17.5.0 |
| 2022-06 | SP#96 | SP-220407 | 3596 | - | F | Correction of message name for paging restriction information | 17.5.0 |
| 2022-06 | SP#96 | SP-220406 | 3599 | 1 | F | Session related subscription information | 17.5.0 |
| 2022-06 | SP#96 | SP-220406 | 3600 | 2 | F | Clarification on UE 5GMM Capability | 17.5.0 |
| 2022-06 | SP#96 | SP-220406 | 3601 | - | F | Removing the editor's note related to CT1 | 17.5.0 |
| 2022-06 | SP#96 | SP-220394 | 3604 | 1 | F | Criterion of Verification of UE location for UE registering via 5G Satellite Access | 17.5.0 |
| 2022-06 | SP#96 | SP-220404 | 3605 | 1 | F | Corrections to Survival Time description | 17.5.0 |
| 2022-06 | SP#96 | SP-220404 | 3606 | 1 | F | Corrections to time synchronization description | 17.5.0 |
| 2022-06 | SP#96 | SP-220394 | 3607 | 1 | F | Clarification on AMF obtaining the satellite-related information | 17.5.0 |
| 2022-06 | SP#96 | SP-220400 | 3609 | 1 | F | SMF UP remote provisioning capability | 17.5.0 |
| 2022-06 | SP#96 | SP-220396 | 3612 | 2 | F | AMF selection to support HLcom feaure for RedCap using power saving function | 17.5.0 |
| 2022-06 | SP#96 | SP-220400 | 3613 | - | F | DCS supporting AUSF/UDM and AAA server functionality | 17.5.0 |
| 2022-06 | SP#96 | SP-220408 | 3617 | 4 | F | 23.501: NSWO and N3GPP access support | 17.5.0 |
| 2022-06 | SP#96 | SP-220394 | 3621 | 1 | F | RAN Initiated UE Context Release for UE using NR satellite access | 17.5.0 |
| 2022-06 | SP#96 | SP-220400 | 3623 | 2 | F | Clarification on the FQDN(s) and IP address(es) of PVS for remote provisioning | 17.5.0 |
| 2022-06 | SP#96 | SP-220404 | 3624 | 1 | F | Clarification on how the TSFTSF assign the NW-TT port to PPT instance | 17.5.0 |
| 2022-06 | SP#96 | SP-220404 | 3625 | 2 | F | Clarification on 5G access stratum distribution in mobility | 17.5.0 |
| 2022-06 | SP#96 | SP-220406 | 3626 | - | F | End of disaster condition | 17.5.0 |
| 2022-06 | SP#96 | SP-220406 | 3628 | 1 | C | UE capabilities indication for UPU with Disaster Roaming information | 17.5.0 |
| 2022-06 | SP#96 | SP-220688 | 3633 | 3 | F | RFSP Index authorized by PCF and subscribed RFSP Index | 17.5.0 |
| 2022-06 | SP#96 | SP-220410 | 3635 | 1 | F | NRF discovery and selection | 17.5.0 |
| 2022-06 | SP#96 | SP-220391 | 3642 | 1 | A | clarifications for CAG access control for a UE without mobility restrictions | 17.5.0 |
| 2022-06 | SP#96 | SP-220410 | 3645 | 1 | F | Correction of UE behaviour upon mobility between GERAN/UTRAN and 5GS | 17.5.0 |
| 2022-06 | SP#96 | SP-220391 | 3649 | 1 | A | Correction of the Signalling Based Tracing support | 17.5.0 |
| 2022-06 | SP#96 | SP-220410 | 3650 | 1 | F | UDR storing of non-subscriber related data | 17.5.0 |
| 2022-06 | SP#96 | SP-220401 | 3652 | 1 | F | Clarification on roaming for NSAC procedure | 17.5.0 |
| 2022-06 | SP#96 | SP-220394 | 3653 | 1 | F | Remove country of UE location from clause 5.16.4.1 in TS23.501 | 17.5.0 |
| 2022-06 | SP#96 | SP-220411 | 3654 | 1 | F | Correction of NSSF involvement in Registration procedure when NSSAA is used | 17.5.0 |
| 2022-06 | SP#96 | SP-220410 | 3655 | 1 | F | Correction of UE Configuration Update procedure conditions for Registration Required and NAS Release | 17.5.0 |
| 2022-09 | SP#97E | SP-220783 | 3603 | 4 | F | Defining the time distribution methods | 17.6.0 |
| 2022-09 | SP#97E | SP-220780 | 3616 | 2 | F | Clarification on UE-Slice-MBR | 17.6.0 |
| 2022-09 | SP#97E | SP-220779 | 3629 | 2 | F | DN-AAA server selection during UE onboarding | 17.6.0 |
| 2022-09 | SP#97E | SP-220771 | 3647 | 2 | A | Clarification of UE egress terminology | 17.6.0 |
| 2022-09 | SP#97E | SP-220789 | 3659 | 1 | F | Handling of PDU Sessions for Emergency services | 17.6.0 |
| 2022-09 | SP#97E | SP-220788 | 3660 | 1 | B | Alignment of SBI-based SMS | 17.6.0 |
| 2022-09 | SP#97E | SP-220789 | 3661 | - | F | Correction on Reference Architecture | 17.6.0 |
| 2022-09 | SP#97E | SP-220785 | 3664 | 1 | F | UCU procedure for MINT update | 17.6.0 |
| 2022-09 | SP#97E | SP-220789 | 3665 | 1 | F | ULI provision with PScell information | 17.6.0 |
| 2022-09 | SP#97E | SP-220769 | 3666 | 1 | C | Periodic update time from UE | 17.6.0 |
| 2022-09 | SP#97E | SP-220789 | 3674 | 1 | F | Handover capability detection | 17.6.0 |
| 2022-09 | SP#97E | SP-220789 | 3676 | 1 | F | Closing open issues on RAN slicing | 17.6.0 |
| 2022-09 | SP#97E | SP-220789 | 3677 | 1 | F | Missing UDSF timer service | 17.6.0 |
| 2022-09 | SP#97E | SP-220776 | 3678 | 1 | F | PMF UAD and UAT message handling clarifications | 17.6.0 |
| 2022-09 | SP#97E | SP-220786 | 3683 | 1 | F | Clarifications on Priority Subscription | 17.6.0 |
| 2022-09 | SP#97E | SP-220783 | 3685 | - | F | Clarification on 5G access stratum distribution in mobility and AM policy modification | 17.6.0 |
| 2022-09 | SP#97E | SP-220774 | 3687 | 1 | F | AMF sends forbidden TAI(s) to UE | 17.6.0 |
| 2022-09 | SP#97E | SP-220771 | 3689 | 1 | A | Correction on 5G VN group management | 17.6.0 |
| 2022-09 | SP#97E | SP-220789 | 3697 | 1 | B | Access Network selection for 5G NSWO | 17.6.0 |
| 2022-09 | SP#97E | SP-220787 | 3698 | 1 | F | Clarification related to Inactive state | 17.6.0 |
| 2022-09 | SP#97E | SP-220785 | 3700 | 1 | F | Clarification related to emergency service | 17.6.0 |
| 2022-12 | SP#98E | - | - | - | - | MCC Correction to add missing N1 line to Figure 4.2.10-1 | 17.7.0 |
| 2022-12 | SP#98E | SP-221079 | 3583 | 4 | F | Clarification on Mapped NSSAI | 17.7.0 |
| 2022-12 | SP#98E | SP-221069 | 3634 | 2 | F | Correction to clarify role of PCC in authorization of EAS Discovery procedure with EASDF | 17.7.0 |
| 2022-12 | SP#98E | SP-221080 | 3663 | 2 | F | Correction related to traffic correlation in PCC rule | 17.7.0 |
| 2022-12 | SP#98E | SP-221079 | 3673 | 2 | F | Mapped NSSAI alignment with stage-3 | 17.7.0 |
| 2022-12 | SP#98E | SP-221071 | 3675 | 2 | F | Alignment with SA3 agreement on usage of SUCI when CH is legacy AAA | 17.7.0 |
| 2022-12 | SP#98E | SP-221072 | 3693 | 2 | F | Pending NSSAI and NSSRG | 17.7.0 |
| 2022-12 | SP#98E | SP-221080 | 3704 | 1 | F | ULI with TAI for non-3GPP access | 17.7.0 |
| 2022-12 | SP#98E | SP-221062 | 3709 | - | A | R17 Correction on TNGF functionality | 17.7.0 |
| 2022-12 | SP#98E | SP-221079 | 3711 | 1 | F | Emergency PDU session transfer | 17.7.0 |
| 2022-12 | SP#98E | SP-221079 | 3712 | 1 | F | Monitoring event in 5GS to EPS mobility | 17.7.0 |
| 2022-12 | SP#98E | SP-221071 | 3731 | 1 | F | Clarification when access SNPN using CH with AAA-S | 17.7.0 |
| 2022-12 | SP#98E | SP-221080 | 3742 | 1 | F | Correction of reference for RedCap indication from UE | 17.7.0 |
| 2022-12 | SP#98E | SP-221079 | 3747 | 1 | F | Correction on conditions for using SPI for UE derived QoS rules | 17.7.0 |
| 2022-12 | SP#98E | SP-221066 | 3801 | 2 | F | NSAG Information validation in Equivalent PLMN | 17.7.0 |
| 2022-12 | SP#98E | SP-221094 | 3701 | 4 | B | Secondary DN authentication and authorization in EPS IWK case | 18.0.0 |
| 2022-12 | SP#98E | SP-221090 | 3705 | 1 | B | Support of RRC_INACTIVE with long eDRX | 18.0.0 |
| 2022-12 | SP#98E | SP-221084 | 3707 | 1 | B | N3IWF selection enhancement for support of S-NSSAI needed by UE | 18.0.0 |
| 2022-12 | SP#98E | SP-221085 | 3710 | 1 | C | RFSP index in use at 5GS to EPS mobility | 18.0.0 |
| 2022-12 | SP#98E | SP-221085 | 3713 | 1 | B | RFSP index during interworking | 18.0.0 |
| 2022-12 | SP#98E | SP-221087 | 3714 | 5 | B | Support of Non-3GPP access for SNPN | 18.0.0 |
| 2022-12 | SP#98E | SP-221089 | 3715 | 1 | B | TS 23.501 Enhancing External Exposure of Network Capability | 18.0.0 |
| 2022-12 | SP#98E | SP-221093 | 3723 | 1 | B | Update for UPF registration and event exposure related context concluded in FS_UPEAS | 18.0.0 |
| 2022-12 | SP#98E | SP-221087 | 3730 | - | B | Equivalent SNPN support | 18.0.0 |
| 2022-12 | SP#98E | SP-221094 | 3733 |  | F | De-activation timer for eCall only mode UE in RRC_INACTIVE | 18.0.0 |
| 2022-12 | SP#98E | SP-221092 | 3734 | 5 | B | RAN feedback for burst sending time adjustment | 18.0.0 |
| 2022-12 | SP#98E | SP-221093 | 3737 | 1 | B | Introduction of UPEAS | 18.0.0 |
| 2022-12 | SP#98E | SP-221091 | 3749 | 1 | B | Support of unavailability period | 18.0.0 |
| 2022-12 | SP#98E | SP-221094 | 3752 | 1 | B | Reference point numbers for charging | 18.0.0 |
| 2022-12 | SP#98E | SP-221092 | 3762 | 3 | B | Adding time synchronization service based on subscription | 18.0.0 |
| 2022-12 | SP#98E | SP-221092 | 3767 | 2 | B | Support for coverage area filters for time synchronization service | 18.0.0 |
| 2022-12 | SP#98E | SP-221139 | 3772 | 3 | B | Discovery and Selection of the NWDAF Supporting Federated Learning in 5GC | 18.0.0 |
| 2022-12 | SP#98E | SP-221139 | 3783 | 2 | B | NWDAF discovery principle enhancements for enhanced model sharing | 18.0.0 |
| 2022-12 | SP#98E | SP-221140 | 3785 | 2 | B | Multiple NSACF architecture enhancement | 18.0.0 |
| 2022-12 | SP#98E | SP-221086 | 3788 | 2 | B | KI#4 23.501 AF traffic influence for common EAS, DNAI selection | 18.0.0 |
| 2022-12 | SP#98E | SP-221081 | 3790 | 2 | B | Verification of UE location update in 23.501 | 18.0.0 |
| 2022-12 | SP#98E | SP-221083 | 3793 | 2 | B | Support of Satellite Edge Computing via UPF deployed on satellite | 18.0.0 |
| 2022-12 | SP#98E | SP-221083 | 3794 | 4 | B | Support of local switch via UPF deployed on satellite for GEO backhaul case | 18.0.0 |
| 2022-12 | SP#98E | SP-221096 | 3796 | 2 | B | Enhancements of PCF Services and NEF Services | 18.0.0 |
| 2022-12 | SP#98E | SP-221083 | 3803 | 2 | B | QoS Monitoring for Dynamic Satellite Backhaul | 18.0.0 |
| 2022-12 | SP#98E | SP-221092 | 3811 | 2 | B | Interworking with TSN network deployed in the transport network | 18.0.0 |
| 2022-12 | SP#98E | SP-221141 | 3813 | 3 | B | Introduction of Mobile Base Station Relay | 18.0.0 |
| 2023-03 | SP#99 | SP-230080 | 3594 | 1 | D | RRC state and CM state terminology alignment | 18.1.0 |
| 2023-03 | SP#99 | SP-230077 | 3720 | 2 | B | UPF event exposure service for TSC management | 18.1.0 |
| 2023-03 | SP#99 | SP-230070 | 3745 | 2 | B | MPS when access to 5GC is WLAN | 18.1.0 |
| 2023-03 | SP#99 | SP-230051 | 3755 | 1 | C | Group Message Delivery | 18.1.0 |
| 2023-03 | SP#99 | SP-230247 | 3759 | 7 | B | Support of XR and Media Services | 18.1.0 |
| 2023-03 | SP#99 | SP-230058 | 3761 | 4 | C | Introducing selection of more granular set of UEs | 18.1.0 |
| 2023-03 | SP#99 | SP-230058 | 3789 | 2 | B | Common EAS/DNAI selection by AF | 18.1.0 |
| 2023-03 | SP#99 | SP-230247 | 3792 | 7 | B | PCF support of 5GS Packet Delay Variation monitoring based on QoS monitoring mechanism and exposed to AF | 18.1.0 |
| 2023-03 | SP#99 | SP-230052 | 3807 | 1 | B | Reporting the RAN timing synchronization status change from AMF to TSCTSF | 18.1.0 |
| 2023-03 | SP#99 | SP-230058 | 3820 | 5 | B | Edge Relocation within the same hosting PLMN's EHEs | 18.1.0 |
| 2023-03 | SP#99 | SP-230063 | 3821 | 2 | B | N5CW device access to SNPN services | 18.1.0 |
| 2023-03 | SP#99 | SP-230169 | 3822 | 7 | B | KI#4: Support for Centralized NSACF in a PLMN with multi-service areas | 18.1.0 |
| 2023-03 | SP#99 | SP-230064 | 3823 | 6 | B | KI#4: Support for HPLMN admission mode while Roaming | 18.1.0 |
| 2023-03 | SP#99 | SP-230077 | 3825 | 1 | B | Support of NAT exposure in 23.501 according to the conclusion in UPEAS | 18.1.0 |
| 2023-03 | SP#99 | SP-230058 | 3830 | 1 | B | The support of Home Routed PDU Session supporting Session Breakout in VPLMN (HR-SBO) | 18.1.0 |
| 2023-03 | SP#99 | SP-230080 | 3831 | 1 | F | Impacts of CH architecture in N3IWF selection | 18.1.0 |
| 2023-03 | SP#99 | SP-230051 | 3834 | 1 | B | MBS service for UE using power saving functions | 18.1.0 |
| 2023-03 | SP#99 | SP-230063 | 3835 | 3 | C | Support for NSWO with CH | 18.1.0 |
| 2023-03 | SP#99 | SP-230055 | 3837 | 1 | F | Resolving EN on PCF's awareness of modified RFSP index indicating a change of priority from 5GC to EPC | 18.1.0 |
| 2023-03 | SP#99 | SP-230034 | 3840 | 1 | A | PDU Session Type Selection in the URSP Rule | 18.1.0 |
| 2023-03 | SP#99 | SP-230063 | 3841 | - | B | Clarification of SNPN access mode | 18.1.0 |
| 2023-03 | SP#99 | SP-230063 | 3842 | 3 | B | Introduction to Localized Services | 18.1.0 |
| 2023-03 | SP#99 | SP-230063 | 3992 | 3 | B | Enabling Access to Localized Services | 18.1.0 |
| 2023-03 | SP#99 | SP-230063 | 3843 | 1 | B | Support for leaving network that provides access to localized services | 18.1.0 |
| 2023-03 | SP#99 | SP-230057 | 3844 | 9 | B | Support of integration with IETF Deterministic Networking | 18.1.0 |
| 2023-03 | SP#99 | SP-230044 | 3848 | - | A | Emergency configuration data update | 18.1.0 |
| 2023-03 | SP#99 | SP-230078 | 3850 | - | F | Update for the support of mobile IAB | 18.1.0 |
| 2023-03 | SP#99 | SP-230073 | 3854 | 4 | B | PIN support in 5GC | 18.1.0 |
| 2023-03 | SP#99 | SP-230247 | 3855 | 11 | B | Introduction of support for L4S | 18.1.0 |
| 2023-03 | SP#99 | SP-230048 | 3858 | 1 | B | Introducing 5G ProSe ph2 function for KI#7 (Support of Emergency for UE-to-Network Relaying) | 18.1.0 |
| 2023-03 | SP#99 | SP-230081 | 3859 | 1 | B | IPv6 prefix delegation in 5GS | 18.1.0 |
| 2023-03 | SP#99 | SP-230075 | 3860 | 1 | B | SFC CR 23.501 | 18.1.0 |
| 2023-03 | SP#99 | SP-230247 | 3864 | 5 | B | Policy control enhancements to support multi-modal flows | 18.1.0 |
| 2023-03 | SP#99 | SP-230064 | 3867 | 5 | B | Change of Network Slice instance for PDU sessions | 18.1.0 |
| 2023-03 | SP#99 | SP-230052 | 3870 | 1 | B | Removing ENs for TSN TN integration | 18.1.0 |
| 2023-03 | SP#99 | SP-230052 | 3871 | 1 | F | Clarification on for TSN TN integration | 18.1.0 |
| 2023-03 | SP#99 | SP-230052 | 3872 | - | B | Removing EN on UL scenario of Reactive RAN feedback for burst sending time adjustment | 18.1.0 |
| 2023-03 | SP#99 | SP-230247 | 3875 | 14 | B | Introduction of support for Jitter Measurement and End of Data Burst reporting to the NG-RAN | 18.1.0 |
| 2023-03 | SP#99 | SP-230056 | 3878 | 1 | B | Support for non-3GPP access path switching | 18.1.0 |
| 2023-03 | SP#99 | SP-230081 | 3881 | 2 | B | 5QI for V2X message delivery via MBS | 18.1.0 |
| 2023-03 | SP#99 | SP-230063 | 3883 | 7 | B | UE discover, select and access to a Hosting network for Localized services | 18.1.0 |
| 2023-03 | SP#99 | SP-230081 | 3886 | - | B | 23.501 - Spending Limits for AM and UE Policies in the 5GC | 18.1.0 |
| 2023-03 | SP#99 | SP-230247 | 3887 | 6 | B | Introduction of 5GS Information Exposure | 18.1.0 |
| 2023-03 | SP#99 | SP-230052 | 3892 | 6 | B | Support for network timing synchronization status and reporting KI1 - description | 18.1.0 |
| 2023-03 | SP#99 | SP-230052 | 3895 | 4 | C | The support for Periodicity feedback in Enablers for Time Sensitive Communications and Time Synchronization feature KI6. | 18.1.0 |
| 2023-03 | SP#99 | SP-230247 | 3896 | 12 | B | Update TS23.501 to reflect conclusion of KI#4 for XRM in TR23.700-60 | 18.1.0 |
| 2023-03 | SP#99 | SP-230073 | 3897 | 12 | B | PIN communication configuration | 18.1.0 |
| 2023-03 | SP#99 | SP-230073 | 3898 | 3 | B | PIN policy configuration | 18.1.0 |
| 2023-03 | SP#99 | SP-230054 | 3910 | 5 | B | Assistance to Member Selection Functionality for Application Operation | 18.1.0 |
| 2023-03 | SP#99 | SP-230073 | 3912 | 1 | B | Non-3GPP QoS and delay budget - 23.501 | 18.1.0 |
| 2023-03 | SP#99 | SP-230068 | 3914 | 1 | B | Service area provisioning and LADN aspects for enhanced group management | 18.1.0 |
| 2023-03 | SP#99 | SP-230247 | 3919 | 7 | B | Introduction of KI#6 conclusion: uplink-downlink transmission coordination | 18.1.0 |
| 2023-03 | SP#99 | SP-230247 | 3923 | 10 | B | Network exposure support for XR services | 18.1.0 |
| 2023-03 | SP#99 | SP-230065 | 3924 | 1 | B | Support URSP provisioning in EPS | 18.1.0 |
| 2023-03 | SP#99 | SP-230062 | 3925 | 1 | B | TS 23.501 enhancements for federated learining. | 18.1.0 |
| 2023-03 | SP#99 | SP-230062 | 3926 | 1 | B | TS 23.501 enhancements for model sharing. | 18.1.0 |
| 2023-03 | SP#99 | SP-230063 | 3927 | 6 | B | Clarifications on Onboarding in SNPN supporting localized services | 18.1.0 |
| 2023-03 | SP#99 | SP-230080 | 3928 | 1 | F | TS 23.501: Clarification of handling of the non-3GPP PDU session in Non-allowed service area | 18.1.0 |
| 2023-03 | SP#99 | SP-230062 | 3929 | 4 | B | Considering ML model management capability during ADRF discovery and selection | 18.1.0 |
| 2023-03 | SP#99 | SP-230078 | 3933 | 1 | B | Providing cell ID/TAC of MBSR for services | 18.1.0 |
| 2023-03 | SP#99 | SP-230040 | 3935 | 1 | A | Clarification on NSSRG enforcement when a UE registered to different PLMNs over 3GPP access and non-3GPP access | 18.1.0 |
| 2023-03 | SP#99 | SP-230056 | 3937 | 1 | B | Support non-3GPP access leg of MA-PDU Session with PDN connection in EPC | 18.1.0 |
| 2023-03 | SP#99 | SP-230064 | 3939 | 7 | B | Improved network control of the UE beahviour for a network slice | 18.1.0 |
| 2023-03 | SP#99 | SP-230043 | 3948 | 1 | A | 5G NSWO clarifications and corrections | 18.1.0 |
| 2023-03 | SP#99 | SP-230077 | 3949 | 1 | C | User Plane Function Selection for UPEAS | 18.1.0 |
| 2023-03 | SP#99 | SP-230053 | 3953 | 1 | B | TNGF selection enhancement for support of S-NSSAI needed by UE | 18.1.0 |
| 2023-03 | SP#99 | SP-230387 | 3956 | 13 | B | Transfer of Satellite Coverage Data to a UE and AMF | 18.1.0 |
| 2023-03 | SP#99 | SP-230064 | 3959 | 7 | B | Hierarchical NSAC architecture enhancement | 18.1.0 |
| 2023-03 | SP#99 | SP-230077 | 3962 | 1 | F | Direct Exposure from UPF and UPF selection | 18.1.0 |
| 2023-03 | SP#99 | SP-230068 | 3964 | 1 | B | KI#3, NEF exposure for handling PDU Session Type change and managing temporal invalidity/validity condition for a group of UEs | 18.1.0 |
| 2023-03 | SP#99 | SP-230049 | 3966 | 3 | B | Paging enhancement during satellite discontinuous coverage | 18.1.0 |
| 2023-03 | SP#99 | SP-230054 | 3968 | 4 | B | 5GS Assistance for Application AI/ML operation: General clause | 18.1.0 |
| 2023-03 | SP#99 | SP-230056 | 3973 | 1 | B | Introduction of the MPQUIC Steering Functionality | 18.1.0 |
| 2023-03 | SP#99 | SP-230052 | 3981 | 1 | F | Update for controlling time synchronization service based on Subscription | 18.1.0 |
| 2023-03 | SP#99 | SP-230068 | 3982 | 1 | B | Group MBR | 18.1.0 |
| 2023-03 | SP#99 | SP-230068 | 3984 | 1 | B | UE-to-UE QoS for a group | 18.1.0 |
| 2023-03 | SP#99 | SP-230050 | 3985 | - | B | Add description for PSA UPF selection | 18.1.0 |
| 2023-03 | SP#99 | SP-230068 | 3986 | 1 | B | Allowing UE to simultaneously send data to different groups with different QoS policy | 18.1.0 |
| 2023-03 | SP#99 | SP-230058 | 3987 | 5 | B | KI#4 AF traffic influence for common EAS, DNAI selection | 18.1.0 |
| 2023-03 | SP#99 | SP-230055 | 3991 | 1 | B | Clarification of AMF behaviour when it receives RFSP Index in Use Validity Time from MME during UE mobility from EPS to 5GS | 18.1.0 |
| 2023-03 | SP#99 | SP-230040 | 3998 | 1 | A | Pending NSSAI and AMF Relocation in Connected mode 23.501. | 18.1.0 |
| 2023-03 | SP#99 | SP-230050 | 3999 | 1 | B | Clarification of N19 forwarding for local switch via PSA UPF on GEO | 18.1.0 |
| 2023-03 | SP#99 | SP-230064 | 4004 | 5 | B | Optimizations for the support of time vality policies for a network slice and graceful network slice PDU sessions release. | 18.1.0 |
| 2023-03 | SP#99 | SP-230068 | 4010 | 1 | B | Add the default QoS parameters for 5G VN group data | 18.1.0 |
| 2023-03 | SP#99 | SP-230038 | 4018 | 1 | A | Correction of supported services in UPF | 18.1.0 |
| 2023-03 | SP#99 | SP-230056 | 4019 | 1 | B | Introducing Redundant Steering Mode | 18.1.0 |
| 2023-03 | SP#99 | SP-230049 | 4020 | 6 | B | Wait range during discontinuous coverage. | 18.1.0 |
| 2023-03 | SP#99 | SP-230073 | 4028 | 5 | B | Informative Annex on PIN Architecture | 18.1.0 |
| 2023-03 | SP#99 | SP-230386 | 4033 | 13 | B | Support of discontinuous coverage | 18.1.0 |
| 2023-03 | SP#99 | SP-230064 | 4035 | 7 | B | Introduction of partially Allowed NSSAI and Partially Rejected S-NSSAI | 18.1.0 |
| 2023-03 | SP#99 | SP-230315 | 4036 | 4 | B | Introduction of Alternative S-NSSAI replacement determined by NSSF | 18.1.0 |
| 2023-03 | SP#99 | SP-230078 | 4039 | 1 | F | Resolving EN on emergency services. | 18.1.0 |
| 2023-03 | SP#99 | SP-230373 | 4040 | 3 | F | Not allowed to act as MBSR handling | 18.1.0 |
| 2023-03 | SP#99 | SP-230058 | 4042 | 3 | B | Edge relocation with common DNAI | 18.1.0 |
| 2023-03 | SP#99 | SP-230247 | 4046 | 12 | B | Support of PDU Set based handling | 18.1.0 |
| 2023-03 | SP#99 | SP-230080 | 4049 |  | F | Corrections of Nudm service operations list | 18.1.0 |
| 2023-03 | SP#99 | SP-230058 | 4054 | - | B | AF obtaining DNAI associated to EAS | 18.1.0 |
| 2023-03 | SP#99 | SP-230080 | 4056 | 1 | F | Generalization of QoS monitoring control description | 18.1.0 |
| 2023-03 | SP#99 | SP-230080 | 4057 | 1 | F | Clarifications for GTP-U Path Monitoring | 18.1.0 |
| 2023-03 | SP#99 | SP-230080 | 4058 | 1 | F | Restructuring of user plane management clause | 18.1.0 |
| 2023-03 | SP#99 | SP-230075 | 4069 | 1 | B | Support for Service Function Chaining in 5GS | 18.1.0 |
| 2023-03 | SP#99 | SP-230062 | 4070 | - | B | Discovery and selection of NWDAF with FL support - Resolve EN | 18.1.0 |
| 2023-03 | SP#99 | SP-230044 | 4076 | 1 | A | Mapped NSSAI when UE is roaming | 18.1.0 |
| 2023-03 | SP#99 | SP-230064 | 4077 | 6 | B | Support of reduced network slice availability | 18.1.0 |
| 2023-03 | SP#99 | SP-230064 | 4078 | 2 | B | Support of graceful/gradual termination of PDU sessions during network slice decommissioning | 18.1.0 |
| 2023-03 | SP#99 | SP-230062 | 4080 | 1 | B | Using network analytics for roaming scenarios | 18.1.0 |
| 2023-03 | SP#99 | SP-230115 | 4081 | 1 | B | CN based MT communication capability indication | 18.1.0 |
| 2023-03 | SP#99 | SP-230064 | 4083 | 10 | B | Support of network slice replacement | 18.1.0 |
| 2023-03 | SP#99 | SP-230068 | 4086 | 1 | B | KI#1: Support the enhancement of group attribute management | 18.1.0 |
| 2023-03 | SP#99 | SP-230068 | 4087 | 1 | B | KI#3: provisioning of traffic characteristics and monitoring of performance characteristics | 18.1.0 |
| 2023-03 | SP#99 | SP-230052 | 4088 | 4 | B | Clarify on periodicity adaption on Proactive feedback | 18.1.0 |
| 2023-03 | SP#99 | SP-230052 | 4089 | 4 | F | Clarification for Controlling time synchronization service based on the Subscription | 18.1.0 |
| 2023-03 | SP#99 | SP-230073 | 4092 | 6 | B | PIN definition and architecture | 18.1.0 |
| 2023-03 | SP#99 | SP-230063 | 4095 | 1 | B | SNPN broadcast system information and manual network selection for localized service | 18.1.0 |
| 2023-03 | SP#99 | SP-230044 | 4101 | 1 | A | UDM determination Internal Group ID values for 5G VN group management | 18.1.0 |
| 2023-03 | SP#99 | SP-230062 | 4105 | 1 | B | Update NEF to support NWDAF-assisted application detection | 18.1.0 |
| 2023-03 | SP#99 | SP-230078 | 4107 | 1 | C | UE mobility when moving together with a MBSR cell | 18.1.0 |
| 2023-03 | SP#99 | SP-230078 | 4108 | 1 | B | Configuration of the MBSR node | 18.1.0 |
| 2023-03 | SP#99 | SP-230063 | 4118 | 3 | B | Support of non-3GPP access to SNPN | 18.1.0 |
| 2023-03 | SP#99 | SP-230063 | 4119 | 3 | B | Support of allowed CAG list with validity condition | 18.1.0 |
| 2023-03 | SP#99 | SP-230063 | 4124 | 3 | B | Support of wireline access as access to SNPN | 18.1.0 |
| 2023-03 | SP#99 | SP-230054 | 4128 | 4 | B | Support of Group AF Sessions for QoS Resource Allocation and QoS monitoring operation | 18.1.0 |
| 2023-03 | SP#99 | SP-230052 | 4133 | 2 | B | Ensuring that a geographical area requested for a time sync service coincides with a RA | 18.1.0 |
| 2023-03 | SP#99 | SP-230040 | 4137 | 1 | A | UE-Slice-MBR clarifications including for priority services | 18.1.0 |
| 2023-03 | SP#99 | SP-230058 | 4144 | - | B | Common EAS re-discovery initiated by SMF | 18.1.0 |
| 2023-03 | SP#99 | SP-230170 | 4156 | 2 | B | Event exposure enhancement for enhanced NSAC architecture | 18.1.0 |
| 2023-03 | SP#99 | SP-230058 | 4160 | 2 | B | Delivery of Traffic Influence information for Home Routed-Session Breakout (HR-SBO) support | 18.1.0 |
| 2023-03 | SP#99 | SP-230052 | 4180 | 1 | C | Corrections for the description of coverage area support for time synchronization service KI2 | 18.1.0 |
| 2023-06 | SP#100 | SP-230490 | 3748 | 2 | F | Support for 5QI Priority Level in QoS constraints | 18.2.0 |
| 2023-06 | SP#100 | SP-230469 | 3764 | 6 | B | Extension of NWDAF registration information to reflect new accuracy checking capability | 18.2.0 |
| 2023-06 | SP#100 | SP-230495 | 3922 | 2 | F | Update for the description of the Nupf interface in 5G reference architecture | 18.2.0 |
| 2023-06 | SP#100 | SP-230490 | 4037 | 2 | F | NWDAF discovery with overlapping Serving Areas | 18.2.0 |
| 2023-06 | SP#100 | SP-230463 | 4155 | 5 | A | Rewording of NOTE on AF Specific UE identifier | 18.2.0 |
| 2023-06 | SP#100 | SP-230497 | 4183 | 3 | B | Support of extra traffic characteristics for alternative QoS profile | 18.2.0 |
| 2023-06 | SP#100 | SP-230491 | 4189 | - | B | Dymically changing AM policies for inbound roamers using LBO | 18.2.0 |
| 2023-06 | SP#100 | SP-230476 | 4190 | - | F | KI#3 -5GS to EPS mobility | 18.2.0 |
| 2023-06 | SP#100 | SP-230457 | 4191 | 1 | F | Translation of Internal-External Information for Assisting Application Layer AI/ML Operations | 18.2.0 |
| 2023-06 | SP#100 | SP-230457 | 4192 | 6 | F | High level feature description for AIMLsys | 18.2.0 |
| 2023-06 | SP#100 | SP-230493 | 4196 | 1 | C | Resolving (Removing) ENs for TSN TN integration | 18.2.0 |
| 2023-06 | SP#100 | SP-230471 | 4202 | 1 | C | Clarify the allowed CAG list with validity condition | 18.2.0 |
| 2023-06 | SP#100 | SP-230471 | 4205 | 1 | C | SNPN selection for access to localized services | 18.2.0 |
| 2023-06 | SP#100 | SP-230459 | 4210 | 1 | C | Updates to non-3GPP access path switching | 18.2.0 |
| 2023-06 | SP#100 | SP-230478 | 4211 | 1 | C | Corrections to handling of LADN area per DNN and S-NSSAI | 18.2.0 |
| 2023-06 | SP#100 | SP-230493 | 4216 | 9 | C | Revision on the support of network timing synchronization status and reporting | 18.2.0 |
| 2023-06 | SP#100 | SP-230483 | 4218 | 1 | C | Co-existence of Small Data Transmission and CN based MT communication handling for UE in RRC_INACTIVE | 18.2.0 |
| 2023-06 | SP#100 | SP-230497 | 4219 | 6 | C | Resolution of EN for L4S | 18.2.0 |
| 2023-06 | SP#100 | SP-230484 | 4224 | 1 | F | PDU session sharing among PINs | 18.2.0 |
| 2023-06 | SP#100 | SP-230496 | 4228 | 6 | C | Additional User Location Information | 18.2.0 |
| 2023-06 | SP#100 | SP-230490 | 4229 | 1 | F | IAB node release handling | 18.2.0 |
| 2023-06 | SP#100 | SP-230483 | 4231 | 1 | F | N2 release handling for RRC_INACTIVE | 18.2.0 |
| 2023-06 | SP#100 | SP-230473 | 4234 | 1 | F | Resolving open issues related to Alternative S-NSSAI | 18.2.0 |
| 2023-06 | SP#100 | SP-230473 | 4235 | - | F | Resolving open issues for temporarily available network slices | 18.2.0 |
| 2023-06 | SP#100 | SP-230473 | 4236 | 1 | C | Resolving open issues for Network Slices with Network Slice Area of Service not matching deployed TAs | 18.2.0 |
| 2023-06 | SP#100 | SP-230471 | 4238 | - | F | Additional requirements for N3IWF selection for onboarding | 18.2.0 |
| 2023-06 | SP#100 | SP-230451 | 4240 | 4 | C | Closing ENs for the procedures for discontinuous coverage reporting | 18.2.0 |
| 2023-06 | SP#100 | SP-230452 | 4246 | 1 | B | Optimization consideration for satellite backhaul QoS monitoring | 18.2.0 |
| 2023-06 | SP#100 | SP-230494 | 4249 | - | B | 5QI for A2X message delivery via MBS | 18.2.0 |
| 2023-06 | SP#100 | SP-230476 | 4253 | 1 | B | Support URSP provisioning in EPS | 18.2.0 |
| 2023-06 | SP#100 | SP-230457 | 4255 | 1 | F | R18 AIMLsys_General_23501 CR_EN on AIML traffic | 18.2.0 |
| 2023-06 | SP#100 | SP-230457 | 4257 | - | F | R18 AIMLsys_KI1_23501 CR_SingleSO_for_QoS | 18.2.0 |
| 2023-06 | SP#100 | SP-230472 | 4259 | 1 | A | Number of PDU session slice availability check during EPC IWK | 18.2.0 |
| 2023-06 | SP#100 | SP-230471 | 4270 | 1 | B | Network access control when the UE accesse an SNPN that provides access for Localized Services | 18.2.0 |
| 2023-06 | SP#100 | SP-230461 | 4271 | 4 | F | Selection of Common DNAI | 18.2.0 |
| 2023-06 | SP#100 | SP-230497 | 4278 | 1 | F | KI#6 text alignment text | 18.2.0 |
| 2023-06 | SP#100 | SP-230460 | 4280 | 1 | F | Architectural diagram change for DetNet | 18.2.0 |
| 2023-06 | SP#100 | SP-230460 | 4281 | 1 | B | UPF discovery and Selection for DetNet | 18.2.0 |
| 2023-06 | SP#100 | SP-230484 | 4284 | 7 | C | Clarifying SMF behaviour for non-3GPP delay budget | 18.2.0 |
| 2023-06 | SP#100 | SP-230484 | 4287 | 6 | B | PIN identifiers | 18.2.0 |
| 2023-06 | SP#100 | SP-230471 | 4288 | 1 | B | Configuration of Credentials Holder for determining SNPN selection information (Annex N.x) | 18.2.0 |
| 2023-06 | SP#100 | SP-230452 | 4293 | 1 | B | Update the descriptions for supporting Edge Computing on satellite | 18.2.0 |
| 2023-06 | SP#100 | SP-230497 | 4294 | 3 | C | QoS Monitoring and 5GS information exposure update | 18.2.0 |
| 2023-06 | SP#100 | SP-230471 | 4300 | 1 | F | N3IWF selection for emergency services for UE not equipped with valid SNPN credentials | 18.2.0 |
| 2023-06 | SP#100 | SP-230451 | 4302 | 1 | B | Provisioning Satellite Coverage Availability to the AMF | 18.2.0 |
| 2023-06 | SP#100 | SP-230478 | 4306 | 1 | B | Support for 5G VN group with multiple SMF(Set)s | 18.2.0 |
| 2023-06 | SP#100 | SP-230478 | 4313 | 1 | B | KI#4 implementation of cross-SMF VN group communication | 18.2.0 |
| 2023-06 | SP#100 | SP-230478 | 4314 | 1 | F | KI#5 correction on the QoS support for UE with multiple groups | 18.2.0 |
| 2023-06 | SP#100 | SP-230469 | 4318 | 1 | B | DCCF Discovery principle enhancements for DCCF relocation in TS 23.501 | 18.2.0 |
| 2023-06 | SP#100 | SP-230497 | 4322 | 9 | B | EN resolving for KI#8 Except TSCAC and clarifications on AF inputs | 18.2.0 |
| 2023-06 | SP#100 | SP-230484 | 4326 | - | F | Solve the EN about handling of the PEMC in 5GC in relation with PIN | 18.2.0 |
| 2023-06 | SP#100 | SP-230484 | 4327 | 1 | F | Solve the EN about PIN deletion, activation and deactivation | 18.2.0 |
| 2023-06 | SP#100 | SP-230459 | 4330 | 1 | F | Clarification on Redundant Steering Mode | 18.2.0 |
| 2023-06 | SP#100 | SP-230459 | 4342 | - | F | Clarification of RTT measurement for RSM | 18.2.0 |
| 2023-06 | SP#100 | SP-230456 | 4351 | 5 | F | Clarification on N3IWF/TNGF selection to support of S-NSSAI needed by UE | 18.2.0 |
| 2023-06 | SP#100 | SP-230473 | 4354 | 3 | C | Explicit subscription to NSSF for network slice instance replacement | 18.2.0 |
| 2023-06 | SP#100 | SP-230496 | 4367 | 1 | B | Open issue resolutions for MBSR support | 18.2.0 |
| 2023-06 | SP#100 | SP-230493 | 4370 | 1 | C | Support of provisioning periodicity set | 18.2.0 |
| 2023-06 | SP#100 | SP-230469 | 4372 |  | C | Updates for registration and discovery for FL entity | 18.2.0 |
| 2023-06 | SP#100 | SP-230461 | 4376 | 3 | B | Update supporting Edge Computing | 18.2.0 |
| 2023-06 | SP#100 | SP-230490 | 4377 | 1 | F | Add FQDN in Traffic Detection Information | 18.2.0 |
| 2023-06 | SP#100 | SP-230495 | 4378 | 1 | B | Considering capability of UPF event exposure during UPF discovery | 18.2.0 |
| 2023-06 | SP#100 | SP-230461 | 4381 | 1 | B | KI#1 V-SMF selection enhancement to support HR-SBO | 18.2.0 |
| 2023-06 | SP#100 | SP-230497 | 4383 | 11 | B | Resolve ENs for support of PDU Set handling | 18.2.0 |
| 2023-06 | SP#100 | SP-230479 | 4390 | 2 | A | Clarification on IAB Authorization | 18.2.0 |
| 2023-06 | SP#100 | SP-230496 | 4391 | 3 | B | Update of MBSR Configuration | 18.2.0 |
| 2023-06 | SP#100 | SP-230495 | 4404 | 1 | B | Updates on TSC management information | 18.2.0 |
| 2023-06 | SP#100 | SP-230457 | 4408 | 4 | B | NEF capability for the new AIML service | 18.2.0 |
| 2023-06 | SP#100 | SP-230478 | 4410 | 1 | B | KI#1: Other Group Attributes | 18.2.0 |
| 2023-06 | SP#100 | SP-230478 | 4411 | 1 | B | KI#1: QoS for a group | 18.2.0 |
| 2023-06 | SP#100 | SP-230478 | 4413 | 1 | B | KI#5: Reference Correction for Group QoS | 18.2.0 |
| 2023-06 | SP#100 | SP-230486 | 4415 | 1 | F | Corrections and alignments of SFC terminology | 18.2.0 |
| 2023-06 | SP#100 | SP-230452 | 4422 | - | F | Clarification of local switch via UPF on GEO satellites | 18.2.0 |
| 2023-06 | SP#100 | SP-230471 | 4424 | - | F | Clarification on the onboarding indication | 18.2.0 |
| 2023-06 | SP#100 | SP-230457 | 4427 | 3 | F | Clarifications on the UE member selection assistance functionality | 18.2.0 |
| 2023-06 | SP#100 | SP-230469 | 4428 | 1 | B | Add NWDAF services and Reference point between two NWDAFs for roaming case | 18.2.0 |
| 2023-06 | SP#100 | SP-230469 | 4430 | - | B | Update of ADRF services | 18.2.0 |
| 2023-06 | SP#100 | SP-230459 | 4431 | 1 | B | Clarifications the Redundant Steering Mode for GBR SDF | 18.2.0 |
| 2023-06 | SP#100 | SP-230473 | 4442 | 1 | B | Hierarchical NSAC Architecture for EPS counting | 18.2.0 |
| 2023-06 | SP#100 | SP-230473 | 4443 | 3 | B | Network control of the slice usage | 18.2.0 |
| 2023-06 | SP#100 | SP-230495 | 4445 | 1 | B | Support of NAT exposure aligned with TS 23.502 | 18.2.0 |
| 2023-06 | SP#100 | SP-230461 | 4447 | - | D | Support fo Edge Computing DNAI mapping update | 18.2.0 |
| 2023-06 | SP#100 | SP-230484 | 4450 | 4 | B | Support QoS management for PIN | 18.2.0 |
| 2023-06 | SP#100 | SP-230459 | 4457 | 1 | B | Determining the ATSSS capabilities of a MA PDU Session when the UE supports MPQUIC | 18.2.0 |
| 2023-06 | SP#100 | SP-230459 | 4459 | 1 | B | Associating a QUIC connection with a QoS flow | 18.2.0 |
| 2023-06 | SP#100 | SP-230470 | 4461 | 1 | A | Correction on maximum number of PVS IP address(es) and/or PVS FQDN(s) allowed to be provided to the UE | 18.2.0 |
| 2023-06 | SP#100 | SP-230476 | 4470 | 1 | B | UE Policy Association handling during EPS to 5GS mobility with N26 | 18.2.0 |
| 2023-06 | SP#100 | SP-230457 | 4473 | 4 | F | 5QI for AIML services | 18.2.0 |
| 2023-06 | SP#100 | SP-230493 | 4475 | 1 | B | Remove the EN on supporting TSN TN | 18.2.0 |
| 2023-06 | SP#100 | SP-230490 | 4476 | 1 | F | Clarification related to LADN PDU session. | 18.2.0 |
| 2023-06 | SP#100 | SP-230452 | 4478 | 1 | B | Remove ENs for QoS monitoring on dynamic satellite backhaul | 18.2.0 |
| 2023-06 | SP#100 | SP-230497 | 4486 | 1 | F | PDU Set Importance spanning across QoS Flows | 18.2.0 |
| 2023-06 | SP#100 | SP-230473 | 4487 | 1 | B | Updates on S-NSSAI Location Availability information | 18.2.0 |
| 2023-06 | SP#100 | SP-230473 | 4488 | 3 | B | Storage of S-NSSAI validity time information | 18.2.0 |
| 2023-06 | SP#100 | SP-230495 | 4490 | 3 | F | Update the description of reporting suggestion information | 18.2.0 |
| 2023-06 | SP#100 | SP-230481 | 4491 | 1 | F | MPS when access to 5GC is WLAN corrections | 18.2.0 |
| 2023-06 | SP#100 | SP-230484 | 4492 | 7 | F | PIN communication definition | 18.2.0 |
| 2023-06 | SP#100 | SP-230497 | 4493 | 3 | B | Introduction of a new standard SST for Extended Reality and Media Services | 18.2.0 |
| 2023-06 | SP#100 | SP-230483 | 4499 | 4 | F | CN based MT communication capability | 18.2.0 |
| 2023-06 | SP#100 | SP-230475 | 4500 | 7 | B | Introduction of the Support of Counting of UEs with at least one PDU sessions in the 5GS option 1 | 18.2.0 |
| 2023-06 | SP#100 | SP-230497 | 4503 | 1 | C | Update for network exposure for XR services | 18.2.0 |
| 2023-06 | SP#100 | SP-230497 | 4506 | 1 | B | Update about the Packet Delay Variation description and add PDV in QoS monitoring parameters | 18.2.0 |
| 2023-06 | SP#100 | SP-230478 | 4510 | 1 | F | Resolving the ENs on the Provisioning and monitoring for a group | 18.2.0 |
| 2023-06 | SP#100 | SP-230478 | 4511 | 1 | F | Clarification on the group-MBR | 18.2.0 |
| 2023-06 | SP#100 | SP-230493 | 4514 | 4 | F | Clarification on the TSCTSF handling when it receives the time sync request from AF and time sync subscription from UDM | 18.2.0 |
| 2023-06 | SP#100 | SP-230497 | 4516 | 1 | C | The update of Policy control enhancements to support multi-modal services | 18.2.0 |
| 2023-06 | SP#100 | SP-230497 | 4527 | 8 | B | Update TS23.501 for PDU Set and PDU Handling | 18.2.0 |
| 2023-06 | SP#100 | SP-230497 | 4529 | 4 | B | PCF provides the Periodicity to SMF via PCC rules for resolving the EN for KI#8 | 18.2.0 |
| 2023-06 | SP#100 | SP-230457 | 4530 | - | B | Service Experience filtering criteria in assistance to UE member selection | 18.2.0 |
| 2023-06 | SP#100 | SP-230484 | 4535 | 1 | F | Editorial change for the PIN | 18.2.0 |
| 2023-06 | SP#100 | SP-230478 | 4541 | 1 | B | Update to Annex O to correct referenced clause number and add an optional condition for setup of the QoS flow | 18.2.0 |
| 2023-06 | SP#100 | SP-230719 | 4553 | 5 | C | Creating an RA when a Slice is Partially Supported in the RA | 18.2.0 |
| 2023-06 | SP#100 | SP-230485 | 4555 | - | B | Support of SL Positioning | 18.2.0 |
| 2023-06 | SP#100 | SP-230457 | 4565 | 1 | F | 23.501 - Member UE terminology update | 18.2.0 |
| 2023-06 | SP#100 | SP-230483 | 4569 | 2 | F | Correction for Asynchronous Type Communication for CN based MT communication handling | 18.2.0 |
| 2023-06 | SP#100 | SP-230476 | 4570 | 2 | B | Handling UE policy association when UE registered over both 3GPP and Non-3GPP access | 18.2.0 |
| 2023-06 | SP#100 | SP-230461 | 4571 | 2 | B | NEF function update | 18.2.0 |
| 2023-06 | SP#100 | SP-230484 | 4572 | 2 | B | PIN traffic routing support | 18.2.0 |
| 2023-06 | SP#100 | SP-230484 | 4573 | 3 | B | PIN general principles | 18.2.0 |
| 2023-06 | SP#100 | SP-230493 | 4580 | - | F | Clarifying the use of TSS information in UMIC | 18.2.0 |
| 2023-06 | SP#100 | SP-230493 | 4581 | 1 | F | Parameters for AF Request Authorization | 18.2.0 |
| 2023-06 | SP#100 | SP-230473 | 4584 | 2 | C | Resolving open issues for Network Slice Area of Service | 18.2.0 |
| 2023-06 | SP#100 | SP-230473 | 4585 | 2 | C | Target NSSAI configuration considering Partial Network Slice support in a Registration Area | 18.2.0 |
| 2023-06 | SP#100 | SP-230473 | 4586 | 2 | C | Number of S-NSSAIs in Partially Allowed NSSAI | 18.2.0 |
| 2023-06 | SP#100 | SP-230497 | 4587 | 2 | F | Clarification on the usage of TSCAI for XRM services | 18.2.0 |
| 2023-06 | SP#100 | SP-230469 | 4589 | 1 | C | Clarification for NWDAF in roaming architecture | 18.2.0 |
| 2023-06 | SP#100 | SP-230469 | 4590 | 2 | C | Clarification of RE-NWDAF discovery | 18.2.0 |
| 2023-06 | SP#100 | SP-230457 | 4591 | 2 | B | NEF capability for the new AIML service | 18.2.0 |
| 2023-06 | SP#100 | SP-230493 | 4592 | 2 | B | Definition of TL Containers | 18.2.0 |
| 2023-06 | SP#100 | SP-230497 | 4604 | 2 | B | QNC Direct Exposure by UPF | 18.2.0 |
| 2023-06 | SP#100 | SP-230498 | 4605 | 2 | B | Exposure of RAN measured data rates | 18.2.0 |
| 2023-06 | SP#100 | SP-230498 | 4611 | 3 | B | PDU Set QoS handling: non-homogenous support (Alternative 2) | 18.2.0 |
| 2023-06 | SP#100 | SP-230484 | 4614 | 1 | C | Resolve ENs on one PIN Served by multiple PDU Sessions | 18.2.0 |
| 2023-06 | SP#100 | SP-230484 | 4621 | 1 | B | Informative annex on PIN traffic routing | 18.2.0 |
| 2023-06 | SP#100 | SP-230457 | 4622 | - | B | Update to UE member selection assistance functionality for application operation | 18.2.0 |
| 2023-06 | SP#100 | SP-230493 | 4636 | 3 | C | Update on Periodicity Range | 18.2.0 |
| 2023-06 | SP#100 | SP-230461 | 4638 | 2 | F | Nnef service update on multiple SMF coordination | 18.2.0 |
| 2023-06 | SP#100 | SP-230473 | 4651 | 1 | B | Support of network slice replacement for handover | 18.2.0 |
| 2023-06 | SP#100 | SP-230451 | 4658 | 2 | B | Completion of Support discontinuous coverage | 18.2.0 |
| 2023-06 | SP#100 | SP-230490 | 4659 | 2 | F | Transfer of emergency PDU session from non-3GPP to 3GPP access | 18.2.0 |
| 2023-06 | SP#100 | SP-230492 | 4666 | 1 | B | 23.501 - Spending Limits for AM and UE Policies in the 5GC | 18.2.0 |
| 2023-06 | SP#100 | SP-230496 | 4669 | 1 | B | Open issue resolutions for MBSR support | 18.2.0 |
| 2023-06 | SP#100 | SP-230496 | 4670 | 3 | B | MBSR registration and authorization support | 18.2.0 |
| 2023-06 | SP#100 | SP-230451 | 4685 | 3 | B | Discontinuous coverage reporting | 18.2.0 |
| 2023-06 | SP#100 | SP-230461 | 4686 | 2 | B | Common EAS/DNAI determination for a set of UEs | 18.2.0 |
| 2023-06 | SP#100 | SP-230461 | 4688 | - | F | SMF determining target AF ID | 18.2.0 |
| 2023-06 | SP#100 | - | - | - | - | MCC correction to table 7.2.8-1 for reference to Nnef_TrafficCorrelation_Notify clause in 23.502 | 18.2.1 |
| 2023-07 | SP#100 | - | 4238 | - | F | MCC correction to add missing bullet and Editor's note in clause 5.30.2.12 | 18.2.2 |
| 2023-09 | SP#101 | SP-230849 | 4582 | 5 | F | NG-RAN resource usage for Alternative S-NSSAI | 18.3.0 |
| 2023-09 | SP#101 | SP-230859 | 4647 | 3 | F | Capability signalling limitation for Reflective QoS | 18.3.0 |
| 2023-09 | SP#101 | SP-230831 | 4695 | 1 | A | Update of subscribed NSSAI when UE is not registered in network | 18.3.0 |
| 2023-09 | SP#101 | SP-230844 | 4696 | 3 | D | Updates to application AI/ML assistance functionality descriptions related to Member UE selection | 18.3.0 |
| 2023-09 | SP#101 | SP-230847 | 4699 | 1 | F | Corrections on NEF(PFDF) support NWDAF-assisted application detection | 18.3.0 |
| 2023-09 | SP#101 | SP-230858 | 4700 | 2 | F | Add support for UPF selection criteria in context of XRM | 18.3.0 |
| 2023-09 | SP#101 | SP-230838 | 4702 | - | A | Replacing obsoleted RFC related to DHCPv6 with RFC 8415 | 18.3.0 |
| 2023-09 | SP#101 | SP-230859 | 4709 | 1 | F | Relaxation of 5QI delay requirements for first packets should also apply for RRC-INACTIVE mode. | 18.3.0 |
| 2023-09 | SP#101 | SP-230849 | 4717 | 4 | F | Resolving open issues related to RAN resoruces handling in KI#1 | 18.3.0 |
| 2023-09 | SP#101 | SP-230850 | 4719 | 3 | F | Clarification of the discovery and seletion of NSACF | 18.3.0 |
| 2023-09 | SP#101 | SP-230836 | 4721 | - | F | Move PMIC and UMIC into Annex | 18.3.0 |
| 2023-09 | SP#101 | SP-230858 | 4723 | 3 | F | PCC support for ECN marking for L4S | 18.3.0 |
| 2023-09 | SP#101 | SP-230856 | 4727 | 2 | F | Clarification on the support for TSCTSF subscribing to AMF notifications for TRS | 18.3.0 |
| 2023-09 | SP#101 | SP-230854 | 4733 | 2 | F | Correction on description about PEGC | 18.3.0 |
| 2023-09 | SP#101 | SP-230849 | 4741 | 2 | F | UP resource deactivation when the UE moves outside the area of slice availability | 18.3.0 |
| 2023-09 | SP#101 | SP-230858 | 4747 | 3 | F | Clarification for GBR and non-GBR support of PDU set QoS Parameters | 18.3.0 |
| 2023-09 | SP#101 | SP-230859 | 4748 | 1 | F | General corrections and alignment for TS23.501 | 18.3.0 |
| 2023-09 | SP#101 | SP-230848 | 4750 | 2 | F | Alt. 1 for the equivalent SNPN used by the UE for Localized Services | 18.3.0 |
| 2023-09 | SP#101 | SP-230854 | 4755 | 3 | F | PIN direct and indirect communication definition correction | 18.3.0 |
| 2023-09 | SP#101 | SP-230854 | 4761 | 2 | F | Make PIN ID unique in PLMN | 18.3.0 |
| 2023-09 | SP#101 | SP-230845 | 4767 | 3 | F | Meaning of availability for 3GPP access | 18.3.0 |
| 2023-09 | SP#101 | SP-230846 | 4769 | 1 | F | Service correction related to traffic correlation | 18.3.0 |
| 2023-09 | SP#101 | SP-230853 | 4770 | 1 | F | Provision of eDRX for RRC_INACTIVE with PTW | 18.3.0 |
| 2023-09 | SP#101 | SP-230857 | 4772 | 2 | F | CAG application for MBSR | 18.3.0 |
| 2023-09 | SP#101 | SP-230854 | 4773 | 3 | F | PIN description correction | 18.3.0 |
| 2023-09 | SP#101 | SP-230833 | 4775 | - | A | Removal of Editor's note for NTN tracking area handling | 18.3.0 |
| 2023-09 | SP#101 | SP-230845 | 4777 | 2 | F | ATSSS_Ph3 Enhanced Considerations of MPQUIC Multi-layer Stack Parameter Settings &amp; Logics | 18.3.0 |
| 2023-09 | SP#101 | SP-230848 | 4784 | 1 | F | Method for exchange info to determine SNPN selection | 18.3.0 |
| 2023-09 | SP#101 | SP-230845 | 4791 | - | F | Clarification on non-3GPP path switching capability when a UE is registered to different PLMNs over 3GPP and non-3GPP accesses | 18.3.0 |
| 2023-09 | SP#101 | SP-230847 | 4798 | 2 | F | Interoperability Indicator for NWDAF discovery and selection | 18.3.0 |
| 2023-09 | SP#101 | SP-230837 | 4817 | 1 | A | PLMN list for NSWO in roaming scenario | 18.3.0 |
| 2023-09 | SP#101 | SP-230846 | 4819 | - | F | clarification on Subscriber category in AF request | 18.3.0 |
| 2023-09 | SP#101 | SP-230859 | 4829 | 3 | F | Update to Network Triggered Service Request for UE in CM_IDLE with Connection Suspend | 18.3.0 |
| 2023-09 | SP#101 | SP-230854 | 4832 | 3 | F | Terminology and specification of functinalties not applicable to PIN. | 18.3.0 |
| 2023-09 | SP#101 | SP-230856 | 4836 | - | F | Adjust AoI | 18.3.0 |
| 2023-09 | SP#101 | SP-230850 | 4839 | 2 | F | Clarifications on NSAC for maximum number of UEs with at least one PDU SessionPDN Connection | 18.3.0 |
| 2023-09 | SP#101 | SP-230858 | 4844 | 3 | F | Corrections on Protocol Description | 18.3.0 |
| 2023-09 | SP#101 | SP-230859 | 4848 | 1 | F | UE Mobility Reference | 18.3.0 |
| 2023-09 | SP#101 | SP-230846 | 4849 | 1 | F | Selection of Common DNAI | 18.3.0 |
| 2023-09 | SP#101 | SP-230835 | 4852 | 1 | A | Clarification on eDRX support for power saving enhancement | 18.3.0 |
| 2023-09 | SP#101 | SP-230841 | 4854 | 4 | F | Clarify on Discontinuous Coverage Support negotiation | 18.3.0 |
| 2023-09 | SP#101 | SP-230845 | 4856 | 1 | F | Editorial correction on ATSSS architecture | 18.3.0 |
| 2023-09 | SP#101 | SP-230849 | 4857 | 4 | F | Downlink packet handling for UE when outside of slice support area | 18.3.0 |
| 2023-09 | SP#101 | SP-230846 | 4858 | - | F | Update on NEF functionality | 18.3.0 |
| 2023-09 | SP#101 | SP-230856 | 4859 | 2 | F | Updates on timing synchronization status reporting | 18.3.0 |
| 2023-09 | SP#101 | SP-230842 | 4861 | 1 | F | QoS monitoring | 18.3.0 |
| 2023-09 | SP#101 | SP-230846 | 4862 | 3 | F | Clarification and editorial on the AF request influence on traffic routing for set of UEs | 18.3.0 |
| 2023-09 | SP#101 | SP-230845 | 4864 | - | F | Clarifications to the Redundant Steering Mode | 18.3.0 |
| 2023-09 | SP#101 | SP-230858 | 4869 | 2 | F | Update on support of PDU Set handling | 18.3.0 |
| 2023-09 | SP#101 | SP-230847 | 4876 | 2 | F | Clarification on NWDAF functionalities and NF profile in TS 23.501 | 18.3.0 |
| 2023-09 | SP#101 | SP-230856 | 4887 | 2 | F | Clarification for time synchronization service monitoring | 18.3.0 |
| 2023-09 | SP#101 | SP-230859 | 4891 | 2 | F | Further clarification on transfer of emergency PDU session from non-3GPP to 3GPP access | 18.3.0 |
| 2023-09 | SP#101 | SP-230838 | 4893 | 2 | A | Aligning secure DNS with SA3 specifications | 18.3.0 |
| 2023-09 | SP#101 | SP-230858 | 4907 | 4 | F | PDU Set QoS handling: Race conditions at mobility from supporting to non-supporting gNB | 18.3.0 |
| 2023-09 | SP#101 | SP-230859 | 4920 | 1 | F | NSAC back-off timer correction | 18.3.0 |
| 2023-12 | SP#102 | SP-231260 | 4350 | 4 | F | Clarification on the list of TAs associated with S-NSSAI partially rejected in the RA | 18.4.0 |
| 2023-12 | SP#102 | SP-231260 | 4480 | 5 | F | PDU session inactivity timer for MAPDU session | 18.4.0 |
| 2023-12 | SP#102 | SP-231260 | 4631 | 8 | F | Handling of rejected S-NSSAI from the NSSF by AMF:KI#5 | 18.4.0 |
| 2023-12 | SP#102 | SP-231362 | 4649 | 6 | F | Clean Up of Hierarchical NSAC Architecture | 18.4.0 |
| 2023-12 | SP#102 | SP-231249 | 4689 | 3 | F | Unavailability period EPC interworking aspects | 18.4.0 |
| 2023-12 | SP#102 | SP-231263 | 4724 | 3 | F | Adding 'URSP delivery over EPS' capability in PCF profile in NRF (23.501) | 18.4.0 |
| 2023-12 | SP#102 | SP-231260 | 4740 | 4 | F | PDU Session management when the UE is outside the area of slice support or availability | 18.4.0 |
| 2023-12 | SP#102 | SP-231234 | 4744 | 7 | B | PDU Set based QoS Handling for uplink transmission | 18.4.0 |
| 2023-12 | SP#102 | SP-231769 | 4749 | 8 | F | Network Slice usage control clarification | 18.4.0 |
| 2023-12 | SP#102 | SP-231269 | 4760 | 4 | F | Enabling PEMC manage PIN via UPF local switch | 18.4.0 |
| 2023-12 | SP#102 | SP-231269 | 4762 | 3 | F | Correction to SMF behaviour for non-3GPP delay budget | 18.4.0 |
| 2023-12 | SP#102 | SP-231267 | 4771 | 4 | B | Support of RRC_INACTIVE with MT-SDT | 18.4.0 |
| 2023-12 | SP#102 | SP-231248 | 4781 | 4 | F | Handling of EPS interworking due to NS-AoS | 18.4.0 |
| 2023-12 | SP#102 | SP-231260 | 4783 | 2 | F | Partially Allowed NSSAI and S-NSSAIs used to determine RFSP | 18.4.0 |
| 2023-12 | SP#102 | SP-231259 | 4785 | 2 | D | eNPN_Ph2 general clean up | 18.4.0 |
| 2023-12 | SP#102 | SP-231259 | 4786 | 3 | F | SNPN N3WIF FQDN terminology alignment with stage 3 | 18.4.0 |
| 2023-12 | SP#102 | SP-231258 | 4788 | 3 | F | Add FL capability and ML model training related services | 18.4.0 |
| 2023-12 | SP#102 | SP-231259 | 4803 | 2 | F | Clarification on NAI format in NSWO scenario | 18.4.0 |
| 2023-12 | SP#102 | SP-231277 | 4807 | 3 | F | RT latency control and RT delay exposure for XR data flow | 18.4.0 |
| 2023-12 | SP#102 | SP-231254 | 4813 | 3 | F | Clarifications on redundant steering mode for GBR QoS Flow | 18.4.0 |
| 2023-12 | SP#102 | SP-231259 | 4818 | 1 | F | Clarification on SNPN list for NSWO in CH scenario | 18.4.0 |
| 2023-12 | SP#102 | SP-231260 | 4850 | 4 | F | Clarification for temporary slices having validity time information | 18.4.0 |
| 2023-12 | SP#102 | SP-231259 | 4865 | 2 | F | Correction to AMF selection for SNPN onboarding | 18.4.0 |
| 2023-12 | SP#102 | SP-231277 | 4871 | 3 | F | Clarifications of policy control enhancements for multi-modal services | 18.4.0 |
| 2023-12 | SP#102 | SP-231238 | 4910 | 2 | A | Add missing gate control information | 18.4.0 |
| 2023-12 | SP#102 | SP-231248 | 4921 | 1 | F | QoS Monitoring Report clarification | 18.4.0 |
| 2023-12 | SP#102 | SP-231248 | 4922 | 1 | F | Dual Connectivity terminology fixes and removal of obsolete Editor's Note | 18.4.0 |
| 2023-12 | SP#102 | SP-231259 | 4933 | 2 | D | Clarification on Stand-alone Non-Public Networks | 18.4.0 |
| 2023-12 | SP#102 | SP-231275 | 4935 | 2 | F | Clarification on Data exposure via SBI | 18.4.0 |
| 2023-12 | SP#102 | SP-231275 | 4937 | 3 | F | Update Architecture for UPF SBI interface | 18.4.0 |
| 2023-12 | SP#102 | SP-231275 | 4942 | 4 | F | Clarification on SMF and UPF functional description for UPF event exposure services | 18.4.0 |
| 2023-12 | SP#102 | SP-231277 | 4943 | 1 | F | Correction on network exposure of estimated bandwidth | 18.4.0 |
| 2023-12 | SP#102 | SP-231259 | 4947 | 2 | F | Clarifications for Enabling Access to Localized Services | 18.4.0 |
| 2023-12 | SP#102 | SP-231616 | 4949 | 5 | F | Removing the Editor's Note about the interaction between NAS and AS | 18.4.0 |
| 2023-12 | SP#102 | SP-231276 | 4950 | 1 | F | Providing both ULI and Additional ULI to other NFs | 18.4.0 |
| 2023-12 | SP#102 | SP-231273 | 4955 | 4 | F | Correction on Support of Time Sensitive Networking (TSN) enabled Transport Network (TN) | 18.4.0 |
| 2023-12 | SP#102 | SP-231277 | 4957 | 3 | F | Correcting the Description of the N6 Traffic Parameter Measurement Report | 18.4.0 |
| 2023-12 | SP#102 | SP-231267 | 4960 | 1 | F | NGAP DL Data Notification Message update | 18.4.0 |
| 2023-12 | SP#102 | SP-231269 | 4961 | 3 | F | PIN ID clarification | 18.4.0 |
| 2023-12 | SP#102 | SP-231276 | 4962 | 2 | F | MBSR authorization handling update | 18.4.0 |
| 2023-12 | SP#102 | SP-231265 | 4964 | 2 | F | IAB authorization handling correction | 18.4.0 |
| 2023-12 | SP#102 | SP-231264 | 4965 | 2 | F | Corrections to QoS provisioning for a group | 18.4.0 |
| 2023-12 | SP#102 | SP-231250 | 4969 | 2 | F | Updates of functional description for 5G Satellite Backhaul | 18.4.0 |
| 2023-12 | SP#102 | SP-231264 | 4970 | 1 | F | Updates of functional description for LADN per DNN and S-NSSAI | 18.4.0 |
| 2023-12 | SP#102 | SP-231250 | 4975 | 1 | F | Clarifications to local switching via UPF deployed on satellite | 18.4.0 |
| 2023-12 | SP#102 | SP-231250 | 4976 | 2 | F | Correction to Edge Computing via UPF deployed on satellite | 18.4.0 |
| 2023-12 | SP#102 | SP-231258 | 4980 | 1 | F | Updates for registration and discovery for FL entity | 18.4.0 |
| 2023-12 | SP#102 | SP-231259 | 4981 | 3 | F | Congestion handling when a UE accesses an SNPN for Localized Services | 18.4.0 |
| 2023-12 | SP#102 | SP-231259 | 4987 | 3 | F | Adding architectures on supporting authentication for NSWO using CH with AAA Server via 5GC | 18.4.0 |
| 2023-12 | SP#102 | SP-231259 | 4988 | - | F | Correction the interface in the NSWO architecture for SNPN | 18.4.0 |
| 2023-12 | SP#102 | SP-231264 | 4989 | 1 | F | LADN (DNN+S-NSSAI) provisioning for individual subscriber and SMF behaviour | 18.4.0 |
| 2023-12 | SP#102 | SP-231264 | 4993 | 2 | F | Change of PDU Session Type correction | 18.4.0 |
| 2023-12 | SP#102 | SP-231275 | 5001 | 3 | F | Corrections to UPF Services | 18.4.0 |
| 2023-12 | SP#102 | SP-231275 | 5002 | 3 | F | UPF Data Collection with QoS Monitoring event | 18.4.0 |
| 2023-12 | SP#102 | SP-231277 | 5012 | 5 | F | Clarification on scenarios for enabling/disabling downlink PDU Set based Handling | 18.4.0 |
| 2023-12 | SP#102 | SP-231255 | 5016 | 1 | F | UPF behaviour alignment for DetNet | 18.4.0 |
| 2023-12 | SP#102 | SP-231273 | 5024 | 7 | F | Clarification on the support for AMF discovery at the TSCTSF | 18.4.0 |
| 2023-12 | SP#102 | SP-231277 | 5026 | 2 | F | Corrections of XRM-specific clauses | 18.4.0 |
| 2023-12 | SP#102 | SP-231264 | 5034 | 2 | F | Provisioning of LADN information | 18.4.0 |
| 2023-12 | SP#102 | SP-231260 | 5036 | 5 | F | Addressing EN on Downlink packet handling for UE with CM-IDLE mode when outside of slice support area | 18.4.0 |
| 2023-12 | SP#102 | SP-231273 | 5039 | 4 | F | Clarifications of Event ID broadcast in SIB9 | 18.4.0 |
| 2023-12 | SP#102 | SP-231248 | 5041 | 3 | F | Support of NR coverage enhancements | 18.4.0 |
| 2023-12 | SP#102 | SP-231248 | 5043 | 2 | F | Relaxation of 5QI delay requirements for first packets should also apply for RRC-INACTIVE mode and for other best effort 5QIs | 18.4.0 |
| 2023-12 | SP#102 | SP-231239 | 5054 | 1 | A | Addressing packet loss and first packet delay for public safety UEs | 18.4.0 |
| 2023-12 | SP#102 | SP-231248 | 5062 | 1 | F | Move text on providing a back-off timer to the UE during NSAC for maximum number of PDU Sessions | 18.4.0 |
| 2023-12 | SP#102 | SP-231259 | 5063 | 2 | F | ESNPN during registration for onboarding | 18.4.0 |
| 2023-12 | SP#102 | SP-231259 | 5064 | 2 | F | Correction on automatic SNPN selection for localized service | 18.4.0 |
| 2023-12 | SP#102 | SP-231259 | 5065 | - | F | Clarification on LADN support in SNPN | 18.4.0 |
| 2023-12 | SP#102 | SP-231276 | 5067 | 1 | F | Clarification on delay in deregistration procedure | 18.4.0 |
| 2023-12 | SP#102 | SP-231263 | 5070 | 3 | F | URSP delivery via EPS | 18.4.0 |
| 2023-12 | SP#102 | SP-231253 | 5073 | 2 | F | Removal of Editor's Note on charging of AI/ML traffic | 18.4.0 |
| 2023-12 | SP#102 | SP-231277 | 5080 | 4 | F | Support of PDU Set handling on a per direction basis | 18.4.0 |
| 2023-12 | SP#102 | SP-231269 | 5083 | 1 | F | AF for PIN description update | 18.4.0 |
| 2023-12 | SP#102 | SP-231269 | 5084 | - | F | Non-3GPP Delay clarification | 18.4.0 |
| 2023-12 | SP#102 | SP-231276 | 5085 | 3 | F | MBSR authorization area restriction | 18.4.0 |
| 2023-12 | SP#102 | SP-231253 | 5087 | - | F | R18 AIMLsys_KI7_23501 CR for clarifying AF filtering criteria | 18.4.0 |
| 2023-12 | SP#102 | SP-231254 | 5091 | 1 | F | Clarification on Suspend and Resume Traffic Duplication | 18.4.0 |
| 2023-12 | SP#102 | SP-231263 | 5096 | - | F | Clarification on URSP delivery in EPS | 18.4.0 |
| 2023-12 | SP#102 | SP-231253 | 5103 | 1 | F | Clarification on the Member UE selection | 18.4.0 |
| 2023-12 | SP#102 | SP-231248 | 5104 | 1 | F | Spending Limits for AM and UE Policies in the 5GC | 18.4.0 |
| 2023-12 | SP#102 | SP-231258 | 5105 | 2 | F | Correct NWDAF discovery principles | 18.4.0 |
| 2023-12 | SP#102 | SP-231260 | 5109 | 3 | F | Further clarification of NSAC | 18.4.0 |
| 2023-12 | SP#102 | SP-231263 | 5110 | 2 | F | Providing URSP support indication in EPS in PDN connectivity request | 18.4.0 |
| 2023-12 | SP#102 | SP-231263 | 5111 | 2 | F | Clarification on PCO support | 18.4.0 |
| 2023-12 | SP#102 | SP-231273 | 5115 | 3 | F | Alignment with RAN3 on the network timing synchronization status information | 18.4.0 |
| 2023-12 | SP#102 | SP-231237 | 5121 | 1 | A | Alignment of how Allowed NSSAI can be determined | 18.4.0 |
| 2023-12 | SP#102 | SP-231254 | 5123 | 3 | F | Clarify MRU handling for non-3GPP access path switching | 18.4.0 |
| 2023-12 | SP#102 | SP-231258 | 5125 | 2 | F | Correction for alignment with TS 23.288 regarding ML Model interoperability per Analytics ID | 18.4.0 |
| 2023-12 | SP#102 | SP-231512 | 5126 | 5 | F | Handling of Alternative S-NSSAI | 18.4.0 |
| 2023-12 | SP#102 | SP-231239 | 5128 | 1 | A | Requesting Configured NSSAI from NSSF | 18.4.0 |
| 2023-12 | SP#102 | SP-231260 | 5137 | 1 | F | Clarification on slice replacement from Alternative S-NSSAI to original S-NSSAI | 18.4.0 |
| 2023-12 | SP#102 | SP-231249 | 5141 | 2 | F | Corrections to Support of Unavailability Period and Overload control | 18.4.0 |
| 2023-12 | SP#102 | SP-231253 | 5142 | 1 | F | Clarification on the Member UE selection assistance functionality for application operation | 18.4.0 |
| 2023-12 | SP#102 | SP-231260 | 5156 | 4 | F | Clarification on Network Slice Replacement | 18.4.0 |
| 2023-12 | SP#102 | SP-231262 | 5162 | 3 | F | Clarification on eNSAC Option 1 | 18.4.0 |
| 2023-12 | SP#102 | SP-231249 | 5163 | 2 | F | Update on support of discontinuous coverage for satellite access | 18.4.0 |
| 2023-12 | SP#102 | SP-231249 | 5164 | - | F | Discontinuous coverage overload control priority users term alignment | 18.4.0 |
| 2023-12 | SP#102 | SP-231260 | 5170 | 4 | F | Clarifications about the Alternative S-NSSAI subject to NSSAA | 18.4.0 |
| 2023-12 | SP#102 | SP-231260 | 5172 | 3 | F | Update of definition of NSAC Service area. | 18.4.0 |
| 2023-12 | SP#102 | SP-231248 | 5185 | 1 | F | UE 5GSM capability indication for supporting secondary auth over EPC | 18.4.0 |
| 2023-12 | SP#102 | SP-231249 | 5187 | - | F | Satellite RAT Types in TS 23.501 | 18.4.0 |
| 2023-12 | SP#102 | SP-231239 | 5195 | 2 | A | Correction to Notification Endpoint | 18.4.0 |
| 2023-12 | SP#102 | SP-231256 | 5203 | 3 | F | KI#1 Alignment and correction on PLMN IDs in AF request | 18.4.0 |
| 2023-12 | SP#102 | SP-231248 | 5207 | 2 | F | Clarifying the ownership of data in UDSF | 18.4.0 |
| 2023-12 | SP#102 | SP-231276 | 5208 | 1 | F | Remove the editor's note for MBSR authorization indication | 18.4.0 |
| 2023-12 | SP#102 | SP-231767 | 4736 | 9 | F | Update for QoS monitoring and network exposure | 18.4.0 |
| 2023-12 | SP#102 | SP-231763 | 5008 | 7 | F | Correction and clarification of the Protocol Description definition | 18.4.0 |
| 2023-12 | SP#102 | SP-231765 | 5014 | 6 | F | Clarification on QoS flow mapping and service data flow | 18.4.0 |
| 2023-12 | SP#102 | SP-231766 | 5175 | 6 | F | Clarification of the Unmarked PDUs with SN Offset and PSI Value | 18.4.0 |
| 2023-12 | SP#102 | SP-231762 | 5186 | 3 | F | Incorrect reference in clause 5.15.17 for procedure for RAN initiated PDU session release | 18.4.0 |
| 2024-03 | SP#103 | SP-240101 | 4489 | 8 | F | Registration status after S-NSSAI removal based on S-NSSAI validity time information | 18.5.0 |
| 2024-03 | SP#103 | SP-240101 | 4583 | 5 | F | Congestion handling with Alternative S-NSSAI | 18.5.0 |
| 2024-03 | SP#103 | SP-240086 | 4660 | 6 | A | Non-Allowed areas clarifications related to MPS | 18.5.0 |
| 2024-03 | SP#103 | SP-240113 | 4812 | 7 | F | Corrections for traffic characteristics parameters in Alternative QoS Profile | 18.5.0 |
| 2024-03 | SP#103 | SP-240093 | 4929 | 1 | F | Removing editor's note on Prefixed N3IWF FQDN format | 18.5.0 |
| 2024-03 | SP#103 | SP-240085 | 4992 | 5 | A | Support of QMC configuration information | 18.5.0 |
| 2024-03 | SP#103 | SP-240115 | 5011 | 8 | F | Corrections to remove Nnef_UEId Service restrictions | 18.5.0 |
| 2024-03 | SP#103 | SP-240089 | 5032 | 4 | F | Updated description of UE Location verification for NTN | 18.5.0 |
| 2024-03 | SP#103 | SP-240113 | 5081 | 2 | F | Correction on Congestion Information Exposure | 18.5.0 |
| 2024-03 | SP#103 | SP-240077 | 5082 | 3 | F | Correction of UPF reporting of QoS Monitoring packet delay | 18.5.0 |
| 2024-03 | SP#103 | SP-240098 | 5095 | 2 | F | Clarification on DL Session AMBR for Offloading in HR-SBO sessions | 18.5.0 |
| 2024-03 | SP#103 | SP-240110 | 5106 | 2 | F | Clarification on AoI of time synchronization service | 18.5.0 |
| 2024-03 | SP#103 | SP-240110 | 5122 | 1 | F | Correction of additional parameters inside AF Request Authorization | 18.5.0 |
| 2024-03 | SP#103 | SP-240191 | 5145 | 1 | F | Corrections for NWDAF functionality description | 18.5.0 |
| 2024-03 | SP#103 | SP-240102 | 5179 | 5 | F | Clarifications related to the scenario when the PDN connection handlig the UE Policy Container is released. | 18.5.0 |
| 2024-03 | SP#103 | SP-240110 | 5181 | 2 | F | KI#5 Corrections on Proactive RAN Feedback and TSN enabled TN | 18.5.0 |
| 2024-03 | SP#103 | SP-240107 | 5182 | 2 | F | Mega CR for editorial modification | 18.5.0 |
| 2024-03 | SP#103 | SP-240089 | 5202 | 2 | F | UE capability for network verified location | 18.5.0 |
| 2024-03 | SP#103 | SP-240090 | 5214 | 1 | F | Correction for multiple broadcast TA reporting in NR Satellite access | 18.5.0 |
| 2024-03 | SP#103 | SP-240113 | 5215 | 1 | F | Clarification on periodicity change from AF | 18.5.0 |
| 2024-03 | SP#103 | SP-240102 | 5217 | 1 | F | PDN Selection for URSP delivery in EPS | 18.5.0 |
| 2024-03 | SP#103 | SP-240112 | 5220 | 7 | F | MBSR mobility | 18.5.0 |
| 2024-03 | SP#103 | SP-240101 | 5221 | 1 | F | Clarification on Slice Replacement | 18.5.0 |
| 2024-03 | SP#103 | SP-240113 | 5222 | 1 | F | Packet filter with DSCP and ECN | 18.5.0 |
| 2024-03 | SP#103 | SP-240113 | 5224 | 3 | F | PSER and PSDB supersede the PER and PDB per direction | 18.5.0 |
| 2024-03 | SP#103 | SP-240110 | 5225 | 4 | F | Correction on CN PDB configured in NG-RAN | 18.5.0 |
| 2024-03 | SP#103 | SP-240091 | 5226 | 1 | F | Clarification on satellite backhaul category change indication | 18.5.0 |
| 2024-03 | SP#103 | SP-240113 | 5228 | 3 | F | Protocol Descriptions for UL and DL traffic | 18.5.0 |
| 2024-03 | SP#103 | SP-240136 | 5229 | 1 | F | Spending Limits for AM and UE Policies in the 5GC | 18.5.0 |
| 2024-03 | SP#103 | SP-240096 | 5230 | 1 | F | Clarify MRU handling for non-3GPP access path switching when UE has only one PDU Session | 18.5.0 |
| 2024-03 | SP#103 | SP-240101 | 5233 | 6 | F | Clarifications on PDU Sessions due to Network Slice Replacement | 18.5.0 |
| 2024-03 | SP#103 | SP-240095 | 5235 | 1 | D | Cleaning up the term of RFSP Index in Use Validity Time | 18.5.0 |
| 2024-03 | SP#103 | SP-240104 | 5237 | 1 | F | LADN provisioning when there is existing PDU session | 18.5.0 |
| 2024-03 | SP#103 | SP-240104 | 5238 | 1 | F | Clarification on the temporal invalidity conditions | 18.5.0 |
| 2024-03 | SP#103 | SP-240110 | 5239 | 2 | F | CQRCI check issue when there are both AF requests and subscriptions | 18.5.0 |
| 2024-03 | SP#103 | SP-240110 | 5240 | 1 | F | Clarification on the UE capability and re-connection indication | 18.5.0 |
| 2024-03 | SP#103 | SP-240110 | 5241 | 1 | F | Correction on InterfaceConfiguration and InterfaceCapability | 18.5.0 |
| 2024-03 | SP#103 | SP-240101 | 5243 | 5 | F | Clarification on subscription retrieval during slice replacement | 18.5.0 |
| 2024-03 | SP#103 | SP-240113 | 5245 | 3 | F | Corrections of XRM related clauses | 18.5.0 |
| 2024-03 | SP#103 | SP-240110 | 5246 | 5 | F | TSCTSF subscribing to RAN TSS based on list of TAs, correction to ASTI without AF request | 18.5.0 |
| 2024-03 | SP#103 | SP-240110 | 5248 | 1 | F | Updating TSCAI and TSCAC to Traffic Assistance Information | 18.5.0 |
| 2024-03 | SP#103 | SP-240112 | 5250 | 1 | F | Corrections on mobile IAB-DU's TAC provisioning | 18.5.0 |
| 2024-03 | SP#103 | SP-240100 | 5252 | 1 | F | Clarification/Alignment on usage of Decorated NAI for 5G-NSWO in case of SNPNs. | 18.5.0 |
| 2024-03 | SP#103 | SP-240100 | 5253 | - | F | Correction on NSSAAF Selection in case of SNPN | 18.5.0 |
| 2024-03 | SP#103 | SP-240096 | 5261 | 1 | F | Clarifications on interworking with EPS | 18.5.0 |
| 2024-03 | SP#103 | SP-240100 | 5262 | 1 | F | Clarifications on network re-selection for SNPN for accessing Localized Services | 18.5.0 |
| 2024-03 | SP#103 | SP-240100 | 5263 | 1 | F | Correction on validity information for SNPN | 18.5.0 |
| 2024-03 | SP#103 | SP-240100 | 5264 | 1 | F | Correction on validity information for CAG | 18.5.0 |
| 2024-03 | SP#103 | SP-240101 | 5265 | 7 | F | Clarification on Network Slice usage control timer | 18.5.0 |
| 2024-03 | SP#103 | SP-240113 | 5267 | 1 | F | Modification to the Packet delay variation monitoring | 18.5.0 |
| 2024-03 | SP#103 | SP-240115 | 5273 | 1 | B | Update to Support Network Controlled Repeater | 18.5.0 |
| 2024-03 | SP#103 | SP-240101 | 5277 | 8 | F | Support of Network Slice Replacement and area restrictions at UE mobility | 18.5.0 |
| 2024-03 | SP#103 | SP-240101 | 5278 | 1 | F | Determination of release or deactivation of PDU Session due to S-NSSAI not supported | 18.5.0 |
| 2024-03 | SP#103 | SP-240113 | 5281 | 1 | F | Clarifications on non-homogeneous support of PDU set based handling in NG-RAN | 18.5.0 |
| 2024-03 | SP#103 | SP-240113 | 5282 | 1 | F | Clarifications on ECN marking for L4S | 18.5.0 |
| 2024-03 | SP#103 | SP-240101 | 5286 | 3 | F | Clarification on Allowed NSSAI for network slice replacement | 18.5.0 |
| 2024-03 | SP#103 | SP-240101 | 5291 | 1 | F | Network Slice usage control for emergency service | 18.5.0 |
| 2024-03 | SP#103 | SP-240101 | 5292 | 4 | F | Clarification on Network based monitoring and enforcement for NS-AoS and partially Allowed NSSAI | 18.5.0 |
| 2024-03 | SP#103 | SP-240113 | 5295 | 3 | F | Clarifications on applicability of Protocol Description in PDR for EoDB identification in DL | 18.5.0 |
| 2024-03 | SP#103 | SP-240081 | 5297 | 1 | F | Access control for users with eRedcap/Redcap subscriptions | 18.5.0 |
| 2024-03 | SP#103 | SP-240096 | 5299 | - | F | MPQUIC support related corrections | 18.5.0 |
| 2024-03 | SP#103 | SP-240084 | 5301 | 1 | A | Handover control for NR-terrestrial to LTE satellite access | 18.5.0 |
| 2024-03 | SP#103 | SP-240112 | 5302 | 1 | F | Clarification on mobile IAB indication when establishing RRC connection | 18.5.0 |
| 2024-03 | SP#103 | SP-240112 | 5303 | 1 | F | Indication to AMF for MBSR connection release | 18.5.0 |
| 2024-03 | SP#103 | SP-240090 | 5304 | 1 | F | Clarification on unavailability period | 18.5.0 |
| 2024-03 | SP#103 | SP-240112 | 5305 | - | F | Clarification on AMF selection | 18.5.0 |
| 2024-03 | SP#103 | SP-240098 | 5310 | 2 | F | KI#4 Clarifications on common EAS/DNAI procedure | 18.5.0 |
| 2024-03 | SP#103 | SP-240110 | 5311 | 3 | F | Update TSCAI at SMF based on proactive RAN feedback on BAT and periodicity | 18.5.0 |
| 2024-03 | SP#103 | SP-240113 | 5313 | 2 | F | Correct the misalignment for congestion exposure and L4S | 18.5.0 |
| 2024-03 | SP#103 | SP-240098 | 5319 | 1 | F | Update Network function update of SMF and UPF selection for HR-SBO | 18.5.0 |
| 2024-03 | SP#103 | SP-240191 | 5320 | 2 | F | Correction to the FL capability type | 18.5.0 |
| 2024-03 | SP#103 | SP-240101 | 5321 | 3 | F | DNN selection for Alternative S-NSSAI | 18.5.0 |
| 2024-03 | SP#103 | SP-240110 | 5327 | 2 | F | Corrections to timing synchronization status reporting | 18.5.0 |
| 2024-03 | SP#103 | SP-240113 | 5328 | 1 | F | Correction of ECN Marking for L4S by UPF | 18.5.0 |
| 2024-03 | SP#103 | SP-240113 | 5331 | 4 | F | Clarification on support of PDU Set based QoS | 18.5.0 |
| 2024-03 | SP#103 | SP-240094 | 5332 | 2 | F | Support of 5GC UE level measurements collection | 18.5.0 |
| 2024-03 | SP#103 | SP-240191 | 5334 | 1 | F | Alignments for the Accuracy checking capability in TS 23.501 | 18.5.0 |
| 2024-03 | SP#103 | SP-240113 | 5339 | 2 | F | Incorrect Protocol Description options including SRTP together with RTP Payload Format | 18.5.0 |
| 2024-03 | SP#103 | SP-240114 | 5342 | 2 | F | DSCP and ECN within the IP Header | 18.5.0 |
| 2024-03 | SP#103 | SP-240114 | 5343 | 1 | F | Max MTU for XR and, for PDU sessions subject to handover from EPS to 5GC | 18.5.0 |
| 2024-03 | SP#103 | SP-240110 | 5344 | 2 | F | Clock status indication from RAN to TSCTSF | 18.5.0 |
| 2024-06 | SP#104 | SP-240597 | 4926 | 5 | F | Clarification on access dependency of Alternative S-NSSAI | 18.6.0 |
| 2024-06 | SP#104 | SP-240591 | 4951 | 2 | F | Clarification on TNGF identifiers | 18.6.0 |
| 2024-06 | SP#104 | SP-240602 | 5204 | 6 | F | Operator specific QoS and handling at inter-PLMN mobility | 18.6.0 |
| 2024-06 | SP#104 | SP-240600 | 5254 | 6 | F | Clarification on (e)RedCap UE | 18.6.0 |
| 2024-06 | SP#104 | SP-240604 | 5258 | 3 | F | Clarification on providing the additional location and time restrictions information to the MBSR IAB-UE | 18.6.0 |
| 2024-06 | SP#104 | SP-240593 | 5322 | 1 | F | Corrections on supported Steering Modes for a MA PDU Session | 18.6.0 |
| 2024-06 | SP#104 | SP-240597 | 5326 | 5 | F | Distinction between network slice supported and available in an area | 18.6.0 |
| 2024-06 | SP#104 | SP-240597 | 5346 | 5 | F | Slice deregistration inactvity timer clarification | 18.6.0 |
| 2024-06 | SP#104 | SP-240602 | 5355 | 1 | F | Alignment of NWDAF discovery parameters | 18.6.0 |
| 2024-06 | SP#104 | SP-240582 | 5359 | 1 | A | Correction on TSCAI calculation | 18.6.0 |
| 2024-06 | SP#104 | SP-240594 | 5361 | 3 | F | Security for EAS discovery procedure via (V-)EASDF | 18.6.0 |
| 2024-06 | SP#104 | SP-240602 | 5362 | - | F | Adding a missing Nudm service (Nudm_UEIdentifier used in 33.503) | 18.6.0 |
| 2024-06 | SP#104 | SP-240602 | 5366 | 2 | F | RAT type change impact to AM Policy association | 18.6.0 |
| 2024-06 | SP#104 | SP-240598 | 5368 | 1 | F | Corrections on the clause reference and ID mapping | 18.6.0 |
| 2024-06 | SP#104 | SP-240602 | 5369 | 1 | F | Clarification on UEs accessing to GERAN/UTRAN over Gn/Gp | 18.6.0 |
| 2024-06 | SP#104 | SP-240600 | 5371 | 3 | F | RedCap/eRedCap UE differentiation upon change of radio capabilities | 18.6.0 |
| 2024-06 | SP#104 | SP-240589 | 5372 | 3 | F | Unavailability period during initial Registration procedure | 18.6.0 |
| 2024-06 | SP#104 | SP-240589 | 5379 | 2 | F | Clarification on Discontinuous coverage for satellite access | 18.6.0 |
| 2024-06 | SP#104 | SP-240596 | 5381 | 2 | F | Clarification on location validity information. | 18.6.0 |
| 2024-06 | SP#104 | SP-240603 | 5385 | 2 | F | Clarifications for UPF selection | 18.6.0 |
| 2024-06 | SP#104 | SP-240602 | 5386 | 2 | F | Update description of UE location verification for NTN | 18.6.0 |
| 2024-06 | SP#104 | SP-240600 | 5388 | 1 | F | Activation of DL data size reporting for support of MT-SDT | 18.6.0 |
| 2024-06 | SP#104 | SP-240605 | 5391 | 1 | F | Clarification on the TSCAI parameters for XR | 18.6.0 |
| 2024-06 | SP#104 | SP-240597 | 5394 | 2 | F | Temporary slice expiry | 18.6.0 |
| 2024-06 | SP#104 | SP-240597 | 5396 | 2 | F | Slice area restriction in case of ETSUN or roaming | 18.6.0 |
| 2024-06 | SP#104 | SP-240602 | 5404 | 2 | D | 23.501 Cleanup CR | 18.6.0 |
| 2024-09 | SP#105 | SP-241244 | 5345 | 5 | F | Handling for UE when present in overlapping of non-allowed area and slice location availability area | 18.7.0 |
| 2024-09 | SP#105 | SP-241244 | 5370 | 4 | F | Handling of the slice deregistration inactivity timer in the inter AMF mobility | 18.7.0 |
| 2024-09 | SP#105 | SP-241261 | 5401 | 3 | F | Session level priority realization in AMF | 18.7.0 |
| 2024-09 | SP#105 | SP-241251 | 5410 | 1 | F | KI#5 correction to reference of IEEE | 18.7.0 |
| 2024-09 | SP#105 | SP-241261 | 5416 | 1 | F | Support for SMS over NAS in Disaster Roaming | 18.7.0 |
| 2024-09 | SP#105 | SP-241278 | 5418 | 1 | F | Lack of indication of Emergency Service Support over NG | 18.7.0 |
| 2024-09 | SP#105 | SP-241278 | 5426 | 2 | F | Clarifications on NWDAF serving area | 18.7.0 |
| 2024-09 | SP#105 | SP-241259 | 5428 | 1 | F | Removal of Editor's note on the use of TLS with MPQUIC | 18.7.0 |
| 2024-09 | SP#105 | SP-241261 | 5432 | 2 | F | Align H-PCF selection with H-SMF selection in 23.501 R18 | 18.7.0 |
| 2024-09 | SP#105 | SP-241261 | 5434 | 1 | F | Support of a UE registered over both 3GPP and Non-3GPP access | 18.7.0 |
| 2024-09 | SP#105 | SP-241260 | 5448 | 1 | F | Alignment action of EAS IP replacement in SMF and UPF | 18.7.0 |
| 2024-09 | SP#105 | SP-241254 | 5456 | 2 | F | Corrections of Traffic Detection Information related descriptions | 18.7.0 |
| 2024-09 | SP#105 | SP-241261 | 5458 | - | F | Correction on MSISDN exposure | 18.7.0 |
| 2024-09 | SP#105 | SP-241252 | 5473 | 2 | F | Subscription of UPF event via I-SMF | 18.7.0 |
| 2024-09 | SP#105 | SP-241251 | 5477 | - | F | Correct to align with RAN for reactive RAN feedback for Burst Arrival Time adaptation | 18.7.0 |
| 2024-09 | SP#105 | SP-241251 | 5479 | - | F | Correction on mapping of the parameters between 5GS and TSN UNI | 18.7.0 |
| 2024-09 | SP#105 | SP-241243 | 5481 | 3 | F | Correction NWDAF discovery and selection | 18.7.0 |
| 2024-09 | SP#105 | SP-241253 | 5486 | 1 | F | Correction of the reference clause and duplicate description | 18.7.0 |
| 2024-09 | SP#105 | SP-241247 | 5494 | 2 | F | Access restrictions for satellite access in the context of 5GC-EPC interworking | 18.7.0 |
| 2024-09 | SP#105 | SP-241253 | 5509 | - | F | Clarification on CAG related UE access restriction | 18.7.0 |
| 2024-09 | SP#105 | SP-241254 | 5511 | - | F | Clarification on End of Data Burst Indication | 18.7.0 |
| 2024-09 | SP#105 | SP-241258 | 5535 | - | F | Correction on N3IWF selection | 18.7.0 |
| 2024-09 | SP#105 | SP-241241 | 5558 | 1 | A | Network Slicing handling for EHPLMN case | 18.7.0 |
| 2024-09 | SP#105 | SP-241261 | 5566 | - | F | Correction of PCF related terminology | 18.7.0 |
| 2024-09 | SP#105 | SP-241256 | 5569 | 2 | F | Clarification on PRU timer considering start of unavailability period | 18.7.0 |
| 2024-09 | SP#105 | SP-241259 | 5576 | 1 | F | Correction of MPQUIC Datagram mode 1 | 18.7.0 |
| 2024-09 | SP#105 | SP-241244 | 5585 | 3 | F | PDU Session clarification when the slice is associated with slice restricted area | 18.7.0 |
| 2024-09 | SP#105 | SP-241254 | 5599 | 2 | F | Clarification on Congestion Event Triggered Reporting | 18.7.0 |
| 2024-09 | SP#105 | SP-241256 | 5614 | 2 | F | Applying AMF determined unavailability values | 18.7.0 |
| 2024-12 | SP#106 | SP-241475 | 5408 | 5 | F | URSP provisioning in EPS support indication at PDU Session Establishment | 18.8.0 |
| 2024-12 | SP#106 | SP-241471 | 5609 | 1 | F | Add missing MFAF Services | 18.8.0 |
| 2024-12 | SP#106 | SP-241468 | 5647 | 1 | F | Correction on PDU Session supporting CIoT | 18.8.0 |
| 2024-12 | SP#106 | SP-241968 | 5682 | 5 | F | Clarification on network slice handling for EHPLMN | 18.8.0 |
| 2024-12 | SP#106 | SP-241478 | 5701 | - | F | Non-3GPP QoS Assistance information update | 18.8.0 |
| 2024-12 | SP#106 | SP-241468 | 5704 | 1 | F | Missing NRF NF instances for CHF and correction | 18.8.0 |
| 2024-12 | SP#106 | SP-241466 | 5715 | 1 | F | Additional ULI only provided to LMF | 18.8.0 |
| 2024-12 | SP#106 | SP-241468 | 5779 | - | F | UDR Discovery/Selection for Group ID Mapping | 18.8.0 |
| 2025-03 | SP#107 | SP-250053 | 5890 | 1 | F | XRM services support in Roaming scenarios | 18.9.0 |
| 2025-03 | SP#107 | SP-250045 | 5895 | 3 | F | Prioritization between UDM, OAM and NSSF based slice validity time | 18.9.0 |
| 2025-03 | SP#107 | SP-250033 | 5931 | 1 | F | VPLMN QoS constraint clarification | 18.9.0 |
| 2025-03 | SP#107 | SP-250052 | 5947 | 1 | F | Addition of missing LLDP TLVs | 18.9.0 |
| 2025-03 | SP#107 | SP-250035 | 5949 | - | F | Updated reference for DetNet RFC | 18.9.0 |
| 2025-03 | SP#107 | SP-250045 | 6032 | 1 | F | Slice deregistration inactivity timer for Alternative S-NSSAI | 18.9.0 |
| 2025-03 | SP#107 | SP-250051 | 6062 | 1 | F | Alignment of Subscription of UPF event via I-SMF | 18.9.0 |
| 2025-03 | SP#107 | SP-250051 | 6123 | 3 | F | Clarification on the UPF Event Exposure | 18.9.0 |
| 2025-06 | SP#108 | SP-250458 | 5255 | 12 | F | Clarifications for multi-modal services | 18.10.0 |
| 2025-06 | SP#108 | SP-250458 | 6204 | 2 | F | Fix PDU Set based Handling description | 18.10.0 |
| 2025-06 | SP#108 | SP-250457 | 6211 | 2 | F | PWS enhancements for MBSR | 18.10.0 |
| 2025-06 | SP#108 | SP-250455 | 6237 | 4 | F | Clarification on always-on PDU Session | 18.10.0 |
| 2025-06 | SP#108 | SP-250451 | 6268 | 6 | F | 5GS common time reference traceable to UTC | 18.10.0 |
| 2025-06 | SP#108 | SP-250452 | 6276 | 3 | F | Alignment with ATSSS Capability IE | 18.10.0 |
| 2025-09 | SP#109 | SP-250943 | 6018 | 5 | F | Clarification on the removal of S-NSSAI from the Configured NSSAI | 18.11.0 |
| 2025-09 | SP#109 | SP-250944 | 6378 | 2 | F | Correcting wrong statemen w.r.t SSC modes 2/3 for I-SMF insertion | 18.11.0 |
| 2025-09 | SP#109 | SP-250944 | 6404 | 1 | F | Clarification for QoS monitoring parameters provided to UPF | 18.11.0 |
| 2025-12 | SP#110 | SP-251319 | 6085 | 4 | A | Clarification of eDRX application with emergency service | 18.12.0 |
| 2025-12 | SP#110 | SP-251319 | 6301 | 5 | A | UE radio capability for paging handling | 18.12.0 |
| 2025-12 | SP#110 | SP-251322 | 6454 | 1 | F | Partially Allowed NSSAI handling for network slice replacement | 18.12.0 |
| 2025-12 | SP#110 | SP-251319 | 6468 | 1 | A | PEIPS for emergency PDU session | 18.12.0 |
<!-- /table -->
