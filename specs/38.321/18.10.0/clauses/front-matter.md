3GPP TS 38.321 V18.10.0 (2026-06)

Technical Specification

3rd Generation Partnership Project;

Technical Specification Group Radio Access Network;

NR;

Medium Access Control (MAC) protocol specification

(Release 18)

The present document has been developed within the 3rd Generation Partnership Project (3GPP <sup>TM</sup>) and may be further elaborated for the purposes of 3GPP.  
The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented.  
This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification.  
Specifications and Reports for implementation of the 3GPP <sup>TM</sup> system should be obtained via the 3GPP Organizational Partners' Publications Offices.

> ***3GPP***
> 
> Postal address
> 
> 3GPP support office address
> 
> 650 Route des Lucioles - Sophia Antipolis
> 
> Valbonne - FRANCE
> 
> Tel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16
> 
> Internet
> 
> http://www.3gpp.org

***Copyright Notification***

No part may be reproduced except as authorized by written permission.  
The copyright and the foregoing restriction extend to reproduction in all media.

© 2026, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC).

All rights reserved.

UMTS™ is a Trade Mark of ETSI registered for the benefit of its members

3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners  
LTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners

GSM® and the GSM logo are registered and owned by the GSM Association

Bluetooth® is a Trade Mark of the Bluetooth SIG registered for the benefit of its members

#   
Contents

Foreword 8

1 Scope 9

2 References 9

3 Definitions, symbols and abbreviations 10

3.1 Definitions 10

3.2 Abbreviations 12

4 General 14

4.1 Introduction 14

4.2 MAC architecture 14

4.2.1 General 14

4.2.2 MAC Entities 14

4.3 Services 16

4.3.1 Services provided to upper layers 16

4.3.2 Services expected from physical layer 16

4.4 Functions 16

4.5 Channel structure 17

4.5.1 General 17

4.5.2 Transport Channels 17

4.5.3 Logical Channels 17

4.5.4 Mapping of Transport Channels to Logical Channels 18

4.5.4.1 General 18

4.5.4.2 Uplink mapping 18

4.5.4.3 Downlink mapping 18

4.5.4.4 Sidelink mapping 18

5 MAC procedures 19

5.1 Random Access procedure 19

5.1.1 Random Access procedure initialization 19

5.1.1a Initialization of variables specific to Random Access type 24

5.1.1b Selection of the set of Random Access resources for the Random Access procedure 27

5.1.1c Availability of the set of Random Access resources 33

5.1.1d Selection of the set of Random Access resources based on feature prioritization 33

5.1.1e Selection of Msg1 repetition for SI request 34

5.1.2 Random Access Resource selection 34

5.1.2a Random Access Resource selection for 2-step RA type 37

5.1.3 Random Access Preamble transmission 39

5.1.3a MSGA transmission 40

5.1.4 Random Access Response reception 42

5.1.4a MSGB reception and contention resolution for 2-step RA type 46

5.1.5 Contention Resolution 49

5.1.6 Completion of the Random Access procedure 51

5.2 Maintenance of Uplink Time Alignment 52

5.2a Maintenance of UL Synchronization 56

5.3 DL-SCH data transfer 57

5.3.1 DL Assignment reception 57

5.3.2 HARQ operation 59

5.3.2.1 HARQ Entity 59

5.3.2.2 HARQ process 60

5.3.3 Disassembly and demultiplexing 61

5.4 UL-SCH data transfer 62

5.4.1 UL Grant reception 62

5.4.2 HARQ operation 67

5.4.2.1 HARQ Entity 67

5.4.2.2 HARQ process 71

5.4.3 Multiplexing and assembly 73

5.4.3.1 Logical Channel Prioritization 73

5.4.3.1.1 General 73

5.4.3.1.2 Selection of logical channels 74

5.4.3.1.3 Allocation of resources 74

5.4.3.2 Multiplexing of MAC Control Elements and MAC SDUs 76

5.4.4 Scheduling Request 76

5.4.5 Buffer Status Reporting 82

5.4.6 Power Headroom Reporting 85

5.4.7 Pre-emptive Buffer Status Reporting 92

5.4.8 Timing Advance Reporting 93

5.4.9 Delay status reporting 93

5.5 PCH reception 94

5.6 BCH reception 95

5.7 Discontinuous Reception (DRX) 95

5.7a Discontinuous Reception (DRX) for MBS Broadcast 103

5.7b Discontinuous Reception (DRX) for MBS Multicast 104

5.8 Transmission and reception without dynamic scheduling 108

5.8.1 Downlink 108

5.8.1a Downlink for Multicast 108

5.8.2 Uplink 109

5.8.3 Sidelink 114

5.9 Activation/Deactivation of SCells 115

5.10 Activation/Deactivation of PDCP duplication 117

5.11 MAC reconfiguration 118

5.12 MAC Reset 119

5.12a Void 121

5.13 Handling of unknown, unforeseen and erroneous protocol data 121

5.14 Handling of measurement gaps 121

5.15 Bandwidth Part (BWP) operation 121

5.15.1 Downlink and Uplink 121

5.15.2 Sidelink 126

5.16 SUL operation 127

5.17 Beam Failure Detection and Recovery procedure 127

5.18 Handling of MAC CEs 131

5.18.1 General 131

5.18.2 Activation/Deactivation of Semi-persistent CSI-RS/CSI-IM resource set 132

5.18.3 Aperiodic CSI Trigger State Subselection 133

5.18.4 Activation/Deactivation of UE-specific PDSCH TCI state 133

5.18.5 Indication of TCI state for UE-specific PDCCH 133

5.18.6 Activation/Deactivation of Semi-persistent CSI reporting on PUCCH 134

5.18.7 Activation/Deactivation of Semi-persistent SRS and Indication of spatial relation of SP/AP SRS 134

5.18.8 Activation/Deactivation of spatial relation of PUCCH resource 134

5.18.9 Activation/Deactivation of semi-persistent ZP CSI-RS resource set 135

5.18.10 Recommended Bit Rate 135

5.18.11 Void 136

5.18.12 Void 136

5.18.13 Void 136

5.18.14 Update of Pathloss Reference RS of SRS 136

5.18.15 Update of Pathloss Reference RS of PUSCH 136

5.18.16 Indication of spatial relation of SRS resource for a Serving Cell set 136

5.18.17 Activation/Deactivation of Semi-Persistent Positioning SRS 137

5.18.18 Timing offset adjustments for IAB 137

5.18.19 Guard symbols for IAB 137

5.18.20 Positioning Measurement Gap Activation/Deactivation Command 138

5.18.21 PPW Activation/Deactivation Command 138

5.18.22 Update of PUCCH Power Control Set for multiple TRP PUCCH repetition 139

5.18.23 Unified TCI States Activation/Deactivation MAC CE 139

5.18.24 Update of Differential Koffset 139

5.18.25 BFD-RS Indication MAC CE 139

5.18.26 Restricted and recommended beam indication for IAB 139

5.18.27 DL TX power adjustment for IAB 140

5.18.28 UL PSD range adjustment for IAB 141

5.18.29 Timing case indication for IAB 141

5.18.30 Case-6 Timing Request 141

5.18.31 Backhaul Link Beam Indication for NCR 141

5.18.32 Access Link Beam Indication for NCR 142

5.18.33 Enhanced Unified TCI States Activation/Deactivation MAC CE 142

5.18.34 Activation/deactivation of PSI-based SDU discard 142

5.18.35 LTM Cell Switch Command 142

5.18.36 Candidate Cell TCI States Activation/Deactivation 143

5.18.37 Activation/Deactivation of Aggregated Semi-Persistent Positioning SRS 143

5.19 Data inactivity monitoring 144

5.20 Void 144

5.21 LBT operation 144

5.21.1 General 144

5.21.2 LBT failure detection and recovery procedure 144

5.22 SL-SCH Data transfer and SL-PRS transmission 146

5.22.1 SL-SCH Data and SL-PRS transmission 146

5.22.1.1 SL Grant reception and SCI transmission 146

5.22.1.2 TX resource (re-)selection check 168

5.22.1.2a Re-evaluation and Pre-emption 169

5.22.1.2b Re-selection for using a received resource conflict indication 171

5.22.1.2c Resource re-selection from SL LBT Failure indication 172

5.22.1.3 Sidelink HARQ operation and SL-PRS transmission 172

5.22.1.3.1 Sidelink HARQ Entity 172

5.22.1.3.1a Sidelink process not associated with Dedicated SL-PRS resource pool 175

5.22.1.3.2 PSFCH reception 177

5.22.1.3.3 HARQ-based Sidelink RLF detection 178

5.22.1.3.4 Processing of sidelink grant on Dedicated SL-PRS resource pool 179

5.22.1.3.5 Sidelink process associated with Dedicated SL-PRS resource pool 180

5.22.1.4 Multiplexing and assembly 180

5.22.1.4.0 General 180

5.22.1.4.1 Logical channel prioritization 180

5.22.1.4.2 Multiplexing of MAC Control Elements and MAC SDUs 185

5.22.1.5 Scheduling Request 185

5.22.1.6 Buffer Status Reporting 186

5.22.1.7 CSI Reporting 189

5.22.1.8 Void 189

5.22.1.9 IUC-Request transmission 189

5.22.1.10 IUC-Information Reporting 190

5.22.1.10.1 General 190

5.22.1.10.2 Reception of IUC-Information Reporting 191

5.22.1.11 TX carrier (re-)selection 191

5.22.1.12 SL-PRS Resource Request 193

5.22.2 SL-SCH Data and SL-PRS reception 193

5.22.2.1 SCI reception 193

5.22.2.2 Sidelink HARQ operation and SL-PRS reception on Shared SL-PRS resource pool 194

5.22.2.2.1 Sidelink HARQ Entity 194

5.22.2.2.2 Sidelink process 195

5.22.2.3 Disassembly and demultiplexing 196

5.22.2.4 SL-PRS reception on Dedicated SL-PRS resource pool 197

5.23 SL-BCH data transfer 197

5.23.1 SL-BCH data transmission 197

5.23.2 SL-BCH data reception 197

5.24 Handling of PRS Processing Window 197

5.25 Positioning Measurement Gap Activation/Deactivation Request 198

5.26 Positioning SRS transmission in RRC\_INACTIVE 198

5.26.1 General 198

5.26.2 TA validation for SRS transmission in RRC\_INACTIVE 198

5.27 Small Data Transmission 199

5.27.1 General 199

5.27.2 TA Validation for CG-SDT 201

5.28 Sidelink Discontinuous Reception (DRX) 202

5.28.1 General 202

5.28.2 Behaviour of UE receiving SL-SCH Data 202

5.28.3 Behaviour of UE transmitting SL-SCH Data 206

5.29 Activation/Deactivation of SCG 207

5.30 Handling of FR2 UL gap 208

5.31 Sidelink LBT operation 208

5.31.1 General 208

5.31.2 Sidelink LBT failure detection and recovery procedure 208

5.32 Void 209

5.33 First PUSCH transmission of RACH-less handover 209

5.34 Cell-Level Energy Saving 210

5.34.1 General 210

5.34.2 Cell Discontinuous Transmission 210

5.34.3 Cell Discontinuous Reception 212

6 Protocol Data Units, formats and parameters 213

6.1 Protocol Data Units 213

6.1.1 General 213

6.1.2 MAC PDU (DL-SCH and UL-SCH except transparent MAC and Random Access Response) 213

6.1.3 MAC Control Elements (CEs) 216

6.1.3.1 Buffer Status Report MAC CEs 216

6.1.3.2 C-RNTI MAC CE 225

6.1.3.3 UE Contention Resolution Identity MAC CE 225

6.1.3.4 Timing Advance Command MAC CE 225

6.1.3.4a Absolute Timing Advance Command MAC CE 226

6.1.3.5 DRX Command MAC CE 226

6.1.3.6 Long DRX Command MAC CE 226

6.1.3.7 Configured Grant Confirmation MAC CE 226

6.1.3.8 Single Entry PHR MAC CE 226

6.1.3.9 Multiple Entry PHR MAC CE 228

6.1.3.10 SCell Activation/Deactivation MAC CEs 231

6.1.3.11 Duplication Activation/Deactivation MAC CE 232

6.1.3.12 SP CSI-RS/CSI-IM Resource Set Activation/Deactivation MAC CE 232

6.1.3.13 Aperiodic CSI Trigger State Subselection MAC CE 233

6.1.3.14 TCI States Activation/Deactivation for UE-specific PDSCH MAC CE 234

6.1.3.15 TCI State Indication for UE-specific PDCCH MAC CE 235

6.1.3.16 SP CSI reporting on PUCCH Activation/Deactivation MAC CE 235

6.1.3.17 SP SRS Activation/Deactivation MAC CE 236

6.1.3.18 PUCCH spatial relation Activation/Deactivation MAC CE 237

6.1.3.19 SP ZP CSI-RS Resource Set Activation/Deactivation MAC CE 238

6.1.3.20 Recommended bit rate MAC CE 238

6.1.3.21 Timing Delta MAC CE 239

6.1.3.22 Guard Symbols MAC CEs 240

6.1.3.23 BFR MAC CEs 241

6.1.3.24 Enhanced TCI States Activation/Deactivation for UE-specific PDSCH MAC CE 242

6.1.3.25 Enhanced PUCCH Spatial Relation Activation/Deactivation MAC CE 243

6.1.3.26 Enhanced SP/AP SRS Spatial Relation Indication MAC CE 244

6.1.3.27 SRS Pathloss Reference RS Update MAC CE 245

6.1.3.28 PUSCH Pathloss Reference RS Update MAC CE 246

6.1.3.29 Serving Cell Set based SRS Spatial Relation Indication MAC CE 246

6.1.3.30 LBT failure MAC CEs 248

6.1.3.31 Multiple Entry Configured Grant Confirmation MAC CE 249

6.1.3.32 Duplication RLC Activation/Deactivation MAC CE 249

6.1.3.33 Sidelink Buffer Status Report MAC CEs 249

6.1.3.34 Sidelink Configured Grant Confirmation MAC CE 250

6.1.3.35 Sidelink CSI Reporting MAC CE 251

6.1.3.36 SP Positioning SRS Activation/Deactivation MAC CE 251

6.1.3.37 Guard Symbols MAC CEs for Case-6 and Case-7 timing modes 254

6.1.3.38 Case-7 Timing advance offset MAC CE 255

6.1.3.39 Case-6 Timing Request MAC CE 255

6.1.3.40 Positioning Measurement Gap Activation/Deactivation Request MAC CE 255

6.1.3.41 Positioning Measurement Gap Activation/Deactivation Command MAC CE 256

6.1.3.42 PPW Activation/Deactivation Command MAC CE 256

6.1.3.43 Enhanced BFR MAC CEs 257

6.1.3.44 Enhanced TCI States Indication for UE-specific PDCCH MAC CE 260

6.1.3.45 PUCCH spatial relation Activation/Deactivation for multiple TRP PUCCH repetition MAC CE 261

6.1.3.46 PUCCH Power Control Set Update for multiple TRP PUCCH repetition MAC CE 262

6.1.3.47 Unified TCI States Activation/Deactivation MAC CE 263

6.1.3.48 Enhanced Single Entry PHR MAC CE 264

6.1.3.49 Enhanced Multiple Entry PHR MAC CE 265

6.1.3.50 Enhanced Single Entry PHR for multiple TRP MAC CE 270

6.1.3.51 Enhanced Multiple Entry PHR for multiple TRP MAC CE 270

6.1.3.52 Sidelink DRX Command MAC CE 273

6.1.3.53 Sidelink Inter-UE Coordination Information MAC CE 273

6.1.3.54 Sidelink Inter-UE Coordination Request MAC CE 276

6.1.3.55 Enhanced SCell Activation/Deactivation MAC CEs 278

6.1.3.56 Timing Advance Report MAC CE 279

6.1.3.57 Differential Koffset MAC CE 279

6.1.3.58 BFD-RS Indication MAC CE 279

6.1.3.59 SP/AP SRS TCI State Indication MAC CE 280

6.1.3.60 Serving Cell Set based SRS TCI State Indication MAC CE 281

6.1.3.61 Child IAB-DU Restricted Beam Indication MAC CE 282

6.1.3.62 IAB-MT Recommended Beam Indication MAC CE 286

6.1.3.63 DL TX Power Adjustment and Desired DL TX Power Adjustment MAC CEs 289

6.1.3.64 Desired IAB-MT PSD range MAC CE 290

6.1.3.65 Timing Case Indication MAC CE 292

6.1.3.66 NCR Downlink Backhaul Link Beam Indication MAC CE 293

6.1.3.67 NCR Uplink Backhaul Link Beam Indication MAC CE 293

6.1.3.68 NCR Access Link Beam Indication MAC CE 294

6.1.3.69 SL LBT failure MAC CE 294

6.1.3.70 Enhanced Unified TCI States Activation/Deactivation MAC CE for Joint TCI States 294

6.1.3.71 Enhanced Unified TCI States Activation/Deactivation MAC CE for Separate TCI States 295

6.1.3.72 Delay Status Report MAC CE 296

6.1.3.73 PSI-Based SDU Discard Activation/Deactivation MAC CE 297

6.1.3.74 SL-PRS Resource Request MAC CE 298

6.1.3.75 LTM Cell Switch Command MAC CE 298

6.1.3.76 Candidate Cell TCI States Activation/Deactivation MAC CE 300

6.1.3.77 Cross-RRH TCI State Indication for UE-specific PDCCH MAC CE 301

6.1.3.78 Single Entry PHR with assumed PUSCH MAC CE 302

6.1.3.79 Multiple Entry PHR with assumed PUSCH MAC CE 303

6.1.3.80 Enhanced SP CSI reporting on PUCCH Activation/Deactivation MAC CE 306

6.1.3.81 Enhanced Single Entry PHR for multiple TRP STx2P MAC CE 307

6.1.3.82 Enhanced Multiple Entry PHR for multiple TRP STx2P MAC CE 308

6.1.3.83 Aggregated SP Positioning SRS Activation/Deactivation MAC CE 311

6.1.4 MAC PDU (transparent MAC) 313

6.1.5 MAC PDU (Random Access Response) 313

6.1.5a MAC PDU (MSGB) 314

6.1.6 MAC PDU (SL-SCH) 315

6.2 Formats and parameters 316

6.2.1 MAC subheader for DL-SCH and UL-SCH 316

6.2.2 MAC subheader for Random Access Response 321

6.2.2a MAC subheader for MSGB 321

6.2.3 MAC payload for Random Access Response 322

6.2.3a MAC payload for MSGB 323

6.2.4 MAC subheader for SL-SCH 325

7 Variables and constants 326

7.1 RNTI values 326

7.2 Backoff Parameter values 329

7.3 DELTA\_PREAMBLE values 329

7.4 PRACH Mask Index values 330

Annex A (informative): Change history 331

#   
Foreword

This Technical Specification has been produced by the 3rd Generation Partnership Project (3GPP).

The contents of the present document are subject to continuing work within the TSG and may change following formal TSG approval. Should the TSG modify the contents of the present document, it will be re-released by the TSG with an identifying change of release date and an increase in version number as follows:

Version x.y.z

where:

x the first digit:

1 presented to TSG for information;

2 presented to TSG for approval;

3 or greater indicates TSG approved document under change control.

y the second digit is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc.

z the third digit is incremented when editorial only changes have been incorporated in the document.
