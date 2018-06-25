## 1. API Description

This API (CreateTopic) is used to create topics under a CKafka instance.

Domain name for API request: ckafka.api.qcloud.com

## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/doc/api/431/5883).

| Parameter Name | Required | Type | Description |
| --- | --- | --- | --- |
| instanceId | Yes | String | Instance ID |
| topicName | Yes | String | Topic name, which must be a combination of not more than 64 characters. It can contain letters, numbers, and hyphens (-), and must begin with a letter. |
| partitionNum | Yes | Int | Number of partitions, which must be greater than 0 |
| replicaNum | Yes | Int | Number of replicas, which cannot be greater than the number of brokers (maximum is 3) |
| enableWhiteList | No | int | Whether to enable IP whitelist. 1: Enable 0: Disable |
| ipWhiteList.n | No | String | Quota limit of IP whitelist. Required when enableWhileList=1 |


## 3. Output Parameters

| Parameter Name | Type | Description |
| --- | --- | --- |
| topicId | String | Topic ID |

## 4. Example

Input:

```
 https://domain/v2/index.php?Action=CreateTopic&<Common request parameters>
```

Output:

```
  {
      "code" : 0,
	"codeDesc":"Success"
      "message" : "ok",
	"topicId" : "topic-xxoo234"
  }

```
