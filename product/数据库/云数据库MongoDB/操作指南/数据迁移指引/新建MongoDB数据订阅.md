本场景介绍使用 DTS 创建腾讯云数据库 MongoDB 的数据订阅任务操作指导。

## 版本说明
- 目前仅支持对腾讯云 MongoDB 的数据订阅，具体版本为3.6、4.0、4.2、4.4。
- MongoDB 3.6版本仅支持集合级别的订阅。

## 前提条件
- 已准备好待订阅的腾讯云数据库，并且数据库版本符合要求，请参见 [数据订阅支持的数据库](https://cloud.tencent.com/document/product/571/59965)。
- 建议在源端实例中创建只读帐号，可参考如下语法进行操作。源库为腾讯云 MongoDB 的，也可[在 MongoDB 控制台创建只读帐号](https://cloud.tencent.com/document/product/240/32721)。
```
# 创建全实例只读帐号
use admin
db.createUser({
  user: "username",  
  pwd: "password",  
  roles:[    
         {role: "readAnyDatabase",db: "admin"}  
        ]
})

# 创建指定库只读帐号
use admin
db.createUser({
  user: "username",  
  pwd: "password",  
  roles:[    
         {role: "read",db: "指定库的库名"}
        ]
})
```

## 注意事项
- 订阅的消息内容目前默认保存时间为最近1天，超过保存时间的数据会被清除，请用户及时消费，避免数据在消费完之前就被清除。
- 数据消费的地域需要与订阅实例的地域相同。 
- DTS 中内置的 Kafka 处理单条消息有一定上限，当源库中的单行数据超过10MB时，这条数据在消费端可能会被丢弃。
- 在源数据库中删除已选订阅对象的指定库或者集合后，该库或者集合的订阅数据（Change Stream）将会被无效化，即使在源数据库中重建该库或者集合也无法续订数据，需要重置订阅任务，重新勾选订阅对象。

## 支持订阅的 SQL 操作

| 操作类型 | 支持的 SQL 操作                                              |
| -------- | ------------------------------------------------------------ |
| DML      | INSERT、UPDATE、DELETE                                       |
| DDL      | INDEX：createIndexes、createIndex、dropIndex、dropIndexes COLLECTION：createCollection、drop、collMod、renameCollection DATABASE：dropDatabase、copyDatabase |

## 订阅配置步骤
1. 登录 [DTS 控制台](https://console.cloud.tencent.com/dts/dss)，在左侧导航选择**数据订阅**，单击**新建数据订阅**。
2. 在新建数据订阅页，选择相应配置，单击**立即购买**。
 - 计费模式：支持**包年包月**和**按量计费**。
 - 地域：地域需与待订阅的数据库实例地域保持一致。
 - 数据库：选择 **MongoDB**。
 - 版本：选择 **kafka 版**，支持通过 Kafka 客户端直接消费。
 - 订阅实例名称：编辑当前数据订阅实例的名称。
 - 购买数量：单次购买最多支持10个任务。
3. 购买成功后，返回数据订阅列表，选择刚才购买的任务，在**操作**列单击**配置订阅**。
![](https://qcloudimg.tencent-cloud.cn/raw/f51308eb148cf30e40bb4dc423bb6fff.png)
4. 在配置数据库订阅页面，配置源库信息后，单击**测试连通性**，通过后单击**下一步**。
 - 接入类型：目前仅支持**云数据库**。
 - 云数据库实例：选择云数据库实例 ID。
 - 数据库帐号/密码：添加订阅实例的帐号和密码，帐号具有只读权限。
 - kafka 分区数量：设置 kafka 分区数量，增加分区数量可提高数据写入和消费的速度。单分区可以保障消息的顺序，多分区无法保障消息顺序，如果您对消费到消息的顺序有严格要求，请选择 kafka 分区数量为1。
<img src="https://qcloudimg.tencent-cloud.cn/raw/9433884ea107b171728ebe644210d4c2.png"  style="zoom:40%;">
5. 在订阅类型和对象选择页面，选择订阅参数后，单击**保存配置**。
![](https://qcloudimg.tencent-cloud.cn/raw/346774ee98c3e49bc8e35fd63464c39a.png)
<table>
<thead><tr><th>参数</th><th>说明</th></tr></thead>
<tbody><tr>
<td>订阅类型</td>
<td>默认Change Stream，不可修改。</td></tr>
<tr>
<td>订阅级别</td>
<td>订阅级别，包括全实例、库和集合。<ul><li>全实例：订阅全实例数据。</li><li>库：订阅库级别的数据，选择后，下面的任务设置中，只能选择一个库。</li><li>集合：订阅集合级别的数据，选择后，下面的任务设置中，只能选择一个集合。</li></ul></td></tr>
<tr>
<td>任务设置</td>
<td>勾选需要订阅的库、集合。仅支持选择一个库或者一个集合。</td></tr>
<tr>
<td>输出聚合设置</td>
<td>勾选后， 聚合管道的执行顺序由页面上的配置顺序决定。更多聚合管道信息及其使用示例，请参见 <a href="https://www.mongodb.com/docs/manual/changeStreams/#modify-change-stream-output">MongoDB 官网文档</a>。</td></tr>
<tr>
<td>Kafka 分区策略</td>
<td><ul><li>按集合名分区：将源库的订阅数据按照集合名进行分区，设置后相同集合名的数据会写入同一个 Kafka 分区中。</li><li>自定义分区策略：先通过正则表达式对订阅数据中的库名和集合名进行匹配，匹配到的数据再按照集合名分区、集合名 + objectid 分区。</li></ul></td></tr>
</tbody></table>
6. 在预校验页面，预校验任务预计会运行2分钟 - 3分钟，预校验通过后，单击**启动**完成数据订阅任务配置。
>?如果校验失败，请参考 [校验不通过处理方法](https://cloud.tencent.com/document/product/571/58685) 进行修正，并重新进行校验。
>
![](https://qcloudimg.tencent-cloud.cn/raw/0c06e3d6bb88fe23f1462d37a48a0644.png)
7. 订阅任务进行初始化，预计会运行3分钟 - 4分钟，初始化成功后进入**运行中**状态。

## 后续操作
1. [新增消费组](https://cloud.tencent.com/document/product/571/52377)。
数据订阅 Kafka 版的消费依赖于 Kafka 的消费组，所以在消费数据前需要创建消费组。数据订阅 Kafka 版支持用户创建多个消费组，进行多点消费。
2. [消费订阅数据](https://cloud.tencent.com/document/product/571/52381)。
订阅任务进入运行中状态之后，就可以开始消费数据。Kafka 的消费需要进行密码认证，具体内容请参考 [消费订阅数据](https://cloud.tencent.com/document/product/571/52381) 中的 Demo，我们提供了多种语言的 Demo 代码，也对消费的主要流程和关键的数据结构进行了说明。

