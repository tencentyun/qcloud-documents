The device's account or alias is set by the terminal SDK when it calls the push registration API. For more information, please see the terminal SDK documentation.
When the number of accounts is greater than 10,000, it is recommended to use the API [Advanced Bulk Accounts](https://cloud.tencent.com/document/product/548/14713) for push.
URL: `http://domain name for API/v2/push/account_list?params`

### Request Parameters
In addition to the [common parameters](https://cloud.tencent.com/document/product/548/14705), the following parameters are needed:

| Parameter Name | Type | Required | Default | Description |
|-|-|-|-|-|
| account_list | string | Yes | None | Json array format, where each element is an account (string type). A maximum of 100 accounts are allowed for a single push. For example: ["account 1","account 2","account 3"] |
| message_type | uint | Yes | None | Message type: 1. notification; 2. transparently transferred message |
| message | string | Yes | None | For more information, please see [Push to Android Platform](https://cloud.tencent.com/document/product/548/14716) and [Push to iOS Platform](https://cloud.tencent.com/document/product/548/14717) |
| expire_time | uint | No | 3 days | The duration for storing the message offline (in sec). The maximum is 3 days. If it is set to 0, default value (3 days) is used. |
| multi_pkg | uint | No | 0 | 0 indicates that the message is delivered based on the packet name provided during registration; 1 indicates that the message is delivered based on the access id. All the Apps registered successfully with the access id can receive the message. |
| environment | uint | Only required for iOS | None | Required when the message is pushed to iOS devices. 1 indicates pushing to production environment; 2 indicates pushing to development environment. It is left empty or set to 0 in case of a push to Android platform. |

### Response Parameters
In the common response parameters, the json in the field "result" sends a error code for each account. This API does not return push id.

### Example
Before MD5 encryption, URL is used to generate sign, and Rest API URL is the URL of the final request. The following is an example of push to Android, in which the common parameters need to be replaced.

#### Before MD5 encryption:
```
GETopenapi.xg.qq.com/v2/push/account_listaccess_id=2100240957account_list=["easonshipushtestaccount"]message={"title": "test message", "content": "message from Rest API for testing the API for pushing messages to bulk accounts"}message_type=1timestamp=1502361241f255184d160bad51b88c31627bbd9530
```
#### Rest API URL:

```
http://openapi.xg.qq.com/v2/push/account_list?access_id=2100240957&account_list=["easonshipushtestaccount"]&message={"title": "test message", "content": "message from Rest API for testing the API for pushing messages to bulk accounts"}&message_type=1&timestamp=1502361241&sign=cff802738763385db89aaadb49dbe345
```

