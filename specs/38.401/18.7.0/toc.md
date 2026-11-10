# TS 38.401 V18.7.0 — NG-RAN architecture

Clause index. `File` is relative to this directory; `Lines` is the 1-based
line range of the clause inside that file.

| Clause | Title | File | Lines |
|---|---|---|---|
| front-matter | Title page, foreword and scope front matter | clauses/front-matter.md | 1-502 |
| 1 | Scope | clauses/1.md | 1-4 |
| 2 | References | clauses/2.md | 1-82 |
| 3 | Definitions and abbreviations | clauses/3.md | 1-282 |
| 3.1 | Definitions | clauses/3.md | 3-103 |
| 3.2 | Abbreviations | clauses/3.md | 104-282 |
| 4 | General principles | clauses/4.md | 1-18 |
| 5 | General architecture | clauses/5.md | 1-42 |
| 5.1 | General | clauses/5.md | 3-14 |
| 5.2 | User plane | clauses/5.md | 15-26 |
| 5.3 | Control plane | clauses/5.md | 27-42 |
| 6 | NG-RAN architecture | clauses/6.md | 1-368 |
| 6.1 | Overview | clauses/6.md | 3-146 |
| 6.1.1 | Overall Architecture of NG-RAN | clauses/6.md | 5-44 |
| 6.1.2 | Overall architecture for separation of gNB-CU-CP and gNB-CU-UP | clauses/6.md | 45-78 |
| 6.1.3 | Overall Architecture of IAB | clauses/6.md | 79-96 |
| 6.1.4 | Protocol stacks of IAB | clauses/6.md | 97-122 |
| 6.1.5 | Overall Architecture of NR MBS | clauses/6.md | 123-134 |
| 6.1.6 | Protocol stacks of L2 UE-to-Network Relay | clauses/6.md | 135-146 |
| 6.2 | NG-RAN identifiers | clauses/6.md | 147-250 |
| 6.2.1 | Principle of handling Application Protocol Identities | clauses/6.md | 149-230 |
| 6.2.2 | gNB-DU ID | clauses/6.md | 231-234 |
| 6.2.3 | ng-eNB-DU ID | clauses/6.md | 235-238 |
| 6.2.4 | gNB-CU-UP ID | clauses/6.md | 239-246 |
| 6.2.5 | RAN UE ID | clauses/6.md | 247-250 |
| 6.3 | Transport addresses | clauses/6.md | 251-258 |
| 6.4 | UE associations in NG-RAN Node | clauses/6.md | 259-304 |
| 6.5 | MBS Session associations in NG-RAN Node | clauses/6.md | 305-368 |
| 7 | NG-RAN functions description | clauses/7.md | 1-154 |
| 7.0 | General | clauses/7.md | 3-6 |
| 7.1 | NG-RAN sharing | clauses/7.md | 7-10 |
| 7.2 | Remote Interference Management | clauses/7.md | 11-20 |
| 7.3 | Cross-Link Interference Management | clauses/7.md | 21-26 |
| 7.4 | Support for Non-Public Networks | clauses/7.md | 27-30 |
| 7.5 | RACH Optimisation Function | clauses/7.md | 31-40 |
| 7.6 | Positioning | clauses/7.md | 41-44 |
| 7.7 | Support for NR MBS | clauses/7.md | 45-110 |
| 7.7.1 | Support of dynamic PTP and PTM switching | clauses/7.md | 49-56 |
| 7.7.2 | Support of resource efficiency for RAN Sharing | clauses/7.md | 57-88 |
| 7.7.2.1 | General | clauses/7.md | 59-66 |
| 7.7.2.2 | Support of resource efficiency for MOCN | clauses/7.md | 67-70 |
| 7.7.2.3 | Support of resource efficiency for RAN Sharing with multiple cell-ID broadcast | clauses/7.md | 71-88 |
| 7.7.3 | Support of Multicast reception for UEs in RRCINACTIVE | clauses/7.md | 89-100 |
| 7.7.4 | Recovery of shared F1-U Failure | clauses/7.md | 101-110 |
| 7.8 | PCI Optimisation Function | clauses/7.md | 111-122 |
| 7.9 | Support for CCO | clauses/7.md | 123-136 |
| 7.9.1 | General | clauses/7.md | 125-128 |
| 7.9.2 | OAM requirements | clauses/7.md | 129-132 |
| 7.9.3 | Dynamic coverage configuration changes | clauses/7.md | 133-136 |
| 7.10 | Support of RAN visible QoE measurement | clauses/7.md | 137-144 |
| 7.11 | Support of AI/ML for NG-RAN | clauses/7.md | 145-154 |
| 8 | Overall procedures in gNB-CU/gNB-DU Architecture | clauses/8.md | 1-1 |
| 8.1 | UE Initial Access | clauses/8.1.md | 1-44 |
| 8.2 | Intra-gNB-CU Mobility | clauses/8.2.md | 1-514 |
| 8.2.1 | Intra-NR Mobility | clauses/8.2.md | 3-246 |
| 8.2.1.1 | Inter-gNB-DU Mobility | clauses/8.2.md | 5-44 |
| 8.2.1.2 | Intra-gNB-DU handover | clauses/8.2.md | 45-48 |
| 8.2.1.3 | Inter-gNB-DU Conditional Handover or Conditional PSCell Change or subsequent CPAC | clauses/8.2.md | 49-86 |
| 8.2.1.4 | Intra-gNB-DU LTM | clauses/8.2.md | 87-140 |
| 8.2.1.5 | Inter-gNB-DU LTM | clauses/8.2.md | 141-204 |
| 8.2.1.6 | LTM with gNB-CU-UP change | clauses/8.2.md | 205-246 |
| 8.2.2 | EN-DC Mobility | clauses/8.2.md | 247-328 |
| 8.2.2.1 | Inter-gNB-DU Mobility using MCG SRB | clauses/8.2.md | 249-288 |
| 8.2.2.2 | Inter-gNB-DU Mobility using SCG SRB (SRB3) | clauses/8.2.md | 289-292 |
| 8.2.2.3 | Inter-gNB-DU Conditional PSCell Change using MCG SRB without MN negotiation | clauses/8.2.md | 293-328 |
| 8.2.3 | Intra-CU topology adaptation procedure | clauses/8.2.md | 329-434 |
| 8.2.3.1 | Intra-CU topology adaptation procedure in SA | clauses/8.2.md | 331-394 |
| 8.2.3.2 | Intra-CU topology adaptation procedure in NSA using MCG SRB | clauses/8.2.md | 395-430 |
| 8.2.3.3 | Intra-CU topology adaptation procedure in NSA using SCG SRB (SRB3) | clauses/8.2.md | 431-434 |
| 8.2.4 | Intra-CU topological redundancy procedure | clauses/8.2.md | 435-494 |
| 8.2.5 | Intra-CU Backhaul RLF recovery for IAB-nodes in SA mode | clauses/8.2.md | 495-514 |
| 8.3 | Mechanism of centralized retransmission of lost PDUs | clauses/8.3.md | 1-26 |
| 8.3.1 | Centralized Retransmission in Intra gNB-CU Cases | clauses/8.3.md | 3-26 |
| 8.4 | Multi-Connectivity operation | clauses/8.4.md | 1-174 |
| 8.4.1 | Secondary Node Addition | clauses/8.4.md | 3-20 |
| 8.4.1.1 | EN-DC | clauses/8.4.md | 5-20 |
| 8.4.2 | Secondary Node Release (MN/SN initiated) | clauses/8.4.md | 21-60 |
| 8.4.2.1 | EN-DC | clauses/8.4.md | 23-60 |
| 8.4.3 | SCG suspend/resume in RRCINACTIVE | clauses/8.4.md | 61-80 |
| 8.4.4 | SCG Deactivation and Activation | clauses/8.4.md | 81-174 |
| 8.4.4.1 | SN Addition with SCG Activation or Deactivation | clauses/8.4.md | 85-110 |
| 8.4.4.2 | MN initiated SN Modification with SCG Activation or Deactivation | clauses/8.4.md | 111-140 |
| 8.4.4.3 | SN initiated SN Modification with SCG Activation or Deactivation | clauses/8.4.md | 141-174 |
| 8.5 | F1 Startup and cells activation | clauses/8.5.md | 1-42 |
| 8.6 | RRC state transition | clauses/8.6.md | 1-57 |
| 8.6.1 | RRC connected to RRC inactive | clauses/8.6.md | 3-18 |
| 8.6.2 | RRC inactive to other states | clauses/8.6.md | 19-57 |
| 8.7 | RRC connection reestablishment | clauses/8.7.md | 1-34 |
| 8.8 | Multiple TNLAs for F1-C | clauses/8.8.md | 1-20 |
| 8.9 | Overall procedures involving E1 and F1 | clauses/8.9.md | 1-446 |
| 8.9.1 | UE Initial Access | clauses/8.9.md | 7-30 |
| 8.9.2 | Bearer context setup over F1-U | clauses/8.9.md | 31-56 |
| 8.9.3 | Bearer context release over F1-U | clauses/8.9.md | 57-102 |
| 8.9.3.1 | gNB-CU-CP initiated bearer context release | clauses/8.9.md | 59-82 |
| 8.9.3.2 | gNB-CU-UP initiated bearer context release | clauses/8.9.md | 83-102 |
| 8.9.4 | Inter-gNB handover involving gNB-CU-UP change | clauses/8.9.md | 103-158 |
| 8.9.5 | Change of gNB-CU-UP | clauses/8.9.md | 159-182 |
| 8.9.6 | RRC State transition | clauses/8.9.md | 183-246 |
| 8.9.6.1 | RRC Connected to RRC Inactive | clauses/8.9.md | 185-212 |
| 8.9.6.2 | RRC Inactive to other states | clauses/8.9.md | 213-246 |
| 8.9.7 | Trace activation/deactivation over F1 and E1 | clauses/8.9.md | 247-266 |
| 8.9.8 | BH RLC channel establishment procedure | clauses/8.9.md | 267-304 |
| 8.9.9 | Traffic Mapping | clauses/8.9.md | 305-330 |
| 8.9.9.1 | Traffic Mapping from IP-layer to Layer-2 | clauses/8.9.md | 309-322 |
| 8.9.9.2 | BH RLC Channel Mapping on BAP Layer | clauses/8.9.md | 323-330 |
| 8.9.10 | IAB-node release | clauses/8.9.md | 331-344 |
| 8.9.10.1 | IAB-node orderly release | clauses/8.9.md | 337-340 |
| 8.9.10.2 | IAB-node disorderly release | clauses/8.9.md | 341-344 |
| 8.9.11 | IAB-node OAM | clauses/8.9.md | 345-362 |
| 8.9.12 | Handling of IAB-MTs in INACTIVE State | clauses/8.9.md | 363-368 |
| 8.9.13 | IP Address Allocation for IAB-nodes | clauses/8.9.md | 369-388 |
| 8.9.14 | Mobile IAB-node authorization | clauses/8.9.md | 389-404 |
| 8.9.15 | IAB-donor-CU-based NR Cell Identity (NCI) (re-)configuration for mobile IAB cells | clauses/8.9.md | 405-412 |
| 8.9.16 | TAC/RANAC (re-)configuration for mobile IAB | clauses/8.9.md | 413-416 |
| 8.9.17 | IAB-node authorization | clauses/8.9.md | 417-446 |
| 8.9.17.1 | IAB-node in NSA | clauses/8.9.md | 419-426 |
| 8.9.17.2 | IAB-node with single IAB-donor in SA | clauses/8.9.md | 427-440 |
| 8.9.17.2.1 | IAB-node is single-connected | clauses/8.9.md | 429-434 |
| 8.9.17.2.2 | IAB-node is NR dual-connected | clauses/8.9.md | 435-440 |
| 8.9.17.3 | IAB-node is served by two IAB-donors in SA | clauses/8.9.md | 441-446 |
| 8.10 | Multiple TNLAs for E1 | clauses/8.10.md | 1-22 |
| 8.11 | Support of Network Sharing with multiple cell-ID broadcast | clauses/8.11.md | 1-70 |
| 8.11.1 | General | clauses/8.11.md | 3-8 |
| 8.11.2 | Initial Registration – separate PLMN signalling | clauses/8.11.md | 9-36 |
| 8.11.3 | RRC Connection Reestablishment – separate PLMN signalling | clauses/8.11.md | 37-62 |
| 8.11.4 | Support of shared signalling transport | clauses/8.11.md | 63-70 |
| 8.12 | IAB-node Integration Procedure | clauses/8.12.md | 1-66 |
| 8.12.1 | Standalone IAB integration | clauses/8.12.md | 3-28 |
| 8.12.2 | NSA IAB Integration procedure | clauses/8.12.md | 29-50 |
| 8.12.3 | Mobile IAB-node integration | clauses/8.12.md | 51-66 |
| 8.13 | Overall procedures for MDT | clauses/8.13.md | 1-184 |
| 8.13.0 | General | clauses/8.13.md | 3-6 |
| 8.13.1 | Signalling based MDT activation | clauses/8.13.md | 7-20 |
| 8.13.2 | Management based MDT activation | clauses/8.13.md | 21-174 |
| 8.13.2.1 | General | clauses/8.13.md | 23-34 |
| 8.13.2.2 | Management based MDT Activation in gNB-CU-CP | clauses/8.13.md | 35-60 |
| 8.13.2.3 | Management based MDT Activation in gNB-DU | clauses/8.13.md | 61-86 |
| 8.13.2.4 | Management based MDT Activation in gNB-CU-UP | clauses/8.13.md | 87-112 |
| 8.13.2.5 | User consent propagation in EN-DC | clauses/8.13.md | 113-134 |
| 8.13.2.6 | User consent propagation in MR-DC with 5GC | clauses/8.13.md | 135-154 |
| 8.13.2.7 | Management based trace activation in MR-DC with 5GC | clauses/8.13.md | 155-174 |
| 8.13.3 | Alignment of MDT and QoE Measurements | clauses/8.13.md | 175-178 |
| 8.13.4 | MDT reporting | clauses/8.13.md | 179-184 |
| 8.14 | Self-optimisation | clauses/8.14.md | 1-42 |
| 8.14.1 | Overall procedures for MRO | clauses/8.14.md | 3-42 |
| 8.14.1.1 | Signalling of RLF information from gNB-CU to gNB-DU | clauses/8.14.md | 7-22 |
| 8.14.1.2 | Signalling of RACH information from gNB-CU to gNB-DU | clauses/8.14.md | 23-38 |
| 8.14.1.3 | Reporting of DL LBT failure information from gNB-DU to gNB-CU | clauses/8.14.md | 39-42 |
| 8.15 | Overall procedures for NR MBS | clauses/8.15.md | 1-220 |
| 8.15.1 | General | clauses/8.15.md | 3-174 |
| 8.15.1.1 | Broadcast MBS Session Setup | clauses/8.15.md | 7-38 |
| 8.15.1.1a | Broadcast MBS Session Setup for resource efficiency for MOCN | clauses/8.15.md | 39-70 |
| 8.15.1.1b | Broadcast MBS Session Setup for resource efficiency for RAN sharing with multiple cell-ID broadcast | clauses/8.15.md | 71-108 |
| 8.15.1.2 | Multicast MBS Session Context Establishment | clauses/8.15.md | 109-156 |
| 8.15.1.3 | Multicast MRB type re-configuration with F1-U ptp-retransmission tunnel establishment | clauses/8.15.md | 157-174 |
| 8.15.2 | Mobility procedure for Multicast | clauses/8.15.md | 175-220 |
| 8.15.2.1 | Inter-gNB-CU Mobility between MBS Supporting nodes | clauses/8.15.md | 177-220 |
| 8.16 | Overall procedures for CPAC | clauses/8.16.md | 1-26 |
| 8.16.1 | MN initiated Conditional PSCell Addition | clauses/8.16.md | 5-18 |
| 8.16.2 | MN initiated conditional SN Change | clauses/8.16.md | 19-22 |
| 8.16.3 | SN initiated conditional inter-SN Change | clauses/8.16.md | 23-26 |
| 8.17 | IAB Inter-CU Topology Management | clauses/8.17.md | 1-234 |
| 8.17.1 | IAB Inter-donor-DU Re-routing | clauses/8.17.md | 3-8 |
| 8.17.2 | IAB Inter-CU Topology Redundancy | clauses/8.17.md | 9-58 |
| 8.17.2.1 | IAB Inter-CU topological redundancy procedure | clauses/8.17.md | 11-58 |
| 8.17.3 | IAB Inter-CU Topology Adaptation | clauses/8.17.md | 59-174 |
| 8.17.3.1 | IAB inter-CU topology adaptation procedure | clauses/8.17.md | 61-126 |
| 8.17.3.2 | IAB inter-CU topology adaptation procedure with descendant IAB-node | clauses/8.17.md | 127-174 |
| 8.17.4 | IAB Inter-CU Backhaul RLF recovery for single connected IAB-node | clauses/8.17.md | 175-234 |
| 8.18 | Overall procedure for Small Data Transmission during RRC Inactive | clauses/8.18.md | 1-144 |
| 8.18.1 | RACH based SDT | clauses/8.18.md | 3-44 |
| 8.18.2 | CG based SDT | clauses/8.18.md | 45-94 |
| 8.18.3 | RA-SDT or non-SDT with CG-SDT configuration | clauses/8.18.md | 95-118 |
| 8.18.4 | MT-SDT | clauses/8.18.md | 119-144 |
| 8.19 | Overall procedures for L2 UE-to-Network Relay | clauses/8.19.md | 1-242 |
| 8.19.1 | Remote UE initial access | clauses/8.19.md | 3-74 |
| 8.19.2 | Remote UE RRC Reestablishment | clauses/8.19.md | 75-102 |
| 8.19.3 | Remote UE RRC Inactive to other states | clauses/8.19.md | 103-130 |
| 8.19.4 | Service Continuity for L2 U2N relay | clauses/8.19.md | 131-242 |
| 8.19.4.1 | Inter-gNB-DU switch from direct to indirect path | clauses/8.19.md | 133-166 |
| 8.19.4.2 | Intra-gNB-DU switch from direct to indirect path | clauses/8.19.md | 167-194 |
| 8.19.4.3 | Inter-gNB-CU switch from direct to indirect path | clauses/8.19.md | 195-242 |
| 8.20 | Void | clauses/8.20.md | 1-2 |
| 8.21 | Overall procedures for Network Controlled Repeater | clauses/8.21.md | 1-18 |
| 8.21.1 | Network Controlled Repeater Integration Procedure | clauses/8.21.md | 3-18 |
| 8.22 | Overall procedures for multi-path support | clauses/8.22.md | 1-164 |
| 8.22.1 | Inter-DU direct path addition on top of indirect path | clauses/8.22.md | 3-44 |
| 8.22.2 | Inter-DU indirect path addition on top of direct path | clauses/8.22.md | 45-92 |
| 8.22.3 | Intra-DU direct path addition on top of indirect path | clauses/8.22.md | 93-124 |
| 8.22.4 | Intra-DU indirect path addition on top of direct path | clauses/8.22.md | 125-164 |
| 8.23 | Mobile IAB migration procedures | clauses/8.23.md | 1-94 |
| 8.23.1 | Migration of mobile IAB-MT via Xn handover | clauses/8.23.md | 3-24 |
| 8.23.2 | Migration of mobile IAB-MT via NG handover | clauses/8.23.md | 25-40 |
| 8.23.3 | Mobile IAB-DU migration procedure | clauses/8.23.md | 41-74 |
| 8.23.4 | Mobile IAB-node RLF recovery | clauses/8.23.md | 75-94 |
| 8.24 | Timing resiliency service | clauses/8.24.md | 1-78 |
| 8.24.1 | RAN TSS reporting towards the CN | clauses/8.24.md | 5-46 |
| 8.24.2 | RAN TSS reporting towards the UE | clauses/8.24.md | 47-78 |
| 9 | Synchronization | clauses/9.md | 1-36 |
| 9.1 | gNB Synchronization | clauses/9.md | 3-36 |
| 10 | NG-RAN interfaces | clauses/10.md | 1-26 |
| 10.1 | NG interface | clauses/10.md | 3-6 |
| 10.2 | Xn interface | clauses/10.md | 7-10 |
| 10.3 | F1 interface | clauses/10.md | 11-14 |
| 10.4 | E1 interface | clauses/10.md | 15-18 |
| 10.5 | Antenna interface - general principles | clauses/10.md | 19-26 |
| 11 | Overall procedures in NG-RAN Architecure | clauses/11.md | 1-226 |
| 11.1 | Multiple TNLAs for Xn-C | clauses/11.md | 3-226 |
