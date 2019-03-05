Currently, Tencent Cloud's cloud load balancer allows the setting of an HTTP persistent connection for Layer-7 cloud load balance to the default value of 75s, and users can customize different cloud load balancer instances. So, what is an HTTP persistent connection, and an HTTP short connection?

## The relationship between HTTP and TCP/IP protocols
HTTP persistent connections and short connections are essentially TCP persistent connections and short connections. HTTP is used at the application layer, TCP is used at the transport layer, and IP is used at the network layer.  IP protocol mainly solves the problem of network routing and addressing, and TCP protocol mainly solves the problem of how to reliably transmit data packets above the IP layer so that the receiving terminal on the network receives all the packets sent by the transmitting terminal in the transmitting order. TCP is a reliable connection-oriented protocol.
 
## What does "HTTP is a stateless protocol" mean?
"HTTP is a stateless protocol" means that the protocol cannot remember transaction processing, and the server does not know the state of the client. That is to say, there is no connection between the actions of opening a web page on the same server this time and last time HTTP is a stateless connection-oriented protocol. But stateless does not mean that HTTP cannot maintain TCP connections and uses UDP protocol (no connection).
 
## What is a persistent connection, and a short connection?
Short connections are used by default in HTTP/1.0. A connection is established between the client and the server for each HTTP operation, and the connection will be interrupted after a task is completed. When an HTML or other types of Web pages the client browser accesses contain other Web resources (such as JavaScript files, image files, and CSS files), the browser will establish a new HTTP session upon each encounter with such a Web resource.

For HTTP/1.1 and later versions, persistent connections are used by default to maintain connection characteristics. This line of code will be added to the response header for HTTP protocols using persistent connections:

```
Connection:keep-alive
```

If a persistent connection is used, when a web page is opened, the TCP connection between the client and the server for the transmission of HTTP data will not be closed. When the client accesses the server again, this established connection will still be used. Keep-Alive does not keep the connection permanently, and it has a persistence duration, which can be set in different server software (such as Apache). The realization of persistent connections requires support by both the client and the server.

HTTP persistent connection and short connection are essentially TCP persistent connection and short connection.

### TCP connections
When a TCP protocol is used for network communication, a connection must be established between the client and the server before the read and write operations are performed. When the read and write operations are completed, the connection can be released when both sides no longer need it. The establishment of a connection depends on "three-way handshake", while the release requires "four-way handshake". So, the establishment of each connection needs to consume resources and time.

Diagram of connection establishment via three-way handshake:
![](//mccdn.qcloud.com/static/img/da079414fde193f4d790c72a719eba78/image.jpg)

Diagram of connection closing via four-way handshake:
![](//mccdn.qcloud.com/static/img/4e7b6439145e3db6c0a2ff62eec24322/image.jpg)

### TCP short connections
Simulation of a TCP short connection: the client initiates a connection request to the server, the server receives the request, and then a connection between them is established. The client sends a message to the server, the server returns a response to the client, and then a request is completed. At this time, both the client and the server can initiate a close operation, but usually the client will first initiate the operation. As mentioned above, short connections only pass one request operation between the client and the server.

The advantage of short connections is that they are easy to manage, as the existing connections are all useful, and no additional control measure is needed.

### TCP persistent connections
Simulation of a persistent connection: the client initiates a connection request to the server, the server accepts the request, and then a connection is established between them. After a request between the client and the server is completed, the connection between them will not be closed actively, and it will still be used for subsequent read and write operations.

TCP's keep-alive function is primarily provided for server applications. If the client has disappeared but the connection is not broken, there will be a half-open connection on the server, and the server, waiting for data from the client, will wait forever. The keep-alive function is used to detect such semi-open connections on the server.

If a given connection has not taken any actions within two hours, the server will send a detection message segment to the client, detecting the client's state based on the client's response. There are four states of the client:
- The client is running normally and the server is reachable. In this case, the client's TCP response is normal, and the server will reset the keep-alive timer.
- The client has crashed and is shut down or is rebooting. In both cases, the client cannot respond to TCP,  and the server will not receive a response to the detection from the client. The server will send a total of 10 detections, with an interval of 75 seconds. If the server does not receive any responses, it will consider the client closed, and it will terminate the connection.
- The client has crashed and already rebooted. The server will receive a response to its keep-alive detection. This response is a reset to inform the server to terminate the connection.
- The client is running normally, but the server is unreachable. This is similar to the second state.
 
## Advantages and disadvantages of persistent and short connections
As can be seen from the above, persistent connections can save more TCP establishment and close operations, reducing the waste of resources and time. For clients that frequently request resources, persistent connections are suitable. In the applications of persistent connections, usually, the client won't close the connection actively. If the connection between the client and the server leaves unclosed, when there are more and more connections for clients, the server will maintain too many connections. At this time, the server needs to take some measures, such as closing some connections through which no request has occurred for a long time, so as to avoid service damage on the server caused by some malicious connections. If possible, the server may limit the maximum number of persistent connections of each client, completely preventing malicious clients from wearing down the overall backend services.

For the server, short connections are easier to manage, as the existing connections are all useful, and no additional control measure is needed. But if the client makes requests frequently, plenty of time and bandwidth will be wasted for establishing and closing TCPs.

Persistent connections and short connections are established depending on the close strategy adopted by the client and the server. Different strategies should be used for different application scenarios.
