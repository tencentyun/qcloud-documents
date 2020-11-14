## Nginx-ingress说明
### 组件介绍
Nginx可以用作反向代理、负载平衡器和HTTP缓存。Nginx-ingress是使用NGINX作为反向代理和负载平衡器的Kubernetes的Ingress控制器。您可以部署Nginx-ingress组件，在集群中使用Nginx-ingress。
### 前置依赖
1. Kubernetes版本建议在1.12版本及以上。
2. 建议您使用节点池功能。
3. 建议您使用TKE云原生监控功能。
4. 建议您使用腾讯云日志服务CLS.

### 将在集群内部署的资源
在集群内部署 Nginx-ingress Add-on，将在集群内部署以下 Kubernetes 对象：

| Kubernetes 对象名称        | 类型         | 默认占用资源 | 所属 Namespaces |
| --------------------- | ---------- | ------ | ------------ |自定义设置  |
| nginx-ingress  | Service | /      | 自定义设置 |
| nginx-ingress  | Configmap | /      | 自定义设置 |



### 相关参考文档
1. [Nginx-ingress概述]()
2. [Nginx-ingress安装]()
3. [使用Nginx-ingress对象接入集群外部流量 ]()
4. [Nginx-ingress监控配置]()
5. [Nginx-ingress日志配置]()
6. [Nginx-ingress证书配置]()