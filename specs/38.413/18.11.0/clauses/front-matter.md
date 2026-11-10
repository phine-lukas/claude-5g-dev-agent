3GPP TS 38.413 V18.11.0 (2026-09)

Technical Specification

3<sup>rd</sup> Generation Partnership Project;

Technical Specification Group Radio Access Network;

NG-RAN;

NG Application Protocol (NGAP)

(Release 18)

[figure] [figure]

The present document has been developed within the 3<sup>rd</sup> Generation Partnership Project (3GPP <sup>TM</sup>) and may be further elaborated for the purposes of 3GPP.  
The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented.  
This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification.  
Specifications and Reports for implementation of the 3GPP <sup>TM</sup> system should be obtained via the 3GPP Organizational Partners' Publications Offices.

> ***3GPP***
>
> Postal address
>
> 3GPP support office address
>
> 650 Route des Lucioles – Sophia Antipolis
>
> Valbonne – FRANCE
>
> Tel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16
>
> Internet
>
> <http://www.3gpp.org>

***Copyright Notification***

No part may be reproduced except as authorized by written permission.  
The copyright and the foregoing restriction extend to reproduction in all media.

© 2026, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC).

All rights reserved.

UMTS™ is a Trade Mark of ETSI registered for the benefit of its members

3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners  
LTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners

GSM® and the GSM logo are registered and owned by the GSM Association

#  Contents

Foreword [19](#foreword)

1 Scope [20](#scope)

2 References [20](#references)

3 Definitions and abbreviations [22](#definitions-and-abbreviations)

3.1 Definitions [22](#definitions)

3.2 Abbreviations [23](#abbreviations)

4 General [24](#general)

4.1 Procedure Specification Principles [24](#procedure-specification-principles)

4.2 Forwards and Backwards Compatibility [25](#forwards-and-backwards-compatibility)

4.3 Specification Notations [25](#specification-notations)

5 NGAP Services [25](#ngap-services)

6 Services Expected from Signalling Transport [25](#services-expected-from-signalling-transport)

7 Functions of NGAP [25](#functions-of-ngap)

8 NGAP Procedures [26](#ngap-procedures)

8.1 List of NGAP Elementary Procedures [26](#list-of-ngap-elementary-procedures)

8.2 PDU Session Management Procedures [29](#pdu-session-management-procedures)

8.2.1 PDU Session Resource Setup [29](#pdu-session-resource-setup)

8.2.1.1 General [29](#general-1)

8.2.1.2 Successful Operation [29](#successful-operation)

8.2.1.3 Unsuccessful Operation [33](#unsuccessful-operation)

8.2.1.4 Abnormal Conditions [34](#abnormal-conditions)

8.2.2 PDU Session Resource Release [34](#pdu-session-resource-release)

8.2.2.1 General [34](#general-2)

8.2.2.2 Successful Operation [34](#successful-operation-1)

8.2.2.3 Unsuccessful Operation [35](#unsuccessful-operation-1)

8.2.2.4 Abnormal Conditions [35](#abnormal-conditions-1)

8.2.3 PDU Session Resource Modify [35](#pdu-session-resource-modify)

8.2.3.1 General [35](#general-3)

8.2.3.2 Successful Operation [35](#successful-operation-2)

8.2.3.3 Unsuccessful Operation [40](#unsuccessful-operation-2)

8.2.3.4 Abnormal Conditions [40](#abnormal-conditions-2)

8.2.4 PDU Session Resource Notify [40](#pdu-session-resource-notify)

8.2.4.1 General [40](#general-4)

8.2.4.2 Successful Operation [41](#successful-operation-3)

8.2.4.3 Abnormal Conditions [41](#abnormal-conditions-3)

8.2.5 PDU Session Resource Modify Indication [42](#pdu-session-resource-modify-indication)

8.2.5.1 General [42](#general-5)

8.2.5.2 Successful Operation [42](#successful-operation-4)

8.2.5.3 Unsuccessful Operation [43](#unsuccessful-operation-3)

8.2.5.4 Abnormal Conditions [44](#abnormal-conditions-4)

8.3 UE Context Management Procedures [44](#ue-context-management-procedures)

8.3.1 Initial Context Setup [44](#initial-context-setup)

8.3.1.1 General [44](#general-6)

8.3.1.2 Successful Operation [44](#successful-operation-5)

8.3.1.3 Unsuccessful Operation [49](#unsuccessful-operation-4)

8.3.1.4 Abnormal Conditions [49](#abnormal-conditions-5)

8.3.2 UE Context Release Request (NG-RAN node initiated) [49](#ue-context-release-request-ng-ran-node-initiated)

8.3.2.1 General [49](#general-7)

8.3.2.2 Successful Operation [50](#successful-operation-6)

8.3.2.3 Abnormal Conditions [50](#abnormal-conditions-6)

8.3.3 UE Context Release (AMF initiated) [50](#ue-context-release-amf-initiated)

8.3.3.1 General [50](#general-8)

8.3.3.2 Successful Operation [50](#successful-operation-7)

8.3.3.3 Unsuccessful Operation [51](#unsuccessful-operation-5)

8.3.3.4 Abnormal Conditions [51](#abnormal-conditions-7)

8.3.4 UE Context Modification [51](#ue-context-modification)

8.3.4.1 General [51](#general-9)

8.3.4.2 Successful Operation [51](#successful-operation-8)

8.3.4.3 Unsuccessful Operation [55](#unsuccessful-operation-6)

8.3.4.4 Abnormal Conditions [55](#abnormal-conditions-8)

8.3.5 RRC Inactive Transition Report [55](#rrc-inactive-transition-report)

8.3.5.1 General [55](#general-10)

8.3.5.2 Successful Operation [56](#successful-operation-9)

8.3.5.3 Abnormal Conditions [56](#abnormal-conditions-9)

8.3.6 Connection Establishment Indication [56](#connection-establishment-indication)

8.3.6.1 General [56](#general-11)

8.3.6.2 Successful Operation [56](#successful-operation-10)

8.3.6.3 Abnormal Conditions [57](#abnormal-conditions-10)

8.3.7 AMF CP Relocation Indication [57](#amf-cp-relocation-indication)

8.3.7.1 General [57](#general-12)

8.3.7.2 Successful Operation [58](#successful-operation-11)

8.3.7.3 Abnormal Conditions [58](#abnormal-conditions-11)

8.3.8 RAN CP Relocation Indication [58](#ran-cp-relocation-indication)

8.3.8.1 General [58](#general-13)

8.3.8.2 Successful Operation [58](#successful-operation-12)

8.3.8.3 Abnormal Conditions [59](#abnormal-conditions-12)

8.3.9 Retrieve UE Information [59](#retrieve-ue-information)

8.3.9.1 General [59](#general-14)

8.3.9.2 Successful Operation [59](#successful-operation-13)

8.3.9.3 Abnormal Conditions [59](#abnormal-conditions-13)

8.3.10 UE Information Transfer [59](#ue-information-transfer)

8.3.10.1 General [59](#general-15)

8.3.10.2 Successful Operation [60](#successful-operation-14)

8.3.10.3 Abnormal Conditions [60](#abnormal-conditions-14)

8.3.11 UE Context Suspend [60](#ue-context-suspend)

8.3.11.1 General [60](#general-16)

8.3.11.2 Successful Operation [61](#successful-operation-15)

8.3.11.3 Unsuccessful Operation [61](#unsuccessful-operation-7)

8.3.11.4 Abnormal Conditions [61](#abnormal-conditions-15)

8.3.12 UE Context Resume [62](#ue-context-resume)

8.3.12.1 General [62](#general-17)

8.3.12.2 Successful Operation [62](#successful-operation-16)

8.3.12.3 Unsuccessful Operation [63](#unsuccessful-operation-8)

8.3.12.4 Abnormal Conditions [63](#abnormal-conditions-16)

8.3.13 MT Communication Handling [63](#mt-communication-handling)

8.3.13.1 General [63](#general-18)

8.3.13.2 Successful Operation [63](#successful-operation-17)

8.3.13.3 Unsuccessful Operation [64](#unsuccessful-operation-9)

8.3.13.4 Abnormal Conditions [64](#abnormal-conditions-17)

8.3.14 RAN Paging Request [64](#ran-paging-request)

8.3.14.1 General [64](#general-19)

8.3.14.2 Successful Operation [64](#successful-operation-18)

8.3.14.3 Abnormal Conditions [64](#abnormal-conditions-18)

8.4 UE Mobility Management Procedures [65](#ue-mobility-management-procedures)

8.4.1 Handover Preparation [65](#handover-preparation)

8.4.1.1 General [65](#general-20)

8.4.1.2 Successful Operation [65](#successful-operation-19)

8.4.1.3 Unsuccessful Operation [67](#unsuccessful-operation-10)

8.4.1.4 Abnormal Conditions [67](#abnormal-conditions-19)

8.4.2 Handover Resource Allocation [68](#handover-resource-allocation)

8.4.2.1 General [68](#general-21)

8.4.2.2 Successful Operation [68](#successful-operation-20)

8.4.2.3 Unsuccessful Operation [75](#unsuccessful-operation-11)

8.4.2.4 Abnormal Conditions [76](#abnormal-conditions-20)

8.4.3 Handover Notification [76](#handover-notification)

8.4.3.1 General [76](#general-22)

8.4.3.2 Successful Operation [77](#successful-operation-21)

8.4.3.3 Abnormal Conditions [77](#abnormal-conditions-21)

8.4.4 Path Switch Request [77](#path-switch-request)

8.4.4.1 General [77](#general-23)

8.4.4.2 Successful Operation [77](#successful-operation-22)

8.4.4.3 Unsuccessful Operation [83](#unsuccessful-operation-12)

8.4.4.4 Abnormal Conditions [83](#abnormal-conditions-22)

8.4.5 Handover Cancellation [83](#handover-cancellation)

8.4.5.1 General [83](#general-24)

8.4.5.2 Successful Operation [84](#successful-operation-23)

8.4.5.3 Unsuccessful Operation [84](#unsuccessful-operation-13)

8.4.5.4 Abnormal Conditions [84](#abnormal-conditions-23)

8.4.6 Uplink RAN Status Transfer [84](#uplink-ran-status-transfer)

8.4.6.1 General [84](#general-25)

8.4.6.2 Successful Operation [84](#successful-operation-24)

8.4.6.3 Abnormal Conditions [85](#abnormal-conditions-24)

8.4.7 Downlink RAN Status Transfer [85](#downlink-ran-status-transfer)

8.4.7.1 General [85](#general-26)

8.4.7.2 Successful Operation [85](#successful-operation-25)

8.4.7.3 Abnormal Conditions [85](#abnormal-conditions-25)

8.4.8 Handover Success [85](#handover-success)

8.4.8.1 General [85](#general-27)

8.4.8.2 Successful Operation [86](#successful-operation-26)

8.4.8.3 Abnormal Conditions [86](#abnormal-conditions-26)

8.4.9 Uplink RAN Early Status Transfer [86](#uplink-ran-early-status-transfer)

8.4.9.1 General [86](#general-28)

8.4.9.2 Successful Operation [86](#successful-operation-27)

8.4.9.3 Abnormal Conditions [86](#abnormal-conditions-27)

8.4.10 Downlink RAN Early Status Transfer [87](#downlink-ran-early-status-transfer)

8.4.10.1 General [87](#general-29)

8.4.10.2 Successful Operation [87](#successful-operation-28)

8.4.10.3 Abnormal Conditions [87](#abnormal-conditions-28)

8.5 Paging Procedures [87](#paging-procedures)

8.5.1 Paging [87](#paging)

8.5.1.1 General [87](#general-30)

8.5.1.2 Successful Operation [88](#successful-operation-29)

8.5.1.3 Abnormal Conditions [89](#abnormal-conditions-29)

8.5.2 Multicast Group Paging [89](#multicast-group-paging)

8.5.2.1 General [89](#general-31)

8.5.2.2 Successful Operation [89](#successful-operation-30)

8.5.2.3 Abnormal Conditions [90](#abnormal-conditions-30)

8.6 Transport of NAS Messages Procedures [90](#transport-of-nas-messages-procedures)

8.6.1 Initial UE Message [90](#initial-ue-message)

8.6.1.1 General [90](#general-32)

8.6.1.2 Successful Operation [90](#successful-operation-31)

8.6.1.3 Abnormal Conditions [91](#abnormal-conditions-31)

8.6.2 Downlink NAS Transport [91](#downlink-nas-transport)

8.6.2.1 General [91](#general-33)

8.6.2.2 Successful Operation [91](#successful-operation-32)

8.6.2.3 Abnormal Conditions [93](#abnormal-conditions-32)

8.6.3 Uplink NAS Transport [93](#uplink-nas-transport)

8.6.3.1 General [93](#general-34)

8.6.3.2 Successful Operation [93](#successful-operation-33)

8.6.3.3 Abnormal Conditions [94](#abnormal-conditions-33)

8.6.4 NAS Non Delivery Indication [94](#nas-non-delivery-indication)

8.6.4.1 General [94](#general-35)

8.6.4.2 Successful Operation [94](#successful-operation-34)

8.6.4.3 Abnormal Conditions [94](#abnormal-conditions-34)

8.6.5 Reroute NAS Request [94](#reroute-nas-request)

8.6.5.1 General [94](#general-36)

8.6.5.2 Successful Operation [95](#successful-operation-35)

8.6.5.3 Abnormal Conditions [95](#abnormal-conditions-35)

8.7 Interface Management Procedures [95](#interface-management-procedures)

8.7.1 NG Setup [95](#ng-setup)

8.7.1.1 General [95](#general-37)

8.7.1.2 Successful Operation [96](#successful-operation-36)

8.7.1.3 Unsuccessful Operation [97](#unsuccessful-operation-14)

8.7.1.4 Abnormal Conditions [97](#abnormal-conditions-36)

8.7.2 RAN Configuration Update [97](#ran-configuration-update)

8.7.2.1 General [97](#general-38)

8.7.2.2 Successful Operation [97](#successful-operation-37)

8.7.2.3 Unsuccessful Operation [99](#unsuccessful-operation-15)

8.7.2.4 Abnormal Conditions [99](#abnormal-conditions-37)

8.7.3 AMF Configuration Update [99](#amf-configuration-update)

8.7.3.1 General [99](#general-39)

8.7.3.2 Successful Operation [99](#successful-operation-38)

8.7.3.3 Unsuccessful Operation [101](#unsuccessful-operation-16)

8.7.3.4 Abnormal Conditions [101](#abnormal-conditions-38)

8.7.4 NG Reset [101](#ng-reset)

8.7.4.1 General [101](#general-40)

8.7.4.2 Successful Operation [101](#successful-operation-39)

8.7.4.2.1 NG Reset initiated by the AMF [101](#ng-reset-initiated-by-the-amf)

8.7.4.2.2 NG Reset initiated by the NG-RAN node [102](#ng-reset-initiated-by-the-ng-ran-node)

8.7.4.3 Unsuccessful Operation [103](#unsuccessful-operation-17)

8.7.4.4 Abnormal Conditions [103](#abnormal-conditions-39)

8.7.4.4.1 Abnormal Condition at the 5GC [103](#abnormal-condition-at-the-5gc)

8.7.4.4.2 Abnormal Condition at the NG-RAN [103](#abnormal-condition-at-the-ng-ran)

8.7.4.4.3 Crossing of NG RESET Messages [103](#crossing-of-ng-reset-messages)

8.7.5 Error Indication [104](#error-indication)

8.7.5.1 General [104](#general-41)

8.7.5.2 Successful Operation [104](#successful-operation-40)

8.7.5.3 Abnormal Conditions [104](#abnormal-conditions-40)

8.7.6 AMF Status Indication [104](#amf-status-indication)

8.7.6.1 General [104](#general-42)

8.7.6.2 Successful Operation [105](#successful-operation-41)

8.7.6.3 Abnormal Conditions [105](#abnormal-conditions-41)

8.7.7 Overload Start [105](#overload-start)

8.7.7.1 General [105](#general-43)

8.7.7.2 Successful Operation [105](#successful-operation-42)

8.7.7.3 Abnormal Conditions [106](#abnormal-conditions-42)

8.7.8 Overload Stop [106](#overload-stop)

8.7.8.1 General [106](#general-44)

8.7.8.2 Successful Operation [107](#successful-operation-43)

8.7.8.3 Abnormal Conditions [107](#abnormal-conditions-43)

8.8 Configuration Transfer Procedures [107](#configuration-transfer-procedures)

8.8.1 Uplink RAN Configuration Transfer [107](#uplink-ran-configuration-transfer)

8.8.1.1 General [107](#general-45)

8.8.1.2 Successful Operation [107](#successful-operation-44)

8.8.1.3 Abnormal Conditions [108](#abnormal-conditions-44)

8.8.2 Downlink RAN Configuration Transfer [108](#downlink-ran-configuration-transfer)

8.8.2.1 General [108](#general-46)

8.8.2.2 Successful Operation [108](#successful-operation-45)

8.8.2.3 Abnormal Conditions [109](#abnormal-conditions-45)

8.9 Warning Message Transmission Procedures [109](#warning-message-transmission-procedures)

8.9.1 Write-Replace Warning [109](#write-replace-warning)

8.9.1.1 General [109](#general-47)

8.9.1.2 Successful Operation [109](#successful-operation-46)

8.9.1.3 Unsuccessful Operation [110](#unsuccessful-operation-18)

8.9.1.4 Abnormal Conditions [110](#abnormal-conditions-46)

8.9.2 PWS Cancel [111](#pws-cancel)

8.9.2.1 General [111](#general-48)

8.9.2.2 Successful Operation [111](#successful-operation-47)

8.9.2.3 Unsuccessful Operation [111](#unsuccessful-operation-19)

8.9.2.4 Abnormal Conditions [111](#abnormal-conditions-47)

8.9.3 PWS Restart Indication [112](#pws-restart-indication)

8.9.3.1 General [112](#general-49)

8.9.3.2 Successful Operation [112](#successful-operation-48)

8.9.3.3 Abnormal Conditions [112](#abnormal-conditions-48)

8.9.4 PWS Failure Indication [112](#pws-failure-indication)

8.9.4.1 General [112](#general-50)

8.9.4.2 Successful Operation [112](#successful-operation-49)

8.9.4.3 Abnormal Conditions [113](#abnormal-conditions-49)

8.10 NRPPa Transport Procedures [113](#nrppa-transport-procedures)

8.10.1 General [113](#general-51)

8.10.2 Successful Operations [113](#successful-operations)

8.10.2.1 DOWNLINK UE ASSOCIATED NRPPA TRANSPORT [113](#downlink-ue-associated-nrppa-transport)

8.10.2.2 UPLINK UE ASSOCIATED NRPPA TRANSPORT [113](#uplink-ue-associated-nrppa-transport)

8.10.2.3 DOWNLINK NON UE ASSOCIATED NRPPA TRANSPORT [114](#downlink-non-ue-associated-nrppa-transport)

8.10.2.4 UPLINK NON UE ASSOCIATED NRPPA TRANSPORT [114](#uplink-non-ue-associated-nrppa-transport)

8.10.3 Unsuccessful Operations [114](#unsuccessful-operations)

8.10.4 Abnormal Conditions [114](#abnormal-conditions-50)

8.11 Trace Procedures [114](#trace-procedures)

8.11.1 Trace Start [114](#trace-start)

8.11.1.1 General [114](#general-52)

8.11.1.2 Successful Operation [115](#successful-operation-50)

8.11.1.3 Abnormal Conditions [116](#abnormal-conditions-51)

8.11.2 Trace Failure Indication [116](#trace-failure-indication)

8.11.2.1 General [116](#general-53)

8.11.2.2 Successful Operation [116](#successful-operation-51)

8.11.2.3 Abnormal Conditions [116](#abnormal-conditions-52)

8.11.3 Deactivate Trace [116](#deactivate-trace)

8.11.3.1 General [116](#general-54)

8.11.3.2 Successful Operation [117](#successful-operation-52)

8.11.3.3 Abnormal Conditions [117](#abnormal-conditions-53)

8.11.4 Cell Traffic Trace [117](#cell-traffic-trace)

8.11.4.1 General [117](#general-55)

8.11.4.2 Successful Operation [117](#successful-operation-53)

8.11.4.3 Abnormal Conditions [117](#abnormal-conditions-54)

8.12 Location Reporting Procedures [118](#location-reporting-procedures)

8.12.1 Location Reporting Control [118](#location-reporting-control)

8.12.1.1 General [118](#general-56)

8.12.1.2 Successful Operation [118](#successful-operation-54)

8.12.1.3 Abnormal Conditions [119](#abnormal-conditions-55)

8.12.2 Location Reporting Failure Indication [119](#location-reporting-failure-indication)

8.12.2.1 General [119](#general-57)

8.12.2.2 Successful Operation [119](#successful-operation-55)

8.12.2.3 Abnormal Conditions [119](#abnormal-conditions-56)

8.12.3 Location Report [119](#location-report)

8.12.3.1 General [119](#general-58)

8.12.3.2 Successful Operation [120](#successful-operation-56)

8.12.3.3 Abnormal Conditions [120](#abnormal-conditions-57)

8.13 UE TNLA Binding Procedures [120](#ue-tnla-binding-procedures)

8.13.1 UE TNLA Binding Release [120](#ue-tnla-binding-release)

8.13.1.1 General [120](#general-59)

8.13.1.2 Successful Operation [120](#successful-operation-57)

8.13.1.3 Abnormal Conditions [120](#abnormal-conditions-58)

8.14 UE Radio Capability Management Procedures [121](#ue-radio-capability-management-procedures)

8.14.1 UE Radio Capability Info Indication [121](#ue-radio-capability-info-indication)

8.14.1.1 General [121](#general-60)

8.14.1.2 Successful Operation [121](#successful-operation-58)

8.14.1.3 Abnormal Conditions [121](#abnormal-conditions-59)

8.14.2 UE Radio Capability Check [121](#ue-radio-capability-check)

8.14.2.1 General [121](#general-61)

8.14.2.2 Successful Operation [122](#successful-operation-59)

8.14.2.3 Unsuccessful Operation [122](#unsuccessful-operation-20)

8.14.2.4 Abnormal Conditions [122](#abnormal-conditions-60)

8.14.3 UE Radio Capability ID Mapping [122](#ue-radio-capability-id-mapping)

8.14.3.1 General [122](#general-62)

8.14.3.2 Successful Operation [123](#successful-operation-60)

8.14.3.3 Unsuccessful Operation [123](#unsuccessful-operation-21)

8.14.3.4 Abnormal Conditions [123](#abnormal-conditions-61)

8.15 Data Usage Reporting Procedures [123](#data-usage-reporting-procedures)

8.15.1 Secondary RAT Data Usage Report [123](#secondary-rat-data-usage-report)

8.15.1.1 General [123](#general-63)

8.15.1.2 Successful Operation [123](#successful-operation-61)

8.15.1.3 Abnormal Conditions [124](#abnormal-conditions-62)

8.16 RIM Information Transfer Procedures [124](#rim-information-transfer-procedures)

8.16.1 Uplink RIM Information Transfer [124](#uplink-rim-information-transfer)

8.16.1.1 General [124](#general-64)

8.16.1.2 Successful Operation [124](#successful-operation-62)

8.16.1.3 Abnormal Conditions [124](#abnormal-conditions-63)

8.16.2 Downlink RIM Information Transfer [124](#downlink-rim-information-transfer)

8.16.2.1 General [124](#general-65)

8.16.2.2 Successful Operation [125](#successful-operation-63)

8.16.2.3 Abnormal Conditions [125](#abnormal-conditions-64)

8.17 Broadcast Session Management Procedures [125](#broadcast-session-management-procedures)

8.17.1 Broadcast Session Setup [125](#broadcast-session-setup)

8.17.1.1 General [125](#general-66)

8.17.1.2 Successful Operation [125](#successful-operation-64)

8.17.1.3 Unsuccessful Operation [126](#unsuccessful-operation-22)

8.17.1.4 Abnormal Conditions [126](#abnormal-conditions-65)

8.17.2 Broadcast Session Modification [126](#broadcast-session-modification)

8.17.2.1 General [126](#general-67)

8.17.2.2 Successful Operation [126](#successful-operation-65)

8.17.2.3 Unsuccessful Operation [127](#unsuccessful-operation-23)

8.17.2.4 Abnormal Conditions [127](#abnormal-conditions-66)

8.17.3 Broadcast Session Release [127](#broadcast-session-release)

8.17.3.1 General [127](#general-68)

8.17.3.2 Successful Operation [127](#successful-operation-66)

8.17.3.3 Unsuccessful Operation [128](#unsuccessful-operation-24)

8.17.3.4 Abnormal Conditions [128](#abnormal-conditions-67)

8.17.4 Broadcast Session Release Required [128](#broadcast-session-release-required)

8.17.4.1 General [128](#general-69)

8.17.4.2 Successful Operation [128](#successful-operation-67)

8.17.4.3 Abnormal Conditions [128](#abnormal-conditions-68)

8.17.5 Broadcast Session Transport [128](#broadcast-session-transport)

8.17.5.1 General [128](#general-70)

8.17.5.2 Successful Operation [129](#successful-operation-68)

8.17.5.3 Unsuccessful Operation [129](#unsuccessful-operation-25)

8.17.5.4 Abnormal Conditions [129](#abnormal-conditions-69)

8.18 Multicast Session Management Procedures [129](#multicast-session-management-procedures)

8.18.1 Distribution Setup [129](#distribution-setup)

8.18.1.1 General [129](#general-71)

8.18.1.2 Successful Operation [130](#successful-operation-69)

8.18.1.3 Unsuccessful Operation [130](#unsuccessful-operation-26)

8.18.1.4 Abnormal Conditions [130](#abnormal-conditions-70)

8.18.2 Distribution Release [131](#distribution-release)

8.18.2.1 General [131](#general-72)

8.18.2.2 Successful Operation [131](#successful-operation-70)

8.18.2.3 Unsuccessful Operation [131](#unsuccessful-operation-27)

8.18.2.4 Abnormal Conditions [131](#abnormal-conditions-71)

8.18.3 Multicast Session Activation [131](#multicast-session-activation)

8.18.3.1 General [131](#general-73)

8.18.3.2 Successful Operation [132](#successful-operation-71)

8.18.3.3 Unsuccessful Operation [132](#unsuccessful-operation-28)

8.18.3.4 Abnormal Conditions [132](#abnormal-conditions-72)

8.18.4 Multicast Session Deactivation [133](#multicast-session-deactivation)

8.18.4.1 General [133](#general-74)

8.18.4.2 Successful Operation [133](#successful-operation-72)

8.18.4.3 Unsuccessful Operation [133](#unsuccessful-operation-29)

8.18.4.4 Abnormal Conditions [133](#abnormal-conditions-73)

8.18.5 Multicast Session Update [133](#multicast-session-update)

8.18.5.1 General [133](#general-75)

8.18.5.2 Successful Operation [134](#successful-operation-73)

8.18.5.3 Unsuccessful Operation [135](#unsuccessful-operation-30)

8.18.5.4 Abnormal Conditions [135](#abnormal-conditions-74)

8.19 Timing Synchronisation Status Reporting Procedures [135](#timing-synchronisation-status-reporting-procedures)

8.19.1 Timing Synchronisation Status [135](#timing-synchronisation-status)

8.19.1.1 General [135](#general-76)

8.19.1.2 Successful Operation [135](#successful-operation-74)

8.19.1.3 Unsuccessful Operation [136](#unsuccessful-operation-31)

8.19.1.4 Abnormal Conditions [136](#abnormal-conditions-75)

8.19.2 Timing Synchronisation Status Report [136](#timing-synchronisation-status-report)

8.19.2.1 General [136](#general-77)

8.19.2.2 Successful Operation [136](#successful-operation-75)

8.19.2.3 Abnormal Conditions [136](#abnormal-conditions-76)

9 Elements for NGAP Communication [137](#elements-for-ngap-communication)

9.0 General [137](#general-78)

9.1 Tabular Format Contents [137](#tabular-format-contents)

9.1.1 Presence [137](#presence)

9.1.2 Criticality [137](#criticality)

9.1.3 Range [137](#range)

9.1.4 Assigned Criticality [138](#assigned-criticality)

9.2 Message Functional Definition and Content [138](#message-functional-definition-and-content)

9.2.1 PDU Session Management Messages [138](#pdu-session-management-messages)

9.2.1.1 PDU SESSION RESOURCE SETUP REQUEST [138](#pdu-session-resource-setup-request)

9.2.1.2 PDU SESSION RESOURCE SETUP RESPONSE [138](#pdu-session-resource-setup-response)

9.2.1.3 PDU SESSION RESOURCE RELEASE COMMAND [139](#pdu-session-resource-release-command)

9.2.1.4 PDU SESSION RESOURCE RELEASE RESPONSE [140](#pdu-session-resource-release-response)

9.2.1.5 PDU SESSION RESOURCE MODIFY REQUEST [140](#pdu-session-resource-modify-request)

9.2.1.6 PDU SESSION RESOURCE MODIFY RESPONSE [142](#pdu-session-resource-modify-response)

9.2.1.7 PDU SESSION RESOURCE NOTIFY [142](#pdu-session-resource-notify-1)

9.2.1.8 PDU SESSION RESOURCE MODIFY INDICATION [143](#pdu-session-resource-modify-indication-1)

9.2.1.9 PDU SESSION RESOURCE MODIFY CONFIRM [144](#pdu-session-resource-modify-confirm)

9.2.2 UE Context Management Messages [144](#ue-context-management-messages)

9.2.2.1 INITIAL CONTEXT SETUP REQUEST [144](#initial-context-setup-request)

9.2.2.2 INITIAL CONTEXT SETUP RESPONSE [147](#initial-context-setup-response)

9.2.2.3 INITIAL CONTEXT SETUP FAILURE [148](#initial-context-setup-failure)

9.2.2.4 UE CONTEXT RELEASE REQUEST [149](#ue-context-release-request)

9.2.2.5 UE CONTEXT RELEASE COMMAND [149](#ue-context-release-command)

9.2.2.6 UE CONTEXT RELEASE COMPLETE [149](#ue-context-release-complete)

9.2.2.7 UE CONTEXT MODIFICATION REQUEST [150](#ue-context-modification-request)

9.2.2.8 UE CONTEXT MODIFICATION RESPONSE [152](#ue-context-modification-response)

9.2.2.9 UE CONTEXT MODIFICATION FAILURE [152](#ue-context-modification-failure)

9.2.2.10 RRC INACTIVE TRANSITION REPORT [153](#rrc-inactive-transition-report-1)

9.2.2.11 CONNECTION ESTABLISHMENT INDICATION [153](#connection-establishment-indication-1)

9.2.2.12 AMF CP RELOCATION INDICATION [154](#amf-cp-relocation-indication-1)

9.2.2.13 RAN CP RELOCATION INDICATION [154](#ran-cp-relocation-indication-1)

9.2.2.14 RETRIEVE UE INFORMATION [154](#retrieve-ue-information-1)

9.2.2.15 UE INFORMATION TRANSFER [155](#ue-information-transfer-1)

9.2.2.16 UE CONTEXT SUSPEND REQUEST [155](#ue-context-suspend-request)

9.2.2.17 UE CONTEXT SUSPEND RESPONSE [156](#ue-context-suspend-response)

9.2.2.18 UE CONTEXT SUSPEND FAILURE [156](#ue-context-suspend-failure)

9.2.2.19 UE CONTEXT RESUME REQUEST [157](#ue-context-resume-request)

9.2.2.20 UE CONTEXT RESUME RESPONSE [157](#ue-context-resume-response)

9.2.2.21 UE CONTEXT RESUME FAILURE [158](#ue-context-resume-failure)

9.2.2.22 MT COMMUNICATION HANDLING REQUEST [158](#mt-communication-handling-request)

9.2.2.23 MT COMMUNICATION HANDLING RESPONSE [159](#mt-communication-handling-response)

9.2.2.24 MT COMMUNICATION HANDLING FAILURE [159](#mt-communication-handling-failure)

9.2.2.25 RAN PAGING REQUEST [159](#ran-paging-request-1)

9.2.3 UE Mobility Management Messages [160](#ue-mobility-management-messages)

9.2.3.1 HANDOVER REQUIRED [160](#handover-required)

9.2.3.2 HANDOVER COMMAND [160](#handover-command)

9.2.3.3 HANDOVER PREPARATION FAILURE [161](#handover-preparation-failure)

9.2.3.4 HANDOVER REQUEST [162](#handover-request)

9.2.3.5 HANDOVER REQUEST ACKNOWLEDGE [165](#handover-request-acknowledge)

9.2.3.6 HANDOVER FAILURE [166](#handover-failure)

9.2.3.7 HANDOVER NOTIFY [166](#handover-notify)

9.2.3.8 PATH SWITCH REQUEST [167](#path-switch-request-1)

9.2.3.9 PATH SWITCH REQUEST ACKNOWLEDGE [168](#path-switch-request-acknowledge)

9.2.3.10 PATH SWITCH REQUEST FAILURE [171](#path-switch-request-failure)

9.2.3.11 HANDOVER CANCEL [171](#handover-cancel)

9.2.3.12 HANDOVER CANCEL ACKNOWLEDGE [171](#handover-cancel-acknowledge)

9.2.3.13 UPLINK RAN STATUS TRANSFER [172](#uplink-ran-status-transfer-1)

9.2.3.14 DOWNLINK RAN STATUS TRANSFER [172](#downlink-ran-status-transfer-1)

9.2.3.15 HANDOVER SUCCESS [172](#handover-success-1)

9.2.3.16 UPLINK RAN EARLY STATUS TRANSFER [172](#uplink-ran-early-status-transfer-1)

9.2.3.17 DOWNLINK RAN EARLY STATUS TRANSFER [173](#downlink-ran-early-status-transfer-1)

9.2.4 Paging Messages [173](#paging-messages)

9.2.4.1 PAGING [173](#paging-1)

9.2.4.2 MULTICAST GROUP PAGING [174](#multicast-group-paging-1)

9.2.5 NAS Transport Messages [176](#nas-transport-messages)

9.2.5.1 INITIAL UE MESSAGE [176](#initial-ue-message-1)

9.2.5.2 DOWNLINK NAS TRANSPORT [177](#downlink-nas-transport-1)

9.2.5.3 UPLINK NAS TRANSPORT [177](#uplink-nas-transport-1)

9.2.5.4 NAS NON DELIVERY INDICATION [178](#nas-non-delivery-indication-1)

9.2.5.5 REROUTE NAS REQUEST [178](#reroute-nas-request-1)

9.2.6 Interface Management Messages [179](#interface-management-messages)

9.2.6.1 NG SETUP REQUEST [179](#ng-setup-request)

9.2.6.2 NG SETUP RESPONSE [180](#ng-setup-response)

9.2.6.3 NG SETUP FAILURE [181](#ng-setup-failure)

9.2.6.4 RAN CONFIGURATION UPDATE [181](#ran-configuration-update-1)

9.2.6.5 RAN CONFIGURATION UPDATE ACKNOWLEDGE [183](#ran-configuration-update-acknowledge)

9.2.6.6 RAN CONFIGURATION UPDATE FAILURE [183](#ran-configuration-update-failure)

9.2.6.7 AMF CONFIGURATION UPDATE [183](#amf-configuration-update-1)

9.2.6.8 AMF CONFIGURATION UPDATE ACKNOWLEDGE [185](#amf-configuration-update-acknowledge)

9.2.6.9 AMF CONFIGURATION UPDATE FAILURE [186](#amf-configuration-update-failure)

9.2.6.10 AMF STATUS INDICATION [186](#amf-status-indication-1)

9.2.6.11 NG RESET [186](#ng-reset-1)

9.2.6.12 NG RESET ACKNOWLEDGE [187](#ng-reset-acknowledge)

9.2.6.13 ERROR INDICATION [187](#error-indication-1)

9.2.6.14 OVERLOAD START [187](#overload-start-1)

9.2.6.15 OVERLOAD STOP [188](#overload-stop-1)

9.2.7 Configuration Transfer Messages [188](#configuration-transfer-messages)

9.2.7.1 UPLINK RAN CONFIGURATION TRANSFER [188](#uplink-ran-configuration-transfer-1)

9.2.7.2 DOWNLINK RAN CONFIGURATION TRANSFER [189](#downlink-ran-configuration-transfer-1)

9.2.8 Warning Message Transmission Messages [189](#warning-message-transmission-messages)

9.2.8.1 WRITE-REPLACE WARNING REQUEST [189](#write-replace-warning-request)

9.2.8.2 WRITE-REPLACE WARNING RESPONSE [189](#write-replace-warning-response)

9.2.8.3 PWS CANCEL REQUEST [190](#pws-cancel-request)

9.2.8.4 PWS CANCEL RESPONSE [190](#pws-cancel-response)

9.2.8.5 PWS RESTART INDICATION [190](#pws-restart-indication-1)

9.2.8.6 PWS FAILURE INDICATION [191](#pws-failure-indication-1)

9.2.9 NRPPa Transport Messages [192](#nrppa-transport-messages)

9.2.9.1 DOWNLINK UE ASSOCIATED NRPPA TRANSPORT [192](#downlink-ue-associated-nrppa-transport-1)

9.2.9.2 UPLINK UE ASSOCIATED NRPPA TRANSPORT [192](#uplink-ue-associated-nrppa-transport-1)

9.2.9.3 DOWNLINK NON UE ASSOCIATED NRPPA TRANSPORT [192](#downlink-non-ue-associated-nrppa-transport-1)

9.2.9.4 UPLINK NON UE ASSOCIATED NRPPA TRANSPORT [192](#uplink-non-ue-associated-nrppa-transport-1)

9.2.10 Trace Messages [193](#trace-messages)

9.2.10.1 TRACE START [193](#trace-start-1)

9.2.10.2 TRACE FAILURE INDICATION [193](#trace-failure-indication-1)

9.2.10.3 DEACTIVATE TRACE [193](#deactivate-trace-1)

9.2.10.4 CELL TRAFFIC TRACE [193](#cell-traffic-trace-1)

9.2.11 Location Reporting Messages [194](#location-reporting-messages)

9.2.11.1 LOCATION REPORTING CONTROL [194](#location-reporting-control-1)

9.2.11.2 LOCATION REPORTING FAILURE INDICATION [194](#location-reporting-failure-indication-1)

9.2.11.3 LOCATION REPORT [195](#location-report-1)

9.2.12 UE TNLA Binding Messages [195](#ue-tnla-binding-messages)

9.2.12.1 UE TNLA BINDING RELEASE REQUEST [195](#ue-tnla-binding-release-request)

9.2.13 UE Radio Capability Management Messages [195](#ue-radio-capability-management-messages)

9.2.13.1 UE RADIO CAPABILITY INFO INDICATION [195](#ue-radio-capability-info-indication-1)

9.2.13.2 UE RADIO CAPABILITY CHECK REQUEST [196](#ue-radio-capability-check-request)

9.2.13.3 UE RADIO CAPABILITY CHECK RESPONSE [196](#ue-radio-capability-check-response)

9.2.13.4 UE RADIO CAPABILITY ID MAPPING REQUEST [196](#ue-radio-capability-id-mapping-request)

9.2.13.5 UE RADIO CAPABILITY ID MAPPING RESPONSE [197](#ue-radio-capability-id-mapping-response)

9.2.14 Data Usage Reporting Messages [197](#data-usage-reporting-messages)

9.2.14.1 SECONDARY RAT DATA USAGE REPORT [197](#secondary-rat-data-usage-report-1)

9.2.15 RIM Information Transfer Messages [197](#rim-information-transfer-messages)

9.2.15.1 UPLINK RIM INFORMATION TRANSFER [197](#uplink-rim-information-transfer-1)

9.2.15.2 DOWNLINK RIM INFORMATION TRANSFER [198](#downlink-rim-information-transfer-1)

9.2.16 Broadcast Session Management Messages [198](#broadcast-session-management-messages)

9.2.16.1 BROADCAST SESSION SETUP REQUEST [198](#broadcast-session-setup-request)

9.2.16.2 BROADCAST SESSION SETUP RESPONSE [198](#broadcast-session-setup-response)

9.2.16.3 BROADCAST SESSION SETUP FAILURE [199](#broadcast-session-setup-failure)

9.2.16.4 BROADCAST SESSION MODIFICATION REQUEST [199](#broadcast-session-modification-request)

9.2.16.5 BROADCAST SESSION MODIFICATION RESPONSE [199](#broadcast-session-modification-response)

9.2.16.6 BROADCAST SESSION MODIFICATION FAILURE [200](#broadcast-session-modification-failure)

9.2.16.7 BROADCAST SESSION RELEASE REQUEST [200](#broadcast-session-release-request)

9.2.16.8 BROADCAST SESSION RELEASE RESPONSE [200](#broadcast-session-release-response)

9.2.16.9 BROADCAST SESSION RELEASE REQUIRED [200](#broadcast-session-release-required-1)

9.2.16.10 BROADCAST SESSION TRANSPORT REQUEST [201](#broadcast-session-transport-request)

9.2.16.11 BROADCAST SESSION TRANSPORT RESPONSE [201](#_Toc241287943)

9.2.16.12 BROADCAST SESSION TRANSPORT FAILURE [201](#_Toc241287944)

9.2.17 Multicast Session Management Messages [202](#multicast-session-management-messages)

9.2.17.1 DISTRIBUTION SETUP REQUEST [202](#distribution-setup-request)

9.2.17.2 DISTRIBUTION SETUP RESPONSE [202](#distribution-setup-response)

9.2.17.3 DISTRIBUTION SETUP FAILURE [202](#distribution-setup-failure)

9.2.17.4 DISTRIBUTION RELEASE REQUEST [203](#distribution-release-request)

9.2.17.5 DISTRIBUTION RELEASE RESPONSE [203](#distribution-release-response)

9.2.17.6 MULTICAST SESSION ACTIVATION REQUEST [203](#multicast-session-activation-request)

9.2.17.7 MULTICAST SESSION ACTIVATION RESPONSE [203](#multicast-session-activation-response)

9.2.17.8 MULTICAST SESSION ACTIVATION FAILURE [204](#multicast-session-activation-failure)

9.2.17.9 MULTICAST SESSION DEACTIVATION REQUEST [204](#multicast-session-deactivation-request)

9.2.17.10 MULTICAST SESSION DEACTIVATION RESPONSE [204](#multicast-session-deactivation-response)

9.2.17.11 MULTICAST SESSION UPDATE REQUEST [204](#multicast-session-update-request)

9.2.17.12 MULTICAST SESSION UPDATE RESPONSE [205](#multicast-session-update-response)

9.2.17.13 MULTICAST SESSION UPDATE FAILURE [205](#multicast-session-update-failure)

9.2.18 Timing Synchronisation Status Reporting Messages [205](#timing-synchronisation-status-reporting-messages)

9.2.18.1 TIMING SYNCHRONISATION STATUS REQUEST [205](#timing-synchronisation-status-request)

9.2.18.2 TIMING SYNCHRONISATION STATUS RESPONSE [206](#timing-synchronisation-status-response)

9.2.18.3 TIMING SYNCHRONISATION STATUS FAILURE [206](#timing-synchronisation-status-failure)

9.2.18.4 TIMING SYNCHRONISATION STATUS REPORT [206](#timing-synchronisation-status-report-1)

9.3 Information Element Definitions [206](#information-element-definitions)

9.3.1 Radio Network Layer Related IEs [206](#radio-network-layer-related-ies)

9.3.1.1 Message Type [206](#message-type)

9.3.1.2 Cause [207](#cause)

9.3.1.3 Criticality Diagnostics [213](#criticality-diagnostics)

9.3.1.4 Bit Rate [214](#bit-rate)

9.3.1.5 Global RAN Node ID [214](#global-ran-node-id)

9.3.1.6 Global gNB ID [214](#global-gnb-id)

9.3.1.7 NR CGI [214](#nr-cgi)

9.3.1.8 Global ng-eNB ID [215](#global-ng-enb-id)

9.3.1.9 E-UTRA CGI [215](#e-utra-cgi)

9.3.1.10 GBR QoS Flow Information [215](#gbr-qos-flow-information)

9.3.1.11 Void [216](#void)

9.3.1.12 QoS Flow Level QoS Parameters [216](#qos-flow-level-qos-parameters)

9.3.1.13 QoS Flow List with Cause [217](#qos-flow-list-with-cause)

9.3.1.14 Trace Activation [218](#trace-activation)

9.3.1.15 Core Network Assistance Information for RRC INACTIVE [219](#core-network-assistance-information-for-rrc-inactive)

9.3.1.16 User Location Information [220](#user-location-information)

9.3.1.17 Slice Support List [222](#slice-support-list)

9.3.1.18 Dynamic 5QI Descriptor [222](#dynamic-5qi-descriptor)

9.3.1.19 Allocation and Retention Priority [224](#allocation-and-retention-priority)

9.3.1.20 Source to Target Transparent Container [224](#source-to-target-transparent-container)

9.3.1.21 Target to Source Transparent Container [225](#target-to-source-transparent-container)

9.3.1.22 Handover Type [225](#handover-type)

9.3.1.23 MICO Mode Indication [226](#mico-mode-indication)

9.3.1.24 S-NSSAI [226](#s-nssai)

9.3.1.25 Target ID [226](#target-id)

9.3.1.26 Emergency Fallback Indicator [227](#emergency-fallback-indicator)

9.3.1.27 Security Indication [227](#security-indication)

9.3.1.28 Non Dynamic 5QI Descriptor [228](#non-dynamic-5qi-descriptor)

9.3.1.29 Source NG-RAN Node to Target NG-RAN Node Transparent Container [229](#source-ng-ran-node-to-target-ng-ran-node-transparent-container)

9.3.1.30 Target NG-RAN Node to Source NG-RAN Node Transparent Container [233](#target-ng-ran-node-to-source-ng-ran-node-transparent-container)

9.3.1.31 Allowed NSSAI [235](#allowed-nssai)

9.3.1.32 Relative AMF Capacity [235](#relative-amf-capacity)

9.3.1.33 DL Forwarding [235](#dl-forwarding)

9.3.1.34 DRBs to QoS Flows Mapping List [235](#drbs-to-qos-flows-mapping-list)

9.3.1.35 Message Identifier [236](#message-identifier)

9.3.1.36 Serial Number [236](#serial-number)

9.3.1.37 Warning Area List [236](#warning-area-list)

9.3.1.38 Number of Broadcasts Requested [236](#number-of-broadcasts-requested)

9.3.1.39 Warning Type [237](#warning-type)

9.3.1.40 Void [237](#void-1)

9.3.1.41 Data Coding Scheme [237](#data-coding-scheme)

9.3.1.42 Warning Message Contents [237](#warning-message-contents)

9.3.1.43 Broadcast Completed Area List [237](#broadcast-completed-area-list)

9.3.1.44 Broadcast Cancelled Area List [238](#broadcast-cancelled-area-list)

9.3.1.45 Number of Broadcasts [240](#number-of-broadcasts)

9.3.1.46 Concurrent Warning Message Indicator [240](#concurrent-warning-message-indicator)

9.3.1.47 Cancel-All Warning Messages Indicator [240](#cancel-all-warning-messages-indicator)

9.3.1.48 Emergency Area ID [240](#emergency-area-id)

9.3.1.49 Repetition Period [240](#repetition-period)

9.3.1.50 PDU Session ID [241](#pdu-session-id)

9.3.1.51 QoS Flow Identifier [241](#qos-flow-identifier)

9.3.1.52 PDU Session Type [241](#pdu-session-type)

9.3.1.53 DRB ID [241](#drb-id)

9.3.1.54 Masked IMEISV [241](#masked-imeisv)

9.3.1.55 New Security Context Indicator [242](#new-security-context-indicator)

9.3.1.56 Time to Wait [242](#time-to-wait)

9.3.1.57 Global N3IWF ID [242](#global-n3iwf-id)

9.3.1.58 UE Aggregate Maximum Bit Rate [242](#ue-aggregate-maximum-bit-rate)

9.3.1.59 Security Result [243](#security-result)

9.3.1.60 User Plane Security Information [243](#user-plane-security-information)

9.3.1.61 Index to RAT/Frequency Selection Priority [243](#index-to-ratfrequency-selection-priority)

9.3.1.62 Data Forwarding Accepted [243](#data-forwarding-accepted)

9.3.1.63 Data Forwarding Not Possible [243](#data-forwarding-not-possible)

9.3.1.64 Direct Forwarding Path Availability [244](#direct-forwarding-path-availability)

9.3.1.65 Location Reporting Request Type [244](#location-reporting-request-type)

9.3.1.66 Area of Interest [246](#area-of-interest)

9.3.1.67 UE Presence in Area of Interest List [246](#ue-presence-in-area-of-interest-list)

9.3.1.68 UE Radio Capability for Paging [246](#ue-radio-capability-for-paging)

9.3.1.69 Assistance Data for Paging [247](#assistance-data-for-paging)

9.3.1.70 Assistance Data for Recommended Cells [247](#assistance-data-for-recommended-cells)

9.3.1.71 Recommended Cells for Paging [247](#recommended-cells-for-paging)

9.3.1.72 Paging Attempt Information [247](#paging-attempt-information)

9.3.1.73 NG-RAN CGI [248](#ng-ran-cgi)

9.3.1.74 UE Radio Capability [248](#ue-radio-capability)

9.3.1.74a UE Radio Capability – E-UTRA Format [248](#a-ue-radio-capability-e-utra-format)

9.3.1.75 Time Stamp [248](#time-stamp)

9.3.1.76 Location Reporting Reference ID [249](#location-reporting-reference-id)

9.3.1.77 Data Forwarding Response DRB List [249](#data-forwarding-response-drb-list)

9.3.1.78 Paging Priority [249](#paging-priority)

9.3.1.79 Packet Loss Rate [249](#packet-loss-rate)

9.3.1.80 Packet Delay Budget [249](#packet-delay-budget)

9.3.1.81 Packet Error Rate [250](#packet-error-rate)

9.3.1.82 Averaging Window [250](#averaging-window)

9.3.1.83 Maximum Data Burst Volume [250](#maximum-data-burst-volume)

9.3.1.84 Priority Level [250](#priority-level)

9.3.1.85 Mobility Restriction List [250](#mobility-restriction-list)

9.3.1.86 UE Security Capabilities [252](#ue-security-capabilities)

9.3.1.87 Security Key [254](#security-key)

9.3.1.88 Security Context [254](#security-context)

9.3.1.89 IMS Voice Support Indicator [254](#ims-voice-support-indicator)

9.3.1.90 Paging DRX [254](#paging-drx)

9.3.1.91 RRC Inactive Transition Report Request [255](#rrc-inactive-transition-report-request)

9.3.1.92 RRC State [255](#rrc-state)

9.3.1.93 Expected UE Behaviour [255](#expected-ue-behaviour)

9.3.1.94 Expected UE Activity Behaviour [256](#expected-ue-activity-behaviour)

9.3.1.95 UE History Information [257](#ue-history-information)

9.3.1.96 Last Visited Cell Information [257](#last-visited-cell-information)

9.3.1.97 Last Visited NG-RAN Cell Information [258](#last-visited-ng-ran-cell-information)

9.3.1.98 Cell Type [259](#cell-type)

9.3.1.99 Associated QoS Flow List [259](#associated-qos-flow-list)

9.3.1.100 Information on Recommended Cells and RAN Nodes for Paging [259](#information-on-recommended-cells-and-ran-nodes-for-paging)

9.3.1.101 Recommended RAN Nodes for Paging [259](#recommended-ran-nodes-for-paging)

9.3.1.102 PDU Session Aggregate Maximum Bit Rate [260](#pdu-session-aggregate-maximum-bit-rate)

9.3.1.103 Maximum Integrity Protected Data Rate [260](#maximum-integrity-protected-data-rate)

9.3.1.104 Overload Response [260](#overload-response)

9.3.1.105 Overload Action [261](#overload-action)

9.3.1.106 Traffic Load Reduction Indication [261](#traffic-load-reduction-indication)

9.3.1.107 Slice Overload List [261](#slice-overload-list)

9.3.1.108 RAN Status Transfer Transparent Container [261](#ran-status-transfer-transparent-container)

9.3.1.109 COUNT Value for PDCP SN Length 12 [263](#count-value-for-pdcp-sn-length-12)

9.3.1.110 COUNT Value for PDCP SN Length 18 [263](#count-value-for-pdcp-sn-length-18)

9.3.1.111 RRC Establishment Cause [263](#rrc-establishment-cause)

9.3.1.112 Warning Area Coordinates [264](#warning-area-coordinates)

9.3.1.113 Network Instance [264](#network-instance)

9.3.1.114 Secondary RAT Usage Information [264](#secondary-rat-usage-information)

9.3.1.115 Volume Timed Report List [265](#volume-timed-report-list)

9.3.1.116 Redirection for Voice EPS Fallback [265](#redirection-for-voice-eps-fallback)

9.3.1.117 UE Retention Information [266](#ue-retention-information)

9.3.1.118 UL Forwarding [266](#ul-forwarding)

9.3.1.119 CN Assisted RAN Parameters Tuning [266](#cn-assisted-ran-parameters-tuning)

9.3.1.120 Common Network Instance [266](#common-network-instance)

9.3.1.121 Data Forwarding Response E-RAB List [266](#data-forwarding-response-e-rab-list)

9.3.1.122 gNB Set ID [267](#gnb-set-id)

9.3.1.123 RNC-ID [267](#rnc-id)

9.3.1.124 Extended RNC-ID [267](#extended-rnc-id)

9.3.1.125 RAT Information [267](#rat-information)

9.3.1.126 Extended RAT Restriction Information [267](#extended-rat-restriction-information)

9.3.1.127 SgNB UE X2AP ID [268](#sgnb-ue-x2ap-id)

9.3.1.128 SRVCC Operation Possible [268](#srvcc-operation-possible)

9.3.1.129 IAB Authorized [268](#iab-authorized)

9.3.1.130 TSC Traffic Characteristics [268](#tsc-traffic-characteristics)

9.3.1.131 TSC Assistance Information [269](#tsc-assistance-information)

9.3.1.132 Periodicity [269](#periodicity)

9.3.1.133 Burst Arrival Time [269](#burst-arrival-time)

9.3.1.134 Redundant QoS Flow Indicator [269](#redundant-qos-flow-indicator)

9.3.1.135 Extended Packet Delay Budget [270](#extended-packet-delay-budget)

9.3.1.136 Redundant PDU Session Information [270](#redundant-pdu-session-information)

9.3.1.137 NB-IoT Default Paging DRX [270](#_Toc241288103)

9.3.1.138 NB-IoT Paging eDRX Information [270](#_Toc241288104)

9.3.1.139 NB-IoT Paging DRX [271](#nb-iot-paging-drx)

9.3.1.140 Enhanced Coverage Restriction [271](#_Toc241288106)

9.3.1.141 Paging Assistance Data for CE Capable UE [271](#paging-assistance-data-for-ce-capable-ue)

9.3.1.142 UE Radio Capability ID [271](#ue-radio-capability-id)

9.3.1.143 WUS Assistance Information [272](#wus-assistance-information)

9.3.1.144 UE Differentiation Information [272](#ue-differentiation-information)

9.3.1.145 NB-IoT UE Priority [274](#nb-iot-ue-priority)

9.3.1.146 NR V2X Services Authorized [274](#nr-v2x-services-authorized)

9.3.1.147 LTE V2X Services Authorized [274](#lte-v2x-services-authorized)

9.3.1.148 NR UE Sidelink Aggregate Maximum Bit Rate [274](#nr-ue-sidelink-aggregate-maximum-bit-rate)

9.3.1.149 LTE UE Sidelink Aggregate Maximum Bit Rate [274](#lte-ue-sidelink-aggregate-maximum-bit-rate)

9.3.1.150 PC5 QoS Parameters [275](#pc5-qos-parameters)

9.3.1.151 Alternative QoS Parameters Set List [275](#alternative-qos-parameters-set-list)

9.3.1.152 Alternative QoS Parameters Set Index [276](#alternative-qos-parameters-set-index)

9.3.1.153 Alternative QoS Parameters Set Notify Index [276](#alternative-qos-parameters-set-notify-index)

9.3.1.154 E-UTRA Paging eDRX Information [276](#e-utra-paging-edrx-information)

9.3.1.155 CE-mode-B Restricted [276](#ce-mode-b-restricted)

9.3.1.156 CE-mode-B Support Indicator [277](#ce-mode-b-support-indicator)

9.3.1.157 LTE-M Indication [277](#lte-m-indication)

9.3.1.158 Suspend Request Indication [277](#suspend-request-indication)

9.3.1.159 Suspend Response Indication [277](#suspend-response-indication)

9.3.1.160 UE User Plane CIoT Support Indicator [277](#ue-user-plane-ciot-support-indicator)

9.3.1.161 Global TNGF ID [278](#global-tngf-id)

9.3.1.162 Global W-AGF ID [278](#global-w-agf-id)

9.3.1.163 Global TWIF ID [278](#global-twif-id)

9.3.1.164 W-AGF User Location Information [279](#w-agf-user-location-information)

9.3.1.165 Global eNB ID [280](#global-enb-id)

9.3.1.166 UE History Information from UE [280](#ue-history-information-from-ue)

9.3.1.167 MDT Configuration [280](#mdt-configuration)

9.3.1.168 MDT PLMN List [281](#mdt-plmn-list)

9.3.1.169 MDT Configuration-NR [281](#mdt-configuration-nr)

9.3.1.170 MDT Configuration-EUTRA [285](#mdt-configuration-eutra)

9.3.1.171 M1 Configuration [285](#m1-configuration)

9.3.1.172 M4 Configuration [287](#m4-configuration)

9.3.1.173 M5 Configuration [287](#m5-configuration)

9.3.1.174 M6 Configuration [288](#m6-configuration)

9.3.1.175 M7 Configuration [288](#_Toc241288141)

9.3.1.176 MDT Location Information [288](#mdt-location-information)

9.3.1.177 Bluetooth Measurement Configuration [289](#bluetooth-measurement-configuration)

9.3.1.178 WLAN Measurement Configuration [289](#wlan-measurement-configuration)

9.3.1.179 Sensor Measurement Configuration [289](#sensor-measurement-configuration)

9.3.1.180 Event Trigger Logged MDT Configuration [290](#event-trigger-logged-mdt-configuration)

9.3.1.181 NR Frequency Info [291](#nr-frequency-info)

9.3.1.182 Area Scope of Neighbour Cells [291](#area-scope-of-neighbour-cells)

9.3.1.183 NPN Paging Assistance Information [291](#npn-paging-assistance-information)

9.3.1.184 NPN Mobility Information [292](#_Toc241288150)

9.3.1.185 Cell CAG Information [292](#cell-cag-information)

9.3.1.186 Target to Source Failure Transparent Container [293](#target-to-source-failure-transparent-container)

9.3.1.187 Target NG-RAN Node to Source NG-RAN Node Failure Transparent Container [293](#target-ng-ran-node-to-source-ng-ran-node-failure-transparent-container)

9.3.1.188 DAPS Request Information [293](#daps-request-information)

9.3.1.189 DAPS Response Information [293](#daps-response-information)

9.3.1.190 Early Status Transfer Transparent Container [294](#early-status-transfer-transparent-container)

9.3.1.191 Extended Slice Support List [295](#extended-slice-support-list)

9.3.1.192 UE Capability Info Request [295](#ue-capability-info-request)

9.3.1.193 Extended RAN Node Name [295](#extended-ran-node-name)

9.3.1.194 MICO All PLMN [295](#mico-all-plmn)

9.3.1.195 Source Node ID [296](#source-node-id)

9.3.1.196 E-UTRAN Composite Available Capacity Group [296](#e-utran-composite-available-capacity-group)

9.3.1.197 E-UTRAN Composite Available Capacity [296](#e-utran-composite-available-capacity)

9.3.1.198 E-UTRAN Cell Capacity Class Value [296](#_Toc241288164)

9.3.1.199 E-UTRAN Capacity Value [296](#e-utran-capacity-value)

9.3.1.200 E-UTRAN Radio Resource Status [297](#e-utran-radio-resource-status)

9.3.1.201 Void [297](#_Toc241288167)

9.3.1.202 Void [297](#void-3)

9.3.1.203 Void [297](#void-4)

9.3.1.204 Void [297](#void-5)

9.3.1.205 NR Radio Resource Status [297](#nr-radio-resource-status)

9.3.1.206 MBS Session ID [298](#mbs-session-id)

9.3.1.207 MBS Area Session ID [298](#mbs-area-session-id)

9.3.1.208 MBS Service Area [298](#mbs-service-area)

9.3.1.209 MBS Service Area Information [299](#mbs-service-area-information)

9.3.1.210 MBS Support Indicator [299](#mbs-support-indicator)

9.3.1.211 MBS Session Setup Request List [299](#mbs-session-setup-request-list)

9.3.1.212 MBS Session Setup or Modify Request List [300](#mbs-session-setup-or-modify-request-list)

9.3.1.213 MBS Session Setup Response List [301](#mbs-session-setup-response-list)

9.3.1.214 MBS Session Failed to Setup List [301](#mbs-session-failed-to-setup-list)

9.3.1.215 MBS Session To Release List [302](#mbs-session-to-release-list)

9.3.1.216 Multicast Group Paging Area [302](#multicast-group-paging-area)

9.3.1.217 MBS Session Status [302](#mbs-session-status)

9.3.1.218 MRB ID [303](#mrb-id)

9.3.1.219 MRB Progress Information [303](#mrb-progress-information)

9.3.1.220 Time Synchronisation Assistance Information [303](#time-synchronisation-assistance-information)

9.3.1.221 Survival Time [303](#survival-time)

9.3.1.222 QMC Deactivation [303](#qmc-deactivation)

9.3.1.223 QMC Configuration Information [304](#_Toc241288189)

9.3.1.224 UE Application Layer Measurement Configuration Information [304](#ue-application-layer-measurement-configuration-information)

9.3.1.225 Available RAN Visible QoE Metrics [307](#available-ran-visible-qoe-metrics)

9.3.1.226 Void [308](#void-6)

9.3.1.227 NR Paging eDRX Information [308](#nr-paging-edrx-information)

9.3.1.228 RedCap Indication [308](#redcap-indication)

9.3.1.229 Target NSSAI Information [308](#target-nssai-information)

9.3.1.230 Target NSSAI [308](#target-nssai)

9.3.1.231 UE Slice Maximum Bit Rate List [309](#ue-slice-maximum-bit-rate-list)

9.3.1.232 PEIPS Assistance Information [309](#peips-assistance-information)

9.3.1.233 5G ProSe Authorized [309](#g-prose-authorized)

9.3.1.234 5G ProSe PC5 QoS Parameters [310](#g-prose-pc5-qos-parameters)

9.3.1.235 Last Visited PSCell Information [311](#last-visited-pscell-information)

9.3.1.236 MBS QoS Flows To Be Setup List [311](#mbs-qos-flows-to-be-setup-list)

9.3.1.237 Reporting System [312](#reporting-system)

9.3.1.238 TAI NSAG Support List [312](#tai-nsag-support-list)

9.3.1.239 NGAP Protocol IE-Id [312](#ngap-protocol-ie-id)

9.3.1.240 NGAP Protocol IE Support Information [312](#ngap-protocol-ie-support-information)

9.3.1.241 NGAP Protocol IE Presence Information [313](#ngap-protocol-ie-presence-information)

9.3.1.242 NGAP IE Support Information Response List [313](#ngap-ie-support-information-response-list)

9.3.1.243 MDT PLMN Modification List [313](#mdt-plmn-modification-list)

9.3.1.244 Excess Packet Delay Threshold Configuration [313](#excess-packet-delay-threshold-configuration)

9.3.1.245 Network Controlled Repeater Authorized [314](#network-controlled-repeater-authorized)

9.3.1.246 Aerial UE Subscription Information [314](#aerial-ue-subscription-information)

9.3.1.247 NR A2X Services Authorized [314](#nr-a2x-services-authorized)

9.3.1.248 LTE A2X Services Authorized [314](#lte-a2x-services-authorized)

9.3.1.249 A2X PC5 QoS Parameters [315](#a2x-pc5-qos-parameters)

9.3.1.250 Clock Quality Reporting Control Information [315](#clock-quality-reporting-control-information)

9.3.1.251 Clock Quality Acceptance Criteria [315](#clock-quality-acceptance-criteria)

9.3.1.252 RAN Timing Synchronisation Status Information [316](#ran-timing-synchronisation-status-information)

9.3.1.253 Clock Accuracy [316](#clock-accuracy)

9.3.1.254 RAN TSS Scope [317](#ran-tss-scope)

9.3.1.255 Burst Arrival Time Window [317](#burst-arrival-time-window)

9.3.1.256 Periodicity Range [317](#periodicity-range)

9.3.1.257 TSC Traffic Characteristics Feedback [318](#tsc-traffic-characteristics-feedback)

9.3.1.258 TSC Feedback Information [318](#tsc-feedback-information)

9.3.1.259 Mobile IAB Authorized [318](#mobile-iab-authorized)

9.3.1.260 Mobile IAB-MT User Location Information [318](#mobile-iab-mt-user-location-information)

9.3.1.261 Partially Allowed NSSAI [319](#partially-allowed-nssai)

9.3.1.262 Associated Session ID [319](#associated-session-id)

9.3.1.263 MBS Assistance Information [319](#mbs-assistance-information)

9.3.1.264 PDU Set QoS Information [319](#pdu-set-qos-information)

9.3.1.265 N6 Jitter Information [320](#n6-jitter-information)

9.3.1.266 ECN Marking or Congestion Information Reporting Request [320](#ecn-marking-or-congestion-information-reporting-request)

9.3.1.267 ECN Marking or Congestion Information Reporting Status [320](#_Toc241288233)

9.3.1.268 PDU Set based Handling Indicator [321](#pdu-set-based-handling-indicator)

9.3.1.269 Ranging and Sidelink Positioning Service Information [321](#ranging-and-sidelink-positioning-service-information)

9.3.1.270 RSPP Transport QoS Parameters [321](#rspp-transport-qos-parameters)

9.3.1.271 User Plane Failure Indication [322](#user-plane-failure-indication)

9.3.1.272 QoE and RVQoE Reporting Paths [322](#qoe-and-rvqoe-reporting-paths)

9.3.2 Transport Network Layer Related IEs [322](#transport-network-layer-related-ies)

9.3.2.1 QoS Flow per TNL Information List [322](#qos-flow-per-tnl-information-list)

9.3.2.2 UP Transport Layer Information [322](#up-transport-layer-information)

9.3.2.3 E-RAB ID [323](#e-rab-id)

9.3.2.4 Transport Layer Address [323](#transport-layer-address)

9.3.2.5 GTP-TEID [323](#gtp-teid)

9.3.2.6 CP Transport Layer Information [324](#cp-transport-layer-information)

9.3.2.7 TNL Association List [324](#tnl-association-list)

9.3.2.8 QoS Flow per TNL Information [324](#qos-flow-per-tnl-information)

9.3.2.9 TNL Association Usage [324](#tnl-association-usage)

9.3.2.10 TNL Address Weight Factor [325](#tnl-address-weight-factor)

9.3.2.11 UP Transport Layer Information Pair List [325](#up-transport-layer-information-pair-list)

9.3.2.12 UP Transport Layer Information List [325](#up-transport-layer-information-list)

9.3.2.13 QoS Flow List with Data Forwarding [325](#qos-flow-list-with-data-forwarding)

9.3.2.14 URI [326](#uri)

9.3.2.15 MBS Session TNL Information 5GC [326](#mbs-session-tnl-information-5gc)

9.3.2.16 Shared NG-U Multicast TNL Information [327](#shared-ng-u-multicast-tnl-information)

9.3.2.17 MBS Session TNL Information NG-RAN [327](#mbs-session-tnl-information-ng-ran)

9.3.2.18 MBS NG-U Failure Indication [327](#mbs-ng-u-failure-indication)

9.3.3 NAS Related IEs [328](#nas-related-ies)

9.3.3.1 AMF UE NGAP ID [328](#amf-ue-ngap-id)

9.3.3.2 RAN UE NGAP ID [328](#ran-ue-ngap-id)

9.3.3.3 GUAMI [328](#guami)

9.3.3.4 NAS-PDU [329](#nas-pdu)

9.3.3.5 PLMN Identity [329](#plmn-identity)

9.3.3.6 SON Configuration Transfer [329](#son-configuration-transfer)

9.3.3.7 SON Information [330](#son-information)

9.3.3.8 SON Information Reply [330](#son-information-reply)

9.3.3.9 Xn TNL Configuration Info [330](#xn-tnl-configuration-info)

9.3.3.10 TAC [331](#tac)

9.3.3.11 TAI [331](#tai)

9.3.3.12 AMF Set ID [332](#amf-set-id)

9.3.3.13 Routing ID [332](#routing-id)

9.3.3.14 NRPPa-PDU [332](#nrppa-pdu)

9.3.3.15 RAN Paging Priority [332](#ran-paging-priority)

9.3.3.16 EPS TAC [332](#eps-tac)

9.3.3.17 EPS TAI [333](#eps-tai)

9.3.3.18 UE Paging Identity [333](#ue-paging-identity)

9.3.3.19 AMF Pointer [333](#amf-pointer)

9.3.3.20 5G-S-TMSI [333](#g-s-tmsi)

9.3.3.21 AMF Name [333](#amf-name)

9.3.3.22 Paging Origin [333](#paging-origin)

9.3.3.23 UE Identity Index Value [334](#ue-identity-index-value)

9.3.3.24 Periodic Registration Update Timer [334](#periodic-registration-update-timer)

9.3.3.25 UE-associated Logical NG-connection List [334](#ue-associated-logical-ng-connection-list)

9.3.3.26 NAS Security Parameters from NG-RAN [335](#nas-security-parameters-from-ng-ran)

9.3.3.27 Source to Target AMF Information Reroute [335](#source-to-target-amf-information-reroute)

9.3.3.28 RIM Information Transfer [335](#rim-information-transfer)

9.3.3.29 RIM Information [336](#rim-information)

9.3.3.30 LAI [336](#lai)

9.3.3.31 Extended Connected Time [336](#extended-connected-time)

9.3.3.32 End Indication [336](#end-indication)

9.3.3.33 Inter-system SON Configuration Transfer [337](#inter-system-son-configuration-transfer)

9.3.3.34 Inter-system SON Information [337](#inter-system-son-information)

9.3.3.35 SON Information Report [338](#son-information-report)

9.3.3.36 Inter-system SON Information Report [338](#inter-system-son-information-report)

9.3.3.37 Failure Indication [339](#failure-indication)

9.3.3.38 Inter-system Failure Indication [339](#inter-system-failure-indication)

9.3.3.39 HO Report [339](#ho-report)

9.3.3.40 Inter-system HO Report [341](#inter-system-ho-report)

9.3.3.41 UE RLF Report Container [343](#ue-rlf-report-container)

9.3.3.42 NID [343](#nid)

9.3.3.43 CAG ID [343](#cag-id)

9.3.3.44 NPN Support [344](#npn-support)

9.3.3.45 Allowed PNI-NPN List [344](#allowed-pni-npn-list)

9.3.3.46 NPN Access Information [344](#npn-access-information)

9.3.3.47 Cell CAG List [345](#cell-cag-list)

9.3.3.48 UL CP Security Information [345](#ul-cp-security-information)

9.3.3.49 DL CP Security Information [345](#_Toc241288307)

9.3.3.50 Configured TAC Indication [345](#configured-tac-indication)

9.3.3.51 Extended AMF Name [345](#extended-amf-name)

9.3.3.52 Extended UE Identity Index Value [346](#extended-ue-identity-index-value)

9.3.3.53 NR NTN TAI Information [346](#nr-ntn-tai-information)

9.3.3.54 Inter-system SON Information Request [346](#inter-system-son-information-request)

9.3.3.55 Inter-system SON Information Reply [346](#inter-system-son-information-reply)

9.3.3.56 Inter-system Cell Activation Request [347](#inter-system-cell-activation-request)

9.3.3.57 Inter-system Cell State Indication [347](#inter-system-cell-state-indication)

9.3.3.58 Inter-system Cell Activation Reply [347](#inter-system-cell-activation-reply)

9.3.3.59 Inter-system Resource Status Request [347](#inter-system-resource-status-request)

9.3.3.60 Inter-system Resource Status Report [349](#inter-system-resource-status-report)

9.3.3.61 Inter-system Resource Status Reply [349](#inter-system-resource-status-reply)

9.3.3.62 Hashed UE Identity Index Value [349](#hashed-ue-identity-index-value)

9.3.3.63 Paging Policy Differentiation [350](#paging-policy-differentiation)

9.3.3.64 NR Paging Long eDRX Information for RRC INACTIVE [350](#nr-paging-long-edrx-information-for-rrc-inactive)

9.3.3.65 CAG List for MDT [350](#cag-list-for-mdt)

9.3.3.66 AUN3 Device Access Information [351](#aun3-device-access-information)

9.3.4 SMF Related IEs [351](#smf-related-ies)

9.3.4.1 PDU Session Resource Setup Request Transfer [351](#pdu-session-resource-setup-request-transfer)

9.3.4.2 PDU Session Resource Setup Response Transfer [353](#pdu-session-resource-setup-response-transfer)

9.3.4.3 PDU Session Resource Modify Request Transfer [355](#pdu-session-resource-modify-request-transfer)

9.3.4.4 PDU Session Resource Modify Response Transfer [357](#pdu-session-resource-modify-response-transfer)

9.3.4.5 PDU Session Resource Notify Transfer [360](#pdu-session-resource-notify-transfer)

9.3.4.6 PDU Session Resource Modify Indication Transfer [362](#pdu-session-resource-modify-indication-transfer)

9.3.4.7 PDU Session Resource Modify Confirm Transfer [362](#pdu-session-resource-modify-confirm-transfer)

9.3.4.8 Path Switch Request Transfer [363](#path-switch-request-transfer)

9.3.4.9 Path Switch Request Acknowledge Transfer [365](#path-switch-request-acknowledge-transfer)

9.3.4.10 Handover Command Transfer [367](#handover-command-transfer)

9.3.4.11 Handover Request Acknowledge Transfer [368](#handover-request-acknowledge-transfer)

9.3.4.12 PDU Session Resource Release Command Transfer [370](#pdu-session-resource-release-command-transfer)

9.3.4.13 PDU Session Resource Notify Released Transfer [370](#pdu-session-resource-notify-released-transfer)

9.3.4.14 Handover Required Transfer [371](#handover-required-transfer)

9.3.4.15 Path Switch Request Setup Failed Transfer [371](#path-switch-request-setup-failed-transfer)

9.3.4.16 PDU Session Resource Setup Unsuccessful Transfer [371](#pdu-session-resource-setup-unsuccessful-transfer)

9.3.4.17 PDU Session Resource Modify Unsuccessful Transfer [371](#pdu-session-resource-modify-unsuccessful-transfer)

9.3.4.18 Handover Preparation Unsuccessful Transfer [371](#handover-preparation-unsuccessful-transfer)

9.3.4.19 Handover Resource Allocation Unsuccessful Transfer [371](#handover-resource-allocation-unsuccessful-transfer)

9.3.4.20 Path Switch Request Unsuccessful Transfer [372](#path-switch-request-unsuccessful-transfer)

9.3.4.21 PDU Session Resource Release Response Transfer [372](#pdu-session-resource-release-response-transfer)

9.3.4.22 PDU Session Resource Modify Indication Unsuccessful Transfer [372](#pdu-session-resource-modify-indication-unsuccessful-transfer)

9.3.4.23 Secondary RAT Data Usage Report Transfer [372](#secondary-rat-data-usage-report-transfer)

9.3.4.24 UE Context Resume Request Transfer [372](#ue-context-resume-request-transfer)

9.3.4.25 UE Context Resume Response Transfer [373](#ue-context-resume-response-transfer)

9.3.4.26 UE Context Suspend Request Transfer [373](#ue-context-suspend-request-transfer)

9.3.5 MB-SMF Related IEs [373](#mb-smf-related-ies)

9.3.5.1 Void [373](#void-7)

9.3.5.2 Void [373](#void-8)

9.3.5.3 MBS Session Setup or Modification Request Transfer [373](#mbs-session-setup-or-modification-request-transfer)

9.3.5.4 Void [374](#void-9)

9.3.5.5 MBS Session Setup or Modification Response Transfer [374](#mbs-session-setup-or-modification-response-transfer)

9.3.5.6 MBS Session Setup or Modification Failure Transfer [374](#mbs-session-setup-or-modification-failure-transfer)

9.3.5.7 MBS Distribution Setup Request Transfer [374](#mbs-distribution-setup-request-transfer)

9.3.5.8 MBS Distribution Setup Response Transfer [375](#mbs-distribution-setup-response-transfer)

9.3.5.9 MBS Distribution Setup Unsuccessful Transfer [375](#mbs-distribution-setup-unsuccessful-transfer)

9.3.5.10 MBS Distribution Release Request Transfer [375](#mbs-distribution-release-request-transfer)

9.3.5.11 Multicast Session Activation Request Transfer [375](#multicast-session-activation-request-transfer)

9.3.5.12 Multicast Session Deactivation Request Transfer [375](#multicast-session-deactivation-request-transfer)

9.3.5.13 Multicast Session Update Request Transfer [376](#multicast-session-update-request-transfer)

9.3.5.14 MBS Session Release Response Transfer [376](#mbs-session-release-response-transfer)

9.3.5.15 Broadcast Transport Request Transfer [376](#broadcast-transport-request-transfer)

9.3.5.16 Broadcast Transport Response Transfer [376](#_Toc241288368)

9.3.5.17 Broadcast Transport Failure Transfer [376](#broadcast-transport-failure-transfer)

9.4 Message and Information Element Abstract Syntax (with ASN.1) [377](#message-and-information-element-abstract-syntax-with-asn.1)

9.4.1 General [377](#general-79)

9.4.2 Usage of private message mechanism for non-standard use [377](#usage-of-private-message-mechanism-for-non-standard-use)

9.4.3 Elementary Procedure Definitions [378](#_Toc241288373)

9.4.4 PDU Definitions [396](#pdu-definitions)

9.4.5 Information Element Definitions [469](#information-element-definitions-1)

9.4.6 Common Definitions [628](#common-definitions)

9.4.7 Constant Definitions [629](#constant-definitions)

9.4.8 Container Definitions [642](#container-definitions)

9.5 Message Transfer Syntax [647](#_Toc241288379)

9.6 Timers [647](#timers)

10 Handling of Unknown, Unforeseen and Erroneous Protocol Data [648](#handling-of-unknown-unforeseen-and-erroneous-protocol-data)

10.1 General [648](#general-80)

10.2 Transfer Syntax Error [648](#transfer-syntax-error)

10.3 Abstract Syntax Error [648](#abstract-syntax-error)

10.3.1 General [648](#general-81)

10.3.2 Criticality Information [649](#criticality-information)

10.3.3 Presence Information [649](#presence-information)

10.3.4 Not comprehended IE/IE group [650](#not-comprehended-ieie-group)

10.3.4.1 Procedure Code [650](#procedure-code)

10.3.4.1A Type of Message [650](#a-type-of-message)

10.3.4.2 IEs other than the Procedure Code and Type of Message [650](#ies-other-than-the-procedure-code-and-type-of-message)

10.3.5 Missing IE or IE group [651](#missing-ie-or-ie-group)

10.3.6 IEs or IE groups received in wrong order or with too many occurrences or erroneously present [652](#ies-or-ie-groups-received-in-wrong-order-or-with-too-many-occurrences-or-erroneously-present)

10.4 Logical Error [653](#logical-error)

10.5 Exceptions [653](#exceptions)

10.6 Handling of AP ID [654](#handling-of-ap-id)

Annex A (informative): Change history [655](#annex-a-informative-change-history)

#  Foreword

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
