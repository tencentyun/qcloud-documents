[ServiceGroup 多地域部署](https://cloud.tencent.com/document/product/457/83214) 中简单描述了 ServiceGroup 的使用方式。本文以详细的案例结合具体的实现原理，向您介绍 ServiceGroup 的使用场景以及需要关注的细节问题。
 
## 关键概念

### 整体架构

<div align="left">
  <img src="https://qcloudimg.tencent-cloud.cn/raw/63781bb68b9a414f9909e9a36f1ab581.jpg" width=100% title="service-group">
</div>

### 基本概念

关于 NodeUnit 和 NodeGroup 最新版设计可以参考 [边缘节点池和边缘节点池分类设计文档](https://github.com/superedge/superedge/blob/main/docs/components/site-manager_CN.md)。

#### NodeUnit（边缘节点池）

- NodeUnit 通常是位于同一边缘站点内的一个或多个计算资源实例，需要保证同一 NodeUnit 中的节点内网是通的。
- ServiceGroup 组中的服务运行在一个 NodeUnit 之内。
- ServiceGroup 允许用户设置服务在一个 NodeUnit 中运行的 pod 数量。
- ServiceGroup 能够把服务之间的调用限制在本 NodeUnit 内。

#### NodeGroup（边缘节点池分类）

- NodeGroup 包含一个或者多个 NodeUnit。
- 保证在集合中每个 NodeUnit 上均部署 ServiceGroup 中的服务。
- 集群中增加 NodeUnit 时自动将 ServiceGroup 中的服务部署到新增 NodeUnit。

#### ServiceGroup

ServiceGroup 包含一个或者多个业务服务。适用场景如下：
- 业务需要打包部署。
- 业务需要在每一个 NodeUnit 中运行起来并且保证 pod 数量。
- 业务需要将服务之间的调用控制在同一个 NodeUnit 中，不能将流量转发到其他 NodeUnit。

>! ServiceGroup 是一种抽象资源，一个集群中可以创建多个 ServiceGroup。
>

 ServiceGroup 涉及的资源类型包括如下三类：
<dx-tabs>
:::  DeploymentGrid

DeploymentGrid 的格式与 Deployment 类似，<deployment-template>字段就是原先 deployment 的 template 字段，比较特殊的是 gridUniqKey 字段，该字段指明了节点分组的 label 的 key 值：

```yaml
apiVersion: superedge.io/v1
kind: DeploymentGrid
metadata:
  name:
  namespace:
spec:
  gridUniqKey: <NodeLabel Key>
  <deployment-template>
```
:::
::: StatefulSetGrid

StatefulSetGrid 的格式与 StatefulSet 类似，<statefulset-template>字段就是原先 statefulset 的 template 字段，比较特殊的是 gridUniqKey 字段，该字段指明了节点分组的 label 的 key 值：

```yaml
apiVersion: superedge.io/v1
kind: StatefulSetGrid
metadata:
  name:
  namespace:
spec:
  gridUniqKey: <NodeLabel Key>
  <statefulset-template>
```
:::
::: ServiceGrid

ServiceGrid 的格式与 Service 类似，<service-template>字段就是原先 service 的 template 字段，比较特殊的是 gridUniqKey 字段，该字段指明了节点分组的 label 的 key 值：

```yaml
apiVersion: superedge.io/v1
kind: ServiceGrid
metadata:
  name:
  namespace:
spec:
  gridUniqKey: <NodeLabel Key>
  <service-template>
```
:::
</dx-tabs>



##  操作步骤

以在边缘部署 echo-service 为例，我们希望在多个节点组内分别部署 echo-service 服务，需要如下操作：

### 确定 ServiceGroup 唯一标识
此步骤为逻辑规划，不需要做任何实际操作。我们将目前要创建的 ServiceGroup 逻辑标记使用的 UniqKey 为 `location`。

### 将边缘节点分组

如下图，我们以一个边缘集群为例，将集群中的节点添加到**边缘节点池**以及**边缘节点池分类**中。本文示例以公有云界面来操作，SuperEdge 开源用户可以参考 [边缘节点池和边缘节点池分类设计文档](https://github.com/superedge/superedge/blob/main/docs/components/site-manager_CN.md) 使用 CRD 进行操作完成下面的步骤。

此集群包含 6 个边缘节点，分别位于北京/广州 2 个地域，节点名为`bj-1`、`bj-2`、`bj-3`、`gz-1`、`gz-2`、`gz-3`。

<div align="left">
  <img src="https://qcloudimg.tencent-cloud.cn/raw/3c4b3bf3cf84a0abace4a95172c7df17.png" width=100% title="node-list">
</div>

然后我们分别创建 2 个 NodeUnit（边缘节点池）：`beijing`、`guangzhou`，分别将相应的节点加入对应的 NodeUnit（边缘节点池）中，如下图：

<div align="left">
  <img src="https://qcloudimg.tencent-cloud.cn/raw/0ca750197aad6b035796d013eb70497d.png" width=100% title="service-group">
</div>

最后，我们创建名称为 `location` 的 NodeGroup（边缘节点池分类），将`beijing`、`guangzhou` 这两个边缘节点池划分到`location`这个分类中，如下图：

<div align="left">
  <img src="https://qcloudimg.tencent-cloud.cn/raw/04879e4f0917b56ddcb7342ae3cb35e8.png" width=100% title="service-group">
</div>

进行上述操作后，每个节点上会被打上相应的标签，节点 gz-2 的标签如下图所示：

<div align="left">
  <img src="https://qcloudimg.tencent-cloud.cn/raw/66a28a98c5c92b70dc23dce6b070b922.jpg" width=50% title="service-group">
</div>

>! 上一步中，label 的 key 就是 NodeGroup 的名字，同时与 ServiceGroup 的 UniqKey 一致，value 是 NodeUnit 的唯一 key，value 相同的节点表示属于同一个 NodeUnit。
>如果同一个集群中有多个 NodeGroup 请为每一个 NodeGroup 分配不同的 UniqKey，部署 ServiceGroup 相关资源的时候会通过 UniqKey 来绑定指定的 NodeGroup 进行部署。

### 无状态 ServiceGroup

#### 部署 DeploymentGrid

```yaml
apiVersion: superedge.io/v1
kind: DeploymentGrid
metadata:
  name: deploymentgrid-demo
  namespace: default
spec:
  gridUniqKey: location
  template:
    replicas: 2
    selector:
      matchLabels:
        appGrid: echo
    strategy: {}
    template:
      metadata:
        creationTimestamp: null
        labels:
          appGrid: echo
      spec:
        containers:
        - image: superedge/echoserver:2.2
          name: echo
          ports:
          - containerPort: 8080
            protocol: TCP
          env:
            - name: NODE_NAME
              valueFrom:
                fieldRef:
                  fieldPath: spec.nodeName
            - name: POD_NAME
              valueFrom:
                fieldRef:
                  fieldPath: metadata.name
            - name: POD_NAMESPACE
              valueFrom:
                fieldRef:
                  fieldPath: metadata.namespace
            - name: POD_IP
              valueFrom:
                fieldRef:
                  fieldPath: status.podIP
          resources: {}
```

#### 部署 ServiceGrid

```yaml
apiVersion: superedge.io/v1
kind: ServiceGrid
metadata:
  name: servicegrid-demo
  namespace: default
spec:
  gridUniqKey: location
  template:
    selector:
      appGrid: echo
    ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
```

gridUniqKey 字段设置为了 location，所以我们在将节点分组时采用 label 的 key 为 location；这时，`bejing` 和 `guangzhou` 的 NodeUnit 内都有了 echo-service 的 deployment 和对应的 pod，在节点内访问统一的 service-name 也只会将请求发向本组的节点。

```shell
[~]# kubectl get dg
NAME                  AGE
deploymentgrid-demo   9s

[~]# kubectl get deployment
NAME                            READY   UP-TO-DATE   AVAILABLE   AGE
deploymentgrid-demo-beijing     2/2     2            2           14s
deploymentgrid-demo-guangzhou   2/2     2            2           14s

[~]# kubectl get pods -o wide
NAME                                             READY   STATUS    RESTARTS   AGE     IP           NODE   NOMINATED NODE   READINESS GATES
deploymentgrid-demo-beijing-65d669b7d-v9zdr      1/1     Running   0          6m51s   10.0.1.72    bj-3   <none>           <none>
deploymentgrid-demo-beijing-65d669b7d-wrx7r      1/1     Running   0          6m51s   10.0.0.70    bj-1   <none>           <none>
deploymentgrid-demo-guangzhou-5d599854c8-hhmt2   1/1     Running   0          6m52s   10.0.0.139   gz-2   <none>           <none>
deploymentgrid-demo-guangzhou-5d599854c8-k9gc7   1/1     Running   0          6m52s   10.0.1.8     gz-3   <none>           <none>

#从上面可以看到，对于一个 deploymentgrid，会分别在每个 nodeunit 下创建一个 deployment，他们会通过 <deployment>-<nodeunit>名称的方式来区分

[~]# kubectl get svc
NAME                   TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)             AGE
kubernetes             ClusterIP   172.16.33.1     <none>        443/TCP             47h
servicegrid-demo-svc   ClusterIP   172.16.33.231   <none>        80/TCP              3s

[~]# kubectl describe svc servicegrid-demo-svc
Name:              servicegrid-demo-svc
Namespace:         default
Labels:            superedge.io/grid-selector=servicegrid-demo
                   superedge.io/grid-uniq-key=location
Annotations:       topologyKeys: ["location"]
Selector:          appGrid=echo
Type:              ClusterIP
IP Families:       <none>
IP:                172.16.33.231
IPs:               <none>
Port:              <unset>  80/TCP
TargetPort:        8080/TCP
Endpoints:         10.0.0.139:8080,10.0.0.70:8080,10.0.1.72:8080 + 1 more...
Session Affinity:  None
Events:            <none>

#从上面可以看到，对于一个 servicegrid，都会创建一个 <servicename>-svc 的标准 Service；
#！！！注意，这里的 Service 对应的后端 Endpoint 仍然为所有 pod 的 endpoint 地址，这里并不会按照 nodeunit 进行 endpoint 筛选

# 在 guangzhou 地域的 pod 内执行下面的命令
[~]# curl 172.16.33.231|grep "node name"
        node name:      gz-2
...
# 这里会随机返回 gz-2 或者 gz-3 的 node 名称，并不会跨 NodeUnit 访问到 bj-1 或者 bj-3

# 在 beijing 地域的 pod 执行下面的命令
[~]# curl 172.16.33.231|grep "node name"
        node name:      bj-3
# 这里会随机返回 bj-1 或者 bj-3 的 node 名称，并不会跨 NodeUnit 访问到 gz-2 或者 gz-3
```

另外，对于部署了 DeploymentGrid 和 ServiceGrid 后才添加进集群的节点组，该功能会在新的节点组内自动创建指定的 deployment。

#### 原理解析

下面来简单介绍一些 ServiceGroup 如何实现不同 NodeUnit 地域的 Service 访问的流量闭环的，如下图：

<div align="left">
  <img src="https://qcloudimg.tencent-cloud.cn/raw/f000b96d244a62850ef4d15f3a82e22c.jpg" width=100% title="deploymentgrid">
</div>

原理剖析：
- 当创建一个 DeploymentGrid 的时候，通过云端的 application-grid-controller 服务，会分别在每个 NodeUnit 上生成一个单独的标准 Deployment。（例如 deploymentgrid-demo-beijing-XXXXX）
- 当创建相应的 ServiceGrid 的时候，会在集群中创建一个标准的 Service，如上图`servicegrid-demo-svc`。
- 此时为标准的 Deployment 和标准 Service，这两个行为无法根据 NodeUnit 实现流量闭环。此时需要添加`application-grid-wrapper` 组件。
- 从上图可以看到`application-grid-wrapper` 组件部署在每一个边缘 node 上，同时边缘侧`kube-proxy` 会通过`application-grid-wrapper`和 apiserver 通信，获取相应资源信息；这里`application-grid-wrapper`会监听 ServiceGrid 的 CRD 信息，同时在获取到对应的 Service 的 Endpoint 信息后，就会根据所在 NodeUnit 的节点信息进行筛选，将不在同一 NodeUnit 的 Node 上的 Endpoint 剔除，传递给`kube-proxy`更新 iptables 规则。下述示例为`bj-3`北京地域节点上的 iptables 规则：
```shell
-A KUBE-SERVICES -d 172.16.33.231/32 -p tcp -m comment --comment "default/servicegrid-demo-svc: cluster IP" -m tcp --dport 80 -j KUBE-SVC-MLDT4NC26VJPGLP7

-A KUBE-SVC-MLDT4NC26VJPGLP7 -m comment --comment "default/servicegrid-demo-svc:" -m statistic --mode random --probability 0.50000000000 -j KUBE-SEP-VB3QR2E2PUKDLHCW

-A KUBE-SVC-MLDT4NC26VJPGLP7 -m comment --comment "default/servicegrid-demo-svc:" -j KUBE-SEP-U5ZEIIBVDDGER3DI

-A KUBE-SEP-U5ZEIIBVDDGER3DI -p tcp -m comment --comment "default/servicegrid-demo-svc:" -m tcp -j DNAT --to-destination 10.0.1.72:8080

-A KUBE-SEP-VB3QR2E2PUKDLHCW -p tcp -m comment --comment "default/servicegrid-demo-svc:" -m tcp -j DNAT --to-destination 10.0.0.70:8080
```
- 从上面规则分析可以看到，`beijing`地域中，172.16.33.231 的 ClusterIP 只会分流到`10.0.1.72`和`10.0.0.70`两个后端 Endpooint 上，对应两个 pod：`deploymentgrid-demo-beijing-65d669b7d-v9zdr`和`deploymentgrid-demo-beijing-65d669b7d-wrx7r`，而且不会添加上`guangzhou`地域的两个 IP 10.0.0.139 和 10.0.1.8，按照此逻辑，可以在不同的 NodeUnit 中实现流量闭环能力。
<dx-alert infotype="notice" title="需注意以下2个场景">
 - **DeploymentGrid + 标准 Service 能否实现流量闭环？**
 不可以。通过上述的分析，如果是标准的 Service，这个 Service:Endpoint 列表并不会被`application-grid-wrapper` 来监听处理，因此这里会获取全量的 Endpoint 列表，`kube-proxy`更新 iptables 规则的时候就会添加相应规则，将流量导出到其他 NodeUnit 中。
<br>
 - **DeploymentGrid + Headless Service 是否可以实现流量闭环？**
 可以根据下面的 Yaml 文件部署一个 Headless Service，同样使用 ServiceGrid 的模板来创建：
 ```yaml
 apiVersion: superedge.io/v1
 kind: ServiceGrid
 metadata:
   name: servicegrid-demo
   namespace: default
 spec:
   gridUniqKey: location
   template:
     clusterIP: None
     selector:
       appGrid: echo
     ports:
     - protocol: TCP
       port: 8080
       targetPort: 8080
 ```

 获取 Service 信息如下：

 ```
 Name:              servicegrid-demo-svc
 Namespace:         default
 Labels:            superedge.io/grid-selector=servicegrid-demo
                    superedge.io/grid-uniq-key=location
 Annotations:       topologyKeys: ["location"]
 Selector:          appGrid=echo
 Type:              ClusterIP
 IP Families:       <none>
 IP:                None
 IPs:               <none>
 Port:              <unset>  8080/TCP
 TargetPort:        8080/TCP
 Endpoints:         10.0.0.139:8080,10.0.0.70:8080,10.0.1.72:8080 + 1 more...
 Session Affinity:  None
 Events:            <none
 ```

 这里能够看到，仍然能够获取 4 个 Endpoint 的信息，同时 ClusterIP 的地址为空，在集群中的任意 Pod 里通过 nslookup 获取的 Service 地址就是 4 个后端 Endpoint，如下：

 ```
 [~]# nslookup servicegrid-demo-svc.default.svc.cluster.local
 Server:         169.254.20.11
 Address:        169.254.20.11#53
 
 Name:   servicegrid-demo-svc.default.svc.cluster.local
 Address: 10.0.1.8
 Name:   servicegrid-demo-svc.default.svc.cluster.local
 Address: 10.0.1.72
 Name:   servicegrid-demo-svc.default.svc.cluster.local
 Address: 10.0.0.70
 Name:   servicegrid-demo-svc.default.svc.cluster.local
 Address: 10.0.0.139
 ```

所以如果通过这种形式访问 servicegrid-demo-svc.default.svc.cluster.local 任然会访问到其余地域的 NodeUnit 内，无法实现流量闭环。
**同时，由于 Deployment 后端 pod 无状态，会随时重启更新，Pod 名称会随机变化，同时 Deployment 的 Pod 不会自动创建 DNS 地址，因此一般我们不会建议 Deployment + Headless Service 这样配合使用；而是推荐大家使用 StatefulsetGrid + Headless Service 的方式**。

<br>
通过上述的分析可得：如果访问 Service 的行为会通过 `kube-proxy`的 iptables 规则去进行转发，同时 Service 是 SerivceGrid 类型，会被`application-grid-wrapper`监听的话，就可以实现区域流量闭环；如果是通过 DNS 获取的实际 Endpoint IP 地址，就无法实现流量闭环。
</dx-alert>


 
### 有状态 ServiceGroup

#### 部署 StatefulSetGrid

```yaml
apiVersion: superedge.io/v1
kind: StatefulSetGrid
metadata:
  name: statefulsetgrid-demo
  namespace: default
spec:
  gridUniqKey: location
  template:
    selector:
      matchLabels:
        appGrid: echo
    serviceName: "servicegrid-demo-svc"
    replicas: 3
    template:
      metadata:
        labels:
          appGrid: echo
      spec:
        terminationGracePeriodSeconds: 10
        containers:
        - image: superedge/echoserver:2.2
          name: echo
          ports:
          - containerPort: 8080
            protocol: TCP
          env:
            - name: NODE_NAME
              valueFrom:
                fieldRef:
                  fieldPath: spec.nodeName
            - name: POD_NAME
              valueFrom:
                fieldRef:
                  fieldPath: metadata.name
            - name: POD_NAMESPACE
              valueFrom:
                fieldRef:
                  fieldPath: metadata.namespace
            - name: POD_IP
              valueFrom:
                fieldRef:
                  fieldPath: status.podIP
          resources: {}
```

>! template 中的 serviceName 设置成即将创建的 service 名称。

#### 部署 ServiceGrid

```yaml
apiVersion: superedge.io/v1
kind: ServiceGrid
metadata:
  name: servicegrid-demo
  namespace: default
spec:
  gridUniqKey: location
  template:
    selector:
      appGrid: echo
    ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
```

gridUniqKey 字段设置为了 location，因此这个 NodeGroup 依然包含`beijing`和`guangzhou`两个 NodeUnit，每个 NodeUnit 内都有了 echo-service 的 statefulset 和对应的 pod，在节点内访问统一的 service-name 也只会将请求发向本组的节点。

```shell
[~]# kubectl get ssg
NAME                   AGE
statefulsetgrid-demo   31s

[~]# kubectl get statefulset
NAME                             READY   AGE
statefulsetgrid-demo-beijing     3/3     49s
statefulsetgrid-demo-guangzhou   3/3     49s

[~]# kubectl get pods -o wide
NAME                               READY   STATUS    RESTARTS   AGE     IP           NODE   NOMINATED NODE   READINESS GATES
statefulsetgrid-demo-beijing-0     1/1     Running   0          9s      10.0.0.67    bj-1   <none>           <none>
statefulsetgrid-demo-beijing-1     1/1     Running   0          8s      10.0.1.67    bj-3   <none>           <none>
statefulsetgrid-demo-beijing-2     1/1     Running   0          6s      10.0.0.69    bj-1   <none>           <none>
statefulsetgrid-demo-guangzhou-0   1/1     Running   0          9s      10.0.0.136   gz-2   <none>           <none>
statefulsetgrid-demo-guangzhou-1   1/1     Running   0          8s      10.0.1.7     gz-3   <none>           <none>
statefulsetgrid-demo-guangzhou-2   1/1     Running   0          6s      10.0.0.138   gz-2   <none>           <none>

[~]# kubectl get svc
NAME                   TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)             AGE
kubernetes             ClusterIP   172.16.33.1     <none>        443/TCP             2d2h
servicegrid-demo-svc   ClusterIP   172.16.33.220   <none>        80/TCP              30s

[~]# kubectl describe svc servicegrid-demo-svc
Name:              servicegrid-demo-svc
Namespace:         default
Labels:            superedge.io/grid-selector=servicegrid-demo
                   superedge.io/grid-uniq-key=location
Annotations:       topologyKeys: ["location"]
Selector:          appGrid=echo
Type:              ClusterIP
IP Families:       <none>
IP:                172.16.33.220
IPs:               <none>
Port:              <unset>  80/TCP
TargetPort:        8080/TCP
Endpoints:         10.0.0.136:8080,10.0.0.138:8080,10.0.0.67:8080 + 3 more...
Session Affinity:  None
Events:            <none>

# 在 guangzhou 地域的 pod 中访问 CluserIP，会随机得到 gz-2 gz-3 节点名称，不会访问到 beijing 区域的 Pod；使用 Service 的域名访问效果一致
[~]# curl 172.16.33.220|grep "node name"
        node name:      gz-2
[~]# curl servicegrid-demo-svc.default.svc.cluster.local|grep "node name"
        node name:      gz-3
        
# 在 beijing 地域的 pod 中访问 CluserIP，会随机得到 bj-1 bj-3 节点名称，不会访问到 guangzhou 区域的 Pod；使用 Service 的域名访问效果一致
[~]# curl 172.16.33.220|grep "node name"
        node name:      bj-1
[~]# curl servicegrid-demo-svc.default.svc.cluster.local|grep "node name"
        node name:      bj-3

```

我们在`guangzhou`地域的节点上检查 iptables 规则，代码示例如下：

```shell
-A KUBE-SERVICES -d 172.16.33.220/32 -p tcp -m comment --comment "default/servicegrid-demo-svc: cluster IP" -m tcp --dport 80 -j KUBE-SVC-MLDT4NC26VJPGLP7

-A KUBE-SVC-MLDT4NC26VJPGLP7 -m comment --comment "default/servicegrid-demo-svc:" -m statistic --mode random --probability 0.33333333349 -j KUBE-SEP-Z2EAS2K37V5WRDQC
  -A KUBE-SVC-MLDT4NC26VJPGLP7 -m comment --comment "default/servicegrid-demo-svc:" -m statistic --mode random --probability 0.50000000000 -j KUBE-SEP-PREBTG6M6AFB3QA4
-A KUBE-SVC-MLDT4NC26VJPGLP7 -m comment --comment "default/servicegrid-demo-svc:" -j KUBE-SEP-URDEBXDF3DV5ITUX

-A KUBE-SEP-Z2EAS2K37V5WRDQC -p tcp -m comment --comment "default/servicegrid-demo-svc:" -m tcp -j DNAT --to-destination 10.0.0.136:8080
-A KUBE-SEP-PREBTG6M6AFB3QA4 -p tcp -m comment --comment "default/servicegrid-demo-svc:" -m tcp -j DNAT --to-destination 10.0.0.138:8080
-A KUBE-SEP-URDEBXDF3DV5ITUX -p tcp -m comment --comment "default/servicegrid-demo-svc:" -m tcp -j DNAT --to-destination 10.0.1.7:8080
```

通过 iptables 规则很明显的可以看到对 `servicegrid-demo-svc`的访问分别 redirect 到了 `10.0.0.136`、`10.0.0.138`、`10.0.1.7`这 3 个地址，分别对应的就是 guangzhou 地域的 3 个 pod 的 IP 地址。可以看到，如果是 StatefulsetGrid + 标准 ServiceGrid 访问方式的话，其原理和上面的 DeploymentGrid 原理一致，都是通过`application-grid-wrapper`配合`kube-proxy`修改 iptables 规则来实现的，没有任何区别。

#### StatefusetGrid + Headless Service 支持

StatefulSetGrid 目前支持使用 Headless service **配合 Pod FQDN**的方式进行闭环访问，如下所示：

<div align="left">
  <img src="https://qcloudimg.tencent-cloud.cn/raw/d4e2d4b058d8bf99046e7c252721b6d3.jpg" width=100% title="stsgrid">
</div>




#### 部署 Headless Service

按照下面的模板部署 Headless Service

```yaml
apiVersion: superedge.io/v1
kind: ServiceGrid
metadata:
  name: servicegrid-demo
  namespace: default
spec:
  gridUniqKey: location
  template:
    clusterIP: None
    selector:
      appGrid: echo
    ports:
    - protocol: TCP
      port: 8080
      targetPort: 8080
```

```
[~]# kubectl describe svc servicegrid-demo-svc
Name:              servicegrid-demo-svc
Namespace:         default
Labels:            superedge.io/grid-selector=servicegrid-demo
                   superedge.io/grid-uniq-key=location
Annotations:       topologyKeys: ["location"]
Selector:          appGrid=echo
Type:              ClusterIP
IP Families:       <none>
IP:                None
IPs:               <none>
Port:              <unset>  8080/TCP
TargetPort:        8080/TCP
Endpoints:         10.0.0.136:8080,10.0.0.138:8080,10.0.0.67:8080 + 3 more...
Session Affinity:  None
Events:            <none>
```

这里可以看到 Service 的 ClusterIP 为空，Endpoint 仍然包含 6 个 pod 的 IP 地址，同时，如果通过域名查询 `servicegrid-demo-svc.default.svc.cluster.local`会得到下面的信息：

```shell
[~]# nslookup servicegrid-demo-svc.default.svc.cluster.local
Server:         169.254.20.11
Address:        169.254.20.11#53

Name:   servicegrid-demo-svc.default.svc.cluster.local
Address: 10.0.1.7
Name:   servicegrid-demo-svc.default.svc.cluster.local
Address: 10.0.0.136
Name:   servicegrid-demo-svc.default.svc.cluster.local
Address: 10.0.0.138
Name:   servicegrid-demo-svc.default.svc.cluster.local
Address: 10.0.0.69
Name:   servicegrid-demo-svc.default.svc.cluster.local
Address: 10.0.1.67
Name:   servicegrid-demo-svc.default.svc.cluster.local
Address: 10.0.0.67
```

此时如果我们通过标准的`servicegrid-demo-svc.default.svc.cluster.local`来访问服务，仍然会跨 NodeUnit 随机访问不同的 Endpoint 地址，无法实现流量闭环。

#### 如何在一个 NodeUnit 内支持 Statefulset 标准访问方式？

在一个标准的 K8s 环境中，按照 Statefulset 的标准使用方式，我们会使用一种逻辑来访问 Statefulset 中的 Pod ，类似`Statefulset-0.SVC.NS.svc.cluster.local` 这样的格式，例如我们想要使用`statefulsetgrid-demo-0.servicegrid-demo-svc.default.svc.cluster.local`来访问这个 Statefulset 中的 Pod-0，SuperEdge 针对这个场景进行了多 NodeUnit 的能力适配。

由于 Statefulset 的 Pod 都有独立的 DNS 域名，可以通过 FQDN 方式来访问单独的 pod，例如可以查询`statefulsetgrid-demo-beijing-0`域名：

```shell
[~]# nslookup statefulsetgrid-demo-beijing-0.servicegrid-demo-svc.default.svc.cluster.local
Server:         169.254.20.11
Address:        169.254.20.11#53

Name:   statefulsetgrid-demo-beijing-0.servicegrid-demo-svc.default.svc.cluster.local
Address: 10.0.0.67
```

因此可以开始考虑一种方式，是不是可以抛弃掉 NodeUnit 的标记，直接使用`statefulsetgrid-demo-0.servicegrid-demo-svc.default.svc.cluster.local`的域名来访问本地域的 Statefulset 内的 Pod-0，如下：

- 在`beijing`地域访问的就是`statefulsetgrid-demo-beijing-0.servicegrid-demo-svc.default.svc.cluster.local` 这个 Pod 的 IP。
- 在`guangzhou`地域访问的就是`statefulsetgrid-demo-guangzhou-0.servicegrid-demo-svc.default.svc.cluster.local` 这个 Pod 的 IP。

上图中使用 CoreDNS 两条记录指向相同的 Pod IP ，这个能力就可以实现上述的标准访问需求。因此 **SuperEdge 在产品层面提供了相应的能力**，在公有云产品上需要在控制台手动开启，如下图（如果是 SuperEdge 开源用户，需要独立部署下面的 Daemonset 服务）：

<div align="left">
  <img src="https://qcloudimg.tencent-cloud.cn/raw/bfac0ebb940f7539860e23fcb71be650.png" width=100% title="deploymentgrid">
</div>

当使能 `Edge Headless`开关后，边缘侧节点上都会部署一个服务 `statefulset-grid-daemon`， 这个服务会来更新节点侧的 CoreDNS 信息。

```shell
edge-system   statefulset-grid-daemon-8gtrz      1/1     Running   0          7h42m   172.16.35.193   gz-3   <none>           <none>
edge-system   statefulset-grid-daemon-8xvrg      1/1     Running   0          7h42m   172.16.32.211   gz-2   <none>           <none>
edge-system   statefulset-grid-daemon-ctr6w      1/1     Running   0          7h42m   192.168.10.15   bj-3   <none>           <none>
edge-system   statefulset-grid-daemon-jnvxz      1/1     Running   0          7h42m   192.168.10.12   bj-1   <none>           <none>
edge-system   statefulset-grid-daemon-v9llj      1/1     Running   0          7h42m   172.16.34.168   gz-1   <none>           <none>
edge-system   statefulset-grid-daemon-w7lpt      1/1     Running   0          7h42m   192.168.10.7    bj-2   <none>           <none>
```

现在，在某个 NodeUnit 内使用统一 headless service 访问形式，例如访问如下 DNS 获取的 IP 地址：

```
{StatefulSet}-{0..N-1}.SVC.default.svc.cluster.local
```

实际就会访问这个 NodeUnit 下具体 pod 的 FQDN 地址获取的是同一 Pod IP：

```
{StatefulSet}-{NodeUnit}-{0..N-1}.SVC.default.svc.cluster.local
```

例如，在`beijing`地域访问 `statefulsetgrid-demo-0.servicegrid-demo-svc.default.svc.cluster.local`DNS 的 IP 地址和 `statefulsetgrid-demo-beijing-0.servicegrid-demo-svc.default.svc.cluster.local`域名返回的 IP 地址是一样的，如下图：

```shell
# 在 guangzhou 地域执行 nslookup 指令
[~]# nslookup statefulsetgrid-demo-0.servicegrid-demo-svc.default.svc.cluster.local
Server:         169.254.20.11
Address:        169.254.20.11#53

Name:   statefulsetgrid-demo-0.servicegrid-demo-svc.default.svc.cluster.local
Address: 10.0.0.136

[~]# nslookup statefulsetgrid-demo-guangzhou-0.servicegrid-demo-svc.default.svc.cluster.local
Server:         169.254.20.11
Address:        169.254.20.11#53

Name:   statefulsetgrid-demo-guangzhou-0.servicegrid-demo-svc.default.svc.cluster.local
Address: 10.0.0.136

# 在 beijing 地域执行 nslookup 指令
[~]# nslookup statefulsetgrid-demo-0.servicegrid-demo-svc.default.svc.cluster.local
Server:         169.254.20.11
Address:        169.254.20.11#53

Name:   statefulsetgrid-demo-0.servicegrid-demo-svc.default.svc.cluster.local
Address: 10.0.0.67

[~]# nslookup statefulsetgrid-demo-beijing-0.servicegrid-demo-svc.default.svc.cluster.local
Server:         169.254.20.11
Address:        169.254.20.11#53

Name:   statefulsetgrid-demo-beijing-0.servicegrid-demo-svc.default.svc.cluster.local
Address: 10.0.0.67
```

每个 NodeUnit 通过相同的 headless service 只会访问本 NodeUnit 内的 pod：

```bash
# 在 guangzhou 区域执行下面的命令
[~]# curl statefulsetgrid-demo-0.servicegrid-demo-svc.default.svc.cluster.local:8080 | grep "pod name:"
        pod name:       statefulsetgrid-demo-guangzhou-0
[~]# curl statefulsetgrid-demo-1.servicegrid-demo-svc.default.svc.cluster.local:8080 | grep "pod name:"
        pod name:       statefulsetgrid-demo-guangzhou-1
[~]# curl statefulsetgrid-demo-2.servicegrid-demo-svc.default.svc.cluster.local:8080 | grep "pod name:"
        pod name:       statefulsetgrid-demo-guangzhou-2

# 在 beijing 区域执行下面的命令
[~]# curl statefulsetgrid-demo-0.servicegrid-demo-svc.default.svc.cluster.local:8080 | grep "pod name:"
        pod name:       statefulsetgrid-demo-beijing-0
[~]# curl statefulsetgrid-demo-1.servicegrid-demo-svc.default.svc.cluster.local:8080 | grep "pod name:"
        pod name:       statefulsetgrid-demo-beijing-1
[~]# curl statefulsetgrid-demo-2.servicegrid-demo-svc.default.svc.cluster.local:8080 | grep "pod name:"
        pod name:       statefulsetgrid-demo-beijing-2
```

#### 实现原理

<div align="left">
  <img src="https://qcloudimg.tencent-cloud.cn/raw/1994c43bbce0886f9946dea017b9a960.jpg" width=100% title="statefulsetgrid">
</div>

上图描述了 StatefulsetGrid+Headless Service 的实现原理，主要就是在边缘节点侧部署了`statefulset-grid-daemon`的组件，会监听`StatefulsetGrid`的资源信息；同时刷新边缘侧 CoreDNS 的相关记录，根据所在 NodeUnit 地域，添加`{StatefulSet}-{0..N-1}.SVC.default.svc.cluster.local`域名记录，和标准的 Pod FQDN 记录 `{StatefulSet}-{NodeUnit}-{0..N-1}.SVC.default.svc.cluster.local`指向同一 Pod 的 IP 地址。具体如何实现 CoreDNS 域名更新可以参考源代码实现。




### 按 NodeUnit 灰度

DeploymentGrid 和 StatefulSetGrid 均支持按照 NodeUnit 进行灰度。

#### 重要字段
和灰度功能相关的字段如下：
<table>
<thead>
  <tr>
    <th>字段</th>
    <th>说明</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>templatePool </td>
    <td>用于灰度的 template 集合</td>
  </tr>
  <tr>
    <td>templates</td>
    <td>NodeUnit 和其使用的 templatePool 中的 template 的映射关系，如果没有指定，NodeUnit 使用 defaultTemplateName 指定的 template</td>
  </tr>
  <tr>
    <td>defaultTemplateName</td>
    <td>默认使用的 template，如果不填写或者使用"default"就采用 spec.template</td>
  </tr>
  <tr>
    <td>autoDeleteUnusedTemplate</td>
    <td>默认为 false，如果设置为 true，会自动删除 templatePool 中既不在 templates 中也不在 spec.template 中的 template 模板</td>
  </tr>
</tbody>
</table>

#### 使用相同的 template 创建 workload
和上面的 DeploymentGrid 和 StatefulsetGrid 例子完全一致，如果不需要使用灰度功能，则无需添加额外字段。

#### 使用不同的 template 创建 workload
```yaml
apiVersion: superedge.io/v1
kind: DeploymentGrid
metadata:
  name: deploymentgrid-demo
  namespace: default
spec:
  defaultTemplateName: test1
  gridUniqKey: zone
  template:
    replicas: 1
    selector:
      matchLabels:
        appGrid: echo
    strategy: {}
    template:
      metadata:
        creationTimestamp: null
        labels:
          appGrid: echo
      spec:
        containers:
        - image: superedge/echoserver:2.2
          name: echo
          ports:
          - containerPort: 8080
            protocol: TCP
          env:
            - name: NODE_NAME
              valueFrom:
                fieldRef:
                  fieldPath: spec.nodeName
            - name: POD_NAME
              valueFrom:
                fieldRef:
                  fieldPath: metadata.name
            - name: POD_NAMESPACE
              valueFrom:
                fieldRef:
                  fieldPath: metadata.namespace
            - name: POD_IP
              valueFrom:
                fieldRef:
                  fieldPath: status.podIP
          resources: {}
  templatePool:
    test1:
      replicas: 2
      selector:
        matchLabels:
          appGrid: echo
      strategy: {}
      template:
        metadata:
          creationTimestamp: null
          labels:
            appGrid: echo
        spec:
          containers:
          - image: superedge/echoserver:2.2
            name: echo
            ports:
            - containerPort: 8080
              protocol: TCP
            env:
              - name: NODE_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: spec.nodeName
              - name: POD_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.name
              - name: POD_NAMESPACE
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.namespace
              - name: POD_IP
                valueFrom:
                  fieldRef:
                    fieldPath: status.podIP
            resources: {}
    test2:
      replicas: 3
      selector:
        matchLabels:
          appGrid: echo
      strategy: {}
      template:
        metadata:
          creationTimestamp: null
          labels:
            appGrid: echo
        spec:
          containers:
          - image: superedge/echoserver:2.3
            name: echo
            ports:
            - containerPort: 8080
              protocol: TCP
            env:
              - name: NODE_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: spec.nodeName
              - name: POD_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.name
              - name: POD_NAMESPACE
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.namespace
              - name: POD_IP
                valueFrom:
                  fieldRef:
                    fieldPath: status.podIP
            resources: {}
  templates:
    zone1: test1
    zone2: test2
```
本示例中，NodeUnit zone1 将会使用 test1 template，NodeUnit zone2 将会使用 test2 template，其余 NodeUnit 将会使用 defaultTemplateName 中指定的 template。 

### 多集群分发
支持 DeploymentGrid 和 ServiceGrid 的多集群分发，分发的同时也支持多地域灰度，当前基于的多集群管理方案为 [clusternet](https://github.com/clusternet/clusternet)。

#### 特点
- 支持多集群的按 NodeUnit 灰度。
- 保证控制集群和被纳管集群应用的强一致和同步更新/删除，做到一次操作，多集群部署。
- 在控制集群可以看到聚合的各分发实例的状态。
- 支持节点地域信息更新情况下应用的补充分发：如原先不属于某个 NodeGroup 的集群，更新节点信息后加入了 NodeGroup，控制集群中的应用会及时向该集群补充下发。

#### 前置条件
- 集群部署了 SuperEdge 中的组件，如果没有 Kubernetes 集群，可以通过 edgeadm 进行创建，如果已有 Kubernetes 集群，可以通过 edageadm 的 addon 部署 SuperEdge 相关组件，将集群转换为一个 SuperEdge 边缘集群。
- 通过 clusternet 进行集群的注册和纳管。

#### 重要字段
如果要指定某个 DeploymentGrid 或 ServiceGrid 需要进行多集群的分发，则在其 label 中添加`superedge.io/fed`，并置为"yes"。

#### 使用示例
创建 3 个集群，分别为一个管控集群和 2 个被纳管的边缘集群 A,B，通过 clusternet 进行注册和纳管。其中 A 集群中一个节点添加 zone: zone1 的 label，加入 NodeUnit zone1；集群 B 不加入 NodeGroup。

在管控集群中创建 DeploymentGrid，其中 labels 中添加了 superedge.io/fed: "yes"，表示该 DeploymentGrid 需要进行集群的分发，同时灰度指定分发出去的应用在 zone1 和 zone2 中使用不同的副本个数。
```yaml
apiVersion: superedge.io/v1
kind: DeploymentGrid
metadata:
  name: deploymentgrid-demo
  namespace: default
  labels:
    superedge.io/fed: "yes"
spec:
  defaultTemplateName: test1
  gridUniqKey: zone
  template:
    replicas: 1
    selector:
      matchLabels:
        appGrid: echo
    strategy: {}
    template:
      metadata:
        creationTimestamp: null
        labels:
          appGrid: echo
      spec:
        containers:
        - image: superedge/echoserver:2.2
          name: echo
          ports:
          - containerPort: 8080
            protocol: TCP
          env:
            - name: NODE_NAME
              valueFrom:
                fieldRef:
                  fieldPath: spec.nodeName
            - name: POD_NAME
              valueFrom:
                fieldRef:
                  fieldPath: metadata.name
            - name: POD_NAMESPACE
              valueFrom:
                fieldRef:
                  fieldPath: metadata.namespace
            - name: POD_IP
              valueFrom:
                fieldRef:
                  fieldPath: status.podIP
          resources: {}
  templatePool:
    test1:
      replicas: 2
      selector:
        matchLabels:
          appGrid: echo
      strategy: {}
      template:
        metadata:
          creationTimestamp: null
          labels:
            appGrid: echo
        spec:
          containers:
          - image: superedge/echoserver:2.2
            name: echo
            ports:
            - containerPort: 8080
              protocol: TCP
            env:
              - name: NODE_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: spec.nodeName
              - name: POD_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.name
              - name: POD_NAMESPACE
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.namespace
              - name: POD_IP
                valueFrom:
                  fieldRef:
                    fieldPath: status.podIP
            resources: {}
    test2:
      replicas: 3
      selector:
        matchLabels:
          appGrid: echo
      strategy: {}
      template:
        metadata:
          creationTimestamp: null
          labels:
            appGrid: echo
        spec:
          containers:
          - image: superedge/echoserver:2.2
            name: echo
            ports:
            - containerPort: 8080
              protocol: TCP
            env:
              - name: NODE_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: spec.nodeName
              - name: POD_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.name
              - name: POD_NAMESPACE
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.namespace
              - name: POD_IP
                valueFrom:
                  fieldRef:
                    fieldPath: status.podIP
            resources: {}
  templates:
    zone1: test1
    zone2: test2
```

创建完成后，可以看到在纳管的 A 集群中，创建了对应的 Deployment，而且依照其 NodeUnit 信息，有两个实例。
```bash
[root@VM-0-174-centos ~]# kubectl get deploy
NAME                        READY   UP-TO-DATE   AVAILABLE   AGE
deploymentgrid-demo-zone1   2/2     2            2           99s
```
如果在纳管的 A 集群中手动更改了 deployment 的相应字段，会以管控集群为模板更新回来。

B 集群中的一个节点添加 zone: zone2 的 label，将其加入 NodeUnit zone2，管控集群会及时向该集群补充下发 zone2 对应的应用。
```bash
[root@VM-0-42-centos ~]# kubectl get deploy
NAME                        READY   UP-TO-DATE   AVAILABLE   AGE
deploymentgrid-demo-zone2   3/3     3            3           6s
```

在管控集群查看 deploymentgrid-demo 的状态，可以看到被聚合在一起的各个被纳管集群的应用状态，便于查看。
```yaml
status:
  states:
    zone1:
      conditions:
      - lastTransitionTime: "2021-06-17T07:33:50Z"
        lastUpdateTime: "2021-06-17T07:33:50Z"
        message: Deployment has minimum availability.
        reason: MinimumReplicasAvailable
        status: "True"
        type: Available
      readyReplicas: 2
      replicas: 2
    zone2:
      conditions:
      - lastTransitionTime: "2021-06-17T07:37:12Z"
        lastUpdateTime: "2021-06-17T07:37:12Z"
        message: Deployment has minimum availability.
        reason: MinimumReplicasAvailable
        status: "True"
        type: Available
      readyReplicas: 3
      replicas: 3
```

## 相关文档

* [SEP: ServiceGroup StatefulSetGrid Design Specification](https://github.com/superedge/superedge/issues/26)
