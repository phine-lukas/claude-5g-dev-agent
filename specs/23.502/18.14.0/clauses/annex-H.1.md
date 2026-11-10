# H.1 Introduction

Secondary authentication/authorization by a DN-AAA Server during the establishment of a PDN connection over 3GPP access to EPC, is supported based on following principles:

\- A SMF+PGW-C shall be used to serve DNN(s) requiring secondary authentication/authorization by a DN-AAA Server.

\- For secondary authentication/authorization by a DN-AAA Server, the SMF+PGW-C runs the same procedures with PCF, UDM and DN-AAA and uses the same corresponding interfaces, as defined in clause 4.3.2, regardless of whether the UE is served by EPC or 5GC.

\- If the UE has included the PDU Session ID in PCO, the UE may indicate in the PCO within the PDN connection establishment request its support for EAP-based secondary authentication and authorization by DN-AAA over EPC. The UE may also include the DN-specific identity in the PCO. The SMF+PGW-C may reject the PDN connection establishment if the UE does not support EAP-based secondary authentication and authorization by DN-AAA over EPC while local policies tell that secondary authentication and authorization by DN-AAA is mandatory to access to the DN. When a PDU Session is established, the UE may also indicate via 5GSM capability parameter that it supports secondary DN authentication and authorization over EPC.

\- The interface towards the UE is different (usage of EPC NAS instead of 5GC NAS) between the EPC and 5GC cases.

\- The MME and SGW are not impacted by the procedure. Specific exchanges between the UE and the SMF+PGW-C for secondary authentication/authorization by a DN-AAA Server are carried via PCO. This includes the support of EAP exchanges between the UE and the DN-AAA Server.

\- As it is only possible to exchange PCO once between the UE and the PGW during PDN connection establishment, the PDN connection is established before EAP-based secondary authentication/authorization by a DN-AAA Server takes place.

\- When secondary authentication/authorization by a DN-AAA Server has successfully taken place, the SMF+PGW-C allows traffic exchange at the UPF and indicates to the UE that User plane traffic is now possible.
