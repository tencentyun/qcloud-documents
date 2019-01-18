## API Name
ApplyUploadWatermark

## Feature Description
1. When creating a watermark template, you can use this API to obtain the upload URL of the watermark file.

> Note: A watermark template can be created in three steps with server APIs. This API is used in step 1:
> 1. Call this API to request the upload URL of the watermark file.
> 2. Use the HTTP PUT method to upload the watermark file to the URL returned in step 1. The request body is the binary data of the watermark image.
> 3. Call the API [CreateWatermarkTemplate](/document/product/266/11599) to create a watermark template.


## Request Method

### Request Domain
vod.api.qcloud.com

### Max Calling Frequency
100/min

### Parameter Description
| Parameter | Required | Type | Description |
|---------------|----------|---------|---------|
| type | Yes | String | Watermark file type, such as jpg or png. We recommend the png format. |
| COMMON_PARAMS | Yes |  | For more information, please see [Common Request Parameters](/document/api/213/6976) |


## Request Example
<pre>
https://vod.api.qcloud.com/v2/index.php?Action=ApplyUploadWatermark
&type=png
&COMMON_PARAMS
</pre>

## API Response

### Parameter Description
| Parameter | Type | Description |
|---------|---------|---------|
| code | Integer | Error code, 0: successful; other values: failed. |
| message | String | Error message |
| uploadUrl | String | The upload URL of the watermark file |

### Error Codes
| Error Code | Description |
|---------|---------|
| 4000-7000 | For more information, please see [Common Error Codes](/document/product/266/7783)  |
| 1000 | Invalid parameter  |
| 1001 | User information error  |


### Response Example

```javascript
{
    "code": 0,
    "message": "",
    "uploadUrl":"http://123.test.com/123.png&sign=abcd",
}
```
