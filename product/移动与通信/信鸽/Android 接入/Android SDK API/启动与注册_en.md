An App can only provide push service to the XGPush SDK after completing the launch of XGPush and registration on it. Before this, make sure to configure AccessId and AccessKey. The new version of SDK has integrated the launch of XGPush and App registration into the registration API. This means that by default, both the launch and registration can be completed by simply calling the registration API.
After the registration is completed successfully, the device token is returned. This token is used to identify the uniqueness of the device and used as a unique identifier by XGPush for maintaining the connection with the backend. For more information on how to obtain the token, please see "[Obtaining Token](https://cloud.tencent.com/document/product/548/14683)" section.
Two versions of registration API are available: simplified version and the version with callback. You can select a version as needed.

## Registration of Bound Device
In an ordinary registration, only the current device is registered, and the backend pushes messages for different device tokens. The API is available in two versions.
Note: This registration method does not support pushing to account.
#### Version 1:
**Prototype**
```
public static void registerPush(Context context)
```

**Parameters**

| Name | Description | Null |
 |-|-|-|
| context | Context object of the current App | No |

**Example**
```
XGPushManager.registerPush(this);
```
#### Version 2:
A version with callback is provided to make it easier for users to obtain the result of registration.
	
**Prototype**
```
public static void registerPush(Context context,
final XGIOperateCallback callback)
```

**Parameters**

| Name | Description | Null |
|-|-|-|
| context | Context object of the current App | No |
| callback | Callbacks for successful and failed operations | No |

**Example**
```
XGPushManager.registerPush(this, new XGIOperateCallback() {
@Override
public void onSuccess(Object data, int flag) {
Log.d("TPush", "Registered successfully. Device token is:" + data);
}
@Override
public void onFail(Object data, int errCode, String msg) {
Log.d("TPush", "Registration failed, error code:" + errCode + ",error message:" + msg);
}
})
```

## Registration of Bound Account
This means that after the registration of bound device, the specified account is registered with the App (one account can be used to log in on multiple devices) so that the messages can be pushed to the specified account from backend. The API is available in two versions.
>Note: The account can be any type of business account such as email address, QQ number, mobile number and user name. A maximum of 15 device tokens can be bound to an account. When the limit is exceeded, the latest token will randomly override the previously bound one.

#### Version 1:
**Prototype**
```
public static void registerPush(Context context, String account)
```
**Parameters**

| Name | Description | Null |
|-|-|-|
| context | Context object of the current App | No |
| account | The account bound. An App can push messages to the account bound to it. The account cannot be a single character such as "2" and "a". Any developer who wants to push messages to an account alias needs to set the alias in the "account" field of the registration request when calling the registration API. Only one account alias is allowed for a device. | No |

**Example**

```
XGPushManager.registerPush(this, "UserAccount")
```
#### Version 2:
A version with callback is provided to make it easier for users to obtain the result of registration.

**Prototype**
```
public static void registerPush(Context context, String account,
final XGIOperateCallback callback)
```

**Parameters**

| Name | Description | Null |
|-|-|-|
| context | Context object of the current App | No |
| account | The account bound. An App can push messages to the account bound to it. Any developer who wants to push messages to an account alias needs to set the alias in the "account" field of the registration request when calling the registration API. Only one account alias is allowed for a device. When multiple devices log in to the same account, only the last bound device is valid. | No |
| callback | Callbacks for successful and failed operations | No |

**Example**
```
XGPushManager.registerPush(this, "UserAccount",
new XGIOperateCallback() {
@Override
public void onSuccess(Object data, int flag) {
Log.d("TPush", "Registered successfully. Device token is:" + data);
}

@Override
public void onFail(Object data, int errCode, String msg) {
Log.d("TPush", "Registration failed, error code:" + errCode + ",error message:" + msg);
}
});
```

## Unbinding Account
For an account that was bound to the App by calling registerPush(context, account), it can be unbound by calling the following method (for example, when the user logs out).
Call
```
registerPush(context, "*") or registerPush(context, "*", xGIOperateCallback )
```
Set account="*" to unbind the account.

In the versions later than XGPush 3.2.2 beta, you need to call a new API to unbind an account. For more information, please see [API Overview](https://cloud.tencent.com/document/product/548/13950).

>Note:
>Unbinding an account is only to remove the association between the token and the App account. If the full/tag-based/token push is used, the account can still receive the notifications/messages.

## Registration with Login Status
For the scenarios where user login status is required, such as mobile QQ or Qzone scenarios, a registration API with login status is provided.

**Prototype**

```
public static void registerPush(Context context, String account,
String ticket, int ticketType, String qua,
final XGIOperateCallback callback)
```

**Parameters**

| Name | Description | Null |
|-|-|-|
| context | Context object of the current App | No |
| callback | Callbacks for successful and failed operations | No |
| account | The account bound. An App can push messages to the account bound to it. Any developer who wants to push messages to an account alias needs to set the alias in the "account" field of the registration request when calling the registration API. Only one account alias is allowed for a device, but a maximum of 15 devices are allowed under an alias. | No |
| ticket | Ticket in login status | No |
| ticketType | Ticket type | |
| qua | Qzone-specific field | No |

**Example**

```java
XGPushManager.registerPush(this, "UserAccount", "ticket", 1, null,
new XGIOperateCallback() {
@Override
public void onSuccess(Object data, int flag) {
Log.d("TPush", "Registered successfully. Device token is:" + data);
}

@Override
public void onFail(Object data, int errCode, String msg) {
Log.d("TPush", "Registration failed, error code:" + errCode + ",error message:" + msg);
}
});
```

## Obtaining Registration Result
You can obtain the registration result in either of the following two ways.

### Using the registration API with callback
The XGIOperateCallback class provides the API to process successful or failed registrations. For more information, please see the example in [Registration API](https://cloud.tencent.com/document/product/548/13950#xgpushmanager-.E5.8A.9F.E8.83.BD.E7.B1.BB).
Definition of XGIOperateCallback:

```
/**
* Operation callback API
*/
public interface XGIOperateCallback {
/**
* Callback when the operation is successful.
* @param data Business data generated for a successful operation, such as the token returned for a successful registration.
* @param flag Flag code
*/
public void onSuccess(Object data, int flag);
/**
* Callback when the operation fails
* @param data Business data generated for a failed operation
* @param errCode Error code
* @param msg Error message
*/
public void onFail(Object data, int errCode, String msg);
}

```

### Overloading XGPushBaseReceiver
You can obtain the registration result by overloading the onRegisterResult method of XGPushBaseReceiver.

>Note:
>The overloaded XGPushBaseReceiver needs to be configured in AndroidManifest.xml. For more information, please see [Message Configuration](https://cloud.tencent.com/document/product/548/13952#.E6.B6.88.E6.81.AF. E9.85.8D.E7.BD.AE).

**Example**

```
/**
* Registration result
*
* @param context
* App's context object
* @param errorCode
* Error code, {@link XGPushBaseReceiver#SUCCESS}: successful; other values: failed
* @param registerMessage
* Registration result is returned
*/
```
The methods provided by XGPushRegisterResult are listed below:

| Method Name | Returned Value | Default | Description |
|-|-|-|-|
| getToken() | String | " " | The device token, i.e. the device's unique ID |
| getAccessId() | long | 0 | Obtain the registered accessId |
| getAccount | String | " " | Obtain the account bound in registration |
| getTicket() | String | " " | Ticket in login status |
| getTicketType() | short | 0 | Ticket type |


## Unregistration
When a user has logged out or the App is closed and it is no longer necessary to receive the pushed messages, the device can be unregistered from the App (Note: once the device is unregistered, the delivered messages will not be received by the device until it is successfully re-registered.)
>Note:
>Please avoid too frequent unregistration, which may cause the delay of synchronization at backend.
>Unregistration is not required for account switching. The last account will be registered by default if you attempt to register multiple accounts.

**Prototype**
```
public static void unregisterPush(Context context)
```
**Parameters**

| Name | Description |
|-|-|
| context | App's context object |
**Example**
```
XGPushManager.unregisterPush(this);
```
### Unregistration Result
You can obtain the unregistration result by overloading the onUnregisterResult method of XGPushBaseReceiver.
**Example**
```
* Unregistration result
*
* @param context
* App's context object
* @param errorCode
* Error code, {@link XGPushBaseReceiver#SUCCESS}: successful; other values: failed
*/
@Override
public void onUnregisterResult(Context context, int errorCode) {

}
```

