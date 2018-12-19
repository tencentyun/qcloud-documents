## 开发说明
下面以 Python 应用为例说明如何改造代码来接入 TSF。Python 服务代码本身不需要修改，只需要修改服务间调用的 host。
- 将原来的 IP:Port 替换为服务名。
- 端口使用 80 或者 443。
- 其他代码不做修改。

#### 示例
>?以下代码片段可参考 Demo 工程内 userService.py 。

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




## 服务定义和注册
在应用程序所在目录中设置创建 `spec.yaml` 文件，该文件用于描述服务信息。Sidecar 会通过服务描述文件将服务注册到服务注册中心。spec.yaml 格式如下：
```yaml
apiVersion: v1
kind: Application
spec:
  services:
    - name: user # service name
      ports:
        - targetPort: 8091 
        protocol: http
      healthCheck:
        path: /health
```


## API 定义和上报
TSF 支持 Mesh 应用 API 上报功能。在应用程序所在目录中创建 `apis` 目录，用来放置服务的 API 定义。一个服务对应一个 yaml 文件，文件名就是服务名，如 petstore 服务对应的配置是 petstore.yaml。API 遵循 [OPENAPI 3.0 规范](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md)。配置文件遵循 [样例参考](https://github.com/OAI/OpenAPI-Specification/blob/master/examples/v3.0/petstore.yaml)。user.yml 的 API 定义如下：
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

### 设置自定义标签
Mesh 支持通过 HTTP Header 设置自定义标签（标签可用于服务治理，参考 [服务治理](https://cloud.tencent.com/document/product/649/15548) 相关文档）。
以 Python 应用为例说明如何设置自定义标签。
```
>>> import requests
>>> url = 'https://api.github.com/some/endpoint'
>>> headers = {'custom-key': 'custom-value'}
>>> r = requests.get(url, headers=headers)
```
>?以上示例已经在依赖机器上安装了 requests 库。

