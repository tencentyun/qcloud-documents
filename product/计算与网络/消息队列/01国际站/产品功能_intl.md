## Asynchronous Communication Protocol
After sending a message to the message queue, the sender can go back immediately instead of waiting for a response from the receiver. The message will be retained in the queue until it is fetched by the receiver. Therefore, the message is sent and processed asynchronously.

## Improved Reliability
In traditional mode, message requests may fail due to overlong waiting. But in CMQ mode, if the receiver is unavailable when a message is sent, the message will be retained in the queue until it is successfully delivered.

## Process Decoupling
CMQ can reduce the coupling between two processes. As long as the message format remains unchanged, the sender needs no modification even if the receiver's API, location or configuration are changed. Besides, the sender doesn't need to know the receiver when sending messages, thus simplifying the system design. However, in traditional mode, processes are connected via a remote procedure call (RPC) or the socket. When the API, IP or port of one side changes, the other must modify request configurations accordingly.

## Message Routing
The sender needs no a direct connection with the receiver since CMQ allows messages to be routed from the sender to the receiver. Even for two services between which network interworking is difficult to be available, the message routing also works.

## Multi-terminals
Multiple parts of the user system can send or receive messages simultaneously, and Tencent Cloud CMQ controls message availability through message status.
## Diversity
All queues can be configured independently and can be different. You can customize queue configurations for different application scenarios. For example, if the message processing in a queue takes a long time, you can optimize queue attributes.
