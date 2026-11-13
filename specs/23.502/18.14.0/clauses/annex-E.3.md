# E.3 Delegated PCF discovery in the Roaming scenario

[figure]

Figure E.3: Delegated Discovery of PCF in the Home Routed Scenario

1\. The AMF sends Nnrf_NFDiscovery Request to the V-NRF in order to discover a PCF in HPLMN. The AMF may indicate the maximum number of H-PCF instances to be returned by the NRF.

2\. The NRF in VPLMN and NRF in HPLMN interact using the Nnrf_NFDiscovery service. See step 2 in clause 4.17.5.

3\. The AMF gets Nnrf_NFDiscovery service response with one or more profile(s) of PCF(s) in HPLMN.

4\. The AMF selects a PCF instance in HPLMN.

5\. The AMF builds a Npcf_UEPolicyControl Request that contains the H-PCF ID in the body of the request. If the AMF supports delegated PCF discovery and is configured to apply it, the AMF forwards the Npcf_UEPolicyControl Request to the selected SCP in VPLMN together with Discovery & Selection parameter set to V-PCF instance ID.

6\. The SCP in VPLMN selects the corresponding (V-)PCF instance for UE policy association based on Discovery & Selection parameter received from the AMF.

7\. The SCP in VPLMN forwards the Npcf_UEPolicyControl Request to the selected PCF instance in VPLMN.

8\. If the V-PCF does not support delegated PCF discovery or is not configured to apply it (Case A), the V-PCF sends Npcf_UEPolicyControl Request to the selected PCF instance. Otherwise (Case B), the V-PCF sends the Npcf_UEPolicyControl Request to a SCP in VPLMN but adds Discovery & Selection parameter set to H-PCF ID.

9\. The SCP in VPLMN sends an Npcf_UEPolicyControl Request to the selected PCF instance in HPLMN indicated in step 8.

######## Annex F (informative): Information flows for 5GS integration with TSN or with Deterministic Networking

This annex defines the procedures for 5GS integration with TSN fully-centralized model as defined in IEEE Std 802.1Q \[66\], it includes 5GS Bridge information reporting and 5GS Bridge configuration.

The annex defines also the procedures for 5GS interworking with the TSN deployed in the transport network, as described in clause 5.28a of TS 23.501 \[2\].
