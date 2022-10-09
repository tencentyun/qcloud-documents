
## 基础监控常见问题

### 节点 cpu/memory 分配量为什么会超出节点资源规格？

**原因：**node 层级的 cpu/memory 分配量指标依赖节点上各个 pod 的 cpu/memory request 来计算，在计算时没有把 failed 的 pod 排除。

示例：节点规格是 4c8g，节点上目前运行 3 个 pod（资源 request 用量如下）：

- pod1 正常运行其 request 为 2c4g；
- pod2 正常运行其 request 为 1c2g；
- pod3 状态为 failed 其 request 为 0.5c1g；

此时节点剩余可调度资源为 4-2-1=1c、8-4-2=2g，pod4 request 为 0.8c1.5g，满足调度器筛选，正常被调度到该节点上。此时节点上共 4 个 pod，3 个正常 1 个异常，此时 node 层级的分配量为 4.3c8.5g（因计算时没有把 failed 的 pod 排除，因此超过了节点规格）。

该问题已在 5 月新版本中修复，即计算 node 资源分配量已把异常 pod 排除。

### 为什么 pod 状态显示正常，但监控指标 k8s_workload_abnormal 展示异常？

**原因：**该指标根据 workload 下 pod 是否异常来判断，pod 是否异常取决于 `pod.status.condition` 下这四个 Type 来确定。当这四个指标同时为`True`时`k8s_workload_abnormal`才会认为是正常，否则认为是异常。
- PodScheduled：Pod 已经被调度到某节点。
- ContainersReady：Pod 中所有容器都已就绪。
- Initialized：所有的 Init 容器 都已成功完成。
- Ready：Pod 可以为请求提供服务，并且应该被添加到对应服务的负载均衡池中。

### daemonSet tke-monitor-agent 报错原因总结

<table>
<thead>
  <tr>
    <th>现象</th>
    <th>原因</th>
    <th>解决措施</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>无法解析域名 `receiver.barad.tencentyun.com`，指标上报失败，导致用户集群没有监控数据</td>
    <td>节点 dns 被修改</td>
    <td>给 DaemonSet tke-monitor-agent 加上 hostAlias。参考代码如下：
```
hostAliases:
- hostnames:
  - receiver.barad.tencentyun.com
  ip: 169.254.0.4
```
</td>
  </tr>
</tbody>
</table>

