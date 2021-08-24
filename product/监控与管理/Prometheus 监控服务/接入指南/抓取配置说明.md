## 概述
Prometheus 主要通过 Pull 的方式来抓取目标服务暴露出来的监控接口，因此需要配置对应的抓取任务来请求监控数据并写入到 Prometheus 提供的存储中，目前 Prometheus 服务提供了如下几个任务的配置：
- 原生 Job 配置：提供 Prometheus 原生抓取 Job 的配置。
- Pod Monitor：在 K8S 生态下，基于 Prometheus Operator 来抓取 Pod 上对应的监控数据。
- Service Monitor：在 K8S 生态下，基于 Prometheus Operator 来抓取 Service 对应 Endpoints 上的监控数据。

>? `[]` 中的配置项为可选。

## 原生 Job 配置

相应配置项说明如下：

```yaml

# 抓取任务名称，同时会在对应抓取的指标中加了一个 label(job=job_name)
job_name: <job_name>

# 抓取任务时间间隔
[ scrape_interval: <duration> | default = <global_config.scrape_interval> ]

# 抓取请求超时时间
[ scrape_timeout: <duration> | default = <global_config.scrape_timeout> ]

# 抓取任务请求 URI 路径
[ metrics_path: <path> | default = /metrics ]

# 解决当抓取的 label 与后端 Prometheus 添加 label 冲突时的处理。
# true: 保留抓取到的 label，忽略与后端 Prometheus 冲突的 label；
# false: 对冲突的 label，把抓取的 label 前加上 exported_<original-label>，添加后端 Prometheus 增加的 label；
[ honor_labels: <boolean> | default = false ]

# 是否使用抓取到 target 上产生的时间。
# true: 如果 target 中有时间，使用 target 上的时间；
# false: 直接忽略 target 上的时间；
[ honor_timestamps: <boolean> | default = true ]

# 抓取协议: http 或者 https
[ scheme: <scheme> | default = http ]

# 抓取请求对应 URL 参数
params:
  [ <string>: [<string>, ...] ]

# 通过 basic auth 设置抓取请求头中 `Authorization` 的值，password/password_file 互斥，优先取 password_file 里面的值。 
basic_auth:
  [ username: <string> ]
  [ password: <secret> ]
  [ password_file: <string> ]

# 通过 bearer token 设置抓取请求头中 `Authorization` bearer_token/bearer_token_file 互斥，优先取 bearer_token 里面的值。 
[ bearer_token: <secret> ]

# 通过 bearer token 设置抓取请求头中 `Authorization` bearer_token/bearer_token_file 互斥，优先取 bearer_token 里面的值。 
[ bearer_token_file: <filename> ]

# 抓取连接是否通过 TLS 安全通道，配置对应的 TLS 参数
tls_config:
  [ <tls_config> ]

# 通过代理服务来抓取 target 上的指标，填写对应的代理服务地址。
[ proxy_url: <string> ]

# 通过静态配置来指定 target，详见下面的说明。
static_configs:
  [ - <static_config> ... ]

# CVM 服务发现配置，详见下面的说明。
cvm_sd_configs:
  [ - <cvm_sd_config> ... ]

# 在抓取数据之后，把 target 上对应的 label 通过 relabel 的机制进行改写，按顺序执行多个 relabel 规则。
# relabel_config 详见下面说明。
relabel_configs:
  [ - <relabel_config> ... ]

# 数据抓取完成写入之前，通过 relabel 机制进行改写 label 对应的值，按顺序执行多个 relabel 规则。
# relabel_config 详见下面说明。
metric_relabel_configs:
  [ - <relabel_config> ... ]

# 一次抓取数据点限制，0：不作限制，默认为 0
[ sample_limit: <int> | default = 0 ]

# 一次抓取 Target 限制，0：不作限制，默认为 0
[ target_limit: <int> | default = 0 ]

```

### static_config 配置

相应配置项说明如下：

<dx-codeblock>
:::  yaml
# 指定对应 target host 的值，如ip:port。
targets:
  [ - '<host>' ]

# 在所有 target 上加上对应的 label，类似全局 label 的概念。
labels:
  [ <labelname>: <labelvalue> ... ]
:::
</dx-codeblock>


### cvm_sd_config 配置
CVM 服务发现利用腾讯云 API 自动获取 CVM 实例列表，默认使用 CVM 的私网 IP。服务发现产生以下元标签，这些标签可以在 relabel 配置中使用。

| 标签                | 说明 |
| ------------------- | --------- |
| \_\_meta\_cvm\_instance\_id | 实例 ID |
| \_\_meta\_cvm\_instance\_name | 实例名 |
| \_\_meta\_cvm\_instance\_state | 实例状态 |
| \_\_meta\_cvm\_instance\_type | 实例机型 |
| \_\_meta\_cvm\_OS | 实例操作系统 |
| \_\_meta\_cvm\_private\_ip | 私网 IP |
| \_\_meta\_cvm\_public\_ip | 公网 IP |
| \_\_meta\_cvm\_vpc\_id | 网络 ID |
| \_\_meta\_cvm_subnet_id | 子网 ID |
| \_\_meta\_cvm\_tag\_&lt;tagkey&gt; | 实例标签值 |
| \_\_meta\_cvm\_region | 实例所在区域 |
| \_\_meta\_cvm\_zone | 实例的可用区 |

CVM 服务发现配置说明：

<dx-codeblock>
:::  yaml
# 腾讯云的地域，地域列表见文档 https://cloud.tencent.com/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8。
region: <string> 

# 自定义 endpoint。
[ endpoint: <string> ]

# 访问腾讯云 API 的的凭证信息。如果不设置，取环境变量 TENCENT_CLOUD_SECRET_ID 和 TENCENT_CLOUD_SECRET_KEY 的值。
[ secret_id: <string> ]
[ secret_key: <secret> ]

# CVM 列表的刷新周期。
[ refresh_interval: <duration> | default = 60s ]

# 抓取 metrics 的端口。
ports: 
  - [ <int> | default = 80 ]

# CVM 列表的过滤规则。支持的过滤条件见文档 https://cloud.tencent.com/document/api/213/15728#2.-.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0。
filters:
  [ - name: <string>
      values: <string>, [...] ]
:::
</dx-codeblock>

#### 例子

##### 静态配置

<dx-codeblock>
:::  yaml
job_name: prometheus
scrape_interval: 30s
static_configs:
- targets:
  - 127.0.0.1:9090
  :::
  </dx-codeblock>


##### CVM 服务发现配置

<dx-codeblock>
:::  yaml
job_name: demo-monitor
cvm_sd_configs:
- region: ap-guangzhou
  ports:
  - 8080
  filters:         
  - name: tag:service
    values: 
    - demo
relabel_configs: 
- source_labels: [__meta_cvm_instance_state]
  regex: RUNNING
  action: keep
- regex: __meta_cvm_tag_(.*)
  replacement: $1
  action: labelmap
- source_labels: [__meta_cvm_region]
  target_label: region
  action: replace
	:::
  </dx-codeblock>

## Pod Monitor

相应配置项说明如下：

<dx-codeblock>
:::  yaml
# Prometheus Operator CRD 版本
apiVersion: monitoring.coreos.com/v1
# 对应 K8S 的资源类型，这里面 Pod Monitor
kind: PodMonitor
# 对应 K8S 的 Metadata，这里只用关心 name，如果没有指定 jobLabel，对应抓取指标 label 中 job 的值为 <namespace>/<name>
metadata:
  name: redis-exporter # 填写一个唯一名称
  namespace: cm-prometheus  # namespace固定，不需要修改
# 描述抓取目标 Pod 的选取及抓取任务的配置
spec:
  # 填写对应 Pod 的 label，pod monitor 会取对应的值作为 job label 的值。
  # 如果查看的是 Pod Yaml，取 pod.metadata.labels 中的值。
  # 如果查看的是 Deployment/Daemonset/Statefulset，取 spec.template.metadata.labels。
  [ jobLabel: string ]
  # 把对应 Pod 上的 Label 添加到 Target 的 Label 中
  [ podTargetLabels: []string ]
  # 一次抓取数据点限制，0：不作限制，默认为 0
  [ sampleLimit: uint64 ]
  # 一次抓取 Target 限制，0：不作限制，默认为 0
  [ targetLimit: uint64 ]
  # 配置需要抓取暴露的 Prometheus HTTP 接口，可以配置多个 Endpoint
  podMetricsEndpoints:
  [ - <endpoint_config> ... ] # 详见下面 endpoint 说明
  # 选择要监控 Pod 所在的 namespace，不填为选取所有 namespace
  [ namespaceSelector: ]  
    # 是否选取所有 namespace
    [ any: bool ]
    # 需要选取 namespace 列表
    [ matchNames: []string ]
  # 填写要监控 Pod 的 Label 值，以定位目标 Pod  [K8S metav1.LabelSelector](https://v1-17.docs.kubernetes.io/docs/reference/generated/kubernetes-api/v1.17/#labelselector-v1-meta)
  selector:  
    [ matchExpressions: array ]
      [ example: - {key: tier, operator: In, values: [cache]} ]
    [ matchLabels: object ]
      [ example: k8s-app: redis-exporter ]
	:::
</dx-codeblock>

#### 例子

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

## Service Monitor

相应配置项说明如下：

<dx-codeblock>
:::  yaml

# Prometheus Operator CRD 版本
apiVersion: monitoring.coreos.com/v1
# 对应 K8S 的资源类型，这里面 Service Monitor
kind: ServiceMonitor
# 对应 K8S 的 Metadata，这里只用关心 name，如果没有指定 jobLabel，对应抓取指标 label 中 job 的值为 Service 的名称。
metadata:
  name: redis-exporter # 填写一个唯一名称
  namespace: cm-prometheus  # namespace固定，不需要修改
# 描述抓取目标 Pod 的选取及抓取任务的配置
spec:
  # 填写对应 Pod 的 label(metadata/labels)，service monitor 会取对应的值作为 job label 的值
  [ jobLabel: string ]
  # 把对应 service 上的 Label 添加到 Target 的 Label 中
  [ targetLabels: []string ]
  # 把对应 Pod 上的 Label 添加到 Target 的 Label 中
  [ podTargetLabels: []string ]
  # 一次抓取数据点限制，0：不作限制，默认为 0
  [ sampleLimit: uint64 ]
  # 一次抓取 Target 限制，0：不作限制，默认为 0
  [ targetLimit: uint64 ]
  # 配置需要抓取暴露的 Prometheus HTTP 接口，可以配置多个 Endpoint
  endpoints:
  [ - <endpoint_config> ... ] # 详见下面 endpoint 说明
  # 选择要监控 Pod 所在的 namespace，不填为选取所有 namespace
  [ namespaceSelector: ]  
    # 是否选取所有 namespace
    [ any: bool ]
    # 需要选取 namespace 列表
    [ matchNames: []string ]
  # 填写要监控 Pod 的 Label 值，以定位目标 Pod  [K8S metav1.LabelSelector](https://v1-17.docs.kubernetes.io/docs/reference/generated/kubernetes-api/v1.17/#labelselector-v1-meta)
  selector:  
    [ matchExpressions: array ]
      [ example: - {key: tier, operator: In, values: [cache]} ]
    [ matchLabels: object ]
      [ example: k8s-app: redis-exporter ]
	:::
</dx-codeblock>

#### 例子

<dx-codeblock>
:::  yaml
  apiVersion: monitoring.coreos.com/v1
  kind: ServiceMonitor
  metadata:
    name: go-demo    # 填写一个唯一名称
    namespace: cm-prometheus  # namespace固定，不要修改
  spec:
    endpoints:
    - interval: 30s
      # 填写service yaml中Prometheus Exporter对应的Port的Name
      port: 8080-8080-tcp
      # 填写Prometheus Exporter对应的Path的值，不填默认/metrics
      path: /metrics
      relabelings:
      # ** 必须要有一个 label 为 application，这里假设 k8s 有一个 label 为 app，
      # 我们通过 relabel 的 replace 动作把它替换成了 application
      - action: replace
        sourceLabels:  [__meta_kubernetes_pod_label_app]
        targetLabel: application
    # 选择要监控service所在的namespace
    namespaceSelector:
      matchNames:
      - golang-demo
    # 填写要监控service的Label值，以定位目标service
    selector:
      matchLabels:
        app: golang-app-demo
	:::
</dx-codeblock>

## endpoint_config 配置

相应配置项说明如下：

<dx-codeblock>
:::  yaml
# 对应 port 的名称，这里需要注意不是对应的端口，默认：80，对应的取值如下：
# ServiceMonitor: 对应 Service>spec/ports/name;
# PodMonitor: 说明如下：
#   如果查看的是 Pod Yaml，取 pod.spec.containers.ports.name 中的值。
#   如果查看的是 Deployment/Daemonset/Statefulset，取 spec.template.spec.containers.ports.name。
[ port: string | default = 80]
# 抓取任务请求 URI 路径
[ path: string | default = /metrics ]
# 抓取协议: http 或者 https
[ scheme: string | default = http]
# 抓取请求对应 URL 参数
[ params: map[string][]string]
# 抓取任务间隔的时间
[ interval: string | default = 30s ]
# 抓取任务超时
[ scrapeTimeout: string | default = 30s]
# 抓取连接是否通过 TLS 安全通道，配置对应的 TLS 参数
[ tlsConfig: TLSConfig ]
# 通过对应的文件读取 bearer token 对应的值，放到抓取任务的 header 中
[ bearerTokenFile: string ]
# 通过对应的 K8S secret key 读取对应的 bearer token，注意 secret namespace 需要和 PodMonitor/ServiceMonitor 相同
[ bearerTokenSecret: string ]
# 解决当抓取的 label 与后端 Prometheus 添加 label 冲突时的处理。
# true: 保留抓取到的 label，忽略与后端 Prometheus 冲突的 label；
# false: 对冲突的 label，把抓取的 label 前加上 exported_<original-label>，添加后端 Prometheus 增加的 label；
[ honorLabels: bool | default = false ]
# 是否使用抓取到 target 上产生的时间。
# true: 如果 target 中有时间，使用 target 上的时间；
# false: 直接忽略 target 上的时间；
[ honorTimestamps: bool | default = true ]
# basic auth 的认证信息，username/password 填写对应 K8S secret key 的值，注意 secret namespace 需要和 PodMonitor/ServiceMonitor 相同。
[ basicAuth: BasicAuth ]
# 通过代理服务来抓取 target 上的指标，填写对应的代理服务地址。
[ proxyUrl: string ]
# 在抓取数据之后，把 target 上对应的 label 通过 relabel 的机制进行改写，按顺序执行多个 relabel 规则。
# relabel_config 详见下面说明。
relabelings:
[ - <relabel_config> ...]
# 数据抓取完成写入之前，通过 relabel 机制进行改写 label 对应的值，按顺序执行多个 relabel 规则。
# relabel_config 详见下面说明。
metricRelabelings: 
[ - <relabel_config> ...]
	:::
</dx-codeblock>

## relabel_config 配置

相应配置项说明如下：

<dx-codeblock>
:::  yaml

# 从原始 labels 中取哪些 label 的值进行 relabel，取出来的值通过 separator 中的定义进行字符拼接。
# 如果是 PodMonitor/ServiceMonitor 对应的配置项为 sourceLabels 。
[ source_labels: '[' <labelname> [, ...] ']' ]
# 定义需要 relabel 的 label 值拼接的字符，默认为 ';'。 
[ separator: <string> | default = ; ]

# action 为 replace/hashmod 时，通过 target_label 来指定对应 label name。
# 如果是 PodMonitor/ServiceMonitor 对应的配置项为 targetLabel 。
[ target_label: <labelname> ]

# 需要对 source labels 对应值进行正则匹配的表达式。
[ regex: <regex> | default = (.*) ]

# action 为 hashmod 时用到，根据 source label 对应值 md5 取模值。
[ modulus: <int> ]

# action 为 replace 的时候，通过 replacement 来定义当 regex 匹配之后需要替换的表达式，可以结合 regex 正规则表达式替换。
[ replacement: <string> | default = $1 ]

# 基于 regex 匹配到的值进行相关的操作，对应的 action 如下，默认为 replace：
# replace: 如果 regex 匹配到，通过 replacement 中定义的值替换相应的值，并通过 target_label 设值并添加相应的 label 
# keep: 如果 regex 没有匹配到，丢弃
# drop: 如果 regex 匹配到，丢弃
# hashmod: 通过 moduels 指定的值把 source label 对应的 md5 值取模，添加一个新的 label，label name 通过 target_label 指定
# labelmap: 如果 regex 匹配到，使用 replacement 替换对就的 label name
# labeldrop: 如果 regex 匹配到，删除对应的 label
# labelkeep: 如果 regex 没有匹配到，删除对应的 label
[ action: <relabel_action> | default = replace ]
	:::
</dx-codeblock>
