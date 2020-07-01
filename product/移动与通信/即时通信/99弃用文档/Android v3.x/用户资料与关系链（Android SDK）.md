
IM 通讯云提供了**关系链和用户资料托管**，App 开发者使用简单的接口就可实现关系链和用户资料存储功能。另外，为了方便不同用户定制化资料，也提供用户资料和用户关系链的自定义字段（目前此功能为内测功能，可提交工单修改，参考：[新增用户维度的自定义字段](/doc/product/269/云通信配置变更需求工单#.E6.96.B0.E5.A2.9E.E7.94.A8.E6.88.B7.E7.BB.B4.E5.BA.A6.E7.9A.84.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5)。）。

>注：本节所有的接口不论对**独立帐号体系**还是**托管帐号体系**都有有效。 

## 关系链资料介绍

- **用户关系链：**指好友关系，通过接口可以实现加好友、解除好友、获取好友列表等操作。
- **用户资料：**保存用户的信息（如昵称、头像等）。另外，还有一种好友资料只跟好友相关（如备注，分组等）。

## 设置自己的资料

通过 `TIMFriendshipManager` 的 `modifyProfile` 方法可以对自己的资料（如昵称、头像、添加好友选项等）进行修改。

**原型：**

```
/**
 * 修改自己的资料信息
 * @param param 资料修改参数
 * @param cb 回调
 */
public void modifyProfile(@NonNull ModifyUserProfileParam param, @NonNull TIMCallBack cb)
```

**`ModifyUserProfileParam` 的相关接口如下：**

```
/**
 * 设置昵称
 * @param nickname 新昵称（最长 64 字节）
 */
public ModifyUserProfileParam setNickname(@NonNull String nickname)

/**
 * 设置添加好友选项
 * @param allowType 添加好友选项
 */
public ModifyUserProfileParam setAllowType(@NonNull TIMFriendAllowType allowType) 

/**
 * 设置头像图片 URL
 * @param faceUrl 头像图片 URL
 */
public ModifyUserProfileParam setFaceUrl(@NonNull String faceUrl) 

/**
 * 设置地理位置
 * @param location 地理位置
 */
public ModifyUserProfileParam setLocation(@NonNull String location) 

/**
 * 设置个人签名
 * @param selfSignature 个人签名
 */
public ModifyUserProfileParam setSelfSignature(@NonNull String selfSignature) 

/**
 * 设置生日信息
 * @param birthday 生日信息，含义由应用自行定义，只有低 32 位有效
 */
public ModifyUserProfileParam setBirthday(long birthday) 

/**
 * 设置语言信息
 * @param language 语言信息，含义由应用自行定义，只有低 32 位有效
 */
public ModifyUserProfileParam setLanguage(long language) 

/**
 * 设置性别类型
 * @param gender 性别类型，参见{@see TIMFriendGenderType}
 */
public ModifyUserProfileParam setGender(@NonNull TIMFriendGenderType gender) 

/**
 * 设置自定义信息
 * @param customInfo 自定义信息
 */
public ModifyUserProfileParam setCustomInfo(@NonNull Map<String, byte[]> customInfo) 
```

>注：具体使用情况请看下边几个小节的介绍。

### 设置自己的昵称 

可通过 `TIMFriendshipManager` 的 `modifyProfile` 方法设置用户自己的昵称，昵称最大为 64 字节。 

**示例：** 

```
//初始化参数，修改昵称为“cat”
TIMFriendshipManager.ModifyUserProfileParam param = new TIMFriendshipManager.ModifyUserProfileParam();
param.setNickname("cat");

TIMFriendshipManager.getInstance().modifyProfile(param, new TIMCallBack() {
	@Override
	public void onError(int code, String desc) {
		//错误码 code 和错误描述 desc，可用于定位请求失败原因
		//错误码 code 列表请参见错误码表
		Log.e(tag, "modifyProfile failed: " + code + " desc" + desc);
	}

	@Override
	public void onSuccess() {
		Log.e(tag, "modifyProfile succ");
	}
});
```

### 设置好友验证方式 

可通过 `TIMFriendshipManager` 的 `modifyProfile` 方法设置好友验证方式。用户可根据需要设置其中一种，**目前没有方法设置默认的好友验证方式，默认都是允许任何人添加好友**。有以下几种验证方式：

- **允许任何人添加好友**
- **拒绝任何人添加好友**
- **添加好友需要验证**

好友验证方式通过 ImSDK 中的 `TIMFriendAllowType` 来定义，具体定义如下。

```
//允许任何人添加好友
TIM_FRIEND_ALLOW_ANY

//拒绝任何人添加好友
TIM_FRIEND_DENY_ANY

//非法的选项类型
TIM_FRIEND_INVALID

//添加好友需要验证
TIM_FRIEND_NEED_CONFIRM
```


以下示例中设置了自己的好友验证方式为需要验证，此时如果有用户申请加好友，会收到加好友的系统通知（详见 [关系链变更系统通知](/doc/product/269/9231#8.-.E5.85.B3.E7.B3.BB.E9.93.BE.E5.8F.98.E6.9B.B4.E7.B3.BB.E7.BB.9F.E9.80.9A.E7.9F.A5)）。

**示例：**

```
//设置自己的好友验证方式为需要验证
TIMFriendshipManager.ModifyUserProfileParam param = new TIMFriendshipManager.ModifyUserProfileParam();
param.setAllowType(TIMFriendAllowType.TIM_FRIEND_NEED_CONFIRM);

TIMFriendshipManager.getInstance().modifyProfile(param, new TIMCallBack() {
	@Override
	public void onError(int code, String desc) {
		//错误码 code 和错误描述 desc，可用于定位请求失败原因
		//错误码 code 列表请参见错误码表
		Log.e(tag, "modifyProfile failed: " + code + " desc" + desc);
	}

	@Override
	public void onSuccess() {
		Log.e(tag, "modifyProfile succ");
	}
});
```


### 设置自己的头像

可通过 `TIMFriendshipManager` 的 `modifyProfile` 方法设置用户自己的头像，当前 ImSDK 不会保存用户图片资源，需要用户上传图片到其他存储平台，通过 ImSDK 设置图片 URL。 

**示例：**

```
TIMFriendshipManager.ModifyUserProfileParam param = new TIMFriendshipManager.ModifyUserProfileParam();
param.setFaceUrl( "http://faceurl");

TIMFriendshipManager.getInstance().modifyProfile(param, new TIMCallBack() {
	@Override
	public void onError(int code, String desc) {
		//错误码 code 和错误描述 desc，可用于定位请求失败原因
		//错误码 code 列表请参见错误码表
		Log.e(tag, "modifyProfile failed: " + code + " desc" + desc);
	}

	@Override
	public void onSuccess() {
		Log.e(tag, "modifyProfile succ");
	}
});
```

### 设置自己的自定义字段

通过 Server 配置（可提交工单修改，可参考：[新增用户维度的自定义字段](/doc/product/269/云通信配置变更需求工单#.E6.96.B0.E5.A2.9E.E7.94.A8.E6.88.B7.E7.BB.B4.E5.BA.A6.E7.9A.84.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5)）可以设置自己的自定义字段，通过自定义字段可以做到很多非内置功能，如用户等级等。

**示例：**

```
Map<String, byte[]> customInfos = new HashMap<String, byte[]>();
try {
	customInfos.put("Tag_Profile_Custom_Test", "test".getBytes("utf-8"));
} catch (UnsupportedEncodingException e) {
	e.printStackTrace();
}

TIMFriendshipManager.ModifyUserProfileParam param = new TIMFriendshipManager.ModifyUserProfileParam();
param.setCustomInfo(customInfos);

TIMFriendshipManager.getInstance().modifyProfile(param, new TIMCallBack() {
	@Override
	public void onError(int code, String desc) {
		//错误码 code 和错误描述 desc，可用于定位请求失败原因
		//错误码 code 列表请参见错误码表
		Log.e(tag, "modifyProfile failed: " + code + " desc" + desc);
	}

	@Override
	public void onSuccess() {
		Log.e(tag, "modifyProfile succ");
	}
});
```

### 设置自己的个性签名

云通信支持个性签名，用户设置后所有人可见。

**示例：**

```
TIMFriendshipManager.ModifyUserProfileParam param = new TIMFriendshipManager.ModifyUserProfileParam();
param.setSelfSignature("stay hungry, stay foolish");

TIMFriendshipManager.getInstance().modifyProfile(param, new TIMCallBack() {
	@Override
	public void onError(int code, String desc) {
		//错误码 code 和错误描述 desc，可用于定位请求失败原因
		//错误码 code 列表请参见错误码表
		Log.e(tag, "modifyProfile failed: " + code + " desc" + desc);
	}

	@Override
	public void onSuccess() {
		Log.e(tag, "modifyProfile succ");
	}
});
```

### 设置自己的性别

云通信支持设置自己的性别，设置后所有人可见。

**示例：**

```
TIMFriendshipManager.ModifyUserProfileParam param = new TIMFriendshipManager.ModifyUserProfileParam();
param.setGender(TIMFriendGenderType.Female);

TIMFriendshipManager.getInstance().modifyProfile(param, new TIMCallBack() {
	@Override
	public void onError(int code, String desc) {
		//错误码 code 和错误描述 desc，可用于定位请求失败原因
		//错误码 code 列表请参见错误码表
		Log.e(tag, "modifyProfile failed: " + code + " desc" + desc);
	}

	@Override
	public void onSuccess() {
		Log.e(tag, "modifyProfile succ");
	}
});
```

### 设置自己的生日

云通信支持设置自己的生日，设置后所有人可见。

> **注意:**
> 生日信息是一个长整形，结果只保留低 32 位，具体含义由应用自行定义和解析。

**示例：**

```
TIMFriendshipManager.ModifyUserProfileParam param = new TIMFriendshipManager.ModifyUserProfileParam();
//生日设置为 2017/5/2
param.setBirthday(1493654400);

TIMFriendshipManager.getInstance().modifyProfile(param, new TIMCallBack() {
	@Override
	public void onError(int code, String desc) {
		//错误码 code 和错误描述 desc，可用于定位请求失败原因
		//错误码 code 列表请参见错误码表
		Log.e(tag, "modifyProfile failed: " + code + " desc" + desc);
	}

	@Override
	public void onSuccess() {
		Log.e(tag, "modifyProfile succ");
	}
});
```

### 设置自己的语言

云通信支持设置自己的语言，设置后所有人可见。

> **注意：**
> 语言信息是一个长整形，结果只保留低 32 位，具体含义由应用自行定义和解析。

**示例：**

```
TIMFriendshipManager.ModifyUserProfileParam param = new TIMFriendshipManager.ModifyUserProfileParam();
//这里假设 1 表示中文
param.setLanguage(1);

TIMFriendshipManager.getInstance().modifyProfile(param, new TIMCallBack() {
	@Override
	public void onError(int code, String desc) {
		//错误码 code 和错误描述 desc，可用于定位请求失败原因
		//错误码 code 列表请参见错误码表
		Log.e(tag, "modifyProfile failed: " + code + " desc" + desc);
	}

	@Override
	public void onSuccess() {
		Log.e(tag, "modifyProfile succ");
	}
});
```

### 设置自己的位置

云通信支持设置自己的位置，设置后所有人可见。

**示例：**

```
TIMFriendshipManager.ModifyUserProfileParam param = new TIMFriendshipManager.ModifyUserProfileParam();
param.setLocation("location");

TIMFriendshipManager.getInstance().modifyProfile(param, new TIMCallBack() {
	@Override
	public void onError(int code, String desc) {
		//错误码 code 和错误描述 desc，可用于定位请求失败原因
		//错误码 code 列表请参见错误码表
		Log.e(tag, "modifyProfile failed: " + code + " desc" + desc);
	}

	@Override
	public void onSuccess() {
		Log.e(tag, "modifyProfile succ");
	}
});
```

## 获取资料

### 获取自己的资料 

可通过 `TIMFriendshipManager` 的 `getSelfProfile` 方法获取用户自己的资料，默认只拉取基本资料，如果只需要个别字段或者自定义字段，可以使用 [按照字段获取用户资料](#.E6.8C.89.E7.85.A7.E5.AD.97.E6.AE.B5.E8.8E.B7.E5.8F.96.E7.94.A8.E6.88.B7.E8.B5.84.E6.96.99) 方法设置，此方法全局有效。

**原型：**

```   
/**
 * 获取自己的基本资料
 * @param cb 回调，OnSuccess 函数的参数中返回包含相应自己的{@see TIMUserProfile}
 */
public void getSelfProfile(final @NonNull TIMValueCallBack<TIMUserProfile> cb)
```

**`TIMUserProfile` 提供的接口如下：**

```
/**
* 获取用户的 identifier
* @return 用户的 identifier
*/
public String getIdentifier()

/**
* 获取用户的昵称
* @return 用户的昵称
*/
public String getNickName()

/**
* 获取用户头像 URL
* @return 用户头像 URL
*/
public String getFaceUrl()

/**
* 获取用户个人签名
* @return 用户个人签名
*/
public String getSelfSignature()

/**
* 获取用户加好友的选项
* @return 用户好友选项
*/
public TIMFriendAllowType getAllowType()

/**
* 获取用户备注
* @return 用户备注
*/
public String getRemark()

/**
* 获取被加入的好友分组列表
* @return 分组列表
*/
public List<String> getFriendGroups()

/**
* 获取用户自定义信息
* @return 自定义信息 Map
*/
public Map<String, byte[]> getCustomInfo()

/**
* 获取用户性别类型
* @return 用户性别类型
 */
public TIMFriendGenderType getGender()

/**
* 获取用户生日信息
* @return 生日信息
 */
public long getBirthday()

/**
* 获取语言
* @return 语言
 */
public long getLanguage()

/**
* 获取位置信息
* @return 位置信息
 */
public String getLocation()
```

**示例： **

```
//获取自己的资料
TIMFriendshipManager.getInstance().getSelfProfile(new TIMValueCallBack<TIMUserProfile>(){
	@Override
	public void onError(int code, String desc){
		//错误码 code 和错误描述 desc，可用于定位请求失败原因
		//错误码 code 列表请参见错误码表
        Log.e(tag, "getSelfProfile failed: " + code + " desc");
	}
	
	@Override
	public void onSuccess(TIMUserProfile result){
		Log.e(tag, "getSelfProfile succ");
		Log.e(tag, "identifier: " + result.getIdentifier() + " nickName: " + result.getNickName() 
					+ " remark: " + result.getRemark() + " allow: " + result.getAllowType());
	}
});
```

### 获取任何人的资料

可通过 `TIMFriendshipManager` 的 `getUsersProfile` 方法获取任何人的资料，默认只拉取基本资料，如果只需要个别字段或者自定义字段，可以使用 [按照字段获取用户资料](#.E6.8C.89.E7.85.A7.E5.AD.97.E6.AE.B5.E8.8E.B7.E5.8F.96.E7.94.A8.E6.88.B7.E8.B5.84.E6.96.99) 方法设置，此方法全局有效。此接口从网络获取数据。

**原型： **  

```
/**
 * 获取用户基本资料（不包括：备注，好友分组）
 * @param users 要获取资料的用户 identifier 列表
 * @param cb 回调，OnSuccess 函数的参数中返回包含相应用户的{@see TIMUserProfile}列表
 */
public void getUsersProfile(@NonNull List<String> users, @NonNull TIMValueCallBack<List<TIMUserProfile>> cb) 
```

**示例：**

```
//待获取用户资料的用户列表
List<String> users = new ArrayList<String>();
users.add("sample_user_1");
users.add("sample_user_2");

//获取用户资料
TIMFriendshipManager.getInstance().getUsersProfile(users, new TIMValueCallBack<List<TIMUserProfile>>(){
	@Override
	public void onError(int code, String desc){
		//错误码 code 和错误描述 desc，可用于定位请求失败原因
		//错误码 code 列表请参见错误码表
        Log.e(tag, "getUsersProfile failed: " + code + " desc");
	}
	
	@Override
	public void onSuccess(List<TIMUserProfile> result){
        Log.e(tag, "getUsersProfile succ");
		for(TIMUserProfile res : result){
	        Log.e(tag, "identifier: " + res.getIdentifier() + " nickName: " + res.getNickName() 
	        		+ " remark: " + res.getRemark());
		}
	}
});
```

### 获取好友的资料

好友关系链的功能是由资料关系链扩展包提供的，可通过 扩展包中 `TIMFriendshipManagerExt` 的 `getFriendsProfile` 方法获取好友的资料，默认只拉取基本资料，如果只需要个别字段或者自定义字段，可以使用 [按照字段获取用户资料](#.E6.8C.89.E7.85.A7.E5.AD.97.E6.AE.B5.E8.8E.B7.E5.8F.96.E7.94.A8.E6.88.B7.E8.B5.84.E6.96.99) 方法设置，此方法全局有效。此接口从网络获取数据。

**原型： **  

```
/**
 * 获取好友的资料（仅好友）
 * @param users 要获取资料的好友 identifier 列表
 * @param cb 回调，OnSuccess 函数的参数中返回包含相应用户的{@see TIMUserProfile}列表
 */
public void getFriendsProfile(@NonNull List<String> users, @NonNull TIMValueCallBack<List<TIMUserProfile>> cb)
```

**示例：**

```
//待获取用户资料的好友列表
List<String> users = new ArrayList<String>();
users.add("sample_friend_1");
users.add("sample_friend_2");

//获取好友资料
TIMFriendshipManagerExt.getInstance().getFriendsProfile(users, new TIMValueCallBack<List<TIMUserProfile>>(){
	@Override
	public void onError(int code, String desc){
		//错误码 code 和错误描述 desc，可用于定位请求失败原因
		//错误码 code 列表请参见错误码表
        Log.e(tag, "getFriendsProfile failed: " + code + " desc");
	}
	
	@Override
	public void onSuccess(List<TIMUserProfile> result){
        Log.e(tag, "getFriendsProfile succ");
		for(TIMUserProfile res : result){
	        Log.e(tag, "identifier: " + res.getIdentifier() + " nickName: " + res.getNickName() 
	        		+ " remark: " + res.getRemark());
		}
	}
});
```



### 按照字段获取用户资料

目前 ImSDK 在获取用户资料的时候，**默认会获取所有基本字段，且不会拉取自定义字段**。如果需要只拉取其中某些字段，或者需要拉取自定义字段，需要在**登录 ImSDK 之前**，通过 `TIMFriendshipSettings` 进行相应的设置，并通过 `TIMManager` 的 `setUserConfig` 将其也当前通信管理器进行关联(参考 [用户配置](/doc/product/269/9229#.E7.94.A8.E6.88.B7.E9.85.8D.E7.BD.AE9))。

**`TIMFriendshipSettings` 提供的相关接口如下：**

```
/**
 * 设置关系链默认拉取资料标识
 * @param flags 拉取资料标识, 参见{@see TIMFriendshipManager#TIM_PROFILE_FLAG_NICK}等
 */
public void setFlags(long flags)

/**
 * 设置自定义资料标签
 * @param tags 自定义资料标签
 */
public void setCustomTags(List<String> tags)

/**
 * 添加单个自定义资料标签
 * @param tag 自定义资料标签
 */
public void addCustomTag(String tag)
```

**示例：**

```
//设置资料关系链拉取字段，这里只关心好友验证类型、头像 URL、昵称和自定义字段"Tag_Profile_Custom_Test"
TIMFriendshipSettings settings = new TIMFriendshipSettings();
long flags = 0;
flags |= TIMFriendshipManager.TIM_PROFILE_FLAG_ALLOW_TYPE
		| TIMFriendshipManager.TIM_PROFILE_FLAG_FACE_URL
		| TIMFriendshipManager.TIM_PROFILE_FLAG_NICK;
settings.setFlags(flags);
settings.addCustomTag("Tag_Profile_Custom_Test");

TIMUserConfig config = new TIMUserConfig();
config.setFriendshipSettings(settings);

//将用户配置与当前通信管理器关联
TIMManager.getInstance().setUserConfig(config);
```

## 关系链相关资料

好友关系链的功能是由资料关系链扩展包提供的，所以所有关系链相关的操作全部由扩展包中的 `TIMFriendshipManagerExt` 实例提供。可以通过 `TIMFriendshipManagerExt` 中的 `modifySnsProfile` 方法修改好友关系链相关资料（如好友备注、好友自定义资料）。

**原型：**

```
/**
 * 修改好友关系链资料
 * @param param 修改参数
 * @param cb 回调
 */
public void modifySnsProfile(@NonNull ModifySnsProfileParam param, @NonNull TIMCallBack cb)
```

**`ModifySnsProfileParam` 提供的接口如下：**

```
/**
 * 构造参数实例
 * @param identifier 需要修改资料的好友用户 ID
 */
public ModifySnsProfileParam(@NonNull String identifier)

/**
 * 设置好友备注
 * @param remark 备注内容
 */
public ModifySnsProfileParam setRemark(String remark)

/**
 * 设置关系链资料自定义字段
 * @param customInfo 自定义字段键值对
 */
public ModifySnsProfileParam setCustomInfo(Map<String, byte[]> customInfo) 
```

### 好友备注 

可通过 `TIMFriendshipManagerExt` 的 `modifySnsProfile` 方法设置好友备注。

> **注意：**
> 好友备注必须先加为好友才可设置备注。

**示例：**

```
//将好友“test_user”的备注设置为“remark”
TIMFriendshipManagerExt.ModifySnsProfileParam param = new TIMFriendshipManagerExt.ModifySnsProfileParam("test_user");
param.setRemark("remark");

TIMFriendshipManagerExt.getInstance().modifySnsProfile(param, new TIMCallBack() {
	@Override
	public void onError(int code, String desc) {
		//错误码 code 和错误描述 desc，可用于定位请求失败原因
		//错误码 code 列表请参见错误码表
		Log.e(tag, "modifySnsProfile failed: " + code + " desc" + desc);
	}

	@Override
	public void onSuccess() {
		Log.e(tag, "modifySnsProfile succ");
	}
});
```

### 设置好友自定义资料

通过 Server 配置（内测功能）可以设置自己的自定义字段，通过自定义字段可以做到很多非内置功能。

**示例：**

```
//将好友“test_user”的好友自定义资料字段“Tag_SNS_Custom_Test”设置为“test”
TIMFriendshipManagerExt.ModifySnsProfileParam param = new TIMFriendshipManagerExt.ModifySnsProfileParam("test_user");

Map<String, byte[]> customInfos = new HashMap<String, byte[]>();
try {
	customInfos.put("Tag_SNS_Custom_Test", "test".getBytes("utf-8"));
} catch (UnsupportedEncodingException e) {
	e.printStackTrace();
}
param.setCustomInfo(customInfos);

TIMFriendshipManagerExt.getInstance().modifySnsProfile(param, new TIMCallBack() {
	@Override
	public void onError(int code, String desc) {
		//错误码 code 和错误描述 desc，可用于定位请求失败原因
		//错误码 code 列表请参见错误码表
		Log.e(tag, "modifySnsProfile failed: " + code + " desc" + desc);
	}

	@Override
	public void onSuccess() {
		Log.e(tag, "modifySnsProfile succ");
	}
});
```

## 好友关系

好友关系链是由资料关系链扩展包提供的功能，所以所有关系链相关操作均由 `TIMFriendshipManagerExt` 提供。

### 添加好友

通过 `TIMFriendshipManagerExt` 的 `addFriend` 方法可以批量添加好友，目前所能支持的最大好友列表为3000个。

**原型：   **

```
/**
 * 添加好友
 * @param users 要添加的用户列表 TIMAddFriendRequest 列表
 * @param cb 回调, onSuccess 函数的参数中返回{@see TIMFriendResult}列表
 */
public void addFriend(@NonNull List<TIMAddFriendRequest> users,
					  @NonNull TIMValueCallBack<List<TIMFriendResult>> cb)
```

**`TIMAddFriendRequest` 提供的接口方法如下： **

```
/**
 * 构造添加好友请求
 * @param id 要添加的好友的 ID
 */
public TIMAddFriendRequest(@NonNull String id)

/**
 * 获取好友分组名称
 * @return 好友分组名称
 */
public String getFriendGroup()

/**
 * 设置好友分组名称
 * @param groupName 好友分组名称
 */
public TIMAddFriendRequest setFriendGroup(@NonNull String groupName)

/**
 * 获取添加好友的 identifier
 * @return identifier
 */
public String getIdentifier()

/**
 * 设置添加好友的 identifier
 * @param identifier 要添加的好友的 identifier
 */
public TIMAddFriendRequest setIdentifier(@NonNull String identifier)

/**
 * 获取添加好友的备注
 * @return 好友备注
 */
public String getRemark()

/**
 * 设置要添加好友的备注
 * @param remark 要添加的好友的备注（最长 96 字节）
 */
public TIMAddFriendRequest setRemark(@NonNull String remark)

/**
 * 获取要添加好友的添加来源
 * @return 添加来源
 */
public String getAddSource()

/**
 * 设置添加好友的添加来源
 * @param addSource 要添加好友的添加来源
 */
public TIMAddFriendRequest setAddrSource(@NonNull String addSource)

/**
 * 获取添加好友的申请理由
 * @return 申请理由（120 字节）
 */
public String getAddWording()

/**
 * 设置添加好友的申请理由
 * @param addWording 添加好友时的申请理由
 */
public TIMAddFriendRequest setAddWording(@NonNull String addWording)
```

**`TIMFriendResult` 的接口方法如下：**

```
/**
 * 获取用户 identifier
 * @return 用户 identifier
 */
public String getIdentifer()

/**
 * 获取操作结果 status
 * @return 操作结果的 status
 */
public TIMFriendStatus getStatus()
```

**`TIMFriendStatus` 定义如下：**

```
//对方已经是好友
TIM_FRIEND_STATUS_EXISTED_FRIEND

//未知错误
TIM_FRIEND_STATUS_FAILED

//等待好友审核通过
TIM_FRIEND_STATUS_PENDING

//操作成功
TIM_FRIEND_STATUS_SUCC

//找不到相应用户信息
TIM_FRIEND_STATUS_USER_NOT_FOUND
```

开发者可根据对应情况提示用户。 

**示例：**

```
//创建请求列表
List<TIMAddFriendRequest> reqList = new ArrayList<TIMAddFriendRequest>();

//添加好友请求
TIMAddFriendRequest req = new TIMAddFriendRequest("sample_user_1");
req.setAddrSource("DemoApp");
req.setAddWording("add me");
req.setRemark("Cat");

reqList.add(req);
            	   
//申请添加好友
TIMFriendshipManagerExt.getInstance().addFriend(reqList, new TIMValueCallBack<List<TIMFriendResult>>() {
	@Override
	public void onError(int code, String desc){
		//错误码 code 和错误描述 desc，可用于定位请求失败原因
		//错误码 code 列表请参见错误码表
		Log.e(tag, "addFriend failed: " + code + " desc");
	}
	
	@Override
	public void onSuccess(List<TIMFriendResult> result){
        Log.e(tag, "addFriend succ");
		for(TIMFriendResult res : result){
	        Log.e(tag, "identifier: " + res.getIdentifer() + " status: " + res.getStatus());
		}
	}
});
```

### 删除好友 

可通过 `TIMFriendshipManagerExt` 的 `delFriend` 方法可以批量删除好友。

**原型：**      

```
/**
 * 删除好友
 * @param param 删除好友参数 {@see DeleteFriendParam}
 * @param cb 回调, onSuccess函数的参数中返回{@see TIMFriendResult}列表
 */
public void delFriend(@NonNull DeleteFriendParam param,
					  @NonNull TIMValueCallBack<List<TIMFriendResult>> cb)
```

**`DeleteFriendParam` 提供的接口如下：**

```
/**
 * 设置删除好友类型
 * @param type 删除好友类型（单向、双向）
 */
public DeleteFriendParam setType(@NonNull TIMDelFriendType type)

/**
 * 设置要删除的好友 ID 列表
 * @param users 好友 ID 列表
 */
public DeleteFriendParam setUsers(@NonNull List<String> users) 
```

**示例：**

```
//双向删除好友 test_user
TIMFriendshipManagerExt.DeleteFriendParam param = new TIMFriendshipManagerExt.DeleteFriendParam();
param.setType(TIMDelFriendType.TIM_FRIEND_DEL_BOTH)
		.setUsers(Collections.singletonList("test_user"));

TIMFriendshipManagerExt.getInstance().delFriend(param, new TIMValueCallBack<List<TIMFriendResult>>() {
	@Override
	public void onError(int code, String desc) {
		//错误码 code 和错误描述 desc，可用于定位请求失败原因
		//错误码 code 列表请参见错误码表
		Log.e(tag, "delFriend failed: " + code + " desc");
	}

	@Override
	public void onSuccess(List<TIMFriendResult> timFriendResults) {
		Log.d(tag, "delFriend succ");
		for(TIMFriendResult result : timFriendResults){
			Log.d(tag, "result id: " + result.getIdentifer() + "|status: " + result.getStatus());
		}

	}
});
```

### 获取所有好友 

可通过 `TIMFriendshipManagerExt` 的 `getFriendList` 方法可以获取所有好友，默认只拉取基本资料，如果只需要个别字段或者自定义字段，可以使用 [按照字段获取用户资料](#.E6.8C.89.E7.85.A7.E5.AD.97.E6.AE.B5.E8.8E.B7.E5.8F.96.E7.94.A8.E6.88.B7.E8.B5.84.E6.96.99) 方法设置，此方法全局有效。

**原型： **   

```
/**
 * 获取所有好友
 * @param cb 回调，OnSuccess 函数的参数中返回所有好友的{@see TIMUserProfile}列表,只包含 identifier，nickname，remark 三个字段
 */
public void getFriendList(@NonNull TIMValueCallBack<List<TIMUserProfile>> cb)
```
 
**示例：**

```
//获取好友列表
TIMFriendshipManagerExt.getInstance().getFriendList(new TIMValueCallBack<List<TIMUserProfile>>(){
    @Override
    public void onError(int code, String desc){
        //错误码 code 和错误描述 desc，可用于定位请求失败原因
        //错误码 code 列表请参见错误码表
        Log.e(tag, "getFriendList failed: " + code + " desc");
    }
    
    @Override
    public void onSuccess(List<TIMUserProfile> result){
        for(TIMUserProfile res : result){
            Log.e(tag, "identifier: " + res.getIdentifier() + " nickName: " + res.getNickName() 
                    + " remark: " + res.getRemark());
        }
    }
});
```

### 同意/拒绝 好友申请 

可通过 `TIMFriendshipManagerExt` 的 `addFriendResponse` 方法可以对未决好友添加申请进行回应。

**原型：**

```
/**
 * 对未决的好友申请进行回应
 * @param response 回应内容
 * @param cb 回调, onSuccess 函数的参数中返回{@see TIMFriendResult}列表
 */
public void addFriendResponse(@NonNull TIMFriendAddResponse response,
							  @NonNull TIMValueCallBack<TIMFriendResult> cb) 
```

** `TIMFriendAddResponse` 提供的成员方法如下：**

```
/**
 * 构造好友申请回应实例
 * @param identifier 好友用户 ID
 */
public TIMFriendAddResponse(@NonNull String identifier)

/**
 * 设置好友备注
 * @param remark 备注内容
 */
public void setRemark(String remark)

/**
 * 设置回应方式（同意还是拒绝）
 * @param type 回应方式
 */
public void setType(TIMFriendResponseType type)
```

**`TIMFriendResponseType` 的定义如下：**

```
//同意对方的好友申请
Agree

//同意对方的好友申请，并添加对方为好友
AgreeAndAdd

//拒绝对方的好友申请
Reject
```

### 添加用户到黑名单

可以通过 `TIMFriendshipManagerExt` 中的 `addBlackList` 方法把任意用户拉黑，如果此前是好友关系，**拉黑后自动解除好友，拉黑后将无法收到对方发送的消息**。

**原型：**

```
/**
 * 添加用户到黑名单
 * @param identifiers 要添加到黑名单的用户列表
 * @param cb 回调, onSuccess 函数的参数中返回{@see TIMFriendResult}列表
 */
public void addBlackList(@NonNull List<String> identifiers,
						 @NonNull TIMValueCallBack<List<TIMFriendResult>> cb) 
```

### 把用户从黑名单删除

相应的通过 `TIMFriendshipManagerExt` 中的 `delBlackList` 方法可以把用户从黑名单中移除。

> **注意：**
> 把用户从黑名单中移出后，不会主动恢复好友关系，需要应用重新添加好友关系。

**原型：**

```
/**
 * 将用户从黑名单中删除
 * @param identifiers 要从黑名单中删除的用户列表
 * @param cb 回调, onSuccess函数的参数中返回{@see TIMFriendResult}列表
 */
public void delBlackList(@NonNull List<String> identifiers,
						 @NonNull TIMValueCallBack<List<TIMFriendResult>> cb)
```

### 获取黑名单列表

通过 `TIMFriendshipManagerExt` 中的 `getBlackList` 方法获取当前黑名单列表。

**原型：**
```
/**
 * 获取黑名单列表
 * @param cb 回调, onSuccess 函数的参数中返回黑名单用户 identifier 列表
 */
public void getBlackList(@NonNull TIMValueCallBack<List<String>> cb) 
```

## 好友分组

**好友分组**是由资料关系链扩展包提供的功能，所以所有好友分组相关操作均由 `TIMFriendshipManagerExt` 提供。

### 创建好友分组

通过 `TIMFriendshipManagerExt` 的接口 `createFriendGroup` 可以创建好友分组。创建分组时，可以同时指定添加的用户，同一用户可以添加到多个分组。

**原型：**
```
/**
 * 新建好友分组
 * @param groupNames 分组名称列表，必须是当前不存在的分组
 * @param users 要添加到分组中的好友列表
 * @param cb 回调，在 onSuccess 回调的参数中返回请求结果{@see TIMFriendResult}列表
 */
public void createFriendGroup(@NonNull List<String> groupNames, @NonNull List<String> users,
							  @NonNull TIMValueCallBack<List<TIMFriendResult>> cb)
```

### 删除好友分组

通过 `TIMFriendshipManagerExt` 的接口 `deleteFriendGroup` 可以删除好友分组。

**原型：**

```
/**
 * 删除好友分组
 * @param groupNames 要删除的好友分组名称列表
 * @param cb 回调
 */
public void deleteFriendGroup(@NonNull List<String> groupNames, @NonNull TIMCallBack cb)
```

### 添加好友到某分组

通过 `TIMFriendshipManagerExt` 的接口 `addFriendsToFriendGroup` 可以将好友添加到好友分组。

**原型：**
```
/**
 * 添加好友到一个好友分组
 * @param groupName 好友分组名称
 * @param users 要加到好友分组的好友列表
 * @param cb 回调，在 onSuccess 回调的参数中返回请求结果{@see TIMFriendResult}列表
 */
public void addFriendsToFriendGroup(@NonNull String groupName, @NonNull List<String> users,
									@NonNull TIMValueCallBack<List<TIMFriendResult>> cb)
```

### 从某分组删除好友

通过 `TIMFriendshipManagerExt` 的接口 `delFriendsFromFriendGroup` 可以将好友从好友分组中删除。

**原型：**

```
/**
 * 从好友分组中删除好友
 * @param groupName 好友分组名称
 * @param users 要从好友分组中删除的好友列表
 * @param cb 回调，在 onSuccess 回调的参数中返回请求结果{@see TIMFriendResult}列表
 */
public void delFriendsFromFriendGroup(@NonNull String groupName, @NonNull List<String> users,
									  @NonNull TIMValueCallBack<List<TIMFriendResult>> cb)
```

### 重命名好友分组

通过 `TIMFriendshipManagerExt` 的接口 `renameFriendGroupName` 可以重命名好友分组。

**原型：**

```
/**
 * 修改好友分组的名称
 * @param oldName 原来的分组名称
 * @param newName 要修改成的分组名称
 * @param cb 回调
 */
public void renameFriendGroupName(@NonNull String oldName, @NonNull String newName,
								  @NonNull final TIMCallBack cb)
```

### 获取指定的好友分组信息

通过 `TIMFriendshipManagerExt` 的接口 `getFriendGroups` 可以获取指定的好友分组。

**原型：**

```
/**
 * 获取指定的好友分组信息
 * @param groupNames 要获取信息的好友分组名称列表, 为 null 则获取所有的好友分组信息
 * @param cb 回调，在 onSuccess 回调的参数中返回好友分组列表，详见{@see TIMFriendGroup}
 */
public void getFriendGroups(@Nullable List<String> groupNames,
							@NonNull TIMValueCallBack<List<TIMFriendGroup>> cb)
```

### 获取所有好友分组

通过 [获取指定的好友分组信息](#.E8.8E.B7.E5.8F.96.E6.8C.87.E5.AE.9A.E7.9A.84.E5.A5.BD.E5.8F.8B.E5.88.86.E7.BB.84.E4.BF.A1.E6.81.AF) 可以获取所有分组信息，另外，通过 [获取所有好友](#.E8.8E.B7.E5.8F.96.E6.89.80.E6.9C.89.E5.A5.BD.E5.8F.8B) 也可以获取分组信息。

## 关系链资料存储

### 开启存储

默认情况下，ImSDK 不会对关系链资料数据进行存储，如果需要开启关系链资料存储，请在**登录前**，通过 `TIMUserConfigSnsExt` 进行相应的配置，并通过 `TIMManager` 的 `setUserConfig` 将相关配置与当前通信管理器进行关联。

**`TIMUserConfigSnsExt` 接口定义如下：**

```
/**
 * 扩展类构造函数
 * @param config 用户配置实例
 */
public TIMUserConfigSnsExt(@NonNull TIMUserConfig config)

/**
 * 设置关系链变更事件监听器
 * @param proxyListener 关系链变更事件监听器
 */
public TIMUserConfigSnsExt setFriendshipProxyListener(TIMFriendshipProxyListener proxyListener)

/**
 * 获取关系链变更事件监听器
 * @return 关系链变更事件监听器
 */
public TIMFriendshipProxyListener getFriendshipProxyListener()

/**
 * 是否开启关系链本地储存
 * @return true - 开启， false - 不开启
 */
public boolean isFriendshipStorageEnabled()

/**
 * 设置是否开启关系链本地储存
 * @param friendshipStorageEnabled true - 开启， false - 不开启
 */
public TIMUserConfigSnsExt enableFriendshipStorage(boolean friendshipStorageEnabled)
```

**示例：**

具体例子请参考 [用户配置](/doc/product/269/9229#.E7.94.A8.E6.88.B7.E9.85.8D.E7.BD.AE9)。

### 内存中同步获取关系链资料数据

通过 `TIMFriendshipProxy` 提供的接口可以从内存中同步获取关系链资料数据。

**原型：**
```
/**
 * 获取好友关系链代理实例
 * @return 代理实例
 */
public static TIMFriendshipProxy getInstance()

/**
 * 获取全部好友
 */
public List<TIMUserProfile> getFriends()

/**
 * 获取指定 ID 好友
 * @param identifiers 用户 identify
 */
public List<TIMUserProfile> getFriendsById(List<String> identifiers)

/**
 * 获取指定好友分组，包括好友信息
 * @param groups 指定分组的名称，为空表示获取所有分组
 */
public List<TIMFriendGroup> getFriendsByGroups(@Nullable List<String> groups)
```

### 好友、资料变更回调

如果没有开启关系链资料存储的情况下，必须通过系统消息来感知关系链资料变更，这种方式需要用户解析消息内容，层次结构较深；如果开启了存储的功能，可以用更加明显易用的回调 `TIMFriendshipProxyListener` 感知变更。通过 `TIMUserConfigSnsExt` 进行相应的配置，并通过 `TIMManager` 的 `setUserConfig` 将相关配置与当前通信管理器进行关联。通过设置 `TIMFriendshipProxyListener` 变更回调，可以在发生不同事件的时候感知不同的事件，之后可通过同步接口获取信息并更新 UI 操作。

**`TIMFriendshipProxyListener` 主要的事件回调如下：**

```
/**
 *  添加好友通知
 *  @param users 好友列表，详见{@see TIMUserProfile}
 */
void OnAddFriends(List<TIMUserProfile> users);

/**
 *  删除好友通知
 *  @param identifiers 用户 ID 列表
 */
void OnDelFriends(List<String> identifiers);

/**
 *  好友资料更新通知
 *  @param profiles 资料列表,详见{@see TIMUserProfile}
 */
void OnFriendProfileUpdate(List<TIMUserProfile> profiles);

/**
 *  好友申请通知
 *  @param reqs 好友申请者 ID 列表，详见{@see TIMSNSChangeInfo}
 */
void OnAddFriendReqs(List<TIMSNSChangeInfo> reqs);
```

**示例：**

具体例子请参考 [用户配置](/doc/product/269/9229#.E7.94.A8.E6.88.B7.E9.85.8D.E7.BD.AE9)。

## 关系链变更系统通知 

`TIMMessage` 中 `Elem` 类型为 `TIMElemType.SNSTips` 的消息为关系链变更系统消息，由 `TIMSNSSystemElem` 表示。 

**`TIMSNSSystemElem` 成员接口如下：**

```
/**
 * 获取变更消息类型
 * @return 关系链变更通知消息类型
 */
public TIMSNSSystemType getSubType() 

/**
 * 获取关系链变更消息详细信息列表
 * @return 关系链变更消息详情信息列表
 */
public List<TIMSNSChangeInfo> getChangeInfoList()

/**
 * 未决已读上报时间戳 type == TIMSNSSystemType.TIM_SNS_SYSTEM_PENDENCY_REPORT 时有效
 * @return 未决已读上报时间戳
 */
public long getPendencyReportTimestamp()
void setPendencyReportTimestamp(long pendencyReportTimestamp) {
	this.pendencyReportTimestamp = pendencyReportTimestamp;
}

/**
 * 已决已读上报时间戳 type == TIMSNSSystemType.TIM_SNS_SYSTEM_DECIDE_REPORT 时有效
 * @return 已决已读上报时间戳
 */
public long getDecideReportTimestamp()

/**
 * 推荐已读上报时间戳 type == TIMSNSSystemType.TIM_SNS_SYSTEM_RECOMMEND_REPORT 时有效
 * @return 推荐已读上报时间戳
 */
public long getRecommendReportTimestamp()
```

**`TIMSNSChangeInfo` 成员方法如下：**

```
/**
 * 获取用户 identifier
 * @return 用户 identifier
 */
public String getIdentifier()

/**
 * 获取添加理由，添加需要验证时有效
 * @return 添加理由 
 */
public String getWording()

/**
 * 获取添加来源，添加需要验证时有效
 * @return 添加来源
 */
public String getSource()

/**
 * 备注，type == TIM_SNS_SYSTEM_SNS_PROFILE_CHANGE 时有效
 * @return
 */
public String getRemark()

/**
 * 获取昵称
 * @return 昵称
 */
public String getNickName()
```

**`TIMSNSSystemType` 定义如下： **

```
/**
 * 无效值
 */
INVALID(0x00),

/**
 * 增加好友消息
 */
TIM_SNS_SYSTEM_ADD_FRIEND(0x01),

/**
 * 删除好友消息
 */
TIM_SNS_SYSTEM_DEL_FRIEND(0x02),

/**
 * 增加好友申请
 */
TIM_SNS_SYSTEM_ADD_FRIEND_REQ(0x03),

/**
 * 删除未决申请
 */
TIM_SNS_SYSTEM_DEL_FRIEND_REQ(0x04),

/**
 * 黑名单添加
 */
TIM_SNS_SYSTEM_ADD_BLACKLIST(0x05),

/**
 * 黑名单删除
 */
TIM_SNS_SYSTEM_DEL_BLACKLIST(0x06),

/**
 *  未决已读上报
 */
TIM_SNS_SYSTEM_PENDENCY_REPORT(0x07),

/**
 *  关系链资料变更
 */
TIM_SNS_SYSTEM_SNS_PROFILE_CHANGE(0x08),

/**
 *  推荐数据增加
 */
TIM_SNS_SYSTEM_ADD_RECOMMEND(0x09),

/**
 *  推荐数据删除
 */
TIM_SNS_SYSTEM_DEL_RECOMMEND(0x0a),

/**
 *  已决增加
 */
TIM_SNS_SYSTEM_ADD_DECIDE(0x0b),

/**
 *  已决删除
 */
TIM_SNS_SYSTEM_DEL_DECIDE(0x0c),

/**
 *  推荐已读上报
 */
TIM_SNS_SYSTEM_RECOMMEND_REPORT(0x0d),

/**
 *  已决已读上报
 */
TIM_SNS_SYSTEM_DECIDE_REPORT(0x0e);
```

### 添加好友系统通知 

当两个用户成为好友时，两个用户均可收到添加好友系统消息。

**触发时机：**
 
当自己的关系链变更，增加好友时，收到消息（如果已经是单向好友，关系链没有变更的一方不会收到）。

**成员方法：**
 
`getSubType`：`TIM_SNS_SYSTEM_ADD_FRIEND` 
`getChangeInfoList`：成为好友的用户列表 

**`TIMSNSChangeInfo` 参数说明：**
 
`getIdentifier`： 用户 `identifier` 

### 删除好友系统通知 

当两个用户解除好友关系时，会收到删除好友系统消息。

**触发时机：**
 
当自己的关系链变更，删除好友时，收到消息（如果删除的是单向好友，关系链没有变更的一方不会收到） 。

**成员方法：**
 
`getSubType`：`TIM_SNS_SYSTEM_DEL_FRIEND` 
`getChangeInfoList`：删除好友的用户列表 

**`TIMSNSChangeInfo` 参数说明：**
 
`getIdentifier` ： 用户 `identifier` 

### 好友申请系统通知 

当申请好友时对方需要验证，自己和对方会收到好友申请系统通知。

**触发时机：**
 
当申请好友时对方需要验证，自己和对方会收到好友申请系统通知，对方可选择同意或者拒绝，自己不能操作，只做信息同步之用。 

**成员方法：**
 
`getSubType`：`TIM_SNS_SYSTEM_ADD_FRIEND_REQ`
`getChangeInfoList`：申请的好友列表 

**`TIMSNSChangeInfo` 参数说明：**
 
`getIdentifier`： 用户 `identifier` 
`getWording`： 申请理由 
`getSource`： 申请来源，申请时填写，由系统页面分配的固定字串 

### 删除未决请求通知 

**触发时机：**
 
当申请对方为好友，申请审核通过后，自己会收到删除未决请求消息，表示之前的申请已经通过。 

**成员方法：**
 
`getSubType`：`TIM_SNS_SYSTEM_DEL_FRIEND_REQ`
`getChangeInfoList`：删除未决请求的好友列表 

**`TIMSNSChangeInfo` 参数说明：**
 
`getIdentifier`： 用户 `identifier`

## 好友资料变更系统通知 

`TIMMessage` 中 `Elem` 类型为 `TIMElemType.ProfileTips` 的消息为关系链变更系统消息，由 `TIMProfileSystemElem` 来表示。 

**`TIMProfileSystemElem` 成员方法如下：**

```
/**
 * 获取资料变更类型
 * @return 资料变更消息类型
 */
public TIMProfileSystemType getSubType()

/**
 * 获取资料变更的用户名
 * @return 资料变更的用户名
 */
public String getFromUser()

/**
 * 获取资料变更的昵称，如果昵称没有变更，则昵称为 null
 * @return 资料变更的新昵称
 */
public String getNickName()
```

**`TIMProfileSystemType` 定义如下：**

```
/**
 * 无效值
 */
INVALID,

/**
 * 好友资料变更
 */
TIM_PROFILE_SYSTEM_FRIEND_PROFILE_CHANGE,
```

## 未决请求

未决请求即为等待处理的请求，比如设置了添加好友选项为需要验证，则对方申请添加好友时会有未决请求，如果同意或者拒绝这个申请，未决请求会变为已决。通过 `TIMFriendshipManagerExt` 的 `getFutureFriends` 方法可以从 Server 获取未决请求列表。

**原型：***

```
/**
 * 未决请求和好友推荐拉取
 * @param flags 获取的资料标识,参见{@see TIMFriendshipManager#TIM_PROFILE_FLAG_NICK}等
 * @param futureFlags 指定要获取的类型，未决 in，未决 out，推荐，已决四种，参见{@see TIMFriendshipManagerExt#TIM_FUTURE_FRIEND_PENDENCY_IN_TYPE}等
 * @param custom 自定义字段，可填 null
 * @param meta 请求信息，参见{@see TIMFriendFutureMeta}
 * @param cb 回调
 */
public void getFutureFriends(long flags, long futureFlags, @Nullable List<String> custom,
							 @NonNull TIMFriendFutureMeta meta, TIMValueCallBack<TIMGetFriendFutureListSucc> cb)
```

