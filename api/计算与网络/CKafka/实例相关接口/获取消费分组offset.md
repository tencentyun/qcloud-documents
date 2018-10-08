## 1. 接口描述

本接口 (GetGroupOffsets) 用于在用户账户下获取 CKafka 消费分组详细信息。

接口请求域名：`ckafka.api.qcloud.com`

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见 [公共请求参数](https://cloud.tencent.com/doc/api/431/5883) 页面。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
|instanceId | 是| String|（过滤条件）按照实例 ID 过滤。|
|group|是|String  |kafka 消费分组。|
|topics|否|string array|group 订阅的主题名称数组，如果没有该数组，则表示指定的group下所有topic信息。|
|searchWord|否|string|模糊匹配topicName。|
|offset|否|int|默认0 ，本次查询的偏移位置。|
|limit|否|int| 默认50， 最大值50， 本次返回结果的最大个数。|



## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
|data|json array| |
|data::totalCount|int|符合本次搜索条件的所有topic。|
|data::topicList|json array|
|data::topicList::topic|string|topicName。|
|data::topicList::partitions|json array|
|data::topicList::parititons::partition|int| topic的partitionId。|
|data::topicList::partitions::offset|int|提交的offset位置。|
|data::topicList::partitions::metadata|string|支持消费者提交消息时，传入metadata作为它用，当前一般为空字符串。|
|data::topicList::partitions::log_end_offset|int|当前partition最新的offset。|
|data::topicList::partitions::lag|int|未消费的消费个数。|
## 4. 示例

输入：

```
 https://domain/v2/index.php?Action=GetGroupOffset&<公共请求参数>
```

输出：

```
{
    "code": 0,
    }
    "message": "",
    "codeDesc": "Success",
    "data": {
        "totalCount": 1,
        "topicList": [
            {
                "topic": "test",
                "partitions": [
                    {
                        "partition": 0,
                        "offset": 22689638,
                        "metadata": "",
                        "err_code": 0,
                        "log_end_offset": 207927929,
                        "lag": 185238291
                    }
                ]
            }
        ]
}
```

