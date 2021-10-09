## 操作场景

metrics-server 可实现 Kubernetes 的 Resource Metrics API（metrics.k8s.io），通过此 API 可以查询 Pod 与 Node 的部分监控指标，Pod 的监控指标用于 [HPA](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)、[VPA](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler) 与 `kubectl top pods` 命令，而 Node 指标目前只用于 `kubectl top nodes` 命令。容器服务 TKE 自带 Resource Metrics API 的实现，指向 hpa-metrics-server，且目前提供 Pod 的监控指标。

将 metrics-server 安装到集群后，可以通过 `kubectl top nodes` 获取节点的监控概览，以替换 Resource Metrics API 的实现。容器服务控制台创建的 HPA 不会用到 Resource Metrics，仅使用 Custom Metrics，因此安装 metrics-server 不会影响在 TKE 控制台创建的 HPA。本文将介绍如何在 TKE 上安装 metrics-server。



## 操作步骤

### 下载 yaml 部署文件

执行以下命令，下载 metrics-server 官方的部署 yaml:

```bash
wget https://github.com/kubernetes-sigs/metrics-server/releases/download/v0.5.0/components.yaml
```

### 修改 metrics-server 启动参数

metrics-server 会请求每台节点的 kubelet 接口来获取监控数据，接口通过 HTTPS 暴露，但 TKE 节点的 kubelet 使用的是自签证书，若 metrics-server 直接请求 kubelet 接口，将产生证书校验失败的错误，因此需要在 components.yaml 文件中加上 `--kubelet-insecure-tls` 启动参数。
且由于 metrics-server 官方镜像仓库存储在 `k8s.gcr.io` ，国内可能无法直接拉取，您可以自行同步到 CCR 或使用已同步的镜像 `ccr.ccs.tencentyun.com/mirrors/metrics-server:v0.5.0`。

components.yaml 文件修改示例如下：

```yaml
      containers:
      - args:
        - --cert-dir=/tmp
        - --secure-port=443
        - --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname
        - --kubelet-use-node-status-port
        - --metric-resolution=15s
        - --kubelet-insecure-tls # 加上该启动参数
        image: ccr.ccs.tencentyun.com/mirrors/metrics-server:v0.5.0 # 国内集群，请替换成这个镜像
```

### 部署 metrics-server

修改 components.yaml 之后，执行以下命令，通过 kubectl 一键部署到集群：

```bash
kubectl apply -f components.yaml
```

### 检查运行状态

1. 执行以下命令，检查 metrics-server 是否正常启动。示例如下：
```bash
$ kubectl get pod -n kube-system | grep metrics-server
metrics-server-f976cb7d-8hssz         1/1     Running   0          1m
```
2. 执行以下命令，检查配置文件。示例如下：
```bash
$ kubectl get --raw /apis/metrics.k8s.io/v1beta1  | jq
{
  "kind": "APIResourceList",
  "apiVersion": "v1",
  "groupVersion": "metrics.k8s.io/v1beta1",
  "resources": [
    {
      "name": "nodes",
      "singularName": "",
      "namespaced": false,
      "kind": "NodeMetrics",
      "verbs": [
        "get",
        "list"
      ]
    },
    {
      "name": "pods",
      "singularName": "",
      "namespaced": true,
      "kind": "PodMetrics",
      "verbs": [
        "get",
        "list"
      ]
    }
  ]
}
```
3. 执行以下命令，检查节点占用性能情况。示例如下：
```bash
$ kubectl top nodes
NAME    CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%
test1   1382m        35%    2943Mi          44%
test2   397m         10%    3316Mi          49%
test3   81m          8%     464Mi           77%
```
