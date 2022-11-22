## 操作场景

本文通过一个 demo 进行 Golang 应用接入微服务引擎托管的 PolarisMesh 治理中心的全流程操作演示，帮助您快速了解如何在 CVM 使用 DNS 协议来体验北极星网格的就近路由能力。

## 前提条件

- 已创建 PolarisMesh 北极星网格，请参见 [创建 PolarisMesh 治理中心](https://cloud.tencent.com/document/product/1364/65866)。
- 下载 Github 的 [demo 源码](https://github.com/polarismesh/polaris-go/tree/main/examples/route/nearby) 到本地并解压。
- 本地编译构建打包机器环境已安装了 golang 环境，并且能够访问 Github。
- 下载 Github 的 [polaris-sidecar-local_${VERSION}](https://github.com/polarismesh/polaris-sidecar/releases) 安装包。
- 根据您自身的业务，已准备好业务部署的 CVM。
  - **虚拟机部署**已创建 CVM 虚拟机，请参见 [创建 CVM 虚拟机](https://cloud.tencent.com/document/product/213/2936)。

## 操作步骤

1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。
2. 在**北极星网格**下的 **polarismesh** 页面，单击页面左上方下拉列表，选择目标地域。
3. 单击目标引擎的“ID”，进入基本信息页面。
4. 查看访问地址，Golang 应用访问使用 gRPC 端口（8091）：
![](https://qcloudimg.tencent-cloud.cn/raw/e7dc5ac5f7c76a316ae68b667d8a365f.png)
5. 修改 demo 中的注册中心地址
 1. 在下载到本地的 [demo 源码](https://github.com/polarismesh/polaris-go/tree/main/examples/route/nearby/provider) 目录下，找到`nearby/provider/polaris.yaml`文件
 - 添加微服务引擎北极星网格地址到项目配置文件中。
<dx-codeblock>
:::  yaml
   global:
     serverConnector:
       addresses:
         - 10.0.4.6:8091
     location:
       # 设置 polaris-go 进程地理信息的提供插件为 腾讯云 插件
       # 如果当前进程在CVM或者TKE中，则能够自动获取当前进程所在的位置信息
       #
       # 如果自动获取失败，则可以设置插件为 env，然后在 linux 中注入以下环境变量
       # POLARIS_INSTANCE_ZONE: 设置 zone 信息, 例如 ap-guangzhou
       # POLARIS_INSTANCE_CAMPUS: 设置 IDC 信息, 例如 ap-guangzhou-3
       provider: qcloud
:::
</dx-codeblock> 
6. 将源码编译成可执行程序。
  1. 在 provider 这个目录下，打开 cmd 命令，执行以下命令，对项目进行编译：
    - 编译 provider：`CGO_ENABLED=0 go build -ldflags "-s -w" -o provider`
    - 编译成功后，生成如下表所示的二进制包。
<table>
<tr>
<th>软件包所在目录</th>
<th>软件包名称</th>
<th>说明</th>
</tr>
<tr>
<td> \route\nearby\provider</td>
<td>provider </td>
<td>服务生产者</td>
</tr>
</table>
 - 将 provider 的二进制以及 polaris-sidecar-local-${VERSION} 安装包上传到不同的 CVM 实例中，这里假定上传的路径均为/data/polaris/golang_examples。
7. 部署 provider 微服务应用以及 polaris-sidecar。
 1. **虚拟机部署**部署 provider 微服务应用。
    - 上传二进制文件以及配置文件（polaris.yaml）至 CVM 实例。
    - 执行启动命令进行启动：
<dx-codeblock>
:::  shell
    ./[二进制文件名称]
:::
</dx-codeblock>
 2. **虚拟机部署**部署 polaris-sidecar。
    - 解压 polaris-sidecar-local-${VERSION} 安装包。
    - 进入安装包目录，执行安装命令，由于 polaris-sidecar 会监听 53 端口，因此需要使用 root 权限进行启动以及需要确保 53 端口没有被监听。
<dx-codeblock>
:::  shell
    bash install-linux.sh -s "10.0.4.6:8091"
:::
</dx-codeblock>
8. 修改 polaris-sidecar 的地址插件并重启 polaris-sidecar。
 1. **配置文件路径信息**：polaris-sidecar-install/polaris-sidecar-release_${VERSION}/polaris.yaml
<dx-codeblock>
:::  yaml
   global:
     serverConnector:
       addresses:
         - 10.0.4.6:8091
     location:
       # 设置 polaris-go 进程地理信息的提供插件为 腾讯云 插件
       # 如果当前进程在CVM或者TKE中，则能够自动获取当前进程所在的位置信息
       #
       # 如果自动获取失败，则可以设置插件为 env，然后在 linux 中注入以下环境变量
       # POLARIS_INSTANCE_ZONE: 设置 zone 信息, 例如 ap-guangzhou
       # POLARIS_INSTANCE_CAMPUS: 设置 IDC 信息, 例如 ap-guangzhou-3
       provider: qcloud
:::
</dx-codeblock> 
 2. **重启** polaris-sidecar。
	 - 进入 **polaris-sidecar-install/polaris-sidecar-release_${VERSION}**
	 - 执行 shell 命令
<dx-codeblock>
:::  shell
    bash tool/stop.sh; bash tool/start.sh
:::
</dx-codeblock>
9.  确认部署结果。
 1. 进入前面提到的微北极星网格实例页面。
 - 选择**服务管理** > **服务列表**，查看微服务 RouteNearbyEchoServer 的实例数量
     - 若实例数量值不为0，则表示已经成功接入微服务引擎
     - 若实例数量为0，或者找不到 RouteNearbyEchoServer 服务名，则表示微服务应用接入微服务引擎失败。
![](https://qcloudimg.tencent-cloud.cn/raw/7f46cd9aabfbfba93ac3e8bc7bbfbe4b.png)
 - 开启 RouteNearbyEchoServer 的就近路由。
![](https://qcloudimg.tencent-cloud.cn/raw/7f46cd9aabfbfba93ac3e8bc7bbfbe4b.png)
10. 为 RouteNearbyEchoServer 创建服务别名 routenearby.echoserver。
![](https://qcloudimg.tencent-cloud.cn/raw/3d542768f5d3e89396c6ac679604dc5f.png)
11. 调用 provider 的 HTTP 接口，执行 http 调用，其中`${app.port}`替换为 provider 的监听端口（默认为28080），`${add.address}`则替换为 provider 的域名信息。
<dx-codeblock>
:::  shell
   curl -L -X GET 'http://routenearby.echoserver.default:28080/echo'
   预期返回值：Hello, I'm RouteNearbyEchoServer Provider, MyLocInfo's : xxx, host : xxx:xxx
:::
</dx-codeblock>  

