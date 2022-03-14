一些服务在往 istio 上迁移过渡的过程中，有时可能会遇到 Pod 启动失败，然后一直重启，排查原因是业务启动时需要调用其它服务（例如从配置中心拉取配置），如果失败就退出，没有重试逻辑。调用失败的原因是 envoy 未就绪（envoy 需要从控制面拉取配置，需要一点时间），导致业务发出的流量无法被处理（参考 k8s issue [#65502](https://github.com/kubernetes/kubernetes/issues/65502) ）。

### 最佳实践

目前这类问题的最佳实践是让应用更加健壮一点，增加重试逻辑，调用失败后不要立刻退出。或者在启动命令前加下 sleep，等待几秒。

如果不想改动应用，您可以参考以下规避方案。

### 规避方案

规避方案为调整 sidecar 注入顺序。
在 istio 1.7，社区通过给 istio-injector 注入逻辑增加一个叫 `HoldApplicationUntilProxyStarts` 的开关来解决了该问题，开关打开后，proxy 将会注入到第一个 container。

示例：
![img](https://main.qcloudimg.com/raw/2b0b4ab385411f76a1be816c0c292dd9.png)

![img](https://main.qcloudimg.com/raw/6a614019db2e05a4a1e7990afa7db023.png)

查看 istio-injector 自动注入使用的 template，可以知道如果打开了 `HoldApplicationUntilProxyStarts` 就会为 sidecar 添加一个 postStart hook：

![img](https://main.qcloudimg.com/raw/4a2e01dde93aa13a37be2a5c5254c39b.png)

它的目的是为了阻塞后面的业务容器启动，sidecar 完全启动后才开始启动后面的业务容器。

开关配置分为全局和局部两种，下面介绍两种启用方法。

<dx-tabs>
::: 全局配置
修改 istio 的 configmap 全局配置：

```bash
kubectl -n istio-system edit cm istio
```

在 `defaultConfig` 下加入 `holdApplicationUntilProxyStarts: true`

```yaml
apiVersion: v1
data:
  mesh: |-
    defaultConfig:
      holdApplicationUntilProxyStarts: true
  meshNetworks: 'networks: {}'
kind: ConfigMap
```

若使用 IstioOperator，defaultConfig 修改 CR 字段 `meshConfig`：

```yaml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
metadata:
  namespace: istio-system
  name: example-istiocontrolplane
spec:
  meshConfig:
    defaultConfig:
      holdApplicationUntilProxyStarts: true
```
:::
::: 局部配置
如果使用 istio 1.8 及其以上的版本，可以为需要打开此开关的 Pod 加上 `proxy.istio.io/config` 注解，将 `holdApplicationUntilProxyStarts` 置为 `true`，示例：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      annotations:
        proxy.istio.io/config: |
          holdApplicationUntilProxyStarts: true
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: "nginx"
```


:::
</dx-tabs>



需要注意的是，打开开关后，意味着业务容器需要等 sidecar 完全 ready 后才能启动，会让 Pod 启动速度变慢一些。在需要快速扩容应对突发流量场景可能会显得吃力，所以建议是自行评估业务场景，利用局部配置的方法，只给需要的业务打开此开关。
