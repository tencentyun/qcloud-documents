
<dx-alert infotype="explain" title="">
日志服务 CLS 为容器服务 TKE 产生的所有审计、事件数据提供**免费服务**至2021年12月31日。请选择自动创建日志集，或在已有日志集中选择自动创建日志主题。活动详情请参见 [TKE 容器服务审计与事件中心日志免费说明](https://cloud.tencent.com/document/product/614/47116#tke-.E5.AE.B9.E5.99.A8.E6.9C.8D.E5.8A.A1.E5.AE.A1.E8.AE.A1.E4.B8.8E.E4.BA.8B.E4.BB.B6.E4.B8.AD.E5.BF.83.E6.97.A5.E5.BF.97.E5.85.8D.E8.B4.B9.E8.AF.B4.E6.98.8E)。
</dx-alert>


## 简介
集群审计是基于 [Kubernetes Audit](https://kubernetes.io/docs/tasks/debug-application-cluster/audit) 对 kube-apiserver 产生的可配置策略的 JSON 结构日志的记录存储及检索功能。本功能记录了对 kube-apiserver 的访问事件，会按顺序记录每个用

## 简介

基于接入层直连 Pod 的场景，当后端进行滚动更新，或后端 Pod 被删除时，如果直接将 Pod 从 LB 的后端摘除，无法处理 Pod 已接收但还未处理的请求。
特别是长链接的场景，例如会议业务，如果直接更新或删除工作负载的 Pod，此时会议会直接中断。

## 应用场景

- 更新工作负载时，Pod 的优雅退出，使客户端不会感受到更新时产生的抖动和错误
- 当 Pod 需要被删除时，Pod 能够处理完已接受到的请求，此时入流量关闭，但出流量仍能走通。直到处理完所有已有请求后，Pod 会真正删除时，出入流量才都关闭。


>!仅针对 [直连场景](https://cloud.tencent.com/document/product/457/41897) 生效，请检查您的集群是否支持直连模式

## 操作步骤

### 步骤1：使用 Annotation 标明使用优雅停机


以下为使用 Annotation 标明使用优雅停机示例，完整 Ingress Annotation 说明可参见 [Service Annotation 说明](https://cloud.tencent.com/document/product/457/51258) 文档。

```yaml
kind: Ingress
apiVersion: v1
metadata:
  annotations:
    ingress.cloud.tencent.com/direct-access: "true" ## 开启直连 Pod 模式
    ingress.cloud.tencent.com/enable-grace-shutdown: "true"  # 表示使用优雅停机
  name: my-Ingress
spec:
  selector:
    app: MyApp
...
```



### 步骤2：配合在需要优雅停机的工作负载里使用 preStop 和 terminationGracePeriodSeconds

步骤2为在需要优雅停机的工作负载里配合使用 preStop 和 terminationGracePeriodSeconds。


#### 容器终止流程


以下为容器在 Kubernetes 环境中的终止流程：

1. Pod 被删除，状态置为 Terminating。
2. kube-proxy 更新转发规则，将 Pod 从 Ingress 的 endpoint 列表中摘除掉，新的流量不再转发到该 Pod。
3. 如果 Pod 配置了 preStop Hook ，将会执行。
4. kubelet 对 Pod 中各个 container 发送 SIGTERM 信号以通知容器进程开始优雅停止。
5. 等待容器进程完全停止，如果在 terminationGracePeriodSeconds 内 (默认 30s) 还未完全停止，就发送 SIGKILL 信号强制停止进程。
6. 所有容器进程终止，清理 Pod 资源。


#### 具体操作步骤

1. **使用 preStop**
要实现优雅终止，务必在业务代码里处理 SIGTERM 信号。主要逻辑是不接受新的流量进入，继续处理存量流量，所有连接全部断开才退出，了解更多可参见 [示例](https://gobyexample.com/signals)。
若您的业务代码中未处理 SIGTERM 信号，或者您无法控制使用的第三方库或系统来增加优雅终止的逻辑，也可以尝试为 Pod 配置下 preStop，在其实现优雅终止的逻辑，示例如下：
<dx-codeblock>
:::  yaml
apiVersion: v1
kind: Pod
metadata: 
  name: lifecycle-demo
spec: 
  containers: 
  - name: lifecycle-demo-container
    image: nginx
    lifecycle: 
      preStop: 
        exec: 
          command: 
          - /clean.sh
:::
</dx-codeblock>
更多关于 preStop 的配置请参见 <a href="https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#lifecycle-1">Kubernetes API</a> 文档。

 在某些极端情况下，Pod 被删除的一小段时间内，仍然可能有新连接被转发过来，因为 kubelet 与 kube-proxy 同时 watch 到 Pod 被删除，kubelet 有可能在 kube-proxy 同步完规则前就已停止容器，这时可能导致一些新的连接被转发到正在删除的 Pod，而通常情况下，当应用受到 SIGTERM 后都不再接受新连接，只保持存量连接继续处理，因此可能导致 Pod 删除的瞬间部分请求失败。

 针对上述情况，可以利用 preStop 先 sleep 短暂时间，等待 kube-proxy 完成规则同步再开始停止容器内进程。示例如下：
<dx-codeblock>
:::  yaml
apiVersion: v1
kind: Pod 
metadata: 
  name: lifecycle-demo
spec: 
  containers: 
  - name: lifecycle-demo-container
    image: nginx 
    lifecycle: 
      preStop: 
        exec: 
          command: 
          - sleep
          - 5s
:::
</dx-codeblock>
2. **使用 terminationGracePeriodSeconds 调整优雅时长**
如果需要的优雅终止时间比较长 (preStop + 业务进程停止可能超过 30s)，可根据实际情况自定义 terminationGracePeriodSeconds，避免过早的被 SIGKILL 停止，示例如下：
<dx-codeblock>
:::  yaml
apiVersion: v1
kind: Pod
metadata: 
  name: grace-demo
spec: 
  terminationGracePeriodSeconds: 60 # 优雅停机默认30s，您可以设置更长的时间
  containers: 
  - name: lifecycle-demo-container
    image: nginx
    lifecycle: 
      preStop: 
        exec: 
          command: 
          - sleep
          - 5s
:::
</dx-codeblock>
户、管理员或系统组件影响集群的活动。


## 功能优势
集群审计功能提供了区别于 metrics 的另一种集群观测维度。开启集群审计后，Kubernetes 可以记录每一次对集群操作的审计日志。每一条审计日志是一个 JSON 格式的结构化记录，包括元数据（metadata）、请求内容（requestObject）和响应内容（responseObject）三个部分。其中元数据（包含了请求的上下文信息，例如谁发起的请求、从哪里发起的、访问的 URI 等信息）一定存在，请求和响应内容是否存在取决于审计级别。通过日志可以了解到以下内容：
- 集群里发生的活动。
- 活动的发生时间及发生对象。
- 活动的触发时间、触发位置及观察点。
- 活动的结果以及后续处理行为。



### 阅读审计日志
```json
{
  "kind":"Event",
  "apiVersion":"audit.k8s.io/v1",
  "level":"RequestResponse",
  "auditID":0a4376d5-307a-4e16-a049-24e017******,
  "stage":"ResponseComplete",
  // 发生了什么
  "requestURI":"/apis/apps/v1/namespaces/default/deployments",
  "verb":"create",
  // 谁发起的
  "user":{
    "username":"admin",
      "uid":"admin",
      "groups":[
        "system:masters",
        "system:authenticated"
      ]
  },
  // 从哪里发起
  "sourceIPs":[
    "10.0.6.68"
  ],
  "userAgent":"kubectl/v1.16.3 (linux/amd64) kubernetes/ald64d8",
  // 发生了什么
  "objectRef":{
    "resource":"deployments",
    "namespace":"default",
    "name":"nginx-deployment",
    "apiGroup":"apps",
    "apiVersion":"v1"
  },
  // 结果是什么
  "responseStatus":{
    "metadata":{
    },
    "code":201
  },
  // 请求及返回具体信息
  "requestObject":Object{...},
  "responseObject":Object{...},
  // 什么时候开始/结束
  "requestReceivedTimestamp":"2020-04-10T10:47:34.315746Z",
  "stageTimestamp":"2020-04-10T10:47:34.328942Z",
  // 请求被接收/拒绝的原因是什么
  "annotations":{
    "authorization.k8s.io/decision":"allow",
    "authorization.k8s.io/reason":""
  }
}
```




## EKS 集群审计策略

### 审计级别（level）

和一般日志不同，kuberenetes 审计日志的级别更像是一种 verbose 配置，用于标示记录信息的详细程度。一共有4个级别，可参考以下表格内容：

| 参数| 说明 | 
|---------|---------|
| None | 不记录。 | 
| Metadata | 记录请求的元数据（例如用户、时间、资源、操作等），不包括请求和响应的消息体。 |
| Request | 除了元数据外，还包括请求消息体，不包括响应消息体。 |
| RequestResponse | 记录所有信息，包括元数据以及请求、响应的消息体。 |

### 审计阶段（stage）

记录日志可以发生在不同的阶段，参考以下表格内容：

| 参数| 说明 | 
|---------|---------|
| RequestReceived | 一收到请求就记录。 | 
| ResponseStarted | 返回消息头发送完毕后记录，只针对 watch 之类的长连接请求。 | 
| ResponseComplete | 返回消息全部发送完毕后记录。 | 
| Panic | 内部服务器出错，请求未完成。 | 



### EKS 审计策略

EKS 默认收到请求即会记录审计日志，且大部分的操作会记录 RequestResponse 级别的审计日志。但也会存在如下情况：
- get、list 和 watch 会记录 Request 级别的日志。
- 针对 secrets 资源、configmaps 资源或 tokenreviews 资源的请求会在 Metadata 级别记录。

以下请求将不会进行记录日志：
- `system:kube-proxy` 发出的监视 endpoints 资源、services 资源或 services/status 资源的请求。
- `system:unsecured` 发出的针对 kube-system 命名空间中 configmaps 资源的 get 请求。
- kubelet 发出的针对 nodes 资源或 nodes/status 资源的 get 请求。
- `system:kube-controller-manager`、`system:kube-scheduler` 或 `system:serviceaccount:endpoint-controller` 发出的针对 kube-system 命名空间中 endpoints 资源的 get 和 update 请求。
- `system:apiserver` 发出的针对 namespaces 资源、namespaces/status 资源或 namespaces/finalize 资源的 get 请求。
- 对与 `/healthz*`、`/version` 或` /swagger*` 匹配的网址发出的请求。


## 操作步骤 

### 开启集群审计

>! 开启集群审计功能需要重启 kube-apiserver ，建议不要频繁开关。

1. 登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 选择左侧导航栏中的【集群运维】>【功能管理】，进入“功能管理”页面。
3. 在“功能管理”页面上方选择地域、选择“弹性集群”类型。如下图所示：
![](https://main.qcloudimg.com/raw/7eb5a0cf87aed669bd8facd5c12268ab.png)
4. 在下方集群列表找到您希望开启集群审计的集群，在其右侧操作栏中单击【设置】。
5. 在弹出的“设置功能”窗口，单击“集群审计”功能右侧的【编辑】。如下图所示：
![](https://main.qcloudimg.com/raw/3fe831d3dfce50a0034a754f487faa89.png)
5. 勾选【开启集群审计】，选择存储审计日志的日志集和日志主题，推荐选择【自动创建日志主题】。如下图所示：
![](https://main.qcloudimg.com/raw/df43fa7f0a495eb904fc2a9bbc65ad7c.png)
6. 单击【确定】即可开启集群审计功能。



