## API Name
GetVideoInfo

## Feature Description
1. The API is used to acquire various information of a single video, including:
    1. Basic information (basicInfo): Video name, size, duration, cover image, etc.;
    2. Transcoding result information (transcodeInfo): Such information of a transcoded video with different bit rates as video address, specification, bit rate, and resolution;
    3. Image sprite information (imageSpriteInfo): Sprite information after acquiring image sprite of a video;
    4. Information about screenshots captured by time offset (snapshotByTimeOffsetInfo): Information about all screenshots captured by time offset.
2. You can specify that only partial information is returned.

## Request Method

### Domain for API Request
vod.api.qcloud.com

### Peak Calling Frequency
100 counts/min

##### Parameter Description
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| fileId | Yes | String | ID of the video whose information is to be acquired |
| infoFilter.n | No | String | Specify the information to be returned. You can specify various information. If this field is left blank, all information will be returned by default. Available values: basicInfo (Basic information), transcodeInfo (Transcoding result information), imageSpriteInfo (Image sprite information), and snapshotByTimeOffsetInfo (Information about screenshots captured by time offset).  |
| COMMON_PARAMS | Yes |  | Refer to [Common Parameters](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### Request Example

**Acquire all information of a video**

```
https://vod.api.qcloud.com/v2/index.php?Action=GetVideoInfo
&fileId=12345
&COMMON_PARAMS
```

**Acquire partial information of a video (basic information and transcoding result information) **
```
https://vod.api.qcloud.com/v2/index.php?Action=GetVideoInfo
&fileId=12345
&infoFilter.1=basicInfo
&infoFilter.2=transcodeInfo
&COMMON_PARAMS
```

## API Response

##### Parameter Description
| Name | Type | Description |
|---------|---------|---------|
| code | Integer | Error code, 0:  Succeeded, other values:  Failed |
| message | String | Error message |
| basicInfo | Object | Basic information of a video |
| transcodeInfo | Object | Transcoding result information of a video |
| imageSpriteInfo | Object | Image sprite information of a video |
| snapshotByTimeOffsetInfo | Object | Information about screenshots captured by time offset |
<!--
| keyFrameDescInfo | Object | Video keyframe description information |
-->

**basicInfo (Basic information of a video)**

| **Parameter name** | **Type** | **Description** |
|---------|---------|---------|
| name | String | Video name |
| size | Integer | Video size. Unit: byte |
| duration | Integer | Video duration. Unit: second |
| description | String | Video description |
| status | String | Video status, "normal": Normal |
| createTime | Integer | Video creation time (Unix timestamp) |
| updateTime | Integer | Last update time for video information (Unix timestamp) |
| expireTime | Integer | Video expiration time (Unix timestamp). After a video expires, the video and all its dependent objects (transcoding result, image sprite, etc.) will be deleted |
| classificationId | Integer | ID of the video category |
| classificationName | String | Name of the video category |
| playerId | Integer | Player ID |
| coverUrl | String | URL of video cover image |
| type | String | Video encapsulation format, such as MP4 and FLV |
| sourceVideoUrl | String | Source video URL |

**transcodeInfo (Transcoding result information of a video)**

> If the video has been transcoded, you can get the transcoding result information of the video; if the video has not been transcoded or the transcoding failed, no transcoding result information exists for the video.

| **Parameter name** | **Type** | **Description** |
|---------|---------|---------|
| transcodeList | Array | A list of transcoding information for all specifications. Each element represents the transcoding result of a specification |
| transcodeList.url | String | Video file URL after transcoding |
| transcodeList.definition | Integer | Refer to [Transcoding Specifications](/document/product/266/8098) |
| transcodeList.bitrate | Integer | Bit rate. Unit: bps |
| transcodeList.height | Integer | Height. Unit: px |
| transcodeList.width | Integer | Width. Unit: px |

**imageSpriteInfo (Image sprite information of a video)**

> If image sprite of the video has been captured, you can get image sprite information of the video; if image sprite has not been captured or capture failed, no image sprite information exists for the video.

| **Parameter name** | **Type** | **Description** |
|---------|---------|---------|
| imageSpriteList | Array | A list of image sprite information for certain specifications. Each element represents a list of image sprites with same specifications |
| imageSpriteList.definition | Integer | Refer to [Image Sprite Specifications](/document/product/266/8099) |
| imageSpriteList.height | Integer | Height of images in image sprite |
| imageSpriteList.width | Integer | Width of images in image sprite |
| imageSpriteList.totalCount | Integer | Number of images in one image sprite |
| imageSpriteList.imageUrls | Array | URL of images in one image sprite |

**snapshotByTimeOffsetInfo (Information about screenshots captured by time offset)**

> If the screenshot of the video has been captured by time offset, you can get the information about screenshots captured by time offset; if it has not been captured, no such screenshot information exists for the video.

| **Parameter name** | **Type** | **Description** |
|---------|---------|---------|
| snapshotByTimeOffsetList | Array | A list of information about screenshots captured by time offset for certain specifications. Each specification may have multiple lists of screenshots. You can set a name (in "name" field) for each list of screenshots |

snapshotByTimeOffsetList: A list of information about screenshots captured by time offset for certain specifications

| **Parameter name** | **Type** | **Description** |
|---------|---------|---------|
| snapshotByTimeOffsetList.definition | Integer | Refer to [ Specifications for Screenshots Captured by Time Offset](/document/product/266/8097) |
| snapshotByTimeOffsetList.picInfoList | Array | A list of screenshot information for the same specification. Each element represents a screeshot. |
<!---
| name | String | The name of the list of screenshots is specified by the user |
-->

picInfoList: A list of screenshot information for the same specification. Each element represents a screeshot

| **Parameter name** | **Type** | **Description** |
|---------|---------|---------|
| timeOffset | Integer | The time offset of the screeshot in the video file. Unit: millisecond |
| url | String | URL of the screeshot. If "status" is not 0, the URL does not exist |

<!---
keyFrameDescInfo: Video keyframe description information

| **Parameter name** | **Type** | **Description** |
|---------|---------|---------|
| keyFrame | Array | A list of video keyframe information. Each element represents a keyframe |

keyFrame A list of video keyframe information

| **Parameter name** | **Type** | **Description** |
|---------|---------|---------|
| timeOffset | Integer | Keyframe time offset. Only for one keyframe. Unit: second |
| type | String | type | Keyframe type |
| comment | String | Keyframe comment |
| screenshotUrl | String | Screenshot URL for the keyframe |
| custom | String | Custom information. No more than 512 characters |
-->

### Error Code Description
| Error Code | Description |
|---------|---------|
| 4000-7000 | Refer to [Common Error Codes](/document/product/266/7783)  |
| 1 | Internal error  |
| 1000 | Invalid parameter  |
| 1001 | Internal error  |
| 1003 | Internal error  |
| 2000 | Internal error  |
| 10008 | The file does not exist  |
| 10022 | Internal error |

### Response Example
```javascript
{
    "code": 0,
    "message": "",
    "basicInfo": {
        "name": "test file",
        "size": 1000,
        "duration": 10,
        "description": "",
        "status": "",
        "createTime": 1485156352,
        "updateTime": 1485156352,
        "expireTime": 1485256352,
        "classificationId": 1,
        "classificationName": "",
        "playerId": 0,
        "coverUrl": "http://www.qq.com/test.jpg",
        "type": "",
        "sourceVideoUrl": "http://vcloud1200.tc.qq.com/1200_5b9688d481d8b811095d30a78cf44c4285026a4c.f0.mp4"
    },
    "transcodeInfo": {
        "transcodeList": [
            {
                "url": "http://vcloud1200.tc.qq.com/1200_5b9688d481d8b811095d30a78cf44c4285026a4c.f0.mp4",
                "definition": 0,
                "bitrate": 2332000,
                "height": 576,
                "width": 1024
            }
        ]
    },
    "imageSpriteInfo": {
        "imageSpriteList": [
            {
                "definition": 10,
                "height": 576,
                "width": 1024,
                "totalCount": 100,
                "imageUrls": [
                    "http://www.qq.com/test.jpg"
                ]
            }
        ]
    },
    "snapshotByTimeOffsetInfo": {
        "snapshotByTimeOffsetList": [
            {
                "definition": 10,
                "name": "",
                "picInfoList": [
                    {
                        "timeOffset": 1,
                        "url": "http: //www.qq.com/test1.jpg"
                    },
                    {
                        "timeOffset": 10,
                        "url": "http: //www.qq.com/test10.jpg"
                    }
                ]
            }
        ]
    }
}
```

