# N.5 Support for leaving network that provides access to Localized Services

When Localized Services in a network are completed, all UEs that are registered with the network are expected to be transferred to other network or to other network resources (e.g. other cells) within the same network, potentially within a relatively short timeframe. The other network can be HPLMN, VPLMN or another SNPN.

UE can stop using the network resources for Localized Services for numerous reasons, e.g. when one or more of the following conditions apply:

\- Localized Services in a network are completed.

\- Validity conditions of network selection information are no longer met.

\- The user decides to stop using the Localized Services before they are completed.

\- A policy decision is taken by the network, with the effect that the UE is deregistered before the Localized Services are completed.

NOTE: The list is not an exhaustive list and UE can stop using the network resources for Localized Services due to other reasons e.g. UE loses coverage, power off.

When large number of UEs move to other network (i.e. HPLMN, VPLMN or another SNPN) or other network resources within a relatively short timeframe, the total signalling involved can cause signalling overload in the target network.

Existing mechanisms for Control Plane Load Control, Congestion and Overload Control described in clause 5.19 and access control and barring described in clause 5.2.5 can be used to mitigate the signalling overload caused by returning UEs. For further enhancement of mitigation of signalling overload, additional mechanisms can be implemented to ensure spreading of the load that returning UEs cause. Such mechanisms are implementation-specific, but some guidelines that can be considered are described below:

\- The time validity of the network selection information given to a UE can be set somewhat longer than the actual duration of the service, e.g. users will by themselves disable Localized Service and the UE then stops using the connectivity to access the Localized Service, thus causing the UE to be moved, e.g. by performing normal network selection.

\- The time validity of the network selection information given to a UE can be different for each UE so that each UE performs network selection at a different time to distribute returning UEs.

\- When the AMF after end of Localized Services triggers deregistration of UEs, the deregistration requests can be sent at a certain rate in an adaptive and distributed manner, with the effect that the signalling load on both the source network and the target network is limited.

\- When the AMF after end of Localized Services triggers UE configuration update procedure, e.g. to remove S-NSSAI from the Allowed NSSAI (if dedicated S-NSSAI is used for the Localized Service), the requests can be sent at a certain rate, with the effect that the signalling load in the network is limited.

When the NAS level congestion control is activated at AMF as specified in clause 5.19.7.2, to prevent a UE staying in an SNPN for accessing for Localized Services but not able to get services from the SNPN due to the congestion, additional mechanism can be implemented. Such mechanisms are implementation-specific but some guidelines that can be considered are described below:

\- the AMF can determine whether to reject the UE with a proper cause without Mobility Management back-off timer to allow the UE to reselect another SNPN for Localized Services.
