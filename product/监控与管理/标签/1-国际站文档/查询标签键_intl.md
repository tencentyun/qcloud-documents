## API Description
 This API (GetTagKeys) is used to query the created tag keys in a tag list.

 Domain name for API request: `tag.api.qcloud.com`

## Input Parameters
The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, please see [Common Request Parameters](https://cloud.tencent.com/document/product/651/18354).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|--------|
| createUin |	No |	Int	| Creator Uin. A value of 0 or empty value means only the current Uin is used for query. |
| page | No | Int | Page number. Default is 1. |
| rp |	No |	Int	| Page size. Default is 15. |


## Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| total | Int | Total number of results |
| page | Int | Current page number |
| rp | Int | Page size|
| rows | Array | Tag list |

The parameters of the array rows are as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| tagKey |	String	| Tag key |


## Error Codes

| Error Code | Description |
|---------|---------|
| 30004 | The main account Uin does not exist |

## Example
### Input example

```
https://domain/v2/index.php?Action=GetTagKeys&<Common request parameters>
```
### Output example

```
{
    "total": 1,
    "page": "1",
    "rp": "15",
    "rows": [
        {
            "tagKey": "testTagKey"
        }
    ]
}
```

