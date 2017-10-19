
## Underlying Implementation

Tencent cloud load balance (CLB) currently provides load balancing services on layer 4 and layer 7. Tencent gateway (TGW), the unified gateway product launched by Tencent, will provide cloud load balance feature, with high reliability, scalability, high performance, strong anti-attack capability and so on. It supports large-scale concurrent access and prevents malicious attacking traffic. The product forms of CLB include: cloud load balance capabilities, converging public network IP, anti DDoS attacks, QoS, FTP and SIP support, etc.

Cloud load balance is deployed in clusters to enable session synchronization to eliminate server single point failure, improve redundancy and ensure service stability. A number of data centers are deployed in the same region to achieve local disaster recovery.

This chapter mainly introduces several key technical points of CLB and chooses different dimensions (platform, resource, business) to analyze which technologies CLB employs to realize the ability of tenant isolation, architecture disaster recovery, resource disaster recovery and anti-attack capacities of cloud platform.
> Note: In this document, RS refers to the CVM that is bound with CLB. VIP refers to the IP address of the CLB for external service.

### Tenant Isolation

One of the key features of cloud platform is tenant isolation. Typically, users who access the cloud don't want their business to be affected by others; at least their business should be isolated on the network so others cannot access their machine. Of course, there are many ways to realize this feature in the industry, among which the most common one is isolation on the hardware level through the use of specific connection switch and vxlan protocol to achieve isolation. The downside:
1. A special switch is needed;
2. Additional equipment is needed to establish connection between vxlan network and ordinary network, which will cause the problem of single point;
3. Poor compatibility with existing network environment.
For the above reasons, we adopted the software solution, realizing tenant isolation via IP tunnel + VPC.

![](//mccdn.qcloud.com/static/img/cf8f46731a218bf7fef43843eef0d4e4/image.png)

From the left side of the figure, we can see that the interaction between CLB and RS uses the IP tunnel method; CVM (RS) allocates the actual private network IP, and the connection to the physical network is established. The advantage is that it's easy to achieve, and is compatible with the previous physical machine solution, but the drawback is:
1. It requires additional modules to achieve tenant isolation;
2. Private network IPs cannot be reused between tenants, thus unable to achieve free networking;
3. Since IP is unique in the private network, RS IP must be changed when migrating, which means hot migration cannot be achieved.

For the above reasons, Tencent Cloud developed VPC. In the right side of the figure, you can see that the same tenant is assigned a VPCID, and the client may perform free networking within the VPC; the tenant network itself is isolated, and the specific processing is done by the vpc.ko kernel module.

### IP Convergence

Speaking of cloud load balance, the most famous one in the industry is LVS (Linux Virtual Server) technology.

LVS has three modes: DR mode, NAT mode and TUNNEL mode. The main restriction of DR mode is that LVS and RS must be in the same vlan, which means deployment is very limited and scalability is poor. The main drawback of NAT mode is that returned data packets for RS need to use default route, and there is also scalability problem. Therefore, we initially built LVS clusters using the TUNNEL mode. However, TUNNEL mode requires that each RS is assigned one public network IP. For Tencent Cloud and services with considerable amount of RS, public network IP is a big challenge.

For the above reasons, CLB is created.

The following figure is a diagram of previously used LVS solution and CLB solution. The main difference is:
1. CLB does not need to assign public network IP to RS, achieving IP convergence;
2. Outbound traffic still go through CLB. It's easier to locate problems; in addition, closed-loop is formed for service traffic, playing the role of bridgehead.
![](//mccdn.qcloud.com/static/img/e4575f5f414666505d8c1a7cdea2c6f0/image.png)

### Highly Reliable Implementation

High reliability is an important metric for cloud services. In order for CLB to achieve a highly reliable service, we carried out the following solutions:
1. Cluster disaster recovery;
2. Session synchronization;
3. Resource isolation;
4. Anti-DDos.

#### Cluster Disaster Recovery and Session Synchronization

To put it simple, cluster disaster recovery means that the failure of one server in a cluster will not affect the service capabilities of the entire cluster. The traditional cluster disaster recovery uses HA mode (vrrp protocol) and common open source solutions include LVS. The drawbacks of traditional method include: only half of the servers in a cluster can work simultaneously, while the other half of the machines are in cold backup state; switching speed after a crash is relatively slow.

This issue is taken into account at the very beginning of CLB design process. It uses ospf dynamic routing protocol to achieve cluster disaster recovery; if a machine fails, ospf protocol can ensure that the machine is removed from the cluster within 10 seconds. CLB puts one cluster under two connection switches and ensures cross-rack disaster recovery, so that failure of a single switch or power failure of a single rack will not affect the services of the cluster.

Cluster disaster recovery guarantees the availability of CLB clusters, but for a client, if the server crashes, the removal of the machine can only guarantee that new connections will not go to this machine. But persistent connections will be disconnected. To solve this problem, we realized a periodic session connection synchronization within the cluster. With this, other servers that take over the packets from the faulty machine can find the correct session and ensure service availability.

![](//mccdn.qcloud.com/static/img/4cdd6084a39561e04539a8866374bb24/image.png)

LVS solution: Synchronizes when the connection status changes; when both persistent and short connections exist, synchronization traffic for short connection services can be very large, which will impact normal forwarding.
CLB solution: Synchronize after 5 seconds when each connection is established; Does not synchronize if connection is within 5 seconds. Only "persistent connections" are synchronized.

![](//mccdn.qcloud.com/static/img/397479668381a345c8bae877e4aa4ff3/image.png)

#### Resource Isolation

The resource isolation feature is to protect other services from being affected when the CLB is under high load as individual service is attacked.

This is realized by regularly (5s) checking whether CLB has reached the configured warning level for high load; if so, resource isolation is activated, and CLB will check the traffic, number of packets, number of connections for each service. Those above the limit will be discarded, so as to ensure that the load of CLB server will not reach the actual limit which would otherwise affect other services. Normally, resource isolation function is disabled. It is guaranteed to activate within 5 seconds when service volume suddenly increases, or a service is attacked which caused CLB to reach the warning level, to ensure that normal service forwarding is not affected.

Resource isolation adopts the classic token bucket algorithm. The process is: regularly place a certain amount of tokens to the bucket, and each arriving packet consumes a token. If tokens are exhausted in a period of time, packets will begin to be discarded.

![](//mccdn.qcloud.com/static/img/86cd36ef04f3200b8d0c591b0c4e7675/image.png)

#### Anti DDos

Cluster disaster recovery and resource isolation are both meant to protect the CLB platform itself. However, when a single service is attacked, this service will be damaged for sure. CLB will not allow this to happen. Tencent Cloud has a very powerful Dayu system to protect services from DDos attacks. But the checking duration of Dayu Aegis system is 10 seconds, which means the client's RS can be already crashed before Dayu system goes into effect. In order to solve problems within this 10 seconds, we have developed the synproxy feature.

Realization: when receiving the three-step handshake request from the client, CLB executes three-step handshake as a proxy without disturbing RS before the arrival of the packet; once the first packet arrives, CLB will cache it and then execute a three-step handshake with RS. If the handshake is a success, the cached data will be sent to RS, and the subsequent process is to transmit the packet in a transparent manner. This will ensure that DDos attacks will not reach RS. CLB will take care of the pressure instead. CLB itself has relatively strong load capacity, plus its cluster mode and the ability to isolate resources, it is difficult to crash the CLB machine within 10 seconds under normal circumstances.

![](//mccdn.qcloud.com/static/img/5c96f1c2548dd15bd00d0ff01b63eddf/image.png)

## Features of Different Types of Tencent Cloud Load Balancers

CLB currently offers three types of services:
- Layer 4 cloud load balance corresponding to listener's tcp and udp;
- Layer 7 cloud load balance, for public network CLB service without daily rate;
- Layer 7 cloud load balance corresponding to listener's http/https capabilities.

### Layer 4 Cloud Load Balance

Layer 4 cloud load balance is the earliest solution CLB has ever achieved and is also a necessary feature for a cloud load balance product. The basic principle is to distinguish different services via ports in the CLB; the key of forwarding rule is vip:vport:protocol. Currently this cloud load balance mode is the most commonly used one in Tencent Cloud. However, VIP belongs to the same developer, and traffic from different developers are strictly isolated.

![](//mccdn.qcloud.com/static/img/bb969f908e3931c61267c316e6e4f909/image.png)

## Public Network Cloud Load Balancer without Daily Rate

This type without daily rate was originally designed for meeting the demand for a large number of web and mobile games. Such games have two main features:
1. Separated regions and servers. Each region needs at least one vip and certain games with hundreds of servers require hundreds of public network vips, causing a substantial waste of public network vips;
2. Web games need to use port 80, but layer 4 cloud load balancer cannot reuse IPs.

In order to solve this problem, we proposed a solution without daily rate; the specific connection method is to add a domain dimension in the rule key.

![](//mccdn.qcloud.com/static/img/e9d4ed8a62b76264f811d6b0dbf24c2e/image.png)

### Layer 7 Cloud Load Balance

The solution without daily rate can cope with ordinary layer 7 cloud load balance services, but layer 7 users who require session and cookie have to build their own nginx to perform an extra reverse proxy, which can be a waste of resources and affect reliability.

![](//mccdn.qcloud.com/static/img/6d385cd8c23ca392c36540eff8689e5c/image.png)

Two solutions were discussed regarding the design of layer 7 cloud load balance at the beginning:
1. Public network IP is directly applied to nginx machines, building a nginx cluster
2. The nginx cluster is connected under layer 4 CLB

The weakness of solution 1 is that it's totally vulnerable to DDos attacks. For Tencent Cloud, a VIP is required to connect to layer 4 and layer 7 at the same time, which is beyond the capacity of solution 1, thus we finally adopted solution 2. Dynamic capacity scaling is another advantage of solution 2, which helps satisfy demands in scenarios when rapid capacity increase is required by services.

However, nginx achieves cloud load balance through the use of reverse proxy and there is a fatal problem in Tencent Cloud: since vpc network is a virtual network, which relies on the parent machine to establish a connection to the physical network, nginx reverse proxy cannot be used directly between layer 7 LD and RS. Therefore, we came up with the idea of simulating layer 4 and adding 17.ko kernel module on layer 7 LD which is responsible for encapsulating the gre tunnel and IPIP tunnel for interaction with RS.

![](//mccdn.qcloud.com/static/img/9874ed32509218619ef4cea119bc3790/image.png)




