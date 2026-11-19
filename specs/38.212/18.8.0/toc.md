# TS 38.212 V18.8.0 — NR multiplexing and channel coding

Clause index. `File` is relative to this directory; `Lines` is the 1-based
line range of the clause inside that file.

| Clause | Title | File | Lines |
|---|---|---|---|
| front-matter | Title page, foreword and scope front matter | clauses/front-matter.md | 1-393 |
| 1 | Scope | clauses/1.md | 1-4 |
| 2 | References | clauses/2.md | 1-38 |
| 3 | Definitions of terms, symbols and abbreviations | clauses/3.md | 1-144 |
| 3.1 | Terms | clauses/3.md | 3-6 |
| 3.2 | Symbols | clauses/3.md | 7-10 |
| 3.3 | Abbreviations | clauses/3.md | 11-144 |
| 4 | Mapping to physical channels | clauses/4.md | 1-56 |
| 4.1 | Uplink | clauses/4.md | 3-19 |
| 4.2 | Downlink | clauses/4.md | 20-37 |
| 4.3 | Sidelink | clauses/4.md | 38-56 |
| 5 | General procedures | clauses/5.md | 1-1277 |
| 5.1 | CRC calculation | clauses/5.md | 5-32 |
| 5.2 | Code block segmentation and code block CRC attachment | clauses/5.md | 33-184 |
| 5.2.1 | Polar coding | clauses/5.md | 35-86 |
| 5.2.2 | Low density parity check coding | clauses/5.md | 87-184 |
| 5.3 | Channel coding | clauses/5.md | 185-903 |
| 5.3.1 | Polar coding | clauses/5.md | 206-499 |
| 5.3.1.1 | Interleaving | clauses/5.md | 232-296 |
| 5.3.1.2 | Polar encoding | clauses/5.md | 297-499 |
| 5.3.2 | Low density parity check coding | clauses/5.md | 500-823 |
| 5.3.3 | Channel coding of small block lengths | clauses/5.md | 824-903 |
| 5.3.3.1 | Encoding of 1-bit information | clauses/5.md | 828-844 |
| 5.3.3.2 | Encoding of 2-bit information | clauses/5.md | 845-861 |
| 5.3.3.3 | Encoding of other small block lengths | clauses/5.md | 862-903 |
| 5.4 | Rate matching | clauses/5.md | 904-1251 |
| 5.4.1 | Rate matching for Polar code | clauses/5.md | 906-1072 |
| 5.4.1.1 | Sub-block interleaving | clauses/5.md | 910-976 |
| 5.4.1.2 | Bit selection | clauses/5.md | 977-1012 |
| 5.4.1.3 | Interleaving of coded bits | clauses/5.md | 1013-1072 |
| 5.4.2 | Rate matching for LDPC code | clauses/5.md | 1073-1241 |
| 5.4.2.1 | Bit selection | clauses/5.md | 1077-1227 |
| 5.4.2.2 | Bit interleaving | clauses/5.md | 1228-1241 |
| 5.4.3 | Rate matching for channel coding of small block lengths | clauses/5.md | 1242-1251 |
| 5.5 | Code block concatenation | clauses/5.md | 1252-1277 |
| 6 | Uplink transport channels and control information | clauses/6.md | 1-1 |
| 6.1 | Random access channel | clauses/6.1.md | 1-4 |
| 6.2 | Uplink shared channel | clauses/6.2.md | 1-676 |
| 6.2.1 | Transport block CRC attachment | clauses/6.2.md | 3-12 |
| 6.2.2 | LDPC base graph selection | clauses/6.2.md | 13-22 |
| 6.2.3 | Code block segmentation and code block CRC attachment | clauses/6.2.md | 23-32 |
| 6.2.4 | Channel coding of UL-SCH | clauses/6.2.md | 33-38 |
| 6.2.5 | Rate matching | clauses/6.2.md | 39-50 |
| 6.2.6 | Code block concatenation | clauses/6.2.md | 51-58 |
| 6.2.7 | Data and control multiplexing | clauses/6.2.md | 59-676 |
| 6.3 | Uplink control information | clauses/6.3.md | 1-1 |
| 6.3.1 | Uplink control information on PUCCH | clauses/6.3.1.md | 1-861 |
| 6.3.1.1 | UCI bit sequence generation | clauses/6.3.1.md | 9-578 |
| 6.3.1.1.1 | HARQ-ACK/SR only | clauses/6.3.1.md | 11-16 |
| 6.3.1.1.2 | CSI only | clauses/6.3.1.md | 17-548 |
| 6.3.1.1.3 | HARQ-ACK/SR and CSI | clauses/6.3.1.md | 549-568 |
| 6.3.1.1.4 | UCI with different priority indexes | clauses/6.3.1.md | 569-578 |
| 6.3.1.2 | Code block segmentation and CRC attachment | clauses/6.3.1.md | 579-596 |
| 6.3.1.2.1 | UCI encoded by Polar code | clauses/6.3.1.md | 583-590 |
| 6.3.1.2.2 | UCI encoded by channel coding of small block lengths | clauses/6.3.1.md | 591-596 |
| 6.3.1.3 | Channel coding of UCI | clauses/6.3.1.md | 597-616 |
| 6.3.1.3.1 | UCI encoded by Polar code | clauses/6.3.1.md | 599-608 |
| 6.3.1.3.2 | UCI encoded by channel coding of small block lengths | clauses/6.3.1.md | 609-616 |
| 6.3.1.4 | Rate matching | clauses/6.3.1.md | 617-719 |
| 6.3.1.4.1 | UCI encoded by Polar code | clauses/6.3.1.md | 630-668 |
| 6.3.1.4.2 | UCI encoded by channel coding of small block lengths | clauses/6.3.1.md | 669-678 |
| 6.3.1.4.3 | UCI with different priority indexes encoded by Polar code | clauses/6.3.1.md | 679-707 |
| 6.3.1.4.4 | UCI with different priority indexes encoded by channel coding of small block lengths | clauses/6.3.1.md | 708-719 |
| 6.3.1.5 | Code block concatenation | clauses/6.3.1.md | 720-727 |
| 6.3.1.6 | Multiplexing of coded UCI bits to PUCCH | clauses/6.3.1.md | 728-861 |
| 6.3.2 | Uplink control information on PUSCH | clauses/6.3.2.md | 1-5 |
| 6.3.2.1 | UCI bit sequence generation | clauses/6.3.2.1.md | 1-671 |
| 6.3.2.1.1 | HARQ-ACK | clauses/6.3.2.1.md | 3-14 |
| 6.3.2.1.2 | CSI | clauses/6.3.2.1.md | 15-579 |
| 6.3.2.1.3 | CG-UCI | clauses/6.3.2.1.md | 580-595 |
| 6.3.2.1.3A | UTO-UCI | clauses/6.3.2.1.md | 596-601 |
| 6.3.2.1.4 | HARQ-ACK and CG-UCI/UTO-UCI | clauses/6.3.2.1.md | 602-611 |
| 6.3.2.1.5 | UCI with different priority indexes | clauses/6.3.2.1.md | 612-671 |
| 6.3.2.2 | Code block segmentation and CRC attachment | clauses/6.3.2.2.md | 1-12 |
| 6.3.2.2.1 | UCI encoded by Polar code | clauses/6.3.2.2.md | 5-8 |
| 6.3.2.2.2 | UCI encoded by channel coding of small block lengths | clauses/6.3.2.2.md | 9-12 |
| 6.3.2.3 | Channel coding of UCI | clauses/6.3.2.3.md | 1-14 |
| 6.3.2.3.1 | UCI encoded by Polar code | clauses/6.3.2.3.md | 3-6 |
| 6.3.2.3.2 | UCI encoded by channel coding of small block lengths | clauses/6.3.2.3.md | 7-14 |
| 6.3.2.4 | Rate matching | clauses/6.3.2.4.md | 1-648 |
| 6.3.2.4.1 | UCI encoded by Polar code | clauses/6.3.2.4.md | 5-524 |
| 6.3.2.4.1.1 | HARQ-ACK | clauses/6.3.2.4.md | 9-120 |
| 6.3.2.4.1.2 | CSI part 1 | clauses/6.3.2.4.md | 121-240 |
| 6.3.2.4.1.3 | CSI part 2 | clauses/6.3.2.4.md | 241-346 |
| 6.3.2.4.1.4 | CG-UCI | clauses/6.3.2.4.md | 347-408 |
| 6.3.2.4.1.5 | HARQ-ACK and CG-UCI | clauses/6.3.2.4.md | 409-472 |
| 6.3.2.4.1.6 | UCI with different priority indexes | clauses/6.3.2.4.md | 473-524 |
| 6.3.2.4.2 | UCI encoded by channel coding of small block lengths | clauses/6.3.2.4.md | 525-648 |
| 6.3.2.4.2.1 | HARQ-ACK | clauses/6.3.2.4.md | 529-542 |
| 6.3.2.4.2.2 | CSI part 1 | clauses/6.3.2.4.md | 543-554 |
| 6.3.2.4.2.3 | CSI part 2 | clauses/6.3.2.4.md | 555-566 |
| 6.3.2.4.2.4 | CG-UCI | clauses/6.3.2.4.md | 567-582 |
| 6.3.2.4.2.5 | HARQ-ACK and CG-UCI | clauses/6.3.2.4.md | 583-596 |
| 6.3.2.4.2.6 | UCI with different priority indexes | clauses/6.3.2.4.md | 597-648 |
| 6.3.2.5 | Code block concatenation | clauses/6.3.2.5.md | 1-4 |
| 6.3.2.6 | Multiplexing of coded UCI bits to PUSCH | clauses/6.3.2.6.md | 1-4 |
| 6.3.2.7 | Multiplexing of coded UCI bits with different priority indexes to PUSCH | clauses/6.3.2.7.md | 1-20 |
| 7 | Downlink transport channels and control information | clauses/7.md | 1-1 |
| 7.1 | Broadcast channel | clauses/7.1.md | 1-154 |
| 7.1.1 | PBCH payload generation | clauses/7.1.md | 15-91 |
| 7.1.2 | Scrambling | clauses/7.1.md | 92-128 |
| 7.1.3 | Transport block CRC attachment | clauses/7.1.md | 129-138 |
| 7.1.4 | Channel coding | clauses/7.1.md | 139-144 |
| 7.1.5 | Rate matching | clauses/7.1.md | 145-154 |
| 7.2 | Downlink shared channel and paging channel | clauses/7.2.md | 1-50 |
| 7.2.1 | Transport block CRC attachment | clauses/7.2.md | 3-12 |
| 7.2.2 | LDPC base graph selection | clauses/7.2.md | 13-22 |
| 7.2.3 | Code block segmentation and code block CRC attachment | clauses/7.2.md | 23-30 |
| 7.2.4 | Channel coding | clauses/7.2.md | 31-36 |
| 7.2.5 | Rate matching | clauses/7.2.md | 37-42 |
| 7.2.6 | Code block concatenation | clauses/7.2.md | 43-50 |
| 7.3 | Downlink control information | clauses/7.3.md | 1-13 |
| 7.3.1 | DCI formats | clauses/7.3.1.md | 1-52 |
| 7.3.1.0 | DCI size alignment | clauses/7.3.1.0.md | 1-152 |
| 7.3.1.0.1 | DCI size alignment for DCI formats for scheduling of sidelink | clauses/7.3.1.0.md | 141-152 |
| 7.3.1.1 | DCI formats for scheduling of PUSCH | clauses/7.3.1.1.md | 1-1 |
| 7.3.1.1.1 | Format 00 | clauses/7.3.1.1.1.md | 1-166 |
| 7.3.1.1.2 | Format 01 | clauses/7.3.1.1.2.md | 1-3036 |
| 7.3.1.1.3 | Format 02 | clauses/7.3.1.1.3.md | 1-413 |
| 7.3.1.1.4 | Format 03 | clauses/7.3.1.1.4.md | 1-388 |
| 7.3.1.2 | DCI formats for scheduling of PDSCH | clauses/7.3.1.2.md | 1-2062 |
| 7.3.1.2.1 | Format 10 | clauses/7.3.1.2.md | 3-214 |
| 7.3.1.2.2 | Format 11 | clauses/7.3.1.2.md | 215-1493 |
| 7.3.1.2.3 | Format 12 | clauses/7.3.1.2.md | 1494-1704 |
| 7.3.1.2.4 | Format 13 | clauses/7.3.1.2.md | 1705-2062 |
| 7.3.1.3 | DCI formats for other purposes | clauses/7.3.1.3.md | 1-178 |
| 7.3.1.3.1 | Format 20 | clauses/7.3.1.3.md | 3-26 |
| 7.3.1.3.2 | Format 21 | clauses/7.3.1.3.md | 27-36 |
| 7.3.1.3.3 | Format 22 | clauses/7.3.1.3.md | 37-56 |
| 7.3.1.3.4 | Format 23 | clauses/7.3.1.3.md | 57-80 |
| 7.3.1.3.5 | Format 24 | clauses/7.3.1.3.md | 81-90 |
| 7.3.1.3.6 | Format 25 | clauses/7.3.1.3.md | 91-100 |
| 7.3.1.3.7 | Format 26 | clauses/7.3.1.3.md | 101-118 |
| 7.3.1.3.8 | Format 27 | clauses/7.3.1.3.md | 119-136 |
| 7.3.1.3.9 | Format 28 | clauses/7.3.1.3.md | 137-152 |
| 7.3.1.3.10 | Format 29 | clauses/7.3.1.3.md | 153-178 |
| 7.3.1.4 | DCI formats for scheduling of sidelink | clauses/7.3.1.4.md | 1-96 |
| 7.3.1.4.1 | Format 30 | clauses/7.3.1.4.md | 3-44 |
| 7.3.1.4.2 | Format 31 | clauses/7.3.1.4.md | 45-68 |
| 7.3.1.4.3 | Format 32 | clauses/7.3.1.4.md | 69-96 |
| 7.3.1.5 | DCI formats for scheduling of MBS | clauses/7.3.1.5.md | 1-138 |
| 7.3.1.5.1 | Format 40 | clauses/7.3.1.5.md | 3-26 |
| 7.3.1.5.2 | Format 41 | clauses/7.3.1.5.md | 27-58 |
| 7.3.1.5.3 | Format 42 | clauses/7.3.1.5.md | 59-138 |
| 7.3.2 | CRC attachment | clauses/7.3.2.md | 1-18 |
| 7.3.3 | Channel coding | clauses/7.3.3.md | 1-6 |
| 7.3.4 | Rate matching | clauses/7.3.4.md | 1-8 |
| 8 | Sidelink transport channels and control information | clauses/8.md | 1-660 |
| 8.1 | Sidelink broadcast channel | clauses/8.md | 3-16 |
| 8.1.1 | Void | clauses/8.md | 15-16 |
| 8.2 | Sidelink shared channel | clauses/8.md | 17-96 |
| 8.2.1 | Data and control multiplexing | clauses/8.md | 25-96 |
| 8.3 | Sidelink control information on PSCCH | clauses/8.md | 97-237 |
| 8.3.1 | 1<sup>st</sup>-stage SCI formats | clauses/8.md | 101-225 |
| 8.3.1.1 | SCI format 1-A | clauses/8.md | 107-192 |
| 8.3.1.2 | SCI format 1-B | clauses/8.md | 193-225 |
| 8.3.2 | CRC attachment | clauses/8.md | 226-229 |
| 8.3.3 | Channel coding | clauses/8.md | 230-233 |
| 8.3.4 | Rate Matching | clauses/8.md | 234-237 |
| 8.4 | Sidelink control information on PSSCH | clauses/8.md | 238-660 |
| 8.4.1 | 2<sup>nd</sup>-stage SCI formats | clauses/8.md | 242-404 |
| 8.4.1.1 | SCI format 2-A | clauses/8.md | 248-289 |
| 8.4.1.2 | SCI format 2-B | clauses/8.md | 290-311 |
| 8.4.1.3 | SCI format 2-C | clauses/8.md | 312-381 |
| 8.4.1.4 | SCI format 2-D | clauses/8.md | 382-404 |
| 8.4.2 | CRC attachment | clauses/8.md | 405-408 |
| 8.4.3 | Channel coding | clauses/8.md | 409-412 |
| 8.4.4 | Rate Matching | clauses/8.md | 413-446 |
| 8.4.5 | Multiplexing of coded 2<sup>nd</sup>-stage SCI bits to PSSCH | clauses/8.md | 447-660 |
