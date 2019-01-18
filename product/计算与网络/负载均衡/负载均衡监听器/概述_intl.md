Cloud Load Balance service is mainly provided by cloud load balancer listener. The listener is responsible for monitoring requests on the cloud load balancer instance, delivering policies to backend CVMs and other services.


Cloud load balancer listener is configured with protocols and ports for frontend connection (client to cloud load balancer) and the ports for backend connection (cloud load balancer to backend CVM instance). In addition, cloud load balancer listener can also be configured with [Session Persistence](https://intl.cloud.tencent.com/document/product/214/6154) and [Health Check](https://intl.cloud.tencent.com/document/product/214/6097) policies.


Cloud load balancer listener can listen on the Layer-4 and Layer-7 requests on the cloud load balancer instances and deliver the requests to the backend CVM for processing. The difference between Layer-4 and Layer-7 cloud load balancers lies in whether Layer-4 information or Layer-7 information is used as the basis for determining the way of forwarding traffic when cloud load balance is performed on backend CVMs. Layer-4 cloud load balancer uses transport layer protocol and receives requests and delivers them to the backend CVMs via VIP and ports, while Layer-7 cloud load balancer uses application layer protocol and delivers traffic based on the application layer information such as URL and HTTP header.

## Supported Protocol Types
Typical communication between Web applications is achieved via various layers of network, each of which provides specific communication features. According to the OSI network model, each layer has a standard communication format. Tencent Cloud's Cloud Load Balance involves Layer 4 (transport layer) and Layer 7 (application layer) in the network model.

Tencent Cloud's Cloud Load Balance supports request forwarding based on the following protocols:

- HTTP (application layer)
- HTTPS (application layer)
- TCP (transport layer)
- UDP (transport layer)

## Layer-4 Protocol

If Layer-4 protocol is used for forwarding, the cloud load balancer instance forwards the request directly to the backend instance without modifying any packets. When the cloud load balancer receives the request, it attempts to open a TCP connection with the backend instance on the port specified in the listener configuration.

## Layer-7 Protocol

If both frontend and backend connections use Layer-7 protocol for forwarding, the cloud load balancer resolves meaningful application layer content in the request and selects a backend CVM accordingly. Therefore, Layer-7 cloud load balancer must establish a connection with the client as a proxy of the backend CVM (three-way handshake) to receive the message containing real application layer content from client, and then determines the final choice of the internal CVM according to the specific fields in the message plus the server selection method set for the cloud load balancer.


Since the cloud load balancer is located between the client and CVM, the backend server access log only contains the IP address of the cloud load balancer. To check the actual IP address of the client, you need to use X-Forwarded-For request header. For more information, please see [Obtain Client IP](https://intl.cloud.tencent.com/document/product/214/3728).

### HTTPS Listener Security Mechanism

HTTPS is a secure HTTP connection that ensures the credibility of servers and clients by using SSL certificates. Cloud load balancer decrypts a request from a client with a certificate, and then sends the request to the backend instance. For more information, please see [How Does SSL Work](https://intl.cloud.tencent.com/document/product/214/4195).


## Difference between Layer-4 and Layer-7 Cloud Load Balancers
The difference between Layer-4 and Layer-7 cloud load balancers lies in whether Layer-4 information or Layer-7 information is used as the basis for determining the way of forwarding traffic when cloud load balance is performed on backend CVM.

Layer-4 cloud load balancer determines which traffic needs load balance based on Layer-3 IP address (VIP) and Layer-4 port number, performs NAT on the traffic to be processed, and then forwards it to the backend CVM.

Layer-7 cloud load balancer takes application layer's characteristics (such as HTTP header and URL) into account on the basis of Layer-4 cloud load balancer. For example, for the same Web server, in addition to determining the traffic to be processed based on VIP and Port 80, Layer-7 cloud load balancer can decide on whether to perform load balance based on URL, browser category and language at Layer 7. Layer-7 cloud load balancer is also known as "content exchange", which is designed to decide on the final choice of internal CVM based on the really meaningful application layer content in message and CVM selection method set for the cloud load balancer. To select CVM based on the real application layer content, the cloud load balancer must establish a connection with the client as a proxy of the final CVM (three-way handshake) to receive the message containing real application layer content from client, and then determines the final choice of the internal CVM according to the specific fields in the message plus the server selection method set for the load balancer. In this case, the cloud load balancer is more like a proxy server. The cloud load balancer establishes TCP connection with frontend client and backend CVM separately.




