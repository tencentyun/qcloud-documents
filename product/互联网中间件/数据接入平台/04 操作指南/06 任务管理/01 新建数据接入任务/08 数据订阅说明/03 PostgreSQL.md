
## 简介

Debezium PostgreSQL connector 能够抓取 PostgreSQL 数据库中的行级（row-level）修改操作，并生成相应的修改事件。Debezium PostgreSQL connector 第一次连接 PostgreSQL 服务器时，会对所有数据库生成一个快照（snapshot），然后会持续的抓取提交给数据库的包括新增（insert）、更新（update）、删除（delete）在内的行级修改操作，并生成数据修改事件，将其作为消息提交给 Kafka 的相应 topic 。客户端应用可以通过消费对应 topic中的消息来对数据库修改事件进行处理，从而达到监控特定数据库的目的。

本文档是根据 Debezium 官方文档进行整理和归纳而来。详情参见 [Debezium connector for PostgreSQL](https://debezium.io/documentation/reference/stable/connectors/postgresql.html#postgresql-events)。

## 事件格式

Debezium PostgreSQL connector 针对每一个行级的插入、更新、删除操作生成数据修改事件。每一个事件（event）在作为消息提交给 kafka 的主题（Topic），Topic 里每条消息包含 key 和 value 两部分。示例如下：

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
<td align="left"><code>schema</code> 字段描述了key的payload 字段的结构，即它描述了被修改的表的主键（primary key）结构，如果表没有主键，则描述其唯一约束（unique key）的结构。</td>
</tr>
<tr>
<td align="center">2</td>
<td align="center"><code>payload</code></td>
<td align="left"><code>payload</code> 字段的结构和第一个<code>schema</code> 中描述的相同，包含了被修改的行的键值。</td>
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
<td align="left"><code>payload</code> 字段的结构和 <code>schema</code> 中定义的相同，它包含被修改行的真实数据。</td>
</tr>
</tbody></table>

## 事件消息 key 

不同类型事件的消息都有一样的 key 结构，下面给出一个示例，一个修改事件的 key 包含被修改的表的主键结构以及对应行的实际主键值。：
<dx-codeblock>
:::  sql
CREATE TABLE customers (
  id SERIAL,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  PRIMARY KEY(id)
);
:::
</dx-codeblock>

该操作对应的事件消息的 key 如下所示（JSON表示）：
<dx-codeblock>
:::  jsom
{
  "schema": { 
    "type": "struct",
    "name": "PostgreSQL_server.public.customers.Key", 
    "optional": false, 
    "fields": [ 
          {
              "name": "id",
              "index": "0",
              "schema": {
                  "type": "INT32",
                  "optional": "false"
              }
          }
      ]
  },
  "payload": { 
      "id": "1"
  },
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
<td align="left">Schema 描述了 payload 中的结构</td>
</tr>
<tr>
<td align="left">2</td>
<td align="left"><code>PostgreSQL_server.inventory.customers.Key</code></td>
<td align="left">schema 的名称格式为 *connector-name*.*database-name*.*table-name*.<code>Key</code>。在这个例子中: <code>PostgreSQL_server</code> 是生成事件的 connector 的名字。 <code>inventory</code> 是对应数据库的名字。 <code>customers</code> 是表的名字。</td>
</tr>
<tr>
<td align="left">3</td>
<td align="left"><code>optional</code></td>
<td align="left">表示字段是否是可选项。</td>
</tr>
<tr>
<td align="left">4</td>
<td align="left"><code>fields</code></td>
<td align="left">列出了所有 <code>payload</code> 中包含的字段及其结构, 包括字段名、字段类型、以及是否可选.</td>
</tr>
<tr>
<td align="left">5</td>
<td align="left"><code>payload</code></td>
<td align="left">包含被修改行的主键.。在例子中仅包含一个字段名为 <code>id</code> 的主键值： <code>1</code>。</td>
</tr>
</tbody></table>

## 事件列表

前面介绍了一个事件消息的 key 的结构，不同类型事件的 key 结构是相同的。本节列举了不同的事件类型，介绍了这些事件类型各自的 value 结构。

### 新增事件（create events）

下面给出一个 Debezium PostgreSQL connector 针对数据库新增操作生成的消息：
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
                "name": "PostgreSQL_server.inventory.customers.Value", 
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
                "name": "PostgreSQL_server.inventory.customers.Value",
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
                        "optional": false,
                        "field": "schema"
                    },
                    {
                        "type": "string",
                        "optional": false,
                        "field": "table"
                    },
                    {
                        "type": "int64",
                        "optional": true,
                        "field": "txId"
                    },
                    {
                        "type": "int64",
                        "optional": true,
                        "field": "lsn"
                    },
                    {
                        "type": "int64",
                        "optional": true,
                        "field": "xmin"
                    }
                ],
                "optional": false,
                "name": "io.debezium.connector.postgresql.Source", 
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
        "name": "PostgreSQL_server.inventory.customers.Envelope" 
    },
    "payload": { 
        "before": null, 
        "after": { 
            "id": 1,
            "first_name": "Anne",
            "last_name": "Kretchmar",
            "email": "annek@noanswer.org"
        },
        "source": { 
            "version": "1.9.3.Final",
            "connector": "postgresql",
            "name": "PostgreSQL_server",
            "ts_ms": 1559033904863,
            "snapshot": true,
            "db": "postgres",
            "sequence": "[\"24023119\",\"24023128\"]"
            "schema": "public",
            "table": "customers",
            "txId": 555,
            "lsn": 24023128,
            "xmin": null
        },
        "op": "c", 
        "ts_ms": 1559033904863 
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
<td align="left"><code>PostgreSQL_server.inventory.customers.Value</code></td>
<td align="left">表示该字段是 PostgreSQL_server 连接器生成的针对 inventory 数据库的 customers 表的 value 部分信息。</td>
</tr>
<tr>
<td align="left">5</td>
<td align="left"><code>io.debezium.connector.postgresql.Source</code></td>
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
<td align="left">表示导致事件生成的修改操作的类型，例子中的 c 表示 修改操作创建了一个新的行。<br>c = create<br>u = update<br>d = delete<br>r = read (仅 snapshots)<br>t = truncate<br>m = message</td>
</tr>
<tr>
<td align="left">8</td>
<td align="left"><code>source</code></td>
<td align="left">source 字段是一个描述事件元数据的字段。它包含的一些字段可以用来与其他事件做比较，如比较事件生成的顺序、事件是否属于同一个事务等。该字段包含以下元数据信息：<br> Debezium version<br>Connector type and name<br>Database and table that contains the new row<br>Stringified JSON array of additional offset information. The first value is always the last committed LSN, the second value is always the current LSN. Either value may be <code>null</code><br>Schema name<br>If the event was part of a snapshot<br>ID of the transaction in which the operation was performed<br>Offset of the operation in the database log<br>Timestamp for when the change was made in the database</td>
</tr>
</tbody></table>

### 更新事件（update events）

下面给出一个 Debezium PostgreSQL connector 针对数据库更新操作生成的消息：
<dx-codeblock>
:::  json
{
    "schema": { ... },
    "payload": {
        "before": { 
            "id": 1
        },
        "after": { 
            "id": 1,
            "first_name": "Anne Marie",
            "last_name": "Kretchmar",
            "email": "annek@noanswer.org"
        },
        "source": { 
            "version": "1.9.3.Final",
            "connector": "postgresql",
            "name": "PostgreSQL_server",
            "ts_ms": 1559033904863,
            "snapshot": false,
            "db": "postgres",
            "schema": "public",
            "table": "customers",
            "txId": 556,
            "lsn": 24023128,
            "xmin": null
        },
        "op": "u", 
        "ts_ms": 1465584025523  
    }
}
:::
</dx-codeblock>

其中 schema 字段和创建操作的事件相同，而 payload 部分有所不同，在创建事件中，before 字段为 null，表示没有原始数据，而更新事件中包含了更新前（before）和更新后（after）的数据。

### 清空表事件（truncate events）

当一个清空表事件发生时，事件消息的 key 为 null，消息示例如下所示：
<dx-codeblock>
:::  json
{
    "schema": { ... },
    "payload": {
        "source": { 
            "version": "1.9.3.Final",
            "connector": "postgresql",
            "name": "PostgreSQL_server",
            "ts_ms": 1559033904863,
            "snapshot": false,
            "db": "postgres",
            "schema": "public",
            "table": "customers",
            "txId": 556,
            "lsn": 46523128,
            "xmin": null
        },
        "op": "t", 
        "ts_ms": 1559033904961 
    }
}
:::
</dx-codeblock>

如果一个 TRUNCATE 语句作用于多个表，那么 connector 会给每一个被作用的表生成一个 truncate event 消息。

### 消息事件（message events）

该消息类型仅支持 Postgres 14+ 的 pgoutput plugin。事务型消息事件的格式示例如下：
<dx-codeblock>
:::  json
{
    "schema": { ... },
    "payload": {
        "source": { 
            "version": "1.9.3.Final",
            "connector": "postgresql",
            "name": "PostgreSQL_server",
            "ts_ms": 1559033904863,
            "snapshot": false,
            "db": "postgres",
            "schema": "",
            "table": "",
            "txId": 556,
            "lsn": 46523128,
            "xmin": null
        },
        "op": "m", 
        "ts_ms": 1559033904961, 
        "message": { 
            "prefix": "foo",
            "content": "Ymfy"
        }
    }
}
:::
</dx-codeblock>

非事务型消息的格式示例如下：
<dx-codeblock>
:::  json
{
    "schema": { ... },
    "payload": {
        "source": { 
            "version": "1.9.3.Final",
            "connector": "postgresql",
            "name": "PostgreSQL_server",
            "ts_ms": 1559033904863,
            "snapshot": false,
            "db": "postgres",
            "schema": "",
            "table": "",
            "lsn": 46523128,
            "xmin": null
        },
        "op": "m", 
        "ts_ms": 1559033904961 
        "message": { 
            "prefix": "foo",
            "content": "Ymfy"
    }
}
:::
</dx-codeblock>

其中事务类型的消息事件包含事务 ID 号字段 “txId”。此外消息事件还包含一个 message 字段，其含义解释如下：

| Field name | Description                                                  |
| :--------- | :----------------------------------------------------------- |
| message    | 该字段包含了消息的元数据：<br />prefix（text）<br />Content (byte array that is encoded based on the [binary handling mode](https://debezium.io/documentation/reference/stable/connectors/postgresql.html#postgresql-property-binary-handling-mode) setting) |

### 删除事件（delete events）

下面给出一个 Debezium PostgreSQL connector 针对数据库删除操作生成的消息：
<dx-codeblock>
:::  json
{
    "schema": { ... },
    "payload": {
        "before": { 
            "id": 1
        },
        "after": null, 
        "source": { 
            "version": "1.9.3.Final",
            "connector": "postgresql",
            "name": "PostgreSQL_server",
            "ts_ms": 1559033904863,
            "snapshot": false,
            "db": "postgres",
            "schema": "public",
            "table": "customers",
            "txId": 556,
            "lsn": 46523128,
            "xmin": null
        },
        "op": "d", 
        "ts_ms": 1465581902461 
    }
}
:::
</dx-codeblock>

其中 schema 字段和创建操作的事件相同，而 payload 部分有所不同，删除事件中包含了修改前（before）的数据，但更新后（after）的数据为 null，表示数据已删除。

### 更新主键（primary key events）

如果一个操作修改了数据表中某行的主键，那么 connector 会生成一条 **删除事件 **来表示原主键对应的数据行删除，同时生成一条**新增事件**来表示插入的新主键对应的行。每一条消息的 header 都会和相应的 key 关联。官方描述如下：

- The `DELETE` event record has `__debezium.newkey` as a message header. The value of this header is the new primary key for the updated row.
- The `CREATE` event record has `__debezium.oldkey` as a message header. The value of this header is the previous (old) primary key that the updated row had.
