### C.3.6.1 IPTV service support

If the "WWC" feature is supported by the SMF and PCF as defined in clause 5.8, when the PCF fetches the Multicast Access Control information from the UDR as defined in 3GPP TS 29.519 \[15\] applicable for a SUPI or Internal Group Id during the PDU session establishment or receives the notification of the Multicast Access Control information from the UDR as defined in 3GPP TS 29.519 \[15\] applicable for a SUPI(s) and/or Internal Group Id(s) and/or DNN/S-NSSAI combination(s) during the PDU session modification, the PCF authorizes the Multicast Access Control information. For each impacted PDU Session that corresponds to the Multicast Access Control information, the PCF shall determine the PCC rule(s) that are generated based on the Multicast Access Control information as follows:

\- for the multicast channel(s) which is allowed indicated in the Multicast Access Control information, the PCF shall include the corresponding multicast address(es) within the "flowInfos" attribute of the PCC rule and include the "mulAccCtrl" attribute set to "ALLOWED" within a Traffic Control Data instance which the PCC rule refers to.

\- for the multicast channel(s) which is not allowed indicated in the Multicast Access Control information, the PCF shall include the corresponding multicast address(es) within the "flowInfos" attribute of the PCC rule and include the "mulAccCtrl" attribute set to "NOT_ALLOWED" within a Traffic Control Data instance which the PCC rule refers to.

NOTE 1: The "flowStatus" attribute is not included in this Traffic Control Data instance. The gate fuction is not applicable to IPTV service, and the control is done with the "mulAccCtrl" attribute.

NOTE 2: Separate PCC Rules are used to convey the information related to allowed and not allowed multicast channel(s).
