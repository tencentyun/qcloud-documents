## 操作场景
千帆鹊桥 iPaaS 中的 Kafka 连接器支持 PLAINTEXT、SASL_PLAINTEXT、SASL_SCRAM 三种认证方式接入 Kafka 集群，可使用任一被支持的认证方式接入到 Kafka 集群。

## 前期准备
### 前提条件
已配置好安全组规则和公网 IP，并开通 Kafka 服务。

**华为云仅以下地域支持开通公网访问：**
- 华北-北京一华北-北京四
- 华北-乌兰察布一
- 华东-上海一
- 华东-上海二
- 华南-广州


### 设置安全组
1. 登录华为云控制台，进入 [安全组](https://console.huaweicloud.com/vpc/?region=cn-south-1#/secGroups) 设置。
2. 新建安全组或者修改已有安全组。
![](https://qcloudimg.tencent-cloud.cn/raw/a2f566787654a5d2eb9407203ce596a8.png)
<dx-tabs>
:::新建安全组

1. 单击控制台右上角的**创建安全组**，进入安全组创建页面，模板选择自定义。
 ![image-20220325104730507](https://qcloudimg.tencent-cloud.cn/raw/d3ca1fde6c2d3c47b7467ce786426fb6/image-20220325104730507.png)
2. 单击配置规则。
 ![image-20220325104804412](https://qcloudimg.tencent-cloud.cn/raw/548e0e1698827d26b9888b0adf3640ce/image-20220325104804412.png)
3. 添加如下入站规则。


 | 方向   | 协议 | 端口 | 源地址    | 说明                                  |
 | ------ | ---- | ---- | --------- | ------------------------------------- |
 | 入方向 | TCP  | 9094 | 0.0.0.0/0 | 通过公网访问 Kafka（关闭 SSL 加密）。    |
 | 入方向 | TCP  | 9092 | 0.0.0.0/0 | 通过 VPC 内网访问 Kafka（关闭 SSL 加密）。 |
 | 入方向 | TCP  | 9095 | 0.0.0.0/0 | 通过公网访问 Kafka（开启 SSL 加密）。    |
 | 入方向 | TCP  | 9093 | 0.0.0.0/0 | 通过 VPC 内网访问 Kafka（开启 SSL 加密）。 |
 | 入方向 | TCP  | 9999 | 0.0.0.0/0 | 访问 Kafka Manager。                   |
:::
::: 修改已有安全组

1. 在安全组实例列表中，点击要修改的安全组实例右侧的**配置规则**，对已有规则进行修改。
![image-20220325105256075](https://qcloudimg.tencent-cloud.cn/raw/9e5ded4fbde443bfd6b4c82f9398654e/image-20220325105256075.png)
2. 修改入方向规则，添加如下入站规则。


 | 方向   | 协议 | 端口 | 源地址    | 说明                                  |   
 | ------ | ---- | ---- | --------- | ------------------------------------- |
 | 入方向 | TCP  | 9094 | 0.0.0.0/0 | 通过公网访问 Kafka（关闭 SSL 加密）。    |
 | 入方向 | TCP  | 9092 | 0.0.0.0/0 | 通过 VPC 内网访问 Kafka（关闭 SSL 加密）。 |
 | 入方向 | TCP  | 9095 | 0.0.0.0/0 | 通过公网访问 Kafka（开启 SSL 加密）。    |
 | 入方向 | TCP  | 9093 | 0.0.0.0/0 | 通过 VPC 内网访问 Kafka（开启 SSL 加密）。 |
 | 入方向 | TCP  | 9999 | 0.0.0.0/0 | 访问 Kafka Manager。                   |
 
:::
</dx-tabs>

### 购买公网 IP

1. 进入 [弹性公网IP控制台](https://console.huaweicloud.com/vpc/?region=cn-south-1#/eips)，点击右上角的**购买弹性公网IP**。
![](https://qcloudimg.tencent-cloud.cn/raw/651e5338bfe657d562f3e9c29be869b6.png)
2. 按实际情况选择计费模式，设置区域，线路和带宽等参数。
3. 单击**立即购买**。
![image-20220325110114446](https://qcloudimg.tencent-cloud.cn/raw/0c3582d96bbb61f27db682f8b636f852/image-20220325110114446.png)

## 接入配置

### 步骤1：设置 Kafka 接入方式

1. 登录 [消息队列 Kafka 控制台](https://console.huaweicloud.com/dms/?engine=kafka&agencyId=344eb50173f9430489ff1be6c4769e54&region=cn-south-1&locale=zh-cn#/queue/manager/newKafkaList)，在实例列表中选择要设置的实例。
![](https://qcloudimg.tencent-cloud.cn/raw/ed4b9d76ae726394e4bd7d6fcd4bb5cc.png)
2. 单击实例名称进入详情页，单击安全组，完成安全组绑定。
若前置条件中直接修改的是 Sys-default 安全组，可省略该步骤。
![](https://qcloudimg.tencent-cloud.cn/raw/2567bcc66808ed543cc71ece8293485c.png)
3. 打开公网访问，从可用弹性IP中选择公网IP进行绑定，并确定。
![](https://qcloudimg.tencent-cloud.cn/raw/a576ce96b30ace5d93a28836c878cc72.png)
4. 等待公网绑定结束后，即可获取到公网访问地址，SASL_SSL 模式的设置可参考 [华为云帮助文档](https://support.huaweicloud.com/intl/zh-cn/usermanual-kafka/kafka-ug-180604013.html)[](id:method1)。
>!华为云 Kafka 实例不支持动态修改 SASL_SSL 模式，请重新创建实例，并在创建实例时开启 SASL_SSL 认证。
>
![](https://qcloudimg.tencent-cloud.cn/raw/4e3389c2f43a175b892d231c668ff25a.png)


### 步骤2： 配置鹊桥 iPaaS Kafka 连接器连接属性 
1. 在[iPaaS平台](https://console.cloud.tencent.com/ipaas)上单击**新建应用**，选择**空白应用**进行创建。
![](https://qcloudimg.tencent-cloud.cn/raw/f0e3a02558a61e6168e4a6c993931820.png)
2. 单击左侧的**集成流**展开选择 **NewFlow** 在画布中单击**+**选择**Apache Kafka 连接器**相关操作。
![](https://qcloudimg.tencent-cloud.cn/raw/188f6b9dbdd2c8c618f417ea3d293ba6.png)
3. 单击右侧的**新建连接器配置**并按照指引填入相关参数。
![](https://qcloudimg.tencent-cloud.cn/raw/8112f535875f2cacfdb1fd2bf36fd3f4.png)

4. 单击**下一步**以使用PLAINTEXT接入点为例，在连接器配置参数中，依次填写如下配置：
 - 集群地址：填入Kafka公网连接地址，可参考 [获取公网访问地址](#method1)
 - 集群Kafka版本：根据购买的Kafka实例版本选择对应的版本
 - SASL安全认证模式：选择 PLAINTEXT
 - 使能TLS安全传输协议：选择 false
![](https://qcloudimg.tencent-cloud.cn/raw/3cad80a06f2e9b7e3bd9ac98fc43ae9b.png)
5. 其他 Kafka 参数请按实际情况填写，也可参考 [Apache Kafka 连接器使用指南](https://cloud.tencent.com/document/product/1270/55465)。

