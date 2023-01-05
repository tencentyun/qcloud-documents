

## 简介
### 组件介绍
Cluster Autoscaler（简称 CA）组件基于模拟调度算法为集群提供节点自动扩缩容能力，支持在资源不足时扩容新节点，在资源闲置时缩容旧节点。
>? 
>- 该组件需搭配节点池一起使用，现已支持原生节点、普通节点。
>- 使用该能力需确保节点池已开启“弹性伸缩”。

### 部署在集群内的 Kubernetes 对象
| kubernetes 对象名称    | 类型                  | 资源量          | Namespaces  |
|--------------------|---------------------|--------------|-------------|
| cluster-autoscaler | PodDisruptionBudget | -            | kube-system |
| cluster-autoscaler | ServiceAccount      | -            | kube-system |
| cluster-autoscaler | Secret              | -            | kube-system |
| cluster-autoscaler | ClusterRole         | -            | -           |
| cluster-autoscaler | ClusterRoleBinding  | -            | -           |
| cluster-autoscaler | Role                | -            | kube-system |
| cluster-autoscaler | RoleBinding         | -            | kube-system |
| cluster-autoscaler | Service             | -            | kube-system |
| cluster-autoscaler | Deployment          | 0.5C1G（针对新建） | kube-system |


## 使用场景
- 当集群中出现因资源不足而无法调度的实例（Pod）时，自动触发节点扩容，通过模拟调度选择合适的节点类型，为您减少人力成本。
- 当满足节点空闲缩容条件时，自动触发节点缩容，为您节约资源成本。

## 限制条件
k8s 集群版本 >= 1.16


## 组件原理
### 扩容原理
1. 当集群中资源不足时（集群的计算/存储/网络等资源满足不了 Pod 的 Request /亲和性规则），CA 会监测到因无法调度而 Pending 的 Pod。
2. CA 根据每个节点池的节点模板进行调度判断，挑选合适的节点模板。
3. 若有多个模板合适，即有多个可扩的节点池备选，CA 会调用 expanders 从多个模板挑选最优模板并对对应节点池进行扩容。
![](https://qcloudimg.tencent-cloud.cn/raw/7e890d013db63578f5dacce9a0e605b7.png)

### 缩容原理
1. CA 监测到利用率（取 CPU 利用率和 MEM 利用率的最大值）低于设定阈值的节点。计算利用率时，可以设置 Daemonset 类型不计入 Pod 占用资源。
2. CA 判断集群的状态是否可以触发缩容，需要满足如下要求：
  - 节点空闲时长要求（默认10分钟）。
  - 集群扩容缓冲时间要求（默认10分钟）。
3. CA 判断该节点是否符合缩容条件。您可以按需设置以下不缩容条件（满足条件的节点不会被 CA 缩容）：
  - 含有本地存储的节点。
  - 含有 Kube-system namespace 下非 DaemonSet 管理的 Pod 的节点。
4. CA 驱逐节点上的 Pod 后释放/关机节点。
	- 完全空闲节点可并发缩容（可设置最大并发缩容数）。
	- 非完全空闲节点逐个缩容。
![](https://qcloudimg.tencent-cloud.cn/raw/ad66907e5c1694ffb55e81b3f6b9e556.png)

## 参数说明
<table>
    <tr>
    <th>模块</th>
    <th>功能项</th>
    <th>参数值介绍</th>
        </tr>
        <tr>
    <td>扩容 
            </td>
    <td>扩容算法 
            </td>
    <td><b>随机（默认）</b>：如果可扩容节点池有多个，从中任意选择一个节点池进行扩容。
                <br><b>most-pods</b>：如果可扩容节点池有多个，从中选择运行 Pod 数量最多的节点池进行扩容。
                <br>
                <b>least-waste</b>：如果可扩容节点池有多个，从中选择一个资源浪费最少的节点池进行扩容。
                <br>
    <b>priority</b>：如果可扩容节点池有多个，会按照您自定义的 ConfigMap（详情参考下方），选择优先级高的节点池进行扩容（该特性仅支持原生节点池，对普通节点不生效）。
            </td>
        </tr>
        <tr>
            <td rowspan="5">
                缩容
            </td>
            <td>
                最大并发缩容数
            </td>
            <td>
                发起缩容时，同时支持缩容的节点数量。
                <br>
                说明：只缩容符合完全空闲的空节点；如果存在 Pod, 每次缩容最多一个节点。
            </td>
        </tr>
        <tr>
            <td rowspan="3">
                缩容条件
            </td>
            <td>
                <b>阈值</b>：Pod 占用资源/可分配资源百分比小于 x%时开始判断缩容条件；
            </td>
        </tr>
        <tr>
            <td>
                <b>触发时延</b>：节点连续空闲 x 分钟后被缩容；
            </td>
        </tr>
        <tr>
            <td>
                <b>静默时间</b>：集群扩容 x 分钟开始判断缩容条件；
            </td>
        </tr>
        <tr>
            <td>
                不缩容节点
            </td>
            <td>
含有本地存储 Pod 的节点（本地存储包括 hostPath 和 emptyDir）。
                <br>含有 kube-system namespace 下非 DaemonSet 管理的 Pod 的节点。
            </td>
        </tr>
    </table>

>! 包年包月类型的普通节点不支持缩容。






### 自定义 ConfigMap 使用 priority 扩容算法
>?
>- 该特性仅支持原生节点池，对普通节点池不生效。
>- 优先级取值1~100，必须为正整数。
>- 一个节点池 ID 属于且只属于一个优先级。
>- 如果节点池 ID 没有配置在 ConfigMap 中，即使满足扩容需求，也会由于优先级未配置而不扩容。

示例如下：
```
apiVersion: v1
data:
  priorities: |-
    100:
      - np-l5wmakan     #np-l5wmakan（节点池id）优先级为100。
    50:
      - np-9r9rh7kp     #np-9r9rh7kp（节点池id）优先级为50。
kind: ConfigMap
metadata:
  name: ca-priority-test
  namespace: kube-system
```


## 相关链接
- [创建原生节点](https://cloud.tencent.com/document/product/457/78198)
- [创建普通节点](https://cloud.tencent.com/document/product/457/43735)


