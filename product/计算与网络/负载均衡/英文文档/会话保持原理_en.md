
## What is Session Persistence?

Session persistence is one of the most common issues with cloud load balancer, and it is also a relatively complex one.  Session persistence is sometimes called Sticky Sessions.  Session persistence refers to a mechanism on the cloud load balancer that can identify the association between the client and the CVM during interaction, ensuring that a series of associated access requests keep allocating to a single server while performing cloud load balance. 


## When do I need session persistence? 
Before discussing this problem, we must take the time to figure out some concepts: what is a Connection, what is a Session, and the difference between the two.  It is important to note that if we are only talking about cloud load balance, sessions and connections usually have the same meaning. 

From a simple perspective, if the user needs to log in, then you can simply regard it as a session; if the user does not need to log in, then it is a connection. 

For packets in the same connection, cloud load balancer will perform NAT translation before forwarding them to a specific backend CVM for processing.  The cloud load balance system contains a specific table to record the status of these connections, including "Source IP: Port", "Destination IP: Port", "Server IP: Port", Idle Timeout, and so on.  Because the table recording the connection status internally on cloud load balancer consumes the system's memory, it cannot be infinitely large, and all traditional manufacturers will face some restrictions.  The size of this table is generally called the maximum number of concurrent connections, that is, how many connections the system can accommodate at the same time.  In items of the current connection status table on cloud load balancer a parameter of Idle Timeout is designed.  When a connection has no traffic during Idle Timeout, the cloud load balancer automatically deletes this connection entry and frees the system resources. 

After the connection is deleted, the client's request will not certainly be sent to the same backend CVM; instead, the CLB's traffic distribution policy prevails. 

In some situations where login is required, a session is required between the client and the server to record various information on the client.  For example, in most e-commerce applications or online systems that require user authentication, a client often go through several interactions with the server to complete a transaction or a request.  Since these interactions are closely interrelated, in a certain interactive step of these interactions, the server often needs to know the result(s) from the last or last few interactions, which in turn requires that all of these associated interactions be completed by one server and cannot be distributed by the cloud load balancer to a different server.  Otherwise, abnormalities may occur: 

- The client entered the correct user name and password, but was repeatedly redirected to the login page; 
- The user entered the correct verification code, but was always alerted to verification code error; 
- Items that the client puts into the shopping cart were lost 
- ...

The significance of the session persistence mechanism is therefore to ensure that requests from the same client are forwarded to the same backend CVM for further processing.  In other words, the connections established between the client and the server are sent to the same server for processing.  If a cloud load balancer is deployed between the client and the server, it is likely that the multiple connections will be forwarded to different servers for processing.  If there is no session information synchronization mechanism between servers, other servers may not identify the user's identity, resulting in exception on interaction between the user and the application system. 

Cloud load balancer is to have the connections and requests from clients evenly forwarded to multiple CVMs to avoid overload of a single CVM; while the session persistence mechanism requires that certain requests be forwarded to the same server.  Therefore, in the actual deployment environment, we have to select the appropriate session persistence mechanism according to the characteristics of the application environment. 

## Session Persistence Category
### Simple Session Persistence (Layer-4 Session Persistence) 
Simple Session Persistence (also known as source address-based session persistence or IP based session persistence) means that the cloud load balancer uses the source address of the access request as the basis for determining the associated session.  All access requests from the same IP address are delivered to a same CVM during cloud load balancing. 

A very important parameter in a simple session persistence is the connection timeout value; the cloud load balancer sets a time value for each session that is in a persistent state.  If the interval of a session from the last completion to the next iteration is less than the timeout value, the cloud load balancer will have the new connection persisted for the same session; but if the interval is greater than the timeout value, the cloud load balancer will regard the new connection as a new session and perform cloud load balancing. 

It's easy to implement simple session persistence, which requires only layer-3 or 4 information of packets, the efficiency being high. 
![](//mccdn.qcloud.com/static/img/c9e0a755c805cbf864063d12101ca387/image.png) 

However, the problem with this approach is that when multiple clients access the server through proxy or address translation, the requests are delivered to the same server due to the same source address, resulting in a serious imbalance between servers. 

In another situation, when a same client generates a large number of concurrent requests to multiple servers for further processing, session persistence occurs.  In this case, the source address based session persistence will also lead the cloud load balancer to failure. 

In above situations, we must consider using other ways for session persistence. 

### Session Saving Session Persistence

This method implements session persistence during cloud load balancing by sharing session between multiple backend servers.  It mainly takes the following forms: 

1) Database Storage 

Session information is stored in the database table to achieve session information sharing between different application servers.  This method is suitable for sites with few database access. 

- Advantages: Easy to implement
- Disadvantages: Because the database server is more expensive and more difficult to scale out than the application server, For Web applications in high concurrency, the biggest performance bottleneck is usually in the database server.  So if session is stored in the database table, you service may be affected due to frequent database operations. 

2) File System Storage 

Sharing session between various servers is achieved through a file system (such as NFS).  This method is suitable for sites in low concurrency. 
- Advantages: For each server, only disks saving the Session are to mount, which is easy to implement. 
- Disadvantages: NFS can't provide high performance for high concurrent read and write, and has huge bottleneck in the hard disk I/O performance and network bandwidth, especially in frequent read from and write to such small file as Session. 

3) Memcached Storage 

Use Memcached to save Session data which is read directly from the memory. 
- Advantages: high efficiency, as read and write will be much faster than that stored in a file system, and sharing Session between multiple servers is more convenient; these servers are simply configured to use the same group memcached server, reducing the additional workload. 
- Disadvantages: Data in the memory will be lost in case of a crash, but it is not a big deal for the Session data.  If the site has very large traffic which causes too many sessions, memcached will delete the uncommonly used part. However, if the user continues to use after a period of time, read failure will occur. 

### Cookie-based Session Persistence (Layer-7 Session Persistence) 

In the cookie based mode, CLB is responsible for inserting cookies without making any modification to backend CVM.  When the client makes the first request, the client HTTP request (without cookie) is directed to CLB, which then selects a backend CVM basing on load balancing algorithm policy and sends the request to the CVM. Then CVM's HTTP response (without cookie) is sent back to CLB.  After that, the CLB inserts a cookie into the backend CVM and returns the HTTP response to the client. 

When the client makes the second request, the client HTTP request containing the cookie inserted by CLB last time is directed to CLB, which then reads the session persistence values in the cookie and sends the HTTP request (with the same cookie as above) to the specified CVM. Then the backend CVM gives a response, and because the CVM does not write the cookie, the HTTP response does not contain the cookie. When the HTTP response flows into the CLB again, the updated session persistence cookie will be written to CLB. 

Tencent Cloud CLB layer 7 session persistence is implemented exactly basing on such a cookie insertion method. 

![](//mccdn.qcloud.com/static/img/ce7f9a6157fe9492469d1d8fb253736d/image.jpg)
