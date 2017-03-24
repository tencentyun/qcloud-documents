## Multiple Availability Zones for Cloud Load Balancer


The cloud load balancer (CLB) supports disaster tolerance across availability zones. For example, multiple clusters are deployed in two availability zone (of one region) in Shenzhen Finance Zone I and II to achieve disaster tolerance across availability zones in one region. This capability allows the cloud load balancer to forward the front-end access traffic of one availability zone to other availability zones in the same region within 10 seconds to restore service capabilities in case of failure of the former available zone


---


## Q & A

Q1: Shenzhen Finance Zone I and II share a cloud load balancer test1. What is the strategy of public network inbound traffic for the client?

- A: There is a pair of IP resource pools at data centers of Shenzhen Zone I and II, which can be understood as peering IP resources. Developers do not need to distinguish between the master cluster and the backup cluster, for both of them have equal cloud load capacity. When the developer buys a cloud load balancer and binds it to the CVM, it generates two sets of rules to write the cluster, and it has gained high availability.

Q2: Shenzhen Finance Zone I and II share a cloud load balancer test1, whose back-end binds 100 CVMs at each availability zone of I and II. 1 million HTTP persistent connections (TCP connection not closed) are established when the business is in operation. If the cloud load balancer clusters in Finance Zone I all break down at this point, what will happen to the business?

- A: When the cloud load balancers in Finance Zone I fail, all persistent connections will be disconnected and short connections will not be affected. The disaster tolerance system will automatically bind the 100 CVMs in Zone I to the load balancer in Zone II within 10 seconds. The business capability is immediately restored without manual intervention.


Q3: Which type of CLB is compatible with the capability of "disaster tolerance across availability zones"? Do I need to pay extra for such capability?

- A: This capability is currently free of charge. It is compatible with the application-based CLB and the public network (with static IP) CLB. It also supports http/https/tcp/udp and other protocols.


