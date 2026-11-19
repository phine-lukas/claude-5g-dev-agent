3GPP TS 38.322 V18.2.0 (2024-12)

Technical Specification

3rd Generation Partnership Project;

Technical Specification Group Radio Access Network;

NR;

Radio Link Control (RLC) protocol specification

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

© 2024, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC).

All rights reserved.

UMTS™ is a Trade Mark of ETSI registered for the benefit of its members

3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners  
LTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners

GSM® and the GSM logo are registered and owned by the GSM Association

#  Contents

Foreword [5](#foreword)

1 Scope [6](#scope)

2 References [6](#references)

3 Definitions, symbols and abbreviations [6](#definitions-symbols-and-abbreviations)

3.1 Definitions [6](#definitions)

3.2 Abbreviations [7](#abbreviations)

4 General [7](#general)

4.1 Introduction [7](#introduction)

4.2 RLC architecture [7](#rlc-architecture)

4.2.1 RLC entities [7](#rlc-entities)

4.2.1.1 TM RLC entity [9](#tm-rlc-entity)

4.2.1.1.1 General [9](#general-1)

4.2.1.1.2 Transmitting TM RLC entity [9](#transmitting-tm-rlc-entity)

4.2.1.1.3 Receiving TM RLC entity [9](#receiving-tm-rlc-entity)

4.2.1.2 UM RLC entity [9](#um-rlc-entity)

4.2.1.2.1 General [9](#general-2)

4.2.1.2.2 Transmitting UM RLC entity [10](#transmitting-um-rlc-entity)

4.2.1.2.3 Receiving UM RLC entity [10](#receiving-um-rlc-entity)

4.2.1.3 AM RLC entity [11](#am-rlc-entity)

4.2.1.3.1 General [11](#general-3)

4.2.1.3.2 Transmitting side [11](#transmitting-side)

4.2.1.3.3 Receiving side [12](#receiving-side)

4.3 Services [12](#services)

4.3.1 Services provided to upper layers [12](#services-provided-to-upper-layers)

4.3.2 Services expected from lower layers [12](#services-expected-from-lower-layers)

4.4 Functions [12](#functions)

5 Procedures [13](#procedures)

5.1 RLC entity handling [13](#rlc-entity-handling)

5.1.1 RLC entity establishment [13](#rlc-entity-establishment)

5.1.2 RLC entity re-establishment [13](#rlc-entity-re-establishment)

5.1.3 RLC entity release [13](#rlc-entity-release)

5.2 Data transfer procedures [13](#data-transfer-procedures)

5.2.1 TM data transfer [13](#tm-data-transfer)

5.2.1.1 Transmit operations [13](#transmit-operations)

5.2.1.1.1 General [13](#general-4)

5.2.1.2 Receive operations [14](#receive-operations)

5.2.1.2.1 General [14](#general-5)

5.2.2 UM data transfer [14](#um-data-transfer)

5.2.2.1 Transmit operations [14](#transmit-operations-1)

5.2.2.1.1 General [14](#general-6)

5.2.2.2 Receive operations [14](#receive-operations-1)

5.2.2.2.1 General [14](#general-7)

5.2.2.2.2 Actions when an UMD PDU is received from lower layer [14](#actions-when-an-umd-pdu-is-received-from-lower-layer)

5.2.2.2.3 Actions when an UMD PDU is placed in the reception buffer [15](#actions-when-an-umd-pdu-is-placed-in-the-reception-buffer)

5.2.2.2.4 Actions when t-Reassembly expires [15](#actions-when-t-reassembly-expires)

5.2.3 AM data transfer [16](#am-data-transfer)

5.2.3.1 Transmit operations [16](#transmit-operations-2)

5.2.3.1.1 General [16](#general-8)

5.2.3.2 Receive operations [16](#receive-operations-2)

5.2.3.2.1 General [16](#general-9)

5.2.3.2.2 Actions when an AMD PDU is received from lower layer [17](#actions-when-an-amd-pdu-is-received-from-lower-layer)

5.2.3.2.3 Actions when an AMD PDU is placed in the reception buffer [17](#actions-when-an-amd-pdu-is-placed-in-the-reception-buffer)

5.2.3.2.4 Actions when *t-Reassembly* expires [18](#actions-when-t-reassembly-expires-1)

5.3 ARQ procedures [18](#arq-procedures)

5.3.1 General [18](#general-10)

5.3.2 Retransmission [18](#retransmission)

5.3.3 Polling [19](#polling)

5.3.3.1 General [19](#general-11)

5.3.3.2 Transmission of a AMD PDU [19](#transmission-of-a-amd-pdu)

5.3.3.3 Reception of a STATUS report [20](#reception-of-a-status-report)

5.3.3.4 Expiry of *t-PollRetransmit* [20](#expiry-of-t-pollretransmit)

5.3.4 Status reporting [20](#status-reporting)

5.4 SDU discard procedures [21](#sdu-discard-procedures)

5.5 Data volume calculation [21](#data-volume-calculation)

5.6 Handling of unknown, unforeseen and erroneous protocol data [22](#handling-of-unknown-unforeseen-and-erroneous-protocol-data)

5.6.1 Reception of PDU with reserved or invalid values [22](#reception-of-pdu-with-reserved-or-invalid-values)

6 Protocol data units, formats and parameters [22](#protocol-data-units-formats-and-parameters)

6.1 Protocol data units [22](#protocol-data-units)

6.1.1 General [22](#general-12)

6.1.2 RLC data PDU [22](#rlc-data-pdu)

6.1.3 RLC control PDU [22](#rlc-control-pdu)

6.2 Formats and parameters [22](#formats-and-parameters)

6.2.1 General [22](#general-13)

6.2.2 Formats [23](#formats)

6.2.2.1 General [23](#general-14)

6.2.2.2 TMD PDU [23](#tmd-pdu)

6.2.2.3 UMD PDU [23](#umd-pdu)

6.2.2.4 AMD PDU [24](#amd-pdu)

6.2.2.5 STATUS PDU [25](#status-pdu)

6.2.3 Parameters [27](#parameters)

6.2.3.1 General [27](#general-15)

6.2.3.2 Data field [27](#data-field)

6.2.3.3 Sequence Number (SN) field [27](#sequence-number-sn-field)

6.2.3.4 Segmentation Info (SI) field [27](#segmentation-info-si-field)

6.2.3.5 Segment Offset (SO) field [27](#segment-offset-so-field)

6.2.3.6 Data/Control (D/C) field [28](#datacontrol-dc-field)

6.2.3.7 Polling bit (P) field [28](#polling-bit-p-field)

6.2.3.8 Reserved (R) field [28](#reserved-r-field)

6.2.3.9 Control PDU Type (CPT) field [28](#control-pdu-type-cpt-field)

6.2.3.10 Acknowledgement SN (ACK_SN) field [28](#acknowledgement-sn-ack_sn-field)

6.2.3.11 Extension bit 1 (E1) field [29](#extension-bit-1-e1-field)

6.2.3.12 Negative Acknowledgement SN (NACK_SN) field [29](#negative-acknowledgement-sn-nack_sn-field)

6.2.3.13 Extension bit 2 (E2) field [29](#extension-bit-2-e2-field)

6.2.3.14 SO start (SOstart) field [29](#so-start-sostart-field)

6.2.3.15 SO end (SOend) field [29](#so-end-soend-field)

6.2.3.16 Extension bit 3 (E3) field [30](#extension-bit-3-e3-field)

6.2.3.17 NACK range field [30](#nack-range-field)

7 Variables, constants and timers [30](#variables-constants-and-timers)

7.1 State variables [30](#state-variables)

7.2 Constants [32](#constants)

7.3 Timers [32](#timers)

7.4 Configurable parameters [32](#configurable-parameters)

Annex A (informative): Change history [33](#annex-a-informative-change-history)

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
