## 1. 接口描述
接口请求域名：`ckafka.api.qcloud.com`
本接口（GetGroupOffsets）用于在用户账户下获取 CKafka 消息分组 offset。

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，其它参数见 [公共请求参数](https://cloud.tencent.com/doc/api/431/5883) 页面。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
|instanceId | 是| String|（过滤条件）按照实例 ID 过滤|
|group|是|String  |Kafka 消费分组|
|topics|否|String Array|group 订阅的主题名称数组，如果没有该数组，则表示指定的 group 下所有 topic 信息|
|searchWord|否|String|模糊匹配 topicName|
|offset|否|Int|本次查询的偏移位置，默认为0|
|limit|否|Int| 本次返回结果的最大个数，默认为50，最大值为50|



## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
|data|JSON Array| 本次返回的消费分组信息|
|data::totalCount|Int|符合本次搜索条件的所有 topic 个数|
|data::topicList|JSON Array|订阅的 topic 数组，其中每个元素为一个 json object|
|data::topicList::topic|String|group 订阅的 topicName|
|data::topicList::partitions|JSON Array|该主题分区数组，其中每个元素为一个 json object|
|data::topicList::parititons::partition|Int| topic 的 partitionId|
|data::topicList::partitions::offset|Int|consumer 提交的 offset 位置|
|data::topicList::partitions::metadata|String|支持消费者提交消息时，传入 metadata 作为它用，当前一般为空字符串|
|data::topicList::partitions::log_end_offset|Int|当前 partition 最新的 offset|
|data::topicList::partitions::lag|Int|未消费的消息个数|

## 4. 示例
**输入：**
```http
 https://domain/v2/index.php?Action=GetGroupOffsets&<公共请求参数>
```

**输出：**
```
{
	"code": 0,
	"message": "",
	"codeDesc": "Success",
	"data": {
		"totalCount": 1,
		"topicList": [{
			"topic": "test",
			"partitions": [{
				"partition": 0,
				"offset": 22689638,
				"metadata": "",
				"err_code": 0,
				"log_end_offset": 207927929,
				"lag": 185238291
			}]
		}]
	}
}
```

