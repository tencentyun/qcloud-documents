## 1. API Description

This API (ListTopic) is used to obtain the list of topics under a CKafka instance.

Domain name for API request: ckafka.api.qcloud.com

## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/doc/api/431/5883).

| Parameter Name | Required | Type | Description |
| --- | --- | --- | --- |
| instanceId | Yes | String | Instance ID |
| searchWord | No | String | (Filter condition) Filter by topicName. Fuzzy search is supported. |
| offset | No | Int | Offset value. It defaults to 0 if left empty. |
| limit | No | Int | Number of returned results. It defaults to 10 if left empty. The maximum is 20. |

## 3. Output Parameters

| Parameter Name | Type | Description |
| --- | --- | --- |
| totalCount | Int | Number of topics matching the filter condition. |
| topicList | Array | List of topic information |
| topicList::topicId | String | Topic ID |
| topicList::topicName | String | Topic name |

## 4. Example

Input:

```
 https://domain/v2/index.php?Action=ListTopic&instanceId=ckafka-xxooa0&<Common request parameters>
```

Output:

```
  {
      "code" : 0,
	"codeDesc":"Success"
      "message" : "ok",
	"totalCount" : 10,
	"topicList" : [
		{
		"topicId" : "topic-xxoo234",
		"topicName" : "jimmy",
		}
	]
  }

```

