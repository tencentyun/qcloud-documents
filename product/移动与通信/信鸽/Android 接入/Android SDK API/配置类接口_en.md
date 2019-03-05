All configuration related APIs are in the XGPushConfig class. To make the configuration take effect in time, developers need to ensure that the configuration API is called before the launch of or registration with XGPush.
## debug mode
**Note:** To ensure the security of your data, make sure that the debug mode is disabled before publishing.

**Prototype**

```
public static void enableDebug(Context context, boolean debugMode)
```

**Parameters**

| Name | Description |
|-|-|
| context | App's context object |
| debugMode |The default is false. To enable the debug log, set it to true |

## Obtaining Token
A token (also known as MID: Mobile ID) is the ID of a device. It is generated randomly and delivered by the server to the local device based on the device's attributes. All the Apps using the XGPush or MTA (Mobile Tencent Analytics) on the same device acquire the same token.
One of the benefits of using tokens is that it eliminates the statistical impact of duplicated IDs of copycat devices and improves accuracy. If you are using the latest version of MTA, the mid obtained via API StatConfig.getMid() of MTA is the same as that obtained via this API.

>Note:
>A token is generated during the first registration, and will remain in the mobile phone. The token always exists regardless of unregistration. For the version 3.0 and above, the token may change in some cases, for example, when the App is uninstalled and then be reinstalled.

**Prototype**

```
public static String getToken(Context context)
```

**Parameters**

| Name | Description |
|-|-|
| context | App's context object |

**Returned Value**
A normal token is returned for a successful operation, and null or "0" is returned for a failed operation.

## Setting Access ID
If it has been configured in AndroidManifest.xml, you do not need to call this API. If both of the APIs are available, this API prevails.

**Prototype**

```
public static boolean setAccessId(Context context, long accessId)
```

**Parameters**

| Name | Description |
|-|-|
| Context | Object |
| accessId | The access ID obtained during the registration at the frontend |

**Returned Value**

true: Successful
false: Failed

>Note:
>The access ID set via this API is also stored in a file.

## Setting AccessKey
If it has been configured in AndroidManifest.xml, you do not need to call this API. If both of the APIs are available, this API prevails.

**Prototype**
```
public static boolean setAccessId(Context context, String accessKey)

```

**Parameters**

| Name | Description |
|-|-|
| Context | Object |
| accessId | The access key obtained during the registration at the frontend |

**Returned Value**

true: Successful
false: Failed

>Note:
>The access ID set via this API is also stored in a file.

