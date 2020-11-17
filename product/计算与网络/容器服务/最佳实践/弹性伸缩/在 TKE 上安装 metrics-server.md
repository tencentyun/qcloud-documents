## 操作场景
[metrics-server]() 实现了 Kubernetes 的 Resource Metrics API (metrics.k8s.io)，通过此 API 可以查询 pod 与 node 的一些监控指标，pod 的监控指标用于 [HPA](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/), [VPA](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler) 与 `kubectl top pods` 命令，而 node 指标目前只用于 `kubectl top nodes` 命令。TKE 自带了一个 Resource Metrics API 的实现，指向 hpa-metrics-server，仅提供 pod 的监控指标。

如果期望使用 `kubectl top nodes` 获取节点的监控概览，可以安装 metrics-server 到集群，会替换 Resource Metrics API 的实现，指向 metrics-server。安装 metrics-server 不会影响在 TKE 控制台创建的 HPA，因为控制台创建的 HPA 不会用到 Resource Metrics，只会用 Custom Metrics。

## 操作步骤

如果嫌麻烦，可以使用下面的命令一键安装，但不保证与最新版同步:

``` bash
kubectl apply -f https://raw.githubusercontent.com/TencentCloudContainerTeam/manifest/master/metrics-server/components.yaml
```

如果要保证使用最新版，可按照下面步骤操作。

### 下载官方部署 yaml

下载 metrics-server 的最新部署 yaml 文件:

``` bash
wget https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

### 修改 metrics-server 启动参数

metrics-server 会去请求每台节点的 kubelet 的接口来获取监控数据，接口通过 https 暴露，但 TKE 节点的 kubelet 使用了自签证书，metrics-server 直接去请求会报证书校验失败的错误，所以我们需要加上 `--kubelet-insecure-tls` 的启动参数；另外，由于 metrics-server 官方镜像仓库在 `k8s.gcr.io` ，国内拉取会失败，可以自行同步到 CCR 或直接使用 `ccr.ccs.tencentyun.com/mirrors/metrics-server:v0.4.0` 这个已经同步好的。

``` yaml
      containers:
      - args:
        - --cert-dir=/tmp
        - --secure-port=4443
        - --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname
        - --kubelet-use-node-status-port
        - --kubelet-insecure-tls # 这个是新加的参数
        image: ccr.ccs.tencentyun.com/mirrors/metrics-server:v0.4.0 # 国内集群替换成这个镜像地址
```

### 部署

修改好 yaml 后，通过 kubectl 一键部署到集群:

``` bash
kubectl apply -f components.yaml
```

### 检查是否正常运行

``` bash
$ kubectl get pod -n kube-system | grep metrics-server
metrics-server-f976cb7d-8hssz         1/1     Running   0          1m

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

$ kubectl top nodes
NAME    CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%
test1   1382m        35%    2943Mi          44%
test2   397m         10%    3316Mi          49%
test3   81m          8%     464Mi           77%
```