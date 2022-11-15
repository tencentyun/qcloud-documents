## 简介

MySQL 通过一种二进制日志（binlog）来按序记录所有提交给数据库的操作，包括对表结构的修改以及对表中数据的修改。MySQL 通过 binlog 来进行备份或恢复数据。

Debezium MySQL connector 通过读取 binlog 来生成行级（row-level）的数据库修改事件（event），包括 INSERT、UPDATE 和 DELETE，并将事件发送给 kafka 中相应的 topic 。客户端应用可以通过消费对应 topic中的消息来对数据库修改事件进行处理，从而达到监控特定数据库的目的。

支持订阅的 SQL 操作：
<table>
<thead>
<tr>
<th>操作类型</th>
<th>支持的SQL操作</th>
</tr>
</thead>
<tbody><tr>
<td>DML</td>
<td>INSERT、UPDATE、DELETE</td>
</tr>
<tr>
<td>DDL</td>
<td>CREATE DATABASE、DROP DATABASE、CREATE TABLE、ALTER TABLE、DROP TABLE、RENAME TABLE</td>
</tr>
</tbody></table>

本文档是根据 Debezium 官方文档进行整理和归纳而来。详情参见 [Debezium connector for MySQL](https://debezium.io/documentation/reference/stable/connectors/mysql.html#mysql-events)。

## 事件格式
Debezium MySQL connector 针对每一次插入、更新、删除操作生成数据变更事件。每一个事件（event）在作为消息提交给 kafka 的主题(Topic)，Topic里每条消息包含 key 和 value 两部分，示例如下：

![](https://qcloudimg.tencent-cloud.cn/raw/bf24fde5b04606e80581600f4ac96554.png)

Kafka 每条消息的key 和 value 都包含 schema 和 payload 两个字段。格式如下：
<dx-codeblock>
:::  json
{
 "schema": { 
   ...
  },
 "payload": { 
   ...
 }
}
:::
</dx-codeblock>

key 字段说明：

<table>
<thead>
<tr>
<th align="center">Item</th>
<th align="center">Field name</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody><tr>
<td align="center">1</td>
<td align="center"><code>schema</code></td>
<td align="left">schema 字段描述了 key 的 payload 字段的结构，即它描述了被修改的表的主键（primary key）结构，如果表没有主键，则描述其唯一约束（unique key）的结构。</td>
</tr>
<tr>
<td align="center">2</td>
<td align="center"><code>payload</code></td>
<td align="left"><code>payload</code> 字段的结构和第一个 <code>schema</code> 中描述的相同，包含了被修改的行的键值。</td>
</tr>
</tbody></table>

value 字段说明：

<table>
<thead>
<tr>
<th align="center">Item</th>
<th align="center">Field name</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody><tr>
<td align="center">1</td>
<td align="center"><code>schema</code></td>
<td align="left"><code>schema</code> 字段描述了 value 的payload 字段的结构，即描述了被修改行的字段结构。这个字段通常是一个嵌套结构的字段。</td>
</tr>
<tr>
<td align="center">2</td>
<td align="center"><code>payload</code></td>
<td align="left"><code>payload</code> 字段的结构和第二个 <code>schema</code> 中定义的相同，它包含被修改行的真实数据。</td>
</tr>
</tbody></table>

## 事件消息 key

不同类型事件的消息都有一样的 key 结构，下面给出一个示例，一个修改事件的 key 包含被修改的表的主键结构以及对应行的实际主键值。
<dx-codeblock>
:::  sql
CREATE TABLE customers (
  id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE KEY
) AUTO_INCREMENT=1001;
:::
</dx-codeblock>

每一个捕获 customers 表修改操作的事件 key 中的 schema 都相同。该操作对应的事件消息的 key 如下所示（JSON表示）：
<dx-codeblock>
:::  json
{
 "schema": { 
    "type": "struct",
    "name": "mysql-server-1.inventory.customers.Key", 
    "optional": false, 
    "fields": [ 
      {
        "field": "id",
        "type": "int32",
        "optional": false
      }
    ]
  },
 "payload": { 
    "id": 1001
  }
}
:::
</dx-codeblock>
<table>
<thead>
<tr>
<th align="left">Item</th>
<th align="left">Field name</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody><tr>
<td align="left">1</td>
<td align="left"><code>schema</code></td>
<td align="left">Schema 描述了 payload 中的结构。</td>
</tr>
<tr>
<td align="left">2</td>
<td align="left"><code>mysql-server-1.inventory.customers.Key</code></td>
<td align="left">schema 的名称格式为 *connector-name*.*database-name*.*table-name*.<code>Key</code>。在这个例子中: <code>mysql-server-1</code> 是生成事件的connector的名字。<code>inventory</code> 是对应数据库的名字。 <code>customers</code> 是表的名字。</td>
</tr>
<tr>
<td align="left">3</td>
<td align="left"><code>optional</code></td>
<td align="left">表示字段是否是可选项。</td>
</tr>
<tr>
<td align="left">4</td>
<td align="left"><code>fields</code></td>
<td align="left">列出了所有 <code>payload</code> 中包含的字段及其结构, 包括字段名、字段类型、以及是否可选。</td>
</tr>
<tr>
<td align="left">5</td>
<td align="left"><code>payload</code></td>
<td align="left">包含被修改行的主键。在例子中仅包含一个字段名为 <code>id</code> 的主键值： <code>1001</code>。</td>
</tr>
</tbody></table>



## DML 事件

前面介绍了一个事件消息的 key 的结构，不同类型事件的 key 结构是相同的。本节列举了不同的事件类型，介绍了这些事件类型各自的 value 结构。

### 新增事件（create events）

下面这个例子展示了在表中新增数据的时候 connector 生成的事件消息的 value 部分：
<dx-codeblock>
:::  json
{
  "schema": { 
    "type": "struct",
    "fields": [
      {
        "type": "struct",
        "fields": [
          {
            "type": "int32",
            "optional": false,
            "field": "id"
          },
          {
            "type": "string",
            "optional": false,
            "field": "first_name"
          },
          {
            "type": "string",
            "optional": false,
            "field": "last_name"
          },
          {
            "type": "string",
            "optional": false,
            "field": "email"
          }
        ],
        "optional": true,
        "name": "mysql-server-1.inventory.customers.Value", 
        "field": "before"
      },
      {
        "type": "struct",
        "fields": [
          {
            "type": "int32",
            "optional": false,
            "field": "id"
          },
          {
            "type": "string",
            "optional": false,
            "field": "first_name"
          },
          {
            "type": "string",
            "optional": false,
            "field": "last_name"
          },
          {
            "type": "string",
            "optional": false,
            "field": "email"
          }
        ],
        "optional": true,
        "name": "mysql-server-1.inventory.customers.Value",
        "field": "after"
      },
      {
        "type": "struct",
        "fields": [
          {
            "type": "string",
            "optional": false,
            "field": "version"
          },
          {
            "type": "string",
            "optional": false,
            "field": "connector"
          },
          {
            "type": "string",
            "optional": false,
            "field": "name"
          },
          {
            "type": "int64",
            "optional": false,
            "field": "ts_ms"
          },
          {
            "type": "boolean",
            "optional": true,
            "default": false,
            "field": "snapshot"
          },
          {
            "type": "string",
            "optional": false,
            "field": "db"
          },
          {
            "type": "string",
            "optional": true,
            "field": "table"
          },
          {
            "type": "int64",
            "optional": false,
            "field": "server_id"
          },
          {
            "type": "string",
            "optional": true,
            "field": "gtid"
          },
          {
            "type": "string",
            "optional": false,
            "field": "file"
          },
          {
            "type": "int64",
            "optional": false,
            "field": "pos"
          },
          {
            "type": "int32",
            "optional": false,
            "field": "row"
          },
          {
            "type": "int64",
            "optional": true,
            "field": "thread"
          },
          {
            "type": "string",
            "optional": true,
            "field": "query"
          }
        ],
        "optional": false,
        "name": "io.debezium.connector.mysql.Source", 
        "field": "source"
      },
      {
        "type": "string",
        "optional": false,
        "field": "op"
      },
      {
        "type": "int64",
        "optional": true,
        "field": "ts_ms"
      }
    ],
    "optional": false,
    "name": "mysql-server-1.inventory.customers.Envelope" 
  },
  "payload": { 
    "op": "c", 
    "ts_ms": 1465491411815, 
    "before": null, 
    "after": { 
      "id": 1004,
      "first_name": "Anne",
      "last_name": "Kretchmar",
      "email": "annek@noanswer.org"
    },
    "source": { 
      "version": "1.9.3.Final",
      "connector": "mysql",
      "name": "mysql-server-1",
      "ts_ms": 0,
      "snapshot": false,
      "db": "inventory",
      "table": "customers",
      "server_id": 0,
      "gtid": null,
      "file": "mysql-bin.000003",
      "pos": 154,
      "row": 0,
      "thread": 7,
      "query": "INSERT INTO customers (first_name, last_name, email) VALUES ('Anne', 'Kretchmar', 'annek@noanswer.org')"
    }
  }
}
:::
</dx-codeblock>
<table>
<thead>
<tr>
<th align="left">Item</th>
<th align="left">Field name</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody><tr>
<td align="left">1</td>
<td align="left"><code>schema</code></td>
<td align="left">Schema 描述了 payload 中的结构, 其中 schema 中的 fields 字段为一个数组，表示 payload 字段包含了多个字段，数组的每个元素是对 payload 中相应字段结构的描述信息。</td>
</tr>
<tr>
<td align="left">2</td>
<td align="left">field</td>
<td align="left">每一个 fields 中的元素都包含一个 field 字段，该字段表示 payload 中对应字段的名称。在示例中包括 <code>before</code>、<code>after</code>、<code>source</code>等。</td>
</tr>
<tr>
<td align="left">3</td>
<td align="left"><code>type</code></td>
<td align="left">表示字段的类型，如整型（int）、字符串（string）等.</td>
</tr>
<tr>
<td align="left">4</td>
<td align="left"><code>mysql-server-1.inventory.customers.Value</code></td>
<td align="left">表示该字段是 mysql-server-1 连接器生成的针对 inventory 数据库的 customers 表的 value 部分信息。</td>
</tr>
<tr>
<td align="left"></td>
<td align="left"><code>io.debezium.connector.mysql.Source</code></td>
<td align="left">该名称和特定的 connector 绑定，由该 connector 生成的事件该名称都相同。</td>
</tr>
<tr>
<td align="left">6</td>
<td align="left"><code>payload</code></td>
<td align="left">包含修改事件中具体被修改的数据，包括修改前（before 字段）和修改后（after 字段）的数据，以及一些 connector 的元数据信息（source 字段）。</td>
</tr>
<tr>
<td align="left">7</td>
<td align="left"><code>op</code></td>
<td align="left">表示导致事件生成的修改操作的类型，例子中的 c 表示 修改操作创建了一个新的行。<br>c = create<br>u = update<br>d = delete<br>r = read (仅 snapshots)</td>
</tr>
<tr>
<td align="left">8</td>
<td align="left"><code>source</code></td>
<td align="left">source 字段是一个描述事件元数据的字段。它包含的一些字段可以用来与其他事件做比较，如比较事件生成的顺序、事件是否属于同一个事务等。该字段包含以下元数据信息：<br> Debezium version<br>Connector name<br>binlog name where the event was recorded<br>binlog position<br>Row within the event<br>If the event was part of a snapshot<br>Name of the database and table that contain the new row<br>ID of the MySQL thread that created the event (non-snapshot only)<br>MySQL server ID (if available)<br>Timestamp for when the change was made in the database</td>
</tr>
<tr>
<td align="left">9</td>
<td align="left"><code>query</code></td>
<td align="left">修改操作的原始 SQL 语句。</td>
</tr>
</tbody></table>


### 更新事件（update events）

下面这个例子展示了更新操作生成的事件的 value 部分：
<dx-codeblock>
:::  json
{
  "schema": { ... },
  "payload": {
    "before": { 
      "id": 1004,
      "first_name": "Anne",
      "last_name": "Kretchmar",
      "email": "annek@noanswer.org"
    },
    "after": { 
      "id": 1004,
      "first_name": "Anne Marie",
      "last_name": "Kretchmar",
      "email": "annek@noanswer.org"
    },
    "source": { 
      "version": "1.9.3.Final",
      "name": "mysql-server-1",
      "connector": "mysql",
      "name": "mysql-server-1",
      "ts_ms": 1465581029100,
      "snapshot": false,
      "db": "inventory",
      "table": "customers",
      "server_id": 223344,
      "gtid": null,
      "file": "mysql-bin.000003",
      "pos": 484,
      "row": 0,
      "thread": 7,
      "query": "UPDATE customers SET first_name='Anne Marie' WHERE id=1004"
    },
    "op": "u", 
    "ts_ms": 1465581029523 
  }
}
:::
</dx-codeblock>

其中 schema 字段和新增操作的事件相同，而 payload 部分有所不同，在新增事件中，before 字段为 null，表示没有原始数据，而更新事件中包含了更新前（before）和更新后（after）的数据。

### 删除事件（delete events）

下面这个例子展示了删除操作生成的事件的 value 部分：
<dx-codeblock>
:::  json
{
  "schema": { ... },
  "payload": {
    "before": { 
      "id": 1004,
      "first_name": "Anne Marie",
      "last_name": "Kretchmar",
      "email": "annek@noanswer.org"
    },
    "after": null, 
    "source": { 
      "version": "1.9.3.Final",
      "connector": "mysql",
      "name": "mysql-server-1",
      "ts_ms": 1465581902300,
      "snapshot": false,
      "db": "inventory",
      "table": "customers",
      "server_id": 223344,
      "gtid": null,
      "file": "mysql-bin.000003",
      "pos": 805,
      "row": 0,
      "thread": 7,
      "query": "DELETE FROM customers WHERE id=1004"
    },
    "op": "d", 
    "ts_ms": 1465581902461 
  }
}
:::
</dx-codeblock>

其中 schema 字段和新增操作的事件相同，而 payload 部分有所不同，删除事件中包含了修改前（before）的数据，但更新后（after）的数据为 null，表示数据已删除。

### 更新主键（primary key updates）

如果一个操作修改了数据表中某行的主键，那么 connector 会生成一条**删除事件**来表示原主键对应的数据行删除，同时生成一条**新增事件**来表示插入的新主键对应的行。每一条消息的 header 都会和相应的 key 关联。官方描述如下：

- The `DELETE` event record has `__debezium.newkey` as a message header. The value of this header is the new primary key for the updated row.
- The `CREATE` event record has `__debezium.oldkey` as a message header. The value of this header is the previous (old) primary key that the updated row had.

## DDL 事件

### 创建数据库（create database）

下面这个例子展示了**创建数据库**操作生成的事件的 value 部分：
<dx-codeblock>
:::  sql
{
  "source" : {
    "server" : "dip_source"
  },
  "position" : {
    "ts_sec" : 1655812326,
    "file" : "mysql-bin.000006",
    "pos" : 26063,
    "gtids" : "b24176f2-5409-11ec-80d4-b8599fe5c6ea:1-78",
    "snapshot" : true
  },
  "databaseName" : "dip_test",
  "ddl" : "CREATE DATABASE `dip_test` CHARSET utf8mb4 COLLATE utf8mb4_0900_ai_ci",
  "tableChanges" : [ ]
}
:::
</dx-codeblock>

其中 position 的内容为记录 binlog 文件，消费偏移量等信息。ddl 字段为触发事件的 sql 语句。

### 删除数据库（drop database）

下面这个例子展示了**删除数据库**操作生成的事件的 value 部分：
<dx-codeblock>
:::  sql
{
  "source" : {
    "server" : "dip_source"
  },
  "position" : {
    "ts_sec" : 1655812326,
    "file" : "mysql-bin.000006",
    "pos" : 26063,
    "gtids" : "b24176f2-5409-11ec-80d4-b8599fe5c6ea:1-78",
    "snapshot" : true
  },
  "databaseName" : "dip_test",
  "ddl" : "DROP DATABASE IF EXISTS `dip_test`",
  "tableChanges" : [ ]
}
:::
</dx-codeblock>

其中 position 的内容为记录 binlog 文件，消费偏移量等信息。ddl 字段为触发事件的 sql 语句。

### 创建表（create table）

下面这个例子展示了**创建表**操作生成的事件的 value 部分：
<dx-codeblock>
:::  sql
{
  "source" : {
    "server" : "dip_source"
  },
  "position" : {
    "ts_sec" : 1655812326,
    "file" : "mysql-bin.000006",
    "pos" : 26063,
    "gtids" : "b24176f2-5409-11ec-80d4-b8599fe5c6ea:1-78",
    "snapshot" : true
  },
  "databaseName" : "dip_test",
  "ddl" : "CREATE TABLE `customers` (\n  `id` int NOT NULL AUTO_INCREMENT,\n  `first_name` varchar(255) NOT NULL,\n  `last_name` varchar(255) NOT NULL,\n  `email` varchar(255) NOT NULL,\n  PRIMARY KEY (`id`),\n  UNIQUE KEY `email` (`email`),\n  KEY `ix_id` (`id`)\n) ENGINE=InnoDB AUTO_INCREMENT=1041 DEFAULT CHARSET=utf8",
  "tableChanges" : [ {
    "type" : "CREATE",
    "id" : "\"dip_test\".\"customers\"",
    "table" : {
      "defaultCharsetName" : "utf8",
      "primaryKeyColumnNames" : [ "id" ],
      "columns" : [ {
        "name" : "id",
        "jdbcType" : 4,
        "typeName" : "INT",
        "typeExpression" : "INT",
        "charsetName" : null,
        "position" : 1,
        "optional" : false,
        "autoIncremented" : true,
        "generated" : true,
        "comment" : null,
        "hasDefaultValue" : false,
        "enumValues" : [ ]
      }, {
        "name" : "first_name",
        "jdbcType" : 12,
        "typeName" : "VARCHAR",
        "typeExpression" : "VARCHAR",
        "charsetName" : "utf8",
        "length" : 255,
        "position" : 2,
        "optional" : false,
        "autoIncremented" : false,
        "generated" : false,
        "comment" : null,
        "hasDefaultValue" : false,
        "enumValues" : [ ]
      }, {
        "name" : "last_name",
        "jdbcType" : 12,
        "typeName" : "VARCHAR",
        "typeExpression" : "VARCHAR",
        "charsetName" : "utf8",
        "length" : 255,
        "position" : 3,
        "optional" : false,
        "autoIncremented" : false,
        "generated" : false,
        "comment" : null,
        "hasDefaultValue" : false,
        "enumValues" : [ ]
      }, {
        "name" : "email",
        "jdbcType" : 12,
        "typeName" : "VARCHAR",
        "typeExpression" : "VARCHAR",
        "charsetName" : "utf8",
        "length" : 255,
        "position" : 4,
        "optional" : false,
        "autoIncremented" : false,
        "generated" : false,
        "comment" : null,
        "hasDefaultValue" : false,
        "enumValues" : [ ]
      } ]
    },
    "comment" : null
  } ]
}
:::
</dx-codeblock>

其中 position 的内容为记录 binlog 文件，消费偏移量等信息。ddl 字段为触发事件的 sql 语句。columns 字段记录了新增表的不同字段的定义信息。

### 修改表（alter table)

下面这个例子展示了**修改表**操作生成的事件的 value 部分：
<dx-codeblock>
:::  sql
{
  "source" : {
    "server" : "1307446078-a123"
  },
  "position" : {
    "transaction_id" : null,
    "ts_sec" : 1655782153,
    "file" : "mysql-bin.000005",
    "pos" : 1218,
    "gtids" : "ddf040ad-7509-11ec-968b-0c42a1eda2e9:1-8",
    "server_id" : 183277
  },
  "databaseName" : "test",
  "ddl" : "ALTER TABLE `user` ADD COLUMN `createtime` datetime NULL DEFAULT CURRENT_TIMESTAMP",
  "tableChanges" : [ {
    "type" : "ALTER",
    "id" : "\"test\".\"user\"",
    "table" : {
      "defaultCharsetName" : "utf8",
      "primaryKeyColumnNames" : [ ],
      "columns" : [ {
        "name" : "name",
        "jdbcType" : 1,
        "typeName" : "CHAR",
        "typeExpression" : "CHAR",
        "charsetName" : "utf8",
        "length" : 20,
        "position" : 1,
        "optional" : true,
        "autoIncremented" : false,
        "generated" : false,
        "comment" : null,
        "hasDefaultValue" : true,
        "defaultValueExpression" : "",
        "enumValues" : [ ]
      }, {
        "name" : "age",
        "jdbcType" : 4,
        "typeName" : "INT",
        "typeExpression" : "INT",
        "charsetName" : null,
        "position" : 2,
        "optional" : true,
        "autoIncremented" : false,
        "generated" : false,
        "comment" : null,
        "hasDefaultValue" : true,
        "enumValues" : [ ]
      }, {
        "name" : "createtime",
        "jdbcType" : 93,
        "typeName" : "DATETIME",
        "typeExpression" : "DATETIME",
        "charsetName" : null,
        "position" : 3,
        "optional" : true,
        "autoIncremented" : false,
        "generated" : false,
        "comment" : null,
        "hasDefaultValue" : true,
        "defaultValueExpression" : "1970-01-01 00:00:00",
        "enumValues" : [ ]
      } ]
    },
    "comment" : null
  } ]
}
:::
</dx-codeblock>

其中 position 的内容为记录 binlog 文件，消费偏移量等信息。ddl 字段为触发事件的 sql 语句。columns 字段记录了被修改的字段的信息。

### 删除表（drop table）

下面这个例子展示了**删除表**操作生成的事件的 value 部分：
<dx-codeblock>
:::  sql
{
  "source" : {
    "server" : "dip_source"
  },
  "position" : {
    "ts_sec" : 1655812326,
    "file" : "mysql-bin.000006",
    "pos" : 26063,
    "gtids" : "b24176f2-5409-11ec-80d4-b8599fe5c6ea:1-78",
    "snapshot" : true
  },
  "databaseName" : "dip_test",
  "ddl" : "DROP TABLE IF EXISTS `dip_test`.`customers`",
  "tableChanges" : [ ]
}
:::
</dx-codeblock>

其中 position 的内容为记录 binlog 文件，消费偏移量等信息。ddl 字段为触发事件的 sql 语句。

### 更改表名

下面这个例子展示了**更改**操作生成的事件的 value 部分：
<dx-codeblock>
:::  json
{
	"schema": {
		"type": "struct",
		"fields": ···,
		"optional": false,
		"name": "io.debezium.connector.mysql.SchemaChangeValue"
	},
	"payload": {
		"source": {
			"version": "1.9.0.Final",
			"connector": "mysql",
			"name": "task-lzpx4pdo",
			"ts_ms": 1656300979748,
			"snapshot": "false",
			"db": "testDB",
			"sequence": null,
			"table": "t_test",
			"server_id": 170993,
			"gtid": "b24176f2-5409-11ec-80d4-b8599fe5c6ea:80",
			"file": "mysql-bin.000006",
			"pos": 26411,
			"row": 0,
			"thread": null,
			"query": null
		},
		"databaseName": "testDB",
		"schemaName": null,
		"ddl": "rename table test to t_test",
		"tableChanges": [{
			"type": "ALTER",
			"id": "\"testDB\".\"t_test\"",
			"table": {
				"defaultCharsetName": "utf8",
				"primaryKeyColumnNames": ["id"],
				"columns": [{
					"name": "id",
					"jdbcType": -5,
					"nativeType": null,
					"typeName": "BIGINT",
					"typeExpression": "BIGINT",
					"charsetName": null,
					"length": 20,
					"scale": null,
					"position": 1,
					"optional": false,
					"autoIncremented": true,
					"generated": true,
					"comment": null
				}, {
					"name": "name",
					"jdbcType": 12,
					"nativeType": null,
					"typeName": "VARCHAR",
					"typeExpression": "VARCHAR",
					"charsetName": "utf8",
					"length": 20,
					"scale": null,
					"position": 2,
					"optional": true,
					"autoIncremented": false,
					"generated": false,
					"comment": null
				}],
				"comment": null
			}
		}]
	}
}
:::
</dx-codeblock>

其中 schema 中包含的是对 payload 的内容格式信息，这里省略了部分内容，payload 字段 source 为元数据信息，ddl 字段为触发事件的 sql 语句。columns 为受影响的表的字段。
