# C.2 Storage of 5GMM information for UEs operating in SNPN access operation mode

The 5GMM information for UEs operating in SNPN access operation mode and not registering or registered for the onboarding service in SNPN are stored according to the following conditions:

\- if the UE does not support access to an SNPN using credentials from a credentials holder and equivalent SNPNs, the following 5GMM parameters shall be stored per subscribed SNPN in a non-volatile memory in the ME together with the subscriber identifier associated with the SNPN identity of the SNPN in the "list of subscriber data" configured in the ME (see 3GPP TS 23.122 \[5\]) or with the SUPI from the USIM if no subscriber identifier is configured in the entry of the "list of subscriber data" associated with the SNPN identity and the UE has a valid USIM;and

\- if the UE supports access to an SNPN using credentials from a credentials holder, equivalent SNPNs or both, the following 5GMM parameters shall be stored in a non-volatile memory in the ME per:

i\) the subscribed SNPN together with the subscriber identifier associated with the selected entry in the "list of subscriber data" configured in the ME (see 3GPP TS 23.122 \[5\]) or with the SUPI from the USIM if no subscriber identifier is configured in the selected entry of the "list of subscriber data" configured in the ME and the UE has a valid USIM; or

ii\) if the UE supports access to an SNPN using credentials from a credentials holder, the PLMN subscription together with the SUPI from the USIM which is associated with the PLMN subscription:

a\) 5G-GUTI;a1) NID of the registered SNPN;

b\) last visited registered TAI;

c\) 5GS update status;

d\) 5G NAS security context parameters from a full native 5G NAS security context (see 3GPP TS 33.501 \[24\]);

e\) K<sub>AUSF</sub> and K<sub>SEAF</sub> (see 3GPP TS 33.501 \[24\]);

f\) UE parameter update counter (see clause 9.11.3.53A);

g\) configured NSSAI(s);

g1) NSSRG information;

g2) S-NSSAI time validity information;

g3) S-NSSAI location validity information;

g4) on-demand NSSAI;

h\) NSSAI inclusion mode(s);

i\) MPS indicator;

j\) MCS indicator;

k\) operator-defined access category definitions;

l\) network-assigned UE radio capability IDs;

m\) zero or more instances of signalled URSP (see 3GPP TS 24.526 \[19\]), each associated with a non-subscribed SNPN, the subscribed SNPN or the HPLMN, which provided the URSP;

m1) zero or more instances of pre-configured URSP rules (see 3GPP TS 24.526 \[19\]), each associated with the subscribed SNPN or the HPLMN, which provided the URSP;

n\) optionally a non-subscribed SNPN signalled URSP handling indication indicating whether the UE is allowed to accept URSP signalled by non-subscribed SNPNs;

o\) "permanently forbidden SNPNs" list;

o1) "permanently forbidden SNPNs for access for localized services in SNPN" list;

p\) "temporarily forbidden SNPNs" list;

p1) "temporarily forbidden SNPNs for access for localized services in SNPN" list;

q\) SOR counter (see clause 9.11.3.51);

r\) SOR-CMCI; and

s\) optionally, the SNPN selection parameters associated with the PLMN subscription (see 3GPP TS 23.122 \[5\] clause 4.9.3.0).

The 5GMM information for UEs operating in SNPN access operation mode and registering or registered for the onboarding service in SNPN are stored as follows:

a\) 5G-GUTI;

b\) last visited registered TAI;

c\) 5GS update status;

d\) 5G NAS security context parameters from a full native 5G NAS security context (see 3GPP TS 33.501 \[24\]);

e\) K<sub>AUSF</sub> and K<sub>SEAF</sub> (see 3GPP TS 33.501 \[24\]);

f\) UE parameter update counter (see clause 9.11.3.53A);

g\) network-assigned UE radio capability IDs;

h\) "permanently forbidden SNPNs for onboarding services in SNPN" list; and

i\) "temporarily forbidden SNPNs for onboarding services in SNPN" list.

The 5GMM information for UEs operating in SNPN access operation mode are stored according to the following conditions:

\- if the UE does not support access to an SNPN using credentials from a credentials holder, equivalent SNPNs or both, the following 5GMM parameters should be stored per subscribed SNPN in a non-volatile memory in the ME together with the subscriber identifier associated with the SNPN identity of the SNPN in the "list of subscriber data" configured in the ME (see 3GPP TS 23.122 \[5\]) or with the SUPI from the USIM if no subscriber identifier is configured in the entry of the "list of subscriber data" associated with the SNPN identity and the UE has a valid USIM; and

\- if the UE supports access to an SNPN using credentials from a credentials holder, equivalent SNPNs or both, the following 5GMM parameters should be stored in a non-volatile memory in the ME per:

i\) the subscribed SNPN together with the subscriber identifier associated with the selected entry in the "list of subscriber data" configured in the ME (see 3GPP TS 23.122 \[5\]) or with the SUPI from the USIM if no subscriber identifier is configured in the selected entry of the "list of subscriber data" configured in the ME and the UE has a valid USIM; or

ii\) if the UE supports access to an SNPN using credentials from a credentials holder, the PLMN subscription together with the SUPI from the USIM which is associated with the PLMN subscription:

a\) allowed NSSAI(s).

If the 5GMM parameters are associated with the PLMN subscription, then the 5GMM parameters can only be used if the SUPI from the USIM which is associated with the selected PLMN subscription matches the SUPI stored in the non-volatile memory; else the UE shall delete the 5GMM parameters.

If the 5GMM parameters are associated with the subscribed SNPN of the entry in the "list of subscriber data", then the 5GMM parameters can only be used if the subscriber identifier of the selected entry of the "list of subscriber data" matches the subscriber identifier stored in the non-volatile memory or if the subscriber identifier from the USIM matches the subscriber identifier stored in the non volatile memory, no subscriber identifier is configured in the selected entry of the "list of subscriber data" configured in the ME and the UE has a valid USIM.

Each configured NSSAI consists of S-NSSAI(s) stored together with an SNPN identity, if it is associated with an SNPN. A configured NSSAI may be associated with NSSRG information, S-NSSAI time validity information, S-NSSAI location validity information, NSAG information and on-demand NSSAI.

Each NSSAI inclusion mode is associated with an SNPN identity and access type.

The MPS indicator is stored together with an SNPN identity of the SNPN that provided it, and is valid in that registered SNPN or equivalent SNPN.

The MCS indicator is stored together with an SNPN identity of the SNPN that provided it, and is valid in that registered SNPN or equivalent SNPN.

Operator-defined access category definitions are stored together with an SNPN identity of the SNPN that provided them, and are valid in that SNPN or equivalent SNPN. The maximum number of stored operator-defined access category definitions is UE implementation dependent.

Each network-assigned UE radio capability ID is stored together with an SNPN identity of the SNPN that provided it as well as a mapping to the corresponding UE radio configuration, and is valid in that SNPN. The UE shall be able to store at least the last 16 received network-assigned UE radio capability IDs. There shall be only one network-assigned UE radio capability ID stored for a given combination of SNPN identity and UE radio configuration and any existing UE radio capability ID shall be deleted when a new UE radio capability ID is added for the same combination of SNPN identity and UE radio configuration. If the UE receives a network-assigned UE radio capability ID with a Version ID value different from the value included in the network-assigned UE radio capability ID(s) stored at the UE for the serving SNPN, the UE may delete these stored network-assigned UE radio capability ID(s).

The handling of the SOR-CMCI stored in the non-volatile memory in the ME is specified in 3GPP TS 23.122 \[5\].

The allowed NSSAI(s) can be stored in a non-volatile memory in the ME. Allowed NSSAI consists of S-NSSAI(s) stored together with an SNPN identity, if it is associated with an SNPN.

The partially allowed NSSAI(s) can be stored as allowed NSSAI(s) in a non-volatile memory in the ME. Partially allowed NSSAI consists of S-NSSAI(s) and a list of TAs for which the S-NSSAI is allowed, stored together with an SNPN identity, if it is associated with an SNPN.

########  Annex D (normative): UE policy delivery service
