# C.2 Npcf_SMPolicyControl Service

## C.2.1 Service Description

### C.2.1.1 Overview

Clause 4.1.1 applies with the exception that the UE is replaced by the 5G-RG and the W-AGF, which is acting as a UE towards the 5GC on behalf of the FN-RG.

### C.2.1.2 Service Architecture

Clause 4.1.2 applies with the exception that roaming functionality does not apply for session policy control in this Release of the specification for 5G-RG users connecting to the 5GC via W-5GAN and FN-RG users. Roaming architecture is only applicable to a 5G-RG connecting to the 5GC via NG RAN.

The 5G-RG may support LTE access connected to EPC and EPC interworking as defined in Annex B.

### C.2.1.3 Network Functions

#### C.2.1.3.1 Policy Control Function (PCF)

The PCF functionality defined in clause 4.1.3.1 shall apply with the exceptions described in this Annex.

#### C.2.1.3.2 NF Service Consumers

The functionality defined in clause 4.1.3.2 shall apply.

The enforcement of the policy decisions applies for a single access PDU session over wireline access and multiaccess PDU sessions over wireline access and 3GPP with the exceptions described in this Annex.

### C.2.1.4 Rules

#### C.2.1.4.1 PCC Rules

Functionality as described in clause 4.1.4.2 applies with the following exceptions for the traffic of a PDU session over wireline access:

\- UL/DL Maximum Packet Loss Rate information does not apply.

\- QoS Notification Control Information does not apply.

#### C.2.1.4.2 Gate Function

Functionality as described in clause 4.2.6.2.2 applies with the following exceptions for the traffic of a PDU session over wireline access:

\- for the IPTV service, the "mulAccCtrl" attribute within the TrafficControlData data structure to which the PCC rule refers shall be used to describe if the gate is open or closed instead of the "flowStatus" attribute.

### C.2.1.5 Policy control request trigger

The Policy Control Request Triggers defined in clause 5.6.3.6 and related procedures are supported for a 5G-RG connecting to the 5GC via NG-RAN.

The Policy Control Request Triggers defined in clause 5.6.3.6 are supported for a 5G-RG or FN-RG connecting to the 5GC via W-5GAN with the following not supporting ones:

\- PLMN_CH

\- SAREA_CH

\- SCNN_CH

\- PRA_CH

\- PS_DA_OFF

\- QOS_NOTIF

\- RES_RELEASE

\- UE_STATUS_RESUME

\- TSN_BRIDGE_INFO

\- QOS_MONITORING

\- SCELL_CH

\- EPS_FALLBACK

\- DDN_FAILURE

\- DDN_DELIVERY_STATUS

\- DDN_FAILURE_CANCELLATION

\- DDN_DELIVERY_STATUS_CANCELLATION

\- USER_LOCATION_CH

\- UE_POL_CONT_IND

\- URSP_ENFORCEMENT_INFO

\- L4S_SUPP

\- VPLMN_QOS_CH

\- SAT_CATEGORY_CHG

\- NWDAF_DATA_CHG

\- BAT_OFFSET_INFO

\- HR_SBO_IND_CHG

Consequently, the procedures related to above policy control request triggers are not supported in the corresponding service operations.

The PS_DA_OFF Policy Control Request Trigger may apply for the 5G-RG connecting to the 5GC via W-5GAN (see clause 4.2.2.8 and 4.2.4.8) in an hybrid access scenario (see clause C.3.6.2).

The RES_MO_RE Policy Control Request trigger is not supported for a FN-RG as described in BBF TR-456 \[47\] and CableLabs WR-TR-5WWC-ARCH \[48\] specification.

### C.2.1.6 UE IP address support

The UE IP address support defined in clause 4.2.8 applies with the following additions, as specified in 3GPP TS 23.316 \[57\]:

\- IPv6 prefix other than default /64, including individual /128 IPv6 address, for IPv6 address allocation using DHCPv6;

\- More than one UE IP addresses may be assigned to a PDU session and may be received by the PCF, where the UE IP addresses may correspond, to:

a\. multiple /128 IPv6 addresses; or

b\. an /64 default prefix used for IPv6 stateless autoconfiguration and IPv6 prefix(es) shorter than the default /64 prefix for IPv6 Prefix Delegation not including the /64 IPv6 Prefix (i.e. when the total IPv6 address space available for the PDU session cannot be aggregated into one single IPv6 prefix).
