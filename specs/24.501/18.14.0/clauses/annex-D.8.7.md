## D.8.7 Non-imperative message part errors

This category includes:

a\) syntactically incorrect optional IEs; and

b\) conditional IE errors.

### D.8.7.1 Syntactically incorrect optional IEs

The UE shall treat all optional IEs that are syntactically incorrect in a message as not present in the message.

The network shall take the same approach.

### D.8.7.2 Conditional IE errors

When upon receipt of a UPDS message the UE diagnoses a "missing conditional IE" error or an "unexpected conditional IE" error, or when it receives a UPDS message containing at least one syntactically incorrect conditional IE, the UE shall ignore the message.

When the network receives a message and diagnoses a "missing conditional IE" error or an "unexpected conditional IE" error or when it receives a message containing at least one syntactically incorrect conditional IE, the network shall either:

a\) try to treat the message (the exact further actions are implementation dependent); or

b\) ignore the message.
