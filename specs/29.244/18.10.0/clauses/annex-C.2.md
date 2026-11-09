# C.2 Charging Support

## C.2.1 Online Charging

### C.2.1.1 Online Charging Call Flow – Normal Scenario

Figure C.2.1.1-1 illustrates the exchanges taking place over the Sxb or Sxc reference points when applying online charging. In this example, the OCS grants quotas by chunks of 100 Mbytes and requests the CP function to request new credits when the remaining credit falls below 10 Mbytes.

[figure]

Figure C.2.1.1-1: Online charging with intermediate and final quotas

1\. Upon the request from the CP function, the OCS grants an intermediate quota of 100 Mbytes and requests the CP function to request a new credit when the remaining credit falls below 10 Mbytes.

2\. The CP function sends a PFCP Session Modification Request to the UP function with an Update URR IE including the Volume Threshold IE set to 90 Mbytes and the Volume Quota IE set to 100 Mbytes.

3\. Upon reaching the Volume Threshold (i.e. 90 Mbytes), the UP function sends a PFCP Session Report Request to the CP function with a Usage Report IE including the Usage Report Trigger set to "Volume Threshold" and the Volume Measurement set to 90 Mbytes. The UP function continues to pass on traffic until reaching the Volume Quota (i.e. an extra 10 Mbytes of traffic can be passed on).

4\. Upon the request from the CP function, the OCS grants a new intermediate quota of 100 Mbytes and requests the CP function to request a new credit when the remaining credit falls below 10 Mbytes.

5\. The CP function sends a PFCP Session Modification Request to the UP function with an Update URR IE including the Volume Threshold IE set to 90 Mbytes and the Volume Quota IE set to 100 Mbytes. If the UP function had forwarded e.g. 5 Mbytes of traffic since the last usage report, the UP function knows that it shall send the next usage report upon passing on an extra 85 Mbytes of traffic.

6\. Upon reaching the Volume Threshold (i.e. 90 Mbytes), the UP function sends a PFCP Session Report Request to the CP function with a Usage Report IE including the Usage Report Trigger set to "Volume Threshold" and the Volume Measurement set to 90 Mbytes. The UP function continues to pass on traffic until reaching the Volume Quota (i.e. an extra 10 Mbytes of traffic can be passed on).

7\. Upon the request from the CP function, the OCS grants a new final quota of 50 Mbytes and requests the CP function to terminate the service or to redirect the traffic towards a redirect destination when the quota is consumed.

8\. The CP function sends a PFCP Session Modification Request to the UP function with an Update URR IE including the Volume Quota IE set to 50 Mbytes. If the UP function had forwarded e.g. 5 Mbytes of traffic since the last usage report, the UP function knows that it shall send the next usage report upon passing on an extra 45 Mbytes of traffic.

9\. Upon reaching the Volume Quota (i.e. 50 Mbytes), the UP function sends a PFCP Session Report Request to the CP function with a Usage Report IE including the Usage Report Trigger set to "Volume Quota" and the Volume Measurement set to 50 Mbytes. The UP function stops passing on traffic.

10\. Upon being notified that the final quota has been reached, the CP function terminates the service (e.g. by preventing the traffic of the corresponding SDF to further pass on in the UP function) or redirects the traffic towards a redirect destination by provisioning a Redirect Information IE within the FAR associated to the traffic.

Figure C.2.1.1-2 illustrates the exchanges taking place over the Sxb or Sxc reference points when applying online charging and the UP function supports being provisioned with the Quota Action to apply when reaching quotas. This example is similar to the previous one, but the CP function provisions the UP function with the action to apply when reaching the final quota.

[figure]

Figure C.2.1.1-2: Online charging with Quota Action provisioned in the UP function

1 to 7'. Same as for figure C.2.1.1-1.

8\. The CP function sends a PFCP Session Modification Request to the UP function with a Create FAR IE provisioning the action the UP function shall apply when reaching the quota, and with an Update URR IE including the Volume Quota IE set to 50 Mbytes and the FAR ID for Quota Action IE set to the new FAR ID). If the UP function had forwarded e.g. 5 Mbytes of traffic since the last usage report, the UP function knows that it shall send the next usage report upon passing on an extra 45 Mbytes of traffic.

9\. Upon reaching the Volume Quota (i.e. 50 Mbytes), the UP function sends a PFCP Session Report Request to the CP function with a Usage Report IE including the Usage Report Trigger set to "Volume Quota" and the Volume Measurement set to 50 Mbytes.

10\. The UP function applies the quota action provisioned at step 8, i.e. it stops forwarding packets or it redirects the traffic towards a redirect destination, according to the FAR identified in the FAR ID for Quota Action.

### C.2.1.2 Online Charging Call Flow with Credit Pooling

#### C.2.1.2.1 General

Figure C.2.1.2-1 illustrates a signalling flow over the Sxb and Gy reference points when applying online charging, and when the CP function (i.e. PGW-C) is instructed by the OCS to handle a Credit Pool for a given Gy Session.

#### C.2.1.2.2 Example Call Flow 1

In this example, the PGW-C is instructed by the OCS to handle a credit pool for two Rating Groups, RG1 and RG2. The PGW-C provisions two URRs, URR1 and URR2, for the two RGs respectively, and a URR3 for the Credit Pool. The PGW-C provisions the URR1 and URR2 with the quota received from the OCS respectively for RG1 and RG2 (like if there was no credit pooling).

This reflects one possible implementation option, whereby each quota remains managed independently from the others. This approach can result in extra usage reports being sent over Sxb for RG1 or RG2 before the credit pool is exhausted.

[figure]

Figure C.2.2.2-1: Online charging with Credit Pooling (alt 1)

1\. Upon the request from the CP function for RG1 and RG2, the OCS grants:

RG1: quota 100 Mbytes, together with a G-S-U-Pool-Reference AVP included within the Multiple Services Credit Control (for RG1), where the G-S-U-Pool-Identifier AVP indicating the identifer (e.g. 1000) of the Credit Pool to which the RG1 pertains, the CC-Unit-Type AVP specifies the type of units for which credit is (e.g. total octets), the Unit-Value AVP specifies the multiplier (e.g. 0.1);

RG2: quotas 100 Mbytes, together with a G-S-U-Pool-Reference AVP included within the Multiple Services Credit Control (for RG2), where the G-S-U-Pool-Identifier AVP indicating the identifer (e.g. 1000) of the Credit Pool to which the RG2 pertains, the CC-Unit-Type AVP specifies the type of units for which credit is (e.g. total octets), the Unit-Value AVP specifies the multiplier (e.g. 0.5);

2\. The CP function sends a PFCP Session Modification Request to the UP function, to create:

A new URR1 for RG1, quota=100, Linked URR = URR3;  
A new URR2 for RG2, quota=100, Linked URR = URR3;  
A new URR3 for Pool, quota = S = 100 x 0.1 + 100 x 0.5 = 60, Aggregated URRs: URR1 with Multiplier 0.1 and URR2 with Multiplier 0.5.

The UP function accepts the request.

3\. The RG1 has consumed 100 counted by URR1, RG2 consumed 10 counted by URR2; the URR3 for the Credit Pool counts U = 100 x 0.1 + 10 x 0.5 = 15 \< S. The URR1 triggers sending a usage report towards the CP function due to reaching the Quota 100. So the UP function sends a PFCP Session Report Request, including the Usage Reports for the URR1. The CP function sends the response message.

4\. Based on operator's policies, the CP function reports used quota for the RG1 to the OCS. The OCS does not grant any quota since the quota for the Credit Pool has not been consumed yet.

NOTE: This step is skipped in the rest flow.

5\. The CP function sends a PFCP Session Modification Request to the UP function with the modified URR1, with new quota 100.

Step 6, 7, 8 and 9 repeats step 3 and 5.

10\. The RG1 has consumed another 100 counted by URR1, RG2 consumed another 10 counted by URR2; the URR3 for the Credit Pool counts U = (100 + 100 + 100 + 100) x 0.1 + (10 +10 + 10 + 10) x 0.5 = 60 \>= S = 60. So the UP function sends a PFCP Session Report Request, including the Usage Reports for:  
- the URR3, generated due to reaching quota (60),  
- for the URR1, generated due to that it is linked to the URR3 and it has reached the quota 100, and  
- for the URR2 generated due to that it is linked to the URR3.  
The CP function sends the response message.

11\. The CP function requests new Quota for RG1 and RG2 to the OCS. The OCS grants 200M for RG1 and 100M for RG2, with the same pool ID and Multipliers.

12\. The CP function sends a PFCP Session Modification Request to the UP function with the modified URRs, for URR1, URR2 and URR3.

#### C.2.1.2.3 Example Call Flow 2

In this example, the PGW-C is instructed by the OCS to handle a credit pool for two Rating Groups, RG1 and RG2. The PGW-C provisions two URRs, URR1 and URR2, for the two RGs respectively, and a URR3 for the Credit Pool. The PGW-C provisions the quotas for URR1 and URR2 taking into account the credit pool quota and the multipliers of the RGs.

This reflects another possible implementation option. This approach avoids extra usage reports being sent over Sxb for RG1 or RG2 before the credit pool is exhausted, and thus reduces Sxb signalling.

[figure]

Figure C.2.2.3-2: Online charging with Credit Pooling (alt 2)

1\. Upon the request from the CP function for RG1 and RG2, the OCS grants:

RG1: quota 100 Mbytes, together with a G-S-U-Pool-Reference AVP included within the Multiple Services Credit Control (for RG1), where the G-S-U-Pool-Identifier AVP indicating the identifer (e.g. 1000) of the Credit Pool to which the RG1 pertains, the CC-Unit-Type AVP specifies the type of units for which credit is (e.g. total octets), the Unit-Value AVP specifies the multiplier (e.g. 0.1);

RG2: quotas 100 Mbytes, together with a G-S-U-Pool-Reference AVP included within the Multiple Services Credit Control (for RG2), where the G-S-U-Pool-Identifier AVP indicating the identifer (e.g. 1000) of the Credit Pool to which the RG2 pertains, the CC-Unit-Type AVP specifies the type of units for which credit is (e.g. total octets), the Unit-Value AVP specifies the multiplier (e.g. 0.5);

2\. The CP function sends a PFCP Session Modification Request to the UP function, to create:

A new URR1 for RG1, quota=600, Linked URR = URR3;  
A new URR2 for RG2, quota=120, Linked URR = URR3;  
And new URR3 for Pool, quota = S = 100 x 0.1 + 100 x 0.5 = 60, Aggregated URRs: URR1 with Multiplier 0.1 and URR2 with Multiplier 0.5.

The UP function accepts the request.

NOTE 1: To avoid receiving usage report upon exceeding the original Quota for RG1 or RG2, the quota can be set to 60 / 0.1 = 600 for RG1, assuming RG1 consumes the complete Quota for the pool; similarly, for RG2, the quota can be set to 60 / 0.5 = 120;

3\. The URR3 always first reaches the Quota, e.g. when the URR1 has counted 400, and URR2 has counted 40, this results the counted usage for the Credit Pool U=400 x 0.1 + 40 x 0.5 = 60. So the UP function sends a PFCP Session Report Request, including the Usage Reports:

\- for the URR3, generated due to that it has reached quota (60);  
- for the URR1, generated due to that it is linked to the URR3; and  
- for the URR2, generated due to that it is linked to the URR3.

The CP function sends the response message.

4\. The CP function requests new Quota for RG1 and RG2 to the OCS. The OCS grants 200M for RG1 and 100M for RG2, with the same pool ID and Multipliers.

5\. The CP function sends a PFCP Session Modification Request to the UP function with the modified URRs, for URR1, URR2 and URR3.

URR1 for RG1, quota=70 / 0.1 = 700;
  
URR2 for RG2, quota=70 / 0.5 = 140;
  
URR3 for The Credit Pool, quota = 200 x 0.1 + 100 x 0.5 = 70.

######## Annex D (Normative): Use of PFCP over N16a for the support of traffic offload by UPF controlled by I-SMF
