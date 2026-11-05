# Annex A (informative): Guidelines, mainly on use of ASN.1

# A.1 Introduction

The following clauses contain guidelines for the specification of RRC protocol data units (PDUs) with ASN.1.

# A.2 Procedural specification

## A.2.1 General principles

The procedural specification provides an overall high level description regarding the UE behaviour in a particular scenario.

It should be noted that most of the UE behaviour associated with the reception of a particular field is covered by the applicable parts of the PDU specification. The procedural specification may also include specific details of the UE behaviour upon reception of a field, but typically this should be done only for cases that are not easy to capture in the PDU clause e.g. general actions, more complicated actions depending on the value of multiple fields.

Likewise, the procedural specification need not specify the UE requirements regarding the setting of fields within the messages that are sent to the network i.e. this may also be covered by the PDU specification.

## A.2.2 More detailed aspects

The following more detailed conventions should be used:

\- Bullets:

\- Capitals should be used in the same manner as in other parts of the procedural text i.e. in most cases no capital applies since the bullets are part of the sentence starting with 'The UE shall:'

\- All bullets, including the last one in a clause, should end with a semi-colon i.e. an ';.

\- Conditions:

\- Whenever multiple conditions apply, a semi-colon should be used at the end of each conditions with the exception of the last one, i.e. as in 'if cond1, or cond2.

# A.3 PDU specification

## A.3.1 General principles

### A.3.1.1 ASN.1 clauses

The RRC PDU contents are formally and completely described using abstract syntax notation (ASN.1), see X.680 \[6\], X.681 \[7\].

The complete ASN.1 code is divided into a number of ASN.1 clauses in the specifications. In order to facilitate the extraction of the complete ASN.1 code from the specification, each ASN.1 clause begins with the following:

\- a first text paragraph consisting entirely of an *ASN.1 start tag*, which consists of a double hyphen followed by a single space and the text string "ASN1START" (in all upper case letters);

\- a second text paragraph consisting entirely of a *block start tag* is included, which consists of a double hyphen followed by a single space and the text string "TAG-NAME-START" (in all upper case letters), where the "NAME" refers to the main name of the paragraph (in all upper-case letters).

Similarly, each ASN.1 clause ends with the following:

\- a first text paragraph consisting entirely of a *blockstop tag*, which consists of a double hyphen followed by a single space and the text string "TAG-NAME-STOP" (in all upper-case letters), where the "NAME" refers to the main name of the paragraph (in all upper-case letters);

\- a second text paragraph consisting entirely of an *ASN.1 stop tag*, which consists of a double hyphen followed by a singlespace and the text "ASN1STOP" (in all upper case letters).

This results in the following tags:

\-- ASN1START

\-- TAG-NAME-START

\-- TAG-NAME-STOP

\-- ASN1STOP

The text paragraphs containing either of the start and stop tags should not contain any ASN.1 code significant for the complete description of the RRC PDU contents. The complete ASN.1 code may be extracted by copying all the text paragraphs between an ASN.1 start tag and the following ASN.1 stop tag in the order they appear, throughout the specification.

NOTE: A typical procedure for extraction of the complete ASN.1 code consists of a first step where the entire RRC PDU contents description (ultimately the entire specification) is saved into a plain text (ASCII) file format, followed by a second step where the actual extraction takes place, based on the occurrence of the ASN.1 start and stop tags.

### A.3.1.2 ASN.1 identifier naming conventions

The naming of identifiers (i.e., the ASN.1 field and type identifiers) should be based on the following guidelines:

\- Message (PDU) identifiers should be ordinary mixed case without hyphenation. These identifiers, *e.g.*, the *RRCConnectionModificationCommand*, should be used for reference in the procedure text. Abbreviations should be avoided in these identifiers and abbreviated forms of these identifiers should not be used.

\- Type identifiers other than PDU identifiers should be ordinary mixed case, with hyphenation used to set off acronyms only where an adjacent letter is a capital, *e.g.*, *EstablishmentCause, SelectedPLMN (not Selected-PLMN, since the "d" in "Selected" is lowercase), InitialUE-Identity and MeasSFN-SFN-TimeDifference*.

\- Field identifiers shall start with a lowercase letter and use mixed case thereafter, *e.g.*, *establishmentCause*. If a field identifier begins with an acronym (which would normally be in upper case), the entire acronym is lowercase (*plmn-Identity*, not *pLMN-Identity*). The acronym is set off with a hyphen (*ue-Identity*, not *ueIdentity), in order to facilitate a consistent search pattern with corresponding type identifiers*.

\- Identifiers should convey the meaning of the identifier and should avoid adding unnecessary postfixes (e.g. abstractions like 'Info') for the name.

\- Identifiers that are likely to be keywords of some language, especially widely used languages, such as C++ or Java, should be avoided to the extent possible.

\- Identifiers, other than PDU identifiers, longer than 25 characters should be avoided where possible. It is recommended to use abbreviations, which should be done in a consistent manner i.e. use 'Meas' instead of 'Measurement' for all occurrences. Examples of typical abbreviations are given in table A.3.1.2.1-1 below.

\- *For future extension:* When an extension is introduced a suffix is added to the identifier of the concerned ASN.1 field and/or type. A suffix of the form "‑rX" is used, with X indicating the release, for ASN.1 fields or types introduced in a later release (i.e. a release later than the original/first release of the protocol) as well as for ASN.1 fields or types for which a revision is introduced in a later release replacing a previous version, *e.g.*, *Foo-r9* for the Rel-9 version of the ASN.1 type *Foo*. A suffix of the form "‑rXb" is used for the first revision of a field that it appears in the same release (X) as the original version of the field, "‑rXc" for a second intra-release revision and so on. A suffix of the form "‑vXYZ" is used for ASN.1 fields or types that only are an extension of a corresponding earlier field or type (see clause A.4), e.g., *AnElement-v10b0* for the extension of the ASN.1 type *AnElement* introduced in version 10.11.0 of the specification. A number *0...9, 10, 11, etc.* is used to represent the first part of the version number, indicating the release of the protocol. Lower case letters *a, b, c, etc.* are used to represent the second (and third) part of the version number if they are greater than 9. In the procedural specification, in field descriptions as well as in headings suffices are not used, unless there is a clear need to distinguish the extension from the original field.

\- More generally, in case there is a need to distinguish different variants of an ASN.1 field or IE, a suffix should be added at the end of the identifiers e.g. *MeasObjectUTRA*, *ConfigCommon*. When there is no particular need to distinguish the fields (e.g. because the field is included in different IEs), a common field identifier name may be used. This may be attractive e.g. in case the procedural specification is the same for the different variants.

\- It should be avoided to use field identifiers with the same name within the elements of a CHOICE, including using a CHOICE inside a SEQUENCE (to avoid certain compiler errors).

Table A.3.1.2-1: Examples of typical abbreviations used in ASN.1 identifiers

| Abbreviation | Abbreviated word       |
| ------------ | ---------------------- |
| Config       | Configuration          |
| DL           | Downlink               |
| Ext          | Extension              |
| Freq         | Frequency              |
| Id           | Identity               |
| Ind          | Indication             |
| Meas         | Measurement            |
| MIB          | MasterInformationBlock |
| Neigh        | Neighbour(ing)         |
| Param(s)     | Parameter(s)           |
| Phys         | Physical               |
| PCI          | Physical Cell Id       |
| Proc         | Process                |
| Reconfig     | Reconfiguration        |
| Reest        | Re-establishment       |
| Req          | Request                |
| Rx           | Reception              |
| Sched        | Scheduling             |
| SIB          | SystemInformationBlock |
| Sync         | Synchronisation        |
| Thr          | Threshold              |
| Tx           | Transmission           |
| UL           | Uplink                 |

NOTE: The table A.3.1.2.1-1 is not exhaustive. Additional abbreviations may be used in ASN.1 identifiers when needed.

### A.3.1.3 Text references using ASN.1 identifiers

A text reference into the RRC PDU contents description from other parts of the specification is made using the ASN.1 field identifier of the referenced type. The ASN.1 field and type identifiers used in text references should be in the *italic font style*. The "do not check spelling and grammar" attribute in Word should be set. Quotation marks (i.e., "") should not be used around the ASN.1 field or type identifier.

A reference to an RRC PDU should be made using the corresponding ASN.1 field identifier followed by the word "message", e.g., a reference to the *RRCRelease* message.

A reference to a specific part of an RRC PDU, or to a specific part of any other ASN.1 type, should be made using the corresponding ASN.1 field identifier followed by the word "field", e.g., a reference to the *prioritisedBitRate* field in the example below.

\-- /example/ ASN1START

LogicalChannelConfig ::= SEQUENCE {

ul-SpecificParameters SEQUENCE {

priority Priority,

prioritisedBitRate PrioritisedBitRate,

bucketSizeDuration BucketSizeDuration,

logicalChannelGroup INTEGER (0..3)

} OPTIONAL

}

\-- ASN1STOP

NOTE: All the ASN.1 start tags in the ASN.1 clauses, used as examples in this annex to the specification, are deliberately distorted, in order not to include them when the ASN.1 description of the RRC PDU contents is extracted from the specification.

A reference to a specific type of information element should be made using the corresponding ASN.1 type identifier preceded by the acronym "IE", e.g., a reference to the IE *LogicalChannelConfig* in the example above.

References to a specific type of information element should only be used when those are generic, i.e., without regard to the particular context wherein the specific type of information element is used. If the reference is related to a particular context, e.g., an RRC PDU type (message) wherein the information element is used, the corresponding field identifier in that context should be used in the text reference.

A reference to a specific value of an ASN.1 field should be made using the corresponding ASN.1 value without using quotation marks around the ASN.1 value, e.g., 'if the *status* field is set to value *true*'.

## A.3.2 High-level message structure

Within each logical channel type, the associated RRC PDU (message) types are alternatives within a CHOICE, as shown in the example below.

\-- /example/ ASN1START

DL-DCCH-Message ::= SEQUENCE {

message DL-DCCH-MessageType

}

DL-DCCH-MessageType ::= CHOICE {

c1 CHOICE {

dlInformationTransfer DLInformationTransfer,

handoverFromEUTRAPreparationRequest HandoverFromEUTRAPreparationRequest,

mobilityFromEUTRACommand MobilityFromEUTRACommand,

rrcConnectionReconfiguration RRCConnectionReconfiguration,

rrcConnectionRelease RRCConnectionRelease,

securityModeCommand SecurityModeCommand,

ueCapabilityEnquiry UECapabilityEnquiry,

spare1 NULL

},

messageClassExtension SEQUENCE {}

}

\-- ASN1STOP

A nested two-level CHOICE structure is used, where the alternative PDU types are alternatives within the inner level *c1* CHOICE.

Spare alternatives (i.e., *spare1* in this case) may be included within the *c1* CHOICE to facilitate future extension. The number of such spare alternatives should not extend the total number of alternatives beyond an integer-power-of-two number of alternatives (i.e., eight in this case).

Further extension of the number of alternative PDU types is facilitated using the *messageClassExtension* alternative in the outer level CHOICE.

## A.3.3 Message definition

Each PDU (message) type is specified in an ASN.1 clause similar to the one shown in the example below.

\-- /example/ ASN1START

RRCConnectionReconfiguration ::= SEQUENCE {

rrc-TransactionIdentifier RRC-TransactionIdentifier,

criticalExtensions CHOICE {

c1 CHOICE{

rrcConnectionReconfiguration-r8 RRCConnectionReconfiguration-r8-IEs,

spare3 NULL, spare2 NULL, spare1 NULL

},

criticalExtensionsFuture SEQUENCE {}

}

}

RRCConnectionReconfiguration-r8-IEs ::= SEQUENCE {

\-- Enter the IEs here.

...

}

\-- ASN1STOP

Hooks for *critical* and *non-critical* extension should normally be included in the PDU type specification. How these hooks are used is further described in clause A.4.

Critical extensions are characterised by a redefinition of the PDU contents and need to be governed by a mechanism for protocol version agreement between the encoder and the decoder of the PDU, such that the encoder is prevented from sending a critically extended version of the PDU type, which is not comprehended by the decoder.

Critical extension of a PDU type is facilitated by a two-level CHOICE structure, where the alternative PDU contents are alternatives within the inner level *c1* CHOICE. Spare alternatives (i.e., *spare3* down to *spare1* in this case) may be included within the *c1* CHOICE. The number of spare alternatives to be included in the original PDU specification should be decided case by case, based on the expected rate of critical extension in the future releases of the protocol.

Further critical extension, when the spare alternatives from the original specifications are used up, is facilitated using the *criticalExtensionsFuture* in the outer level CHOICE.

In PDU types where critical extension is not expected in the future releases of the protocol, the inner level *c1* CHOICE and the spare alternatives may be excluded, as shown in the example below.

\-- /example/ ASN1START

RRCConnectionReconfigurationComplete ::= SEQUENCE {

rrc-TransactionIdentifier RRC-TransactionIdentifier,

criticalExtensions CHOICE {

rrcConnectionReconfigurationComplete-r8

RRCConnectionReconfigurationComplete-r8-IEs,

criticalExtensionsFuture SEQUENCE {}

}

}

RRCConnectionReconfigurationComplete-r8-IEs ::= SEQUENCE {

\-- Enter the fields here.

...

}

\-- ASN1STOP

Non-critical extensions are characterised by the addition of new information to the original specification of the PDU type. If not comprehended, a non-critical extension may be skipped by the decoder, whilst the decoder is still able to complete the decoding of the comprehended parts of the PDU contents.

Non-critical extensions at locations other than the end of the message or other than at the end of a field contained in a BIT or OCTET STRING are facilitated by use of the ASN.1 extension marker "...". The original specification of a PDU type should normally include the extension marker at the end of the sequence of information elements contained.

Non-critical extensions at the end of the message or at the end of a field that is contained in a BIT or OCTET STRING may be facilitated by use of an empty sequence that is marked OPTIONAL e.g. as shown in the following example:

\-- /example/ ASN1START

RRCMessage-r8-IEs ::= SEQUENCE {

field1 InformationElement1,

field2 InformationElement2,

nonCriticalExtension SEQUENCE {} OPTIONAL

}

\-- ASN1STOP

The ASN.1 clause specifying the contents of a PDU type may be followed by a *field description* table where a further description of, e.g., the semantic properties of the fields may be included. The general format of this table is shown in the example below. The field description table is absent in case there are no fields for which further description needs to be provided e.g. because the PDU does not include any fields, or because an IE is defined for each field while there is nothing specific regarding the use of this IE that needs to be specified.

<!-- table -->
| %PDU-TypeIdentifier% field descriptions |
| %field identifier% Field description. |
| %field identifier% Field description. |
<!-- /table -->

The field description table has one column. The header row shall contain the ASN.1 type identifier of the PDU type.

The following rows are used to provide field descriptions. Each row shall include a first paragraph with a *field identifier* (in ***bold and italic*** font style) referring to the part of the PDU to which it applies. The following paragraphs at the same row may include (in regular font style), e.g., semantic description, references to other specifications and/or specification of value units, which are relevant for the particular part of the PDU.

The parts of the PDU contents that do not require a field description shall be omitted from the field description table.

## A.3.4 Information elements

Each IE (information element) type is specified in an ASN.1 clause similar to the one shown in the example below.

\-- /example/ ASN1START

PRACH-ConfigSIB ::= SEQUENCE {

rootSequenceIndex INTEGER (0..1023),

prach-ConfigInfo PRACH-ConfigInfo

}

PRACH-Config ::= SEQUENCE {

rootSequenceIndex INTEGER (0..1023),

prach-ConfigInfo PRACH-ConfigInfo OPTIONAL -- Need N

}

PRACH-ConfigInfo ::= SEQUENCE {

prach-ConfigIndex ENUMERATED {ffs},

highSpeedFlag ENUMERATED {ffs},

zeroCorrelationZoneConfig ENUMERATED {ffs}

}

\-- ASN1STOP

IEs should be introduced whenever there are multiple fields for which the same set of values apply. IEs may also be defined for other reasons e.g. to break down a ASN.1 definition in to smaller pieces.

A group of closely related IE type definitions, like the IEs *PRACH-ConfigSIB* and *PRACH-Config* in this example, are preferably placed together in a common ASN.1 clause. The IE type identifiers should in this case have a common base, defined as the *generic type identifier*. It may be complemented by a suffix to distinguish the different variants. The "*PRACH-Config*" is the generic type identifier in this example, and the "*SIB*" suffix is added to distinguish the variant. The clause heading and generic references to a group of closely related IEs defined in this way should use the generic type identifier.

The same principle should apply if a new version, or an extension version, of an existing IE is created for *critical* or *non-critical* extension of the protocol (see clause A.4). The new version, or the extension version, of the IE is included in the same ASN.1 clause defining the original. A suffix is added to the type identifier, using the naming conventions defined in clause A.3.1.2, indicating the release or version of the where the new version, or extension version, was introduced.

Local IE type definitions, like the IE *PRACH-ConfigInfo* in the example above, may be included in the ASN.1 clause and be referenced in the other IE types defined in the same ASN.1 clause. The use of locally defined IE types should be encouraged, as a tool to break up large and complex IE type definitions. It can improve the readability of the code. There may also be a benefit for the software implementation of the protocol end-points, as these IE types are typically provided by the ASN.1 compiler as independent data elements, to be used in the software implementation.

An IE type defined in a local context, like the IE *PRACH-ConfigInfo*, should not be referenced directly from other ASN.1 clauses in the RRC specification. An IE type which is referenced in more than one ASN.1 clause should be defined in a separate clause, with a separate heading and a separate ASN.1 clause (possibly as one in a set of closely related IE types, like the IEs *PRACH-ConfigSIB* and *PRACH-Config* in the example above). Such IE types are also referred to as 'global IEs'.

NOTE: Referring to an IE type, that is defined as a local IE type in the context of another ASN.1 clause, does not generate an ASN.1 compilation error. Nevertheless, using a locally defined IE type in that way makes the IE type definition difficult to find, as it would not be visible at an outline level of the specification. It should be avoided.

The ASN.1 clause specifying the contents of one or more IE types, like in the example above, may be followed by a *field description* table, where a further description of, e.g., the semantic properties of the fields of the information elements may be included. This table may be absent, similar as indicated in clause A.3.3 for the specification of the PDU type. The general format of the *field description* table is the same as shown in clause A.3.3 for the specification of the PDU type.

## A.3.5 Fields with optional presence

A field with optional presence may be declared with the keyword DEFAULT. It identifies a default value to be assumed, if the sender does not include a value for that field in the encoding:

\-- /example/ ASN1START

PreambleInfo ::= SEQUENCE {

numberOfRA-Preambles INTEGER (1..64) DEFAULT 1,

...

}

\-- ASN1STOP

Alternatively, a field with optional presence may be declared with the keyword OPTIONAL. It identifies a field for which a value can be omitted. The omission carries semantics, which is different from any normal value of the field:

\-- /example/ ASN1START

PRACH-Config ::= SEQUENCE {

rootSequenceIndex INTEGER (0..1023),

prach-ConfigInfo PRACH-ConfigInfo OPTIONAL -- Need N

}

\-- ASN1STOP

The semantics of an optionally present field, in the case it is omitted, should be indicated at the end of the paragraph including the keyword OPTIONAL, using a short comment text with a need code. The need code includes the keyword "Need", followed by one of the predefined semantics tags (S, M, N or R) defined in clause 6.1. If the semantics tag S is used, the semantics of the absent field are further specified either in the field description table following the ASN.1 clause, or in procedure text.

The addition of OPTIONAL keywords for capability groups is based on the following guideline. If there is more than one field in the lower level IE, then OPTIONAL keyword is added at the group level. If there is only one field in the lower level IE, OPTIONAL keyword is not added at the group level.

## A.3.6 Fields with conditional presence

A field with conditional presence is declared with the keyword OPTIONAL. In addition, a short comment text shall be included at the end of the paragraph including the keyword OPTIONAL. The comment text includes the keyword "Cond", followed by a condition tag associated with the field ("UL" in this example):

\-- /example/ ASN1START

LogicalChannelConfig ::= SEQUENCE {

ul-SpecificParameters SEQUENCE {

priority INTEGER (0),

...

} OPTIONAL -- Cond UL

}

\-- ASN1STOP

When conditionally present fields are included in an ASN.1 clause, the field description table after the ASN.1 clause shall be followed by a *conditional presence* table. The conditional presence table specifies the conditions for including the fields with conditional presence in the particular ASN.1 clause.

| Conditional presence | Explanation                                                                                                                                                                              |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| UL                   | Specification of the conditions for including the field associated with the condition tag = "UL". Semantics in case of optional presence under certain conditions may also be specified. |

The conditional presence table has two columns. The first column (heading: "Conditional presence") contains the condition tag (in *italic* font style), which links the fields with a condition tag in the ASN.1 clause to an entry in the table. The second column (heading: "Explanation") contains a text specification of the conditions and requirements for the presence of the field. The second column may also include semantics, in case of an optional presence of the field, under certain conditions i.e. using the same predefined tags as defined for optional fields in A.3.5.

Conditional presence should primarily be used when presence of a field depends on the presence and/or value of other fields within the same message. If the presence of a field depends on whether another feature/function has been configured, while this function can be configured independently e.g. by another message and/or at another point in time, the relation is best reflected by means of a statement in the field description table.

If the ASN.1 clause does not include any fields with conditional presence, the conditional presence table shall not be included.

Whenever a field is only applicable in specific cases e.g. TDD, use of conditional presence should be considered.

## A.3.7 Guidelines on use of lists with elements of SEQUENCE type

Where an information element has the form of a list (the SEQUENCE OF construct in ASN.1) with the type of the list elements being a SEQUENCE data type, an information element shall be defined for the list elements even if it would not otherwise be needed.

For example, a list of PLMN identities with reservation flags is defined as in the following example:

\-- /example/ ASN1START

PLMN-IdentityInfoList ::= SEQUENCE (SIZE (1..6)) OF PLMN-IdentityInfo

PLMN-IdentityInfo ::= SEQUENCE {

plmn-Identity PLMN-Identity,

cellReservedForOperatorUse ENUMERATED {reserved, notReserved}

}

\-- ASN1STOP

rather than as in the following (bad) example, which may cause generated code to contain types with unpredictable names:

\-- /bad example/ ASN1START

PLMN-IdentityList ::= SEQUENCE (SIZE (1..6)) OF SEQUENCE {

plmn-Identity PLMN-Identity,

cellReservedForOperatorUse ENUMERATED {reserved, notReserved}

}

\-- ASN1STOP

## A.3.8 Guidelines on use of parameterised SetupRelease type

The usage of the parameterised *SetupRelease* type is like a function call in programming languages where the element type parameter is passed as a parameter. The parameterised type only implies a textual change in abstract syntax where all references to the parameterised type are replaced by the compiler with the release/setup choice. Two examples of the usage are shown below:

\-- /example/ ASN1START

RRCMessage-rX-IEs ::= SEQUENCE {

field-rX SetupRelease { IE-rX } OPTIONAL, -- Need M

...

}

RRCMessage-rX-IEs ::= SEQUENCE {

field-rX SetupRelease { Element-rX }

} OPTIONAL, -- Need M

Element-rX ::= SEQUENCE {

field1-rX IE1-rX,

field2-rX IE2-rX OPTIONAL -- Need N

} OPTIONAL, -- Need M

\-- /example/ ASN1STOP

The *SetupRelease* is always be used with only named IEs, i.e. the example below is not allowed:

\-- /example/ ASN1START

RRCMessage-rX-IEs ::= SEQUENCE {

field-rX SetupRelease { SEQUENCE { -- Unnamed SEQUENCEs are not allowed\!

field1-rX IE1-rX,

field2-rX IE2-rX OPTIONAL -- Need N

}

} OPTIONAL, -- Need M

}

\-- /example/ ASN1STOP

If a field defined using the parameterized SetupRelease type requires procedural text, the field is referred to using the values defined for the type itself, namely, "setup" and "release". For example, procedural text for field-rX above could be as follows:

1\> if *field-rX* is set to "setup":

2\> do something;

1\> else (*field-rX* is set to "release"):

2\> release *field-rX* (if appropriate).

## A.3.9 Guidelines on use of ToAddModList and ToReleaseList

In order to benefit from delta signalling when modifying lists with many and/or large elements, so-called add/mod- and release- lists should be used. Instead of a single list containing all elements of the list, the ASN.1 provides two lists. One list is used to convey the actual elements that are to be added to the list or modified in the list. The second list conveys only the identities (IDs) of the list elements that are to be released from the list. In other words, the ASN.1 defines only means to signal modifications to a list maintained in the receiver (typically the UE). An example is provided below:

\-- /example/ ASN1START

AnExampleIE ::= SEQUENCE {

elementsToAddModList SEQUENCE (SIZE (1..maxNrofElements)) OF Element OPTIONAL, -- Need N

elementsToReleaseList SEQUENCE (SIZE (1..maxNrofElements)) OF ElementId OPTIONAL, -- Need N

...

}

Element ::= SEQUENCE {

elementId ElementId,

aField INTEG ER (0..16777215),

anotherField OCTET STRING,

...

}

ElementId ::= INTEGER (0..maxNrofElements-1)

maxNrofElements INTEGER ::= 50

maxNrofElements-1 INTEGER ::= 49

\-- /example/ ASN1STOP

As can be seen, the elements of the list must contain an identity (INTEGER) that identifies the elements unambiguously upon addition, modification and removal. It is recommended to define an IE for that identifier (here ElementId) so that it can be used both for a field inside the element as well as in the *elementsToReleaseList*.

Both lists should be made OPTIONAL and flagged as "Need N". The need code reflects that the UE does not maintain the received lists as such but rather updates its configuration using the information therein. In other words, it is not possible to provide via delta signalling an update to a previously signalled *elementsToAddModList* or elementsToReleaseList (which Need M would imply). The update is always in relation to the UE's internal configuration.

Note that the release of a field (a list element as well as any other field) releases all its sub-fields (sub-fields configured by elementsToAddModList and any other sub-field).

If no procedural text is provided for a set of ToAddModList and ToReleaseList, the following generic procedure applies:

The UE shall:

1\> for each *ElementId* in the *elementsToReleaseList*,:

2\> if the current UE configuration includes an *Element* with the given *ElementId*:

3\> release the *Element* from the current UE configuration;

1\> for each *Element* in the *elementsToAddModList*:

2\> if the current UE configuration includes an *Element* with the given *ElementId*:

3\> modify the configured *Element* in accordance with the received *Element*;

2\> else:

3\> add received *Element* to the UE configuration.

## A.3.10 Guidelines on use of lists (without ToAddModList and ToReleaseList)

As per clause 6.1.3, when using lists without the ToAddModList and ToReleaseList structure, the contents of the lists are always replaced. To illustrate this, an example is provided below:

\-- /example/ ASN1START

\-- TAG\_EXAMPLE\_LISTS\_START

AnExampleIE ::= SEQUENCE {

elementList SEQUENCE (SIZE (1..maxNrofElements)) OF Element OPTIONAL, -- Need M

...,

\[\[

elementListExt-v2030 SEQUENCE (SIZE (1..maxNrofElementsExt)) OF Element OPTIONAL, -- Need M

\]\]

}

Element ::= SEQUENCE {

useFeatureX BOOLEAN,

aField INTEGER (0..127) OPTIONAL, -- Need M

anotherField INTEGER (0..127) OPTIONAL, -- Need R

...

}

maxNrofElements INTEGER ::= 8

maxNrofElements-1 INTEGER ::= 7

maxNrofElementsExt INTEGER ::= 8

maxNrofElementsExt-1 INTEGER ::= 7

\-- TAG\_EXAMPLE\_LISTS\_STOP

\-- /example/ ASN1STOP

As can be seen, the *elementList* list itself uses Need M, but each list entry *Element* contains mandatory, Need M and Need R fields. If the list is first signalled to UE with 3 entries, and subsequently again with 2 entries, UE shall retain only the latter list, i.e. the list with 2 elements will completely replace the list with 3 elements. That also means that the field *aField* will be treated as if it was newly created, i.e. network must include it if it wishes UE to utilize the field even if it was previously signalled. This also implies that the Need M field (*aField*) will be treated in the same way as the Need R field (*anotherField*), i.e. delta signalling is not applied and the network has to signal the field to ensure UE does not release the value (which is why Need M should not normally be used in the entries of these lists).

# A.4 Extension of the PDU specifications

## A.4.1 General principles to ensure compatibility

It is essential that extension of the protocol does not affect interoperability i.e. it is essential that implementations based on different versions of the RRC protocol are able to interoperate. In particular, this requirement applies for the following kind of protocol extensions:

\- Introduction of new PDU types (i.e. these should not cause unexpected behaviour or damage).

\- Introduction of additional fields in an extensible PDUs (i.e. it should be possible to ignore uncomprehended extensions without affecting the handling of the other parts of the message).

\- Introduction of additional values of an extensible field of PDUs. If used, the behaviour upon reception of an uncomprehended value should be defined.

It should be noted that the PDU extension mechanism may depend on the logical channel used to transfer the message e.g. for some PDUs an implementation may be aware of the protocol version of the peer in which case selective ignoring of extensions may not be required.

The non-critical extension mechanism is the primary mechanism for introducing protocol extensions i.e. the critical extension mechanism is used merely when there is a need to introduce a 'clean' message version. Such a need appears when the last message version includes a large number of non-critical extensions, which results in issues like readability, overhead associated with the extension markers. The critical extension mechanism may also be considered when it is complicated to accommodate the extensions by means of non-critical extension mechanisms.

## A.4.2 Critical extension of messages and fields

The mechanisms to critically extend a message are defined in A.3.3. There are both "outer branch" and "inner branch" mechanisms available. The "outer branch" consists of a CHOICE having the name *criticalExtensions*, with two values, *c1* and *criticalExtensionsFuture*. The *criticalExtensionsFuture* branch consists of an empty SEQUENCE, while the c1 branch contains the "inner branch" mechanism.

The "inner branch" structure is a CHOICE with values of the form "*MessageName-rX-IEs*" (e.g., "*RRCConnectionReconfiguration-r8-IEs*") or "*spareX*", with the spare values having type NULL. The "-rX-IEs" structures contain the *complete* structure of the message IEs for the appropriate release; i.e., the critical extension branch for the Rel-10 version of a message includes all Rel-8 and Rel-9 fields (that are not obviated in the later version), rather than containing only the additional Rel-10 fields.

The following guidelines may be used when deciding which mechanism to introduce for a particular message, i.e. only an 'outer branch', or an 'outer branch' in combination with an 'inner branch' including a certain number of spares:

\- For certain messages, e.g. initial uplink messages, messages transmitted on a broadcast channel, critical extension may not be applicable.

\- An outer branch may be sufficient for messages not including any fields.

\- The number of spares within inner branch should reflect the likelihood that the message will be critically extended in future releases (since each release with a critical extension for the message consumes one of the spare values). The estimation of the critical extension likelihood may be based on the number, size and changeability of the fields included in the message.

\- In messages where an inner branch extension mechanism is available, all spare values of the inner branch should be used before any critical extensions are added using the outer branch.

The following example illustrates the use of the critical extension mechanism by showing the ASN.1 of the original and of a later release

\-- /example/ ASN1START -- Original release

RRCMessage ::= SEQUENCE {

rrc-TransactionIdentifier RRC-TransactionIdentifier,

criticalExtensions CHOICE {

c1 CHOICE{

rrcMessage-r8 RRCMessage-r8-IEs,

spare3 NULL, spare2 NULL, spare1 NULL

},

criticalExtensionsFuture SEQUENCE {}

}

}

\-- ASN1STOP

\-- /example/ ASN1START -- Later release

RRCMessage ::= SEQUENCE {

rrc-TransactionIdentifier RRC-TransactionIdentifier,

criticalExtensions CHOICE {

c1 CHOICE{

rrcMessage-r8 RRCMessage-r8-IEs,

rrcMessage-r10 RRCMessage-r10-IEs,

rrcMessage-r11 RRCMessage-r11-IEs,

rrcMessage-r14 RRCMessage-r14-IEs

},

later CHOICE {

c2 CHOICE{

rrcMessage-r16 RRCMessage-r16-IEs,

spare7 NULL, spare6 NULL, spare5 NULL, spare4 NULL,

spare3 NULL, spare2 NULL, spare1 NULL

},

criticalExtensionsFuture SEQUENCE {}

}

}

}

\-- ASN1STOP

It is important to note that critical extensions may also be used at the level of individual fields i.e. a field may be replaced by a critically extended version. When sending the extended version, the original version may also be included (e.g. original field is mandatory, E-UTRAN is unaware if UE supports the extended version). In such cases, a UE supporting both versions may be required to ignore the original field. The following example illustrates the use of the critical extension mechanism by showing the ASN.1 of the original and of a later release.

\-- /example/ ASN1START -- Original release

RRCMessage ::= SEQUENCE {

rrc-TransactionIdentifier RRC-TransactionIdentifier,

criticalExtensions CHOICE {

c1 CHOICE{

rrcMessage-r8 RRCMessage-r8-IEs,

spare3 NULL, spare2 NULL, spare1 NULL

},

criticalExtensionsFuture SEQUENCE {}

}

}

RRCMessage-rN-IEs ::= SEQUENCE {

field1-rN ENUMERATED {

value1, value2, value3, value4} OPTIONAL, -- Need N

field2-rN InformationElement2-rN OPTIONAL, -- Need N

nonCriticalExtension RRCConnectionReconfiguration-vMxy-IEs OPTIONAL

}

RRCConnectionReconfiguration-vMxy-IEs ::= SEQUENCE {

field2-rM InformationElement2-rM OPTIONAL, -- Cond NoField2rN

nonCriticalExtension SEQUENCE {} OPTIONAL

}

\-- ASN1STOP

| Conditional presence | Explanation                                                                                    |
| -------------------- | ---------------------------------------------------------------------------------------------- |
| *NoField2rN*         | The field is optionally present, need N, if field2-rN is absent. Otherwise the field is absent |

Finally, it is noted that a critical extension may be introduced in the same release as the one in which the original field was introduced e.g. to correct an essential ASN.1 error. In such cases a UE capability may be introduced, to assist the network in deciding whether or not to use the critical extension.

In the case of list fields (SEQUENCE OF types in ASN.1) using the ToAddMod/ToRelease construction, the use of critical extensions to increase the size of a list should be avoided; that is, replacing the original list field by a new field also used to signal entries previously covered by the original field (i.e. extensions done according to the following example) should be avoided:

\-- /example/ ASN1START -- Discouraged example

ContainingStructure ::= SEQUENCE {

listElementToAddModList SEQUENCE (SIZE (1..maxNrofListElements)) OF ListElement OPTIONAL, -- Need N

...,

\[\[

listElementToAddModList-rN SEQUENCE (SIZE (1..maxNrofListElements-rN)) OF ListElement OPTIONAL -- Need N

\]\]

}-- ASN1STOP

Instead, a non-critical list extension mechanism should typically be used, such that the extension field only adds the new entries of the list. This approach is further described in clause A.4.3.6.

If the critical extension mechanism for a list is used, it should be clarified in the field description that the two versions of the list are not configured together, and that the network should release the contents of the original version when configuring the replacement version.

## A.4.3 Non-critical extension of messages

### A.4.3.1 General principles

The mechanisms to extend a message in a non-critical manner are defined in A.3.3. W.r.t. the use of extension markers, the following additional guidelines apply:

\- When further non-critical extensions are added to a message that has been critically extended, the inclusion of these non-critical extensions in earlier critical branches of the message should be avoided when possible.

\- The extension marker ("...") is the primary non-critical extension mechanism that is used but empty sequences may be used if length determinant is not required. Examples of cases where a length determinant is not required:

\- at the end of a message;

\- at the end of a structure contained in a BIT STRING or OCTET STRING.

\- When an extension marker is available, non-critical extensions are preferably placed at the location (e.g. the IE) where the concerned parameter belongs from a logical/ functional perspective (referred to as the '*default extension location*').

\- It is desirable to aggregate extensions of the same release or version of the specification into a group, which should be placed at the lowest possible level.

\- In specific cases it may be preferable to place extensions elsewhere (referred to as the '*actual extension location*') e.g. when it is possible to aggregate several extensions in a group. In such a case, the group should be placed at the lowest suitable level in the message.

\- In case placement at the default extension location affects earlier critical branches of the message, locating the extension at a following higher level in the message should be considered.

\- In case an extension is not placed at the default extension location, an IE should be defined. The IE's ASN.1 definition should be placed in the same ASN.1 clause as the default extension location. In case there are intermediate levels in-between the actual and the default extension location, an IE may be defined for each level. Intermediate levels are primarily introduced for readability and overview. Hence intermediate levels need not always be introduced e.g. they may not be needed when the default and the actual extension location are within the same ASN.1 clause.

### A.4.3.2 Further guidelines

Further to the general principles defined in the previous clause, the following additional guidelines apply regarding the use of extension markers:

\- Extension markers within SEQUENCE:

\- Extension markers are primarily, but not exclusively, introduced at the higher nesting levels.

\- Extension markers are introduced for a SEQUENCE comprising several fields as well as for information elements whose extension would result in complex structures without it (e.g. re-introducing another list).

\- Extension markers are introduced to make it possible to maintain important information structures e.g. parameters relevant for one particular RAT.

\- Extension markers are also used for size critical messages (i.e. messages on BCCH, BR-BCCH, PCCH and CCCH), although introduced somewhat more carefully.

\- The extension fields introduced (or frozen) in a specific version of the specification are grouped together using double brackets.

\- Extension markers within ENUMERATED:

\- Spare values may be used until the number of values reaches the next power of 2, while the extension marker caters for extension beyond that limit, given that the use of spare values in a later Release is possible without any error cases.

\- A suffix of the form "vXYZ" is used for the identifier of each new value, e.g. "value-vXYZ".

\- Extension markers within CHOICE:

\- Extension markers are introduced when extension is foreseen and when comprehension is not required by the receiver i.e. behaviour is defined for the case where the receiver cannot comprehend the extended value (e.g. ignoring an optional CHOICE field). It should be noted that defining the behaviour of a receiver upon receiving a not comprehended choice value is not required if the sender is aware whether or not the receiver supports the extended value.

\- A suffix of the form "vXYZ" is used for the identifier of each new choice value, e.g. "choice-vXYZ".

Non-critical extensions at the end of a message/ of a field contained in an OCTET or BIT STRING:

\- When a nonCriticalExtension is actually used, a "Need" code should not be provided for the field, which always is a group including at least one extension and a field facilitating further possible extensions. For simplicity, it is recommended not to provide a "Need" code when the field is not actually used either.

Further, more general, guidelines:

\- In case a need code is not provided for a group, a "Need" code is provided for all individual extension fields within the group i.e. including for fields that are not marked as OPTIONAL. The latter is to clarify the action upon absence of the whole group.

### A.4.3.3 Typical example of evolution of IE with local extensions

The following example illustrates the use of the extension marker for a number of elementary cases (sequence, enumerated, choice). The example also illustrates how the IE may be revised in case the critical extension mechanism is used.

NOTE In case there is a need to support further extensions of release n while the ASN.1 of release (n+1) has been frozen, without requiring the release n receiver to support decoding of release (n+1) extensions, more advanced mechanisms are needed e.g. including multiple extension markers.

\-- /example/ ASN1START

InformationElement1 ::= SEQUENCE {

field1 ENUMERATED {

value1, value2, value3, value4-v880,

..., value5-v960 },

field2 CHOICE {

field2a BOOLEAN,

field2b InformationElement2b,

...,

field2c-v960 InformationElement2c-r9

},

...,

\[\[

field3-r9 InformationElement3-r9 OPTIONAL -- Need R

\]\],

\[\[

field3-v9a0 InformationElement3-v9a0 OPTIONAL, -- Need R

field4-r9 InformationElement4 OPTIONAL -- Need R

\]\]

}

InformationElement1-r10 ::= SEQUENCE {

field1 ENUMERATED {

value1, value2, value3, value4-v880,

value5-v960, value6-v1170, spare2, spare1, ... },

field2 CHOICE {

field2a BOOLEAN,

field2b InformationElement2b,

field2c-v960 InformationElement2c-r9,

...,

field2d-v12b0 INTEGER (0..63)

},

field3-r9 InformationElement3-r10 OPTIONAL, -- Need R

field4-r9 InformationElement4 OPTIONAL, -- Need R

field5-r10 BOOLEAN,

field6-r10 InformationElement6-r10 OPTIONAL, -- Need R

...,

\[\[

field3-v1170 InformationElement3-v1170 OPTIONAL -- Need R

\]\]

}

\-- ASN1STOP

Some remarks regarding the extensions of *InformationElement1* as shown in the above example:

– The *InformationElement1* is initially extended with a number of non-critical extensions. In release 10 however, a critical extension is introduced for the message using this IE. Consequently, a new version of the IE *InformationElement1* (i.e. *InformationElement1-r10*) is defined in which the earlier non-critical extensions are incorporated by means of a revision of the original field.

– The *value4-v880* is replacing a spare value defined in the original protocol version for *field1*. Likewise *value6-v1170* replaces *spare3* that was originally defined in the r10 version of *field1.*

– Within the critically extended release 10 version of *InformationElement1*, the names of the original fields/IEs are not changed, unless there is a real need to distinguish them from other fields/IEs. E.g. the *field1* and *InformationElement4* were defined in the original protocol version (release 8) and hence not tagged. Moreover, the *field3-r9* is introduced in release 9 and not re-tagged; although, the *InformationElement3* is also critically extended and therefore tagged *InformationElement3-r10* in the release 10 version of InformationElement1.

### A.4.3.4 Typical examples of non critical extension at the end of a message

The following example illustrates the use of non-critical extensions at the end of the message or at the end of a field that is contained in a BIT or OCTET STRING i.e. when an empty sequence is used.

\-- /example/ ASN1START

RRCMessage-r8-IEs ::= SEQUENCE {

field1 InformationElement1,

field2 InformationElement2,

field3 InformationElement3 OPTIONAL, -- Need N

nonCriticalExtension RRCMessage-v860-IEs OPTIONAL

}

RRCMessage-v860-IEs ::= SEQUENCE {

field4-v860 InformationElement4 OPTIONAL, -- Need S

field5-v860 BOOLEAN OPTIONAL, -- Cond C54

nonCriticalExtension RRCMessage-v940-IEs OPTIONAL

}

RRCMessage-v940-IEs ::= SEQUENCE {

field6-v940 InformationElement6-r9 OPTIONAL, -- Need R

nonCriticalExtensions SEQUENCE {} OPTIONAL

}

\-- ASN1STOP

Some remarks regarding the extensions shown in the above example:

– The *InformationElement4* is introduced in the original version of the protocol (release 8) and hence no suffix is used.

### A.4.3.5 Examples of non-critical extensions not placed at the default extension location

The following example illustrates the use of non-critical extensions in case an extension is not placed at the default extension location.

#### – *ParentIE-WithEM*

The IE *ParentIE-WithEM*is an example of a high level IE including the extension marker (EM). The root encoding of this IE includes two lower level IEs *ChildIE1-WithoutEM* and *ChildIE2-WithoutEM* which not include the extension marker. Consequently, non-critical extensions of the Child-IEs have to be included at the level of the Parent-IE.

The example illustrates how the two extension IEs *ChildIE1-WithoutEM-vNx0* and *ChildIE2-WithoutEM-vNx0* (both in release N) are used to connect non-critical extensions with a default extension location in the lower level IEs to the actual extension location in this IE.

***ParentIE-WithEM*** information element

\-- /example/ ASN1START

ParentIE-WithEM ::= SEQUENCE {

\-- Root encoding, including:

childIE1-WithoutEM ChildIE1-WithoutEM OPTIONAL, -- Need N

childIE2-WithoutEM ChildIE2-WithoutEM OPTIONAL, -- Need N

...,

\[\[

childIE1-WithoutEM-vNx0 ChildIE1-WithoutEM-vNx0 OPTIONAL, -- Need N

childIE2-WithoutEM-vNx0 ChildIE2-WithoutEM-vNx0 OPTIONAL -- Need N

\]\]

}

\-- ASN1STOP

Some remarks regarding the extensions shown in the above example:

– The fields *childIEx-WithoutEM-vNx0* may not really need to be optional (depends on what is defined at the next lower level).

– In general, especially when there are several nesting levels, fields should be marked as optional only when there is a clear reason.

#### *– ChildIE1-WithoutEM*

The IE *ChildIE1-WithoutEM* is an example of a lower level IE, used to control certain radio configurations including a configurable feature which can be setup or released using the local IE *ChIE1-ConfigurableFeature*. The example illustrates how the new field *chIE1-NewField* is added in release N to the configuration of the configurable feature. The example is based on the following assumptions:

– When initially configuring as well as when modifying the new field, the original fields of the configurable feature have to be provided also i.e. as if the extended ones were present within the setup branch of this feature.

– When the configurable feature is released, the new field should be released also.

– When omitting the original fields of the configurable feature the UE continues using the existing values (which is used to optimise the signalling for features that typically continue unchanged upon handover).

– When omitting the new field of the configurable feature the UE releases the existing values and discontinues the associated functionality (which may be used to support release of unsupported functionality upon handover to an eNB supporting an earlier protocol version).

The above assumptions, which affect the use of conditions and need codes, may not always apply. Hence, the example should not be re-used blindly.

***ChildIE1-WithoutEM*** information element

\-- /example/ ASN1START

ChildIE1-WithoutEM ::= SEQUENCE {

\-- Root encoding, including:

chIE1-ConfigurableFeature ChIE1-ConfigurableFeature OPTIONAL -- Need N

}

ChildIE1-WithoutEM-vNx0 ::= SEQUENCE {

chIE1-ConfigurableFeature-vNx0 ChIE1-ConfigurableFeature-vNx0 OPTIONAL -- Cond ConfigF

}

ChIE1-ConfigurableFeature ::= CHOICE {

release NULL,

setup SEQUENCE {

\-- Root encoding

}

}

ChIE1-ConfigurableFeature-vNx0 ::= SEQUENCE {

chIE1-NewField-rN INTEGER (0..31)

}

\-- ASN1STOP

| Conditional presence | Explanation                                                                                                                                                                                          |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *ConfigF*            | The field is optional present, need R, in case of chIE1-ConfigurableFeature is included and set to "setup"; otherwise the field is absent and the UE shall delete any existing value for this field. |

#### *– ChildIE2-WithoutEM*

The IE *ChildIE2-WithoutEM* is an example of a lower level IE, typically used to control certain radio configurations. The example illustrates how the new field *chIE1-NewField* is added in release N to the configuration of the configurable feature.

***ChildIE2-WithoutEM*** information element

\-- /example/ ASN1START

ChildIE2-WithoutEM ::= CHOICE {

release NULL,

setup SEQUENCE {

\-- Root encoding

}

}

ChildIE2-WithoutEM-vNx0 ::= SEQUENCE {

chIE2-NewField-rN INTEGER (0..31) OPTIONAL -- Cond ConfigF

}

\-- ASN1STOP

| Conditional presence | Explanation                                                                                                                                                                                          |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *ConfigF*            | The field is optional present, need R, in case of chIE2-ConfigurableFeature is included and set to "setup"; otherwise the field is absent and the UE shall delete any existing value for this field. |

A.4.3.6 Non-critical extensions of lists with ToAddMod/ToRelease

When the size of a list using the ToAddMod/ToRelease construction is extended and/or fields are added to the list element structure, the list should be non-critically extended in accordance with the following general principles:

– When only the size of the list is extended, this extension is reflected in a non-critical extension of the list, with a "SizeExt" suffix added to the end of the field name (before the -vNxy suffix). The differential size of the extended list uses the suffix "Diff". A new ToRelease list is needed, and its range should include only the increase in list size. In many cases, extending the list size will also require an extended list element ID type to account for the increased size of the list; in these cases the element type will need to be extended to include the extended element ID, resulting in a more complex extension (see example 3 for further discussion of this case). The field description table should indicate that the UE considers the original list and the extension list as a single list; thus entries added with the original list can be modified by the extension list (or removed by the extension of the ToRelease list), or vice versa. The result is as shown in the following example:

\-- /example 1/ ASN1START

ContainingStructure ::= SEQUENCE {

listElementToAddModList SEQUENCE (SIZE (1..maxNrofListElements)) OF ListElement OPTIONAL, -- Need N

listElementToReleaseList SEQUENCE (SIZE (1..maxNrofListElements)) OF ListElementId OPTIONAL, -- Need N

...,

\[\[

\-- Non-critical extension lists

listElementToAddModListSizeExt-vNxy SEQUENCE (SIZE (1..maxNrofListElementsDiff-rN)) OF ListElement OPTIONAL, -- Need N

listElementToReleaseListSizeExt-vNxy SEQUENCE (SIZE (1..maxNrofListElementsDiff-rN)) OF ListElementId OPTIONAL -- Need N

\]\]

}

\-- ASN1STOP

– When fields are added to the list element structure, an extension marker should normally be used if available. If no extension marker is available or if overhead or other considerations prevent using the extension marker, an extension structure should be created for the new fields, with the suffix "Ext" added to the end of the field name and the element structure type name (before the -vNxy suffix), and a parallel ToAddMod list introduced to hold the new structures, also with the "Ext" suffix. The field description table should indicate that the parallel list contains the same number of entries, and in the same order, as the original list. No new ToRelease list is typically needed (unless the list element ID type changes). It should typically be ensured that the contained fields in the "Ext" elements are releasable without release and add of the entire list element; this can, for instance, be ensured by having the new fields be OPTIONAL Need R. If multiple extensions of the same list are needed, the version suffix should distinguish the lists (e.g. *listElementToAddModListExt-vNwz* added after *listElementToAddModListExt-vNxy*). The result is as shown in the following example:

\-- /example 2/ ASN1START

ContainingStructure ::= SEQUENCE {

listElementToAddModList SEQUENCE (SIZE (1..maxNrofListElements)) OF ListElement OPTIONAL, -- Need N

listElementToReleaseList SEQUENCE (SIZE (1..maxNrofListElements)) OF ListElementId OPTIONAL, -- Need N

...,

\[\[

\-- Parallel list

listElementToAddModListExt-vNxy SEQUENCE (SIZE (1..maxNrofListElements)) OF ListElementExt-vNxy OPTIONAL -- Need N

\]\],

\[\[

\-- Second parallel list from a later spec version

listElementToAddModListExt-vNwz SEQUENCE (SIZE (1..maxNrofListElements)) OF ListElementExt-vNwz OPTIONAL -- Need N

\]\]

}

ListElement ::= SEQUENCE {

elementId ListElementId,

field1 INTEGER (0..3),

field2 ENUMERATED { value1, value2, value3 }

}

ListElementExt-vNxy ::= SEQUENCE {

field3-rN BIT STRING (SIZE (8)) OPTIONAL -- Need R

}

ListElementExt-vNwz ::= SEQUENCE {

field4-rN INTEGER (0..255) OPTIONAL -- Need R

}

\-- ASN1STOP

– When the size of a list is extended and fields are added to the list element structure, an extension marker should normally be used for the added fields if available, and the list extended with the non-critical mechanism as described in example 1 above*.* Note that if the list element ID type changes in this case, the new ID can be added after the extension marker, and the entries of the size-extended ToRelease list should have the type of the new ID (e.g. *ListElementId-vNxy*). If no extension marker is available or if overhead or other considerations prevent using the extension marker, an extension structure should be created for the new fields and a parallel list with ToAddMod introduced to hold the extension structures, as in the second example above, for entries of the original list and for entries of the extension list holding new entries. The field description table should indicate that the parallel list contains the same number of entries, and in the same order, as the concatenation of the original list and the extension list. An extended ToRelease list is needed, but no additional parallel ToRelease list is needed (i.e. there is no *listElementToReleaseListExt-vNxy* in the example below), as the original and extended ToRelease lists suffice to release any element of the combined list. The extended element ID type should be captured as a non-critical extension of the original element ID type, with the field description indicating that if the extended ID is present, the original ID is ignored. The result is as shown in the following example:

\-- /example 3/ ASN1START

ContainingStructure ::= SEQUENCE {

listElementToAddModList SEQUENCE (SIZE (1..maxNrofListElements)) OF ListElement OPTIONAL, -- Need N

listElementToReleaseList SEQUENCE (SIZE (1..maxNrofListElements)) OF ListElementId OPTIONAL, -- Need N

...,

\[\[

\-- Non-critical extension lists

listElementToAddModListSizeExt-vNxy SEQUENCE (SIZE (1..maxNrofListElementsDiff-rN)) OF ListElement OPTIONAL, -- Need N

listElementToReleaseListSizeExt-vNxy SEQUENCE (SIZE (1..maxNrofListElementsDiff-rN)) OF ListElementId-vNxy OPTIONAL, -- Need N

\-- Parallel list with maxNrofListElements-rN = maxNrofListElements + maxNrofListElementsDiff-rN

listElementToAddModListExt-vNxy SEQUENCE (SIZE (1..maxNrofListElements-rN)) OF ListElementExt-vNxy OPTIONAL -- Need N

\]\]

}

ListElement ::= SEQUENCE {

elementId ListElementId,

field1 INTEGER (0..3),

field2 ENUMERATED { value1, value2, value3 }

}

ListElementExt-vNxy ::= SEQUENCE {

\-- Field description should indicate that if the elementId-vNxy is present, the elementId (without suffix) is ignored

elementId-vNxy ListElementId-vNxy OPTIONAL, -- Need S

field3-rN BIT STRING (SIZE (8)) OPTIONAL -- Need R

}

ListElementId ::= INTEGER (0..maxNrofListElements-1)

ListElementId-vNxy ::= INTEGER (maxNrofListElements..maxNrofListElements-1-rN)

\-- ASN1STOP

– When different extensions are made to a list in separate releases, the extension mechanisms described above may interact. In case fields are added in Rel-M (*listElementToAddModListExt-vMxy*) and later the list size is extended in Rel-N (*listElementToAddModListSizeExt-vNwz*), the size-extended list in Rel-N should be a single list extending the combination of *listElementToAddModList* and *listElementToAddModListExt-vMxy*. This requires creating a new type (*ListElement-rN*) to contain the combined fields of *ListElement* and *ListElementExt-vMxy*. A corresponding ToRelease list is needed. The result is as shown in the following example:

\-- /example 4/ ASN1START

ContainingStructure ::= SEQUENCE {

listElementToAddModList SEQUENCE (SIZE (1..maxNrofListElements)) OF ListElement OPTIONAL, -- Need N

listElementToReleaseList SEQUENCE (SIZE (1..maxNrofListElements)) OF ListElementId OPTIONAL, -- Need N

...,

\[\[

\-- Parallel list (Rel-M)

listElementToAddModListExt-vMxy SEQUENCE (SIZE (1..maxNrofListElements)) OF ListElementExt-vMxy OPTIONAL -- Need N

\]\],

\[\[

\-- Size-extended list (Rel-N) with maxNrofListElements-rN = maxNrofListElements + maxNrofListElementsDiff-rN

listElementToAddModListSizeExt-vNwz SEQUENCE (SIZE (1..maxNrofListElementsDiff-rN)) OF ListElement-rN OPTIONAL, -- Need N

listElementToReleaseListSizeExt-vNwz SEQUENCE (SIZE (1..maxNrofListElementsDiff-rN)) OF ListElementId-vNwz OPTIONAL -- Need N

\]\]

}

ListElement ::= SEQUENCE {

elementId ListElementId,

field1 INTEGER (0..3),

field2 ENUMERATED { value1, value2, value3 }

}

ListElementExt-vMxy ::= SEQUENCE {

field3-rM BIT STRING (SIZE (8)) OPTIONAL -- Need R

}

ListElement-rN ::= SEQUENCE {

elementId-vNwz ListElementId-vNwz,

field1 INTEGER (0..3),

field2 ENUMERATED { value1, value2, value3 },

field3-rN BIT STRING (SIZE (8)) OPTIONAL -- Need R

}

ListElementId ::= INTEGER (0..maxNrofListElements-1)

ListElementId-vNwz ::= INTEGER (maxNrofListElements..maxNrofListElementsDiff-1-rN)

\-- ASN1STOP

# A.5 Guidelines regarding inclusion of transaction identifiers in RRC messages

The following rules provide guidance on which messages should include a Transaction identifier

1: DL messages on CCCH that move UE to RRC-Idle should not include the RRC transaction identifier.

2: All network initiated DL messages by default should include the RRC transaction identifier.

3: All UL messages that are direct response to a DL message with an RRC Transaction identifier should include the RRC Transaction identifier.

4: All UL messages that require a direct DL response message should include an RRC transaction identifier.

5: All UL messages that are not in response to a DL message nor require a corresponding response from the network should not include the RRC Transaction identifier.

# A.6 Guidelines regarding use of need codes

The following rule provides guidance for determining need codes for optional downlink fields:

\- if the field needs to be stored by the UE (i.e. maintained) when absent:

\- use Need M (=Maintain);

\- else, if the field needs to be released by the UE when absent:

\- use Need R (=Release);

\- else, if UE shall take no action when the field is absent (i.e. UE does not even need to maintain any existing value of the field):

\- use Need N (=None);

\- else (UE behaviour upon absence does not fit any of the above conditions):

\- use Need S (=Specified);

\- specify the UE behaviour upon absence of the field in the procedural text or in the field description table.

# A.7 Guidelines regarding use of conditions

Conditions are primarily used to specify network restrictions, for which the following types can be distinguished:

\- Message Contents related constraints e.g. that a field B is mandatory present if the same message includes field A and when it is set value X.

\- Configuration Constraints e.g. that a field D can only be signalled if field C is configured and set to value Y. (i.e. regardless of whether field C is present in the same message or previously configured).

The use of these conditions is illustrated by an example.

\-- /example/ ASN1START

RRCMessage-IEs ::= SEQUENCE {

fieldA FieldA OPTIONAL, -- Need M

fieldB FieldB OPTIONAL, -- Cond FieldAsetToX

fieldC FieldC OPTIONAL, -- Need M

fieldD FieldD OPTIONAL, -- Cond FieldCsetToY

nonCriticalExtension SEQUENCE {} OPTIONAL

}

\-- /example/ ASN1STOP

| *Conditional presence* | *Explanation*                                                                                                                                            |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *FieldAsetToX*         | The field is mandatory present if fieldA is included and set to valueX. Otherwise the field is optionally present, need R.                               |
| *FieldCsetToY*         | The field is optionally present, need M, if fieldC is configured and set to valueY. Otherwise the field is absent and the UE does not maintain the value |

# A.8 Miscellaneous

The following miscellaneous convention should be used:

\- UE capabilities: TS 38.306 \[26\] specifies that the network should in general respect the UE's capabilities. Hence there is no need to include statement clarifying that the network, when setting the value of a certain configuration field, shall respect the related UE capabilities unless there is a particular need e.g. particularly complicated cases.
