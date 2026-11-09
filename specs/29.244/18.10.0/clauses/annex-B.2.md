# B.2 UP Selection Function

## B.2.1 General

The following requirements apply for the selection of the UP function:

\- the SGW-C, PGW-C and TDF-C shall be responsible for the selection of the SGW-U, PGW-U and TDF-U respectively;

\- an SGW-C may select different SGW-U functions for different PDN connections of a same user.

It is implementation specific how to support the UP selection function requirements specified in this clause. Clause B.2.6 specifies one possible implementation.

## B.2.2 SGW-U Selection Function

The SGW-C shall be able to select the SGW-U considering the following parameters:

\- the SGW-U location and the user 's location (i.e. ECGI, eNodeB ID or TAI for E-UTRAN, RAI or RNC-ID for UTRAN);

\- the SGW-U's capabilities and the capabilities required for the particular UE session to establish;

\- the mapped UE Usage Type (when dedicating SGW-U to specific Dedicated Core Networks);

\- the SGW-U's dynamic load;

\- the SGW-U's relative static capacity (versus other SGW-Us);

\- the UP Function Selection Information Flags, indicating whether it is desired to select an SGW-U optimized for NR, as specified in 3GPP TS 29.274 \[9\].

Based on local policy, if the user's location information is required to be used for selecting the UP function, the SGW-C shall determine the list of candidate SGW-Us taking into account the user's location (ECGI, eNodeB ID or TAI for E-UTRAN, RAI or RNC-ID for UTRAN).

The SGW-C shall select, among the candidate SGW-U functions, an SGW-U function which supports all the capabilities required for the particular UE session, considering the information received during the PFCP Association Setup.

## B.2.3 PGW-U Selection Function

The PGW-C shall be able to select the PGW-U considering the following parameters:

\- the requested APN for the PDN connection;

\- the PGW-U location and the user 's location;

\- the PGW-U's capabilities and the capabilities required for the particular UE session to establish;

\- the mapped UE Usage Type (when dedicating PGW-U to specific Dedicated Core Networks);

\- the PGW-U's dynamic load;

\- the PGW-U's relative static capacity (versus other PGW-Us);

\- whether a PDN connection already exists for the same UE and APN, in which case the same PGW-U shall be selected (to enable APN-AMBR enforcement);

\- the UP Function Selection Information Flags, indicating whether it is desired to select a PGW-U optimized for NR, as specified in 3GPP TS 29.274 \[9\].

NOTE: The SGW-U and PGW-U location can be configured in the SGW-C and PGW-C or derived from DNS procedures as specified in clause B.2.2.

If the PGW-C already assigned a PGW-U to the UE for the requested APN (e.g. UE with multiple PDN connections to the same APN), the PGW-C shall select the same PGW-U for the new PDN connection.

If a non-null IPv4 address and/or an IPv6 prefix is received in the PDN Address Allocation (PAA) IE in the Create Session Request, e.g. static address assignment in the user subscription, the PGW-C shall select a PGW-U which can support the requested UE's IP address and/or IPv6 prefix.

Otherwise, the PGW-C shall determine the list of candidate PGW-Us taking into account the requested APN.

The PGW-C shall select, among the candidate PGW-U functions, a PGW-U function which supports all the capabilities required for the particular UE session, considering the information received during the PFCP Association Setup.

## B.2.4 Combined SGW-U/PGW-U Selection Function

A Combined SGW-C/PGW-C function shall be able to select a combined SGW-U/PGW-U function. This shall be possible for all the UE's PDN connections, as shown in Figure B.2.1-1.

[figure]

Figure B.2.4-1: SGW-U/PGW-U colocation with Control and User Plane Separation

A combined SGW-C/PGW-C function shall select the SGW-U and PGW-U as defined respectively in B.2.2 and B.2.3, with the following additions:

\- the combined SGW-C/PGW-C function shall select the best couple of SGW-U and PGW-U (e.g. the combined SGW-U/PGW-U function), for the requested APN, among all candidate couples of (SGW-U, PGW-U), instead of selecting independently the SGW-U and the PGW-U.

## B.2.5 TDF-U selection function

The TDF-C shall be able to select the TDF-U as specified in clause 5.12.5 of 3GPP TS 23.214 \[2\].

## B.2.6 UP Selection Function Based on DNS

### B.2.6.1 General

This clause specifies optional DNS procedures to select the SGW-U and PGW-U functions and the requirements which apply when these procedures are supported.

The relative static capacity of an SGW-U and PGW-U may be configured in the DNS.

The Node ID of an SGW-U and PGW-U may take the form of a canonical node name to allow the selection of a SGW-U and PGW-U with the best topological match.

### B.2.6.2 SGW-U Selection Function Based on DNS

The SGW-C shall retrieve the list of candidate SGW-Us using DNS procedures taking into account the user's location (ECGI, eNodeB ID or TAI for E-UTRAN, RAI or RNC-ID for UTRAN), as specified in 3GPP TS 29.303 \[25\].

In non-roaming or LBO scenarios where the PGW-U is already selected (e.g. TAU with SGW change) and when it is preferred to select a collocated node or a topologically closer node, the SGW-C shall try to select an SGW-U collocated with the PGW-U.

### B.2.6.3 PGW-U Selection Function Based on DNS

The PGW-C shall retrieve the list of candidate PGW-Us using DNS procedures taking into account the requested APN, as specified in 3GPP TS 29.303 \[25\].

In non-roaming or LBO scenarios, when it is preferred to select a collocated node or a topologically closer node, i.e. when such preference is indicated in the canonical node names of the PGW-U functions in the DNS (using "topon" as the first label of canonical node name), the PGW-C shall give precedence to collocation of SGW-U and PGW-U, then to topological closeness (i.e. pairs of SGW-U and PGW-U with canonical node names with the highest number of matching labels). This requires the SGW-C to provide the SGW-U Node ID to the PGW-C.

### B.2.6.4 Combined SGW-U/PGW-U Selection Function Based on DNS

A combined SGW-C/PGW-C function shall select the SGW-U and PGW-U as defined respectively in B.2.4, B.2.6.2 and B.2.6.3.

######## Annex C (Informative): Examples scenarios
