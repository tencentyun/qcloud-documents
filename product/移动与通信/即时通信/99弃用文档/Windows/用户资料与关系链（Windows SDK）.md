IM 通讯云提供了关系链和用户资料托管，App 开发者使用简单的接口就可实现关系链和用户资料存储功能，另外，为了方便不通用户定制化资料，也提供用户资料和用户关系链的自定义字段（目前此功能为内测功能）。本节所有的接口不论对独立帐号体系还是托管帐号体系都有有效。 

## 关系链资料介绍

用户关系链是指好友关系，通过接口可以实现加好友、解除好友、获取好友列表等操作。用户资料保存用户的信息，比如昵称、头像等，另外，还有一种好友资料，只跟好友相关比如备注，分组等。

## 设置自己的资料

### 设置自己的昵称

可通过 `TIMSetNickName` 方法设置用户自己的昵称，昵称最大为 64 字节。

**原型： ** 

```
	/**
	Description:	设置自己的昵称
	@param	[in]	nick	昵称
	@param	[in]	len		昵称长度
	@param	[in]	cb		回调
	@return			void
	@exception      none
	*/
	TIM_DECL void TIMSetNickName(char* nick, uint32_t len, TIMCommCB * cb);
```

**参数说明：**

参数  | 说明
--- | ---
nick | 要设置的昵称 
len | 要设置的昵称长度
cb | 回调 

### 设置好友验证方式 

可通过 `TIMFriendshipManager` 的 `SetAllowType` 方法设置好友验证方式，用户可根据需要设置其中一种，**目前没有方法设置默认的好友验证方式，默认都是任何人可加好友**。目前有以下几种验证方式。

* 同意任何用户加好友
* 拒绝任何人加好友
* 需要验证

**原型：**

```
	/**
	Description:	设置好友验证方式
	@param	[in]	type	验证方式
	@param	[in]	cb		回调
	@return			void
	@exception      none
	*/
	TIM_DECL void TIMSetAllowType(E_TIMFriendAllowType type, TIMCommCB * cb);
```

**参数说明： **

参数  | 说明
--- | ---
type | 好友验证方式，详见 TIMFriendAllowType<br>TIM_FRIEND_ALLOW_ANY：同意任何用户加好友<br>TIM_FRIEND_DENY_ANY：拒绝任何人加好友<br>TIM_FRIEND_NEED_CONFIRM：需要验证 
cb | 回调 

### 设置自己的头像
 
`TIMSetFaceURL` 方法设置用户自己的头像，当前 ImSDK 不会保存用户图片资源，需要用户上传图片到其他存储平台，通过 ImSDK 设置图片 URL。

**原型：**

```
	/**
	Description:	设置自己的头像
	@param	[in]	url		头像 URL
	@param	[in]	url_len	URL 长度
	@param	[in]	cb		回调
	@return			void
	@exception      none
	*/
	TIM_DECL void TIMSetFaceURL(char* url, uint32_t url_len, TIMCommCB * cb);
```

**参数说明：**
 
参数 | 说明
--- | ---
url | 要设置的头像 URL
url_len | URL 长度
cb | 回调 

## 获取资料 

### 获取自己的资料 
可通过 `TIMGetSelfProfile` 方法获取用户自己的资料，默认只拉取基本资料，如果只需要个别字段或者自定义字段，可以使用 [获取好友资料的部分字段](#.E8.8E.B7.E5.8F.96.E5.A5.BD.E5.8F.8B.E8.B5.84.E6.96.99.E7.9A.84.E9.83.A8.E5.88.86.E5.AD.97.E6.AE.B5) 方法设置，此方法全局有效。

**原型：**

```
	/**
	Description:	获取自己的资料 
	@param	[in]	cb	回调
	@return			void
	@exception      none
	*/
	TIM_DECL void TIMGetSelfProfile(TIMGetSelfProfileCallback* cb);
typedef void (*CBGetSelfProfileCallbackOnSuccess) (TIMSelfProfileHandle* handles, uint32_t num, void* data);
typedef void (*CBGetSelfProfileCallbackOnError) (int code, const char* desc, void* data);
typedef struct_T_TIMGetSelfProfileCallback
{
	CBGetSelfProfileCallbackOnSuccess OnSuccess;
	CBGetSelfProfileCallbackOnError OnError;
	void* data;
}TIMGetSelfProfileCallback;
typedef void* TIMSelfProfileHandle;
TIMSelfProfileHandle CloneSelfProfileHandle(TIMSelfProfileHandle handle);
void DestroySelfProfileHandle(TIMSelfProfileHandle handle);
int GetNickName4SlefProfileHandle(TIMSelfProfileHandle handle, char* buf, uint32_t* len);
E_TIMFriendAllowType GetAllowType4SlefProfileHandle(TIMSelfProfileHandle handle);
```

**参数说明：**
 
属性 | 说明
--- | ---
cb | 回调

**属性说明：**
 
属性 | 说明
--- | ---
identifier | 自己的用户标识 
nickname | 自己的昵称 
allowType | 好友验证方式 

### 获取好友的资料

可通过 `TIMGetFriendProfile` 方法获取好友的资料（1.9 版本之前可以获取任何人资料，1.9 版本之后调用 `GetUsersProfile` 获取），默认只拉取基本资料，如果只需要个别字段或者自定义字段，可以使用 [获取好友资料的部分字段](#.E8.8E.B7.E5.8F.96.E5.A5.BD.E5.8F.8B.E8.B5.84.E6.96.99.E7.9A.84.E9.83.A8.E5.88.86.E5.AD.97.E6.AE.B5) 方法设置，此方法全局有效。此接口从网路获取数据。

**原型：**

```
/**
Description:	获取好友的资料
@param	[in]	id		要获取的好友 ID 数组
@param	[in]	num		要获取的好友个数
@param	[in]	cb		回调
@return			void
@exception      none
*/
TIM_DECL void TIMGetFriendProfile(const char** id, uint32_t num, TIMGetFriendProfileCallback* cb);

typedef void (*CBGetFriendProfileCallbackOnSuccess) (TIMFriendProfileHandle* handles, uint32_t num, void* data);
typedef void (*CBGetFriendProfileCallbackOnError) (int code, const char* desc, void* data);
typedef struct _T_TIMGetFriendProfileCallback
{
	CBGetFriendProfileCallbackOnSuccess OnSuccess;
	CBGetFriendProfileCallbackOnError OnError;
	void* data;
}TIMGetFriendProfileCallback;
typedef void* TIMFriendProfileHandle;
TIMFriendProfileHandle CloneFriendProfileHandle(TIMFriendProfileHandle handle);
void DestroyFriendProfileHandle(TIMFriendProfileHandle handle);
int GetID4FriendProfileHandle(TIMFriendProfileHandle handle, char* id, uint32_t* len);
int GetNickName4FriendProfileHandle(TIMFriendProfileHandle handle, char* buf, uint32_t* len);
int GetRemark4FriendProfileHandle(TIMFriendProfileHandle handle, char* remark, uint32_t* len);
E_TIMFriendAllowType GetAllowType4FriendProfileHandle(TIMFriendProfileHandle handle);
```
 
**参数说明：**
 
参数 | 说明
--- | ---
id | 用户列表 
num | 用户个数 
cb | 回调，返回 TIMFriendProfileHandle 数组，包含用户资料 

**属性说明：**
 
属性 | 说明
--- | ---
identifier | 好友的 identifer 
nickname | 好友昵称 
remark  | 好友备注 
allowType | 好友验证方式 


### 获取任何人的资料

1.9 以后版本可通过 `TIMFriendshipManager` 的 `GetUsersProfile` 方法获取任何用户公开资料，1.9 版本之前可以使用 `GetFriendsProfile` 获取所有人资料，默认只拉取基本资料，如果只需要个别字段或者自定义字段，可以使用 [获取好友资料的部分字段](#.E8.8E.B7.E5.8F.96.E5.A5.BD.E5.8F.8B.E8.B5.84.E6.96.99.E7.9A.84.E9.83.A8.E5.88.86.E5.AD.97.E6.AE.B5) 方法设置，此方法全局有效。

```
/**
Description:	获取任何人的资料
@param	[in]	id		要获取的用户 ID 数组
@param	[in]	num		要获取的用户个数
@param	[in]	cb		回调
@return			void
@exception      none
*/
TIM_DECL void TIMGetUserProfile(const char** id, uint32_t num, TIMGetFriendProfileCallback* cb);

typedef void (*CBGetFriendProfileCallbackOnSuccess) (TIMFriendProfileHandle* handles, uint32_t num, void* data);
typedef void (*CBGetFriendProfileCallbackOnError) (int code, const char* desc, void* data);
typedef struct _T_TIMGetFriendProfileCallback
{
	CBGetFriendProfileCallbackOnSuccess OnSuccess;
	CBGetFriendProfileCallbackOnError OnError;
	void* data;
}TIMGetFriendProfileCallback;
typedef void* TIMFriendProfileHandle;
TIMFriendProfileHandle CloneFriendProfileHandle(TIMFriendProfileHandle handle);
void DestroyFriendProfileHandle(TIMFriendProfileHandle handle);
int GetID4FriendProfileHandle(TIMFriendProfileHandle handle, char* id, uint32_t* len);
int GetNickName4FriendProfileHandle(TIMFriendProfileHandle handle, char* buf, uint32_t* len);
int GetRemark4FriendProfileHandle(TIMFriendProfileHandle handle, char* remark, uint32_t* len);
E_TIMFriendAllowType GetAllowType4FriendProfileHandle(TIMFriendProfileHandle handle);
```

**参数说明：**
 
参数 | 说明
--- | ---
id | 用户列表 
num | 用户个数 
cb | 回调，返回 TIMFriendProfileHandle 数组，包含用户资料 

**属性说明：**
 
属性 | 说明
--- | ---
identifier | 好友的 identifer 
nickname | 好友昵称 
remark  | 好友备注 
allowType | 好友验证方式 

### 获取好友资料的部分字段 

可通过 `TIMGetPartialProfile` 方法获取部分好友的资料。

**原型：**

```
void TIMGetPartialProfile(char** id, uint32_t num, TIMGetProfileOptionHandle handle, TIMGetFriendProfileCallback* cb);
typedef enum _E_TIMProfileFlag
{
	TIM_PROFILE_FLAG_NONE			= 0x00,
	TIM_PROFILE_FLAG_NICK			= 0x01, //昵称
	TIM_PROFILE_FLAG_ALLOW_TYPE		= 0x01 << 1, //好友验证方式
	TIM_PROFILE_FLAG_FACE_URL       = 0x01 << 2, //头像
	TIM_PROFILE_FLAG_REMARK         = 0x01 << 3, //好友备注
	TIM_PROFILE_FLAG_GROUP			= 0x01 << 4, //好友分组
	TIM_PROFILE_FLAG_SELF_SIGNATURE = 0X01 << 5, //个性签名
	TIM_PROFILE_FLAG_GENDER			= 0x01 << 6,
	TIM_PROFILE_FLAG_BIRTHDAY		= 0x01 << 7,
	TIM_PROFILE_FLAG_LOCATION		= 0x01 << 8,
	TIM_PROFILE_FLAG_LANGUAGE		= 0x01 << 9,
}TIMProfileFlag;
typedef void* TIMGetProfileOptionHandle;
TIMGetProfileOptionHandle CreateGetProfileOptionHandle();
void DestroyGetProfileOptionHandle(TIMGetProfileOptionHandle handle);
void SetFlag4GetProfileOptionHandle(TIMGetProfileOptionHandle handle, TIMProfileFlag type);
void SetCustomInfo4GetProfileOptionHandle(TIMGetProfileOptionHandle handle, TIMProfileCustomInfoHandle custom_info);
```

**参数说明：**

| 参数 | 说明 |
| --- | --- |
| id | 用户列表 |
| num | 用户个数 |
| handle | 获取资料选项 |

**返回值：**

- 成功回调，返回 `TIMFriendProfileHandle` 数组，包含用户资料 
- 失败回调，会返回错误码和错误信息，详见错误码表 

**示例： **  

```
void DemoGetPartialProfile()
{
	char** members = new char*[DEMO_MEM_COUNT];
	members[0] = "user1";
	members[1] = "user2";
	TIMGetProfileOptionHandle opt = CreateGetProfileOptionHandle();
	SetFlag4GetProfileOptionHandle(opt, TIMProfileFlag(TIM_GET_PROFILE_Nick | TIM_GET_PROFILE_FaceUrl));
	TIMProfileCustomInfoElemHandle custom_elem = CreateProfileCustomInfoElemHandle();
	char* key = "my_key";
	SetKey4ProfileCustomInfoElemHandle(custom_elem, key, strlen(key)); // 设置查询 key 为“my_key”的 profile 自定义字段
	TIMProfileCustomInfoHandle custom_info = CreateProfileCustomInfoHandle();
	SetProfileCustomInfo(custom_info, &custom_elem, 1);
	SetCustomInfo4SetProfileOptionHandle(opt, custom_info);
	TIMGetFriendProfileCallback callback;
	callback.OnSuccess = CBGetFriendProfileCallbackOnSuccessImp;
	callback.OnError = CBGetFriendProfileCallbackOnErrorImp;
	TIMGetPartialProfile(members, 2, opt, &callback);
	//wait for callback
	SLEEP(1);
	DestroyProfileCustomInfoHandle(custom_info);
	DestroyProfileCustomInfoElemHandle(custom_elem);
	DestroyGetProfileOptionHandle(opt);
}
void CBGetFriendProfileCallbackOnSuccessImp(TIMFriendProfileHandle* handles, uint32_t num, void* data)
{
	char buf[BUF_LEN] = {0};
	for(uint32_ti = 0; i<num; i++)
	{
		auto handle = handles[i];
		uint32_t id_len = BUF_LEN; GetID4FriendProfileHandle(handle, buf, &id_len);printf("friend id: %s", buf);
		uint32_t nick_len = BUF_LEN; GetNickName4FriendProfileHandle(handle, buf, &nick_len);printf("nick name: %s", buf);
	}
}
void CBGetFriendProfileCallbackOnErrorImp(int code, const char* desc, void* data)
{
	printf("CBGetFriendProfileCallbackOnErrorImp Error! code = <%d> desc = <%s>", code, desc);
}
```

## 关系链相关资料

### 好友备注
 
可通过 `TIMSetFriendRemark` 方法设置好友备注，**需要注意好友备注必须先加为好友才可设置备注**。

```
/**
Description:	设置好友备注
@param	[in]	id		好友 ID	
@param	[in]	remark	备注	
@param	[in]	remark_len	备注长度
@param	[in]	cb			回调
@return			void
@exception      none
*/
TIM_DECL void TIMSetFriendRemark(const char* id, const char* remark, const uint32_t remark_len, TIMCommCB * cb);
```

**参数说明：**
 
参数 | 说明
--- | ---
id | 要设置备注的好友标识 
remark | 要设置的备注 
remark_len | 备注长度
cb | 回调 

## 好友关系

### 添加好友
 
通过 `TIMFriendshipManager` 的 `AddFriend` 方法可以批量添加好友，开发者可根据对应情况提示用户。 目前所能支持的最大好友列表为 3000 个。

**原型： ** 

```
/**
Description:	批量添加好友
@param	[in]	handles		添加好友 handle 数组
@param	[in]	num			添加好友个数
@param	[in]	cb			回调
@return           void
@exception        none
*/
TIM_DECL void TIMAddFriend(TIMAddFriendHandle* handles, uint32_t num, TIMAddFriendCallback * cb);
typedef void* TIMAddFriendHandle;
TIMAddFriendHandleCreateAddFriendHandle();
void DestroyAddFriendHandle(TIMAddFriendHandle handle);
TIM_DECL void SetID4AddFriendHandle(TIMAddFriendHandle handle, char* id);
//用户昵称 最大 96 字节
TIM_DECL void SetNickName4AddFriendHandle(TIMAddFriendHandle handle, char* nick_name, uint32_t len);
//好友备注 最大 120 字节
TIM_DECL void SetRemark4AddFriendHandle(TIMAddFriendHandle handle, char* remark, uint32_t len);
//好友来源
TIM_DECL void SetAddSource4AddFriendHandle(TIMAddFriendHandle handle, char* source);
//加好友 wording
TIM_DECL void SetAddWord4AddFriendHandle(TIMAddFriendHandle handle, char* word, uint32_t len);
```

**参数说明： **

参数 | 说明
--- | ---
handles | TIMAddFriendHandle 数组 
num | 添加用户个数
cb | 回调，返回 TIMFriendResult\* 数组，包含用户添加结果 

**属性说明：**
 
属性 | 说明
--- | ---
id | 用户标识 
remard | 添加成功后给用户的备注信息，最大 96 字节。 
addWording | 添加请求说明，最大 120 字节，如果用户设置为添加好友需要审核，对方会收到此信息并决定是否通过。 
addSource | 添加来源，固定字串，在页面上申请，留空表示未知来源。 

**返回码说明：**
 
成功回调会返回操作用户的 `TIMFriendResultHandle` 结果数据，添加好友的错误码如下。

```
//操作成功
#defineTIM_FRIEND_STATUS_SUCC	0 
//被加好友在自己的黑名单中
#define TIM_ADD_FRIEND_STATUS_IN_SELF_BLACK_LIST		30515 
//被加好友设置为禁止加好友
#define TIM_ADD_FRIEND_STATUS_FRIEND_SIDE_FORBID_ADD	30516
//好友数量已满
#define TIM_ADD_FRIEND_STATUS_SELF_FRIEND_FULL			30519
//已经是好友
#define TIM_ADD_FRIEND_STATUS_ALREADY_FRIEND				30520
//已被被添加好友设置为黑名单
#define TIM_ADD_FRIEND_STATUS_IN_OTHER_SIDE_BLACK_LIST	30525
//等待好友审核同意
#define TIM_ADD_FRIEND_STATUS_PENDING						30539
```

### 删除好友
 
可通过 `TIMFriendshipManager` 的 `DelFriend` 方法可以批量删除好友，开发者可根据情况提示用户。 

**原型：**

```
/**
Description:	删除好友
@param	[in]	type	删除类型（单向好友、双向好友）
@param	[in]	id		要删除的好友 ID 数组
@param	[in]	num		删除的好友个数
@param	[in]	cb		回调
@return			void
@exception      none
*/
TIM_DECL void TIMDelFriend(int type, char** id, uint32_t num, TIMDelFriendCallback * cb);
```

**参数说明：**

参数|说明
---|---
type | 删除类型，可选择删除双向好友或者单向好友 1-单向好友 2-双向好友 
id | 要删除的用户 ID 
cb | 回调：返回 TIMFriendResultHandle 数组，包含用户添加结果 

**返回码说明：**
 
成功回调会返回操作用户的 `TIMFriendResultHandle` 结果数据，删除好友的错误码如下。

```
//操作成功
#define TIM_FRIEND_STATUS_SUCC				0 
//删除好友时对方不是好友
#define TIM_DEL_FRIEND_STATUS_NO_FRIEND	30515 
```

### 获取所有好友
 
可通过 `TIMGetFriendList` 方法可以获取所有好友，默认只拉取基本资料，如果只需要个别字段或者自定义字段，可以使用 [按照字段获取用户资料](#.E6.8C.89.E7.85.A7.E5.AD.97.E6.AE.B5.E8.8E.B7.E5.8F.96.E7.94.A8.E6.88.B7.E8.B5.84.E6.96.99) 方法设置，此方法全局有效。

**原型：**

```
/**
Description:	获取所有好友
@param	[in]	cb	回调
@return			void
@exception      none
*/
TIM_DECL void TIMGetFriendList(TIMGetFriendListCallback * cb);
typedef void (*CBGetFriendListCallbackOnSuccess) (TIMFriendListElemHandle* handles, uint32_t num, void* data);
typedef void (*CBGetFriendListCallbackOnError) (int code, const char* desc, void* data);
typedef struct _T_TIMGetFriendListCallback
{
	CBGetFriendListCallbackOnSuccessOnSuccess;
	CBGetFriendListCallbackOnErrorOnError;
	void* data;
}TIMGetFriendListCallback;
```

**参数说明：**

参数|说明
---|---
cb | 回调：返回好友列表 TIMFriendListElemHandle 数组，只包含 identifier，nickname，remark 三个属性 

**`TIMFriendListElemHandle` 属性说明：**

>注：其他属性需要通过拉取好友的详细资料获得。 

默认属性|说明
---|---
identifier | 自己的用户标识 
nickname | 自己的昵称 
remark | 用户备注 

### 同意/拒绝 好友申请
 
可通过 `TIMFriendResponse` 方法可以获取所有好友，开发者可根据情况提示用户。

**原型： **

```
/**
Description:	同意/拒绝 好友申请
@param	[in]	handles	TIMFriendResponseHandle 数组
@param	[in]	num		数组元素个数
@param	[in]	cb		回调
@return			void
@exception      none
*/
TIM_DECL void TIMFriendResponse(TIMFriendResponseHandle* handles, uint32_t num, TIMFriendResponseCallback * cb);
typedef void* TIMFriendResponseHandle;
	//用户 ID
voidSetID4FriendResponseHandle(TIMFriendResponseHandle handle, char* id);
	//响应类型
voidSetResponseType4FriendResponseHandle(TIMFriendResponseHandle handle, E_TIMFriendResponseType type);
typedef enum_E_TIMFriendResponseType
{
TIM_FRIEND_RESPONSE_AGREE				= 0,//同意加好友（建立单向好友）
TIM_FRIEND_RESPONSE_AGREE_AND_ADD		= 1,//同意加好友并加对方为好友（建立双向好友）
TIM_FRIEND_RESPONSE_REJECT				= 2,//拒绝对方好友请求
}E_TIMFriendResponseType;
typedef void (*CBFriendResponseCallbackOnSuccess) (TIMFriendResultHandle* handles, uint32_t num, void* data);
typedef void (*CBFriendResponseCallbackOnError) (intcode, constchar* desc, void* data);
typedef struct_T_TIMFriendResponseCallback
{
	CBFriendResponseCallbackOnSuccessOnSuccess;
	CBFriendResponseCallbackOnErrorOnError;
	void* data;
}TIMFriendResponseCallback; 
```

**参数说明：**

参数|说明
---|---
handles|响应的用户列表，TIMFriendResponseHandle 数组 
num | 响应个数
cb | 回调，返回 TIMFriendResultHandle 数组 

**属性说明：**

属性|说明
---|---
id | 用户 ID
type | 响应类型 0-同意（单向） 1-同意并加对方（双想） 2-拒绝

**返回码说明：**
 
成功回调会返回操作用户的 `TIMFriendResultHandle` 结果数据，处理用户请求的错误码如下。

```
//操作成功
#define TIM_FRIEND_STATUS_SUCC									0
//响应好友申请时有效：对方没有申请过好友
#define TIM_RESPONSE_FRIEND_STATUS_NO_REQ                  30614
//响应好友申请时有效：自己的好友满
#define TIM_RESPONSE_FRIEND_STATUS_SELF_FRIEND_FULL		30615
//响应好友申请时有效：好友已经存在
#define TIM_RESPONSE_FRIEND_STATUS_FRIEND_EXIST				30617
//响应好友申请时有效：对方好友满
#define TIM_RESPONSE_FRIEND_STATUS_OTHER_SIDE_FRIEND_FULL30630
```

### 添加用户到黑名单

可以把任意用户拉黑，如果此前是好友关系，拉黑后自动解除好友，拉黑后对方发消息无法收到。

**原型： **

```
/**参数|说明
---|---
Description:	添加用户到黑名单
@param	[in]	id	用户 ID 数组
@param	[in]	num	用户数
@param	[in]	cb	回调
@return			void
@exception      none
*/
·TIM_DECL void TIMAddBlackList(const char** id, uint32_t num, TIMFriendshipActionCB * cb);
```

**参数说明：**

参数|说明
---|---
id|用户 ID 数组
num|用户数
cb|回调


### 把用户从黑名单删除

**原型： **

```
/**
Description:	把用户从黑名单删除
@param	[in]	id	用户 ID 数组
@param	[in]	num	用户个数
@param	[in]	cb	回调
@return			void
@exception      none
*/
TIM_DECL void TIMDelBlackList(const char** id, uint32_t num, TIMFriendshipActionCB * cb);
```

**参数说明：**

参数|说明
---|---
id|用户 ID 数组
num|用户数
cb|回调

### 获取黑名单列表

**原型： **

```
/**
Description:	获取黑名单列表
@param	[in]	cb	回调
@return			void
@exception      none
*/
TIM_DECL void TIMGetBlackList(TIMFriendshipActionCB * cb);
```

**参数说明：**

参数|说明
---|---
cb|回调

## 好友分组

### 创建好友分组

创建分组时，可以同时指定添加的用户，同一用户可以添加到多个分组。

**原型：**

```
/**
Description:	创建好友分组
@param	[in]	handle		好友分组名称列表
@param	[in]	friend_ids	好友 ID 数组
@param	[in]	friend_num	好友个数
@param	[in]	cb			回调
@return			void
@exception      none
*/
TIM_DECL void TIMCreateFriendGroup(TIMFriendGroupNamesHandle handle, const char** friend_ids, uint32_t friend_num, TIMAddFriendGroupCallback* cb);

typedef void* TIMFriendGroupNamesHandle;
TIM_DECL TIMFriendGroupNamesHandle CreateFriendGroupNamesHandle();
TIM_DECL void DestroyFriendGroupNamesHandle(TIMFriendGroupNamesHandle handle);
TIM_DECL void AddGroupNameforFriendGroupNamesHandle(TIMFriendGroupNamesHandle handle, const char* name, uint32_t len);
```

**参数说明：**

参数 | 说明
--- | ---
handle | 分组名称列表，必须是不存在的分组
friend_ids | 要添加分组中的用户列表
friend_num | 分组中的用户个数
cb | 回调

### 删除好友分组

**原型：**

```
/**
Description:	删除好友分组
@param	[in]	handle	好友分组名称列表
@param	[in]	cb		回调
@return			void
@exception      none
*/
TIM_DECL void TIMDeleteFriendGroup(TIMFriendGroupNamesHandle handle, TIMCommCB * cb);
```

**参数说明：**

参数 | 说明
--- | ---
handle | 要删除的分组名称
cb| 回调

### 添加好友到某分组

**原型：**

```
/**
Description:	添加好友到某分组
@param	[in]	group_name	好友分组名称
@param	[in]	name_len	好友分组名长度
@param	[in]	friend_ids  要添加到分组中的好友ID数组
@param	[in]	friend_num	要添加到分组中的好友个数
@param	[in]	cb			回调
@return			void
@exception      none
*/
TIM_DECL void TIMAddFriends2Group(const char* group_name, uint32_t name_len, const char** friend_ids, uint32_t friend_num, TIMAddFriends2GroupCallback* cb);
	
typedef void(*CBAddFriends2GroupCallbackOnSuccess) (TIMFriendResultHandle* handles, uint32_t num, void* data);
typedef void(*CBAddFriends2GroupCallbackOnError) (int code, const char* desc, void* data);
typedef struct _T_TIMAddFriends2GroupCallback
{
	CBAddFriends2GroupCallbackOnSuccess OnSuccess;
	CBAddFriends2GroupCallbackOnError OnError;
	void* data;
}TIMAddFriends2GroupCallback;
```

**参数说明：**

参数|说明
---|---
group_name | 分组名称
name_len | 好友分组名长度
friend_ids | 要添加到分组中的好友 ID 数组
friend_num | 要添加到分组中的好友个数
cb | 回调

### 从某分组删除好友

**原型：**

```
/**
Description:	从分组中删除好友
@param	[in]	group_name	好友分组名称
@param	[in]	name_len	好友分组名长度
@param	[in]	friend_ids	要从分组中删除的好友 ID 数组
@param	[in]	friend_num	要从分组中删除的好友 ID 个数
@param	[in]	cb			回调
@return			void
@exception      none
*/
TIM_DECL void TIMDelFriendsFromGroup(const char* group_name, uint32_t name_len, const char** friend_ids, uint32_t friend_num, TIMDelFriendsFromGroupCallback* cb);
```

**参数说明：**

参数 | 说明
--- | ---
group_name | 好友分组名称
name_len | 好友分组名长度
friend_ids |  要从分组删除的好友列表
friend_num |  要从分组中删除的好友 ID 个数
cb | 回调

### 重命名好友分组

**原型：**

```
/**
Description:	重命名好友分组
@param	[in]	old_name		原来的分组名
@param	[in]	old_name_len	原来的分组名长度
@param	[in]	new_name		新的分组名
@param	[in]	new_name_len	新的分组名长度
@param	[in]	cb				回调
@return			void
@exception      none
*/
TIM_DECL void TIMRenameFriendGroup(const char* old_name, uint32_t old_name_len, const char* new_name, uint32_t new_name_len, TIMCommCB * cb);
```

**参数说明：**

参数 | 说明
--- | ---
old_name | 原来的分组名
old_name_len |  原来的分组名长度
new_name | 新的分组名
new_name_len |  新的分组名长度
cb | 回调

### 获取指定的好友分组信息

**原型：**

```
/**
Description:	获取指定的好友分组信息
@param	[in]	handle			好友分组名称列表
@param	[in]	need_get_id_list 是否需要获取好友列表
@param	[in]	cb				回调
@return			void
@exception      none
*/
TIM_DECL void TIMGetFriendGroup(TIMFriendGroupNamesHandle handle, bool need_get_id_list, TIMGetFriendsGroupGroupCallback* cb);
```

**参数说明：**

参数 | 说明
--- | ---
handle | 要获取的分组好友名称，传入 NULL 获取所有分组信息
cb | 回调

## 关系链资料存储

在 1.9 版本之前，ImSDK 不会对关系链和消息进行存储和缓存，调用异步接口每次都会从 Server 拉取，1.9 版本之后，新增存储模块，用户可以不对资料和关系链进行存储，并且提供了内存同步访问接口，减少开发者调用负担。

### 开启存储

为了兼容老版本，避免老版本开发者和 ImSDK 都存储数据，默认情况下行为跟 1.9 版本一致，不会进行存储，需要用户显示调用开启存储。

**原型：**

```
/**
Description:	开启存储
@return			void
@exception      none
*/
void TIMEnableFriendshipProxy();
```

### 内存中同步获取关系链资料数据

**原型：**

```
/**
Description:	内存中同步获取关系链资料数据
@param	[in/out]	handles profile handle 数组
@param	[in/out]	num	获取个数
@return			int
@exception      none
*/
int TIMFriendProxyGetFriendList(TIMProfileHandle* handles, uint32_t* num);
```

### 好友、资料变更回调

1.9 版本之前，必须通过系统消息来感知变更，这种方式需要用户解析消息内容，层次结构较深，在 1.9 版本之后，如果开启了存储的功能，可以用更加明显易用的回调感知变更。

```
typedef struct 
{
	CBOnProxyStatusChange onProxyStatusChange; //收到代理状态变更通知
	CBOnAddFriends onAddFriends;               //添加好友通知
	CBOnDelFriends onDelFriends;               //删除好友通知
	CBOnFriendProfileUpdate onFriendProfileUpdate; //好友资料更新通知
}TIMFriendshipPorxyListener;
/**
Description:	设置好友代理回调
@param	[in]	listener	回调
@return			void
@exception      none
*/
void TIMSetFriendshipProxyListener(TIMFriendshipPorxyListener* listener);
```

## 关系链变更系统通知 

`TIMMsgElemHandle` 中 `Elem` 类型 `kElemFriendChange` 为关系链变更系统消息。

**原型和属性：**

```
//关系链变更消息类型
typedef enum _E_TIM_SNS_SYSTEM_TYPE
{
		TIM_SNS_SYSTEM_ADD_FRIEND = 0x01,//添加好友系统通知
		TIM_SNS_SYSTEM_DEL_FRIEND = 0x02,//删除好友系统通知
		TIM_SNS_SYSTEM_ADD_FRIEND_REQ = 0x03,//好友申请系统通知
		TIM_SNS_SYSTEM_DEL_FRIEND_REQ = 0x04,//删除未决请求通知
}E_TIM_SNS_SYSTEM_TYPE;
typedef void* TIMMsgSNSChangeInfoHandle;
int GetID4SNSChangeInfoHandle(TIMMsgSNSChangeInfoHandle handle, char* id, uint32_t * len);
int GetNick4SNSChangeInfoHandle(TIMMsgSNSChangeInfoHandle handle, char* nick, uint32_t * len);
int GetAddWord4SNSChangeInfoHandle(TIMMsgSNSChangeInfoHandle handle, char* word, uint32_t * len);
int GetAddSource4SNSChangeInfoHandle(TIMMsgSNSChangeInfoHandle handle, char* source, uint32_t * len);
E_TIM_SNS_SYSTEM_TYPE GetType4SNSSystemElem(TIMMsgSNSSystemElemHandle handle);
uint32_t GetChangeInfoNum4SNSSystemElem(TIMMsgSNSSystemElemHandle handle);
int GetChangeInfo4SNSSystemElem(TIMMsgSNSSystemElemHandle elem_handle, TIMMsgSNSChangeInfoHandle* info_handle, uint32_t* num);
```

**元素属性说明：**

属性|说明
---|---
类型 | 变更消息子类型 E_TIM_SNS_SYSTEM_TYPE 
用户信息列表 | 信息列表 TIMMsgSNSChangeInfoHandle 数组 

**用户信息属性：**
 
属性|说明
---|---
ID | 用户 identifier 
AddWord | 申请理由 
AddSource | 申请来源，申请时填写，由系统页面分配的固定字串 
Nick | 用户昵称 

### 添加好友系统通知 

当两个用户成为好友时，两个用户均可收到添加好友系统消息。

**触发时机：**当自己的关系链变更，增加好友时，收到消息（如果已经是单向好友，关系链没有变更的一方不会收到）。

**参数说明：**
 
属性|说明
---|---
类型 | TIM_SNS_SYSTEM_ADD_FRIEND 
用户信息列表 | 成为好友的用户列表 

**用户信息属性说明：** 

属性|说明
---|---
ID | 用户 identifier 

### 删除好友系统通知 

当两个用户解除好友关系时，会收到删除好友系统消息。 

**触发时机：**当自己的关系链变更，删除好友时，收到消息（如果删除的是单向好友，关系链没有变更的一方不会收到） 

**属性说明：**
 
 属性|说明
---|---
类型 | TIM_SNS_SYSTEM_DEL_FRIEND 
用户信息列表 | 删除好友的用户列表 

**用户信息属性说明： **

属性|说明
---|---
ID | 用户 identifier 

### 好友申请系统通知 

当申请好友时对方需要验证，自己和对方会收到好友申请系统通知： 

**触发时机：**当申请好友时对方需要验证，自己和对方会收到好友申请系统通知，对方可选择同意或者拒绝，自己不能操作，只做信息同步之用。 

**参数说明：**
 
参数|说明
---|---
类型 | TIM_SNS_SYSTEM_ADD_FRIEND_REQ 
用户信息列表 | 申请的好友列表 

**用户信息属性说明： **

属性|说明
---|---
ID | 用户 identifier 
AddWord | 申请理由 
AddSource | 申请来源，申请时填写，由系统页面分配的固定字串 

### 删除未决请求通知 

**触发时机：**当申请对方为好友，申请审核通过后，自己会收到删除未决请求消息，表示之前的申请已经通过。 

**参数说明：**

参数|说明
---|---
类型 | TIM_SNS_SYSTEM_DEL_FRIEND_REQ 
用户信息列表 |删除未决请求的好友列表 

**用户信息属性说明： **

属性|说明
---|---
ID | 用户 identifier 

## 好友资料变更系统通知 

`TIMMsgElemHandle` 中 `Elem` 类型 `kElemProfileChange` 为关系链变更系统消息。

**原型：**

```
typedef enum _E_TIM_PROFILE_SYSTEM_TYPE
	{
  TIM_PROFILE_SYSTEM_FRIEND_PROFILE_CHANGE = 0x01,//好友资料变更
	}E_TIM_PROFILE_SYSTEM_TYPE;
E_TIM_PROFILE_SYSTEM_TYPE GetType4ProfileProfileSystemElemHandle(TIMMsgProfileSystemElemHandle handle);
int GetID4ProfileProfileSystemElemHandle(TIMMsgProfileSystemElemHandle handle, char* id, uint32_t* len);
in tGetNick4ProfileProfileSystemElemHandle(TIMMsgProfileSystemElemHandle handle, char* nick, uint32_t* len);
```

**属性说明：**

属性|说明
---|--- 
E_TIM_PROFILE_SYSTEM_TYPE |资料变更类型 
ID | 资料变更的用户 
Nick | 昵称变更，注意，如果昵称没有变更，为 NULL 

## 未决请求

未决请求即为等待处理的请求，比如设置了需要验证好友，对方申请时会有未决请求，如果同意或者拒绝这个申请，未决请求会变为已决。通过 `TIMGetFutureFriends` 方法可以从 Server 获取未决请求列表。

**原型：***

```
/**
Description:	未决请求和好友推荐拉取
@param	[in]	flag			获取的资料标识
@param	[in]	type			获取的类型，按位设置
@param	[in]	custom_handle	自定义字段，（尚未实现，填 NULL）
@param	[in]	meta			请求信息，参见TIMFriendFutureMetaHandle
@param	[in]	cb				回调
@return			void
@exception      none
*/
TIM_DECL void TIMGetFutureFriends(TIMProfileFlag flag, TIMFutureFriendType type, TIMProfileCustomInfoHandle custom_handle, TIMFriendFutureMetaHandle meta, TIMGetFriendFurtureListCallback* cb);
typedef void* TIMFriendFutureMetaHandle;
TIM_DECL TIMFriendFutureMetaHandle CreateFriendFutureMetaHandle();
TIM_DECL void DestroyFriendFutureMetaHandle(TIMFriendFutureMetaHandle handle);
TIM_DECL TIMFriendFutureMetaHandle CloneFriendFutureMetaHandle(TIMFriendFutureMetaHandle handle);
// req info
TIM_DECL void SetDirection4FriendFutureMetaHandle(TIMFriendFutureMetaHandle handle, TIMPageDirectionType type);
TIM_DECL void SetReqNum4FriendFutureMetaHandle(TIMFriendFutureMetaHandle handle, uint64_t reqnum);
```

**参数说明：**

参数|说明
---|---
flags | 获取的资料标志，详见 TIMProfileFlag
type | 获取的类型，按位设置
custom_handle | 自定义字段，如要获取填写
meta | 请求信息，参见 TIMFriendFutureMeta 定义
cb | 回调

## 昵称检索 

ImSDK 支持使用依照昵称模糊搜索用户，使用 TIMSearchNickName 实现。 

**原型：**

```
/**
Description:	通过昵称模糊搜索用户
@param	[in]	nick		要搜索的昵称关键字 
@param	[in]	nick_len	用户昵称长度
@param	[in]	page_idx	分页号
@param	[in]	num_perpage	每页用户数目
@param	[in]	cb			回调
@return			void
@exception      none
*/
TIM_DECL void TIMSearchNickName(const char* nick, uint32_t nick_len, uint64_t page_idx, uint64_t num_perpage, TIMFriendSearchNickNameCB* cb);
```

**参数说明：**

参数 | 说明
--- | ---
nick  | 要搜索的昵称关键字 
nick_len | 昵称长度
page_idx  |  分页号，从 0 开始 
num_perpage      | 每页的数量 
cb | 回调，返回搜索结果 