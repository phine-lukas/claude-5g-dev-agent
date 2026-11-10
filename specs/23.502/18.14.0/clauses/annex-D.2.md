# D.2 Determination of UE presence in Area of Interest by NG-RAN

If the AMF has requested for the Area of Interest, NG-RAN determines the UE presence of Area Of Interest as follows:

\- IN:

\- if the UE is inside the Area Of Interest and the UE is in RRC_CONNECTED state; or

\- if the UE is inside an RNA which is completely contained within the Area Of Interest.

\- OUT:

\- if the UE is outside the Area Of Interest in RRC_CONNECTED state; or

\- if UE is inside an RNA which does not contain any part of Area Of Interest.

\- UNKNOWN:

\- if none of above conditions for IN or OUT is met.

########  Annex E (normative): Delegated SMF and PCF discovery in the Home Routed and specific SMF Service Areas scenarios
