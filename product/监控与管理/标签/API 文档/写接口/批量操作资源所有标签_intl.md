
## API Description
This API (ModifyResourceTags) is used to deal with tags of existing Tencent Cloud resources in batches.

Domain name for API request: `tag.api.qcloud.com`

## Input Parameters
The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, please see [Common Request Parameters](https://cloud.tencent.com/document/product/651/18354).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|--------|
| resource |	Yes |	String	| Six-segment resource tag |
| addTags | No | Array | A collection of added tags |
| replaceTags |	No |		Array	| A collection of tags to modify |
| deleteTags |	No |		Array	| A collection of tags to delete |


The parameters of the array addTags are as follows:

| Parameter Name | Required | Type | Description |
|---------|---|------|---------|
| tagKey | No | String | Tag key, an element of addTags |
| tagValue | No | String | Tag value, an element of addTags |

The parameters of the array replaceTags are as follows:

| Parameter Name | Required | Type | Description |
|---------|-----|----|---------|
| tagKey | No | String | Tag key, an element of replaceTags |
| tagValue | No | String | Tag value, an element of replaceTags |

The parameters of the array deleteTags are as follows:

| Parameter Name | Required | Type | Description |
|---------|----|-----|---------|
| tagKey | No | String | Tag key, an element of deleteTags |
| tagValue | No | String | Tag value, an element of deleteTags |


## Output Parameters
None

## Error Codes

| Error Code | Description |
|---------|---------|
| 9003 | Invalid parameter |
| 30001 | The tag key does not exist |
| 30006 | The tag value does not exist |
| 30004 | The main account Uin does not exist |
| 30016 | The creator Uin does not exist |
| 30003 | Incorrect parameter in the six-segment resource tag |
| 30007 | The tag does not exist |
| 30010 |	A user can have at most 1,000 different keys |
| 30011	| The number of tag keys for a resource cannot exceed 50 |
| 30020 |	The number of tag values corresponding to a tag key exceeds the limit of 1,000 |

## Example
### Input example

```
https://domain/v2/index.php?Action=ModifyResourceTags&replaceTags.0.tagKey=t1&replaceTags.0.tagValue=v1&deleteTags.0.tagKey=t2&replaceTags.0.tagValue=v2&resource=qcs::cvm:ap-beijing:uin/1234567:instance/ins-123&<Common request parameters>
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

