## 简介
Ingress 是允许访问到集群内 Service 的规则的集合，您可以通过配置转发规则，实现不同 URL 可以访问到集群内不同的 Service。
为了使 Ingress 资源正常工作，集群必须运行 Ingress-controller。TKE 服务在集群内默认启用了基于腾讯云负载均衡器实现的 `l7-lb-controller`，支持 HTTP、HTTPS，同时也支持 nginx-ingress 类型，您可以根据您的业务需要选择不同的 Ingress 类型。

## Ingress 控制台操作指引

### 创建 Ingress

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在左侧导航栏中，单击【集群】，进入集群管理页面。
3. 单击需要创建 Ingress 的集群 ID，进入待创建 Ingress 的集群管理页面。
4. 选择 “服务” > “Ingress”，进入 Ingress 信息页面。如下图所示：
![Ingress](https://main.qcloudimg.com/raw/72d715c235d98e1a8e38c05ddf105a21.png)
5. 单击【新建】，进入 “新建Ingress” 页面。如下图所示：
![新建Ingress](https://main.qcloudimg.com/raw/116d6add93717282a62f1793e2146317.png)
6. 根据实际需求，设置 Ingress 参数。关键参数信息如下：
 - Ingress名称：自定义。
 - 网络类型：默认为 “公网”，请根据实际需求进行选择。
 - 命名空间：根据实际需求进行选择。
 - 监听端口：默认为 “Http:80”，请根据实际需求进行选择。
 - 转发配置：根据实际需求进行设置。
7. 单击【创建Ingress】，完成创建。

### 更新 Ingress

#### 更新 YAML

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在左侧导航栏中，单击【集群】，进入集群管理页面。
3. 单击需要更新 YAML 的集群 ID，进入待更新 YAML 的集群管理页面。
4. 选择 “服务” > “Ingress”，进入 Ingress 信息页面。如下图所示：
![Ingress](https://main.qcloudimg.com/raw/72d715c235d98e1a8e38c05ddf105a21.png)
5. 在需要更新 YAML 的 Ingress 行中，单击【编辑YAML】，进入更新 Ingress 页面。
6. 在 “更新Ingress” 页面，编辑 YAML，单击【完成】，即可更新 YAML。

#### 更新转发规则

1. 集群管理页面，单击需要更新 YAML 的集群 ID，进入待更新 YAML 的集群管理页面。
2. 选择 “服务” > “Ingress”，进入 Ingress 信息页面。如下图所示：
![Ingress](https://main.qcloudimg.com/raw/72d715c235d98e1a8e38c05ddf105a21.png)
3. 在需要更新转发规则的 Ingress 行中，单击【更新转发配置】，进入更新转发配置页面。如下图所示：
![更新转发配置](https://main.qcloudimg.com/raw/4246dede3aaa2e21bdb691dd6ccf1a48.png)
3. 根据实际需求，修改转发配置，单击【更新转发配置】，即可完成更新。

## kubectl 操作 Ingress 指引

<span id="YAMLSample"></span>
### YAML 示例
```Yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  annotations:
    kubernetes.io/ingress.class: qcloud ## 可选值：qcloud（CLB类型ingress）, nginx（nginx-ingress）
    ## kubernetes.io/ingress.subnetId: subnet-xxxxxxxx  ##若是创建CLB类型内网ingress需指定该条annotation
  name: my-ingress
  namespace: default
spec:
  rules:
  - host: localhost
    http:
      paths:
      - backend:
          serviceName: non-service
          servicePort: 65535
        path: /
```
- kind：标识Ingress资源类型。
- metadata：Ingress 的名称、Label等基本信息。
- metadata.annotations: Ingress 的额外说明，可通过该参数设置腾讯云 TKE 的额外增强能力。
- spec.rules：Ingress 的转发规则，配置该规则可实现简单路由服务、基于域名的简单扇出路由、简单路由默认域名、配置安全的路由服务等。

>? 如果您使用的是带宽上移账号，在创建公网访问方式的服务时需要指定以下两个 annotations 项：
> - `kubernetes.io/ingress.internetChargeType` 公网带宽计费方式，TRAFFIC_POSTPAID_BY_HOUR（按使用流量计费），BANDWIDTH_POSTPAID_BY_HOUR（按带宽计费）。
> - `kubernetes.io/ingress.internetMaxBandwidthOut` 带宽上限，范围：[1,2000] Mbps。
例如：
```Yaml
metadata:
  annotations:
    kubernetes.io/ingress.internetChargeType: TRAFFIC_POSTPAID_BY_HOUR
    kubernetes.io/ingress.internetMaxBandwidthOut: "10"
```

### 创建 Ingress

1. 参考 [YAML 示例](#YAMLSample)，准备 Ingress YAML 文件。
2. 安装 Kubectl，并连接集群。操作详情请参考 [通过 Kubectl 连接集群](https://cloud.tencent.com/document/product/457/8438)。
3. 执行以下命令，创建 Ingress YAML 文件。
```shell
kubectl create -f Ingress YAML 文件名称
```
例如，创建一个文件名为 my-ingress.yaml 的 Ingress YAML 文件，则执行以下命令：
```shell
kubectl create -f my-ingress.yaml
```
4. 执行以下命令，验证创建是否成功。
```shell
kubectl get ingress
```
返回类似以下信息，即表示创建成功。
```
NAME          HOSTS       ADDRESS   PORTS     AGE
clb-ingress   localhost             80        21s
```

### 更新 Ingress

#### 方法一

执行以下命令，更新 Ingress。
```
kubectl edit  ingress/[name]
```

#### 方法二

1. 手动删除旧的 Ingress。
2. 执行以下命令，重新创建 Ingress。
```
kubectl create/apply
```
