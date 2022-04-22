# 阿里云 Redis 快速接入千帆鹊桥 iPaaS
## 使用场景
iPaaS Redis连接器支持Redis单点模式、哨兵模式、Cluster集群模式的连接及常用操作，本文以Redis单点模式为例，介绍主流云厂商Redis产品的接入流程。
## 操作步骤
### 前期准备
> *前置条件：开通Redis，并配置好外网访问规则和公网访问连接地址* 

### 购买云数据库Redis实例

根据业务需求购买云数据库Redis，并设置对应的管理员账密[](id:method2)。
![image-20220407141316017](https://qcloudimg.tencent-cloud.cn/raw/25f65e1411f4b0ec5a3c39a48b7f5e25.png)
#### 开通公网访问

1. 登录[云数据库Redis控制台](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，注意地域选择，选择目标实例，单击**实例名称**，进入实例的**基本信息**页面。在**连接信息**>**公网访问**处，单击**申请连接地址**。

![image-20220407142145318](https://qcloudimg.tencent-cloud.cn/raw/ecd971486eae96c109f3601962d4b5ef.png)

2. 单击**确认**提交申请。
![image-20220407142233327](https://qcloudimg.tencent-cloud.cn/raw/a8bbceddf0a1d474bb4dd021e9eb68cb.png)

3. 配置成功后，控制台页面会显示公网连接地址及端口号。后续填写在iPaas Redis连接器配置中[](id:method1)。

![image-20220407142515884](https://qcloudimg.tencent-cloud.cn/raw/ba2d7809b6e5a2d6ec174663ba87a693.png)

#### 设置访问白名单
登录[云数据库Redis控制台](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，注意地域选择，选择目标实例，单击**实例名称**，进入实例的**基本信息**页面。在左侧导航中单击**白名单设置**>**添加白名单分组**设置0.0.0.0/0 允许被访问。
>! 若需配置指定的iPaaS出口IP访问，请提工单联系。

![](https://qcloudimg.tencent-cloud.cn/raw/f9a3226b46a053a32a6925fbe98918ff.png)

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

![image-20220407143035493](https://qcloudimg.tencent-cloud.cn/raw/b159ca7eca7c22e3c91b3df81ee10784.png)
5.其他相关配置可参考[Redis连接器使用指南](https://cloud.tencent.com/document/product/1270/55479)



