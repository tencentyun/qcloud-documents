
## 使用原理
Cilium-Overlay 网络模式是容器服务 TKE 基于 Cilium VXLan 实现的容器网络插件，实现分布式云场景中，第三方节点添加到 TKE 集群的网络管理。该网络模式特征如下：
- 云上节点和第三方节点共用指定的容器网段。
- 容器网段分配灵活，容器 IP 段不占用 VPC 的其他网段。
- 使用 Cilium VXLan 隧道封装协议构建 Overlay 网络。

云上 VPC 网络和第三方节点 IDC 网络通过云联网互通后，跨节点 Pod 访问原理如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/c09deb3c0e07b777a436c62945055158.png)
 
>? 由于 Cilium-Overlay 模式存在性能损耗，因此此模式只支持分布式云中第三方节点场景，不支持只存在云上节点场景，分布式云中第三方节点详情可参见 [第三方节点概述](https://cloud.tencent.com/document/product/457/57916)。

 
 
## 使用限制
- 使用 Cilium VXLan 隧道封装协议，有10%以内的性能损耗。
- Pod IP 在集群外不能直接访问。
- 需从指定子网获取 2 个 IP 创建内网负载均衡，满足 IDC 中第三方节点访问 APIServer 和云上公共服务。
- 集群网络和容器网络网段不能重叠。
- 不支持固定 Pod IP。


## 容器 IP 分配机制
容器网络名词介绍和数量计算可参见 [容器网络说明](https://cloud.tencent.com/document/product/457/50353#.E5.AE.B9.E5.99.A8.E7.BD.91.E7.BB.9C.E8.AF.B4.E6.98.8E.3Ca-id.3D.22annotation.22.3E.3C.2Fa.3E)。


#### Pod IP 分配
工作原理如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/0d460871c1e8c756560f533bf5d75474.png)

- 集群中节点包括云上节点和第三方节点。
- 集群的每一个节点会使用容器 CIDR 中的指定大小的网段用于该节点下 Pod 的 IP 地址分配。
- 集群的 Service 网段会选用容器 CIDR 中最后一段指定大小的网段用于 Service 的 IP 地址分配。
- 节点释放后，使用的容器网段也会释放回 IP 段池。
- 扩容节点自动按顺序循环选择容器 CIDR 大段中可用的 IP 段。
