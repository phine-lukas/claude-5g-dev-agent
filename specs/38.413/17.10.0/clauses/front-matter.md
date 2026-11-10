3GPP TS 38.413 V17.10.0 (2024-09)

Technical Specification

3<sup>rd</sup> Generation Partnership Project;

Technical Specification Group Radio Access Network;

NG-RAN;

NG Application Protocol (NGAP)

(Release 17)

<img src="media/image1.jpeg" style="width:1.32569in;height:1.32569in" /> <img src="media/image2.png" style="width:1.77778in;height:1.03681in" />

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

© 2024, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC).

All rights reserved.

UMTS™ is a Trade Mark of ETSI registered for the benefit of its members

3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners  
LTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners

GSM® and the GSM logo are registered and owned by the GSM Association

#  Contents

Foreword [18](#foreword)

1 Scope [19](#scope)

2 References [19](#references)

3 Definitions and abbreviations [21](#definitions-and-abbreviations)

3.1 Definitions [21](#definitions)

3.2 Abbreviations [22](#abbreviations)

4 General [23](#general)

4.1 Procedure Specification Principles [23](#procedure-specification-principles)

4.2 Forwards and Backwards Compatibility [23](#forwards-and-backwards-compatibility)

4.3 Specification Notations [24](#specification-notations)

5 NGAP Services [24](#ngap-services)

6 Services Expected from Signalling Transport [24](#services-expected-from-signalling-transport)

7 Functions of NGAP [24](#functions-of-ngap)

8 NGAP Procedures [24](#ngap-procedures)

8.1 List of NGAP Elementary Procedures [24](#list-of-ngap-elementary-procedures)

8.2 PDU Session Management Procedures [27](#pdu-session-management-procedures)

8.2.1 PDU Session Resource Setup [27](#pdu-session-resource-setup)

8.2.1.1 General [27](#general-1)

8.2.1.2 Successful Operation [27](#successful-operation)

8.2.1.3 Unsuccessful Operation [31](#unsuccessful-operation)

8.2.1.4 Abnormal Conditions [31](#abnormal-conditions)

8.2.2 PDU Session Resource Release [31](#pdu-session-resource-release)

8.2.2.1 General [31](#general-2)

8.2.2.2 Successful Operation [32](#successful-operation-1)

8.2.2.3 Unsuccessful Operation [32](#unsuccessful-operation-1)

8.2.2.4 Abnormal Conditions [32](#abnormal-conditions-1)

8.2.3 PDU Session Resource Modify [33](#pdu-session-resource-modify)

8.2.3.1 General [33](#general-3)

8.2.3.2 Successful Operation [33](#successful-operation-2)

8.2.3.3 Unsuccessful Operation [36](#unsuccessful-operation-2)

8.2.3.4 Abnormal Conditions [36](#abnormal-conditions-2)

8.2.4 PDU Session Resource Notify [37](#pdu-session-resource-notify)

8.2.4.1 General [37](#general-4)

8.2.4.2 Successful Operation [37](#successful-operation-3)

8.2.4.3 Abnormal Conditions [38](#abnormal-conditions-3)

8.2.5 PDU Session Resource Modify Indication [38](#pdu-session-resource-modify-indication)

8.2.5.1 General [38](#general-5)

8.2.5.2 Successful Operation [38](#successful-operation-4)

8.2.5.3 Unsuccessful Operation [40](#unsuccessful-operation-3)

8.2.5.4 Abnormal Conditions [40](#abnormal-conditions-4)

8.3 UE Context Management Procedures [40](#ue-context-management-procedures)

8.3.1 Initial Context Setup [40](#initial-context-setup)

8.3.1.1 General [40](#general-6)

8.3.1.2 Successful Operation [40](#successful-operation-5)

8.3.1.3 Unsuccessful Operation [44](#unsuccessful-operation-4)

8.3.1.4 Abnormal Conditions [44](#abnormal-conditions-5)

8.3.2 UE Context Release Request (NG-RAN node initiated) [44](#ue-context-release-request-ng-ran-node-initiated)

8.3.2.1 General [44](#general-7)

8.3.2.2 Successful Operation [45](#successful-operation-6)

8.3.2.3 Abnormal Conditions [45](#abnormal-conditions-6)

8.3.3 UE Context Release (AMF initiated) [45](#ue-context-release-amf-initiated)

8.3.3.1 General [45](#general-8)

8.3.3.2 Successful Operation [45](#successful-operation-7)

8.3.3.3 Unsuccessful Operation [46](#unsuccessful-operation-5)

8.3.3.4 Abnormal Conditions [46](#abnormal-conditions-7)

8.3.4 UE Context Modification [46](#ue-context-modification)

8.3.4.1 General [46](#general-9)

8.3.4.2 Successful Operation [46](#successful-operation-8)

8.3.4.3 Unsuccessful Operation [49](#unsuccessful-operation-6)

8.3.4.4 Abnormal Conditions [49](#abnormal-conditions-8)

8.3.5 RRC Inactive Transition Report [49](#rrc-inactive-transition-report)

8.3.5.1 General [49](#general-10)

8.3.5.2 Successful Operation [50](#successful-operation-9)

8.3.5.3 Abnormal Conditions [50](#abnormal-conditions-9)

8.3.6 Connection Establishment Indication [50](#connection-establishment-indication)

8.3.6.1 General [50](#general-11)

8.3.6.2 Successful Operation [50](#successful-operation-10)

8.3.6.3 Abnormal Conditions [51](#abnormal-conditions-10)

8.3.7 AMF CP Relocation Indication [51](#amf-cp-relocation-indication)

8.3.7.1 General [51](#general-12)

8.3.7.2 Successful Operation [51](#successful-operation-11)

8.3.7.3 Abnormal Conditions [52](#abnormal-conditions-11)

8.3.8 RAN CP Relocation Indication [52](#ran-cp-relocation-indication)

8.3.8.1 General [52](#general-13)

8.3.8.2 Successful Operation [52](#successful-operation-12)

8.3.8.3 Abnormal Conditions [53](#abnormal-conditions-12)

8.3.9 Retrieve UE Information [53](#retrieve-ue-information)

8.3.9.1 General [53](#general-14)

8.3.9.2 Successful Operation [53](#successful-operation-13)

8.3.9.3 Abnormal Conditions [53](#abnormal-conditions-13)

8.3.10 UE Information Transfer [53](#ue-information-transfer)

8.3.10.1 General [53](#general-15)

8.3.10.2 Successful Operation [53](#successful-operation-14)

8.3.10.3 Abnormal Conditions [54](#abnormal-conditions-14)

8.3.11 UE Context Suspend [54](#ue-context-suspend)

8.3.11.1 General [54](#general-16)

8.3.11.2 Successful Operation [54](#successful-operation-15)

8.3.11.3 Unsuccessful Operation [55](#unsuccessful-operation-7)

8.3.11.4 Abnormal Conditions [55](#abnormal-conditions-15)

8.3.12 UE Context Resume [55](#ue-context-resume)

8.3.12.1 General [55](#general-17)

8.3.12.2 Successful Operation [56](#successful-operation-16)

8.3.12.3 Unsuccessful Operation [57](#unsuccessful-operation-8)

8.4 UE Mobility Management Procedures [57](#ue-mobility-management-procedures)

8.4.1 Handover Preparation [57](#handover-preparation)

8.4.1.1 General [57](#general-18)

8.4.1.2 Successful Operation [57](#successful-operation-17)

8.4.1.3 Unsuccessful Operation [59](#unsuccessful-operation-9)

8.4.1.4 Abnormal Conditions [60](#abnormal-conditions-16)

8.4.2 Handover Resource Allocation [60](#handover-resource-allocation)

8.4.2.1 General [60](#general-19)

8.4.2.2 Successful Operation [60](#successful-operation-18)

8.4.2.3 Unsuccessful Operation [67](#unsuccessful-operation-10)

8.4.2.4 Abnormal Conditions [67](#abnormal-conditions-17)

8.4.3 Handover Notification [68](#handover-notification)

8.4.3.1 General [68](#general-20)

8.4.3.2 Successful Operation [68](#successful-operation-19)

8.4.3.3 Abnormal Conditions [68](#abnormal-conditions-18)

8.4.4 Path Switch Request [68](#path-switch-request)

8.4.4.1 General [68](#general-21)

8.4.4.2 Successful Operation [69](#successful-operation-20)

8.4.4.3 Unsuccessful Operation [73](#unsuccessful-operation-11)

8.4.4.4 Abnormal Conditions [73](#abnormal-conditions-19)

8.4.5 Handover Cancellation [73](#handover-cancellation)

8.4.5.1 General [73](#general-22)

8.4.5.2 Successful Operation [74](#successful-operation-21)

8.4.5.3 Unsuccessful Operation [74](#unsuccessful-operation-12)

8.4.5.4 Abnormal Conditions [74](#abnormal-conditions-20)

8.4.6 Uplink RAN Status Transfer [74](#uplink-ran-status-transfer)

8.4.6.1 General [74](#general-23)

8.4.6.2 Successful Operation [74](#successful-operation-22)

8.4.6.3 Abnormal Conditions [75](#abnormal-conditions-21)

8.4.7 Downlink RAN Status Transfer [75](#downlink-ran-status-transfer)

8.4.7.1 General [75](#general-24)

8.4.7.2 Successful Operation [75](#successful-operation-23)

8.4.7.3 Abnormal Conditions [75](#abnormal-conditions-22)

8.4.8 Handover Success [75](#handover-success)

8.4.8.1 General [75](#general-25)

8.4.8.2 Successful Operation [76](#successful-operation-24)

8.4.8.3 Abnormal Conditions [76](#abnormal-conditions-23)

8.4.9 Uplink RAN Early Status Transfer [76](#uplink-ran-early-status-transfer)

8.4.9.1 General [76](#general-26)

8.4.9.2 Successful Operation [76](#successful-operation-25)

8.4.9.3 Abnormal Conditions [76](#abnormal-conditions-24)

8.4.10 Downlink RAN Early Status Transfer [77](#downlink-ran-early-status-transfer)

8.4.10.1 General [77](#general-27)

8.4.10.2 Successful Operation [77](#successful-operation-26)

8.4.10.3 Abnormal Conditions [77](#abnormal-conditions-25)

8.5 Paging Procedures [77](#paging-procedures)

8.5.1 Paging [77](#paging)

8.5.1.1 General [77](#general-28)

8.5.1.2 Successful Operation [77](#successful-operation-27)

8.5.1.3 Abnormal Conditions [79](#abnormal-conditions-26)

8.5.2 Multicast Group Paging [79](#multicast-group-paging)

8.5.2.1 General [79](#general-29)

8.5.2.2 Successful Operation [79](#successful-operation-28)

8.5.2.3 Abnormal Conditions [79](#abnormal-conditions-27)

8.6 Transport of NAS Messages Procedures [79](#transport-of-nas-messages-procedures)

8.6.1 Initial UE Message [79](#initial-ue-message)

8.6.1.1 General [79](#general-30)

8.6.1.2 Successful Operation [80](#successful-operation-29)

8.6.1.3 Abnormal Conditions [81](#abnormal-conditions-28)

8.6.2 Downlink NAS Transport [81](#downlink-nas-transport)

8.6.2.1 General [81](#general-31)

8.6.2.2 Successful Operation [81](#successful-operation-30)

8.6.2.3 Abnormal Conditions [82](#abnormal-conditions-29)

8.6.3 Uplink NAS Transport [83](#uplink-nas-transport)

8.6.3.1 General [83](#general-32)

8.6.3.2 Successful Operation [83](#successful-operation-31)

8.6.3.3 Abnormal Conditions [83](#abnormal-conditions-30)

8.6.4 NAS Non Delivery Indication [83](#nas-non-delivery-indication)

8.6.4.1 General [83](#general-33)

8.6.4.2 Successful Operation [83](#successful-operation-32)

8.6.4.3 Abnormal Conditions [84](#abnormal-conditions-31)

8.6.5 Reroute NAS Request [84](#reroute-nas-request)

8.6.5.1 General [84](#general-34)

8.6.5.2 Successful Operation [84](#successful-operation-33)

8.6.5.3 Abnormal Conditions [84](#abnormal-conditions-32)

8.7 Interface Management Procedures [84](#interface-management-procedures)

8.7.1 NG Setup [84](#ng-setup)

8.7.1.1 General [84](#general-35)

8.7.1.2 Successful Operation [85](#successful-operation-34)

8.7.1.3 Unsuccessful Operation [86](#unsuccessful-operation-13)

8.7.1.4 Abnormal Conditions [86](#abnormal-conditions-33)

8.7.2 RAN Configuration Update [86](#ran-configuration-update)

8.7.2.1 General [86](#general-36)

8.7.2.2 Successful Operation [86](#successful-operation-35)

8.7.2.3 Unsuccessful Operation [87](#unsuccessful-operation-14)

8.7.2.4 Abnormal Conditions [88](#abnormal-conditions-34)

8.7.3 AMF Configuration Update [88](#amf-configuration-update)

8.7.3.1 General [88](#general-37)

8.7.3.2 Successful Operation [88](#successful-operation-36)

8.7.3.3 Unsuccessful Operation [90](#unsuccessful-operation-15)

8.7.3.4 Abnormal Conditions [90](#abnormal-conditions-35)

8.7.4 NG Reset [90](#ng-reset)

8.7.4.1 General [90](#general-38)

8.7.4.2 Successful Operation [90](#successful-operation-37)

8.7.4.2.1 NG Reset initiated by the AMF [90](#ng-reset-initiated-by-the-amf)

8.7.4.2.2 NG Reset initiated by the NG-RAN node [91](#ng-reset-initiated-by-the-ng-ran-node)

8.7.4.3 Unsuccessful Operation [92](#unsuccessful-operation-16)

8.7.4.4 Abnormal Conditions [92](#abnormal-conditions-36)

8.7.4.4.1 Abnormal Condition at the 5GC [92](#abnormal-condition-at-the-5gc)

8.7.4.4.2 Abnormal Condition at the NG-RAN [92](#abnormal-condition-at-the-ng-ran)

8.7.4.4.3 Crossing of NG RESET Messages [92](#crossing-of-ng-reset-messages)

8.7.5 Error Indication [93](#error-indication)

8.7.5.1 General [93](#general-39)

8.7.5.2 Successful Operation [93](#successful-operation-38)

8.7.5.3 Abnormal Conditions [93](#abnormal-conditions-37)

8.7.6 AMF Status Indication [93](#amf-status-indication)

8.7.6.1 General [93](#general-40)

8.7.6.2 Successful Operation [94](#successful-operation-39)

8.7.6.3 Abnormal Conditions [94](#abnormal-conditions-38)

8.7.7 Overload Start [94](#overload-start)

8.7.7.1 General [94](#general-41)

8.7.7.2 Successful Operation [94](#successful-operation-40)

8.7.7.3 Abnormal Conditions [95](#abnormal-conditions-39)

8.7.8 Overload Stop [95](#overload-stop)

8.7.8.1 General [95](#general-42)

8.7.8.2 Successful Operation [96](#successful-operation-41)

8.7.8.3 Abnormal Conditions [96](#abnormal-conditions-40)

8.8 Configuration Transfer Procedures [96](#configuration-transfer-procedures)

8.8.1 Uplink RAN Configuration Transfer [96](#uplink-ran-configuration-transfer)

8.8.1.1 General [96](#general-43)

8.8.1.2 Successful Operation [96](#successful-operation-42)

8.8.1.3 Abnormal Conditions [97](#abnormal-conditions-41)

8.8.2 Downlink RAN Configuration Transfer [97](#downlink-ran-configuration-transfer)

8.8.2.1 General [97](#general-44)

8.8.2.2 Successful Operation [97](#successful-operation-43)

8.8.2.3 Abnormal Conditions [98](#abnormal-conditions-42)

8.9 Warning Message Transmission Procedures [98](#warning-message-transmission-procedures)

8.9.1 Write-Replace Warning [98](#write-replace-warning)

8.9.1.1 General [98](#general-45)

8.9.1.2 Successful Operation [98](#successful-operation-44)

8.9.1.3 Unsuccessful Operation [99](#unsuccessful-operation-17)

8.9.1.4 Abnormal Conditions [99](#abnormal-conditions-43)

8.9.2 PWS Cancel [100](#pws-cancel)

8.9.2.1 General [100](#general-46)

8.9.2.2 Successful Operation [100](#successful-operation-45)

8.9.2.3 Unsuccessful Operation [100](#unsuccessful-operation-18)

8.9.2.4 Abnormal Conditions [100](#abnormal-conditions-44)

8.9.3 PWS Restart Indication [101](#pws-restart-indication)

8.9.3.1 General [101](#general-47)

8.9.3.2 Successful Operation [101](#successful-operation-46)

8.9.3.3 Abnormal Conditions [101](#abnormal-conditions-45)

8.9.4 PWS Failure Indication [101](#pws-failure-indication)

8.9.4.1 General [101](#general-48)

8.9.4.2 Successful Operation [101](#successful-operation-47)

8.9.4.3 Abnormal Conditions [102](#abnormal-conditions-46)

8.10 NRPPa Transport Procedures [102](#nrppa-transport-procedures)

8.10.1 General [102](#general-49)

8.10.2 Successful Operations [102](#successful-operations)

8.10.2.1 DOWNLINK UE ASSOCIATED NRPPA TRANSPORT [102](#downlink-ue-associated-nrppa-transport)

8.10.2.2 UPLINK UE ASSOCIATED NRPPA TRANSPORT [102](#uplink-ue-associated-nrppa-transport)

8.10.2.3 DOWNLINK NON UE ASSOCIATED NRPPA TRANSPORT [103](#downlink-non-ue-associated-nrppa-transport)

8.10.2.4 UPLINK NON UE ASSOCIATED NRPPA TRANSPORT [103](#uplink-non-ue-associated-nrppa-transport)

8.10.3 Unsuccessful Operations [103](#unsuccessful-operations)

8.10.4 Abnormal Conditions [103](#abnormal-conditions-47)

8.11 Trace Procedures [104](#trace-procedures)

8.11.1 Trace Start [104](#trace-start)

8.11.1.1 General [104](#general-50)

8.11.1.2 Successful Operation [104](#successful-operation-48)

8.11.1.3 Abnormal Conditions [105](#abnormal-conditions-48)

8.11.2 Trace Failure Indication [105](#trace-failure-indication)

8.11.2.1 General [105](#general-51)

8.11.2.2 Successful Operation [105](#successful-operation-49)

8.11.2.3 Abnormal Conditions [105](#abnormal-conditions-49)

8.11.3 Deactivate Trace [105](#deactivate-trace)

8.11.3.1 General [105](#general-52)

8.11.3.2 Successful Operation [105](#successful-operation-50)

8.11.3.3 Abnormal Conditions [106](#abnormal-conditions-50)

8.11.4 Cell Traffic Trace [106](#cell-traffic-trace)

8.11.4.1 General [106](#general-53)

8.11.4.2 Successful Operation [106](#successful-operation-51)

8.11.4.3 Abnormal Conditions [106](#abnormal-conditions-51)

8.12 Location Reporting Procedures [106](#location-reporting-procedures)

8.12.1 Location Reporting Control [106](#location-reporting-control)

8.12.1.1 General [106](#general-54)

8.12.1.2 Successful Operation [107](#successful-operation-52)

8.12.1.3 Abnormal Conditions [107](#abnormal-conditions-52)

8.12.2 Location Reporting Failure Indication [108](#location-reporting-failure-indication)

8.12.2.1 General [108](#general-55)

8.12.2.2 Successful Operation [108](#successful-operation-53)

8.12.2.3 Abnormal Conditions [108](#abnormal-conditions-53)

8.12.3 Location Report [108](#location-report)

8.12.3.1 General [108](#general-56)

8.12.3.2 Successful Operation [108](#successful-operation-54)

8.12.3.3 Abnormal Conditions [109](#abnormal-conditions-54)

8.13 UE TNLA Binding Procedures [109](#ue-tnla-binding-procedures)

8.13.1 UE TNLA Binding Release [109](#ue-tnla-binding-release)

8.13.1.1 General [109](#general-57)

8.13.1.2 Successful Operation [109](#successful-operation-55)

8.13.1.3 Abnormal Conditions [109](#abnormal-conditions-55)

8.14 UE Radio Capability Management Procedures [109](#ue-radio-capability-management-procedures)

8.14.1 UE Radio Capability Info Indication [109](#ue-radio-capability-info-indication)

8.14.1.1 General [109](#general-58)

8.14.1.2 Successful Operation [110](#successful-operation-56)

8.14.1.3 Abnormal Conditions [110](#abnormal-conditions-56)

8.14.2 UE Radio Capability Check [110](#ue-radio-capability-check)

8.14.2.1 General [110](#general-59)

8.14.2.2 Successful Operation [110](#successful-operation-57)

8.14.2.3 Unsuccessful Operation [111](#unsuccessful-operation-19)

8.14.2.4 Abnormal Conditions [111](#abnormal-conditions-57)

8.14.3 UE Radio Capability ID Mapping [111](#ue-radio-capability-id-mapping)

8.14.3.1 General [111](#general-60)

8.14.3.2 Successful Operation [111](#successful-operation-58)

8.14.3.3 Unsuccessful Operation [111](#unsuccessful-operation-20)

8.14.3.4 Abnormal Conditions [112](#abnormal-conditions-58)

8.15 Data Usage Reporting Procedures [112](#data-usage-reporting-procedures)

8.15.1 Secondary RAT Data Usage Report [112](#secondary-rat-data-usage-report)

8.15.1.1 General [112](#general-61)

8.15.1.2 Successful Operation [112](#successful-operation-59)

8.15.1.3 Abnormal Conditions [112](#abnormal-conditions-59)

8.16 RIM Information Transfer Procedures [112](#rim-information-transfer-procedures)

8.16.1 Uplink RIM Information Transfer [112](#uplink-rim-information-transfer)

8.16.1.1 General [112](#general-62)

8.16.1.2 Successful Operation [113](#successful-operation-60)

8.16.1.3 Abnormal Conditions [113](#abnormal-conditions-60)

8.16.2 Downlink RIM Information Transfer [113](#downlink-rim-information-transfer)

8.16.2.1 General [113](#general-63)

8.16.2.2 Successful Operation [113](#successful-operation-61)

8.16.2.3 Abnormal Conditions [113](#abnormal-conditions-61)

8.17 Broadcast Session Management Procedures [114](#broadcast-session-management-procedures)

8.17.1 Broadcast Session Setup [114](#broadcast-session-setup)

8.17.1.1 General [114](#general-64)

8.17.1.2 Successful Operation [114](#successful-operation-62)

8.17.1.3 Unsuccessful Operation [114](#unsuccessful-operation-21)

8.17.1.4 Abnormal Conditions [114](#abnormal-conditions-62)

8.17.2 Broadcast Session Modification [115](#broadcast-session-modification)

8.17.2.1 General [115](#general-65)

8.17.2.2 Successful Operation [115](#successful-operation-63)

8.17.2.3 Unsuccessful Operation [115](#unsuccessful-operation-22)

8.17.2.4 Abnormal Conditions [115](#abnormal-conditions-63)

8.17.3 Broadcast Session Release [116](#broadcast-session-release)

8.17.3.1 General [116](#general-66)

8.17.3.2 Successful Operation [116](#successful-operation-64)

8.17.3.3 Unsuccessful Operation [116](#unsuccessful-operation-23)

8.17.3.4 Abnormal Conditions [116](#abnormal-conditions-64)

8.17.4 Broadcast Session Release Required [116](#broadcast-session-release-required)

8.17.4.1 General [116](#general-67)

8.17.4.2 Successful Operation [117](#successful-operation-65)

8.17.4.3 Abnormal Conditions [117](#abnormal-conditions-65)

8.18 Multicast Session Management Procedures [117](#multicast-session-management-procedures)

8.18.1 Distribution Setup [117](#distribution-setup)

8.18.1.1 General [117](#general-68)

8.18.1.2 Successful Operation [117](#successful-operation-66)

8.18.1.3 Unsuccessful Operation [118](#unsuccessful-operation-24)

8.18.1.4 Abnormal Conditions [118](#abnormal-conditions-66)

8.18.2 Distribution Release [118](#distribution-release)

8.18.2.1 General [118](#general-69)

8.18.2.2 Successful Operation [118](#successful-operation-67)

8.18.2.3 Unsuccessful Operation [119](#unsuccessful-operation-25)

8.18.2.4 Abnormal Conditions [119](#abnormal-conditions-67)

8.18.3 Multicast Session Activation [119](#multicast-session-activation)

8.18.3.1 General [119](#general-70)

8.18.3.2 Successful Operation [119](#successful-operation-68)

8.18.3.3 Unsuccessful Operation [120](#unsuccessful-operation-26)

8.18.3.4 Abnormal Conditions [120](#abnormal-conditions-68)

8.18.4 Multicast Session Deactivation [120](#multicast-session-deactivation)

8.18.4.1 General [120](#general-71)

8.18.4.2 Successful Operation [120](#successful-operation-69)

8.18.4.3 Unsuccessful Operation [121](#unsuccessful-operation-27)

8.18.4.4 Abnormal Conditions [121](#abnormal-conditions-69)

8.18.5 Multicast Session Update [121](#multicast-session-update)

8.18.5.1 General [121](#general-72)

8.18.5.2 Successful Operation [121](#successful-operation-70)

8.18.5.3 Unsuccessful Operation [122](#unsuccessful-operation-28)

8.18.5.4 Abnormal Conditions [122](#abnormal-conditions-70)

9 Elements for NGAP Communication [122](#elements-for-ngap-communication)

9.0 General [122](#general-73)

9.1 Tabular Format Contents [122](#tabular-format-contents)

9.1.1 Presence [122](#presence)

9.1.2 Criticality [123](#criticality)

9.1.3 Range [123](#range)

9.1.4 Assigned Criticality [123](#assigned-criticality)

9.2 Message Functional Definition and Content [123](#message-functional-definition-and-content)

9.2.1 PDU Session Management Messages [123](#pdu-session-management-messages)

9.2.1.1 PDU SESSION RESOURCE SETUP REQUEST [123](#pdu-session-resource-setup-request)

9.2.1.2 PDU SESSION RESOURCE SETUP RESPONSE [124](#pdu-session-resource-setup-response)

9.2.1.3 PDU SESSION RESOURCE RELEASE COMMAND [125](#pdu-session-resource-release-command)

9.2.1.4 PDU SESSION RESOURCE RELEASE RESPONSE [126](#pdu-session-resource-release-response)

9.2.1.5 PDU SESSION RESOURCE MODIFY REQUEST [126](#pdu-session-resource-modify-request)

9.2.1.6 PDU SESSION RESOURCE MODIFY RESPONSE [128](#pdu-session-resource-modify-response)

9.2.1.7 PDU SESSION RESOURCE NOTIFY [128](#pdu-session-resource-notify-1)

9.2.1.8 PDU SESSION RESOURCE MODIFY INDICATION [129](#pdu-session-resource-modify-indication-1)

9.2.1.9 PDU SESSION RESOURCE MODIFY CONFIRM [130](#pdu-session-resource-modify-confirm)

9.2.2 UE Context Management Messages [130](#ue-context-management-messages)

9.2.2.1 INITIAL CONTEXT SETUP REQUEST [130](#initial-context-setup-request)

9.2.2.2 INITIAL CONTEXT SETUP RESPONSE [132](#initial-context-setup-response)

9.2.2.3 INITIAL CONTEXT SETUP FAILURE [133](#initial-context-setup-failure)

9.2.2.4 UE CONTEXT RELEASE REQUEST [134](#ue-context-release-request)

9.2.2.5 UE CONTEXT RELEASE COMMAND [134](#ue-context-release-command)

9.2.2.6 UE CONTEXT RELEASE COMPLETE [135](#ue-context-release-complete)

9.2.2.7 UE CONTEXT MODIFICATION REQUEST [135](#ue-context-modification-request)

9.2.2.8 UE CONTEXT MODIFICATION RESPONSE [137](#ue-context-modification-response)

9.2.2.9 UE CONTEXT MODIFICATION FAILURE [137](#ue-context-modification-failure)

9.2.2.10 RRC INACTIVE TRANSITION REPORT [137](#rrc-inactive-transition-report-1)

9.2.2.11 CONNECTION ESTABLISHMENT INDICATION [137](#connection-establishment-indication-1)

9.2.2.12 AMF CP RELOCATION INDICATION [138](#amf-cp-relocation-indication-1)

9.2.2.13 RAN CP RELOCATION INDICATION [138](#ran-cp-relocation-indication-1)

9.2.2.14 RETRIEVE UE INFORMATION [138](#retrieve-ue-information-1)

9.2.2.15 UE INFORMATION TRANSFER [139](#ue-information-transfer-1)

9.2.2.16 UE CONTEXT SUSPEND REQUEST [139](#ue-context-suspend-request)

9.2.2.17 UE CONTEXT SUSPEND RESPONSE [140](#ue-context-suspend-response)

9.2.2.18 UE CONTEXT SUSPEND FAILURE [140](#ue-context-suspend-failure)

9.2.2.19 UE CONTEXT RESUME REQUEST [140](#ue-context-resume-request)

9.2.2.20 UE CONTEXT RESUME RESPONSE [141](#ue-context-resume-response)

9.2.2.21 UE CONTEXT RESUME FAILURE [142](#ue-context-resume-failure)

9.2.3 UE Mobility Management Messages [142](#ue-mobility-management-messages)

9.2.3.1 HANDOVER REQUIRED [142](#handover-required)

9.2.3.2 HANDOVER COMMAND [143](#handover-command)

9.2.3.3 HANDOVER PREPARATION FAILURE [144](#handover-preparation-failure)

9.2.3.4 HANDOVER REQUEST [145](#handover-request)

9.2.3.5 HANDOVER REQUEST ACKNOWLEDGE [147](#handover-request-acknowledge)

9.2.3.6 HANDOVER FAILURE [148](#handover-failure)

9.2.3.7 HANDOVER NOTIFY [149](#handover-notify)

9.2.3.8 PATH SWITCH REQUEST [150](#path-switch-request-1)

9.2.3.9 PATH SWITCH REQUEST ACKNOWLEDGE [151](#path-switch-request-acknowledge)

9.2.3.10 PATH SWITCH REQUEST FAILURE [154](#path-switch-request-failure)

9.2.3.11 HANDOVER CANCEL [154](#handover-cancel)

9.2.3.12 HANDOVER CANCEL ACKNOWLEDGE [154](#handover-cancel-acknowledge)

9.2.3.13 UPLINK RAN STATUS TRANSFER [155](#uplink-ran-status-transfer-1)

9.2.3.14 DOWNLINK RAN STATUS TRANSFER [155](#downlink-ran-status-transfer-1)

9.2.3.15 HANDOVER SUCCESS [155](#handover-success-1)

9.2.3.16 UPLINK RAN EARLY STATUS TRANSFER [155](#uplink-ran-early-status-transfer-1)

9.2.3.17 DOWNLINK RAN EARLY STATUS TRANSFER [156](#downlink-ran-early-status-transfer-1)

9.2.4 Paging Messages [156](#paging-messages)

9.2.4.1 PAGING [156](#paging-1)

9.2.4.2 MULTICAST GROUP PAGING [157](#multicast-group-paging-1)

9.2.5 NAS Transport Messages [158](#nas-transport-messages)

9.2.5.1 INITIAL UE MESSAGE [158](#initial-ue-message-1)

9.2.5.2 DOWNLINK NAS TRANSPORT [159](#downlink-nas-transport-1)

9.2.5.3 UPLINK NAS TRANSPORT [159](#uplink-nas-transport-1)

9.2.5.4 NAS NON DELIVERY INDICATION [160](#nas-non-delivery-indication-1)

9.2.5.5 REROUTE NAS REQUEST [160](#reroute-nas-request-1)

9.2.6 Interface Management Messages [160](#interface-management-messages)

9.2.6.1 NG SETUP REQUEST [160](#ng-setup-request)

9.2.6.2 NG SETUP RESPONSE [161](#ng-setup-response)

9.2.6.3 NG SETUP FAILURE [162](#ng-setup-failure)

9.2.6.4 RAN CONFIGURATION UPDATE [162](#ran-configuration-update-1)

9.2.6.5 RAN CONFIGURATION UPDATE ACKNOWLEDGE [164](#ran-configuration-update-acknowledge)

9.2.6.6 RAN CONFIGURATION UPDATE FAILURE [164](#ran-configuration-update-failure)

9.2.6.7 AMF CONFIGURATION UPDATE [164](#amf-configuration-update-1)

9.2.6.8 AMF CONFIGURATION UPDATE ACKNOWLEDGE [166](#amf-configuration-update-acknowledge)

9.2.6.9 AMF CONFIGURATION UPDATE FAILURE [166](#amf-configuration-update-failure)

9.2.6.10 AMF STATUS INDICATION [167](#amf-status-indication-1)

9.2.6.11 NG RESET [167](#ng-reset-1)

9.2.6.12 NG RESET ACKNOWLEDGE [167](#ng-reset-acknowledge)

9.2.6.13 ERROR INDICATION [168](#error-indication-1)

9.2.6.14 OVERLOAD START [168](#overload-start-1)

9.2.6.15 OVERLOAD STOP [168](#overload-stop-1)

9.2.7 Configuration Transfer Messages [169](#configuration-transfer-messages)

9.2.7.1 UPLINK RAN CONFIGURATION TRANSFER [169](#uplink-ran-configuration-transfer-1)

9.2.7.2 DOWNLINK RAN CONFIGURATION TRANSFER [169](#downlink-ran-configuration-transfer-1)

9.2.8 Warning Message Transmission Messages [169](#warning-message-transmission-messages)

9.2.8.1 WRITE-REPLACE WARNING REQUEST [169](#write-replace-warning-request)

9.2.8.2 WRITE-REPLACE WARNING RESPONSE [170](#write-replace-warning-response)

9.2.8.3 PWS CANCEL REQUEST [170](#pws-cancel-request)

9.2.8.4 PWS CANCEL RESPONSE [170](#pws-cancel-response)

9.2.8.5 PWS RESTART INDICATION [171](#pws-restart-indication-1)

9.2.8.6 PWS FAILURE INDICATION [171](#pws-failure-indication-1)

9.2.9 NRPPa Transport Messages [172](#nrppa-transport-messages)

9.2.9.1 DOWNLINK UE ASSOCIATED NRPPA TRANSPORT [172](#downlink-ue-associated-nrppa-transport-1)

9.2.9.2 UPLINK UE ASSOCIATED NRPPA TRANSPORT [172](#uplink-ue-associated-nrppa-transport-1)

9.2.9.3 DOWNLINK NON UE ASSOCIATED NRPPA TRANSPORT [173](#downlink-non-ue-associated-nrppa-transport-1)

9.2.9.4 UPLINK NON UE ASSOCIATED NRPPA TRANSPORT [173](#uplink-non-ue-associated-nrppa-transport-1)

9.2.10 Trace Messages [173](#trace-messages)

9.2.10.1 TRACE START [173](#trace-start-1)

9.2.10.2 TRACE FAILURE INDICATION [173](#trace-failure-indication-1)

9.2.10.3 DEACTIVATE TRACE [173](#deactivate-trace-1)

9.2.10.4 CELL TRAFFIC TRACE [174](#cell-traffic-trace-1)

9.2.11 Location Reporting Messages [174](#location-reporting-messages)

9.2.11.1 LOCATION REPORTING CONTROL [174](#location-reporting-control-1)

9.2.11.2 LOCATION REPORTING FAILURE INDICATION [175](#location-reporting-failure-indication-1)

9.2.11.3 LOCATION REPORT [175](#location-report-1)

9.2.12 UE TNLA Binding Messages [175](#ue-tnla-binding-messages)

9.2.12.1 UE TNLA BINDING RELEASE REQUEST [175](#ue-tnla-binding-release-request)

9.2.13 UE Radio Capability Management Messages [176](#ue-radio-capability-management-messages)

9.2.13.1 UE RADIO CAPABILITY INFO INDICATION [176](#ue-radio-capability-info-indication-1)

9.2.13.2 UE RADIO CAPABILITY CHECK REQUEST [176](#ue-radio-capability-check-request)

9.2.13.3 UE RADIO CAPABILITY CHECK RESPONSE [176](#ue-radio-capability-check-response)

9.2.13.4 UE RADIO CAPABILITY ID MAPPING REQUEST [176](#ue-radio-capability-id-mapping-request)

9.2.13.5 UE RADIO CAPABILITY ID MAPPING RESPONSE [177](#ue-radio-capability-id-mapping-response)

9.2.14 Data Usage Reporting Messages [177](#data-usage-reporting-messages)

9.2.14.1 SECONDARY RAT DATA USAGE REPORT [177](#secondary-rat-data-usage-report-1)

9.2.15 RIM Information Transfer Messages [177](#rim-information-transfer-messages)

9.2.15.1 UPLINK RIM INFORMATION TRANSFER [177](#uplink-rim-information-transfer-1)

9.2.15.2 DOWNLINK RIM INFORMATION TRANSFER [178](#downlink-rim-information-transfer-1)

9.2.16 Broadcast Session Management Messages [178](#broadcast-session-management-messages)

9.2.16.1 BROADCAST SESSION SETUP REQUEST [178](#broadcast-session-setup-request)

9.2.16.2 BROADCAST SESSION SETUP RESPONSE [178](#broadcast-session-setup-response)

9.2.16.3 BROADCAST SESSION SETUP FAILURE [179](#broadcast-session-setup-failure)

9.2.16.4 BROADCAST SESSION MODIFICATION REQUEST [179](#broadcast-session-modification-request)

9.2.16.5 BROADCAST SESSION MODIFICATION RESPONSE [179](#broadcast-session-modification-response)

9.2.16.6 BROADCAST SESSION MODIFICATION FAILURE [180](#broadcast-session-modification-failure)

9.2.16.7 BROADCAST SESSION RELEASE REQUEST [180](#broadcast-session-release-request)

9.2.16.8 BROADCAST SESSION RELEASE RESPONSE [180](#broadcast-session-release-response)

9.2.16.9 BROADCAST SESSION RELEASE REQUIRED [180](#broadcast-session-release-required-1)

9.2.17 Multicast Session Management Messages [181](#multicast-session-management-messages)

9.2.17.1 DISTRIBUTION SETUP REQUEST [181](#distribution-setup-request)

9.2.17.2 DISTRIBUTION SETUP RESPONSE [181](#distribution-setup-response)

9.2.17.3 DISTRIBUTION SETUP FAILURE [181](#distribution-setup-failure)

9.2.17.4 DISTRIBUTION RELEASE REQUEST [182](#distribution-release-request)

9.2.17.5 DISTRIBUTION RELEASE RESPONSE [182](#distribution-release-response)

9.2.17.6 MULTICAST SESSION ACTIVATION REQUEST [182](#multicast-session-activation-request)

9.2.17.7 MULTICAST SESSION ACTIVATION RESPONSE [183](#multicast-session-activation-response)

9.2.17.8 MULTICAST SESSION ACTIVATION FAILURE [183](#multicast-session-activation-failure)

9.2.17.9 MULTICAST SESSION DEACTIVATION REQUEST [183](#multicast-session-deactivation-request)

9.2.17.10 MULTICAST SESSION DEACTIVATION RESPONSE [184](#multicast-session-deactivation-response)

9.2.17.11 MULTICAST SESSION UPDATE REQUEST [184](#multicast-session-update-request)

9.2.17.12 MULTICAST SESSION UPDATE RESPONSE [184](#multicast-session-update-response)

9.2.17.13 MULTICAST SESSION UPDATE FAILURE [184](#multicast-session-update-failure)

9.3 Information Element Definitions [185](#information-element-definitions)

9.3.1 Radio Network Layer Related IEs [185](#radio-network-layer-related-ies)

9.3.1.1 Message Type [185](#message-type)

9.3.1.2 Cause [185](#cause)

9.3.1.3 Criticality Diagnostics [191](#criticality-diagnostics)

9.3.1.4 Bit Rate [191](#bit-rate)

9.3.1.5 Global RAN Node ID [192](#global-ran-node-id)

9.3.1.6 Global gNB ID [192](#global-gnb-id)

9.3.1.7 NR CGI [192](#nr-cgi)

9.3.1.8 Global ng-eNB ID [193](#global-ng-enb-id)

9.3.1.9 E-UTRA CGI [193](#e-utra-cgi)

9.3.1.10 GBR QoS Flow Information [193](#gbr-qos-flow-information)

9.3.1.11 Void [194](#void)

9.3.1.12 QoS Flow Level QoS Parameters [194](#qos-flow-level-qos-parameters)

9.3.1.13 QoS Flow List with Cause [195](#qos-flow-list-with-cause)

9.3.1.14 Trace Activation [196](#trace-activation)

9.3.1.15 Core Network Assistance Information for RRC INACTIVE [197](#core-network-assistance-information-for-rrc-inactive)

9.3.1.16 User Location Information [197](#user-location-information)

9.3.1.17 Slice Support List [199](#slice-support-list)

9.3.1.18 Dynamic 5QI Descriptor [199](#dynamic-5qi-descriptor)

9.3.1.19 Allocation and Retention Priority [201](#allocation-and-retention-priority)

9.3.1.20 Source to Target Transparent Container [201](#source-to-target-transparent-container)

9.3.1.21 Target to Source Transparent Container [202](#target-to-source-transparent-container)

9.3.1.22 Handover Type [202](#handover-type)

9.3.1.23 MICO Mode Indication [203](#mico-mode-indication)

9.3.1.24 S-NSSAI [203](#s-nssai)

9.3.1.25 Target ID [203](#target-id)

9.3.1.26 Emergency Fallback Indicator [204](#emergency-fallback-indicator)

9.3.1.27 Security Indication [204](#security-indication)

9.3.1.28 Non Dynamic 5QI Descriptor [204](#non-dynamic-5qi-descriptor)

9.3.1.29 Source NG-RAN Node to Target NG-RAN Node Transparent Container [205](#source-ng-ran-node-to-target-ng-ran-node-transparent-container)

9.3.1.30 Target NG-RAN Node to Source NG-RAN Node Transparent Container [208](#target-ng-ran-node-to-source-ng-ran-node-transparent-container)

9.3.1.31 Allowed NSSAI [210](#allowed-nssai)

9.3.1.32 Relative AMF Capacity [210](#relative-amf-capacity)

9.3.1.33 DL Forwarding [210](#dl-forwarding)

9.3.1.34 DRBs to QoS Flows Mapping List [210](#drbs-to-qos-flows-mapping-list)

9.3.1.35 Message Identifier [211](#message-identifier)

9.3.1.36 Serial Number [211](#serial-number)

9.3.1.37 Warning Area List [211](#warning-area-list)

9.3.1.38 Number of Broadcasts Requested [211](#number-of-broadcasts-requested)

9.3.1.39 Warning Type [212](#warning-type)

9.3.1.40 Void [212](#void-1)

9.3.1.41 Data Coding Scheme [212](#data-coding-scheme)

9.3.1.42 Warning Message Contents [212](#warning-message-contents)

9.3.1.43 Broadcast Completed Area List [212](#broadcast-completed-area-list)

9.3.1.44 Broadcast Cancelled Area List [213](#broadcast-cancelled-area-list)

9.3.1.45 Number of Broadcasts [215](#number-of-broadcasts)

9.3.1.46 Concurrent Warning Message Indicator [215](#concurrent-warning-message-indicator)

9.3.1.47 Cancel-All Warning Messages Indicator [215](#cancel-all-warning-messages-indicator)

9.3.1.48 Emergency Area ID [215](#emergency-area-id)

9.3.1.49 Repetition Period [215](#repetition-period)

9.3.1.50 PDU Session ID [216](#pdu-session-id)

9.3.1.51 QoS Flow Identifier [216](#qos-flow-identifier)

9.3.1.52 PDU Session Type [216](#pdu-session-type)

9.3.1.53 DRB ID [216](#drb-id)

9.3.1.54 Masked IMEISV [216](#masked-imeisv)

9.3.1.55 New Security Context Indicator [217](#new-security-context-indicator)

9.3.1.56 Time to Wait [217](#time-to-wait)

9.3.1.57 Global N3IWF ID [217](#global-n3iwf-id)

9.3.1.58 UE Aggregate Maximum Bit Rate [217](#ue-aggregate-maximum-bit-rate)

9.3.1.59 Security Result [218](#security-result)

9.3.1.60 User Plane Security Information [218](#user-plane-security-information)

9.3.1.61 Index to RAT/Frequency Selection Priority [218](#index-to-ratfrequency-selection-priority)

9.3.1.62 Data Forwarding Accepted [218](#data-forwarding-accepted)

9.3.1.63 Data Forwarding Not Possible [218](#data-forwarding-not-possible)

9.3.1.64 Direct Forwarding Path Availability [219](#direct-forwarding-path-availability)

9.3.1.65 Location Reporting Request Type [219](#location-reporting-request-type)

9.3.1.66 Area of Interest [220](#area-of-interest)

9.3.1.67 UE Presence in Area of Interest List [220](#ue-presence-in-area-of-interest-list)

9.3.1.68 UE Radio Capability for Paging [220](#ue-radio-capability-for-paging)

9.3.1.69 Assistance Data for Paging [221](#assistance-data-for-paging)

9.3.1.70 Assistance Data for Recommended Cells [221](#assistance-data-for-recommended-cells)

9.3.1.71 Recommended Cells for Paging [221](#recommended-cells-for-paging)

9.3.1.72 Paging Attempt Information [221](#paging-attempt-information)

9.3.1.73 NG-RAN CGI [222](#ng-ran-cgi)

9.3.1.74 UE Radio Capability [222](#ue-radio-capability)

9.3.1.74a UE Radio Capability – E-UTRA Format [222](#a-ue-radio-capability-e-utra-format)

9.3.1.75 Time Stamp [222](#time-stamp)

9.3.1.76 Location Reporting Reference ID [223](#location-reporting-reference-id)

9.3.1.77 Data Forwarding Response DRB List [223](#data-forwarding-response-drb-list)

9.3.1.78 Paging Priority [223](#paging-priority)

9.3.1.79 Packet Loss Rate [223](#packet-loss-rate)

9.3.1.80 Packet Delay Budget [223](#packet-delay-budget)

9.3.1.81 Packet Error Rate [224](#packet-error-rate)

9.3.1.82 Averaging Window [224](#averaging-window)

9.3.1.83 Maximum Data Burst Volume [224](#maximum-data-burst-volume)

9.3.1.84 Priority Level [224](#priority-level)

9.3.1.85 Mobility Restriction List [224](#mobility-restriction-list)

9.3.1.86 UE Security Capabilities [226](#ue-security-capabilities)

9.3.1.87 Security Key [228](#security-key)

9.3.1.88 Security Context [228](#security-context)

9.3.1.89 IMS Voice Support Indicator [228](#ims-voice-support-indicator)

9.3.1.90 Paging DRX [228](#paging-drx)

9.3.1.91 RRC Inactive Transition Report Request [229](#rrc-inactive-transition-report-request)

9.3.1.92 RRC State [229](#rrc-state)

9.3.1.93 Expected UE Behaviour [229](#expected-ue-behaviour)

9.3.1.94 Expected UE Activity Behaviour [230](#expected-ue-activity-behaviour)

9.3.1.95 UE History Information [231](#ue-history-information)

9.3.1.96 Last Visited Cell Information [231](#last-visited-cell-information)

9.3.1.97 Last Visited NG-RAN Cell Information [232](#last-visited-ng-ran-cell-information)

9.3.1.98 Cell Type [232](#cell-type)

9.3.1.99 Associated QoS Flow List [233](#associated-qos-flow-list)

9.3.1.100 Information on Recommended Cells and RAN Nodes for Paging [233](#information-on-recommended-cells-and-ran-nodes-for-paging)

9.3.1.101 Recommended RAN Nodes for Paging [233](#recommended-ran-nodes-for-paging)

9.3.1.102 PDU Session Aggregate Maximum Bit Rate [234](#pdu-session-aggregate-maximum-bit-rate)

9.3.1.103 Maximum Integrity Protected Data Rate [234](#maximum-integrity-protected-data-rate)

9.3.1.104 Overload Response [234](#overload-response)

9.3.1.105 Overload Action [234](#overload-action)

9.3.1.106 Traffic Load Reduction Indication [235](#traffic-load-reduction-indication)

9.3.1.107 Slice Overload List [235](#slice-overload-list)

9.3.1.108 RAN Status Transfer Transparent Container [235](#ran-status-transfer-transparent-container)

9.3.1.109 COUNT Value for PDCP SN Length 12 [237](#count-value-for-pdcp-sn-length-12)

9.3.1.110 COUNT Value for PDCP SN Length 18 [237](#count-value-for-pdcp-sn-length-18)

9.3.1.111 RRC Establishment Cause [237](#rrc-establishment-cause)

9.3.1.112 Warning Area Coordinates [238](#warning-area-coordinates)

9.3.1.113 Network Instance [238](#network-instance)

9.3.1.114 Secondary RAT Usage Information [238](#secondary-rat-usage-information)

9.3.1.115 Volume Timed Report List [239](#volume-timed-report-list)

9.3.1.116 Redirection for Voice EPS Fallback [239](#redirection-for-voice-eps-fallback)

9.3.1.117 UE Retention Information [240](#ue-retention-information)

9.3.1.118 UL Forwarding [240](#ul-forwarding)

9.3.1.119 CN Assisted RAN Parameters Tuning [240](#cn-assisted-ran-parameters-tuning)

9.3.1.120 Common Network Instance [240](#common-network-instance)

9.3.1.121 Data Forwarding Response E-RAB List [240](#data-forwarding-response-e-rab-list)

9.3.1.122 gNB Set ID [241](#gnb-set-id)

9.3.1.123 RNC-ID [241](#rnc-id)

9.3.1.124 Extended RNC-ID [241](#extended-rnc-id)

9.3.1.125 RAT Information [241](#rat-information)

9.3.1.126 Extended RAT Restriction Information [241](#extended-rat-restriction-information)

9.3.1.127 SgNB UE X2AP ID [242](#sgnb-ue-x2ap-id)

9.3.1.128 SRVCC Operation Possible [242](#srvcc-operation-possible)

9.3.1.129 IAB Authorized [242](#iab-authorized)

9.3.1.130 TSC Traffic Characteristics [242](#tsc-traffic-characteristics)

9.3.1.131 TSC Assistance Information [243](#tsc-assistance-information)

9.3.1.132 Periodicity [243](#periodicity)

9.3.1.133 Burst Arrival Time [243](#burst-arrival-time)

9.3.1.134 Redundant QoS Flow Indicator [243](#redundant-qos-flow-indicator)

9.3.1.135 Extended Packet Delay Budget [243](#extended-packet-delay-budget)

9.3.1.136 Redundant PDU Session Information [244](#redundant-pdu-session-information)

9.3.1.137 NB-IoT Default Paging DRX [244](#_Toc175580149)

9.3.1.138 NB-IoT Paging eDRX Information [244](#_Toc175580150)

9.3.1.139 NB-IoT Paging DRX [244](#nb-iot-paging-drx)

9.3.1.140 Enhanced Coverage Restriction [245](#_Toc175580152)

9.3.1.141 Paging Assistance Data for CE Capable UE [245](#paging-assistance-data-for-ce-capable-ue)

9.3.1.142 UE Radio Capability ID [245](#ue-radio-capability-id)

9.3.1.143 WUS Assistance Information [245](#wus-assistance-information)

9.3.1.144 UE Differentiation Information [245](#ue-differentiation-information)

9.3.1.145 NB-IoT UE Priority [247](#nb-iot-ue-priority)

9.3.1.146 NR V2X Services Authorized [247](#nr-v2x-services-authorized)

9.3.1.147 LTE V2X Services Authorized [247](#lte-v2x-services-authorized)

9.3.1.148 NR UE Sidelink Aggregate Maximum Bit Rate [247](#nr-ue-sidelink-aggregate-maximum-bit-rate)

9.3.1.149 LTE UE Sidelink Aggregate Maximum Bit Rate [247](#lte-ue-sidelink-aggregate-maximum-bit-rate)

9.3.1.150 PC5 QoS Parameters [248](#pc5-qos-parameters)

9.3.1.151 Alternative QoS Parameters Set List [248](#alternative-qos-parameters-set-list)

9.3.1.152 Alternative QoS Parameters Set Index [249](#alternative-qos-parameters-set-index)

9.3.1.153 Alternative QoS Parameters Set Notify Index [249](#alternative-qos-parameters-set-notify-index)

9.3.1.154 E-UTRA Paging eDRX Information [249](#e-utra-paging-edrx-information)

9.3.1.155 CE-mode-B Restricted [249](#ce-mode-b-restricted)

9.3.1.156 CE-mode-B Support Indicator [250](#ce-mode-b-support-indicator)

9.3.1.157 LTE-M Indication [250](#lte-m-indication)

9.3.1.158 Suspend Request Indication [250](#suspend-request-indication)

9.3.1.159 Suspend Response Indication [250](#suspend-response-indication)

9.3.1.160 UE User Plane CIoT Support Indicator [250](#ue-user-plane-ciot-support-indicator)

9.3.1.161 Global TNGF ID [251](#global-tngf-id)

9.3.1.162 Global W-AGF ID [251](#global-w-agf-id)

9.3.1.163 Global TWIF ID [251](#global-twif-id)

9.3.1.164 W-AGF User Location Information [252](#w-agf-user-location-information)

9.3.1.165 Global eNB ID [253](#global-enb-id)

9.3.1.166 UE History Information from UE [253](#ue-history-information-from-ue)

9.3.1.167 MDT Configuration [253](#mdt-configuration)

9.3.1.168 MDT PLMN List [253](#mdt-plmn-list)

9.3.1.169 MDT Configuration-NR [254](#mdt-configuration-nr)

9.3.1.170 MDT Configuration-EUTRA [257](#mdt-configuration-eutra)

9.3.1.171 M1 Configuration [257](#m1-configuration)

9.3.1.172 M4 Configuration [259](#m4-configuration)

9.3.1.173 M5 Configuration [259](#m5-configuration)

9.3.1.174 M6 Configuration [260](#m6-configuration)

9.3.1.175 M7 Configuration [260](#_Toc175580187)

9.3.1.176 MDT Location Information [261](#mdt-location-information)

9.3.1.177 Bluetooth Measurement Configuration [261](#bluetooth-measurement-configuration)

9.3.1.178 WLAN Measurement Configuration [261](#wlan-measurement-configuration)

9.3.1.179 Sensor Measurement Configuration [262](#sensor-measurement-configuration)

9.3.1.180 Event Trigger Logged MDT Configuration [262](#event-trigger-logged-mdt-configuration)

9.3.1.181 NR Frequency Info [263](#nr-frequency-info)

9.3.1.182 Area Scope of Neighbour Cells [264](#area-scope-of-neighbour-cells)

9.3.1.183 NPN Paging Assistance Information [264](#npn-paging-assistance-information)

9.3.1.184 NPN Mobility Information [264](#_Toc175580196)

9.3.1.185 Cell CAG Information [264](#cell-cag-information)

9.3.1.186 Target to Source Failure Transparent Container [265](#target-to-source-failure-transparent-container)

9.3.1.187 Target NG-RAN Node to Source NG-RAN Node Failure Transparent Container [265](#target-ng-ran-node-to-source-ng-ran-node-failure-transparent-container)

9.3.1.188 DAPS Request Information [265](#daps-request-information)

9.3.1.189 DAPS Response Information [265](#daps-response-information)

9.3.1.190 Early Status Transfer Transparent Container [266](#early-status-transfer-transparent-container)

9.3.1.191 Extended Slice Support List [266](#extended-slice-support-list)

9.3.1.192 UE Capability Info Request [266](#ue-capability-info-request)

9.3.1.193 Extended RAN Node Name [267](#extended-ran-node-name)

9.3.1.194 MICO All PLMN [267](#mico-all-plmn)

9.3.1.195 Source Node ID [267](#source-node-id)

9.3.1.196 E-UTRAN Composite Available Capacity Group [267](#e-utran-composite-available-capacity-group)

9.3.1.197 E-UTRAN Composite Available Capacity [267](#e-utran-composite-available-capacity)

9.3.1.198 E-UTRAN Cell Capacity Class Value [268](#_Toc175580210)

9.3.1.199 E-UTRAN Capacity Value [268](#e-utran-capacity-value)

9.3.1.200 E-UTRAN Radio Resource Status [268](#e-utran-radio-resource-status)

9.3.1.201 Void [269](#_Toc175580213)

9.3.1.202 Void [269](#void-3)

9.3.1.203 Void [269](#void-4)

9.3.1.204 Void [269](#void-5)

9.3.1.205 NR Radio Resource Status [269](#nr-radio-resource-status)

9.3.1.206 MBS Session ID [269](#mbs-session-id)

9.3.1.207 MBS Area Session ID [269](#mbs-area-session-id)

9.3.1.208 MBS Service Area [270](#mbs-service-area)

9.3.1.209 MBS Service Area information [270](#mbs-service-area-information)

9.3.1.210 MBS Support Indicator [270](#mbs-support-indicator)

9.3.1.211 MBS Session Setup Request List [270](#mbs-session-setup-request-list)

9.3.1.212 MBS Session Setup or Modify Request List [271](#mbs-session-setup-or-modify-request-list)

9.3.1.213 MBS Session Setup Response List [271](#mbs-session-setup-response-list)

9.3.1.214 MBS Session Failed to Setup List [272](#mbs-session-failed-to-setup-list)

9.3.1.215 MBS Session To Release List [272](#mbs-session-to-release-list)

9.3.1.216 Multicast Group Paging Area [272](#multicast-group-paging-area)

9.3.1.217 MBS Session Status [273](#mbs-session-status)

9.3.1.218 MRB ID [273](#mrb-id)

9.3.1.219 MRB Progress Information [273](#mrb-progress-information)

9.3.1.220 Time Synchronisation Assistance Information [273](#time-synchronisation-assistance-information)

9.3.1.221 Survival Time [273](#survival-time)

9.3.1.222 QMC Deactivation [274](#qmc-deactivation)

9.3.1.223 QMC Configuration Information [274](#_Toc175580235)

9.3.1.224 UE Application Layer Measurement Configuration Information [274](#ue-application-layer-measurement-configuration-information)

9.3.1.225 Available RAN Visible QoE Metrics [276](#available-ran-visible-qoe-metrics)

9.3.1.226 Void [276](#void-6)

9.3.1.227 NR Paging eDRX Information [276](#nr-paging-edrx-information)

9.3.1.228 RedCap Indication [277](#redcap-indication)

9.3.1.229 Target NSSAI Information [277](#target-nssai-information)

9.3.1.230 Target NSSAI [277](#target-nssai)

9.3.1.231 UE Slice Maximum Bit Rate List [277](#ue-slice-maximum-bit-rate-list)

9.3.1.232 PEIPS Assistance Information [278](#peips-assistance-information)

9.3.1.233 5G ProSe Authorized [278](#g-prose-authorized)

9.3.1.234 5G ProSe PC5 QoS Parameters [278](#g-prose-pc5-qos-parameters)

9.3.1.235 Last Visited PSCell Information [279](#last-visited-pscell-information)

9.3.1.236 MBS QoS Flows To Be Setup List [279](#mbs-qos-flows-to-be-setup-list)

9.3.1.237 Reporting System [280](#reporting-system)

9.3.1.238 TAI NSAG Support List [280](#tai-nsag-support-list)

9.3.1.239 NGAP Protocol IE-Id [280](#ngap-protocol-ie-id)

9.3.1.240 NGAP Protocol IE Support Information [280](#ngap-protocol-ie-support-information)

9.3.1.241 NGAP Protocol IE Presence Information [281](#ngap-protocol-ie-presence-information)

9.3.1.242 NGAP IE Support Information Response List [281](#ngap-ie-support-information-response-list)

9.3.1.243 MDT PLMN Modification List [281](#mdt-plmn-modification-list)

9.3.1.244 Excess Packet Delay Threshold Configuration [281](#excess-packet-delay-threshold-configuration)

9.3.2 Transport Network Layer Related IEs [282](#transport-network-layer-related-ies)

9.3.2.1 QoS Flow per TNL Information List [282](#qos-flow-per-tnl-information-list)

9.3.2.2 UP Transport Layer Information [282](#up-transport-layer-information)

9.3.2.3 E-RAB ID [283](#e-rab-id)

9.3.2.4 Transport Layer Address [283](#transport-layer-address)

9.3.2.5 GTP-TEID [283](#gtp-teid)

9.3.2.6 CP Transport Layer Information [283](#cp-transport-layer-information)

9.3.2.7 TNL Association List [283](#tnl-association-list)

9.3.2.8 QoS Flow per TNL Information [284](#qos-flow-per-tnl-information)

9.3.2.9 TNL Association Usage [284](#tnl-association-usage)

9.3.2.10 TNL Address Weight Factor [284](#tnl-address-weight-factor)

9.3.2.11 UP Transport Layer Information Pair List [284](#up-transport-layer-information-pair-list)

9.3.2.12 UP Transport Layer Information List [285](#up-transport-layer-information-list)

9.3.2.13 QoS Flow List with Data Forwarding [285](#qos-flow-list-with-data-forwarding)

9.3.2.14 URI [286](#uri)

9.3.2.15 MBS Session TNL Information 5GC [286](#mbs-session-tnl-information-5gc)

9.3.2.16 Shared NG-U Multicast TNL Information [287](#shared-ng-u-multicast-tnl-information)

9.3.2.17 MBS Session TNL Information NG-RAN [287](#mbs-session-tnl-information-ng-ran)

9.3.3 NAS Related IEs [287](#nas-related-ies)

9.3.3.1 AMF UE NGAP ID [287](#amf-ue-ngap-id)

9.3.3.2 RAN UE NGAP ID [287](#ran-ue-ngap-id)

9.3.3.3 GUAMI [288](#guami)

9.3.3.4 NAS-PDU [288](#nas-pdu)

9.3.3.5 PLMN Identity [288](#plmn-identity)

9.3.3.6 SON Configuration Transfer [288](#son-configuration-transfer)

9.3.3.7 SON Information [289](#son-information)

9.3.3.8 SON Information Reply [289](#son-information-reply)

9.3.3.9 Xn TNL Configuration Info [289](#xn-tnl-configuration-info)

9.3.3.10 TAC [290](#tac)

9.3.3.11 TAI [290](#tai)

9.3.3.12 AMF Set ID [291](#amf-set-id)

9.3.3.13 Routing ID [291](#routing-id)

9.3.3.14 NRPPa-PDU [291](#nrppa-pdu)

9.3.3.15 RAN Paging Priority [291](#ran-paging-priority)

9.3.3.16 EPS TAC [291](#eps-tac)

9.3.3.17 EPS TAI [292](#eps-tai)

9.3.3.18 UE Paging Identity [292](#ue-paging-identity)

9.3.3.19 AMF Pointer [292](#amf-pointer)

9.3.3.20 5G-S-TMSI [292](#g-s-tmsi)

9.3.3.21 AMF Name [292](#amf-name)

9.3.3.22 Paging Origin [292](#paging-origin)

9.3.3.23 UE Identity Index Value [293](#ue-identity-index-value)

9.3.3.24 Periodic Registration Update Timer [293](#periodic-registration-update-timer)

9.3.3.25 UE-associated Logical NG-connection List [293](#ue-associated-logical-ng-connection-list)

9.3.3.26 NAS Security Parameters from NG-RAN [294](#nas-security-parameters-from-ng-ran)

9.3.3.27 Source to Target AMF Information Reroute [294](#source-to-target-amf-information-reroute)

9.3.3.28 RIM Information Transfer [294](#rim-information-transfer)

9.3.3.29 RIM Information [295](#rim-information)

9.3.3.30 LAI [295](#lai)

9.3.3.31 Extended Connected Time [295](#extended-connected-time)

9.3.3.32 End Indication [295](#end-indication)

9.3.3.33 Inter-system SON Configuration Transfer [296](#inter-system-son-configuration-transfer)

9.3.3.34 Inter-system SON Information [296](#inter-system-son-information)

9.3.3.35 SON Information Report [297](#son-information-report)

9.3.3.36 Inter-system SON Information Report [297](#inter-system-son-information-report)

9.3.3.37 Failure Indication [297](#failure-indication)

9.3.3.38 Inter-system Failure Indication [298](#inter-system-failure-indication)

9.3.3.39 HO Report [298](#ho-report)

9.3.3.40 Inter-system HO Report [300](#inter-system-ho-report)

9.3.3.41 UE RLF Report Container [301](#ue-rlf-report-container)

9.3.3.42 NID [301](#nid)

9.3.3.43 CAG ID [301](#cag-id)

9.3.3.44 NPN Support [301](#npn-support)

9.3.3.45 Allowed PNI-NPN List [301](#allowed-pni-npn-list)

9.3.3.46 NPN Access Information [302](#npn-access-information)

9.3.3.47 Cell CAG List [302](#cell-cag-list)

9.3.3.48 UL CP Security Information [302](#ul-cp-security-information)

9.3.3.49 DL CP Security Information [303](#_Toc175580324)

9.3.3.50 Configured TAC Indication [303](#configured-tac-indication)

9.3.3.51 Extended AMF Name [303](#extended-amf-name)

9.3.3.52 Extended UE Identity Index Value [304](#extended-ue-identity-index-value)

9.3.3.53 NR NTN TAI Information [304](#nr-ntn-tai-information)

9.3.3.54 Inter-system SON Information Request [304](#inter-system-son-information-request)

9.3.3.55 Inter-system SON Information Reply [304](#inter-system-son-information-reply)

9.3.3.56 Inter-system Cell Activation Request [305](#inter-system-cell-activation-request)

9.3.3.57 Inter-system Cell State Indication [305](#inter-system-cell-state-indication)

9.3.3.58 Inter-system Cell Activation Reply [305](#inter-system-cell-activation-reply)

9.3.3.59 Inter-system Resource Status Request [305](#inter-system-resource-status-request)

9.3.3.60 Inter-system Resource Status Report [307](#inter-system-resource-status-report)

9.3.3.61 Inter-system Resource Status Reply [307](#inter-system-resource-status-reply)

9.3.3.62 Hashed UE Identity Index Value [307](#hashed-ue-identity-index-value)

9.3.4 SMF Related IEs [308](#smf-related-ies)

9.3.4.1 PDU Session Resource Setup Request Transfer [308](#pdu-session-resource-setup-request-transfer)

9.3.4.2 PDU Session Resource Setup Response Transfer [310](#pdu-session-resource-setup-response-transfer)

9.3.4.3 PDU Session Resource Modify Request Transfer [312](#pdu-session-resource-modify-request-transfer)

9.3.4.4 PDU Session Resource Modify Response Transfer [314](#pdu-session-resource-modify-response-transfer)

9.3.4.5 PDU Session Resource Notify Transfer [316](#pdu-session-resource-notify-transfer)

9.3.4.6 PDU Session Resource Modify Indication Transfer [318](#pdu-session-resource-modify-indication-transfer)

9.3.4.7 PDU Session Resource Modify Confirm Transfer [318](#pdu-session-resource-modify-confirm-transfer)

9.3.4.8 Path Switch Request Transfer [319](#path-switch-request-transfer)

9.3.4.9 Path Switch Request Acknowledge Transfer [321](#path-switch-request-acknowledge-transfer)

9.3.4.10 Handover Command Transfer [323](#handover-command-transfer)

9.3.4.11 Handover Request Acknowledge Transfer [324](#handover-request-acknowledge-transfer)

9.3.4.12 PDU Session Resource Release Command Transfer [326](#pdu-session-resource-release-command-transfer)

9.3.4.13 PDU Session Resource Notify Released Transfer [326](#pdu-session-resource-notify-released-transfer)

9.3.4.14 Handover Required Transfer [326](#handover-required-transfer)

9.3.4.15 Path Switch Request Setup Failed Transfer [326](#path-switch-request-setup-failed-transfer)

9.3.4.16 PDU Session Resource Setup Unsuccessful Transfer [327](#pdu-session-resource-setup-unsuccessful-transfer)

9.3.4.17 PDU Session Resource Modify Unsuccessful Transfer [327](#pdu-session-resource-modify-unsuccessful-transfer)

9.3.4.18 Handover Preparation Unsuccessful Transfer [327](#handover-preparation-unsuccessful-transfer)

9.3.4.19 Handover Resource Allocation Unsuccessful Transfer [327](#handover-resource-allocation-unsuccessful-transfer)

9.3.4.20 Path Switch Request Unsuccessful Transfer [327](#path-switch-request-unsuccessful-transfer)

9.3.4.21 PDU Session Resource Release Response Transfer [327](#pdu-session-resource-release-response-transfer)

9.3.4.22 PDU Session Resource Modify Indication Unsuccessful Transfer [327](#pdu-session-resource-modify-indication-unsuccessful-transfer)

9.3.4.23 Secondary RAT Data Usage Report Transfer [328](#secondary-rat-data-usage-report-transfer)

9.3.4.24 UE Context Resume Request Transfer [328](#ue-context-resume-request-transfer)

9.3.4.25 UE Context Resume Response Transfer [328](#ue-context-resume-response-transfer)

9.3.4.26 UE Context Suspend Request Transfer [328](#ue-context-suspend-request-transfer)

9.3.5 MB-SMF Related IEs [328](#mb-smf-related-ies)

9.3.5.1 Void [328](#void-7)

9.3.5.2 Void [328](#void-8)

9.3.5.3 MBS Session Setup or Modification Request Transfer [328](#mbs-session-setup-or-modification-request-transfer)

9.3.5.4 Void [329](#void-9)

9.3.5.5 MBS Session Setup or Modification Response Transfer [329](#mbs-session-setup-or-modification-response-transfer)

9.3.5.6 MBS Session Setup or Modification Failure Transfer [329](#mbs-session-setup-or-modification-failure-transfer)

9.3.5.7 MBS Distribution Setup Request Transfer [329](#mbs-distribution-setup-request-transfer)

9.3.5.8 MBS Distribution Setup Response Transfer [329](#mbs-distribution-setup-response-transfer)

9.3.5.9 MBS Distribution Setup Unsuccessful Transfer [330](#mbs-distribution-setup-unsuccessful-transfer)

9.3.5.10 MBS Distribution Release Request Transfer [330](#mbs-distribution-release-request-transfer)

9.3.5.11 Multicast Session Activation Request Transfer [330](#multicast-session-activation-request-transfer)

9.3.5.12 Multicast Session Deactivation Request Transfer [330](#multicast-session-deactivation-request-transfer)

9.3.5.13 Multicast Session Update Request Transfer [330](#multicast-session-update-request-transfer)

9.3.5.14 MBS Session Release Response Transfer [331](#mbs-session-release-response-transfer)

9.4 Message and Information Element Abstract Syntax (with ASN.1) [331](#message-and-information-element-abstract-syntax-with-asn.1)

9.4.1 General [331](#general-74)

9.4.2 Usage of private message mechanism for non-standard use [331](#usage-of-private-message-mechanism-for-non-standard-use)

9.4.3 Elementary Procedure Definitions [333](#elementary-procedure-definitions)

9.4.4 PDU Definitions [350](#pdu-definitions)

9.4.5 Information Element Definitions [416](#information-element-definitions-1)

9.4.6 Common Definitions [553](#common-definitions)

9.4.7 Constant Definitions [554](#constant-definitions)

9.4.8 Container Definitions [565](#container-definitions)

9.5 Message Transfer Syntax [570](#message-transfer-syntax)

9.6 Timers [570](#timers)

10 Handling of Unknown, Unforeseen and Erroneous Protocol Data [571](#handling-of-unknown-unforeseen-and-erroneous-protocol-data)

10.1 General [571](#general-75)

10.2 Transfer Syntax Error [571](#transfer-syntax-error)

10.3 Abstract Syntax Error [571](#abstract-syntax-error)

10.3.1 General [571](#general-76)

10.3.2 Criticality Information [572](#criticality-information)

10.3.3 Presence Information [572](#presence-information)

10.3.4 Not comprehended IE/IE group [573](#not-comprehended-ieie-group)

10.3.4.1 Procedure Code [573](#procedure-code)

10.3.4.1A Type of Message [573](#a-type-of-message)

10.3.4.2 IEs other than the Procedure Code and Type of Message [573](#ies-other-than-the-procedure-code-and-type-of-message)

10.3.5 Missing IE or IE group [574](#missing-ie-or-ie-group)

10.3.6 IEs or IE groups received in wrong order or with too many occurrences or erroneously present [575](#ies-or-ie-groups-received-in-wrong-order-or-with-too-many-occurrences-or-erroneously-present)

10.4 Logical Error [576](#logical-error)

10.5 Exceptions [576](#exceptions)

10.6 Handling of AP ID [577](#handling-of-ap-id)

Annex A (informative): Change history [578](#annex-a-informative-change-history)

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
