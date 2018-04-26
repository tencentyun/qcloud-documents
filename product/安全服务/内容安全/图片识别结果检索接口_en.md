## API Description
This API (BSP.GetFileDetectionList) is used to get the result of FileDetection API, and multi-dimensional data retrieval is supported.

Protocol: `HTTPS`

Domain name: `csec.api.qcloud.com`

API name: `BSP.GetFileDetectionList`

## Request Parameters

Since the logical "Or" relationship exists among hotScore, pornScore, normalScore and confidence, if only one condition is satisfied, the desired result can be retrieved.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| paging.index | Required | UInt | The page numbers to which the data belongs |
| paging.count | Required | UInt | Number of items on the current page |
| filtering.beginTimestamp | Required | UInt | Start timestamp |
| filtering.endTimestamp | Required | UInt | End Timestamp |
| filtering.roomId | Optional | UInt | Backend room number |
| filtering.sdkAppId | Optional | UInt | The sdkappid for multi-person video |
| filtering.groupNum | Optional | UInt | User's room number |
| filtering.userId | Optional | UInt | User ID |
| hotScore.lower | Optional | UInt | The lowest score for a sexy image |
| hotScore.upper | Optional | UInt | The highest score for a sexy image |
| pornScore.lower | Optional | UInt | The lowest score for a porn image |
| pornScore.upper | Optional | UInt | The highest score for a porn image |
| normalScore.lower | Optional | UInt | The lowest score for a normal image |
| normalScore.upper | Optional | UInt | The highest score for a normal image |
| confidence.lower | Optional | UInt | The lowest score for the confidence of a porn image |
| confidence.lower | Optional | UInt | The highest score for the confidence of a porn image |

## Response Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| total | UInt | Total number of records |
| details | Array | Details of the retrieved image |

**Details of the retrieved image**

| Parameter Name | Type | Type |
|---------|---------|---------|
| url | String | Image link |
| hotScore | UInt | The score for a sexy image |
| pornScore | UInt | The score for a porn image |
| normalScore | UInt | The score for a normal image |
| confidence | UInt | The confidence of an image identified as a porn image |
| roomId | UInt | Backend room number |
| sdkAppId | UInt | The sdkappid for multi-person video |
| userId | UInt | User ID |
| groupNum | UInt | User's room number |

## Request Example

```
https://csec.api.qcloud.com/v2/index.php?Action=BSP.GetFileDetectionList&Nonce=22895&Region=all&SecretId=AKIDda6jN9xwrtMTeoazDzNlWK0RCan0eQMm&Timestamp=1462949302&confidence.lower=70&confidence.upper=90&filtering.beginTimestamp=1462939186&filtering.endTimestamp=1462939786&paging.count=1&paging.index=0&pornScore.lower=20&pornScore.upper=40&Signature=eGM8LtgwXoX7Iqo4nZmINPoi5LQ%3D
```

## Response Example

```
{
    "code": 0,
    "data": {
        "details": [
            {
                "confidence": 75,
                "hotScore": 0,
                "normalScore": 0,
                "pornScore": 99,
                "url": "http://qq.com/hello.jpg"
            }
        ],
        "total": 1
    },
    "message": "OK"
}
```

