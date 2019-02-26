## Preset Tags
Preset tags are automatically reported in the SDK. XGPush provides three types of preset tags:
- Geographic locations (provincial level)
- App versions
- Churned users (3 or 7 days)

## Setting Tags
Developers can set tags for different users and then send bulk notifications to the tagged user group at frontend. A maximum of 10,000 tags are allowed for an App, and each token can have a maximum of 100 tags under one App. A tag cannot contain any space.

**Prototype**

```
public static void setTag(Context context, String tagName)
```

**Parameters**

| Name | Description |
|-|-|
| context | Context object |
| tagName | The tag name to be set. It cannot be null or empty. |

**Result**
You can obtain the result by overloading the onSetTagResult method of XGPushBaseReceiver.

**Example**

```
XGPushManager.setTag(this, "male");
```

## Deleting Tags
The developer deletes a user tag.

**Prototype**

```
public static void deleteTag(Context context, String tagName)
```

**Parameters**

| Name | Description |
|-|-|
| context | Context object |
| tagName | The tag name to be deleted. It cannot be null or empty. |

**Result**
You can obtain the result by overloading the onDeleteTagResult method of XGPushBaseReceiver.

**Example**

```
XGPushManager.deleteTag (this, "male");
```

