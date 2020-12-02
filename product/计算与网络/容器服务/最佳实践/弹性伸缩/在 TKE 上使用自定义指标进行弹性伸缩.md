## 背景

TKE 基于 [Custom Metrics API](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/instrumentation/custom-metrics-api.md) 支持了许多用于弹性伸缩的指标，涵盖 CPU、内存、硬盘、网络以及 GPU 相关的指标，覆盖绝大多数的 HPA 弹性伸缩场景，详细列表参考 [自动伸缩指标说明](https://cloud.tencent.com/document/product/457/38929)。
如果有更复杂的场景需求，比如基于业务单副本 QPS 大小来进行自动扩缩容，可以考虑自行安装 [prometheus-adapter](https://github.com/DirectXMan12/k8s-prometheus-adapter) 来实现，也是本文所要将的内容。

## 实现原理
Kubernetes 提供了  [Custom Metrics API](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/instrumentation/custom-metrics-api.md) 与 [External Metrics API](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/instrumentation/external-metrics-api.md) 来对 HPA 的指标进行扩展，让用户能够根据实际需求进行自定义。

prometheus-adapter 对这两种 API 都有支持，通常使用 Custom Metrics API 就够了，本文也主要针对此 API 来实现使用自定义指标进行弹性伸缩。

## 前提条件

* 创建了 TKE 集群，且版本在 1.12 及以上。
* 部署有 Prometheus 并做了相应的自定义指标采集。
* 安装好 [helm](https://helm.sh/docs/intro/install/)。

## 操作步骤

### 业务暴露监控指标

这里以一个简单的 golang 业务程序为例，暴露 HTTP 请求的监控指标:

``` go
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

该示例程序暴露了 `httpserver_requests_total` 指标，记录 HTTP 的请求，通过这个指标可以计算出该业务程序的 QPS 值。

### 部署业务程序

将我们的业务程序进行容器化并部署到 TKE 集群，通过使用 Deployment 部署:

``` yaml
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

业务部署好了，我们需要让我们的 Promtheus 去采集业务暴露的监控指标。

#### 方式一: 配置 Promtheus 采集规则

在 Promtheus 的采集规则配置文件添加采集规则:

``` yaml
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

#### 方式二: 配置 ServiceMonitor

若已安装 prometheus-operator，则可通过创建 ServiceMonitor 的 CRD 对象配置 Prometheus。示例如下:

``` yaml
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

我们使用 helm 安装 [prometheus-adapter](https://artifacthub.io/packages/helm/prometheus-community/prometheus-adapter)，安装前最重要的是确定并配置自定义指标，按照前面的示例，我们业务中使用 `httpserver_requests_total` 这个指标来记录 HTTP 请求，那么我们可以通过类似下面的 PromQL 计算出每个业务 Pod 的 QPS 监控:

```
sum(rate(http_requests_total[2m])) by (pod)
```

我们需要将其转换为 prometheus-adapter 的配置，准备一个 `values.yaml`:

``` yaml
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
  port: 9090u
```

执行 helm 命令进行安装:

``` bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
# Helm 3
helm install prometheus-adapter prometheus-community/prometheus-adapter -f values.yaml
# Helm 2
# helm install --name prometheus-adapter prometheus-community/prometheus-adapter -f values.yaml
```

### 测试是否安装正确

如果安装正确，是可以看到 Custom Metrics API 返回了我们配置的 QPS 相关指标:

``` bash
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

也能看到业务 Pod 的 QPS 值:

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

> 上面示例 QPS 为 `500m`，表示 QPS 值为 0.5

### 测试 HPA

假如我们设置每个业务 Pod 的平均 QPS 达到 50，就触发扩容，最小副本为 1 个，最大副本为1000，HPA 可以这么配置:

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

然后对业务进行压测，观察是否扩容:

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

扩容正常则说明已经实现 HPA 基于业务自定义指标进行弹性伸缩。