## API Name
UpdateWatermarkTemplate

## Feature Description
1. This API is used to update watermark templates.


## Request Method

### Request Domain
vod.api.qcloud.com

### Max Calling Frequency
100/min

### Parameter Description
| Parameter | Required | Type | Description |
|---------|---------|---------|---------|
| definition | Yes | Integer | Sampling screenshot template ID |
| type | No | String | Watermark type, with a fixed value "image". |
| left | No | String | The horizontal distance from the upper left corner of the watermark image to the upper left corner of the video image. The string ending with % presents the percentage of the horizontal distance in the video image width. The string ending with px represents the horizontal distance in pixels. For example, 10% means the horizontal distance is 10% of the video width. 100px means the horizontal distance is 100 pixels. The default is 0px. |
| top | No | String | The vertical distance from the upper left corner of the watermark image to the upper left corner of the video image. The string ending with % represents the percentage of the vertical distance in the video image height. The string ending with px represents the vertical distance in pixels. For example, 10% means the vertical distance is 10% of the video height. 100px means the vertical distance is 100 pixels. The default is 0px. |
| width | Yes | String | The width of the watermark image. The string ending with % represents the percentage of watermark width in the video image width. The string ending with px represents watermark width in pixels. For example, 10% means watermark width is 10% of the video width. 100px means watermark width is 100 pixels. |
| height | No | String | The height of the watermark image. The string ending with % presents the percentage of watermark height in the video image height. The string ending with px represents the height in pixels. For example, 10% means the height is 10% of the video height. 100px means the height is 100 pixels. The default is 0px, and the watermark image is scaled down by the video ratio. |
| COMMON_PARAMS | Yes |  | For more information, please see [Common Request Parameters](/document/api/213/6976) |

## Request Example
<pre>
https://vod.api.qcloud.com/v2/index.php?Action=UpdateWatermarkTemplate
&definition=10005
&name=test
&type=image
&url=www.watermark.com/test.jpg
&width=10%
&left=20px
&top=30px
&COMMON_PARAMS
</pre>

## API Response

### Parameter Description
| Parameter | Type | Description |
|---------|---------|---------|
| code | Integer | Error code, 0: successful; other values: failed. |
| message | String | Error message |

### Error Codes
| Error Code | Description |
|---------|---------|
| 4000-7000 | For more information, please see [Common Error Codes](/document/product/266/7783)  |
| 1000 | Invalid parameter  |
| 10801 | The "url" parameter in the request is invalid. |
| 10802 | The "type" parameter in the request is invalid. |
| 10803 | The "left" parameter in the request is invalid. |
| 10804 | The "top" parameter in the request is invalid. |
| 10807 | The "definition" parameter in the request is invalid. |
| 10810 | The "width" parameter in the request is invalid. |
| 10811 | The "height" parameter in the request is invalid. |
### Response Example

```javascript
{
    "code": 0,
    "message": ""
}
```

