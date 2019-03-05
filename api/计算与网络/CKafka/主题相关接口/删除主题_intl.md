## 1. API Description

This API (DeleteTopic) is used to delete the topics under a CKafka instance.

Domain name for API request: ckafka.api.qcloud.com>

## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/doc/api/431/5883).

| Parameter Name | Required | Type | Description |
| --- | --- | --- | --- |
| instanceId | Yes | String | Instance ID |
| topicName | Yes | String | Topic name |


## 3. Example

Input:

```
 https://domain/v2/index.php?Action=DeleteTopic&instanceId=topic-xxxxxx&topicName=tinatest<Common request parameters>
```

Output:

```
  {
      "code" : 0,
      "codeDesc":"Success",
      "message" : "ok",
  }

```

