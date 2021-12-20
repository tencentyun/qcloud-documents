## 操作场景

在使用数据库 Redis 过程中需要对 Redis 运行状态进行监控，以便了解 Redis 服务是否运行正常，排查 Redis 故障等。Prometheus 监控服务提供基于 Exporter 的方式来监控 Redis 运行状态，并提供了开箱即用的 Grafana 监控大盘。本文为您介绍如何使用 Prometheus 监控 Redis。

>?为了方便安装管理 Exporter，推荐使用腾讯云 [容器服务](https://cloud.tencent.com/document/product/457) 进行统一管理。




## 前提条件


- 在 Prometheus 实例对应地域及私有网络 VPC 下，创建腾讯云容器服务 [Kubernetes 集群](https://cloud.tencent.com/document/product/457/32189#TemplateCreation)，并为集群创建 [命名空间](https://cloud.tencent.com/document/product/1141/41803)。
- 在 [**Prometheus 监控服务控制台**](https://console.cloud.tencent.com/monitor/prometheus) > **选择“对应的 Prometheus 实例”** > **集成容器服务**中找到对应容器集群完成集成操作，详情请参见 [Agent 管理](https://cloud.tencent.com/document/product/1416/56000)。



## 操作步骤

### Exporter 部署


1. 登录 [容器服务](https://console.cloud.tencent.com/tke2/cluster) 控制台。
2. 单击需要获取集群访问凭证的集群 ID/名称，进入该集群的管理页面。
3. 执行以下 [使用 Secret 管理 Redis 密码](#step1) > [部署 Redis Exporter](#step2) > [验证](#step3) 步骤完成 Exporter 部署。



#### 使用 Secret 管理 Redis 密码[](id:step1)

1. 在左侧菜单中选择**工作负载** > **Deployment**，进入 Deployment 页面。
2. 在页面右上角单击 **YAML 创建资源**，创建 YAML 配置，配置说明如下：
使用 Kubernetes 的 Secret 来管理密码并对密码进行加密处理，在启动 Redis Exporter 的时候直接使用 Secret Key，需要调整对应的 `password`，YAML 配置示例如下：
<dx-codeblock>
:::  yaml
apiVersion: v1
kind: Secret
metadata:
    name: redis-secret-test
    namespace: redis-test
type: Opaque
stringData:
    password: you-guess  #对应 Redis 密码
:::
</dx-codeblock>

#### 部署 Redis Exporter[](id:step2)

在 Deployment 管理页面，单击**新建**，选择对应的**命名空间**来进行部署服务。可以通过控制台的方式创建，如下以 YAML 的方式部署 Exporter，YAML 配置示例如下：
>?更多 Exporter 详细参数介绍请参见 [redis_exporter](https://github.com/oliver006/redis_exporter)。

<dx-codeblock>
:::  yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    k8s-app: redis-exporter # 根据业务需要调整成对应的名称，建议加上 Redis 实例的信息
  name: redis-exporter # 根据业务需要调整成对应的名称，建议加上 Redis 实例的信息
  namespace: redis-test
spec:
  replicas: 1
  selector:
    matchLabels:
      k8s-app: redis-exporter # 根据业务需要调整成对应的名称，建议加上 Redis 实例的信息
  template:
    metadata:
      labels:
        k8s-app: redis-exporter # 根据业务需要调整成对应的名称，建议加上 Redis 实例的信息
    spec:
      containers:
      - env:
        - name: REDIS_ADDR
          value: ip:port # 对应 Redis 的 ip:port
        - name: REDIS_PASSWORD
          valueFrom:
            secretKeyRef:
              name: redis-secret-test
              key: password
        image: ccr.ccs.tencentyun.com/redis-operator/redis-exporter:1.12.0
        imagePullPolicy: IfNotPresent
        name: redis-exporter
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



#### 验证[](id:step3)

1. 在 Deployment 页面单击上述步骤创建的 Deployment，进入 Deployment 管理页面。
2. 单击**日志**页签，可以查看到 Exporter 成功启动并暴露对应的访问地址，如下图所示：
	 ![](https://main.qcloudimg.com/raw/4f38e24d2363579014719e303f5667d1.png)
3. 单击 **Pod 管理**页签，进入 Pod 页面。
4. 在右侧的操作项下单击**远程登录**登录 Pod，在命令行窗口中执行以下 curl 命令对应 Exporter 暴露的地址，可以正常得到对应的 Redis 指标。如发现未能得到对应的数据，请检查一下 `REDIS_ADDR` 和 `REDIS_PASSWORD` 是否正确。示例如下：
```
curl localhost:9121/metrics
```
	命令执行结果如下图所示：
	![](https://main.qcloudimg.com/raw/bbac65ba711420fdb81d11cf6c4a3cdb.png)




### 添加采取任务

1. 登录 [ Prometheus 监控服务控制台](https://console.cloud.tencent.com/monitor/prometheus)，选择对应 Prometheus 实例进入管理页面。
2. 通过集成容器服务列表单击**集群 ID** 进入到容器服务集成管理页面。
3. 通过服务发现添加 `Pod Monitor` 来定义 Prometheus 抓取任务，YAML 配置示例如下：

<dx-codeblock>
:::  yaml
  apiVersion: monitoring.coreos.com/v1
  kind: PodMonitor
  metadata:
    name: redis-exporter # 填写一个唯一名称
    namespace: cm-prometheus  # namespace固定，不要修改
  spec:
    podMetricsEndpoints:
    - interval: 30s
      port: metric-port  # 填写pod yaml中Prometheus Exporter对应的Port的Name
      path: /metrics  # 填写Prometheus Exporter对应的Path的值，不填默认/metrics
      relabelings:
      - action: replace
        sourceLabels:
        - instance
        regex: (.*)
        targetLabel: instance
        replacement: 'crs-xxxxxx' # 调整成对应的 Redis 实例 ID
      - action: replace
        sourceLabels:
        - instance
        regex: (.*)
        targetLabel: ip
        replacement: '1.x.x.x' # 调整成对应的 Redis 实例 IP
    namespaceSelector:   # 选择要监控pod所在的namespace
      matchNames:
      - redis-test
    selector:    # 填写要监控pod的Label值，以定位目标pod
      matchLabels:
        k8s-app: redis-exporter
:::
</dx-codeblock>

>?由于 `Exporter` 和 `Redis` 部署在不同的服务器上，因此建议通过 Prometheus Relabel 机制将 Redis 实例的信息放到监控指标中，以方便定位问题。



### 查看监控


1. 登录 [ Prometheus 监控服务控制台](https://console.cloud.tencent.com/monitor/prometheus)，选择对应 Prometheus 实例进入管理页面。
2. 单击**集成中心**，进入集成中心页面。找到 Redis 监控，安装对应的 Grafana Dashboard 即可开启 Redis 监控大盘，查看实例相关的监控数据，如下图所示：
![](https://main.qcloudimg.com/raw/ce0215baf6137d35341d56419bfb6d36.png)

### 告警以及接入

1. 登录 [Prometheus 监控服务控制台](https://console.cloud.tencent.com/monitor/prometheus)，选择对应 Prometheus 实例进入管理页面。
2. 单击告警策略，可以添加相应的告警策略，详情请参见 [新建告警策略](https://cloud.tencent.com/document/product/248/48952)。
