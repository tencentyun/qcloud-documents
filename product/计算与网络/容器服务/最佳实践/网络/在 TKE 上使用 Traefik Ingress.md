## 背景

[Traefik](https://doc.traefik.io/traefik/) 与 Nginx 类似，是一款优秀的反向代理工具，相比之下，它具有以下优势:
1. 原生支持动态配置，比如 Kubernetes 的 Ingress 资源或 IngressRoute 等 CRD 资源 (nginx 每次需要 reload 完整配置，某些情况下可能会影响连接)。
2. 原生支持服务发现，使用 Ingress 或 IngressRoute 等动态配置后，会自动 watch 后端 endpoint，同步更新到负载均衡的后端列表中。
3. 自带漂亮的 dashboard 后台页面。
4. Metrics 原生的支持，与 Prometheus 和 Kubernetes 无缝集成。
5. 拥有更丰富的高级功能，比如多版本的灰度发布、流量复制、自动生成 HTTPS 免费证书、中间件等。

## 前提条件

* 创建了 TKE 集群并能够通过 kubectl 管理集群，参考官方文档 [连接集群](https://cloud.tencent.com/document/product/457/32191)。
* 安装了 [helm](https://helm.sh/docs/intro/install/)。

## 安装

这里给出一个在 TKE 上安装的示例，完整安装方法请参考 [官方文档](https://doc.traefik.io/traefik/getting-started/install-traefik/#use-the-helm-chart)。

首先添加 traefik 的 helm chart repo:

``` bash
helm repo add traefik https://helm.traefik.io/traefik
```

然后准备安装配置 `values-traefik.yaml`:

``` yaml
providers:
  kubernetesIngress:
    publishedService:
      enabled: true # 让 Ingress 的外部 IP 地址状态显示为 Traefik 的 LB IP 地址。

additionalArguments:
- "--providers.kubernetesingress.ingressclass=traefik" # 指定 ingress class 名称
- "--log.level=DEBUG"

service:
  annotations:
    service.cloud.tencent.com/direct-access: "true" # 网关类的应用建议使用 LB 直通 Pod (绕过 NodePort)。若使用 VPC-CNI 与 Global Router 两种网络模式混用，用此注解来显示声明 LB 直绑 Pod (绕过 NodePort); 若创建集群时就选的 VPC-CNI 网络模式，则不需要显示声明 (默认 LB 直通 Pod)。更多请参考官方文档: https://cloud.tencent.com/document/product/457/48793
    service.kubernetes.io/tke-existed-lbid: lb-lb57hvgl # 用此注解绑定提前创建好的 LB，使得即便 Traefik 日后重建，也能保证流量入口不变。若不指定此注解，默认自动创建新的 LB。更多请参考官方文档: https://cloud.tencent.com/document/product/457/45491

ports:
  web:
    expose: true
    exposedPort: 80 # 对外的 HTTP 端口号，使用标准端口号在国内需备案
  websecure:
    expose: true
    exposedPort: 443 # 对外的 HTTPS 端口号，使用标准端口号在国内需备案

deployment:
  enabled: true
  replicas: 1
  podAnnotations:
    tke.cloud.tencent.com/networks: "tke-route-eni" # 在 VPC-CNI 与 Global Router 两种网络模式混用的情况下，显示声明 Pod 要使用弹性网卡，与下面 eni-ip 的 request 与 limit 一起配合使用。

resources:
  requests:
    tke.cloud.tencent.com/eni-ip: "1"
  limits:
    tke.cloud.tencent.com/eni-ip: "1"
```

> 完整的默认配置可通过 `helm show values traefik/traefik` 查看。

准备好安装配置后使用 helm 命令将 traefik 安装到集群中:

``` bash
kubectl create ns ingress
helm upgrade --install traefik -f values-traefik.yaml traefik/traefik
```

获取流量入口的 IP 地址 (EXTERNAL-IP):

``` bash
$ kubectl get service -n ingress
NAME      TYPE           CLUSTER-IP       EXTERNAL-IP     PORT(S)                      AGE
traefik   LoadBalancer   172.22.252.242   49.233.239.84   80:31650/TCP,443:32288/TCP   42h
```

## 使用 Ingress

Traefik 支持使用 Kubernetes 的 Ingress 资源作为动态配置，所以可以直接在集群中创建 Ingress 资源来对外暴露集群中，注意需要加上指定的 ingress class (安装 traefik 时定义的):

``` yaml
apiVersion: networking.k8s.io/v1beta1
kind: Ingress
metadata:
  name: test-ingress
  annotations:
    kubernetes.io/ingress.class: traefik # 这里指定 ingress class 名称
spec:
  rules:
  - host: traefik.demo.com
    http:
      paths:
      - path: /test
        backend:
          serviceName: nginx
          servicePort: 80
```

>! 由于 TKE 暂时没有将 Traefik 产品化，所以创建 Ingress 不能直接在界面控制台可视化创建，需要使用 yaml 来创建。

## 使用 IngressRoute

Traefik 不仅支持标准的 Kubernetes 的 Ingress 资源，也支持 Traefik 特有的 CRD 资源，用的最多的是 IngressRoute，它可以支持更多 Ingress 不具备的高级功能，下面是一个简单的例子:

``` yaml
apiVersion: traefik.containo.us/v1alpha1
kind: IngressRoute
metadata:
  name: test-ingressroute
spec:
  entryPoints:
    - web
  routes:
    - match: Host(`traefik.demo.com`) && PathPrefix(`/test`)
      kind: Rule
      services:
        - name: nginx
          port: 80
```

更多用法请参考 Traefik 的 [官方文档](https://doc.traefik.io/traefik/routing/providers/kubernetes-crd/)。