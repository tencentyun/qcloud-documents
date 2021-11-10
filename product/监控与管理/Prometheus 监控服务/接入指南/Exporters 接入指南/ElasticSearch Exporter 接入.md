## 操作场景

在使用 ElasticSearch 过程中需要对 ElasticSearch 运行状态进行监控，例如集群及索引状态等， Prometheus 监控服务提供了基于 Exporter 的方式来监控 ElasticSearch 运行状态，并提供了开箱即用的 Grafana 监控大盘。本文介绍如何部署 Exporter 以及实现 ElasticSearch Exporter 告警接入等操作。



>?为了方便安装管理 Exporter，推荐使用腾讯云 [容器服务](https://cloud.tencent.com/document/product/457) 进行统一管理。

## 前提条件

- 在 Prometheus 实例对应地域及私有网络 VPC 下，创建腾讯云容器服务 [托管版集群](https://cloud.tencent.com/document/product/457/32189#TemplateCreation)，并为集群创建 [命名空间](https://cloud.tencent.com/document/product/1141/41803)。
- 在 [**Prometheus 监控服务控制台**](https://console.cloud.tencent.com/monitor/prometheus) > **选择“对应的 Prometheus 实例”** > **集成容器服务**中找到对应容器集群完成集成操作，详情请参见 [Agent 管理](https://cloud.tencent.com/document/product/1416/56000)。


## 操作步骤

### Exporter 部署



1. 登录 [容器服务](https://console.cloud.tencent.com/tke2/cluster) 控制台。
2. 单击需要获取集群访问凭证的集群 ID/名称，进入该集群的管理页面。
3. 执行以下 [使用 Secret 管理 ElasticSearch 连接串](#step1) > [部署 ElasticSearch Exporter](#step2) > [验证](#step3) 步骤完成 Exporter 部署。

[](id:step1)

#### 使用 Secret 管理 ElasticSearch 连接串[](id:step1)

1. 在左侧菜单中选择**工作负载** > **Deployment**，进入 Deployment 页面。
2. 在页面右上角单击 **YAML创建资源**，创建 YAML 配置，配置说明如下：
   使用 Kubernetes 的 Secret 来管理密码并对密码进行加密处理，在启动 ElasticSearch Exporter 的时候直接使用 Secret Key，需要调整对应的 URI，YAML 配置示例如下：
	

<dx-codeblock>
:::  yaml
apiVersion: v1
kind: Secret
metadata:
  name: es-secret-test
  namespace: es-demo 
type: Opaque
stringData:
  esURI: you-guess  #对应 ElasticSearch 的 URI
:::
</dx-codeblock>

>?ElasticSearch 连接串的格式为 `<proto>://<user>:<password>@<host>:<port>`，例如 `http://admin:pass@localhost:9200`。

[](id:step2)

#### 部署 ElasticSearch Exporter[](id:step2)

在 Deployment 管理页面，单击**新建**，选择对应的**命名空间**来进行部署服务。可以通过控制台的方式创建，如下以 YAML 的方式部署 Exporter，YAML 配置示例如下：

<dx-codeblock>
:::  yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    k8s-app: es-exporter
  name: es-exporter
  namespace: es-demo
spec:
  replicas: 1
  selector:
    matchLabels:
      k8s-app: es-exporter
  template:
    metadata:
      labels:
        k8s-app: es-exporter
    spec:
      containers:
      - env:
          - name: ES_URI
            valueFrom:
              secretKeyRef:
                name: es-secret-test
                key: esURI
          - name: ES_ALL
            value: "true"
        image: bitnami/elasticsearch-exporter:latest
        imagePullPolicy: IfNotPresent
        name: es-exporter
        ports:
        - containerPort: 9114
          name: metric-port
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

>?上述示例通过 `ES_ALL` 采集了所有 ElasticSearch 的监控项，可以通过对应的参数进行调整，Exporter 更多详细的参数请参见 [elasticsearch_exporter](https://github.com/justwatchcom/elasticsearch_exporter)。

[](id:step3)

#### 验证[](id:step3)


1. 在 Deployment 页面单击上述步骤创建的 Deployment，进入 Deployment 管理页面。
2. 单击**日志**页签，可以查看到 Exporter 成功启动并暴露对应的访问地址，如下图所示：
    ![](https://main.qcloudimg.com/raw/c9b6c2a85da29a9176ae720d70ace7bb.png)
3. 单击**Pod管理**页签进入 Pod 页面。
4. 在右侧的操作项下单击**远程登录**登录 Pod，在命令行窗口中执行以下 curl 命令对应 Exporter 暴露的地址，可以正常得到对应的 ElasticSearch 指标。如发现未能得到对应的数据，请检查**连接串**是否正确，具体如：
```
curl localhost:9114/metrics
```
执行结果如下图所示：
![](https://main.qcloudimg.com/raw/0c919a2bee21aa48f117960dc696f6e2.png)




### 添加采取任务

1. 登录 [ Prometheus 监控服务控制台](https://console.cloud.tencent.com/monitor/prometheus)，选择对应 Prometheus 实例进入管理页面。
2. 通过集成容器服务列表单击**集群 ID**进入到容器服务集成管理页面。
3. 通过服务发现添加 `Pod Monitor` 来定义 Prometheus 抓取任务，YAML 配置示例如下：

<dx-codeblock>
:::  yaml
apiVersion: monitoring.coreos.com/v1
kind: PodMonitor
metadata:
  name: es-exporter
  namespace: cm-prometheus
spec:
  namespaceSelector:
    matchNames:
      - es-demo
  podMetricsEndpoints:
  - interval: 30s
    path: /metrics
    port: metric-port
    selector:
    matchLabels:
    k8s-app: es-exporter
:::
</dx-codeblock>

### 查看监控

1. 登录 [ Prometheus 监控服务控制台](https://console.cloud.tencent.com/monitor/prometheus)，选择对应 Prometheus 实例进入管理页面。
2. 单击**集成中心**，进入集成中心页面。找到 ElasticSearch 监控，安装对应的 Grafana Dashboard 即可开启 ElasticSearch 监控大盘，查看实例相关的监控数据，如下图所示：
![](https://main.qcloudimg.com/raw/d4361aa170c8ab94ed13d9c5cd15f4d7.png)


### 告警以及接入

1. 登录 [ Prometheus 监控服务控制台](https://console.cloud.tencent.com/monitor/prometheus)，选择对应 Prometheus 实例进入管理页面。
2. 单击告警策略，可以添加相应的告警策略，详情请参见 [新建告警策略](https://cloud.tencent.com/document/product/1416/56009)。
