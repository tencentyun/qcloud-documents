## 1. API Description

This API (SetInstanceAttributes) is used to set the CKafka instance attributes.

Domain name for API request: ckafka.api.qcloud.com

## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/doc/api/431/5883).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| instanceId | Yes | String | Instance ID |
| msgRetentionTime | No | Int | Optional. The maximum retention time of instance log (in minute). The minimum is 1 min, and the maximum is 30 days. |


## 3. Example

Input:

```
 https://domain/v2/index.php?Action=SetInstanceAttributes&instanceId=ckafka-xxxxxx&<Common request parameters>
```

Output:

```
  {
      "code" : 0,
	"codeDesc":"Success"
      "message" : "ok",
  }

```







