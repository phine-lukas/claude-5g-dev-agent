# K.1 Standardized port and user plane node management information

Table K.1-1 and Table K.1-2 list standardized port management information and user plane node management information, respectively.

Table K.1-1: Standardized port management information

<!-- table -->
| Port management information | Applicability (see NOTE 6) (x2) | Supported operations by TSN AF | Supported operations by TSCTSF | Reference |
|  | DS-TT | NW-TT | (see NOTE 1) | (see NOTE 1) |  |
| General |  |  |  |  |  |
| Port management capabilities (see NOTE 2) | X | X | R | R |  |
| Bridge delay related information |  |  |  |  |  |
| txPropagationDelay | X | X | R | - | IEEE Std 802.1Q [98] clause 12.32.2.1 |
| txPropagationDelayDeltaThreshold (see NOTE 23) | X | X | RW |  |  |
| Traffic class related information |  |  |  |  |  |
| Traffic class table | X | X | RW | - | IEEE Std 802.1Q [98] clause 12.6.3 and clause 8.6.6. |
| Gate control information |  |  |  |  |  |
| queueMaxSDUTable |  |  |  |  | IEEE Std 802.1Q [98], clause 12.29.1 |
| &gt; queueMaxSDU | X | X | RW |  | IEEE Std 802.1Q [98], clause 12.29.1 |
| &gt; TransmissionOverrun (see NOTE 3) | X | X | R |  | IEEE Std 802.1Q [98], clause 12.29.1 |
| GateEnabled | X | X | RW | - | IEEE Std 802.1Q [98] Table 12-32 |
| AdminGateStates | X | X | RW |  | IEEE Std 802.1Q [98] Table 12-32 |
| AdminBaseTime | X | X | RW | - | IEEE Std 802.1Q [98] Table 12-32 |
| AdminControlList | X | X | RW | - | IEEE Std 802.1Q [98] Table 12-32 |
| AdminCycleTime (see NOTE 3) | X | X | RW | - | IEEE Std 802.1Q [98] Table 12-32 |
| AdminControlListLength (see NOTE 3) | X | X | RW | - | IEEE Std 802.1Q [98] Table 12-32 |
| AdminCycleTimeExtension | X | X | RW | - | IEEE Std 802.1Q [98] Table 12-32 |
| Tick granularity | X | X | R | - | IEEE Std 802.1Q [98] Table 12-32 |
| SupportedListMax | X | X | R | - | IEEE Std 802.1Q [98] Table 12-32 |
| General Neighbor discovery configuration (NOTE 4) |  |  |  |  |  |
| adminStatus | D | X | RW | - | IEEE Std 802.1AB [97] clause 9.2.5.1 |
| lldpV2LocChassisIdSubtype | D | X | RW | - | IEEE Std 802.1AB [97] Table 11-2 |
| lldpV2LocChassisId | D | X | RW | - | IEEE Std 802.1AB [97] Table 11-2 |
| lldpV2MessageTxInterval | D | X | RW | - | IEEE Std 802.1AB [97] Table 11-2 |
| lldpV2MessageTxHoldMultiplier | D | X | RW | - | IEEE Std 802.1AB [97] Table 11-2 |
| NW-TT port neighbor discovery configuration |  |  |  |  |  |
| lldpV2LocPortIdSubtype |  | X | RW | - | IEEE Std 802.1AB [97] Table 11-2 |
| lldpV2LocPortId |  | X | RW | - | IEEE Std 802.1AB [97] Table 11-2 |
| OtlvSet |  | X | RW | - | IEC/IEEE 60802 [195], clause 6.5.2.4.5 and clause 6.5.2.4.6. |
| DS-TT port neighbor discovery configuration |  |  |  |  |  |
| lldpV2LocPortIdSubtype | D |  | RW | - | IEEE Std 802.1AB [97] Table 11-2 |
| lldpV2LocPortId | D |  | RW | - | IEEE Std 802.1AB [97] Table 11-2 |
| OtlvSet | D |  | RW | - | IEC/IEEE 60802 [195], clause 6.5.2.4.5 and clause 6.5.2.4.6. |
| Neighbor discovery information for each discovered neighbor of NW-TT (NOTE 26) |  |  |  |  |  |
| lldpV2RemChassisIdSubtype |  | X | R | - | IEEE Std 802.1AB [97] Table 11-2 |
| lldpV2RemChassisId |  | X | R | - | IEEE Std 802.1AB [97] Table 11-2 |
| lldpV2RemPortIdSubtype |  | X | R | - | IEEE Std 802.1AB [97] Table 11-2 |
| lldpV2RemPortId |  | X | R | - | IEEE Std 802.1AB [97] Table 11-2 |
| TTL |  | X | R | - | IEEE Std 802.1AB [97] clause 8.5.4 |
| OtlvSet |  | X | R | - | IEC/IEEE 60802 [195], clause 6.5.2.4.5 and clause 6.5.2.4.6. |
| Neighbor discovery information for each discovered neighbor of DS-TT (NOTE 5) |  |  |  |  |  |
| lldpV2RemChassisIdSubtype | D |  | R | - | IEEE Std 802.1AB [97] Table 11-2 |
| lldpV2RemChassisId | D |  | R | - | IEEE Std 802.1AB [97] Table 11-2 |
| lldpV2RemPortIdSubtype | D |  | R | - | IEEE Std 802.1AB [97] Table 11-2 |
| lldpV2RemPortId | D |  | R | - | IEEE Std 802.1AB [97] Table 11-2 |
| TTL | D |  | R | - | IEEE Std 802.1AB [97] clause 8.5.4.1 |
| OtlvSet | D |  | R | - | IEC/IEEE 60802 [195], clause 6.5.2.4.5 and clause 6.5.2.4.6. |
| Information for deterministic networking for each NW-TT port (NOTE 27) |  |  |  |  |  |
| Interface information |  |  |  |  |  |
| Interface type |  | X |  | R | IETF RFC 8343 [151] |
| Interface enabled status |  | X |  | R | IETF RFC 8343 [151] |
| phys-address |  | X |  | R | IETF RFC 8343 [151] |
| IPv4 information |  |  |  |  |  |
| IPv4 enabled status |  | X |  | R | IETF RFC 8344 [152] |
| IPv4 forwarding status |  | X |  | R | IETF RFC 8344 [152] |
| IPv4 MTU |  | X |  | R | IETF RFC 8344 [152] |
| Information for each IPv4 address |  |  |  |  |  |
| IPv4 address |  | X |  | R | IETF RFC 8344 [152] |
| prefix-length |  | X |  | R | IETF RFC 8344 [152] |
| netmask |  | X |  | R | IETF RFC 8344 [152] |
| origin |  | X |  | R | IETF RFC 8344 [152] |
| Information for each IPv4 neighbor |  |  |  |  |  |
| IPv4 address |  | X |  | R | IETF RFC 8344 [152] |
| link-layer-address |  | X |  | R | IETF RFC 8344 [152] |
| origin |  | X |  | R | IETF RFC 8344 [152] |
| IPv6 information |  |  |  |  |  |
| IPv6 enabled status |  | X |  | R | IETF RFC 8344 [152] |
| IPv6 forwarding status |  | X |  | R | IETF RFC 8344 [152] |
| IPv6 MTU |  | X |  | R | IETF RFC 8344 [152] |
| Information for each IPv6 address |  |  |  |  |  |
| IPv6 address |  | X |  | R | IETF RFC 8344 [152] |
| prefix-length |  | X |  | R | IETF RFC 8344 [152] |
| origin |  | X |  | R | IETF RFC 8344 [152] |
| status |  | X |  | R | IETF RFC 8344 [152] |
| Information for each IPv6 neighbor |  |  |  |  |  |
| IPv6 address |  | X |  | R | IETF RFC 8344 [152] |
| link-layer-address |  | X |  | R | IETF RFC 8344 [152] |
| origin |  | X |  | R | IETF RFC 8344 [152] |
| is-router |  | X |  | R | IETF RFC 8344 [152] |
| state |  | X |  | R | IETF RFC 8344 [152] |
| Stream Parameters (NOTE 11) |  |  |  |  |  |
| MaxStreamFilterInstances | X |  | R | - | IEEE Std 802.1Q [98] clause 12.31.1.1 |
| MaxStreamGateInstances | X |  | R | - | IEEE Std 802.1Q [98] clause 12.31.1.2 |
| MaxFlowMeterInstances | X |  | R | - | IEEE Std 802.1Q [98] clause 12.31.1.3 |
| SupportedListMax | X |  | R | - | IEEE Std 802.1Q [98] clause 12.31.1.4 |
| Per-Stream Filtering and Policing information (NOTE 10) |  |  |  |  |  |
| Stream Filter Instance Table (NOTE 8) |  |  |  | - | IEEE Std 802.1Q [98] Table 12-35 |
| &gt; StreamFilterInstanceIndex | X | X | RW | - | IEEE Std 802.1Q [98] Table 12-35 |
| &gt; Stream Identification type | X | X | RW | - | IEEE 802.1CB [83] clause 9.1.1.6 |
| &gt; Stream Identification Controlling Parameters | X | X | RW | - | IEEE 802.1CB [83] clauses 9.1.2, 9.1.3, 9.1.4 (NOTE 12) |
| &gt; PrioritySpec | X | X | RW | - | IEEE Std 802.1Q [98] Table 12-35 |
| &gt; StreamGateInstanceID | X | X | RW | - | IEEE Std 802.1Q [98] Table 12-35 |
| Stream Gate Instance Table (NOTE 9) |  |  |  |  | IEEE Std 802.1Q [98] Table 12-33 |
| StreamGateInstanceIndex | X | X | RW | - | IEEE Std 802.1Q [98] Table 12-36 |
| StreamGateAdminBaseTime | X | X | RW | - | IEEE Std 802.1Q [98] Table 12-36 |
| StreamGateAdminControlList | X | X | RW | - | IEEE Std 802.1Q [98] Table 12-36 |
| StreamGateAdminCycleTime | X | X | RW | - | IEEE Std 802.1Q [98] Table 12-36 |
| StreamGateTickGranularity | X | X | R | - | IEEE Std 802.1Q [98] Table 12-36 |
| StreamGateAdminCycleTimeExtension | X | X | R | - | IEEE Std 802.1Q [98] Table 12-36 |
| Time Synchronization Information |  |  |  |  |  |
| TSN Time domain number (NOTE 24) | X | X | RW |  |  |
| Supported PTP instance types (NOTE 13) | X |  | R | R | IEEE Std 1588 [126] clause 8.2.1.5.5 |
| Supported transport types (NOTE 14) | X |  | R | R |  |
| Supported delay mechanisms (NOTE 15) | X |  | R | R | IEEE Std 1588 [126] clause 8.2.15.4.4 |
| PTP grandmaster capable (NOTE 16) | X |  | R | R |  |
| gPTP grandmaster capable (NOTE 17) | X |  | R | R |  |
| Supported PTP profiles (NOTE 18) | X |  | R | R |  |
| Number of supported PTP instances | X |  | R | R |  |
| PTP instance specification |  |  |  |  |  |
| PTP Instance ID (NOTE 25) | X | X | RW | RW |  |
| &gt; PTP profile (NOTE 19) | X |  | RW | RW |  |
| &gt; Transport type (NOTE 20) | X |  | RW | RW |  |
| &gt; Grandmaster enabled (NOTE 21) | X |  | RW | RW |  |
| IEEE Std 1588 [126] data sets (NOTE 22) |  |  |  |  |  |
| &gt; defaultDS.clockIdentity | X |  | RW | RW | IEEE Std 1588 [126] clause 8.2.1.2.2 |
| &gt; defaultDS.clockQuality.clockClass | X |  | RW | RW | IEEE Std 1588 [126] clause 8.2.1.3.1.2 |
| &gt; defaultDS.clockQuality.clockAccuracy | X |  | RW | RW | IEEE Std 1588 [126] clause 8.2.1.3.1.3 |
| &gt; defaultDS.clockQuality.offsetScaledLogVariance | X |  | RW | RW | IEEE Std 1588 [126] clause 8.2.1.3.1.4 |
| &gt; defaultDS.priority1 | X |  | RW | RW | IEEE Std 1588 [126] clause 8.2.1.4.1 |
| &gt; defaultDS.priority2 | X |  | RW | RW | IEEE Std 1588 [126] clause 8.2.1.4.2 |
| &gt; defaultDS.domainNumber | X |  | RW | RW | IEEE Std 1588 [126] clause 8.2.1.4.3 |
| &gt; defaultDS.sdoId | X |  | RW | RW | IEEE Std 1588 [126] clause 8.2.1.4.5 |
| &gt; defaultDS.instanceEnable | X |  | RW | RW | IEEE Std 1588 [126] clause 8.2.1.5.2 |
| &gt; defaultDS.instanceType | X |  | RW | RW | IEEE Std 1588 [126] clause 8.2.1.5.5 |
| &gt; portDS.portIdentity | X | X | RW | RW | IEEE Std 1588 [126] clause 8.2.15.2.1 |
| &gt; portDS.portState | X | X | R | R | IEEE Std 1588 [126] clause 8.2.15.3.1 |
| &gt; portDS.logMinDelayReqInterval | X | X | RW | RW | IEEE Std 1588 [126] clause 8.2.15.3.2 |
| &gt; portDS.logAnnounceInterval | X | X | RW | RW | IEEE Std 1588 [126] clause 8.2.15.4.1 |
| &gt; portDS.announceReceiptTimeout |  | X | RW | RW | IEEE Std 1588 [126] clause 8.2.15.4.2 |
| &gt; portDS.logSyncInterval | X | X | RW | RW | IEEE Std 1588 [126] clause 8.2.15.4.3 |
| &gt; portDS.delayMechanism | X | X | RW | RW | IEEE Std 1588 [126] clause 8.2.15.4.4 |
| &gt; portDS.logMinPdelayReqInterval | X | X | RW | RW | IEEE Std 1588 [126] clause 8.2.15.4.5 |
| &gt; portDS.versionNumber | X | X | RW | RW | IEEE Std 1588 [126] clause 8.2.15.4.6 |
| &gt; portDS.minorVersionNumber | X | X | RW | RW | IEEE Std 1588 [126] clause 8.2.15.4.7 |
| &gt; portDS.delayAsymmetry | X | X | RW | RW | IEEE Std 1588 [126] clause 8.2.15.4.8 |
| &gt; portDS.portEnable | X | X | RW | RW | IEEE Std 1588 [126] clause 8.2.15.5.1 |
| &gt; timePropertiesDS.currentUtcOffset | X |  | RW | RW | IEEE Std 1588 [126] clause 8.2.4.2 |
| &gt; timePropertiesDS.timeSource | X |  | RW | RW | IEEE Std 1588 [126] clause 8.2.4.9 |
| &gt; externalPortConfigurationPortDS.desiredState |  |  | RW | RW | IEEE Std 1588 [126] clause 15.5.3.7.15.1 |
| IEEE Std 802.1AS [104] data sets (NOTE 22) |  |  |  |  |  |
| &gt; defaultDS.clockIdentity | X |  | RW | RW | IEEE Std 802.1AS [104] clause 14.2.2 |
| &gt; defaultDS.clockQuality.clockClass | X |  | RW | RW | IEEE Std 802.1AS [104] clause 14.2.4.2 |
| &gt; defaultDS.clockQuality.clockAccuracy | X |  | RW | RW | IEEE Std 802.1AS [104] clause 14.2.4.3 |
| &gt; defaultDS.clockQuality.offsetScaledLogVariance | X |  | RW | RW | IEEE Std 802.1AS [104] clause 14.2.4.4 |
| &gt; defaultDS.priority1 | X |  | RW | RW | IEEE Std 802.1AS [104] clause 14.2.5 |
| &gt; defaultDS.priority2 | X |  | RW | RW | IEEE Std 802.1AS [104] clause 14.2.6 |
| &gt; defaultDS.timeSource | X |  | RW | RW | IEEE Std 802.1AS [104] clause 14.2.15 |
| &gt; defaultDS.domainNumber | X |  | RW | RW | IEEE Std 802.1AS [104] clause 14.2.16 |
| &gt; defaultDS.sdoId | X |  | RW | RW | IEEE Std 802.1AS [104] clause 14.2.4.3 |
| &gt; defaultDS.instanceEnable | X |  | RW | RW | IEEE Std 802.1AS [104] clause 14.2.19 |
| &gt; portDS.portIdentity |  | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.2 |
| &gt; portDS.portState |  | X | R | R | IEEE Std 802.1AS [104] clause 14.8.3 |
| &gt; portDS.ptpPortEnabled | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.4 |
| &gt; portDS.delayMechanism | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.5 |
| &gt; portDS.isMeasuringDelay | X | X | R | R | IEEE Std 802.1AS [104] clause 14.8.6 |
| &gt; portDS.asCapable | X | X | R | R | IEEE Std 802.1AS [104] clause 14.8.7 |
| &gt; portDS.meanLinkDelay | X | X | R | R | IEEE Std 802.1AS [104] clause 14.8.8 |
| &gt; portDS.meanLinkDelayThresh | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.9 |
| &gt; portDS.delayAsymmetry | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.10 |
| &gt; portDS.neighborRateRatio | X | X | R | R | IEEE Std 802.1AS [104] clause 14.8.11 |
| &gt; portDS.initialLogAnnounceInterval | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.12 |
| &gt; portDS.currentLogAnnounceInterval | X | X | R | R | IEEE Std 802.1AS [104] clause 14.8.13 |
| &gt; portDS.useMgtSettableLogAnnounceInterval | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.14 |
| &gt; portDS.mgtSettableLogAnnounceInterval | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.15 |
| &gt; portDS.announceReceiptTimeout |  | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.16 |
| &gt; portDS.initialLogSyncInterval | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.17 |
| &gt; portDS.currentLogSyncInterval | X | X | R | R | IEEE Std 802.1AS [104] clause 14.8.18 |
| &gt; portDS.useMgtSettableLogSyncInterval | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.19 |
| &gt; portDS.mgtSettableLogSyncInterval | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.20 |
| &gt; portDS.syncReceiptTimeout |  | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.21 |
| &gt; portDS.syncReceiptTimeoutTimeInterval |  | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.22 |
| &gt; portDS.initialLogPdelayReqInterval | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.23 |
| &gt; portDS.currentLogPdelayReqInterval | X | X | R | R | IEEE Std 802.1AS [104] clause 14.8.24 |
| &gt; portDS.useMgtSettableLogPdelayReqInterval | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.25 |
| &gt; portDS.mgtSettableLogPdelayReqInterval | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.26 |
| &gt; portDS.initialLogGptpCapableMessageInterval | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.27 |
| &gt; portDS.currentLogGptpCapableMessageInterval | X | X | R | R | IEEE Std 802.1AS [104] clause 14.8.28 |
| &gt; portDS.useMgtSettableLogGptpCapableMessageInterval | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.29 |
| &gt; portDS.mgtSettableLogGptpCapableMessageInterval | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.30 |
| &gt; portDS.initialComputeNeighborRateRatio | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.31 |
| &gt; portDS.currentComputeNeighborRateRatio | X | X | R | R | IEEE Std 802.1AS [104] clause 14.8.32 |
| &gt; portDS.useMgtSettableComputeNeighborRateRatio | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.33 |
| &gt; portDS.mgtSettableComputeNeighborRateRatio | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.34 |
| &gt; portDS.initialComputeMeanLinkDelay | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.35 |
| &gt; portDS.currentComputeMeanLinkDelay | X | X | R | R | IEEE Std 802.1AS [104] clause 14.8.36 |
| &gt; portDS.useMgtSettableComputeMeanLinkDelay | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.37 |
| &gt; portDS.mgtSettableComputeMeanLinkDelay | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.38 |
| &gt; portDS.allowedLostResponses | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.39 |
| &gt; portDS.allowedFaults | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.40 |
| &gt; portDS.gPtpCapableReceiptTimeout | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.41 |
| &gt; portDS.versionNumber | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.42 |
| &gt; portDS.nup | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.43 |
| &gt; portDS.ndown | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.44 |
| &gt; portDS.oneStepTxOper | X | X | R | R | IEEE Std 802.1AS [104] clause 14.8.45 |
| &gt; portDS.oneStepReceive | X | X | R | R | IEEE Std 802.1AS [104] clause 14.8.46 |
| &gt; portDS.oneStepTransmit | X | X | R | R | IEEE Std 802.1AS [104] clause 14.8.47 |
| &gt; portDS.initialOneStepTxOper | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.48 |
| &gt; portDS.currentOneStepTxOper | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.49 |
| &gt; portDS.useMgtSettableOneStepTxOper | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.50 |
| &gt; portDS.mgtSettableOneStepTxOper | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.51 |
| &gt; portDS.syncLocked | X | X | R | R | IEEE Std 802.1AS [104] clause 14.8.52 |
| &gt; portDS.pdelayTruncatedTimestampsArray | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.53 |
| &gt; portDS.minorVersionNumber | X | X | RW | RW | IEEE Std 802.1AS [104] clause 14.8.54 |
| &gt; timePropertiesDS.currentUtcOffset | X |  | RW | RW | IEEE Std 802.1AS [104] clause 14.5.2 |
| &gt; externalPortConfigurationPortDS.desiredState |  | X | RW | RW | IEEE Std 802.1AS [104] clause 14.12.2 |
| NOTE 1: R = Read only access; RW = Read/Write access; ― = not supported. NOTE 2: Indicates which standardized and deployment-specific port management information is supported by DS-TT or NW-TT. NOTE 3: AdminCycleTime, AdminControlListLength and TransmissionOverrun are optional for gate control information. NOTE 4: If DS-TT supports neighbor discovery, then TSN AF sends the general neighbor discovery configuration for DS-TT Ethernet ports to DS-TT. If DS-TT does not support neighbor discovery, then TSN AF sends the general neighbor discovery configuration for DS-TT Ethernet ports to NW-TT using the User Plane Node Management Information Container (refer to Table K.1-2) and NW-TT performs neighbor discovery on behalf on DS-TT. When a parameter in this group is changed, it is necessary to provide the change to every DS-TT and the NW-TT that belongs to the 5GS TSN bridge. It is mandatory that the general neighbor discovery configuration is identical for all DS-TTs and the NW-TTs that belongs to the bridge. NOTE 5: If DS-TT supports neighbor discovery, then TSN AF retrieves neighbor discovery information for DS-TT Ethernet ports from DS-TT. TSN AF indicates the neighbor discovery information for each discovered neighbor of DS-TT port to CNC. If DS-TT does not support neighbor discovery, then TSN AF retrieves neighbor discovery information for DS-TT Ethernet ports from NW-TT, using the User Plane Node Management Information Container (refer to Table K.1-2), the NW-TT performing neighbor discovery on behalf on DS-TT. NOTE 6: X = applicable; D = applicable when validation and generation of LLDP frames is processed at the DS-TT. NOTE 7: Void. NOTE 8: There is a Stream Filter Instance Table per Stream. NOTE 9: There is a Stream Gate Instance Table per Gate. NOTE 10: TSN AF indicates the support for PSFP to the CNC only if each DS-TT and NW-TT of the 5GS bridge has indicated support of PSFP. DS-TT indicates support of PSFP using port management capabilities, i.e. by indicating support for the Per-Stream Filtering and Policing information and by setting higher than zero values for MaxStreamFilterInstances, MaxStreamGateInstances, MaxFlowMeterInstances, SupportedListMax parameters. When available, TSN AF uses the PSFP information for determination of the traffic pattern information as described in Annex I. The PSFP information can be used at the DS-TT (if supported) and at the NW-TT (if supported) for the purpose of per-stream filtering and policing as defined in clause 8.6.5.2.1 of IEEE Std 802.1Q [98]. NOTE 11: TSN AF composes a Stream Parameter Table towards the CNC. It is up to TSN AF how it composes the Stream Parameter Table based on the numerical values as received from DS-TT and NW-TT port(s) and for the bridge for each individual parameter. NOTE 12: The set of Stream Identification Controlling Parameters depends on the Stream Identification type value as defined in IEEE Std 802.1CB [83] Table 9-1 and clauses 9.1.2, 9.1.3, 9.1.4. NOTE 13: Enumeration of supported PTP instance types. Allowed values as defined in clause 8.2.1.5.5 of IEEE Std 1588 [126]. NOTE 14: Enumeration of supported transport types. Allowed values: IPv4 (as defined in Annex C of IEEE Std 1588 [126]), IPv6 (as defined in IEEE Std 1588 [126] Annex D), Ethernet (as defined in Annex E of IEEE Std 1588 [126]). NOTE 15: Enumeration of supported PTP delay mechanisms. Allowed values as defined in clause 8.2.15.4.4 of IEEE Std 1588 [126]. NOTE 16: Indicates whether DS-TT supports acting as a PTP grandmaster. NOTE 17: Indicates whether DS-TT supports acting as a gPTP grandmaster. NOTE 18: Enumeration of supported PTP profiles, each identified by PTP profile ID, as defined in clause 20.3.3 of IEEE Std 1588 [126]. NOTE 19: PTP profile to apply, identified by PTP profile ID, as defined in clause 20.3.3 of IEEE Std 1588 [126]. NOTE 20: Transport type to use. Allowed values: IPv4 (as defined in Annex C of IEEE Std 1588 [126]), IPv6 (as defined in IEEE Std 1588 [126] Annex D), Ethernet (as defined in Annex E of IEEE Std 1588 [126]). NOTE 21: Indicates whether to act as grandmaster or not, i.e. whether to send Announce, Sync and optionally Follow_Up messages. NOTE 22: The IEEE Std 802.1AS [104] data sets apply if the IEEE 802.1AS PTP profile is used; otherwise the IEEE Std 1588 [126] data sets apply. NOTE 23: Indicates how much the txPropagationDelay needs to change so that DS-TT/NW-TT report a change in txPropagationDelay to TSN AF. This is optional for NW-TT. NOTE 24: Indicates the gPTP domain (identified by a domain number) that is assumed by the CNC as the reference clock for time information in the scheduled traffic (gate control) information, PSFP information and bridge delay related information. This is optional for NW-TT. NOTE 25: PTP Instance ID uniquely identifies a PTP instance within the user plane node. NOTE 26: TSN AF indicates the neighbor discovery information for each discovered neighbor of NW-TT port to CNC. NOTE 27: Applicable in case of interworking with IETF Deterministic Networking. (x6) |
<!-- /table -->

Table K.1-2: Standardized user plane node management information

<!-- table -->
| User plane node management information | Supported operations by TSN AF | Supported operations by TSCTSF | Reference |
|  | (see NOTE 1) | (see NOTE 1) |  |
| Information for 5GS Bridge/Router |  |  |  |
| User plane node Address | R | R |  |
| User plane node ID | R | R |  |
| NW-TT port numbers | R | R |  |
| Traffic forwarding information |  |  |  |
| Static Filtering Entry (NOTE 3) | RW | - | IEEE Std 802.1Q [98] clause 8.8.1 |
| General Neighbor discovery configuration (NOTE 2) |  |  |  |
| adminStatus | RW | - | IEEE Std 802.1AB [97] clause 9.2.5.1 |
| lldpV2LocChassisIdSubtype | RW | - | IEEE Std 802.1AB [97] Table 11-2 |
| lldpV2LocChassisId | RW | - | IEEE Std 802.1AB [97] Table 11-2 |
| lldpV2MessageTxInterval | RW | - | IEEE Std 802.1AB [97] Table 11-2 |
| lldpV2MessageTxHoldMultiplier | RW | - | IEEE Std 802.1AB [97] Table 11-2 |
| DS-TT port neighbor discovery configuration for DS-TT ports (NOTE 4) |  |  |  |
| &gt;DS-TT port neighbor discovery configuration for each DS-TT port |  |  |  |
| &gt;&gt; DS-TT port number | RW | - |  |
| &gt;&gt; lldpV2LocPortIdSubtype | RW | - | IEEE Std 802.1AB [97] Table 11-2 |
| &gt;&gt; lldpV2LocPortId | RW | - | IEEE Std 802.1AB [97] Table 11-2 |
| &gt;&gt; OtlvSet | RW | - | IEC/IEEE 60802 [195], clause 6.5.2.4.5 and clause 6.5.2.4.6. |
| Discovered neighbor information for DS-TT ports (NOTE 4) |  |  |  |
| &gt;Discovered neighbor information for each DS-TT port (NOTE 4) |  |  |  |
| &gt;&gt; DS-TT port number | R | - |  |
| &gt;&gt; lldpV2RemChassisIdSubtype | R | - | IEEE Std 802.1AB [97] Table 11-2 |
| &gt;&gt; lldpV2RemChassisId | R | - | IEEE Std 802.1AB [97] Table 11-2 |
| &gt;&gt; lldpV2RemPortIdSubtype | R | - | IEEE Std 802.1AB [97] Table 11-2 |
| &gt;&gt; lldpV2RemPortId | R | - | IEEE Std 802.1AB [97] Table 11-2 |
| &gt;&gt; TTL | R | - | IEEE Std 802.1AB [97] clause 8.5.4.1 |
| &gt;&gt; OtlvSet | R | - | IEC/IEEE 60802 [195], clause 6.5.2.4.5 and clause 6.5.2.4.6. |
| Stream Parameters (NOTE 5) |  |  |  |
| MaxStreamFilterInstances | R | - | IEEE Std 802.1Q [98] Table 12-34 |
| MaxStreamGateInstances | R | - | IEEE Std 802.1Q [98] Table 12-34 |
| MaxFlowMeterInstances | R | - | IEEE Std 802.1Q [98] Table 12-34 |
| SupportedListMax | R | - | IEEE Std 802.1Q [98] Table 12-34 |
| Time synchronization information |  |  |  |
| Supported PTP instance types (NOTE 6) | R | R |  |
| Supported transport types (NOTE 7) | R | R |  |
| Supported delay mechanisms (NOTE 8) | R | R |  |
| PTP grandmaster capable (NOTE 9) | R | R |  |
| gPTP grandmaster capable (NOTE 10) | R | R |  |
| Supported PTP profiles (NOTE 11) | R | R |  |
| Number of supported PTP instances | R | R |  |
| Time synchronization information for PTP instances (NOTE 16) |  |  |  |
| &gt; PTP instance specification |  |  |  |
| &gt;&gt; PTP Instance ID (NOTE 17) | RW | RW |  |
| &gt;&gt; PTP profile (NOTE 12) | RW | RW |  |
| &gt;&gt; Transport type (NOTE 13) | RW | RW |  |
| &gt;&gt; Grandmaster candidate enabled | RW | RW |  |
| IEEE Std 1588 [126] data sets (NOTE 15) |  |  |  |
| &gt;&gt; defaultDS.clockIdentity | RW | RW | IEEE Std 1588 [126] clause 8.2.1.2.2 |
| &gt;&gt; defaultDS.clockQuality.clockClass | RW | RW | IEEE Std 1588 [126] clause 8.2.1.3.1.2 |
| &gt;&gt; defaultDS.clockQuality.clockAccuracy | RW | RW | IEEE Std 1588 [126] clause 8.2.1.3.1.3 |
| &gt;&gt; defaultDS.clockQuality.offsetScaledLogVariance | RW | RW | IEEE Std 1588 [126] clause 8.2.1.3.1.4 |
| &gt;&gt; defaultDS.priority1 | RW | RW | IEEE Std 1588 [126] clause 8.2.1.4.1 |
| &gt;&gt; defaultDS.priority2 | RW | RW | IEEE Std 1588 [126] clause 8.2.1.4.2 |
| &gt;&gt; defaultDS.domainNumber | RW | RW | IEEE Std 1588 [126] clause 8.2.1.4.3 |
| &gt;&gt; defaultDS.sdoId | RW | RW | IEEE Std 1588 [126] clause 8.2.1.4.5 |
| &gt;&gt; defaultDS.instanceEnable | RW | RW | IEEE Std 1588 [126] clause 8.2.1.5.2 |
| &gt;&gt; defaultDS.externalPortConfigurationEnabled | RW | RW | IEEE Std 1588 [126] clause 8.2.1.5.3 |
| &gt;&gt; defaultDS.instanceType | RW | RW | IEEE Std 1588 [126] clause 8.2.1.5.5 |
| &gt;&gt; timePropertiesDS.currentUtcOffset | RW | RW | IEEE Std 1588 [126] clause 8.2.4.2 |
| &gt;&gt; timePropertiesDS.timeSource | RW | RW | IEEE Std 1588 [126] clause 8.2.4.9 |
| IEEE Std 802.1AS [104] data sets (NOTE 15) |  |  |  |
| &gt;&gt; defaultDS.clockIdentity | RW | RW | IEEE Std 802.1AS [104] clause 14.2.2 |
| &gt;&gt; defaultDS.clockQuality.clockClass | RW | RW | IEEE Std 802.1AS [104] clause 14.2.4.2 |
| &gt;&gt; defaultDS.clockQuality.clockAccuracy | RW | RW | IEEE Std 802.1AS [104] clause 14.2.4.3 |
| &gt;&gt; defaultDS.clockQuality.offsetScaledLogVariance | RW | RW | IEEE Std 802.1AS [104] clause 14.2.4.4 |
| &gt;&gt; defaultDS.priority1 | RW | RW | IEEE Std 802.1AS [104] clause 14.2.5 |
| &gt;&gt; defaultDS.priority2 | RW | RW | IEEE Std 802.1AS [104] clause 14.2.6 |
| &gt;&gt; defaultDS.timeSource | RW | RW | IEEE Std 802.1AS [104] clause 14.2.15 |
| &gt;&gt; defaultDS.domainNumber | RW | RW | IEEE Std 802.1AS [104] clause 14.2.16 |
| &gt;&gt; defaultDS.sdoId | RW | RW | IEEE Std 802.1AS [104] clause 14.2.18 |
| &gt;&gt; defaultDS.externalPortConfigurationEnabled | RW | RW | IEEE Std 802.1AS [104] clause 14.2.4.3 |
| &gt;&gt; defaultDS.instanceEnable | RW | RW | IEEE Std 802.1AS [104] clause 14.2.19 |
| &gt;&gt; timePropertiesDS.currentUtcOffset | RW | RW | IEEE Std 802.1AS [104] clause 14.5.2 |
| Time synchronization information for DS-TT ports |  |  |  |
| &gt; Time synchronization information for each DS-TT port |  |  |  |
| &gt; DS-TT port number | RW | RW |  |
| &gt;&gt; Time synchronization information for each PTP Instance |  |  |  |
| &gt;&gt; PTP Instance ID (NOTE 17) | RW | RW |  |
| &gt;&gt; Grandmaster on behalf of DS-TT enabled (NOTE 14) | RW | RW |  |
| IEEE Std 1588 [126] data sets (NOTE 15) |  |  |  |
| &gt;&gt; portDS.portIdentity | RW | RW | IEEE Std 1588 [126] clause 8.2.15.2.1 |
| &gt;&gt; portDS.portState | R | R | IEEE Std 1588 [126] clause 8.2.15.3.1 |
| &gt;&gt; portDS.logMinDelayReqInterval | RW | RW | IEEE Std 1588 [126] clause 8.2.15.3.2 |
| &gt;&gt; portDS.logAnnounceInterval | RW | RW | IEEE Std 1588 [126] clause 8.2.15.4.1 |
| &gt;&gt; portDS.announceReceiptTimeout | RW | RW | IEEE Std 1588 [126] clause 8.2.15.4.2 |
| &gt;&gt; portDS.logSyncInterval | RW | RW | IEEE Std 1588 [126] clause 8.2.15.4.3 |
| &gt;&gt; portDS.delayMechanism | RW | RW | IEEE Std 1588 [126] clause 8.2.15.4.4 |
| &gt;&gt; portDS.logMinPdelayReqInterval | RW | RW | IEEE Std 1588 [126] clause 8.2.15.4.5 |
| &gt;&gt; portDS.versionNumber | RW | RW | IEEE Std 1588 [126] clause 8.2.15.4.6 |
| &gt;&gt; portDS.minorVersionNumber | RW | RW | IEEE Std 1588 [126] clause 8.2.15.4.7 |
| &gt;&gt; portDS.delayAsymmetry | RW | RW | IEEE Std 1588 [126] clause 8.2.15.4.8 |
| &gt;&gt; portDS.portEnable | RW | RW | IEEE Std 1588 [126] clause 8.2.15.5.1 |
| &gt;&gt; externalPortConfigurationPortDS.desiredState | RW | RW | IEEE Std 1588 [126] clause 15.5.3.7.15.1 |
| IEEE Std 802.1AS [104] data sets (NOTE 15) |  |  |  |
| &gt;&gt; portDS.portIdentity | RW | RW | IEEE Std 802.1AS [104] clause 14.8.2 |
| &gt;&gt; portDS.portState | R | R | IEEE Std 802.1AS [104] clause 14.8.3 |
| &gt;&gt; portDS.ptpPortEnabled | RW | RW | IEEE Std 802.1AS [104] clause 14.8.4 |
| &gt;&gt; portDS.delayMechanism | RW | RW | IEEE Std 802.1AS [104] clause 14.8.5 |
| &gt;&gt; portDS.isMeasuringDelay | R | R | IEEE Std 802.1AS [104] clause 14.8.6 |
| &gt;&gt; portDS.asCapable | R | R | IEEE Std 802.1AS [104] clause 14.8.7 |
| &gt;&gt; portDS.meanLinkDelay | R | R | IEEE Std 802.1AS [104] clause 14.8.8 |
| &gt;&gt; portDS.meanLinkDelayThresh | RW | RW | IEEE Std 802.1AS [104] clause 14.8.9 |
| &gt;&gt; portDS.delayAsymmetry | RW | RW | IEEE Std 802.1AS [104] clause 14.8.10 |
| &gt;&gt; portDS.neighborRateRatio | R | R | IEEE Std 802.1AS [104] clause 14.8.11 |
| &gt;&gt; portDS.initialLogAnnounceInterval | RW | RW | IEEE Std 802.1AS [104] clause 14.8.12 |
| &gt;&gt; portDS.currentLogAnnounceInterval | R | R | IEEE Std 802.1AS [104] clause 14.8.13 |
| &gt;&gt; portDS.useMgtSettableLogAnnounceInterval | RW | RW | IEEE Std 802.1AS [104] clause 14.8.14 |
| &gt;&gt; portDS.mgtSettableLogAnnounceInterval | RW | RW | IEEE Std 802.1AS [104] clause 14.8.15 |
| &gt;&gt; portDS.announceReceiptTimeout | RW | RW | IEEE Std 802.1AS [104] clause 14.8.16 |
| &gt;&gt; portDS.initialLogSyncInterval | RW | RW | IEEE Std 802.1AS [104] clause 14.8.17 |
| &gt;&gt; portDS.currentLogSyncInterval | R | R | IEEE Std 802.1AS [104] clause 14.8.18 |
| &gt;&gt; portDS.useMgtSettableLogSyncInterval | RW | RW | IEEE Std 802.1AS [104] clause 14.8.19 |
| &gt;&gt; portDS.mgtSettableLogSyncInterval | RW | RW | IEEE Std 802.1AS [104] clause 14.8.20 |
| &gt;&gt; portDS.syncReceiptTimeout | RW | RW | IEEE Std 802.1AS [104] clause 14.8.21 |
| &gt;&gt; portDS.syncReceiptTimeoutTimeInterval | RW | RW | IEEE Std 802.1AS [104] clause 14.8.22 |
| &gt;&gt; portDS.initialLogPdelayReqInterval | RW | RW | IEEE Std 802.1AS [104] clause 14.8.23 |
| &gt;&gt; portDS.currentLogPdelayReqInterval | R | R | IEEE Std 802.1AS [104] clause 14.8.24 |
| &gt;&gt; portDS.useMgtSettableLogPdelayReqInterval | RW | RW | IEEE Std 802.1AS [104] clause 14.8.25 |
| &gt;&gt; portDS.mgtSettableLogPdelayReqInterval | RW | RW | IEEE Std 802.1AS [104] clause 14.8.26 |
| &gt;&gt; portDS.initialLogGptpCapableMessageInterval | RW | RW | IEEE Std 802.1AS [104] clause 14.8.27 |
| &gt;&gt; portDS.currentLogGptpCapableMessageInterval | R | R | IEEE Std 802.1AS [104] clause 14.8.28 |
| &gt;&gt; portDS.useMgtSettableLogGptpCapableMessageInterval | RW | RW | IEEE Std 802.1AS [104] clause 14.8.29 |
| &gt;&gt; portDS.mgtSettableLogGptpCapableMessageInterval | RW | RW | IEEE Std 802.1AS [104] clause 14.8.30 |
| &gt;&gt; portDS.initialComputeNeighborRateRatio | RW | RW | IEEE Std 802.1AS [104] clause 14.8.31 |
| &gt;&gt; portDS.currentComputeNeighborRateRatio | R | R | IEEE Std 802.1AS [104] clause 14.8.32 |
| &gt;&gt; portDS.useMgtSettableComputeNeighborRateRatio | RW | RW | IEEE Std 802.1AS [104] clause 14.8.33 |
| &gt;&gt; portDS.mgtSettableComputeNeighborRateRatio | RW | RW | IEEE Std 802.1AS [104] clause 14.8.34 |
| &gt;&gt; portDS.initialComputeMeanLinkDelay | RW | RW | IEEE Std 802.1AS [104] clause 14.8.35 |
| &gt;&gt; portDS.currentComputeMeanLinkDelay | R | R | IEEE Std 802.1AS [104] clause 14.8.36 |
| &gt;&gt; portDS.useMgtSettableComputeMeanLinkDelay | RW | RW | IEEE Std 802.1AS [104] clause 14.8.37 |
| &gt;&gt; portDS.mgtSettableComputeMeanLinkDelay | RW | RW | IEEE Std 802.1AS [104] clause 14.8.38 |
| &gt;&gt; portDS.allowedLostResponses | RW | RW | IEEE Std 802.1AS [104] clause 14.8.39 |
| &gt;&gt; portDS.allowedFaults | RW | RW | IEEE Std 802.1AS [104] clause 14.8.40 |
| &gt;&gt; portDS.gPtpCapableReceiptTimeout | RW | RW | IEEE Std 802.1AS [104] clause 14.8.41 |
| &gt;&gt; portDS.versionNumber | RW | RW | IEEE Std 802.1AS [104] clause 14.8.42 |
| &gt;&gt; portDS.nup | RW | RW | IEEE Std 802.1AS [104] clause 14.8.43 |
| &gt;&gt; portDS.ndown | RW | RW | IEEE Std 802.1AS [104] clause 14.8.44 |
| &gt;&gt; portDS.oneStepTxOper | R | R | IEEE Std 802.1AS [104] clause 14.8.45 |
| &gt;&gt; portDS.oneStepReceive | R | R | IEEE Std 802.1AS [104] clause 14.8.46 |
| &gt;&gt; portDS.oneStepTransmit | R | R | IEEE Std 802.1AS [104] clause 14.8.47 |
| &gt;&gt; portDS.initialOneStepTxOper | RW | RW | IEEE Std 802.1AS [104] clause 14.8.48 |
| &gt;&gt; portDS.currentOneStepTxOper | RW | RW | IEEE Std 802.1AS [104] clause 14.8.49 |
| &gt;&gt; portDS.useMgtSettableOneStepTxOper | RW | RW | IEEE Std 802.1AS [104] clause 14.8.50 |
| &gt;&gt; portDS.mgtSettableOneStepTxOper | RW | RW | IEEE Std 802.1AS [104] clause 14.8.51 |
| &gt;&gt; portDS.syncLocked | R | R | IEEE Std 802.1AS [104] clause 14.8.52 |
| &gt;&gt; portDS.pdelayTruncatedTimestampsArray | RW | RW | IEEE Std 802.1AS [104] clause 14.8.53 |
| &gt;&gt; portDS.minorVersionNumber | RW | RW | IEEE Std 802.1AS [104] clause 14.8.54 |
| &gt;&gt; externalPortConfigurationPortDS.desiredState | RW | RW | IEEE Std 802.1AS [104] clause 14.12.2 |
| Time synchronization status (TSS) information |  |  |  |
| &gt; Synchronization state | - | R | Table 5.27.1.12-1 |
| &gt; Clock quality | - | R | Table 5.27.1.12-1 |
| &gt;&gt; Traceable to UTC | - | R | Table 5.27.1.12-1 |
| &gt;&gt; Traceable to GNSS | - | R | Table 5.27.1.12-1 |
| &gt;&gt; Frequency stability | - | R | Table 5.27.1.12-1 |
| &gt;&gt; Clock accuracy | - | R | Table 5.27.1.12-1 |
| &gt; Parent time source | - | R | Table 5.27.1.12-1 |
| NOTE 1: R = Read only access; RW = Read/Write access; ― = not supported. NOTE 2: General neighbor discovery information is included only when NW-TT performs neighbor discovery on behalf of DS-TT. When a parameter in this group is changed, it is necessary to provide the change to every DS-TT and the NW-TT that belongs to the 5GS TSN bridge. NOTE 3: If the Static Filtering Entry information is present, UPF/NW-TT can use Static Filtering Entry information for forwarding TSC traffic, as specified in clause 5.8.2.5.3. NOTE 4: DS-TT discovery configuration and DS-TT discovery information are used only when DS-TT does not support LLDP and NW-TT performs neighbor discovery on behalf of DS-TT. TSN AF indicates the discovered neighbor information for each DS-TT port to CNC. NOTE 5: TSN AF indicates the support for PSFP to the CNC only if each DS-TT and NW-TT of the 5GS bridge have indicated support of PSFP. The support of PSFP at the NW-TT ports is expressed by setting higher than zero values for MaxStreamFilterInstances, MaxStreamGateInstances, MaxFlowMeterInstances, SupportedListMax parameters. NOTE 6: Enumeration of supported PTP instance types. Allowed values as defined in clause 8.2.1.5.5 of IEEE Std 1588 [126]. NOTE 7: Enumeration of supported transport types. Allowed values: IPv4 (as defined in IEEE Std 1588 [126] Annex C), IPv6 (as defined in IEEE Std 1588 [126] Annex D), Ethernet (as defined in Annex E of IEEE Std 1588 [126]). NOTE 8: Enumeration of supported PTP delay mechanisms. Allowed values as defined in clause 8.2.15.4.4 of IEEE Std 1588 [126]. NOTE 9: Indicates whether NW-TT supports acting as a PTP grandmaster. NOTE 10: Indicates whether NW-TT supports acting as a gPTP grandmaster. NOTE 11: Enumeration of supported PTP profiles, each identified by PTP profile ID, as defined in clause 20.3.3 of IEEE Std 1588 [126]. NOTE 12: PTP profile to apply, identified by PTP profile ID, as defined in clause 20.3.3 of IEEE Std 1588 [126]. NOTE 13: Transport type to use. Allowed values: IPv4 (as defined in Annex C of IEEE Std 1588 [126]), IPv6 (as defined in IEEE Std 1588 [126] Annex D), Ethernet (as defined in Annex E of IEEE Std 1588 [126]). NOTE 14: Indicates whether to act as grandmaster on behalf of a DS-TT port or not if 5GS is determined to be the grandmaster clock, i.e. whether to send Announce, Sync and optionally Follow_Up messages on behalf of DS-TT. NOTE 15: The IEEE Std 802.1AS [104] data sets apply if the IEEE 802.1AS PTP profile is used; otherwise, the IEEE Std 1588 [126] data sets apply. NOTE 16: Specifies the default data set for each PTP instance identified by PTP instance ID within the user plane node. NOTE 17: PTP Instance ID uniquely identifies a PTP instance within the user plane node. (x4) |
<!-- /table -->
