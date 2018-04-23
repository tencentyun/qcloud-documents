## 1. API Description

This API (SetTopicAttributes) is used to modify the topic attributes under a CKafka instance.

Domain name for API request: ckafka.api.qcloud.com

## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/doc/api/431/5883).

| Parameter Name | Required | Type | Description |
| --- | --- | --- | --- |
| instanceId | Yes | String | Instance ID |
| topicName | Yes | String | Topic name |
| enableWhiteList | No | int | Whether to enable IP whitelist. 1: Enable 0: Disable |


## 3. Example

Input:

```
 https://domain/v2/index.php?Action=SetTopicAttributes&instanceId=ckafka-xxxxxx&topicName=xxxxx&<Common request parameters>
```

Output:

```
  {
      "code" : 0,
	"codeDesc":"Success"
      "message" : "ok",
  }

```
