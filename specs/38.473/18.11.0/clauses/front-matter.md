3GPP TS 38.473 V18.11.0 (2026-09)

Technical Specification

3rd Generation Partnership Project;

Technical Specification Group Radio Access Network;

NG-RAN;

F1 application protocol (F1AP)

(Release 18)

[figure] <img src="media/image2.png" style="width:1.77778in;height:1.03681in" />

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

© 2026, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC).

All rights reserved.

UMTS™ is a Trade Mark of ETSI registered for the benefit of its members

3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners  
LTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners

GSM® and the GSM logo are registered and owned by the GSM Association

#  Contents

Foreword [20](#foreword)

1 Scope [21](#scope)

2 References [21](#references)

3 Definitions and abbreviations [23](#definitions-and-abbreviations)

3.1 Definitions [23](#definitions)

3.2 Abbreviations [25](#abbreviations)

4 General [26](#general)

4.1 Procedure specification principles [26](#procedure-specification-principles)

4.2 Forwards and backwards compatibility [27](#forwards-and-backwards-compatibility)

4.3 Specification notations [27](#specification-notations)

5 F1AP services [27](#f1ap-services)

6 Services expected from signalling transport [27](#services-expected-from-signalling-transport)

7 Functions of F1AP [28](#functions-of-f1ap)

8 F1AP procedures [28](#f1ap-procedures)

8.1 List of F1AP Elementary procedures [28](#list-of-f1ap-elementary-procedures)

8.2 Interface Management procedures [31](#interface-management-procedures)

8.2.1 Reset [31](#reset)

8.2.1.1 General [31](#general-1)

8.2.1.2 Successful Operation [31](#successful-operation)

8.2.1.2.1 Reset Procedure Initiated from the gNB-CU [31](#reset-procedure-initiated-from-the-gnb-cu)

8.2.1.2.2 Reset Procedure Initiated from the gNB-DU [32](#reset-procedure-initiated-from-the-gnb-du)

8.2.1.3 Abnormal Conditions [33](#abnormal-conditions)

8.2.2 Error Indication [33](#error-indication)

8.2.2.1 General [33](#general-2)

8.2.2.2 Successful Operation [33](#successful-operation-1)

8.2.2.3 Abnormal Conditions [34](#abnormal-conditions-1)

8.2.3 F1 Setup [34](#f1-setup)

8.2.3.1 General [34](#general-3)

8.2.3.2 Successful Operation [35](#successful-operation-2)

8.2.3.3 Unsuccessful Operation [37](#unsuccessful-operation)

8.2.3.4 Abnormal Conditions [37](#abnormal-conditions-2)

8.2.4 gNB-DU Configuration Update [37](#gnb-du-configuration-update)

8.2.4.1 General [37](#general-4)

8.2.4.2 Successful Operation [38](#successful-operation-3)

8.2.4.3 Unsuccessful Operation [41](#unsuccessful-operation-1)

8.2.4.4 Abnormal Conditions [41](#abnormal-conditions-3)

8.2.5 gNB-CU Configuration Update [41](#gnb-cu-configuration-update)

8.2.5.1 General [41](#general-5)

8.2.5.2 Successful Operation [41](#successful-operation-4)

8.2.5.3 Unsuccessful Operation [44](#unsuccessful-operation-2)

8.2.5.4 Abnormal Conditions [44](#abnormal-conditions-4)

8.2.6 gNB-DU Resource Coordination [44](#gnb-du-resource-coordination)

8.2.6.1 General [44](#general-6)

8.2.6.2 Successful Operation [45](#successful-operation-5)

8.2.7 gNB-DU Status Indication [45](#gnb-du-status-indication)

8.2.7.1 General [45](#general-7)

8.2.7.2 Successful Operation [45](#successful-operation-6)

8.2.7.3 Abnormal Conditions [46](#abnormal-conditions-5)

8.2.8 F1 Removal [46](#f1-removal)

8.2.8.1 General [46](#general-8)

8.2.8.2 Successful Operation [46](#successful-operation-7)

8.2.8.3 Unsuccessful Operation [47](#unsuccessful-operation-3)

8.2.8.4 Abnormal Conditions [47](#abnormal-conditions-6)

8.2.9 Network Access Rate Reduction [47](#network-access-rate-reduction)

8.2.9.1 General [47](#general-9)

8.2.9.2 Successful operation [48](#successful-operation-8)

8.2.9.3 Abnormal Conditions [48](#abnormal-conditions-7)

8.2.10 Resource Status Reporting Initiation [48](#resource-status-reporting-initiation)

8.2.10.1 General [48](#general-10)

8.2.10.2 Successful Operation [48](#successful-operation-9)

8.2.10.3 Unsuccessful Operation [50](#unsuccessful-operation-4)

8.2.10.4 Abnormal Conditions [50](#abnormal-conditions-8)

8.2.11 Resource Status Reporting [50](#resource-status-reporting)

8.2.11.1 General [50](#general-11)

8.2.11.2 Successful Operation [50](#successful-operation-10)

8.2.11.3 Unsuccessful Operation [51](#unsuccessful-operation-5)

8.2.11.4 Abnormal Conditions [51](#abnormal-conditions-9)

8.2.12 DU-CU TA Information Transfer [51](#du-cu-ta-information-transfer)

8.2.12.1 General [51](#general-12)

8.2.12.2 Successful Operation [51](#successful-operation-11)

8.2.12.3 Unsuccessful Operation [51](#unsuccessful-operation-6)

8.2.12.4 Abnormal Conditions [51](#abnormal-conditions-10)

8.2.13 CU-DU TA Information Transfer [51](#cu-du-ta-information-transfer)

8.2.13.1 General [51](#general-13)

8.2.13.2 Successful Operation [52](#successful-operation-12)

8.2.13.3 Unsuccessful Operation [52](#unsuccessful-operation-7)

8.2.13.4 Abnormal Conditions [52](#abnormal-conditions-11)

8.2.14 RACH Indication [52](#rach-indication)

8.2.14.1 General [52](#general-14)

8.2.14.2 Successful Operation [52](#successful-operation-13)

8.2.14.3 Abnormal Conditions [53](#abnormal-conditions-12)

8.3 UE Context Management procedures [53](#ue-context-management-procedures)

8.3.1 UE Context Setup [53](#ue-context-setup)

8.3.1.1 General [53](#general-15)

8.3.1.2 Successful Operation [53](#successful-operation-14)

8.3.1.3 Unsuccessful Operation [62](#unsuccessful-operation-8)

8.3.1.4 Abnormal Conditions [63](#abnormal-conditions-13)

8.3.2 UE Context Release Request (gNB-DU initiated) [63](#ue-context-release-request-gnb-du-initiated)

8.3.2.1 General [63](#general-16)

8.3.2.2 Successful Operation [63](#successful-operation-15)

8.3.2.3 Abnormal Conditions [64](#abnormal-conditions-14)

8.3.3 UE Context Release (gNB-CU initiated) [64](#ue-context-release-gnb-cu-initiated)

8.3.3.1 General [64](#general-17)

8.3.3.2 Successful Operation [64](#successful-operation-16)

8.3.3.3 Void [65](#void)

8.3.3.4 Abnormal Conditions [65](#abnormal-conditions-15)

8.3.4 UE Context Modification (gNB-CU initiated) [65](#ue-context-modification-gnb-cu-initiated)

8.3.4.1 General [65](#general-18)

8.3.4.2 Successful Operation [66](#successful-operation-17)

8.3.4.3 Unsuccessful Operation [79](#unsuccessful-operation-9)

8.3.4.4 Abnormal Conditions [80](#abnormal-conditions-16)

8.3.5 UE Context Modification Required (gNB-DU initiated) [80](#ue-context-modification-required-gnb-du-initiated)

8.3.5.1 General [80](#general-19)

8.3.5.2 Successful Operation [81](#successful-operation-18)

8.3.5.2A Unsuccessful Operation [82](#a-unsuccessful-operation)

8.3.5.3 Abnormal Conditions [83](#abnormal-conditions-17)

8.3.6 UE Inactivity Notification [83](#ue-inactivity-notification)

8.3.6.1 General [83](#general-20)

8.3.6.2 Successful Operation [83](#successful-operation-19)

8.3.6.3 Abnormal Conditions [83](#abnormal-conditions-18)

8.3.7 Notify [83](#notify)

8.3.7.1 General [83](#general-21)

8.3.7.2 Successful Operation [84](#successful-operation-20)

8.3.7.3 Abnormal Conditions [84](#abnormal-conditions-19)

8.3.8 Access Success [84](#access-success)

8.3.8.1 General [84](#general-22)

8.3.8.2 Successful Operation [84](#successful-operation-21)

8.3.8.3 Abnormal Conditions [85](#abnormal-conditions-20)

8.3.9 DU-CU Cell Switch Notification [85](#du-cu-cell-switch-notification)

8.3.9.1 General [85](#general-23)

8.3.9.2 Successful Operation [85](#successful-operation-22)

8.3.9.3 Unsuccessful Operation [85](#unsuccessful-operation-10)

8.3.9.4 Abnormal Conditions [85](#abnormal-conditions-21)

8.3.10 CU-DU Cell Switch Notification [86](#cu-du-cell-switch-notification)

8.3.10.1 General [86](#general-24)

8.3.10.2 Successful Operation [86](#successful-operation-23)

8.3.10.3 Unsuccessful Operation [86](#unsuccessful-operation-11)

8.3.10.4 Abnormal Conditions [86](#abnormal-conditions-22)

8.3.11 CU-DU Mobility Initiation [86](#cu-du-mobility-initiation)

8.3.11.1 General [86](#general-25)

8.3.11.2 Successful Operation [87](#successful-operation-24)

8.3.11.3 Unsuccessful Operation [87](#unsuccessful-operation-12)

8.3.11.4 Abnormal Conditions [87](#abnormal-conditions-23)

8.4 RRC Message Transfer procedures [87](#rrc-message-transfer-procedures)

8.4.1 Initial UL RRC Message Transfer [87](#initial-ul-rrc-message-transfer)

8.4.1.1 General [87](#general-26)

8.4.1.2 Successful operation [87](#successful-operation-25)

8.4.1.3 Abnormal Conditions [88](#abnormal-conditions-24)

8.4.2 DL RRC Message Transfer [88](#dl-rrc-message-transfer)

8.4.2.1 General [88](#general-27)

8.4.2.2 Successful operation [88](#successful-operation-26)

8.4.2.3 Abnormal Conditions [89](#abnormal-conditions-25)

8.4.3 UL RRC Message Transfer [89](#ul-rrc-message-transfer)

8.4.3.1 General [89](#general-28)

8.4.3.2 Successful operation [90](#successful-operation-27)

8.4.3.3 Abnormal Conditions [90](#abnormal-conditions-26)

8.4.4 RRC Delivery Report [90](#rrc-delivery-report)

8.4.4.1 General [90](#general-29)

8.4.4.2 Successful operation [90](#successful-operation-28)

8.4.4.3 Abnormal Conditions [91](#abnormal-conditions-27)

8.5 Warning Message Transmission Procedures [91](#warning-message-transmission-procedures)

8.5.1 Write-Replace Warning [91](#write-replace-warning)

8.5.1.1 General [91](#general-30)

8.5.1.2 Successful Operation [91](#successful-operation-29)

8.5.1.3 Unsuccessful Operation [92](#unsuccessful-operation-13)

8.5.1.4 Abnormal Conditions [92](#abnormal-conditions-28)

8.5.2 PWS Cancel [92](#pws-cancel)

8.5.2.1 General [92](#general-31)

8.5.2.2 Successful Operation [92](#successful-operation-30)

8.5.2.3 Unsuccessful Operation [93](#unsuccessful-operation-14)

8.5.2.4 Abnormal Conditions [93](#abnormal-conditions-29)

8.5.3 PWS Restart Indication [93](#pws-restart-indication)

8.5.3.1 General [93](#general-32)

8.5.3.2 Successful Operation [93](#successful-operation-31)

8.5.3.3 Abnormal Conditions [93](#abnormal-conditions-30)

8.5.4 PWS Failure Indication [93](#pws-failure-indication)

8.5.4.1 General [93](#general-33)

8.5.4.2 Successful Operation [94](#successful-operation-32)

8.5.4.3 Abnormal Conditions [94](#abnormal-conditions-31)

8.6 System Information Procedures [94](#system-information-procedures)

8.6.1 System Information Delivery [94](#system-information-delivery)

8.6.1.1 General [94](#general-34)

8.6.1.2 Successful Operation [94](#successful-operation-33)

8.6.1.3 Abnormal Conditions [95](#abnormal-conditions-32)

8.7 Paging procedures [95](#paging-procedures)

8.7.1 Paging [95](#paging)

8.7.1.1 General [95](#general-35)

8.7.1.2 Successful Operation [95](#successful-operation-34)

8.7.1.3 Abnormal Conditions [96](#abnormal-conditions-33)

8.8 Trace Procedures [96](#trace-procedures)

8.8.1 Trace Start [96](#trace-start)

8.8.1.1 General [96](#general-36)

8.8.1.2 Successful Operation [96](#successful-operation-35)

8.8.1.3 Abnormal Conditions [97](#abnormal-conditions-34)

8.8.2 Deactivate Trace [97](#deactivate-trace)

8.8.2.1 General [97](#general-37)

8.8.2.2 Successful Operation [97](#successful-operation-36)

8.8.2.3 Abnormal Conditions [97](#abnormal-conditions-35)

8.8.3 Cell Traffic Trace [97](#cell-traffic-trace)

8.8.3.1 General [97](#general-38)

8.8.3.2 Successful Operation [98](#successful-operation-37)

8.8.3.3 Abnormal Conditions [98](#abnormal-conditions-36)

8.9 Radio Information Transfer procedures [98](#radio-information-transfer-procedures)

8.9.1 DU-CU Radio Information Transfer [98](#du-cu-radio-information-transfer)

8.9.1.1 General [98](#general-39)

8.9.1.2 Successful operation [98](#successful-operation-38)

8.9.1.3 Abnormal Conditions [98](#abnormal-conditions-37)

8.9.2 CU-DU Radio Information Transfer [99](#cu-du-radio-information-transfer)

8.9.2.1 General [99](#general-40)

8.9.2.2 Successful operation [99](#successful-operation-39)

8.9.2.3 Abnormal Conditions [99](#abnormal-conditions-38)

8.10 IAB Procedures [99](#iab-procedures)

8.10.0 General [99](#general-41)

8.10.1 BAP Mapping Configuration [99](#bap-mapping-configuration)

8.10.1.1 General [99](#general-42)

8.10.1.2 Successful Operation [99](#successful-operation-40)

8.10.1.A Unsuccessful Operation [101](#a-unsuccessful-operation-1)

8.10.1.3 Abnormal Conditions [101](#abnormal-conditions-39)

8.10.2 gNB-DU Resource Configuration [101](#gnb-du-resource-configuration)

8.10.2.1 General [101](#general-43)

8.10.2.2 Successful Operation [101](#successful-operation-41)

8.10.2.B Unsuccessful Operation [102](#b-unsuccessful-operation)

8.10.2.3 Abnormal Conditions [102](#abnormal-conditions-40)

8.10.3 IAB TNL Address Allocation [102](#iab-tnl-address-allocation)

8.10.3.1 General [102](#general-44)

8.10.3.2 Successful Operation [103](#successful-operation-42)

8.10.3.C Unsuccessful Operation [103](#c-unsuccessful-operation)

8.10.3.3 Abnormal Conditions [104](#abnormal-conditions-41)

8.10.4 IAB UP Configuration Update [104](#iab-up-configuration-update)

8.10.4.1 General [104](#general-45)

8.10.4.2 Successful Operation [104](#successful-operation-43)

8.10.4.3 Unsuccessful Operation [105](#unsuccessful-operation-15)

8.10.4.4 Abnormal Conditions [105](#abnormal-conditions-42)

8.10.5 Mobile IAB F1 Setup Triggering [105](#mobile-iab-f1-setup-triggering)

8.10.5.1 General [105](#general-46)

8.10.5.2 Successful Operation [105](#successful-operation-44)

8.10.5.3 Abnormal Conditions [106](#abnormal-conditions-43)

8.10.6 Mobile IAB F1 Setup Outcome Notification [106](#mobile-iab-f1-setup-outcome-notification)

8.10.6.1 General [106](#general-47)

8.10.6.2 Successful Operation [106](#successful-operation-45)

8.10.6.3 Abnormal Conditions [107](#abnormal-conditions-44)

8.11 Self Optimisation Support procedures [107](#self-optimisation-support-procedures)

8.11.1 Access and Mobility Indication [107](#access-and-mobility-indication)

8.11.1.1 General [107](#general-48)

8.11.1.2 Successful Operation [107](#successful-operation-46)

8.11.1.3 Abnormal Conditions [107](#abnormal-conditions-45)

8.11.2 DU-CU Access and Mobility Indication [107](#du-cu-access-and-mobility-indication)

8.11.2.1 General [107](#general-49)

8.11.2.2 Successful Operation [108](#successful-operation-47)

8.11.2.3 Abnormal Conditions [108](#abnormal-conditions-46)

8.12 Reference Time Information Reporting procedures [108](#reference-time-information-reporting-procedures)

8.12.1 Reference Time Information Reporting Control [108](#reference-time-information-reporting-control)

8.12.1.1 General [108](#general-50)

8.12.1.2 Successful Operation [108](#successful-operation-48)

8.12.1.3 Abnormal Conditions [109](#abnormal-conditions-47)

8.12.2 Reference Time Information Report [109](#reference-time-information-report)

8.12.2.1 General [109](#general-51)

8.12.2.2 Successful Operation [109](#successful-operation-49)

8.12.2.3 Abnormal Conditions [109](#abnormal-conditions-48)

8.13 Positioning Procedures [109](#positioning-procedures)

8.13.1 Positioning Assistance Information Control [109](#positioning-assistance-information-control)

8.13.1.1 General [109](#general-52)

8.13.1.2 Successful Operation [109](#successful-operation-50)

8.13.1.3 Abnormal Conditions [110](#abnormal-conditions-49)

8.13.2 Positioning Assistance Information Feedback [110](#positioning-assistance-information-feedback)

8.13.2.1 General [110](#general-53)

8.13.2.2 Successful Operation [110](#successful-operation-51)

8.13.2.3 Abnormal Conditions [111](#abnormal-conditions-50)

8.13.3 Positioning Measurement [111](#positioning-measurement)

8.13.3.1 General [111](#general-54)

8.13.3.2 Successful Operation [111](#successful-operation-52)

8.13.3.3 Unsuccessful Operation [112](#unsuccessful-operation-16)

8.13.3.4 Abnormal Conditions [112](#abnormal-conditions-51)

8.13.4 Positioning Measurement Report [112](#positioning-measurement-report)

8.13.4.1 General [112](#general-55)

8.13.4.2 Successful Operation [113](#successful-operation-53)

8.13.4.3 Unsuccessful Operation [113](#unsuccessful-operation-17)

8.13.4.4 Abnormal Conditions [113](#abnormal-conditions-52)

8.13.5 Positioning Measurement Abort [113](#positioning-measurement-abort)

8.13.5.1 General [113](#general-56)

8.13.5.2 Successful Operation [113](#successful-operation-54)

8.13.5.3 Unsuccessful Operation [113](#unsuccessful-operation-18)

8.13.5.4 Abnormal Conditions [113](#abnormal-conditions-53)

8.13.6 Positioning Measurement Failure Indication [114](#positioning-measurement-failure-indication)

8.13.6.1 General [114](#general-57)

8.13.6.2 Successful Operation [114](#successful-operation-55)

8.13.6.3 Unsuccessful Operation [114](#unsuccessful-operation-19)

8.13.6.4 Abnormal Conditions [114](#abnormal-conditions-54)

8.13.7 Positioning Measurement Update [114](#positioning-measurement-update)

8.13.7.1 General [114](#general-58)

8.13.7.2 Successful Operation [114](#successful-operation-56)

8.13.7.3 Unsuccessful Operation [115](#unsuccessful-operation-20)

8.13.7.4 Abnormal Conditions [115](#abnormal-conditions-55)

8.13.8 TRP Information Exchange [115](#trp-information-exchange)

8.13.8.1 General [115](#general-59)

8.13.8.2 Successful Operation [115](#successful-operation-57)

8.13.8.3 Unsuccessful Operation [116](#unsuccessful-operation-21)

8.13.9 Positioning Information Exchange [116](#positioning-information-exchange)

8.13.9.1 General [116](#general-60)

8.13.9.2 Successful Operation [117](#successful-operation-58)

8.13.9.3 Unsuccessful Operation [118](#unsuccessful-operation-22)

8.13.10 Positioning Activation [118](#positioning-activation)

8.13.10.1 General [118](#general-61)

8.13.10.2 Successful Operation [118](#successful-operation-59)

8.13.10.3 Unsuccessful Operation [119](#unsuccessful-operation-23)

8.13.10.4 Abnormal Conditions [119](#abnormal-conditions-56)

8.13.11 Positioning Deactivation [119](#positioning-deactivation)

8.13.11.1 General [119](#general-62)

8.13.11.2 Successful Operation [119](#successful-operation-60)

8.13.11.3 Unsuccessful Operation [119](#unsuccessful-operation-24)

8.13.11.4 Abnormal Conditions [120](#abnormal-conditions-57)

8.13.12 E-CID Measurement Initiation [120](#e-cid-measurement-initiation)

8.13.12.1 General [120](#general-63)

8.13.12.2 Successful Operation [120](#successful-operation-61)

8.13.12.3 Unsuccessful Operation [120](#unsuccessful-operation-25)

8.13.13 E-CID Measurement Failure Indication [121](#e-cid-measurement-failure-indication)

8.13.13.1 General [121](#general-64)

8.13.13.2 Successful Operation [121](#successful-operation-62)

8.13.13.3 Unsuccessful Operation [121](#unsuccessful-operation-26)

8.13.14 E-CID Measurement Report [121](#e-cid-measurement-report)

8.13.14.1 General [121](#general-65)

8.13.14.2 Successful Operation [121](#successful-operation-63)

8.13.14.3 Unsuccessful Operation [122](#unsuccessful-operation-27)

8.13.15 E-CID Measurement Termination [122](#e-cid-measurement-termination)

8.13.15.1 General [122](#general-66)

8.13.15.2 Successful Operation [122](#successful-operation-64)

8.13.15.3 Unsuccessful Operation [122](#unsuccessful-operation-28)

8.13.16 Positioning Information Update [122](#positioning-information-update)

8.13.16.1 General [122](#general-67)

8.13.16.2 Successful Operation [123](#successful-operation-65)

8.13.16.3 Unsuccessful Operation [123](#unsuccessful-operation-29)

8.13.16.4 Abnormal Conditions [123](#abnormal-conditions-58)

8.13.17 PRS Configuration Exchange [123](#prs-configuration-exchange)

8.13.17.1 General [123](#general-68)

8.13.17.2 Successful Operation [123](#successful-operation-66)

8.13.17.3 Unsuccessful Operation [124](#unsuccessful-operation-30)

8.13.17.4 Abnormal Conditions [124](#abnormal-conditions-59)

8.13.18 Measurement Preconfiguration [124](#measurement-preconfiguration)

8.13.18.1 General [124](#general-69)

8.13.18.2 Successful Operation [124](#successful-operation-67)

8.13.18.3 Unsuccessful Operation [125](#unsuccessful-operation-31)

8.13.19 Measurement Activation [125](#measurement-activation)

8.13.19.1 General [125](#general-70)

8.13.19.2 Successful Operation [125](#successful-operation-68)

8.13.19.3 Unsuccessful Operation [125](#unsuccessful-operation-32)

8.13.20 Positioning System Information Delivery [125](#positioning-system-information-delivery)

8.13.20.1 General [125](#general-71)

8.13.20.2 Successful Operation [126](#successful-operation-69)

8.13.20.3 Abnormal Conditions [126](#abnormal-conditions-60)

8.13.21 SRS Information Reservation Notification [126](#srs-information-reservation-notification)

8.13.21.1 General [126](#general-72)

8.13.21.2 Successful Operation [126](#successful-operation-70)

8.13.21.3 Unsuccessful Operation [127](#unsuccessful-operation-33)

8.13.21.4 Abnormal Conditions [127](#abnormal-conditions-61)

8.14 NR MBS Procedures [127](#nr-mbs-procedures)

8.14.1 Broadcast Context Setup [127](#broadcast-context-setup)

8.14.1.1 General [127](#general-73)

8.14.1.2 Successful Operation [127](#successful-operation-71)

8.14.1.3 Unsuccessful Operation [128](#unsuccessful-operation-34)

8.14.1.4 Abnormal Conditions [128](#abnormal-conditions-62)

8.14.2 Broadcast Context Release [128](#broadcast-context-release)

8.14.2.1 General [128](#general-74)

8.14.2.2 Successful Operation [129](#successful-operation-72)

8.14.2.3 Unsuccessful Operation [129](#unsuccessful-operation-35)

8.14.2.4 Abnormal Conditions [129](#abnormal-conditions-63)

8.14.3 Broadcast Context Release Request [129](#broadcast-context-release-request)

8.14.3.1 General [129](#general-75)

8.14.3.2 Successful Operation [129](#successful-operation-73)

8.14.3.3 Unsuccessful Operation [130](#unsuccessful-operation-36)

8.14.3.4 Abnormal Conditions [130](#abnormal-conditions-64)

8.14.4 Broadcast Context Modification [130](#broadcast-context-modification)

8.14.4.1 General [130](#general-76)

8.14.4.2 Successful Operation [130](#successful-operation-74)

8.14.4.3 Unsuccessful Operation [131](#unsuccessful-operation-37)

8.14.4.4 Abnormal Conditions [131](#abnormal-conditions-65)

8.14.5 Multicast Group Paging [132](#multicast-group-paging)

8.14.5.1 General [132](#general-77)

8.14.5.2 Successful Operation [132](#successful-operation-75)

8.14.5.3 Abnormal Conditions [132](#abnormal-conditions-66)

8.14.6 Multicast Context Setup [132](#multicast-context-setup)

8.14.6.1 General [132](#general-78)

8.14.6.2 Successful Operation [133](#successful-operation-76)

8.14.6.3 Unsuccessful Operation [134](#unsuccessful-operation-38)

8.14.6.4 Abnormal Conditions [134](#abnormal-conditions-67)

8.14.7 Multicast Context Release [134](#multicast-context-release)

8.14.7.1 General [134](#general-79)

8.14.7.2 Successful Operation [134](#successful-operation-77)

8.14.7.3 Unsuccessful Operation [134](#unsuccessful-operation-39)

8.14.7.4 Abnormal Conditions [135](#abnormal-conditions-68)

8.14.8 Multicast Context Release Request [135](#multicast-context-release-request)

8.14.8.1 General [135](#general-80)

8.14.8.2 Successful Operation [135](#successful-operation-78)

8.14.8.3 Unsuccessful Operation [135](#unsuccessful-operation-40)

8.14.8.4 Abnormal Conditions [135](#abnormal-conditions-69)

8.14.9 Multicast Context Modification [135](#multicast-context-modification)

8.14.9.1 General [135](#general-81)

8.14.9.2 Successful Operation [136](#successful-operation-79)

8.14.9.3 Unsuccessful Operation [137](#unsuccessful-operation-41)

8.14.9.4 Abnormal Conditions [137](#abnormal-conditions-70)

8.14.10 Multicast Distribution Setup [137](#multicast-distribution-setup)

8.14.10.1 General [137](#general-82)

8.14.10.2 Successful Operation [137](#successful-operation-80)

8.14.10.3 Unsuccessful Operation [138](#unsuccessful-operation-42)

8.14.10.4 Abnormal Conditions [138](#abnormal-conditions-71)

8.14.11 Multicast Distribution Release [138](#multicast-distribution-release)

8.14.11.1 General [138](#general-83)

8.14.11.2 Successful Operation [138](#successful-operation-81)

8.14.11.3 Unsuccessful Operation [139](#unsuccessful-operation-43)

8.14.11.4 Abnormal Conditions [139](#abnormal-conditions-72)

8.14.12 Multicast Context Notification [139](#multicast-context-notification)

8.14.12.1 General [139](#general-84)

8.14.12.2 Successful Operation [139](#successful-operation-82)

8.14.12.3 Unsuccessful Operation [139](#unsuccessful-operation-44)

8.14.12.4 Abnormal Conditions [140](#abnormal-conditions-73)

8.14.13 Multicast Common Configuration [140](#multicast-common-configuration)

8.14.13.1 General [140](#general-85)

8.14.13.2 Successful Operation [140](#successful-operation-83)

8.14.13.3 Unsuccessful Operation [140](#unsuccessful-operation-45)

8.14.13.4 Abnormal Conditions [140](#abnormal-conditions-74)

8.14.14 Broadcast Transport Resource Request [141](#broadcast-transport-resource-request)

8.14.14.1 General [141](#general-86)

8.14.14.2 Successful Operation [141](#successful-operation-84)

8.14.14.3 Unsuccessful Operation [141](#unsuccessful-operation-46)

8.14.14.4 Abnormal Conditions [141](#abnormal-conditions-75)

8.15 PDC Measurement Reporting procedures [141](#pdc-measurement-reporting-procedures)

8.15.1 PDC Measurement Initiation [141](#pdc-measurement-initiation)

8.15.1.1 General [141](#general-87)

8.15.1.2 Successful Operation [142](#successful-operation-85)

8.15.1.3 Unsuccessful Operation [142](#unsuccessful-operation-47)

8.15.2 PDC Measurement Report [142](#pdc-measurement-report)

8.15.2.1 General [142](#general-88)

8.15.2.2 Successful Operation [143](#successful-operation-86)

8.15.2.3 Unsuccessful Operation [143](#unsuccessful-operation-48)

8.15.3 PDC Measurement Termination [143](#pdc-measurement-termination)

8.15.3.1 General [143](#general-89)

8.15.3.2 Successful Operation [143](#successful-operation-87)

8.15.3.3 Unsuccessful Operation [143](#unsuccessful-operation-49)

8.15.3.4 Abnormal Conditions [143](#abnormal-conditions-76)

8.15.4 PDC Measurement Failure Indication [144](#pdc-measurement-failure-indication)

8.15.4.1 General [144](#general-90)

8.15.4.2 Successful Operation [144](#successful-operation-88)

8.15.4.3 Unsuccessful Operation [144](#unsuccessful-operation-50)

8.15.4.4 Abnormal Conditions [144](#abnormal-conditions-77)

8.16 QMC Procedures [144](#qmc-procedures)

8.16.1 QoE Information Transfer [144](#qoe-information-transfer)

8.16.1.1 General [144](#general-91)

8.16.1.2 Successful operation [144](#successful-operation-89)

8.16.1.3 Abnormal Conditions [145](#abnormal-conditions-78)

8.16.2 QoE Information Transfer Control [145](#qoe-information-transfer-control)

8.16.2.1 General [145](#general-92)

8.16.2.2 Successful operation [145](#successful-operation-90)

8.16.2.3 Abnormal Conditions [145](#abnormal-conditions-79)

8.17 Timing Synchronisation Status Reporting Procedures [145](#timing-synchronisation-status-reporting-procedures)

8.17.1 Timing Synchronisation Status [145](#timing-synchronisation-status)

8.17.1.1 General [145](#general-93)

8.17.1.2 Successful Operation [146](#successful-operation-91)

8.17.1.3 Unsuccessful Operation [146](#unsuccessful-operation-51)

8.17.1.4 Abnormal Conditions [146](#abnormal-conditions-80)

8.17.2 Timing Synchronisation Status Report [146](#timing-synchronisation-status-report)

8.17.2.1 General [146](#general-94)

8.17.2.2 Successful Operation [147](#successful-operation-92)

8.17.2.3 Abnormal Conditions [147](#abnormal-conditions-81)

9 Elements for F1AP Communication [147](#elements-for-f1ap-communication)

9.1 General [147](#general-95)

9.2 Message Functional Definition and Content [147](#message-functional-definition-and-content)

9.2.1 Interface Management messages [147](#interface-management-messages)

9.2.1.1 RESET [147](#reset-1)

9.2.1.2 RESET ACKNOWLEDGE [148](#reset-acknowledge)

9.2.1.3 ERROR INDICATION [148](#error-indication-1)

9.2.1.4 F1 SETUP REQUEST [149](#f1-setup-request)

9.2.1.5 F1 SETUP RESPONSE [150](#f1-setup-response)

9.2.1.6 F1 SETUP FAILURE [151](#f1-setup-failure)

9.2.1.7 GNB-DU CONFIGURATION UPDATE [151](#gnb-du-configuration-update-1)

9.2.1.8 GNB-DU CONFIGURATION UPDATE ACKNOWLEDGE [153](#gnb-du-configuration-update-acknowledge)

9.2.1.9 GNB-DU CONFIGURATION UPDATE FAILURE [154](#gnb-du-configuration-update-failure)

9.2.1.10 GNB-CU CONFIGURATION UPDATE [154](#gnb-cu-configuration-update-1)

9.2.1.11 GNB-CU CONFIGURATION UPDATE ACKNOWLEDGE [158](#gnb-cu-configuration-update-acknowledge)

9.2.1.12 GNB-CU CONFIGURATION UPDATE FAILURE [160](#gnb-cu-configuration-update-failure)

9.2.1.13 GNB-DU RESOURCE COORDINATION REQUEST [160](#gnb-du-resource-coordination-request)

9.2.1.14 GNB-DU RESOURCE COORDINATION RESPONSE [160](#gnb-du-resource-coordination-response)

9.2.1.15 GNB-DU STATUS INDICATION [161](#gnb-du-status-indication-1)

9.2.1.16 F1 REMOVAL REQUEST [161](#f1-removal-request)

9.2.1.17 F1 REMOVAL RESPONSE [161](#f1-removal-response)

9.2.1.18 F1 REMOVAL FAILURE [162](#f1-removal-failure)

9.2.1.19 NETWORK ACCESS RATE REDUCTION [162](#network-access-rate-reduction-1)

9.2.1.20 RESOURCE STATUS REQUEST [162](#resource-status-request)

9.2.1.21 RESOURCE STATUS RESPONSE [164](#resource-status-response)

9.2.1.22 RESOURCE STATUS FAILURE [164](#resource-status-failure)

9.2.1.23 RESOURCE STATUS UPDATE [164](#resource-status-update)

9.2.1.24 DU-CU TA INFORMATION TRANSFER [166](#du-cu-ta-information-transfer-1)

9.2.1.25 CU-DU TA INFORMATION TRANSFER [167](#cu-du-ta-information-transfer-1)

9.2.1.26 RACH INDICATION [167](#rach-indication-1)

9.2.2 UE Context Management messages [168](#ue-context-management-messages)

9.2.2.1 UE CONTEXT SETUP REQUEST [168](#ue-context-setup-request)

9.2.2.2 UE CONTEXT SETUP RESPONSE [177](#ue-context-setup-response)

9.2.2.3 UE CONTEXT SETUP FAILURE [182](#ue-context-setup-failure)

9.2.2.4 UE CONTEXT RELEASE REQUEST [183](#ue-context-release-request)

9.2.2.5 UE CONTEXT RELEASE COMMAND [183](#ue-context-release-command)

9.2.2.6 UE CONTEXT RELEASE COMPLETE [184](#ue-context-release-complete)

9.2.2.7 UE CONTEXT MODIFICATION REQUEST [185](#ue-context-modification-request)

9.2.2.8 UE CONTEXT MODIFICATION RESPONSE [201](#ue-context-modification-response)

9.2.2.9 UE CONTEXT MODIFICATION FAILURE [209](#ue-context-modification-failure)

9.2.2.10 UE CONTEXT MODIFICATION REQUIRED [209](#ue-context-modification-required)

9.2.2.11 UE CONTEXT MODIFICATION CONFIRM [212](#ue-context-modification-confirm)

9.2.2.11A UE CONTEXT MODIFICATION REFUSE [215](#a-ue-context-modification-refuse)

9.2.2.12 UE INACTIVITY NOTIFICATION [215](#ue-inactivity-notification-1)

9.2.2.13 NOTIFY [215](#notify-1)

9.2.2.14 ACCESS SUCCESS [216](#access-success-1)

9.2.2.15 DU-CU CELL SWITCH NOTIFICATION [216](#du-cu-cell-switch-notification-1)

9.2.2.16 CU-DU CELL SWITCH NOTIFICATION [217](#cu-du-cell-switch-notification-1)

9.2.2.17 CU-DU MOBILITY INITIATION REQUEST [217](#cu-du-mobility-initiation-request)

9.2.3 RRC Message Transfer messages [219](#rrc-message-transfer-messages)

9.2.3.1 INITIAL UL RRC MESSAGE TRANSFER [219](#initial-ul-rrc-message-transfer-1)

9.2.3.2 DL RRC MESSAGE TRANSFER [220](#dl-rrc-message-transfer-1)

9.2.3.3 UL RRC MESSAGE TRANSFER [221](#ul-rrc-message-transfer-1)

9.2.3.4 RRC DELIVERY REPORT [222](#rrc-delivery-report-1)

9.2.4 Warning Message Transmission Messages [222](#warning-message-transmission-messages)

9.2.4.1 WRITE-REPLACE WARNING REQUEST [222](#write-replace-warning-request)

9.2.4.2 WRITE-REPLACE WARNING RESPONSE [223](#write-replace-warning-response)

9.2.4.3 PWS CANCEL REQUEST [223](#pws-cancel-request)

9.2.4.4 PWS CANCEL RESPONSE [224](#pws-cancel-response)

9.2.4.5 PWS RESTART INDICATION [224](#pws-restart-indication-1)

9.2.4.6 PWS FAILURE INDICATION [225](#pws-failure-indication-1)

9.2.5 System Information messages [225](#system-information-messages)

9.2.5.1 SYSTEM INFORMATION DELIVERY COMMAND [225](#system-information-delivery-command)

9.2.6 Paging messages [226](#paging-messages)

9.2.6.1 PAGING [226](#paging-1)

9.2.7 Trace Messages [227](#trace-messages)

9.2.7.1 TRACE START [227](#trace-start-1)

9.2.7.2 DEACTIVATE TRACE [227](#deactivate-trace-1)

9.2.7.3 CELL TRAFFIC TRACE [227](#cell-traffic-trace-1)

9.2.8 Radio Information Transfer messages [228](#radio-information-transfer-messages)

9.2.8.1 DU-CU RADIO INFORMATION TRANSFER [228](#du-cu-radio-information-transfer-1)

9.2.8.2 CU-DU RADIO INFORMATION TRANSFER [228](#cu-du-radio-information-transfer-1)

9.2.9 IAB messages [229](#iab-messages)

9.2.9.1 BAP MAPPING CONFIGURATION [229](#bap-mapping-configuration-1)

9.2.9.2 BAP MAPPING CONFIGURATION ACKNOWLEDGE [230](#bap-mapping-configuration-acknowledge)

9.2.9.2A BAP MAPPING CONFIGURATION FAILURE [230](#a-bap-mapping-configuration-failure)

9.2.9.3 GNB-DU RESOURCE CONFIGURATION [231](#gnb-du-resource-configuration-1)

9.2.9.4 GNB-DU RESOURCE CONFIGURATION ACKNOWLEDGE [235](#gnb-du-resource-configuration-acknowledge)

9.2.9.4A GNB-DU RESOURCE CONFIGURATION FAILURE [235](#a-gnb-du-resource-configuration-failure)

9.2.9.5 IAB TNL ADDRESS REQUEST [235](#iab-tnl-address-request)

9.2.9.6 IAB TNL ADDRESS RESPONSE [236](#iab-tnl-address-response)

9.2.9.6A IAB TNL ADDRESS FAILURE [237](#a-iab-tnl-address-failure)

9.2.9.7 IAB UP CONFIGURATION UPDATE REQUEST [237](#iab-up-configuration-update-request)

9.2.9.8 IAB UP CONFIGURATION UPDATE RESPONSE [238](#iab-up-configuration-update-response)

9.2.9.9 IAB UP CONFIGURATION UPDATE FAILURE [238](#iab-up-configuration-update-failure)

9.2.9.10 MIAB F1 SETUP TRIGGERING [239](#miab-f1-setup-triggering)

9.2.9.11 MIAB F1 SETUP OUTCOME NOTIFICATION [239](#miab-f1-setup-outcome-notification)

9.2.10 Self Optimisation Support Messages [240](#self-optimisation-support-messages)

9.2.10.1 ACCESS AND MOBILITY INDICATION [240](#access-and-mobility-indication-1)

9.2.10.2 DU-CU ACCESS AND MOBILITY INDICATION [241](#du-cu-access-and-mobility-indication-1)

9.2.11 Reference Time Information Reporting messages [241](#reference-time-information-reporting-messages)

9.2.11.1 REFERENCE TIME INFORMATION REPORTING CONTROL [241](#reference-time-information-reporting-control-1)

9.2.11.2 REFERENCE TIME INFORMATION REPORT [241](#reference-time-information-report-1)

9.2.12 Messages for Positioning Procedures [242](#messages-for-positioning-procedures)

9.2.12.1 POSITIONING ASSISTANCE INFORMATION CONTROL [242](#positioning-assistance-information-control-1)

9.2.12.2 POSITIONING ASSISTANCE INFORMATION FEEDBACK [242](#positioning-assistance-information-feedback-1)

9.2.12.3 POSITIONING MEASUREMENT REQUEST [242](#positioning-measurement-request)

9.2.12.4 POSITIONING MEASUREMENT RESPONSE [245](#positioning-measurement-response)

9.2.12.5 POSITIONING MEASUREMENT FAILURE [245](#positioning-measurement-failure)

9.2.12.6 POSITIONING MEASUREMENT REPORT [245](#positioning-measurement-report-1)

9.2.12.7 POSITIONING MEASUREMENT ABORT [246](#positioning-measurement-abort-1)

9.2.12.8 POSITIONING MEASUREMENT FAILURE INDICATION [246](#positioning-measurement-failure-indication-1)

9.2.12.9 POSITIONING MEASUREMENT UPDATE [246](#positioning-measurement-update-1)

9.2.12.10 TRP INFORMATION REQUEST [247](#trp-information-request)

9.2.12.11 TRP INFORMATION RESPONSE [248](#trp-information-response)

9.2.12.12 TRP INFORMATION FAILURE [248](#trp-information-failure)

9.2.12.13 POSITIONING INFORMATION REQUEST [248](#positioning-information-request)

9.2.12.14 POSITIONING INFORMATION RESPONSE [249](#positioning-information-response)

9.2.12.15 POSITIONING INFORMATION FAILURE [249](#positioning-information-failure)

9.2.12.16 POSITIONING ACTIVATION REQUEST [250](#positioning-activation-request)

9.2.12.17 POSITIONING ACTIVATION RESPONSE [250](#positioning-activation-response)

9.2.12.18 POSITIONING ACTIVATION FAILURE [251](#positioning-activation-failure)

9.2.12.19 POSITIONING DEACTIVATION [251](#positioning-deactivation-1)

9.2.12.20 E-CID MEASUREMENT INITIATION REQUEST [251](#e-cid-measurement-initiation-request)

9.2.12.21 E-CID MEASUREMENT INITIATION RESPONSE [252](#e-cid-measurement-initiation-response)

9.2.12.22 E-CID MEASUREMENT INITIATION FAILURE [253](#e-cid-measurement-initiation-failure)

9.2.12.23 E-CID MEASUREMENT FAILURE INDICATION [253](#e-cid-measurement-failure-indication-1)

9.2.12.24 E-CID MEASUREMENT REPORT [253](#e-cid-measurement-report-1)

9.2.12.25 E-CID MEASUREMENT TERMINATION COMMAND [254](#e-cid-measurement-termination-command)

9.2.12.26 POSITIONING INFORMATION UPDATE [254](#positioning-information-update-1)

9.2.12.27 PRS CONFIGURATION REQUEST [254](#prs-configuration-request)

9.2.12.28 PRS CONFIGURATION RESPONSE [255](#prs-configuration-response)

9.2.12.29 PRS CONFIGURATION FAILURE [255](#prs-configuration-failure)

9.2.12.30 MEASUREMENT PRECONFIGURATION REQUIRED [255](#measurement-preconfiguration-required)

9.2.12.31 MEASUREMENT PRECONFIGURATION CONFIRM [256](#measurement-preconfiguration-confirm)

9.2.12.32 MEASUREMENT PRECONFIGURATION REFUSE [256](#measurement-preconfiguration-refuse)

9.2.12.33 MEASUREMENT ACTIVATION [256](#measurement-activation-1)

9.2.12.34 POSITIONING SYSTEM INFORMATION DELIVERY COMMAND [257](#positioning-system-information-delivery-command)

9.2.12.35 SRS INFORMATION RESERVATION NOTIFICATION [257](#srs-information-reservation-notification-1)

9.2.13 Broadcast Context Management messages [258](#broadcast-context-management-messages)

9.2.13.1 BROADCAST CONTEXT SETUP REQUEST [258](#broadcast-context-setup-request)

9.2.13.2 BROADCAST CONTEXT SETUP RESPONSE [259](#broadcast-context-setup-response)

9.2.13.3 BROADCAST CONTEXT SETUP FAILURE [259](#broadcast-context-setup-failure)

9.2.13.4 BROADCAST CONTEXT RELEASE COMMAND [260](#broadcast-context-release-command)

9.2.13.5 BROADCAST CONTEXT RELEASE COMPLETE [260](#broadcast-context-release-complete)

9.2.13.5a BROADCAST CONTEXT RELEASE REQUEST [260](#a-broadcast-context-release-request)

9.2.13.6 BROADCAST CONTEXT MODIFICATION REQUEST [260](#broadcast-context-modification-request)

9.2.13.7 BROADCAST CONTEXT MODIFICATION RESPONSE [262](#broadcast-context-modification-response)

9.2.13.8 BROADCAST CONTEXT MODIFICATION FAILURE [263](#broadcast-context-modification-failure)

9.2.13.9 BROADCAST TRANSPORT RESOURCE REQUEST [263](#broadcast-transport-resource-request-1)

9.2.14 Multicast Context Management messages [263](#multicast-context-management-messages)

9.2.14.1 MULTICAST GROUP PAGING [263](#multicast-group-paging-1)

9.2.14.2 MULTICAST CONTEXT SETUP REQUEST [264](#multicast-context-setup-request)

9.2.14.3 MULTICAST CONTEXT SETUP RESPONSE [265](#multicast-context-setup-response)

9.2.14.4 MULTICAST CONTEXT SETUP FAILURE [265](#multicast-context-setup-failure)

9.2.14.5 MULTICAST CONTEXT RELEASE COMMAND [266](#multicast-context-release-command)

9.2.14.6 MULTICAST CONTEXT RELEASE COMPLETE [266](#multicast-context-release-complete)

9.2.14.6a MULTICAST CONTEXT RELEASE REQUEST [266](#a-multicast-context-release-request)

9.2.14.7 MULTICAST CONTEXT MODIFICATION REQUEST [266](#multicast-context-modification-request)

9.2.14.8 MULTICAST CONTEXT MODIFICATION RESPONSE [267](#multicast-context-modification-response)

9.2.14.9 MULTICAST CONTEXT MODIFICATION FAILURE [268](#multicast-context-modification-failure)

9.2.14.10 MULTICAST DISTRIBUTION SETUP REQUEST [268](#multicast-distribution-setup-request)

9.2.14.11 MULTICAST DISTRIBUTION SETUP RESPONSE [269](#multicast-distribution-setup-response)

9.2.14.12 MULTICAST DISTRIBUTION SETUP FAILURE [270](#multicast-distribution-setup-failure)

9.2.14.13 MULTICAST DISTRIBUTION RELEASE COMMAND [270](#multicast-distribution-release-command)

9.2.14.14 MULTICAST DISTRIBUTION RELEASE COMPLETE [270](#multicast-distribution-release-complete)

9.2.14.15 MULTICAST CONTEXT NOTIFICATION INDICATION [271](#multicast-context-notification-indication)

9.2.14.16 MULTICAST CONTEXT NOTIFICATION CONFIRM [271](#multicast-context-notification-confirm)

9.2.14.17 MULTICAST CONTEXT NOTIFICATION REFUSE [271](#multicast-context-notification-refuse)

9.2.14.18 MULTICAST COMMON CONFIGURATION REQUEST [271](#multicast-common-configuration-request)

9.2.14.19 MULTICAST COMMON CONFIGURATION RESPONSE [271](#multicast-common-configuration-response)

9.2.14.20 MULTICAST COMMON CONFIGURATION REFUSE [272](#multicast-common-configuration-refuse)

9.2.15 PDC Measurement Reporting messages [272](#pdc-measurement-reporting-messages)

9.2.15.1 PDC MEASUREMENT INITIATION REQUEST [272](#pdc-measurement-initiation-request)

9.2.15.2 PDC MEASUREMENT INITIATION RESPONSE [273](#pdc-measurement-initiation-response)

9.2.15.3 PDC MEASUREMENT INITIATION FAILURE [273](#pdc-measurement-initiation-failure)

9.2.15.4 PDC MEASUREMENT REPORT [273](#pdc-measurement-report-1)

9.2.15.5 PDC MEASUREMENT TERMINATION COMMAND [273](#pdc-measurement-termination-command)

9.2.15.6 PDC MEASUREMENT FAILURE INDICATION [274](#pdc-measurement-failure-indication-1)

9.2.16 QMC messages [274](#qmc-messages)

9.2.16.1 QOE INFORMATION TRANSFER [274](#qoe-information-transfer-1)

9.2.16.2 QOE INFORMATION TRANSFER CONTROL [274](#qoe-information-transfer-control-1)

9.2.17 Timing Synchronisation Status Reporting Messages [275](#timing-synchronisation-status-reporting-messages)

9.2.17.1 TIMING SYNCHRONISATION STATUS REQUEST [275](#timing-synchronisation-status-request)

9.2.17.2 TIMING SYNCHRONISATION STATUS RESPONSE [275](#timing-synchronisation-status-response)

9.2.17.3 TIMING SYNCHRONISATION STATUS FAILURE [276](#timing-synchronisation-status-failure)

9.2.17.4 TIMING SYNCHRONISATION STATUS REPORT [276](#timing-synchronisation-status-report-1)

9.3 Information Element Definitions [276](#information-element-definitions)

9.3.1 Radio Network Layer Related IEs [276](#radio-network-layer-related-ies)

9.3.1.1 Message Type [276](#message-type)

9.3.1.2 Cause [276](#cause)

9.3.1.3 Criticality Diagnostics [280](#criticality-diagnostics)

9.3.1.4 gNB-CU UE F1AP ID [281](#gnb-cu-ue-f1ap-id)

9.3.1.5 gNB-DU UE F1AP ID [281](#gnb-du-ue-f1ap-id)

9.3.1.6 RRC-Container [281](#rrc-container)

9.3.1.7 SRB ID [282](#srb-id)

9.3.1.8 DRB ID [282](#drb-id)

9.3.1.9 gNB-DU ID [282](#gnb-du-id)

9.3.1.10 Served Cell Information [282](#served-cell-information)

9.3.1.11 Transmission Action Indicator [288](#transmission-action-indicator)

9.3.1.12 NR CGI [288](#nr-cgi)

9.3.1.13 Time To wait [288](#time-to-wait)

9.3.1.14 PLMN Identity [288](#plmn-identity)

9.3.1.15 Transmission Bandwidth [289](#transmission-bandwidth)

9.3.1.16 Void [289](#void-1)

9.3.1.17 NR Frequency Info [289](#nr-frequency-info)

9.3.1.18 gNB-DU System Information [290](#gnb-du-system-information)

9.3.1.19 E-UTRAN QoS [291](#e-utran-qos)

9.3.1.20 Allocation and Retention Priority [292](#allocation-and-retention-priority)

9.3.1.21 GBR QoS Information [293](#gbr-qos-information)

9.3.1.22 Bit Rate [293](#bit-rate)

9.3.1.23 Transaction ID [293](#transaction-id)

9.3.1.24 DRX Cycle [294](#drx-cycle)

9.3.1.25 CU to DU RRC Information [294](#cu-to-du-rrc-information)

9.3.1.26 DU to CU RRC Information [297](#du-to-cu-rrc-information)

9.3.1.27 RLC Mode [301](#rlc-mode)

9.3.1.28 SUL Information [301](#sul-information)

9.3.1.29 5GS TAC [302](#gs-tac)

9.3.1.29a Configured EPS TAC [302](#a-configured-eps-tac)

9.3.1.30 RRC Reconfiguration Complete Indicator [302](#rrc-reconfiguration-complete-indicator)

9.3.1.31 UL Configuration [302](#ul-configuration)

9.3.1.32 C-RNTI [303](#c-rnti)

9.3.1.33 Cell UL Configured [303](#cell-ul-configured)

9.3.1.34 RAT-Frequency Priority Information [303](#rat-frequency-priority-information)

9.3.1.35 LCID [303](#lcid)

9.3.1.36 Duplication Activation [303](#duplication-activation)

9.3.1.37 Slice Support List [304](#slice-support-list)

9.3.1.38 S-NSSAI [304](#s-nssai)

9.3.1.39 UE Identity Index value [304](#ue-identity-index-value)

9.3.1.40 Paging DRX [304](#paging-drx)

9.3.1.41 Paging Priority [304](#paging-priority)

9.3.1.42 gNB-CU System Information [305](#gnb-cu-system-information)

9.3.1.43 RAN UE Paging identity [305](#ran-ue-paging-identity)

9.3.1.44 CN UE Paging Identity [306](#cn-ue-paging-identity)

9.3.1.45 QoS Flow Level QoS Parameters [306](#qos-flow-level-qos-parameters)

9.3.1.46 GBR QoS Flow Information [307](#gbr-qos-flow-information)

9.3.1.47 Dynamic 5QI Descriptor [307](#dynamic-5qi-descriptor)

9.3.1.48 NG-RAN Allocation and Retention Priority [309](#ng-ran-allocation-and-retention-priority)

9.3.1.49 Non Dynamic 5QI Descriptor [310](#non-dynamic-5qi-descriptor)

9.3.1.50 Maximum Packet Loss Rate [311](#maximum-packet-loss-rate)

9.3.1.51 Packet Delay Budget [311](#packet-delay-budget)

9.3.1.52 Packet Error Rate [311](#packet-error-rate)

9.3.1.53 Averaging Window [311](#averaging-window)

9.3.1.54 Maximum Data Burst Volume [311](#maximum-data-burst-volume)

9.3.1.55 Masked IMEISV [311](#masked-imeisv)

9.3.1.56 Notification Control [312](#notification-control)

9.3.1.57 RAN Area Code [312](#ran-area-code)

9.3.1.58 PWS System Information [312](#pws-system-information)

9.3.1.59 Repetition Period [313](#repetition-period)

9.3.1.60 Number of Broadcasts Requested [313](#number-of-broadcasts-requested)

9.3.1.61 Void [313](#void-2)

9.3.1.62 SIType List [313](#sitype-list)

9.3.1.63 QoS Flow Identifier [313](#qos-flow-identifier)

9.3.1.64 Served E-UTRA Cell Information [314](#served-e-utra-cell-information)

9.3.1.65 Available PLMN List [314](#available-plmn-list)

9.3.1.66 RLC Failure Indication [314](#rlc-failure-indication)

9.3.1.67 Uplink TxDirectCurrentList Information [314](#uplink-txdirectcurrentlist-information)

9.3.1.68 Service Status [314](#service-status)

9.3.1.69 RLC Status [315](#rlc-status)

9.3.1.70 RRC Version [315](#rrc-version)

9.3.1.71 RRC Delivery Status [315](#rrc-delivery-status)

9.3.1.72 QoS Flow Mapping Indication [315](#qos-flow-mapping-indication)

9.3.1.73 Resource Coordination Transfer Information [316](#resource-coordination-transfer-information)

9.3.1.74 E-UTRA PRACH Configuration [316](#e-utra-prach-configuration)

9.3.1.75 Resource Coordination E-UTRA Cell Information [316](#resource-coordination-e-utra-cell-information)

9.3.1.76 Extended Available PLMN List [317](#extended-available-plmn-list)

9.3.1.77 Associated SCell List [318](#associated-scell-list)

9.3.1.78 Cell Direction [318](#cell-direction)

9.3.1.79 Paging Origin [318](#paging-origin)

9.3.1.80 E-UTRA Transmission Bandwidth [318](#e-utra-transmission-bandwidth)

9.3.1.81 Message Identifier [319](#message-identifier)

9.3.1.82 Serial Number [319](#serial-number)

9.3.1.83 UAC Assistance Information [319](#uac-assistance-information)

9.3.1.84 UAC Action [320](#uac-action)

9.3.1.85 UAC reduction Indication [320](#uac-reduction-indication)

9.3.1.86 Additional SIB Message List [320](#additional-sib-message-list)

9.3.1.87 Cell Type [321](#cell-type)

9.3.1.87a Configured TAC Indication [321](#a-configured-tac-indication)

9.3.1.88 Trace Activation [321](#trace-activation)

9.3.1.89 Intended TDD DL-UL Configuration [322](#intended-tdd-dl-ul-configuration)

9.3.1.90 Additional RRM Policy Index [323](#additional-rrm-policy-index)

9.3.1.91 DU-CU RIM Information [323](#du-cu-rim-information)

9.3.1.92 CU-DU RIM Information [324](#cu-du-rim-information)

9.3.1.93 gNB Set ID [324](#gnb-set-id)

9.3.1.94 Lower Layer Presence Status Change [324](#lower-layer-presence-status-change)

9.3.1.95 Traffic Mapping Information [324](#traffic-mapping-information)

9.3.1.96 IP-to-layer-2 traffic mapping Information List [325](#ip-to-layer-2-traffic-mapping-information-list)

9.3.1.97 IP Header Information [325](#ip-header-information)

9.3.1.98 BAP layer BH RLC channel mapping Information List [326](#bap-layer-bh-rlc-channel-mapping-information-list)

9.3.1.99 Mapping Information to Remove [326](#mapping-information-to-remove)

9.3.1.100 Mapping Information Index [327](#mapping-information-index)

9.3.1.101 IAB TNL Addresses Requested [327](#iab-tnl-addresses-requested)

9.3.1.102 IAB TNL Address [327](#iab-tnl-address)

9.3.1.103 Uplink BH Non-UP Traffic Mapping [327](#uplink-bh-non-up-traffic-mapping)

9.3.1.104 Non-UP Traffic Type [328](#non-up-traffic-type)

9.3.1.105 IAB Info IAB-donor-CU [328](#iab-info-iab-donor-cu)

9.3.1.106 IAB Info IAB-DU [328](#iab-info-iab-du)

9.3.1.107 gNB-DU Cell Resource Configuration [328](#gnb-du-cell-resource-configuration)

9.3.1.108 Multiplexing Info [331](#multiplexing-info)

9.3.1.109 IAB STC Info [333](#iab-stc-info)

9.3.1.110 BAP Routing ID [333](#bap-routing-id)

9.3.1.111 BAP Address [334](#bap-address)

9.3.1.112 BAP Path ID [334](#bap-path-id)

9.3.1.113 BH RLC Channel ID [334](#bh-rlc-channel-id)

9.3.1.114 BH Information [334](#_Toc241157050)

9.3.1.115 Control Plane Traffic Type [335](#control-plane-traffic-type)

9.3.1.116 NR V2X Services Authorized [335](#nr-v2x-services-authorized)

9.3.1.117 LTE V2X Services Authorized [335](#lte-v2x-services-authorized)

9.3.1.118 LTE UE Sidelink Aggregate Maximum Bit Rate [336](#lte-ue-sidelink-aggregate-maximum-bit-rate)

9.3.1.119 NR UE Sidelink Aggregate Maximum Bit Rate [336](#nr-ue-sidelink-aggregate-maximum-bit-rate)

9.3.1.120 SL DRB ID [336](#sl-drb-id)

9.3.1.121 PC5 QoS Flow Identifier [336](#pc5-qos-flow-identifier)

9.3.1.122 PC5 QoS Parameters [336](#pc5-qos-parameters)

9.3.1.123 Alternative QoS Parameters Set Index [337](#alternative-qos-parameters-set-index)

9.3.1.124 Alternative QoS Parameters Set Notify Index [337](#alternative-qos-parameters-set-notify-index)

9.3.1.125 Alternative QoS Parameters Set List [337](#alternative-qos-parameters-set-list)

9.3.1.126 Non Dynamic PQI Descriptor [338](#non-dynamic-pqi-descriptor)

9.3.1.127 Dynamic PQI Descriptor [338](#dynamic-pqi-descriptor)

9.3.1.128 TNL Capacity Indicator [339](#tnl-capacity-indicator)

9.3.1.129 Radio Resource Status [339](#radio-resource-status)

9.3.1.130 Composite Available Capacity Group [341](#composite-available-capacity-group)

9.3.1.131 Composite Available Capacity [342](#composite-available-capacity)

9.3.1.132 Cell Capacity Class Value [342](#cell-capacity-class-value)

9.3.1.133 Capacity Value [342](#capacity-value)

9.3.1.134 Slice Available Capacity [343](#slice-available-capacity)

9.3.1.135 Number of Active UEs [343](#number-of-active-ues)

9.3.1.136 Hardware Load Indicator [344](#hardware-load-indicator)

9.3.1.137 NR Carrier List [344](#nr-carrier-list)

9.3.1.138 SSB Positions In Burst [344](#ssb-positions-in-burst)

9.3.1.139 NR PRACH Configuration [345](#nr-prach-configuration)

9.3.1.140 NR PRACH Configuration List [345](#nr-prach-configuration-list)

9.3.1.141 TSC Traffic Characteristics [347](#tsc-traffic-characteristics)

9.3.1.142 TSC Assistance Information [347](#tsc-assistance-information)

9.3.1.143 Periodicity [348](#periodicity)

9.3.1.144 Burst Arrival Time [348](#burst-arrival-time)

9.3.1.145 Extended Packet Delay Budget [348](#extended-packet-delay-budget)

9.3.1.146 RLC Duplication Information [348](#rlc-duplication-information)

9.3.1.147 Reporting Request Type [349](#reporting-request-type)

9.3.1.148 Time Reference Information [349](#time-reference-information)

9.3.1.149 Reference Time [350](#reference-time)

9.3.1.150 MDT Configuration [350](#mdt-configuration)

9.3.1.151 MDT PLMN List [350](#mdt-plmn-list)

9.3.1.152 M5 Configuration [351](#m5-configuration)

9.3.1.153 M6 Configuration [351](#m6-configuration)

9.3.1.154 M7 Configuration [351](#_Toc241157090)

9.3.1.155 NID [352](#nid)

9.3.1.156 NPN Support Information [352](#npn-support-information)

9.3.1.157 NPN Broadcast Information [352](#npn-broadcast-information)

9.3.1.158 Broadcast SNPN ID List [352](#broadcast-snpn-id-list)

9.3.1.159 Broadcast NID List [353](#broadcast-nid-list)

9.3.1.160 Broadcast CAG-Identifier List [353](#broadcast-cag-identifier-list)

9.3.1.161 CAG ID [353](#cag-id)

9.3.1.162 Broadcast PNI-NPN ID Information [353](#broadcast-pni-npn-id-information)

9.3.1.163 Available SNPN ID List [353](#available-snpn-id-list)

9.3.1.164 Void [354](#void-3)

9.3.1.165 Extended Slice Support List [354](#extended-slice-support-list)

9.3.1.166 Positioning Measurement Result [354](#positioning-measurement-result)

9.3.1.167 UL Angle of Arrival [355](#ul-angle-of-arrival)

9.3.1.168 UL RTOA Measurement [356](#ul-rtoa-measurement)

9.3.1.169 Additional Path List [356](#additional-path-list)

9.3.1.170 gNB Rx-Tx Time Difference [357](#gnb-rx-tx-time-difference)

9.3.1.171 Time Stamp [358](#time-stamp)

9.3.1.172 TRP Measurement Quality [359](#trp-measurement-quality)

9.3.1.173 Measurement Beam Information [359](#measurement-beam-information)

9.3.1.174 NG-RAN Access Point Position [359](#ng-ran-access-point-position)

9.3.1.175 Requested SRS Transmission Characteristics [360](#requested-srs-transmission-characteristics)

9.3.1.176 TRP Information [362](#trp-information)

9.3.1.177 PRS Configuration [363](#prs-configuration)

9.3.1.178 DL-PRS Muting Pattern [365](#dl-prs-muting-pattern)

9.3.1.179 Spatial Direction Information [365](#spatial-direction-information)

9.3.1.180 SRS Resource Set ID [365](#srs-resource-set-id)

9.3.1.181 Spatial Relation Information [366](#spatial-relation-information)

9.3.1.182 SRS Resource Trigger [366](#srs-resource-trigger)

9.3.1.183 Relative Time 1900 [366](#relative-time-1900)

9.3.1.184 Geographical Coordinates [367](#geographical-coordinates)

9.3.1.185 DL-PRS Resource Coordinates [368](#dl-prs-resource-coordinates)

9.3.1.186 Relative Geodetic Location [368](#relative-geodetic-location)

9.3.1.187 Relative Cartesian Location [369](#relative-cartesian-location)

9.3.1.188 Reference Point [369](#reference-point)

9.3.1.189 Location Uncertainty [370](#location-uncertainty)

9.3.1.190 NG-RAN High Accuracy Access Point Position [370](#ng-ran-high-accuracy-access-point-position)

9.3.1.191 Positioning Broadcast Cells [370](#positioning-broadcast-cells)

9.3.1.192 SRS Configuration [371](#srs-configuration)

9.3.1.193 SRS Resource [372](#srs-resource)

9.3.1.194 Positioning SRS Resource [374](#positioning-srs-resource)

9.3.1.195 SRS Resource Set [375](#srs-resource-set)

9.3.1.196 Positioning SRS Resource Set [376](#positioning-srs-resource-set)

9.3.1.197 TRP ID [376](#trp-id)

9.3.1.198 NR-PRS Beam Information [376](#nr-prs-beam-information)

9.3.1.199 E-CID Measurement Result [377](#e-cid-measurement-result)

9.3.1.200 Cell Portion ID [378](#cell-portion-id)

9.3.1.201 Pathloss Reference Information [378](#pathloss-reference-information)

9.3.1.202 SSB Information [379](#ssb-information)

9.3.1.203 SSB Time/Frequency Configuration [379](#ssb-timefrequency-configuration)

9.3.1.204 Search Window Information [379](#search-window-information)

9.3.1.205 Extended gNB-DU Name [380](#extended-gnb-du-name)

9.3.1.206 Extended gNB-CU Name [380](#extended-gnb-cu-name)

9.3.1.207 F1-C Transfer Path [380](#f1-c-transfer-path)

9.3.1.208 SFN Offset [380](#sfn-offset)

9.3.1.209 Transmission Stop Indicator [381](#transmission-stop-indicator)

9.3.1.210 Spatial Relation Information per SRS Resource [381](#spatial-relation-information-per-srs-resource)

9.3.1.211 CCO Assistance Information [381](#cco-assistance-information)

9.3.1.212 Affected Cells and Beams [382](#affected-cells-and-beams)

9.3.1.213 Coverage Modification Notification [382](#coverage-modification-notification)

9.3.1.214 Cells for SON List [383](#cells-for-son-list)

9.3.1.215 Neighbour NR Cells for SON List [383](#neighbour-nr-cells-for-son-list)

9.3.1.216 NR Mode Info Rel16 [384](#nr-mode-info-rel16)

9.3.1.217 Frequency Info Rel16 [384](#frequency-info-rel16)

9.3.1.218 MBS Session ID [384](#mbs-session-id)

9.3.1.219 gNB-CU MBS F1AP ID [385](#gnb-cu-mbs-f1ap-id)

9.3.1.220 gNB-DU MBS F1AP ID [385](#gnb-du-mbs-f1ap-id)

9.3.1.221 MBS Area Session ID [385](#mbs-area-session-id)

9.3.1.222 MBS Service Area [385](#mbs-service-area)

9.3.1.223 MBS Service Area Information [386](#mbs-service-area-information)

9.3.1.224 MRB ID [386](#mrb-id)

9.3.1.225 MBS CU to DU RRC Information [386](#mbs-cu-to-du-rrc-information)

9.3.1.226 MBS Broadcast Neighbour Cell List [387](#mbs-broadcast-neighbour-cell-list)

9.3.1.227 IAB Congestion Indication [387](#iab-congestion-indication)

9.3.1.228 F1-C Transfer Path NRDC [387](#f1-c-transfer-path-nrdc)

9.3.1.229 IAB TNL Address Exception [387](#iab-tnl-address-exception)

9.3.1.230 RB Set Configuration [388](#rb-set-configuration)

9.3.1.231 Survival Time [388](#survival-time)

9.3.1.232 PDC Measurement Result [388](#pdc-measurement-result)

9.3.1.233 SCG Activation Request [389](#scg-activation-request)

9.3.1.234 SCG Activation Status [389](#scg-activation-status)

9.3.1.235 Requested DL PRS Transmission Characteristics [389](#requested-dl-prs-transmission-characteristics)

9.3.1.236 Start Time and Duration [390](#start-time-and-duration)

9.3.1.237 PRS Transmission Off Information [390](#prs-transmission-off-information)

9.3.1.238 UL-AoA Assistance Information [391](#ul-aoa-assistance-information)

9.3.1.239 Zenith Angle of Arrival Information [391](#zenith-angle-of-arrival-information)

9.3.1.240 On-demand PRS TRP Information [392](#on-demand-prs-trp-information)

9.3.1.241 LCS to GCS Translation [393](#lcs-to-gcs-translation)

9.3.1.242 Response Time [393](#response-time)

9.3.1.243 ARP Location Information [394](#arp-location-information)

9.3.1.244 ARP ID [394](#arp-id)

9.3.1.245 Multiple UL AoA [394](#multiple-ul-aoa)

9.3.1.246 UL SRS-RSRPP [395](#ul-srs-rsrpp)

9.3.1.247 SRS Resource type [395](#srs-resource-type)

9.3.1.248 Extended Additional Path List [395](#extended-additional-path-list)

9.3.1.249 LoS/NLoS Information [396](#losnlos-information)

9.3.1.250 Requested DL-PRS Resource List [396](#requested-dl-prs-resource-list)

9.3.1.251 Void [397](#void-4)

9.3.1.252 TRP Tx TEG Association [397](#trp-tx-teg-association)

9.3.1.253 TRP TEG Information [397](#trp-teg-information)

9.3.1.254 Measurement Characteristics Request Indicator [397](#measurement-characteristics-request-indicator)

9.3.1.255 UE Reporting Information [398](#ue-reporting-information)

9.3.1.256 TRP Beam Antenna Information [399](#trp-beam-antenna-information)

9.3.1.257 TRP Beam Antenna Angles [399](#trp-beam-antenna-angles)

9.3.1.258 NR Paging eDRX Information [400](#nr-paging-edrx-information)

9.3.1.259 NR Paging eDRX Information for RRC INACTIVE [401](#nr-paging-edrx-information-for-rrc-inactive)

9.3.1.260 QoE Metrics [401](#qoe-metrics)

9.3.1.261 CG-SDT Session Info [401](#cg-sdt-session-info)

9.3.1.262 SDT Information [401](#sdt-information)

9.3.1.263 Path Switch Configuration [402](#path-switch-configuration)

9.3.1.264 Sidelink Relay Configuration [402](#sidelink-relay-configuration)

9.3.1.265 PC5 RLC Channel ID [402](#pc5-rlc-channel-id)

9.3.1.266 Uu RLC Channel ID [402](#uu-rlc-channel-id)

9.3.1.267 Remote UE Local ID [402](#remote-ue-local-id)

9.3.1.268 5G ProSe Authorized [403](#g-prose-authorized)

9.3.1.269 PEIPS Assistance Information [403](#peips-assistance-information)

9.3.1.270 UE Paging Capability [404](#ue-paging-capability)

9.3.1.271 gNB-DU UE Slice Maximum Bit Rate List [404](#gnb-du-ue-slice-maximum-bit-rate-list)

9.3.1.272 Multicast MBS Session List [404](#multicast-mbs-session-list)

9.3.1.273 TAI NSAG Support List [404](#tai-nsag-support-list)

9.3.1.274 MDT PLMN Modification List [405](#mdt-plmn-modification-list)

9.3.1.275 MRB RLC Configuration [405](#mrb-rlc-configuration)

9.3.1.276 Timing Error Margin [406](#timing-error-margin)

9.3.1.277 SDT Bearer Configuration Info [406](#sdt-bearer-configuration-info)

9.3.1.278 PosSIType List [406](#possitype-list)

9.3.1.279 IAB-DU Cell Resource Configuration-Mode-Info [407](#iab-du-cell-resource-configuration-mode-info)

9.3.1.280 TRP Rx TEG Information [408](#trp-rx-teg-information)

9.3.1.281 TRP Tx TEG Information [408](#trp-tx-teg-information)

9.3.1.282 TRP RxTx TEG Information [408](#trp-rxtx-teg-information)

9.3.1.283 Uplink TxDirectCurrentTwoCarrierList Information [408](#uplink-txdirectcurrenttwocarrierlist-information)

9.3.1.284 Uplink TxDirectCurrentMoreCarrierList Information [409](#uplink-txdirectcurrentmorecarrierlist-information)

9.3.1.285 Extended UE Identity Index Value [409](#extended-ue-identity-index-value)

9.3.1.286 Hashed UE Identity Index Value [409](#hashed-ue-identity-index-value)

9.3.1.287 Broadcast Area Scope [409](#broadcast-area-scope)

9.3.1.288 Network Controlled Repeater Authorized [409](#network-controlled-repeater-authorized)

9.3.1.289 MT-SDT Information [410](#mt-sdt-information)

9.3.1.290 Supported UE Type List [410](#supported-ue-type-list)

9.3.1.291 LTM Cells To Be Released List [410](#ltm-cells-to-be-released-list)

9.3.1.292 Reference Configuration [410](#reference-configuration)

9.3.1.293 Void [411](#void-5)

9.3.1.294 LTM Configuration ID Mapping List [411](#ltm-configuration-id-mapping-list)

9.3.1.295 Radio Resource Status NR-U [411](#radio-resource-status-nr-u)

9.3.1.296 Path Addition Information [411](#path-addition-information)

9.3.1.297 Recommended SSBs for Paging List [412](#recommended-ssbs-for-paging-list)

9.3.1.298 RAN Timing Synchronisation Status Information [412](#ran-timing-synchronisation-status-information)

9.3.1.299 Clock Accuracy [412](#clock-accuracy)

9.3.1.300 Burst Arrival Time Window [413](#burst-arrival-time-window)

9.3.1.301 Periodicity Range [413](#periodicity-range)

9.3.1.302 TSC Traffic Characteristics Feedback [413](#tsc-traffic-characteristics-feedback)

9.3.1.303 TSC Feedback Information [414](#tsc-feedback-information)

9.3.1.304 Mobile TRP Location Information [414](#mobile-trp-location-information)

9.3.1.305 Global gNB ID [414](#global-gnb-id)

9.3.1.306 RRC Terminating IAB-Donor Related Info [414](#rrc-terminating-iab-donor-related-info)

9.3.1.307 Mobile IAB-MT User Location Information [415](#mobile-iab-mt-user-location-information)

9.3.1.308 TAI [415](#tai)

9.3.1.309 Associated Session ID [415](#associated-session-id)

9.3.1.310 Multicast CU to DU RRC Information [415](#multicast-cu-to-du-rrc-information)

9.3.1.311 Multicast DU to CU RRC Information [416](#multicast-du-to-cu-rrc-information)

9.3.1.312 MBS Multicast Configuration Response Information [416](#mbs-multicast-configuration-response-information)

9.3.1.313 MBS Multicast Configuration Notification [416](#mbs-multicast-configuration-notification)

9.3.1.314 Multicast CU to DU Common RRC Information [417](#multicast-cu-to-du-common-rrc-information)

9.3.1.315 Update MBS Multicast Neighbour Cell List Information [417](#update-mbs-multicast-neighbour-cell-list-information)

9.3.1.316 Update ThresholdMBS-List Information [418](#update-thresholdmbs-list-information)

9.3.1.317 MBS Multicast Session Reception State [419](#mbs-multicast-session-reception-state)

9.3.1.318 Multicast RRC_INACTIVE Reception Mode [419](#multicast-rrc_inactive-reception-mode)

9.3.1.319 PDU Set QoS Information [419](#pdu-set-qos-information)

9.3.1.320 N6 Jitter Information [419](#n6-jitter-information)

9.3.1.321 ECN Marking or Congestion Information Reporting Request [419](#ecn-marking-or-congestion-information-reporting-request)

9.3.1.322 ECN Marking or Congestion Information Reporting Status [420](#ecn-marking-or-congestion-information-reporting-status)

9.3.1.323 NR A2X Services Authorized [420](#nr-a2x-services-authorized)

9.3.1.324 LTE A2X Services Authorized [420](#lte-a2x-services-authorized)

9.3.1.325 NR Paging Long eDRX Information for RRC INACTIVE [420](#nr-paging-long-edrx-information-for-rrc-inactive)

9.3.1.326 SSBs within the cell to be Activated List [421](#ssbs-within-the-cell-to-be-activated-list)

9.3.1.327 DL LBT Failure Information [421](#dl-lbt-failure-information)

9.3.1.328 Early UL Sync Configuration [421](#early-ul-sync-configuration)

9.3.1.329 Preamble Index List [421](#preamble-index-list)

9.3.1.330 CSI Resource Configuration [422](#csi-resource-configuration)

9.3.1.331 Ranging and Sidelink Positioning Service Information [422](#ranging-and-sidelink-positioning-service-information)

9.3.1.332 RSPP Transport QoS Parameters [422](#rspp-transport-qos-parameters)

9.3.1.333 Time Window Information SRS List [423](#time-window-information-srs-list)

9.3.1.334 Time Window Information Measurement List [423](#time-window-information-measurement-list)

9.3.1.335 UL RSCP [424](#ul-rscp)

9.3.1.336 Positioning Validity Area Cell List [424](#positioning-validity-area-cell-list)

9.3.1.337 Aggregated Positioning SRS Resource Set List [425](#aggregated-positioning-srs-resource-set-list)

9.3.1.338 Aggregated PRS Resource Set List [425](#aggregated-prs-resource-set-list)

9.3.1.339 Validity Area specific SRS Information [426](#validity-area-specific-srs-information)

9.3.1.340 Requested SRS Preconfiguration Characteristics List [427](#requested-srs-preconfiguration-characteristics-list)

9.3.1.341 SRS Preconfiguration List [427](#srs-preconfiguration-list)

9.3.1.342 SRS Periodicity [427](#srs-periodicity)

9.3.1.343 Tx Hopping Configuration [428](#_Toc241157279)

9.3.1.344 Non-Integer DRX Cycle [428](#non-integer-drx-cycle)

9.3.1.345 RAN Sharing Assistance Information [429](#ran-sharing-assistance-information)

9.3.1.346 LTM Reset Information [429](#ltm-reset-information)

9.3.1.347 PRS Bandwidth Aggregation Request Information List [430](#prs-bandwidth-aggregation-request-information-list)

9.3.1.348 Candidate Cell with Beam Information [431](#candidate-cell-with-beam-information)

9.3.1.349 Candidate Cell with Beam Information List [431](#candidate-cell-with-beam-information-list)

9.3.1.350 Measurement Quantities [431](#measurement-quantities)

9.3.1.351 Validity Area specific SRS Information Extended [432](#validity-area-specific-srs-information-extended)

9.3.1.352 Void [433](#void-6)

9.3.1.353 Void [433](#void-7)

9.3.1.354 Void [433](#void-8)

9.3.1.355 Void [433](#void-9)

9.3.1.356 Void [433](#void-10)

9.3.1.357 Void [433](#void-11)

9.3.1.358 Void [433](#void-12)

9.3.1.359 Void [433](#void-13)

9.3.1.360 Void [433](#void-14)

9.3.1.361 Void [433](#void-15)

9.3.1.362 Void [433](#void-16)

9.3.1.363 Void [433](#void-17)

9.3.1.364 Void [433](#void-18)

9.3.1.365 Void [433](#void-19)

9.3.1.366 Void [433](#void-20)

9.3.1.367 Void [433](#void-21)

9.3.1.368 Void [433](#void-22)

9.3.1.369 Void [433](#void-23)

9.3.1.370 Void [433](#void-24)

9.3.1.371 Void [433](#void-25)

9.3.1.372 Area-specific Semi-persistent SRS Positioning Information [433](#area-specific-semi-persistent-srs-positioning-information)

9.3.2 Transport Network Layer Related IEs [434](#transport-network-layer-related-ies)

9.3.2.1 UP Transport Layer Information [434](#up-transport-layer-information)

9.3.2.2 GTP-TEID [434](#gtp-teid)

9.3.2.3 Transport Layer Address [434](#transport-layer-address)

9.3.2.4 CP Transport Layer Information [434](#cp-transport-layer-information)

9.3.2.5 Transport Layer Address Info [435](#transport-layer-address-info)

9.3.2.6 URI [435](#uri)

9.3.2.7 BC Bearer Context F1-U TNL Info [436](#bc-bearer-context-f1-u-tnl-info)

9.3.2.8 MBS Multicast F1-U Context Descriptor [436](#mbs-multicast-f1-u-context-descriptor)

9.3.2.9 Void [437](#void-26)

9.3.2.10 MBS PTP Retransmission Tunnel Required [437](#mbs-ptp-retransmission-tunnel-required)

9.3.2.11 Multicast F1-U Context Reference F1 [437](#multicast-f1-u-context-reference-f1)

9.3.2.12 MRB Progress Information [437](#mrb-progress-information)

9.3.2.13 Multicast F1-U Context Reference CU [437](#multicast-f1-u-context-reference-cu)

9.4 Message and Information Element Abstract Syntax (with ASN.1) [438](#message-and-information-element-abstract-syntax-with-asn.1)

9.4.1 General [438](#general-96)

9.4.2 Usage of private message mechanism for non-standard use [438](#usage-of-private-message-mechanism-for-non-standard-use)

9.4.3 Elementary Procedure Definitions [439](#elementary-procedure-definitions)

9.4.4 PDU Definitions [459](#pdu-definitions)

9.4.5 Information Element Definitions [573](#information-element-definitions-1)

9.4.6 Common Definitions [768](#common-definitions)

9.4.7 Constant Definitions [769](#constant-definitions)

9.4.8 Container Definitions [791](#container-definitions)

9.5 Message Transfer Syntax [795](#message-transfer-syntax)

9.6 Timers [795](#timers)

10 Handling of unknown, unforeseen and erroneous protocol data [795](#handling-of-unknown-unforeseen-and-erroneous-protocol-data)

Annex A (informative): Change History [796](#annex-a-informative-change-history)

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
