## 操作场景

本文通过一个demo进行 Golang 应用接入微服务引擎托管的 PolarisMesh 治理中心的全流程操作演示，帮助您快速了解如何使用服务治理中心。

## 前提条件

- 已创建PolarisMesh服务治理中心，请参考[创建PolarisMesh治理中心]()。
- 下载github的[demo源码](https://github.com/polarismesh/polaris-go/tree/main/sample/quickstart)到本地并解压。
- 【虚拟机部署】已创建CVM虚拟机，请参考[创建CVM虚拟机](https://cloud.tencent.com/document/product/213/2936)。
- 【容器化部署】已创建TKE容器集群，请参考[创建 TKE 集群](https://cloud.tencent.com/document/product/457/32189)。
- 【golang环境安装】CVM需要安装了golang环境

## 操作步骤

1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。

2. 在**治理中心**下的 **polarismesh** 页面，点击页面上方下拉列表，选择目标地域：![region_icon](https://qcloudimg.tencent-cloud.cn/raw/b5153fa452844ee19e24436e11b2376e.png)

3. 单击目标引擎的“ID”，进入基本信息页面。

4. 查看访问地址，Golang 应用访问使用gRPC端口（8091）：
    ![access](https://qcloudimg.tencent-cloud.cn/raw/561460943b0404c44c29d2c0dd09c56f.png)

5. 修改demo中的注册中心地址

- 在下载到本地的demo源码目录下，分别找到`quickstart/consumer/polaris.yaml`以及`quickstart/provider/polaris.yaml`文件

- 添加polarismesh治理中心的地址到项目的配置文件中（这里已`quickstart/consumer/polaris.yaml`为例）。

   ```yaml
   global:
     serverConnector:
     	# 治理中心地址，当前php sdk支持的gRPC协议，因此要使用8091端口
       addresses:
         - 192.168.100.9:8091
   ```

6. 将源码编译成可执行程序。

  - 分别在`consumer`和`provider`这2个目录下，打开cmd命令，执行以下命令，对项目进行编译：

    - 编译consumer：`CGO_ENABLED=0 go build -ldflags "-s -w" -o consumer`
    - 编译provider：`CGO_ENABLED=0 go build -ldflags "-s -w" -o provider`
- 编译成功后，生成如表1所示的2个二进制包。
      表1 软件包列表

  | 软件包所在目录                | 软件包名称 | 说明       |
  | ----------------------------- | ---------- | ---------- |
  | \examples\quickstart\provider | provider   | 服务生产者 |
  | \examples\quickstart\consumer | consumer   | 服务消费者 |

- 分别将`consumer`以及`provider`的二进制上传到不同的CVM实例中，这里假定上传的路径均为`/data/polaris/golang_examples`
7. 【虚拟机部署】部署provider和consumer微服务。

- 上传二进制以及配置文件至 CVM 实例。

- 运行`provider`

   ```shell
   # 进入provider目录
   cd /data/polaris/golang_examples/provider
   # 运行 provider
   ./provider --host="{CVM内网 or 公网IP}" --port=7879
   ```
   
- 运行`consumer`

   ```shell
   # 进入consumer目录
   cd /data/polaris/golang_examples/consumer
   
   # 运行 consumer
   [root@VM-50-33-centos ./consumer]# ./consumer --service="EchoServerGolang" --namespace="default"
   ```
8. 【容器化部署】部署provider和consumer微服务。

- 编写dockerfile生成镜像，参考：

   ```
   FROM golang:alpine
   WORKDIR /root
   ADD . /root
   ENTRYPOINT ./[二进制名称] [启动参数命令]
   ```
- 通过TKE部署并运行镜像

9. 确认部署结果

- 进入微服务引擎控制台，选择前提条件中创建的polarismesh治理中心实例

- 选择`服务管理` > `服务列表`，查看服务`EchoServerGolang`的实例数量

- 若实例数量值不为0，则表示已经成功接入微服务引擎
- 若实例数量为0，或者找不到`EchoServerGolang`服务名，则表示微服务应用接入微服务引擎失败。

![](https://qcloudimg.tencent-cloud.cn/raw/ee84221306724bc6b45e055c1859b8df.png)

 - 调用consumer的HTTP接口

   - 执行http调用，其中${app.port}替换为consumer的监听端口（默认为18080），${add.address}则替换为consumer暴露的地址。

    ```
   curl -L -X GET 'http://${add.address}:${app.port}/echo'
   预期返回值：Hello, I'm EchoServerGolang Provider
    ```

