Prometheus 提供了 [官方版 Golang 库](https://github.com/prometheus/client_golang) 用于采集并暴露监控数据，本文为您介绍如何使用官方版 Golang 库来暴露 Golang runtime 相关的数据，以及其它一些基本简单的示例，并使用腾讯云监控 Prometheus 托管服务来采集指标展示数据等。

>?Golang Client API 相关的文档详见 [GoDoc](https://pkg.go.dev/github.com/prometheus/client_golang)。



## 安装

通过 `go get` 命令来安装相关依赖，示例如下：

```bash
go get github.com/prometheus/client_golang/prometheus
go get github.com/prometheus/client_golang/prometheus/promauto
go get github.com/prometheus/client_golang/prometheus/promhttp
```

## 开始（运行时指标）

1. 准备一个 HTTP 服务，路径通常使用 `/metrics`。可以直接使用 [`prometheus/promhttp`](https://pkg.go.dev/github.com/prometheus/client_golang@v1.8.0/prometheus/promhttp) 里提供的 [`Handler`](https://pkg.go.dev/github.com/prometheus/client_golang@v1.8.0/prometheus/promhttp#Handler) 函数。
如下是一个简单的示例应用，通过 `http://localhost:2112/metrics` 暴露 Golang 应用的一些默认指标数据（包括运行时指标、进程相关指标以及构建相关的指标）：

```go
package main

import (
        "net/http"

        "github.com/prometheus/client_golang/prometheus/promhttp"
)

func main() {
        http.Handle("/metrics", promhttp.Handler())
        http.ListenAndServe(":2112", nil)
}
```

2. 执行以下命令启动应用：

```bash
go run main.go
```

3. 执行以下命令，访问基础内置指标数据：

```bash
curl http://localhost:2112/metrics
```

## 应用层面指标

1. 上述示例仅仅暴露了一些基础的内置指标。应用层面的指标还需要额外添加（后续我们将提供一些 SDK 方便接入）。如下示例暴露了一个名为 `myapp_processed_ops_total` 的 [计数类型](https://prometheus.io/docs/concepts/metric_types/#counter) 指标，用于对目前已经完成的操作进行计数。如下每两秒操作一次，同时计数器加1：

```go
package main

import (
        "net/http"
        "time"

        "github.com/prometheus/client_golang/prometheus"
        "github.com/prometheus/client_golang/prometheus/promauto"
        "github.com/prometheus/client_golang/prometheus/promhttp"
)

func recordMetrics() {
        go func() {
                for {
                        opsProcessed.Inc()
                        time.Sleep(2 * time.Second)
                }
        }()
}

var (
        opsProcessed = promauto.NewCounter(prometheus.CounterOpts{
                Name: "myapp_processed_ops_total",
                Help: "The total number of processed events",
        })
)

func main() {
        recordMetrics()

        http.Handle("/metrics", promhttp.Handler())
        http.ListenAndServe(":2112", nil)
}
```

2. 执行以下命令启动应用：

```bash
go run main.go
```

3. 执行以下命令，访问暴露的指标：

```bash
curl http://localhost:2112/metrics
```

从输出结果我们可以看到 `myapp_processed_ops_total` 计数器相关的信息，包括帮助文档、类型信息、指标名和当前值，如下所示：

```
# HELP myapp_processed_ops_total The total number of processed events
# TYPE myapp_processed_ops_total counter
myapp_processed_ops_total 666
```

## 使用腾讯云 Prometheus 监控服务

上述我们提供了两个示例展示如何使用 Prometheus Golang 库来暴露应用的指标数据，但暴露的监控指标数据为文本类型，需要搭建维护额外的 Prometheus 服务来抓取指标，可能还需要额外的 Grafana 来对数据进行可视化展示。

通过使用 Prometheus 托管服务可以直接省去如上步骤，只需简单的单击操作即可使用。详情请参见 [快速使用指南](https://cloud.tencent.com/document/product/248/48688)。

### 打包部署应用

1. Golang 应用一般可以使用如下形式的 Dockerfile（按需修改）：

```dockerfile
FROM golang:alpine AS builder
RUN apk add --no-cache ca-certificates \
        make \
        git
COPY . /go-build
RUN cd /go-build && \
        export GO111MODULE=on && \
        export GOPROXY=https://goproxy.io && \
        go build -o 'golang-exe' path/to/main/

FROM alpine
RUN apk add --no-cache tzdata
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs
COPY --from=builder /go-build/golang-exe /usr/bin/golang-exe
ENV TZ Asia/Shanghai
CMD ["golang-exe"]
```

2. 镜像可以使用 [腾讯云的镜像仓库](https://cloud.tencent.com/document/product/457/9117)，或者使用其它公有或者自有镜像仓库。

3. 需要根据应用类型定义一个 Kubernetes 的资源，这里我们使用 [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)，示例如下：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: golang-app-demo
  labels:
    app: golang-app-demo
spec:
  replicas: 3
  selector:
    matchLabels:
      app: golang-app-demo
  template:
    metadata:
      labels:
        app: golang-app-demo
    spec:
      containers:
      - name: golang-exe-demo:v1
        image: nginx:1.14.2
        ports:
        - containerPort: 80
```

4. 同时需要 Kubernetes [Service](https://kubernetes.io/docs/concepts/services-networking/service/) 做服务发现和负载均衡。

```yaml
apiVersion: v1
kind: Service
metadata:
  name: golang-app-demo
spec:
  selector:
    app: golang-app-demo
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
```

>!必须添加一个 Label 来标明目前的应用，Label 名不一定为 `app`，但是必须有类似含义的 Label 存在，其它名字的 Label 我们可以在后面添加数据采集任务的时候做 relabel 来达成目的。

5. 可以通过 [容器服务控制台](https://console.cloud.tencent.com/tke2/) 或者直接使用 [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) 将这些资源定义提交给 Kubernetes，然后等待创建成功。

### 添加数据采集任务

当服务运行起来之后，需要进行如下操作让腾讯云 Prometheus 托管服务发现并采集监控指标：

1. 登录 [云监控 Prometheus 控制台](https://console.cloud.tencent.com/monitor/prometheus)，选择对应 Prometheus 实例进入管理页面。
2. 通过集成容器服务列表单击**集群 ID**，进入到容器服务集成管理页面。
3. 通过服务发现添加 `Service Monitor`，目前支持基于 `Labels` 发现对应的目标实例地址，因此可以对一些服务添加特定的 `K8S Labels`，可以使 `Labels` 下的服务都会被 Prometheus 服务自动识别出来，不需要再为每个服务一一添加采取任务，以上面的例子配置信息如下：

> ? `port` 的取值为 `service yaml` 配置文件里的 `spec/ports/name` 对应的值。

```yaml
  apiVersion: monitoring.coreos.com/v1
  kind: ServiceMonitor
  metadata:
    name: go-demo    # 填写一个唯一名称
    namespace: cm-prometheus  # namespace固定，不要修改
  spec:
    endpoints:
    - interval: 30s
      # 填写service yaml中Prometheus Exporter对应的Port的Name
      port: 2112
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

```

>!示例中名称为 application 的 Label 必须配置，否则无法使用我们提供一些其它的开箱即用的集成功能。更多高阶用法请参见 [ServiceMonitor](https://github.com/prometheus-operator/prometheus-operator/blob/master/Documentation/api.md#servicemonitor) 或 [PodMonitor](https://github.com/prometheus-operator/prometheus-operator/blob/master/Documentation/api.md#podmonitor)。

### 查看监控

1. 在 [Prometheus 实例](https://console.cloud.tencent.com/monitor/prometheus) 列表，找到对应的  Prometheus 实例，单击实例ID 右侧**<img src="https://main.qcloudimg.com/raw/978c842f0c093a31df8d5240dd01016d.png" width="2%"/>** 图标，打开您的专属 Grafana，输入您的账号密码，即可进行 Grafana 可视化大屏操作区。
2. 进入 Grafana，单击**<img src="https://main.qcloudimg.com/raw/7e3fff6131aa085987552a9725e9ae54.png" width="2%"/>**图表，展开监控面板，单击对应的监控图表名称即可查看监控数据。
![](https://main.qcloudimg.com/raw/cafce5a26169309cb89ba176317c8d5c.png)
![](https://main.qcloudimg.com/raw/627c99e89dd58043069b3c2e086cf8a9.png)


## 总结

本文通过两个示例展示了如何将 Golang 相关的指标暴露给 Prometheus 托管服务，以及如何使用内置的可视化的图表查看监控数据。文档只使用了计数类型 Counter 的指标，对于其它场景可能还需要 Gauge，Histgram 以及 Summary 类型的指标， [指标类型](https://prometheus.io/docs/concepts/metric_types/)。

对于其它应用场景，我们会集成更多框架提供更多开箱即用的指标监控、可视化面板以及告警模板。
