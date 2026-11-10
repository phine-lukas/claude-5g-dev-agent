<!-- table -->
| 3GPP TR 38.821 V16.2.0 (2023-03) (x2) |
| Technical Report (x2) |
| 3rd Generation Partnership Project; Technical Specification Group Radio Access Network; Solutions for NR to support non-terrestrial networks (NTN) (Release 16) (x2) |
| The present document has been developed within the 3rd Generation Partnership Project (3GPP TM ) and may be further elaborated for the purposes of 3GPP. / The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented. / This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification. / Specifications and Reports for implementation of the 3GPP TM system should be obtained via the 3GPP Organizational Partners' Publications Offices. (x2) |
<!-- /table -->

<!-- table -->
| 3GPP Postal address 3GPP support office address 650 Route des Lucioles - Sophia Antipolis Valbonne - FRANCE Tel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16 Internet http://www.3gpp.org |
| Copyright Notification No part may be reproduced except as authorized by written permission. / The copyright and the foregoing restriction extend to reproduction in all media. © 2023, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC). All rights reserved. UMTS™ is a Trade Mark of ETSI registered for the benefit of its members 3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners / LTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners GSM® and the GSM logo are registered and owned by the GSM Association |
<!-- /table -->

#  Contents

Foreword [7](#foreword)

1 Scope [9](#scope)

2 References [9](#references)

3 Definitions of terms, symbols and abbreviations [12](#definitions-of-terms-symbols-and-abbreviations)

3.1 Terms [12](#terms)

3.2 Symbols [13](#symbols)

3.3 Abbreviations [13](#abbreviations)

4 Non-Terrestrial Networks overview and scenarios [15](#non-terrestrial-networks-overview-and-scenarios)

4.1 Non-Terrestrial Networks overview [15](#non-terrestrial-networks-overview)

4.2 Non-Terrestrial Networks reference scenarios [16](#non-terrestrial-networks-reference-scenarios)

5 NTN-based NG-RAN Architectures [19](#ntn-based-ng-ran-architectures)

5.1 Transparent satellite based NG-RAN architecture [19](#transparent-satellite-based-ng-ran-architecture)

5.1.1 Overview [19](#overview)

5.1.2 Detailed description of the architecture [20](#detailed-description-of-the-architecture)

5.1.3 NG-RAN impacts [21](#ng-ran-impacts)

5.2 Regenerative satellite based NG-RAN architectures [22](#regenerative-satellite-based-ng-ran-architectures)

5.2.1 gNB processed payload [22](#gnb-processed-payload)

5.2.1.1 Overview [22](#overview-1)

5.2.1.2 Detailed description of the architecture [23](#detailed-description-of-the-architecture-1)

5.2.1.3 NG-RAN impacts [24](#ng-ran-impacts-1)

5.2.2 gNB-DU processed payload [25](#gnb-du-processed-payload)

5.2.2.1 Overview [25](#overview-2)

5.2.2.2 Detailed description of the architecture [25](#detailed-description-of-the-architecture-2)

5.2.2.3 NG-RAN impacts [27](#ng-ran-impacts-2)

5.2.3 gNB processed payload based on relay-like architectures (Optional) [27](#gnb-processed-payload-based-on-relay-like-architectures-optional)

5.3 Multi connectivity involving NTN-based NG-RAN [28](#multi-connectivity-involving-ntn-based-ng-ran)

5.3.1 Overview [28](#overview-3)

5.3.2 Architecture aspects [28](#architecture-aspects)

5.3.3 NG-RAN impacts [30](#ng-ran-impacts-3)

5.4 Service continuity between NTN and Terrestrial Networks [31](#service-continuity-between-ntn-and-terrestrial-networks)

5.4.1 Scope [32](#scope-1)

5.4.2 Reference scenario [33](#reference-scenario)

5.4.3 Assumptions [33](#assumptions)

6 Radio Layer 1 issues and related solutions [34](#radio-layer-1-issues-and-related-solutions)

6.1 Link-Level and System-Level Evaluations [34](#link-level-and-system-level-evaluations)

6.1.1 System level simulations [34](#system-level-simulations)

6.1.1.1 Simulation assumptions [34](#simulation-assumptions)

6.1.1.2 Calibration results [46](#calibration-results)

6.1.1.3 System Level Simulation Evaluation Results [48](#system-level-simulation-evaluation-results)

6.1.2 Link level simulations [49](#link-level-simulations)

6.1.3 Link Budget Analysis [51](#link-budget-analysis)

6.1.3.1 Link Budget Calculation [51](#link-budget-calculation)

6.1.3.2 Parameters [52](#parameters)

6.1.3.3 Link Budget Results [55](#link-budget-results)

6.1.4 Multiple satellites simulation [57](#multiple-satellites-simulation)

6.1.4.1 Simulation cases [57](#simulation-cases)

6.1.4.2 Methodology for multiple satellites simulation [57](#methodology-for-multiple-satellites-simulation)

6.2 Physical layer control procedures [58](#physical-layer-control-procedures)

6.2.1 Timing relationships [58](#timing-relationships)

6.2.1.1 Background [59](#background)

6.2.1.2 Enhancements [60](#enhancements)

6.2.2 Uplink power control [61](#uplink-power-control)

6.2.3 AMC and delayed CSI feedback [61](#amc-and-delayed-csi-feedback)

6.2.4 Beam management and polarization support [63](#beam-management-and-polarization-support)

6.2.5 Impact of feeder link switch [63](#impact-of-feeder-link-switch)

6.3 Uplink timing advance/RACH procedure [64](#uplink-timing-advancerach-procedure)

6.3.1 General [64](#general)

6.3.2 DL synchronization [64](#dl-synchronization)

6.3.3 Random access [64](#random-access)

6.3.4 Maintenance for UL timing advance and frequency synchronization [65](#maintenance-for-ul-timing-advance-and-frequency-synchronization)

6.4 More delay-tolerant re-transmission mechanisms [66](#more-delay-tolerant-re-transmission-mechanisms)

6.4.1 Disabling of HARQ in NR NTN [66](#disabling-of-harq-in-nr-ntn)

6.4.2 HARQ Optimization for NR NTN [66](#harq-optimization-for-nr-ntn)

7 Radio protocol issues and related solutions [69](#radio-protocol-issues-and-related-solutions)

7.1 Requirements and key issues [69](#requirements-and-key-issues)

7.1.1 Delay [69](#delay)

7.2 User plane enhancements [70](#user-plane-enhancements)

7.2.1 MAC [70](#mac)

7.2.1.1 Random Access [70](#random-access-1)

7.2.1.1.1 4-Step RACH Procedure [70](#step-rach-procedure)

7.2.1.1.1.1 RACH capacity evaluation [70](#rach-capacity-evaluation)

7.2.1.1.1.2 4-step RACH enhancements for Non-Terrestrial Networks [71](#step-rach-enhancements-for-non-terrestrial-networks)

7.2.1.1.2 2-Step RACH Procedure [79](#step-rach-procedure-1)

7.2.1.1.3 Random access enhancements to address mobility issues [79](#random-access-enhancements-to-address-mobility-issues)

7.2.1.1.4 Co-existence with different random access capabilities [80](#co-existence-with-different-random-access-capabilities)

7.2.1.2 Discontinuous Reception (DRX) [80](#discontinuous-reception-drx)

7.2.1.2.1 DRX enhancements [82](#drx-enhancements)

7.2.1.3 Scheduling Request [83](#scheduling-request)

7.2.1.4 HARQ [83](#harq)

7.2.1.5 Uplink scheduling [84](#uplink-scheduling)

7.2.1.5.1 Assignment of uplink resources [84](#assignment-of-uplink-resources)

7.2.2 RLC [85](#rlc)

7.2.2.1 Status Reporting [85](#status-reporting)

7.2.2.2 RLC Sequence Numbers [85](#rlc-sequence-numbers)

7.2.3 PDCP [87](#pdcp)

7.2.3.1 SDU Discard [87](#sdu-discard)

7.2.3.2 Reordering and In-order Delivery [87](#reordering-and-in-order-delivery)

7.2.3.3 PDCP Sequence Number and Window Size [87](#pdcp-sequence-number-and-window-size)

7.2.4 SDAP [89](#sdap)

7.3 Control plane enhancements [89](#control-plane-enhancements)

7.3.1 Idle mode mobility enhancements [90](#idle-mode-mobility-enhancements)

7.3.1.1 General Tracking Area Issues \[16\] [90](#general-tracking-area-issues-16)

7.3.1.2 Moving Tracking Area for NTN LEO, Scenario C2 and D2 \[17\] [91](#moving-tracking-area-for-ntn-leo-scenario-c2-and-d2-17)

7.3.1.3 Fixed Tracking Area for NTN LEO, Scenario C2 and D2 \[17\] [91](#fixed-tracking-area-for-ntn-leo-scenario-c2-and-d2-17)

7.3.1.3.1 Approach 1: For the case when UE location information is unavailable [91](#approach-1-for-the-case-when-ue-location-information-is-unavailable)

7.3.1.3.2 Approach 2: For the case when UE location information is available [92](#approach-2-for-the-case-when-ue-location-information-is-available)

7.3.1.3.3 Tracking Area recommendation [92](#tracking-area-recommendation)

7.3.1.4 Enhancements to idle/inactive UE mobility procedure [92](#enhancements-to-idleinactive-ue-mobility-procedure)

7.3.1.5 Mobility state estimation mechanism [93](#mobility-state-estimation-mechanism)

7.3.1.6 Using ephemeris information and UE location information [93](#using-ephemeris-information-and-ue-location-information)

7.3.1.7 System information broadcast [93](#system-information-broadcast)

7.3.2 Connected mode mobility enhancements [93](#connected-mode-mobility-enhancements)

7.3.2.1 Mobility Challenges for Non-Terrestrial Networks [93](#mobility-challenges-for-non-terrestrial-networks)

7.3.2.1.1 Latency associated with mobility signalling [93](#latency-associated-with-mobility-signalling)

7.3.2.1.2 Measurement Validity [94](#measurement-validity)

7.3.2.1.3 Cell overlap and reduced signal strength variation [95](#cell-overlap-and-reduced-signal-strength-variation)

7.3.2.1.4 Frequent and unavoidable handover [95](#frequent-and-unavoidable-handover)

7.3.2.1.5 Dynamic neighbour cell set [96](#dynamic-neighbour-cell-set)

7.3.2.1.6 Handover for a large number of UEs [96](#handover-for-a-large-number-of-ues)

7.3.2.1.7 Impact of Propagation Delay Difference on Measurements [98](#impact-of-propagation-delay-difference-on-measurements)

7.3.2.2 Mobility Enhancements for Non-Terrestrial Networks [98](#mobility-enhancements-for-non-terrestrial-networks)

7.3.2.2.1 Enhancements to Measurement Configuration/Reporting [98](#enhancements-to-measurement-configurationreporting)

7.3.2.2.2 Conditional Handover [98](#conditional-handover)

7.3.2.2.3 Mobility Configuration [100](#mobility-configuration)

7.3.2.3 Connected mode mobility for feeder link switch for LEO NTN \[18\] [100](#connected-mode-mobility-for-feeder-link-switch-for-leo-ntn-18)

7.3.2.4 Connected mode mobility assumptions [100](#connected-mode-mobility-assumptions)

7.3.3 Paging issue [100](#paging-issue)

7.3.3.1 Paging Capacity [100](#paging-capacity)

7.3.3.1.1 Paging capacity of non-multibeam cell [101](#paging-capacity-of-non-multibeam-cell)

7.3.3.1.2 Example of calculation [101](#example-of-calculation)

7.3.4 Radio Link Monitoring [103](#radio-link-monitoring)

7.3.5 PLMN identities deployment [103](#plmn-identities-deployment)

7.3.6 Ephemeris Data for NTN [103](#ephemeris-data-for-ntn)

7.3.6.1 Representation of Complete Ephemeris Data [103](#representation-of-complete-ephemeris-data)

7.3.6.2 Provision and Use of Ephemeris Data [104](#provision-and-use-of-ephemeris-data)

7.3.6.3 Updating Stored Ephemeris Data [105](#updating-stored-ephemeris-data)

7.4 Earth fixed cells vs Earth moving cells [105](#earth-fixed-cells-vs-earth-moving-cells)

8 Issues and related solutions for NG-RAN architecture and interface protocols [106](#issues-and-related-solutions-for-ng-ran-architecture-and-interface-protocols)

8.1 Tracking area management [106](#tracking-area-management)

8.1.1 NTN cells are fixed w.r.t the ground [106](#ntn-cells-are-fixed-w.r.t-the-ground)

8.1.2 NTN cells are moving w.r.t the ground [106](#ntn-cells-are-moving-w.r.t-the-ground)

8.1.2.1 Tracking Area defined on satellite [107](#tracking-area-defined-on-satellite)

8.1.2.2 Tracking Area defined on earth [107](#tracking-area-defined-on-earth)

8.2 Registration Update and Paging Handling [107](#registration-update-and-paging-handling)

8.2.1 Option 1: UE is capable to determine its location [108](#option-1-ue-is-capable-to-determine-its-location)

8.2.1.1 Mapping of UE location to gNB list in the AMF [108](#mapping-of-ue-location-to-gnb-list-in-the-amf)

8.2.2 Option 2: UE is not capable to determine its location [109](#option-2-ue-is-not-capable-to-determine-its-location)

8.2.2.1 Solution 1: Timing window based Registration update and paging [109](#solution-1-timing-window-based-registration-update-and-paging)

8.2.2.2 Solution 2: UE assisted TA list report/registration and paging [110](#solution-2-ue-assisted-ta-list-reportregistration-and-paging)

8.2.2.3 Solution 3: Multi-Tracking Area ID based Registration update and paging [111](#solution-3-multi-tracking-area-id-based-registration-update-and-paging)

8.2.2.4 Solution 4: UE location determined by NTN based NG-RAN [112](#solution-4-ue-location-determined-by-ntn-based-ng-ran)

8.3 Connected mode mobility [113](#connected-mode-mobility)

8.3.1 Architecture Classification [113](#architecture-classification)

8.3.2 Intra-gNB Mobility ("Monolithic gNB") [114](#intra-gnb-mobility-monolithic-gnb)

8.3.3 Intra-DU Mobility [114](#intra-du-mobility)

8.3.4 Intra-gNB/Inter-DU Mobility [114](#intra-gnbinter-du-mobility)

8.3.5 Inter-gNB Mobility [114](#inter-gnb-mobility)

8.3.5.1 Xn Mobility [114](#xn-mobility)

8.3.5.2 Mobility through the 5GC [114](#mobility-through-the-5gc)

8.3.6 Mobility due to interface change [115](#mobility-due-to-interface-change)

8.3.6.1 Architecture option with gNB on board satellite [115](#architecture-option-with-gnb-on-board-satellite)

8.3.6.2 Architecture option with gNB-DU on board satellite [115](#architecture-option-with-gnb-du-on-board-satellite)

8.3.7 Summary [116](#summary)

8.4 Transport aspects [117](#transport-aspects)

8.4.1 Characteristics of transport links in NTN [117](#characteristics-of-transport-links-in-ntn)

8.4.1.1 Characteristics of SRI on the feeder link [117](#characteristics-of-sri-on-the-feeder-link)

8.4.1.2 Characteristics of Inter Satellite link [118](#characteristics-of-inter-satellite-link)

8.4.1.3 Characteristics of NTN GW [118](#characteristics-of-ntn-gw)

8.4.1.4 Ephemeris [118](#ephemeris)

8.4.2 Transporting F1 over the SRI [118](#transporting-f1-over-the-sri)

8.4.3 Applicability of Xn to NTNs [119](#applicability-of-xn-to-ntns)

8.4.3.1 List of Current Xn Functions [119](#list-of-current-xn-functions)

8.4.3.2 Inter-Satellite Xn [119](#inter-satellite-xn)

8.4.3.3 On-ground NTN-terrestrial Xn [119](#on-ground-ntn-terrestrial-xn)

8.4.3.4 Transporting Xn over SRI [119](#transporting-xn-over-sri)

8.5 Network Identities Handling [120](#network-identities-handling)

8.5.1 General [120](#general-1)

8.5.2 GEO based NTN (Scenario A and B) [120](#geo-based-ntn-scenario-a-and-b)

8.5.3 Non-GEO based NTN (Scenario C and D) [120](#non-geo-based-ntn-scenario-c-and-d)

8.5.3.1 Stationary Identifiers on ground [120](#stationary-identifiers-on-ground)

8.5.3.2 Moving Identifiers on ground [120](#moving-identifiers-on-ground)

8.5.3.3 Possible Implications on Neighbour Relationships [121](#possible-implications-on-neighbour-relationships)

8.5.3.4 Possible PCI Conflicts [121](#possible-pci-conflicts)

8.6 User Location [121](#user-location)

8.7 Feeder link switch over [122](#feeder-link-switch-over)

8.7.1 Principles [122](#principles)

8.7.1.1 Transparent Satellite [122](#transparent-satellite)

8.7.1.1.1 Transparent LEO, Architecture Option 1, different gNBs [122](#transparent-leo-architecture-option-1-different-gnbs)

8.7.1.1.2 Transparent LEO NTN, Architecture Option 1, same gNB [124](#transparent-leo-ntn-architecture-option-1-same-gnb)

8.7.1.2 Regenerative Satellite, Split gNB [124](#regenerative-satellite-split-gnb)

8.7.1.3 Regenerative Satellite, with full gNB on board, Architecture Options 3-5 [125](#regenerative-satellite-with-full-gnb-on-board-architecture-options-3-5)

8.7.1.3.1 Regenerative LEO NTN with one gNB-DU as payload, Architecture Options 3-5 [126](#regenerative-leo-ntn-with-one-gnb-du-as-payload-architecture-options-3-5)

8.7.1.3.2 Regenerative LEO NTN with two gNBs, or gNB-DUs as payload, Architecture Options 3-5 [127](#regenerative-leo-ntn-with-two-gnbs-or-gnb-dus-as-payload-architecture-options-3-5)

8.7.2 Procedures [127](#procedures)

8.7.2.1 Transparent payload case [127](#transparent-payload-case)

8.7.2.2 Regenerative payload case (gNB on board) [128](#regenerative-payload-case-gnb-on-board)

8.7.2.3 Regenerative payload case (gNB split) [129](#regenerative-payload-case-gnb-split)

8.8 Operations & Maintenance (O&M) [130](#operations-maintenance-om)

9 Recommendations on the way forward [130](#recommendations-on-the-way-forward)

9.1 Recommendations from RAN1 [130](#recommendations-from-ran1)

9.2 Recommendations from RAN2 [131](#recommendations-from-ran2)

9.3 Recommendations from RAN3 [132](#recommendations-from-ran3)

9.4 Other assumptions [133](#other-assumptions)

Annex A: Satellite ephemeris [134](#annex-a-satellite-ephemeris)

A.1 Key parameters [134](#a.1-key-parameters)

Annex B: KPI and evaluation assumptions [136](#annex-b-kpi-and-evaluation-assumptions)

B.1 Key Performance Indicators [136](#b.1-key-performance-indicators)

B.2 Performance targets for evaluation purposes [136](#b.2-performance-targets-for-evaluation-purposes)

Annex C: Regulatory Aspects [138](#annex-c-regulatory-aspects)

Annex D (Informative): Change history [140](#annex-d-informative-change-history)

# Foreword

This Technical Report has been produced by the 3rd Generation Partnership Project (3GPP).

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
