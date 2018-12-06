## DDoS 攻击
分布式拒绝服务攻击（Distributed Denial of Service，DDoS），指攻击者通过网络远程控制大量僵尸主机，向一个或多个目标发送大量攻击请求，耗尽攻击目标服务器的系统资源，导致其无法响应正常的服务请求。

## 网络层 DDoS 攻击
网络层 DDoS 攻击，主要指攻击者利用大流量攻击，拥塞目标服务器的网络带宽，消耗服务器系统层资源，导致目标服务器无法正常响应客户访问的攻击方式。常见攻击类型包括 SYN Flood、ACK Flood、UDP Flood、ICMP Flood以及 DNS/NTP/SSDP/memcached 反射型攻击。

## CC 攻击
CC 攻击主要指通过恶意占用目标服务器应用层资源，消耗处理性能，导致其无法正常提供服务的攻击方式。常见的攻击类型包括基于 HTTP/HTTPS的GET/POST Flood、四层 CC、Connect Flood 等攻击方式。