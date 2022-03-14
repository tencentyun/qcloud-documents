## 操作场景

在使用 Kafka 过程中需要对 Kafka 运行状态进行监控，例如集群状态、消息消费情况是否有积压等， Prometheus 监控服务提供基于 Exporter 的方式来监控 Kafka 运行状态，并提供了开箱即用的 Grafana 监控大盘。本文介绍如何部署 Exporter 以及实现 Kafka Exporter 告警接入等操作。



>?为了方便安装管理 Exporter，推荐使用腾讯云 [容器服务](https://cloud.tencent.com/document/product/457) 进行统一管理。

## 前提条件

- 在 Prometheus 实例对应地域及私有网络 VPC 下，创建腾讯云容器服务 [托管版集群](https://cloud.tencent.com/document/product/457/32189#TemplateCreation)，并为集群创建 [命名空间](https://cloud.tencent.com/document/product/1141/41803)。
- 在 [**Prometheus 监控服务控制台**](https://console.cloud.tencent.com/monitor/prometheus) > **选择“对应的 Prometheus 实例”** > **集成容器服务**中找到对应容器集群完成集成操作，详情请参见 [Agent 管理](https://cloud.tencent.com/document/product/1416/56000)。


## 操作步骤

### Exporter 部署


1. 登录 [容器服务](https://console.cloud.tencent.com/tke2/cluster) 控制台。
2. 单击需要获取集群访问凭证的集群 ID/名称，进入该集群的管理页面。
3. 在左侧菜单中选择**工作负载** > **Deployment**，进入 Deployment 页面。
4. 在 Deployment 管理页面，单击**新建**，选择对应的**命名空间**来进行部署服务。可以通过控制台的方式创建，如下以 YAML 的方式部署 Exporter，YAML 配置示例如下：

<dx-codeblock>
:::  yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    k8s-app: kafka-exporter # 根据业务需要调整成对应的名称，建议加上 Kafka 实例的信息
  name: kafak-exporter # 根据业务需要调整成对应的名称，建议加上 Kafka 实例的信息
  namespace: kafka-demo
spec:
  replicas: 1
  selector:
    matchLabels:
      k8s-app: kafka-exporter # 根据业务需要调整成对应的名称，建议加上 Kafka 实例的信息
  template:
    metadata:
      labels:
        k8s-app: kafka-exporter # 根据业务需要调整成对应的名称，建议加上 Kafka 实例的信息
    spec:
      containers:
      - args:
        - --kafka.server=x.x.x.x:9092 # 对应 Kafka 实例的地址信息
        image: danielqsj/kafka-exporter:latest
        imagePullPolicy: IfNotPresent
        name: kafka-exporter
        ports:
        - containerPort: 9121
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
      securityContext: {}
      terminationGracePeriodSeconds: 30
:::
</dx-codeblock>

>?Exporter 详细参数请参见 [kafka_exporter](https://github.com/danielqsj/kafka_exporter)。


### 添加采取任务

1. 登录 [ Prometheus 监控服务控制台](https://console.cloud.tencent.com/monitor/prometheus)，选择对应 Prometheus 实例进入管理页面。
2. 通过集成容器服务列表单击**集群 ID** 进入到容器服务集成管理页面。
3. 通过服务发现添加 `Pod Monitor` 来定义 Prometheus 抓取任务，YAML 配置示例如下：

<dx-codeblock>
:::  yaml
  apiVersion: monitoring.coreos.com/v1
  kind: PodMonitor
  metadata:
    name: kafka-exporter  # 填写一个唯一名称
    namespace: cm-prometheus  # namespace固定，不要修改
  spec:
    podMetricsEndpoints:
    - interval: 30s
      port: metric-port # 填写pod yaml中Prometheus Exporter对应的Port的Name
      path: /metrics # 填写Prometheus Exporter对应的Path的值，不填默认/metrics
      relabelings:
      - action: replace
        sourceLabels:
        - instance
        regex: (.*)
        targetLabel: instance
        replacement: 'ckafka-xxxxxx' # 调整成对应的 Kafka 实例 ID
      - action: replace
        sourceLabels:
        - instance
        regex: (.*)
        targetLabel: ip
        replacement: '1.x.x.x' # 调整成对应的 Kafka 实例 IP
        namespaceSelector:
      matchNames:
      - kafka-demo
        selector:  # 填写要监控pod的Label值，以定位目标pod
      matchLabels:
        k8s-app: kafka-exporter
:::
</dx-codeblock>

>?由于 `Exporter` 和 `Kafka` 部署在不同的服务器上，因此建议通过 Prometheus Relabel 机制将 Kafka 实例的信息放到监控指标中，以便定位问题。

### 查看监控

1. 登录 [ Prometheus 监控服务控制台](https://console.cloud.tencent.com/monitor/prometheus)，选择对应 Prometheus 实例进入管理页面。
2. 单击**集成中心**，进入集成中心页面。找到 kafka 监控，安装对应的 Grafana Dashboard 即可开启 kafaka 监控大盘，查看实例相关的监控数据，如下图所示：
![](https://main.qcloudimg.com/raw/9eac552bd9fda6604c9d845604dd5ef0.png)


### 告警以及接入

1. 登录 [ Prometheus 监控服务控制台](https://console.cloud.tencent.com/monitor/prometheus)，选择对应 Prometheus 实例进入管理页面。
2. 单击告警策略，可以添加相应的告警策略，详情请参见 [新建告警策略](https://cloud.tencent.com/document/product/1416/56009)。
