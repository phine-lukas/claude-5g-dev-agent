<img src="media/image1.jpeg" style="width:1.32569in;height:1.32569in" /><img src="media/image2.png" style="width:1.77708in;height:1.03889in" />

#  

# Contents

Foreword [17](#foreword)

1 Scope [18](#scope)

2 References [18](#references)

3 Definitions and abbreviations [20](#definitions-and-abbreviations)

3.1 Definitions [20](#definitions)

3.2 Abbreviations [21](#abbreviations)

4 General [22](#general)

4.1 Procedure specification principles [22](#procedure-specification-principles)

4.2 Forwards and backwards compatibility [23](#forwards-and-backwards-compatibility)

4.3 Specification notations [23](#specification-notations)

5 F1AP services [23](#f1ap-services)

6 Services expected from signalling transport [23](#services-expected-from-signalling-transport)

7 Functions of F1AP [23](#functions-of-f1ap)

8 F1AP procedures [24](#f1ap-procedures)

8.1 List of F1AP Elementary procedures [24](#list-of-f1ap-elementary-procedures)

8.2 Interface Management procedures [28](#interface-management-procedures)

8.2.1 Reset [28](#reset)

8.2.1.1 General [28](#general-1)

8.2.1.2 Successful Operation [28](#successful-operation)

8.2.1.2.1 Reset Procedure Initiated from the gNB-CU [28](#reset-procedure-initiated-from-the-gnb-cu)

8.2.1.2.2 Reset Procedure Initiated from the gNB-DU [29](#reset-procedure-initiated-from-the-gnb-du)

8.2.1.3 Abnormal Conditions [30](#abnormal-conditions)

8.2.2 Error Indication [30](#error-indication)

8.2.2.1 General [30](#general-2)

8.2.2.2 Successful Operation [30](#successful-operation-1)

8.2.2.3 Abnormal Conditions [30](#abnormal-conditions-1)

8.2.3 F1 Setup [30](#f1-setup)

8.2.3.1 General [30](#general-3)

8.2.3.2 Successful Operation [31](#successful-operation-2)

8.2.3.3 Unsuccessful Operation [33](#unsuccessful-operation)

8.2.3.4 Abnormal Conditions [33](#abnormal-conditions-2)

8.2.4 gNB-DU Configuration Update [33](#gnb-du-configuration-update)

8.2.4.1 General [33](#general-4)

8.2.4.2 Successful Operation [33](#successful-operation-3)

8.2.4.3 Unsuccessful Operation [36](#unsuccessful-operation-1)

8.2.4.4 Abnormal Conditions [36](#abnormal-conditions-3)

8.2.5 gNB-CU Configuration Update [36](#gnb-cu-configuration-update)

8.2.5.1 General [36](#general-5)

8.2.5.2 Successful Operation [36](#successful-operation-4)

8.2.5.3 Unsuccessful Operation [38](#unsuccessful-operation-2)

8.2.5.4 Abnormal Conditions [39](#abnormal-conditions-4)

8.2.6 gNB-DU Resource Coordination [39](#gnb-du-resource-coordination)

8.2.6.1 General [39](#general-6)

8.2.6.2 Successful Operation [39](#successful-operation-5)

8.2.7 gNB-DU Status Indication [39](#gnb-du-status-indication)

8.2.7.1 General [39](#general-7)

8.2.7.2 Successful Operation [40](#successful-operation-6)

8.2.7.3 Abnormal Conditions [40](#abnormal-conditions-5)

8.2.8 F1 Removal [40](#f1-removal)

8.2.8.1 General [40](#general-8)

8.2.8.2 Successful Operation [40](#successful-operation-7)

8.2.8.3 Unsuccessful Operation [41](#unsuccessful-operation-3)

8.2.8.4 Abnormal Conditions [42](#abnormal-conditions-6)

8.2.9 Network Access Rate Reduction [42](#network-access-rate-reduction)

8.2.9.1 General [42](#general-9)

8.2.9.2 Successful operation [42](#successful-operation-8)

8.2.9.3 Abnormal Conditions [42](#abnormal-conditions-7)

8.2.10 Resource Status Reporting Initiation [42](#resource-status-reporting-initiation)

8.2.10.1 General [42](#general-10)

8.2.10.2 Successful Operation [43](#successful-operation-9)

8.2.10.3 Unsuccessful Operation [44](#unsuccessful-operation-4)

8.2.10.4 Abnormal Conditions [44](#abnormal-conditions-8)

8.2.11 Resource Status Reporting [44](#resource-status-reporting)

8.2.11.1 General [44](#general-11)

8.2.11.2 Successful Operation [45](#successful-operation-10)

8.2.11.3 Unsuccessful Operation [45](#unsuccessful-operation-5)

8.2.11.4 Abnormal Conditions [45](#abnormal-conditions-9)

8.3 UE Context Management procedures [45](#ue-context-management-procedures)

8.3.1 UE Context Setup [45](#ue-context-setup)

8.3.1.1 General [45](#general-12)

8.3.1.2 Successful Operation [45](#successful-operation-11)

8.3.1.3 Unsuccessful Operation [52](#unsuccessful-operation-6)

8.3.1.4 Abnormal Conditions [52](#abnormal-conditions-10)

8.3.2 UE Context Release Request (gNB-DU initiated) [52](#ue-context-release-request-gnb-du-initiated)

8.3.2.1 General [52](#general-13)

8.3.2.2 Successful Operation [53](#successful-operation-12)

8.3.2.3 Abnormal Conditions [53](#abnormal-conditions-11)

8.3.3 UE Context Release (gNB-CU initiated) [53](#ue-context-release-gnb-cu-initiated)

8.3.3.1 General [53](#general-14)

8.3.3.2 Successful Operation [54](#successful-operation-13)

8.3.3.4 Abnormal Conditions [54](#abnormal-conditions-12)

8.3.4 UE Context Modification (gNB-CU initiated) [54](#ue-context-modification-gnb-cu-initiated)

8.3.4.1 General [54](#general-15)

8.3.4.2 Successful Operation [55](#successful-operation-14)

8.3.4.3 Unsuccessful Operation [63](#unsuccessful-operation-7)

8.3.4.4 Abnormal Conditions [63](#abnormal-conditions-13)

8.3.5 UE Context Modification Required (gNB-DU initiated) [64](#ue-context-modification-required-gnb-du-initiated)

8.3.5.1 General [64](#general-16)

8.3.5.2 Successful Operation [64](#successful-operation-15)

8.3.5.2A Unsuccessful Operation [65](#a-unsuccessful-operation)

8.3.5.3 Abnormal Conditions [65](#abnormal-conditions-14)

8.3.6 UE Inactivity Notification [66](#ue-inactivity-notification)

8.3.6.1 General [66](#general-17)

8.3.6.2 Successful Operation [66](#successful-operation-16)

8.3.6.3 Abnormal Conditions [66](#abnormal-conditions-15)

8.3.7 Notify [66](#notify)

8.3.7.1 General [66](#general-18)

8.3.7.2 Successful Operation [66](#successful-operation-17)

8.3.7.3 Abnormal Conditions [67](#abnormal-conditions-16)

8.3.8 Access Success [67](#access-success)

8.3.8.1 General [67](#general-19)

8.3.8.2 Successful Operation [67](#successful-operation-18)

8.3.8.3 Abnormal Conditions [67](#abnormal-conditions-17)

8.4 RRC Message Transfer procedures [68](#rrc-message-transfer-procedures)

8.4.1 Initial UL RRC Message Transfer [68](#initial-ul-rrc-message-transfer)

8.4.1.1 General [68](#general-20)

8.4.1.2 Successful operation [68](#successful-operation-19)

8.4.1.3 Abnormal Conditions [68](#abnormal-conditions-18)

8.4.2 DL RRC Message Transfer [69](#dl-rrc-message-transfer)

8.4.2.1 General [69](#general-21)

8.4.2.2 Successful operation [69](#successful-operation-20)

8.4.2.3 Abnormal Conditions [69](#abnormal-conditions-19)

8.4.3 UL RRC Message Transfer [70](#ul-rrc-message-transfer)

8.4.3.1 General [70](#general-22)

8.4.3.2 Successful operation [70](#successful-operation-21)

8.4.3.3 Abnormal Conditions [70](#abnormal-conditions-20)

8.4.4 RRC Delivery Report [70](#rrc-delivery-report)

8.4.4.1 General [70](#general-23)

8.4.4.2 Successful operation [71](#successful-operation-22)

8.4.4.3 Abnormal Conditions [71](#abnormal-conditions-21)

8.5 Warning Message Transmission Procedures [71](#warning-message-transmission-procedures)

8.5.1 Write-Replace Warning [71](#write-replace-warning)

8.5.1.1 General [71](#general-24)

8.5.1.2 Successful Operation [71](#successful-operation-23)

8.5.1.3 Unsuccessful Operation [72](#unsuccessful-operation-8)

8.5.1.4 Abnormal Conditions [72](#abnormal-conditions-22)

8.5.2 PWS Cancel [72](#pws-cancel)

8.5.2.1 General [72](#general-25)

8.5.2.2 Successful Operation [72](#successful-operation-24)

8.5.2.3 Unsuccessful Operation [73](#unsuccessful-operation-9)

8.5.2.4 Abnormal Conditions [73](#abnormal-conditions-23)

8.5.3 PWS Restart Indication [73](#pws-restart-indication)

8.5.3.1 General [73](#general-26)

8.5.3.2 Successful Operation [73](#successful-operation-25)

8.5.3.3 Abnormal Conditions [74](#abnormal-conditions-24)

8.5.4 PWS Failure Indication [74](#pws-failure-indication)

8.5.4.1 General [74](#general-27)

8.5.4.2 Successful Operation [74](#successful-operation-26)

8.5.4.3 Abnormal Conditions [74](#abnormal-conditions-25)

8.6 System Information Procedures [74](#system-information-procedures)

8.6.1 System Information Delivery [74](#system-information-delivery)

8.6.1.1 General [74](#general-28)

8.6.1.2 Successful Operation [74](#successful-operation-27)

8.6.1.3 Abnormal Conditions [75](#abnormal-conditions-26)

8.7 Paging procedures [75](#paging-procedures)

8.7.1 Paging [75](#paging)

8.7.1.1 General [75](#general-29)

8.7.1.2 Successful Operation [75](#successful-operation-28)

8.7.1.3 Abnormal Conditions [76](#abnormal-conditions-27)

8.8 Trace Procedures [76](#trace-procedures)

8.8.1 Trace Start [76](#trace-start)

8.8.1.1 General [76](#general-30)

8.8.1.2 Successful Operation [76](#successful-operation-29)

8.8.1.3 Abnormal Conditions [77](#abnormal-conditions-28)

8.8.2 Deactivate Trace [77](#deactivate-trace)

8.8.2.1 General [77](#general-31)

8.8.2.2 Successful Operation [77](#successful-operation-30)

8.8.2.3 Abnormal Conditions [77](#abnormal-conditions-29)

8.8.3 Cell Traffic Trace [77](#cell-traffic-trace)

8.8.3.1 General [77](#general-32)

8.8.3.2 Successful Operation [77](#successful-operation-31)

8.8.3.3 Abnormal Conditions [78](#abnormal-conditions-30)

8.9 Radio Information Transfer procedures [78](#radio-information-transfer-procedures)

8.9.1 DU-CU Radio Information Transfer [78](#du-cu-radio-information-transfer)

8.9.1.1 General [78](#general-33)

8.9.1.2 Successful operation [78](#successful-operation-32)

8.9.1.3 Abnormal Conditions [78](#abnormal-conditions-31)

8.9.2 CU-DU Radio Information Transfer [78](#cu-du-radio-information-transfer)

8.9.2.1 General [78](#general-34)

8.9.2.2 Successful operation [79](#successful-operation-33)

8.9.2.3 Abnormal Conditions [79](#abnormal-conditions-32)

8.10 IAB Procedures [79](#iab-procedures)

8.10.0 General [79](#general-35)

8.10.1 BAP Mapping Configuration [79](#bap-mapping-configuration)

8.10.1.1 General [79](#general-36)

8.10.1.2 Successful Operation [79](#successful-operation-34)

8.10.1.A Unsuccessful Operation [80](#a-unsuccessful-operation-1)

8.10.1.3 Abnormal Conditions [81](#abnormal-conditions-33)

8.10.2 gNB-DU Resource Configuration [81](#gnb-du-resource-configuration)

8.10.2.1 General [81](#general-37)

8.10.2.2 Successful Operation [81](#successful-operation-35)

8.10.2.B Unsuccessful Operation [82](#b-unsuccessful-operation)

8.10.2.3 Abnormal Conditions [82](#abnormal-conditions-34)

8.10.3 IAB TNL Address Allocation [82](#iab-tnl-address-allocation)

8.10.3.1 General [82](#general-38)

8.10.3.2 Successful Operation [82](#successful-operation-36)

8.10.3.C Unsuccessful Operation [83](#c-unsuccessful-operation)

8.10.3.3 Abnormal Conditions [83](#abnormal-conditions-35)

8.10.4 IAB UP Configuration Update [83](#iab-up-configuration-update)

8.10.4.1 General [83](#general-39)

8.10.4.2 Successful Operation [84](#successful-operation-37)

8.10.4.3 Unsuccessful Operation [84](#unsuccessful-operation-10)

8.10.4.4 Abnormal Conditions [84](#abnormal-conditions-36)

8.11 Self Optimisation Support procedures [85](#self-optimisation-support-procedures)

8.11.1 Access and Mobility Indication [85](#access-and-mobility-indication)

8.11.1.1 General [85](#general-40)

8.11.1.2 Successful Operation [85](#successful-operation-38)

8.11.1.3 Abnormal Conditions [85](#abnormal-conditions-37)

8.12 Reference Time Information Reporting procedures [85](#reference-time-information-reporting-procedures)

8.12.1 Reference Time Information Reporting Control [85](#reference-time-information-reporting-control)

8.12.1.1 General [85](#general-41)

8.12.1.2 Successful Operation [85](#successful-operation-39)

8.12.1.3 Abnormal Conditions [86](#abnormal-conditions-38)

8.12.2 Reference Time Information Report [86](#reference-time-information-report)

8.12.2.1 General [86](#general-42)

8.12.2.2 Successful Operation [86](#successful-operation-40)

8.12.2.3 Abnormal Conditions [86](#abnormal-conditions-39)

8.13 Positioning Procedures [87](#positioning-procedures)

8.13.1 Positioning Assistance Information Control [87](#positioning-assistance-information-control)

8.13.1.1 General [87](#general-43)

8.13.1.2 Successful Operation [87](#successful-operation-41)

8.13.1.3 Abnormal Conditions [87](#abnormal-conditions-40)

8.13.2 Positioning Assistance Information Feedback [88](#positioning-assistance-information-feedback)

8.13.2.1 General [88](#general-44)

8.13.2.2 Successful Operation [88](#successful-operation-42)

8.13.2.3 Abnormal Conditions [88](#abnormal-conditions-41)

8.13.3 Positioning Measurement [88](#positioning-measurement)

8.13.3.1 General [88](#general-45)

8.13.3.2 Successful Operation [88](#successful-operation-43)

8.13.3.3 Unsuccessful Operation [89](#unsuccessful-operation-11)

8.13.3.4 Abnormal Conditions [90](#abnormal-conditions-42)

8.13.4 Positioning Measurement Report [90](#positioning-measurement-report)

8.13.4.1 General [90](#general-46)

8.13.4.2 Successful Operation [90](#successful-operation-44)

8.13.4.3 Unsuccessful Operation [90](#unsuccessful-operation-12)

8.13.4.4 Abnormal Conditions [90](#abnormal-conditions-43)

8.13.5 Positioning Measurement Abort [90](#positioning-measurement-abort)

8.13.5.1 General [90](#general-47)

8.13.5.2 Successful Operation [91](#successful-operation-45)

8.13.5.3 Unsuccessful Operation [91](#unsuccessful-operation-13)

8.13.5.4 Abnormal Conditions [91](#abnormal-conditions-44)

8.13.6 Positioning Measurement Failure Indication [91](#positioning-measurement-failure-indication)

8.13.6.1 General [91](#general-48)

8.13.6.2 Successful Operation [91](#successful-operation-46)

8.13.6.3 Unsuccessful Operation [91](#unsuccessful-operation-14)

8.13.6.4 Abnormal Conditions [92](#abnormal-conditions-45)

8.13.7 Positioning Measurement Update [92](#positioning-measurement-update)

8.13.7.1 General [92](#general-49)

8.13.7.2 Successful Operation [92](#successful-operation-47)

8.13.7.3 Unsuccessful Operation [92](#unsuccessful-operation-15)

8.13.7.4 Abnormal Conditions [92](#abnormal-conditions-46)

8.13.8 TRP Information Exchange [92](#trp-information-exchange)

8.13.8.1 General [92](#general-50)

8.13.8.2 Successful Operation [93](#successful-operation-48)

8.13.8.3 Unsuccessful Operation [93](#unsuccessful-operation-16)

8.13.9 Positioning Information Exchange [94](#positioning-information-exchange)

8.13.9.1 General [94](#general-51)

8.13.9.2 Successful Operation [94](#successful-operation-49)

8.13.9.3 Unsuccessful Operation [95](#unsuccessful-operation-17)

8.13.10 Positioning Activation [95](#positioning-activation)

8.13.10.1 General [95](#general-52)

8.13.10.2 Successful Operation [95](#successful-operation-50)

8.13.10.3 Unsuccessful Operation [96](#unsuccessful-operation-18)

8.13.10.4 Abnormal Conditions [96](#abnormal-conditions-47)

8.13.11 Positioning Deactivation [96](#positioning-deactivation)

8.13.11.1 General [96](#general-53)

8.13.11.2 Successful Operation [96](#successful-operation-51)

8.13.11.3 Unsuccessful Operation [96](#unsuccessful-operation-19)

8.13.11.4 Abnormal Conditions [96](#abnormal-conditions-48)

8.13.12 E-CID Measurement Initiation [97](#e-cid-measurement-initiation)

8.13.12.1 General [97](#general-54)

8.13.12.2 Successful Operation [97](#successful-operation-52)

8.13.12.3 Unsuccessful Operation [97](#unsuccessful-operation-20)

8.13.13 E-CID Measurement Failure Indication [98](#e-cid-measurement-failure-indication)

8.13.13.1 General [98](#general-55)

8.13.13.2 Successful Operation [98](#successful-operation-53)

8.13.13.3 Unsuccessful Operation [98](#unsuccessful-operation-21)

8.13.14 E-CID Measurement Report [98](#e-cid-measurement-report)

8.13.14.1 General [98](#general-56)

8.13.14.2 Successful Operation [98](#successful-operation-54)

8.13.14.3 Unsuccessful Operation [99](#unsuccessful-operation-22)

8.13.15 E-CID Measurement Termination [99](#e-cid-measurement-termination)

8.13.15.1 General [99](#general-57)

8.13.15.2 Successful Operation [99](#successful-operation-55)

8.13.15.3 Unsuccessful Operation [99](#unsuccessful-operation-23)

8.13.16 Positioning Information Update [99](#positioning-information-update)

8.13.16.1 General [99](#general-58)

8.13.16.2 Successful Operation [99](#successful-operation-56)

8.13.16.3 Unsuccessful Operation [100](#unsuccessful-operation-24)

8.13.16.4 Abnormal Conditions [100](#abnormal-conditions-49)

8.13.17 PRS Configuration Exchange [100](#prs-configuration-exchange)

8.13.17.1 General [100](#general-59)

8.13.17.2 Successful Operation [100](#successful-operation-57)

8.13.17.3 Unsuccessful Operation [101](#unsuccessful-operation-25)

8.13.17.4 Abnormal Conditions [101](#abnormal-conditions-50)

8.13.18 Measurement Preconfiguration [101](#measurement-preconfiguration)

8.13.18.1 General [101](#general-60)

8.13.18.2 Successful Operation [101](#successful-operation-58)

8.13.18.3 Unsuccessful Operation [102](#unsuccessful-operation-26)

8.13.19 Measurement Activation [102](#measurement-activation)

8.13.19.1 General [102](#general-61)

8.13.19.2 Successful Operation [102](#successful-operation-59)

8.13.19.3 Unsuccessful Operation [102](#unsuccessful-operation-27)

8.14 NR MBS Procedures [102](#nr-mbs-procedures)

8.14.1 Broadcast Context Setup [102](#broadcast-context-setup)

8.14.1.1 General [102](#general-62)

8.14.1.2 Successful Operation [103](#successful-operation-60)

8.14.1.3 Unsuccessful Operation [103](#unsuccessful-operation-28)

8.14.1.4 Abnormal Conditions [103](#abnormal-conditions-51)

8.14.2 Broadcast Context Release [104](#broadcast-context-release)

8.14.2.1 General [104](#general-63)

8.14.2.2 Successful Operation [104](#successful-operation-61)

8.14.2.3 Unsuccessful Operation [104](#unsuccessful-operation-29)

8.14.2.4 Abnormal Conditions [104](#abnormal-conditions-52)

8.14.3 Broadcast Context Release Request [104](#broadcast-context-release-request)

8.14.3.1 General [104](#general-64)

8.14.3.2 Successful Operation [105](#successful-operation-62)

8.14.3.3 Unsuccessful Operation [105](#unsuccessful-operation-30)

8.14.3.4 Abnormal Conditions [105](#abnormal-conditions-53)

8.14.4 Broadcast Context Modification [105](#broadcast-context-modification)

8.14.4.1 General [105](#general-65)

8.14.4.2 Successful Operation [105](#successful-operation-63)

8.14.4.3 Unsuccessful Operation [106](#unsuccessful-operation-31)

8.14.4.4 Abnormal Conditions [106](#abnormal-conditions-54)

8.14.5 Multicast Group Paging [107](#multicast-group-paging)

8.14.5.1 General [107](#general-66)

8.14.5.2 Successful Operation [107](#successful-operation-64)

8.14.5.3 Abnormal Conditions [107](#abnormal-conditions-55)

8.14.6 Multicast Context Setup [107](#multicast-context-setup)

8.14.6.1 General [107](#general-67)

8.14.6.2 Successful Operation [107](#successful-operation-65)

8.14.6.3 Unsuccessful Operation [108](#unsuccessful-operation-32)

8.14.6.4 Abnormal Conditions [108](#abnormal-conditions-56)

8.14.7 Multicast Context Release [108](#multicast-context-release)

8.14.7.1 General [108](#general-68)

8.14.7.2 Successful Operation [109](#successful-operation-66)

8.14.7.3 Unsuccessful Operation [109](#unsuccessful-operation-33)

8.14.7.4 Abnormal Conditions [109](#abnormal-conditions-57)

8.14.8 Multicast Context Release Request [109](#multicast-context-release-request)

8.14.8.1 General [109](#general-69)

8.14.8.2 Successful Operation [109](#successful-operation-67)

8.14.8.3 Unsuccessful Operation [110](#unsuccessful-operation-34)

8.14.8.4 Abnormal Conditions [110](#abnormal-conditions-58)

8.14.9 Multicast Context Modification [110](#multicast-context-modification)

8.14.9.1 General [110](#general-70)

8.14.9.2 Successful Operation [110](#successful-operation-68)

8.14.9.3 Unsuccessful Operation [111](#unsuccessful-operation-35)

8.14.9.4 Abnormal Conditions [111](#abnormal-conditions-59)

8.14.10 Multicast Distribution Setup [111](#multicast-distribution-setup)

8.14.10.1 General [111](#general-71)

8.14.10.2 Successful Operation [111](#successful-operation-69)

8.14.10.3 Unsuccessful Operation [112](#unsuccessful-operation-36)

8.14.10.4 Abnormal Conditions [112](#abnormal-conditions-60)

8.14.11 Multicast Distribution Release [112](#multicast-distribution-release)

8.14.11.1 General [112](#general-72)

8.14.11.2 Successful Operation [112](#successful-operation-70)

8.14.11.3 Unsuccessful Operation [113](#unsuccessful-operation-37)

8.14.11.4 Abnormal Conditions [113](#abnormal-conditions-61)

8.15 PDC Measurement Reporting procedures [113](#pdc-measurement-reporting-procedures)

8.15.1 PDC Measurement Initiation [113](#pdc-measurement-initiation)

8.15.1.1 General [113](#general-73)

8.15.1.2 Successful Operation [113](#successful-operation-71)

8.15.1.3 Unsuccessful Operation [114](#unsuccessful-operation-38)

8.15.2 PDC Measurement Report [114](#pdc-measurement-report)

8.15.2.1 General [114](#general-74)

8.15.2.2 Successful Operation [114](#successful-operation-72)

8.15.2.3 Unsuccessful Operation [114](#unsuccessful-operation-39)

8.16 QoE Procedures [114](#qoe-procedures)

8.16.1 QoE Information Transfer [114](#qoe-information-transfer)

8.16.1.1 General [114](#general-75)

8.16.1.2 Successful operation [115](#successful-operation-73)

8.16.1.3 Abnormal Conditions [115](#abnormal-conditions-62)

9 Elements for F1AP Communication [115](#elements-for-f1ap-communication)

9.1 General [115](#general-76)

9.2 Message Functional Definition and Content [115](#message-functional-definition-and-content)

9.2.1 Interface Management messages [115](#interface-management-messages)

9.2.1.1 RESET [115](#reset-1)

9.2.1.2 RESET ACKNOWLEDGE [116](#reset-acknowledge)

9.2.1.3 ERROR INDICATION [116](#error-indication-1)

9.2.1.4 F1 SETUP REQUEST [117](#f1-setup-request)

9.2.1.5 F1 SETUP RESPONSE [118](#f1-setup-response)

9.2.1.6 F1 SETUP FAILURE [120](#f1-setup-failure)

9.2.1.7 GNB-DU CONFIGURATION UPDATE [120](#gnb-du-configuration-update-1)

9.2.1.8 GNB-DU CONFIGURATION UPDATE ACKNOWLEDGE [122](#gnb-du-configuration-update-acknowledge)

9.2.1.9 GNB-DU CONFIGURATION UPDATE FAILURE [123](#gnb-du-configuration-update-failure)

9.2.1.10 GNB-CU CONFIGURATION UPDATE [123](#gnb-cu-configuration-update-1)

9.2.1.11 GNB-CU CONFIGURATION UPDATE ACKNOWLEDGE [127](#gnb-cu-configuration-update-acknowledge)

9.2.1.12 GNB-CU CONFIGURATION UPDATE FAILURE [128](#gnb-cu-configuration-update-failure)

9.2.1.13 GNB-DU RESOURCE COORDINATION REQUEST [128](#gnb-du-resource-coordination-request)

9.2.1.14 GNB-DU RESOURCE COORDINATION RESPONSE [128](#gnb-du-resource-coordination-response)

9.2.1.15 GNB-DU STATUS INDICATION [129](#gnb-du-status-indication-1)

9.2.1.16 F1 REMOVAL REQUEST [129](#f1-removal-request)

9.2.1.17 F1 REMOVAL RESPONSE [129](#f1-removal-response)

9.2.1.18 F1 REMOVAL FAILURE [130](#f1-removal-failure)

9.2.1.19 NETWORK ACCESS RATE REDUCTION [130](#network-access-rate-reduction-1)

9.2.1.20 RESOURCE STATUS REQUEST [130](#resource-status-request)

9.2.1.21 RESOURCE STATUS RESPONSE [132](#resource-status-response)

9.2.1.22 RESOURCE STATUS FAILURE [132](#resource-status-failure)

9.2.1.23 RESOURCE STATUS UPDATE [133](#resource-status-update)

9.2.2 UE Context Management messages [135](#ue-context-management-messages)

9.2.2.1 UE CONTEXT SETUP REQUEST [135](#ue-context-setup-request)

9.2.2.2 UE CONTEXT SETUP RESPONSE [142](#ue-context-setup-response)

9.2.2.3 UE CONTEXT SETUP FAILURE [146](#ue-context-setup-failure)

9.2.2.4 UE CONTEXT RELEASE REQUEST [146](#ue-context-release-request)

9.2.2.5 UE CONTEXT RELEASE COMMAND [147](#ue-context-release-command)

9.2.2.6 UE CONTEXT RELEASE COMPLETE [148](#ue-context-release-complete)

9.2.2.7 UE CONTEXT MODIFICATION REQUEST [149](#ue-context-modification-request)

9.2.2.8 UE CONTEXT MODIFICATION RESPONSE [160](#ue-context-modification-response)

9.2.2.9 UE CONTEXT MODIFICATION FAILURE [166](#ue-context-modification-failure)

9.2.2.10 UE CONTEXT MODIFICATION REQUIRED [166](#ue-context-modification-required)

9.2.2.11 UE CONTEXT MODIFICATION CONFIRM [169](#ue-context-modification-confirm)

9.2.2.11A UE CONTEXT MODIFICATION REFUSE [171](#a-ue-context-modification-refuse)

9.2.2.12 UE INACTIVITY NOTIFICATION [171](#ue-inactivity-notification-1)

9.2.2.13 NOTIFY [172](#notify-1)

9.2.2.14 ACCESS SUCCESS [172](#access-success-1)

9.2.3 RRC Message Transfer messages [173](#rrc-message-transfer-messages)

9.2.3.1 INITIAL UL RRC MESSAGE TRANSFER [173](#initial-ul-rrc-message-transfer-1)

9.2.3.2 DL RRC MESSAGE TRANSFER [174](#dl-rrc-message-transfer-1)

9.2.3.3 UL RRC MESSAGE TRANSFER [175](#ul-rrc-message-transfer-1)

9.2.3.4 RRC DELIVERY REPORT [175](#rrc-delivery-report-1)

9.2.4 Warning Message Transmission Messages [175](#warning-message-transmission-messages)

9.2.4.1 WRITE-REPLACE WARNING REQUEST [175](#write-replace-warning-request)

9.2.4.2 WRITE-REPLACE WARNING RESPONSE [176](#write-replace-warning-response)

9.2.4.3 PWS CANCEL REQUEST [177](#pws-cancel-request)

9.2.4.4 PWS CANCEL RESPONSE [178](#pws-cancel-response)

9.2.4.5 PWS RESTART INDICATION [179](#pws-restart-indication-1)

9.2.4.6 PWS FAILURE INDICATION [180](#pws-failure-indication-1)

9.2.5 System Information messages [180](#system-information-messages)

9.2.5.1 SYSTEM INFORMATION DELIVERY COMMAND [180](#system-information-delivery-command)

9.2.6 Paging messages [180](#paging-messages)

9.2.6.1 PAGING [180](#paging-1)

9.2.7 Trace Messages [181](#trace-messages)

9.2.7.1 TRACE START [181](#trace-start-1)

9.2.7.2 DEACTIVATE TRACE [182](#deactivate-trace-1)

9.2.7.3 CELL TRAFFIC TRACE [182](#cell-traffic-trace-1)

9.2.8 Radio Information Transfer messages [183](#radio-information-transfer-messages)

9.2.8.1 DU-CU RADIO INFORMATION TRANSFER [183](#du-cu-radio-information-transfer-1)

9.2.8.2 CU-DU RADIO INFORMATION TRANSFER [183](#cu-du-radio-information-transfer-1)

9.2.9 IAB messages [184](#iab-messages)

9.2.9.1 BAP MAPPING CONFIGURATION [184](#bap-mapping-configuration-1)

9.2.9.2 BAP MAPPING CONFIGURATION ACKNOWLEDGE [186](#bap-mapping-configuration-acknowledge)

9.2.9.2A BAP MAPPING CONFIGURATION FAILURE [186](#a-bap-mapping-configuration-failure)

9.2.9.3 GNB-DU RESOURCE CONFIGURATION [186](#gnb-du-resource-configuration-1)

9.2.9.4 GNB-DU RESOURCE CONFIGURATION ACKNOWLEDGE [194](#gnb-du-resource-configuration-acknowledge)

9.2.9.4A GNB-DU RESOURCE CONFIGURATION FAILURE [194](#a-gnb-du-resource-configuration-failure)

9.2.9.5 IAB TNL ADDRESS REQUEST [194](#iab-tnl-address-request)

9.2.9.6 IAB TNL ADDRESS RESPONSE [195](#iab-tnl-address-response)

9.2.9.6A IAB TNL ADDRESS FAILURE [196](#a-iab-tnl-address-failure)

9.2.9.7 IAB UP CONFIGURATION UPDATE REQUEST [196](#iab-up-configuration-update-request)

9.2.9.8 IAB UP CONFIGURATION UPDATE RESPONSE [197](#iab-up-configuration-update-response)

9.2.9.9 IAB UP CONFIGURATION UPDATE FAILURE [198](#iab-up-configuration-update-failure)

9.2.10 Self Optimisation Support Messages [198](#self-optimisation-support-messages)

9.2.10.1 ACCESS AND MOBILITY INDICATION [198](#access-and-mobility-indication-1)

9.2.11 Reference Time Information Reporting messages [199](#reference-time-information-reporting-messages)

9.2.11.1 REFERENCE TIME INFORMATION REPORTING CONTROL [199](#reference-time-information-reporting-control-1)

9.2.11.2 REFERENCE TIME INFORMATION REPORT [200](#reference-time-information-report-1)

9.2.12 Messages for Positioning Procedures [200](#messages-for-positioning-procedures)

9.2.12.1 POSITIONING ASSISTANCE INFORMATION CONTROL [200](#positioning-assistance-information-control-1)

9.2.12.2 POSITIONING ASSISTANCE INFORMATION FEEDBACK [200](#positioning-assistance-information-feedback-1)

9.2.12.3 POSITIONING MEASUREMENT REQUEST [201](#positioning-measurement-request)

9.2.12.4 POSITIONING MEASUREMENT RESPONSE [203](#positioning-measurement-response)

9.2.12.5 POSITIONING MEASUREMENT FAILURE [204](#positioning-measurement-failure)

9.2.12.6 POSITIONING MEASUREMENT REPORT [204](#positioning-measurement-report-1)

9.2.12.7 POSITIONING MEASUREMENT ABORT [205](#positioning-measurement-abort-1)

9.2.12.8 POSITIONING MEASUREMENT FAILURE INDICATION [205](#positioning-measurement-failure-indication-1)

9.2.12.9 POSITIONING MEASUREMENT UPDATE [206](#positioning-measurement-update-1)

9.2.12.10 TRP INFORMATION REQUEST [206](#trp-information-request)

9.2.12.11 TRP INFORMATION RESPONSE [207](#trp-information-response)

9.2.12.12 TRP INFORMATION FAILURE [207](#trp-information-failure)

9.2.12.13 POSITIONING INFORMATION REQUEST [207](#positioning-information-request)

9.2.12.14 POSITIONING INFORMATION RESPONSE [208](#positioning-information-response)

9.2.12.15 POSITIONING INFORMATION FAILURE [208](#positioning-information-failure)

9.2.12.16 POSITIONING ACTIVATION REQUEST [208](#positioning-activation-request)

9.2.12.17 POSITIONING ACTIVATION RESPONSE [209](#positioning-activation-response)

9.2.12.18 POSITIONING ACTIVATION FAILURE [209](#positioning-activation-failure)

9.2.12.19 POSITIONING DEACTIVATION [210](#positioning-deactivation-1)

9.2.12.20 E-CID MEASUREMENT INITIATION REQUEST [210](#e-cid-measurement-initiation-request)

9.2.12.21 E-CID MEASUREMENT INITIATION RESPONSE [211](#e-cid-measurement-initiation-response)

9.2.12.22 E-CID MEASUREMENT INITIATION FAILURE [211](#e-cid-measurement-initiation-failure)

9.2.12.23 E-CID MEASUREMENT FAILURE INDICATION [211](#e-cid-measurement-failure-indication-1)

9.2.12.24 E-CID MEASUREMENT REPORT [211](#e-cid-measurement-report-1)

9.2.12.25 E-CID MEASUREMENT TERMINATION COMMAND [212](#e-cid-measurement-termination-command)

9.2.12.26 POSITIONING INFORMATION UPDATE [212](#positioning-information-update-1)

9.2.12.27 PRS CONFIGURATION REQUEST [212](#prs-configuration-request)

9.2.12.28 PRS CONFIGURATION RESPONSE [213](#prs-configuration-response)

9.2.12.29 PRS CONFIGURATION FAILURE [213](#prs-configuration-failure)

9.2.12.30 MEASUREMENT PRECONFIGURATION REQUIRED [214](#measurement-preconfiguration-required)

9.2.12.31 MEASUREMENT PRECONFIGURATION CONFIRM [214](#measurement-preconfiguration-confirm)

9.2.12.32 MEASUREMENT PRECONFIGURATION REFUSE [214](#measurement-preconfiguration-refuse)

9.2.12.33 MEASUREMENT ACTIVATION [215](#measurement-activation-1)

9.2.13 Broadcast Context Management messages [215](#broadcast-context-management-messages)

9.2.13.1 BROADCAST CONTEXT SETUP REQUEST [215](#broadcast-context-setup-request)

9.2.13.2 BROADCAST CONTEXT SETUP RESPONSE [216](#broadcast-context-setup-response)

9.2.13.3 BROADCAST CONTEXT SETUP FAILURE [217](#broadcast-context-setup-failure)

9.2.13.4 BROADCAST CONTEXT RELEASE COMMAND [217](#broadcast-context-release-command)

9.2.13.5 BROADCAST CONTEXT RELEASE COMPLETE [218](#broadcast-context-release-complete)

9.2.13.5a BROADCAST CONTEXT RELEASE REQUEST [218](#a-broadcast-context-release-request)

9.2.13.6 BROADCAST CONTEXT MODIFICATION REQUEST [218](#broadcast-context-modification-request)

9.2.13.7 BROADCAST CONTEXT MODIFICATION RESPONSE [220](#broadcast-context-modification-response)

9.2.13.8 BROADCAST CONTEXT MODIFICATION FAILURE [221](#broadcast-context-modification-failure)

9.2.14 Multicast Context Management messages [221](#multicast-context-management-messages)

9.2.14.1 MULTICAST GROUP PAGING [221](#multicast-group-paging-1)

9.2.14.2 MULTICAST CONTEXT SETUP REQUEST [221](#multicast-context-setup-request)

9.2.14.3 MULTICAST CONTEXT SETUP RESPONSE [222](#multicast-context-setup-response)

9.2.14.4 MULTICAST CONTEXT SETUP FAILURE [223](#multicast-context-setup-failure)

9.2.14.5 MULTICAST CONTEXT RELEASE COMMAND [223](#multicast-context-release-command)

9.2.14.6 MULTICAST CONTEXT RELEASE COMPLETE [223](#multicast-context-release-complete)

9.2.14.6a MULTICAST CONTEXT RELEASE REQUEST [223](#a-multicast-context-release-request)

9.2.14.7 MULTICAST CONTEXT MODIFICATION REQUEST [224](#multicast-context-modification-request)

9.2.14.8 MULTICAST CONTEXT MODIFICATION RESPONSE [224](#multicast-context-modification-response)

9.2.14.9 MULTICAST CONTEXT MODIFICATION FAILURE [225](#multicast-context-modification-failure)

9.2.14.10 MULTICAST DISTRIBUTION SETUP REQUEST [225](#multicast-distribution-setup-request)

9.2.14.11 MULTICAST DISTRIBUTION SETUP RESPONSE [226](#multicast-distribution-setup-response)

9.2.14.12 MULTICAST DISTRIBUTION SETUP FAILURE [227](#multicast-distribution-setup-failure)

9.2.14.13 MULTICAST DISTRIBUTION RELEASE COMMAND [227](#multicast-distribution-release-command)

9.2.14.14 MULTICAST DISTRIBUTION RELEASE COMPLETE [227](#multicast-distribution-release-complete)

9.2.15 PDC Measurement Reporting messages [227](#pdc-measurement-reporting-messages)

9.2.15.1 PDC MEASUREMENT INITIATION REQUEST [227](#pdc-measurement-initiation-request)

9.2.15.2 PDC MEASUREMENT INITIATION RESPONSE [228](#pdc-measurement-initiation-response)

9.2.15.3 PDC MEASUREMENT INITIATION FAILURE [228](#pdc-measurement-initiation-failure)

9.2.15.4 PDC MEASUREMENT REPORT [229](#pdc-measurement-report-1)

9.2.16 QoE Information Transfer messages [229](#qoe-information-transfer-messages)

9.2.16.1 QOE INFORMATION TRANSFER [229](#qoe-information-transfer-1)

9.3 Information Element Definitions [229](#information-element-definitions)

9.3.1 Radio Network Layer Related IEs [229](#radio-network-layer-related-ies)

9.3.1.1 Message Type [229](#message-type)

9.3.1.2 Cause [230](#cause)

9.3.1.3 Criticality Diagnostics [233](#criticality-diagnostics)

9.3.1.4 gNB-CU UE F1AP ID [234](#gnb-cu-ue-f1ap-id)

9.3.1.5 gNB-DU UE F1AP ID [234](#gnb-du-ue-f1ap-id)

9.3.1.6 RRC-Container [235](#rrc-container)

9.3.1.7 SRB ID [235](#srb-id)

9.3.1.8 DRB ID [235](#drb-id)

9.3.1.9 gNB-DU ID [235](#gnb-du-id)

9.3.1.10 Served Cell Information [235](#served-cell-information)

9.3.1.11 Transmission Action Indicator [240](#transmission-action-indicator)

9.3.1.12 NR CGI [240](#nr-cgi)

9.3.1.13 Time To wait [240](#time-to-wait)

9.3.1.14 PLMN Identity [240](#plmn-identity)

9.3.1.15 Transmission Bandwidth [240](#transmission-bandwidth)

9.3.1.16 Void [241](#void)

9.3.1.17 NR Frequency Info [241](#nr-frequency-info)

9.3.1.18 gNB-DU System Information [243](#gnb-du-system-information)

9.3.1.19 E-UTRAN QoS [243](#e-utran-qos)

9.3.1.20 Allocation and Retention Priority [244](#allocation-and-retention-priority)

9.3.1.21 GBR QoS Information [245](#gbr-qos-information)

9.3.1.22 Bit Rate [246](#bit-rate)

9.3.1.23 Transaction ID [246](#transaction-id)

9.3.1.24 DRX Cycle [246](#drx-cycle)

9.3.1.25 CU to DU RRC Information [246](#cu-to-du-rrc-information)

9.3.1.26 DU to CU RRC Information [247](#du-to-cu-rrc-information)

9.3.1.27 RLC Mode [249](#rlc-mode)

9.3.1.28 SUL Information [249](#sul-information)

9.3.1.29 5GS TAC [250](#gs-tac)

9.3.1.29a Configured EPS TAC [250](#a-configured-eps-tac)

9.3.1.30 RRC Reconfiguration Complete Indicator [250](#rrc-reconfiguration-complete-indicator)

9.3.1.31 UL Configuration [251](#ul-configuration)

9.3.1.32 C-RNTI [251](#c-rnti)

9.3.1.33 Cell UL Configured [251](#cell-ul-configured)

9.3.1.34 RAT-Frequency Priority Information [251](#rat-frequency-priority-information)

9.3.1.35 LCID [252](#lcid)

9.3.1.36 Duplication activation [252](#duplication-activation)

9.3.1.37 Slice Support List [252](#slice-support-list)

9.3.1.38 S-NSSAI [252](#s-nssai)

9.3.1.39 UE Identity Index value [252](#ue-identity-index-value)

9.3.1.40 Paging DRX [253](#paging-drx)

9.3.1.41 Paging Priority [253](#paging-priority)

9.3.1.42 gNB-CU System Information [253](#gnb-cu-system-information)

9.3.1.43 RAN UE Paging identity [254](#ran-ue-paging-identity)

9.3.1.44 CN UE Paging Identity [254](#cn-ue-paging-identity)

9.3.1.45 QoS Flow Level QoS Parameters [254](#qos-flow-level-qos-parameters)

9.3.1.46 GBR QoS Flow Information [255](#gbr-qos-flow-information)

9.3.1.47 Dynamic 5QI Descriptor [256](#dynamic-5qi-descriptor)

9.3.1.48 NG-RAN Allocation and Retention Priority [258](#ng-ran-allocation-and-retention-priority)

9.3.1.49 Non Dynamic 5QI Descriptor [259](#non-dynamic-5qi-descriptor)

9.3.1.50 Maximum Packet Loss Rate [260](#maximum-packet-loss-rate)

9.3.1.51 Packet Delay Budget [261](#packet-delay-budget)

9.3.1.52 Packet Error Rate [261](#packet-error-rate)

9.3.1.53 Averaging Window [261](#averaging-window)

9.3.1.54 Maximum Data Burst Volume [261](#maximum-data-burst-volume)

9.3.1.55 Masked IMEISV [261](#masked-imeisv)

9.3.1.56 Notification Control [261](#notification-control)

9.3.1.57 RAN Area Code [262](#ran-area-code)

9.3.1.58 PWS System Information [262](#pws-system-information)

9.3.1.59 Repetition Period [262](#repetition-period)

9.3.1.60 Number of Broadcasts Requested [262](#number-of-broadcasts-requested)

9.3.1.61 Void [263](#void-1)

9.3.1.62 SIType List [263](#sitype-list)

9.3.1.63 QoS Flow Identifier [263](#qos-flow-identifier)

9.3.1.64 Served E-UTRA Cell Information [263](#served-e-utra-cell-information)

9.3.1.65 Available PLMN List [263](#available-plmn-list)

9.3.1.66 RLC Failure Indication [264](#rlc-failure-indication)

9.3.1.67 Uplink TxDirectCurrentList Information [264](#uplink-txdirectcurrentlist-information)

9.3.1.68 Service Status [264](#service-status)

9.3.1.69 RLC Status [264](#rlc-status)

9.3.1.70 RRC Version [265](#rrc-version)

9.3.1.71 RRC Delivery Status [265](#rrc-delivery-status)

9.3.1.72 QoS Flow Mapping Indication [265](#qos-flow-mapping-indication)

9.3.1.73 Resource Coordination Transfer Information [265](#resource-coordination-transfer-information)

9.3.1.74 E-UTRA PRACH Configuration [265](#e-utra-prach-configuration)

9.3.1.75 Resource Coordination E-UTRA Cell Information [266](#resource-coordination-e-utra-cell-information)

9.3.1.76 Extended Available PLMN List [268](#extended-available-plmn-list)

9.3.1.77 Associated SCell List [268](#associated-scell-list)

9.3.1.78 Cell Direction [268](#cell-direction)

9.3.1.79 Paging Origin [268](#paging-origin)

9.3.1.80 E-UTRA Transmission Bandwidth [268](#e-utra-transmission-bandwidth)

9.3.1.81 Message Identifier [269](#message-identifier)

9.3.1.82 Serial Number [269](#serial-number)

9.3.1.83 UAC Assistance Information [270](#uac-assistance-information)

9.3.1.84 UAC Action [270](#uac-action)

9.3.1.85 UAC reduction Indication [271](#uac-reduction-indication)

9.3.1.86 Additional SIB Message List [271](#additional-sib-message-list)

9.3.1.87 Cell Type [271](#cell-type)

9.3.1.87a Configured TAC Indication [272](#a-configured-tac-indication)

9.3.1.88 Trace Activation [272](#trace-activation)

9.3.1.89 Intended TDD DL-UL Configuration [274](#intended-tdd-dl-ul-configuration)

9.3.1.90 Additional RRM Policy Index [276](#additional-rrm-policy-index)

9.3.1.91 DU-CU RIM Information [276](#du-cu-rim-information)

9.3.1.92 CU-DU RIM Information [276](#cu-du-rim-information)

9.3.1.93 gNB Set ID [277](#gnb-set-id)

9.3.1.94 Lower Layer Presence Status Change [277](#lower-layer-presence-status-change)

9.3.1.95 Traffic Mapping Information [277](#traffic-mapping-information)

9.3.1.96 IP-to-layer-2 traffic mapping Information List [277](#__RefHeading___Toc99731038)

9.3.1.97 IP Header Information [278](#ip-header-information)

9.3.1.98 BAP layer BH RLC channel mapping Information List [278](#bap-layer-bh-rlc-channel-mapping-information-list)

9.3.1.99 Mapping Information to Remove [279](#mapping-information-to-remove)

9.3.1.100 Mapping Information Index [279](#mapping-information-index)

9.3.1.101 IAB TNL Addresses Requested [280](#iab-tnl-addresses-requested)

9.3.1.102 IAB TNL Address [280](#iab-tnl-address)

9.3.1.103 Uplink BH Non-UP Traffic Mapping [280](#uplink-bh-non-up-traffic-mapping)

9.3.1.104 Non-UP Traffic Type [281](#non-up-traffic-type)

9.3.1.105 IAB Info IAB-donor-CU [281](#iab-info-iab-donor-cu)

9.3.1.106 IAB Info IAB-DU [281](#iab-info-iab-du)

9.3.1.107 gNB-DU Cell Resource Configuration [281](#gnb-du-cell-resource-configuration)

9.3.1.108 Multiplexing Info [284](#multiplexing-info)

9.3.1.109 IAB STC Info [285](#iab-stc-info)

9.3.1.110 BAP Routing ID [286](#bap-routing-id)

9.3.1.111 BAP Address [286](#bap-address)

9.3.1.112 BAP Path ID [287](#bap-path-id)

9.3.1.113 BH RLC Channel ID [287](#bh-rlc-channel-id)

9.3.1.114 BH Information [287](#__RefHeading___Toc99731056)

9.3.1.115 Control Plane Traffic Type [288](#control-plane-traffic-type)

9.3.1.116 NR V2X Services Authorized [289](#nr-v2x-services-authorized)

9.3.1.117 LTE V2X Services Authorized [289](#lte-v2x-services-authorized)

9.3.1.118 LTE UE Sidelink Aggregate Maximum Bit Rate [289](#lte-ue-sidelink-aggregate-maximum-bit-rate)

9.3.1.119 NR UE Sidelink Aggregate Maximum Bit Rate [289](#nr-ue-sidelink-aggregate-maximum-bit-rate)

9.3.1.120 SL DRB ID [289](#sl-drb-id)

9.3.1.121 PC5 QoS Flow Identifier [289](#pc5-qos-flow-identifier)

9.3.1.122 PC5 QoS Parameters [290](#pc5-qos-parameters)

9.3.1.123 Alternative QoS Parameters Set Index [290](#alternative-qos-parameters-set-index)

9.3.1.124 Alternative QoS Parameters Set Notify Index [291](#alternative-qos-parameters-set-notify-index)

9.3.1.125 Alternative QoS Parameters Set List [291](#alternative-qos-parameters-set-list)

9.3.1.126 Non Dynamic PQI Descriptor [291](#non-dynamic-pqi-descriptor)

9.3.1.127 Dynamic PQI Descriptor [292](#dynamic-pqi-descriptor)

9.3.1.128 TNL Capacity Indicator [292](#tnl-capacity-indicator)

9.3.1.129 Radio Resource Status [292](#radio-resource-status)

9.3.1.130 Composite Available Capacity Group [294](#composite-available-capacity-group)

9.3.1.131 Composite Available Capacity [295](#composite-available-capacity)

9.3.1.132 Cell Capacity Class Value [295](#cell-capacity-class-value)

9.3.1.133 Capacity Value [295](#capacity-value)

9.3.1.134 Slice Available Capacity [296](#slice-available-capacity)

9.3.1.135 Number of Active UEs [297](#number-of-active-ues)

9.3.1.136 Hardware Load Indicator [297](#hardware-load-indicator)

9.3.1.137 NR Carrier List [297](#nr-carrier-list)

9.3.1.138 SSB Positions In Burst [297](#ssb-positions-in-burst)

9.3.1.139 NR PRACH Configuration [298](#nr-prach-configuration)

9.3.1.140 NR PRACH Configuration List [298](#nr-prach-configuration-list)

9.3.1.141 TSC Traffic Characteristics [300](#tsc-traffic-characteristics)

9.3.1.142 TSC Assistance Information [300](#tsc-assistance-information)

9.3.1.143 Periodicity [300](#periodicity)

9.3.1.144 Burst Arrival Time [300](#burst-arrival-time)

9.3.1.145 Extended Packet Delay Budget [300](#extended-packet-delay-budget)

9.3.1.146 RLC Duplication Information [301](#rlc-duplication-information)

9.3.1.147 Reporting Request Type [301](#reporting-request-type)

9.3.1.148 Time Reference Information [301](#time-reference-information)

9.3.1.149 Reference Time [302](#reference-time)

9.3.1.150 MDT Configuration [302](#mdt-configuration)

9.3.1.151 MDT PLMN List [302](#mdt-plmn-list)

9.3.1.152 M5 Configuration [303](#m5-configuration)

9.3.1.153 M6 Configuration [303](#m6-configuration)

9.3.1.154 M7 Configuration [303](#m7-configuration)

9.3.1.155 NID [304](#nid)

9.3.1.156 NPN Support Information [304](#npn-support-information)

9.3.1.157 NPN Broadcast Information [304](#npn-broadcast-information)

9.3.1.158 Broadcast SNPN ID List [304](#broadcast-snpn-id-list)

9.3.1.159 Broadcast NID List [305](#broadcast-nid-list)

9.3.1.160 Broadcast CAG-Identifier List [305](#broadcast-cag-identifier-list)

9.3.1.161 CAG ID [305](#cag-id)

9.3.1.162 Broadcast PNI-NPN ID Information [305](#broadcast-pni-npn-id-information)

9.3.1.163 Available SNPN ID List [306](#available-snpn-id-list)

9.3.1.164 Void [306](#void-2)

9.3.1.165 Extended Slice Support List [306](#extended-slice-support-list)

9.3.1.166 Positioning Measurement Result [306](#positioning-measurement-result)

9.3.1.167 UL Angle of Arrival [307](#ul-angle-of-arrival)

9.3.1.168 UL RTOA Measurement [307](#ul-rtoa-measurement)

9.3.1.169 Additional Path List [308](#additional-path-list)

9.3.1.170 gNB Rx-Tx Time Difference [308](#gnb-rx-tx-time-difference)

9.3.1.171 Time Stamp [309](#time-stamp)

9.3.1.172 TRP Measurement Quality [309](#trp-measurement-quality)

9.3.1.173 Measurement Beam Information [309](#measurement-beam-information)

9.3.1.174 NG-RAN Access Point Position [310](#ng-ran-access-point-position)

9.3.1.175 Requested SRS Transmission Characteristics [310](#requested-srs-transmission-characteristics)

9.3.1.176 TRP Information [312](#trp-information)

9.3.1.177 PRS Configuration [313](#prs-configuration)

9.3.1.178 DL-PRS Muting Pattern [315](#dl-prs-muting-pattern)

9.3.1.179 Spatial Direction Information [315](#spatial-direction-information)

9.3.1.180 SRS Resource Set ID [315](#srs-resource-set-id)

9.3.1.181 Spatial Relation Information [315](#spatial-relation-information)

9.3.1.182 SRS Resource Trigger [316](#srs-resource-trigger)

9.3.1.183 Relative Time 1900 [316](#relative-time-1900)

9.3.1.184 Geographical Coordinates [317](#geographical-coordinates)

9.3.1.185 DL-PRS Resource Coordinates [318](#dl-prs-resource-coordinates)

9.3.1.186 Relative Geodetic Location [319](#relative-geodetic-location)

9.3.1.187 Relative Cartesian Location [320](#relative-cartesian-location)

9.3.1.188 Reference Point [320](#reference-point)

9.3.1.189 Location Uncertainty [321](#location-uncertainty)

9.3.1.190 NG-RAN High Accuracy Access Point Position [321](#ng-ran-high-accuracy-access-point-position)

9.3.1.191 Positioning Broadcast Cells [322](#positioning-broadcast-cells)

9.3.1.192 SRS Configuration [322](#srs-configuration)

9.3.1.193 SRS Resource [324](#srs-resource)

9.3.1.194 Positioning SRS Resource [324](#positioning-srs-resource)

9.3.1.195 SRS Resource Set [326](#srs-resource-set)

9.3.1.196 Positioning SRS Resource Set [326](#positioning-srs-resource-set)

9.3.1.197 TRP ID [326](#trp-id)

9.3.1.198 NR-PRS Beam Information [327](#nr-prs-beam-information)

9.3.1.199 E-CID Measurement Result [328](#e-cid-measurement-result)

9.3.1.200 Cell Portion ID [328](#cell-portion-id)

9.3.1.201 Pathloss Reference Information [328](#pathloss-reference-information)

9.3.1.202 SSB Information [329](#ssb-information)

9.3.1.203 SSB Time/Frequency Configuration [329](#ssb-timefrequency-configuration)

9.3.1.204 Search Window Information [330](#search-window-information)

9.3.1.205 Extended gNB-DU Name [331](#extended-gnb-du-name)

9.3.1.206 Extended gNB-CU Name [331](#extended-gnb-cu-name)

9.3.1.207 F1-C Transfer Path [331](#f1-c-transfer-path)

9.3.1.208 SFN Offset [331](#sfn-offset)

9.3.1.209 Transmission Stop Indicator [331](#transmission-stop-indicator)

9.3.1.210 Spatial Relation Information per SRS Resource [332](#spatial-relation-information-per-srs-resource)

9.3.1.211 CCO Assistance Information [332](#cco-assistance-information)

9.3.1.212 Affected Cells and Beams [332](#affected-cells-and-beams)

9.3.1.213 Coverage Modification Notification [333](#coverage-modification-notification)

9.3.1.214 Cells for SON List [333](#cells-for-son-list)

9.3.1.215 Neighbour NR Cells for SON List [334](#neighbour-nr-cells-for-son-list)

9.3.1.216 NR Mode Info Rel16 [334](#nr-mode-info-rel16)

9.3.1.217 Frequency Info Rel16 [334](#frequency-info-rel16)

9.3.1.218 MBS Session ID [335](#mbs-session-id)

9.3.1.219 gNB-CU MBS F1AP ID [335](#gnb-cu-mbs-f1ap-id)

9.3.1.220 gNB-DU MBS F1AP ID [335](#gnb-du-mbs-f1ap-id)

9.3.1.221 MBS Area Session ID [336](#mbs-area-session-id)

9.3.1.222 MBS Service Area [336](#mbs-service-area)

9.3.1.223 MBS Service Area information [336](#mbs-service-area-information)

9.3.1.224 MRB ID [336](#mrb-id)

9.3.1.225 MBS CU to DU RRC Information [337](#mbs-cu-to-du-rrc-information)

9.3.1.226 MBS Broadcast Neighbour Cell List [337](#mbs-broadcast-neighbour-cell-list)

9.3.1.227 IAB Congestion Indication [337](#iab-congestion-indication)

9.3.1.228 F1-C Transfer Path NRDC [338](#f1-c-transfer-path-nrdc)

9.3.1.229 IAB TNL Address Exception [338](#iab-tnl-address-exception)

9.3.1.230 RB Set Configuration [338](#rb-set-configuration)

9.3.1.231 Survival Time [339](#__RefHeading___Toc99731173)

9.3.1.232 PDC Measurement Result [339](#pdc-measurement-result)

9.3.1.233 SCG Activation Request [339](#scg-activation-request)

9.3.1.234 SCG Activation Status [339](#scg-activation-status)

9.3.1.235 Requested DL PRS Transmission Characteristics [339](#requested-dl-prs-transmission-characteristics)

9.3.1.236 Start Time and Duration [340](#start-time-and-duration)

9.3.1.237 PRS Transmission Off Information [340](#prs-transmission-off-information)

9.3.1.238 UL-AoA Assistance Information [341](#ul-aoa-assistance-information)

9.3.1.239 Zenith Angle of Arrival Information [342](#zenith-angle-of-arrival-information)

9.3.1.240 On-demand PRS TRP Information [343](#on-demand-prs-trp-information)

9.3.1.241 LCS to GCS Translation AoA [344](#lcs-to-gcs-translation-aoa)

9.3.1.242 Response Time [344](#response-time)

9.3.1.243 ARP Location Information [344](#arp-location-information)

9.3.1.244 ARP ID [345](#arp-id)

9.3.1.245 Multiple UL AoA [345](#multiple-ul-aoa)

9.3.1.246 UL SRS-RSRPP [345](#ul-srs-rsrpp)

9.3.1.247 SRS Resource type [346](#srs-resource-type)

9.3.1.248 Extended Additional Path List [346](#extended-additional-path-list)

9.3.1.249 LoS/NLoS Information [346](#losnlos-information)

9.3.1.250 Requested DL-PRS Resource List [347](#requested-dl-prs-resource-list)

9.3.1.251 UE Tx TEG Association [347](#ue-tx-teg-association)

9.3.1.252 TRP Tx TEG Association [348](#trp-tx-teg-association)

9.3.1.253 TRP TEG ID Information [348](#trp-teg-id-information)

9.3.1.254 Measurement Characteristics Request Indicator [348](#measurement-characteristics-request-indicator)

9.3.1.255 UE Reporting Information [349](#ue-reporting-information)

9.3.1.256 TRP Beam Antenna Information [349](#__RefHeading___Toc99731198)

9.3.1.257 TRP Beam Antenna Angles [350](#trp-beam-antenna-angles)

9.3.1.258 NR Paging eDRX Information [352](#nr-paging-edrx-information)

9.3.1.259 NR Paging eDRX Information for RRC INACTIVE [352](#nr-paging-edrx-information-for-rrc-inactive)

9.3.1.260 QoE Metrics [352](#qoe-metrics)

9.3.1.261 CG-SDT Session Info [352](#cg-sdt-session-info)

9.3.1.262 SDT Information [352](#sdt-information)

9.3.1.263 Path Switch Configuration [353](#path-switch-configuration)

9.3.1.264 Sidelink Relay Configuration [353](#sidelink-relay-configuration)

9.3.1.265 PC5 RLC Channel ID [353](#pc5-rlc-channel-id)

9.3.1.266 Uu RLC Channel ID [353](#uu-rlc-channel-id)

9.3.1.267 Remote UE Local ID [353](#remote-ue-local-id)

9.3.1.268 5G ProSe Authorized [354](#g-prose-authorized)

9.3.1.269 PEIPS Assistance Information [354](#peips-assistance-information)

9.3.1.270 UE Paging Capability [354](#ue-paging-capability)

9.3.1.271 gNB-DU UE Slice Maximum Bit Rate List [354](#gnb-du-ue-slice-maximum-bit-rate-list)

9.3.2 Transport Network Layer Related IEs [355](#transport-network-layer-related-ies)

9.3.2.1 UP Transport Layer Information [355](#up-transport-layer-information)

9.3.2.2 GTP-TEID [355](#gtp-teid)

9.3.2.3 Transport Layer Address [355](#transport-layer-address)

9.3.2.4 CP Transport Layer Information [355](#cp-transport-layer-information)

9.3.2.5 Transport Layer Address Info [356](#transport-layer-address-info)

9.3.2.6 URI [357](#uri)

9.3.2.7 BC Bearer Context F1-U TNL Info [357](#bc-bearer-context-f1-u-tnl-info)

9.3.2.8 MBS Multicast F1-U Context Descriptor [357](#mbs-multicast-f1-u-context-descriptor)

9.3.2.9 MBS PTP UE Reference [358](#mbs-ptp-ue-reference)

9.4 Message and Information Element Abstract Syntax (with ASN.1) [358](#message-and-information-element-abstract-syntax-with-asn.1)

9.4.1 General [358](#general-77)

9.4.2 Usage of private message mechanism for non-standard use [359](#usage-of-private-message-mechanism-for-non-standard-use)

9.4.3 Elementary Procedure Definitions [360](#elementary-procedure-definitions)

9.4.4 PDU Definitions [377](#pdu-definitions)

9.4.5 Information Element Definitions [471](#information-element-definitions-1)

9.4.6 Common Definitions [617](#common-definitions)

9.4.7 Constant Definitions [618](#constant-definitions)

9.4.8 Container Definitions [634](#container-definitions)

9.5 Message Transfer Syntax [639](#message-transfer-syntax)

9.6 Timers [639](#timers)

10 Handling of unknown, unforeseen and erroneous protocol data [639](#handling-of-unknown-unforeseen-and-erroneous-protocol-data)

Annex A (informative): Change History [640](#annex-a-informative-change-history)

# Foreword

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
