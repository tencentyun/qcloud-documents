
## Product Overview

Tencent Cloud's Cloud Message Queue (CMQ) is a distributed message queue service used for storing messages transferred between processes. It is designed to provide reliable message-based asynchronous communication service between different applications deployed in a distributed way or between different components of an application. Messages are stored in a highly reliable and available message queue, which allows multiple processes to perform read and write operations simultaneously without interfering with each other. With Tencent Cloud CMQ, messages can be transferred, without any data loss, between distributed components of applications executing different tasks. There is no need to keep every component available at all time.

The queue acts as a buffer between the data sender and the data receiver, eliminating the problems caused by the circumstances in which the data sender works faster than the data receiver or the data sender or receiver only connects to the network intermittently.

"Message" in CMQ indicates data transmitted between processes of the same computer/different computers while "message queue" is a container for retaining messages during the transmission. The message is sent to the queue, which acts as an intermediary to relay the message from its source to its destination.

The figure below shows an example of the traditional process communication mode, in which the client requests a service from the server and waits for a response from the server. Such a mode has many shortcomings, for example, the likelihood of lost request in case of poor network conditions, or failed request due to timeout caused by overlong waiting of client in case of lengthy processing of server.
![](//mccdn.qcloud.com/static/img/6c066f82f7e94e6ee58c782325860c02/image.jpg)

To deal with these problems, Tencent Cloud introduces the CMQ service for message distribution and management. With Tencent Cloud CMQ, components of an application can be separated to run independently, and message management between the components can be simplified. Any component of a distributed application can store messages in the queue, and Tencent Cloud CMQ ensures that each message is transmitted at least once and can be read and written many times. A single queue can be used by multiple distributed application components at the same time which are not required to collaborate with each other. All the components can programmatically retrieve and operate messages using CMQ APIs.


## Application Scenarios


CMQ is recommended for application scenarios in which asynchronous communication is required. For example:

- In applications where reliable delivery of a message needs to be ensured, even if the receiver is unavailable for reasons such as power outage, crash or CPU overload when the message is being sent from the sender, receiver can still receive the message once becoming available. This function is not available in traditional message queues since it only stores messages in memory. Tencent Cloud CMQ enables messages to be stored persistently until message is acquired by the receiver successfully.

- A message queue should run normally even if the number of messages stored in the queue and visits keep increasing. The traditional message queue stores messages in local memory. Since the processing capability and memory capacity of stand-alone computers are limited, the queue is not scalable. In contrast, Tencent Cloud CMQ, featuring distributed architecture, can ensure the simple scalability of the queue and the scalability is completely visible to CMQ users.

- Two services need to communicate with each other in the case that the networks cannot be interconnected or the routing information (such as IP and port) of applications is not known. For example, if two services on Tencent Cloud need to communicate while they do not know each other's address, the communication can be achieved in such a way that one party sends messages to and the other party receives the messages from the queue agreed upon by both parties.

- Communication between system components or applications is frequent so that the components or applications need to maintain their network connections, and there are multiple communication contents. In such a scenario, traditional architecture will complicate the system design. For example, when a central processing service needs to assign tasks to multiple task processing services (similar to the master-worker mode), the master needs to maintain connections with all the workers and determine whether the workers have started to process the tasks so as to decide whether to reassign tasks. At the same time, the workers need to report task processing results to the master. Maintaining such a system at the same level will complicate the design, thus increasing the implementation difficulty and maintenance cost. As shown below, Tencent Cloud CMQ can reduce the coupling between the two sides, making the system simpler and more efficient.
![](//mccdn.qcloud.com/static/img/c39a0f8227943738dceb85575f56e4eb/image.jpg)

- The coupling between system components or applications is tight and needs to be reduced, especially when the controllability over the dependent components is relatively weak. For example, when a company's business CGI receives user submissions, it will store some data in its own system and forward the processed data to other business applications (such as data analysis system, data storage system, etc.). The traditional solution is to establish a connection between services through the socket. In this way, if the receiver's IP or port changes, or the receiver changes, the data sender needs to modify the information accordingly. But with Tencent Cloud CMQ, the sender and the receiver do not know each other's information, thus greatly reducing the coupling between them.

