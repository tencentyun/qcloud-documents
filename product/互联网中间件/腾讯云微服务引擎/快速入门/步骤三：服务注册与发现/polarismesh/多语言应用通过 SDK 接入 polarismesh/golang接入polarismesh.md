# Golang服务应用接入polarismesh

您可以将golang服务应用接入polarismesh治理中心，使用polarismesh提供的一系列服务治理能力，大幅提升线上golang服务的稳定性和开发效率。

> 说明：
>
> - 本章节将使用一个provider服务和一个consumer服务接入微服务引擎。
> - 本章节涉及的demo部署环境使用CVM服务

## 前提条件

- 已创建PolarisMesh服务治理中心，请参考[创建PolarisMesh治理中心]()。
- 下载github的[demo源码](https://github.com/polarismesh/polaris-go/tree/main/sample/quickstart)到本地并解压
- 【虚拟机部署】已创建CVM虚拟机，请参考[创建CVM虚拟机](https://cloud.tencent.com/document/product/213/2936)
- 【golang环境安装】CVM需要安装了golang环境

## 操作步骤

1. 登录微服务引擎控制台
  - 登录[腾讯云控制台](https://cloud.tencent.com/)
  - 单击左上角云产品，搜索”微服务引擎”，选择并进入微服务引擎控制台。
    ![console](https://qcloudimg.tencent-cloud.cn/raw/7f7daff61aff9aface98161c61a56239.png)

2. 获取微服务引擎服务治理中心地址
  - 点击左边栏polarismesh按钮，进入polarismesh引擎列表：![pm_icon](https://qcloudimg.tencent-cloud.cn/raw/bdd06200187fff733eb1222f794a014a.png)
  - 点击页面上方下拉列表，选择地域：![region_icon](https://qcloudimg.tencent-cloud.cn/raw/b5153fa452844ee19e24436e11b2376e.png)
  - 在引擎列表中，选择已经创建好的polarismesh服务治理中心引擎，点击进入：![instance_icon](https://qcloudimg.tencent-cloud.cn/raw/c75a4b2c7b53a6cb2bec33bde7fa8c99.png)
  - 进入“基本信息”页，查看访问地址，PHP应用访问使用gRPC端口（8091）：
    ![access](https://qcloudimg.tencent-cloud.cn/raw/561460943b0404c44c29d2c0dd09c56f.png)

3. 修改demo中的注册中心地址

   a. 在下载到本地的demo源码目录下，分别找到`quickstart/consumer/polaris.yaml`以及`quickstart/provider/polaris.yaml`文件

   b. 添加polarismesh治理中心的地址到项目的配置文件中（这里已`quickstart/consumer/polaris.yaml`为例）。

   ```yaml
   global:
     serverConnector:
     	# 治理中心地址，当前php sdk支持的gRPC协议，因此要使用8091端口
       addresses:
         - 192.168.100.9:8091
   ```

4. 上传demo源码

   a. 安装`golang`环境[Download and install - go.dev](https://go.dev/doc/install)

   b. 分别将`consumer`以及`provider`的demo源码上传到不同的CVM实例中，这里假定上传的路径均为`/data/polaris/golang_examples`
   
5. 将demo示例运行

   a. 运行`provider`

   ```shell
   # 进入provider目录
   cd /data/polaris/golang_examples/provider
   # 运行 provider
   ./provider --service="polaris_go_test" --namespace="default" --host="{CVM内网 or 公网IP}" --port=9999
   ```
   
   b. 运行`consumer`

   ```shell
   # 进入consumer目录
   cd /data/polaris/golang_examples/consumer
   # 运行 consumer
   ./consumer --service="polaris_go_test" --namespace="default"
   
   # 确认是否收到输出
   [root@VM-50-33-centos ./consumer]# php consumer.php 
   Attempting to connect to '10.0.50.33' on port '9996'...Connect success. 
   Client send success 
   Reading response:
   hello. I`m provider
   ```
   
6. 确认部署结果

   a. 进入微服务引擎控制台，选择前提条件中创建的polarismesh治理中心实例

   b. 选择`服务管理` > `服务列表`，查看服务`polaris_go_test`的实例数量

   - 若实例数量值不为0，则表示已经成功接入微服务引擎
   - 若实例数量为0，或者找不到`polaris_php_test`服务名，则表示微服务应用接入微服务引擎失败。
   
   ![](https://qcloudimg.tencent-cloud.cn/raw/c75595d9d8ece9633427a8206f9ecb63.png)
   
   