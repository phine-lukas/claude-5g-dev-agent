# D.2 Support of Non-Public Network as a network slice of a PLMN

The PLMN operator can provide access to an NPN by using network slicing mechanisms.

NOTE: Access to PLMN services can be supported in addition to PNI-NPN services, e.g. based on different S-NSSAI/DNN for different services.

The following are some considerations in such a PNI-NPN case:

1\. The UE has subscription and credentials for the PLMN;

2\. The PLMN and NPN service provider have an agreement of where the NPN Network Slice is to be deployed (i.e. in which TAs of the PLMN and optionally including support for roaming PLMNs);

3\. The PLMN subscription includes support for Subscribed S-NSSAI to be used for the NPN (see clause 5.15.3);

4\. The PLMN operator can offer possibilities for the NPN service provider to manage the NPN Network Slice according to TS 28.533 \[79\].

5\. When the UE registers the first time to the PLMN, the PLMN can configure the UE with URSP including NSSP associating Applications to the NPN S-NSSAI (if the UE also is able to access other PLMN services);

6\. The PLMN can configure the UE with Configured NSSAI for the Serving PLMN (see clause 5.15.4);

7\. The PLMN and NPN can perform a Network Slice specific authentication and authorization using additional NPN credentials;

8\. The UE follows the logic as defined for Network Slicing, see clause 5.15;

9\. The network selection logic, access control etc are following the principles for PLMN selection; and

10\. The PLMN may indicate to the UE that the NPN S-NSSAI is rejected for the RA when the UE moves out of the coverage of the NPN Network Slice. However, limiting the availability of the NPN S-NSSAI would imply that the NPN is not available outside of the area agreed for the NPN S-NSSAI, e.g. resulting in the NPN PDU Sessions being terminated when the UE moves out of the coverage of the NPN Network Slice. Similarly access to NPN DNNs would not be available via non-NPN cells.

11\. In order to prevent access to NPNs for authorized UE(s) in the case of network congestion/overload and if a dedicated S-NSSAI has been allocated for an NPN, the Unified Access Control can be used using the operator-defined access categories with access category criteria type (as defined in TS 24.501 \[47\]) set to the S-NSSAI used for an NPN.

12\. If NPN isolation is desired, it is assumed that a dedicated S-NSSAI is configured for the NPN and that the UE is configured to operate in Access Stratum Connection Establishment NSSAI Inclusion Mode a, b or c, see clause 5.15.9, such that NG-RAN receives Requested NSSAI from the UE and it can use the S-NSSAI for AMF selection.
