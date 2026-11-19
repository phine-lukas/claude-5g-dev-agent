# B.1 CP Selection Function

## B.1.1 General

The SGW-C and PGW-C selection function shall follow the principles specified in 3GPP TS 29.303 \[25\] for the SGW and PGW selection functions without Control and User Plane Separation.

The following additional considerations apply with Control and User Plane Separation:

1\. At most one SGW-C shall be selected per user at any time.

2\. The service area of an SGW-C function shall be aligned with the service area of the corresponding SGW-U functions (see clause 4.3.4 of 3GPP TS 23.214 \[2\]. All the SGW-U functions in the service area shall have a full meshed connectivity with all the eNBs of TAs and/or all RNCs/BSCs of RAs served by that service area.

3\. The SGW dynamic load reported to the MME/SGSN and the PGW dynamic load reported to the MME/SGSN or TWAN/ePDG should take into account the operating status of the CP and UP functions' resources that the SGW-C/PGW-C is controlling. See clause 6.2.3 for how the CP function obtains load control information from the UP function.

4\. For Dedicated Core Networks (see clause 5.8 of 3GPP TS 29.303 \[25\]), an SGW-C or PGW-C function shall be declared in DNS as dedicated to certain mapped UE usage types if the CP function or if all the UP functions it controls are dedicated to certain mapped UE usage types. In this case, the CP function shall be provisioned in DNS with all the mapped UE usage types that both the CP function and its UP functions support.

5\. The MME/SGSN shall be able to select an SGW-C and a PGW-C optimized for NR, e.g. for UEs indicating support of dual connectivity with NR in NAS signalling to the MME or SGSN and without subscription restriction to use NR as secondary RAT, according to the requirements specified in clause 5.12.2 of 3GPP TS 29.303 \[25\]. The SGW-C and the PGW-C optimized for NR may be a combined SGW-C/PGW-C function optimized for the NR.
