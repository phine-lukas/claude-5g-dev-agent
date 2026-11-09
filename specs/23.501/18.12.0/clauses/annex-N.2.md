# N.2 Enabling access to Localized Services

## N.2.1 General

To enable a PNI-NPN or SNPN to provide access to Localized Services, the PNI-NPN or SNPN operator configures the network with information enabling the UEs to access the Localized Services using the PNI-NPN or SNPN according to any validity of the Localized Services and the information is determined in agreement with the Localized Service Provider e.g.:

a\. Identification of each Localized Service, e.g. to be used in URSP rules.

b\. validity restriction for each Localized Service, e.g. the validity of time and/or location.

c\. service parameters for each Localized Service, e.g. DNN, S-NSSAI and QoS requirements.

d\. service authorization methods, e.g. NSSAA or Secondary authentication/authorization during PDU Session establishment.

To allow the UE to access the PNI-NPN providing access to Localized Services using credentials of the HPLMN, the PNI-NPN can be configured based on the Localized Service agreements between the PNI-NPN and the HPLMN, to allow primary authentication towards the HPLMN.

To allow the UE to access the SNPN providing access to Localized Services using credentials of the Credentials Holder, the SNPN can be configured based on Localized Service agreements between the SNPN and the Credentials Holder, to allow primary authentication towards the Credentials Holder.

To allow the UE to access the SNPN providing access to Localized Services when new credential is required, the SNPN can provide UE onboarding function as specified in clause 5.30.2.10 for the UE to obtain credential and necessary information to access the SNPN, or the UE can leverage existing credential and network connection to get access to a PVS via User Plane to obtain new credential.

To allow the UE to access the PNI-NPN providing access to the Localized Services where NSSAA or secondary authentication/authorization during PDU session establishment is required, the UE can obtain new credential using remote provisioning functionality as defined in clause 5.39.

To allow the UE to access the HPLMN or subscribed SNPN services while being registered in the PNI-NPN or SNPN, the PNI-NPN or SNPN can establish service agreements and configure inter-connect with the HPLMN or subscribed SNPN operator. If a PNI-NPN is providing access to the Localized Services, the existing roaming architecture with home-routed PDU Sessions are used. If an SNPN is providing access to the Localized Services, then the UE can access HPLMN or subscribed SNPN as described in Annex D, clauses D.3, D.6 and D.7.

## N.2.2 Configuration of network to provide access to Localized Services

For configuring the PNI-NPN or SNPN (e.g. creation of network slice/DNN for carrying Localized Service traffic), existing OAM mechanisms can be re-used as per TS 28.557 \[148\] clause 6.3.1, that provides a solution for NPN provisioning by a network slice of a PLMN and for exposure of management capability of PNI-NPN (clause 6.3.2). The attributes to support this management is further documented in TS 28.541 \[149\].

## N.2.3 Session Management aspects

For session management level information and interactions such as monitoring the PNI-NPN or SNPN performance and enabling suitable QoS for UE in the PNI-NPN or SNPN for Localized Service, the following non-exhaustive options can be used:

\- Covered by the SLA between the PNI-NPN or SNPN operator and the Localized Service Provider.

\- Reuse the existing network exposure procedures as specified in TS 23.502 \[3\] clause 4.15, where the Localized Service Provider is taking the AF role and utilizing the exposure capability provided by the PNI-NPN or SNPN.

\- Enable NEF/PCF in the PNI-NPN or SNPN providing access to the Localized Services (via AF of the Localized Service Provider) to receive and forward the validity conditions and QoS requirements of the Localized Services to the AMF/SMF by reusing the existing PCF initiated AM/SM policy association procedures described in TS 23.502 \[3\] clause 4.16.
