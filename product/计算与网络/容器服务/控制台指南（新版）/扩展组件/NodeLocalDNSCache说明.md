## 简介

### 组件介绍

NodeLocal DNSCache 通过在集群节点上作为 DaemonSet 运行 DNS 缓存代理来提高集群 DNS 性能。在当今的体系结构中，处于 ClusterFirst DNS 模式的 Pod 可以连接到 kube-dns serviceIP 进行 DNS 查询。通过 kube-proxy 添加的 iptables 规则将其转换为 kube-dns/CoreDNS 端点。借助此新架构，Pods 将可以访问在同一节点上运行的 DNS 缓存代理，从而避免了 iptables DNAT 规则和连接跟踪。本地缓存代理将查询 kube-dns 服务以获取集群主机名的缓存缺失（默认为 cluster.local 后缀）。

### 部署在集群内的 Kubernetes 对象

| kubernets 对象名称 | 类型           | 请求资源                | 所属 Namespace |
| :----------------- | -------------- | ----------------------- | -------------- |
| node-local-dns     | DaemonSet      | 每节点50mCPU，5Mi内存 | kube-system    |
| kube-dns-upstream  | Service        | -                       | kube-system    |
| node-local-dns     | ServiceAccount | -                       | kube-system    |
| node-local-dns     | Configmap      | -                       | kube-system    |

## 限制条件

- 仅支持 1.14 版本以上的 kubernetes 版本。
- VPC-CNI 同时支持 kube-proxy 的 iptables 和 ipvs 模式，GlobalRouter 仅支持 kube-proxy 的 iptables 模式，ipvs 模式下需要更改 kubelet 参数，详情请参见 [官方文档](https://kubernetes.io/docs/tasks/administer-cluster/nodelocaldns/)。
- 集群创建后没有调整过 dns 服务对应工作负载的相关 name 和 label，检查集群 kube-system 命名空间中存在以下 dns 服务的相关工作负载：
  - service/kube-dns
  - deployment/kube-dns 或者 deployment/coredns，且存在 k8s-app: kube-dns 的 label
- 由于 Ubuntu 20.04 LTS 主机默认启动 named 服务，该服务会与 NodeLocal DNSCache 冲突，因此暂不能添加该 OS 的节点。
- IPVS 的独立集群，需要确保 add-pod-eni-ip-limit-webhook ClusterRole 具备以下权限：
```
- apiGroups:
  - ""
  resources:
  - configmaps
  - secrets
  - namespaces
  - services
  verbs:
  - list
  - watch
  - get
  - create
  - update
  - delete
  - patch
```
- IPVS 的独立集群和托管集群，都需要确保 tke-eni-ip-webhook Namespace 下的 add-pod-eni-ip-limit-webhook Deployment 镜像版本大于等于 v0.0.5。

## 推荐配置
当安装 NodeLocal DNSCache 后，推荐为 CoreDNS 增加如下配置：
```yaml
            template ANY HINFO . {
                rcode NXDOMAIN
            }
            forward . /etc/resolv.conf {
                prefer_udp
            }
```

## 操作步骤


1. 登录 [容器服务控制台](https://console.qcloud.com/tke2)，在左侧导航栏中选择**集群**。
2. 在“集群管理”页面单击目标集群 ID，进入集群详情页。
3. 选择左侧菜单栏中的**组件管理**，进入 “组件列表” 页面。
4. 在“组件列表”页面中选择**新建**，并在“新建组件”页面中勾选 NodeLocalDNSCache。NodeLocalDNSCache 详细配置可参见 [官方文档](https://kubernetes.io/docs/tasks/administer-cluster/nodelocaldns)。
5. 单击**完成**即可创建组件。
