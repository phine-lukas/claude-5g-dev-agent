# A.3 Nmbsmf_MBSSession API

openapi: 3.0.0

info:

title: 'Nmbsmf-MBSSession'

version: 1.2.1

description: \|

MB-SMF MBSSession Service.

© 2025, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC).

All rights reserved.

externalDocs:

description: \>

3GPP TS 29.532 V18.6.0; 5G System; 5G Multicast-Broadcast Session Management Services;

Stage 3.

url: https://www.3gpp.org/ftp/Specs/archive/29_series/29.532/

servers:

\- url: '{apiRoot}/nmbsmf-mbssession/v1'

variables:

apiRoot:

default: https://example.com

description: apiRoot as defined in clause 4.4 of 3GPP TS 29.501

security:

\- {}

\- oAuth2ClientCredentials:

\- nmbsmf-mbssession

paths:

/mbs-sessions:

post:

summary: Create

tags:

\- MBS sessions collection

operationId: Create

security:

\- {}

\- oAuth2ClientCredentials:

\- nmbsmf-mbssession

\- oAuth2ClientCredentials:

\- nmbsmf-mbssession

\- nmbsmf-mbssession:mbs-sessions

requestBody:

description: \>

Representation of the MBS session to be created in the MB-SMF

Creates an individual MBS session resource in the MB-SMF.

required: true

content:

application/json:

schema:

\$ref: '#/components/schemas/CreateReqData'

responses:

'201':

description: \>

Successful creation of an MBS session

content:

application/json:

schema:

\$ref: '#/components/schemas/CreateRspData'

headers:

Location:

description: \>

'Contains the URI of the newly created resource, according to the structure:

{apiRoot}/nmbsmf-mbssession/\<apiVersion\>/mbs-sessions/{mbsSessionRef}'

required: true

schema:

type: string

'307':

\$ref: 'TS29571_CommonData.yaml#/components/responses/307'

'308':

\$ref: 'TS29571_CommonData.yaml#/components/responses/308'

'400':

\$ref: 'TS29571_CommonData.yaml#/components/responses/400'

'401':

\$ref: 'TS29571_CommonData.yaml#/components/responses/401'

'403':

description: Forbidden.

content:

application/problem+json:

schema:

\$ref: '#/components/schemas/ExtProblemDetails'

'404':

\$ref: 'TS29571_CommonData.yaml#/components/responses/404'

'411':

\$ref: 'TS29571_CommonData.yaml#/components/responses/411'

'413':

\$ref: 'TS29571_CommonData.yaml#/components/responses/413'

'415':

\$ref: 'TS29571_CommonData.yaml#/components/responses/415'

'429':

\$ref: 'TS29571_CommonData.yaml#/components/responses/429'

'500':

\$ref: 'TS29571_CommonData.yaml#/components/responses/500'

'502':

\$ref: 'TS29571_CommonData.yaml#/components/responses/502'

'503':

\$ref: 'TS29571_CommonData.yaml#/components/responses/503'

default:

\$ref: 'TS29571_CommonData.yaml#/components/responses/default'

/mbs-sessions/{mbsSessionRef}:

patch:

summary: Updates an individual MBS session resource in the MB-SMF.

tags:

\- Individual MBS session

operationId: Update

security:

\- {}

\- oAuth2ClientCredentials:

\- nmbsmf-mbssession

\- oAuth2ClientCredentials:

\- nmbsmf-mbssession

\- nmbsmf-mbssession:mbs-sessions

parameters:

\- name: mbsSessionRef

in: path

required: true

description: Unique ID of the MBS session to be modified

schema:

type: string

requestBody:

description: Data within the Update Request

required: true

content:

application/json-patch+json:

schema:

type: array

items:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/PatchItem'

minItems: 1

responses:

'204':

description: \>

Successful modification of the MBS session without content in the response.

'200':

description: \>

Successful modification of the MBS session with content in the response

content:

application/json:

schema:

\$ref: '#/components/schemas/UpdateRspData'

'307':

\$ref: 'TS29571_CommonData.yaml#/components/responses/307'

'308':

\$ref: 'TS29571_CommonData.yaml#/components/responses/308'

'400':

\$ref: 'TS29571_CommonData.yaml#/components/responses/400'

'401':

\$ref: 'TS29571_CommonData.yaml#/components/responses/401'

'403':

description: Forbidden.

content:

application/problem+json:

schema:

\$ref: '#/components/schemas/ExtProblemDetails'

'404':

\$ref: 'TS29571_CommonData.yaml#/components/responses/404'

'411':

\$ref: 'TS29571_CommonData.yaml#/components/responses/411'

'413':

\$ref: 'TS29571_CommonData.yaml#/components/responses/413'

'415':

\$ref: 'TS29571_CommonData.yaml#/components/responses/415'

'429':

\$ref: 'TS29571_CommonData.yaml#/components/responses/429'

'500':

\$ref: 'TS29571_CommonData.yaml#/components/responses/500'

'502':

\$ref: 'TS29571_CommonData.yaml#/components/responses/502'

'503':

\$ref: 'TS29571_CommonData.yaml#/components/responses/503'

default:

\$ref: 'TS29571_CommonData.yaml#/components/responses/default'

delete:

summary: Deletes an individual MBS session resource in the MB-SMF.

tags:

\- Individual MBS session

operationId: Release

security:

\- {}

\- oAuth2ClientCredentials:

\- nmbsmf-mbssession

\- oAuth2ClientCredentials:

\- nmbsmf-mbssession

\- nmbsmf-mbssession:mbs-sessions

parameters:

\- name: mbsSessionRef

in: path

required: true

description: Unique ID of the MBS session to be released

schema:

type: string

responses:

'204':

description: \>

Successful release of the MBS session without content in the response.

'307':

\$ref: 'TS29571_CommonData.yaml#/components/responses/307'

'308':

\$ref: 'TS29571_CommonData.yaml#/components/responses/308'

'400':

\$ref: 'TS29571_CommonData.yaml#/components/responses/400'

'401':

\$ref: 'TS29571_CommonData.yaml#/components/responses/401'

'403':

\$ref: 'TS29571_CommonData.yaml#/components/responses/403'

'404':

\$ref: 'TS29571_CommonData.yaml#/components/responses/404'

'429':

\$ref: 'TS29571_CommonData.yaml#/components/responses/429'

'500':

\$ref: 'TS29571_CommonData.yaml#/components/responses/500'

'502':

\$ref: 'TS29571_CommonData.yaml#/components/responses/502'

'503':

\$ref: 'TS29571_CommonData.yaml#/components/responses/503'

default:

\$ref: 'TS29571_CommonData.yaml#/components/responses/default'

/mbs-sessions/contexts/update:

post:

summary: ContextUpdate

tags:

\- MBS sessions collection

operationId: ContextUpdate

security:

\- {}

\- oAuth2ClientCredentials:

\- nmbsmf-mbssession

\- oAuth2ClientCredentials:

\- nmbsmf-mbssession

\- nmbsmf-mbssession:mbs-contexts

requestBody:

description: Data within the ContextUpdate Request

required: true

content:

application/json: \# message without binary body part

schema:

\$ref: '#/components/schemas/ContextUpdateReqData'

multipart/related: \# message with binary body part

schema:

type: object

properties: \# Request parts

jsonData:

\$ref: '#/components/schemas/ContextUpdateReqData'

binaryDataN2Information:

type: string

format: binary

encoding:

jsonData:

contentType: application/json

binaryDataN2Information:

contentType: application/vnd.3gpp.ngap

headers:

Content-Id:

schema:

type: string

responses:

'200':

description: Successful response with content in the response

content:

application/json: \# message without binary body part

schema:

\$ref: '#/components/schemas/ContextUpdateRspData'

multipart/related: \# message with binary body part

schema:

type: object

properties:

jsonData:

\$ref: '#/components/schemas/ContextUpdateRspData'

binaryDataN2Information:

type: string

format: binary

encoding:

jsonData:

contentType: application/json

binaryDataN2Information:

contentType: application/vnd.3gpp.ngap

headers:

Content-Id:

schema:

type: string

'204':

description: Successful response without content in the response

'307':

\$ref: 'TS29571_CommonData.yaml#/components/responses/307'

'308':

\$ref: 'TS29571_CommonData.yaml#/components/responses/308'

'400':

\$ref: 'TS29571_CommonData.yaml#/components/responses/400'

'401':

\$ref: 'TS29571_CommonData.yaml#/components/responses/401'

'403':

\$ref: 'TS29571_CommonData.yaml#/components/responses/403'

'404':

\$ref: 'TS29571_CommonData.yaml#/components/responses/404'

'411':

\$ref: 'TS29571_CommonData.yaml#/components/responses/411'

'413':

\$ref: 'TS29571_CommonData.yaml#/components/responses/413'

'415':

\$ref: 'TS29571_CommonData.yaml#/components/responses/415'

'429':

\$ref: 'TS29571_CommonData.yaml#/components/responses/429'

'500':

\$ref: 'TS29571_CommonData.yaml#/components/responses/500'

'502':

\$ref: 'TS29571_CommonData.yaml#/components/responses/502'

'503':

\$ref: 'TS29571_CommonData.yaml#/components/responses/503'

default:

\$ref: 'TS29571_CommonData.yaml#/components/responses/default'

/mbs-sessions/subscriptions:

post:

summary: StatusSubscribe creating a subscription

tags:

\- Subscriptions collection for MBS sessions

operationId: StatusSubscribe

security:

\- {}

\- oAuth2ClientCredentials:

\- nmbsmf-mbssession

\- oAuth2ClientCredentials:

\- nmbsmf-mbssession

\- nmbsmf-mbssession:mbs-sessions

requestBody:

description: Data within the StatusSubscribe Request

required: true

content:

application/json:

schema:

\$ref: '#/components/schemas/StatusSubscribeReqData'

responses:

'201':

description: Data within a successful StatusSubscribe Response

content:

application/json:

schema:

\$ref: '#/components/schemas/StatusSubscribeRspData'

'204':

description: Successful response without content in the response

'307':

\$ref: 'TS29571_CommonData.yaml#/components/responses/307'

'308':

\$ref: 'TS29571_CommonData.yaml#/components/responses/308'

'400':

\$ref: 'TS29571_CommonData.yaml#/components/responses/400'

'401':

\$ref: 'TS29571_CommonData.yaml#/components/responses/401'

'403':

\$ref: 'TS29571_CommonData.yaml#/components/responses/403'

'404':

\$ref: 'TS29571_CommonData.yaml#/components/responses/404'

'411':

\$ref: 'TS29571_CommonData.yaml#/components/responses/411'

'413':

\$ref: 'TS29571_CommonData.yaml#/components/responses/413'

'415':

\$ref: 'TS29571_CommonData.yaml#/components/responses/415'

'429':

\$ref: 'TS29571_CommonData.yaml#/components/responses/429'

'500':

\$ref: 'TS29571_CommonData.yaml#/components/responses/500'

'502':

\$ref: 'TS29571_CommonData.yaml#/components/responses/502'

'503':

\$ref: 'TS29571_CommonData.yaml#/components/responses/503'

default:

\$ref: 'TS29571_CommonData.yaml#/components/responses/default'

callbacks:

statusNotification:

'{\$request.body#/notifUri}':

post:

parameters:

\- name: Content-Encoding

in: header

description: Content-Encoding, described in IETF RFC 9110

schema:

type: string

requestBody:

description: Notification Content

content:

application/json:

schema:

\$ref: '#/components/schemas/StatusNotifyReqData'

responses:

'204':

description: Expected response to a successful callback processing

headers:

Accept-Encoding:

description: Accept-Encoding, described in IETF RFC 9110

schema:

type: string

'307':

\$ref: 'TS29571_CommonData.yaml#/components/responses/307'

'308':

\$ref: 'TS29571_CommonData.yaml#/components/responses/308'

'400':

\$ref: 'TS29571_CommonData.yaml#/components/responses/400'

'401':

\$ref: 'TS29571_CommonData.yaml#/components/responses/401'

'403':

\$ref: 'TS29571_CommonData.yaml#/components/responses/403'

'404':

\$ref: 'TS29571_CommonData.yaml#/components/responses/404'

'411':

\$ref: 'TS29571_CommonData.yaml#/components/responses/411'

'413':

\$ref: 'TS29571_CommonData.yaml#/components/responses/413'

'415':

\$ref: 'TS29571_CommonData.yaml#/components/responses/415'

'429':

\$ref: 'TS29571_CommonData.yaml#/components/responses/429'

'500':

\$ref: 'TS29571_CommonData.yaml#/components/responses/500'

'501':

\$ref: 'TS29571_CommonData.yaml#/components/responses/501'

'502':

\$ref: 'TS29571_CommonData.yaml#/components/responses/502'

'503':

\$ref: 'TS29571_CommonData.yaml#/components/responses/503'

default:

\$ref: 'TS29571_CommonData.yaml#/components/responses/default'

/mbs-sessions/subscriptions/{subscriptionId}:

patch:

summary: StatusSubscribe to modify (update or renew) an individual subscription

tags:

\- Individual Subscription for an MBS session

operationId: StatusSubscribeMod

security:

\- {}

\- oAuth2ClientCredentials:

\- nmbsmf-mbssession

\- oAuth2ClientCredentials:

\- nmbsmf-mbssession

\- nmbsmf-mbssession:mbs-sessions

parameters:

\- name: subscriptionId

in: path

required: true

description: Unique ID of the individual subscription to be modified

schema:

type: string

requestBody:

description: Data to be modified in the MBSSessionSubscription

required: true

content:

application/json-patch+json:

schema:

type: array

items:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/PatchItem'

minItems: 1

responses:

'200':

description: Successful modification of the individual Status Subscription

content:

application/json:

schema:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/MbsSessionSubscription'

'307':

\$ref: 'TS29571_CommonData.yaml#/components/responses/307'

'308':

\$ref: 'TS29571_CommonData.yaml#/components/responses/308'

'400':

\$ref: 'TS29571_CommonData.yaml#/components/responses/400'

'401':

\$ref: 'TS29571_CommonData.yaml#/components/responses/401'

'403':

\$ref: 'TS29571_CommonData.yaml#/components/responses/403'

'404':

\$ref: 'TS29571_CommonData.yaml#/components/responses/404'

'411':

\$ref: 'TS29571_CommonData.yaml#/components/responses/411'

'413':

\$ref: 'TS29571_CommonData.yaml#/components/responses/413'

'415':

\$ref: 'TS29571_CommonData.yaml#/components/responses/415'

'429':

\$ref: 'TS29571_CommonData.yaml#/components/responses/429'

'500':

\$ref: 'TS29571_CommonData.yaml#/components/responses/500'

'502':

\$ref: 'TS29571_CommonData.yaml#/components/responses/502'

'503':

\$ref: 'TS29571_CommonData.yaml#/components/responses/503'

default:

\$ref: 'TS29571_CommonData.yaml#/components/responses/default'

delete:

summary: StatusUnSubscribe to unsubscribe from the Status Subscription

tags:

\- Individual Subscription for an MBS session

operationId: StatusUnSubscribe

security:

\- {}

\- oAuth2ClientCredentials:

\- nmbsmf-mbssession

\- oAuth2ClientCredentials:

\- nmbsmf-mbssession

\- nmbsmf-mbssession:mbs-sessions

parameters:

\- name: subscriptionId

in: path

required: true

description: Unique ID of the subscription to be deleted

schema:

type: string

responses:

'204':

description: Successful deletion of the subscription

'307':

\$ref: 'TS29571_CommonData.yaml#/components/responses/307'

'308':

\$ref: 'TS29571_CommonData.yaml#/components/responses/308'

'400':

\$ref: 'TS29571_CommonData.yaml#/components/responses/400'

'401':

\$ref: 'TS29571_CommonData.yaml#/components/responses/401'

'403':

\$ref: 'TS29571_CommonData.yaml#/components/responses/403'

'404':

\$ref: 'TS29571_CommonData.yaml#/components/responses/404'

'429':

\$ref: 'TS29571_CommonData.yaml#/components/responses/429'

'500':

\$ref: 'TS29571_CommonData.yaml#/components/responses/500'

'502':

\$ref: 'TS29571_CommonData.yaml#/components/responses/502'

'503':

\$ref: 'TS29571_CommonData.yaml#/components/responses/503'

default:

\$ref: 'TS29571_CommonData.yaml#/components/responses/default'

/mbs-sessions/contexts/subscriptions:

post:

summary: ContextStatusSubscribe creating a subscription

tags:

\- Subscriptions collection for MBS contexts

operationId: ContextStatusSubscribe

security:

\- {}

\- oAuth2ClientCredentials:

\- nmbsmf-mbssession

\- oAuth2ClientCredentials:

\- nmbsmf-mbssession

\- nmbsmf-mbssession:mbs-contexts

requestBody:

description: Data within the ContextStatusSubscribe Request

required: true

content:

application/json:

schema:

\$ref: '#/components/schemas/ContextStatusSubscribeReqData'

responses:

'201':

description: successful creation of a Context Status Subscription

content:

application/json:

schema:

\$ref: '#/components/schemas/ContextStatusSubscribeRspData'

'204':

description: Successful response without content in the response

'307':

\$ref: 'TS29571_CommonData.yaml#/components/responses/307'

'308':

\$ref: 'TS29571_CommonData.yaml#/components/responses/308'

'400':

\$ref: 'TS29571_CommonData.yaml#/components/responses/400'

'401':

\$ref: 'TS29571_CommonData.yaml#/components/responses/401'

'403':

\$ref: 'TS29571_CommonData.yaml#/components/responses/403'

'404':

\$ref: 'TS29571_CommonData.yaml#/components/responses/404'

'411':

\$ref: 'TS29571_CommonData.yaml#/components/responses/411'

'413':

\$ref: 'TS29571_CommonData.yaml#/components/responses/413'

'415':

\$ref: 'TS29571_CommonData.yaml#/components/responses/415'

'429':

\$ref: 'TS29571_CommonData.yaml#/components/responses/429'

'500':

\$ref: 'TS29571_CommonData.yaml#/components/responses/500'

'502':

\$ref: 'TS29571_CommonData.yaml#/components/responses/502'

'503':

\$ref: 'TS29571_CommonData.yaml#/components/responses/503'

default:

\$ref: 'TS29571_CommonData.yaml#/components/responses/default'

callbacks:

contextStatusNotification:

'{\$request.body#/subscription/notifUri}':

post:

parameters:

\- name: Content-Encoding

in: header

description: Content-Encoding, described in IETF RFC 9110

schema:

type: string

requestBody:

description: Notification Content

content:

application/json:

schema:

\$ref: '#/components/schemas/ContextStatusNotifyReqData'

responses:

'204':

description: Expected response to a successful callback processing

headers:

Accept-Encoding:

description: Accept-Encoding, described in IETF RFC 9110

schema:

type: string

'307':

\$ref: 'TS29571_CommonData.yaml#/components/responses/307'

'308':

\$ref: 'TS29571_CommonData.yaml#/components/responses/308'

'400':

\$ref: 'TS29571_CommonData.yaml#/components/responses/400'

'401':

\$ref: 'TS29571_CommonData.yaml#/components/responses/401'

'403':

\$ref: 'TS29571_CommonData.yaml#/components/responses/403'

'404':

\$ref: 'TS29571_CommonData.yaml#/components/responses/404'

'411':

\$ref: 'TS29571_CommonData.yaml#/components/responses/411'

'413':

\$ref: 'TS29571_CommonData.yaml#/components/responses/413'

'415':

\$ref: 'TS29571_CommonData.yaml#/components/responses/415'

'429':

\$ref: 'TS29571_CommonData.yaml#/components/responses/429'

'500':

\$ref: 'TS29571_CommonData.yaml#/components/responses/500'

'501':

\$ref: 'TS29571_CommonData.yaml#/components/responses/501'

'502':

\$ref: 'TS29571_CommonData.yaml#/components/responses/502'

'503':

\$ref: 'TS29571_CommonData.yaml#/components/responses/503'

default:

\$ref: 'TS29571_CommonData.yaml#/components/responses/default'

/mbs-sessions/contexts/subscriptions/{subscriptionId}:

patch:

summary: ContextStatusSubscribe modifying an individual subscription

tags:

\- Individual Subscription for an MBS context

operationId: ContextStatusSubscribeMod

security:

\- {}

\- oAuth2ClientCredentials:

\- nmbsmf-mbssession

\- oAuth2ClientCredentials:

\- nmbsmf-mbssession

\- nmbsmf-mbssession:mbs-contexts

parameters:

\- name: subscriptionId

in: path

required: true

description: Unique ID of the subscription to be modified

schema:

type: string

requestBody:

description: Data to be modified in the ContextStatusSubscription

required: true

content:

application/json-patch+json:

schema:

type: array

items:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/PatchItem'

minItems: 1

responses:

'200':

description: Successful modification of a Context Status Subscription

content:

application/json:

schema:

\$ref: '#/components/schemas/ContextStatusSubscription'

'307':

\$ref: 'TS29571_CommonData.yaml#/components/responses/307'

'308':

\$ref: 'TS29571_CommonData.yaml#/components/responses/308'

'400':

\$ref: 'TS29571_CommonData.yaml#/components/responses/400'

'401':

\$ref: 'TS29571_CommonData.yaml#/components/responses/401'

'403':

\$ref: 'TS29571_CommonData.yaml#/components/responses/403'

'404':

\$ref: 'TS29571_CommonData.yaml#/components/responses/404'

'411':

\$ref: 'TS29571_CommonData.yaml#/components/responses/411'

'413':

\$ref: 'TS29571_CommonData.yaml#/components/responses/413'

'415':

\$ref: 'TS29571_CommonData.yaml#/components/responses/415'

'429':

\$ref: 'TS29571_CommonData.yaml#/components/responses/429'

'500':

\$ref: 'TS29571_CommonData.yaml#/components/responses/500'

'502':

\$ref: 'TS29571_CommonData.yaml#/components/responses/502'

'503':

\$ref: 'TS29571_CommonData.yaml#/components/responses/503'

default:

\$ref: 'TS29571_CommonData.yaml#/components/responses/default'

delete:

summary: ContextStatusUnSubscribe

tags:

\- Individual Subscription for an MBS context

operationId: ContextStatusUnSubscribe

security:

\- {}

\- oAuth2ClientCredentials:

\- nmbsmf-mbssession

\- oAuth2ClientCredentials:

\- nmbsmf-mbssession

\- nmbsmf-mbssession:mbs-contexts

parameters:

\- name: subscriptionId

in: path

required: true

description: Unique ID of the subscription to be deleted

schema:

type: string

responses:

'204':

description: Successful deletion

'307':

\$ref: 'TS29571_CommonData.yaml#/components/responses/307'

'308':

\$ref: 'TS29571_CommonData.yaml#/components/responses/308'

'400':

\$ref: 'TS29571_CommonData.yaml#/components/responses/400'

'401':

\$ref: 'TS29571_CommonData.yaml#/components/responses/401'

'403':

\$ref: 'TS29571_CommonData.yaml#/components/responses/403'

'404':

\$ref: 'TS29571_CommonData.yaml#/components/responses/404'

'429':

\$ref: 'TS29571_CommonData.yaml#/components/responses/429'

'500':

\$ref: 'TS29571_CommonData.yaml#/components/responses/500'

'502':

\$ref: 'TS29571_CommonData.yaml#/components/responses/502'

'503':

\$ref: 'TS29571_CommonData.yaml#/components/responses/503'

default:

\$ref: 'TS29571_CommonData.yaml#/components/responses/default'

components:

securitySchemes:

oAuth2ClientCredentials:

type: oauth2

flows:

clientCredentials:

tokenUrl: '{nrfApiRoot}/oauth2/token'

scopes:

nmbsmf-mbssession: Access to the Nmbsmf-MBSSession API

nmbsmf-mbssession:mbs-sessions: \>

Access to service operations applying to MBS session resources, i.e. Create, Update,

Delete, StatusSubscribe, StatusUnsubscribe

nmbsmf-mbssession:mbs-contexts: \>

Access to service operations applying to MBS session context resources, i.e.

ContextUpdate, ContextStatusSubscribe and ContextStatusUnsubscribe

schemas:

\#

\# STRUCTURED DATA TYPES

\#

CreateReqData:

description: Data within Create Request

type: object

properties:

mbsSession:

\$ref: '#/components/schemas/ExtMbsSession'

supportedFeatures:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/SupportedFeatures'

required:

\- mbsSession

CreateRspData:

description: Data within Create Response

type: object

properties:

mbsSession:

\$ref: '#/components/schemas/ExtMbsSession'

eventList:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/MbsSessionEventReportList'

supportedFeatures:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/SupportedFeatures'

required:

\- mbsSession

ExtMbsSession:

description: MbsSession common data type with MB-SMF API specific extensions

allOf:

\- \$ref: 'TS29571_CommonData.yaml#/components/schemas/MbsSession'

\- \$ref: '#/components/schemas/MbsSessionExtension'

MbsSessionExtension:

description: MB-SMF API specific extensions to the MbsSession common data type

type: object

properties:

mbsSecurityContext:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/MbsSecurityContext'

contactPcfInd:

type: boolean

default: false

areaSessionPolicyId:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/AreaSessionPolicyId'

ContextUpdateReqData:

description: Data within ContextUpdate Request

type: object

properties:

nfcInstanceId:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/NfInstanceId'

mbsSessionId:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/MbsSessionId'

areaSessionId:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/AreaSessionId'

requestedAction:

\$ref: '#/components/schemas/ContextUpdateAction'

dlTunnelInfo:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/Bytes'

n2MbsSmInfo:

\$ref: '#/components/schemas/N2MbsSmInfo'

ranNodeId:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/GlobalRanNodeId'

leaveInd:

type: boolean

enum:

\- true

required:

\- nfcInstanceId

\- mbsSessionId

ContextUpdateRspData:

description: Data within ContextUpdate Response

type: object

properties:

llSsm:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/Ssm'

cTeid:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/Uint32'

n2MbsSmInfo:

\$ref: '#/components/schemas/N2MbsSmInfo'

ContextStatusSubscribeReqData:

description: Data within ContextStatusSubscribe Request

type: object

properties:

subscription:

\$ref: '#/components/schemas/ContextStatusSubscription'

required:

\- subscription

ContextStatusSubscription:

description: Context Status Subscription

type: object

properties:

nfcInstanceId:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/NfInstanceId'

mbsSessionId:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/MbsSessionId'

eventList:

type: array

items:

\$ref: '#/components/schemas/ContextStatusEvent'

minItems: 1

notifyUri:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/Uri'

notifyCorrelationId:

type: string

expiryTime:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/DateTime'

required:

\- nfcInstanceId

\- mbsSessionId

\- eventList

\- notifyUri

ContextStatusEvent:

description: Context Status Event

type: object

properties:

eventType:

\$ref: '#/components/schemas/ContextStatusEventType'

immediateReportInd:

type: boolean

default: false

reportingMode:

\$ref: '#/components/schemas/ReportingMode'

required:

\- eventType

ContextStatusSubscribeRspData:

description: Data within ContextStatusSubscribe Response

type: object

properties:

subscription:

\$ref: '#/components/schemas/ContextStatusSubscription'

reportList:

type: array

items:

\$ref: '#/components/schemas/ContextStatusEventReport'

minItems: 1

mbsContextInfo:

\$ref: '#/components/schemas/MbsContextInfo'

required:

\- subscription

MbsContextInfo:

description: MBS context information

type: object

properties:

startTime:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/DateTime'

anyUeInd:

type: boolean

default: false

llSsm:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/Ssm'

cTeid:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/Uint32'

mbsServiceArea:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/MbsServiceArea'

mbsServiceAreaInfoList:

description: \>

A map (list of key-value pairs) where the key identifies an areaSessionId

additionalProperties:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/MbsServiceAreaInfo'

minProperties: 1

ContextStatusEventReport:

description: Context Status Event Report

type: object

properties:

eventType:

\$ref: '#/components/schemas/ContextStatusEventType'

timeStamp:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/DateTime'

qosInfo:

\$ref: '#/components/schemas/QosInfo'

statusInfo:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/MbsSessionActivityStatus'

mbsServiceArea:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/MbsServiceArea'

mbsServiceAreaInfoList:

description: \>

A map (list of key-value pairs) where the key identifies an areaSessionId

additionalProperties:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/MbsServiceAreaInfo'

minProperties: 1

multicastTransAddInfo:

\$ref: '#/components/schemas/MulticastTransportAddressChangeInfo'

mbsSecurityContext:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/MbsSecurityContext'

required:

\- eventType

\- timeStamp

ContextStatusNotifyReqData:

description: Context Status Notification

type: object

properties:

reportList:

type: array

items:

\$ref: '#/components/schemas/ContextStatusEventReport'

minItems: 1

notifyCorrelationId:

type: string

required:

\- reportList

StatusSubscribeReqData:

description: Data within the StatusSubscribe Request

type: object

properties:

subscription:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/MbsSessionSubscription'

required:

\- subscription

StatusSubscribeRspData:

description: Data within StatusSubscribe Response

type: object

properties:

subscription:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/MbsSessionSubscription'

eventList:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/MbsSessionEventReportList'

required:

\- subscription

StatusNotifyReqData:

description: Status Notification

type: object

properties:

eventList:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/MbsSessionEventReportList'

required:

\- eventList

N2MbsSmInfo:

description: N2 MBS Session Management information

type: object

properties:

ngapIeType:

\$ref: '#/components/schemas/NgapIeType'

ngapData:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/RefToBinaryData'

required:

\- ngapIeType

\- ngapData

MulticastTransportAddressChangeInfo:

description: Multicast Transport Address Change Information

type: object

properties:

llSsm:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/Ssm'

cTeid:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/Uint32'

areaSessionId:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/AreaSessionId'

required:

\- llSsm

\- cTeid

QosInfo:

description: QoS Information

type: object

properties:

qosFlowsAddModRequestList:

type: array

items:

\$ref: '#/components/schemas/QosFlowAddModifyRequestItem'

minItems: 1

qosFlowsRelRequestList:

type: array

items:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/Qfi'

minItems: 1

QosFlowAddModifyRequestItem:

description: Individual MBS QoS flow requested to be created or modified

type: object

properties:

qfi:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/Qfi'

qosFlowProfile:

\$ref: '#/components/schemas/QosFlowProfile'

required:

\- qfi

QosFlowProfile:

description: MBS QoS flow profile

type: object

properties:

5qi:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/5Qi'

nonDynamic5Qi:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/NonDynamic5Qi'

dynamic5Qi:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/Dynamic5Qi'

arp:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/Arp'

gbrQosFlowInfo:

\$ref: '#/components/schemas/GbrQosFlowInformation'

required:

\- 5qi

GbrQosFlowInformation:

description: GBR MBS QoS flow information

type: object

properties:

maxFbrDl:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/BitRate'

guaFbrDl:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/BitRate'

maxPacketLossRateDl:

\$ref: 'TS29571_CommonData.yaml#/components/schemas/PacketLossRate'

required:

\- maxFbrDl

\- guaFbrDl

ExtProblemDetails:

description: Extended Problem Details data structure

allOf:

\- \$ref: 'TS29571_CommonData.yaml#/components/schemas/ProblemDetails'

\- \$ref: '#/components/schemas/ProblemDetailsExtension'

ProblemDetailsExtension:

description: Extensions to ProblemDetails

type: object

properties:

accMbsServiceInfo:

\$ref: 'TS29537_Npcf_MBSPolicyAuthorization.yaml#/components/schemas/AcceptableMbsServInfo'

UpdateRspData:

description: Data within Update Response

type: object

properties:

mbsSession:

\$ref: '#/components/schemas/ExtMbsSession'

required:

\- mbsSession

\#

\# SIMPLE DATA TYPES

\#

\#

\# ENUMERATIONS

\#

ContextUpdateAction:

description: Start or Terminate MBS data reception

anyOf:

\- type: string

enum:

\- START

\- TERMINATE

\- type: string

ContextStatusEventType:

description: Context Status Event Type

anyOf:

\- type: string

enum:

\- QOS_INFO

\- STATUS_INFO

\- SERVICE_AREA_INFO

\- SESSION_RELEASE

\- MULT_TRANS_ADD_CHANGE

\- SECURITY_INFO

\- type: string

ReportingMode:

description: Reporting Mode

anyOf:

\- type: string

enum:

\- CONTINUOUS

\- ONE_TIME

\- type: string

NgapIeType:

description: NGAP Information Element Type

anyOf:

\- type: string

enum:

\- MBS_DIS_SETUP_REQ

\- MBS_DIS_SETUP_RSP

\- MBS_DIS_SETUP_FAIL

\- MBS_DIS_REL_REQ

\- type: string

########  Annex B (informative): Change history

<!-- table -->
| Change history (x8) |
| Date | Meeting | TDoc | CR | Rev | Cat | Subject/Comment | New version |
| 2021-08 | CT4#105e | C4-214755 |  |  |  | Following pCRs are implemented into the skeleton of the TS 29.532 v0.0.0 (C4-214118): C4-214026, C4-214032, C4-214188, C4-214190, C4-214191, C4-214236, C4-214237, C4-214238, C4-214239, C4-214547, C4-214549, C4-214551, C4-214554, C4-214683, C4-214684, C4-214685 and C4-214686. | 0.1.0 |
| 2021-10 | CT4#106e | C4-215519 |  |  |  | Following pCRs are implemented: C4-21-5015, C4-21-5017, C4-21-5071, C4-21-5075, C4-21-5076, C4-21-5077, C4-21-5078, C4-21-5079, C4-21-5080, C4-21-5081, C4-21-5083, C4-21-5335, C4-21-5337, C4-21-5338, C4-21-5339, C4-21-5340, C4-21-5341, C4-21-5374, C4-21-5375, C4-21-5376, C4-21-5377, C4-21-5498, C4-21-5500. | 0.2.0 |
| 2021-11 | CT4#107e | C4-216472 |  |  |  | Following pCRs are implemented: C4-216019, C4-216139, C4-216210, C4-216424, C4-216425, C4-216601, C4-216604, C4-216605. | 0.3.0 |
| 2021-12 | CT#94 | CP-213158 |  |  |  | V1.0.0 presented for information | 1.0.0 |
| 2022-01 | CT4#107e-bis | CP-220454 |  |  |  | Following pCRs are implemented: C4-220097, C4-220098, C4-220327, C4-220352, C4-220416, C4-220417 and C4-220418. | 1.1.0 |
| 2022-02 | CT4#108e | C4-221592 |  |  |  | Following pCRs are implemented: C4-221123, C4-221138, C4-221140, C4-221147, C4-221380, C4-221419, C4-221420, C4-221531, C4-221546. | 1.2.0 |
| 2022-03 | CT#95e | CP-220107 |  |  |  | TS presented for approval | 2.0.0 |
| 2022-03 | CT#95e |  |  |  |  | TS approved | 17.0.0 |
| 2022-06 | CT#96 | CP-221023 | 0006 |  | F | Nmbsmf miscellaneous corrections | 17.1.0 |
| 2022-06 | CT#96 | CP-221023 | 0008 |  | B | MBS Frequency Selection Area Identifier | 17.1.0 |
| 2022-06 | CT#96 | CP-221023 | 0010 |  | F | MBS Service Area Information for Location dependent MBS session | 17.1.0 |
| 2022-06 | CT#96 | CP-221023 | 0011 |  | F | Granularity of MBSSession service operations for Location dependent MBS session | 17.1.0 |
| 2022-06 | CT#96 | CP-221023 | 0012 |  | B | Broadcast Delivery Status event | 17.1.0 |
| 2022-06 | CT#96 | CP-221023 | 0013 |  | B | Ingress Tunnel Address Change Status Event | 17.1.0 |
| 2022-06 | CT#96 | CP-221023 | 0007 | 1 | F | NGAP MB-SMF related Ies | 17.1.0 |
| 2022-06 | CT#96 | CP-221023 | 0002 | 2 | F | Simple data types and enumerations for Nmbsmf_TMGI Service | 17.1.0 |
| 2022-06 | CT#96 | CP-221023 | 0004 | 2 | F | Simple data types for Nmbsmf_MBSSession Service | 17.1.0 |
| 2022-06 | CT#96 | CP-221023 | 0005 | 1 | F | Corrections to Nmbsmf data models | 17.1.0 |
| 2022-06 | CT#96 | CP-221024 | 0014 | 1 | B | Multicast Transport Address Change Context Status event | 17.1.0 |
| 2022-06 | CT#96 | CP-221236 | 0009 | 3 | B | QoS information in Context Status Event Report | 17.1.0 |
| 2022-06 | CT#96 | CP-221024 | 0001 | 3 | B | MBS Security Context Delivery | 17.1.0 |
| 2022-06 | CT#96 | CP-221024 | 0017 | 1 | F | Updates to Service Description | 17.1.0 |
| 2022-06 | CT#96 | CP-221024 | 0020 | 1 | F | Corrctions on HTTP Response | 17.1.0 |
| 2022-06 | CT#96 | CP-221024 | 0018 | 2 | F | Application Error for TMGI Service | 17.1.0 |
| 2022-06 | CT#96 | CP-221024 | 0019 | 2 | F | Application Error for MBS Session Service | 17.1.0 |
| 2022-06 | CT#96 | CP-221051 | 0025 |  | F | 29.532 Rel-17 API version and External doc update | 17.1.0 |
| 2022-09 | CT#97e | CP-222031 | 0029 |  | F | Event reports in Create response and Status Subscribe Response | 17.2.0 |
| 2022-09 | CT#97e | CP-222058 | 0033 |  | F | 29.532 0033 Rel-17 API version and External doc update | 17.2.0 |
| 2022-09 | CT#97e | CP-222031 | 0027 | 2 | F | Change of MBS session authorization | 17.2.0 |
| 2022-09 | CT#97e | CP-222031 | 0031 | 1 | F | Clarification on the tunnel information | 17.2.0 |
| 2022-09 | CT#97e | CP-222031 | 0034 |  | B | Defining the "indication that the PCF has to be contacted" | 17.2.0 |
| 2022-12 | CT#98e | CP-223036 | 0037 |  | F | Complete the applicable procedure for the ContextStatusNotify service operation | 17.3.0 |
| 2022-12 | CT#98e | CP-223036 | 0042 |  | F | Corrections for MBS session with PCC | 17.3.0 |
| 2022-12 | CT#98e | CP-223036 | 0043 | 1 | F | Miscellaneous corrections (OpenAPI errors, incorrect IEs and references, etc) | 17.3.0 |
| 2022-12 | CT#98e | CP-223036 | 0044 | 1 | F | Corrections to N2 MBS Session Management Information | 17.3.0 |
| 2022-12 | CT#98e | CP-223042 | 0041 | 1 | F | Missing mandatory status codes and 307/308 codes in OpenAPI | 17.3.0 |
| 2022-12 | CT#98e | CP-223225 | 0039 | 3 | F | Adding NID to TmgiAllocated type | 17.3.0 |
| 2022-12 | CT#98e | CP-223225 | 0036 | 2 | F | Complete the description for ProblemDetails in the Nmbsmf_MBSSession API | 17.3.0 |
| 2022-12 | CT#98e | CP-223066 | 0046 |  | F | 29.532 0046 Rel-17 API version and External doc update | 17.3.0 |
| 2022-12 | CT#98e | CP-223036 | 0045 | 2 | F | Clarification on MB-SMF behaviour on handling shared NG-U tunnel | 17.3.0 |
| 2023-03 | CT#99 | CP-230029 | 0048 |  | F | OAuth2 scopes in the MBSSession API | 18.0.0 |
| 2023-03 | CT#99 | CP-230049 | 0049 | 1 | F | Correct string datatype and StatusNotify service operation description | 18.0.0 |
| 2023-03 | CT#99 | CP-230071 | 0052 |  | F | 29.532 Rel18 API version and External doc update | 18.0.0 |
| 2023-06 | CT#100 | CP-231026 | 0050 | 2 | F | Location header description | 18.1.0 |
| 2023-06 | CT#100 | CP-231037 | 0054 | 1 | B | Adding Associated Session ID to Nmbsmf_MBSSession_Create Request | 18.1.0 |
| 2023-06 | CT#100 | CP-231076 | 0057 | 1 | A | Essential Correction for the usage of the cause "UNKNOWN_MBS_SERVICE_AREA" | 18.1.0 |
| 2023-09 | CT#101 | CP-232065 | 0063 | 1 | F | Correct callback URI for mbsSession service | 18.2.0 |
| 2023-09 | CT#101 | CP-232058 | 0064 |  | F | EventType attribute correction | 18.2.0 |
| 2023-12 | CT#102 | CP-233044 | 0067 |  | F | Editorial corrections and DateTime clarification | 18.3.0 |
| 2023-12 | CT#102 | CP-233027 | 0068 |  | F | Update and replace obsoleted HTTP RFCs | 18.3.0 |
| 2023-12 | CT#102 | CP-233063 | 0073 | 1 | A | Area Session Policy ID in Nmbsmf_MBSSession_Create request | 18.3.0 |
| 2023-12 | CT#102 | CP-233063 | 0075 | 1 | A | MBS Service Area not contained within the MB-SMF service area | 18.3.0 |
| 2023-12 | CT#102 | CP-233063 | 0077 | 2 | A | Location Dependent MBS broadcast session with multiple MB-SMFs | 18.3.0 |
| 2023-12 | CT#102 | CP-233030 | 0079 |  | F | 29.532: Replacing obsoleted HTTP RFC 7807 with 9457 | 18.3.0 |
| 2023-12 | CT#102 | CP-233060 | 0082 |  | F | 29.532 Rel-18 API version and External doc update | 18.3.0 |
| 2024-03 | CT#103 | CP-240035 | 0085 | 2 | B | RedCap UEs Information for a broadcast MBS session | 18.4.0 |
| 2024-03 | CT#103 | CP-240035 | 0086 | 2 | B | New feature for Nmbsmf_MBSSession to support MOCN | 18.4.0 |
| 2024-03 | CT#103 | CP-240236 | 0088 |  | F | 29.532 Rel-18 API version and External doc update | 18.4.0 |
| 2024-06 | CT#104 | CP-241050 | 0089 | 1 | F | Definition of MBS related terms | 18.5.0 |
| 2024-06 | CT#104 | CP-241033 | 0090 |  | F | Supported Features in MBS Session Create request and response | 18.5.0 |
| 2024-06 | CT#104 | CP-241033 | 0091 | 1 | F | Correction of enumeration description and editorial mistake | 18.5.0 |
| 2024-06 | CT#104 | CP-241052 | 0092 |  | F | 29.532 Rel-18 API version and External doc update | 18.5.0 |
| 2025-03 | CT#107 | CP-250031 | 0093 |  | F | Correction of MBS support for eRedCap UEs | 18.6.0 |
| 2025-03 | CT#107 | CP-250136 | 0094 |  | F | 29.532 Rel-18 API version and External doc update | 18.6.0 |
<!-- /table -->
