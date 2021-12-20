## 操作场景

在使用 MongoDB 过程中需要对 MongoDB 运行状态进行监控，以便了解 MongoDB 服务是否运行正常，排查 MongoDB 故障问题原因，云监控 Prometheus 服务提供了基于 Exporter 的方式来监控 MongoDB 运行状态，并提供了开箱即用的 Grafana 监控大盘。本文介绍如何部署 Exporter 以及实现 MongoDB Exporter 告警接入等操作。


>?为了方便安装管理 Exporter，推荐使用腾讯云 [容器服务](https://cloud.tencent.com/document/product/457) 进行统一管理。

## 前提条件

- 在 Proemtheus 实例对应地域及私有网络 VPC 下，创建腾讯云容器服务 [Kubernetes 集群](https://cloud.tencent.com/document/product/457/32189#TemplateCreation)。
- 在**[云监控 Prometheus 控制台](https://console.cloud.tencent.com/monitor/prometheus)** >**选择“对应的 Prometheus 实例”** >**集成容器服务**中找到对应容器集群完成集成操作，详情请参见 [Agent 管理](https://cloud.tencent.com/document/product/248/48859)。



## 操作步骤

### Exporter 部署

1. 登录 [容器服务](https://console.cloud.tencent.com/tke2/cluster) 控制台。
2. 单击需要获取集群访问凭证的集群 ID/名称，进入该集群的管理页面。
3. 执行以下 [使用 Secret 管理 MongoDB 连接串](#step1) > [部署 MongoDB Exporter](#step2) > [验证](#step3) 步骤完成 Exporter 部署。

[](id:step1)

#### 使用 Secret 管理 MongoDB 连接串

1. 在左侧菜单中选择**工作负载** > **Deployment**，进入 Deployment 页面。
2. 在页面右上角单击**YAML创建资源**，创建 YAML 配置，配置说明如下：
   使用 Kubernetes 的 Secret 来管理密码并对密码进行加密处理，在启动 MongoDB   Exporter 的时候直接使用 Secret Key，需要调整对应的 URI，YAML 配置示例如下：
```yaml
apiVersion: v1
kind: Secret
metadata:
      name: mongodb-secret-test
      namespace: mongodb-test
type: Opaque
stringData:
      datasource: "mongodb://{user}:{passwd}@{host1}:{port1},{host2}:{port2},{host3}:{port3}/admin"  # 对应连接URI
```

[](id:step2)

#### 部署 MongoDB Exporter

在 Deployment 管理页面，单击**新建**，选择对应的**命名空间**来进行部署服务。可以通过控制台的方式创建，如下以 YAML 的方式部署 Exporter，YAML 配置示例如下：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    k8s-app: mongodb-exporter # 根据业务需要调整成对应的名称，建议加上 MongoDB 实例的信息
  name: mongodb-exporter # 根据业务需要调整成对应的名称，建议加上 MongoDB 实例的信息
  namespace: mongodb-test
spec:
  replicas: 1
  selector:
    matchLabels:
      k8s-app: mongodb-exporter # 根据业务需要调整成对应的名称，建议加上 MongoDB 实例的信息
  template:
    metadata:
      labels:
        k8s-app: mongodb-exporter # 根据业务需要调整成对应的名称，建议加上 MongoDB 实例的信息
    spec:
      containers:
        - args:
            - --collect.database       # 启用采集 Database metrics
            - --collect.collection     # 启用采集 Collection metrics
            - --collect.topmetrics     # 启用采集 table top metrics
            - --collect.indexusage     # 启用采集 per index usage stats
            - --collect.connpoolstats  # 启动采集 MongoDB connpoolstats
          env:
            - name: MONGODB_URI
              valueFrom:
                secretKeyRef:
                  name: mongodb-secret-test
                  key: datasource
          image: ssheehy/mongodb-exporter
          imagePullPolicy: IfNotPresent
          name: mongodb-exporter
          ports:
            - containerPort: 9216
                name: metric-port  # 这个名称在配置抓取任务的时候需要
          securityContext:
            privileged: false
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
      dnsPolicy: ClusterFirst
      imagePullSecrets:
        - name: qcloudregistrykey
      restartPolicy: Always
      schedulerName: default-scheduler
      securityContext: { }
      terminationGracePeriodSeconds: 30
```

>?Exporter 详细参数请参见 [mongodb_exporter](https://github.com/percona/mongodb_exporter)。

[](id:step3)

#### 验证

1. 在 Deployment 页面单击上述步骤创建的 Deployment，进入 Deployment 管理页面。
2. 单击**日志**页签，可以查看到 Exporter 成功启动并暴露对应的访问地址，如下图所示：
![](https://main.qcloudimg.com/raw/8e02dd72301a6dbcf91e2c121dba3084.png)
3. 单击**Pod管理**页签，进入 Pod 页面。
4. 在右侧的操作项下单击**远程登录**登录 Pod，在命令行中执行以下 wget 命令对应 Exporter 暴露的地址，可以正常得到对应的 MongoDB 指标，若发现未能得到对应的数据，请检查一下连接 URI 是否正确，具体如下：
```
wget 127.0.0.1:9216/metrics 
cat metrics
```
命令执行结果如下图所示：
![](https://main.qcloudimg.com/raw/8437a4020c4923087680786f1bd9c9e4.png)



### 添加采集任务

1. 登录 [云监控 Prometheus 控制台](https://console.cloud.tencent.com/monitor/prometheus)，选择对应 Prometheus 实例进入管理页面。
2. 通过集成容器服务列表单击**集群 ID**进入到容器服务集成管理页面。
3. 通过服务发现添加 `Pod Monitor` 来定义 Prometheus 抓取任务，YAML 配置示例如下：

```yaml
  apiVersion: monitoring.coreos.com/v1
  kind: PodMonitor
  metadata:
    name: mongodb-exporter # 填写一个唯一名称
    namespace: cm-prometheus  # namespace固定，不要修改
  spec:
    podMetricsEndpoints:
    - interval: 30s
      port: metric-port   # 填写pod yaml中Prometheus Exporter对应的Port的Name
      path: /metrics  # 填写Prometheus Exporter对应的Path的值，不填默认/metrics
      relabelings:
      - action: replace
        sourceLabels: 
        - instance
        regex: (.*)
        targetLabel: instance
        replacement: 'cmgo-xxxxxxxx' # 调整成对应的 MongoDB 实例 ID
    namespaceSelector:  # 选择要监控pod所在的namespace
      matchNames:
      - mongodb-test 
    selector: # 填写要监控pod的Label值，以定位目标pod
      matchLabels:
        k8s-app: mongodb-exporter
```

> ? 由于 `Exporter` 和 `MongoDB` 部署在不同的服务器上，因此建议通过 Prometheus Relabel 机制将 MongoDB 实例的信息放到监控指标中，以便定位问题。

### 查看监控

1. 登录 [云监控 Prometheus 控制台](https://console.cloud.tencent.com/monitor/prometheus)，选择对应 Prometheus 实例进入管理页面。
2. 单击**集成中心**，进入集成中心页面。找到 `MongoDB`监控，安装对应的 Grafana Dashboard 即可开启 `MongoDB` 监控大盘，查看实例相关的监控数据，如下图所示：
	- **MongoDB 概览**：以实例的纬度查看实例状态，例如文档个数、连接使用率、读写耗时等，可单击实例跳转到该实例详情。
	![](https://main.qcloudimg.com/raw/3e211a4a306c2ae9dd92d38fd11a24cc.png)
	- **MongoDB 详情**：可以查看某个实例的详细状态，例如元数据概览、核心指标、命令操作、请求流量、读写 Top 等。
	![](https://main.qcloudimg.com/raw/6c60788641571a7f848b81fb975b37ff.png)
> ? 每个图表可以单击左侧的**!**进行查看说明

### 告警以及接入

1. 登录 [云监控 Prometheus 控制台](https://console.cloud.tencent.com/monitor/prometheus)，选择对应 Prometheus 实例进入管理页面。
2. 单击告警策略，可以添加相应的告警策略，详情请参见 [新建告警策略](https://cloud.tencent.com/document/product/248/48952)。


## 常见问题

#### 客户端报错：client checkout connect timeout，该如何处理？

可能是连接池使用率达到100%，导致创建连接失败。可以通过 Grafana 大盘**MongoDB 详情/核心指标/连接使用率**指标排查。
![](https://main.qcloudimg.com/raw/ed65b8c0a8b9013e2532e392a55a1058.png)

#### 写入不断超时，该如何处理？

需检查 Cache 使用率是否过高、Transactions 可用个数是否为0，可以通过 Grafana 大盘**MongoDB详情/核心指标/ WiredTiger Transactions 可用个数| WiredTiger Cache 使用率| GetLastError 写耗时| GetLastError 写超时**指标排查。
![](https://main.qcloudimg.com/raw/282ab600c5d8a65e0735d61b538e3db8.png)
