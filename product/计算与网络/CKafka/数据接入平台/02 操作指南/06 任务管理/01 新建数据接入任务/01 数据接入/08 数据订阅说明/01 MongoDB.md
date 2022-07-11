
## 简介

MongoDB Kafka Connector 允许监控一个 Mongo 实例内的所有数据库（database）或单个数据库，也允许监控某个数据库内的所有集合（collection）或单个集合。将 Mongo 的修改信息生成修改事件消息，以消息流的方式提交给 kafka 的 topic。客户端应用可以通过消费对应 topic 中的消息来对数据库修改事件进行处理，从而达到监控特定数据库的目的。

本文档是对 Mongo 官方文档的归纳和整理，详情参见 [MongoDB Change Events](https://www.mongodb.com/docs/manual/reference/change-events/)。

## 事件格式

以下 JSON 框架展示了所有修改事件消息中可能出现的字段：
<dx-codeblock>
:::  json
{
   _id : { <BSON Object> },
   "operationType" : "<operation>",
   "fullDocument" : { <document> },
   "ns" : {
      "db" : "<database>",
      "coll" : "<collection>"
   },
   "to" : {
      "db" : "<database>",
      "coll" : "<collection>"
   },
   "documentKey" : { "_id" : <value> },
   "updateDescription" : {
      "updatedFields" : { <document> },
      "removedFields" : [ "<field>", ... ],
      "truncatedArrays" : [
         { "field" : <field>, "newSize" : <integer> },
         ...
      ]
   },
   "clusterTime" : <Timestamp>,
   "txnNumber" : <NumberLong>,
   "lsid" : {
      "id" : <UUID>,
      "uid" : <BinData>
   }
}
:::
</dx-codeblock>
其中部分字段可能只在特定的事件类型中才会出现，下表对相应字段及其含义进行了描述。
<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody><tr>
<td align="left"><code>_id</code></td>
<td align="left">document</td>
<td align="left">一个用来唯一标识事件的<a href="https://www.mongodb.com/docs/manual/reference/glossary/#std-term-BSON">BSON</a> 对象。   <code>_id</code> 对象的格式如下：<code>{   "_data" : &lt;BinData|hex string&gt;}</code> 。<code>_data</code> 的类型取决于 MongoDB 的版本 ，可通过 <a href="https://www.mongodb.com/docs/manual/changeStreams/#std-label-change-stream-resume-token">Resume Tokens</a> 查看完整的<code>_data</code>类型介绍。</td>
</tr>
<tr>
<td align="left"><code>operationType</code></td>
<td align="left">string</td>
<td align="left">触发修改事件的操作类型，具体包括以下 8 种：<br><code>insert</code><br><code>delete</code><br><code>replace</code><br><code>update</code><br><code>drop</code><br><code>rename</code><br><code>dropDatabase</code><br><code>invalidate</code></td>
</tr>
<tr>
<td align="left"><code>fullDocument</code></td>
<td align="left">document</td>
<td align="left">表示被新增（ <code>insert</code>）, 替换（<code>replace</code>）, 删除（<code>delete</code>）, 更新（<code>update</code> ）操作所影响的文档。对于 <code>insert</code> 和 <code>replace</code> 操作，该字段表示新增的文档。对于 <code>delete</code> 操作,，该字段缺省表示文档已经不存在。对于 <code>update</code> 操作，只有配置了 <code>fullDocument</code> 为 <code>updateLookup</code> 时才会显示。</td>
</tr>
<tr>
<td align="left"><code>ns</code></td>
<td align="left">document</td>
<td align="left">命名空间（namespace），由 database 和 collection 构成。</td>
</tr>
<tr>
<td align="left"><code>ns.db</code></td>
<td align="left">string</td>
<td align="left">数据库名称。</td>
</tr>
<tr>
<td align="left"><code>ns.coll</code></td>
<td align="left">string</td>
<td align="left">集合名称。对于 <code>dropDatabase</code> 操作，该字段缺省。</td>
</tr>
<tr>
<td align="left"><code>to</code></td>
<td align="left">document</td>
<td align="left">当操作类型为 <code>rename</code> 时，表示新的集合名称。该字段对其他操作是缺省的。</td>
</tr>
<tr>
<td align="left"><code>to.db</code></td>
<td align="left">string</td>
<td align="left">新的数据库的名称。</td>
</tr>
<tr>
<td align="left"><code>to.coll</code></td>
<td align="left">string</td>
<td align="left">新的集合名称。</td>
</tr>
<tr>
<td align="left"><code>documentKey</code></td>
<td align="left">document</td>
<td align="left">操作修改的文档的 ID。</td>
</tr>
<tr>
<td align="left"><code>updateDescription</code></td>
<td align="left">document</td>
<td align="left">一个用来描述被更新操作（update operation）修改的字段的文档。该字段仅当事件对应的操作为 <code>update</code> 时才有。</td>
</tr>
<tr>
<td align="left"><code>updateDescription.updatedFields</code></td>
<td align="left">document</td>
<td align="left">包含被更新操作修改的字段，字段的 value 值为更新后的值。</td>
</tr>
<tr>
<td align="left"><code>updateDescription.removedFields</code></td>
<td align="left">array</td>
<td align="left">包含被更新操作删除的字段。</td>
</tr>
<tr>
<td align="left"><code>updateDescription.truncatedArrays</code></td>
<td align="left">array</td>
<td align="left">其中记录了使用以下一个或多个基于 pipeline 的更新执行的数组截断：<br><a href="https://www.mongodb.com/docs/manual/reference/operator/aggregation/addFields/#mongodb-pipeline-pipe.-addFields"><code>$addFields</code></a><br><a href="https://www.mongodb.com/docs/manual/reference/operator/aggregation/set/#mongodb-pipeline-pipe.-set"><code>$set</code></a><br><a href="https://www.mongodb.com/docs/manual/reference/operator/aggregation/replaceRoot/#mongodb-pipeline-pipe.-replaceRoot"><code>$replaceRoot</code></a><br><a href="https://www.mongodb.com/docs/manual/reference/operator/aggregation/replaceWith/#mongodb-pipeline-pipe.-replaceWith"><code>$replaceWith</code></a></td>
</tr>
<tr>
<td align="left"><code>updateDescription.truncatedArrays.field</code></td>
<td align="left">string</td>
<td align="left">被删除的字段。</td>
</tr>
<tr>
<td align="left"><code>updateDescription.truncatedArrays.newSize</code></td>
<td align="left">integer</td>
<td align="left">truncated array 中的元素个数。</td>
</tr>
<tr>
<td align="left"><code>clusterTime</code></td>
<td align="left">Timestamp</td>
<td align="left">oplog 与事件关联的时间戳。对于涉及 <a href="https://www.mongodb.com/docs/manual/core/transactions/">多文档事务</a>, 关联的事件的<code>clusterTime</code> 值时相同的。</td>
</tr>
<tr>
<td align="left"><code>txnNumber</code></td>
<td align="left">NumberLong</td>
<td align="left">事务 ID。仅当操作是 <a href="https://www.mongodb.com/docs/manual/core/transactions/">多文档事务</a> 时出现。</td>
</tr>
<tr>
<td align="left"><code>lsid</code></td>
<td align="left">Document</td>
<td align="left">与事务关联的 session 的 ID，仅当操作是 <a href="https://www.mongodb.com/docs/manual/core/transactions/">多文档事务</a> 时出现。</td>
</tr>
</tbody></table>

## 事件列表

### 新增事件（insert event）
<dx-codeblock>
:::  json
{
   _id: { < Resume Token > },
   operationType: 'insert',
   clusterTime: <Timestamp>,
   ns: {
      db: 'engineering',
      coll: 'users'
   },
   documentKey: {
      userName: 'alice123',
      _id: ObjectId("599af247bb69cd8996xxxxxx")
   },
   fullDocument: {
      _id: ObjectId("599af247bb69cd8996xxxxxx"),
      userName: 'alice123',
      name: 'Alice'
   }
}
:::
</dx-codeblock>
其中 documentKey 字段同时包含了 _id 和 username 字段。表示 engineering.users 集合是分片的，shard key 为 username 和 _id。

### 更新事件（update event）
<dx-codeblock>
:::  json
{
   _id: { < Resume Token > },
   operationType: 'update',
   clusterTime: <Timestamp>,
   ns: {
      db: 'engineering',
      coll: 'users'
   },
   documentKey: {
      _id: ObjectId("58a4eb4a30c75625e0xxxxxx")
   },
   updateDescription: {
      updatedFields: {
         email: 'alice@10gen.com'
      },
      removedFields: ['phoneNumber'],
      truncatedArrays: [ {
         "field" : "vacation_time",
         "newSize" : 36
      } ]
   }
}
:::
</dx-codeblock>
以下例子展示了 `update` event 配置了 `fullDocument : updateLookup` 选项的消息内容：
<dx-codeblock>
:::  json
{
   _id: { < Resume Token > },
   operationType: 'update',
   clusterTime: <Timestamp>,
   ns: {
      db: 'engineering',
      coll: 'users'
   },
   documentKey: {
      _id: ObjectId("58a4eb4a30c75625e0xxxxxx")
   },
   updateDescription: {
      updatedFields: {
         email: 'alice@10gen.com'
      },
      removedFields: ['phoneNumber'],
      truncatedArrays: [ {
         "field" : "vacation_time",
         "newSize" : 36
      } ]
   },
   fullDocument: {
      _id: ObjectId("58a4eb4a30c75625e0xxxxxx"),
      name: 'Alice',
      userName: 'alice123',
      email: 'alice@10gen.com',
      team: 'replication'
   }
}
:::
</dx-codeblock>


### 替换事件（replace event）
<dx-codeblock>
:::  json
{
   _id: { < Resume Token > },
   operationType: 'replace',
   clusterTime: <Timestamp>,
   ns: {
      db: 'engineering',
      coll: 'users'
   },
   documentKey: {
      _id: ObjectId("599af247bb69cd8996xxxxxx")
   },
   fullDocument: {
      _id: ObjectId("599af247bb69cd8996xxxxxx"),
      userName: 'alice123',
      name: 'Alice'
   }
}
:::
</dx-codeblock>

 `replace` 操作是通过两步操作实现的：

- 删除原 `documentKey` 对应的文档
- 根据一样的 `documentkey`插入新的文档


  基于 `replace` 事件的 `fullDocument` 字段表示的是插入后的新文档。

### 删文档事件（delete event）
<dx-codeblock>
:::  json
{
   _id: { < Resume Token > },
   operationType: 'delete',
   clusterTime: <Timestamp>,
   ns: {
      db: 'engineering',
      coll: 'users'
   },
   documentKey: {
      _id: ObjectId("599af247bb69cd8996xxxxxx")
   }
}
:::
</dx-codeblock>
对于删除文档事件的消息，`fullDocument` 字段缺省。

### 删集合事件（drop event）
<dx-codeblock>
:::  json
{
   _id: { < Resume Token > },
   operationType: 'drop',
   clusterTime: <Timestamp>,
   ns: {
      db: 'engineering',
      coll: 'users'
   }
}
:::
</dx-codeblock>

当一个集合被删除时会触发该事件，同时会导致订阅了该集合的 connector 产生一个无效事件（invalidate event）。

### 改名事件（rename event）
<dx-codeblock>
:::  json
{
   _id: { < Resume Token > },
   operationType: 'rename',
   clusterTime: <Timestamp>,
   ns: {
      db: 'engineering',
      coll: 'users'
   },
   to: {
      db: 'engineering',
      coll: 'people'
   }
}
:::
</dx-codeblock>
当一个集合名称被更改时会触发该事件，同时会导致订阅了该集合的 connector 产生一个无效事件（invalidate event）。

### 删库事件（drop database event）
<dx-codeblock>
:::  json
{
   _id: { < Resume Token > },
   operationType: 'dropDatabase',
   clusterTime: <Timestamp>,
   ns: {
      db: 'engineering'
   }
}
:::
</dx-codeblock>

当一个数据库被删除时会触发该事件，同时会导致订阅了该集合的 connector 产生一个无效事件（invalidate event）。

在生成数据库删除事件（dropDatabase）之前，会为数据库中的每一个集合生成一个集合删除事件（drop event）。

### 无效事件（invalidate event）
<dx-codeblock>
:::  json
{
   _id: { < Resume Token > },
   operationType: 'invalidate',
   clusterTime: <Timestamp>
}
:::
</dx-codeblock>

- 对于订阅了一个集合（collection）的 connector，drop event，rename event 或 dropDatabase event 这类会对该集合产生影响的事件都会产生一个无效事件。
- 对于订阅了一个数据库（database）的 connector，dropDatabase event 会产生一个无效事件。



