## 下载 Demo 
|  Demo 语言  |  下载地址  | 说明 |
| --- | --- | --- |
| Python Demo（vm）|  [tsf_python_vm_demo](https://main.qcloudimg.com/raw/7a47d828d43dc5fa905ab8960db687b9/tsf_python_vm_demo-1225.tar.gz) | -  |
| Python Demo（docker）| [tsf_python_docker_demo](https://main.qcloudimg.com/raw/b4a0a86d3eb11bcee368b3eccf6e3052/tsf_python_docker_demo-1225.tar.gz) | - |
| <nobr>.NET Demo（vm & docker）</nobr>| [tsf_mesh_demo_dotnet](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/tsf_mesh_demo_dotnet.zip) | 其中 REAME.md 介绍了程序包和镜像两种构建方式|
| Java Demo（vm）| [tsf_mesh_vm_java_demo](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/mesh-demo/tsf-mesh-demo-java.zip) |- |
| Java Demo (docker)  |  [ tsf_mesh_docker_java_demo](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91/tsf%20mesh%20demo/tsf_mesh_demo_java_docker.zip)   |    -|
| PHP Demo（vm）| [tsf_php_vm_demo](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91/tsf%20mesh%20demo/tsf_php_vm_demo.zip) | 其中 README.md 介绍了健康检查的端口和路径 |
| Dubbo Demo（vm）| [tsf_mesh_dubbo_vm_demo](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/mesh-demo/tsf-mesh-dubbo-demo.tar.gz) | - |

>!Mesh 的部署和使用与语言无关，具体可参考 Python 使用方式进行改造。


## 调用说明
下文以 Python Demo 为例进行介绍。Python Demo 提供了3个应用，对应的服务名和应用监听端口为：
- user （8089）
- shop （8090）
- promotion （8091）

3个应用之间的调用关系是：`user -> shop -> promotion`，相互访问时可以用默认的80或者业务的真实端口（对应 Demo 中的 sidecarPort），如 shop 监听8090，user 访问 shop 可以用`shop:80/api/v6/shop/items`或者`shop:8090/api/v6/shop/items`。

>!Mesh 的调用链通过头传递实现。如果用户想要串联整个服务调用关系，需要在访问其他服务时，带上父调用的9个相关调用链头，具体示例如下：

<jump id="header"></jump>
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

// 填充调用链相关的头
def build_trace_headers(handler):
    retHeaders = {}
    for header in traceHeaders:
        if handler.headers.has_key(header):
            header_value = handler.headers.get(header)
            retHeaders[header] = header_value
    return retHeaders

// 访问 shop 服务的端口，使用默认的80，或者 shop 的真实端口8090
sidecarPort = 80
def do_GET(self):
    // 调用 shop 服务时填充父调用的调用链相关头
    if self.path == '/api/v6/user/create':
        print "headers are %s" % self.headers.keys()
        logger.info("headers are %s" % self.headers.keys())
        headers = common.build_trace_headers(self)
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

#### Spring Cloud 应用和 Mesh 应用调用打通 tracing
Spring Cloud 应用和 Mesh 应用相互调用时，如果要打通 tracing，需要在请求中传递调用链相关的 header（参考 [上文](#header)）。



## 工程目录
### 虚拟机工程目录
以 tsf_python_vm_demo 中的 userService 为例说明虚拟机应用工程目录。
- **userService.py 和 common.py**：Python 应用程序
- **start.sh**：启动脚本
- **stop.sh**：停止脚本
- **cmdline**：检查进程是否存活的文件
- **spec.yaml**：服务描述文件，具体解释请参考 [Mesh 开发使用指引](https://cloud.tencent.com/document/product/649/19049)
- **apis 目录**：存放 API 定义的目录， 具体解释请参考 [Mesh 开发使用指引](https://cloud.tencent.com/document/product/649/19049)

其中 star.sh、stop.sh、cmdline 的编写方法请参考 [上传程序包要求](https://cloud.tencent.com/document/product/649/30359)。


### 容器应用工程目录
以 tsf_python_docker_demo 中的 demo-mesh-user 为例说明容器应用工程目录。
> !您需要在容器启动后通过用户程序的启动脚本拷贝目录，不可以在 Dockerfile 中提前拷贝。

- **Dockerfile**：使用 userService 目录中 start.sh 脚本来启动 Python 应用。
- **userService**目录：基本结构类似 tsf_python_vm_demo 中 userService 目录，但是没有 stop.sh 和 cmdline 文件。
- **start.sh**：应用的启动脚本，user demo 的启动脚本如下：
```shell
#! /bin/bash
cp /root/app/userService/spec.yaml /opt/tsf/app_config/
cp -r /root/app/userService/apis /opt/tsf/app_config/
cd /root/app/userService/
python ./userService.py 80 1>./logs/user.log 2>&1
```
脚本说明：
- 应用工作目录为`/root/app/userService/`，应用日志目录为`/root/app/userService/logs/user.log`。
- 第2行：创建`/opt/tsf/app_config/apis`目录，并将`spec.yaml`文件拷贝到`/opt/tsf/app_config/`中。
- 第3行：将`apis`目录拷贝到`/opt/tsf/app_config/`中。
- 第5行：启动 user 应用。


