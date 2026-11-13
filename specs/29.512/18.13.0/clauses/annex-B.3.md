# B.3 Service Operation

## B.3.1 Introduction

This clause defines the specific service operations for the 5GC and EPC interworking scenario. In addition, the service operations defined in clause 4.2 shall be applicable.

NOTE: For brevity reason, the combined SMF and PGW-C is denoted as SMF in what follows.

## B.3.2 Npcf_SMPolicyControl_Create Service Operation

### B.3.2.0 General

When the UE establishes the PDN connection through the EPC network and the SMF+PGW-C receives the Create Session Request message as defined in 3GPP TS 29.274 \[37\], the SMF+PGW-C shall behave as defined in clause 4.2.2.2 with the differences that the SMF+PGW-C shall include (if available) in SmPolicyContextData data structure:

\- the IMSI of the user within the "supi" attribute;

\- the MSISDN of the user within the "gpsi" attribute;

\- APN within the "dnn" attribute;

\- PDU Session Id determined by the SMF+PGW-C within "pduSessionId" attribute for a UE that has an EPS subscription that allows 5GC interworking but does not support 5GC NAS.

NOTE 1: For a PDN connection established via the MME or ePDG, the PDU Session ID value is assigned from a reserved range as specified in Table 5.4.2-1 of 3GPP TS 29.571 \[11\]. The PDU session ID value assigned at PDN connection establishment remains unchanged along the PDN connection, i.e., it does not change when the UE handovers between EPS and EPC/ePDG. In the scenarios where UE handover between EPS and EPC/ePDG is enabled, to ensure uniqueness of the assigned PDU Session ID value, the SMF+PGW-C can retrieve from UDM the already assigned PDU Session ID values, allocate a non-colliding PDU Session ID value, and register in UDM the allocated PDU session ID;

\- PDN Type within the "pduSessionType" attribute;

\- IMEI-SV within the "pei" attribute;

\- IP-CAN type within the "accessType" attribute;

\- RAT type within the "ratType" attribute;

NOTE 2: See Annex B.3.2.2 for further information.

\- subscribed APN-AMBR within "subsSessAmbr" attribute;

\- subscribed Default EPS bearer QoS within "subsDefQos" attribute;

NOTE 3: Subscribed APN-AMBR and the QCI within the subscribed default EPS bearer QoS are mapped to subscribed Session-AMBR and 5QI as defined in Annex B.3.6.1 respectively.

\- user location information within the "userLocationInfo" attribute;

NOTE 4: See Annex B.3.2.1 for further information.

\- the S-NSSAI determined by the SMF+PGW-C within the "sliceInfo" attribute;

\- the bearer usage required of the default bearer within the "qosFlowUsage" attribute;

\- the UE time zone information within "ueTimeZone" attribute, if available.

NOTE 5: The UE time zone is not available in EPC untrusted WLAN.

When the UE establishes the PDN connection in an 5GS-EPC interworking deployment, the SMF+PGW-C shall behave as defined in clause 4.2.2.2 (access through 5GS network) or this clause (access through the EPC network) and additionally, if the feature "PackFiltAllocPrecedence" is supported and there is a possibility to run into a restriction regarding the number of TFT packet filters that can be allocated when interworking with EPS with N26 is supported (see clause 4.11.1 of TS 23.502 \[3\]), the PCF may provide, as part of the PccRule data type(s) for the PCC Rules to be installed, the "packFiltAllPrec" attribute to indicate the order of the PCC Rules in the allocation of TFT packet filter(s) by the SMF+PGW-C.

NOTE 6: PCF can know that interworking with EPS with N26 is supported based on the received DNN and S-NSSAI of the PDU Session.

When the UE establishes a PDU session in a 5GS-EPC interworking deployment, and the feature "EpsUrsp" defined in clause 5.8 is supported by both, the PCF and the SMF+PGW-C:

1\. to identify the 5GS to EPS mobility scenario, the PCF shall subscribe to RAT Type changes with the SMF+PGW-C in the SM Policy Association establishment response, if not previously subscribed, using an existing PDU session with "EpsUrsp" feature support; and

2\. to enable the UE to determine (when attached in EPC) whether UE STATE INDICATION message may need to be sent to the network using the UE requested bearer resource modification procedure, the SMF+PGW-C, if the UE included the URSP provisioning in EPS support indication in the PDU Session Establishment Request, shall provide to the UE the indication of URSP Provisioning Support in EPS in the PDU Session Establishment Accept message as defined in 3GPP TS 24.501 \[20\].

### B.3.2.1 UE Location related information

When the UE establishes the PDN connection through the EPC/E-UTRAN network, the SMF+PGW-C shall include, if available, the following user location information:

\- user location information within the "eutraLocation" attribute included in the "userLocationInfo" attribute; and

\- S-GW address, if available, within the "anGwAddr" attribute included in the "servNfId" attribute.

When the UE establishes the PDN connection through the EPC/UTRAN network and the feature "2G3GIWK" is supported, the SMF+PGW-C shall include, if available, the following user location information:

\- user location information within the "utraLocationInfo" attribute included in the "userLocationInfo" attribute; and

\- SGSN address, if available, within the "sgsnAddr" attribute included in the "servNfId" attribute.

When the UE establishes the PDN connection through the EPC/GERAN network and the feature "2G3GIWK" is supported, the SMF+PGW-C shall include, if available, the following user location information:

\- user location information within the "geraLocationInfo" attribute included in the "userLocationInfo" attribute; and

\- SGSN address, if available, within the "sgsnAddr" attribute included in the "servNfId" attribute.

When the UE establishes the PDN connection through the EPC/ePDG network, the SMF+PGW-C shall include, if available, the following user location information:

\- user location information within the "n3gaLocation" attribute included in the "userLocationInfo" attribute. The "n3gaLocation" attribute includes the "ueIpv4Addr" or "ueIpv6Addr" attributes, and, if available the "portNumber" and "protocol" attributes and, if the feature "WLAN_Location" is supported, the "twapId" attribute encoding the WLAN location information, if available; and

\- ePDG identification within the "anGwAddr" attribute included in the "servNfId" attribute.

NOTE: The "n3gaLocation" attribute does not include the "n3gppTai" and "n3IwfId" attributes in EPC interworking scenarios.

### B.3.2.2 Access Type related information

When the UE establishes the PDN connection through the EPC/E-UTRAN network, the SMF+PGW shall include, if available, the following access type information:

\- the "3GPP_ACCESS" value within the "accessType" attribute; and

\- the "EUTRA" value within the "ratType" attribute.

When the UE establishes the PDN connection through the EPC/UTRAN network and the feature "2G3GIWK" is supported, the SMF+PGW shall include, if available, the following access type information:

\- the "3GPP_ACCESS" value within the "accessType" attribute; and

\- the "UTRA" value within the "ratType" attribute.

When the UE establishes the PDN connection through the EPC/GERAN network and the feature "2G3GIWK" is supported, the SMF+PGW shall include, if available, the following access type information:

\- the "3GPP_ACCESS" value within the "accessType" attribute; and

\- the "GERA" value within the "ratType" attribute.

When the UE establishes the PDN connection through the EPC/ePDG network, the SMF+PGW shall include, if available, the following access type information:

\- the "NON_3GPP_ACCESS" value within the "accessType" attribute;

\- the "WLAN" or "VIRTUAL" value within the "ratType" attribute, as applicable; and

\- the ePDG address in the "servNfId" attribute within the "anGwAddr" attribute.

### B.3.2.3 Access Network Charging Identifier report

During PDU session establishment procedure, the SMF+PGW-C may provide the Access Network Charging Identifier for the PDU session (i.e., for the default QoS flow or the default EPS bearer) as specified in clause 4.2.2.11, or may provide the Access Network Charging Identifier for the default EPS bearer and indicate that there is a separate access network charging identifier for each EPS bearer/QoS flow by omitting or setting to false the "sessionChScope" attribute.

In both cases above, the Access Network Charging Identifier value and the address of the network entity performing the charging are provided as specified in clause 4.2.2.11.

NOTE: During the PDU Session Establishment procedure, when there are different charging identifiers for each EPS bearer (or QoS flow), the "refPccRuleIds" attribute is not provided within the AccNetChId data structure, since the PCC Rules are not yet authorized at this stage.

## B.3.3 Npcf_SMPolicyControl_UpdateNotify Service Operation

### B.3.3.0 General

When the UE has an established PDN connection through the EPC/E-UTRAN network and the PCF provisions the policy to the SMF+PGW-C as defined in clause 4.2.3. The SMF+ PGW-C shall behave as defined in clause 4.2.3 with the differences that the SMF+PGW-C shall map the QoS information within the PCC rule and/or session rule into EPS QoS information as defined in Annex B.3.6.1.

When the UE has an established PDN connection in an 5GS-EPC interworking deployment, the SMF+PGW-C shall behave as defined in clause 4.2.3 (access through the 5GS network) or this clause (access through the EPC network) and additionally, if the feature "PackFiltAllocPrecedence" is supported and there is a possibility to run into a restriction regarding the number of TFT packet filters that can be allocated when interworking with EPS with N26 is supported as described in Annex B.3.2.0, the PCF may provide, as part of the PccRule data type for the new PCC Rules to be installed, the "packFiltAllPrec" attribute to indicate the order of the PCC Rules in the allocation of TFT packet filter(s) by the SMF+PGW-C.

### B.3.3.1 Policy Update When UE suspends

If the PolicyUpdateWhenUESuspends feature as defined in clause 5.8 is supported the PCF and the SMF shall comply with the procedures specified in this clause. During PDU session/PDN connection establishment or modification procedure, the PCF shall subscribe to the "UE_STATUS_RESUME" policy control request trigger if not subscribed yet, as described in clause 4.2.6.4. When the SMF receives the policy decision from the PCF as defined in clause 4.2.3.1 for a PDN connection maintained when the UE's status is suspend state, the SMF shall reject the request and include an HTTP "400 Bad Request" status code together with an ErrorReport structure. Within the ErrorReport data structure, the SMF shall include the "error" attribute containing the "cause" attribute of the ProblemDetails data structure set to "UE_STATUS_SUSPEND" which indicates the failure to enforce the corresponding policy decision, except if the policy decision is for the PCC rule removal only and/or session rule removal only, and further include the information as follows:

\- If the policy decision includes the installation of one or more PCC rules, the SMF shall invoke the procedure as defined in clause 4.2.3.16 with the "failureCode" attribute set to "UE_STA_SUSP" and "ruleStatus" attribute set to INACTIVE to indicate the failure to enforce those PCC rules.

\- If the policy decision includes the modification of one or more PCC rules, the SMF shall invoke the procedure as defined in clause 4.2.3.16 with the "failureCode" attribute set to "UE_STA_SUSP" and "ruleStatus" attribute set to ACTIVE to indicate the failure to enforce those PCC rules.

\- If the policy decision includes the modification of one or more session rules, the SMF shall within a RuleReport data structure include the "sessRuleReports" attribute. Within each SessionRuleReport data structure, the SMF shall include the affected session rules within the "ruleIds" attribute(s), the "sessRuleFailureCode" attribute set to "UE_STA_SUSP" and "ruleStatus" attribute set to ACTIVE to indicate the failure to enforce those session rules.

Upon reception of the "failureCode" attribute and/or "sessRuleFailureCode" attribute set to "UE_STA_SUSP" or the ProblemDetails data structure set to "UE_STATUS_SUSPEND", the PCF shall not initiate any PDU Session Modification procedure, except if it is initiated for the PCC rule removal only or the session rule removal only, for the given PDU session over N7 until the UE's status is resumed. When the SMF detected the UE's status is resumed from suspend state, the SMF shall inform the PCF of the UE status as defined in Annex B.3.4.2.

### B.3.3.2 Request report of EPS Fallback

When the "EPSFallbackReport" feature is supported, if the AF requests the PCF to report the EPS fallback for voice media type as described in clauses 4.2.2.30 or 4.2.3.29 of 3GPP TS 29.514 \[17\] or in clause E.3 of 3GPP TS 29.214 \[18\], the PCF shall perform the PCC rule provisioning procedure as defined in clause 4.2.6.2.1 and additionally provide the request of EPS fallback report to the SMF as follows:

\- it shall include the "lastReqRuleData" attribute to contain the "reqData" attribute with the value "EPS_FALLBACK" and the "refPccRuleIds" attribute to contain the related installed/modified PCC rule identifier(s) with 5QI=1.

\- it shall provide the "EPS_FALLBACK" policy control request rigger within the "policyCtrlReqTriggers" attribute, if not provided before.

### B.3.3.3 S-GW Restoration Support

If the SGWRest feature as defined in clause 5.8 is supported, the PCF and the SMF shall comply with the procedures specified in this clause. During PDU session/PDN connection establishment or modification procedure, the PCF shall subscribe to the "SCNN_CH" policy control request trigger if not subscribed yet, as described in clause 4.2.6.4.

When the SMF+PGW receives the policy decision from the PCF as defined in clause 4.2.3.1 for a PDN connection maintained during a S-GW failure, the SMF+PGW shall act as follows:

\- For MME/S4-SGSN triggered S-GW Restoration scenarios:

\- the SMF+PGW shall reject the request and include an HTTP "400 Bad Request" status code together with an ErrorReport structure. Within the ErrorReport data structure, the SMF shall include the "error" attribute containing the "cause" attribute of the ProblemDetails data structure set to "AN_GW_FAILED" which indicates the failure to enforce the corresponding policy decision, except if the policy decision is for the PCC rule removal only and/or session rule removal only, and further include the information as follows:

\- If the policy decision is related to one or more PCC rules, the SMF+PGW shall behave as defined in clause 4.2.3.16 with the "failureCode" attribute set to "AN_GW_FAILE".

\- If the policy decision is related to one or more session rules, the SMF+PGW shall behave as defined in clause 4.2.3.20 with the "sessRuleFailureCode" attribute set to "AN_GW_FAILED".

\- For SMF+PGW triggered S-GW Restoration scenarios, the SMF+PGW shall accept the procedure as per normal procedures. In the case, the PDN connection is not restored during an operator configured time period, the SMF+PGW shall behave as follows as defined in annex B.3.4.9.

Upon reception of the "cause" attribute of the ProblemDetails data structure set to "AN_GW_FAILED" or the "failureCode" attribute set to "AN_GW_FAILE" and/or the "sessRuleFailureCode" attribute set to "AN_GW_FAILED", the PCF shall not initiate any SM Policy association modification procedure, except if the I SM Policy association modification procedure is initiated for the PCC rule removal only, for the given SM Policy association over N7 until the S-GW has recovered.

The SMF+PGW shall maintain the PDN connections affected by the S-GW failure and eligible for restoration for an operator configurable time period. Upon expiry of that time period, the SMF+PGW shall release the PDN connection and inform the PCF about the SM Policy association termination as specified in clause 4.2.5.2.

The SMF+PGW should maintain the GBR bearers of the PDN connections eligible for restoration for an operator configurable time period. Upon expiry of that time period, the SMF+PGW shall release GBR bearers that have not yet been restored and inform the PCF about the PCC rule removal as specified in clause 4.2.4.7.

The SMF+PGW shall discard downlink packets received for a PDN connection maintained during a S-GW failure that has not yet been restored.

The SMF+PGW shall delete the PDN connection locally when it receives an SM Policy association termination from the PCF as described in clause 4.2.4.3.

### B.3.3.4 Request of Access Network Charging Identifier

When the PCF received from the SMF+PGW-C the indication that the Access Network Charging Identifier is different per EPS bearer/QoS flow (see clause B.3.2.3), or the Access Network Charging identifier is unknown for an AF session to the PCF, and the PCF received from the AF the request of access network information as specified in 3GPP TS 29.514 \[17\] or 3GPP TS 29.214 \[18\], the PCF shall request the access network charging identifier associated to the dynamic PCC rulesas specified in clause 4.2.6.5.1.

### B.3.3.5 Forwarding of UE policy container and/or PCRT(s) for URSP provisioning in EPS

The PCF may receive a UE policy container and/or policy control request trigger(s) from the PCF for the UE during the lifetime of the PDU session and forward it to the SMF+PGW-C by invoking the procedure defined in clause 4.2.3.2.

If the feature "EpsUrsp" is supported, the PCF selects the SM Policy association of the PDN connection used for the delivery of UE policy container(s) and policy control request trigger(s) as described in 3GPP TS 29.525 \[57\] and invokes the Npcf_SMPolicyControl_UpdateNotify request to provide to the SMF+PGW-C via the SmPolicyDecision structure:

\- the updated policy control request trigger(s), if available. and, if not previously provided, the RAT Type change policy control request trigger (to identify EPS to 5GS mobility); and

\- transparently, the received UE policy container within the "uePolCont" attribute.

## B.3.4 Npcf_SMPolicyControl_Update Service Operation

### B.3.4.0 General

When the established PDN connection through the EPC/E-UTRAN network is modified and SMF+PGW-C receives Modify Bearer Request, Modify Bearer or Delete Bearer Command message and if the SMF detects the policy control request trigger(s) is met or the error(s) needs to be reported or when the UE handed over from the 5GS to the EPS and the SMF detects the policy control request trigger(s) is met, the SMF+PGW-C shall behave as defined in clause 4.2.4.2 with the differences that the SMF+PGW-C shall include (if available) in the SmPolicyUpdateContextData data structure:

\- IP-CAN type within the "accessType" attribute;

\- RAT type within the "ratType" attribute;

NOTE 1: See Annex B.3.4.5 for further information.

\- subscribed APN-AMBR within the "subsSessAmbr" attribute;

\- subscribed Default EPS bearer QoS Information within the "subsDefQos" attribute;

NOTE 2: Subscribed APN-AMBR and the QCI within the subscribed default EPS bearer QoS are mapped to subscribed Session-AMBR and 5QI as defined in Annex B.3.6.1 respectively.

\- the bearer usage required for the dedicated bearer within the "qosFlowUsage" attribute if the UE initiates a resource modification request procedure and the bearer usage request was present in the Bearer Resource Command;

\- user location information of EPC within the "userLocationInfo" attribute; and

NOTE 3: See Annex B.3.4.3 for further information.

\- UE policy container within "uePolCont" attribute, if available.

The policy control request trigger "RES_MO_RE" is not supported when the PDN connection is established through the EPC/E-UTRAN network. The SMF+PGW shall reject the PDU session modification that initiated the UE's resource modification.

During interworking from 5GS to EPS, if the feature "PackFiltAllocPrecedence" is supported, for QoS Flows without EPS bearer ID(s) assigned or for QoS Flows related to PCC Rules that do not have allocated TFT packet filters, the SMF+PGW-C shall delete those PCC Rules and inform the PCF. The SMF+PGW-C shall include the "ruleReports" attribute containing the RuleReport data instance which specifies the affected PCC rules within the "pccRuleIds" attribute, set to "INACTIVE" the value within the "ruleStatus" attribute and the "PACKET_FILTER_TFT_ALLOCATION_EXCEEDED" as the value of the "failureCode" attribute.

If the feature "PackFiltAllocPrecedence" is supported, the PCF may provide, as part of the PccRule data type for the new PCC Rules to be installed the "packFiltAllPrec" attribute to indicate the order of the PCC Rules in the allocation of TFT packet filter(s) by the SMF+PGW-C. The PCF may include this parameter if the feature "PackFiltAllocPrecedence" is supported and there is a possibility to run into a restriction regarding the number of TFT packet filters that can be allocated for the PDU Session and interworking with EPS with N26 deployment is supported as described in Annex B.3.2.0.

### B.3.4.1 Number of Supported Packet Filters Report

When the UE handed over from the EPC/E-UTRAN to the 5GS and the number of supported packet filters for signalled QoS rules is received from the UE, the SMF shall include the "NUM_OF_PACKET_FILTER" within the "repPolicyCtrlReqTriggers" attribute and the number of supported packet filters for signalled QoS rules within the "numOfPackFilter". In this case, the PCF shall behave as defined in clause 4.2.6.2.16.

NOTE: The maximum number of packet filters sent to the UE per QoS rule is additionally limited as specified in 3GPP TS 24.501 \[20\] when the UE is camping in 5GS.

### B.3.4.2 Policy Update When UE suspends

#### B.3.4.2.1 Policy Update Error Report

If the PolicyUpdateWhenUESuspends feature as defined in clause 5.8 is supported, the PCF and the SMF shall comply with the procedures specified in this clause. During PDU session/PDN connection establishment or modification procedure, the PCF shall subscribe to the "UE_STATUS_RESUME" policy control request trigger if not subscribed yet, as described in clause 4.2.6.4. When the SMF receives the policy decision from the PCF as defined in clause 4.2.4.1 for a PDN connection maintained when the UE's status is suspend state, the SMF shall include the "ruleReports" attribute for the affected PCC rules and/or session rules to report the failure within the SmPolicyUpdateContextData data structure. Within the RuleReport data structure, the SMF shall include the "failureCode" attribute set to "UE_STA_SUSP" which indicates the failure to enforce the corresponding policy decision, except if the policy decision is for the PCC rule removal only and/or session rule removal only, and further include the information as follows:

\- if the policy decision includes the modification of one or more session rules, within an RuleReport instance, the SMF shall include the "sessRuleReports" attribute. Within each SessionRuleReport data structure, the SMF shall include the affected session rules within the "ruleIds" attribute, the "sessRuleFailureCode" attribute set to "UE_STA_SUSP" and the "ruleStatus" attribute set to ACTIVE to indicate the failure to enforce those session rules.

\- if the policy decision includes the installation of one or more PCC rules, the SMF shall invoke the procedure as defined in clause 4.2.4.15 with the "failureCode" attribute set to "UE_STA_SUSP" and "ruleStatus" attribute set to INACTIVE to indicate the failure to enforce those PCC rules.

\- if the policy decision includes the modification of one or more PCC rules, the SMF shall invoke the procedure as defined in clause 4.2.4.15 with the "failureCode" attribute set to "UE_STA_SUSP" and "ruleStatus" attribute set to ACTIVE to indicate the failure to enforce those PCC rules.

Upon reception of the "failureCode" attribute and/or "sessRuleFailureCode" attribute set to "UE_STA_SUSP", the PCF shall not initiate any PDU Session Modification procedure, except if it is initiated for the PCC rule removal only and/or session rule removal only, for the given PDU session over N7 until the UE's status is resumed.

#### B.3.4.2.2 UE State Change Report

If the SMF detected the UE's status is resumed from suspend state, the SMF shall inform the PCF of the UE status including the "UE_STATUS_RESUME" within "repPolicyCtrlReqTriggers" attribute. The PCF shall after this update the SMF with PCC Rules or session rules if necessary.

### B.3.4.3 UE Location related information

When the UE handed over from the EPC/GERAN or EPC/UTRAN and the feature "2G3GIWK" is supported, or 5GS to EPC/E-UTRAN the SMF+PGW-C shall include, together with the policy control request triggers met, the following user location information:

\- If the "SAREA_CH" or "SCELL_CH" policy control request trigger is provisioned and met, the user location information within the "eutraLocation" attribute included in the "userLocationInfo" attribute.

\- If the "SCNN_CH" policy control request trigger is provisioned and met, the "servNfId" attribute including the S-GW identification within the "anGwAddr" attribute.

\- If the "AN_INFO" policy control request trigger is met, the user location was requested by the PCF and provided to the SMF+PGW-C, the SMF shall provide the user location information within the "eutraLocation" attribute included in the "userLocationInfo" attribute and the time when it was last known in the 3GPP access within "userLocationInfoTime" attribute (if available).

When the UE handed over from the EPC/E-UTRAN to the EPC/GERAN or EPC/UTRAN and the feature "2G3GIWK" is supported the SMF+PGW-C shall include, together with the policy control request triggers met, the following user location information:

\- If the "SAREA_CH" or "SCELL_CH" policy control request trigger is provisioned and met, the user location information within the "geraLocation" attribute or "utraLocation" attribute included in the "userLocationInfo" attribute.

\- If the "SCNN_CH" policy control request trigger is provisioned and met, the "servNfId" attribute including the SGSN identification within the "sgsnAddr" attribute.

When the UE handed over from the 5GS to EPC non-3GPP access, the SMF+PGW-C shall include, together with the applicable provisioned policy control request triggers, the following user location information:

\- If the "SAREA_CH" policy control request trigger is provisioned and met, and the hand over is to EPC untrusted non-3GPP access, the user location information within the "n3gaLocation" attribute included in the "userLocationInfo" attribute as specified in clause B.3.2.1.

\- If the "SCNN_CH" policy control request trigger is provisioned and met, the ePDG identification within the "anGwAddr" attribute included in the "servNfId" attribute.

\- If the "AN_INFO" policy control request trigger is met, the user location was requested by the PCF and provided to the SMF+PGW-C, the SMF shall provide the user location information within the "n3gaLocation" attribute included in the "userLocationInfo" attribute and the time when it was last known in the non-3GPP access within "userLocationInfoTime" attribute (if available). The "n3gaLocation" attribute includes the "ueIpv4Addr" or "ueIpv6Addr" attributes, and, if available the "portNumber" and "protocol" attributes and, if the feature "WLAN_Location" is supported, the "twapId" attribute encoding the WLAN location information, if available.

NOTE 1: The "n3gaLocation" attribute does not include the "n3gppTai" and "n3IwfId" attributes in EPC interworking scenarios.

NOTE 2: SCELL_CH policy control request trigger is not supported in EPC Non-3GPP access. The PCF will not receive user location information related to this trigger in this case.

### B.3.4.4 Presence Reporting Area Information Report

When the UE is connected through the EPC/E-UTRAN network, the SMF+PGW-C receives the presence reporting area information as defined in 3GPP TS 29.274 \[37\]. When the PRA or ePRA feature is supported, the SMF+PGW-C provides presence reporting area to the PCF as specified in clause 4.2.4.16.

If the SMF+PGW-C receives from the MME presence reporting information corresponding to the Set of Core Network predefined Presence Reporting Areas, and the individual presence reporting area as specified in 3GPP TS 29.274 \[37\], the SMF+PGW shall only provide the PCF with the individual presence reporting area within the "praId" attribute of the PresenceInfo data type.

### B.3.4.5 Access Type related information

The SMF+PGW shall include, when the policy control request trigger "AC_TY_CH" is met, the following access type information:

\- If after handover the new access type is EPC/E-UTRAN:

a\) the "3GPP_ACCESS" value within the "accessType" attribute; and

b\) the "EUTRA" value within the "ratType" attribute.

\- If after handover the new access type is EPC/UTRAN and the feature "2G3GIWK" is supported:

a\) the "3GPP_ACCESS" value within the "accessType" attribute; and

b\) the "UTRA" value within the "ratType" attribute.

\- If after handover the new access type is EPC/GERAN and the feature "2G3GIWK" is supported:

a\) the "3GPP_ACCESS" value within the "accessType" attribute; and

b\) the "GERA" value within the "ratType" attribute.

\- If after handover the new access type is EPC/ePDG:

a\) the "NON_3GPP_ACCESS" value within the "accessType" attribute;

b\) the "WLAN" or "VIRTUAL" value within the "ratType" attribute, as applicable; and

c\) the ePDG address in the "servNfId" attribute within the "anGwAddr" attribute.

NOTE 1: In the interworking scenario, "AC_TY_CH" is met when the UE handed over from the 5GC/N3IWF or 5GC/TNAN/TWAN to the EPC/E-UTRAN, or when the UE handed over from the 5GS to the EPC/ePDG.

The SMF+PGW shall include, when the policy control request trigger "RAT_TY_CH" is met, the following RAT type information:

\- If after handover the new RAT type is the E-UTRA, the "EUTRA" value within the "ratType" attribute.

\- If after handover the new RAT type is the WLAN, the "WLAN" or "VIRTUAL" value within the "ratType" attribute, as applicable.

NOTE 2: In the interworking scenario, "RAT_TY_CH" is met when the UE handed over from the NR to the E-UTRA or when the UE handed over from the NR to the WLAN (untrusted) and from E-UTRA to WLAN (trusted/untrusted) or from E-UTRA to N3GA.

### B.3.4.6 Report of EPS Fallback

When the "EPSFallbackReport" feature is supported, if the "policyCtrlReqTriggers" attribute with the value "EPS_FALLBACK" has been provided to the SMF, the SMF shall notify to the PCF of EPS fallback when a PCC rule referred from the "lastReqRuleData" attribute required the EPS fallback report within the "reqData" attribute.

When the SMF received a PDU session modification response from the access network indicating the establishment of the QoS flow with 5QI=1 is rejected due to EPS fallback, the SMF shall within the SmPolicyUpdateContextData data structure include:

\- the "EPS_FALLBACK" value within the "repPolicyCtrlReqTriggers" attribute; and

\- the affected PCC rules within the "pccRuleIds" attribute included in the "ruleReports" attribute, where the "ruleStatus" attribute is set to ACTIVE.

The PCF shall identify the AF session that requested the voice media type that triggered the EPS fallback and shall notify the AF as described in clauses 4.2.5.15 of 3GPP TS 29.514 \[17\] or in clause E.3 of 3GPP TS 29.214 \[18\].

### B.3.4.7 MA PDU Session

If the UE or the network does not support MA PDU Session with 3GPP access connected to EPC, when the UE handed over from the EPC/E-UTRAN to the 5GS and the MA PDU Request Indication or MA PDU Network-Upgrade Allowed Indication and ATSSS Capability are received from the UE, if the "ATSSS" feature defined in clause 5.8 is supported, the SMF shall include the "MA_PDU" within the "repPolicyCtrlReqTriggers" attribute, and, as defined in clause 4.2.2.17, the SMF shall include the MA PDU session Indication within the "maPduInd" attribute and the ATSSS capability of the MA PDU session within the "atsssCapab" attribute. In this case, the PCF shall behave as defined in clause 4.2.2.17.

NOTE: If the UE and the network support MA PDU Sessions with 3GPP access connected to EPC, the MA PDU Session can be simultaneously associated with user-plane resources on 3GPP access network connected to EPC and with non-3GPP access network connected to 5GC as specified in clause B.3.6.4.

### B.3.4.8 EPS RAN NAS Cause Support

If the RAN-NAS-Cause feature as defined in clause 5.8 is supported, and the PDN connection is established through the EPC network, the SMF shall report the RAN/NAS release cause(s) as specified in clauses 4.2.4.7, 4.2.4.12 and 4.2.4.15, with the exception that the received EPS RAN/NAS cause(s) are encoded within the "epsCause" attribute included in the RanNasRelCause data type. In this Release of the specification, the EPS release cause code information may include RAN/NAS release cause(s), a TWAN release cause or an untrusted WLAN release cause.

### B.3.4.9 S-GW Restoration Support

If the SGWRest feature as defined in clause 5.8 is supported, the PCF and the SMF shall comply with the procedures specified in this clause. During PDU session/PDN connection establishment or modification procedure, the PCF shall subscribe to the "SCNN_CH" policy control request trigger if not subscribed yet, as described in clause 4.2.6.4.

When the SMF+PGW receives the policy decision from the PCF as defined in clause 4.2.4.1 or for a PDN connection maintained during a S-GW failure for a policy decision received as defined in clause 4.2.3.1 or 4.2.4.1, the SMF+PGW shall act as follows:

\- For MME/S4-SGSN triggered S-GW Restoration scenarios:

\- When the SMF receives the policy decision from the PCF as defined in clause 4.2.4.1 for a PDN connection maintained during a S-GW failure, the SMF shall include the "ruleReports" attribute for the affected PCC rules and/or the "sessRuleReports" attribute for the affected session rules to report the failure within the SmPolicyUpdateContextData data structure and further include the information as follows.

\- if the policy decision is related to one or more PCC rules, the SMF+PGW shall behave as defined in clause 4.2.4.15 with the "failureCode" attribute set to set to "AN_GW_FAILE".

\- if the policy decision is related to one or more session rules the SMF+PGW shall behave as defined in clause 4.2.4.21 with the "sessRuleFailureCode" attribute set to "AN_GW_FAILED".

\- For SMF+PGW triggered S-GW Restoration scenarios, if the SMF+PGW has accepted the procedure as per normal procedures but the PDN connection is not restored during an operator configured time period, the SMF+PGW shall behave as follows when the related timer expires:

\- if the policy decision is related to the PCC rule(s), the SMF+PGW shall behave as defined in clause 4.2.4.15 with the "failureCode" attribute set to "RESOURCE_ALLOCATION_FAILURE"

\- if the policy decision is related to the session rule(s), and the "SessQoSModEnforcementFailure" feature is not supported the SMF+PGW shall behave as defined in clause 4.2.4.21 with the "sessRuleFailureCode" attribute set to "SESSION_RESOURCE_ALLOCATION_FAILURE". If the "SessQoSModEnforcementFailure" feature is supported, the "sessRuleFailureCode" attribute shall be set to "DEFAULT_QOS_MODIFICATION_FAILURE" or "SESSION_AMBR_MODIFICATION_FAILURE" based on the failure to enforce the corresponding policy decision.

For MME/S4-SGSN triggered S-GW Restoration scenarios, while the S-GW restoration is in progress, if the SMF+PGW sends a request towards the PCF that is triggered by a different event (e.g. internal event at SMF+PGW), the SMF+PGW shall include the "anGwStatus" attribute set to "true".

Upon reception of the "failureCode" attribute set to "AN_GW_FAILED" and/or the "sessRuleFailureCode" attribute set to "AN_GW_FAILED" or the "anGwStatus" attribute set to "true", the PCF shall not initiate any SM Policy association modification procedure, except if the SM Policy association modification procedure is initiated for the PCC rule removal only, for the given SM Policy association over N7 until the S-GW has recovered.

If the SMF+PGW indicated "AN_GW_FAILED" and/or "AN_GW_FAILE" previously according to the procedures described above or in annex B.3.3.3, the SMF+PGW shall inform the PCF when the S-GW has recovered by including "repPolicyCtrlReqTriggers" attribute set to the "SCNN_CH" and the "servNfId" attribute including the S-GW identification within the "anGwAddr" attribute related to the restored or new S-GW. The PCF may after this update the SMF+PGW if necessary.

NOTE 1: The PCF could reject requests from the AF and UDR when the "cause" attribute of the ProblemDetails data structure set to "AN_GW_FAILED", the "failureCode" attribute set to "AN_GW_FAILE" and/or the "sessRuleFailureCode" attribute set to "AN_GW_FAILED" or the "anGwStatus" attribute set to "true" is received until the "repPolicyCtrlReqTriggers" attribute set to the "SCNN_CH" is received.

The SMF+PGW shall maintain the PDN connections affected by the S-GW failure and eligible for restoration for an operator configurable time period. Upon expiry of that time period, the SMF+PGW shall release the PDN connection and inform the PCF about the SM Policy association termination as specified in clause 4.2.5.2.

NOTE 2: The PCF is not aware of which PDN connections are eligible for restoration. When the SMF+PGW detects a S-GW failure, the SMF+PGW requests the PCF to terminate SM Policy associations associated to PDN connections affected by the S-GW failure and not eligible for restoration.

The SMF+PGW should maintain the GBR bearers of the PDN connections eligible for restoration for an operator configurable time period. Upon expiry of that time period, the SMF+PGW shall release GBR bearers that have not yet been restored and inform the PCF about the PCC rule removal as specified in clause 4.2.4.7.

The SMF+PGW shall discard downlink packets received for a PDN connection maintained during a S-GW failure that has not yet been restored.

The SMF+PGW shall delete the PDN connection locally when it receives an SM Policy association termination from the PCF as described in clause 4.2.4.3.

### B.3.4.10 UE initiates a resource modification support

In the case that the UE initiates a resource allocation procedure as defined in clause 6.5.3 or UE initiates a resource modification procedure as defined in clause 6.5.4 of 3GPP 3GPP TS 24.301 \[52\], the SMF+PGW shall within the SmPolicyUpdateContextData data structure include the "RES_MO_RE" within the "repPolicyCtrlReqTriggers" attribute and shall include the UE request of specific QoS handling for selected SDF within the "ueInitResReq" attribute. Within the UeInitiatedResourceRequest data structure, the SMF+PGW shall include the "ruleOp" attribute, "packFiltInfo" attribute and "reqQos" attribute if applicable as follows:

\- When the UE requests to "Create new TFT", the SMF+PGW shall include the "ruleOp" attribute set to "CREATE_PCC_RULE", the "packFiltInfo" attribute and "reqQos" attribute containing the requested QoS for the new PCC rule. Each PacketFilterInfo instance shall contain one packet filter provided by the UE. If the PCF authorizes the request, the PCF shall create a new PCC rule by including the new packet filters within the service data flow template of the PCC rule.

\- When the UE requests to "Add packet filters to existing TFT", SMF+PGW shall include the "ruleOp" attribute set to "MODIFY_PCC_RULE_AND_ADD_PACKET_FILTERS", the "pccRuleId" attribute including the PCC rule identifier corresponding the packet filter identifier provided by the UE and the "packFiltInfo" attribute. Each PacketFilterInfo instance shall contain one packet filter requested for addition. If the UE request includes the modified QoS information the SMF+PGW shall also include the "reqQos" attribute to indicate the updated QoS for the affected PCC rule(s). If the PCF authorizes the request, the PCF shall update the PCC rule by adding the new packet filters to the service data flow template of the PCC rule.

\- When the UE requests to "Replace packet filters in existing TFT", SMF+PGW shall include the "ruleOp" attribute set to "MODIFY\_ PCC_RULE_AND_REPLACE_PACKET_FILTERS", the "pccRuleId" attribute including the PCC rule identifier corresponding the packet filter identifier provided by the UE and the "packFiltInfo" attribute. Each PacketFilterInfo instance shall within the "packFiltId" attribute include the replaced packet filter identifier assigned by the PCF corresponding to the packet filter identifier received from the UE and one packet filter requested for addition. If the UE request includes the modified QoS information the SMF+PGW shall also include the "reqQos" attribute to indicate the updated QoS for the affected PCC rule. If the PCF authorizes the request, the PCF shall update PCC rule by replacing the existing packet filter with the new packet filter within the service data flow template of the PCC rule.

\- When the UE requests to "Delete packet filters from existing TFT", SMF+PGW shall include the "ruleOp" attribute set to "MODIFY\_ PCC_RULE_AND_DELETE_PACKET_FILTERS", the "pccRuleId" attribute including the PCC rule identifier corresponding the paceket filter identifier provided by the UE and the "packFiltInfo" attribute. Each PacketFilterInfo instance shall within the "packFiltId" attribute include the removed packet filter identifier assigned by the PCF corresponding to the packet filter identifier received from the UE. If the UE request includes modified QoS information the SMF+PGW shall also include the "reqQos" attribute to indicate the updated QoS for the affected PCC rule(s). If the PCF authorizes the request, the PCF shall update PCC rule by removing the corresponding packet filters from the service data flow template of the PCC rule.

\- When the UE requests to "No TFT operation", SMF+PGW shall include the "ruleOp" attribute set to "MODIFY_PCC_RULE_WITHOUT_MODIFY_PACKET_FILTERS", the "pccRuleId" attribute including the PCC rule identifier corresponding the paceket filter identifier provided by the UE and the modified QoS information within the "reqQos" attribute.

\- When the UE requests to "Delete existing TFT", the SMF+PGW shall include the "ruleOp" attribute set to "DELETE_PCC_RULE", the "pccRuleId" attribute including the PCC rule identifier corresponding the packet filter identifier provided by the UE and the "packFiltInfo" attribute. The PCF shall remove the PCC rule when the PCF receives the request according to the PCC rule identifier.

NOTE 1: The UE can only modify or delete packet filters that the UE has introduced and associated resources. The packet filter identifiers contained in the FlowInformation data structure are only used for packet filters created by the UE.

The SMF+PGW shall calculate the requested GBR, for a GBR QCI, as the sum of the previously authorized GBR for the affected PCC rule, adjusted with the difference between the requested GBR for the EPS bearer and previously negotiated GBR for the EPS bearer. For the UE request to "Create new TFT", the GBR as requested by the UE for those filters shall be used.

If the request covers all the PCC rules with a bearer binding to the same bearer, then the SMF+PGW may request a change to the QCI for existing packet filters.

For the purpose of creating or modifying a packet filter, replacing and modifying packet filter, within the UeInitiatedResourceRequest instance, the SMF+PGW shall include the precedence information of the packet filter within the "precedence" attribute, and within each PacketFilterInfo instance, the SMF+PGW shall include the "packFiltCont" attribute, "tosTrafficClass" attribute, "spi" attribute, "flowLabel" attribute and "flowDirection" attribute set to the value(s) describing the packet filter provided by the UE.

NOTE 2: The UE signalling with the network is governed by the applicable NAS signalling TS. The NAS 3GPP TS for a specific access may restrict the UE possibilities to make requests compared to what is stated above.

If the PCF authorizes the request from the UE, the PCF shall construct a PCC rule(s) based on the UeInitiatedResourceRequest data structure. For "CREATE_PCC_RULE" or "MODIFY_PCC_RULE_AND_ADD_PACKET_FILTERS" operation, the PCF shall within the FlowInformation data structure include the assigned packet filter identifier within the "packFiltId" attribute. When the SMF+PGW derives the TFT based on the PCC rule, the SMF+PGW shall assign a new packet filter identifier for each added packet filter and keep the mapping between the packet filter identifier for the packet filter within the PCC rule and TFT sento the UE.

### B.3.4.11 Report of Access Charging Network Identifier

The report of the Access Network Charging Identifier(s) is as specified in clause 4.2.4.13, with the difference that when the SMF assigns an Access Network Charging Identifier per EPS bearer/QoS flow, the SMF shall additionally include, within each AccNetChId instance, all the PCC rule identifier(s) associated to the provided Access Network Charging Identifier within the "refPccRuleIds" attribute.

### B.3.4.11a Detection of the SM Policy Association enabling URSP provisioning in EPS

During UE Initial Attach with default PDN connection establishment in EPS, the UE and the SMF+PGW-C perform ePCO capability negotiation as defined in 3GPP TS 24.301 \[52\] to ensure that both, the network and the UE support URSP provisioning in EPS PCO. The SMF+PGW-C, when receives from the UE the Indication of URSP Provisioning Support in EPS PCO in the PDN connectivity request, and supports the feature "EpsUrsp" as defined in clause 5.8, the SMF+PGW-C shall select a PCF that supports the feature "EpsUrsp", shall create the SM Policy Association as described in clause B.3.2 and shall provide to the UE the Indication of URSP Provisioning Support in EPS PCO in the PDN Connectivity Accept message as defined in 3GPP TS 24.301 \[52\].

When the UE determines the URSP provisioning in EPS PCO is supported by the network, then the UE intiates the UE requested bearer modification procedure and includes the UE Policy Container ePCO, which will be further forwarded by the MME to the SMF+PGW-C. When the feature "EpsUrsp" is supported and the SMF+PGW-C receives the UE Policy Container ePCO, the SMF+PGW-C shall include the "UE_POL_CONT_IND" within the "repPolicyCtrlReqTriggers" attribute and shall forward transparently the UE Policy Container to the PCF for the PDU session within the "uePolCont" attribute. When the feature "EpsUrsp" is supported and the SMF+PGW-C receives the failure result for UE Policy Container delivery, the SMF+PGW-C shall include the "UE_POL_CONT_IND" within the "repPolicyCtrlReqTriggers" attribute and shall forward transparently the appropriate failure delivery report to the PCF for the PDU session within the "uePolFailReport" attribute.

The PCF for the PDU session then detects that the SM Policy Association enables the URSP provisioning in EPS and establishes a UE Policy Association with the PCF for the UE as described in 3GPP TS 29.525 \[57\] to transparently forward the received UE policy container. The PCF for the PDU session shall subscribe to RAT Type and/or Access-Type changes if not previously subscribed.

To detect the 5GS to EPS handover or 5GS to EPS Idle Mode mobility (both referred as 5GS to EPS mobility with N26 in the present document) and if the "EpsUrsp" feature described in clause 5.8 is supported, the PCF for the PDU session shall subscribe to RAT Type and/or Access Type changes, if not previously subscribed. During 5GS to EPS mobility with N26, and if the "EpsUrsp" feature described in clause 5.8 is supported, the PCF for the PDU session associated with the SMF+PGW-C serving the PDN connection(s) determines whether 5GS to EPS mobility applies based on the received RAT and/or Access-Type change event. When the reported RAT and Access-Type change event indicates the UE is moving from 5GS to EPS, the PCF for the PDU session then determines that the SM Policy Association(s) enables the URSP provisioning in EPS and establishes a UE Policy Association with the PCF for the UE, if applicable, as described in 3GPP TS 29.525 \[57\].

### B.3.4.12 Reporting of UE Policy container for URSP provisioning in EPS

When the feature "EpsUrsp" is supported and a UE policy container is received from the UE in EPC over a PDN connection, the SMF+PGW-C requests to update the SM Policy Association and provides to the PCF the received UE policy container.

The Policy Control Request Trigger condition "UE_POL_CONT_IND" is met when the SMF+PGW-C receives a UE policy container from the UE or a failure delivery report. The SMF+PGW-C shall include the "UE_POL_CONT_IND" within the "repPolicyCtrlReqTriggers" attribute and shall transparently forward to the PCF the UE policy container encoded within the "uePolCont" attribute or the failure delivery report encoded within the "uePolFailReport" attribute. The PCF shall transparently forward the UE policy container to the PCF for the UE in Npcf_UEPolicyControl_Update/Create Request as described in 3GPP TS 29.525 \[57\].

### B.3.4.13 Reporting of the PCC rule(s) removal in EPS

If the SMF+PGW-C releases dedicated QoS Flows established in 5GS, and remove the PCC rule(s) associated with these QoS Flows when the UE is handed over from 5GC to EPC/GERAN or EPC/UTRAN as described in clause 5.17.2.4, 3GPP TS 23.502 \[3\], then the SMF shall inform the PCF about the removal of the affected PCC rule(s) as defined in clause 4.2.4.12, and may provide the "RES_ALLO_FAIL" as the value of the "failureCode" attribute.

## B.3.5 Npcf_SMPolicyControl_Delete Service Operation

### B.3.5.1 General

When the UE deletes the PDN connection through the EPC network and the SMF+PGW-C shall behave as defined in clause 4.2.5.2 with the difference that the SMF+PGW-C shall include the information elements contained in the Delete Session Request message within the SmPolicyDeleteData data structure.

NOTE: See Annex B.3.2.1 for location information.

### B.3.5.2 EPS RAN NAS Cause Support

If the RAN-NAS-Cause feature as defined in clause 5.8 is supported, and the PDN connection is established through the EPC network, the SMF shall report the RAN/NAS release cause(s) as specified in clause 4.2.5.4.7, with the exception that the received EPS RAN/NAS cause(s) are encoded within the "epsCause" attribute included in the RanNasRelCause data type. In this Release of the specification, the EPS release cause code information may include RAN/NAS release cause(s), a TWAN release cause or an untrusted WLAN release cause.

## B.3.6 Provisioning and Enforcement of Policy Decisions

### B.3.6.1 QoS mapping perfomed by the SMF+PGW-C

When the UE is served by the 5GC, during PDU Session establishment and GBR QoS flow establishment, SMF+ PGW-C performs EPS QoS mappings, from the 5G QoS parameters obtained from the PCF, and allocates TFT with the PCC rules obtained from the PCF. If a TFT is to be allocated for a downlink unidirectional EPS bearer mapped from a downlink only QoS Flow, the SMF+ PGW-C shall allocate a TFT packet filter that effectively disallows any useful uplink packet as described in clause 15.3.3.4 of 3GPP TS 23.060 \[26\]. The SMF+PGW-C sends the mapped QoS parameters and TFT to the UE via PCO.

When the UE is served by the EPC, during PDN Connection establishment and dedicated bearer establishment/modification, SMF+ PGW-C performs EPS QoS mappings, from the 5G QoS parameters obtained from the PCF, and allocates TFT with the PCC rules obtained from the PCF. Other 5G QoS parameters corresponding to the PDN connection, e.g. Session-AMBR, and QoS rules and QoS Flow level QoS parameters if needed for the QoS Flow(s) associated with the QoS rule(s), are sent to UE in PCO.

The SMF+PGW-C shall perform EPS QoS mappings as defined in clause 4.11.1.1 and Annex C in 3GPP TS 23.502 \[3\] as follows:

\- ignore the QNC and reflective QoS indication if received;

\- for standardized 5QIs, the authorized 5QI is one to one mapped to the QCI;

NOTE: The delay critical 5QI mapping to QCI is unspecified in the present specification.

\- for non-standardized 5QI,derive the authorized QCI based on the authorized 5QI and operator policy;

\- one to one map the subscribed default QCI to the subscribed default 5QI;

\- set the subscribed Session-AMBR according to operator policy (e.g. taking the value of subscribed APN-AMBR into account); and

\- set the authorized APN-AMBR according to operator policy (e.g. taking the value of authorized Session-AMBR into account).

When SMF+PGW-C is used for GERAN/UTRAN access during PDN Connection establishment, dedicated bearer establishment/modification and the feature "2G3GIWK" is supported, SMF+ PGW-C maps R99 QoS to/from EPS parameters as defined in Annex E of TS 23.401 \[58\]. The EPS and 5G QoS mapping is performed as defined in this clause.

### B.3.6.2 Provisioning of Presence Reporting Area Information

When the PRA or ePRA feature is supported, the PCF provides the SMF with Presence Reporting Area(s) information as specified in clause 4.2.6.5.6. When the UE is connected through the EPC/E-UTRAN network, the SMF+PGW-C initiates the appropriate PDN connection specific procedures specified in 3GPP TS 29.274 \[37\] to obtain or to deactivate the report of the presence state of a UE in a presence reporting area.

NOTE: Homogeneous support of Presence Area reporting in EPC and 5GC networks is assumed.

### B.3.6.3 Request and Report of Access Network information

If the NetLoc feature as defined in clause 5.8 is supported, the PCF may request the SMF+PGW-C to report the access network information as defined in clause 4.2.6.5.4.

If the AN_INFO policy control request trigger is set, upon receiving the "lastReqRuleData" attribute with the "reqData" attribute with the value(s) MS_TIME_ZONE and/or USER_LOC_INFO and the "refPccRuleIds" attribute containing the PCC rule identifier(s) corresponding to the PCC rule(s) being installed, modified or removed:

\- If the "reqData" attribute indicates MS_TIME_ZONE and USER_LOC_INFO and the SMF+PGW-C determines that the access network does not support the access network information reporting, the SMF+PGW-C shall immediately inform the PCF by including the "netLocAccSupp" attribute set to "ANR_NOT_SUPPORTED" value in the "UeCampingRep" data structure returned in the "200 OK" response to the policy update notification request.

\- If the "reqData" attribute only includes the MS_TIME_ZONE value and the SMF+PGW-C determines that the access network does not support the report of the UE time zone, the SMF+PGW-C shall immediately inform the PCF by including the "netLocAccSupp" attribute set to "TZR_NOT_SUPPORTED" value in the "UeCampingRep" data structure returned in the "200 OK" response to the policy update notification request.

\- If the "reqData" attribute only includes the USER_LOC_INFO value and the SMF+PGW-C determines that the access network does not support the report of the UE location, the SMF+PGW-C shall immediately inform the PCF by including the "netLocAccSupp" attribute set to "LOC_NOT_SUPPORTED" value in the "UeCampingRep" data structure returned in the "200 OK" response to the policy update notification request.

\- If the "reqData" attribute includes the USER_LOC_INFO value and the MS_TIME_ZONE value, and the SMF+PGW-C determines the access network supports the report of UE location and/or UE time zone, the SMF+PGW-C shall apply appropriate procedures to the EPC access network to obtain the requested and supported access network information and shall report the available information as specified in clause 4.2.4.9.

NOTE: The SMF+PGW determines whether the access network supports access network information reporting based on access type, RAT type and trusted/untrusted type of the access network.

When the request to report access network information occurs within an EPS Fallback for IMS voice procedure, the SMF shall delay the report of access network information till the handover to EPS has been completed, as specified in 3GPP TS 23.502 \[3\], clause 4.13.6.1.

### B.3.6.4 MA PDU sessions with connectivity over E-UTRAN/EPC and non-3GPP access to 5GC

If the "EnATSSS" feature defined in clause 5.8 is supported by both the SMF and the PCF, this scenario uses the Access Traffic Steering, Switching and Splitting functionality as described in clauses 4.2.2.17, 4.2.3.21, and 4.2.4.2 with the following specifics:

\- Multi access connectivity is provided using EUTRAN/EPC as 3GPP access and non-3GPP/5GC system as non-3GPP access.

\- The ATSSS rules are derived from PCC rules and provided from the PGW-C+SMF to the UE over the non-3GPP access in 5GC system.

\- When the UE requests a PDN connection in EPC indicating the association with a MA PDU session, the PDN connection may be handed over to 3GPP access in 5GC without affecting the ATSSS control.

### B.3.6.5 MA PDU sessions with connectivity over 5GC and non-3GPP access to EPC

If the "EnATSSS_v2" feature defined in clause 5.8 is supported by both the SMF and the PCF, this scenario uses the Access Traffic Steering, Switching and Splitting functionality as described in clauses 4.2.2.17, 4.2.3.21, and 4.2.4.2 with the following specifics:

\- Multi access connectivity is provided using 5GS as 3GPP access and ePDG/EPC system as non-3GPP access.

\- The ATSSS rules are derived from PCC rules and provided from the PGW-C+SMF to the UE over the 3GPP access in 5GC system. ATSSS rules may be provided to the UE via ePDG/EPC.

\- When the UE requests a PDU session in 5GS indicating the association with a MA PDU session, the PDU session may be handed over to 3GPP access in EPC without affecting the ATSSS control.

## B.3.7 Detection and handling of late arriving requests for interworking scenario

### B.3.7.1 Handling of requests which collide with an existing SM Policy Association

When the UE is served by the EPC and the SMF+PGW-C receives the origination time stamp from the originating entity (see clause 13.2 of 3GPP TS 29.274 \[37\]) during the PDN connection establishment, the SMF+PGW-C shall include the origination time stamp parameter within 3gpp-Sbi-Origination-Timestamp header in the HTTP POST request sent to the PCF, the PCF shall perform the behaviour as defined in clause 4.2.7.1.

### B.3.7.2 Detection and handling of requests which have timed out at the originating entity

When the UE is served by the EPC and the SMF+PGW-C receives the origination time stamp and the maximum wait time from the originating entity (see clause 13.3 of 3GPP TS 29.274 \[37\]), the SMF+PGW-C shall behave as defined in annex B.3.2 with the differences that the SMF+PGW-C:

\- shall include a 3gpp-Sbi-Sender-Timestamp header set to the value of the received origination time stamp;

\- shall include a 3gpp-Sbi-Max-Rsp-Time header set to the value of the received maximum wait time.

When the PCF receives the request from the SMF+PGW-C, the PCF shall behave as defined in clause 6.11.2 of 3GPP TS 29.500 \[4\].

######## Annex C (normative): Wireless and wireline convergence access support
