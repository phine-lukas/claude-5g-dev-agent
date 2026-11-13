## C.3.2 Npcf_SMPolicyControl_Create Service Operation

### C.3.2.1 General

Clause 4.2.2.2 is applied with the following differences:

\- The allocated /128 IPv6 address or IPv6 /64 prefix or IPv6 prefix shorter than /64 is included within the "ipv6AddressPrefix" attribute.

\- Request of Presence Reporting Area Change Report is not applicable when the 5G-RG or FN-RG connects to the 5GC via W-5GAN.

\- Global Line ID including the line Id and either PLMN Id or operator Id is encoded within the "gli" attribute of the "n3gaLocation" attribute included in the "userLoc" attribute within the PolicyAssociationRequest data structure when the 5G-RG or FN-RG registers via W-5GBAN.

\- The HFC Node Identifier is encoded in the "hfcNodeId" attribute of the "n3gaLocation" attribute included in the "userLocationInfo" attribute within the SmPolicyContextData data structure when the 5G-CRG or FN-CRG connects to the 5GC via W-5GCAN.

\- The PEI that may be included within the "pei" attribute shall have one of the following representations:

i\. When the UE supports only wireline access, the PEI shall be a MAC address.

NOTE: When the PEI includes an indication that the MAC address cannot be used as Equipment identifier, the PEI cannot be trusted for regulatory purposes and cannot be used for equipment based policy evaluation.

ii\. When the UE supports at least one 3GPP access technology, the PEI shall be the allocated IMEI or IMEISV.

\- To support of Hybrid Access for a 5G-RG with a single PDU session as described in clause C.3.6.2.2, EPC interworking specific attributes and procedures apply as described in clause B.3.2;

\- Access Traffic Steering, Switching and Splitting as defined in clause 4.2.2.17 is only applicable to the case that the 5G-RG establishes:

a\) Hybrid Access with a multi-access PDU Session connectivity via NG-RAN and W-5GAN, as described in clause C.3.6.2.3; or

b\) Hybrid Access with a multi-access PDU Session connectivity via EPC/E-UTRAN and W-5GAN, as described in clause C.3.6.2.4.

\- The access network transmission technology for the wireline access may be encoded:

i\. within the "ratType" attribute of the SmPolicyContextData type; or

ii\. when Access Traffic Steering, Switching and Splitting is supported, within the "ratType" attribute of the SmPolicyContextData type, or within the "ratType" attribute of the AdditionalAccessInfo type.

\- The onboarding mechanism defined in 3GPP TS 23.501 \[2\], clause 5.30.2.10, is not applicable for an RG and thus the functionality related to the "PvsSupport" feature defined in this specification does not apply.

### C.3.2.2 IPTV service support

If the PCF fetches the Multicast Access Control information from the UDR as defined in 3GPP TS 29.519 \[15\], the PCF shall authorize a PCC rule as defined in Annex C.3.6.1 and provision it to the SMF in the HTTP response message.

### C.3.2.3 SNPN services support

Access to SNPN applies following the same specification as for accessing a PLMN with the exception that User Plane Remote Provisioning of UEs SNPN Credentials when in Onboarding Network (ONN) is not applicable, i.e. clause 4.2.2.21 does not apply.

NOTE: In this Release of the specification, the RG will not access to an ON-SNPN to initiate the onboarding procedure and thus the SMF will never provide the "onboardInd" attribute set to true.
