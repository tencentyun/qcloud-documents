istio 中 http 请求，envoy 返回 431 异常状态码：

```txt
HTTP/1.1 431 Request Header Fields Too Large
```

## 原因分析

此状态码说明 http 请求 header 大小超限了，默认限制为60KiB，由 `HttpConnectionManager` 配置的 `max_request_headers_kb` 字段决定，最大可调整到96KiB：
![](https://qcloudimg.tencent-cloud.cn/raw/63489f6754a9d767518c733e347d33e4.png)

## 解决方案

可以通过 EnvoyFilter 调整 `max_request_headers_kb` 字段来提升 header 大小限制。

EnvoyFilter 示例（istio 1.6 验证通过）：

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: EnvoyFilter
metadata:
  name: max-header
  namespace: istio-system
spec:
  configPatches:
  - applyTo: NETWORK_FILTER
    match:
      context: ANY
      listener:
        filterChain:
          filter:
            name: "envoy.http_connection_manager"
    patch:
      operation: MERGE
      value:
        typed_config:
          "@type": "type.googleapis.com/envoy.config.filter.network.http_connection_manager.v2.HttpConnectionManager"
          max_request_headers_kb: 96
```

高版本兼容上面的 v2 配置，但建议用 v3 的 配置（istio 1.8验证通过）：

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: EnvoyFilter
metadata:
  name: max-header
  namespace: istio-system
spec:
  configPatches:
  - applyTo: NETWORK_FILTER
    match:
      context: ANY
      listener:
        filterChain:
          filter:
            name: "envoy.http_connection_manager"
    patch:
      operation: MERGE
      value:
        typed_config:
          "@type": "type.googleapis.com/envoy.extensions.filters.network.http_connection_manager.v3.HttpConnectionManager"
          max_request_headers_kb: 96
```

若 header 大小超过96KiB，建议将这部分数据放到 body。
