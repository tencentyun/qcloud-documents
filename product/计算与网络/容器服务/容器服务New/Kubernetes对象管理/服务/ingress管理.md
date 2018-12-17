## ingress 管理
### ingress 简介
ingress是允许访问到集群内Service的规则的集合， 可以配置转发规则达到根据不同URL访问到集群内不同的Service。
为了使Ingress资源正常工作，群集必须运行Ingress-controller. TKE服务在集群内默认启用了基于腾讯云负载均衡器实现的`l7-lb-controller` Ingress-controller, 支持HTTP，HTTPS。
同时也默认支持nginx-ingress类型， 您可以根据您的业务需要选择不同的ingress类型。

### ingress 控制台操作指引
#### 创建 Ingress
1. 点击需要部署 Ingress 的集群ID，进入集群详情页面。
2. 点击 Ingress 选项，选择新建 Ingress
3. 根据指引设置 Ingress 参数，完成创建。

![][createIngress]

#### 更新Ingress
**Yaml更新**
1. 点击需要部署的 Ingress 的集群ID，进入集群详情页面。
2. 选择需要更新的 Ingress , 进入 Ingress 详情页，点击Yaml tab, 可编辑Yaml直接更新

**更新转发规则**
1. 点击需要部署的 Ingress 的集群ID，进入集群详情页面。
2. 选择需要更新的 Ingress , 点击更新转发规则操作。
3. 根据UI填写转发设置，完成更新。

![][updateIngress]

### kubectl 操作 ingress 指引
#### Yaml示例
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
>注：如果是带宽上移账号，在创建公网访问方式的服务时需要指定如下两个 annotations 项：
- `kubernetes.io/ingress.internetChargeType`.公网带宽计费方式， TRAFFIC_POSTPAID_BY_HOUR（按使用流量计费），BANDWIDTH_POSTPAID_BY_HOUR（按带宽计费）。
- `kubernetes.io/ingress.internetMaxBandwidthOut`.带宽上限，范围：[1,2000] Mbps。
如：
```Yaml
metadata:
  annotations:
    kubernetes.io/ingress.internetChargeType: TRAFFIC_POSTPAID_BY_HOUR
    kubernetes.io/ingress.internetMaxBandwidthOut: "10"
```

- kind: 标识该资源是 ingress 类型
- metadata：该 ingress 的名称、Label等基本信息
- metadata.annotations: 对 ingress 的额外说明，腾讯云TKE额外增强能力可以通过该参数设置。
- spec.rules：该ingress的转发规则， 配置该规则可实现简单路由服务、基于域名的简单扇出路由、简单路由默认域名、配置安全的路由服务等。


#### 创建Ingress
1. 准备 ingress Yaml文件， 例如上述文件为my-ingress.Yaml （请先创建好工作负载）
2. kubectl安装完成，并且已连接上集群（可直接登录集群节点使用kubectl）
3. 执行命令创建：
```shell
kubectl create -f my-ingress.yaml
```
4. 执行命令验证创建情况：
```shell
kubectl get ingress
```

#### 更新Ingress
**方法一**：直接通过`kubectl edit  ingress/[name]`更新
**方法二**：删除旧的ingress， 重新通过kubectl create/apply 创建ingress.

[createIngress]:https://main.qcloudimg.com/raw/826ae150ef1e2bcb360d9d2d8c6130b0.png
[updateIngress]:https://main.qcloudimg.com/raw/83672cc160779ee627d5a6caa653d7f4.png
