According to users' stress test experiences, this document summarizes common performance issues of stress tests, and provides users with troubleshooting solutions and suggestions for stress test.

## Stress Test FAQ

### 1. The public network traffic is not enabled for backend CVMs
When you purchase a CVM, if public network traffic is not enabled, the CVM may fail to forward when the public network cloud load balancer is mounted.
### 2. Bandwidth of Backend CVM is Insufficient
If the set bandwidth for the backend CVM is too low, the backend server cannot send packets back to the LB when the bandwidth exceeds the set threshold, and LB will return 504 and 502 to the client.
### 3. Insufficient Client Ports 
If there are too few clients or the port range of the client is too small, it may fail to establish the connection due to insufficient ports. In addition, if the keep_alive field is greater than 0 when a persistent connection is established, the connection will always occupy the port, thus resulting in insufficient client ports.
### 4. Applications Depended by Backend CVM Become a Performance Bottleneck
After the request reaches the backend server through cloud load balancer, the backend server itself is normally loaded, but because all applications on the backend server depend on other applications such as databases, performance bottlenecks in the databases may also affect the performance of stress test.
### 5. The Health Status of the Backend Server is Exceptional
The health status of the backend server tends to be ignored when performing stress test. If there is a health check failure or unstable health check status (sometimes good, sometimes bad and changing repeatedly) for backend server, it may lead to low performance of stress test.
### 6. Session Persistence is Enabled for Cloud Load Balancer, Resulting in Uneven Backend CVM Traffic Distribution
After a session persistence is enabled for cloud load balancer, it is easy to cause the request to fall on several fixed backend servers. As a result, the traffic distribution is uneven and the performance of the stress test is affected. It is recommended to disable session persistence when performing stress tests.

## Suggestions for Stress Tests

Note: The following settings are only used for stress tests of cloud load balancer, and are not required for user's production environment setting.

- It is recommended to use short connection to perform stress tests on forwarding capability of cloud load balancer

In general, except for verifying the features such as session persistence, the stress test is mainly designed to verify the forwarding capability of cloud load balancer. Therefore, the short connection can be used to test the processing capability of LBs and backend servers.

- It is recommended to use a persistent connection to perform the stress tests on throughput of cloud load balancer. The persistent connection is used to test the upper limit of bandwidth or long connection service.

In this case, it is recommended to adjust the timeout value of a stress test tool to a smaller threshold. If the timeout period is too long, the average response time will be longer, which will be detrimental to quickly determine whether the stress test level is reached.

- It is recommended to use a static web page provided by backend server for stress test to avoid loss caused by application logic itself, such as I/O, DB, etc.

- Disable session persistence feature for listening. Otherwise, the pressure will be concentrated on individual backend servers. In addition, when the pressure performance is not up to standard, you can determine whether the traffic is evenly distributed by checking the monitor data of backend CVM under cloud load balancer.

- Disable health check feature for listening to reduce access requests to backend servers caused by health check

- Use multiple clients (> 5) for stress tests. Dispersed source IP is better for simulating the actual situation online

