## 1. API Description

This API (ListInstance) is used to obtain the list of CKafka instances under the user account.

Domain name for API request: ckafka.api.qcloud.com

## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/doc/api/431/5883).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| instanceId | No | String | (Filter condition) Filter by instance ID |
| searchWord | No | String | (Filter condition) Filter by instance name. Fuzzy search is supported. |
| status.n | No | Int | (Filter condition) Status of instance. 0: Creating; 1: Running; 2: Deleting. All instances are returned by default if this parameter is let empty. |
| offset | No | Int | Offset value. It defaults to 0 if left empty. |
| limit | No | Int | Number of returned results. It defaults to 10 if left empty. The maximum is 20. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| totalCount | Int | Number of instances matching the filter condition.
| instanceList | Array | List of instance information. |
| instanceList::instanceId | String| Instance ID |
| instanceList::instanceName | String | Instance name |
| instanceList::status | Int | Status of instance. 0: Creating; 1: Running; 2: Deleting. |

## 4. Example

Input:

```
 https://domain/v2/index.php?Action=ListInstance&<Common request parameters>
```

Output:

```
  {
      "code" : 0,
      "message" : "ok",
	"codeDesc":"Success",
	"totalCount": 14,
     "instanceList": [
        {
            "instanceId":"ckafka-xxooa0",
		"instanceName":"test",
		"status":0
        }
    ]
  }

```







