## API Name
CreateWatermarkTemplate

## Feature Description
1. This API is used to create a watermark template.

Note: A watermark template can be created in three steps with server APIs. This API is used in step 3:
1. Call the API [ApplyUploadWatermark](https://cloud.tencent.com/document/product/266/11607) to request the upload URL of the watermark file;
2. Use the HTTP PUT method to upload the watermark file to the URL returned in step 1. The request body is the binary data of the watermark image;
3. Call this API to create a watermark template.


## Request Method

### Request Domain
vod.api.qcloud.com

### Max Calling Frequency
100/min

### Parameter Description
| Parameter| Required | Type | Description |
|---------|---------|---------|---------|
| name | No | String | Watermark template name, with a maximum length of 64 bytes. |
| comment | No | String | Description of the template, with a maximum length of 1024 bytes. |
| type | No | String | Watermark type, with a fixed value "image". |
| url | Yes | String | The URL of the watermark, which must be the URL returned after API ApplyUploadWatermark is called. |
| left | No | String | The horizontal distance from the upper left corner of the watermark image to the upper left corner of the video image. The string ending with % presents the percentage of the horizontal distance in the video image width. The string ending with px represents the horizontal distance in pixels. For example, 10% means the horizontal distance is 10% of the video width. 100px means the horizontal distance is 100 pixels. The default is 0px. |
| top | No | String | The vertical distance from the upper left corner of the watermark image to the upper left corner of the video image. The string ending with % presents the percentage of the vertical distance in the video image height. The string ending with px represents the vertical distance in pixels. For example, 10% means the vertical distance is 10% of the video height. 100px means the vertical distance is 100 pixels. The default is 0px. |
| width | Yes | String | The width of the watermark image. The string ending with % presents the percentage of watermark width in the video image width. The string ending with px represents watermark width in pixels. For example, 10% means watermark width is 10% of the video width. 100px means watermark width is 100 pixels. The default is 10%. |
| height | No | String | The height of the watermark image. The string ending with % presents the percentage of watermark height in the video image height. The string ending with px represents watermark height in pixels. For example, 10% means watermark height is 10% of the video height. 100px means watermark height is 100 pixels. The default is 0px, and the watermark image is scaled down by the video ratio. |
| COMMON_PARAMS | Yes |  | For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976) |

## Request Example

<pre>
https://vod.api.qcloud.com/v2/index.php?Action=CreateWatermarkTemplate
&name=test
&type=image
&url=www.watermark.com/test.jpg
&left=20px
&top=30px
&width=100px
&COMMON_PARAMS
</pre>

## API Response

### Parameter Description
| Parameter | Type | Description |
|---------|---------|---------|
| code | Integer | Error code, 0: successful; other values: failed. |
| message | String | Error message |
| definition | Integer | Sampling screenshot template ID |

### Error Codes
| Error Code | Description |
|---------|---------|
| 4000-7000 | For more information, please see [Common Error Codes](https://cloud.tencent.com/document/product/266/7783)  |
| 1000 | Invalid parameter  |
| 1001 | Internal error  |
| 10706 | The number of watermark templates has reached the limit  |
| 10801 | The "url" parameter in the request is invalid. |
| 10802 | The "type" parameter in the request is invalid. |
| 10803 | The "left" parameter in the request is invalid. |
| 10804 | The "top" parameter in the request is invalid. |
| 10810 | The "width" parameter in the request is invalid. |
| 10811 | The "height" parameter in the request is invalid. |

### Response Example

```javascript
{
    "code": 0,
    "message": "",
    "definition": 1008
}
```

