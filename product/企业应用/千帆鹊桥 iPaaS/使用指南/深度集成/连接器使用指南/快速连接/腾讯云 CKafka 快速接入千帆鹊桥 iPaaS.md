## 操作场景
千帆鹊桥 iPaaS 中的 Kafka 连接器支持 PLAINTEXT、SASL_PLAINTEXT、SASL_SCRAM 三种认证方式接入 Kafka 集群，可使用任一被支持的认证方式接入到 Kafka 集群。

## 前期准备
您需要先开通 CKafka 服务，并设置公网域名访问及对应 ACL 策略。

### 购买腾讯云 CKafka
详细操请参考 [创建公网域名接入的 CKafka 实例](https://cloud.tencent.com/document/product/597/54840)。

### 设置 CKafka 接入方式
1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka/index?rid=1)，在实例列表中选中想要设置的实例。
![](https://qcloudimg.tencent-cloud.cn/raw/0d9e8ae5f9ba6668bd849d786ef8ab4d.png)
2. 单击实例的“ID/名称”，进入实例详情页。
![](https://qcloudimg.tencent-cloud.cn/raw/05d8bc7d61f34acf40460a1a2641e6d1.png)
3. 单击**添加路由策略**，在弹出的配置窗口中，路由策略配置为“公网域名接入”，接入方式选择“SASL_PLAINTEXT”。
![](https://qcloudimg.tencent-cloud.cn/raw/c63e0029e5ba8c364752c2bef4aad4d7.png)
4. 单击**提交**，配置完成后，获得公网访问的域名和接口[](id:method2)。
![kafka-public-route](https://qcloudimg.tencent-cloud.cn/raw/ec08cd239605c06b11a6fd1cb613a949/kafka-public-route.png)

### 创建 Topic
1. 登录[ CKafka 控制台](https://console.cloud.tencent.com/ckafka/index?rid=1)，在实例列表中选中想要设置的实例，单击实例的“ID/名称”，进入实例详情页。
2. 在实例详情页，单击页面顶部的 **Topic 管理**，单击**新建**。
3. 在编辑 Topic 窗口中，选择分区数和副本数等信息。
![](https://qcloudimg.tencent-cloud.cn/raw/3d56db2b59a50acd20bf2a97464098ce.png)

### 设置 CKafka  登录用户[](id:method1)
1. 在 CKafka 实例详情页面中，单击**用户管理**，进入用户管理页面。
![](https://qcloudimg.tencent-cloud.cn/raw/8c6c49b32c25a5d2d0e061bc4958c745.png)
2. 点击**新建**，依次输入**用户名**、**密码**、**确认密码**。后续iPaaS连接器配置需填写对应字段。
![kafka-new-user](https://qcloudimg.tencent-cloud.cn/raw/3df7602f1fd199372794ea183125506f/kafka-new-user.png)

###  设置 ACL 策略（可选）
1. 进入对应实例的 ACL 策略管理页面。
![](https://qcloudimg.tencent-cloud.cn/raw/f89cc906be484920aef2e9c7376b88cb.png)
2. 单击**批量设置**或单击某一 Topic 右侧的**编辑ACL策略**链接，进入新建 ACL 策略。
![](https://qcloudimg.tencent-cloud.cn/raw/9c814afa923aa5f4b9a04449892fd9ef.png)
3. 勾选要设置 ACL 策略的 Topic，并在下方 ACL 策略栏中针对用户和 IP 配置读写策略。
>?配置 IP 地址为“ * ” 表示允许全部 IP 访问。

## 接入配置
配置鹊桥 iPaaS Kafka 连接器连接属性步骤如下：
1.  在[iPaaS平台](https://console.cloud.tencent.com/ipaas)上单击**新建应用**，选择**空白应用**进行创建。
![](https://qcloudimg.tencent-cloud.cn/raw/f0e3a02558a61e6168e4a6c993931820.png)
2. 单击左侧的**集成流**展开选择**NewFlow**在画布中单击**+**选择**Apache Kafka 连接器**相关操作。
![](https://qcloudimg.tencent-cloud.cn/raw/188f6b9dbdd2c8c618f417ea3d293ba6.png)
3. 单击右侧的**新建连接器配置**并按照指引填入相关参数。
![](https://qcloudimg.tencent-cloud.cn/raw/8112f535875f2cacfdb1fd2bf36fd3f4.png)
4. 单击**下一步**以使用SASL/PLAINTEXT接入点为例，在连接器配置参数中，依次填写如下配置：
 - 集群地址：填入 CKafka 公网接入域名，可参考 [获得公网访问的域名和接口](#method2)
 - 集群 Kafka 版本：根据购买的Kafka实例版本选择对应的版本
 - SASL安全认证模式：选择 SASL/PLAINTEXT
 - SASL用户名：CKafka 此处的填写规则为 **CKafka实例ID#CKafka用户名**，假设CKafka实例ID为ckafka-instance1，[设置 CKafka  登录用户](#method1) 中设置的用户名为 kafkaUser，则此处用户名应填写：**ckafka-instance1#kafkaUser**
 - SASL密码：请填写 [设置 CKafka  登录用户](#method1) 中创建的用户密码
 - 使能TLS安全传输协议：选择false
![](https://qcloudimg.tencent-cloud.cn/raw/a98033fee48fdf62ca44170db08af91b.png)
5. 其他 Kafka 参数请按实际情况填写，也可参考 [Apache Kafka 连接器使用指南](https://cloud.tencent.com/document/product/1270/55465)。






