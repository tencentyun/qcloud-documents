## API Name
QueryWatermarkTemplate

## Feature Description
1. This API is used to query the watermark template details according to its ID.

## Request Method

### Request Domain
vod.api.qcloud.com

### Max Calling Frequency
100/min

### Parameter Description
| Parameter| Required | Type | Description |
|---------|---------|---------|---------|
| definition | Yes | Integer | Watermark template ID |
| COMMON_PARAMS | Yes |  | For more information, please see [Common Request Parameters](/document/api/213/6976) |

## Request Example
<pre>
https://vod.api.qcloud.com/v2/index.php?Action=QueryWatermarkTemplate
&definition=1008
&COMMON_PARAMS
</pre>


## API Response

### Parameter Description
| Parameter | Type | Description |
|---------|---------|---------|
| code | Integer | Error code, 0: Successful; other values: Failed. |
| message | String | Error message |
| definition | Integer | Watermark template ID |
| name | String | Watermark template name |
| comment | String | Description of the watermark template |
| type | String | Watermark type, with a fixed value "image". |
| url | Integer | Watermark URL |
| left | String | The horizontal distance from the upper left corner of the watermark image to the upper left corner of the video image. The string ending with % represents the percentage of the horizontal distance in the video image width. The string ending with px represents the horizontal distance in pixels. For example, 10% means the horizontal distance is 10% of the video width. 100px means the horizontal distance is 100 pixels. The default is 0px. |
| top | String | The vertical distance from the upper left corner of the watermark image to the upper left corner of the video image. The string ending with % represents the percentage of the vertical distance in the video image height. The string ending with px represents the vertical distance in pixels. For example, 10% means the vertical distance is 10% of the video height. 100px means the vertical distance is 100 pixels. The default is 0px. |
| width | String | The width of the watermark image. The string ending with % presents the percentage of watermark width in the video image width. The string ending with px represents watermark width in pixels. For example, 10% means watermark width is 10% of the video width. 100px means watermark width is 100 pixels. The default is 10%. |
| height | String | The height of the watermark image. The string ending with % presents the percentage of watermark height in the video image height. The string ending with px represents watermark height in pixels. For example, 10% means watermark height is 10% of the video height. 100px means watermark height is 100 pixels. The default is 0px, and the watermark image is scaled down by the video ratio. |

| Error Code | Description |
|---------|---------|
| 4000-7000 | For more information, please see [Common Error Codes](/document/product/266/7783)  |
| 1000 | Invalid parameter  |
| 10702 | Internal processing error |
| 10704 | The watermark template does not exist. |

### Response Example

```javascript
{
    "code": 0,
    "message": "",
    "definition": 1008,
    "name": "test",
    "createTime": 1485156352,
    "updateTime": 1485156352,
    "comment": "",
    "type": "image",
    "url": "http://www.watermark.com/test.jpg",
    "width": "10%",
    "left": "20px",
    "top": "30px"
}
```

