<!-- table -->
| 3GPP TS 23.502 V18.14.0 (2026-06) (x2) |
| Technical Specification (x2) |
| 3rd Generation Partnership Project; Technical Specification Group Services and System Aspects; Procedures for the 5G System (5GS); Stage 2 (Release 18) (x2) |
| The present document has been developed within the 3rd Generation Partnership Project (3GPP TM ) and may be further elaborated for the purposes of 3GPP. / The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented. / This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification. / Specifications and Reports for implementation of the 3GPP TM system should be obtained via the 3GPP Organizational Partners' Publications Offices. (x2) |
<!-- /table -->

<!-- table -->
| 3GPP Postal address 3GPP support office address 650 Route des Lucioles - Sophia Antipolis Valbonne - FRANCE Tel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16 Internet http://www.3gpp.org |
| Copyright Notification No part may be reproduced except as authorized by written permission. / The copyright and the foregoing restriction extend to reproduction in all media. © 2026, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC). All rights reserved. UMTS™ is a Trade Mark of ETSI registered for the benefit of its members 3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners / LTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners GSM® and the GSM logo are registered and owned by the GSM Association |
<!-- /table -->

#  Contents

Foreword [26](#foreword)

1 Scope [27](#scope)

2 References [27](#references)

3 Definitions, symbols and abbreviations [30](#definitions-symbols-and-abbreviations)

3.1 Definitions [30](#definitions)

3.2 Abbreviations [31](#abbreviations)

4 System procedures [31](#system-procedures)

4.1 General [31](#general)

4.2 Connection, Registration and Mobility Management procedures [31](#connection-registration-and-mobility-management-procedures)

4.2.1 General [31](#general-1)

4.2.2 Registration Management procedures [31](#registration-management-procedures)

4.2.2.1 General [31](#general-2)

4.2.2.2 Registration procedures [31](#registration-procedures)

4.2.2.2.1 General [31](#general-3)

4.2.2.2.2 General Registration [33](#general-registration)

4.2.2.2.3 Registration with AMF re-allocation [54](#registration-with-amf-re-allocation)

4.2.2.2.4 Registration with Onboarding SNPN [58](#registration-with-onboarding-snpn)

4.2.2.3 Deregistration procedures [60](#deregistration-procedures)

4.2.2.3.1 General [60](#general-4)

4.2.2.3.2 UE-initiated Deregistration [60](#ue-initiated-deregistration)

4.2.2.3.3 Network-initiated Deregistration [62](#network-initiated-deregistration)

4.2.3 Service Request procedures [63](#service-request-procedures)

4.2.3.1 General [63](#general-5)

4.2.3.2 UE Triggered Service Request [64](#ue-triggered-service-request)

4.2.3.3 Network Triggered Service Request [76](#network-triggered-service-request)

4.2.4 UE Configuration Update [85](#ue-configuration-update)

4.2.4.1 General [85](#general-6)

4.2.4.2 UE Configuration Update procedure for access and mobility management related parameters [86](#ue-configuration-update-procedure-for-access-and-mobility-management-related-parameters)

4.2.4.3 UE Configuration Update procedure for transparent UE Policy delivery [90](#ue-configuration-update-procedure-for-transparent-ue-policy-delivery)

4.2.5 Reachability procedures [92](#reachability-procedures)

4.2.5.1 General [92](#general-7)

4.2.5.2 UE Reachability Notification Request procedure [92](#ue-reachability-notification-request-procedure)

4.2.5.3 UE Activity Notification procedure [94](#ue-activity-notification-procedure)

4.2.6 AN Release [95](#an-release)

4.2.7 N2 procedures [98](#n2-procedures)

4.2.7.1 N2 Configuration [98](#n2-configuration)

4.2.7.2 NGAP UE-TNLA-binding related procedures [98](#ngap-ue-tnla-binding-related-procedures)

4.2.7.2.1 Creating NGAP UE-TNLA-bindings during Registration and Service Request [98](#creating-ngap-ue-tnla-bindings-during-registration-and-service-request)

4.2.7.2.2 Creating NGAP UE-TNLA-bindings during handovers [99](#creating-ngap-ue-tnla-bindings-during-handovers)

4.2.7.2.3 Re-Creating NGAP UE-TNLA-bindings subsequent to NGAP UE-TNLA-binding release [99](#re-creating-ngap-ue-tnla-bindings-subsequent-to-ngap-ue-tnla-binding-release)

4.2.7.2.4 NGAP UE-TNLA-binding update procedure [100](#ngap-ue-tnla-binding-update-procedure)

4.2.7.2.5 NGAP UE-TNLA-binding per UE Release procedure [100](#ngap-ue-tnla-binding-per-ue-release-procedure)

4.2.7.3 AMF Failure or Planned Maintenance handling procedure [100](#amf-failure-or-planned-maintenance-handling-procedure)

4.2.7.4 Additional User Location Information with Mobile Base Station Relay (MBSR) [101](#additional-user-location-information-with-mobile-base-station-relay-mbsr)

4.2.8 Void [101](#void)

4.2.8a UE Capability Match Request procedure [101](#a-ue-capability-match-request-procedure)

4.2.9 Network Slice-Specific Authentication and Authorization procedure [102](#network-slice-specific-authentication-and-authorization-procedure)

4.2.9.1 General [102](#general-8)

4.2.9.2 Network Slice-Specific Authentication and Authorization [103](#network-slice-specific-authentication-and-authorization)

4.2.9.3 AAA Server triggered Network Slice-Specific Re-authentication and Re-authorization procedure [105](#aaa-server-triggered-network-slice-specific-re-authentication-and-re-authorization-procedure)

4.2.9.4 AAA Server triggered Slice-Specific Authorization Revocation [106](#aaa-server-triggered-slice-specific-authorization-revocation)

4.2.10 N3 data transfer establishment procedure when Control Plane CIoT 5GS Optimisation is enabled [107](#n3-data-transfer-establishment-procedure-when-control-plane-ciot-5gs-optimisation-is-enabled)

4.2.10.1 UE triggered N3 data transfer establishment procedure [107](#ue-triggered-n3-data-transfer-establishment-procedure)

4.2.10.2 SMF triggered N3 data transfer establishment procedure [107](#smf-triggered-n3-data-transfer-establishment-procedure)

4.2.11 Network Slice Admission Control Function (NSACF) procedures [108](#network-slice-admission-control-function-nsacf-procedures)

4.2.11.1 General [108](#general-9)

4.2.11.2 Number of UEs per network slice availability check and update procedure [108](#number-of-ues-per-network-slice-availability-check-and-update-procedure)

4.2.11.2a Hierarchical NSACF-based number of UEs per network slice availability check and update procedure [111](#a-hierarchical-nsacf-based-number-of-ues-per-network-slice-availability-check-and-update-procedure)

4.2.11.3 Configuration for Early Admission Control (EAC) update procedure [113](#configuration-for-early-admission-control-eac-update-procedure)

4.2.11.4 Number of PDU Sessions per network slice availability check and update procedure [114](#number-of-pdu-sessions-per-network-slice-availability-check-and-update-procedure)

4.2.11.4a Hierarchical NSACF-based Number of PDU Sessions per network slice availability check and update procedure [117](#a-hierarchical-nsacf-based-number-of-pdu-sessions-per-network-slice-availability-check-and-update-procedure)

4.2.11.5 Network Slice Admission Control Support for Roaming [118](#network-slice-admission-control-support-for-roaming)

4.2.11.5.1 Network Slice Admission Control Support for Roaming by VPLMN [118](#network-slice-admission-control-support-for-roaming-by-vplmn)

4.2.11.5.2 Network Slice Admission Control Support for Roaming by HPLMN [119](#network-slice-admission-control-support-for-roaming-by-hplmn)

4.2.11.6 Update of local maximum number in Hierarchical NSAC Architecture [124](#update-of-local-maximum-number-in-hierarchical-nsac-architecture)

4.3 Session Management procedures [125](#session-management-procedures)

4.3.1 General [125](#general-11)

4.3.2 PDU Session Establishment [126](#pdu-session-establishment)

4.3.2.1 General [126](#general-12)

4.3.2.2 UE Requested PDU Session Establishment [126](#ue-requested-pdu-session-establishment)

4.3.2.2.1 Non-roaming and Roaming with Local Breakout [126](#non-roaming-and-roaming-with-local-breakout)

4.3.2.2.2 Home-routed Roaming [142](#home-routed-roaming)

4.3.2.2.3 SMF selection [147](#smf-selection)

4.3.2.2.4 Multiple PDU Sessions towards the same DNN and S-NSSAI [151](#multiple-pdu-sessions-towards-the-same-dnn-and-s-nssai)

4.3.2.3 Secondary authorization/authentication by an DN-AAA Server during the PDU Session establishment [151](#secondary-authorizationauthentication-by-an-dn-aaa-server-during-the-pdu-session-establishment)

4.3.2.4 Support of L2TP [154](#support-of-l2tp)

4.3.3 PDU Session Modification [156](#pdu-session-modification)

4.3.3.1 General [156](#general-14)

4.3.3.2 UE or network requested PDU Session Modification (non-roaming and roaming with local breakout) [156](#ue-or-network-requested-pdu-session-modification-non-roaming-and-roaming-with-local-breakout)

4.3.3.3 UE or network requested PDU Session Modification (home-routed roaming) [166](#ue-or-network-requested-pdu-session-modification-home-routed-roaming)

4.3.4 PDU Session Release [170](#pdu-session-release)

4.3.4.1 General [170](#general-15)

4.3.4.2 UE or network requested PDU Session Release for Non-Roaming and Roaming with Local Breakout [170](#ue-or-network-requested-pdu-session-release-for-non-roaming-and-roaming-with-local-breakout)

4.3.4.3 UE or network requested PDU Session Release for Home-routed Roaming [176](#ue-or-network-requested-pdu-session-release-for-home-routed-roaming)

4.3.5 Session continuity, service continuity and UP path management [179](#session-continuity-service-continuity-and-up-path-management)

4.3.5.1 Change of SSC mode 2 PDU Session Anchor with different PDU Sessions [179](#change-of-ssc-mode-2-pdu-session-anchor-with-different-pdu-sessions)

4.3.5.2 Change of SSC mode 3 PDU Session Anchor with multiple PDU Sessions [180](#change-of-ssc-mode-3-pdu-session-anchor-with-multiple-pdu-sessions)

4.3.5.3 Change of SSC mode 3 PDU Session Anchor with IPv6 Multi-homed PDU Session [183](#change-of-ssc-mode-3-pdu-session-anchor-with-ipv6-multi-homed-pdu-session)

4.3.5.4 Addition of additional PDU Session Anchor and Branching Point or UL CL [186](#addition-of-additional-pdu-session-anchor-and-branching-point-or-ul-cl)

4.3.5.5 Removal of additional PDU Session Anchor and Branching Point or UL CL [187](#removal-of-additional-pdu-session-anchor-and-branching-point-or-ul-cl)

4.3.5.6 Change of additional PDU Session Anchor for IPv6 multi-homing or UL CL [189](#change-of-additional-pdu-session-anchor-for-ipv6-multi-homing-or-ul-cl)

4.3.5.7 Simultaneous change of Branching Point or UL CL and additional PSA for a PDU Session [190](#simultaneous-change-of-branching-point-or-ul-cl-and-additional-psa-for-a-pdu-session)

4.3.5.8 Ethernet PDU Session Anchor Relocation [193](#ethernet-pdu-session-anchor-relocation)

4.3.6 Application Function influence on traffic routing and service function chaining [195](#application-function-influence-on-traffic-routing-and-service-function-chaining)

4.3.6.1 General [195](#general-16)

4.3.6.2 Processing AF requests to influence traffic routing and/or Service Function Chaining for Sessions not identified by an UE address [198](#processing-af-requests-to-influence-traffic-routing-andor-service-function-chaining-for-sessions-not-identified-by-an-ue-address)

4.3.6.3 Notification of User Plane Management Events [200](#notification-of-user-plane-management-events)

4.3.6.4 Transferring an AF request targeting an individual UE address to the relevant PCF [204](#transferring-an-af-request-targeting-an-individual-ue-address-to-the-relevant-pcf)

4.3.6.5 Processing AF requests to influence traffic routing for HR-SBO session [205](#processing-af-requests-to-influence-traffic-routing-for-hr-sbo-session)

4.3.6.5.1 General [205](#general-17)

4.3.6.5.2 AF traffic influence request includes HPLMN DNN, HPLMN S-NSSAI [206](#af-traffic-influence-request-includes-hplmn-dnn-hplmn-s-nssai)

4.3.6.5.3 AF traffic influence request without HPLMN DNN, S-NSSAI information for a single UE, with private IP address or public IP address owned by VPLMN [208](#af-traffic-influence-request-without-hplmn-dnn-s-nssai-information-for-a-single-ue-with-private-ip-address-or-public-ip-address-owned-by-vplmn)

4.3.6.5.4 AF traffic influence request without HPLMN DNN, S-NSSAI information for a single UE, with UE IP address owned and assigned by HPLMN [209](#af-traffic-influence-request-without-hplmn-dnn-s-nssai-information-for-a-single-ue-with-ue-ip-address-owned-and-assigned-by-hplmn)

4.3.6.5.5 AF traffic influence request for GPSI or any UE [210](#af-traffic-influence-request-for-gpsi-or-any-ue)

4.3.7 CN-initiated selective deactivation of UP connection of an existing PDU Session [211](#cn-initiated-selective-deactivation-of-up-connection-of-an-existing-pdu-session)

4.3.8 Change of Network Slice instance for PDU Sessions [212](#change-of-network-slice-instance-for-pdu-sessions)

4.4 SMF and UPF interactions [213](#smf-and-upf-interactions)

4.4.1 N4 session management procedures [213](#n4-session-management-procedures)

4.4.1.1 General [213](#general-18)

4.4.1.2 N4 Session Establishment procedure [213](#n4-session-establishment-procedure)

4.4.1.3 N4 Session Modification procedure [214](#n4-session-modification-procedure)

4.4.1.4 N4 Session Release procedure [214](#n4-session-release-procedure)

4.4.2 N4 Reporting Procedures [215](#n4-reporting-procedures)

4.4.2.1 General [215](#general-19)

4.4.2.2 N4 Session Level Reporting Procedure [215](#n4-session-level-reporting-procedure)

4.4.3 N4 Node Level Procedures [216](#n4-node-level-procedures)

4.4.3.1 N4 Association Setup Procedure [216](#n4-association-setup-procedure)

4.4.3.2 N4 Association Update Procedure [217](#n4-association-update-procedure)

4.4.3.3 N4 Association Release Procedure [218](#n4-association-release-procedure)

4.4.3.4 N4 Report Procedure [218](#n4-report-procedure)

4.4.3.5 N4 PFD management Procedure [219](#n4-pfd-management-procedure)

4.4.4 SMF Pause of Charging procedure [220](#smf-pause-of-charging-procedure)

4.5 User Profile management procedures [221](#user-profile-management-procedures)

4.5.1 Subscriber Data Update Notification to AMF [221](#subscriber-data-update-notification-to-amf)

4.5.2 Session Management Subscriber Data Update Notification to SMF [222](#session-management-subscriber-data-update-notification-to-smf)

4.5.3 Purge of subscriber data in AMF [222](#purge-of-subscriber-data-in-amf)

4.6 Security procedures [223](#security-procedures)

4.7 ME Identity check procedure [223](#me-identity-check-procedure)

4.8 RAN-CN interactions [223](#ran-cn-interactions)

4.8.1 Connection Inactive and Suspend procedure [223](#connection-inactive-and-suspend-procedure)

4.8.1.1 Connection Inactive procedure [223](#connection-inactive-procedure)

4.8.1.1a Connection Inactive procedure with CN based MT communication handling [223](#a-connection-inactive-procedure-with-cn-based-mt-communication-handling)

4.8.1.2 Connection Suspend procedure [225](#connection-suspend-procedure)

4.8.2 Connection Resume procedure [226](#connection-resume-procedure)

4.8.2.1 General [226](#general-20)

4.8.2.2 UE Triggered Connection Resume in RRC_INACTIVE procedure [226](#ue-triggered-connection-resume-in-rrc_inactive-procedure)

4.8.2.2a Network Triggered Connection Resume in RRC_INACTIVE procedure [228](#a-network-triggered-connection-resume-in-rrc_inactive-procedure)

4.8.2.2b Network Triggered Connection Resume in RRC_INACTIVE with CN based MT communication handling [229](#b-network-triggered-connection-resume-in-rrc_inactive-with-cn-based-mt-communication-handling)

4.8.2.3 Connection Resume in CM-IDLE with Suspend procedure [231](#connection-resume-in-cm-idle-with-suspend-procedure)

4.8.2.4 Connection Resume in CM-IDLE with Suspend and MO EDT procedure [232](#connection-resume-in-cm-idle-with-suspend-and-mo-edt-procedure)

4.8.3 N2 Notification procedure [234](#n2-notification-procedure)

4.9 Handover procedures [235](#handover-procedures)

4.9.1 Handover procedures in 3GPP access [235](#handover-procedures-in-3gpp-access)

4.9.1.1 General [235](#general-21)

4.9.1.2 Xn based inter NG-RAN handover [235](#xn-based-inter-ng-ran-handover)

4.9.1.2.1 General [235](#general-22)

4.9.1.2.2 Xn based inter NG-RAN handover without User Plane function re-allocation [236](#xn-based-inter-ng-ran-handover-without-user-plane-function-re-allocation)

4.9.1.2.3 Xn based inter NG-RAN handover with insertion of intermediate UPF [240](#xn-based-inter-ng-ran-handover-with-insertion-of-intermediate-upf)

4.9.1.2.4 Xn based inter NG-RAN handover with re-allocation of intermediate UPF [241](#xn-based-inter-ng-ran-handover-with-re-allocation-of-intermediate-upf)

4.9.1.3 Inter NG-RAN node N2 based handover [243](#inter-ng-ran-node-n2-based-handover)

4.9.1.3.1 General [243](#general-23)

4.9.1.3.2 Preparation phase [244](#preparation-phase)

4.9.1.3.3 Execution phase [251](#execution-phase)

4.9.1.3.3a Execution phase for DAPS handover [255](#a-execution-phase-for-daps-handover)

4.9.1.4 Inter NG-RAN node N2 based handover, Cancel [256](#inter-ng-ran-node-n2-based-handover-cancel)

4.9.2 Handover of a PDU Session procedure between 3GPP and untrusted non-3GPP access [256](#handover-of-a-pdu-session-procedure-between-3gpp-and-untrusted-non-3gpp-access)

4.9.2.0 General [256](#general-24)

4.9.2.1 Handover of a PDU Session procedure from untrusted non-3GPP to 3GPP access (non-roaming and roaming with local breakout) [256](#handover-of-a-pdu-session-procedure-from-untrusted-non-3gpp-to-3gpp-access-non-roaming-and-roaming-with-local-breakout)

4.9.2.2 Handover of a PDU Session procedure from 3GPP to untrusted non-3GPP access (non-roaming and roaming with local breakout) [257](#handover-of-a-pdu-session-procedure-from-3gpp-to-untrusted-non-3gpp-access-non-roaming-and-roaming-with-local-breakout)

4.9.2.3 Handover of a PDU Session procedure from untrusted non-3GPP to 3GPP access (home routed roaming) [258](#handover-of-a-pdu-session-procedure-from-untrusted-non-3gpp-to-3gpp-access-home-routed-roaming)

4.9.2.3.1 The target AMF is in the PLMN of the N3IWF [258](#the-target-amf-is-in-the-plmn-of-the-n3iwf)

4.9.2.3.2 The target AMF is not in the PLMN of the N3IWF (i.e. N3IWF in HPLMN) [259](#the-target-amf-is-not-in-the-plmn-of-the-n3iwf-i.e.-n3iwf-in-hplmn)

4.9.2.4 Handover of a PDU Session procedure from 3GPP to untrusted non-3GPP access (home routed roaming) [260](#handover-of-a-pdu-session-procedure-from-3gpp-to-untrusted-non-3gpp-access-home-routed-roaming)

4.9.2.4.1 The selected N3IWF is in the registered PLMN [260](#the-selected-n3iwf-is-in-the-registered-plmn)

4.9.2.4.2 The UE is roaming and the selected N3IWF is in the home PLMN [260](#the-ue-is-roaming-and-the-selected-n3iwf-is-in-the-home-plmn)

4.9.3 Handover of a PDU Session procedure between 3GPP and trusted non-3GPP access [261](#handover-of-a-pdu-session-procedure-between-3gpp-and-trusted-non-3gpp-access)

4.9.3.0 General [261](#general-25)

4.10 NG-RAN Location reporting procedures [261](#ng-ran-location-reporting-procedures)

4.11 System interworking procedures with EPC [263](#system-interworking-procedures-with-epc)

4.11.0 General [263](#general-26)

4.11.0a Impacts to EPS Procedures [263](#a-impacts-to-eps-procedures)

4.11.0a.1 General [263](#a.1-general)

4.11.0a.2 Interaction with PCC [264](#a.2-interaction-with-pcc)

4.11.0a.2a Interaction with PCC for URSP delivery via EPS [264](#a.2a-interaction-with-pcc-for-ursp-delivery-via-eps)

4.11.0a.2a.0 General [264](#a.2a.0-general)

4.11.0a.2a.1 SM Policy Association Establishment [265](#a.2a.1-sm-policy-association-establishment)

4.11.0a.2a.1a SM Policy Association Establishment in EPS [265](#a.2a.1a-sm-policy-association-establishment-in-eps)

4.11.0a.2a.2 SMF initiated SM Policy Association Modification [266](#a.2a.2-smf-initiated-sm-policy-association-modification)

4.11.0a.2a.3 PCF initiated SM Policy Association Modification [267](#a.2a.3-pcf-initiated-sm-policy-association-modification)

4.11.0a.2a.4 Void [267](#a.2a.4-void)

4.11.0a.2a.5 UE Policy Association establishment [267](#a.2a.5-ue-policy-association-establishment)

4.11.0a.2a.6 UE Policy Association Modification initiated by the PCF for the UE [269](#a.2a.6-ue-policy-association-modification-initiated-by-the-pcf-for-the-ue)

4.11.0a.2a.7 UE Policy Association Modification initiated by the PCF for the PDU Session [270](#a.2a.7-ue-policy-association-modification-initiated-by-the-pcf-for-the-pdu-session)

4.11.0a.2a.8 UE Policy Association Termination initiated by PCF for PDU session [271](#a.2a.8-ue-policy-association-termination-initiated-by-pcf-for-pdu-session)

4.11.0a.2a.9 UE Policy Association termination initiated by the PCF for the UE [271](#a.2a.9-ue-policy-association-termination-initiated-by-the-pcf-for-the-ue)

4.11.0a.2a.10 UE Policy Container delivery via EPS [272](#a.2a.10-ue-policy-container-delivery-via-eps)

4.11.0a.3 Mobility Restrictions [273](#a.3-mobility-restrictions)

4.11.0a.4 PGW Selection [273](#a.4-pgw-selection)

4.11.0a.5 PDN Connection Establishment [274](#a.5-pdn-connection-establishment)

4.11.0a.6 Network Configuration [276](#a.6-network-configuration)

4.11.0a.7 Interactions with DN-AAA Server [276](#a.7-interactions-with-dn-aaa-server)

4.11.0a.8 5GC NAS capability (re-)enabled and disabled [276](#a.8-5gc-nas-capability-re-enabled-and-disabled)

4.11.0a.9 PDN Connection Release [276](#a.9-pdn-connection-release)

4.11.0a.10 UE requested bearer resource modification procedure [276](#a.10-ue-requested-bearer-resource-modification-procedure)

4.11.0a.11 SMF+PGW-C initiated bearer modification without bearer QoS update [277](#a.11-smfpgw-c-initiated-bearer-modification-without-bearer-qos-update)

4.11.1 N26 based Interworking Procedures [277](#n26-based-interworking-procedures)

4.11.1.1 General [277](#general-27)

4.11.1.2 Handover procedures [279](#handover-procedures-1)

4.11.1.2.1 5GS to EPS handover using N26 interface [279](#gs-to-eps-handover-using-n26-interface)

4.11.1.2.2 EPS to 5GS handover using N26 interface [285](#eps-to-5gs-handover-using-n26-interface)

4.11.1.2.3 Handover Cancel [293](#handover-cancel)

4.11.1.3 Idle Mode Mobility procedures [295](#idle-mode-mobility-procedures)

4.11.1.3.1 General [295](#general-29)

4.11.1.3.2 5GS to EPS Idle mode mobility using N26 interface [295](#gs-to-eps-idle-mode-mobility-using-n26-interface)

4.11.1.3.2A 5GS to EPS Idle mode mobility using N26 interface with data forwarding [298](#a-5gs-to-eps-idle-mode-mobility-using-n26-interface-with-data-forwarding)

4.11.1.3.3 EPS to 5GS Mobility Registration Procedure (Idle and Connected State) using N26 interface [299](#eps-to-5gs-mobility-registration-procedure-idle-and-connected-state-using-n26-interface)

4.11.1.3.3A EPS to 5GS Idle mode mobility using N26 interface with data forwarding [305](#a-eps-to-5gs-idle-mode-mobility-using-n26-interface-with-data-forwarding)

4.11.1.3.4 EPS to 5GS Mobility Registration Procedure (Idle) using N26 interface with AMF reallocation [306](#eps-to-5gs-mobility-registration-procedure-idle-using-n26-interface-with-amf-reallocation)

4.11.1.4 Procedures for EPS bearer ID allocation [307](#procedures-for-eps-bearer-id-allocation)

4.11.1.4.1 EPS bearer ID allocation [307](#eps-bearer-id-allocation)

4.11.1.4.2 EPS bearer ID transfer [310](#eps-bearer-id-transfer)

4.11.1.4.3 EPS bearer ID revocation [311](#eps-bearer-id-revocation)

4.11.1.5 Impacts to EPS Procedures [312](#impacts-to-eps-procedures)

4.11.1.5.1 General [312](#general-30)

4.11.1.5.2 E-UTRAN Initial Attach [312](#e-utran-initial-attach)

4.11.1.5.3 Tracking Area Update [313](#tracking-area-update)

4.11.1.5.4 Session Management [314](#session-management)

4.11.1.5.5 5GS to EPS handover using N26 interface [316](#gs-to-eps-handover-using-n26-interface-1)

4.11.1.5.6 UE triggered Service Request [316](#ue-triggered-service-request-1)

4.11.1.5.7 Establishment of S1-U bearer during Data Transport in Control Plane CIoT EPS Optimisation [316](#establishment-of-s1-u-bearer-during-data-transport-in-control-plane-ciot-eps-optimisation)

4.11.1.5.8 Radio Resource Management functions and Information Storage [316](#radio-resource-management-functions-and-information-storage)

4.11.1.6 EPS interworking information storing Procedure [317](#eps-interworking-information-storing-procedure)

4.11.2 Interworking procedures without N26 interface [317](#interworking-procedures-without-n26-interface)

4.11.2.1 General [317](#general-31)

4.11.2.2 5GS to EPS Mobility [317](#gs-to-eps-mobility)

4.11.2.3 EPS to 5GS Mobility [320](#eps-to-5gs-mobility)

4.11.2.4 Impacts to EPS Procedures [322](#impacts-to-eps-procedures-1)

4.11.2.4.1 E-UTRAN Attach [322](#e-utran-attach)

4.11.2.4.2 Session Management [324](#session-management-1)

4.11.2.4.3 Void [324](#void-1)

4.11.3 Handover procedures between EPS and 5GC-N3IWF [325](#handover-procedures-between-eps-and-5gc-n3iwf)

4.11.3.1 Handover from EPS to 5GC-N3IWF [325](#handover-from-eps-to-5gc-n3iwf)

4.11.3.2 Handover from 5GC-N3IWF to EPS [325](#handover-from-5gc-n3iwf-to-eps)

4.11.3a Handover procedures between EPS and 5GC-TNGF [326](#a-handover-procedures-between-eps-and-5gc-tngf)

4.11.3a.1 Handover from EPS to 5GC-TNGF [326](#a.1-handover-from-eps-to-5gc-tngf)

4.11.3a.2 Handover from 5GC-TNGF to EPS [326](#a.2-handover-from-5gc-tngf-to-eps)

4.11.4 Handover procedures between EPC/ePDG and 5GS [327](#handover-procedures-between-epcepdg-and-5gs)

4.11.4.1 Handover from EPC/ePDG to 5GS [327](#handover-from-epcepdg-to-5gs)

4.11.4.2 Handover from 5GS to EPC/ePDG [328](#handover-from-5gs-to-epcepdg)

4.11.4.3 Impacts to EPC/ePDG Procedures [328](#impacts-to-epcepdg-procedures)

4.11.4.3.1 General [328](#general-32)

4.11.4.3.2 ePDG FQDN construction [328](#epdg-fqdn-construction)

4.11.4.3.3 Initial Attach with GTP on S2b [329](#initial-attach-with-gtp-on-s2b)

4.11.4.3.3a Initial Attach for emergency session (GTP on S2b) [329](#a-initial-attach-for-emergency-session-gtp-on-s2b)

4.11.4.3.4 Interaction with PCC [329](#interaction-with-pcc)

4.11.4.3.5 UE initiated Connectivity to Additional PDN with GTP on S2b [330](#ue-initiated-connectivity-to-additional-pdn-with-gtp-on-s2b)

4.11.4.3.6 Use of N10 interface instead of S6b [330](#use-of-n10-interface-instead-of-s6b)

4.11.4.3.7 5GC NAS capability (re-)enabled and disabled [331](#gc-nas-capability-re-enabled-and-disabled)

4.11.5 Impacts to 5GC Procedures [331](#impacts-to-5gc-procedures)

4.11.5.1 General [331](#general-33)

4.11.5.2 Registration procedure [331](#registration-procedure)

4.11.5.3 UE Requested PDU Session Establishment procedure [332](#ue-requested-pdu-session-establishment-procedure)

4.11.5.4 UE or Network Requested PDU Session Modification procedure [334](#ue-or-network-requested-pdu-session-modification-procedure)

4.11.5.5 Xn based inter NG-RAN handover [334](#xn-based-inter-ng-ran-handover-1)

4.11.5.6 Inter NG-RAN node N2 based handover [335](#inter-ng-ran-node-n2-based-handover-1)

4.11.5.7 UE or Network Requested PDU Session Release procedure [335](#ue-or-network-requested-pdu-session-release-procedure)

4.11.5.8 Network Configuration [335](#network-configuration)

4.11.5.9 Network Slice Admission Control [335](#network-slice-admission-control)

4.11.5.9a Network Slice Admission Control in 5GS for maximum number of UE with at least one PDU session and one PDN connection [336](#a-network-slice-admission-control-in-5gs-for-maximum-number-of-ue-with-at-least-one-pdu-session-and-one-pdn-connection)

4.11.5.10 UE Policy Association control [337](#ue-policy-association-control)

4.11.5.10.1 UE Policy Association Establishment for URSP delivery in EPS [337](#ue-policy-association-establishment-for-ursp-delivery-in-eps)

4.11.6 Interworking for common network exposure [338](#interworking-for-common-network-exposure)

4.11.6.1 Subscription and Notification of availability or expected level of support of a service API [338](#subscription-and-notification-of-availability-or-expected-level-of-support-of-a-service-api)

4.11.6.2 Unsubscribing to N11otification of availability or expected level of support of a service API [339](#unsubscribing-to-n11otification-of-availability-or-expected-level-of-support-of-a-service-api)

4.11.6.3 Configuration of monitoring events for common network exposure [340](#configuration-of-monitoring-events-for-common-network-exposure)

4.12 Procedures for Untrusted non-3GPP access [341](#procedures-for-untrusted-non-3gpp-access)

4.12.1 General [341](#general-34)

4.12.2 Registration via Untrusted non-3GPP Access [341](#registration-via-untrusted-non-3gpp-access)

4.12.2.1 General [341](#general-35)

4.12.2.2 Registration procedure for untrusted non-3GPP access [341](#registration-procedure-for-untrusted-non-3gpp-access)

4.12.2.3 Emergency Registration for untrusted non-3GPP Access [345](#emergency-registration-for-untrusted-non-3gpp-access)

4.12.3 Deregistration procedure for untrusted non-3gpp access [346](#deregistration-procedure-for-untrusted-non-3gpp-access)

4.12.4 N2 procedures via Untrusted non-3GPP Access [347](#n2-procedures-via-untrusted-non-3gpp-access)

4.12.4.1 Service Request procedures via Untrusted non-3GPP Access [347](#service-request-procedures-via-untrusted-non-3gpp-access)

4.12.4.2 Procedure for the UE context release in the N3IWF [348](#procedure-for-the-ue-context-release-in-the-n3iwf)

4.12.4.3 CN-initiated selective deactivation of UP connection of an existing PDU Session associated with Untrusted non-3GPP Access [349](#cn-initiated-selective-deactivation-of-up-connection-of-an-existing-pdu-session-associated-with-untrusted-non-3gpp-access)

4.12.5 UE Requested PDU Session Establishment via Untrusted non-3GPP Access [349](#ue-requested-pdu-session-establishment-via-untrusted-non-3gpp-access)

4.12.6 UE or Network Requested PDU Session Modification via Untrusted non-3GPP access [351](#ue-or-network-requested-pdu-session-modification-via-untrusted-non-3gpp-access)

4.12.7 UE or network Requested PDU Session Release via Untrusted non-3GPP access [353](#ue-or-network-requested-pdu-session-release-via-untrusted-non-3gpp-access)

4.12.8 Mobility from a non-geographically selected AMF to a geographically selected AMF [355](#mobility-from-a-non-geographically-selected-amf-to-a-geographically-selected-amf)

4.12a Procedures for Trusted non-3GPP access [356](#a-procedures-for-trusted-non-3gpp-access)

4.12a.1 General [356](#a.1-general-1)

4.12a.2 Registration via Trusted non-3GPP Access [356](#a.2-registration-via-trusted-non-3gpp-access)

4.12a.2.1 General [356](#a.2.1-general)

4.12a.2.2 Registration procedure for trusted non-3GPP access [356](#a.2.2-registration-procedure-for-trusted-non-3gpp-access)

4.12a.2.3 Emergency Registration for trusted non-3GPP Access [360](#a.2.3-emergency-registration-for-trusted-non-3gpp-access)

4.12a.3 Deregistration procedure for Trusted non-3GPP access [360](#a.3-deregistration-procedure-for-trusted-non-3gpp-access)

4.12a.4 N2 procedures via Trusted non-3GPP Access [361](#a.4-n2-procedures-via-trusted-non-3gpp-access)

4.12a.4.1 Service Request procedures via Trusted non-3GPP Access [361](#a.4.1-service-request-procedures-via-trusted-non-3gpp-access)

4.12a.4.2 Procedure for the UE context release in the TNGF [361](#a.4.2-procedure-for-the-ue-context-release-in-the-tngf)

4.12a.4.3 CN-initiated selective deactivation of UP connection of an existing PDU Session associated with Trusted non-3GPP Access [361](#a.4.3-cn-initiated-selective-deactivation-of-up-connection-of-an-existing-pdu-session-associated-with-trusted-non-3gpp-access)

4.12a.5 UE Requested PDU Session Establishment via Trusted non-3GPP Access [361](#a.5-ue-requested-pdu-session-establishment-via-trusted-non-3gpp-access)

4.12a.6 UE or network Requested PDU Session Modification via Trusted non-3GPP access [362](#a.6-ue-or-network-requested-pdu-session-modification-via-trusted-non-3gpp-access)

4.12a.7 UE or network Requested PDU Session Release via Trusted non-3GPP access [363](#a.7-ue-or-network-requested-pdu-session-release-via-trusted-non-3gpp-access)

4.12a.8 Mobility from a non-geographically selected AMF to a geographically selected AMF [363](#a.8-mobility-from-a-non-geographically-selected-amf-to-a-geographically-selected-amf)

4.12a.9 Support of mobility from source to target TNAP [363](#a.9-support-of-mobility-from-source-to-target-tnap)

4.12b Procedures for devices that do not support 5GC NAS over WLAN access [363](#b-procedures-for-devices-that-do-not-support-5gc-nas-over-wlan-access)

4.12b.1 General [363](#b.1-general)

4.12b.2 Initial Registration & PDU Session Establishment [363](#b.2-initial-registration-pdu-session-establishment)

4.12b.3 Deregistration procedure [367](#b.3-deregistration-procedure)

4.12b.4 N2 procedures [367](#b.4-n2-procedures)

4.12b.4.1 Service Request procedures [367](#b.4.1-service-request-procedures)

4.12b.4.2 Procedure for the UE context release in the TWIF [367](#b.4.2-procedure-for-the-ue-context-release-in-the-twif)

4.12b.4.3 CN-initiated selective deactivation of UP connection of an existing PDU Session [368](#b.4.3-cn-initiated-selective-deactivation-of-up-connection-of-an-existing-pdu-session)

4.13 Specific services [368](#specific-services)

4.13.1 General [368](#general-36)

4.13.2 Application Triggering [368](#application-triggering)

4.13.2.1 General [368](#general-37)

4.13.2.2 The procedure of "Application Triggering" Service [369](#the-procedure-of-application-triggering-service)

4.13.3 SMS over NAS procedures [371](#sms-over-nas-procedures)

4.13.3.1 Registration procedures for SMS over NAS [371](#registration-procedures-for-sms-over-nas)

4.13.3.2 Deregistration procedures for SMS over NAS [372](#deregistration-procedures-for-sms-over-nas)

4.13.3.3 MO SMS over NAS in CM-IDLE (baseline) [373](#mo-sms-over-nas-in-cm-idle-baseline)

4.13.3.4 Void [374](#void-2)

4.13.3.5 MO SMS over NAS in CM-CONNECTED [374](#mo-sms-over-nas-in-cm-connected)

4.13.3.6 MT SMS over NAS in CM-IDLE state and RRC_INACTIVE with CN based MT communication state via 3GPP access [375](#mt-sms-over-nas-in-cm-idle-state-and-rrc_inactive-with-cn-based-mt-communication-state-via-3gpp-access)

4.13.3.7 MT SMS over NAS in CM-CONNECTED state via 3GPP access [376](#mt-sms-over-nas-in-cm-connected-state-via-3gpp-access)

4.13.3.8 MT SMS over NAS via non-3GPP access [376](#mt-sms-over-nas-via-non-3gpp-access)

4.13.3.9 Unsuccessful Mobile terminating SMS delivery re-attempt [376](#unsuccessful-mobile-terminating-sms-delivery-re-attempt)

4.13.4 Emergency Services [377](#emergency-services)

4.13.4.1 General [377](#general-38)

4.13.4.2 Emergency Services Fallback [377](#emergency-services-fallback)

4.13.5 Location Services procedures [379](#location-services-procedures)

4.13.5.0 General [379](#general-39)

4.13.5.1 5GC-NI-LR Procedure [379](#gc-ni-lr-procedure)

4.13.5.2 5GC-MT-LR Procedure without UDM Query [379](#gc-mt-lr-procedure-without-udm-query)

4.13.5.3 5GC-MT-LR Procedure [379](#gc-mt-lr-procedure)

4.13.5.4 UE Assisted and UE Based Positioning Procedure [379](#ue-assisted-and-ue-based-positioning-procedure)

4.13.5.5 Network Assisted Positioning Procedure [379](#network-assisted-positioning-procedure)

4.13.5.6 Obtaining Non-UE Associated Network Assistance Data [379](#obtaining-non-ue-associated-network-assistance-data)

4.13.5.7 Location continuity for Handover of an Emergency session from NG-RAN [379](#location-continuity-for-handover-of-an-emergency-session-from-ng-ran)

4.13.6 Support of IMS Voice [379](#support-of-ims-voice)

4.13.6.1 EPS fallback for IMS voice [379](#eps-fallback-for-ims-voice)

4.13.6.2 Inter RAT Fallback in 5GC for IMS voice [381](#inter-rat-fallback-in-5gc-for-ims-voice)

4.13.6.3 Transfer of PDU session used for IMS voice from non-3GPP access to 5GS [382](#transfer-of-pdu-session-used-for-ims-voice-from-non-3gpp-access-to-5gs)

4.13.7 MSISDN-less MO SMS [383](#msisdn-less-mo-sms)

4.13.7.1 General [383](#general-40)

4.13.7.2 The procedure of MSISDN-less MO SMS Service [384](#the-procedure-of-msisdn-less-mo-sms-service)

4.13.8 Support of 5G LAN-type service [385](#support-of-5g-lan-type-service)

4.13.8.1 Support of 5G VN group management [385](#support-of-5g-vn-group-management)

4.13.8.2 Support of 5G VN group communication [385](#support-of-5g-vn-group-communication)

4.13.8.2.1 General [385](#general-41)

4.13.8.2.2 group-level N4 session management procedures [385](#group-level-n4-session-management-procedures)

4.14 Support for Dual Connectivity [385](#support-for-dual-connectivity)

4.14.1 RAN Initiated QoS Flow Mobility [385](#ran-initiated-qos-flow-mobility)

4.15 Network Exposure [387](#network-exposure)

4.15.1 General [387](#general-42)

4.15.2 External Exposure of Network Capabilities [391](#external-exposure-of-network-capabilities)

4.15.2a Data Collection from an AF [391](#a-data-collection-from-an-af)

4.15.3 Event Exposure using NEF [392](#event-exposure-using-nef)

4.15.3.1 Monitoring Events [392](#monitoring-events)

4.15.3.2 Information flows [398](#information-flows)

4.15.3.2.1 AMF service operations information flow [398](#amf-service-operations-information-flow)

4.15.3.2.2 UDM service operations information flow [398](#udm-service-operations-information-flow)

4.15.3.2.3 NEF service operations information flow [401](#nef-service-operations-information-flow)

4.15.3.2.3a Void [405](#a-void)

4.15.3.2.3b Specific NEF service operations information flow for loss of connectivity and UE reachability [405](#b-specific-nef-service-operations-information-flow-for-loss-of-connectivity-and-ue-reachability)

4.15.3.2.3c Specific NEF service operations information flow for group member list change [407](#c-specific-nef-service-operations-information-flow-for-group-member-list-change)

4.15.3.2.4 Exposure with bulk subscription [407](#exposure-with-bulk-subscription)

4.15.3.2.5 Information flow for downlink data delivery status with SMF buffering [409](#information-flow-for-downlink-data-delivery-status-with-smf-buffering)

4.15.3.2.6 GMLC service operations information flow [410](#gmlc-service-operations-information-flow)

4.15.3.2.7 Information flow for Availability after DDN Failure with SMF buffering [410](#information-flow-for-availability-after-ddn-failure-with-smf-buffering)

4.15.3.2.8 Information flow for downlink data delivery status with UPF buffering [412](#information-flow-for-downlink-data-delivery-status-with-upf-buffering)

4.15.3.2.9 Information flow for Availability after DDN Failure with UPF buffering [413](#information-flow-for-availability-after-ddn-failure-with-upf-buffering)

4.15.3.2.10 Number of UEs and PDU Sessions per network slice notification procedure [415](#number-of-ues-and-pdu-sessions-per-network-slice-notification-procedure)

4.15.3.2.11 Network-initiated explicit event notification subscription cancel procedure [419](#network-initiated-explicit-event-notification-subscription-cancel-procedure)

4.15.3.2.12 Void [420](#void-3)

4.15.3.2.13 Handling AF requests when the UE is identified via UE addressing information [420](#handling-af-requests-when-the-ue-is-identified-via-ue-addressing-information)

4.15.3.3 Void [420](#void-4)

4.15.4 Core Network Internal Event Exposure [420](#core-network-internal-event-exposure)

4.15.4.1 General [420](#general-43)

4.15.4.2 Exposure of Mobility Events from AMF [421](#exposure-of-mobility-events-from-amf)

4.15.4.3 Exposure of Communication trends from SMF [422](#exposure-of-communication-trends-from-smf)

4.15.4.4 Internal Event Exposure Subscription/Unsubscription via UDM [423](#internal-event-exposure-subscriptionunsubscription-via-udm)

4.15.4.5 Exposure of Events from UPF for UPF Data Collection [424](#exposure-of-events-from-upf-for-upf-data-collection)

4.15.4.5.1 General [424](#general-44)

4.15.4.5.2 Information flow for subscription to UPF event exposure service for certain UE(s) via SMF [426](#information-flow-for-subscription-to-upf-event-exposure-service-for-certain-ues-via-smf)

4.15.4.5.3 Information flow for UPF event exposure service for any UE [427](#information-flow-for-upf-event-exposure-service-for-any-ue)

4.15.4.5.4 Information flow for subscription via SMF to UPF event exposure service related with AOI [428](#information-flow-for-subscription-via-smf-to-upf-event-exposure-service-related-with-aoi)

4.15.5 Void [429](#void-5)

4.15.6 External Parameter Provisioning [429](#external-parameter-provisioning)

4.15.6.1 General [429](#general-45)

4.15.6.2 NEF service operations information flow [430](#nef-service-operations-information-flow-1)

4.15.6.3 Expected UE Behaviour parameters [433](#expected-ue-behaviour-parameters)

4.15.6.3a Network Configuration parameters [434](#a-network-configuration-parameters)

4.15.6.3b 5G VN group data [435](#b-5g-vn-group-data)

4.15.6.3c 5G VN Group membership management parameters [436](#c-5g-vn-group-membership-management-parameters)

4.15.6.3d ECS Address Configuration Information Parameters [436](#d-ecs-address-configuration-information-parameters)

4.15.6.3e DNN and S-NSSAI specific Group Parameters [437](#e-dnn-and-s-nssai-specific-group-parameters)

4.15.6.3f Application-Specific Expected UE Behaviour parameters [437](#f-application-specific-expected-ue-behaviour-parameters)

4.15.6.3g Network Slice Usage Control parameters for dedicated S-NSSAI to a single AF [438](#g-network-slice-usage-control-parameters-for-dedicated-s-nssai-to-a-single-af)

4.15.6.4 Set a chargeable party at AF session setup [438](#set-a-chargeable-party-at-af-session-setup)

4.15.6.5 Change the chargeable party during the session [439](#change-the-chargeable-party-during-the-session)

4.15.6.6 Setting up an AF session with required QoS procedure [440](#setting-up-an-af-session-with-required-qos-procedure)

4.15.6.6a AF session with required QoS update procedure [444](#a-af-session-with-required-qos-update-procedure)

4.15.6.7 Service specific parameter provisioning [446](#service-specific-parameter-provisioning)

4.15.6.7.1 General [446](#general-46)

4.15.6.7.2 Service specific parameter provisioning by AF to HPLMN [446](#service-specific-parameter-provisioning-by-af-to-hplmn)

4.15.6.7.3 Service specific parameter provisioning by AF to VPLMN [448](#service-specific-parameter-provisioning-by-af-to-vplmn)

4.15.6.7a Authorization of service specific parameter provisioning [450](#a-authorization-of-service-specific-parameter-provisioning)

4.15.6.8 Set a policy for a future AF session [452](#set-a-policy-for-a-future-af-session)

4.15.6.9 Procedures for AF-triggered dynamically changing access and mobility management policies [452](#procedures-for-af-triggered-dynamically-changing-access-and-mobility-management-policies)

4.15.6.9.1 General [452](#general-47)

4.15.6.9.2 Processing AF requests to influence access and mobility management policies targeting an individual UE [453](#processing-af-requests-to-influence-access-and-mobility-management-policies-targeting-an-individual-ue)

4.15.6.9.3 Processing AF requests to influence access and mobility management policies [455](#processing-af-requests-to-influence-access-and-mobility-management-policies)

4.15.6.10 Application guidance for URSP determination [456](#application-guidance-for-ursp-determination)

4.15.6.11 Void [458](#void-6)

4.15.6.12 Parameter Provisioning when the UE is identified via UE addressing information [458](#parameter-provisioning-when-the-ue-is-identified-via-ue-addressing-information)

4.15.6.13 Multi-member AF session with required QoS [458](#multi-member-af-session-with-required-qos)

4.15.6.13.1 General Descriptions [458](#general-descriptions)

4.15.6.13.2 Procedures for Creating a Multi-member AF session with required QoS [460](#procedures-for-creating-a-multi-member-af-session-with-required-qos)

4.15.6.13.3 Procedure for updating a Multi-member AF session with required QoS [462](#procedure-for-updating-a-multi-member-af-session-with-required-qos)

4.15.6.13.4 Procedure for Revoking a Multi-member AF session with required QoS [464](#procedure-for-revoking-a-multi-member-af-session-with-required-qos)

4.15.6.14 Procedures for AF requested QoS for a UE or group of UEs not identified by a UE address [465](#procedures-for-af-requested-qos-for-a-ue-or-group-of-ues-not-identified-by-a-ue-address)

4.15.7 Network status reporting [466](#network-status-reporting)

4.15.8 Event exposure controlled by a DCCF [467](#event-exposure-controlled-by-a-dccf)

4.15.9 Time Synchronization exposure [467](#time-synchronization-exposure)

4.15.9.1 General [467](#general-48)

4.15.9.2 Exposure of UE availability for Time Synchronization service [467](#exposure-of-ue-availability-for-time-synchronization-service)

4.15.9.3 Time Synchronization activation, modification and deactivation [470](#time-synchronization-activation-modification-and-deactivation)

4.15.9.3.1 General [470](#general-49)

4.15.9.3.2 Time synchronization service activation [475](#time-synchronization-service-activation)

4.15.9.3.3 Time synchronization service modification [479](#time-synchronization-service-modification)

4.15.9.3.4 Time synchronization service deactivation [481](#time-synchronization-service-deactivation)

4.15.9.4 Procedures for management of 5G access stratum time distribution [481](#procedures-for-management-of-5g-access-stratum-time-distribution)

4.15.9.5 Procedures for subscription and management of network timing synchronization status monitoring [488](#procedures-for-subscription-and-management-of-network-timing-synchronization-status-monitoring)

4.15.9.5.1 Network timing synchronization status [488](#network-timing-synchronization-status)

4.15.9.5.2 5G access stratum time distribution status reporting to the UE [490](#g-access-stratum-time-distribution-status-reporting-to-the-ue)

4.15.10 AF specific UE ID retrieval [491](#af-specific-ue-id-retrieval)

4.15.10A MSISDN retrieval [492](#a-msisdn-retrieval)

4.15.11 Void [493](#void-7)

4.15.12 Event Exposure using Local NEF [493](#event-exposure-using-local-nef)

4.15.13 Assistance for Member UE selection [494](#assistance-for-member-ue-selection)

4.15.13.0 General [494](#general-50)

4.15.13.1 Member UE selection assistance subscribe and update procedure [494](#member-ue-selection-assistance-subscribe-and-update-procedure)

4.15.13.2 Member UE Filtering Criteria for 5GS assistance to Member UE selection [496](#member-ue-filtering-criteria-for-5gs-assistance-to-member-ue-selection)

4.15.13.3 Specific procedure for QoS Member UE filtering criteria [499](#specific-procedure-for-qos-member-ue-filtering-criteria)

4.15.13.3.1 General [499](#general-51)

4.15.13.3.2 Void [499](#void-8)

4.15.13.3.3 Member UE Selection Assistance with QoS filtering criteria for real-time QoS Monitoring [499](#member-ue-selection-assistance-with-qos-filtering-criteria-for-real-time-qos-monitoring)

4.15.13.4 Specific procedure for the 5GC assistance to member UE selection based on the UE's current location, historical location and direction and UE separation distance [502](#specific-procedure-for-the-5gc-assistance-to-member-ue-selection-based-on-the-ues-current-location-historical-location-and-direction-and-ue-separation-distance)

4.15.13.5 Specific procedure for Service Experience Member UE filtering criteria [503](#specific-procedure-for-service-experience-member-ue-filtering-criteria)

4.15.13.5.1 General [503](#general-52)

4.15.13.5.2 Member UE Selection Assistance with Service Experience filtering criteria [504](#member-ue-selection-assistance-with-service-experience-filtering-criteria)

4.15.13.6 Specific procedure for end-to-end data volume transfer time related member UE filtering criteria [505](#specific-procedure-for-end-to-end-data-volume-transfer-time-related-member-ue-filtering-criteria)

4.15.13.6.1 General [505](#general-53)

4.15.13.6.2 Member UE Selection assistance with end-to-end data volume transfer time related filtering criteria [506](#member-ue-selection-assistance-with-end-to-end-data-volume-transfer-time-related-filtering-criteria)

4.15.13.7 Member UE selection assistance unsubscribe procedure [507](#member-ue-selection-assistance-unsubscribe-procedure)

4.16 Procedures and flows for Policy Framework [507](#procedures-and-flows-for-policy-framework)

4.16.1 AM Policy Association Establishment [507](#am-policy-association-establishment)

4.16.1.1 General [507](#general-54)

4.16.1.2 AM Policy Association Establishment with new Selected PCF [508](#am-policy-association-establishment-with-new-selected-pcf)

4.16.1.3 Void [509](#void-9)

4.16.2 AM Policy Association Modification [509](#am-policy-association-modification)

4.16.2.0 General [509](#general-55)

4.16.2.1 AM Policy Association Modification initiated by the AMF [509](#am-policy-association-modification-initiated-by-the-amf)

4.16.2.1.1 AM Policy Association Modification initiated by the AMF without AMF relocation [509](#am-policy-association-modification-initiated-by-the-amf-without-amf-relocation)

4.16.2.1.2 AM Policy Association Modification with old PCF during AMF relocation [510](#am-policy-association-modification-with-old-pcf-during-amf-relocation)

4.16.2.2 AM Policy Association Modification initiated by the PCF [512](#am-policy-association-modification-initiated-by-the-pcf)

4.16.3 AM Policy Association Termination [513](#am-policy-association-termination)

4.16.3.1 General [513](#general-56)

4.16.3.2 AMF-initiated AM Policy Association Termination [513](#amf-initiated-am-policy-association-termination)

4.16.3.3 Void [514](#void-10)

4.16.4 SM Policy Association Establishment [514](#sm-policy-association-establishment)

4.16.5 SM Policy Association Modification [516](#sm-policy-association-modification)

4.16.5.0 General [516](#general-57)

4.16.5.1 SMF initiated SM Policy Association Modification [516](#smf-initiated-sm-policy-association-modification)

4.16.5.2 PCF initiated SM Policy Association Modification [518](#pcf-initiated-sm-policy-association-modification)

4.16.6 SM Policy Association Termination [520](#sm-policy-association-termination)

4.16.7 Negotiations for future background data transfer [521](#negotiations-for-future-background-data-transfer)

4.16.7.1 General [521](#general-58)

4.16.7.2 Procedures for future background data transfer [522](#procedures-for-future-background-data-transfer)

4.16.7.3 Procedure for BDT warning notification [524](#procedure-for-bdt-warning-notification)

4.16.8 Procedures on interaction between PCF and CHF [525](#procedures-on-interaction-between-pcf-and-chf)

4.16.8.1 General [525](#general-59)

4.16.8.2 Initial Spending Limit Retrieval [526](#initial-spending-limit-retrieval)

4.16.8.3 Intermediate Spending Limit Report Retrieval [526](#intermediate-spending-limit-report-retrieval)

4.16.8.4 Final Spending Limit Report Retrieval [527](#final-spending-limit-report-retrieval)

4.16.8.5 Spending Limit Report [528](#spending-limit-report)

4.16.8.6 CHF report the removal of the subscriber [528](#chf-report-the-removal-of-the-subscriber)

4.16.9 Update of the subscription information in the PCF [529](#update-of-the-subscription-information-in-the-pcf)

4.16.10 Void [530](#void-11)

4.16.11 UE Policy Association Establishment [530](#ue-policy-association-establishment)

4.16.11.1 General [530](#general-60)

4.16.12 UE Policy Association Modification [532](#ue-policy-association-modification)

4.16.12.1 UE Policy Association Modification initiated by the AMF [532](#ue-policy-association-modification-initiated-by-the-amf)

4.16.12.1.1 UE Policy Association Modification initiated by the AMF without AMF relocation [532](#ue-policy-association-modification-initiated-by-the-amf-without-amf-relocation)

4.16.12.1.2 UE Policy Association Modification with old PCF during AMF relocation [534](#ue-policy-association-modification-with-old-pcf-during-amf-relocation)

4.16.12.2 UE Policy Association Modification initiated by the PCF [535](#ue-policy-association-modification-initiated-by-the-pcf)

4.16.13 UE Policy Association Termination [536](#ue-policy-association-termination)

4.16.13.1 AMF-initiated UE Policy Association Termination [536](#amf-initiated-ue-policy-association-termination)

4.16.13.2 PCF-initiated UE Policy Association Termination [538](#pcf-initiated-ue-policy-association-termination)

4.16.14 Management of access and mobility related policy information depending on the application in use [539](#management-of-access-and-mobility-related-policy-information-depending-on-the-application-in-use)

4.16.14.1 General [539](#general-61)

4.16.14.2 Procedures for management of access and mobility related policy information [539](#procedures-for-management-of-access-and-mobility-related-policy-information)

4.16.14.2.1 Management of access and mobility related policy information at start and stop of application traffic [539](#management-of-access-and-mobility-related-policy-information-at-start-and-stop-of-application-traffic)

4.16.14.2.2 Management of access and mobility related policy information at SM Policy Association establishment and termination with the notification sent by the BSF [542](#management-of-access-and-mobility-related-policy-information-at-sm-policy-association-establishment-and-termination-with-the-notification-sent-by-the-bsf)

4.16.15 Negotiations for planned data transfer with QoS requirements [543](#negotiations-for-planned-data-transfer-with-qos-requirements)

4.16.15.1 General [543](#general-62)

4.16.15.2 Procedures [543](#procedures)

4.16.15.2.1 Procedures for negotiation of planned data transfer with QoS requirements [543](#procedures-for-negotiation-of-planned-data-transfer-with-qos-requirements)

4.16.15.2.2 Procedure for PDTQ warning notification [546](#procedure-for-pdtq-warning-notification)

4.16.16 Awareness of URSP Rule Enforcement [547](#awareness-of-ursp-rule-enforcement)

4.16.16.1 General [547](#general-63)

4.16.16.2 Forwarding of URSP Rule Enforcement Information (for non-roaming and HR roaming) [547](#forwarding-of-ursp-rule-enforcement-information-for-non-roaming-and-hr-roaming)

4.16.16.3 Forwarding of URSP Rule Enforcement Information (for LBO roaming) [549](#forwarding-of-ursp-rule-enforcement-information-for-lbo-roaming)

4.17 Network Function Service Framework Procedure [551](#network-function-service-framework-procedure)

4.17.1 NF service Registration [551](#nf-service-registration)

4.17.2 NF service update [552](#nf-service-update)

4.17.3 NF service deregistration [552](#nf-service-deregistration)

4.17.4 NF/NF service discovery by NF service consumer in the same PLMN [553](#nfnf-service-discovery-by-nf-service-consumer-in-the-same-plmn)

4.17.4a NF/NF service discovery by NF service consumer in the same SNPN [554](#a-nfnf-service-discovery-by-nf-service-consumer-in-the-same-snpn)

4.17.5 NF/NF service discovery across PLMNs in the case of discovery made by NF service consumer [554](#nfnf-service-discovery-across-plmns-in-the-case-of-discovery-made-by-nf-service-consumer)

4.17.5a NF/NF service discovery between SNPN and Credentials Holder hosting AUSF/UDM or between SNPN and DCS hosting AUSF/UDM [555](#a-nfnf-service-discovery-between-snpn-and-credentials-holder-hosting-ausfudm-or-between-snpn-and-dcs-hosting-ausfudm)

4.17.6 SMF Provisioning of available UPFs using the NRF [556](#smf-provisioning-of-available-upfs-using-the-nrf)

4.17.6.1 General [556](#general-64)

4.17.6.2 SMF provisioning of UPF instances using NRF [556](#smf-provisioning-of-upf-instances-using-nrf)

4.17.7 NF/NF service status subscribe/notify in the same PLMN [558](#nfnf-service-status-subscribenotify-in-the-same-plmn)

4.17.8 NF/NF service status subscribe/notify across PLMNs [558](#nfnf-service-status-subscribenotify-across-plmns)

4.17.9 Delegated service discovery when NF service consumer and NF service producer are in same PLMN [559](#delegated-service-discovery-when-nf-service-consumer-and-nf-service-producer-are-in-same-plmn)

4.17.10 Delegated service discovery when NF service consumer and NF service producer are in different PLMNs [561](#delegated-service-discovery-when-nf-service-consumer-and-nf-service-producer-are-in-different-plmns)

4.17.11 Indirect Communication without delegated discovery Procedure [561](#indirect-communication-without-delegated-discovery-procedure)

4.17.12 Binding between NF service consumer and NF service producer [562](#binding-between-nf-service-consumer-and-nf-service-producer)

4.17.12.1 General [562](#general-65)

4.17.12.2 Binding created as part of service response [562](#binding-created-as-part-of-service-response)

4.17.12.3 Binding created as part of service request [563](#binding-created-as-part-of-service-request)

4.17.12.4 Binding for subscription requests [564](#binding-for-subscription-requests)

4.17.13 NRF bootstrapping procedure [566](#nrf-bootstrapping-procedure)

4.18 Procedures for Management of PFDs [566](#procedures-for-management-of-pfds)

4.18.1 General [566](#general-66)

4.18.2 PFD management via NEF (PFDF) [566](#pfd-management-via-nef-pfdf)

4.18.2.1 PFD management triggered by AF [566](#pfd-management-triggered-by-af)

4.18.2.2 PFD management based on PFD Determination analytics [567](#pfd-management-based-on-pfd-determination-analytics)

4.18.3 PFD management in the SMF [568](#pfd-management-in-the-smf)

4.18.3.1 PFD Retrieval by the SMF [568](#pfd-retrieval-by-the-smf)

4.18.3.2 Management of PFDs in the SMF [568](#management-of-pfds-in-the-smf)

4.19 Network Data Analytics [569](#network-data-analytics)

4.19.1 Void [569](#void-12)

4.19.2 Void [569](#void-13)

4.20 UE Parameters Update via UDM Control Plane Procedure [569](#ue-parameters-update-via-udm-control-plane-procedure)

4.20.1 General [569](#general-67)

4.20.2 UE Parameters Update via UDM Control Plane Procedure [570](#ue-parameters-update-via-udm-control-plane-procedure-1)

4.20.3 Void [571](#void-14)

4.21 Secondary RAT Usage Data Reporting Procedure [571](#secondary-rat-usage-data-reporting-procedure)

4.22 ATSSS Procedures [572](#atsss-procedures)

4.22.1 General [572](#general-68)

4.22.2 UE Requested MA PDU Session Establishment [573](#ue-requested-ma-pdu-session-establishment)

4.22.2.0 Overview [573](#overview)

4.22.2.1 Non-roaming and Roaming with Local Breakout [573](#non-roaming-and-roaming-with-local-breakout-2)

4.22.2.2 Home-routed Roaming [575](#home-routed-roaming-2)

4.22.2.2.1 Home-routed Roaming - UE registered to the same PLMN [575](#home-routed-roaming---ue-registered-to-the-same-plmn)

4.22.2.2.2 Home-routed Roaming - UE registered to different PLMNs [576](#home-routed-roaming---ue-registered-to-different-plmns)

4.22.2.3 MA PDU Session establishment with 3GPP access connected to EPC and non-3GPP access connected to 5GC [577](#ma-pdu-session-establishment-with-3gpp-access-connected-to-epc-and-non-3gpp-access-connected-to-5gc)

4.22.2.3.1 General [577](#general-69)

4.22.2.3.2 PDN Connections and Multi Access PDU Sessions [578](#pdn-connections-and-multi-access-pdu-sessions)

4.22.2.3.3 QoS Support [579](#qos-support)

4.22.2.4 MA PDU Session establishment with non-3GPP access connected to EPC and 3GPP access connected to 5GC [579](#ma-pdu-session-establishment-with-non-3gpp-access-connected-to-epc-and-3gpp-access-connected-to-5gc)

4.22.2.4.1 General [579](#general-70)

4.22.2.4.2 PDN Connections and Multi Access PDU Sessions [580](#pdn-connections-and-multi-access-pdu-sessions-1)

4.22.2.4.3 QoS Support [581](#qos-support-1)

4.22.3 UE Requested PDU Session Establishment with Network Modification to MA PDU Session [581](#ue-requested-pdu-session-establishment-with-network-modification-to-ma-pdu-session)

4.22.3.1 Overview [581](#overview-1)

4.22.3.2 Non-roaming or roaming with local breakout [582](#non-roaming-or-roaming-with-local-breakout)

4.22.3.3 Home-routed, the UE registered to the same VPLMN over both access [582](#home-routed-the-ue-registered-to-the-same-vplmn-over-both-access)

4.22.3.4 Home-routed, the UE registered to different PLMNs over both access [583](#home-routed-the-ue-registered-to-different-plmns-over-both-access)

4.22.4 Access Network Performance Measurements [584](#access-network-performance-measurements)

4.22.5 Reporting of Access Availability [584](#reporting-of-access-availability)

4.22.5A Suspend and Resume Traffic Duplication [584](#a-suspend-and-resume-traffic-duplication)

4.22.6 EPS Interworking [585](#eps-interworking)

4.22.6.1 General [585](#general-71)

4.22.6.2 Impacts to EPS interworking procedures [585](#impacts-to-eps-interworking-procedures)

4.22.6.2.1 5GS to EPS handover using N26 interface [585](#gs-to-eps-handover-using-n26-interface-2)

4.22.6.2.2 5GS to EPS idle mode mobility using N26 interface [585](#gs-to-eps-idle-mode-mobility-using-n26-interface-1)

4.22.6.2.3 EPS bearer ID allocation [586](#eps-bearer-id-allocation-1)

4.22.6.2.4 EPS bearer ID revocation [586](#eps-bearer-id-revocation-1)

4.22.6.2.5 5GS to EPS mobility without N26 interface [586](#gs-to-eps-mobility-without-n26-interface)

4.22.6.3 Network Modification to MA PDU Session after a UE moving from EPC [587](#network-modification-to-ma-pdu-session-after-a-ue-moving-from-epc)

4.22.7 Adding / Re-activating / De-activating User-Plane Resources [588](#adding-re-activating-de-activating-user-plane-resources)

4.22.8 UE or network requested MA PDU Session Modification [588](#ue-or-network-requested-ma-pdu-session-modification)

4.22.8.1 General [588](#general-72)

4.22.8.2 UE or network requested MA PDU Session Modification (non-roaming and roaming with local breakout) [588](#ue-or-network-requested-ma-pdu-session-modification-non-roaming-and-roaming-with-local-breakout)

4.22.8.3 UE or network requested MA PDU Session Modification (home-routed roaming) [589](#ue-or-network-requested-ma-pdu-session-modification-home-routed-roaming)

4.22.9 Connection, Registration and Mobility Management procedures [590](#connection-registration-and-mobility-management-procedures-1)

4.22.9.1 Registration procedures [590](#registration-procedures-1)

4.22.9.2 UE Triggered Service Request [591](#ue-triggered-service-request-2)

4.22.9.3 N2 based handover [591](#n2-based-handover)

4.22.9.4 Network Triggered Service Request [591](#network-triggered-service-request-1)

4.22.9.5 Registration procedures for non-3GPP access path switching [592](#registration-procedures-for-non-3gpp-access-path-switching)

4.22.10 MA PDU Session Release [594](#ma-pdu-session-release)

4.22.10.1 General [594](#general-73)

4.22.10.2 UE or network requested MA PDU Session Release (non-roaming and roaming with local breakout) [595](#ue-or-network-requested-ma-pdu-session-release-non-roaming-and-roaming-with-local-breakout)

4.22.10.3 UE or network requested MA PDU Session Release (home-routed roaming) [595](#ue-or-network-requested-ma-pdu-session-release-home-routed-roaming)

4.23 Support of deployments topologies with specific SMF Service Areas [596](#support-of-deployments-topologies-with-specific-smf-service-areas)

4.23.1 General [596](#general-74)

4.23.2 I-SMF selection [597](#i-smf-selection)

4.23.3 Registration procedure [597](#registration-procedure-1)

4.23.3a Deregistration procedure [598](#a-deregistration-procedure)

4.23.4 Service Request procedures [599](#service-request-procedures-1)

4.23.4.1 General [599](#general-75)

4.23.4.2 UE Triggered Service Request without I-SMF change/removal [599](#ue-triggered-service-request-without-i-smf-changeremoval)

4.23.4.3 UE Triggered Service Request with I-SMF insertion/change/removal [599](#ue-triggered-service-request-with-i-smf-insertionchangeremoval)

4.23.4.4 Network Triggered Service Request [606](#network-triggered-service-request-2)

4.23.5 PDU Session Management procedure [606](#pdu-session-management-procedure)

4.23.5.1 PDU Session establishment procedure [606](#pdu-session-establishment-procedure)

4.23.5.2 PDU Session Release procedure [607](#pdu-session-release-procedure)

4.23.5.3 PDU Session modification procedure [607](#pdu-session-modification-procedure)

4.23.5.4 SMF triggered I-SMF selection or removal [608](#smf-triggered-i-smf-selection-or-removal)

4.23.6 I-SMF Related Procedures with PCF [609](#i-smf-related-procedures-with-pcf)

4.23.6.1 General [609](#general-76)

4.23.6.2 Policy Update Procedures with I-SMF [610](#policy-update-procedures-with-i-smf)

4.23.6.3 Reporting UP path change to the AF [610](#reporting-up-path-change-to-the-af)

4.23.7 Inter NG-RAN node N2 based handover [611](#inter-ng-ran-node-n2-based-handover-2)

4.23.7.1 General [611](#general-77)

4.23.7.2 Inter NG-RAN node N2 based handover without I-SMF change/removal [611](#inter-ng-ran-node-n2-based-handover-without-i-smf-changeremoval)

4.23.7.2.1 General [611](#general-78)

4.23.7.2.2 Preparation phase [611](#preparation-phase-2)

4.23.7.2.3 Execution phase [611](#execution-phase-2)

4.23.7.2.4 Handover Cancel [611](#handover-cancel-1)

4.23.7.3 Inter NG-RAN node N2 based handover with I-SMF insertion/change/removal [612](#inter-ng-ran-node-n2-based-handover-with-i-smf-insertionchangeremoval)

4.23.7.3.1 General [612](#general-79)

4.23.7.3.2 Preparation phase [613](#preparation-phase-3)

4.23.7.3.3 Execution phase [619](#execution-phase-3)

4.23.7.3.4 Handover Cancel [623](#handover-cancel-2)

4.23.8 AN Release procedure involving I-SMF [625](#an-release-procedure-involving-i-smf)

4.23.9 Branching Point or UL CL controlled by I-SMF [625](#branching-point-or-ul-cl-controlled-by-i-smf)

4.23.9.0 Overview [625](#overview-2)

4.23.9.1 Addition of PDU Session Anchor and Branching Point or UL CL controlled by I-SMF [626](#addition-of-pdu-session-anchor-and-branching-point-or-ul-cl-controlled-by-i-smf)

4.23.9.2 Removal of PDU Session Anchor and Branching Point or UL CL controlled by I-SMF [629](#removal-of-pdu-session-anchor-and-branching-point-or-ul-cl-controlled-by-i-smf)

4.23.9.3 Change of PDU Session Anchor for IPv6 multi-homing or UL CL controlled by I-SMF [630](#change-of-pdu-session-anchor-for-ipv6-multi-homing-or-ul-cl-controlled-by-i-smf)

4.23.9.4 Simultaneous change of Branching Point or UL CL and additional PSA controlled by I-SMF [632](#simultaneous-change-of-branching-point-or-ul-cl-and-additional-psa-controlled-by-i-smf)

4.23.9.5 Simultaneous change of Branching Points or UL CLs controlled by different I-SMFs [634](#simultaneous-change-of-branching-points-or-ul-cls-controlled-by-different-i-smfs)

4.23.9a Void [637](#a-void-1)

4.23.10 CN-initiated selective deactivation of UP connection of an existing PDU Session involving I-SMF [637](#cn-initiated-selective-deactivation-of-up-connection-of-an-existing-pdu-session-involving-i-smf)

4.23.11 Xn based handover [637](#xn-based-handover)

4.23.11.1 General [637](#general-80)

4.23.11.2 Xn based handover with insertion of intermediate SMF [637](#xn-based-handover-with-insertion-of-intermediate-smf)

4.23.11.3 Xn based handover with re-allocation of intermediate SMF [639](#xn-based-handover-with-re-allocation-of-intermediate-smf)

4.23.11.4 Xn based handover with removal of intermediate SMF [641](#xn-based-handover-with-removal-of-intermediate-smf)

4.23.11.5 Xn based handover without change of intermediate SMF [643](#xn-based-handover-without-change-of-intermediate-smf)

4.23.12 N26 based Interworking Procedures with I-SMF [643](#n26-based-interworking-procedures-with-i-smf)

4.23.12.1 General [643](#general-81)

4.23.12.2 5GS to EPS Idle mode mobility using N26 interface with I-SMF removal [643](#gs-to-eps-idle-mode-mobility-using-n26-interface-with-i-smf-removal)

4.23.12.2A 5GS to EPS Idle mode mobility using N26 interface with Data forwarding and I-SMF removal [643](#a-5gs-to-eps-idle-mode-mobility-using-n26-interface-with-data-forwarding-and-i-smf-removal)

4.23.12.3 EPS to 5GS mobility registration procedure (Idle and Connected State) using N26 interface with I-SMF insertion [643](#eps-to-5gs-mobility-registration-procedure-idle-and-connected-state-using-n26-interface-with-i-smf-insertion)

4.23.12.3A EPS to 5GS Idle mode mobility using N26 interface with Data forwarding and I-SMF insertion [644](#a-eps-to-5gs-idle-mode-mobility-using-n26-interface-with-data-forwarding-and-i-smf-insertion)

4.23.12.4 Procedures for EPS bearer ID allocation [644](#procedures-for-eps-bearer-id-allocation-1)

4.23.12.5 EPS to 5GS mobility registration procedure (Idle) using N26 interface with AMF reallocation and I-SMF insertion [644](#eps-to-5gs-mobility-registration-procedure-idle-using-n26-interface-with-amf-reallocation-and-i-smf-insertion)

4.23.12.6 5GS to EPS handover using N26 interface with I-SMF removal [644](#gs-to-eps-handover-using-n26-interface-with-i-smf-removal)

4.23.12.7 EPS to 5GS handover using N26 interface with I-SMF insertion [644](#eps-to-5gs-handover-using-n26-interface-with-i-smf-insertion)

4.23.12.7.1 Preparation phase [644](#preparation-phase-4)

4.23.12.7.2 Execution phase [645](#execution-phase-4)

4.23.12.8 Impact to 5GC procedures [645](#impact-to-5gc-procedures)

4.23.12.8.1 General [645](#general-82)

4.23.12.8.2 UE Triggered Service Request with I-SMF insertion/change/removal [645](#ue-triggered-service-request-with-i-smf-insertionchangeremoval-1)

4.23.12.8.3 PDU Session establishment procedure [645](#pdu-session-establishment-procedure-1)

4.23.12.8.4 PDU Session modification procedure [645](#pdu-session-modification-procedure-1)

4.23.12.8.5 Inter NG-RAN node N2 based handover with I-SMF insertion/change/removal [645](#inter-ng-ran-node-n2-based-handover-with-i-smf-insertionchangeremoval-1)

4.23.12.8.6 Xn based handover with insertion of I-SMF [646](#xn-based-handover-with-insertion-of-i-smf)

4.23.13 Non N26 based Interworking Procedures with I-SMF [646](#non-n26-based-interworking-procedures-with-i-smf)

4.23.13.1 General [646](#general-83)

4.23.13.2 Mobility procedure without N26 interface from EPS to 5GS [646](#mobility-procedure-without-n26-interface-from-eps-to-5gs)

4.23.13.3 Mobility procedure without N26 interface from EPC/ePDG to 5GS [646](#mobility-procedure-without-n26-interface-from-epcepdg-to-5gs)

4.23.13.4 Mobility procedure without N26 interface from 5GS to EPS [646](#mobility-procedure-without-n26-interface-from-5gs-to-eps)

4.23.13.5 Mobility procedure without N26 interface from 5GS to EPC/ePDG [646](#mobility-procedure-without-n26-interface-from-5gs-to-epcepdg)

4.23.14 Pause of charging [647](#pause-of-charging)

4.23.15 PDU Session mobility between 3GPP and non-3GPP access [647](#pdu-session-mobility-between-3gpp-and-non-3gpp-access)

4.23.16 Handover of a PDU Session procedure between 3GPP and untrusted non-3GPP access [647](#handover-of-a-pdu-session-procedure-between-3gpp-and-untrusted-non-3gpp-access-1)

4.23.16.1 Handover of a PDU Session procedure from untrusted non-3GPP to 3GPP access (non-roaming and roaming with local breakout) [647](#handover-of-a-pdu-session-procedure-from-untrusted-non-3gpp-to-3gpp-access-non-roaming-and-roaming-with-local-breakout-1)

4.23.16.2 Handover of a PDU Session procedure from 3GPP to untrusted non-3GPP access (non-roaming and roaming with local breakout) [647](#handover-of-a-pdu-session-procedure-from-3gpp-to-untrusted-non-3gpp-access-non-roaming-and-roaming-with-local-breakout-1)

4.23.16.3 Handover of a PDU Session procedure from untrusted non-3GPP to 3GPP access (home routed roaming) [648](#handover-of-a-pdu-session-procedure-from-untrusted-non-3gpp-to-3gpp-access-home-routed-roaming-1)

4.23.16.3.1 The target AMF is in the PLMN of the N3IWF [648](#the-target-amf-is-in-the-plmn-of-the-n3iwf-1)

4.23.16a Handover of a PDU Session procedure between 3GPP and trusted non-3GPP access [648](#a-handover-of-a-pdu-session-procedure-between-3gpp-and-trusted-non-3gpp-access)

4.23.16a.1 General [648](#a.1-general-2)

4.23.17 Additional considerations for Home-routed roaming [648](#additional-considerations-for-home-routed-roaming)

4.24 Procedures for UPF Anchored Data Transport in Control Plane CIoT 5GS Optimisation [649](#procedures-for-upf-anchored-data-transport-in-control-plane-ciot-5gs-optimisation)

4.24.1 UPF anchored Mobile Originated Data Transport in Control Plane CIoT 5GS Optimisation [649](#upf-anchored-mobile-originated-data-transport-in-control-plane-ciot-5gs-optimisation)

4.24.2 UPF anchored Mobile Terminated Data Transport in Control Plane CIoT 5GS Optimisation [652](#upf-anchored-mobile-terminated-data-transport-in-control-plane-ciot-5gs-optimisation)

4.25 Procedures for NEF based Non-IP Data Delivery [657](#procedures-for-nef-based-non-ip-data-delivery)

4.25.1 General [657](#general-84)

4.25.2 SMF-NEF Connection Establishment [657](#smf-nef-connection-establishment)

4.25.3 NIDD Configuration [658](#nidd-configuration)

4.25.4 NEF Anchored Mobile Originated Data Transport [660](#nef-anchored-mobile-originated-data-transport)

4.25.5 NEF Anchored Mobile Terminated Data Transport [661](#nef-anchored-mobile-terminated-data-transport)

4.25.6 NIDD Authorization Update [664](#nidd-authorization-update)

4.25.7 SMF Initiated SMF-NEF Connection Release procedure [665](#smf-initiated-smf-nef-connection-release-procedure)

4.25.8 NEF Initiated SMF-NEF Connection Release procedure [665](#nef-initiated-smf-nef-connection-release-procedure)

4.25.9 NEF Anchored Group NIDD via NEF anchored unicast MT data [667](#nef-anchored-group-nidd-via-nef-anchored-unicast-mt-data)

4.26 Network Function/NF Service Context Transfer Procedures [667](#network-functionnf-service-context-transfer-procedures)

4.26.1 General [667](#general-85)

4.26.2 NF/NF Service Context Transfer Push Procedure [668](#nfnf-service-context-transfer-push-procedure)

4.26.3 NF/NF Service Context Transfer Pull procedure [668](#nfnf-service-context-transfer-pull-procedure)

4.26.4 Context Transfer due to decommissioning [669](#context-transfer-due-to-decommissioning)

4.26.5 SMF Service Context Transfer procedures [669](#smf-service-context-transfer-procedures)

4.26.5.1 General [669](#general-86)

4.26.5.2 I-SMF Context Transfer procedure [669](#i-smf-context-transfer-procedure)

4.26.5.3 SMF Context Transfer procedure, LBO or no Roaming, no I-SMF [669](#smf-context-transfer-procedure-lbo-or-no-roaming-no-i-smf)

4.27 Procedures for Enhanced Coverage Restriction Control via NEF [672](#procedures-for-enhanced-coverage-restriction-control-via-nef)

4.27.1 General [672](#general-87)

4.28 Subscription-based distribution of timing information [673](#subscription-based-distribution-of-timing-information)

4.28.1 General [673](#general-88)

4.28.2 5G Access Stratum-based Time Distribution [673](#g-access-stratum-based-time-distribution)

4.28.2.1 Control of access stratum time synchronization service without AF request [673](#control-of-access-stratum-time-synchronization-service-without-af-request)

4.28.3 (g)PTP-based Time Distribution [674](#gptp-based-time-distribution)

4.28.3.1 Control of (g)PTP time synchronization service without AF request [674](#control-of-gptp-time-synchronization-service-without-af-request)

5 Network Function Service procedures [676](#network-function-service-procedures)

5.1 Network Function Service framework procedures [676](#network-function-service-framework-procedures)

5.1.1 Network Function Service Discovery [676](#network-function-service-discovery)

5.2 Network Function services [676](#network-function-services)

5.2.1 General [676](#general-89)

5.2.2 AMF Services [676](#amf-services)

5.2.2.1 General [676](#general-90)

5.2.2.2 Namf_Communication service [677](#namf_communication-service)

5.2.2.2.1 General [677](#general-91)

5.2.2.2.2 Namf_Communication_UEContextTransfer service operation [678](#namf_communication_uecontexttransfer-service-operation)

5.2.2.2.3 Namf_Communication_RegistrationStatusUpdate service operation [683](#namf_communication_registrationstatusupdate-service-operation)

5.2.2.2.4 Namf_Communication_N1MessageNotify service operation [684](#namf_communication_n1messagenotify-service-operation)

5.2.2.2.5 Namf_Communication_N1N2MessageSubscribe service operation [684](#namf_communication_n1n2messagesubscribe-service-operation)

5.2.2.2.6 Namf_Communication_N1N2MessageUnSubscribe service operation [684](#namf_communication_n1n2messageunsubscribe-service-operation)

5.2.2.2.7 Namf_Communication_N1N2MessageTransfer service operation [685](#namf_communication_n1n2messagetransfer-service-operation)

5.2.2.2.7A Namf_Communication_N1N2TransferFailureNotification service operation [686](#a-namf_communication_n1n2transferfailurenotification-service-operation)

5.2.2.2.8 Namf_Communication_N2InfoSubscribe service operation [686](#namf_communication_n2infosubscribe-service-operation)

5.2.2.2.9 Namf_Communication_N2InfoUnsubscribe service operation [686](#namf_communication_n2infounsubscribe-service-operation)

5.2.2.2.10 Namf_Communication_N2InfoNotify service operation [686](#namf_communication_n2infonotify-service-operation)

5.2.2.2.11 Namf_Communication_CreateUEContext service operation [687](#namf_communication_createuecontext-service-operation)

5.2.2.2.12 Namf_Communication_ReleaseUEContext service operation [687](#namf_communication_releaseuecontext-service-operation)

5.2.2.2.13 Namf_Communication_EBIAssignment service operation [687](#namf_communication_ebiassignment-service-operation)

5.2.2.2.14 Namf_Communication_AMFStatusChangeSubscribe service operation [688](#namf_communication_amfstatuschangesubscribe-service-operation)

5.2.2.2.15 Namf_Communication_AMFStatusChangeUnSubscribe service operation [688](#namf_communication_amfstatuschangeunsubscribe-service-operation)

5.2.2.2.16 Namf_Communication_AMFStatusChangeNotify service operation [688](#namf_communication_amfstatuschangenotify-service-operation)

5.2.2.2.17 Namf_Communication_NonUeN2MessageTransfer service operation [688](#namf_communication_nonuen2messagetransfer-service-operation)

5.2.2.2.18 Namf_Communication_NonUeN2InfoSubscribe service operation [689](#namf_communication_nonuen2infosubscribe-service-operation)

5.2.2.2.19 Namf_Communication_NonUeN2InfoUnSubscribe service operation [689](#namf_communication_nonuen2infounsubscribe-service-operation)

5.2.2.2.20 Namf_Communication_NonUeN2InfoNotify service operation [689](#namf_communication_nonuen2infonotify-service-operation)

5.2.2.2.21 Namf_Communication_RelocateUEContext service operation [689](#namf_communication_relocateuecontext-service-operation)

5.2.2.2.22 Namf_Communication_CancelRelocateUEContext service operation [690](#namf_communication_cancelrelocateuecontext-service-operation)

5.2.2.3 Namf_EventExposure service [690](#namf_eventexposure-service)

5.2.2.3.1 General [690](#general-92)

5.2.2.3.2 Namf_EventExposure_Subscribe service operation [692](#namf_eventexposure_subscribe-service-operation)

5.2.2.3.3 Namf_EventExposure_UnSubscribe service operation [693](#namf_eventexposure_unsubscribe-service-operation)

5.2.2.3.4 Namf_EventExposure_Notify service operation [693](#namf_eventexposure_notify-service-operation)

5.2.2.4 Namf_MT service [694](#namf_mt-service)

5.2.2.4.1 General [694](#general-93)

5.2.2.4.2 Namf_MT_EnableUEReachability service operation [694](#namf_mt_enableuereachability-service-operation)

5.2.2.4.3 Namf_MT_ProvideDomainSelectionInfo [695](#namf_mt_providedomainselectioninfo)

5.2.2.4.4 Namf_MT_EnableGroupReachability service operation [695](#namf_mt_enablegroupreachability-service-operation)

5.2.2.4.5 Namf_MT_UEReachabilityInfoNotify [695](#namf_mt_uereachabilityinfonotify)

5.2.2.5 Namf_Location service [695](#namf_location-service)

5.2.2.5.1 General [695](#general-94)

5.2.2.5.2 Namf_Location_ProvidePositioningInfo service operation [696](#namf_location_providepositioninginfo-service-operation)

5.2.2.5.3 Namf_Location_EventNotify service operation [696](#namf_location_eventnotify-service-operation)

5.2.2.5.4 Namf_Location_ProvideLocationInfo service operation [696](#namf_location_providelocationinfo-service-operation)

5.2.2.5.5 Namf_Location_CancelLocation service operation [697](#namf_location_cancellocation-service-operation)

5.2.3 UDM Services [697](#udm-services)

5.2.3.1 General [697](#general-95)

5.2.3.2 Nudm_UECM (UECM) service [698](#nudm_uecm-uecm-service)

5.2.3.2.1 Nudm_UECM_Registration service operation [698](#nudm_uecm_registration-service-operation)

5.2.3.2.2 Nudm_UECM_DeregistrationNotification service operation [699](#nudm_uecm_deregistrationnotification-service-operation)

5.2.3.2.3 Nudm_UECM_Deregistration service operation [700](#nudm_uecm_deregistration-service-operation)

5.2.3.2.4 Nudm_UECM_Get service operation [700](#nudm_uecm_get-service-operation)

5.2.3.2.5 Nudm_UECM_Update service operation [700](#nudm_uecm_update-service-operation)

5.2.3.2.6 Nudm_UECM_PCscfRestoration service operation [701](#nudm_uecm_pcscfrestoration-service-operation)

5.2.3.2.7 Nudm_UECM_SendRoutingInfoForSM service operation [701](#nudm_uecm_sendroutinginfoforsm-service-operation)

5.2.3.3 Nudm_SubscriberDataManagement (SDM) Service [701](#nudm_subscriberdatamanagement-sdm-service)

5.2.3.3.1 General [701](#general-96)

5.2.3.3.2 Nudm_SDM_Get service operation [714](#nudm_sdm_get-service-operation)

5.2.3.3.3 Nudm_SDM_Notification service operation [714](#nudm_sdm_notification-service-operation)

5.2.3.3.4 Nudm_SDM_Subscribe service operation [715](#nudm_sdm_subscribe-service-operation)

5.2.3.3.5 Nudm_SDM_Unsubscribe service operation [715](#nudm_sdm_unsubscribe-service-operation)

5.2.3.3.6 Nudm_SDM_Info service operation [715](#nudm_sdm_info-service-operation)

5.2.3.3.7 Void [716](#void-15)

5.2.3.3.8 Nudm_SDM_ModifySubscription service operation [716](#nudm_sdm_modifysubscription-service-operation)

5.2.3.4 Nudm_UEAuthentication Service [716](#nudm_ueauthentication-service)

5.2.3.4.1 General [716](#general-97)

5.2.3.4.2 Nudm_UEAuthentication_Get service operation [716](#nudm_ueauthentication_get-service-operation)

5.2.3.4.3 Nudm_UEAuthentication_ResultConfirmation service operation [716](#nudm_ueauthentication_resultconfirmation-service-operation)

5.2.3.5 Nudm_EventExposure service [716](#nudm_eventexposure-service)

5.2.3.5.1 General [716](#general-98)

5.2.3.5.2 Nudm_EventExposure_Subscribe service operation [716](#nudm_eventexposure_subscribe-service-operation)

5.2.3.5.3 Nudm_EventExposure_Unsubscribe service operation [717](#nudm_eventexposure_unsubscribe-service-operation)

5.2.3.5.4 Nudm_EventExposure_Notify service operation [717](#nudm_eventexposure_notify-service-operation)

5.2.3.5.5 Nudm_EventExposure_ModifySubscription service operation [717](#nudm_eventexposure_modifysubscription-service-operation)

5.2.3.6 Nudm_ParameterProvision service [717](#nudm_parameterprovision-service)

5.2.3.6.1 General [717](#general-99)

5.2.3.6.2 Nudm_ParameterProvision_Update service operation [719](#nudm_parameterprovision_update-service-operation)

5.2.3.6.3 Nudm_ParameterProvision_Create service operation [719](#nudm_parameterprovision_create-service-operation)

5.2.3.6.4 Nudm_ParameterProvision_Delete service operation [720](#nudm_parameterprovision_delete-service-operation)

5.2.3.6.5 Nudm_ParameterProvision_Get service operation [720](#nudm_parameterprovision_get-service-operation)

5.2.3.7 Nudm_NIDDAuthorisation service [720](#nudm_niddauthorisation-service)

5.2.3.7.1 General [720](#general-100)

5.2.3.7.2 Nudm_NIDDAuthorisation_Get service operation [720](#nudm_niddauthorisation_get-service-operation)

5.2.3.7.3 Nudm_NIDDAuthorisation_UpdateNotify service operation [721](#nudm_niddauthorisation_updatenotify-service-operation)

5.2.3.7.4 Void [721](#void-16)

5.2.3.7.5 Void [721](#void-17)

5.2.3.8 Nudm_ServiceSpecificAuthorisation service [721](#nudm_servicespecificauthorisation-service)

5.2.3.8.1 General [721](#general-101)

5.2.3.8.2 Nudm_ServiceSpecificAuthorisation_Create service operation [721](#nudm_servicespecificauthorisation_create-service-operation)

5.2.3.8.3 Nudm_ServiceSpecificAuthorisation_UpdateNotify service operation [721](#nudm_servicespecificauthorisation_updatenotify-service-operation)

5.2.3.8.4 Nudm_ServiceSpecificAuthorisation_Remove service operation [722](#nudm_servicespecificauthorisation_remove-service-operation)

5.2.3.9 Nudm_ReportSMDeliveryStatus service [722](#nudm_reportsmdeliverystatus-service)

5.2.3.9.1 General [722](#general-102)

5.2.3.9.2 Nudm_ReportSMDeliveryStatus_Request service operation [722](#nudm_reportsmdeliverystatus_request-service-operation)

5.2.4 5G-EIR Services [722](#g-eir-services)

5.2.4.1 General [722](#general-103)

5.2.4.2 N5g-eir_EquipmentIdentityCheck service [722](#n5g-eir_equipmentidentitycheck-service)

5.2.4.2.1 General [722](#general-104)

5.2.4.2.2 N5g-eir_EquipmentIdentityCheck_Get service operation [722](#n5g-eir_equipmentidentitycheck_get-service-operation)

5.2.5 PCF Services [723](#pcf-services)

5.2.5.1 General [723](#general-105)

5.2.5.2 Npcf_AMPolicyControl service [724](#npcf_ampolicycontrol-service)

5.2.5.2.1 General [724](#general-106)

5.2.5.2.2 Npcf_AMPolicyControl_Create service operation [725](#npcf_ampolicycontrol_create-service-operation)

5.2.5.2.3 Npcf_AMPolicyControl_UpdateNotify service operation [725](#npcf_ampolicycontrol_updatenotify-service-operation)

5.2.5.2.4 Npcf_AMPolicyControl_Delete service operation [726](#npcf_ampolicycontrol_delete-service-operation)

5.2.5.2.5 Npcf_AMPolicyControl_Update service operation [726](#npcf_ampolicycontrol_update-service-operation)

5.2.5.3 Npcf_PolicyAuthorization Service [726](#npcf_policyauthorization-service)

5.2.5.3.1 General [726](#general-107)

5.2.5.3.2 Npcf_PolicyAuthorization_Create service operation [726](#npcf_policyauthorization_create-service-operation)

5.2.5.3.3 Npcf_PolicyAuthorization_Update service operation [727](#npcf_policyauthorization_update-service-operation)

5.2.5.3.4 Npcf_PolicyAuthorization_Delete service operation [728](#npcf_policyauthorization_delete-service-operation)

5.2.5.3.5 Npcf_PolicyAuthorization_Notify service operation [728](#npcf_policyauthorization_notify-service-operation)

5.2.5.3.6 Npcf_PolicyAuthorization_Subscribe service operation [729](#npcf_policyauthorization_subscribe-service-operation)

5.2.5.3.7 Npcf_PolicyAuthorization_Unsubscribe service operation [729](#npcf_policyauthorization_unsubscribe-service-operation)

5.2.5.4 Npcf_SMPolicyControl service [729](#npcf_smpolicycontrol-service)

5.2.5.4.1 General [729](#general-108)

5.2.5.4.2 Npcf_SMPolicyControl_Create service operation [730](#npcf_smpolicycontrol_create-service-operation)

5.2.5.4.3 Npcf_SMPolicyControl_UpdateNotify service operation [730](#npcf_smpolicycontrol_updatenotify-service-operation)

5.2.5.4.4 Npcf_SMPolicyControl_Delete service operation [731](#npcf_smpolicycontrol_delete-service-operation)

5.2.5.4.5 Npcf_SMPolicyControl_Update service operation [731](#npcf_smpolicycontrol_update-service-operation)

5.2.5.5 Npcf_BDTPolicyControl Service [731](#npcf_bdtpolicycontrol-service)

5.2.5.5.1 General [731](#general-109)

5.2.5.5.2 Npcf_BDTPolicyControl_Create service operation [731](#npcf_bdtpolicycontrol_create-service-operation)

5.2.5.5.3 Npcf_BDTPolicyControl_Update service operation [732](#npcf_bdtpolicycontrol_update-service-operation)

5.2.5.5.4 Npcf_BDTPolicyControl_Notify service operation [732](#npcf_bdtpolicycontrol_notify-service-operation)

5.2.5.6 Npcf_UEPolicyControl Service [732](#npcf_uepolicycontrol-service)

5.2.5.6.1 General [732](#general-110)

5.2.5.6.2 Npcf_UEPolicyControl_Create service operation [733](#npcf_uepolicycontrol_create-service-operation)

5.2.5.6.3 Npcf_UEPolicyControl_UpdateNotify service operation [733](#npcf_uepolicycontrol_updatenotify-service-operation)

5.2.5.6.4 Npcf_UEPolicyControl_Delete service operation [734](#npcf_uepolicycontrol_delete-service-operation)

5.2.5.6.5 Npcf_UEPolicyControl_Update service operation [734](#npcf_uepolicycontrol_update-service-operation)

5.2.5.7 Npcf_EventExposure service [734](#npcf_eventexposure-service)

5.2.5.7.1 General [734](#general-111)

5.2.5.7.2 Npcf_EventExposure_Subscribe service operation [734](#npcf_eventexposure_subscribe-service-operation)

5.2.5.7.3 Npcf_EventExposure_Unsubscribe service operation [735](#npcf_eventexposure_unsubscribe-service-operation)

5.2.5.7.4 Npcf_EventExposure_Notify service operation [735](#npcf_eventexposure_notify-service-operation)

5.2.5.8 Npcf_AMPolicyAuthorization Service [736](#npcf_ampolicyauthorization-service)

5.2.5.8.1 General [736](#general-112)

5.2.5.8.2 Npcf_AMPolicyAuthorization_Create service operation [736](#npcf_ampolicyauthorization_create-service-operation)

5.2.5.8.3 Npcf_AMPolicyAuthorization_Update service operation [736](#npcf_ampolicyauthorization_update-service-operation)

5.2.5.8.4 Npcf_AMPolicyAuthorization_Delete service operation [736](#npcf_ampolicyauthorization_delete-service-operation)

5.2.5.8.5 Npcf_AMPolicyAuthorization_Notify service operation [737](#npcf_ampolicyauthorization_notify-service-operation)

5.2.5.8.6 Npcf_AMPolicyAuthorization_Subscribe service operation [737](#npcf_ampolicyauthorization_subscribe-service-operation)

5.2.5.8.7 Npcf_AMPolicyAuthorization_Unsubscribe service operation [737](#npcf_ampolicyauthorization_unsubscribe-service-operation)

5.2.5.9 Npcf_PDTQPolicyControl Service [737](#npcf_pdtqpolicycontrol-service)

5.2.5.9.1 General [737](#general-113)

5.2.5.9.2 Npcf_PDTQPolicyControl_Create service operation [737](#npcf_pdtqpolicycontrol_create-service-operation)

5.2.5.9.3 Npcf_PDTQPolicyControl_Update service operation [738](#npcf_pdtqpolicycontrol_update-service-operation)

5.2.5.9.4 Npcf_PDTQPolicyControl_Notify service operation [738](#npcf_pdtqpolicycontrol_notify-service-operation)

5.2.6 NEF Services [738](#nef-services)

5.2.6.1 General [738](#general-114)

5.2.6.2 Nnef_EventExposure service [742](#nnef_eventexposure-service)

5.2.6.2.1 General [742](#general-115)

5.2.6.2.2 Nnef_EventExposure_Subscribe operation [742](#nnef_eventexposure_subscribe-operation)

5.2.6.2.3 Nnef_EventExposure_Unsubscribe service operation [743](#nnef_eventexposure_unsubscribe-service-operation)

5.2.6.2.4 Nnef_EventExposure_Notify service operation [743](#nnef_eventexposure_notify-service-operation)

5.2.6.3 Nnef_PFDManagement service [743](#nnef_pfdmanagement-service)

5.2.6.3.1 General [743](#general-116)

5.2.6.3.2 Nnef_PFDManagement_Fetch service operation [743](#nnef_pfdmanagement_fetch-service-operation)

5.2.6.3.3 Nnef_PFDManagement_Subscribe service operation [743](#nnef_pfdmanagement_subscribe-service-operation)

5.2.6.3.4 Nnef_PFDManagement_Notify service operation [744](#nnef_pfdmanagement_notify-service-operation)

5.2.6.3.5 Nnef_PFDManagement_Unsubscribe service operation [744](#nnef_pfdmanagement_unsubscribe-service-operation)

5.2.6.3.6 Nnef_PFDManagement_Create service operation [744](#nnef_pfdmanagement_create-service-operation)

5.2.6.3.7 Nnef_PFDManagement_Update service operation [744](#nnef_pfdmanagement_update-service-operation)

5.2.6.3.8 Nnef_PFDManagement_Delete service operation [744](#nnef_pfdmanagement_delete-service-operation)

5.2.6.4 Nnef_ParameterProvision service [745](#nnef_parameterprovision-service)

5.2.6.4.1 General [745](#general-117)

5.2.6.4.2 Nnef_ParameterProvision_Update service operation [745](#nnef_parameterprovision_update-service-operation)

5.2.6.4.3 Nnef_ParameterProvision_Create service operation [745](#nnef_parameterprovision_create-service-operation)

5.2.6.4.4 Nnef_ParameterProvision_Delete service operation [745](#nnef_parameterprovision_delete-service-operation)

5.2.6.4.5 Nnef_ParameterProvision_Get service operation [746](#nnef_parameterprovision_get-service-operation)

5.2.6.5 Nnef_Trigger service [746](#nnef_trigger-service)

5.2.6.5.1 General [746](#general-118)

5.2.6.5.2 Nnef_Trigger_Delivery service operation [746](#nnef_trigger_delivery-service-operation)

5.2.6.5.3 Nnef_Trigger_DeliveryNotify service operation [746](#nnef_trigger_deliverynotify-service-operation)

5.2.6.6 Nnef_BDTPNegotiation service [746](#nnef_bdtpnegotiation-service)

5.2.6.6.1 General [746](#general-119)

5.2.6.6.2 Nnef_BDTPNegotiation_Create service operation [747](#nnef_bdtpnegotiation_create-service-operation)

5.2.6.6.3 Nnef_BDTPNegotiation_Update service operation [747](#nnef_bdtpnegotiation_update-service-operation)

5.2.6.6.4 Nnef_BDTPNegotiation_Notify service operation [747](#nnef_bdtpnegotiation_notify-service-operation)

5.2.6.7 Nnef_TrafficInfluence service [747](#nnef_trafficinfluence-service)

5.2.6.7.1 General [747](#general-120)

5.2.6.7.2 Nnef_TrafficInfluence_Create operation [747](#nnef_trafficinfluence_create-operation)

5.2.6.7.3 Nnef_TrafficInfluence_Update operation [748](#nnef_trafficinfluence_update-operation)

5.2.6.7.4 Nnef_TrafficInfluence_Delete operation [748](#nnef_trafficinfluence_delete-operation)

5.2.6.7.4A Nnef_TrafficInfluence_Get operation [749](#a-nnef_trafficinfluence_get-operation)

5.2.6.7.5 Nnef_TrafficInfluence_Notify operation [749](#nnef_trafficinfluence_notify-operation)

5.2.6.7.6 Nnef_TrafficInfluence_AppRelocationInfo operation [749](#nnef_trafficinfluence_apprelocationinfo-operation)

5.2.6.8 Nnef_ChargeableParty service [749](#nnef_chargeableparty-service)

5.2.6.8.1 General [749](#general-121)

5.2.6.8.2 Nnef_ChargeableParty_Create service operation [750](#nnef_chargeableparty_create-service-operation)

5.2.6.8.3 Nnef_ChargeableParty_Update service operation [750](#nnef_chargeableparty_update-service-operation)

5.2.6.8.4 Nnef_ChargeableParty_Notify service operation [750](#nnef_chargeableparty_notify-service-operation)

5.2.6.9 Nnef_AFsessionWithQoS service [750](#nnef_afsessionwithqos-service)

5.2.6.9.1 General [750](#general-122)

5.2.6.9.2 Nnef_AFsessionWithQoS_Create service operation [750](#nnef_afsessionwithqos_create-service-operation)

5.2.6.9.3 Nnef_AFsessionWithQoS_Notify service operation [751](#nnef_afsessionwithqos_notify-service-operation)

5.2.6.9.4 Nnef_AFsessionWithQoS_Revoke service operation [752](#nnef_afsessionwithqos_revoke-service-operation)

5.2.6.9.5 Nnef_AFsessionWithQoS_Update service operation [752](#nnef_afsessionwithqos_update-service-operation)

5.2.6.10 Nnef_MSISDN-less_MO_SMS service [753](#nnef_msisdn-less_mo_sms-service)

5.2.6.10.1 General [753](#general-123)

5.2.6.10.2 Nnef_MSISDN-less_MO_SMSNotify service operation [753](#nnef_msisdn-less_mo_smsnotify-service-operation)

5.2.6.11 Nnef_ServiceParameter service [753](#nnef_serviceparameter-service)

5.2.6.11.1 General [753](#general-124)

5.2.6.11.2 Nnef_ServiceParameter_Create operation [753](#nnef_serviceparameter_create-operation)

5.2.6.11.3 Nnef_ServiceParameter_Update operation [753](#nnef_serviceparameter_update-operation)

5.2.6.11.4 Nnef_ServiceParameter_Delete operation [754](#nnef_serviceparameter_delete-operation)

5.2.6.11.5 Nnef_ServiceParameter_Get operation [754](#nnef_serviceparameter_get-operation)

5.2.6.11.6 Nnef_ServiceParameter_Notify operation [754](#nnef_serviceparameter_notify-operation)

5.2.6.12 Nnef_APISupportCapability service [755](#nnef_apisupportcapability-service)

5.2.6.12.1 General [755](#general-125)

5.2.6.12.2 Nnef_APISupportCapability_Subscribe service operation [755](#nnef_apisupportcapability_subscribe-service-operation)

5.2.6.12.3 Nnef_APISupportCapability_Notify service operation [755](#nnef_apisupportcapability_notify-service-operation)

5.2.6.12.4 Nnef_APISupportCapability_Unsubscribe service operation [755](#nnef_apisupportcapability_unsubscribe-service-operation)

5.2.6.13 Nnef_NIDDConfiguration service [755](#nnef_niddconfiguration-service)

5.2.6.13.1 General [755](#general-126)

5.2.6.13.2 Nnef_NIDDConfiguration_Create service operation [756](#nnef_niddconfiguration_create-service-operation)

5.2.6.13.3 Nnef_NIDDConfiguration_TriggerNotify service operation [756](#nnef_niddconfiguration_triggernotify-service-operation)

5.2.6.13.4 Nnef_NIDDConfiguration_UpdateNotify service operation [756](#nnef_niddconfiguration_updatenotify-service-operation)

5.2.6.13.5 Nnef_NIDDConfiguration_Delete service operation [756](#nnef_niddconfiguration_delete-service-operation)

5.2.6.14 Nnef_NIDD service [756](#nnef_nidd-service)

5.2.6.14.1 General [756](#general-127)

5.2.6.14.2 Nnef_NIDD_Delivery service operation [756](#nnef_nidd_delivery-service-operation)

5.2.6.14.3 Nnef_NIDD_DeliveryNotify service operation [757](#nnef_nidd_deliverynotify-service-operation)

5.2.6.14.4 Nnef_NIDD_GroupDeliveryNotify service operation [757](#nnef_nidd_groupdeliverynotify-service-operation)

5.2.6.15 Nnef_SMContext service [757](#nnef_smcontext-service)

5.2.6.15.1 General [757](#general-128)

5.2.6.15.2 Nnef_SMContext_Create service operation [757](#nnef_smcontext_create-service-operation)

5.2.6.15.3 Nnef_SMContext_Delete service operation [757](#nnef_smcontext_delete-service-operation)

5.2.6.15.4 Nnef_SMContext_DeleteNotify service operation [758](#nnef_smcontext_deletenotify-service-operation)

5.2.6.15.5 Nnef_SMContext_Delivery service operation [758](#nnef_smcontext_delivery-service-operation)

5.2.6.16 Nnef_AnalyticsExposure service [758](#nnef_analyticsexposure-service)

5.2.6.16.1 General [758](#general-129)

5.2.6.16.2 Nnef_AnalyticsExposure_Subscribe operation [758](#nnef_analyticsexposure_subscribe-operation)

5.2.6.16.3 Nnef_AnalyticsExposure_Unsubscribe service operation [758](#nnef_analyticsexposure_unsubscribe-service-operation)

5.2.6.16.4 Nnef_AnalyticsExposure_Notify service operation [759](#nnef_analyticsexposure_notify-service-operation)

5.2.6.16.5 Nnef_AnalyticsExposure_Fetch service operation [759](#nnef_analyticsexposure_fetch-service-operation)

5.2.6.17 Nnef_UCMFProvisioning service [759](#nnef_ucmfprovisioning-service)

5.2.6.17.1 General [759](#general-130)

5.2.6.17.2 Nnef_UCMFProvisioning_Create operation [759](#nnef_ucmfprovisioning_create-operation)

5.2.6.17.3 Nnef_UCMFProvisioning_Delete operation [760](#nnef_ucmfprovisioning_delete-operation)

5.2.6.17.4 Nnef_UCMFProvisioning_Update operation [760](#nnef_ucmfprovisioning_update-operation)

5.2.6.18 Nnef_ECRestriction service [760](#nnef_ecrestriction-service)

5.2.6.18.1 General [760](#general-131)

5.2.6.18.2 Nnef_ECRestriction_Get service operation [760](#nnef_ecrestriction_get-service-operation)

5.2.6.18.3 Nnef_ECRestriction_Update service operation [761](#nnef_ecrestriction_update-service-operation)

5.2.6.19 Nnef_ApplyPolicy service [761](#nnef_applypolicy-service)

5.2.6.19.1 General [761](#general-132)

5.2.6.19.2 Nnef_ApplyPolicy_Create service operation [761](#nnef_applypolicy_create-service-operation)

5.2.6.19.3 Nnef_ApplyPolicy_Update service operation [761](#nnef_applypolicy_update-service-operation)

5.2.6.19.4 Nnef_ApplyPolicy_Delete service operation [761](#nnef_applypolicy_delete-service-operation)

5.2.6.20 Void [762](#void-18)

5.2.6.21 Nnef_Location service [762](#nnef_location-service)

5.2.6.21.1 General [762](#general-133)

5.2.6.21.2 Nnef_Location_LocationUpdateNotify service operation [762](#nnef_location_locationupdatenotify-service-operation)

5.2.6.22 Nnef_AMPolicyAuthorization Service [762](#nnef_ampolicyauthorization-service)

5.2.6.22.1 General [762](#general-134)

5.2.6.22.2 Nnef_AMPolicyAuthorization_Create service operation [762](#nnef_ampolicyauthorization_create-service-operation)

5.2.6.22.3 Nnef_AMPolicyAuthorization_Update service operation [762](#nnef_ampolicyauthorization_update-service-operation)

5.2.6.22.4 Nnef_AMPolicyAuthorization_Delete service operation [763](#nnef_ampolicyauthorization_delete-service-operation)

5.2.6.22.5 Nnef_AMPolicyAuthorization_Notify service operation [763](#nnef_ampolicyauthorization_notify-service-operation)

5.2.6.22.6 Nnef_AMPolicyAuthorization_Subscribe service operation [763](#nnef_ampolicyauthorization_subscribe-service-operation)

5.2.6.22.7 Nnef_AMPolicyAuthorization_Unsubscribe service operation [763](#nnef_ampolicyauthorization_unsubscribe-service-operation)

5.2.6.23 Nnef_AMInfluence service [764](#nnef_aminfluence-service)

5.2.6.23.1 General [764](#general-135)

5.2.6.23.2 Nnef_AMInfluence_Create operation [764](#nnef_aminfluence_create-operation)

5.2.6.23.3 Nnef_AMInfluence_Update operation [764](#nnef_aminfluence_update-operation)

5.2.6.23.4 Nnef_AMInfluence_Delete operation [764](#nnef_aminfluence_delete-operation)

5.2.6.23.6 Nnef_AMInfluence_Notify operation [765](#nnef_aminfluence_notify-operation)

5.2.6.24 Void [765](#void-19)

5.2.6.25 Nnef_TimeSynchronization service [765](#nnef_timesynchronization-service)

5.2.6.25.1 General [765](#general-136)

5.2.6.25.2 Nnef_TimeSynchronization_ConfigCreate operation [765](#nnef_timesynchronization_configcreate-operation)

5.2.6.25.3 Nnef_TimeSynchronization_ConfigUpdate operation [766](#nnef_timesynchronization_configupdate-operation)

5.2.6.25.4 Nnef_TimeSynchronization_ConfigDelete operation [766](#nnef_timesynchronization_configdelete-operation)

5.2.6.25.5 Nnef_TimeSynchronization_ConfigUpdateNotify operation [766](#nnef_timesynchronization_configupdatenotify-operation)

5.2.6.25.6 Nnef_TimeSynchronization_CapsSubscribe operation [766](#nnef_timesynchronization_capssubscribe-operation)

5.2.6.25.7 Nnef_TimeSynchronization_CapsUnsubscribe operation [767](#nnef_timesynchronization_capsunsubscribe-operation)

5.2.6.25.8 Nnef_TimeSynchronization_CapsNotify operation [767](#nnef_timesynchronization_capsnotify-operation)

5.2.6.25.9 Void [767](#void-20)

5.2.6.25.10 Void [767](#void-21)

5.2.6.25.11 Void [767](#void-22)

5.2.6.25.12 Void [767](#void-23)

5.2.6.26 Nnef_EASDeployment service [768](#nnef_easdeployment-service)

5.2.6.26.1 General [768](#general-137)

5.2.6.26.2 Nnef_EASDeployment_Create service operation [768](#nnef_easdeployment_create-service-operation)

5.2.6.26.3 Nnef_EASDeployment_Update service operation [768](#nnef_easdeployment_update-service-operation)

5.2.6.26.4 Nnef_EASDeployment_Delete service operation [768](#nnef_easdeployment_delete-service-operation)

5.2.6.26.5 Void [768](#void-24)

5.2.6.26.6 Nnef_EASDeployment_Subscribe service operation [768](#nnef_easdeployment_subscribe-service-operation)

5.2.6.26.7 Nnef_EASDeployment_Unsubscribe service operation [769](#nnef_easdeployment_unsubscribe-service-operation)

5.2.6.26.8 Nnef_EASDeployment_Notify service operation [769](#nnef_easdeployment_notify-service-operation)

5.2.6.27 Nnef_UEId service [769](#nnef_ueid-service)

5.2.6.27.1 General [769](#general-138)

5.2.6.27.2 Nnef_UEId_Get operation [769](#nnef_ueid_get-operation)

5.2.6.27.3 Nnef_UEId_UeIdMappingGet operation [770](#nnef_ueid_ueidmappingget-operation)

5.2.6.27.4 Nnef_UEId_UeIdMappingCreate operation [770](#nnef_ueid_ueidmappingcreate-operation)

5.2.6.27.5 Nnef_UEId_UeIdMappingUpdate operation [770](#nnef_ueid_ueidmappingupdate-operation)

5.2.6.27.6 Nnef_UEId_UeIdMappingDelete operation [770](#nnef_ueid_ueidmappingdelete-operation)

5.2.6.28 Nnef_ASTI service [771](#nnef_asti-service)

5.2.6.28.1 General [771](#general-139)

5.2.6.28.2 Nnef_ASTI_Create operation [771](#nnef_asti_create-operation)

5.2.6.28.3 Nnef_ASTI_Update operation [771](#nnef_asti_update-operation)

5.2.6.28.4 Nnef_ASTI_Delete operation [771](#nnef_asti_delete-operation)

5.2.6.28.5 Nnef_ASTI_Get operation [771](#nnef_asti_get-operation)

5.2.6.28.6 Nnef_ASTI_UpdateNotify operation [772](#nnef_asti_updatenotify-operation)

5.2.6.28.7 Void [772](#void-25)

5.2.6.28.8 Void [772](#void-26)

5.2.6.29 Nnef_SMService service [772](#nnef_smservice-service)

5.2.6.29.1 General [772](#general-140)

5.2.6.29.2 Nnef_SMService_MoForwardSm service operation [772](#nnef_smservice_moforwardsm-service-operation)

5.2.6.30 Nnef_PDTQPolicyNegotiation service [772](#nnef_pdtqpolicynegotiation-service)

5.2.6.30.1 General [772](#general-141)

5.2.6.30.2 Nnef_PDTQPolicyNegotiation_Create service operation [773](#nnef_pdtqpolicynegotiation_create-service-operation)

5.2.6.30.3 Nnef_PDTQPolicyNegotiation_Update service operation [773](#nnef_pdtqpolicynegotiation_update-service-operation)

5.2.6.30.4 Nnef_PDTQPolicyNegotiation_Notify service operation [773](#nnef_pdtqpolicynegotiation_notify-service-operation)

5.2.6.31 Void [773](#void-27)

5.2.6.32 Nnef_MemberUESelectionAssistance service [773](#nnef_memberueselectionassistance-service)

5.2.6.32.1 General [773](#general-142)

5.2.6.32.2 Nnef_MemberUESelectionAssistance_Subscribe service operation [773](#nnef_memberueselectionassistance_subscribe-service-operation)

5.2.6.32.3 Nnef_MemberUESelectionAssistance_Unsubscribe service operation [774](#nnef_memberueselectionassistance_unsubscribe-service-operation)

5.2.6.32.4 Nnef_MemberUESelectionAssistance_Notify service operation [774](#nnef_memberueselectionassistance_notify-service-operation)

5.2.6.33 Nnef_AF_request_for_QoS service [774](#nnef_af_request_for_qos-service)

5.2.6.33.1 General [774](#general-143)

5.2.6.33.2 Nnef_AF_request_for_QoS_Create service operation [775](#nnef_af_request_for_qos_create-service-operation)

5.2.6.33.3 Nnef_AF_request_for_QoS_Notify service operation [775](#nnef_af_request_for_qos_notify-service-operation)

5.2.6.33.4 Nnef_AF_request_for_QoS_Revoke service operation [775](#nnef_af_request_for_qos_revoke-service-operation)

5.2.6.33.5 Nnef_AF_request_for_QoS_Update service operation [775](#nnef_af_request_for_qos_update-service-operation)

5.2.6.34 Nnef_DNAIMapping service [776](#nnef_dnaimapping-service)

5.2.6.34.1 General [776](#general-144)

5.2.6.34.2 Nnef_DNAIMapping_Subscribe service operation [776](#nnef_dnaimapping_subscribe-service-operation)

5.2.6.34.3 Nnef_DNAIMapping_Unsubscribe service operation [776](#nnef_dnaimapping_unsubscribe-service-operation)

5.2.6.34.4 Nnef_DNAIMapping_UpdateNotify service operation [776](#nnef_dnaimapping_updatenotify-service-operation)

5.2.6.35 Nnef TrafficInfluenceData service [777](#nnef-trafficinfluencedata-service)

5.2.6.35.1 General [777](#general-145)

5.2.6.35.2 Nnef_TrafficInfluenceData_Subscribe operation [777](#nnef_trafficinfluencedata_subscribe-operation)

5.2.6.35.3 Nnef_TrafficInfluenceData_Unsubscribe service operation [777](#nnef_trafficinfluencedata_unsubscribe-service-operation)

5.2.6.35.4 Nnef_TrafficInfluenceData_Notify service operation [777](#nnef_trafficinfluencedata_notify-service-operation)

5.2.6.36 Nnef_UEAddress service [777](#nnef_ueaddress-service)

5.2.6.36.1 General [777](#general-146)

5.2.6.36.2 Nnef_UEAddress_Get operation [777](#nnef_ueaddress_get-operation)

5.2.6.37 Nnef_ECSAddress service [778](#nnef_ecsaddress-service)

5.2.6.37.1 General [778](#general-147)

5.2.6.37.2 Nnef_ECSAddress_Create service operation [778](#nnef_ecsaddress_create-service-operation)

5.2.6.37.3 Nnef_ECSAddress_Update service operation [778](#nnef_ecsaddress_update-service-operation)

5.2.6.37.4 Nnef_ECSAddress_Delete service operation [778](#nnef_ecsaddress_delete-service-operation)

5.2.6.37.5 Nnef_ECSAddress_Subscribe service operation [779](#nnef_ecsaddress_subscribe-service-operation)

5.2.6.37.6 Nnef_ECSAddress_Unsubscribe service operation [779](#nnef_ecsaddress_unsubscribe-service-operation)

5.2.6.37.7 Nnef_ECSAddress_Notify service operation [779](#nnef_ecsaddress_notify-service-operation)

5.2.6.38 Void [779](#void-28)

5.2.6A Void [779](#a-void-2)

5.2.7 NRF Services [780](#nrf-services)

5.2.7.1 General [780](#general-148)

5.2.7.2 Nnrf_NFManagement service [780](#nnrf_nfmanagement-service)

5.2.7.2.1 General [780](#general-149)

5.2.7.2.2 Nnrf_NFManagement_NFRegister service operation [781](#nnrf_nfmanagement_nfregister-service-operation)

5.2.7.2.3 Nnrf_NFManagement_NFUpdate service operation [784](#nnrf_nfmanagement_nfupdate-service-operation)

5.2.7.2.4 Nnrf_NFManagement_NFDeregister service operation [784](#nnrf_nfmanagement_nfderegister-service-operation)

5.2.7.2.5 Nnrf_NFManagement_NFStatusSubscribe service operation [784](#nnrf_nfmanagement_nfstatussubscribe-service-operation)

5.2.7.2.6 Nnrf_NFManagement_NFStatusNotify service operation [786](#nnrf_nfmanagement_nfstatusnotify-service-operation)

5.2.7.2.7 Nnrf_NFManagement_NFStatusUnsubscribe service operation [786](#nnrf_nfmanagement_nfstatusunsubscribe-service-operation)

5.2.7.3 Nnrf_NFDiscovery service [786](#nnrf_nfdiscovery-service)

5.2.7.3.1 General [786](#general-150)

5.2.7.3.2 Nnrf_NFDiscovery_Request service operation [786](#nnrf_nfdiscovery_request-service-operation)

5.2.7.4 Nnrf_AccessToken_service [792](#nnrf_accesstoken_service)

5.2.7.4.1 General [792](#general-151)

5.2.7.4.2 Nnrf_AccessToken_Get Service Operation [792](#nnrf_accesstoken_get-service-operation)

5.2.7.5 Nnrf_Bootstrapping service [792](#nnrf_bootstrapping-service)

5.2.7.5.1 General [792](#general-152)

5.2.7.5.2 Nnrf_Bootstrapping_Get service operation [792](#nnrf_bootstrapping_get-service-operation)

5.2.8 SMF Services [792](#smf-services)

5.2.8.1 General [792](#general-153)

5.2.8.2 Nsmf_PDUSession Service [793](#nsmf_pdusession-service)

5.2.8.2.1 General [793](#general-154)

5.2.8.2.2 Nsmf_PDUSession_Create service operation [794](#nsmf_pdusession_create-service-operation)

5.2.8.2.3 Nsmf_PDUSession_Update service operation [795](#nsmf_pdusession_update-service-operation)

5.2.8.2.4 Nsmf_PDUSession_Release service operation [796](#nsmf_pdusession_release-service-operation)

5.2.8.2.5 Nsmf_PDUSession_CreateSMContext service operation [796](#nsmf_pdusession_createsmcontext-service-operation)

5.2.8.2.6 Nsmf_PDUSession_UpdateSMContext service operation [797](#nsmf_pdusession_updatesmcontext-service-operation)

5.2.8.2.7 Nsmf_PDUSession_ReleaseSMContext service operation [798](#nsmf_pdusession_releasesmcontext-service-operation)

5.2.8.2.8 Nsmf_PDUSession_SMContextStatusNotify service operation [799](#nsmf_pdusession_smcontextstatusnotify-service-operation)

5.2.8.2.9 Nsmf_PDUSession_StatusNotify service operation [799](#nsmf_pdusession_statusnotify-service-operation)

5.2.8.2.10 Nsmf_PDUSession_ContextRequest service operation [799](#nsmf_pdusession_contextrequest-service-operation)

5.2.8.2.11 Nsmf_PDUSession_ContextPush service operation [803](#nsmf_pdusession_contextpush-service-operation)

5.2.8.2.12 Nsmf_PDUSession_SendMOData service operation [803](#nsmf_pdusession_sendmodata-service-operation)

5.2.8.2.13 Nsmf_PDUSession_TransferMOData service operation [804](#nsmf_pdusession_transfermodata-service-operation)

5.2.8.2.14 Nsmf_PDUSession_TransferMTData service operation [804](#nsmf_pdusession_transfermtdata-service-operation)

5.2.8.3 Nsmf_EventExposure Service [804](#nsmf_eventexposure-service)

5.2.8.3.1 General [804](#general-155)

5.2.8.3.2 Nsmf_EventExposure_Notify service operation [808](#nsmf_eventexposure_notify-service-operation)

5.2.8.3.2A Nsmf_EventExposure_AppRelocationInfo service operation [808](#a-nsmf_eventexposure_apprelocationinfo-service-operation)

5.2.8.3.3 Nsmf_EventExposure_Subscribe service operation [809](#nsmf_eventexposure_subscribe-service-operation)

5.2.8.3.4 Nsmf_EventExposure_UnSubscribe service operation [809](#nsmf_eventexposure_unsubscribe-service-operation)

5.2.8.4 Nsmf_NIDD Service [809](#nsmf_nidd-service)

5.2.8.4.1 General [809](#general-156)

5.2.8.4.2 Nsmf_NIDD_Delivery service operation [809](#nsmf_nidd_delivery-service-operation)

5.2.8.5 Nsmf_TrafficCorrelation service [810](#nsmf_trafficcorrelation-service)

5.2.8.5.1 General [810](#general-157)

5.2.8.5.2 Nsmf_TrafficCorrelation_Notify service operation [810](#nsmf_trafficcorrelation_notify-service-operation)

5.2.9 SMSF Services [810](#smsf-services)

5.2.9.1 General [810](#general-158)

5.2.9.2 Nsmsf_SMService service [810](#nsmsf_smservice-service)

5.2.9.2.1 General [810](#general-159)

5.2.9.2.2 Nsmsf_SMService_Activate service operation [810](#nsmsf_smservice_activate-service-operation)

5.2.9.2.3 Nsmsf_SMService_Deactivate service operation [811](#nsmsf_smservice_deactivate-service-operation)

5.2.9.2.4 Nsmsf_SMService_UplinkSMS service operation [811](#nsmsf_smservice_uplinksms-service-operation)

5.2.9.2.5 Nsmsf_SMService_MtForwardSm service operation [811](#nsmsf_smservice_mtforwardsm-service-operation)

5.2.10 AUSF Services [811](#ausf-services)

5.2.10.1 General [811](#general-160)

5.2.10.2 Nausf_UEAuthentication service [812](#_Toc232749468)

5.2.10.2.1 General [812](#general-161)

5.2.10.2.2 Nausf_UEAuthentication_Authenticate service operation [812](#nausf_ueauthentication_authenticate-service-operation)

5.2.10.2.3 Void [812](#void-29)

5.2.10.3 Nausf_SoRProtection service [812](#nausf_sorprotection-service)

5.2.10.3.1 General [812](#general-162)

5.2.10.3.2 Nausf_SoRProtection Protect service operation [812](#nausf_sorprotection-protect-service-operation)

5.2.10.4 Nausf_UPUProtection service [812](#nausf_upuprotection-service)

5.2.10.4.1 General [812](#general-163)

5.2.10.4.2 Nausf_UPUProtection Protect service operation [812](#nausf_upuprotection-protect-service-operation)

5.2.10.5 Void [812](#void-30)

5.2.11 NWDAF Services [812](#nwdaf-services)

5.2.11.1 Void [812](#void-31)

5.2.11.2 Void [813](#void-32)

5.2.11.3 Void [813](#void-33)

5.2.12 UDR Services [813](#udr-services)

5.2.12.1 General [813](#general-164)

5.2.12.2 Nudr_DataManagement (DM) service [814](#_Toc232749485)

5.2.12.2.1 General [814](#general-165)

5.2.12.2.2 Nudr_DM_Query service operation [820](#nudr_dm_query-service-operation)

5.2.12.2.3 Nudr_DM_Create service operation [820](#nudr_dm_create-service-operation)

5.2.12.2.4 Nudr_DM_Delete service operation [820](#nudr_dm_delete-service-operation)

5.2.12.2.5 Nudr_DM_Update service operation [820](#nudr_dm_update-service-operation)

5.2.12.2.6 Nudr_DM_Subscribe service operation [821](#nudr_dm_subscribe-service-operation)

5.2.12.2.7 Nudr_DM_Unsubscribe service operation [821](#nudr_dm_unsubscribe-service-operation)

5.2.12.2.8 Nudr_DM_Notify service operation [821](#nudr_dm_notify-service-operation)

5.2.12.3 Nudr_GroupIDmap service [821](#nudr_groupidmap-service)

5.2.12.3.1 General [821](#general-166)

5.2.12.3.2 Nudr_GroupIDmap_query service operation [821](#nudr_groupidmap_query-service-operation)

5.2.13 BSF Services [822](#bsf-services)

5.2.13.1 General [822](#general-167)

5.2.13.2 Nbsf_Management service [822](#nbsf_management-service)

5.2.13.2.1 General [822](#general-168)

5.2.13.2.2 Nbsf_Management_Register service operation [822](#nbsf_management_register-service-operation)

5.2.13.2.3 Nbsf_Management_Deregister service operation [823](#nbsf_management_deregister-service-operation)

5.2.13.2.4 Nbsf_Management_Discovery service operation [823](#nbsf_management_discovery-service-operation)

5.2.13.2.5 Nbsf_Management_Update service operation [823](#nbsf_management_update-service-operation)

5.2.13.2.6 Nbsf_Management_Subscribe service operation [824](#nbsf_management_subscribe-service-operation)

5.2.13.2.7 Nbsf_Management_Unsubscribe service operation [824](#nbsf_management_unsubscribe-service-operation)

5.2.13.2.8 Nbsf_Management_Notify service operation [824](#nbsf_management_notify-service-operation)

5.2.14 UDSF Services [825](#udsf-services)

5.2.14.1 General [825](#general-169)

5.2.14.2 Nudsf_UnstructuredDataManagement service [825](#nudsf_unstructureddatamanagement-service)

5.2.14.2.1 General [825](#general-170)

5.2.14.2.2 Nudsf_UnstructuredDataManagement_Query service operation [825](#nudsf_unstructureddatamanagement_query-service-operation)

5.2.14.2.3 Nudsf_UnstructuredDataManagement_Create service operation [825](#nudsf_unstructureddatamanagement_create-service-operation)

5.2.14.2.4 Nudsf_UnstructuredDataManagement_Delete service operation [826](#nudsf_unstructureddatamanagement_delete-service-operation)

5.2.14.2.5 Nudsf_UnstructuredDataManagement_Update service operation [826](#nudsf_unstructureddatamanagement_update-service-operation)

5.2.14.2.6 Nudsf_UnstructuredDataManagement_Subscribe [826](#nudsf_unstructureddatamanagement_subscribe)

5.2.14.2.7 Nudsf_UnstructuredDataManagement_Unsubscribe [827](#nudsf_unstructureddatamanagement_unsubscribe)

5.2.14.2.8 Nudsf_UnstructuredDataManagement_Notify [827](#nudsf_unstructureddatamanagement_notify)

5.2.14.3 Nudsf_Timer service [827](#nudsf_timer-service)

5.2.14.3.1 General [827](#general-171)

5.2.14.3.2 Nudsf_Timer_Start service operation [827](#nudsf_timer_start-service-operation)

5.2.14.3.3 Nudsf_Timer_Update service operation [827](#nudsf_timer_update-service-operation)

5.2.14.3.4 Nudsf_Timer_Notify service operation [828](#nudsf_timer_notify-service-operation)

5.2.14.3.5 Nudsf_Timer_Stop service operation [828](#nudsf_timer_stop-service-operation)

5.2.14.3.6 Nudsf_Timer_Search service operation [828](#nudsf_timer_search-service-operation)

5.2.15 LMF Services [828](#lmf-services)

5.2.16 NSSF Services [828](#nssf-services)

5.2.16.1 General [828](#general-172)

5.2.16.2 Nnssf_NSSelection service [829](#nnssf_nsselection-service)

5.2.16.2.1 Nnssf_NSSelection_Get service operation [829](#nnssf_nsselection_get-service-operation)

5.2.16.3 Nnssf_NSSAIAvailability service [831](#nnssf_nssaiavailability-service)

5.2.16.3.1 General [831](#general-173)

5.2.16.3.2 Nnssf_NSSAIAvailability_Update service operation [831](#nnssf_nssaiavailability_update-service-operation)

5.2.16.3.3 Nnssf_NSSAIAvailability_Notify service operation [831](#nnssf_nssaiavailability_notify-service-operation)

5.2.16.3.4 Nnssf_NSSAIAvailability_Subscribe service operation [832](#nnssf_nssaiavailability_subscribe-service-operation)

5.2.16.3.5 Nnssf_NSSAIAvailability_Unsubscribe service operation [833](#nnssf_nssaiavailability_unsubscribe-service-operation)

5.2.16.3.6 Nnssf_NSSAIAvailability_Delete service operation [834](#nnssf_nssaiavailability_delete-service-operation)

5.2.16.4 Void [834](#void-34)

5.2.17 CHF Spending Limit Control Service [834](#chf-spending-limit-control-service)

5.2.17.1 General [834](#general-174)

5.2.17.2 Nchf_SpendingLimitControl service [834](#nchf_spendinglimitcontrol-service)

5.2.17.2.1 General [834](#general-175)

5.2.17.2.2 Nchf_SpendingLimitControl Subscribe service operation [834](#nchf_spendinglimitcontrol-subscribe-service-operation)

5.2.17.2.3 Nchf_SpendingLimitControl Unsubscribe service operation [835](#nchf_spendinglimitcontrol-unsubscribe-service-operation)

5.2.17.2.4 Nchf_SpendingLimitControl Notify service operation [835](#nchf_spendinglimitcontrol-notify-service-operation)

5.2.18 UCMF Services [835](#ucmf-services)

5.2.18.1 General [835](#general-176)

5.2.18.2 Nucmf_Provisioning service [835](#nucmf_provisioning-service)

5.2.18.2.1 Nucmf_Provisioning_Create service operation [835](#nucmf_provisioning_create-service-operation)

5.2.18.2.2 Nucmf_Provisioning_Delete service operation [836](#nucmf_provisioning_delete-service-operation)

5.2.18.2.3 Nucmf_Provisioning_Update service operation [836](#nucmf_provisioning_update-service-operation)

5.2.18.3 Nucmf_UECapabilityManagement Service [836](#nucmf_uecapabilitymanagement-service)

5.2.18.3.1 Nucmf_UECapabilityManagement Resolve service operation [836](#nucmf_uecapabilitymanagement-resolve-service-operation)

5.2.18.3.2 Nucmf_UECapabilityManagement_Assign service operation [837](#nucmf_uecapabilitymanagement_assign-service-operation)

5.2.18.3.3 Nucmf_UECapabilityManagement_Subscribe service operation [837](#nucmf_uecapabilitymanagement_subscribe-service-operation)

5.2.18.3.4 Nucmf_UECapabilityManagement_Unsubscribe service operation [837](#nucmf_uecapabilitymanagement_unsubscribe-service-operation)

5.2.18.3.5 Nucmf_UECapabilityManagement_Notify service operation [838](#nucmf_uecapabilitymanagement_notify-service-operation)

5.2.19 AF Services [838](#af-services)

5.2.19.1 General [838](#general-177)

5.2.19.2 Naf_EventExposure service [838](#naf_eventexposure-service)

5.2.19.2.1 General [838](#general-178)

5.2.19.2.2 Naf_EventExposure_Subscribe service operation [839](#naf_eventexposure_subscribe-service-operation)

5.2.19.2.3 Naf_EventExposure_Unsubscribe service operation [840](#naf_eventexposure_unsubscribe-service-operation)

5.2.19.2.4 Naf_EventExposure_Notify service operation [840](#naf_eventexposure_notify-service-operation)

5.2.19.3 Void [840](#void-35)

5.2.20 NSSAAF services [840](#nssaaf-services)

5.2.20.1 General [840](#general-179)

5.2.20.2 Nnssaaf_NSSAA service [841](#nnssaaf_nssaa-service)

5.2.20.2.1 General [841](#general-180)

5.2.20.2.2 Nnssaaf_NSSAA_Authenticate service operation [841](#nnssaaf_nssaa_authenticate-service-operation)

5.2.20.2.3 Nnssaaf_NSSAA_Re-AuthenticationNotification service operation [841](#nnssaaf_nssaa_re-authenticationnotification-service-operation)

5.2.20.2.4 Nnssaaf_NSSAA_RevocationNotification service operation [841](#nnssaaf_nssaa_revocationnotification-service-operation)

5.2.20.3 Nnssaaf_AIW service [841](#nnssaaf_aiw-service)

5.2.20.3.1 General [841](#general-181)

5.2.20.3.2 Nnssaaf_AIW_Authenticate service operation [841](#nnssaaf_aiw_authenticate-service-operation)

5.2.21 NSACF services [841](#nsacf-services)

5.2.21.1 General [841](#general-182)

5.2.21.2 Nnsacf_NSAC services [842](#nnsacf_nsac-services)

5.2.21.2.1 General [842](#general-183)

5.2.21.2.2 Nnsacf_NSAC_NumOfUEsUpdate service operation [842](#nnsacf_nsac_numofuesupdate-service-operation)

5.2.21.2.3 Nnsacf_NSAC_EACNotify service operation [843](#nnsacf_nsac_eacnotify-service-operation)

5.2.21.2.4 Nnsacf_NSAC_NumOfPDUsUpdate service operation [844](#nnsacf_nsac_numofpdusupdate-service-operation)

5.2.21.2.5 Nnsacf_NSAC_QuotaUpdate service operation [845](#nnsacf_nsac_quotaupdate-service-operation)

5.2.21.2.6 Nnsacf_NSAC_LocalNumberUpdate service operation [845](#nnsacf_nsac_localnumberupdate-service-operation)

5.2.21.3 Void [845](#void-36)

5.2.21.4 Nnsacf_SliceEventExposure services [845](#nnsacf_sliceeventexposure-services)

5.2.21.4.1 General [845](#general-184)

5.2.21.4.2 Nnsacf_SliceEventExposure_Subscribe service operation [845](#nnsacf_sliceeventexposure_subscribe-service-operation)

5.2.21.4.3 Nnsacf_SliceEventExposure_Unsubscribe service operation [846](#nnsacf_sliceeventexposure_unsubscribe-service-operation)

5.2.21.4.4 Nnsacf_SliceEventExposure_Notify service operation [846](#nnsacf_sliceeventexposure_notify-service-operation)

5.2.21.5 Void [847](#void-37)

5.2.22 DCCF Services [847](#dccf-services)

5.2.23 MFAF Services [847](#mfaf-services)

5.2.24 ADRF Services [847](#adrf-services)

5.2.25 EASDF Services [847](#easdf-services)

5.2.26 UPF Services [847](#upf-services)

5.2.26.1 General [847](#general-185)

5.2.26.2 Nupf_EventExposure Service [847](#nupf_eventexposure-service)

5.2.26.2.1 General [847](#general-186)

5.2.26.2.2 Nupf_EventExposure_Notify service operation [849](#nupf_eventexposure_notify-service-operation)

5.2.26.2.3 Nupf_EventExposure_Subscribe service operation [849](#nupf_eventexposure_subscribe-service-operation)

5.2.26.2.4 Nupf_EventExposure_UnSubscribe service operation [849](#nupf_eventexposure_unsubscribe-service-operation)

5.2.26.3 Nupf_GetUEPrivateIPaddrAndIdentifiers service [849](#nupf_getueprivateipaddrandidentifiers-service)

5.2.26.3.1 General [849](#general-187)

5.2.26.3.2 Nupf_GetPrivateUEIPaddrAndIdentifiers_Get service operation [850](#nupf_getprivateueipaddrandidentifiers_get-service-operation)

5.2.27 TSCTSF Services [850](#tsctsf-services)

5.2.27.1 General [850](#general-188)

5.2.27.2 Ntsctsf_TimeSynchronization service [850](#ntsctsf_timesynchronization-service)

5.2.27.2.1 General [850](#general-189)

5.2.27.2.2 Ntsctsf_TimeSynchronization_ConfigCreate operation [850](#ntsctsf_timesynchronization_configcreate-operation)

5.2.27.2.3 Ntsctsf_TimeSynchronization_ConfigUpdate operation [851](#ntsctsf_timesynchronization_configupdate-operation)

5.2.27.2.4 Ntsctsf_TimeSynchronization_ConfigDelete operation [851](#ntsctsf_timesynchronization_configdelete-operation)

5.2.27.2.5 Ntsctsf_TimeSynchronization_ConfigUpdateNotify operation [851](#ntsctsf_timesynchronization_configupdatenotify-operation)

5.2.27.2.6 Ntsctsf_TimeSynchronization_CapsSubscribe operation [852](#ntsctsf_timesynchronization_capssubscribe-operation)

5.2.27.2.7 Ntsctsf_TimeSynchronization_CapsUnsubscribe operation [853](#ntsctsf_timesynchronization_capsunsubscribe-operation)

5.2.27.2.8 Ntsctsf_TimeSynchronization_CapsNotify operation [853](#ntsctsf_timesynchronization_capsnotify-operation)

5.2.27.2.9 Void [854](#void-38)

5.2.27.2.10 Void [854](#void-39)

5.2.27.2.11 Void [854](#void-40)

5.2.27.2.12 Void [854](#void-41)

5.2.27.3 Ntsctsf_QoSandTSCAssistance [854](#ntsctsf_qosandtscassistance)

5.2.27.3.1 General [854](#general-190)

5.2.27.3.2 Ntsctsf_QoSandTSCAssistance_Create operation [854](#ntsctsf_qosandtscassistance_create-operation)

5.2.27.3.3 Ntsctsf_QoSandTSCAssistance_Update operation [854](#ntsctsf_qosandtscassistance_update-operation)

5.2.27.3.4 Ntsctsf_QoSandTSCAssistance_Delete operation [855](#ntsctsf_qosandtscassistance_delete-operation)

5.2.27.3.5 Ntsctsf_QoSandTSCAssistance_Notify operation [855](#ntsctsf_qosandtscassistance_notify-operation)

5.2.27.3.6 Ntsctsf_QoSandTSCAssistance_Subscribe operation [855](#ntsctsf_qosandtscassistance_subscribe-operation)

5.2.27.3.7 Ntsctsf_QoSandTSCAssistance_Unsubscribe operation [855](#ntsctsf_qosandtscassistance_unsubscribe-operation)

5.2.27.4 Ntsctsf_ASTI service [856](#ntsctsf_asti-service)

5.2.27.4.1 General [856](#general-191)

5.2.27.4.2 Ntsctsf_ASTI_Create operation [856](#ntsctsf_asti_create-operation)

5.2.27.4.3 Ntsctsf_ASTI_Update operation [856](#ntsctsf_asti_update-operation)

5.2.27.4.4 Ntsctsf_ASTI_Delete operation [856](#ntsctsf_asti_delete-operation)

5.2.27.4.5 Ntsctsf_ASTI_Get operation [857](#ntsctsf_asti_get-operation)

5.2.27.4.6 Ntsctsf_ASTI_UpdateNotify operation [857](#ntsctsf_asti_updatenotify-operation)

5.2.27.4.7 Void [857](#void-42)

5.2.27.4.8 Void [857](#void-43)

Annex A (informative): Drafting rules and conventions for NF services [858](#annex-a-informative-drafting-rules-and-conventions-for-nf-services)

A.1 General [858](#a.1-general-3)

A.2 Naming [858](#a.2-naming)

A.2.1 Service naming [858](#a.2.1-service-naming)

A.2.2 Service operation naming [858](#a.2.2-service-operation-naming)

A.3 Representation in an information flow [859](#a.3-representation-in-an-information-flow)

A.4 Reference to services and service operations in procedures [860](#a.4-reference-to-services-and-service-operations-in-procedures)

A.5 Service and service operation description template [860](#a.5-service-and-service-operation-description-template)

A.6 Design Guidelines for NF services [860](#a.6-design-guidelines-for-nf-services)

A.6.1 Self-Containment [860](#a.6.1-self-containment)

A.6.2 Reusability [861](#a.6.2-reusability)

A.6.3 Use Independent Management Schemes [861](#a.6.3-use-independent-management-schemes)

Annex B (informative): Drafting Rules for Information flows [862](#annex-b-informative-drafting-rules-for-information-flows)

Annex C (informative): Generating EPS PDN Connection parameters from 5G PDU Session parameters [863](#annex-c-informative-generating-eps-pdn-connection-parameters-from-5g-pdu-session-parameters)

Annex D (normative): UE Presence in Area of Interest [864](#annex-d-normative-ue-presence-in-area-of-interest)

D.1 Determination of UE presence in Area of Interest by AMF [864](#d.1-determination-of-ue-presence-in-area-of-interest-by-amf)

D.2 Determination of UE presence in Area of Interest by NG-RAN [865](#d.2-determination-of-ue-presence-in-area-of-interest-by-ng-ran)

Annex E (normative): Delegated SMF and PCF discovery in the Home Routed and specific SMF Service Areas scenarios [866](#annex-e-normative-delegated-smf-and-pcf-discovery-in-the-home-routed-and-specific-smf-service-areas-scenarios)

E.0 Overview [866](#e.0-overview)

E.1 Delegated SMF discovery in the Home Routed scenario [866](#e.1-delegated-smf-discovery-in-the-home-routed-scenario)

E.2 Delegated I-SMF discovery [868](#e.2-delegated-i-smf-discovery)

E.3 Delegated PCF discovery in the Roaming scenario [870](#e.3-delegated-pcf-discovery-in-the-roaming-scenario)

Annex F (informative): Information flows for 5GS integration with TSN or with Deterministic Networking [872](#annex-f-informative-information-flows-for-5gs-integration-with-tsn-or-with-deterministic-networking)

F.1 5GS Bridge information reporting [872](#f.1-5gs-bridge-information-reporting)

F.2 5GS Bridge configuration [874](#f.2-5gs-bridge-configuration)

F.3 BMCA procedure [875](#f.3-bmca-procedure)

F.4 5GS interworking with TSN deployed in the transport network [876](#f.4-5gs-interworking-with-tsn-deployed-in-the-transport-network)

F.5 5GS DetNet node information reporting [879](#f.5-5gs-detnet-node-information-reporting)

F.6 5GS DetNet node configuration [879](#f.6-5gs-detnet-node-configuration)

Annex G (normative): Support of GERAN/UTRAN access by SMF+PGW-C [881](#annex-g-normative-support-of-geranutran-access-by-smfpgw-c)

Annex H (normative): Support of EAP-based secondary authentication and authorization by DN-AAA over EPC [883](#annex-h-normative-support-of-eap-based-secondary-authentication-and-authorization-by-dn-aaa-over-epc)

H.1 Introduction [883](#h.1-introduction)

H.2 Procedures [883](#h.2-procedures)

H.2.1 Secondary authentication and authorization by DN-AAA at PDN Connection Establishment [883](#h.2.1-secondary-authentication-and-authorization-by-dn-aaa-at-pdn-connection-establishment)

Annex I (informative): Member UE selection without the NEF assistance at the AF [886](#annex-i-informative-member-ue-selection-without-the-nef-assistance-at-the-af)

Annex J (informative): Support for Personal IoT Networks [887](#annex-j-informative-support-for-personal-iot-networks)

J.1 Procedure for PIN service [887](#j.1-procedure-for-pin-service)

Annex K (informative): Change history [889](#annex-k-informative-change-history)

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
