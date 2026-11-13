# A.2 Cause related to subscription options

Cause \#5 – PEI not accepted

This cause is sent to the UE if the network does not accept an initial registration procedure for emergency services using a PEI.

Cause \#7 – 5GS services not allowed

This 5GMM cause is sent to the UE when it is not allowed to operate 5GS services.

Cause \#11 – PLMN not allowed

This 5GMM cause is sent to the UE if it requests service, or if the network initiates a de-registration request, in a PLMN where the UE, by subscription or due to operator determined barring, is not allowed to operate.

This 5GMM cause can also be sent to the UE when the disaster condition is no longer being applicable in the current location of the UE.

Cause \#12 – Tracking area not allowed

This 5GMM cause is sent to the UE if it requests service, or if the network initiates a de-registration request, in a tracking area where the HPLMN or SNPN determines that the UE, by subscription, is not allowed to operate.

NOTE 1: If 5GMM cause \#12 is sent to a roaming subscriber the subscriber is denied service even if other PLMNs are available on which registration was possible.

Cause \#13 – Roaming not allowed in this tracking area

This 5GMM cause is sent to a UE which requests service, or if the network initiates a de-registration request, in a tracking area of a PLMN or SNPN which by subscription offers roaming to that UE but not in that tracking area.

This 5GMM cause can also be sent to the UE when the disaster condition is no longer being applicable in the current location of the UE.

Cause \#15 – No suitable cells in tracking area

This 5GMM cause is sent to the UE if it requests service, or if the network initiates a de-registration request, in a tracking area where the UE, by subscription, is not allowed to operate, but when it should find another allowed tracking area in the same PLMN or an equivalent PLMN or the same SNPN or an equivalent SNPN.

NOTE 2: Cause \#15 and cause \#12 differ in the fact that cause \#12 does not trigger the UE to search for another allowed tracking area on the same PLMN or SNPN.

Cause \#27 – N1 mode not allowed

This 5GMM cause is sent to the UE if it requests service, or if the network initiates a de-registration request, in a PLMN or SNPN where the UE by subscription or operator policy, is not allowed to operate in N1 mode.

Cause \#31 – Redirection to EPC required

This 5GMM cause is sent to the UE if it requests service in a PLMN where the UE by operator policy, is not allowed in 5GCN and redirection to EPC is required.

Cause \#36 – IAB-node operation not authorized

This 5GMM cause is sent to the UE if a UE operating as an IAB-node requests service, or if the network initiates a de-registration procedure, in a PLMN or SNPN where the UE by subscription is not authorized for IAB operation.

Cause \#72 – Non-3GPP access to 5GCN not allowed

This 5GMM cause is sent to the UE if it requests accessing 5GCN over non-3GPP access in a PLMN or SNPN, where the UE by subscription, is not allowed to access 5GCN over non-3GPP access.

Cause \#74 – Temporarily not authorized for this SNPN

This 5GMM cause is sent to the UE if it requests access, or if the network initiates a de-registration procedure, in a cell belonging to an SNPN for which the UE has no subscription to operate or for which the UE is not allowed to operate onboarding services.

Cause \#75 – Permanently not authorized for this SNPN

This 5GMM cause is sent to the UE if it requests access, or if the network initiates a de-registration procedure, in a cell belonging to an SNPN with a globally-unique SNPN identity for which the UE either has no subscription to operate, the UE's subscription has expired or the UE is not allowed to operate onboarding services.

Cause \#76 – Not authorized for this CAG or authorized for CAG cells only

This 5GMM cause is sent to the UE if the UE requests access or de-registration:

i\) in a CAG cell with a CAG-ID which is not authorized based on the UE's "allowed CAG list" for the PLMN; or

ii\) in a non-CAG cell, wherein the UE is only allowed to access 5GS via CAG cells

Cause \#77 – Wireline access area not allowed

This 5GMM cause is sent to the 5G-RG or the W-AGF acting on behalf of the FN-CRG (or on behalf of the N5GC device) if the 5G-RG or the W-AGF acting on behalf of the FN-CRG (or on behalf of the N5GC device) request accessing 5GCN over a wireline access network belonging to a wireline access area, where the 5G-RG or the W-AGF acting on behalf of the FN-CRG (or on behalf of the N5GC device) are not allowed by subscription to access the 5GCN over the wireline access.

Cause \#79 – UAS services not allowed

This 5GMM cause is sent to the UE to indicate that the request of UAS services is not allowed.

Cause \#80 – Disaster roaming for the determined PLMN with disaster condition not allowed

This 5GMM cause is sent by the network in a PLMN where the UE has requested registration for disaster roaming service for the determined PLMN with disaster condition, but the AMF determines that it does not support providing disaster roaming services to the UE for the determined PLMN with disaster condition as roaming agreement for disaster roaming services with HPLMN of the UE does not exist, or the determined PLMN with disaster condition is a forbidden PLMN of the UE.

Cause \#94 – User plane positioning not authorized

This 5GMM cause is sent to the UE if it requests the user plane positioning, where the UE by subscription is not authorized for user plane positioning.
