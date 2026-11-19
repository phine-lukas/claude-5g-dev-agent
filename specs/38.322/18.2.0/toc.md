# TS 38.322 V18.2.0 — NR RLC

Clause index. `File` is relative to this directory; `Lines` is the 1-based
line range of the clause inside that file.

| Clause | Title | File | Lines |
|---|---|---|---|
| front-matter | Title page, foreword and scope front matter | clauses/front-matter.md | 1-282 |
| 1 | Scope | clauses/1.md | 1-4 |
| 2 | References | clauses/2.md | 1-28 |
| 3 | Definitions, symbols and abbreviations | clauses/3.md | 1-64 |
| 3.1 | Definitions | clauses/3.md | 3-18 |
| 3.2 | Abbreviations | clauses/3.md | 19-64 |
| 4 | General | clauses/4.md | 1-198 |
| 4.1 | Introduction | clauses/4.md | 3-6 |
| 4.2 | RLC architecture | clauses/4.md | 7-158 |
| 4.2.1 | RLC entities | clauses/4.md | 9-158 |
| 4.2.1.1 | TM RLC entity | clauses/4.md | 49-78 |
| 4.2.1.1.1 | General | clauses/4.md | 51-64 |
| 4.2.1.1.2 | Transmitting TM RLC entity | clauses/4.md | 65-72 |
| 4.2.1.1.3 | Receiving TM RLC entity | clauses/4.md | 73-78 |
| 4.2.1.2 | UM RLC entity | clauses/4.md | 79-112 |
| 4.2.1.2.1 | General | clauses/4.md | 81-98 |
| 4.2.1.2.2 | Transmitting UM RLC entity | clauses/4.md | 99-102 |
| 4.2.1.2.3 | Receiving UM RLC entity | clauses/4.md | 103-112 |
| 4.2.1.3 | AM RLC entity | clauses/4.md | 113-158 |
| 4.2.1.3.1 | General | clauses/4.md | 115-134 |
| 4.2.1.3.2 | Transmitting side | clauses/4.md | 135-148 |
| 4.2.1.3.3 | Receiving side | clauses/4.md | 149-158 |
| 4.3 | Services | clauses/4.md | 159-178 |
| 4.3.1 | Services provided to upper layers | clauses/4.md | 161-170 |
| 4.3.2 | Services expected from lower layers | clauses/4.md | 171-178 |
| 4.4 | Functions | clauses/4.md | 179-198 |
| 5 | Procedures | clauses/5.md | 1-518 |
| 5.1 | RLC entity handling | clauses/5.md | 3-44 |
| 5.1.1 | RLC entity establishment | clauses/5.md | 5-24 |
| 5.1.2 | RLC entity re-establishment | clauses/5.md | 25-34 |
| 5.1.3 | RLC entity release | clauses/5.md | 35-44 |
| 5.2 | Data transfer procedures | clauses/5.md | 45-302 |
| 5.2.1 | TM data transfer | clauses/5.md | 47-64 |
| 5.2.1.1 | Transmit operations | clauses/5.md | 49-56 |
| 5.2.1.1.1 | General | clauses/5.md | 51-56 |
| 5.2.1.2 | Receive operations | clauses/5.md | 57-64 |
| 5.2.1.2.1 | General | clauses/5.md | 59-64 |
| 5.2.2 | UM data transfer | clauses/5.md | 65-172 |
| 5.2.2.1 | Transmit operations | clauses/5.md | 67-76 |
| 5.2.2.1.1 | General | clauses/5.md | 69-76 |
| 5.2.2.2 | Receive operations | clauses/5.md | 77-172 |
| 5.2.2.2.1 | General | clauses/5.md | 79-98 |
| 5.2.2.2.2 | Actions when an UMD PDU is received from lower layer | clauses/5.md | 99-114 |
| 5.2.2.2.3 | Actions when an UMD PDU is placed in the reception buffer | clauses/5.md | 115-156 |
| 5.2.2.2.4 | Actions when t-Reassembly expires | clauses/5.md | 157-172 |
| 5.2.3 | AM data transfer | clauses/5.md | 173-302 |
| 5.2.3.1 | Transmit operations | clauses/5.md | 175-208 |
| 5.2.3.1.1 | General | clauses/5.md | 177-208 |
| 5.2.3.2 | Receive operations | clauses/5.md | 209-302 |
| 5.2.3.2.1 | General | clauses/5.md | 211-230 |
| 5.2.3.2.2 | Actions when an AMD PDU is received from lower layer | clauses/5.md | 231-248 |
| 5.2.3.2.3 | Actions when an AMD PDU is placed in the reception buffer | clauses/5.md | 249-288 |
| 5.2.3.2.4 | Actions when t-Reassembly expires | clauses/5.md | 289-302 |
| 5.3 | ARQ procedures | clauses/5.md | 303-486 |
| 5.3.1 | General | clauses/5.md | 305-308 |
| 5.3.2 | Retransmission | clauses/5.md | 309-350 |
| 5.3.3 | Polling | clauses/5.md | 351-424 |
| 5.3.3.1 | General | clauses/5.md | 353-356 |
| 5.3.3.2 | Transmission of a AMD PDU | clauses/5.md | 357-400 |
| 5.3.3.3 | Reception of a STATUS report | clauses/5.md | 401-410 |
| 5.3.3.4 | Expiry of t-PollRetransmit | clauses/5.md | 411-424 |
| 5.3.4 | Status reporting | clauses/5.md | 425-486 |
| 5.4 | SDU discard procedures | clauses/5.md | 487-490 |
| 5.5 | Data volume calculation | clauses/5.md | 491-510 |
| 5.6 | Handling of unknown, unforeseen and erroneous protocol data | clauses/5.md | 511-518 |
| 5.6.1 | Reception of PDU with reserved or invalid values | clauses/5.md | 513-518 |
| 6 | Protocol data units, formats and parameters | clauses/6.md | 1-293 |
| 6.1 | Protocol data units | clauses/6.md | 3-28 |
| 6.1.1 | General | clauses/6.md | 5-8 |
| 6.1.2 | RLC data PDU | clauses/6.md | 9-22 |
| 6.1.3 | RLC control PDU | clauses/6.md | 23-28 |
| 6.2 | Formats and parameters | clauses/6.md | 29-293 |
| 6.2.1 | General | clauses/6.md | 31-34 |
| 6.2.2 | Formats | clauses/6.md | 35-118 |
| 6.2.2.1 | General | clauses/6.md | 37-42 |
| 6.2.2.2 | TMD PDU | clauses/6.md | 43-50 |
| 6.2.2.3 | UMD PDU | clauses/6.md | 51-78 |
| 6.2.2.4 | AMD PDU | clauses/6.md | 79-102 |
| 6.2.2.5 | STATUS PDU | clauses/6.md | 103-118 |
| 6.2.3 | Parameters | clauses/6.md | 119-293 |
| 6.2.3.1 | General | clauses/6.md | 121-124 |
| 6.2.3.2 | Data field | clauses/6.md | 125-148 |
| 6.2.3.3 | Sequence Number (SN) field | clauses/6.md | 149-154 |
| 6.2.3.4 | Segmentation Info (SI) field | clauses/6.md | 155-170 |
| 6.2.3.5 | Segment Offset (SO) field | clauses/6.md | 171-176 |
| 6.2.3.6 | Data/Control (D/C) field | clauses/6.md | 177-189 |
| 6.2.3.7 | Polling bit (P) field | clauses/6.md | 190-202 |
| 6.2.3.8 | Reserved (R) field | clauses/6.md | 203-208 |
| 6.2.3.9 | Control PDU Type (CPT) field | clauses/6.md | 209-222 |
| 6.2.3.10 | Acknowledgement SN (ACKSN) field | clauses/6.md | 223-228 |
| 6.2.3.11 | Extension bit 1 (E1) field | clauses/6.md | 229-241 |
| 6.2.3.12 | Negative Acknowledgement SN (NACKSN) field | clauses/6.md | 242-247 |
| 6.2.3.13 | Extension bit 2 (E2) field | clauses/6.md | 248-260 |
| 6.2.3.14 | SO start (SOstart) field | clauses/6.md | 261-266 |
| 6.2.3.15 | SO end (SOend) field | clauses/6.md | 267-274 |
| 6.2.3.16 | Extension bit 3 (E3) field | clauses/6.md | 275-287 |
| 6.2.3.17 | NACK range field | clauses/6.md | 288-293 |
| 7 | Variables, constants and timers | clauses/7.md | 1-160 |
| 7.1 | State variables | clauses/7.md | 3-84 |
| 7.2 | Constants | clauses/7.md | 85-94 |
| 7.3 | Timers | clauses/7.md | 95-110 |
| 7.4 | Configurable parameters | clauses/7.md | 111-160 |
