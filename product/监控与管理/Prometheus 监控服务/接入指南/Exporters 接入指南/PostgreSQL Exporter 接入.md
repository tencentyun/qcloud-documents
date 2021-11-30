## 操作场景

在使用 PostgreSQL 过程中都需要对 PostgreSQL 运行状态进行监控，以便了解 PostgreSQL 服务是否运行正常，排查 PostgreSQL 故障问题原因， Prometheus 监控服务提供了基于 Exporter 的方式来监控 PostgreSQL 运行状态，并提供了开箱即用的 Grafana 监控大盘。本文介绍如何部署 Exporter 以及实现 PostgreSQL Exporter 告警接入等操作。


>?为了方便安装管理 Exporter，推荐使用腾讯云 [容器服务](https://cloud.tencent.com/document/product/457) 进行统一管理。

## 前提条件

- 在 Prometheus 实例对应地域及私有网络 VPC 下，创建腾讯云容器服务 [Kubernetes 集群](https://cloud.tencent.com/document/product/457/32189#TemplateCreation)。
- 在 [**Prometheus 监控服务控制台**](https://console.cloud.tencent.com/monitor/prometheus) > **选择“对应的 Prometheus 实例”** > **集成容器服务**中找到对应容器集群完成集成操作，详情请参见 [Agent 管理](https://cloud.tencent.com/document/product/1416/56000)。


## 操作步骤

### Exporter 部署

1. 登录 [容器服务](https://console.cloud.tencent.com/tke2/cluster) 控制台。
2. 单击需要获取集群访问凭证的集群 ID/名称，进入该集群的管理页面。
3. 执行以下 [使用 Secret 管理 PostgreSQL 密码](#step1) > [部署 PostgreSQL Exporter](#step2) > [获取指标](#step3) 步骤完成 Exporter 部署。


#### 使用 Secret 管理 PostgreSQL 密码[](id:step1) 

1. 在左侧菜单中选择**工作负载** > **Deployment**，进入 Deployment 页面。
2. 在页面右上角单击 **YAML 创建资源**，创建 YAML 配置，配置说明如下：
   使用 Kubernetes 的 Secret 来管理密码并对密码进行加密处理，在启动 PostgreSQL Exporter 的时候直接使用 Secret Key，需要调整对应的 `password`，YAML 配置示例如下：
<dx-codeblock>
:::  yaml
apiVersion: v1
kind: Secret
metadata:
    name: postgres-test
type: Opaque
stringData:
    username: postgres
    password: you-guess #对应 PostgreSQL 密码
:::
</dx-codeblock>

#### 部署 PostgreSQL Exporter[](id:step2) 

在 Deployment 管理页面，单击**新建**，选择对应的**命名空间**来进行部署服务。可以通过控制台的方式创建，如下以 YAML 的方式部署 Exporter，YAML 配置示例如下（`请直接复制下面的内容，根据实际业务调整相应的参数`）:

<dx-codeblock>
:::  yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: postgres-test
  namespace: postgres-test
  labels:
    app: postgres
    app.kubernetes.io/name: postgresql
spec:
  replicas: 1
  selector:
    matchLabels:
      app: postgres
      app.kubernetes.io/name: postgresql
  template:
    metadata:
      labels:
        app: postgres
        app.kubernetes.io/name: postgresql
    spec:
      containers:
      - name: postgres-exporter
        image: wrouesnel/postgres_exporter:latest
        args:
          - "--web.listen-address=:9187"
          - "--log.level=debug"
        env:
          - name: DATA_SOURCE_USER
            valueFrom:
              secretKeyRef:
                name: postgres-test
                key: username
          - name: DATA_SOURCE_PASS
            valueFrom:
              secretKeyRef:
                name: postgres-test
                key: password
          - name: DATA_SOURCE_URI
            value: "x.x.x.x:5432/postgres?sslmode=disable"
        ports:
        - name: http-metrics
          containerPort: 9187
:::
</dx-codeblock>

> ?上述示例将 Secret 中的用户名密码传给了环境变量 `DATA_SOURCE_USER` 和 `DATA_SOURCE_PASS`，使用户无法查看到明文的用户名密码。您还可以用 `DATA_SOURCE_USER_FILE`/`DATA_SOURCE_PASS_FILE` 从文件读取用户名密码。或使用 `DATA_SOURCE_NAME` 将用户名密码也放在连接串里，例如 `postgresql://login:password@hostname:port/dbname`。

#### 参数说明

`DATA_SOURCE_URI`/`DATA_SOURCE_NAME` 连接串 query 部分（`?`之后）支持的参数如下（最新的以 [GoDoc](https://pkg.go.dev/github.com/lib/pq#hdr-Connection_String_Parameters) 为准）：
<table>
<thead>
<tr>
<th>参数</th>
<th>参数说明</th>
</tr>
</thead>
<tbody><tr>
<td>sslmode</td>
<td>是否使用 SSL，支持的值如下：</td>
</tr>
<tr>
<td>- disable</td>
<td>不使用 SSL</td>
</tr>
<tr>
<td>- require</td>
<td>总是使用（跳过验证）</td>
</tr>
<tr>
<td>- verify-ca</td>
<td>总是使用（检查服务端提供的证书是不是由一个可信的 CA 签发）</td>
</tr>
<tr>
<td>- verify-full</td>
<td>总是使用（检查服务端提供的证书是不是由一个可信的 CA 签发，并且检查 hostname 是不是被证书所匹配）</td>
</tr>
<tr>
<td>fallback_application_name</td>
<td>一个备选的 <code>application_name</code></td>
</tr>
<tr>
<td>connect_timeout</td>
<td>最大连接等待时间，单位秒。0 值等于无限大</td>
</tr>
<tr>
<td>sslcert</td>
<td>证书文件路径。文件数据格式必须是 <code>PEM</code></td>
</tr>
<tr>
<td>sslkey</td>
<td>私钥文件路径。文件数据格式必须是 <code>PEM</code></td>
</tr>
<tr>
<td>sslrootcert</td>
<td>root 证书文件路径。文件数据格式必须是 <code>PEM</code></td>
</tr>
</tbody></table>

另外 Exporter 支持其他参数，如下说明（详情请参见 [README](https://github.com/wrouesnel/postgres_exporter)）：

<table>
<thead>
<tr>
<th>参数</th>
<th>参数说明</th>
<th>环境变量</th>
</tr>
</thead>
<tbody><tr>
<td>--web.listen-address</td>
<td>监听地址，默认 <code>:9487</code></td>
<td>PG_EXPORTER_WEB_LISTEN_ADDRESS</td>
</tr>
<tr>
<td>--web.telemetry-path</td>
<td>暴露指标的路径，默认 <code>/metrics</code></td>
<td>PG_EXPORTER_WEB_TELEMETRY_PATH</td>
</tr>
<tr>
<td>--extend.query-path</td>
<td>指定一个包含自定义查询语句的 YAML 文件，参考 <a href="https://github.com/wrouesnel/postgres_exporter/blob/master/queries.yaml">queries.yaml</a>。</td>
<td>PG_EXPORTER_EXTEND_QUERY_PATH</td>
</tr>
<tr>
<td>--disable-default-metrics</td>
<td>只使用通过 <code>queries.yaml</code> 提供的指标</td>
<td>PG_EXPORTER_DISABLE_DEFAULT_METRICS</td>
</tr>
<tr>
<td>--disable-settings-metrics</td>
<td>不抓取 <code>pg_settings</code> 相关的指标</td>
<td>PG_EXPORTER_DISABLE_SETTINGS_METRICS</td>
</tr>
<tr>
<td>--auto-discover-databases</td>
<td>是否自动发现 Postgres 实例上的数据库</td>
<td>PG_EXPORTER_AUTO_DISCOVER_DATABASES</td>
</tr>
<tr>
<td>--dumpmaps</td>
<td>打印内部的指标信息，除了 debug 不要使用，方便排查自定义 queries 相关的问题</td>
<td>-</td>
</tr>
<tr>
<td>--constantLabels</td>
<td>自定义标签，通过 <code>key=value</code> 的形式提供，多个标签对使用 <code>,</code> 分隔</td>
<td>PG_EXPORTER_CONSTANT_LABELS</td>
</tr>
<tr>
<td>--exclude-databases</td>
<td>需要排除的数据库，仅在 <code>--auto-discover-databases</code> 开启的情况下有效</td>
<td>PG_EXPORTER_EXCLUDE_DATABASES</td>
</tr>
<tr>
<td>--log.level</td>
<td>日志级别 <code>debug</code>/<code>info</code>/<code>warn</code>/<code>error</code>/<code>fatal</code></td>
<td>PG_EXPORTER_LOG_LEVEL</td>
</tr>
</tbody></table>

[](id:way)

#### 获取指标[](id:step3)

通过 `curl http://exporter:9187/metrics` 无法获取 `Postgres` 实例运行时间。我们可以通过自定义一个 `queries.yaml` 来获取该指标：

1. 创建一个包含 `queries.yaml` 的 [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/)。
2. 将 ConfigMap 作为 Volume 挂载到 Exporter 某个目录下面。
3. 通过 `--extend.query-path` 来使用 ConfigMap，将上述的 [Secret](#step1) 以及 [Deployment](#step2) 进行汇总，汇总后的 YAML 如下所示：

<dx-codeblock>
:::  yaml
# 注意: 以下 document 创建一个名为 postgres-test 的 Namespace，仅作参考
apiVersion: v1
kind: Namespace
metadata:
  name: postgres-test

# 以下 document 创建一个包含用户名密码的 Secret
---
apiVersion: v1
kind: Secret
metadata:
  name: postgres-test-secret
  namespace: postgres-test
type: Opaque
stringData:
  username: postgres
  password: you-guess

# 以下 document 创建一个包含自定义指标的 queries.yaml
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: postgres-test-configmap
  namespace: postgres-test
data:
  queries.yaml: |
    pg_postmaster:
      query: "SELECT pg_postmaster_start_time as start_time_seconds from pg_postmaster_start_time()"
      master: true
      metrics:
        - start_time_seconds:
            usage: "GAUGE"
            description: "Time at which postmaster started"

# 以下 document 挂载了 Secret 和 ConfigMap ，定义了部署 Exporter 相关的镜像等参数
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: postgres-test
  namespace: postgres-test
  labels:
    app: postgres
    app.kubernetes.io/name: postgresql
spec:
  replicas: 1
  selector:
    matchLabels:
      app: postgres
      app.kubernetes.io/name: postgresql
  template:
    metadata:
      labels:
        app: postgres
        app.kubernetes.io/name: postgresql
    spec:
      containers:
        - name: postgres-exporter
          image: wrouesnel/postgres_exporter:latest
          args:
            - "--web.listen-address=:9187"
            - "--extend.query-path=/etc/config/queries.yaml"
            - "--log.level=debug"
          env:
            - name: DATA_SOURCE_USER
              valueFrom:
                secretKeyRef:
                  name: postgres-test-secret
                  key: username
            - name: DATA_SOURCE_PASS
              valueFrom:
                secretKeyRef:
                  name: postgres-test-secret
                  key: password
            - name: DATA_SOURCE_URI
              value: "x.x.x.x:5432/postgres?sslmode=disable"
          ports:
            - name: http-metrics
              containerPort: 9187
          volumeMounts:
            - name: config-volume
              mountPath: /etc/config
      volumes:
        - name: config-volume
          configMap:
            name: postgres-test-configmap
:::
</dx-codeblock>

4. 执行 `curl http://exporter:9187/metrics`，即可通过自定义的 `queries.yaml` 查询到 Postgres 实例启动时间指标。示例如下：

```
# HELP pg_postmaster_start_time_seconds Time at which postmaster started
# TYPE pg_postmaster_start_time_seconds gauge
pg_postmaster_start_time_seconds{server="x.x.x.x:5432"} 1.605061592e+09
```



### 添加采取任务

当 Exporter 运行起来之后，需要进行以下操作配置 Prometheus 监控服务发现并采集监控指标：

1. 登录 [ Prometheus 监控服务控制台](https://console.cloud.tencent.com/monitor/prometheus)，选择对应 Prometheus 实例进入管理页面。
2. 通过集成容器服务列表单击**集群 ID** 进入到容器服务集成管理页面。
3. 通过服务发现添加 `Pod Monitor` 来定义 Prometheus 抓取任务，YAML 配置示例如下：

<dx-codeblock>
:::  yaml
  apiVersion: monitoring.coreos.com/v1
  kind: PodMonitor
  metadata:
    name: postgres-exporter
    namespace: cm-prometheus
  spec:
    namespaceSelector:
      matchNames:
      - postgres-test
    podMetricsEndpoints:
    - interval: 30s
      path: /metrics
      port: http-metrics # 前面 Exporter 那个 Container 的端口名
      relabelings:
      - action: labeldrop
        regex: __meta_kubernetes_pod_label_(pod_|statefulset_|deployment_|controller_)(.+)
      - action: replace
        regex: (.*)
        replacement: postgres-xxxxxx
        sourceLabels:
        - instance
        targetLabel: instance
    selector:
      matchLabels:
        app: postgres
:::
</dx-codeblock>

>?更多高阶用法请参见 [ServiceMonitor](https://github.com/prometheus-operator/prometheus-operator/blob/master/Documentation/api.md#servicemonitor) 和 [PodMonitor](https://github.com/prometheus-operator/prometheus-operator/blob/master/Documentation/api.md#podmonitor)。

### Grafana 大屏可视化

> ?需要使用上述 [获取指标](#step3) 配置来获取 Postgres 实例的启动时间。

1. 在 [Prometheus 实例](https://console.cloud.tencent.com/monitor/prometheus) 列表，找到对应的  Prometheus 实例，单击 实例ID 右侧<img src="https://main.qcloudimg.com/raw/978c842f0c093a31df8d5240dd01016d.png" width="2%">图标，打开您的专属 Grafana，输入您的账号密码，即可进行 Grafana 可视化大屏操作区。
2. 进入 Grafana，单击<img src="https://main.qcloudimg.com/raw/7e3fff6131aa085987552a9725e9ae54.png" width="2%">图表，展开监控面板，单击对应的监控图表名称即可查看监控数据。
![示例](https://main.qcloudimg.com/raw/91715279d22a1f6efe1844e318712391.png)

### 告警以及接入

1. 登录 [Prometheus 监控服务控制台](https://console.cloud.tencent.com/monitor/prometheus)，选择对应 Prometheus 实例进入管理页面。
2. 单击告警策略，可以添加相应的告警策略，详情请参见 [新建告警策略](https://cloud.tencent.com/document/product/1416/56009)。
> ?后续 Prometheus 监控服务将提供更多 PostgreSQL 相关的告警模板。
