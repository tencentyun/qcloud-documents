## 1. 接口描述

本接口 (SetGroupOffsets) 用于在用户账户下设置 CKafka 实例某个消费分组 offset。

接口请求域名：`ckafka.api.qcloud.com`

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见 [公共请求参数](https://cloud.tencent.com/doc/api/431/5883) 页面。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
|instanceId | 是| String|（过滤条件）按照实例 ID 过滤。|
|group|是|String  |kafka 消费分组。|
|topics|否|String Array|表示需要重置 offset 的 topic 数组，不填表示全部 topic。<br>传参方法请参见 [topic.N（数组参数）](https://cloud.tencent.com/document/product/597/14358#topic)|
|strategy|是|Int|重置 offset 的策略，入参含义：<br> 0：对齐 shift-by 参数，代表把 offset 向前或向后移动 shift 条。<br> 1：对齐参考(by-duration,to-datetime,to-earliest,to-latest),代表把 offset 移动到指定timestamp的位置。<br> 2：对齐参考(to-offset)，代表把 offset 移动到指定的 offset 位置。|
|shift|否|Int|当 strategy 为 0 时，必须包含该字段，可以大于零代表会把 offset 向后移动 shift 条，小于零则将 offset 向前回溯 shift 条数。正确重置后新的 offset 应该是(old_offset + shift)，**如果新的 offset 小于 partition 的 earliest 则会设置为 earliest，如果大于partition 的 latest 则会设置为 latest**。|
|timestamp|否|Int|	单位：ms。当 strategy 为 1 时，必须包含该字段，其中 -2 表示重置 offset 到最开始的位置，-1 表示重置到最新的位置(相当于清空)，其它值则代表指定的时间，会获取 topic 中指定时间的 offset 然后进行重置，**如果指定的时间不存在消息，则获取最末尾的 offset**。|
|offset|否|Int|需要重新设置的 offset 位置。当 strategy 为 2 时，必须包含该字段。|

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
|data|JSON Array|本次接口返回的设置消费分组结果信息。|
|data::succ|JSON Array|重置成功数组，说明参考实例。|
|data::failed|JSON Array|重置失败数组，说明参见实例。

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

