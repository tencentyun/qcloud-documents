## 1. 接口描述

本接口 (SetGroupOffsets) 用于在用户账户下获取 CKafka 消费分组详细信息。

接口请求域名：`ckafka.api.qcloud.com`

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见 [公共请求参数](https://cloud.tencent.com/doc/api/431/5883) 页面。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
|instanceId | 是| String|（过滤条件）按照实例 ID 过滤。|
|group|是|String  |kafka 消费分组。|
|topics|否|string array|表示需要重置offset的topic数组，不填表示全部topic。|
|strategy|是|int|重置offset的策略，入参含义 0. 对齐shift-by参数，代表把offset向前或向后移动shift条 1. 对齐参考(by-duration,to-datetime,to-earliest,to-latest),代表把offset移动到指定timestamp的位置 2. 对齐参考(to-offset)，代表把offset移动到指定的offset位置。|
|shift|否|int|当strategy为0时，必须包含该字段，可以大于零代表会把offset向后移动shift条，小于零则将offset向前回溯shift条数。正确重置后新的offset应该是(old_offset + shift)，需要注意的是如果新的offset小于partition的earliest则会设置为earliest，如果大于partition 的latest则会设置为latest。|
|timestamp|否|int|	单位ms。当strategy为1时，必须包含该字段，其中-2表示重置offset到最开始的位置，-1表示重置到最新的位置(相当于清空)，其它值则代表指定的时间，会获取topic中指定时间的offset然后进行重置，需要注意的时，如果指定的时间不存在消息，则获取最末尾的offset。|
|offset|否|int|需要重新设置的offset位置。当strategy为2，必须包含该字段。|

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
|data|json array| |
|data::succ|json array|重置成功数组，说明参考实例|
|data::failed|json array|重置失败数组，说明参见实例

## 4. 示例

输入：

```
 https://domain/v2/index.php?Action=SetGroupOffset&<公共请求参数>
```

输出：

```
{
    "codeDesc":"Success",
    "code":0,
    "msg":"",
    "data":{
        "succ":[
            {
                "topic":"streams-wordcount-output",// 主题名称
                "error_code":0,
                "partitions":[
                    {
                        "partition":2, //分区id 
                        "offset":27708,// 分区offset
                        "error_code":0
                    },
                    {
                        "partition":1,
                        "offset":112843,
                        "error_code":0
                    },
                    {
                        "partition":3,
                        "offset":29149,
                        "error_code":0
                    },
                    {
                        "partition":0,
                        "offset":29402,
                        "error_code":0
                    }
                ]
            }
        ],
        "failed":[
            {
                "topic":"aaaa",// 主题名称
                "error_code":3,
                "error_msg":"This request is for a topic or partition that does not exist on this broker.",// 失败信息
                "partitions":[
                ]
            }
        ]
    }
}
```

