事件模式是事件总线 EventBridge 用来过滤相关事件的模式定义。事件总线 EventBridge 通过事件模式过滤事件并将事件路由到事件目标，事件模式必须和匹配的事件具有相同的结构。本文介绍事件模式的常用类型。
### 注意事项

事件模式匹配的原则如下：


- 事件必须包含事件模式中列出的所有字段名，且事件模式里的字段名必须和事件中的字段名具有相同嵌套结构。
- 事件模式是逐个字符精确匹配的 ，需注意大小写，匹配过程中不会对字符串进行任何标准化的操作。
- 要匹配的值遵循 JSON 规则：用引号引起来的字符串、数字以及不带引号的关键字 true、false 和 null。


### 指定值及 OR 和 AND 模式

您可以指定某个字段的值进行匹配，对比值在 JSON 阵列中，以 [ ] 包围。 [ ] 内值为 OR，KEY 匹配为 AND。
以 COS 数据为例，接收到的事件如下：


```
{
    "specversion": "1.0",
    "id": "13a3f42d-7258-4ada-da6d-023a333b4662",
    "type": "cos:created:object",
    "source": "cos.cloud.tencent",
    "subject": "qcs::cos:ap-guangzhou:uid1250000000:bucketname",
    "time": "1615430559146",
    "region": "ap-guangzhou",
    "datacontenttype": "application/json;charset=utf-8",
    "resource": [
        "qcs::eb:ap-guangzhou:uid1250000000:eventbusid/eventruleid"
    ],
    "data": {
        "name": "testname",
        "scope": 100
    }
}
```
对于如上事件，若指定 data 字段的 name 值进行指定值匹配，可以被正常触发的规则如下：


```
{
    "data": {
        "name": [
            "testname"
        ]
    }
}
```
若指定 data 字段的 name 值进行 OR 匹配，可以被正常触发的规则如下：


```
{
    "data": {
        "name": [
            "testname","test"
        ]
    }
}
```


### 前缀匹配

您可以对比事件来源中的前缀进行键值匹配，例如 { "prefix": "2021-10-02" }。
以 COS 数据为例，接收到的事件如下：


```
{
    "specversion": "1.0",
    "id": "13a3f42d-7258-4ada-da6d-023a333b4662",
    "type": "cos:created:object",
    "source": "cos.cloud.tencent",
    "subject": "qcs::cos:ap-guangzhou:uid1250000000:bucketname",
    "time": "1615430559146",
    "region": "ap-guangzhou",
    "datacontenttype": "application/json;charset=utf-8",
    "resource": [
        "qcs::eb:ap-guangzhou:uid1250000000:eventbusid/eventruleid"
    ],
    "data": {
        "name": "testname",
        "scope": 100
    }
}
```
指定 data 字段的 name 的前缀匹配值，可以被正常触发的规则如下：


```
{
   "data":{
      "name":[
         {
            "prefix":"te"
         }
      ]
   }
}
```
### 后缀匹配

您可以对比事件来源中的后缀进行键值匹配，例如 { "suffix": ".txt" }。
以 TDMQ 数据为例，接收到的事件如下：


```
{
    "specversion": "1.0",
    "id": "13a3f42d-7258-4ada-da6d-023a333b4662",
    "type": "connector:tdmq",
    "source": "tdmq.cloud.tencent",
    "subject": "qcs::tdmq:$region:$account:topicName/$topicSets.clusterId/$topicSets.environmentId/$topicSets.topicName/$topicSets.subscriptionName",
    "time": "1615430559146",
    "region": "ap-guangzhou",
    "datacontenttype": "application/json;charset=utf-8",
    "data": {
                    "topic":  "persistent://appid/namespace/topic-1",
                    "tags": "testtopic",
                    "TopicType": "0",
                    "subscriptionName": "xxxxxx",
                    "toTimestamp": "1603352765001",
                    "partitions": "0",
                    "msgId": "123345346",
                    "msgBody": "Hello from TDMQ!"
    }
}
```
指定 data 字段的 topic 的后缀匹配值，可以被正常触发的规则如下：


```
{
    "data": {
        "topic": [{
            "suffix":"/topic-1"
        }]
    }
}
```
### 除外匹配

您可以指定某个字段除了提供的值之外的任何值进行匹配，例如 { "anything-but": "initializing" }。
以 COS 数据为例，接收到的事件如下：


```
{
   "specversion":"1.0",
   "id":"13a3f42d-7258-4ada-da6d-023a333b4662",
   "type":"cos:created:object",
   "source":"cos.cloud.tencent",
   "subject":"qcs::cos:ap-guangzhou:uid1250000000:bucketname",
   "time":"1615430559146",
   "region":"ap-guangzhou",
   "datacontenttype": "application/json;charset=utf-8",
   "resource":[
    "qcs::eb:ap-guangzhou:uid1250000000:eventbusid/eventruleid"
   ],
   "data":{
      "name":"testname",
      "scope":100
   }
}
```
指定 data 字段的 name 的除外匹配值，可以被正常触发的规则如下：


```
{
    "data": {
        "name": [{
            "anything-but":"test1"
        }]
    }
}
```
指定 data 字段的 name 的除外匹配值，不可以被正常触发的规则如下：


```
{
    "data": {
        "name": [{
            "anything-but":"testname"
        }]
    }
}
```
### 包含匹配

您可以指定 data 中存在的某个字段进行匹配，例如 { "contain": ".txt" }。
以 TDMQ 数据为例，接收到的事件如下：


```
{
    "specversion": "1.0",
    "id": "13a3f42d-7258-4ada-da6d-023a333b4662",
    "type": "connector:tdmq",
    "source": "tdmq.cloud.tencent",
    "subject": "qcs::tdmq:$region:$account:topicName/$topicSets.clusterId/$topicSets.environmentId/$topicSets.topicName/$topicSets.subscriptionName",
    "time": "1615430559146",
    "region": "ap-guangzhou",
    "datacontenttype": "application/json;charset=utf-8",
    "data": {
                    "topic":  "persistent://appid/namespace/topic-1",
                    "tags": "testtopic",
                    "TopicType": "0",
                    "subscriptionName": "xxxxxx",
                    "toTimestamp": "1603352765001",
                    "partitions": "0",
                    "msgId": "123345346",
                    "msgBody": "Hello from TDMQ!"
    }
}
```
指定 data 字段的 topic 的包含匹配值，可以被正常触发的规则如下：


```
{
    "data": {
        "topic": [{
            "contain":"topic-1"
        }]
    }
}
```

指定 data 字段的 topic 同时包含多个匹配值，可以被正常触发的规则如下：


```
{
    "data": {
        "topic": [{
            "contain":["topic-1","appid"]
        }]
    }
}
```
### 数组匹配

您可以通过语法过滤数组类型的字段，例如 `{"array": "{\"key1:\"value1\"}"}` 。
典型场景如要根据产品属性 `data` 结构中的某个字段生成事件规则，以数据订阅 DTS 数据为例，接收到的事件如下：


```
{
  "id": "13a3f42d-7258-4ada-da6d-023a33******",
  "type": "dts:mysql:update",
  "specversion": "1.0",
  "source": "dts.cloud.tencent",
  "subject": "cdb-xxx",
  "time": 1660013278609,
  "region": "ap-guangzhou",
  "dataContentType": "application/json;charset=utf-8",
  "tags": {
    "key1": "value1",
    "key2": "value2"
  },
  "data": {
    "topic": "topic-subs-xxx-cdb-xxx",
    "partition": 0,
    "offset": 72235,
    "partition_seq": 72236,
    "event": {
      "dmlEvent": {
        "dmlEventType": 1,
        "columns": [
          {
            "name": "time",
            "originalType": "time"
          },
          {
            "name": "id",
            "originalType": "int(11)",
            "isKey": true
          }
        ],
        "rows": [
          {
            "oldColumns": [
              {
                "dataType": 13,
                "charset": "utf8",
                "bv": "c3NzYWFhcWFxMTEx"
              }
            ],
            "newColumns": [
              {
                "dataType": 13,
                "charset": "utf8",
                "bv": "MjA6MTI6MjI="
              }
            ]
          }
        ]
      }
    },
    "header": {
      "sourceType": 1,
      "messageType": 2,
      "timestamp": 1648555949,
      "serverId": 109741,
      "fileName": "mysql-bin.000005",
      "position": 11172920,
      "gtid": "38cecd93-a9c2-11ec-b952-043f72d8da53:55",
      "schemaName": "dts",
      "tableName": "dts_mysql",
      "seqId": 72286,
      "isLast": true
    },
    "eb_consumer_time": "2022-03-29T20:12:29+08:00",
    "eb_connector": "cdb-xxx"
  }
}
```
对于如上事件，若需要通过 `columns` 字段进行规则匹配，可以被正常触发的规则如下：


```
{
    "source": "dts.cloud.tencent",
    "type": "dts:mysql:update",
    "data": {
        "event": {
            "dmlEvent": {
                "columns": [{
                    "array": "{\"name\":\"time\"}"
                }]
            }
        }
    }
}
```
一个字段的多条数据过滤规则时，多条数据之间是 **“与”** 的关系：


```
{
    "source": "dts.cloud.tencent",
    "type": "dts:mysql:update",
    "data": {
        "event": {
            "dmlEvent": {
                "columns": [{
                    "array": "{\"name\":\"id\",\"originalType\":\"int(11)\"}"
                            }]
            }
        }
    }
}
```
### IP 地址匹配

您可以指定 data 中字段的 IP 地址。例如，以下示例事件模式中只匹配 a 为10.0.0.0/24的事件：{ "cidr": "10.0.0.0/24" }。
以 COS 数据为例，接收到的事件如下：


```
{
    "specversion": "1.0",
    "id": "13a3f42d-7258-4ada-da6d-023a333b4662",
    "type": "cos:created:object",
    "source": "cos.cloud.tencent",
    "subject": "qcs::cos:ap-guangzhou:uid1250000000:bucketname",
    "time": "1615430559146",
    "region": "ap-guangzhou",
    "datacontenttype": "application/json;charset=utf-8",
    "resource": [
        "qcs::eb:ap-guangzhou:uid1250000000:eventbusid/eventruleid"
    ],
    "data": {
        "name": "testname",
        "scope": 100,
        "source-ip": "10.0.0.123"
    }
}
```
指定 data 字段的 source-ip 包含匹配值，可以被正常触发的规则如下：


```
{
    "data": {
        "source-ip": [{
            "cidr": "10.0.0.0/24"
        }]
    }
}
```
### 更多说明


- 进行模式匹配时，null 值和空字符串不等同。用于匹配空字符串的模式不会匹配到 null 值。
- 所有匹配模式可被嵌套使用，如下示例，同时嵌套除外匹配与前缀匹配。
```
{
    "data": {
        "name": [{
            "anything-but": {
                "prefix": "init"
            }
        }]
    }
}
```

- 所有匹配模式支持 OR 模式规则，如下示例，指定前缀匹配或指定后缀匹配。
```
{
    "data": {
        "topic": [
          {
            "prefix":"pre"
          },
          {
            "suffix":"suf"
          }
        ]
    }
}
```	
