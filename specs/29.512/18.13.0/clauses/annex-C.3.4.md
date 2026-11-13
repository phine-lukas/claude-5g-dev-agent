## C.3.4 Npcf_SMPolicyControl_Update Service Operation

### C.3.4.1 General

Clause 4.2.4.2 is applied with the following differences:

\- The released /128 IPv6 address or IPv6 /64 prefix or IPv6 prefix shorter than /64 is included within the "relIpv6AddressPrefix" attribute.

\- If the feature "MultiIpv6AddrPrefix" is supported, the additionally allocated IPv6 prefix may be included within the "addIpv6AddrPrefixes" attribute and the additional released IPv6 prefix may be included within the "addRelIpv6AddrPrefixes" attribute. If the "UnlimitedMultiIpv6Prefix" feature is supported, and if multiple allocated or released IPv6 prefixes are detected, the NF service consumer shall include the new allocated UE Ipv6 prefixes within the "multiIpv6Prefixes" attribute and the released UE Ipv6 prefixes within the "multiRelIpv6Prefixes" attribute.

\- RAN cause and/or the NAS cause information is not applicable when the 5G-RG or FN-RG connects the 5GC via W-5GAN.

\- To support Hybrid Access for a 5G-RG with a single PDU session as described in clause C.3.6.2.2, EPC interworking specific attributes and procedures apply as described in B.3.4;

\- When the report of access network information described in clause 4.2.4.9 includes the user location information, the "n3gaLocation" attribute shall be included in the "userLocationInfo" attribute and:

a\) if the UE connects via W-5GBAN access:

\- Global Line Identifier shall be encoded in the "gli" attribute; and

\- the "w5gbanLineType" attribute to indicate whether the W-5GBAN access is DSL or PON may be included; or

b\) if the UE connects via W-5GCAN access, the HFC Node Identifier shall be encoded in the "hfcNodeId" attribute.

\- Access traffic steering, switching and splitting support as described in clause 4.2.4.25 is only applicable to the case that 5G-RG establishes:

a\) Hybrid Access with a multi-access PDU Session connectivity via NG-RAN and W-5GAN, as described in clause C.3.6.2.3; or

b\) Hybrid Access with a multi-access PDU Session connectivity via EPC/E-UTRAN and W-5GAN, as described in clause C.3.6.2.4.

\- The access network transmission technology for the wireline access may be encoded:

i\. within the "ratType" attribute of the SmPolicyUpdateContextData type; or

ii\. when Access Traffic Steering, Switching and Splitting is supported, within the "ratType" attribute of the SmPolicyContextUpdateData type, or within the "ratType" attribute of the AdditionalAccessInfo type.

### C.3.4.2 IPTV service support

If the "WWC" feature is supported and "5G_RG_JOIN" and/or "5G_RG_LEAVE" are provisioned and when the SMF detects a 5G-RG has joined or left to an IP Multicast Group, the SMF shall send an HTTP POST message as defined in clause 4.2.4.2 and include the "5G_RG_JOIN" or "5G_RG_LEAVE" within the "repPolicyCtrlReqTriggers" attribute respectively and the received one or more IP multicast addressing information within the "mulAddrInfos" attribute. Within each IpMulticastAddressInfo data structure, the SMF shall include the destination IPv4 multicast address of the DL multicast flow within the "ipv4MulAddr" attribute and the source IPv4 address of the DL multicast flow within the "srcIpv4Addr" attribute if available or the destination IPv6 multicast address of the DL multicast flow within the "ipv6MulAddr" attribute and the source IPv6 address of the DL multicast flow within the "srcIpv6Addr" attribute if available.

NOTE: The corresponding notification can be used by the PCF to manage Preview Rights related with an IP multicast flow corresponding to an IPTV channel by provisioning the corresponding PCC rule. In this case the PCF is responsible to remove the provisioned PCC rule when the preview duration has elapsed.
