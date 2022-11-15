


## 场景说明

本文档满足如下场景：将 PostgreSQL 表的数据(存量+增量)实时同步数据同步到目标ES索引。实时同步需要同步新增，修改和删除操作。即当 PostgreSQL 源表出现新增、修改、删除时，目标 ES 中的数据也需要发生相应的增删改。

## 使用限制

本种实时同步增删改的任务。一个订阅任务只能订阅一张表的数据，一个 Topic 里面只能存一个表的订阅数据。即订阅一张表的数据到 ES 需要创建一个订阅任务，一个 Topic，一个数据流出任务。同时为了保证数据同步的有序性，一个 Topic 只支持一个分区。

>?如果需要同步多张表的数据到 ES 里面。则需要创建多个 Topic，同时创建多个订阅任务和流出任务。



## 操作步骤

操作步骤分为四步：
<dx-steps>
-[创建连接](#step1)
-[创建 Topic](#step2)
-[创建数据订阅任务](#step3)
-[创建数据流出任务](#step4)
</dx-steps>


[](id:step1)
### 步骤1：创建连接

#### 1. 创建 PostgreSQL 连接

1. 单击**数据接入平台**中的 **连接列表**，单击**新建连接**，选择 TDSQL-C 数据库。
<img src="https://qcloudimg.tencent-cloud.cn/raw/c756bb62774bf1db51d480d52a93e58f.png" width = "60%" height = "60%"> 
2. 填写需要同步的 PostgreSQL 数据库的相关信息。
<img src="https://qcloudimg.tencent-cloud.cn/raw/51463aafe856a3038abfe0091c5b7b0a.png" width = "50%" height = "80%"> 

#### 2. 创建 Elasticsearch 连接

1. 单击**数据接入平台**中的 **连接列表**，单击**新建连接**，选择 **Elasticsearch Service**。
<img src="https://qcloudimg.tencent-cloud.cn/raw/d701ec1635998d0d2e956da7a9b75078.png" width = "40%" height = "40%"> 
2. 配置 ES 相关的参数：
<img src="https://qcloudimg.tencent-cloud.cn/raw/1eb88b4454f5d3c82263b11a3c1af2d7.png" width = "40%" height = "40%"> 


[](id:step2)
### 步骤2：创建 Topic

创建 Topic 有两种方式，如果已购买 kafka 实例，则直接在实例中新建 Topic 即可。否则，可以新建按量付费的 Topic（无需购买实例）。购买按量付费 Topic 操作步骤如下：

进入 Ckafka 控制台，单击**数据接入平台**中的 **Topic 列表**，单击新建 Topic。（**若计划将数据同步至 Ckafka 实例中的 topic 则可跳过此步骤**）
<img src="https://qcloudimg.tencent-cloud.cn/raw/e1ec61b337488a72548560e1a2fcc356.png" width = "60%" height = "60%">


[](id:step3)
### 步骤3：创建数据订阅任务

1. 单击 **数据接入平台** 中的 **任务管理**，单击**任务列表**，单击**新建任务**。
<img src="https://qcloudimg.tencent-cloud.cn/raw/3a642bf5bab01564c0ef9443eccf8c8b.png" width = "50%" height = "50%"> 
2. 单击**下一步**，填写数据源配置信息，数据源为 **步骤一** 中创建的 Postgresql 订阅连接：
<img src="https://qcloudimg.tencent-cloud.cn/raw/62600bac03df622d8dabfc671e72e106.png" width = "50%" height = "50%"> 
3. 继续单击**下一步**，选择数据目标信息，即同步 PostgreSQL 数据的 topic，根据实际情况选择 DIP Topic 或 CKafka Topic 即可，此处选择 **步骤二 **中创建的 DIP topic：
<img src="https://qcloudimg.tencent-cloud.cn/raw/dc83fca27670a5dcd416dcc4779c94c4.png" width = "50%" height = "50%"> 
4. 任务创建成功后，在**任务详情 - 查看消息**可以看到订阅的数据信息：
<img src="https://qcloudimg.tencent-cloud.cn/raw/89e7d0075042d218298c98ec6a6e0394.jpg" width = "60%" height = "60%"> 
只有源表有数据存在的时候，才会订阅到消息。当源表没有数据时，可执行如下类似的 insert 语句，触发订阅行为，即可查询到订阅的数据：
<dx-codeblock>
:::  sql
insert into test values('testname',25);
:::
</dx-codeblock>



[](id:step4)
### 步骤4：创建数据流出任务

1. 新建连接后，单击**任务管理->任务列表**，单击**新建任务**，任务类型选择**数据流出**，选择**Elasticsearch Service**：
<img src="https://qcloudimg.tencent-cloud.cn/raw/77a09f68dbbc077b413d6653aec65d4e.png" width = "40%" height = "40%"> 
2. 配置数据源，选择同步了 mysql 数据的 topic，这里选择 [步骤1](#step1) 中的 topic，选择 **从最开始位置开始消费**。
<img src="https://qcloudimg.tencent-cloud.cn/raw/8a69cf6307ee15f0503bd127b2ecc43c.png" width = "40%" height = "40%"> 
3. 下一步中数据处理可根据实际情况进行配置，这里不进行相关配置，使用原始消息数据。最后进行 ES 相关配置，其中主键为数据库表的主键名称。
<dx-alert infotype="notice" title="">
此模式需要开启 **数据库同步模式**，并填写表的主键的列名，如此处主键列名为 **id**。
<img src="https://qcloudimg.tencent-cloud.cn/raw/dea34d9dc0e9d56f429fa4924875b546.png" width = "60%" height = "60%">  
</dx-alert>
4. 	当数据任务运行后，即可在 ES 对应的索引中查询到相应的消息。
