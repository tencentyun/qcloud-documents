

本文主要描述使用自建 Prometheus 采集腾讯云容器服务 TKE 的监控数据时如何配置采集规则。TKE 集群内按照节点类型分为常规节点和超级节点，Prometheus 通过配置 `scrape_config` 来抓取节点和容器的监控数据，由于节点性质不同因此需要配置的采集规则略有差异。

## 常规节点采集规则

常规节点的采集配置文件如下所示：

```yaml
    - job_name: "tke-cadvisor"
      scheme: https
      metrics_path: /metrics/cadvisor # 采集容器 cadvisor 监控数据
      tls_config:
        insecure_skip_verify: true # tke 的 kubelet 使用自签证书，忽略证书校验
      authorization:
        credentials_file: /var/run/secrets/kubernetes.io/serviceaccount/token
      kubernetes_sd_configs:
      - role: node
      relabel_configs:
      - source_labels: [__meta_kubernetes_node_label_node_kubernetes_io_instance_type]
        regex: eklet # 排除超级节点
        action: drop
      - action: labelmap
        regex: __meta_kubernetes_node_label_(.+)
    - job_name: "tke-kubelet"
      scheme: https
      metrics_path: /metrics # 采集 kubelet 自身的监控数据
      tls_config:
        insecure_skip_verify: true
      authorization:
        credentials_file: /var/run/secrets/kubernetes.io/serviceaccount/token
      kubernetes_sd_configs:
      - role: node
      relabel_configs:
      - source_labels: [__meta_kubernetes_node_label_node_kubernetes_io_instance_type]
        regex: eklet
        action: drop
      - action: labelmap
        regex: __meta_kubernetes_node_label_(.+)
    - job_name: "tke-probes" # 采集容器健康检查健康数据
      scheme: https
      metrics_path: /metrics/probes
      tls_config:
        insecure_skip_verify: true
      authorization:
        credentials_file: /var/run/secrets/kubernetes.io/serviceaccount/token
      kubernetes_sd_configs:
      - role: node
      relabel_configs:
      - source_labels: [__meta_kubernetes_node_label_node_kubernetes_io_instance_type]
        regex: eklet
        action: drop
      - action: labelmap
        regex: __meta_kubernetes_node_label_(.+)
```

**使用说明：**
- 使用节点服务发现（`kubernetes_sd_configs` 的 role 为 `node`），抓取所有节点 `kubelet:10250` 暴露的几种监控数据。
- 如果集群是普通节点与超级节点混用，排除超级节点（`relabel_configs` 中将带 `node.kubernetes.io/instance-type: eklet` 这种 label 的 node 排除）。
- TKE 节点上的 kubelet 证书是自签的，需要忽略证书校验，所以 `insecure_skip_verify` 要置为 true。
- kubelet 通过 `/metrics/cadvisor`, `/metrics` 与 `/metrics/probes` 路径分别暴露了容器 cadvisor 监控数据、kubelet 自身监控数据以及容器健康检查健康数据，为这三个不同路径分别配置采集 job 进行采集。

## 超级节点采集规则

超级节点的采集配置文件如下所示：

```yaml
    - job_name: TKE Serverless # 采集超级节点监控数据
      honor_timestamps: true
      metrics_path: '/metrics' # 所有健康数据都在这个路径
      params: # 通常需要加参数过滤掉 ipvs 相关的指标，因为可能数据量较大，打高 Pod 负载。
        collect[]:
        - 'ipvs'
        # - 'cpu'
        # - 'meminfo'
        # - 'diskstats'
        # - 'filesystem'
        # - 'load0vg'
        # - 'netdev'
        # - 'filefd'
        # - 'pressure'
        # - 'vmstat'
      scheme: http
      kubernetes_sd_configs:
      - role: pod # 超级节点 Pod 的监控数据暴露在 Pod 自身 IP 的 9100 端口，所以使用 Pod 服务发现
      relabel_configs:
      - source_labels: [__meta_kubernetes_pod_annotation_tke_cloud_tencent_com_pod_type]
        regex: eklet # 只采集超级节点的 Pod
        action: keep
      - source_labels: [__meta_kubernetes_pod_phase]
        regex: Running # 非 Running 状态的 Pod 机器资源已释放，不需要采集
        action: keep
      - source_labels: [__meta_kubernetes_pod_ip]
        separator: ;
        regex: (.*)
        target_label: __address__
        replacement: ${1}:9100 # 监控指标暴露在 Pod 的 9100 端口
        action: replace
      - source_labels: [__meta_kubernetes_pod_name]
        separator: ;
        regex: (.*)
        target_label: pod # 将 Pod 名字写到 "pod" label
        replacement: ${1}
        action: replace
      - source_labels: [__meta_kubernetes_namespace]
        separator: ;
        regex: (.*)
        target_label: namespace # 将 Pod 所在 namespace 写到 "namespace" label
        replacement: ${1}
        action: replace
      metric_relabel_configs:
      - source_labels: [__name__]
        separator: ;
        regex: (container_.*|pod_.*|kubelet_.*)
        replacement: $1
        action: keep
```

**使用说明：**
- 超级节点的监控数据暴露在每个 Pod 的9100端口的 `/metrics` 这个 HTTP API 路径（非 HTTPS），使用 Pod 服务发现（`kubernetes_sd_configs` 的 role 为 `pod`），用一个 job 就可以采集完。
- 超级节点的 Pod 支持通过 `collect[]` 这个查询参数来过滤掉不希望采集的指标，这样可以避免指标数据量过大，导致 Pod 负载升高，通常要过滤掉 `ipvs` 的指标。
- 如果集群是普通节点与超级节点混用，确保只采集超级节点的 Pod（`relabel_configs` 中只保留有 `tke.cloud.tencent.com/pod-type:eklet` 这个注解的 Pod）。
- 如果 Pod 的 phase 不是 Running 也无法采集，可以排除。
- `container_` 开头的指标是 cadvisor 监控数据，`pod_` 前缀指标是超级节点 Pod 所在子机的监控数据（相当于将 `node_exporter` 的 `node_` 前缀指标替换成了 `pod_`），`kubelet_` 前缀指标是超级节点 Pod 子机内兼容 kubelet 的指标（主要是 pvc 存储监控）。

## kube-prometheus-stack 配置

通常使用 [kube-prometheus-stack](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack) 这个 helm chart 来自建 Prometheus，在 `values.yaml` 中进行自定义配置然后安装到集群，其中可以配置 Prometheus 原生的 `scrape_config`（非 CRD），配置方法是将自定义的 `scrape_config` 写到 `prometheus.prometheusSpec.additionalScrapeConfigs` 字段下，示例如下：

```yaml
prometheus:
  prometheusSpec:
    additionalScrapeConfigs:
    - job_name: "tke-cadvisor"
      scheme: https
      metrics_path: /metrics/cadvisor
      tls_config:
        insecure_skip_verify: true
      authorization:
        credentials_file: /var/run/secrets/kubernetes.io/serviceaccount/token
      kubernetes_sd_configs:
      - role: node
      relabel_configs:
      - source_labels: [__meta_kubernetes_node_label_node_kubernetes_io_instance_type]
        regex: eklet
        action: drop
      - action: labelmap
        regex: __meta_kubernetes_node_label_(.+)
    - job_name: "tke-kubelet"
      scheme: https
      metrics_path: /metrics
      tls_config:
        insecure_skip_verify: true
      authorization:
        credentials_file: /var/run/secrets/kubernetes.io/serviceaccount/token
      kubernetes_sd_configs:
      - role: node
      relabel_configs:
      - source_labels: [__meta_kubernetes_node_label_node_kubernetes_io_instance_type]
        regex: eklet
        action: drop
      - action: labelmap
        regex: __meta_kubernetes_node_label_(.+)
    - job_name: "tke-probes"
      scheme: https
      metrics_path: /metrics/probes
      tls_config:
        insecure_skip_verify: true
      authorization:
        credentials_file: /var/run/secrets/kubernetes.io/serviceaccount/token
      kubernetes_sd_configs:
      - role: node
      relabel_configs:
      - source_labels: [__meta_kubernetes_node_label_node_kubernetes_io_instance_type]
        regex: eklet
        action: drop
      - action: labelmap
        regex: __meta_kubernetes_node_label_(.+)
    - job_name: eks
      honor_timestamps: true
      metrics_path: '/metrics'
      params:
        collect[]: ['ipvs']
        # - 'cpu'
        # - 'meminfo'
        # - 'diskstats'
        # - 'filesystem'
        # - 'load0vg'
        # - 'netdev'
        # - 'filefd'
        # - 'pressure'
        # - 'vmstat'
      scheme: http
      kubernetes_sd_configs:
      - role: pod
      relabel_configs:
      - source_labels: [__meta_kubernetes_pod_annotation_tke_cloud_tencent_com_pod_type]
        regex: eklet
        action: keep
      - source_labels: [__meta_kubernetes_pod_phase]
        regex: Running
        action: keep
      - source_labels: [__meta_kubernetes_pod_ip]
        separator: ;
        regex: (.*)
        target_label: __address__
        replacement: ${1}:9100
        action: replace
      - source_labels: [__meta_kubernetes_pod_name]
        separator: ;
        regex: (.*)
        target_label: pod
        replacement: ${1}
        action: replace
      - source_labels: [__meta_kubernetes_namespace]
        separator: ;
        regex: (.*)
        target_label: namespace
        replacement: ${1}
        action: replace
      metric_relabel_configs:
      - source_labels: [__name__]
        separator: ;
        regex: (container_.*|pod_.*|kubelet_.*)
        replacement: $1
        action: keep
    storageSpec:
     volumeClaimTemplate:
       spec:
         accessModes: ["ReadWriteOnce"]
         resources:
           requests:
             storage: 100Gi
```
