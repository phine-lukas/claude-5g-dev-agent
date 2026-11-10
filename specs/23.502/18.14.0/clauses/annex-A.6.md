# A.6 Design Guidelines for NF services

Clause 7.1.1 of TS 23.501 \[2\] defines the criteria for defining the NF services. The following clauses identify the design guidelines that shall be considered for identifying the NF services.

## A.6.1 Self-Containment

The following design guidelines are used for identifying self-contained NF services.

\- Each NF service operates on its own set of context(s). A context refers to a state or a software resource or an internal data storage. The NF service operations can create, read, update or delete the context(s).

\- Any direct access of a context(s) owned by a NF service is be made by the service operations of that NF service. Services provided by the same NF can communicate internally within the NF.

## A.6.2 Reusability

The following design guidelines are used for specifying NF services to be reusable.

\- NF service operations are specified such that other NF can potentially invoke them in future, if required.

\- The service operations may be usable in multiple system procedures specified in clause 4 of this specification.

\- Using clause 4 of the current document, the system procedures in which the NF service operations can be used are considered and based on that the parameters for the NF service operations are clearly listed.

NOTE: It is possible that, when mapping an end to end call flow to service based architecture, one step in the call flow may map to multiple NF service operation invocations. This specification clearly identifies each NF service operation invocation in the call flow. Protocol optimization of multiple NF service operation invocations are left for TS 29.500 \[17\] consideration.

## A.6.3 Use Independent Management Schemes

The mechanisms for independent management schemes are not in scope of this specification.

########  Annex B (informative): Drafting Rules for Information flows

The following drafting rules are recommended for information flows specified in this specification in order to ensure that the Control Plane network functions can be supported with service based interfaces:

1\. Information flows should describe the end to end functionality. NF services in clause 5 shall only be derived from the information flows in clause 4.

2\. Information flows should strive to use type of interactions such as REQUEST/RESPONSE (e.g. location request, location response), SUBSCRIBE/NOTIFY between Core CP NFs. Any other type of interactions described should have justifications for its use.

3\. Information flows should also ensure readability thus the semantics of the REQUEST/RESPONSE should still be maintained (for instance, we need to indicate PDU Session request, PDU Session response and Subscribe for UE location reporting/Notify UE location reporting) for readers and developers to understand the need for a certain transaction.

NOTE: As stated in TS 23.501 \[2\], service based interface is not supported for N1, N2, N4. Thus, the rules are not meant for those interfaces.

########  Annex C (informative): Generating EPS PDN Connection parameters from 5G PDU Session parameters

This annex specifies how to generate the EPS PDN connection parameters from the 5G PDU Session parameters in SMF+PGW-C.

When the SMF+PGW-C is requested to set up/modify either a PDN connection or a PDU session supporting interworking between EPS and 5GS, the SMF+PGW-C generates the PDN Connection parameters from the PDU session parameters.

When the SMF+PGW-C generates the PDN Connection parameters based on the PDU Session parameters, the following rules hold:

\- PDN type: the PDN type is set to IPv4, IPv6 or IPv4v6 if the PDU Session Type is IPv4, IPv6 or IPv4v6, respectively. The PDN Type is set to Ethernet if the MME, SGW and UE support Ethernet PDN Type, otherwise the PDN type is set to Non-IP for Ethernet and Unstructured PDU Session Types

\- EPS bearer ID: the EBI is requested from the AMF during the establishment of a QoS Flow as described in clause 4.11.1.4.1 for PDU Sessions supporting interworking between EPS and 5GS. The EBI is obtained from MME during the establishment of an EPS Bearer (that is triggered by an establishment of a QoS Flow) as defined in TS 23.401 \[13\] for PDN Connections hosted by SMF+PGW-C. The association between EBI and QoS Flow is stored by the SMF.

\- APN-AMBR: APN-AMBR is set according to operator policy (e.g. taking the Session AMBR into account).

\- EPS QoS parameters (including ARP, QCI, GBR and MBR):

If QoS Flow is mapped to one EPS bearer, ARP, GBR and MBR of the EPS Bearer is set to the ARP, GFBR and MFBR of the corresponding QoS Flow, respectively. For standardized 5QIs, the QCI is one to one mapped to the 5QI. For non-standardized 5QIs, the SMF+PGW-C derives the QCI based on the 5QI and operator policy.

A GBR QoS Flow is mapped 1 to 1 to a GBR dedicated EPS Bearer if an EBI has been assigned. After mobility to EPS traffic flows corresponding to GBR QoS Flow for which no EBI has been assigned will continue flowing on the default EPS bearer if it does not have assigned TFT.

If multiple QoS Flows are mapped to one EPS bearer, the EPS bearer parameters are set based on operator policy, e.g. EPS bearer QoS parameters are set according to the highest QoS of all mapped QoS Flows.

After mobility to EPS traffic flows corresponding to Non-GBR QoS Flows for which no EBI has been assigned will continue flowing on the default EPS Bearer if it does not have assigned TFT.

########  Annex D (normative): UE Presence in Area of Interest
