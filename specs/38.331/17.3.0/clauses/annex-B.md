# Annex B (informative): RRC Information

# B.1 Protection of RRC messages

The following list provides information which messages can be sent (unprotected) prior to AS security activation and which messages can be sent unprotected after AS security activation. Those messages indicated "-" in "P" column should never be sent unprotected by gNB or UE. Further requirements are defined in the procedural text.

P…Messages that can be sent (unprotected) prior to AS security activation

A – I…Messages that can be sent without integrity protection after AS security activation

A – C…Messages that can be sent unciphered after AS security activation

NA… Message can never be sent after AS security activation

<!-- table -->
| Message | P | A-I | A-C | Comment |
| CounterCheck | - | - | - |  |
| CounterCheckResponse | - | - | - |  |
| DedicatedSIBRequest | + | - | - |  |
| DLDedicatedMessageSegment | NOTE 1 |  |  |  |
| DLInformationTransfer | + | - | - |  |
| DLInformationTransferMRDC | - | - | - |  |
| FailureInformation | - | - | - |  |
| LocationMeasurementIndication | - | - | - |  |
| MCGFailureInformation | - | - | - |  |
| MeasurementReportAppLayer | - | - | - |  |
| MBSBroadcastConfiguration | + | + | + |  |
| MBSInterestIndication | - | - | - |  |
| MIB | + | + | + |  |
| MeasurementReport | - | - | - | Measurement configuration may be sent prior to AS security activation. But: In order to protect privacy of UEs, MeasurementReport is only sent from the UE after successful AS security activation. |
| MobilityFromNRCommand | - | - | - |  |
| Paging | + | + | + |  |
| RRCReconfiguration | + | - | - | The message shall not be sent unprotected before AS security activation if it is used to perform handover or to establish SRB2, SRB4, multicast MRBs and DRBs. |
| RRCReconfigurationComplete | + | - | - | Unprotected, if sent as response to RRCReconfiguration which was sent before AS security activation. |
| RRCReestablishment | - | - | + | Integrity protection applied, but no ciphering. |
| RRCReestablishmentComplete | - | - | - |  |
| RRCReestablishmentRequest | - | - | + | This message is not protected by PDCP operation. However, a shortMAC-I is included. |
| RRCReject | + | + | + | Justification for A-I and A-C: the message can be sent in SRB0 in RRC_INACTIVE state, after the AS security is activated. |
| RRCRelease | + | - | - | Justification for P: If the RRC connection only for signalling not requiring DRBs or ciphered messages, or the signalling connection has to be released prematurely, this message is sent as unprotected. RRCRelease message sent before AS security activation cannot include deprioritisationReq, suspendConfig, redirectedCarrierInfo, cellReselectionPriorities information fields. |
| RRCResume | - | - | - |  |
| RRCResumeComplete | - | - | - |  |
| RRCResumeRequest | - | - | + | This message is not protected by PDCP operation. However, a resumeMAC-I is included. |
| RRCResumeRequest1 | - | - | + | This message is not protected by PDCP operation. However, a resumeMAC-I is included. |
| RRCSetup | + | + | + | Justification for A-I and A-C: the message can be sent in SRB0 in RRC_INACTIVE or RRC_CONNECTED states, after the AS security is activated. |
| RRCSetupComplete | + | NA | NA |  |
| RRCSetupRequest | + | NA | NA |  |
| RRCSystemInfoRequest | + | + | + | Justification for A-I and A-C: the message can be sent in SRB0 in RRC_INACTIVE state, after the AS security is activated. |
| SIB1 | + | + | + |  |
| SCGFailureInformation | - | - | - |  |
| SCGFailureInformationEUTRA | - | - | - |  |
| SecurityModeCommand | + | NA | NA | Integrity protection applied, but no ciphering (integrity verification done after the message received by RRC). |
| SecurityModeComplete | - | - | + | The message is sent after AS security activation. Integrity protection applied, but no ciphering. Ciphering is applied after completing the procedure. |
| SecurityModeFailure | + | NA | NA | Neither integrity protection nor ciphering applied. |
| SidelinkUEInformationNR | + | - | - | The message shall not be sent unprotected before AS security activation if sl-CapabilityInformationSidelink information field is included in the message. |
| SystemInformation | + | + | + |  |
| UEAssistanceInformation | - | - | - |  |
| UECapabilityEnquiry | + | - | - | The network should retrieve UE capabilities only after AS security activation. |
| UECapabilityInformation | + | - | - |  |
| ULDedicatedMessageSegment | + | - | - |  |
| UEInformationRequest | - | - | - |  |
| UEInformationResponse | - | - | - | In order to protect privacy of UEs, UEInformationResponse is only sent from the UE after successful security activation |
| UEPositioningAssistanceInfo | - | - | - |  |
| ULInformationTransfer | + | - | - |  |
| ULInformationTransferIRAT | NOTE 2 |  |  |  |
| ULInformationTransferMRDC | - | - | - |  |
| NOTE 1: This message type carries segments of other RRC messages. The protection of an instance of this message is the same as for the message which this message is carrying. NOTE 2: This message type carries others RRC messages. The protection of an instance of this message is the same as for the message which this message is carrying. |  |  |  |  |
<!-- /table -->

# B.2 Description of BWP configuration options

There are two possible ways to configure BWP\#0 (i.e. the initial BWP) for a UE:

1\) Configure *BWP-DownlinkCommon* and *BWP-UplinkCommon* in *ServingCellConfigCommon*, but do not configure dedicated configurations in *BWP-DownlinkDedicated* or *BWP-UplinkDedicated* in *ServingCellConfig*.

2\) Configure both *BWP-DownlinkCommon* and *BWP-UplinkCommon* in *ServingCellConfigCommon* and configure dedicated configurations in at least one of *BWP-DownlinkDedicated* or *BWP-UplinkDedicated* in *ServingCellConfig*.

The same way of configuration is used for UL BWP\#0 and DL BWP\#0 if both are configured.

With the first option (illustrated by figure B2-1 below), the BWP\#0 is not considered to be an RRC-configured BWP, i.e., UE only supporting one BWP can still be configured with BWP\#1 in addition to BWP\#0 when using this configuration. The BWP\#0 can still be used even if it does not have the dedicated configuration, albeit in a more limited manner since only the SIB1-defined configurations are available. For example, only DCI format 1\_0 can be used with BWP\#0 without dedicated configuration, so changing to another BWP requires RRCReconfiguration since DCI format 1\_0 doesn't support DCI-based switching.

Figure B2-1: BWP\#0 configuration without dedicated configuration

With the second option (illustrated by figure B2-2 below), the BWP\#0 is considered to be an RRC-configured BWP, i.e. UE only supporting one BWP cannot be configured with BWP\#1 in addition to BWP\#0 when using this configuration. However, UE supporting more than one BWP can still switch to and from BWP\#0 e.g. via DCI normally, and there are no explicit limitations to using the BWP\#0 (compared to the first option).

Figure B2-2: BWP\#0 configuration with dedicated configuration

For BWP\#0, the *BWP-DownlinkCommon* and *BWP-UplinkCommon* in *ServingCellConfigCommon* should match the parameters configured by MIB and SIB1 (if provided) in the corresponding serving cell.

If a RedCap-specific initial UL/DL BWP is configured, for BWP switching, the BWP \#0 always maps to the RedCap-specific initial UL/DL BWP.
