3GPP TS 38.213 V18.9.0 (2026-09)

Technical Specification

3rd Generation Partnership Project;

Technical Specification Group Radio Access Network;

NR;  
Physical layer procedures for control

(Release 18)

[figure] <img src="media/image2.png" style="width:1.78125in;height:1.04167in" alt="3GPP-logo_web" />

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

Foreword [6](#foreword)

1 Scope [7](#scope)

2 References [7](#references)

3 Definitions of terms, symbols and abbreviations [8](#definitions-of-terms-symbols-and-abbreviations)

3.1 Terms [8](#terms)

3.2 Symbols [8](#symbols)

3.3 Abbreviations [8](#abbreviations)

4 Synchronization procedures [10](#synchronization-procedures)

4.1 Cell search [10](#cell-search)

4.2 Transmission timing adjustments [12](#transmission-timing-adjustments)

4.3 Timing for secondary cell activation / deactivation [14](#timing-for-secondary-cell-activation-deactivation)

5 Radio link monitoring [15](#radio-link-monitoring)

6 Link recovery procedures [16](#link-recovery-procedures)

7 Uplink Power control [22](#uplink-power-control)

7.1 Physical uplink shared channel [23](#physical-uplink-shared-channel)

7.1.1 UE behaviour [24](#ue-behaviour)

7.2 Physical uplink control channel [37](#physical-uplink-control-channel)

7.2.1 UE behaviour [37](#ue-behaviour-1)

7.3 Sounding reference signals [43](#sounding-reference-signals)

7.3.1 UE behaviour [43](#ue-behaviour-2)

7.4 Physical random access channel [46](#physical-random-access-channel)

7.5 Prioritizations for transmission power reductions [48](#prioritizations-for-transmission-power-reductions)

7.6 Dual connectivity [49](#dual-connectivity)

7.6.1 EN-DC [49](#en-dc)

7.6.1A NE-DC [50](#a-ne-dc)

7.6.2 NR-DC [50](#nr-dc)

7.7 Power headroom report [52](#power-headroom-report)

7.7.1 Type 1 PH report [53](#type-1-ph-report)

7.7.2 Type 2 PH report [57](#type-2-ph-report)

7.7.3 Type 3 PH report [57](#type-3-ph-report)

8 Random access procedure [58](#random-access-procedure)

8.1 Random access preamble [59](#random-access-preamble)

8.1A PUSCH for Type-2 random access procedure [63](#a-pusch-for-type-2-random-access-procedure)

8.2 Random access response - Type-1 random access procedure [65](#random-access-response---type-1-random-access-procedure)

8.2A Random access response - Type-2 random access procedure [67](#a-random-access-response---type-2-random-access-procedure)

8.3 PUSCH scheduled by RAR UL grant [69](#pusch-scheduled-by-rar-ul-grant)

8.4 PDSCH with UE contention resolution identity [71](#pdsch-with-ue-contention-resolution-identity)

9 UE procedure for reporting control information [71](#ue-procedure-for-reporting-control-information)

9.A PUCCH cell switching [81](#a-pucch-cell-switching)

9.1 HARQ-ACK codebook determination [82](#harq-ack-codebook-determination)

9.1.1 CBG-based HARQ-ACK codebook determination [83](#cbg-based-harq-ack-codebook-determination)

9.1.2 Type-1 HARQ-ACK codebook determination [84](#type-1-harq-ack-codebook-determination)

9.1.2.1 Type-1 HARQ-ACK codebook in physical uplink control channel [86](#type-1-harq-ack-codebook-in-physical-uplink-control-channel)

9.1.2.2 Type-1 HARQ-ACK codebook in physical uplink shared channel [98](#type-1-harq-ack-codebook-in-physical-uplink-shared-channel)

9.1.3 Type-2 HARQ-ACK codebook determination [100](#type-2-harq-ack-codebook-determination)

9.1.3.1 Type-2 HARQ-ACK codebook in physical uplink control channel [101](#type-2-harq-ack-codebook-in-physical-uplink-control-channel)

9.1.3.2 Type-2 HARQ-ACK codebook in physical uplink shared channel [117](#type-2-harq-ack-codebook-in-physical-uplink-shared-channel)

9.1.3.3 Type-2 HARQ-ACK codebook grouping and HARQ-ACK retransmission [118](#type-2-harq-ack-codebook-grouping-and-harq-ack-retransmission)

9.1.4 Type-3 HARQ-ACK codebook determination [120](#type-3-harq-ack-codebook-determination)

9.1.5 HARQ-ACK codebook retransmission [124](#harq-ack-codebook-retransmission)

9.2 UCI reporting in physical uplink control channel [126](#uci-reporting-in-physical-uplink-control-channel)

9.2.1 PUCCH Resource Sets [126](#pucch-resource-sets)

9.2.2 PUCCH Formats for UCI transmission [130](#pucch-formats-for-uci-transmission)

9.2.3 UE procedure for reporting HARQ-ACK [132](#ue-procedure-for-reporting-harq-ack)

9.2.4 UE procedure for reporting SR [135](#ue-procedure-for-reporting-sr)

9.2.5 UE procedure for reporting multiple UCI types [136](#ue-procedure-for-reporting-multiple-uci-types)

9.2.5.0 UE procedure for prioritization between SL HARQ-ACK information in a PUCCH and DL HARQ-ACK or SR or CSI in a PUCCH [141](#ue-procedure-for-prioritization-between-sl-harq-ack-information-in-a-pucch-and-dl-harq-ack-or-sr-or-csi-in-a-pucch)

9.2.5.1 UE procedure for multiplexing HARQ-ACK or CSI and SR in a PUCCH [142](#ue-procedure-for-multiplexing-harq-ack-or-csi-and-sr-in-a-pucch)

9.2.5.2 UE procedure for multiplexing HARQ-ACK/SR/CSI in a PUCCH [143](#ue-procedure-for-multiplexing-harq-acksrcsi-in-a-pucch)

9.2.5.3 UE procedure for reporting UCI of different priorities [147](#ue-procedure-for-reporting-uci-of-different-priorities)

9.2.5.4 UE procedure for deferring HARQ-ACK for SPS PDSCH [148](#ue-procedure-for-deferring-harq-ack-for-sps-pdsch)

9.2.6 PUCCH repetition procedure [150](#pucch-repetition-procedure)

9.3 UCI reporting in physical uplink shared channel [152](#uci-reporting-in-physical-uplink-shared-channel)

9.3.1 UE procedure for reporting UTO-UCI [157](#ue-procedure-for-reporting-uto-uci)

10 UE procedure for receiving control information [157](#ue-procedure-for-receiving-control-information)

10.1 UE procedure for determining physical downlink control channel assignment [171](#ue-procedure-for-determining-physical-downlink-control-channel-assignment)

10.1.1 Self-carrier and cross-carrier scheduling on the primary cell [194](#self-carrier-and-cross-carrier-scheduling-on-the-primary-cell)

10.2 PDCCH validation for DL SPS and UL grant Type 2 [194](#pdcch-validation-for-dl-sps-and-ul-grant-type-2)

10.2A PDCCH validation for SL configured grant Type 2 [196](#a-pdcch-validation-for-sl-configured-grant-type-2)

10.3 PDCCH monitoring indication and dormancy/non-dormancy behaviour for SCells [197](#pdcch-monitoring-indication-and-dormancynon-dormancy-behaviour-for-scells)

10.4 Search space set group switching and skipping of PDCCH monitoring [200](#search-space-set-group-switching-and-skipping-of-pdcch-monitoring)

10.4A PDCCH monitoring for early indication of paging [204](#a-pdcch-monitoring-for-early-indication-of-paging)

10.4B Indication of TRS resources [205](#b-indication-of-trs-resources)

10.5 HARQ-ACK information for PUSCH transmissions [205](#harq-ack-information-for-pusch-transmissions)

11 UE-group common signalling [206](#ue-group-common-signalling)

11.1 Slot configuration [206](#slot-configuration)

11.1.1 UE procedure for determining slot format [212](#ue-procedure-for-determining-slot-format)

11.2 Interrupted transmission indication [219](#interrupted-transmission-indication)

11.2A Cancellation indication [220](#a-cancellation-indication)

11.3 Group TPC commands for PUCCH/PUSCH [221](#group-tpc-commands-for-pucchpusch)

11.4 SRS switching [222](#srs-switching)

11.5 Adaptation of cell operation [223](#adaptation-of-cell-operation)

12 Bandwidth part operation [224](#bandwidth-part-operation)

13 UE procedure for monitoring Type0-PDCCH CSS sets [227](#ue-procedure-for-monitoring-type0-pdcch-css-sets)

14 Integrated access-backhaul operation [241](#integrated-access-backhaul-operation)

15 Dual active protocol stack based handover [248](#dual-active-protocol-stack-based-handover)

16 UE procedures for sidelink [249](#ue-procedures-for-sidelink)

16.1 Synchronization procedures [250](#synchronization-procedures-1)

16.2 Power control [253](#power-control)

16.2.0 S-SS/PSBCH blocks [253](#s-sspsbch-blocks)

16.2.1 PSSCH [254](#pssch)

16.2.2 PSCCH [255](#pscch)

16.2.3 PSFCH [255](#psfch)

16.2.3A SL PRS [260](#a-sl-prs)

16.2.4 Prioritization of transmissions/receptions [261](#prioritization-of-transmissionsreceptions)

16.2.4.1 Simultaneous NR and E-UTRA transmission/reception [261](#simultaneous-nr-and-e-utra-transmissionreception)

16.2.4.2 Simultaneous PSFCH transmission/reception [262](#simultaneous-psfch-transmissionreception)

16.2.4.3 Simultaneous SL and UL transmissions/receptions [263](#simultaneous-sl-and-ul-transmissionsreceptions)

16.2.4.3.1 Prioritizations for sidelink and uplink transmissions/receptions [263](#prioritizations-for-sidelink-and-uplink-transmissionsreceptions)

16.2.5 SL Carrier Aggregation [265](#sl-carrier-aggregation)

16.3 UE procedure for reporting and obtaining control information in PSFCH [265](#ue-procedure-for-reporting-and-obtaining-control-information-in-psfch)

16.3.0 UE procedure for transmitting PSFCH with control information [265](#ue-procedure-for-transmitting-psfch-with-control-information)

16.3.1 UE procedure for receiving PSFCH with control information [270](#ue-procedure-for-receiving-psfch-with-control-information)

16.4 UE procedure for transmitting PSCCH [271](#ue-procedure-for-transmitting-pscch)

16.4A UE procedure for transmitting PSCCH in dedicated SL PRS resource pool [272](#a-ue-procedure-for-transmitting-pscch-in-dedicated-sl-prs-resource-pool)

16.5 UE procedure for reporting HARQ-ACK on uplink [273](#ue-procedure-for-reporting-harq-ack-on-uplink)

16.5.1 Type-1 HARQ-ACK codebook determination [276](#type-1-harq-ack-codebook-determination-1)

16.5.1.1 Type-1 HARQ-ACK codebook in physical uplink control channel [276](#type-1-harq-ack-codebook-in-physical-uplink-control-channel-1)

16.5.1.2 Type-1 HARQ-ACK codebook in physical uplink shared channel [278](#type-1-harq-ack-codebook-in-physical-uplink-shared-channel-1)

16.5.2 Type-2 HARQ-ACK codebook determination [279](#type-2-harq-ack-codebook-determination-1)

16.5.2.1 Type-2 HARQ-ACK codebook in physical uplink control channel [279](#type-2-harq-ack-codebook-in-physical-uplink-control-channel-1)

16.5.2.2 Type-2 HARQ-ACK codebook in physical uplink shared channel [281](#type-2-harq-ack-codebook-in-physical-uplink-shared-channel-1)

16.6 UE procedure for LTE sidelink transmission [282](#ue-procedure-for-lte-sidelink-transmission)

16.7 Operation for in-device coexistence and for co-channel coexistence [282](#operation-for-in-device-coexistence-and-for-co-channel-coexistence)

17 UE with reduced capabilities [282](#ue-with-reduced-capabilities)

17.1 First procedures for RedCap UE [282](#first-procedures-for-redcap-ue)

17.1A Second procedures for RedCap UE [284](#a-second-procedures-for-redcap-ue)

17.2 Half-Duplex UE in paired spectrum [285](#half-duplex-ue-in-paired-spectrum)

18 Multicast Broadcast Services [286](#multicast-broadcast-services)

19 PUSCH transmission in RRC_INACTIVE state [291](#pusch-transmission-in-rrc_inactive-state)

19.1 Configured-grant based PUSCH transmission [291](#configured-grant-based-pusch-transmission)

19.2 Random-access based PUSCH transmission [293](#random-access-based-pusch-transmission)

20 Network controlled repeater [293](#network-controlled-repeater)

21 L1/L2-triggered mobility procedures [296](#l1l2-triggered-mobility-procedures)

21.1 Configured-grant PUSCH transmission in RACH-less LTM cell switch [297](#configured-grant-pusch-transmission-in-rach-less-ltm-cell-switch)

22 PUSCH transmission in RACH-less handover [298](#pusch-transmission-in-rach-less-handover)

22.1 Configured-grant PUSCH transmission [298](#configured-grant-pusch-transmission)

22.2 Dynamic-grant PUSCH transmission [299](#dynamic-grant-pusch-transmission)

Annex A (informative): Change history [300](#annex-a-informative-change-history)

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
