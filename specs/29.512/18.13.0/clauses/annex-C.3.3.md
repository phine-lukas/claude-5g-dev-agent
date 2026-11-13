## C.3.3 Npcf_SMPolicyControl_UpdateNotify Service Operation

### C.3.3.1 General

The descriptions in clause 4.2.3.1 are applied with the following differences:

\- To support Hybrid Access for a 5G-RG with a single PDU session as described in clause C.3.6.2.2, EPC interworking specific attributes and procedures apply as described in B.3.3;

\- Access traffic steering, switching and splitting support as described in clause 4.2.3.21 is only applicable to the case that 5G-RG establishes:

a\) Hybrid Access with a multi-access PDU Session connectivity via NG-RAN and W-5GAN, as described in clause C.3.6.2.3; or

b\) Hybrid Access with a multi-access PDU Session connectivity via EPC/E-UTRAN and W-5GAN, as described in clause C.3.6.2.4.

\- Request for the result of PCC rule removal is not applicable when the 5G-RG or FN-RG connects to the 5GC via W-5GAN.

### C.3.3.2 IPTV service support

If the PCF fetches the Multicast Access Control information from the UDR as defined in 3GPP TS 29.519 \[15\], for each impacted PDU session, the PCF shall authorize a PCC rule as defined in Annex C.3.6.1 and provision it to the SMF in the HTTP POST message.
