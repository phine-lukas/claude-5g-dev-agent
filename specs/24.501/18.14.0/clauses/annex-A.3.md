# A.3 Causes related to PLMN or SNPN specific network failures and congestion/authentication failures

Cause \#20 – MAC failure

This 5GMM cause is sent to the network if the USIM detects that the MAC in the AUTHENTICATION REQUEST message is not fresh.

Cause \#21 – Synch failure

This 5GMM cause is sent to the network if the USIM detects that the SQN in the AUTHENTICATION REQUEST message is out of range.

Cause \#22 – Congestion

This 5GMM cause is sent to the UE because of congestion in the network (e.g. no channel, facility busy/congested etc.).

Cause \#23 – UE security capabilities mismatch

This 5GMM cause is sent to the network if the UE detects that the UE security capability does not match the one sent back by the network.

Cause \#24 – Security mode rejected, unspecified

This 5GMM cause is sent to the network if the security mode command is rejected by the UE for unspecified reasons.

Cause \#26 – Non-5G authentication unacceptable

This 5GMM cause is sent to the network in N1 mode if the "separation bit" in the AMF field of AUTN is set to 0 in the AUTHENTICATION REQUEST message (see 3GPP TS 33.501 \[24\]).

Cause \#28 – Restricted service area

This 5GMM cause is sent to the UE if it requests service in a tracking area of the 3GPP access or in an area of the wireline access, which is a part of the UE's non-allowed area or is not a part of the UE's allowed area.

Cause \#43 – LADN not available

This 5GMM cause is sent to the UE if the user-plane resources of the PDU session are not established when the UE is located outside the LADN service area.

Cause \#62 – No network slices available

This 5GMM cause is sent by the network if there are no available network slices allowed for use by the UE.

NOTE: Network does not send this cause in REGISTRATION REJECT message if the UE does not include a requested NSSAI in the REGISTRATION REQUEST message. In that case, if the UE is not registered for onboarding services in SNPN, the network uses other causes (e.g. \#13, \#15, etc.) based on the subscription.

Cause \#65 – Maximum number of PDU sessions reached

This 5GMM cause is used by the network to indicate that the procedure requested by the UE was rejected as the network has reached the maximum number of simultaneously active PDU sessions for the UE.

Cause \#67 – Insufficient resources for specific slice and DNN

This 5GMM cause is sent by the network to indicate that the requested service cannot be provided due to insufficient resources for specific slice and DNN.

Cause \#69 – Insufficient resources for specific slice

This 5GMM cause is sent by the network to indicate that the requested service cannot be provided due to insufficient resources for specific slice.

Cause \#71 – ngKSI already in use

This 5GMM cause is sent to the network in N1 mode if the ngKSI value received in the AUTHENTICATION REQUEST message is already associated with one of the 5G security contexts stored in the UE.

Cause \#73 – Serving network not authorized

This 5GMM cause is sent to the UE if the UE initiates registration towards a serving network and the serving network fails to be authorized by the UE's home network.

Cause \#78 –PLMN not allowed to operate at the present UE location

This 5GMM cause is sent to the UE to indicate that the PLMN is not allowed to operate at the present UE location.

NOTE: This cause is only applicable for satellite NG-RAN access.

Cause \#81 – Selected N3IWF is not compatible with the allowed NSSAI

This 5GMM cause is sent by the network to indicate that the requested service cannot be provided due to the selected N3IWF is not compatible with the allowed NSSAI.

Cause \#82 – Selected TNGF is not compatible with the allowed NSSAI

This 5GMM cause is sent by the network to indicate that the requested service cannot be provided due to the selected TNGF is not compatible with the allowed NSSAI.

Cause \#90 – Payload was not forwarded

This 5GMM cause is sent by the network to indicate that the requested service cannot be provided because payload could not be forwarded by AMF.

Cause \#91 – DNN not supported or not subscribed in the slice

This 5GMM cause is sent by the network to indicate that the requested service cannot be provided because payload could not be forwarded by AMF because the DNN is not supported or not subscribed in the slice selected by the network if the UE did not indicate a slice, or the DNN is not supported or not subscribed in the slice indicated by the UE.

Cause \#92 – Insufficient user-plane resources for the PDU session

This 5GMM cause is sent by the network to indicate that the requested service cannot be provided due to insufficient user-plane resources for the PDU session.

Cause \#93 – Onboarding services terminated

This 5GMM cause is sent by the network if the network initiates a de-registration procedure because the onboarding services are terminated.
