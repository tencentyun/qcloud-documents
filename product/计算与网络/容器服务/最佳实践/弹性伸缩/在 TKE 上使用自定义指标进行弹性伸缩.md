## 操作场景

容器服务 TKE 基于 [Custom Metrics API](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/instrumentation/custom-metrics-api.md) 支持许多用于弹性伸缩的指标，涵盖 CPU、内存、硬盘、网络以及 GPU 相关的指标，覆盖绝大多数的 HPA 弹性伸缩场景，详细列表请参见 [自动伸缩指标说明](https://cloud.tencent.com/document/product/457/38929)。
针对例如基于业务单副本 QPS 大小来进行自动扩缩容等复杂场景，可通过安装 [prometheus-adapter](https://github.com/DirectXMan12/k8s-prometheus-adapter) 来实现自动扩缩容。而 Kubernetes 提供 [Custom Metrics API](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/instrumentation/custom-metrics-api.md) 与 [External Metrics API](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/instrumentation/external-metrics-api.md) 来对 HPA 指标进行扩展，让用户能够根据实际需求进行自定义。
prometheus-adapter 支持以上两种API，在实际环境中，使用 Custom Metrics API 即可满足大部分场景。本文将介绍如何通过 Custom Metrics API 实现使用自定义指标进行弹性伸缩。




## 前提条件

- 已创建1.12或以上版本的 TKE 集群，详情请参见 [创建集群](https://cloud.tencent.com/document/product/457/32189)。
- 已部署 Prometheus 并进行相应的自定义指标采集。
- 已安装 [Helm](https://helm.sh/docs/intro/install/)。

## 操作步骤


[](id:example)

### 暴露监控指标

本文以 Golang 业务程序为例，该示例程序暴露了 `httpserver_requests_total` 指标，并记录 HTTP 的请求，通过该指标可以计算出业务程序的 QPS 值。示例如下：
```go
package main

import (
		"github.com/prometheus/client_golang/prometheus"
		"github.com/prometheus/client_golang/prometheus/promhttp"
		"net/http"
		"strconv"
)

var (
HTTPRequests = prometheus.NewCounterVec(
		prometheus.CounterOpts{
			Name: "httpserver_requests_total",
			Help: "Number of the http requests received since the server started",
		},
		[]string{"status"},
	)
)

func init() {
	prometheus.MustRegister(HTTPRequests)
}

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		path := r.URL.Path
		code := 200
		switch path {
		case "/test":
			w.WriteHeader(200)
			w.Write([]byte("OK"))
		case "/metrics":
			promhttp.Handler().ServeHTTP(w, r)
		default:
			w.WriteHeader(404)
			w.Write([]byte("Not Found"))
		}
		HTTPRequests.WithLabelValues(strconv.Itoa(code)).Inc()
	})
	http.ListenAndServe(":80", nil)
}
```



### 部署业务程序

通过使用 Deployment 部署，将业务程序进行容器化并部署到 TKE 集群。示例如下：
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: httpserver
  namespace: httpserver
spec:
  replicas: 1
  selector:
    matchLabels:
      app: httpserver
  template:
    metadata:
      labels:
        app: httpserver
    spec:
      containers:
      - name: httpserver
        image: imroc.tencentcloudcr.com/test/httpserver:v1
        imagePullPolicy: Always

---

apiVersion: v1
kind: Service
metadata:
  name: httpserver
  namespace: httpserver
  labels:
    app: httpserver
  annotations:
    prometheus.io/scrape: "true"
    prometheus.io/path: "/metrics"
    prometheus.io/port: "http"
spec:
  type: ClusterIP
  ports:
  - port: 80
    protocol: TCP
    name: http
  selector:
    app: httpserver
```


### Prometheus 采集业务监控

您可以通过 [Promtheus 采集规则](#way1) 或 [ServiceMonitor](#way2) 配置 Promtheus 采集业务暴露的监控指标。


[](id:way1)

#### 方式1：配置 Promtheus 采集规则

在 Promtheus 的采集规则配置文件中添加以下采集规则。示例如下：
```yaml
	- job_name: httpserver
		scrape_interval: 5s
		kubernetes_sd_configs:
		- role: endpoints
			namespaces:
				names:
				- httpserver
		relabel_configs:
		- action: keep
			source_labels:
			- __meta_kubernetes_service_label_app
			regex: httpserver
		- action: keep
			source_labels:
			- __meta_kubernetes_endpoint_port_name
			regex: http
```

[](id:way2)

#### 方式2：配置 ServiceMonitor

若已安装 prometheus-operator，可以通过创建 ServiceMonitor 的 CRD 对象配置 Prometheus。示例如下：
```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: httpserver
spec:
  endpoints:
  - port: http
    interval: 5s
  namespaceSelector:
    matchNames:
    - httpserver
  selector:
    matchLabels:
      app: httpserver
```

### 安装 prometheus-adapter

1. 使用 Helm 安装 [prometheus-adapter](https://artifacthub.io/packages/helm/prometheus-community/prometheus-adapter)，安装前请确定并配置自定义指标。按照上文 [暴露监控指标](#example) 中的示例，在业务中使用 `httpserver_requests_total` 指标来记录 HTTP 请求，因此可以通过如下的 PromQL 计算出每个业务 Pod 的 QPS 监控。示例如下：
```
sum(rate(http_requests_total[2m])) by (pod)
```
2. 将其转换为 prometheus-adapter 的配置，创建 `values.yaml`，内容如下：
```yaml
rules:
      default: false
      custom:
      - seriesQuery: 'httpserver_requests_total'
        resources:
          template: <<.Resource>>
        name:
          matches: "httpserver_requests_total"
          as: "httpserver_requests_qps" # PromQL 计算出来的 QPS 指标
        metricsQuery: sum(rate(<<.Series>>{<<.LabelMatchers>>}[1m])) by (<<.GroupBy>>)
prometheus:
      url: http://prometheus.monitoring.svc.cluster.local # 替换 Prometheus API 的地址 (不写端口)
      port: 9090
```
3. 执行以下 Helm 命令安装 prometheus-adapter，示例如下：
>! 安装前需要删除 TKE 已经注册的 Custom Metrics API，删除命令如下：
> `kubectl delete apiservice v1beta1.custom.metrics.k8s.io`
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
# Helm 3
helm install prometheus-adapter prometheus-community/prometheus-adapter -f values.yaml
# Helm 2
# helm install --name prometheus-adapter prometheus-community/prometheus-adapter -f values.yaml
```

### 测试验证

若安装正确，执行以下命令，可以查看到 Custom Metrics API 返回配置的 QPS 相关指标。示例如下：
```bash
$ kubectl get --raw /apis/custom.metrics.k8s.io/v1beta1
{
  "kind": "APIResourceList",
  "apiVersion": "v1",
  "groupVersion": "custom.metrics.k8s.io/v1beta1",
  "resources": [
    {
      "name": "jobs.batch/httpserver_requests_qps",
      "singularName": "",
      "namespaced": true,
      "kind": "MetricValueList",
      "verbs": [
        "get"
      ]
    },
    {
      "name": "pods/httpserver_requests_qps",
      "singularName": "",
      "namespaced": true,
      "kind": "MetricValueList",
      "verbs": [
        "get"
      ]
    },
    {
      "name": "namespaces/httpserver_requests_qps",
      "singularName": "",
      "namespaced": false,
      "kind": "MetricValueList",
      "verbs": [
        "get"
      ]
    }
  ]
}
```

执行以下命令，可以查看到 Pod 的 QPS 值。示例如下：
>?下述示例 QPS 为500m，表示 QPS 值为0.5。
``` bash
$ kubectl get --raw /apis/custom.metrics.k8s.io/v1beta1/namespaces/httpserver/pods/*/httpserver_requests_qps
{
  "kind": "MetricValueList",
  "apiVersion": "custom.metrics.k8s.io/v1beta1",
  "metadata": {
    "selfLink": "/apis/custom.metrics.k8s.io/v1beta1/namespaces/httpserver/pods/%2A/httpserver_requests_qps"
  },
  "items": [
    {
      "describedObject": {
        "kind": "Pod",
        "namespace": "httpserver",
        "name": "httpserver-6f94475d45-7rln9",
        "apiVersion": "/v1"
      },
      "metricName": "httpserver_requests_qps",
      "timestamp": "2020-11-17T09:14:36Z",
      "value": "500m",
      "selector": null
    }
  ]
}
```



### 测试 HPA

假如设置每个业务 Pod 的平均 QPS 达到50时将触发扩容，最小副本为1个，最大副本为1000个，则配置示例如下：
``` yaml
apiVersion: autoscaling/v2beta2
kind: HorizontalPodAutoscaler
metadata:
  name: httpserver
  namespace: httpserver
spec:
  minReplicas: 1
  maxReplicas: 1000
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: httpserver
  metrics:
  - type: Pods
    pods:
      metric:
        name: httpserver_requests_qps
      target:
        averageValue: 50
        type: AverageValue
```

执行以下命令对业务进行压测，观察是否自动扩容。示例如下：
``` bash
$ kubectl get hpa
NAME         REFERENCE               TARGETS     MINPODS   MAXPODS   REPLICAS   AGE
httpserver   Deployment/httpserver   83933m/50   1         1000      2          18h
$ kubectl get pods
NAME                          READY   STATUS              RESTARTS   AGE
httpserver-6f94475d45-47d5w   1/1     Running             0          3m41s
httpserver-6f94475d45-7rln9   1/1     Running             0          37h
httpserver-6f94475d45-6c5xm   0/1     ContainerCreating   0          1s
httpserver-6f94475d45-wl78d   0/1     ContainerCreating   0          1s
```

若扩容正常，则说明已实现 HPA 基于业务自定义指标进行弹性伸缩。
