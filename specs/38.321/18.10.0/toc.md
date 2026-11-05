# TS 38.321 V18.10.0 — NR MAC

Clause index. `File` is relative to this directory; `Lines` is the 1-based
line range of the clause inside that file.

| Clause | Title | File | Lines |
|---|---|---|---|
| front-matter | Title page, foreword and scope front matter | clauses/front-matter.md | 1-672 |
| 1 | Scope | clauses/1.md | 1-5 |
| 2 | References | clauses/2.md | 1-72 |
| 3 | Definitions, symbols and abbreviations | clauses/3.md | 1-276 |
| 3.1 | Definitions | clauses/3.md | 3-94 |
| 3.2 | Abbreviations | clauses/3.md | 95-276 |
| 4 | General | clauses/4.md | 1-208 |
| 4.1 | Introduction | clauses/4.md | 3-6 |
| 4.2 | MAC architecture | clauses/4.md | 7-58 |
| 4.2.1 | General | clauses/4.md | 9-14 |
| 4.2.2 | MAC Entities | clauses/4.md | 15-58 |
| 4.3 | Services | clauses/4.md | 59-80 |
| 4.3.1 | Services provided to upper layers | clauses/4.md | 61-68 |
| 4.3.2 | Services expected from physical layer | clauses/4.md | 69-80 |
| 4.4 | Functions | clauses/4.md | 81-114 |
| 4.5 | Channel structure | clauses/4.md | 115-208 |
| 4.5.1 | General | clauses/4.md | 117-120 |
| 4.5.2 | Transport Channels | clauses/4.md | 121-136 |
| 4.5.3 | Logical Channels | clauses/4.md | 137-159 |
| 4.5.4 | Mapping of Transport Channels to Logical Channels | clauses/4.md | 160-208 |
| 4.5.4.1 | General | clauses/4.md | 162-165 |
| 4.5.4.2 | Uplink mapping | clauses/4.md | 166-178 |
| 4.5.4.3 | Downlink mapping | clauses/4.md | 179-195 |
| 4.5.4.4 | Sidelink mapping | clauses/4.md | 196-208 |
| 5 | MAC procedures | clauses/5.md | 1-1 |
| 5.1 | Random Access procedure | clauses/5.1.md | 1-1740 |
| 5.1.1 | Random Access procedure initialization | clauses/5.1.md | 3-256 |
| 5.1.1a | Initialization of variables specific to Random Access type | clauses/5.1.md | 257-456 |
| 5.1.1b | Selection of the set of Random Access resources for the Random Access procedure | clauses/5.1.md | 457-742 |
| 5.1.1c | Availability of the set of Random Access resources | clauses/5.1.md | 743-778 |
| 5.1.1d | Selection of the set of Random Access resources based on feature prioritization | clauses/5.1.md | 779-802 |
| 5.1.1e | Selection of Msg1 repetition for SI request | clauses/5.1.md | 803-822 |
| 5.1.2 | Random Access Resource selection | clauses/5.1.md | 823-976 |
| 5.1.2a | Random Access Resource selection for 2-step RA type | clauses/5.1.md | 977-1062 |
| 5.1.3 | Random Access Preamble transmission | clauses/5.1.md | 1063-1130 |
| 5.1.3a | MSGA transmission | clauses/5.1.md | 1131-1224 |
| 5.1.4 | Random Access Response reception | clauses/5.1.md | 1225-1396 |
| 5.1.4a | MSGB reception and contention resolution for 2-step RA type | clauses/5.1.md | 1397-1560 |
| 5.1.5 | Contention Resolution | clauses/5.1.md | 1561-1724 |
| 5.1.6 | Completion of the Random Access procedure | clauses/5.1.md | 1725-1740 |
| 5.2 | Maintenance of Uplink Time Alignment | clauses/5.2.md | 1-252 |
| 5.2a | Maintenance of UL Synchronization | clauses/5.2a.md | 1-28 |
| 5.3 | DL-SCH data transfer | clauses/5.3.md | 1-234 |
| 5.3.1 | DL Assignment reception | clauses/5.3.md | 3-112 |
| 5.3.2 | HARQ operation | clauses/5.3.md | 113-226 |
| 5.3.2.1 | HARQ Entity | clauses/5.3.md | 115-136 |
| 5.3.2.2 | HARQ process | clauses/5.3.md | 137-226 |
| 5.3.3 | Disassembly and demultiplexing | clauses/5.3.md | 227-234 |
| 5.4 | UL-SCH data transfer | clauses/5.4.md | 1-1494 |
| 5.4.1 | UL Grant reception | clauses/5.4.md | 3-238 |
| 5.4.2 | HARQ operation | clauses/5.4.md | 239-496 |
| 5.4.2.1 | HARQ Entity | clauses/5.4.md | 241-414 |
| 5.4.2.2 | HARQ process | clauses/5.4.md | 415-496 |
| 5.4.3 | Multiplexing and assembly | clauses/5.4.md | 497-674 |
| 5.4.3.1 | Logical Channel Prioritization | clauses/5.4.md | 499-668 |
| 5.4.3.1.1 | General | clauses/5.4.md | 501-544 |
| 5.4.3.1.2 | Selection of logical channels | clauses/5.4.md | 545-566 |
| 5.4.3.1.3 | Allocation of resources | clauses/5.4.md | 567-668 |
| 5.4.3.2 | Multiplexing of MAC Control Elements and MAC SDUs | clauses/5.4.md | 669-674 |
| 5.4.4 | Scheduling Request | clauses/5.4.md | 675-874 |
| 5.4.5 | Buffer Status Reporting | clauses/5.4.md | 875-1054 |
| 5.4.6 | Power Headroom Reporting | clauses/5.4.md | 1055-1388 |
| 5.4.7 | Pre-emptive Buffer Status Reporting | clauses/5.4.md | 1389-1418 |
| 5.4.8 | Timing Advance Reporting | clauses/5.4.md | 1419-1456 |
| 5.4.9 | Delay status reporting | clauses/5.4.md | 1457-1494 |
| 5.5 | PCH reception | clauses/5.5.md | 1-12 |
| 5.6 | BCH reception | clauses/5.6.md | 1-10 |
| 5.7 | Discontinuous Reception (DRX) | clauses/5.7.md | 1-420 |
| 5.7a | Discontinuous Reception (DRX) for MBS Broadcast | clauses/5.7a.md | 1-34 |
| 5.7b | Discontinuous Reception (DRX) for MBS Multicast | clauses/5.7b.md | 1-196 |
| 5.8 | Transmission and reception without dynamic scheduling | clauses/5.8.md | 1-395 |
| 5.8.1 | Downlink | clauses/5.8.md | 3-30 |
| 5.8.1a | Downlink for Multicast | clauses/5.8.md | 31-58 |
| 5.8.2 | Uplink | clauses/5.8.md | 59-309 |
| 5.8.3 | Sidelink | clauses/5.8.md | 310-395 |
| 5.9 | Activation/Deactivation of SCells | clauses/5.9.md | 1-122 |
| 5.10 | Activation/Deactivation of PDCP duplication | clauses/5.10.md | 1-46 |
| 5.11 | MAC reconfiguration | clauses/5.11.md | 1-14 |
| 5.12 | MAC Reset | clauses/5.12.md | 1-126 |
| 5.12a | Void | clauses/5.12a.md | 1-2 |
| 5.13 | Handling of unknown, unforeseen and erroneous protocol data | clauses/5.13.md | 1-18 |
| 5.14 | Handling of measurement gaps | clauses/5.14.md | 1-20 |
| 5.15 | Bandwidth Part (BWP) operation | clauses/5.15.md | 1-318 |
| 5.15.1 | Downlink and Uplink | clauses/5.15.md | 3-232 |
| 5.15.2 | Sidelink | clauses/5.15.md | 233-318 |
| 5.16 | SUL operation | clauses/5.16.md | 1-14 |
| 5.17 | Beam Failure Detection and Recovery procedure | clauses/5.17.md | 1-186 |
| 5.18 | Handling of MAC CEs | clauses/5.18.md | 1-602 |
| 5.18.1 | General | clauses/5.18.md | 3-84 |
| 5.18.2 | Activation/Deactivation of Semi-persistent CSI-RS/CSI-IM resource set | clauses/5.18.md | 85-94 |
| 5.18.3 | Aperiodic CSI Trigger State Subselection | clauses/5.18.md | 95-104 |
| 5.18.4 | Activation/Deactivation of UE-specific PDSCH TCI state | clauses/5.18.md | 105-118 |
| 5.18.5 | Indication of TCI state for UE-specific PDCCH | clauses/5.18.md | 119-136 |
| 5.18.6 | Activation/Deactivation of Semi-persistent CSI reporting on PUCCH | clauses/5.18.md | 137-146 |
| 5.18.7 | Activation/Deactivation of Semi-persistent SRS and Indication of spatial relation of SP/AP SRS | clauses/5.18.md | 147-164 |
| 5.18.8 | Activation/Deactivation of spatial relation of PUCCH resource | clauses/5.18.md | 165-182 |
| 5.18.9 | Activation/Deactivation of semi-persistent ZP CSI-RS resource set | clauses/5.18.md | 183-192 |
| 5.18.10 | Recommended Bit Rate | clauses/5.18.md | 193-220 |
| 5.18.11 | Void | clauses/5.18.md | 221-222 |
| 5.18.12 | Void | clauses/5.18.md | 223-224 |
| 5.18.13 | Void | clauses/5.18.md | 225-226 |
| 5.18.14 | Update of Pathloss Reference RS of SRS | clauses/5.18.md | 227-236 |
| 5.18.15 | Update of Pathloss Reference RS of PUSCH | clauses/5.18.md | 237-246 |
| 5.18.16 | Indication of spatial relation of SRS resource for a Serving Cell set | clauses/5.18.md | 247-260 |
| 5.18.17 | Activation/Deactivation of Semi-Persistent Positioning SRS | clauses/5.18.md | 261-270 |
| 5.18.18 | Timing offset adjustments for IAB | clauses/5.18.md | 271-282 |
| 5.18.19 | Guard symbols for IAB | clauses/5.18.md | 283-336 |
| 5.18.20 | Positioning Measurement Gap Activation/Deactivation Command | clauses/5.18.md | 337-350 |
| 5.18.21 | PPW Activation/Deactivation Command | clauses/5.18.md | 351-366 |
| 5.18.22 | Update of PUCCH Power Control Set for multiple TRP PUCCH repetition | clauses/5.18.md | 367-376 |
| 5.18.23 | Unified TCI States Activation/Deactivation MAC CE | clauses/5.18.md | 377-386 |
| 5.18.24 | Update of Differential Koffset | clauses/5.18.md | 387-396 |
| 5.18.25 | BFD-RS Indication MAC CE | clauses/5.18.md | 397-406 |
| 5.18.26 | Restricted and recommended beam indication for IAB | clauses/5.18.md | 407-430 |
| 5.18.27 | DL TX power adjustment for IAB | clauses/5.18.md | 431-454 |
| 5.18.28 | UL PSD range adjustment for IAB | clauses/5.18.md | 455-474 |
| 5.18.29 | Timing case indication for IAB | clauses/5.18.md | 475-482 |
| 5.18.30 | Case-6 Timing Request | clauses/5.18.md | 483-502 |
| 5.18.31 | Backhaul Link Beam Indication for NCR | clauses/5.18.md | 503-514 |
| 5.18.32 | Access Link Beam Indication for NCR | clauses/5.18.md | 515-522 |
| 5.18.33 | Enhanced Unified TCI States Activation/Deactivation MAC CE | clauses/5.18.md | 523-532 |
| 5.18.34 | Activation/deactivation of PSI-based SDU discard | clauses/5.18.md | 533-546 |
| 5.18.35 | LTM Cell Switch Command | clauses/5.18.md | 547-582 |
| 5.18.36 | Candidate Cell TCI States Activation/Deactivation | clauses/5.18.md | 583-592 |
| 5.18.37 | Activation/Deactivation of Aggregated Semi-Persistent Positioning SRS | clauses/5.18.md | 593-602 |
| 5.19 | Data inactivity monitoring | clauses/5.19.md | 1-16 |
| 5.20 | Void | clauses/5.20.md | 1-2 |
| 5.21 | LBT operation | clauses/5.21.md | 1-86 |
| 5.21.1 | General | clauses/5.21.md | 3-6 |
| 5.21.2 | LBT failure detection and recovery procedure | clauses/5.21.md | 7-86 |
| 5.22 | SL-SCH Data transfer and SL-PRS transmission | clauses/5.22.md | 1-1 |
| 5.22.1 | SL-SCH Data and SL-PRS transmission | clauses/5.22.1.md | 1-1 |
| 5.22.1.1 | SL Grant reception and SCI transmission | clauses/5.22.1.1.md | 1-745 |
| 5.22.1.2 | TX resource (re-)selection check | clauses/5.22.1.2.md | 1-44 |
| 5.22.1.2a | Re-evaluation and Pre-emption | clauses/5.22.1.2a.md | 1-58 |
| 5.22.1.2b | Re-selection for using a received resource conflict indication | clauses/5.22.1.2b.md | 1-32 |
| 5.22.1.2c | Resource re-selection from SL LBT Failure indication | clauses/5.22.1.2c.md | 1-18 |
| 5.22.1.3 | Sidelink HARQ operation and SL-PRS transmission | clauses/5.22.1.3.md | 1-398 |
| 5.22.1.3.1 | Sidelink HARQ Entity | clauses/5.22.1.3.md | 3-148 |
| 5.22.1.3.1a | Sidelink process not associated with Dedicated SL-PRS resource pool | clauses/5.22.1.3.md | 149-226 |
| 5.22.1.3.2 | PSFCH reception | clauses/5.22.1.3.md | 227-278 |
| 5.22.1.3.3 | HARQ-based Sidelink RLF detection | clauses/5.22.1.3.md | 279-322 |
| 5.22.1.3.4 | Processing of sidelink grant on Dedicated SL-PRS resource pool | clauses/5.22.1.3.md | 323-372 |
| 5.22.1.3.5 | Sidelink process associated with Dedicated SL-PRS resource pool | clauses/5.22.1.3.md | 373-398 |
| 5.22.1.4 | Multiplexing and assembly | clauses/5.22.1.4.md | 1-240 |
| 5.22.1.4.0 | General | clauses/5.22.1.4.md | 3-8 |
| 5.22.1.4.1 | Logical channel prioritization | clauses/5.22.1.4.md | 9-236 |
| 5.22.1.4.1.1 | General | clauses/5.22.1.4.md | 11-46 |
| 5.22.1.4.1.2 | Selection of logical channels and SL-PRS | clauses/5.22.1.4.md | 47-168 |
| 5.22.1.4.1.3 | Allocation of sidelink resources | clauses/5.22.1.4.md | 169-236 |
| 5.22.1.4.2 | Multiplexing of MAC Control Elements and MAC SDUs | clauses/5.22.1.4.md | 237-240 |
| 5.22.1.5 | Scheduling Request | clauses/5.22.1.5.md | 1-22 |
| 5.22.1.6 | Buffer Status Reporting | clauses/5.22.1.6.md | 1-120 |
| 5.22.1.7 | CSI Reporting | clauses/5.22.1.7.md | 1-40 |
| 5.22.1.8 | Void | clauses/5.22.1.8.md | 1-2 |
| 5.22.1.9 | IUC-Request transmission | clauses/5.22.1.9.md | 1-14 |
| 5.22.1.10 | IUC-Information Reporting | clauses/5.22.1.10.md | 1-52 |
| 5.22.1.10.1 | General | clauses/5.22.1.10.md | 3-42 |
| 5.22.1.10.2 | Reception of IUC-Information Reporting | clauses/5.22.1.10.md | 43-52 |
| 5.22.1.11 | TX carrier (re-)selection | clauses/5.22.1.11.md | 1-72 |
| 5.22.1.12 | SL-PRS Resource Request | clauses/5.22.1.12.md | 1-24 |
| 5.22.2 | SL-SCH Data and SL-PRS reception | clauses/5.22.2.md | 1-184 |
| 5.22.2.1 | SCI reception | clauses/5.22.2.md | 3-32 |
| 5.22.2.2 | Sidelink HARQ operation and SL-PRS reception on Shared SL-PRS resource pool | clauses/5.22.2.md | 33-156 |
| 5.22.2.2.1 | Sidelink HARQ Entity | clauses/5.22.2.md | 35-70 |
| 5.22.2.2.2 | Sidelink process | clauses/5.22.2.md | 71-156 |
| 5.22.2.3 | Disassembly and demultiplexing | clauses/5.22.2.md | 157-160 |
| 5.22.2.4 | SL-PRS reception on Dedicated SL-PRS resource pool | clauses/5.22.2.md | 161-184 |
| 5.23 | SL-BCH data transfer | clauses/5.23.md | 1-20 |
| 5.23.1 | SL-BCH data transmission | clauses/5.23.md | 3-10 |
| 5.23.2 | SL-BCH data reception | clauses/5.23.md | 11-20 |
| 5.24 | Handling of PRS Processing Window | clauses/5.24.md | 1-14 |
| 5.25 | Positioning Measurement Gap Activation/Deactivation Request | clauses/5.25.md | 1-26 |
| 5.26 | Positioning SRS transmission in RRCINACTIVE | clauses/5.26.md | 1-46 |
| 5.26.1 | General | clauses/5.26.md | 3-14 |
| 5.26.2 | TA validation for SRS transmission in RRCINACTIVE | clauses/5.26.md | 15-46 |
| 5.27 | Small Data Transmission | clauses/5.27.md | 1-126 |
| 5.27.1 | General | clauses/5.27.md | 3-108 |
| 5.27.2 | TA Validation for CG-SDT | clauses/5.27.md | 109-126 |
| 5.28 | Sidelink Discontinuous Reception (DRX) | clauses/5.28.md | 1-211 |
| 5.28.1 | General | clauses/5.28.md | 3-24 |
| 5.28.2 | Behaviour of UE receiving SL-SCH Data | clauses/5.28.md | 25-181 |
| 5.28.3 | Behaviour of UE transmitting SL-SCH Data | clauses/5.28.md | 182-211 |
| 5.29 | Activation/Deactivation of SCG | clauses/5.29.md | 1-58 |
| 5.30 | Handling of FR2 UL gap | clauses/5.30.md | 1-18 |
| 5.31 | Sidelink LBT operation | clauses/5.31.md | 1-78 |
| 5.31.1 | General | clauses/5.31.md | 3-6 |
| 5.31.2 | Sidelink LBT failure detection and recovery procedure | clauses/5.31.md | 7-78 |
| 5.32 | Void | clauses/5.32.md | 1-2 |
| 5.33 | First PUSCH transmission of RACH-less handover | clauses/5.33.md | 1-26 |
| 5.34 | Cell-Level Energy Saving | clauses/5.34.md | 1-128 |
| 5.34.1 | General | clauses/5.34.md | 3-22 |
| 5.34.2 | Cell Discontinuous Transmission | clauses/5.34.md | 23-78 |
| 5.34.3 | Cell Discontinuous Reception | clauses/5.34.md | 79-128 |
| 6 | Protocol Data Units, formats and parameters | clauses/6.md | 1-1 |
| 6.1 | Protocol Data Units | clauses/6.1.md | 1-1 |
| 6.1.1 | General | clauses/6.1.1.md | 1-12 |
| 6.1.2 | MAC PDU (DL-SCH and UL-SCH except transparent MAC and Random Access Response) | clauses/6.1.2.md | 1-32 |
| 6.1.3 | MAC Control Elements (CEs) | clauses/6.1.3.md | 1-1 |
| 6.1.3.1 | Buffer Status Report MAC CEs | clauses/6.1.3.1.md | 1-211 |
| 6.1.3.2 | C-RNTI MAC CE | clauses/6.1.3.2.md | 1-10 |
| 6.1.3.3 | UE Contention Resolution Identity MAC CE | clauses/6.1.3.3.md | 1-10 |
| 6.1.3.4 | Timing Advance Command MAC CE | clauses/6.1.3.4.md | 1-12 |
| 6.1.3.4a | Absolute Timing Advance Command MAC CE | clauses/6.1.3.4a.md | 1-14 |
| 6.1.3.5 | DRX Command MAC CE | clauses/6.1.3.5.md | 1-6 |
| 6.1.3.6 | Long DRX Command MAC CE | clauses/6.1.3.6.md | 1-6 |
| 6.1.3.7 | Configured Grant Confirmation MAC CE | clauses/6.1.3.7.md | 1-6 |
| 6.1.3.8 | Single Entry PHR MAC CE | clauses/6.1.3.8.md | 1-66 |
| 6.1.3.9 | Multiple Entry PHR MAC CE | clauses/6.1.3.9.md | 1-38 |
| 6.1.3.10 | SCell Activation/Deactivation MAC CEs | clauses/6.1.3.10.md | 1-16 |
| 6.1.3.11 | Duplication Activation/Deactivation MAC CE | clauses/6.1.3.11.md | 1-10 |
| 6.1.3.12 | SP CSI-RS/CSI-IM Resource Set Activation/Deactivation MAC CE | clauses/6.1.3.12.md | 1-22 |
| 6.1.3.13 | Aperiodic CSI Trigger State Subselection MAC CE | clauses/6.1.3.13.md | 1-14 |
| 6.1.3.14 | TCI States Activation/Deactivation for UE-specific PDSCH MAC CE | clauses/6.1.3.14.md | 1-14 |
| 6.1.3.15 | TCI State Indication for UE-specific PDCCH MAC CE | clauses/6.1.3.15.md | 1-12 |
| 6.1.3.16 | SP CSI reporting on PUCCH Activation/Deactivation MAC CE | clauses/6.1.3.16.md | 1-18 |
| 6.1.3.17 | SP SRS Activation/Deactivation MAC CE | clauses/6.1.3.17.md | 1-28 |
| 6.1.3.18 | PUCCH spatial relation Activation/Deactivation MAC CE | clauses/6.1.3.18.md | 1-16 |
| 6.1.3.19 | SP ZP CSI-RS Resource Set Activation/Deactivation MAC CE | clauses/6.1.3.19.md | 1-16 |
| 6.1.3.20 | Recommended bit rate MAC CE | clauses/6.1.3.20.md | 1-54 |
| 6.1.3.21 | Timing Delta MAC CE | clauses/6.1.3.21.md | 1-12 |
| 6.1.3.22 | Guard Symbols MAC CEs | clauses/6.1.3.22.md | 1-25 |
| 6.1.3.23 | BFR MAC CEs | clauses/6.1.3.23.md | 1-38 |
| 6.1.3.24 | Enhanced TCI States Activation/Deactivation for UE-specific PDSCH MAC CE | clauses/6.1.3.24.md | 1-16 |
| 6.1.3.25 | Enhanced PUCCH Spatial Relation Activation/Deactivation MAC CE | clauses/6.1.3.25.md | 1-16 |
| 6.1.3.26 | Enhanced SP/AP SRS Spatial Relation Indication MAC CE | clauses/6.1.3.26.md | 1-28 |
| 6.1.3.27 | SRS Pathloss Reference RS Update MAC CE | clauses/6.1.3.27.md | 1-16 |
| 6.1.3.28 | PUSCH Pathloss Reference RS Update MAC CE | clauses/6.1.3.28.md | 1-20 |
| 6.1.3.29 | Serving Cell Set based SRS Spatial Relation Indication MAC CE | clauses/6.1.3.29.md | 1-24 |
| 6.1.3.30 | LBT failure MAC CEs | clauses/6.1.3.30.md | 1-14 |
| 6.1.3.31 | Multiple Entry Configured Grant Confirmation MAC CE | clauses/6.1.3.31.md | 1-8 |
| 6.1.3.32 | Duplication RLC Activation/Deactivation MAC CE | clauses/6.1.3.32.md | 1-10 |
| 6.1.3.33 | Sidelink Buffer Status Report MAC CEs | clauses/6.1.3.33.md | 1-26 |
| 6.1.3.34 | Sidelink Configured Grant Confirmation MAC CE | clauses/6.1.3.34.md | 1-8 |
| 6.1.3.35 | Sidelink CSI Reporting MAC CE | clauses/6.1.3.35.md | 1-12 |
| 6.1.3.36 | SP Positioning SRS Activation/Deactivation MAC CE | clauses/6.1.3.36.md | 1-62 |
| 6.1.3.37 | Guard Symbols MAC CEs for Case-6 and Case-7 timing modes | clauses/6.1.3.37.md | 1-18 |
| 6.1.3.38 | Case-7 Timing advance offset MAC CE | clauses/6.1.3.38.md | 1-12 |
| 6.1.3.39 | Case-6 Timing Request MAC CE | clauses/6.1.3.39.md | 1-6 |
| 6.1.3.40 | Positioning Measurement Gap Activation/Deactivation Request MAC CE | clauses/6.1.3.40.md | 1-14 |
| 6.1.3.41 | Positioning Measurement Gap Activation/Deactivation Command MAC CE | clauses/6.1.3.41.md | 1-14 |
| 6.1.3.42 | PPW Activation/Deactivation Command MAC CE | clauses/6.1.3.42.md | 1-18 |
| 6.1.3.43 | Enhanced BFR MAC CEs | clauses/6.1.3.43.md | 1-50 |
| 6.1.3.44 | Enhanced TCI States Indication for UE-specific PDCCH MAC CE | clauses/6.1.3.44.md | 1-18 |
| 6.1.3.45 | PUCCH spatial relation Activation/Deactivation for multiple TRP PUCCH repetition MAC CE | clauses/6.1.3.45.md | 1-18 |
| 6.1.3.46 | PUCCH Power Control Set Update for multiple TRP PUCCH repetition MAC CE | clauses/6.1.3.46.md | 1-18 |
| 6.1.3.47 | Unified TCI States Activation/Deactivation MAC CE | clauses/6.1.3.47.md | 1-22 |
| 6.1.3.48 | Enhanced Single Entry PHR MAC CE | clauses/6.1.3.48.md | 1-26 |
| 6.1.3.49 | Enhanced Multiple Entry PHR MAC CE | clauses/6.1.3.49.md | 1-32 |
| 6.1.3.50 | Enhanced Single Entry PHR for multiple TRP MAC CE | clauses/6.1.3.50.md | 1-22 |
| 6.1.3.51 | Enhanced Multiple Entry PHR for multiple TRP MAC CE | clauses/6.1.3.51.md | 1-36 |
| 6.1.3.52 | Sidelink DRX Command MAC CE | clauses/6.1.3.52.md | 1-8 |
| 6.1.3.53 | Sidelink Inter-UE Coordination Information MAC CE | clauses/6.1.3.53.md | 1-24 |
| 6.1.3.54 | Sidelink Inter-UE Coordination Request MAC CE | clauses/6.1.3.54.md | 1-22 |
| 6.1.3.55 | Enhanced SCell Activation/Deactivation MAC CEs | clauses/6.1.3.55.md | 1-16 |
| 6.1.3.56 | Timing Advance Report MAC CE | clauses/6.1.3.56.md | 1-14 |
| 6.1.3.57 | Differential Koffset MAC CE | clauses/6.1.3.57.md | 1-10 |
| 6.1.3.58 | BFD-RS Indication MAC CE | clauses/6.1.3.58.md | 1-18 |
| 6.1.3.59 | SP/AP SRS TCI State Indication MAC CE | clauses/6.1.3.59.md | 1-26 |
| 6.1.3.60 | Serving Cell Set based SRS TCI State Indication MAC CE | clauses/6.1.3.60.md | 1-22 |
| 6.1.3.61 | Child IAB-DU Restricted Beam Indication MAC CE | clauses/6.1.3.61.md | 1-36 |
| 6.1.3.62 | IAB-MT Recommended Beam Indication MAC CE | clauses/6.1.3.62.md | 1-28 |
| 6.1.3.63 | DL TX Power Adjustment and Desired DL TX Power Adjustment MAC CEs | clauses/6.1.3.63.md | 1-32 |
| 6.1.3.64 | Desired IAB-MT PSD range MAC CE | clauses/6.1.3.64.md | 1-28 |
| 6.1.3.65 | Timing Case Indication MAC CE | clauses/6.1.3.65.md | 1-10 |
| 6.1.3.66 | NCR Downlink Backhaul Link Beam Indication MAC CE | clauses/6.1.3.66.md | 1-10 |
| 6.1.3.67 | NCR Uplink Backhaul Link Beam Indication MAC CE | clauses/6.1.3.67.md | 1-10 |
| 6.1.3.68 | NCR Access Link Beam Indication MAC CE | clauses/6.1.3.68.md | 1-16 |
| 6.1.3.69 | SL LBT failure MAC CE | clauses/6.1.3.69.md | 1-10 |
| 6.1.3.70 | Enhanced Unified TCI States Activation/Deactivation MAC CE for Joint TCI States | clauses/6.1.3.70.md | 1-16 |
| 6.1.3.71 | Enhanced Unified TCI States Activation/Deactivation MAC CE for Separate TCI States | clauses/6.1.3.71.md | 1-20 |
| 6.1.3.72 | Delay Status Report MAC CE | clauses/6.1.3.72.md | 1-20 |
| 6.1.3.73 | PSI-Based SDU Discard Activation/Deactivation MAC CE | clauses/6.1.3.73.md | 1-10 |
| 6.1.3.74 | SL-PRS Resource Request MAC CE | clauses/6.1.3.74.md | 1-14 |
| 6.1.3.75 | LTM Cell Switch Command MAC CE | clauses/6.1.3.75.md | 1-32 |
| 6.1.3.76 | Candidate Cell TCI States Activation/Deactivation MAC CE | clauses/6.1.3.76.md | 1-16 |
| 6.1.3.77 | Cross-RRH TCI State Indication for UE-specific PDCCH MAC CE | clauses/6.1.3.77.md | 1-16 |
| 6.1.3.78 | Single Entry PHR with assumed PUSCH MAC CE | clauses/6.1.3.78.md | 1-22 |
| 6.1.3.79 | Multiple Entry PHR with assumed PUSCH MAC CE | clauses/6.1.3.79.md | 1-40 |
| 6.1.3.80 | Enhanced SP CSI reporting on PUCCH Activation/Deactivation MAC CE | clauses/6.1.3.80.md | 1-16 |
| 6.1.3.81 | Enhanced Single Entry PHR for multiple TRP STx2P MAC CE | clauses/6.1.3.81.md | 1-22 |
| 6.1.3.82 | Enhanced Multiple Entry PHR for multiple TRP STx2P MAC CE | clauses/6.1.3.82.md | 1-36 |
| 6.1.3.83 | Aggregated SP Positioning SRS Activation/Deactivation MAC CE | clauses/6.1.3.83.md | 1-18 |
| 6.1.4 | MAC PDU (transparent MAC) | clauses/6.1.4.md | 1-6 |
| 6.1.5 | MAC PDU (Random Access Response) | clauses/6.1.5.md | 1-22 |
| 6.1.5a | MAC PDU (MSGB) | clauses/6.1.5a.md | 1-32 |
| 6.1.6 | MAC PDU (SL-SCH) | clauses/6.1.6.md | 1-28 |
| 6.2 | Formats and parameters | clauses/6.2.md | 1-350 |
| 6.2.1 | MAC subheader for DL-SCH and UL-SCH | clauses/6.2.md | 3-210 |
| 6.2.2 | MAC subheader for Random Access Response | clauses/6.2.md | 211-226 |
| 6.2.2a | MAC subheader for MSGB | clauses/6.2.md | 227-246 |
| 6.2.3 | MAC payload for Random Access Response | clauses/6.2.md | 247-264 |
| 6.2.3a | MAC payload for MSGB | clauses/6.2.md | 265-304 |
| 6.2.4 | MAC subheader for SL-SCH | clauses/6.2.md | 305-350 |
| 7 | Variables and constants | clauses/7.md | 1-147 |
| 7.1 | RNTI values | clauses/7.md | 3-67 |
| 7.2 | Backoff Parameter values | clauses/7.md | 68-92 |
| 7.3 | DELTAPREAMBLE values | clauses/7.md | 93-123 |
| 7.4 | PRACH Mask Index values | clauses/7.md | 124-147 |
| Annex A | (informative): | clauses/annex-A.md | 1-547 |
