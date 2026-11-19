<!-- table -->
| 3GPP TS 23.247 V18.8.0 (2025-03) (x2) |
| Technical Specification (x2) |
| 3rd Generation Partnership Project; Technical Specification Group Services and System Aspects; Architectural enhancements for 5G multicast-broadcast services; Stage 2 (Release 18) (x2) |
| The present document has been developed within the 3rd Generation Partnership Project (3GPP TM ) and may be further elaborated for the purposes of 3GPP. / The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented. / This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification. / Specifications and Reports for implementation of the 3GPP TM system should be obtained via the 3GPP Organizational Partners' Publications Offices. (x2) |
<!-- /table -->

<!-- table -->
| 3GPP Postal address 3GPP support office address 650 Route des Lucioles - Sophia Antipolis Valbonne - FRANCE Tel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16 Internet http://www.3gpp.org |
| Copyright Notification No part may be reproduced except as authorized by written permission. / The copyright and the foregoing restriction extend to reproduction in all media. © 2025, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC). All rights reserved. UMTS™ is a Trade Mark of ETSI registered for the benefit of its members 3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners / LTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners GSM® and the GSM logo are registered and owned by the GSM Association |
<!-- /table -->

#  Contents

Foreword [8](#foreword)

1 Scope [10](#scope)

2 References [10](#references)

3 Definitions of terms and abbreviations [11](#definitions-of-terms-and-abbreviations)

3.1 Terms [11](#terms)

3.2 Abbreviations [12](#abbreviations)

4 General Concept [13](#_Toc193699571)

4.1 Overview of multicast and broadcast communication [13](#overview-of-multicast-and-broadcast-communication)

4.2 MB service provisioning [15](#mb-service-provisioning)

4.2.1 Multicast data provisioning [15](#multicast-data-provisioning)

4.2.2 Broadcast data provisioning [16](#broadcast-data-provisioning)

4.3 Multicast session state model [17](#multicast-session-state-model)

5 Architecture model [20](#architecture-model)

5.1 General architecture [20](#general-architecture)

5.2 General architecture for interworking with EPS [21](#general-architecture-for-interworking-with-eps)

5.3 Service-based interfaces, Reference point and functional entities [22](#service-based-interfaces-reference-point-and-functional-entities)

5.3.0 Service-based interfaces [22](#service-based-interfaces)

5.3.1 Reference point [22](#reference-point)

5.3.2 Functional entities [23](#functional-entities)

5.3.2.1 PCF [23](#pcf)

5.3.2.2 MB-SMF [23](#mb-smf)

5.3.2.3 SMF [24](#smf)

5.3.2.4 MB-UPF [24](#mb-upf)

5.3.2.5 UPF [24](#upf)

5.3.2.6 AMF [25](#amf)

5.3.2.7 NG-RAN [25](#ng-ran)

5.3.2.8 UE [25](#ue)

5.3.2.9 AF [25](#af)

5.3.2.10 NEF [26](#nef)

5.3.2.11 MBSF [26](#mbsf)

5.3.2.12 MBSTF [26](#mbstf)

5.3.2.13 UDM [27](#udm)

5.3.2.14 UDR [27](#udr)

5.3.2.15 NRF [27](#nrf)

5.3.2.15.1 General [27](#general)

5.3.2.15.2 Extensions to NF profile at NRF [27](#extensions-to-nf-profile-at-nrf)

6 Functionalities and features [27](#functionalities-and-features)

6.1 Authorization to MBS service [27](#authorization-to-mbs-service)

6.1.1 AF authorization to the service for multicast and broadcast [27](#af-authorization-to-the-service-for-multicast-and-broadcast)

6.1.2 UE authorization to the service for multicast [27](#ue-authorization-to-the-service-for-multicast)

6.2 Local MBS service and Location dependent MBS service [28](#local-mbs-service-and-location-dependent-mbs-service)

6.2.1 General [28](#general-1)

6.2.2 Local MBS service [28](#local-mbs-service)

6.2.3 Location dependent MBS service [29](#location-dependent-mbs-service)

6.2.4 Void [29](#void)

6.2.5 Void [29](#void-1)

6.3 Mobility support of MBS service [30](#mobility-support-of-mbs-service)

6.3.1 Mobility of Multicast MBS session [30](#mobility-of-multicast-mbs-session)

6.3.2 Mobility of Broadcast MBS session [30](#mobility-of-broadcast-mbs-session)

6.4 Subscription to multicast services [31](#subscription-to-multicast-services)

6.4.1 General [31](#general-2)

6.4.2 MBS subscription data in UDM [31](#mbs-subscription-data-in-udm)

6.4.3 MBS information in UDR [32](#mbs-information-in-udr)

6.5 Identifiers [32](#identifiers)

6.5.1 MBS Session ID [32](#mbs-session-id)

6.5.2 Temporary Mobile Group Identity [32](#temporary-mobile-group-identity)

6.5.3 Source Specific IP Multicast Address [32](#source-specific-ip-multicast-address)

6.5.4 MBS Frequency Selection Area ID [32](#mbs-frequency-selection-area-id)

6.5.5 Associated Session ID [33](#associated-session-id)

6.6 QoS Handling for Multicast and Broadcast services [33](#qos-handling-for-multicast-and-broadcast-services)

6.7 User plane management [34](#user-plane-management)

6.8 Interworking with MBMS over E-UTRAN for public safety services [36](#interworking-with-mbms-over-e-utran-for-public-safety-services)

6.9 MBS Session Context [36](#mbs-session-context)

6.9.1 MBS Session Context [36](#mbs-session-context-1)

6.10 Policy control for Multicast and Broadcast services [38](#policy-control-for-multicast-and-broadcast-services)

6.10.1 General [38](#general-3)

6.10.2 MBS Session policy control data in UDR [39](#mbs-session-policy-control-data-in-udr)

6.11 Service Announcement [39](#service-announcement)

6.12 Paging strategy handling [40](#paging-strategy-handling)

6.13 MBS Security function [41](#mbs-security-function)

6.14 MBS Service Information [41](#mbs-service-information)

6.15 Group Message Delivery [42](#group-message-delivery)

6.16 Support of MBS data reception for UEs using power saving functions [42](#support-of-mbs-data-reception-for-ues-using-power-saving-functions)

6.17 Support of Multicast MBS session data reception in UE with RRC_INACTIVE state [43](#support-of-multicast-mbs-session-data-reception-in-ue-with-rrc_inactive-state)

6.18 Resource sharing across broadcast MBS Sessions during network sharing [44](#resource-sharing-across-broadcast-mbs-sessions-during-network-sharing)

6.19 Support of Broadcast MBS Session Intended for NR (e)RedCap UEs [45](#support-of-broadcast-mbs-session-intended-for-nr-eredcap-ues)

6.20 QoE Measurement Collection Support for MBS [45](#qoe-measurement-collection-support-for-mbs)

7 MBS procedures [46](#mbs-procedures)

7.1 Common procedure for Multicast and Broadcast [46](#common-procedure-for-multicast-and-broadcast)

7.1.1 MBS Session Management [46](#mbs-session-management)

7.1.1.1 General [46](#general-4)

7.1.1.2 MBS Session Creation without PCC [46](#mbs-session-creation-without-pcc)

7.1.1.3 MBS Session Creation with PCC [50](#mbs-session-creation-with-pcc)

7.1.1.4 MBS Session Deletion without PCC [54](#mbs-session-deletion-without-pcc)

7.1.1.5 MBS Session Deletion with PCC [55](#mbs-session-deletion-with-pcc)

7.1.1.6 MBS Session Update without PCC [57](#mbs-session-update-without-pcc)

7.1.1.7 MBS Session Update with PCC [58](#mbs-session-update-with-pcc)

7.1.2 MB-SMF discovery and selection for multicast/broadcast session [60](#mb-smf-discovery-and-selection-for-multicastbroadcast-session)

7.1.3 MB-UPF discovery and selection for multicast/broadcast session [61](#mb-upf-discovery-and-selection-for-multicastbroadcast-session)

7.2 MBS procedures for multicast Session [61](#mbs-procedures-for-multicast-session)

7.2.1 MBS join and Session establishment procedure [61](#mbs-join-and-session-establishment-procedure)

7.2.1.1 General [61](#general-5)

7.2.1.2 Establishment of a PDU Session that can be associated with multicast session(s) [62](#establishment-of-a-pdu-session-that-can-be-associated-with-multicast-sessions)

7.2.1.3 Multicast session join and session establishment procedure [62](#multicast-session-join-and-session-establishment-procedure)

7.2.1.4 Establishment of shared delivery toward RAN node [67](#establishment-of-shared-delivery-toward-ran-node)

7.2.2 Multicast MBS Session leave and Multicast MBS Session release procedure [68](#multicast-mbs-session-leave-and-multicast-mbs-session-release-procedure)

7.2.2.1 General [68](#general-6)

7.2.2.2 Multicast Session leave requested by the UE [68](#multicast-session-leave-requested-by-the-ue)

7.2.2.3 Multicast session leave requested by the network or MBS session release [70](#multicast-session-leave-requested-by-the-network-or-mbs-session-release)

7.2.2.4 Release of shared delivery toward RAN node [72](#release-of-shared-delivery-toward-ran-node)

7.2.3 Mobility Procedures for MBS [73](#mobility-procedures-for-mbs)

7.2.3.1 General [73](#general-7)

7.2.3.2 Xn based handover from MBS supporting NG-RAN node [73](#xn-based-handover-from-mbs-supporting-ng-ran-node)

7.2.3.3 N2 based handover from MBS supporting NG-RAN node [75](#n2-based-handover-from-mbs-supporting-ng-ran-node)

7.2.3.4 Xn/N2 based handover from non-MBS supporting NG-RAN node [76](#xnn2-based-handover-from-non-mbs-supporting-ng-ran-node)

7.2.3.5 Minimization of data loss [77](#minimization-of-data-loss)

7.2.3.6 Xn/N2 based handover for inactive MBS session [77](#xnn2-based-handover-for-inactive-mbs-session)

7.2.3.7 Connection Resume in RRC_INACTIVE procedure [78](#connection-resume-in-rrc_inactive-procedure)

7.2.3.8 Mobility procedures to enable delivery of multicast MBS session data to UEs in RRC_INACTIVE state [78](#mobility-procedures-to-enable-delivery-of-multicast-mbs-session-data-to-ues-in-rrc_inactive-state)

7.2.3.8.1 General [78](#general-8)

7.2.3.8.2 Mobility of UE in RRC_INACTIVE state receiving MBS data within RNA [79](#mobility-of-ue-in-rrc_inactive-state-receiving-mbs-data-within-rna)

7.2.3.8.3 Mobility of UE in RRC_INACTIVE state receiving MBS data out of RNA and within RA [79](#mobility-of-ue-in-rrc_inactive-state-receiving-mbs-data-out-of-rna-and-within-ra)

7.2.3.8.4 Mobility of UE in RRC_INACTIVE state receiving MBS data out of RA [79](#mobility-of-ue-in-rrc_inactive-state-receiving-mbs-data-out-of-ra)

7.2.4 Support of Local multicast service and Location dependent multicast service [79](#support-of-local-multicast-service-and-location-dependent-multicast-service)

7.2.4.1 General [79](#general-9)

7.2.4.2 Support of location dependent multicast service [79](#support-of-location-dependent-multicast-service)

7.2.4.2.0 Creation for location dependent MBS session [79](#creation-for-location-dependent-mbs-session)

7.2.4.2.1 UE join location dependent Multicast MBS session and establishment procedure [80](#ue-join-location-dependent-multicast-mbs-session-and-establishment-procedure)

7.2.4.2.2 Void [81](#void-2)

7.2.4.2.3 Handover procedure [81](#handover-procedure)

7.2.4.2.4 Activation of location dependent MBS session [83](#activation-of-location-dependent-mbs-session)

7.2.4.2.5 UE location change handling within the same NG-RAN node between cells belonging to different MBS service areas during Individual delivery [83](#ue-location-change-handling-within-the-same-ng-ran-node-between-cells-belonging-to-different-mbs-service-areas-during-individual-delivery)

7.2.4.2.6 UE location change handling by SMF [84](#ue-location-change-handling-by-smf)

7.2.4.2.7 UE mobility within the same NG-RAN between cells belonging to different MBS service areas for shared delivery [84](#ue-mobility-within-the-same-ng-ran-between-cells-belonging-to-different-mbs-service-areas-for-shared-delivery)

7.2.4.2.8 Void [85](#void-3)

7.2.4.2.9 Connection Resume procedure [85](#connection-resume-procedure)

7.2.4.3 Support of local MBS for multicast [85](#support-of-local-mbs-for-multicast)

7.2.4.3.1 Local MBS service area information provided by AF [85](#local-mbs-service-area-information-provided-by-af)

7.2.4.3.2 Multicast session join and session establishment procedure for local MBS [85](#multicast-session-join-and-session-establishment-procedure-for-local-mbs)

7.2.4.3.3 Handover procedure with local MBS session [86](#handover-procedure-with-local-mbs-session)

7.2.4.3.4 Activation of local MBS session [87](#activation-of-local-mbs-session)

7.2.4.3.5 UE location change handling by SMF [87](#ue-location-change-handling-by-smf-1)

7.2.4.3.6 UE mobility within the same NG-RAN between cells in or out of the MBS service area [88](#ue-mobility-within-the-same-ng-ran-between-cells-in-or-out-of-the-mbs-service-area)

7.2.4.3.7 Void [88](#void-4)

7.2.4.3.8 Connection Resume procedure with local MBS session [88](#connection-resume-procedure-with-local-mbs-session)

7.2.5 MBS session activation and deactivation [88](#mbs-session-activation-and-deactivation)

7.2.5.1 General [88](#general-10)

7.2.5.2 MBS session activation procedure [89](#mbs-session-activation-procedure)

7.2.5.3 MBS session deactivation procedure [92](#mbs-session-deactivation-procedure)

7.2.6 Multicast session update procedure [93](#multicast-session-update-procedure)

7.2.7 Void [96](#void-5)

7.2.8 Service request procedure [96](#service-request-procedure)

7.2.9 AF provisioning multicast MBS Session Authorization information [96](#af-provisioning-multicast-mbs-session-authorization-information)

7.2.9a AF provisioning MBS Session assistance information [97](#a-af-provisioning-mbs-session-assistance-information)

7.2.10 Multicast MBS procedures for UEs using power saving functions [97](#multicast-mbs-procedures-for-ues-using-power-saving-functions)

7.3 MBS procedures for broadcast Session [98](#mbs-procedures-for-broadcast-session)

7.3.1 MBS Session Start for Broadcast [98](#mbs-session-start-for-broadcast)

7.3.1a MBS Session Start for resource sharing across multiple broadcast MBS Sessions during network sharing [101](#a-mbs-session-start-for-resource-sharing-across-multiple-broadcast-mbs-sessions-during-network-sharing)

7.3.2 MBS Session Release for Broadcast [101](#mbs-session-release-for-broadcast)

7.3.2a MBS Session Release for resource sharing across multiple broadcast MBS Sessions during network sharing [102](#a-mbs-session-release-for-resource-sharing-across-multiple-broadcast-mbs-sessions-during-network-sharing)

7.3.3 MBS Session Update for Broadcast [103](#mbs-session-update-for-broadcast)

7.3.4 Support for Location dependent Broadcast Service [105](#support-for-location-dependent-broadcast-service)

7.3.5 MBS Session Delivery Status Indication for Broadcast [105](#mbs-session-delivery-status-indication-for-broadcast)

7.3.6 Broadcast MBS Session Release Require [106](#broadcast-mbs-session-release-require)

7.3.7 Transport change for resource sharing across broadcast MBS Sessions during network sharing [107](#transport-change-for-resource-sharing-across-broadcast-mbs-sessions-during-network-sharing)

7.3.8 Broadcast MBS procedures for UEs using power saving functions [108](#broadcast-mbs-procedures-for-ues-using-power-saving-functions)

7.4 MBS procedures for inter System Mobility [109](#mbs-procedures-for-inter-system-mobility)

7.4.1 Inter-system mobility with interworking at service layer [109](#inter-system-mobility-with-interworking-at-service-layer)

7.5 MBS procedures for Group Message Delivery [110](#mbs-procedures-for-group-message-delivery)

7.5.1 Group Message Delivery via MBS Broadcast [110](#group-message-delivery-via-mbs-broadcast)

7.5.2 Modification of previously submitted Group message [112](#modification-of-previously-submitted-group-message)

7.5.3 Cancellation of previously submitted Group message [113](#cancellation-of-previously-submitted-group-message)

8 Control and user plane stacks [114](#control-and-user-plane-stacks)

8.1 Control plane for Multicast and Broadcast services [114](#control-plane-for-multicast-and-broadcast-services)

8.1.1 General [114](#general-11)

8.1.2 NG-RAN – MB-SMF [114](#ng-ran-mb-smf)

8.2 User plane for Multicast and Broadcast services [114](#user-plane-for-multicast-and-broadcast-services)

9 Network Function Services [116](#network-function-services)

9.1 MB-SMF Services [116](#mb-smf-services)

9.1.1 General [116](#general-12)

9.1.2 Nmbsmf_TMGI service [116](#nmbsmf_tmgi-service)

9.1.2.1 General [116](#general-13)

9.1.2.2 Nmbsmf_TMGI_Allocate service operation [116](#nmbsmf_tmgi_allocate-service-operation)

9.1.2.3 Nmbsmf_TMGI_Deallocate service operation [116](#nmbsmf_tmgi_deallocate-service-operation)

9.1.3 Nmbsmf_MBSSession service [117](#nmbsmf_mbssession-service)

9.1.3.1 General [117](#general-14)

9.1.3.2 Nmbsmf_MBSSession_ContextUpdate service operation [117](#nmbsmf_mbssession_contextupdate-service-operation)

9.1.3.3 Nmbsmf_MBSSession_ContextStatusSubscribe service operation [118](#nmbsmf_mbssession_contextstatussubscribe-service-operation)

9.1.3.4 Nmbsmf_MBSSession_ContextStatusNotify service operation [118](#nmbsmf_mbssession_contextstatusnotify-service-operation)

9.1.3.5 Nmbsmf_MBSSession_ContextStatusUnsubscribe service operation [118](#nmbsmf_mbssession_contextstatusunsubscribe-service-operation)

9.1.3.6 Nmbsmf_MBSSession_Create service operation [119](#nmbsmf_mbssession_create-service-operation)

9.1.3.7 Nmbsmf_MBSSession_Update service operation [119](#nmbsmf_mbssession_update-service-operation)

9.1.3.8 Nmbsmf_MBSSession_Delete service operation [119](#nmbsmf_mbssession_delete-service-operation)

9.1.3.9 Nmbsmf_MBSSession_StatusNotify service operation [119](#nmbsmf_mbssession_statusnotify-service-operation)

9.1.3.10 Nmbsmf_MBSSession_StatusSubscribe service operation [120](#nmbsmf_mbssession_statussubscribe-service-operation)

9.1.3.11 Nmbsmf_MBSSession_StatusUnsubscribe service operation [120](#nmbsmf_mbssession_statusunsubscribe-service-operation)

9.2 PCF Services [120](#pcf-services)

9.2.1 General [120](#general-15)

9.2.2 Npcf_MBSPolicyControl service [120](#npcf_mbspolicycontrol-service)

9.2.2.1 General [120](#general-16)

9.2.2.2 Npcf_MBSPolicyControl_Create service operation [121](#npcf_mbspolicycontrol_create-service-operation)

9.2.2.3 Void [121](#void-6)

9.2.2.4 Npcf_MBSPolicyControl_Delete service operation [121](#npcf_mbspolicycontrol_delete-service-operation)

9.2.2.5 Npcf_MBSPolicyControl_Update service operation [121](#npcf_mbspolicycontrol_update-service-operation)

9.2.3 Npcf_MBSPolicyAuthorization Service [122](#npcf_mbspolicyauthorization-service)

9.2.3.1 General [122](#general-17)

9.2.3.2 Npcf_MBSPolicyAuthorization_Create service operation [122](#npcf_mbspolicyauthorization_create-service-operation)

9.2.3.3 Npcf_MBSPolicyAuthorization_Update service operation [122](#npcf_mbspolicyauthorization_update-service-operation)

9.2.3.4 Npcf_MBSPolicyAuthorization_Delete service operation [122](#npcf_mbspolicyauthorization_delete-service-operation)

9.3 AMF Services [123](#amf-services)

9.3.1 General [123](#general-18)

9.3.2 Namf_MBSBroadcast service [123](#namf_mbsbroadcast-service)

9.3.2.1 General [123](#general-19)

9.3.2.2 Namf_MBSBroadcast_ContextCreate service operation [123](#namf_mbsbroadcast_contextcreate-service-operation)

9.3.2.3 Namf_MBSBroadcast_ContextUpdate service operation [123](#namf_mbsbroadcast_contextupdate-service-operation)

9.3.2.4 Namf_MBSBroadcast_ContextRelease service operation [124](#namf_mbsbroadcast_contextrelease-service-operation)

9.3.2.5 Namf_MBSBroadcast_ContextStatusNotify service operation [124](#namf_mbsbroadcast_contextstatusnotify-service-operation)

9.3.3 Namf_MBSCommunication Service [124](#namf_mbscommunication-service)

9.3.3.1 General [124](#general-20)

9.3.3.2 Namf_MBSCommunication_N2MessageTransfer service operation [124](#namf_mbscommunication_n2messagetransfer-service-operation)

9.4 NEF Services [124](#nef-services)

9.4.1 General [124](#general-21)

9.4.2 Nnef_MBSTMGI service [125](#nnef_mbstmgi-service)

9.4.2.1 General [125](#general-22)

9.4.2.2 Nnef_MBSTMGI_Allocate service operation [125](#nnef_mbstmgi_allocate-service-operation)

9.4.2.3 Nnef_MBSTMGI_Deallocate service operation [125](#nnef_mbstmgi_deallocate-service-operation)

9.4.2.4 Nnef_MBSTMGI_ExpiryNotify service operation [125](#nnef_mbstmgi_expirynotify-service-operation)

9.4.3 Nnef_MBSSession Service [126](#nnef_mbssession-service)

9.4.3.1 General [126](#general-23)

9.4.3.2 Nnef_MBSSession_Create service operation [126](#nnef_mbssession_create-service-operation)

9.4.3.3 Nnef_MBSSession_Update service operation [126](#nnef_mbssession_update-service-operation)

9.4.3.4 Nnef_MBSSession_Delete service operation [127](#nnef_mbssession_delete-service-operation)

9.4.3.5 Nnef_MBSSession_StatusNotify service operation [127](#nnef_mbssession_statusnotify-service-operation)

9.4.3.6 Nnef_MBSSession_StatusSubscribe service operation [127](#nnef_mbssession_statussubscribe-service-operation)

9.4.3.7 Nnef_MBSSession_StatusUnsubscribe service operation [127](#nnef_mbssession_statusunsubscribe-service-operation)

9.4.4 Nnef_MBSGroupMsgDelivery Service [128](#nnef_mbsgroupmsgdelivery-service)

9.4.4.1 General [128](#general-24)

9.4.4.2 Nnef_MBSGroupMsgDelivery_Create service operation [128](#nnef_mbsgroupmsgdelivery_create-service-operation)

9.4.4.3 Nnef_MBSGroupMsgDelivery_Update service operation [128](#nnef_mbsgroupmsgdelivery_update-service-operation)

9.4.4.3a Nnef_MBSGroupMsgDelivery_Delete service operation [128](#a-nnef_mbsgroupmsgdelivery_delete-service-operation)

9.4.4.4 Nnef_MBSGroupMsgDelivery_StatusNotify service operation [128](#nnef_mbsgroupmsgdelivery_statusnotify-service-operation)

9.5 MBSF Services [129](#mbsf-services)

Annex A (normative): Configuration options at Service and/or Application for MBS [130](#annex-a-normative-configuration-options-at-service-andor-application-for-mbs)

Annex B (informative): Service levels for multicast communication service [132](#annex-b-informative-service-levels-for-multicast-communication-service)

Annex C (normative): Interworking at reference points MB2 and xMB [133](#annex-c-normative-interworking-at-reference-points-mb2-and-xmb)

Annex D (informative): Change history [134](#annex-d-informative-change-history)

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

In the present document, modal verbs have the following meanings:

**shall** indicates a mandatory requirement to do something

**shall not** indicates an interdiction (prohibition) to do something

The constructions "shall" and "shall not" are confined to the context of normative provisions, and do not appear in Technical Reports.

The constructions "must" and "must not" are not used as substitutes for "shall" and "shall not". Their use is avoided insofar as possible, and they are not used in a normative context except in a direct citation from an external, referenced, non-3GPP document, or so as to maintain continuity of style when extending or modifying the provisions of such a referenced document.

**should** indicates a recommendation to do something

**should not** indicates a recommendation not to do something

**may** indicates permission to do something

**need not** indicates permission not to do something

The construction "may not" is ambiguous and is not used in normative elements. The unambiguous constructions "might not" or "shall not" are used instead, depending upon the meaning intended.

**can** indicates that something is possible

**cannot** indicates that something is impossible

The constructions "can" and "cannot" are not substitutes for "may" and "need not".

**will** indicates that something is certain or expected to happen as a result of action taken by an agency the behaviour of which is outside the scope of the present document

**will not** indicates that something is certain or expected not to happen as a result of action taken by an agency the behaviour of which is outside the scope of the present document

**might** indicates a likelihood that something will happen as a result of action taken by some agency the behaviour of which is outside the scope of the present document

**might not** indicates a likelihood that something will not happen as a result of action taken by some agency the behaviour of which is outside the scope of the present document

In addition:

**is** (or any other verb in the indicative mood) indicates a statement of fact

**is not** (or any other negative verb in the indicative mood) indicates a statement of fact

The constructions "is" and "is not" do not indicate requirements.
