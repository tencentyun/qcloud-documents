腾讯云本地专用集群（Cloud Dedicated Cluster，CDC）是全新推出的托管型基础设施类产品，将腾讯云的计算、网络、存储等服务以整机柜的形式，扩展到用户 IDC，就近提供与云上一致能力，支持通过公有云现有工具（控制台、API 等）实现 CDC 资源的统一管理。

CDC 融合了公有云与本地 IDC 的双重优势，用户可以以本地化的时延和数据安全来使用公有云的丰富能力，构建强大的分布式边缘云网络。
<img src="https://main.qcloudimg.com/raw/7820418a0b0b98fb98c2943fb137c7d3.png" width="60%" />

## 网络功能
CDC支持的网络功能包括：
+ 支持单 VPC 多子网
+ 支持 VPC 主路由表，也支持自定义路由表
+ 支持安全组、ACL、流日志
+ 支持访问主 Region 云上公共服务，如 DNS、YUM 等
+ 本地 IDC 通信
+ 弹性 IP
+ 公网 CLB 通信

![](https://main.qcloudimg.com/raw/589aa793b1268761919ef4c437e04d9e.png)

## 使用限制
+ 用户 IDC 需提供1Gbps以上的互联网接入能力，不限于使用腾讯云互联网专用通道或运营商互联网专线。
+ CDC 暂不支持内网 CLB、VPN、NAT 网关、专线接入等其他网络接入能力。
+ CDC 支持和云上关联的 VPC 内的所有子网服务进行通信，不支持跨 VPC 互访，也不支持和该 VPC 内的专线、SD-WAN Edge、黑石服务器、VPN 互访。
+ CDC 独占子网，子网支持更换路由表、ACL，不支持 IPv6、广播功能。
+ 1个 CDC 只支持1个 VPC，1个 CDC 集群的1个 VPC 只能够创建1个 CDC 本地网关。

## 网络通信场景
+ CDC 通过本地网关与本地 IDC 通信
+ CDC内云服务器本地出公网
+ CDC 通过云联网和其他 VPC、IDC 通信

