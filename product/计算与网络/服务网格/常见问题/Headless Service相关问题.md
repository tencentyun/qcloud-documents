## 服务间通过注册中心调用响应 404
#### 现象
传统服务（例如 Srping Cloud）迁移到 istio 后，服务间调用返回 404。


#### 原因
网格没有使用 Kubernetes 的服务发现，而是通过注册中心获取服务 IP 地址，服务间调用不经过域名解析，直接向获取到的目的 IP 发起调用。由于 istio 的 LDS 会拦截 headless service 中包含的 PodIP+Port 的请求，然后匹配请求 hosts，如果没有 hosts 或者 hosts 中没有这个 PodIP+Port 的 service 域名 (比如直接是 Pod IP)，就会匹配失败，最后返回 404。

#### 解决方案

  1. 注册中心不直接注册 Pod IP 地址，注册 service 域名。
  2. 客户端请求时带上 hosts（需要更新代码）。

## 负载均衡策略不生效

由于 istio 默认对 headless service 进行 passthrougth，使用 `ORIGINAL_DST` 转发，即直接转发到原始的目的 IP，不做任何的负载均衡，所以 `Destinationrule` 中配置的 `trafficPolicy.loadBalancer` 都不会生效，影响的功能包括：
- 会话保持（consistentHash）
- 地域感知（localityLbSetting）

#### 解决方案
解决方案为单独再创建一个 service（非 headless）。

## 访问不带 sidecar 的 headless service 失败

#### 现象
client（有sidecar）通过 headless service 访问 server (无sidecar)，访问失败，access log 中可以看到 response_flags 为 `UF,URX`。
- 原因: istio 1.5/1.6 对 headless service 支持有个 bug，不管 endpoint 有没有 sidecar，都固定启用 mtls，导致没有 sidecar 的 headless 服务(如 redis) 访问被拒绝 (详见 [#21964](https://github.com/istio/istio/issues/21964)) ，更多细节可参考 [Istio 运维实战系列（2）：让人头大的『无头服务』-上](https://zhaohuabing.com/post/2020-09-11-headless-mtls/)。


#### 解决方案


**方案1：**配置 `DestinationRule` 禁用 mtls

```yaml
kind: DestinationRule
metadata:
  name: redis-disable-mtls
spec:
  host: redis.default.svc.cluster.local
  trafficPolicy:
    tls:
      mode: DISABLE 
```

**方案2**：升级 istio 到1.7及其以上的版本

## Pod 重建后访问失败

#### 现象
client 通过 headless service 访问 server，当 server 的 pod 发生重建后，client 访问 server 失败，access log 中可以看到 response_flags 为 `UF,URX`。

#### 原因
istio 1.5对 headless service 支持的 bug。
  - client 通过 dns 解析 headless service，返回其中一个 Pod IP，然后发起请求。
  - envoy 检测到是 headless service，使用 `ORIGINAL_DST` 转发，即不做负载均衡，直接转发到原始的目的 IP。
  - 当 headless service 的 pod 发生重建，由于 client 与它的 sidecar (envoy) 是长连接，所以 client 侧的连接并没有断开。
  - 又由于是长连接，client 继续发请求并不会重新解析 dns，而是仍然发请求给之前解析到的旧 Pod IP。
  - 由于旧 Pod 已经销毁，Envoy 会返回错误 (503)。
  - 客户端并不会因为服务端返回错误而断开连接，后续请求继续发给旧的 Pod IP，如此循环，一直失败。
  - 更多详情参考 [Istio 运维实战系列（3）：让人头大的『无头服务』-下](https://zhaohuabing.com/post/2020-09-19-headless-mtls/)。

#### 解决方案
升级 istio 到1.6及其以上的版本，Envoy 在 Upstream 链接断开后会主动断开和 Downstream 的长链接。



