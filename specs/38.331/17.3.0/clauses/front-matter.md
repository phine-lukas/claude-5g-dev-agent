3GPP TS 38.331 V17.3.0 (2022-12)

Technical Specification

3rd Generation Partnership Project;

Technical Specification Group Radio Access Network;

NR;

Radio Resource Control (RRC) protocol specification

(Release 17)

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

© 2022, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC).

All rights reserved.

UMTS™ is a Trade Mark of ETSI registered for the benefit of its members

3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners  
LTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners

GSM® and the GSM logo are registered and owned by the GSM Association

#   
Contents

Foreword 23

1 Scope 24

2 References 24

3 Definitions, symbols and abbreviations 27

3.1 Definitions 27

3.2 Abbreviations 29

4 General 31

4.1 Introduction 31

4.2 Architecture 32

4.2.1 UE states and state transitions including inter RAT 32

4.2.2 Signalling radio bearers 35

4.3 Services 35

4.3.1 Services provided to upper layers 35

4.3.2 Services expected from lower layers 36

4.4 Functions 36

5 Procedures 37

5.1 General 37

5.1.1 Introduction 37

5.1.2 General requirements 37

5.1.3 Requirements for UE in MR-DC 38

5.2 System information 38

5.2.1 Introduction 38

5.2.2 System information acquisition 39

5.2.2.1 General UE requirements 39

5.2.2.2 SIB validity and need to (re)-acquire SIB 39

5.2.2.2.1 SIB validity 39

5.2.2.2.2 SI change indication and PWS notification 41

5.2.2.3 Acquisition of System Information 42

5.2.2.3.1 Acquisition of *MIB* and *SIB1* 42

5.2.2.3.2 Acquisition of an SI message 43

5.2.2.3.3 Request for on demand system information 45

5.2.2.3.3a Request for on demand positioning system information 46

5.2.2.3.4 Actions related to transmission of *RRCSystemInfoRequest* message 47

5.2.2.3.5 Acquisition of SIB(s) or posSIB(s) in RRC\_CONNECTED 47

5.2.2.3.6 Actions related to transmission of *DedicatedSIBRequest* message 48

5.2.2.4 Actions upon receipt of System Information 48

5.2.2.4.1 Actions upon reception of the *MIB* 48

5.2.2.4.2 Actions upon reception of the *SIB1* 49

5.2.2.4.3 Actions upon reception of *SIB2* 53

5.2.2.4.4 Actions upon reception of *SIB3* 53

5.2.2.4.5 Actions upon reception of *SIB4* 54

5.2.2.4.6 Actions upon reception of *SIB5* 54

5.2.2.4.7 Actions upon reception of *SIB6* 55

5.2.2.4.8 Actions upon reception of *SIB7* 55

5.2.2.4.9 Actions upon reception of *SIB8* 55

5.2.2.4.10 Actions upon reception of *SIB9* 56

5.2.2.4.11 Actions upon reception of *SIB10* 56

5.2.2.4.12 Actions upon reception of *SIB11* 56

5.2.2.4.13 Actions upon reception of *SIB12* 56

5.2.2.4.14 Actions upon reception of *SIB13* 58

5.2.2.4.15 Actions upon reception of *SIB14* 58

5.2.2.4.16 Actions upon reception of *SIBpos* 58

5.2.2.4.17 Actions upon reception of *SIB15* 58

5.2.2.4.18 Actions upon reception of *SIB16* 58

5.2.2.4.19 Actions upon reception of *SIB17* 58

5.2.2.4.20 Actions upon reception of *SIB18* 58

5.2.2.4.21 Actions upon reception of *SIB19* 58

5.2.2.4.22 Actions upon reception of *SIB20* 59

5.2.2.4.23 Actions upon reception of *SIB21* 59

5.2.2.5 Essential system information missing 59

5.2.2.6 T430 expiry 59

5.3 Connection control 59

5.3.1 Introduction 59

5.3.1.1 RRC connection control 59

5.3.1.2 AS Security 60

5.3.2 Paging 61

5.3.2.1 General 61

5.3.2.2 Initiation 62

5.3.2.3 Reception of the *Paging* *message* by the UE or *PagingRecord* by the L2 U2N Remote UE 62

5.3.3 RRC connection establishment 64

5.3.3.1 General 64

5.3.3.1a Conditions for establishing RRC Connection for NR sidelink communication/discovery/V2X sidelink communication 64

5.3.3.2 Initiation 65

5.3.3.3 Actions related to transmission of *RRCSetupRequest* message 65

5.3.3.4 Reception of the *RRCSetup* by the UE 66

5.3.3.5 Reception of the *RRCReject* by the UE 70

5.3.3.6 Cell re-selection or cell selection or relay (re)selection while T390, T300 or T302 is running (UE in RRC\_IDLE) 70

5.3.3.7 T300 expiry 70

5.3.3.8 Abortion of RRC connection establishment 72

5.3.4 Initial AS security activation 72

5.3.4.1 General 72

5.3.4.2 Initiation 72

5.3.4.3 Reception of the *SecurityModeCommand* by the UE 72

5.3.5 RRC reconfiguration 73

5.3.5.1 General 73

5.3.5.2 Initiation 74

5.3.5.3 Reception of an *RRCReconfiguration* by the UE 75

5.3.5.4 Secondary cell group release 86

5.3.5.5 Cell Group configuration 86

5.3.5.5.1 General 86

5.3.5.5.2 Reconfiguration with sync 87

5.3.5.5.3 RLC bearer release 89

5.3.5.5.4 RLC bearer addition/modification 89

5.3.5.5.5 MAC entity configuration 90

5.3.5.5.6 RLF Timers & Constants configuration 91

5.3.5.5.7 SpCell Configuration 91

5.3.5.5.8 SCell Release 92

5.3.5.5.9 SCell Addition/Modification 93

5.3.5.5.10 BH RLC channel release 93

5.3.5.5.11 BH RLC channel addition/modification 94

5.3.5.5.12 Uu Relay RLC channel release 94

5.3.5.5.13 Uu Relay RLC channel addition/modification 94

5.3.5.6 Radio Bearer configuration 94

5.3.5.6.1 General 94

5.3.5.6.2 SRB release 95

5.3.5.6.3 SRB addition/modification 95

5.3.5.6.4 DRB release 97

5.3.5.6.5 DRB addition/modification 97

5.3.5.6.6 Multicast MRB release 100

5.3.5.6.7 Multicast MRB addition/modification 101

5.3.5.7 AS Security key update 101

5.3.5.8 Reconfiguration failure 103

5.3.5.8.1 Void 103

5.3.5.8.2 Inability to comply with *RRCReconfiguration* 103

5.3.5.8.3 T304 expiry (Reconfiguration with sync Failure) or T420 expiry (Path switch failure) 105

5.3.5.9 Other configuration 106

5.3.5.9a MUSIM gap configuration 110

5.3.5.10 MR-DC release 111

5.3.5.11 Full configuration 111

5.3.5.12 BAP configuration 113

5.3.5.12a IAB Other Configuration 114

5.3.5.12a.1 IP address management 114

5.3.5.12a.1.1 IP Address Release 114

5.3.5.12a.1.2 IP Address Addition/Modification 114

5.3.5.13 Conditional Reconfiguration 115

5.3.5.13.1 General 115

5.3.5.13.2 Conditional reconfiguration removal 116

5.3.5.13.3 Conditional reconfiguration addition/modification 116

5.3.5.13.4 Conditional reconfiguration evaluation 116

5.3.5.13.4a Conditional reconfiguration evaluation of SN initiated inter-SN CPC for EN-DC 117

5.3.5.13.5 Conditional reconfiguration execution 118

5.3.5.13a SCG activation 118

5.3.5.13b SCG deactivation 119

5.3.5.13b1 SCG activation without SN message 119

5.3.5.13c FR2 UL gap configuration 119

5.3.5.13d Application layer measurement configuration 120

5.3.5.14 Sidelink dedicated configuration 121

5.3.5.15 L2 U2N Relay UE configuration 123

5.3.5.15.1 General 123

5.3.5.15.2 L2 U2N Remote UE Release 123

5.3.5.15.3 L2 U2N Remote UE Addition/Modification 123

5.3.5.16 L2 U2N Remote UE configuration 124

5.3.6 Counter check 124

5.3.6.1 General 124

5.3.6.2 Initiation 125

5.3.6.3 Reception of the *CounterCheck* message by the UE 125

5.3.7 RRC connection re-establishment 125

5.3.7.1 General 125

5.3.7.2 Initiation 126

5.3.7.3 Actions following cell selection while T311 is running 129

5.3.7.3a Actions following relay selection while T311 is running 131

5.3.7.4 Actions related to transmission of *RRCReestablishmentRequest* message 132

5.3.7.5 Reception of the *RRCReestablishment* by the UE 133

5.3.7.6 T311 expiry 134

5.3.7.7 T301 expiry or selected cell/L2 U2N Relay UE no longer suitable 134

5.3.7.8 Reception of the *RRCSetup* by the UE 135

5.3.8 RRC connection release 135

5.3.8.1 General 135

5.3.8.2 Initiation 135

5.3.8.3 Reception of the *RRCRelease* by the UE 135

5.3.8.4 T320 expiry 139

5.3.8.5 UE actions upon the expiry of *DataInactivityTimer* 139

5.3.8.6 T346g expiry 139

5.3.9 RRC connection release requested by upper layers 140

5.3.9.1 General 140

5.3.9.2 Initiation 140

5.3.10 Radio link failure related actions 140

5.3.10.1 Detection of physical layer problems in RRC\_CONNECTED 140

5.3.10.2 Recovery of physical layer problems 140

5.3.10.3 Detection of radio link failure 140

5.3.10.4 RLF cause determination 142

5.3.10.5 RLF report content determination 143

5.3.11 UE actions upon going to RRC\_IDLE 147

5.3.12 UE actions upon PUCCH/SRS release request 148

5.3.13 RRC connection resume 149

5.3.13.1 General 149

5.3.13.1a Conditions for resuming RRC Connection for NR sidelink communication/discovery/V2X sidelink communication 150

5.3.13.1b Conditions for initiating SDT 150

5.3.13.2 Initiation 150

5.3.13.3 Actions related to transmission of *RRCResumeRequest* or *RRCResumeRequest1* message 154

5.3.13.4 Reception of the *RRCResume* by the UE 155

5.3.13.5 Handling of failure to resume RRC Connection 160

5.3.13.6 Cell re-selection or cell selection or L2 U2N relay (re)selection while T390, T319 or T302 is running or SDT procedure is ongoing (UE in RRC\_INACTIVE) or SRS transmission in RRC\_INACTIVE is configured 162

5.3.13.7 Reception of the *RRCSetup* by the UE 162

5.3.13.8 RNA update 162

5.3.13.9 Reception of the *RRCRelease* by the UE 163

5.3.13.10 Reception of the *RRCReject* by the UE 163

5.3.13.11 Inability to comply with *RRCResume* 163

5.3.13.12 Inter RAT cell reselection 163

5.3.14 Unified Access Control 163

5.3.14.1 General 163

5.3.14.2 Initiation 163

5.3.14.3 Void 165

5.3.14.4 T302, T390 expiry or stop (Barring alleviation) 165

5.3.14.5 Access barring check 166

5.3.15 RRC connection reject 167

5.3.15.1 Initiation 167

5.3.15.2 Reception of the *RRCReject* by the UE 167

5.4 Inter-RAT mobility 168

5.4.1 Introduction 168

5.4.2 Handover to NR 168

5.4.2.1 General 168

5.4.2.2 Initiation 168

5.4.2.3 Reception of the *RRCReconfiguration* by the UE 168

5.4.3 Mobility from NR 169

5.4.3.1 General 169

5.4.3.2 Initiation 169

5.4.3.3 Reception of the *MobilityFromNRCommand* by the UE 169

5.4.3.4 Successful completion of the mobility from NR 170

5.4.3.5 Mobility from NR failure 170

5.5 Measurements 171

5.5.1 Introduction 171

5.5.2 Measurement configuration 174

5.5.2.1 General 174

5.5.2.2 Measurement identity removal 175

5.5.2.3 Measurement identity addition/modification 175

5.5.2.4 Measurement object removal 177

5.5.2.5 Measurement object addition/modification 177

5.5.2.6 Reporting configuration removal 179

5.5.2.7 Reporting configuration addition/modification 179

5.5.2.8 Quantity configuration 180

5.5.2.9 Measurement gap configuration 180

5.5.2.10 Reference signal measurement timing configuration 182

5.5.2.10a RSSI measurement timing configuration 183

5.5.2.11 Measurement gap sharing configuration 183

5.5.3 Performing measurements 184

5.5.3.1 General 184

5.5.3.2 Layer 3 filtering 189

5.5.3.3 Derivation of cell measurement results 190

5.5.3.3a Derivation of layer 3 beam filtered measurement 191

5.5.3.4 Derivation of L2 U2N Relay UE measurement results 191

5.5.4 Measurement report triggering 191

5.5.4.1 General 191

5.5.4.2 Event A1 (Serving becomes better than threshold) 198

5.5.4.3 Event A2 (Serving becomes worse than threshold) 198

5.5.4.4 Event A3 (Neighbour becomes offset better than SpCell) 199

5.5.4.5 Event A4 (Neighbour becomes better than threshold) 199

5.5.4.6 Event A5 (SpCell becomes worse than threshold1 and neighbour becomes better than threshold2) 200

5.5.4.7 Event A6 (Neighbour becomes offset better than SCell) 201

5.5.4.8 Event B1 (Inter RAT neighbour becomes better than threshold) 202

5.5.4.9 Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) 202

5.5.4.10 Event I1 (Interference becomes higher than threshold) 203

5.5.4.11 Event C1 (The NR sidelink channel busy ratio is above a threshold) 203

5.5.4.12 Event C2 (The NR sidelink channel busy ratio is below a threshold) 204

5.5.4.13 Void 204

5.5.4.14 Void 204

5.5.4.15 Event D1 (Distance between UE and referenceLocation1 is above threshold1 and distance between UE and referenceLocation2 is below threshold2) 204

5.5.4.16 CondEvent T1 (Time measured at UE is within a duration from threshold) 205

5.5.4.17 Event X1 (Serving L2 U2N Relay UE becomes worse than threshold1 and NR Cell becomes better than threshold2) 206

5.5.4.18 Event X2 (Serving L2 U2N Relay UE becomes worse than threshold) 207

5.5.4.19 Event Y1 (PCell becomes worse than threshold1 and candidate L2 U2N Relay UE becomes better than threshold2) 207

5.5.4.20 Event Y2 (Candidate L2 U2N Relay UE becomes better than threshold) 208

5.5.5 Measurement reporting 208

5.5.5.1 General 208

5.5.5.2 Reporting of beam measurement information 217

5.5.5.3 Sorting of cell measurement results 217

5.5.6 Location measurement indication 218

5.5.6.1 General 218

5.5.6.2 Initiation 218

5.5.6.3 Actions related to transmission of *LocationMeasurementIndication* message 219

5.5a Logged Measurements 220

5.5a.1 Logged Measurement Configuration 220

5.5a.1.1 General 220

5.5a.1.2 Initiation 220

5.5a.1.3 Reception of the *LoggedMeasurementConfiguration* by the UE 220

5.5a.1.4 T330 expiry 221

5.5a.2 Release of Logged Measurement Configuration 221

5.5a.2.1 General 221

5.5a.2.2 Initiation 221

5.5a.3 Measurements logging 221

5.5a.3.1 General 221

5.5a.3.2 Initiation 221

5.6 UE capabilities 224

5.6.1 UE capability transfer 224

5.6.1.1 General 224

5.6.1.2 Initiation 224

5.6.1.3 Reception of the *UECapabilityEnquiry* by the UE 224

5.6.1.4 Setting band combinations, feature set combinations and feature sets supported by the UE 225

5.6.1.5 Void 228

5.7 Other 228

5.7.1 DL information transfer 228

5.7.1.1 General 228

5.7.1.2 Initiation 228

5.7.1.3 Reception of the *DLInformationTransfer* by the UE 228

5.7.1a DL information transfer for MR-DC 229

5.7.1a.1 General 229

5.7.1a.2 Initiation 229

5.7.1a.3 Actions related to reception of *DLInformationTransferMRDC* message 229

5.7.2 UL information transfer 230

5.7.2.1 General 230

5.7.2.2 Initiation 230

5.7.2.3 Actions related to transmission of *ULInformationTransfer* message 230

5.7.2.4 Failure to deliver *ULInformationTransfer* message 230

5.7.2a UL information transfer for MR-DC 231

5.7.2a.1 General 231

5.7.2a.2 Initiation 231

5.7.2a.3 Actions related to transmission of *ULInformationTransferMRDC* message 231

5.7.2b UL transfer of IRAT information 231

5.7.2b.1 General 231

5.7.2b.2 Initiation 232

5.7.2b.3 Actions related to transmission of *ULInformationTransferIRAT* message 232

5.7.3 SCG failure information 232

5.7.3.1 General 232

5.7.3.2 Initiation 232

5.7.3.3 Failure type determination for (NG)EN-DC 233

5.7.3.4 Setting the contents of *MeasResultSCG-Failure* 234

5.7.3.5 Actions related to transmission of *SCGFailureInformation* message 234

5.7.3a EUTRA SCG failure information 237

5.7.3a.1 General 237

5.7.3a.2 Initiation 237

5.7.3a.3 Actions related to transmission of *SCGFailureInformationEUTRA* message 237

5.7.3b MCG failure information 238

5.7.3b.1 General 238

5.7.3b.2 Initiation 238

5.7.3b.3 Failure type determination 238

5.7.3b.4 Actions related to transmission of *MCGFailureInformation* message 239

5.7.3b.5 T316 expiry 240

5.7.4 UE Assistance Information 241

5.7.4.1 General 241

5.7.4.2 Initiation 241

5.7.4.3 Actions related to transmission of *UEAssistanceInformation* message 248

5.7.4.3a Setting the contents of *OverheatingAssistance* IE 256

5.7.4.4 Relaxed measurement criterion for a stationary RedCap UE 257

5.7.4a Void 257

5.7.5 Failure information 257

5.7.5.1 General 257

5.7.5.2 Initiation 258

5.7.5.3 Actions related to transmission of *FailureInformation* message 258

5.7.6 DL message segment transfer 258

5.7.6.1 General 258

5.7.6.2 Initiation 259

5.7.6.3 Reception of *DLDedicatedMessageSegment* by the UE 259

5.7.7 UL message segment transfer 259

5.7.7.1 General 259

5.7.7.2 Initiation 259

5.7.7.3 Actions related to transmission of *ULDedicatedMessageSegment* message 259

5.7.8 Idle/inactive Measurements 260

5.7.8.1 General 260

5.7.8.1a Measurement configuration 260

5.7.8.2 Void 261

5.7.8.2a Performing measurements 261

5.7.8.3 T331 expiry or stop 264

5.7.8.4 Cell re-selection or cell selection while T331 is running 264

5.7.9 Mobility history information 264

5.7.9.1 General 264

5.7.9.2 Initiation 264

5.7.10 UE Information 267

5.7.10.1 General 267

5.7.10.2 Initiation 268

5.7.10.3 Reception of the *UEInformationRequest* message 268

5.7.10.4 Actions upon successful completion of a random-access procedure or on completion of a request of on-demand system information 271

5.7.10.5 RA information determination 272

5.7.10.6 Actions for the successful handover report determination 274

5.7.12 IAB Other Information 277

5.7.12.1 General 277

5.7.12.2 Initiation 277

5.7.12.3 Actions related to transmission of *IABOtherInformation* message 278

5.7.13 RLM/BFD relaxation 279

5.7.13.1 Relaxed measurement criterion for low mobility 279

5.7.13.2 Relaxed measurement criterion for good serving cell quality 280

5.7.14 UE Positioning Assistance Information 280

5.7.14.1 General 280

5.7.14.2 Initiation 280

5.7.14.3 Actions related to transmission of *UEPositioningAssistanceInfo* message 280

5.7.15 Void 281

5.7.17 Derivation of pathloss reference for TA validation of SRS for Positioning transmission and CG-SDT in RRC\_INACTIVE 282

5.8 Sidelink 282

5.8.1 General 282

5.8.2 Conditions for NR sidelink communication/discovery operation 283

5.8.3 Sidelink UE information for NR sidelink communication/discovery 284

5.8.3.1 General 284

5.8.3.2 Initiation 284

5.8.3.3 Actions related to transmission of *SidelinkUEInformationNR* message 289

5.8.4 Void 293

5.8.5 Sidelink synchronisation information transmission for NR sidelink communication/discovery 293

5.8.5.1 General 293

5.8.5.2 Initiation 294

5.8.5.3 Transmission of SLSS 294

5.8.5a Sidelink synchronisation information transmission for V2X sidelink communication 296

5.8.5a.1 General 296

5.8.5a.2 Initiation 296

5.8.6 Sidelink synchronisation reference 296

5.8.6.1 General 296

5.8.6.2 Selection and reselection of synchronisation reference 296

5.8.6.3 Sidelink communication transmission reference cell selection 299

5.8.7 Sidelink communication reception 299

5.8.8 Sidelink communication transmission 300

5.8.9 Sidelink RRC procedure 302

5.8.9.1 Sidelink RRC reconfiguration 302

5.8.9.1.1 General 302

5.8.9.1.2 Actions related to transmission of *RRCReconfigurationSidelink* message 303

5.8.9.1.3 Reception of an *RRCReconfigurationSidelink* by the UE 304

5.8.9.1.4 Void 306

5.8.9.1.5 Void 306

5.8.9.1.6 Void 306

5.8.9.1.7 Void 306

5.8.9.1.8 Reception of an *RRCReconfigurationFailureSidelink* by the UE 306

5.8.9.1.9 Reception of an *RRCReconfigurationCompleteSidelink* by the UE 306

5.8.9.1a Sidelink radio bearer management 306

5.8.9.1a.1 Sidelink DRB release 306

5.8.9.1a.2 Sidelink DRB addition/modification 308

5.8.9.1a.3 Sidelink SRB release 309

5.8.9.1a.4 Sidelink SRB addition 309

5.8.9.2 Sidelink UE capability transfer 310

5.8.9.2.1 General 310

5.8.9.2.2 Initiation 310

5.8.9.2.3 Actions related to transmission of the *UECapabilityEnquirySidelink* by the UE 310

5.8.9.2.4 Actions related to reception of the *UECapabilityEnquirySidelink* by the UE 310

5.8.9.3 Sidelink radio link failure related actions 311

5.8.9.4 Sidelink common control information 311

5.8.9.4.1 General 311

5.8.9.4.2 Actions related to reception of *MasterInformationBlockSidelink* message 312

5.8.9.4.3 Transmission of *MasterInformationBlockSidelink* message 312

5.8.9.5 Actions related to PC5-RRC connection release requested by upper layers 313

5.8.9.6 Sidelink UE assistance information 313

5.8.9.6.1 General 313

5.8.9.6.2 Initiation 313

5.8.9.6.3 Actions related to reception of *UEAssistanceInformationSidelink* message 314

5.8.9.8 Remote UE information 315

5.8.9.8.1 General 315

5.8.9.8.2 Actions related to transmission of *RemoteUEInformationSidelink* message 315

5.8.9.8.3 Reception of *RemoteUEInformationSidelink* message by the L2 U2N Relay UE 316

5.8.9.9 Uu message transfer in sidelink 317

5.8.9.9.1 General 317

5.8.9.9.2 Actions related to transmission of *UuMessageTransferSidelink* message 317

5.8.9.9.3 Reception of the *UuMessageTransferSidelink* 317

5.8.9.10 Notification Message 318

5.8.9.10.1 General 318

5.8.9.10.2 Initiation 318

5.8.9.10.3 Actions related to transmission of *NotificationMessageSidelink* message 318

5.8.9.10.4 Actions related to reception of *NotificationMessageSidelink* message 318

5.8.10 Sidelink measurement 319

5.8.10.1 Introduction 319

5.8.10.2 Sidelink measurement configuration 319

5.8.10.2.1 General 319

5.8.10.2.2 Sidelink measurement identity removal 320

5.8.10.2.3 Sidelink measurement identity addition/modification 320

5.8.10.2.4 Sidelink measurement object removal 320

5.8.10.2.5 Sidelink measurement object addition/modification 321

5.8.10.2.6 Sidelink reporting configuration removal 321

5.8.10.2.7 Sidelink reporting configuration addition/modification 322

5.8.10.2.8 Sidelink quantity configuration 322

5.8.10.3 Performing NR sidelink measurements 322

5.8.10.3.1 General 322

5.8.10.3.2 Derivation of NR sidelink measurement results 322

5.8.10.4 Sidelink measurement report triggering 323

5.8.10.4.1 General 323

5.8.10.4.2 Event S1 (Serving becomes better than threshold) 324

5.8.10.4.3 Event S2 (Serving becomes worse than threshold) 324

5.8.10.5 Sidelink measurement reporting 325

5.8.10.5.1 General 325

5.8.11 Zone identity calculation 325

5.8.12 DFN derivation from GNSS 326

5.9 MBS Broadcast 332

5.9.1 Introduction 332

5.9.1.1 General 332

5.9.1.2 MCCH scheduling 332

5.9.1.3 MCCH information validity and notification of changes 332

5.9.2 MCCH information acquisition 333

5.9.2.1 General 333

5.9.2.2 Initiation 333

5.9.2.3 MCCH information acquisition by the UE 333

5.9.2.4 Actions upon reception of the MBSBroadcastConfiguration message 333

5.9.3 Broadcast MRB configuration 334

5.9.3.1 General 334

5.9.3.2 Initiation 334

5.9.3.3 Broadcast MRB establishment 334

5.9.3.4 Broadcast MRB release 334

5.9.4 MBS Interest Indication 335

5.9.4.1 General 335

5.9.4.2 Initiation 335

5.9.4.3 MBS frequencies of interest determination 336

5.9.4.4 MBS services of interest determination 336

5.9.4.5 Setting of the contents of MBS Interest Indication 336

6 Protocol data units, formats and parameters (ASN.1) 338

6.1 General 338

6.1.1 Introduction 338

6.1.2 Need codes and conditions for optional fields 338

6.1.3 General rules 341

6.2 RRC messages 341

6.2.1 General message structure 341

– *NR-RRC-Definitions* 341

– *BCCH-BCH-Message* 341

– *BCCH-DL-SCH-Message* 342

– *DL-CCCH-Message* 342

– *DL-DCCH-Message* 343

– *MCCH-Message* 343

– *PCCH-Message* 344

– *UL-CCCH-Message* 344

– *UL-CCCH1-Message* 345

– *UL-DCCH-Message* 345

6.2.2 Message definitions 347

– *CounterCheck* 347

– *CounterCheckResponse* 348

– ***DedicatedSIBRequest*** 349

– *DLDedicatedMessageSegment* 350

– *DLInformationTransfer* 351

– *DLInformationTransferMRDC* 353

– *FailureInformation* 354

– *IABOtherInformation* 355

– *LocationMeasurementIndication* 358

– *LoggedMeasurementConfiguration* 359

– *MBSBroadcastConfiguration* 361

– *MBSInterestIndication* 362

– *MCGFailureInformation* 363

– *MeasurementReport* 365

– *MeasurementReportAppLayer* 366

– *MIB* 367

– *MobilityFromNRCommand* 368

– *Paging* 370

– *RRCReestablishment* 371

– *RRCReestablishmentComplete* 372

– *RRCReestablishmentRequest* 373

– *RRCReconfiguration* 374

– *RRCReconfigurationComplete* 382

– *RRCReject* 383

– *RRCRelease* 384

– *RRCResume* 392

– *RRCResumeComplete* 396

– *RRCResumeRequest* 397

– *RRCResumeRequest1* 398

– *RRCSetup* 399

– *RRCSetupComplete* 400

– *RRCSetupRequest* 402

– ***RRCSystemInfoRequest*** 403

– *SCGFailureInformation* 405

– *SCGFailureInformationEUTRA* 407

– *SecurityModeCommand* 408

– *SecurityModeComplete* 409

– *SecurityModeFailure* 410

– *SIB1* 410

– *SidelinkUEInformationNR* 415

– *SystemInformation* 420

– *UEAssistanceInformation* 422

– *UECapabilityEnquiry* 431

– *UECapabilityInformation* 431

– *UEInformationRequest* 432

– *UEInformationResponse* 434

– *UEPositioningAssistanceInfo* 448

– *ULDedicatedMessageSegment* 450

– *ULInformationTransfer* 451

– *ULInformationTransferIRAT* 452

– *ULInformationTransferMRDC* 453

6.3 RRC information elements 454

6.3.0 Parameterized types 454

– *SetupRelease* 454

6.3.1 System information blocks 454

– *SIB2* 454

– *SIB3* 459

– *SIB4* 461

– *SIB5* 467

– *SIB6* 470

– *SIB7* 470

– *SIB8* 471

– *SIB9* 472

– *SIB10* 473

– *SIB11* 474

– *SIB12* 475

– *SIB13* 478

– *SIB14* 478

– *SIB15* 479

– *SIB16* 480

– *SIB17* 480

– *SIB18* 482

– *SIB20* 484

– *SIB21* 485

6.3.1a Positioning System information blocks 486

– *PosSystemInformation-r16-IEs* 486

– *PosSI-SchedulingInfo* 488

– *SIBpos* 490

6.3.2 Radio resource control information elements 490

– *AdditionalSpectrumEmission* 490

– *Alpha* 490

– *AMF-Identifier* 491

– *ARFCN-ValueEUTRA* 491

– *ARFCN-ValueNR* 491

– *ARFCN-ValueUTRA-FDD* 492

– *AvailabilityCombinationsPerCell* 492

– *AvailabilityIndicator* 494

– *BAP-RoutingID* 494

– *BeamFailureRecoveryConfig* 495

– *BeamFailureRecoveryRSConfig* 498

– *BetaOffsets* 499

– *BetaOffsetsCrossPri* 500

– *BH-LogicalChannelIdentity* 500

– *BH-LogicalChannelIdentity-Ext* 501

– *BH-RLC-ChannelConfig* 501

– *BH-RLC-ChannelID* 502

– *BSR-Config* 502

– *BWP* 503

– *BWP-Downlink* 504

– *BWP-DownlinkCommon* 505

– *BWP-DownlinkDedicated* 505

– *BWP-Id* 508

– *BWP-Uplink* 508

– *BWP-UplinkCommon* 509

– *BWP-UplinkDedicated* 512

– *CandidateBeamRS* 516

– *CellAccessRelatedInfo* 516

– *CellAccessRelatedInfo-EUTRA-5GC* 518

– *CellAccessRelatedInfo-EUTRA-EPC* 518

– *CellGroupConfig* 519

– *CellGroupId* 529

– *CellIdentity* 529

– *CellReselectionPriority* 529

– *CellReselectionSubPriority* 530

– *CFR-ConfigMulticast* 530

– *CGI-InfoEUTRA* 531

– *CGI-InfoEUTRALogging* 531

– *CGI-InfoNR* 532

– *CGI-Info-Logging* 533

– *CLI-RSSI-Range* 534

– *CodebookConfig* 534

– *CommonLocationInfo* 540

– *CondReconfigId* 540

– *CondReconfigToAddModList* 541

– *ConditionalReconfiguration* 542

– *ConfiguredGrantConfig* 543

– *ConfiguredGrantConfigIndex* 552

– *ConfiguredGrantConfigIndexMAC* 553

– *ConnEstFailureControl* 553

– *ControlResourceSet* 554

– *ControlResourceSetId* 556

– *ControlResourceSetZero* 556

– *CrossCarrierSchedulingConfig* 557

– *CSI-AperiodicTriggerStateList* 558

– *CSI-FrequencyOccupation* 561

– *CSI-IM-Resource* 561

– *CSI-IM-ResourceId* 562

– *CSI-IM-ResourceSet* 563

– *CSI-IM-ResourceSetId* 563

– *CSI-MeasConfig* 563

– *CSI-ReportConfig* 565

– *CSI-ReportConfigId* 572

– *CSI-ResourceConfig* 573

– *CSI-ResourceConfigId* 574

– *CSI-ResourcePeriodicityAndOffset* 575

– *CSI-RS-ResourceConfigMobility* 575

– *CSI-RS-ResourceMapping* 578

– *CSI-SemiPersistentOnPUSCH-TriggerStateList* 579

– *CSI-SSB-ResourceSet* 580

– *CSI-SSB-ResourceSetId* 581

– *DedicatedNAS-Message* 581

– *DL-PPW-PreConfig* 581

– *DMRS-BundlingPUCCH-Config* 584

– *DMRS-BundlingPUSCH-Config* 585

– *DMRS-DownlinkConfig* 586

– *DMRS-UplinkConfig* 587

– *DownlinkConfigCommon* 589

– *DownlinkConfigCommonSIB* 590

– *DownlinkPreemption* 594

– *DRB-Identity* 595

– *DRX-Config* 595

– *DRX-ConfigSecondaryGroup* 597

– *DRX-ConfigSL* 598

– *EphemerisInfo* 599

– *FeatureCombination* 600

– *FeatureCombinationPreambles* 601

– *FilterCoefficient* 604

– *FreqBandIndicatorNR* 604

– *FreqPriorityListDedicatedSlicing* 604

– *FreqPriorityListSlicing* 605

– *FrequencyInfoDL* 606

– *FrequencyInfoDL-SIB* 607

– *FrequencyInfoUL* 608

– *FrequencyInfoUL-SIB* 609

– *GapPriority* 610

– *HighSpeedConfig* 611

– *Hysteresis* 612

– *HysteresisLocation* 613

– *InvalidSymbolPattern* 613

– *I-RNTI-Value* 614

– *LBT-FailureRecoveryConfig* 614

– *LocationInfo* 615

– *LocationMeasurementInfo* 615

– *LogicalChannelConfig* 617

– *LogicalChannelIdentity* 620

– *LTE-NeighCellsCRS-AssistInfoList* 620

– *MAC-CellGroupConfig* 622

– *MeasConfig* 626

– *MeasGapConfig* 627

– *MeasGapId* 631

– *MeasGapSharingConfig* 632

– *MeasId* 633

– *MeasIdleConfig* 633

– *MeasIdToAddModList* 637

– *MeasObjectCLI* 637

– *MeasObjectEUTRA* 640

– *MeasObjectId* 642

– *MeasObjectNR* 642

– *MeasObjectNR-SL* 650

– *MeasObjectRxTxDiff* 650

– *MeasObjectToAddModList* 651

– *MeasObjectUTRA-FDD* 651

– *MeasResultCellListSFTD-NR* 652

– *MeasResultCellListSFTD-EUTRA* 653

– *MeasResults* 654

– *MeasResult2EUTRA* 660

– *MeasResult2NR* 660

– *MeasResultIdleEUTRA* 661

– *MeasResultIdleNR* 662

– *MeasResultRxTxTimeDiff* 663

– *MeasResultSCG-Failure* 664

– *MeasResultsSL* 664

– *MeasTriggerQuantityEUTRA* 665

– *MobilityStateParameters* 666

– *MRB-Identity* 666

– *MsgA-ConfigCommon* 667

– *MsgA-PUSCH-Config* 667

– *MultiFrequencyBandListNR* 671

– *MultiFrequencyBandListNR-SIB* 672

– *MUSIM-GapConfig* 672

– *MUSIM-GapId* 673

– *MUSIM-GapInfo* 674

– *NeedForGapsConfigNR* 675

– *NeedForGapNCSG-ConfigEUTRA* 677

– *NeedForGapNCSG-ConfigNR* 677

– *NeedForGapNCSG-InfoEUTRA* 678

– *NeedForGapNCSG-InfoNR* 679

– *NextHopChainingCount* 680

– *NG-5G-S-TMSI* 681

– *NonCellDefiningSSB* 681

– *NPN-Identity* 682

– *NPN-IdentityInfoList* 683

– *NR-DL-PRS-PDC-Info* 684

– *NR-NS-PmaxList* 688

– *NSAG-ID* 688

– *NSAG-IdentityInfo* 688

– *NTN-Config* 689

– *NZP-CSI-RS-Resource* 691

– *NZP-CSI-RS-ResourceId* 692

– *NZP-CSI-RS-ResourceSet* 692

– *NZP-CSI-RS-ResourceSetId* 694

– *P-Max* 695

– *PathlossReferenceRS* 695

– *PathlossReferenceRS-Id* 696

– *PCI-ARFCN-EUTRA* 696

– *PCI-ARFCN-NR* 696

– *PCI-List* 697

– *PCI-Range* 697

– *PCI-RangeElement* 698

– *PCI-RangeIndex* 698

– *PCI-RangeIndexList* 699

– *PDCCH-Config* 699

– *PDCCH-ConfigCommon* 702

– *PDCCH-ConfigSIB1* 705

– *PDCCH-ServingCellConfig* 706

– *PDCP-Config* 707

– *PDSCH-Config* 713

– *PDSCH-ConfigCommon* 720

– *PDSCH-ServingCellConfig* 720

– *PDSCH-TimeDomainResourceAllocationList* 722

– *PHR-Config* 724

– *PhysCellId* 726

– *PhysicalCellGroupConfig* 727

– *PLMN-Identity* 734

– *PLMN-IdentityInfoList* 735

– *PLMN-IdentityList2* 736

– *PRB-Id* 736

– *PTRS-DownlinkConfig* 737

– *PTRS-UplinkConfig* 737

– *PUCCH-Config* 739

– *PUCCH-ConfigCommon* 748

– *PUCCH-ConfigurationList* 749

– *PUCCH-PathlossReferenceRS-Id* 750

– *PUCCH-PowerControl* 750

– *PUCCH-SpatialRelationInfo* 752

– *PUCCH-SpatialRelationInfo-Id* 753

– *PUCCH-TPC-CommandConfig* 753

– *PUSCH-Config* 754

– *PUSCH-ConfigCommon* 762

– *PUSCH-PowerControl* 762

– *PUSCH-ServingCellConfig* 767

– *PUSCH-TimeDomainResourceAllocationList* 768

– *PUSCH-TPC-CommandConfig* 771

– *Q-OffsetRange* 772

– *Q-QualMin* 772

– *Q-RxLevMin* 773

– *QuantityConfig* 773

– *RACH-ConfigCommon* 775

– *RACH-ConfigCommonTwoStepRA* 778

– *RACH-ConfigDedicated* 782

– *RACH-ConfigGeneric* 785

– *RACH-ConfigGenericTwoStepRA* 787

– *RA-Prioritization* 790

– *RA-PrioritizationForSlicing* 791

– *RadioBearerConfig* 791

– *RadioLinkMonitoringConfig* 795

– *RadioLinkMonitoringRS-Id* 797

– *RAN-AreaCode* 798

– *RateMatchPattern* 798

– *RateMatchPatternId* 800

– *RateMatchPatternLTE-CRS* 801

– *ReferenceLocation* 802

– *ReferenceTimeInfo* 802

– *RejectWaitTime* 803

– *RepetitionSchemeConfig* 804

– *ReportConfigId* 805

– *ReportConfigInterRAT* 805

– *ReportConfigNR* 810

– *ReportConfigNR-SL* 820

– *ReportConfigToAddModList* 822

– *ReportInterval* 822

– *ReselectionThreshold* 822

– *ReselectionThresholdQ* 823

– *ResumeCause* 823

– *RLC-BearerConfig* 823

– *RLC-Config* 825

– *RLF-TimersAndConstants* 829

– *RNTI-Value* 829

– *RSRP-Range* 830

– *RSRQ-Range* 830

– *RSSI-Range* 830

– *RxTxTimeDiff* 831

– *SCellActivationRS-Config* 831

– *SCellActivationRS-ConfigId* 832

– *SCellIndex* 832

– *SchedulingRequestConfig* 833

– *SchedulingRequestId* 834

– *SchedulingRequestResourceConfig* 834

– *SchedulingRequestResourceId* 836

– *ScramblingId* 836

– *SCS-SpecificCarrier* 837

– *SDAP-Config* 838

– *SearchSpace* 839

– *SearchSpaceId* 846

– *SearchSpaceZero* 847

– *SecurityAlgorithmConfig* 847

– *SemiStaticChannelAccessConfig* 848

– *SemiStaticChannelAccessConfigUE* 848

– *Sensor-LocationInfo* 849

– *ServingCellAndBWP-Id* 850

– *ServCellIndex* 850

– *ServingCellConfig* 850

– *ServingCellConfigCommon* 862

– *ServingCellConfigCommonSIB* 865

– *ShortI-RNTI-Value* 868

– *ShortMAC-I* 868

– *SINR-Range* 868

– *SI-RequestConfig* 869

– *SI-SchedulingInfo* 870

– *SK-Counter* 873

– *SlotFormatCombinationsPerCell* 874

– *SlotFormatIndicator* 875

– *S-NSSAI* 878

– *SpeedStateScaleFactors* 879

– *SPS-Config* 879

– *SPS-ConfigIndex* 882

– *SPS-PUCCH-AN* 882

– *SPS-PUCCH-AN-List* 882

– *SRB-Identity* 883

– *SRS-CarrierSwitching* 883

– *SRS-Config* 884

– *SRS-RSRP-Range* 897

– *SRS-TPC-CommandConfig* 898

– *SSB-Index* 898

– *SSB-MTC* 899

– *SSB-PositionQCL-Relation* 901

– *SSB-ToMeasure* 901

– *SS-RSSI-Measurement* 902

– *SubcarrierSpacing* 903

– *TAG-Config* 903

– *TAR-Config* 904

– *TCI-ActivatedConfig* 904

– *TCI-State* 905

– *TCI-StateId* 907

– *TCI-UL-State* 907

– *TCI-UL-StateId* 908

– *TDD-UL-DL-ConfigCommon* 908

– *TDD-UL-DL-ConfigDedicated* 910

– *TrackingAreaCode* 912

– *T-Reselection* 912

– *TimeAlignmentTimer* 913

– *TimeToTrigger* 913

– *UAC-BarringInfoSetIndex* 913

– *UAC-BarringInfoSetList* 914

– *UAC-BarringPerCatList* 915

– *UAC-BarringPerPLMN-List* 916

– *UE-TimersAndConstants* 916

– *UE-TimersAndConstantsRemoteUE* 917

– *UL-DelayValueConfig* 917

– *UL-ExcessDelayConfig* 918

– *UL-GapFR2-Config* 918

– *UplinkCancellation* 919

– *UplinkConfigCommon* 921

– *UplinkConfigCommonSIB* 922

– *Uplink-PowerControl* 923

– *Uu-RelayRLC-ChannelConfig* 924

– *Uu-RelayRLC-ChannelID* 924

– *UplinkTxDirectCurrentList* 925

– *UplinkTxDirectCurrentMoreCarrierList* 926

– *UplinkTxDirectCurrentTwoCarrierList* 928

– *ZP-CSI-RS-Resource* 929

– *ZP-CSI-RS-ResourceSet* 930

– *ZP-CSI-RS-ResourceSetId* 931

6.3.3 UE capability information elements 931

– *AccessStratumRelease* 931

– *AppLayerMeasParameters* 931

– *BandCombinationList* 932

– *BandCombinationListSidelinkEUTRA-NR* 940

– *BandCombinationListSL-Discovery* 941

– *CA-BandwidthClassEUTRA* 942

– *CA-BandwidthClassNR* 942

– *CA-ParametersEUTRA* 943

– *CA-ParametersNR* 943

– *CA-ParametersNRDC* 952

– *CarrierAggregationVariant* 954

– *CodebookParameters* 954

– *FeatureSetCombination* 962

– *FeatureSetCombinationId* 964

– *FeatureSetDownlink* 964

– *FeatureSetDownlinkId* 969

– *FeatureSetDownlinkPerCC* 970

– *FeatureSetDownlinkPerCC-Id* 971

– *FeatureSetEUTRA-DownlinkId* 971

– *FeatureSetEUTRA-UplinkId* 972

– *FeatureSets* 972

– *FeatureSetUplink* 973

– *FeatureSetUplinkId* 979

– *FeatureSetUplinkPerCC* 979

– *FeatureSetUplinkPerCC-Id* 980

– *FreqBandIndicatorEUTRA* 980

– *FreqBandList* 981

– *FreqSeparationClass* 981

– *FreqSeparationClassDL-Only* 982

– *FR2-2-AccessParamsPerBand* 982

– *HighSpeedParameters* 984

– *IMS-Parameters* 984

– *InterRAT-Parameters* 985

– *MAC-Parameters* 986

– *MeasAndMobParameters* 989

– *MeasAndMobParametersMRDC* 992

– *MIMO-Layers* 994

– *MIMO-ParametersPerBand* 994

– *ModulationOrder* 1005

– *MRDC-Parameters* 1005

– *NRDC-Parameters* 1007

– *NTN-Parameters* 1008

– *OLPC-SRS-Pos* 1008

– *PDCP-Parameters* 1009

– *PDCP-ParametersMRDC* 1010

– *Phy-Parameters* 1010

– *Phy-ParametersMRDC* 1018

– *Phy-ParametersSharedSpectrumChAccess* 1019

– *PosSRS-RRC-Inactive-OutsideInitialUL-BWP* 1020

– *PowSav-Parameters* 1021

– *ProcessingParameters* 1021

– *PRS-ProcessingCapabilityOutsideMGinPPWperType* 1022

– *RAT-Type* 1023

– *RedCapParameters* 1023

– *RF-Parameters* 1024

– *RF-ParametersMRDC* 1033

– *RLC-Parameters* 1035

– *SDAP-Parameters* 1036

– *SidelinkParameters* 1036

– *SimultaneousRxTxPerBandPair* 1040

– *SON-Parameters* 1041

– *SpatialRelationsSRS-Pos* 1041

– *SRS-AllPosResourcesRRC-Inactive* 1042

– *SRS-SwitchingTimeNR* 1042

– *SRS-SwitchingTimeEUTRA* 1043

– *SupportedBandwidth* 1043

– *UE-BasedPerfMeas-Parameters* 1044

– *UE-CapabilityRAT-ContainerList* 1044

– *UE-CapabilityRAT-RequestList* 1045

– *UE-CapabilityRequestFilterCommon* 1045

– *UE-CapabilityRequestFilterNR* 1048

– *UE-MRDC-Capability* 1048

– *UE-NR-Capability* 1050

– *UE-RadioPagingInfo* 1054

– *SharedSpectrumChAccessParamsPerBand* 1055

6.3.4 Other information elements 1057

– *AbsoluteTimeInfo* 1057

– *AreaConfiguration* 1059

– ***BT-NameList*** 1060

– *DedicatedInfoF1c* 1061

– *EUTRA-AllowedMeasBandwidth* 1061

– *EUTRA-MBSFN-SubframeConfigList* 1062

– *EUTRA-MultiBandInfoList* 1063

– *EUTRA-NS-PmaxList* 1063

– *EUTRA-PhysCellId* 1063

– *EUTRA-PhysCellIdRange* 1064

– *EUTRA-PresenceAntennaPort1* 1064

– *EUTRA-Q-OffsetRange* 1065

– *IAB-IP-Address* 1065

– *IAB-IP-AddressIndex* 1066

– *IAB-IP-Usage* 1066

– *LoggingDuration* 1066

– *LoggingInterval* 1067

– *LogMeasResultListBT* 1067

– *LogMeasResultListWLAN* 1068

– *MeasConfigAppLayerId* 1069

– *OtherConfig* 1069

– *PhysCellIdUTRA-FDD* 1075

– *RRC-TransactionIdentifier* 1075

– ***Sensor-NameList*** 1076

– *TraceReference* 1076

– *UE-MeasurementsAvailable* 1077

– *UTRA-FDD-Q-OffsetRange* 1077

– *VisitedCellInfoList* 1078

– ***WLAN-NameList*** 1079

6.3.5 Sidelink information elements 1079

– *SL-BWP-Config* 1079

– *SL-BWP-ConfigCommon* 1081

– *SL-BWP-DiscPoolConfig* 1082

– *SL-BWP-DiscPoolConfigCommon* 1082

– *SL-BWP-PoolConfig* 1083

– *SL-BWP-PoolConfigCommon* 1084

– *SL-CBR-PriorityTxConfigList* 1085

– *SL-CBR-CommonTxConfigList* 1086

– *SL-ConfigDedicatedNR* 1087

– *SL-ConfiguredGrantConfig* 1090

– *SL-DestinationIdentity* 1091

– *SL-DRX-Config* 1092

– *SL-DRX-ConfigGC-BC* 1093

– *SL-DRX-ConfigUC* 1094

– *SL-DRX-ConfigUC-SemiStatic* 1096

– *SL-FreqConfig* 1097

– *SL-FreqConfigCommon* 1098

– *SL-InterUE-CoordinationConfig* 1099

– *SL-LogicalChannelConfig* 1102

– *SL-L2RelayUE-Config* 1104

– *SL-L2RemoteUE-Config* 1105

– *SL-MeasConfigCommon* 1106

– *SL-MeasConfigInfo* 1106

– *SL-MeasIdList* 1107

– *SL-MeasObjectList* 1108

– *SL-PagingIdentityRemoteUE* 1109

– *SL-PBPS-CPS-Config* 1109

– *SL-PDCP-Config* 1112

– *SL-PSSCH-TxConfigList* 1113

– *SL-QoS-FlowIdentity* 1114

– *SL-QoS-Profile* 1115

– *SL-QuantityConfig* 1116

– *SL-RadioBearerConfig* 1117

– *SL-RemoteUE-Config* 1118

– *SL-ReportConfigList* 1119

– *SL-ResourcePool* 1121

– *SL-RLC-BearerConfig* 1130

– *SL-RLC-BearerConfigIndex* 1131

– *SL-RLC-ChannelConfig* 1131

– *SL-RLC-ChannelID* 1132

– *SL-RLC-Config* 1132

– *SL-ScheduledConfig* 1133

– *SL-SDAP-Config* 1135

– *SL-ServingCellInfo* 1136

– *SL-SourceIdentity* 1137

– *SL-SRAP-Config* 1137

– *SL-SyncConfig* 1138

– *SL-Thres-RSRP-List* 1140

– *SL-TxPower* 1140

– *SL-TypeTxSync* 1140

– *SL-UE-SelectedConfig* 1141

– *SL-ZoneConfig* 1141

– *SLRB-Uu-ConfigIndex* 1142

6.3.6 MBS information elements 1142

– *CarrierFreqListMBS* 1142

– *CFR-ConfigMCCH-MTCH* 1143

– *DRX-ConfigPTM* 1144

– *MBS-NeighbourCellList* 1145

– *MBS-ServiceList* 1146

– *MBS-SessionInfoList* 1146

– *MTCH-SSB-MappingWindowList* 1149

– *PDSCH-ConfigBroadcast* 1149

– *TMGI* 1151

6.4 RRC multiplicity and type constraint values 1151

– Multiplicity and type constraint definitions 1151

– End of NR-RRC-Definitions 1159

6.5 Short Message 1159

6.6 PC5 RRC messages 1160

6.6.1 General message structure 1160

– *PC5-RRC-Definitions* 1160

– *SBCCH-SL-BCH-Message* 1161

– *SCCH-Message* 1161

– *MasterInformationBlockSidelink* 1162

– *MeasurementReportSidelink* 1163

– *NotificationMessageSidelink* 1164

– *RemoteUEInformationSidelink* 1165

– *RRCReconfigurationSidelink* 1166

– *RRCReconfigurationCompleteSidelink* 1169

– *RRCReconfigurationFailureSidelink* 1170

– *UEAssistanceInformationSidelink* 1171

– *UECapabilityEnquirySidelink* 1172

– *UECapabilityInformationSidelink* 1173

– *UuMessageTransferSidelink* 1175

– *End of PC5-RRC-Definitions* 1176

7 Variables and constants 1177

7.1 Timers 1177

7.1.1 Timers (Informative) 1177

7.1.2 Timer handling 1186

7.2 Counters 1187

7.3 Constants 1187

7.4 UE variables 1187

– *NR-UE-Variables* 1187

– *VarConditionalReconfig* 1189

– *VarConnEstFailReport* 1189

– *VarConnEstFailReportList* 1190

– *VarLogMeasConfig* 1190

– *VarLogMeasReport* 1191

– *VarMeasConfig* 1191

– *VarMeasConfigSL* 1192

– *VarMeasIdleConfig* 1192

– *VarMeasIdleReport* 1193

– *VarMeasReportList* 1193

– *VarMeasReportListSL* 1194

– *VarMobilityHistoryReport* 1194

– *VarPendingRNA-Update* 1195

– *VarRA-Report* 1195

– *VarResumeMAC-Input* 1195

– *VarRLF-Report* 1196

– *VarShortMAC-Input* 1196

– *VarSuccessHO-Report* 1197

– End of *NR-UE-Variables* 1197

8 Protocol data unit abstract syntax 1199

8.1 General 1199

8.2 Structure of encoded RRC messages 1199

8.3 Basic production 1199

8.4 Extension 1199

8.5 Padding 1200

9 Specified and default radio configurations 1200

9.1 Specified configurations 1200

9.1.1 Logical channel configurations 1200

9.1.1.1 BCCH configuration 1200

9.1.1.2 CCCH configuration 1201

9.1.1.3 PCCH configuration 1201

9.1.1.4 SCCH configuration 1201

9.1.1.5 STCH configuration 1204

9.1.1.6 MCCH configuration 1204

9.1.1.7 MTCH configuration for MBS broadcast 1205

9.1.2 Void 1205

9.2 Default radio configurations 1205

9.2.1 Default SRB configurations 1205

9.2.2 Default MAC Cell Group configuration 1205

9.2.3 Default values timers and constants 1206

9.2.4 Default PC5 Relay RLC Channel 1206

9.2.5 Default SRAP configurations 1206

9.3 Sidelink pre-configured parameters 1207

– *NR-Sidelink-Preconf* 1207

– *SL-PreconfigurationNR* 1207

– *End of NR-Sidelink-Preconf* 1209

– *SL-AccessInfo-L2U2N* 1209

10 Generic error handling 1211

10.1 General 1211

10.2 ASN.1 violation or encoding error 1211

10.3 Field set to a not comprehended value 1211

10.4 Mandatory field missing 1211

10.5 Not comprehended field 1213

11 Radio information related interactions between network nodes 1214

11.1 General 1214

11.2 Inter-node RRC messages 1214

11.2.1 General 1214

11.2.2 Message definitions 1216

– *CG-CandidateList* 1216

– *HandoverCommand* 1217

– *HandoverPreparationInformation* 1218

– *CG-Config* 1222

– *CG-ConfigInfo* 1230

– *MeasurementTimingConfiguration* 1242

– *UERadioPagingInformation* 1244

– *UERadioAccessCapabilityInformation* 1246

11.2.3 Mandatory information in inter-node RRC messages 1246

11.3 Inter-node RRC information element definitions 1248

11.4 Inter-node RRC multiplicity and type constraint values 1248

– Multiplicity and type constraints definitions 1248

– *End of NR-InterNodeDefinitions* 1248

12 Processing delay requirements for RRC procedures 1249

Annex A (informative): Guidelines, mainly on use of ASN.1 1253

A.1 Introduction 1253

A.2 Procedural specification 1254

A.2.1 General principles 1254

A.2.2 More detailed aspects 1254

A.3 PDU specification 1254

A.3.1 General principles 1254

A.3.1.1 ASN.1 clauses 1254

A.3.1.2 ASN.1 identifier naming conventions 1255

A.3.1.3 Text references using ASN.1 identifiers 1257

A.3.2 High-level message structure 1258

A.3.3 Message definition 1259

A.3.4 Information elements 1261

A.3.5 Fields with optional presence 1262

A.3.6 Fields with conditional presence 1263

A.3.7 Guidelines on use of lists with elements of SEQUENCE type 1264

A.3.8 Guidelines on use of parameterised SetupRelease type 1264

A.3.9 Guidelines on use of ToAddModList and ToReleaseList 1266

A.3.10 Guidelines on use of lists (without ToAddModList and ToReleaseList) 1267

A.4 Extension of the PDU specifications 1268

A.4.1 General principles to ensure compatibility 1268

A.4.2 Critical extension of messages and fields 1268

A.4.3 Non-critical extension of messages 1271

A.4.3.1 General principles 1271

A.4.3.2 Further guidelines 1272

A.4.3.3 Typical example of evolution of IE with local extensions 1273

A.4.3.4 Typical examples of non critical extension at the end of a message 1274

A.4.3.5 Examples of non-critical extensions not placed at the default extension location 1275

– *ParentIE-WithEM* 1275

– *ChildIE1-WithoutEM* 1275

– *ChildIE2-WithoutEM* 1276

A.5 Guidelines regarding inclusion of transaction identifiers in RRC messages 1280

A.6 Guidelines regarding use of need codes 1281

A.7 Guidelines regarding use of conditions 1281

A.8 Miscellaneous 1282

Annex B (informative): RRC Information 1283

B.1 Protection of RRC messages 1283

B.2 Description of BWP configuration options 1285

Annex C (normative): List of CRs Containing Early Implementable Features and Corrections 1287

Annex D (normative): UE requirements on ASN.1 comprehension 1291

Annex E (informative): Change history 1293

# Foreword

This Technical Specification has been produced by the 3<sup>rd</sup> Generation Partnership Project (3GPP).

The contents of the present document are subject to continuing work within the TSG and may change following formal TSG approval. Should the TSG modify the contents of the present document, it will be re-released by the TSG with an identifying change of release date and an increase in version number as follows:

Version x.y.z

where:

x the first digit:

1 presented to TSG for information;

2 presented to TSG for approval;

3 or greater indicates TSG approved document under change control.

y the second digit is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc.

z the third digit is incremented when editorial only changes have been incorporated in the document.
