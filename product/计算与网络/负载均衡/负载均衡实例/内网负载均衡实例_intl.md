Private network cloud load balancer can only be accessed from within Tencent Cloud. Accessing via the Internet is not supported (without public network domain or public IP). The private network cloud load balancer properly allocates the requests sent from private network client to CVM to the CVM clusters via the corresponding VIP.

Private cloud load balancer routes the traffic to back-end CVM instances in the same region by using [Private IP Address](/doc/product/213/5225), and this is how internal CVM clusters are composed. If an application has a multilayer structure (for example, a Web server that can communicate with the Internet, and a database server that can only link with private network but cannot communicate with the Internet), you can design an architecture that can use both private network cloud load balancer instance and public network cloud load balancer instance. You can connect all the Web servers to the public network cloud load balancer instance, and connect the corresponding database server to the private network cloud load balancer instance. The public network cloud load balancer instance receives a request from the Internet and sends it to the back-end Web server which will process the request to the database and send it to the private network cloud load balancer. Then, the private cloud load balancer will route the request to the database server.

## Product Features

- Only Layer-4 forwarding (UDP, TCP) is supported
- Layer-7 forwarding (HTTP) is not supported
- Session persistence is not supported
- Heath check is not supported

## Usage Scenarios

- When there are multiple CVMs within Tencent Cloud and the requests from the client needs to be allocated to each CVM properly,
- When performing fault-tolerant and failure recovery operations for the private server clusters,
- When the service provider wants to block its physical IP address and provide transparent services to the client,

It is recommended to use private network cloud load balancer.

## Charges

Private network cloud load balancer instance is free of charge. 

## Creating Private Network Cloud Load Balancer Instance
For information on how to create a private network cloud load balancer instance, refer to [Creating Cloud Load Balancer Instance](/doc/product/214/6149).
