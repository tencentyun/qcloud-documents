使用 istio ，在集群中定义了 `VirutualService`，但测试发现定义的规则似乎没有生效，通常是一些配置问题，本文列举一下常见的可能原因。

## 集群内访问：gateway 字段没有显式指定 “mesh”

如果 `VirutualService` 没有指定 `gateways` 字段，实际隐含了一层意思，istio 会默认加上一个叫 “mesh” 的保留 Gateway，表示集群内部所有 Sidecar，也就表示此 `VirutualService` 规则针对集群内的访问生效。

但如果指定了 `gateways` 字段，istio 不会默认加上 “mesh”，如：

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: productpage
spec:
  gateways:
  - istio-test/test-gateway
  hosts:
  - bookinfo.example.com
  http:
  - route:
    - destination:
        host: productpage
        port:
          number: 9080
```

这个表示此 `VirualService` 规则仅对 `istio-test/test-gateway` 这个 Gateway 生效，如果是在集群内访问，流量不会经过这个 Gateway，所以此规则也就不会生效。

那如果要同时在集群内也生效该怎么做呢？答案是给 `gateways` 显式指定上 “mesh”：

```yaml
  gateways:
  - istio-test/test-gateway
  - mesh
```

表示此 `VirutualService` 不仅对 `istio-test/test-gateway` 这个 Gateway 生效，也对集群内部访问生效。

参考 [istio 官方文档](https://istio.io/latest/docs/reference/config/networking/virtual-service/#VirtualService) 对此字段的解释：

![img](https://main.qcloudimg.com/raw/58da5f89006e47248aeb7621899a87ab.png)

值得注意的是，从集群内访问一般是直接访问 service 名称，这里 `hosts` 就需要加上访问集群内的 service 名称：

```yaml
hosts:
- bookinfo.example.com
- productpage
```

## 通过 ingressgateway 访问: hosts 定义错误

若从 ingressgateway 访问，需要确保 `Gateway` 和 `VirtualService` 中的 hosts 均包含实际访问用到的 `Host` 或使用通配符能匹配得上，通常是外部域名。

只要有一方 hosts 没定义正确，都可能导致 `404 Not Found`，正确示例：

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: test-gateway
  namespace: istio-test
spec:
  selector:
    app: istio-ingressgateway
    istio: ingressgateway
  servers:
  - port:
      number: 80
      name: HTTP-80-www
      protocol: HTTP
    hosts:
    - bookinfo.example.com # 这里定义外部访问域名
  
---

apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: productpage
spec:
  gateways:
  - istio-test/test-gateway
  hosts:
  - bookinfo.example.com  # 这里也要定义外部访问域名
  http:
  - route:
    - destination:
        host: productpage
        port:
          number: 9080
```
