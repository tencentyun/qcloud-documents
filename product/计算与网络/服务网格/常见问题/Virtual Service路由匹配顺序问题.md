在写 VirtualService 路由规则时，通常会 match 各种不同路径转发到不同的后端服务，有时候不小心命名冲突了，导致始终只匹配到前面的服务，例如：

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: test
spec:
  gateways:
  - default/example-gw
  hosts:
  - 'test.example.com'
  http:
  - match:
    - uri:
        prefix: /usrv
    rewrite:
      uri: /
    route:
    - destination:
        host: usrv.default.svc.cluster.local
        port:
          number: 80
  - match:
    - uri:
        prefix: /usrv-expand
    rewrite:
      uri: /
    route:
    - destination:
        host: usrv-expand.default.svc.cluster.local
        port:
          number: 80
```

istio 匹配是按顺序匹配，不像 nginx 那样使用最长前缀匹配。这里使用 prefix 进行匹配，第一个是 `/usrv`，表示只要访问路径前缀含 `/usrv` 就会转发到第一个服务，由于第二个匹配路径 `/usrv-expand` 本身也属于带 `/usrv` 的前缀，所以永远不会转发到第二个匹配路径的服务。

## 解决方案

这种情况可以调整下匹配顺序，如果前缀有包含的冲突关系，越长的放在越前面：

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: test
spec:
  gateways:
  - default/example-gw
  hosts:
  - 'test.example.com'
  http:
  - match:
    - uri:
        prefix: /usrv-expand
    rewrite:
      uri: /
    route:
    - destination:
        host: usrv-expand.default.svc.cluster.local
        port:
          number: 80
  - match:
    - uri:
        prefix: /usrv
    rewrite:
      uri: /
    route:
    - destination:
        host: usrv.default.svc.cluster.local
        port:
          number: 80
```

也可以用正则匹配：

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: test
spec:
  gateways:
  - default/gateway
  hosts:
  - 'test.example.com'
  http:
  - match:
    - uri:
        regex: "/usrv(/.*)?"
    rewrite:
      uri: /
    route:
    - destination:
        host: nginx.default.svc.cluster.local
        port:
          number: 80
        subset: v1
  - match:
    - uri:
        regex: "/usrv-expand(/.*)?"
    rewrite:
      uri: /
    route:
    - destination:
        host: nginx.default.svc.cluster.local
        port:
          number: 80
        subset: v2
```
