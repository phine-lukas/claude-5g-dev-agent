# F.3 BMCA procedure

[figure]

Figure F.3-1: BMCA procedure

1\. PDU Session Establishment is performed as shown in F.1-1 step 1 and 2 for an Ethernet or IP type PDU Session to carry the UMIC or PMIC.

2\. The TSN AF or TSCTSF may subscribe to notifications for the PTP port state changes from UPF/NW-TT.

3\. The UPF/NW-TT receives the Announce message via User -plane from DS-TT connectivity established using PDU session, or via NW-TT port over N6.

As Announce message is a periodic message, after step 3, the UPF/NW-TT will receive Announce messages regularly.

4\. The NW-TT runs the BMCA algorithm in order to determine the PTP port state for the DS-TT port(s) and NW-TT port(s).

BMCA will be triggered after receiving the Announce message.

5\. If the BMCA procedure in NW-TT determines to use Announce message from the external grandmaster PTP instance, the UPF/NW-TT regenerates the Announce message based on the received Announce message for each Leader PTP port on the NW-TT and DS-TT(s) port for this PTP domain. The NW-TT/UPF forwards the regenerated Announce messages to the PDU session(s) related to the Leader PTP ports on the DS-TT(s).

NOTE: Leader and Follower terms in this specification are aligned with NOTE 2 in clause 5.27.1.2.2.1 of TS 23.501 \[2\]..

6\. If the TSN AF or TSCTSF has subscribed for notifications for the PTP port state changes, the UPF/NW-TT reports any changes to the PTP port states to the TSN AF or TSCTSF via UMIC (for DS-TT ports) or PMIC (for NW-TT ports).

7\. Based on the notification for the PTP port state changes, the TSN AF or TSCTSF may request appropriate QoS treatment and PDU Session modification may then be triggered to modify the QoS Flow carrying the gPTP messages over user plane in order to be compliant with the IEEE Std 802.1AS \[75\] delay recommendation for carrying gPTP messages as in clause 5.27.1.6 of TS 23.501 \[2\].
