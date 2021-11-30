## 使用场景

通过额外节点 Label 的使用，您可以直接将请求转发到某个服务下的具有指定 Label 的 Pod，精细需要控制转发的 Pod。

例如：defaul 命名空间下，存在 Label 为 app: httpbin 和 version: v1 的 Pod， 也存在 app: httpbin 和 version: v2 的 Pod，存在一个 httpbin 服务（selector 选择的是 app:httpbin）。如果希望 API 网关只转发到 Label 为 app: httpbin 和 version: v1 的 Pod， 可以通过额外节点 Label，加上version: v1的配置，就可以实现。

## 操作步骤

1. 在 [配置 TKE 通道](https://cloud.tencent.com/document/product/628/64688) 的服务前提下，再手动输入额外节点 Label。效果如下：
![](https://qcloudimg.tencent-cloud.cn/raw/02e06bdebb15e79706fd231d6b3aae54.png)        
2. 单击**保存**，新建或修改 TKE 通道。
  最终转发的效果如下：
   ![](https://qcloudimg.tencent-cloud.cn/raw/80e178d36f3147eceb00a1ed6ebf1fcf.png)


## 原理说明

TKE 集群中，服务本身是有 selector 的配置。例如：httpbin 服务中，selector 的配置是 app: httpbin，但是 API 网关提供的额外节点Label 会与 httpbin 服务中的 selector 合并起来，组合成的 Label 是：app: httpbin 和 version: v1。 因此，改 TKE 通道节点，只会出现 version: v1的 http 的 Pod。

如果在额外节点 Label 中输入在 httpbin 服务中已经存在的 Label 的键，那么额外节点中输入的该 Label 会被忽略，以 selector 中存在的 Label 的值为准。例如：额外 Label 中输入 app: not-httpbin，这个 Label 与服务 httpbin 的 selector 发生了冲突，app: not-httpbin 将会被忽略。

httpbin 服务的 YAML 如下：
```yaml
apiVersion: v1
kind: Service
metadata:
  name: httpbin
  labels:
    app: httpbin
    service: httpbin
spec:
  ports:
  - name: http
    port: 8000
    targetPort: 80
  selector:
    app: httpbin
```



## 注意事项

- 额外节点 Label 是高级功能，需要用户输入的时候确认 Label 的存在。如果输入错误的 Label，会导致 TKE 通道的节点数量变为0.
- 如果服务的 selector 和额外节点 Label 出现同一个键的时候，会以 selector 中的配置为准。
- 如果服务的端口（port）发生更改（例如从80改为8080），需要在 API 网关中同步修改；如果端口（port）没有修改，仅仅修改了目标端口（target port），API 网关会自动同步，不需要在 API 网关修改。
