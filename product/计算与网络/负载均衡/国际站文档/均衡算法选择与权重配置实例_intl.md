
## 1. Comparative analysis of Cloud Load Balancing Algorithm

### 1.1. Weighted Round-Robin Scheduling

- **Principle**: Round-Robin Scheduling means dispatching requests to different servers in sequence in a round-robin approach. By performing i = (i + 1) mod n for each dispatching request, the i server will be selected. Weighted Round-Robin Scheduling is used to solve problems caused by performance inconsistency issues between servers. It uses corresponding weight values to represent each server's performance level and distribute requests to the servers according to these weight values and round-robin method. Servers with high weight values will receive connections first. They process more connections than those with low weight values. Servers with the same weight value will process the same number of connections.

- **Advantage**: This scheduling method is simple and practical. There's no need to record the statuses of current connections. It's a stateless scheduling method.

- **Disadvantage**: Weighted Round-Robin Scheduling is relatively simple but isn't suitable for situations where the service time of a request changes a lot, or where each request needs a different time length. In these cases, this round-robin scheduling will cause imbalanced load distribution among servers.

- **Applicable Scenario**: Back-end service time needed by each request is relatively identical, in which case load distribution situation would be optimal. This is commonly used for short connection services, such as HTTP, etc.

- **Recommendation to Users**: If users have known that each request costs basically the same amount of back-end service time, and that the RS (real server) processes requests of the same type or of similar types, it is recommended to choose Weighted Round-Robin Scheduling. Weighted Round-Robin Scheduling is also recommended when the time needed by requests varies little, because this scheduling method costs little resource, has no need for traversing and is highly efficient.

### 1.2. Weighted Least-Connection Scheduling

- **Principle**: In practice, each request service from the client may stay at the server for different time lengths. If a simple round-robin or random balancing scheduling method is used, the numbers of connection processes on each server may vary greatly as time passes by, which means load balance is not actually achieved. Weighted Least-Connection Scheduling is a dynamic scheduling method which estimates a server's load situation according to its current number of active connections. Opposite from Round-Robin Scheduling, Weighted Least-Connection Scheduling is a dynamic scheduling method which estimates a server's load situation according to its current number of active connections. The scheduler needs to record the number of established connections for every server. This number increases by 1 when a request is dispatched to the server, and decreases by 1 when a connection is terminated or is timed out. Based on Least-Connection Scheduling, Weighted Least-Connection Scheduling assigns different weight values to servers based on their processing performance, which allows the servers to receive a number of service requests according to their weight values. This method is an improved version of the original Least-Connection Scheduling.
　　1) Assuming that the weight values for back-end servers are w1, w2...wi, and their numbers of current connections are c1, c2...ci, the values of ci/wi are calculated in succession, and the RS with the smallest value will be the next one to which the request will be distributed.
　　2) If there are RSs with the same ci/wi value, the scheduling will be done using Weighted Round-Robin Scheduling.
	
- **Advantage**: This balancing method is suitable for request services that need a long time to process, such as FTP, etc.

- **Disadvantage**: Due to API restrictions, currently you cannot enable Least-Connection and session persistence at the same time.

- **Applicable Scenario**: Back-end service time needed by each request varies greatly. This is commonly used for persistent connection services.

- **Recommendation to Users**: When users need to process different requests and the back-end service time needed by these requests varies greatly (such as 3ms and 3s), it is recommended to use Weighted Least-Connection Scheduling to achieve load balance.

### 1.3. Source Hashing Scheduling (ip_hash)

- **Principle**: Use the source IP address of the request as Hash Key and find the corresponding server from the statically distributed hash table. The request will be sent to this server if the server is available and not overloaded, otherwise the response will be empty.

- **Advantages**: ip_hash can achieve similar effects of the session persistence feature by remembering the source IP, so that requests from a certain client can be constantly mapped to the same RS through the hash table. Thus, ip_hash can be used for scheduling in scenarios where session persistence is not supported.

- **Recommendation to Users**: Hash the source address of the request and dispatch request to a matching server according to server weight. This will allow all requests from the same client IP to be constantly dispatched to a certain server. This scheduling method is suitable for TCP protocols for cloud load balancer without cookie feature.

## 2. Choosing Load Balance Scheduling Method and Configuring Weight

According to the new features of the upcoming cloud load balancer, ***Layer-7 forwarding will support the Least-Connection balance method.*** In order to allow RS clusters to undertake business in a stable manner in different scenarios, we've provided several reference cases regarding how to choose cloud load balance scheduling method and configure weight.

- Scenario 1:
　　Suppose there are three RSs with the same configuration (CPU/RAM), since they have the same performance level, the user may configure their weight as 10. Now, each RS has established 100 TCP connections with clients. Then we add another RS. In this scenario, it is recommended for users to choose Least-Connection Scheduling, which will quickly distribute load to the fourth RS and lower pressure on the other three RSs.
　　
- Scenario 2:
　　Suppose a user has just begun to use Cloud Services, and the user website is relatively new and has low website load, it is recommended for the user to purchase RSs with the same configuration, because all RSs are identical access layer servers. In this scenario, the user can configure the weight for all RSs as 10 and use Weighted Round-Robin Scheduling to distribute traffic.

- Scenario 3:
　　Suppose a user uses 5 servers to satisfy the access need for a simple static website, and the ratio of their computing capability is 9:3:3:3:1 (calculated by considering their CPUs and RAMs): In this scenario, the user can set the weights of these RSs as 90, 30, 30, 30, 10, respectively. Most access requests towards static websites are short connection requests, thus, by using Weighted Round-Robin Scheduling, the CLB will distribute requests according to the performance ratio of the RSs.

- Scenario 4:
　　Suppose a user uses 10 RSs to support huge amount of Web access requests, and is not planning to purchase additional RSs in order to save cost,  and one of the RSs often restarts due to overload: In this scenario, it is recommended for the user to set up weight based on the performance levels of the RSs and set a relatively low weight value for the RS whose load is too high. In addition, the user can use Least-Connection cloud load balance method to distribute requests to RSs which have fewer active connections, in order to reduce pressure on the overloading RS.
　　
- Scenario 5:
　　Suppose a user uses 3 RSs to process several persistent connection requests, and the ratio of these servers' computing capability is 3:1:1 (calculated by considering their CPUs and RAMs).  In this case, the server with the best performance processes more requests. To avoid overloading, the user hopes to distribute new requests to idle servers. In this scenario, the user can use Least-Connection balance method and lower the weight of the busy server by a certain extent, after which CLB will distribute requests to RSs with fewer active connections, achieving a balanced load distribution.

- Scenario 6:
　　Suppose a user wishes that requests from subsequent clients can be distributed to the same server. However, Weighted Round-Robin or Weighted Least-Connection scheduling method cannot guarantee that requests from the same client will be distributed to the same server. In this scenario, in order to meet user's demand for specific application servers and ensure "stickiness" or "persistence" of client sessions, we can use ip_hash balance method to distribute traffic. This method ensures that requests from the same client are always distributed to the same RS. (Not including situations when there is a change in the number of servers, or the server becomes unavailable)

