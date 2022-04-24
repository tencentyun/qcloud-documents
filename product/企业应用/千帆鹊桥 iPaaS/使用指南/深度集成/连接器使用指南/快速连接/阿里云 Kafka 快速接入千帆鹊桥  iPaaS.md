
## 操作场景
鹊桥 iPaaS 中的 Kafka 连接器支持 PLAINTEXT、SASL_PLAINTEXT、SASL_SCRAM 三种认证方式接入 Kafka 集群，可使用任一被支持的认证方式接入到 Kafka 集群。


## 前期准备

>!在购买阿里云 Kafka 时，有 VPC 接入版和公网 + VPC 接入版可选，由于 iPaaS 位于阿里云的外网，因此创建实例时请选择**公网+VPC接入版**。

###  步骤1：购买 Kafka 实例

1. 登录 [阿里云 Kafka 控制台](https://kafka.console.aliyun.com/region/cn-hangzhou/instances)。
2. 单击**购买实例**，进入实例购买页面。
3. 按照实际付费方式选择包年包月或按量计费，单击**确定**进入购买页面（本文以按量计费为例）。
![](https://qcloudimg.tencent-cloud.cn/raw/9659d2059622356e4d57d235514e1965.png)
4. 在实例购买页面，按照实际情况选择地域和规格类型。
**实例类型**请选择**公网+VPC实例**，按照实际情况选择公网流量大小，其他参数如磁盘类型、磁盘大小可参考 [阿里云 Kafka 文档](https://help.aliyun.com/document_detail/99956.html) 说明，按照业务实际情况选择。
5. 勾选服务协议后，单击**立即购买**即可完成实例购买。
![image-20220325113354820](https://qcloudimg.tencent-cloud.cn/raw/de2e9513e154ca76c862328126ee1c32/image-20220325113354820.png)


### 步骤2：创建资源

####  Kafka实例部署
 
根据 [阿里云 Kafka 文档](https://help.aliyun.com/document_detail/99952.html)，推荐在阿里云控制台手动创建规划好的 Topic 和 Consumer Group 等资源。

1. 登录 [阿里云 Kafka 控制台](https://kafka.console.aliyun.com/region/cn-hangzhou/instances)，单击左侧菜单栏的**实例列表**，进入实例列表页面。
2. 单击操作列的**部署**，在弹出的部署页面中，关联已有 VPC 或新建 VPC。
![](https://qcloudimg.tencent-cloud.cn/raw/9337a98b07804bda4f4f6b104fe11f5d.png)
关联界面如下：
![](https://qcloudimg.tencent-cloud.cn/raw/5bcea74ad053de56466c921fd845aaaa.png)
3. 点击页面中 VPC 创建链接，进入专有网络控制台，单击**创建专有网络**。
![image-20220325114229164](https://qcloudimg.tencent-cloud.cn/raw/046cb7659584ff540b4ea2a3d40561c9/image-20220325114229164.png)
	1. 根据页面填写相关参数。
	![image-20220325114345867](https://qcloudimg.tencent-cloud.cn/raw/fac7fedaad3133f31812f1f37cb16a67/image-20220325114345867.png)
	2. 单击**确定**完成专有网络的创建。
	![](https://qcloudimg.tencent-cloud.cn/raw/25c4e5058843df9f0a70c1e4179dee14.png)
4. 切换回阿里云 Kafka 实例部署页面，选中创建好的 VPC 和 vSwitch。
![](https://qcloudimg.tencent-cloud.cn/raw/a1cc58fac54bfafba345efd26840c49c.png)
5. 单击**确定**后，等待实例部署完成。
![](https://qcloudimg.tencent-cloud.cn/raw/047db6123c2549a5c08aa251a9790014.png)


#### Kafka 资源创建

1. 在 [Kafka 控制台](https://kafka.console.aliyun.com/region/cn-hangzhou/instances) 单击目标实例名称，进入实例管理页。
![](https://qcloudimg.tencent-cloud.cn/raw/69c327f0064937750bd0a824250be570.png)
2. 单击**Topic管理**，单击**创建Topic**，进入T opic 创建页面，填写对应参数后，单击**确定**完成Topic创建。
![](https://qcloudimg.tencent-cloud.cn/raw/28c65d2ff768ea66b93c5913b3e82560.png)
3. 单击**Group管理**，单击**创建Group**，进入 Group 创建页面，填写 group id 和描述等必填参数后，单击**确定**，完成 Group 创建。
![](https://qcloudimg.tencent-cloud.cn/raw/390c84dc008e83196f91ca913eeab19f.png)



## 接入配置

### 步骤1：获取 iPaaS Kafka 连接器配置信息

1. 登录 [阿里云 Kafka 控制台](https://kafka.console.aliyun.com/region/cn-hangzhou/instances)，单击**目标实例ID**进入实例详情页，可以查询到接入点信息。[](id:method1)
![](https://qcloudimg.tencent-cloud.cn/raw/1ebf7c6f5bedfcf2c070d6fc1ac01925.png)
2. 登录 [阿里云 Kafka 控制台](https://kafka.console.aliyun.com/region/cn-hangzhou/instances)，单击**目标实例ID**进入实例详情页，下拉页面可以查询到配置信息[](id:method2)
![](https://qcloudimg.tencent-cloud.cn/raw/a63f40a78e8088c7175a6dfb42e3f5db.png)

### 步骤2：配置鹊桥 iPaaS Kafka 连接器连接属性 
1. 登录 [千帆鹊桥 iPaaS 控制台](https://console.cloud.tencent.com/ipaas)，单击**新建应用**，选择**空白应用**进行创建。
![](https://qcloudimg.tencent-cloud.cn/raw/2de14b55e78c95b5af12a36d53812f82.png)
2. 单击左侧的**集成流**展开选择**NewFlow**在画布中单击**+**选择**Apache Kafka 连接器**相关操作。
![](https://qcloudimg.tencent-cloud.cn/raw/188f6b9dbdd2c8c618f417ea3d293ba6.png)
3. 单击右侧的**新建连接器配置**并按照指引填入相关参数。
![](https://qcloudimg.tencent-cloud.cn/raw/8112f535875f2cacfdb1fd2bf36fd3f4.png)
4. 单击**下一步**，以使用 SASL/PlainText 接入点为例，在连接器配置参数中，依次填写如下配置：
 - 集群地址：填入 Kafka 公网接入域名，此处填写 [接入点信息](#method1) 中网络为公网的域名接入点
 - 集群Kafka版本：根据购买的 Kafka 实例版本选择对应的版本，此处填写 [接入点信息](#method1)中的大版本号
 - SASL安全认证模式：选择SASL/PlainText
 - SASL用户名：此处填写[配置信息](#method2)中的用户名
 - SASL密码：此处填写[配置信息](#method2)中的密码
 - 使能TLS安全传输协议：选择true
 - 消费者组：填写刚刚创建的 ipaas-consumer
 - 主题：填写刚刚创建的 ipaas-test
![](https://qcloudimg.tencent-cloud.cn/raw/ae8a9835802014fe2bb75d7b8859a19c.png)
5.  其他 Kafka 参数请按实际情况填写，也可参考 [Apache Kafka 连接器使用指南](https://cloud.tencent.com/document/product/1270/55465)。
