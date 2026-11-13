# A.2 Naming

## A.2.1 Service naming

Each NF service provided by a service-based interface shall be named and referred to according to the following nomenclature:

*- Nnfname_ServiceName*, where *Nnfname* is the service-based interface where the NF service is invoked. See clause 4.2.5 of TS 23.501 \[2\] for the list of service-based interfaces in the 5GS Architecture.

Example (illustrative): *Namf_Registration.*

## A.2.2 Service operation naming

If a service contains multiple independent operations, each operation shall be named and referred to according to the following nomenclature:

*- Nnfname_ServiceName_ServiceOperation\[Method\]*, where the *ServiceName* represents the actual NF service. The *ServiceOperation* itself defines the available service functionality which can be addressed by a specific operation. The *Method(s)* is/are the action(s), how the ServiceOperation can be used. It can be created, read, updated or deleted.

Example (illustrative): *Namf_Session_Registration\[Create\]*, *Namf_Session_Registration\[Delete\]*

In general, this operation naming structure for the given example is depicted in a tree-structure diagram:

[figure]

Figure A.2.2-1: Service Operation Naming and its Methods
