Messages can be pushed to devices with tags such as Females, College Students, Low Spending, etc.
URL: `http://domain name for API/v2/push/tags_device?params`

### Request Parameters
In addition to the [common parameters](https://cloud.tencent.com/document/product/548/14705), the following parameters are needed:

| Parameter Name | Type | Required | Default | Description |
|-|-|-|-|-|
| message | string | Yes | None | For more information, please see [Push to Android Platform](https://cloud.tencent.com/document/product/548/14716) and [Push to iOS Platform](https://cloud.tencent.com/document/product/548/14717) |
| message_type | uint | Yes | 1 | Message type: 1. notification; 2. transparently transfered message. Enter 0 for iOS platform. |
| tags_list | json | Yes | None | ["tag 1","tag 2","tag 3"] |
| tags_op | string | Yes | None | Value is AND or OR |
| expire_time | uint | No | 3 days | The duration for storing the message offline (in sec). The maximum is 3 days. If it is set to 0, default value (3 days) is used. |
| send_time | string | No | Immediately | Specify a push time in the format of year-month-day hour:min:sec. If it is earlier than the current server time, the message is pushed immediately |
| multi_pkg | uint | No | 0 | 0 indicates that the message is delivered based on the packet name provided during registration; 1 indicates that the message is delivered based on the access id. All the Apps registered successfully with the access id can receive the message. This field does not apply to iOS platform. |
| environment | uint | Only required for iOS | None | Required when the message is pushed to iOS devices. 1 indicates pushing to production environment; 2 indicates pushing to development environment. It is left empty or set to 0 in case of a push to Android platform. |
| loop_times | uint | No | None| The number of times the loop task is executed. Value range: 1-15 |
| loop_interval | uint | No | None | The interval in which the loop task is executed (in days). Value range: 1-14. loop_interval is used with loop_times to indicate the lifecycle of a task and must not exceed 14 days. |
### Response Parameters
In the common response parameters, the json of the field "result" is as follows:
```
{
"push_id": string (indicates the task ID assigned to the App. For a loop task, it returns the ID of the parent loop task).
}
```
### Example
Before MD5 encryption, URL is used to generate sign, and Rest API URL is the URL of the final request (the following is an example of push to Android, in which the common parameters need to be replaced.)

#### Before MD5 encryption:

```
GETopenapi.xg.qq.com/v2/push/tags_deviceaccess_id=2100240957message={"title":"test message","content":"message from Rest API for testing the API for tags"}message_type=1tags_list=["qwertyuiop"]tags_op=ORtimestamp=1502360486f255184d160bad51b88c31627bbd9530
```
#### Rest API URL:

```
http://openapi.xg.qq.com/v2/push/tags_device?access_id=2100240957&message={"title":"test message","content":"message from Rest API for testing the API for tags"}&message_type=1&timestamp=1502360486&tags_list=["qwertyuiop"]&tags_op=OR&sign=95dbc4d1107a99d6824fda19e7ff09c9
```

