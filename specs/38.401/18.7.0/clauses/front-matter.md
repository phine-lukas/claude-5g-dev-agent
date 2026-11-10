3GPP TS 38.401 V18.7.0 (2025-09)

Technical Specification

3rd Generation Partnership Project;

Technical Specification Group Radio Access Network;

NG-RAN;

Architecture description

(Release 18)

[figure] [figure]

The present document has been developed within the 3<sup>rd</sup> Generation Partnership Project (3GPP <sup>TM</sup>) and may be further elaborated for the purposes of 3GPP.  
The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented.  
This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification.  
Specifications and reports for implementation of the 3GPP <sup>TM</sup> system should be obtained via the 3GPP Organizational Partners' Publications Offices.

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
> <http://www.3gpp.org>

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

Foreword [7](#foreword)

1 Scope [8](#scope)

2 References [8](#references)

3 Definitions and abbreviations [9](#definitions-and-abbreviations)

3.1 Definitions [9](#definitions)

3.2 Abbreviations [11](#abbreviations)

4 General principles [13](#general-principles)

5 General architecture [13](#general-architecture)

5.1 General [13](#general)

5.2 User plane [13](#user-plane)

5.3 Control plane [14](#control-plane)

6 NG-RAN architecture [15](#ng-ran-architecture)

6.1 Overview [15](#overview)

6.1.1 Overall Architecture of NG-RAN [15](#overall-architecture-of-ng-ran)

6.1.2 Overall architecture for separation of gNB-CU-CP and gNB-CU-UP [16](#overall-architecture-for-separation-of-gnb-cu-cp-and-gnb-cu-up)

6.1.3 Overall Architecture of IAB [17](#overall-architecture-of-iab)

6.1.4 Protocol stacks of IAB [18](#protocol-stacks-of-iab)

6.1.5 Overall Architecture of NR MBS [20](#overall-architecture-of-nr-mbs)

6.1.6 Protocol stacks of L2 UE-to-Network Relay [20](#protocol-stacks-of-l2-ue-to-network-relay)

6.2 NG-RAN identifiers [21](#ng-ran-identifiers)

6.2.1 Principle of handling Application Protocol Identities [21](#principle-of-handling-application-protocol-identities)

6.2.2 gNB-DU ID [24](#gnb-du-id)

6.2.3 ng-eNB-DU ID [24](#ng-enb-du-id)

6.2.4 gNB-CU-UP ID [24](#gnb-cu-up-id)

6.2.5 RAN UE ID [24](#ran-ue-id)

6.3 Transport addresses [24](#transport-addresses)

6.4 UE associations in NG-RAN Node [24](#ue-associations-in-ng-ran-node)

6.5 MBS Session associations in NG-RAN Node [25](#mbs-session-associations-in-ng-ran-node)

7 NG-RAN functions description [27](#ng-ran-functions-description)

7.0 General [27](#general-1)

7.1 NG-RAN sharing [27](#ng-ran-sharing)

7.2 Remote Interference Management [27](#remote-interference-management)

7.3 Cross-Link Interference Management [27](#cross-link-interference-management)

7.4 Support for Non-Public Networks [27](#support-for-non-public-networks)

7.5 RACH Optimisation Function [27](#rach-optimisation-function)

7.6 Positioning [28](#positioning)

7.7 Support for NR MBS [28](#support-for-nr-mbs)

7.7.1 Support of dynamic PTP and PTM switching [28](#support-of-dynamic-ptp-and-ptm-switching)

7.7.2 Support of resource efficiency for RAN Sharing [28](#support-of-resource-efficiency-for-ran-sharing)

7.7.2.1 General [28](#general-2)

7.7.2.2 Support of resource efficiency for MOCN [28](#support-of-resource-efficiency-for-mocn)

7.7.2.3 Support of resource efficiency for RAN Sharing with multiple cell-ID broadcast [28](#support-of-resource-efficiency-for-ran-sharing-with-multiple-cell-id-broadcast)

7.7.3 Support of Multicast reception for UEs in RRC_INACTIVE [29](#support-of-multicast-reception-for-ues-in-rrc_inactive)

7.7.4 Recovery of shared F1-U Failure [29](#recovery-of-shared-f1-u-failure)

7.8 PCI Optimisation Function [29](#pci-optimisation-function)

7.9 Support for CCO [30](#support-for-cco)

7.9.1 General [30](#general-3)

7.9.2 OAM requirements [30](#oam-requirements)

7.9.3 Dynamic coverage configuration changes [30](#_Toc209704744)

7.10 Support of RAN visible QoE measurement [30](#support-of-ran-visible-qoe-measurement)

7.11 Support of AI/ML for NG-RAN [30](#support-of-aiml-for-ng-ran)

8 Overall procedures in gNB-CU/gNB-DU Architecture [30](#overall-procedures-in-gnb-cugnb-du-architecture)

8.1 UE Initial Access [30](#ue-initial-access)

8.2 Intra-gNB-CU Mobility [32](#intra-gnb-cu-mobility)

8.2.1 Intra-NR Mobility [32](#intra-nr-mobility)

8.2.1.1 Inter-gNB-DU Mobility [32](#inter-gnb-du-mobility)

8.2.1.2 Intra-gNB-DU handover [33](#intra-gnb-du-handover)

8.2.1.3 Inter-gNB-DU Conditional Handover or Conditional PSCell Change or subsequent CPAC [34](#inter-gnb-du-conditional-handover-or-conditional-pscell-change-or-subsequent-cpac)

8.2.1.4 Intra-gNB-DU LTM [35](#intra-gnb-du-ltm)

8.2.1.5 Inter-gNB-DU LTM [38](#inter-gnb-du-ltm)

8.2.1.6 LTM with gNB-CU-UP change [41](#ltm-with-gnb-cu-up-change)

8.2.2 EN-DC Mobility [43](#en-dc-mobility)

8.2.2.1 Inter-gNB-DU Mobility using MCG SRB [43](#inter-gnb-du-mobility-using-mcg-srb)

8.2.2.2 Inter-gNB-DU Mobility using SCG SRB (SRB3) [45](#inter-gnb-du-mobility-using-scg-srb-srb3)

8.2.2.3 Inter-gNB-DU Conditional PSCell Change using MCG SRB without MN negotiation [45](#inter-gnb-du-conditional-pscell-change-using-mcg-srb-without-mn-negotiation)

8.2.3 Intra-CU topology adaptation procedure [47](#intra-cu-topology-adaptation-procedure)

8.2.3.1 Intra-CU topology adaptation procedure in SA [47](#intra-cu-topology-adaptation-procedure-in-sa)

8.2.3.2 Intra-CU topology adaptation procedure in NSA using MCG SRB [50](#intra-cu-topology-adaptation-procedure-in-nsa-using-mcg-srb)

8.2.3.3 Intra-CU topology adaptation procedure in NSA using SCG SRB (SRB3) [52](#intra-cu-topology-adaptation-procedure-in-nsa-using-scg-srb-srb3)

8.2.4 Intra-CU topological redundancy procedure [52](#intra-cu-topological-redundancy-procedure)

8.2.5 Intra-CU Backhaul RLF recovery for IAB-nodes in SA mode [55](#intra-cu-backhaul-rlf-recovery-for-iab-nodes-in-sa-mode)

8.3 Mechanism of centralized retransmission of lost PDUs [56](#mechanism-of-centralized-retransmission-of-lost-pdus)

8.3.1 Centralized Retransmission in Intra gNB-CU Cases [56](#centralized-retransmission-in-intra-gnb-cu-cases)

8.4 Multi-Connectivity operation [57](#multi-connectivity-operation)

8.4.1 Secondary Node Addition [57](#secondary-node-addition)

8.4.1.1 EN-DC [57](#en-dc)

8.4.2 Secondary Node Release (MN/SN initiated) [58](#secondary-node-release-mnsn-initiated)

8.4.2.1 EN-DC [58](#en-dc-1)

8.4.3 SCG suspend/resume in RRC_INACTIVE [59](#scg-suspendresume-in-rrc_inactive)

8.4.4 SCG Deactivation and Activation [60](#scg-deactivation-and-activation)

8.4.4.1 SN Addition with SCG Activation or Deactivation [60](#_Toc209704776)

8.4.4.2 MN initiated SN Modification with SCG Activation or Deactivation [61](#mn-initiated-sn-modification-with-scg-activation-or-deactivation)

8.4.4.3 SN initiated SN Modification with SCG Activation or Deactivation [62](#sn-initiated-sn-modification-with-scg-activation-or-deactivation)

8.5 F1 Startup and cells activation [62](#f1-startup-and-cells-activation)

8.6 RRC state transition [64](#rrc-state-transition)

8.6.1 RRC connected to RRC inactive [64](#rrc-connected-to-rrc-inactive)

8.6.2 RRC inactive to other states [64](#rrc-inactive-to-other-states)

8.7 RRC connection reestablishment [66](#rrc-connection-reestablishment)

8.8 Multiple TNLAs for F1-C [68](#multiple-tnlas-for-f1-c)

8.9 Overall procedures involving E1 and F1 [69](#overall-procedures-involving-e1-and-f1)

8.9.1 UE Initial Access [69](#ue-initial-access-1)

8.9.2 Bearer context setup over F1-U [70](#bearer-context-setup-over-f1-u)

8.9.3 Bearer context release over F1-U [72](#bearer-context-release-over-f1-u)

8.9.3.1 gNB-CU-CP initiated bearer context release [72](#gnb-cu-cp-initiated-bearer-context-release)

8.9.3.2 gNB-CU-UP initiated bearer context release [72](#gnb-cu-up-initiated-bearer-context-release)

8.9.4 Inter-gNB handover involving gNB-CU-UP change [73](#inter-gnb-handover-involving-gnb-cu-up-change)

8.9.5 Change of gNB-CU-UP [75](#change-of-gnb-cu-up)

8.9.6 RRC State transition [76](#rrc-state-transition-1)

8.9.6.1 RRC Connected to RRC Inactive [76](#rrc-connected-to-rrc-inactive-1)

8.9.6.2 RRC Inactive to other states [77](#rrc-inactive-to-other-states-1)

8.9.7 Trace activation/deactivation over F1 and E1 [79](#trace-activationdeactivation-over-f1-and-e1)

8.9.8 BH RLC channel establishment procedure [79](#bh-rlc-channel-establishment-procedure)

8.9.9 Traffic Mapping [81](#traffic-mapping)

8.9.9.1 Traffic Mapping from IP-layer to Layer-2 [81](#traffic-mapping-from-ip-layer-to-layer-2)

8.9.9.2 BH RLC Channel Mapping on BAP Layer [81](#bh-rlc-channel-mapping-on-bap-layer)

8.9.10 IAB-node release [81](#iab-node-release)

8.9.10.1 IAB-node orderly release [82](#iab-node-orderly-release)

8.9.10.2 IAB-node disorderly release [82](#iab-node-disorderly-release)

8.9.11 IAB-node OAM [82](#iab-node-oam)

8.9.12 Handling of IAB-MTs in INACTIVE State [82](#handling-of-iab-mts-in-inactive-state)

8.9.13 IP Address Allocation for IAB-nodes [83](#ip-address-allocation-for-iab-nodes)

8.9.14 Mobile IAB-node authorization [83](#mobile-iab-node-authorization)

8.9.15 IAB-donor-CU-based NR Cell Identity (NCI) (re-)configuration for mobile IAB cells [84](#iab-donor-cu-based-nr-cell-identity-nci-re-configuration-for-mobile-iab-cells)

8.9.16 TAC/RANAC (re-)configuration for mobile IAB [84](#tacranac-re-configuration-for-mobile-iab)

8.9.17 IAB-node authorization [84](#iab-node-authorization)

8.9.17.1 IAB-node in NSA [84](#iab-node-in-nsa)

8.9.17.2 IAB-node with single IAB-donor in SA [85](#iab-node-with-single-iab-donor-in-sa)

8.9.17.2.1 IAB-node is single-connected [85](#iab-node-is-single-connected)

8.9.17.2.2 IAB-node is NR dual-connected [85](#iab-node-is-nr-dual-connected)

8.9.17.3 IAB-node is served by two IAB-donors in SA [85](#iab-node-is-served-by-two-iab-donors-in-sa)

8.10 Multiple TNLAs for E1 [85](#multiple-tnlas-for-e1)

8.11 Support of Network Sharing with multiple cell-ID broadcast [87](#support-of-network-sharing-with-multiple-cell-id-broadcast)

8.11.1 General [87](#general-4)

8.11.2 Initial Registration – separate PLMN signalling [87](#initial-registration-separate-plmn-signalling)

8.11.3 RRC Connection Reestablishment – separate PLMN signalling [88](#rrc-connection-reestablishment-separate-plmn-signalling)

8.11.4 Support of shared signalling transport [89](#support-of-shared-signalling-transport)

8.12 IAB-node Integration Procedure [89](#iab-node-integration-procedure)

8.12.1 Standalone IAB integration [89](#standalone-iab-integration)

8.12.2 NSA IAB Integration procedure [90](#nsa-iab-integration-procedure)

8.12.3 Mobile IAB-node integration [91](#mobile-iab-node-integration)

8.13 Overall procedures for MDT [92](#overall-procedures-for-mdt)

8.13.0 General [92](#general-5)

8.13.1 Signalling based MDT activation [92](#signalling-based-mdt-activation)

8.13.2 Management based MDT activation [93](#management-based-mdt-activation)

8.13.2.1 General [93](#general-6)

8.13.2.2 Management based MDT Activation in gNB-CU-CP [93](#management-based-mdt-activation-in-gnb-cu-cp)

8.13.2.3 Management based MDT Activation in gNB-DU [94](#management-based-mdt-activation-in-gnb-du)

8.13.2.4 Management based MDT Activation in gNB-CU-UP [95](#management-based-mdt-activation-in-gnb-cu-up)

8.13.2.5 User consent propagation in EN-DC [96](#user-consent-propagation-in-en-dc)

8.13.2.6 User consent propagation in MR-DC with 5GC [97](#user-consent-propagation-in-mr-dc-with-5gc)

8.13.2.7 Management based trace activation in MR-DC with 5GC [98](#management-based-trace-activation-in-mr-dc-with-5gc)

8.13.3 Alignment of MDT and QoE Measurements [99](#alignment-of-mdt-and-qoe-measurements)

8.13.4 MDT reporting [99](#mdt-reporting)

8.14 Self-optimisation [99](#self-optimisation)

8.14.1 Overall procedures for MRO [99](#overall-procedures-for-mro)

8.14.1.1 Signalling of RLF information from gNB-CU to gNB-DU [100](#signalling-of-rlf-information-from-gnb-cu-to-gnb-du)

8.14.1.2 Signalling of RACH information from gNB-CU to gNB-DU [100](#signalling-of-rach-information-from-gnb-cu-to-gnb-du)

8.14.1.3 Reporting of DL LBT failure information from gNB-DU to gNB-CU [101](#reporting-of-dl-lbt-failure-information-from-gnb-du-to-gnb-cu)

8.15 Overall procedures for NR MBS [101](#overall-procedures-for-nr-mbs)

8.15.1 General [101](#general-7)

8.15.1.1 Broadcast MBS Session Setup [101](#broadcast-mbs-session-setup)

8.15.1.1a Broadcast MBS Session Setup for resource efficiency for MOCN [102](#a-broadcast-mbs-session-setup-for-resource-efficiency-for-mocn)

8.15.1.1b Broadcast MBS Session Setup for resource efficiency for RAN sharing with multiple cell-ID broadcast [104](#b-broadcast-mbs-session-setup-for-resource-efficiency-for-ran-sharing-with-multiple-cell-id-broadcast)

8.15.1.2 Multicast MBS Session Context Establishment [105](#multicast-mbs-session-context-establishment)

8.15.1.3 Multicast MRB type re-configuration with F1-U ptp-retransmission tunnel establishment [107](#multicast-mrb-type-re-configuration-with-f1-u-ptp-retransmission-tunnel-establishment)

8.15.2 Mobility procedure for Multicast [107](#mobility-procedure-for-multicast)

8.15.2.1 Inter-gNB-CU Mobility between MBS Supporting nodes [107](#inter-gnb-cu-mobility-between-mbs-supporting-nodes)

8.16 Overall procedures for CPAC [109](#overall-procedures-for-cpac)

8.16.1 MN initiated Conditional PSCell Addition [109](#mn-initiated-conditional-pscell-addition)

8.16.2 MN initiated conditional SN Change [110](#mn-initiated-conditional-sn-change)

8.16.3 SN initiated conditional inter-SN Change [110](#sn-initiated-conditional-inter-sn-change)

8.17 IAB Inter-CU Topology Management [110](#iab-inter-cu-topology-management)

8.17.1 IAB Inter-donor-DU Re-routing [110](#iab-inter-donor-du-re-routing)

8.17.2 IAB Inter-CU Topology Redundancy [110](#iab-inter-cu-topology-redundancy)

8.17.2.1 IAB Inter-CU topological redundancy procedure [110](#iab-inter-cu-topological-redundancy-procedure)

8.17.3 IAB Inter-CU Topology Adaptation [113](#iab-inter-cu-topology-adaptation)

8.17.3.1 IAB inter-CU topology adaptation procedure [113](#iab-inter-cu-topology-adaptation-procedure)

8.17.3.2 IAB inter-CU topology adaptation procedure with descendant IAB-node [116](#iab-inter-cu-topology-adaptation-procedure-with-descendant-iab-node)

8.17.4 IAB Inter-CU Backhaul RLF recovery for single connected IAB-node [118](#_Toc209704864)

8.18 Overall procedure for Small Data Transmission during RRC Inactive [121](#overall-procedure-for-small-data-transmission-during-rrc-inactive)

8.18.1 RACH based SDT [121](#rach-based-sdt)

8.18.2 CG based SDT [122](#cg-based-sdt)

8.18.3 RA-SDT or non-SDT with CG-SDT configuration [124](#ra-sdt-or-non-sdt-with-cg-sdt-configuration)

8.18.4 MT-SDT [125](#mt-sdt)

8.19 Overall procedures for L2 UE-to-Network Relay [126](#overall-procedures-for-l2-ue-to-network-relay)

8.19.1 Remote UE initial access [126](#remote-ue-initial-access)

8.19.2 Remote UE RRC Reestablishment [129](#remote-ue-rrc-reestablishment)

8.19.3 Remote UE RRC Inactive to other states [131](#remote-ue-rrc-inactive-to-other-states)

8.19.4 Service Continuity for L2 U2N relay [133](#service-continuity-for-l2-u2n-relay)

8.19.4.1 Inter-gNB-DU switch from direct to indirect path [133](#inter-gnb-du-switch-from-direct-to-indirect-path)

8.19.4.2 Intra-gNB-DU switch from direct to indirect path [135](#intra-gnb-du-switch-from-direct-to-indirect-path)

8.19.4.3 Inter-gNB-CU switch from direct to indirect path [136](#inter-gnb-cu-switch-from-direct-to-indirect-path)

8.20 Void [138](#void)

8.21 Overall procedures for Network Controlled Repeater [138](#overall-procedures-for-network-controlled-repeater)

8.21.1 Network Controlled Repeater Integration Procedure [138](#network-controlled-repeater-integration-procedure)

8.22 Overall procedures for multi-path support [139](#overall-procedures-for-multi-path-support)

8.22.1 Inter-DU direct path addition on top of indirect path [139](#inter-du-direct-path-addition-on-top-of-indirect-path)

8.22.2 Inter-DU indirect path addition on top of direct path [141](#inter-du-indirect-path-addition-on-top-of-direct-path)

8.22.3 Intra-DU direct path addition on top of indirect path [143](#intra-du-direct-path-addition-on-top-of-indirect-path)

8.22.4 Intra-DU indirect path addition on top of direct path [145](#intra-du-indirect-path-addition-on-top-of-direct-path)

8.23 Mobile IAB migration procedures [146](#mobile-iab-migration-procedures)

8.23.1 Migration of mobile IAB-MT via Xn handover [146](#migration-of-mobile-iab-mt-via-xn-handover)

8.23.2 Migration of mobile IAB-MT via NG handover [147](#migration-of-mobile-iab-mt-via-ng-handover)

8.23.3 Mobile IAB-DU migration procedure [148](#mobile-iab-du-migration-procedure)

8.23.4 Mobile IAB-node RLF recovery [149](#mobile-iab-node-rlf-recovery)

8.24 Timing resiliency service [150](#timing-resiliency-service)

8.24.1 RAN TSS reporting towards the CN [150](#ran-tss-reporting-towards-the-cn)

8.24.2 RAN TSS reporting towards the UE [152](#ran-tss-reporting-towards-the-ue)

9 Synchronization [153](#synchronization)

9.1 gNB Synchronization [153](#gnb-synchronization)

10 NG-RAN interfaces [154](#_Toc209704896)

10.1 NG interface [154](#ng-interface)

10.2 Xn interface [154](#_Toc209704898)

10.3 F1 interface [154](#_Toc209704899)

10.4 E1 interface [154](#_Toc209704900)

10.5 Antenna interface - general principles [154](#antenna-interface---general-principles)

11 Overall procedures in NG-RAN Architecure [154](#overall-procedures-in-ng-ran-architecure)

11.1 Multiple TNLAs for Xn-C [154](#multiple-tnlas-for-xn-c)

Annex A (informative): Deployment scenarios of gNB/en-gNB [156](#annex-a-informative-deployment-scenarios-of-gnben-gnb)

Annex B: NG-RAN Architecture for Radio Access Network Sharing with multiple cell ID broadcast (informative) [157](#annex-b-ng-ran-architecture-for-radio-access-network-sharing-with-multiple-cell-id-broadcast-informative)

Annex C (informative): Change History [158](#annex-c-informative-change-history)

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
