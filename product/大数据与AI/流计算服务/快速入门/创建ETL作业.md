## 前提条件
流计算作业 ETL 作业需运行于流计算独享集群，若还没有集群，请参考 [创建独享集群](https://cloud.tencent.com/document/product/849/48298)。 

## 步骤1：创建 ETL 作业
登录 [流计算 Oceanus 控制台](https://console.cloud.tencent.com/oceanus)，进入某一工作空间后，单击左侧导航**作业管理**，进入作业管理页面，单击**新建作业**，作业类型选中 **ETL 作业**，输入作业名称，并选择一个运行中的集群，新建的 ETL 作业将运行于此集群，单击**确定**后即成功创建作业。
![](https://qcloudimg.tencent-cloud.cn/raw/34da335c753022921f8baa5759aae420.png)

>! 注意: 当前ETL作业暂时只支持1.13版Flink，尚不支持1.13版本内核的集群需要先提 [工单](https://console.cloud.tencent.com/workorder/category) 升级后再使用。

## 步骤2：流计算服务委托授权
选择**作业管理**中刚新建的作业，单击**开发调试**。在未授权时，弹出访问授权对话框如下，单击**前往授权**，授权流计算作业访问您的消息队列或云数据库等资源。此授权的详细说明参见 [流计算服务委托授权](https://cloud.tencent.com/document/product/849/38290)。
![](https://main.qcloudimg.com/raw/ec69259360d4b73ba7962f1247b0f7aa.png)

## 步骤3：配置数据源表
授权完成后，单击作业进入**作业开发-草稿**，从左侧列表拖入MySQL数据源。
![](https://qcloudimg.tencent-cloud.cn/raw/d0e013fd2fe2b5bec8965cdba90a40e3.png)
单击MySQL数据源可以进行数据源的配置。
![](https://qcloudimg.tencent-cloud.cn/raw/413ccbef32952618309114c33070e41a.png)

如果当前没有可用的数据库实例，可以单击**管理连接信息**，并单击新建连接信息增加新的数据源。
![](https://qcloudimg.tencent-cloud.cn/raw/02382da8815ab0a0183b41d8b3c11179.png)

**腾讯云实例**可以使用当前账号下的腾讯云产品实例，但注意账号需要拥有对应产品的查询列表权限。

**IP连接**则直接用填入的IP进行连接，需要确保IP与Oceanus集群处于同一个VPC或是有进行过相关的网络打通操作。

选择好数据源之后，可以通过下拉框选择需要进行同步的数据库与表。
![](https://qcloudimg.tencent-cloud.cn/raw/fcfec54ed541df23fb96a5831022aff9.png)
单击下一步，配置需要进行同步的字段，并单击确认完成配置。
![](https://qcloudimg.tencent-cloud.cn/raw/64259b2e70fea04a0d79084ef6b7558d.png)
再次返回画布，可以看到数据源已经配置完成。
![](https://qcloudimg.tencent-cloud.cn/raw/1d062fe5033f774f0ea830112d2e7f86.png)

## 步骤4：配置数据目的
从左侧拖入数据目的，并与数据源相连。
![](https://qcloudimg.tencent-cloud.cn/raw/2cc532634ecad0253d0fb973204f4cda.png)
单击数据目的对象，配置好数据库实例与库表选择
![](https://qcloudimg.tencent-cloud.cn/raw/f74808edc0937e8dd12c7265348015a9.png)
单击下一步进行字段映射配置
![](https://qcloudimg.tencent-cloud.cn/raw/9b2684b920576f713cb691fc405b315a.png)
完成后，单击确认完成数据目的的配置
![](https://qcloudimg.tencent-cloud.cn/raw/d4c47b68bb2f1d4f8c511a8024a3391b.png)

## 步骤5：设置作业参数
在**作业参数**中可以设置作业相关的参数，详情可以查看文档[作业高级参数](https://cloud.tencent.com/document/product/849/53391)。
![](https://qcloudimg.tencent-cloud.cn/raw/92ef1ed4d2bd78d15c82af1723877ba4.png)

## 步骤6：发布运行 ETL 作业
单击运行，会进行作业预检查，并启动作业。
![](https://qcloudimg.tencent-cloud.cn/raw/712341b417a79a74b2f8e20e4c20c2eb.png)
![](https://qcloudimg.tencent-cloud.cn/raw/0cd5a22e5145b863bf5e0820e68eaa75.png)

## 步骤7：查看作业日志
单击日志按钮可以查看作业日志。
![](https://qcloudimg.tencent-cloud.cn/raw/3c2eef2d3eb727eb484c425873cad400.png)

