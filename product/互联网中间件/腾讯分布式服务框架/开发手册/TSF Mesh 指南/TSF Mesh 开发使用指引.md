## 开发说明
本文将以 Python 应用为例说明如何改造代码来接入 TSF。您不需要修改 Python 服务代码，只需要修改服务间调用的 host。
- 将原来的 IP:Port 替换为服务名，如果不使用服务名调用，流量不会经过 sidecar 直接传递到被调服务，被调服务无法处理识别主调服务的服务名。
- 端口使用80或者业务真实的监听端口。
- 其他代码不做修改。

>?以下代码片段可参考 Demo 工程内 userService.py。

改造前：
```python
sidecarPort = 80
if common.sendAndVerify("127.0.0.1", sidecarPort, "/api/v6/shop/items", headers):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            msg = {"result":{"userId":"1234", "userName":"vincent"}}
            self.wfile.write(json.dumps(msg))
        else:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            msg = {"exception":"Error invoke %s" % "/api/v6/shop/items"}
            self.wfile.write(json.dumps(msg))
```

改造后：
```python
sidecarPort = 80
if common.sendAndVerify("shop", sidecarPort, "/api/v6/shop/items", headers):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            msg = {"result":{"userId":"1234", "userName":"vincent"}}
            self.wfile.write(json.dumps(msg))
        else:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            msg = {"exception":"Error invoke %s" % "/api/v6/shop/items"}
            self.wfile.write(json.dumps(msg))
```
可以看到，代码行中除了**访问方式发生变化（`127.0.0.1`变为`shop`）**外，其他都不需要改动。



## 服务定义和注册（必选）
**如果是虚拟机部署**，需要在应用程序所在目录中设置创建 `spec.yaml` 文件；**如果是容器部署**，需要在应用启动时，在`/opt/tsf/app_config`下写入 `spec.yaml` 文件，该文件用于描述服务信息。
Sidecar 会通过服务描述文件将服务注册到服务注册中心。
spec.yaml 格式如下：

```yaml
apiVersion: v1
kind: Application
spec:
  services:
  - name: user # 服务名
    ports:     	
    - targetPort: 8091 # 服务监听端口 
      protocol: http # 目前仅支持 http
    healthCheck:
      path: /health # 健康检查 URL
```

>!
- healthCheck 是健康检查的接口，请确认本地调用`curl -i -H 'Host: local-service' {ip}:{Port}/health`能返回200。
- `Host: local-service`是代理加的 header，业务如果对 Host 有检查（如 nginx 配置的 server_name），则需将 local-service 加到白名单。



## 服务间调用方式

### 1. 使用服务名来调用（推荐）

在 user 服务所在实例上执行 curl 命令，通过使用 `shop` 服务名进行访问。

```
curl shop:<shop端口>/api/v6/shop/order
```

### 2. 统一域名转发

> ？适用于 1.13.0 之后版本的 Mesh 应用

#### 使用场景

主要解决是，同一命名空间下，不同服务之间，希望采用统一的host，以及不同的url来进行访问。

比如：通过以下配置

```
Version: v1
kind: Application
spec:
  baseConfig:
    localCache:
      enable: true
  egressPorts:
    # 统一host域名
    host: "test.com"
    config:
      prefix: "/api/v6"
  services:
  - name: shop
    ports:
    - targetPort: 8090
      protocol: http
    healthCheck:
      path: /health
    tracing:
      randomSampling: 1.0
```

即可实现，访问 user 服务，可以通过curl http://test.com/api/v6/user/create来进行访问。

而访问 shop 服务，则可以通过curl http://test.com/api/v6/shop/query来进行访问。

#### 配置项说明

spec.yaml配置说明

```
Version: v1
kind: Application
spec:
  baseConfig:
    localCache:
      enable: true
  egressPorts:
    # 统一host域名
    host: "test.com"
    # 可选，配置参数
    config:
      # 可选，url前缀，适用于带固定前缀的URL路径，默认为"/"
      prefix: "/"
      # 可选，url后缀，适用于带固定后缀的URL路径，默认为空
      # 或者也适用于区分如/user以及/user1这样带相似字符串的URL
      suffix: 
  services:
  - name: shop
    ports:
    - targetPort: 8090
      protocol: http
    healthCheck:
      path: /health
    tracing:
      randomSampling: 1.0
```

#### 特殊场景说明

假如用户配置了API 路由能力，而且 API 的 PATH 刚好与服务的 PATH 重合，那么会优先匹配用户配置的 API 路由规则。



## API 定义和上报（可选）

TSF 支持 Mesh 应用 API 上报功能，用于 API 级别的服务治理，如路由、鉴权和限流等，不需要可以跳过。
**如果是虚拟机部署**，需要在应用程序所在目录中创建`apis`目录；**如果是容器部署**，需要在`/opt/tsf/app_config`下创建`apis`目录，该目录放置服务的 API 定义。
一个服务对应一个 yaml 文件，文件名即服务名，如 petstore 服务对应 petstore.yaml 配置。API 遵循 [OPENAPI 3.0 规范](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md)。配置文件遵循 [样例参考](https://github.com/OAI/OpenAPI-Specification/blob/master/examples/v3.0/petstore.yaml)。user.yml 的 API 定义如下：
```yaml
openapi: 3.0.0
info:
  version: "1.0.0"
  title: user service
paths:
  /api/v6/user/create:
    get:
      responses:
        '200':
           description: OK
        '401':
           description: Unauthorized
        '402':
           description: Forbidden
        '403':
           description: Not Found
  /api/v6/user/account/query:
    get:
      responses:
        '200':
           description: OK
        '401':
           description: Unauthorized
        '402':
           description: Forbidden
        '403':
           description: Not Found
  /health:
    get:
      responses:
        '200':
           description: OK
        '401':
           description: Unauthorized
        '402':
           description: Forbidden
        '403':
           description: Not Found
```



## 设置自定义标签 （可选）

Mesh 支持通过 HTTP Header 设置自定义标签（标签可用于服务治理，参考 [服务治理](https://cloud.tencent.com/document/product/649/15548) 相关文档）。
以 Python 应用为例说明如何设置自定义标签。

```
>>> import requests
>>> url = 'https://api.github.com/some/endpoint'
>>> headers = {'custom-key': 'custom-value'}
>>> r = requests.get(url, headers=headers)
```
>?以上示例已经在依赖机器上安装了 requests 库。



## 调用链 Header 传递（可选）

要实现 Mesh 应用调用链和服务依赖拓扑功能，需要在请求中带上 9 个相关 header。

```
// 9个调用链相关的头，具体说明见(https://www.envoyproxy.io/docs/envoy/v1.8.0/configuration/http_conn_man/headers.html?highlight=tracing)
traceHeaders = ['x-request-id',
                'x-trace-service',
                'x-ot-span-context',
                'x-client-trace-id',
                'x-b3-traceid',
                'x-b3-spanid',
                'x-b3-parentspanid',
                'x-b3-sampled',
                'x-b3-flags']
```

具体使用方法参考文档 [Mesh Demo 介绍](https://cloud.tencent.com/document/product/649/30436) 。
