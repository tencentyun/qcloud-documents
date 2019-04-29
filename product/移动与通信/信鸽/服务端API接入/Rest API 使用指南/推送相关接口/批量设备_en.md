Push notifications to bulk devices.
- First, you need to create a bulk message (get push_id).
- Next, push the bulk message you created to multiple devices.

## Create Bulk Message
URL: `http://domain name for API/v2/push/create_multipush?params`
### Request Parameters
In addition to the [common parameters](https://cloud.tencent.com/document/product/548/14705), the following parameters are needed:

| Parameter Name | Type | Required | Default | Description |
|-|-|-|-|-|
| message_type | uint | Yes | None | Message type: 1. notification; 2. transparently transfered message |
| message | string | Yes | None | For more information, please see [Push to Android Platform](https://cloud.tencent.com/document/product/548/14716) and [Push to iOS Platform](https://cloud.tencent.com/document/product/548/14717) |
| expire_time | uint | No | 3 days | The duration for storing the message offline (in sec). The maximum is 3 days. If it is set to 0, the message is not stored. This parameter is not required for iOS. |
| multi_pkg | uint | No | 0 | 0 indicates that the message is delivered based on the packet name provided during registration; 1 indicates that the message is delivered based on the access id. All the Apps registered successfully with the access id can receive the message. |
| environment | uint | Only required for iOS | None | Required when the message is pushed to iOS devices. 1 indicates pushing to production environment; 2 indicates pushing to development environment. It is left empty or set to 0 in case of a push to Android platform. |

### Response Parameters
In the common response parameters, the json of the field "result" is as follows:
```
{
"push_id": string (indicates the task ID assigned to the App)
}
```

## Push Bulk Message
URL: `http://domain name for API/v2/push/device_list_multiple?params`

### Request Parameters
In addition to [common parameters](https://cloud.tencent.com/document/product/548/14705), the following parameters are needed:

| Parameter Name | Type | Required | Default | Description |
|-|-|-|-|-|
| device_list | string | Yes | None | Json array format, where each element is a token (string type). A maximum of 1000 tokes are allowed for a sing push. For example: ["token 1","token 2","token 3"] |
| push_id | uint | Yes | None | push_id in the return values of API for creating bulk message |
### Response Parameters
In the common response parameters, the json of the field "result" is empty.

### Example
Before MD5 encryption, URL is used to generate sign, and Rest API URL is the URL of the final request (the following is an example of push to Android, in which the common parameters need to be replaced.)
- **Obtain push_id:**
#### Before MD5 encryption:
```
GETopenapi.xg.qq.com/v2/push/create_multipushaccess_id=2100264266message={"title":"test message","content":"message from Rest API for testing API for pushing messages to bulk devices","custom_content":{"key1":"value1","key2":"value2"}}message_type=2timestamp=1502694940d8fc29c627259a06452794e31dab5bb8
```
#### Rest API URL:
```
http://openapi.xg.qq.com/v2/push/create_multipush?access_id=2100264266&message={"title":"test message","content":"message from Rest API for testing API for pushing messages to bulk devices","custom_content":{"key1":"value1","key2":"value2"}}&message_type=2&timestamp=1502694940&sign=e5ca158c01712fb185399e67b6a57d1f
```
- **Push:**
#### Before MD5 encryption:
```
GETopenapi.xg.qq.com/v2/push/device_list_multipleaccess_id=2100264266device_list=["78e8540853619eb14fb49fdd53274c0c82ca2025"]push_id=2854657652timestamp=1502694940d8fc29c627259a06452794e31dab5bb8
```
#### Rest API URL:
```
http://openapi.xg.qq.com/v2/push/device_list_multiple?access_id=2100264266&device_list=["78e8540853619eb14fb49fdd53274c0c82ca2025"]&push_id=2854657652&timestamp=1502694940&sign=e4779a9173a1c51541800e76b8a25322
```
