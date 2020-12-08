## 背景

在 K8S 1.18 之前，HPA 扩容是无法调整灵敏度的:

1. 对于缩容，由 `kube-controller-manager` 的 `--horizontal-pod-autoscaler-downscale-stabilization-window` 参数控制缩容时间窗口，默认 5 分钟，即负载减小后至少需要等 5 分钟才会缩容。
2. 对于扩容，由 hpa controller 固定的算法、硬编码的常量因子来控制扩容速度，无法自定义。

这样的设计逻辑导致用户无法自定义 HPA 的扩缩容灵敏度，而不同的业务场景对于扩容容灵敏度要求可能是不一样的，比如：

1. 对于有流量突发的关键业务，在需要的时候应该快速扩容 (即便可能不需要，以防万一)，但缩容要慢 (防止另一个流量高峰)。
2. 对于一些需要处理大量数据的离线业务，在需要的时候应该尽快扩容以减少处理时间，不需要那么多资源的时候应该尽快缩容以节约成本。
3. 处理常规数据/网络流量的业务，它们可能会以一般的方式扩大和缩小规模，以减少抖动。

HPA 在 K8S 1.18 迎来了一次更新，在之前 v2beta2 版本上新增了扩缩容灵敏度的控制，不过版本号依然保持 v2beta2 不变。

## 如何使用

这次更新实际就是在 HPA Spec 下新增了一个 `behavior` 字段，下面有 `scaleUp` 和 `scaleDown` 两个字段分别控制扩容和缩容的行为，具体可参考官方 API 文档: https://v1-18.docs.kubernetes.io/docs/reference/generated/kubernetes-api/v1.18/#horizontalpodautoscalerbehavior-v2beta2-autoscaling

下面给出一些使用场景的示例。

### 快速扩容

当你的应用需要快速扩容时，可以使用类似如下的 HPA 配置:

``` yaml
apiVersion: autoscaling/v2beta2
kind: HorizontalPodAutoscaler
metadata:
  name: web
spec:
  minReplicas: 1
  maxReplicas: 1000
  metrics:
  - pods:
      metric:
        name: k8s_pod_rate_cpu_core_used_limit
      target:
        averageValue: "80"
        type: AverageValue
    type: Pods
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: web
  behavior: # 这里是重点
    scaleUp:
      policies:
      - type: percent
        value: 900%
```

上面的配置表示扩容时立即新增当前 9 倍数量的副本数，即立即扩容到当前 10 倍的 Pod 数量，当然也不能超过 `maxReplicas` 的限制。

假如一开始只有 1 个 Pod，如果遭遇流量突发，它将以飞快的速度进行扩容，扩容时 Pod 数量变化趋势如下:

```
1 -> 10 -> 100 -> 1000
```

没有配置缩容策略，将等待全局默认的缩容时间窗口 (`--horizontal-pod-autoscaler-downscale-stabilization-window`，默认5分钟) 后开始缩容。

### 快速扩容，缓慢缩容

如果流量高峰过了，并发量骤降，如果用默认的缩容策略，等几分钟后 Pod 数量也会随之骤降，如果 Pod 缩容后突然又来一个流量高峰，虽然可以快速扩容，但扩容的过程毕竟还是需要一定时间的，如果流量高峰足够高，在这段时间内还是可能造成后端处理能力跟不上，导致部分请求失败。这时候我们可以为 HPA 加上缩容策略，HPA `behavior` 配置示例如下:

``` yaml
behavior:
  scaleUp:
    policies:
    - type: percent
      value: 900%
  scaleDown:
    policies:
    - type: pods
      value: 1
      periodSeconds: 600 # 每 10 分钟只缩掉 1 个 Pod
```

上面示例中增加了 `scaleDown` 的配置，指定缩容时每 10 分钟才缩掉 1 个 Pod，大大降低了缩容速度，缩容时的 Pod 数量变化趋势如下:

```
1000 -> … (10 min later) -> 999
```

这个可以让关键业务在可能有流量突发的情况下保持处理能力，避免流量高峰导致部分请求失败。

### 缓慢扩容

如果想要你的应用不太关键，希望扩容时不要太敏感，可以让它扩容平稳缓慢一点，为 HPA 加入下面的 `behavior`:

``` yaml
behavior:
  scaleUp:
    policies:
    - type: pods
      value: 1 # 每次扩容只新增 1 个 Pod
```

假如一开始只有 1 个 Pod，扩容时它的 Pod 数量变化趋势如下:

```
1 -> 2 -> 3 -> 4
```

### 禁止自动缩容

如果应用非常关键，希望扩容后不自动缩容，需要人工干预或其它自己开发的 controller 来判断缩容条件，可以使用类型如下的 `behavior` 配置来禁止自动缩容:

``` yaml
behavior:
  scaleDown:
    policies:
    - type: pods
      value: 0
```

### 延长缩容时间窗口

缩容默认时间窗口是 5 min (`--horizontal-pod-autoscaler-downscale-stabilization-window`)，如果我们需要延长时间窗口以避免一些流量毛刺造成的异常，可以指定下缩容的时间窗口，`behavior` 配置示例如下:

``` yaml
behavior:
  scaleDown:
    stabilizationWindowSeconds: 600 # 等待 10 分钟再开始缩容
    policies:
    - type: pods
      value: 5 # 每次只缩掉 5 个 Pod
```

上面的示例表示当负载降下来时，会等待 600s (10 分钟) 再缩容，每次只缩容 5 个 Pod。

### 延长扩容时间窗口

有些应用经常会有数据毛刺导致频繁扩容，而扩容出来的 Pod 其实没太大必要，反而浪费资源。比如数据处理管道的场景，扩容指标是队列中的事件数量， 当队列中堆积了大量事件时，我们希望可以快速扩容，但又不希望太灵敏，因为可能只是短时间内的事件堆积，即使不扩容也可以很快处理掉。

默认的扩容算法会在较短的时间内扩容，针对这种场景我们可以给扩容增加一个时间窗口以避免毛刺导致扩容带来的资源浪费，`behavior` 配置示例如下:

``` yaml
behavior:
  scaleUp:
    stabilizationWindowSeconds: 300 # 扩容前等待 5 分钟的时间窗口
    policies:
    - type: pods
      value: 20 # 每次扩容新增 20 个 Pod
```

上面的示例表示扩容时，需要先等待 5 分钟的时间窗口，如果在这段时间内负载降下来了就不再扩容，如果负载持续超过扩容阀值才扩容，每次扩容新增 20 个 Pod。

## 小结

本文介绍了如何利用 K8S 1.18 的 HPA 新特性来控制扩缩容的灵敏度，以更好的满足各种不同场景对扩容速度的需求。

## 参考资料

* HPA 介绍: https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/
* 控制 HPA 扩容速度的提案: https://github.com/kubernetes/enhancements/blob/master/keps/sig-autoscaling/20190307-configurable-scale-velocity-for-hpa.md