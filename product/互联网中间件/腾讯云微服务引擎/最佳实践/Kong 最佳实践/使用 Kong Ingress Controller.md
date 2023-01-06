

## 操作场景
Kong 通过 Ingress Controller 实现为 Kubernetes Service 配置插件、健康检查、负载均衡等功能。通过整合 Kong Ingress Controller，Kong 可直接关联到 Kubernetes 整个生命周期，Ingress Controller 将监听容器集群变化，并更新 Kong 的配置，以便能正确代理所有的流量，免去人工管理的困扰。

## 前提条件
- [已创建云原生 API 网关实例](https://cloud.tencent.com/document/product/1364/72495)。
- 已购买腾讯云容器服务，包括 [TKE 标准集群](https://cloud.tencent.com/document/product/457/31697) 或 [TKE Serverless 集群](https://cloud.tencent.com/document/product/457/39809)。

## 操作步骤
### 步骤1：启用 Kong Ingress Controller
1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。
2. 在左侧导航栏，单击 kong，进入 kong 网关实例列表页面。
3. 单击目标实例的“ID/名称”，进入实例详情页面。
4. 在基本信息页面。展示 Kong Ingress Controller 当前状态，默认为关闭。
5. 单击当前状态后的**编辑**， 选择对接集群类型和集群信息，单击**确定**，即启用 Kong Ingress Controller。
6. 确认当前状态变更为**已开启**，同时展示选择的容器集群信息。
7. 修改 Kubernetes Ingress 资源中的 ingress.class 为 kong，创建对应 Ingress 规则。
<dx-alert infotype="notice" title="">
对于 apiVersion 为 v1beta1 和 v1 版本的 Ingress 资源，配置方式有所不同，请参考如下示例进行配置。有关不同版本的详细区别，请参见 [Kong 官方文档说明](https://docs.konghq.com/kubernetes-ingress-controller/latest/concepts/ingress-versions/)。
</dx-alert>
<ul><li>对于 apiVersion 为 v1beta1 版本的 Ingress 资源，请参考如下示例进行配置：</li>
<dx-codeblock>
:::  yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: demo
  annotations:
    kubernetes.io/ingress.class: kong
spec:
  rules:
  - http:
      paths:
      - path: /tse
        backend:
          serviceName: nginx
          servicePort: 80

:::
</dx-codeblock>
<li>对于 apiVersion 为 v1 版本的 Ingress 资源，请参考如下示例进行配置：</li>
<dx-codeblock>
:::  yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: demo-v1
  annotations:
    konghq.com/plugins: "httpbin-auth"
spec:
  ingressClassName: kong
  rules:
  - http:
      paths:
      - path: /demo-v1
        pathType: Prefix
        backend:
          service:
           name: nginx
           port:
             number: 80

:::
</dx-codeblock>
</ul>
8. 单击实例 访问控制 页，登录 Konga 控制台，查看是否已生成对应的 Upstream 和 Service。
![](https://qcloudimg.tencent-cloud.cn/raw/092ed94196871086361d09ce22a3d1f3.png)
![](https://qcloudimg.tencent-cloud.cn/raw/6c68bb4c7300042bb61b84ca751e9c3d.png)

### 步骤2：停止 Kong Ingress Controller

1. 在 kong 实例详情页，查看基本信息 > Kong Ingress Controller 卡片，当前状态为**已开启**。
2. 单击当前状态后的**编辑**，单击**确定**，停止 Kong Ingress Controller。
>!停止后，kong 不再监听容器集群变化。
3. 确认当前状态变更为**关闭**。
