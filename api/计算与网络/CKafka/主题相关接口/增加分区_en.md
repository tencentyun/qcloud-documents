## 1. API Description

This API (AddPartition) is used to add partitions in a topic.

Domain name for API request: ckafka.api.qcloud.com

## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/doc/api/431/5883).

| Parameter Name | Required | Type | Description |
| --- | --- | --- | --- |
| instanceId | Yes | String | Instance ID |
| topicName | Yes | String | Topic name |
| partitionNum | Yes | Int | Required. Number of partitions |

## 3. Example

Input:

```
 https://domain/v2/index.php?Action=AddPartition&instanceId=ckafka-xxooa0&topicName=tinatest&partitionNum=3&<Common request parameters>
```

Output:

```
  {
      "code" : 0,
      "codeDesc":"Success",
      "message" : "ok",
  }

```
> Note: All the partitions under the same topic have the same number of replicas.
