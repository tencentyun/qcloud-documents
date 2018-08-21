## 获取 Demo

[Demo for Python](https://main.qcloudimg.com/raw/f84f0735204c8f24fcc3f21519a8740f/tsf_python_vm_demo.zip) 提供了 3 个 Python 应用及 Dockerfile。3 个应用对应的服务名分别是：
  - user
  - shop
  - promotion

3 个应用之间的调用关系是：`user => shop => promotion`




## 开发说明

下面以 Python 应用说明如何改造来接入 TSF。Python 服务代码本身不需要修改，只需要修改服务间调用的 host。

- 将原来的 IP:Port 替换为服务名。
- 端口使用 80 或者 443。
- 其他代码不做修改

#### 示例

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

> **注意：**以上代码片段可参考 Demo 工程内 userService.py 。
