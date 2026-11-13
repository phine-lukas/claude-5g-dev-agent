# A.5 Service and service operation description template

The description of a service or service operation in this specification shall be done according to the following template.

NOTE: The heading level should follow that of the actual clause where the service is specified.

**X.x \<*Nnfname*\_ServiceName\<\_OperationName\>\>**

**X.x.1 Description**

**Service or service operation name:** \<Nnfname_ServiceName\<\_OperationName\>\>.

**Description:** \<short descriptive text\>.

**Known NF Consumers:** \<list of NFs\>.

**Inputs, Required:** \<list of parameters\> *-- Parameters required from NF Consumer for successful completion of the service or service operation. Parameters required for the operation of the underlying protocol shall not be listed.*

**Inputs, Optional:** \<list of parameters\> *-- Additional parameters that may be provided by NF Consumer for execution of the service or service operation. Parameters required for the operation of the underlying protocol shall not be listed.*

**Outputs, Required:** \<list of parameters\>, \< Nnfname_ServiceNameX\<\_OperationNameY \>\>, \<Other\> *-- Parameters provided to NF Consumer and/or service triggered upon successful completion of the service and/or other (e.g. procedure triggered). Parameters required for the operation of the underlying protocol shall not be listed.*

**Outputs, Optional:** \<list of parameters\> -- *Additional parameters provided to NF Consumer upon successful completion of the service or service operation. Parameters required for the operation of the underlying protocol shall not be listed.*

**X.x.2 Service/service operation information flow**

\<Information flow of the service or service operation offered by NF Producer to NF Consumer over the NF Producer service-based interface\>.

NOTE: This information flow can require invoking other services. In this case, the invoked services are represented as described in clause A.3.
