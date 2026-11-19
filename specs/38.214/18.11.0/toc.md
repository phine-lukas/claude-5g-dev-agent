# TS 38.214 V18.11.0 — NR physical layer procedures for data

Clause index. `File` is relative to this directory; `Lines` is the 1-based
line range of the clause inside that file.

| Clause | Title | File | Lines |
|---|---|---|---|
| front-matter | Title page, foreword and scope front matter | clauses/front-matter.md | 1-452 |
| 1 | Scope | clauses/1.md | 1-4 |
| 2 | References | clauses/2.md | 1-48 |
| 3 | Definitions of terms, symbols and abbreviations | clauses/3.md | 1-140 |
| 3.1 | Terms | clauses/3.md | 3-6 |
| 3.2 | Symbols | clauses/3.md | 7-10 |
| 3.3 | Abbreviations | clauses/3.md | 11-140 |
| 4 | Power control | clauses/4.md | 1-55 |
| 4.1 | Power allocation for downlink | clauses/4.md | 5-55 |
| 5 | Physical downlink shared channel related procedures | clauses/5.md | 1-1 |
| 5.1 | UE procedure for receiving the physical downlink shared channel | clauses/5.1.md | 1-139 |
| 5.1.1 | Transmission schemes | clauses/5.1.1.md | 1-8 |
| 5.1.1.1 | Transmission scheme 1 | clauses/5.1.1.md | 5-8 |
| 5.1.2 | Resource allocation | clauses/5.1.2.md | 1-440 |
| 5.1.2.1 | Resource allocation in time domain | clauses/5.1.2.md | 3-285 |
| 5.1.2.1.1 | Determination of the resource allocation table to be used for PDSCH | clauses/5.1.2.md | 121-285 |
| 5.1.2.2 | Resource allocation in frequency domain | clauses/5.1.2.md | 286-394 |
| 5.1.2.2.1 | Downlink resource allocation type 0 | clauses/5.1.2.md | 296-320 |
| 5.1.2.2.2 | Downlink resource allocation type 1 | clauses/5.1.2.md | 321-368 |
| 5.1.2.2.3 | Downlink resource allocation type 1 for multicast/broadcast | clauses/5.1.2.md | 369-394 |
| 5.1.2.3 | Physical resource block (PRB) bundling | clauses/5.1.2.md | 395-440 |
| 5.1.3 | Modulation order, target code rate, redundancy version and transport block size determination | clauses/5.1.3.md | 1-498 |
| 5.1.3.1 | Modulation order and target code rate determination | clauses/5.1.3.md | 103-368 |
| 5.1.3.2 | Transport block size determination | clauses/5.1.3.md | 369-498 |
| 5.1.4 | PDSCH resource mapping | clauses/5.1.4.md | 1-96 |
| 5.1.4.1 | PDSCH resource mapping with RB symbol level granularity | clauses/5.1.4.md | 15-40 |
| 5.1.4.2 | PDSCH resource mapping with RE level granularity | clauses/5.1.4.md | 41-96 |
| 5.1.5 | Antenna ports quasi co-location | clauses/5.1.5.md | 1-240 |
| 5.1.6 | UE procedure for receiving reference signals | clauses/5.1.6.md | 1-580 |
| 5.1.6.1 | CSI-RS reception procedure | clauses/5.1.6.md | 3-142 |
| 5.1.6.1.1 | CSI-RS for tracking | clauses/5.1.6.md | 21-110 |
| 5.1.6.1.1.1 | Aperiodic CSI-RS for tracking for fast SCell activation | clauses/5.1.6.md | 105-110 |
| 5.1.6.1.2 | CSI-RS for L1-RSRP and L1-SINR computation | clauses/5.1.6.md | 111-116 |
| 5.1.6.1.3 | CSI-RS for mobility | clauses/5.1.6.md | 117-142 |
| 5.1.6.2 | DM-RS reception procedure | clauses/5.1.6.md | 143-268 |
| 5.1.6.3 | PT-RS reception procedure | clauses/5.1.6.md | 269-337 |
| 5.1.6.4 | SRS reception procedure for CLI | clauses/5.1.6.md | 338-341 |
| 5.1.6.5 | PRS reception procedure | clauses/5.1.6.md | 342-580 |
| 5.1.6.5.1 | PRS receiver frequency hopping | clauses/5.1.6.md | 541-544 |
| 5.1.6.5.2 | PRS for carrier phase positioning | clauses/5.1.6.md | 545-562 |
| 5.1.6.5.3 | PRS bandwidth aggregation for positioning measurements | clauses/5.1.6.md | 563-580 |
| 5.1.7 | Code block group based PDSCH transmission | clauses/5.1.7.md | 1-32 |
| 5.1.7.1 | UE procedure for grouping of code blocks to code block groups | clauses/5.1.7.md | 5-16 |
| 5.1.7.2 | UE procedure for receiving code block group based transmissions | clauses/5.1.7.md | 17-32 |
| 5.2 | UE procedure for reporting channel state information (CSI) | clauses/5.2.md | 1-1 |
| 5.2.1 | Channel state information framework | clauses/5.2.1.md | 1-747 |
| 5.2.1.1 | Reporting settings | clauses/5.2.1.md | 9-18 |
| 5.2.1.2 | Resource settings | clauses/5.2.1.md | 19-48 |
| 5.2.1.3 | (void) | clauses/5.2.1.md | 49-50 |
| 5.2.1.4 | Reporting configurations | clauses/5.2.1.md | 51-462 |
| 5.2.1.4.1 | Resource Setting configuration | clauses/5.2.1.md | 147-196 |
| 5.2.1.4.2 | Report quantity configurations | clauses/5.2.1.md | 197-368 |
| 5.2.1.4.3 | L1-RSRP Reporting | clauses/5.2.1.md | 369-388 |
| 5.2.1.4.4 | L1-SINR Reporting | clauses/5.2.1.md | 389-408 |
| 5.2.1.4.5 | TDCP Reporting | clauses/5.2.1.md | 409-462 |
| 5.2.1.5 | Triggering/activation of CSI Reports and CSI-RS | clauses/5.2.1.md | 463-685 |
| 5.2.1.5.1 | Aperiodic CSI Reporting/Aperiodic CSI-RS when the triggering PDCCH and the CSI-RS have the same numerology | clauses/5.2.1.md | 465-566 |
| 5.2.1.5.1a | Aperiodic CSI Reporting/Aperiodic CSI-RS when the triggering PDCCH and the CSI-RS have different numerologies | clauses/5.2.1.md | 567-633 |
| 5.2.1.5.2 | Semi-persistent CSI/Semi-persistent CSI-RS | clauses/5.2.1.md | 634-675 |
| 5.2.1.5.3 | Aperiodic CSI-RS for tracking for fast SCell activation | clauses/5.2.1.md | 676-685 |
| 5.2.1.6 | CSI processing criteria | clauses/5.2.1.md | 686-747 |
| 5.2.2 | Channel state information | clauses/5.2.2.md | 1-1 |
| 5.2.2.1 | Channel quality indicator (CQI) | clauses/5.2.2.1.md | 1-135 |
| 5.2.2.1.1 | (void) | clauses/5.2.2.1.md | 134-135 |
| 5.2.2.2 | Precoding matrix indicator (PMI) | clauses/5.2.2.2.md | 1-1 |
| 5.2.2.2.1 | Type I Single-Panel Codebook | clauses/5.2.2.2.1.md | 1-206 |
| 5.2.2.2.2 | Type I Multi-Panel Codebook | clauses/5.2.2.2.2.md | 1-125 |
| 5.2.2.2.3 | Type II Codebook | clauses/5.2.2.2.3.md | 1-230 |
| 5.2.2.2.4 | Type II Port Selection Codebook | clauses/5.2.2.2.4.md | 1-77 |
| 5.2.2.2.5 | Enhanced Type II Codebook | clauses/5.2.2.2.5.md | 1-401 |
| 5.2.2.2.6 | Enhanced Type II Port Selection Codebook | clauses/5.2.2.2.6.md | 1-128 |
| 5.2.2.2.7 | Further enhanced Type II port selection codebook | clauses/5.2.2.2.7.md | 1-255 |
| 5.2.2.2.8 | Enhanced Type II codebook for CJT | clauses/5.2.2.2.8.md | 1-322 |
| 5.2.2.2.9 | Further enhanced Type II port selection codebook for CJT | clauses/5.2.2.2.9.md | 1-309 |
| 5.2.2.2.10 | Enhanced Type II codebook for predicted PMI | clauses/5.2.2.2.10.md | 1-242 |
| 5.2.2.2.11 | Further enhanced Type II port selection codebook for predicted PMI | clauses/5.2.2.2.11.md | 1-18 |
| 5.2.2.3 | Reference signal (CSI-RS) | clauses/5.2.2.3.md | 1-44 |
| 5.2.2.3.1 | NZP CSI-RS | clauses/5.2.2.3.md | 3-44 |
| 5.2.2.4 | Channel State Information – Interference Measurement (CSI-IM) | clauses/5.2.2.4.md | 1-24 |
| 5.2.2.5 | CSI reference resource definition | clauses/5.2.2.5.md | 1-169 |
| 5.2.2.5.1 | UE assumptions for CQI/PMI/RI calculation | clauses/5.2.2.5.md | 45-112 |
| 5.2.2.5.1a | UE assumptions for CQI/PMI/RI calculation for NCJT | clauses/5.2.2.5.md | 113-132 |
| 5.2.2.5.1b | UE assumptions for CQI/PMI/RI calculation for CJT | clauses/5.2.2.5.md | 133-165 |
| 5.2.2.5.1c | UE assumptions for CQI/PMI/RI calculation for predicted CSI | clauses/5.2.2.5.md | 166-169 |
| 5.2.3 | CSI reporting using PUSCH | clauses/5.2.3.md | 1-147 |
| 5.2.4 | CSI reporting using PUCCH | clauses/5.2.4.md | 1-18 |
| 5.2.5 | Priority rules for CSI reports | clauses/5.2.5.md | 1-34 |
| 5.3 | UE PDSCH processing procedure time | clauses/5.3.md | 1-106 |
| 5.3.1 | Application delay of the minimum scheduling offset restriction | clauses/5.3.md | 88-106 |
| 5.4 | UE CSI computation time | clauses/5.4.md | 1-74 |
| 5.5 | UE PDSCH reception preparation time with different subcarrier spacings for PDCCH and PDSCH in different cells | clauses/5.5.md | 1-21 |
| 6 | Physical uplink shared channel related procedure | clauses/6.md | 1-1 |
| 6.1 | UE procedure for transmitting the physical uplink shared channel | clauses/6.1.md | 1-71 |
| 6.1.1 | Transmission schemes | clauses/6.1.1.md | 1-124 |
| 6.1.1.1 | Codebook based UL transmission | clauses/6.1.1.md | 5-82 |
| 6.1.1.2 | Non-Codebook based UL transmission | clauses/6.1.1.md | 83-124 |
| 6.1.2 | Resource allocation | clauses/6.1.2.md | 1-737 |
| 6.1.2.1 | Resource allocation in time domain | clauses/6.1.2.md | 3-451 |
| 6.1.2.1.1 | Determination of the resource allocation table to be used for PUSCH | clauses/6.1.2.md | 339-451 |
| 6.1.2.2 | Resource allocation in frequency domain | clauses/6.1.2.md | 452-579 |
| 6.1.2.2.1 | Uplink resource allocation type 0 | clauses/6.1.2.md | 464-490 |
| 6.1.2.2.2 | Uplink resource allocation type 1 | clauses/6.1.2.md | 491-534 |
| 6.1.2.2.3 | Uplink resource allocation type 2 | clauses/6.1.2.md | 535-579 |
| 6.1.2.3 | Resource allocation for uplink transmission with configured grant | clauses/6.1.2.md | 580-737 |
| 6.1.2.3.1 | Transport Block repetition for uplink transmissions of PUSCH repetition Type A with a configured grant | clauses/6.1.2.md | 644-687 |
| 6.1.2.3.2 | Transport Block repetition for uplink transmissions of PUSCH repetition Type B with a configured grant | clauses/6.1.2.md | 688-711 |
| 6.1.2.3.3 | Transport Block repetition for uplink transmissions of TB processing over multiple slots with a configured grant | clauses/6.1.2.md | 712-737 |
| 6.1.3 | UE procedure for applying transform precoding on PUSCH | clauses/6.1.3.md | 1-34 |
| 6.1.4 | Modulation order, redundancy version and transport block size determination | clauses/6.1.4.md | 1-356 |
| 6.1.4.1 | Modulation order and target code rate determination | clauses/6.1.4.md | 63-292 |
| 6.1.4.2 | Transport block size determination | clauses/6.1.4.md | 293-356 |
| 6.1.5 | Code block group based PUSCH transmission | clauses/6.1.5.md | 1-28 |
| 6.1.5.1 | UE procedure for grouping of code blocks to code block groups | clauses/6.1.5.md | 5-16 |
| 6.1.5.2 | UE procedure for transmitting code block group based transmissions | clauses/6.1.5.md | 17-28 |
| 6.1.6 | Uplink switching | clauses/6.1.6.md | 1-132 |
| 6.1.6.1 | Uplink switching for EN-DC | clauses/6.1.6.md | 41-68 |
| 6.1.6.2 | Uplink switching for carrier aggregation | clauses/6.1.6.md | 69-122 |
| 6.1.6.2.0 | Uplink switching with two uplink bands | clauses/6.1.6.md | 71-94 |
| 6.1.6.2.1 | void | clauses/6.1.6.md | 95-96 |
| 6.1.6.2.2 | Uplink switching with 3 or 4 uplink bands | clauses/6.1.6.md | 97-122 |
| 6.1.6.3 | Uplink switching with two uplink bands for supplementary uplink | clauses/6.1.6.md | 123-132 |
| 6.1.7 | UE procedure for determining time domain windows for bundling DM-RS | clauses/6.1.7.md | 1-100 |
| 6.2 | UE reference signal (RS) procedure | clauses/6.2.md | 1-683 |
| 6.2.1 | UE sounding procedure | clauses/6.2.md | 3-462 |
| 6.2.1.1 | UE SRS frequency hopping procedure | clauses/6.2.md | 179-188 |
| 6.2.1.2 | UE sounding procedure for DL CSI acquisition | clauses/6.2.md | 189-284 |
| 6.2.1.3 | UE sounding procedure between component carriers | clauses/6.2.md | 285-350 |
| 6.2.1.4 | UE sounding procedure for positioning purposes | clauses/6.2.md | 351-462 |
| 6.2.1.4.1 | SRS frequency hopping for positioning | clauses/6.2.md | 393-436 |
| 6.2.1.4.2 | SRS bandwidth aggregation for positioning measurements | clauses/6.2.md | 437-462 |
| 6.2.2 | UE DM-RS transmission procedure | clauses/6.2.md | 463-530 |
| 6.2.3 | UE PT-RS transmission procedure | clauses/6.2.md | 531-683 |
| 6.2.3.1 | UE PT-RS transmission procedure when transform precoding is not enabled | clauses/6.2.md | 535-650 |
| 6.2.3.2 | UE PT-RS transmission procedure when transform precoding is enabled | clauses/6.2.md | 651-683 |
| 6.3 | UE PUSCH frequency hopping procedure | clauses/6.3.md | 1-75 |
| 6.3.1 | Frequency hopping for PUSCH repetition Type A and for TB processing over multiple slots | clauses/6.3.md | 3-47 |
| 6.3.2 | Frequency hopping for PUSCH repetition Type B | clauses/6.3.md | 48-75 |
| 6.4 | UE PUSCH preparation procedure time | clauses/6.4.md | 1-49 |
| 7 | UE procedures for transmitting and receiving on a carrier with intra-cell guard bands | clauses/7.md | 1-22 |
| 8 | Physical sidelink shared channel related procedures | clauses/8.md | 1-1226 |
| 8.1 | UE procedure for transmitting the physical sidelink shared channel | clauses/8.md | 57-794 |
| 8.1.1 | Transmission schemes | clauses/8.md | 181-186 |
| 8.1.2 | Resource allocation | clauses/8.md | 187-260 |
| 8.1.2.1 | Resource allocation in time domain | clauses/8.md | 193-238 |
| 8.1.2.2 | Resource allocation in frequency domain | clauses/8.md | 239-260 |
| 8.1.3 | Modulation order, target code rate, redundancy version and transport block size determination | clauses/8.md | 261-334 |
| 8.1.3.1 | Modulation order and target code rate determination | clauses/8.md | 265-290 |
| 8.1.3.2 | Transport block size determination | clauses/8.md | 291-334 |
| 8.1.4 | UE procedure for determining the subset of resources to be reported to higher layers in PSSCH resource selection in sidelink resource allocation mode 2 | clauses/8.md | 335-582 |
| 8.1.4A | UE procedure for determining a set of preferred or non-preferred resources for another UE's transmission | clauses/8.md | 583-628 |
| 8.1.4B | Void | clauses/8.md | 629-630 |
| 8.1.4C | UE procedure for using a received non-preferred resource set | clauses/8.md | 631-642 |
| 8.1.5 | UE procedure for determining slots and resource blocks for PSSCH transmission associated with an SCI format 1-A | clauses/8.md | 643-726 |
| 8.1.5A | UE procedure for determining slots and resource blocks indicated by a preferred or non-preferred resource set | clauses/8.md | 727-756 |
| 8.1.6 | Sidelink congestion control in sidelink resource allocation mode 2 | clauses/8.md | 757-786 |
| 8.1.7 | UE procedure for determining the number of logical slots for a reservation period | clauses/8.md | 787-794 |
| 8.2 | UE procedure for transmitting sidelink reference signals | clauses/8.md | 795-1017 |
| 8.2.1 | CSI-RS transmission procedure | clauses/8.md | 797-814 |
| 8.2.2 | PSSCH DM-RS transmission procedure | clauses/8.md | 815-822 |
| 8.2.3 | PT-RS transmission procedure | clauses/8.md | 823-834 |
| 8.2.4 | SL PRS transmission procedure | clauses/8.md | 835-1017 |
| 8.2.4.1 | Resource allocation | clauses/8.md | 851-910 |
| 8.2.4.1.1 | Resource allocation in time domain | clauses/8.md | 865-904 |
| 8.2.4.1.2 | Resource allocation in frequency domain | clauses/8.md | 905-910 |
| 8.2.4.2 | UE procedure for determining the subset of resources to be reported to higher layers in SL PRS resource selection in a dedicated SL PRS resource pool in sidelink resource allocation mode 2 | clauses/8.md | 911-962 |
| 8.2.4.2A | UE procedure for determining slots and SL PRS resource(s) associated with an SCI format 1-B in a dedicated SL PRS resource pool | clauses/8.md | 963-998 |
| 8.2.4.3 | Sidelink congestion control in a dedicated SL PRS resource pool in sidelink resource allocation mode 2 | clauses/8.md | 999-1017 |
| 8.3 | UE procedure for receiving the physical sidelink shared channel | clauses/8.md | 1018-1027 |
| 8.4 | UE procedure for receiving reference signals | clauses/8.md | 1028-1085 |
| 8.4.1 | CSI-RS reception procedure | clauses/8.md | 1030-1033 |
| 8.4.2 | DM-RS reception procedure for RSRP computation | clauses/8.md | 1034-1043 |
| 8.4.3 | PT-RS reception procedure | clauses/8.md | 1044-1053 |
| 8.4.4 | SL PRS reception procedure | clauses/8.md | 1054-1085 |
| 8.5 | UE procedure for reporting channel state information (CSI) | clauses/8.md | 1086-1201 |
| 8.5.1 | Channel state information framework | clauses/8.md | 1088-1115 |
| 8.5.1.1 | Reporting configurations | clauses/8.md | 1092-1107 |
| 8.5.1.2 | Triggering of sidelink CSI reports | clauses/8.md | 1108-1115 |
| 8.5.2 | Channel state information | clauses/8.md | 1116-1197 |
| 8.5.2.1 | CSI reporting quantities | clauses/8.md | 1118-1145 |
| 8.5.2.1.1 | Channel quality indicator (CQI) | clauses/8.md | 1120-1145 |
| 8.5.2.2 | Reference signal (CSI-RS) | clauses/8.md | 1146-1155 |
| 8.5.2.3 | CSI reference resource definition | clauses/8.md | 1156-1197 |
| 8.5.3 | CSI reporting | clauses/8.md | 1198-1201 |
| 8.6 | UE PSSCH preparation procedure time | clauses/8.md | 1202-1226 |
| 9 | UE procedures for transmitting and receiving for RTT-based propagation delay compensation | clauses/9.md | 1-619 |
| 9.1 | PRS reception procedure for RTT-based propagation delay compensation | clauses/9.md | 17-619 |
