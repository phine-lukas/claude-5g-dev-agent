3GPP TS 38.470 V18.5.0 (2025-06)

Technical Specification

3rd Generation Partnership Project;

Technical Specification Group Radio Access Network;

NG-RAN;

F1 general aspects and principles

(Release 18)

[figure] <img src="media/image2.png" style="width:1.77778in;height:1.03681in" />

The present document has been developed within the 3rd Generation Partnership Project (3GPP <sup>TM</sup>) and may be further elaborated for the purposes of 3GPP..  
The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented.  
This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification.  
Specifications and Reports for implementation of the 3GPP <sup>TM</sup> system should be obtained via the 3GPP Organizational Partners' Publications Offices.

> Keywords
>
> NR-RAN
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

© 2025, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC).

All rights reserved.

UMTS™ is a Trade Mark of ETSI registered for the benefit of its members

3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners  
LTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners

GSM® and the GSM logo are registered and owned by the GSM Association

#  Contents

Foreword [5](#foreword)

1 Scope [6](#scope)

2 References [6](#references)

3 Definitions and abbreviations [6](#definitions-and-abbreviations)

3.1 Definitions [6](#definitions)

3.2 Abbreviations [7](#abbreviations)

4 General aspects [8](#general-aspects)

4.1 F1 interface general principles [8](#f1-interface-general-principles)

4.2 F1 interface specification objectives [9](#f1-interface-specification-objectives)

4.3 F1 interface capabilities [9](#f1-interface-capabilities)

4.4 Void [9](#void)

5 Functions of the F1 interface [9](#functions-of-the-f1-interface)

5.1 General [9](#general)

5.2 F1-C functions [9](#f1-c-functions)

5.2.1 F1 interface management function [9](#f1-interface-management-function)

5.2.2 System Information management function [10](#system-information-management-function)

5.2.3 F1 UE context management function [10](#f1-ue-context-management-function)

5.2.4 RRC message transfer function [13](#rrc-message-transfer-function)

5.2.5 Paging function [13](#paging-function)

5.2.6 Warning messages information transfer function [13](#warning-messages-information-transfer-function)

5.2.7 Remote Interference Management (RIM) message transfer function [13](#remote-interference-management-rim-message-transfer-function)

5.2.8 Trace function [13](#trace-function)

5.2.9 Load management function [13](#load-management-function)

5.2.10 Self-optimisation support function [13](#self-optimisation-support-function)

5.2.11 Positioning function [14](#positioning-function)

5.2.12 IAB support function [14](#iab-support-function)

5.2.13 NR MBS function [14](#nr-mbs-function)

5.2.14 PDC measurement function [15](#pdc-measurement-function)

5.2.15 QMC support function [15](#qmc-support-function)

5.2.16 Timing Synchronisation Status Reporting function [15](#timing-synchronisation-status-reporting-function)

5.3 F1-U functions [15](#f1-u-functions)

5.3.1 Transfer of user data [15](#transfer-of-user-data)

5.3.2 Flow control function [15](#flow-control-function)

5.4 TEIDs allocation [15](#teids-allocation)

6 Procedures of the F1 interface [15](#procedures-of-the-f1-interface)

6.1 Control plane procedures [15](#control-plane-procedures)

6.1.1 Interface Management procedures [15](#interface-management-procedures)

6.1.2 Context Management procedures [16](#context-management-procedures)

6.1.3 RRC Message Transfer procedures [16](#rrc-message-transfer-procedures)

6.1.3A Warning Message Transmission procedures [16](#a-warning-message-transmission-procedures)

6.1.4 System Information procedures [16](#system-information-procedures)

6.1.5 Paging procedures [17](#paging-procedures)

6.1.6 Void [17](#void-1)

6.1.7 Radio information transfer procedures [17](#radio-information-transfer-procedures)

6.1.8 UE Tracing procedures [17](#ue-tracing-procedures)

6.1.9 Load management procedures [17](#load-management-procedures)

6.1.10 Self-optimisation support procedure [17](#self-optimisation-support-procedure)

6.1.11 Positioning procedures [17](#positioning-procedures)

6.1.12 IAB procedures [18](#iab-procedures)

6.1.13 NR MBS procedures [18](#nr-mbs-procedures)

6.1.14 PDC Measurement procedures [19](#pdc-measurement-procedures)

6.1.15 QMC procedures [19](#qmc-procedures)

6.1.16 Timing Synchronisation Status Reporting procedures [19](#timing-synchronisation-status-reporting-procedures)

6.2 User plane procedures [19](#user-plane-procedures)

7 F1 interface protocol structure [19](#f1-interface-protocol-structure)

7.1 F1 Control Plane Protocol (F1-C) [19](#f1-control-plane-protocol-f1-c)

7.2 F1 User Plane Protocol (F1-U) [20](#f1-user-plane-protocol-f1-u)

8 Other F1 interface specifications [20](#other-f1-interface-specifications)

8.1 NG-RAN F1 interface: layer 1 (3GPP TS 38.471) [20](#ng-ran-f1-interface-layer-1-3gpp-ts-38.471)

8.2 NG-RAN F1 interface: signalling transport (3GPP TS 38.472) [20](#ng-ran-f1-interface-signalling-transport-3gpp-ts-38.472)

8.3 NG-RAN F1 interface: F1AP specification (3GPP TS 38.473) [21](#ng-ran-f1-interface-f1ap-specification-3gpp-ts-38.473)

8.4 NG-RAN F1 interface: data transport and transport signalling (3GPP TS 38.474) [21](#ng-ran-f1-interface-data-transport-and-transport-signalling-3gpp-ts-38.474)

8.5 NG-RAN F1 interface: user plane protocol (3GPP TS 38.425) [21](#ng-ran-f1-interface-user-plane-protocol-3gpp-ts-38.425)

8.6 NG-RAN F1 interface: PDU Session user plane protocol (TS 38.415) [21](#ng-ran-f1-interface-pdu-session-user-plane-protocol-ts-38.415)

Annex A (informative): Change history [22](#annex-a-informative-change-history)

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
