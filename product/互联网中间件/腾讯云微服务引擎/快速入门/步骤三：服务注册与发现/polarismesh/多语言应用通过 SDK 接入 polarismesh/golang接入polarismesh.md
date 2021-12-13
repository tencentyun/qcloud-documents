# Golang服务应用接入polarismesh

本文通过一个demo进行 Golang 应用接入微服务引擎托管的 PolarisMesh 治理中心的全流程操作演示，帮助您快速了解如何使用服务治理中心。

## 前提条件

- 已创建PolarisMesh服务治理中心，请参考[创建PolarisMesh治理中心]()。
- 下载github的[demo源码](https://github.com/polarismesh/polaris-go/tree/main/sample/quickstart)到本地并解压
- 【虚拟机部署】已创建CVM虚拟机，请参考[创建CVM虚拟机](https://cloud.tencent.com/document/product/213/2936)
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

6. 上传demo源码

- 安装`golang`环境[Download and install - go.dev](https://go.dev/doc/install)

- 分别将`consumer`以及`provider`的demo源码上传到不同的CVM实例中，这里假定上传的路径均为`/data/polaris/golang_examples`
7. 将demo示例运行

- 运行`provider`

   ```shell
   # 进入provider目录
   cd /data/polaris/golang_examples/provider
   # 运行 provider
   ./provider --service="polaris_go_test" --namespace="default" --host="{CVM内网 or 公网IP}" --port=7879
   ```
   
- 运行`consumer`

   ```shell
   # 进入consumer目录
   cd /data/polaris/golang_examples/consumer
   
   # 运行 consumer
   [root@VM-50-33-centos ./consumer]# ./consumer --service="polaris_go_test" --namespace="default"
   2021/12/13 14:40:03 start to invoke getOneInstance operation
   2021/12/13 14:40:03 instance getOneInstance is 10.0.50.33:7879
   2021/12/13 14:40:03 Hello, I'm Provider
   ```
8. 确认部署结果

- 进入微服务引擎控制台，选择前提条件中创建的polarismesh治理中心实例

- 选择`服务管理` > `服务列表`，查看服务`polaris_go_test`的实例数量

- 若实例数量值不为0，则表示已经成功接入微服务引擎
- 若实例数量为0，或者找不到`polaris_go_test`服务名，则表示微服务应用接入微服务引擎失败。

![](https://qcloudimg.tencent-cloud.cn/raw/a0167bfcec91615b572a5576c97b68b0.png)

   