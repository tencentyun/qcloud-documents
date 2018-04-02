## 1. API Description

This API (DeleteTopicIpwhitelist) is used to delete whitelist of a topic.

Domain name for API request: ckafka.api.qcloud.com

## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/doc/api/431/5883).

| Parameter Name | Required | Type | Description |
| --- | --- | --- | --- |
| instanceId | Yes | String | Instance ID |
| topicName | Yes | String | Topic name |
| Ip.n | Yes | String | Required. IP whitelist |

## 3. Example

Input:

```
 https://domain/v2/index.php?Action=DeleteTopicIpwhitelist&instanceId=ckafka-xxooa0&topicName=tinatest&ip.n=111.111.111.11&<Common request parameters>
```

Output:

```
  {
      "code" : 0,
	"codeDesc":"Success"
      "message" : "ok",
  }

```
> Note: This API deletes the IPs in ipWhiteList from the existing whitelist.

