
## API Description
This API (GetResourceTagsByResourceIds) is used to query key-value pairs of existing resource tags.

Domain name for API request: `tag.api.qcloud.com`

## Input Parameters
The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, please see [Common Request Parameters](https://cloud.tencent.com/document/product/651/18354).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|--------|
| createUin |	No |	Int	| Creator uin. A value of 0 or empty value means the current uin is used for query. |
| page | Yes | String | Page number. Default is 1. |
| rp |	Yes |	String	| Page size. Default is 15. |
| region | Yes | String | A region where resources reside. |
| serviceType | Yes | String | Business type |
| resourcePrefix | Yes | Int | Resource prefix |
| resourceIds | Yes | Array | Uniquely identifies a resource |

## Output Parameters

data's parameters are as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| total | Int | Total number of results |
| page | Int | Current page number |
| rp | Int | Page size|
| rows | Array | Tag list |

rows' parameters are as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| tagKey |	String	| Tag key |
| tagValue |	String	| Tag value |
| resourceId | String | Uniquely identifies a resource |

## Error Codes

| Error Code | Description |
|---------|---------|
| 30004 | The main account Uin does not exist |

## Example
### Input example

```
https://domain/v2/index.php?Action=GetResourceTagsByResourceIds&region=ap-guangzhou&seviceType=cvm&prefix=instance&resourceId.0=ins-123&resourceId.1=ins-456&<Common request parameters>
```
### Output example

```
{
        "total": 4,
        "page": 1,
        "rp": 15,
        "rows": [
            {
                "tagKey": "testTagKey1",
                "tagValue": "testTagVal1",
                "resourceId": "ins-123"
            },
            {
                "tagKey": "testTagKey2",
                "tagValue": "testTagVal2",
                "resourceId": "ins-123"
            },
            {
                "tagKey": "testTagKey3",
                "tagValue": "testTagVal3",
                "resourceId": "ins-123"
            },
            {
                "tagKey": "testTagKey1",
                "tagValue": "testTagVal1",
                "resourceId": "ins-456"
            }
        ]
    }
```

