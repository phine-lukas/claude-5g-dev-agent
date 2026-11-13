## D.8.3 Unknown or unforeseen procedure transaction identity

### D.8.3.1 Procedure transaction identity

The following network procedures shall apply for handling an unknown, erroneous, or unforeseen PTI received in a UPDS message:

a\) In case the network receives a MANAGE UE POLICY COMPLETE message or MANAGE UE POLICY COMMAND REJECT message in which the PTI value is an assigned or unassigned value that does not match any PTI in use, the network shall ignore the UPDS message.

b\) In case the network receives a UPDS message in which the PTI value is a reserved value, the network shall ignore the UPDS message.

The following UE procedures shall apply for handling an unknown, erroneous, or unforeseen PTI received in a UPDS message:

a\) In case the UE receives a UPDS message in which the PTI value is a reserved value, the UE shall ignore the UPDS message.
