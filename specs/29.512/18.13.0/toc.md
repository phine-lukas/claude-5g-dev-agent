# TS 29.512 V18.13.0 — Npcf SMPolicyControl

Clause index. `File` is relative to this directory; `Lines` is the 1-based
line range of the clause inside that file.

| Clause | Title | File | Lines |
|---|---|---|---|
| front-matter | Title page, foreword and scope front matter | clauses/front-matter.md | 1-891 |
| 1 | Scope | clauses/1.md | 1-10 |
| 2 | References | clauses/2.md | 1-138 |
| 3 | Definitions, symbols and abbreviations | clauses/3.md | 1-242 |
| 3.1 | Definitions | clauses/3.md | 3-76 |
| 3.2 | Abbreviations | clauses/3.md | 77-242 |
| 4 | NpcfSMPolicyControl Service | clauses/4.md | 1-1 |
| 4.1 | Service Description | clauses/4.1.md | 1-566 |
| 4.1.1 | Overview | clauses/4.1.md | 3-6 |
| 4.1.2 | Service Architecture | clauses/4.1.md | 7-22 |
| 4.1.3 | Network Functions | clauses/4.1.md | 23-104 |
| 4.1.3.1 | Policy Control Function (PCF) | clauses/4.1.md | 25-72 |
| 4.1.3.2 | NF Service Consumers | clauses/4.1.md | 73-104 |
| 4.1.4 | Rules | clauses/4.1.md | 105-514 |
| 4.1.4.1 | General | clauses/4.1.md | 107-120 |
| 4.1.4.2 | PCC rules | clauses/4.1.md | 121-266 |
| 4.1.4.2.1 | PCC rules definition | clauses/4.1.md | 123-250 |
| 4.1.4.2.2 | PCC rules operation | clauses/4.1.md | 251-266 |
| 4.1.4.3 | Session rule | clauses/4.1.md | 267-298 |
| 4.1.4.3.1 | Session rules definition | clauses/4.1.md | 269-288 |
| 4.1.4.3.2 | Session rules operation | clauses/4.1.md | 289-298 |
| 4.1.4.4 | Policy Decision types | clauses/4.1.md | 299-514 |
| 4.1.4.4.1 | General | clauses/4.1.md | 301-316 |
| 4.1.4.4.2 | Traffic control data definition | clauses/4.1.md | 317-374 |
| 4.1.4.4.3 | QoS data definition | clauses/4.1.md | 375-426 |
| 4.1.4.4.4 | Charging data definition | clauses/4.1.md | 427-454 |
| 4.1.4.4.5 | UsageMonitoring data definition | clauses/4.1.md | 455-488 |
| 4.1.4.4.6 | QoS Monitoring data definition | clauses/4.1.md | 489-514 |
| 4.1.5 | Policy control request trigger | clauses/4.1.md | 515-524 |
| 4.1.6 | Requested rule data | clauses/4.1.md | 525-536 |
| 4.1.7 | Requested usage data | clauses/4.1.md | 537-546 |
| 4.1.8 | Condition data | clauses/4.1.md | 547-566 |
| 4.2 | Service Operations | clauses/4.2.md | 1-1 |
| 4.2.1 | Introduction | clauses/4.2.1.md | 1-14 |
| 4.2.2 | NpcfSMPolicyControlCreate Service Operation | clauses/4.2.2.md | 1-512 |
| 4.2.2.1 | General | clauses/4.2.2.md | 3-74 |
| 4.2.2.2 | SM Policy Association establishment | clauses/4.2.2.md | 75-218 |
| 4.2.2.3 | Provisioning of charging related information for PDU session | clauses/4.2.2.md | 219-268 |
| 4.2.2.3.1 | Provisioning of Charging Addresses | clauses/4.2.2.md | 221-248 |
| 4.2.2.3.2 | Provisioning of Default Charging Method | clauses/4.2.2.md | 249-268 |
| 4.2.2.4 | Provisioning of revalidation time | clauses/4.2.2.md | 269-274 |
| 4.2.2.5 | Policy provisioning and enforcement of authorized AMBR per PDU session | clauses/4.2.2.md | 275-292 |
| 4.2.2.6 | Policy provisioning and enforcement of authorized default QoS | clauses/4.2.2.md | 293-312 |
| 4.2.2.7 | Provisioning of PCC rule for Application Detection and Control | clauses/4.2.2.md | 313-318 |
| 4.2.2.8 | 3GPP PS Data Off Support | clauses/4.2.2.md | 319-338 |
| 4.2.2.9 | IMS Emergency Session Support | clauses/4.2.2.md | 339-356 |
| 4.2.2.10 | Request Usage Monitoring Control | clauses/4.2.2.md | 357-360 |
| 4.2.2.11 | Access Network Charging Identifier report | clauses/4.2.2.md | 361-372 |
| 4.2.2.12 | Request for the successful resource allocation notification | clauses/4.2.2.md | 373-376 |
| 4.2.2.13 | Request of Presence Reporting Area Change Report | clauses/4.2.2.md | 377-380 |
| 4.2.2.14 | Provisioning of IP Index Information | clauses/4.2.2.md | 381-386 |
| 4.2.2.15 | Negotiation of the QoS flow for IMS signalling | clauses/4.2.2.md | 387-394 |
| 4.2.2.16 | PCF resource cleanup | clauses/4.2.2.md | 395-398 |
| 4.2.2.17 | Access traffic steering, switching and splitting support | clauses/4.2.2.md | 399-442 |
| 4.2.2.18 | DNN Selection Mode Support | clauses/4.2.2.md | 443-454 |
| 4.2.2.19 | Detection of the SM Policy Association enabling Time Sensitive Communications, Time Synchronization and Deterministic Networking | clauses/4.2.2.md | 455-460 |
| 4.2.2.20 | Support of Dual Connectivity end to end redundant User Plane paths | clauses/4.2.2.md | 461-468 |
| 4.2.2.21 | User Plane Remote Provisioning of UE SNPN Credentials in Onboarding Network | clauses/4.2.2.md | 469-492 |
| 4.2.2.22 | Network slice related data rate policy control | clauses/4.2.2.md | 493-496 |
| 4.2.2.23 | Group related data rate policy control | clauses/4.2.2.md | 497-500 |
| 4.2.2.24 | Network slice usage control | clauses/4.2.2.md | 501-506 |
| 4.2.2.25 | VPLMN Specific Offloading Policy | clauses/4.2.2.md | 507-512 |
| 4.2.3 | NpcfSMPolicyControlUpdateNotify Service Operation | clauses/4.2.3.md | 1-604 |
| 4.2.3.1 | General | clauses/4.2.3.md | 3-68 |
| 4.2.3.2 | SM Policy Association Update request | clauses/4.2.3.md | 69-112 |
| 4.2.3.3 | SM Policy Association termination request | clauses/4.2.3.md | 113-138 |
| 4.2.3.4 | Provisioning of revalidation time | clauses/4.2.3.md | 139-148 |
| 4.2.3.5 | Policy provisioning and enforcement of authorized AMBR per PDU session | clauses/4.2.3.md | 149-160 |
| 4.2.3.6 | Policy provisioning and enforcement of authorized default QoS | clauses/4.2.3.md | 161-170 |
| 4.2.3.7 | Provisioning of PCC rule for Application Detection and Control | clauses/4.2.3.md | 171-178 |
| 4.2.3.8 | 3GPP PS Data Off Support | clauses/4.2.3.md | 179-202 |
| 4.2.3.9 | IMS Emergency Session Support | clauses/4.2.3.md | 203-230 |
| 4.2.3.9.1 | Provisioning of PCC rule | clauses/4.2.3.md | 205-218 |
| 4.2.3.9.2 | Removal of PCC Rules for Emergency Services | clauses/4.2.3.md | 219-230 |
| 4.2.3.10 | Request of Access Network Information | clauses/4.2.3.md | 231-234 |
| 4.2.3.11 | Request Usage Monitoring Control | clauses/4.2.3.md | 235-238 |
| 4.2.3.12 | Ipv6 Multi-homing support | clauses/4.2.3.md | 239-242 |
| 4.2.3.13 | Request for the result of PCC rule removal | clauses/4.2.3.md | 243-248 |
| 4.2.3.14 | Access Network Charging Identifier request | clauses/4.2.3.md | 249-252 |
| 4.2.3.15 | Request for the successful resource allocation notification | clauses/4.2.3.md | 253-256 |
| 4.2.3.16 | PCC Rule Error Report | clauses/4.2.3.md | 257-272 |
| 4.2.3.17 | IMS Restoration Support | clauses/4.2.3.md | 273-286 |
| 4.2.3.18 | P-CSCF Restoration Enhancement Support | clauses/4.2.3.md | 287-294 |
| 4.2.3.19 | Request of Presence Reporting Area Change Report | clauses/4.2.3.md | 295-298 |
| 4.2.3.20 | Session Rule Error Report | clauses/4.2.3.md | 299-312 |
| 4.2.3.21 | Access traffic steering, switching and splitting support | clauses/4.2.3.md | 313-316 |
| 4.2.3.22 | Policy provisioning and enforcement of the AF session with required QoS | clauses/4.2.3.md | 317-338 |
| 4.2.3.23 | Forwarding of TSC user plane node management information and port management information received from the TSN AF or TSCTSF | clauses/4.2.3.md | 339-352 |
| 4.2.3.24 | Provisioning of TSCAI input information and TSC QoS related data | clauses/4.2.3.md | 353-426 |
| 4.2.3.25 | Policy provisioning of QoS Monitoring control | clauses/4.2.3.md | 427-518 |
| 4.2.3.25.1 | General | clauses/4.2.3.md | 429-512 |
| 4.2.3.25.2 | QoS Monitoring when dynamic Satellite Backhaul is used | clauses/4.2.3.md | 513-518 |
| 4.2.3.26 | Policy decision error handling | clauses/4.2.3.md | 519-566 |
| 4.2.3.26.1 | Policy decision types and condition data error handling | clauses/4.2.3.md | 521-536 |
| 4.2.3.26.2 | Policy decision types, condition data and other policy decisions error handling | clauses/4.2.3.md | 537-566 |
| 4.2.3.27 | Network slice related data rate policy control | clauses/4.2.3.md | 567-570 |
| 4.2.3.28 | Group related data rate policy control | clauses/4.2.3.md | 571-574 |
| 4.2.3.29 | Policy provisioning of Periodicity and N6 Traffic Parameter to be measured | clauses/4.2.3.md | 575-592 |
| 4.2.3.30 | Network slice usage control | clauses/4.2.3.md | 593-598 |
| 4.2.3.31 | VPLMN Specific Offloading Policy | clauses/4.2.3.md | 599-604 |
| 4.2.4 | NpcfSMPolicyControlUpdate Service Operation | clauses/4.2.4.md | 1-758 |
| 4.2.4.1 | General | clauses/4.2.4.md | 3-70 |
| 4.2.4.2 | Requesting the update of the Session Management related policies | clauses/4.2.4.md | 71-186 |
| 4.2.4.3 | Request the policy based on revalidation time | clauses/4.2.4.md | 187-202 |
| 4.2.4.4 | Policy provisioning and enforcement of authorized AMBR per PDU session | clauses/4.2.4.md | 203-220 |
| 4.2.4.5 | Policy provisioning and enforcement of authorized default QoS | clauses/4.2.4.md | 221-234 |
| 4.2.4.6 | Application detection information reporting | clauses/4.2.4.md | 235-256 |
| 4.2.4.7 | Indication of QoS Flow Termination Implications | clauses/4.2.4.md | 257-278 |
| 4.2.4.8 | 3GPP PS Data Off Support | clauses/4.2.4.md | 279-310 |
| 4.2.4.9 | Request and Report of Access Network Information | clauses/4.2.4.md | 311-332 |
| 4.2.4.10 | Request Usage Monitoring Control and Reporting Accumulated Usage | clauses/4.2.4.md | 333-380 |
| 4.2.4.10.1 | General | clauses/4.2.4.md | 335-374 |
| 4.2.4.10.2 | PCC Rule Removal | clauses/4.2.4.md | 375-380 |
| 4.2.4.11 | Ipv6 Multi-homing support | clauses/4.2.4.md | 381-390 |
| 4.2.4.12 | Request and report for the result of PCC rule removal | clauses/4.2.4.md | 391-400 |
| 4.2.4.13 | Access Network Charging Identifier request and report | clauses/4.2.4.md | 401-410 |
| 4.2.4.14 | Request and report for the successful resource allocation notification | clauses/4.2.4.md | 411-420 |
| 4.2.4.15 | PCC Rule Error Report | clauses/4.2.4.md | 421-442 |
| 4.2.4.16 | Presence Reporting Area Information Report | clauses/4.2.4.md | 443-456 |
| 4.2.4.17 | UE initiates a resource modification support | clauses/4.2.4.md | 457-494 |
| 4.2.4.18 | Trace Control | clauses/4.2.4.md | 495-498 |
| 4.2.4.19 | Negotiation of the QoS flow for IMS signalling | clauses/4.2.4.md | 499-502 |
| 4.2.4.20 | Notification about Service Data Flow QoS target enforcement | clauses/4.2.4.md | 503-534 |
| 4.2.4.21 | Session Rule Error Report | clauses/4.2.4.md | 535-554 |
| 4.2.4.22 | Request the termination of SM Policy association | clauses/4.2.4.md | 555-560 |
| 4.2.4.23 | Reporting of TSC user plane node management information and port management information | clauses/4.2.4.md | 561-594 |
| 4.2.4.24 | Notification about Service Data Flow QoS Monitoring | clauses/4.2.4.md | 595-648 |
| 4.2.4.25 | Access traffic steering, switching and splitting support | clauses/4.2.4.md | 649-658 |
| 4.2.4.26 | Policy decision error handling | clauses/4.2.4.md | 659-684 |
| 4.2.4.26.1 | Policy decision types and condition data error handling | clauses/4.2.4.md | 661-666 |
| 4.2.4.26.2 | Policy decision types, condition data and other policy decisions error handling | clauses/4.2.4.md | 667-684 |
| 4.2.4.27 | Policy Control for DDN Events | clauses/4.2.4.md | 685-718 |
| 4.2.4.28 | Network slice related data rate policy control | clauses/4.2.4.md | 719-722 |
| 4.2.4.29 | Group related data rate policy control | clauses/4.2.4.md | 723-726 |
| 4.2.4.30 | Notification on network provided BAT Offset policy control trigger | clauses/4.2.4.md | 727-744 |
| 4.2.4.31 | Network slice usage control | clauses/4.2.4.md | 745-750 |
| 4.2.4.32 | VPLMN Specific Offloading Policy | clauses/4.2.4.md | 751-758 |
| 4.2.5 | NpcfSMPolicyControlDelete Service Operation | clauses/4.2.5.md | 1-72 |
| 4.2.5.1 | General | clauses/4.2.5.md | 3-18 |
| 4.2.5.2 | SM Policy Association termination | clauses/4.2.5.md | 19-48 |
| 4.2.5.3 | Report Accumulated Usage | clauses/4.2.5.md | 49-54 |
| 4.2.5.4 | Report Access Network Information | clauses/4.2.5.md | 55-62 |
| 4.2.5.5 | Void | clauses/4.2.5.md | 63-64 |
| 4.2.5.6 | Network slice related data rate policy control | clauses/4.2.5.md | 65-68 |
| 4.2.5.7 | Group related data rate policy control | clauses/4.2.5.md | 69-72 |
| 4.2.6 | Provisioning and Enforcement of Policy Decisions | clauses/4.2.6.md | 1-1 |
| 4.2.6.1 | General | clauses/4.2.6.1.md | 1-112 |
| 4.2.6.2 | PCC Rules | clauses/4.2.6.2.md | 1-772 |
| 4.2.6.2.1 | Overview | clauses/4.2.6.2.md | 3-60 |
| 4.2.6.2.2 | Gate Function | clauses/4.2.6.2.md | 61-68 |
| 4.2.6.2.3 | Policy enforcement for authorized QoS per PCC Rule | clauses/4.2.6.2.md | 69-74 |
| 4.2.6.2.4 | Redirect Function | clauses/4.2.6.2.md | 75-102 |
| 4.2.6.2.5 | Usage Monitoring Control | clauses/4.2.6.2.md | 103-108 |
| 4.2.6.2.6 | Traffic Steering Control support | clauses/4.2.6.2.md | 109-238 |
| 4.2.6.2.6.1 | Steering the traffic in the N6-LAN or steering the 5G-LAN type of services | clauses/4.2.6.2.md | 119-142 |
| 4.2.6.2.6.2 | Steering the traffic to a local access of the data network | clauses/4.2.6.2.md | 143-238 |
| 4.2.6.2.7 | Conditioned PCC rule | clauses/4.2.6.2.md | 239-284 |
| 4.2.6.2.8 | PCC rule for resource sharing | clauses/4.2.6.2.md | 285-300 |
| 4.2.6.2.9 | Resource reservation for services sharing priority | clauses/4.2.6.2.md | 301-338 |
| 4.2.6.2.10 | PCC rule bound to the default QoS flow | clauses/4.2.6.2.md | 339-352 |
| 4.2.6.2.11 | PCC rule for Application Detection and Control | clauses/4.2.6.2.md | 353-368 |
| 4.2.6.2.12 | Provisioning of PCC Rules for Multimedia Priority Services | clauses/4.2.6.2.md | 369-466 |
| 4.2.6.2.12.1 | General | clauses/4.2.6.2.md | 371-394 |
| 4.2.6.2.12.2 | Invocation/Revocation of Priority PDU connectivity services | clauses/4.2.6.2.md | 395-424 |
| 4.2.6.2.12.3 | Invocation/Revocation of IMS Multimedia Priority Services | clauses/4.2.6.2.md | 425-442 |
| 4.2.6.2.12.4 | Invocation/Revocation of MPS for DTS | clauses/4.2.6.2.md | 443-466 |
| 4.2.6.2.13 | Sponsored Data Connectivity | clauses/4.2.6.2.md | 467-484 |
| 4.2.6.2.14 | Support for PCC rule versioning | clauses/4.2.6.2.md | 485-498 |
| 4.2.6.2.15 | Background data transfer support | clauses/4.2.6.2.md | 499-508 |
| 4.2.6.2.16 | Number of supported packet filter for signalled QoS rule limitation support | clauses/4.2.6.2.md | 509-516 |
| 4.2.6.2.17 | Access traffic steering, switching and splitting support | clauses/4.2.6.2.md | 517-636 |
| 4.2.6.2.18 | Void | clauses/4.2.6.2.md | 637-638 |
| 4.2.6.2.19 | Provisioning of PCC Rules for Mission Critical Services | clauses/4.2.6.2.md | 639-712 |
| 4.2.6.2.19.1 | General | clauses/4.2.6.2.md | 641-664 |
| 4.2.6.2.19.2 | Invocation/Revocation of Priority PDU connectivity services | clauses/4.2.6.2.md | 665-694 |
| 4.2.6.2.19.3 | Invocation/Revocation of IMS Mission Critical Services | clauses/4.2.6.2.md | 695-712 |
| 4.2.6.2.20 | PCC rules authorization with preliminary service information | clauses/4.2.6.2.md | 713-732 |
| 4.2.6.2.21 | Policy Control for L4S | clauses/4.2.6.2.md | 733-750 |
| 4.2.6.2.22 | UL/DL policy control based on Round-Trip latency requirements | clauses/4.2.6.2.md | 751-764 |
| 4.2.6.2.23 | Policy Decision for AF requested QoS for a target UE or group of UE(s) not identified by UE address(es) | clauses/4.2.6.2.md | 765-772 |
| 4.2.6.3 | Session Rules | clauses/4.2.6.3.md | 1-130 |
| 4.2.6.3.1 | Overview | clauses/4.2.6.3.md | 3-28 |
| 4.2.6.3.2 | Conditioned Session rule | clauses/4.2.6.3.md | 29-106 |
| 4.2.6.3.2.1 | General | clauses/4.2.6.3.md | 31-70 |
| 4.2.6.3.2.2 | Time conditioned authorized Session-AMBR | clauses/4.2.6.3.md | 71-80 |
| 4.2.6.3.2.3 | Time conditioned authorized default QoS | clauses/4.2.6.3.md | 81-90 |
| 4.2.6.3.2.4 | Access type conditioned authorized Session-AMBR | clauses/4.2.6.3.md | 91-106 |
| 4.2.6.3.3 | Provisioning of authorized default QoS | clauses/4.2.6.3.md | 107-114 |
| 4.2.6.3.4 | Access traffic steering, switching and splitting support | clauses/4.2.6.3.md | 115-122 |
| 4.2.6.3.5 | Usage Monitoring Control | clauses/4.2.6.3.md | 123-130 |
| 4.2.6.4 | Policy control request triggers | clauses/4.2.6.4.md | 1-10 |
| 4.2.6.5 | Encoding of the request of information reporting | clauses/4.2.6.5.md | 1-224 |
| 4.2.6.5.1 | Request of Access Network Charging Identifier | clauses/4.2.6.5.md | 3-8 |
| 4.2.6.5.2 | RAN NAS Cause Support | clauses/4.2.6.5.md | 9-14 |
| 4.2.6.5.3 | Provisioning of the Usage Monitoring Control Policy | clauses/4.2.6.5.md | 15-152 |
| 4.2.6.5.3.1 | General | clauses/4.2.6.5.md | 17-86 |
| 4.2.6.5.3.2 | Disabling Usage Monitoring | clauses/4.2.6.5.md | 87-100 |
| 4.2.6.5.3.3 | PCF Requested Usage Report | clauses/4.2.6.5.md | 101-104 |
| 4.2.6.5.3.4 | Usage Monitoring during Network Slice Replacement | clauses/4.2.6.5.md | 105-152 |
| 4.2.6.5.4 | Request for Access Network Information | clauses/4.2.6.5.md | 153-166 |
| 4.2.6.5.5 | Request for the successful resource allocation notification | clauses/4.2.6.5.md | 167-170 |
| 4.2.6.5.6 | Provisioning of Presence Reporting Area Information | clauses/4.2.6.5.md | 171-204 |
| 4.2.6.5.7 | Policy provisioning and enforcement of reflective QoS | clauses/4.2.6.5.md | 205-224 |
| 4.2.6.6 | Authorized QoS | clauses/4.2.6.6.md | 1-86 |
| 4.2.6.6.1 | General | clauses/4.2.6.6.md | 3-32 |
| 4.2.6.6.2 | Policy provisioning and enforcement of authorized QoS per service data flow | clauses/4.2.6.6.md | 33-76 |
| 4.2.6.6.3 | Policy provisioning and enforcement of authorized explicitly signalled QoS Characteristics | clauses/4.2.6.6.md | 77-86 |
| 4.2.6.7 | Monitoring the data rate per network slice for a UE | clauses/4.2.6.7.md | 1-18 |
| 4.2.6.8 | Network slice related data rate policy control | clauses/4.2.6.8.md | 1-84 |
| 4.2.6.8.1 | General | clauses/4.2.6.8.md | 3-22 |
| 4.2.6.8.2 | PCF-based network slice data rate policy control by using QoS parameters | clauses/4.2.6.8.md | 23-68 |
| 4.2.6.8.3 | Network slice data rate policy control with assistance of the NWDAF | clauses/4.2.6.8.md | 69-84 |
| 4.2.6.9 | Group related data rate policy control | clauses/4.2.6.9.md | 1-32 |
| 4.2.6.9.1 | General | clauses/4.2.6.9.md | 3-32 |
| 4.2.6.10 | Policy Provisioning for eXtended Reality and Interactive Media Services | clauses/4.2.6.10.md | 1-38 |
| 4.2.6.10.1 | Support for delivery of multi-modal services | clauses/4.2.6.10.md | 3-14 |
| 4.2.6.10.2 | Traffic Parameter Information and N6 Traffic Parameter Measurement | clauses/4.2.6.10.md | 15-18 |
| 4.2.6.10.3 | PDU Set handling | clauses/4.2.6.10.md | 19-28 |
| 4.2.6.10.4 | End of Data Burst Handling | clauses/4.2.6.10.md | 29-38 |
| 4.2.7 | Handling of requests which collide with an existing SM Policy Association | clauses/4.2.7.md | 1-10 |
| 4.2.8 | UE IP address support | clauses/4.2.8.md | 1-12 |
| 5 | NpcfSMPolicyControl Service API | clauses/5.md | 1-1 |
| 5.1 | Introduction | clauses/5.1.md | 1-22 |
| 5.2 | Usage of HTTP | clauses/5.2.md | 1-32 |
| 5.2.1 | General | clauses/5.2.md | 3-10 |
| 5.2.2 | HTTP standard headers | clauses/5.2.md | 11-22 |
| 5.2.2.1 | General | clauses/5.2.md | 13-16 |
| 5.2.2.2 | Content type | clauses/5.2.md | 17-22 |
| 5.2.3 | HTTP custom headers | clauses/5.2.md | 23-32 |
| 5.2.3.1 | General | clauses/5.2.md | 25-28 |
| 5.2.3.2 | 3gpp-Sbi-Origination-Timestamp | clauses/5.2.md | 29-32 |
| 5.3 | Resources | clauses/5.3.md | 1-259 |
| 5.3.1 | Resource Structure | clauses/5.3.md | 3-20 |
| 5.3.2 | Resource: SM Policies | clauses/5.3.md | 21-90 |
| 5.3.2.1 | Description | clauses/5.3.md | 23-26 |
| 5.3.2.2 | Resource definition | clauses/5.3.md | 27-39 |
| 5.3.2.3 | Resource Standard Methods | clauses/5.3.md | 40-86 |
| 5.3.2.3.1 | POST | clauses/5.3.md | 42-86 |
| 5.3.2.4 | Resource Custom Operations | clauses/5.3.md | 87-90 |
| 5.3.3 | Resource: Individual SM Policy | clauses/5.3.md | 91-259 |
| 5.3.3.1 | Description | clauses/5.3.md | 93-96 |
| 5.3.3.2 | Resource definition | clauses/5.3.md | 97-110 |
| 5.3.3.3 | Resource Standard Methods | clauses/5.3.md | 111-158 |
| 5.3.3.3.1 | GET | clauses/5.3.md | 113-158 |
| 5.3.3.4 | Resource Custom Operations | clauses/5.3.md | 159-259 |
| 5.3.3.4.1 | Overview | clauses/5.3.md | 161-170 |
| 5.3.3.4.2 | Operation: delete | clauses/5.3.md | 171-213 |
| 5.3.3.4.2.1 | Description | clauses/5.3.md | 173-174 |
| 5.3.3.4.2.2 | Operation Definition | clauses/5.3.md | 175-213 |
| 5.3.3.4.3 | Operation: update | clauses/5.3.md | 214-259 |
| 5.3.3.4.3.1 | Description | clauses/5.3.md | 216-217 |
| 5.3.3.4.3.2 | Operation Definition | clauses/5.3.md | 218-259 |
| 5.4 | Custom Operations without associated resources | clauses/5.4.md | 1-4 |
| 5.5 | Notifications | clauses/5.5.md | 1-102 |
| 5.5.1 | General | clauses/5.5.md | 3-12 |
| 5.5.2 | Policy Update Notification | clauses/5.5.md | 13-59 |
| 5.5.2.1 | Description | clauses/5.5.md | 15-18 |
| 5.5.2.2 | Operation Definition | clauses/5.5.md | 19-59 |
| 5.5.3 | Request for termination of the policy association | clauses/5.5.md | 60-102 |
| 5.5.3.1 | Description | clauses/5.5.md | 62-65 |
| 5.5.3.2 | Operation Definition | clauses/5.5.md | 66-102 |
| 5.6 | Data Model | clauses/5.6.md | 1-1 |
| 5.6.1 | General | clauses/5.6.1.md | 1-220 |
| 5.6.2 | Structured data types | clauses/5.6.2.md | 1-977 |
| 5.6.2.1 | Introduction | clauses/5.6.2.md | 3-6 |
| 5.6.2.2 | Type SmPolicyControl | clauses/5.6.2.md | 7-16 |
| 5.6.2.3 | Type SmPolicyContextData | clauses/5.6.2.md | 17-79 |
| 5.6.2.4 | Type SmPolicyDecision | clauses/5.6.2.md | 80-123 |
| 5.6.2.5 | Type SmPolicyNotification | clauses/5.6.2.md | 124-134 |
| 5.6.2.6 | Type PccRule | clauses/5.6.2.md | 135-175 |
| 5.6.2.7 | Type SessionRule | clauses/5.6.2.md | 176-190 |
| 5.6.2.8 | Type QosData | clauses/5.6.2.md | 191-221 |
| 5.6.2.9 | Type ConditionData | clauses/5.6.2.md | 222-235 |
| 5.6.2.10 | Type TrafficControlData | clauses/5.6.2.md | 236-268 |
| 5.6.2.11 | Type ChargingData | clauses/5.6.2.md | 269-289 |
| 5.6.2.12 | Type UsageMonitoringData | clauses/5.6.2.md | 290-310 |
| 5.6.2.13 | Type RedirectInformation | clauses/5.6.2.md | 311-321 |
| 5.6.2.14 | Type FlowInformation | clauses/5.6.2.md | 322-338 |
| 5.6.2.15 | Type SmPolicyDeleteData | clauses/5.6.2.md | 339-354 |
| 5.6.2.16 | Type QosCharacteristics | clauses/5.6.2.md | 355-371 |
| 5.6.2.17 | Type ChargingInformation | clauses/5.6.2.md | 372-386 |
| 5.6.2.18 | Type AccuUsageReport | clauses/5.6.2.md | 387-403 |
| 5.6.2.19 | Type SmPolicyUpdateContextData | clauses/5.6.2.md | 404-486 |
| 5.6.2.20 | Type UpPathChgEvent | clauses/5.6.2.md | 487-498 |
| 5.6.2.21 | Type TerminationNotification | clauses/5.6.2.md | 499-509 |
| 5.6.2.22 | Type AppDetectionInfo | clauses/5.6.2.md | 510-520 |
| 5.6.2.23 | Type AccNetChId | clauses/5.6.2.md | 521-533 |
| 5.6.2.24 | Type RequestedRuleData | clauses/5.6.2.md | 534-543 |
| 5.6.2.25 | Type RequestedUsageData | clauses/5.6.2.md | 544-553 |
| 5.6.2.26 | Type UeCampingRep | clauses/5.6.2.md | 554-574 |
| 5.6.2.27 | Type RuleReport | clauses/5.6.2.md | 575-590 |
| 5.6.2.28 | Type RanNasRelCause | clauses/5.6.2.md | 591-602 |
| 5.6.2.29 | Type UeInitiatedResourceRequest | clauses/5.6.2.md | 603-615 |
| 5.6.2.30 | Type PacketFilterInfo | clauses/5.6.2.md | 616-629 |
| 5.6.2.31 | Type RequestedQos | clauses/5.6.2.md | 630-640 |
| 5.6.2.32 | Type QosNotificationControlInfo | clauses/5.6.2.md | 641-653 |
| 5.6.2.33 | Type PartialSuccessReport | clauses/5.6.2.md | 654-668 |
| 5.6.2.34 | Type AuthorizedDefaultQos | clauses/5.6.2.md | 669-687 |
| 5.6.2.35 | Type AccNetChargingAddress | clauses/5.6.2.md | 688-698 |
| 5.6.2.36 | Type ErrorReport | clauses/5.6.2.md | 699-711 |
| 5.6.2.37 | Type SessionRuleReport | clauses/5.6.2.md | 712-722 |
| 5.6.2.38 | Type ServingNfIdentity | clauses/5.6.2.md | 723-735 |
| 5.6.2.39 | Type SteeringMode | clauses/5.6.2.md | 736-752 |
| 5.6.2.40 | Type QosMonitoringData | clauses/5.6.2.md | 753-779 |
| 5.6.2.41 | Type TsnBridgeInfo | clauses/5.6.2.md | 780-793 |
| 5.6.2.42 | Type QosMonitoringReport | clauses/5.6.2.md | 794-811 |
| 5.6.2.43 | Type AdditionalAccessInfo | clauses/5.6.2.md | 812-821 |
| 5.6.2.44 | Void | clauses/5.6.2.md | 822-823 |
| 5.6.2.45 | Type PortManagementContainer | clauses/5.6.2.md | 824-833 |
| 5.6.2.46 | Type IpMulticastAddressInfo | clauses/5.6.2.md | 834-846 |
| 5.6.2.47 | Type BridgeManagementContainer | clauses/5.6.2.md | 847-855 |
| 5.6.2.48 | Type DownlinkDataNotificationControl | clauses/5.6.2.md | 856-866 |
| 5.6.2.49 | Type DownlinkDataNotificationControlRm | clauses/5.6.2.md | 867-874 |
| 5.6.2.50 | Type SgsnAddress | clauses/5.6.2.md | 875-885 |
| 5.6.2.51 | Void | clauses/5.6.2.md | 886-887 |
| 5.6.2.52 | Type ThresholdValue | clauses/5.6.2.md | 888-898 |
| 5.6.2.53 | Type NwdafData | clauses/5.6.2.md | 899-908 |
| 5.6.2.54 | Type CallInfo | clauses/5.6.2.md | 909-918 |
| 5.6.2.55 | Type CalleeInfo | clauses/5.6.2.md | 919-929 |
| 5.6.2.56 | Type TrafficParaData | clauses/5.6.2.md | 930-944 |
| 5.6.2.57 | Type L4sSupportInfo | clauses/5.6.2.md | 945-954 |
| 5.6.2.58 | Void | clauses/5.6.2.md | 955-956 |
| 5.6.2.59 | Type SliceUsgCtrlInfo | clauses/5.6.2.md | 957-977 |
| 5.6.3 | Simple data types and enumerations | clauses/5.6.3.md | 1-627 |
| 5.6.3.1 | Introduction | clauses/5.6.3.md | 3-6 |
| 5.6.3.2 | Simple data types | clauses/5.6.3.md | 7-24 |
| 5.6.3.3 | Enumeration: FlowDirection | clauses/5.6.3.md | 25-36 |
| 5.6.3.4 | Enumeration: ReportingLevel | clauses/5.6.3.md | 37-47 |
| 5.6.3.5 | Enumeration: MeteringMethod | clauses/5.6.3.md | 48-59 |
| 5.6.3.6 | Enumeration: PolicyControlRequestTrigger | clauses/5.6.3.md | 60-256 |
| 5.6.3.7 | Enumeration: RequestedRuleDataType | clauses/5.6.3.md | 257-271 |
| 5.6.3.8 | Enumeration: RuleStatus | clauses/5.6.3.md | 272-281 |
| 5.6.3.9 | Enumeration: FailureCode | clauses/5.6.3.md | 282-321 |
| 5.6.3.10 | Enumeration: AfSigProtocol | clauses/5.6.3.md | 322-331 |
| 5.6.3.11 | Enumeration: RuleOperation | clauses/5.6.3.md | 332-346 |
| 5.6.3.12 | Enumeration: RedirectAddressType | clauses/5.6.3.md | 347-358 |
| 5.6.3.13 | Enumeration: QosFlowUsage | clauses/5.6.3.md | 359-368 |
| 5.6.3.14 | Enumeration: FailureCause | clauses/5.6.3.md | 369-381 |
| 5.6.3.15 | Enumeration: FlowDirectionRm | clauses/5.6.3.md | 382-385 |
| 5.6.3.16 | Enumeration: CreditManagementStatus | clauses/5.6.3.md | 386-398 |
| 5.6.3.17 | Enumeration: SessionRuleFailureCode | clauses/5.6.3.md | 399-419 |
| 5.6.3.18 | Enumeration: SteeringFunctionality | clauses/5.6.3.md | 420-430 |
| 5.6.3.19 | Enumeration: SteerModeValue | clauses/5.6.3.md | 431-444 |
| 5.6.3.20 | Enumeration: MulticastAccessControl | clauses/5.6.3.md | 445-454 |
| 5.6.3.21 | Enumeration RequestedQosMonitoringParameter | clauses/5.6.3.md | 455-469 |
| 5.6.3.22 | Enumeration: ReportingFrequency | clauses/5.6.3.md | 470-479 |
| 5.6.3.23 | Enumeration: SmPolicyAssociationReleaseCause | clauses/5.6.3.md | 480-494 |
| 5.6.3.24 | Enumeration: PduSessionRelCause | clauses/5.6.3.md | 495-504 |
| 5.6.3.25 | Enumeration: MaPduIndication | clauses/5.6.3.md | 505-514 |
| 5.6.3.26 | Enumeration: AtsssCapability | clauses/5.6.3.md | 515-535 |
| 5.6.3.27 | Enumeration: NetLocAccessSupport | clauses/5.6.3.md | 536-547 |
| 5.6.3.28 | Enumeration: PolicyDecisionFailureCode | clauses/5.6.3.md | 548-562 |
| 5.6.3.29 | Enumeration: NotificationControlIndication | clauses/5.6.3.md | 563-574 |
| 5.6.3.31 | Enumeration: SteerModeIndicator | clauses/5.6.3.md | 575-584 |
| 5.6.3.32 | Enumeration TrafficParameterMeas | clauses/5.6.3.md | 585-595 |
| 5.6.3.33 | Enumeration: QosMonitoringParamType | clauses/5.6.3.md | 596-606 |
| 5.6.3.34 | Enumeration TransportMode | clauses/5.6.3.md | 607-627 |
| 5.7 | Error handling | clauses/5.7.md | 1-56 |
| 5.7.1 | General | clauses/5.7.md | 3-12 |
| 5.7.2 | Protocol Errors | clauses/5.7.md | 13-16 |
| 5.7.3 | Application Errors | clauses/5.7.md | 17-56 |
| 5.8 | Feature negotiation | clauses/5.8.md | 1-109 |
| 5.9 | Security | clauses/5.9.md | 1-12 |
| A.1 | General | clauses/annex-A.1.md | 1-10 |
| A.2 | NpcfSMPolicyControl API | clauses/annex-A.2.md | 1-6382 |
| B.1 | Scope | clauses/annex-B.1.md | 1-14 |
| B.2 | NpcfSMPolicyControl Service | clauses/annex-B.2.md | 1-26 |
| B.2.1 | Service Description | clauses/annex-B.2.md | 3-26 |
| B.2.1.1 | Overview | clauses/annex-B.2.md | 5-8 |
| B.2.1.2 | Service Architecture | clauses/annex-B.2.md | 9-26 |
| B.3 | Service Operation | clauses/annex-B.3.md | 1-536 |
| B.3.1 | Introduction | clauses/annex-B.3.md | 3-8 |
| B.3.2 | NpcfSMPolicyControlCreate Service Operation | clauses/annex-B.3.md | 9-126 |
| B.3.2.0 | General | clauses/annex-B.3.md | 11-62 |
| B.3.2.1 | UE Location related information | clauses/annex-B.3.md | 63-90 |
| B.3.2.2 | Access Type related information | clauses/annex-B.3.md | 91-118 |
| B.3.2.3 | Access Network Charging Identifier report | clauses/annex-B.3.md | 119-126 |
| B.3.3 | NpcfSMPolicyControlUpdateNotify Service Operation | clauses/annex-B.3.md | 127-194 |
| B.3.3.0 | General | clauses/annex-B.3.md | 129-134 |
| B.3.3.1 | Policy Update When UE suspends | clauses/annex-B.3.md | 135-146 |
| B.3.3.2 | Request report of EPS Fallback | clauses/annex-B.3.md | 147-154 |
| B.3.3.3 | S-GW Restoration Support | clauses/annex-B.3.md | 155-180 |
| B.3.3.4 | Request of Access Network Charging Identifier | clauses/annex-B.3.md | 181-184 |
| B.3.3.5 | Forwarding of UE policy container and/or PCRT(s) for URSP provisioning in EPS | clauses/annex-B.3.md | 185-194 |
| B.3.4 | NpcfSMPolicyControlUpdate Service Operation | clauses/annex-B.3.md | 195-436 |
| B.3.4.0 | General | clauses/annex-B.3.md | 197-226 |
| B.3.4.1 | Number of Supported Packet Filters Report | clauses/annex-B.3.md | 227-232 |
| B.3.4.2 | Policy Update When UE suspends | clauses/annex-B.3.md | 233-250 |
| B.3.4.2.1 | Policy Update Error Report | clauses/annex-B.3.md | 235-246 |
| B.3.4.2.2 | UE State Change Report | clauses/annex-B.3.md | 247-250 |
| B.3.4.3 | UE Location related information | clauses/annex-B.3.md | 251-278 |
| B.3.4.4 | Presence Reporting Area Information Report | clauses/annex-B.3.md | 279-284 |
| B.3.4.5 | Access Type related information | clauses/annex-B.3.md | 285-324 |
| B.3.4.6 | Report of EPS Fallback | clauses/annex-B.3.md | 325-336 |
| B.3.4.7 | MA PDU Session | clauses/annex-B.3.md | 337-342 |
| B.3.4.8 | EPS RAN NAS Cause Support | clauses/annex-B.3.md | 343-346 |
| B.3.4.9 | S-GW Restoration Support | clauses/annex-B.3.md | 347-384 |
| B.3.4.10 | UE initiates a resource modification support | clauses/annex-B.3.md | 385-412 |
| B.3.4.11 | Report of Access Charging Network Identifier | clauses/annex-B.3.md | 413-416 |
| B.3.4.11a | Detection of the SM Policy Association enabling URSP provisioning in EPS | clauses/annex-B.3.md | 417-426 |
| B.3.4.12 | Reporting of UE Policy container for URSP provisioning in EPS | clauses/annex-B.3.md | 427-432 |
| B.3.4.13 | Reporting of the PCC rule(s) removal in EPS | clauses/annex-B.3.md | 433-436 |
| B.3.5 | NpcfSMPolicyControlDelete Service Operation | clauses/annex-B.3.md | 437-448 |
| B.3.5.1 | General | clauses/annex-B.3.md | 439-444 |
| B.3.5.2 | EPS RAN NAS Cause Support | clauses/annex-B.3.md | 445-448 |
| B.3.6 | Provisioning and Enforcement of Policy Decisions | clauses/annex-B.3.md | 449-518 |
| B.3.6.1 | QoS mapping perfomed by the SMF+PGW-C | clauses/annex-B.3.md | 451-474 |
| B.3.6.2 | Provisioning of Presence Reporting Area Information | clauses/annex-B.3.md | 475-480 |
| B.3.6.3 | Request and Report of Access Network information | clauses/annex-B.3.md | 481-498 |
| B.3.6.4 | MA PDU sessions with connectivity over E-UTRAN/EPC and non-3GPP access to 5GC | clauses/annex-B.3.md | 499-508 |
| B.3.6.5 | MA PDU sessions with connectivity over 5GC and non-3GPP access to EPC | clauses/annex-B.3.md | 509-518 |
| B.3.7 | Detection and handling of late arriving requests for interworking scenario | clauses/annex-B.3.md | 519-536 |
| B.3.7.1 | Handling of requests which collide with an existing SM Policy Association | clauses/annex-B.3.md | 521-524 |
| B.3.7.2 | Detection and handling of requests which have timed out at the originating entity | clauses/annex-B.3.md | 525-536 |
| C.1 | Scope | clauses/annex-C.1.md | 1-4 |
| C.2 | NpcfSMPolicyControl Service | clauses/annex-C.2.md | 1-116 |
| C.2.1 | Service Description | clauses/annex-C.2.md | 3-116 |
| C.2.1.1 | Overview | clauses/annex-C.2.md | 5-8 |
| C.2.1.2 | Service Architecture | clauses/annex-C.2.md | 9-14 |
| C.2.1.3 | Network Functions | clauses/annex-C.2.md | 15-26 |
| C.2.1.3.1 | Policy Control Function (PCF) | clauses/annex-C.2.md | 17-20 |
| C.2.1.3.2 | NF Service Consumers | clauses/annex-C.2.md | 21-26 |
| C.2.1.4 | Rules | clauses/annex-C.2.md | 27-42 |
| C.2.1.4.1 | PCC Rules | clauses/annex-C.2.md | 29-36 |
| C.2.1.4.2 | Gate Function | clauses/annex-C.2.md | 37-42 |
| C.2.1.5 | Policy control request trigger | clauses/annex-C.2.md | 43-104 |
| C.2.1.6 | UE IP address support | clauses/annex-C.2.md | 105-116 |
| C.3 | Service Operation | clauses/annex-C.3.md | 1-1 |
| C.3.1 | Introduction | clauses/annex-C.3.1.md | 1-4 |
| C.3.2 | NpcfSMPolicyControlCreate Service Operation | clauses/annex-C.3.2.md | 1-48 |
| C.3.2.1 | General | clauses/annex-C.3.2.md | 3-38 |
| C.3.2.2 | IPTV service support | clauses/annex-C.3.2.md | 39-42 |
| C.3.2.3 | SNPN services support | clauses/annex-C.3.2.md | 43-48 |
| C.3.3 | NpcfSMPolicyControlUpdateNotify Service Operation | clauses/annex-C.3.3.md | 1-20 |
| C.3.3.1 | General | clauses/annex-C.3.3.md | 3-16 |
| C.3.3.2 | IPTV service support | clauses/annex-C.3.3.md | 17-20 |
| C.3.4 | NpcfSMPolicyControlUpdate Service Operation | clauses/annex-C.3.4.md | 1-42 |
| C.3.4.1 | General | clauses/annex-C.3.4.md | 3-36 |
| C.3.4.2 | IPTV service support | clauses/annex-C.3.4.md | 37-42 |
| C.3.5 | NpcfSMPolicyControlDelete Service Operation | clauses/annex-C.3.5.md | 1-22 |
| C.3.5.1 | General | clauses/annex-C.3.5.md | 3-22 |
| C.3.6 | Provisioning and Enforcement of Policy Decisions | clauses/annex-C.3.6.md | 1-1 |
| C.3.6.0 | General | clauses/annex-C.3.6.0.md | 1-14 |
| C.3.6.1 | IPTV service support | clauses/annex-C.3.6.1.md | 1-12 |
| C.3.6.2 | Hybrid Access support | clauses/annex-C.3.6.2.md | 1-1 |
| C.3.6.2.1 | General | clauses/annex-C.3.6.2.1.md | 1-12 |
| C.3.6.2.2 | Hybrid Access with single PDU session | clauses/annex-C.3.6.2.2.md | 1-18 |
| C.3.6.2.3 | Hybrid Access with MA PDU session connectivity over NG-RAN and wireline | clauses/annex-C.3.6.2.3.md | 1-8 |
| C.3.6.2.4 | Hybrid Access with MA PDU session connectivity over EPC/E-UTRAN and wireline using EPC interworking scenarios | clauses/annex-C.3.6.2.4.md | 1-895 |
