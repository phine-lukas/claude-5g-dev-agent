# A.1 Throttling Aalgorithms

## A.1.1 "Loss" Throttling Algorithm

### A.1.1.1 Example of Possible Implementation

This clause provides an example of a possible implementation of the "Loss" algorithm, amongst other possible methods.

It is possible to make use of a statistical loss function (e.g., random selection of messages to throttle based on the indicated percentage) to decide if the given message can be sent or need to be throttled. For example, the source node generates a random number between (0, 100) for each message which is a potential candidate for throttling. To realize 10% throttling, messages with a random number 10 or less are throttled and hence this achieves approximately a 10% reduction in the overall traffic. The actual traffic reduction might vary slightly from the requested percentage, albeit by an insignificant amount.

The algorithm can select certain messages to throttle in priority. For example, implementations can distinguish between higher-priority and lower-priority messages, and drop the lower-priority messages in favour of dropping the higher priority messages, as long as the total reduction in traffic conforms to the requested reduction in effect at the time. For example, in the 50-50 distribution of high priority and low priority messages, 20% reduction to low priority messages and 0% reduction to high priority messages need to be applied in order to achieve the effective reduction in traffic by 10% towards the overloaded node.

######## Annex B (Normative): CP and UP Selection Functions with Control and User Plane Separation
