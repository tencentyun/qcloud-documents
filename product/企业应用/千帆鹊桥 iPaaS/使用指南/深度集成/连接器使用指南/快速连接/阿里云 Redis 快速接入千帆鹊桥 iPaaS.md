
## 操作场景
iPaaS Redis 连接器支持 Redis 单点模式、哨兵模式、Cluster 集群模式的连接及常用操作。
本文以 Redis 单点模式为例，为您介绍主流云厂商 Redis 产品的接入流程。


## 前期准备
您需要开通 Redis，并配置好外网访问规则和公网访问连接地址。

### 购买云数据库 Redis 实例

根据业务需求 [购买云数据库 Redis](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，并设置对应的管理员账密[](id:method2)。
![](https://qcloudimg.tencent-cloud.cn/raw/a0d49b5cf55416fbb4d3fb2a44880bdd.png)


### 开通公网访问

1. 登录 [云数据库Redis控制台](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)（注意地域选择），选择目标实例，单击**实例名称**，进入实例的**基本信息**页面。在**连接信息**>**公网访问**处，单击**申请连接地址**。
![](https://qcloudimg.tencent-cloud.cn/raw/24787d3093696a5008ff188122a20bbf.png)
2. 单击**确认**提交申请。
![](https://qcloudimg.tencent-cloud.cn/raw/a7c77d3d8d9bcabf43e10c0f28cffd2a.png)
3. 配置成功后，控制台页面会显示公网连接地址及端口号。后续填写在iPaas Redis连接器配置中[](id:method1)。
![](https://qcloudimg.tencent-cloud.cn/raw/ddde86cc63d34646e9a139d9d936f373.png)

### 设置访问白名单
登录 [云数据库Redis控制台](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)（注意地域选择），选择目标实例，单击**实例名称**，进入实例的**基本信息**页面。在左侧导航中单击**白名单设置**>**添加白名单分组**设置0.0.0.0/0 允许被访问。
>! 若需配置指定的 iPaaS 出口 IP 访问，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系我们。
>
![](https://qcloudimg.tencent-cloud.cn/raw/f9a3226b46a053a32a6925fbe98918ff.png)

## 接入配置
配置鹊桥 iPaaS Database 连接器连接属性步骤如下：

1. 在 [千帆鹊桥 iPaaS 控制台](https://console.cloud.tencent.com/ipaas)，单击**新建应用**，选择**空白应用**进行创建。
![](https://qcloudimg.tencent-cloud.cn/raw/f0e3a02558a61e6168e4a6c993931820.png)
2. 单击左侧的**集成流**展开选择**NewFlow**在画布中单击**+**选择**Redis连接器**相关操作。
![](https://qcloudimg.tencent-cloud.cn/raw/865f5d010b10fd5084f3c02d121e9d48.png)
3. 单击右侧的**新建连接器配置**并按照指引填入相关参数。
![](https://qcloudimg.tencent-cloud.cn/raw/b1a4c023f49bc1192b8c7b1a4347dc68.png)
4. 填写完连接器配置参数后，单击**测试连接**，测试连通性，测试成功后，会出现”连接配置正确“的提示，保存连接器配置即可，失败根据提示来重新填写对应信息。
 - Redis 连接模式：此处选择 Noncluster 模式
 - 地址：填写 [外网访问域名](#method1)
 - 端口号：填写 [数据库访问端口](#method1)
 - 密码：填写 [购买数据库时的密码](#method2)
![](https://qcloudimg.tencent-cloud.cn/raw/520072c2a7dc07f864885dd5cec52a6b.png)
5. 其他相关配置可参考 [Redis连接器使用指南](https://cloud.tencent.com/document/product/1270/55479)。



