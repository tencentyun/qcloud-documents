## 各类型 Ingress Controllers 介绍

### 应用型 CLB

应用型 CLB 是基于腾讯云负载均衡器 CLB 实现的 TKE Ingress Controller，可以配置实现不同 URL 访问到集群内不同的 Service。CLB 直接将流量通过 NodePort 转发至 Pod（CLB 直连 Pod 时直接转发到 Pod），一条 Ingress 配置绑定一个 CLB 实例（IP），适合仅需做简单路由管理，对 IP 地址收敛不敏感的场景。详情可参见 [CLB 类型 Ingress](https://cloud.tencent.com/document/product/457/45685)。

### Istio Ingress Gateway

基于腾讯云负载均衡器 CLB 和 Istio Ingress Gateway（由腾讯云服务网格 TCM 提供）的 Ingress Controller，控制面与相关支撑组件由腾讯云维护，集群内仅需容器化部署执行流量转发的数据面，可使用原生 Kubernetes Ingress 或提供更多精细化流量管理能力的 [Istio API](https://istio.io/latest/docs/concepts/traffic-management/)。CLB 后增加了一层代理（envoy），适合对接入层路由管理有更多诉求，有 IP 地址收敛诉求，有跨集群、异构部署服务入口流量管理诉求的场景。

### 专享型 API 网关

专享型 API 网关是基于腾讯云 API 网关专享实例实现的 TKE Ingress Controller，适用于有多个 TKE 集群，需要统一接入层的场景、以及对接入层有认证、流控等诉求的场景。详情可参见 [API 网关类型 Ingress](https://cloud.tencent.com/document/product/457/65124)。API Gateway Ingress 主要有以下优势：
- API 网关直接连接 TKE 集群的 Pod，无任何中间节点。
- 一个 API 网关 TKE 通道可以同时对接多个 TKE 服务，多个服务间采用加权轮询算法分配流量。
- 支持 API 网关提供的认证鉴权、流量控制、灰度分流、缓存、熔断降级等高级能力拓展。
- 采用 API 网关专享实例支撑，底层物理资源由用户独享，性能稳定，SLA 高。


### Nginx Ingress Controller

Nginx Ingress Controller 是基于腾讯云负载均衡器 CLB 和 Nginx 反向代理（容器化部署在集群内）的 Ingress Controller，通过 [Annotations](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/annotations/) 扩展了原生 Kubernetes Ingress 的功能。CLB 后增加了一层代理（nginx），适合对接入层路由管理有更多诉求，及有 IP 地址收敛诉求的场景。详情可参见 [Nginx 类型 Ingress](https://cloud.tencent.com/document/product/457/50502)。

## 各类型 Ingress Controllers 功能对比

<table>
<thead>
<tr>
<th>模块</th>
<th>功能</th>
<th>应用型 CLB</th>
<th>Istio Ingress Gateway（由腾讯云服务网格 TCM 提供）</th>
<th>专享型 API 网关</th>
<th>Nginx Ingress Controller</th>
</tr>
</thead>
<tbody><tr>
<th rowspan=5>流量管理</th>
<td>支持协议</td>
<td>http，https</td>
<td>http，https，http2，grpc，tcp，tcp + tls</td>
<td>http，https，http2, grpc</td>
<td>http，https，http2，grpc，tcp，udp</td>
</tr>
<tr>
<td>IP 管理</td>
<td>一条 Ingress 规则对应一个 IP（CLB）</td>
<td>多条 Ingress 规则对应一个 IP（CLB），IP 地址收敛</td>
<td>多条 Ingress 规则对应一个 IP（专享型 API 网关），IP 地址收敛</td>
<td>多条 Ingress 规则对应一个 IP（CLB），IP 地址收敛</td>
</tr>
<tr>
<td>特征路由</td>
<td>host，URL</td>
<td>更多特征支持：header、method、query parameter 等</td>
<td>更多特征支持：header、method、query parameter 等</td>
<td>更多特征支持：header、cookie 等</td>
</tr>
<tr>
<td>流量行为</td>
<td>不支持</td>
<td>支持，重定向，重写等</td>
<td>支持重定向，自定义请求，自定义响应</td>
<td>支持，重定向，重写等</td>
</tr>
<tr>
<td>地域感知负载均衡</td>
<td>不支持</td>
<td>支持</td>
<td>不支持</td>
<td>不支持</td>
</tr>
<tr>
<th>应用访问寻址</th>
<td>服务发现</td>
<td>单 Kubernetes 集群</td>
<td>多 Kubernetes 集群 + 异构服务</td>
<td>多 Kubernetes 集群</td>
<td>单 Kubernetes 集群</td>
</tr>
<tr>
<th rowspan=2>安全</th>
<td>SSL 配置</td>
<td>支持</td>
<td>支持</td>
<td>支持</td>
<td>支持</td>
</tr>
<tr>
<td>认证授权</td>
<td>不支持</td>
<td>支持</td>
<td>支持</td>
<td>支持</td>
</tr>
<tr>
<th rowspan=3>可观测性</th>
<td>监控指标</td>
<td>支持（需要在 CLB 中查看）</td>
<td>支持（云原生监控、云监控）</td>
<td>支持（需要在 API 网关中查看）</td>
<td>支持（云原生监控）</td>
</tr>
<tr>
<td>调用追踪</td>
<td>不支持</td>
<td>支持</td>
<td>不支持</td>
<td>不支持</td>
</tr>
<td>组件运维</td>
<td>关联 CLB 已托管，仅需集群内运行 TKE Ingress Controller</td>
<td>控制面已托管，需集群内运行数据面 Ingress Gateway</td>
<td>Kubernetes集群内不需要运行管控面，只需要开启集群内网访问功能</td>
<td>需集群内运行 Nginx Ingress Controller（控制面 + 数据面）</td>
</tr>
</tbody></table>

