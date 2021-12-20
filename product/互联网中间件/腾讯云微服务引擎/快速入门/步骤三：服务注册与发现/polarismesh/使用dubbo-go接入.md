## 操作场景

本文通过一个demo进行 dubbo-go 应用接入微服务引擎托管的 PolarisMesh 治理中心的全流程操作演示，帮助您快速了解如何使用服务治理中心。

## 前提条件

- 已创建PolarisMesh服务治理中心，请参考[创建PolarisMesh治理中心]()。
- 下载github的[demo源码](https://github.com/polarismesh/examples/tree/main/dubbo3/dubbogo)到本地并解压
- 本地编译构建打包机器环境已安装了golang环境，并且能够访问Github
- 当前仅支持dubbo-go的接口注册模型
- 根据您自身的业务，已准备好业务部署的资源，虚拟机部署和容器化部署选择其中一种方式即可。
  - 【虚拟机部署】已创建CVM虚拟机，请参考[创建CVM虚拟机](https://cloud.tencent.com/document/product/213/2936)
  - 【容器化部署】已创建TKE容器集群，请参考[创建 TKE 集群](https://cloud.tencent.com/document/product/457/32189)。

## 操作步骤

1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。

2. 在**治理中心**下的 **polarismesh** 页面，点击页面上方下拉列表，选择目标地域，如：![region_icon](https://qcloudimg.tencent-cloud.cn/raw/b5153fa452844ee19e24436e11b2376e.png)

3. 单击目标引擎的“ID”，进入基本信息页面。

4. 查看访问地址，Dubbo-Go 应用访问使用gRPC端口（8091）：
   ![access](https://qcloudimg.tencent-cloud.cn/raw/29eb8647e119d0d284f36d417f3bb551.png)

5. 修改demo中的注册中心地址

- 在下载到本地的[demo源码](https://github.com/polarismesh/examples/tree/main/dubbo3/dubbogo)目录下，分别找到“”以及“dubbo\dubbogo\consumer\dubbogo.yaml”文件

- 添加微服务引擎服务治理中心地址到项目配置文件中（这里已“dubbo\dubbogo\provider\dubbogo.yaml”为例）。

  ```yaml
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
  ```

6. 将源码编译成可执行程序。

  - 分别在consumer和provider这2个目录下，打开cmd命令，执行以下命令，对项目进行编译：

    - 编译consumer：`CGO_ENABLED=0 go build -ldflags "-s -w" -o consumer`
    - 编译provider：`CGO_ENABLED=0 go build -ldflags "-s -w" -o provider`

- 编译成功后，生成如表1所示的2个二进制包。
      表1 软件包列表

  | 软件包所在目录          | 软件包名称 | 说明       |
  | ----------------------- | ---------- | ---------- |
  | dubbo3\dubbogo\provider | provider   | 服务生产者 |
  | dubbo3\dubbogo\consumer | consumer   | 服务消费者 |


7. 部署provider和consumer微服务应用，虚拟机部署方式和容器化部署根据您业务实际的部署方式选择一种即可。

   （1）【虚拟机部署】部署provider和consumer微服务应用。

    - 上传二进制包至 CVM 实例。
		
    - 执行启动命令进行启动：
	```
   	# 进入provider目录
		cd /data/polaris/dubbogo_examples/provider
		# 设置配置文件目录
		export DUBBO_GO_CONFIG_PATH="./dubbogo.yml"
		# 运行 provider
		./provider
	```
   
   （2）【容器化部署】部署provider和consumer微服务应用。
   
    - 编写dockerfile生成镜像，参考：
   
   ```
    FROM golang:alpine
    WORKDIR /root
    ADD . /root
    ENTRYPOINT ./[二进制名称] [启动参数命令]
   ```
   
    - 通过TKE部署并运行镜像
   
8. 确认部署结果

- 进入前面提到的微服务治理中心实例页面。
- 选择“服务管理 > 服务列表”，查看一下服务的实例数量：
- 若实例数量值不为0，则表示已经成功接入微服务引擎
- 若实例数量为0，或者找不到上述服务名，则表示`Dubbo-Go`应用接入微服务引擎失败。

![](https://qcloudimg.tencent-cloud.cn/raw/7cc1d0a8766e6a175ab10fc6e4dac517.png)

 - 调用consumer的HTTP接口

   - 执行http调用，其中${app.port}替换为consumer的监听端口（默认为18080），${add.address}则替换为consumer暴露的地址。

    ```
   curl -L -X GET 'http://${add.address}:${app.port}/echo'
   预期返回值：{"UserProvider":{"id":"A001","name":"Alex Stocks","age":18,"time":"2021-12-16T16:57:27.945+08:00"},"UserProviderWithCustomGroupAndVersion":{"id":"A001","name":"Alex Stocks from UserProviderWithCustomGroupAndVersion","age":18,"time":"2021-12-16T16:57:27.946+08:00"}}
    ```

