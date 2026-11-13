# D.3 UE policy re-assembly at the UE

When the UE needs to apply ANDSP as specified in 3GPP TS 24.502 \[18\], the UE shall consider all UE policy parts with ANDSP contents currently stored at the UE.

When the UE needs to apply URSP as specified in 3GPP TS 24.526 \[19\], the UE shall consider all UE policy parts with URSP contents currently stored at the UE.

a\) if the UE supports VPS URSP then:

1\) the UE shall consider as VPS URSP of the RPLMN all UE policy parts with URSP contents currently stored at the UE, which are a part of one or more UE policy sections identified by a UPSI:

i\) with the PLMN ID part indicating the HPLMN; and

ii\) with UPSC indicated in a tuple of the stored VPS URSP configuration, such that the tuple contains the network descriptor with a network descriptor entry containing:

A\) the network descriptor entry type field set to "one or more VPLMNs" and the network descriptor entry value field containing PLMN ID of the RPLMN of an access, if the UE is registered via one or both accesses and the RPLMN of each access is a VPLMN;

B\) the network descriptor entry type field set to "one or more MCCs" and the network descriptor entry value field containing MCC of the PLMN ID of the RPLMN of an access, if the UE is registered via one or both accesses and the RPLMN of each access is a VPLMN; or

C\) the network descriptor entry type field set to "any VPLMN", if the UE is registered via one or both accesses and the RPLMN of each access is a VPLMN;

2\) the UE shall consider as VPS URSP of the equivalent PLMN of the RPLMN all UE policy parts with URSP contents currently stored at the UE, which are a part of one or more UE policy sections identified by a UPSI:

i\) with the PLMN ID part indicating the HPLMN; and

ii\) with UPSC indicated in a tuple of the stored VPS URSP configuration, such that the tuple contains the network descriptor with a network descriptor entry containing:

A\) the network descriptor entry type field set to "one or more VPLMNs" and the network descriptor entry value field containing PLMN ID of an equivalent PLMN, if the UE is registered via one or both accesses, the RPLMN of each access is a VPLMN and the equivalent PLMN is a VPLMN;

B\) the network descriptor entry type field set to "one or more MCCs" and the network descriptor entry value field containing MCC of the PLMN ID of an equivalent PLMN, if the UE is registered via one or both accesses, the RPLMN of each access is a VPLMN and the equivalent PLMN is a VPLMN; or

C\) the network descriptor entry type field set to "any VPLMN", if the UE is registered via one or both accesses, the RPLMN of each access is a VPLMN and an equivalent PLMN is a VPLMN; and

3\) the UE shall consider as PG URSP all UE policy parts with URSP contents currently stored at the UE except zero or more UE policy parts, if any, which are a part of one or more UE policy sections identified by a UPSI:

i\) with the PLMN ID part indicating the HPLMN; and

ii\) with UPSC indicated in any tuple of the stored VPS URSP configuration; and

b\) the UE shall consider all UE policy parts with URSP contents currently stored at the UE as the signalled URSP.

When the UE needs to apply V2XP as specified in 3GPP TS 24.588 \[19C\], the UE shall consider all UE policy parts with V2XP contents currently stored at the UE.

When the UE needs to apply ProSeP as specified in 3GPP TS 24.555 \[19F\], the UE shall consider all UE policy parts with ProSeP contents currently stored at the UE.

When the UE needs to apply A2XP as specified in 3GPP TS 24.578 \[61\], the UE shall consider all UE policy parts with A2XP contents currently stored at the UE.

When the UE needs to apply RSLPP as specified in 3GPP TS 24.514 \[62\], the UE shall consider all UE policy parts with RSLPP contents currently stored at the UE.
