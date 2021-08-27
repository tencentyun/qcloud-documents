## VPC-CNI 模式基本信息
腾讯云容器服务（Tencent Kubernetes Engine，TKE）默认提供 Global Router 网络模式，即基于 VPC 的全局路由能力，让容器 IP（与 VPC 网段不重叠）在 VPC 内可以路由，其原理是 VPC 底层根据容器 IP 转发到对应 Pod CIDR 的节点上，再通过 cbr0 网桥路由到对应容器 IP 的 Pod 内。如下图所示：
<img style="width:450px" src="https://main.qcloudimg.com/raw/e94d6f31028d804a346b78be8255a91a.png" data-nonescope="true">
TKE 后续推出 VPC-CNI 网络模式，即为每个 Pod 插入一张弹性网卡，IP 范围在 VPC 网段内，Pod 间通信直接通过弹性网卡路由。如下图所示：
<img style="width:450px" src="https://main.qcloudimg.com/raw/24f9223d9cd7c26789f32bc235f56e51.png" data-nonescope="true">

## VPC-CNI 模式应用场景
相比 Global Router，VPC-CNI 具有以下优势及适用场景：

|                         优势                                           |                       适用场景                                       | 
|----------------------------------------------------------------|----------------------------------------------------------------|
| 少了一层网桥，网络转发性能更高，大约提升10%    | 对网络时延要求较高的场景。                                 | 
| 支持 Pod 固定 IP    | 依赖容器固定 IP 的场景。例如，传统架构迁移到容器平台及针对 IP 做安全策略限制。  |
| 支持 LB 直通 Pod   |          希望使用 LB 直通 Pod。                                                                           | 

## VPC-CNI 模式使用限制
- 需要为容器专门规划子网，并且子网不能与其他云上资源共用（如云服务器、负载均衡等）。
- 集群内的节点需要和子网处于相同可用区，如果节点买错可用区，Pod 将无法调度。
- 节点上可调度的 VPC-CNI 模式的 Pod 数量受限于节点所支持插入弹性网卡能绑定 IP 的最大数量。配置越高的机器可插入的弹性网卡数量越多，可以通过查看节点的 Allocatable 来确认。


## VPC-CNI 模式操作步骤
登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
### 启用 VPC-CNI[](id:VPC-CNI">
TKE 有两种方式启用 VPC-CNI：
- 方式1：创建集群时选择 VPC-CNI 网络插件。如下图所示：
![](https://main.qcloudimg.com/raw/d3d84cfc2ede5be4c67d698c03b18c6a.png)
>! 使用 [方式1](#VPC-CNI) 启用 VPC-CNI 时，需要展开**高级设置** > **设置IP回收策略**。
>
- 方式2：创建集群时选择 Global Router 网络插件，在集群基本信息页面开启 VPC-CNI 模式（两种默认混用）。如下图所示：   
![](https://main.qcloudimg.com/raw/ab4d97e82fff662de4c7532beac46238.png)
针对固定 IP 场景，启用 VPC-CNI 后需要设置 IP 回收策略，即设置 Pod 销毁后需要退还 IP 的时长。非固定 IP 的 Pod 销毁后可立即释放 IP，不受此设置的影响。如下图所示：<br>
<img style="width:350px" src="https://main.qcloudimg.com/raw/6db435ed2756ca6ba8a1262720ad0165.png" data-nonescope="true">



### 使用 VPC-CNI
>! 
使用 VPC-CNI 需要确保 rp_filter 处于关闭状态。可参考以下代码示例：
``` bash
sysctl -w net.ipv4.conf.all.rp_filter=0
sysctl -w net.ipv4.conf.default.rp_filter=0
```
`tke-cni-agent` 组件自动设置节点的内核参数。若您自己有维护内核参数且打开 rp_filter，会导致网络不通。
>
- 若使用 [方式1](#VPC-CNI) 启用 VPC-CNI，通过控制台或通过 yaml 创建工作负载，Pod 均默认使用弹性网卡。   
- 若使用 [方式2](#VPC-CNI) 启用 VPC-CNI（Global Router 与 VPC-CNI 两种模式混用），Pod 默认不使用弹性网卡，需注意以下事项：
  - 通过控制台创建工作负载，VPC-CNI 只支持 StatefulSet 类型，展开高级设置并勾选 `使用VPC-CNI模式`。如下图所示：
    <img style="width:450px" src="https://main.qcloudimg.com/raw/390152f469ac6199eeb25c1b81507e40.png" data-nonescope="true">
  - 通过 yaml 创建，VPC-CNI 支持任意类型工作负载，只需为 Pod 添加一个 annotation，即 `tke.cloud.tencent.com/networks: "tke-route-eni"`，并为其中一个容器添加 requests 与 limits，例如 `tke.cloud.tencent.com/eni-ip: "1"`。可参考以下代码示例：
   ``` yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: nginx
     labels:
       app: nginx
   spec:
     replicas: 1
     selector:
       matchLabels:
         app: nginx
     template:
       metadata:
         annotations:
           tke.cloud.tencent.com/networks: "tke-route-eni"
         labels:
           app: nginx
       spec:
         containers:
           - name: nginx
             image: nginx
             resources:
               requests:
                 tke.cloud.tencent.com/eni-ip: "1"
               limits:
                 tke.cloud.tencent.com/eni-ip: "1"
   ```


### 固定 Pod IP 

固定 IP 功能仅适用于 StatefulSet 类型的工作负载，可通过以下两种方法开启固定 IP：
- 方式1：通过控制台创建，可选择开启固定 IP。如下图所示：
    <img style="width:450px" src="https://main.qcloudimg.com/raw/f1183fa3418cea6a07036e9516f15cdf.png" data-nonescope="true">
- 方式2：通过 yaml 创建，需要为 StatefulSet 添加一个 annotation，即 `tke.cloud.tencent.com/vpc-ip-claim-delete-policy: Never`。可参考以下代码示例：
   ``` yaml
   apiVersion: apps/v1beta1
   kind: StatefulSet
   metadata:
     name: busybox
   spec:
     serviceName: "busybox"
     replicas: 1
     template:
       metadata:
         annotations:
           tke.cloud.tencent.com/networks: tke-route-eni
           tke.cloud.tencent.com/vpc-ip-claim-delete-policy: Never
         labels:
           app: busybox
       spec:
         terminationGracePeriodSeconds: 0
         containers:
         - name: busybox
           image: busybox
           command: ["sleep", "10000000000"]
           resources:
             requests:
               tke.cloud.tencent.com/eni-ip: "1"
             limits:
               tke.cloud.tencent.com/eni-ip: "1"
   ```


### 更改 IP 回收策略 

若启用 VPC-CNI 时设置了 IP 回收策略，后续可通过手动修改 ipamd 组件的启动参数来实现更改，即 `kubectl -n kube-system edit deployments.v1.apps tke-eni-ipamd`。可参考以下代码示例：
``` yaml
    spec:
      containers:
      - args:
        - --clusterid
        - cls-kjqul1ir
        - --claim-expired-duration
        - 10m0s
```
>! 修改 `--claim-expired-duration` 指定的值即可。

### 扩容 IP 容量

若 VPC-CNI 的子网 IP 数量不够时，可以通过手动修改 ipamd 组件的配置来增加子网，编辑 `kube-system` 命名空间下 `tke-eni-ipamd` 的 configmap，即 `kubectl -n kube-system edit configmap tke-eni-ipamd`。可参考以下代码示例：
``` yaml
apiVersion: v1
kind: ConfigMap
metadata:
  namespace: kube-system
  name: tke-eni-ipamd
data:
  TKE_ENI_IPAMD_SUBNET_ID: subnet-4k3fdq3f:subnet-aa7clla5
  TKE_ENI_IPAMD_VPC_ID: vpc-409o11tu
```
>!
- 将要增加的子网 id 加入 `TKE_ENI_IPAMD_SUBNET_ID`，通过 `:` 分隔即可。需注意加入的子网应为空，即子网内没有云服务器、负载均衡等云上资源，否则会造成冲突。
- 如果看到 TKE_ENI_IPAMD_ZONE 的配置，可忽略，该项配置已废弃。
- 修改 ipamd 组件的配置以后，还需要执行以下命令删除重建 ipamd pod，才能使修改生效：
  ```
  kubectl -nkube-system get po -ocustom-columns=Name:.metadata.name | grep ipamd | kubectl -nkube-system delete po
  ```



## 参考资料
- [如何选择容器服务网络模式](https://cloud.tencent.com/document/product/457/41636)
- [GlobalRouter 附加 VPC-CNI 模式说明](https://cloud.tencent.com/document/product/457/34993)
- [固定 Pod IP 类型 StatefulSet 管理](https://cloud.tencent.com/document/product/457/34994)
