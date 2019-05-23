## API Name
DescribeVodInfo

## Feature Description
1. This API is used to acquire video attributes via FileID, including name, tag and creation time.

## Request Method

### Request Domain
vod.api.qcloud.com

### Peak Calling Frequency
100 counts/min

##### Parameter Description
| Parameter Name | Required | Type    | Description                              |
| -------------- | -------- | ------- | ---------------------------------------- |
| fileIds.n      | No       | String  | Video ID list. Batch operation is currently not supported |
| from           | No       | String  | Start time. Default is 1970-1-1 00:00:00 |
| to             | No       | String  | End time. Default is 2038-1-1 00:00:00   |
| classId        | No       | Integer | Video category ID, used for filtering    |
| status         | No       | Integer | Video status, used for filtering. -1: Upload incomplete, does not exist; 0: Initialize, not in use; 1: Verification failed, not in use; 2: Normal; 3: Paused; 4: Transcoding; 5: Publishing; 6: Deleting; 7: Transcoding failed; 100: Deleted |
| orderby        | No       | Integer | Order of the results. By default, the results are sorted in ascending order by time. 0: Ascending order by time; 1: Descending order by time |
| pageNo         | No       | Integer | Page number                              |
| pageSize       | No       | Integer | Page size, value range: 10-100           |
| COMMON_PARAMS  | Yes      |         | Refer to [Common Parameters](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### Request Example
```
https://vod.api.qcloud.com/v2/index.php?Action=DescribeVodInfo
&fileIds.1=1976554120332374777
&COMMON_PARAMS
```
## API Response

##### Parameter Description
| Name       | Type    | Description                              |
| ---------- | ------- | ---------------------------------------- |
| code       | Integer | Error code, 0:  Succeeded, other values:  Failed |
| message    | String  | Error message                            |
| totalCount | Integer | Total number of videos                   |
| fileSet    | Array   | Video list result set                    |

fileSet video list result set

| **Parameter name** | **Type** | **Description**                          |
| ------------------ | -------- | ---------------------------------------- |
| fileId             | String   | Video ID                                 |
| fileName           | String   | Video name                               |
| size               | String   | Video size                               |
| duration           | String   | Video duration                           |
| status             | String   | Video status. -1: Upload incomplete, does not exist; 0: Initialize, not in use; 1: Verification failed, not in use; 2: Normal; 3: Paused; 4: Transcoding; 5: Publishing; 6: Deleting; 7: Transcoding failed; 10: Waiting to be transcoded; 100: Deleted |
| vid                | String   | Unique ID of the video                   |
| createTime         | String   | Video creation time                      |
| updateTime         | String   | Video modification time                  |
| classId            | String   | Video category ID                        |
| className          | String   | Video category name                      |
| imageUrl           | String   | Video cover image                        |
| tags               | Array    | Video tag list                           |
| description        | string   | Description                              |
| cdnStatus          | Integer  | Indicate whether CDN publishing operation has been performed in the API. 0 - Not been published; 1 - Publishing, 2 - Successful, 3 - Publishing failed, 4 - Terminated (not in use), 5 - Deleted |

### Error Code Description
| Error Code | Description                              |
| ---------- | ---------------------------------------- |
| 4000-7000  | Refer to [Common Error Codes](/document/product/266/7783) |
| 1          | Internal error                           |
| 1000       | Invalid parameter                        |
| 1001       | Internal error                           |
| 1003       | Internal error                           |
| 2000       | Internal error                           |
| 10008      | The file does not exist                  |
| 10022      | Internal error                           |

### Response Example
```javascript
{
    "code": 0,
    "message": "",
    "fileSet": [
        {
            "fileId": "1976554120332374777",
            "fileName": "Blue Jasmine(01h35m56s-01h38m23s)",
            "fileIntro": "",
            "size": "7865592",
            "duration": "147",
            "status": "2",
            "vid": "1200_1870483a9a6011e4a137dfa495b17abf",
            "createTime": "2015-01-12 21:37:11",
            "updateTime": "2015-01-13 11:23:01",
            "classId": "0",
            "className": "Others",
            "imageUrl": "http://p.qpic.cn/videoyun/0/1200_1870483a9a6011e4a137dfa495b17abf_1/640",
            "tags": [
                "Others"
            ]
        }
    ]
}
```

