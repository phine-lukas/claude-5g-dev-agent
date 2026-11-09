<!-- table -->
| 3GPP TS 23.501 V18.12.0 (2025-12) (x2) |
| Technical Specification (x2) |
| 3rd Generation Partnership Project; Technical Specification Group Services and System Aspects; System architecture for the 5G System (5GS); Stage 2 (Release 18) (x2) |
| The present document has been developed within the 3rd Generation Partnership Project (3GPP TM ) and may be further elaborated for the purposes of 3GPP. / The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented. / This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification. / Specifications and Reports for implementation of the 3GPP TM system should be obtained via the 3GPP Organizational Partners' Publications Offices. (x2) |
<!-- /table -->

<!-- table -->
| 3GPP Postal address 3GPP support office address 650 Route des Lucioles - Sophia Antipolis Valbonne - FRANCE Tel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16 Internet http://www.3gpp.org |
| Copyright Notification No part may be reproduced except as authorized by written permission. / The copyright and the foregoing restriction extend to reproduction in all media. © 2025, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC). All rights reserved. UMTS™ is a Trade Mark of ETSI registered for the benefit of its members 3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners / LTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners GSM® and the GSM logo are registered and owned by the GSM Association |
<!-- /table -->

#  Contents

Foreword [22](#foreword)

1 Scope [23](#scope)

2 References [23](#references)

3 Definitions and abbreviations [30](#definitions-and-abbreviations)

3.1 Definitions [30](#definitions)

3.2 Abbreviations [37](#abbreviations)

4 Architecture model and concepts [41](#architecture-model-and-concepts)

4.1 General concepts [41](#general-concepts)

4.2 Architecture reference model [41](#architecture-reference-model)

4.2.1 General [41](#general)

4.2.2 Network Functions and entities [42](#network-functions-and-entities)

4.2.3 Non-roaming reference architecture [43](#non-roaming-reference-architecture)

4.2.4 Roaming reference architectures [46](#roaming-reference-architectures)

4.2.5 Data Storage architectures [50](#data-storage-architectures)

4.2.5a Radio Capabilities Signalling optimisation [52](#a-radio-capabilities-signalling-optimisation)

4.2.6 Service-based interfaces [52](#service-based-interfaces)

4.2.7 Reference points [53](#reference-points)

4.2.8 Support of non-3GPP access [56](#support-of-non-3gpp-access)

4.2.8.0 General [56](#general-1)

4.2.8.1 General Concepts to Support Trusted and Untrusted Non-3GPP Access [56](#general-concepts-to-support-trusted-and-untrusted-non-3gpp-access)

4.2.8.1A General Concepts to support Wireline Access [57](#a-general-concepts-to-support-wireline-access)

4.2.8.2 Architecture Reference Model for Trusted and Untrusted Non-3GPP Accesses [58](#architecture-reference-model-for-trusted-and-untrusted-non-3gpp-accesses)

4.2.8.2.1 Non-roaming Architecture [58](#non-roaming-architecture)

4.2.8.2.2 LBO Roaming Architecture [59](#lbo-roaming-architecture)

4.2.8.2.3 Home-routed Roaming Architecture [62](#home-routed-roaming-architecture)

4.2.8.3 Reference Points for Non-3GPP Access [64](#reference-points-for-non-3gpp-access)

4.2.8.3.1 Overview [64](#overview)

4.2.8.3.2 Requirements on Ta [64](#requirements-on-ta)

4.2.8.4 Architecture Reference Model for Wireline Access network [65](#architecture-reference-model-for-wireline-access-network)

4.2.8.5 Access to 5GC from devices that do not support 5GC NAS over WLAN access [66](#access-to-5gc-from-devices-that-do-not-support-5gc-nas-over-wlan-access)

4.2.8.5.1 General [66](#general-2)

4.2.8.5.2 Reference Architecture [66](#reference-architecture)

4.2.8.5.3 Network Functions [67](#network-functions)

4.2.8.5.4 Reference Points [67](#reference-points-1)

4.2.9 Network Analytics architecture [68](#network-analytics-architecture)

4.2.10 Architecture Reference Model for ATSSS Support [68](#architecture-reference-model-for-atsss-support)

4.2.11 Architecture for 5G multicast-broadcast services [69](#architecture-for-5g-multicast-broadcast-services)

4.2.12 Architecture for Proximity based Services (ProSe) in 5GS [69](#architecture-for-proximity-based-services-prose-in-5gs)

4.2.13 Architecture enhancements for Edge Computing [70](#architecture-enhancements-for-edge-computing)

4.2.14 Architecture for Support of Uncrewed Aerial Systems connectivity, identification and tracking [70](#architecture-for-support-of-uncrewed-aerial-systems-connectivity-identification-and-tracking)

4.2.15 Architecture to support WLAN connection using 5G credentials without 5GS registration [70](#architecture-to-support-wlan-connection-using-5g-credentials-without-5gs-registration)

4.2.16 Architecture to support User Plane Information Exposure via a service-based interface [74](#architecture-to-support-user-plane-information-exposure-via-a-service-based-interface)

4.2.17 Architecture for Ranging based services and Sidelink Positioning [74](#architecture-for-ranging-based-services-and-sidelink-positioning)

4.3 Interworking with EPC [75](#interworking-with-epc)

4.3.1 Non-roaming architecture [75](#non-roaming-architecture-1)

4.3.2 Roaming architecture [75](#roaming-architecture)

4.3.3 Interworking between 5GC via non-3GPP access and E-UTRAN connected to EPC [77](#interworking-between-5gc-via-non-3gpp-access-and-e-utran-connected-to-epc)

4.3.3.1 Non-roaming architecture [77](#non-roaming-architecture-2)

4.3.3.2 Roaming architecture [78](#roaming-architecture-1)

4.3.4 Interworking between ePDG connected to EPC and 5GS [80](#interworking-between-epdg-connected-to-epc-and-5gs)

4.3.4.1 Non-roaming architecture [80](#non-roaming-architecture-3)

4.3.4.2 Roaming architectures [81](#roaming-architectures)

4.3.5 Service Exposure in Interworking Scenarios [83](#service-exposure-in-interworking-scenarios)

4.3.5.1 Non-roaming architecture [83](#non-roaming-architecture-4)

4.3.5.2 Roaming architectures [84](#roaming-architectures-1)

4.4 Specific services [85](#specific-services)

4.4.1 Public Warning System [85](#public-warning-system)

4.4.2 SMS over NAS [85](#sms-over-nas)

4.4.2.0 General [85](#general-3)

4.4.2.1 Architecture to support SMS over NAS [85](#architecture-to-support-sms-over-nas)

4.4.2.2 Reference point to support SMS over NAS [87](#reference-point-to-support-sms-over-nas)

4.4.2.3 Service based interface to support SMS over NAS [87](#service-based-interface-to-support-sms-over-nas)

4.4.3 IMS support [87](#ims-support)

4.4.4 Location services [88](#location-services)

4.4.4.1 Architecture to support Location Services [88](#architecture-to-support-location-services)

4.4.4.2 Reference point to support Location Services [88](#reference-point-to-support-location-services)

4.4.4.3 Service Based Interfaces to support Location Services [88](#service-based-interfaces-to-support-location-services)

4.4.5 Application Triggering Services [88](#application-triggering-services)

4.4.6 5G LAN-type Services [88](#g-lan-type-services)

4.4.6.1 User plane architecture to support 5G LAN-type service [88](#user-plane-architecture-to-support-5g-lan-type-service)

4.4.6.2 Reference points to support 5G LAN-type service [89](#reference-points-to-support-5g-lan-type-service)

4.4.7 MSISDN-less MO SMS Service [89](#msisdn-less-mo-sms-service)

4.4.8 Architecture to enable Time Sensitive Communication, Time Synchronization and Deterministic Networking [89](#architecture-to-enable-time-sensitive-communication-time-synchronization-and-deterministic-networking)

4.4.8.1 General [89](#general-4)

4.4.8.2 Architecture to support IEEE Time Sensitive Networking [90](#architecture-to-support-ieee-time-sensitive-networking)

4.4.8.3 Architecture for AF requested support of Time Sensitive Communication and Time Synchronization [91](#architecture-for-af-requested-support-of-time-sensitive-communication-and-time-synchronization)

4.4.8.4 Architecture to support IETF Deterministic Networking [91](#architecture-to-support-ietf-deterministic-networking)

5 High level features [92](#high-level-features)

5.1 General [92](#general-5)

5.2 Network Access Control [93](#network-access-control)

5.2.1 General [93](#general-6)

5.2.2 Network selection [93](#network-selection)

5.2.2a Void [93](#a-void)

5.2.3 Identification and authentication [93](#identification-and-authentication)

5.2.4 Authorisation [93](#authorisation)

5.2.5 Access control and barring [93](#access-control-and-barring)

5.2.6 Policy control [94](#policy-control)

5.2.7 Lawful Interception [94](#lawful-interception)

5.3 Registration and Connection Management [94](#registration-and-connection-management)

5.3.1 General [94](#general-7)

5.3.2 Registration Management [94](#registration-management)

5.3.2.1 General [94](#general-8)

5.3.2.2 5GS Registration Management states [95](#gs-registration-management-states)

5.3.2.2.1 General [95](#general-9)

5.3.2.2.2 RM-DEREGISTERED state [95](#rm-deregistered-state)

5.3.2.2.3 RM-REGISTERED state [95](#rm-registered-state)

5.3.2.2.4 5GS Registration Management State models [96](#gs-registration-management-state-models)

5.3.2.3 Registration Area management [96](#registration-area-management)

5.3.2.4 Support of a UE registered over both 3GPP and Non-3GPP access [98](#support-of-a-ue-registered-over-both-3gpp-and-non-3gpp-access)

5.3.3 Connection Management [99](#connection-management)

5.3.3.1 General [99](#general-10)

5.3.3.2 5GS Connection Management states [100](#gs-connection-management-states)

5.3.3.2.1 General [100](#general-11)

5.3.3.2.2 CM-IDLE state [100](#cm-idle-state)

5.3.3.2.3 CM-CONNECTED state [100](#cm-connected-state)

5.3.3.2.4 5GS Connection Management State models [101](#gs-connection-management-state-models)

5.3.3.2.5 CM-CONNECTED with RRC_INACTIVE state [101](#cm-connected-with-rrc_inactive-state)

5.3.3.3 NAS signalling connection management [104](#nas-signalling-connection-management)

5.3.3.3.1 General [104](#general-12)

5.3.3.3.2 NAS signalling connection establishment [104](#nas-signalling-connection-establishment)

5.3.3.3.3 NAS signalling connection Release [104](#nas-signalling-connection-release)

5.3.3.4 Support of a UE connected over both 3GPP and Non-3GPP access [104](#support-of-a-ue-connected-over-both-3gpp-and-non-3gpp-access)

5.3.4 UE Mobility [105](#ue-mobility)

5.3.4.1 Mobility Restrictions [105](#mobility-restrictions)

5.3.4.1.1 General [105](#general-13)

5.3.4.1.2 Management of Service Area Restrictions [108](#management-of-service-area-restrictions)

5.3.4.2 Mobility Pattern [109](#mobility-pattern)

5.3.4.3 Radio Resource Management functions [109](#radio-resource-management-functions)

5.3.4.3.1 General [109](#general-14)

5.3.4.3.2 Preferred band(s) per data radio bearer(s) [110](#preferred-bands-per-data-radio-bearers)

5.3.4.3.3 Redirection to dedicated frequency band(s) for an S-NSSAI [110](#redirection-to-dedicated-frequency-bands-for-an-s-nssai)

5.3.4.3.4 Network Slice based cell reselection and Random Access [111](#network-slice-based-cell-reselection-and-random-access)

5.3.4.4 UE mobility event notification [112](#ue-mobility-event-notification)

5.3.5 Triggers for network analytics [113](#triggers-for-network-analytics)

5.4 3GPP access specific aspects [114](#gpp-access-specific-aspects)

5.4.1 UE reachability in CM-IDLE [114](#ue-reachability-in-cm-idle)

5.4.1.1 General [114](#general-15)

5.4.1.2 UE reachability allowing mobile terminated data while the UE is CM-IDLE [115](#ue-reachability-allowing-mobile-terminated-data-while-the-ue-is-cm-idle)

5.4.1.3 Mobile Initiated Connection Only (MICO) mode [115](#mobile-initiated-connection-only-mico-mode)

5.4.1.4 Support of Unavailability Period [116](#support-of-unavailability-period)

5.4.2 UE reachability in CM-CONNECTED [118](#ue-reachability-in-cm-connected)

5.4.3 Paging strategy handling [118](#paging-strategy-handling)

5.4.3.1 General [118](#general-16)

5.4.3.2 Paging Policy Differentiation [118](#paging-policy-differentiation)

5.4.3.3 Paging Priority [119](#paging-priority)

5.4.4 UE Radio Capability handling [119](#ue-radio-capability-handling)

5.4.4.1 UE radio capability information storage in the AMF [119](#ue-radio-capability-information-storage-in-the-amf)

5.4.4.1a UE radio capability signalling optimisation (RACS) [120](#a-ue-radio-capability-signalling-optimisation-racs)

5.4.4.2 Void [124](#void)

5.4.4.2a UE Radio Capability Match Request [124](#a-ue-radio-capability-match-request)

5.4.4.3 Paging assistance information [125](#paging-assistance-information)

5.4.4a UE MM Core Network Capability handling [125](#a-ue-mm-core-network-capability-handling)

5.4.4b UE 5GSM Core Network Capability handling [127](#b-ue-5gsm-core-network-capability-handling)

5.4.5 DRX (Discontinuous Reception) framework [127](#drx-discontinuous-reception-framework)

5.4.6 Core Network assistance information for RAN optimization [127](#core-network-assistance-information-for-ran-optimization)

5.4.6.1 General [127](#general-17)

5.4.6.2 Core Network assisted RAN parameters tuning [128](#core-network-assisted-ran-parameters-tuning)

5.4.6.3 Core Network assisted RAN paging information [129](#core-network-assisted-ran-paging-information)

5.4.7 NG-RAN location reporting [129](#ng-ran-location-reporting)

5.4.8 Support for identification and restriction of using unlicensed spectrum [129](#support-for-identification-and-restriction-of-using-unlicensed-spectrum)

5.4.9 Wake Up Signal Assistance [130](#wake-up-signal-assistance)

5.4.9.1 General [130](#general-18)

5.4.9.2 Group Wake Up Signal [131](#group-wake-up-signal)

5.4.10 Support for identification and restriction of using NR satellite access [131](#support-for-identification-and-restriction-of-using-nr-satellite-access)

5.4.11 Support for integrating NR satellite access into 5GS [132](#support-for-integrating-nr-satellite-access-into-5gs)

5.4.11.1 General [132](#general-19)

5.4.11.2 Support of RAT types defined in 5GC for satellite access [132](#support-of-rat-types-defined-in-5gc-for-satellite-access)

5.4.11.3 Void [132](#void-1)

5.4.11.4 Verification of UE location [132](#verification-of-ue-location)

5.4.11.5 Network selection for NR satellite access [133](#network-selection-for-nr-satellite-access)

5.4.11.6 Support of Mobility Registration Update [133](#support-of-mobility-registration-update)

5.4.11.7 Tracking Area handling for NR satellite access [133](#tracking-area-handling-for-nr-satellite-access)

5.4.11.8 Support for mobility Forbidden Area and Service Area Restrictions for NR satellite access [133](#support-for-mobility-forbidden-area-and-service-area-restrictions-for-nr-satellite-access)

5.4.12 Paging Early Indication with Paging Subgrouping Assistance [134](#paging-early-indication-with-paging-subgrouping-assistance)

5.4.12.1 General [134](#general-20)

5.4.12.2 Core Network Assistance for PEIPS [134](#core-network-assistance-for-peips)

5.4.13 Support of discontinuous network coverage for satellite access [135](#support-of-discontinuous-network-coverage-for-satellite-access)

5.4.13.0 General [135](#general-21)

5.4.13.1 Mobility Management and Power Saving Optimization [135](#mobility-management-and-power-saving-optimization)

5.4.13.2 Coverage availability information provisioning to the UE [136](#coverage-availability-information-provisioning-to-the-ue)

5.4.13.3 Coverage availability information provisioning to the AMF [136](#coverage-availability-information-provisioning-to-the-amf)

5.4.13.4 Paging [136](#paging)

5.4.13.5 Overload control [136](#overload-control)

5.5 Non-3GPP access specific aspects [137](#non-3gpp-access-specific-aspects)

5.5.0 General [137](#general-22)

5.5.1 Registration Management [137](#registration-management-1)

5.5.2 Connection Management [138](#connection-management-1)

5.5.3 UE Reachability [139](#ue-reachability)

5.5.3.1 UE reachability in CM-IDLE [139](#ue-reachability-in-cm-idle-1)

5.5.3.2 UE reachability in CM-CONNECTED [139](#ue-reachability-in-cm-connected-1)

5.6 Session Management [140](#session-management)

5.6.1 Overview [140](#overview-1)

5.6.2 Interaction between AMF and SMF [143](#interaction-between-amf-and-smf)

5.6.3 Roaming [145](#roaming)

5.6.4 Single PDU Session with multiple PDU Session Anchors [145](#single-pdu-session-with-multiple-pdu-session-anchors)

5.6.4.1 General [145](#general-23)

5.6.4.2 Usage of an UL Classifier for a PDU Session [146](#usage-of-an-ul-classifier-for-a-pdu-session)

5.6.4.3 Usage of IPv6 multi-homing for a PDU Session [148](#usage-of-ipv6-multi-homing-for-a-pdu-session)

5.6.5 Support for Local Area Data Network [149](#support-for-local-area-data-network)

5.6.5a Supporting LADN per DNN and S-NSSAI [151](#a-supporting-ladn-per-dnn-and-s-nssai)

5.6.6 Secondary authentication/authorization by a DN-AAA server during the establishment of a PDU Session [152](#secondary-authenticationauthorization-by-a-dn-aaa-server-during-the-establishment-of-a-pdu-session)

5.6.7 Application Function influence on traffic routing [154](#application-function-influence-on-traffic-routing)

5.6.7.1 General [154](#general-24)

5.6.7.2 Enhancement of UP path management based on the coordination with AFs [164](#enhancement-of-up-path-management-based-on-the-coordination-with-afs)

5.6.8 Selective activation and deactivation of UP connection of existing PDU Session [165](#selective-activation-and-deactivation-of-up-connection-of-existing-pdu-session)

5.6.9 Session and Service Continuity [166](#session-and-service-continuity)

5.6.9.1 General [166](#general-25)

5.6.9.2 SSC mode [166](#ssc-mode)

5.6.9.2.1 SSC Mode 1 [166](#ssc-mode-1)

5.6.9.2.2 SSC Mode 2 [166](#ssc-mode-2)

5.6.9.2.3 SSC Mode 3 [167](#ssc-mode-3)

5.6.9.3 SSC mode selection [167](#ssc-mode-selection)

5.6.10 Specific aspects of different PDU Session types [168](#specific-aspects-of-different-pdu-session-types)

5.6.10.1 Support of IP PDU Session type [168](#support-of-ip-pdu-session-type)

5.6.10.2 Support of Ethernet PDU Session type [168](#support-of-ethernet-pdu-session-type)

5.6.10.3 Support of Unstructured PDU Session type [170](#support-of-unstructured-pdu-session-type)

5.6.10.4 Maximum Transfer Unit size considerations [171](#maximum-transfer-unit-size-considerations)

5.6.11 UE presence in Area of Interest reporting usage by SMF [171](#ue-presence-in-area-of-interest-reporting-usage-by-smf)

5.6.12 Use of Network Instance [173](#use-of-network-instance)

5.6.13 Always-on PDU session [173](#always-on-pdu-session)

5.6.14 Support of Framed Routing [174](#support-of-framed-routing)

5.6.15 Triggers for network analytics [174](#triggers-for-network-analytics-1)

5.6.16 Support for Service Function Chaining [175](#support-for-service-function-chaining)

5.6.16.1 General [175](#general-26)

5.6.16.2 Application Function influence on Service Function Chaining [175](#application-function-influence-on-service-function-chaining)

5.7 QoS model [176](#qos-model)

5.7.1 General Overview [176](#general-overview)

5.7.1.1 QoS Flow [176](#qos-flow)

5.7.1.2 QoS Profile [177](#qos-profile)

5.7.1.2a Alternative QoS Profile [178](#a-alternative-qos-profile)

5.7.1.3 Control of QoS Flows [178](#control-of-qos-flows)

5.7.1.4 QoS Rules [178](#qos-rules)

5.7.1.5 QoS Flow mapping [179](#qos-flow-mapping)

5.7.1.6 DL traffic [181](#dl-traffic)

5.7.1.7 UL Traffic [181](#ul-traffic)

5.7.1.8 AMBR/MFBR enforcement and rate limitation [182](#ambrmfbr-enforcement-and-rate-limitation)

5.7.1.9 Precedence Value [182](#precedence-value)

5.7.1.10 UE-Slice-MBR enforcement and rate limitation [182](#ue-slice-mbr-enforcement-and-rate-limitation)

5.7.1.11 QoS aspects of home-routed roaming [183](#qos-aspects-of-home-routed-roaming)

5.7.2 5G QoS Parameters [184](#g-qos-parameters)

5.7.2.1 5QI [184](#qi)

5.7.2.2 ARP [184](#arp)

5.7.2.3 RQA [184](#rqa)

5.7.2.4 Notification control [185](#notification-control)

5.7.2.4.1 General [185](#general-27)

5.7.2.4.1a Notification Control without Alternative QoS Profiles [185](#a-notification-control-without-alternative-qos-profiles)

5.7.2.4.1b Notification control with Alternative QoS Profiles [186](#b-notification-control-with-alternative-qos-profiles)

5.7.2.4.2 Usage of Notification control with Alternative QoS Profiles at handover [186](#usage-of-notification-control-with-alternative-qos-profiles-at-handover)

5.7.2.4.3 Usage of Notification control with Alternative QoS Profiles during QoS Flow establishment and modification [187](#usage-of-notification-control-with-alternative-qos-profiles-during-qos-flow-establishment-and-modification)

5.7.2.5 Flow Bit Rates [187](#flow-bit-rates)

5.7.2.6 Aggregate Bit Rates [188](#aggregate-bit-rates)

5.7.2.7 Default values [188](#default-values)

5.7.2.8 Maximum Packet Loss Rate [189](#maximum-packet-loss-rate)

5.7.2.9 Wireline access network specific 5G QoS parameters [189](#wireline-access-network-specific-5g-qos-parameters)

5.7.3 5G QoS characteristics [189](#g-qos-characteristics)

5.7.3.1 General [189](#general-28)

5.7.3.2 Resource Type [190](#resource-type)

5.7.3.3 Priority Level [190](#priority-level)

5.7.3.4 Packet Delay Budget [190](#packet-delay-budget)

5.7.3.5 Packet Error Rate [191](#packet-error-rate)

5.7.3.6 Averaging Window [191](#averaging-window)

5.7.3.7 Maximum Data Burst Volume [192](#maximum-data-burst-volume)

5.7.4 Standardized 5QI to QoS characteristics mapping [192](#standardized-5qi-to-qos-characteristics-mapping)

5.7.5 Reflective QoS [197](#reflective-qos)

5.7.5.1 General [197](#general-29)

5.7.5.2 UE Derived QoS Rule [198](#ue-derived-qos-rule)

5.7.5.3 Reflective QoS Control [199](#reflective-qos-control)

5.7.6 Packet Filter Set [200](#packet-filter-set)

5.7.6.1 General [200](#general-30)

5.7.6.2 IP Packet Filter Set [200](#ip-packet-filter-set)

5.7.6.3 Ethernet Packet Filter Set [201](#ethernet-packet-filter-set)

5.7.7 PDU Set QoS Parameters [201](#pdu-set-qos-parameters)

5.7.7.1 General [201](#general-31)

5.7.7.2 PDU Set Delay Budget [201](#pdu-set-delay-budget)

5.7.7.3 PDU Set Error Rate [202](#pdu-set-error-rate)

5.7.7.4 PDU Set Integrated Handling Information [202](#pdu-set-integrated-handling-information)

5.8 User Plane Management [202](#user-plane-management)

5.8.1 General [202](#general-32)

5.8.2 Functional Description [203](#functional-description)

5.8.2.1 General [203](#general-33)

5.8.2.2 UE IP Address Management [203](#ue-ip-address-management)

5.8.2.2.1 General [203](#general-34)

5.8.2.2.2 Routing rules configuration [205](#routing-rules-configuration)

5.8.2.2.3 The procedure of Stateless IPv6 Address Autoconfiguration [206](#the-procedure-of-stateless-ipv6-address-autoconfiguration)

5.8.2.2.4 IPv6 Prefix Delegation via DHCPv6 [206](#ipv6-prefix-delegation-via-dhcpv6)

5.8.2.3 Management of CN Tunnel Info [207](#management-of-cn-tunnel-info)

5.8.2.3.1 General [207](#general-35)

5.8.2.3.2 Void [207](#void-2)

5.8.2.3.3 Management of CN Tunnel Info in the UPF [207](#management-of-cn-tunnel-info-in-the-upf)

5.8.2.4 Traffic Detection [207](#traffic-detection)

5.8.2.4.1 General [207](#general-36)

5.8.2.4.2 Traffic Detection Information [207](#traffic-detection-information)

5.8.2.5 Control of User Plane Forwarding [208](#control-of-user-plane-forwarding)

5.8.2.5.1 General [208](#general-37)

5.8.2.5.2 Data forwarding between the SMF and UPF [208](#data-forwarding-between-the-smf-and-upf)

5.8.2.5.3 Support of Ethernet PDU Session type [209](#support-of-ethernet-pdu-session-type-1)

5.8.2.6 Charging and Usage Monitoring Handling [210](#charging-and-usage-monitoring-handling)

5.8.2.6.1 General [210](#general-38)

5.8.2.6.2 Activation of Usage Reporting in UPF [210](#activation-of-usage-reporting-in-upf)

5.8.2.6.3 Reporting of Usage Information towards SMF [211](#reporting-of-usage-information-towards-smf)

5.8.2.7 PDU Session and QoS Flow Policing [211](#pdu-session-and-qos-flow-policing)

5.8.2.8 PCC Related Functions [211](#pcc-related-functions)

5.8.2.8.1 Activation/Deactivation of predefined PCC rules [211](#activationdeactivation-of-predefined-pcc-rules)

5.8.2.8.2 Enforcement of Dynamic PCC Rules [212](#enforcement-of-dynamic-pcc-rules)

5.8.2.8.3 Redirection [212](#redirection)

5.8.2.8.4 Support of PFD Management [213](#support-of-pfd-management)

5.8.2.9 Functionality of Sending of "End marker" [213](#functionality-of-sending-of-end-marker)

5.8.2.9.0 Introduction [213](#introduction)

5.8.2.9.1 UPF Constructing the "End marker" Packets [213](#upf-constructing-the-end-marker-packets)

5.8.2.9.2 SMF Constructing the "End marker" Packets [214](#smf-constructing-the-end-marker-packets)

5.8.2.10 UP Tunnel Management [214](#up-tunnel-management)

5.8.2.11 Parameters for N4 session management (moved) [214](#parameters-for-n4-session-management-moved)

5.8.2.12 Reporting of the UE MAC addresses used in a PDU Session [215](#reporting-of-the-ue-mac-addresses-used-in-a-pdu-session)

5.8.2.13 Support for 5G VN group communication [215](#support-for-5g-vn-group-communication)

5.8.2.13.0 General [215](#general-39)

5.8.2.13.1 Support for unicast traffic forwarding of a 5G VN [216](#support-for-unicast-traffic-forwarding-of-a-5g-vn)

5.8.2.13.2 Support for unicast traffic forwarding update due to UE mobility [217](#support-for-unicast-traffic-forwarding-update-due-to-ue-mobility)

5.8.2.13.3 Support for user plane traffic replication in a 5G VN [217](#support-for-user-plane-traffic-replication-in-a-5g-vn)

5.8.2.14 Inter PLMN User Plane Security functionality [219](#inter-plmn-user-plane-security-functionality)

5.8.2.15 Void [220](#void-3)

5.8.2.16 Support for L2TP tunnelling on N6 [220](#support-for-l2tp-tunnelling-on-n6)

5.8.2.17 Data exposure via Service Based interface [220](#data-exposure-via-service-based-interface)

5.8.2.18 QoS Flow related QoS monitoring and reporting [221](#qos-flow-related-qos-monitoring-and-reporting)

5.8.2.19 Explicit Buffer Management [222](#explicit-buffer-management)

5.8.2.19.1 General [222](#general-40)

5.8.2.19.2 Buffering at UPF [222](#buffering-at-upf)

5.8.2.19.3 Buffering at SMF [223](#buffering-at-smf)

5.8.2.20 SMF Pause of Charging [223](#smf-pause-of-charging)

5.8.3 Explicit Buffer Management (moved) [223](#explicit-buffer-management-moved)

5.8.4 SMF Pause of Charging (moved) [223](#smf-pause-of-charging-moved)

5.8.5 Parameters for N4 session management [223](#parameters-for-n4-session-management)

5.8.5.1 General [223](#general-41)

5.8.5.2 N4 Session Context [224](#n4-session-context)

5.8.5.3 Packet Detection Rule [225](#packet-detection-rule)

5.8.5.4 QoS Enforcement Rule [228](#qos-enforcement-rule)

5.8.5.5 Usage Reporting Rule [231](#usage-reporting-rule)

5.8.5.6 Forwarding Action Rule [234](#forwarding-action-rule)

5.8.5.7 Usage Report generated by UPF [237](#usage-report-generated-by-upf)

5.8.5.8 Multi-Access Rule [238](#multi-access-rule)

5.8.5.9 Bridge/Router Information [239](#bridgerouter-information)

5.8.5.10 Void [239](#void-4)

5.8.5.11 Session Reporting Rule [240](#session-reporting-rule)

5.8.5.12 Session reporting generated by UPF [240](#session-reporting-generated-by-upf)

5.8.5.13 Void [240](#void-5)

5.8.5.14 TSC Management Information [241](#tsc-management-information)

5.8.5.15 Downlink Data Report generated by UPF [241](#downlink-data-report-generated-by-upf)

5.9 Identifiers [241](#identifiers)

5.9.1 General [241](#general-42)

5.9.2 Subscription Permanent Identifier [242](#subscription-permanent-identifier)

5.9.2a Subscription Concealed Identifier [242](#a-subscription-concealed-identifier)

5.9.3 Permanent Equipment Identifier [242](#permanent-equipment-identifier)

5.9.4 5G Globally Unique Temporary Identifier [243](#g-globally-unique-temporary-identifier)

5.9.5 AMF Name [243](#amf-name)

5.9.6 Data Network Name (DNN) [243](#data-network-name-dnn)

5.9.7 Internal-Group Identifier [244](#internal-group-identifier)

5.9.8 Generic Public Subscription Identifier [244](#generic-public-subscription-identifier)

5.9.9 AMF UE NGAP ID [244](#amf-ue-ngap-id)

5.9.10 UE Radio Capability ID [244](#ue-radio-capability-id)

5.10 Security aspects [245](#security-aspects)

5.10.1 General [245](#general-43)

5.10.2 Security Model for non-3GPP access [245](#security-model-for-non-3gpp-access)

5.10.2.1 Signalling Security [245](#signalling-security)

5.10.3 PDU Session User Plane Security [245](#pdu-session-user-plane-security)

5.11 Support for Dual Connectivity, Multi-Connectivity [248](#support-for-dual-connectivity-multi-connectivity)

5.11.1 Support for Dual Connectivity [248](#support-for-dual-connectivity)

5.12 Charging [249](#charging)

5.12.1 General [249](#general-44)

5.12.2 Usage Data Reporting for Secondary RAT [249](#usage-data-reporting-for-secondary-rat)

5.12.3 Secondary RAT Periodic Usage Data Reporting Procedure [249](#secondary-rat-periodic-usage-data-reporting-procedure)

5.13 Support for Edge Computing [250](#support-for-edge-computing)

5.14 Policy Control [251](#policy-control-1)

5.15 Network slicing [251](#network-slicing)

5.15.1 General [251](#general-45)

5.15.2 Identification and selection of a Network Slice: the S-NSSAI and the NSSAI [252](#identification-and-selection-of-a-network-slice-the-s-nssai-and-the-nssai)

5.15.2.1 General [252](#general-46)

5.15.2.2 Standardised SST values [253](#standardised-sst-values)

5.15.3 Subscription aspects [254](#subscription-aspects)

5.15.4 UE NSSAI configuration and NSSAI storage aspects [255](#ue-nssai-configuration-and-nssai-storage-aspects)

5.15.4.1 General [255](#general-47)

5.15.4.1.1 UE Network Slice configuration [255](#ue-network-slice-configuration)

5.15.4.1.2 Mapping of S-NSSAIs values in the Allowed NSSAI and in the Requested NSSAI to the S-NSSAIs values used in the HPLMN [257](#mapping-of-s-nssais-values-in-the-allowed-nssai-and-in-the-requested-nssai-to-the-s-nssais-values-used-in-the-hplmn)

5.15.4.2 Update of UE Network Slice configuration [258](#update-of-ue-network-slice-configuration)

5.15.5 Detailed Operation Overview [259](#detailed-operation-overview)

5.15.5.1 General [259](#general-48)

5.15.5.2 Selection of a Serving AMF supporting the Network Slices [259](#selection-of-a-serving-amf-supporting-the-network-slices)

5.15.5.2.1 Registration to a set of Network Slices [259](#registration-to-a-set-of-network-slices)

5.15.5.2.2 Modification of the Set of Network Slice(s) for a UE [264](#modification-of-the-set-of-network-slices-for-a-ue)

5.15.5.2.3 AMF Re-allocation due to Network Slice(s) Support [266](#amf-re-allocation-due-to-network-slices-support)

5.15.5.3 Establishing a PDU Session in a Network Slice [266](#establishing-a-pdu-session-in-a-network-slice)

5.15.6 Network Slicing Support for Roaming [268](#network-slicing-support-for-roaming)

5.15.7 Network slicing and Interworking with EPS [269](#network-slicing-and-interworking-with-eps)

5.15.7.1 General [269](#general-49)

5.15.7.2 Idle mode aspects [269](#idle-mode-aspects)

5.15.7.3 Connected mode aspects [270](#connected-mode-aspects)

5.15.7.4 Support of Network Slice usage control and Interworking with EPC [270](#support-of-network-slice-usage-control-and-interworking-with-epc)

5.15.8 Configuration of Network Slice support and availability in a PLMN [270](#configuration-of-network-slice-support-and-availability-in-a-plmn)

5.15.9 Operator-controlled inclusion of NSSAI in Access Stratum Connection Establishment [271](#operator-controlled-inclusion-of-nssai-in-access-stratum-connection-establishment)

5.15.10 Network Slice-Specific Authentication and Authorization [272](#network-slice-specific-authentication-and-authorization)

5.15.11 Network Slice Admission Control [273](#network-slice-admission-control)

5.15.11.0 General [273](#general-50)

5.15.11.1 Network Slice Admission Control for maximum number of UEs [275](#network-slice-admission-control-for-maximum-number-of-ues)

5.15.11.1.1 Non-Hierarchical NSAC architecture [275](#non-hierarchical-nsac-architecture)

5.15.11.1.2 Hierarchical NSAC architecture [275](#hierarchical-nsac-architecture)

5.15.11.1.3 Centralized NSAC architecture [277](#centralized-nsac-architecture)

5.15.11.2 Network Slice Admission Control for maximum number of PDU sessions [277](#network-slice-admission-control-for-maximum-number-of-pdu-sessions)

5.15.11.2.1 Non- Hierarchical NSAC architecture [277](#non--hierarchical-nsac-architecture)

5.15.11.2.2 Hierarchical NSAC architecture [277](#hierarchical-nsac-architecture-1)

5.15.11.2.3 Centralized NSAC architecture [278](#centralized-nsac-architecture-1)

5.15.11.3 Network Slice Admission Control for Roaming [278](#network-slice-admission-control-for-roaming)

5.15.11.3.0 General [278](#general-51)

5.15.11.3.1 VPLMN NSAC Admission Mode [278](#vplmn-nsac-admission-mode)

5.15.11.3.2 VPLMN with HPLMN assistance NSAC Admission [279](#vplmn-with-hplmn-assistance-nsac-admission)

5.15.11.3.3 HPLMN NSAC Admission Mode [279](#hplmn-nsac-admission-mode)

5.15.11.4 Network Slice status notifications and reports to a consumer NF [279](#network-slice-status-notifications-and-reports-to-a-consumer-nf)

5.15.11.5 Support of Network Slice Admission Control and Interworking with EPC [280](#support-of-network-slice-admission-control-and-interworking-with-epc)

5.15.11.5a Support of Network Slice Admission Control in 5GS for maximum number of UEs with at least one PDU Session/PDN Connection [281](#a-support-of-network-slice-admission-control-in-5gs-for-maximum-number-of-ues-with-at-least-one-pdu-sessionpdn-connection)

5.15.12 Support of subscription-based restrictions to simultaneous registration of network slices [283](#support-of-subscription-based-restrictions-to-simultaneous-registration-of-network-slices)

5.15.12.1 General [283](#general-52)

5.15.12.2 UE and UE configuration aspects [283](#ue-and-ue-configuration-aspects)

5.15.13 Support of data rate limitation per Network Slice for a UE [284](#support-of-data-rate-limitation-per-network-slice-for-a-ue)

5.15.14 Network Slice AS Groups support [285](#network-slice-as-groups-support)

5.15.15 Support of Network Slice usage control [285](#support-of-network-slice-usage-control)

5.15.15.1 General [285](#general-53)

5.15.15.2 UE Configuration of network-controlled Slice Usage Policy [286](#ue-configuration-of-network-controlled-slice-usage-policy)

5.15.15.3 Network-based per UE Network Slice usage behaviour control [287](#network-based-per-ue-network-slice-usage-behaviour-control)

5.15.16 Optimized handling of temporarily available network slices [287](#optimized-handling-of-temporarily-available-network-slices)

5.15.17 Partial Network Slice support in a Registration Area [289](#partial-network-slice-support-in-a-registration-area)

5.15.18 Support for Network Slices with Network Slice Area of Service not matching deployed Tracking Areas [292](#support-for-network-slices-with-network-slice-area-of-service-not-matching-deployed-tracking-areas)

5.15.18.1 General [292](#general-54)

5.15.18.2 S-NSSAI location availability information [292](#s-nssai-location-availability-information)

5.15.18.3 Network based monitoring and enforcement of Network Slice Area of Service not matching deployed Tracking Areas [293](#network-based-monitoring-and-enforcement-of-network-slice-area-of-service-not-matching-deployed-tracking-areas)

5.15.19 Support of Network Slice Replacement [294](#support-of-network-slice-replacement)

5.15.20 Support of Network Slice Instance Replacement [297](#support-of-network-slice-instance-replacement)

5.16 Support for specific services [297](#support-for-specific-services)

5.16.1 Public Warning System [297](#public-warning-system-1)

5.16.2 SMS over NAS [297](#sms-over-nas-1)

5.16.2.1 General [297](#general-55)

5.16.2.2 SMS over NAS transport [298](#sms-over-nas-transport)

5.16.3 IMS support [298](#ims-support-1)

5.16.3.1 General [298](#general-56)

5.16.3.2 IMS voice over PS Session Supported Indication over 3GPP access [298](#ims-voice-over-ps-session-supported-indication-over-3gpp-access)

5.16.3.2a IMS voice over PS Session Supported Indication over non-3GPP access [299](#a-ims-voice-over-ps-session-supported-indication-over-non-3gpp-access)

5.16.3.3 Homogeneous support for IMS voice over PS Session supported indication [299](#homogeneous-support-for-ims-voice-over-ps-session-supported-indication)

5.16.3.4 P-CSCF address delivery [300](#p-cscf-address-delivery)

5.16.3.5 Domain selection for UE originating sessions / calls [300](#domain-selection-for-ue-originating-sessions-calls)

5.16.3.6 Terminating domain selection for IMS voice [301](#terminating-domain-selection-for-ims-voice)

5.16.3.7 UE's usage setting [301](#ues-usage-setting)

5.16.3.8 Domain and Access Selection for UE originating SMS [301](#domain-and-access-selection-for-ue-originating-sms)

5.16.3.8.1 UE originating SMS for IMS Capable UEs supporting SMS over IP [301](#ue-originating-sms-for-ims-capable-ues-supporting-sms-over-ip)

5.16.3.8.2 Access Selection for SMS over NAS [301](#access-selection-for-sms-over-nas)

5.16.3.9 SMF support for P-CSCF restoration procedure [302](#smf-support-for-p-cscf-restoration-procedure)

5.16.3.10 IMS Voice Service via EPS Fallback or RAT fallback in 5GS [302](#ims-voice-service-via-eps-fallback-or-rat-fallback-in-5gs)

5.16.3.11 P-CSCF discovery and selection [302](#p-cscf-discovery-and-selection)

5.16.3.12 HSS discovery and selection [303](#hss-discovery-and-selection)

5.16.4 Emergency Services [303](#emergency-services)

5.16.4.1 Introduction [303](#introduction-1)

5.16.4.2 Architecture Reference Model for Emergency Services [306](#architecture-reference-model-for-emergency-services)

5.16.4.3 Mobility Restrictions and Access Restrictions for Emergency Services [306](#mobility-restrictions-and-access-restrictions-for-emergency-services)

5.16.4.4 Reachability Management [307](#reachability-management)

5.16.4.5 SMF and UPF selection function for Emergency Services [307](#smf-and-upf-selection-function-for-emergency-services)

5.16.4.6 QoS for Emergency Services [307](#qos-for-emergency-services)

5.16.4.7 PCC for Emergency Services [307](#pcc-for-emergency-services)

5.16.4.8 IP Address Allocation [307](#ip-address-allocation)

5.16.4.9 Handling of PDU Sessions for Emergency Services [307](#handling-of-pdu-sessions-for-emergency-services)

5.16.4.9a Handling of PDU Sessions for normal services for Emergency Registered UEs [308](#a-handling-of-pdu-sessions-for-normal-services-for-emergency-registered-ues)

5.16.4.10 Support of eCall Only Mode [308](#support-of-ecall-only-mode)

5.16.4.11 Emergency Services Fallback [308](#emergency-services-fallback)

5.16.5 Multimedia Priority Services [309](#multimedia-priority-services)

5.16.6 Mission Critical Services [311](#mission-critical-services)

5.17 Interworking and Migration [312](#interworking-and-migration)

5.17.1 Support for Migration from EPC to 5GC [312](#support-for-migration-from-epc-to-5gc)

5.17.1.1 General [312](#general-57)

5.17.1.2 User Plane management to support interworking with EPS [314](#user-plane-management-to-support-interworking-with-eps)

5.17.1.3 QoS handling for home routed roaming [314](#qos-handling-for-home-routed-roaming)

5.17.2 Interworking with EPC [314](#interworking-with-epc-1)

5.17.2.1 General [314](#general-58)

5.17.2.2 Interworking Procedures with N26 interface [318](#interworking-procedures-with-n26-interface)

5.17.2.2.1 General [318](#general-59)

5.17.2.2.2 Mobility for UEs in single-registration mode [319](#mobility-for-ues-in-single-registration-mode)

5.17.2.3 Interworking Procedures without N26 interface [320](#interworking-procedures-without-n26-interface)

5.17.2.3.1 General [320](#general-60)

5.17.2.3.2 Mobility for UEs in single-registration mode [321](#mobility-for-ues-in-single-registration-mode-1)

5.17.2.3.3 Mobility for UEs in dual-registration mode [321](#mobility-for-ues-in-dual-registration-mode)

5.17.2.3.4 Redirection for UEs in connected state [323](#redirection-for-ues-in-connected-state)

5.17.2.4 Mobility between 5GS and GERAN/UTRAN [323](#mobility-between-5gs-and-geranutran)

5.17.2.5 Secondary DN authentication and authorization in EPS Interworking case [324](#secondary-dn-authentication-and-authorization-in-eps-interworking-case)

5.17.3 Interworking with EPC in presence of Non-3GPP PDU Sessions [324](#interworking-with-epc-in-presence-of-non-3gpp-pdu-sessions)

5.17.4 Network sharing support and interworking between EPS and 5GS [325](#network-sharing-support-and-interworking-between-eps-and-5gs)

5.17.5 Service Exposure in Interworking Scenarios [325](#service-exposure-in-interworking-scenarios-1)

5.17.5.1 General [325](#general-61)

5.17.5.2 Support of interworking for Monitoring Events [326](#support-of-interworking-for-monitoring-events)

5.17.5.2.1 Interworking with N26 interface [326](#interworking-with-n26-interface)

5.17.5.2.2 Interworking without N26 interface [326](#interworking-without-n26-interface)

5.17.5.3 Availability or expected level of a service API [326](#availability-or-expected-level-of-a-service-api)

5.17.6 Void [327](#void-6)

5.17.7 Configuration Transfer Procedure between NG-RAN and E-UTRAN [327](#_Toc217021352)

5.17.7.1 Architecture Principles for Configuration Transfer between NG-RAN and E-UTRAN [327](#architecture-principles-for-configuration-transfer-between-ng-ran-and-e-utran)

5.17.7.2 Addressing, routing and relaying [328](#addressing-routing-and-relaying)

5.17.7.2.1 Addressing [328](#addressing)

5.17.7.2.2 Routing [328](#routing)

5.17.7.2.3 Relaying [329](#relaying)

5.17.8 URSP Provisioning in EPS [329](#ursp-provisioning-in-eps)

5.18 Network Sharing [331](#network-sharing)

5.18.1 General concepts [331](#general-concepts-1)

5.18.2 Broadcast system information for network sharing [332](#broadcast-system-information-for-network-sharing)

5.18.2a PLMN list and SNPN list handling for network sharing [332](#a-plmn-list-and-snpn-list-handling-for-network-sharing)

5.18.3 Network selection by the UE [332](#network-selection-by-the-ue)

5.18.4 Network selection by the network [333](#network-selection-by-the-network)

5.18.5 Network Sharing and Network Slicing [334](#network-sharing-and-network-slicing)

5.19 Control Plane Load Control, Congestion and Overload Control [334](#control-plane-load-control-congestion-and-overload-control)

5.19.1 General [334](#general-62)

5.19.2 TNLA Load Balancing and TNLA Load Re-Balancing [334](#tnla-load-balancing-and-tnla-load-re-balancing)

5.19.3 AMF Load Balancing [334](#amf-load-balancing)

5.19.4 AMF Load Re-Balancing [334](#amf-load-re-balancing)

5.19.5 AMF Control Of Overload [335](#amf-control-of-overload)

5.19.5.1 General [335](#general-63)

5.19.5.2 AMF Overload Control [335](#amf-overload-control)

5.19.6 SMF Overload Control [336](#smf-overload-control)

5.19.7 NAS level congestion control [336](#nas-level-congestion-control)

5.19.7.1 General [336](#general-64)

5.19.7.2 General NAS level congestion control [337](#general-nas-level-congestion-control)

5.19.7.3 DNN based congestion control [338](#dnn-based-congestion-control)

5.19.7.4 S-NSSAI based congestion control [339](#s-nssai-based-congestion-control)

5.19.7.5 Group specific NAS level congestion control [341](#group-specific-nas-level-congestion-control)

5.19.7.6 Control Plane data specific NAS level congestion control [341](#control-plane-data-specific-nas-level-congestion-control)

5.20 External Exposure of Network Capability [342](#external-exposure-of-network-capability)

5.20a Data Collection from an AF [343](#a-data-collection-from-an-af)

5.20b Support exposure of DNN and S-NSSAI specific Group Parameters [344](#b-support-exposure-of-dnn-and-s-nssai-specific-group-parameters)

5.20b.1 Group attribute provisioning [344](#b.1-group-attribute-provisioning)

5.20b.2 Support LADN service area for a group [344](#b.2-support-ladn-service-area-for-a-group)

5.20b.3 Support QoS for a group [344](#b.3-support-qos-for-a-group)

5.20b.4 Void [344](#b.4-void)

5.20b.5 Void [344](#b.5-void)

5.20c Provisioning of traffic characteristics and monitoring of performance characteristics for a group [345](#c-provisioning-of-traffic-characteristics-and-monitoring-of-performance-characteristics-for-a-group)

5.20d User Plane Direct 5GS Information Exposure [345](#d-user-plane-direct-5gs-information-exposure)

5.20d.1 General [345](#d.1-general)

5.21 Architectural support for virtualized deployments [346](#architectural-support-for-virtualized-deployments)

5.21.0 General [346](#general-65)

5.21.1 Architectural support for N2 [346](#architectural-support-for-n2)

5.21.1.1 TNL associations [346](#tnl-associations)

5.21.1.2 NGAP UE-TNLA-binding [347](#ngap-ue-tnla-binding)

5.21.1.3 N2 TNL association selection [347](#n2-tnl-association-selection)

5.21.2 AMF Management [347](#amf-management)

5.21.2.1 AMF Addition/Update [347](#amf-additionupdate)

5.21.2.2 AMF planned removal procedure [348](#amf-planned-removal-procedure)

5.21.2.2.1 AMF planned removal procedure with UDSF deployed [348](#amf-planned-removal-procedure-with-udsf-deployed)

5.21.2.2.2 AMF planned removal procedure without UDSF [349](#amf-planned-removal-procedure-without-udsf)

5.21.2.3 Procedure for AMF Auto-recovery [351](#procedure-for-amf-auto-recovery)

5.21.3 Network Reliability support with Sets [352](#network-reliability-support-with-sets)

5.21.3.1 General [352](#general-66)

5.21.3.2 NF Set and NF Service Set [353](#nf-set-and-nf-service-set)

5.21.3.3 Reliability of NF instances within the same NF Set [353](#reliability-of-nf-instances-within-the-same-nf-set)

5.21.3.4 Reliability of NF Services [353](#reliability-of-nf-services)

5.21.4 Network Function/NF Service Context Transfer [353](#network-functionnf-service-context-transfer)

5.21.4.1 General [353](#general-67)

5.22 System Enablers for priority mechanism [354](#system-enablers-for-priority-mechanism)

5.22.1 General [354](#general-68)

5.22.2 Subscription-related Priority Mechanisms [354](#subscription-related-priority-mechanisms)

5.22.3 Invocation-related Priority Mechanisms [355](#invocation-related-priority-mechanisms)

5.22.4 QoS Mechanisms applied to established QoS Flows [356](#qos-mechanisms-applied-to-established-qos-flows)

5.23 Supporting for Asynchronous Type Communication [357](#supporting-for-asynchronous-type-communication)

5.24 3GPP PS Data Off [357](#gpp-ps-data-off)

5.25 Support of OAM Features [358](#support-of-oam-features)

5.25.1 Support of Tracing: Signalling Based Activation/Deactivation of Tracing [358](#support-of-tracing-signalling-based-activationdeactivation-of-tracing)

5.25.2 Support of OAM-based 5G VN group management [359](#support-of-oam-based-5g-vn-group-management)

5.25.3 Signalling Based Activation of QoE Measurement Collection [359](#signalling-based-activation-of-qoe-measurement-collection)

5.26 Configuration Transfer Procedure [359](#configuration-transfer-procedure)

5.26.1 Architecture Principles for Configuration Transfer [359](#architecture-principles-for-configuration-transfer)

5.26.2 Addressing, routing and relaying [360](#addressing-routing-and-relaying-1)

5.26.2.1 Addressing [360](#addressing-1)

5.26.2.2 Routing [360](#routing-1)

5.26.2.3 Relaying [360](#relaying-1)

5.27 Enablers for Time Sensitive Communications, Time Synchronization and Deterministic Networking [360](#enablers-for-time-sensitive-communications-time-synchronization-and-deterministic-networking)

5.27.0 General [360](#general-69)

5.27.1 Time Synchronization [361](#time-synchronization)

5.27.1.1 General [361](#general-70)

5.27.1.2 Distribution of timing information [362](#distribution-of-timing-information)

5.27.1.2.1 Distribution of 5G internal system clock [362](#distribution-of-5g-internal-system-clock)

5.27.1.2.2 Distribution of grandmaster clock and time-stamping [362](#distribution-of-grandmaster-clock-and-time-stamping)

5.27.1.3 Support for multiple (g)PTP domains [365](#support-for-multiple-gptp-domains)

5.27.1.4 DS-TT and NW-TT Time Synchronization functionality [366](#ds-tt-and-nw-tt-time-synchronization-functionality)

5.27.1.5 Detection of (g)PTP Sync and Announce timeouts [367](#detection-of-gptp-sync-and-announce-timeouts)

5.27.1.6 Distribution of Announce messages and best master clock selection [367](#distribution-of-announce-messages-and-best-master-clock-selection)

5.27.1.7 Support for PTP grandmaster function in 5GS [368](#support-for-ptp-grandmaster-function-in-5gs)

5.27.1.8 Exposure of Time Synchronization [368](#exposure-of-time-synchronization)

5.27.1.9 Support for derivation of Uu time synchronization error budget [370](#support-for-derivation-of-uu-time-synchronization-error-budget)

5.27.1.10 Support for coverage area filters for time synchronization service [370](#support-for-coverage-area-filters-for-time-synchronization-service)

5.27.1.11 Controlling time synchronization service based on the Subscription [371](#controlling-time-synchronization-service-based-on-the-subscription)

5.27.1.12 Support for network timing synchronization status monitoring [374](#support-for-network-timing-synchronization-status-monitoring)

5.27.1a Periodic deterministic communication [377](#a-periodic-deterministic-communication)

5.27.2 TSC Assistance Information (TSCAI) and TSC Assistance Container (TSCAC) [378](#tsc-assistance-information-tscai-and-tsc-assistance-container-tscac)

5.27.2.1 General [378](#general-71)

5.27.2.2 TSC Assistance Container determination based on PSFP [379](#tsc-assistance-container-determination-based-on-psfp)

5.27.2.3 TSC Assistance Container determination by TSCTSF [380](#tsc-assistance-container-determination-by-tsctsf)

5.27.2.4 TSCAI determination based on TSC Assistance Container [381](#tscai-determination-based-on-tsc-assistance-container)

5.27.2.5 RAN feedback for Burst Arrival Time offset and adjusted Periodicity [382](#ran-feedback-for-burst-arrival-time-offset-and-adjusted-periodicity)

5.27.2.5.1 Overview [382](#overview-2)

5.27.2.5.2 Proactive RAN feedback for adaptation of Burst Arrival Time and Periodicity [382](#proactive-ran-feedback-for-adaptation-of-burst-arrival-time-and-periodicity)

5.27.2.5.3 Reactive RAN feedback for Burst Arrival Time adaptation [383](#reactive-ran-feedback-for-burst-arrival-time-adaptation)

5.27.3 Support for TSC QoS Flows [383](#support-for-tsc-qos-flows)

5.27.4 Hold and Forward Buffering mechanism [384](#hold-and-forward-buffering-mechanism)

5.27.5 5G System Bridge delay [384](#g-system-bridge-delay)

5.28 Support of integration with TSN, Time Sensitive Communications, Time Synchronization and Deterministic Networking [385](#support-of-integration-with-tsn-time-sensitive-communications-time-synchronization-and-deterministic-networking)

5.28.0 General [385](#general-72)

5.28.1 5GS bridge management for TSN [385](#gs-bridge-management-for-tsn)

5.28.2 5GS Bridge configuration for TSN [387](#gs-bridge-configuration-for-tsn)

5.28.3 Port and user plane node management information exchange in 5GS [389](#port-and-user-plane-node-management-information-exchange-in-5gs)

5.28.3.1 General [389](#general-73)

5.28.3.2 Transfer of port or user plane node management information [390](#transfer-of-port-or-user-plane-node-management-information)

5.28.3.3 VLAN Configuration Information for TSN [391](#vlan-configuration-information-for-tsn)

5.28.4 QoS mapping tables for TSN [391](#qos-mapping-tables-for-tsn)

5.28.5 Support of integration with IETF Deterministic Networking [393](#support-of-integration-with-ietf-deterministic-networking)

5.28.5.1 General [393](#general-74)

5.28.5.2 5GS DetNet node reporting [393](#gs-detnet-node-reporting)

5.28.5.3 DetNet node configuration mapping in 5GS [394](#detnet-node-configuration-mapping-in-5gs)

5.28a Support for TSN enabled Transport Network [395](#a-support-for-tsn-enabled-transport-network)

5.28a.1 General [395](#a.1-general)

5.28a.2 Transfer of TL-Container between SMF/CUC and AN-TL and CN-TL [395](#a.2-transfer-of-tl-container-between-smfcuc-and-an-tl-and-cn-tl)

5.28a.3 Topology Information for TSN TN [396](#a.3-topology-information-for-tsn-tn)

5.29 Support for 5G LAN-type service [396](#support-for-5g-lan-type-service)

5.29.1 General [396](#general-75)

5.29.2 5G VN group management [397](#g-vn-group-management)

5.29.3 PDU Session management [398](#pdu-session-management)

5.29.4 User Plane handling [399](#user-plane-handling)

5.30 Support for non-public networks [400](#support-for-non-public-networks)

5.30.1 General [400](#general-76)

5.30.2 Stand-alone Non-Public Networks [401](#stand-alone-non-public-networks)

5.30.2.0 General [401](#general-77)

5.30.2.1 Identifiers [401](#identifiers-1)

5.30.2.2 Broadcast system information [402](#broadcast-system-information)

5.30.2.3 UE configuration and subscription aspects [403](#ue-configuration-and-subscription-aspects)

5.30.2.4 Network selection in SNPN access mode [405](#network-selection-in-snpn-access-mode)

5.30.2.4.1 General [405](#general-78)

5.30.2.4.2 Automatic network selection [406](#automatic-network-selection)

5.30.2.4.3 Manual network selection [408](#manual-network-selection)

5.30.2.5 Network access control [408](#network-access-control-1)

5.30.2.6 Cell (re-)selection in SNPN access mode [408](#cell-re-selection-in-snpn-access-mode)

5.30.2.7 Access to PLMN services via stand-alone non-public networks [408](#access-to-plmn-services-via-stand-alone-non-public-networks)

5.30.2.8 Access to stand-alone non-public network services via PLMN [409](#access-to-stand-alone-non-public-network-services-via-plmn)

5.30.2.9 SNPN connectivity for UEs with credentials owned by Credentials Holder [409](#snpn-connectivity-for-ues-with-credentials-owned-by-credentials-holder)

5.30.2.9.1 General [409](#general-79)

5.30.2.9.2 Credentials Holder using AAA Server for primary authentication and authorization [410](#credentials-holder-using-aaa-server-for-primary-authentication-and-authorization)

5.30.2.9.3 Credentials Holder using AUSF and UDM for primary authentication and authorization [411](#credentials-holder-using-ausf-and-udm-for-primary-authentication-and-authorization)

5.30.2.10 Onboarding of UEs for SNPNs [412](#onboarding-of-ues-for-snpns)

5.30.2.10.1 General [412](#general-80)

5.30.2.10.2 Onboarding Network is an SNPN [412](#onboarding-network-is-an-snpn)

5.30.2.10.3 Onboarding Network is a PLMN [417](#onboarding-network-is-a-plmn)

5.30.2.10.4 Remote Provisioning of UEs in Onboarding Network [417](#remote-provisioning-of-ues-in-onboarding-network)

5.30.2.11 UE Mobility support for SNPN [419](#ue-mobility-support-for-snpn)

5.30.2.12 Access to SNPN services via Untrusted non-3GPP access [420](#access-to-snpn-services-via-untrusted-non-3gpp-access)

5.30.2.13 Access to SNPN services via Trusted non-3GPP access [421](#access-to-snpn-services-via-trusted-non-3gpp-access)

5.30.2.14 Access to SNPN services via wireline access network [422](#access-to-snpn-services-via-wireline-access-network)

5.30.2.15 Access to SNPN services for N5CW devices [422](#access-to-snpn-services-for-n5cw-devices)

5.30.3 Public Network Integrated NPN [422](#public-network-integrated-npn)

5.30.3.1 General [422](#general-84)

5.30.3.2 Identifiers [423](#identifiers-2)

5.30.3.3 UE configuration, subscription aspects and storage [423](#ue-configuration-subscription-aspects-and-storage)

5.30.3.4 Network and cell (re-)selection and access control [424](#network-and-cell-re-selection-and-access-control)

5.30.3.5 Support of emergency services in CAG cells [426](#support-of-emergency-services-in-cag-cells)

5.31 Support for Cellular IoT [426](#support-for-cellular-iot)

5.31.1 General [426](#general-85)

5.31.2 Preferred and Supported Network Behaviour [426](#preferred-and-supported-network-behaviour)

5.31.3 Selection, steering and redirection between EPS and 5GS [427](#selection-steering-and-redirection-between-eps-and-5gs)

5.31.4 Control Plane CIoT 5GS Optimisation [428](#control-plane-ciot-5gs-optimisation)

5.31.4.1 General [428](#general-86)

5.31.4.2 Establishment of N3 data transfer during Data Transport in Control Plane CIoT 5GS Optimisation [429](#establishment-of-n3-data-transfer-during-data-transport-in-control-plane-ciot-5gs-optimisation)

5.31.4.3 Control Plane Relocation Indication procedure [429](#control-plane-relocation-indication-procedure)

5.31.5 Non-IP Data Delivery (NIDD) [429](#non-ip-data-delivery-nidd)

5.31.6 Reliable Data Service [430](#reliable-data-service)

5.31.7 Power Saving Enhancements [431](#power-saving-enhancements)

5.31.7.1 General [431](#general-87)

5.31.7.2 Extended Discontinuous Reception (DRX) for CM-IDLE and CM-CONNECTED with RRC-INACTIVE [431](#extended-discontinuous-reception-drx-for-cm-idle-and-cm-connected-with-rrc-inactive)

5.31.7.2.1 Overview [431](#overview-3)

5.31.7.2.2 Paging for extended idle mode DRX in E-UTRA and NR connected to 5GC [433](#paging-for-extended-idle-mode-drx-in-e-utra-and-nr-connected-to-5gc)

5.31.7.2.3 Paging for a UE registered in a tracking area with heterogeneous support of extended idle mode DRX [434](#paging-for-a-ue-registered-in-a-tracking-area-with-heterogeneous-support-of-extended-idle-mode-drx)

5.31.7.2.4 Paging for extended DRX for RRC_INACTIVE in NR connected to 5GC [434](#paging-for-extended-drx-for-rrc_inactive-in-nr-connected-to-5gc)

5.31.7.3 MICO mode with Extended Connected Time [435](#mico-mode-with-extended-connected-time)

5.31.7.4 MICO mode with Active Time [435](#mico-mode-with-active-time)

5.31.7.5 MICO mode and Periodic Registration Timer Control [435](#mico-mode-and-periodic-registration-timer-control)

5.31.8 High latency communication [436](#high-latency-communication)

5.31.9 Support for Monitoring Events [437](#support-for-monitoring-events)

5.31.10 NB-IoT UE Radio Capability Handling [437](#nb-iot-ue-radio-capability-handling)

5.31.11 Inter-RAT idle mode mobility to and from NB-IoT [437](#inter-rat-idle-mode-mobility-to-and-from-nb-iot)

5.31.12 Restriction of use of Enhanced Coverage [438](#restriction-of-use-of-enhanced-coverage)

5.31.13 Paging for Enhanced Coverage [439](#paging-for-enhanced-coverage)

5.31.14 Support of rate control of user data [439](#support-of-rate-control-of-user-data)

5.31.14.1 General [439](#general-89)

5.31.14.2 Serving PLMN Rate Control [439](#serving-plmn-rate-control)

5.31.14.3 Small Data Rate Control [440](#small-data-rate-control)

5.31.15 Control Plane Data Transfer Congestion Control [441](#control-plane-data-transfer-congestion-control)

5.31.16 Service Gap Control [441](#service-gap-control)

5.31.17 Inter-UE QoS for NB-IoT [443](#inter-ue-qos-for-nb-iot)

5.31.18 User Plane CIoT 5GS Optimisation [443](#user-plane-ciot-5gs-optimisation)

5.31.19 QoS model for NB-IoT [444](#qos-model-for-nb-iot)

5.31.20 Category M UEs differentiation [444](#category-m-ues-differentiation)

5.32 Support for ATSSS [445](#support-for-atsss)

5.32.1 General [445](#general-90)

5.32.2 Multi Access PDU Sessions [446](#multi-access-pdu-sessions)

5.32.3 Policy for ATSSS Control [451](#policy-for-atsss-control)

5.32.4 QoS Support [452](#qos-support)

5.32.5 Access Network Performance Measurements [453](#access-network-performance-measurements)

5.32.5.1 General principles [453](#general-principles)

5.32.5.1a Address of PMF messages [456](#a-address-of-pmf-messages)

5.32.5.2 Round Trip Time Measurements [457](#round-trip-time-measurements)

5.32.5.2a Packet Loss Rate Measurements [457](#a-packet-loss-rate-measurements)

5.32.5.3 Access Availability/Unavailability Report [458](#access-availabilityunavailability-report)

5.32.5.4 Protocol stack for user plane measurements and measurement reports [459](#protocol-stack-for-user-plane-measurements-and-measurement-reports)

5.32.5.5 UE Assistance Operation [460](#ue-assistance-operation)

5.32.5.6 Suspend and Resume Traffic Duplication [460](#suspend-and-resume-traffic-duplication)

5.32.6 Support of Steering Functionalities [461](#support-of-steering-functionalities)

5.32.6.1 General [461](#general-91)

5.32.6.2 High-Layer Steering Functionalities [463](#high-layer-steering-functionalities)

5.32.6.2.1 MPTCP Functionality [463](#mptcp-functionality)

5.32.6.2.2 MPQUIC Functionality [464](#mpquic-functionality)

5.32.6.3 Low-Layer Steering Functionalities [467](#low-layer-steering-functionalities)

5.32.6.3.1 ATSSS-LL Functionality [467](#atsss-ll-functionality)

5.32.7 Interworking with EPS [467](#interworking-with-eps)

5.32.7.1 General [467](#general-92)

5.32.7.2 Interworking with N26 Interface [468](#interworking-with-n26-interface-1)

5.32.7.3 Interworking without N26 Interface [469](#interworking-without-n26-interface-1)

5.32.8 ATSSS Rules [469](#atsss-rules)

5.33 Support for Ultra Reliable Low Latency Communication [473](#support-for-ultra-reliable-low-latency-communication)

5.33.1 General [473](#general-93)

5.33.2 Redundant transmission for high reliability communication [474](#redundant-transmission-for-high-reliability-communication)

5.33.2.1 Dual Connectivity based end to end Redundant User Plane Paths [474](#dual-connectivity-based-end-to-end-redundant-user-plane-paths)

5.33.2.2 Support of redundant transmission on N3/N9 interfaces [476](#support-of-redundant-transmission-on-n3n9-interfaces)

5.33.2.3 Support for redundant transmission at transport layer [478](#support-for-redundant-transmission-at-transport-layer)

5.33.3 QoS Monitoring for packet delay [478](#qos-monitoring-for-packet-delay)

5.33.3.1 General [478](#general-94)

5.33.3.2 Per QoS Flow per UE QoS Measurement [478](#per-qos-flow-per-ue-qos-measurement)

5.33.3.3 GTP-U Path Measurement [479](#gtp-u-path-measurement)

5.34 Support of deployments topologies with specific SMF Service Areas [481](#support-of-deployments-topologies-with-specific-smf-service-areas)

5.34.1 General [481](#general-95)

5.34.2 Architecture [482](#architecture-1)

5.34.2.1 SBA architecture [482](#sba-architecture)

5.34.2.2 Non-roaming architecture [482](#non-roaming-architecture-5)

5.34.2.3 Roaming architecture [483](#roaming-architecture-2)

5.34.3 I-SMF selection, V-SMF reselection [483](#i-smf-selection-v-smf-reselection)

5.34.4 Usage of an UL Classifier for a PDU Session controlled by I-SMF [484](#usage-of-an-ul-classifier-for-a-pdu-session-controlled-by-i-smf)

5.34.5 Usage of IPv6 multi-homing for a PDU Session controlled by I-SMF [485](#usage-of-ipv6-multi-homing-for-a-pdu-session-controlled-by-i-smf)

5.34.6 Interaction between I-SMF and SMF for the support of traffic offload by UPF controlled by the I-SMF [485](#interaction-between-i-smf-and-smf-for-the-support-of-traffic-offload-by-upf-controlled-by-the-i-smf)

5.34.6.1 General [485](#general-96)

5.34.6.2 N4 information sent from SMF to I-SMF for local traffic offload [486](#n4-information-sent-from-smf-to-i-smf-for-local-traffic-offload)

5.34.7 Event Management [487](#event-management)

5.34.7.1 UE's Mobility Event Management [487](#ues-mobility-event-management)

5.34.7.2 SMF event exposure service [487](#smf-event-exposure-service)

5.34.7.3 AMF implicit subscription about events related with the PDU Session [487](#amf-implicit-subscription-about-events-related-with-the-pdu-session)

5.34.8 Support for Cellular IoT [488](#support-for-cellular-iot-1)

5.34.9 Support of the Deployment Topologies with specific SMF Service Areas feature within and between PLMN(s) [488](#support-of-the-deployment-topologies-with-specific-smf-service-areas-feature-within-and-between-plmns)

5.34.10 Support for 5G LAN-type service [488](#support-for-5g-lan-type-service-1)

5.35 Support for Integrated access and backhaul (IAB) [488](#support-for-integrated-access-and-backhaul-iab)

5.35.1 IAB architecture and functional entities [488](#iab-architecture-and-functional-entities)

5.35.2 5G System enhancements to support IAB [490](#g-system-enhancements-to-support-iab)

5.35.3 Data handling and QoS support with IAB [490](#data-handling-and-qos-support-with-iab)

5.35.4 Mobility support with IAB [491](#mobility-support-with-iab)

5.35.5 Charging support with IAB [491](#charging-support-with-iab)

5.35.6 IAB operation involving EPC [491](#iab-operation-involving-epc)

5.35A Support for Mobile Base Station Relay (MBSR) [491](#a-support-for-mobile-base-station-relay-mbsr)

5.35A.1 General [491](#a.1-general-1)

5.35A.2 Configuration of the MBSR [492](#a.2-configuration-of-the-mbsr)

5.35A.3 Mobility support of UEs served by MBSR [492](#a.3-mobility-support-of-ues-served-by-mbsr)

5.35A.3.1 UE mobility between a fixed cell and MBSR cell [492](#a.3.1-ue-mobility-between-a-fixed-cell-and-mbsr-cell)

5.35A.3.2 UE mobility between MBSR cells [492](#a.3.2-ue-mobility-between-mbsr-cells)

5.35A.3.3 UE mobility when moving together with a MBSR cell [492](#a.3.3-ue-mobility-when-moving-together-with-a-mbsr-cell)

5.35A.3.4 MBSR mobility [492](#a.3.4-mbsr-mobility)

5.35A.4 MBSR authorization [493](#a.4-mbsr-authorization)

5.35A.5 Location Service Support of UEs served by MBSR [494](#a.5-location-service-support-of-ues-served-by-mbsr)

5.35A.6 Providing cell ID/TAC of MBSR for services [494](#a.6-providing-cell-idtac-of-mbsr-for-services)

5.35A.7 Control of UE access to MBSR [495](#a.7-control-of-ue-access-to-mbsr)

5.36 RIM Information Transfer [495](#rim-information-transfer)

5.37 Support for high data rate low latency services, eXtended Reality (XR) and interactive media services [495](#support-for-high-data-rate-low-latency-services-extended-reality-xr-and-interactive-media-services)

5.37.1 General [495](#general-97)

5.37.2 Policy control enhancements to support multi-modal services [496](#policy-control-enhancements-to-support-multi-modal-services)

5.37.3 Support of ECN marking for L4S to expose the congestion information [496](#support-of-ecn-marking-for-l4s-to-expose-the-congestion-information)

5.37.3.1 General [496](#general-98)

5.37.3.2 Support of ECN marking for L4S in NG-RAN [497](#support-of-ecn-marking-for-l4s-in-ng-ran)

5.37.3.3 Support of ECN marking for L4S in PSA UPF [497](#support-of-ecn-marking-for-l4s-in-psa-upf)

5.37.4 Network Exposure of 5GS information [498](#network-exposure-of-5gs-information)

5.37.5 PDU Set based Handling [499](#pdu-set-based-handling)

5.37.5.1 General [499](#general-99)

5.37.5.2 PDU Set Information and Identification [500](#pdu-set-information-and-identification)

5.37.5.3 Non-homogenous support of PDU set based handling in NG-RAN [500](#non-homogenous-support-of-pdu-set-based-handling-in-ng-ran)

5.37.6 UL/DL policy control based on round-trip latency requirement [501](#uldl-policy-control-based-on-round-trip-latency-requirement)

5.37.7 5GS Packet Delay Variation monitoring and reporting [501](#gs-packet-delay-variation-monitoring-and-reporting)

5.37.7.1 General [501](#general-100)

5.37.8 UE power saving management [502](#ue-power-saving-management)

5.37.8.1 General [502](#general-101)

5.37.8.2 Periodicity and N6 Jitter Information associated with Periodicity [502](#periodicity-and-n6-jitter-information-associated-with-periodicity)

5.37.8.3 End of Data Burst Indication [503](#end-of-data-burst-indication)

5.38 Support for Multi-USIM UE [503](#support-for-multi-usim-ue)

5.38.1 General [503](#general-102)

5.38.2 Connection Release [503](#connection-release)

5.38.3 Paging Cause Indication for Voice Service [504](#paging-cause-indication-for-voice-service)

5.38.4 Reject Paging Request [504](#reject-paging-request)

5.38.5 Paging Restriction [505](#paging-restriction)

5.38.6 Paging Timing Collision Control [505](#paging-timing-collision-control)

5.39 Remote provisioning of credentials for NSSAA or secondary authentication/authorization [506](#remote-provisioning-of-credentials-for-nssaa-or-secondary-authenticationauthorization)

5.39.1 General [506](#general-103)

5.39.2 Configuration for the UE [506](#configuration-for-the-ue)

5.40 Support of Disaster Roaming with Minimization of Service Interruption [506](#support-of-disaster-roaming-with-minimization-of-service-interruption)

5.40.1 General [506](#general-104)

5.40.2 UE configuration and provisioning for Disaster Roaming [507](#ue-configuration-and-provisioning-for-disaster-roaming)

5.40.3 Disaster Condition Notification and Determination [507](#disaster-condition-notification-and-determination)

5.40.4 Registration for Disaster Roaming service [508](#registration-for-disaster-roaming-service)

5.40.5 Handling when a Disaster Condition is no longer applicable [508](#handling-when-a-disaster-condition-is-no-longer-applicable)

5.40.6 Prevention of signalling overload related to Disaster Condition and Disaster Roaming service [509](#prevention-of-signalling-overload-related-to-disaster-condition-and-disaster-roaming-service)

5.41 NR RedCap and NR eRedCap UEs differentiation [509](#nr-redcap-and-nr-eredcap-ues-differentiation)

5.42 Support of Non-seamless WLAN offload [510](#support-of-non-seamless-wlan-offload)

5.43 Support for 5G Satellite Backhaul [511](#support-for-5g-satellite-backhaul)

5.43.1 General [511](#general-105)

5.43.2 Edge Computing via UPF deployed on satellite [511](#edge-computing-via-upf-deployed-on-satellite)

5.43.3 Local switch for UE-to-UE communications via UPF deployed on GEO satellite [512](#local-switch-for-ue-to-ue-communications-via-upf-deployed-on-geo-satellite)

5.43.3.1 General [512](#general-106)

5.43.3.2 Local switch with PSA UPF deployed on satellite [512](#local-switch-with-psa-upf-deployed-on-satellite)

5.43.3.3 Local switching with UL CL/BP and local PSA UPF deployed on satellite [513](#local-switching-with-ul-clbp-and-local-psa-upf-deployed-on-satellite)

5.43.4 Reporting of satellite backhaul to SMF [513](#reporting-of-satellite-backhaul-to-smf)

5.43.5 QoS monitoring when dynamic Satellite Backhaul is used [513](#qos-monitoring-when-dynamic-satellite-backhaul-is-used)

5.44 Support of Personal IoT network service [514](#support-of-personal-iot-network-service)

5.44.1 General [514](#general-107)

5.44.2 UE policy delivery for PIN [514](#ue-policy-delivery-for-pin)

5.44.3 Session management enhancement for PIN service support [514](#session-management-enhancement-for-pin-service-support)

5.44.3.1 PDU Session Establishment for PIN [514](#pdu-session-establishment-for-pin)

5.44.3.2 Session management related policy control [515](#session-management-related-policy-control)

5.44.3.3 Non-3GPP QoS Assistance Information [515](#non-3gpp-qos-assistance-information)

5.44.3.4 Non-3GPP delay budget between PINE and PEGC [515](#non-3gpp-delay-budget-between-pine-and-pegc)

5.44.4 Identifiers for PIN [516](#identifiers-for-pin)

5.45 QoS Monitoring [516](#qos-monitoring)

5.45.1 General [516](#general-108)

5.45.2 Packet delay monitoring [517](#packet-delay-monitoring)

5.45.3 Congestion information monitoring [517](#congestion-information-monitoring)

5.45.4 Data rate monitoring [517](#data-rate-monitoring)

5.45.5 Void [517](#void-7)

5.46 Assistance to AI/ML Operations in the Application Layer [518](#assistance-to-aiml-operations-in-the-application-layer)

5.46.1 General [518](#general-109)

5.46.2 Member UE selection assistance functionality for application operation [519](#member-ue-selection-assistance-functionality-for-application-operation)

5.47 Support for Network Controlled Repeater (NCR) [520](#support-for-network-controlled-repeater-ncr)

6 Network Functions [520](#network-functions-1)

6.1 General [520](#general-110)

6.2 Network Function Functional description [520](#network-function-functional-description)

6.2.1 AMF [520](#amf)

6.2.2 SMF [522](#smf)

6.2.3 UPF [524](#upf)

6.2.4 PCF [525](#pcf)

6.2.5 NEF [525](#nef)

6.2.5.0 NEF functionality [525](#nef-functionality)

6.2.5.1 Support for CAPIF [527](#support-for-capif)

6.2.5a Void [527](#a-void-1)

6.2.6 NRF [527](#nrf)

6.2.6.1 General [527](#general-111)

6.2.6.2 NF profile [528](#nf-profile)

6.2.6.3 SCP profile [530](#scp-profile)

6.2.7 UDM [531](#udm)

6.2.8 AUSF [531](#ausf)

6.2.9 N3IWF [531](#n3iwf)

6.2.9A TNGF [532](#a-tngf)

6.2.10 AF [532](#af)

6.2.11 UDR [533](#udr)

6.2.12 UDSF [533](#udsf)

6.2.13 SMSF [533](#smsf)

6.2.14 NSSF [533](#nssf)

6.2.15 5G-EIR [534](#g-eir)

6.2.16 LMF [534](#lmf)

6.2.16A GMLC [534](#a-gmlc)

6.2.17 SEPP [534](#sepp)

6.2.18 Network Data Analytics Function (NWDAF) [534](#network-data-analytics-function-nwdaf)

6.2.19 SCP [535](#scp)

6.2.20 W-AGF [535](#w-agf)

6.2.21 UE radio Capability Management Function (UCMF) [536](#ue-radio-capability-management-function-ucmf)

6.2.22 TWIF [536](#twif)

6.2.23 NSSAAF [536](#nssaaf)

6.2.24 DCCF [536](#dccf)

6.2.25 MFAF [537](#mfaf)

6.2.26 ADRF [537](#adrf)

6.2.27 MB-SMF [537](#mb-smf)

6.2.27a MB-UPF [537](#a-mb-upf)

6.2.27b MBSF [537](#b-mbsf)

6.2.27c MBSTF [537](#c-mbstf)

6.2.28 NSACF [538](#nsacf)

6.2.29 TSCTSF [538](#tsctsf)

6.2.30 5G DDNMF [539](#g-ddnmf)

6.2.31 EASDF [539](#easdf)

6.2.32 TSN AF [539](#tsn-af)

6.2.33 NSWOF [539](#nswof)

6.3 Principles for Network Function and Network Function Service discovery and selection [539](#principles-for-network-function-and-network-function-service-discovery-and-selection)

6.3.1 General [539](#general-112)

6.3.1.0 Principles for Binding, Selection and Reselection [541](#principles-for-binding-selection-and-reselection)

6.3.1.1 NF Discovery and Selection aspects relevant with indirect communication [543](#nf-discovery-and-selection-aspects-relevant-with-indirect-communication)

6.3.1.2 Location information [543](#location-information)

6.3.2 SMF discovery and selection [543](#smf-discovery-and-selection)

6.3.3 User Plane Function Selection [546](#user-plane-function-selection)

6.3.3.1 Overview [546](#overview-4)

6.3.3.2 SMF Provisioning of available UPF(s) [547](#smf-provisioning-of-available-upfs)

6.3.3.3 Selection of an UPF for a particular PDU Session [547](#selection-of-an-upf-for-a-particular-pdu-session)

6.3.4 AUSF discovery and selection [548](#ausf-discovery-and-selection)

6.3.5 AMF discovery and selection [549](#amf-discovery-and-selection)

6.3.6 N3IWF selection [552](#n3iwf-selection)

6.3.6.1 General [552](#general-113)

6.3.6.2 Stand-alone N3IWF selection [554](#stand-alone-n3iwf-selection)

6.3.6.2a SNPN N3IWF selection [555](#a-snpn-n3iwf-selection)

6.3.6.3 Combined N3IWF/ePDG Selection [556](#combined-n3iwfepdg-selection)

6.3.6.4 PLMN and non-3GPP access node Selection for emergency services [558](#plmn-and-non-3gpp-access-node-selection-for-emergency-services)

6.3.6.4.1 General [558](#general-114)

6.3.6.4.2 Stand-alone N3IWF selection [558](#stand-alone-n3iwf-selection-1)

6.3.6.3.3 Combined N3IWF/ePDG Selection [559](#combined-n3iwfepdg-selection-1)

6.3.7 PCF discovery and selection [560](#pcf-discovery-and-selection)

6.3.7.0 General principles [560](#general-principles-1)

6.3.7.1 PCF discovery and selection for a UE or a PDU Session [560](#pcf-discovery-and-selection-for-a-ue-or-a-pdu-session)

6.3.7.2 Providing policy requirements that apply to multiple UE and hence to multiple PCF [563](#providing-policy-requirements-that-apply-to-multiple-ue-and-hence-to-multiple-pcf)

6.3.7.3 Binding an AF request targeting a UE address to the relevant PCF [563](#binding-an-af-request-targeting-a-ue-address-to-the-relevant-pcf)

6.3.7.4 Binding an AF request targeting a UE to the relevant PCF [563](#binding-an-af-request-targeting-a-ue-to-the-relevant-pcf)

6.3.8 UDM discovery and selection [563](#udm-discovery-and-selection)

6.3.9 UDR discovery and selection [564](#udr-discovery-and-selection)

6.3.10 SMSF discovery and selection [565](#smsf-discovery-and-selection)

6.3.11 CHF discovery and selection [565](#chf-discovery-and-selection)

6.3.12 Trusted Non-3GPP Access Network selection [567](#trusted-non-3gpp-access-network-selection)

6.3.12.1 General [567](#general-115)

6.3.12.2 Access Network Selection Procedure [568](#access-network-selection-procedure)

6.3.12a Access Network selection for devices that do not support 5GC NAS over WLAN [571](#a-access-network-selection-for-devices-that-do-not-support-5gc-nas-over-wlan)

6.3.12a.1 General [571](#a.1-general-2)

6.3.12a.2 Access Network Selection Procedure [571](#a.2-access-network-selection-procedure)

6.3.12b Access Network selection for 5G NSWO [572](#b-access-network-selection-for-5g-nswo)

6.3.13 NWDAF discovery and selection [573](#nwdaf-discovery-and-selection)

6.3.14 NEF Discovery [574](#nef-discovery)

6.3.15 UCMF Discovery and Selection [575](#ucmf-discovery-and-selection)

6.3.16 SCP discovery and selection [575](#scp-discovery-and-selection)

6.3.17 NSSAAF discovery and selection [576](#nssaaf-discovery-and-selection)

6.3.18 5G-EIR discovery and selection [576](#g-eir-discovery-and-selection)

6.3.19 DCCF discovery and selection [576](#dccf-discovery-and-selection)

6.3.20 ADRF discovery and selection [577](#adrf-discovery-and-selection)

6.3.21 MFAF discovery and selection [577](#mfaf-discovery-and-selection)

6.3.22 NSACF discovery and selection [577](#nsacf-discovery-and-selection)

6.3.23 EASDF discovery and selection [578](#easdf-discovery-and-selection)

6.3.24 TSCTSF Discovery [578](#tsctsf-discovery)

6.3.25 AF Discovery and Selection [579](#af-discovery-and-selection)

6.3.26 NRF discovery and selection [579](#nrf-discovery-and-selection)

7 Network Function Services and descriptions [579](#network-function-services-and-descriptions)

7.1 Network Function Service Framework [579](#network-function-service-framework)

7.1.1 General [579](#general-116)

7.1.2 NF Service Consumer - NF Service Producer interactions [580](#nf-service-consumer---nf-service-producer-interactions)

7.1.3 Network Function Service discovery [582](#network-function-service-discovery)

7.1.4 Network Function Service Authorization [582](#network-function-service-authorization)

7.1.5 Network Function and Network Function Service registration and de-registration [583](#network-function-and-network-function-service-registration-and-de-registration)

7.2 Network Function Services [583](#network-function-services)

7.2.1 General [583](#general-117)

7.2.2 AMF Services [584](#amf-services)

7.2.3 SMF Services [585](#smf-services)

7.2.4 PCF Services [585](#pcf-services)

7.2.5 UDM Services [586](#udm-services)

7.2.6 NRF Services [587](#nrf-services)

7.2.7 AUSF Services [588](#ausf-services)

7.2.8 NEF Services [588](#_Toc217021807)

7.2.8A Void [591](#_Toc217021808)

7.2.9 SMSF Services [591](#smsf-services)

7.2.10 UDR Services [591](#udr-services)

7.2.11 5G-EIR Services [592](#g-eir-services)

7.2.12 NWDAF Services [592](#nwdaf-services)

7.2.13 UDSF Services [593](#udsf-services)

7.2.14 NSSF Services [593](#nssf-services)

7.2.15 BSF Services [594](#bsf-services)

7.2.16 LMF Services [594](#lmf-services)

7.2.16A GMLC Services [594](#a-gmlc-services)

7.2.17 CHF Services [594](#chf-services)

7.2.18 UCMF Services [595](#ucmf-services)

7.2.19 AF Services [595](#af-services)

7.2.20 NSSAAF Services [596](#nssaaf-services)

7.2.21 DCCF Services [596](#dccf-services)

7.2.22 MFAF Services [596](#mfaf-services)

7.2.23 ADRF Services [597](#adrf-services)

7.2.24 5G DDNMF Services [597](#g-ddnmf-services)

7.2.25 EASDF Services [597](#easdf-services)

7.2.26 TSCTSF Services [597](#tsctsf-services)

7.2.27 NSACF Services [598](#nsacf-services)

7.2.28 MB-SMF Services [598](#mb-smf-services)

7.2.29 UPF Services [599](#upf-services)

7.3 Exposure [599](#exposure)

8 Control and User Plane Protocol Stacks [599](#control-and-user-plane-protocol-stacks)

8.1 General [599](#general-118)

8.2 Control Plane Protocol Stacks [599](#control-plane-protocol-stacks)

8.2.1 Control Plane Protocol Stacks between the 5G-AN and the 5G Core: N2 [599](#control-plane-protocol-stacks-between-the-5g-an-and-the-5g-core-n2)

8.2.1.1 General [599](#general-119)

8.2.1.2 5G-AN - AMF [600](#g-an---amf)

8.2.1.3 5G-AN - SMF [601](#g-an---smf)

8.2.2 Control Plane Protocol Stacks between the UE and the 5GC [601](#control-plane-protocol-stacks-between-the-ue-and-the-5gc)

8.2.2.1 General [601](#general-120)

8.2.2.2 UE - AMF [603](#ue---amf)

8.2.2.3 UE – SMF [603](#ue-smf)

8.2.3 Control Plane Protocol Stacks between the network functions in 5GC [604](#control-plane-protocol-stacks-between-the-network-functions-in-5gc)

8.2.3.1 The Control Plane Protocol Stack for the service based interface [604](#the-control-plane-protocol-stack-for-the-service-based-interface)

8.2.3.2 The Control Plane protocol stack for the N4 interface between SMF and UPF [604](#the-control-plane-protocol-stack-for-the-n4-interface-between-smf-and-upf)

8.2.4 Control Plane for untrusted non 3GPP Access [604](#control-plane-for-untrusted-non-3gpp-access)

8.2.5 Control Plane for trusted non-3GPP Access [605](#control-plane-for-trusted-non-3gpp-access)

8.2.6 Control Plane for W-5GAN Access [606](#control-plane-for-w-5gan-access)

8.2.7 Control Plane for Trusted WLAN Access for N5CW Device [606](#control-plane-for-trusted-wlan-access-for-n5cw-device)

8.3 User Plane Protocol Stacks [606](#user-plane-protocol-stacks)

8.3.1 User Plane Protocol Stack for a PDU Session [606](#user-plane-protocol-stack-for-a-pdu-session)

8.3.2 User Plane for untrusted non-3GPP Access [608](#user-plane-for-untrusted-non-3gpp-access)

8.3.3 User Plane for trusted non-3GPP Access [608](#user-plane-for-trusted-non-3gpp-access)

8.3.4 User Plane for W-5GAN Access [608](#user-plane-for-w-5gan-access)

8.3.5 User Plane for N19-based forwarding of a 5G VN group [609](#user-plane-for-n19-based-forwarding-of-a-5g-vn-group)

8.3.6 User Plane for Trusted WLAN Access for N5CW Device [609](#user-plane-for-trusted-wlan-access-for-n5cw-device)

Annex A (informative): Relationship between Service-Based Interfaces and Reference Points [610](#annex-a-informative-relationship-between-service-based-interfaces-and-reference-points)

Annex B (normative): Mapping between temporary identities [612](#annex-b-normative-mapping-between-temporary-identities)

Annex C (informative): Guidelines and Principles for Compute-Storage Separation [613](#annex-c-informative-guidelines-and-principles-for-compute-storage-separation)

Annex D (informative): 5GS support for Non-Public Network deployment options [614](#annex-d-informative-5gs-support-for-non-public-network-deployment-options)

D.1 Introduction [614](#d.1-introduction)

D.2 Support of Non-Public Network as a network slice of a PLMN [614](#d.2-support-of-non-public-network-as-a-network-slice-of-a-plmn)

D.3 Support for access to PLMN services via Stand-alone Non-Public Network and access to Stand-alone Non Public Network services via PLMN [615](#d.3-support-for-access-to-plmn-services-via-stand-alone-non-public-network-and-access-to-stand-alone-non-public-network-services-via-plmn)

D.4 Support for UE capable of simultaneously connecting to an SNPN and a PLMN [616](#d.4-support-for-ue-capable-of-simultaneously-connecting-to-an-snpn-and-a-plmn)

D.5 Support for keeping UE in CM-CONNECTED state in overlay network when accessing services via NWu [616](#d.5-support-for-keeping-ue-in-cm-connected-state-in-overlay-network-when-accessing-services-via-nwu)

D.6 Support for session/service continuity between SNPN and PLMN when using N3IWF [617](#d.6-support-for-sessionservice-continuity-between-snpn-and-plmn-when-using-n3iwf)

D.7 Guidance for underlay network to support QoS differentiation for User Plane IPsec Child SA [618](#d.7-guidance-for-underlay-network-to-support-qos-differentiation-for-user-plane-ipsec-child-sa)

D.7.1 Network initiated QoS [618](#d.7.1-network-initiated-qos)

D.7.2 UE initiated QoS [619](#d.7.2-ue-initiated-qos)

Annex E (informative): Communication models for NF/NF services interaction [621](#annex-e-informative-communication-models-for-nfnf-services-interaction)

E.1 General [621](#e.1-general)

Annex F (informative): Redundant user plane paths based on multiple UEs per device [623](#annex-f-informative-redundant-user-plane-paths-based-on-multiple-ues-per-device)

Annex G (informative): SCP Deployment Examples [626](#annex-g-informative-scp-deployment-examples)

G.1 General [626](#g.1-general)

G.2 An SCP based on service mesh [626](#g.2-an-scp-based-on-service-mesh)

G.2.1 Introduction [626](#g.2.1-introduction)

G.2.2 Communication across service mesh boundaries [627](#g.2.2-communication-across-service-mesh-boundaries)

G.3 An SCP based on independent deployment units [628](#g.3-an-scp-based-on-independent-deployment-units)

G.4 An SCP deployment example based on name-based routing [629](#g.4-an-scp-deployment-example-based-on-name-based-routing)

G.4.0 General Information [629](#g.4.0-general-information)

G.4.1 Service Registration and Service Discovery [630](#g.4.1-service-registration-and-service-discovery)

G.4.2 Overview of Deployment Scenario [631](#g.4.2-overview-of-deployment-scenario)

G.4.3 References [631](#g.4.3-references)

Annex H (normative): PTP usage guidelines [632](#annex-h-normative-ptp-usage-guidelines)

H.1 General [632](#h.1-general)

H.2 Signalling of ingress time for time synchronization [632](#h.2-signalling-of-ingress-time-for-time-synchronization)

H.3 Void [632](#h.3-void)

H.4 Path and Link delay measurements [632](#h.4-path-and-link-delay-measurements)

Annex I (normative): TSN usage guidelines [634](#annex-i-normative-tsn-usage-guidelines)

I.1 Determination of traffic pattern information [634](#i.1-determination-of-traffic-pattern-information)

Annex J (informative): Link MTU considerations [636](#annex-j-informative-link-mtu-considerations)

Annex K (normative): Port and user plane node management information exchange [638](#annex-k-normative-port-and-user-plane-node-management-information-exchange)

K.1 Standardized port and user plane node management information [638](#k.1-standardized-port-and-user-plane-node-management-information)

K.2 Port and user plane node management information exchange for time synchronization [654](#k.2-port-and-user-plane-node-management-information-exchange-for-time-synchronization)

K.2.1 Capability exchange [654](#k.2.1-capability-exchange)

K.2.2 PTP Instance configuration [655](#k.2.2-ptp-instance-configuration)

K.2.2.1 General [655](#k.2.2.1-general)

K.2.2.2 Configuration for Sync and Announce reception timeouts [656](#k.2.2.2-configuration-for-sync-and-announce-reception-timeouts)

K.2.2.3 Configuration for PTP port states [656](#k.2.2.3-configuration-for-ptp-port-states)

K.2.2.4 Configuration for PTP grandmaster function [657](#k.2.2.4-configuration-for-ptp-grandmaster-function)

K.2.2.5 Configuration for Sync and Announce intervals [657](#k.2.2.5-configuration-for-sync-and-announce-intervals)

K.2.2.6 Configuration for transport protocols [658](#k.2.2.6-configuration-for-transport-protocols)

Annex L (normative): Support of GERAN/UTRAN access [659](#annex-l-normative-support-of-geranutran-access)

Annex M (normative): Interworking with TSN deployed in the Transport Network [660](#annex-m-normative-interworking-with-tsn-deployed-in-the-transport-network)

M.1 Mapping of the parameters between 5GS and TSN UNI [660](#m.1-mapping-of-the-parameters-between-5gs-and-tsn-uni)

M.2 TL-Container Information [664](#m.2-tl-container-information)

Annex N (informative): Support for access to Localized Services [667](#annex-n-informative-support-for-access-to-localized-services)

N.1 General [667](#n.1-general)

N.2 Enabling access to Localized Services [667](#n.2-enabling-access-to-localized-services)

N.2.1 General [667](#n.2.1-general)

N.2.2 Configuration of network to provide access to Localized Services [668](#n.2.2-configuration-of-network-to-provide-access-to-localized-services)

N.2.3 Session Management aspects [668](#n.2.3-session-management-aspects)

N.3 Selection of network providing access to Localized Services [668](#n.3-selection-of-network-providing-access-to-localized-services)

N.4 Enabling the UE access to Localized Services [668](#n.4-enabling-the-ue-access-to-localized-services)

N.5 Support for leaving network that provides access to Localized Services [668](#n.5-support-for-leaving-network-that-provides-access-to-localized-services)

N.6 Configuration of Credentials Holder for determining SNPN selection information [669](#n.6-configuration-of-credentials-holder-for-determining-snpn-selection-information)

Annex O (informative): Allowing UE to simultaneously send data to different groups with different QoS policy [671](#annex-o-informative-allowing-ue-to-simultaneously-send-data-to-different-groups-with-different-qos-policy)

O.1 A PDU Session with multiple QoS Flows for different groups [671](#o.1-a-pdu-session-with-multiple-qos-flows-for-different-groups)

O.2 Multiple PDU Sessions for different groups [672](#o.2-multiple-pdu-sessions-for-different-groups)

O.3 A PDU Session targeting a predefined group formed of multiple sub-groups [673](#o.3-a-pdu-session-targeting-a-predefined-group-formed-of-multiple-sub-groups)

Annex P (informative): Personal IoT Networks [675](#annex-p-informative-personal-iot-networks)

P.1 PIN Reference Architecture [675](#p.1-pin-reference-architecture)

P.2 Session management and traffic routing for PIN [675](#p.2-session-management-and-traffic-routing-for-pin)

Annex Q (informative): Satellite coverage availability information [677](#annex-q-informative-satellite-coverage-availability-information)

Annex R (informative): Change history [678](#annex-r-informative-change-history)

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
