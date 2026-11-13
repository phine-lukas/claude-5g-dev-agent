# TS 24.501 V18.14.0 — 5GS NAS

Clause index. `File` is relative to this directory; `Lines` is the 1-based
line range of the clause inside that file.

| Clause | Title | File | Lines |
|---|---|---|---|
| front-matter | Title page, foreword and scope front matter | clauses/front-matter.md | 1-2749 |
| 1 | Scope | clauses/1.md | 1-22 |
| 2 | References | clauses/2.md | 1-276 |
| 3 | Definitions and abbreviations | clauses/3.md | 1-1134 |
| 3.1 | Definitions | clauses/3.md | 3-748 |
| 3.2 | Abbreviations | clauses/3.md | 749-1134 |
| 4 | General | clauses/4.md | 1-1 |
| 4.1 | Overview | clauses/4.1.md | 1-26 |
| 4.2 | Coordination between the protocols for 5GS mobility management and 5GS session management | clauses/4.2.md | 1-30 |
| 4.3 | UE domain selection | clauses/4.3.md | 1-120 |
| 4.3.1 | UE's usage setting | clauses/4.3.md | 3-18 |
| 4.3.2 | Domain selection for UE originating sessions / calls | clauses/4.3.md | 19-90 |
| 4.3.3 | Change of UE's usage setting | clauses/4.3.md | 91-106 |
| 4.3.4 | Change or determination of IMS voice availability | clauses/4.3.md | 107-120 |
| 4.4 | NAS security | clauses/4.4.md | 1-580 |
| 4.4.1 | General | clauses/4.4.md | 3-10 |
| 4.4.2 | Handling of 5G NAS security contexts | clauses/4.4.md | 11-214 |
| 4.4.2.1 | General | clauses/4.4.md | 13-86 |
| 4.4.2.1.1 | Establishment of 5G NAS security context | clauses/4.4.md | 15-74 |
| 4.4.2.1.2 | UE leaving state 5GMM-DEREGISTERED | clauses/4.4.md | 75-80 |
| 4.4.2.1.3 | UE entering state 5GMM-DEREGISTERED | clauses/4.4.md | 81-86 |
| 4.4.2.2 | Establishment of a mapped 5G NAS security context during inter-system change from S1 mode to N1 mode in 5GMM-CONNECTED mode | clauses/4.4.md | 87-112 |
| 4.4.2.3 | Establishment of a 5G NAS security context during N1 mode to N1 mode handover | clauses/4.4.md | 113-136 |
| 4.4.2.4 | Establishment of an EPS security context during inter-system change from N1 mode to S1 mode in 5GMM-CONNECTED mode | clauses/4.4.md | 137-152 |
| 4.4.2.5 | Establishment of secure exchange of NAS messages | clauses/4.4.md | 153-206 |
| 4.4.2.6 | Change of security keys | clauses/4.4.md | 207-214 |
| 4.4.3 | Handling of NAS COUNT and NAS sequence number | clauses/4.4.md | 215-314 |
| 4.4.3.1 | General | clauses/4.4.md | 217-250 |
| 4.4.3.2 | Replay protection | clauses/4.4.md | 251-258 |
| 4.4.3.3 | Integrity protection and verification | clauses/4.4.md | 259-278 |
| 4.4.3.4 | Ciphering and deciphering | clauses/4.4.md | 279-294 |
| 4.4.3.5 | NAS COUNT wrap around | clauses/4.4.md | 295-314 |
| 4.4.4 | Integrity protection of NAS signalling messages | clauses/4.4.md | 315-430 |
| 4.4.4.1 | General | clauses/4.4.md | 317-344 |
| 4.4.4.2 | Integrity checking of NAS signalling messages in the UE | clauses/4.4.md | 345-368 |
| 4.4.4.3 | Integrity checking of NAS signalling messages in the AMF | clauses/4.4.md | 369-430 |
| 4.4.5 | Ciphering of NAS signalling messages | clauses/4.4.md | 431-448 |
| 4.4.6 | Protection of initial NAS signalling messages | clauses/4.4.md | 449-570 |
| 4.4.7 | Protection of NAS IEs | clauses/4.4.md | 571-580 |
| 4.5 | Unified access control | clauses/4.5.md | 1-646 |
| 4.5.1 | General | clauses/4.5.md | 3-68 |
| 4.5.2 | Determination of the access identities and access category associated with a request for access for UEs not operating in SNPN access operation mode over 3GPP access | clauses/4.5.md | 69-136 |
| 4.5.2A | Determination of the access identities and access category associated with a request for access for UEs operating in SNPN access operation mode over 3GPP access | clauses/4.5.md | 137-193 |
| 4.5.3 | Operator-defined access categories | clauses/4.5.md | 194-277 |
| 4.5.4 | Access control and checking | clauses/4.5.md | 278-385 |
| 4.5.4.1 | Access control and checking in 5GMM-IDLE mode and in 5GMM-IDLE mode with suspend indication | clauses/4.5.md | 280-327 |
| 4.5.4.2 | Access control and checking in 5GMM-CONNECTED mode and in 5GMM-CONNECTED mode with RRC inactive indication | clauses/4.5.md | 328-385 |
| 4.5.5 | Exception handling and avoiding double barring | clauses/4.5.md | 386-597 |
| 4.5.6 | Mapping between access categories/access identities and RRC establishment cause | clauses/4.5.md | 598-646 |
| 4.6 | Network slicing | clauses/4.6.md | 1-1000 |
| 4.6.1 | General | clauses/4.6.md | 3-100 |
| 4.6.2 | Mobility management aspects | clauses/4.6.md | 101-796 |
| 4.6.2.1 | General | clauses/4.6.md | 103-144 |
| 4.6.2.2 | NSSAI storage | clauses/4.6.md | 145-396 |
| 4.6.2.3 | Provision of NSSAI to lower layers in 5GMM-IDLE mode | clauses/4.6.md | 397-440 |
| 4.6.2.4 | Network slice-specific authentication and authorization | clauses/4.6.md | 441-492 |
| 4.6.2.5 | Mobility management based network slice admission control | clauses/4.6.md | 493-522 |
| 4.6.2.6 | Provision of NSAG information to lower layers | clauses/4.6.md | 523-572 |
| 4.6.2.7 | Mobility management based network slice replacement | clauses/4.6.md | 573-628 |
| 4.6.2.8 | Mobility management for optimised handling of temporarily available network slices | clauses/4.6.md | 629-672 |
| 4.6.2.9 | Mobility management based network slice usage control | clauses/4.6.md | 673-716 |
| 4.6.2.10 | Mobility management aspects of handling network slices with NS-AoS not matching deployed tracking areas | clauses/4.6.md | 717-748 |
| 4.6.2.11 | Mobility management for partial network slice | clauses/4.6.md | 749-796 |
| 4.6.3 | Session management aspects | clauses/4.6.md | 797-1000 |
| 4.6.3.0 | General | clauses/4.6.md | 799-802 |
| 4.6.3.1 | Session management based network slice admission control | clauses/4.6.md | 803-820 |
| 4.6.3.2 | Support of network slice admission control and interworking with EPC | clauses/4.6.md | 821-826 |
| 4.6.3.3 | Session management based network slice data rate limitation control | clauses/4.6.md | 827-836 |
| 4.6.3.4 | Session management based network slice replacement | clauses/4.6.md | 837-890 |
| 4.6.3.5 | Session management for optimized handling of temporarily available network slices | clauses/4.6.md | 891-904 |
| 4.6.3.6 | Session management for partial network slice | clauses/4.6.md | 905-962 |
| 4.6.3.7 | Session management aspect of handling network slices with NS-AoS not matching deployed tracking areas | clauses/4.6.md | 963-1000 |
| 4.7 | NAS over non-3GPP access | clauses/4.7.md | 1-171 |
| 4.7.1 | General | clauses/4.7.md | 3-6 |
| 4.7.2 | 5GS mobility management aspects | clauses/4.7.md | 7-113 |
| 4.7.2.1 | General | clauses/4.7.md | 9-54 |
| 4.7.2.2 | Establishment cause for non-3GPP access | clauses/4.7.md | 55-113 |
| 4.7.3 | 5GS session management aspects | clauses/4.7.md | 114-129 |
| 4.7.4 | Limited service state over non-3GPP access | clauses/4.7.md | 130-153 |
| 4.7.5 | NAS signalling using trusted WLAN access network | clauses/4.7.md | 154-171 |
| 4.8 | Interworking with E-UTRAN connected to EPC | clauses/4.8.md | 1-242 |
| 4.8.1 | General | clauses/4.8.md | 3-10 |
| 4.8.2 | Single-registration mode | clauses/4.8.md | 11-148 |
| 4.8.2.1 | General | clauses/4.8.md | 13-24 |
| 4.8.2.2 | Single-registration mode with N26 interface | clauses/4.8.md | 25-28 |
| 4.8.2.3 | Single-registration mode without N26 interface | clauses/4.8.md | 29-148 |
| 4.8.2.3.1 | Interworking between NG-RAN and E-UTRAN | clauses/4.8.md | 31-110 |
| 4.8.2.3.2 | Interworking between TNGF or N3IWF connected to 5GCN and E-UTRAN | clauses/4.8.md | 111-148 |
| 4.8.3 | Dual-registration mode | clauses/4.8.md | 149-190 |
| 4.8.4 | Core Network selection for UEs not using CIoT 5GS optimizations | clauses/4.8.md | 191-208 |
| 4.8.4A | Core Network selection and redirection for UEs using CIoT optimizations | clauses/4.8.md | 209-242 |
| 4.9 | Disabling and re-enabling of UE's N1 mode capability | clauses/4.9.md | 1-148 |
| 4.9.1 | General | clauses/4.9.md | 3-6 |
| 4.9.2 | Disabling and re-enabling of UE's N1 mode capability for 3GPP access | clauses/4.9.md | 7-118 |
| 4.9.3 | Disabling and re-enabling of UE's N1 mode capability for non-3GPP access | clauses/4.9.md | 119-132 |
| 4.9.4 | Disabling and re-enabling of UE's satellite NG-RAN capability | clauses/4.9.md | 133-148 |
| 4.10 | Interworking with ePDG connected to EPC | clauses/4.10.md | 1-12 |
| 4.11 | UE configuration parameter updates | clauses/4.11.md | 1-28 |
| 4.12 | Access traffic steering, switching and splitting (ATSSS) | clauses/4.12.md | 1-14 |
| 4.13 | Support of NAS signalling using wireline access network | clauses/4.13.md | 1-50 |
| 4.14 | Non-public network (NPN) | clauses/4.14.md | 1-138 |
| 4.14.1 | General | clauses/4.14.md | 3-6 |
| 4.14.2 | Stand-alone non-public network (SNPN) | clauses/4.14.md | 7-90 |
| 4.14.3 | Public network integrated non-public network (PNI-NPN) | clauses/4.14.md | 91-138 |
| 4.15 | Time synchronization and time sensitive communication | clauses/4.15.md | 1-36 |
| 4.15.1 | General | clauses/4.15.md | 3-6 |
| 4.15.2 | Void | clauses/4.15.md | 7-14 |
| 4.15.2.1 | Void | clauses/4.15.md | 9-10 |
| 4.15.2.2 | Void | clauses/4.15.md | 11-12 |
| 4.15.2.3 | Void | clauses/4.15.md | 13-14 |
| 4.15.3 | Time synchronization | clauses/4.15.md | 15-28 |
| 4.15.4 | User plane node management | clauses/4.15.md | 29-36 |
| 4.16 | UE radio capability signalling optimisation | clauses/4.16.md | 1-36 |
| 4.17 | 5GS mobility management in NB-N1 mode | clauses/4.17.md | 1-10 |
| 4.18 | 5GS session management in NB-N1 mode | clauses/4.18.md | 1-10 |
| 4.19 | 5GS mobility management in WB-N1 mode for IoT | clauses/4.19.md | 1-24 |
| 4.20 | 5GS session management in WB-N1 mode for IoT | clauses/4.20.md | 1-88 |
| 4.22.1 | General | clauses/4.20.md | 43-48 |
| 4.22.2 | Authentication and authorization of UAV | clauses/4.20.md | 49-68 |
| 4.22.3 | Authorization of C2 communication | clauses/4.20.md | 69-86 |
| 4.22.4 | Void | clauses/4.20.md | 87-88 |
| 4.23 | NAS over Non-Terrestrial Network | clauses/4.23.md | 1-98 |
| 4.23.1 | General | clauses/4.23.md | 3-6 |
| 4.23.2 | List of "PLMNs not allowed to operate at the present UE location" | clauses/4.23.md | 7-46 |
| 4.23.3 | 5GS mobility management via a satellite NG-RAN cell | clauses/4.23.md | 47-60 |
| 4.23.4 | 5GS session management via a satellite NG-RAN cell | clauses/4.23.md | 61-72 |
| 4.23.5 | Handling multiple tracking area codes from the lower layers | clauses/4.23.md | 73-98 |
| 4.24 | Minimization of service interruption | clauses/4.24.md | 1-44 |
| 4.25 | Support of MUSIM features | clauses/4.25.md | 1-16 |
| 4.26 | Support for Personal IoT Network service | clauses/4.26.md | 1-28 |
| 4.27 | Mobile base station relay support | clauses/4.27.md | 1-8 |
| 5 | Elementary procedures for 5GS mobility management | clauses/5.md | 1-1 |
| 5.1 | Overview | clauses/5.1.md | 1-376 |
| 5.1.1 | General | clauses/5.1.md | 3-10 |
| 5.1.2 | Types of 5GMM procedures | clauses/5.1.md | 11-78 |
| 5.1.3 | 5GMM sublayer states | clauses/5.1.md | 79-324 |
| 5.1.3.1 | General | clauses/5.1.md | 81-84 |
| 5.1.3.2 | 5GMM sublayer states | clauses/5.1.md | 85-324 |
| 5.1.3.2.1 | 5GMM sublayer states in the UE | clauses/5.1.md | 87-274 |
| 5.1.3.2.1.1 | General | clauses/5.1.md | 89-98 |
| 5.1.3.2.1.2 | Main states | clauses/5.1.md | 99-124 |
| 5.1.3.2.1.3 | Substates of state 5GMM-DEREGISTERED | clauses/5.1.md | 125-188 |
| 5.1.3.2.1.4 | Substates of state 5GMM-REGISTERED | clauses/5.1.md | 189-274 |
| 5.1.3.2.2 | 5GS update status in the UE | clauses/5.1.md | 275-296 |
| 5.1.3.2.3 | 5GMM sublayer states in the network side | clauses/5.1.md | 297-324 |
| 5.1.3.2.3.1 | General | clauses/5.1.md | 299-308 |
| 5.1.3.2.3.2 | 5GMM-DEREGISTERED | clauses/5.1.md | 309-312 |
| 5.1.3.2.3.3 | 5GMM-COMMON-PROCEDURE-INITIATED | clauses/5.1.md | 313-316 |
| 5.1.3.2.3.4 | 5GMM-REGISTERED | clauses/5.1.md | 317-320 |
| 5.1.3.2.3.5 | 5GMM-DEREGISTERED-INITIATED | clauses/5.1.md | 321-324 |
| 5.1.4 | Coordination between 5GMM and EMM | clauses/5.1.md | 325-366 |
| 5.1.4.1 | General | clauses/5.1.md | 327-336 |
| 5.1.4.2 | Coordination between 5GMM for 3GPP access and EMM with N26 interface | clauses/5.1.md | 337-350 |
| 5.1.4.3 | Coordination between 5GMM for 3GPP access and EMM without N26 interface | clauses/5.1.md | 351-366 |
| 5.1.5 | Coordination between 5GMM and GMM | clauses/5.1.md | 367-376 |
| 5.2 | Behaviour of the UE in state 5GMM-DEREGISTERED and state 5GMM-REGISTERED | clauses/5.2.md | 1-328 |
| 5.2.1 | General | clauses/5.2.md | 3-6 |
| 5.2.2 | UE behaviour in state 5GMM-DEREGISTERED | clauses/5.2.md | 7-190 |
| 5.2.2.1 | General | clauses/5.2.md | 9-24 |
| 5.2.2.2 | Primary substate selection | clauses/5.2.md | 25-62 |
| 5.2.2.2.1 | Selection of the substate after power on | clauses/5.2.md | 27-62 |
| 5.2.2.3 | Detailed description of UE behaviour in state 5GMM-DEREGISTERED | clauses/5.2.md | 63-170 |
| 5.2.2.3.1 | NORMAL-SERVICE | clauses/5.2.md | 65-70 |
| 5.2.2.3.2 | LIMITED-SERVICE | clauses/5.2.md | 71-76 |
| 5.2.2.3.3 | ATTEMPTING-REGISTRATION | clauses/5.2.md | 77-134 |
| 5.2.2.3.4 | PLMN-SEARCH | clauses/5.2.md | 135-140 |
| 5.2.2.3.5 | NO-SUPI | clauses/5.2.md | 141-144 |
| 5.2.2.3.6 | NO-CELL-AVAILABLE | clauses/5.2.md | 145-148 |
| 5.2.2.3.7 | eCALL-INACTIVE | clauses/5.2.md | 149-164 |
| 5.2.2.3.8 | INITIAL-REGISTRATION-NEEDED | clauses/5.2.md | 165-170 |
| 5.2.2.4 | Substate when back to state 5GMM-DEREGISTERED from another 5GMM state | clauses/5.2.md | 171-190 |
| 5.2.3 | UE behaviour in state 5GMM-REGISTERED | clauses/5.2.md | 191-328 |
| 5.2.3.1 | General | clauses/5.2.md | 193-198 |
| 5.2.3.2 | Detailed description of UE behaviour in state 5GMM-REGISTERED | clauses/5.2.md | 199-328 |
| 5.2.3.2.1 | NORMAL-SERVICE | clauses/5.2.md | 201-220 |
| 5.2.3.2.2 | NON-ALLOWED-SERVICE | clauses/5.2.md | 221-226 |
| 5.2.3.2.3 | ATTEMPTING-REGISTRATION-UPDATE | clauses/5.2.md | 227-296 |
| 5.2.3.2.4 | LIMITED-SERVICE | clauses/5.2.md | 297-306 |
| 5.2.3.2.5 | PLMN-SEARCH | clauses/5.2.md | 307-310 |
| 5.2.3.2.6 | NO-CELL-AVAILABLE | clauses/5.2.md | 311-314 |
| 5.2.3.2.7 | UPDATE-NEEDED | clauses/5.2.md | 315-328 |
| 5.3 | General on elementary 5GMM procedures | clauses/5.3.md | 1-1 |
| 5.3.1 | 5GMM modes and N1 NAS signalling connection | clauses/5.3.1.md | 1-490 |
| 5.3.1.1 | Establishment of the N1 NAS signalling connection | clauses/5.3.1.md | 3-72 |
| 5.3.1.2 | Re-establishment of the N1 NAS signalling connection | clauses/5.3.1.md | 73-130 |
| 5.3.1.3 | Release of the N1 NAS signalling connection | clauses/5.3.1.md | 131-314 |
| 5.3.1.4 | 5GMM-CONNECTED mode with RRC inactive indication | clauses/5.3.1.md | 315-452 |
| 5.3.1.5 | Suspend and resume of the N1 NAS signalling connection | clauses/5.3.1.md | 453-490 |
| 5.3.2 | Permanent identifiers | clauses/5.3.2.md | 1-126 |
| 5.3.3 | Temporary identities | clauses/5.3.3.md | 1-46 |
| 5.3.4 | Registration areas | clauses/5.3.4.md | 1-30 |
| 5.3.5 | Service area restrictions | clauses/5.3.5.md | 1-284 |
| 5.3.5.1 | General | clauses/5.3.5.md | 3-12 |
| 5.3.5.2 | 3GPP access service area restrictions | clauses/5.3.5.md | 13-234 |
| 5.3.5.3 | Wireline access service area restrictions | clauses/5.3.5.md | 235-284 |
| 5.3.6 | Mobile initiated connection only mode | clauses/5.3.6.md | 1-58 |
| 5.3.7 | Handling of the periodic registration update timer and mobile reachable timer | clauses/5.3.7.md | 1-58 |
| 5.3.8 | Handling of timer T3502 | clauses/5.3.8.md | 1-18 |
| 5.3.9 | Handling of NAS level mobility management congestion control | clauses/5.3.9.md | 1-50 |
| 5.3.10 | Handling of DNN based congestion control | clauses/5.3.10.md | 1-6 |
| 5.3.11 | Handling of S-NSSAI based congestion control | clauses/5.3.11.md | 1-8 |
| 5.3.12 | Handling of local emergency numbers | clauses/5.3.12.md | 1-32 |
| 5.3.12A | Handling of local emergency numbers received via 3GPP access and non-3GPP access | clauses/5.3.12A.md | 1-50 |
| 5.3.13 | Lists of 5GS forbidden tracking areas | clauses/5.3.13.md | 1-44 |
| 5.3.13A | Forbidden PLMN lists | clauses/5.3.13A.md | 1-14 |
| 5.3.14 | List of equivalent PLMNs | clauses/5.3.14.md | 1-8 |
| 5.3.14A | List of equivalent SNPNs | clauses/5.3.14A.md | 1-26 |
| 5.3.15 | Transmission failure abnormal case in the UE | clauses/5.3.15.md | 1-8 |
| 5.3.16 | Extended DRX cycle for UEs in 5GMM-IDLE and 5GMM-CONNECTED mode with RRC inactive indication | clauses/5.3.16.md | 1-30 |
| 5.3.17 | Service Gap Control | clauses/5.3.17.md | 1-78 |
| 5.3.18 | Restriction on use of enhanced coverage | clauses/5.3.18.md | 1-34 |
| 5.3.19 | Handling of congestion control for transport of user data via the control plane | clauses/5.3.19.md | 1-22 |
| 5.3.19A | Specific requirements for UE configured to use timer T3245 | clauses/5.3.19A.md | 1-34 |
| 5.3.20 | Specific requirements for UE when receiving non-integrity protected reject messages | clauses/5.3.20.md | 1-334 |
| 5.3.20.1 | General | clauses/5.3.20.md | 3-8 |
| 5.3.20.2 | Requirements for UE in a PLMN | clauses/5.3.20.md | 9-180 |
| 5.3.20.3 | Requirements for UE in an SNPN | clauses/5.3.20.md | 181-334 |
| 5.3.21 | CIoT 5GS optimizations | clauses/5.3.21.md | 1-80 |
| 5.3.22 | Interaction between MICO mode with active time and extended idle mode DRX cycle | clauses/5.3.22.md | 1-6 |
| 5.3.23 | Forbidden wireline access area | clauses/5.3.23.md | 1-14 |
| 5.3.24 | WUS assistance | clauses/5.3.24.md | 1-34 |
| 5.3.25 | Paging Early Indication with Paging Subgrouping Assistance | clauses/5.3.25.md | 1-30 |
| 5.3.26 | Support for unavailability period | clauses/5.3.26.md | 1-26 |
| 5.4 | 5GMM common procedures | clauses/5.4.md | 1-1 |
| 5.4.1 | Primary authentication and key agreement procedure | clauses/5.4.1.md | 1-1192 |
| 5.4.1.1 | General | clauses/5.4.1.md | 3-14 |
| 5.4.1.2 | EAP based primary authentication and key agreement procedure | clauses/5.4.1.md | 15-864 |
| 5.4.1.2.1 | General | clauses/5.4.1.md | 17-60 |
| 5.4.1.2.2 | EAP-AKA' related procedures | clauses/5.4.1.md | 61-310 |
| 5.4.1.2.2.1 | General | clauses/5.4.1.md | 63-72 |
| 5.4.1.2.2.2 | Initiation | clauses/5.4.1.md | 73-98 |
| 5.4.1.2.2.3 | UE successfully authenticates network | clauses/5.4.1.md | 99-116 |
| 5.4.1.2.2.4 | Errors when handling EAP-request/AKA'-challenge message | clauses/5.4.1.md | 117-128 |
| 5.4.1.2.2.5 | Network successfully authenticates UE | clauses/5.4.1.md | 129-152 |
| 5.4.1.2.2.6 | UE handling EAP-AKA' notification message | clauses/5.4.1.md | 153-156 |
| 5.4.1.2.2.6A | EAP based Identification initiation by the network | clauses/5.4.1.md | 157-162 |
| 5.4.1.2.2.6B | EAP based Identification response by the UE | clauses/5.4.1.md | 163-170 |
| 5.4.1.2.2.7 | Network sending EAP-success message | clauses/5.4.1.md | 171-176 |
| 5.4.1.2.2.8 | UE handling EAP-success message | clauses/5.4.1.md | 177-198 |
| 5.4.1.2.2.9 | Network not successfully authenticates UE | clauses/5.4.1.md | 199-202 |
| 5.4.1.2.2.10 | Network sending EAP-failure message | clauses/5.4.1.md | 203-218 |
| 5.4.1.2.2.11 | UE handling EAP-failure message | clauses/5.4.1.md | 219-302 |
| 5.4.1.2.2.12 | Abnormal cases in the UE | clauses/5.4.1.md | 303-310 |
| 5.4.1.2.3 | EAP-TLS related procedures | clauses/5.4.1.md | 311-466 |
| 5.4.1.2.3.1 | General | clauses/5.4.1.md | 313-466 |
| 5.4.1.2.3A | Procedures related to EAP methods other than EAP-AKA' and EAP-TLS | clauses/5.4.1.md | 467-626 |
| 5.4.1.2.3B | Procedures related to EAP methods used for primary authentication of an N5GC device | clauses/5.4.1.md | 627-674 |
| 5.4.1.2.3C | Procedures related to EAP methods used for primary authentication of an AUN3 device | clauses/5.4.1.md | 675-720 |
| 5.4.1.2.4 | EAP message reliable transport procedure | clauses/5.4.1.md | 721-830 |
| 5.4.1.2.4.1 | General | clauses/5.4.1.md | 723-728 |
| 5.4.1.2.4.2 | EAP message reliable transport procedure initiation by the network | clauses/5.4.1.md | 729-742 |
| 5.4.1.2.4.3 | EAP message reliable transport procedure accepted by the UE | clauses/5.4.1.md | 743-752 |
| 5.4.1.2.4.4 | Abnormal cases on the network side | clauses/5.4.1.md | 753-764 |
| 5.4.1.2.4.5 | Abnormal cases in the UE | clauses/5.4.1.md | 765-830 |
| 5.4.1.2.5 | EAP result message transport procedure | clauses/5.4.1.md | 831-864 |
| 5.4.1.2.5.1 | General | clauses/5.4.1.md | 833-842 |
| 5.4.1.2.5.2 | EAP result message transport procedure initiation by the network | clauses/5.4.1.md | 843-864 |
| 5.4.1.3 | 5G AKA based primary authentication and key agreement procedure | clauses/5.4.1.md | 865-1192 |
| 5.4.1.3.1 | General | clauses/5.4.1.md | 867-884 |
| 5.4.1.3.2 | Authentication initiation by the network | clauses/5.4.1.md | 885-896 |
| 5.4.1.3.3 | Authentication response by the UE | clauses/5.4.1.md | 897-940 |
| 5.4.1.3.4 | Authentication completion by the network | clauses/5.4.1.md | 941-948 |
| 5.4.1.3.5 | Authentication not accepted by the network | clauses/5.4.1.md | 949-1038 |
| 5.4.1.3.6 | Authentication not accepted by the UE | clauses/5.4.1.md | 1039-1068 |
| 5.4.1.3.7 | Abnormal cases | clauses/5.4.1.md | 1069-1192 |
| 5.4.2 | Security mode control procedure | clauses/5.4.2.md | 1-304 |
| 5.4.2.1 | General | clauses/5.4.2.md | 3-24 |
| 5.4.2.2 | NAS security mode control initiation by the network | clauses/5.4.2.md | 25-136 |
| 5.4.2.3 | NAS security mode command accepted by the UE | clauses/5.4.2.md | 137-234 |
| 5.4.2.4 | NAS security mode control completion by the network | clauses/5.4.2.md | 235-248 |
| 5.4.2.5 | NAS security mode command not accepted by the UE | clauses/5.4.2.md | 249-262 |
| 5.4.2.6 | Abnormal cases in the UE | clauses/5.4.2.md | 263-280 |
| 5.4.2.7 | Abnormal cases on the network side | clauses/5.4.2.md | 281-304 |
| 5.4.3 | Identification procedure | clauses/5.4.3.md | 1-78 |
| 5.4.3.1 | General | clauses/5.4.3.md | 3-6 |
| 5.4.3.2 | Identification initiation by the network | clauses/5.4.3.md | 7-14 |
| 5.4.3.3 | Identification response by the UE | clauses/5.4.3.md | 15-28 |
| 5.4.3.4 | Identification completion by the network | clauses/5.4.3.md | 29-32 |
| 5.4.3.5 | Abnormal cases in the UE | clauses/5.4.3.md | 33-44 |
| 5.4.3.6 | Abnormal cases on the network side | clauses/5.4.3.md | 45-78 |
| 5.4.4 | Generic UE configuration update procedure | clauses/5.4.4.md | 1-854 |
| 5.4.4.1 | General | clauses/5.4.4.md | 3-226 |
| 5.4.4.2 | Generic UE configuration update procedure initiated by the network | clauses/5.4.4.md | 227-458 |
| 5.4.4.3 | Generic UE configuration update accepted by the UE | clauses/5.4.4.md | 459-742 |
| 5.4.4.4 | Generic UE configuration update completion by the network | clauses/5.4.4.md | 743-780 |
| 5.4.4.5 | Abnormal cases in the UE | clauses/5.4.4.md | 781-810 |
| 5.4.4.6 | Abnormal cases on the network side | clauses/5.4.4.md | 811-854 |
| 5.4.5 | NAS transport procedure(s) | clauses/5.4.5.md | 1-1314 |
| 5.4.5.1 | General | clauses/5.4.5.md | 3-36 |
| 5.4.5.2 | UE-initiated NAS transport procedure | clauses/5.4.5.md | 37-802 |
| 5.4.5.2.1 | General | clauses/5.4.5.md | 39-72 |
| 5.4.5.2.2 | UE-initiated NAS transport procedure initiation | clauses/5.4.5.md | 73-206 |
| 5.4.5.2.3 | UE-initiated NAS transport of messages accepted by the network | clauses/5.4.5.md | 207-386 |
| 5.4.5.2.4 | UE-initiated NAS transport of messages not accepted by the network | clauses/5.4.5.md | 387-498 |
| 5.4.5.2.5 | Abnormal cases on the network side | clauses/5.4.5.md | 499-702 |
| 5.4.5.2.6 | Abnormal cases in the UE | clauses/5.4.5.md | 703-802 |
| 5.4.5.3 | Network-initiated NAS transport procedure | clauses/5.4.5.md | 803-1314 |
| 5.4.5.3.1 | General | clauses/5.4.5.md | 805-864 |
| 5.4.5.3.2 | Network-initiated NAS transport procedure initiation | clauses/5.4.5.md | 865-1152 |
| 5.4.5.3.3 | Network-initiated NAS transport of messages accepted by the UE | clauses/5.4.5.md | 1153-1314 |
| 5.4.6 | 5GMM status procedure | clauses/5.4.6.md | 1-18 |
| 5.4.6.1 | General | clauses/5.4.6.md | 3-10 |
| 5.4.6.2 | 5GMM status received in the UE | clauses/5.4.6.md | 11-14 |
| 5.4.6.3 | 5GMM status received in the network | clauses/5.4.6.md | 15-18 |
| 5.4.7 | Network slice-specific authentication and authorization procedure | clauses/5.4.7.md | 1-152 |
| 5.4.7.1 | General | clauses/5.4.7.md | 3-36 |
| 5.4.7.2 | Network slice-specific EAP message reliable transport procedure | clauses/5.4.7.md | 37-132 |
| 5.4.7.2.1 | Network slice-specific EAP message reliable transport procedure initiation | clauses/5.4.7.md | 39-56 |
| 5.4.7.2.2 | Network slice-specific EAP message reliable transport procedure accepted by the UE | clauses/5.4.7.md | 57-72 |
| 5.4.7.2.3 | Abnormal cases on the network side | clauses/5.4.7.md | 73-100 |
| 5.4.7.2.4 | Abnormal cases in the UE | clauses/5.4.7.md | 101-132 |
| 5.4.7.3 | Network slice-specific EAP result message transport procedure | clauses/5.4.7.md | 133-152 |
| 5.4.7.3.1 | Network slice-specific EAP result message transport procedure initiation | clauses/5.4.7.md | 135-152 |
| 5.5 | 5GMM specific procedures | clauses/5.5.md | 1-1 |
| 5.5.1 | Registration procedure | clauses/5.5.1.md | 1-1 |
| 5.5.1.1 | General | clauses/5.5.1.1.md | 1-56 |
| 5.5.1.2 | Registration procedure for initial registration | clauses/5.5.1.2.md | 1-1 |
| 5.5.1.2.1 | General | clauses/5.5.1.2.1.md | 1-18 |
| 5.5.1.2.2 | Initial registration initiation | clauses/5.5.1.2.2.md | 1-358 |
| 5.5.1.2.3 | 5GMM common procedure initiation | clauses/5.5.1.2.3.md | 1-8 |
| 5.5.1.2.4 | Initial registration accepted by the network | clauses/5.5.1.2.4.md | 1-970 |
| 5.5.1.2.5 | Initial registration not accepted by the network | clauses/5.5.1.2.5.md | 1-474 |
| 5.5.1.2.6 | Initial registration for emergency services not accepted by the network | clauses/5.5.1.2.6.md | 1-50 |
| 5.5.1.2.6A | Initial registration for initiating an emergency PDU session not accepted by the network | clauses/5.5.1.2.6A.md | 1-28 |
| 5.5.1.2.7 | Abnormal cases in the UE | clauses/5.5.1.2.7.md | 1-136 |
| 5.5.1.2.8 | Abnormal cases on the network side | clauses/5.5.1.2.8.md | 1-62 |
| 5.5.1.3 | Registration procedure for mobility and periodic registration update | clauses/5.5.1.3.md | 1-1 |
| 5.5.1.3.1 | General | clauses/5.5.1.3.1.md | 1-18 |
| 5.5.1.3.2 | Mobility and periodic registration update initiation | clauses/5.5.1.3.2.md | 1-560 |
| 5.5.1.3.3 | 5GMM common procedure initiation | clauses/5.5.1.3.3.md | 1-16 |
| 5.5.1.3.4 | Mobility and periodic registration update accepted by the network | clauses/5.5.1.3.4.md | 1-1252 |
| 5.5.1.3.5 | Mobility and periodic registration update not accepted by the network | clauses/5.5.1.3.5.md | 1-504 |
| 5.5.1.3.6 | Mobility and periodic registration update for initiating an emergency PDU session not accepted by the network | clauses/5.5.1.3.6.md | 1-22 |
| 5.5.1.3.6A | Mobility and periodic registration update for an emergency services fallback not accepted by the network | clauses/5.5.1.3.6A.md | 1-18 |
| 5.5.1.3.7 | Abnormal cases in the UE | clauses/5.5.1.3.7.md | 1-190 |
| 5.5.1.3.8 | Abnormal cases on the network side | clauses/5.5.1.3.8.md | 1-120 |
| 5.5.2 | De-registration procedure | clauses/5.5.2.md | 1-784 |
| 5.5.2.1 | General | clauses/5.5.2.md | 3-90 |
| 5.5.2.2 | UE-initiated de-registration procedure | clauses/5.5.2.md | 91-294 |
| 5.5.2.2.1 | UE-initiated de-registration procedure initiation | clauses/5.5.2.md | 93-130 |
| 5.5.2.2.2 | UE-initiated de-registration procedure completion | clauses/5.5.2.md | 131-136 |
| 5.5.2.2.3 | UE-initiated de-registration procedure completion for 5GS services over 3GPP access | clauses/5.5.2.md | 137-150 |
| 5.5.2.2.4 | UE-initiated de-registration procedure completion for 5GS services over non-3GPP access | clauses/5.5.2.md | 151-162 |
| 5.5.2.2.5 | UE-initiated de-registration procedure completion for 5GS services over both 3GPP access and non-3GPP access | clauses/5.5.2.md | 163-166 |
| 5.5.2.2.6 | Abnormal cases in the UE | clauses/5.5.2.md | 167-270 |
| 5.5.2.2.7 | Abnormal cases in the network side | clauses/5.5.2.md | 271-294 |
| 5.5.2.3 | Network-initiated de-registration procedure | clauses/5.5.2.md | 295-784 |
| 5.5.2.3.1 | Network-initiated de-registration procedure initiation | clauses/5.5.2.md | 297-366 |
| 5.5.2.3.2 | Network-initiated de-registration procedure completion by the UE | clauses/5.5.2.md | 367-710 |
| 5.5.2.3.3 | Network-initiated de-registration procedure completion by the network | clauses/5.5.2.md | 711-714 |
| 5.5.2.3.4 | Abnormal cases in the UE | clauses/5.5.2.md | 715-736 |
| 5.5.2.3.5 | Abnormal cases in the network side | clauses/5.5.2.md | 737-784 |
| 5.5.3 | eCall inactivity procedure | clauses/5.5.3.md | 1-36 |
| 5.5.4 | Authentication and key agreement procedure for 5G ProSe UE-to-network relay and 5G ProSe UE-to-UE relay | clauses/5.5.4.md | 1-140 |
| 5.5.4.1 | General | clauses/5.5.4.md | 3-30 |
| 5.5.4.2 | ProSe relay transaction identity (PRTI) | clauses/5.5.4.md | 31-36 |
| 5.5.4.3 | UE-initiated authentication and key agreement procedure initiation | clauses/5.5.4.md | 37-52 |
| 5.5.4.4 | UE-initiated authentication and key agreement procedure accepted by the network | clauses/5.5.4.md | 53-92 |
| 5.5.4.5 | UE-initiated authentication and key agreement procedure not accepted by the network | clauses/5.5.4.md | 93-108 |
| 5.5.4.6 | Abnormal cases in the UE | clauses/5.5.4.md | 109-124 |
| 5.5.4.7 | Abnormal cases on the network side | clauses/5.5.4.md | 125-140 |
| 5.6 | 5GMM connection management procedures | clauses/5.6.md | 1-1 |
| 5.6.1 | Service request procedure | clauses/5.6.1.md | 1-1 |
| 5.6.1.1 | General | clauses/5.6.1.1.md | 1-162 |
| 5.6.1.2 | Service request procedure initiation | clauses/5.6.1.2.md | 1-234 |
| 5.6.1.2.1 | UE is not using 5GS services with control plane CIoT 5GS optimization | clauses/5.6.1.2.md | 3-134 |
| 5.6.1.2.2 | UE is using 5GS services with control plane CIoT 5GS optimization | clauses/5.6.1.2.md | 135-234 |
| 5.6.1.3 | Common procedure initiation | clauses/5.6.1.3.md | 1-4 |
| 5.6.1.4 | Service request procedure accepted by the network | clauses/5.6.1.4.md | 1-362 |
| 5.6.1.4.1 | UE is not using 5GS services with control plane CIoT 5GS optimization | clauses/5.6.1.4.md | 3-170 |
| 5.6.1.4.2 | UE is using 5GS services with control plane CIoT 5GS optimization | clauses/5.6.1.4.md | 171-362 |
| 5.6.1.5 | Service request procedure not accepted by the network | clauses/5.6.1.5.md | 1-404 |
| 5.6.1.6 | Service request procedure for initiating an emergency PDU session not accepted by the network | clauses/5.6.1.6.md | 1-22 |
| 5.6.1.6A | Service request procedure for an emergency services fallback not accepted by the network | clauses/5.6.1.6A.md | 1-12 |
| 5.6.1.7 | Abnormal cases in the UE | clauses/5.6.1.7.md | 1-202 |
| 5.6.1.8 | Abnormal cases on the network side | clauses/5.6.1.8.md | 1-54 |
| 5.6.2 | Paging procedure | clauses/5.6.2.md | 1-138 |
| 5.6.2.1 | General | clauses/5.6.2.md | 3-20 |
| 5.6.2.2 | Paging for 5GS services | clauses/5.6.2.md | 21-138 |
| 5.6.2.2.1 | General | clauses/5.6.2.md | 23-120 |
| 5.6.2.2.2 | Abnormal cases on the network side | clauses/5.6.2.md | 121-126 |
| 5.6.2.2.3 | Abnormal cases in the UE | clauses/5.6.2.md | 127-138 |
| 5.6.3 | Notification procedure | clauses/5.6.3.md | 1-184 |
| 5.6.3.1 | General | clauses/5.6.3.md | 3-24 |
| 5.6.3.2 | Notification procedure initiation | clauses/5.6.3.md | 25-120 |
| 5.6.3.3 | Notification procedure completion | clauses/5.6.3.md | 121-150 |
| 5.6.3.4 | Abnormal cases on the network side | clauses/5.6.3.md | 151-172 |
| 5.6.3.5 | Abnormal cases on the UE side | clauses/5.6.3.md | 173-184 |
| 6 | Elementary procedures for 5GS session management | clauses/6.md | 1-1 |
| 6.1 | Overview | clauses/6.1.md | 1-762 |
| 6.1.1 | General | clauses/6.1.md | 3-20 |
| 6.1.2 | Types of 5GSM procedures | clauses/6.1.md | 21-60 |
| 6.1.3 | 5GSM sublayer states | clauses/6.1.md | 61-154 |
| 6.1.3.1 | General | clauses/6.1.md | 63-66 |
| 6.1.3.2 | 5GSM sublayer states in the UE | clauses/6.1.md | 67-112 |
| 6.1.3.2.1 | Overview | clauses/6.1.md | 69-80 |
| 6.1.3.2.2 | PDU SESSION INACTIVE | clauses/6.1.md | 81-84 |
| 6.1.3.2.3 | PDU SESSION ACTIVE PENDING | clauses/6.1.md | 85-88 |
| 6.1.3.2.4 | PDU SESSION ACTIVE | clauses/6.1.md | 89-92 |
| 6.1.3.2.5 | PDU SESSION INACTIVE PENDING | clauses/6.1.md | 93-96 |
| 6.1.3.2.6 | PDU SESSION MODIFICATION PENDING | clauses/6.1.md | 97-100 |
| 6.1.3.2.7 | PROCEDURE TRANSACTION INACTIVE | clauses/6.1.md | 101-104 |
| 6.1.3.2.8 | PROCEDURE TRANSACTION PENDING | clauses/6.1.md | 105-112 |
| 6.1.3.3 | 5GSM sublayer states in the network side | clauses/6.1.md | 113-154 |
| 6.1.3.3.1 | Overview | clauses/6.1.md | 115-126 |
| 6.1.3.3.2 | PDU SESSION INACTIVE | clauses/6.1.md | 127-130 |
| 6.1.3.3.3 | PDU SESSION ACTIVE | clauses/6.1.md | 131-134 |
| 6.1.3.3.4 | PDU SESSION INACTIVE PENDING | clauses/6.1.md | 135-138 |
| 6.1.3.3.5 | PDU SESSION MODIFICATION PENDING | clauses/6.1.md | 139-142 |
| 6.1.3.3.6 | PROCEDURE TRANSACTION INACTIVE | clauses/6.1.md | 143-146 |
| 6.1.3.3.7 | PROCEDURE TRANSACTION PENDING | clauses/6.1.md | 147-154 |
| 6.1.4 | Coordination between 5GSM and ESM | clauses/6.1.md | 155-722 |
| 6.1.4.1 | Coordination between 5GSM and ESM with N26 interface | clauses/6.1.md | 157-622 |
| 6.1.4.2 | Coordination between 5GSM and ESM without N26 interface | clauses/6.1.md | 623-722 |
| 6.1.4a | Coordination between 5GSM and SM | clauses/6.1.md | 723-728 |
| 6.1.5 | Coordination for interworking with ePDG connected to EPC | clauses/6.1.md | 729-762 |
| 6.2 | General on elementary 5GSM procedures | clauses/6.2.md | 1-1042 |
| 6.2.1 | Principles of PTI handling for 5GSM procedures | clauses/6.2.md | 3-28 |
| 6.2.2 | PDU session types | clauses/6.2.md | 29-46 |
| 6.2.3 | PDU session management | clauses/6.2.md | 47-68 |
| 6.2.4 | IP address allocation | clauses/6.2.md | 69-162 |
| 6.2.4.1 | General | clauses/6.2.md | 71-98 |
| 6.2.4.2 | IP address allocation via NAS signalling | clauses/6.2.md | 99-122 |
| 6.2.4.2a | IPv6 prefix delegation via DHCPv6 | clauses/6.2.md | 123-132 |
| 6.2.4.3 | Additional RG related requirements for IP address allocation | clauses/6.2.md | 133-156 |
| 6.2.4.4 | Additional requirements of the UE acting as 5G ProSe layer-3 UE-to-network relay UE for IP address allocation | clauses/6.2.md | 157-162 |
| 6.2.5 | Quality of service | clauses/6.2.md | 163-492 |
| 6.2.5.1 | General | clauses/6.2.md | 165-468 |
| 6.2.5.1.1 | QoS rules | clauses/6.2.md | 167-308 |
| 6.2.5.1.1.1 | General | clauses/6.2.md | 169-174 |
| 6.2.5.1.1.2 | Signalled QoS rules | clauses/6.2.md | 175-254 |
| 6.2.5.1.1.3 | Derived QoS rules | clauses/6.2.md | 255-280 |
| 6.2.5.1.1.4 | QoS flow descriptions | clauses/6.2.md | 281-308 |
| 6.2.5.1.2 | Session-AMBR | clauses/6.2.md | 309-314 |
| 6.2.5.1.2A | Void | clauses/6.2.md | 315-316 |
| 6.2.5.1.3 | UL user data packet matching | clauses/6.2.md | 317-334 |
| 6.2.5.1.4 | Reflective QoS | clauses/6.2.md | 335-468 |
| 6.2.5.1.4.1 | General | clauses/6.2.md | 337-346 |
| 6.2.5.1.4.2 | Derivation of packet filter for UL direction from DL user data packet | clauses/6.2.md | 347-432 |
| 6.2.5.1.4.3 | Creating a derived QoS rule by reflective QoS in the UE | clauses/6.2.md | 433-444 |
| 6.2.5.1.4.4 | Updating a derived QoS rule by reflective QoS in the UE | clauses/6.2.md | 445-452 |
| 6.2.5.1.4.5 | Deleting a derived QoS rule in the UE | clauses/6.2.md | 453-464 |
| 6.2.5.1.4.6 | Ignoring RQI in the UE | clauses/6.2.md | 465-468 |
| 6.2.5.2 | QoS in MA PDU session | clauses/6.2.md | 469-492 |
| 6.2.6 | Local area data network (LADN) | clauses/6.2.md | 493-586 |
| 6.2.7 | Handling of DNN based congestion control | clauses/6.2.md | 587-626 |
| 6.2.8 | Handling of S-NSSAI based congestion control | clauses/6.2.md | 627-776 |
| 6.2.9 | Interaction with upper layers | clauses/6.2.md | 777-804 |
| 6.2.9.1 | General | clauses/6.2.md | 779-782 |
| 6.2.9.2 | URSP | clauses/6.2.md | 783-792 |
| 6.2.9.3 | ProSeP | clauses/6.2.md | 793-804 |
| 6.2.10 | Handling of 3GPP PS data off | clauses/6.2.md | 805-872 |
| 6.2.11 | Multi-homed IPv6 PDU session | clauses/6.2.md | 873-886 |
| 6.2.12 | Handling of network rejection not due to congestion control | clauses/6.2.md | 887-920 |
| 6.2.13 | Handling of Small data rate control | clauses/6.2.md | 921-956 |
| 6.2.14 | Handling of Serving PLMN rate control | clauses/6.2.md | 957-968 |
| 6.2.15 | Handling of Reliable Data Service | clauses/6.2.md | 969-978 |
| 6.2.16 | Handling of header compression for control plane CIoT optimizations | clauses/6.2.md | 979-992 |
| 6.2.17 | Handling of edge computing enhancements | clauses/6.2.md | 993-1018 |
| 6.2.18 | Support of redundant PDU sessions | clauses/6.2.md | 1019-1026 |
| 6.2.19 | Handling of maximum group data rate limitation control | clauses/6.2.md | 1027-1034 |
| 6.2.20 | Support of UL PDU set handling | clauses/6.2.md | 1035-1042 |
| 6.3 | Network-requested 5GSM procedures | clauses/6.3.md | 1-1 |
| 6.3.1 | PDU session authentication and authorization procedure | clauses/6.3.1.md | 1-182 |
| 6.3.1.1 | General | clauses/6.3.1.md | 3-60 |
| 6.3.1.2 | PDU EAP message reliable transport procedure | clauses/6.3.1.md | 61-154 |
| 6.3.1.2.1 | PDU EAP message reliable transport procedure initiation | clauses/6.3.1.md | 63-120 |
| 6.3.1.2.2 | PDU EAP message reliable transport procedure accepted by the UE | clauses/6.3.1.md | 121-130 |
| 6.3.1.2.3 | Abnormal cases on the network side | clauses/6.3.1.md | 131-142 |
| 6.3.1.2.4 | Abnormal cases in the UE | clauses/6.3.1.md | 143-154 |
| 6.3.1.3 | PDU EAP result message transport procedure | clauses/6.3.1.md | 155-182 |
| 6.3.1.3.1 | PDU EAP result message transport procedure initiation | clauses/6.3.1.md | 157-170 |
| 6.3.1.3.2 | Abnormal cases in the UE | clauses/6.3.1.md | 171-182 |
| 6.3.1A | Service-level authentication and authorization procedure | clauses/6.3.1A.md | 1-126 |
| 6.3.2 | Network-requested PDU session modification procedure | clauses/6.3.2.md | 1-750 |
| 6.3.2.1 | General | clauses/6.3.2.md | 3-6 |
| 6.3.2.2 | Network-requested PDU session modification procedure initiation | clauses/6.3.2.md | 7-192 |
| 6.3.2.3 | Network-requested PDU session modification procedure accepted by the UE | clauses/6.3.2.md | 193-520 |
| 6.3.2.4 | Network-requested PDU session modification procedure not accepted by the UE | clauses/6.3.2.md | 521-686 |
| 6.3.2.5 | Abnormal cases on the network side | clauses/6.3.2.md | 687-734 |
| 6.3.2.6 | Abnormal cases in the UE | clauses/6.3.2.md | 735-750 |
| 6.3.3 | Network-requested PDU session release procedure | clauses/6.3.3.md | 1-676 |
| 6.3.3.1 | General | clauses/6.3.3.md | 3-6 |
| 6.3.3.2 | Network-requested PDU session release procedure initiation | clauses/6.3.3.md | 7-98 |
| 6.3.3.3 | Network-requested PDU session release procedure accepted by the UE | clauses/6.3.3.md | 99-636 |
| 6.3.3.4 | N1 SM delivery skipped | clauses/6.3.3.md | 637-640 |
| 6.3.3.5 | Abnormal cases on the network side | clauses/6.3.3.md | 641-664 |
| 6.3.3.6 | Abnormal cases in the UE | clauses/6.3.3.md | 665-676 |
| 6.4 | UE-requested 5GSM procedures | clauses/6.4.md | 1-1 |
| 6.4.1 | UE-requested PDU session establishment procedure | clauses/6.4.1.md | 1-1 |
| 6.4.1.1 | General | clauses/6.4.1.1.md | 1-26 |
| 6.4.1.2 | UE-requested PDU session establishment procedure initiation | clauses/6.4.1.2.md | 1-440 |
| 6.4.1.3 | UE-requested PDU session establishment procedure accepted by the network | clauses/6.4.1.3.md | 1-502 |
| 6.4.1.4 | UE-requested PDU session establishment procedure not accepted by the network | clauses/6.4.1.4.md | 1-860 |
| 6.4.1.4.1 | General | clauses/6.4.1.4.md | 3-156 |
| 6.4.1.4.2 | Handling of network rejection due to congestion control | clauses/6.4.1.4.md | 157-542 |
| 6.4.1.4.3 | Handling of network rejection not due to congestion control | clauses/6.4.1.4.md | 543-860 |
| 6.4.1.5 | Handling the maximum number of established PDU sessions | clauses/6.4.1.5.md | 1-50 |
| 6.4.1.5A | Handling the maximum number of allowed active user-plane resources for PDU sessions of UEs in NB-N1 mode | clauses/6.4.1.5A.md | 1-16 |
| 6.4.1.6 | Abnormal cases in the UE | clauses/6.4.1.6.md | 1-74 |
| 6.4.1.7 | Abnormal cases on the network side | clauses/6.4.1.7.md | 1-26 |
| 6.4.2 | UE-requested PDU session modification procedure | clauses/6.4.2.md | 1-930 |
| 6.4.2.1 | General | clauses/6.4.2.md | 3-44 |
| 6.4.2.2 | UE-requested PDU session modification procedure initiation | clauses/6.4.2.md | 45-246 |
| 6.4.2.3 | UE-requested PDU session modification procedure accepted by the network | clauses/6.4.2.md | 247-252 |
| 6.4.2.4 | UE-requested PDU session modification procedure not accepted by the network | clauses/6.4.2.md | 253-844 |
| 6.4.2.4.1 | General | clauses/6.4.2.md | 255-316 |
| 6.4.2.4.2 | Handling of network rejection due to congestion control | clauses/6.4.2.md | 317-708 |
| 6.4.2.4.3 | Handling of network rejection not due to congestion control | clauses/6.4.2.md | 709-844 |
| 6.4.2.5 | Abnormal cases in the UE | clauses/6.4.2.md | 845-894 |
| 6.4.2.6 | Abnormal cases on the network side | clauses/6.4.2.md | 895-930 |
| 6.4.3 | UE-requested PDU session release procedure | clauses/6.4.3.md | 1-126 |
| 6.4.3.1 | General | clauses/6.4.3.md | 3-14 |
| 6.4.3.2 | UE-requested PDU session release procedure initiation | clauses/6.4.3.md | 15-52 |
| 6.4.3.3 | UE-requested PDU session release procedure accepted by the network | clauses/6.4.3.md | 53-56 |
| 6.4.3.4 | UE-requested PDU session release procedure not accepted by the network | clauses/6.4.3.md | 57-74 |
| 6.4.3.5 | Abnormal cases in the UE | clauses/6.4.3.md | 75-118 |
| 6.4.3.6 | Abnormal cases on the network side | clauses/6.4.3.md | 119-126 |
| 6.5 | 5GSM status procedure | clauses/6.5.md | 1-56 |
| 6.5.1 | General | clauses/6.5.md | 3-10 |
| 6.5.2 | 5GSM status received in the UE | clauses/6.5.md | 11-28 |
| 6.5.3 | 5GSM status received in the SMF | clauses/6.5.md | 29-56 |
| 6.6 | Miscellaneous procedures | clauses/6.6.md | 1-90 |
| 6.6.1 | Exchange of extended protocol configuration options | clauses/6.6.md | 3-8 |
| 6.6.2 | Remote UE report procedure | clauses/6.6.md | 9-90 |
| 6.6.2.1 | General | clauses/6.6.md | 11-20 |
| 6.6.2.2 | Remote UE report procedure initiation | clauses/6.6.md | 21-48 |
| 6.6.2.3 | Remote UE report procedure accepted by the network | clauses/6.6.md | 49-56 |
| 6.6.2.4 | Abnormal cases in the UE | clauses/6.6.md | 57-78 |
| 6.6.2.5 | Abnormal cases on the network side | clauses/6.6.md | 79-90 |
| 7 | Handling of unknown, unforeseen, and erroneous protocol data | clauses/7.md | 1-252 |
| 7.1 | General | clauses/7.md | 3-16 |
| 7.2 | Message too short or too long | clauses/7.md | 17-30 |
| 7.2.1 | Message too short | clauses/7.md | 19-22 |
| 7.2.2 | Message too long | clauses/7.md | 23-30 |
| 7.3 | Unknown or unforeseen procedure transaction identity or PDU Session identity | clauses/7.md | 31-92 |
| 7.3.1 | Procedure transaction identity | clauses/7.md | 33-70 |
| 7.3.2 | PDU Session identity | clauses/7.md | 71-92 |
| 7.4 | Unknown or unforeseen message type | clauses/7.md | 93-104 |
| 7.5 | Non-semantical mandatory information element errors | clauses/7.md | 105-158 |
| 7.5.1 | Common procedures | clauses/7.md | 107-134 |
| 7.5.2 | 5GS mobility management | clauses/7.md | 135-140 |
| 7.5.3 | 5GS session management | clauses/7.md | 141-158 |
| 7.6 | Unknown and unforeseen IEs in the non-imperative message part | clauses/7.md | 159-200 |
| 7.6.1 | IEIs unknown in the message | clauses/7.md | 161-166 |
| 7.6.2 | Out of sequence IEs | clauses/7.md | 167-172 |
| 7.6.3 | Repeated IEs | clauses/7.md | 173-178 |
| 7.6.4 | Unknown and unforeseen IEs in a Type 6 IE container information element | clauses/7.md | 179-200 |
| 7.6.4.1 | IEIs unknown in the Type 6 IE container information element | clauses/7.md | 181-188 |
| 7.6.4.2 | Out of sequence IEs | clauses/7.md | 189-194 |
| 7.6.4.3 | Repeated IEs | clauses/7.md | 195-200 |
| 7.7 | Non-imperative message part errors | clauses/7.md | 201-246 |
| 7.7.1 | Syntactically incorrect optional IEs | clauses/7.md | 209-214 |
| 7.7.2 | Conditional IE errors | clauses/7.md | 215-224 |
| 7.7.3 | Errors in a Type 6 IE container information element | clauses/7.md | 225-246 |
| 7.7.3.1 | Syntactically incorrect optional IEs | clauses/7.md | 227-236 |
| 7.7.3.2 | Conditional IE errors | clauses/7.md | 237-246 |
| 7.8 | Messages with semantically incorrect contents | clauses/7.md | 247-252 |
| 8 | Message functional definitions and contents | clauses/8.md | 1-1 |
| 8.1 | Overview | clauses/8.1.md | 1-38 |
| 8.2 | 5GS mobility management messages | clauses/8.2.md | 1-2308 |
| 8.2.1 | Authentication request | clauses/8.2.md | 3-44 |
| 8.2.1.1 | Message definition | clauses/8.2.md | 5-30 |
| 8.2.1.2 | Authentication parameter RAND | clauses/8.2.md | 31-34 |
| 8.2.1.3 | Authentication parameter AUTN | clauses/8.2.md | 35-38 |
| 8.2.1.4 | Void | clauses/8.2.md | 39-40 |
| 8.2.1.5 | EAP message | clauses/8.2.md | 41-44 |
| 8.2.2 | Authentication response | clauses/8.2.md | 45-76 |
| 8.2.2.1 | Message definition | clauses/8.2.md | 47-68 |
| 8.2.2.2 | Authentication response parameter | clauses/8.2.md | 69-72 |
| 8.2.2.3 | EAP message | clauses/8.2.md | 73-76 |
| 8.2.3 | Authentication result | clauses/8.2.md | 77-113 |
| 8.2.3.1 | Message definition | clauses/8.2.md | 79-105 |
| 8.2.3.2 | ABBA | clauses/8.2.md | 106-109 |
| 8.2.3.3 | AUN3 device security key | clauses/8.2.md | 110-113 |
| 8.2.4 | Authentication failure | clauses/8.2.md | 114-141 |
| 8.2.4.1 | Message definition | clauses/8.2.md | 116-137 |
| 8.2.4.2 | Authentication failure parameter | clauses/8.2.md | 138-141 |
| 8.2.5 | Authentication reject | clauses/8.2.md | 142-168 |
| 8.2.5.1 | Message definition | clauses/8.2.md | 144-164 |
| 8.2.5.2 | EAP message | clauses/8.2.md | 165-168 |
| 8.2.6 | Registration request | clauses/8.2.md | 169-449 |
| 8.2.6.1 | Message definition | clauses/8.2.md | 171-235 |
| 8.2.6.2 | Non-current native NAS key set identifier | clauses/8.2.md | 236-239 |
| 8.2.6.3 | 5GMM capability | clauses/8.2.md | 240-243 |
| 8.2.6.4 | UE security capability | clauses/8.2.md | 244-247 |
| 8.2.6.5 | Requested NSSAI | clauses/8.2.md | 248-255 |
| 8.2.6.6 | Last visited registered TAI | clauses/8.2.md | 256-259 |
| 8.2.6.7 | S1 UE network capability | clauses/8.2.md | 260-263 |
| 8.2.6.8 | Uplink data status | clauses/8.2.md | 264-267 |
| 8.2.6.9 | PDU session status | clauses/8.2.md | 268-271 |
| 8.2.6.10 | MICO indication | clauses/8.2.md | 272-275 |
| 8.2.6.11 | UE status | clauses/8.2.md | 276-279 |
| 8.2.6.12 | Additional GUTI | clauses/8.2.md | 280-287 |
| 8.2.6.13 | Allowed PDU session status | clauses/8.2.md | 288-291 |
| 8.2.6.14 | UE's usage setting | clauses/8.2.md | 292-295 |
| 8.2.6.15 | Requested DRX parameters | clauses/8.2.md | 296-299 |
| 8.2.6.16 | EPS NAS message container | clauses/8.2.md | 300-315 |
| 8.2.6.17 | LADN indication | clauses/8.2.md | 316-319 |
| 8.2.6.17A | Payload container type | clauses/8.2.md | 320-325 |
| 8.2.6.18 | Payload container | clauses/8.2.md | 326-339 |
| 8.2.6.19 | Network slicing indication | clauses/8.2.md | 340-343 |
| 8.2.6.20 | 5GS update type | clauses/8.2.md | 344-353 |
| 8.2.6.21 | NAS message container | clauses/8.2.md | 354-357 |
| 8.2.6.22 | Requested extended DRX parameters | clauses/8.2.md | 358-361 |
| 8.2.6.23 | EPS bearer context status | clauses/8.2.md | 362-365 |
| 8.2.6.24 | T3324 value | clauses/8.2.md | 366-369 |
| 8.2.6.25 | Mobile station classmark 2 | clauses/8.2.md | 370-373 |
| 8.2.6.26 | Supported codecs | clauses/8.2.md | 374-377 |
| 8.2.6.27 | UE radio capability ID | clauses/8.2.md | 378-381 |
| 8.2.6.28 | Requested mapped NSSAI | clauses/8.2.md | 382-385 |
| 8.2.6.29 | Additional information requested | clauses/8.2.md | 386-389 |
| 8.2.6.30 | Requested WUS assistance information | clauses/8.2.md | 390-399 |
| 8.2.6.31 | Void | clauses/8.2.md | 400-401 |
| 8.2.6.32 | N5GC indication | clauses/8.2.md | 402-405 |
| 8.2.6.33 | Requested NB-N1 mode DRX parameters | clauses/8.2.md | 406-409 |
| 8.2.6.34 | UE request type | clauses/8.2.md | 410-413 |
| 8.2.6.35 | Paging restriction | clauses/8.2.md | 414-417 |
| 8.2.6.35 | Service-level-AA container | clauses/8.2.md | 418-421 |
| 8.2.6.36 | NID | clauses/8.2.md | 422-425 |
| 8.2.6.37 | UE determined PLMN with disaster condition | clauses/8.2.md | 426-429 |
| 8.2.6.38 | Requested PEIPS assistance information | clauses/8.2.md | 430-433 |
| 8.2.6.39 | Requested T3512 value | clauses/8.2.md | 434-437 |
| 8.2.6.40 | Unavailability information | clauses/8.2.md | 438-441 |
| 8.2.6.41 | Non-3GPP path switching information | clauses/8.2.md | 442-445 |
| 8.2.6.42 | AUN3 indication | clauses/8.2.md | 446-449 |
| 8.2.7 | Registration accept | clauses/8.2.md | 450-862 |
| 8.2.7.1 | Message definition | clauses/8.2.md | 452-532 |
| 8.2.7.2 | 5G-GUTI | clauses/8.2.md | 533-536 |
| 8.2.7.3 | Equivalent PLMNs | clauses/8.2.md | 537-540 |
| 8.2.7.4 | TAI list | clauses/8.2.md | 541-544 |
| 8.2.7.5 | Allowed NSSAI | clauses/8.2.md | 545-562 |
| 8.2.7.6 | Rejected NSSAI | clauses/8.2.md | 563-566 |
| 8.2.7.7 | Configured NSSAI | clauses/8.2.md | 567-570 |
| 8.2.7.8 | 5GS network feature support | clauses/8.2.md | 571-574 |
| 8.2.7.9 | PDU session status | clauses/8.2.md | 575-578 |
| 8.2.7.10 | PDU session reactivation result | clauses/8.2.md | 579-586 |
| 8.2.7.11 | PDU session reactivation result error cause | clauses/8.2.md | 587-590 |
| 8.2.7.12 | LADN information | clauses/8.2.md | 591-594 |
| 8.2.7.13 | MICO indication | clauses/8.2.md | 595-602 |
| 8.2.7.14 | Network slicing indication | clauses/8.2.md | 603-606 |
| 8.2.7.15 | Service area list | clauses/8.2.md | 607-610 |
| 8.2.7.16 | T3512 value | clauses/8.2.md | 611-614 |
| 8.2.7.17 | Non-3GPP de-registration timer value | clauses/8.2.md | 615-618 |
| 8.2.7.18 | T3502 value | clauses/8.2.md | 619-622 |
| 8.2.7.19 | Emergency number list | clauses/8.2.md | 623-626 |
| 8.2.7.20 | Extended emergency number list | clauses/8.2.md | 627-630 |
| 8.2.7.21 | SOR transparent container | clauses/8.2.md | 631-634 |
| 8.2.7.22 | EAP message | clauses/8.2.md | 635-638 |
| 8.2.7.23 | NSSAI inclusion mode | clauses/8.2.md | 639-642 |
| 8.2.7.24 | Operator-defined access category definitions | clauses/8.2.md | 643-646 |
| 8.2.7.25 | Negotiated DRX parameters | clauses/8.2.md | 647-650 |
| 8.2.7.26 | Non-3GPP NW policies | clauses/8.2.md | 651-658 |
| 8.2.7.27 | Negotiated extended DRX parameters | clauses/8.2.md | 659-666 |
| 8.2.7.28 | T3447 value | clauses/8.2.md | 667-674 |
| 8.2.7.29 | T3448 value | clauses/8.2.md | 675-678 |
| 8.2.7.30 | T3324 value | clauses/8.2.md | 679-682 |
| 8.2.7.31 | EPS bearer context status | clauses/8.2.md | 683-686 |
| 8.2.7.32 | UE radio capability ID | clauses/8.2.md | 687-690 |
| 8.2.7.33 | UE radio capability ID deletion indication | clauses/8.2.md | 691-694 |
| 8.2.7.34 | Pending NSSAI | clauses/8.2.md | 695-698 |
| 8.2.7.35 | Ciphering key data | clauses/8.2.md | 699-702 |
| 8.2.7.36 | CAG information list | clauses/8.2.md | 703-706 |
| 8.2.7.37 | Truncated 5G-S-TMSI configuration | clauses/8.2.md | 707-718 |
| 8.2.7.38 | Negotiated NB-N1 mode DRX parameters | clauses/8.2.md | 719-722 |
| 8.2.7.39 | Negotiated WUS assistance information | clauses/8.2.md | 723-734 |
| 8.2.7.40 | Extended rejected NSSAI | clauses/8.2.md | 735-738 |
| 8.2.7.41 | Service-level-AA container | clauses/8.2.md | 739-742 |
| 8.2.7.42 | Negotiated PEIPS assistance information | clauses/8.2.md | 743-752 |
| 8.2.7.43 | 5GS additional request result | clauses/8.2.md | 753-756 |
| 8.2.7.44 | NSSRG information | clauses/8.2.md | 757-760 |
| 8.2.7.45 | Disaster roaming wait range | clauses/8.2.md | 761-764 |
| 8.2.7.46 | Disaster return wait range | clauses/8.2.md | 765-768 |
| 8.2.7.47 | List of PLMNs to be used in disaster condition | clauses/8.2.md | 769-772 |
| 8.2.7.48 | Forbidden TAI(s) for the list of "5GS forbidden tracking areas for roaming" | clauses/8.2.md | 773-776 |
| 8.2.7.49 | Forbidden TAI(s) for the list of "5GS forbidden tracking areas for regional provision of service" | clauses/8.2.md | 777-780 |
| 8.2.7.50 | Extended CAG information list | clauses/8.2.md | 781-784 |
| 8.2.7.51 | NSAG information | clauses/8.2.md | 785-788 |
| 8.2.7.52 | Equivalent SNPNs | clauses/8.2.md | 789-792 |
| 8.2.7.53 | NID | clauses/8.2.md | 793-796 |
| 8.2.7.54 | Registration accept type 6 IE container | clauses/8.2.md | 797-834 |
| 8.2.7.54.1 | General | clauses/8.2.md | 799-814 |
| 8.2.7.54.2 | Extended LADN information | clauses/8.2.md | 815-818 |
| 8.2.7.54.3 | S-NSSAI location validity information | clauses/8.2.md | 819-822 |
| 8.2.7.54.4 | Void | clauses/8.2.md | 823-826 |
| 8.2.7.54.5 | Partially allowed NSSAI | clauses/8.2.md | 827-830 |
| 8.2.7.54.6 | Partially rejected NSSAI | clauses/8.2.md | 831-834 |
| 8.2.7.55 | RAN timing synchronization | clauses/8.2.md | 835-838 |
| 8.2.7.56 | Alternative NSSAI | clauses/8.2.md | 839-842 |
| 8.2.7.57 | Maximum time offset | clauses/8.2.md | 843-846 |
| 8.2.7.58 | S-NSSAI time validity information | clauses/8.2.md | 847-850 |
| 8.2.7.59 | Unavailability configuration | clauses/8.2.md | 851-854 |
| 8.2.7.60 | Feature authorization indication | clauses/8.2.md | 855-858 |
| 8.2.7.61 | On-demand NSSAI | clauses/8.2.md | 859-862 |
| 8.2.8 | Registration complete | clauses/8.2.md | 863-889 |
| 8.2.8.1 | Message definition | clauses/8.2.md | 865-885 |
| 8.2.8.2 | SOR transparent container | clauses/8.2.md | 886-889 |
| 8.2.9 | Registration reject | clauses/8.2.md | 890-984 |
| 8.2.9.1 | Message definition | clauses/8.2.md | 892-928 |
| 8.2.9.2 | T3346 value | clauses/8.2.md | 929-932 |
| 8.2.9.3 | T3502 value | clauses/8.2.md | 933-936 |
| 8.2.9.4 | EAP message | clauses/8.2.md | 937-940 |
| 8.2.9.5 | Rejected NSSAI | clauses/8.2.md | 941-944 |
| 8.2.9.6 | CAG information list | clauses/8.2.md | 945-948 |
| 8.2.9.7 | Extended rejected NSSAI | clauses/8.2.md | 949-952 |
| 8.2.9.8 | Disaster return wait range | clauses/8.2.md | 953-956 |
| 8.2.9.9 | Extended CAG information list | clauses/8.2.md | 957-960 |
| 8.2.9.10 | Lower bound timer value | clauses/8.2.md | 961-964 |
| 8.2.9.11 | Forbidden TAI(s) for the list of "5GS forbidden tracking areas for roaming" | clauses/8.2.md | 965-968 |
| 8.2.9.12 | Forbidden TAI(s) for the list of "5GS forbidden tracking areas for regional provision of service" | clauses/8.2.md | 969-972 |
| 8.2.9.13 | N3IWF identifier | clauses/8.2.md | 973-976 |
| 8.2.9.14 | TNAN information | clauses/8.2.md | 977-980 |
| 8.2.9.15 | Extended 5GMM cause | clauses/8.2.md | 981-984 |
| 8.2.10 | UL NAS transport | clauses/8.2.md | 985-1068 |
| 8.2.10.1 | Message definition | clauses/8.2.md | 987-1020 |
| 8.2.10.2 | PDU session ID | clauses/8.2.md | 1021-1024 |
| 8.2.10.3 | Old PDU session ID | clauses/8.2.md | 1025-1028 |
| 8.2.10.4 | Request type | clauses/8.2.md | 1029-1032 |
| 8.2.10.5 | S-NSSAI | clauses/8.2.md | 1033-1036 |
| 8.2.10.6 | DNN | clauses/8.2.md | 1037-1040 |
| 8.2.10.7 | Additional information | clauses/8.2.md | 1041-1044 |
| 8.2.10.8 | MA PDU session information | clauses/8.2.md | 1045-1048 |
| 8.2.10.9 | Release assistance indication | clauses/8.2.md | 1049-1056 |
| 8.2.10.10 | Non-3GPP access path switching indication | clauses/8.2.md | 1057-1060 |
| 8.2.10.11 | Alternative S-NSSAI | clauses/8.2.md | 1061-1064 |
| 8.2.10.12 | Payload container information | clauses/8.2.md | 1065-1068 |
| 8.2.11 | DL NAS transport | clauses/8.2.md | 1069-1118 |
| 8.2.11.1 | Message definition | clauses/8.2.md | 1071-1098 |
| 8.2.11.2 | PDU session ID | clauses/8.2.md | 1099-1102 |
| 8.2.11.3 | Additional information | clauses/8.2.md | 1103-1106 |
| 8.2.11.4 | 5GMM cause | clauses/8.2.md | 1107-1110 |
| 8.2.11.5 | Back-off timer value | clauses/8.2.md | 1111-1114 |
| 8.2.11.6 | Lower bound timer value | clauses/8.2.md | 1115-1118 |
| 8.2.12 | De-registration request (UE originating de-registration) | clauses/8.2.md | 1119-1153 |
| 8.2.12.1 | Message definition | clauses/8.2.md | 1121-1145 |
| 8.2.12.2 | Unavailability information | clauses/8.2.md | 1146-1149 |
| 8.2.12.3 | NAS message container | clauses/8.2.md | 1150-1153 |
| 8.2.13 | De-registration accept (UE originating de-registration) | clauses/8.2.md | 1154-1175 |
| 8.2.13.1 | Message definition | clauses/8.2.md | 1156-1175 |
| 8.2.14 | De-registration request (UE terminated de-registration) | clauses/8.2.md | 1176-1251 |
| 8.2.14.1 | Message definition | clauses/8.2.md | 1178-1211 |
| 8.2.14.2 | 5GMM cause | clauses/8.2.md | 1212-1215 |
| 8.2.14.3 | T3346 value | clauses/8.2.md | 1216-1219 |
| 8.2.14.4 | Rejected NSSAI | clauses/8.2.md | 1220-1223 |
| 8.2.14.5 | CAG information list | clauses/8.2.md | 1224-1227 |
| 8.2.14.6 | Extended rejected NSSAI | clauses/8.2.md | 1228-1231 |
| 8.2.14.7 | Disaster return wait range | clauses/8.2.md | 1232-1235 |
| 8.2.14.7A | Extended CAG information list | clauses/8.2.md | 1236-1239 |
| 8.2.14.8 | Lower bound timer value | clauses/8.2.md | 1240-1243 |
| 8.2.14.9 | Forbidden TAI(s) for the list of "5GS forbidden tracking areas for roaming" | clauses/8.2.md | 1244-1247 |
| 8.2.14.10 | Forbidden TAI(s) for the list of "5GS forbidden tracking areas for regional provision of service" | clauses/8.2.md | 1248-1251 |
| 8.2.15 | De-registration accept (UE terminated de-registration) | clauses/8.2.md | 1252-1273 |
| 8.2.15.1 | Message definition | clauses/8.2.md | 1254-1273 |
| 8.2.16 | Service request | clauses/8.2.md | 1274-1328 |
| 8.2.16.1 | Message definition | clauses/8.2.md | 1276-1304 |
| 8.2.16.2 | Uplink data status | clauses/8.2.md | 1305-1308 |
| 8.2.16.3 | PDU session status | clauses/8.2.md | 1309-1312 |
| 8.2.16.4 | Allowed PDU session status | clauses/8.2.md | 1313-1316 |
| 8.2.16.5 | NAS message container | clauses/8.2.md | 1317-1320 |
| 8.2.16.6 | UE request type | clauses/8.2.md | 1321-1324 |
| 8.2.16.7 | Paging restriction | clauses/8.2.md | 1325-1328 |
| 8.2.17 | Service accept | clauses/8.2.md | 1329-1394 |
| 8.2.17.1 | Message definition | clauses/8.2.md | 1331-1358 |
| 8.2.17.2 | PDU session status | clauses/8.2.md | 1359-1362 |
| 8.2.17.3 | PDU session reactivation result | clauses/8.2.md | 1363-1370 |
| 8.2.17.4 | PDU session reactivation result error cause | clauses/8.2.md | 1371-1374 |
| 8.2.17.5 | EAP message | clauses/8.2.md | 1375-1378 |
| 8.2.17.6 | T3448 value | clauses/8.2.md | 1379-1382 |
| 8.2.17.7 | 5GS additional request result | clauses/8.2.md | 1383-1386 |
| 8.2.17.8 | Forbidden TAI(s) for the list of "5GS forbidden tracking areas for roaming" | clauses/8.2.md | 1387-1390 |
| 8.2.17.9 | Forbidden TAI(s) for the list of "5GS forbidden tracking areas for regional provision of service" | clauses/8.2.md | 1391-1394 |
| 8.2.18 | Service reject | clauses/8.2.md | 1395-1469 |
| 8.2.18.1 | Message definition | clauses/8.2.md | 1397-1429 |
| 8.2.18.2 | PDU session status | clauses/8.2.md | 1430-1433 |
| 8.2.18.3 | T3346 value | clauses/8.2.md | 1434-1437 |
| 8.2.18.4 | EAP message | clauses/8.2.md | 1438-1441 |
| 8.2.18.5 | T3448 value | clauses/8.2.md | 1442-1445 |
| 8.2.18.6 | CAG information list | clauses/8.2.md | 1446-1449 |
| 8.2.18.7 | Disaster return wait range | clauses/8.2.md | 1450-1453 |
| 8.2.18.8 | Extended CAG information list | clauses/8.2.md | 1454-1457 |
| 8.2.18.9 | Lower bound timer value | clauses/8.2.md | 1458-1461 |
| 8.2.18.10 | Forbidden TAI(s) for the list of "5GS forbidden tracking areas for roaming" | clauses/8.2.md | 1462-1465 |
| 8.2.18.11 | Forbidden TAI(s) for the list of "5GS forbidden tracking areas for regional provision of service" | clauses/8.2.md | 1466-1469 |
| 8.2.19 | Configuration update command | clauses/8.2.md | 1470-1711 |
| 8.2.19.1 | Message definition | clauses/8.2.md | 1472-1535 |
| 8.2.19.2 | Configuration update indication | clauses/8.2.md | 1536-1539 |
| 8.2.19.3 | 5G-GUTI | clauses/8.2.md | 1540-1543 |
| 8.2.19.4 | TAI list | clauses/8.2.md | 1544-1547 |
| 8.2.19.5 | Allowed NSSAI | clauses/8.2.md | 1548-1551 |
| 8.2.19.6 | Service area list | clauses/8.2.md | 1552-1555 |
| 8.2.19.7 | Full name for network | clauses/8.2.md | 1556-1559 |
| 8.2.19.8 | Short name for network | clauses/8.2.md | 1560-1563 |
| 8.2.19.9 | Local time zone | clauses/8.2.md | 1564-1567 |
| 8.2.19.10 | Universal time and local time zone | clauses/8.2.md | 1568-1571 |
| 8.2.19.11 | Network daylight saving time | clauses/8.2.md | 1572-1575 |
| 8.2.19.12 | LADN information | clauses/8.2.md | 1576-1579 |
| 8.2.19.13 | MICO indication | clauses/8.2.md | 1580-1583 |
| 8.2.19.14 | Network slicing indication | clauses/8.2.md | 1584-1587 |
| 8.2.19.15 | Configured NSSAI | clauses/8.2.md | 1588-1591 |
| 8.2.19.16 | Rejected NSSAI | clauses/8.2.md | 1592-1595 |
| 8.2.19.17 | Operator-defined access category definitions | clauses/8.2.md | 1596-1599 |
| 8.2.19.18 | SMS indication | clauses/8.2.md | 1600-1603 |
| 8.2.19.19 | T3447 value | clauses/8.2.md | 1604-1607 |
| 8.2.19.20 | CAG information list | clauses/8.2.md | 1608-1611 |
| 8.2.19.21 | UE radio capability ID | clauses/8.2.md | 1612-1615 |
| 8.2.19.22 | UE radio capability ID deletion indication | clauses/8.2.md | 1616-1619 |
| 8.2.19.23 | 5GS registration result | clauses/8.2.md | 1620-1623 |
| 8.2.19.24 | Truncated 5G-S-TMSI configuration | clauses/8.2.md | 1624-1627 |
| 8.2.19.25 | Additional configuration indication | clauses/8.2.md | 1628-1631 |
| 8.2.19.26 | Extended rejected NSSAI | clauses/8.2.md | 1632-1635 |
| 8.2.19.27 | Service-level-AA container | clauses/8.2.md | 1636-1639 |
| 8.2.19.28 | NSSRG information | clauses/8.2.md | 1640-1643 |
| 8.2.19.29 | Disaster roaming wait range | clauses/8.2.md | 1644-1647 |
| 8.2.19.30 | Disaster return wait range | clauses/8.2.md | 1648-1651 |
| 8.2.19.31 | List of PLMNs to be used in disaster condition | clauses/8.2.md | 1652-1655 |
| 8.2.19.32 | Extended CAG information list | clauses/8.2.md | 1656-1659 |
| 8.2.19.33 | Updated PEIPS assistance information | clauses/8.2.md | 1660-1663 |
| 8.2.19.34 | NSAG information | clauses/8.2.md | 1664-1667 |
| 8.2.19.35 | Priority indicator | clauses/8.2.md | 1668-1671 |
| 8.2.19.36 | RAN timing synchronization | clauses/8.2.md | 1672-1675 |
| 8.2.19.37 | Extended LADN information | clauses/8.2.md | 1676-1679 |
| 8.2.19.38 | Alternative NSSAI | clauses/8.2.md | 1680-1683 |
| 8.2.19.39 | S-NSSAI location validity information | clauses/8.2.md | 1684-1687 |
| 8.2.19.40 | S-NSSAI time validity information | clauses/8.2.md | 1688-1691 |
| 8.2.19.41 | Maximum time offset | clauses/8.2.md | 1692-1695 |
| 8.2.19.42 | Partially allowed NSSAI | clauses/8.2.md | 1696-1699 |
| 8.2.19.43 | Partially rejected NSSAI | clauses/8.2.md | 1700-1703 |
| 8.2.19.44 | Feature authorization indication | clauses/8.2.md | 1704-1707 |
| 8.2.19.45 | On-demand NSSAI | clauses/8.2.md | 1708-1711 |
| 8.2.20 | Configuration update complete | clauses/8.2.md | 1712-1735 |
| 8.2.20.1 | Message definition | clauses/8.2.md | 1714-1733 |
| 8.2.20.2 | Void | clauses/8.2.md | 1734-1735 |
| 8.2.21 | Identity request | clauses/8.2.md | 1736-1759 |
| 8.2.21.1 | Message definition | clauses/8.2.md | 1738-1759 |
| 8.2.22 | Identity response | clauses/8.2.md | 1760-1782 |
| 8.2.22.1 | Message definition | clauses/8.2.md | 1762-1782 |
| 8.2.23 | Notification | clauses/8.2.md | 1783-1806 |
| 8.2.23.1 | Message definition | clauses/8.2.md | 1785-1806 |
| 8.2.24 | Notification response | clauses/8.2.md | 1807-1833 |
| 8.2.24.1 | Message definition | clauses/8.2.md | 1809-1829 |
| 8.2.24.2 | PDU session status | clauses/8.2.md | 1830-1833 |
| 8.2.25 | Security mode command | clauses/8.2.md | 1834-1902 |
| 8.2.25.1 | Message definition | clauses/8.2.md | 1836-1868 |
| 8.2.25.2 | IMEISV request | clauses/8.2.md | 1869-1872 |
| 8.2.25.3 | Void | clauses/8.2.md | 1873-1874 |
| 8.2.25.4 | Selected EPS NAS security algorithms | clauses/8.2.md | 1875-1878 |
| 8.2.25.5 | Additional 5G security information | clauses/8.2.md | 1879-1886 |
| 8.2.25.6 | EAP message | clauses/8.2.md | 1887-1890 |
| 8.2.25.7 | ABBA | clauses/8.2.md | 1891-1894 |
| 8.2.25.8 | Replayed S1 UE security capabilities | clauses/8.2.md | 1895-1898 |
| 8.2.25.9 | AUN3 device security key | clauses/8.2.md | 1899-1902 |
| 8.2.26 | Security mode complete | clauses/8.2.md | 1903-1945 |
| 8.2.26.1 | Message definition | clauses/8.2.md | 1905-1927 |
| 8.2.26.2 | IMEISV | clauses/8.2.md | 1928-1931 |
| 8.2.26.3 | NAS message container | clauses/8.2.md | 1932-1939 |
| 8.2.26.4 | non-IMEISV PEI | clauses/8.2.md | 1940-1945 |
| 8.2.27 | Security mode reject | clauses/8.2.md | 1946-1968 |
| 8.6.27.1 | Message definition | clauses/8.2.md | 1948-1968 |
| 8.2.28 | Security protected 5GS NAS message | clauses/8.2.md | 1969-1994 |
| 8.2.28.1 | Message definition | clauses/8.2.md | 1971-1994 |
| 8.2.29 | 5GMM status | clauses/8.2.md | 1995-2017 |
| 8.2.29.1 | Message definition | clauses/8.2.md | 1997-2017 |
| 8.2.30 | Control Plane Service request | clauses/8.2.md | 2018-2107 |
| 8.2.30.1 | Message definition | clauses/8.2.md | 2020-2053 |
| 8.2.30.2 | CIoT small data container | clauses/8.2.md | 2054-2059 |
| 8.2.30.3 | Payload container type | clauses/8.2.md | 2060-2063 |
| 8.2.30.4 | Payload container | clauses/8.2.md | 2064-2067 |
| 8.2.30.5 | PDU session ID | clauses/8.2.md | 2068-2071 |
| 8.2.30.6 | PDU session status | clauses/8.2.md | 2072-2075 |
| 8.2.30.7 | Release assistance indication | clauses/8.2.md | 2076-2083 |
| 8.2.30.8 | Uplink data status | clauses/8.2.md | 2084-2087 |
| 8.2.30.9 | NAS message container | clauses/8.2.md | 2088-2091 |
| 8.2.30.10 | Additional information | clauses/8.2.md | 2092-2095 |
| 8.2.30.11 | Allowed PDU session status | clauses/8.2.md | 2096-2099 |
| 8.2.30.12 | UE request type | clauses/8.2.md | 2100-2103 |
| 8.2.30.13 | Paging restriction | clauses/8.2.md | 2104-2107 |
| 8.2.31 | Network slice-specific authentication command | clauses/8.2.md | 2108-2131 |
| 8.2.31.1 | Message definition | clauses/8.2.md | 2110-2131 |
| 8.2.32 | Network slice-specific authentication complete | clauses/8.2.md | 2132-2155 |
| 8.2.32.1 | Message definition | clauses/8.2.md | 2134-2155 |
| 8.2.33 | Network slice-specific authentication result | clauses/8.2.md | 2156-2179 |
| 8.2.33.1 | Message definition | clauses/8.2.md | 2158-2179 |
| 8.2.34 | Relay key request | clauses/8.2.md | 2180-2203 |
| 8.2.34.1 | Message definition | clauses/8.2.md | 2182-2203 |
| 8.2.35 | Relay key accept | clauses/8.2.md | 2204-2232 |
| 8.2.35.1 | Message definition | clauses/8.2.md | 2206-2228 |
| 8.2.35.2 | EAP message | clauses/8.2.md | 2229-2232 |
| 8.2.36 | Relay key reject | clauses/8.2.md | 2233-2260 |
| 8.2.36.1 | Message definition | clauses/8.2.md | 2235-2256 |
| 8.2.36.2 | EAP message | clauses/8.2.md | 2257-2260 |
| 8.2.37 | Relay authentication request | clauses/8.2.md | 2261-2284 |
| 8.2.37.1 | Message definition | clauses/8.2.md | 2263-2284 |
| 8.2.38 | Relay authentication response | clauses/8.2.md | 2285-2308 |
| 8.2.38.1 | Message definition | clauses/8.2.md | 2287-2308 |
| 8.3 | 5GS session management messages | clauses/8.3.md | 1-1057 |
| 8.3.1 | PDU session establishment request | clauses/8.3.md | 3-133 |
| 8.3.1.1 | Message definition | clauses/8.3.md | 5-43 |
| 8.3.1.2 | PDU session type | clauses/8.3.md | 44-47 |
| 8.3.1.3 | SSC mode | clauses/8.3.md | 48-51 |
| 8.3.1.4 | Maximum number of supported packet filters | clauses/8.3.md | 52-55 |
| 8.3.1.5 | 5GSM capability | clauses/8.3.md | 56-59 |
| 8.3.1.6 | Void | clauses/8.3.md | 60-61 |
| 8.3.1.7 | Always-on PDU session requested | clauses/8.3.md | 62-65 |
| 8.3.1.8 | SM PDU DN request container | clauses/8.3.md | 66-69 |
| 8.3.1.9 | Extended protocol configuration options | clauses/8.3.md | 70-73 |
| 8.3.1.10 | IP header compression configuration | clauses/8.3.md | 74-83 |
| 8.3.1.11 | DS-TT Ethernet port MAC address | clauses/8.3.md | 84-87 |
| 8.3.1.12 | UE-DS-TT residence time | clauses/8.3.md | 88-95 |
| 8.3.1.13 | Port management information container | clauses/8.3.md | 96-99 |
| 8.3.1.14 | Ethernet header compression configuration | clauses/8.3.md | 100-109 |
| 8.3.1.15 | Suggested interface identifier | clauses/8.3.md | 110-113 |
| 8.3.1.16 | Service-level-AA container | clauses/8.3.md | 114-117 |
| 8.3.1.17 | Requested MBS container | clauses/8.3.md | 118-121 |
| 8.3.1.18 | PDU session pair ID | clauses/8.3.md | 122-125 |
| 8.3.1.19 | RSN | clauses/8.3.md | 126-129 |
| 8.3.1.20 | URSP rule enforcement reports | clauses/8.3.md | 130-133 |
| 8.3.2 | PDU session establishment accept | clauses/8.3.md | 134-273 |
| 8.3.2.1 | Message definition | clauses/8.3.md | 136-179 |
| 8.3.2.2 | 5GSM cause | clauses/8.3.md | 180-183 |
| 8.3.2.3 | PDU address | clauses/8.3.md | 184-187 |
| 8.3.2.4 | RQ timer value | clauses/8.3.md | 188-191 |
| 8.3.2.5 | S-NSSAI | clauses/8.3.md | 192-195 |
| 8.3.2.6 | Always-on PDU session indication | clauses/8.3.md | 196-199 |
| 8.3.2.7 | Mapped EPS bearer contexts | clauses/8.3.md | 200-203 |
| 8.3.2.8 | EAP message | clauses/8.3.md | 204-207 |
| 8.3.2.9 | Authorized QoS flow descriptions | clauses/8.3.md | 208-211 |
| 8.3.2.10 | Extended protocol configuration options | clauses/8.3.md | 212-215 |
| 8.3.2.11 | DNN | clauses/8.3.md | 216-219 |
| 8.3.2.12 | 5GSM network feature support | clauses/8.3.md | 220-223 |
| 8.3.2.13 | Void | clauses/8.3.md | 224-225 |
| 8.3.2.14 | Serving PLMN rate control | clauses/8.3.md | 226-229 |
| 8.3.2.15 | ATSSS container | clauses/8.3.md | 230-233 |
| 8.3.2.16 | Control plane only indication | clauses/8.3.md | 234-237 |
| 8.3.2.17 | IP header compression configuration | clauses/8.3.md | 238-247 |
| 8.3.2.18 | Ethernet header compression configuration | clauses/8.3.md | 248-257 |
| 8.3.2.19 | Service-level-AA container | clauses/8.3.md | 258-261 |
| 8.3.2.20 | Received MBS container | clauses/8.3.md | 262-265 |
| 8.3.2.21 | N3QAI | clauses/8.3.md | 266-269 |
| 8.3.2.22 | Protocol description | clauses/8.3.md | 270-273 |
| 8.3.3 | PDU session establishment reject | clauses/8.3.md | 274-331 |
| 8.3.3.1 | Message definition | clauses/8.3.md | 276-303 |
| 8.3.3.2 | Back-off timer value | clauses/8.3.md | 304-307 |
| 8.3.3.3 | Allowed SSC mode | clauses/8.3.md | 308-311 |
| 8.3.3.4 | EAP message | clauses/8.3.md | 312-315 |
| 8.3.3.4A | 5GSM congestion re-attempt indicator | clauses/8.3.md | 316-319 |
| 8.3.3.5 | Extended protocol configuration options | clauses/8.3.md | 320-323 |
| 8.3.3.6 | Re-attempt indicator | clauses/8.3.md | 324-327 |
| 8.3.3.7 | Service-level-AA container | clauses/8.3.md | 328-331 |
| 8.3.4 | PDU session authentication command | clauses/8.3.md | 332-363 |
| 8.3.4.1 | Message definition | clauses/8.3.md | 334-355 |
| 8.3.4.2 | Extended protocol configuration options | clauses/8.3.md | 356-361 |
| 8.3.4.3 | Void | clauses/8.3.md | 362-363 |
| 8.3.5 | PDU session authentication complete | clauses/8.3.md | 364-395 |
| 8.3.5.1 | Message definition | clauses/8.3.md | 366-387 |
| 8.3.5.2 | Extended protocol configuration options | clauses/8.3.md | 388-393 |
| 8.3.5.3 | Void | clauses/8.3.md | 394-395 |
| 8.3.6 | PDU session authentication result | clauses/8.3.md | 396-429 |
| 8.3.6.1 | Message definition | clauses/8.3.md | 398-419 |
| 8.3.6.2 | EAP message | clauses/8.3.md | 420-423 |
| 8.3.6.3 | Extended protocol configuration options | clauses/8.3.md | 424-429 |
| 8.3.7 | PDU session modification request | clauses/8.3.md | 430-549 |
| 8.3.7.1 | Message definition | clauses/8.3.md | 432-469 |
| 8.3.7.2 | 5GSM capability | clauses/8.3.md | 470-481 |
| 8.3.7.3 | 5GSM cause | clauses/8.3.md | 482-485 |
| 8.3.7.4 | Maximum number of supported packet filters | clauses/8.3.md | 486-489 |
| 8.3.7.5 | Always-on PDU session requested | clauses/8.3.md | 490-493 |
| 8.3.7.6 | Integrity protection maximum data rate | clauses/8.3.md | 494-497 |
| 8.3.7.7 | Requested QoS rules | clauses/8.3.md | 498-501 |
| 8.3.7.8 | Requested QoS flow descriptions | clauses/8.3.md | 502-505 |
| 8.3.7.9 | Extended protocol configuration options | clauses/8.3.md | 506-509 |
| 8.3.7.10 | Mapped EPS bearer contexts | clauses/8.3.md | 510-513 |
| 8.3.7.11 | Port management information container | clauses/8.3.md | 514-517 |
| 8.3.7.12 | IP header compression configuration | clauses/8.3.md | 518-525 |
| 8.3.7.13 | Ethernet header compression configuration | clauses/8.3.md | 526-533 |
| 8.3.7.14 | Requested MBS container | clauses/8.3.md | 534-537 |
| 8.3.7.15 | Service-level-AA container | clauses/8.3.md | 538-541 |
| 8.3.7.16 | Non-3GPP delay budget | clauses/8.3.md | 542-545 |
| 8.3.7.17 | URSP rule enforcement reports | clauses/8.3.md | 546-549 |
| 8.3.8 | PDU session modification reject | clauses/8.3.md | 550-592 |
| 8.3.8.1 | Message definition | clauses/8.3.md | 552-576 |
| 8.3.8.2 | Back-off timer value | clauses/8.3.md | 577-580 |
| 8.3.8.2A | 5GSM congestion re-attempt indicator | clauses/8.3.md | 581-584 |
| 8.3.8.3 | Extended protocol configuration options | clauses/8.3.md | 585-588 |
| 8.3.8.4 | Re-attempt indicator | clauses/8.3.md | 589-592 |
| 8.3.9 | PDU session modification command | clauses/8.3.md | 593-716 |
| 8.3.9.1 | Message definition | clauses/8.3.md | 595-634 |
| 8.3.9.2 | 5GSM cause | clauses/8.3.md | 635-638 |
| 8.3.9.3 | Session-AMBR | clauses/8.3.md | 639-642 |
| 8.3.9.4 | RQ timer value | clauses/8.3.md | 643-646 |
| 8.3.9.5 | Always-on PDU session indication | clauses/8.3.md | 647-650 |
| 8.3.9.6 | Authorized QoS rules | clauses/8.3.md | 651-654 |
| 8.3.9.7 | Mapped EPS bearer contexts | clauses/8.3.md | 655-658 |
| 8.3.9.8 | Authorized QoS flow descriptions | clauses/8.3.md | 659-662 |
| 8.3.9.9 | Extended protocol configuration options | clauses/8.3.md | 663-666 |
| 8.3.9.10 | Void | clauses/8.3.md | 667-668 |
| 8.3.9.11 | ATSSS container | clauses/8.3.md | 669-672 |
| 8.3.9.12 | IP header compression configuration | clauses/8.3.md | 673-676 |
| 8.3.9.13 | Port management information container | clauses/8.3.md | 677-680 |
| 8.3.9.14 | Serving PLMN rate control | clauses/8.3.md | 681-684 |
| 8.3.9.15 | Ethernet header compression configuration | clauses/8.3.md | 685-688 |
| 8.3.9.16 | Received MBS container | clauses/8.3.md | 689-700 |
| 8.3.9.17 | Service-level-AA container | clauses/8.3.md | 701-704 |
| 8.3.9.18 | Alternative S-NSSAI | clauses/8.3.md | 705-708 |
| 8.3.9.19 | N3QAI | clauses/8.3.md | 709-712 |
| 8.3.9.20 | Protocol description | clauses/8.3.md | 713-716 |
| 8.3.10 | PDU session modification complete | clauses/8.3.md | 717-750 |
| 8.3.10.1 | Message definition | clauses/8.3.md | 719-742 |
| 8.3.10.2 | Extended protocol configuration options | clauses/8.3.md | 743-746 |
| 8.3.10.3 | Port management information container | clauses/8.3.md | 747-750 |
| 8.3.11 | PDU session modification command reject | clauses/8.3.md | 751-778 |
| 8.3.11.1 | Message definition | clauses/8.3.md | 753-774 |
| 8.3.11.2 | Extended protocol configuration options | clauses/8.3.md | 775-778 |
| 8.3.12 | PDU session release request | clauses/8.3.md | 779-810 |
| 8.3.12.1 | Message definition | clauses/8.3.md | 781-802 |
| 8.3.12.2 | 5GSM cause | clauses/8.3.md | 803-806 |
| 8.3.12.3 | Extended protocol configuration options | clauses/8.3.md | 807-810 |
| 8.3.13 | PDU session release reject | clauses/8.3.md | 811-838 |
| 8.3.13.1 | Message definition | clauses/8.3.md | 813-834 |
| 8.3.13.2 | Extended protocol configuration options | clauses/8.3.md | 835-838 |
| 8.3.14 | PDU session release command | clauses/8.3.md | 839-896 |
| 8.3.14.1 | Message definition | clauses/8.3.md | 841-868 |
| 8.3.14.2 | Back-off timer value | clauses/8.3.md | 869-872 |
| 8.3.14.3 | EAP message | clauses/8.3.md | 873-876 |
| 8.3.14.4 | Extended protocol configuration options | clauses/8.3.md | 877-880 |
| 8.3.14.5 | 5GSM congestion re-attempt indicator | clauses/8.3.md | 881-884 |
| 8.3.14.6 | Access type | clauses/8.3.md | 885-888 |
| 8.3.14.7 | Service-level-AA container | clauses/8.3.md | 889-892 |
| 8.3.14.8 | Alternative S-NSSAI | clauses/8.3.md | 893-896 |
| 8.3.15 | PDU session release complete | clauses/8.3.md | 897-928 |
| 8.3.15.1 | Message definition | clauses/8.3.md | 899-920 |
| 8.3.15.2 | 5GSM cause | clauses/8.3.md | 921-924 |
| 8.3.15.3 | Extended protocol configuration options | clauses/8.3.md | 925-928 |
| 8.3.16 | 5GSM status | clauses/8.3.md | 929-951 |
| 8.3.16.1 | Message definition | clauses/8.3.md | 931-951 |
| 8.3.17 | Service-level authentication command | clauses/8.3.md | 952-974 |
| 8.3.17.1 | Message definition | clauses/8.3.md | 954-974 |
| 8.3.18 | Service-level authentication complete | clauses/8.3.md | 975-997 |
| 8.3.18.1 | Message definition | clauses/8.3.md | 977-997 |
| 8.3.19 | Remote UE report | clauses/8.3.md | 998-1029 |
| 8.3.19.1 | Message definition | clauses/8.3.md | 1000-1021 |
| 8.3.19.2 | Remote UE context connected | clauses/8.3.md | 1022-1025 |
| 8.3.19.3 | Remote UE context disconnected | clauses/8.3.md | 1026-1029 |
| 8.3.20 | Remote UE report response | clauses/8.3.md | 1030-1057 |
| 8.3.20.1 | Message definition | clauses/8.3.md | 1032-1051 |
| 8.3.20.2 | Void | clauses/8.3.md | 1052-1053 |
| 8.3.20.3 | Void | clauses/8.3.md | 1054-1055 |
| 8.3.20.4 | Void | clauses/8.3.md | 1056-1057 |
| 9 | General message format and information elements coding | clauses/9.md | 1-1 |
| 9.1 | Overview | clauses/9.1.md | 1-83 |
| 9.1.1 | NAS message format | clauses/9.1.md | 3-67 |
| 9.1.2 | Field format and mapping | clauses/9.1.md | 68-83 |
| 9.2 | Extended protocol discriminator | clauses/9.2.md | 1-4 |
| 9.3 | Security header type | clauses/9.3.md | 1-24 |
| 9.4 | PDU session identity | clauses/9.4.md | 1-4 |
| 9.5 | Spare half octet | clauses/9.5.md | 1-4 |
| 9.6 | Procedure transaction identity | clauses/9.6.md | 1-4 |
| 9.7 | Message type | clauses/9.7.md | 1-91 |
| 9.8 | Message authentication code | clauses/9.8.md | 1-8 |
| 9.9 | Plain 5GS NAS message | clauses/9.9.md | 1-4 |
| 9.10 | Sequence number | clauses/9.10.md | 1-8 |
| 9.11 | Other information elements | clauses/9.11.md | 1-1 |
| 9.11.1 | General | clauses/9.11.1.md | 1-22 |
| 9.11.2 | Common information elements | clauses/9.11.2.md | 1-548 |
| 9.11.2.1 | Additional information | clauses/9.11.2.md | 3-27 |
| 9.11.2.1A | Access type | clauses/9.11.2.md | 28-55 |
| 9.11.2.1B | DNN | clauses/9.11.2.md | 56-74 |
| 9.11.2.2 | EAP message | clauses/9.11.2.md | 75-96 |
| 9.11.2.3 | GPRS timer | clauses/9.11.2.md | 97-100 |
| 9.11.2.4 | GPRS timer 2 | clauses/9.11.2.md | 101-104 |
| 9.11.2.5 | GPRS timer 3 | clauses/9.11.2.md | 105-108 |
| 9.11.2.6 | Intra N1 mode NAS transparent container | clauses/9.11.2.md | 109-150 |
| 9.11.2.7 | N1 mode to S1 mode NAS transparent container | clauses/9.11.2.md | 151-176 |
| 9.11.2.8 | S-NSSAI | clauses/9.11.2.md | 177-219 |
| 9.11.2.9 | S1 mode to N1 mode NAS transparent container | clauses/9.11.2.md | 220-259 |
| 9.11.2.10 | Service-level-AA container | clauses/9.11.2.md | 260-339 |
| 9.11.2.11 | Service-level device ID | clauses/9.11.2.md | 340-361 |
| 9.11.2.12 | Service-level-AA server address | clauses/9.11.2.md | 362-394 |
| 9.11.2.13 | Service-level-AA payload | clauses/9.11.2.md | 395-417 |
| 9.11.2.14 | Service-level-AA response | clauses/9.11.2.md | 418-455 |
| 9.11.2.15 | Service-level-AA payload type | clauses/9.11.2.md | 456-482 |
| 9.11.2.16 | Void | clauses/9.11.2.md | 483-484 |
| 9.11.2.17 | Service-level-AA pending indication | clauses/9.11.2.md | 485-508 |
| 9.11.2.18 | Service-level-AA service status indication | clauses/9.11.2.md | 509-536 |
| 9.11.2.19 | Time duration | clauses/9.11.2.md | 537-540 |
| 9.11.2.20 | Unavailability information | clauses/9.11.2.md | 541-544 |
| 9.11.2.21 | Unavailability configuration | clauses/9.11.2.md | 545-548 |
| 9.11.3 | 5GS mobility management (5GMM) information elements | clauses/9.11.3.md | 1-1 |
| 9.11.3.1 | 5GMM capability | clauses/9.11.3.1.md | 1-380 |
| 9.11.3.2 | 5GMM cause | clauses/9.11.3.2.md | 1-77 |
| 9.11.3.2A | 5GS DRX parameters | clauses/9.11.3.2A.md | 1-34 |
| 9.11.3.3 | 5GS identity type | clauses/9.11.3.3.md | 1-32 |
| 9.11.3.4 | 5GS mobile identity | clauses/9.11.3.4.md | 1-194 |
| 9.11.3.5 | 5GS network feature support | clauses/9.11.3.5.md | 1-311 |
| 9.11.3.6 | 5GS registration result | clauses/9.11.3.6.md | 1-58 |
| 9.11.3.7 | 5GS registration type | clauses/9.11.3.7.md | 1-38 |
| 9.11.3.8 | 5GS tracking area identity | clauses/9.11.3.8.md | 1-27 |
| 9.11.3.9 | 5GS tracking area identity list | clauses/9.11.3.9.md | 1-151 |
| 9.11.3.9A | 5GS update type | clauses/9.11.3.9A.md | 1-62 |
| 9.11.3.10 | ABBA | clauses/9.11.3.10.md | 1-24 |
| 9.11.3.11 | Void | clauses/9.11.3.11.md | 1-2 |
| 9.11.3.12 | Additional 5G security information | clauses/9.11.3.12.md | 1-31 |
| 9.11.3.12A | Additional information requested | clauses/9.11.3.12A.md | 1-30 |
| 9.11.3.13 | Allowed PDU session status | clauses/9.11.3.13.md | 1-28 |
| 9.11.3.14 | Authentication failure parameter | clauses/9.11.3.14.md | 1-4 |
| 9.11.3.15 | Authentication parameter AUTN | clauses/9.11.3.15.md | 1-4 |
| 9.11.3.16 | Authentication parameter RAND | clauses/9.11.3.16.md | 1-4 |
| 9.11.3.17 | Authentication response parameter | clauses/9.11.3.17.md | 1-4 |
| 9.11.3.18 | Configuration update indication | clauses/9.11.3.18.md | 1-32 |
| 9.11.3.18A | CAG information list | clauses/9.11.3.18A.md | 1-49 |
| 9.11.3.18B | CIoT small data container | clauses/9.11.3.18B.md | 1-79 |
| 9.11.3.18C | Ciphering key data | clauses/9.11.3.18C.md | 1-384 |
| 9.11.3.18D | Control plane service type | clauses/9.11.3.18D.md | 1-32 |
| 9.11.3.19 | Daylight saving time | clauses/9.11.3.19.md | 1-4 |
| 9.11.3.20 | De-registration type | clauses/9.11.3.20.md | 1-47 |
| 9.11.3.21 | Void | clauses/9.11.3.21.md | 1-2 |
| 9.11.3.22 | Void | clauses/9.11.3.22.md | 1-2 |
| 9.11.3.23 | Emergency number list | clauses/9.11.3.23.md | 1-4 |
| 9.11.3.23A | EPS bearer context status | clauses/9.11.3.23A.md | 1-4 |
| 9.11.3.24 | EPS NAS message container | clauses/9.11.3.24.md | 1-24 |
| 9.11.3.25 | EPS NAS security algorithms | clauses/9.11.3.25.md | 1-4 |
| 9.11.3.26 | Extended emergency number list | clauses/9.11.3.26.md | 1-4 |
| 9.11.3.26A | Extended DRX parameters | clauses/9.11.3.26A.md | 1-4 |
| 9.11.3.27 | Void | clauses/9.11.3.27.md | 1-2 |
| 9.11.3.28 | IMEISV request | clauses/9.11.3.28.md | 1-4 |
| 9.11.3.29 | LADN indication | clauses/9.11.3.29.md | 1-28 |
| 9.11.3.30 | LADN information | clauses/9.11.3.30.md | 1-39 |
| 9.11.3.31 | MICO indication | clauses/9.11.3.31.md | 1-34 |
| 9.11.3.31A | MA PDU session information | clauses/9.11.3.31A.md | 1-26 |
| 9.11.3.31B | Mapped NSSAI | clauses/9.11.3.31B.md | 1-37 |
| 9.11.3.31C | Mobile station classmark 2 | clauses/9.11.3.31C.md | 1-4 |
| 9.11.3.32 | NAS key set identifier | clauses/9.11.3.32.md | 1-39 |
| 9.11.3.33 | NAS message container | clauses/9.11.3.33.md | 1-28 |
| 9.11.3.34 | NAS security algorithms | clauses/9.11.3.34.md | 1-48 |
| 9.11.3.35 | Network name | clauses/9.11.3.35.md | 1-4 |
| 9.11.3.36 | Network slicing indication | clauses/9.11.3.36.md | 1-31 |
| 9.11.3.36A | Non-3GPP NW provided policies | clauses/9.11.3.36A.md | 1-4 |
| 9.11.3.37 | NSSAI | clauses/9.11.3.37.md | 1-29 |
| 9.11.3.37A | NSSAI inclusion mode | clauses/9.11.3.37A.md | 1-28 |
| 9.11.3.38 | Operator-defined access category definitions | clauses/9.11.3.38.md | 1-81 |
| 9.11.3.39 | Payload container | clauses/9.11.3.39.md | 1-102 |
| 9.11.3.40 | Payload container type | clauses/9.11.3.40.md | 1-39 |
| 9.11.3.41 | PDU session identity 2 | clauses/9.11.3.41.md | 1-21 |
| 9.11.3.42 | PDU session reactivation result | clauses/9.11.3.42.md | 1-30 |
| 9.11.3.43 | PDU session reactivation result error cause | clauses/9.11.3.43.md | 1-30 |
| 9.11.3.44 | PDU session status | clauses/9.11.3.44.md | 1-26 |
| 9.11.3.45 | PLMN list | clauses/9.11.3.45.md | 1-4 |
| 9.11.3.46 | Rejected NSSAI | clauses/9.11.3.46.md | 1-50 |
| 9.11.3.46A | Release assistance indication | clauses/9.11.3.46A.md | 1-4 |
| 9.11.3.47 | Request type | clauses/9.11.3.47.md | 1-32 |
| 9.11.3.48 | S1 UE network capability | clauses/9.11.3.48.md | 1-4 |
| 9.11.3.48A | S1 UE security capability | clauses/9.11.3.48A.md | 1-4 |
| 9.11.3.49 | Service area list | clauses/9.11.3.49.md | 1-141 |
| 9.11.3.50 | Service type | clauses/9.11.3.50.md | 1-39 |
| 9.11.3.50A | SMS indication | clauses/9.11.3.50A.md | 1-27 |
| 9.11.3.51 | SOR transparent container | clauses/9.11.3.51.md | 1-512 |
| 9.11.3.51A | Supported codec list | clauses/9.11.3.51A.md | 1-4 |
| 9.11.3.52 | Time zone | clauses/9.11.3.52.md | 1-4 |
| 9.11.3.53 | Time zone and time | clauses/9.11.3.53.md | 1-4 |
| 9.11.3.53A | UE parameters update transparent container | clauses/9.11.3.53A.md | 1-152 |
| 9.11.3.54 | UE security capability | clauses/9.11.3.54.md | 1-137 |
| 9.11.3.55 | UE's usage setting | clauses/9.11.3.55.md | 1-27 |
| 9.11.3.56 | UE status | clauses/9.11.3.56.md | 1-31 |
| 9.11.3.57 | Uplink data status | clauses/9.11.3.57.md | 1-26 |
| 9.11.3.58 | Void | clauses/9.11.3.58.md | 1-2 |
| 9.11.3.59 | Void | clauses/9.11.3.59.md | 1-2 |
| 9.11.3.60 | Void | clauses/9.11.3.60.md | 1-2 |
| 9.11.3.61 | Void | clauses/9.11.3.61.md | 1-2 |
| 9.11.3.62 | Void | clauses/9.11.3.62.md | 1-2 |
| 9.11.3.63 | Void | clauses/9.11.3.63.md | 1-2 |
| 9.11.3.64 | Void | clauses/9.11.3.64.md | 1-2 |
| 9.11.3.65 | Void | clauses/9.11.3.65.md | 1-2 |
| 9.11.3.66 | Void | clauses/9.11.3.66.md | 1-2 |
| 9.11.3.67 | Void | clauses/9.11.3.67.md | 1-2 |
| 9.11.3.68 | UE radio capability ID | clauses/9.11.3.68.md | 1-26 |
| 9.11.3.69 | UE radio capability ID deletion indication | clauses/9.11.3.69.md | 1-27 |
| 9.11.3.70 | Truncated 5G-S-TMSI configuration | clauses/9.11.3.70.md | 1-49 |
| 9.11.3.71 | WUS assistance information | clauses/9.11.3.71.md | 1-4 |
| 9.11.3.72 | N5GC indication | clauses/9.11.3.72.md | 1-26 |
| 9.11.3.73 | NB-N1 mode DRX parameters | clauses/9.11.3.73.md | 1-36 |
| 9.11.3.74 | Additional configuration indication | clauses/9.11.3.74.md | 1-26 |
| 9.11.3.75 | Extended rejected NSSAI | clauses/9.11.3.75.md | 1-96 |
| 9.11.3.76 | UE request type | clauses/9.11.3.76.md | 1-4 |
| 9.11.3.77 | Paging restriction | clauses/9.11.3.77.md | 1-45 |
| 9.11.3.78 | Void | clauses/9.11.3.78.md | 1-2 |
| 9.11.3.79 | NID | clauses/9.11.3.79.md | 1-4 |
| 9.11.3.80 | PEIPS assistance information | clauses/9.11.3.80.md | 1-86 |
| 9.11.3.81 | 5GS additional request result | clauses/9.11.3.81.md | 1-31 |
| 9.11.3.82 | NSSRG information | clauses/9.11.3.82.md | 1-41 |
| 9.11.3.83 | List of PLMNs to be used in disaster condition | clauses/9.11.3.83.md | 1-38 |
| 9.11.3.84 | Registration wait range | clauses/9.11.3.84.md | 1-25 |
| 9.11.3.85 | PLMN identity | clauses/9.11.3.85.md | 1-30 |
| 9.11.3.86 | Extended CAG information list | clauses/9.11.3.86.md | 1-124 |
| 9.11.3.87 | NSAG information | clauses/9.11.3.87.md | 1-56 |
| 9.11.3.88 | ProSe relay transaction identity | clauses/9.11.3.88.md | 1-30 |
| 9.11.3.89 | Relay key request parameters | clauses/9.11.3.89.md | 1-33 |
| 9.11.3.90 | Relay key response parameters | clauses/9.11.3.90.md | 1-25 |
| 9.11.3.91 | Priority indicator | clauses/9.11.3.91.md | 1-28 |
| 9.11.3.92 | SNPN list | clauses/9.11.3.92.md | 1-53 |
| 9.11.3.93 | N3IWF identifier | clauses/9.11.3.93.md | 1-54 |
| 9.11.3.94 | TNAN information | clauses/9.11.3.94.md | 1-49 |
| 9.11.3.95 | RAN timing synchronization | clauses/9.11.3.95.md | 1-30 |
| 9.11.3.96 | Extended LADN information | clauses/9.11.3.96.md | 1-41 |
| 9.11.3.97 | Alternative NSSAI | clauses/9.11.3.97.md | 1-37 |
| 9.11.3.98 | Type 6 IE container | clauses/9.11.3.98.md | 1-42 |
| 9.11.3.99 | Non-3GPP access path switching indication | clauses/9.11.3.99.md | 1-32 |
| 9.11.3.100 | S-NSSAI location validity information | clauses/9.11.3.100.md | 1-70 |
| 9.11.3.101 | S-NSSAI time validity information | clauses/9.11.3.101.md | 1-79 |
| 9.11.3.102 | Non-3GPP path switching information | clauses/9.11.3.102.md | 1-29 |
| 9.11.3.103 | Partial NSSAI | clauses/9.11.3.103.md | 1-32 |
| 9.11.3.104 | AUN3 indication | clauses/9.11.3.104.md | 1-29 |
| 9.11.3.105 | Feature authorization indication | clauses/9.11.3.105.md | 1-34 |
| 9.11.3.106 | Payload container information | clauses/9.11.3.106.md | 1-28 |
| 9.11.3.107 | AUN3 device security key | clauses/9.11.3.107.md | 1-32 |
| 9.11.3.108 | On-demand NSSAI | clauses/9.11.3.108.md | 1-34 |
| 9.11.3.109 | Extended 5GMM cause | clauses/9.11.3.109.md | 1-32 |
| 9.11.4 | 5GS session management (5GSM) information elements | clauses/9.11.4.md | 1-1 |
| 9.11.4.1 | 5GSM capability | clauses/9.11.4.1.md | 1-172 |
| 9.11.4.2 | 5GSM cause | clauses/9.11.4.2.md | 1-71 |
| 9.11.4.3 | Always-on PDU session indication | clauses/9.11.4.3.md | 1-27 |
| 9.11.4.4 | Always-on PDU session requested | clauses/9.11.4.4.md | 1-27 |
| 9.11.4.5 | Allowed SSC mode | clauses/9.11.4.5.md | 1-38 |
| 9.11.4.6 | Extended protocol configuration options | clauses/9.11.4.6.md | 1-4 |
| 9.11.4.7 | Integrity protection maximum data rate | clauses/9.11.4.7.md | 1-40 |
| 9.11.4.8 | Mapped EPS bearer contexts | clauses/9.11.4.8.md | 1-54 |
| 9.11.4.9 | Maximum number of supported packet filters | clauses/9.11.4.9.md | 1-24 |
| 9.11.4.10 | PDU address | clauses/9.11.4.10.md | 1-62 |
| 9.11.4.11 | PDU session type | clauses/9.11.4.11.md | 1-30 |
| 9.11.4.12 | QoS flow descriptions | clauses/9.11.4.12.md | 1-58 |
| 9.11.4.13 | QoS rules | clauses/9.11.4.13.md | 1-81 |
| 9.11.4.14 | Session-AMBR | clauses/9.11.4.14.md | 1-27 |
| 9.11.4.15 | SM PDU DN request container | clauses/9.11.4.15.md | 1-23 |
| 9.11.4.16 | SSC mode | clauses/9.11.4.16.md | 1-30 |
| 9.11.4.17 | Re-attempt indicator | clauses/9.11.4.17.md | 1-34 |
| 9.11.4.18 | 5GSM network feature support | clauses/9.11.4.18.md | 1-40 |
| 9.11.4.19 | Void | clauses/9.11.4.19.md | 1-2 |
| 9.11.4.20 | Serving PLMN rate control | clauses/9.11.4.20.md | 1-4 |
| 9.11.4.21 | 5GSM congestion re-attempt indicator | clauses/9.11.4.21.md | 1-31 |
| 9.11.4.22 | ATSSS container | clauses/9.11.4.22.md | 1-22 |
| 9.11.4.23 | Control plane only indication | clauses/9.11.4.23.md | 1-28 |
| 9.11.4.24 | IP header compression configuration | clauses/9.11.4.24.md | 1-31 |
| 9.11.4.25 | DS-TT Ethernet port MAC address | clauses/9.11.4.25.md | 1-25 |
| 9.11.4.26 | UE-DS-TT residence time | clauses/9.11.4.26.md | 1-25 |
| 9.11.4.27 | Port management information container | clauses/9.11.4.27.md | 1-24 |
| 9.11.4.28 | Ethernet header compression configuration | clauses/9.11.4.28.md | 1-29 |
| 9.11.4.29 | Remote UE context list | clauses/9.11.4.29.md | 1-90 |
| 9.11.4.30 | Requested MBS container | clauses/9.11.4.30.md | 1-79 |
| 9.11.4.31 | Received MBS container | clauses/9.11.4.31.md | 1-218 |
| 9.11.4.32 | PDU session pair ID | clauses/9.11.4.32.md | 1-30 |
| 9.11.4.33 | RSN | clauses/9.11.4.33.md | 1-29 |
| 9.11.4.34 | ECS address | clauses/9.11.4.34.md | 1-156 |
| 9.11.4.35 | Void | clauses/9.11.4.35.md | 1-2 |
| 9.11.4.36 | N3QAI | clauses/9.11.4.36.md | 1-58 |
| 9.11.4.37 | Non-3GPP delay budget | clauses/9.11.4.37.md | 1-46 |
| 9.11.4.38 | URSP rule enforcement reports | clauses/9.11.4.38.md | 1-42 |
| 9.11.4.39 | Protocol description | clauses/9.11.4.39.md | 1-104 |
| 9.12 | 3GPP specific coding information defined within present document | clauses/9.12.md | 1-62 |
| 9.12.1 | Serving network name (SNN) | clauses/9.12.md | 3-62 |
| 10 | List of system parameters | clauses/10.md | 1-1 |
| 10.1 | General | clauses/10.1.md | 1-4 |
| 10.2 | Timers of 5GS mobility management | clauses/10.2.md | 1-50 |
| 10.3 | Timers of 5GS session management | clauses/10.3.md | 1-38 |
| 10.4 | Void | clauses/10.4.md | 1-4 |
| A.1 | Causes related to UE identification | clauses/annex-A.1.md | 1-18 |
| A.2 | Cause related to subscription options | clauses/annex-A.2.md | 1-82 |
| A.3 | Causes related to PLMN or SNPN specific network failures and congestion/authentication failures | clauses/annex-A.3.md | 1-90 |
| A.4 | Causes related to invalid messages | clauses/annex-A.4.md | 1-36 |
| B.1 | Causes related to nature of request | clauses/annex-B.1.md | 1-150 |
| B.2 | Protocol errors (e.g. unknown message) | clauses/annex-B.2.md | 1-36 |
| C.1 | Storage of 5GMM information for UEs not operating in SNPN access operation mode | clauses/annex-C.1.md | 1-108 |
| C.2 | Storage of 5GMM information for UEs operating in SNPN access operation mode | clauses/annex-C.2.md | 1-120 |
| D.1 | General | clauses/annex-D.1.md | 1-56 |
| D.1.1 | Overview | clauses/annex-D.1.md | 3-32 |
| D.1.2 | Principles of PTI handling for UE policy delivery service procedures | clauses/annex-D.1.md | 33-56 |
| D.2 | Procedures | clauses/annex-D.2.md | 1-242 |
| D.2.1 | Network-requested UE policy management procedure | clauses/annex-D.2.md | 3-172 |
| D.2.1.1 | General | clauses/annex-D.2.md | 5-16 |
| D.2.1.2 | Network-requested UE policy management procedure initiation | clauses/annex-D.2.md | 17-88 |
| D.2.1.3 | Network-requested UE policy management procedure accepted by the UE | clauses/annex-D.2.md | 89-100 |
| D.2.1.4 | Network-requested UE policy management procedure not accepted by the UE | clauses/annex-D.2.md | 101-124 |
| D.2.1.5 | Abnormal cases on the network side | clauses/annex-D.2.md | 125-132 |
| D.2.1.6 | Abnormal cases in the UE | clauses/annex-D.2.md | 133-172 |
| D.2.2 | UE-initiated UE state indication procedure | clauses/annex-D.2.md | 173-242 |
| D.2.2.1 | General | clauses/annex-D.2.md | 175-196 |
| D.2.2.2 | UE-initiated UE state indication procedure initiation | clauses/annex-D.2.md | 197-234 |
| D.2.2.3 | UE-initiated UE state indication procedure accepted by the network | clauses/annex-D.2.md | 235-238 |
| D.2.2.4 | Abnormal cases on the network side | clauses/annex-D.2.md | 239-242 |
| D.3 | UE policy re-assembly at the UE | clauses/annex-D.3.md | 1-48 |
| D.4 | Void | clauses/annex-D.4.md | 1-2 |
| D.5 | Message functional definition and contents | clauses/annex-D.5.md | 1-114 |
| D.5.1 | Manage UE policy command | clauses/annex-D.5.md | 3-34 |
| D.5.1.1 | Message definition | clauses/annex-D.5.md | 5-26 |
| D.5.1.2 | UE policy network classmark | clauses/annex-D.5.md | 27-30 |
| D.5.1.3 | VPS URSP configuration | clauses/annex-D.5.md | 31-34 |
| D.5.2 | Manage UE policy complete | clauses/annex-D.5.md | 35-54 |
| D.5.2.1 | Message definition | clauses/annex-D.5.md | 37-54 |
| D.5.3 | Manage UE policy command reject | clauses/annex-D.5.md | 55-76 |
| D.5.3.1 | Message definition | clauses/annex-D.5.md | 57-76 |
| D.5.4 | UE state indication | clauses/annex-D.5.md | 77-114 |
| D.5.4.1 | Message definition | clauses/annex-D.5.md | 79-114 |
| D.6 | Information elements coding | clauses/annex-D.6.md | 1-563 |
| D.6.1 | UE policy delivery service message type | clauses/annex-D.6.md | 3-21 |
| D.6.2 | UE policy section management list | clauses/annex-D.6.md | 22-170 |
| D.6.3 | UE policy section management result | clauses/annex-D.6.md | 171-274 |
| D.6.4 | UPSI list | clauses/annex-D.6.md | 275-324 |
| D.6.5 | UE policy classmark | clauses/annex-D.6.md | 325-369 |
| D.6.6 | UE OS Id | clauses/annex-D.6.md | 370-393 |
| D.6.7 | UE policy network classmark | clauses/annex-D.6.md | 394-424 |
| D.6.8 | VPS URSP configuration | clauses/annex-D.6.md | 425-563 |
| D.7 | Timers of UE policy delivery service | clauses/annex-D.7.md | 1-12 |
| D.8 | Handling of unknown, unforeseen, and erroneous UPDS data | clauses/annex-D.8.md | 1-1 |
| D.8.1 | General | clauses/annex-D.8.1.md | 1-14 |
| D.8.2 | Message too short or too long | clauses/annex-D.8.2.md | 1-10 |
| D.8.2.1 | Message too short | clauses/annex-D.8.2.md | 3-6 |
| D.8.2.2 | Message too long | clauses/annex-D.8.2.md | 7-10 |
| D.8.3 | Unknown or unforeseen procedure transaction identity | clauses/annex-D.8.3.md | 1-14 |
| D.8.3.1 | Procedure transaction identity | clauses/annex-D.8.3.md | 3-14 |
| D.8.4 | Unknown or unforeseen message type | clauses/annex-D.8.4.md | 1-10 |
| D.8.5 | Non-semantical mandatory information element errors | clauses/annex-D.8.5.md | 1-28 |
| D.8.5.1 | Common procedures | clauses/annex-D.8.5.md | 3-28 |
| D.8.6 | Unknown and unforeseen IEs in the non-imperative message part | clauses/annex-D.8.6.md | 1-20 |
| D.8.6.1 | IEIs unknown in the message | clauses/annex-D.8.6.md | 3-8 |
| D.8.6.2 | Out of sequence IEs | clauses/annex-D.8.6.md | 9-14 |
| D.8.6.3 | Repeated IEs | clauses/annex-D.8.6.md | 15-20 |
| D.8.7 | Non-imperative message part errors | clauses/annex-D.8.7.md | 1-24 |
| D.8.7.1 | Syntactically incorrect optional IEs | clauses/annex-D.8.7.md | 9-14 |
| D.8.7.2 | Conditional IE errors | clauses/annex-D.8.7.md | 15-24 |
| D.8.8 | Messages with semantically incorrect contents | clauses/annex-D.8.8.md | 1-3932 |
