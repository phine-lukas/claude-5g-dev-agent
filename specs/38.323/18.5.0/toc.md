# TS 38.323 V18.5.0 — NR PDCP

Clause index. `File` is relative to this directory; `Lines` is the 1-based
line range of the clause inside that file.

| Clause | Title | File | Lines |
|---|---|---|---|
| front-matter | Title page, foreword and scope front matter | clauses/front-matter.md | 1-346 |
| 1 | Scope | clauses/1.md | 1-4 |
| 2 | References | clauses/2.md | 1-56 |
| 3 | Definitions and abbreviations | clauses/3.md | 1-148 |
| 3.1 | Definitions | clauses/3.md | 3-60 |
| 3.2 | Abbreviations | clauses/3.md | 61-148 |
| 4 | General | clauses/4.md | 1-140 |
| 4.1 | Introduction | clauses/4.md | 3-6 |
| 4.2 | Architecture | clauses/4.md | 7-70 |
| 4.2.1 | PDCP structure | clauses/4.md | 9-48 |
| 4.2.2 | PDCP entities | clauses/4.md | 49-70 |
| 4.3 | Services | clauses/4.md | 71-106 |
| 4.3.1 | Services provided to upper layers | clauses/4.md | 73-90 |
| 4.3.2 | Services expected from lower layers | clauses/4.md | 91-106 |
| 4.4 | Functions | clauses/4.md | 107-140 |
| 5 | Procedures | clauses/5.md | 1-995 |
| 5.1 | PDCP entity handling | clauses/5.md | 3-148 |
| 5.1.1 | PDCP entity establishment | clauses/5.md | 5-16 |
| 5.1.2 | PDCP entity re-establishment | clauses/5.md | 17-94 |
| 5.1.3 | PDCP entity release | clauses/5.md | 95-106 |
| 5.1.4 | PDCP entity suspend | clauses/5.md | 107-124 |
| 5.1.5 | PDCP entity reconfiguration | clauses/5.md | 125-148 |
| 5.2 | Data transfer | clauses/5.md | 149-402 |
| 5.2.1 | Transmit operation | clauses/5.md | 151-274 |
| 5.2.2 | Receive operation | clauses/5.md | 275-378 |
| 5.2.2.1 | Actions when a PDCP Data PDU is received from lower layers | clauses/5.md | 277-352 |
| 5.2.2.2 | Actions when a t-Reordering expires | clauses/5.md | 353-370 |
| 5.2.2.3 | Actions when the value of t-Reordering is reconfigured | clauses/5.md | 371-378 |
| 5.2.3 | Sidelink transmit operation | clauses/5.md | 379-394 |
| 5.2.4 | Sidelink receive operation | clauses/5.md | 395-402 |
| 5.3 | SDU discard | clauses/5.md | 403-424 |
| 5.4 | Status reporting | clauses/5.md | 425-474 |
| 5.4.1 | Transmit operation | clauses/5.md | 427-468 |
| 5.4.2 | Receive operation | clauses/5.md | 469-474 |
| 5.5 | Data recovery | clauses/5.md | 475-482 |
| 5.6 | Data volume calculation | clauses/5.md | 483-550 |
| 5.7 | Robust header compression and decompression | clauses/5.md | 551-643 |
| 5.7.1 | Supported header compression protocols and profiles | clauses/5.md | 553-577 |
| 5.7.2 | Configuration of ROHC | clauses/5.md | 578-581 |
| 5.7.3 | Protocol parameters | clauses/5.md | 582-605 |
| 5.7.4 | Header compression using ROHC | clauses/5.md | 606-623 |
| 5.7.5 | Header decompression using ROHC | clauses/5.md | 624-629 |
| 5.7.6 | PDCP Control PDU for interspersed ROHC feedback | clauses/5.md | 630-643 |
| 5.7.6.1 | Transmit Operation | clauses/5.md | 632-637 |
| 5.7.6.2 | Receive Operation | clauses/5.md | 638-643 |
| 5.8 | Ciphering and deciphering | clauses/5.md | 644-667 |
| 5.9 | Integrity protection and verification | clauses/5.md | 668-697 |
| 5.10 | Handling of unknown, unforeseen, and erroneous protocol data | clauses/5.md | 698-705 |
| 5.11 | PDCP duplication | clauses/5.md | 706-765 |
| 5.11.1 | Activation/Deactivation of PDCP duplication | clauses/5.md | 708-741 |
| 5.11.2 | Duplicate PDU discard | clauses/5.md | 742-765 |
| 5.12 | Ethernet header compression and decompression | clauses/5.md | 766-823 |
| 5.12.1 | Supported header compression protocols | clauses/5.md | 768-771 |
| 5.12.2 | Configuration of EHC | clauses/5.md | 772-775 |
| 5.12.3 | Protocol parameters | clauses/5.md | 776-781 |
| 5.12.4 | Header compression using EHC | clauses/5.md | 782-793 |
| 5.12.5 | Header decompression using EHC | clauses/5.md | 794-797 |
| 5.12.6 | PDCP Control PDU for EHC feedback | clauses/5.md | 798-811 |
| 5.12.6.1 | Transmit Operation | clauses/5.md | 800-805 |
| 5.12.6.2 | Receive Operation | clauses/5.md | 806-811 |
| 5.12.7 | Simultaneous configuration of ROHC and EHC | clauses/5.md | 812-823 |
| 5.13 | Uplink data switching | clauses/5.md | 824-843 |
| 5.14 | Uplink Data compression and decompression | clauses/5.md | 844-889 |
| 5.14.1 | UDC protocol | clauses/5.md | 846-853 |
| 5.14.2 | Configuration of UDC | clauses/5.md | 854-857 |
| 5.14.3 | UDC header | clauses/5.md | 858-865 |
| 5.14.4 | Uplink data compression | clauses/5.md | 866-871 |
| 5.14.5 | PDCP Control PDU for UDC feedback | clauses/5.md | 872-877 |
| 5.14.6 | Pre-defined dictionary | clauses/5.md | 878-881 |
| 5.14.7 | UDC buffer reset procedure | clauses/5.md | 882-885 |
| 5.14.8 | UDC checksum error handling | clauses/5.md | 886-889 |
| 5.15 | Data volume calculation for delay status reporting | clauses/5.md | 890-935 |
| 5.16 | SN gap report | clauses/5.md | 936-995 |
| 5.16.1 | Transmit operation | clauses/5.md | 938-965 |
| 5.16.2 | Receive operation | clauses/5.md | 966-995 |
| 6 | Protocol data units, formats, and parameters | clauses/6.md | 1-319 |
| 6.1 | Protocol data units | clauses/6.md | 3-28 |
| 6.1.1 | Data PDU | clauses/6.md | 5-14 |
| 6.1.2 | Control PDU | clauses/6.md | 15-28 |
| 6.2 | Formats | clauses/6.md | 29-138 |
| 6.2.1 | General | clauses/6.md | 31-36 |
| 6.2.2 | Data PDU | clauses/6.md | 37-96 |
| 6.2.2.1 | Data PDU for SRBs | clauses/6.md | 39-46 |
| 6.2.2.2 | Data PDU for DRBs and MRBs with 12 bits PDCP SN | clauses/6.md | 47-54 |
| 6.2.2.3 | Data PDU for DRBs and MRBs with 18 bits PDCP SN | clauses/6.md | 55-62 |
| 6.2.2.4 | Data PDU for sidelink DRBs for groupcast and broadcast, for the sidelink SRB0‎ and for the sidelink SRB4 | clauses/6.md | 63-72 |
| 6.2.2.5 | Data PDU for sidelink SRBs for unicast | clauses/6.md | 73-80 |
| 6.2.2.6 | Data PDU for sidelink DRBs for unicast with 12 bits PDCP SN | clauses/6.md | 81-88 |
| 6.2.2.7 | Data PDU for sidelink DRBs for unicast with 18 bits PDCP SN | clauses/6.md | 89-96 |
| 6.2.3 | Control PDU | clauses/6.md | 97-138 |
| 6.2.3.1 | Control PDU for PDCP status report | clauses/6.md | 99-106 |
| 6.2.3.2 | Control PDU for interspersed ROHC feedback | clauses/6.md | 107-114 |
| 6.2.3.3 | Control PDU for EHC feedback | clauses/6.md | 115-122 |
| 6.2.3.4 | Control PDU for UDC feedback | clauses/6.md | 123-130 |
| 6.2.3.5 | Control PDU for PDCP SN gap report | clauses/6.md | 131-138 |
| 6.3 | Parameters | clauses/6.md | 139-319 |
| 6.3.1 | General | clauses/6.md | 141-146 |
| 6.3.2 | PDCP SN | clauses/6.md | 147-160 |
| 6.3.3 | Data | clauses/6.md | 161-172 |
| 6.3.4 | MAC-I | clauses/6.md | 173-184 |
| 6.3.5 | COUNT | clauses/6.md | 185-196 |
| 6.3.6 | R | clauses/6.md | 197-202 |
| 6.3.7 | D/C | clauses/6.md | 203-216 |
| 6.3.8 | PDU type | clauses/6.md | 217-234 |
| 6.3.9 | FMC | clauses/6.md | 235-240 |
| 6.3.10 | Bitmap | clauses/6.md | 241-254 |
| 6.3.11 | Interspersed ROHC feedback | clauses/6.md | 255-260 |
| 6.3.12 | SDU Type | clauses/6.md | 261-278 |
| 6.3.13 | K<sub>NRP-sess</sub> ID | clauses/6.md | 279-286 |
| 6.3.14 | FE | clauses/6.md | 287-300 |
| 6.3.15 | FDC | clauses/6.md | 301-306 |
| 6.3.16 | Discard Bitmap | clauses/6.md | 307-319 |
| 7 | State variables, constants, and timers | clauses/7.md | 1-286 |
| 7.1 | State variables | clauses/7.md | 3-36 |
| 7.2 | Constants | clauses/7.md | 37-42 |
| 7.3 | Timers | clauses/7.md | 43-62 |
| A.1 | EHC principle | clauses/7.md | 63-88 |
| A.2 | EHC packet format and parameters | clauses/7.md | 89-136 |
| A.2.1 | EHC packet format | clauses/7.md | 91-112 |
| A.2.1.1 | EHC Full Header packet and EHC Compressed Header packet | clauses/7.md | 93-104 |
| A.2.1.2 | EHC feedback packet | clauses/7.md | 105-112 |
| A.2.2 | Parameters | clauses/7.md | 113-136 |
| A.2.2.1 | F/C | clauses/7.md | 115-128 |
| A.2.2.2 | CID | clauses/7.md | 129-136 |
| B.1 | UDC general description | clauses/7.md | 137-144 |
| B.2 | UDC packet format and parameters | clauses/7.md | 145-286 |
| B.2.1 | UDC Header and UDC Data Block format | clauses/7.md | 147-154 |
| B.2.2 | UDC parameters | clauses/7.md | 155-200 |
| B.2.2.1 | FU | clauses/7.md | 157-170 |
| B.2.2.2 | FR | clauses/7.md | 171-184 |
| B.2.2.3 | Checksum | clauses/7.md | 185-200 |
| B.2.3 | An example of UDC Checksum calculation | clauses/7.md | 201-286 |
