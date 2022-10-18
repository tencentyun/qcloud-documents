## 操作场景

数据接入平台 DIP 支持接入各种数据源产生的不同类型的数据，统一管理，再分发给下游的离线/在线处理平台，构建清晰的数据通道。

DIP 支持订阅 MySQL 变更数据，免去对基于 CDC 的订阅组件如（Canal、Debezium 等）的运维成本。本文介绍在 DIP 控制台创建 MySQL 数据接入任务的操作方法。

## 前提条件

- 已创建好数据目标 Topic。
- 已创建好数据源 MySQL 连接。

## 操作步骤

1. 登录 [DIP 控制台](https://console.cloud.tencent.com/ckafka/datahub-overview)。
2. 在左侧导航栏单击**任务管理** > **任务列表**，选择好地域后，单击**新建任务**。
3. 填写任务名称，任务类型选择**数据接入**，数据目标类型选择 **MySQL 数据订阅**，单击**下一步**。
4. 填写数据源配置信息。
<table>
<thead>
<tr>
<th>参数</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>数据源</td>
<td>选择提前创建好的 MySQL 源数据连接</td>
</tr>
<tr>
<td>选择数据库表</td>
<td>支持三种选择方式：<ul><li>全部库表：订阅该连接关联的所有数据库表。</li><li>批量选择：支持手动勾选要订阅的数据库和表，支持订阅多个数据库、多个表。</li><li>正则匹配：支持使用正则匹配筛选订阅符合条件的表。</li></ul></td>
</tr>
</tbody></table>
<img src="https://qcloudimg.tencent-cloud.cn/raw/4df62ff73d92de9ca2e1439773beeaf7.png" alt=""> 
5. （可选）设置高级参数。
<table>
<thead>
<tr>
<th>参数</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>复制存量数据</td>
<td>开启后将复制源 MySQL 数据库中的存量数据，开关一经打开，无论后续是否关闭，都无法新增需要监听的库。</td>
</tr>
<tr>
<td>订阅结构更新</td>
<td>订阅结构更新将订阅整个数据库实例所有对象的结构创建，删除以及修改。若数据目标配置选择分发到多个Topic 则不支持订阅结构更新。</td>
</tr>
<tr>
<td>包含原始 SQL 查询</td>
<td>是否包含生成变更事件的原始 SQL 查询。需要 MySQL 的配置项"binlog_rows_query_log_events"的值为"ON"。</td>
</tr>
<tr>
<td>分区策略</td>
<td>订阅数据写入，默认情况下根据主键 hash 到不同的分区。可以手动指定表的 hash 字段。</td>
</tr>
<tr>
<td>数据格式</td>
<td>默认采用 Debezium 格式，同时提供了兼容其他消息格式的能力。<ul><li>Canal 格式：详情介绍请参见 <a href="https://cloud.tencent.com/document/product/1591/79158">MySQL 订阅消息 Canal 格式说明</a>。</li><li>官方格式一：详情介绍请参见 <a href="https://cloud.tencent.com/document/product/1591/79157">MySQL 订阅消息官方格式说明</a>。</li></ul></td>
</tr>
</tbody></table>
<img src="https://qcloudimg.tencent-cloud.cn/raw/5e9583ffe15566fcbd5ca352125e11fd.png" alt=""> 
6. 单击**下一步**，配置数据目标信息。
   分发到多个 Topic：支持将不同数据库表中的数据分发到不同的 Topic 中去。
   - 开启后：只能选择同一个 CKafka 实例下的 Topic。
   - 未开启：支持选择 **DIP Topic** 或者 **CKafka Topic**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/0daa51f156dc33a3602f90b23208dec3.png)
7. 单击**提交**，可以在任务列表看到刚刚创建的任务，在状态栏可以看到创建进度。

   
