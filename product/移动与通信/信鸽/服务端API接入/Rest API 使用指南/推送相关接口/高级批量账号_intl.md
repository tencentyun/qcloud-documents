If the number of destination accounts of a push is very large (for example, greater than10000), it is recommended to use the API account_list_multiple.
- First, you need to create a bulk message (similar to pushing to bulk devices).
- Next, select the accounts for the bulk push.

## Create Bulk Message
URL: `http://domain name for API/v2/push/create_multipush?params`

### Request Parameters
In addition to the [common parameters](https://cloud.tencent.com/document/product/548/14705), the following parameters are needed:

| Parameter Name | Type | Required | Default | Description |
|-|-|-|-|-|
| message_type | uint | Yes | None | Message type: 1. notification; 2. transparently transferred message |
| message | string | Yes | None | For more information, please see [Push to Android Platform](https://cloud.tencent.com/document/product/548/14716) and [Push to iOS Platform](https://cloud.tencent.com/document/product/548/14717) |
| expire_time | uint | No | None | The duration for storing the message offline (in sec). The maximum is 3 days. During the timeout period, bulk push for this message can be initiated |
| multi_pkg | uint | No | 0 | 0 indicates that the message is delivered based on the packet name provided during registration; 1 indicates that the message is delivered based on the access id. All the Apps registered successfully with the access id can receive the message | 
| environment | uint | Only required for iOS | None | Required when the message is pushed to iOS devices. 1 indicates pushing to production environment; 2 indicates pushing to development environment. It is left empty or set to 0 in case of a push to Android platform. |

## Select Accounts for Bulk Push

URL: `http://domain name for API/v2/push/account_list_multiple?params`

### Request Parameters
In addition to the [common parameters](https://cloud.tencent.com/document/product/548/14705), the following parameters are needed:

| Parameter Name | Type | Required | Default | Description |
|-|-|-|-|-|
| account_list | string | Yes | None | Json array format, where each element is an account (string type). A maximum of 1,000 accounts are allowed for a single push. For example: ["account 1","account 2","account 3"] |
| push_id | uint | Yes | None | push_id in the return values of API for creating bulk message |

### Response Parameters
In the common response parameters, the json of the field "result" is empty.

### Example
See [Bulk Devices](https://cloud.tencent.com/document/product/548/14709).

