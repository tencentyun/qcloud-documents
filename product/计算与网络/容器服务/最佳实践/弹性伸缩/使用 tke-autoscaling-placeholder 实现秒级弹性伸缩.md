## 操作场景

如 TKE 集群配置了节点池并启用弹性伸缩，则在节点资源不够时可以触发节点的自动扩容（自动购买机器并加入集群），该扩容流程需要一定的时间才能完成，在一些流量突高的场景，该扩容速度可能会显得太慢，影响业务正常运行。而 `tke-autoscaling-placeholder` 可以用于在 TKE 上实现秒级伸缩，应对流量突高场景。本文将介绍如何使用 `tke-autoscaling-placeholder` 实现秒级弹性伸缩。

## 实现原理

`tke-autoscaling-placeholder` 利用低优先级的 Pod 对资源进行提前占位（带 request 的 pause 容器，实际消耗资源量低），为一些可能会出现流量突高的高优先级业务预留部分资源作为缓冲。当需要扩容 Pod 时，高优先级的 Pod 就可以快速抢占低优先级 Pod 的资源进行调度，而低优先级的 `tke-autoscaling-placeholder` 的 Pod 则会被“挤走”，状态变成 Pending，如果配置了节点池并启用弹性伸缩，将会触发节点的扩容。由于通过一些资源作为缓冲，即使节点扩容慢，也能保证一些 Pod 能够快速扩容并调度上，实现秒级伸缩。调整预留的缓冲资源多少，可根据实际需求调整 `tke-autoscaling-placeholder` 的 request 或副本数。

## 使用限制

使用 `tke-autoscaling-placeholder` 应用，集群版本需要在1.18以上。

## 操作步骤

### 安装 tke-autoscaling-placeholder
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在左侧导航栏中，单击**应用市场**进入“应用市场”管理页面。
3. 在应用市场页面搜索框，输入 `tke-autoscaling-placeholder` 进行搜索，找到该应用。如下图所示：
![](https://main.qcloudimg.com/raw/b48a227c35dd1c52633a838c72e95b26.jpg)
4. 在“应用详情页”中，单击“基本信息”模块中的**创建应用**。
5. 在弹出的“创建应用”窗口中，按需配置并创建应用。如下图所示：
![](https://main.qcloudimg.com/raw/72e50043f590875c14a0fe6b05c3b8fd.png)
 配置说明如下：
 - **名称**：输入应用名称。最长63个字符，只能包含小写字母、数字及分隔符“-”，且必须以小写字母开头，数字或小写字母结尾。
 - **地域**：选择需要部署的所在地域。
 - **集群类型**：选择**标准集群**。
 - **集群**：选择需要部署的集群 ID。
 - **Namespace**：选择需要部署的 namespace。
 - **参数**：配置参数中最重要的是 `replicaCount` 与 `resources.request`，分别表示 `tke-autoscaling-placeholder` 的副本数与每个副本占位的资源大小，它们共同决定缓冲资源的大小，可以根据流量突高需要的额外资源量来估算进行设置。
 `tke-autoscaling-placeholder`  完整参数配置说明请参考如下表格：
<table>
<thead>
<tr>
<th>参数名称</th>
<th>描述</th>
<th>默认值</th>
</tr>
</thead>
<tbody><tr>
<td>replicaCount</td>
<td>placeholder 的副本数</td>
<td>10</td>
</tr>
<tr>
<td>image</td>
<td>placeholder 的镜像地址</td>
<td><code>ccr.ccs.tencentyun.com<br>/library/pause:latest</code></td>
</tr>
<tr>
<td>resources.requests.cpu</td>
<td>单个 placeholder 副本占位的 CPU 资源大小</td>
<td>300m</td>
</tr>
<tr>
<td>resources.requests.memory</td>
<td>单个 placeholder 副本占位的内存大小</td>
<td>600Mi</td>
</tr>
<tr>
<td>lowPriorityClass.create</td>
<td>是否创建低优先级的 PriorityClass (用于被 placeholder 引用)</td>
<td>true</td>
</tr>
<tr>
<td>lowPriorityClass.name</td>
<td>低优先级的 PriorityClass 的名称</td>
<td>low-priority</td>
</tr>
<tr>
<td>nodeSelector</td>
<td>指定 placeholder 被调度到带有特定 label 的节点</td>
<td>{}</td>
</tr>
<tr>
<td>tolerations</td>
<td>指定 placeholder 要容忍的污点</td>
<td>[]</td>
</tr>
<tr>
<td>affinity</td>
<td>指定 placeholder 的亲和性配置</td>
<td>{}</td>
</tr>
</tbody></table>
6. 单击**创建**，部署 tke-autoscaling-placeholder 应用。
7. 执行如下命令，查看进行资源占位的 Pod 是否启动成功。示例如下：
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

 



### 部署高优先级 Pod

`tke-autoscaling-placeholder` 默认优先级较低，其中业务 Pod 可以指定一个高优先的 PriorityClass，方便抢占资源实现快速扩容。如果还未创建 PriorityClass，您可以参考如下示例进行创建：

``` yaml
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: high-priority
value: 1000000
globalDefault: false
description: "high priority class"
```

在业务 Pod 中指定 `priorityClassName` 为高优先的 PriorityClass。示例如下：
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

当集群节点资源不够时，扩容出来的高优先级业务 Pod 就可以将低优先级的 `tke-autoscaling-placeholder` 的 Pod 资源抢占过来并调度上，此时 `tke-autoscaling-placeholder`  的 Pod 状态将变成 Pending。示例如下：

```bash
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

如果配置了节点池弹性伸缩，则将触发节点的扩容，虽然节点速度慢，但由于缓冲资源已分配到业务 Pod，业务能够快速得到扩容，因此不会影响业务的正常运行。

## 总结

本文介绍了用于实现秒级伸缩的工具  `tke-autoscaling-placeholder`，巧妙的利用了 Pod 优先级与抢占的特点，提前部署一些用于占位资源的低优先级“空 Pod” 作为缓冲资源填充，在流量突高并且集群资源不够的情况下抢占这些低优先级的“空 Pod” 的资源，同时触发节点扩容，实现在资源紧张的情况下也能做到秒级伸缩，不影响业务正常运行。

## 相关文档

- [Pod 优先级与抢占](https://kubernetes.io/zh/docs/concepts/scheduling-eviction/pod-priority-preemption/)
- [创建节点池](https://cloud.tencent.com/document/product/457/43735)
