# F.5 5GS DetNet node information reporting

The TSCTSF collects the information for Deterministic Networking from the UPF/NW-TT and the SMF as shown in Figure F.5-1, with the addition of new parameters as shown in Figure F.5-1.

[figure]

Figure F.5-1: 5GS DetNet node information reporting

1\. PDU Session Establishment as defined clause 4.3.2.2.1-1 is used to establish a PDU Session. When Framed Routes applies, the SMF reports to the PCF Framed Route information.

2\. SMF reports device port related information to PCF. When prefix delegation applies, the SMF reports to the PCF prefixes delegated to the UE by IPv6 prefix delegation. The PCF notifies TSCTSF of the Bridge/Router information. The TSCTSF subscribes for notifications on the Bridge/Router information and also subscribes for notifications on Reporting of extra addresses, so that the TSCTSF is notified when the SMF has reported to the PCF the Framed Route information or prefixes delegated to UE via IPv6 prefix delegation corresponding to the PDU Session.

3-4. Using the 5GS user-plane Node ID received in step 2b the TSCTSF can subscribe with the NW-TT for receiving user plane node management information changes for the 5GS router indicated by the 5GS user-plane Node ID in case it does not yet have such a subscription, as described in clause 5.28.3.1 of TS 23.501 \[2\].

After receiving a User plane node Management Information Container (UMIC) containing the NW-TT port numbers, the TSCTSF can subscribe with the NW-TT for receiving NW-TT port management information changes for the NW-TT port indicated by each of the NW-TT port numbers as described in clause 5.28.3.1 of TS 23.501 \[2\].

The TSCTSF can use any PDU Session to subscribe with the NW-TT for node or port management information notifications. Similarly, the UPF can use any PDU Session to send bridge or port management information notifications.

5\. The TSCTSF may provide collected exposure information to the DetNet controller. The information being reported to the DetNet controller is defined in clause 5.28.5.2 of TS 23.501 \[2\].
