CPM is an on-demand physical bare metal rental service provided on cloud on a pay-by-usage basis.  </br>Compared with self-built data center, CPM allows you to build your private cloud faster, with Tencent Cloud providing interconnection between data center private　networks as well as VPCs, BM　load balancers, NAT gateway, operation and maintenance, monitoring, security protection and other capabilities. What you need to do is just specifying the configuration and number of CPMs, and　the time consumed in CPM　deployment and delivery will be shortened to 4 hours. If your business is sensitive to performance, you're recommended to use CPM for a more powerful computing capability without any compromise on performance.

## Game Applications
MMORPG (Massive Multiplayer Online Role-Playing Game) is very popular among players for its brilliant pictures, grand scenes and a wide variety of play rules and scenarios. In particular, its large-scale cross-server activity has attracted many players, with all the players in the same region being visible to each other and all of their operations broadcasted within the view. The participation of large number of players poses an extraordinarily high requirement for the load, stability and network of the access servers.

![](http://mc.qcloudimg.com/static/img/77625f46c7c3c971cc9f7e785eb81103/image.png)


>Step 1: Purchase high-performance CPMs to deploy battle logic modules and make use of the physical bare metals to deal with scenarios with high I/O and high PPS. </br>Tencent Cloud data center is equipped with security protection modules that can prevent attacks such as DDoS and Cc to ensure the security of CPMs.</br>
Game applications feature a short life cycle, and a large number of servers need to be put into service during peak hours. With Tencent Cloud's large resource pool, a rapid scale-up can be achieved rapidly. At the end of the life cycle of application during which a game company is faced up with many problems such as withdrawal and devaluation of resources, CPMs based on a pay-as-you-grow and pay-by-usage model can be used to change the cost structure of the game company to reduce the TCO (Total Cost of Ownership).


## Government and Enterprise Applications
Security is a major consideration for government and enterprise applications, which takes exclusiveness, high performance and ease of scale-up as the top priority in the OLTP and big data processing scenarios. 

![](http://mc.qcloudimg.com/static/img/441357f140bc237ff9d7a76b3c09af9c/image.png)

><li>Step 1: In the virtual cloud zone, purchase CVMs to deploy your Web Servers to process user requests. All the CPM instances are deployed in an auto scaling group so that auto scaling can dynamically adjust the scale of instances based on the conditions defined by you. After auto scaling is deployed, the number of CPM instances can automatically increase during peak hours of visits to ensure availability. When the volume of visits falls, the instances will be automatically destroyed to save costs.</li></br>
<li>Step 2: Purchase high-performance CPMs to acquire an exclusive physical cluster within 4 hours. CPM uses the VPC based on switch controller to ensure the access isolation among different tenants to meet the data security requirements. Tencent Cloud's large resource pool allows rapid scale-up to guarantee the security and scalability.</li></br>
<li>Step 3: Connect to the out-of-band network via SSL VPN to remotely operate and maintain CPMs. Tencent Cloud can identify and deal with hardware failures in a timely manner, and replace the faulty hardware to recover service rapidly.</li>

## LVB Applications
Barrage scenes in Live Video Broadcasting (LVB) have a very high requirement for network bandwidth and server performance because every barrage message needs to be pushed in real time to all the users in an LVB room. During peak hours, there may be hundreds of millions of long URLs, with the bandwidth for a single machine being up to several gigabytes.

![](http://mc.qcloudimg.com/static/img/5e66d6b05719335a0a3c8c57993bfcf5/image.png)

><li>Step 1: In the virtual cloud zone, deploy the frontend access service on the CVMs to receive the barrage messages sent by users. With auto scaling capability, the number of CVMs can automatically increase during peak hours of visits to ensure availability. When the volume of visits falls, the CVMs will be automatically destroyed to save costs.</li></br>
<li>Step 2: In BM physical cloud zone, CPMs are responsible for the barrage push module. After receiving barrage messages, CVMs push them to the CPM cluster via hybrid cloud at private network level, and then the CPMs pushes the received barrage messages to the EIP cluster. During peak hours, a single CPM needs to maintain hundreds of millions of long URLs and generate as high as several gigabytes of bandwidth.</li></br>
<li>Step 3: Barrage messages are presented to the LVB viewers in real time via a dedicated EIP cluster.</li>


