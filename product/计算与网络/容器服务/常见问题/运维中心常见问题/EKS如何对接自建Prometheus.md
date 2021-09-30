



## EKS 如何对接腾讯云原生 Prometheus 监控？

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2/prometheus/list?rid=8)，选择左侧导航中的**云原生监控**。
2. 创建监控实例，操作详情请参见 [监控实例管理](https://cloud.tencent.com/document/product/457/49889#.E5.88.9B.E5.BB.BA.E7.9B.91.E6.8E.A7.E5.AE.9E.E4.BE.8B)。
3. 完成创建后，在“云原生监控”列表页中单击监控实例名称进入监控实例详情页。
4. 在监控实例详情页，选择“关联集群”页签。
5. 单击**关联集群**。如下图所示：
![](https://main.qcloudimg.com/raw/cb00ca575ec1af802e7384bf66802e60.png)
 - **集群类型**：选择“弹性集群”。
 - **集群**：勾选当前 VPC 下需要关联的集群。
6. 单击**确定**完成关联集群。
7. 在“关联集群”页签中，单击集群 ID 右侧的**数据采集配置**，完成数据采集规则配置。操作详情请参见 [数据采集配置](https://cloud.tencent.com/document/product/457/49891#.E9.85.8D.E7.BD.AE.E6.95.B0.E6.8D.AE.E9.87.87.E9.9B.86)。
8. 在“基本信息”页签中，查看 Grafana 信息。登录指定的 Grafana 地址并输入账号密码即可查看监控数据。




## EKS 如何对接自建 Prometheus？
**前提条件**
- 已创建 Prometheus。
- 已安装 Prometheus Operator。
- 已配置 Grafana。

在 EKS 集群中，需要获取以下监控指标：

| 指标类型         | 采集源                | 发现类型            |
| ---------------- | --------------------- | ------------------- |
| k8s资源指标      | kube-state-metrics    | 通过coredns 访问域名 |
| 容器运行时指标   | pod的metrics接口      | k8s_sd pod 级别      |



#### 监控 k8s 资源指标
若您希望监控 k8s 的资源指标，可以通过在 EKS 集群内部署 kube-state-metrics 组件及编写 ServiceMonitor 实现。
<dx-accordion>
::: 在\sEKS\s集群内部署\skube-state-metrics\s组件
如果您在 EKS 的集群内已经部署了 Prometheus Operator 会发现对应的 kube-state-metrics 组件和node exportor的Pod是pending状态，这是因为它们并不适用于EKS集群的场景，node exportor在EKS集群的监控中不需要使用，可以直接删除该pod，同时我们需要重新部署kube-state-metrics组件，具体的部署内容如下所示：

- kube-state-metrics-ClusterRole
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
   labels:
     app.kubernetes.io/name: kube-state-metrics
     app.kubernetes.io/version: 1.9.7
   name: tke-kube-state-metrics
 rules:
   - apiGroups:
       - ""
     resources:
       - configmaps
       - secrets
       - nodes
       - pods
       - services
       - resourcequotas
       - replicationcontrollers
       - limitranges
       - persistentvolumeclaims
       - persistentvolumes
       - namespaces
       - endpoints
     verbs:
       - list
       - watch
   - apiGroups:
       - extensions
     resources:
       - daemonsets
       - deployments
       - replicasets
       - ingresses
     verbs:
       - list
       - watch
   - apiGroups:
       - apps
     resources:
       - statefulsets
       - daemonsets
       - deployments
       - replicasets
     verbs:
       - list
       - watch
   - apiGroups:
       - batch
     resources:
       - cronjobs
       - jobs
     verbs:
       - list
       - watch
   - apiGroups:
       - autoscaling
     resources:
       - horizontalpodautoscalers
     verbs:
       - list
       - watch
   - apiGroups:
       - authentication.k8s.io
     resources:
       - tokenreviews
     verbs:
       - create
   - apiGroups:
       - authorization.k8s.io
     resources:
       - subjectaccessreviews
     verbs:
       - create
   - apiGroups:
       - policy
     resources:
       - poddisruptionbudgets
     verbs:
       - list
       - watch
   - apiGroups:
       - certificates.k8s.io
     resources:
       - certificatesigningrequests
     verbs:
       - list
       - watch
   - apiGroups:
       - storage.k8s.io
     resources:
       - storageclasses
       - volumeattachments
     verbs:
       - list
       - watch
   - apiGroups:
       - admissionregistration.k8s.io
     resources:
       - mutatingwebhookconfigurations
       - validatingwebhookconfigurations
     verbs:
       - list
       - watch
   - apiGroups:
       - networking.k8s.io
     resources:
       - networkpolicies
     verbs:
       - list
       - watch
   - apiGroups:
       - coordination.k8s.io
     resources:
       - leases
     verbs:
       - list
       - watch
```

- kube-state-metrics-service-ClusterRoleBinding
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
   labels:
     app.kubernetes.io/name: kube-state-metrics
     app.kubernetes.io/version: 1.9.7
   name: tke-kube-state-metrics
roleRef:
   apiGroup: rbac.authorization.k8s.io
   kind: ClusterRole
   name: tke-kube-state-metrics
subjects:
   - kind: ServiceAccount
     name: tke-kube-state-metrics
     namespace: kube-system
```

- kube-state-metrics-deployment
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
   labels:
     app.kubernetes.io/name: kube-state-metrics
     app.kubernetes.io/version: 1.9.7
   name: tke-kube-state-metrics
   namespace: kube-system
 spec:
   replicas: 1
   selector:
     matchLabels:
       app.kubernetes.io/name: kube-state-metrics
   template:
     metadata:
       labels:
         app.kubernetes.io/name: kube-state-metrics
         app.kubernetes.io/version: 1.9.7
     spec:
       containers:
         - image: ccr.ccs.tencentyun.com/tkeimages/kube-state-metrics:v1.9.7
           livenessProbe:
             httpGet:
               path: /healthz
               port: 8080
             initialDelaySeconds: 5
             timeoutSeconds: 5
           name: kube-state-metrics
           ports:
             - containerPort: 8080
               name: http-metrics
             - containerPort: 8081
               name: telemetry
           readinessProbe:
             httpGet:
               path: /
               port: 8081
             initialDelaySeconds: 5
             timeoutSeconds: 5
           securityContext:
             runAsUser: 65534
       serviceAccountName: tke-kube-state-metrics
```

- kube-state-metrics-service
```yaml
apiVersion: v1
kind: Service
metadata:
   labels:
     app.kubernetes.io/name: kube-state-metrics
     app.kubernetes.io/version: 1.9.7
   name: tke-kube-state-metrics
   namespace: kube-system
 spec:
   clusterIP: None
   ports:
     - name: http-metrics
       port: 8180
       targetPort: http-metrics
     - name: telemetry
       port: 8181
       targetPort: telemetry
   selector:
     app.kubernetes.io/name: kube-state-metrics
```


- kube-state-metrics-serviceaccount
```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
   labels:
     app.kubernetes.io/name: kube-state-metrics
     app.kubernetes.io/version: 1.9.7
   name: tke-kube-state-metrics
   namespace: kube-system
```
:::
::: 在\sEKS\s集群内部署\sServiceMonitor
ServiceMonitor 可以定义如何监控一组动态服务，部署 kube-state-metrics-servicemonitor 后，Prometheus 可以通过 kube-state-metrics 来收集 k8s 的资源指标。具体的部署内容如下所示：

- kube-state-metrics-servicemonitor
```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
   labels:
     app.kubernetes.io/name: kube-state-metrics
     app.kubernetes.io/version: 1.9.7
   name: kube-state-metrics
   namespace: kube-system
spec:
   endpoints:
     - interval: 15s
       port: http-metrics
       scrapeTimeout: 15s
       honorLabels: true
   jobLabel: app.kubernetes.io/name
   selector:
     matchLabels:
       app.kubernetes.io/name: kube-state-metrics
```

:::
</dx-accordion>










#### 监控容器运行时指标

EKS 中的 Pod 通过暴露9100端口向外提供监控数据，您可以通过访问 podip：9100/metrics 获取监控数据指标。相较于容器服务 TKE 标准的监控配置，监控 EKS 需要修改相应的配置文件，建议使用 Operator 的 [additional scrape config ](https://github.com/prometheus-operator/prometheus-operator/blob/master/Documentation/additional-scrape-config.md) 配置。此外，您也可以通过在 Pod 中添加 annotation 的方式对指定的 Pod 进行监控。

<dx-accordion>
::: 通过配置\sOperator\s的\sadditional\sscrape\sconfig\s获取监控数据指标
若您希望通过访问 podip：9100/metrics 获取监控数据指标，可执行以下步骤：

1. 新建 prometheus-additional.yaml 文件。
2. 在文件中添加 scrape_configs。scrape_configs 内容如下所示：
```yaml
- job_name: eks-info
  honor_timestamps: true
  metrics_path: /metrics
  scheme: http
  kubernetes_sd_configs:
  - role: pod
  bearer_token_file: /var/run/secrets/kubernetes.io/serviceaccount/token
  tls_config:
    insecure_skip_verify: true
  relabel_configs:
  - source_labels: [__meta_kubernetes_pod_ip]
    separator: ;
    regex: (.*)
    target_label: __address__
    replacement: ${1}:9100
    action: replace
  - source_labels: [__meta_kubernetes_pod_name]
    separator: ;
    regex: (.*)
    target_label: pod_name
    replacement: ${1}
    action: replace
  metric_relabel_configs:
  - source_labels: [__name__]
    separator: ;
    regex: node_network_receive_packets_total
    target_label: __name__
    replacement: container_network_receive_packets_total
    action: replace
  - source_labels: [__name__]
    separator: ;
    regex: node_network_receive_bytes_total
    target_label: __name__
    replacement: container_network_receive_bytes_total
    action: replace
  - source_labels: [__name__]
    separator: ;
    regex: node_network_transmit_bytes_total
    target_label: __name__
    replacement: container_network_transmit_bytes_total
    action: replace
  - source_labels: [__name__]
    separator: ;
    regex: node_network_transmit_packets_total
    target_label: __name__
    replacement: container_network_transmit_packets_total
    action: replace
  - source_labels: [pod_name]
    separator: ;
    regex: (.*)
    target_label: pod
    replacement: $1
    action: replace
  - source_labels: [__name__]
    separator: ;
    regex: (container_network.*|pod_.*)
    replacement: $1
    action: keep
  - separator: ;
    regex: pod_name|node|unInstanceId|workload_kind|workload_name
    replacement: $1
    action: labeldrop
```
3. 完成部署后，连接 Grafana 获取相应数据。

:::
::: 通过在\sPod\s中添加\sannotation\s对指定\sPod\s进行监控
若您希望通过在 Pod 中添加 annotation 的方式对指定的 Pod 进行监控，可执行以下步骤：
1. 修改需要进行采集的 Pod 的 yaml 文件，在 spec.template.metadata.annotations 中配置以下内容：
```yaml
prometheus.io/scrape: 'true'
prometheus.io/port: '9100'
prometheus.io/path: 'metrics'
```
2. 配置 scrape_configs。配置 scrape_configs 后，prometheus 会对所有配置过采集信息为 true 的 Pod 进行监控。scrape_configs 请参考以下配置：
```yaml
scrape_configs:
- job_name: kubernetes-pods
  honor_timestamps: true
  metrics_path: /metrics
  scheme: http
  kubernetes_sd_configs:
  - role: pod
  relabel_configs:
  - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
    separator: ;
    regex: "true"
    replacement: $1
    action: keep
  - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
    separator: ;
    regex: (.+)
    target_label: __metrics_path__
    replacement: $1
    action: replace
  - source_labels: [__address__, __meta_kubernetes_pod_annotation_prometheus_io_port]
    separator: ;
    regex: ([^:]+)(?::\d+)?;(\d+)
    target_label: __address__
    replacement: $1:$2
    action: replace
  - separator: ;
    regex: __meta_kubernetes_pod_label_(.+)
    replacement: $1
    action: labelmap
  - source_labels: [__meta_kubernetes_namespace]
    separator: ;
    regex: (.*)
    target_label: kubernetes_namespace
    replacement: $1
    action: replace
  - source_labels: [__meta_kubernetes_pod_name]
    separator: ;
    regex: (.*)
    target_label: kubernetes_pod_name
    replacement: $1
    action: replace
```
:::
</dx-accordion>












## 自建 Prometheus 如何迁移到腾讯云原生监控服务?
若您需要将自建的 Prometheus 迁移至腾讯云原生监控服务，可参见 [自建 Prometheus 迁移到云原生监控](https://cloud.tencent.com/document/product/457/51684)。



