## 注意事项

该文档仅适用于 [DescribeStatisticData](https://cloud.tencent.com/document/product/248/51845) 接口，下列所有指标必入参 `tke_cluster_instance_id` 维度，选填维度中必须选一项入参，非必选维度可不入参。

## 命名空间

Namespace = QCE/TKE2

## 监控指标

| 指标英文名                     | 指标中文名                           | 指标单位 | 维度                                                         | 统计粒度                                  |
| ------------------------------ | ------------------------------------ | -------- | ------------------------------------------------------------ | ----------------------------------------- |
| K8sPodCpuCoreUsed              | CPU 使用量                            | 核       | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s、 |
| K8sPodMemNoCacheBytes          | 内存使用量（不包含 cache）            | MB       | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodNetworkReceivePackets    | 网络入包量                           | 个/秒    | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodRateCpuCoreUsedLimit     | CPU 利用率（占 limit）                 | %        | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodRateMemNoCacheNode       | 内存利用率（占节点，不包含 cache）    | %        | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodRateMemUsageRequest      | 内存使用量（占 Request）              | %        | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodFsReadBytes              | 块设备读取带宽                       | MB       | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodMemUsageBytes            | 内存使用量                           | MB       | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodNetworkTransmitBytes     | 网络出流量                           | MB       | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodRateCpuCoreUsedNode      | CPU 利用率（占节点）                  | %        | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodRateMemNoCacheRequest    | 内存利用率（占 request，不包含 cache） | %        | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodRestartTotal             | Pod 重启次数                         | 次       | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodFsReadTimes              | 块设备读取次数                       | 次       | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodNetworkReceiveBytes      | 网络入流量                           | MB       | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodNetworkTransmitBytesBw   | 网络出带宽                           | MB/S     | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodRateCpuCoreUsedRequest   | CPU 利用率（占 request）               | %        | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodRateMemUsageLimit        | 内存利用率（占 limit）                | %        | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodStatusReady              | Pod_Ready 状态                        | -        | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodFsWriteBytes             | 块设备写入带宽                       | MB       | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodNetworkReceiveBytesBw    | 网络入带宽                           | MB       | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodNetworkTransmitPackets   | 网络出包量                           | 个/秒    | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodRateMemNoCacheLimit      | 内存利用率(占 limit，不包含 cache)     | %        | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodRateMemUsageNode         | 内存利用率（占节点）                 | %        | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodFsWriteTimes             | 块设备写入次数                       | 次       | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodRateGpuMemoryUsedNode    | GPU 内存利用率（占节点）              | %        | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodRateGpuMemoryUsedRequest | GPU 内存利用率（占 request）           | %        | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodRateGpuUsedNode          | GPU 利用率（占节点）                  | %        | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodRateGpuUsedRequest       | GPU 利用率（占 request）               | %        | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodGpuMemoryRequestBytes    | GPU 内存申请量                        | 卡       | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodGpuMemoryUsedBytes       | GPU 内存使用量                        | MB       | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodGpuRequest               | GPU 申请量                            | 卡       | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodGpuUsed                  | GPU 使用量                            | MB       | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodRateCpuCoreUsedResource  | CPU 使用率                            | %        | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodRateMemUsageResource     | 内存利用率（占 Pod 规格）              | %        | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br/>86400s   |
| K8sPodRateMemNoCacheResource   | 内存利用率（占 Pod 规格，不包含 cache） | %        | 必填维度：tke_cluster_instance_id、<br>选填维度（必选其中任一维度）：workload_name、un_instance_id、node<br>非必选：node_role、workload_kind、namespace、pod_name | 60s、<br/>300s、<br/>3600s、<br> 86400s   |

## 统计粒度与时间跨度
不同统计粒度支持的时间跨度不一致，拉取监控数据时需注意时间跨度限制，具体说明如下：

| 统计粒度 | 支持最大时间跨度（结束时间-起始时间） |
| -------- | ------------------------------------- |
| 60s      | 12小时                                |
| 300s     | 3天                                   |
| 3600s    | 30天                                  |
| 86400s   | 186天                                 |

## 各维度对应参数总览

<table>
    <thead>
        <tr>
            <th><span>参数名称</span></th>
            <th><span>类型</span></th>
            <th><span>维度名称</span></th>
            <th><span>维度解释</span></th>
            <th><span>格式</span></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><span>Conditions.N.Dimensions.N.Name</span></td>
            <td rowspan="2"><span>必填</span></td>
            <td><span>tke_cluster_instance_id</span></td>
            <td><span>集群的维度名称</span></td>
            <td><span>输入 String 类型维度名称：tke_cluster_instance_id</span></td>
        </tr>
        <tr>
            <td><span>Conditions.N.Dimensions.N.Value</span></td>
            <td><span>tke_cluster_instance_id</span></td>
            <td><span>具体集群 ID</span></td>
            <td><span>输入具体集群 ID，例如：cls-fvkxp123</span></td>
        </tr>
        <tr>
            <td><span>Conditions.N.Dimensions.N.Name</span></td>
           <td rowspan="6">必选（必选其中任一维度）<span></span></td>
            <td><span>workload_name</span></td>
            <td><span>工作负载名称的维度名称</span></td>
            <td><span>输入 String 类型维度名称：workload_name</span></td>
        </tr>
        <tr>
            <td><span>Conditions.N.Dimensions.N.Value</span></td>
            <td><span>workload_name</span></td>
            <td><span>具体工作负载名称</span></td>
            <td><span>输入具体工作负载名称，例如：coredns</span></td>
        </tr>
        <tr>
            <td><span>Conditions.N.Dimensions.N.Name</span></td>
            <td><span>node</span></td>
            <td><span>节点名称的维度名称</span></td>
            <td><span>输入 String 类型维度名称：node</span></td>
        </tr>
        <tr>
            <td><span>Conditions.N.Dimensions.N.Value</span></td>
            <td><span>node</span></td>
            <td><span>具体节点名称</span></td>
            <td><span>输入具体节点名称，例如：node</span></td>
        </tr>
        <tr>
            <td><span>Conditions.N.Dimensions.N.Name</span></td>
            <td><span>un_instance_id</span></td>
            <td><span>节点 ID 的维度名称</span></td>
            <td><span>输入 String 类型维度名称：un_instance_id</span></td>
        </tr>
        <tr>
            <td><span>Conditions.N.Dimensions.N.Value</span></td>
            <td><span>un_instance_id</span></td>
            <td><span>具体节点 ID</span></td>
            <td><span>输入具体节点 ID，例如：ins-nwjhh123</span></td>
        </tr>
           <tr>
            <td><span>Conditions.N.Dimensions.N.Name</span></td>
            <td rowspan="8">选填（可不选，也可选择一项或多项）<span></span></td>
            <td><span>workload_kind</span></td>
            <td><span>工作负载类型的维度名称</span></td>
            <td><span>输入 String 类型维度名称：workload_kind</span></td>
        </tr>
        <tr>
            <td><span>Conditions.N.Dimensions.N.Value</span></td>
            <td><span>workload_kind</span></td>
            <td><span>具体工作负载类型</span></td>
            <td><span>输入具体工作负载名称，例如：Deployment</span></td>
        </tr>
          <tr>
            <td><span>Conditions.N.Dimensions.N.Name</span></td>
            <td><span>namespace</span></td>
            <td><span>命名空间的维度名称</span></td>
            <td><span>输入 String 类型维度名称：namespace</span></td>
        </tr>
        <tr>
            <td><span>Conditions.N.Dimensions.N.Value</span></td>
            <td><span>namespace</span></td>
            <td><span>具体命名空间</span></td>
            <td><span>输入具体命名空间，例如：kube-system</span></td>
        </tr>
          <tr>
            <td><span>Conditions.N.Dimensions.N.Name</span></td>
            <td><span>node_role</span></td>
            <td><span>集群的维度名称</span></td>
            <td><span>输入 String 类型维度名称：node_role</span></td>
        </tr>
        <tr>
            <td><span>Conditions.N.Dimensions.N.Value</span></td>
            <td><span>node_role</span></td>
            <td><span>具体节点角色</span></td>
            <td><span>输入具体节点角色，例如：node</span></td>
        </tr>
        <tr>
            <td><span>Conditions.N.Dimensions.N.Name</span></td>
            <td><span>pod_name</span></td>
            <td><span>Pod 名称的维度名称</span></td>
            <td><span>输入 String 类型维度名称：pod_name</span></td>
        </tr>
        <tr>
            <td><span>Conditions.N.Dimensions.N.Value</span></td>
            <td><span>pod_name</span></td>
            <td><span>具体 Pod 名称</span></td>
            <td><span>输入具体 Pod 名称，例如：coredns-6ffc45f789-46lpq</span></td>
        </tr>
    </tbody>
</table>



## 入参说明

**根据命名空间入参取值如下：**
&Namespace=QCE/TKE2
&Conditions.N.Dimensions.0.Name=tke_cluster_instance_id
&Conditions.N.Dimensions.0.Value=cls-fvkxp123
&Conditions.N.Dimensions.1.Name=namespace
&Conditions.N.Dimensions.1.Value=kube-system

**根据工作负载入参取值如下：**
&Namespace=QCE/TKE2
&Conditions.N.Dimensions.0.Name=tke_cluster_instance_id
&Conditions.N.Dimensions.0.Value=cls-fvkxp123
&Conditions.N.Dimensions.1.Name=workload_kind
&Conditions.N.Dimensions.1.Value=Deployment

**根据工作负载名称入参取值如下：**
&Namespace=QCE/TKE
&Conditions.N.Dimensions.0.Name=tke_cluster_instance_id
&Conditions.N.Dimensions.0.Value=cls-fvkxp123
&Conditions.N.Dimensions.1.Name=workload_name
&Conditions.N.Dimensions.1.Value=coredns

**根据节点角色入参取值如下：**
&Namespace=QCE/TKE2
&Conditions.N.Dimensions.0.Name=tke_cluster_instance_id
&Conditions.N.Dimensions.0.Value=cls-fvkxp123
&Conditions.N.Dimensions.1.Name=node_role
&Conditions.N.Dimensions.1.Value=node

**根据节点 ID 入参取值如下：**
&Namespace=QCE/TKE2
&Conditions.N.Dimensions.0.Name=tke_cluster_instance_id
&Conditions.N.Dimensions.0.Value=cls-fvkxp123
&Conditions.N.Dimensions.1.Name=un_instance_id
&Conditions.N.Dimensions.1.Value=ins-nwjhh123

**根据节点名称入参取值如下：**
&Namespace=QCE/TKE2
&Conditions.N.Dimensions.0.Name=tke_cluster_instance_id
&Conditions.N.Dimensions.0.Value=cls-fvkxp123
&Conditions.N.Dimensions.1.Name=node
&Conditions.N.Dimensions.1.Value=node

**根据 Pod 名称入参取值如下：**
&Namespace=QCE/TKE2
&Conditions.N.Dimensions.0.Name=tke_cluster_instance_id
&Conditions.N.Dimensions.0.Value=cls-fvkxp123
&Conditions.N.Dimensions.1.Name=pod_name
&Conditions.N.Dimensions.1.Value=coredns-6ffc45f789-46lpq
