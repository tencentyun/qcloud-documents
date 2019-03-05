
## API Description
This API (AddResourceTag) is used to associate resources on Tencent Cloud with tags.

Domain name for API request: `tag.api.qcloud.com `

## Input Parameters
The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, please see [Common Request Parameters](https://cloud.tencent.com/document/product/651/18354).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|--------|
| tagKey |	Yes |	String	| Tag key |
| tagValue |	Yes |	String	| Tag value |
| resource |	Yes |	String	| Six-segment resource tag |

## Output Parameters

None

## Error Codes

| Error Code | Description |
|---------|---------|
| 30001 | The tag key does not exist |
| 30002 | Default tag keys `qcloud:` and `tencent:` must be used. You cannot change them. |
| 30004 | The main account Uin does not exist |
| 30016 | The creator Uin does not exist |
| 30003 | Incorrect parameter in the six-segment resource tag |
| 30010 | The number of created tag keys exceeds the limit of 1,000 |
| 30020 |	The number of tag values corresponding to a tag key exceeds the limit of 1,000 |
| 30005 |	The user resource tag already exists. You cannot add it again. |

## Example
### Input example

```
https://domain/v2/index.php?Action=AddResourceTag&tagKey=t1&tagValue=v1&resource=qcs::cvm:ap-beijing:uin/1234567:instance/ins-123&<Common request parameters>
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

