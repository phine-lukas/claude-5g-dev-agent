# E.2 Multipath TCP Connection Setup

## E.2.1 General

Multipath TCP Connection is setup between the MPTCP Client in the UE and the MPTCP Proxy in the UPF (PSA). The outgoing Multipath is initiated by the MPTCP Client in the UE towards the MPTCP Proxy in the UPF.

NOTE: The incoming Multipath which is assumed to be initiated by the MPTCP Proxy in the UPF towards the MPTCP Client in the UE is not supported in this release of the specification.

The RTT TCP Convert Protocol (specified in IETF RFC 8803 \[60\]) is used to setup Multipath TCP connection and used for data exchange. The MPTCP Proxy implements the Transport Converter functionality.

## E.2.2 Outgoing Multipath TCP Connection Setup

Figure E.2.2-1 describes the establishment of an outgoing multipath TCP connection through a Transport Converter.

The MPTCP Client initiates a Multipath TCP connection towards the Transport Converter, by sending a SYN with the MP_CAPABLE option (MPC in Figure E.2.2-1). The SYN includes the address and port number of the Server (i.e. remote host), that are extracted by the Transport Converter and used to initiate a Multipath TCP connection towards this Server. As the Server does not support Multipath TCP, it replies with a SYN+ACK that does not contain the MP_CAPABLE option. The Transport Converter notes that the connection with the Server does not support Multipath TCP and returns the extended TCP header received from the Server to the Client.

[figure]

Figure E.2.2-1 – Outgoing Converter-Assisted Multipath TCP Connection Setup

## E.2.3 Incoming Multipath TCP Connection Setup

Incoming Multipath TCP Connection Setup as described in clause 5.2 of IETF RFC 8803 \[60\] is not supported in this release of the specification.

## E.2.4 MPTCP Session Entry Stored in MPTCP Proxy

Once Multipath TCP Connection is successfully setup between the MPTCP Client in the UE and the MPTCP Proxy in the UPF, the MPTCP Proxy stores the MPTCP session entry in its storage.

The MPTCP session entry includes the following information:

\- MPTCP link-specific multipath IP address and the associated TCP ports;

\- UE's MA-PDU session IP address and its TCP port, if the MA-PDU session IP address is used by MPTCP Proxy for IP translation;

\- N6 routable IP address and its TCP port, if N6 routable IP address is used by the MPTCP Proxy for IP translation;

\- the remote host IP address and its TCP port.

The stored MPTCP session entry is used by the MPTCP Proxy for IP translation when receiving uplink or downlink MPTCP traffic.
