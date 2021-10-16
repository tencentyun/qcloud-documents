## 使用场景

在 K8S 1.18之前，HPA 扩缩容无法调整灵敏度：

- 对于缩容，由 `kube-controller-manager` 的 `--horizontal-pod-autoscaler-downscale-stabilization-window` 参数控制缩容时间窗口，默认为5分钟，即负载减小后至少需要5分钟后才开始缩容。
- 对于扩容，由 hpa controller 固定的算法、硬编码的常量因子来控制扩容速度，无法自定义。

K8S 设计逻辑导致用户无法自定义 HPA 的扩缩容灵敏度，不同的业务场景对于扩缩容灵敏度要求并不一样，例如：

- 对于有流量突发的关键业务，需要快速扩容（防止流量瓶颈）、缓慢缩容（防止另一个流量高峰）。
- 对于需要处理大量数据的离线业务，在处理高峰期时应尽快扩容以减少处理时间，高峰期后应尽快缩容以节约成本。
- 对于处理常规数据、网络流量的业务，需要以正常速度扩大和缩小规模，以减少抖动。

>? K8S 1.18的 HPA 更新后，在之前的 v2beta2 版本上新增支持控制扩缩容灵敏度，版本号保持 v2beta2 不变。

本文提供以下几种常见场景的扩缩容示例，介绍如何利用 K8S 1.18的 HPA 新特性来控制扩缩容的灵敏度，以更好的满足各种不同场景对扩容速度的需求。


## 使用示例

K8S 1.18在 HPA Spec 下新增了 `behavior` 字段，该字段提供 `scaleUp` 和 `scaleDown` 两个字段分别控制扩容和缩容行为，详情请参见官方 [K8S API](https://v1-18.docs.kubernetes.io/docs/reference/generated/kubernetes-api/v1.18/#horizontalpodautoscalerbehavior-v2beta2-autoscaling) 文档。



### 示例1：快速扩容

当业务需要快速扩容时，可以使用类似如下的 HPA 配置。示例如下：

```yaml
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
    behavior: # 重要
      scaleUp:
        policies:
        - type: Percent
          value: 900
          periodSeconds: 15
```

示例表示扩容时立即新增当前9倍数量的副本数，即立即扩容到当前10倍的 Pod 数量，最大不超过 `maxReplicas` 的限制。

例如，应用开始只有1个 Pod，如果遭遇流量突发，应用将高速进行扩容，扩容时 Pod 数量变化趋势如下：

```
1 -> 10 -> 100 -> 1000
```

若未配置缩容策略，将等待全局默认的缩容时间窗口（`--horizontal-pod-autoscaler-downscale-stabilization-window`，默认5分钟）后开始缩容。




### 示例2：快速扩容，缓慢缩容

业务在流量高峰期后、并发量骤降的场景中，使用默认的缩容策略，几分钟后 Pod 数量也会随之骤降。如果 Pod 缩容后又迎来流量高峰，此时业务仍可以快速扩容，但扩容过程需要一定时间，且流量高峰可能持续较长时间，在这段时间内可能造成业务后端处理能力达到瓶颈，将导致部分请求失败。可以为 HPA 配置以下 `behavior` 缩容策略，在快速扩容之后缓慢缩容。示例如下：

```yaml
behavior:
    scaleUp:
      policies:
      - type: Percent
        value: 900%
    scaleDown:
      policies:
      - type: Pods
        value: 1
        periodSeconds: 600 # 每10分钟缩掉1个 Pod
```

示例中增加了 `scaleDown` 配置，指定缩容时每10分钟减少1个 Pod，大大降低缩容速度，缩容时的 Pod 数量变化趋势如下：

```
1000 -> … (10 min later) -> 999
```

通过该配置可以让关键业务在流量突发的情况下保持处理能力，避免流量高峰导致部分请求失败。




### 示例3：缓慢扩容


对于无需快速扩容的非关键业务应用，可以为 HPA 加入以下 `behavior` 策略，使业务平稳缓慢扩容。示例如下：

```yaml
behavior:
    scaleUp:
      policies:
      - type: Pods
        value: 1 # 每次扩容只新增1个 Pod
```

例如，业务默认为1个 Pod，扩容时它的 Pod 数量变化趋势如下：
```
1 -> 2 -> 3 -> 4
```

### 示例4：禁止自动缩容

对于扩容后需要禁止自动缩容的关键业务应用，需要人工干预或其它自主开发的 controller 来判断缩容条件，可以使用以下 `behavior` 配置策略来禁止自动缩容。示例如下：

```yaml
behavior:
    scaleDown:
      selectPolicy: Disabled
```

### 示例5：延长缩容时间窗口

缩容默认时间窗口为5分钟（`--horizontal-pod-autoscaler-downscale-stabilization-window`），如果需要延长时间窗口以避免一些流量毛刺造成的异常，可以通过以下 `behavior`  策略指定缩容的时间窗口。示例如下：

```yaml
behavior:
    scaleDown:
      stabilizationWindowSeconds: 600 # 等待600s（10分钟）再开始缩容
      policies:
      - type: Pods
        value: 5 # 每次只缩掉5个 Pod
```

示例表示当负载降下来时，将等待600s（10分钟）再开始缩容，每次只缩容5个 Pod。



### 示例6：延长扩容时间窗口




部分业务应用经常会遇到数据毛刺导致频繁扩容，在短时间内 Pod 并不需要扩容，扩容的 Pod 反而可能造成资源浪费。例如数据处理管道的场景，扩容指标是队列中的事件数量，当队列中堆积了大量事件时，希望在负载持续超过扩容阈值时才快速扩容，如只是短时间内的事件堆积，则即使不扩容队列也可以快速处理事件。

默认的扩容算法会在较短的时间内扩容，针对上述场景，可以通过以下 `behavior` 策略为扩容增加一个时间窗口以避免毛刺导致扩容带来的资源浪费。示例如下：

``` yaml
behavior:
    scaleUp:
      stabilizationWindowSeconds: 300 # 扩容前等待5分钟的时间窗口
      policies:
      - type: pods
        value: 20 # 每次扩容新增20个 Pod
```

示例表示扩容时，需要先等待5分钟的时间窗口，如果在这段时间内负载降下，则不进行扩容。在负载持续超过扩容阈值后才进行扩容，每次扩容新增20个 Pod。




## 参考文档

- [HPA 介绍](https://kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale/)
- [HPA 扩容速度控制提案](https://github.com/kubernetes/enhancements/tree/master/keps/sig-autoscaling/853-configurable-hpa-scale-velocity)
