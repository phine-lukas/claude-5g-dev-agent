# D.6 Information elements coding

## D.6.1 UE policy delivery service message type

Table D.6.1.1: UE policy delivery service message type

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |     |     |     |     |     |     |     |     |     |                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|---------------------------------------------------|
| Bits                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |     |     |     |     |     |     |     |     |     |                                                   |
| 8                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 7   | 6   | 5   | 4   | 3   | 2   | 1   |     |     |                                                   |
| 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 0   | 0   | 0   | 0   | 0   | 0   | 0   |     |     | Reserved                                          |
| 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 0   | 0   | 0   | 0   | 0   | 0   | 1   |     |     | MANAGE UE POLICY COMMAND message                  |
| 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 0   | 0   | 0   | 0   | 0   | 1   | 0   |     |     | MANAGE UE POLICY COMPLETE message                 |
| 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 0   | 0   | 0   | 0   | 0   | 1   | 1   |     |     | MANAGE UE POLICY COMMAND REJECT message           |
| 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 0   | 0   | 0   | 0   | 1   | 0   | 0   |     |     | UE STATE INDICATION message                       |
| 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 0   | 0   | 0   | 0   | 1   | 0   | 1   |     |     | UE POLICY PROVISIONING REQUEST message (see NOTE) |
| 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 0   | 0   | 0   | 0   | 1   | 1   | 0   |     |     | UE POLICY PROVISIONING REJECT message (see NOTE)  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |     |     |     |     |     |     |     |     |     |                                                   |
| All other values are reserved                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |     |     |     |     |     |     |     |     |     |                                                   |
| NOTE: Coding of UE POLICY PROVISIONING REQUEST message and UE POLICY PROVISIONING REJECT message are specified in 3GPP TS 24.587 \[19B\]. Usage of UE POLICY PROVISIONING REQUEST message and UE POLICY PROVISIONING REJECT message for V2X policy is specified in 3GPP TS 24.587 \[19B\]. Usage of UE POLICY PROVISIONING REQUEST message and UE POLICY PROVISIONING REJECT message for ProSeP policy is specified in 3GPP TS 24.554 \[19E\]. Usage of UE POLICY PROVISIONING REQUEST message and UE POLICY PROVISIONING REJECT message for A2X policy is specified in 3GPP TS 24.577 \[60\]. Usage of UE POLICY PROVISIONING REQUEST message and UE POLICY PROVISIONING REJECT message for RSLPP policy is specified in 3GPP TS 24.514 \[62\]. |     |     |     |     |     |     |     |     |     |                                                   |

## D.6.2 UE policy section management list

The purpose of the UE policy section management list information element is to transfer from the PCF to the UE a list of instructions to be performed at the UE for management of UE policy section stored at the UE.

The UE policy section management list information element is coded as shown in figure D.6.2.1, figure D.6.2.2, figure D.6.2.3, figure D.6.2.4, figure D.6.2.5, figure D.6.2.6, figure D.6.2.7 and table D.6.2.1.

The UE policy section management list information element has a minimum length of 12 octets and a maximum length of 65534 octets.

<!-- table -->
| 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |  |
| UE policy section management list IEI (x8) | octet 1 |
| Length of UE policy section management list contents (x8) | octet 2 octet 3 |
| UE policy section management list contents (x8) | octet 4 octet z |
<!-- /table -->

Figure D.6.2.1: UE policy section management list information element

<!-- table -->
| 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |  |
| UE policy section management sublist (PLMN 1) (x8) | octet 4 octet a |
| UE policy section management sublist (PLMN 2) (x8) | octet (a+1)* octet b* |
| … (x8) | octet (b+1)* … octet c* |
| UE policy section management sublist (PLMN N) (x8) | octet (c+1)* octet z* |
<!-- /table -->

Figure D.6.2.2: UE policy section management list contents

<!-- table -->
| 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |  |
| Length of UE policy section management sublist (x8) | octet d octet d+1 |
|  | MCC digit 1 (x4) | octet d+2 |
| MCC digit 2 (x4) |
|  | MCC digit 3 (x4) | octet d+3 |
| MNC digit 3 (x4) |
|  | MNC digit 1 (x4) | octet d+4 |
| MNC digit 2 (x4) |
| UE policy section management sublist contents (x8) | octet d+5 octet y |
<!-- /table -->

Figure D.6.2.3: UE policy section management sublist

<!-- table -->
| 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |  |
| Instruction 1 (x8) | octet d+5 octet e |
| Instruction 2 (x8) | octet (e+1)* octet f* |
| … (x8) | octet (f+1)* … octet g* |
| Instruction N (x8) | octet (g+1)* octet e* |
<!-- /table -->

Figure D.6.2.4: UE policy section management sublist contents

<!-- table -->
| 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |  |
| Instruction contents length (x8) | octet d+5 octet d+6 |
| UPSC (x8) | octet d+7 octet d+8 |
| UE policy section contents (x8) | octet (d+9)* octet k* |
<!-- /table -->

Figure D.6.2.5: Instruction

<!-- table -->
| 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |  |
| UE policy part 1 (x8) | octet l octet m |
| UE policy part 2 (x8) | octet (m+1)* octet n* |
| … (x8) | octet (n+1)* … octet o* |
| UE policy part N (x8) | octet (o+1)* octet p* |
<!-- /table -->

Figure D.6.2.6: UE policy section contents

<!-- table -->
| 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |  |
| UE policy part contents length (x8) | octet q octet q+1 |
| 0 | 0 | 0 | 0 | UE policy part type (x4) | octet q+2 |
| Spare (x4) |
| UE policy part contents (x8) | octet q+3 octet r |
<!-- /table -->

Figure D.6.2.7: UE policy part

Table D.6.2.1: UE policy section management list information element

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |     |     |          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|-----|----------|
| Value part of the UE policy section management list information element (octets 4 to z)                                                                                                                                                                                                                                                                                                                                                                                        |     |     |     |          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |     |     |          |
| The value part of the UE policy section management list information element consists of one or several UE policy section management sublists.                                                                                                                                                                                                                                                                                                                                  |     |     |     |          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |     |     |          |
| UE policy section management sublist:                                                                                                                                                                                                                                                                                                                                                                                                                                          |     |     |     |          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |     |     |          |
| Length of UE policy section management sublist (octets d to d+1)                                                                                                                                                                                                                                                                                                                                                                                                               |     |     |     |          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |     |     |          |
| This field contains the binary encoding of the length of the UE policy section management sublist in units of octets.                                                                                                                                                                                                                                                                                                                                                          |     |     |     |          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |     |     |          |
| MCC, Mobile country code (octet d+2, and bits 4 to 1 of octet d+3)                                                                                                                                                                                                                                                                                                                                                                                                             |     |     |     |          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |     |     |          |
| The MCC field is coded as in ITU-T Recommendation E.212 \[42\], annex A.                                                                                                                                                                                                                                                                                                                                                                                                       |     |     |     |          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |     |     |          |
| MNC, Mobile network code (bits 8 to 5 of octet d+3, and octet d+4)                                                                                                                                                                                                                                                                                                                                                                                                             |     |     |     |          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |     |     |          |
| The coding of this field is the responsibility of each administration but BCD coding shall be used. The MNC shall consist of 2 or 3 digits. If a network operator decides to use only two digits in the MNC, MNC digit 3 shall be coded as "1111". (NOTE 1)                                                                                                                                                                                                                    |     |     |     |          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |     |     |          |
| UE policy section management sublist contents (octets d+5 to y)                                                                                                                                                                                                                                                                                                                                                                                                                |     |     |     |          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |     |     |          |
| The UE policy section management sublist contents consist of one or several instructions.                                                                                                                                                                                                                                                                                                                                                                                      |     |     |     |          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |     |     |          |
| Instruction:                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |     |     |     |          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |     |     |          |
| Instruction contents length (octets d+5 to d+6)                                                                                                                                                                                                                                                                                                                                                                                                                                |     |     |     |          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |     |     |          |
| This field contains the binary encoding of the instruction contents length in units of octets.                                                                                                                                                                                                                                                                                                                                                                                 |     |     |     |          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |     |     |          |
| UPSC (octets d+7 to d+8)                                                                                                                                                                                                                                                                                                                                                                                                                                                       |     |     |     |          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |     |     |          |
| This field contains the binary encoding of the UPSC. The value of the UPSC is set by the PCF.                                                                                                                                                                                                                                                                                                                                                                                  |     |     |     |          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |     |     |          |
| UE policy section contents (octets d+9 to k)                                                                                                                                                                                                                                                                                                                                                                                                                                   |     |     |     |          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |     |     |          |
| The UE policy section contents consist of one or several UE policy parts.                                                                                                                                                                                                                                                                                                                                                                                                      |     |     |     |          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |     |     |          |
| UE policy part:                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |     |     |          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |     |     |          |
| UE policy part contents length (octets q to q+1)                                                                                                                                                                                                                                                                                                                                                                                                                               |     |     |     |          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |     |     |          |
| This field contains the binary encoding of the UE policy part contents length in units of octets (NOTE 2).                                                                                                                                                                                                                                                                                                                                                                     |     |     |     |          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |     |     |          |
| UE policy part type (bits 4 to 1 of octet q+2)                                                                                                                                                                                                                                                                                                                                                                                                                                 |     |     |     |          |
| Bits                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |     |     |     |          |
| 4                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 3   | 2   | 1   |          |
| 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 0   | 0   | 0   | Reserved |
| 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 0   | 0   | 1   | URSP     |
| 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 0   | 1   | 0   | ANDSP    |
| 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 0   | 1   | 1   | V2XP     |
| 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 1   | 0   | 0   | ProSeP   |
| 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 1   | 0   | 1   | A2XP     |
| 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 1   | 1   | 0   | RSLPP    |
| All other values are reserved.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |     |     |     |          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |     |     |          |
| Bits 8 to 5 of octet q+2 are spare and shall be coded as zero.                                                                                                                                                                                                                                                                                                                                                                                                                 |     |     |     |          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |     |     |          |
| UE policy part contents (octets q+3 to r)                                                                                                                                                                                                                                                                                                                                                                                                                                      |     |     |     |          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |     |     |          |
| This field contains a UE policy part encoded as specified in 3GPP TS 24.526 \[19\] for the UE policy part type field set to "URSP" or "ANDSP", in 3GPP TS 24.588 \[19C\] for the UE policy part type field set to "V2XP", in 3GPP TS 24.555 \[19F\] for the UE policy part type field set to "ProSeP" and in 3GPP TS 24.514 \[62\] for the UE policy part type field set to "RSLPP" and in 3GPP TS 24.578 \[61\] for the UE policy part type field set to "A2XP" respectively. |     |     |     |          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |     |     |          |
| NOTE 1: When the PCF is in an SNPN, the PCF shall include the PLMN ID part of the SNPN identity in the UE policy section management sublist.                                                                                                                                                                                                                                                                                                                                   |     |     |     |          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |     |     |          |
| NOTE 2: The UE policy part contents length indicates the length of the value part of the UE policy part field (i.e. octet q+2 to octet r).                                                                                                                                                                                                                                                                                                                                     |     |     |     |          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |     |     |          |

## D.6.3 UE policy section management result

The purpose of the UE policy section management result information element is to transfer from the UE to the PCF information about instructions for UE policy section management which the UE could not execute successfully.

The UE policy section management result information element is coded as shown in figure D.6.3.1, figure D.6.3.2, figure D.6.3.3, figure D.6.3.4, figure D.6.3.5 and table D.6.3.1.

The UE policy section management result information element has a minimum length of 12 octets and a maximum length of 65534 octets.

<!-- table -->
| 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |  |
| UE policy section management result IEI (x8) | octet 1 |
| Length of UE policy section management result contents (x8) | octet 2 octet 3 |
| UE policy section management result contents (x8) | octet 4 octet z |
<!-- /table -->

Figure D.6.3.1: UE policy section management result information element

<!-- table -->
| 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |  |
| UE policy section management subresult (PLMN 1) (x8) | octet 4 octet a |
| UE policy section management subresult (PLMN 2) (x8) | octet (a+1)* octet b* |
| … (x8) | octet (b+1)* … octet c* |
| UE policy section management subresult (PLMN N) (x8) | octet (c+1)* octet z* |
<!-- /table -->

Figure D.6.3.2: UE policy section management result contents

<!-- table -->
| 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |  |
| Number of results (x8) | octet d |
|  | MCC digit 1 (x4) | octet d+1 |
| MCC digit 2 (x4) |
|  | MCC digit 3 (x4) | octet d+2 |
| MNC digit 3 (x4) |
|  | MNC digit 1 (x4) | octet d+3 |
| MNC digit 2 (x4) |
| UE policy section management subresult contents (x8) | octet d+4 octet y |
<!-- /table -->

Figure D.6.3.3: UE policy section management subresult

<!-- table -->
| 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |  |
| Result 1 (x8) | octet d+4 octet d+8 |
| Result 2 (x8) | octet (d+9)* octet (d+13)* |
| … (x8) | Octet (d+14)* … octet e* |
| Result N (x8) | Octet (e+1)* octet (e+5)* |
<!-- /table -->

Figure D.6.3.4: UE policy section management subresult contents

<!-- table -->
| 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |  |
| UPSC (x8) | octet f octet f+1 |
| Failed instruction order (x8) | octet f+2 octet f+3 |
| Cause (x8) | octet f+4 |
<!-- /table -->

Figure D.6.3.5: Result

Table D.6.3.1: UE policy section management result information element

|                                                                                                                                                                                                                                                                                                                                                                                       |     |     |     |     |     |     |     |     |                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----------------------------|
| Value part of the UE policy section management result information element (octets 4 to z)                                                                                                                                                                                                                                                                                             |     |     |     |     |     |     |     |     |                             |
|                                                                                                                                                                                                                                                                                                                                                                                       |     |     |     |     |     |     |     |     |                             |
| The value part of the UE policy section management result information element consists of one or several UE policy section management subresults.                                                                                                                                                                                                                                     |     |     |     |     |     |     |     |     |                             |
|                                                                                                                                                                                                                                                                                                                                                                                       |     |     |     |     |     |     |     |     |                             |
|                                                                                                                                                                                                                                                                                                                                                                                       |     |     |     |     |     |     |     |     |                             |
| UE policy section management subresult:                                                                                                                                                                                                                                                                                                                                               |     |     |     |     |     |     |     |     |                             |
|                                                                                                                                                                                                                                                                                                                                                                                       |     |     |     |     |     |     |     |     |                             |
| Number of results (octet d)                                                                                                                                                                                                                                                                                                                                                           |     |     |     |     |     |     |     |     |                             |
|                                                                                                                                                                                                                                                                                                                                                                                       |     |     |     |     |     |     |     |     |                             |
| This field contains the binary encoding of number of results included in the UE policy section management subresult.                                                                                                                                                                                                                                                                  |     |     |     |     |     |     |     |     |                             |
|                                                                                                                                                                                                                                                                                                                                                                                       |     |     |     |     |     |     |     |     |                             |
| MCC, Mobile country code (octet d+1, and bits 4 to 1 of octet d+2)                                                                                                                                                                                                                                                                                                                    |     |     |     |     |     |     |     |     |                             |
|                                                                                                                                                                                                                                                                                                                                                                                       |     |     |     |     |     |     |     |     |                             |
| The MCC field is coded as in ITU-T Recommendation E.212 \[42\], annex A.                                                                                                                                                                                                                                                                                                              |     |     |     |     |     |     |     |     |                             |
|                                                                                                                                                                                                                                                                                                                                                                                       |     |     |     |     |     |     |     |     |                             |
| MNC, Mobile network code (bits 8 to 5 of octet d+2, and octet d+3)                                                                                                                                                                                                                                                                                                                    |     |     |     |     |     |     |     |     |                             |
|                                                                                                                                                                                                                                                                                                                                                                                       |     |     |     |     |     |     |     |     |                             |
| The coding of this field is the responsibility of each administration but BCD coding shall be used. The MNC shall consist of 2 or 3 digits. If a network operator decides to use only two digits in the MNC, MNC digit 3 shall be coded as "1111". (NOTE)                                                                                                                             |     |     |     |     |     |     |     |     |                             |
|                                                                                                                                                                                                                                                                                                                                                                                       |     |     |     |     |     |     |     |     |                             |
| UE policy section management subresult contents (octets d+4 to y)                                                                                                                                                                                                                                                                                                                     |     |     |     |     |     |     |     |     |                             |
| The UE policy section management subresult contents consist of one or several results.                                                                                                                                                                                                                                                                                                |     |     |     |     |     |     |     |     |                             |
|                                                                                                                                                                                                                                                                                                                                                                                       |     |     |     |     |     |     |     |     |                             |
| Result (octet f to f+4)                                                                                                                                                                                                                                                                                                                                                               |     |     |     |     |     |     |     |     |                             |
|                                                                                                                                                                                                                                                                                                                                                                                       |     |     |     |     |     |     |     |     |                             |
| UPSC (octet f to f+1)                                                                                                                                                                                                                                                                                                                                                                 |     |     |     |     |     |     |     |     |                             |
|                                                                                                                                                                                                                                                                                                                                                                                       |     |     |     |     |     |     |     |     |                             |
| This field contains the binary encoding of the UPSC. The value of the UPSC is set by the PCF                                                                                                                                                                                                                                                                                          |     |     |     |     |     |     |     |     |                             |
|                                                                                                                                                                                                                                                                                                                                                                                       |     |     |     |     |     |     |     |     |                             |
| Failed instruction order (octets f+2 to f+3)                                                                                                                                                                                                                                                                                                                                          |     |     |     |     |     |     |     |     |                             |
|                                                                                                                                                                                                                                                                                                                                                                                       |     |     |     |     |     |     |     |     |                             |
| This field contains the binary encoding of the order of the instruction in the UE policy section management sublist contents as specified in Figure D.6.2.4, which could not be executed successfully. The value of failed instruction order set to one indicates that the first instruction in the UE policy section management sublist contents could not be executed successfully. |     |     |     |     |     |     |     |     |                             |
|                                                                                                                                                                                                                                                                                                                                                                                       |     |     |     |     |     |     |     |     |                             |
| Cause (octet f+4)                                                                                                                                                                                                                                                                                                                                                                     |     |     |     |     |     |     |     |     |                             |
| Bits                                                                                                                                                                                                                                                                                                                                                                                  |     |     |     |     |     |     |     |     |                             |
| 8                                                                                                                                                                                                                                                                                                                                                                                     | 7   | 6   | 5   | 4   | 3   | 2   | 1   |     |                             |
| 0                                                                                                                                                                                                                                                                                                                                                                                     | 1   | 1   | 0   | 1   | 1   | 1   | 1   |     | Protocol error, unspecified |
| The receiving entity shall treat any other value as 0110 1111, "Protocol error, unspecified".                                                                                                                                                                                                                                                                                         |     |     |     |     |     |     |     |     |                             |
| NOTE: The UE operating in the SNPN access operation mode shall include the PLMN ID part of the SNPN identity of the SNPN in the UE policy section management subresult.                                                                                                                                                                                                               |     |     |     |     |     |     |     |     |                             |
|                                                                                                                                                                                                                                                                                                                                                                                       |     |     |     |     |     |     |     |     |                             |

## D.6.4 UPSI list

The purpose of the UPSI list information element is to transfer from the UE to the PCF a list of UPSIs.

The UPSI list information element is coded as shown in figure D.6.4.1, figure D.6.4.2, and table D.6.4.1.

The UPSI list information element has a minimum length of 3 octets and a maximum length of 65532 octets.

NOTE: A PCF implementing a previous version of the present specification will expect the UPSI list information element to have a minimum length of 10 octets and could be unable to decode a UPSI list information element with a length of 3 octets i.e. a UPSI list information element not containing any UPSI.

<!-- table -->
| 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |  |
| UPSI list IEI (x8) | octet 1 |
| Length of UPSI list contents (x8) | octet 2 octet 3 |
| UPSI sublist (PLMN 1) (x8) | octet 4* octet a* |
| UPSI sublist (PLMN 2) (x8) | octet a+1* octet b* |
| … (x8) | octet b+1* octet c* |
| UPSI sublist (PLMN N) (x8) | octet c+1* octet z* |
<!-- /table -->

Figure D.6.4.1: UPSI list information element

<!-- table -->
| 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |  |
| Length of UPSI sublist (x8) | octet d octet d+1 |
| MCC digit 2 (x4) | MCC digit 1 (x4) | octet d+2 |
| MNC digit 3 (x4) | MCC digit 3 (x4) | octet d+3 |
| MNC digit 2 (x4) | MNC digit 1 (x4) | octet d+4 |
| UPSC 1 (x8) | octet d+5 octet d+6 |
| UPSC 2 (x8) | octet d+7* octet d+8* |
| … (x8) | octet d+9* octet e* |
| UPSC M (x8) | octet e+1* octet e+2* |
<!-- /table -->

Figure D.6.4.2: UPSI sublist

Table D.6.4.1: UPSI list information element

<!-- table -->
| Length of UPSI list contents (octets 2 to 3) |
| This field indicates the length of the UPSI list contents. If no UPSIs are included in the UPSI list, the UE shall set the length of UPSI list contents to zero. |
| MCC, Mobile country code (octet d+2, and bits 4 to 1 of octet d+3) |
| The MCC field is coded as in ITU-T Recommendation E.212 [42], annex A. |
| MNC, Mobile network code (bits 8 to 5 of octet d+3, and octet d+4) |
| The coding of this field is the responsibility of each administration but BCD coding shall be used. The MNC shall consist of 2 or 3 digits. If a network operator decides to use only two digits in the MNC, MNC digit 3 shall be coded as "1111". (NOTE) |
| UPSC (octets d+5 to d+6) |
| This field contains the binary encoding of the UPSC. The value of the UPSC is set by the PCF. |
| NOTE: The UE operating in the SNPN access operation mode shall include the PLMN ID part of the SNPN identity in the UPSI sublist. |
<!-- /table -->

## D.6.5 UE policy classmark

The purpose of the UE policy classmark information element is to provide the network with information about the policy aspects of the UE.

The UE policy classmark information element is coded as shown in figure D.6.5.1 and table D.6.5.1.

The UE policy classmark is a type 4 information element with a minimum length of 3 octets and a maximum length of 5 octets.

<!-- table -->
| 8 (x2) | 7 (x2) | 6 (x2) | 5 (x2) | 4 (x2) | 3 (x2) | 2 (x2) | 1 (x2) |  |
| Policy information IEI (x16) | octet 1 (x2) |
| Length of Policy information contents (x16) | octet 2 (x2) |
| 0 Spare (x2) | 0 Spare (x2) | 0 Spare (x2) | 0 Spare (x2) | SupportRURE (x2) | SVPSU (x2) | EPSURSP (x2) | SupportANDSP (x2) | octet 3 (x2) |
| 0 (x2) | 0 (x2) | 0 (x2) | 0 (x2) | 0 (x2) | 0 (x2) | 0 (x2) | 0 (x2) | octet 4* -5* (x2) |
| Spare (x16) |
<!-- /table -->

Figure D.6.5.1: UE policy classmark information element

Table D.6.5.1: UE policy classmark information element

<!-- table -->
| Support of ANDSP by the UE (SupportANDSP) (octet 3, bit 1) (x2) |
| Bit (x2) |
| 1 |  |
| 0 | ANDSP not supported by the UE |
| 1 | ANDSP supported by the UE |
| Support of URSP provisioning in EPS by the UE (EPSURSP) (octet 3, bit 2) (see NOTE) (x2) |
| Bit (x2) |
| 2 |  |
| 0 | URSP provisioning in EPS not supported by the UE |
| 1 | URSP provisioning in EPS supported by the UE |
| Support of VPS URSP (SVPSU) (octet 3, bit 3) (x2) |
| Bit (x2) |
| 3 |  |
| 0 | VPS URSP not supported by the UE |
| 1 | VPS URSP supported by the UE |
| Support of Reporting URSP Rule Enforcement by the UE (SupportRURE) (octet 3, bit 4) Bit (x2) |
| 4 |  |
| 0 | Reporting URSP rule enforcement not supported by the UE |
| 1 | Reporting URSP rule enforcement supported by the UE |
| All other bits in octet 3 to 5 are spare and shall be coded as zero, if the respective octet is included in the information element. (x2) |
| NOTE: This indicator shall be ignored by an EPS receiving entity as the UE in EPS providing UE STATE INDICATION message, supports URSP provisioning in EPS. (x2) |
<!-- /table -->

## D.6.6 UE OS Id

The purpose of the UE OS Id information element is to provide the network with information about the OS of the UE.

The UE OS Id information element is coded as shown in figure D.6.6.1 and table D.6.6.1.

The UE OS Id is a type 4 information element with a minimum length of 18 octet and a maximum length of 242 octets.

| 8                                    | 7   | 6   | 5   | 4   | 3   | 2   | 1   |     |                     |     |
|--------------------------------------|-----|-----|-----|-----|-----|-----|-----|-----|---------------------|-----|
| OS Id IEI                            |     |     |     |     |     |     |     |     | octet 1             |     |
| Length of OS Id information contents |     |     |     |     |     |     |     |     | octet 2             |     |
| OS Id_1                              |     |     |     |     |     |     |     |     | octets 3 - 18       |     |
| …                                    |     |     |     |     |     |     |     |     |  …                  |     |
| OS Id_15                             |     |     |     |     |     |     |     |     | octets 227\* -242\* |     |

Figure D.6.6.1: UE OS Id information element

Table D.6.6.1: UE OS Id information element

| OS Id:                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The OS Id is coded as a sequence of a sixteen octet OS Id value field. The OS Id value field is defined as Universally Unique IDentifier (UUID) as specified in IETF RFC 4122 \[35A\]. |

## D.6.7 UE policy network classmark

The purpose of the UE policy network classmark information element is to provide the UE with information about the policy aspects of the network.

The UE policy network classmark information element is coded as shown in figure D.6.7.1 and table D.6.7.1.

The UE policy network classmark is a type 4 information element with a minimum length of 3 octets and a maximum length of 5 octets.

<!-- table -->
| 8 (x2) | 7 (x2) | 6 (x2) | 5 (x2) | 4 (x2) | 3 (x2) | 2 (x2) | 1 (x2) |  |
| UE policy network classmark IEI (x16) | octet 1 (x2) |
| Length of UE policy network classmark contents (x16) | octet 2 (x2) |
| 0 Spare (x2) | 0 Spare (x2) | 0 Spare (x2) | 0 Spare (x2) | 0 Spare (x2) | 0 Spare (x2) | 0 Spare (x2) | NSSUI (x2) | octet 3 (x2) |
| 0 (x2) | 0 (x2) | 0 (x2) | 0 (x2) | 0 (x2) | 0 (x2) | 0 (x2) | 0 (x2) | octet 4* -5* (x2) |
| Spare (x16) |
<!-- /table -->

Figure D.6.7.1: UE policy network classmark information element

Table D.6.7.1: UE policy network classmark information element

| Non-subscribed SNPN signalled URSP handling indication (NSSUI) (octet 3, bit 1) (see NOTE)                                                                                                                                                                                                                                            |     |                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|--------------------------------------------------------------------|
| Bits                                                                                                                                                                                                                                                                                                                                  |     |                                                                    |
| 1                                                                                                                                                                                                                                                                                                                                     |     |                                                                    |
| 0                                                                                                                                                                                                                                                                                                                                     |     | UE is allowed to accept URSP signalled by non-subscribed SNPNs     |
| 1                                                                                                                                                                                                                                                                                                                                     |     | UE is not allowed to accept URSP signalled by non-subscribed SNPNs |
|                                                                                                                                                                                                                                                                                                                                       |     |                                                                    |
| All other bits in octet 3 to 5 are spare and shall be coded as zero, if the respective octet is included in the information element.                                                                                                                                                                                                  |     |                                                                    |
| NOTE: Receiving UE shall ignore this bit, if i) UE has an empty or non-present EHPLMN list and the bit is received from the RPLMN which is not the HPLMN, ii) UE has non-empty EHPLMN list and the bit is received from the RPLMN which is not an EHPLMN or iii) the bit is received from the RSNPN which is not the subscribed SNPN. |     |                                                                    |

## D.6.8 VPS URSP configuration

The purpose of the VPS URSP configuration information element is to transfer the VPS URSP configuration from the PCF to the UE. The VPS URSP configuration contains zero or more tuples. Each tuple contains the tuple ID identifying the tuple, the network descriptor identifying one or more VPLMNs, and zero or more UPSCs of HPLMN's UE policy sections which contain solely one or more UE policy parts with the UE policy part type set to "URSP", such that the URSP rules in those one or more UE policy parts are applicable to the VPLMN and its equivalent PLMN.

The VPS URSP configuration information element is coded as shown in figure D.6.8.1, figure D.6.8.2, figure D.6.8.3, figure D.6.8.4, figure D.6.8.5, figure D.6.8.6, figure D.6.8.7, figure D.6.8.8, figure D.6.8.9, and table D.6.8.1.

The VPS URSP configuration is type 6 information element with a minimum length of 3 octets and a maximum length of 65533 octets.

<!-- table -->
| 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |  |
| VPS URSP configuration IEI (x8) | octet 1 |
| Length of VPS URSP configuration contents (x8) | octet 2 octet 3 |
| 0 Spare | 0 Spare | 0 Spare | 0 Spare | 0 Spare | 0 Spare | RT (x2) | octet 4 |
| Tuple 1 (x8) | octet 5* octet a* |
| Tuple 2 (x8) | octet (a+1)* octet b* |
| … (x8) | octet (b+1)* octet c* |
| Tuple N (x8) | octet (c+1)* octet z* |
<!-- /table -->

Figure D.6.8.1: VPS URSP configuration information element

<!-- table -->
| 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |  |
| Length of tuple contents (x8) | octet a+1 octet a+2 |
| Tuple ID (x8) | octet a+3 |
| Network descriptor (x8) | octet a+4 octet e |
| UPSC 1 (x8) | octet (e+1)* octet (e+2)* |
| UPSC 2 (x8) | octet (e+3)* octet (e+4)* |
| … (x8) | octet (e+5)* octet (e+n*2e-2)* |
| UPSC n (x8) | octet (e+n*2-1)* octet (e+n*2)* = octet b* |
<!-- /table -->

Figure D.6.8.2: Tuple

<!-- table -->
| 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |  |
| Number of network descriptor entries (x8) | octet a+4 |
| Network descriptor entry 1 (x8) | octet (a+5) octet f |
| Network descriptor entry 2 (x8) | octet (f+1)* octet g* |
| ... (x8) | octet (g+1)* octet h* |
| Network descriptor entry m (x8) | octet (h+1)* octet e* |
<!-- /table -->

Figure D.6.8.3: Network descriptor

<!-- table -->
| 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |  |
| Network descriptor entry type (x8) | octet f+1 |
| Network descriptor entry value (x8) | octet (f+2)* octet g* |
<!-- /table -->

Figure D.6.8.4: Network descriptor entry

<!-- table -->
| 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |  |
| Number of PLMN IDs (x8) | octet (f+2) |
| PLMN ID 1 (x8) | octet (f+3) octet (f+5) |
| PLMN ID 2 (x8) | octet (f+6)* octet (f+8)* |
| ... (x8) |  |
| PLMN ID m (x8) | octet (m*3+f)* octet (m*3+f+2)* = octet g* |
<!-- /table -->

Figure D.6.8.5: Network descriptor entry value for network descriptor entry type set to "one or more VPLMNs"

|             |             |           |
|-------------|-------------|-----------|
| MCC digit 2 | MCC digit 1 | octet f+6 |
| MNC digit 3 | MCC digit 3 | octet f+7 |
| MNC digit 2 | MNC digit 1 | octet f+8 |

Figure D.6.8.6: PLMN ID

<!-- table -->
| 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |  |
| Number of MCCs (x8) | octet (f+2) |
| MCC pair 1 (x8) | octet (f+3) octet (f+5) |
| MCC pair 2 (x8) | octet (f+6)* octet (f+8)* |
| ... (x8) |  |
| MCC pair m (x8) | octet (m*3+f)* octet (m*3+f+2)* |
| Odd MCC (x8) | octet (m*3+f+3)* octet (m*3+f+4)* = octet g* |
<!-- /table -->

Figure D.6.8.7: Network descriptor entry value for network descriptor entry type set to "one or more MCCs"

|               |               |           |
|---------------|---------------|-----------|
| MCC 1 digit 2 | MCC 1 digit 1 | octet f+6 |
| MCC 2 digit 3 | MCC 1 digit 3 | octet f+7 |
| MCC 2 digit 2 | MCC 2 digit 1 | octet f+8 |

Figure D.6.8.8: MCC pair

<!-- table -->
| MCC digit 2 (x4) | MCC digit 1 | octet (m*3+f+3) |
| 0 Spare | 0 Spare | 0 Spare | 0 Spare | MCC digit 3 | octet (m*3+f+4) = octet g |
<!-- /table -->

Figure D.6.8.9: Odd MCC

Table D.6.8.1: VPS URSP configuration information element

| Replacement type (octet 4, bits 1 and 2)                                                                                                                                                                                                                                                                                        |       |       |       |       |                       |       |       |     |                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|-------|-------|-------|-----------------------|-------|-------|-----|--------------------|
| Bits                                                                                                                                                                                                                                                                                                                            |       |       |       |       |                       |       |       |     |                    |
| **2**                                                                                                                                                                                                                                                                                                                           | **1** |       |       |       |                       |       |       |     |                    |
| 0                                                                                                                                                                                                                                                                                                                               | 1     |       |       |       | per-tuple replacement |       |       |     |                    |
| 1                                                                                                                                                                                                                                                                                                                               | 0     |       |       |       | full list of tuples   |       |       |     |                    |
| All other values are reserved.                                                                                                                                                                                                                                                                                                  |       |       |       |       |                       |       |       |     |                    |
|                                                                                                                                                                                                                                                                                                                                 |       |       |       |       |                       |       |       |     |                    |
| Tuple ID (octet a+3)                                                                                                                                                                                                                                                                                                            |       |       |       |       |                       |       |       |     |                    |
| This field contains the binary encoding of the tuple ID. The value of the tuple ID is set by the PCF.                                                                                                                                                                                                                           |       |       |       |       |                       |       |       |     |                    |
|                                                                                                                                                                                                                                                                                                                                 |       |       |       |       |                       |       |       |     |                    |
| Network descriptor entry type (octet f+1)                                                                                                                                                                                                                                                                                       |       |       |       |       |                       |       |       |     |                    |
| Bits                                                                                                                                                                                                                                                                                                                            |       |       |       |       |                       |       |       |     |                    |
| **8**                                                                                                                                                                                                                                                                                                                           | **7** | **6** | **5** | **4** | **3**                 | **2** | **1** |     |                    |
| 0                                                                                                                                                                                                                                                                                                                               | 0     | 0     | 0     | 0     | 0                     | 0     | 1     |     | one or more VPLMNs |
| 0                                                                                                                                                                                                                                                                                                                               | 0     | 0     | 0     | 0     | 0                     | 1     | 0     |     | one or more MCCs   |
| 0                                                                                                                                                                                                                                                                                                                               | 0     | 0     | 0     | 0     | 0                     | 1     | 1     |     | any VPLMN          |
| All other values are reserved.                                                                                                                                                                                                                                                                                                  |       |       |       |       |                       |       |       |     |                    |
|                                                                                                                                                                                                                                                                                                                                 |       |       |       |       |                       |       |       |     |                    |
| If the network descriptor entry type field is set to "one or more VPLMNs" or "one or more MCCs", then the network descriptor entry value field is present. If the network descriptor entry type field is set to "any VPLMN", then the network descriptor entry value field is absent.                                           |       |       |       |       |                       |       |       |     |                    |
|                                                                                                                                                                                                                                                                                                                                 |       |       |       |       |                       |       |       |     |                    |
| Number of PLMN IDs (octet (f+2) of the network descriptor entry value for network descriptor entry type set to "one or more VPLMNs")                                                                                                                                                                                            |       |       |       |       |                       |       |       |     |                    |
| The number of PLMN IDs field indicates the number of the PLMN IDs in the network descriptor entry value field.                                                                                                                                                                                                                  |       |       |       |       |                       |       |       |     |                    |
|                                                                                                                                                                                                                                                                                                                                 |       |       |       |       |                       |       |       |     |                    |
| MCC, Mobile country code (octet f+6 and bits 4 to 1 of octet f+7 of the PLMN ID, octet f+6 and bits 4 to 1 of octet f+7 of the MCC pair, and octet f+8 and bits 8 to 5 of octet f+7 of the MCC pair, octet m\*3+f+3 and bits 4 to 1 of m\*3+f+4 of the odd MCC)                                                                 |       |       |       |       |                       |       |       |     |                    |
| The MCC field is coded as in ITU-T Recommendation E.212 \[42\], annex A.                                                                                                                                                                                                                                                        |       |       |       |       |                       |       |       |     |                    |
|                                                                                                                                                                                                                                                                                                                                 |       |       |       |       |                       |       |       |     |                    |
| MNC, Mobile network code (bits 8 to 5 of octet f+7, and octet f+8)                                                                                                                                                                                                                                                              |       |       |       |       |                       |       |       |     |                    |
| The coding of this field is the responsibility of each administration but BCD coding shall be used. The MNC shall consist of 2 or 3 digits. If a network operator decides to use only two digits in the MNC, MNC digit 3 shall be coded as "1111".                                                                              |       |       |       |       |                       |       |       |     |                    |
|                                                                                                                                                                                                                                                                                                                                 |       |       |       |       |                       |       |       |     |                    |
| Number of MCCs (octet (f+2) of the network descriptor entry value for network descriptor entry type set to "one or more MCCs")                                                                                                                                                                                                  |       |       |       |       |                       |       |       |     |                    |
| The number of MCCs field indicates the number of the MCCs in the network descriptor entry value field. If the number of MCCs field is an odd value, then the odd MCC field is present otherwise the odd MCC field is absent.                                                                                                    |       |       |       |       |                       |       |       |     |                    |
|                                                                                                                                                                                                                                                                                                                                 |       |       |       |       |                       |       |       |     |                    |
| UPSC (octets e+3 to e+4)                                                                                                                                                                                                                                                                                                        |       |       |       |       |                       |       |       |     |                    |
| This field contains the binary encoding of the UPSC of an UPSI of a UE policy section of the HPLMN (see NOTE), which contains solely one or more UE policy parts with the UE policy part type set to "URSP", such that the URSP rules in those one or more UE policy parts are applicable to the VPLMN and its equivalent PLMN. |       |       |       |       |                       |       |       |     |                    |
|                                                                                                                                                                                                                                                                                                                                 |       |       |       |       |                       |       |       |     |                    |
| NOTE: PLMN ID of the UPSI is not indicated.                                                                                                                                                                                                                                                                                     |       |       |       |       |                       |       |       |     |                    |
