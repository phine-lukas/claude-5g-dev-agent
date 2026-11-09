# TS 23.501 V18.12.0 — 5GS system architecture

Clause index. `File` is relative to this directory; `Lines` is the 1-based
line range of the clause inside that file.

| Clause | Title | File | Lines |
|---|---|---|---|
| front-matter | Title page, foreword and scope front matter | clauses/front-matter.md | 1-2153 |
| 1 | Scope | clauses/1.md | 1-12 |
| 2 | References | clauses/2.md | 1-404 |
| 3 | Definitions and abbreviations | clauses/3.md | 1-768 |
| 3.1 | Definitions | clauses/3.md | 3-334 |
| 3.2 | Abbreviations | clauses/3.md | 335-768 |
| 4 | Architecture model and concepts | clauses/4.md | 1-1324 |
| 4.1 | General concepts | clauses/4.md | 3-26 |
| 4.2 | Architecture reference model | clauses/4.md | 27-976 |
| 4.2.1 | General | clauses/4.md | 29-56 |
| 4.2.2 | Network Functions and entities | clauses/4.md | 57-134 |
| 4.2.3 | Non-roaming reference architecture | clauses/4.md | 135-190 |
| 4.2.4 | Roaming reference architectures | clauses/4.md | 191-262 |
| 4.2.5 | Data Storage architectures | clauses/4.md | 263-316 |
| 4.2.5a | Radio Capabilities Signalling optimisation | clauses/4.md | 317-330 |
| 4.2.6 | Service-based interfaces | clauses/4.md | 331-398 |
| 4.2.7 | Reference points | clauses/4.md | 399-566 |
| 4.2.8 | Support of non-3GPP access | clauses/4.md | 567-838 |
| 4.2.8.0 | General | clauses/4.md | 569-580 |
| 4.2.8.1 | General Concepts to Support Trusted and Untrusted Non-3GPP Access | clauses/4.md | 581-626 |
| 4.2.8.1A | General Concepts to support Wireline Access | clauses/4.md | 627-648 |
| 4.2.8.2 | Architecture Reference Model for Trusted and Untrusted Non-3GPP Accesses | clauses/4.md | 649-716 |
| 4.2.8.2.1 | Non-roaming Architecture | clauses/4.md | 651-668 |
| 4.2.8.2.2 | LBO Roaming Architecture | clauses/4.md | 669-694 |
| 4.2.8.2.3 | Home-routed Roaming Architecture | clauses/4.md | 695-716 |
| 4.2.8.3 | Reference Points for Non-3GPP Access | clauses/4.md | 717-762 |
| 4.2.8.3.1 | Overview | clauses/4.md | 719-746 |
| 4.2.8.3.2 | Requirements on Ta | clauses/4.md | 747-762 |
| 4.2.8.4 | Architecture Reference Model for Wireline Access network | clauses/4.md | 763-790 |
| 4.2.8.5 | Access to 5GC from devices that do not support 5GC NAS over WLAN access | clauses/4.md | 791-838 |
| 4.2.8.5.1 | General | clauses/4.md | 793-800 |
| 4.2.8.5.2 | Reference Architecture | clauses/4.md | 801-810 |
| 4.2.8.5.3 | Network Functions | clauses/4.md | 811-826 |
| 4.2.8.5.4 | Reference Points | clauses/4.md | 827-838 |
| 4.2.9 | Network Analytics architecture | clauses/4.md | 839-842 |
| 4.2.10 | Architecture Reference Model for ATSSS Support | clauses/4.md | 843-880 |
| 4.2.11 | Architecture for 5G multicast-broadcast services | clauses/4.md | 881-884 |
| 4.2.12 | Architecture for Proximity based Services (ProSe) in 5GS | clauses/4.md | 885-888 |
| 4.2.13 | Architecture enhancements for Edge Computing | clauses/4.md | 889-892 |
| 4.2.14 | Architecture for Support of Uncrewed Aerial Systems connectivity, identification and tracking | clauses/4.md | 893-896 |
| 4.2.15 | Architecture to support WLAN connection using 5G credentials without 5GS registration | clauses/4.md | 897-958 |
| 4.2.16 | Architecture to support User Plane Information Exposure via a service-based interface | clauses/4.md | 959-972 |
| 4.2.17 | Architecture for Ranging based services and Sidelink Positioning | clauses/4.md | 973-976 |
| 4.3 | Interworking with EPC | clauses/4.md | 977-1108 |
| 4.3.1 | Non-roaming architecture | clauses/4.md | 979-994 |
| 4.3.2 | Roaming architecture | clauses/4.md | 995-1010 |
| 4.3.3 | Interworking between 5GC via non-3GPP access and E-UTRAN connected to EPC | clauses/4.md | 1011-1044 |
| 4.3.3.1 | Non-roaming architecture | clauses/4.md | 1013-1024 |
| 4.3.3.2 | Roaming architecture | clauses/4.md | 1025-1044 |
| 4.3.4 | Interworking between ePDG connected to EPC and 5GS | clauses/4.md | 1045-1078 |
| 4.3.4.1 | Non-roaming architecture | clauses/4.md | 1047-1058 |
| 4.3.4.2 | Roaming architectures | clauses/4.md | 1059-1078 |
| 4.3.5 | Service Exposure in Interworking Scenarios | clauses/4.md | 1079-1108 |
| 4.3.5.1 | Non-roaming architecture | clauses/4.md | 1081-1098 |
| 4.3.5.2 | Roaming architectures | clauses/4.md | 1099-1108 |
| 4.4 | Specific services | clauses/4.md | 1109-1324 |
| 4.4.1 | Public Warning System | clauses/4.md | 1111-1114 |
| 4.4.2 | SMS over NAS | clauses/4.md | 1115-1174 |
| 4.4.2.0 | General | clauses/4.md | 1117-1122 |
| 4.4.2.1 | Architecture to support SMS over NAS | clauses/4.md | 1123-1158 |
| 4.4.2.2 | Reference point to support SMS over NAS | clauses/4.md | 1159-1170 |
| 4.4.2.3 | Service based interface to support SMS over NAS | clauses/4.md | 1171-1174 |
| 4.4.3 | IMS support | clauses/4.md | 1175-1184 |
| 4.4.4 | Location services | clauses/4.md | 1185-1198 |
| 4.4.4.1 | Architecture to support Location Services | clauses/4.md | 1187-1190 |
| 4.4.4.2 | Reference point to support Location Services | clauses/4.md | 1191-1194 |
| 4.4.4.3 | Service Based Interfaces to support Location Services | clauses/4.md | 1195-1198 |
| 4.4.5 | Application Triggering Services | clauses/4.md | 1199-1206 |
| 4.4.6 | 5G LAN-type Services | clauses/4.md | 1207-1230 |
| 4.4.6.1 | User plane architecture to support 5G LAN-type service | clauses/4.md | 1209-1226 |
| 4.4.6.2 | Reference points to support 5G LAN-type service | clauses/4.md | 1227-1230 |
| 4.4.7 | MSISDN-less MO SMS Service | clauses/4.md | 1231-1240 |
| 4.4.8 | Architecture to enable Time Sensitive Communication, Time Synchronization and Deterministic Networking | clauses/4.md | 1241-1324 |
| 4.4.8.1 | General | clauses/4.md | 1243-1256 |
| 4.4.8.2 | Architecture to support IEEE Time Sensitive Networking | clauses/4.md | 1257-1286 |
| 4.4.8.3 | Architecture for AF requested support of Time Sensitive Communication and Time Synchronization | clauses/4.md | 1287-1304 |
| 4.4.8.4 | Architecture to support IETF Deterministic Networking | clauses/4.md | 1305-1324 |
| 5 | High level features | clauses/5.md | 1-1 |
| 5.1 | General | clauses/5.1.md | 1-4 |
| 5.2 | Network Access Control | clauses/5.2.md | 1-68 |
| 5.2.1 | General | clauses/5.2.md | 3-18 |
| 5.2.2 | Network selection | clauses/5.2.md | 19-24 |
| 5.2.2a | Void | clauses/5.2.md | 25-26 |
| 5.2.3 | Identification and authentication | clauses/5.2.md | 27-30 |
| 5.2.4 | Authorisation | clauses/5.2.md | 31-34 |
| 5.2.5 | Access control and barring | clauses/5.2.md | 35-60 |
| 5.2.6 | Policy control | clauses/5.2.md | 61-64 |
| 5.2.7 | Lawful Interception | clauses/5.2.md | 65-68 |
| 5.3 | Registration and Connection Management | clauses/5.3.md | 1-724 |
| 5.3.1 | General | clauses/5.3.md | 3-6 |
| 5.3.2 | Registration Management | clauses/5.3.md | 7-200 |
| 5.3.2.1 | General | clauses/5.3.md | 9-22 |
| 5.3.2.2 | 5GS Registration Management states | clauses/5.3.md | 23-86 |
| 5.3.2.2.1 | General | clauses/5.3.md | 25-32 |
| 5.3.2.2.2 | RM-DEREGISTERED state | clauses/5.3.md | 33-50 |
| 5.3.2.2.3 | RM-REGISTERED state | clauses/5.3.md | 51-76 |
| 5.3.2.2.4 | 5GS Registration Management State models | clauses/5.3.md | 77-86 |
| 5.3.2.3 | Registration Area management | clauses/5.3.md | 87-142 |
| 5.3.2.4 | Support of a UE registered over both 3GPP and Non-3GPP access | clauses/5.3.md | 143-200 |
| 5.3.3 | Connection Management | clauses/5.3.md | 201-408 |
| 5.3.3.1 | General | clauses/5.3.md | 203-206 |
| 5.3.3.2 | 5GS Connection Management states | clauses/5.3.md | 207-380 |
| 5.3.3.2.1 | General | clauses/5.3.md | 209-218 |
| 5.3.3.2.2 | CM-IDLE state | clauses/5.3.md | 219-244 |
| 5.3.3.2.3 | CM-CONNECTED state | clauses/5.3.md | 245-266 |
| 5.3.3.2.4 | 5GS Connection Management State models | clauses/5.3.md | 267-280 |
| 5.3.3.2.5 | CM-CONNECTED with RRCINACTIVE state | clauses/5.3.md | 281-380 |
| 5.3.3.3 | NAS signalling connection management | clauses/5.3.md | 381-400 |
| 5.3.3.3.1 | General | clauses/5.3.md | 383-386 |
| 5.3.3.3.2 | NAS signalling connection establishment | clauses/5.3.md | 387-394 |
| 5.3.3.3.3 | NAS signalling connection Release | clauses/5.3.md | 395-400 |
| 5.3.3.4 | Support of a UE connected over both 3GPP and Non-3GPP access | clauses/5.3.md | 401-408 |
| 5.3.4 | UE Mobility | clauses/5.3.md | 409-710 |
| 5.3.4.1 | Mobility Restrictions | clauses/5.3.md | 411-580 |
| 5.3.4.1.1 | General | clauses/5.3.md | 413-550 |
| 5.3.4.1.2 | Management of Service Area Restrictions | clauses/5.3.md | 551-580 |
| 5.3.4.2 | Mobility Pattern | clauses/5.3.md | 581-586 |
| 5.3.4.3 | Radio Resource Management functions | clauses/5.3.md | 587-670 |
| 5.3.4.3.1 | General | clauses/5.3.md | 589-618 |
| 5.3.4.3.2 | Preferred band(s) per data radio bearer(s) | clauses/5.3.md | 619-622 |
| 5.3.4.3.3 | Redirection to dedicated frequency band(s) for an S-NSSAI | clauses/5.3.md | 623-650 |
| 5.3.4.3.4 | Network Slice based cell reselection and Random Access | clauses/5.3.md | 651-670 |
| 5.3.4.4 | UE mobility event notification | clauses/5.3.md | 671-710 |
| 5.3.5 | Triggers for network analytics | clauses/5.3.md | 711-724 |
| 5.4 | 3GPP access specific aspects | clauses/5.4.md | 1-814 |
| 5.4.1 | UE reachability in CM-IDLE | clauses/5.4.md | 3-144 |
| 5.4.1.1 | General | clauses/5.4.md | 5-50 |
| 5.4.1.2 | UE reachability allowing mobile terminated data while the UE is CM-IDLE | clauses/5.4.md | 51-54 |
| 5.4.1.3 | Mobile Initiated Connection Only (MICO) mode | clauses/5.4.md | 55-88 |
| 5.4.1.4 | Support of Unavailability Period | clauses/5.4.md | 89-144 |
| 5.4.2 | UE reachability in CM-CONNECTED | clauses/5.4.md | 145-158 |
| 5.4.3 | Paging strategy handling | clauses/5.4.md | 159-204 |
| 5.4.3.1 | General | clauses/5.4.md | 161-172 |
| 5.4.3.2 | Paging Policy Differentiation | clauses/5.4.md | 173-196 |
| 5.4.3.3 | Paging Priority | clauses/5.4.md | 197-204 |
| 5.4.4 | UE Radio Capability handling | clauses/5.4.md | 205-378 |
| 5.4.4.1 | UE radio capability information storage in the AMF | clauses/5.4.md | 207-240 |
| 5.4.4.1a | UE radio capability signalling optimisation (RACS) | clauses/5.4.md | 241-348 |
| 5.4.4.2 | Void | clauses/5.4.md | 349-350 |
| 5.4.4.2a | UE Radio Capability Match Request | clauses/5.4.md | 351-356 |
| 5.4.4.3 | Paging assistance information | clauses/5.4.md | 357-378 |
| 5.4.4a | UE MM Core Network Capability handling | clauses/5.4.md | 379-454 |
| 5.4.4b | UE 5GSM Core Network Capability handling | clauses/5.4.md | 455-476 |
| 5.4.5 | DRX (Discontinuous Reception) framework | clauses/5.4.md | 477-494 |
| 5.4.6 | Core Network assistance information for RAN optimization | clauses/5.4.md | 495-540 |
| 5.4.6.1 | General | clauses/5.4.md | 497-500 |
| 5.4.6.2 | Core Network assisted RAN parameters tuning | clauses/5.4.md | 501-530 |
| 5.4.6.3 | Core Network assisted RAN paging information | clauses/5.4.md | 531-540 |
| 5.4.7 | NG-RAN location reporting | clauses/5.4.md | 541-556 |
| 5.4.8 | Support for identification and restriction of using unlicensed spectrum | clauses/5.4.md | 557-588 |
| 5.4.9 | Wake Up Signal Assistance | clauses/5.4.md | 589-616 |
| 5.4.9.1 | General | clauses/5.4.md | 591-604 |
| 5.4.9.2 | Group Wake Up Signal | clauses/5.4.md | 605-616 |
| 5.4.10 | Support for identification and restriction of using NR satellite access | clauses/5.4.md | 617-632 |
| 5.4.11 | Support for integrating NR satellite access into 5GS | clauses/5.4.md | 633-696 |
| 5.4.11.1 | General | clauses/5.4.md | 635-638 |
| 5.4.11.2 | Support of RAT types defined in 5GC for satellite access | clauses/5.4.md | 639-644 |
| 5.4.11.3 | Void | clauses/5.4.md | 645-646 |
| 5.4.11.4 | Verification of UE location | clauses/5.4.md | 647-662 |
| 5.4.11.5 | Network selection for NR satellite access | clauses/5.4.md | 663-670 |
| 5.4.11.6 | Support of Mobility Registration Update | clauses/5.4.md | 671-676 |
| 5.4.11.7 | Tracking Area handling for NR satellite access | clauses/5.4.md | 677-684 |
| 5.4.11.8 | Support for mobility Forbidden Area and Service Area Restrictions for NR satellite access | clauses/5.4.md | 685-696 |
| 5.4.12 | Paging Early Indication with Paging Subgrouping Assistance | clauses/5.4.md | 697-734 |
| 5.4.12.1 | General | clauses/5.4.md | 699-714 |
| 5.4.12.2 | Core Network Assistance for PEIPS | clauses/5.4.md | 715-734 |
| 5.4.13 | Support of discontinuous network coverage for satellite access | clauses/5.4.md | 735-814 |
| 5.4.13.0 | General | clauses/5.4.md | 737-752 |
| 5.4.13.1 | Mobility Management and Power Saving Optimization | clauses/5.4.md | 753-778 |
| 5.4.13.2 | Coverage availability information provisioning to the UE | clauses/5.4.md | 779-784 |
| 5.4.13.3 | Coverage availability information provisioning to the AMF | clauses/5.4.md | 785-792 |
| 5.4.13.4 | Paging | clauses/5.4.md | 793-798 |
| 5.4.13.5 | Overload control | clauses/5.4.md | 799-814 |
| 5.5 | Non-3GPP access specific aspects | clauses/5.5.md | 1-102 |
| 5.5.0 | General | clauses/5.5.md | 3-6 |
| 5.5.1 | Registration Management | clauses/5.5.md | 7-36 |
| 5.5.2 | Connection Management | clauses/5.5.md | 37-80 |
| 5.5.3 | UE Reachability | clauses/5.5.md | 81-102 |
| 5.5.3.1 | UE reachability in CM-IDLE | clauses/5.5.md | 83-92 |
| 5.5.3.2 | UE reachability in CM-CONNECTED | clauses/5.5.md | 93-102 |
| 5.6 | Session Management | clauses/5.6.md | 1-1230 |
| 5.6.1 | Overview | clauses/5.6.md | 3-117 |
| 5.6.2 | Interaction between AMF and SMF | clauses/5.6.md | 118-201 |
| 5.6.3 | Roaming | clauses/5.6.md | 202-229 |
| 5.6.4 | Single PDU Session with multiple PDU Session Anchors | clauses/5.6.md | 230-333 |
| 5.6.4.1 | General | clauses/5.6.md | 232-247 |
| 5.6.4.2 | Usage of an UL Classifier for a PDU Session | clauses/5.6.md | 248-299 |
| 5.6.4.3 | Usage of IPv6 multi-homing for a PDU Session | clauses/5.6.md | 300-333 |
| 5.6.5 | Support for Local Area Data Network | clauses/5.6.md | 334-431 |
| 5.6.5a | Supporting LADN per DNN and S-NSSAI | clauses/5.6.md | 432-469 |
| 5.6.6 | Secondary authentication/authorization by a DN-AAA server during the establishment of a PDU Session | clauses/5.6.md | 470-549 |
| 5.6.7 | Application Function influence on traffic routing | clauses/5.6.md | 550-801 |
| 5.6.7.1 | General | clauses/5.6.md | 552-773 |
| 5.6.7.2 | Enhancement of UP path management based on the coordination with AFs | clauses/5.6.md | 774-801 |
| 5.6.8 | Selective activation and deactivation of UP connection of existing PDU Session | clauses/5.6.md | 802-831 |
| 5.6.9 | Session and Service Continuity | clauses/5.6.md | 832-915 |
| 5.6.9.1 | General | clauses/5.6.md | 834-845 |
| 5.6.9.2 | SSC mode | clauses/5.6.md | 846-893 |
| 5.6.9.2.1 | SSC Mode 1 | clauses/5.6.md | 848-859 |
| 5.6.9.2.2 | SSC Mode 2 | clauses/5.6.md | 860-873 |
| 5.6.9.2.3 | SSC Mode 3 | clauses/5.6.md | 874-893 |
| 5.6.9.3 | SSC mode selection | clauses/5.6.md | 894-915 |
| 5.6.10 | Specific aspects of different PDU Session types | clauses/5.6.md | 916-1053 |
| 5.6.10.1 | Support of IP PDU Session type | clauses/5.6.md | 918-941 |
| 5.6.10.2 | Support of Ethernet PDU Session type | clauses/5.6.md | 942-1011 |
| 5.6.10.3 | Support of Unstructured PDU Session type | clauses/5.6.md | 1012-1037 |
| 5.6.10.4 | Maximum Transfer Unit size considerations | clauses/5.6.md | 1038-1053 |
| 5.6.11 | UE presence in Area of Interest reporting usage by SMF | clauses/5.6.md | 1054-1109 |
| 5.6.12 | Use of Network Instance | clauses/5.6.md | 1110-1127 |
| 5.6.13 | Always-on PDU session | clauses/5.6.md | 1128-1139 |
| 5.6.14 | Support of Framed Routing | clauses/5.6.md | 1140-1163 |
| 5.6.15 | Triggers for network analytics | clauses/5.6.md | 1164-1179 |
| 5.6.16 | Support for Service Function Chaining | clauses/5.6.md | 1180-1230 |
| 5.6.16.1 | General | clauses/5.6.md | 1182-1203 |
| 5.6.16.2 | Application Function influence on Service Function Chaining | clauses/5.6.md | 1204-1230 |
| 5.7 | QoS model | clauses/5.7.md | 1-805 |
| 5.7.1 | General Overview | clauses/5.7.md | 3-276 |
| 5.7.1.1 | QoS Flow | clauses/5.7.md | 5-28 |
| 5.7.1.2 | QoS Profile | clauses/5.7.md | 29-66 |
| 5.7.1.2a | Alternative QoS Profile | clauses/5.7.md | 67-84 |
| 5.7.1.3 | Control of QoS Flows | clauses/5.7.md | 85-100 |
| 5.7.1.4 | QoS Rules | clauses/5.7.md | 101-118 |
| 5.7.1.5 | QoS Flow mapping | clauses/5.7.md | 119-184 |
| 5.7.1.6 | DL traffic | clauses/5.7.md | 185-202 |
| 5.7.1.7 | UL Traffic | clauses/5.7.md | 203-216 |
| 5.7.1.8 | AMBR/MFBR enforcement and rate limitation | clauses/5.7.md | 217-240 |
| 5.7.1.9 | Precedence Value | clauses/5.7.md | 241-244 |
| 5.7.1.10 | UE-Slice-MBR enforcement and rate limitation | clauses/5.7.md | 245-254 |
| 5.7.1.11 | QoS aspects of home-routed roaming | clauses/5.7.md | 255-276 |
| 5.7.2 | 5G QoS Parameters | clauses/5.7.md | 277-452 |
| 5.7.2.1 | 5QI | clauses/5.7.md | 279-292 |
| 5.7.2.2 | ARP | clauses/5.7.md | 293-308 |
| 5.7.2.3 | RQA | clauses/5.7.md | 309-312 |
| 5.7.2.4 | Notification control | clauses/5.7.md | 313-384 |
| 5.7.2.4.1 | General | clauses/5.7.md | 315-322 |
| 5.7.2.4.1a | Notification Control without Alternative QoS Profiles | clauses/5.7.md | 323-338 |
| 5.7.2.4.1b | Notification control with Alternative QoS Profiles | clauses/5.7.md | 339-358 |
| 5.7.2.4.2 | Usage of Notification control with Alternative QoS Profiles at handover | clauses/5.7.md | 359-374 |
| 5.7.2.4.3 | Usage of Notification control with Alternative QoS Profiles during QoS Flow establishment and modification | clauses/5.7.md | 375-384 |
| 5.7.2.5 | Flow Bit Rates | clauses/5.7.md | 385-402 |
| 5.7.2.6 | Aggregate Bit Rates | clauses/5.7.md | 403-424 |
| 5.7.2.7 | Default values | clauses/5.7.md | 425-442 |
| 5.7.2.8 | Maximum Packet Loss Rate | clauses/5.7.md | 443-448 |
| 5.7.2.9 | Wireline access network specific 5G QoS parameters | clauses/5.7.md | 449-452 |
| 5.7.3 | 5G QoS characteristics | clauses/5.7.md | 453-552 |
| 5.7.3.1 | General | clauses/5.7.md | 455-478 |
| 5.7.3.2 | Resource Type | clauses/5.7.md | 479-486 |
| 5.7.3.3 | Priority Level | clauses/5.7.md | 487-498 |
| 5.7.3.4 | Packet Delay Budget | clauses/5.7.md | 499-530 |
| 5.7.3.5 | Packet Error Rate | clauses/5.7.md | 531-534 |
| 5.7.3.6 | Averaging Window | clauses/5.7.md | 535-542 |
| 5.7.3.7 | Maximum Data Burst Volume | clauses/5.7.md | 543-552 |
| 5.7.4 | Standardized 5QI to QoS characteristics mapping | clauses/5.7.md | 553-597 |
| 5.7.5 | Reflective QoS | clauses/5.7.md | 598-693 |
| 5.7.5.1 | General | clauses/5.7.md | 600-613 |
| 5.7.5.2 | UE Derived QoS Rule | clauses/5.7.md | 614-649 |
| 5.7.5.3 | Reflective QoS Control | clauses/5.7.md | 650-693 |
| 5.7.6 | Packet Filter Set | clauses/5.7.md | 694-755 |
| 5.7.6.1 | General | clauses/5.7.md | 696-709 |
| 5.7.6.2 | IP Packet Filter Set | clauses/5.7.md | 710-735 |
| 5.7.6.3 | Ethernet Packet Filter Set | clauses/5.7.md | 736-755 |
| 5.7.7 | PDU Set QoS Parameters | clauses/5.7.md | 756-805 |
| 5.7.7.1 | General | clauses/5.7.md | 758-775 |
| 5.7.7.2 | PDU Set Delay Budget | clauses/5.7.md | 776-789 |
| 5.7.7.3 | PDU Set Error Rate | clauses/5.7.md | 790-801 |
| 5.7.7.4 | PDU Set Integrated Handling Information | clauses/5.7.md | 802-805 |
| 5.8 | User Plane Management | clauses/5.8.md | 1-1056 |
| 5.8.1 | General | clauses/5.8.md | 3-24 |
| 5.8.2 | Functional Description | clauses/5.8.md | 25-759 |
| 5.8.2.1 | General | clauses/5.8.md | 27-30 |
| 5.8.2.2 | UE IP Address Management | clauses/5.8.md | 31-142 |
| 5.8.2.2.1 | General | clauses/5.8.md | 33-108 |
| 5.8.2.2.2 | Routing rules configuration | clauses/5.8.md | 109-116 |
| 5.8.2.2.3 | The procedure of Stateless IPv6 Address Autoconfiguration | clauses/5.8.md | 117-126 |
| 5.8.2.2.4 | IPv6 Prefix Delegation via DHCPv6 | clauses/5.8.md | 127-142 |
| 5.8.2.3 | Management of CN Tunnel Info | clauses/5.8.md | 143-156 |
| 5.8.2.3.1 | General | clauses/5.8.md | 145-150 |
| 5.8.2.3.2 | Void | clauses/5.8.md | 151-152 |
| 5.8.2.3.3 | Management of CN Tunnel Info in the UPF | clauses/5.8.md | 153-156 |
| 5.8.2.4 | Traffic Detection | clauses/5.8.md | 157-196 |
| 5.8.2.4.1 | General | clauses/5.8.md | 159-164 |
| 5.8.2.4.2 | Traffic Detection Information | clauses/5.8.md | 165-196 |
| 5.8.2.5 | Control of User Plane Forwarding | clauses/5.8.md | 197-279 |
| 5.8.2.5.1 | General | clauses/5.8.md | 199-222 |
| 5.8.2.5.2 | Data forwarding between the SMF and UPF | clauses/5.8.md | 223-237 |
| 5.8.2.5.3 | Support of Ethernet PDU Session type | clauses/5.8.md | 238-279 |
| 5.8.2.6 | Charging and Usage Monitoring Handling | clauses/5.8.md | 280-325 |
| 5.8.2.6.1 | General | clauses/5.8.md | 282-287 |
| 5.8.2.6.2 | Activation of Usage Reporting in UPF | clauses/5.8.md | 288-301 |
| 5.8.2.6.3 | Reporting of Usage Information towards SMF | clauses/5.8.md | 302-325 |
| 5.8.2.7 | PDU Session and QoS Flow Policing | clauses/5.8.md | 326-337 |
| 5.8.2.8 | PCC Related Functions | clauses/5.8.md | 338-397 |
| 5.8.2.8.1 | Activation/Deactivation of predefined PCC rules | clauses/5.8.md | 340-361 |
| 5.8.2.8.2 | Enforcement of Dynamic PCC Rules | clauses/5.8.md | 362-373 |
| 5.8.2.8.3 | Redirection | clauses/5.8.md | 374-379 |
| 5.8.2.8.4 | Support of PFD Management | clauses/5.8.md | 380-397 |
| 5.8.2.9 | Functionality of Sending of "End marker" | clauses/5.8.md | 398-429 |
| 5.8.2.9.0 | Introduction | clauses/5.8.md | 400-403 |
| 5.8.2.9.1 | UPF Constructing the "End marker" Packets | clauses/5.8.md | 404-415 |
| 5.8.2.9.2 | SMF Constructing the "End marker" Packets | clauses/5.8.md | 416-429 |
| 5.8.2.10 | UP Tunnel Management | clauses/5.8.md | 430-439 |
| 5.8.2.11 | Parameters for N4 session management (moved) | clauses/5.8.md | 440-443 |
| 5.8.2.12 | Reporting of the UE MAC addresses used in a PDU Session | clauses/5.8.md | 444-453 |
| 5.8.2.13 | Support for 5G VN group communication | clauses/5.8.md | 454-635 |
| 5.8.2.13.0 | General | clauses/5.8.md | 456-489 |
| 5.8.2.13.1 | Support for unicast traffic forwarding of a 5G VN | clauses/5.8.md | 490-537 |
| 5.8.2.13.2 | Support for unicast traffic forwarding update due to UE mobility | clauses/5.8.md | 538-547 |
| 5.8.2.13.3 | Support for user plane traffic replication in a 5G VN | clauses/5.8.md | 548-635 |
| 5.8.2.13.3.1 | User plane traffic replication based on UPF internal functionality | clauses/5.8.md | 550-569 |
| 5.8.2.13.3.2 | User plane traffic replication based on PDRs with replication instructions | clauses/5.8.md | 570-635 |
| 5.8.2.14 | Inter PLMN User Plane Security functionality | clauses/5.8.md | 636-643 |
| 5.8.2.15 | Void | clauses/5.8.md | 644-645 |
| 5.8.2.16 | Support for L2TP tunnelling on N6 | clauses/5.8.md | 646-657 |
| 5.8.2.17 | Data exposure via Service Based interface | clauses/5.8.md | 658-671 |
| 5.8.2.18 | QoS Flow related QoS monitoring and reporting | clauses/5.8.md | 672-701 |
| 5.8.2.19 | Explicit Buffer Management | clauses/5.8.md | 702-753 |
| 5.8.2.19.1 | General | clauses/5.8.md | 704-711 |
| 5.8.2.19.2 | Buffering at UPF | clauses/5.8.md | 712-747 |
| 5.8.2.19.3 | Buffering at SMF | clauses/5.8.md | 748-753 |
| 5.8.2.20 | SMF Pause of Charging | clauses/5.8.md | 754-759 |
| 5.8.3 | Explicit Buffer Management (moved) | clauses/5.8.md | 760-763 |
| 5.8.4 | SMF Pause of Charging (moved) | clauses/5.8.md | 764-767 |
| 5.8.5 | Parameters for N4 session management | clauses/5.8.md | 768-1056 |
| 5.8.5.1 | General | clauses/5.8.md | 770-819 |
| 5.8.5.2 | N4 Session Context | clauses/5.8.md | 820-831 |
| 5.8.5.3 | Packet Detection Rule | clauses/5.8.md | 832-863 |
| 5.8.5.4 | QoS Enforcement Rule | clauses/5.8.md | 864-888 |
| 5.8.5.5 | Usage Reporting Rule | clauses/5.8.md | 889-910 |
| 5.8.5.6 | Forwarding Action Rule | clauses/5.8.md | 911-934 |
| 5.8.5.7 | Usage Report generated by UPF | clauses/5.8.md | 935-953 |
| 5.8.5.8 | Multi-Access Rule | clauses/5.8.md | 954-975 |
| 5.8.5.9 | Bridge/Router Information | clauses/5.8.md | 976-986 |
| 5.8.5.10 | Void | clauses/5.8.md | 987-988 |
| 5.8.5.11 | Session Reporting Rule | clauses/5.8.md | 989-1010 |
| 5.8.5.12 | Session reporting generated by UPF | clauses/5.8.md | 1011-1024 |
| 5.8.5.13 | Void | clauses/5.8.md | 1025-1026 |
| 5.8.5.14 | TSC Management Information | clauses/5.8.md | 1027-1041 |
| 5.8.5.15 | Downlink Data Report generated by UPF | clauses/5.8.md | 1042-1056 |
| 5.9 | Identifiers | clauses/5.9.md | 1-148 |
| 5.9.1 | General | clauses/5.9.md | 3-8 |
| 5.9.2 | Subscription Permanent Identifier | clauses/5.9.md | 9-32 |
| 5.9.2a | Subscription Concealed Identifier | clauses/5.9.md | 33-38 |
| 5.9.3 | Permanent Equipment Identifier | clauses/5.9.md | 39-56 |
| 5.9.4 | 5G Globally Unique Temporary Identifier | clauses/5.9.md | 57-90 |
| 5.9.5 | AMF Name | clauses/5.9.md | 91-94 |
| 5.9.6 | Data Network Name (DNN) | clauses/5.9.md | 95-110 |
| 5.9.7 | Internal-Group Identifier | clauses/5.9.md | 111-122 |
| 5.9.8 | Generic Public Subscription Identifier | clauses/5.9.md | 123-132 |
| 5.9.9 | AMF UE NGAP ID | clauses/5.9.md | 133-136 |
| 5.9.10 | UE Radio Capability ID | clauses/5.9.md | 137-148 |
| 5.10 | Security aspects | clauses/5.10.md | 1-118 |
| 5.10.1 | General | clauses/5.10.md | 3-20 |
| 5.10.2 | Security Model for non-3GPP access | clauses/5.10.md | 21-26 |
| 5.10.2.1 | Signalling Security | clauses/5.10.md | 23-26 |
| 5.10.3 | PDU Session User Plane Security | clauses/5.10.md | 27-118 |
| 5.11 | Support for Dual Connectivity, Multi-Connectivity | clauses/5.11.md | 1-32 |
| 5.11.1 | Support for Dual Connectivity | clauses/5.11.md | 3-32 |
| 5.12 | Charging | clauses/5.12.md | 1-40 |
| 5.12.1 | General | clauses/5.12.md | 3-14 |
| 5.12.2 | Usage Data Reporting for Secondary RAT | clauses/5.12.md | 15-36 |
| 5.12.3 | Secondary RAT Periodic Usage Data Reporting Procedure | clauses/5.12.md | 37-40 |
| 5.13 | Support for Edge Computing | clauses/5.13.md | 1-46 |
| 5.14 | Policy Control | clauses/5.14.md | 1-4 |
| 5.15 | Network slicing | clauses/5.15.md | 1-1 |
| 5.15.1 | General | clauses/5.15.1.md | 1-54 |
| 5.15.2 | Identification and selection of a Network Slice: the S-NSSAI and the NSSAI | clauses/5.15.2.md | 1-59 |
| 5.15.2.1 | General | clauses/5.15.2.md | 3-38 |
| 5.15.2.2 | Standardised SST values | clauses/5.15.2.md | 39-59 |
| 5.15.3 | Subscription aspects | clauses/5.15.3.md | 1-30 |
| 5.15.4 | UE NSSAI configuration and NSSAI storage aspects | clauses/5.15.4.md | 1-132 |
| 5.15.4.1 | General | clauses/5.15.4.md | 3-110 |
| 5.15.4.1.1 | UE Network Slice configuration | clauses/5.15.4.md | 5-98 |
| 5.15.4.1.2 | Mapping of S-NSSAIs values in the Allowed NSSAI and in the Requested NSSAI to the S-NSSAIs values used in the HPLMN | clauses/5.15.4.md | 99-110 |
| 5.15.4.2 | Update of UE Network Slice configuration | clauses/5.15.4.md | 111-132 |
| 5.15.5 | Detailed Operation Overview | clauses/5.15.5.md | 1-244 |
| 5.15.5.1 | General | clauses/5.15.5.md | 3-10 |
| 5.15.5.2 | Selection of a Serving AMF supporting the Network Slices | clauses/5.15.5.md | 11-208 |
| 5.15.5.2.1 | Registration to a set of Network Slices | clauses/5.15.5.md | 13-142 |
| 5.15.5.2.2 | Modification of the Set of Network Slice(s) for a UE | clauses/5.15.5.md | 143-198 |
| 5.15.5.2.3 | AMF Re-allocation due to Network Slice(s) Support | clauses/5.15.5.md | 199-208 |
| 5.15.5.3 | Establishing a PDU Session in a Network Slice | clauses/5.15.5.md | 209-244 |
| 5.15.6 | Network Slicing Support for Roaming | clauses/5.15.6.md | 1-38 |
| 5.15.7 | Network slicing and Interworking with EPS | clauses/5.15.7.md | 1-40 |
| 5.15.7.1 | General | clauses/5.15.7.md | 3-14 |
| 5.15.7.2 | Idle mode aspects | clauses/5.15.7.md | 15-28 |
| 5.15.7.3 | Connected mode aspects | clauses/5.15.7.md | 29-36 |
| 5.15.7.4 | Support of Network Slice usage control and Interworking with EPC | clauses/5.15.7.md | 37-40 |
| 5.15.8 | Configuration of Network Slice support and availability in a PLMN | clauses/5.15.8.md | 1-18 |
| 5.15.9 | Operator-controlled inclusion of NSSAI in Access Stratum Connection Establishment | clauses/5.15.9.md | 1-34 |
| 5.15.10 | Network Slice-Specific Authentication and Authorization | clauses/5.15.10.md | 1-40 |
| 5.15.11 | Network Slice Admission Control | clauses/5.15.11.md | 1-264 |
| 5.15.11.0 | General | clauses/5.15.11.md | 3-46 |
| 5.15.11.1 | Network Slice Admission Control for maximum number of UEs | clauses/5.15.11.md | 47-94 |
| 5.15.11.1.1 | Non-Hierarchical NSAC architecture | clauses/5.15.11.md | 49-60 |
| 5.15.11.1.2 | Hierarchical NSAC architecture | clauses/5.15.11.md | 61-88 |
| 5.15.11.1.3 | Centralized NSAC architecture | clauses/5.15.11.md | 89-94 |
| 5.15.11.2 | Network Slice Admission Control for maximum number of PDU sessions | clauses/5.15.11.md | 95-130 |
| 5.15.11.2.1 | Non- Hierarchical NSAC architecture | clauses/5.15.11.md | 97-108 |
| 5.15.11.2.2 | Hierarchical NSAC architecture | clauses/5.15.11.md | 109-124 |
| 5.15.11.2.3 | Centralized NSAC architecture | clauses/5.15.11.md | 125-130 |
| 5.15.11.3 | Network Slice Admission Control for Roaming | clauses/5.15.11.md | 131-184 |
| 5.15.11.3.0 | General | clauses/5.15.11.md | 133-148 |
| 5.15.11.3.1 | VPLMN NSAC Admission Mode | clauses/5.15.11.md | 149-164 |
| 5.15.11.3.2 | VPLMN with HPLMN assistance NSAC Admission | clauses/5.15.11.md | 165-174 |
| 5.15.11.3.3 | HPLMN NSAC Admission Mode | clauses/5.15.11.md | 175-184 |
| 5.15.11.4 | Network Slice status notifications and reports to a consumer NF | clauses/5.15.11.md | 185-190 |
| 5.15.11.5 | Support of Network Slice Admission Control and Interworking with EPC | clauses/5.15.11.md | 191-236 |
| 5.15.11.5a | Support of Network Slice Admission Control in 5GS for maximum number of UEs with at least one PDU Session/PDN Connection | clauses/5.15.11.md | 237-264 |
| 5.15.12 | Support of subscription-based restrictions to simultaneous registration of network slices | clauses/5.15.12.md | 1-46 |
| 5.15.12.1 | General | clauses/5.15.12.md | 3-20 |
| 5.15.12.2 | UE and UE configuration aspects | clauses/5.15.12.md | 21-46 |
| 5.15.13 | Support of data rate limitation per Network Slice for a UE | clauses/5.15.13.md | 1-12 |
| 5.15.14 | Network Slice AS Groups support | clauses/5.15.14.md | 1-26 |
| 5.15.15 | Support of Network Slice usage control | clauses/5.15.15.md | 1-72 |
| 5.15.15.1 | General | clauses/5.15.15.md | 3-14 |
| 5.15.15.2 | UE Configuration of network-controlled Slice Usage Policy | clauses/5.15.15.md | 15-46 |
| 5.15.15.3 | Network-based per UE Network Slice usage behaviour control | clauses/5.15.15.md | 47-72 |
| 5.15.16 | Optimized handling of temporarily available network slices | clauses/5.15.16.md | 1-58 |
| 5.15.17 | Partial Network Slice support in a Registration Area | clauses/5.15.17.md | 1-62 |
| 5.15.18 | Support for Network Slices with Network Slice Area of Service not matching deployed Tracking Areas | clauses/5.15.18.md | 1-66 |
| 5.15.18.1 | General | clauses/5.15.18.md | 3-12 |
| 5.15.18.2 | S-NSSAI location availability information | clauses/5.15.18.md | 13-38 |
| 5.15.18.3 | Network based monitoring and enforcement of Network Slice Area of Service not matching deployed Tracking Areas | clauses/5.15.18.md | 39-66 |
| 5.15.19 | Support of Network Slice Replacement | clauses/5.15.19.md | 1-88 |
| 5.15.20 | Support of Network Slice Instance Replacement | clauses/5.15.20.md | 1-4 |
| 5.16 | Support for specific services | clauses/5.16.md | 1-546 |
| 5.16.1 | Public Warning System | clauses/5.16.md | 3-6 |
| 5.16.2 | SMS over NAS | clauses/5.16.md | 7-30 |
| 5.16.2.1 | General | clauses/5.16.md | 9-22 |
| 5.16.2.2 | SMS over NAS transport | clauses/5.16.md | 23-30 |
| 5.16.3 | IMS support | clauses/5.16.md | 31-252 |
| 5.16.3.1 | General | clauses/5.16.md | 33-58 |
| 5.16.3.2 | IMS voice over PS Session Supported Indication over 3GPP access | clauses/5.16.md | 59-92 |
| 5.16.3.2a | IMS voice over PS Session Supported Indication over non-3GPP access | clauses/5.16.md | 93-98 |
| 5.16.3.3 | Homogeneous support for IMS voice over PS Session supported indication | clauses/5.16.md | 99-116 |
| 5.16.3.4 | P-CSCF address delivery | clauses/5.16.md | 117-126 |
| 5.16.3.5 | Domain selection for UE originating sessions / calls | clauses/5.16.md | 127-152 |
| 5.16.3.6 | Terminating domain selection for IMS voice | clauses/5.16.md | 153-166 |
| 5.16.3.7 | UE's usage setting | clauses/5.16.md | 167-174 |
| 5.16.3.8 | Domain and Access Selection for UE originating SMS | clauses/5.16.md | 175-194 |
| 5.16.3.8.1 | UE originating SMS for IMS Capable UEs supporting SMS over IP | clauses/5.16.md | 177-184 |
| 5.16.3.8.2 | Access Selection for SMS over NAS | clauses/5.16.md | 185-194 |
| 5.16.3.9 | SMF support for P-CSCF restoration procedure | clauses/5.16.md | 195-198 |
| 5.16.3.10 | IMS Voice Service via EPS Fallback or RAT fallback in 5GS | clauses/5.16.md | 199-224 |
| 5.16.3.11 | P-CSCF discovery and selection | clauses/5.16.md | 225-248 |
| 5.16.3.12 | HSS discovery and selection | clauses/5.16.md | 249-252 |
| 5.16.4 | Emergency Services | clauses/5.16.md | 253-448 |
| 5.16.4.1 | Introduction | clauses/5.16.md | 255-348 |
| 5.16.4.2 | Architecture Reference Model for Emergency Services | clauses/5.16.md | 349-352 |
| 5.16.4.3 | Mobility Restrictions and Access Restrictions for Emergency Services | clauses/5.16.md | 353-364 |
| 5.16.4.4 | Reachability Management | clauses/5.16.md | 365-370 |
| 5.16.4.5 | SMF and UPF selection function for Emergency Services | clauses/5.16.md | 371-374 |
| 5.16.4.6 | QoS for Emergency Services | clauses/5.16.md | 375-380 |
| 5.16.4.7 | PCC for Emergency Services | clauses/5.16.md | 381-386 |
| 5.16.4.8 | IP Address Allocation | clauses/5.16.md | 387-390 |
| 5.16.4.9 | Handling of PDU Sessions for Emergency Services | clauses/5.16.md | 391-402 |
| 5.16.4.9a | Handling of PDU Sessions for normal services for Emergency Registered UEs | clauses/5.16.md | 403-412 |
| 5.16.4.10 | Support of eCall Only Mode | clauses/5.16.md | 413-424 |
| 5.16.4.11 | Emergency Services Fallback | clauses/5.16.md | 425-448 |
| 5.16.5 | Multimedia Priority Services | clauses/5.16.md | 449-512 |
| 5.16.6 | Mission Critical Services | clauses/5.16.md | 513-546 |
| 5.17 | Interworking and Migration | clauses/5.17.md | 1-592 |
| 5.17.1 | Support for Migration from EPC to 5GC | clauses/5.17.md | 3-74 |
| 5.17.1.1 | General | clauses/5.17.md | 5-56 |
| 5.17.1.2 | User Plane management to support interworking with EPS | clauses/5.17.md | 57-70 |
| 5.17.1.3 | QoS handling for home routed roaming | clauses/5.17.md | 71-74 |
| 5.17.2 | Interworking with EPC | clauses/5.17.md | 75-410 |
| 5.17.2.1 | General | clauses/5.17.md | 77-182 |
| 5.17.2.2 | Interworking Procedures with N26 interface | clauses/5.17.md | 183-240 |
| 5.17.2.2.1 | General | clauses/5.17.md | 185-212 |
| 5.17.2.2.2 | Mobility for UEs in single-registration mode | clauses/5.17.md | 213-240 |
| 5.17.2.3 | Interworking Procedures without N26 interface | clauses/5.17.md | 241-352 |
| 5.17.2.3.1 | General | clauses/5.17.md | 243-270 |
| 5.17.2.3.2 | Mobility for UEs in single-registration mode | clauses/5.17.md | 271-304 |
| 5.17.2.3.3 | Mobility for UEs in dual-registration mode | clauses/5.17.md | 305-344 |
| 5.17.2.3.4 | Redirection for UEs in connected state | clauses/5.17.md | 345-352 |
| 5.17.2.4 | Mobility between 5GS and GERAN/UTRAN | clauses/5.17.md | 353-394 |
| 5.17.2.5 | Secondary DN authentication and authorization in EPS Interworking case | clauses/5.17.md | 395-410 |
| 5.17.3 | Interworking with EPC in presence of Non-3GPP PDU Sessions | clauses/5.17.md | 411-420 |
| 5.17.4 | Network sharing support and interworking between EPS and 5GS | clauses/5.17.md | 421-424 |
| 5.17.5 | Service Exposure in Interworking Scenarios | clauses/5.17.md | 425-494 |
| 5.17.5.1 | General | clauses/5.17.md | 427-460 |
| 5.17.5.2 | Support of interworking for Monitoring Events | clauses/5.17.md | 461-478 |
| 5.17.5.2.1 | Interworking with N26 interface | clauses/5.17.md | 463-470 |
| 5.17.5.2.2 | Interworking without N26 interface | clauses/5.17.md | 471-478 |
| 5.17.5.3 | Availability or expected level of a service API | clauses/5.17.md | 479-494 |
| 5.17.6 | Void | clauses/5.17.md | 495-496 |
| 5.17.7 | Configuration Transfer Procedure between NG-RAN and E-UTRAN | clauses/5.17.md | 497-542 |
| 5.17.7.1 | Architecture Principles for Configuration Transfer between NG-RAN and E-UTRAN | clauses/5.17.md | 499-516 |
| 5.17.7.2 | Addressing, routing and relaying | clauses/5.17.md | 517-542 |
| 5.17.7.2.1 | Addressing | clauses/5.17.md | 519-526 |
| 5.17.7.2.2 | Routing | clauses/5.17.md | 527-536 |
| 5.17.7.2.3 | Relaying | clauses/5.17.md | 537-542 |
| 5.17.8 | URSP Provisioning in EPS | clauses/5.17.md | 543-592 |
| 5.18 | Network Sharing | clauses/5.18.md | 1-99 |
| 5.18.1 | General concepts | clauses/5.18.md | 3-33 |
| 5.18.2 | Broadcast system information for network sharing | clauses/5.18.md | 34-43 |
| 5.18.2a | PLMN list and SNPN list handling for network sharing | clauses/5.18.md | 44-55 |
| 5.18.3 | Network selection by the UE | clauses/5.18.md | 56-69 |
| 5.18.4 | Network selection by the network | clauses/5.18.md | 70-95 |
| 5.18.5 | Network Sharing and Network Slicing | clauses/5.18.md | 96-99 |
| 5.19 | Control Plane Load Control, Congestion and Overload Control | clauses/5.19.md | 1-276 |
| 5.19.1 | General | clauses/5.19.md | 3-6 |
| 5.19.2 | TNLA Load Balancing and TNLA Load Re-Balancing | clauses/5.19.md | 7-10 |
| 5.19.3 | AMF Load Balancing | clauses/5.19.md | 11-24 |
| 5.19.4 | AMF Load Re-Balancing | clauses/5.19.md | 25-44 |
| 5.19.5 | AMF Control Of Overload | clauses/5.19.md | 45-90 |
| 5.19.5.1 | General | clauses/5.19.md | 47-54 |
| 5.19.5.2 | AMF Overload Control | clauses/5.19.md | 55-90 |
| 5.19.6 | SMF Overload Control | clauses/5.19.md | 91-100 |
| 5.19.7 | NAS level congestion control | clauses/5.19.md | 101-276 |
| 5.19.7.1 | General | clauses/5.19.md | 103-110 |
| 5.19.7.2 | General NAS level congestion control | clauses/5.19.md | 111-146 |
| 5.19.7.3 | DNN based congestion control | clauses/5.19.md | 147-192 |
| 5.19.7.4 | S-NSSAI based congestion control | clauses/5.19.md | 193-246 |
| 5.19.7.5 | Group specific NAS level congestion control | clauses/5.19.md | 247-252 |
| 5.19.7.6 | Control Plane data specific NAS level congestion control | clauses/5.19.md | 253-276 |
| 5.20 | External Exposure of Network Capability | clauses/5.20.md | 1-50 |
| 5.20a | Data Collection from an AF | clauses/5.20a.md | 1-8 |
| 5.20b | Support exposure of DNN and S-NSSAI specific Group Parameters | clauses/5.20b.md | 1-36 |
| 5.20c | Provisioning of traffic characteristics and monitoring of performance characteristics for a group | clauses/5.20c.md | 1-30 |
| 5.20d | User Plane Direct 5GS Information Exposure | clauses/5.20d.md | 1-18 |
| 5.21 | Architectural support for virtualized deployments | clauses/5.21.md | 1-266 |
| 5.21.0 | General | clauses/5.21.md | 3-20 |
| 5.21.1 | Architectural support for N2 | clauses/5.21.md | 21-54 |
| 5.21.1.1 | TNL associations | clauses/5.21.md | 23-34 |
| 5.21.1.2 | NGAP UE-TNLA-binding | clauses/5.21.md | 35-44 |
| 5.21.1.3 | N2 TNL association selection | clauses/5.21.md | 45-54 |
| 5.21.2 | AMF Management | clauses/5.21.md | 55-214 |
| 5.21.2.1 | AMF Addition/Update | clauses/5.21.md | 57-72 |
| 5.21.2.2 | AMF planned removal procedure | clauses/5.21.md | 73-164 |
| 5.21.2.2.1 | AMF planned removal procedure with UDSF deployed | clauses/5.21.md | 75-122 |
| 5.21.2.2.2 | AMF planned removal procedure without UDSF | clauses/5.21.md | 123-164 |
| 5.21.2.3 | Procedure for AMF Auto-recovery | clauses/5.21.md | 165-214 |
| 5.21.3 | Network Reliability support with Sets | clauses/5.21.md | 215-258 |
| 5.21.3.1 | General | clauses/5.21.md | 217-224 |
| 5.21.3.2 | NF Set and NF Service Set | clauses/5.21.md | 225-240 |
| 5.21.3.3 | Reliability of NF instances within the same NF Set | clauses/5.21.md | 241-250 |
| 5.21.3.4 | Reliability of NF Services | clauses/5.21.md | 251-258 |
| 5.21.4 | Network Function/NF Service Context Transfer | clauses/5.21.md | 259-266 |
| 5.21.4.1 | General | clauses/5.21.md | 261-266 |
| 5.22 | System Enablers for priority mechanism | clauses/5.22.md | 1-104 |
| 5.22.1 | General | clauses/5.22.md | 3-18 |
| 5.22.2 | Subscription-related Priority Mechanisms | clauses/5.22.md | 19-40 |
| 5.22.3 | Invocation-related Priority Mechanisms | clauses/5.22.md | 41-88 |
| 5.22.4 | QoS Mechanisms applied to established QoS Flows | clauses/5.22.md | 89-104 |
| 5.23 | Supporting for Asynchronous Type Communication | clauses/5.23.md | 1-14 |
| 5.24 | 3GPP PS Data Off | clauses/5.24.md | 1-20 |
| 5.25 | Support of OAM Features | clauses/5.25.md | 1-42 |
| 5.25.1 | Support of Tracing: Signalling Based Activation/Deactivation of Tracing | clauses/5.25.md | 3-28 |
| 5.25.2 | Support of OAM-based 5G VN group management | clauses/5.25.md | 29-36 |
| 5.25.3 | Signalling Based Activation of QoE Measurement Collection | clauses/5.25.md | 37-42 |
| 5.26 | Configuration Transfer Procedure | clauses/5.26.md | 1-38 |
| 5.26.1 | Architecture Principles for Configuration Transfer | clauses/5.26.md | 5-20 |
| 5.26.2 | Addressing, routing and relaying | clauses/5.26.md | 21-38 |
| 5.26.2.1 | Addressing | clauses/5.26.md | 23-26 |
| 5.26.2.2 | Routing | clauses/5.26.md | 27-34 |
| 5.26.2.3 | Relaying | clauses/5.26.md | 35-38 |
| 5.27 | Enablers for Time Sensitive Communications, Time Synchronization and Deterministic Networking | clauses/5.27.md | 1-818 |
| 5.27.0 | General | clauses/5.27.md | 3-26 |
| 5.27.1 | Time Synchronization | clauses/5.27.md | 27-584 |
| 5.27.1.1 | General | clauses/5.27.md | 29-74 |
| 5.27.1.2 | Distribution of timing information | clauses/5.27.md | 75-178 |
| 5.27.1.2.1 | Distribution of 5G internal system clock | clauses/5.27.md | 77-80 |
| 5.27.1.2.2 | Distribution of grandmaster clock and time-stamping | clauses/5.27.md | 81-178 |
| 5.27.1.2.2.1 | Distribution of gPTP Sync and FollowUp messages | clauses/5.27.md | 83-132 |
| 5.27.1.2.2.2 | Distribution of PTP Sync and FollowUp messages | clauses/5.27.md | 133-178 |
| 5.27.1.3 | Support for multiple (g)PTP domains | clauses/5.27.md | 179-194 |
| 5.27.1.4 | DS-TT and NW-TT Time Synchronization functionality | clauses/5.27.md | 195-236 |
| 5.27.1.5 | Detection of (g)PTP Sync and Announce timeouts | clauses/5.27.md | 237-246 |
| 5.27.1.6 | Distribution of Announce messages and best master clock selection | clauses/5.27.md | 247-280 |
| 5.27.1.7 | Support for PTP grandmaster function in 5GS | clauses/5.27.md | 281-298 |
| 5.27.1.8 | Exposure of Time Synchronization | clauses/5.27.md | 299-340 |
| 5.27.1.9 | Support for derivation of Uu time synchronization error budget | clauses/5.27.md | 341-366 |
| 5.27.1.10 | Support for coverage area filters for time synchronization service | clauses/5.27.md | 367-392 |
| 5.27.1.11 | Controlling time synchronization service based on the Subscription | clauses/5.27.md | 393-492 |
| 5.27.1.12 | Support for network timing synchronization status monitoring | clauses/5.27.md | 493-584 |
| 5.27.1a | Periodic deterministic communication | clauses/5.27.md | 585-594 |
| 5.27.2 | TSC Assistance Information (TSCAI) and TSC Assistance Container (TSCAC) | clauses/5.27.md | 595-772 |
| 5.27.2.1 | General | clauses/5.27.md | 597-640 |
| 5.27.2.2 | TSC Assistance Container determination based on PSFP | clauses/5.27.md | 641-664 |
| 5.27.2.3 | TSC Assistance Container determination by TSCTSF | clauses/5.27.md | 665-682 |
| 5.27.2.4 | TSCAI determination based on TSC Assistance Container | clauses/5.27.md | 683-724 |
| 5.27.2.5 | RAN feedback for Burst Arrival Time offset and adjusted Periodicity | clauses/5.27.md | 725-772 |
| 5.27.2.5.1 | Overview | clauses/5.27.md | 727-738 |
| 5.27.2.5.2 | Proactive RAN feedback for adaptation of Burst Arrival Time and Periodicity | clauses/5.27.md | 739-762 |
| 5.27.2.5.3 | Reactive RAN feedback for Burst Arrival Time adaptation | clauses/5.27.md | 763-772 |
| 5.27.3 | Support for TSC QoS Flows | clauses/5.27.md | 773-790 |
| 5.27.4 | Hold and Forward Buffering mechanism | clauses/5.27.md | 791-800 |
| 5.27.5 | 5G System Bridge delay | clauses/5.27.md | 801-818 |
| 5.28 | Support of integration with TSN, Time Sensitive Communications, Time Synchronization and Deterministic Networking | clauses/5.28.md | 1-338 |
| 5.28.0 | General | clauses/5.28.md | 3-10 |
| 5.28.1 | 5GS bridge management for TSN | clauses/5.28.md | 11-100 |
| 5.28.2 | 5GS Bridge configuration for TSN | clauses/5.28.md | 101-156 |
| 5.28.3 | Port and user plane node management information exchange in 5GS | clauses/5.28.md | 157-236 |
| 5.28.3.1 | General | clauses/5.28.md | 159-208 |
| 5.28.3.2 | Transfer of port or user plane node management information | clauses/5.28.md | 209-230 |
| 5.28.3.3 | VLAN Configuration Information for TSN | clauses/5.28.md | 231-236 |
| 5.28.4 | QoS mapping tables for TSN | clauses/5.28.md | 237-266 |
| 5.28.5 | Support of integration with IETF Deterministic Networking | clauses/5.28.md | 267-338 |
| 5.28.5.1 | General | clauses/5.28.md | 269-288 |
| 5.28.5.2 | 5GS DetNet node reporting | clauses/5.28.md | 289-310 |
| 5.28.5.3 | DetNet node configuration mapping in 5GS | clauses/5.28.md | 311-338 |
| 5.28a | Support for TSN enabled Transport Network | clauses/5.28a.md | 1-80 |
| 5.29 | Support for 5G LAN-type service | clauses/5.29.md | 1-150 |
| 5.29.1 | General | clauses/5.29.md | 3-8 |
| 5.29.2 | 5G VN group management | clauses/5.29.md | 9-72 |
| 5.29.3 | PDU Session management | clauses/5.29.md | 73-114 |
| 5.29.4 | User Plane handling | clauses/5.29.md | 115-150 |
| 5.30 | Support for non-public networks | clauses/5.30.md | 1-916 |
| 5.30.1 | General | clauses/5.30.md | 3-14 |
| 5.30.2 | Stand-alone Non-Public Networks | clauses/5.30.md | 15-782 |
| 5.30.2.0 | General | clauses/5.30.md | 17-58 |
| 5.30.2.1 | Identifiers | clauses/5.30.md | 59-92 |
| 5.30.2.2 | Broadcast system information | clauses/5.30.md | 93-120 |
| 5.30.2.3 | UE configuration and subscription aspects | clauses/5.30.md | 121-242 |
| 5.30.2.4 | Network selection in SNPN access mode | clauses/5.30.md | 243-340 |
| 5.30.2.4.1 | General | clauses/5.30.md | 245-262 |
| 5.30.2.4.2 | Automatic network selection | clauses/5.30.md | 263-332 |
| 5.30.2.4.3 | Manual network selection | clauses/5.30.md | 333-340 |
| 5.30.2.5 | Network access control | clauses/5.30.md | 341-352 |
| 5.30.2.6 | Cell (re-)selection in SNPN access mode | clauses/5.30.md | 353-358 |
| 5.30.2.7 | Access to PLMN services via stand-alone non-public networks | clauses/5.30.md | 359-372 |
| 5.30.2.8 | Access to stand-alone non-public network services via PLMN | clauses/5.30.md | 373-386 |
| 5.30.2.9 | SNPN connectivity for UEs with credentials owned by Credentials Holder | clauses/5.30.md | 387-440 |
| 5.30.2.9.1 | General | clauses/5.30.md | 389-396 |
| 5.30.2.9.2 | Credentials Holder using AAA Server for primary authentication and authorization | clauses/5.30.md | 397-424 |
| 5.30.2.9.3 | Credentials Holder using AUSF and UDM for primary authentication and authorization | clauses/5.30.md | 425-440 |
| 5.30.2.10 | Onboarding of UEs for SNPNs | clauses/5.30.md | 441-674 |
| 5.30.2.10.1 | General | clauses/5.30.md | 443-456 |
| 5.30.2.10.2 | Onboarding Network is an SNPN | clauses/5.30.md | 457-588 |
| 5.30.2.10.2.1 | General | clauses/5.30.md | 459-462 |
| 5.30.2.10.2.2 | Architecture | clauses/5.30.md | 463-508 |
| 5.30.2.10.2.3 | Broadcast system information | clauses/5.30.md | 509-516 |
| 5.30.2.10.2.4 | UE Configuration Aspects | clauses/5.30.md | 517-530 |
| 5.30.2.10.2.5 | Network selection | clauses/5.30.md | 531-540 |
| 5.30.2.10.2.6 | Registration for UE onboarding | clauses/5.30.md | 541-576 |
| 5.30.2.10.2.7 | Deregistration from the ON-SNPN for onboarding registered UE | clauses/5.30.md | 577-588 |
| 5.30.2.10.3 | Onboarding Network is a PLMN | clauses/5.30.md | 589-602 |
| 5.30.2.10.3.1 | General | clauses/5.30.md | 591-594 |
| 5.30.2.10.3.2 | Network selection and Registration | clauses/5.30.md | 595-602 |
| 5.30.2.10.4 | Remote Provisioning of UEs in Onboarding Network | clauses/5.30.md | 603-674 |
| 5.30.2.10.4.1 | General | clauses/5.30.md | 605-610 |
| 5.30.2.10.4.2 | Onboarding configuration for the UE | clauses/5.30.md | 611-634 |
| 5.30.2.10.4.3 | User Plane Remote Provisioning of UEs when Onboarding Network is an ON-SNPN | clauses/5.30.md | 635-654 |
| 5.30.2.10.4.4 | User Plane Remote Provisioning of UEs when Onboarding Network is a PLMN | clauses/5.30.md | 655-674 |
| 5.30.2.11 | UE Mobility support for SNPN | clauses/5.30.md | 675-686 |
| 5.30.2.12 | Access to SNPN services via Untrusted non-3GPP access | clauses/5.30.md | 687-738 |
| 5.30.2.13 | Access to SNPN services via Trusted non-3GPP access | clauses/5.30.md | 739-764 |
| 5.30.2.14 | Access to SNPN services via wireline access network | clauses/5.30.md | 765-768 |
| 5.30.2.15 | Access to SNPN services for N5CW devices | clauses/5.30.md | 769-782 |
| 5.30.3 | Public Network Integrated NPN | clauses/5.30.md | 783-916 |
| 5.30.3.1 | General | clauses/5.30.md | 785-806 |
| 5.30.3.2 | Identifiers | clauses/5.30.md | 807-820 |
| 5.30.3.3 | UE configuration, subscription aspects and storage | clauses/5.30.md | 821-848 |
| 5.30.3.4 | Network and cell (re-)selection and access control | clauses/5.30.md | 849-904 |
| 5.30.3.5 | Support of emergency services in CAG cells | clauses/5.30.md | 905-916 |
| 5.31 | Support for Cellular IoT | clauses/5.31.md | 1-640 |
| 5.31.1 | General | clauses/5.31.md | 3-16 |
| 5.31.2 | Preferred and Supported Network Behaviour | clauses/5.31.md | 17-58 |
| 5.31.3 | Selection, steering and redirection between EPS and 5GS | clauses/5.31.md | 59-78 |
| 5.31.4 | Control Plane CIoT 5GS Optimisation | clauses/5.31.md | 79-136 |
| 5.31.4.1 | General | clauses/5.31.md | 81-120 |
| 5.31.4.2 | Establishment of N3 data transfer during Data Transport in Control Plane CIoT 5GS Optimisation | clauses/5.31.md | 121-126 |
| 5.31.4.3 | Control Plane Relocation Indication procedure | clauses/5.31.md | 127-136 |
| 5.31.5 | Non-IP Data Delivery (NIDD) | clauses/5.31.md | 137-154 |
| 5.31.6 | Reliable Data Service | clauses/5.31.md | 155-170 |
| 5.31.7 | Power Saving Enhancements | clauses/5.31.md | 171-316 |
| 5.31.7.1 | General | clauses/5.31.md | 173-188 |
| 5.31.7.2 | Extended Discontinuous Reception (DRX) for CM-IDLE and CM-CONNECTED with RRC-INACTIVE | clauses/5.31.md | 189-280 |
| 5.31.7.2.1 | Overview | clauses/5.31.md | 191-230 |
| 5.31.7.2.2 | Paging for extended idle mode DRX in E-UTRA and NR connected to 5GC | clauses/5.31.md | 231-266 |
| 5.31.7.2.2.0 | General | clauses/5.31.md | 233-240 |
| 5.31.7.2.2.1 | Hyper SFN, Paging Hyperframe and Paging Time Window length | clauses/5.31.md | 241-246 |
| 5.31.7.2.2.2 | Loose Hyper SFN synchronization | clauses/5.31.md | 247-256 |
| 5.31.7.2.2.3 | AMF paging and paging retransmission strategy | clauses/5.31.md | 257-266 |
| 5.31.7.2.3 | Paging for a UE registered in a tracking area with heterogeneous support of extended idle mode DRX | clauses/5.31.md | 267-272 |
| 5.31.7.2.4 | Paging for extended DRX for RRCINACTIVE in NR connected to 5GC | clauses/5.31.md | 273-280 |
| 5.31.7.3 | MICO mode with Extended Connected Time | clauses/5.31.md | 281-292 |
| 5.31.7.4 | MICO mode with Active Time | clauses/5.31.md | 293-304 |
| 5.31.7.5 | MICO mode and Periodic Registration Timer Control | clauses/5.31.md | 305-316 |
| 5.31.8 | High latency communication | clauses/5.31.md | 317-344 |
| 5.31.9 | Support for Monitoring Events | clauses/5.31.md | 345-352 |
| 5.31.10 | NB-IoT UE Radio Capability Handling | clauses/5.31.md | 353-356 |
| 5.31.11 | Inter-RAT idle mode mobility to and from NB-IoT | clauses/5.31.md | 357-382 |
| 5.31.12 | Restriction of use of Enhanced Coverage | clauses/5.31.md | 383-414 |
| 5.31.13 | Paging for Enhanced Coverage | clauses/5.31.md | 415-426 |
| 5.31.14 | Support of rate control of user data | clauses/5.31.md | 427-498 |
| 5.31.14.1 | General | clauses/5.31.md | 429-444 |
| 5.31.14.2 | Serving PLMN Rate Control | clauses/5.31.md | 445-464 |
| 5.31.14.3 | Small Data Rate Control | clauses/5.31.md | 465-498 |
| 5.31.15 | Control Plane Data Transfer Congestion Control | clauses/5.31.md | 499-502 |
| 5.31.16 | Service Gap Control | clauses/5.31.md | 503-558 |
| 5.31.17 | Inter-UE QoS for NB-IoT | clauses/5.31.md | 559-564 |
| 5.31.18 | User Plane CIoT 5GS Optimisation | clauses/5.31.md | 565-610 |
| 5.31.19 | QoS model for NB-IoT | clauses/5.31.md | 611-624 |
| 5.31.20 | Category M UEs differentiation | clauses/5.31.md | 625-640 |
| 5.32 | Support for ATSSS | clauses/5.32.md | 1-859 |
| 5.32.1 | General | clauses/5.32.md | 3-46 |
| 5.32.2 | Multi Access PDU Sessions | clauses/5.32.md | 47-192 |
| 5.32.3 | Policy for ATSSS Control | clauses/5.32.md | 193-202 |
| 5.32.4 | QoS Support | clauses/5.32.md | 203-262 |
| 5.32.5 | Access Network Performance Measurements | clauses/5.32.md | 263-482 |
| 5.32.5.1 | General principles | clauses/5.32.md | 265-352 |
| 5.32.5.1a | Address of PMF messages | clauses/5.32.md | 353-384 |
| 5.32.5.2 | Round Trip Time Measurements | clauses/5.32.md | 385-396 |
| 5.32.5.2a | Packet Loss Rate Measurements | clauses/5.32.md | 397-420 |
| 5.32.5.3 | Access Availability/Unavailability Report | clauses/5.32.md | 421-430 |
| 5.32.5.4 | Protocol stack for user plane measurements and measurement reports | clauses/5.32.md | 431-450 |
| 5.32.5.5 | UE Assistance Operation | clauses/5.32.md | 451-466 |
| 5.32.5.6 | Suspend and Resume Traffic Duplication | clauses/5.32.md | 467-482 |
| 5.32.6 | Support of Steering Functionalities | clauses/5.32.md | 483-710 |
| 5.32.6.1 | General | clauses/5.32.md | 485-572 |
| 5.32.6.2 | High-Layer Steering Functionalities | clauses/5.32.md | 573-690 |
| 5.32.6.2.1 | MPTCP Functionality | clauses/5.32.md | 575-610 |
| 5.32.6.2.2 | MPQUIC Functionality | clauses/5.32.md | 611-690 |
| 5.32.6.2.2.1 | Supported Transport Modes | clauses/5.32.md | 677-690 |
| 5.32.6.3 | Low-Layer Steering Functionalities | clauses/5.32.md | 691-710 |
| 5.32.6.3.1 | ATSSS-LL Functionality | clauses/5.32.md | 693-710 |
| 5.32.7 | Interworking with EPS | clauses/5.32.md | 711-752 |
| 5.32.7.1 | General | clauses/5.32.md | 713-720 |
| 5.32.7.2 | Interworking with N26 Interface | clauses/5.32.md | 721-744 |
| 5.32.7.3 | Interworking without N26 Interface | clauses/5.32.md | 745-752 |
| 5.32.8 | ATSSS Rules | clauses/5.32.md | 753-859 |
| 5.33 | Support for Ultra Reliable Low Latency Communication | clauses/5.33.md | 1-212 |
| 5.33.1 | General | clauses/5.33.md | 3-16 |
| 5.33.2 | Redundant transmission for high reliability communication | clauses/5.33.md | 17-136 |
| 5.33.2.1 | Dual Connectivity based end to end Redundant User Plane Paths | clauses/5.33.md | 19-82 |
| 5.33.2.2 | Support of redundant transmission on N3/N9 interfaces | clauses/5.33.md | 83-122 |
| 5.33.2.3 | Support for redundant transmission at transport layer | clauses/5.33.md | 123-136 |
| 5.33.3 | QoS Monitoring for packet delay | clauses/5.33.md | 137-212 |
| 5.33.3.1 | General | clauses/5.33.md | 139-148 |
| 5.33.3.2 | Per QoS Flow per UE QoS Measurement | clauses/5.33.md | 149-178 |
| 5.33.3.3 | GTP-U Path Measurement | clauses/5.33.md | 179-212 |
| 5.34 | Support of deployments topologies with specific SMF Service Areas | clauses/5.34.md | 1-240 |
| 5.34.1 | General | clauses/5.34.md | 3-34 |
| 5.34.2 | Architecture | clauses/5.34.md | 35-68 |
| 5.34.2.1 | SBA architecture | clauses/5.34.md | 37-40 |
| 5.34.2.2 | Non-roaming architecture | clauses/5.34.md | 41-58 |
| 5.34.2.3 | Roaming architecture | clauses/5.34.md | 59-68 |
| 5.34.3 | I-SMF selection, V-SMF reselection | clauses/5.34.md | 69-108 |
| 5.34.4 | Usage of an UL Classifier for a PDU Session controlled by I-SMF | clauses/5.34.md | 109-120 |
| 5.34.5 | Usage of IPv6 multi-homing for a PDU Session controlled by I-SMF | clauses/5.34.md | 121-132 |
| 5.34.6 | Interaction between I-SMF and SMF for the support of traffic offload by UPF controlled by the I-SMF | clauses/5.34.md | 133-186 |
| 5.34.6.1 | General | clauses/5.34.md | 135-164 |
| 5.34.6.2 | N4 information sent from SMF to I-SMF for local traffic offload | clauses/5.34.md | 165-186 |
| 5.34.7 | Event Management | clauses/5.34.md | 187-210 |
| 5.34.7.1 | UE's Mobility Event Management | clauses/5.34.md | 189-198 |
| 5.34.7.2 | SMF event exposure service | clauses/5.34.md | 199-206 |
| 5.34.7.3 | AMF implicit subscription about events related with the PDU Session | clauses/5.34.md | 207-210 |
| 5.34.8 | Support for Cellular IoT | clauses/5.34.md | 211-222 |
| 5.34.9 | Support of the Deployment Topologies with specific SMF Service Areas feature within and between PLMN(s) | clauses/5.34.md | 223-234 |
| 5.34.10 | Support for 5G LAN-type service | clauses/5.34.md | 235-240 |
| 5.35 | Support for Integrated access and backhaul (IAB) | clauses/5.35.md | 1-98 |
| 5.35.1 | IAB architecture and functional entities | clauses/5.35.md | 3-48 |
| 5.35.2 | 5G System enhancements to support IAB | clauses/5.35.md | 49-68 |
| 5.35.3 | Data handling and QoS support with IAB | clauses/5.35.md | 69-78 |
| 5.35.4 | Mobility support with IAB | clauses/5.35.md | 79-82 |
| 5.35.5 | Charging support with IAB | clauses/5.35.md | 83-86 |
| 5.35.6 | IAB operation involving EPC | clauses/5.35.md | 87-98 |
| 5.35A | Support for Mobile Base Station Relay (MBSR) | clauses/5.35A.md | 1-128 |
| 5.36 | RIM Information Transfer | clauses/5.36.md | 1-6 |
| 5.37 | Support for high data rate low latency services, eXtended Reality (XR) and interactive media services | clauses/5.37.md | 1-270 |
| 5.37.1 | General | clauses/5.37.md | 3-20 |
| 5.37.2 | Policy control enhancements to support multi-modal services | clauses/5.37.md | 21-40 |
| 5.37.3 | Support of ECN marking for L4S to expose the congestion information | clauses/5.37.md | 41-88 |
| 5.37.3.1 | General | clauses/5.37.md | 43-60 |
| 5.37.3.2 | Support of ECN marking for L4S in NG-RAN | clauses/5.37.md | 61-72 |
| 5.37.3.3 | Support of ECN marking for L4S in PSA UPF | clauses/5.37.md | 73-88 |
| 5.37.4 | Network Exposure of 5GS information | clauses/5.37.md | 89-114 |
| 5.37.5 | PDU Set based Handling | clauses/5.37.md | 115-200 |
| 5.37.5.1 | General | clauses/5.37.md | 117-162 |
| 5.37.5.2 | PDU Set Information and Identification | clauses/5.37.md | 163-192 |
| 5.37.5.3 | Non-homogenous support of PDU set based handling in NG-RAN | clauses/5.37.md | 193-200 |
| 5.37.6 | UL/DL policy control based on round-trip latency requirement | clauses/5.37.md | 201-214 |
| 5.37.7 | 5GS Packet Delay Variation monitoring and reporting | clauses/5.37.md | 215-228 |
| 5.37.7.1 | General | clauses/5.37.md | 217-228 |
| 5.37.8 | UE power saving management | clauses/5.37.md | 229-270 |
| 5.37.8.1 | General | clauses/5.37.md | 231-242 |
| 5.37.8.2 | Periodicity and N6 Jitter Information associated with Periodicity | clauses/5.37.md | 243-260 |
| 5.37.8.3 | End of Data Burst Indication | clauses/5.37.md | 261-270 |
| 5.38 | Support for Multi-USIM UE | clauses/5.38.md | 1-90 |
| 5.38.1 | General | clauses/5.38.md | 3-26 |
| 5.38.2 | Connection Release | clauses/5.38.md | 27-38 |
| 5.38.3 | Paging Cause Indication for Voice Service | clauses/5.38.md | 39-52 |
| 5.38.4 | Reject Paging Request | clauses/5.38.md | 53-60 |
| 5.38.5 | Paging Restriction | clauses/5.38.md | 61-84 |
| 5.38.6 | Paging Timing Collision Control | clauses/5.38.md | 85-90 |
| 5.39 | Remote provisioning of credentials for NSSAA or secondary authentication/authorization | clauses/5.39.md | 1-20 |
| 5.39.1 | General | clauses/5.39.md | 3-8 |
| 5.39.2 | Configuration for the UE | clauses/5.39.md | 9-20 |
| 5.40 | Support of Disaster Roaming with Minimization of Service Interruption | clauses/5.40.md | 1-116 |
| 5.40.1 | General | clauses/5.40.md | 3-20 |
| 5.40.2 | UE configuration and provisioning for Disaster Roaming | clauses/5.40.md | 21-40 |
| 5.40.3 | Disaster Condition Notification and Determination | clauses/5.40.md | 41-50 |
| 5.40.4 | Registration for Disaster Roaming service | clauses/5.40.md | 51-72 |
| 5.40.5 | Handling when a Disaster Condition is no longer applicable | clauses/5.40.md | 73-98 |
| 5.40.6 | Prevention of signalling overload related to Disaster Condition and Disaster Roaming service | clauses/5.40.md | 99-116 |
| 5.41 | NR RedCap and NR eRedCap UEs differentiation | clauses/5.41.md | 1-20 |
| 5.42 | Support of Non-seamless WLAN offload | clauses/5.42.md | 1-30 |
| 5.43 | Support for 5G Satellite Backhaul | clauses/5.43.md | 1-102 |
| 5.43.1 | General | clauses/5.43.md | 3-8 |
| 5.43.2 | Edge Computing via UPF deployed on satellite | clauses/5.43.md | 9-32 |
| 5.43.3 | Local switch for UE-to-UE communications via UPF deployed on GEO satellite | clauses/5.43.md | 33-86 |
| 5.43.3.1 | General | clauses/5.43.md | 35-50 |
| 5.43.3.2 | Local switch with PSA UPF deployed on satellite | clauses/5.43.md | 51-64 |
| 5.43.3.3 | Local switching with UL CL/BP and local PSA UPF deployed on satellite | clauses/5.43.md | 65-86 |
| 5.43.4 | Reporting of satellite backhaul to SMF | clauses/5.43.md | 87-94 |
| 5.43.5 | QoS monitoring when dynamic Satellite Backhaul is used | clauses/5.43.md | 95-102 |
| 5.44 | Support of Personal IoT network service | clauses/5.44.md | 1-70 |
| 5.44.1 | General | clauses/5.44.md | 3-22 |
| 5.44.2 | UE policy delivery for PIN | clauses/5.44.md | 23-26 |
| 5.44.3 | Session management enhancement for PIN service support | clauses/5.44.md | 27-62 |
| 5.44.3.1 | PDU Session Establishment for PIN | clauses/5.44.md | 29-36 |
| 5.44.3.2 | Session management related policy control | clauses/5.44.md | 37-44 |
| 5.44.3.3 | Non-3GPP QoS Assistance Information | clauses/5.44.md | 45-52 |
| 5.44.3.4 | Non-3GPP delay budget between PINE and PEGC | clauses/5.44.md | 53-62 |
| 5.44.4 | Identifiers for PIN | clauses/5.44.md | 63-70 |
| 5.45 | QoS Monitoring | clauses/5.45.md | 1-70 |
| 5.45.1 | General | clauses/5.45.md | 3-40 |
| 5.45.2 | Packet delay monitoring | clauses/5.45.md | 41-46 |
| 5.45.3 | Congestion information monitoring | clauses/5.45.md | 47-62 |
| 5.45.4 | Data rate monitoring | clauses/5.45.md | 63-68 |
| 5.45.5 | Void | clauses/5.45.md | 69-70 |
| 5.46 | Assistance to AI/ML Operations in the Application Layer | clauses/5.46.md | 1-60 |
| 5.46.1 | General | clauses/5.46.md | 3-42 |
| 5.46.2 | Member UE selection assistance functionality for application operation | clauses/5.46.md | 43-60 |
| 5.47 | Support for Network Controlled Repeater (NCR) | clauses/5.47.md | 1-12 |
| 6 | Network Functions | clauses/6.md | 1-1 |
| 6.1 | General | clauses/6.1.md | 1-10 |
| 6.2 | Network Function Functional description | clauses/6.2.md | 1-1036 |
| 6.2.1 | AMF | clauses/6.2.md | 3-114 |
| 6.2.2 | SMF | clauses/6.2.md | 115-210 |
| 6.2.3 | UPF | clauses/6.2.md | 211-260 |
| 6.2.4 | PCF | clauses/6.2.md | 261-276 |
| 6.2.5 | NEF | clauses/6.2.md | 277-364 |
| 6.2.5.0 | NEF functionality | clauses/6.2.md | 279-360 |
| 6.2.5.1 | Support for CAPIF | clauses/6.2.md | 361-364 |
| 6.2.5a | Void | clauses/6.2.md | 365-366 |
| 6.2.6 | NRF | clauses/6.2.md | 367-576 |
| 6.2.6.1 | General | clauses/6.2.md | 369-402 |
| 6.2.6.2 | NF profile | clauses/6.2.md | 403-544 |
| 6.2.6.3 | SCP profile | clauses/6.2.md | 545-576 |
| 6.2.7 | UDM | clauses/6.2.md | 577-614 |
| 6.2.8 | AUSF | clauses/6.2.md | 615-622 |
| 6.2.9 | N3IWF | clauses/6.2.md | 623-650 |
| 6.2.9A | TNGF | clauses/6.2.md | 651-670 |
| 6.2.10 | AF | clauses/6.2.md | 671-694 |
| 6.2.11 | UDR | clauses/6.2.md | 695-712 |
| 6.2.12 | UDSF | clauses/6.2.md | 713-724 |
| 6.2.13 | SMSF | clauses/6.2.md | 725-742 |
| 6.2.14 | NSSF | clauses/6.2.md | 743-758 |
| 6.2.15 | 5G-EIR | clauses/6.2.md | 759-764 |
| 6.2.16 | LMF | clauses/6.2.md | 765-768 |
| 6.2.16A | GMLC | clauses/6.2.md | 769-772 |
| 6.2.17 | SEPP | clauses/6.2.md | 773-786 |
| 6.2.18 | Network Data Analytics Function (NWDAF) | clauses/6.2.md | 787-824 |
| 6.2.19 | SCP | clauses/6.2.md | 825-852 |
| 6.2.20 | W-AGF | clauses/6.2.md | 853-856 |
| 6.2.21 | UE radio Capability Management Function (UCMF) | clauses/6.2.md | 857-876 |
| 6.2.22 | TWIF | clauses/6.2.md | 877-880 |
| 6.2.23 | NSSAAF | clauses/6.2.md | 881-890 |
| 6.2.24 | DCCF | clauses/6.2.md | 891-910 |
| 6.2.25 | MFAF | clauses/6.2.md | 911-928 |
| 6.2.26 | ADRF | clauses/6.2.md | 929-938 |
| 6.2.27 | MB-SMF | clauses/6.2.md | 939-942 |
| 6.2.27a | MB-UPF | clauses/6.2.md | 943-946 |
| 6.2.27b | MBSF | clauses/6.2.md | 947-950 |
| 6.2.27c | MBSTF | clauses/6.2.md | 951-954 |
| 6.2.28 | NSACF | clauses/6.2.md | 955-976 |
| 6.2.29 | TSCTSF | clauses/6.2.md | 977-1012 |
| 6.2.30 | 5G DDNMF | clauses/6.2.md | 1013-1016 |
| 6.2.31 | EASDF | clauses/6.2.md | 1017-1020 |
| 6.2.32 | TSN AF | clauses/6.2.md | 1021-1032 |
| 6.2.33 | NSWOF | clauses/6.2.md | 1033-1036 |
| 6.3 | Principles for Network Function and Network Function Service discovery and selection | clauses/6.3.md | 1-1509 |
| 6.3.1 | General | clauses/6.3.md | 3-117 |
| 6.3.1.0 | Principles for Binding, Selection and Reselection | clauses/6.3.md | 45-101 |
| 6.3.1.1 | NF Discovery and Selection aspects relevant with indirect communication | clauses/6.3.md | 102-109 |
| 6.3.1.2 | Location information | clauses/6.3.md | 110-117 |
| 6.3.2 | SMF discovery and selection | clauses/6.3.md | 118-239 |
| 6.3.3 | User Plane Function Selection | clauses/6.3.md | 240-343 |
| 6.3.3.1 | Overview | clauses/6.3.md | 242-259 |
| 6.3.3.2 | SMF Provisioning of available UPF(s) | clauses/6.3.md | 260-271 |
| 6.3.3.3 | Selection of an UPF for a particular PDU Session | clauses/6.3.md | 272-343 |
| 6.3.4 | AUSF discovery and selection | clauses/6.3.md | 344-375 |
| 6.3.5 | AMF discovery and selection | clauses/6.3.md | 376-495 |
| 6.3.6 | N3IWF selection | clauses/6.3.md | 496-765 |
| 6.3.6.1 | General | clauses/6.3.md | 498-557 |
| 6.3.6.2 | Stand-alone N3IWF selection | clauses/6.3.md | 558-581 |
| 6.3.6.2a | SNPN N3IWF selection | clauses/6.3.md | 582-623 |
| 6.3.6.3 | Combined N3IWF/ePDG Selection | clauses/6.3.md | 624-691 |
| 6.3.6.4 | PLMN and non-3GPP access node Selection for emergency services | clauses/6.3.md | 692-765 |
| 6.3.6.4.1 | General | clauses/6.3.md | 694-701 |
| 6.3.6.4.2 | Stand-alone N3IWF selection | clauses/6.3.md | 702-729 |
| 6.3.6.3.3 | Combined N3IWF/ePDG Selection | clauses/6.3.md | 730-765 |
| 6.3.7 | PCF discovery and selection | clauses/6.3.md | 766-895 |
| 6.3.7.0 | General principles | clauses/6.3.md | 768-779 |
| 6.3.7.1 | PCF discovery and selection for a UE or a PDU Session | clauses/6.3.md | 780-867 |
| 6.3.7.2 | Providing policy requirements that apply to multiple UE and hence to multiple PCF | clauses/6.3.md | 868-887 |
| 6.3.7.3 | Binding an AF request targeting a UE address to the relevant PCF | clauses/6.3.md | 888-891 |
| 6.3.7.4 | Binding an AF request targeting a UE to the relevant PCF | clauses/6.3.md | 892-895 |
| 6.3.8 | UDM discovery and selection | clauses/6.3.md | 896-925 |
| 6.3.9 | UDR discovery and selection | clauses/6.3.md | 926-945 |
| 6.3.10 | SMSF discovery and selection | clauses/6.3.md | 946-969 |
| 6.3.11 | CHF discovery and selection | clauses/6.3.md | 970-1015 |
| 6.3.12 | Trusted Non-3GPP Access Network selection | clauses/6.3.md | 1016-1127 |
| 6.3.12.1 | General | clauses/6.3.md | 1018-1051 |
| 6.3.12.2 | Access Network Selection Procedure | clauses/6.3.md | 1052-1127 |
| 6.3.12a | Access Network selection for devices that do not support 5GC NAS over WLAN | clauses/6.3.md | 1128-1177 |
| 6.3.12b | Access Network selection for 5G NSWO | clauses/6.3.md | 1178-1197 |
| 6.3.13 | NWDAF discovery and selection | clauses/6.3.md | 1198-1279 |
| 6.3.14 | NEF Discovery | clauses/6.3.md | 1280-1321 |
| 6.3.15 | UCMF Discovery and Selection | clauses/6.3.md | 1322-1327 |
| 6.3.16 | SCP discovery and selection | clauses/6.3.md | 1328-1341 |
| 6.3.17 | NSSAAF discovery and selection | clauses/6.3.md | 1342-1361 |
| 6.3.18 | 5G-EIR discovery and selection | clauses/6.3.md | 1362-1367 |
| 6.3.19 | DCCF discovery and selection | clauses/6.3.md | 1368-1387 |
| 6.3.20 | ADRF discovery and selection | clauses/6.3.md | 1388-1401 |
| 6.3.21 | MFAF discovery and selection | clauses/6.3.md | 1402-1417 |
| 6.3.22 | NSACF discovery and selection | clauses/6.3.md | 1418-1441 |
| 6.3.23 | EASDF discovery and selection | clauses/6.3.md | 1442-1465 |
| 6.3.24 | TSCTSF Discovery | clauses/6.3.md | 1466-1481 |
| 6.3.25 | AF Discovery and Selection | clauses/6.3.md | 1482-1497 |
| 6.3.26 | NRF discovery and selection | clauses/6.3.md | 1498-1509 |
| 7 | Network Function Services and descriptions | clauses/7.md | 1-532 |
| 7.1 | Network Function Service Framework | clauses/7.md | 3-108 |
| 7.1.1 | General | clauses/7.md | 5-26 |
| 7.1.2 | NF Service Consumer - NF Service Producer interactions | clauses/7.md | 27-72 |
| 7.1.3 | Network Function Service discovery | clauses/7.md | 73-80 |
| 7.1.4 | Network Function Service Authorization | clauses/7.md | 81-98 |
| 7.1.5 | Network Function and Network Function Service registration and de-registration | clauses/7.md | 99-108 |
| 7.2 | Network Function Services | clauses/7.md | 109-528 |
| 7.2.1 | General | clauses/7.md | 111-140 |
| 7.2.2 | AMF Services | clauses/7.md | 141-156 |
| 7.2.3 | SMF Services | clauses/7.md | 157-169 |
| 7.2.4 | PCF Services | clauses/7.md | 170-188 |
| 7.2.5 | UDM Services | clauses/7.md | 189-208 |
| 7.2.6 | NRF Services | clauses/7.md | 209-221 |
| 7.2.7 | AUSF Services | clauses/7.md | 222-233 |
| 7.2.8 | NEF Services | clauses/7.md | 234-278 |
| 7.2.8A | Void | clauses/7.md | 279-280 |
| 7.2.9 | SMSF Services | clauses/7.md | 281-291 |
| 7.2.10 | UDR Services | clauses/7.md | 292-303 |
| 7.2.11 | 5G-EIR Services | clauses/7.md | 304-313 |
| 7.2.12 | NWDAF Services | clauses/7.md | 314-332 |
| 7.2.13 | UDSF Services | clauses/7.md | 333-343 |
| 7.2.14 | NSSF Services | clauses/7.md | 344-354 |
| 7.2.15 | BSF Services | clauses/7.md | 355-365 |
| 7.2.16 | LMF Services | clauses/7.md | 366-376 |
| 7.2.16A | GMLC Services | clauses/7.md | 377-386 |
| 7.2.17 | CHF Services | clauses/7.md | 387-398 |
| 7.2.18 | UCMF Services | clauses/7.md | 399-410 |
| 7.2.19 | AF Services | clauses/7.md | 411-422 |
| 7.2.20 | NSSAAF Services | clauses/7.md | 423-433 |
| 7.2.21 | DCCF Services | clauses/7.md | 434-444 |
| 7.2.22 | MFAF Services | clauses/7.md | 445-456 |
| 7.2.23 | ADRF Services | clauses/7.md | 457-467 |
| 7.2.24 | 5G DDNMF Services | clauses/7.md | 468-471 |
| 7.2.25 | EASDF Services | clauses/7.md | 472-483 |
| 7.2.26 | TSCTSF Services | clauses/7.md | 484-495 |
| 7.2.27 | NSACF Services | clauses/7.md | 496-506 |
| 7.2.28 | MB-SMF Services | clauses/7.md | 507-517 |
| 7.2.29 | UPF Services | clauses/7.md | 518-528 |
| 7.3 | Exposure | clauses/7.md | 529-532 |
| 8 | Control and User Plane Protocol Stacks | clauses/8.md | 1-1 |
| 8.1 | General | clauses/8.1.md | 1-4 |
| 8.2 | Control Plane Protocol Stacks | clauses/8.2.md | 1-214 |
| 8.2.1 | Control Plane Protocol Stacks between the 5G-AN and the 5G Core: N2 | clauses/8.2.md | 3-62 |
| 8.2.1.1 | General | clauses/8.2.md | 5-36 |
| 8.2.1.2 | 5G-AN - AMF | clauses/8.2.md | 37-48 |
| 8.2.1.3 | 5G-AN - SMF | clauses/8.2.md | 49-62 |
| 8.2.2 | Control Plane Protocol Stacks between the UE and the 5GC | clauses/8.2.md | 63-152 |
| 8.2.2.1 | General | clauses/8.2.md | 65-114 |
| 8.2.2.2 | UE - AMF | clauses/8.2.md | 115-126 |
| 8.2.2.3 | UE – SMF | clauses/8.2.md | 127-152 |
| 8.2.3 | Control Plane Protocol Stacks between the network functions in 5GC | clauses/8.2.md | 153-162 |
| 8.2.3.1 | The Control Plane Protocol Stack for the service based interface | clauses/8.2.md | 155-158 |
| 8.2.3.2 | The Control Plane protocol stack for the N4 interface between SMF and UPF | clauses/8.2.md | 159-162 |
| 8.2.4 | Control Plane for untrusted non 3GPP Access | clauses/8.2.md | 163-182 |
| 8.2.5 | Control Plane for trusted non-3GPP Access | clauses/8.2.md | 183-202 |
| 8.2.6 | Control Plane for W-5GAN Access | clauses/8.2.md | 203-206 |
| 8.2.7 | Control Plane for Trusted WLAN Access for N5CW Device | clauses/8.2.md | 207-214 |
| 8.3 | User Plane Protocol Stacks | clauses/8.3.md | 1-140 |
| 8.3.1 | User Plane Protocol Stack for a PDU Session | clauses/8.3.md | 3-34 |
| 8.3.2 | User Plane for untrusted non-3GPP Access | clauses/8.3.md | 35-44 |
| 8.3.3 | User Plane for trusted non-3GPP Access | clauses/8.3.md | 45-54 |
| 8.3.4 | User Plane for W-5GAN Access | clauses/8.3.md | 55-58 |
| 8.3.5 | User Plane for N19-based forwarding of a 5G VN group | clauses/8.3.md | 59-66 |
| 8.3.6 | User Plane for Trusted WLAN Access for N5CW Device | clauses/8.3.md | 67-140 |
| D.1 | Introduction | clauses/annex-D.1.md | 1-8 |
| D.2 | Support of Non-Public Network as a network slice of a PLMN | clauses/annex-D.2.md | 1-32 |
| D.3 | Support for access to PLMN services via Stand-alone Non-Public Network and access to Stand-alone Non Public Network services via PLMN | clauses/annex-D.3.md | 1-22 |
| D.4 | Support for UE capable of simultaneously connecting to an SNPN and a PLMN | clauses/annex-D.4.md | 1-8 |
| D.5 | Support for keeping UE in CM-CONNECTED state in overlay network when accessing services via NWu | clauses/annex-D.5.md | 1-14 |
| D.6 | Support for session/service continuity between SNPN and PLMN when using N3IWF | clauses/annex-D.6.md | 1-16 |
| D.7 | Guidance for underlay network to support QoS differentiation for User Plane IPsec Child SA | clauses/annex-D.7.md | 1-38 |
| D.7.1 | Network initiated QoS | clauses/annex-D.7.md | 3-22 |
| D.7.2 | UE initiated QoS | clauses/annex-D.7.md | 23-38 |
| E.1 | General | clauses/annex-E.1.md | 1-93 |
| G.1 | General | clauses/annex-G.1.md | 1-4 |
| G.2 | An SCP based on service mesh | clauses/annex-G.2.md | 1-42 |
| G.2.1 | Introduction | clauses/annex-G.2.md | 3-30 |
| G.2.2 | Communication across service mesh boundaries | clauses/annex-G.2.md | 31-42 |
| G.3 | An SCP based on independent deployment units | clauses/annex-G.3.md | 1-22 |
| G.4 | An SCP deployment example based on name-based routing | clauses/annex-G.4.md | 1-44 |
| G.4.0 | General Information | clauses/annex-G.4.md | 3-20 |
| G.4.1 | Service Registration and Service Discovery | clauses/annex-G.4.md | 21-30 |
| G.4.2 | Overview of Deployment Scenario | clauses/annex-G.4.md | 31-38 |
| G.4.3 | References | clauses/annex-G.4.md | 39-44 |
| H.1 | General | clauses/annex-H.1.md | 1-4 |
| H.2 | Signalling of ingress time for time synchronization | clauses/annex-H.2.md | 1-4 |
| H.3 | Void | clauses/annex-H.3.md | 1-2 |
| H.4 | Path and Link delay measurements | clauses/annex-H.4.md | 1-60 |
| I.1 | Determination of traffic pattern information | clauses/annex-I.1.md | 1-74 |
| K.1 | Standardized port and user plane node management information | clauses/annex-K.1.md | 1-382 |
| K.2 | Port and user plane node management information exchange for time synchronization | clauses/annex-K.2.md | 1-168 |
| K.2.1 | Capability exchange | clauses/annex-K.2.md | 3-26 |
| K.2.2 | PTP Instance configuration | clauses/annex-K.2.md | 27-168 |
| K.2.2.1 | General | clauses/annex-K.2.md | 29-68 |
| K.2.2.2 | Configuration for Sync and Announce reception timeouts | clauses/annex-K.2.md | 69-80 |
| K.2.2.3 | Configuration for PTP port states | clauses/annex-K.2.md | 81-90 |
| K.2.2.4 | Configuration for PTP grandmaster function | clauses/annex-K.2.md | 91-110 |
| K.2.2.5 | Configuration for Sync and Announce intervals | clauses/annex-K.2.md | 111-132 |
| K.2.2.6 | Configuration for transport protocols | clauses/annex-K.2.md | 133-168 |
| M.1 | Mapping of the parameters between 5GS and TSN UNI | clauses/annex-M.1.md | 1-120 |
| M.2 | TL-Container Information | clauses/annex-M.2.md | 1-39 |
| N.1 | General | clauses/annex-N.1.md | 1-6 |
| N.2 | Enabling access to Localized Services | clauses/annex-N.2.md | 1-38 |
| N.2.1 | General | clauses/annex-N.2.md | 3-24 |
| N.2.2 | Configuration of network to provide access to Localized Services | clauses/annex-N.2.md | 25-28 |
| N.2.3 | Session Management aspects | clauses/annex-N.2.md | 29-38 |
| N.3 | Selection of network providing access to Localized Services | clauses/annex-N.3.md | 1-4 |
| N.4 | Enabling the UE access to Localized Services | clauses/annex-N.4.md | 1-10 |
| N.5 | Support for leaving network that provides access to Localized Services | clauses/annex-N.5.md | 1-32 |
| N.6 | Configuration of Credentials Holder for determining SNPN selection information | clauses/annex-N.6.md | 1-20 |
| O.1 | A PDU Session with multiple QoS Flows for different groups | clauses/annex-O.1.md | 1-28 |
| O.2 | Multiple PDU Sessions for different groups | clauses/annex-O.2.md | 1-28 |
| O.3 | A PDU Session targeting a predefined group formed of multiple sub-groups | clauses/annex-O.3.md | 1-34 |
| P.1 | PIN Reference Architecture | clauses/annex-P.1.md | 1-14 |
| P.2 | Session management and traffic routing for PIN | clauses/annex-P.2.md | 1-2584 |
