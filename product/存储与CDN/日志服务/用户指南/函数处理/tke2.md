## 背景

当 TKE 集群配置了节点池并启用了弹性伸缩，在节点资源不够时可以触发节点的自动扩容 (自动买机器并加入集群)，但这个扩容流程需要一定的时间才能完成，在一些流量突高的场景，这个扩容速度可能会显得太慢，影响业务。 `tke-autoscaling-placeholder` 可以用于在 TKE 上实现秒级伸缩，应对这种流量突高的场景。

## 原理

`tke-autoscaling-placeholder` 实际就是利用低优先级的 Pod 对资源进行提前占位(带 request 的 pause 容器，实际不怎么消耗资源)，为一些可能会出现流量突高的高优先级业务预留部分资源作为缓冲，当需要扩容 Pod 时，高优先级的 Pod 就可以快速抢占低优先级 Pod 的资源进行调度，而低优先级的 `tke-autoscaling-placeholder` 的 Pod 则会被 "挤走"，状态变成 Pending，如果配置了节点池并启用弹性伸缩，就会触发节点的扩容。这样，由于有了一些资源作为缓冲，即使节点扩容慢，也能保证一些 Pod 能够快速扩容并调度上，实现秒级伸缩。要调整预留的缓冲资源多少，可根据实际需求调整 `tke-autoscaling-placeholder` 的 request 或副本数。

## 使用限制

使用该应用要求集群版本在 1.18 以上。

## 操作步骤

### 安装 tke-autoscaling-placeholder

在应用市场找到 `tke-autoscaling-placeholder`，点击进入应用详情，再点 `创建应用`:

![](https://main.qcloudimg.com/raw/bb081fd1923819c4a85c4b2cff80ff11.png)

选择要部署的集群 id 与 namespace，应用的配置参数中最重要的是 `replicaCount` 与 `resources.request`，分别表示 `tke-autoscaling-placeholder` 的副本数与每个副本占位的资源大小，它们共同决定缓冲资源的大小，可以根据流量突高需要的额外资源量来估算进行设置。

最后点击创建，你可以查看这些进行资源占位的 Pod 是否启动成功:

``` bash
$ kubectl get pod -n default
tke-autoscaling-placeholder-b58fd9d5d-2p6ww   1/1     Running   0          8s
tke-autoscaling-placeholder-b58fd9d5d-55jw7   1/1     Running   0          8s
tke-autoscaling-placeholder-b58fd9d5d-6rq9r   1/1     Running   0          8s
tke-autoscaling-placeholder-b58fd9d5d-7c95t   1/1     Running   0          8s
tke-autoscaling-placeholder-b58fd9d5d-bfg8r   1/1     Running   0          8s
tke-autoscaling-placeholder-b58fd9d5d-cfqt6   1/1     Running   0          8s
tke-autoscaling-placeholder-b58fd9d5d-gmfmr   1/1     Running   0          8s
tke-autoscaling-placeholder-b58fd9d5d-grwlh   1/1     Running   0          8s
tke-autoscaling-placeholder-b58fd9d5d-ph7vl   1/1     Running   0          8s
tke-autoscaling-placeholder-b58fd9d5d-xmrmv   1/1     Running   0          8s
```

 `tke-autoscaling-placeholder`  的完整配置参考下面的表格:

| 参数                        | 描述                                                       | 默认值                                        |
| --------------------------- | ---------------------------------------------------------- | --------------------------------------------- |
| `replicaCount`              | placeholder 的副本数                                       | `10`                                          |
| `image`                     | placeholder 的镜像地址                                     | `ccr.ccs.tencentyun.com/library/pause:latest` |
| `resources.requests.cpu`    | 单个 placeholder 副本占位的 cpu 资源大小                   | `300m`                                        |
| `resources.requests.memory` | 单个 placeholder 副本占位的内存大小                        | `600Mi`                                       |
| `lowPriorityClass.create`   | 是否创建低优先级的 PriorityClass (用于被 placeholder 引用) | `true`                                        |
| `lowPriorityClass.name`     | 低优先级的 PriorityClass 的名称                            | `low-priority`                                |
| `nodeSelector`              | 指定 placeholder 被调度到带有特定 label 的节点             | `{}`                                          |
| `tolerations`               | 指定 placeholder 要容忍的污点                              | `[]`                                          |
| `affinity`                  | 指定 placeholder 的亲和性配置                              | `{}`                                          |

### 部署高优先级 Pod

 `tke-autoscaling-placeholder` 的优先级很低，我们的业务 Pod 可以指定一个高优先的 PriorityClass，方便抢占资源实现快速扩容，如果没有可以先创建一个:

``` yaml
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: high-priority
value: 1000000
globalDefault: false
description: "high priority class"
```

在我们的业务 Pod 中指定 `priorityClassName` 为高优先的 PriorityClass:

``` yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  replicas: 8
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      priorityClassName: high-priority # 这里指定高优先的 PriorityClass
      containers:
      - name: nginx
        image: nginx
        resources:
          requests:
            cpu: 400m
            memory: 800Mi
```

当集群节点资源不够，扩容出来的高优先级业务 Pod 就可以将低优先级的 `tke-autoscaling-placeholder` 的 Pod 资源抢占过来并调度上，然后 `tke-autoscaling-placeholder`  的 Pod 再 Pending:

``` yaml
$ kubectl get pod -n default
NAME                                          READY   STATUS    RESTARTS   AGE
nginx-bf79bbc8b-5kxcw                         1/1     Running   0          23s
nginx-bf79bbc8b-5xhbx                         1/1     Running   0          23s
nginx-bf79bbc8b-bmzff                         1/1     Running   0          23s
nginx-bf79bbc8b-l2vht                         1/1     Running   0          23s
nginx-bf79bbc8b-q84jq                         1/1     Running   0          23s
nginx-bf79bbc8b-tq2sx                         1/1     Running   0          23s
nginx-bf79bbc8b-tqgxg                         1/1     Running   0          23s
nginx-bf79bbc8b-wz5w5                         1/1     Running   0          23s
tke-autoscaling-placeholder-b58fd9d5d-255r8   0/1     Pending   0          23s
tke-autoscaling-placeholder-b58fd9d5d-4vt8r   0/1     Pending   0          23s
tke-autoscaling-placeholder-b58fd9d5d-55jw7   1/1     Running   0          94m
tke-autoscaling-placeholder-b58fd9d5d-7c95t   1/1     Running   0          94m
tke-autoscaling-placeholder-b58fd9d5d-ph7vl   1/1     Running   0          94m
tke-autoscaling-placeholder-b58fd9d5d-qjrsx   0/1     Pending   0          23s
tke-autoscaling-placeholder-b58fd9d5d-t5qdm   0/1     Pending   0          23s
tke-autoscaling-placeholder-b58fd9d5d-tgvmw   0/1     Pending   0          23s
tke-autoscaling-placeholder-b58fd9d5d-xmrmv   1/1     Running   0          94m
tke-autoscaling-placeholder-b58fd9d5d-zxtwp   0/1     Pending   0          23s
```

如果配置了节点池弹性伸缩，就会触发节点的扩容，虽然节点速度速度慢，但由于我们的缓冲资源都给了业务 Pod，业务能够快速得到扩容，也就不会影响业务。

## 小结

本文介绍了 `tke-autoscaling-placeholder` 这个用于实现秒级伸缩的工具，巧妙的利用了 Pod 优先级与抢占的特点，提前部署一些用于占位资源的低优先级 "空 Pod" 作为缓冲资源填充，在流量突高并且集群资源不够的情况下抢占这些低优先级的 "空 Pod" 的资源，同时触发节点扩容，实现在资源紧张的情况下也能做到秒级伸缩，不影响业务。

## 参考资料

* [Pod 优先级与抢占](https://kubernetes.io/zh/docs/concepts/configuration/pod-priority-preemption/)
* [创建节点池](https://cloud.tencent.com/document/product/457/43735)
