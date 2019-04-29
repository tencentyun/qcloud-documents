## API Description
This API (GetTags) is used to query the created tag lists.

Domain name for API request: `tag.api.qcloud.com`

## Input Parameters
The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, please see [Common Request Parameters](https://cloud.tencent.com/document/product/651/18354).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|--------|
| createUin |	No |	int	| Creator Uin. A value of 0 or empty value means only the current Uin is used for query. |
| page | No | int | Page number. Default is 1. |
| rp |	No |	int	| Page size. Default is 15. |
| tagKey | No | String | Tag key, which only exists when tag value exists. If it does not exist, all tags of the user are queried. |
| tagValue | No | String | Tag value, which only exists when tag key exists. If it does not exist, all tags of the user are queried. |

## Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| total | int | Total number of results |
| page | int | Current page number |
| rp | int | Page size|
| rows | Array | Tag list |

The parameters of the array rows are as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| tagKey |	String	| Tag key |
| tagValue |	String	| Tag value |
| canDelete | int | Indicates that the tag cannot be deleted because it is associated with some resources |

## Error Codes

| Error Code | Description |
|---------|---------|
| 30004 | The main account Uin does not exist |

## Example
### Input example

```
https://domain/v2/index.php?Action=GetTags&tagKey=testTagKey&tagValue=testTagVal&<Common request parameters>
```
### Output example

```
{
    "total": 1,
    "page": "1",
    "rp": "15",
    "rows": [
        {
            "tagKey": "testTagKey",
            "tagValue": "testTagVal",
            "canDelete": 0
        }
    ]
}
```

