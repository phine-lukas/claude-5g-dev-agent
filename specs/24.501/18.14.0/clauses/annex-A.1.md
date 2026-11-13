# A.1 Causes related to UE identification

Cause \#3 – Illegal UE

This 5GMM cause is sent to the UE when the network refuses service to the UE either because an identity of the UE is not acceptable to the network or because the UE does not pass the authentication check.

Cause \#6 – Illegal ME

This 5GMM cause is sent to the UE if the ME used is not acceptable to the network, e.g. on the prohibited list.

Cause \#9 – UE identity cannot be derived by the network.

This 5GMM cause is sent to the UE when the network cannot derive the UE's identity from the 5G-GUTI or 5G-S-TMSI because of e.g. no matching identity/context in the network, failure to validate the UE's identity due to integrity check failure of the received message.

Cause \#10 – Implicitly de-registered

This 5GMM cause is sent to the UE either if the network has implicitly de-registered the UE, e.g. after the implicit de-registration timer has expired, or if the 5GMM context data related to the subscription does not exist in the AMF e.g. because of a AMF restart, or because of a registration request for mobility or registration update is routed to a new AMF.
