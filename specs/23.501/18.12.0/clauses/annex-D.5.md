# D.5 Support for keeping UE in CM-CONNECTED state in overlay network when accessing services via NWu

When UE is accessing the overlay network via the underlay network as described in clause D.3, it is possible to keep the UE in CM-CONNECTED state in the overlay network:

\- UE maintains at least one PDU Session in underlay network, from where the N3IWF of the overlay network is reachable via the DN of the PDU Session in underlay network. In this case, the UE is considered as successfully connected to the non-3GPP access of the overlay network, thus UE always attempts to transit to CM-CONNECTED state from CM-IDLE, as described in NOTE 3 in clause 5.5.2.

\- IKEv2 liveness check procedure initiated either by UE or N3IWF as defined in clause 7.8 and clause 7.9 of TS 24.502 \[48\] can be utilized to ensure the signalling connection between UE and N3IWF is still valid when UE stays in CM-CONNECTED state. Adjusting the time interval of the liveness check to avoid the deletion of the IKEv2 SA due to inactivity, on both endpoints of the SA.

\- If NAT is used, so as to avoid a timeout of the NAT entries between the UPF in the underlay network and the N3IWF in the overlay network, NAT-Traversal mechanisms described in RFC 7296 \[60\] and NAT-Keepalive described in RFC 3948 \[138\] are recommended.

\- AMF in overlay network keeps the UE in CM-CONNECTED state unless UE or N3IWF triggers the release.

\- The NG-RAN node in the underlay network can use the existing information to decide an appropriate RRC state for the UE (e.g. whether release a UE to RRC_INACTIVE).
