# TS 23.247 V18.8.0 — 5G MBS architecture

Clause index. `File` is relative to this directory; `Lines` is the 1-based
line range of the clause inside that file.

| Clause | Title | File | Lines |
|---|---|---|---|
| front-matter | Title page, foreword and scope front matter | clauses/front-matter.md | 1-549 |
| 1 | Scope | clauses/1.md | 1-6 |
| 2 | References | clauses/2.md | 1-74 |
| 3 | Definitions of terms and abbreviations | clauses/3.md | 1-80 |
| 3.1 | Terms | clauses/3.md | 3-40 |
| 3.2 | Abbreviations | clauses/3.md | 41-80 |
| 4 | General Concept | clauses/4.md | 1-184 |
| 4.1 | Overview of multicast and broadcast communication | clauses/4.md | 3-66 |
| 4.2 | MB service provisioning | clauses/4.md | 67-132 |
| 4.2.1 | Multicast data provisioning | clauses/4.md | 69-106 |
| 4.2.2 | Broadcast data provisioning | clauses/4.md | 107-132 |
| 4.3 | Multicast session state model | clauses/4.md | 133-184 |
| 5 | Architecture model | clauses/5.md | 1-336 |
| 5.1 | General architecture | clauses/5.md | 3-28 |
| 5.2 | General architecture for interworking with EPS | clauses/5.md | 29-42 |
| 5.3 | Service-based interfaces, Reference point and functional entities | clauses/5.md | 43-336 |
| 5.3.0 | Service-based interfaces | clauses/5.md | 45-58 |
| 5.3.1 | Reference point | clauses/5.md | 59-100 |
| 5.3.2 | Functional entities | clauses/5.md | 101-336 |
| 5.3.2.1 | PCF | clauses/5.md | 103-114 |
| 5.3.2.2 | MB-SMF | clauses/5.md | 115-138 |
| 5.3.2.3 | SMF | clauses/5.md | 139-156 |
| 5.3.2.4 | MB-UPF | clauses/5.md | 157-174 |
| 5.3.2.5 | UPF | clauses/5.md | 175-184 |
| 5.3.2.6 | AMF | clauses/5.md | 185-196 |
| 5.3.2.7 | NG-RAN | clauses/5.md | 197-218 |
| 5.3.2.8 | UE | clauses/5.md | 219-240 |
| 5.3.2.9 | AF | clauses/5.md | 241-252 |
| 5.3.2.10 | NEF | clauses/5.md | 253-266 |
| 5.3.2.11 | MBSF | clauses/5.md | 267-284 |
| 5.3.2.12 | MBSTF | clauses/5.md | 285-300 |
| 5.3.2.13 | UDM | clauses/5.md | 301-308 |
| 5.3.2.14 | UDR | clauses/5.md | 309-316 |
| 5.3.2.15 | NRF | clauses/5.md | 317-336 |
| 5.3.2.15.1 | General | clauses/5.md | 319-330 |
| 5.3.2.15.2 | Extensions to NF profile at NRF | clauses/5.md | 331-336 |
| 6 | Functionalities and features | clauses/6.md | 1-658 |
| 6.1 | Authorization to MBS service | clauses/6.md | 3-26 |
| 6.1.1 | AF authorization to the service for multicast and broadcast | clauses/6.md | 5-8 |
| 6.1.2 | UE authorization to the service for multicast | clauses/6.md | 9-26 |
| 6.2 | Local MBS service and Location dependent MBS service | clauses/6.md | 27-76 |
| 6.2.1 | General | clauses/6.md | 29-36 |
| 6.2.2 | Local MBS service | clauses/6.md | 37-48 |
| 6.2.3 | Location dependent MBS service | clauses/6.md | 49-72 |
| 6.2.4 | Void | clauses/6.md | 73-74 |
| 6.2.5 | Void | clauses/6.md | 75-76 |
| 6.3 | Mobility support of MBS service | clauses/6.md | 77-116 |
| 6.3.1 | Mobility of Multicast MBS session | clauses/6.md | 79-110 |
| 6.3.2 | Mobility of Broadcast MBS session | clauses/6.md | 111-116 |
| 6.4 | Subscription to multicast services | clauses/6.md | 117-176 |
| 6.4.1 | General | clauses/6.md | 119-144 |
| 6.4.2 | MBS subscription data in UDM | clauses/6.md | 145-164 |
| 6.4.3 | MBS information in UDR | clauses/6.md | 165-176 |
| 6.5 | Identifiers | clauses/6.md | 177-228 |
| 6.5.1 | MBS Session ID | clauses/6.md | 179-196 |
| 6.5.2 | Temporary Mobile Group Identity | clauses/6.md | 197-202 |
| 6.5.3 | Source Specific IP Multicast Address | clauses/6.md | 203-206 |
| 6.5.4 | MBS Frequency Selection Area ID | clauses/6.md | 207-222 |
| 6.5.5 | Associated Session ID | clauses/6.md | 223-228 |
| 6.6 | QoS Handling for Multicast and Broadcast services | clauses/6.md | 229-278 |
| 6.7 | User plane management | clauses/6.md | 279-338 |
| 6.8 | Interworking with MBMS over E-UTRAN for public safety services | clauses/6.md | 339-350 |
| 6.9 | MBS Session Context | clauses/6.md | 351-404 |
| 6.9.1 | MBS Session Context | clauses/6.md | 353-404 |
| 6.10 | Policy control for Multicast and Broadcast services | clauses/6.md | 405-454 |
| 6.10.1 | General | clauses/6.md | 407-440 |
| 6.10.2 | MBS Session policy control data in UDR | clauses/6.md | 441-454 |
| 6.11 | Service Announcement | clauses/6.md | 455-502 |
| 6.12 | Paging strategy handling | clauses/6.md | 503-510 |
| 6.13 | MBS Security function | clauses/6.md | 511-536 |
| 6.14 | MBS Service Information | clauses/6.md | 537-560 |
| 6.15 | Group Message Delivery | clauses/6.md | 561-570 |
| 6.16 | Support of MBS data reception for UEs using power saving functions | clauses/6.md | 571-582 |
| 6.17 | Support of Multicast MBS session data reception in UE with RRCINACTIVE state | clauses/6.md | 583-608 |
| 6.18 | Resource sharing across broadcast MBS Sessions during network sharing | clauses/6.md | 609-638 |
| 6.19 | Support of Broadcast MBS Session Intended for NR (e)RedCap UEs | clauses/6.md | 639-652 |
| 6.20 | QoE Measurement Collection Support for MBS | clauses/6.md | 653-658 |
| 7 | MBS procedures | clauses/7.md | 1-1 |
| 7.1 | Common procedure for Multicast and Broadcast | clauses/7.1.md | 1-394 |
| 7.1.1 | MBS Session Management | clauses/7.1.md | 3-370 |
| 7.1.1.1 | General | clauses/7.1.md | 5-20 |
| 7.1.1.2 | MBS Session Creation without PCC | clauses/7.1.md | 21-126 |
| 7.1.1.3 | MBS Session Creation with PCC | clauses/7.1.md | 127-218 |
| 7.1.1.4 | MBS Session Deletion without PCC | clauses/7.1.md | 219-250 |
| 7.1.1.5 | MBS Session Deletion with PCC | clauses/7.1.md | 251-282 |
| 7.1.1.6 | MBS Session Update without PCC | clauses/7.1.md | 283-328 |
| 7.1.1.7 | MBS Session Update with PCC | clauses/7.1.md | 329-370 |
| 7.1.2 | MB-SMF discovery and selection for multicast/broadcast session | clauses/7.1.md | 371-386 |
| 7.1.3 | MB-UPF discovery and selection for multicast/broadcast session | clauses/7.1.md | 387-394 |
| 7.2 | MBS procedures for multicast Session | clauses/7.2.md | 1-1141 |
| 7.2.1 | MBS join and Session establishment procedure | clauses/7.2.md | 3-182 |
| 7.2.1.1 | General | clauses/7.2.md | 5-8 |
| 7.2.1.2 | Establishment of a PDU Session that can be associated with multicast session(s) | clauses/7.2.md | 9-20 |
| 7.2.1.3 | Multicast session join and session establishment procedure | clauses/7.2.md | 21-146 |
| 7.2.1.4 | Establishment of shared delivery toward RAN node | clauses/7.2.md | 147-182 |
| 7.2.2 | Multicast MBS Session leave and Multicast MBS Session release procedure | clauses/7.2.md | 183-324 |
| 7.2.2.1 | General | clauses/7.2.md | 185-188 |
| 7.2.2.2 | Multicast Session leave requested by the UE | clauses/7.2.md | 189-240 |
| 7.2.2.3 | Multicast session leave requested by the network or MBS session release | clauses/7.2.md | 241-286 |
| 7.2.2.4 | Release of shared delivery toward RAN node | clauses/7.2.md | 287-324 |
| 7.2.3 | Mobility Procedures for MBS | clauses/7.2.md | 325-524 |
| 7.2.3.1 | General | clauses/7.2.md | 327-332 |
| 7.2.3.2 | Xn based handover from MBS supporting NG-RAN node | clauses/7.2.md | 333-374 |
| 7.2.3.3 | N2 based handover from MBS supporting NG-RAN node | clauses/7.2.md | 375-408 |
| 7.2.3.4 | Xn/N2 based handover from non-MBS supporting NG-RAN node | clauses/7.2.md | 409-428 |
| 7.2.3.5 | Minimization of data loss | clauses/7.2.md | 429-446 |
| 7.2.3.6 | Xn/N2 based handover for inactive MBS session | clauses/7.2.md | 447-462 |
| 7.2.3.7 | Connection Resume in RRCINACTIVE procedure | clauses/7.2.md | 463-480 |
| 7.2.3.8 | Mobility procedures to enable delivery of multicast MBS session data to UEs in RRCINACTIVE state | clauses/7.2.md | 481-524 |
| 7.2.3.8.1 | General | clauses/7.2.md | 483-512 |
| 7.2.3.8.2 | Mobility of UE in RRCINACTIVE state receiving MBS data within RNA | clauses/7.2.md | 513-516 |
| 7.2.3.8.3 | Mobility of UE in RRCINACTIVE state receiving MBS data out of RNA and within RA | clauses/7.2.md | 517-520 |
| 7.2.3.8.4 | Mobility of UE in RRCINACTIVE state receiving MBS data out of RA | clauses/7.2.md | 521-524 |
| 7.2.4 | Support of Local multicast service and Location dependent multicast service | clauses/7.2.md | 525-836 |
| 7.2.4.1 | General | clauses/7.2.md | 527-530 |
| 7.2.4.2 | Support of location dependent multicast service | clauses/7.2.md | 531-712 |
| 7.2.4.2.0 | Creation for location dependent MBS session | clauses/7.2.md | 533-556 |
| 7.2.4.2.1 | UE join location dependent Multicast MBS session and establishment procedure | clauses/7.2.md | 557-582 |
| 7.2.4.2.2 | Void | clauses/7.2.md | 583-584 |
| 7.2.4.2.3 | Handover procedure | clauses/7.2.md | 585-636 |
| 7.2.4.2.4 | Activation of location dependent MBS session | clauses/7.2.md | 637-654 |
| 7.2.4.2.5 | UE location change handling within the same NG-RAN node between cells belonging to different MBS service areas during Individual delivery | clauses/7.2.md | 655-674 |
| 7.2.4.2.6 | UE location change handling by SMF | clauses/7.2.md | 675-688 |
| 7.2.4.2.7 | UE mobility within the same NG-RAN between cells belonging to different MBS service areas for shared delivery | clauses/7.2.md | 689-700 |
| 7.2.4.2.8 | Void | clauses/7.2.md | 701-702 |
| 7.2.4.2.9 | Connection Resume procedure | clauses/7.2.md | 703-712 |
| 7.2.4.3 | Support of local MBS for multicast | clauses/7.2.md | 713-836 |
| 7.2.4.3.1 | Local MBS service area information provided by AF | clauses/7.2.md | 715-722 |
| 7.2.4.3.2 | Multicast session join and session establishment procedure for local MBS | clauses/7.2.md | 723-762 |
| 7.2.4.3.3 | Handover procedure with local MBS session | clauses/7.2.md | 763-788 |
| 7.2.4.3.4 | Activation of local MBS session | clauses/7.2.md | 789-800 |
| 7.2.4.3.5 | UE location change handling by SMF | clauses/7.2.md | 801-814 |
| 7.2.4.3.6 | UE mobility within the same NG-RAN between cells in or out of the MBS service area | clauses/7.2.md | 815-824 |
| 7.2.4.3.7 | Void | clauses/7.2.md | 825-826 |
| 7.2.4.3.8 | Connection Resume procedure with local MBS session | clauses/7.2.md | 827-836 |
| 7.2.5 | MBS session activation and deactivation | clauses/7.2.md | 837-994 |
| 7.2.5.1 | General | clauses/7.2.md | 839-846 |
| 7.2.5.2 | MBS session activation procedure | clauses/7.2.md | 847-944 |
| 7.2.5.3 | MBS session deactivation procedure | clauses/7.2.md | 945-994 |
| 7.2.6 | Multicast session update procedure | clauses/7.2.md | 995-1054 |
| 7.2.7 | Void | clauses/7.2.md | 1055-1056 |
| 7.2.8 | Service request procedure | clauses/7.2.md | 1057-1068 |
| 7.2.9 | AF provisioning multicast MBS Session Authorization information | clauses/7.2.md | 1069-1094 |
| 7.2.9a | AF provisioning MBS Session assistance information | clauses/7.2.md | 1095-1115 |
| 7.2.10 | Multicast MBS procedures for UEs using power saving functions | clauses/7.2.md | 1116-1141 |
| 7.3 | MBS procedures for broadcast Session | clauses/7.3.md | 1-312 |
| 7.3.1 | MBS Session Start for Broadcast | clauses/7.3.md | 5-66 |
| 7.3.1a | MBS Session Start for resource sharing across multiple broadcast MBS Sessions during network sharing | clauses/7.3.md | 67-98 |
| 7.3.2 | MBS Session Release for Broadcast | clauses/7.3.md | 99-128 |
| 7.3.2a | MBS Session Release for resource sharing across multiple broadcast MBS Sessions during network sharing | clauses/7.3.md | 129-148 |
| 7.3.3 | MBS Session Update for Broadcast | clauses/7.3.md | 149-196 |
| 7.3.4 | Support for Location dependent Broadcast Service | clauses/7.3.md | 197-228 |
| 7.3.5 | MBS Session Delivery Status Indication for Broadcast | clauses/7.3.md | 229-242 |
| 7.3.6 | Broadcast MBS Session Release Require | clauses/7.3.md | 243-260 |
| 7.3.7 | Transport change for resource sharing across broadcast MBS Sessions during network sharing | clauses/7.3.md | 261-296 |
| 7.3.8 | Broadcast MBS procedures for UEs using power saving functions | clauses/7.3.md | 297-312 |
| 7.4 | MBS procedures for inter System Mobility | clauses/7.4.md | 1-30 |
| 7.4.1 | Inter-system mobility with interworking at service layer | clauses/7.4.md | 3-30 |
| 7.5 | MBS procedures for Group Message Delivery | clauses/7.5.md | 1-108 |
| 7.5.1 | Group Message Delivery via MBS Broadcast | clauses/7.5.md | 3-48 |
| 7.5.2 | Modification of previously submitted Group message | clauses/7.5.md | 49-80 |
| 7.5.3 | Cancellation of previously submitted Group message | clauses/7.5.md | 81-108 |
| 8 | Control and user plane stacks | clauses/8.md | 1-50 |
| 8.1 | Control plane for Multicast and Broadcast services | clauses/8.md | 3-22 |
| 8.1.1 | General | clauses/8.md | 5-12 |
| 8.1.2 | NG-RAN – MB-SMF | clauses/8.md | 13-22 |
| 8.2 | User plane for Multicast and Broadcast services | clauses/8.md | 23-50 |
| 9 | Network Function Services | clauses/9.md | 1-996 |
| 9.1 | MB-SMF Services | clauses/9.md | 3-232 |
| 9.1.1 | General | clauses/9.md | 5-26 |
| 9.1.2 | NmbsmfTMGI service | clauses/9.md | 27-60 |
| 9.1.2.1 | General | clauses/9.md | 29-32 |
| 9.1.2.2 | NmbsmfTMGIAllocate service operation | clauses/9.md | 33-46 |
| 9.1.2.3 | NmbsmfTMGIDeallocate service operation | clauses/9.md | 47-60 |
| 9.1.3 | NmbsmfMBSSession service | clauses/9.md | 61-232 |
| 9.1.3.1 | General | clauses/9.md | 63-98 |
| 9.1.3.2 | NmbsmfMBSSessionContextUpdate service operation | clauses/9.md | 99-112 |
| 9.1.3.3 | NmbsmfMBSSessionContextStatusSubscribe service operation | clauses/9.md | 113-126 |
| 9.1.3.4 | NmbsmfMBSSessionContextStatusNotify service operation | clauses/9.md | 127-140 |
| 9.1.3.5 | NmbsmfMBSSessionContextStatusUnsubscribe service operation | clauses/9.md | 141-154 |
| 9.1.3.6 | NmbsmfMBSSessionCreate service operation | clauses/9.md | 155-168 |
| 9.1.3.7 | NmbsmfMBSSessionUpdate service operation | clauses/9.md | 169-182 |
| 9.1.3.8 | NmbsmfMBSSessionDelete service operation | clauses/9.md | 183-196 |
| 9.1.3.9 | NmbsmfMBSSessionStatusNotify service operation | clauses/9.md | 197-208 |
| 9.1.3.10 | NmbsmfMBSSessionStatusSubscribe service operation | clauses/9.md | 209-220 |
| 9.1.3.11 | NmbsmfMBSSessionStatusUnsubscribe service operation | clauses/9.md | 221-232 |
| 9.2 | PCF Services | clauses/9.md | 233-366 |
| 9.2.1 | General | clauses/9.md | 235-250 |
| 9.2.2 | NpcfMBSPolicyControl service | clauses/9.md | 251-316 |
| 9.2.2.1 | General | clauses/9.md | 253-272 |
| 9.2.2.2 | NpcfMBSPolicyControlCreate service operation | clauses/9.md | 273-286 |
| 9.2.2.3 | Void | clauses/9.md | 287-288 |
| 9.2.2.4 | NpcfMBSPolicyControlDelete service operation | clauses/9.md | 289-302 |
| 9.2.2.5 | NpcfMBSPolicyControlUpdate service operation | clauses/9.md | 303-316 |
| 9.2.3 | NpcfMBSPolicyAuthorization Service | clauses/9.md | 317-366 |
| 9.2.3.1 | General | clauses/9.md | 319-322 |
| 9.2.3.2 | NpcfMBSPolicyAuthorizationCreate service operation | clauses/9.md | 323-336 |
| 9.2.3.3 | NpcfMBSPolicyAuthorizationUpdate service operation | clauses/9.md | 337-352 |
| 9.2.3.4 | NpcfMBSPolicyAuthorizationDelete service operation | clauses/9.md | 353-366 |
| 9.3 | AMF Services | clauses/9.md | 367-467 |
| 9.3.1 | General | clauses/9.md | 369-385 |
| 9.3.2 | NamfMBSBroadcast service | clauses/9.md | 386-447 |
| 9.3.2.1 | General | clauses/9.md | 388-391 |
| 9.3.2.2 | NamfMBSBroadcastContextCreate service operation | clauses/9.md | 392-405 |
| 9.3.2.3 | NamfMBSBroadcastContextUpdate service operation | clauses/9.md | 406-419 |
| 9.3.2.4 | NamfMBSBroadcastContextRelease service operation | clauses/9.md | 420-433 |
| 9.3.2.5 | NamfMBSBroadcastContextStatusNotify service operation | clauses/9.md | 434-447 |
| 9.3.3 | NamfMBSCommunication Service | clauses/9.md | 448-467 |
| 9.3.3.1 | General | clauses/9.md | 450-453 |
| 9.3.3.2 | NamfMBSCommunicationN2MessageTransfer service operation | clauses/9.md | 454-467 |
| 9.4 | NEF Services | clauses/9.md | 468-702 |
| 9.4.1 | General | clauses/9.md | 470-492 |
| 9.4.2 | NnefMBSTMGI service | clauses/9.md | 493-540 |
| 9.4.2.1 | General | clauses/9.md | 495-498 |
| 9.4.2.2 | NnefMBSTMGIAllocate service operation | clauses/9.md | 499-512 |
| 9.4.2.3 | NnefMBSTMGIDeallocate service operation | clauses/9.md | 513-526 |
| 9.4.2.4 | NnefMBSTMGIExpiryNotify service operation | clauses/9.md | 527-540 |
| 9.4.3 | NnefMBSSession Service | clauses/9.md | 541-638 |
| 9.4.3.1 | General | clauses/9.md | 543-554 |
| 9.4.3.2 | NnefMBSSessionCreate service operation | clauses/9.md | 555-568 |
| 9.4.3.3 | NnefMBSSessionUpdate service operation | clauses/9.md | 569-582 |
| 9.4.3.4 | NnefMBSSessionDelete service operation | clauses/9.md | 583-596 |
| 9.4.3.5 | NnefMBSSessionStatusNotify service operation | clauses/9.md | 597-610 |
| 9.4.3.6 | NnefMBSSessionStatusSubscribe service operation | clauses/9.md | 611-624 |
| 9.4.3.7 | NnefMBSSessionStatusUnsubscribe service operation | clauses/9.md | 625-638 |
| 9.4.4 | NnefMBSGroupMsgDelivery Service | clauses/9.md | 639-702 |
| 9.4.4.1 | General | clauses/9.md | 641-644 |
| 9.4.4.2 | NnefMBSGroupMsgDeliveryCreate service operation | clauses/9.md | 645-658 |
| 9.4.4.3 | NnefMBSGroupMsgDeliveryUpdate service operation | clauses/9.md | 659-672 |
| 9.4.4.3a | NnefMBSGroupMsgDeliveryDelete service operation | clauses/9.md | 673-686 |
| 9.4.4.4 | NnefMBSGroupMsgDeliveryStatusNotify service operation | clauses/9.md | 687-702 |
| 9.5 | MBSF Services | clauses/9.md | 703-996 |
