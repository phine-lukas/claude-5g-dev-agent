<!-- table -->
| 3GPP TS 38.212 V18.8.0 (2025-12) (x2) |
| Technical Specification (x2) |
| 3rd Generation Partnership Project; Technical Specification Group Radio Access Network; NR; Multiplexing and channel coding (Release 18) (x2) |
| The present document has been developed within the 3rd Generation Partnership Project (3GPP TM ) and may be further elaborated for the purposes of 3GPP. / The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented. / This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification. / Specifications and Reports for implementation of the 3GPP TM system should be obtained via the 3GPP Organizational Partners' Publications Offices. (x2) |
<!-- /table -->

<!-- table -->
| 3GPP Postal address 3GPP support office address 650 Route des Lucioles - Sophia Antipolis Valbonne - FRANCE Tel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16 Internet http://www.3gpp.org |
| Copyright Notification No part may be reproduced except as authorized by written permission. / The copyright and the foregoing restriction extend to reproduction in all media. © 2025, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC). All rights reserved. UMTS™ is a Trade Mark of ETSI registered for the benefit of its members 3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners / LTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners GSM® and the GSM logo are registered and owned by the GSM Association |
<!-- /table -->

#  Contents

Foreword [6](#foreword)

1 Scope [8](#scope)

2 References [8](#references)

3 Definitions of terms, symbols and abbreviations [8](#definitions-of-terms-symbols-and-abbreviations)

3.1 Terms [8](#terms)

3.2 Symbols [8](#symbols)

3.3 Abbreviations [9](#abbreviations)

4 Mapping to physical channels [10](#mapping-to-physical-channels)

4.1 Uplink [10](#uplink)

4.2 Downlink [10](#downlink)

4.3 Sidelink [10](#sidelink)

5 General procedures [11](#general-procedures)

5.1 CRC calculation [11](#crc-calculation)

5.2 Code block segmentation and code block CRC attachment [12](#code-block-segmentation-and-code-block-crc-attachment)

5.2.1 Polar coding [12](#polar-coding)

5.2.2 Low density parity check coding [12](#low-density-parity-check-coding)

5.3 Channel coding [14](#channel-coding)

5.3.1 Polar coding [15](#polar-coding-1)

5.3.1.1 Interleaving [15](#interleaving)

5.3.1.2 Polar encoding [16](#polar-encoding)

5.3.2 Low density parity check coding [19](#low-density-parity-check-coding-1)

5.3.3 Channel coding of small block lengths [24](#channel-coding-of-small-block-lengths)

5.3.3.1 Encoding of 1-bit information [24](#encoding-of-1-bit-information)

5.3.3.2 Encoding of 2-bit information [25](#encoding-of-2-bit-information)

5.3.3.3 Encoding of other small block lengths [25](#encoding-of-other-small-block-lengths)

5.4 Rate matching [26](#rate-matching)

5.4.1 Rate matching for Polar code [26](#rate-matching-for-polar-code)

5.4.1.1 Sub-block interleaving [26](#sub-block-interleaving)

5.4.1.2 Bit selection [27](#bit-selection)

5.4.1.3 Interleaving of coded bits [28](#interleaving-of-coded-bits)

5.4.2 Rate matching for LDPC code [29](#rate-matching-for-ldpc-code)

5.4.2.1 Bit selection [29](#bit-selection-1)

5.4.2.2 Bit interleaving [32](#bit-interleaving)

5.4.3 Rate matching for channel coding of small block lengths [33](#rate-matching-for-channel-coding-of-small-block-lengths)

5.5 Code block concatenation [33](#code-block-concatenation)

6 Uplink transport channels and control information [34](#uplink-transport-channels-and-control-information)

6.1 Random access channel [34](#random-access-channel)

6.2 Uplink shared channel [34](#uplink-shared-channel)

6.2.1 Transport block CRC attachment [34](#transport-block-crc-attachment)

6.2.2 LDPC base graph selection [34](#ldpc-base-graph-selection)

6.2.3 Code block segmentation and code block CRC attachment [34](#code-block-segmentation-and-code-block-crc-attachment-1)

6.2.4 Channel coding of UL-SCH [35](#channel-coding-of-ul-sch)

6.2.5 Rate matching [35](#rate-matching-1)

6.2.6 Code block concatenation [35](#code-block-concatenation-1)

6.2.7 Data and control multiplexing [35](#data-and-control-multiplexing)

6.3 Uplink control information [47](#uplink-control-information)

6.3.1 Uplink control information on PUCCH [47](#uplink-control-information-on-pucch)

6.3.1.1 UCI bit sequence generation [47](#uci-bit-sequence-generation)

6.3.1.1.1 HARQ-ACK/SR only [47](#harq-acksr-only)

6.3.1.1.2 CSI only [47](#csi-only)

6.3.1.1.3 HARQ-ACK/SR and CSI [65](#harq-acksr-and-csi)

6.3.1.1.4 UCI with different priority indexes [66](#uci-with-different-priority-indexes)

6.3.1.2 Code block segmentation and CRC attachment [66](#code-block-segmentation-and-crc-attachment)

6.3.1.2.1 UCI encoded by Polar code [66](#uci-encoded-by-polar-code)

6.3.1.2.2 UCI encoded by channel coding of small block lengths [67](#uci-encoded-by-channel-coding-of-small-block-lengths)

6.3.1.3 Channel coding of UCI [67](#channel-coding-of-uci)

6.3.1.3.1 UCI encoded by Polar code [67](#uci-encoded-by-polar-code-1)

6.3.1.3.2 UCI encoded by channel coding of small block lengths [67](#uci-encoded-by-channel-coding-of-small-block-lengths-1)

6.3.1.4 Rate matching [67](#rate-matching-2)

6.3.1.4.1 UCI encoded by Polar code [67](#uci-encoded-by-polar-code-2)

6.3.1.4.2 UCI encoded by channel coding of small block lengths [68](#uci-encoded-by-channel-coding-of-small-block-lengths-2)

6.3.1.4.3 UCI with different priority indexes encoded by Polar code [69](#uci-with-different-priority-indexes-encoded-by-polar-code)

6.3.1.4.4 UCI with different priority indexes encoded by channel coding of small block lengths [69](#uci-with-different-priority-indexes-encoded-by-channel-coding-of-small-block-lengths)

6.3.1.5 Code block concatenation [69](#code-block-concatenation-2)

6.3.1.6 Multiplexing of coded UCI bits to PUCCH [70](#multiplexing-of-coded-uci-bits-to-pucch)

6.3.2 Uplink control information on PUSCH [72](#uplink-control-information-on-pusch)

6.3.2.1 UCI bit sequence generation [72](#uci-bit-sequence-generation-1)

6.3.2.1.1 HARQ-ACK [72](#harq-ack)

6.3.2.1.2 CSI [73](#csi)

6.3.2.1.3 CG-UCI [95](#cg-uci)

6.3.2.1.3A UTO-UCI [96](#a-uto-uci)

6.3.2.1.4 HARQ-ACK and CG-UCI/UTO-UCI [96](#harq-ack-and-cg-uciuto-uci)

6.3.2.1.5 UCI with different priority indexes [97](#uci-with-different-priority-indexes-1)

6.3.2.2 Code block segmentation and CRC attachment [99](#code-block-segmentation-and-crc-attachment-1)

6.3.2.2.1 UCI encoded by Polar code [99](#uci-encoded-by-polar-code-3)

6.3.2.2.2 UCI encoded by channel coding of small block lengths [99](#uci-encoded-by-channel-coding-of-small-block-lengths-3)

6.3.2.3 Channel coding of UCI [99](#channel-coding-of-uci-1)

6.3.2.3.1 UCI encoded by Polar code [99](#uci-encoded-by-polar-code-4)

6.3.2.3.2 UCI encoded by channel coding of small block lengths [99](#uci-encoded-by-channel-coding-of-small-block-lengths-4)

6.3.2.4 Rate matching [99](#rate-matching-3)

6.3.2.4.1 UCI encoded by Polar code [99](#uci-encoded-by-polar-code-5)

6.3.2.4.2 UCI encoded by channel coding of small block lengths [113](#uci-encoded-by-channel-coding-of-small-block-lengths-5)

6.3.2.5 Code block concatenation [116](#code-block-concatenation-3)

6.3.2.6 Multiplexing of coded UCI bits to PUSCH [116](#multiplexing-of-coded-uci-bits-to-pusch)

6.3.2.7 Multiplexing of coded UCI bits with different priority indexes to PUSCH [116](#multiplexing-of-coded-uci-bits-with-different-priority-indexes-to-pusch)

7 Downlink transport channels and control information [117](#downlink-transport-channels-and-control-information)

7.1 Broadcast channel [117](#broadcast-channel)

7.1.1 PBCH payload generation [117](#pbch-payload-generation)

7.1.2 Scrambling [118](#scrambling)

7.1.3 Transport block CRC attachment [119](#transport-block-crc-attachment-1)

7.1.4 Channel coding [119](#channel-coding-1)

7.1.5 Rate matching [120](#rate-matching-4)

7.2 Downlink shared channel and paging channel [120](#downlink-shared-channel-and-paging-channel)

7.2.1 Transport block CRC attachment [120](#transport-block-crc-attachment-2)

7.2.2 LDPC base graph selection [120](#ldpc-base-graph-selection-1)

7.2.3 Code block segmentation and code block CRC attachment [120](#code-block-segmentation-and-code-block-crc-attachment-2)

7.2.4 Channel coding [120](#channel-coding-2)

7.2.5 Rate matching [121](#rate-matching-5)

7.2.6 Code block concatenation [121](#code-block-concatenation-4)

7.3 Downlink control information [121](#downlink-control-information)

7.3.1 DCI formats [121](#dci-formats)

7.3.1.0 DCI size alignment [123](#dci-size-alignment)

7.3.1.0.1 DCI size alignment for DCI formats for scheduling of sidelink [126](#dci-size-alignment-for-dci-formats-for-scheduling-of-sidelink)

7.3.1.1 DCI formats for scheduling of PUSCH [126](#dci-formats-for-scheduling-of-pusch)

7.3.1.1.1 Format 0_0 [126](#format-0_0)

7.3.1.1.2 Format 0_1 [130](#format-0_1)

7.3.1.1.3 Format 0_2 [201](#format-0_2)

7.3.1.1.4 Format 0_3 [214](#format-0_3)

7.3.1.2 DCI formats for scheduling of PDSCH [225](#dci-formats-for-scheduling-of-pdsch)

7.3.1.2.1 Format 1_0 [225](#format-1_0)

7.3.1.2.2 Format 1_1 [229](#format-1_1)

7.3.1.2.3 Format 1_2 [256](#format-1_2)

7.3.1.2.4 Format 1_3 [261](#format-1_3)

7.3.1.3 DCI formats for other purposes [270](#dci-formats-for-other-purposes)

7.3.1.3.1 Format 2_0 [270](#format-2_0)

7.3.1.3.2 Format 2_1 [270](#format-2_1)

7.3.1.3.3 Format 2_2 [270](#format-2_2)

7.3.1.3.4 Format 2_3 [271](#format-2_3)

7.3.1.3.5 Format 2_4 [272](#format-2_4)

7.3.1.3.6 Format 2_5 [272](#format-2_5)

7.3.1.3.7 Format 2_6 [272](#format-2_6)

7.3.1.3.8 Format 2_7 [272](#format-2_7)

7.3.1.3.9 Format 2_8 [273](#format-2_8)

7.3.1.3.10 Format 2_9 [273](#format-2_9)

7.3.1.4 DCI formats for scheduling of sidelink [274](#dci-formats-for-scheduling-of-sidelink)

7.3.1.4.1 Format 3_0 [274](#format-3_0)

7.3.1.4.2 Format 3_1 [275](#format-3_1)

7.3.1.4.3 Format 3_2 [275](#format-3_2)

7.3.1.5 DCI formats for scheduling of MBS [276](#dci-formats-for-scheduling-of-mbs)

7.3.1.5.1 Format 4_0 [276](#format-4_0)

7.3.1.5.2 Format 4_1 [276](#format-4_1)

7.3.1.5.3 Format 4_2 [277](#format-4_2)

7.3.2 CRC attachment [279](#crc-attachment)

7.3.3 Channel coding [279](#channel-coding-3)

7.3.4 Rate matching [279](#rate-matching-6)

8 Sidelink transport channels and control information [279](#sidelink-transport-channels-and-control-information)

8.1 Sidelink broadcast channel [279](#sidelink-broadcast-channel)

8.1.1 Void [280](#void)

8.2 Sidelink shared channel [280](#sidelink-shared-channel)

8.2.1 Data and control multiplexing [280](#data-and-control-multiplexing-1)

8.3 Sidelink control information on PSCCH [281](#sidelink-control-information-on-pscch)

8.3.1 1<sup>st</sup>-stage SCI formats [281](#st-stage-sci-formats)

8.3.1.1 SCI format 1-A [281](#sci-format-1-a)

8.3.1.2 SCI format 1-B [283](#sci-format-1-b)

8.3.2 CRC attachment [284](#crc-attachment-1)

8.3.3 Channel coding [284](#channel-coding-4)

8.3.4 Rate Matching [284](#rate-matching-7)

8.4 Sidelink control information on PSSCH [284](#sidelink-control-information-on-pssch)

8.4.1 2<sup>nd</sup>-stage SCI formats [284](#nd-stage-sci-formats)

8.4.1.1 SCI format 2-A [284](#sci-format-2-a)

8.4.1.2 SCI format 2-B [285](#sci-format-2-b)

8.4.1.3 SCI format 2-C [286](#sci-format-2-c)

8.4.1.4 SCI format 2-D [287](#sci-format-2-d)

8.4.2 CRC attachment [288](#crc-attachment-2)

8.4.3 Channel coding [288](#channel-coding-5)

8.4.4 Rate Matching [288](#rate-matching-8)

8.4.5 Multiplexing of coded 2<sup>nd</sup>-stage SCI bits to PSSCH [289](#multiplexing-of-coded-2nd-stage-sci-bits-to-pssch)

Annex A (informative): Change history [290](#annex-a-informative-change-history)

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
