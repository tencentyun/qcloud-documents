
## 简介
### 组件介绍

Dynamic Scheduler 是容器服务 TKE 基于 Kubernetes 原生 Kube-scheduler Extender 机制实现的基于 Node 真实负载进行预选和优选的动态调度器插件。
在 TKE 集群中安装该插件后，该插件将与 Kube-scheduler 协同生效，有效避免原生调度器基于 request 和 limit 的调度机制带来的节点负载不均的问题。
该组件依赖 Prometheus 监控组件以及相关规则配置，您可参考 [依赖部署](#Dynamic) 进行操作，避免遇到插件无法正常工作的问题。

## 应用场景

- 集群负载不均
Kubernetes 原生的调度器多是基于 Pod Request 的资源来进行调度的，没有根据 Node 当前和过去一段时间的真实负载情况进行相关调度的决策。
这样可能会导致一个问题：集群内有些节点的剩余可调度资源比较多（根据节点上运行的 Pod 的request和limit计算出的值）但是真实负载却比较高，而另一些节点的剩余可调度资源比较少但是真实负载却比较低, 但是这时候Kube-scheduler会优先将Pod调度到剩余资源比较多的节点上（根据LeastRequestedPriority策略）。
如下图，Kube-Scheduler会把pod调度到Node2上，但很显然调度到Node1（真实负载水位更低）是一个更优的选择。
![](https://main.qcloudimg.com/raw/2b186b7558659915e33ce2ce20608640.png)

- 防止调度热点

为了防止低负载的节点被持续调度很多pod，Dynamic Scheduler 还设置了防调度热点策略（统计节点过去几分钟调度了几个pod，并相应减小节点在优选阶段的评分）。
当前采取策略如下：

2. 如果节点在过去一分钟调度了超过2个pod，则优选评分减去1分

3. 如果节点在过去五分钟调度了超过5个pod，则优选评分减去1分

## 限制条件

1. TKE 建议在 >= v1.10.x
2. 如果要升级kubernetes master版本，对于托管集群无需再次设置本插件，对于独立集群，因为master版本升级会重置master上所有组件的配置，从而影响到本插件作为Scheduler Extender的配置，所以本插件需要卸载后再重新安装。

## 依赖部署[](id:Dynamic)

动态调度器依赖于Node当前和过去一段时间的真实负载情况来进行调度决策，这依赖于Prometheus等监控组件获取系统Node真实负载信息。在使用动态调度器之前，需要部署Prometheus等监控组件。在TKE，用户可以采用自建的Prometheus监控服务，也可以采用TKE推出的云原生监控，下面对这两种方式依次介绍。

### 用户自建Prometheus等监控服务

#### 部署node-exporter 和 prometheus

我们通过node-exporter实现对于Node指标的监控，用户可以根据自己的需要部署node-exporter和prometheus。

#### 聚合规则配置

在 node-exporter获取节点监控数据后，需要通过Prometheus对原始的node-exporter中采集数据进行聚合计算。为了获取动态调度器中需要的`cpu_usage_avg_5m`, `cpu_usage_max_avg_1h`, `cpu_usage_max_avg_1d`，`mem_usage_avg_5m`, `mem_usage_max _avg_1h`, `mem_usage_max_avg_1d`等指标，需要在Prometheus的 rules 规则配置如下：

```yaml
groups:
    - name: cpu_mem_usage_active
      interval: 30s
      rules:
      - record: mem_usage_active
        expr: 100*(1-node_memory_MemAvailable_bytes/node_memory_MemTotal_bytes)
    - name: cpu-usage-5m
      interval: 5m
      rules:
      - record: cpu_usage_max_avg_1h
        expr: max_over_time(cpu_usage_avg_5m[1h])
      - record: cpu_usage_max_avg_1d
        expr: max_over_time(cpu_usage_avg_5m[1d])
    - name: cpu-usage-1m
      interval: 1m
      rules:
      - record: cpu_usage_avg_5m
        expr: 100 - (avg by (instance) (irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
    - name: mem-usage-5m
      interval: 5m
      rules:
      - record: mem_usage_max_avg_1h
        expr: max_over_time(mem_usage_avg_5m[1h])
      - record: mem_usage_max_avg_1d
        expr: max_over_time(mem_usage_avg_5m[1d])
    - name: mem-usage-1m
      interval: 1m
      rules:
      - record: mem_usage_avg_5m
        expr: avg_over_time(mem_usage_active[5m])
```

#### pometheus 文件配置

前面定义了动态调度器所需要的指标计算的rule，然后我们需要把这个rule配置到prometheus中，参考一般的prometheus配置文件

```
global:
  evaluation_interval: 30s
  scrape_interval: 30s
  external_labels:
rule_files:
- /etc/prometheus/rules/*.yml # /etc/prometheus/rules/*.yml就是定义的rules文件
```

我们把上面的rules配置，复制到一个文件如dynamic-scheduler.yaml，文件放到上述prometheus 容器的/etc/prometheus/rules/下，然后reload prometheus server就可以从prometheus中获取到动态调度器需要的指标。

通常情况下，上述prometheus配置文件和rules配置文件都是通过configmap存储，然后挂载到prometheus server的容器里面，所以修改相应的configmap即可。

### 云原生监控 Prometheus

1. 创建与Cluster处于同一VPC下的云原生监控Prometheus实例，并与用户集群关联。
   ![](https://main.qcloudimg.com/raw/b17e7ea4642e6aaea70c885956f30b0b.png)
2. 与原生托管集群关联后，可以在用户集群看到每个节点都已经安装了node-exporter。
   ![](https://main.qcloudimg.com/raw/e35d4af7eeba15f6d9da62ce79176904.png)
3. 接下来设置Prometheus的聚合规则，如下图所示，具体规则内容与上一小节介绍的规则相同，此处不再赘述。
   ![](https://main.qcloudimg.com/raw/20faac41cda527332183d492cc01ac09.png)


## 组件原理

动态调度器原理：基于scheduler extender扩展机制，从prometheus监控数据中获取节点负载数据，开发基于节点实际负载的调度策略，在调度预选和优选阶段进行干预，优先将pod调度到低负载节点上。
该组件由node-annotator，dynamic-scheduler构成。

### node-annotator

node-annotator组件负责定期从监控中拉取节点负载metric，同步到节点的annotation。
>!请注意：组件删除后，node-annotator生成的annotation并不会被自动清除。您可根据需要手动清除。
>
![](https://main.qcloudimg.com/raw/750af0d5443cd670f856ba9b6bfbe63d.png)

### dynamic-scheduler

dynamic-scheduler是一个scheduler-extender，根据node annotation负载数据，在节点预选和优选中进行过滤和评分计算。

#### 预选策略

为了避免Pod调度到高负载的Node上，需要先通过预选把一些高负载的Node过滤掉（其中的过滤策略和比例是可以动态配置的，具体请查看后续参数配置说明）。如下图所示，Node2过去5分钟的负载，Node3过去1小时的负载多超过了对应的域值，所以不会参与接下来的优选阶段。
![](https://main.qcloudimg.com/raw/c841416dd1536ace7af02f790ba4485d.png)

#### 优选策略

同时为了使集群各节点的负载尽量均衡，Dynamic-scheduler会根据Node负载数据进行打分, 负载越低打分越高。如下图所示Node1的打分最高将会被优先调度（这些打分策略和权重也是可以动态配置的，具体请查看后续参数配置说明）。
![](https://main.qcloudimg.com/raw/f65af9208923627071b84a88daa1f316.png)

## 在集群内部署的kubernetes对象

### Kubernetes 资源

| Kubernets对象名称        | 类型               |                   请求资源                   | 所属Namespace |
| :----------------------- | :----------------- | :------------------------------------------: | ------------- |
| node-annotator           | Deployment         | 每个实例CPU:100m，Memory:100Mi ，共1个实例 | kube-system   |
| dynamic-scheduler        | Deployment         | 每个实例CPU:400m，Memory:200Mi，共3个实例  | kube-system   |
| dynamic-scheduler        | Service            |                      -                       | kube-system   |
| node-annotator           | ClusterRole        |                      -                       | kube-system   |
| node-annotator           | ClusterRoleBinding |                      -                       | kube-system   |
| node-annotator           | ServiceAccount     |                      -                       | kube-system   |
| dynamic-scheduler-policy | ConfigMap          |                      -                       | kube-system   |
| restart-kube-scheduler   | ConfigMap          |                      -                       | kube-system   |
| probe-prometheus         | ConfigMap          |                      -                       | kube-system   |

## 组件参数说明

### Prometheus数据查询地址

> ! 请确保您已经按照【依赖部署】-【Prometheus规则配置】进行了监控数据采集规则配置，这样我们的组件才可以拉取到需要的监控数据，调度策略才会生效。

1. 如果您使用自建Prometheus，直接填入数据查询url（http/https）即可。
2. 如果您使用托管Promethes, 选择托管实例id即可，我们会自动解析实例对应的数据查询url

### 预选参数

> !
> 预选和优选参数我们已经为您设置了默认值，如您无额外需求，可直接采用。

- 5分钟平均**cpu**利用率阈值：
  节点过去 5分钟 **平均** cpu利用率超过设定阈值，不会调度pod到该节点上
- 1小时最大**cpu**利用率阈值：
  节点过去 1小时 **最大** cpu利用率超过设定阈值，不会调度pod到该节点上
- 5分钟平均**内存**利用率阈值：
  节点过去 5分钟 **平均** 内存利用率超过设定阈值，不会调度pod到该节点上

- 1小时最大**内存**利用率阈值：
  节点过去 1小时 **最大** 内存利用率超过设定阈值，不会调度pod到该节点上

### 优选参数

- 5分钟平均**cpu**利用率权重
  该权重越大，过去 5分钟 节点**平均**cpu利用率对节点的评分影响越大
- 1小时最大**cpu**利用率权重
  该权重越大，过去 1小时 节点**最大**cpu利用率对节点的评分影响越大
- 1天最大**cpu**利用率权重
  该权重越大，过去 1天内 节点**最大**cpu利用率对节点的评分影响越大
- 5分钟平均**内存**利用率权重
  该权重越大，过去 5分钟 节点**平均**内存利用率对节点的评分影响越大
- 1小时最大**内存**利用率权重
  该权重越大，过去 1小时 节点**最大**内存利用率对节点的评分影响越大
- 1天最大**内存**利用率权重
  该权重越大，过去 1天内 节点**最大**内存利用率对节点的评分影响越大

## 风险控制

1. 该组件已对接TKE的监控告警体系。
2. 推荐您为集群开启事件持久化，以免更好的监控组件异常以及故障定位。
3. 该组件卸载后，只会删除动态调度器有关调度逻辑，不会对原生Kube-Scheduler的调度功能有任何影响。

## 使用方法

1. 按照【依赖部署】部署好Prometheus, Node-Exporter，并配置好 Prometheus Rule。
2. 单击左侧导航栏中的【集群】，进入集群管理界面。
3. 单击需新建组件的集群 ID，进入集群详情页，在该页面左侧栏中选择【组件管理】。
4. 单击【新建】，进入“新建组件”页面。
5. 在组件列表勾选【Dynamic Scheduler(动态调度器)】，点击【参数配置】。
6. 按照【参数说明】填写组件所需参数。
7. 单击【完成】，组件安装成功后Dynamic Scheduler即可正常运行，无需进行额外配置。
