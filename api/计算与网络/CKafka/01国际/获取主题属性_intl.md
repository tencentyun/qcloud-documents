## 1. API Description

This API (GetTopicAttributes) is used to obtain the topic attributes of a CKafka instance.

Domain name for API request: ckafka.api.qcloud.com

## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/doc/api/431/5883).

| Parameter Name | Required | Type | Description |
| --- | --- | --- | --- |
| instanceId | Yes | String | Instance ID |
| topicName | No | String | Topic name |

## 3. Output Parameters

| Parameter Name | Type | Description |
| --- | --- | --- |
| topicId | String | Topic ID |
| partitionNum | Int | Number of partitions |
| enableWhiteList | int | Whether to enable IP whitelist. 1: Enable 0: Disable |
| ipWhiteList | array | IP whitelist |
| createTime | Int | Creation time, expressed as timestamp (in second) |
| partitions | Array | Partition details |
| partitions::partition | Int | Partition id |
| partitions :: leaderStatus | Int | Running status of leader  |
| partitions::replicaNum | array | Number of replicas |
| partitions::isrNum | array | Number of ISRs |

## 4. Example

Input:

```
 https://domain/v2/index.php?Action=GetTopicAttributes&instanceId=ckafka-xxooa0&<Common request parameters>
```

Output:

```
 {
      "code" : 0,
	"codeDesc":"Success"
      "message" : "ok",
		
		"topicId" : "topic-xxoo234",
		"partitionNum" : 2,
		"enableWhiteList" : 1,
		"ipWhiteList" :["10.0.0.1"],
		"partitions" : [
			{
			"partition":0,
                		"leaderStatus":1,
			"isrNum": 3,
			"replicaNum" : 3
			},
			{
			"partition":1,
                		"leaderStatus":2,
			"isrNum": 2,
			"replicaNum" : 3
			}
		]
  }
```







