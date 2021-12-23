
## 默认后端选择

默认情况下，Service 会配置负载均衡的后端到集群节点的 NodePort，如下图 TKE 接入层组件部分。此方案具有非常高的容错性，流量从负载均衡到任何一个 NodePort 之后，NodePort 会再一次随机选择一个 Pod 将流量转发过去。同时这也是 Kubernetes 官方提出的最基础的网络接入层方案。如下图所示：
![A.png](https://main.qcloudimg.com/raw/958fdb435750a042ac745ad4871e0a55.png)

`TKE Service Controller` 默认不会将以下节点作为负载均衡后端：
- Master 节点（不允许 Master 节点参与网络接入层的负载）。
- 节点状态为 NotReady 或节点被设置为 Unschedulable（节点不健康或不可调度）。



## 指定接入层后端
对于一些规模很大的集群，Service 管理的负载均衡会挂载几乎所有集群节点的 NodePort 作为后端。此场景存在以下问题：
- 负载均衡的后端数量有数量限制。
- 负载均衡会对每一个 NodePort 进行健康检查，所有健康检查都会请求到后端的工作负载上。

此类问题可通过以下方式进行解决：
在一些大规模集群的场景中，用户可以通过 `service.kubernetes.io/qcloud-loadbalancer-backends-label` 注解指定一部分节点进行绑定。`service.kubernetes.io/qcloud-loadbalancer-backends-label` 的内容是一个标签选择器，用户可以通过在集群节点上标记 Label，然后在 Service 中通过该注解描述的标签选择器，选择匹配的节点进行绑定。这个同步会持续进行，当节点发生变化导致其被选择或是不再被选择时，Service Controller 会对应添加或删除负载均衡上的对应后端。详情请参见 [Kubernetes 标签与选择器](https://kubernetes.io/zh/docs/concepts/overview/working-with-objects/labels/)。

### 注意事项
- 当 `service.kubernetes.io/qcloud-loadbalancer-backends-label` 的选择器没有选取到任何节点的时候，服务的后端将会被排空，会使得服务中断。使用此功能时，需要对集群节点的 Label 有一定的管理。
- 新增符合要求的节点或变更存量节点也会触发 controller 更新。
- 仅适用于处理低流量、低负载的业务，不建议在生产环境中使用。

### 使用场景
#### 大规模集群下的测试应用
在一个大规模集群下，部署一个仅包含一两个 Pod 的测试应用。通过 Service 进行服务暴露时，负载均衡将对所有的后端 NodePort 进行健康检查，此健康检查的请求量对测试应用有很大影响。此时可以在集群中通过 Label 指定一小部分节点作为后端，缓解健康检查带来的压力。详情请参见 [关于健康检查探测频率过高的说明](https://cloud.tencent.com/document/product/214/3394#.E5.81.A5.E5.BA.B7.E6.A3.80.E6.9F.A5.E6.8E.A2.E6.B5.8B.E9.A2.91.E7.8E.87.E8.BF.87.E9.AB.98)。

### 示例
```
apiVersion: v1
kind: Service
metadata:
  annotations:
    service.kubernetes.io/qcloud-loadbalancer-backends-label: "group=access-layer"
  name: nginx-service
spec:
  ports:
    - name: 80-80-no
      port: 80
      protocol: TCP
      targetPort: 80
  selector:
    app: nginx
  type: LoadBalancer
```
该示例包含以下配置：
- 描述了一个公网类型负载均衡的服务暴露。
- `service.kubernetes.io/qcloud-loadbalancer-backends-label` 注解声明了后端选择器，仅支持集群节点上有 `group=access-layer` Label 的节点才会作为这个负载均衡的后端。




## Service Local 模式
Kubernetes 提供了 Service 特性 `ExternalTrafficPolicy`。当 `ExternalTrafficPolicy` 设置为 Local 时，可以避免流量通过 NAT 在节点间的转发，减少了 NAT 操作也使得源 IP 得到了保留。NodePort 仅会将流量转发到当前节点的 Pod。Local 模式特点如下：
* 优点：
 - 避免了 NAT 与节点间转发带来的性能损失。
  2. 为服务端保留了请求来源 IP。
* 缺点：
  - 没有工作负载的节点，NodePort 将无法提供服务。

### 注意事项
负载均衡的同步是需要时间的。当 Local 类型的服务工作负载数量很少时，工作负载的飘移或滚动更新会很快。此时后端如未来得及同步，后端的服务可能会出现不可用的情况。


#### 示例：Service 开启 Local 转发（externalTrafficPolicy: Local）
```
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  externalTrafficPolicy: Local
  ports:
    - name: 80-80-no
      port: 80
      protocol: TCP
      targetPort: 80
  selector:
    app: nginx
  type: LoadBalancer
```


### Local 默认后端选择
默认情况下，当 Service 开启 Local 模式之后，仍会按默认方式挂载几乎所有节点的 NodePort 作为后端。负载均衡会根据健康检查的结果，避免流量进入没有工作负载的后端节点。为了避免这些没有工作负载的后端被绑定，用户可以通过 `service.kubernetes.io/local-svc-only-bind-node-with-pod: "true"` 注解，在 Local 模式下指定绑定有工作负载节点作为后端。更多信息请参考 [Kubernetes Service Local](https://kubernetes.io/zh/docs/tutorials/services/source-ip/)。

#### 示例：Service 开启 Local 转发并开启 Local 绑定
```
apiVersion: v1
kind: Service
metadata:
  annotations:
    service.kubernetes.io/local-svc-only-bind-node-with-pod: "true"
  name: nginx-service
spec:
  externalTrafficPolicy: Local
  ports:
    - name: 80-80-no
      port: 80
      protocol: TCP
      targetPort: 80
  selector:
    app: nginx
  type: LoadBalancer
```

由于 Local 模式下，进入节点的请求流量不会在节点间转发。所以当节点上的工作负载数量不一致的时候，同样的后端权重可能会使得每一个节点上的负载不平均。此时用户可以通过 `service.cloud.tencent.com/local-svc-weighted-balance: "true"` 进行加权平衡。使用此注解时，NodePort 后端的权重将由节点上工作负载的数量决定，从而避免不同节点上工作负载数量不同带来的负载不均的问题。其中，**Local 加权平衡必须和 Local 绑定同时使用**。示例如下：

#### 示例：Service 开启 Local 转发，并开启 Local 绑定与 Local 加权平衡
```
apiVersion: v1
kind: Service
metadata:
  annotations:
    service.kubernetes.io/local-svc-only-bind-node-with-pod: "true"
    service.cloud.tencent.com/local-svc-weighted-balance: "true"
  name: nginx-service
spec:
  externalTrafficPolicy: Local
  ports:
    - name: 80-80-no
      port: 80
      protocol: TCP
      targetPort: 80
  selector:
    app: nginx
  type: LoadBalancer
```


