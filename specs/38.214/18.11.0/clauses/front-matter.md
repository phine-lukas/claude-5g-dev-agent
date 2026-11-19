3GPP TS 38.214 V18.11.0 (2026-09)

Technical Specification

3rd Generation Partnership Project;

Technical Specification Group Radio Access Network;

NR;

Physical layer procedures for data

(Release 18)

[figure] <img src="media/image2.png" style="width:1.77778in;height:1.03681in" alt="3GPP-logo_web" />

The present document has been developed within the 3rd Generation Partnership Project (3GPP <sup>TM</sup>) and may be further elaborated for the purposes of 3GPP..  
The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented.  
This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification.  
Specifications and Reports for implementation of the 3GPP <sup>TM</sup> system should be obtained via the 3GPP Organizational Partners' Publications Offices.

> Keywords
>
> 3GPP, New Radio, Layer 1
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

Foreword [7](#foreword)

1 Scope [8](#scope)

2 References [8](#references)

3 Definitions of terms, symbols and abbreviations [9](#definitions-of-terms-symbols-and-abbreviations)

3.1 Terms [9](#terms)

3.2 Symbols [9](#symbols)

3.3 Abbreviations [9](#abbreviations)

4 Power control [10](#power-control)

4.1 Power allocation for downlink [10](#power-allocation-for-downlink)

5 Physical downlink shared channel related procedures [11](#physical-downlink-shared-channel-related-procedures)

5.1 UE procedure for receiving the physical downlink shared channel [11](#ue-procedure-for-receiving-the-physical-downlink-shared-channel)

5.1.1 Transmission schemes [17](#transmission-schemes)

5.1.1.1 Transmission scheme 1 [17](#transmission-scheme-1)

5.1.2 Resource allocation [17](#resource-allocation)

5.1.2.1 Resource allocation in time domain [17](#resource-allocation-in-time-domain)

5.1.2.1.1 Determination of the resource allocation table to be used for PDSCH [22](#determination-of-the-resource-allocation-table-to-be-used-for-pdsch)

5.1.2.2 Resource allocation in frequency domain [27](#resource-allocation-in-frequency-domain)

5.1.2.2.1 Downlink resource allocation type 0 [27](#downlink-resource-allocation-type-0)

5.1.2.2.2 Downlink resource allocation type 1 [28](#downlink-resource-allocation-type-1)

5.1.2.2.3 Downlink resource allocation type 1 for multicast/broadcast [29](#downlink-resource-allocation-type-1-for-multicastbroadcast)

5.1.2.3 Physical resource block (PRB) bundling [30](#physical-resource-block-prb-bundling)

5.1.3 Modulation order, target code rate, redundancy version and transport block size determination [31](#modulation-order-target-code-rate-redundancy-version-and-transport-block-size-determination)

5.1.3.1 Modulation order and target code rate determination [33](#modulation-order-and-target-code-rate-determination)

5.1.3.2 Transport block size determination [39](#transport-block-size-determination)

5.1.4 PDSCH resource mapping [43](#pdsch-resource-mapping)

5.1.4.1 PDSCH resource mapping with RB symbol level granularity [43](#pdsch-resource-mapping-with-rb-symbol-level-granularity)

5.1.4.2 PDSCH resource mapping with RE level granularity [44](#pdsch-resource-mapping-with-re-level-granularity)

5.1.5 Antenna ports quasi co-location [47](#antenna-ports-quasi-co-location)

5.1.6 UE procedure for receiving reference signals [56](#ue-procedure-for-receiving-reference-signals)

5.1.6.1 CSI-RS reception procedure [56](#csi-rs-reception-procedure)

5.1.6.1.1 CSI-RS for tracking [57](#csi-rs-for-tracking)

5.1.6.1.2 CSI-RS for L1-RSRP and L1-SINR computation [60](#csi-rs-for-l1-rsrp-and-l1-sinr-computation)

5.1.6.1.3 CSI-RS for mobility [60](#csi-rs-for-mobility)

5.1.6.2 DM-RS reception procedure [61](#dm-rs-reception-procedure)

5.1.6.3 PT-RS reception procedure [65](#pt-rs-reception-procedure)

5.1.6.4 SRS reception procedure for CLI [67](#srs-reception-procedure-for-cli)

5.1.6.5 PRS reception procedure [67](#prs-reception-procedure)

5.1.6.5.1 PRS receiver frequency hopping [74](#prs-receiver-frequency-hopping)

5.1.6.5.2 PRS for carrier phase positioning [74](#prs-for-carrier-phase-positioning)

5.1.6.5.3 PRS bandwidth aggregation for positioning measurements [75](#prs-bandwidth-aggregation-for-positioning-measurements)

5.1.7 Code block group based PDSCH transmission [76](#code-block-group-based-pdsch-transmission)

5.1.7.1 UE procedure for grouping of code blocks to code block groups [76](#ue-procedure-for-grouping-of-code-blocks-to-code-block-groups)

5.1.7.2 UE procedure for receiving code block group based transmissions [76](#ue-procedure-for-receiving-code-block-group-based-transmissions)

5.2 UE procedure for reporting channel state information (CSI) [76](#ue-procedure-for-reporting-channel-state-information-csi)

5.2.1 Channel state information framework [76](#channel-state-information-framework)

5.2.1.1 Reporting settings [77](#reporting-settings)

5.2.1.2 Resource settings [78](#resource-settings)

5.2.1.3 (void) [79](#void)

5.2.1.4 Reporting configurations [79](#reporting-configurations)

5.2.1.4.1 Resource Setting configuration [81](#resource-setting-configuration)

5.2.1.4.2 Report quantity configurations [83](#report-quantity-configurations)

5.2.1.4.3 L1-RSRP Reporting [90](#l1-rsrp-reporting)

5.2.1.4.4 L1-SINR Reporting [91](#l1-sinr-reporting)

5.2.1.4.5 TDCP Reporting [92](#tdcp-reporting)

5.2.1.5 Triggering/activation of CSI Reports and CSI-RS [92](#triggeringactivation-of-csi-reports-and-csi-rs)

5.2.1.5.1 Aperiodic CSI Reporting/Aperiodic CSI-RS when the triggering PDCCH and the CSI-RS have the same numerology [92](#aperiodic-csi-reportingaperiodic-csi-rs-when-the-triggering-pdcch-and-the-csi-rs-have-the-same-numerology)

5.2.1.5.1a Aperiodic CSI Reporting/Aperiodic CSI-RS when the triggering PDCCH and the CSI-RS have different numerologies [98](#a-aperiodic-csi-reportingaperiodic-csi-rs-when-the-triggering-pdcch-and-the-csi-rs-have-different-numerologies)

5.2.1.5.2 Semi-persistent CSI/Semi-persistent CSI-RS [101](#semi-persistent-csisemi-persistent-csi-rs)

5.2.1.5.3 Aperiodic CSI-RS for tracking for fast SCell activation [102](#aperiodic-csi-rs-for-tracking-for-fast-scell-activation-1)

5.2.1.6 CSI processing criteria [102](#csi-processing-criteria)

5.2.2 Channel state information [105](#channel-state-information)

5.2.2.1 Channel quality indicator (CQI) [105](#channel-quality-indicator-cqi)

5.2.2.1.1 (void) [108](#void-1)

5.2.2.2 Precoding matrix indicator (PMI) [108](#precoding-matrix-indicator-pmi)

5.2.2.2.1 Type I Single-Panel Codebook [108](#type-i-single-panel-codebook)

5.2.2.2.2 Type I Multi-Panel Codebook [114](#type-i-multi-panel-codebook)

5.2.2.2.3 Type II Codebook [118](#type-ii-codebook)

5.2.2.2.4 Type II Port Selection Codebook [124](#type-ii-port-selection-codebook)

5.2.2.2.5 Enhanced Type II Codebook [127](#enhanced-type-ii-codebook)

5.2.2.2.6 Enhanced Type II Port Selection Codebook [134](#enhanced-type-ii-port-selection-codebook)

5.2.2.2.7 Further enhanced Type II port selection codebook [135](#further-enhanced-type-ii-port-selection-codebook)

5.2.2.2.8 Enhanced Type II codebook for CJT [140](#enhanced-type-ii-codebook-for-cjt)

5.2.2.2.9 Further enhanced Type II port selection codebook for CJT [146](#further-enhanced-type-ii-port-selection-codebook-for-cjt)

5.2.2.2.10 Enhanced Type II codebook for predicted PMI [152](#enhanced-type-ii-codebook-for-predicted-pmi)

5.2.2.2.11 Further enhanced Type II port selection codebook for predicted PMI [156](#further-enhanced-type-ii-port-selection-codebook-for-predicted-pmi)

5.2.2.3 Reference signal (CSI-RS) [157](#reference-signal-csi-rs)

5.2.2.3.1 NZP CSI-RS [157](#nzp-csi-rs)

5.2.2.4 Channel State Information – Interference Measurement (CSI-IM) [158](#channel-state-information-interference-measurement-csi-im)

5.2.2.5 CSI reference resource definition [158](#csi-reference-resource-definition)

5.2.2.5.1 UE assumptions for CQI/PMI/RI calculation [161](#ue-assumptions-for-cqipmiri-calculation)

5.2.2.5.1a UE assumptions for CQI/PMI/RI calculation for NCJT [162](#a-ue-assumptions-for-cqipmiri-calculation-for-ncjt)

5.2.2.5.1b UE assumptions for CQI/PMI/RI calculation for CJT [163](#b-ue-assumptions-for-cqipmiri-calculation-for-cjt)

5.2.2.5.1c UE assumptions for CQI/PMI/RI calculation for predicted CSI [163](#c-ue-assumptions-for-cqipmiri-calculation-for-predicted-csi)

5.2.3 CSI reporting using PUSCH [163](#csi-reporting-using-pusch)

5.2.4 CSI reporting using PUCCH [169](#csi-reporting-using-pucch)

5.2.5 Priority rules for CSI reports [170](#priority-rules-for-csi-reports)

5.3 UE PDSCH processing procedure time [171](#ue-pdsch-processing-procedure-time)

5.3.1 Application delay of the minimum scheduling offset restriction [173](#application-delay-of-the-minimum-scheduling-offset-restriction)

5.4 UE CSI computation time [174](#ue-csi-computation-time)

5.5 UE PDSCH reception preparation time with different subcarrier spacings for PDCCH and PDSCH in different cells [176](#ue-pdsch-reception-preparation-time-with-different-subcarrier-spacings-for-pdcch-and-pdsch-in-different-cells)

6 Physical uplink shared channel related procedure [177](#physical-uplink-shared-channel-related-procedure)

6.1 UE procedure for transmitting the physical uplink shared channel [177](#ue-procedure-for-transmitting-the-physical-uplink-shared-channel)

6.1.1 Transmission schemes [180](#transmission-schemes-1)

6.1.1.1 Codebook based UL transmission [181](#codebook-based-ul-transmission)

6.1.1.2 Non-Codebook based UL transmission [184](#non-codebook-based-ul-transmission)

6.1.2 Resource allocation [186](#resource-allocation-1)

6.1.2.1 Resource allocation in time domain [186](#resource-allocation-in-time-domain-1)

6.1.2.1.1 Determination of the resource allocation table to be used for PUSCH [197](#determination-of-the-resource-allocation-table-to-be-used-for-pusch)

6.1.2.2 Resource allocation in frequency domain [200](#resource-allocation-in-frequency-domain-1)

6.1.2.2.1 Uplink resource allocation type 0 [201](#uplink-resource-allocation-type-0)

6.1.2.2.2 Uplink resource allocation type 1 [201](#uplink-resource-allocation-type-1)

6.1.2.2.3 Uplink resource allocation type 2 [202](#uplink-resource-allocation-type-2)

6.1.2.3 Resource allocation for uplink transmission with configured grant [204](#resource-allocation-for-uplink-transmission-with-configured-grant)

6.1.2.3.1 Transport Block repetition for uplink transmissions of PUSCH repetition Type A with a configured grant [206](#transport-block-repetition-for-uplink-transmissions-of-pusch-repetition-type-a-with-a-configured-grant)

6.1.2.3.2 Transport Block repetition for uplink transmissions of PUSCH repetition Type B with a configured grant [208](#transport-block-repetition-for-uplink-transmissions-of-pusch-repetition-type-b-with-a-configured-grant)

6.1.2.3.3 Transport Block repetition for uplink transmissions of TB processing over multiple slots with a configured grant [209](#transport-block-repetition-for-uplink-transmissions-of-tb-processing-over-multiple-slots-with-a-configured-grant)

6.1.3 UE procedure for applying transform precoding on PUSCH [209](#ue-procedure-for-applying-transform-precoding-on-pusch)

6.1.4 Modulation order, redundancy version and transport block size determination [211](#modulation-order-redundancy-version-and-transport-block-size-determination)

6.1.4.1 Modulation order and target code rate determination [212](#modulation-order-and-target-code-rate-determination-1)

6.1.4.2 Transport block size determination [217](#transport-block-size-determination-1)

6.1.5 Code block group based PUSCH transmission [218](#code-block-group-based-pusch-transmission)

6.1.5.1 UE procedure for grouping of code blocks to code block groups [219](#ue-procedure-for-grouping-of-code-blocks-to-code-block-groups-1)

6.1.5.2 UE procedure for transmitting code block group based transmissions [219](#ue-procedure-for-transmitting-code-block-group-based-transmissions)

6.1.6 Uplink switching [219](#uplink-switching)

6.1.6.1 Uplink switching for EN-DC [220](#uplink-switching-for-en-dc)

6.1.6.2 Uplink switching for carrier aggregation [221](#uplink-switching-for-carrier-aggregation)

6.1.6.2.0 Uplink switching with two uplink bands [221](#uplink-switching-with-two-uplink-bands)

6.1.6.2.1 void [222](#void-2)

6.1.6.2.2 Uplink switching with 3 or 4 uplink bands [222](#uplink-switching-with-3-or-4-uplink-bands)

6.1.6.3 Uplink switching with two uplink bands for supplementary uplink [223](#uplink-switching-with-two-uplink-bands-for-supplementary-uplink)

6.1.7 UE procedure for determining time domain windows for bundling DM-RS [223](#ue-procedure-for-determining-time-domain-windows-for-bundling-dm-rs)

6.2 UE reference signal (RS) procedure [226](#ue-reference-signal-rs-procedure)

6.2.1 UE sounding procedure [226](#ue-sounding-procedure)

6.2.1.1 UE SRS frequency hopping procedure [234](#ue-srs-frequency-hopping-procedure)

6.2.1.2 UE sounding procedure for DL CSI acquisition [235](#ue-sounding-procedure-for-dl-csi-acquisition)

6.2.1.3 UE sounding procedure between component carriers [240](#ue-sounding-procedure-between-component-carriers)

6.2.1.4 UE sounding procedure for positioning purposes [242](#ue-sounding-procedure-for-positioning-purposes)

6.2.1.4.1 SRS frequency hopping for positioning [244](#srs-frequency-hopping-for-positioning)

6.2.1.4.2 SRS bandwidth aggregation for positioning measurements [245](#srs-bandwidth-aggregation-for-positioning-measurements)

6.2.2 UE DM-RS transmission procedure [246](#ue-dm-rs-transmission-procedure)

6.2.3 UE PT-RS transmission procedure [248](#ue-pt-rs-transmission-procedure)

6.2.3.1 UE PT-RS transmission procedure when transform precoding is not enabled [248](#ue-pt-rs-transmission-procedure-when-transform-precoding-is-not-enabled)

6.2.3.2 UE PT-RS transmission procedure when transform precoding is enabled [252](#ue-pt-rs-transmission-procedure-when-transform-precoding-is-enabled)

6.3 UE PUSCH frequency hopping procedure [252](#_Toc219373058)

6.3.1 Frequency hopping for PUSCH repetition Type A and for TB processing over multiple slots [252](#frequency-hopping-for-pusch-repetition-type-a-and-for-tb-processing-over-multiple-slots)

6.3.2 Frequency hopping for PUSCH repetition Type B [254](#frequency-hopping-for-pusch-repetition-type-b)

6.4 UE PUSCH preparation procedure time [255](#ue-pusch-preparation-procedure-time)

7 UE procedures for transmitting and receiving on a carrier with intra-cell guard bands [256](#ue-procedures-for-transmitting-and-receiving-on-a-carrier-with-intra-cell-guard-bands)

8 Physical sidelink shared channel related procedures [257](#physical-sidelink-shared-channel-related-procedures)

8.1 UE procedure for transmitting the physical sidelink shared channel [258](#ue-procedure-for-transmitting-the-physical-sidelink-shared-channel)

8.1.1 Transmission schemes [260](#transmission-schemes-2)

8.1.2 Resource allocation [261](#resource-allocation-2)

8.1.2.1 Resource allocation in time domain [261](#resource-allocation-in-time-domain-2)

8.1.2.2 Resource allocation in frequency domain [262](#resource-allocation-in-frequency-domain-2)

8.1.3 Modulation order, target code rate, redundancy version and transport block size determination [263](#modulation-order-target-code-rate-redundancy-version-and-transport-block-size-determination-1)

8.1.3.1 Modulation order and target code rate determination [263](#modulation-order-and-target-code-rate-determination-2)

8.1.3.2 Transport block size determination [263](#transport-block-size-determination-2)

8.1.4 UE procedure for determining the subset of resources to be reported to higher layers in PSSCH resource selection in sidelink resource allocation mode 2 [264](#ue-procedure-for-determining-the-subset-of-resources-to-be-reported-to-higher-layers-in-pssch-resource-selection-in-sidelink-resource-allocation-mode-2)

8.1.4A UE procedure for determining a set of preferred or non-preferred resources for another UE's transmission [272](#a-ue-procedure-for-determining-a-set-of-preferred-or-non-preferred-resources-for-another-ues-transmission)

8.1.4B Void [273](#b-void)

8.1.4C UE procedure for using a received non-preferred resource set [273](#c-ue-procedure-for-using-a-received-non-preferred-resource-set)

8.1.5 UE procedure for determining slots and resource blocks for PSSCH transmission associated with an SCI format 1-A [274](#ue-procedure-for-determining-slots-and-resource-blocks-for-pssch-transmission-associated-with-an-sci-format-1-a)

8.1.5A UE procedure for determining slots and resource blocks indicated by a preferred or non-preferred resource set [276](#a-ue-procedure-for-determining-slots-and-resource-blocks-indicated-by-a-preferred-or-non-preferred-resource-set)

8.1.6 Sidelink congestion control in sidelink resource allocation mode 2 [276](#sidelink-congestion-control-in-sidelink-resource-allocation-mode-2)

8.1.7 UE procedure for determining the number of logical slots for a reservation period [277](#ue-procedure-for-determining-the-number-of-logical-slots-for-a-reservation-period)

8.2 UE procedure for transmitting sidelink reference signals [277](#ue-procedure-for-transmitting-sidelink-reference-signals)

8.2.1 CSI-RS transmission procedure [277](#csi-rs-transmission-procedure)

8.2.2 PSSCH DM-RS transmission procedure [278](#pssch-dm-rs-transmission-procedure)

8.2.3 PT-RS transmission procedure [278](#pt-rs-transmission-procedure)

8.2.4 SL PRS transmission procedure [278](#sl-prs-transmission-procedure)

8.2.4.1 Resource allocation [278](#resource-allocation-3)

8.2.4.1.1 Resource allocation in time domain [279](#resource-allocation-in-time-domain-3)

8.2.4.1.2 Resource allocation in frequency domain [279](#resource-allocation-in-frequency-domain-3)

8.2.4.2 UE procedure for determining the subset of resources to be reported to higher layers in SL PRS resource selection in a dedicated SL PRS resource pool in sidelink resource allocation mode 2 [280](#ue-procedure-for-determining-the-subset-of-resources-to-be-reported-to-higher-layers-in-sl-prs-resource-selection-in-a-dedicated-sl-prs-resource-pool-in-sidelink-resource-allocation-mode-2)

8.2.4.2A UE procedure for determining slots and SL PRS resource(s) associated with an SCI format 1-B in a dedicated SL PRS resource pool [281](#a-ue-procedure-for-determining-slots-and-sl-prs-resources-associated-with-an-sci-format-1-b-in-a-dedicated-sl-prs-resource-pool)

8.2.4.3 Sidelink congestion control in a dedicated SL PRS resource pool in sidelink resource allocation mode 2 [282](#sidelink-congestion-control-in-a-dedicated-sl-prs-resource-pool-in-sidelink-resource-allocation-mode-2)

8.3 UE procedure for receiving the physical sidelink shared channel [282](#ue-procedure-for-receiving-the-physical-sidelink-shared-channel)

8.4 UE procedure for receiving reference signals [282](#ue-procedure-for-receiving-reference-signals-1)

8.4.1 CSI-RS reception procedure [282](#csi-rs-reception-procedure-1)

8.4.2 DM-RS reception procedure for RSRP computation [282](#dm-rs-reception-procedure-for-rsrp-computation)

8.4.3 PT-RS reception procedure [283](#pt-rs-reception-procedure-1)

8.4.4 SL PRS reception procedure [283](#sl-prs-reception-procedure)

8.5 UE procedure for reporting channel state information (CSI) [284](#ue-procedure-for-reporting-channel-state-information-csi-1)

8.5.1 Channel state information framework [284](#channel-state-information-framework-1)

8.5.1.1 Reporting configurations [284](#reporting-configurations-1)

8.5.1.2 Triggering of sidelink CSI reports [284](#triggering-of-sidelink-csi-reports)

8.5.2 Channel state information [284](#channel-state-information-1)

8.5.2.1 CSI reporting quantities [284](#csi-reporting-quantities)

8.5.2.1.1 Channel quality indicator (CQI) [284](#channel-quality-indicator-cqi-1)

8.5.2.2 Reference signal (CSI-RS) [285](#reference-signal-csi-rs-1)

8.5.2.3 CSI reference resource definition [285](#csi-reference-resource-definition-1)

8.5.3 CSI reporting [286](#csi-reporting)

8.6 UE PSSCH preparation procedure time [286](#ue-pssch-preparation-procedure-time)

9 UE procedures for transmitting and receiving for RTT-based propagation delay compensation [286](#ue-procedures-for-transmitting-and-receiving-for-rtt-based-propagation-delay-compensation)

9.1 PRS reception procedure for RTT-based propagation delay compensation [287](#prs-reception-procedure-for-rtt-based-propagation-delay-compensation)

Annex A (informative): Change history [289](#annex-a-informative-change-history)

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
