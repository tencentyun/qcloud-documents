IM 通讯云提供了关系链和用户资料托管，App 开发者使用简单的接口就可实现关系链和用户资料存储功能，另外，为了方便不同用户定制化资料，也提供用户资料和用户关系链的自定义字段，您可以登录 [云通信控制台](https://console.cloud.tencent.com/avc) 自助申请。以下介绍到的方法，除非特别说明，均属于 `TIMFriendshipManager` 中提供的方法。

## 关系链资料介绍

**用户关系链**是指好友关系，通过接口可以实现加好友、解除好友、获取好友列表等操作。用户资料保存用户的信息，比如昵称、头像等，另外，还有一种好友资料，只跟好友相关比如备注，分组等。

## 设置自己的资料

### 设置自己的昵称 

可通过 `TIMFriendshipManager` 的 `setNickname` 方法设置用户自己的昵称，昵称最大为 64 字节。

**原型：**

```
public void setNickName(java.lang.String nickName,
                        TIMCallBack cb)
```

**参数说明：**

参数|说明
---|---
nickName | 新昵称（最长 64 字节） 
cb | 回调 

**示例：** 

```
//设置新昵称为 cat
TIMFriendshipManager.getInstance().setNickName("cat", new TIMCallBack(){
	@Override
	public void onError(int code, String desc){
		//错误码 code 和错误描述 desc，可用于定位请求失败原因
		//错误码 code 列表请参见错误码表
        Log.e(tag, "setNickName failed: " + code + " desc");
	}
	@Override
	public void onSuccess(){
	        Log.e(tag, "setNickName succ");
	}
});
```

### 设置好友验证方式 

可通过 `TIMFriendshipManager` 的 `setAllowType` 方法设置好友验证方式，用户可根据需要设置其中一种，**目前没有方法设置默认的好友验证方式，默认都是任何人可加好友**。有以下几种验证方式：

- 允许任何人添加好友
- 拒绝任何人添加好友
- 添加好友需要验证

**原型：**
```
public void setAllowType(TIMFriendAllowType allowType,
                         TIMCallBack cb)
```

**参数说明：**
 
参数|说明
---|---
allowType | 加好友选项 
cb | 回调 

**`TIMFriendAllowType` 原型：**

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

以下示例中设置了自己的好友验证方式为需要验证，此时如果有用户申请加好友，会收到加好友的系统通知（详见[关系链变更系统通知](#.E5.85.B3.E7.B3.BB.E9.93.BE.E5.8F.98.E6.9B.B4.E7.B3.BB.E7.BB.9F.E9.80.9A.E7.9F.A5)）。**示例： **

```
//设置自己的好友验证方式为需要验证
TIMFriendshipManager.getInstance().setAllowType(TIMFriendAllowType.TIM_FRIEND_NEED_CONFIRM, new TIMCallBack(){
	@Override
	public void onError(int code, String desc){
		//错误码 code 和错误描述 desc，可用于定位请求失败原因
		//错误码 code 列表请参见错误码表
        Log.e(tag, "setAllowType failed: " + code + " desc");
	}
	@Override
	public void onSuccess(){
	        Log.e(tag, "setAllowType succ");
	}
});
```

### 设置自己的头像

可通过 `TIMFriendshipManager` 的 `setFaceUrl` 方法设置用户自己的头像，当前 ImSDK 不会保存用户图片资源，需要用户上传图片到其他存储平台，通过 ImSDK 设置图片 URL。

**原型：**

```
public void setFaceUrl(java.lang.String faceUrl,
                       TIMCallBack cb)
```

**参数说明：**
 
 参数|说明
 ---|---
faceUrl| 要设置的头像 
cb |回调 

**示例：**

```
String faceUrl = "http://faceurl";
TIMFriendshipManager.getInstance().setFaceUrl(faceUrl, new TIMCallBack(){
	@Override
	public void onError(int code, String desc) {
		//错误码 code 和错误描述 desc，可用于定位请求失败原因
		//错误码 code 列表请参见错误码表
		Log.e(tag, "setFaceUrl failed: " + code + " desc" + desc);
	}
	@Override
	public void onSuccess() {
		Log.e(tag, "setFaceUrl succ");
	}
});
```

### 设置自己的自定义字段

通过 Server 配置（内测功能，可提交工单修改，可参考：[新增用户维度的自定义字段](/doc/product/269/云通信配置变更需求工单#.E6.96.B0.E5.A2.9E.E7.94.A8.E6.88.B7.E7.BB.B4.E5.BA.A6.E7.9A.84.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5)）可以设置自己的自定义字段，通过自定义字段可以做到很多非内置功能，如用户性别、地址等字段。

**原型：**

```
public void setCustomInfo(String key, byte[] value, TIMCallBack cb)
```

**参数说明：**
 
参数 | 说明
--- | ---
key | 自定义信息 key
value | 自定义信息 value 
cb | 回调

### 设置自己的个性签名

云通信支持个性签名，用户设置后所有人可见。

**原型：**

```
public void setSelfSignature(String signature, TIMCallBack cb)
```

**参数说明：**
 
参数 | 说明
--- | ---
signature | 个性签名
cb | 回调 

### 设置自己的性别

云通信支持设置自己的性别，设置后所有人可见。设置方法为 `TIMFriendshipManager` 中的 `setGender`。

**原型：**

```
/**
 * 设置性别
 * @param type 性别类型
 * @param cb 回调
 */
public void setGender(TIMFriendGenderType type, TIMCallBack cb)
```

### 设置自己的生日

云通信支持设置自己的生日，设置后所有人可见。设置方法为 `TIMFriendshipManager` 中的 `setBirthday`。

>!生日信息是一个长整形，结果只保留低 32 位，具体含义由应用自行定义和解析。

**原型：**

```
/**
 * 设置生日信息
 * @param birthday 生日信息，含义由应用自行定义，只有低 32 位有效
 * @param cb 回调
 */
public void setBirthday(long birthday, TIMCallBack cb)
```

### 设置自己的语言

云通信支持设置自己的语言，设置后所有人可见。设置方法为 `TIMFriendshipManager` 中的 `setLanguage`。

>!语言信息是一个长整形，结果只保留低 32 位，具体含义由应用自行定义和解析。

**原型：**

```
/**
 * 设置语言
 * @param lang 语言信息，含义由应用自行定义，只有低 32 位有效
 * @param cb 回调
 */
public void setLanguage(long lang, TIMCallBack cb)
```

### 设置自己的位置

云通信支持设置自己的位置，设置后所有人可见。设置方法为 `TIMFriendshipManager` 中的 `setLocation`。

**原型：**

```
/**
 * 设置位置信息
 * @param location 位置信息
 * @param cb 回调
 */
public void setLocation(String location, TIMCallBack cb)
```

## 获取资料

### 获取自己的资料 

可通过 `TIMFriendshipManager` 的 `getSelfProfile` 方法获取用户自己的资料，默认只拉取基本资料，如果只需要个别字段或者自定义字段，可以使用 [按照字段获取用户资料](#.E6.8C.89.E7.85.A7.E5.AD.97.E6.AE.B5.E8.8E.B7.E5.8F.96.E7.94.A8.E6.88.B7.E8.B5.84.E6.96.99) 方法设置，此方法全局有效。

**原型：**

```
public void getSelfProfile(TIMValueCallBack<TIMUserProfile> cb)
```

**参数说明：**

参数|说明
---|---
cb | 回调，OnSuccess 函数的参数中返回自己的资料，详见 TIMUserProfile 

**`TIMUserProfile` 成员方法：**

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

**示例：**

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

### 获取好友的资料

可通过 `TIMFriendshipManager` 的 `getFriendsProfile` 方法获取好友的资料（1.9 版本之前可以获取任何人资料，1.9 版本之后调用 `getUsersProfile` 获取），默认只拉取基本资料，如果只需要个别字段或者自定义字段，可以使用 [按照字段获取用户资料](#.E6.8C.89.E7.85.A7.E5.AD.97.E6.AE.B5.E8.8E.B7.E5.8F.96.E7.94.A8.E6.88.B7.E8.B5.84.E6.96.99) 方法设置，此方法全局有效。此接口从网路获取数据。

**原型：**  

```
public void getFriendsProfile(java.util.List<java.lang.String> users,
                              TIMValueCallBack<java.util.List<TIMUserProfile>> cb)
```

**参数说明：**
 
 参数|说明
 ---|---
users | 要获取资料的好友 identifier 列表 
cb | 回调，OnSuccess 函数的参数中返回包含相应用户的 TIMUserProfile 列表 

**示例：**

```
//待获取用户资料的好友列表
List<String> users = new ArrayList<String>();
users.add("sample_user_1");
users.add("sample_user_2");
//获取好友资料
TIMFriendshipManager.getInstance().getFriendsProfile(users, new TIMValueCallBack<List<TIMUserProfile>>(){
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

### 获取任何人的资料

可通过 `TIMFriendshipManager` 的 `getUsersProfile` 方法获取好友的资料（1.9 版本之前可以获取任何人资料，1.9 版本之后调用 `getFriendsProfile` 获取），默认只拉取基本资料，如果只需要个别字段或者自定义字段，可以使用 [按照字段获取用户资料](#.E6.8C.89.E7.85.A7.E5.AD.97.E6.AE.B5.E8.8E.B7.E5.8F.96.E7.94.A8.E6.88.B7.E8.B5.84.E6.96.99) 方法设置，此方法全局有效。此接口从网路获取数据。

**原型：**  

```
public void getUsersProfile(java.util.List<java.lang.String> users,
                              TIMValueCallBack<java.util.List<TIMUserProfile>> cb)
```

**参数说明：**
 
 参数|说明
 ---|---
users | 要获取资料的用户 identifier 列表 
cb | 回调，OnSuccess 函数的参数中返回包含相应用户的 TIMUserProfile 列表 

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

### 按照字段获取用户资料

1.9 以后版本可以通过 `TIMManager` 中的 `initFriendshipSettings` 方法设置所需要拉取的资料字段，方便更灵活的获取资料。需登录前设置，若不设置则默认拉取所有基本字段，不拉取自定义字段。

**原型：**
```
public void initFriendshipSettings(long flags,@Nullable List<String> customFields)
```

**参数说明：**

参数|说明
---|---
flags|关系链默认拉取资料标识，按位设置，参见 TIMFriendshipManager.TIM_PROFILE_FLAG_NICK 等
customFields|自定义字段列表，可以填 null

## 关系链相关资料

### 好友备注 

可通过 `TIMFriendshipManager` 的 `setFriendRemark` 方法设置好友备注，**需要注意好友备注必须先加为好友才可设置备注**。

**原型：**

```
public void setFriendRemark(java.lang.String identifier,
                   java.lang.String remark,
                   TIMCallBack cb)
```

**参数说明：**
 
 参数|说明
 ---|---
identifier | 用户标识 
remark | 备注 
cb | 回调 

以下示例中设置好友『sample_user_002』的备注为『002 remark』。 **示例：**

```
String remark = "002_remark";
String identifier = "sample_user_002";
TIMFriendshipManager.getInstance().setFriendRemark(identifier, remark, 
        new TIMCallBack() {//回调接口
            @Override
            public void onSuccess() {//成功
                Log.d(tag, "setFriendRemark succ");
            }
            @Override
            public void onError(int code, String desc) {//失败
                //错误码 code 和错误描述 desc，可用于定位请求失败原因
                //错误码 code 含义请参见错误码表
                Log.d(tag, "setFriendRemark failed. code: " + code + " errmsg: " + desc);
            }
});
```

### 设置好友自定义资料

通过 Server 配置（内测功能）可以设置自己的自定义字段，通过自定义字段可以做到很多非内置功能。

**原型：**

```
public void setFriendCustom(String identifier, Map<byte[], byte[]> customInfos, TIMCallBack cb)
```

**参数说明：**
 
参数 | 说明
--- | ---
identifier | 要设置的好友 identifier
customInfos | 自定义属性 map
cb | 回调

## 好友关系

### 添加好友

通过 `TIMFriendshipManager` 的 `addFriend` 方法可以批量添加好友，目前所能支持的最大好友列表为3000个。

**原型：**

```
public void addFriend(java.util.List<TIMAddFriendRequest> users,
                      TIMValueCallBack<java.util.List<TIMFriendResult>> cb)
```

**参数说明：**
 
 | 参数 | 说明 |
| --- | --- |
| users | 要添加的用户列表 TIMAddFriendRequest 列表 |
| cb | 回调，onSuccess 函数的参数中返回 TIMFriendResult 列表，详见 TIMFriendResult |

**`TIMAddFriendRequest` 成员方法：**

```
//添加来源，固定字f符串，在页面上申请，留空表示未知来源
void	setAddrSource(java.lang.String addSource)
//添加请求说明，最大 120 字节，如果用户设置为添加好友需要审核，对方会收到此信息并决定是否通过。
void	setAddWording(java.lang.String addWording)
//设置添加好友的 identifier
void	setIdentifier(java.lang.String identifier)
//添加成功后给用户的备注信息，最大 96 字节
void	setRemark(java.lang.String remark)
```

**`TIMFriendResult` 成员方法：**

```
//获取用户 identifier
java.lang.String	getIdentifer()
//获取操作结果 status
TIMFriendStatus	getStatus()
```

**`TIMFriendStatus` 原型：**

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

开发者可根据对应情况提示用户。 **示例：**

```
//创建请求列表
List<TIMAddFriendRequest> reqList = new ArrayList<TIMAddFriendRequest>();
//添加好友请求
TIMAddFriendRequest req = new TIMAddFriendRequest();
req.setAddrSource("DemoApp");
req.setAddWording("add me");
req.setIdentifier("sample_user_1");
req.setRemark("Cat");
reqList.add(req);
//申请添加好友
TIMFriendshipManager.getInstance().addFriend(reqList, new TIMValueCallBack<List<TIMFriendResult>>() {
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

可通过 `TIMFriendshipManager` 的 `delFriend` 方法可以批量删除好友。

**原型：**      

```
public void delFriend(TIMDelFriendType delType,
                      java.util.List<TIMAddFriendRequest> users,
                      TIMValueCallBack<java.util.List<TIMFriendResult>> cb)
```

**参数说明：**
 
 
 | 参数 | 说明 |
| --- | --- |
| delType | 删除类型（单向好友、双向好友） |
| users | 要删除的用户列表 TIMAddFriendRequest 列表 |
| cb | 回调，onSuccess 函数的参数中返回 TIMFriendResult 列表，详见 TIMFriendResult |

**示例：**

```
//删除好友
List<TIMAddFriendRequest> reqList = new ArrayList<TIMAddFriendRequest>();
TIMAddFriendRequest req = new TIMAddFriendRequest();
req.setIdentifier("sample_user_1");
reqList.add(req);
//指定删除双向好友
TIMFriendshipManager.getInstance().delFriend(TIMDelFriendType.TIM_FRIEND_DEL_BOTH, reqList, new TIMValueCallBack<List<TIMFriendResult>>() {
    @Override
    public void onError(int code, String desc){
        //错误码 code 和错误描述 desc，可用于定位请求失败原因
        //错误码 code 列表请参见错误码表
        Log.e(tag, "delFriend failed: " + code + " desc");
    }
    @Override
    public void onSuccess(Listresult){
        for(TIMFriendResult res : result){
            Log.e(tag, "identifier: " + res.getIdentifer() + " status: " + res.getStatus());
        }
    }
});
```

### 获取所有好友 

可通过 `TIMFriendshipManager` 的 `getFriendList` 方法可以获取所有好友，默认只拉取基本资料，如果只需要个别字段或者自定义字段，可以使用 [按照字段获取用户资料](#.E6.8C.89.E7.85.A7.E5.AD.97.E6.AE.B5.E8.8E.B7.E5.8F.96.E7.94.A8.E6.88.B7.E8.B5.84.E6.96.99) 方法设置，此方法全局有效。

**原型： **   

```
public void getFriendList(TIMValueCallBack<java.util.List<TIMUserProfile>> cb)
```

**参数说明：**
 
| 参数 | 说明 |
| --- | --- |
| cb | 回调，OnSuccess 函数的参数中返回所有好友的 TIMUserProfile 列表，只包含 identifier，nickname，remark 三个字段，其他字段需要通过拉取好友的详细资料获得 |
 
**示例：**

```
//获取好友列表
TIMFriendshipManager.getInstance().getFriendList(new TIMValueCallBack<List<TIMUserProfile>>(){
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

### 同意/拒绝好友申请 

可通过 `TIMFriendshipManager` 的 `doResponse` 方法可以获取所有好友。

**对未决的好友申请进行回应原型：**

```
public void addFriendResponse(TIMFriendAddResponse response,
                              TIMValueCallBack<TIMFriendResult> cb)
```

**参数说明：**
 
 | 参数 | 说明 |
| --- | --- |
| response | 回应内容  |
| cb | onSuccess 函数的参数中返回 TIMFriendResult 列表，详见 TIMFriendResult |

**`TIMFriendAddResponse` 成员方法：**

```
//设置对方 identifier
void	setIdentifier(java.lang.String identifier) 
//加好友成功时设置对方备注
void	setRemark(java.lang.String remark) 
//设置响应类型
void	setType(TIMFriendResponseType type) 
```

**`TIMFriendResponseType` 原型：**

```
//同意对方的好友申请
Agree
//同意对方的好友申请，并添加对方为好友
AgreeAndAdd
//拒绝对方的好友申请
Reject
```

### 添加用户到黑名单

可以把任意用户拉黑，如果此前是好友关系，拉黑后自动解除好友，拉黑后对方发消息无法收到。

**原型：**
```
public void addBlackList(List<String> identifiers, TIMValueCallBack<List<TIMFriendResult>> cb)
```

**参数说明：**

参数 | 说明
--- | ---
identifiers | 要添加到黑名单的用户列表
cb | 回调，onSuccess 函数的参数中返回 TIMFriendResult 列表

### 把用户从黑名单删除

**原型：**
```
public void delBlackList(List<String> identifiers, TIMValueCallBack<List<TIMFriendResult>> cb)
```

**参数说明：**

参数 | 说明
--- | ---
identifiers | 要从黑名单中删除的用户列表
cb | 回调, onSuccess 函数的参数中返回 TIMFriendResult 列表

### 获取黑名单列表

**原型：**
```
public void getBlackList(TIMValueCallBack<List<String>> cb)
```

**参数说明：**

参数 | 说明
--- | ---
cb | 回调，onSuccess 函数的参数中返回黑名单用户 identifier 列表


## 好友分组

### 创建好友分组

创建分组时，可以同时指定添加的用户，同一用户可以添加到多个分组。

**原型：**

```
public void createFriendGroup(List<String> groupNames, List<String> users,
                                  TIMValueCallBack<List<TIMFriendResult>> cb)
```

**参数说明：**

参数 | 说明
--- | ---
groupNames | 分组名称列表，必须是当前不存在的分组
users | 要添加到分组中的好友列表
cb | 回调，在 onSuccess 回调的参数中返回请求结果{@see TIMFriendResult}列表

### 删除好友分组

**原型：**

```
public void deleteFriendGroup(List<String> groupNames, TIMCallBack cb)
```

**参数说明：**

参数 | 说明
--- | ---
groupNames | 要删除的好友分组名称列表
cb | 回调

### 添加好友到某分组

**原型：**

```
public void addFriendsToFriendGroup(String groupName, List<String> users, TIMValueCallBack<List<TIMFriendResult>> cb)
```

**参数说明：**

参数 | 说明
--- | ---
groupName | 分组名称
users |  要添加到分组中的好友列表
cb | 回调，在 onSuccess 回调的参数中返回请求结果 TIMFriendResult 列表

### 从某分组删除好友

**原型：**

```
public void delFriendsFromFriendGroup(String groupName, List<String> users, TIMValueCallBack<List<TIMFriendResult>> cb)
```

**参数说明：**

参数 | 说明
--- | ---
groupName | 分组名称
users |  要从分组删除的好友列表
cb | 回调，在 onSuccess 回调的参数中返回请求结果 TIMFriendResult 列表


### 重命名好友分组

**原型：**

```
public void renameFriendGroupName(String oldName, String newName, TIMCallBack cb)
```

**参数说明：**

参数 | 说明
--- | ---
oldName | 旧分组名称
newName |  新分组名称
cb | 回调

### 获取指定的好友分组信息

**原型：**

```
public void getFriendGroups(List<String> groupNames, TIMValueCallBack<List<TIMFriendGroup>> cb)
```

**参数说明：**

参数 | 说明
--- | ---
groupNames | 要获取信息的好友分组名称列表，为 null 则获取所有的好友分组信息
cb | 回调，在 onSuccess 回调的参数中返回好友分组列表，详见 TIMFriendGroup


### 获取所有好友分组

通过 [获取指定的好友分组信息](#.E8.8E.B7.E5.8F.96.E6.8C.87.E5.AE.9A.E7.9A.84.E5.A5.BD.E5.8F.8B.E5.88.86.E7.BB.84.E4.BF.A1.E6.81.AF) 可以获取所有分组信息，另外，通过 [获取所有好友](#.E8.8E.B7.E5.8F.96.E6.89.80.E6.9C.89.E5.A5.BD.E5.8F.8B)，也可以获取分组信息。

## 关系链资料存储

### 开启存储

为了兼容老版本，避免老版本开发者和 ImSDK 都存储数据，默认情况下行为跟 1.9 版本一致，不会进行存储。需要用户**在登录前**调用显式调用 `TIMManager` 中的 `enableFriendshipStorage` 设置是否启用关系链资料本地存储。

**原型：**

```
public void enableFriendshipStorage(boolean enable)
```

**参数说明：**

参数|说明
---|---
enable|true - 启用关系链资料本地存储， false - 不启用关系链资料本地存储

### 内存中同步获取关系链资料数据

通过 `TIMFriendshipProxy` 提供的接口可以从内存中同步获取关系链资料数据。

**原型：**

```
//获取 TIMFriendshipProxy 实例
public static TIMFriendshipProxy getInstance()
//获取全部好友
public List<TIMUserProfile> getFriends()
//获取指定 ID 好友
public List<TIMUserProfile> getFriendsById(List<String> identifiers)
//获取指定好友分组，包括好友信息
public List<TIMFriendGroup> getFriendsByGroups(@Nullable List<String> groups)
```

**参数说明：**

参数|说明
---|---
identifiers | 好友用户 ID
groups | 好友分组名称


### 好友、资料变更回调

1.9 版本之前，必须通过系统消息来感知变更，这种方式需要用户解析消息内容，层次结构较深，在 1.9 版本之后，如果开启了存储的功能，可以用更加明显易用的回调感知变更。通过 `TIMManager` 中的 `setFriendshipProxyListener` 方法来设置关系链变更事件监听器。

**原型：**

```
public void setFriendshipProxyListener(TIMFriendshipProxyListener listener) 
```

**参数说明：**

参数|说明
---|---
listener | 关系链变更事件监听器

通过设置 `TIMFriendshipProxyListener` 变更回调，可以在发生不同事件的时候感知不同的事件，之后可通过同步接口获取信息并更新 UI 操作。**`TIMFriendshipProxyListener` 主要的事件回调如下：**

```
/**
 *  收到代理状态变更通知
 *
 *  @param status 当前状态
 */
void OnProxyStatusChange(TIMFriendshipProxyStatus status);
/**
 *  添加好友通知
 *
 *  @param users 好友列表，详见{@see TIMUserProfile}
 */
void OnAddFriends(List<TIMUserProfile> users);
/**
 *  删除好友通知
 *
 *  @param identifiers 用户 ID 列表
 */
void OnDelFriends(List<String> identifiers);
/**
 *  好友资料更新通知
 *
 *  @param profiles 资料列表,详见{@see TIMUserProfile}
 */
void OnFriendProfileUpdate(List<TIMUserProfile> profiles);
/**
 *  好友申请通知
 *
 *  @param reqs 好友申请者ID列表，详见{@see TIMSNSChangeInfo}
 */
void OnAddFriendReqs(List<TIMSNSChangeInfo> reqs);
```

## 关系链变更系统通知 

`TIMMessage` 中 `Elem` 类型 `TIMSNSSystemElem` 为关系链变更系统消息。

**成员方法：**

```
//获取关系链变更消息详细信息列表
java.util.ListgetChangeInfoList()
//获取变更消息类型
TIMSNSSystemType	getSubType()
```

**`TIMSNSChangeInfo` 成员方法：**

```
//获取用户 identifier
java.lang.String	getIdentifier()
//获取添加来源，添加需要验证时有效
java.lang.String	getSource()
//获取添加理由，添加需要验证时有效
java.lang.String	getWording()
```

**`TIMSNSSystemType` 原型： **

```
//增加好友消息
TIM_SNS_SYSTEM_ADD_FRIEND
//增加好友申请
TIM_SNS_SYSTEM_ADD_FRIEND_REQ
//删除好友消息
TIM_SNS_SYSTEM_DEL_FRIEND
//删除未决申请
TIM_SNS_SYSTEM_DEL_FRIEND_REQ
```

### 添加好友系统通知 

当两个用户成为好友时，两个用户均可收到添加好友系统消息。

**触发时机：**当自己的关系链变更，增加好友时，收到消息（如果已经是单向好友，关系链没有变更的一方不会收到） 。

**成员方法：**
 
| 成员方法 | 说明 |
| --- | --- |
| getSubType | TIM_SNS_SYSTEM_ADD_FRIEND |
| getChangeInfoList | 成为好友的用户列表 |

**`TIMSNSChangeInfo` 参数说明：**
 
| 参数 | 说明 |
| --- | --- |
| getIdentifier | 用户 identifier |

### 删除好友系统通知 

当两个用户解除好友关系时，会收到删除好友系统消息。

**触发时机：**当自己的关系链变更，删除好友时，收到消息（如果删除的是单向好友，关系链没有变更的一方不会收到） 。

**成员方法：**
 
| 成员方法 | 说明 |
| --- | --- |
| getSubType | TIM_SNS_SYSTEM_DEL_FRIEND |
| getChangeInfoList | 删除好友的用户列表 |

**TIMSNSChangeInfo 参数说明：**
 
| 参数 | 说明 |
| --- | --- |
| getIdentifier | 用户 identifier |

### 好友申请系统通知 

当申请好友时对方需要验证，自己和对方会收到好友申请系统通知。

**触发时机：**当申请好友时对方需要验证，自己和对方会收到好友申请系统通知，对方可选择同意或者拒绝，自己不能操作，只做信息同步之用。 

**成员方法：**
 
| 成员方法 | 说明 |
| --- | --- |
| getSubType | TIM_SNS_SYSTEM_ADD_FRIEND_REQ |
| getChangeInfoList | 申请的好友列表 |

**`TIMSNSChangeInfo` 参数说明：**
 
| 参数 | 说明 |
| --- | --- |
| getIdentifier | 用户 identifier |
| getWording | 申请理由 |
| getSource | 申请来源，申请时填写，由系统页面分配的固定字串  |

### 删除未决请求通知 

**触发时机：**当申请对方为好友，申请审核通过后，自己会收到删除未决请求消息，表示之前的申请已经通过。 

**成员方法：**
 
| 成员方法 | 说明 |
| --- | --- |
| getSubType | TIM_SNS_SYSTEM_DEL_FRIEND_REQ |
| getChangeInfoList | 删除未决请求的好友列表 |

**TIMSNSChangeInfo 参数说明：**
 
| 参数 | 说明 |
| --- | --- |
| getIdentifier | 用户 identifier |

## 好友资料变更系统通知 

`TIMMessage` 中 `Elem` 类型 `TIMProfileSystemElem` 为关系链变更系统消息。

**`TIMProfileSystemElem` 成员方法：**

```
//获取资料变更的用户名
java.lang.String	getFromUser()
//获取资料变更的昵称，如果昵称没有变更，则昵称为 null
java.lang.String	getNickName()
//获取资料变更类型
TIMProfileSystemType	getSubType()
```

## 未决请求

未决请求即为等待处理的请求，比如设置了需要验证好友，对方申请时会有未决请求，如果同意或者拒绝这个申请，未决请求会变为已决。通过 `TIMFriendshipManager` 的 `getFutureFriends` 方法可以从 Server 获取未决请求列表。

**原型：**

```
public void getFutureFriends(long flags, long futureFlags, List<String> custom,
                                 TIMFriendFutureMeta meta, TIMValueCallBack<TIMGetFriendFutureListSucc> cb)
```

**参数说明：**

参数|说明
---|---
flags | 获取的资料标志，详见 TIMProfileFlag
futureFlag | 获取的未决标记，如未决，已决，推荐等类型
custom | 自定义字段，如要获取填写
meta | 请求信息，参见 TIMFriendFutureMeta 定义
cb | 回调
