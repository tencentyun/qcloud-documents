# 华为云 Kafka 快速接入千帆鹊桥 iPaaS
## 操作场景
千帆鹊桥 iPaaS 中的Kafka连接器支持 PLAINTEXT、SASL_PLAINTEXT、SASL_SCRAM 三种认证方式接入Kafka集群，可使用任一被支持的认证方式接入到Kafka集群
## 操作步骤
### 前期准备
> *前置条件：已配置好安全组规则和公网ip，并开通Kafka服务* 
>注意，华为云仅以下地域支持开通公网访问
>  **华北-北京一、华北-北京四、华北-乌兰察布一、华东-上海一、华东-上海二、华南-广州**
#### 设置安全组
1.登录控制台，进入[安全组](https://console.huaweicloud.com/vpc/?region=cn-south-1#/secGroups)设置，可新建安全组或者修改已有安全组
 ![image-20220325104610280](https://qcloudimg.tencent-cloud.cn/raw/a0b6024e6bf67010a69135170187de5e/image-20220325104610280.png)
<dx-tabs>
:::新建安全组

1. 点击控制台右上角创建安全组按钮，进入安全组创建页面，模板选择自定义

 ![image-20220325104730507](https://qcloudimg.tencent-cloud.cn/raw/d3ca1fde6c2d3c47b7467ce786426fb6/image-20220325104730507.png)

2. 点击配置规则
 ![image-20220325104804412](https://qcloudimg.tencent-cloud.cn/raw/548e0e1698827d26b9888b0adf3640ce/image-20220325104804412.png)

3. 添加如下入站规则

 | 方向   | 协议 | 端口 | 源地址    | 说明                                  |
 | ------ | ---- | ---- | --------- | ------------------------------------- |
 | 入方向 | TCP  | 9094 | 0.0.0.0/0 | 通过公网访问Kafka（关闭SSL加密）。    |
 | 入方向 | TCP  | 9092 | 0.0.0.0/0 | 通过VPC内网访问Kafka（关闭SSL加密）。 |
 | 入方向 | TCP  | 9095 | 0.0.0.0/0 | 通过公网访问Kafka（开启SSL加密）。    |
 | 入方向 | TCP  | 9093 | 0.0.0.0/0 | 通过VPC内网访问Kafka（开启SSL加密）。 |
 | 入方向 | TCP  | 9999 | 0.0.0.0/0 | 访问Kafka Manager。                   |
:::
::: 修改已有安全组

1. 在安全组实例列表中，点击要修改的安全组实例右侧的*配置规则*按钮，对已有规则进行修改

![image-20220325105256075](https://qcloudimg.tencent-cloud.cn/raw/9e5ded4fbde443bfd6b4c82f9398654e/image-20220325105256075.png)

2. 修改入方向规则，添加如下入站规则

 | 方向   | 协议 | 端口 | 源地址    | 说明                                  |   
 | ------ | ---- | ---- | --------- | ------------------------------------- |
 | 入方向 | TCP  | 9094 | 0.0.0.0/0 | 通过公网访问Kafka（关闭SSL加密）。    |
 | 入方向 | TCP  | 9092 | 0.0.0.0/0 | 通过VPC内网访问Kafka（关闭SSL加密）。 |
 | 入方向 | TCP  | 9095 | 0.0.0.0/0 | 通过公网访问Kafka（开启SSL加密）。    |
 | 入方向 | TCP  | 9093 | 0.0.0.0/0 | 通过VPC内网访问Kafka（开启SSL加密）。 |
 | 入方向 | TCP  | 9999 | 0.0.0.0/0 | 访问Kafka Manager。                   |
 
:::
</dx-tabs>

#### 购买公网ip

1. 进入公网ip控制台，点击右上角购买弹性公网ip

 ![image-20220325105957204](https://qcloudimg.tencent-cloud.cn/raw/da9d0685e106381d7ddf3ce35933d556/image-20220325105957204.png)

2. 按实际情况选择计费模式，设置区域，线路和带宽等参数，点击立即购买

![image-20220325110114446](https://qcloudimg.tencent-cloud.cn/raw/0c3582d96bbb61f27db682f8b636f852/image-20220325110114446.png)

### 接入配置

#### 步骤1： 设置 Kafka 接入方式

1.登录控制台，在实例列表中选择要设置的实例

![image-20220224145347641](https://qcloudimg.tencent-cloud.cn/raw/bff5ac162a47c8e25853402da57c05e7/image-20220224145347641.png)

2. 点击实例名称进入详情页，点击安全组，完成安全组绑定；若前置条件中直接修改的是Sys-default安全组，可省略该步骤

![image-20220224145606576](https://qcloudimg.tencent-cloud.cn/raw/8ed329606e8c994046017488a0597acd/image-20220224145606576.png)

![image-20220325110528408](https://qcloudimg.tencent-cloud.cn/raw/d8461f6051b0daa2cbab61e8e33085a8/image-20220325110528408.png)

3. 打开公网访问，从可用弹性ip中选择公网ip进行绑定，并确定

![image-20220224145722491](https://qcloudimg.tencent-cloud.cn/raw/50bf93c05fb3860bae9f7939befbdc3f/image-20220224145722491.png)

4. 等待公网绑定结束后，即可获取到公网访问地址，SASL_SSL模式的设置可参考[华为云帮助文档](https://support.huaweicloud.com/intl/zh-cn/usermanual-kafka/kafka-ug-180604013.html)[](id:method1)

> 注意：华为云Kafka实例不支持动态修改SASL_SSL模式，请重新创建实例，并在创建实例时开启SASL_SSL认证

![image-20220224145822273](https://qcloudimg.tencent-cloud.cn/raw/dbf4fbb3d6aaa4b2aeeeb50ed0d9132f/image-20220224145822273.png)

#### 步骤2： 配置鹊桥 iPaaS Kafka 连接器连接属性 
1. 在[iPaaS平台](https://console.cloud.tencent.com/ipaas)上单击**新建应用**，选择**空白应用**进行创建。
![](https://qcloudimg.tencent-cloud.cn/raw/f0e3a02558a61e6168e4a6c993931820.png)
2. 单击左侧的**集成流**展开选择**NewFlow**在画布中单击**+**选择**Apache Kafka 连接器**相关操作。
![](https://qcloudimg.tencent-cloud.cn/raw/188f6b9dbdd2c8c618f417ea3d293ba6.png)
3. 单击右侧的**新建连接器配置**并按照指引填入相关参数。
![](https://qcloudimg.tencent-cloud.cn/raw/8112f535875f2cacfdb1fd2bf36fd3f4.png)

4. 单击**下一步**以使用PLAINTEXT接入点为例，在连接器配置参数中，依次填写如下配置：

 - 在集群地址栏中填入Kafka公网连接地址，可参考[获取公网访问地址](#method1)
 - 集群Kafka版本根据购买的Kafka实例版本选择对应的版本
 - SASL安全认证模式选择PLAINTEXT
 - 使能TLS安全传输协议：选择false

![image-20220224155146910](https://qcloudimg.tencent-cloud.cn/raw/07590c36fb16e5a753245965133872cd/image-20220224155146910.png)

5. 其他Kafka参数请按实际情况填写，也可参考 [Apache Kafka 连接器使用指南](https://cloud.tencent.com/document/product/1270/55465)

