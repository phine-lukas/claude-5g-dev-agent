<!-- table -->
| 3GPP TS 29.244 V18.10.0 (2025-06) (x2) |
| Technical Specification (x2) |
| 3rd Generation Partnership Project; Technical Specification Group Core Network and Terminals; Interface between the Control Plane and the User Plane Nodes; Stage 3 (Release 18) (x2) |
| The present document has been developed within the 3rd Generation Partnership Project (3GPP TM ) and may be further elaborated for the purposes of 3GPP. / The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented. / This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification. / Specifications and Reports for implementation of the 3GPP TM system should be obtained via the 3GPP Organizational Partners' Publications Offices. (x2) |
<!-- /table -->

<!-- table -->
| 3GPP Postal address 3GPP support office address 650 Route des Lucioles - Sophia Antipolis Valbonne - FRANCE Tel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16 Internet http://www.3gpp.org |
| Copyright Notification No part may be reproduced except as authorized by written permission. / The copyright and the foregoing restriction extend to reproduction in all media. © 2025, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC). All rights reserved. UMTS™ is a Trade Mark of ETSI registered for the benefit of its members 3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners / LTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners GSM® and the GSM logo are registered and owned by the GSM Association |
<!-- /table -->

#  Contents

Foreword [16](#foreword)

1 Scope [17](#scope)

2 References [17](#references)

3 Definitions, symbols and abbreviations [21](#definitions-symbols-and-abbreviations)

3.1 Definitions [21](#definitions)

3.2 Abbreviations [22](#abbreviations)

4 Protocol Stack [23](#protocol-stack)

4.1 Introduction [23](#introduction)

4.2 UDP Header and Port Numbers [24](#udp-header-and-port-numbers)

4.2.1 General [24](#general)

4.2.2 Request Message [25](#request-message)

4.2.3 Response Message [25](#response-message)

4.3 IP Header and IP Addresses [25](#ip-header-and-ip-addresses)

4.3.1 General [25](#general-1)

4.3.2 Request Message [25](#request-message-1)

4.3.3 Response Message [25](#response-message-1)

4.4 Layer 2 [25](#layer-2)

4.5 Layer 1 [25](#layer-1)

5 General description [25](#general-description)

5.1 Introduction [25](#introduction-1)

5.2 Packet Forwarding Model [26](#packet-forwarding-model)

5.2.1 General [26](#general-2)

5.2.1A Packet Detection Rule Handling [29](#a-packet-detection-rule-handling)

5.2.1A.1 General [29](#a.1-general)

5.2.1A.2 PDI Optimization [29](#a.2-pdi-optimization)

5.2.1A.2A Provisioning of SDF filters [29](#a.2a-provisioning-of-sdf-filters)

5.2.1A.3 Bidirectional SDF Filters [30](#a.3-bidirectional-sdf-filters)

5.2.1A.4 Application detection with PFD [30](#a.4-application-detection-with-pfd)

5.2.2 Usage Reporting Rule Handling [31](#usage-reporting-rule-handling)

5.2.2.1 General [31](#general-3)

5.2.2.2 Provisioning of Usage Reporting Rule in the UP function [31](#provisioning-of-usage-reporting-rule-in-the-up-function)

5.2.2.2.1 General [31](#general-4)

5.2.2.2.2 Credit pooling (for EPC) [36](#credit-pooling-for-epc)

5.2.2.3 Reporting of Usage Report to the CP function [36](#reporting-of-usage-report-to-the-cp-function)

5.2.2.3.1 General [36](#general-5)

5.2.2.3.2 Credit pooling [40](#credit-pooling)

5.2.2.3.3 Traffic Usage Reporting with Redundant Transmission [41](#traffic-usage-reporting-with-redundant-transmission)

5.2.2.4 Reporting of Linked Usage Reports to the CP function [41](#reporting-of-linked-usage-reports-to-the-cp-function)

5.2.2.5 End Marker Reception Reporting [41](#end-marker-reception-reporting)

5.2.3 Forwarding Action Rule Handling [42](#forwarding-action-rule-handling)

5.2.3.1 General [42](#general-6)

5.2.4 Buffering Action Rule Handling [44](#buffering-action-rule-handling)

5.2.4.1 General [44](#general-7)

5.2.4.2 Provisioning of Buffering Action Rule in the UP function [44](#provisioning-of-buffering-action-rule-in-the-up-function)

5.2.4.3 Applying DL Buffering Duration in the CP function [45](#applying-dl-buffering-duration-in-the-cp-function)

5.2.5 QoS Enforcement Rule Handling [45](#qos-enforcement-rule-handling)

5.2.5.1 General [45](#general-8)

5.2.5.2 Provisioning of QoS Enforcement Rule in the UP function [45](#provisioning-of-qos-enforcement-rule-in-the-up-function)

5.2.5.3 Reflective QoS (for 5GC) [46](#reflective-qos-for-5gc)

5.2.6 Combined SGW/PGW Architecture [46](#combined-sgwpgw-architecture)

5.2.7 Multi-Access Rule Handling (for 5GC) [46](#multi-access-rule-handling-for-5gc)

5.2.7.1 General [46](#general-9)

5.2.8 Session Reporting Rule Handling [48](#session-reporting-rule-handling)

5.2.8.1 General [48](#general-10)

5.2.8.2 Provisioning of Session Reporting Rule in the UP function [48](#provisioning-of-session-reporting-rule-in-the-up-function)

5.2.8.2.1 General [48](#general-11)

5.2.8.3 Reporting of Session Report to the CP function [48](#reporting-of-session-report-to-the-cp-function)

5.2.8.3.1 General [48](#general-12)

5.2.9 Handling of Rules that cannot be activated [49](#handling-of-rules-that-cannot-be-activated)

5.3 Data Forwarding between the CP and UP Functions [49](#data-forwarding-between-the-cp-and-up-functions)

5.3.1 General [49](#general-13)

5.3.2 Sending of End Marker Packets [50](#sending-of-end-marker-packets)

5.3.3 Forwarding of Packets Subject to Buffering in the CP Function [51](#forwarding-of-packets-subject-to-buffering-in-the-cp-function)

5.3.3.1 General [51](#general-14)

5.3.3.2 Forwarding of Packets from the UP Function to the CP Function [51](#forwarding-of-packets-from-the-up-function-to-the-cp-function)

5.3.3.3 Forwarding of Packets from the CP Function to the UP Function [52](#forwarding-of-packets-from-the-cp-function-to-the-up-function)

5.3.4 Data Forwarding between the CP and UP Functions with one PFCP-u Tunnel per UP Function or PDN [52](#data-forwarding-between-the-cp-and-up-functions-with-one-pfcp-u-tunnel-per-up-function-or-pdn)

5.3.4.1 General [52](#general-15)

5.3.4.2 Forwarding of Packets from the UP Function to the CP Function [52](#forwarding-of-packets-from-the-up-function-to-the-cp-function-1)

5.3.4.3 Forwarding of Packets from the CP Function to the UP Function [52](#forwarding-of-packets-from-the-cp-function-to-the-up-function-1)

5.3.5 Forwarding of user data using Control Plane CIoT 5GS Optimisation (for 5GC) [53](#forwarding-of-user-data-using-control-plane-ciot-5gs-optimisation-for-5gc)

5.3.5.1 General [53](#general-16)

5.3.5.2 Forwarding of Packets from the UP Function to the CP Function [53](#forwarding-of-packets-from-the-up-function-to-the-cp-function-2)

5.3.5.3 Forwarding of Packets from the CP Function to the UP Function [53](#forwarding-of-packets-from-the-cp-function-to-the-up-function-2)

5.4 Policy and Charging Control [54](#policy-and-charging-control)

5.4.1 General [54](#general-17)

5.4.2 Service Detection and Bearer/QoS Flow Binding [54](#service-detection-and-bearerqos-flow-binding)

5.4.3 Gating Control [55](#gating-control)

5.4.4 QoS Control [55](#qos-control)

5.4.5 DL Flow Level Marking for Application Detection [56](#dl-flow-level-marking-for-application-detection)

5.4.6 Usage Monitoring [56](#usage-monitoring)

5.4.7 Traffic Redirection [57](#traffic-redirection)

5.4.8 Traffic Steering [57](#traffic-steering)

5.4.9 Provisioning of Predefined PCC/ADC Rules [58](#provisioning-of-predefined-pccadc-rules)

5.4.10 Charging [59](#charging)

5.4.11 (Un)solicited Application Reporting [60](#unsolicited-application-reporting)

5.4.12 Service Identification for Improved Radio Utilisation for GERAN [61](#service-identification-for-improved-radio-utilisation-for-geran)

5.4.13 Transport Level Marking [61](#transport-level-marking)

5.4.14 Deferred PDR activation and deactivation [62](#deferred-pdr-activation-and-deactivation)

5.4.15 Packet Rate enforcement [62](#packet-rate-enforcement)

5.4.15.1 General [62](#general-18)

5.4.15.2 Packet rate enforcement over Sxb and N4 interfaces [63](#packet-rate-enforcement-over-sxb-and-n4-interfaces)

5.4.15.3 PGW and SMF behaviour [63](#pgw-and-smf-behaviour)

5.4.16 QoS differentiation for Stand-alone Non-Public Network (SNPN) [64](#qos-differentiation-for-stand-alone-non-public-network-snpn)

5.4.16.1 General [64](#general-19)

5.4.16.2 Access to PLMN services via SNPN [65](#access-to-plmn-services-via-snpn)

5.4.16.3 Access to SNPN services via PLMN [65](#access-to-snpn-services-via-plmn)

5.4.17 QoS differentiation for UEs behind RG [65](#qos-differentiation-for-ues-behind-rg)

5.5 F-TEID Allocation and Release [65](#f-teid-allocation-and-release)

5.5.1 General [65](#general-20)

5.5.2 Void [66](#void)

5.5.3 F-TEID allocation in the UP function [66](#f-teid-allocation-in-the-up-function)

5.6 PFCP Session Handling [66](#pfcp-session-handling)

5.6.1 General [66](#general-21)

5.6.2 Session Endpoint Identifier Handling [66](#session-endpoint-identifier-handling)

5.6.3 Modifying the Rules of an Existing PFCP Session [66](#modifying-the-rules-of-an-existing-pfcp-session)

5.7 Support of Lawful Interception [67](#support-of-lawful-interception)

5.7.1 General [67](#general-22)

5.7.2 Lawful Interception in EPC [67](#lawful-interception-in-epc)

5.7.3 Lawful Interception in 5GC [67](#lawful-interception-in-5gc)

5.8 PFCP Association [67](#pfcp-association)

5.8.1 General [67](#general-23)

5.8.2 Behaviour with an Established PFCP Association [68](#behaviour-with-an-established-pfcp-association)

5.8.3 Behaviour without an Established PFCP Association [69](#behaviour-without-an-established-pfcp-association)

5.9 Usage of Vendor-specific IE [69](#usage-of-vendor-specific-ie)

5.10 Error Indication Handling [69](#error-indication-handling)

5.10A User Plane Path Failure or Recovery Handling [70](#a-user-plane-path-failure-or-recovery-handling)

5.11 User plane inactivity detection and reporting [70](#user-plane-inactivity-detection-and-reporting)

5.11.1 General [70](#general-24)

5.11.2 User plane inactivity detection and reporting per PDN connection or PDU session [70](#user-plane-inactivity-detection-and-reporting-per-pdn-connection-or-pdu-session)

5.11.3 User plane inactivity detection and reporting per PDR [71](#user-plane-inactivity-detection-and-reporting-per-pdr)

5.12 Suspend and Resume Notification procedures [71](#suspend-and-resume-notification-procedures)

5.13 Ethernet traffic (for 5GC) [71](#ethernet-traffic-for-5gc)

5.13.1 General [71](#general-25)

5.13.2 Address Resolution Protocol or IPv6 Neighbour Solicitation Response by SMF [73](#address-resolution-protocol-or-ipv6-neighbour-solicitation-response-by-smf)

5.13.3 Address Resolution Protocol or IPv6 Neighbour Solicitation Response by UPF [73](#address-resolution-protocol-or-ipv6-neighbour-solicitation-response-by-upf)

5.13.3A Provisioning of MAC addresses and SDF filters in Ethernet Packet Filters [73](#a-provisioning-of-mac-addresses-and-sdf-filters-in-ethernet-packet-filters)

5.13.4 Bidirectional Ethernet Filters [74](#bidirectional-ethernet-filters)

5.13.5 Reporting of UE MAC addresses to the SMF [74](#reporting-of-ue-mac-addresses-to-the-smf)

5.13.6 Ethernet PDU session anchor relocation [74](#ethernet-pdu-session-anchor-relocation)

5.14 Support IPv6 Prefix Delegation [75](#support-ipv6-prefix-delegation)

5.15 Signalling based Trace (De)Activation [75](#signalling-based-trace-deactivation)

5.15A UE level measurement (De)Activation [76](#a-ue-level-measurement-deactivation)

5.15A.1 General [76](#a.1-general-1)

5.15A.2 UE level measurement only (De)Activation [77](#a.2-ue-level-measurement-only-deactivation)

5.15A.3 Signalling based Trace and UE level measurement (De)Activation [77](#a.3-signalling-based-trace-and-ue-level-measurement-deactivation)

5.16 Framed Routing [77](#framed-routing)

5.17 5G UPF (for 5GC) [78](#g-upf-for-5gc)

5.17.1 Introduction [78](#introduction-2)

5.17.2 Uplink Classifier and Branching Point [78](#uplink-classifier-and-branching-point)

5.17.3 Data forwarding during handovers between 5GS and EPS [78](#data-forwarding-during-handovers-between-5gs-and-eps)

5.18 Enhanced PFCP Association Release [79](#enhanced-pfcp-association-release)

5.18.1 General [79](#general-26)

5.18.2 UP Function Initiated PFCP Session Release [80](#up-function-initiated-pfcp-session-release)

5.19 Activation and Deactivation of Pre-defined PDRs [80](#activation-and-deactivation-of-pre-defined-pdrs)

5.20 Support of Access Traffic Steering, Switching and Splitting (ATSSS) for 5GC [81](#support-of-access-traffic-steering-switching-and-splitting-atsss-for-5gc)

5.20.1 General [81](#general-27)

5.20.2 MPTCP functionality [82](#mptcp-functionality)

5.20.2.1 General [82](#general-28)

5.20.2.2 Activate MPTCP functionality and Exchange MPTCP Parameters [83](#activate-mptcp-functionality-and-exchange-mptcp-parameters)

5.20.2.3 Control of Multipath TCP Connection Establishment by MPTCP Proxy [83](#control-of-multipath-tcp-connection-establishment-by-mptcp-proxy)

5.20.2.4 Traffic Steering and IP Translation by MPTCP Proxy [83](#traffic-steering-and-ip-translation-by-mptcp-proxy)

5.20.2A MPQUIC functionality [84](#a-mpquic-functionality)

5.20.2A.1 General [84](#a.1-general-2)

5.20.2A.2 Activate MPQUIC functionality and Exchange MPQUIC Parameters [84](#a.2-activate-mpquic-functionality-and-exchange-mpquic-parameters)

5.20.2A.3 Control of Multipath QUIC Connection Establishment by MPQUIC Proxy [84](#a.3-control-of-multipath-quic-connection-establishment-by-mpquic-proxy)

5.20.2A.4 Traffic Steering and IP Translation by MPQUIC Proxy [85](#a.4-traffic-steering-and-ip-translation-by-mpquic-proxy)

5.20.3 ATSSS-LL functionality [85](#atsss-ll-functionality)

5.20.3.1 Activate ATSSS-LL functionality and Exchange ATSSS-LL Parameters [85](#activate-atsss-ll-functionality-and-exchange-atsss-ll-parameters)

5.20.4 Handling of GBR traffic of a MA PDU session [86](#handling-of-gbr-traffic-of-a-ma-pdu-session)

5.20.4.1 General [86](#general-29)

5.20.4.2 Access Availability Reporting [86](#access-availability-reporting)

5.20.5 Access type of an MA PDU session becoming (un)available [86](#access-type-of-an-ma-pdu-session-becoming-unavailable)

5.20.6 PMFP message handling in UPF [87](#pmfp-message-handling-in-upf)

5.21 UE IP address/prefix Allocation and Release [87](#ue-ip-addressprefix-allocation-and-release)

5.21.1 General [87](#general-30)

5.21.2 UE IP address/prefix allocation in the CP function [88](#ue-ip-addressprefix-allocation-in-the-cp-function)

5.21.2.1 General [88](#general-31)

5.21.2.2 UE IP Address/prefix allocation using DHCP or AAA server [88](#ue-ip-addressprefix-allocation-using-dhcp-or-aaa-server)

5.21.3 UE IP address/prefix allocation in the UP function [89](#ue-ip-addressprefix-allocation-in-the-up-function)

5.21.3.1 General [89](#general-32)

5.21.3.2 Reporting UE IP Address Usage to the CP function [89](#reporting-ue-ip-address-usage-to-the-cp-function)

5.22 PFCP sessions successively controlled by different SMFs of an SMF set (for 5GC) [90](#pfcp-sessions-successively-controlled-by-different-smfs-of-an-smf-set-for-5gc)

5.22.1 General [90](#general-33)

5.22.2 With one PFCP association per SMF Set and UPF [90](#with-one-pfcp-association-per-smf-set-and-upf)

5.22.3 With one PFCP association per SMF and UPF [92](#with-one-pfcp-association-per-smf-and-upf)

5.22.4 Restoration of PFCP Sessions associated with an FQ-CSID, Group ID or PGW-C/SMF IP Address [93](#restoration-of-pfcp-sessions-associated-with-an-fq-csid-group-id-or-pgw-csmf-ip-address)

5.23 5G VN Group Communication (for 5GC) [94](#_Toc199175279)

5.23.1 General [94](#general-34)

5.23.2 5G VN group communication without N6-based forwarding [95](#g-vn-group-communication-without-n6-based-forwarding)

5.24 Support of Ultra Reliable Low Latency Communication for 5GC [95](#support-of-ultra-reliable-low-latency-communication-for-5gc)

5.24.1 General [95](#general-35)

5.24.2 Redundant Transmission on N3/N9 interfaces [96](#redundant-transmission-on-n3n9-interfaces)

5.24.2.1 General [96](#general-36)

5.24.2.2 GTP-U tunnel setup for redundant transmission [96](#gtp-u-tunnel-setup-for-redundant-transmission)

5.24.2.3 Duplicating downlink packets for redundant transmission [97](#duplicating-downlink-packets-for-redundant-transmission)

5.24.2.4 Eliminating duplicated uplink packets [97](#eliminating-duplicated-uplink-packets)

5.24.3 Redundant Transmission at transport layer [97](#redundant-transmission-at-transport-layer)

5.24.4 Per QoS Flow Per UE QoS Monitoring [97](#per-qos-flow-per-ue-qos-monitoring)

5.24.4.1 General [97](#general-37)

5.24.4.2 QoS Monitoring Control [98](#qos-monitoring-control)

5.24.4.3 QoS Monitoring Reporting [98](#qos-monitoring-reporting)

5.24.5 Per GTP-U Path QoS Monitoring [99](#per-gtp-u-path-qos-monitoring)

5.24.5.1 General [99](#general-38)

5.24.5.2 GTP-U path monitoring [99](#gtp-u-path-monitoring)

5.24.5.3 QoS monitoring of a PDU session based on GTP-U path monitoring [100](#qos-monitoring-of-a-pdu-session-based-on-gtp-u-path-monitoring)

5.24.5.4 QoS Monitoring Reporting [100](#qos-monitoring-reporting-1)

5.25 Support of IPTV (for 5GC) [100](#support-of-iptv-for-5gc)

5.26 Support of Time Sensitive Communication, Time Synchronization, 5GS integration with TSN and Deterministic Networking (for 5GC) [101](#support-of-time-sensitive-communication-time-synchronization-5gs-integration-with-tsn-and-deterministic-networking-for-5gc)

5.26.1 General [101](#general-39)

5.26.2 5GS User Plane Node management [102](#gs-user-plane-node-management)

5.26.3 Transfer of 5GS user plane node and port management information [103](#transfer-of-5gs-user-plane-node-and-port-management-information)

5.26.3.1 General [103](#general-40)

5.26.3.2 Direct Reporting of TSC management information event to TSN AF or TSCTSF [103](#direct-reporting-of-tsc-management-information-event-to-tsn-af-or-tsctsf)

5.26.4 Reporting clock drift between External and 5GS times from UPF to SMF [104](#reporting-clock-drift-between-external-and-5gs-times-from-upf-to-smf)

5.26A Support of TSN enabled Transport Network [104](#a-support-of-tsn-enabled-transport-network)

5.26A.1 General [104](#a.1-general-3)

5.27 Inter-PLMN User Plane Security [105](#inter-plmn-user-plane-security)

5.28 Downlink data delivery status with UPF buffering (for 5GC) [105](#downlink-data-delivery-status-with-upf-buffering-for-5gc)

5.28.1 General [105](#general-41)

5.29 Support Reliable Data Service [106](#support-reliable-data-service)

5.30 Notifying Start Pause of Charging [106](#notifying-start-pause-of-charging)

5.31 Support of L2TP [107](#support-of-l2tp)

5.31.1 General [107](#general-42)

5.31.2 L2TP Tunnel and L2TP Session Setup [108](#l2tp-tunnel-and-l2tp-session-setup)

5.31.3 L2TP Session and L2TP Tunnel Release [109](#l2tp-session-and-l2tp-tunnel-release)

5.32 Support of Uplink packets buffering [109](#support-of-uplink-packets-buffering)

5.32.1 General [109](#general-43)

5.32.2 Uplink packets buffering for on-line charging [109](#uplink-packets-buffering-for-on-line-charging)

5.32.3 Uplink packets buffering during EAS relocation [109](#uplink-packets-buffering-during-eas-relocation)

5.33 Support of enhancement of Edge Computing (for 5GC) [110](#support-of-enhancement-of-edge-computing-for-5gc)

5.33.1 General [110](#general-44)

5.33.2 Uplink packet buffering for low packet loss during EAS relocation [110](#uplink-packet-buffering-for-low-packet-loss-during-eas-relocation)

5.33.3 Edge Relocation using EAS IP address and Port number Replacement [110](#edge-relocation-using-eas-ip-address-and-port-number-replacement)

5.33.4 EAS Discovery procedure with Local DNS Server/Resolver [110](#eas-discovery-procedure-with-local-dns-serverresolver)

5.33.5 Direct Reporting of QoS monitoring events to Local NEF or AF [111](#direct-reporting-of-qos-monitoring-events-to-local-nef-or-af)

5.33.6 EAS Discovery procedure with V-EASDF [111](#eas-discovery-procedure-with-v-easdf)

5.33.7 DNS traffic routing for different UEs with same private UE IP address [111](#dns-traffic-routing-for-different-ues-with-same-private-ue-ip-address)

5.34 Support of 5G Multicast and Broadcast Service [112](#support-of-5g-multicast-and-broadcast-service)

5.34.1 General [112](#general-45)

5.34.2 N4mb requirements [112](#n4mb-requirements)

5.34.2.1 General [112](#general-46)

5.34.2.1A PFCP protocol extensions for N4mb [112](#a-pfcp-protocol-extensions-for-n4mb)

5.34.2.2 Instructing the MB-UPF to forward MBS data using multicast and/or unicast transport [113](#instructing-the-mb-upf-to-forward-mbs-data-using-multicast-andor-unicast-transport)

5.34.2.3 Detecting and reporting user plane (in)activity of an MBS session [115](#detecting-and-reporting-user-plane-inactivity-of-an-mbs-session)

5.34.2.4 Activation and Deactivation of a Multicast MBS session [115](#activation-and-deactivation-of-a-multicast-mbs-session)

5.34.2.5 MBS data usage reporting for MBS charging [115](#mbs-data-usage-reporting-for-mbs-charging)

5.34.3 N4 requirements [116](#n4-requirements)

5.34.3.1 General [116](#general-47)

5.34.3.2 Instructing the UPF to forward (or stop forwarding) multicast MBS data to associated PDU sessions [116](#instructing-the-upf-to-forward-or-stop-forwarding-multicast-mbs-data-to-associated-pdu-sessions)

5.34.3.3 Instructing a combined UPF/MBS-UPF to forward multicast MBS data to associated PDU sessions [119](#instructing-a-combined-upfmbs-upf-to-forward-multicast-mbs-data-to-associated-pdu-sessions)

5.34.3.4 MBS data usage reporting for MBS charging [119](#mbs-data-usage-reporting-for-mbs-charging-1)

5.35 Support of Per Slice UP Resource Allocation and Usage Reporting by the UP Function [120](#support-of-per-slice-up-resource-allocation-and-usage-reporting-by-the-up-function)

5.35.1 General [120](#general-48)

5.36 Paging Policy Indicator Provisioning [120](#paging-policy-indicator-provisioning)

5.36.1 General [120](#general-49)

5.36.2 Enhanced Paging Policy Indicator Provisioning [121](#enhanced-paging-policy-indicator-provisioning)

5.37 Traffic Parameters Measurement per QoS flow [121](#traffic-parameters-measurement-per-qos-flow)

5.37.1 General [121](#general-50)

5.37.2 Traffic Parameter Measurement Control [121](#traffic-parameter-measurement-control)

5.37.3 Traffic Parameter Measurement Report [122](#traffic-parameter-measurement-report)

5.38 Support for high data rate low latency services, (eXtended Reality) XR and interactive media services [122](#support-for-high-data-rate-low-latency-services-extended-reality-xr-and-interactive-media-services)

5.38.0 General [122](#general-51)

5.38.1 Support of ECN marking for L4S [122](#support-of-ecn-marking-for-l4s)

5.38.2 Support of Network Exposure of 5GS information [123](#support-of-network-exposure-of-5gs-information)

5.38.3 Support of PDU Set based QoS Handling [123](#support-of-pdu-set-based-qos-handling)

5.38.4 N6 Jitter Measurement and End of Data Burst Marking [125](#n6-jitter-measurement-and-end-of-data-burst-marking)

5.38.4.1 General [125](#general-52)

5.38.4.2 N6 Jitter and UL/DL Periodicity Measurement Control [125](#n6-jitter-and-uldl-periodicity-measurement-control)

5.38.4.3 N6 Jitter and UL/DL Periodicity Measurement Report [125](#n6-jitter-and-uldl-periodicity-measurement-report)

5.38.4.4 End of Data Burst Marking [125](#end-of-data-burst-marking)

5.39 QoS flow related QoS monitoring and reporting [126](#qos-flow-related-qos-monitoring-and-reporting)

5.39.1 General [126](#general-53)

5.39.2 QoS Monitoring Control [126](#qos-monitoring-control-1)

5.39.3 Measurable QoS parameters and specific requirements for their measurement [127](#measurable-qos-parameters-and-specific-requirements-for-their-measurement)

5.39.3.1 General [127](#general-54)

5.39.3.2 Packet delay monitoring [128](#packet-delay-monitoring)

5.39.3.3 Congestion information monitoring [128](#congestion-information-monitoring)

5.39.3.4 Data rate monitoring [128](#data-rate-monitoring)

5.39.4 QoS Monitoring Reporting [129](#qos-monitoring-reporting-2)

5.40 Support of UPF event subscription via Service Based Interface (for 5GC) [129](#support-of-upf-event-subscription-via-service-based-interface-for-5gc)

6 Procedures [130](#procedures)

6.1 Introduction [130](#introduction-3)

6.2 PFCP Node Related Procedures [130](#pfcp-node-related-procedures)

6.2.1 General [130](#general-55)

6.2.2 Heartbeat Procedure [130](#heartbeat-procedure)

6.2.2.1 General [130](#general-56)

6.2.2.2 Heartbeat Request [130](#heartbeat-request)

6.2.2.3 Heartbeat Response [130](#heartbeat-response)

6.2.3 Load Control Procedure [130](#load-control-procedure)

6.2.3.1 General [130](#general-57)

6.2.3.2 Principles [131](#principles)

6.2.3.3 Load Control Information [131](#load-control-information)

6.2.3.3.1 General Description [131](#general-description-1)

6.2.3.3.2 Parameters [132](#parameters)

6.2.3.3.3 Frequency of Inclusion [132](#frequency-of-inclusion)

6.2.4 Overload Control Procedure [133](#overload-control-procedure)

6.2.4.1 General [133](#general-58)

6.2.4.2 Principles [133](#principles-1)

6.2.4.3 Overload Control Information [134](#overload-control-information)

6.2.4.3.1 General Description [134](#general-description-2)

6.2.4.3.2 Parameters [134](#parameters-1)

6.2.4.3.3 Frequency of Inclusion [136](#frequency-of-inclusion-1)

6.2.4.4 Message Throttling [136](#message-throttling)

6.2.4.4.1 General [136](#general-59)

6.2.4.4.2 Throttling algorithm – "Loss" [137](#throttling-algorithm-loss)

6.2.4.5 Message Prioritization [137](#message-prioritization)

6.2.4.5.1 Description [137](#description-1)

6.2.4.5.2 Based on the Message Priority Signalled in the PFCP Message [138](#based-on-the-message-priority-signalled-in-the-pfcp-message)

6.2.5 PFCP PFD Management Procedure [138](#pfcp-pfd-management-procedure)

6.2.5.1 General [138](#general-60)

6.2.5.2 CP Function Behaviour [138](#cp-function-behaviour)

6.2.5.3 UP Function Behaviour [138](#up-function-behaviour)

6.2.6 PFCP Association Setup Procedure [139](#pfcp-association-setup-procedure)

6.2.6.1 General [139](#general-61)

6.2.6.2 PFCP Association Setup Initiated by the CP Function [139](#pfcp-association-setup-initiated-by-the-cp-function)

6.2.6.2.1 CP Function Behaviour [139](#cp-function-behaviour-1)

6.2.6.2.2 UP Function behaviour [140](#up-function-behaviour-1)

6.2.6.3 PFCP Association Setup Initiated by the UP Function [140](#pfcp-association-setup-initiated-by-the-up-function)

6.2.6.3.1 UP Function Behaviour [140](#up-function-behaviour-2)

6.2.6.3.2 CP Function Behaviour [141](#cp-function-behaviour-2)

6.2.7 PFCP Association Update Procedure [141](#pfcp-association-update-procedure)

6.2.7.1 General [141](#general-62)

6.2.7.2 PFCP Association Update Procedure Initiated by the CP Function [141](#pfcp-association-update-procedure-initiated-by-the-cp-function)

6.2.7.2.1 CP Function Behaviour [141](#cp-function-behaviour-3)

6.2.7.2.2 UP Function Behaviour [141](#up-function-behaviour-3)

6.2.7.3 PFCP Association Update Procedure Initiated by UP Function [142](#pfcp-association-update-procedure-initiated-by-up-function)

6.2.7.3.1 UP Function Behaviour [142](#up-function-behaviour-4)

6.2.7.3.2 CP Function Behaviour [142](#cp-function-behaviour-4)

6.2.8 PFCP Association Release Procedure [143](#pfcp-association-release-procedure)

6.2.8.1 General [143](#general-63)

6.2.8.2 CP Function Behaviour [143](#cp-function-behaviour-5)

6.2.8.3 UP Function behaviour [143](#up-function-behaviour-5)

6.2.9 PFCP Node Report Procedure [143](#pfcp-node-report-procedure)

6.2.9.1 General [143](#general-64)

6.2.9.2 UP Function Behaviour [143](#up-function-behaviour-6)

6.2.9.3 CP Function behaviour [144](#cp-function-behaviour-6)

6.3 PFCP Session Related Procedures [144](#pfcp-session-related-procedures)

6.3.1 General [144](#general-65)

6.3.2 PFCP Session Establishment Procedure [144](#pfcp-session-establishment-procedure)

6.3.2.1 General [144](#general-66)

6.3.2.2 CP Function Behaviour [144](#cp-function-behaviour-7)

6.3.2.3 UP Function Behaviour [144](#up-function-behaviour-7)

6.3.3 PFCP Session Modification Procedure [145](#pfcp-session-modification-procedure)

6.3.3.1 General [145](#general-67)

6.3.3.2 CP Function behaviour [145](#cp-function-behaviour-8)

6.3.3.3 UP Function Behaviour [145](#up-function-behaviour-8)

6.3.4 PFCP Session Deletion Procedure [146](#pfcp-session-deletion-procedure)

6.3.4.1 General [146](#general-68)

6.3.4.2 CP Function Behaviour [146](#cp-function-behaviour-9)

6.3.4.3 UP Function Behaviour [146](#up-function-behaviour-9)

6.3.5 PFCP Session Report Procedure [146](#pfcp-session-report-procedure)

6.3.5.1 General [146](#general-69)

6.3.5.2 UP Function Behaviour [146](#up-function-behaviour-10)

6.3.5.3 CP Function Behaviour [146](#cp-function-behaviour-10)

6.4 Reliable Delivery of PFCP Messages [147](#reliable-delivery-of-pfcp-messages)

6.5 PFCP messages bundling [147](#pfcp-messages-bundling)

7 Messages and Message Formats [148](#messages-and-message-formats)

7.1 Transmission Order and Bit Definitions [148](#transmission-order-and-bit-definitions)

7.2 Message Format [148](#message-format)

7.2.1 General [148](#general-70)

7.2.1A PFCP messages bundled in one UDP/IP packet [148](#a-pfcp-messages-bundled-in-one-udpip-packet)

7.2.2 Message Header [149](#message-header)

7.2.2.1 General Format [149](#general-format)

7.2.2.2 PFCP Header for Node Related Messages [149](#pfcp-header-for-node-related-messages)

7.2.2.3 PFCP Header for Session Related Messages [150](#pfcp-header-for-session-related-messages)

7.2.2.4 Usage of the PFCP Header [150](#usage-of-the-pfcp-header)

7.2.2.4.1 General [150](#general-71)

7.2.2.4.2 Conditions for Sending SEID=0 in PFCP Header [151](#conditions-for-sending-seid0-in-pfcp-header)

7.2.3 Information Elements [151](#information-elements)

7.2.3.1 General [151](#general-72)

7.2.3.2 Presence Requirements of Information Elements [151](#presence-requirements-of-information-elements)

7.2.3.3 Grouped Information Elements [153](#grouped-information-elements)

7.2.3.4 Information Element Type [153](#information-element-type)

7.3 Message Types [153](#message-types)

7.4 PFCP Node Related Messages [154](#pfcp-node-related-messages)

7.4.1 General [154](#general-73)

7.4.2 Heartbeat Messages [154](#heartbeat-messages)

7.4.2.1 Heartbeat Request [154](#heartbeat-request-1)

7.4.2.2 Heartbeat Response [155](#heartbeat-response-1)

7.4.3 PFCP PFD Management [155](#pfcp-pfd-management)

7.4.3.1 PFCP PFD Management Request [155](#pfcp-pfd-management-request)

7.4.3.2 PFCP PFD Management Response [156](#pfcp-pfd-management-response)

7.4.4 PFCP Association messages [157](#pfcp-association-messages)

7.4.4.1 PFCP Association Setup Request [157](#pfcp-association-setup-request)

7.4.4.1.1 General [157](#general-74)

7.4.4.1.2 Clock Drift Control Information IE within PFCP Association Setup Request [159](#clock-drift-control-information-ie-within-pfcp-association-setup-request)

7.4.4.1.3 GTP-U Path QoS Control Information IE within PFCP Association Setup Request [160](#gtp-u-path-qos-control-information-ie-within-pfcp-association-setup-request)

7.4.4.2 PFCP Association Setup Response [162](#pfcp-association-setup-response)

7.4.4.3 PFCP Association Update Request [165](#pfcp-association-update-request)

7.4.4.3.1 UE IP Address Usage Information IE within PFCP Association Update Request [167](#ue-ip-address-usage-information-ie-within-pfcp-association-update-request)

7.4.4.4 PFCP Association Update Response [169](#pfcp-association-update-response)

7.4.4.5 PFCP Association Release Request [169](#pfcp-association-release-request)

7.4.4.6 PFCP Association Release Response [169](#pfcp-association-release-response)

7.4.4.7 PFCP Version Not Supported Response [169](#pfcp-version-not-supported-response)

7.4.5 PFCP Node Report Procedure [170](#pfcp-node-report-procedure-1)

7.4.5.1 PFCP Node Report Request [170](#pfcp-node-report-request)

7.4.5.1.1 General [170](#general-75)

7.4.5.1.2 User Plane Path Failure Report IE within PFCP Node Report Request [170](#user-plane-path-failure-report-ie-within-pfcp-node-report-request)

7.4.5.1.3 User Plane Path Recovery Report IE within PFCP Node Report Request [171](#user-plane-path-recovery-report-ie-within-pfcp-node-report-request)

7.4.5.1.4 Clock Drift Report IE within PFCP Node Report Request [171](#clock-drift-report-ie-within-pfcp-node-report-request)

7.4.5.1.5 GTP-U Path QoS Report IE within PFCP Node Report Request [171](#gtp-u-path-qos-report-ie-within-pfcp-node-report-request)

7.4.5.1.6 QoS Information in GTP-U Path QoS Report IE [172](#qos-information-in-gtp-u-path-qos-report-ie)

7.4.5.1.7 Peer UP Restart Report IE within PFCP Node Report Request [172](#peer-up-restart-report-ie-within-pfcp-node-report-request)

7.4.5.2 PFCP Node Report Response [172](#pfcp-node-report-response)

7.4.5.2.1 General [172](#general-76)

7.4.6 PFCP Session Set Deletion [173](#pfcp-session-set-deletion)

7.4.6.1 PFCP Session Set Deletion Request [173](#pfcp-session-set-deletion-request)

7.4.6.2 PFCP Session Set Deletion Response [173](#pfcp-session-set-deletion-response)

7.4.7 PFCP Session Set Modification [174](#pfcp-session-set-modification)

7.4.7.1 PFCP Session Set Modification Request [174](#pfcp-session-set-modification-request)

7.4.7.2 PFCP Session Set Modification Response [175](#pfcp-session-set-modification-response)

7.5 PFCP Session Related Messages [176](#pfcp-session-related-messages)

7.5.1 General [176](#general-77)

7.5.2 PFCP Session Establishment Request [176](#pfcp-session-establishment-request)

7.5.2.1 General [176](#general-78)

7.5.2.2 Create PDR IE within PFCP Session Establishment Request [183](#create-pdr-ie-within-pfcp-session-establishment-request)

7.5.2.3 Create FAR IE within PFCP Session Establishment Request [192](#create-far-ie-within-pfcp-session-establishment-request)

7.5.2.4 Create URR IE within PFCP Session Establishment Request [198](#create-urr-ie-within-pfcp-session-establishment-request)

7.5.2.5 Create QER IE within PFCP Session Establishment Request [203](#create-qer-ie-within-pfcp-session-establishment-request)

7.5.2.6 Create BAR IE within PFCP Session Establishment Request [207](#create-bar-ie-within-pfcp-session-establishment-request)

7.5.2.7 Create Traffic Endpoint IE within PFCP Session Establishment Request [208](#create-traffic-endpoint-ie-within-pfcp-session-establishment-request)

7.5.2.8 Create MAR IE within PFCP Session Establishment Request [211](#create-mar-ie-within-pfcp-session-establishment-request)

7.5.2.9 Create SRR IE within PFCP Session Establishment Request [213](#create-srr-ie-within-pfcp-session-establishment-request)

7.5.2.10 Provide ATSSS Control Information IE within PFCP Session Establishment Request [217](#provide-atsss-control-information-ie-within-pfcp-session-establishment-request)

7.5.2.11 Provide RDS Configuration Information IE within PFCP Session Establishment Request [218](#provide-rds-configuration-information-ie-within-pfcp-session-establishment-request)

7.5.3 PFCP Session Establishment Response [218](#pfcp-session-establishment-response)

7.5.3.1 General [218](#general-79)

7.5.3.2 Created PDR IE within PFCP Session Establishment Response [221](#created-pdr-ie-within-pfcp-session-establishment-response)

7.5.3.3 Load Control Information IE within PFCP Session Establishment Response [222](#load-control-information-ie-within-pfcp-session-establishment-response)

7.5.3.4 Overload Control Information IE within PFCP Session Establishment Response [222](#overload-control-information-ie-within-pfcp-session-establishment-response)

7.5.3.5 Created Traffic Endpoint IE within PFCP Session Establishment Response [223](#created-traffic-endpoint-ie-within-pfcp-session-establishment-response)

7.5.3.6 Created Bridge/Router Info IE within PFCP Session Establishment Response [223](#created-bridgerouter-info-ie-within-pfcp-session-establishment-response)

7.5.3.7 ATSSS Control Parameters IE within PFCP Session Establishment Response [223](#atsss-control-parameters-ie-within-pfcp-session-establishment-response)

7.5.3.8 Void [225](#void-1)

7.5.4 PFCP Session Modification Request [225](#pfcp-session-modification-request)

7.5.4.1 General [225](#general-80)

7.5.4.2 Update PDR IE within PFCP Session Modification Request [231](#update-pdr-ie-within-pfcp-session-modification-request)

7.5.4.3 Update FAR IE within PFCP Session Modification Request [232](#update-far-ie-within-pfcp-session-modification-request)

7.5.4.4 Update URR IE within PFCP Session Modification Request [235](#update-urr-ie-within-pfcp-session-modification-request)

7.5.4.5 Update QER IE within PFCP Session Modification Request [239](#update-qer-ie-within-pfcp-session-modification-request)

7.5.4.6 Remove PDR IE within PFCP Session Modification Request [242](#remove-pdr-ie-within-pfcp-session-modification-request)

7.5.4.7 Remove FAR IE within PFCP Session Modification Request [243](#remove-far-ie-within-pfcp-session-modification-request)

7.5.4.8 Remove URR IE within PFCP Session Modification Request [243](#remove-urr-ie-within-pfcp-session-modification-request)

7.5.4.9 Remove QER IE PFCP Session Modification Request [243](#remove-qer-ie-pfcp-session-modification-request)

7.5.4.10 Query URR IE within PFCP Session Modification Request [243](#query-urr-ie-within-pfcp-session-modification-request)

7.5.4.11 Update BAR IE within PFCP Session Modification Request [244](#update-bar-ie-within-pfcp-session-modification-request)

7.5.4.12 Remove BAR IE within PFCP Session Modification Request [244](#remove-bar-ie-within-pfcp-session-modification-request)

7.5.4.13 Update Traffic Endpoint IE within PFCP Session Modification Request [245](#update-traffic-endpoint-ie-within-pfcp-session-modification-request)

7.5.4.14 Remove Traffic Endpoint IE within PFCP Session Modification Request [247](#remove-traffic-endpoint-ie-within-pfcp-session-modification-request)

7.5.4.15 Remove MAR IE within PFCP Session Modification Request [247](#remove-mar-ie-within-pfcp-session-modification-request)

7.5.4.16 Update MAR IE within PFCP Session Modification Request [247](#update-mar-ie-within-pfcp-session-modification-request)

7.5.4.17 Create PDR/FAR/URR/QER/BAR/MAR IEs within PFCP Session Modification Request [249](#create-pdrfarurrqerbarmar-ies-within-pfcp-session-modification-request)

7.5.4.18 TSC Management Information IE within PFCP Session Modification Request [249](#tsc-management-information-ie-within-pfcp-session-modification-request)

7.5.4.19 Remove SRR IE within PFCP Session Modification Request [249](#remove-srr-ie-within-pfcp-session-modification-request)

7.5.4.20 Update SRR IE within PFCP Session Modification Request [250](#update-srr-ie-within-pfcp-session-modification-request)

7.5.4.21 Ethernet Context Information within PFCP Session Modification Request [250](#ethernet-context-information-within-pfcp-session-modification-request)

7.5.4.22 Query Packet Rate Status IE within PFCP Session Modification Request [251](#query-packet-rate-status-ie-within-pfcp-session-modification-request)

7.5.5 PFCP Session Modification Response [251](#pfcp-session-modification-response)

7.5.5.1 General [251](#general-81)

7.5.5.2 Usage Report IE within PFCP Session Modification Response [254](#usage-report-ie-within-pfcp-session-modification-response)

7.5.5.3 TSC Management Information IE within PFCP Session Modification Response [255](#tsc-management-information-ie-within-pfcp-session-modification-response)

7.5.5.4 Packet Rate Status Report IE within PFCP Session Modification Response [255](#packet-rate-status-report-ie-within-pfcp-session-modification-response)

7.5.5.5 Updated PDR IE within PFCP Session Modification Response [255](#updated-pdr-ie-within-pfcp-session-modification-response)

7.5.6 PFCP Session Deletion Request [256](#pfcp-session-deletion-request)

7.5.7 PFCP Session Deletion Response [256](#pfcp-session-deletion-response)

7.5.7.1 General [256](#general-82)

7.5.7.2 Usage Report IE within PFCP Session Deletion Response [258](#usage-report-ie-within-pfcp-session-deletion-response)

7.5.8 PFCP Session Report Request [258](#pfcp-session-report-request)

7.5.8.1 General [258](#general-83)

7.5.8.2 Downlink Data Report IE within PFCP Session Report Request [260](#downlink-data-report-ie-within-pfcp-session-report-request)

7.5.8.3 Usage Report IE within PFCP Session Report Request [261](#usage-report-ie-within-pfcp-session-report-request)

7.5.8.4 Error Indication Report IE within PFCP Session Report Request [264](#error-indication-report-ie-within-pfcp-session-report-request)

7.5.8.5 TSC Management Information IE within PFCP Session Report Request [264](#tsc-management-information-ie-within-pfcp-session-report-request)

7.5.8.6 Session Report IE within PFCP Session Report Request [265](#session-report-ie-within-pfcp-session-report-request)

7.5.9 PFCP Session Report Response [266](#pfcp-session-report-response)

7.5.9.1 General [266](#general-84)

7.5.9.2 Update BAR IE within PFCP Session Report Response [268](#update-bar-ie-within-pfcp-session-report-response)

7.6 Error Handling [269](#error-handling)

7.6.1 Protocol Errors [269](#protocol-errors)

7.6.2 Different PFCP Versions [269](#different-pfcp-versions)

7.6.3 PFCP Message of Invalid Length [269](#pfcp-message-of-invalid-length)

7.6.4 Unknown PFCP Message [269](#unknown-pfcp-message)

7.6.5 Unexpected PFCP Message [269](#unexpected-pfcp-message)

7.6.6 Missing Information Elements [270](#missing-information-elements)

7.6.7 Invalid Length Information Element [270](#invalid-length-information-element)

7.6.8 Semantically incorrect Information Element [270](#semantically-incorrect-information-element)

7.6.9 Unknown or unexpected Information Element [271](#unknown-or-unexpected-information-element)

7.6.10 Repeated Information Elements [271](#repeated-information-elements)

8 Information Elements [271](#information-elements-1)

8.1 Information Elements Format [271](#information-elements-format)

8.1.1 Information Element Format [271](#information-element-format)

8.1.2 Information Element Types [272](#information-element-types)

8.2 Information Elements [281](#information-elements-2)

8.2.1 Cause [281](#cause)

8.2.2 Source Interface [283](#source-interface)

8.2.3 F-TEID [284](#f-teid)

8.2.4 Network Instance [285](#network-instance)

8.2.5 SDF Filter [285](#sdf-filter)

8.2.6 Application ID [286](#application-id)

8.2.7 Gate Status [287](#gate-status)

8.2.8 MBR [287](#mbr)

8.2.9 GBR [288](#gbr)

8.2.10 QER Correlation ID [288](#qer-correlation-id)

8.2.11 Precedence [288](#precedence)

8.2.12 Transport Level Marking [289](#transport-level-marking-1)

8.2.13 Volume Threshold [289](#volume-threshold)

8.2.14 Time Threshold [290](#time-threshold)

8.2.15 Monitoring Time [290](#monitoring-time)

8.2.16 Subsequent Volume Threshold [290](#subsequent-volume-threshold)

8.2.17 Subsequent Time Threshold [291](#subsequent-time-threshold)

8.2.18 Inactivity Detection Time [291](#inactivity-detection-time)

8.2.19 Reporting Triggers [291](#reporting-triggers)

8.2.20 Redirect Information [293](#redirect-information)

8.2.21 Report Type [294](#report-type)

8.2.22 Offending IE [294](#offending-ie)

8.2.23 Forwarding Policy [295](#forwarding-policy)

8.2.24 Destination Interface [295](#destination-interface)

8.2.25 UP Function Features [296](#up-function-features)

8.2.26 Apply Action [301](#apply-action)

8.2.27 Downlink Data Service Information [302](#downlink-data-service-information)

8.2.28 Downlink Data Notification Delay [303](#downlink-data-notification-delay)

8.2.29 DL Buffering Duration [303](#dl-buffering-duration)

8.2.30 DL Buffering Suggested Packet Count [304](#dl-buffering-suggested-packet-count)

8.2.31 PFCPSMReq-Flags [304](#pfcpsmreq-flags)

8.2.32 PFCPSRRsp-Flags [305](#pfcpsrrsp-flags)

8.2.33 Sequence Number [305](#sequence-number)

8.2.34 Metric [305](#metric)

8.2.35 Timer [305](#timer)

8.2.36 Packet Detection Rule ID (PDR ID) [306](#packet-detection-rule-id-pdr-id)

8.2.37 F-SEID [306](#f-seid)

8.2.38 Node ID [307](#node-id)

8.2.39 PFD Contents [308](#pfd-contents)

8.2.40 Measurement Method [310](#measurement-method)

8.2.41 Usage Report Trigger [310](#usage-report-trigger)

8.2.42 Measurement Period [311](#measurement-period)

8.2.43 Fully qualified PDN Connection Set Identifier (FQ-CSID) [312](#fully-qualified-pdn-connection-set-identifier-fq-csid)

8.2.44 Volume Measurement [313](#volume-measurement)

8.2.45 Duration Measurement [314](#duration-measurement)

8.2.46 Time of First Packet [314](#time-of-first-packet)

8.2.47 Time of Last Packet [314](#time-of-last-packet)

8.2.48 Quota Holding Time [315](#quota-holding-time)

8.2.49 Dropped DL Traffic Threshold [315](#dropped-dl-traffic-threshold)

8.2.50 Volume Quota [315](#volume-quota)

8.2.51 Time Quota [316](#time-quota)

8.2.52 Start Time [316](#start-time)

8.2.53 End Time [317](#end-time)

8.2.54 URR ID [317](#urr-id)

8.2.55 Linked URR ID IE [317](#linked-urr-id-ie)

8.2.56 Outer Header Creation [318](#outer-header-creation)

8.2.57 BAR ID [319](#bar-id)

8.2.58 CP Function Features [319](#cp-function-features)

8.2.59 Usage Information [320](#usage-information)

8.2.60 Application Instance ID [321](#application-instance-id)

8.2.61 Flow Information [321](#flow-information)

8.2.62 UE IP Address [321](#ue-ip-address)

8.2.63 Packet Rate [322](#packet-rate)

8.2.64 Outer Header Removal [324](#outer-header-removal)

8.2.65 Recovery Time Stamp [326](#recovery-time-stamp)

8.2.66 DL Flow Level Marking [326](#dl-flow-level-marking)

8.2.67 Header Enrichment [326](#header-enrichment)

8.2.68 Measurement Information [327](#measurement-information)

8.2.69 Node Report Type [328](#node-report-type)

8.2.70 Remote GTP-U Peer [329](#remote-gtp-u-peer)

8.2.71 UR-SEQN [329](#ur-seqn)

8.2.72 Activate Predefined Rules [330](#activate-predefined-rules)

8.2.73 Deactivate Predefined Rules [330](#deactivate-predefined-rules)

8.2.74 FAR ID [330](#far-id)

8.2.75 QER ID [331](#qer-id)

8.2.76 OCI Flags [331](#oci-flags)

8.2.77 PFCP Association Release Request [331](#pfcp-association-release-request-1)

8.2.78 Graceful Release Period [332](#graceful-release-period)

8.2.79 PDN Type [332](#pdn-type)

8.2.80 Failed Rule ID [333](#failed-rule-id)

8.2.81 Time Quota Mechanism [333](#time-quota-mechanism)

8.2.82 Void [334](#void-2)

8.2.83 User Plane Inactivity Timer [334](#user-plane-inactivity-timer)

8.2.84 Multiplier [334](#multiplier)

8.2.85 Aggregated URR ID IE [335](#aggregated-urr-id-ie)

8.2.86 Subsequent Volume Quota [335](#subsequent-volume-quota)

8.2.87 Subsequent Time Quota [335](#subsequent-time-quota)

8.2.88 RQI [336](#rqi)

8.2.89 QFI [336](#qfi)

8.2.90 Query URR Reference [336](#query-urr-reference)

8.2.91 Additional Usage Reports Information [337](#additional-usage-reports-information)

8.2.92 Traffic Endpoint ID [337](#traffic-endpoint-id)

8.2.93 MAC address [337](#mac-address)

8.2.94 C-TAG (Customer-VLAN tag) [338](#c-tag-customer-vlan-tag)

8.2.95 S-TAG (Service-VLAN tag) [339](#s-tag-service-vlan-tag)

8.2.96 Ethertype [339](#ethertype)

8.2.97 Proxying [340](#proxying)

8.2.98 Ethernet Filter ID [340](#ethernet-filter-id)

8.2.99 Ethernet Filter Properties [340](#ethernet-filter-properties)

8.2.100 Suggested Buffering Packets Count [341](#suggested-buffering-packets-count)

8.2.101 User ID [341](#user-id)

8.2.102 Ethernet PDU Session Information [342](#ethernet-pdu-session-information)

8.2.103 MAC Addresses Detected [343](#mac-addresses-detected)

8.2.104 MAC Addresses Removed [343](#mac-addresses-removed)

8.2.105 Ethernet Inactivity Timer [344](#ethernet-inactivity-timer)

8.2.106 Subsequent Event Quota [344](#subsequent-event-quota)

8.2.107 Subsequent Event Threshold [344](#subsequent-event-threshold)

8.2.108 Trace Information [345](#trace-information)

8.2.109 Framed-Route [345](#framed-route)

8.2.110 Framed-Routing [345](#framed-routing-1)

8.2.111 Framed-IPv6-Route [346](#framed-ipv6-route)

8.2.112 Event Quota [346](#event-quota)

8.2.113 Event Threshold [346](#event-threshold)

8.2.114 Time Stamp [347](#time-stamp)

8.2.115 Averaging Window [347](#averaging-window)

8.2.116 Paging Policy Indicator (PPI) [347](#paging-policy-indicator-ppi)

8.2.117 APN/DNN [347](#apndnn)

8.2.118 3GPP Interface Type [348](#gpp-interface-type)

8.2.119 PFCPSRReq-Flags [349](#pfcpsrreq-flags)

8.2.120 PFCPAUReq-Flags [350](#pfcpaureq-flags)

8.2.121 Activation Time [350](#activation-time)

8.2.122 Deactivation Time [351](#deactivation-time)

8.2.123 MAR ID [351](#mar-id)

8.2.124 Steering Functionality [351](#steering-functionality)

8.2.125 Steering Mode [352](#steering-mode)

8.2.126 Weight [352](#weight)

8.2.127 Priority [352](#priority)

8.2.128 UE IP address Pool Identity [353](#ue-ip-address-pool-identity)

8.2.129 Alternative SMF IP Address [353](#alternative-smf-ip-address)

8.2.130 Packet Replication and Detection Carry-On Information [354](#packet-replication-and-detection-carry-on-information)

8.2.131 SMF Set ID [354](#smf-set-id)

8.2.132 Quota Validity Time [355](#quota-validity-time)

8.2.133 Number of Reports [355](#number-of-reports)

8.2.134 PFCPASRsp-Flags [355](#pfcpasrsp-flags)

8.2.135 CP PFCP Entity IP Address [356](#cp-pfcp-entity-ip-address)

8.2.136 PFCPSEReq-Flags [356](#pfcpsereq-flags)

8.2.137 IP Multicast Address [356](#ip-multicast-address)

8.2.138 Source IP Address [357](#source-ip-address)

8.2.139 Packet Rate Status [358](#packet-rate-status)

8.2.140 Create Bridge/Router Info IE [359](#create-bridgerouter-info-ie)

8.2.141 Port Number [359](#port-number)

8.2.142 NW-TT Port Number [359](#nw-tt-port-number)

8.2.143 5GS User Plane Node ID [360](#gs-user-plane-node-id)

8.2.144 Port Management Information Container [360](#port-management-information-container)

8.2.145 Requested Clock Drift Information [361](#requested-clock-drift-information)

8.2.146 Time Domain Number [361](#time-domain-number)

8.2.147 Time Offset Threshold [361](#time-offset-threshold)

8.2.148 Cumulative rateRatio Threshold [362](#cumulative-rateratio-threshold)

8.2.149 Time Offset Measurement [362](#time-offset-measurement)

8.2.150 Cumulative rateRatio Measurement [362](#cumulative-rateratio-measurement)

8.2.151 SRR ID [362](#srr-id)

8.2.152 Requested Access Availability Information [363](#requested-access-availability-information)

8.2.153 Access Availability Information [363](#access-availability-information)

8.2.154 MPTCP Control Information [364](#mptcp-control-information)

8.2.155 ATSSS-LL Control Information [364](#atsss-ll-control-information)

8.2.156 PMF Control Information [364](#pmf-control-information)

8.2.157 MPTCP Address Information [365](#mptcp-address-information)

8.2.158 Link-Specific Multipath IP Address [366](#link-specific-multipath-ip-address)

8.2.159 PMF Address Information [366](#pmf-address-information)

8.2.160 ATSSS-LL Information [367](#atsss-ll-information)

8.2.161 Data Network Access Identifier [368](#data-network-access-identifier)

8.2.162 Average Packet Delay [368](#average-packet-delay)

8.2.163 Minimum Packet Delay [368](#minimum-packet-delay)

8.2.164 Maximum Packet Delay [368](#maximum-packet-delay)

8.2.165 QoS Report Trigger [369](#qos-report-trigger)

8.2.166 GTP-U Path Interface Type [369](#gtp-u-path-interface-type)

8.2.167 Requested QoS Monitoring [369](#requested-qos-monitoring)

8.2.168 Reporting Frequency [370](#reporting-frequency)

8.2.169 Packet Delay Thresholds [371](#packet-delay-thresholds)

8.2.170 Minimum Wait Time [371](#minimum-wait-time)

8.2.171 QoS Monitoring Measurement [372](#qos-monitoring-measurement)

8.2.172 MT-EDT Control Information [373](#mt-edt-control-information)

8.2.173 DL Data Packets Size [373](#dl-data-packets-size)

8.2.174 QER Control Indications [373](#qer-control-indications)

8.2.175 NF Instance ID [374](#nf-instance-id)

8.2.176 S-NSSAI [374](#s-nssai)

8.2.177 IP version [374](#ip-version)

8.2.178 PFCPASReq-Flags [374](#pfcpasreq-flags)

8.2.179 Data Status [375](#data-status)

8.2.180 RDS Configuration Information [375](#rds-configuration-information)

8.2.188 LNS Address [376](#lns-address)

8.2.181 Multipath Applicable Indication [376](#multipath-applicable-indication)

8.2.182 User Plane Node Management Information Container [376](#user-plane-node-management-information-container)

8.2.183 Number of UE IP Addresses [377](#number-of-ue-ip-addresses)

8.2.184 Validity Timer [377](#validity-timer)

8.2.185 Offending IE Information [377](#offending-ie-information)

8.2.186 RAT Type [378](#rat-type)

8.2.187 L2TP User Authentication [378](#l2tp-user-authentication)

8.2.189 Tunnel Preference [379](#tunnel-preference)

8.2.190 Calling Number [380](#calling-number)

8.2.191 Called Number [380](#called-number)

8.2.192 L2TP Session Indications [380](#l2tp-session-indications)

8.2.193 DNS Server Address [381](#dns-server-address)

8.2.194 NBNS Server Address [381](#nbns-server-address)

8.2.195 Maximum Receive Unit [381](#maximum-receive-unit)

8.2.196 Thresholds [381](#thresholds)

8.2.197 Steering Mode Indicator [382](#steering-mode-indicator)

8.2.198 Group Id [382](#group-id)

8.2.199 CP IP Address [382](#cp-ip-address)

8.2.200 IP Address and Port Number Replacement [383](#ip-address-and-port-number-replacement)

8.2.201 DNS Query/Response Filter [384](#dns-queryresponse-filter)

8.2.202 Event Notification URI [384](#event-notification-uri)

8.2.203 Notification Correlation ID [384](#notification-correlation-id)

8.2.204 Reporting Flags [385](#reporting-flags)

8.2.205 Predefined Rules Name [385](#predefined-rules-name)

8.2.206 MBS Session Identifier [385](#mbs-session-identifier)

8.2.207 Multicast Transport Information [386](#multicast-transport-information)

8.2.208 MBSN4mbReq-Flags [387](#mbsn4mbreq-flags)

8.2.209 Local Ingress Tunnel [387](#local-ingress-tunnel)

8.2.210 MBS Unicast Parameters ID [388](#mbs-unicast-parameters-id)

8.2.211 MBSN4Resp-Flags [388](#mbsn4resp-flags)

8.2.212 Tunnel Password [389](#tunnel-password)

8.2.213 Area Session ID [389](#area-session-id)

8.2.214 DSCP to PPI Mapping Information [389](#dscp-to-ppi-mapping-information)

8.2.215 PFCPSDRsp-Flags [390](#pfcpsdrsp-flags)

8.2.216 QER Indications [390](#qer-indications)

8.2.217 Vendor-Specific Node Report Type [391](#vendor-specific-node-report-type)

8.2.218 Configured Time Domain [391](#configured-time-domain)

8.2.219 Metadata [391](#metadata)

8.2.223 Traffic Parameter Measurement Indication [393](#traffic-parameter-measurement-indication)

8.2.225 MPQUIC Control Information [394](#mpquic-control-information)

8.2.226 MPQUIC Address Information [394](#mpquic-address-information)

8.2.227 Transport Mode [395](#transport-mode)

8.2.228 Void [395](#_Toc199175809)

8.2.229 Reporting Suggestion Info [395](#reporting-suggestion-info)

8.2.230 TL-Container [396](#tl-container)

8.2.231 Measurement Indication [396](#measurement-indication)

8.2.232 HPLMN S-NSSAI [396](#hplmn-s-nssai)

8.2.233 Media Transport Protocol [397](#media-transport-protocol)

8.2.234 RTP Header Extension Type [397](#rtp-header-extension-type)

8.2.235 RTP Header Extension ID [397](#rtp-header-extension-id)

8.2.236 RTP Payload Type [398](#rtp-payload-type)

8.2.237 RTP Payload Format [398](#rtp-payload-format)

8.2.238 Extended DL Buffering Notification Policy [398](#extended-dl-buffering-notification-policy)

8.2.239 MT-SDT Control Information [399](#mt-sdt-control-information)

8.2.240 Reporting Thresholds [399](#reporting-thresholds)

8.2.241 RTP Header Extension Additional Information [400](#rtp-header-extension-additional-information)

8.2.242 Mapped N6 IP Address [401](#mapped-n6-ip-address)

8.2.243 N6 Routing Information [401](#n6-routing-information)

8.2.244 URI [402](#uri)

8.2.245 UE Level Measurements Configuration [402](#ue-level-measurements-configuration)

8.2.246 - 8.2.271 Used by Rel-19 onwards [403](#used-by-rel-19-onwards)

8.2.272 Reporting Control Information [403](#reporting-control-information)

A.1 Throttling Aalgorithms [404](#a.1-throttling-aalgorithms)

A.1.1 "Loss" Throttling Algorithm [404](#a.1.1-loss-throttling-algorithm)

A.1.1.1 Example of Possible Implementation [404](#a.1.1.1-example-of-possible-implementation)

B.1 CP Selection Function [404](#b.1-cp-selection-function)

B.1.1 General [404](#b.1.1-general)

B.2 UP Selection Function [405](#b.2-up-selection-function)

B.2.1 General [405](#b.2.1-general)

B.2.2 SGW-U Selection Function [405](#b.2.2-sgw-u-selection-function)

B.2.3 PGW-U Selection Function [405](#b.2.3-pgw-u-selection-function)

B.2.4 Combined SGW-U/PGW-U Selection Function [406](#b.2.4-combined-sgw-upgw-u-selection-function)

B.2.5 TDF-U selection function [406](#b.2.5-tdf-u-selection-function)

B.2.6 UP Selection Function Based on DNS [407](#b.2.6-up-selection-function-based-on-dns)

B.2.6.1 General [407](#b.2.6.1-general)

B.2.6.2 SGW-U Selection Function Based on DNS [407](#b.2.6.2-sgw-u-selection-function-based-on-dns)

B.2.6.3 PGW-U Selection Function Based on DNS [407](#b.2.6.3-pgw-u-selection-function-based-on-dns)

B.2.6.4 Combined SGW-U/PGW-U Selection Function Based on DNS [407](#b.2.6.4-combined-sgw-upgw-u-selection-function-based-on-dns)

C.1 General [407](#c.1-general)

C.2 Charging Support [408](#c.2-charging-support)

C.2.1 Online Charging [408](#c.2.1-online-charging)

C.2.1.1 Online Charging Call Flow – Normal Scenario [408](#c.2.1.1-online-charging-call-flow-normal-scenario)

C.2.1.2 Online Charging Call Flow with Credit Pooling [410](#c.2.1.2-online-charging-call-flow-with-credit-pooling)

C.2.1.2.1 General [410](#c.2.1.2.1-general)

C.2.1.2.2 Example Call Flow 1 [410](#c.2.1.2.2-example-call-flow-1)

C.2.1.2.3 Example Call Flow 2 [412](#c.2.1.2.3-example-call-flow-2)

D.1 General [414](#d.1-general)

D.2 Procedures [415](#d.2-procedures)

D.2.1 Addition of PSA and UL CL/BP controlled by I-SMF [415](#d.2.1-addition-of-psa-and-ul-clbp-controlled-by-i-smf)

D.2.2 Removal of PSA and UL CL/BP [419](#d.2.2-removal-of-psa-and-ul-clbp)

D.2.3 Change of PSA [419](#d.2.3-change-of-psa)

D.2.4 Traffic Usage Reporting [419](#d.2.4-traffic-usage-reporting)

D.2.5 Updating N4 information towards I-SMF [419](#d.2.5-updating-n4-information-towards-i-smf)

D.2.6 PDU session release [419](#d.2.6-pdu-session-release)

D.2.7 Simultaneous change of UL CL/BP and PSA controlled by I-SMF [420](#d.2.7-simultaneous-change-of-ul-clbp-and-psa-controlled-by-i-smf)

D.2.8 Simultaneous change of UL CL/BP and PSA controlled by different I-SMFs [423](#d.2.8-simultaneous-change-of-ul-clbp-and-psa-controlled-by-different-i-smfs)

E.1 General [424](#e.1-general)

E.2 Multipath TCP Connection Setup [425](#e.2-multipath-tcp-connection-setup)

E.2.1 General [425](#e.2.1-general)

E.2.2 Outgoing Multipath TCP Connection Setup [425](#e.2.2-outgoing-multipath-tcp-connection-setup)

E.2.3 Incoming Multipath TCP Connection Setup [425](#e.2.3-incoming-multipath-tcp-connection-setup)

E.2.4 MPTCP Session Entry Stored in MPTCP Proxy [425](#e.2.4-mptcp-session-entry-stored-in-mptcp-proxy)

E.3 IP Translation Procedure [426](#e.3-ip-translation-procedure)

E.3.1 General [426](#e.3.1-general)

E.3.2 IP Translation on Uplink IP Packets [426](#e.3.2-ip-translation-on-uplink-ip-packets)

E.3.3 IP Translation on Downlink IP Packets [427](#e.3.3-ip-translation-on-downlink-ip-packets)

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
