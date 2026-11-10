3GPP TS 38.423 V18.9.0 (2026-06)

Technical Specification

3<sup>rd</sup> Generation Partnership Project;

Technical Specification Group Radio Access Network;

NG-RAN;

Xn application protocol (XnAP)

(Release 18)

[figure] <img src="media/image2.png" style="width:1.76806in;height:1.07986in" />

The present document has been developed within the 3<sup>rd</sup> Generation Partnership Project (3GPP <sup>TM</sup>) and may be further elaborated for the purposes of 3GPP..  
The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented.  
This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification.  
Specifications and Reports for implementation of the 3GPP <sup>TM</sup> system should be obtained via the 3GPP Organizational Partners’ Publications Offices.

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

Foreword [16](#foreword)

1 Scope [17](#scope)

2 References [17](#references)

3 Definitions, symbols and abbreviations [19](#definitions-symbols-and-abbreviations)

3.1 Definitions [19](#definitions)

3.2 Abbreviations [20](#abbreviations)

4 General [21](#general)

4.1 Procedure specification principles [21](#procedure-specification-principles)

4.2 Forwards and backwards compatibility [21](#forwards-and-backwards-compatibility)

4.3 Specification notations [21](#specification-notations)

5 XnAP services [22](#xnap-services)

5.1 XnAP procedure modules [22](#xnap-procedure-modules)

5.2 Parallel transactions [22](#parallel-transactions)

6 Services expected from signalling transport [22](#services-expected-from-signalling-transport)

7 Functions of XnAP [22](#functions-of-xnap)

8 XnAP procedures [22](#xnap-procedures)

8.1 Elementary procedures [22](#elementary-procedures)

8.2 Basic mobility procedures [25](#basic-mobility-procedures)

8.2.1 Handover Preparation [25](#handover-preparation)

8.2.1.1 General [25](#general-1)

8.2.1.2 Successful Operation [25](#successful-operation)

8.2.1.3 Unsuccessful Operation [33](#unsuccessful-operation)

8.2.1.4 Abnormal Conditions [33](#abnormal-conditions)

8.2.2 SN Status Transfer [34](#sn-status-transfer)

8.2.2.1 General [34](#general-2)

8.2.2.2 Successful Operation [34](#successful-operation-1)

8.2.2.3 Unsuccessful Operation [35](#unsuccessful-operation-1)

8.2.2.4 Abnormal Conditions [35](#abnormal-conditions-1)

8.2.3 Handover Cancel [35](#handover-cancel)

8.2.3.1 General [35](#general-3)

8.2.3.2 Successful Operation [35](#successful-operation-2)

8.2.3.3 Unsuccessful Operation [36](#unsuccessful-operation-2)

8.2.3.4 Abnormal Conditions [36](#abnormal-conditions-2)

8.2.4 Retrieve UE Context [36](#retrieve-ue-context)

8.2.4.1 General [36](#general-4)

8.2.4.2 Successful Operation [36](#successful-operation-3)

8.2.4.3 Unsuccessful Operation [40](#unsuccessful-operation-3)

8.2.4.4 Abnormal Conditions [40](#abnormal-conditions-3)

8.2.5 RAN Paging [41](#ran-paging)

8.2.5.1 General [41](#general-5)

8.2.5.2 Successful operation [41](#successful-operation-4)

8.2.5.3 Unsuccessful Operation [42](#unsuccessful-operation-4)

8.2.5.4 Abnormal Condition [42](#abnormal-condition)

8.2.6 XN-U Address Indication [42](#xn-u-address-indication)

8.2.6.1 General [42](#general-6)

8.2.6.2 Successful Operation [42](#successful-operation-5)

8.2.6.3 Unsuccessful Operation [44](#unsuccessful-operation-5)

8.2.6.4 Abnormal Conditions [44](#abnormal-conditions-4)

8.2.7 UE Context Release [44](#ue-context-release)

8.2.7.1 General [44](#general-7)

8.2.7.2 Successful Operation [44](#successful-operation-6)

8.2.7.3 Unsuccessful Operation [45](#unsuccessful-operation-6)

8.2.7.4 Abnormal Conditions [46](#abnormal-conditions-5)

8.2.8 Handover Success [46](#handover-success)

8.2.8.1 General [46](#general-8)

8.2.8.2 Successful Operation [46](#successful-operation-7)

8.2.8.3 Unsuccessful Operation [46](#unsuccessful-operation-7)

8.2.8.4 Abnormal Conditions [46](#abnormal-conditions-6)

8.2.9 Conditional Handover Cancel [47](#conditional-handover-cancel)

8.2.9.1 General [47](#general-9)

8.2.9.2 Successful Operation [47](#successful-operation-8)

8.2.9.3 Unsuccessful Operation [47](#unsuccessful-operation-8)

8.2.9.4 Abnormal Conditions [47](#abnormal-conditions-7)

8.2.10 Early Status Transfer [47](#early-status-transfer)

8.2.10.1 General [47](#general-10)

8.2.10.2 Successful Operation [48](#successful-operation-9)

8.2.10.3 Unsuccessful Operation [49](#unsuccessful-operation-9)

8.2.10.4 Abnormal Conditions [49](#abnormal-conditions-8)

8.2.11 RAN Multicast Group Paging [49](#ran-multicast-group-paging)

8.2.11.1 General [49](#general-11)

8.2.11.2 Successful operation [50](#successful-operation-10)

8.2.12 Retrieve UE Context Confirm [50](#retrieve-ue-context-confirm)

8.2.12.1 General [50](#general-12)

8.2.12.2 Successful Operation [50](#successful-operation-11)

8.2.12.3 Unsuccessful Operation [51](#unsuccessful-operation-10)

8.2.12.4 Abnormal Conditions [51](#abnormal-conditions-9)

8.2.13 Partial UE Context Transfer [51](#partial-ue-context-transfer)

8.2.13.1 General [51](#general-13)

8.2.13.2 Successful Operation [51](#successful-operation-12)

8.2.13.3 Unsuccessful Operation [52](#unsuccessful-operation-11)

8.2.13.4 Abnormal Condition [52](#abnormal-condition-1)

8.3 Procedures for Dual Connectivity [52](#procedures-for-dual-connectivity)

8.3.1 S-NG-RAN node Addition Preparation [52](#s-ng-ran-node-addition-preparation)

8.3.1.1 General [52](#general-14)

8.3.1.2 Successful Operation [52](#successful-operation-13)

8.3.1.3 Unsuccessful Operation [59](#unsuccessful-operation-12)

8.3.1.4 Abnormal Conditions [59](#abnormal-conditions-10)

8.3.2 S-NG-RAN node Reconfiguration Completion [60](#s-ng-ran-node-reconfiguration-completion)

8.3.2.1 General [60](#general-15)

8.3.2.2 Successful Operation [60](#successful-operation-14)

8.3.2.3 Abnormal Conditions [61](#abnormal-conditions-11)

8.3.3 M-NG-RAN node initiated S-NG-RAN node Modification Preparation [61](#m-ng-ran-node-initiated-s-ng-ran-node-modification-preparation)

8.3.3.1 General [61](#general-16)

8.3.3.2 Successful Operation [61](#successful-operation-15)

8.3.3.3 Unsuccessful Operation [70](#unsuccessful-operation-13)

8.3.3.4 Abnormal Conditions [70](#abnormal-conditions-12)

8.3.4 S-NG-RAN node initiated S-NG-RAN node Modification [72](#s-ng-ran-node-initiated-s-ng-ran-node-modification)

8.3.4.1 General [72](#general-17)

8.3.4.2 Successful Operation [72](#successful-operation-16)

8.3.4.3 Unsuccessful Operation [75](#unsuccessful-operation-14)

8.3.4.4 Abnormal Conditions [75](#abnormal-conditions-13)

8.3.5 S-NG-RAN node initiated S-NG-RAN node Change [76](#s-ng-ran-node-initiated-s-ng-ran-node-change)

8.3.5.1 General [76](#general-18)

8.3.5.2 Successful Operation [76](#successful-operation-17)

8.3.5.3 Unsuccessful Operation [78](#unsuccessful-operation-15)

8.3.5.4 Abnormal Conditions [78](#abnormal-conditions-14)

8.3.6 M-NG-RAN node initiated S-NG-RAN node Release [78](#m-ng-ran-node-initiated-s-ng-ran-node-release)

8.3.6.1 General [78](#general-19)

8.3.6.2 Successful Operation [79](#successful-operation-18)

8.3.6.3 Unsuccessful Operation [80](#unsuccessful-operation-16)

8.3.6.4 Abnormal Conditions [80](#abnormal-conditions-15)

8.3.7 S-NG-RAN node initiated S-NG-RAN node Release [80](#s-ng-ran-node-initiated-s-ng-ran-node-release)

8.3.7.1 General [80](#general-20)

8.3.7.2 Successful Operation [80](#successful-operation-19)

8.3.7.3 Unsuccessful Operation [81](#unsuccessful-operation-17)

8.3.7.4 Abnormal Conditions [81](#abnormal-conditions-16)

8.3.8 S-NG-RAN node Counter Check [81](#s-ng-ran-node-counter-check)

8.3.8.1 General [81](#general-21)

8.3.8.2 Successful Operation [81](#successful-operation-20)

8.3.8.3 Unsuccessful Operation [82](#unsuccessful-operation-18)

8.3.8.4 Abnormal Conditions [82](#abnormal-conditions-17)

8.3.9 RRC Transfer [82](#rrc-transfer)

8.3.9.1 General [82](#general-22)

8.3.9.2 Successful Operation [82](#successful-operation-21)

8.3.9.3 Unsuccessful Operation [83](#unsuccessful-operation-19)

8.3.9.4 Abnormal Conditions [83](#abnormal-conditions-18)

8.3.10 Notification Control Indication [83](#notification-control-indication)

8.3.10.1 General [83](#general-23)

8.3.10.2 Successful Operation – M-NG-RAN node initiated [84](#successful-operation-m-ng-ran-node-initiated)

8.3.10.3 Successful Operation – S-NG-RAN node initiated [84](#successful-operation-s-ng-ran-node-initiated)

8.3.10.4 Abnormal Conditions [84](#abnormal-conditions-19)

8.3.11 Activity Notification [85](#activity-notification)

8.3.11.1 General [85](#general-24)

8.3.11.2 Successful Operation [85](#successful-operation-22)

8.3.11.3 Abnormal Conditions [85](#abnormal-conditions-20)

8.3.12 E-UTRA - NR Cell Resource Coordination [86](#e-utra---nr-cell-resource-coordination)

8.3.12.1 General [86](#general-25)

8.3.12.2 Successful Operation [86](#successful-operation-23)

8.3.13 Secondary RAT Data Usage Report [87](#secondary-rat-data-usage-report)

8.3.13.1 General [87](#general-26)

8.3.13.2 Successful Operation [87](#successful-operation-24)

8.3.13.3 Unsuccessful Operation [87](#unsuccessful-operation-20)

8.3.13.4 Abnormal Conditions [87](#abnormal-conditions-21)

8.3.14 Trace Start [87](#trace-start)

8.3.14.1 General [87](#general-27)

8.3.14.2 Successful Operation [88](#successful-operation-25)

8.3.14.3 Abnormal Conditions [88](#abnormal-conditions-22)

8.3.15 Deactivate Trace [89](#deactivate-trace)

8.3.15.1 General [89](#general-28)

8.3.15.2 Successful Operation [89](#successful-operation-26)

8.3.15.3 Abnormal Conditions [89](#abnormal-conditions-23)

8.3.16 Cell Traffic Trace [89](#cell-traffic-trace)

8.3.16.1 General [89](#general-29)

8.3.16.2 Successful Operation [90](#successful-operation-27)

8.3.17 SCG Failure Information Report [90](#scg-failure-information-report)

8.3.17.1 General [90](#general-30)

8.3.17.2 Successful Operation [90](#successful-operation-28)

8.3.17.3 Unsuccessful Operation [91](#unsuccessful-operation-21)

8.3.17.4 Abnormal Conditions [91](#abnormal-conditions-24)

8.3.18 SCG Failure Transfer [91](#scg-failure-transfer)

8.3.18.1 General [91](#general-31)

8.3.18.2 Successful Operation [91](#successful-operation-29)

8.3.18.3 Unsuccessful Operation [91](#unsuccessful-operation-22)

8.3.18.4 Abnormal Conditions [91](#abnormal-conditions-25)

8.3.19 Conditional PSCell Change Cancel [91](#conditional-pscell-change-cancel)

8.3.19.1 General [91](#general-32)

8.3.19.2 Successful Operation [92](#successful-operation-30)

8.3.19.3 Unsuccessful Operation [92](#unsuccessful-operation-23)

8.3.19.4 Abnormal Conditions [92](#abnormal-conditions-26)

8.3.20 RACH Indication [92](#rach-indication)

8.3.20.1 General [92](#general-33)

8.3.20.2 Successful Operation [92](#successful-operation-31)

8.3.20.3 Abnormal Conditions [93](#abnormal-conditions-27)

8.4 Global procedures [93](#global-procedures)

8.4.1 Xn Setup [93](#xn-setup)

8.4.1.1 General [93](#general-34)

8.4.1.2 Successful Operation [93](#successful-operation-32)

8.4.1.3 Unsuccessful Operation [96](#unsuccessful-operation-24)

8.4.1.4 Abnormal Conditions [96](#abnormal-conditions-28)

8.4.2 NG-RAN node Configuration Update [97](#ng-ran-node-configuration-update)

8.4.2.1 General [97](#general-35)

8.4.2.2 Successful Operation [97](#successful-operation-33)

8.4.2.3 Unsuccessful Operation [102](#unsuccessful-operation-25)

8.4.2.4 Abnormal Conditions [102](#abnormal-conditions-29)

8.4.3 Cell Activation [102](#cell-activation)

8.4.3.1 General [102](#general-36)

8.4.3.2 Successful Operation [103](#successful-operation-34)

8.4.3.3 Unsuccessful Operation [103](#unsuccessful-operation-26)

8.4.3.4 Abnormal Conditions [104](#abnormal-conditions-30)

8.4.4 Reset [104](#reset)

8.4.4.1 General [104](#general-37)

8.4.4.2 Successful Operation [104](#successful-operation-35)

8.4.4.3 Unsuccessful Operation [105](#unsuccessful-operation-27)

8.4.4.4 Abnormal Conditions [105](#abnormal-conditions-31)

8.4.5 Error Indication [105](#error-indication)

8.4.5.1 General [105](#general-38)

8.4.5.2 Successful Operation [105](#successful-operation-36)

8.4.5.3 Unsuccessful Operation [106](#unsuccessful-operation-28)

8.4.5.4 Abnormal Conditions [106](#abnormal-conditions-32)

8.4.6 Xn Removal [106](#xn-removal)

8.4.6.1 General [106](#general-39)

8.4.6.2 Successful Operation [106](#successful-operation-37)

8.4.6.3 Unsuccessful Operation [107](#unsuccessful-operation-29)

8.4.6.4 Abnormal Conditions [107](#abnormal-conditions-33)

8.4.7 Failure Indication [107](#failure-indication)

8.4.7.1 General [107](#general-40)

8.4.7.2 Successful Operation [107](#successful-operation-38)

8.4.7.3 Unsuccessful Operation [108](#unsuccessful-operation-30)

8.4.7.4 Abnormal Conditions [108](#abnormal-conditions-34)

8.4.8 Handover Report [108](#handover-report)

8.4.8.1 General [108](#general-41)

8.4.8.2 Successful Operation [108](#successful-operation-39)

8.4.8.3 Unsuccessful Operation [109](#unsuccessful-operation-31)

8.4.8.4 Abnormal Conditions [109](#abnormal-conditions-35)

8.4.9 Mobility Settings Change [109](#mobility-settings-change)

8.4.9.1 General [109](#general-42)

8.4.9.2 Successful Operation [109](#successful-operation-40)

8.4.9.3 Unsuccessful Operation [110](#unsuccessful-operation-32)

8.4.9.4 Abnormal Conditions [110](#abnormal-conditions-36)

8.4.10 Resource Status Reporting Initiation [110](#resource-status-reporting-initiation)

8.4.10.1 General [110](#general-43)

8.4.10.2 Successful Operation [110](#successful-operation-41)

8.4.10.3 Unsuccessful Operation [112](#unsuccessful-operation-33)

8.4.10.4 Abnormal Conditions [112](#abnormal-conditions-37)

8.4.11 Resource Status Reporting [112](#resource-status-reporting)

8.4.11.1 General [112](#general-44)

8.4.11.2 Successful Operation [113](#successful-operation-42)

8.4.11.3 Unsuccessful Operation [113](#unsuccessful-operation-34)

8.4.11.4 Abnormal Conditions [113](#abnormal-conditions-38)

8.4.12 Access And Mobility Indication [113](#access-and-mobility-indication)

8.4.12.1 General [113](#general-45)

8.4.12.2 Successful Operation [113](#successful-operation-43)

8.4.12.3 Abnormal Conditions [114](#abnormal-conditions-39)

8.4.13 Data Collection Reporting Initiation [114](#data-collection-reporting-initiation)

8.4.13.1 General [114](#general-46)

8.4.13.2 Successful Operation [114](#successful-operation-44)

8.4.13.3 Unsuccessful Operation [116](#unsuccessful-operation-35)

8.4.13.4 Abnormal Conditions [116](#abnormal-conditions-40)

8.4.14 Data Collection Reporting [117](#data-collection-reporting)

8.4.14.1 General [117](#general-47)

8.4.14.2 Successful Operation [117](#successful-operation-45)

8.4.14.3 Unsuccessful Operation [117](#unsuccessful-operation-36)

8.4.14.4 Abnormal Conditions [117](#abnormal-conditions-41)

8.5 IAB Procedures [117](#iab-procedures)

8.5.1 F1-C Traffic Transfer [117](#f1-c-traffic-transfer)

8.5.1.1 General [117](#general-48)

8.5.1.2 Successful Operation [118](#successful-operation-46)

8.5.1.3 Unsuccessful Operation [118](#unsuccessful-operation-37)

8.5.1.4 Abnormal Conditions [118](#abnormal-conditions-42)

8.5.2 IAB Transport Migration Management [118](#iab-transport-migration-management)

8.5.2.1 General [118](#general-49)

8.5.2.2 Successful Operation [119](#successful-operation-47)

8.5.2.3 Unsuccessful Operation [120](#unsuccessful-operation-38)

8.5.2.4 Abnormal Conditions [120](#abnormal-conditions-43)

8.5.3 IAB Transport Migration Modification [120](#iab-transport-migration-modification)

8.5.3.1 General [120](#general-50)

8.5.3.2 Successful Operation [120](#successful-operation-48)

8.5.3.3 Unsuccessful Operation [121](#unsuccessful-operation-39)

8.5.3.4 Abnormal Conditions [121](#abnormal-conditions-44)

8.5.4 IAB Resource Coordination [121](#iab-resource-coordination)

8.5.4.1 General [121](#general-51)

8.5.4.2 Successful Operation [122](#successful-operation-49)

8.5.4.3 Unsuccessful Operation [122](#unsuccessful-operation-40)

8.5.4.4 Abnormal Conditions [122](#abnormal-conditions-45)

9 Elements for XnAP Communication [123](#elements-for-xnap-communication)

9.0 General [123](#general-52)

9.1 Message Functional Definition and Content [123](#message-functional-definition-and-content)

9.1.1 Messages for Basic Mobility Procedures [123](#messages-for-basic-mobility-procedures)

9.1.1.1 HANDOVER REQUEST [123](#handover-request)

9.1.1.2 HANDOVER REQUEST ACKNOWLEDGE [127](#handover-request-acknowledge)

9.1.1.3 HANDOVER PREPARATION FAILURE [128](#handover-preparation-failure)

9.1.1.4 SN STATUS TRANSFER [129](#sn-status-transfer-1)

9.1.1.5 UE CONTEXT RELEASE [129](#ue-context-release-1)

9.1.1.6 HANDOVER CANCEL [130](#handover-cancel-1)

9.1.1.7 RAN PAGING [130](#ran-paging-1)

9.1.1.8 RETRIEVE UE CONTEXT REQUEST [131](#retrieve-ue-context-request)

9.1.1.9 RETRIEVE UE CONTEXT RESPONSE [133](#retrieve-ue-context-response)

9.1.1.10 RETRIEVE UE CONTEXT FAILURE [134](#retrieve-ue-context-failure)

9.1.1.11 XN-U ADDRESS INDICATION [135](#xn-u-address-indication-1)

9.1.1.12 HANDOVER SUCCESS [136](#handover-success-1)

9.1.1.13 CONDITIONAL HANDOVER CANCEL [137](#conditional-handover-cancel-1)

9.1.1.14 EARLY STATUS TRANSFER [138](#early-status-transfer-1)

9.1.1.15 RAN MULTICAST GROUP PAGING [139](#ran-multicast-group-paging-1)

9.1.1.16 RETRIEVE UE CONTEXT CONFIRM [140](#retrieve-ue-context-confirm-1)

9.1.1.17 PARTIAL UE CONTEXT TRANSFER [140](#partial-ue-context-transfer-1)

9.1.1.18 PARTIAL UE CONTEXT TRANSFER ACKNOWLEDGE [141](#partial-ue-context-transfer-acknowledge)

9.1.1.19 PARTIAL UE CONTEXT TRANSFER FAILURE [141](#partial-ue-context-transfer-failure)

9.1.2 Messages for Dual Connectivity Procedures [142](#messages-for-dual-connectivity-procedures)

9.1.2.1 S-NODE ADDITION REQUEST [142](#s-node-addition-request)

9.1.2.2 S-NODE ADDITION REQUEST ACKNOWLEDGE [146](#s-node-addition-request-acknowledge)

9.1.2.3 S-NODE ADDITION REQUEST REJECT [148](#s-node-addition-request-reject)

9.1.2.4 S-NODE RECONFIGURATION COMPLETE [149](#s-node-reconfiguration-complete)

9.1.2.5 S-NODE MODIFICATION REQUEST [150](#s-node-modification-request)

9.1.2.6 S-NODE MODIFICATION REQUEST ACKNOWLEDGE [155](#s-node-modification-request-acknowledge)

9.1.2.7 S-NODE MODIFICATION REQUEST REJECT [158](#s-node-modification-request-reject)

9.1.2.8 S-NODE MODIFICATION REQUIRED [158](#s-node-modification-required)

9.1.2.9 S-NODE MODIFICATION CONFIRM [161](#s-node-modification-confirm)

9.1.2.10 S-NODE MODIFICATION REFUSE [163](#s-node-modification-refuse)

9.1.2.11 S-NODE CHANGE REQUIRED [163](#_Toc232069003)

9.1.2.12 S-NODE CHANGE CONFIRM [165](#s-node-change-confirm)

9.1.2.13 S-NODE CHANGE REFUSE [166](#s-node-change-refuse)

9.1.2.14 S-NODE RELEASE REQUEST [167](#s-node-release-request)

9.1.2.15 S-NODE RELEASE REQUEST ACKNOWLEDGE [167](#s-node-release-request-acknowledge)

9.1.2.16 S-NODE RELEASE REJECT [168](#s-node-release-reject)

9.1.2.17 S-NODE RELEASE REQUIRED [168](#s-node-release-required)

9.1.2.18 S-NODE RELEASE CONFIRM [169](#s-node-release-confirm)

9.1.2.19 S-NODE COUNTER CHECK REQUEST [169](#s-node-counter-check-request)

9.1.2.20 RRC TRANSFER [170](#rrc-transfer-1)

9.1.2.21 NOTIFICATION CONTROL INDICATION [173](#notification-control-indication-1)

9.1.2.22 ACTIVITY NOTIFICATION [173](#activity-notification-1)

9.1.2.23 E-UTRA - NR CELL RESOURCE COORDINATION REQUEST [174](#e-utra---nr-cell-resource-coordination-request)

9.1.2.24 E-UTRA - NR CELL RESOURCE COORDINATION RESPONSE [176](#e-utra---nr-cell-resource-coordination-response)

9.1.2.25 SECONDARY RAT DATA USAGE REPORT [177](#secondary-rat-data-usage-report-1)

9.1.2.26 TRACE START [177](#trace-start-1)

9.1.2.27 DEACTIVATE TRACE [178](#deactivate-trace-1)

9.1.2.28 CELL TRAFFIC TRACE [178](#cell-traffic-trace-1)

9.1.2.29 SCG FAILURE INFORMATION REPORT [178](#scg-failure-information-report-1)

9.1.2.30 SCG FAILURE TRANSFER [179](#scg-failure-transfer-1)

9.1.2.31 CONDITIONAL PSCELL CHANGE CANCEL [179](#conditional-pscell-change-cancel-1)

9.1.2.32 RACH INDICATION [180](#rach-indication-1)

9.1.3 Messages for Global Procedures [180](#messages-for-global-procedures)

9.1.3.1 XN SETUP REQUEST [180](#xn-setup-request)

9.1.3.2 XN SETUP RESPONSE [182](#xn-setup-response)

9.1.3.3 XN SETUP FAILURE [183](#xn-setup-failure)

9.1.3.4 NG-RAN NODE CONFIGURATION UPDATE [184](#ng-ran-node-configuration-update-1)

9.1.3.5 NG-RAN NODE CONFIGURATION UPDATE ACKNOWLEDGE [186](#ng-ran-node-configuration-update-acknowledge)

9.1.3.6 NG-RAN NODE CONFIGURATION UPDATE FAILURE [188](#ng-ran-node-configuration-update-failure)

9.1.3.7 CELL ACTIVATION REQUEST [188](#cell-activation-request)

9.1.3.8 CELL ACTIVATION RESPONSE [189](#cell-activation-response)

9.1.3.9 CELL ACTIVATION FAILURE [190](#cell-activation-failure)

9.1.3.10 RESET REQUEST [191](#reset-request)

9.1.3.11 RESET RESPONSE [191](#reset-response)

9.1.3.12 ERROR INDICATION [192](#error-indication-1)

9.1.3.13 XN REMOVAL REQUEST [192](#xn-removal-request)

9.1.3.14 XN REMOVAL RESPONSE [193](#xn-removal-response)

9.1.3.15 XN REMOVAL FAILURE [193](#xn-removal-failure)

9.1.3.16 FAILURE INDICATION [193](#failure-indication-1)

9.1.3.17 HANDOVER REPORT [194](#handover-report-1)

9.1.3.18 RESOURCE STATUS REQUEST [196](#resource-status-request)

9.1.3.19 RESOURCE STATUS RESPONSE [198](#resource-status-response)

9.1.3.20 RESOURCE STATUS FAILURE [198](#resource-status-failure)

9.1.3.21 RESOURCE STATUS UPDATE [198](#resource-status-update)

9.1.3.22 MOBILITY CHANGE REQUEST [200](#mobility-change-request)

9.1.3.23 MOBILITY CHANGE ACKNOWLEDGE [201](#mobility-change-acknowledge)

9.1.3.24 MOBILITY CHANGE FAILURE [201](#mobility-change-failure)

9.1.3.25 ACCESS AND MOBILITY INDICATION [201](#access-and-mobility-indication-1)

9.1.3.26 DATA COLLECTION REQUEST [203](#data-collection-request)

9.1.3.27 DATA COLLECTION RESPONSE [205](#data-collection-response)

9.1.3.28 DATA COLLECTION FAILURE [206](#data-collection-failure)

9.1.3.29 DATA COLLECTION UPDATE [207](#data-collection-update)

9.1.4 Messages for IAB Procedures [208](#messages-for-iab-procedures)

9.1.4.1 F1-C TRAFFIC TRANSFER [208](#f1-c-traffic-transfer-1)

9.1.4.2 IAB TRANSPORT MIGRATION MANAGEMENT REQUEST [208](#iab-transport-migration-management-request)

9.1.4.3 IAB TRANSPORT MIGRATION MANAGEMENT RESPONSE [209](#iab-transport-migration-management-response)

9.1.4.3a IAB TRANSPORT MIGRATION MANAGEMENT REJECT [210](#a-iab-transport-migration-management-reject)

9.1.4.4 IAB TRANSPORT MIGRATION MODIFICATION REQUEST [211](#iab-transport-migration-modification-request)

9.1.4.5 IAB TRANSPORT MIGRATION MODIFICATION RESPONSE [212](#iab-transport-migration-modification-response)

9.1.4.6 IAB RESOURCE COORDINATION REQUEST [212](#iab-resource-coordination-request)

9.1.4.7 IAB RESOURCE COORDINATION RESPONSE [213](#_Toc232069063)

9.2 Information Element definitions [214](#information-element-definitions)

9.2.0 General [214](#general-53)

9.2.1 Container and List IE definitions [214](#container-and-list-ie-definitions)

9.2.1.1 PDU Session Resources To Be Setup List [214](#pdu-session-resources-to-be-setup-list)

9.2.1.2 PDU Session Resources Admitted List [216](#pdu-session-resources-admitted-list)

9.2.1.3 PDU Session Resources Not Admitted List [216](#pdu-session-resources-not-admitted-list)

9.2.1.4 QoS Flow List with Cause [217](#qos-flow-list-with-cause)

9.2.1.4a QoS Flow List [217](#a-qos-flow-list)

9.2.1.5 PDU Session Resource Setup Info – SN terminated [217](#pdu-session-resource-setup-info-sn-terminated)

9.2.1.6 PDU Session Resource Setup Response Info – SN terminated [218](#pdu-session-resource-setup-response-info-sn-terminated)

9.2.1.7 PDU Session Resource Setup Info – MN terminated [221](#pdu-session-resource-setup-info-mn-terminated)

9.2.1.8 PDU Session Resource Setup Response Info – MN terminated [223](#pdu-session-resource-setup-response-info-mn-terminated)

9.2.1.9 PDU Session Resource Modification Info – SN terminated [224](#pdu-session-resource-modification-info-sn-terminated)

9.2.1.10 PDU Session Resource Modification Response Info – SN terminated [226](#pdu-session-resource-modification-response-info-sn-terminated)

9.2.1.11 PDU Session Resource Modification Info – MN terminated [230](#pdu-session-resource-modification-info-mn-terminated)

9.2.1.12 PDU Session Resource Modification Response Info – MN terminated [233](#pdu-session-resource-modification-response-info-mn-terminated)

9.2.1.13 UE Context Information – Retrieve UE Context Response [234](#ue-context-information-retrieve-ue-context-response)

9.2.1.14 DRBs Subject To Status Transfer List [236](#drbs-subject-to-status-transfer-list)

9.2.1.15 DRB to QoS Flow Mapping List [238](#drb-to-qos-flow-mapping-list)

9.2.1.16 Data Forwarding Info from target NG-RAN node [238](#data-forwarding-info-from-target-ng-ran-node)

9.2.1.17 Data Forwarding and Offloading Info from source NG-RAN node [239](#data-forwarding-and-offloading-info-from-source-ng-ran-node)

9.2.1.18 PDU Session Resource Change Required Info – SN terminated [240](#pdu-session-resource-change-required-info-sn-terminated)

9.2.1.19 PDU Session Resource Change Confirm Info – SN terminated [240](#pdu-session-resource-change-confirm-info-sn-terminated)

9.2.1.20 PDU Session Resource Modification Required Info – SN terminated [240](#pdu-session-resource-modification-required-info-sn-terminated)

9.2.1.21 PDU Session Resource Modification Confirm Info – SN terminated [243](#pdu-session-resource-modification-confirm-info-sn-terminated)

9.2.1.22 PDU Session Resource Modification Required Info – MN terminated [245](#pdu-session-resource-modification-required-info-mn-terminated)

9.2.1.23 PDU Session Resource Modification Confirm Info – MN terminated [246](#pdu-session-resource-modification-confirm-info-mn-terminated)

9.2.1.24 PDU Session List with data forwarding request info [246](#_Toc232069091)

9.2.1.25 PDU Session List with data forwarding info from the target node [246](#pdu-session-list-with-data-forwarding-info-from-the-target-node)

9.2.1.26 PDU Session List with Cause [247](#pdu-session-list-with-cause)

9.2.1.27 PDU Session List [247](#pdu-session-list)

9.2.1.28 DRB List with Cause [247](#drb-list-with-cause)

9.2.1.29 DRB List [247](#drb-list)

9.2.1.30 PDU Session Resource Setup Complete Info – SN terminated [248](#pdu-session-resource-setup-complete-info-sn-terminated)

9.2.1.31 Secondary Data Forwarding Info from target NG-RAN node List [248](#secondary-data-forwarding-info-from-target-ng-ran-node-list)

9.2.1.32 Additional UL NG-U UP TNL Information at UPF List [248](#additional-ul-ng-u-up-tnl-information-at-upf-list)

9.2.1.33 DAPS Request Information [249](#daps-request-information)

9.2.1.34 DAPS Response Information [249](#daps-response-information)

9.2.1.35 Data Forwarding Info from target E-UTRAN node [249](#data-forwarding-info-from-target-e-utran-node)

9.2.1.36 MBS Session Information List [250](#mbs-session-information-list)

9.2.1.37 MBS Session Associated Information [250](#mbs-session-associated-information)

9.2.1.38 MBS Session Information Response List [251](#mbs-session-information-response-list)

9.2.1.39 MBS Mapping and Data Forwarding Request Info from source NG-RAN node [251](#mbs-mapping-and-data-forwarding-request-info-from-source-ng-ran-node)

9.2.1.40 MBS Data Forwarding Response Info from target NG-RAN node [252](#mbs-data-forwarding-response-info-from-target-ng-ran-node)

9.2.1.41 PDU Sessions List To Be Released - UPError [252](#pdu-sessions-list-to-be-released---uperror)

9.2.2 NG-RAN Node and Cell Configuration related IE definitions [252](#ng-ran-node-and-cell-configuration-related-ie-definitions)

9.2.2.1 Global gNB ID [252](#global-gnb-id)

9.2.2.2 Global ng-eNB ID [253](#global-ng-enb-id)

9.2.2.3 Global NG-RAN Node ID [253](#global-ng-ran-node-id)

9.2.2.4 PLMN Identity [253](#plmn-identity)

9.2.2.5 TAC [254](#tac)

9.2.2.6 RAN Area Code [254](#ran-area-code)

9.2.2.7 NR CGI [254](#nr-cgi)

9.2.2.8 E-UTRA CGI [254](#e-utra-cgi)

9.2.2.9 NG-RAN Cell Identity [254](#ng-ran-cell-identity)

9.2.2.10 NG-RAN Cell PCI [255](#ng-ran-cell-pci)

9.2.2.11 Served Cell Information NR [255](#served-cell-information-nr)

9.2.2.12 Served Cell Information E-UTRA [262](#served-cell-information-e-utra)

9.2.2.13 Neighbour Information NR [265](#neighbour-information-nr)

9.2.2.14 Neighbour Information E-UTRA [266](#neighbour-information-e-utra)

9.2.2.15 Served Cells To Update NR [266](#served-cells-to-update-nr)

9.2.2.16 Served Cells to Update E-UTRA [267](#served-cells-to-update-e-utra)

9.2.2.17 Cell Assistance Information NR [268](#cell-assistance-information-nr)

9.2.2.18 SUL Information [268](#sul-information)

9.2.2.19 NR Frequency Info [269](#nr-frequency-info)

9.2.2.20 NR Transmission Bandwidth [270](#nr-transmission-bandwidth)

9.2.2.21 E-UTRA ARFCN [271](#e-utra-arfcn)

9.2.2.22 E-UTRA Transmission Bandwidth [271](#e-utra-transmission-bandwidth)

9.2.2.23 Number of Antenna Ports E-UTRA [271](#number-of-antenna-ports-e-utra)

9.2.2.24 E-UTRA Multiband Info List [271](#e-utra-multiband-info-list)

9.2.2.25 E-UTRA PRACH Configuration [272](#e-utra-prach-configuration)

9.2.2.26 MBSFN Subframe Allocation E-UTRA [272](#mbsfn-subframe-allocation-e-utra)

9.2.2.27 Global NG-RAN Cell Identity [272](#global-ng-ran-cell-identity)

9.2.2.28 Connectivity Support [272](#connectivity-support)

9.2.2.29 Protected E-UTRA Resource Indication [273](#protected-e-utra-resource-indication)

9.2.2.30 Data Traffic Resource Indication [274](#data-traffic-resource-indication)

9.2.2.31 Data Traffic Resources [275](#data-traffic-resources)

9.2.2.32 Reserved Subframe Pattern [275](#reserved-subframe-pattern)

9.2.2.33 MR-DC Resource Coordination Information [276](#mr-dc-resource-coordination-information)

9.2.2.34 E-UTRA Resource Coordination Information [276](#e-utra-resource-coordination-information)

9.2.2.35 NR Resource Coordination Information [277](#nr-resource-coordination-information)

9.2.2.36 E-UTRA Coordination Assistance Information [279](#e-utra-coordination-assistance-information)

9.2.2.37 NR Coordination Assistance Information [279](#nr-coordination-assistance-information)

9.2.2.38 NE-DC TDM Pattern [279](#ne-dc-tdm-pattern)

9.2.2.39 Interface Instance Indication [279](#interface-instance-indication)

9.2.2.39a Configured TAC Indication [280](#a-configured-tac-indication)

9.2.2.40 Intended TDD DL-UL Configuration NR [280](#intended-tdd-dl-ul-configuration-nr)

9.2.2.41 Cell and Capacity Assistance Information NR [281](#cell-and-capacity-assistance-information-nr)

9.2.2.42 Cell and Capacity Assistance Information E-UTRA [281](#cell-and-capacity-assistance-information-e-utra)

9.2.2.43 Cell Assistance Information E-UTRA [281](#cell-assistance-information-e-utra)

9.2.2.44 Maximum Cell List Size [282](#maximum-cell-list-size)

9.2.2.45 Message Oversize Notification [282](#message-oversize-notification)

9.2.2.46 Partial List Indicator [282](#partial-list-indicator)

9.2.2.47 Offset of NB-IoT Channel Number to EARFCN [282](#offset-of-nb-iot-channel-number-to-earfcn)

9.2.2.48 NB-IoT UL DL Alignment Offset [283](#nb-iot-ul-dl-alignment-offset)

9.2.2.49 TNL Capacity Indicator [283](#tnl-capacity-indicator)

9.2.2.50 Radio Resource Status [283](#radio-resource-status)

9.2.2.51 Composite Available Capacity Group [286](#composite-available-capacity-group)

9.2.2.52 Composite Available Capacity [286](#composite-available-capacity)

9.2.2.53 Cell Capacity Class Value [286](#cell-capacity-class-value)

9.2.2.54 Capacity Value [287](#capacity-value)

9.2.2.55 Slice Available Capacity [287](#slice-available-capacity)

9.2.2.56 RRC Connections [288](#rrc-connections)

9.2.2.57 Number of RRC Connections [288](#number-of-rrc-connections)

9.2.2.58 Available RRC Connection Capacity Value [288](#available-rrc-connection-capacity-value)

9.2.2.59 UE RLF Report [288](#ue-rlf-report)

9.2.2.60 Mobility Parameters Information [289](#mobility-parameters-information)

9.2.2.61 Mobility Parameters Modification Range [289](#mobility-parameters-modification-range)

9.2.2.62 Number of Active UEs [289](#number-of-active-ues)

9.2.2.63 NR Carrier List [290](#nr-carrier-list)

9.2.2.64 SSB Positions In Burst [290](#ssb-positions-in-burst)

9.2.2.65 NID [291](#nid)

9.2.2.66 CAG-Identifier [291](#cag-identifier)

9.2.2.67 Broadcast NID List [291](#broadcast-nid-list)

9.2.2.68 Broadcast SNPN ID List [291](#broadcast-snpn-id-list)

9.2.2.69 Broadcast CAG-Identifier List [292](#broadcast-cag-identifier-list)

9.2.2.70 Broadcast PNI-NPN ID Information [292](#broadcast-pni-npn-id-information)

9.2.2.71 NPN Broadcast Information [292](#npn-broadcast-information)

9.2.2.72 NPN Support [292](#npn-support)

9.2.2.73 Global Cell Identity [293](#global-cell-identity)

9.2.2.74 NPRACH Configuration [293](#nprach-configuration)

9.2.2.75 SFN Offset [294](#sfn-offset)

9.2.2.76 CHO Configuration [294](#cho-configuration)

9.2.2.77 SSB Offset Information [295](#ssb-offset-information)

9.2.2.78 SSB Offset Modification Range [295](#ssb-offset-modification-range)

9.2.2.79 Multiplexing Info [295](#multiplexing-info)

9.2.2.80 Traffic Index [296](#traffic-index)

9.2.2.81 Traffic Profile [296](#traffic-profile)

9.2.2.82 F1-Terminating Topology BH Information [296](#f1-terminating-topology-bh-information)

9.2.2.83 Non-F1-terminating Topology BH Information [297](#non-f1-terminating-topology-bh-information)

9.2.2.84 Traffic To Be Released Information [298](#traffic-to-be-released-information)

9.2.2.85 IAB TNL Address Request [298](#iab-tnl-address-request)

9.2.2.86 IAB TNL Address Response [299](#iab-tnl-address-response)

9.2.2.87 BAP Routing ID [299](#bap-routing-id)

9.2.2.88 BH RLC Channel ID [299](#bh-rlc-channel-id)

9.2.2.89 BAP Address [299](#bap-address)

9.2.2.90 BAP Path ID [300](#bap-path-id)

9.2.2.91 IAB QoS mapping information [300](#iab-qos-mapping-information)

9.2.2.92 IAB TNL Address [300](#iab-tnl-address)

9.2.2.93 IAB TNL Addresses Requested [300](#iab-tnl-addresses-requested)

9.2.2.94 IAB Cell Information [301](#iab-cell-information)

9.2.2.95 gNB-DU Cell Resource Configuration [302](#gnb-du-cell-resource-configuration)

9.2.2.96 IAB STC Info [304](#iab-stc-info)

9.2.2.97 RB Set Configuration [305](#rb-set-configuration)

9.2.2.98 IAB TNL Address Exception [305](#iab-tnl-address-exception)

9.2.2.99 BH Info List [305](#bh-info-list)

9.2.2.100 Non-UP traffic [306](#non-up-traffic)

9.2.2.101 Local NG-RAN Node Identifier [306](#local-ng-ran-node-identifier)

9.2.2.102 Served Cell Specific Info Request [307](#served-cell-specific-info-request)

9.2.2.103 CPAC Configuration [308](#cpac-configuration)

9.2.2.104 Radio Resource Status NR-U [308](#radio-resource-status-nr-u)

9.2.2.105 Mobile IAB Authorization Status [309](#mobile-iab-authorization-status)

9.2.2.106 Mobile IAB Cell [309](#mobile-iab-cell)

9.2.3 General IE definitions [309](#general-ie-definitions)

9.2.3.1 Message Type [309](#message-type)

9.2.3.2 Cause [309](#cause)

9.2.3.3 Criticality Diagnostics [316](#criticality-diagnostics)

9.2.3.4 Bit Rate [316](#bit-rate)

9.2.3.5 QoS Flow Level QoS Parameters [316](#qos-flow-level-qos-parameters)

9.2.3.6 GBR QoS Flow Information [317](#gbr-qos-flow-information)

9.2.3.7 Allocation and Retention Priority [318](#allocation-and-retention-priority)

9.2.3.8 Non dynamic 5QI Descriptor [319](#non-dynamic-5qi-descriptor)

9.2.3.9 Dynamic 5QI Descriptor [320](#dynamic-5qi-descriptor)

9.2.3.10 QoS Flow Identifier [321](#qos-flow-identifier)

9.2.3.11 Packet Loss Rate [321](#packet-loss-rate)

9.2.3.12 Packet Delay Budget [321](#packet-delay-budget)

9.2.3.13 Packet Error Rate [322](#packet-error-rate)

9.2.3.14 Averaging Window [322](#averaging-window)

9.2.3.15 Maximum Data Burst Volume [322](#maximum-data-burst-volume)

9.2.3.16 NG-RAN node UE XnAP ID [322](#ng-ran-node-ue-xnap-id)

9.2.3.17 UE Aggregate Maximum Bit Rate [322](#ue-aggregate-maximum-bit-rate)

9.2.3.18 PDU Session ID [323](#pdu-session-id)

9.2.3.19 PDU Session Type [323](#pdu-session-type)

9.2.3.20 TAI Support List [323](#tai-support-list)

9.2.3.21 S-NSSAI [324](#s-nssai)

9.2.3.22 Slice Support List [324](#slice-support-list)

9.2.3.23 Index to RAT/Frequency Selection Priority [324](#index-to-ratfrequency-selection-priority)

9.2.3.24 GUAMI [324](#guami)

9.2.3.25 Target Cell Global ID [325](#target-cell-global-id)

9.2.3.26 AMF UE NGAP ID [325](#amf-ue-ngap-id)

9.2.3.27 SCG Configuration Query [325](#scg-configuration-query)

9.2.3.28 RLC Mode [325](#rlc-mode)

9.2.3.29 Transport Layer Address [325](#transport-layer-address)

9.2.3.30 UP Transport Layer Information [326](#up-transport-layer-information)

9.2.3.31 CP Transport Layer Information [326](#cp-transport-layer-information)

9.2.3.32 Masked IMEISV [326](#masked-imeisv)

9.2.3.33 DRB ID [327](#drb-id)

9.2.3.34 DL Forwarding [327](#dl-forwarding)

9.2.3.35 Data Forwarding Accepted [327](#data-forwarding-accepted)

9.2.3.36 COUNT Value for PDCP SN Length 12 [327](#count-value-for-pdcp-sn-length-12)

9.2.3.37 COUNT Value for PDCP SN Length 18 [327](#count-value-for-pdcp-sn-length-18)

9.2.3.38 RAN Paging Area [327](#ran-paging-area)

9.2.3.39 RAN Area ID [328](#ran-area-id)

9.2.3.40 UE Context ID [328](#ue-context-id)

9.2.3.41 Assistance Data for RAN Paging [329](#assistance-data-for-ran-paging)

9.2.3.42 RAN Paging Attempt Information [329](#ran-paging-attempt-information)

9.2.3.43 UE RAN Paging Identity [329](#ue-ran-paging-identity)

9.2.3.44 Paging Priority [329](#paging-priority)

9.2.3.45 Delivery Status [330](#delivery-status)

9.2.3.46 I-RNTI [330](#i-rnti)

9.2.3.47 Location Reporting Information [330](#location-reporting-information)

9.2.3.48 Area of Interest Information [331](#area-of-interest-information)

9.2.3.49 UE Security Capabilities [331](#ue-security-capabilities)

9.2.3.50 AS Security Information [333](#as-security-information)

9.2.3.51 S-NG-RAN node Security Key [333](#s-ng-ran-node-security-key)

9.2.3.52 Security Indication [333](#security-indication)

9.2.3.53 Mobility Restriction List [334](#mobility-restriction-list)

9.2.3.54 Xn Benefit Value [336](#xn-benefit-value)

9.2.3.55 Trace Activation [336](#trace-activation)

9.2.3.56 Time To Wait [337](#time-to-wait)

9.2.3.57 QoS Flow Notification Control Indication Info [337](#qos-flow-notification-control-indication-info)

9.2.3.58 Request Reporting Reference ID [337](#request-reporting-reference-id)

9.2.3.59 User plane traffic activity report [337](#user-plane-traffic-activity-report)

9.2.3.60 Lower Layer presence status change [338](#lower-layer-presence-status-change)

9.2.3.61 RRC Resume Cause [338](#rrc-resume-cause)

9.2.3.62 Priority Level [338](#priority-level)

9.2.3.63 PDCP SN Length [338](#pdcp-sn-length)

9.2.3.64 UE History Information [338](#ue-history-information)

9.2.3.65 Last Visited Cell Information [339](#last-visited-cell-information)

9.2.3.66 Paging DRX [339](#paging-drx)

9.2.3.67 Security Result [339](#security-result)

9.2.3.68 UE Context Kept Indicator [339](#ue-context-kept-indicator)

9.2.3.69 PDU Session Aggregate Maximum Bit Rate [340](#pdu-session-aggregate-maximum-bit-rate)

9.2.3.70 LCID [340](#lcid)

9.2.3.71 Duplication Activation [340](#duplication-activation)

9.2.3.72 RRC Config Indication [340](#rrc-config-indication)

9.2.3.73 Maximum Integrity Protected Data Rate [340](#maximum-integrity-protected-data-rate)

9.2.3.74 PDCP Change Indication [341](#pdcp-change-indication)

9.2.3.75 UL Configuration [341](#ul-configuration)

9.2.3.76 UP Transport Parameters [341](#up-transport-parameters)

9.2.3.77 Desired Activity Notification Level [342](#desired-activity-notification-level)

9.2.3.78 Number of DRB IDs [342](#number-of-drb-ids)

9.2.3.79 QoS Flow Mapping Indication [342](#qos-flow-mapping-indication)

9.2.3.80 RLC Status [342](#rlc-status)

9.2.3.81 Expected UE Behaviour [343](#expected-ue-behaviour)

9.2.3.82 Expected UE Activity Behaviour [343](#expected-ue-activity-behaviour)

9.2.3.83 AMF Region Information [344](#amf-region-information)

9.2.3.84 TNL Association Usage [344](#tnl-association-usage)

9.2.3.85 Network Instance [344](#network-instance)

9.2.3.86 PDCP Duplication Configuration [344](#pdcp-duplication-configuration)

9.2.3.87 Secondary RAT Usage Information [345](#secondary-rat-usage-information)

9.2.3.88 Volume Timed Report List [345](#volume-timed-report-list)

9.2.3.89 Maximum IP Rate [346](#maximum-ip-rate)

9.2.3.90 UL Forwarding [346](#ul-forwarding)

9.2.3.91 UE Radio Capability for Paging [346](#ue-radio-capability-for-paging)

9.2.3.92 Common Network Instance [346](#common-network-instance)

9.2.3.93 Default DRB Allowed [347](#default-drb-allowed)

9.2.3.94 Split Session Indicator [347](#split-session-indicator)

9.2.3.95 UL Forwarding Proposal [347](#ul-forwarding-proposal)

9.2.3.96 TNL Configuration Info [347](#tnl-configuration-info)

9.2.3.97 NG-RAN Trace ID [348](#ng-ran-trace-id)

9.2.3.98 Non-GBR Resources Offered [348](#non-gbr-resources-offered)

9.2.3.99 Extended RAT Restriction Information [348](#extended-rat-restriction-information)

9.2.3.100 5GC Mobility Restriction List Container [349](#gc-mobility-restriction-list-container)

9.2.3.101 Maximum Number of CHO Preparations [349](#maximum-number-of-cho-preparations)

9.2.3.102 Alternative QoS Parameters Set List [349](#alternative-qos-parameters-set-list)

9.2.3.103 Alternative QoS Parameters Set Index [350](#alternative-qos-parameters-set-index)

9.2.3.104 Alternative QoS Parameters Set Notify Index [350](#alternative-qos-parameters-set-notify-index)

9.2.3.105 NR V2X Services Authorized [350](#nr-v2x-services-authorized)

9.2.3.106 LTE V2X Services Authorized [350](#lte-v2x-services-authorized)

9.2.3.107 NR UE Sidelink Aggregate Maximum Bit Rate [351](#nr-ue-sidelink-aggregate-maximum-bit-rate)

9.2.3.108 LTE UE Sidelink Aggregate Maximum Bit Rate [351](#lte-ue-sidelink-aggregate-maximum-bit-rate)

9.2.3.109 PC5 QoS Parameters [351](#pc5-qos-parameters)

9.2.3.110 UE History Information from the UE [352](#ue-history-information-from-the-ue)

9.2.3.111 RLC Duplication Information [352](#rlc-duplication-information)

9.2.3.112 Redundant PDU Session Information [352](#redundant-pdu-session-information)

9.2.3.113 Extended Packet Delay Budget [352](#extended-packet-delay-budget)

9.2.3.114 TSC Traffic Characteristics [353](#tsc-traffic-characteristics)

9.2.3.115 TSC Assistance Information [353](#tsc-assistance-information)

9.2.3.116 Periodicity [353](#periodicity)

9.2.3.117 Burst Arrival Time [353](#burst-arrival-time)

9.2.3.118 Redundant QoS Flow Indicator [353](#redundant-qos-flow-indicator)

9.2.3.119 NPN Mobility Information [354](#npn-mobility-information)

9.2.3.120 Allowed PNI-NPN ID List [354](#allowed-pni-npn-id-list)

9.2.3.121 NPN Paging Assistance Information [355](#npn-paging-assistance-information)

9.2.3.122 Void [355](#void)

9.2.3.123 PNI-NPN Restricted Information [355](#pni-npn-restricted-information)

9.2.3.124 URI [355](#uri)

9.2.3.125 MDT Configuration [355](#mdt-configuration)

9.2.3.126 MDT Configuration-NR [356](#mdt-configuration-nr)

9.2.3.127 MDT Configuration-EUTRA [359](#mdt-configuration-eutra)

9.2.3.128 M1 Configuration [360](#m1-configuration)

9.2.3.129 M4 Configuration [362](#m4-configuration)

9.2.3.130 M5 Configuration [362](#m5-configuration)

9.2.3.131 M6 Configuration [363](#m6-configuration)

9.2.3.132 M7 Configuration [363](#m7-configuration)

9.2.3.133 MDT PLMN List [363](#mdt-plmn-list)

9.2.3.134 Bluetooth Measurement Configuration [364](#bluetooth-measurement-configuration)

9.2.3.135 WLAN Measurement Configuration [364](#wlan-measurement-configuration)

9.2.3.136 Sensor Measurement Configuration [365](#sensor-measurement-configuration)

9.2.3.137 Logged Event Trigger Config [365](#logged-event-trigger-config)

9.2.3.138 UE Radio Capability ID [366](#ue-radio-capability-id)

9.2.3.139 Extended Slice Support List [366](#extended-slice-support-list)

9.2.3.140 Area Scope of Neighbour Cells [366](#area-scope-of-neighbour-cells)

9.2.3.141 Extended UE Identity Index Value [366](#extended-ue-identity-index-value)

9.2.3.142 E-UTRA Paging eDRX Information [366](#e-utra-paging-edrx-information)

9.2.3.143 UE Specific DRX [367](#ue-specific-drx)

9.2.3.144 QoS Mapping Information [367](#qos-mapping-information)

9.2.3.144a Hashed UE Identity Index Value [367](#a-hashed-ue-identity-index-value)

9.2.3.145 MRB ID [367](#mrb-id)

9.2.3.146 MBS Session ID [367](#mbs-session-id)

9.2.3.147 MRB Progress Information [368](#mrb-progress-information)

9.2.3.148 MBS Area Session ID [368](#mbs-area-session-id)

9.2.3.149 MBS Service Area information [368](#mbs-service-area-information)

9.2.3.150 MBS Service Area [368](#mbs-service-area)

9.2.3.151 SCG UE History Information [369](#scg-ue-history-information)

9.2.3.152 Survival Time [369](#survival-time)

9.2.3.153 Time Synchronisation Assistance Information [369](#time-synchronisation-assistance-information)

9.2.3.154 SCG Activation Request [370](#scg-activation-request)

9.2.3.155 SCG Activation Status [370](#scg-activation-status)

9.2.3.156 QMC Configuration Information [370](#qmc-configuration-information)

9.2.3.157 UE Application Layer Measurement Configuration Information [370](#ue-application-layer-measurement-configuration-information)

9.2.3.158 Available RAN Visible QoE Metrics [373](#available-ran-visible-qoe-metrics)

9.2.3.159 5G ProSe Authorized [373](#g-prose-authorized)

9.2.3.160 5G ProSe PC5 QoS Parameters [374](#g-prose-pc5-qos-parameters)

9.2.3.161 NR Paging eDRX Information [374](#nr-paging-edrx-information)

9.2.3.162 NR Paging eDRX Information for RRC INACTIVE [375](#nr-paging-edrx-information-for-rrc-inactive)

9.2.3.163 SDT Support Request [375](#sdt-support-request)

9.2.3.164 Partial UE Context Information for SDT [375](#partial-ue-context-information-for-sdt)

9.2.3.165 SRB ID [376](#srb-id)

9.2.3.166 PEIPS Assistance Information [376](#peips-assistance-information)

9.2.3.167 UE Slice Maximum Bit Rate List [376](#ue-slice-maximum-bit-rate-list)

9.2.3.168 Positioning Information [377](#positioning-information)

9.2.3.169 MDT PLMN Modification List [377](#mdt-plmn-modification-list)

9.2.3.170 TAI NSAG Support List [377](#tai-nsag-support-list)

9.2.3.171 Excess Packet Delay Threshold Configuration [378](#excess-packet-delay-threshold-configuration)

9.2.3.172 MT-SDT Information [378](#mt-sdt-information)

9.2.3.173 Partial UE Context Information for Positioning [378](#partial-ue-context-information-for-positioning)

9.2.3.174 DL LBT Failure Information [379](#dl-lbt-failure-information)

9.2.3.175 Aerial UE Subscription Information [379](#aerial-ue-subscription-information)

9.2.3.176 NR A2X Services Authorized [379](#nr-a2x-services-authorized)

9.2.3.177 LTE A2X Services Authorized [379](#lte-a2x-services-authorized)

9.2.3.178 A2X PC5 QoS Parameters [379](#a2x-pc5-qos-parameters)

9.2.3.179 UE Performance [380](#ue-performance)

9.2.3.180 Cell Based UE Trajectory Prediction [380](#cell-based-ue-trajectory-prediction)

9.2.3.181 Predicted Trajectory Cell Information [381](#predicted-trajectory-cell-information)

9.2.3.182 Measured UE Trajectory [381](#measured-ue-trajectory)

9.2.3.183 Measured Trajectory Cell Information [382](#_Toc232069401)

9.2.3.184 Data Collection ID [382](#data-collection-id)

9.2.3.185 UE Trajectory Collection Configuration [382](#ue-trajectory-collection-configuration)

9.2.3.186 UE Performance Collection Configuration [382](#ue-performance-collection-configuration)

9.2.3.187 Average Packet Delay [382](#average-packet-delay)

9.2.3.188 Candidate Relay UE Info List [383](#candidate-relay-ue-info-list)

9.2.3.189 Clock Quality Reporting Control Information [383](#clock-quality-reporting-control-information)

9.2.3.190 Clock Quality Acceptance Criteria [383](#clock-quality-acceptance-criteria)

9.2.3.191 CAG List for MDT [384](#cag-list-for-mdt)

9.2.3.192 S-CPAC Request Information [385](#s-cpac-request-information)

9.2.3.193 S-CPAC Security Configurations List [385](#s-cpac-security-configurations-list)

9.2.3.194 Complete Candidate Configuration Indicator [385](#complete-candidate-configuration-indicator)

9.2.3.195 NR Paging Long eDRX Information for RRC INACTIVE [385](#nr-paging-long-edrx-information-for-rrc-inactive)

9.2.3.196 MBS Assistance Information [386](#mbs-assistance-information)

9.2.3.197 QMC Coordination Request [386](#qmc-coordination-request)

9.2.3.198 QMC Coordination Response [388](#qmc-coordination-response)

9.2.3.199 Void [389](#void-1)

9.2.3.200 QoE and RVQoE Reporting Paths [389](#qoe-and-rvqoe-reporting-paths)

9.2.3.201 RAN Visible QoE Configuration [390](#ran-visible-qoe-configuration)

9.2.3.202 CHO-CPAC Information [390](#cho-cpac-information)

9.2.3.203 PDU Set QoS Information [390](#pdu-set-qos-information)

9.2.3.204 N6 Jitter Information [391](#n6-jitter-information)

9.2.3.205 ECN Marking or Congestion Information Reporting Request [391](#ecn-marking-or-congestion-information-reporting-request)

9.2.3.206 PDU Set based Handling Indicator [391](#pdu-set-based-handling-indicator)

9.2.3.207 TAI Slice Unavailable Cell List [391](#tai-slice-unavailable-cell-list)

9.2.3.208 Ranging and Sidelink Positioning Services Information [392](#ranging-and-sidelink-positioning-services-information)

9.2.3.209 RSPP Transport QoS Parameters [392](#rspp-transport-qos-parameters)

9.2.3.210 User Plane Failure Indication [393](#user-plane-failure-indication)

9.2.3.211 NRPPa Positioning Information [393](#nrppa-positioning-information)

9.2.3.212 Void [394](#void-2)

9.2.3.213 Void [394](#void-3)

9.2.3.214 Void [394](#void-4)

9.2.3.215 Void [394](#void-5)

9.2.3.216 Void [394](#void-6)

9.2.3.217 Void [394](#void-7)

9.2.3.218 Void [394](#void-8)

9.2.3.219 Void [394](#void-9)

9.2.3.220 Void [394](#void-10)

9.2.3.221 Void [394](#void-11)

9.2.3.222 Void [394](#void-12)

9.2.3.223 Void [394](#void-13)

9.2.3.224 Void [394](#void-14)

9.2.3.225 Void [394](#void-15)

9.2.3.226 Void [394](#void-16)

9.2.3.227 Void [394](#void-17)

9.2.3.228 Void [394](#void-18)

9.2.3.229 Void [394](#void-19)

9.2.3.230 Void [394](#void-20)

9.2.3.231 Void [394](#void-21)

9.2.3.232 Void [394](#void-22)

9.2.3.233 Void [394](#void-23)

9.2.3.234 Void [394](#void-24)

9.2.3.235 Void [394](#void-25)

9.2.3.236 Void [394](#void-26)

9.2.3.237 Void [395](#void-27)

9.2.3.238 Void [395](#void-28)

9.2.3.239 Void [395](#void-29)

9.2.3.240 Void [395](#void-30)

9.2.3.241 Void [395](#void-31)

9.2.3.242 Void [395](#void-32)

9.2.3.243 Void [395](#void-33)

9.2.3.244 Void [395](#void-34)

9.2.3.245 Void [395](#void-35)

9.2.3.246 Semi-persistent Positioning Information [395](#semi-persistent-positioning-information)

9.3 Message and Information Element Abstract Syntax (with ASN.1) [396](#message-and-information-element-abstract-syntax-with-asn.1)

9.3.1 General [396](#general-54)

9.3.2 Usage of Private Message Mechanism for Non-standard Use [396](#usage-of-private-message-mechanism-for-non-standard-use)

9.3.3 Elementary Procedure Definitions [397](#elementary-procedure-definitions)

9.3.4 PDU Definitions [410](#pdu-definitions)

9.3.5 Information Element definitions [479](#information-element-definitions-1)

9.3.6 Common definitions [654](#common-definitions)

9.3.7 Constant definitions [655](#constant-definitions)

9.3.8 Container definitions [668](#container-definitions)

9.4 Message transfer syntax [673](#message-transfer-syntax)

9.5 Timers [673](#timers)

10 Handling of unknown, unforeseen and erroneous protocol data [673](#handling-of-unknown-unforeseen-and-erroneous-protocol-data)

Annex A (informative): Change history [674](#annex-a-informative-change-history)

#  Foreword

This Technical Specification has been produced by the 3<sup>rd</sup> Generation Partnership Project (3GPP).

The contents of the present document are subject to continuing work within the TSG and may change following formal TSG approval. Should the TSG modify the contents of the present document, it will be re-released by the TSG with an identifying change of release date and an increase in version number as follows:

Version x.y.z

where:

x the first digit:

1 presented to TSG for information;

2 presented to TSG for approval;

3 or greater indicates TSG approved document under change control.

y the second digit is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc.

z the third digit is incremented when editorial only changes have been incorporated in the document.
