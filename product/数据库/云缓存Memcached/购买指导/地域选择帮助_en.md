Currently, Tencent Cloud offers a number of available regions: **East China (Shanghai), South China (Guangzhou), Hong Kong, North America**. Financial institutions and enterprises can apply for **Shanghai Finance Zone** by submitting a ticket.
**Note:**
1. Cloud products in the same region communicate with each other through private networks.
2. Cloud products in different regions cannot communicate with each other through private networks.
  1) CVMs in different regions can access each other through private networks. But a CVM cannot access Cloud Databases and Cloud Memcached in other regions.
  2) When binding load balance service to a CVM, you can only bind to a CVM in the same region.
  3) A CVM can access CVMs, Cloud Object Storages and Cloud Elastic Engines in other regions only through public network.
3. When purchasing cloud services, it is recommended to choose the region that is closest to your customer to minimize access latency and improve download speed.
4. Tencent Cloud provides post-paid CVMs and Cloud Databases only in Guangzhou. If you want to purchase CVMs and Cloud Databases in other regions such as Shanghai, you need to change the purchase mode to "Prepaid".
**Special Notes About Hong Kong Region:**
1. The following cloud services are available in Hong Kong: CVM, Load Balance, Cloud Database (CDB), Content Delivery Network (CDN), Mobile Acceleration, Cloud Monitor, Cloud Automated Testing (CAT), Cloud Security, Application Reinforcement, Key Factor, Fasion SDK Open Platform Payment API.
(Note: Only users in the whitelist can buy Cloud Database)
2. The following cloud services are temporarily unavailable in North America: Cloud Memcached, Cloud Elastic Engine (CEE), Cloud Object Storage (COS), Cloud Block Storage (CBS), One-click Start-up of Server and Binding of Domain by Regions and Servers.
3. When you need to log in to CVMs in Hong Kong, login via a jump server is recommended for a better operation and maintenance experience.
**Special Notes About North America Region:**
1. The following cloud services are available in North America: CVM, Cloud Database, Cloud Memcached, Load Balance, VPC, Content Delivery Network (CDN), Cloud Monitor, Cloud Security, Application Reinforcement, Key Factor.
2. The following cloud services are temporarily unavailable in North America: Cloud Block Storage (CBS), Cloud Elastic Engine (CEE), Cloud Object Storage (COS), Mobile Acceleration, Cloud Automated Testing (CAT), One-click Start-up of Server and Binding of Domains by Regions and Servers.
3. Due to the considerable latency between North America and China, when you need to log in to CVMs in North America region, login via jump server is recommended for a better operation and maintenance experience.
Note: The "interconnection over private network" mentioned above refers to the interconnection among resources under the same account. The private networks for the resources under different accounts are completely isolated from each other.
**Special Notes About Shanghai Finance Zone:**
Compliance zone customized according to regulatory requirements of finance industry features high level of security and isolation. Currently available services are CVM, finance database, Redis storage, face recognition, etc. Verified clients in finance industry can apply for the zone by submitting tickets. For more information, please see [About Finance Zone](http://cloud.tencent.com/doc/product/304/%E9%87%91%E8%9E%8D%E4%BA%91%E7%AE%80%E4%BB%8B).

