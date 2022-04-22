# 腾讯云 Redis 快速接入千帆鹊桥 iPaaS
## 使用场景
iPaaS Redis连接器支持Redis单点模式、哨兵模式、Cluster集群模式的连接及常用操作，本文以Redis单点模式为例，介绍主流云厂商Redis产品的接入流程。
## 操作指南
### 前期准备
> *前置条件：开通Redis，并配置好外网访问规则和公网访问连接地址* 
#### 购买云数据库Redis
>！网络类型选择“私有网络”，“基础网络”不能开启公网地址访问

登录[腾讯云数据库Redis购买页面](https://buy.cloud.tencent.com/redis?regionId=8)，根据需求购买云数据库并设置密码[](id:method2)。

![](https://qcloudimg.tencent-cloud.cn/raw/7e26ab09e99ad31b479c34814230d571.png)

#### 设置安全组
设置允许iPaaS出口IP访问数据库的操作。详细可参考[Redis配置安全组](https://cloud.tencent.com/document/product/239/30911)
<dx-tabs>
:::新建安全组
  
i.点击[安全组](https://console.cloud.tencent.com/vpc/securitygroup?rid=8&rid=8)或购买页面的**自定义安全组**按钮，进入安全组创建页面。
![](https://qcloudimg.tencent-cloud.cn/raw/333b8d9d584e9ecad29591dafffb3382.png)
ii.模板选择自定义或放通全部端口。
    ![](https://qcloudimg.tencent-cloud.cn/raw/31cf4340d5c42857a277ebcb2545cc5e.jpg)

iii.点击配置规则(选择自定义需操作此步骤，上一步选择全部端口放通单击确定即可)  
![](https://qcloudimg.tencent-cloud.cn/raw/de71cb94854233ad1ce7be789075b3d6.png)

vi.添加如下入站规则

| 方向   | 协议 | 端口 | 源地址    | 说明                                |
| :------------- | ---- | ---- | --------- | ------------------------------------- |
| 入方向 | TCP  | ALL（若数据库自定义端口填写自定义端口号） | 0.0.0.0/0 | 开启通过公网访问 redis|
 >! 若需配置指定的iPaaS出口IP访问，请提工单联系。
:::
::: 选择已有安全组后修改

i.在[安全组实例列表](https://console.cloud.tencent.com/vpc/securitygroup?rid=8&rid=8)中，点击已绑定Redis数据库的安全组右侧的*修改规则*按钮，对已有规则进行修改

![](https://qcloudimg.tencent-cloud.cn/raw/c7413fc7c2727bbfbd5031290498d4bb.png)

ii.修改入方向规则，添加如下入站规则

 | 方向   | 协议 | 端口 | 源地址    | 说明                                |
 | :-------------  | ---- | ---- | --------- | ------------------------------------- |
 | 入方向 | TCP  |ALL（若数据库自定义端口填写自定义端口号） | 0.0.0.0/0 | 开启通过公网访问 redis|
 >! 若需配置指定的iPaaS出口IP访问，请提工单联系。
:::

</dx-tabs>

#### 开启外网地址访问
1. 登录[云数据库Redis实例控制台](https://console.cloud.tencent.com/redis?regionId=1#/)，在实例列表中选中想要设置的实例，进入实例管理页面，开启外网地址访问。

![image-20220407104543833](https://qcloudimg.tencent-cloud.cn/raw/fa6db66c930737444ca3023f04201f40.png)

2.配置成功后，控制台会显示外网地址。后续iPaaS连接器配置需填写对应字段[](id:method1)。

![image-20220407104750296](https://qcloudimg.tencent-cloud.cn/raw/e3b4f6b31e709937df08734d7460f387.png)

### 接入配置

#### 配置鹊桥 iPaaS Database连接器连接属性

1. 在[iPaaS平台](https://console.cloud.tencent.com/ipaas)上单击**新建应用**，选择**空白应用**进行创建。
![](https://qcloudimg.tencent-cloud.cn/raw/f0e3a02558a61e6168e4a6c993931820.png)
2. 单击左侧的**集成流**展开选择**NewFlow**在画布中单击**+**选择**Redis连接器**相关操作。
![](https://qcloudimg.tencent-cloud.cn/raw/865f5d010b10fd5084f3c02d121e9d48.png)
3. 单击右侧的**新建连接器配置**并按照指引填入相关参数。

![](https://qcloudimg.tencent-cloud.cn/raw/b1a4c023f49bc1192b8c7b1a4347dc68.png)

4. 填写完连接器配置参数后，单击**测试连接**，测试连通性，测试成功后，会出现”连接配置正确“的提示，保存连接器配置即可，失败根据提示来重新填写对应信息。

 - Redis连接模式：此处选择Noncluster模式
 - 地址：填写[外网访问域名](#method1)
 - 端口号：填写[数据库访问端口](#method1)
 - 密码：填写[购买数据库时的密码](#method2)
![image-20220407105800922](https://qcloudimg.tencent-cloud.cn/raw/0b6a7780d7569940645153668b4ebd95.png)
5. 其他相关配置可参考[Redis连接器使用指南](https://cloud.tencent.com/document/product/1270/55479)


