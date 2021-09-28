## 简介
### 组件介绍

DeScheduler 是容器服务 TKE 基于 Kubernetes 原生社区 [DeScheduler](https://github.com/kubernetes-sigs/descheduler)  实现的一个基于 Node 真实负载进行重调度的插件。在 TKE 集群中安装该插件后，该插件会和 Kube-scheduler 协同生效，实时监控集群中高负载节点并驱逐低优先级 Pod。建议您搭配 TKE [Dynamic Scheduler（动态调度器扩展组件）](https://cloud.tencent.com/document/product/457/50843)一起使用，多维度保障集群负载均衡。 
该插件依赖 Prometheus 监控组件以及相关规则配置，建议您安装插件之前仔细阅读 [依赖部署](#DeScheduler)，以免插件无法正常工作。



### 部署在集群内的 Kubernetes 对象

| Kubernetes 对象名称  | 类型               |                   请求资源                   | 所属 Namespace |
| :----------------- | :----------------- | :------------------------------------------ | ------------- |
| descheduler        | Deployment         | 每个实例 CPU:200m，Memory:200Mi，共1个实例 | kube-system   |
| descheduler        | ClusterRole        |                      -                       | kube-system   |
| descheduler        | ClusterRoleBinding |                      -                       | kube-system   |
| descheduler        | ServiceAccount     |                      -                       | kube-system   |
| descheduler-policy | ConfigMap          |                      -                       | kube-system   |
| probe-prometheus   | ConfigMap          |                      -                       | kube-system   |


## 使用场景

DeScheduler 通过重调度来解决集群现有节点上不合理的运行方式。社区版本 DeScheduler 中提出的策略基于 APIServer 中的数据实现，并未基于节点真实负载。因此可以增加对于节点的监控，基于真实负载进行重调度调整。

容器服务 TKE 自研的 ReduceHighLoadNode 策略依赖 Prometheus 和 node_exporter 监控数据，根据节点 CPU 利用率、内存利用率、网络 IO、system loadavg 等指标进行 Pod 驱逐重调度，防止出现节点极端负载的情况。DeScheduler 的 ReduceHighLoadNode 与 TKE 自研的 Dynamic Scheduler 基于节点真实负载进行调度的策略需配合使用。



## 限制条件

- Kubernetes 版本 ≥ v1.10.x
- 在特定场景下，某些 Pod 会被重复调度到需要重调度的节点上，从而引发 Pod 被重复驱逐。此时可以根据实际场景改变 Pod 可调度的节点，或者将 Pod 标记为不可驱逐。 
- 该组件已对接容器服务 TKE 的监控告警体系。
- 建议您为集群开启事件持久化，以便更好的监控组件异常以及故障定位。Descheduler 驱逐 Pod 时会产生对应事件，可根据 reason 为 “Descheduled” 类型的事件观察 Pod 是否被重复驱逐。
- 为避免 DeScheduler 驱逐关键的 Pod，设计的算法默认不驱逐 Pod。对于可以驱逐的 Pod，用户需要显示给判断 Pod 所属 workload。例如，statefulset、deployment 等对象设置可驱逐 annotation。
- 驱逐大量 Pod，导致服务不可用。
   Kubernetes 原生提供 PDB 对象用于防止驱逐接口造成的 workload 不可用 Pod 过多，但需要用户创建该 PDB 配置。容器服务 TKE 自研的 DeScheduler 组件加入了兜底措施，即调用驱逐接口前，判断 workload 准备的 Pod 数是否大于副本数一半，否则不调用驱逐接口。





## 组件原理

DeScheduler  基于 [社区版本 Descheduler](https://github.com/kubernetes-sigs/descheduler) 的重调度思想，定期扫描各个节点上的运行 Pod，发现不符合策略条件的进行驱逐以进行重调度。社区版本 DeScheduler  已提供部分策略，策略基于 APIServer 中的数据，例如 `LowNodeUtilization` 策略依赖的是 Pod 的 request 和 limit 数据，这类数据能够有效均衡集群资源分配、防止出现资源碎片。但社区策略缺少节点真实资源占用的支持，例如节点 A 和 B 分配出去的资源一致，由于 Pod 实际运行情况，CPU 消耗型和内存消耗型不同，峰谷期不同造成两个节点的负载差别巨大。

因此，腾讯云 TKE 推出 DeScheduler，底层依赖对节点真实负载的监控进行重调度。通过 Prometheus 拿到集群 Node 的负载统计信息，根据用户设置的负载阈值，定期执行策略里面的检查规则，驱逐高负载节点上的 Pod。
![](https://main.qcloudimg.com/raw/9e37814fd4f4831217b33b35ce72f03b.png)


## 组件参数说明[](id:parameter)

### Prometheus 数据查询地址


>!为确保组件可以拉取到所需的监控数据、调度策略生效，请按照 **[依赖部署](#DeScheduler)**>**Prometheus 文件配置**步骤配置监控数据采集规则。

- 如果使用自建 Prometheus，直接填入数据查询 URL（HTTPS/HTTPS）即可。
- 如果使用托管 Prometheus，选择托管实例 ID 即可，系统会自动解析实例对应的数据查询 URL。

### 利用率阈值和目标利用率

>! 负载阈值参数已设置默认值，如您无额外需求，可直接采用。

过去5分钟内，节点的 CPU 平均利用率或者内存平均使用率超过设定阈值，Descheduler 会判断节点为高负载节点，执行 Pod 驱逐逻辑，并尽量通过 Pod 重调度使节点负载降到目标利用率以下。



## 操作步骤
### 依赖部署[](id:DeScheduler)

DeScheduler 组件依赖于 Node 当前和过去一段时间的真实负载情况来进行调度决策，需要通过 Prometheus 等监控组件获取系统 Node 真实负载信息。在使用 DeScheduler 组件之前，您可以采用自建 Prometheus 监控或采用 TKE 云原生监控。
[](id:rules)
<dx-tabs>
::: 自建\sPrometheus\s监控服务
#### 部署 node-exporter 和 Prometheus

通过 node-exporter 实现对于 Node 指标的监控，您可按需部署 node-exporter 和 Prometheus。

#### 聚合规则配置[](id:rules)

在 node-exporter 获取节点监控数据后，需要通过 Prometheus 对原始的 node-exporter 中采集数据进行聚合计算。为获取 DeScheduler 所需要的 `cpu_usage_avg_5m`、`mem_usage_avg_5m` 等指标，需要在 Prometheus 的 rules 规则中进行配置。示例如下：
<dx-codeblock>
:::  yaml
```
groups:
   - name: cpu_mem_usage_active
     interval: 30s
     rules:
     - record: mem_usage_active
       expr: 100*(1-node_memory_MemAvailable_bytes/node_memory_MemTotal_bytes)
   - name: cpu-usage-1m
     interval: 1m
     rules:
     - record: cpu_usage_avg_5m
       expr: 100 - (avg by (instance) (irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
   - name: mem-usage-1m
     interval: 1m
     rules:
     - record: mem_usage_avg_5m
       expr: avg_over_time(mem_usage_active[5m])
```
:::
</dx-codeblock>
>!当您使用 TKE 提供的 DynamicScheduler 时，需在 Prometheus 配置获取 Node 监控数据的聚合规则。DynamicScheduler 聚合规则与 DeScheduler 聚合规则有部分重合，但并不完全一样，请您在配置规则时不要互相覆盖。同时使用 DynamicScheduler 和 DeScheduler 时应该配置如下规则：
<dx-codeblock>
:::  yaml
```
groups:
   - name: cpu_mem_usage_active
     interval: 30s
     rules:
     - record: mem_usage_active
       expr: 100*(1-node_memory_MemAvailable_bytes/node_memory_MemTotal_bytes)
   - name: mem-usage-1m
     interval: 1m
     rules:
     - record: mem_usage_avg_5m
       expr: avg_over_time(mem_usage_active[5m])
   - name: mem-usage-5m
     interval: 5m
     rules:
     - record: mem_usage_max_avg_1h
       expr: max_over_time(mem_usage_avg_5m[1h])
     - record: mem_usage_max_avg_1d
       expr: max_over_time(mem_usage_avg_5m[1d])
   - name: cpu-usage-1m
     interval: 1m
     rules:
     - record: cpu_usage_avg_5m
       expr: 100 - (avg by (instance) (irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
   - name: cpu-usage-5m
     interval: 5m
     rules:
     - record: cpu_usage_max_avg_1h
       expr: max_over_time(cpu_usage_avg_5m[1h])
     - record: cpu_usage_max_avg_1d
       expr: max_over_time(cpu_usage_avg_5m[1d])
```
:::
</dx-codeblock>
#### Prometheus 文件配置
1. 上述定义了 DeScheduler 所需要的指标计算的 rules，需要将 rules 配置到 Prometheus 中，参考一般的 Prometheus 配置文件。示例如下：
```
global:
   evaluation_interval: 30s
   scrape_interval: 30s
   external_labels:
rule_files:
- /etc/prometheus/rules/*.yml # /etc/prometheus/rules/*.yml 是定义的 rules 文件
```
2. 将 rules 配置复制到一个文件（例如 de-scheduler.yaml），文件放到上述 Prometheus 容器的 `/etc/prometheus/rules/` 下。
3. 重新加载 Prometheus server，即可从 Prometheus 中获取到动态调度器需要的指标。
>?通常情况下，上述 Prometheus 配置文件和 rules 配置文件都是通过 configmap 存储，再挂载到 Prometheus server 容器，因此修改相应的 configmap 即可。
:::
::: 云原生监控\sPrometheus
1. 登录容器服务控制台，在左侧菜单栏中选择 **[云原生监控](https://console.cloud.tencent.com/tke2/prometheus)**，进入“云原生监控”页面。
2. 创建与 Cluster 处于同一 VPC 下的 [云原生监控 Prometheus 实例](https://cloud.tencent.com/document/product/457/49889#.E5.88.9B.E5.BB.BA.E7.9B.91.E6.8E.A7.E5.AE.9E.E4.BE.8B)，并 [关联用户集群](https://cloud.tencent.com/document/product/457/49890)。如下图所示：
   ![](https://main.qcloudimg.com/raw/bafb027663fbb3f2a5063531743c2e97.jpg)
3. 与原生托管集群关联后，可以在用户集群查看到每个节点都已安装 node-exporter。如下图所示：
   ![](https://main.qcloudimg.com/raw/e35d4af7eeba15f6d9da62ce79176904.png)
4. 设置 Prometheus 聚合规则，具体规则内容与上述 [自建Prometheus监控服务](#rules) 中的“聚合规则配置”相同。规则保存后立即生效，无需重新加载 server。
:::
</dx-tabs>





### 安装组件

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2/cluster)，选择左侧导航栏中的**集群**。
2. 在“集群管理”页面单击目标集群 ID，进入集群详情页。
3. 选择左侧菜单栏中的**组件管理**，进入 “组件列表” 页面。
4. 在“组件列表”页面中选择**新建**，并在“新建组件”页面中勾选 Decheduler（重调度器）。
5. 单击**参数配置**，按照 [参数说明](#parameter) 填写组件所需参数。
6. 单击**完成**即可创建组件。安装成功后，DeScheduler 即可正常运行，无需进行额外配置。
7. 若您需要驱逐 workload（例如 statefulset、deployment 等对象），可以设置 Annotation 如下：
```plaintext
descheduler.alpha.kubernetes.io/evictable: 'true'
```

