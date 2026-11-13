<img src="media/image2.png" style="width:1.77708in;height:1.03889in" />

#  

# Contents

Foreword [11](#foreword)

1 Scope [12](#scope)

2 References [12](#references)

3 Definitions, symbols and abbreviations [14](#definitions-symbols-and-abbreviations)

3.1 Definitions [14](#definitions)

3.2 Abbreviations [16](#abbreviations)

4 Npcf_SMPolicyControl Service [17](#npcf_smpolicycontrol-service)

4.1 Service Description [17](#service-description)

4.1.1 Overview [17](#overview)

4.1.2 Service Architecture [18](#service-architecture)

4.1.3 Network Functions [18](#network-functions)

4.1.3.1 Policy Control Function (PCF) [18](#policy-control-function-pcf)

4.1.3.2 NF Service Consumers [19](#nf-service-consumers)

4.1.4 Rules [20](#rules)

4.1.4.1 General [20](#general)

4.1.4.2 PCC rules [20](#pcc-rules)

4.1.4.2.1 PCC rules definition [20](#pcc-rules-definition)

4.1.4.2.2 PCC rules operation [24](#pcc-rules-operation)

4.1.4.3 Session rule [25](#session-rule)

4.1.4.3.1 Session rules definition [25](#session-rules-definition)

4.1.4.3.2 Session rules operation [25](#session-rules-operation)

4.1.4.4 Policy Decision types [25](#policy-decision-types)

4.1.4.4.1 General [25](#general-1)

4.1.4.4.2 Traffic control data definition [26](#traffic-control-data-definition)

4.1.4.4.3 QoS data definition [26](#qos-data-definition)

4.1.4.4.4 Charging data definition [27](#charging-data-definition)

4.1.4.4.5 UsageMonitoring data definition [28](#usagemonitoring-data-definition)

4.1.4.4.6 QoS Monitoring data definition [28](#qos-monitoring-data-definition)

4.1.5 Policy control request trigger [29](#policy-control-request-trigger)

4.1.6 Requested rule data [29](#requested-rule-data)

4.1.7 Requested usage data [29](#requested-usage-data)

4.1.8 Condition data [29](#condition-data)

4.2 Service Operations [30](#service-operations)

4.2.1 Introduction [30](#introduction)

4.2.2 Npcf_SMPolicyControl_Create Service Operation [30](#npcf_smpolicycontrol_create-service-operation)

4.2.2.1 General [30](#general-2)

4.2.2.2 SM Policy Association establishment [31](#sm-policy-association-establishment)

4.2.2.3 Provisioning of charging related information for PDU session [35](#provisioning-of-charging-related-information-for-pdu-session)

4.2.2.3.1 Provisioning of Charging Addresses [35](#provisioning-of-charging-addresses)

4.2.2.3.2 Provisioning of Default Charging Method [36](#provisioning-of-default-charging-method)

4.2.2.4 Provisioning of revalidation time [36](#provisioning-of-revalidation-time)

4.2.2.5 Policy provisioning and enforcement of authorized AMBR per PDU session [36](#policy-provisioning-and-enforcement-of-authorized-ambr-per-pdu-session)

4.2.2.6 Policy provisioning and enforcement of authorized default QoS [37](#policy-provisioning-and-enforcement-of-authorized-default-qos)

4.2.2.7 Provisioning of PCC rule for Application Detection and Control [37](#provisioning-of-pcc-rule-for-application-detection-and-control)

4.2.2.8 3GPP PS Data Off Support [38](#gpp-ps-data-off-support)

4.2.2.9 IMS Emergency Session Support [38](#ims-emergency-session-support)

4.2.2.10 Request Usage Monitoring Control [39](#request-usage-monitoring-control)

4.2.2.11 Access Network Charging Identifier report [39](#access-network-charging-identifier-report)

4.2.2.12 Request for the successful resource allocation notification [39](#request-for-the-successful-resource-allocation-notification)

4.2.2.13 Request of Presence Reporting Area Change Report [39](#request-of-presence-reporting-area-change-report)

4.2.2.14 Provisioning of IP Index Information [39](#provisioning-of-ip-index-information)

4.2.2.15 Negotiation of the QoS flow for IMS signalling [40](#negotiation-of-the-qos-flow-for-ims-signalling)

4.2.2.16 PCF resource cleanup [40](#pcf-resource-cleanup)

4.2.2.17 Access traffic steering, switching and splitting support [40](#access-traffic-steering-switching-and-splitting-support)

4.2.2.18 DNN Selection Mode Support [41](#dnn-selection-mode-support)

4.2.2.19 Detection of the SM Policy Association enabling Time Sensitive Communications, Time Synchronization and Deterministic Networking [42](#detection-of-the-sm-policy-association-enabling-time-sensitive-communications-time-synchronization-and-deterministic-networking)

4.2.2.20 Support of Dual Connectivity end to end redundant User Plane paths [42](#support-of-dual-connectivity-end-to-end-redundant-user-plane-paths)

4.2.2.21 User Plane Remote Provisioning of UE SNPN Credentials in Onboarding Network [42](#user-plane-remote-provisioning-of-ue-snpn-credentials-in-onboarding-network)

4.2.2.22 Network slice related data rate policy control [43](#network-slice-related-data-rate-policy-control)

4.2.2.23 Group related data rate policy control [43](#group-related-data-rate-policy-control)

4.2.2.24 Network slice usage control [43](#network-slice-usage-control)

4.2.2.25 VPLMN Specific Offloading Policy [43](#vplmn-specific-offloading-policy)

4.2.3 Npcf_SMPolicyControl_UpdateNotify Service Operation [44](#npcf_smpolicycontrol_updatenotify-service-operation)

4.2.3.1 General [44](#general-3)

4.2.3.2 SM Policy Association Update request [45](#sm-policy-association-update-request)

4.2.3.3 SM Policy Association termination request [47](#sm-policy-association-termination-request)

4.2.3.4 Provisioning of revalidation time [47](#provisioning-of-revalidation-time-1)

4.2.3.5 Policy provisioning and enforcement of authorized AMBR per PDU session [48](#policy-provisioning-and-enforcement-of-authorized-ambr-per-pdu-session-1)

4.2.3.6 Policy provisioning and enforcement of authorized default QoS [48](#policy-provisioning-and-enforcement-of-authorized-default-qos-1)

4.2.3.7 Provisioning of PCC rule for Application Detection and Control [48](#provisioning-of-pcc-rule-for-application-detection-and-control-1)

4.2.3.8 3GPP PS Data Off Support [48](#gpp-ps-data-off-support-1)

4.2.3.9 IMS Emergency Session Support [49](#ims-emergency-session-support-1)

4.2.3.9.1 Provisioning of PCC rule [49](#provisioning-of-pcc-rule)

4.2.3.9.2 Removal of PCC Rules for Emergency Services [49](#removal-of-pcc-rules-for-emergency-services)

4.2.3.10 Request of Access Network Information [50](#request-of-access-network-information)

4.2.3.11 Request Usage Monitoring Control [50](#request-usage-monitoring-control-1)

4.2.3.12 Ipv6 Multi-homing support [50](#ipv6-multi-homing-support)

4.2.3.13 Request for the result of PCC rule removal [50](#request-for-the-result-of-pcc-rule-removal)

4.2.3.14 Access Network Charging Identifier request [50](#access-network-charging-identifier-request)

4.2.3.15 Request for the successful resource allocation notification [50](#request-for-the-successful-resource-allocation-notification-1)

4.2.3.16 PCC Rule Error Report [50](#pcc-rule-error-report)

4.2.3.17 IMS Restoration Support [51](#ims-restoration-support)

4.2.3.18 P-CSCF Restoration Enhancement Support [51](#p-cscf-restoration-enhancement-support)

4.2.3.19 Request of Presence Reporting Area Change Report [51](#request-of-presence-reporting-area-change-report-1)

4.2.3.20 Session Rule Error Report [52](#session-rule-error-report)

4.2.3.21 Access traffic steering, switching and splitting support [52](#access-traffic-steering-switching-and-splitting-support-1)

4.2.3.22 Policy provisioning and enforcement of the AF session with required QoS [52](#policy-provisioning-and-enforcement-of-the-af-session-with-required-qos)

4.2.3.23 Forwarding of TSC user plane node management information and port management information received from the TSN AF or TSCTSF [53](#forwarding-of-tsc-user-plane-node-management-information-and-port-management-information-received-from-the-tsn-af-or-tsctsf)

4.2.3.24 Provisioning of TSCAI input information and TSC QoS related data [54](#provisioning-of-tscai-input-information-and-tsc-qos-related-data)

4.2.3.25 Policy provisioning of QoS Monitoring control [56](#policy-provisioning-of-qos-monitoring-control)

4.2.3.25.1 General [56](#general-4)

4.2.3.25.2 QoS Monitoring when dynamic Satellite Backhaul is used [59](#qos-monitoring-when-dynamic-satellite-backhaul-is-used)

4.2.3.26 Policy decision error handling [59](#policy-decision-error-handling)

4.2.3.26.1 Policy decision types and condition data error handling [59](#policy-decision-types-and-condition-data-error-handling)

4.2.3.26.2 Policy decision types, condition data and other policy decisions error handling [59](#policy-decision-types-condition-data-and-other-policy-decisions-error-handling)

4.2.3.27 Network slice related data rate policy control [60](#network-slice-related-data-rate-policy-control-1)

4.2.3.28 Group related data rate policy control [61](#group-related-data-rate-policy-control-1)

4.2.3.29 Policy provisioning of Periodicity and N6 Traffic Parameter to be measured [61](#policy-provisioning-of-periodicity-and-n6-traffic-parameter-to-be-measured)

4.2.3.30 Network slice usage control [61](#network-slice-usage-control-1)

4.2.3.31 VPLMN Specific Offloading Policy [61](#vplmn-specific-offloading-policy-1)

4.2.4 Npcf_SMPolicyControl_Update Service Operation [62](#npcf_smpolicycontrol_update-service-operation)

4.2.4.1 General [62](#general-5)

4.2.4.2 Requesting the update of the Session Management related policies [63](#requesting-the-update-of-the-session-management-related-policies)

4.2.4.3 Request the policy based on revalidation time [66](#request-the-policy-based-on-revalidation-time)

4.2.4.4 Policy provisioning and enforcement of authorized AMBR per PDU session [66](#policy-provisioning-and-enforcement-of-authorized-ambr-per-pdu-session-2)

4.2.4.5 Policy provisioning and enforcement of authorized default QoS [67](#policy-provisioning-and-enforcement-of-authorized-default-qos-2)

4.2.4.6 Application detection information reporting [67](#application-detection-information-reporting)

4.2.4.7 Indication of QoS Flow Termination Implications [68](#indication-of-qos-flow-termination-implications)

4.2.4.8 3GPP PS Data Off Support [69](#gpp-ps-data-off-support-2)

4.2.4.9 Request and Report of Access Network Information [70](#request-and-report-of-access-network-information)

4.2.4.10 Request Usage Monitoring Control and Reporting Accumulated Usage [70](#request-usage-monitoring-control-and-reporting-accumulated-usage)

4.2.4.10.1 General [70](#general-6)

4.2.4.10.2 PCC Rule Removal [71](#pcc-rule-removal)

4.2.4.11 Ipv6 Multi-homing support [72](#ipv6-multi-homing-support-1)

4.2.4.12 Request and report for the result of PCC rule removal [72](#request-and-report-for-the-result-of-pcc-rule-removal)

4.2.4.13 Access Network Charging Identifier request and report [73](#access-network-charging-identifier-request-and-report)

4.2.4.14 Request and report for the successful resource allocation notification [73](#request-and-report-for-the-successful-resource-allocation-notification)

4.2.4.15 PCC Rule Error Report [73](#pcc-rule-error-report-1)

4.2.4.16 Presence Reporting Area Information Report [74](#presence-reporting-area-information-report)

4.2.4.17 UE initiates a resource modification support [75](#ue-initiates-a-resource-modification-support)

4.2.4.18 Trace Control [76](#trace-control)

4.2.4.19 Negotiation of the QoS flow for IMS signalling [76](#negotiation-of-the-qos-flow-for-ims-signalling-1)

4.2.4.20 Notification about Service Data Flow QoS target enforcement [77](#notification-about-service-data-flow-qos-target-enforcement)

4.2.4.21 Session Rule Error Report [78](#session-rule-error-report-1)

4.2.4.22 Request the termination of SM Policy association [78](#request-the-termination-of-sm-policy-association)

4.2.4.23 Reporting of TSC user plane node management information and port management information [78](#reporting-of-tsc-user-plane-node-management-information-and-port-management-information)

4.2.4.24 Notification about Service Data Flow QoS Monitoring [79](#notification-about-service-data-flow-qos-monitoring)

4.2.4.25 Access traffic steering, switching and splitting support [80](#access-traffic-steering-switching-and-splitting-support-2)

4.2.4.26 Policy decision error handling [81](#policy-decision-error-handling-1)

4.2.4.26.1 Policy decision types and condition data error handling [81](#policy-decision-types-and-condition-data-error-handling-1)

4.2.4.26.2 Policy decision types, condition data and other policy decisions error handling [81](#policy-decision-types-condition-data-and-other-policy-decisions-error-handling-1)

4.2.4.27 Policy Control for DDN Events [81](#policy-control-for-ddn-events)

4.2.4.28 Network slice related data rate policy control [83](#network-slice-related-data-rate-policy-control-2)

4.2.4.29 Group related data rate policy control [83](#group-related-data-rate-policy-control-2)

4.2.4.30 Notification on network provided BAT Offset policy control trigger [83](#notification-on-network-provided-bat-offset-policy-control-trigger)

4.2.4.31 Network slice usage control [84](#network-slice-usage-control-2)

4.2.4.32 VPLMN Specific Offloading Policy [84](#vplmn-specific-offloading-policy-2)

4.2.5 Npcf_SMPolicyControl_Delete Service Operation [84](#npcf_smpolicycontrol_delete-service-operation)

4.2.5.1 General [84](#general-7)

4.2.5.2 SM Policy Association termination [85](#sm-policy-association-termination)

4.2.5.3 Report Accumulated Usage [86](#report-accumulated-usage)

4.2.5.4 Report Access Network Information [86](#report-access-network-information)

4.2.5.5 Void [86](#void)

4.2.5.6 Network slice related data rate policy control [86](#network-slice-related-data-rate-policy-control-3)

4.2.5.7 Group related data rate policy control [86](#group-related-data-rate-policy-control-3)

4.2.6 Provisioning and Enforcement of Policy Decisions [86](#provisioning-and-enforcement-of-policy-decisions)

4.2.6.1 General [86](#general-8)

4.2.6.2 PCC Rules [89](#pcc-rules-1)

4.2.6.2.1 Overview [89](#overview-1)

4.2.6.2.2 Gate Function [91](#gate-function)

4.2.6.2.3 Policy enforcement for authorized QoS per PCC Rule [91](#policy-enforcement-for-authorized-qos-per-pcc-rule)

4.2.6.2.4 Redirect Function [91](#redirect-function)

4.2.6.2.5 Usage Monitoring Control [92](#usage-monitoring-control)

4.2.6.2.6 Traffic Steering Control support [92](#traffic-steering-control-support)

4.2.6.2.7 Conditioned PCC rule [97](#conditioned-pcc-rule)

4.2.6.2.8 PCC rule for resource sharing [98](#pcc-rule-for-resource-sharing)

4.2.6.2.9 Resource reservation for services sharing priority [99](#resource-reservation-for-services-sharing-priority)

4.2.6.2.10 PCC rule bound to the default QoS flow [100](#pcc-rule-bound-to-the-default-qos-flow)

4.2.6.2.11 PCC rule for Application Detection and Control [101](#pcc-rule-for-application-detection-and-control)

4.2.6.2.12 Provisioning of PCC Rules for Multimedia Priority Services [101](#provisioning-of-pcc-rules-for-multimedia-priority-services)

4.2.6.2.13 Sponsored Data Connectivity [104](#sponsored-data-connectivity)

4.2.6.2.14 Support for PCC rule versioning [104](#support-for-pcc-rule-versioning)

4.2.6.2.15 Background data transfer support [105](#background-data-transfer-support)

4.2.6.2.16 Number of supported packet filter for signalled QoS rule limitation support [105](#number-of-supported-packet-filter-for-signalled-qos-rule-limitation-support)

4.2.6.2.17 Access traffic steering, switching and splitting support [106](#access-traffic-steering-switching-and-splitting-support-3)

4.2.6.2.18 Void [110](#void-1)

4.2.6.2.19 Provisioning of PCC Rules for Mission Critical Services [110](#provisioning-of-pcc-rules-for-mission-critical-services)

4.2.6.2.20 PCC rules authorization with preliminary service information [112](#pcc-rules-authorization-with-preliminary-service-information)

4.2.6.2.21 Policy Control for L4S [113](#policy-control-for-l4s)

4.2.6.2.22 UL/DL policy control based on Round-Trip latency requirements [114](#uldl-policy-control-based-on-round-trip-latency-requirements)

4.2.6.2.23 Policy Decision for AF requested QoS for a target UE or group of UE(s) not identified by UE address(es) [114](#policy-decision-for-af-requested-qos-for-a-target-ue-or-group-of-ues-not-identified-by-ue-addresses)

4.2.6.3 Session Rules [114](#session-rules)

4.2.6.3.1 Overview [114](#overview-2)

4.2.6.3.2 Conditioned Session rule [115](#conditioned-session-rule)

4.2.6.3.3 Provisioning of authorized default QoS [117](#provisioning-of-authorized-default-qos)

4.2.6.3.4 Access traffic steering, switching and splitting support [118](#access-traffic-steering-switching-and-splitting-support-4)

4.2.6.3.5 Usage Monitoring Control [118](#usage-monitoring-control-1)

4.2.6.4 Policy control request triggers [118](#policy-control-request-triggers)

4.2.6.5 Encoding of the request of information reporting [119](#encoding-of-the-request-of-information-reporting)

4.2.6.5.1 Request of Access Network Charging Identifier [119](#request-of-access-network-charging-identifier)

4.2.6.5.2 RAN NAS Cause Support [119](#ran-nas-cause-support)

4.2.6.5.3 Provisioning of the Usage Monitoring Control Policy [119](#provisioning-of-the-usage-monitoring-control-policy)

4.2.6.5.4 Request for Access Network Information [123](#request-for-access-network-information)

4.2.6.5.5 Request for the successful resource allocation notification [123](#request-for-the-successful-resource-allocation-notification-2)

4.2.6.5.6 Provisioning of Presence Reporting Area Information [123](#provisioning-of-presence-reporting-area-information)

4.2.6.5.7 Policy provisioning and enforcement of reflective QoS [124](#policy-provisioning-and-enforcement-of-reflective-qos)

4.2.6.6 Authorized QoS [125](#authorized-qos)

4.2.6.6.1 General [125](#general-13)

4.2.6.6.2 Policy provisioning and enforcement of authorized QoS per service data flow [126](#policy-provisioning-and-enforcement-of-authorized-qos-per-service-data-flow)

4.2.6.6.3 Policy provisioning and enforcement of authorized explicitly signalled QoS Characteristics [127](#policy-provisioning-and-enforcement-of-authorized-explicitly-signalled-qos-characteristics)

4.2.6.7 Monitoring the data rate per network slice for a UE [128](#monitoring-the-data-rate-per-network-slice-for-a-ue)

4.2.6.8 Network slice related data rate policy control [128](#network-slice-related-data-rate-policy-control-4)

4.2.6.8.1 General [128](#general-14)

4.2.6.8.2 PCF-based network slice data rate policy control by using QoS parameters [129](#pcf-based-network-slice-data-rate-policy-control-by-using-qos-parameters)

4.2.6.8.3 Network slice data rate policy control with assistance of the NWDAF [130](#network-slice-data-rate-policy-control-with-assistance-of-the-nwdaf)

4.2.6.9 Group related data rate policy control [131](#group-related-data-rate-policy-control-4)

4.2.6.9.1 General [131](#general-15)

4.2.6.10 Policy Provisioning for eXtended Reality and Interactive Media Services [132](#policy-provisioning-for-extended-reality-and-interactive-media-services)

4.2.6.10.1 Support for delivery of multi-modal services [132](#support-for-delivery-of-multi-modal-services)

4.2.6.10.2 Traffic Parameter Information and N6 Traffic Parameter Measurement [132](#traffic-parameter-information-and-n6-traffic-parameter-measurement)

4.2.6.10.3 PDU Set handling [132](#pdu-set-handling)

4.2.6.10.4 End of Data Burst Handling [132](#end-of-data-burst-handling)

4.2.7 Handling of requests which collide with an existing SM Policy Association [133](#handling-of-requests-which-collide-with-an-existing-sm-policy-association)

4.2.8 UE IP address support [133](#ue-ip-address-support)

5 Npcf_SMPolicyControl Service API [133](#npcf_smpolicycontrol-service-api)

5.1 Introduction [133](#introduction-1)

5.2 Usage of HTTP [134](#usage-of-http)

5.2.1 General [134](#general-16)

5.2.2 HTTP standard headers [134](#http-standard-headers)

5.2.2.1 General [134](#general-17)

5.2.2.2 Content type [134](#content-type)

5.2.3 HTTP custom headers [134](#http-custom-headers)

5.2.3.1 General [134](#general-18)

5.2.3.2 3gpp-Sbi-Origination-Timestamp [134](#gpp-sbi-origination-timestamp)

5.3 Resources [135](#resources)

5.3.1 Resource Structure [135](#resource-structure)

5.3.2 Resource: SM Policies [135](#resource-sm-policies)

5.3.2.1 Description [135](#description)

5.3.2.2 Resource definition [135](#resource-definition)

5.3.2.3 Resource Standard Methods [136](#resource-standard-methods)

5.3.2.3.1 POST [136](#post)

5.3.2.4 Resource Custom Operations [136](#resource-custom-operations)

5.3.3 Resource: Individual SM Policy [137](#resource-individual-sm-policy)

5.3.3.1 Description [137](#description-1)

5.3.3.2 Resource definition [137](#resource-definition-1)

5.3.3.3 Resource Standard Methods [137](#resource-standard-methods-1)

5.3.3.3.1 GET [137](#get)

5.3.3.4 Resource Custom Operations [138](#resource-custom-operations-1)

5.3.3.4.1 Overview [138](#overview-3)

5.3.3.4.2 Operation: delete [138](#operation-delete)

5.3.3.4.3 Operation: update [139](#operation-update)

5.4 Custom Operations without associated resources [140](#custom-operations-without-associated-resources)

5.5 Notifications [141](#notifications)

5.5.1 General [141](#general-19)

5.5.2 Policy Update Notification [141](#policy-update-notification)

5.5.2.1 Description [141](#description-4)

5.5.2.2 Operation Definition [141](#operation-definition-2)

5.5.3 Request for termination of the policy association [142](#request-for-termination-of-the-policy-association)

5.5.3.1 Description [142](#description-5)

5.5.3.2 Operation Definition [143](#operation-definition-3)

5.6 Data Model [143](#data-model)

5.6.1 General [143](#general-20)

5.6.2 Structured data types [151](#structured-data-types)

5.6.2.1 Introduction [151](#introduction-2)

5.6.2.2 Type SmPolicyControl [151](#type-smpolicycontrol)

5.6.2.3 Type SmPolicyContextData [152](#type-smpolicycontextdata)

5.6.2.4 Type SmPolicyDecision [155](#type-smpolicydecision)

5.6.2.5 Type SmPolicyNotification [158](#type-smpolicynotification)

5.6.2.6 Type PccRule [159](#type-pccrule)

5.6.2.7 Type SessionRule [162](#type-sessionrule)

5.6.2.8 Type QosData [163](#type-qosdata)

5.6.2.9 Type ConditionData [165](#type-conditiondata)

5.6.2.10 Type TrafficControlData [166](#type-trafficcontroldata)

5.6.2.11 Type ChargingData [168](#type-chargingdata)

5.6.2.12 Type UsageMonitoringData [170](#type-usagemonitoringdata)

5.6.2.13 Type RedirectInformation [171](#type-redirectinformation)

5.6.2.14 Type FlowInformation [172](#type-flowinformation)

5.6.2.15 Type SmPolicyDeleteData [173](#type-smpolicydeletedata)

5.6.2.16 Type QosCharacteristics [174](#type-qoscharacteristics)

5.6.2.17 Type ChargingInformation [175](#type-charginginformation)

5.6.2.18 Type AccuUsageReport [176](#type-accuusagereport)

5.6.2.19 Type SmPolicyUpdateContextData [177](#type-smpolicyupdatecontextdata)

5.6.2.20 Type UpPathChgEvent [181](#type-uppathchgevent)

5.6.2.21 Type TerminationNotification [181](#type-terminationnotification)

5.6.2.22 Type AppDetectionInfo [181](#type-appdetectioninfo)

5.6.2.23 Type AccNetChId [182](#type-accnetchid)

5.6.2.24 Type RequestedRuleData [182](#type-requestedruledata)

5.6.2.25 Type RequestedUsageData [183](#type-requestedusagedata)

5.6.2.26 Type UeCampingRep [184](#type-uecampingrep)

5.6.2.27 Type RuleReport [185](#type-rulereport)

5.6.2.28 Type RanNasRelCause [185](#type-rannasrelcause)

5.6.2.29 Type UeInitiatedResourceRequest [186](#type-ueinitiatedresourcerequest)

5.6.2.30 Type PacketFilterInfo [187](#type-packetfilterinfo)

5.6.2.31 Type RequestedQos [187](#type-requestedqos)

5.6.2.32 Type QosNotificationControlInfo [188](#type-qosnotificationcontrolinfo)

5.6.2.33 Type PartialSuccessReport [188](#type-partialsuccessreport)

5.6.2.34 Type AuthorizedDefaultQos [189](#type-authorizeddefaultqos)

5.6.2.35 Type AccNetChargingAddress [189](#type-accnetchargingaddress)

5.6.2.36 Type ErrorReport [190](#type-errorreport)

5.6.2.37 Type SessionRuleReport [190](#type-sessionrulereport)

5.6.2.38 Type ServingNfIdentity [190](#type-servingnfidentity)

5.6.2.39 Type SteeringMode [191](#type-steeringmode)

5.6.2.40 Type QosMonitoringData [192](#type-qosmonitoringdata)

5.6.2.41 Type TsnBridgeInfo [194](#type-tsnbridgeinfo)

5.6.2.42 Type QosMonitoringReport [195](#__RefHeading___Toc224641531)

5.6.2.43 Type AdditionalAccessInfo [195](#type-additionalaccessinfo)

5.6.2.44 Void [195](#void-2)

5.6.2.45 Type PortManagementContainer [195](#type-portmanagementcontainer)

5.6.2.46 Type IpMulticastAddressInfo [196](#type-ipmulticastaddressinfo)

5.6.2.47 Type BridgeManagementContainer [196](#type-bridgemanagementcontainer)

5.6.2.48 Type DownlinkDataNotificationControl [196](#type-downlinkdatanotificationcontrol)

5.6.2.49 Type DownlinkDataNotificationControlRm [196](#type-downlinkdatanotificationcontrolrm)

5.6.2.50 Type SgsnAddress [197](#type-sgsnaddress)

5.6.2.51 Void [197](#void-3)

5.6.2.52 Type ThresholdValue [197](#type-thresholdvalue)

5.6.2.53 Type NwdafData [197](#type-nwdafdata)

5.6.2.54 Type CallInfo [197](#type-callinfo)

5.6.2.55 Type CalleeInfo [198](#type-calleeinfo)

5.6.2.56 Type TrafficParaData [198](#type-trafficparadata)

5.6.2.57 Type L4sSupportInfo [199](#type-l4ssupportinfo)

5.6.2.58 Void [199](#void-4)

5.6.2.59 Type SliceUsgCtrlInfo [199](#type-sliceusgctrlinfo)

5.6.3 Simple data types and enumerations [199](#simple-data-types-and-enumerations)

5.6.3.1 Introduction [199](#introduction-3)

5.6.3.2 Simple data types [199](#simple-data-types)

5.6.3.3 Enumeration: FlowDirection [200](#enumeration-flowdirection)

5.6.3.4 Enumeration: ReportingLevel [200](#enumeration-reportinglevel)

5.6.3.5 Enumeration: MeteringMethod [201](#enumeration-meteringmethod)

5.6.3.6 Enumeration: PolicyControlRequestTrigger [202](#enumeration-policycontrolrequesttrigger)

5.6.3.7 Enumeration: RequestedRuleDataType [209](#enumeration-requestedruledatatype)

5.6.3.8 Enumeration: RuleStatus [209](#enumeration-rulestatus)

5.6.3.9 Enumeration: FailureCode [210](#enumeration-failurecode)

5.6.3.10 Enumeration: AfSigProtocol [212](#enumeration-afsigprotocol)

5.6.3.11 Enumeration: RuleOperation [212](#enumeration-ruleoperation)

5.6.3.12 Enumeration: RedirectAddressType [212](#enumeration-redirectaddresstype)

5.6.3.13 Enumeration: QosFlowUsage [213](#enumeration-qosflowusage)

5.6.3.14 Enumeration: FailureCause [213](#enumeration-failurecause)

5.6.3.15 Enumeration: FlowDirectionRm [213](#enumeration-flowdirectionrm)

5.6.3.16 Enumeration: CreditManagementStatus [213](#enumeration-creditmanagementstatus)

5.6.3.17 Enumeration: SessionRuleFailureCode [214](#enumeration-sessionrulefailurecode)

5.6.3.18 Enumeration: SteeringFunctionality [215](#enumeration-steeringfunctionality)

5.6.3.19 Enumeration: SteerModeValue [215](#enumeration-steermodevalue)

5.6.3.20 Enumeration: MulticastAccessControl [215](#enumeration-multicastaccesscontrol)

5.6.3.21 Enumeration RequestedQosMonitoringParameter [216](#enumeration-requestedqosmonitoringparameter)

5.6.3.22 Enumeration: ReportingFrequency [216](#enumeration-reportingfrequency)

5.6.3.23 Enumeration: SmPolicyAssociationReleaseCause [216](#enumeration-smpolicyassociationreleasecause)

5.6.3.24 Enumeration: PduSessionRelCause [216](#enumeration-pdusessionrelcause)

5.6.3.25 Enumeration: MaPduIndication [217](#enumeration-mapduindication)

5.6.3.26 Enumeration: AtsssCapability [218](#enumeration-atssscapability)

5.6.3.27 Enumeration: NetLocAccessSupport [219](#enumeration-netlocaccesssupport)

5.6.3.28 Enumeration: PolicyDecisionFailureCode [219](#enumeration-policydecisionfailurecode)

5.6.3.29 Enumeration: NotificationControlIndication [219](#enumeration-notificationcontrolindication)

5.6.3.31 Enumeration: SteerModeIndicator [219](#enumeration-steermodeindicator)

5.6.3.32 Enumeration TrafficParameterMeas [220](#enumeration-trafficparametermeas)

5.6.3.33 Enumeration: QosMonitoringParamType [220](#enumeration-qosmonitoringparamtype)

5.6.3.34 Enumeration TransportMode [220](#enumeration-transportmode)

5.7 Error handling [221](#error-handling)

5.7.1 General [221](#general-21)

5.7.2 Protocol Errors [221](#protocol-errors)

5.7.3 Application Errors [221](#application-errors)

5.8 Feature negotiation [225](#feature-negotiation)

5.9 Security [230](#security)

Annex A (normative): OpenAPI specification [232](#annex-a-normative-openapi-specification)

A.1 General [232](#a.1-general)

A.2 Npcf_SMPolicyControl API [232](#a.2-npcf_smpolicycontrol-api)

Annex B (normative): 5GC and EPC interworking scenario support [274](#annex-b-normative-5gc-and-epc-interworking-scenario-support)

B.1 Scope [274](#b.1-scope)

B.2 Npcf_SMPolicyControl Service [274](#b.2-npcf_smpolicycontrol-service)

B.2.1 Service Description [274](#b.2.1-service-description)

B.2.1.1 Overview [274](#b.2.1.1-overview)

B.2.1.2 Service Architecture [275](#b.2.1.2-service-architecture)

B.3 Service Operation [275](#b.3-service-operation)

B.3.1 Introduction [275](#b.3.1-introduction)

B.3.2 Npcf_SMPolicyControl_Create Service Operation [275](#b.3.2-npcf_smpolicycontrol_create-service-operation)

B.3.2.0 General [275](#b.3.2.0-general)

B.3.2.1 UE Location related information [277](#b.3.2.1-ue-location-related-information)

B.3.2.2 Access Type related information [277](#b.3.2.2-access-type-related-information)

B.3.2.3 Access Network Charging Identifier report [278](#b.3.2.3-access-network-charging-identifier-report)

B.3.3 Npcf_SMPolicyControl_UpdateNotify Service Operation [278](#b.3.3-npcf_smpolicycontrol_updatenotify-service-operation)

B.3.3.0 General [278](#b.3.3.0-general)

B.3.3.1 Policy Update When UE suspends [278](#b.3.3.1-policy-update-when-ue-suspends)

B.3.3.2 Request report of EPS Fallback [279](#b.3.3.2-request-report-of-eps-fallback)

B.3.3.3 S-GW Restoration Support [279](#b.3.3.3-s-gw-restoration-support)

B.3.3.4 Request of Access Network Charging Identifier [280](#b.3.3.4-request-of-access-network-charging-identifier)

B.3.3.5 Forwarding of UE policy container and/or PCRT(s) for URSP provisioning in EPS [280](#b.3.3.5-forwarding-of-ue-policy-container-andor-pcrts-for-ursp-provisioning-in-eps)

B.3.4 Npcf_SMPolicyControl_Update Service Operation [280](#b.3.4-npcf_smpolicycontrol_update-service-operation)

B.3.4.0 General [280](#b.3.4.0-general)

B.3.4.1 Number of Supported Packet Filters Report [281](#b.3.4.1-number-of-supported-packet-filters-report)

B.3.4.2 Policy Update When UE suspends [281](#b.3.4.2-policy-update-when-ue-suspends)

B.3.4.2.1 Policy Update Error Report [281](#b.3.4.2.1-policy-update-error-report)

B.3.4.2.2 UE State Change Report [282](#b.3.4.2.2-ue-state-change-report)

B.3.4.3 UE Location related information [282](#b.3.4.3-ue-location-related-information)

B.3.4.4 Presence Reporting Area Information Report [283](#b.3.4.4-presence-reporting-area-information-report)

B.3.4.5 Access Type related information [283](#b.3.4.5-access-type-related-information)

B.3.4.6 Report of EPS Fallback [283](#b.3.4.6-report-of-eps-fallback)

B.3.4.7 MA PDU Session [284](#b.3.4.7-ma-pdu-session)

B.3.4.8 EPS RAN NAS Cause Support [284](#b.3.4.8-eps-ran-nas-cause-support)

B.3.4.9 S-GW Restoration Support [284](#b.3.4.9-s-gw-restoration-support)

B.3.4.10 UE initiates a resource modification support [285](#b.3.4.10-ue-initiates-a-resource-modification-support)

B.3.4.11 Report of Access Charging Network Identifier [287](#b.3.4.11-report-of-access-charging-network-identifier)

B.3.4.11a Detection of the SM Policy Association enabling URSP provisioning in EPS [287](#b.3.4.11a-detection-of-the-sm-policy-association-enabling-ursp-provisioning-in-eps)

B.3.4.12 Reporting of UE Policy container for URSP provisioning in EPS [287](#b.3.4.12-reporting-of-ue-policy-container-for-ursp-provisioning-in-eps)

B.3.4.13 Reporting of the PCC rule(s) removal in EPS [287](#b.3.4.13-reporting-of-the-pcc-rules-removal-in-eps)

B.3.5 Npcf_SMPolicyControl_Delete Service Operation [288](#b.3.5-npcf_smpolicycontrol_delete-service-operation)

B.3.5.1 General [288](#b.3.5.1-general)

B.3.5.2 EPS RAN NAS Cause Support [288](#b.3.5.2-eps-ran-nas-cause-support)

B.3.6 Provisioning and Enforcement of Policy Decisions [288](#b.3.6-provisioning-and-enforcement-of-policy-decisions)

B.3.6.1 QoS mapping perfomed by the SMF+PGW-C [288](#b.3.6.1-qos-mapping-perfomed-by-the-smfpgw-c)

B.3.6.2 Provisioning of Presence Reporting Area Information [289](#b.3.6.2-provisioning-of-presence-reporting-area-information)

B.3.6.3 Request and Report of Access Network information [289](#b.3.6.3-request-and-report-of-access-network-information)

B.3.6.4 MA PDU sessions with connectivity over E-UTRAN/EPC and non-3GPP access to 5GC [289](#b.3.6.4-ma-pdu-sessions-with-connectivity-over-e-utranepc-and-non-3gpp-access-to-5gc)

B.3.6.5 MA PDU sessions with connectivity over 5GC and non-3GPP access to EPC [290](#b.3.6.5-ma-pdu-sessions-with-connectivity-over-5gc-and-non-3gpp-access-to-epc)

B.3.7 Detection and handling of late arriving requests for interworking scenario [290](#b.3.7-detection-and-handling-of-late-arriving-requests-for-interworking-scenario)

B.3.7.1 Handling of requests which collide with an existing SM Policy Association [290](#b.3.7.1-handling-of-requests-which-collide-with-an-existing-sm-policy-association)

B.3.7.2 Detection and handling of requests which have timed out at the originating entity [290](#b.3.7.2-detection-and-handling-of-requests-which-have-timed-out-at-the-originating-entity)

Annex C (normative): Wireless and wireline convergence access support [290](#annex-c-normative-wireless-and-wireline-convergence-access-support)

C.1 Scope [290](#c.1-scope)

C.2 Npcf_SMPolicyControl Service [291](#c.2-npcf_smpolicycontrol-service)

C.2.1 Service Description [291](#c.2.1-service-description)

C.2.1.1 Overview [291](#c.2.1.1-overview)

C.2.1.2 Service Architecture [291](#c.2.1.2-service-architecture)

C.2.1.3 Network Functions [291](#c.2.1.3-network-functions)

C.2.1.3.1 Policy Control Function (PCF) [291](#c.2.1.3.1-policy-control-function-pcf)

C.2.1.3.2 NF Service Consumers [291](#c.2.1.3.2-nf-service-consumers)

C.2.1.4 Rules [291](#c.2.1.4-rules)

C.2.1.4.1 PCC Rules [291](#c.2.1.4.1-pcc-rules)

C.2.1.4.2 Gate Function [291](#c.2.1.4.2-gate-function)

C.2.1.5 Policy control request trigger [291](#c.2.1.5-policy-control-request-trigger)

C.2.1.6 UE IP address support [292](#c.2.1.6-ue-ip-address-support)

C.3 Service Operation [293](#c.3-service-operation)

C.3.1 Introduction [293](#c.3.1-introduction)

C.3.2 Npcf_SMPolicyControl_Create Service Operation [293](#c.3.2-npcf_smpolicycontrol_create-service-operation)

C.3.2.1 General [293](#c.3.2.1-general)

C.3.2.2 IPTV service support [294](#c.3.2.2-iptv-service-support)

C.3.2.3 SNPN services support [294](#c.3.2.3-snpn-services-support)

C.3.3 Npcf_SMPolicyControl_UpdateNotify Service Operation [294](#c.3.3-npcf_smpolicycontrol_updatenotify-service-operation)

C.3.3.1 General [294](#c.3.3.1-general)

C.3.3.2 IPTV service support [294](#c.3.3.2-iptv-service-support)

C.3.4 Npcf_SMPolicyControl_Update Service Operation [294](#c.3.4-npcf_smpolicycontrol_update-service-operation)

C.3.4.1 General [294](#c.3.4.1-general)

C.3.4.2 IPTV service support [295](#c.3.4.2-iptv-service-support)

C.3.5 Npcf_SMPolicyControl_Delete Service Operation [295](#c.3.5-npcf_smpolicycontrol_delete-service-operation)

C.3.5.1 General [295](#c.3.5.1-general)

C.3.6 Provisioning and Enforcement of Policy Decisions [296](#c.3.6-provisioning-and-enforcement-of-policy-decisions)

C.3.6.0 General [296](#c.3.6.0-general)

C.3.6.1 IPTV service support [296](#c.3.6.1-iptv-service-support)

C.3.6.2 Hybrid Access support [297](#c.3.6.2-hybrid-access-support)

C.3.6.2.1 General [297](#c.3.6.2.1-general)

C.3.6.2.2 Hybrid Access with single PDU session [297](#c.3.6.2.2-hybrid-access-with-single-pdu-session)

C.3.6.2.3 Hybrid Access with MA PDU session connectivity over NG-RAN and wireline [297](#c.3.6.2.3-hybrid-access-with-ma-pdu-session-connectivity-over-ng-ran-and-wireline)

C.3.6.2.4 Hybrid Access with MA PDU session connectivity over EPC/E-UTRAN and wireline using EPC interworking scenarios [297](#c.3.6.2.4-hybrid-access-with-ma-pdu-session-connectivity-over-epce-utran-and-wireline-using-epc-interworking-scenarios)

Annex D(informative): Change history [299](#annex-dinformative-change-history)

# Foreword

This Technical Specification has been produced by the 3<sup>rd</sup> Generation Partnership Project (3GPP).

The contents of the present document are subject to continuing work within the TSG and may change following formal TSG approval. Should the TSG modify the contents of the present document, it will be re-released by the TSG with an identifying change of release date and an increase in version number as follows:

Version x.y.z

where:

x the first digit:

1 presented to TSG for information;

2 presented to TSG for approval;

3 or greater indicates TSG approved document under change control.

Y the second digit is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc.

z the third digit is incremented when editorial only changes have been incorporated in the document.
