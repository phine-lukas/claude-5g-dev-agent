# G.4 An SCP deployment example based on name-based routing

## G.4.0 General Information

This clause provides a deployment example for the SCP which is based on a name-based routing mechanism that provides IP over ICN capabilities such as those described in Xylomenos, George, et al. \[G1\].

The scenario describes an SCP offering based on an SBA-platform to interconnect 5GC Services (or a subset of the respective services). The Name-based Routing mechanism, described in this deployment example, is realized through a Path Computation Element which is the core part of the SCP. The 5GC Services are running as microservices on cloud/deployment units (clusters). A Service Router is the communication node (access node/gateway) between the SCP and the 5GC Services and resides as a single unit within a Service Deployment Cluster. The Service Router acts as communication proxy and it is responsible for mapping IP based messages onto ICN publication and subscriptions. The Service Router serves multiple 5GC Service Endpoints within that cluster. For direct communication the Service Router is not used.

5GC Functionalities communicate with the Service Router using standardized 3GPP SBIs.

The Functionalities within the Service Deployment Cluster are containerized Service Functions.

Depicted in Figure G.4-1, the Service Router act as SCP termination point and offer the SBI to the respective 5GC Service Functionalities. In this example, Service Routers and 5GC functionality, although co-located, are separate components within the Service Deployment Cluster. Multiple Functionalities can exist within the Service Deployment Cluster, all served by the respective Service Router when needed to communicate to other Service Functionalities within different clusters.

[figure]

Figure G.4-1: Deployment unit: 5GC functionality and co-located Service Agent(s) implementing peripheral tasks

In Figure G.4-1, the two depicted 5GC Service Functionalities (realized as Network Function Service Instances) may communicate in two ways. However, before the communication can be established between two 5GC Functionalities, Service Registration and Service Discovery need to take place, as described in Figure G.4.1-1. Service Registration and Service Discovery are provided in a standardized manner using 3GPP Service Based Interfaces.

## G.4.1 Service Registration and Service Discovery

Service registration can be done in several ways. One option is that ready 5GC Service Functions may register themselves with their service profile via the Nnrf interface. The registration request is forwarded to the internal Registry as well as forwarded to the operator's NRF. The internal registration is used to store the address to identifier relationship and the Service Deployment Cluster location. The external registration (NRF) is used to expose the Service Functionality to Services outside the depicted SCP.

Service discovery entails Function A requesting a resolvable identifier for Functionality B. This resolve request is received by the Service Router which performs the task with the help of the SCP. After the resolve is done, the 5GC Functionalities may communicate either directly without any further interaction through the SCP, when the targeted address is resolved within the same Service Deployment Cluster; or via the Service Router when the Functionality resides outside of the originator's Service Deployment Cluster. The Service Router then acts as gateway towards the underlying SCP platform.

[figure]

Figure G.4.1-1: Registering 5GC Functionalities in the SCP

## G.4.2 Overview of Deployment Scenario

Figure G.4.2-1 shows an overview of this deployment scenario. For SBI-based interactions with other 5GC functionalities, a consumer entity (e.g. 5GC functionality B in the cluster on the left side) communicates through the cluster's Service Router with other entities in other clusters (e.g. 5GC Functionality D in the cluster on the right side). The target selection is performed through the platform's Discovery Service. From the client's perspective, the Service Router is the first and only contact point to the SCP. The platform resolves the requested Service identifier and aligns the results with the platform's policies. The Path Computation Element calculates a path between the consumer and the producer (e.g. the shortest path between the nodes).

[figure]

Figure G.4.2-1: (NbR-) SCP interconnects multiple deployment clusters with external NRF

## G.4.3 References

\[G1\] Xylomenos, George, et al.: "IP over ICN goes live", 2018 European Conference on Networks and Communications (EuCNC). IEEE, 2018.

########  Annex H (normative): PTP usage guidelines
