## C.3.5 Npcf_SMPolicyControl_Delete Service Operation

### C.3.5.1 General

Clause 4.2.5.1 is applied with the following differences and limitations:

\- the "n3gaLocation" attribute shall be included in the "userLocationInfo" attribute and:

a\) if the UE connects via W-5GBAN access:

\- Global Line Identifier shall be encoded in the "gli" attribute; and

\- the "w5gbanLineType" attribute to indicate whether the W-5GBAN access is DSL or PON may be included; or

b\) if the UE connects via W-5GCAN access,

\- the HFC Node Identifier shall be encoded in the "hfcNodeId" attribute; and

\- the Global Cable Identifier may be encoded within the "gci" attribute.

\- RAN cause and/or the NAS cause information is not applicable when the 5G-RG or FN-RG connects the 5GC via W-5GAN.
