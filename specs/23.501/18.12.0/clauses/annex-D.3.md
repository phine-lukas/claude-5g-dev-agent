# D.3 Support for access to PLMN services via Stand-alone Non-Public Network and access to Stand-alone Non Public Network services via PLMN

[figure]

Figure D.3-1: Access to PLMN services via Stand-alone Non-Public Network

NOTE 1: The reference architecture in Figure D.3-1 and Figure D.3-2 only shows the network functions directly connected to the UPF or N3IWF and other parts of the architecture are same as defined in clause 4.2.

In order to obtain access to PLMN services when the UE is camping in NG-RAN of Stand-alone Non-Public Network, the UE obtains IP connectivity, discovers and establishes connectivity to an N3IWF in the PLMN.

In the Figure D.3-1, the N1 (for NPN) represents the reference point between UE and the AMF in Stand-alone Non-Public Network. The NWu (for PLMN) represents the reference point between the UE and the N3IWF in the PLMN for establishing secure tunnel between UE and the N3IWF over the Stand-alone Non-Public Network. N1 (for PLMN) represents the reference point between UE and the AMF in PLMN.

[figure]

Figure D.3-2: Access to Stand-alone Non-Public Network services via PLMN

In order to obtain access to Non-Public Network services when the UE is camping in NG-RAN of a PLMN, the UE obtains IP connectivity, discovers and establishes connectivity to an N3IWF in the Stand-alone Non-Public Network.

In Figure D.3-2, the N1 (for PLMN) represents the reference point between UE and the AMF in the PLMN. The NWu (for NPN) represents the reference point between the UE and the N3IWF in the stand-alone Non-Public Network for establishing a secure tunnel between UE and the N3IWF over the PLMN. The N1 (for NPN) represents the reference point between UE and the AMF in NPN.

When using the mechanism described above to access overlay network via underlay network, the overlay network can act as authorized 3rd party with AF to interact with NEF in the underlay network, to use the existing network exposure capabilities provided by the underlay network defined in clause 4.15 of TS 23.502 \[3\]. This interaction is subject of agreements between the overlay and the underlay network.
