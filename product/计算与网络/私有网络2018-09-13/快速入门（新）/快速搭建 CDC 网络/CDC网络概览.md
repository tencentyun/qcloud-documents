
腾讯云本地专用集群（Cloud Dedicated Cluster，CDC）是全新推出的托管型基础设施类产品，将腾讯云的计算、网络、存储等服务以整机柜的形式，扩展到用户IDC，就近提供与云上一致能力，支持通过公有云现有工具（控制台、API 等）实现 CDC 资源的统一管理。
CDC 融合了公有云与本地 IDC 的双重优势，用户可以以本地化的时延和数据安全来使用公有云的丰富能力，构建强大的分布式边缘云网络。

<img src="https://main.qcloudimg.com/raw/7820418a0b0b98fb98c2943fb137c7d3.png" width="60%" />

## 网络功能
CDC支持的网络功能包括：
+ 支持单VPC多子网
+ 支持VPC主路由表，也支持自定义路由表
+ 支持安全组、ACL、流日志
+ 支持访问主Region云上公共服务，如DNS、YUM等
+ 本地IDC通信
+ 本地EIP
+ 公网CLB通信

![](https://main.qcloudimg.com/raw/589aa793b1268761919ef4c437e04d9e.png)

## 使用限制
+ 用户IDC需提供1Gbps以上的互联网接入能力，不限于使用腾讯云互联网专用通道或运营商互联网专线。
+ CDC内仅支持一个VPC。
+ CDC暂不支持内网CLB、VPN、NAT网关、专线接入等其他网络接入能力。
+ CDC支持和云上关联的VPC内的所有子网服务进行通信，不支持跨VPC互访，也不支持和该VPC内的专线、SD-WAN Edge、黑石服务器、VPN互访。
+ CDC独占子网

## 网络通信场景
+ CDC通过本地网关与本地IDC通信
+ CDC通过本地EIP或公网CLB访问公网
+ CDC通过云联网和其他VPC、IDC通信

