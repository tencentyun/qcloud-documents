Polling refers to the scheduling algorithm with which load balancer distributes traffic to [RS](/doc/product/214/6095). Different polling methods combined with different weight configurations on the RS lead to different outcomes.

## Weighted Round-Robin Scheduling

Weighted Round-Robin Scheduling means dispatching requests to different servers in sequence by use of polling. Weighted Round-Robin Scheduling is used to solve problems cause by performance inconsistency between servers. It uses appropriate weight values to represent each server's performance level and assign requests to servers according to these weight values and polling method. Servers with high weight values receive connections first. They process more connections than those with low weight values. Servers with the same weight value process the same number of connections.

- **Advantage**: This scheduling algorithm is simple and practical. It's a stateless scheduling method because there is no need to record the statuses of current connections.

- **Disadvantage**: Weighted Round-Robin Scheduling is relatively simple but is not suitable for situations where the service time of a request changes a lot, or where each request needs a different time length. In these cases, this round-robin scheduling will cause unbalanced load distribution among servers.

- **Application Scenario**: Backend service time needed by each request is relatively identical, in which case load distribution is optimal. This is commonly used for short connection services, such as HTTP, etc.

- **Recommendation**: If users have known that each request takes basically the same amount of backend service time, and that the RS processes requests of the same type or of similar types, it is recommended to choose Weighted Round-Robin Scheduling. Weighted Round-Robin Scheduling is also recommended when the time needed by requests varies little, because this highly efficient scheduling method consumes little resources with no need for traversing.

## Weighted Least-Connection Scheduling

In practice, each request service from the client may stay at the server for a different time length. If a simple polling or random load balancing algorithm is used, the numbers of connection processes on each server may vary greatly over time, which means load balance is not actually achieved.

Weighted Least-Connection Scheduling is a dynamic scheduling algorithm which estimates a server's load condition according to its current number of active connections. Opposite to Round-Robin Scheduling, Weighted Least-Connection Scheduling is a dynamic scheduling algorithm which estimates a server's load condition according to its current number of active connections. The scheduler needs to record the number of established connections for every server. This number increases by 1 when a request is dispatched to a server, and decreases by 1 when a connection is terminated or has timed out.

Based on Least-Connection Scheduling, Weighted Least-Connection Scheduling assigns different weight values to servers based on their processing performance, which allows the servers to receive a number of service requests according to their weight values. This method is an improved version of the original Least-Connection Scheduling.

1. Suppose the weight values for RS instances are w1, w2...wi, and their numbers of current connections are c1, c2...ci. The values of ci/wi are calculated in succession, and the RS instance with the smallest value will be the next one to which the request is allocated.

2. If RS instances with the same ci/wi value exist, the scheduling is done using Weighted Round-Robin Scheduling. 
	
- **Advantage**: This load balancing algorithm is suitable for request services that take a long time to process, such as FTP, etc.

- **Disadvantage**: Due to API restrictions, you cannot enable Least-Connection and session persistence at the same time.

- **Application Scenario**: Backend service time needed by each request varies greatly. This is commonly used for persistent connection services.

- **Recommendation**: When users need to process different requests, and the backend service time needed by these requests varies greatly (such as 3 ms and 3 sec), it is recommended to use Weighted Least-Connection Scheduling to achieve load balance.

## Source Hashing Scheduling (ip_hash)

Use the source IP address of the request as Hash Key and find the corresponding server from the statically assigned hash table. The request is sent to this server if the server is available and not overloaded, otherwise the response is empty.

- **Advantage**: Requests from a certain client can be constantly mapped to the same RS through the hash table. Therefore, a simple session persistence can be achieved by use of ip_hash in scenarios where session persistence is not supported.

- **Recommendation**: Hash the source IP of a request and dispatch the request to a matching server according to RS weight. This allows all requests from the same client IP to be constantly dispatched to a certain server. This scheduling method is suitable for TCP protocols without cookie feature.

## Choosing Load Balancing Algorithm and Configuring Weight

To allow RS clusters to undertake business in a stable manner in different scenarios, we provide the following reference cases regarding how to choose load balancing algorithm and configure weight.

- Scenario 1:
  If there are three RS instances with the same configuration (CPU/RAM), you may configure their weight as 10 because they have the same performance level. Each RS has established 100 TCP connections with clients, in which case you need to add another RS. In this scenario, it is recommended that you use Least-Connection Scheduling to quickly assign load to the fourth RS and lower the pressure on the other three servers.
  
- Scenario 2:
  Suppose you have just begun to use cloud services, your website is relatively new with low website load. In this case, it is recommended that you purchase a RS with the same configuration, because RS instances are identically the same access layer servers. In this scenario, you can configure RS weight as 10 and use Weighted Round-Robin Scheduling to distribute traffic.

- Scenario 3:
  You use 5 servers to satisfy the access need for a simple static website, the ratio of their computing capability is 9:3:3:3:1 (calculated based on their CPUs and RAMs). In this scenario, you can set the weights of these RS to 90, 30, 30, 30, 10, respectively. Since most access requests towards static websites are short connection requests, you can use Weighted Round-Robin Scheduling to allow the load balancer instance to assign requests according to the performance ratio of each RS.

- Scenario 4:
  You use 10 RS to support huge amount of Web access requests, and are not planning to purchase additional RS to save cost. One of the RS often restarts due to overload. In this scenario, it is recommended that you set the weight based on the performance level of each RS and set a relatively low weight value for the RS whose load is too high. In addition, you can use Least-Connection load balancing algorithm to assign requests to RS with fewer active connections to reduce the pressure on overloading RS.
  
- Scenario 5:
  You use 3 RS to process several persistent connection requests, the ratio of these servers' computing capability is 3:1:1 (calculated based on their CPUs and RAMs). In this case, the server with the best performance processes more requests. To avoid overloading, you wish to assign new requests to idle servers. In this scenario, you can use Least-Connection load balancing algorithm and lower the weight of busy servers as appropriate. This allows load balancer to assign requests to RS with fewer active connections to achieve load balance.

- Scenario 6:
  Suppose you want the requests from subsequent clients to be assigned to the same server. However, neither Weighted Round-Robin nor Weighted Least-Connection scheduling method can guarantee that requests from the same client are assigned to the same server. In this scenario, in order to meet your requirements for specific application servers and ensure "stickiness" or "persistence" of client sessions, we can use ip-hash load balancing method to distribute traffic. This ensures that requests from the same client are always distributed to the same RS. (Not including the situations where the number of servers changes, or the server becomes unavailable)

