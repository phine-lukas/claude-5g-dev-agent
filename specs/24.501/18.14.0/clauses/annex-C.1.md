# C.1 Storage of 5GMM information for UEs not operating in SNPN access operation mode

The following 5GMM parameters shall be stored on the USIM if the corresponding file or file extension is present:

a\) 5G-GUTI;

b\) last visited registered TAI;

c\) 5GS update status;

d\) 5G NAS security context parameters from a full native 5G NAS security context (see 3GPP TS 33.501 \[24\]);

e\) K<sub>AUSF</sub> and K<sub>SEAF</sub> (see 3GPP TS 33.501 \[24\]);

f\) SOR counter (see clause 9.11.3.51); and

g\) UE parameter update counter (see clause 9.11.3.53A);

The UE may support multiple records of NAS security context storage for multiple registration (see 3GPP TS 31.102 \[22\]). If the UE supports multiple records of NAS security context storage for multiple registration, the first 5G security context of one access shall be stored in record 1 of the 5G NAS Security Context USIM file for that access and the second 5G security context of that access shall be stored in record 2 of the same file. The presence and format of corresponding files on the USIM is specified in 3GPP TS 31.102 \[22\].

If the corresponding file or file extension is not present on the USIM, these 5GMM parameters are stored in a non-volatile memory in the ME together with the SUPI from the USIM. These 5GMM parameters can only be used if the SUPI from the USIM matches the SUPI stored in the non-volatile memory; else the UE shall delete the 5GMM parameters.

Upon power up or when a USIM is inserted if K<sub>AUSF</sub> is stored on the USIM but the SOR counter and the UE parameter update counter are not present on the USIM the UE may delete the K<sub>AUSF</sub> and associated 5G security context that are stored at the USIM and set the KSI value of ngKSI to '111' (see 3GPP TS 33.501 \[24\]).

NOTE: The above handling can be used to prevent a stored CounterSoR and CounterUPU being associated with the wrong KAUSF. Further criteria for deleting the security information are left to the UE implementation.

The following 5GMM parameters shall be stored in a non-volatile memory in the ME together with the SUPI from the USIM:

\- configured NSSAI(s);

\- NSSRG information;

\- S-NSSAI time validity information;

\- S-NSSAI location validity information;

\- on-demand NSSAI;

\- NSSAI inclusion mode(s);

\- MPS indicator;

\- MCS indicator;

\- operator-defined access category definitions;

\- network-assigned UE radio capability IDs;

\- "CAG information list", if the UE supports CAG;

\- signalled URSP (see 3GPP TS 24.526 \[19\]);

\- SOR-CMCI;

\- one or more lists of type "list of PLMN(s) to be used in disaster condition", if the UE supports MINT;

\- disaster roaming wait range, if the UE supports MINT;

\- disaster return wait range, if the UE supports MINT;

\- indication of whether disaster roaming is enabled in the UE;

\- indication of 'applicability of "lists of PLMN(s) to be used in disaster condition" provided by a VPLMN';

\- VPS URSP configuration; and

\- indication of whether interworking without N26 interface is supported.

The following 5GMM parameters should be stored in a non-volatile memory in the ME together with the SUPI from the USIM:

\- allowed NSSAI(s); and

\- partially allowed NSSAI(s).

Each configured NSSAI consists of S-NSSAI(s) stored together with a PLMN identity, if it is associated with a PLMN. The UE shall store the S-NSSAI(s) of the HPLMN. If the UE is in the VPLMN, the UE shall also store the configured NSSAI for the current PLMN and any necessary mapped S-NSSAI(s). The configured NSSAI(s) can only be used if the SUPI from the USIM matches the SUPI stored in the non-volatile memory of the ME; else the UE shall delete the configured NSSAI(s). A configured NSSAI may be associated with NSSRG information, S-NSSAI location validity information, S-NSSAI time validity information, NSAG information and on-demand NSSAI.

Each NSSAI inclusion mode is associated with a PLMN identity and access type. The NSSAI inclusion mode(s) can only be used if the SUPI from the USIM matches the SUPI stored in the non-volatile memory of the ME; else the UE shall delete the NSSAI inclusion mode(s).

The MPS indicator is stored together with a PLMN identity of the PLMN that provided it, and is valid in that RPLMN or equivalent PLMN. The MPS indicator can only be used if the SUPI from the USIM matches the SUPI stored in the non-volatile memory of the ME, else the UE shall delete the MPS indicator.

The MCS indicator is stored together with a PLMN identity of the PLMN that provided it, and is valid in that RPLMN or equivalent PLMN. The MCS indicator can only be used if the SUPI from the USIM matches the SUPI stored in the non-volatile memory of the ME, else the UE shall delete the MCS indicator.

Operator-defined access category definitions are stored together with a PLMN identity of the PLMN that provided them, and is valid in that PLMN or equivalent PLMN. The operator-defined access category definitions can only be used if the SUPI from the USIM matches the SUPI stored in the non-volatile memory of the ME, else the UE shall delete the operator-defined access category definitions. The maximum number of stored operator-defined access category definitions is UE implementation dependent.

Each network-assigned UE radio capability ID is stored together with a PLMN identity of the PLMN that provided it as well as a mapping to the corresponding UE radio configuration, and is valid in that PLMN. A network-assigned UE radio capability ID can only be used if the SUPI from the USIM matches the SUPI stored in the non-volatile memory of the ME, else the UE shall delete the network-assigned UE radio capability ID. The UE shall be able to store at least the last 16 received network-assigned UE radio capability IDs. There shall be only one network-assigned UE radio capability ID stored for a given combination of PLMN identity and UE radio configuration and any existing UE radio capability ID shall be deleted when a new UE radio capability ID is added for the same combination of PLMN identity and UE radio configuration. If the UE receives a network-assigned UE radio capability ID with a Version ID value different from the value included in the network-assigned UE radio capability ID(s) stored at the UE for the serving PLMN, the UE may delete these stored network-assigned UE radio capability ID(s).

The allowed NSSAI(s) can be stored in a non-volatile memory in the ME together with the SUPI from the USIM. Allowed NSSAI consists of S-NSSAI(s) stored together with a PLMN identity, if it is associated with a PLMN. If the allowed NSSAI is stored, then the UE shall store the S-NSSAI(s) of the HPLMN. If the UE is in the VPLMN, the UE shall also store the allowed NSSAI for the serving PLMN and any necessary mapping of the allowed NSSAI for the serving PLMN to the S-NSSAI(s) of the HPLMN. The allowed NSSAI(s) can only be used if the SUPI from the USIM matches the SUPI stored in the non-volatile memory of the ME; else the UE shall delete the allowed NSSAI(s).

The partially allowed NSSAI(s) can be stored as allowed NSSAI(s) in a non-volatile memory in the ME together with the SUPI from the USIM. Partially allowed NSSAI consists of allowed S-NSSAI(s) and for each S-NSSAI a list of TAs for which the S-NSSAI is allowed, together with a PLMN identity.

If the UE is registered for emergency services, the UE shall not store the 5GMM parameters described in this annex on the USIM or in non-volatile memory. Instead the UE shall temporarily store these parameters locally in the ME and the UE shall delete these parameters when the UE is deregistered from emergency services (e.g. before registering for normal service).

If the UE is configured for eCall only mode as specified in 3GPP TS 31.102 \[22\], the UE shall not store the 5GMM parameters described in this annex on the USIM or in non-volatile memory. Instead the UE shall temporarily store these parameters locally in the ME and the UE shall delete these parameters when the UE enters 5GMM-DEREGISTERED.eCALL-INACTIVE state, the UE is switched-off or the USIM is removed.

The "CAG information list" can only be used if the SUPI from the USIM matches the SUPI stored in the non-volatile memory of the ME; else the UE shall delete the "CAG information list".

The handling of the SOR-CMCI stored in the non-volatile memory in the ME is specified in 3GPP TS 23.122 \[5\].

Each "list of PLMN(s) to be used in disaster condition" is stored together with the PLMN identity of the PLMN that provided it. The stored lists of type "list of PLMN(s) to be used in disaster condition" can only be used if the SUPI from the USIM matches the SUPI stored in the non-volatile memory of the ME; else the UE shall delete the lists of type "list of PLMN(s) to be used in disaster condition". The UE shall store at least the "list of PLMN(s) to be used in disaster condition" provided by the HPLMN or EHPLMN. If the 'applicability of "lists of PLMN(s) to be used in disaster condition" provided by a VPLMN' is set to "true", the UE should also store the "list of PLMN(s) to be used in disaster condition" provided by the VPLMN. The maximum number of stored lists of type "list of PLMN(s) to be used in disaster condition" provided by a PLMN other than the HPLMN or EHPLMN is UE implementation dependent.

The disaster roaming wait range can only be used if the SUPI from the USIM matches the SUPI stored in the non-volatile memory of the ME; else the UE shall delete the disaster roaming wait range.

The disaster return wait range can only be used if the SUPI from the USIM matches the SUPI stored in the non-volatile memory of the ME; else the UE shall delete the disaster return wait range.

The indication of whether disaster roaming is enabled in the UE can only be used if the SUPI from the USIM matches the SUPI stored in the non-volatile memory of the ME; else the UE shall delete the indication of whether disaster roaming is enabled in the UE.

The indication of 'applicability of "lists of PLMN(s) to be used in disaster condition" provided by a VPLMN' can only be used if the SUPI from the USIM matches the SUPI stored in the non-volatile memory of the ME; else the UE shall delete the indication of 'applicability of "lists of PLMN(s) to be used in disaster condition" provided by a VPLMN'.
