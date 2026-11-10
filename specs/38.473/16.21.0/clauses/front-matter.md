3GPP TS 38.473 V16.21.0 (2025-03)

Technical Specification

3rd Generation Partnership Project;

Technical Specification Group Radio Access Network;

NG-RAN;

F1 application protocol (F1AP)

(Release 16)

<img src="media/image1.jpeg" style="width:1.32569in;height:1.32569in" /> <img src="media/image2.png" style="width:1.77778in;height:1.03681in" />

The present document has been developed within the 3rd Generation Partnership Project (3GPP <sup>TM</sup>) and may be further elaborated for the purposes of 3GPP..  
The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented.  
This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification.  
Specifications and Reports for implementation of the 3GPP <sup>TM</sup> system should be obtained via the 3GPP Organizational Partners' Publications Offices.

> Keywords
>
> NG-RAN, Radio
>
> ***3GPP***
>
> Postal address
>
> 3GPP support office address
>
> 650 Route des Lucioles - Sophia Antipolis
>
> Valbonne - FRANCE
>
> Tel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16
>
> Internet
>
> http://www.3gpp.org

***Copyright Notification***

No part may be reproduced except as authorized by written permission.  
The copyright and the foregoing restriction extend to reproduction in all media.

© 2025, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC).

All rights reserved.

UMTS™ is a Trade Mark of ETSI registered for the benefit of its members

3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners  
LTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners

GSM® and the GSM logo are registered and owned by the GSM Association

#  Contents

Foreword [14](#foreword)

1 Scope [15](#scope)

2 References [15](#references)

3 Definitions and abbreviations [17](#definitions-and-abbreviations)

3.1 Definitions [17](#definitions)

3.2 Abbreviations [18](#abbreviations)

4 General [19](#general)

4.1 Procedure specification principles [19](#procedure-specification-principles)

4.2 Forwards and backwards compatibility [19](#forwards-and-backwards-compatibility)

4.3 Specification notations [19](#specification-notations)

5 F1AP services [20](#f1ap-services)

6 Services expected from signalling transport [20](#services-expected-from-signalling-transport)

7 Functions of F1AP [20](#functions-of-f1ap)

8 F1AP procedures [20](#f1ap-procedures)

8.1 List of F1AP Elementary procedures [20](#list-of-f1ap-elementary-procedures)

8.2 Interface Management procedures [23](#interface-management-procedures)

8.2.1 Reset [23](#reset)

8.2.1.1 General [23](#general-1)

8.2.1.2 Successful Operation [23](#successful-operation)

8.2.1.2.1 Reset Procedure Initiated from the gNB-CU [23](#reset-procedure-initiated-from-the-gnb-cu)

8.2.1.2.2 Reset Procedure Initiated from the gNB-DU [24](#reset-procedure-initiated-from-the-gnb-du)

8.2.1.3 Abnormal Conditions [25](#abnormal-conditions)

8.2.2 Error Indication [25](#error-indication)

8.2.2.1 General [25](#general-2)

8.2.2.2 Successful Operation [25](#successful-operation-1)

8.2.2.3 Abnormal Conditions [25](#abnormal-conditions-1)

8.2.3 F1 Setup [25](#f1-setup)

8.2.3.1 General [25](#general-3)

8.2.3.2 Successful Operation [26](#successful-operation-2)

8.2.3.3 Unsuccessful Operation [28](#unsuccessful-operation)

8.2.3.4 Abnormal Conditions [28](#abnormal-conditions-2)

8.2.4 gNB-DU Configuration Update [28](#gnb-du-configuration-update)

8.2.4.1 General [28](#general-4)

8.2.4.2 Successful Operation [28](#successful-operation-3)

8.2.4.3 Unsuccessful Operation [30](#unsuccessful-operation-1)

8.2.4.4 Abnormal Conditions [31](#abnormal-conditions-3)

8.2.5 gNB-CU Configuration Update [31](#gnb-cu-configuration-update)

8.2.5.1 General [31](#general-5)

8.2.5.2 Successful Operation [31](#successful-operation-4)

8.2.5.3 Unsuccessful Operation [33](#unsuccessful-operation-2)

8.2.5.4 Abnormal Conditions [33](#abnormal-conditions-4)

8.2.6 gNB-DU Resource Coordination [34](#gnb-du-resource-coordination)

8.2.6.1 General [34](#general-6)

8.2.6.2 Successful Operation [34](#successful-operation-5)

8.2.7 gNB-DU Status Indication [34](#gnb-du-status-indication)

8.2.7.1 General [34](#general-7)

8.2.7.2 Successful Operation [34](#successful-operation-6)

8.2.7.3 Abnormal Conditions [35](#abnormal-conditions-5)

8.2.8 F1 Removal [35](#f1-removal)

8.2.8.1 General [35](#general-8)

8.2.8.2 Successful Operation [35](#successful-operation-7)

8.2.8.3 Unsuccessful Operation [36](#unsuccessful-operation-3)

8.2.8.4 Abnormal Conditions [36](#abnormal-conditions-6)

8.2.9 Network Access Rate Reduction [36](#network-access-rate-reduction)

8.2.9.1 General [36](#general-9)

8.2.9.2 Successful operation [37](#successful-operation-8)

8.2.9.3 Abnormal Conditions [37](#abnormal-conditions-7)

8.2.10 Resource Status Reporting Initiation [37](#resource-status-reporting-initiation)

8.2.10.1 General [37](#general-10)

8.2.10.2 Successful Operation [37](#successful-operation-9)

8.2.10.3 Unsuccessful Operation [38](#unsuccessful-operation-4)

8.2.10.4 Abnormal Conditions [39](#abnormal-conditions-8)

8.2.11 Resource Status Reporting [39](#resource-status-reporting)

8.2.11.1 General [39](#general-11)

8.2.11.2 Successful Operation [39](#successful-operation-10)

8.2.11.3 Unsuccessful Operation [39](#unsuccessful-operation-5)

8.2.11.4 Abnormal Conditions [39](#abnormal-conditions-9)

8.3 UE Context Management procedures [40](#ue-context-management-procedures)

8.3.1 UE Context Setup [40](#ue-context-setup)

8.3.1.1 General [40](#general-12)

8.3.1.2 Successful Operation [40](#successful-operation-11)

8.3.1.3 Unsuccessful Operation [45](#unsuccessful-operation-6)

8.3.1.4 Abnormal Conditions [46](#abnormal-conditions-10)

8.3.2 UE Context Release Request (gNB-DU initiated) [46](#ue-context-release-request-gnb-du-initiated)

8.3.2.1 General [46](#general-13)

8.3.2.2 Successful Operation [46](#successful-operation-12)

8.3.2.3 Abnormal Conditions [47](#abnormal-conditions-11)

8.3.3 UE Context Release (gNB-CU initiated) [47](#ue-context-release-gnb-cu-initiated)

8.3.3.1 General [47](#general-14)

8.3.3.2 Successful Operation [47](#successful-operation-13)

8.3.3.4 Abnormal Conditions [48](#abnormal-conditions-12)

8.3.4 UE Context Modification (gNB-CU initiated) [48](#ue-context-modification-gnb-cu-initiated)

8.3.4.1 General [48](#general-15)

8.3.4.2 Successful Operation [48](#successful-operation-14)

8.3.4.3 Unsuccessful Operation [55](#unsuccessful-operation-7)

8.3.4.4 Abnormal Conditions [55](#abnormal-conditions-13)

8.3.5 UE Context Modification Required (gNB-DU initiated) [56](#ue-context-modification-required-gnb-du-initiated)

8.3.5.1 General [56](#general-16)

8.3.5.2 Successful Operation [56](#successful-operation-15)

8.3.5.2A Unsuccessful Operation [57](#a-unsuccessful-operation)

8.3.5.3 Abnormal Conditions [58](#abnormal-conditions-14)

8.3.6 UE Inactivity Notification [58](#ue-inactivity-notification)

8.3.6.1 General [58](#general-17)

8.3.6.2 Successful Operation [58](#successful-operation-16)

8.3.6.3 Abnormal Conditions [58](#abnormal-conditions-15)

8.3.7 Notify [58](#notify)

8.3.7.1 General [58](#general-18)

8.3.7.2 Successful Operation [59](#successful-operation-17)

8.3.7.3 Abnormal Conditions [59](#abnormal-conditions-16)

8.3.8 Access Success [59](#access-success)

8.3.8.1 General [59](#general-19)

8.3.8.2 Successful Operation [59](#successful-operation-18)

8.3.8.3 Abnormal Conditions [60](#abnormal-conditions-17)

8.4 RRC Message Transfer procedures [60](#rrc-message-transfer-procedures)

8.4.1 Initial UL RRC Message Transfer [60](#initial-ul-rrc-message-transfer)

8.4.1.1 General [60](#general-20)

8.4.1.2 Successful operation [60](#successful-operation-19)

8.4.1.3 Abnormal Conditions [60](#abnormal-conditions-18)

8.4.2 DL RRC Message Transfer [60](#dl-rrc-message-transfer)

8.4.2.1 General [60](#general-21)

8.4.2.2 Successful operation [61](#successful-operation-20)

8.4.2.3 Abnormal Conditions [61](#abnormal-conditions-19)

8.4.3 UL RRC Message Transfer [61](#ul-rrc-message-transfer)

8.4.3.1 General [61](#general-22)

8.4.3.2 Successful operation [62](#successful-operation-21)

8.4.3.3 Abnormal Conditions [62](#abnormal-conditions-20)

8.4.4 RRC Delivery Report [62](#rrc-delivery-report)

8.4.4.1 General [62](#general-23)

8.4.4.2 Successful operation [62](#successful-operation-22)

8.4.4.3 Abnormal Conditions [62](#abnormal-conditions-21)

8.5 Warning Message Transmission Procedures [63](#warning-message-transmission-procedures)

8.5.1 Write-Replace Warning [63](#write-replace-warning)

8.5.1.1 General [63](#general-24)

8.5.1.2 Successful Operation [63](#successful-operation-23)

8.5.1.3 Unsuccessful Operation [64](#unsuccessful-operation-8)

8.5.1.4 Abnormal Conditions [64](#abnormal-conditions-22)

8.5.2 PWS Cancel [64](#pws-cancel)

8.5.2.1 General [64](#general-25)

8.5.2.2 Successful Operation [64](#successful-operation-24)

8.5.2.3 Unsuccessful Operation [65](#unsuccessful-operation-9)

8.5.3 PWS Restart Indication [65](#pws-restart-indication)

8.5.3.1 General [65](#general-26)

8.5.3.2 Successful Operation [65](#successful-operation-25)

8.5.3.3 Abnormal Conditions [65](#abnormal-conditions-23)

8.5.4 PWS Failure Indication [65](#pws-failure-indication)

8.5.4.1 General [65](#general-27)

8.5.4.2 Successful Operation [66](#successful-operation-26)

8.5.4.3 Abnormal Conditions [66](#abnormal-conditions-24)

8.6 System Information Procedures [66](#system-information-procedures)

8.6.1 System Information Delivery [66](#system-information-delivery)

8.6.1.1 General [66](#general-28)

8.6.1.2 Successful Operation [66](#successful-operation-27)

8.6.1.3 Abnormal Conditions [67](#abnormal-conditions-25)

8.7 Paging procedures [67](#paging-procedures)

8.7.1 Paging [67](#paging)

8.7.1.1 General [67](#general-29)

8.7.1.2 Successful Operation [67](#successful-operation-28)

8.7.1.3 Abnormal Conditions [67](#abnormal-conditions-26)

8.8 Trace Procedures [67](#trace-procedures)

8.8.1 Trace Start [67](#trace-start)

8.8.1.1 General [67](#general-30)

8.8.1.2 Successful Operation [68](#successful-operation-29)

8.8.1.3 Abnormal Conditions [68](#abnormal-conditions-27)

8.8.2 Deactivate Trace [68](#deactivate-trace)

8.8.2.1 General [68](#general-31)

8.8.2.2 Successful Operation [68](#successful-operation-30)

8.8.2.3 Abnormal Conditions [68](#abnormal-conditions-28)

8.8.3 Cell Traffic Trace [69](#cell-traffic-trace)

8.8.3.1 General [69](#general-32)

8.8.3.2 Successful Operation [69](#successful-operation-31)

8.8.3.3 Abnormal Conditions [69](#abnormal-conditions-29)

8.9 Radio Information Transfer procedures [69](#radio-information-transfer-procedures)

8.9.1 DU-CU Radio Information Transfer [69](#du-cu-radio-information-transfer)

8.9.1.1 General [69](#general-33)

8.9.1.2 Successful operation [69](#successful-operation-32)

8.9.1.3 Abnormal Conditions [70](#abnormal-conditions-30)

8.9.2 CU-DU Radio Information Transfer [70](#cu-du-radio-information-transfer)

8.9.2.1 General [70](#general-34)

8.9.2.2 Successful operation [70](#successful-operation-33)

8.9.2.3 Abnormal Conditions [70](#abnormal-conditions-31)

8.10 IAB Procedures [70](#iab-procedures)

8.10.0 General [70](#general-35)

8.10.1 BAP Mapping Configuration [70](#bap-mapping-configuration)

8.10.1.1 General [70](#general-36)

8.10.1.2 Successful Operation [71](#successful-operation-34)

8.10.1.A Unsuccessful Operation [71](#a-unsuccessful-operation-1)

8.10.1.3 Abnormal Conditions [72](#abnormal-conditions-32)

8.10.2 gNB-DU Resource Configuration [72](#gnb-du-resource-configuration)

8.10.2.1 General [72](#general-37)

8.10.2.2 Successful Operation [72](#successful-operation-35)

8.10.2.B Unsuccessful Operation [73](#b-unsuccessful-operation)

8.10.2.3 Abnormal Conditions [73](#abnormal-conditions-33)

8.10.3 IAB TNL Address Allocation [73](#iab-tnl-address-allocation)

8.10.3.1 General [73](#general-38)

8.10.3.2 Successful Operation [73](#successful-operation-36)

8.10.3.C Unsuccessful Operation [74](#c-unsuccessful-operation)

8.10.3.3 Abnormal Conditions [74](#abnormal-conditions-34)

8.10.4 IAB UP Configuration Update [74](#iab-up-configuration-update)

8.10.4.1 General [74](#general-39)

8.10.4.2 Successful Operation [75](#successful-operation-37)

8.10.4.3 Unsuccessful Operation [75](#unsuccessful-operation-10)

8.10.4.4 Abnormal Conditions [75](#abnormal-conditions-35)

8.11 Self Optimisation Support procedures [76](#self-optimisation-support-procedures)

8.11.1 Access and Mobility Indication [76](#access-and-mobility-indication)

8.11.1.1 General [76](#general-40)

8.11.1.2 Successful Operation [76](#successful-operation-38)

8.11.1.3 Abnormal Conditions [76](#abnormal-conditions-36)

8.12 Reference Time Information Reporting procedures [76](#reference-time-information-reporting-procedures)

8.12.1 Reference Time Information Reporting Control [76](#reference-time-information-reporting-control)

8.12.1.1 General [76](#general-41)

8.12.1.2 Successful Operation [76](#successful-operation-39)

8.12.1.3 Abnormal Conditions [77](#abnormal-conditions-37)

8.12.2 Reference Time Information Report [77](#reference-time-information-report)

8.12.2.1 General [77](#general-42)

8.12.2.2 Successful Operation [77](#successful-operation-40)

8.12.2.3 Abnormal Conditions [77](#abnormal-conditions-38)

8.13 Positioning Procedures [78](#positioning-procedures)

8.13.1 Positioning Assistance Information Control [78](#positioning-assistance-information-control)

8.13.1.1 General [78](#general-43)

8.13.1.2 Successful Operation [78](#successful-operation-41)

8.13.1.3 Abnormal Conditions [78](#abnormal-conditions-39)

8.13.2 Positioning Assistance Information Feedback [78](#positioning-assistance-information-feedback)

8.13.2.1 General [78](#general-44)

8.13.2.2 Successful Operation [79](#successful-operation-42)

8.13.2.3 Abnormal Conditions [79](#abnormal-conditions-40)

8.13.3 Positioning Measurement [79](#positioning-measurement)

8.13.3.1 General [79](#general-45)

8.13.3.2 Successful Operation [79](#successful-operation-43)

8.13.3.3 Unsuccessful Operation [80](#unsuccessful-operation-11)

8.13.3.4 Abnormal Conditions [80](#abnormal-conditions-41)

8.13.4 Positioning Measurement Report [80](#positioning-measurement-report)

8.13.4.1 General [80](#general-46)

8.13.4.2 Successful Operation [81](#successful-operation-44)

8.13.4.3 Unsuccessful Operation [81](#unsuccessful-operation-12)

8.13.4.4 Abnormal Conditions [81](#abnormal-conditions-42)

8.13.5 Positioning Measurement Abort [81](#positioning-measurement-abort)

8.13.5.1 General [81](#general-47)

8.13.5.2 Successful Operation [81](#successful-operation-45)

8.13.5.3 Unsuccessful Operation [81](#unsuccessful-operation-13)

8.13.5.4 Abnormal Conditions [81](#abnormal-conditions-43)

8.13.6 Positioning Measurement Failure Indication [82](#positioning-measurement-failure-indication)

8.13.6.1 General [82](#general-48)

8.13.6.2 Successful Operation [82](#successful-operation-46)

8.13.6.3 Unsuccessful Operation [82](#unsuccessful-operation-14)

8.13.6.4 Abnormal Conditions [82](#abnormal-conditions-44)

8.13.7 Positioning Measurement Update [82](#positioning-measurement-update)

8.13.7.1 General [82](#general-49)

8.13.7.2 Successful Operation [82](#successful-operation-47)

8.13.7.3 Unsuccessful Operation [83](#unsuccessful-operation-15)

8.13.7.4 Abnormal Conditions [83](#abnormal-conditions-45)

8.13.8 TRP Information Exchange [83](#trp-information-exchange)

8.13.8.1 General [83](#general-50)

8.13.8.2 Successful Operation [83](#successful-operation-48)

8.13.8.3 Unsuccessful Operation [84](#unsuccessful-operation-16)

8.13.9 Positioning Information Exchange [84](#positioning-information-exchange)

8.13.9.1 General [84](#general-51)

8.13.9.2 Successful Operation [84](#successful-operation-49)

8.13.9.3 Unsuccessful Operation [85](#unsuccessful-operation-17)

8.13.10 Positioning Activation [85](#positioning-activation)

8.13.10.1 General [85](#general-52)

8.13.10.2 Successful Operation [85](#successful-operation-50)

8.13.10.3 Unsuccessful Operation [86](#unsuccessful-operation-18)

8.13.10.4 Abnormal Conditions [86](#abnormal-conditions-46)

8.13.11 Positioning Deactivation [86](#positioning-deactivation)

8.13.11.1 General [86](#general-53)

8.13.11.2 Successful Operation [86](#successful-operation-51)

8.13.11.3 Unsuccessful Operation [86](#unsuccessful-operation-19)

8.13.11.4 Abnormal Conditions [87](#abnormal-conditions-47)

8.13.12 E-CID Measurement Initiation [87](#e-cid-measurement-initiation)

8.13.12.1 General [87](#general-54)

8.13.12.2 Successful Operation [87](#successful-operation-52)

8.13.12.3 Unsuccessful Operation [87](#unsuccessful-operation-20)

8.13.13 E-CID Measurement Failure Indication [88](#e-cid-measurement-failure-indication)

8.13.13.1 General [88](#general-55)

8.13.13.2 Successful Operation [88](#successful-operation-53)

8.13.13.3 Unsuccessful Operation [88](#unsuccessful-operation-21)

8.13.14 E-CID Measurement Report [88](#e-cid-measurement-report)

8.13.14.1 General [88](#general-56)

8.13.14.2 Successful Operation [88](#successful-operation-54)

8.13.14.3 Unsuccessful Operation [89](#unsuccessful-operation-22)

8.13.15 E-CID Measurement Termination [89](#e-cid-measurement-termination)

8.13.15.1 General [89](#general-57)

8.13.15.2 Successful Operation [89](#successful-operation-55)

8.13.15.3 Unsuccessful Operation [89](#unsuccessful-operation-23)

8.13.16 Positioning Information Update [89](#positioning-information-update)

8.13.16.1 General [89](#general-58)

8.13.16.2 Successful Operation [89](#successful-operation-56)

8.13.16.3 Unsuccessful Operation [90](#unsuccessful-operation-24)

8.13.16.4 Abnormal Conditions [90](#abnormal-conditions-48)

8.13.17 Positioning System Information Delivery [90](#positioning-system-information-delivery)

8.13.17.1 General [90](#general-59)

8.13.17.2 Successful Operation [90](#successful-operation-57)

8.13.17.3 Abnormal Conditions [90](#abnormal-conditions-49)

9 Elements for F1AP Communication [91](#elements-for-f1ap-communication)

9.1 General [91](#general-60)

9.2 Message Functional Definition and Content [91](#message-functional-definition-and-content)

9.2.1 Interface Management messages [91](#interface-management-messages)

9.2.1.1 RESET [91](#reset-1)

9.2.1.2 RESET ACKNOWLEDGE [92](#reset-acknowledge)

9.2.1.3 ERROR INDICATION [92](#error-indication-1)

9.2.1.4 F1 SETUP REQUEST [92](#f1-setup-request)

9.2.1.5 F1 SETUP RESPONSE [93](#f1-setup-response)

9.2.1.6 F1 SETUP FAILURE [94](#f1-setup-failure)

9.2.1.7 GNB-DU CONFIGURATION UPDATE [94](#gnb-du-configuration-update-1)

9.2.1.8 GNB-DU CONFIGURATION UPDATE ACKNOWLEDGE [96](#gnb-du-configuration-update-acknowledge)

9.2.1.9 GNB-DU CONFIGURATION UPDATE FAILURE [97](#gnb-du-configuration-update-failure)

9.2.1.10 GNB-CU CONFIGURATION UPDATE [97](#gnb-cu-configuration-update-1)

9.2.1.11 GNB-CU CONFIGURATION UPDATE ACKNOWLEDGE [101](#gnb-cu-configuration-update-acknowledge)

9.2.1.12 GNB-CU CONFIGURATION UPDATE FAILURE [102](#gnb-cu-configuration-update-failure)

9.2.1.13 GNB-DU RESOURCE COORDINATION REQUEST [102](#gnb-du-resource-coordination-request)

9.2.1.14 GNB-DU RESOURCE COORDINATION RESPONSE [103](#gnb-du-resource-coordination-response)

9.2.1.15 GNB-DU STATUS INDICATION [103](#gnb-du-status-indication-1)

9.2.1.16 F1 REMOVAL REQUEST [104](#f1-removal-request)

9.2.1.17 F1 REMOVAL RESPONSE [104](#f1-removal-response)

9.2.1.18 F1 REMOVAL FAILURE [104](#f1-removal-failure)

9.2.1.19 NETWORK ACCESS RATE REDUCTION [104](#network-access-rate-reduction-1)

9.2.1.20 RESOURCE STATUS REQUEST [105](#resource-status-request)

9.2.1.21 RESOURCE STATUS RESPONSE [106](#resource-status-response)

9.2.1.22 RESOURCE STATUS FAILURE [107](#resource-status-failure)

9.2.1.23 RESOURCE STATUS UPDATE [107](#resource-status-update)

9.2.2 UE Context Management messages [107](#ue-context-management-messages)

9.2.2.1 UE CONTEXT SETUP REQUEST [107](#ue-context-setup-request)

9.2.2.2 UE CONTEXT SETUP RESPONSE [112](#ue-context-setup-response)

9.2.2.3 UE CONTEXT SETUP FAILURE [115](#ue-context-setup-failure)

9.2.2.4 UE CONTEXT RELEASE REQUEST [116](#ue-context-release-request)

9.2.2.5 UE CONTEXT RELEASE COMMAND [116](#ue-context-release-command)

9.2.2.6 UE CONTEXT RELEASE COMPLETE [117](#ue-context-release-complete)

9.2.2.7 UE CONTEXT MODIFICATION REQUEST [117](#ue-context-modification-request)

9.2.2.8 UE CONTEXT MODIFICATION RESPONSE [125](#ue-context-modification-response)

9.2.2.9 UE CONTEXT MODIFICATION FAILURE [130](#ue-context-modification-failure)

9.2.2.10 UE CONTEXT MODIFICATION REQUIRED [130](#ue-context-modification-required)

9.2.2.11 UE CONTEXT MODIFICATION CONFIRM [132](#_Toc192843135)

9.2.2.11A UE CONTEXT MODIFICATION REFUSE [133](#a-ue-context-modification-refuse)

9.2.2.12 UE INACTIVITY NOTIFICATION [134](#ue-inactivity-notification-1)

9.2.2.13 NOTIFY [134](#notify-1)

9.2.2.14 ACCESS SUCCESS [135](#access-success-1)

9.2.3 RRC Message Transfer messages [135](#rrc-message-transfer-messages)

9.2.3.1 INITIAL UL RRC MESSAGE TRANSFER [135](#initial-ul-rrc-message-transfer-1)

9.2.3.2 DL RRC MESSAGE TRANSFER [136](#dl-rrc-message-transfer-1)

9.2.3.3 UL RRC MESSAGE TRANSFER [136](#ul-rrc-message-transfer-1)

9.2.3.4 RRC DELIVERY REPORT [137](#rrc-delivery-report-1)

9.2.4 Warning Message Transmission Messages [137](#warning-message-transmission-messages)

9.2.4.1 WRITE-REPLACE WARNING REQUEST [137](#write-replace-warning-request)

9.2.4.2 WRITE-REPLACE WARNING RESPONSE [138](#write-replace-warning-response)

9.2.4.3 PWS CANCEL REQUEST [138](#pws-cancel-request)

9.2.4.4 PWS CANCEL RESPONSE [139](#pws-cancel-response)

9.2.4.5 PWS RESTART INDICATION [139](#pws-restart-indication-1)

9.2.4.6 PWS FAILURE INDICATION [140](#pws-failure-indication-1)

9.2.5 System Information messages [140](#system-information-messages)

9.2.5.1 SYSTEM INFORMATION DELIVERY COMMAND [140](#system-information-delivery-command)

9.2.6 Paging messages [141](#paging-messages)

9.2.6.1 PAGING [141](#paging-1)

9.2.7 Trace Messages [141](#trace-messages)

9.2.7.1 TRACE START [141](#trace-start-1)

9.2.7.2 DEACTIVATE TRACE [142](#deactivate-trace-1)

9.2.7.3 CELL TRAFFIC TRACE [142](#cell-traffic-trace-1)

9.2.8 Radio Information Transfer messages [142](#radio-information-transfer-messages)

9.2.8.1 DU-CU RADIO INFORMATION TRANSFER [142](#du-cu-radio-information-transfer-1)

9.2.8.2 CU-DU RADIO INFORMATION TRANSFER [143](#cu-du-radio-information-transfer-1)

9.2.9 IAB messages [143](#iab-messages)

9.2.9.1 BAP MAPPING CONFIGURATION [143](#bap-mapping-configuration-1)

9.2.9.2 BAP MAPPING CONFIGURATION ACKNOWLEDGE [144](#bap-mapping-configuration-acknowledge)

9.2.9.2A BAP MAPPING CONFIGURATION FAILURE [144](#a-bap-mapping-configuration-failure)

9.2.9.3 GNB-DU RESOURCE CONFIGURATION [144](#gnb-du-resource-configuration-1)

9.2.9.4 GNB-DU RESOURCE CONFIGURATION ACKNOWLEDGE [147](#gnb-du-resource-configuration-acknowledge)

9.2.9.4A GNB-DU RESOURCE CONFIGURATION FAILURE [147](#a-gnb-du-resource-configuration-failure)

9.2.9.5 IAB TNL ADDRESS REQUEST [147](#iab-tnl-address-request)

9.2.9.6 IAB TNL ADDRESS RESPONSE [148](#iab-tnl-address-response)

9.2.9.6A IAB TNL ADDRESS FAILURE [148](#a-iab-tnl-address-failure)

9.2.9.7 IAB UP CONFIGURATION UPDATE REQUEST [148](#iab-up-configuration-update-request)

9.2.9.8 IAB UP CONFIGURATION UPDATE RESPONSE [149](#iab-up-configuration-update-response)

9.2.9.9 IAB UP CONFIGURATION UPDATE FAILURE [150](#iab-up-configuration-update-failure)

9.2.10 Self Optimisation Support Messages [150](#self-optimisation-support-messages)

9.2.10.1 ACCESS AND MOBILITY INDICATION [150](#access-and-mobility-indication-1)

9.2.11 Reference Time Information Reporting messages [151](#reference-time-information-reporting-messages)

9.2.11.1 REFERENCE TIME INFORMATION REPORTING CONTROL [151](#reference-time-information-reporting-control-1)

9.2.11.2 REFERENCE TIME INFORMATION REPORT [151](#reference-time-information-report-1)

9.2.12 Messages for Positioning Procedures [151](#messages-for-positioning-procedures)

9.2.12.1 POSITIONING ASSISTANCE INFORMATION CONTROL [152](#positioning-assistance-information-control-1)

9.2.12.2 POSITIONING ASSISTANCE INFORMATION FEEDBACK [152](#positioning-assistance-information-feedback-1)

9.2.12.3 POSITIONING MEASUREMENT REQUEST [152](#positioning-measurement-request)

9.2.12.4 POSITIONING MEASUREMENT RESPONSE [154](#positioning-measurement-response)

9.2.12.5 POSITIONING MEASUREMENT FAILURE [154](#positioning-measurement-failure)

9.2.12.6 POSITIONING MEASUREMENT REPORT [155](#positioning-measurement-report-1)

9.2.12.7 POSITIONING MEASUREMENT ABORT [155](#positioning-measurement-abort-1)

9.2.12.8 POSITIONING MEASUREMENT FAILURE INDICATION [155](#positioning-measurement-failure-indication-1)

9.2.12.9 POSITIONING MEASUREMENT UPDATE [156](#positioning-measurement-update-1)

9.2.12.10 TRP INFORMATION REQUEST [156](#trp-information-request)

9.2.12.11 TRP INFORMATION RESPONSE [156](#trp-information-response)

9.2.12.12 TRP INFORMATION FAILURE [157](#trp-information-failure)

9.2.12.13 POSITIONING INFORMATION REQUEST [157](#positioning-information-request)

9.2.12.14 POSITIONING INFORMATION RESPONSE [157](#positioning-information-response)

9.2.12.15 POSITIONING INFORMATION FAILURE [158](#positioning-information-failure)

9.2.12.16 POSITIONING ACTIVATION REQUEST [158](#positioning-activation-request)

9.2.12.17 POSITIONING ACTIVATION RESPONSE [158](#positioning-activation-response)

9.2.12.18 POSITIONING ACTIVATION FAILURE [159](#positioning-activation-failure)

9.2.12.19 POSITIONING DEACTIVATION [159](#positioning-deactivation-1)

9.2.12.20 E-CID MEASUREMENT INITIATION REQUEST [159](#e-cid-measurement-initiation-request)

9.2.12.21 E-CID MEASUREMENT INITIATION RESPONSE [160](#e-cid-measurement-initiation-response)

9.2.12.22 E-CID MEASUREMENT INITIATION FAILURE [161](#e-cid-measurement-initiation-failure)

9.2.12.23 E-CID MEASUREMENT FAILURE INDICATION [161](#e-cid-measurement-failure-indication-1)

9.2.12.24 E-CID MEASUREMENT REPORT [161](#e-cid-measurement-report-1)

9.2.12.25 E-CID MEASUREMENT TERMINATION COMMAND [162](#e-cid-measurement-termination-command)

9.2.12.26 POSITIONING INFORMATION UPDATE [162](#positioning-information-update-1)

9.2.12.27 POSITIONING SYSTEM INFORMATION DELIVERY COMMAND [162](#positioning-system-information-delivery-command)

9.3 Information Element Definitions [162](#information-element-definitions)

9.3.1 Radio Network Layer Related IEs [163](#radio-network-layer-related-ies)

9.3.1.1 Message Type [163](#message-type)

9.3.1.2 Cause [163](#cause)

9.3.1.3 Criticality Diagnostics [166](#criticality-diagnostics)

9.3.1.4 gNB-CU UE F1AP ID [167](#gnb-cu-ue-f1ap-id)

9.3.1.5 gNB-DU UE F1AP ID [167](#gnb-du-ue-f1ap-id)

9.3.1.6 RRC-Container [167](#rrc-container)

9.3.1.7 SRB ID [167](#srb-id)

9.3.1.8 DRB ID [168](#drb-id)

9.3.1.9 gNB-DU ID [168](#gnb-du-id)

9.3.1.10 Served Cell Information [168](#served-cell-information)

9.3.1.11 Transmission Action Indicator [171](#transmission-action-indicator)

9.3.1.12 NR CGI [171](#nr-cgi)

9.3.1.13 Time To wait [172](#time-to-wait)

9.3.1.14 PLMN Identity [172](#plmn-identity)

9.3.1.15 Transmission Bandwidth [172](#transmission-bandwidth)

9.3.1.16 Void [172](#void)

9.3.1.17 NR Frequency Info [172](#nr-frequency-info)

9.3.1.18 gNB-DU System Information [174](#gnb-du-system-information)

9.3.1.19 E-UTRAN QoS [174](#e-utran-qos)

9.3.1.20 Allocation and Retention Priority [175](#allocation-and-retention-priority)

9.3.1.21 GBR QoS Information [175](#gbr-qos-information)

9.3.1.22 Bit Rate [176](#bit-rate)

9.3.1.23 Transaction ID [176](#transaction-id)

9.3.1.24 DRX Cycle [176](#drx-cycle)

9.3.1.25 CU to DU RRC Information [177](#cu-to-du-rrc-information)

9.3.1.26 DU to CU RRC Information [178](#du-to-cu-rrc-information)

9.3.1.27 RLC Mode [181](#rlc-mode)

9.3.1.28 SUL Information [181](#sul-information)

9.3.1.29 5GS TAC [182](#gs-tac)

9.3.1.29a Configured EPS TAC [182](#a-configured-eps-tac)

9.3.1.30 RRC Reconfiguration Complete Indicator [182](#rrc-reconfiguration-complete-indicator)

9.3.1.31 UL Configuration [182](#ul-configuration)

9.3.1.32 C-RNTI [183](#c-rnti)

9.3.1.33 Cell UL Configured [183](#cell-ul-configured)

9.3.1.34 RAT-Frequency Priority Information [183](#rat-frequency-priority-information)

9.3.1.35 LCID [183](#lcid)

9.3.1.36 Duplication activation [183](#duplication-activation)

9.3.1.37 Slice Support List [184](#slice-support-list)

9.3.1.38 S-NSSAI [184](#s-nssai)

9.3.1.39 UE Identity Index value [184](#ue-identity-index-value)

9.3.1.40 Paging DRX [184](#paging-drx)

9.3.1.41 Paging Priority [184](#paging-priority)

9.3.1.42 gNB-CU System Information [185](#gnb-cu-system-information)

9.3.1.43 RAN UE Paging identity [185](#ran-ue-paging-identity)

9.3.1.44 CN UE Paging Identity [185](#cn-ue-paging-identity)

9.3.1.45 QoS Flow Level QoS Parameters [186](#qos-flow-level-qos-parameters)

9.3.1.46 GBR QoS Flow Information [187](#gbr-qos-flow-information)

9.3.1.47 Dynamic 5QI Descriptor [187](#dynamic-5qi-descriptor)

9.3.1.48 NG-RAN Allocation and Retention Priority [188](#ng-ran-allocation-and-retention-priority)

9.3.1.49 Non Dynamic 5QI Descriptor [189](#non-dynamic-5qi-descriptor)

9.3.1.50 Maximum Packet Loss Rate [190](#maximum-packet-loss-rate)

9.3.1.51 Packet Delay Budget [190](#packet-delay-budget)

9.3.1.52 Packet Error Rate [190](#packet-error-rate)

9.3.1.53 Averaging Window [191](#averaging-window)

9.3.1.54 Maximum Data Burst Volume [191](#maximum-data-burst-volume)

9.3.1.55 Masked IMEISV [191](#masked-imeisv)

9.3.1.56 Notification Control [191](#notification-control)

9.3.1.57 RAN Area Code [191](#ran-area-code)

9.3.1.58 PWS System Information [191](#pws-system-information)

9.3.1.59 Repetition Period [192](#repetition-period)

9.3.1.60 Number of Broadcasts Requested [192](#number-of-broadcasts-requested)

9.3.1.61 Void [192](#void-1)

9.3.1.62 SIType List [192](#sitype-list)

9.3.1.63 QoS Flow Identifier [193](#qos-flow-identifier)

9.3.1.64 Served E-UTRA Cell Information [193](#served-e-utra-cell-information)

9.3.1.65 Available PLMN List [193](#available-plmn-list)

9.3.1.66 RLC Failure Indication [194](#rlc-failure-indication)

9.3.1.67 Uplink TxDirectCurrentList Information [194](#uplink-txdirectcurrentlist-information)

9.3.1.68 Service Status [194](#service-status)

9.3.1.69 RLC Status [194](#rlc-status)

9.3.1.70 RRC Version [194](#rrc-version)

9.3.1.71 RRC Delivery Status [195](#rrc-delivery-status)

9.3.1.72 QoS Flow Mapping Indication [195](#qos-flow-mapping-indication)

9.3.1.73 Resource Coordination Transfer Information [195](#resource-coordination-transfer-information)

9.3.1.74 E-UTRA PRACH Configuration [195](#e-utra-prach-configuration)

9.3.1.75 Resource Coordination E-UTRA Cell Information [196](#resource-coordination-e-utra-cell-information)

9.3.1.76 Extended Available PLMN List [197](#extended-available-plmn-list)

9.3.1.77 Associated SCell List [197](#associated-scell-list)

9.3.1.78 Cell Direction [197](#cell-direction)

9.3.1.79 Paging Origin [198](#paging-origin)

9.3.1.80 E-UTRA Transmission Bandwidth [198](#e-utra-transmission-bandwidth)

9.3.1.81 Message Identifier [198](#message-identifier)

9.3.1.82 Serial Number [198](#serial-number)

9.3.1.83 UAC Assistance Information [198](#uac-assistance-information)

9.3.1.84 UAC Action [199](#uac-action)

9.3.1.85 UAC reduction Indication [199](#uac-reduction-indication)

9.3.1.86 Additional SIB Message List [200](#additional-sib-message-list)

9.3.1.87 Cell Type [200](#cell-type)

9.3.1.87a Configured TAC Indication [200](#a-configured-tac-indication)

9.3.1.88 Trace Activation [200](#trace-activation)

9.3.1.89 Intended TDD DL-UL Configuration [201](#intended-tdd-dl-ul-configuration)

9.3.1.90 Additional RRM Policy Index [202](#additional-rrm-policy-index)

9.3.1.91 DU-CU RIM Information [202](#du-cu-rim-information)

9.3.1.92 CU-DU RIM Information [203](#cu-du-rim-information)

9.3.1.93 gNB Set ID [203](#gnb-set-id)

9.3.1.94 Lower Layer Presence Status Change [203](#lower-layer-presence-status-change)

9.3.1.95 Traffic Mapping Information [203](#traffic-mapping-information)

9.3.1.96 IP-to-layer-2 traffic mapping Information List [204](#ip-to-layer-2-traffic-mapping-information-list)

9.3.1.97 IP Header Information [204](#ip-header-information)

9.3.1.98 BAP layer BH RLC channel mapping Information List [205](#bap-layer-bh-rlc-channel-mapping-information-list)

9.3.1.99 Mapping Information to Remove [205](#mapping-information-to-remove)

9.3.1.100 Mapping Information Index [205](#mapping-information-index)

9.3.1.101 IAB TNL Addresses Requested [206](#iab-tnl-addresses-requested)

9.3.1.102 IAB TNL Address [206](#iab-tnl-address)

9.3.1.103 Uplink BH Non-UP Traffic Mapping [206](#uplink-bh-non-up-traffic-mapping)

9.3.1.104 Non-UP Traffic Type [206](#non-up-traffic-type)

9.3.1.105 IAB Info IAB-donor-CU [207](#iab-info-iab-donor-cu)

9.3.1.106 IAB Info IAB-DU [207](#iab-info-iab-du)

9.3.1.107 gNB-DU Cell Resource Configuration [207](#gnb-du-cell-resource-configuration)

9.3.1.108 Multiplexing Info [208](#multiplexing-info)

9.3.1.109 IAB STC Info [209](#iab-stc-info)

9.3.1.110 BAP Routing ID [209](#bap-routing-id)

9.3.1.111 BAP Address [210](#bap-address)

9.3.1.112 BAP Path ID [210](#bap-path-id)

9.3.1.113 BH RLC Channel ID [210](#bh-rlc-channel-id)

9.3.1.114 BH Information [210](#_Toc192843326)

9.3.1.115 Control Plane Traffic Type [211](#control-plane-traffic-type)

9.3.1.116 NR V2X Services Authorized [211](#nr-v2x-services-authorized)

9.3.1.117 LTE V2X Services Authorized [211](#lte-v2x-services-authorized)

9.3.1.118 LTE UE Sidelink Aggregate Maximum Bit Rate [211](#lte-ue-sidelink-aggregate-maximum-bit-rate)

9.3.1.119 NR UE Sidelink Aggregate Maximum Bit Rate [212](#nr-ue-sidelink-aggregate-maximum-bit-rate)

9.3.1.120 SL DRB ID [212](#sl-drb-id)

9.3.1.121 PC5 QoS Flow Identifier [212](#pc5-qos-flow-identifier)

9.3.1.122 PC5 QoS Parameters [212](#pc5-qos-parameters)

9.3.1.123 Alternative QoS Parameters Set Index [213](#alternative-qos-parameters-set-index)

9.3.1.124 Alternative QoS Parameters Set Notify Index [213](#alternative-qos-parameters-set-notify-index)

9.3.1.125 Alternative QoS Parameters Set List [213](#alternative-qos-parameters-set-list)

9.3.1.126 Non Dynamic PQI Descriptor [213](#non-dynamic-pqi-descriptor)

9.3.1.127 Dynamic PQI Descriptor [214](#dynamic-pqi-descriptor)

9.3.1.128 TNL Capacity Indicator [214](#tnl-capacity-indicator)

9.3.1.129 Radio Resource Status [215](#radio-resource-status)

9.3.1.130 Composite Available Capacity Group [215](#composite-available-capacity-group)

9.3.1.131 Composite Available Capacity [215](#composite-available-capacity)

9.3.1.132 Cell Capacity Class Value [215](#cell-capacity-class-value)

9.3.1.133 Capacity Value [216](#capacity-value)

9.3.1.134 Slice Available Capacity [216](#slice-available-capacity)

9.3.1.135 Number of Active UEs [217](#number-of-active-ues)

9.3.1.136 Hardware Load Indicator [217](#hardware-load-indicator)

9.3.1.137 NR Carrier List [217](#nr-carrier-list)

9.3.1.138 SSB Positions In Burst [218](#ssb-positions-in-burst)

9.3.1.139 NR PRACH Configuration [218](#nr-prach-configuration)

9.3.1.140 NR PRACH Configuration List [218](#nr-prach-configuration-list)

9.3.1.141 TSC Traffic Characteristics [220](#tsc-traffic-characteristics)

9.3.1.142 TSC Assistance Information [221](#tsc-assistance-information)

9.3.1.143 Periodicity [221](#periodicity)

9.3.1.144 Burst Arrival Time [221](#burst-arrival-time)

9.3.1.145 Extended Packet Delay Budget [221](#extended-packet-delay-budget)

9.3.1.146 RLC Duplication Information [221](#rlc-duplication-information)

9.3.1.147 Reporting Request Type [222](#reporting-request-type)

9.3.1.148 Time Reference Information [222](#time-reference-information)

9.3.1.149 Reference Time [222](#reference-time)

9.3.1.150 MDT Configuration [223](#mdt-configuration)

9.3.1.151 MDT PLMN List [223](#mdt-plmn-list)

9.3.1.152 M5 Configuration [223](#m5-configuration)

9.3.1.153 M6 Configuration [224](#m6-configuration)

9.3.1.154 M7 Configuration [224](#_Toc192843366)

9.3.1.155 NID [224](#nid)

9.3.1.156 NPN Support Information [224](#npn-support-information)

9.3.1.157 NPN Broadcast Information [225](#npn-broadcast-information)

9.3.1.158 Broadcast SNPN ID List [225](#broadcast-snpn-id-list)

9.3.1.159 Broadcast NID List [225](#broadcast-nid-list)

9.3.1.160 Broadcast CAG-Identifier List [225](#broadcast-cag-identifier-list)

9.3.1.161 CAG ID [226](#cag-id)

9.3.1.162 Broadcast PNI-NPN ID Information [226](#broadcast-pni-npn-id-information)

9.3.1.163 Available SNPN ID List [226](#available-snpn-id-list)

9.3.1.164 Void [226](#void-2)

9.3.1.165 Extended Slice Support List [226](#extended-slice-support-list)

9.3.1.166 Positioning Measurement Result [227](#positioning-measurement-result)

9.3.1.167 UL Angle of Arrival [227](#ul-angle-of-arrival)

9.3.1.168 UL RTOA Measurement [227](#ul-rtoa-measurement)

9.3.1.169 Additional Path List [228](#additional-path-list)

9.3.1.170 gNB Rx-Tx Time Difference [228](#gnb-rx-tx-time-difference)

9.3.1.171 Time Stamp [229](#time-stamp)

9.3.1.172 TRP Measurement Quality [229](#trp-measurement-quality)

9.3.1.173 Measurement Beam Information [229](#measurement-beam-information)

9.3.1.174 NG-RAN Access Point Position [229](#ng-ran-access-point-position)

9.3.1.175 Requested SRS Transmission Characteristics [230](#requested-srs-transmission-characteristics)

9.3.1.176 TRP Information [231](#trp-information)

9.3.1.177 PRS Configuration [232](#prs-configuration)

9.3.1.178 DL-PRS Muting Pattern [233](#dl-prs-muting-pattern)

9.3.1.179 Spatial Direction Information [234](#spatial-direction-information)

9.3.1.180 SRS Resource Set ID [234](#srs-resource-set-id)

9.3.1.181 Spatial Relation Information [234](#spatial-relation-information)

9.3.1.182 SRS Resource Trigger [234](#srs-resource-trigger)

9.3.1.183 Relative Time 1900 [235](#relative-time-1900)

9.3.1.184 Geographical Coordinates [235](#geographical-coordinates)

9.3.1.185 DL-PRS Resource Coordinates [236](#dl-prs-resource-coordinates)

9.3.1.186 Relative Geodetic Location [236](#relative-geodetic-location)

9.3.1.187 Relative Cartesian Location [237](#relative-cartesian-location)

9.3.1.188 Reference Point [237](#reference-point)

9.3.1.189 Location Uncertainty [237](#location-uncertainty)

9.3.1.190 NG-RAN High Accuracy Access Point Position [238](#ng-ran-high-accuracy-access-point-position)

9.3.1.191 Positioning Broadcast Cells [238](#positioning-broadcast-cells)

9.3.1.192 SRS Configuration [238](#srs-configuration)

9.3.1.193 SRS Resource [239](#srs-resource)

9.3.1.194 Positioning SRS Resource [240](#positioning-srs-resource)

9.3.1.195 SRS Resource Set [242](#srs-resource-set)

9.3.1.196 Positioning SRS Resource Set [242](#positioning-srs-resource-set)

9.3.1.197 TRP ID [243](#trp-id)

9.3.1.198 NR-PRS Beam Information [243](#nr-prs-beam-information)

9.3.1.199 E-CID Measurement Result [244](#e-cid-measurement-result)

9.3.1.200 Cell Portion ID [244](#cell-portion-id)

9.3.1.201 Pathloss Reference Information [244](#pathloss-reference-information)

9.3.1.202 SSB Information [245](#ssb-information)

9.3.1.203 SSB Time/Frequency Configuration [245](#ssb-timefrequency-configuration)

9.3.1.204 Search Window Information [245](#search-window-information)

9.3.1.205 Extended gNB-DU Name [246](#extended-gnb-du-name)

9.3.1.206 Extended gNB-CU Name [246](#extended-gnb-cu-name)

9.3.1.207 F1-C Transfer Path [246](#f1-c-transfer-path)

9.3.1.208 SFN Offset [246](#sfn-offset)

9.3.1.209 Transmission Stop Indicator [247](#transmission-stop-indicator)

9.3.1.210 Spatial Relation Information per SRS Resource [247](#spatial-relation-information-per-srs-resource)

9.3.1.278 PosSIType List [247](#possitype-list)

9.3.1.283 Uplink TxDirectCurrentTwoCarrierList Information [248](#uplink-txdirectcurrenttwocarrierlist-information)

9.3.2 Transport Network Layer Related IEs [248](#transport-network-layer-related-ies)

9.3.2.1 UP Transport Layer Information [248](#up-transport-layer-information)

9.3.2.2 GTP-TEID [248](#gtp-teid)

9.3.2.3 Transport Layer Address [249](#transport-layer-address)

9.3.2.4 CP Transport Layer Information [249](#cp-transport-layer-information)

9.3.2.5 Transport Layer Address Info [249](#transport-layer-address-info)

9.3.2.6 URI [250](#uri)

9.4 Message and Information Element Abstract Syntax (with ASN.1) [250](#message-and-information-element-abstract-syntax-with-asn.1)

9.4.1 General [250](#general-61)

9.4.2 Usage of private message mechanism for non-standard use [251](#usage-of-private-message-mechanism-for-non-standard-use)

9.4.3 Elementary Procedure Definitions [252](#elementary-procedure-definitions)

9.4.4 PDU Definitions [265](#pdu-definitions)

9.4.5 Information Element Definitions [335](#information-element-definitions-1)

9.4.6 Common Definitions [441](#common-definitions)

9.4.7 Constant Definitions [442](#constant-definitions)

9.4.8 Container Definitions [454](#container-definitions)

9.5 Message Transfer Syntax [458](#message-transfer-syntax)

9.6 Timers [458](#timers)

10 Handling of unknown, unforeseen and erroneous protocol data [458](#handling-of-unknown-unforeseen-and-erroneous-protocol-data)

Annex A (informative): Change History [459](#annex-a-informative-change-history)

#  Foreword

This Technical Specification has been produced by the 3rd Generation Partnership Project (3GPP).

The contents of the present document are subject to continuing work within the TSG and may change following formal TSG approval. Should the TSG modify the contents of the present document, it will be re-released by the TSG with an identifying change of release date and an increase in version number as follows:

Version x.y.z

where:

x the first digit:

1 presented to TSG for information;

2 presented to TSG for approval;

3 or greater indicates TSG approved document under change control.

y the second digit is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc.

z the third digit is incremented when editorial only changes have been incorporated in the document.
