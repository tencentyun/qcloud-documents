# 1. About Cloud Load Balancer (CLB)'s HTTPS Capability
Tencent Cloud's CLB has achieved significant improvement in HTTPS performance based on the full optimization of protocol stack and servers. At the same time, our cooperation with world-leading certificate providers results in a considerable cost-saving in certificates. Tencent Cloud's CLB brings substantial benefits for your business in the following aspects:

1） The use of HTTPS does not affect the access speed of client.

2）A single CVM in a cluster features a fast SSL encryption and decryption capability, with the full handshakes reaching up to 65,000 cps. This is at least 3.5 times faster than that when high-performance CPU is relied on, which greatly reduces the server costs, enhances the service capacity at the time of business volume and traffic surges and achieves a stronger computing-based anti-attack capability.

3） Support the uninstallation and translation of a variety of protocols. Reduce the stress involved in the adaption to various protocols of the client. The business back-end just needs to support HTTP1.1 to use various versions of protocols such as HTTP2, SPDY, SSL3.0 and TLS1.2.

4） One-stop service covering SSL certificate application, monitoring and replacement. By working with world-leading certificate providers including comodo and symantec, we have significantly simplified the certificate application procedures and reduced relevant costs.

5）Anti-CC and WAF capabilities Effectively prevent attacks at application layer such as slow connection, high-frequency targeted attack, SQL injection, website malicious code.





# 2. Test Purpose
HTTPS service has such advantages as authentication, message encryption and integrity verification. However, achieving secure communication by adding SSL protocol will inevitably cause some performance loss, including a longer latency and consumption of CPU resources for encryption and decryption. This document provides the test data on performance limits of Tencent Cloud's HTTPS service with SSL encryption and decryption, which can be used for reference and comparison with traditional performance data of HTTPS.

# 3. Test Environment
- Stress testing tool: wrk 4.0.2
- Tencent Cloud's underlying service environment: Nginx 1.1.6_1.9.9 + Openssl 1.0.2h
- OS of the machine on which Nginx is installed: Linux TENCENT64.site 3.10.94-1-tlinux2-0036.tl2 # 1 SMP Thu Jan 21 03:40:59 CST 2016 x86_64 x86_64 x86_64 GNU / Linux
- OS of other stress-source machines: Linux TENCENT64.site 2.6.32.43-tlinux-1.0.17-default # 1 SMP Tue Nov 17 18:03:12 CST 2015 x86_64 x86_64 x86_64 GNU / Linux

# 4. WebServer Cluster Test Scheme
The stress from a single stress-source machine is not enough to test the performance limit of Tencent Cloud's HTTPS service. Therefore, multiple stress-source machines are needed to send stress. The test involves three parts:

1) Stress-source machine cluster. Used to exert HTTP/HTTPS stress and output stress testing results of a single machine.

2) Central control machine, which synchronously controls the start and stop of the stress-source machine cluster, obtains the stress testing data from each machine, and aggregates and outputs the data.

3) Tested machine, the CVM hosting Tencent Cloud's HTTPS service. When the performance of webserver is tested, page is returned directly and there is no need to make upstream connection.
The connections are as follows:

![](https://mc.qcloudimg.com/static/img/45cc4191947ca44b37c47499138c8669/image.jpg)

# 5. Performance Testing Data of HTTPS WebServer

| Connection Type | Session cache | Packet Size (bytes) | Encryption Suite | Performance (qps) |
|---------|---------|---------|---------|---------|
| Persistent | On | 230 | ECDHE-RSA-AES128-GCM-SHA256 | 296241 |
| Short | Off | 230 | ECDHE-RSA-AES128-GCM-SHA256 | 65630 |

# 6. Conclusion on CLB HTTPS Capability Test 
According to the above table, Tencent Cloud's HTTPS service supports SSL encryption and decryption, and it has multiple CVM clusters at back-end. A single CVM in a cluster can achieve a performance of up to 65000 qps during full handshake and of about 300000 qps during a persistent connection.

In general, due to the use of SSL protocol, at least an additional full handshake is required for HTTPS protocol, making the latency increase by 2*RTT. In addition, SSL symmetric/asymmetric encryption can consume substantial CPU resource, and RSA's decryption capability is the main barrier to the HTTPS access.

With Tencent Cloud's HTTPS service, users need not to deploy services additionally for SSL encryption and decryption. With no additional cost is charged, the service allows users to easily enjoy powerful business-hosting capacity and anti-attack capability.

