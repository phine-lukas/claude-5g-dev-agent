# D.1 General

## D.1.1 Overview

The UE provides the PCF with a list of one or more stored UE policy section identifiers (UPSIs) during the UE-initiated UE state indication procedure. The UPSI is composed of two parts:

a\) a PLMN ID part containing:

1\) the PLMN ID for the PLMN; or

2\) the PLMN ID part of the SNPN identity for the SNPN;

of the PCF which provides the UE policies; and

b\) a UE policy section code (UPSC) containing a value assigned by the PCF.

During the UE-initiated UE state indication procedure, the UE also provides the PCF with the UE policy related capabilities such as the UE's support for ANDSP, the UE's support for URSP provisioning in EPS, and the UE's OS Id.

During the network-requested UE policy management procedure, the PCF provides the UE with one or more UE policy sections containing UE policies. The UE processes the received UE policy sections, each identified by the UPSI, received from the PCF and informs the PCF of the result.

In the present annex, the condition that the PLMN ID part of the UPSI is referring to the HPLMN shall be considered as fulfilled only if the PLMN ID is equal to the HPLMN code derived from the IMSI.

NOTE: This is also applicable if the UE has a non-empty EHPLMN list, even if the EHPLMN list does not include the PLMN ID derived from the IMSI.

The UE can also request the PCF to provide V2XP as specified in 3GPP TS 24.587 \[19B\].

The UE can also request the PCF to provide ProSeP as specified in 3GPP TS 24.554 \[19E\].

The UE can also request the PCF to provide A2XP as specified in 3GPP TS 24.577 \[60\].

The UE can also request the PCF to provide RSLPP as specified in 3GPP TS 24.514 \[62\].

## D.1.2 Principles of PTI handling for UE policy delivery service procedures

When the PCF or the UE initiates a procedure, it shall include a valid PTI value in the message header of the command message or the request message. When the UE initiates a procedure, the UE shall use a PTI value in range between 01H and 77H. When the PCF initiates a procedure, the PCF shall use a PTI value in range between 80H and FEH.

When the PCF initiates a transaction related procedure (i.e. a procedure consisting of more than one message and the messages are related), it shall include a valid PTI value in the message header of the command message.

If a response message is sent as result of a received command or request message, the UE or the PCF shall include in the response message the PTI value received within the received command or request message (see examples in figure D.1.2.1, figure D.1.2.2 and figure D.1.2.3).

If a command message is sent as result of a received request message, the PCF shall include in the command message the PTI value received with the request message (see examples in figure D.1.2.3).

[figure]

Figure D.1.2.1: Network-requested transaction related procedure

[figure]

Figure D.1.2.2: UE-requested transaction related procedure rejected by the network

[figure]

Figure D.1.2.3: UE-requested transaction related procedure triggering a network-requested transaction related procedure

NOTE: In earlier versions of this protocol, the UE can include in the response message a PTI value which is not the same as the one received within the command message, and therefore the PCF could not associate the response message from the UE to the command message sent.
