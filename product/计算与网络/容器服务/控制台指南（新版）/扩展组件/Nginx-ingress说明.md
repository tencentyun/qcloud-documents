## 简介
### 组件介绍
Nginx 可以用作反向代理、负载平衡器和 HTTP 缓存。Nginx-ingress 组件是使用 Nginx 作为反向代理和负载平衡器的 Kubernetes 的 Ingress 控制器。您可以部署 Nginx-ingress 组件，在集群中使用 Nginx-ingress。

### 前置依赖
1. Kubernetes 版本建议在1.12版本及以上。
2. 建议您使用 TKE [节点池功能](https://cloud.tencent.com/document/product/457/43719)。
3. 建议您使用 TKE 云原生监控功能。
4. 建议您使用 [腾讯云日志服务 CLS](https://cloud.tencent.com/document/product/614)。

### 在集群内部署 Kubernetes 对象
在集群内部署 Nginx-ingress Add-on，将在集群内部署以下 Kubernetes 对象：

| Kubernetes 对象名称        | 类型         | 默认占用资源 | 所属 Namespaces |
| --------------------- | ---------- | ------ | ------------ |
| nginx-ingress  | Service | -      | 自定义设置 |
| nginx-ingress  | Configmap | -      | 自定义设置 |
| tke-ingress-nginx-controller-operator | Deployment | 0.13C   128M | kube-system |
| ingress-nginx-controller | Deployment/DaementSe t | 0.1C | kube-system |
| ingress-nginx-controller-hpa | HPA |  | kube-system |



### 相关参考文档
- [Nginx-ingress 概述](https://cloud.tencent.com/document/product/457/50502)
- [Nginx-ingress 安装](https://cloud.tencent.com/document/product/457/50503)
- [使用 Nginx-ingress 对象接入集群外部流量 ](https://cloud.tencent.com/document/product/457/50504)
- [Nginx-ingress 监控配置](https://cloud.tencent.com/document/product/457/50506)
- [Nginx-ingress 日志配置](https://cloud.tencent.com/document/product/457/50505)
