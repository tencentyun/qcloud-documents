## 1. API Description

This API (AddTopicIpwhitelist) is used to add a whitelist for a topic.

Domain name for API request: ckafka.api.qcloud.com

## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/doc/api/431/5883).

| Parameter Name | Required | Type | Description |
| --- | --- | --- | --- |
| instanceId | Yes | String | Instance ID |
| topicName | Yes | String | Topic name |
| ipWhiteList.n | Yes | String | Required. IP whitelist |

## 3. Example

Input:

```
 https://domain/v2/index.php?Action=AddTopicIpwhitelist&instanceId=ckafka-xxooa0&topicName=tinatest&ipWhiteList.n=111.111.111.11&<Common request parameters>
```

Output:

```
  {
      "code" : 0,
	"codeDesc":"Success"
      "message" : "ok",
  }

```
> Note: If the IP whitelist is empty, all the IPs are not allowed to access this topic. Otherwise, only the IPs in the whitelist are allowed. This API adds the IPs in ipWhiteList to the existing whitelist.

