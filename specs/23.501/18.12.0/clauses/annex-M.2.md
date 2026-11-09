# M.2 TL-Container Information

Table M.2-1: TL-Container Information

<!-- table -->
|  | TL-Container information | Supported Operations - AN-TL/CN-TL (see NOTE 1) (x2) | Reference |
|  |  | Talker | Listener |  |
| End Station Parameters of AN-TL/CN-TL (x5) |
|  | List of InterfaceID group(s) (x4) |
|  | &gt;Mac Address | Get | Get | IEEE Std 802.1Q [98], Table 46-3 |
|  | &gt;InterfaceName (see NOTE 2) | Get | Get | IEEE Std 802.1Q [98], Table 46-3 |
|  | InterfaceCapabilities (see NOTE 3) (x4) |
|  | &gt;VlanTagCapable (see NOTE 4) | Get | Get | IEEE Std 802.1Q [98], Table 46-11 |
|  | &gt;BufferCapability (see NOTE 5) | Get | - | Annex M.1 |
| TN Stream Parameters (x5) |
|  | TN Stream Identification Information for mask-and-match (see NOTE 7, NOTE 14) (x4) |
|  | &gt;tsnCpeMmIdMsduMaskLength | Set | Set | IEEE Std 802.1CBdb [X], clause 9.1.6.5 |
|  | &gt;tsnCpeMmIdMsduMask | Set | Set | IEEE Std 802.1CBdb [X], clause 9.1.6.6 |
|  | &gt;tsnCpeMmIdMsduMatch | Set | Set | IEEE Std 802.1CBdb [X], clause 9.1.6.7 |
| TN Stream Identification Information for DataFrameSpecification (See NOTE 13, NOTE 14) (x5) |
|  | &gt;DataFrameSpecification | Set | Set | IEEE Std 802.1Q [98], Clause 46.2.3.4 |
| Configuration of End Station Interface (x5) |
|  | &gt;Interface ID group (x4) |
|  | &gt;&gt;InterfaceName (see NOTE 8) | Set | Set | IEEE Std 802.1Q [98],Table 46-3 |
|  | &gt;&gt;Mac Address | Set | Set | IEEE Std 802.1Q [98],Table 46-3 |
| &gt;InterfaceConfiguration (See NOTE 9, NOTE 10, NOTE 12) (x5) |
|  | &gt;&gt;IEEE802-MacAddresses | Set | Set | IEEE Std 802.1Q [98], Clause 46.2.5.3.1 |
|  | &gt;&gt;IEEE802-VlanTag | Set | Set | IEEE Std 802.1Q [98], Clause 46.2.5.3.2 |
|  | &gt;&gt;IPv4-tuple | Set | Set | IEEE Std 802.1Q [98], Clause 46.2.5.3.3 |
|  | &gt;&gt;IPv6-tuple | Set | Set | IEEE Std 802.1Q [98], Clause 46.2.5.3.4 |
|  | &gt;&gt;TimeAwareOffset (see NOTE 12) | Set | - | IEEE Std 802.1Q [98], clause 46.2.5.3.5 |
| &gt;Other parameters to Calculate Gate Control Information (See NOTE 6) (x5) |
|  | &gt;&gt;Interval | Set | - | IEEE Std 802.1Q [98], Table 46-8 |
|  | &gt;&gt;MaxFrameSize (see NOTE 11) | Set | - | IEEE Std 802.1Q [98], Table 46-8 |
| NOTE 1: Get = Get Response; Set = Set Request; - = not supported. NOTE 2: This parameter is optional and only required if End Station has more than one Interface/Port. It identifies the Interface/Port at the End Station. NOTE 3 Interface Capabilities are identical for all Interfaces/Ports of the End Station. NOTE 4: Possible values are TRUE or FALSE. NOTE 5: Maximum possible buffer duration for a packet with the maximum size of an Ethernet packet (1522 Bytes). NOTE 6: SMF/CUC enables the TL to calculate Gate Control Information. Port(s) of the Talker TL may create jitter due to implementation of the TL. How the jitter behaviour is identified and the correction is carried out is up to implementation. NOTE 7: The parameters are provided if mask-and-match stream identification is supported. NOTE 8: The parameter is provided if End Station supports multiple Interfaces/Ports. SMF/CUC guarantees that the End Station MAC address + InterfaceName, which is provided from TN-CNC as InterfaceConfiguration is conveyed with respect to the LLDP information sent via each interface at the user plane. NOTE 9: IEEE802-MacAddresses and IEEE802-VlanTag are provided if Stream Transformation is performed at AN-TL/CN-TL and if Active Destination MAC and VLAN stream identification is signalled from SMF/CUC to TN CNC and if TN CNC provides it in the status group for the Interface/Port. NOTE 10: Vlanid in IEEE802-VlanTag is provided if Stream Transformation is performed at AN-TL/CN-TL and if Active Destination MAC and VLAN stream identification is signalled from SMF/CUC to TN CNC and if TN CNC provides it in the status group for the Interface/Port and End Station VlanTagCapable is TRUE. NOTE 11: Message Length of the Stream including the GTP-U header size. NOTE 12: TimeAwareOffset is provided if TN Stream is scheduled. NOTE 13: The TL indicates a respective FailureCode if it detects a mismatch between the DataFrameSpecification and the GTP-U information received outside of the TL-Container. NOTE 14: Mask-and-match and DataFrameSpecification shall not be supported at the same time. (x5) |
<!-- /table -->

######## Annex N (informative): Support for access to Localized Services
