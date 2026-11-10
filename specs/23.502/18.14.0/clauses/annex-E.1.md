# E.1 Delegated SMF discovery in the Home Routed scenario

[figure]

Figure E.1: Delegated Discovery of SMF in the Home Routed Scenario

1\. The AMF sends Nnrf_NFDiscovery Request to the V-NRF. The AMF may indicate the maximum number of H-SMF instances to be returned by the NRF.

2\. The NRF in VPLMN and NRF in HPLMN interact using the Nnrf_NFDiscovery service. See step 2 in clause 4.17.5.

3\. The AMF gets Nnrf_NFDiscovery service response with one or more profile(s) of SMF(s) in HPLMN.

4\. The AMF selects an SMF instance in HPLMN (H-SMF endpoint).

5\. The AMF builds a Nsmf_PDUSession_CreateSMContext Request that includes the endpoint (e.g. URI) of the selected H-SMF in the body of the request. If the AMF supports delegated SMF discovery and is configured to apply it, the AMF sends the Nsmf_PDUSession_CreateSMContext Request with Discovery & Selection parameters to the selected SCP in the VPLMN. Discovery & Selection parameters include S-NSSAI, UE location (TAI), i.e. parameter for V-SMF selection.

6\. \[Optional\] The SCP in VPLMN sends Nnrf_NFDiscovery Request to the V-NRF using Discovery & Selection parameters received from AMF.

7\. \[Optional\] The SCP in VPLMN gets Nnrf_NFDiscovery service response with profile(s) of SMF(s) in VPLMN.

8\. The SCP in VPLMN selects an SMF instance in VPLMN (V-SMF), which supports the Discovery & Selection parameters received earlier from the AMF.

9\. The SCP in VPLMN forwards the Nsmf_PDUSession_CreateSMContext Request received from the AMF to the selected SMF instance in VPLMN.

10\. If the V-SMF does not support delegated SMF discovery or is not configured to apply it (Case A), the V-SMF sends Nsmf_PDUSession_Create Request directly to the H-SMF. Otherwise (Case B), the V-SMF sends the Nsmf_PDUSession_Create Request to the SCP in VPLMN but adds Discovery & Selection parameter set to H-SMF endpoint received from the AMF. In both cases, the V-SMF uses the received endpoint (e.g. URI) of the selected H-SMF to construct the target destination to be addressed.

NOTE: The Nsmf_PDUSession_Create Request sent by the V-SMF in Case A and in Case B is the same apart from the Discovery & Selection parameter. The Nsmf_PDUSession_Create Request received by the H-SMF in Case A and in Case B is the same.

11\. The SCP in VPLMN sends a Nsmf_PDUSession_Create Request to the selected SMF instance in HPLMN indicated in step 10.

When the V-SMF responds to AMF with Nsmf_PDUSession_CreateSMContext Response as in clause 4.3.2.2.2 in step 3b, if the AMF has not stored the SMF Service Area for the V-SMF, the AMF shall obtain the SMF Service Area for the concerned V-SMF from the NRF using the Nnrf_NFManagement_NFStatusSubscribe service operation.
