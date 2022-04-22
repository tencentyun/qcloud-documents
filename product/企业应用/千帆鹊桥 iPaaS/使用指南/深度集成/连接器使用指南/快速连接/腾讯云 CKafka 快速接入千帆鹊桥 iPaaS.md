
# 腾讯云 CKafka 快速接入千帆鹊桥 iPaaS
## 使用场景
千帆鹊桥 iPaaS 中的Kafka连接器支持 PLAINTEXT、SASL_PLAINTEXT、SASL_SCRAM 三种认证方式接入Kafka集群，可使用任一被支持的认证方式接入到Kafka集群。
## 操作步骤
### 前期准备
> *前置条件：已开通CKafka服务，并设置公网域名访问及对应ACL策略*

#### 购买腾讯云CKafka
购买腾讯云CKafka请参考[创建公网域名接入的CKafka实例](https://cloud.tencent.com/document/product/597/54840)

#### 设置 CKafka 接入方式
1. 登录[ CKafka 控制台](https://console.cloud.tencent.com/ckafka/index?rid=1)，在实例列表中选中想要设置的实例
![kafka-console](https://qcloudimg.tencent-cloud.cn/raw/0f296a41f01a284260a96bd96b9d04f8.png)
2. 点击实例名称进入实例详情页
![kafka-instance](https://qcloudimg.tencent-cloud.cn/raw/4370cd1e5f0c2977f91975a991f2da59/kafka-instance.png)
3. 点击*添加路由策略*，在弹出的配置窗口中，路由策略配置为*公网域名接入*，接入方式选择*SASL_PLAINTEXT*
![](https://qcloudimg.tencent-cloud.cn/raw/c63e0029e5ba8c364752c2bef4aad4d7.png)
4. 单击提交，配置完成后，获得公网访问的域名和接口[](id:method2)。
![kafka-public-route](https://qcloudimg.tencent-cloud.cn/raw/ec08cd239605c06b11a6fd1cb613a949/kafka-public-route.png)

#### 创建 Topic
1. 登录[ CKafka 控制台](https://console.cloud.tencent.com/ckafka/index?rid=1)，在实例列表中选中想要设置的实例，单击实例的“ID/名称”，进入实例详情页。
![kafka-instance](https://qcloudimg.tencent-cloud.cn/raw/4370cd1e5f0c2977f91975a991f2da59/kafka-instance.png)
2. 在实例详情页，单击页面顶部的Topic 管理，单击新建。在编辑 Topic 窗口中，选择分区数和副本数等信息。
![](https://qcloudimg.tencent-cloud.cn/raw/3d56db2b59a50acd20bf2a97464098ce.png)

#### 设置 CKafka  登录用户[](id:method1)
1. 在CKafka实例详情页面中，点击**用户管理**，进入用户管理页面
![kafka-users](https://qcloudimg.tencent-cloud.cn/raw/b8381b2e088230bd7d2a8906c43cc37d/kafka-users.png)
2. 点击**新建**，依次输入**用户名**、**密码**、**确认密码**。后续iPaaS连接器配置需填写对应字段。
![kafka-new-user](https://qcloudimg.tencent-cloud.cn/raw/3df7602f1fd199372794ea183125506f/kafka-new-user.png)

####  设置 ACL 策略（可选）
1. 进入对应实例的 ACL 策略管理页面
![kafka-acl](https://qcloudimg.tencent-cloud.cn/raw/7211b630313712f9aaba1c119feff19f/kafka-acl.png)
2. 点击**批量设置**按钮或点击某一topic右侧的*编辑ACL策略*链接，进入*新建ACL策略*
![kafka-new-acl](https://qcloudimg.tencent-cloud.cn/raw/623c17d3a92d2670a7d405199765e4b5/kafka-new-acl.png)
3. 勾选要设置ACL策略的Topic，并在下方ACL策略栏中针对用户和ip配置读写策略
配置IP地址为“ * ” 允许全部IP访问。

### 接入配置
####  配置鹊桥 iPaaS Kafka 连接器连接属性
1.  在[iPaaS平台](https://console.cloud.tencent.com/ipaas)上单击**新建应用**，选择**空白应用**进行创建。
![](https://qcloudimg.tencent-cloud.cn/raw/f0e3a02558a61e6168e4a6c993931820.png)
2. 单击左侧的**集成流**展开选择**NewFlow**在画布中单击**+**选择**Apache Kafka 连接器**相关操作。
![](https://qcloudimg.tencent-cloud.cn/raw/188f6b9dbdd2c8c618f417ea3d293ba6.png)
3. 单击右侧的**新建连接器配置**并按照指引填入相关参数。
![](https://qcloudimg.tencent-cloud.cn/raw/8112f535875f2cacfdb1fd2bf36fd3f4.png)

4. 单击**下一步**以使用SASL/PLAINTEXT接入点为例，在连接器配置参数中，依次填写如下配置：

 - 在集群地址栏中填入CKafka公网接入域名，可参考[获得公网访问的域名和接口](#method2)
 - 集群Kafka版本根据购买的Kafka实例版本选择对应的版本
 - SASL安全认证模式选择SASL/PLAINTEXT
 - SASL用户名：CKafka此处的填写规则为 **CKafka实例ID#CKafka用户名**，假设CKafka实例ID为ckafka-instance1，[设置 CKafka  登录用户](#method1)中设置的用户名为kafkaUser，则此处用户名应填写： **ckafka-instance1#kafkaUser**
 - SASL密码：请填写[设置 CKafka  登录用户](#method1)中创建的用户密码
 - 使能TLS安全传输协议：选择false

![image-20220120162453560](https://qcloudimg.tencent-cloud.cn/raw/58fe9328d8335aca2eef8e4ee8bd8a95/image-20220120162453560.png)

5. 其他Kafka参数请按实际情况填写，也可参考 [Apache Kafka 连接器使用指南](https://cloud.tencent.com/document/product/1270/55465)






