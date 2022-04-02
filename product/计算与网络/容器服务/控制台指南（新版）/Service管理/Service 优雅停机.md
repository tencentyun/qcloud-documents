
## 简介

基于接入层直连 Pod 的场景，当后端进行滚动更新或后端 Pod 被删除时，如果直接将 Pod 从 LB 的后端摘除，则无法处理 Pod 已接收但还未处理的请求。
特别是长链接的场景，例如会议业务，如果直接更新或删除工作负载的 Pod，此时会议会直接中断。

## 应用场景

- 更新工作负载时，Pod 的优雅退出，使客户端不会感受到更新时产生的抖动和错误。
- 当 Pod 需要被删除时，Pod 能够处理完已接受到的请求，此时入流量关闭，但出流量仍能走通。直到处理完所有已有请求和 Pod 真正删除时，出入流量才进行关闭。


>!仅针对 [直连场景](https://cloud.tencent.com/document/product/457/41897) 生效，请检查您的集群是否支持直连模式。


## 操作步骤

### 步骤1：使用 Annotation 标明使用优雅停机

以下为使用 Annotation 标明使用优雅停机示例，完整 Service Annotation 说明可参见 [Service Annotation 说明](https://cloud.tencent.com/document/product/457/51258)。

<dx-codeblock>
:::  yaml
kind: Service
apiVersion: v1
metadata: 
  annotations: 
    service.cloud.tencent.com/direct-access: "true" ## 开启直连 Pod 模式
    service.cloud.tencent.com/enable-grace-shutdown: "true"  # 表示使用优雅停机
  name: my-service
spec: 
  selector: 
    app: MyApp
:::
</dx-codeblock>




### 步骤2：使用 preStop 和 terminationGracePeriodSeconds




步骤2为在需要优雅停机的工作负载里配合使用 preStop 和 terminationGracePeriodSeconds。

#### 容器终止流程

以下为容器在 Kubernetes 环境中的终止流程：

1. Pod 被删除，状态置为 Terminating。
2. kube-proxy 更新转发规则，将 Pod 从 service 的 endpoint 列表中摘除掉，新的流量不再转发到该 Pod。
3. 如果 Pod 配置了 preStop Hook ，将会执行。
4. kubelet 将对 Pod 中各个 container 发送 SIGTERM 信号，以通知容器进程开始优雅停止。
5. 等待容器进程完全停止，如果在 terminationGracePeriodSeconds 内 (默认30s) 还未完全停止，将发送 SIGKILL 信号强制停止进程。
6. 所有容器进程终止，清理 Pod 资源。




#### 具体操作步骤

1. **使用 preStop**
要实现优雅终止，务必在业务代码里处理 SIGTERM 信号。主要逻辑是不接受新的流量进入，继续处理存量流量，所有连接全部断开才退出，了解更多可参见 [示例](https://gobyexample.com/signals)。
若您的业务代码中未处理 SIGTERM 信号，或者您无法控制使用的第三方库或系统来增加优雅终止的逻辑，也可以尝试为 Pod 配置 preStop，在其实现优雅终止的逻辑，示例如下：
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
...
:::
</dx-codeblock>
更多关于 preStop 的配置请参见 <a href="https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#lifecycle-1">Kubernetes API</a> 文档。

 在某些极端情况下，Pod 被删除的一小段时间内，仍然可能有新连接被转发过来，因为 kubelet 与 kube-proxy 同时 watch 到 Pod 被删除，kubelet 有可能在 kube-proxy 同步完规则前就已经停止容器，这时可能导致一些新的连接被转发到正在删除的 Pod，而通常情况下，当应用受到 SIGTERM 后都不再接受新连接，只保持存量连接继续处理，因此可能导致 Pod 删除的瞬间部分请求失败。

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
如果需要优雅终止时间较长 (preStop + 业务进程停止可能超过30s)，可根据实际情况自定义 terminationGracePeriodSeconds，避免过早的被 SIGKILL 停止，示例如下：
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
...
:::
</dx-codeblock>


## 相关文档
- 故障处理：[Nginx Ingress Controller 后端解绑不优雅的问题](https://cloud.tencent.com/document/product/457/71216)
