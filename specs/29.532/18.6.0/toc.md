# TS 29.532 V18.6.0 — Nmbsmf MBS session management

Clause index. `File` is relative to this directory; `Lines` is the 1-based
line range of the clause inside that file.

| Clause | Title | File | Lines |
|---|---|---|---|
| front-matter | Title page, foreword and scope front matter | clauses/front-matter.md | 1-449 |
| 1 | Scope | clauses/1.md | 1-8 |
| 2 | References | clauses/2.md | 1-56 |
| 3 | Definitions, symbols and abbreviations | clauses/3.md | 1-56 |
| 3.1 | Definitions | clauses/3.md | 3-8 |
| 3.2 | Abbreviations | clauses/3.md | 9-56 |
| 4 | Overview | clauses/4.md | 1-24 |
| 4.1 | Introduction | clauses/4.md | 3-24 |
| 5 | Services offered by the MB-SMF | clauses/5.md | 1-689 |
| 5.1 | Introduction | clauses/5.md | 3-23 |
| 5.2 | NmbsmfTMGI Service | clauses/5.md | 24-99 |
| 5.2.1 | Service Description | clauses/5.md | 26-43 |
| 5.2.2 | Service Operations | clauses/5.md | 44-99 |
| 5.2.2.1 | Introduction | clauses/5.md | 46-49 |
| 5.2.2.2 | TMGI Allocate service operation | clauses/5.md | 50-75 |
| 5.2.2.2.1 | General | clauses/5.md | 52-75 |
| 5.2.2.3 | TMGI Deallocate service operation | clauses/5.md | 76-99 |
| 5.2.2.3.1 | General | clauses/5.md | 78-99 |
| 5.3 | NmbsmfMBSSession Service | clauses/5.md | 100-689 |
| 5.3.1 | Service Description | clauses/5.md | 102-131 |
| 5.3.2 | Service Operations | clauses/5.md | 132-689 |
| 5.3.2.1 | Introduction | clauses/5.md | 134-137 |
| 5.3.2.2 | Create | clauses/5.md | 138-231 |
| 5.3.2.2.1 | General | clauses/5.md | 140-231 |
| 5.3.2.3 | Update | clauses/5.md | 232-279 |
| 5.3.2.3.1 | General | clauses/5.md | 234-279 |
| 5.3.2.4 | Release | clauses/5.md | 280-305 |
| 5.3.2.4.1 | General | clauses/5.md | 282-305 |
| 5.3.2.5 | ContextUpdate | clauses/5.md | 306-385 |
| 5.3.2.5.1 | General | clauses/5.md | 308-385 |
| 5.3.2.6 | StatusSubscribe service operation | clauses/5.md | 386-457 |
| 5.3.2.6.1 | General | clauses/5.md | 388-393 |
| 5.3.2.6.2 | Subscription creation | clauses/5.md | 394-435 |
| 5.3.2.6.3 | Subscription update | clauses/5.md | 436-457 |
| 5.3.2.7 | StatusUnsubscribe | clauses/5.md | 458-477 |
| 5.3.2.7.1 | General | clauses/5.md | 460-477 |
| 5.3.2.8 | StatusNotify | clauses/5.md | 478-509 |
| 5.3.2.8.1 | General | clauses/5.md | 480-509 |
| 5.3.2.9 | ContextStatusSubscribe | clauses/5.md | 510-621 |
| 5.3.2.9.1 | General | clauses/5.md | 512-517 |
| 5.3.2.9.2 | Creation of a subscription | clauses/5.md | 518-593 |
| 5.3.2.9.3 | Modification of a Subscription | clauses/5.md | 594-621 |
| 5.3.2.10 | ContextStatusUnSubscribe | clauses/5.md | 622-641 |
| 5.3.2.10.1 | General | clauses/5.md | 624-641 |
| 5.3.2.11 | ContextStatusNotify | clauses/5.md | 642-689 |
| 5.3.2.11.1 | General | clauses/5.md | 644-689 |
| 6 | API Definitions | clauses/6.md | 1-1 |
| 6.1 | NmbsmfTMGI Service API | clauses/6.1.md | 1-365 |
| 6.1.1 | Introduction | clauses/6.1.md | 3-24 |
| 6.1.2 | Usage of HTTP | clauses/6.1.md | 25-50 |
| 6.1.2.1 | General | clauses/6.1.md | 27-34 |
| 6.1.2.2 | HTTP standard headers | clauses/6.1.md | 35-46 |
| 6.1.2.2.1 | General | clauses/6.1.md | 37-40 |
| 6.1.2.2.2 | Content type | clauses/6.1.md | 41-46 |
| 6.1.2.3 | HTTP custom headers | clauses/6.1.md | 47-50 |
| 6.1.3 | Resources | clauses/6.1.md | 51-223 |
| 6.1.3.1 | Overview | clauses/6.1.md | 53-70 |
| 6.1.3.2 | Resource: TMGI collection | clauses/6.1.md | 71-223 |
| 6.1.3.2.1 | Description | clauses/6.1.md | 73-78 |
| 6.1.3.2.2 | Resource Definition | clauses/6.1.md | 79-90 |
| 6.1.3.2.3 | Resource Standard Methods | clauses/6.1.md | 91-219 |
| 6.1.3.2.3.1 | POST | clauses/6.1.md | 93-163 |
| 6.1.3.2.3.2 | DELETE | clauses/6.1.md | 164-219 |
| 6.1.3.2.4 | Resource Custom Operations | clauses/6.1.md | 220-223 |
| 6.1.4 | Custom Operations without associated resources | clauses/6.1.md | 224-227 |
| 6.1.5 | Notifications | clauses/6.1.md | 228-231 |
| 6.1.6 | Data Model | clauses/6.1.md | 232-315 |
| 6.1.6.1 | General | clauses/6.1.md | 234-256 |
| 6.1.6.2 | Structured data types | clauses/6.1.md | 257-284 |
| 6.1.6.2.1 | Introduction | clauses/6.1.md | 259-262 |
| 6.1.6.2.2 | Type: TmgiAllocate | clauses/6.1.md | 263-272 |
| 6.1.6.2.3 | Type: TmgiAllocated | clauses/6.1.md | 273-284 |
| 6.1.6.3 | Simple data types and enumerations | clauses/6.1.md | 285-307 |
| 6.1.6.3.1 | Introduction | clauses/6.1.md | 287-290 |
| 6.1.6.3.2 | Simple data types | clauses/6.1.md | 291-301 |
| 6.1.6.3.3 | Enumeration: <EnumType1> | clauses/6.1.md | 302-305 |
| 6.1.6.3.4 | Void | clauses/6.1.md | 306-307 |
| 6.1.6.4 | Data types describing alternative data types or combinations of data types | clauses/6.1.md | 308-311 |
| 6.1.6.5 | Binary data | clauses/6.1.md | 312-315 |
| 6.1.7 | Error Handling | clauses/6.1.md | 316-337 |
| 6.1.7.1 | General | clauses/6.1.md | 318-323 |
| 6.1.7.2 | Protocol Errors | clauses/6.1.md | 324-327 |
| 6.1.7.3 | Application Errors | clauses/6.1.md | 328-337 |
| 6.1.8 | Feature negotiation | clauses/6.1.md | 338-347 |
| 6.1.9 | Security | clauses/6.1.md | 348-357 |
| 6.1.10 | HTTP redirection | clauses/6.1.md | 358-365 |
| 6.2 | NmbsmfMBSSession Service API | clauses/6.2.md | 1-1469 |
| 6.2.1 | Introduction | clauses/6.2.md | 3-24 |
| 6.2.2 | Usage of HTTP | clauses/6.2.md | 25-87 |
| 6.2.2.1 | General | clauses/6.2.md | 27-34 |
| 6.2.2.2 | HTTP standard headers | clauses/6.2.md | 35-65 |
| 6.2.2.2.1 | General | clauses/6.2.md | 37-40 |
| 6.2.2.2.2 | Content type | clauses/6.2.md | 41-65 |
| 6.2.2.3 | HTTP custom headers | clauses/6.2.md | 66-69 |
| 6.2.2.4 | HTTP multipart messages | clauses/6.2.md | 70-87 |
| 6.2.3 | Resources | clauses/6.2.md | 88-837 |
| 6.2.3.1 | Overview | clauses/6.2.md | 90-116 |
| 6.2.3.2 | Resource: MBS sessions collection (Collection) | clauses/6.2.md | 117-257 |
| 6.2.3.2.1 | Description | clauses/6.2.md | 119-124 |
| 6.2.3.2.2 | Resource Definition | clauses/6.2.md | 125-136 |
| 6.2.3.2.3 | Resource Standard Methods | clauses/6.2.md | 137-203 |
| 6.2.3.2.3.1 | POST | clauses/6.2.md | 139-203 |
| 6.2.3.2.4 | Resource Custom Operations | clauses/6.2.md | 204-257 |
| 6.2.3.2.4.1 | Overview | clauses/6.2.md | 206-213 |
| 6.2.3.2.4.2 | Operation: update | clauses/6.2.md | 214-257 |
| 6.2.3.2.4.2.1 | Description | clauses/6.2.md | 216-219 |
| 6.2.3.2.4.2.2 | Operation Definition | clauses/6.2.md | 220-257 |
| 6.2.3.3 | Resource: Individual MBS session (Document) | clauses/6.2.md | 258-385 |
| 6.2.3.3.1 | Description | clauses/6.2.md | 260-265 |
| 6.2.3.3.2 | Resource Definition | clauses/6.2.md | 266-278 |
| 6.2.3.3.3 | Resource Standard Methods | clauses/6.2.md | 279-381 |
| 6.2.3.3.3.1 | PATCH | clauses/6.2.md | 281-332 |
| 6.2.3.3.3.2 | DELETE | clauses/6.2.md | 333-381 |
| 6.2.3.3.4 | Resource Custom Operations | clauses/6.2.md | 382-385 |
| 6.2.3.4 | Resource: Subscriptions collection for MBS sessions (Collection) | clauses/6.2.md | 386-474 |
| 6.2.3.4.1 | Description | clauses/6.2.md | 388-393 |
| 6.2.3.4.2 | Resource Definition | clauses/6.2.md | 394-405 |
| 6.2.3.4.3 | Resource Standard Methods | clauses/6.2.md | 406-470 |
| 6.2.3.4.3.1 | POST | clauses/6.2.md | 408-470 |
| 6.2.3.4.4 | Resource Custom Operations | clauses/6.2.md | 471-474 |
| 6.2.3.5 | Resource: Individual subscription for an MBS session (Document) | clauses/6.2.md | 475-611 |
| 6.2.3.5.1 | Description | clauses/6.2.md | 477-482 |
| 6.2.3.5.2 | Resource Definition | clauses/6.2.md | 483-495 |
| 6.2.3.5.3 | Resource Standard Methods | clauses/6.2.md | 496-607 |
| 6.2.3.5.3.1 | PATCH | clauses/6.2.md | 498-559 |
| 6.2.3.5.3.2 | DELETE | clauses/6.2.md | 560-607 |
| 6.2.3.5.4 | Resource Custom Operations | clauses/6.2.md | 608-611 |
| 6.2.3.6 | Resource: Subscriptions collection for MBS contexts (Collection) | clauses/6.2.md | 612-700 |
| 6.2.3.6.1 | Description | clauses/6.2.md | 614-619 |
| 6.2.3.6.2 | Resource Definition | clauses/6.2.md | 620-631 |
| 6.2.3.6.3 | Resource Standard Methods | clauses/6.2.md | 632-696 |
| 6.2.3.6.3.1 | POST | clauses/6.2.md | 634-696 |
| 6.2.3.6.4 | Resource Custom Operations | clauses/6.2.md | 697-700 |
| 6.2.3.7 | Resource: Individual subscription for an MBS context (Document) | clauses/6.2.md | 701-837 |
| 6.2.3.7.1 | Description | clauses/6.2.md | 703-708 |
| 6.2.3.7.2 | Resource Definition | clauses/6.2.md | 709-721 |
| 6.2.3.7.3 | Resource Standard Methods | clauses/6.2.md | 722-833 |
| 6.2.3.7.3.1 | PATCH | clauses/6.2.md | 724-785 |
| 6.2.3.7.3.2 | DELETE | clauses/6.2.md | 786-833 |
| 6.2.3.7.4 | Resource Custom Operations | clauses/6.2.md | 834-837 |
| 6.2.4 | Custom Operations without associated resources | clauses/6.2.md | 838-841 |
| 6.2.5 | Notifications | clauses/6.2.md | 842-961 |
| 6.2.5.1 | General | clauses/6.2.md | 844-855 |
| 6.2.5.2 | StatusNotify | clauses/6.2.md | 856-908 |
| 6.2.5.2.1 | Description | clauses/6.2.md | 858-861 |
| 6.2.5.2.2 | Target URI | clauses/6.2.md | 862-871 |
| 6.2.5.2.3 | Standard Methods | clauses/6.2.md | 872-908 |
| 6.2.5.2.3.1 | POST | clauses/6.2.md | 874-908 |
| 6.2.5.3 | ContextStatusNotify | clauses/6.2.md | 909-961 |
| 6.2.5.3.1 | Description | clauses/6.2.md | 911-914 |
| 6.2.5.3.2 | Target URI | clauses/6.2.md | 915-924 |
| 6.2.5.3.3 | Standard Methods | clauses/6.2.md | 925-961 |
| 6.2.5.3.3.1 | POST | clauses/6.2.md | 927-961 |
| 6.2.6 | Data Model | clauses/6.2.md | 962-1397 |
| 6.2.6.1 | General | clauses/6.2.md | 964-1039 |
| 6.2.6.2 | Structured data types | clauses/6.2.md | 1040-1293 |
| 6.2.6.2.1 | Introduction | clauses/6.2.md | 1042-1045 |
| 6.2.6.2.2 | Type: CreateReqData | clauses/6.2.md | 1046-1054 |
| 6.2.6.2.3 | Type: CreateRspData | clauses/6.2.md | 1055-1064 |
| 6.2.6.2.4 | Type: MbsSessionExtension | clauses/6.2.md | 1065-1075 |
| 6.2.6.2.5 | Type: ContextUpdateReqData | clauses/6.2.md | 1076-1092 |
| 6.2.6.2.6 | Type: ContextUpdateRspData | clauses/6.2.md | 1093-1103 |
| 6.2.6.2.7 | Type: StatusSubscribeReqData | clauses/6.2.md | 1104-1111 |
| 6.2.6.2.8 | Type: StatusSubscribeRspData | clauses/6.2.md | 1112-1120 |
| 6.2.6.2.9 | Type: N2MbsSmInfo | clauses/6.2.md | 1121-1129 |
| 6.2.6.2.10 | Type: ContextStatusNotifyReqData | clauses/6.2.md | 1130-1139 |
| 6.2.6.2.11 | Type: StatusNotifyReqData | clauses/6.2.md | 1140-1147 |
| 6.2.6.2.12 | Type: ContextStatusSubscribeReqData | clauses/6.2.md | 1148-1155 |
| 6.2.6.2.13 | Type: ContextStatusSubscription | clauses/6.2.md | 1156-1169 |
| 6.2.6.2.14 | Type: ContextStatusEvent | clauses/6.2.md | 1170-1181 |
| 6.2.6.2.15 | Type: ContextStatusSubscribeRspData | clauses/6.2.md | 1182-1191 |
| 6.2.6.2.16 | Type: MbsContextInfo | clauses/6.2.md | 1192-1205 |
| 6.2.6.2.17 | Type: ContextStatusEventReport | clauses/6.2.md | 1206-1221 |
| 6.2.6.2.18 | Type: MulticastTransportAddressChangeInfo | clauses/6.2.md | 1222-1232 |
| 6.2.6.2.19 | Type: QosInfo | clauses/6.2.md | 1233-1242 |
| 6.2.6.2.20 | Type: QosFlowAddModifyRequestItem | clauses/6.2.md | 1243-1252 |
| 6.2.6.2.21 | Type: QosFlowProfile | clauses/6.2.md | 1253-1266 |
| 6.2.6.2.22 | Type: GbrQosFlowInformation | clauses/6.2.md | 1267-1276 |
| 6.2.6.2.23 | Type: ProblemDetailsExtension | clauses/6.2.md | 1277-1284 |
| 6.2.6.2.24 | Type: UpdateRspData | clauses/6.2.md | 1285-1293 |
| 6.2.6.3 | Simple data types and enumerations | clauses/6.2.md | 1294-1347 |
| 6.2.6.3.1 | Introduction | clauses/6.2.md | 1296-1299 |
| 6.2.6.3.2 | Simple data types | clauses/6.2.md | 1300-1303 |
| 6.2.6.3.3 | Enumeration: ContextUpdateAction | clauses/6.2.md | 1304-1314 |
| 6.2.6.3.4 | Enumeration: ContextStatusEventType | clauses/6.2.md | 1315-1327 |
| 6.2.6.3.5 | Enumeration: ReportingMode | clauses/6.2.md | 1328-1336 |
| 6.2.6.3.6 | Enumeration: NgapIeType | clauses/6.2.md | 1337-1347 |
| 6.2.6.4 | Data types describing alternative data types or combinations of data types | clauses/6.2.md | 1348-1367 |
| 6.2.6.4.1 | Type: ExtMbsSession | clauses/6.2.md | 1350-1358 |
| 6.2.6.4.2 | Type: ExtProblemDetails | clauses/6.2.md | 1359-1367 |
| 6.2.6.5 | Binary data | clauses/6.2.md | 1368-1397 |
| 6.2.6.5.1 | Introduction | clauses/6.2.md | 1370-1379 |
| 6.2.6.5.2 | N2 MBS Session Management Information | clauses/6.2.md | 1380-1395 |
| 6.2.6.5.3 | Void | clauses/6.2.md | 1396-1397 |
| 6.2.7 | Error Handling | clauses/6.2.md | 1398-1429 |
| 6.2.7.1 | General | clauses/6.2.md | 1400-1405 |
| 6.2.7.2 | Protocol Errors | clauses/6.2.md | 1406-1409 |
| 6.2.7.3 | Application Errors | clauses/6.2.md | 1410-1429 |
| 6.2.8 | Feature negotiation | clauses/6.2.md | 1430-1441 |
| 6.2.9 | Security | clauses/6.2.md | 1442-1459 |
| 6.2.10 | HTTP redirection | clauses/6.2.md | 1460-1469 |
| A.1 | General | clauses/annex-A.1.md | 1-10 |
| A.2 | NmbsmfTMGI API | clauses/annex-A.2.md | 1-332 |
| A.3 | NmbsmfMBSSession API | clauses/annex-A.3.md | 1-2320 |
