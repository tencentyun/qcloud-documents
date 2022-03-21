
## 现象描述

当用户在使用 Nginx Ingress 时，减少 Nginx Ingress Controller 副本过程中，可能出现 Connection Refused 的问题，此时 CLB 批量解绑 RS，TCP/UDP 监听器存量连接停止转发。




## 可能原因

查看 [Nginx Ingress](https://github.com/kubernetes/ingress-nginx/blob/main/cmd/waitshutdown/main.go) 源码，Nginx Ingress Controller 工作负载没有优雅停机的能力， Pod 在收到 kill signal 之后直接退出。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/5f0c9f052d67d6e25d249c0c88a633c6.png)



## 解决思路

若您使用 TKE [Service 优雅停机](https://cloud.tencent.com/document/product/457/60064) 的能力，当 Pod 需要被删除时，Pod 能够处理完已接受到的请求，此时入流量关闭，但出流量仍能走通。直到处理完所有已有请求和 Pod 真正删除时，出入流量才进行关闭。待到优雅停机时间结束后，Pod 才被真正的删除。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/c86a0aab1d6f4d3be656b2267a6678f5.png)





## 处理步骤
>! 仅针对 [直连场景](https://cloud.tencent.com/document/product/457/41897) 生效，请检查您的集群是否支持直连模式。

#### 步骤1
在 kube-system 命名空间下名为 ****-ingress-nginx-controller 的 Service 里使用 Annotation 标明使用优雅停机。

以下为使用 Annotation 标明使用优雅停机示例，完整 Service Annotation 说明可参见 [Service Annotation 说明](https://cloud.tencent.com/document/product/457/51258)。


```
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
```


#### 步骤2
在 kube-system 命名空间下名为 ****-ingress-nginx-controller 的 Deployment 里的 wait-shutdown 前面加一段时间的 sleep。示例如下：
```
  lifecycle:
          preStop:
            exec:
              command:
              - sleep                        # 添加 sleep 时间
              - 30s                          # 添加 sleep 时间
              - /wait-shutdown      # 在这一行前，添加 sleep 时间
```

更多内容请参考 [Service 优雅停机](https://cloud.tencent.com/document/product/457/60064)。如果通过以上步骤仍无法解决您的问题，您可以通过 [在线支持](https://cloud.tencent.com/online-service?source=PRESALE&from=doc_457) 反馈和解决问题。
