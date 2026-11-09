# TS 29.244 V18.10.0 — PFCP (N4)

Clause index. `File` is relative to this directory; `Lines` is the 1-based
line range of the clause inside that file.

| Clause | Title | File | Lines |
|---|---|---|---|
| front-matter | Title page, foreword and scope front matter | clauses/front-matter.md | 1-1619 |
| 1 | Scope | clauses/1.md | 1-24 |
| 2 | References | clauses/2.md | 1-186 |
| 3 | Definitions, symbols and abbreviations | clauses/3.md | 1-230 |
| 3.1 | Definitions | clauses/3.md | 3-34 |
| 3.2 | Abbreviations | clauses/3.md | 35-230 |
| 4 | Protocol Stack | clauses/4.md | 1-64 |
| 4.1 | Introduction | clauses/4.md | 3-16 |
| 4.2 | UDP Header and Port Numbers | clauses/4.md | 17-36 |
| 4.2.1 | General | clauses/4.md | 19-22 |
| 4.2.2 | Request Message | clauses/4.md | 23-30 |
| 4.2.3 | Response Message | clauses/4.md | 31-36 |
| 4.3 | IP Header and IP Addresses | clauses/4.md | 37-56 |
| 4.3.1 | General | clauses/4.md | 39-42 |
| 4.3.2 | Request Message | clauses/4.md | 43-50 |
| 4.3.3 | Response Message | clauses/4.md | 51-56 |
| 4.4 | Layer 2 | clauses/4.md | 57-60 |
| 4.5 | Layer 1 | clauses/4.md | 61-64 |
| 5 | General description | clauses/5.md | 1-1 |
| 5.1 | Introduction | clauses/5.1.md | 1-10 |
| 5.2 | Packet Forwarding Model | clauses/5.2.md | 1-827 |
| 5.2.1 | General | clauses/5.2.md | 3-96 |
| 5.2.1A | Packet Detection Rule Handling | clauses/5.2.md | 97-186 |
| 5.2.2 | Usage Reporting Rule Handling | clauses/5.2.md | 187-553 |
| 5.2.2.1 | General | clauses/5.2.md | 189-198 |
| 5.2.2.2 | Provisioning of Usage Reporting Rule in the UP function | clauses/5.2.md | 199-354 |
| 5.2.2.2.1 | General | clauses/5.2.md | 201-330 |
| 5.2.2.2.2 | Credit pooling (for EPC) | clauses/5.2.md | 331-354 |
| 5.2.2.3 | Reporting of Usage Report to the CP function | clauses/5.2.md | 355-523 |
| 5.2.2.3.1 | General | clauses/5.2.md | 357-498 |
| 5.2.2.3.2 | Credit pooling | clauses/5.2.md | 499-515 |
| 5.2.2.3.3 | Traffic Usage Reporting with Redundant Transmission | clauses/5.2.md | 516-523 |
| 5.2.2.4 | Reporting of Linked Usage Reports to the CP function | clauses/5.2.md | 524-543 |
| 5.2.2.5 | End Marker Reception Reporting | clauses/5.2.md | 544-553 |
| 5.2.3 | Forwarding Action Rule Handling | clauses/5.2.md | 554-623 |
| 5.2.3.1 | General | clauses/5.2.md | 556-623 |
| 5.2.4 | Buffering Action Rule Handling | clauses/5.2.md | 624-679 |
| 5.2.4.1 | General | clauses/5.2.md | 626-649 |
| 5.2.4.2 | Provisioning of Buffering Action Rule in the UP function | clauses/5.2.md | 650-669 |
| 5.2.4.3 | Applying DL Buffering Duration in the CP function | clauses/5.2.md | 670-679 |
| 5.2.5 | QoS Enforcement Rule Handling | clauses/5.2.md | 680-711 |
| 5.2.5.1 | General | clauses/5.2.md | 682-685 |
| 5.2.5.2 | Provisioning of QoS Enforcement Rule in the UP function | clauses/5.2.md | 686-699 |
| 5.2.5.3 | Reflective QoS (for 5GC) | clauses/5.2.md | 700-711 |
| 5.2.6 | Combined SGW/PGW Architecture | clauses/5.2.md | 712-725 |
| 5.2.7 | Multi-Access Rule Handling (for 5GC) | clauses/5.2.md | 726-783 |
| 5.2.7.1 | General | clauses/5.2.md | 728-783 |
| 5.2.8 | Session Reporting Rule Handling | clauses/5.2.md | 784-815 |
| 5.2.8.1 | General | clauses/5.2.md | 786-797 |
| 5.2.8.2 | Provisioning of Session Reporting Rule in the UP function | clauses/5.2.md | 798-807 |
| 5.2.8.2.1 | General | clauses/5.2.md | 800-807 |
| 5.2.8.3 | Reporting of Session Report to the CP function | clauses/5.2.md | 808-815 |
| 5.2.8.3.1 | General | clauses/5.2.md | 810-815 |
| 5.2.9 | Handling of Rules that cannot be activated | clauses/5.2.md | 816-827 |
| 5.3 | Data Forwarding between the CP and UP Functions | clauses/5.3.md | 1-191 |
| 5.3.1 | General | clauses/5.3.md | 3-45 |
| 5.3.2 | Sending of End Marker Packets | clauses/5.3.md | 46-63 |
| 5.3.3 | Forwarding of Packets Subject to Buffering in the CP Function | clauses/5.3.md | 64-121 |
| 5.3.3.1 | General | clauses/5.3.md | 66-71 |
| 5.3.3.2 | Forwarding of Packets from the UP Function to the CP Function | clauses/5.3.md | 72-103 |
| 5.3.3.3 | Forwarding of Packets from the CP Function to the UP Function | clauses/5.3.md | 104-121 |
| 5.3.4 | Data Forwarding between the CP and UP Functions with one PFCP-u Tunnel per UP Function or PDN | clauses/5.3.md | 122-153 |
| 5.3.4.1 | General | clauses/5.3.md | 124-127 |
| 5.3.4.2 | Forwarding of Packets from the UP Function to the CP Function | clauses/5.3.md | 128-139 |
| 5.3.4.3 | Forwarding of Packets from the CP Function to the UP Function | clauses/5.3.md | 140-153 |
| 5.3.5 | Forwarding of user data using Control Plane CIoT 5GS Optimisation (for 5GC) | clauses/5.3.md | 154-191 |
| 5.3.5.1 | General | clauses/5.3.md | 156-161 |
| 5.3.5.2 | Forwarding of Packets from the UP Function to the CP Function | clauses/5.3.md | 162-181 |
| 5.3.5.3 | Forwarding of Packets from the CP Function to the UP Function | clauses/5.3.md | 182-191 |
| 5.4 | Policy and Charging Control | clauses/5.4.md | 1-486 |
| 5.4.1 | General | clauses/5.4.md | 3-6 |
| 5.4.2 | Service Detection and Bearer/QoS Flow Binding | clauses/5.4.md | 7-34 |
| 5.4.3 | Gating Control | clauses/5.4.md | 35-46 |
| 5.4.4 | QoS Control | clauses/5.4.md | 47-88 |
| 5.4.5 | DL Flow Level Marking for Application Detection | clauses/5.4.md | 89-100 |
| 5.4.6 | Usage Monitoring | clauses/5.4.md | 101-132 |
| 5.4.7 | Traffic Redirection | clauses/5.4.md | 133-158 |
| 5.4.8 | Traffic Steering | clauses/5.4.md | 159-186 |
| 5.4.9 | Provisioning of Predefined PCC/ADC Rules | clauses/5.4.md | 187-236 |
| 5.4.10 | Charging | clauses/5.4.md | 237-276 |
| 5.4.11 | (Un)solicited Application Reporting | clauses/5.4.md | 277-320 |
| 5.4.12 | Service Identification for Improved Radio Utilisation for GERAN | clauses/5.4.md | 321-328 |
| 5.4.13 | Transport Level Marking | clauses/5.4.md | 329-338 |
| 5.4.14 | Deferred PDR activation and deactivation | clauses/5.4.md | 339-364 |
| 5.4.15 | Packet Rate enforcement | clauses/5.4.md | 365-448 |
| 5.4.15.1 | General | clauses/5.4.md | 367-378 |
| 5.4.15.2 | Packet rate enforcement over Sxb and N4 interfaces | clauses/5.4.md | 379-408 |
| 5.4.15.3 | PGW and SMF behaviour | clauses/5.4.md | 409-448 |
| 5.4.16 | QoS differentiation for Stand-alone Non-Public Network (SNPN) | clauses/5.4.md | 449-480 |
| 5.4.16.1 | General | clauses/5.4.md | 451-460 |
| 5.4.16.2 | Access to PLMN services via SNPN | clauses/5.4.md | 461-470 |
| 5.4.16.3 | Access to SNPN services via PLMN | clauses/5.4.md | 471-480 |
| 5.4.17 | QoS differentiation for UEs behind RG | clauses/5.4.md | 481-486 |
| 5.5 | F-TEID Allocation and Release | clauses/5.5.md | 1-32 |
| 5.5.1 | General | clauses/5.5.md | 3-8 |
| 5.5.2 | Void | clauses/5.5.md | 9-10 |
| 5.5.3 | F-TEID allocation in the UP function | clauses/5.5.md | 11-32 |
| 5.6 | PFCP Session Handling | clauses/5.6.md | 1-34 |
| 5.6.1 | General | clauses/5.6.md | 3-6 |
| 5.6.2 | Session Endpoint Identifier Handling | clauses/5.6.md | 7-12 |
| 5.6.3 | Modifying the Rules of an Existing PFCP Session | clauses/5.6.md | 13-34 |
| 5.7 | Support of Lawful Interception | clauses/5.7.md | 1-20 |
| 5.7.1 | General | clauses/5.7.md | 3-6 |
| 5.7.2 | Lawful Interception in EPC | clauses/5.7.md | 7-16 |
| 5.7.3 | Lawful Interception in 5GC | clauses/5.7.md | 17-20 |
| 5.8 | PFCP Association | clauses/5.8.md | 1-62 |
| 5.8.1 | General | clauses/5.8.md | 3-24 |
| 5.8.2 | Behaviour with an Established PFCP Association | clauses/5.8.md | 25-52 |
| 5.8.3 | Behaviour without an Established PFCP Association | clauses/5.8.md | 53-62 |
| 5.9 | Usage of Vendor-specific IE | clauses/5.9.md | 1-12 |
| 5.10 | Error Indication Handling | clauses/5.10.md | 1-18 |
| 5.10A | User Plane Path Failure or Recovery Handling | clauses/5.10A.md | 1-8 |
| 5.11 | User plane inactivity detection and reporting | clauses/5.11.md | 1-38 |
| 5.11.1 | General | clauses/5.11.md | 3-6 |
| 5.11.2 | User plane inactivity detection and reporting per PDN connection or PDU session | clauses/5.11.md | 7-30 |
| 5.11.3 | User plane inactivity detection and reporting per PDR | clauses/5.11.md | 31-38 |
| 5.12 | Suspend and Resume Notification procedures | clauses/5.12.md | 1-14 |
| 5.13 | Ethernet traffic (for 5GC) | clauses/5.13.md | 1-128 |
| 5.13.1 | General | clauses/5.13.md | 3-52 |
| 5.13.2 | Address Resolution Protocol or IPv6 Neighbour Solicitation Response by SMF | clauses/5.13.md | 53-64 |
| 5.13.3 | Address Resolution Protocol or IPv6 Neighbour Solicitation Response by UPF | clauses/5.13.md | 65-74 |
| 5.13.3A | Provisioning of MAC addresses and SDF filters in Ethernet Packet Filters | clauses/5.13.md | 75-82 |
| 5.13.4 | Bidirectional Ethernet Filters | clauses/5.13.md | 83-98 |
| 5.13.5 | Reporting of UE MAC addresses to the SMF | clauses/5.13.md | 99-118 |
| 5.13.6 | Ethernet PDU session anchor relocation | clauses/5.13.md | 119-128 |
| 5.14 | Support IPv6 Prefix Delegation | clauses/5.14.md | 1-20 |
| 5.15 | Signalling based Trace (De)Activation | clauses/5.15.md | 1-10 |
| 5.15A | UE level measurement (De)Activation | clauses/5.15A.md | 1-64 |
| 5.16 | Framed Routing | clauses/5.16.md | 1-14 |
| 5.17 | 5G UPF (for 5GC) | clauses/5.17.md | 1-58 |
| 5.17.1 | Introduction | clauses/5.17.md | 3-6 |
| 5.17.2 | Uplink Classifier and Branching Point | clauses/5.17.md | 7-26 |
| 5.17.3 | Data forwarding during handovers between 5GS and EPS | clauses/5.17.md | 27-58 |
| 5.18 | Enhanced PFCP Association Release | clauses/5.18.md | 1-38 |
| 5.18.1 | General | clauses/5.18.md | 3-24 |
| 5.18.2 | UP Function Initiated PFCP Session Release | clauses/5.18.md | 25-38 |
| 5.19 | Activation and Deactivation of Pre-defined PDRs | clauses/5.19.md | 1-36 |
| 5.20 | Support of Access Traffic Steering, Switching and Splitting (ATSSS) for 5GC | clauses/5.20.md | 1-228 |
| 5.20.1 | General | clauses/5.20.md | 3-40 |
| 5.20.2 | MPTCP functionality | clauses/5.20.md | 41-88 |
| 5.20.2.1 | General | clauses/5.20.md | 43-48 |
| 5.20.2.2 | Activate MPTCP functionality and Exchange MPTCP Parameters | clauses/5.20.md | 49-60 |
| 5.20.2.3 | Control of Multipath TCP Connection Establishment by MPTCP Proxy | clauses/5.20.md | 61-80 |
| 5.20.2.4 | Traffic Steering and IP Translation by MPTCP Proxy | clauses/5.20.md | 81-88 |
| 5.20.2A | MPQUIC functionality | clauses/5.20.md | 89-144 |
| 5.20.3 | ATSSS-LL functionality | clauses/5.20.md | 145-168 |
| 5.20.3.1 | Activate ATSSS-LL functionality and Exchange ATSSS-LL Parameters | clauses/5.20.md | 147-168 |
| 5.20.4 | Handling of GBR traffic of a MA PDU session | clauses/5.20.md | 169-188 |
| 5.20.4.1 | General | clauses/5.20.md | 171-182 |
| 5.20.4.2 | Access Availability Reporting | clauses/5.20.md | 183-188 |
| 5.20.5 | Access type of an MA PDU session becoming (un)available | clauses/5.20.md | 189-200 |
| 5.20.6 | PMFP message handling in UPF | clauses/5.20.md | 201-228 |
| 5.21 | UE IP address/prefix Allocation and Release | clauses/5.21.md | 1-94 |
| 5.21.1 | General | clauses/5.21.md | 3-28 |
| 5.21.2 | UE IP address/prefix allocation in the CP function | clauses/5.21.md | 29-46 |
| 5.21.2.1 | General | clauses/5.21.md | 31-34 |
| 5.21.2.2 | UE IP Address/prefix allocation using DHCP or AAA server | clauses/5.21.md | 35-46 |
| 5.21.3 | UE IP address/prefix allocation in the UP function | clauses/5.21.md | 47-94 |
| 5.21.3.1 | General | clauses/5.21.md | 49-76 |
| 5.21.3.2 | Reporting UE IP Address Usage to the CP function | clauses/5.21.md | 77-94 |
| 5.22 | PFCP sessions successively controlled by different SMFs of an SMF set (for 5GC) | clauses/5.22.md | 1-124 |
| 5.22.1 | General | clauses/5.22.md | 3-18 |
| 5.22.2 | With one PFCP association per SMF Set and UPF | clauses/5.22.md | 19-58 |
| 5.22.3 | With one PFCP association per SMF and UPF | clauses/5.22.md | 59-108 |
| 5.22.4 | Restoration of PFCP Sessions associated with an FQ-CSID, Group ID or PGW-C/SMF IP Address | clauses/5.22.md | 109-124 |
| 5.23 | 5G VN Group Communication (for 5GC) | clauses/5.23.md | 1-44 |
| 5.23.1 | General | clauses/5.23.md | 3-32 |
| 5.23.2 | 5G VN group communication without N6-based forwarding | clauses/5.23.md | 33-44 |
| 5.24 | Support of Ultra Reliable Low Latency Communication for 5GC | clauses/5.24.md | 1-180 |
| 5.24.1 | General | clauses/5.24.md | 3-16 |
| 5.24.2 | Redundant Transmission on N3/N9 interfaces | clauses/5.24.md | 17-66 |
| 5.24.2.1 | General | clauses/5.24.md | 19-26 |
| 5.24.2.2 | GTP-U tunnel setup for redundant transmission | clauses/5.24.md | 27-52 |
| 5.24.2.3 | Duplicating downlink packets for redundant transmission | clauses/5.24.md | 53-62 |
| 5.24.2.4 | Eliminating duplicated uplink packets | clauses/5.24.md | 63-66 |
| 5.24.3 | Redundant Transmission at transport layer | clauses/5.24.md | 67-76 |
| 5.24.4 | Per QoS Flow Per UE QoS Monitoring | clauses/5.24.md | 77-118 |
| 5.24.4.1 | General | clauses/5.24.md | 79-88 |
| 5.24.4.2 | QoS Monitoring Control | clauses/5.24.md | 89-98 |
| 5.24.4.3 | QoS Monitoring Reporting | clauses/5.24.md | 99-118 |
| 5.24.5 | Per GTP-U Path QoS Monitoring | clauses/5.24.md | 119-180 |
| 5.24.5.1 | General | clauses/5.24.md | 121-126 |
| 5.24.5.2 | GTP-U path monitoring | clauses/5.24.md | 127-152 |
| 5.24.5.3 | QoS monitoring of a PDU session based on GTP-U path monitoring | clauses/5.24.md | 153-172 |
| 5.24.5.4 | QoS Monitoring Reporting | clauses/5.24.md | 173-180 |
| 5.25 | Support of IPTV (for 5GC) | clauses/5.25.md | 1-44 |
| 5.26 | Support of Time Sensitive Communication, Time Synchronization, 5GS integration with TSN and Deterministic Networking (for 5GC) | clauses/5.26.md | 1-84 |
| 5.26.1 | General | clauses/5.26.md | 3-22 |
| 5.26.2 | 5GS User Plane Node management | clauses/5.26.md | 23-38 |
| 5.26.3 | Transfer of 5GS user plane node and port management information | clauses/5.26.md | 39-68 |
| 5.26.3.1 | General | clauses/5.26.md | 41-52 |
| 5.26.3.2 | Direct Reporting of TSC management information event to TSN AF or TSCTSF | clauses/5.26.md | 53-68 |
| 5.26.4 | Reporting clock drift between External and 5GS times from UPF to SMF | clauses/5.26.md | 69-84 |
| 5.26A | Support of TSN enabled Transport Network | clauses/5.26A.md | 1-22 |
| 5.27 | Inter-PLMN User Plane Security | clauses/5.27.md | 1-10 |
| 5.28 | Downlink data delivery status with UPF buffering (for 5GC) | clauses/5.28.md | 1-32 |
| 5.28.1 | General | clauses/5.28.md | 3-32 |
| 5.29 | Support Reliable Data Service | clauses/5.29.md | 1-12 |
| 5.30 | Notifying Start Pause of Charging | clauses/5.30.md | 1-34 |
| 5.31 | Support of L2TP | clauses/5.31.md | 1-62 |
| 5.31.1 | General | clauses/5.31.md | 3-16 |
| 5.31.2 | L2TP Tunnel and L2TP Session Setup | clauses/5.31.md | 17-48 |
| 5.31.3 | L2TP Session and L2TP Tunnel Release | clauses/5.31.md | 49-62 |
| 5.32 | Support of Uplink packets buffering | clauses/5.32.md | 1-16 |
| 5.32.1 | General | clauses/5.32.md | 3-6 |
| 5.32.2 | Uplink packets buffering for on-line charging | clauses/5.32.md | 7-10 |
| 5.32.3 | Uplink packets buffering during EAS relocation | clauses/5.32.md | 11-16 |
| 5.33 | Support of enhancement of Edge Computing (for 5GC) | clauses/5.33.md | 1-76 |
| 5.33.1 | General | clauses/5.33.md | 3-6 |
| 5.33.2 | Uplink packet buffering for low packet loss during EAS relocation | clauses/5.33.md | 7-10 |
| 5.33.3 | Edge Relocation using EAS IP address and Port number Replacement | clauses/5.33.md | 11-20 |
| 5.33.4 | EAS Discovery procedure with Local DNS Server/Resolver | clauses/5.33.md | 21-32 |
| 5.33.5 | Direct Reporting of QoS monitoring events to Local NEF or AF | clauses/5.33.md | 33-42 |
| 5.33.6 | EAS Discovery procedure with V-EASDF | clauses/5.33.md | 43-50 |
| 5.33.7 | DNS traffic routing for different UEs with same private UE IP address | clauses/5.33.md | 51-76 |
| 5.34 | Support of 5G Multicast and Broadcast Service | clauses/5.34.md | 1-240 |
| 5.34.1 | General | clauses/5.34.md | 3-8 |
| 5.34.2 | N4mb requirements | clauses/5.34.md | 9-138 |
| 5.34.2.1 | General | clauses/5.34.md | 11-16 |
| 5.34.2.1A | PFCP protocol extensions for N4mb | clauses/5.34.md | 17-44 |
| 5.34.2.2 | Instructing the MB-UPF to forward MBS data using multicast and/or unicast transport | clauses/5.34.md | 45-90 |
| 5.34.2.3 | Detecting and reporting user plane (in)activity of an MBS session | clauses/5.34.md | 91-98 |
| 5.34.2.4 | Activation and Deactivation of a Multicast MBS session | clauses/5.34.md | 99-118 |
| 5.34.2.5 | MBS data usage reporting for MBS charging | clauses/5.34.md | 119-138 |
| 5.34.3 | N4 requirements | clauses/5.34.md | 139-240 |
| 5.34.3.1 | General | clauses/5.34.md | 141-150 |
| 5.34.3.2 | Instructing the UPF to forward (or stop forwarding) multicast MBS data to associated PDU sessions | clauses/5.34.md | 151-210 |
| 5.34.3.3 | Instructing a combined UPF/MBS-UPF to forward multicast MBS data to associated PDU sessions | clauses/5.34.md | 211-226 |
| 5.34.3.4 | MBS data usage reporting for MBS charging | clauses/5.34.md | 227-240 |
| 5.35 | Support of Per Slice UP Resource Allocation and Usage Reporting by the UP Function | clauses/5.35.md | 1-32 |
| 5.35.1 | General | clauses/5.35.md | 3-32 |
| 5.36 | Paging Policy Indicator Provisioning | clauses/5.36.md | 1-26 |
| 5.36.1 | General | clauses/5.36.md | 3-16 |
| 5.36.2 | Enhanced Paging Policy Indicator Provisioning | clauses/5.36.md | 17-26 |
| 5.37 | Traffic Parameters Measurement per QoS flow | clauses/5.37.md | 1-24 |
| 5.37.1 | General | clauses/5.37.md | 3-6 |
| 5.37.2 | Traffic Parameter Measurement Control | clauses/5.37.md | 7-20 |
| 5.37.3 | Traffic Parameter Measurement Report | clauses/5.37.md | 21-24 |
| 5.38 | Support for high data rate low latency services, (eXtended Reality) XR and interactive media services | clauses/5.38.md | 1-128 |
| 5.38.0 | General | clauses/5.38.md | 3-16 |
| 5.38.1 | Support of ECN marking for L4S | clauses/5.38.md | 17-48 |
| 5.38.2 | Support of Network Exposure of 5GS information | clauses/5.38.md | 49-54 |
| 5.38.3 | Support of PDU Set based QoS Handling | clauses/5.38.md | 55-96 |
| 5.38.4 | N6 Jitter Measurement and End of Data Burst Marking | clauses/5.38.md | 97-128 |
| 5.38.4.1 | General | clauses/5.38.md | 99-106 |
| 5.38.4.2 | N6 Jitter and UL/DL Periodicity Measurement Control | clauses/5.38.md | 107-116 |
| 5.38.4.3 | N6 Jitter and UL/DL Periodicity Measurement Report | clauses/5.38.md | 117-120 |
| 5.38.4.4 | End of Data Burst Marking | clauses/5.38.md | 121-128 |
| 5.39 | QoS flow related QoS monitoring and reporting | clauses/5.39.md | 1-130 |
| 5.39.1 | General | clauses/5.39.md | 3-8 |
| 5.39.2 | QoS Monitoring Control | clauses/5.39.md | 9-56 |
| 5.39.3 | Measurable QoS parameters and specific requirements for their measurement | clauses/5.39.md | 57-114 |
| 5.39.3.1 | General | clauses/5.39.md | 59-62 |
| 5.39.3.2 | Packet delay monitoring | clauses/5.39.md | 63-72 |
| 5.39.3.3 | Congestion information monitoring | clauses/5.39.md | 73-92 |
| 5.39.3.4 | Data rate monitoring | clauses/5.39.md | 93-114 |
| 5.39.4 | QoS Monitoring Reporting | clauses/5.39.md | 115-130 |
| 5.40 | Support of UPF event subscription via Service Based Interface (for 5GC) | clauses/5.40.md | 1-12 |
| 6 | Procedures | clauses/6.md | 1-720 |
| 6.1 | Introduction | clauses/6.md | 3-6 |
| 6.2 | PFCP Node Related Procedures | clauses/6.md | 7-560 |
| 6.2.1 | General | clauses/6.md | 9-12 |
| 6.2.2 | Heartbeat Procedure | clauses/6.md | 13-34 |
| 6.2.2.1 | General | clauses/6.md | 15-20 |
| 6.2.2.2 | Heartbeat Request | clauses/6.md | 21-30 |
| 6.2.2.3 | Heartbeat Response | clauses/6.md | 31-34 |
| 6.2.3 | Load Control Procedure | clauses/6.md | 35-122 |
| 6.2.3.1 | General | clauses/6.md | 37-48 |
| 6.2.3.2 | Principles | clauses/6.md | 49-58 |
| 6.2.3.3 | Load Control Information | clauses/6.md | 59-122 |
| 6.2.3.3.1 | General Description | clauses/6.md | 61-82 |
| 6.2.3.3.2 | Parameters | clauses/6.md | 83-108 |
| 6.2.3.3.2.1 | Load Control Sequence Number | clauses/6.md | 85-96 |
| 6.2.3.3.2.2 | Load Metric | clauses/6.md | 97-108 |
| 6.2.3.3.3 | Frequency of Inclusion | clauses/6.md | 109-122 |
| 6.2.4 | Overload Control Procedure | clauses/6.md | 123-296 |
| 6.2.4.1 | General | clauses/6.md | 125-136 |
| 6.2.4.2 | Principles | clauses/6.md | 137-150 |
| 6.2.4.3 | Overload Control Information | clauses/6.md | 151-236 |
| 6.2.4.3.1 | General Description | clauses/6.md | 153-176 |
| 6.2.4.3.2 | Parameters | clauses/6.md | 177-222 |
| 6.2.4.3.2.1 | Overload Control Sequence Number | clauses/6.md | 179-194 |
| 6.2.4.3.2.2 | Period of Validity | clauses/6.md | 195-208 |
| 6.2.4.3.2.3 | Overload Reduction Metric | clauses/6.md | 209-222 |
| 6.2.4.3.3 | Frequency of Inclusion | clauses/6.md | 223-236 |
| 6.2.4.4 | Message Throttling | clauses/6.md | 237-264 |
| 6.2.4.4.1 | General | clauses/6.md | 239-246 |
| 6.2.4.4.2 | Throttling algorithm – "Loss" | clauses/6.md | 247-264 |
| 6.2.4.4.2.1 | Description | clauses/6.md | 249-264 |
| 6.2.4.5 | Message Prioritization | clauses/6.md | 265-296 |
| 6.2.4.5.1 | Description | clauses/6.md | 267-278 |
| 6.2.4.5.2 | Based on the Message Priority Signalled in the PFCP Message | clauses/6.md | 279-296 |
| 6.2.5 | PFCP PFD Management Procedure | clauses/6.md | 297-340 |
| 6.2.5.1 | General | clauses/6.md | 299-310 |
| 6.2.5.2 | CP Function Behaviour | clauses/6.md | 311-320 |
| 6.2.5.3 | UP Function Behaviour | clauses/6.md | 321-340 |
| 6.2.6 | PFCP Association Setup Procedure | clauses/6.md | 341-444 |
| 6.2.6.1 | General | clauses/6.md | 343-352 |
| 6.2.6.2 | PFCP Association Setup Initiated by the CP Function | clauses/6.md | 353-404 |
| 6.2.6.2.1 | CP Function Behaviour | clauses/6.md | 355-370 |
| 6.2.6.2.2 | UP Function behaviour | clauses/6.md | 371-404 |
| 6.2.6.3 | PFCP Association Setup Initiated by the UP Function | clauses/6.md | 405-444 |
| 6.2.6.3.1 | UP Function Behaviour | clauses/6.md | 407-426 |
| 6.2.6.3.2 | CP Function Behaviour | clauses/6.md | 427-444 |
| 6.2.7 | PFCP Association Update Procedure | clauses/6.md | 445-504 |
| 6.2.7.1 | General | clauses/6.md | 447-452 |
| 6.2.7.2 | PFCP Association Update Procedure Initiated by the CP Function | clauses/6.md | 453-472 |
| 6.2.7.2.1 | CP Function Behaviour | clauses/6.md | 455-460 |
| 6.2.7.2.2 | UP Function Behaviour | clauses/6.md | 461-472 |
| 6.2.7.3 | PFCP Association Update Procedure Initiated by UP Function | clauses/6.md | 473-504 |
| 6.2.7.3.1 | UP Function Behaviour | clauses/6.md | 475-488 |
| 6.2.7.3.2 | CP Function Behaviour | clauses/6.md | 489-504 |
| 6.2.8 | PFCP Association Release Procedure | clauses/6.md | 505-536 |
| 6.2.8.1 | General | clauses/6.md | 507-518 |
| 6.2.8.2 | CP Function Behaviour | clauses/6.md | 519-524 |
| 6.2.8.3 | UP Function behaviour | clauses/6.md | 525-536 |
| 6.2.9 | PFCP Node Report Procedure | clauses/6.md | 537-560 |
| 6.2.9.1 | General | clauses/6.md | 539-544 |
| 6.2.9.2 | UP Function Behaviour | clauses/6.md | 545-552 |
| 6.2.9.3 | CP Function behaviour | clauses/6.md | 553-560 |
| 6.3 | PFCP Session Related Procedures | clauses/6.md | 561-686 |
| 6.3.1 | General | clauses/6.md | 563-566 |
| 6.3.2 | PFCP Session Establishment Procedure | clauses/6.md | 567-596 |
| 6.3.2.1 | General | clauses/6.md | 569-572 |
| 6.3.2.2 | CP Function Behaviour | clauses/6.md | 573-584 |
| 6.3.2.3 | UP Function Behaviour | clauses/6.md | 585-596 |
| 6.3.3 | PFCP Session Modification Procedure | clauses/6.md | 597-634 |
| 6.3.3.1 | General | clauses/6.md | 599-602 |
| 6.3.3.2 | CP Function behaviour | clauses/6.md | 603-618 |
| 6.3.3.3 | UP Function Behaviour | clauses/6.md | 619-634 |
| 6.3.4 | PFCP Session Deletion Procedure | clauses/6.md | 635-658 |
| 6.3.4.1 | General | clauses/6.md | 637-640 |
| 6.3.4.2 | CP Function Behaviour | clauses/6.md | 641-650 |
| 6.3.4.3 | UP Function Behaviour | clauses/6.md | 651-658 |
| 6.3.5 | PFCP Session Report Procedure | clauses/6.md | 659-686 |
| 6.3.5.1 | General | clauses/6.md | 661-664 |
| 6.3.5.2 | UP Function Behaviour | clauses/6.md | 665-674 |
| 6.3.5.3 | CP Function Behaviour | clauses/6.md | 675-686 |
| 6.4 | Reliable Delivery of PFCP Messages | clauses/6.md | 687-702 |
| 6.5 | PFCP messages bundling | clauses/6.md | 703-720 |
| 7 | Messages and Message Formats | clauses/7.md | 1-1 |
| 7.1 | Transmission Order and Bit Definitions | clauses/7.1.md | 1-6 |
| 7.2 | Message Format | clauses/7.2.md | 1-247 |
| 7.2.1 | General | clauses/7.2.md | 3-17 |
| 7.2.1A | PFCP messages bundled in one UDP/IP packet | clauses/7.2.md | 18-40 |
| 7.2.2 | Message Header | clauses/7.2.md | 41-169 |
| 7.2.2.1 | General Format | clauses/7.2.md | 43-79 |
| 7.2.2.2 | PFCP Header for Node Related Messages | clauses/7.2.md | 80-97 |
| 7.2.2.3 | PFCP Header for Session Related Messages | clauses/7.2.md | 98-123 |
| 7.2.2.4 | Usage of the PFCP Header | clauses/7.2.md | 124-169 |
| 7.2.2.4.1 | General | clauses/7.2.md | 126-157 |
| 7.2.2.4.2 | Conditions for Sending SEID=0 in PFCP Header | clauses/7.2.md | 158-169 |
| 7.2.3 | Information Elements | clauses/7.2.md | 170-247 |
| 7.2.3.1 | General | clauses/7.2.md | 172-175 |
| 7.2.3.2 | Presence Requirements of Information Elements | clauses/7.2.md | 176-221 |
| 7.2.3.3 | Grouped Information Elements | clauses/7.2.md | 222-237 |
| 7.2.3.4 | Information Element Type | clauses/7.2.md | 238-247 |
| 7.3 | Message Types | clauses/7.3.md | 1-42 |
| 7.4 | PFCP Node Related Messages | clauses/7.4.md | 1-470 |
| 7.4.1 | General | clauses/7.4.md | 3-6 |
| 7.4.2 | Heartbeat Messages | clauses/7.4.md | 7-29 |
| 7.4.2.1 | Heartbeat Request | clauses/7.4.md | 9-19 |
| 7.4.2.2 | Heartbeat Response | clauses/7.4.md | 20-29 |
| 7.4.3 | PFCP PFD Management | clauses/7.4.md | 30-74 |
| 7.4.3.1 | PFCP PFD Management Request | clauses/7.4.md | 32-63 |
| 7.4.3.2 | PFCP PFD Management Response | clauses/7.4.md | 64-74 |
| 7.4.4 | PFCP Association messages | clauses/7.4.md | 75-270 |
| 7.4.4.1 | PFCP Association Setup Request | clauses/7.4.md | 77-165 |
| 7.4.4.1.1 | General | clauses/7.4.md | 79-123 |
| 7.4.4.1.2 | Clock Drift Control Information IE within PFCP Association Setup Request | clauses/7.4.md | 124-142 |
| 7.4.4.1.3 | GTP-U Path QoS Control Information IE within PFCP Association Setup Request | clauses/7.4.md | 143-165 |
| 7.4.4.2 | PFCP Association Setup Response | clauses/7.4.md | 166-187 |
| 7.4.4.3 | PFCP Association Update Request | clauses/7.4.md | 188-229 |
| 7.4.4.3.1 | UE IP Address Usage Information IE within PFCP Association Update Request | clauses/7.4.md | 209-229 |
| 7.4.4.4 | PFCP Association Update Response | clauses/7.4.md | 230-243 |
| 7.4.4.5 | PFCP Association Release Request | clauses/7.4.md | 244-253 |
| 7.4.4.6 | PFCP Association Release Response | clauses/7.4.md | 254-264 |
| 7.4.4.7 | PFCP Version Not Supported Response | clauses/7.4.md | 265-270 |
| 7.4.5 | PFCP Node Report Procedure | clauses/7.4.md | 271-393 |
| 7.4.5.1 | PFCP Node Report Request | clauses/7.4.md | 273-378 |
| 7.4.5.1.1 | General | clauses/7.4.md | 275-293 |
| 7.4.5.1.2 | User Plane Path Failure Report IE within PFCP Node Report Request | clauses/7.4.md | 294-305 |
| 7.4.5.1.3 | User Plane Path Recovery Report IE within PFCP Node Report Request | clauses/7.4.md | 306-317 |
| 7.4.5.1.4 | Clock Drift Report IE within PFCP Node Report Request | clauses/7.4.md | 318-335 |
| 7.4.5.1.5 | GTP-U Path QoS Report IE within PFCP Node Report Request | clauses/7.4.md | 336-352 |
| 7.4.5.1.6 | QoS Information in GTP-U Path QoS Report IE | clauses/7.4.md | 353-366 |
| 7.4.5.1.7 | Peer UP Restart Report IE within PFCP Node Report Request | clauses/7.4.md | 367-378 |
| 7.4.5.2 | PFCP Node Report Response | clauses/7.4.md | 379-393 |
| 7.4.5.2.1 | General | clauses/7.4.md | 381-393 |
| 7.4.6 | PFCP Session Set Deletion | clauses/7.4.md | 394-427 |
| 7.4.6.1 | PFCP Session Set Deletion Request | clauses/7.4.md | 396-414 |
| 7.4.6.2 | PFCP Session Set Deletion Response | clauses/7.4.md | 415-427 |
| 7.4.7 | PFCP Session Set Modification | clauses/7.4.md | 428-470 |
| 7.4.7.1 | PFCP Session Set Modification Request | clauses/7.4.md | 430-457 |
| 7.4.7.2 | PFCP Session Set Modification Response | clauses/7.4.md | 458-470 |
| 7.5 | PFCP Session Related Messages | clauses/7.5.md | 1-1 |
| 7.5.1 | General | clauses/7.5.1.md | 1-4 |
| 7.5.2 | PFCP Session Establishment Request | clauses/7.5.2.md | 1-673 |
| 7.5.2.1 | General | clauses/7.5.2.md | 3-114 |
| 7.5.2.2 | Create PDR IE within PFCP Session Establishment Request | clauses/7.5.2.md | 115-266 |
| 7.5.2.3 | Create FAR IE within PFCP Session Establishment Request | clauses/7.5.2.md | 267-364 |
| 7.5.2.4 | Create URR IE within PFCP Session Establishment Request | clauses/7.5.2.md | 365-436 |
| 7.5.2.5 | Create QER IE within PFCP Session Establishment Request | clauses/7.5.2.md | 437-464 |
| 7.5.2.6 | Create BAR IE within PFCP Session Establishment Request | clauses/7.5.2.md | 465-484 |
| 7.5.2.7 | Create Traffic Endpoint IE within PFCP Session Establishment Request | clauses/7.5.2.md | 485-516 |
| 7.5.2.8 | Create MAR IE within PFCP Session Establishment Request | clauses/7.5.2.md | 517-562 |
| 7.5.2.9 | Create SRR IE within PFCP Session Establishment Request | clauses/7.5.2.md | 563-644 |
| 7.5.2.10 | Provide ATSSS Control Information IE within PFCP Session Establishment Request | clauses/7.5.2.md | 645-660 |
| 7.5.2.11 | Provide RDS Configuration Information IE within PFCP Session Establishment Request | clauses/7.5.2.md | 661-673 |
| 7.5.3 | PFCP Session Establishment Response | clauses/7.5.3.md | 1-226 |
| 7.5.3.1 | General | clauses/7.5.3.md | 3-78 |
| 7.5.3.2 | Created PDR IE within PFCP Session Establishment Response | clauses/7.5.3.md | 79-97 |
| 7.5.3.3 | Load Control Information IE within PFCP Session Establishment Response | clauses/7.5.3.md | 98-111 |
| 7.5.3.4 | Overload Control Information IE within PFCP Session Establishment Response | clauses/7.5.3.md | 112-127 |
| 7.5.3.5 | Created Traffic Endpoint IE within PFCP Session Establishment Response | clauses/7.5.3.md | 128-146 |
| 7.5.3.6 | Created Bridge/Router Info IE within PFCP Session Establishment Response | clauses/7.5.3.md | 147-160 |
| 7.5.3.7 | ATSSS Control Parameters IE within PFCP Session Establishment Response | clauses/7.5.3.md | 161-224 |
| 7.5.3.8 | Void | clauses/7.5.3.md | 225-226 |
| 7.5.4 | PFCP Session Modification Request | clauses/7.5.4.md | 1-525 |
| 7.5.4.1 | General | clauses/7.5.4.md | 3-65 |
| 7.5.4.2 | Update PDR IE within PFCP Session Modification Request | clauses/7.5.4.md | 66-93 |
| 7.5.4.3 | Update FAR IE within PFCP Session Modification Request | clauses/7.5.4.md | 94-161 |
| 7.5.4.4 | Update URR IE within PFCP Session Modification Request | clauses/7.5.4.md | 162-207 |
| 7.5.4.5 | Update QER IE within PFCP Session Modification Request | clauses/7.5.4.md | 208-234 |
| 7.5.4.6 | Remove PDR IE within PFCP Session Modification Request | clauses/7.5.4.md | 235-249 |
| 7.5.4.7 | Remove FAR IE within PFCP Session Modification Request | clauses/7.5.4.md | 250-262 |
| 7.5.4.8 | Remove URR IE within PFCP Session Modification Request | clauses/7.5.4.md | 263-275 |
| 7.5.4.9 | Remove QER IE PFCP Session Modification Request | clauses/7.5.4.md | 276-288 |
| 7.5.4.10 | Query URR IE within PFCP Session Modification Request | clauses/7.5.4.md | 289-303 |
| 7.5.4.11 | Update BAR IE within PFCP Session Modification Request | clauses/7.5.4.md | 304-325 |
| 7.5.4.12 | Remove BAR IE within PFCP Session Modification Request | clauses/7.5.4.md | 326-338 |
| 7.5.4.13 | Update Traffic Endpoint IE within PFCP Session Modification Request | clauses/7.5.4.md | 339-363 |
| 7.5.4.14 | Remove Traffic Endpoint IE within PFCP Session Modification Request | clauses/7.5.4.md | 364-376 |
| 7.5.4.15 | Remove MAR IE within PFCP Session Modification Request | clauses/7.5.4.md | 377-389 |
| 7.5.4.16 | Update MAR IE within PFCP Session Modification Request | clauses/7.5.4.md | 390-435 |
| 7.5.4.17 | Create PDR/FAR/URR/QER/BAR/MAR IEs within PFCP Session Modification Request | clauses/7.5.4.md | 436-439 |
| 7.5.4.18 | TSC Management Information IE within PFCP Session Modification Request | clauses/7.5.4.md | 440-467 |
| 7.5.4.19 | Remove SRR IE within PFCP Session Modification Request | clauses/7.5.4.md | 468-480 |
| 7.5.4.20 | Update SRR IE within PFCP Session Modification Request | clauses/7.5.4.md | 481-498 |
| 7.5.4.21 | Ethernet Context Information within PFCP Session Modification Request | clauses/7.5.4.md | 499-512 |
| 7.5.4.22 | Query Packet Rate Status IE within PFCP Session Modification Request | clauses/7.5.4.md | 513-525 |
| 7.5.5 | PFCP Session Modification Response | clauses/7.5.5.md | 1-101 |
| 7.5.5.1 | General | clauses/7.5.5.md | 3-30 |
| 7.5.5.2 | Usage Report IE within PFCP Session Modification Response | clauses/7.5.5.md | 31-55 |
| 7.5.5.3 | TSC Management Information IE within PFCP Session Modification Response | clauses/7.5.5.md | 56-70 |
| 7.5.5.4 | Packet Rate Status Report IE within PFCP Session Modification Response | clauses/7.5.5.md | 71-84 |
| 7.5.5.5 | Updated PDR IE within PFCP Session Modification Response | clauses/7.5.5.md | 85-101 |
| 7.5.6 | PFCP Session Deletion Request | clauses/7.5.6.md | 1-14 |
| 7.5.7 | PFCP Session Deletion Response | clauses/7.5.7.md | 1-57 |
| 7.5.7.1 | General | clauses/7.5.7.md | 3-33 |
| 7.5.7.2 | Usage Report IE within PFCP Session Deletion Response | clauses/7.5.7.md | 34-57 |
| 7.5.8 | PFCP Session Report Request | clauses/7.5.8.md | 1-209 |
| 7.5.8.1 | General | clauses/7.5.8.md | 3-27 |
| 7.5.8.2 | Downlink Data Report IE within PFCP Session Report Request | clauses/7.5.8.md | 28-44 |
| 7.5.8.3 | Usage Report IE within PFCP Session Report Request | clauses/7.5.8.md | 45-122 |
| 7.5.8.4 | Error Indication Report IE within PFCP Session Report Request | clauses/7.5.8.md | 123-136 |
| 7.5.8.5 | TSC Management Information IE within PFCP Session Report Request | clauses/7.5.8.md | 137-151 |
| 7.5.8.6 | Session Report IE within PFCP Session Report Request | clauses/7.5.8.md | 152-209 |
| 7.5.9 | PFCP Session Report Response | clauses/7.5.9.md | 1-44 |
| 7.5.9.1 | General | clauses/7.5.9.md | 3-24 |
| 7.5.9.2 | Update BAR IE within PFCP Session Report Response | clauses/7.5.9.md | 25-44 |
| 7.6 | Error Handling | clauses/7.6.md | 1-94 |
| 7.6.1 | Protocol Errors | clauses/7.6.md | 3-18 |
| 7.6.2 | Different PFCP Versions | clauses/7.6.md | 19-22 |
| 7.6.3 | PFCP Message of Invalid Length | clauses/7.6.md | 23-30 |
| 7.6.4 | Unknown PFCP Message | clauses/7.6.md | 31-34 |
| 7.6.5 | Unexpected PFCP Message | clauses/7.6.md | 35-40 |
| 7.6.6 | Missing Information Elements | clauses/7.6.md | 41-56 |
| 7.6.7 | Invalid Length Information Element | clauses/7.6.md | 57-68 |
| 7.6.8 | Semantically incorrect Information Element | clauses/7.6.md | 69-82 |
| 7.6.9 | Unknown or unexpected Information Element | clauses/7.6.md | 83-88 |
| 7.6.10 | Repeated Information Elements | clauses/7.6.md | 89-94 |
| 8 | Information Elements | clauses/8.md | 1-1 |
| 8.1 | Information Elements Format | clauses/8.1.md | 1-441 |
| 8.1.1 | Information Element Format | clauses/8.1.md | 3-55 |
| 8.1.2 | Information Element Types | clauses/8.1.md | 56-441 |
| 8.2 | Information Elements | clauses/8.2.md | 1-1 |
| 8.2.1 | Cause | clauses/8.2.1.md | 1-54 |
| 8.2.2 | Source Interface | clauses/8.2.2.md | 1-29 |
| 8.2.3 | F-TEID | clauses/8.2.3.md | 1-42 |
| 8.2.4 | Network Instance | clauses/8.2.4.md | 1-17 |
| 8.2.5 | SDF Filter | clauses/8.2.5.md | 1-67 |
| 8.2.6 | Application ID | clauses/8.2.6.md | 1-15 |
| 8.2.7 | Gate Status | clauses/8.2.7.md | 1-30 |
| 8.2.8 | MBR | clauses/8.2.8.md | 1-19 |
| 8.2.9 | GBR | clauses/8.2.9.md | 1-19 |
| 8.2.10 | QER Correlation ID | clauses/8.2.10.md | 1-18 |
| 8.2.11 | Precedence | clauses/8.2.11.md | 1-16 |
| 8.2.12 | Transport Level Marking | clauses/8.2.12.md | 1-18 |
| 8.2.13 | Volume Threshold | clauses/8.2.13.md | 1-31 |
| 8.2.14 | Time Threshold | clauses/8.2.14.md | 1-16 |
| 8.2.15 | Monitoring Time | clauses/8.2.15.md | 1-18 |
| 8.2.16 | Subsequent Volume Threshold | clauses/8.2.16.md | 1-31 |
| 8.2.17 | Subsequent Time Threshold | clauses/8.2.17.md | 1-16 |
| 8.2.18 | Inactivity Detection Time | clauses/8.2.18.md | 1-16 |
| 8.2.19 | Reporting Triggers | clauses/8.2.19.md | 1-62 |
| 8.2.20 | Redirect Information | clauses/8.2.20.md | 1-48 |
| 8.2.21 | Report Type | clauses/8.2.21.md | 1-34 |
| 8.2.22 | Offending IE | clauses/8.2.22.md | 1-15 |
| 8.2.23 | Forwarding Policy | clauses/8.2.23.md | 1-19 |
| 8.2.24 | Destination Interface | clauses/8.2.24.md | 1-30 |
| 8.2.25 | UP Function Features | clauses/8.2.25.md | 1-104 |
| 8.2.26 | Apply Action | clauses/8.2.26.md | 1-59 |
| 8.2.27 | Downlink Data Service Information | clauses/8.2.27.md | 1-29 |
| 8.2.28 | Downlink Data Notification Delay | clauses/8.2.28.md | 1-16 |
| 8.2.29 | DL Buffering Duration | clauses/8.2.29.md | 1-20 |
| 8.2.30 | DL Buffering Suggested Packet Count | clauses/8.2.30.md | 1-17 |
| 8.2.31 | PFCPSMReq-Flags | clauses/8.2.31.md | 1-34 |
| 8.2.32 | PFCPSRRsp-Flags | clauses/8.2.32.md | 1-20 |
| 8.2.33 | Sequence Number | clauses/8.2.33.md | 1-13 |
| 8.2.34 | Metric | clauses/8.2.34.md | 1-13 |
| 8.2.35 | Timer | clauses/8.2.35.md | 1-20 |
| 8.2.36 | Packet Detection Rule ID (PDR ID) | clauses/8.2.36.md | 1-16 |
| 8.2.37 | F-SEID | clauses/8.2.37.md | 1-29 |
| 8.2.38 | Node ID | clauses/8.2.38.md | 1-34 |
| 8.2.39 | PFD Contents | clauses/8.2.39.md | 1-108 |
| 8.2.40 | Measurement Method | clauses/8.2.40.md | 1-26 |
| 8.2.41 | Usage Report Trigger | clauses/8.2.41.md | 1-70 |
| 8.2.42 | Measurement Period | clauses/8.2.42.md | 1-16 |
| 8.2.43 | Fully qualified PDN Connection Set Identifier (FQ-CSID) | clauses/8.2.43.md | 1-56 |
| 8.2.44 | Volume Measurement | clauses/8.2.44.md | 1-40 |
| 8.2.45 | Duration Measurement | clauses/8.2.45.md | 1-16 |
| 8.2.46 | Time of First Packet | clauses/8.2.46.md | 1-18 |
| 8.2.47 | Time of Last Packet | clauses/8.2.47.md | 1-18 |
| 8.2.48 | Quota Holding Time | clauses/8.2.48.md | 1-16 |
| 8.2.49 | Dropped DL Traffic Threshold | clauses/8.2.49.md | 1-28 |
| 8.2.50 | Volume Quota | clauses/8.2.50.md | 1-31 |
| 8.2.51 | Time Quota | clauses/8.2.51.md | 1-16 |
| 8.2.52 | Start Time | clauses/8.2.52.md | 1-18 |
| 8.2.53 | End Time | clauses/8.2.53.md | 1-18 |
| 8.2.54 | URR ID | clauses/8.2.54.md | 1-18 |
| 8.2.55 | Linked URR ID IE | clauses/8.2.55.md | 1-16 |
| 8.2.56 | Outer Header Creation | clauses/8.2.56.md | 1-54 |
| 8.2.57 | BAR ID | clauses/8.2.57.md | 1-16 |
| 8.2.58 | CP Function Features | clauses/8.2.58.md | 1-36 |
| 8.2.59 | Usage Information | clauses/8.2.59.md | 1-26 |
| 8.2.60 | Application Instance ID | clauses/8.2.60.md | 1-15 |
| 8.2.61 | Flow Information | clauses/8.2.61.md | 1-30 |
| 8.2.62 | UE IP Address | clauses/8.2.62.md | 1-42 |
| 8.2.63 | Packet Rate | clauses/8.2.63.md | 1-60 |
| 8.2.64 | Outer Header Removal | clauses/8.2.64.md | 1-46 |
| 8.2.65 | Recovery Time Stamp | clauses/8.2.65.md | 1-16 |
| 8.2.66 | DL Flow Level Marking | clauses/8.2.66.md | 1-28 |
| 8.2.67 | Header Enrichment | clauses/8.2.67.md | 1-37 |
| 8.2.68 | Measurement Information | clauses/8.2.68.md | 1-34 |
| 8.2.69 | Node Report Type | clauses/8.2.69.md | 1-36 |
| 8.2.70 | Remote GTP-U Peer | clauses/8.2.70.md | 1-45 |
| 8.2.71 | UR-SEQN | clauses/8.2.71.md | 1-15 |
| 8.2.72 | Activate Predefined Rules | clauses/8.2.72.md | 1-15 |
| 8.2.73 | Deactivate Predefined Rules | clauses/8.2.73.md | 1-15 |
| 8.2.74 | FAR ID | clauses/8.2.74.md | 1-18 |
| 8.2.75 | QER ID | clauses/8.2.75.md | 1-18 |
| 8.2.76 | OCI Flags | clauses/8.2.76.md | 1-20 |
| 8.2.77 | PFCP Association Release Request | clauses/8.2.77.md | 1-22 |
| 8.2.78 | Graceful Release Period | clauses/8.2.78.md | 1-20 |
| 8.2.79 | PDN Type | clauses/8.2.79.md | 1-27 |
| 8.2.80 | Failed Rule ID | clauses/8.2.80.md | 1-32 |
| 8.2.81 | Time Quota Mechanism | clauses/8.2.81.md | 1-27 |
| 8.2.82 | Void | clauses/8.2.82.md | 1-2 |
| 8.2.83 | User Plane Inactivity Timer | clauses/8.2.83.md | 1-16 |
| 8.2.84 | Multiplier | clauses/8.2.84.md | 1-16 |
| 8.2.85 | Aggregated URR ID IE | clauses/8.2.85.md | 1-15 |
| 8.2.86 | Subsequent Volume Quota | clauses/8.2.86.md | 1-31 |
| 8.2.87 | Subsequent Time Quota | clauses/8.2.87.md | 1-16 |
| 8.2.88 | RQI | clauses/8.2.88.md | 1-22 |
| 8.2.89 | QFI | clauses/8.2.89.md | 1-16 |
| 8.2.90 | Query URR Reference | clauses/8.2.90.md | 1-16 |
| 8.2.91 | Additional Usage Reports Information | clauses/8.2.91.md | 1-23 |
| 8.2.92 | Traffic Endpoint ID | clauses/8.2.92.md | 1-16 |
| 8.2.93 | MAC address | clauses/8.2.93.md | 1-30 |
| 8.2.94 | C-TAG (Customer-VLAN tag) | clauses/8.2.94.md | 1-34 |
| 8.2.95 | S-TAG (Service-VLAN tag) | clauses/8.2.95.md | 1-34 |
| 8.2.96 | Ethertype | clauses/8.2.96.md | 1-14 |
| 8.2.97 | Proxying | clauses/8.2.97.md | 1-22 |
| 8.2.98 | Ethernet Filter ID | clauses/8.2.98.md | 1-16 |
| 8.2.99 | Ethernet Filter Properties | clauses/8.2.99.md | 1-20 |
| 8.2.100 | Suggested Buffering Packets Count | clauses/8.2.100.md | 1-16 |
| 8.2.101 | User ID | clauses/8.2.101.md | 1-68 |
| 8.2.102 | Ethernet PDU Session Information | clauses/8.2.102.md | 1-20 |
| 8.2.103 | MAC Addresses Detected | clauses/8.2.103.md | 1-34 |
| 8.2.104 | MAC Addresses Removed | clauses/8.2.104.md | 1-34 |
| 8.2.105 | Ethernet Inactivity Timer | clauses/8.2.105.md | 1-16 |
| 8.2.106 | Subsequent Event Quota | clauses/8.2.106.md | 1-16 |
| 8.2.107 | Subsequent Event Threshold | clauses/8.2.107.md | 1-16 |
| 8.2.108 | Trace Information | clauses/8.2.108.md | 1-32 |
| 8.2.109 | Framed-Route | clauses/8.2.109.md | 1-15 |
| 8.2.110 | Framed-Routing | clauses/8.2.110.md | 1-15 |
| 8.2.111 | Framed-IPv6-Route | clauses/8.2.111.md | 1-15 |
| 8.2.112 | Event Quota | clauses/8.2.112.md | 1-16 |
| 8.2.113 | Event Threshold | clauses/8.2.113.md | 1-16 |
| 8.2.114 | Time Stamp | clauses/8.2.114.md | 1-18 |
| 8.2.115 | Averaging Window | clauses/8.2.115.md | 1-16 |
| 8.2.116 | Paging Policy Indicator (PPI) | clauses/8.2.116.md | 1-16 |
| 8.2.117 | APN/DNN | clauses/8.2.117.md | 1-17 |
| 8.2.118 | 3GPP Interface Type | clauses/8.2.118.md | 1-56 |
| 8.2.119 | PFCPSRReq-Flags | clauses/8.2.119.md | 1-20 |
| 8.2.120 | PFCPAUReq-Flags | clauses/8.2.120.md | 1-20 |
| 8.2.121 | Activation Time | clauses/8.2.121.md | 1-18 |
| 8.2.122 | Deactivation Time | clauses/8.2.122.md | 1-18 |
| 8.2.123 | MAR ID | clauses/8.2.123.md | 1-16 |
| 8.2.124 | Steering Functionality | clauses/8.2.124.md | 1-26 |
| 8.2.125 | Steering Mode | clauses/8.2.125.md | 1-28 |
| 8.2.126 | Weight | clauses/8.2.126.md | 1-15 |
| 8.2.127 | Priority | clauses/8.2.127.md | 1-32 |
| 8.2.128 | UE IP address Pool Identity | clauses/8.2.128.md | 1-17 |
| 8.2.129 | Alternative SMF IP Address | clauses/8.2.129.md | 1-28 |
| 8.2.130 | Packet Replication and Detection Carry-On Information | clauses/8.2.130.md | 1-26 |
| 8.2.131 | SMF Set ID | clauses/8.2.131.md | 1-19 |
| 8.2.132 | Quota Validity Time | clauses/8.2.132.md | 1-16 |
| 8.2.133 | Number of Reports | clauses/8.2.133.md | 1-13 |
| 8.2.134 | PFCPASRsp-Flags | clauses/8.2.134.md | 1-22 |
| 8.2.135 | CP PFCP Entity IP Address | clauses/8.2.135.md | 1-26 |
| 8.2.136 | PFCPSEReq-Flags | clauses/8.2.136.md | 1-24 |
| 8.2.137 | IP Multicast Address | clauses/8.2.137.md | 1-40 |
| 8.2.138 | Source IP Address | clauses/8.2.138.md | 1-35 |
| 8.2.139 | Packet Rate Status | clauses/8.2.139.md | 1-45 |
| 8.2.140 | Create Bridge/Router Info IE | clauses/8.2.140.md | 1-22 |
| 8.2.141 | Port Number | clauses/8.2.141.md | 1-19 |
| 8.2.142 | NW-TT Port Number | clauses/8.2.142.md | 1-19 |
| 8.2.143 | 5GS User Plane Node ID | clauses/8.2.143.md | 1-23 |
| 8.2.144 | Port Management Information Container | clauses/8.2.144.md | 1-15 |
| 8.2.145 | Requested Clock Drift Information | clauses/8.2.145.md | 1-24 |
| 8.2.146 | Time Domain Number | clauses/8.2.146.md | 1-16 |
| 8.2.147 | Time Offset Threshold | clauses/8.2.147.md | 1-16 |
| 8.2.148 | Cumulative rateRatio Threshold | clauses/8.2.148.md | 1-16 |
| 8.2.149 | Time Offset Measurement | clauses/8.2.149.md | 1-16 |
| 8.2.150 | Cumulative rateRatio Measurement | clauses/8.2.150.md | 1-16 |
| 8.2.151 | SRR ID | clauses/8.2.151.md | 1-16 |
| 8.2.152 | Requested Access Availability Information | clauses/8.2.152.md | 1-22 |
| 8.2.153 | Access Availability Information | clauses/8.2.153.md | 1-36 |
| 8.2.154 | MPTCP Control Information | clauses/8.2.154.md | 1-20 |
| 8.2.155 | ATSSS-LL Control Information | clauses/8.2.155.md | 1-20 |
| 8.2.156 | PMF Control Information | clauses/8.2.156.md | 1-31 |
| 8.2.157 | MPTCP Address Information | clauses/8.2.157.md | 1-32 |
| 8.2.158 | Link-Specific Multipath IP Address | clauses/8.2.158.md | 1-34 |
| 8.2.159 | PMF Address Information | clauses/8.2.159.md | 1-40 |
| 8.2.160 | ATSSS-LL Information | clauses/8.2.160.md | 1-20 |
| 8.2.161 | Data Network Access Identifier | clauses/8.2.161.md | 1-16 |
| 8.2.162 | Average Packet Delay | clauses/8.2.162.md | 1-17 |
| 8.2.163 | Minimum Packet Delay | clauses/8.2.163.md | 1-17 |
| 8.2.164 | Maximum Packet Delay | clauses/8.2.164.md | 1-17 |
| 8.2.165 | QoS Report Trigger | clauses/8.2.165.md | 1-24 |
| 8.2.166 | GTP-U Path Interface Type | clauses/8.2.166.md | 1-22 |
| 8.2.167 | Requested QoS Monitoring | clauses/8.2.167.md | 1-38 |
| 8.2.168 | Reporting Frequency | clauses/8.2.168.md | 1-28 |
| 8.2.169 | Packet Delay Thresholds | clauses/8.2.169.md | 1-32 |
| 8.2.170 | Minimum Wait Time | clauses/8.2.170.md | 1-17 |
| 8.2.171 | QoS Monitoring Measurement | clauses/8.2.171.md | 1-49 |
| 8.2.172 | MT-EDT Control Information | clauses/8.2.172.md | 1-20 |
| 8.2.173 | DL Data Packets Size | clauses/8.2.173.md | 1-16 |
| 8.2.174 | QER Control Indications | clauses/8.2.174.md | 1-20 |
| 8.2.175 | NF Instance ID | clauses/8.2.175.md | 1-15 |
| 8.2.176 | S-NSSAI | clauses/8.2.176.md | 1-16 |
| 8.2.177 | IP version | clauses/8.2.177.md | 1-24 |
| 8.2.178 | PFCPASReq-Flags | clauses/8.2.178.md | 1-20 |
| 8.2.179 | Data Status | clauses/8.2.179.md | 1-22 |
| 8.2.180 | RDS Configuration Information | clauses/8.2.180.md | 1-20 |
| 8.2.188 | LNS Address | clauses/8.2.188.md | 1-18 |
| 8.2.181 | Multipath Applicable Indication | clauses/8.2.181.md | 1-22 |
| 8.2.182 | User Plane Node Management Information Container | clauses/8.2.182.md | 1-15 |
| 8.2.183 | Number of UE IP Addresses | clauses/8.2.183.md | 1-24 |
| 8.2.184 | Validity Timer | clauses/8.2.184.md | 1-14 |
| 8.2.185 | Offending IE Information | clauses/8.2.185.md | 1-18 |
| 8.2.186 | RAT Type | clauses/8.2.186.md | 1-51 |
| 8.2.187 | L2TP User Authentication | clauses/8.2.187.md | 1-42 |
| 8.2.189 | Tunnel Preference | clauses/8.2.189.md | 1-15 |
| 8.2.190 | Calling Number | clauses/8.2.190.md | 1-15 |
| 8.2.191 | Called Number | clauses/8.2.191.md | 1-15 |
| 8.2.192 | L2TP Session Indications | clauses/8.2.192.md | 1-26 |
| 8.2.193 | DNS Server Address | clauses/8.2.193.md | 1-14 |
| 8.2.194 | NBNS Server Address | clauses/8.2.194.md | 1-14 |
| 8.2.195 | Maximum Receive Unit | clauses/8.2.195.md | 1-15 |
| 8.2.196 | Thresholds | clauses/8.2.196.md | 1-30 |
| 8.2.197 | Steering Mode Indicator | clauses/8.2.197.md | 1-24 |
| 8.2.198 | Group Id | clauses/8.2.198.md | 1-13 |
| 8.2.199 | CP IP Address | clauses/8.2.199.md | 1-25 |
| 8.2.200 | IP Address and Port Number Replacement | clauses/8.2.200.md | 1-48 |
| 8.2.201 | DNS Query/Response Filter | clauses/8.2.201.md | 1-17 |
| 8.2.202 | Event Notification URI | clauses/8.2.202.md | 1-15 |
| 8.2.203 | Notification Correlation ID | clauses/8.2.203.md | 1-15 |
| 8.2.204 | Reporting Flags | clauses/8.2.204.md | 1-20 |
| 8.2.205 | Predefined Rules Name | clauses/8.2.205.md | 1-15 |
| 8.2.206 | MBS Session Identifier | clauses/8.2.206.md | 1-35 |
| 8.2.207 | Multicast Transport Information | clauses/8.2.207.md | 1-35 |
| 8.2.208 | MBSN4mbReq-Flags | clauses/8.2.208.md | 1-24 |
| 8.2.209 | Local Ingress Tunnel | clauses/8.2.209.md | 1-31 |
| 8.2.210 | MBS Unicast Parameters ID | clauses/8.2.210.md | 1-16 |
| 8.2.211 | MBSN4Resp-Flags | clauses/8.2.211.md | 1-26 |
| 8.2.212 | Tunnel Password | clauses/8.2.212.md | 1-17 |
| 8.2.213 | Area Session ID | clauses/8.2.213.md | 1-15 |
| 8.2.214 | DSCP to PPI Mapping Information | clauses/8.2.214.md | 1-22 |
| 8.2.215 | PFCPSDRsp-Flags | clauses/8.2.215.md | 1-20 |
| 8.2.216 | QER Indications | clauses/8.2.216.md | 1-26 |
| 8.2.217 | Vendor-Specific Node Report Type | clauses/8.2.217.md | 1-25 |
| 8.2.218 | Configured Time Domain | clauses/8.2.218.md | 1-20 |
| 8.2.219 | Metadata | clauses/8.2.219.md | 1-82 |
| 8.2.223 | Traffic Parameter Measurement Indication | clauses/8.2.223.md | 1-41 |
| 8.2.225 | MPQUIC Control Information | clauses/8.2.225.md | 1-20 |
| 8.2.226 | MPQUIC Address Information | clauses/8.2.226.md | 1-32 |
| 8.2.227 | Transport Mode | clauses/8.2.227.md | 1-26 |
| 8.2.228 | Void | clauses/8.2.228.md | 1-2 |
| 8.2.229 | Reporting Suggestion Info | clauses/8.2.229.md | 1-28 |
| 8.2.230 | TL-Container | clauses/8.2.230.md | 1-15 |
| 8.2.231 | Measurement Indication | clauses/8.2.231.md | 1-20 |
| 8.2.232 | HPLMN S-NSSAI | clauses/8.2.232.md | 1-16 |
| 8.2.233 | Media Transport Protocol | clauses/8.2.233.md | 1-25 |
| 8.2.234 | RTP Header Extension Type | clauses/8.2.234.md | 1-22 |
| 8.2.235 | RTP Header Extension ID | clauses/8.2.235.md | 1-15 |
| 8.2.236 | RTP Payload Type | clauses/8.2.236.md | 1-15 |
| 8.2.237 | RTP Payload Format | clauses/8.2.237.md | 1-24 |
| 8.2.238 | Extended DL Buffering Notification Policy | clauses/8.2.238.md | 1-20 |
| 8.2.239 | MT-SDT Control Information | clauses/8.2.239.md | 1-20 |
| 8.2.240 | Reporting Thresholds | clauses/8.2.240.md | 1-37 |
| 8.2.241 | RTP Header Extension Additional Information | clauses/8.2.241.md | 1-36 |
| 8.2.242 | Mapped N6 IP Address | clauses/8.2.242.md | 1-25 |
| 8.2.243 | N6 Routing Information | clauses/8.2.243.md | 1-40 |
| 8.2.244 | URI | clauses/8.2.244.md | 1-15 |
| 8.2.245 | UE Level Measurements Configuration | clauses/8.2.245.md | 1-47 |
| 8.2.246 | - 8.2.271 Used by Rel-19 onwards | clauses/8.2.246.md | 1-2 |
| 8.2.272 | Reporting Control Information | clauses/8.2.272.md | 1-22 |
| A.1 | Throttling Aalgorithms | clauses/annex-A.1.md | 1-14 |
| A.1.1 | "Loss" Throttling Algorithm | clauses/annex-A.1.md | 3-14 |
| A.1.1.1 | Example of Possible Implementation | clauses/annex-A.1.md | 5-14 |
| B.1 | CP Selection Function | clauses/annex-B.1.md | 1-18 |
| B.1.1 | General | clauses/annex-B.1.md | 3-18 |
| B.2 | UP Selection Function | clauses/annex-B.2.md | 1-106 |
| B.2.1 | General | clauses/annex-B.2.md | 3-12 |
| B.2.2 | SGW-U Selection Function | clauses/annex-B.2.md | 13-32 |
| B.2.3 | PGW-U Selection Function | clauses/annex-B.2.md | 33-62 |
| B.2.4 | Combined SGW-U/PGW-U Selection Function | clauses/annex-B.2.md | 63-74 |
| B.2.5 | TDF-U selection function | clauses/annex-B.2.md | 75-78 |
| B.2.6 | UP Selection Function Based on DNS | clauses/annex-B.2.md | 79-106 |
| B.2.6.1 | General | clauses/annex-B.2.md | 81-88 |
| B.2.6.2 | SGW-U Selection Function Based on DNS | clauses/annex-B.2.md | 89-94 |
| B.2.6.3 | PGW-U Selection Function Based on DNS | clauses/annex-B.2.md | 95-100 |
| B.2.6.4 | Combined SGW-U/PGW-U Selection Function Based on DNS | clauses/annex-B.2.md | 101-106 |
| C.1 | General | clauses/annex-C.1.md | 1-6 |
| C.2 | Charging Support | clauses/annex-C.2.md | 1-142 |
| C.2.1 | Online Charging | clauses/annex-C.2.md | 3-142 |
| C.2.1.1 | Online Charging Call Flow – Normal Scenario | clauses/annex-C.2.md | 5-46 |
| C.2.1.2 | Online Charging Call Flow with Credit Pooling | clauses/annex-C.2.md | 47-142 |
| C.2.1.2.1 | General | clauses/annex-C.2.md | 49-52 |
| C.2.1.2.2 | Example Call Flow 1 | clauses/annex-C.2.md | 53-96 |
| C.2.1.2.3 | Example Call Flow 2 | clauses/annex-C.2.md | 97-142 |
| D.1 | General | clauses/annex-D.1.md | 1-38 |
| D.2 | Procedures | clauses/annex-D.2.md | 1-330 |
| D.2.1 | Addition of PSA and UL CL/BP controlled by I-SMF | clauses/annex-D.2.md | 3-168 |
| D.2.2 | Removal of PSA and UL CL/BP | clauses/annex-D.2.md | 169-174 |
| D.2.3 | Change of PSA | clauses/annex-D.2.md | 175-180 |
| D.2.4 | Traffic Usage Reporting | clauses/annex-D.2.md | 181-186 |
| D.2.5 | Updating N4 information towards I-SMF | clauses/annex-D.2.md | 187-190 |
| D.2.6 | PDU session release | clauses/annex-D.2.md | 191-206 |
| D.2.7 | Simultaneous change of UL CL/BP and PSA controlled by I-SMF | clauses/annex-D.2.md | 207-286 |
| D.2.8 | Simultaneous change of UL CL/BP and PSA controlled by different I-SMFs | clauses/annex-D.2.md | 287-330 |
| E.1 | General | clauses/annex-E.1.md | 1-6 |
| E.2 | Multipath TCP Connection Setup | clauses/annex-E.2.md | 1-40 |
| E.2.1 | General | clauses/annex-E.2.md | 3-10 |
| E.2.2 | Outgoing Multipath TCP Connection Setup | clauses/annex-E.2.md | 11-20 |
| E.2.3 | Incoming Multipath TCP Connection Setup | clauses/annex-E.2.md | 21-24 |
| E.2.4 | MPTCP Session Entry Stored in MPTCP Proxy | clauses/annex-E.2.md | 25-40 |
| E.3 | IP Translation Procedure | clauses/annex-E.3.md | 1-640 |
| E.3.1 | General | clauses/annex-E.3.md | 3-14 |
| E.3.2 | IP Translation on Uplink IP Packets | clauses/annex-E.3.md | 15-26 |
| E.3.3 | IP Translation on Downlink IP Packets | clauses/annex-E.3.md | 27-640 |
