# P.1 PIN Reference Architecture

Figure P.1-1 shows the logical Personal IoT Network (PIN) reference architecture.

[figure]

Figure P.1-1: PIN reference architecture

A PIN consists of one or more devices providing gateway/routing functionality known as the PEGC to route the traffic towards the 5G network and one or more devices providing PIN management functionality known as the PEMC to manage the PIN; and device(s) enabling communication within the PIN called the PINE. A PINE and PEMC can be a non-3GPP device.

The PIN can also have an AF for PIN (see TS 23.542 \[181\]). The AF for PIN can be deployed by mobile operator or by an authorized third party. When the AF for PIN is deployed by third party, the interworking with 5GC is performed via the NEF.

With PIN-DN communication, the PEMC and PEGC communicates with the AF for PIN at the application layer over the user plane. The PEGC and PEMC can communicate with each other via PIN direct communication using 3GPP access (e.g. PC5) or non-3GPP access (e.g. WiFi, BT) or via PIN indirect communication using a PDU Session in the 5GS.
