Envoy 缺省会把 http header 的 key 转换为小写，例如有一个 http header `Test-Upper-Case-Header: some-value`，经过 envoy 代理后会变成 `test-upper-case-header: some-value`。这个在正常情况下没问题，[RFC 2616](https://www.ietf.org/rfc/rfc2616.txt) 规范也说明了处理 HTTP Header 是大小写不敏感的。

## 依赖大小写的场景

通常 header 转换为小写不存在规范问题，但有些情况下对 header 大小写敏感会存在以下问题，例如：
- 业务解析 header 依赖大小写。
- 使用的 SDK 对 Header 大小写敏感，如读取 `Content-Length` 来判断 response 长度时依赖首字母大写。

## Envoy 支持的规则

Envoy 只支持两种规则：
- 全小写（默认使用的规则）。例如：`test-upper-case-header: some-value`
- 首字母大写（默认没有启用）。例如：`Test-Upper-Case-Header: some-value`


如果应用的 http header 的大小写完全没有规律，则无法兼容。例如：`Test-UPPER-CASE-Header: some-value`



## 规避方案

规避方案为强制指定为 TCP 协议。将服务声明为 TCP 协议，不让 istio 进行七层处理，也就不会更改 http header 大小写了，但需要注意的是同时也会丧失 istio 的七层能力。

如果服务在集群内，可以在 Service 的 port 名称中带上 “tcp” 前缀，如下所示：

```yaml
kind: Service
metadata:
  name: myservice
spec:
  ports:
  - number: 80
    name: tcp-web # 指定该端口协议为 tcp
```

如果服务在集群外，可以通过一个类似如下 ServiceEntry 将服务强制指定为 TCP Service，以避免 envoy 对其进行七层的处理:

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: ServiceEntry
metadata:
  name: qcloud-cos
spec:
  hosts:
  - "private-1251349835.cos.ap-guangzhou.myqcloud.com"
  location: MESH_INTERNAL
  addresses:
  - 169.254.0.47
  ports:
  - number: 80
    name: tcp
    protocol: TCP
  resolution: DNS
```

更多协议指定方式请参见 [为服务显式指定协议](https://imroc.cc/istio/best-practice/specify-protocol/)。

## 最佳实践 

如果希望 Envoy 对某些请求开启 Header 首字母大写的规则，可以使用 EnvoyFilter 指定 Header 规则为首字母大写。示例如下：

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: EnvoyFilter
metadata:
  name: http-header-proper-case-words
  namespace: istio-system
spec:
  configPatches:
  - applyTo: NETWORK_FILTER # http connection manager is a filter in Envoy
    match:
      # context omitted so that this applies to both sidecars and gateways
      listener:
        name: XXX # 指定 cos使用的listener name，可以从config_dump中查询到
        filterChain:
          filter:
            name: "envoy.http_connection_manager"
    patch:
      operation: MERGE
      value:
        name: "envoy.http_connection_manager"
        typed_config:
          "@type": "type.googleapis.com/envoy.config.filter.network.http_connection_manager.v2.HttpConnectionManager"
          http_protocol_options:
            header_key_format:
              proper_case_words: {}
```

>! 需替换 `listener name`。

## 建议

应用程序应遵循 [RFC 2616](https://www.ietf.org/rfc/rfc2616.txt) 规范，对 Http Header 的处理采用大小写不敏感的原则。

