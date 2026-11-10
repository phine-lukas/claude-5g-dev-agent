<img src="media/image1.jpeg" style="width:1.32569in;height:1.32569in" /><img src="media/image2.png" style="width:1.77708in;height:1.03889in" />

#  

# Contents

Foreword [13](#foreword)

1 Scope [14](#scope)

2 References [14](#references)

3 Definitions and abbreviations [15](#definitions-and-abbreviations)

3.1 Definitions [15](#definitions)

3.2 Abbreviations [16](#abbreviations)

4 General [16](#general)

4.1 Procedure Specification Principles [16](#procedure-specification-principles)

4.2 Forwards and Backwards Compatibility [17](#forwards-and-backwards-compatibility)

4.3 Specification Notations [17](#specification-notations)

5 NGAP Services [17](#ngap-services)

6 Services Expected from Signalling Transport [18](#services-expected-from-signalling-transport)

7 Functions of NGAP [18](#functions-of-ngap)

8 NGAP Procedures [18](#ngap-procedures)

8.1 List of NGAP Elementary Procedures [18](#list-of-ngap-elementary-procedures)

8.2 PDU Session Management Procedures [20](#pdu-session-management-procedures)

8.2.1 PDU Session Resource Setup [20](#pdu-session-resource-setup)

8.2.1.1 General [20](#general-1)

8.2.1.2 Successful Operation [21](#successful-operation)

8.2.1.3 Unsuccessful Operation [23](#unsuccessful-operation)

8.2.1.4 Abnormal Conditions [23](#abnormal-conditions)

8.2.2 PDU Session Resource Release [24](#pdu-session-resource-release)

8.2.2.1 General [24](#general-2)

8.2.2.2 Successful Operation [24](#successful-operation-1)

8.2.2.3 Unsuccessful Operation [25](#unsuccessful-operation-1)

8.2.2.4 Abnormal Conditions [25](#abnormal-conditions-1)

8.2.3 PDU Session Resource Modify [25](#pdu-session-resource-modify)

8.2.3.1 General [25](#general-3)

8.2.3.2 Successful Operation [25](#successful-operation-2)

8.2.3.3 Unsuccessful Operation [28](#unsuccessful-operation-2)

8.2.3.4 Abnormal Conditions [28](#abnormal-conditions-2)

8.2.4 PDU Session Resource Notify [28](#pdu-session-resource-notify)

8.2.4.1 General [28](#general-4)

8.2.4.2 Successful Operation [28](#successful-operation-3)

8.2.4.3 Abnormal Conditions [29](#abnormal-conditions-3)

8.2.5 PDU Session Resource Modify Indication [29](#pdu-session-resource-modify-indication)

8.2.5.1 General [29](#general-5)

8.2.5.2 Successful Operation [29](#successful-operation-4)

8.2.5.3 Unsuccessful Operation [30](#unsuccessful-operation-3)

8.2.5.4 Abnormal Conditions [30](#abnormal-conditions-4)

8.3 UE Context Management Procedures [31](#ue-context-management-procedures)

8.3.1 Initial Context Setup [31](#initial-context-setup)

8.3.1.1 General [31](#general-6)

8.3.1.2 Successful Operation [31](#successful-operation-5)

8.3.1.3 Unsuccessful Operation [33](#unsuccessful-operation-4)

8.3.1.4 Abnormal Conditions [33](#abnormal-conditions-5)

8.3.2 UE Context Release Request (NG-RAN node initiated) [33](#ue-context-release-request-ng-ran-node-initiated)

8.3.2.1 General [33](#general-7)

8.3.2.2 Successful Operation [34](#successful-operation-6)

8.3.2.3 Abnormal Conditions [34](#abnormal-conditions-6)

8.3.3 UE Context Release (AMF initiated) [34](#ue-context-release-amf-initiated)

8.3.3.1 General [34](#general-8)

8.3.3.2 Successful Operation [34](#successful-operation-7)

8.3.3.3 Unsuccessful Operation [35](#unsuccessful-operation-5)

8.3.3.4 Abnormal Conditions [35](#abnormal-conditions-7)

8.3.4 UE Context Modification [35](#ue-context-modification)

8.3.4.1 General [35](#general-9)

8.3.4.2 Successful Operation [35](#successful-operation-8)

8.3.4.3 Unsuccessful Operation [37](#unsuccessful-operation-6)

8.3.4.4 Abnormal Conditions [37](#abnormal-conditions-8)

8.3.5 RRC Inactive Transition Report [37](#rrc-inactive-transition-report)

8.3.5.1 General [37](#general-10)

8.3.5.2 Successful Operation [37](#successful-operation-9)

8.3.5.3 Abnormal Conditions [37](#abnormal-conditions-9)

8.4 UE Mobility Management Procedures [38](#ue-mobility-management-procedures)

8.4.1 Handover Preparation [38](#handover-preparation)

8.4.1.1 General [38](#general-11)

8.4.1.2 Successful Operation [38](#successful-operation-10)

8.4.1.3 Unsuccessful Operation [40](#unsuccessful-operation-7)

8.4.1.4 Abnormal Conditions [40](#abnormal-conditions-10)

8.4.2 Handover Resource Allocation [40](#handover-resource-allocation)

8.4.2.1 General [40](#general-12)

8.4.2.2 Successful Operation [40](#successful-operation-11)

8.4.2.3 Unsuccessful Operation [43](#unsuccessful-operation-8)

8.4.2.4 Abnormal Conditions [43](#abnormal-conditions-11)

8.4.3 Handover Notification [43](#handover-notification)

8.4.3.1 General [43](#general-13)

8.4.3.2 Successful Operation [44](#successful-operation-12)

8.4.3.3 Abnormal Conditions [44](#abnormal-conditions-12)

8.4.4 Path Switch Request [44](#path-switch-request)

8.4.4.1 General [44](#general-14)

8.4.4.2 Successful Operation [44](#successful-operation-13)

8.4.4.3 Unsuccessful Operation [46](#unsuccessful-operation-9)

8.4.4.4 Abnormal Conditions [46](#abnormal-conditions-13)

8.4.5 Handover Cancellation [46](#handover-cancellation)

8.4.5.1 General [46](#general-15)

8.4.5.2 Successful Operation [47](#successful-operation-14)

8.4.5.3 Unsuccessful Operation [47](#unsuccessful-operation-10)

8.4.5.4 Abnormal Conditions [47](#abnormal-conditions-14)

8.4.6 Uplink RAN Status Transfer [47](#uplink-ran-status-transfer)

8.4.6.1 General [47](#general-16)

8.4.6.2 Successful Operation [47](#successful-operation-15)

8.4.6.3 Abnormal Conditions [48](#abnormal-conditions-15)

8.4.7 Downlink RAN Status Transfer [48](#downlink-ran-status-transfer)

8.4.7.1 General [48](#general-17)

8.4.7.2 Successful Operation [48](#successful-operation-16)

8.4.7.3 Abnormal Conditions [48](#abnormal-conditions-16)

8.5 Paging Procedures [48](#paging-procedures)

8.5.1 Paging [48](#paging)

8.5.1.1 General [48](#general-18)

8.5.1.2 Successful Operation [49](#successful-operation-17)

8.5.1.3 Abnormal Conditions [49](#abnormal-conditions-17)

8.6 Transport of NAS Messages Procedures [49](#transport-of-nas-messages-procedures)

8.6.1 Initial UE Message [49](#initial-ue-message)

8.6.1.1 General [49](#general-19)

8.6.1.2 Successful Operation [50](#successful-operation-18)

8.6.1.3 Abnormal Conditions [50](#abnormal-conditions-18)

8.6.2 Downlink NAS Transport [50](#downlink-nas-transport)

8.6.2.1 General [50](#general-20)

8.6.2.2 Successful Operation [51](#successful-operation-19)

8.6.2.3 Abnormal Conditions [51](#abnormal-conditions-19)

8.6.3 Uplink NAS Transport [52](#uplink-nas-transport)

8.6.3.1 General [52](#general-21)

8.6.3.2 Successful Operation [52](#successful-operation-20)

8.6.3.3 Abnormal Conditions [52](#abnormal-conditions-20)

8.6.4 NAS Non Delivery Indication [52](#nas-non-delivery-indication)

8.6.4.1 General [52](#general-22)

8.6.4.2 Successful Operation [52](#successful-operation-21)

8.6.4.3 Abnormal Conditions [53](#abnormal-conditions-21)

8.6.5 Reroute NAS Request [53](#reroute-nas-request)

8.6.5.1 General [53](#general-23)

8.6.5.2 Successful Operation [53](#successful-operation-22)

8.6.5.3 Abnormal Conditions [53](#abnormal-conditions-22)

8.7 Interface Management Procedures [53](#interface-management-procedures)

8.7.1 NG Setup [53](#ng-setup)

8.7.1.1 General [53](#general-24)

8.7.1.2 Successful Operation [54](#successful-operation-23)

8.7.1.3 Unsuccessful Operation [54](#unsuccessful-operation-11)

8.7.1.4 Abnormal Conditions [54](#abnormal-conditions-23)

8.7.2 RAN Configuration Update [54](#ran-configuration-update)

8.7.2.1 General [54](#general-25)

8.7.2.2 Successful Operation [55](#successful-operation-24)

8.7.2.3 Unsuccessful Operation [55](#unsuccessful-operation-12)

8.7.2.4 Abnormal Conditions [56](#abnormal-conditions-24)

8.7.3 AMF Configuration Update [56](#amf-configuration-update)

8.7.3.1 General [56](#general-26)

8.7.3.2 Successful Operation [56](#successful-operation-25)

8.7.3.3 Unsuccessful Operation [57](#unsuccessful-operation-13)

8.7.3.4 Abnormal Conditions [57](#abnormal-conditions-25)

8.7.4 NG Reset [57](#ng-reset)

8.7.4.1 General [57](#general-27)

8.7.4.2 Successful Operation [58](#successful-operation-26)

8.7.4.2.1 NG Reset initiated by the AMF [58](#ng-reset-initiated-by-the-amf)

8.7.4.2.2 NG Reset initiated by the NG-RAN node [59](#ng-reset-initiated-by-the-ng-ran-node)

8.7.4.3 Unsuccessful Operation [59](#unsuccessful-operation-14)

8.7.4.4 Abnormal Conditions [59](#abnormal-conditions-26)

8.7.4.4.1 Abnormal Condition at the 5GC [59](#abnormal-condition-at-the-5gc)

8.7.4.4.2 Abnormal Condition at the NG-RAN [60](#abnormal-condition-at-the-ng-ran)

8.7.4.4.3 Crossing of NG RESET Messages [60](#crossing-of-ng-reset-messages)

8.7.5 Error Indication [60](#error-indication)

8.7.5.1 General [60](#general-28)

8.7.5.2 Successful Operation [60](#successful-operation-27)

8.7.5.3 Abnormal Conditions [61](#abnormal-conditions-27)

8.7.6 AMF Status Indication [61](#amf-status-indication)

8.7.6.1 General [61](#general-29)

8.7.6.2 Successful Operation [61](#successful-operation-28)

8.7.6.3 Abnormal Conditions [62](#abnormal-conditions-28)

8.7.7 Overload Start [62](#overload-start)

8.7.7.1 General [62](#general-30)

8.7.7.2 Successful Operation [62](#successful-operation-29)

8.7.7.3 Abnormal Conditions [63](#abnormal-conditions-29)

8.7.8 Overload Stop [63](#overload-stop)

8.7.8.1 General [63](#general-31)

8.7.8.2 Successful Operation [63](#successful-operation-30)

8.7.8.3 Abnormal Conditions [63](#abnormal-conditions-30)

8.8 Configuration Transfer Procedures [63](#configuration-transfer-procedures)

8.8.1 Uplink RAN Configuration Transfer [63](#uplink-ran-configuration-transfer)

8.8.1.1 General [63](#general-32)

8.8.1.2 Successful Operation [64](#successful-operation-31)

8.8.1.3 Abnormal Conditions [64](#abnormal-conditions-31)

8.8.2 Downlink RAN Configuration Transfer [64](#downlink-ran-configuration-transfer)

8.8.2.1 General [64](#general-33)

8.8.2.2 Successful Operation [64](#successful-operation-32)

8.8.2.3 Abnormal Conditions [65](#abnormal-conditions-32)

8.9 Warning Message Transmission Procedures [65](#warning-message-transmission-procedures)

8.9.1 Write-Replace Warning [65](#write-replace-warning)

8.9.1.1 General [65](#general-34)

8.9.1.2 Successful Operation [65](#successful-operation-33)

8.9.1.3 Unsuccessful Operation [66](#unsuccessful-operation-15)

8.9.1.4 Abnormal Conditions [66](#abnormal-conditions-33)

8.9.2 PWS Cancel [67](#pws-cancel)

8.9.2.1 General [67](#general-35)

8.9.2.2 Successful Operation [67](#successful-operation-34)

8.9.2.3 Unsuccessful Operation [67](#unsuccessful-operation-16)

8.9.2.4 Abnormal Conditions [67](#abnormal-conditions-34)

8.9.3 PWS Restart Indication [68](#pws-restart-indication)

8.9.3.1 General [68](#general-36)

8.9.3.2 Successful Operation [68](#successful-operation-35)

8.9.3.3 Abnormal Conditions [68](#abnormal-conditions-35)

8.9.4 PWS Failure Indication [68](#pws-failure-indication)

8.9.4.1 General [68](#general-37)

8.9.4.2 Successful Operation [68](#successful-operation-36)

8.9.4.3 Abnormal Conditions [69](#abnormal-conditions-36)

8.10 NRPPa Transport Procedures [69](#nrppa-transport-procedures)

8.10.1 General [69](#general-38)

8.10.2 Successful Operations [69](#successful-operations)

8.10.2.1 DOWNLINK UE ASSOCIATED NRPPA TRANSPORT [69](#downlink-ue-associated-nrppa-transport)

8.10.2.2 UPLINK UE ASSOCIATED NRPPA TRANSPORT [69](#uplink-ue-associated-nrppa-transport)

8.10.2.3 DOWNLINK NON UE ASSOCIATED NRPPA TRANSPORT [70](#downlink-non-ue-associated-nrppa-transport)

8.10.2.4 UPLINK NON UE ASSOCIATED NRPPA TRANSPORT [70](#uplink-non-ue-associated-nrppa-transport)

8.10.3 Unsuccessful Operations [70](#unsuccessful-operations)

8.10.4 Abnormal Conditions [70](#abnormal-conditions-37)

8.11 Trace Procedures [70](#trace-procedures)

8.11.1 Trace Start [70](#trace-start)

8.11.1.1 General [70](#general-39)

8.11.1.2 Successful Operation [71](#successful-operation-37)

8.11.1.3 Abnormal Conditions [71](#abnormal-conditions-38)

8.11.2 Trace Failure Indication [71](#trace-failure-indication)

8.11.2.1 General [71](#general-40)

8.11.2.2 Successful Operation [71](#successful-operation-38)

8.11.2.3 Abnormal Conditions [71](#abnormal-conditions-39)

8.11.3 Deactivate Trace [72](#deactivate-trace)

8.11.3.1 General [72](#general-41)

8.11.3.2 Successful Operation [72](#successful-operation-39)

8.11.3.3 Abnormal Conditions [72](#abnormal-conditions-40)

8.11.4 Cell Traffic Trace [72](#cell-traffic-trace)

8.11.4.1 General [72](#general-42)

8.11.4.2 Successful Operation [72](#successful-operation-40)

8.11.4.3 Abnormal Conditions [73](#abnormal-conditions-41)

8.12 Location Reporting Procedures [73](#location-reporting-procedures)

8.12.1 Location Reporting Control [73](#location-reporting-control)

8.12.1.1 General [73](#general-43)

8.12.1.2 Successful Operation [73](#successful-operation-41)

8.12.1.3 Abnormal Conditions [74](#abnormal-conditions-42)

8.12.2 Location Reporting Failure Indication [74](#location-reporting-failure-indication)

8.12.2.1 General [74](#general-44)

8.12.2.2 Successful Operation [74](#successful-operation-42)

8.12.2.3 Abnormal Conditions [74](#abnormal-conditions-43)

8.12.3 Location Report [74](#location-report)

8.12.3.1 General [74](#general-45)

8.12.3.2 Successful Operation [74](#successful-operation-43)

8.12.3.3 Abnormal Conditions [75](#abnormal-conditions-44)

8.13 UE TNLA Binding Procedures [75](#ue-tnla-binding-procedures)

8.13.1 UE TNLA Binding Release [75](#ue-tnla-binding-release)

8.13.1.1 General [75](#general-46)

8.13.1.2 Successful Operation [75](#successful-operation-44)

8.13.1.3 Abnormal Conditions [75](#abnormal-conditions-45)

8.14 UE Radio Capability Management Procedures [75](#ue-radio-capability-management-procedures)

8.14.1 UE Radio Capability Info Indication [75](#ue-radio-capability-info-indication)

8.14.1.1 General [75](#general-47)

8.14.1.2 Successful Operation [76](#successful-operation-45)

8.14.1.3 Abnormal Conditions [76](#abnormal-conditions-46)

8.14.2 UE Radio Capability Check [76](#ue-radio-capability-check)

8.14.2.1 General [76](#general-48)

8.14.2.2 Successful Operation [76](#successful-operation-46)

8.14.2.3 Unsuccessful Operation [77](#unsuccessful-operation-17)

8.14.2.4 Abnormal Conditions [77](#abnormal-conditions-47)

8.15 Data Usage Reporting Procedures [77](#data-usage-reporting-procedures)

8.15.1 Secondary RAT Data Usage Report [77](#secondary-rat-data-usage-report)

8.15.1.1 General [77](#general-49)

8.15.1.2 Successful Operation [77](#successful-operation-47)

8.15.1.3 Abnormal Conditions [77](#abnormal-conditions-48)

9 Elements for NGAP Communication [78](#elements-for-ngap-communication)

9.0 General [78](#general-50)

9.1 Tabular Format Contents [78](#tabular-format-contents)

9.1.1 Presence [78](#presence)

9.1.2 Criticality [78](#criticality)

9.1.3 Range [78](#range)

9.1.4 Assigned Criticality [79](#assigned-criticality)

9.2 Message Functional Definition and Content [79](#message-functional-definition-and-content)

9.2.1 PDU Session Management Messages [79](#pdu-session-management-messages)

9.2.1.1 PDU SESSION RESOURCE SETUP REQUEST [79](#pdu-session-resource-setup-request)

9.2.1.2 PDU SESSION RESOURCE SETUP RESPONSE [79](#pdu-session-resource-setup-response)

9.2.1.3 PDU SESSION RESOURCE RELEASE COMMAND [80](#pdu-session-resource-release-command)

9.2.1.4 PDU SESSION RESOURCE RELEASE RESPONSE [81](#pdu-session-resource-release-response)

9.2.1.5 PDU SESSION RESOURCE MODIFY REQUEST [81](#pdu-session-resource-modify-request)

9.2.1.6 PDU SESSION RESOURCE MODIFY RESPONSE [83](#pdu-session-resource-modify-response)

9.2.1.7 PDU SESSION RESOURCE NOTIFY [83](#pdu-session-resource-notify-1)

9.2.1.8 PDU SESSION RESOURCE MODIFY INDICATION [84](#pdu-session-resource-modify-indication-1)

9.2.1.9 PDU SESSION RESOURCE MODIFY CONFIRM [85](#pdu-session-resource-modify-confirm)

9.2.2 UE Context Management Messages [85](#ue-context-management-messages)

9.2.2.1 INITIAL CONTEXT SETUP REQUEST [85](#initial-context-setup-request)

9.2.2.2 INITIAL CONTEXT SETUP RESPONSE [87](#initial-context-setup-response)

9.2.2.3 INITIAL CONTEXT SETUP FAILURE [87](#initial-context-setup-failure)

9.2.2.4 UE CONTEXT RELEASE REQUEST [88](#ue-context-release-request)

9.2.2.5 UE CONTEXT RELEASE COMMAND [88](#ue-context-release-command)

9.2.2.6 UE CONTEXT RELEASE COMPLETE [89](#ue-context-release-complete)

9.2.2.7 UE CONTEXT MODIFICATION REQUEST [89](#ue-context-modification-request)

9.2.2.8 UE CONTEXT MODIFICATION RESPONSE [90](#ue-context-modification-response)

9.2.2.9 UE CONTEXT MODIFICATION FAILURE [90](#ue-context-modification-failure)

9.2.2.10 RRC INACTIVE TRANSITION REPORT [90](#rrc-inactive-transition-report-1)

9.2.3 UE Mobility Management Messages [91](#ue-mobility-management-messages)

9.2.3.1 HANDOVER REQUIRED [91](#handover-required)

9.2.3.2 HANDOVER COMMAND [91](#handover-command)

9.2.3.3 HANDOVER PREPARATION FAILURE [92](#handover-preparation-failure)

9.2.3.4 HANDOVER REQUEST [93](#handover-request)

9.2.3.5 HANDOVER REQUEST ACKNOWLEDGE [94](#handover-request-acknowledge)

9.2.3.6 HANDOVER FAILURE [94](#handover-failure)

9.2.3.7 HANDOVER NOTIFY [95](#handover-notify)

9.2.3.8 PATH SWITCH REQUEST [96](#path-switch-request-1)

9.2.3.9 PATH SWITCH REQUEST ACKNOWLEDGE [97](#path-switch-request-acknowledge)

9.2.3.10 PATH SWITCH REQUEST FAILURE [98](#path-switch-request-failure)

9.2.3.11 HANDOVER CANCEL [98](#handover-cancel)

9.2.3.12 HANDOVER CANCEL ACKNOWLEDGE [98](#handover-cancel-acknowledge)

9.2.3.13 UPLINK RAN STATUS TRANSFER [99](#uplink-ran-status-transfer-1)

9.2.3.14 DOWNLINK RAN STATUS TRANSFER [99](#downlink-ran-status-transfer-1)

9.2.4 Paging Messages [99](#paging-messages)

9.2.4.1 PAGING [99](#paging-1)

9.2.5 NAS Transport Messages [100](#nas-transport-messages)

9.2.5.1 INITIAL UE MESSAGE [100](#initial-ue-message-1)

9.2.5.2 DOWNLINK NAS TRANSPORT [100](#downlink-nas-transport-1)

9.2.5.3 UPLINK NAS TRANSPORT [100](#uplink-nas-transport-1)

9.2.5.4 NAS NON DELIVERY INDICATION [101](#nas-non-delivery-indication-1)

9.2.5.5 REROUTE NAS REQUEST [101](#reroute-nas-request-1)

9.2.6 Interface Management Messages [101](#interface-management-messages)

9.2.6.1 NG SETUP REQUEST [101](#ng-setup-request)

9.2.6.2 NG SETUP RESPONSE [102](#ng-setup-response)

9.2.6.3 NG SETUP FAILURE [103](#ng-setup-failure)

9.2.6.4 RAN CONFIGURATION UPDATE [103](#ran-configuration-update-1)

9.2.6.5 RAN CONFIGURATION UPDATE ACKNOWLEDGE [104](#ran-configuration-update-acknowledge)

9.2.6.6 RAN CONFIGURATION UPDATE FAILURE [104](#ran-configuration-update-failure)

9.2.6.7 AMF CONFIGURATION UPDATE [104](#amf-configuration-update-1)

9.2.6.8 AMF CONFIGURATION UPDATE ACKNOWLEDGE [106](#amf-configuration-update-acknowledge)

9.2.6.9 AMF CONFIGURATION UPDATE FAILURE [106](#amf-configuration-update-failure)

9.2.6.10 AMF STATUS INDICATION [106](#amf-status-indication-1)

9.2.6.11 NG RESET [107](#ng-reset-1)

9.2.6.12 NG RESET ACKNOWLEDGE [107](#ng-reset-acknowledge)

9.2.6.13 ERROR INDICATION [107](#error-indication-1)

9.2.6.14 OVERLOAD START [108](#overload-start-1)

9.2.6.15 OVERLOAD STOP [108](#overload-stop-1)

9.2.7 Configuration Transfer Messages [108](#configuration-transfer-messages)

9.2.7.1 UPLINK RAN CONFIGURATION TRANSFER [108](#uplink-ran-configuration-transfer-1)

9.2.7.2 DOWNLINK RAN CONFIGURATION TRANSFER [109](#downlink-ran-configuration-transfer-1)

9.2.8 Warning Message Transmission Messages [109](#warning-message-transmission-messages)

9.2.8.1 WRITE-REPLACE WARNING REQUEST [109](#write-replace-warning-request)

9.2.8.2 WRITE-REPLACE WARNING RESPONSE [110](#write-replace-warning-response)

9.2.8.3 PWS CANCEL REQUEST [110](#pws-cancel-request)

9.2.8.4 PWS CANCEL RESPONSE [110](#pws-cancel-response)

9.2.8.5 PWS RESTART INDICATION [110](#pws-restart-indication-1)

9.2.8.6 PWS FAILURE INDICATION [111](#pws-failure-indication-1)

9.2.9 NRPPa Transport Messages [112](#nrppa-transport-messages)

9.2.9.1 DOWNLINK UE ASSOCIATED NRPPA TRANSPORT [112](#downlink-ue-associated-nrppa-transport-1)

9.2.9.2 UPLINK UE ASSOCIATED NRPPA TRANSPORT [112](#uplink-ue-associated-nrppa-transport-1)

9.2.9.3 DOWNLINK NON UE ASSOCIATED NRPPA TRANSPORT [112](#downlink-non-ue-associated-nrppa-transport-1)

9.2.9.4 UPLINK NON UE ASSOCIATED NRPPA TRANSPORT [112](#uplink-non-ue-associated-nrppa-transport-1)

9.2.10 Trace Messages [113](#trace-messages)

9.2.10.1 TRACE START [113](#trace-start-1)

9.2.10.2 TRACE FAILURE INDICATION [113](#trace-failure-indication-1)

9.2.10.3 DEACTIVATE TRACE [113](#deactivate-trace-1)

9.2.10.4 CELL TRAFFIC TRACE [113](#cell-traffic-trace-1)

9.2.11 Location Reporting Messages [114](#location-reporting-messages)

9.2.11.1 LOCATION REPORTING CONTROL [114](#location-reporting-control-1)

9.2.11.2 LOCATION REPORTING FAILURE INDICATION [114](#location-reporting-failure-indication-1)

9.2.11.3 LOCATION REPORT [114](#location-report-1)

9.2.12 UE TNLA Binding Messages [115](#ue-tnla-binding-messages)

9.2.12.1 UE TNLA BINDING RELEASE REQUEST [115](#ue-tnla-binding-release-request)

9.2.13 UE Radio Capability Management Messages [115](#ue-radio-capability-management-messages)

9.2.13.1 UE RADIO CAPABILITY INFO INDICATION [115](#ue-radio-capability-info-indication-1)

9.2.13.2 UE RADIO CAPABILITY CHECK REQUEST [115](#ue-radio-capability-check-request)

9.2.13.3 UE RADIO CAPABILITY CHECK RESPONSE [116](#ue-radio-capability-check-response)

9.2.14 Data Usage Reporting Messages [116](#data-usage-reporting-messages)

9.2.14.1 SECONDARY RAT DATA USAGE REPORT [116](#secondary-rat-data-usage-report-1)

9.3 Information Element Definitions [117](#information-element-definitions)

9.3.1 Radio Network Layer Related IEs [117](#radio-network-layer-related-ies)

9.3.1.1 Message Type [117](#message-type)

9.3.1.2 Cause [117](#cause)

9.3.1.3 Criticality Diagnostics [121](#criticality-diagnostics)

9.3.1.4 Bit Rate [122](#bit-rate)

9.3.1.5 Global RAN Node ID [122](#global-ran-node-id)

9.3.1.6 Global gNB ID [123](#global-gnb-id)

9.3.1.7 NR CGI [123](#nr-cgi)

9.3.1.8 Global ng-eNB ID [123](#global-ng-enb-id)

9.3.1.9 E-UTRA CGI [124](#e-utra-cgi)

9.3.1.10 GBR QoS Flow Information [124](#gbr-qos-flow-information)

9.3.1.11 Void [124](#void)

9.3.1.12 QoS Flow Level QoS Parameters [124](#qos-flow-level-qos-parameters)

9.3.1.13 QoS Flow List with Cause [125](#qos-flow-list-with-cause)

9.3.1.14 Trace Activation [125](#trace-activation)

9.3.1.15 Core Network Assistance Information for RRC INACTIVE [126](#core-network-assistance-information-for-rrc-inactive)

9.3.1.16 User Location Information [126](#user-location-information)

9.3.1.17 Slice Support List [127](#slice-support-list)

9.3.1.18 Dynamic 5QI Descriptor [127](#dynamic-5qi-descriptor)

9.3.1.19 Allocation and Retention Priority [128](#allocation-and-retention-priority)

9.3.1.20 Source to Target Transparent Container [129](#source-to-target-transparent-container)

9.3.1.21 Target to Source Transparent Container [130](#target-to-source-transparent-container)

9.3.1.22 Handover Type [130](#handover-type)

9.3.1.23 MICO Mode Indication [130](#mico-mode-indication)

9.3.1.24 S-NSSAI [130](#s-nssai)

9.3.1.25 Target ID [130](#target-id)

9.3.1.26 Emergency Fallback Indicator [131](#emergency-fallback-indicator)

9.3.1.27 Security Indication [131](#security-indication)

9.3.1.28 Non Dynamic 5QI Descriptor [132](#non-dynamic-5qi-descriptor)

9.3.1.29 Source NG-RAN Node to Target NG-RAN Node Transparent Container [133](#source-ng-ran-node-to-target-ng-ran-node-transparent-container)

9.3.1.30 Target NG-RAN Node to Source NG-RAN Node Transparent Container [134](#target-ng-ran-node-to-source-ng-ran-node-transparent-container)

9.3.1.31 Allowed NSSAI [134](#allowed-nssai)

9.3.1.32 Relative AMF Capacity [134](#relative-amf-capacity)

9.3.1.33 DL Forwarding [134](#dl-forwarding)

9.3.1.34 DRBs to QoS Flows Mapping List [134](#drbs-to-qos-flows-mapping-list)

9.3.1.35 Message Identifier [135](#message-identifier)

9.3.1.36 Serial Number [135](#serial-number)

9.3.1.37 Warning Area List [135](#warning-area-list)

9.3.1.38 Number of Broadcasts Requested [136](#number-of-broadcasts-requested)

9.3.1.39 Warning Type [136](#warning-type)

9.3.1.40 Void [136](#void-1)

9.3.1.41 Data Coding Scheme [136](#data-coding-scheme)

9.3.1.42 Warning Message Contents [136](#warning-message-contents)

9.3.1.43 Broadcast Completed Area List [136](#broadcast-completed-area-list)

9.3.1.44 Broadcast Cancelled Area List [137](#broadcast-cancelled-area-list)

9.3.1.45 Number of Broadcasts [139](#number-of-broadcasts)

9.3.1.46 Concurrent Warning Message Indicator [139](#concurrent-warning-message-indicator)

9.3.1.47 Cancel-All Warning Messages Indicator [139](#cancel-all-warning-messages-indicator)

9.3.1.48 Emergency Area ID [139](#emergency-area-id)

9.3.1.49 Repetition Period [139](#repetition-period)

9.3.1.50 PDU Session ID [140](#pdu-session-id)

9.3.1.51 QoS Flow Identifier [140](#qos-flow-identifier)

9.3.1.52 PDU Session Type [140](#pdu-session-type)

9.3.1.53 DRB ID [140](#drb-id)

9.3.1.54 Masked IMEISV [140](#masked-imeisv)

9.3.1.55 New Security Context Indicator [141](#new-security-context-indicator)

9.3.1.56 Time to Wait [141](#time-to-wait)

9.3.1.57 Global N3IWF ID [141](#global-n3iwf-id)

9.3.1.58 UE Aggregate Maximum Bit Rate [141](#ue-aggregate-maximum-bit-rate)

9.3.1.59 Security Result [142](#security-result)

9.3.1.60 User Plane Security Information [142](#user-plane-security-information)

9.3.1.61 Index to RAT/Frequency Selection Priority [142](#index-to-ratfrequency-selection-priority)

9.3.1.62 Data Forwarding Accepted [142](#data-forwarding-accepted)

9.3.1.63 Data Forwarding Not Possible [142](#data-forwarding-not-possible)

9.3.1.64 Direct Forwarding Path Availability [143](#direct-forwarding-path-availability)

9.3.1.65 Location Reporting Request Type [143](#location-reporting-request-type)

9.3.1.66 Area of Interest [144](#area-of-interest)

9.3.1.67 UE Presence in Area of Interest List [144](#ue-presence-in-area-of-interest-list)

9.3.1.68 UE Radio Capability for Paging [144](#ue-radio-capability-for-paging)

9.3.1.69 Assistance Data for Paging [144](#assistance-data-for-paging)

9.3.1.70 Assistance Data for Recommended Cells [145](#assistance-data-for-recommended-cells)

9.3.1.71 Recommended Cells for Paging [145](#recommended-cells-for-paging)

9.3.1.72 Paging Attempt Information [145](#paging-attempt-information)

9.3.1.73 NG-RAN CGI [146](#ng-ran-cgi)

9.3.1.74 UE Radio Capability [146](#ue-radio-capability)

9.3.1.75 Time Stamp [146](#time-stamp)

9.3.1.76 Location Reporting Reference ID [146](#location-reporting-reference-id)

9.3.1.77 Data Forwarding Response DRB List [146](#data-forwarding-response-drb-list)

9.3.1.78 Paging Priority [147](#paging-priority)

9.3.1.79 Packet Loss Rate [147](#packet-loss-rate)

9.3.1.80 Packet Delay Budget [147](#packet-delay-budget)

9.3.1.81 Packet Error Rate [147](#packet-error-rate)

9.3.1.82 Averaging Window [147](#averaging-window)

9.3.1.83 Maximum Data Burst Volume [148](#maximum-data-burst-volume)

9.3.1.84 Priority Level [148](#priority-level)

9.3.1.85 Mobility Restriction List [148](#mobility-restriction-list)

9.3.1.86 UE Security Capabilities [150](#ue-security-capabilities)

9.3.1.87 Security Key [151](#security-key)

9.3.1.88 Security Context [152](#security-context)

9.3.1.89 IMS Voice Support Indicator [152](#ims-voice-support-indicator)

9.3.1.90 Paging DRX [152](#paging-drx)

9.3.1.91 RRC Inactive Transition Report Request [152](#rrc-inactive-transition-report-request)

9.3.1.92 RRC State [152](#rrc-state)

9.3.1.93 Expected UE Behaviour [153](#expected-ue-behaviour)

9.3.1.94 Expected UE Activity Behaviour [153](#expected-ue-activity-behaviour)

9.3.1.95 UE History Information [154](#ue-history-information)

9.3.1.96 Last Visited Cell Information [154](#last-visited-cell-information)

9.3.1.97 Last Visited NG-RAN Cell Information [155](#last-visited-ng-ran-cell-information)

9.3.1.98 Cell Type [155](#cell-type)

9.3.1.99 Associated QoS Flow List [155](#associated-qos-flow-list)

9.3.1.100 Information on Recommended Cells and RAN Nodes for Paging [155](#information-on-recommended-cells-and-ran-nodes-for-paging)

9.3.1.101 Recommended RAN Nodes for Paging [156](#recommended-ran-nodes-for-paging)

9.3.1.102 PDU Session Aggregate Maximum Bit Rate [156](#pdu-session-aggregate-maximum-bit-rate)

9.3.1.103 Maximum Integrity Protected Data Rate [156](#maximum-integrity-protected-data-rate)

9.3.1.104 Overload Response [157](#overload-response)

9.3.1.105 Overload Action [157](#overload-action)

9.3.1.106 Traffic Load Reduction Indication [157](#traffic-load-reduction-indication)

9.3.1.107 Slice Overload List [157](#slice-overload-list)

9.3.1.108 RAN Status Transfer Transparent Container [158](#ran-status-transfer-transparent-container)

9.3.1.109 COUNT Value for PDCP SN Length 12 [160](#count-value-for-pdcp-sn-length-12)

9.3.1.110 COUNT Value for PDCP SN Length 18 [160](#count-value-for-pdcp-sn-length-18)

9.3.1.111 RRC Establishment Cause [161](#rrc-establishment-cause)

9.3.1.112 Warning Area Coordinates [161](#warning-area-coordinates)

9.3.1.113 Network Instance [161](#network-instance)

9.3.1.114 Secondary RAT Usage Information [161](#secondary-rat-usage-information)

9.3.1.115 Volume Timed Report List [162](#volume-timed-report-list)

9.3.1.116 Redirection for Voice EPS Fallback [162](#redirection-for-voice-eps-fallback)

9.3.1.117 UE Retention Information [163](#ue-retention-information)

9.3.1.118 UL Forwarding [163](#ul-forwarding)

9.3.1.119 CN Assisted RAN Parameters Tuning [163](#cn-assisted-ran-parameters-tuning)

9.3.1.120 Common Network Instance [163](#common-network-instance)

9.3.2 Transport Network Layer Related IEs [163](#transport-network-layer-related-ies)

9.3.2.1 QoS Flow per TNL Information List [163](#qos-flow-per-tnl-information-list)

9.3.2.2 UP Transport Layer Information [164](#up-transport-layer-information)

9.3.2.3 E-RAB ID [164](#e-rab-id)

9.3.2.4 Transport Layer Address [164](#transport-layer-address)

9.3.2.5 GTP-TEID [164](#gtp-teid)

9.3.2.6 CP Transport Layer Information [165](#cp-transport-layer-information)

9.3.2.7 TNL Association List [165](#tnl-association-list)

9.3.2.8 QoS Flow per TNL Information [165](#qos-flow-per-tnl-information)

9.3.2.9 TNL Association Usage [165](#tnl-association-usage)

9.3.2.10 TNL Address Weight Factor [166](#tnl-address-weight-factor)

9.3.2.11 UP Transport Layer Information Pair List [166](#up-transport-layer-information-pair-list)

9.3.2.12 UP Transport Layer Information List [166](#up-transport-layer-information-list)

9.3.2.13 QoS Flow List with Data Forwarding [166](#qos-flow-list-with-data-forwarding)

9.3.3 NAS Related IEs [167](#nas-related-ies)

9.3.3.1 AMF UE NGAP ID [167](#amf-ue-ngap-id)

9.3.3.2 RAN UE NGAP ID [167](#ran-ue-ngap-id)

9.3.3.3 GUAMI [167](#guami)

9.3.3.4 NAS-PDU [167](#nas-pdu)

9.3.3.5 PLMN Identity [167](#plmn-identity)

9.3.3.6 SON Configuration Transfer [168](#son-configuration-transfer)

9.3.3.7 SON Information [168](#son-information)

9.3.3.8 SON Information Reply [169](#son-information-reply)

9.3.3.9 Xn TNL Configuration Info [169](#xn-tnl-configuration-info)

9.3.3.10 TAC [169](#tac)

9.3.3.11 TAI [170](#tai)

9.3.3.12 AMF Set ID [170](#amf-set-id)

9.3.3.13 Routing ID [170](#routing-id)

9.3.3.14 NRPPa-PDU [170](#nrppa-pdu)

9.3.3.15 RAN Paging Priority [170](#ran-paging-priority)

9.3.3.16 EPS TAC [170](#eps-tac)

9.3.3.17 EPS TAI [171](#eps-tai)

9.3.3.18 UE Paging Identity [171](#ue-paging-identity)

9.3.3.19 AMF Pointer [171](#amf-pointer)

9.3.3.20 5G-S-TMSI [171](#g-s-tmsi)

9.3.3.21 AMF Name [171](#amf-name)

9.3.3.22 Paging Origin [172](#paging-origin)

9.3.3.23 UE Identity Index Value [172](#ue-identity-index-value)

9.3.3.24 Periodic Registration Update Timer [172](#periodic-registration-update-timer)

9.3.3.25 UE-associated Logical NG-connection List [173](#ue-associated-logical-ng-connection-list)

9.3.3.26 NAS Security Parameters from NG-RAN [173](#nas-security-parameters-from-ng-ran)

9.3.3.27 Source to Target AMF Information Reroute [173](#source-to-target-amf-information-reroute)

9.3.4 SMF Related IEs [174](#smf-related-ies)

9.3.4.1 PDU Session Resource Setup Request Transfer [174](#pdu-session-resource-setup-request-transfer)

9.3.4.2 PDU Session Resource Setup Response Transfer [175](#pdu-session-resource-setup-response-transfer)

9.3.4.3 PDU Session Resource Modify Request Transfer [176](#pdu-session-resource-modify-request-transfer)

9.3.4.4 PDU Session Resource Modify Response Transfer [177](#pdu-session-resource-modify-response-transfer)

9.3.4.5 PDU Session Resource Notify Transfer [177](#pdu-session-resource-notify-transfer)

9.3.4.6 PDU Session Resource Modify Indication Transfer [178](#pdu-session-resource-modify-indication-transfer)

9.3.4.7 PDU Session Resource Modify Confirm Transfer [178](#pdu-session-resource-modify-confirm-transfer)

9.3.4.8 Path Switch Request Transfer [179](#path-switch-request-transfer)

9.3.4.9 Path Switch Request Acknowledge Transfer [180](#path-switch-request-acknowledge-transfer)

9.3.4.10 Handover Command Transfer [180](#handover-command-transfer)

9.3.4.11 Handover Request Acknowledge Transfer [181](#handover-request-acknowledge-transfer)

9.3.4.12 PDU Session Resource Release Command Transfer [183](#pdu-session-resource-release-command-transfer)

9.3.4.13 PDU Session Resource Notify Released Transfer [183](#pdu-session-resource-notify-released-transfer)

9.3.4.14 Handover Required Transfer [183](#handover-required-transfer)

9.3.4.15 Path Switch Request Setup Failed Transfer [183](#path-switch-request-setup-failed-transfer)

9.3.4.16 PDU Session Resource Setup Unsuccessful Transfer [183](#pdu-session-resource-setup-unsuccessful-transfer)

9.3.4.17 PDU Session Resource Modify Unsuccessful Transfer [183](#pdu-session-resource-modify-unsuccessful-transfer)

9.3.4.18 Handover Preparation Unsuccessful Transfer [184](#handover-preparation-unsuccessful-transfer)

9.3.4.19 Handover Resource Allocation Unsuccessful Transfer [184](#handover-resource-allocation-unsuccessful-transfer)

9.3.4.20 Path Switch Request Unsuccessful Transfer [184](#path-switch-request-unsuccessful-transfer)

9.3.4.21 PDU Session Resource Release Response Transfer [184](#pdu-session-resource-release-response-transfer)

9.3.4.22 PDU Session Resource Modify Indication Unsuccessful Transfer [184](#pdu-session-resource-modify-indication-unsuccessful-transfer)

9.3.4.23 Secondary RAT Data Usage Report Transfer [184](#secondary-rat-data-usage-report-transfer)

9.4 Message and Information Element Abstract Syntax (with ASN.1) [185](#message-and-information-element-abstract-syntax-with-asn.1)

9.4.1 General [185](#general-51)

9.4.2 Usage of private message mechanism for non-standard use [185](#usage-of-private-message-mechanism-for-non-standard-use)

9.4.3 Elementary Procedure Definitions [186](#elementary-procedure-definitions)

9.4.4 PDU Definitions [198](#pdu-definitions)

9.4.5 Information Element Definitions [240](#information-element-definitions-1)

9.4.6 Common Definitions [310](#common-definitions)

9.4.7 Constant Definitions [311](#constant-definitions)

9.4.8 Container Definitions [317](#container-definitions)

9.5 Message Transfer Syntax [322](#message-transfer-syntax)

9.6 Timers [322](#timers)

10 Handling of Unknown, Unforeseen and Erroneous Protocol Data [323](#handling-of-unknown-unforeseen-and-erroneous-protocol-data)

10.1 General [323](#general-52)

10.2 Transfer Syntax Error [323](#transfer-syntax-error)

10.3 Abstract Syntax Error [323](#abstract-syntax-error)

10.3.1 General [323](#general-53)

10.3.2 Criticality Information [324](#criticality-information)

10.3.3 Presence Information [324](#presence-information)

10.3.4 Not comprehended IE/IE group [325](#not-comprehended-ieie-group)

10.3.4.1 Procedure Code [325](#procedure-code)

10.3.4.1A Type of Message [325](#a-type-of-message)

10.3.4.2 IEs other than the Procedure Code and Type of Message [325](#ies-other-than-the-procedure-code-and-type-of-message)

10.3.5 Missing IE or IE group [326](#missing-ie-or-ie-group)

10.3.6 IEs or IE groups received in wrong order or with too many occurrences or erroneously present [327](#ies-or-ie-groups-received-in-wrong-order-or-with-too-many-occurrences-or-erroneously-present)

10.4 Logical Error [328](#logical-error)

10.5 Exceptions [328](#exceptions)

10.6 Handling of AP ID [329](#handling-of-ap-id)

Annex A (informative): Change history [330](#annex-a-informative-change-history)

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
