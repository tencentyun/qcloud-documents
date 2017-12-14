
## What is Cloud Load Balancer?
Cloud Load Balancer is a traffic delivery service for multiple [CVMs](/doc/product/213/495). Cloud load balancer can extend application systems' external service capabilities through traffic delivery and improve their availability by eliminating single point of failure.

The Cloud Load Balance service virtualizes multiple CVM resources located in the **same region** into a high-performance, high-availability application service pool by setting a virtual service address (VIP), and delivers the network requests from the client to the CVM pool in a way specified by the application.

Cloud Load Balance can check the health of CVMs in the CVM Pool, and automatically isolate abnormal CVMs, thus dealing with the single point of failure (SPOF) of a single CVM and improving the overall service capability of applications.

Tencent Cloud Load Balance provides self-management, self-troubleshooting, anti-network attacks and other advanced features for enterprises, communities, e-commerce, games and other user scenarios.

## Components
A cloud load balancer group that provides services typically consists of the following components:

- CloudLoadBalancer: A cloud load balancer instance for traffic delivery
- VIP (virtual IP): An IP address through which the cloud load balancer provides service to the client
- Backend/Virtual Server: A group of cloud load balancer instances on the backend for processing requests
- VPC/Basic network: The overall network environment

Access requests from other servers other than cloud load balancer is delivered through the cloud load balancer instance to the backend CVM for processing according to the associated policies and forwarding rules.

## Glossary
| Term | Full Name| Description |
|---------|---------|---------|
| Cloud Load balancer | Cloud Load Balancer | A network cloud load balance service provided by Tencent Cloud that can be combined with CVM to offer cloud load balance service based on TCP/UDP and HTTP |
| Load Balance Listener | Load Balance Listener | Including listening port, load balance policy and health check configuration, each item to be listened corresponds to a back-end application service |
| Back-end Server | Real Server | A group of CVM instances that accept load balance delivery requests. The cloud load balancing service forwards access requests to this group of back-end CVMs according to user-defined rules |
| Virtual Service Address | Virtual IP | The service address assigned by the system, which is currently the IP address. Users can choose whether to expose the service address to the public, in order to create a public/private network cloud load balancing service |

## How Does Cloud Load Balancer Work?
## Working Principle

The cloud load balancer accepts incoming traffic from the client and routes the request to a back-end CVM instance in one or more available zones for processing.

Cloud Load Balance service is mainly provided by cloud load balancer listener. The listener is responsible for monitoring requests on the cloud load balancer instance, delivering policies to back-end CVMs and other services. By configuring the forwarding protocols and protocol ports of "client-cloud load balancer" and "cloud load balancer-backend CVM", cloud load balancer can forward the request directly to the back-end CVM.

It is recommended that you configure a back-end CVM instance of the cloud load balancer across multiple available zones. If an available area becomes unavailable, the cloud load balancer routes the traffic to other available zones for normal operation, thereby shielding off the service interruption caused by a single available zone failure.

### Request Routing Selection

The client requests to access the service through domain name. Before the request is sent to the cloud load balancer, the DNS server will resolve the load balancing domain name and return the requested CVM IP address to the client. When the cloud load listener is requested, a different cloud load balancing algorithm will be used to deliver the request to the back-end CVM. Tencent Cloud currently supports Weighted Round-Robin and ip_hash balancing algorithms. It will support the Weighted Least-Connection Scheduling in the future.

### Monitoring Back-end Service Status

The cloud load balancer also monitors the running status of back-end instances, so as to ensure that traffic is only routed to the normal running instance. When the cloud load balancer detects an abnormal instance, it stops routing traffic to that instance until the instance is detected to return to normal again.


## Related Services

Cloud Load Balance can be used with the following services to improve application availability and scalability:

- CVM Instance: enables the application to run on the cloud virtual server. For more information, refer to [CVM Product Documentation](https://cloud.tencent.com/doc/product/213).
- Auto Scaling: Controls the number of instances flexibly. When a cloud load balancer instance is enabled in Auto Scaling, the scaled instance is automatically added to the cloud load balancing group, and the terminated instance is automatically moved out of the cloud load balancing group. For more information, see [Auto Scaling Product Documentation](https://cloud.tencent.com/doc/product/377).
- Cloud Monitor: Helps you monitor the running status of cloud load balancer and all back-end instances and perform the operations accordingly. For more information, refer to [Cloud Monitor Product Documentation](https://cloud.tencent.com/doc/product/248).
- Domain Name Registration and Resolution: Quickly and easily route requests to cloud load balancer instances by converting your custom domain name (e.g. `www.example.com`) to an IP address (e.g. ` 192.0.2.1`) for network communication. 



