3GPP TS 38.211 V18.10.0 (2026-09)

Technical Specification

3rd Generation Partnership Project;

Technical Specification Group Radio Access Network;

NR;

Physical channels and modulation

(Release 18)

[figure] <img src="media/image2.png" style="width:1.78125in;height:1.04167in" alt="3GPP-logo_web" />

The present document has been developed within the 3rd Generation Partnership Project (3GPP <sup>TM</sup>) and may be further elaborated for the purposes of 3GPP..  
The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented.  
This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification.  
Specifications and Reports for implementation of the 3GPP <sup>TM</sup> system should be obtained via the 3GPP Organizational Partners' Publications Offices.

> Keywords
>
> New Radio, Layer 1
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

Foreword [8](#foreword)

1 Scope [9](#scope)

2 References [9](#references)

3 Definitions of terms, symbols and abbreviations [9](#definitions-of-terms-symbols-and-abbreviations)

3.1 Terms [9](#terms)

3.2 Symbols [9](#symbols)

3.3 Abbreviations [11](#abbreviations)

4 Frame structure and physical resources [11](#frame-structure-and-physical-resources)

4.1 General [11](#general)

4.2 Numerologies [12](#numerologies)

4.3 Frame structure [12](#frame-structure)

4.3.1 Frames and subframes [12](#frames-and-subframes)

4.3.2 Slots [13](#slots)

4.4 Physical resources [14](#physical-resources)

4.4.1 Antenna ports [14](#antenna-ports)

4.4.2 Resource grid [14](#resource-grid)

4.4.3 Resource elements [14](#resource-elements)

4.4.4 Resource blocks [14](#resource-blocks)

4.4.4.1 General [14](#general-1)

4.4.4.2 Point A [15](#point-a)

4.4.4.3 Common resource blocks [15](#common-resource-blocks)

4.4.4.4 Physical resource blocks [15](#physical-resource-blocks)

4.4.4.5 Virtual resource blocks [15](#virtual-resource-blocks)

4.4.4.6 Interlaced resource blocks [15](#interlaced-resource-blocks)

4.4.5 Bandwidth part [16](#bandwidth-part)

4.4.6 Common MBS frequency resource [16](#common-mbs-frequency-resource)

4.5 Carrier aggregation [16](#carrier-aggregation)

5 Generic functions [17](#generic-functions)

5.1 Modulation mapper [17](#modulation-mapper)

5.1.1 π/2-BPSK [17](#π2-bpsk)

5.1.2 BPSK [17](#bpsk)

5.1.3 QPSK [17](#qpsk)

5.1.4 16QAM [17](#qam)

5.1.5 64QAM [17](#qam-1)

5.1.6 256QAM [17](#qam-2)

5.1.7 1024QAM [18](#qam-3)

5.2 Sequence generation [18](#sequence-generation)

5.2.1 Pseudo-random sequence generation [18](#pseudo-random-sequence-generation)

5.2.2 Low-PAPR sequence generation type 1 [18](#low-papr-sequence-generation-type-1)

5.2.2.1 Base sequences of length 36 or larger [18](#base-sequences-of-length-36-or-larger)

5.2.2.2 Base sequences of length less than 36 [19](#base-sequences-of-length-less-than-36)

5.2.3 Low-PAPR sequence generation type 2 [22](#low-papr-sequence-generation-type-2)

5.2.3.1 Sequences of length 30 or larger [22](#sequences-of-length-30-or-larger)

5.2.3.2 Sequences of length less than 30 [22](#sequences-of-length-less-than-30)

5.3 OFDM baseband signal generation [26](#ofdm-baseband-signal-generation)

5.3.1 OFDM baseband signal generation for all channels except PRACH and RIM-RS [26](#ofdm-baseband-signal-generation-for-all-channels-except-prach-and-rim-rs)

5.3.2 OFDM baseband signal generation for PRACH [28](#ofdm-baseband-signal-generation-for-prach)

5.3.3 OFDM baseband signal generation for RIM-RS [30](#ofdm-baseband-signal-generation-for-rim-rs)

5.4 Modulation and upconversion [30](#modulation-and-upconversion)

6 Uplink [31](#uplink)

6.1 Overview [31](#overview)

6.1.1 Overview of physical channels [31](#overview-of-physical-channels)

6.1.2 Overview of physical signals [31](#overview-of-physical-signals)

6.2 Physical resources [31](#physical-resources-1)

6.3 Physical channels [32](#physical-channels)

6.3.1 Physical uplink shared channel [32](#physical-uplink-shared-channel)

6.3.1.1 Scrambling [32](#scrambling)

6.3.1.2 Modulation [33](#modulation)

6.3.1.3 Layer mapping [33](#layer-mapping)

6.3.1.4 Transform precoding [33](#transform-precoding)

6.3.1.5 Precoding [34](#precoding)

6.3.1.6 Mapping to virtual resource blocks [59](#mapping-to-virtual-resource-blocks)

6.3.1.7 Mapping from virtual to physical resource blocks [60](#mapping-from-virtual-to-physical-resource-blocks)

6.3.2 Physical uplink control channel [60](#physical-uplink-control-channel)

6.3.2.1 General [60](#general-2)

6.3.2.2 Sequence and cyclic shift hopping [60](#sequence-and-cyclic-shift-hopping)

6.3.2.2.1 Group and sequence hopping [60](#group-and-sequence-hopping)

6.3.2.2.2 Cyclic shift hopping [61](#cyclic-shift-hopping)

6.3.2.3 PUCCH format 0 [62](#pucch-format-0)

6.3.2.3.1 Sequence generation [62](#sequence-generation-1)

6.3.2.3.2 Mapping to physical resources [62](#mapping-to-physical-resources)

6.3.2.4 PUCCH format 1 [62](#pucch-format-1)

6.3.2.4.1 Sequence modulation [62](#sequence-modulation)

6.3.2.4.2 Mapping to physical resources [63](#mapping-to-physical-resources-1)

6.3.2.5 PUCCH format 2 [64](#pucch-format-2)

6.3.2.5.1 Scrambling [64](#scrambling-1)

6.3.2.5.2 Modulation [64](#modulation-1)

6.3.2.5.2A Spreading [64](#a-spreading)

6.3.2.5.3 Mapping to physical resources [65](#mapping-to-physical-resources-2)

6.3.2.6 PUCCH formats 3 and 4 [65](#pucch-formats-3-and-4)

6.3.2.6.1 Scrambling [65](#scrambling-2)

6.3.2.6.2 Modulation [66](#modulation-2)

6.3.2.6.3 Block-wise spreading [66](#block-wise-spreading)

6.3.2.6.4 Transform precoding [67](#transform-precoding-1)

6.3.2.6.5 Mapping to physical resources [67](#mapping-to-physical-resources-3)

6.3.3 Physical random-access channel [67](#physical-random-access-channel)

6.3.3.1 Sequence generation [67](#sequence-generation-2)

6.3.3.2 Mapping to physical resources [74](#mapping-to-physical-resources-4)

6.4 Physical signals [94](#physical-signals)

6.4.1 Reference signals [94](#reference-signals)

6.4.1.1 Demodulation reference signal for PUSCH [94](#demodulation-reference-signal-for-pusch)

6.4.1.1.1 Sequence generation [94](#sequence-generation-3)

6.4.1.1.2 (void) [96](#void)

6.4.1.1.3 Precoding and mapping to physical resources [96](#precoding-and-mapping-to-physical-resources)

6.4.1.2 Phase-tracking reference signals for PUSCH [101](#phase-tracking-reference-signals-for-pusch)

6.4.1.2.1 Sequence generation [101](#sequence-generation-4)

6.4.1.2.1.1 Sequence generation if transform precoding is not enabled [101](#sequence-generation-if-transform-precoding-is-not-enabled)

6.4.1.2.1.2 Sequence generation if transform precoding is enabled [101](#sequence-generation-if-transform-precoding-is-enabled)

6.4.1.2.2 Mapping to physical resources [102](#mapping-to-physical-resources-5)

6.4.1.2.2.1 Precoding and mapping to physical resources if transform precoding is not enabled [102](#precoding-and-mapping-to-physical-resources-if-transform-precoding-is-not-enabled)

6.4.1.2.2.2 Mapping to physical resources if transform precoding is enabled [104](#mapping-to-physical-resources-if-transform-precoding-is-enabled)

6.4.1.3 Demodulation reference signal for PUCCH [105](#demodulation-reference-signal-for-pucch)

6.4.1.3.1 Demodulation reference signal for PUCCH format 1 [105](#demodulation-reference-signal-for-pucch-format-1)

6.4.1.3.1.1 Sequence generation [105](#sequence-generation-5)

6.4.1.3.1.2 Mapping to physical resources [106](#mapping-to-physical-resources-6)

6.4.1.3.2 Demodulation reference signal for PUCCH format 2 [106](#demodulation-reference-signal-for-pucch-format-2)

6.4.1.3.2.1 Sequence generation [106](#sequence-generation-6)

6.4.1.3.2.2 Mapping to physical resources [107](#mapping-to-physical-resources-7)

6.4.1.3.3 Demodulation reference signal for PUCCH formats 3 and 4 [107](#demodulation-reference-signal-for-pucch-formats-3-and-4)

6.4.1.3.3.1 Sequence generation [107](#sequence-generation-7)

6.4.1.3.3.2 Mapping to physical resources [107](#mapping-to-physical-resources-8)

6.4.1.4 Sounding reference signal [108](#sounding-reference-signal)

6.4.1.4.1 SRS resource [108](#srs-resource)

6.4.1.4.2 Sequence generation [108](#sequence-generation-8)

6.4.1.4.3 Mapping to physical resources [110](#mapping-to-physical-resources-9)

6.4.1.4.4 Sounding reference signal slot configuration [116](#sounding-reference-signal-slot-configuration)

7 Downlink [116](#downlink)

7.1 Overview [116](#overview-1)

7.1.1 Overview of physical channels [116](#overview-of-physical-channels-1)

7.1.2 Overview of physical signals [117](#overview-of-physical-signals-1)

7.2 Physical resources [117](#physical-resources-2)

7.3 Physical channels [117](#physical-channels-1)

7.3.1 Physical downlink shared channel [117](#physical-downlink-shared-channel)

7.3.1.1 Scrambling [117](#scrambling-3)

7.3.1.2 Modulation [118](#modulation-3)

7.3.1.3 Layer mapping [119](#layer-mapping-1)

7.3.1.4 Antenna port mapping [120](#antenna-port-mapping)

7.3.1.5 Mapping to virtual resource blocks [120](#mapping-to-virtual-resource-blocks-1)

7.3.1.6 Mapping from virtual to physical resource blocks [120](#mapping-from-virtual-to-physical-resource-blocks-1)

7.3.2 Physical downlink control channel (PDCCH) [122](#physical-downlink-control-channel-pdcch)

7.3.2.1 Control-channel element (CCE) [122](#control-channel-element-cce)

7.3.2.2 Control-resource set (CORESET) [122](#control-resource-set-coreset)

7.3.2.3 Scrambling [124](#scrambling-4)

7.3.2.4 PDCCH modulation [124](#pdcch-modulation)

7.3.2.5 Mapping to physical resources [124](#mapping-to-physical-resources-10)

7.3.3 Physical broadcast channel [125](#physical-broadcast-channel)

7.3.3.1 Scrambling [125](#scrambling-5)

7.3.3.2 Modulation [125](#modulation-4)

7.3.3.3 Mapping to physical resources [125](#mapping-to-physical-resources-11)

7.4 Physical signals [125](#physical-signals-1)

7.4.1 Reference signals [125](#reference-signals-1)

7.4.1.1 Demodulation reference signals for PDSCH [125](#demodulation-reference-signals-for-pdsch)

7.4.1.1.1 Sequence generation [125](#sequence-generation-9)

7.4.1.1.2 Mapping to physical resources [126](#mapping-to-physical-resources-12)

7.4.1.2 Phase-tracking reference signals for PDSCH [130](#phase-tracking-reference-signals-for-pdsch)

7.4.1.2.1 Sequence generation [130](#sequence-generation-10)

7.4.1.2.2 Mapping to physical resources [130](#mapping-to-physical-resources-13)

7.4.1.3 Demodulation reference signals for PDCCH [132](#demodulation-reference-signals-for-pdcch)

7.4.1.3.1 Sequence generation [132](#sequence-generation-11)

7.4.1.3.2 Mapping to physical resources [132](#mapping-to-physical-resources-14)

7.4.1.4 Demodulation reference signals for PBCH [133](#demodulation-reference-signals-for-pbch)

7.4.1.4.1 Sequence generation [133](#sequence-generation-12)

7.4.1.4.2 Mapping to physical resources [133](#mapping-to-physical-resources-15)

7.4.1.5 CSI reference signals [133](#csi-reference-signals)

7.4.1.5.1 General [133](#general-3)

7.4.1.5.2 Sequence generation [134](#sequence-generation-13)

7.4.1.5.3 Mapping to physical resources [134](#mapping-to-physical-resources-16)

7.4.1.6 RIM reference signals [137](#rim-reference-signals)

7.4.1.6.1 General [137](#general-4)

7.4.1.6.2 Sequence generation [137](#sequence-generation-14)

7.4.1.6.3 Mapping to physical resources [138](#mapping-to-physical-resources-17)

7.4.1.6.4 RIM-RS configuration [138](#rim-rs-configuration)

7.4.1.6.4.1 General [138](#general-5)

7.4.1.6.4.2 Time-domain parameters and mapping from $i\text{t}$ to time-domain parameters [138](#time-domain-parameters-and-mapping-from-i_textt-to-time-domain-parameters)

7.4.1.6.4.3 Frequency-domain parameters and mapping from $i\text{f}$ to frequency-domain parameters [139](#frequency-domain-parameters-and-mapping-from-i_textf-to-frequency-domain-parameters)

7.4.1.6.4.4 Sequence parameters and mapping from $i\text{s}$ to sequence parameters [140](#sequence-parameters-and-mapping-from-i_texts-to-sequence-parameters)

7.4.1.6.4.5 Mapping between resource triplet and set ID [140](#mapping-between-resource-triplet-and-set-id)

7.4.1.7 Positioning reference signals [141](#positioning-reference-signals)

7.4.1.7.1 General [141](#general-6)

7.4.1.7.2 Sequence generation [141](#sequence-generation-15)

7.4.1.7.3 Mapping to physical resources in a downlink PRS resource [141](#mapping-to-physical-resources-in-a-downlink-prs-resource)

7.4.1.7.4 Mapping to slots in a downlink PRS resource set [142](#mapping-to-slots-in-a-downlink-prs-resource-set)

7.4.2 Synchronization signals [143](#synchronization-signals)

7.4.2.1 Physical-layer cell identities [143](#physical-layer-cell-identities)

7.4.2.2 Primary synchronization signal [143](#primary-synchronization-signal)

7.4.2.2.1 Sequence generation [143](#sequence-generation-16)

7.4.2.2.2 Mapping to physical resources [143](#mapping-to-physical-resources-18)

7.4.2.3 Secondary synchronization signal [143](#secondary-synchronization-signal)

7.4.2.3.1 Sequence generation [143](#sequence-generation-17)

7.4.2.3.2 Mapping to physical resources [143](#mapping-to-physical-resources-19)

7.4.3 SS/PBCH block [144](#sspbch-block)

7.4.3.1 Time-frequency structure of an SS/PBCH block [144](#time-frequency-structure-of-an-sspbch-block)

7.4.3.1.1 Mapping of PSS within an SS/PBCH block [145](#mapping-of-pss-within-an-sspbch-block)

7.4.3.1.2 Mapping of SSS within an SS/PBCH block [145](#mapping-of-sss-within-an-sspbch-block)

7.4.3.1.3 Mapping of PBCH and DM-RS within an SS/PBCH block [145](#mapping-of-pbch-and-dm-rs-within-an-sspbch-block)

7.4.3.2 Time location of an SS/PBCH block [145](#time-location-of-an-sspbch-block)

8 Sidelink [146](#sidelink)

8.1 Overview [146](#overview-2)

8.1.1 Overview of physical channels [146](#overview-of-physical-channels-2)

8.1.2 Overview of physical signals [146](#overview-of-physical-signals-2)

8.2 Physical resources [146](#physical-resources-3)

8.2.1 General [146](#general-7)

8.2.2 Numerologies [146](#numerologies-1)

8.2.3 Frame structure [147](#frame-structure-1)

8.2.3.1 Frames and subframes [147](#frames-and-subframes-1)

8.2.3.2 Slots [147](#slots-1)

8.2.4 Antenna ports [147](#_Toc219310449)

8.2.5 Resource grid [147](#resource-grid-1)

8.2.6 Resource elements [148](#resource-elements-1)

8.2.7 Resource blocks [148](#_Toc219310452)

8.2.8 Bandwidth part [148](#bandwidth-part-1)

8.3 Physical channels [148](#physical-channels-2)

8.3.1 Physical sidelink shared channel [148](#physical-sidelink-shared-channel)

8.3.1.1 Scrambling [148](#scrambling-6)

8.3.1.2 Modulation [149](#modulation-5)

8.3.1.3 Layer mapping [149](#layer-mapping-2)

8.3.1.4 Precoding [149](#precoding-1)

8.3.1.5 Mapping to virtual resource blocks [149](#mapping-to-virtual-resource-blocks-2)

8.3.1.6 Mapping from virtual to physical resource blocks [150](#mapping-from-virtual-to-physical-resource-blocks-2)

8.3.2 Physical sidelink control channel [150](#physical-sidelink-control-channel)

8.3.2.1 Scrambling [150](#scrambling-7)

8.3.2.2 Modulation [150](#modulation-6)

8.3.2.3 Mapping to physical resources [150](#mapping-to-physical-resources-20)

8.3.3 Physical sidelink broadcast channel [150](#physical-sidelink-broadcast-channel)

8.3.3.1 Scrambling [150](#scrambling-8)

8.3.3.2 Modulation [151](#modulation-7)

8.3.3.3 Mapping to physical resources [151](#mapping-to-physical-resources-21)

8.3.4 Physical sidelink feedback channel [151](#physical-sidelink-feedback-channel)

8.3.4.1 General [151](#general-8)

8.3.4.2 PSFCH format 0 [151](#psfch-format-0)

8.3.4.2.1 Sequence generation [151](#sequence-generation-18)

8.3.4.2.2 Mapping to physical resources [151](#mapping-to-physical-resources-22)

8.4 Physical signals [152](#physical-signals-2)

8.4.1 Reference signals [152](#reference-signals-2)

8.4.1.1 Demodulation reference signals for PSSCH [152](#demodulation-reference-signals-for-pssch)

8.4.1.1.1 Sequence generation [152](#sequence-generation-19)

8.4.1.1.2 Mapping to physical resources [152](#mapping-to-physical-resources-23)

8.4.1.2 Phase-tracking reference signals for PSSCH [153](#phase-tracking-reference-signals-for-pssch)

8.4.1.2.1 Sequence generation [153](#sequence-generation-20)

8.4.1.2.2 Mapping to physical resources [153](#mapping-to-physical-resources-24)

8.4.1.3 Demodulation reference signals for PSCCH [154](#demodulation-reference-signals-for-pscch)

8.4.1.3.1 Sequence generation [154](#sequence-generation-21)

8.4.1.3.2 Mapping to physical resources [155](#mapping-to-physical-resources-25)

8.4.1.4 Demodulation reference signals for PSBCH [155](#demodulation-reference-signals-for-psbch)

8.4.1.4.1 Sequence generation [155](#sequence-generation-22)

8.4.1.4.2 Mapping to physical resources [155](#mapping-to-physical-resources-26)

8.4.1.5 CSI reference signals [156](#csi-reference-signals-1)

8.4.1.5.1 General [156](#general-9)

8.4.1.5.2 Sequence generation [156](#sequence-generation-23)

8.4.1.5.3 Mapping to physical resources [156](#mapping-to-physical-resources-27)

8.4.1.6 Positioning reference signals [156](#positioning-reference-signals-1)

8.4.1.6.1 General [156](#general-10)

8.4.1.6.2 Sequence generation [156](#sequence-generation-24)

8.4.1.6.3 Mapping to physical resources [157](#mapping-to-physical-resources-28)

8.4.2 Synchronization signals [158](#synchronization-signals-1)

8.4.2.1 Physical-layer sidelink synchronization identities [158](#physical-layer-sidelink-synchronization-identities)

8.4.2.2 Sidelink primary synchronization signal [158](#sidelink-primary-synchronization-signal)

8.4.2.2.1 Sequence generation [158](#sequence-generation-25)

8.4.2.2.2 Mapping to physical resources [158](#mapping-to-physical-resources-29)

8.4.2.3 Sidelink secondary synchronization signal [158](#sidelink-secondary-synchronization-signal)

8.4.2.3.1 Sequence generation [158](#sequence-generation-26)

8.4.2.3.2 Mapping to physical resources [158](#mapping-to-physical-resources-30)

8.4.3 S-SS/PSBCH block [159](#s-sspsbch-block)

8.4.3.1 Time-frequency structure of an S-SS/PSBCH block [159](#time-frequency-structure-of-an-s-sspsbch-block)

8.4.3.1.1 Mapping of S-PSS within an S-SS/PSBCH block [159](#mapping-of-s-pss-within-an-s-sspsbch-block)

8.4.3.1.2 Mapping of S-SSS within an S-SS/PSBCH block [159](#mapping-of-s-sss-within-an-s-sspsbch-block)

8.4.3.1.3 Mapping of PSBCH and DM-RS within an S-SS/PSBCH block [159](#mapping-of-psbch-and-dm-rs-within-an-s-sspsbch-block)

8.4.3.2 Time location of an S-SS/PSBCH block [160](#time-location-of-an-s-sspsbch-block)

8.5 Timing [160](#timing)

Annex A (informative): Change history [161](#annex-a-informative-change-history)

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
