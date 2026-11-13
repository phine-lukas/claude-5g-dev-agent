# D.2 Procedures

## D.2.1 Network-requested UE policy management procedure

### D.2.1.1 General

The purpose of the network-requested UE policy management procedure is to enable the network to:

a\) add one or more new UE policy sections to the UE;

b\) modify one or more UE policy sections stored at the UE; or

c\) delete one or more UE policy sections stored at the UE;

and optionally to enable the HPLMN or the subscribed SNPN to provide a UE accessing the subscribed SNPN or the HPLMN with a non-subscribed SNPN signalled URSP handling indication indicating whether the UE is allowed to accept URSP signalled by non-subscribed SNPNs.

### D.2.1.2 Network-requested UE policy management procedure initiation

In order to initiate the network-requested UE policy management procedure, the PCF shall:

a\) if the network-requested UE policy management procedure is triggered by the UE-requested V2X policy provisioning procedure as specified in 3GPP TS 24.587 \[19B\], the UE-requested ProSe policy provisioning procedure as specified in 3GPP TS 24.554 \[19E\] or the UE-requested A2X policy provisioning procedure as specified in 3GPP TS 24.577 \[60\], then set the PTI IE to the PTI value of the received UE POLICY PROVISIONING REQUEST message of the UE-requested V2X policy provisioning procedure, the UE-requested ProSe policy provisioning procedure or the UE-requested A2X policy provisioning procedure, otherwise allocate a PTI value currently not used and set the PTI IE to the allocated PTI value;

b\) encode the information about the UE policy sections to be added, modified or deleted in a UE policy section management list IE as specified in clause D.6.2 and include it in a MANAGE UE POLICY COMMAND message;

c\) if the PCF is a PCF of the HPLMN or the subscribed SNPN, optionally include the UE policy network classmark IE in a MANAGE UE POLICY COMMAND message and set the non-subscribed SNPN signalled URSP handling indication of the UE policy network classmark IE to "UE is not allowed to accept URSP signalled by non-subscribed SNPNs", or "UE is allowed to accept URSP signalled by non-subscribed SNPNs";

c1) if the UE supports VPS URSP, optionally encode the information about entries of VPS URSP configuration to be added, modified or deleted in the VPS URSP configuration IE as specified in clause D.6.8 and include it in a MANAGE UE POLICY COMMAND message;

d\) send the MANAGE UE POLICY COMMAND message to the UE via the AMF as specified in 3GPP TS 23.502 \[9\]; and

e\) start timer T3501 (see example in figure D.2.1.2.1).

NOTE: The PCF starts a different timer T3501 for each PTI value.

[figure]

Figure D.2.1.2.1: Network-requested UE policy management procedure

Upon receipt of the MANAGE UE POLICY COMMAND message with a PTI value currently not used by a network-requested UE policy management procedure, for each instruction included in the UE policy section management list IE, the UE shall:

a\) store the received UE policy section of the instruction, if the UE has no stored UE policy section associated with the same UPSI as the UPSI associated with the instruction;

b\) replace the stored UE policy section with the received UE policy section of the instruction, if the UE has a stored UE policy section associated with the same UPSI as the UPSI associated with the instruction; or

c\) delete the stored UE policy section, if the UE has a stored UE policy section associated with the same UPSI as the UPSI associated with the instruction and the UE policy section of the instruction is empty;

additionally, if the UE policy network classmark IE is included in the MANAGE UE POLICY COMMAND message, and

a\) the UE has an empty EHPLMN list or the EHPLMN list is not present, and the UE's RPLMN is the HPLMN;

b\) the UE has a non-empty EHPLMN list, and the UE's RPLMN is an EHPLMN; or

c\) the UE's RSNPN is the subscribed SNPN,

the UE shall delete the non-subscribed SNPN signalled URSP handling indication stored for the selected entry of "list of subscriber data" or the selected PLMN subscription, if any, and store the non-subscribed SNPN signalled URSP handling indication received in the UE policy network classmark IE, for the selected entry of "list of subscriber data" or the selected PLMN subscription.

If the UE supports the VPS URSP, and the VPS URSP configuration is included in the MANAGE UE POLICY COMMAND message:

a\) if the replacement type field of the received VPS URSP configuration indicates "full list of tuples", the UE shall delete the stored VPS URSP configuration, if any; and

b\) if the received VPS URSP configuration contains one or more tuples:

1\) if the UE does not have the stored VPS URSP configuration, the UE shall store the received VPS URSP configuration except zero or more tuples with no UPSCs; or

2\) otherwise:

i\) for each tuple with a tuple ID in the stored VPS URSP configuration:

A\) if a tuple with the tuple ID is in the received VPS URSP configuration and contains:

\- no UPSCs, the UE shall delete the tuple with the tuple ID from the stored VPS URSP configuration; or

\- one or more UPSCs, the UE shall replace the tuple with the tuple ID in the stored VPS URSP configuration with the tuple with the tuple ID from the received VPS URSP configuration; or

B\) if no tuple with the tuple ID is in the received VPS URSP configuration, the UE shall keep the tuple with the tuple ID in the stored VPS URSP configuration; and

ii\) for each tuple with a tuple ID in the received VPS URSP configuration, if no tuple with the tuple ID is in the stored VPS URSP configuration and:

A\) the tuple with the tuple ID in the received VPS URSP configuration contains no UPSCs, the UE shall ignore the tuple with the tuple ID in the received VPS URSP configuration; or

B\) the tuple with the tuple ID in the received VPS URSP configuration contains one or more UPSCs, the UE shall add the tuple with the tuple ID from the received VPS URSP configuration to the stored VPS URSP configuration.

The UE may continue storing a received UE policy section for a PLMN or SNPN when the UE registers in another PLMN or SNPN. If necessary, the UE may delete UE policy sections stored for a PLMN other than the RPLMN and the HPLMN or for an SNPN other than the registered SNPN and the subscribed SNPN, before storing the new received UE policy sections.

When storing a UE policy section received from an SNPN, the UE shall associate the NID of that SNPN with the UPSI of the stored UE policy section.

NOTE: The maximum number of UE policy sections for PLMNs or SNPNs other than the HPLMN and the RPLMN or the registered SNPN and the subscribed SNPN that the UE can store and how the UE selects the UE policy sections to be deleted are up to the UE implementation.

### D.2.1.3 Network-requested UE policy management procedure accepted by the UE

If all instructions included in the UE policy section management list IE were executed successfully by the UE, the UE shall:

a\) create a MANAGE UE POLICY COMPLETE message including the PTI value received within the MANAGE UE POLICY COMMAND message; and

b\) transport the MANAGE UE POLICY COMPLETE message using the NAS transport procedure as specified in clause 5.4.5.

Upon receipt of the MANAGE UE POLICY COMPLETE message, the PCF shall stop timer T3501. The PCF should ensure that the PTI value assigned to this procedure is not released immediately.

NOTE: The way to achieve this is implementation dependent. For example, the PCF can ensure that the PTI value assigned to this procedure is not released during the time equal to or greater than the default value of timer T3501.

### D.2.1.4 Network-requested UE policy management procedure not accepted by the UE

If the UE could not execute all instructions included in the UE policy section management list IE successfully, the UE shall:

a\) set the PTI IE to the PTI value received within the MANAGE UE POLICY COMMAND message and encode the results by including:

1\) the UPSI associated with the instructions which could not be executed successfully;

2\) the failed instruction order set to order of the instruction in the UE policy section management sublist of the received UE policy section management list IE which could not be executed successfully; and

3\) the cause of the failure,

in the UE policy section management result IE as specified in clause D.5.3 and include it in a MANAGE UE POLICY COMMAND REJECT message, and

b\) transport the MANAGE UE POLICY COMMAND REJECT message using the NAS transport procedure as specified in clause 5.4.5.

Upon receipt of the MANAGE UE POLICY COMMAND REJECT message, the PCF shall stop timer T3501. Any instruction that was included in the UE policy section management list IE but not indicatedin the UE policy section management result IE of the received MANAGE UE POLICY COMMAND REJECT message, shall be considered as successfully executed.

The PCF should ensure that the PTI value assigned to this procedure is not released immediately.

NOTE: The way to achieve this is implementation dependent. For example, the PCF can ensure that the PTI value assigned to this procedure is not released during the time equal to or greater than the default value of timer T3501.

Upon receipt of the notification from the AMF that the UE is not reachable, the PCF shall stop the T3501.

### D.2.1.5 Abnormal cases on the network side

The following abnormal cases can be identified:

a\) T3501 expired.

The PCF shall, on the first expiry of the timer T3501, retransmit the MANAGE UE POLICY COMMAND message and shall reset and start timer T3501. This retransmission is repeated four times, i.e. on the fifth expiry of timer T3501, the PCF shall abort the procedure and release the allocated PTI.

### D.2.1.6 Abnormal cases in the UE

The following abnormal cases can be identified:

a\) Receipt of an instruction associated with a UPSI which has a PLMN ID part that is not equal to the PLMN ID of the UE's HPLMN and the instruction contains a UE policy part with a UE policy part type set to "URSP" for a UE not operating in SNPN access operation mode, or receipt of an instruction associated with a UPSI which has a PLMN ID part that is not equal to the PLMN ID part of the selected SNPN and the instruction contains a UE policy part with a UE policy part type set to "URSP" for a UE operating in SNPN access operation mode.

The UE shall set the UE policy delivery service cause to \#111 "Protocol error, unspecified" for the instruction in the UE policy section management result IE of the MANAGE UE POLICY COMMAND REJECT message.

b\) Receipt of an instruction associated with a UPSI which has a PLMN ID part that is not equal to the PLMN ID of the UE's HPLMN or the UE's RPLMN and the instruction contains a UE policy part with a UE policy part type set to "ANDSP" for a UE not operating in SNPN access operation mode or receipt of an instruction associated with a UPSI which has a PLMN ID part that is not equal to the PLMN ID part of the subscribed SNPN or the UE's RSNPN and the instruction contains a UE policy part with a UE policy part type set to "ANDSP" for a UE operating in SNPN access operation mode.

The UE shall set the UE policy delivery service cause to \#111 "Protocol error, unspecified" for the instruction in the UE policy section management result IE of the MANAGE UE POLICY COMMAND REJECT message.

c\) Transmission failure of the MANAGE UE POLICY COMPLETE message indication from lower layers.

The UE shall not diagnose an error and consider the network-requested UE policy management procedure is complete.

NOTE 1: Considering the network-requested UE policy management procedure is complete as the result of this abnormal case, does not cause the UE to revert the execution of the successfully executed instructions included in the MANAGE UE POLICY COMMAND message.

d\) Transmission failure of the MANAGE UE POLICY COMMAND REJECT message indication from lower layers.

The UE shall not diagnose an error and consider the network-requested UE policy management procedure is complete.

NOTE 2: Considering the network-requested UE policy management procedure is complete as the result of this abnormal case, does not cause the UE to revert the execution of the successfully executed instructions included in the MANAGE UE POLICY COMMAND message.

e\) Receipt of a MANAGE UE POLICY COMMAND message with a PTI set to the same value as the PTI of a previously received MANAGE UE POLICY COMMAND message.

The UE shall discard the message and retransmit the MANAGE UE POLICY COMMAND COMPLETE or MANAGE UE POLICY COMMAND REJECT message transmitted in response to the previously received MANAGE UE POLICY COMMAND message.

NOTE 3: The way to achieve this is UE implementation dependent. For example, the UE can assume that on the fifth expiry of timer T3501, the PCF will abort the procedure and that the PTI value assigned to the procedure will be released.

f\) Receipt of an instruction associated with a UPSI which has a PLMN ID part that is equal to the PLMN ID part of the selected SNPN, the instruction contains a UE policy part with a UE policy part type set to "URSP", UE's RSNPN is a non-subscribed SNPN and:

1\) the UE has a stored non-subscribed SNPN signalled URSP handling indication for the selected entry of "list of subscriber data" or the selected PLMN subscription indicating that the UE is not allowed to accept URSP signalled by non-subscribed SNPNs; or

2\) the UE does not have a stored non-subscribed SNPN signalled URSP handling indication for the selected entry of "list of subscriber data" or the selected PLMN subscription, and the non-subscribed SNPN signalled URSP handling indication preconfigured in the selected entry of "list of subscriber data" or the selected PLMN subscription indicates that the UE is not allowed to accept URSP signalled by non-subscribed SNPNs;

for a UE operating in SNPN access operation mode.

The UE shall set the UE policy delivery service cause to \#111 "Protocol error, unspecified" for the instruction in the UE policy section management result IE of the MANAGE UE POLICY COMMAND REJECT message.

## D.2.2 UE-initiated UE state indication procedure

### D.2.2.1 General

The purpose of the UE-initiated UE state indication procedure is:

a\) to deliver the UPSI(s) of the UE policy section(s) which are:

\- identified by a UPSI with the PLMN ID part indicating the HPLMN or the selected PLMN, and stored in the UE, if any; or

\- identified by a UPSI with the PLMN ID part indicating the PLMN ID part of the SNPN identity of the selected SNPN and associated with the NID of the selected SNPN, and stored in the UE, if any;

b\) to indicate whether UE supports ANDSP;

c\) to indicate whether UE supports URSP provisioning in EPS;

c1) to indicate whether UE supports VPS URSP;

d\) to indicate whether UE supports reporting URSP rule enforcement; and

e\) to deliver the UE's one or more OS IDs;

to the PCF.

### D.2.2.2 UE-initiated UE state indication procedure initiation

In order to initiate the UE-initiated UE state indication procedure, the UE shall create a UE STATE INDICATION message. The UE:

a\) shall allocate a PTI value currently not used and set the PTI IE to the allocated PTI value;

b\) if not operating in SNPN access operation mode, shall include the UPSI(s) of the UE policy section(s) which are identified by a UPSI with the PLMN ID part indicating the HPLMN or the selected PLMN available in the UE in the UPSI list IE, if any;

NOTE 1: If the UE does not have any UE policy section which is identified by a UPSI with the PLMN ID part indicating the HPLMN or the selected PLMN, the UE sets the Length of UPSI list contents field in the UPSI list IE to zero.

c\) if operating in SNPN access operation mode, shall include UPSI(s) of the UE policy section(s) which are identified by a UPSI:

\- with the PLMN ID part indicating the MCC and MNC of the selected SNPN; and

\- associated with the NID of the selected SNPN;

available in the UE in the UPSI list IE, if any;

NOTE 2: If the UE does not have any UE policy section which is identified by a UPSI with the PLMN ID part indicating the MCC and MNC of the selected SNPN and associated with the NID of the selected SNPN, the UE sets the Length of UPSI list contents field in the UPSI list IE to zero.

d\) shall specify whether the UE supports ANDSP in the UE policy classmark IE;

e\) shall specify whether the UE supports URSP provisioning in EPS in the UE policy classmark IE;

NOTE 3: ANDSP and URSP are specified in 3GPP TS 24.526 \[19\].

e1) if the UE supports VPS URSP, shall set the SVPSU bit to "VPS URSP supported by the UE" in the UE policy classmark IE;

f\) if the UE supports reporting URSP rule enforcement, shall set the SupportRURE bit to "Reporting URSP rule enforcement supported by the UE"; and

g\) may include the UE's one or more OS IDs in the UE OS Id IE.

The UE shall send the UE STATE INDICATION message (see example in figure D.2.2.2.1). The UE shall transport the created UE STATE INDICATION message using the registration procedure (see clause 5.5.1).

[figure]

Figure D.2.2.2.1: UE-initiated UE state indication procedure

### D.2.2.3 UE-initiated UE state indication procedure accepted by the network

Upon receipt of the UE STATE INDICATION message, the PCF shall operate as described in 3GPP TS 23.502 \[9\] and 3GPP TS 29.525 \[21\].

### D.2.2.4 Abnormal cases on the network side

Apart from the case described in clause D.2.2.3, no abnormal cases have been identified.
