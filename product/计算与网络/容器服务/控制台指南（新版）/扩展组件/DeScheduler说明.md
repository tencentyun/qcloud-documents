## 组件介绍

`DeScheduler` 是腾讯云TKE基于Kubernetes原生的 社区 [descheduler](https://github.com/kubernetes-sigs/descheduler)  实现的一个基于Node真实负载进行重调度的插件。 在 TKE 集群中安装该插件后，该插件会和Kube-scheduler协同生效，实时监控集群中高负载节点并驱逐低优先级pod。 
该组件依赖Prometheus监控组件以及相关规则配置，强烈建议您安装组件之前仔细阅读【依赖部署】，以免插件无法正常工作。
强烈建议您与TKE的 `Dynamic Scheduler`(动态调度器扩展组件) 一起使用，多维度保障集群负载均衡。


## 应用场景

`DeScheduler`  的重调度思想就是通过重调度来解决集群现有节点上一些不合理的运行方式，社区版本的`DeScheduler` 已经给出一些策略，只是这些策略是基于APIServer中的数据，并没有基于节点真实负载。所以，可以增加对于节点的监控，基于真实负载进行重调度调整。

腾讯云TKE自研的 `ReduceHighLoadNode` 策略就是基于这样的目的，依赖prometheus+node_exporter监控数据，基于节点cpu利用率/内存利用率/网络IO/system loadavg等指标进行pod驱逐重调度。防止出现节点极端负载的情况。`DeScheduler` 中的驱逐策略对应于调度器时都有相应的调度策略，所以`DeScheduler` 的`ReduceHighLoadNode` 与 腾讯云TKE自研的 `Dynamic Scheduler`基于节点真实负载进行调度的策略是很适合配合起来使用。

## 限制条件

1. k8s版本 建议 >= v1.10.x

## 在集群内部署的kubernetes对象

| Kubernets对象名称  | 类型               |                   请求资源                   | 所属Namespace |
| :----------------- | :----------------- | :------------------------------------------: | ------------- |
| descheduler        | Deployment         | 每个实例CPU: 200m, Memory: 200Mi ，共1个实例 | kube-system   |
| descheduler        | ClusterRole        |                      -                       | kube-system   |
| descheduler        | ClusterRoleBinding |                      -                       | kube-system   |
| descheduler        | ServiceAccount     |                      -                       | kube-system   |
| descheduler-policy | ConfigMap          |                      -                       | kube-system   |
| probe-prometheus   | ConfigMap          |                      -                       | kube-system   |

## 依赖部署

`DeScheduler`依赖于Node当前和过去一段时间的真实负载情况来进行调度决策，这依赖于Prometheus等监控组件获取系统Node真实负载信息。在使用`DeScheduler`之前，需要部署Prometheus等监控组件。在TKE，用户可以采用自建的Prometheus监控服务，也可以采用TKE推出的云原生监控，下面对这两种方式依次介绍。

### 用户自建Prometheus等监控服务

##### 部署node-exporter 和 prometheus

我们通过node-exporter实现对于Node指标的监控，用户可以根据自己的需要部署node-exporter和prometheus。

#### 聚合规则配置

在 node-exporter获取节点监控数据后，需要通过Prometheus对原始的node-exporter中采集数据进行聚合计算。为了获取`DeScheduler`中需要 `cpu_usage_avg_5m`，`mem_usage_avg_5m`, 等指标，需要在Prometheus的 rules 规则配置如下：

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

#### pometheus文件配置

前面定义了`DeScheduler`所需要的指标计算的rule，然后我们需要把这个rule配置到prometheus中，参考一般的prometheus配置文件

```
global:
  evaluation_interval: 30s
  scrape_interval: 30s
  external_labels:
rule_files:
- /etc/prometheus/rules/*.yml # /etc/prometheus/rules/*.yml就是定义的rules文件
```

我们把上面的rules配置，复制到一个文件如de-scheduler.yaml，文件放到上述prometheus 容器的/etc/prometheus/rules/下，然后reload prometheus server就可以从prometheus中获取到动态调度器需要的指标。

通常情况下，上述prometheus配置文件和rules配置文件都是通过configmap存储，然后挂载到prometheus server的容器里面，所以修改相应的configmap即可。

### 云原生监控Prometheus

1. 创建与Cluster处于同一VPC下的云原生监控Prometheus实例，并与用户集群关联。 
   ![](https://main.qcloudimg.com/raw/b17e7ea4642e6aaea70c885956f30b0b.png)
2. 与原生托管集群关联后，可以在用户集群看到每个节点都已经安装了node-exporter。 
   ![](https://main.qcloudimg.com/raw/e35d4af7eeba15f6d9da62ce79176904.png)

3. 接下来设置Prometheus的聚合规则，如下图所示，具体规则内容与上一小节介绍的规则相同，此处不再赘述。 规则保存后立即生效，无需reload server。

## 组件原理

`DeScheduler`  基于社区 [descheduler](https://github.com/kubernetes-sigs/descheduler) 的重调度思想，定期扫描各个节点上的运行pod，发现不符合策略条件的进行驱逐以进行重调度。社区版本的descheduler已经给出一些策略，只是这些策略是基于APIServer中的数据，比如 `LowNodeUtilization` 策略依赖的是pod的request/limit数据，这些数据对均衡集群资源分配，防止出现资源碎片有帮助。但是社区策略缺少节点真实资源占用的支持，例如节点A和B分配出去的资源一致，但是由于pod实际运行情况，cpu消耗型和内存消耗型不同，峰谷期不同造成两个节点的负载差别巨大。

因此，腾讯云TKE推出 `DeScheduler`，底层依赖对节点真实负载的监控进行重调度。具体实现上，通过 Prometheus 拿到集群Node的负载统计信息，根据用户设置的负载阈值，定期执行策略里面的检查规则，驱逐高负载节点上的 Pod 。

![](https://main.qcloudimg.com/raw/9a31a5d0995c40f3540a83da3b037323.png)

### 1. 查找高负载节点

![](https://main.qcloudimg.com/raw/ac5285d3fc10fad645239507570a3e39.png)

### 2. 筛选可驱逐pod

![](https://main.qcloudimg.com/raw/00c60959cb1956e1a1cfa9d683f1f542.png)

可迁移标记是我们指定的annotation，设置为 `"descheduler.alpha.kubernetes.io/evictable": true`，注入到workload中。


### 3. 根据pod驱逐顺序进行驱逐

当节点CPU或者内存超过阈值时，对节点进行Pod驱逐的顺序基于以下规则排序，比如有两个Pod ： A与B。

>? 当节点CPU和内存都超过了阈值时，先按照降低内存到目标水位的策略去驱逐pod，因为内存是不可压缩资源，且会同步将驱逐的pod对 节点CPU的降低值 更新到节点负载中。然后再按照降低CPU到目标水位的策略去驱逐pod。

1. priority值低的pod优先驱逐。
2. QosClass低的（besteffort < burstable < guaruanteed）优先驱逐。
3. 如果A与B的priority与QosClass都相同，则比较二者对CPU/内存的利用率，利用率高的优先驱逐（为了快速降低负载）。


## 组件参数说明

### Prometheus数据查询地址

> ! 请确保您已经按照【依赖部署】-【Prometheus规则配置】进行了监控数据采集规则配置，这样我们的组件才可以拉取到需要的监控数据，调度策略才会生效。

1. 如果您使用自建Prometheus，直接填入数据查询url（http/https）即可。
2. 如果您使用托管Promethes, 选择托管实例id即可，我们会自动解析实例对应的数据查询url

### 利用率阈值&目标利用率

> ! 负载阈值参数我们已经为您设置了默认值，如您无额外需求，可直接采用。
>
> 过去五分钟内，节点的cpu平均利用率或者内存平均使用率超过设定阈值，Descheduler会判断节点为高负载节点，执行pod驱逐逻辑（不可驱逐pod筛选以及驱逐顺序请参考组件说明），并尽量通过pod重调度使节点负载降到目标利用率以下。


## 风险控制

1. 该组件已对接TKE的监控告警体系。
2. 推荐您为集群开启事件持久化，以免更好的监控组件异常以及故障定位。
3. 为了避免 `DeScheduler` 驱逐了关键的Pod，设计的算法是默认不驱逐Pod，对于可以驱逐的Pod，用户需要显示给判断pod所属workload比如statefulset/deployment等对象设置可驱逐annotation。
4. pod驱逐太多导致服务不可用
   k8s原生有PDB对象来防止驱逐接口造成workload不可用pod过多，但是需要用户创建这样的pdb配置，腾讯云TKE自研的 `DeScheduler`里面加入了自己的兜底措施，即调用驱逐接口前，判断workload ready的pod数是否大于副本数一半，否则则不调用驱逐接口。

## 使用方法

1. 按照【依赖部署】部署好Prometheus, Node-Exporter，并配置好 Prometheus Rule。
2. 单击左侧导航栏中的【集群】，进入集群管理界面。
3. 单击需新建组件的集群 ID，进入集群详情页，在该页面左侧栏中选择【组件管理】。
4. 单击【新建】，进入“新建组件”页面。
5. 在组件列表勾选【Decheduler(重调度器)】，点击【参数配置】。
6. 按照【参数说明】填写组件所需参数。
7. 单击【完成】，组件安装成功后DeScheduler即可正常运行，无需进行额外配置。
8. 对于用户认为可以驱逐的workload（比如statefulset/deployment等对象），可以设置 `Annotation` 如下
   `descheduler.alpha.kubernetes.io/evictable: 'true'`

