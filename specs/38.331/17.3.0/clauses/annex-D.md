# Annex D (normative): UE requirements on ASN.1 comprehension

This clause specifies UE requirements regarding the ASN.1 transfer syntax support, i.e. the ASN.1 definitions to be comprehended by the UE.

A UE that indicates release X in field *accessStratumRelease* shall comprehend the entire transfer syntax (ASN.1) of release X, in particular at least the first version upon ASN.1 freeze. The UE is however not required to support dedicated signalling related transfer syntax associated with optional features it does not support.

In case a UE that indicates release X in field *accessStratumRelease* supports a feature specified in release Y, which is later than release X, (i.e. early UE implementation) additional requirements apply. The UE obviously also has to support the ASN.1 parts related to indicating support of the feature (in UE capabilities).

**Critical extensions (dedicated signaling)**

If the early implemented feature involves one or more critical extensions in dedicated signalling, the UE shall comprehend the parts of the transfer syntax (ASN.1) of release Y that are related to the feature implemented early. This, in particular, concerns the ASN.1 parts related to configuration of the feature.

If configuration of an early implemented feature introduced in release Y involves a message or field that has been critically extended, the UE shall support configuration of all features supported by the UE that are associated with sub-fields of this critical extension. Apart from the early implemented feature(s), the UE needs, however, not to support functionality beyond what is defined in the release the UE indicates in access stratum release.

Let's consider the example of a UE indicating value X in field *accessStratumRelease* that supports the features A1, A3, and A5, associated with fields *fieldA1*, *fieldA3* and *fieldA5* of *InformationElementA* (see ASN.1 below).

The feature A5 implemented early is associated with *fieldA5*, and can only be configured by the –rY version of *InformationElementA*. In such case, the UE should support configuration of all the features A1, A3 and A5 associated with fields *fieldA1*, *fieldA3* and *fieldA5* by the –rY version of *InformationElementA*.

If, however, one of the features was modified, e.g. the feature A3 associated with *fieldA3*, the network should assume the UE only supports the feature A3 according to the release it indicated in field *accessStratumRelease* (i.e. X).

The UE is neither required to support the additional code-point (*n80-vY0*) nor the additional sub-field (*fieldA3c-rY*).

InformationElementA-rX ::= SEQUENCE {

fieldA1-rX InformationElementA1-rX OPTIONAL, -- Need N

fieldA2-rX InformationElementA2-rX OPTIONAL, -- Need R

fieldA3-rX InformationElementA3-rX OPTIONAL -- Need R

}

InformationElementA-rY ::= SEQUENCE {

fieldA1-rY InformationElementA1-rX OPTIONAL, -- Need N

fieldA2-rY InformationElementA2-rX OPTIONAL, -- Need R

fieldA3-rY InformationElementA3-rY OPTIONAL, -- Need R

fieldA4-rY InformationElementA4-rY OPTIONAL, -- Need R

fieldA5-rY InformationElementA5-rY OPTIONAL -- Need R

}

InformationElementA3-rX ::= SEQUENCE {

fieldA3a-rX InformationElementA3a-rX OPTIONAL, -- Need N

fieldA3b-rX ENUMERATED {n10, n20, n40} OPTIONAL -- Need R

}

InformationElementA3-rY ::= SEQUENCE {

fieldA3a-rY InformationElementA3a-rX OPTIONAL, -- Need N

fieldA3b-rY ENUMERATED {n10, n20, n40, n80-vY0} OPTIONAL, -- Need R

fieldA3c-rY InformationElementA3c-rY OPTIONAL -- Need R

}

**Non-critical extensions (dedicated and broadcast signaling)**

If the early implemented feature involves one or more non-critical extensions, the UE shall comprehend the parts of the transfer syntax (ASN.1) of release Y that are related to the feature implemented early.

If the early implemented feature involves one or more non-critical extensions in dedicated signaling, the network does not include extensions introduced after the release X that are not the parts related to the feature which the UE indicates early support of in UE capabilities. The UE shall anyway comprehend the parts of the transfer syntax (ASN.1) which indicate absence of such extensions.

If the early implemented feature involves one or more non-critical extensions in system information, the SIB(s) containing the release Y fields related to the early implemented features may also include other extensions introduced after the release X that are not the parts related to the feature which the UE supports. The UE shall comprehend such intermediate fields (but again is not required to support the functionality associated with these intermediate fields, in case this concerns optional features not supported by the UE).
