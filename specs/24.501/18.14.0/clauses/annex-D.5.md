# D.5 Message functional definition and contents

## D.5.1 Manage UE policy command

### D.5.1.1 Message definition

The MANAGE UE POLICY COMMAND message is sent by the PCF to the UE to request the UE to manage UE policy sections, see table D.5.1.1.1

Message type: MANAGE UE POLICY COMMAND

Significance: dual

Direction: network to UE

Table D.5.1.1.1: MANAGE UE POLICY COMMAND message content

<!-- table -->
| IEI | Information Element | Type/Reference | Presence | Format | Length |
|  | PTI | Procedure transaction identity 9.6 | M | V | 1 |
|  | MANAGE UE POLICY COMMAND message identity | UE policy delivery service message type D.6.1 | M | V | 1 |
|  | UE policy section management list | UE policy section management list D.6.2 | M | LV-E | 11-65533 |
| 42 | UE policy network classmark | UE policy network classmark D.6.7 | O | TLV | 3-5 |
| 70 | VPS URSP configuration | VPS URSP configuration D.6.8 | O | TLV-E | 3-65533 |
| NOTE: The total length of the MANAGE UE POLICY COMMAND message content cannot exceed 65535 octets (see Payload container contents maximum length as specified in clause 9.11.3.39.1). (x6) |
<!-- /table -->

### D.5.1.2 UE policy network classmark

The UE policy network classmark is included when the PCF of a PLMN or an SNPN intends to provide the UE with information about the policy aspects of the network.

### D.5.1.3 VPS URSP configuration

The VPS URSP configuration IE is included when the PCF of a PLMN intends to provide the UE with the VPS URSP configuration.

## D.5.2 Manage UE policy complete

### D.5.2.1 Message definition

The MANAGE UE POLICY COMPLETE message is sent by the UE to the PCF to report that all received instructions have been successfully executed at the UE, see table D.5.2.1.1

Message type: MANAGE UE POLICY COMPLETE

Significance: dual

Direction: UE to network

Table D.5.2.1.1: MANAGE UE POLICY COMPLETE message content

<!-- table -->
| IEI | Information Element | Type/Reference | Presence | Format | Length |
|  | PTI | Procedure transaction identity 9.6 | M | V | 1 |
|  | MANAGE UE POLICY COMPLETE message identity | UE policy delivery service message type D.6.1 | M | V | 1 |
<!-- /table -->

## D.5.3 Manage UE policy command reject

### D.5.3.1 Message definition

The MANAGE UE POLICY COMMAND REJECT message is sent by the UE to the PCF to report that one or more instructions could not be successfully executed at the UE, see table D.5.3.1.1

Message type: MANAGE UE POLICY COMMAND REJECT

Significance: dual

Direction: UE to network

Table D.5.3.1.1: MANAGE UE POLICY COMMAND REJECT message content

<!-- table -->
| IEI | Information Element | Type/Reference | Presence | Format | Length |
|  | PTI | Procedure transaction identity 9.6 | M | V | 1 |
|  | MANAGE UE POLICY COMMAND REJECT message identity | UE policy delivery service message type D.6.1. | M | V | 1 |
|  | UE policy section management result | UE policy section management result D.6.3 | M | LV-E | 11-65533 |
| NOTE: The total length of the MANAGE UE POLICY COMMAND REJECT message content cannot exceed 65535 octets (see Payload container contents maximum length as specified in clause 9.11.3.39.1). (x6) |
<!-- /table -->

## D.5.4 UE state indication

### D.5.4.1 Message definition

The UE STATE INDICATION message is sent by the UE to the PCF:

a\) to deliver the UPSI(s) of the UE policy section(s) stored in the UE;

b\) to indicate whether the UE supports ANDSP;

c\) to indicate whether the UE supports URSP provisioning in EPS in the UE policy classmark IE;

c1) to indicate whether the UE supports VPS URSP;

c2) to indicate whether the UE supports reporting URSP rule enforcement; and

d\) to deliver the UE's one or more OS IDs;

see table D.5.4.1.1.

Message type: UE STATE INDICATION

Significance: dual

Direction: UE to network

Table D.5.4.1.1: UE STATE INDICATION message content

<!-- table -->
| IEI | Information Element | Type/Reference | Presence | Format | Length |
|  | PTI | Procedure transaction identity 9.6 | M | V | 1 |
|  | UE STATE INDICATION message identity | UE policy delivery service message type D.6.1 | M | V | 1 |
|  | UPSI list | UPSI list D.6.4 | M | LV-E | 2-65531 |
|  | UE policy classmark | UE policy classmark D.6.5 | M | LV | 2-4 |
| 41 | UE OS Id | OS Id D.6.6 | O | TLV | 18-242 |
| NOTE: The total length of the UE STATE INDICATION message content cannot exceed 65535 octets (see Payload container contents maximum length as specified in clause 9.11.3.39.1). (x6) |
<!-- /table -->
