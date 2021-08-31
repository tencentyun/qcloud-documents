## 前提条件
流计算作业 ETL 作业需运行于流计算独享集群，若还没有集群，请参考 [创建独享集群](https://cloud.tencent.com/document/product/849/48298)。

## 步骤1：创建 ETL 作业
登录 [流计算 Oceanus 控制台](https://console.cloud.tencent.com/oceanus)，单击左侧导航**作业管理**，进入作业管理页面，单击**新建作业**，作业类型选中 **ETL 作业**，输入作业名称，并选择一个运行中的集群，新建的 ETL 作业将运行于此集群，单击**确定**后即成功创建作业。
![](https://main.qcloudimg.com/raw/5f95c942e9d1a84f939819bfdb2d816d.png)

## 步骤2：流计算服务委托授权
选择**作业管理**中刚新建的作业，单击**开发调试**。在未授权时，弹出访问授权对话框如下，单击**前往授权**，授权流计算作业访问您的消息队列或云数据库等资源。此授权的详细说明参见 [流计算服务委托授权](https://cloud.tencent.com/document/product/849/38290)。
![](https://main.qcloudimg.com/raw/ec69259360d4b73ba7962f1247b0f7aa.png)

## 步骤3：创建数据源表和目的表
授权完成后，进入**开发调试**，单击“数据源表”右侧的**添加**，选择数据源类型并输入对应信息，单击**确定**。
![](https://main.qcloudimg.com/raw/f7c17e2b06f582e93150b0ab25ed29e0.png)
单击“数据目的表”右侧的**添加**，选择数据源类型并输入对应信息，单击**确定**。数据源表和数据目的表都添加好后效果如图所示。
![](https://main.qcloudimg.com/raw/a8d154e123a06f3052fe7cbd431a70e3.png)


## 步骤4：配置字段映射
添加完数据源表和目的表后，即可配置字段映射。此处将数据源表的 id、name、age 都映射到目的表，将 weight 字段的值 * 2，映射到目的表的 weight 字段。
![](https://main.qcloudimg.com/raw/b03c99934b8cc2e26d993027e2080d6d.png)

## 步骤5：设置作业参数
在**作业参数**中可以设置 Checkpoint 和算子默认并行度的值。
![](https://main.qcloudimg.com/raw/06ab78133a06cbd830d507576fda20b5.png)

## 步骤6：发布运行 ETL 作业
单击**发布运行**，将进行作业运行检查，检查通过后将进入发布确认。单击**确认启动**即可启动作业，如果此时线上已有运行的版本，则会覆盖线上版本。
![](https://main.qcloudimg.com/raw/261d4e4a6db1ef55287d2b51e936a4ed.png)

## 步骤7：查看作业运行情况
作业发布并启动运行后，将变为操作中的状态，成功启动后将变为运行中的状态。作业运行中时，可以通过监控、日志、Flink UI 等功能查看作业运行的情况。
