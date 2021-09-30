## 简介
### 组件介绍

DNSAutoscaler 是 DNS 自动水平伸缩组件，可通过一个 deployment 获取集群的节点数和核数，根据预设的伸缩策略，自动水平伸缩 DNS 的副本数。目前的伸缩模式分为两种，分别是 [Linear 线性模式](#Linear) 和 [Ladder 阶梯模式](#Ladder)。

#### Linear Mode[](id:Linear)

ConfigMap 配置示例如下：
```
data:
  linear: |-
    {
      "coresPerReplica": 2,
      "nodesPerReplica": 1,
      "min": 1,
      "max": 100,
      "preventSinglePointFailure": true
    }
```

目标副本计算公式：
replicas = max( ceil( cores _ 1/coresPerReplica ) , ceil( nodes _ 1/nodesPerReplica ) )
replicas = min(replicas, max)
replicas = max(replicas, min)

#### Ladder Mode[](id:Ladder)

ConfigMap 配置示例如下：
```
data:
  ladder: |-
    {
      "coresToReplicas":
      [
        [ 1, 1 ],
        [ 64, 3 ],
        [ 512, 5 ],
        [ 1024, 7 ],
        [ 2048, 10 ],
        [ 4096, 15 ]
      ],
      "nodesToReplicas":
      [
        [ 1, 1 ],
        [ 2, 2 ]
      ]
    }
```

目标副本计算：
假设 100nodes/400cores 的集群中，按上述配置，nodesToReplicas 取2（100>2)，coresToReplicas 取3（64<400<512），二者取较大值3，最终 replica 为3。

### 部署在集群内的 Kubernetes 对象

| kubernets 对象名称 | 类型               | 请求资源                 | 所属 Namespace |
| :----------------- | ------------------ | ------------------------ | -------------- |
| tke-dns-autoscaler | Deployment         | 每节点20mCPU，10Mi内存 | kube-system    |
| dns-autoscaler     | ConfigMap          | -                        | kube-system    |
| tke-dns-autoscale  | ServiceAccount     | -                        | kube-system    |
| tke-dns-autoscaler | ClusterRole        | -                        | kube-system    |
| tke-dns-autoscaler | ClusterRoleBinding | -                        | kube-system    |

## 限制条件

- 仅在 1.8 版本以上的 kubernetes 集群支持。
- 集群中的 dns server 的工作负载为 deployment/coredns。

## 使用方法
1. 登录 [容器服务控制台](https://console.qcloud.com/tke2)，在左侧导航栏中选择**集群**。
2. 在“集群管理”页面单击目标集群 ID，进入集群详情页。
3. 选择左侧菜单栏中的**组件管理**，进入 “组件列表” 页面。
4. 在“组件列表”页面中选择**新建**，并在“新建组件”页面中勾选 DNSAutoscaler。
    该组件默认伸缩配置策略如下：
```
data:
  ladder: |-
    {
      "coresToReplicas":
      [
        [ 1, 1 ],
        [ 128, 3 ],
        [ 512,4 ],
      ],
      "nodesToReplicas":
      [
        [ 1, 1 ],
        [ 2, 2 ]
      ]
    }
```
扩展组件创建成功后，可以通过修改 kube-system 命名空间下的 `configmap/tke-dns-autoscaler` 来变更配置。详细配置请参见 [官方文档](https://github.com/kubernetes-sigs/cluster-proportional-autoscaler)。
5. 单击**完成**即可创建组件。


