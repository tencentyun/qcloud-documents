Push notifications to a single device.
URL: `http://domain name for API/v2/push/single_device?params`

### Request Parameters
In addition to the [common parameters](https://cloud.tencent.com/document/product/548/14705), the following parameters are needed:

| Parameter Name | Type | Required | Default | Description |
|-|-|-|-|-|
| device_token | string | Yes | None | The unique ID of the device to which the messages are pushed |
| message_type | uint | Yes | None | Message type: 1. notification; 2. transparently transfered message. Enter 0 for iOS platform. |
| message | string | Yes | None | For more information, please see [Push to Android Platform](https://cloud.tencent.com/document/product/548/14716) and [Push to iOS Platform](https://cloud.tencent.com/document/product/548/14717) |
| expire_time | uint | No | 3 days | The duration for storing the message offline (in sec). The maximum is 3 days. If it is set to 0, default value (3 days) is used. |
| send_time | string | No | Immediately | Specify a push time in the format of year-month-day hour:min:sec. If it is earlier than the current server time, the message is pushed immediately. |
| multi_pkg | uint | No | 0 | 0 indicates that the message is delivered based on the packet name provided during registration; 1 indicates that the message is delivered based on the access id. All the Apps registered successfully with the access id can receive the message. This field does not apply to iOS platform. |
| environment | uint | Only required for iOS | None | Required when the message is pushed to iOS devices. 1 indicates pushing to production environment; 2 indicates pushing to development environment. It is left empty or set to 0 in case of a push to Android platform. |
### Response Parameters
In the common response parameters, the json of the field "result" is empty.
This API does not return push id.

### Example
Before MD5 encryption, URL is used to generate sign, and Rest API URL is the URL of the final request (the following is an example of push to Android, in which the common parameters need to be replaced.)
#### Before MD5 encryption:
```
GETopenapi.xg.qq.com/v2/push/single_deviceaccess_id=2100250470device_token=76501cd0277cdcef4d8499784a819d4772e0fddemessage={"title":"test message","content":"message from Rest API for testing the API for pushing messages to a single device"}message_type=1timestamp=1502356505f1fa8b11f540794bf13e10d499ac5c36
```

#### Rest API URL:
```
http://openapi.xg.qq.com/v2/push/single_device?access_id=2100250470&timestamp=1502356505&device_token=76501cd0277cdcef4d8499784a819d4772e0fdde&message_type=1&message={"title":"test message","content":"message from Rest API for testing the API for pushing messages to a single device"}&sign=b7f5761d37fb352536e53db0c50ffcc6
```

