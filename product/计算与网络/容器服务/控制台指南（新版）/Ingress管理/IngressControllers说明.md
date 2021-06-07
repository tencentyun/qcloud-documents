
## 各类型 Ingress Controllers 介绍

### 应用型 CLB
应用型 CLB 是基于腾讯云负载均衡器 CLB 实现的 TKE Ingress Controller，可以配置实现不同 URL 访问到集群内不同的 Service。CLB 直接将流量通过 NodePort 转发至 Pod（CLB 直连 Pod 时直接转发到 Pod），一条 Ingress 配置绑定一个 CLB 实例（IP），适合仅需做简单路由管理，对 IP 地址收敛不敏感的场景。详情可参见 [CLB 类型 Ingress](https://cloud.tencent.com/document/product/457/45685)。

### Nginx Ingress Controller
Nginx Ingress Controller 是基于腾讯云负载均衡器 CLB 和 Nginx 反向代理（容器化部署在集群内）的 Ingress Controller，通过 [Annotations](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/annotations/) 扩展了原生 Kubernetes Ingress 的功能。CLB 后增加了一层代理（nginx），适合对接入层路由管理有更多诉求，及有 IP 地址收敛诉求的场景。详情可参见 [Nginx 类型 Ingress](https://cloud.tencent.com/document/product/457/50502)。


### Istio Ingress Gateway
Istio Ingress Gateway 是基于腾讯云负载均衡器 CLB 和 Istio Ingress Gateway（由腾讯云服务网格 TCM 提供）的 Ingress Controller，控制面与相关支撑组件由腾讯云维护，集群内仅需容器化部署执行流量转发的数据面，可使用原生 Kubernetes Ingress 或提供更多精细化流量管理能力的 [Istio API](https://istio.io/latest/docs/concepts/traffic-management/)。CLB 后增加了一层代理（envoy），适合对接入层路由管理有更多诉求，有 IP 地址收敛诉求，有跨集群、异构部署服务入口流量管理诉求的场景。

## 各类型 Ingress Controllers 功能对比

| 模块         | 功能             | 应用型 CLB                                             | Nginx Ingress Controller                                 | Istio Ingress Gateway（由腾讯云服务网格 TCM 提供） |
| ------------ | ---------------- | ------------------------------------------------------ | -------------------------------------------------------- | -------------------------------------------------- |
| 流量管理     | 支持协议         | http，https                                            | http，https，http2，grpc，tcp，udp                       | http，https，http2，grpc，tcp，tcp + tls           |
| 流量管理     | IP 管理          | 一条 Ingress 规则对应一个 IP（CLB）                    | 多条 Ingress 规则对应一个 IP（CLB），IP 地址收敛         | 多条 Ingress 规则对应一个 IP（CLB），IP 地址收敛   |
| 流量管理     | 特征路由         | host，URL                                              | 更多特征支持：header、cookie 等                          | 更多特征支持：header、method、query parameter 等   |
| 流量管理     | 流量行为         | 不支持                                                 | 支持，重定向，重写等                                     | 支持，重定向，重写等                               |
| 流量管理     | 地域感知负载均衡 | 不支持                                                 | 不支持                                                   | 支持                                               |
| 应用访问寻址 | 服务发现         | 单 Kubernetes 集群                                     | 单 Kubernetes 集群                                       | 多 Kubernetes 集群 + 异构服务                      |
| 安全         | SSL 配置         | 支持                                                   | 支持                                                     | 支持                                               |
| 安全         | 认证授权         | 不支持                                                 | 支持                                                     | 支持                                               |
| 可观测性     | 监控指标         | 支持（需要在 CLB 中查看）                                | 支持（云原生监控）                                       | 支持（云原生监控、云监控）                         |
| 可观测性     | 调用追踪         | 不支持                                                 | 不支持                                                   | 支持                                               |
| 可观测性     | 组件运维         | 关联 CLB 已托管，仅需集群内运行 TKE Ingress Controller | 需集群内运行 Nginx Ingress Controller（控制面 + 数据面） | 控制面已托管，需集群内运行数据面 Ingress Gateway   |

