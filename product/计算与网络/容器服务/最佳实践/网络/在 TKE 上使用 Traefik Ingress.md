## 操作场景

[Traefik](https://doc.traefik.io/traefik/) 是一款优秀的反向代理工具，与 Nginx 相比，Traefik 具有以下优势：

- 原生支持动态配置。例如，Kubernetes 的 Ingress 资源或 IngressRoute 等 CRD 资源（Nginx 每次需重新加载完整配置，部分情况下可能会影响连接）。
- 原生支持服务发现。使用 Ingress 或 IngressRoute 等动态配置后，会自动 watch 后端 endpoint，同步更新到负载均衡的后端列表中。
- 提供美观的 Dashboard 管理页面。
- 原生支持 Metrics，与 Prometheus 和 Kubernetes 无缝集成。
- 拥有更丰富的高级功能。例如，多版本的灰度发布、流量复制、自动生成 HTTPS 免费证书、中间件等。

本文将介绍如何在 TKE 集群安装 Traefik 以及提供通过 Traefik 使用 Ingress 和 IngressRoute 示例。


## 前提条件

- 已创建 [TKE 集群](https://cloud.tencent.com/document/product/457/32189) 并能够通过 Kubectl [连接集群](https://cloud.tencent.com/document/product/457/32191)。
- 已安装 [Helm](https://helm.sh/docs/intro/install/)。




## 操作步骤

### 安装 Traefik

本文提供以下在 TKE 集群上安装 Traefik 为例，完整安装方法请参见 [官方文档](https://doc.traefik.io/traefik/getting-started/install-traefik/#use-the-helm-chart)。

1. 执行以下命令，添加 Traefik 的 Helm chart repo 源。示例如下：
```bash
 helm repo add traefik https://helm.traefik.io/traefik
```
2. 准备安装配置文件 `values-traefik.yaml`。示例如下：
<dx-codeblock>
:::  yaml
providers: 
  kubernetesIngress: 
    publishedService: 
      enabled: true # 让 Ingress 的外部 IP 地址状态显示为 Traefik 的 LB IP 地址
additionalArguments: 
- "--providers.kubernetesingress.ingressclass=traefik" # 指定 ingress class 名称 
- "--log.level=DEBUG" 
service: 
  annotations: 
    service.cloud.tencent.com/direct-access: "true" # 网关类的应用建议使用 LB 直通 Pod (绕过 NodePort)。若使用 VPC-CNI 与 Global Router 两种网络模式混用，用此注解来显示声明 LB 直绑 Pod (绕过 NodePort); 若创建集群时就选的 VPC-CNI 网络模式，则不需要显示声明 (默认 LB 直通 Pod)。详情请参见官方文档 https://cloud.tencent.com/document/product/457/48793
    service.kubernetes.io/tke-existed-lbid: lb-lb57hvgl # 用此注解绑定提前创建好的 LB，使得即便 Traefik 日后重建，也能保证流量入口不变。若不指定此注解，默认自动创建新的 LB。详情请参见官方文档 https://cloud.tencent.com/document/product/457/45491
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
    tke.cloud.tencent.com/networks: "tke-route-eni" # 在 VPC-CNI 与 Global Router 两种网络模式混用的情况下，显示声明 Pod 要使用弹性网卡，与以下 eni-ip 的 request 与 limit 一起配合使用
resources: 
  requests: 
    tke.cloud.tencent.com/eni-ip: "1"
  limits: 
    tke.cloud.tencent.com/eni-ip: "1"
:::
</dx-codeblock>

 >? 完整的默认配置可执行 `helm show values traefik/traefik` 命令查看。
3. 执行以下命令将 Traefik 安装到 TKE 集群。示例如下：
```bash
kubectl create ns ingress
helm upgrade --install traefik -f values-traefik.yaml traefik/traefik
```
4. 执行以下命令，获取流量入口的 IP 地址（如下为 EXTERNAL-IP 字段）。示例如下：
```bash
$ kubectl get service -n ingress
NAME      TYPE           CLUSTER-IP       EXTERNAL-IP     PORT(S)                      AGE
traefik   LoadBalancer   172.22.252.242   49.233.239.84   80:31650/TCP,443:32288/TCP   42h
```



### 使用 Ingress

Traefik 支持使用 Kubernetes 的 Ingress 资源作为动态配置，可直接在集群中创建 Ingress 资源用于对外暴露集群，需要加上指定的 Ingress class（安装 Traefik 时定义）。示例如下：

<dx-codeblock>
:::  yaml
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
:::
</dx-codeblock>

>! TKE 暂未将 Traefik 产品化，无法直接在 TKE 控制台进行可视化创建 Ingress，需要使用 YAML 进行创建。

### 使用 IngressRoute

Traefik 不仅支持标准的 Kubernetes Ingress 资源，也支持 Traefik 特有的 CRD 资源，例如 IngressRoute，可以支持更多 Ingress 不具备的高级功能。IngressRoute 使用示例如下：

<dx-codeblock>
:::  yaml
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
:::
</dx-codeblock>

>?Traefik 更多用法请参见 [Traefik 官方文档](https://doc.traefik.io/traefik/routing/providers/kubernetes-crd/)。
