# N.6 Configuration of Credentials Holder for determining SNPN selection information

To enable the HPLMN or the subscribed SNPN acting as Credentials Holder to generate and provision UEs with SNPN selection information for discovery and selection of SNPNs providing Localized Services, based on Localized Service agreements between the Localized Service Provider or the SNPN providing Localized Services and the HPLMN or the subscribed SNPN acting as Credentials Holder, the Localized Service Provider or the SNPN providing access to Localized Services can provide configuration information for SNPN selection to the HPLMN or the subscribed SNPN acting as Credentials Holder. The configuration information for SNPN selection may contain at least one of the following parameters:

a\. SNPN ID or GIN of the SNPN providing access to one or more Localized Services;

b\. Identification of each Localized Service;

c\. validity information (e.g. time validity information and optionally location validity information) for each Localized Service and/or location assistance information; and/or

d\. List of UE IDs (e.g. GPSIs or External Group ID) identifying the UEs subscribed with a Localized Service.

NOTE: How HPLMN or subscribed SNPN obtains the information above as part of the Localized Service agreements is out of 3GPP scope.

The operator of the HPLMN or the subscribed SNPN acting as Credentials Holder then may use the information received from the SNPN providing Localized Services and/or Localized Service Provider to create or update the Credentials Holder controlled prioritized lists of preferred SNPNs/GINs for accessing Localized Services and provision the UEs using the Steering of Roaming procedure as defined in TS 23.122 \[17\].

######## Annex O (informative): Allowing UE to simultaneously send data to different groups with different QoS policy

This Annex provides deployment examples allowing a UE to simultaneously send data to different groups (i.e. IP or Ethernet multicast groups) with different QoS policy as in clause 6.13.2 of TS 22.261 \[2\].
