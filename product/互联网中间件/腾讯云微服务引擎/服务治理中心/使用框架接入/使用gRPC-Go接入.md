## 操作场景

本文通过一个 demo 进行 gRPC-Go 应用接入微服务引擎托管的 PolarisMesh 治理中心的全流程操作演示，帮助您快速了解如何使用服务治理中心。

## 前提条件

- 已创建 PolarisMesh 服务治理中心，请参见 [创建 PolarisMesh 治理中心](https://cloud.tencent.com/document/product/1364/65866)。
- 下载 Github 的 [demo 源码](https://github.com/polarismesh/grpc-go-polaris/tree/main/examples/quickstart) 到本地并解压。
- 本地编译构建打包机器环境已安装了 [Go](https://go.dev/doc/devel/release)，并且能够使用 Go mod 拉取依赖。
- 根据您自身的业务，已准备好业务部署的资源，`虚拟机部署`、`容器化部署`和 `TEM 部署`选择其中一种方式即可。
  - **虚拟机部署**已创建 CVM 虚拟机，请参见 [创建 CVM 虚拟机](https://cloud.tencent.com/document/product/213/2936)。
  - **容器化部署**已创建 TKE 容器集群，请参见 [创建 TKE 集群](https://cloud.tencent.com/document/product/457/32189)。
  - **TEM部署**已创建 TEM 环境，请参见 [创建 TEM 环境](https://cloud.tencent.com/document/product/1371/53293)。

## 操作步骤

1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。
2. 在**治理中心**下的 **polarismesh** 页面，单击页面左上方下拉列表，选择目标地域。
3. 单击目标引擎的“ID”，进入基本信息页面。
4. 查看访问地址，gRPC-Go 应用访问使用 gRPC 端口（8091）：
![](https://qcloudimg.tencent-cloud.cn/raw/e7dc5ac5f7c76a316ae68b667d8a365f.png)
5. 修改 demo 中的注册中心地址。
  1. 在下载到本地的 [demo 源码目录](https://github.com/polarismesh/grpc-go-polaris/tree/main/examples/quickstart) 下，分别找到
`\examples\quickstart\provider\polaris.yaml`和`\examples\quickstart\consumer\polaris.yaml`两个文件。
  - 添加微服务引擎服务治理中心地址到项目配置文件中（以`\examples\quickstart\provider\polaris.yaml`为例）。
  <dx-codeblock>
:::  yml
global:
  serverConnector:
    addresses:
    - 10.0.4.6:8091
:::
</dx-codeblock>
6. 将源码编译成可执行程序。
  1. 分别在`consumer`和`provider`这2个目录下，打开 cmd 命令，执行以下命令，对项目进行编译：
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
<td>\examples\quickstart\provider</td>
<td>provider</td>
<td>服务生产者</td>
</tr>
<tr>
<td>\examples\quickstart\consumer</td>
<td>consumer</td>
<td>服务消费者</td>
</tr>
</table>    
7. 部署 provider 和 consumer 微服务应用，虚拟机部署方式和容器化部署根据您业务实际的部署方式选择一种即可。
 1. **虚拟机部署**部署 provider 和 consumer 微服务应用。
      - 上传  Jar 包至 CVM 实例。
      - 执行启动命令进行启动：
<dx-codeblock>
:::  shell
    nohup [二进制名称] &
:::
</dx-codeblock>     
 2. **容器化部署**部署 provider 和 consumer 微服务应用。
      - 编写 dockerfile 生成镜像，参考：
<dx-codeblock>
:::  shell
    FROM golang:alpine
    WORKDIR /root
    ADD . /root
    ENTRYPOINT ./[二进制名称]
:::
</dx-codeblock>        
     - 通过 TKE 部署并运行镜像。
 3. **TEM 部署**部署 provider 和 consumer 微服务应用。
     - 选择 TEM 环境，注意所选择的环境，其依赖的 VPC，必须和上面已经创建的治理中心实例所依赖的 VPC 一致：
![](https://qcloudimg.tencent-cloud.cn/raw/f0d2eb2341c6d4f5ef327f8c105b9cc1.png)
     - 在已选择的环境中，新建TEM应用，相关参数填写参考：
![](https://qcloudimg.tencent-cloud.cn/raw/30bb315d4e127432b163c35358c68074.png)
     - 部署应用，相关参数填写请参考（端口号映射，consumer 默认端口号为16011，provider默认端口号为16010）：
![](https://qcloudimg.tencent-cloud.cn/raw/cee2750778739a9b2d90577b22940e6a.png)
     - 查看访问路径，consumer 应用部署完后，可以在**基本信息** > **访问配置**中查看访问地址，如需公网访问，可以**编辑并更新**开启公网访问：
![](https://qcloudimg.tencent-cloud.cn/raw/f7d77e0bdb680df35d27c862070082db.png)
8. 确认部署结果。
 1. 进入前面提到的微服务治理中心实例页面。
    - 选择**服务管理** > **服务列表**，查看微服务 EchoServerGRPC（provider）的实例数量：
    - 若实例数量值不为0，则表示已经成功接入微服务引擎。
    - 若实例数量为0，或者找不到 EchoServerGRPC 服务名，则表示微服务应用接入微服务引擎失败。
![](https://qcloudimg.tencent-cloud.cn/raw/c63dec2f8797d79fce57db420a622fa9.png)
 - 调用 consumer 的 HTTP 接口
    - 执行 http 调用，其中`${app.port}`替换为 consumer 的监听端口（默认为16011），`${add.address}`则替换为 consumer 暴露的地址。
<dx-codeblock>
:::  shell
    curl -L -X GET 'http://${add.address}:${app.port}/echo?value=hello_world'
    预期返回值：echo: hello_world
:::
</dx-codeblock>


