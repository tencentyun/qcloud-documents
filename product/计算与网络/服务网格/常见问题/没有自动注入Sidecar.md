通过 `kubectl label namespace xxx istio-injection=enalbed` 为某个 namespace 开启 sidecar 自动注入，发现不生效。

## TCM 自动注入的 label

TCM 1.6 及其以上的版本并不是用 `istio-inejction=enabled` 这个 label 来开启 namespace 的自动注入，而是用类似 `istio.io/rev=1-8-1` 这样的 label，根据不同的版本不一样:

- 1.6 是 `istio.io/rev=1-6-9`
- 1.8 是 `istio.io/rev=1-8-1`

所以如果用社区常见的 `istio-injection=enalbed` 这样的 label，在 TCM 上是不会生效的，以下为不使用社区常见的 label 的原因。

## 网格灰度升级需使用不同 label

为了支持服务网格的灰度升级，就需要新旧两个控制面共存一段时间，让旧的数据面逐渐滚动更新升级并连到新的控制面，如果两个控制面都使用同一个 label 来识别是否需要自动注入，在滚动更新的过程中，两个控制面都去注入 sidecar，就会造成冲突。所以 istio 官方给出了 [灰度升级方案](https://istio.io/latest/docs/setup/upgrade/canary/#data-plane) ，正是基于不同控制面使用不同 label 的方法来实现多控制面共存，这也是 TCM 所采用的方案。

## TCM 如何开启自动注入

在服务网格控制台，选择**服务**>**sidecar自动注入**。如下图所示：

![img](https://main.qcloudimg.com/raw/1fe8bd87b51230d641e6ee57ad5a57c2.png)

然后勾选需要开启自动注入的命名空间即可。

也可以通过使用 kubectl 给 namespace 打 label 来开启:

```bash
kubectl label namespace xxx istio.io/rev=1-8-1
```

>! 注意替换 namespace 以及根据版本替换对应的 label。
