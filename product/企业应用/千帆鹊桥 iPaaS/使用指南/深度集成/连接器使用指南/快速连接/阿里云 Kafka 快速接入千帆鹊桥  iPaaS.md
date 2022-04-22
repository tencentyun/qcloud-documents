# 阿里云 Kafka 快速接入千帆鹊桥  iPaaS
## 操作场景
鹊桥 iPaaS 中的Kafka连接器支持 PLAINTEXT、SASL_PLAINTEXT、SASL_SCRAM 三种认证方式接入Kafka集群，可使用任一被支持的认证方式接入到Kafka集群。
## 操作步骤
### 前期准备

>!阿里云Kafka在购买时，有VPC接入版和公网+VPC接入版可选，由于iPaaS位于阿里云的外网，因此创建实例时请选择**公网+VPC接入版**

####  步骤1：购买Kafka实例

1. 进入[阿里云 Kafka 控制台](https://kafka.console.aliyun.com/region/cn-hangzhou/instances)

![image-20220325112756327](https://qcloudimg.tencent-cloud.cn/raw/3150c111381a45abdef4a794a6a191e2/image-20220325112756327.png)

2. 点击购买实例，进入实例购买页面，按照实际付费方式选择包年包月或按量计费，确定后进入购买页面，这里以按量计费为例。

![image-20220325113020084](https://qcloudimg.tencent-cloud.cn/raw/35734b3c763cb15c2fba0323744f5c10/image-20220325113020084.png)

3. 进入实例购买页面后，按照实际情况选择地域和规格类型，**实例类型**请选择**公网+VPC实例**，按照实际情况选择公网流量大小，其他参数如磁盘类型、磁盘大小可参考阿里云Kafka文档说明，按照业务实际情况选择，勾选服务协议后，点击**立即购买**即可完成实例购买。

![image-20220325113354820](https://qcloudimg.tencent-cloud.cn/raw/de2e9513e154ca76c862328126ee1c32/image-20220325113354820.png)

#### 步骤2：资源创建

#####  Kafka实例部署

> 根据[阿里云 Kafka 文档](https://help.aliyun.com/document_detail/99952.html)，推荐在阿里云控制台手动创建规划好的 Topic 和 Consumer Group 等资源。

1. 进入[阿里云 Kafka 控制台](https://kafka.console.aliyun.com/region/cn-hangzhou/instances)，点击左边栏的实例列表，进入实例列表页面。

![image-20220325113656891](https://qcloudimg.tencent-cloud.cn/raw/c6cfe533cae121af7eaa204ef1bb7fda/image-20220325113656891.png)

2. 点击部署按钮，在弹出的部署页面中，关联已有VPC或新建VPC。

![image-20220325114030967](https://qcloudimg.tencent-cloud.cn/raw/40c99fdbf4605908e37d6548397de1b3/image-20220325114030967.png)

3. 点击页面中VPC创建连接，进入专有网络控制台，点击创建专有网络。

![image-20220325114229164](https://qcloudimg.tencent-cloud.cn/raw/046cb7659584ff540b4ea2a3d40561c9/image-20220325114229164.png)

- 根据页面填写相关参数

![image-20220325114345867](https://qcloudimg.tencent-cloud.cn/raw/fac7fedaad3133f31812f1f37cb16a67/image-20220325114345867.png)
- 单击确定完成专有网络的创建

![image-20220325114417108](https://qcloudimg.tencent-cloud.cn/raw/e21dd38d89a6bf9acbb2e302db479355/image-20220325114417108.png)

4. 切换回阿里云Kafka实例部署页面，选中创建好的VPC和vSwitch。

![image-20220325114528844](https://qcloudimg.tencent-cloud.cn/raw/bdffcdfed224b5570b274de87596c2d3/image-20220325114528844.png)

5. 点击确定后，等待实例部署完成。

![image-20220325114615576](https://qcloudimg.tencent-cloud.cn/raw/2c0717325f2991b3a06b4a20c803f3c1/image-20220325114615576.png)

##### Kafka资源创建

1. 在[Kafka控制台](https://kafka.console.aliyun.com/region/cn-hangzhou/instances)点击实例目标名称，进入实例管理页。

![image-20220325122438823](https://qcloudimg.tencent-cloud.cn/raw/581a8e22152123fd527bdae7c347a402/image-20220325122438823.png)

2. 点击Topic管理，点击创建Topic，进入Topic创建页面，填写对应参数后，点击确定完成Topic创建。

![image-20220325122618362](https://qcloudimg.tencent-cloud.cn/raw/43352d56041ec4d353fa4db2c3abbfbf/image-20220325122618362.png)

3. 点击Group管理，点击创建Group，进入Group创建页面，填写group id和描述等必填参数后，点击确定，完成group创建。

![image-20220325122754397](https://qcloudimg.tencent-cloud.cn/raw/1a87637ffec26eeeab224d9a3ddccd1e/image-20220325122754397.png)



### 接入配置

#### 步骤1： 获取iPaaS Kafka连接器配置信息

1. 登录[阿里云 Kafka 控制台](https://kafka.console.aliyun.com/region/cn-hangzhou/instances)点击**目标实例ID**进入实例详情页，可以查询到接入点信息。[](id:method1)

![image-20220325123127238](https://qcloudimg.tencent-cloud.cn/raw/cb0cc51cdaa996dd016712021170b2ff/image-20220325123127238.png)
2. 登录[阿里云 Kafka 控制台](https://kafka.console.aliyun.com/region/cn-hangzhou/instances)点击**目标实例ID**进入实例详情页，下拉页面可以查询到配置信息[](id:method2)
![](https://qcloudimg.tencent-cloud.cn/raw/12ba783fc1cfca5e8d95b1d2a9bc9d9d.png)

#### 步骤2：配置鹊桥 iPaaS Kafka 连接器连接属性 
3. 在[iPaaS平台](https://console.cloud.tencent.com/ipaas)上单击**新建应用**，选择**空白应用**进行创建。
![](https://qcloudimg.tencent-cloud.cn/raw/f0e3a02558a61e6168e4a6c993931820.png)
4. 单击左侧的**集成流**展开选择**NewFlow**在画布中单击**+**选择**Apache Kafka 连接器**相关操作。
![](https://qcloudimg.tencent-cloud.cn/raw/188f6b9dbdd2c8c618f417ea3d293ba6.png)
5. 单击右侧的**新建连接器配置**并按照指引填入相关参数。
![](https://qcloudimg.tencent-cloud.cn/raw/8112f535875f2cacfdb1fd2bf36fd3f4.png)

6. 单击**下一步**以使用SASL/PlainText接入点为例，在连接器配置参数中，依次填写如下配置：

 - 在集群地址栏中填入Kafka公网接入域名，此处填写[接入点信息](#method1)中网络为公网的域名接入点
 - 集群Kafka版本根据购买的Kafka实例版本选择对应的版本，此处填写[接入点信息](#method1)中的大版本号
 - SASL安全认证模式选择SASL/PlainText
 - SASL用户名：此处填写[配置信息](#method2)中的用户名
 - SASL密码：此处填写[配置信息](#method2)中的密码
 - 使能TLS安全传输协议：选择true
 - 消费者组填写刚刚创建的：ipaas-consumer
 - 主题填写刚刚创建的：ipaas-test

![](https://qcloudimg.tencent-cloud.cn/raw/61c6de359c350aeaabdd5a8b2b02abbc.png)

7.  其他Kafka参数请按实际情况填写，也可参考 [Apache Kafka 连接器使用指南](https://cloud.tencent.com/document/product/1270/55465)
