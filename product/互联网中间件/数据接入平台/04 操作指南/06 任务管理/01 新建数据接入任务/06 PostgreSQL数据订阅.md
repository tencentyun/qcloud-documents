## 操作场景

数据接入平台 DIP 支持接入各种数据源产生的不同类型的数据，统一管理，再分发给下游的离线/在线处理平台，构建清晰的数据通道

DIP 支持订阅 PostgreSQL 变更数据，免去对基于 CDC 的订阅组件如（Canal、Debezium 等）的运维成本。本文介绍在 DIP 控制台创建 PostgreSQL 数据接入任务的操作方法。

## 前提条件

- 已创建好数据目标 Topic。
- 已创建好数据源 PostgreSQL 连接。

## 操作步骤

1. 登录 [DIP 控制台](https://console.cloud.tencent.com/ckafka/datahub-overview)。
2. 在左侧导航栏单击**任务管理** > **任务列表**，选择好地域后，单击**新建任务**。
3. 填写任务名称，任务类型选择**数据接入**，数据源类型选择 **PostgreSQL 数据订阅**，单击**下一步**。
4. 填写数据源配置信息。
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">说明</th>
</tr>
</thead>
<tbody><tr>
<td align="left">数据源</td>
<td align="left">选择提前创建好的 PostgreSQL 源数据连接</td>
</tr>
<tr>
<td align="left">database</td>
<td align="left">选择要监听的数据库。</td>
</tr>
<tr>
<td align="left">Table</td>
<td align="left">支持两种种选择方式：<ul><li>批量选择：支持手动勾选要订阅的数据库和表，支持订阅多个数据库、多个表。</li><li>正则匹配：支持使用正则匹配筛选订阅符合条件的表。</li></ul></td>
</tr>
<tr>
<td align="left">监听全部表</td>
<td align="left">如果需要捕捉到表内数据的更新与删除，需要该表存在主键。
update 和 delete 需要转储更新前的数据，需要将表的配置项"REPLICA IDENTITY"设置成"FULL"</td>
</tr>
</tbody></table>

![](https://qcloudimg.tencent-cloud.cn/raw/76cb663cbf07797cd0e0daa2e568dc16.png) 
5. （可选）设置高级参数。
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">说明</th>
</tr>
</thead>
<tbody><tr>
<td align="left">复制存量数据</td>
<td align="left">开启后将复制源 PostgreSQL 数据库中的存量数据，开关一经打开，无论后续是否关闭，都无法新增需要监听的库。</td>
</tr>
<tr>
<td align="left">是否包含 Schema</td>
<td align="left">消息输出时，key 和 value 内容是否包含 schema。</td>
</tr>
<tr>
<td align="left">pluginName</td>
<td align="left">选择自建的 PostgreSQL 连接时，需要使用 pgoutput。</td>
</tr>
<tr>
<td align="left">分区策略</td>
<td align="left">订阅数据写入，默认情况下根据主键 hash 到不同的分区。可以手动指定表的 hash 字段。</td>
</tr>
</tbody></table>
<img src="https://qcloudimg.tencent-cloud.cn/raw/0265e7a8c635d4098888a6dcb2d2b7dc.png" alt=""> 
6. 选择数据目标 Topic，支持选择 **DIP Topic** 或者 **CKafka Topic**。
   分发到多个 Topic：支持将不同数据库表中的数据分发到不同的 Topic 中去。
   - 开启后：支持自动创建 Topic 或者选择已有 Topic。
     - 自动创建 Topic：只能自动创建 CKafka Topic，自动创建的 topic 名是由 database.schema.table 形式构建。
     - 选择已有 Topic：只能选择同一个 CKafka 实例下的 Topic。
   - 未开启：支持自动创建 Topic 或者选择已有 Topic。
     - 自动创建 Topic：可以选择 CKafka Topic 或者 DIP Topic，若选择CKafka Topic，则需要指定目标 CKafka 实例。支持批量连续命名或指定模式串命名，[参考文档](https://cloud.tencent.com/document/product/597/59246)。
     - 选择已有 Topic：支持选择 **DIP Topic** 或者 **CKafka Topic**。选择 CKafka Topic 时，若实例设置了 ACL 策略，请确保选中的 Topic 有读写权限。
       ![](https://qcloudimg.tencent-cloud.cn/raw/1b9a55964e8486c6d773077d4a506805.png)
7. 选择是否开启数据压缩，数据压缩可以减少网络 IO 传输量，减少磁盘存储空间，[数据压缩说明](https://cloud.tencent.com/document/product/597/40402)。
8. 单击**提交**，可以在任务列表看到刚刚创建的任务，在状态栏可以看到创建进度。

   
