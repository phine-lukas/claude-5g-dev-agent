<!-- table -->
| 3GPP TS 29.532 V18.6.0 (2025-03) (x2) |
| Technical Specification (x2) |
| 3rd Generation Partnership Project; Technical Specification Group Core Network and Terminals; 5G System; 5G Multicast-Broadcast Session Management Services; Stage 3 (Release 18) (x2) |
| The present document has been developed within the 3rd Generation Partnership Project (3GPP TM ) and may be further elaborated for the purposes of 3GPP. / The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented. / This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification. / Specifications and Reports for implementation of the 3GPP TM system should be obtained via the 3GPP Organizational Partners' Publications Offices. (x2) |
<!-- /table -->

<!-- table -->
| 3GPP Postal address 3GPP support office address 650 Route des Lucioles - Sophia Antipolis Valbonne - FRANCE Tel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16 Internet http://www.3gpp.org |
| Copyright Notification No part may be reproduced except as authorized by written permission. / The copyright and the foregoing restriction extend to reproduction in all media. © 2025, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC). All rights reserved. UMTS™ is a Trade Mark of ETSI registered for the benefit of its members 3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners / LTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners GSM® and the GSM logo are registered and owned by the GSM Association |
<!-- /table -->

#  Contents

1 Scope [9](#scope)

2 References [9](#references)

3 Definitions, symbols and abbreviations [10](#definitions-symbols-and-abbreviations)

3.1 Definitions [10](#definitions)

3.2 Abbreviations [10](#abbreviations)

4 Overview [11](#overview)

4.1 Introduction [11](#introduction)

5 Services offered by the MB-SMF [11](#services-offered-by-the-mb-smf)

5.1 Introduction [11](#introduction-1)

5.2 Nmbsmf_TMGI Service [12](#nmbsmf_tmgi-service)

5.2.1 Service Description [12](#service-description)

5.2.2 Service Operations [13](#service-operations)

5.2.2.1 Introduction [13](#introduction-2)

5.2.2.2 TMGI Allocate service operation [13](#tmgi-allocate-service-operation)

5.2.2.2.1 General [13](#general)

5.2.2.3 TMGI Deallocate service operation [13](#tmgi-deallocate-service-operation)

5.2.2.3.1 General [13](#general-1)

5.3 Nmbsmf_MBSSession Service [14](#nmbsmf_mbssession-service)

5.3.1 Service Description [14](#service-description-1)

5.3.2 Service Operations [15](#service-operations-1)

5.3.2.1 Introduction [15](#introduction-3)

5.3.2.2 Create [15](#create)

5.3.2.2.1 General [15](#general-2)

5.3.2.3 Update [17](#update)

5.3.2.3.1 General [17](#general-3)

5.3.2.4 Release [18](#release)

5.3.2.4.1 General [18](#general-4)

5.3.2.5 ContextUpdate [19](#contextupdate)

5.3.2.5.1 General [19](#general-5)

5.3.2.6 StatusSubscribe service operation [21](#statussubscribe-service-operation)

5.3.2.6.1 General [21](#general-6)

5.3.2.6.2 Subscription creation [21](#subscription-creation)

5.3.2.6.3 Subscription update [22](#subscription-update)

5.3.2.7 StatusUnsubscribe [23](#statusunsubscribe)

5.3.2.7.1 General [23](#general-7)

5.3.2.8 StatusNotify [23](#statusnotify)

5.3.2.8.1 General [23](#general-8)

5.3.2.9 ContextStatusSubscribe [24](#contextstatussubscribe)

5.3.2.9.1 General [24](#general-9)

5.3.2.9.2 Creation of a subscription [24](#creation-of-a-subscription)

5.3.2.9.3 Modification of a Subscription [26](#modification-of-a-subscription)

5.3.2.10 ContextStatusUnSubscribe [27](#contextstatusunsubscribe)

5.3.2.10.1 General [27](#general-10)

5.3.2.11 ContextStatusNotify [27](#contextstatusnotify)

5.3.2.11.1 General [27](#general-11)

6 API Definitions [28](#api-definitions)

6.1 Nmbsmf_TMGI Service API [28](#nmbsmf_tmgi-service-api)

6.1.1 Introduction [28](#introduction-4)

6.1.2 Usage of HTTP [29](#usage-of-http)

6.1.2.1 General [29](#general-12)

6.1.2.2 HTTP standard headers [29](#http-standard-headers)

6.1.2.2.1 General [29](#general-13)

6.1.2.2.2 Content type [29](#content-type)

6.1.2.3 HTTP custom headers [29](#http-custom-headers)

6.1.3 Resources [29](#resources)

6.1.3.1 Overview [29](#overview-1)

6.1.3.2 Resource: TMGI collection [30](#resource-tmgi-collection)

6.1.3.2.1 Description [30](#description)

6.1.3.2.2 Resource Definition [30](#resource-definition)

6.1.3.2.3 Resource Standard Methods [30](#resource-standard-methods)

6.1.3.2.4 Resource Custom Operations [33](#resource-custom-operations)

6.1.4 Custom Operations without associated resources [33](#custom-operations-without-associated-resources)

6.1.5 Notifications [33](#notifications)

6.1.6 Data Model [33](#data-model)

6.1.6.1 General [33](#general-14)

6.1.6.2 Structured data types [34](#structured-data-types)

6.1.6.2.1 Introduction [34](#introduction-5)

6.1.6.2.2 Type: TmgiAllocate [34](#type-tmgiallocate)

6.1.6.2.3 Type: TmgiAllocated [34](#type-tmgiallocated)

6.1.6.3 Simple data types and enumerations [35](#simple-data-types-and-enumerations)

6.1.6.3.1 Introduction [35](#introduction-6)

6.1.6.3.2 Simple data types [35](#simple-data-types)

6.1.6.3.3 Enumeration: \<EnumType1\> [35](#enumeration-enumtype1)

6.1.6.3.4 Void [35](#void)

6.1.6.4 Data types describing alternative data types or combinations of data types [35](#data-types-describing-alternative-data-types-or-combinations-of-data-types)

6.1.6.5 Binary data [35](#binary-data)

6.1.7 Error Handling [35](#error-handling)

6.1.7.1 General [35](#general-15)

6.1.7.2 Protocol Errors [35](#protocol-errors)

6.1.7.3 Application Errors [35](#application-errors)

6.1.8 Feature negotiation [36](#feature-negotiation)

6.1.9 Security [36](#_Toc192835899)

6.1.10 HTTP redirection [36](#http-redirection)

6.2 Nmbsmf_MBSSession Service API [36](#nmbsmf_mbssession-service-api)

6.2.1 Introduction [36](#introduction-7)

6.2.2 Usage of HTTP [37](#usage-of-http-1)

6.2.2.1 General [37](#general-16)

6.2.2.2 HTTP standard headers [37](#http-standard-headers-1)

6.2.2.2.1 General [37](#general-17)

6.2.2.2.2 Content type [37](#content-type-1)

6.2.2.3 HTTP custom headers [37](#http-custom-headers-1)

6.2.2.4 HTTP multipart messages [37](#http-multipart-messages)

6.2.3 Resources [38](#resources-1)

6.2.3.1 Overview [38](#overview-2)

6.2.3.2 Resource: MBS sessions collection (Collection) [39](#resource-mbs-sessions-collection-collection)

6.2.3.2.1 Description [39](#description-1)

6.2.3.2.2 Resource Definition [39](#resource-definition-1)

6.2.3.2.3 Resource Standard Methods [39](#resource-standard-methods-1)

6.2.3.2.4 Resource Custom Operations [44](#resource-custom-operations-1)

6.2.3.3 Resource: Individual MBS session (Document) [45](#resource-individual-mbs-session-document)

6.2.3.3.1 Description [45](#description-3)

6.2.3.3.2 Resource Definition [45](#resource-definition-2)

6.2.3.3.3 Resource Standard Methods [45](#resource-standard-methods-2)

6.2.3.3.4 Resource Custom Operations [49](#resource-custom-operations-2)

6.2.3.4 Resource: Subscriptions collection for MBS sessions (Collection) [49](#resource-subscriptions-collection-for-mbs-sessions-collection)

6.2.3.4.1 Description [49](#description-4)

6.2.3.4.2 Resource Definition [49](#resource-definition-3)

6.2.3.4.3 Resource Standard Methods [50](#resource-standard-methods-3)

6.2.3.4.4 Resource Custom Operations [51](#resource-custom-operations-3)

6.2.3.5 Resource: Individual subscription for an MBS session (Document) [51](#resource-individual-subscription-for-an-mbs-session-document)

6.2.3.5.1 Description [51](#description-5)

6.2.3.5.2 Resource Definition [51](#resource-definition-4)

6.2.3.5.3 Resource Standard Methods [52](#resource-standard-methods-4)

6.2.3.5.4 Resource Custom Operations [54](#resource-custom-operations-4)

6.2.3.6 Resource: Subscriptions collection for MBS contexts (Collection) [54](#resource-subscriptions-collection-for-mbs-contexts-collection)

6.2.3.6.1 Description [54](#description-6)

6.2.3.6.2 Resource Definition [54](#resource-definition-5)

6.2.3.6.3 Resource Standard Methods [54](#resource-standard-methods-5)

6.2.3.6.4 Resource Custom Operations [56](#resource-custom-operations-5)

6.2.3.7 Resource: Individual subscription for an MBS context (Document) [56](#resource-individual-subscription-for-an-mbs-context-document)

6.2.3.7.1 Description [56](#description-7)

6.2.3.7.2 Resource Definition [56](#resource-definition-6)

6.2.3.7.3 Resource Standard Methods [56](#resource-standard-methods-6)

6.2.3.7.4 Resource Custom Operations [58](#resource-custom-operations-6)

6.2.4 Custom Operations without associated resources [59](#custom-operations-without-associated-resources-1)

6.2.5 Notifications [59](#notifications-1)

6.2.5.1 General [59](#general-18)

6.2.5.2 StatusNotify [59](#statusnotify-1)

6.2.5.2.1 Description [59](#description-8)

6.2.5.2.2 Target URI [59](#target-uri)

6.2.5.2.3 Standard Methods [59](#standard-methods)

6.2.5.3 ContextStatusNotify [60](#contextstatusnotify-1)

6.2.5.3.1 Description [60](#description-9)

6.2.5.3.2 Target URI [60](#target-uri-1)

6.2.5.3.3 Standard Methods [60](#standard-methods-1)

6.2.6 Data Model [61](#data-model-1)

6.2.6.1 General [61](#general-19)

6.2.6.2 Structured data types [63](#structured-data-types-1)

6.2.6.2.1 Introduction [63](#introduction-8)

6.2.6.2.2 Type: CreateReqData [63](#type-createreqdata)

6.2.6.2.3 Type: CreateRspData [64](#type-createrspdata)

6.2.6.2.4 Type: MbsSessionExtension [64](#type-mbssessionextension)

6.2.6.2.5 Type: ContextUpdateReqData [65](#type-contextupdatereqdata)

6.2.6.2.6 Type: ContextUpdateRspData [65](#type-contextupdaterspdata)

6.2.6.2.7 Type: StatusSubscribeReqData [66](#type-statussubscribereqdata)

6.2.6.2.8 Type: StatusSubscribeRspData [66](#type-statussubscriberspdata)

6.2.6.2.9 Type: N2MbsSmInfo [66](#type-n2mbssminfo)

6.2.6.2.10 Type: ContextStatusNotifyReqData [66](#_Toc192835965)

6.2.6.2.11 Type: StatusNotifyReqData [66](#type-statusnotifyreqdata)

6.2.6.2.12 Type: ContextStatusSubscribeReqData [67](#type-contextstatussubscribereqdata)

6.2.6.2.13 Type: ContextStatusSubscription [67](#type-contextstatussubscription)

6.2.6.2.14 Type: ContextStatusEvent [67](#type-contextstatusevent)

6.2.6.2.15 Type: ContextStatusSubscribeRspData [68](#type-contextstatussubscriberspdata)

6.2.6.2.16 Type: MbsContextInfo [68](#type-mbscontextinfo)

6.2.6.2.17 Type: ContextStatusEventReport [69](#type-contextstatuseventreport)

6.2.6.2.18 Type: MulticastTransportAddressChangeInfo [69](#type-multicasttransportaddresschangeinfo)

6.2.6.2.19 Type: QosInfo [70](#type-qosinfo)

6.2.6.2.20 Type: QosFlowAddModifyRequestItem [70](#type-qosflowaddmodifyrequestitem)

6.2.6.2.21 Type: QosFlowProfile [70](#type-qosflowprofile)

6.2.6.2.22 Type: GbrQosFlowInformation [71](#type-gbrqosflowinformation)

6.2.6.2.23 Type: ProblemDetailsExtension [71](#type-problemdetailsextension)

6.2.6.2.24 Type: UpdateRspData [71](#type-updaterspdata)

6.2.6.3 Simple data types and enumerations [71](#simple-data-types-and-enumerations-1)

6.2.6.3.1 Introduction [71](#introduction-9)

6.2.6.3.2 Simple data types [71](#simple-data-types-1)

6.2.6.3.3 Enumeration: ContextUpdateAction [71](#enumeration-contextupdateaction)

6.2.6.3.4 Enumeration: ContextStatusEventType [72](#enumeration-contextstatuseventtype)

6.2.6.3.5 Enumeration: ReportingMode [72](#enumeration-reportingmode)

6.2.6.3.6 Enumeration: NgapIeType [72](#enumeration-ngapietype)

6.2.6.4 Data types describing alternative data types or combinations of data types [72](#data-types-describing-alternative-data-types-or-combinations-of-data-types-1)

6.2.6.4.1 Type: ExtMbsSession [72](#type-extmbssession)

6.2.6.4.2 Type: ExtProblemDetails [73](#type-extproblemdetails)

6.2.6.5 Binary data [73](#binary-data-1)

6.2.6.5.1 Introduction [73](#introduction-10)

6.2.6.5.2 N2 MBS Session Management Information [73](#n2-mbs-session-management-information)

6.2.6.5.3 Void [73](#void-1)

6.2.7 Error Handling [73](#error-handling-1)

6.2.7.1 General [73](#general-20)

6.2.7.2 Protocol Errors [74](#protocol-errors-1)

6.2.7.3 Application Errors [74](#application-errors-1)

6.2.8 Feature negotiation [74](#feature-negotiation-1)

6.2.9 Security [75](#_Toc192835999)

6.2.10 HTTP redirection [75](#http-redirection-1)

A.1 General [76](#a.1-general)

A.2 Nmbsmf_TMGI API [76](#a.2-nmbsmf_tmgi-api)

A.3 Nmbsmf_MBSSession API [78](#a.3-nmbsmf_mbssession-api)

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
