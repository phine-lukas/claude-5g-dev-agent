# D.6 Support for session/service continuity between SNPN and PLMN when using N3IWF

Depending on the UE's radio capability and implementation, the following existing mechanisms can be used to allow session/service continuity between SNPN and PLMN:

\- For Single Radio UE which includes single Rx/Tx and dual Rx/single Tx UE, seamless service continuity is not supported in this release when the UE is moving between the 3GPP access networks of SNPN and PLMN because of the single radio limitation. But the PDU session continuity between SNPN and PLMN can be realized by utilizing the existing handover procedure between non-3GPP access and 3GPP access as defined in clause 4.9.2 of TS 23.502 \[3\], where one network is acting as non-3GPP access of the other network.

\- For Dual Radio (Dual Rx/Dual Tx) UE, the service continuity can be achieved by utilizing the existing handover procedure between non-3GPP access and 3GPP access for PDU session on a single access and the existing user plane resource addition procedure for MA PDU session, where one network is acting as non-3GPP access of the other network

\- For PDU session on a single access, UE can register to the same 5GC via both Uu and NWu interfaces from two networks when it is possible, by following the procedure defined in clause 4.2.2 of TS 23.502 \[3\] if the registration is via Uu, or in clause 4.12.2 of TS 23.502 \[3\] if the registration is via NWu. The registration via NWu utilizes the user plane which is established in another 5GC using another network's Uu interface. For example, if UE is moving out of its SNPN 3GPP access coverage and would like to continue its SNPN service in PLMN, UE can register to its SNPN 5GC via PLMN's 3GPP access network using NWu interface with SNPN's 5GC before moving out SNPN NG-RAN coverage. Upon mobility, the existing handover procedure between non-3GPP access and 3GPP access defined in clause 4.9.2 of TS 23.502 \[3\] can be utilized.

\- For MA PDU session, if supported by UE and network, UE can register to the same 5GC via Uu and NWu interfaces and establish MA PDU session with ATSSS support to be anchored in the 5GC as defined in clause 4.22.2.2 of TS 23.502 \[3\], where one network is acting as non-3GPP access of the other network (Figure D.6-1 shows the example of UE with MA PDU session anchored in SNPN UPF when connected to SNPN via Uu and NWu interfaces). Upon mobility, UE can add/activate the user plane resource to the corresponding access type basing on the procedures defined in clause 4.22.7 of TS 23.502 \[3\].

[figure]

Figure D.6-1: MA PDU session with ATSSS support for dual radio UE accessing to Stand-alone Non-Public Network services via Uu and NWu interfaces
