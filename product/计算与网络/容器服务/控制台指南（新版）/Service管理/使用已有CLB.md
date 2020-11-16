

腾讯云容器服务 TKE 具备通过 `service.kubernetes.io/tke-existed-lbid: <LoadBalanceId>` 注解实现使用已有负载均衡的功能，您可使用该注解指定集群 Service 资源关联的负载均衡实例。还提供了 **Service 负载均衡复用**功能，即指定多个 Service 使用同一个已有负载均衡，您可参考本文进行设置。

## 使用已有负载均衡的同步行为
* 使用已有负载均衡时，指定 Service 的网络类型的注解不生效。
* 当 Service 不再使用已有负载均衡时，该 Service 描述的对应监听器会删除，该负载均衡将保留。
删除监听器时，会校验监听器名称是否被修改。如果用户修改监听器名称，则认为该监听器可能由用户创建，不进行主动删除。
* 如果 Service 目前正在使用自动创建的负载均衡，那么给它添加使用已有负载均衡的注解，会使得当前负载均衡的生命周期结束并释放，Service 的配置将会与该负载均衡进行同步。反之，如果删除 Service 正在使用的已有负载均衡的注解，Service Controller 组件将会为该 Service 创建负载均衡并进行同步。


## 使用已有负载均衡同步腾讯云标签行为
- 默认情况下，Service 创建的 CLB 均会配置 `tke-createdBy-flag = yes` 标签，Service 会在销毁时删除对应资源。若使用已有 CLB，则不会配置该标签，Service 销毁时也不会删除对应资源。
- 所有 Service 均会配置 `tke-clusterId = ` 标签，若 ClusterId 正确，则 Service 会在销毁时删除对应标签。
- 于2020年8月17日起创建的集群，将默认关闭多个 Service 复用相同 CLB 的功能。该日期前后集群内 Service 创建的 CLB 标签配置规则变更情况及详细信息，请参见  [多 Service 复用 CLB](https://cloud.tencent.com/document/product/457/46370)。




## 注意事项
- 指定使用的负载均衡需和集群处于同一 VPC。
- 请确保您的容器业务不和云服务器 CVM 业务共用一个负载均衡。
- 不支持您在负载均衡控制台操作 TKE 所管理负载均衡的监听器和后端绑定的服务器，您的更改会被 TKE 的自动同步所覆盖。
- 使用已有的负载均衡时：
  - Service Controller 将不负责该已有负载均衡的释放与回收。
  - 仅支持使用通过负载均衡控制台创建的负载均衡器，不支持复用由 TKE 自动创建的负载均衡，会破坏其他 Service 负载均衡的生命周期管理。
-  **复用**负载均衡时：
  - 不支持跨集群复用负载均衡。
  - 您需要使用**复用**功能时，建议有明确的监听器端口管理，否则负载均衡在多个 Service 的使用下，会出现管理混乱。
  - 复用负载均衡的端口冲突时，将会被拒绝。如果在修改中出现冲突，那么出现冲突的监听器后端同步无法确保正确。
  - 复用负载均衡的 Service 不支持开启 Local 访问（传统型负载均衡限制）。
  - 删除 Service，则复用负载均衡绑定的后端云服务器需要自行解绑，同时会保留一个 tag `tke-clusterId: cls-xxxx`，需自行清理。


## Service 示例
```Yaml
apiVersion: v1
kind: Service
metadata:
  annotations:
    service.kubernetes.io/tke-existed-lbid: lb-6swtxxxx
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
>?
>- `service.kubernetes.io/tke-existed-lbid: lb-6swtxxxx` 注解表示该 Service 将使用已有负载均衡进行配置。
>- 请注意 Service 的类型，需设置为 `LoadBalancer` 类型。


## 使用场景示例
### 使用包年包月的负载均衡对外提供服务
Service Controller 组件管理负载均衡生命周期时，仅支持购买按量计费的负载均衡资源。当用户需要长时间使用负载均衡时，包年包月计费模式在价格上有一定的优势。在此类场景下，用户就可以独立购买和管理负载均衡，再通过注解控制 Service 使用已有负载均衡，并将负载均衡的生命周期管理从 Service Controller 组件中剥离。

### 在同一端口暴露 TCP 和 UDP 服务
Kubernetes 官方在 Service 的设计中具有限制：一个 Service 下暴露的多个端口协议必须相同。有许多游戏场景下的用户，有在同一个端口同时暴露 TCP 和 UDP 服务的需求，腾讯云负载均衡服务支持在同一个端口上同时监听 UDP 和 TCP 协议，此需求可以通过 Service 负载均衡复用来解决。
例如以下 Service 配置，`game-service` 被描述为两个 Service 资源，描述的内容除了监听的协议以外基本相同。两个 Service 都通过注解指定使用已有负载均衡 `lb-6swtxxxx`。通过 kubectl 将以上资源应用到集群中，就可以实现在同一个负载均衡的端口上暴露多种协议的目的。
```
apiVersion: v1
kind: Service
metadata:
  annotations:
    service.kubernetes.io/tke-existed-lbid: lb-6swtxxxx
  name: game-service-a
spec:
  ports:
    - name: 80-80-tcp
      port: 80
      protocol: TCP
      targetPort: 80
  selector:
    app: game
  type: LoadBalancer
------------------------------------------------
apiVersion: v1
kind: Service
metadata:
  annotations:
    service.kubernetes.io/tke-existed-lbid: lb-6swtxxxx
  name: game-service-b
spec:
  ports:
    - name: 80-80-udp
      port: 80
      protocol: UCP
      targetPort: 80
  selector:
    app: game
  type: LoadBalancer
```
