## API Name
ConfirmEvent

## Feature Description
1. This API is used to confirm that the message has been received after the developer calls to pull the event notification and gets the event;
2. For details, refer to [Server Event Notification](/document/product/266/7829).

## Request Method

### Request Domain
vod.api.qcloud.com

### Peak Calling Frequency
1,000 counts/min

##### Parameter Description
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| msgHandle.n | Yes | String | Event handler |
| COMMON_PARAMS | Yes |  | Refer to [Common Parameters](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### Request Example
```
https://vod.api.qcloud.com/v2/index.php?Action=ConfirmEvent
&msgHandle.1=XXXX
&msgHandle.2=YYYY
&COMMON_PARAMS
```
## API Response

##### Parameter Description
| Name | Type | Description |
|---------|---------|---------|
| code | Integer | Error code, 0:  Succeeded, other values:  Failed |
| message | String | Error message |

### Error Code Description
| Error Code | Description |
|---------|---------|
| 4000-7000 | Refer to [Common Error Codes](/document/product/266/7783)  |
| 1000 | Invalid parameter  |
| 1001 | Internal error  |
| 2000 | Internal error  |

### Response Example
```javascript
{
    "code": 0,
    "message": ""
}
```

