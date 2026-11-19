# TS 38.213 V18.9.0 — NR physical layer procedures for control

Clause index. `File` is relative to this directory; `Lines` is the 1-based
line range of the clause inside that file.

| Clause | Title | File | Lines |
|---|---|---|---|
| front-matter | Title page, foreword and scope front matter | clauses/front-matter.md | 1-337 |
| 1 | Scope | clauses/1.md | 1-4 |
| 2 | References | clauses/2.md | 1-52 |
| 3 | Definitions of terms, symbols and abbreviations | clauses/3.md | 1-190 |
| 3.1 | Terms | clauses/3.md | 3-6 |
| 3.2 | Symbols | clauses/3.md | 7-10 |
| 3.3 | Abbreviations | clauses/3.md | 11-190 |
| 4 | Synchronization procedures | clauses/4.md | 1-152 |
| 4.1 | Cell search | clauses/4.md | 3-98 |
| 4.2 | Transmission timing adjustments | clauses/4.md | 99-136 |
| 4.3 | Timing for secondary cell activation / deactivation | clauses/4.md | 137-152 |
| 5 | Radio link monitoring | clauses/5.md | 1-42 |
| 6 | Link recovery procedures | clauses/6.md | 1-172 |
| 7 | Uplink Power control | clauses/7.md | 1-31 |
| 7.1 | Physical uplink shared channel | clauses/7.1.md | 1-429 |
| 7.1.1 | UE behaviour | clauses/7.1.md | 21-429 |
| 7.2 | Physical uplink control channel | clauses/7.2.md | 1-199 |
| 7.2.1 | UE behaviour | clauses/7.2.md | 17-199 |
| 7.3 | Sounding reference signals | clauses/7.3.md | 1-124 |
| 7.3.1 | UE behaviour | clauses/7.3.md | 9-124 |
| 7.4 | Physical random access channel | clauses/7.4.md | 1-50 |
| 7.5 | Prioritizations for transmission power reductions | clauses/7.5.md | 1-32 |
| 7.6 | Dual connectivity | clauses/7.6.md | 1-120 |
| 7.6.1 | EN-DC | clauses/7.6.md | 3-28 |
| 7.6.1A | NE-DC | clauses/7.6.md | 29-60 |
| 7.6.2 | NR-DC | clauses/7.6.md | 61-120 |
| 7.7 | Power headroom report | clauses/7.7.md | 1-196 |
| 7.7.1 | Type 1 PH report | clauses/7.7.md | 39-176 |
| 7.7.2 | Type 2 PH report | clauses/7.7.md | 177-180 |
| 7.7.3 | Type 3 PH report | clauses/7.7.md | 181-196 |
| 8 | Random access procedure | clauses/8.md | 1-412 |
| 8.1 | Random access preamble | clauses/8.md | 21-177 |
| 8.1A | PUSCH for Type-2 random access procedure | clauses/8.md | 178-251 |
| 8.2 | Random access response - Type-1 random access procedure | clauses/8.md | 252-307 |
| 8.2A | Random access response - Type-2 random access procedure | clauses/8.md | 308-341 |
| 8.3 | PUSCH scheduled by RAR UL grant | clauses/8.md | 342-406 |
| 8.4 | PDSCH with UE contention resolution identity | clauses/8.md | 407-412 |
| 9 | UE procedure for reporting control information | clauses/9.md | 1-369 |
| 9.1 | HARQ-ACK codebook determination | clauses/9.1.md | 1-39 |
| 9.1.1 | CBG-based HARQ-ACK codebook determination | clauses/9.1.1.md | 1-14 |
| 9.1.2 | Type-1 HARQ-ACK codebook determination | clauses/9.1.2.md | 1-714 |
| 9.1.2.1 | Type-1 HARQ-ACK codebook in physical uplink control channel | clauses/9.1.2.md | 99-652 |
| 9.1.2.2 | Type-1 HARQ-ACK codebook in physical uplink shared channel | clauses/9.1.2.md | 653-714 |
| 9.1.3 | Type-2 HARQ-ACK codebook determination | clauses/9.1.3.md | 1-808 |
| 9.1.3.1 | Type-2 HARQ-ACK codebook in physical uplink control channel | clauses/9.1.3.md | 27-674 |
| 9.1.3.2 | Type-2 HARQ-ACK codebook in physical uplink shared channel | clauses/9.1.3.md | 675-710 |
| 9.1.3.3 | Type-2 HARQ-ACK codebook grouping and HARQ-ACK retransmission | clauses/9.1.3.md | 711-808 |
| 9.1.4 | Type-3 HARQ-ACK codebook determination | clauses/9.1.4.md | 1-196 |
| 9.1.5 | HARQ-ACK codebook retransmission | clauses/9.1.5.md | 1-48 |
| 9.2 | UCI reporting in physical uplink control channel | clauses/9.2.md | 1-922 |
| 9.2.1 | PUCCH Resource Sets | clauses/9.2.md | 11-147 |
| 9.2.2 | PUCCH Formats for UCI transmission | clauses/9.2.md | 148-237 |
| 9.2.3 | UE procedure for reporting HARQ-ACK | clauses/9.2.md | 238-339 |
| 9.2.4 | UE procedure for reporting SR | clauses/9.2.md | 340-361 |
| 9.2.5 | UE procedure for reporting multiple UCI types | clauses/9.2.md | 362-832 |
| 9.2.5.0 | UE procedure for prioritization between SL HARQ-ACK information in a PUCCH and DL HARQ-ACK or SR or CSI in a PUCCH | clauses/9.2.md | 566-587 |
| 9.2.5.1 | UE procedure for multiplexing HARQ-ACK or CSI and SR in a PUCCH | clauses/9.2.md | 588-621 |
| 9.2.5.2 | UE procedure for multiplexing HARQ-ACK/SR/CSI in a PUCCH | clauses/9.2.md | 622-742 |
| 9.2.5.3 | UE procedure for reporting UCI of different priorities | clauses/9.2.md | 743-794 |
| 9.2.5.4 | UE procedure for deferring HARQ-ACK for SPS PDSCH | clauses/9.2.md | 795-832 |
| 9.2.6 | PUCCH repetition procedure | clauses/9.2.md | 833-922 |
| 9.3 | UCI reporting in physical uplink shared channel | clauses/9.3.md | 1-123 |
| 9.3.1 | UE procedure for reporting UTO-UCI | clauses/9.3.md | 120-123 |
| 10 | UE procedure for receiving control information | clauses/10.md | 1-485 |
| 10.1 | UE procedure for determining physical downlink control channel assignment | clauses/10.1.md | 1-799 |
| 10.1.1 | Self-carrier and cross-carrier scheduling on the primary cell | clauses/10.1.md | 778-799 |
| 10.2 | PDCCH validation for DL SPS and UL grant Type 2 | clauses/10.2.md | 1-66 |
| 10.2A | PDCCH validation for SL configured grant Type 2 | clauses/10.2A.md | 1-33 |
| 10.3 | PDCCH monitoring indication and dormancy/non-dormancy behaviour for SCells | clauses/10.3.md | 1-134 |
| 10.4 | Search space set group switching and skipping of PDCCH monitoring | clauses/10.4.md | 1-186 |
| 10.4A | PDCCH monitoring for early indication of paging | clauses/10.4A.md | 1-20 |
| 10.4B | Indication of TRS resources | clauses/10.4B.md | 1-8 |
| 10.5 | HARQ-ACK information for PUSCH transmissions | clauses/10.5.md | 1-20 |
| 11 | UE-group common signalling | clauses/11.md | 1-597 |
| 11.1 | Slot configuration | clauses/11.md | 19-424 |
| 11.1.1 | UE procedure for determining slot format | clauses/11.md | 217-424 |
| 11.2 | Interrupted transmission indication | clauses/11.md | 425-448 |
| 11.2A | Cancellation indication | clauses/11.md | 449-498 |
| 11.3 | Group TPC commands for PUCCH/PUSCH | clauses/11.md | 499-534 |
| 11.4 | SRS switching | clauses/11.md | 535-558 |
| 11.5 | Adaptation of cell operation | clauses/11.md | 559-597 |
| 12 | Bandwidth part operation | clauses/12.md | 1-120 |
| 13 | UE procedure for monitoring Type0-PDCCH CSS sets | clauses/13.md | 1-517 |
| 14 | Integrated access-backhaul operation | clauses/14.md | 1-232 |
| 15 | Dual active protocol stack based handover | clauses/15.md | 1-52 |
| 16 | UE procedures for sidelink | clauses/16.md | 1-1230 |
| 16.1 | Synchronization procedures | clauses/16.md | 19-151 |
| 16.2 | Power control | clauses/16.md | 152-607 |
| 16.2.0 | S-SS/PSBCH blocks | clauses/16.md | 154-183 |
| 16.2.1 | PSSCH | clauses/16.md | 184-249 |
| 16.2.2 | PSCCH | clauses/16.md | 250-267 |
| 16.2.3 | PSFCH | clauses/16.md | 268-393 |
| 16.2.3A | SL PRS | clauses/16.md | 394-461 |
| 16.2.4 | Prioritization of transmissions/receptions | clauses/16.md | 462-595 |
| 16.2.4.1 | Simultaneous NR and E-UTRA transmission/reception | clauses/16.md | 464-497 |
| 16.2.4.2 | Simultaneous PSFCH transmission/reception | clauses/16.md | 498-521 |
| 16.2.4.3 | Simultaneous SL and UL transmissions/receptions | clauses/16.md | 522-595 |
| 16.2.4.3.1 | Prioritizations for sidelink and uplink transmissions/receptions | clauses/16.md | 556-595 |
| 16.2.5 | SL Carrier Aggregation | clauses/16.md | 596-607 |
| 16.3 | UE procedure for reporting and obtaining control information in PSFCH | clauses/16.md | 608-792 |
| 16.3.0 | UE procedure for transmitting PSFCH with control information | clauses/16.md | 612-754 |
| 16.3.1 | UE procedure for receiving PSFCH with control information | clauses/16.md | 755-792 |
| 16.4 | UE procedure for transmitting PSCCH | clauses/16.md | 793-828 |
| 16.4A | UE procedure for transmitting PSCCH in dedicated SL PRS resource pool | clauses/16.md | 829-870 |
| 16.5 | UE procedure for reporting HARQ-ACK on uplink | clauses/16.md | 871-1216 |
| 16.5.1 | Type-1 HARQ-ACK codebook determination | clauses/16.md | 955-1072 |
| 16.5.1.1 | Type-1 HARQ-ACK codebook in physical uplink control channel | clauses/16.md | 971-1040 |
| 16.5.1.2 | Type-1 HARQ-ACK codebook in physical uplink shared channel | clauses/16.md | 1041-1072 |
| 16.5.2 | Type-2 HARQ-ACK codebook determination | clauses/16.md | 1073-1216 |
| 16.5.2.1 | Type-2 HARQ-ACK codebook in physical uplink control channel | clauses/16.md | 1077-1178 |
| 16.5.2.2 | Type-2 HARQ-ACK codebook in physical uplink shared channel | clauses/16.md | 1179-1216 |
| 16.6 | UE procedure for LTE sidelink transmission | clauses/16.md | 1217-1220 |
| 16.7 | Operation for in-device coexistence and for co-channel coexistence | clauses/16.md | 1221-1230 |
| 17 | UE with reduced capabilities | clauses/17.md | 1-134 |
| 17.1 | First procedures for RedCap UE | clauses/17.md | 5-58 |
| 17.1A | Second procedures for RedCap UE | clauses/17.md | 59-98 |
| 17.2 | Half-Duplex UE in paired spectrum | clauses/17.md | 99-134 |
| 18 | Multicast Broadcast Services | clauses/18.md | 1-123 |
| 19 | PUSCH transmission in RRCINACTIVE state | clauses/19.md | 1-77 |
| 19.1 | Configured-grant based PUSCH transmission | clauses/19.md | 3-69 |
| 19.2 | Random-access based PUSCH transmission | clauses/19.md | 70-77 |
| 20 | Network controlled repeater | clauses/20.md | 1-76 |
| 21 | L1/L2-triggered mobility procedures | clauses/21.md | 1-46 |
| 21.1 | Configured-grant PUSCH transmission in RACH-less LTM cell switch | clauses/21.md | 17-46 |
| 22 | PUSCH transmission in RACH-less handover | clauses/22.md | 1-1 |
| 22.1 | Configured-grant PUSCH transmission | clauses/22.1.md | 1-34 |
| 22.2 | Dynamic-grant PUSCH transmission | clauses/22.2.md | 1-619 |
