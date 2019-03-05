
## API Description
This API (CreateTag) is used to create tags for resources on Tencent Cloud.

Domain name for API request: `tag.api.qcloud.com `

## Input Parameters
The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, please see [Common Request Parameters](https://cloud.tencent.com/document/product/651/18354).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|--------|
| tagKey |	Yes |	String	| Tag key |
| tagValue |	Yes |	String	| Tag value |

## Output Parameters
None

## Error Codes

| Error Code | Description |
|---------|---------|
| 30001 | The tag key does not exist |
| 30002 | System reserved tag keys `qcloud:` and `tencent:` cannot be created. |
| 30004 | The main account Uin does not exist |
| 30016 | The creator Uin does not exist |
| 30017 |	The user tag already exists |
| 30010 | The number of created tag keys exceeds the limit of 1,000 |
| 30020 |	The number of tag values corresponding to a tag key exceeds the limit of 1,000 |

## Example
### Input example

```
https://domain/v2/index.php?Action=CreateTag&tagKey=t1&tagValue=v1&<Common request parameters>
```

### Output example

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": []
}
```

