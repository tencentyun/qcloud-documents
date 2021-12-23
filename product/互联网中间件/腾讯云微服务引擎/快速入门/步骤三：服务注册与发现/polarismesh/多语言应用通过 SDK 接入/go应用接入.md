## 操作场景

本文通过一个 demo 进行 Golang 应用接入微服务引擎托管的 PolarisMesh 治理中心的全流程操作演示，帮助您快速了解如何使用服务治理中心。

## 前提条件

- 已创建 PolarisMesh 服务治理中心，请参见 [创建 PolarisMesh 治理中心](https://cloud.tencent.com/document/product/1364/65866)。
- 下载 Github 的 [demo 源码](https://github.com/polarismesh/polaris-go/tree/main/examples/quickstart) 到本地并解压。
- 本地编译构建打包机器环境已安装了 golang 环境，并且能够访问 Github。
- 根据您自身的业务，已准备好业务部署的资源，虚拟机部署和容器化部署选择其中一种方式即可。
  - **虚拟机部署**已创建 CVM 虚拟机，请参见 [创建 CVM 虚拟机](https://cloud.tencent.com/document/product/213/2936)。
  - **容器化部署**已创建 TKE 容器集群，请参见 [创建 TKE 集群](https://cloud.tencent.com/document/product/457/32189)。

## 操作步骤

1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。
2. 在**治理中心**下的 **polarismesh** 页面，单击页面左上方下拉列表，选择目标地域。
3. 单击目标引擎的“ID”，进入基本信息页面。
4. 查看访问地址，Golang 应用访问使用 gRPC 端口（8091）：
![](https://qcloudimg.tencent-cloud.cn/raw/e7dc5ac5f7c76a316ae68b667d8a365f.png)
5. 修改 demo 中的注册中心地址
 1. 在下载到本地的 [demo 源码](https://github.com/polarismesh/polaris-go/tree/main/sample/quickstart) 目录下，分别找到`quickstart/consumer/polaris.yaml`以及`quickstart/provider/polaris.yaml`文件
 - 添加微服务引擎服务治理中心地址到项目配置文件中（这里已`quickstart/consumer/polaris.yaml`为例）。
<dx-codeblock>
:::  yaml
   global:
     serverConnector:
       addresses:
         - 10.0.4.6:8091
:::
</dx-codeblock> 
6. 将源码编译成可执行程序。
  1. 分别在 consumer 和 provider 这2个目录下，打开 cmd 命令，执行以下命令，对项目进行编译：

    - 编译 consumer：`CGO_ENABLED=0 go build -ldflags "-s -w" -o consumer`
    - 编译 provider：`CGO_ENABLED=0 go build -ldflags "-s -w" -o provider`
 - 编译成功后，生成如下表所示的2个二进制包。
<table>
<tr>
<th>软件包所在目录</th>
<th>软件包名称</th>
<th>说明</th>
</tr>
<tr>
<td> \examples\quickstart\provider</td>
<td>provider </td>
<td>服务生产者</td>
</tr>
<tr>
<td>\examples\quickstart\consumer</td>
<td>consumer </td>
<td>服务消费者</td>
</tr>
</table>
 - 分别将 consumer 以及 provider 的二进制上传到不同的 CVM 实例中，这里假定上传的路径均为/data/polaris/golang_examples。
7. 部署 provider 和 consumer 微服务应用，虚拟机部署方式和容器化部署根据您业务实际的部署方式选择一种即可。
 1. **虚拟机部署**部署provider和consumer微服务应用。
    - 上传二进制文件以及配置文件（polaris.yaml）至 CVM 实例。
    - 执行启动命令进行启动：
    <dx-codeblock>
    :::  shell
    ./[二进制文件名称]
    :::
    </dx-codeblock>
 2. **容器化部署**部署 provider 和 consumer 微服务应用。
    - 编写 dockerfile 生成镜像，参考：
    <dx-codeblock>
    :::  shell
    FROM golang:alpine
    WORKDIR /root
    ADD . /root
    ENTRYPOINT ./[二进制名称] [启动参数命令]
    :::
    </dx-codeblock>
    - 通过 TKE 部署并运行镜像。
9. 确认部署结果
 1. 进入前面提到的微服务治理中心实例页面。
 - 选择**服务管理** > **服务列表**，查看微服务 EchoServerGolang 的实例数量
    - 若实例数量值不为0，则表示已经成功接入微服务引擎
    - 若实例数量为0，或者找不到 EchoServerGolang 服务名，则表示微服务应用接入微服务引擎失败。
    ![](https://qcloudimg.tencent-cloud.cn/raw/7f46cd9aabfbfba93ac3e8bc7bbfbe4b.png)
 - 调用 consumer 的 HTTP 接口
    - 执行 http 调用，其中`${app.port}`替换为 consumer 的监听端口（默认为18080），`${add.address}`则替换为 consumer 暴露的地址。
    <dx-codeblock>
    :::  shell
   curl -L -X GET 'http://${add.address}:${app.port}/echo'
   预期返回值：Hello, I'm EchoServerGolang Provider
    :::
    </dx-codeblock>  

