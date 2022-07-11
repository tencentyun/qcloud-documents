## 操作场景

本文通过一个 demo 进行 dubbo-go 应用接入微服务引擎托管的 PolarisMesh 治理中心的全流程操作演示，帮助您快速了解如何使用服务治理中心。

## 前提条件

- 已创建 PolarisMesh 服务治理中心，请参见 [创建 PolarisMesh 治理中心](https://cloud.tencent.com/document/product/1364/65866)。
- 下载 Github 的 [demo 源码](https://github.com/polarismesh/examples/tree/main/dubbo3/dubbogo) 到本地并解压。
- 本地编译构建打包机器环境已安装了 golang 环境，并且能够访问 Github。
- 当前仅支持 dubbo-go 的接口注册模型。
- 根据您自身的业务，已准备好业务部署的资源，虚拟机部署和容器化部署选择其中一种方式即可。
  - **虚拟机部署**已创建 CVM 虚拟机，请参见 [创建 CVM 虚拟机](https://cloud.tencent.com/document/product/213/2936)。
  - **容器化部署**已创建 TKE 容器集群，请参见 [创建 TKE 集群](https://cloud.tencent.com/document/product/457/32189)。

## 操作步骤

1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。
2. 在**治理中心**下的 **polarismesh** 页面，单击页面左上方下拉列表，选择目标地域。
3. 单击目标引擎的“ID”，进入基本信息页面。
4. 查看访问地址，Dubbo-Go 应用访问使用 gRPC 端口（8091）：
![](https://qcloudimg.tencent-cloud.cn/raw/e7dc5ac5f7c76a316ae68b667d8a365f.png)
5. 修改 demo 中的注册中心地址
 1. 在下载到本地的 [demo 源码](https://github.com/polarismesh/examples/tree/main/dubbo3/dubbogo) 目录下，分别找到`dubbo\dubbogo\provider\dubbogo.yaml`以及`dubbo\dubbogo\consumer\dubbogo.yaml`文件
 - 添加微服务引擎服务治理中心地址到项目配置文件中（这里已`dubbo\dubbogo\provider\dubbogo.yaml`为例）。
<dx-codeblock>
:::  yaml
  dubbo:
    registries:
      polarisMesh:
        protocol: polaris
        address: 10.0.4.6:8091
        namespace: default
    consumer:
      references:
        UserProvider:
          protocol: dubbo
          interface: org.apache.dubbo.UserProvider.Test
        UserProviderWithCustomGroupAndVersion:
          protocol: dubbo
          interface: org.apache.dubbo.UserProvider.Test2
          version: myInterfaceVersion # dubbo interface version must be same with server
:::
</dx-codeblock>
6. 将源码编译成可执行程序。
   1. 分别在 consumer 和 provider 这2个目录下，打开 cmd 命令，执行以下命令，对项目进行编译：
     - 编译 consumer：`CGO_ENABLED=0 go build -ldflags "-s -w" -o consumer`
     - 编译 provider：`CGO_ENABLED=0 go build -ldflags "-s -w" -o provider`
  - 编译成功后，生成如表1所示的2个二进制包。
<table>
<tr>
<th>软件包所在目录</th>
<th>软件包名称</th>
<th>说明</th>
</tr>
<tr>
<td>dubbo3\dubbogo\provider</td>
<td>provider</td>
<td>服务生产者</td>
</tr>
<tr>
<td>dubbo3\dubbogo\consumer</td>
<td>consumer</td>
<td>服务消费者</td>
</tr>
</table>    
7. 部署 provider 和 consumer 微服务应用，虚拟机部署方式和容器化部署根据您业务实际的部署方式选择一种即可。
 1. **虚拟机部署**部署 provider 和 consumer 微服务应用。
    - 上传二进制包至 CVM 实例。
    - 执行启动命令进行启动：
<dx-codeblock>
:::  shell
   	# 进入provider目录
		cd /data/polaris/dubbogo_examples/provider
		# 设置配置文件目录
		export DUBBO_GO_CONFIG_PATH="./dubbogo.yml"
		# 运行 provider
		./provider
:::
</dx-codeblock>     
 2. **容器化部署**部署 provider 和 consumer 微服务应用。
    - 编写dockerfile生成镜像，参考：
<dx-codeblock>
:::  shell
    FROM golang:alpine
    WORKDIR /root
    ADD . /root
    ENTRYPOINT ./[二进制名称] [启动参数命令]
:::
</dx-codeblock>  
    - 通过 TKE 部署并运行镜像
8. 确认部署结果
 1. 进入前面提到的微服务治理中心实例页面。
 - 选择**服务管理** > **服务列表**，查看一下服务的实例数量：
    - 若实例数量值不为0，则表示已经成功接入微服务引擎
    - 若实例数量为0，或者找不到上述服务名，则表示`Dubbo-Go`应用接入微服务引擎失败。
![](https://qcloudimg.tencent-cloud.cn/raw/7cc1d0a8766e6a175ab10fc6e4dac517.png)
 - 调用 consumer 的 HTTP 接口
    - 执行 http 调用，其中`${app.port}`替换为 consumer 的监听端口（默认为18080），`${add.address}`则替换为 consumer 暴露的地址。
<dx-codeblock>
:::  shell
   curl -L -X GET 'http://${add.address}:${app.port}/echo'
   预期返回值：{"UserProvider":{"id":"A001","name":"Alex Stocks","age":18,"time":"2021-12-16T16:57:27.945+08:00"},"UserProviderWithCustomGroupAndVersion":{"id":"A001","name":"Alex Stocks from UserProviderWithCustomGroupAndVersion","age":18,"time":"2021-12-16T16:57:27.946+08:00"}}
:::
</dx-codeblock>


