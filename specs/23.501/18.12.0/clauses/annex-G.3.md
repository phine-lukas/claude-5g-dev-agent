# G.3 An SCP based on independent deployment units

This clause shows an overview of SCP deployment based on the 5GC functionality and SCP being deployed in independent deployment units.

[figure]

Figure G.3-1: Independent deployment units for SCP and 5GC functionality

The SCP deployment unit can internally make use of microservices, however these microservices are up to vendors implementation and can be for example SCP agents and SCP controller as used in this example. The SCP agents implement the http intermediaries between service consumers and service producers. The SCP agents are controlled by the SCP controller. Communication between SCP controller and SCP agents is via SCP internal interface (4) and up to vendors implementation.

In this model it is a deployment choice to co-locate SCP and other 5GC functions or not. The SCP interfaces (1), (2) and (3) are service based interfaces. SCP itself is not a service producer itself, however acting as http proxy it registers services on behave of the producers in NRF. Interface (2) represents same services as (1) however using SCP proxy addresses. Interface (3) is interfacing NRF e.g. for service registration on behalf of the 5GC functions or service discovery.

[figure]

Figure G.3-2: 5GC functionality and SCP co-location choices

For SBI-based interactions with other 5GC functions, a consumer communicates through a SCP agent via SBI (1). SCP agent selects a target based on the request and routes the request to the target SCP agent (2). What routing and selection policies each SCP agent applies for a given request is determined by routing and selection policies determined by the SCP controller using for example information provided via NRF (3) or locally configured in the SCP controller. The routing and selection information is provided by the SCP controller to the SCP agents via SCP internal interface (4). Direct communication can coexist in the same deployment based on 3GPP specified mechanisms.

[figure]

Figure G.3-3: Overview of SCP deployment
