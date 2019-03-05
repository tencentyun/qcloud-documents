## Purchase Channels

Users may purchase any types of cloud load balancer instances provided by Tencent Cloud in the following ways:

### Purchase on Console
Log in to Tencent Cloud [Cloud Load Balance Service Purchase Page](https://buy.cloud.tencent.com/lb) to purchase cloud load balance products.

### Purchae via API
Refer to [Cloud Load Balance API](http://cloud.tencent.com/doc/api/244/%E7%AE%80%E4%BB%8B) for details.

## Billing
The charges for cloud load balance service include instance rental fee and bandwidth traffic fee of backend servers. For example, if there is a CLB instance managing 3 CVMs, then the actual charges will include cost for the CLB instance and the cost for the 3 CVM instances (cost for instances will be accounted into network charges).

Cloud load balance is postpaid product. As long as the account is not in arrears, the system will not cancel cloud load balancer instances unless the user returns (deletes) them. When the account is in appears, cloud load balancer instances will be isolated by the system on 21st of the month, and reclaimed on 28th if the user does not renew the service. Once reclaimed, all binding relationships with backend servers will be disconnected.

>Note: When a CVM is isolated (Go into recycle bin for prepaid CVMs, or be in arrears for more than two hours for postpaid CVMs), its binding relationship with the LB will be terminated.  

## Pricing Overview
### Prices and Product Positioning of Cloud Load Balancer Instances
​
When purchasing public network application-based instances and public network instances with static IP, a balance of 30 yuan will be blocked (monthly cost). Please make sure your account balance is sufficient.

| Product Type | Price | Name | Definition | Target Scenario |
|---------|---------|---------|---------|---------|---------|
| Public network application-based cloud load balancer | 1 yuan/day |Cloud Application Load Balancer | Satisfies traffic balancing needs for medium to large sized complex websites. Able to provide advanced route balance capabilities based on Http request content (domain, URL path and so on). Supports HTTPS, HTTP protocol forwarding on the application layer.  | **Large-scale e-commerce and portal websites:** Suitable for web business with above tens to hundreds of millions of daily PV. Satisfies demand for route distribution between complex second level domains and business modules. </br> **Routing based on content:** If your application consists of different services, the application load balancer can route a request to a certain service based on the request content (domain, URL) </br>**Reduces DNS polling:** Reduces the number of second level domains significantly by forwarding paths via custom URLs, which will improve efficiency for accessing pages</br>**More accurate health check:** Able to determine the health status of second level domains/URLs, providing feedback regarding the status of running business with a higher granularity</br>**Supports HTTP/2:** HTTP/2 uses a single multiplexed connection, able to send multiple requests using the same connection. It can also compress header data and send the data in binary format, as well as connect clients using TLS.  |
| Public network (static IP) cloud load balancer | 0.147 USD/day | Cloud Load Balancer (with fixed IP address) | Satisfies 90% of traffic load balancing scenarios, it allows you to achieve higher level of application error tolerance and provides cloud load balance capacity needed for allocating application traffic with perfection. Suitable for medium to small sized websites and other businesses. Supports forwarding of HTTPS, HTTP, TCP, UDP and other protocols.  | **Suitable for medium to small sized websites:**Suitable for web businesses whose daily PV is below one million, with relatively simple service structure, few business modules and second level domains.<br>**Private protocol balancing:** The transport layer uses TCP listening to ensure that private protocols at your application layer can acquire reliable traffic balancing. For example: game service server request distribution uses IP session persistence to ensure that users are able to reconnect after being disconnected<br>**Persistent connection:** Satisfies demand of persistent TCP connections at the application layer (Http, websocket). For example, servers may exchange real-time information with end users with the help of WebSocket, in which case end users don't need to request (or poll) servers to provide update |
| Public network (without static IP) cloud load balancer | Free | Cloud Load Balancer (without fixed IP address) | Free trial product. No static public network IP, only supports layer 7 HTTP protocol forwarding, A Record and Cname binding are not supported | **Trial:** Helps new users learn and get familiar with the basic features of cloud load balancing</br>**Testing environment:** Used to create testing environment for traffic balancers. It is not recommended to use it as production system |
| Private network cloud load balancer | Free | Internal Cloud Load Balancer | Satisfies forwarding needs between internal modules within the user enterprise. Can only be accessed from within Tencent Cloud. Accessing via Internet is not supported. Supports TCP/UDP layer 4 protocols.  | **LAN service:**Used to forward requests between internal modules within the enterprise.  |

> Note: When a user cancels cloud load balance service in advance, the corresponding charges will be deducted from blocked balance in the user account according to the actual usage period. The remaining balance will be returned to the account.

### Cloud Load Balance Bandwidth Fee

#### Bandwidth Fee Billing Scenario
1) CVM is paid by bandwidth: Consumed bandwidth is public network bandwidth already contained in the CVM. No additional bandwidth fee will be charged;
2) CVM is paid by traffic: Public network cloud load balancer used by the user will cause traffic, which will incur a corresponding cost.
​
#### Bandwidth Fee Billing Standard
In the above mentioned scenario 2), the actual bandwidth fee for using CLB refers to the network fee incurred by backend CVMs. Please refer to [Network Billing](http://cloud.tencent.com/doc/product/213/%E8%B4%AD%E4%B9%B0%E7%BD%91%E7%BB%9C%E5%B8%A6%E5%AE%BD) for detailed billing methods.
