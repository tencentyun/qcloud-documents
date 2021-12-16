# Dubbo-Go服务应用接入polarismesh

本文通过一个demo进行 dubbo-go 应用接入微服务引擎托管的 PolarisMesh 治理中心的全流程操作演示，帮助您快速了解如何使用服务治理中心。

## 前提条件

- 已创建PolarisMesh服务治理中心，请参考[创建PolarisMesh治理中心]()。
- 下载github的[demo源码](https://github.com/apache/dubbo-go-samples/tree/master/registry/polaris)到本地并解压
- 【虚拟机部署】已创建CVM虚拟机，请参考[创建CVM虚拟机](https://cloud.tencent.com/document/product/213/2936)
- 【golang环境安装】CVM需要安装了golang环境

## 操作步骤

1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。

2. 在**治理中心**下的 **polarismesh** 页面，点击页面上方下拉列表，选择目标地域：![region_icon](https://qcloudimg.tencent-cloud.cn/raw/b5153fa452844ee19e24436e11b2376e.png)

3. 单击目标引擎的“ID”，进入基本信息页面。

4. 查看访问地址，Dubbo-Go 应用访问使用gRPC端口（8091）：
   ![access](https://qcloudimg.tencent-cloud.cn/raw/561460943b0404c44c29d2c0dd09c56f.png)

5. 修改demo中的注册中心地址

- 在下载到本地的demo源码目录下，分别找到`go-client/conf/dubbogo.yaml`以及`go-server/conf/dubbogo.yaml`文件

- 添加polarismesh治理中心的地址到项目的配置文件中（这里已`go-client/conf/dubbogo.yaml`为例）。

  ```yaml
  dubbo:
    registries:
      polarisMesh:
        protocol: polaris
        address: 127.0.0.1:8091
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

6. 上传demo源码

- 安装`golang`环境[Download and install - go.dev](https://go.dev/doc/install)

- 分别将`go-client`以及`go-server`的demo源码上传到不同的CVM实例中，这里假定上传的路径均为`/data/polaris/dubbogo_examples`

7. 将demo示例运行

- 运行`go-server`

  ```shell
  # 进入provider目录
  cd /data/polaris/dubbogo_examples/go-server/cmd
  # 设置配置文件目录
  export DUBBO_GO_CONFIG_PATH="../conf/dubbogo.yml"
  # 运行 provider
  [root@VM-50-33-centos ./go-server/cmd]# go run .
  go run .
  ```

- 运行`go-client`

  ```shell
  # 进入consumer目录
  cd /data/polaris/dubbogo_examples/go-client/cmd
  # 设置配置文件目录
  export DUBBO_GO_CONFIG_PATH="../conf/dubbogo.yml"
  # 运行 consumer
  [root@VM-50-33-centos ./go-client/cmd]# go run .
  ...
  start to test dubbo
  2021-12-16T12:51:46.102+0800    INFO    cmd/main.go:71  response result: &{A001 Alex Stocks 18 2021-12-16 12:51:46.102 +0800 CST}
  
  2021-12-16T12:51:46.103+0800    INFO    cmd/main.go:79  response result: &{A001 Alex Stocks from UserProviderWithCustomGroupAndVersion 18 2021-12-16 12:51:46.103 +0800 CST}
  ```

8. 确认部署结果

- 进入微服务引擎控制台，选择前提条件中创建的polarismesh治理中心实例
- 选择`服务管理` > `服务列表`，查看一下服务的实例数量
  - `consumers:org.apache.dubbo.UserProvider.Test2`
  - `consumers:org.apache.dubbo.UserProvider.Test`
  - `provider:org.apache.dubbo.UserProvider.Test2`
  - `provider:org.apache.dubbo.UserProvider.Test`
- 若实例数量值不为0，则表示已经成功接入微服务引擎
- 若实例数量为0，或者找不到上述服务名，则表示`Dubbo-Go`应用接入微服务引擎失败。

![](https://qcloudimg.tencent-cloud.cn/raw/27547973537c1f6bcbee0b6560295abe.png)

   