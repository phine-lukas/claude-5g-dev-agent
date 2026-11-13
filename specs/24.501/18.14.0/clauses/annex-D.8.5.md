## D.8.5 Non-semantical mandatory information element errors

### D.8.5.1 Common procedures

When on receipt of a message,

a\) an "imperative message part" error; or

b\) a "missing mandatory IE" error

is diagnosed or when a message containing:

a\) a syntactically incorrect mandatory IE;

b\) an IE with an IEI unknown in the message, but encoded as "comprehension required" (see 3GPP TS 24.007 \[11\]); or

c\) an out of sequence IE encoded as "comprehension required" (see 3GPP TS 24.007 \[11\]) is received,

the UE shall ignore the UPDS message;

the network shall proceed as follows:

the network shall:

1\) try to treat the message (the exact further actions are implementation dependent); or

2\) ignore the message.
