3GPP TS 38.323 V18.5.0 (2025-03)

Technical Specification

3rd Generation Partnership Project;

Technical Specification Group Radio Access Network;

NR;

Packet Data Convergence Protocol (PDCP) specification

(Release 18)

[figure] [figure]

The present document has been developed within the 3rd Generation Partnership Project (3GPP <sup>TM</sup>) and may be further elaborated for the purposes of 3GPP.  
The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented.  
This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification.  
Specifications and Reports for implementation of the 3GPP <sup>TM</sup> system should be obtained via the 3GPP Organizational Partners' Publications Offices.

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

© 2025, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC).

All rights reserved.

UMTS™ is a Trade Mark of ETSI registered for the benefit of its members

3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners  
LTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners

GSM® and the GSM logo are registered and owned by the GSM Association

#  Contents

Foreword [6](#foreword)

1 Scope [7](#scope)

2 References [7](#references)

3 Definitions and abbreviations [8](#definitions-and-abbreviations)

3.1 Definitions [8](#definitions)

3.2 Abbreviations [9](#abbreviations)

4 General [10](#general)

4.1 Introduction [10](#introduction)

4.2 Architecture [10](#architecture)

4.2.1 PDCP structure [10](#pdcp-structure)

4.2.2 PDCP entities [13](#pdcp-entities)

4.3 Services [14](#services)

4.3.1 Services provided to upper layers [14](#services-provided-to-upper-layers)

4.3.2 Services expected from lower layers [14](#services-expected-from-lower-layers)

4.4 Functions [15](#functions)

5 Procedures [15](#procedures)

5.1 PDCP entity handling [15](#pdcp-entity-handling)

5.1.1 PDCP entity establishment [15](#pdcp-entity-establishment)

5.1.2 PDCP entity re-establishment [15](#pdcp-entity-re-establishment)

5.1.3 PDCP entity release [17](#pdcp-entity-release)

5.1.4 PDCP entity suspend [17](#pdcp-entity-suspend)

5.1.5 PDCP entity reconfiguration [18](#pdcp-entity-reconfiguration)

5.2 Data transfer [18](#data-transfer)

5.2.1 Transmit operation [18](#transmit-operation)

5.2.2 Receive operation [20](#receive-operation)

5.2.2.1 Actions when a PDCP Data PDU is received from lower layers [20](#actions-when-a-pdcp-data-pdu-is-received-from-lower-layers)

5.2.2.2 Actions when a *t-Reordering* expires [22](#actions-when-a-t-reordering-expires)

5.2.2.3 Actions when the value of *t-Reordering* is reconfigured [22](#actions-when-the-value-of-t-reordering-is-reconfigured)

5.2.3 Sidelink transmit operation [22](#sidelink-transmit-operation)

5.2.4 Sidelink receive operation [22](#sidelink-receive-operation)

5.3 SDU discard [23](#sdu-discard)

5.4 Status reporting [23](#status-reporting)

5.4.1 Transmit operation [23](#transmit-operation-1)

5.4.2 Receive operation [24](#receive-operation-1)

5.5 Data recovery [24](#data-recovery)

5.6 Data volume calculation [24](#data-volume-calculation)

5.7 Robust header compression and decompression [26](#robust-header-compression-and-decompression)

5.7.1 Supported header compression protocols and profiles [26](#supported-header-compression-protocols-and-profiles)

5.7.2 Configuration of ROHC [26](#configuration-of-rohc)

5.7.3 Protocol parameters [26](#protocol-parameters)

5.7.4 Header compression using ROHC [27](#header-compression-using-rohc)

5.7.5 Header decompression using ROHC [27](#header-decompression-using-rohc)

5.7.6 PDCP Control PDU for interspersed ROHC feedback [27](#pdcp-control-pdu-for-interspersed-rohc-feedback)

5.7.6.1 Transmit Operation [27](#transmit-operation-2)

5.7.6.2 Receive Operation [28](#receive-operation-2)

5.8 Ciphering and deciphering [28](#ciphering-and-deciphering)

5.9 Integrity protection and verification [28](#integrity-protection-and-verification)

5.10 Handling of unknown, unforeseen, and erroneous protocol data [29](#handling-of-unknown-unforeseen-and-erroneous-protocol-data)

5.11 PDCP duplication [30](#pdcp-duplication)

5.11.1 Activation/Deactivation of PDCP duplication [30](#activationdeactivation-of-pdcp-duplication)

5.11.2 Duplicate PDU discard [30](#duplicate-pdu-discard)

5.12 Ethernet header compression and decompression [31](#ethernet-header-compression-and-decompression)

5.12.1 Supported header compression protocols [31](#supported-header-compression-protocols)

5.12.2 Configuration of EHC [31](#configuration-of-ehc)

5.12.3 Protocol parameters [31](#protocol-parameters-1)

5.12.4 Header compression using EHC [31](#header-compression-using-ehc)

5.12.5 Header decompression using EHC [31](#header-decompression-using-ehc)

5.12.6 PDCP Control PDU for EHC feedback [31](#pdcp-control-pdu-for-ehc-feedback)

5.12.6.1 Transmit Operation [31](#transmit-operation-3)

5.12.6.2 Receive Operation [31](#receive-operation-3)

5.12.7 Simultaneous configuration of ROHC and EHC [32](#simultaneous-configuration-of-rohc-and-ehc)

5.13 Uplink data switching [32](#uplink-data-switching)

5.14 Uplink Data compression and decompression [33](#uplink-data-compression-and-decompression)

5.14.1 UDC protocol [33](#udc-protocol)

5.14.2 Configuration of UDC [33](#configuration-of-udc)

5.14.3 UDC header [33](#udc-header)

5.14.4 Uplink data compression [33](#uplink-data-compression)

5.14.5 PDCP Control PDU for UDC feedback [33](#pdcp-control-pdu-for-udc-feedback)

5.14.6 Pre-defined dictionary [34](#pre-defined-dictionary)

5.14.7 UDC buffer reset procedure [34](#udc-buffer-reset-procedure)

5.14.8 UDC checksum error handling [34](#udc-checksum-error-handling)

5.15 Data volume calculation for delay status reporting [34](#data-volume-calculation-for-delay-status-reporting)

5.16 SN gap report [35](#sn-gap-report)

5.16.1 Transmit operation [35](#transmit-operation-4)

5.16.2 Receive operation [35](#receive-operation-4)

6 Protocol data units, formats, and parameters [36](#protocol-data-units-formats-and-parameters)

6.1 Protocol data units [36](#protocol-data-units)

6.1.1 Data PDU [36](#data-pdu)

6.1.2 Control PDU [36](#control-pdu)

6.2 Formats [37](#formats)

6.2.1 General [37](#general-1)

6.2.2 Data PDU [37](#data-pdu-1)

6.2.2.1 Data PDU for SRBs [37](#data-pdu-for-srbs)

6.2.2.2 Data PDU for DRBs and MRBs with 12 bits PDCP SN [37](#data-pdu-for-drbs-and-mrbs-with-12-bits-pdcp-sn)

6.2.2.3 Data PDU for DRBs and MRBs with 18 bits PDCP SN [38](#data-pdu-for-drbs-and-mrbs-with-18-bits-pdcp-sn)

6.2.2.4 Data PDU for sidelink DRBs for groupcast and broadcast, for the sidelink SRB0‎ and for the sidelink SRB4 [38](#data-pdu-for-sidelink-drbs-for-groupcast-and-broadcast-for-the-sidelink-srb0-and-for-the-sidelink-srb4)

6.2.2.5 Data PDU for sidelink SRBs for unicast [39](#data-pdu-for-sidelink-srbs-for-unicast)

6.2.2.6 Data PDU for sidelink DRBs for unicast with 12 bits PDCP SN [39](#data-pdu-for-sidelink-drbs-for-unicast-with-12-bits-pdcp-sn)

6.2.2.7 Data PDU for sidelink DRBs for unicast with 18 bits PDCP SN [40](#data-pdu-for-sidelink-drbs-for-unicast-with-18-bits-pdcp-sn)

6.2.3 Control PDU [41](#control-pdu-1)

6.2.3.1 Control PDU for PDCP status report [41](#control-pdu-for-pdcp-status-report)

6.2.3.2 Control PDU for interspersed ROHC feedback [42](#control-pdu-for-interspersed-rohc-feedback)

6.2.3.3 Control PDU for EHC feedback [42](#control-pdu-for-ehc-feedback)

6.2.3.4 Control PDU for UDC feedback [42](#control-pdu-for-udc-feedback)

6.2.3.5 Control PDU for PDCP SN gap report [42](#control-pdu-for-pdcp-sn-gap-report)

6.3 Parameters [43](#parameters)

6.3.1 General [43](#general-2)

6.3.2 PDCP SN [43](#pdcp-sn)

6.3.3 Data [43](#data)

6.3.4 MAC-I [44](#mac-i)

6.3.5 COUNT [44](#count)

6.3.6 R [44](#r)

6.3.7 D/C [44](#dc)

6.3.8 PDU type [44](#pdu-type)

6.3.9 FMC [45](#fmc)

6.3.10 Bitmap [45](#bitmap)

6.3.11 Interspersed ROHC feedback [45](#interspersed-rohc-feedback)

6.3.12 SDU Type [45](#sdu-type)

6.3.13 K<sub>NRP-sess</sub> ID [45](#knrp-sess-id)

6.3.14 FE [46](#fe)

6.3.15 FDC [46](#fdc)

6.3.16 Discard Bitmap [46](#discard-bitmap)

7 State variables, constants, and timers [46](#state-variables-constants-and-timers)

7.1 State variables [46](#state-variables)

7.2 Constants [47](#constants)

7.3 Timers [47](#timers)

Annex A (normative): Ethernet Header Compression (EHC) protocol [48](#annex-a-normative-ethernet-header-compression-ehc-protocol)

A.1 EHC principle [48](#a.1-ehc-principle)

A.2 EHC packet format and parameters [49](#a.2-ehc-packet-format-and-parameters)

A.2.1 EHC packet format [49](#a.2.1-ehc-packet-format)

A.2.1.1 EHC Full Header packet and EHC Compressed Header packet [49](#a.2.1.1-ehc-full-header-packet-and-ehc-compressed-header-packet)

A.2.1.2 EHC feedback packet [50](#a.2.1.2-ehc-feedback-packet)

A.2.2 Parameters [51](#a.2.2-parameters)

A.2.2.1 F/C [51](#a.2.2.1-fc)

A.2.2.2 CID [51](#a.2.2.2-cid)

Annex B (normative): Uplink Data Compression Protocol [51](#annex-b-normative-uplink-data-compression-protocol)

B.1 UDC general description [51](#b.1-udc-general-description)

B.2 UDC packet format and parameters [51](#b.2-udc-packet-format-and-parameters)

B.2.1 UDC Header and UDC Data Block format [51](#b.2.1-udc-header-and-udc-data-block-format)

B.2.2 UDC parameters [52](#b.2.2-udc-parameters)

B.2.2.1 FU [52](#b.2.2.1-fu)

B.2.2.2 FR [52](#b.2.2.2-fr)

B.2.2.3 Checksum [52](#b.2.2.3-checksum)

B.2.3 An example of UDC Checksum calculation [52](#b.2.3-an-example-of-udc-checksum-calculation)

Annex C (informative): Change history [53](#annex-c-informative-change-history)

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
