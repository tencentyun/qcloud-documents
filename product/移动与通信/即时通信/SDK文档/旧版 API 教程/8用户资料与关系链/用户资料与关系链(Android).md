
即时通信 IM 提供了**用户资料托管**，App 开发者使用简单的接口就可实现用户资料存储功能。另外，为了方便不同用户定制化资料，也提供用户资料的自定义字段。

## 用户资料
### 获取自己的资料 

- 可通过 `TIMFriendshipManager` 的 `getSelfProfile` 方法获取服务器保存的用户自己的资料。
- 可通过  `TIMFriendshipManager` 的 `querySelfProfile` 方法获取本地保存的用户自己的资料。


**原型：**

```   
/**
 * 获取服务器保存的自己的资料
 * @param cb 回调，OnSuccess 函数的参数中返回包含相应自己的{@see TIMUserProfile}
 */
public void getSelfProfile(final @NonNull TIMValueCallBack<TIMUserProfile> cb)

/**
 * 获取本地保存的自己的资料，没有则返回 null
 *
 * @return TIMUserProfile
 */
public TIMUserProfile querySelfProfile()
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
 * @return 用户好友选项，见 TIMFriendAllowType 中常量
 */
public String getAllowType()

/**
 * 获取用户自定义信息
 * @return 自定义信息 Map
 */
public Map<String, byte[]> getCustomInfo()

/**
 * 获取用户自定义信息
 * @return 自定义信息 Map
 */
public Map<String, Long> getCustomInfoUint()

/**
 * 获取用户性别类型， 见TIMFriendGenderType中的常量定义
 * @return 用户性别类型
 */
public int getGender()

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
//获取服务器保存的自己的资料
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
					 + " allow: " + result.getAllowType());
	}
});

//获取本地保存的自己的资料
TIMUserProfile selfProfile = TIMFriendshipManager.getInstance().querySelfProfile();
```

### 获取指定用户的资料

可通过 `TIMFriendshipManager` 的 `getUsersProfile` 方法获取好友的资料。该方法支持从缓存和后台两种方式获取：
- 当 `forceUpdate = true` 时，会强制从后台拉取数据，并把返回的数据缓存下来。
- 当 `forceUpdate = false` 时，则先在本地查找，如果本地没有数据则再向后台请求数据。
   建议只在显示资料时强制拉取，以减少等待时间。

可通过  `TIMFriendshipManager` 的 `queryUserProfile` 方法通过返回值获取本地缓存的好友资料，没有则返回 `null`。

**原型：**

```
/**
 * 获取指定好友资料（不包括：备注，好友分组）
 * @param users 要获取资料的用户 identifier 列表
 * @param forceUpdate 强制从后台拉取
 * @param cb 回调，OnSuccess 函数的参数中返回包含相应用户的{@see TIMUserProfile}列表
 */
public void getUsersProfile(@NonNull List<String> users, boolean forceUpdate, @NonNull TIMValueCallBack<List<TIMUserProfile>> cb) 

/**
 * 获取本地好友资料（不包括：备注，好友分组），没有则返回 null
 * @param identifier
 * @return TIMUserProfile
 */
public TIMUserProfile queryUserProfile(String identifier)
```

**示例：**

```
//待获取用户资料的用户列表
List<String> users = new ArrayList<String>();
users.add("sample_user_1");
users.add("sample_user_2");

//获取用户资料
TIMFriendshipManager.getInstance().getUsersProfile(users, true, new TIMValueCallBack<List<TIMUserProfile>>(){
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
	        Log.e(tag, "identifier: " + res.getIdentifier() + " nickName: " + res.getNickName());
		}
	}
});

//获取本地缓存的用户资料
TIMUserProfile userProfile = TIMFriendshipManager.getInstance().queryUserProfile("sample_user_1");
```

`getUsersProfile` 接口缓存的时间可通过 `TIMFriendProfileOption` 的 `setExpiredSeconds` 接口设置，默认缓存时间一天。

```
TIMUserConfig config = new TIMUserConfig();
TIMFriendProfileOption timFriendProfileOption = new TIMFriendProfileOption();
timFriendProfileOption.setExpiredSeconds(60 * 60); // 1小时
config.setTIMFriendProfileOption(timFriendProfileOption);
TIMManager.getInstance().setUserConfig(config);
```

### 修改自己的资料

通过 `TIMFriendshipManager` 的 `modifySelfProfile` 方法可以对自己的资料（如昵称、头像、添加好友选项等）进行修改。

**原型：**

```
/**
 * 修改自己的资料信息
 * @param profileMap 需要修改的字段放在hashMap中, key值取TIMFriendshipManager中定义的常量:
 * TIMFriendshipManager.TIM_PROFILE_TYPE_KEY_XXX
 * @param cb 回调
 */
public void modifySelfProfile(@NonNull HashMap<String, Object> profileMap, @NonNull TIMCallBack cb)
```

通过 `profileMap` 可以一次设置多个字段，例如同时设置昵称和性别的代码如下：

```
HashMap<String, Object> profileMap = new HashMap<>();
profileMap.put(TIMUserProfile.TIM_PROFILE_TYPE_KEY_NICK, "我的昵称");
profileMap.put(TIMUserProfile.TIM_PROFILE_TYPE_KEY_GENDER, TIMFriendGenderType.GENDER_MALE);
profileMap.put(TIMUserProfile.TIM_PROFILE_TYPE_KEY_BIRTHDAY, 20190419);
TIMFriendshipManager.getInstance().modifySelfProfile(profileMap, new TIMCallBack() {
    @Override
    public void onError(int code, String desc) {
    	Log.e(tag, "modifySelfProfile failed: " + code + " desc" + desc);
    }

    @Override
    public void onSuccess() {
    	Log.e(tag, "modifySelfProfile success");
    }
});
```

设置不存在的键值可能会导致失败，在 `TIMUserProfile` 中定义了一些常用的键值：

| Key                                  | Value       | 说明           |
| ------------------------------------ | ----------- | -------------- |
| `TIM_PROFILE_TYPE_KEY_NICK`          | String      | 昵称           |
| `TIM_PROFILE_TYPE_KEY_FACEURL`       | String      | 头像           |
| `TIM_PROFILE_TYPE_KEY_ALLOWTYPE`     | String         | 好友申请       |
| `TIM_PROFILE_TYPE_KEY_GENDER`        | int         | 性别           |
| `TIM_PROFILE_TYPE_KEY_BIRTHDAY`      | int         | 生日           |
| `TIM_PROFILE_TYPE_KEY_LOCATION`      | String      | 位置           |
| `TIM_PROFILE_TYPE_KEY_LANGUAGE`      | int         | 语言           |
| `TIM_PROFILE_TYPE_KEY_LEVEL`         | int         | 等级           |
| `TIM_PROFILE_TYPE_KEY_ROLE`          | int         | 角色           |
| `TIM_PROFILE_TYPE_KEY_SELFSIGNATURE` | String      | 签名           |
| `TIM_PROFILE_TYPE_KEY_CUSTOM_PREFIX` | String, int | 自定义字段前缀 |

自定义字段需要您加上我们的前缀。例如后台有一个自定义字段`Blood`，类型为整数，设置代码如下：

```
HashMap<String, Object> profileMap = new HashMap<>();
profileMap.put(TIMUserProfile.TIM_PROFILE_TYPE_KEY_CUSTOM_PREFIX + "Blood", 1);
TIMFriendshipManager.getInstance().modifySelfProfile(profileMap, new TIMCallBack() {
    @Override
    public void onError(int code, String desc) {
    	Log.e(tag, "modifySelfProfile failed: " + code + " desc" + desc);
    }

    @Override
    public void onSuccess() {
    	Log.e(tag, "modifySelfProfile success");
    }
});
```

## 好友关系
### 获取所有好友
可通过 `TIMFriendshipManager` 的 `getFriendList` 方法获取所有好友列表。

```
/**
 * 获取好友列表
 * @param cb 回调 TIMFriend 列表
 */
public void getFriendList(@NonNull TIMValueCallBack<List<TIMFriend>> cb)
```
获取成功后返回好友列表，好友对象用 `TIMFriend` 存储，`TIMFriend` 的定义如下:
```
/**
 * 获取用户的 identifier
 * @return 用户的 identifier
 */
public String getIdentifier()

/**
 * 获取好友备注
 * @return 好友备注
 */
public String getRemark()

/**
 * 获取申请加好友的理由
 * @return 申请理由
 */
public String getAddWording()

/**
 * 获取申请加好友的来源
 * @return 申请来源
 */
public String getAddSource()

/**
 * 获取分组名称
 * @return 分组名称列表
 */
public List<String> getGroupNames()

/**
 * 获取好友自定义信息，key 值按照后台配置的字符串传入，不包括 TIM_FRIEND_PROFILE_TYPE_KEY_CUSTOM_PREFIX 前缀
 * @return 自定义信息 Map
 */
public Map<String, byte[]> getCustomInfo()

/**
 * 获取 uint 类型的好友自定义信息，key 值按照后台配置的字符串传入，不包括 
 * TIM_FRIEND_PROFILE_TYPE_KEY_CUSTOM_PREFIX 前缀
 * @return 自定义信息 Map
 */
public Map<String, byte[]> getCustomInfoUint()

/**
 * 获取好友资料
 * @return 用户资料
 */
public TIMUserProfile getTimUserProfile()()
```
示例代码
```
TIMFriendshipManager.getInstance().getFriendList(new TIMValueCallBack<List<TIMFriend>>() {
            @Override
            public void onError(int code, String desc) {
                QLog.e(TAG, "getFriendList err code = " + code);
            }

            @Override
            public void onSuccess(List<TIMFriend> timFriends) {
                StringBuilder stringBuilder = new StringBuilder();
                for (TIMFriend timFriend : timFriends){
                    stringBuilder.append(timFriend.toString());
                }
                QLog.i(TAG, "getFriendList success result = " + stringBuilder.toString());
            }
        });
```

### 修改好友

修改好友调用`modifyFriend`方法进行。与修改自己资料方法类似，可一次更新多个字段。
```
/**
 * 修改好友资料
 * @param identifier 好友标识
 * @param profileMap 修改的字段，见TIMFriend中的TIM_FRIEND_PROFILE_TYPE_KEY_XXX
 * @param cb 回调
 */
public void modifyFriend(@NonNull String identifier, @NonNull HashMap<String, Object> profileMap, @NonNull TIMCallBack cb)
```
设置不存在的键值可能会导致失败，后台定义了一些常用的键值

Key | Value  | 说明
--- | --- | --
TIM_FRIEND_PROFILE_TYPE_KEY_REMARK | String | 备注 
TIM_FRIEND_PROFILE_TYPE_KEY_GROUP | List< String > | 分组 
TIM_FRIEND_PROFILE_TYPE_KEY_CUSTOM_PREFIX | String、int | 自定义字段前缀

示例：设置好友『Android_002』的备注为『002 remark』 

```
String identifier = "Android_002";
HashMap<String, Object> hashMap = new HashMap<>();
hashMap.put(TIMFriend.TIM_FRIEND_PROFILE_TYPE_KEY_REMARK, "002 remark");
TIMFriendshipManager.getInstance().modifyFriend(identifier, hashMap, new TIMCallBack() {
            @Override
            public void onError(int i, String s) {
                Log.e(TAG, "modifyFriend err code = " + i + ", desc = " + s);
            }

            @Override
            public void onSuccess() {
                Log.i(TAG, "modifyFriend success");
            }
        });
```

>?修改好友自定义资料，需先通过 Server 配置关系链自定义字段，才能修改成功。

### 添加好友

通过 `TIMFriendshipManager` 的 `addFriend` 方法可以添加好友。 

```
/**
 * 添加好友
 * @param timFriendRequest 添加请求
 * @param cb 回调
 */
public void addFriend(@NonNull TIMFriendRequest timFriendRequest, @NonNull TIMValueCallBack<TIMFriendResult> cb)
```

加好友需要传入 request 参数，该参数类型定义如下：
```
/**
 *  用户 identifier
 */
private String identifier = "";

/**
 *  用户备注（备注最大96字节）
 */
private String remark = "";

/**
 *  请求说明（最大120字节）
 */
private String addWording = "";

/**
 *  添加来源
 *  来源不能超过8个字节，并且需要添加“AddSource_Type_”前缀
 */
private String addSource = "";

/**
 *  分组名
 */
private String friendGroup = "";

```

成功回调会返回操作用户的 `TIMFriendResult` 结果数据，开发者可根据对应情况提示用户。添加好友的返回码如下：

```
public class TIMFriendStatus {
    /**
     *  操作成功
     */
    public static final int TIM_FRIEND_STATUS_SUCC                            = 0;
		
		/**
     * 请求参数错误，请根据错误描述检查请求是否正确
     */
    public static final int TIM_FRIEND_PARAM_INVALID                          = 30001;
		
		/**
     *  加好友、响应好友时有效：自己的好友数已达系统上限
     */
    public static final int TIM_ADD_FRIEND_STATUS_SELF_FRIEND_FULL            = 30010;
		
		/**
     *  加好友、响应好友时有效：对方的好友数已达系统上限
     */
    public static final int TIM_ADD_FRIEND_STATUS_THEIR_FRIEND_FULL           = 30014;
		
    /**
     *  加好友时有效：被加好友在自己的黑名单中
     */
    public static final int TIM_ADD_FRIEND_STATUS_IN_SELF_BLACK_LIST          = 30515;
		
    /**
     *  加好友时有效：被加好友设置为禁止加好友
     */
    public static final int TIM_ADD_FRIEND_STATUS_FRIEND_SIDE_FORBID_ADD      = 30516;
		
    /**
     *  加好友时有效：已被被添加好友设置为黑名单
     */
    public static final int TIM_ADD_FRIEND_STATUS_IN_OTHER_SIDE_BLACK_LIST    = 30525;
    /**
     *  加好友时有效：等待好友审核同意
     */
    public static final int TIM_ADD_FRIEND_STATUS_PENDING                     = 30539;
};
```

示例代码

```
TIMFriendRequest timFriendRequest = new TIMFriendRequest("test_id");
timFriendRequest.setAddWording("it's me!");
timFriendRequest.setAddSource("android");
TIMFriendshipManager.getInstance().addFriend(timFriendRequest, new TIMValueCallBack<TIMFriendResult>() {
		@Override
		public void onError(int i, String s) {
				QLog.e(TAG, "addFriend err code = " + i + ", desc = " + s);
		}

		@Override
		public void onSuccess(TIMFriendResult timFriendResult) {
				QLog.i(TAG, "addFriend success result = " + timFriendResult.toString());
		}
});
```

### 删除好友

可通过 `TIMFriendshipManager` 的 `deleteFriends` 方法批量删除好友。 

```
/**
 * 删除好友
 * @param identifiers 好友列表
 * @param delFriendType 删除类型
 * @param cb 回调
 */
public void deleteFriends(@NonNull List<String> identifiers, @NonNull int delFriendType, @NonNull TIMValueCallBack<List<TIMFriendResult>> cb)
```

成功回调会返回操作用户的 `TIMFriendResult` 结果数据，开发者可根据情况提示用户。 删除好友的错误码如下：

```
public class TIMFriendStatus {
    /**
     *  操作成功
     */
    public static final int TIM_FRIEND_STATUS_SUCC             = 0;
    /**
     *  删除好友时有效：删除好友时对方不是好友
     */
    public static final int TIM_DEL_FRIEND_STATUS_NO_FRIEND    = 31704;
};
```

示例代码

```
List<String> identifiers = new ArrayList<>();
identifiers.add("test_id");
TIMFriendshipManager.getInstance().deleteFriends(identifiers, TIMDelFriendType.TIM_FRIEND_DEL_SINGLE, new TIMValueCallBack<List<TIMFriendResult>>() {
		@Override
		public void onError(int i, String s) {
				QLog.e(TAG, "deleteFriends err code = " + i + ", desc = " + s);
		}

		@Override
		public void onSuccess(List<TIMFriendResult> timUserProfiles) {
				QLog.i(TAG, "deleteFriends success");
		}
});
```

### 同意/拒绝好友申请

可通过 `TIMFriendshipManager` 的 `doResponse` 方法同意/拒绝好友申请

```
/**
 * 处理好友请求
 * @param response 请求参数，包含好友 ID，预备注，回应类型
 * @param cb
 */
public void doResponse(TIMFriendResponse response, @NonNull TIMValueCallBack<TIMFriendResult> cb)
```

参数 `response` 定义如下：
```
public class TIMFriendResponse {
    /**
     *  同意加好友（建立单向好友）
     */
    public static final int TIM_FRIEND_RESPONSE_AGREE = 0;

    /**
     *  同意加好友并加对方为好友（建立双向好友）
     */
    public static final int TIM_FRIEND_RESPONSE_AGREE_AND_ADD = 1;

    /**
     *  拒绝对方好友请求
     */
    public static final int TIM_FRIEND_RESPONSE_REJECT  = 2;

    /**
     * 响应类型
     */
    private int responseType = TIM_FRIEND_RESPONSE_AGREE;

    /**
     * 响应的好友 ID
     */
    private String identifier = ""; // 回应好友的 ID

    /**
     * 备注好友（可选，如果要加对方为好友）。备注最大96字节
     */
    private String remark = "";
    
    .......省略 get set 方法
}
```

成功回调会返回操作用户的 `TIMFriendResult` 结果数据，处理用户请求的错误码如下。
```
public class TIMFriendStatus {
    /**
     *  操作成功
     */
    public static final int TIM_FRIEND_STATUS_SUCC                    = 0;
		
    /**
     *  加好友、响应好友时有效：自己的好友数已达系统上限
     */
    public static final int TIM_ADD_FRIEND_STATUS_SELF_FRIEND_FULL    = 30010;
		
    /**
     *  加好友、响应好友时有效：对方的好友数已达系统上限
     */
    public static final int TIM_ADD_FRIEND_STATUS_THEIR_FRIEND_FULL   = 30014;
		
    /**
     *  响应好友申请时有效：对方没有申请过好友
     */
    public static final int TIM_RESPONSE_FRIEND_STATUS_NO_REQ         = 30614;
};
```

### 校验好友关系

可通过 `TIMFriendshipManager` 的 `checkFriends` 方法校验好友关系。

```
/**
 * 校验好友
 * @param checkInfo 校验好友参数
 * @param cb 回调
 */
public void checkFriends(@NonNull TIMFriendCheckInfo checkInfo, @NonNull TIMValueCallBack<List<TIMCheckFriendResult>> cb)
```

参数 `checkInfo` 定义如下：

```
public class TIMFriendCheckInfo {
	private List<String> users = new ArrayList<>();
    private int checkType = TIMFriendCheckType.TIM_FRIEND_CHECK_TYPE_UNIDIRECTION;
    
    /**
     * 设置需要检查的好友 ID
     *
     * @param users
     */
    public void setUsers(List<String> users);
    
    /**
     * 设置需要检查的关系类型，见 TIMFriendCheckType 定义的常量
     *
     * @param type
     */
    public void setCheckType(int type);
}
```

参数 `TIMFriendCheckType` 定义如下：

```
public class TIMFriendCheckType {
    /**
     * 单向好友
     */
    public static final int TIM_FRIEND_CHECK_TYPE_UNIDIRECTION     = 1;

    /**
     * 互为好友
     */
    public static final int TIM_FRIEND_CHECK_TYPE_BIDIRECTION      = 2;
}
```

成功回调会返回操作用户的 `TIMCheckFriendResult` 列表数据，定义如下。

```
public class TIMCheckFriendResult {
    private String identifier = "";
    private int resultCode;
    private String resultInfo = "";
    private int resultType;

    /**
     * 获取好友 ID
     *
     * @return 好友 ID
     */
    public String getIdentifier();

    /**
     * 获取返回码
     *
     * @return 返回码
     */
    public int getResultCode();

    /**
     * 获取返回结果描述
     *
     * @return 结果描述
     */
    public String getResultInfo();

    /**
     * 获取检查好友类型，常量见 TIMFriendRelationType 中定义
     *
     * @return 好友关系类型
     */
    public int getResultType();
}
```

参数 `TIMFriendRelationType` 定义如下：

```
public class TIMFriendRelationType {
    /**
     *  不是好友
     */
    public static final int TIM_FRIEND_RELATION_TYPE_NONE           = 0;

    /**
     *  对方在我的好友列表中
     */
    public static final int TIM_FRIEND_RELATION_TYPE_MY_UNI         = 1;

    /**
     *  我在对方的好友列表中
     */
    public static final int TIM_FRIEND_RELATION_TYPE_OTHER_UNI      = 2;

    /**
     *  互为好友
     */
    public static final int TIM_FRIEND_RELATION_TYPE_BOTH_WAY       = 3;

}
```






## 好友未决

### 获取未决列表
其它用户通过`addFriend`方法添加自己为好友，此时会在后台增加一条未决记录。当自己向其它用户请求好友时，后台也会记录一条未决信息。可通过`getPendencyList`方法获取未决列表
```
/**
 * 获取未决列表
 * 
 * @param timFriendPendencyRequest
 * @param cb
 */
public void getPendencyList(TIMFriendPendencyRequest timFriendPendencyRequest, @NonNull TIMValueCallBack<TIMFriendPendencyResponse> cb)
```

由于后台可能存储多条好未决，超出界面显示范围，所以此接口支持翻页操作。需要传入参数  `timFriendPendencyRequest` 定义如下：
```
/**
 * 未决列表序列号。建议客户端保存 seq 和未决列表，请求时填入 server 返回的 seq。如果 seq 是 server 最新的，则不返回数据
 * 
 * @param seq 序列号
 */
public void setSeq(long seq)

/**
 * 翻页时间戳，只用来翻页，server 返回0时表示没有更多数据，第一次请求填0
 * 特别注意的是，如果 server 返回的 seq 跟填入的 seq 不同，翻页过程中，需要使用客户端原始 seq 请求，直到数据请求完毕，才能更新本地 seq
 * 
 * @param timestamp 翻页时间戳
 */
public void setTimestamp(long timestamp)

/**
 * 每页的数量，请求时有效
 * 
 * @param numPerPage 每页的数量
 */
public void setNumPerPage(int numPerPage)

/**
 * 未决请求拉取类型，见 TIMPendencyType 中的常量定义
 * 
 * @param timPendencyType 未决请求拉取类型
 */
public void setTimPendencyGetType(int timPendencyType)
```

操作成功后，回调返回分页信息和未决记录 `TIMFriendPendencyResponse`
```
/**
 * 获取本次请求的未决列表序列号
 * @return 序列号
 */
public long getSeq()

/**
 * 获取本次请求的翻页时间戳
 * 
 * @return 时间戳
 */
public long getTimestamp()

/**
 * 获取未决请求未读数量
 * 
 * @return 未读数量
 */
public long getUnreadCnt()

/**
 * 获取未决信息列表
 * 
 * @return 信息列表
 */
public List<TIMFriendPendencyItem> getItems()
```

未决请求 `TIMFriendPendencyItem` 定义如下：

```
/**
 * 获取用户 ID
 * 
 * @return id
 */
public String getIdentifier()

/**
 * 获取增加时间
 * 
 * @return 时间
 */
public long getAddTime()

/**
 * 获取来源
 * 
 * @return 来源
 */
public String getAddSource()

/**
 * 获取好友附言
 * 
 * @return 附言
 */
public String getAddWording()

/**
 * 获取好友昵称
 * 
 * @return 昵称
 */
public String getNickname()

/**
 * 获取未决请求类型，见 TIMPendencyType 常量定义
 * 
 * @return 未决请求类型
 */
public int getType()
```

未决类型 `TIMPendencyType` 定义如下：
```
public class TIMPendencyType {
    /**
     * 别人发给我的未决请求
     */
    public static final int TIM_PENDENCY_COME_IN    = 1;

    /**
     * 我发给别人的未决请求
     */
    public static final int TIM_PENDENCY_SEND_OUT   = 2;

    /**
     * 别人发给我的以及我发给别人的所有未决请求，仅在拉取时有效。
     */
    public static final int TIM_PENDENCY_BOTH       = 3;

}
```


### 未决删除
```
/**
 * 未决删除
 * 
 * @param pendencyType 未决类型，见 TIMPendencyType, 删除只支持 TIM_PENDENCY_COME_IN 和 TIM_PENDENCY_SEND_OUT
 * @param users 要删除的未决用户 ID 列表
 * @param cb 回调
 */
public void deletePendency(int pendencyType, List<String> users, @NonNull TIMValueCallBack<List<TIMFriendResult>> cb)
```

### 未决已读上报
当用户拉取到未决记录，可以将本次拉取的未决在后台标记为已读。
```
/**
 * 未决已读上报
 * 
 * @param timestamp 已读时间戳，此时间戳以前的消息都将置为已读
 * @param cb 回调
 */
public void pendencyReport(long timestamp, @NonNull TIMCallBack cb)
```
上报后，下次调用`getPendencyList`返回的未读计数将会改变。

## 黑名单

### 添加用户到黑名单

可以把任意用户拉黑，如果此前是好友关系，拉黑后自动解除好友，拉黑后对方发消息无法收到。

```
/**
 * 添加用户到黑名单
 * 
 * @param users 用户列表
 * @param cb 回调
 */
public void addBlackList(List<String> users, @NonNull TIMValueCallBack<List<TIMFriendResult>> cb)
```

### 把用户从黑名单删除

```
/**
 * 把用户从黑名单中删除
 * 
 * @param users 用户列表
 * @param cb 回调
 */
public void deleteBlackList(List<String> users, @NonNull TIMValueCallBack<List<TIMFriendResult>> cb)
```

### 获取黑名单列表

```
/**
 * 获取黑名单列表
 * 
 * @param cb 回调
 */
public void getBlackList(@NonNull TIMValueCallBack<List<TIMFriend>> cb)
```

## 好友分组

### 创建好友分组

创建分组时，可以同时指定添加的用户。同一用户可以添加到多个分组。

```
/**
 * 新建好友分组
 * 
 * @param groupNames 分组名称列表,必须是当前不存在的分组
 * @param identifiers 要添加到分组中的好友
 * @param cb 回调
 */
public void createFriendGroup(List<String> groupNames, List<String> identifiers, @NonNull TIMValueCallBack<List<TIMFriendResult>> cb)
```

### 删除好友分组

```
/**
 * 删除好友分组
 * 
 * @param groupNames 要删除的好友分组名称列表
 * @param cb 回调
 */
public void deleteFriendGroup(List<String> groupNames, @NonNull TIMCallBack cb)
```

### 添加好友到某分组

```
/**
 * 添加好友到某分组
 *
 * @param groupName 好友分组名称
 * @param identifiers 要添加到分组中的好友列表
 * @param cb 回调
 */
public void addFriendsToFriendGroup(String groupName, List<String> identifiers, @NonNull TIMValueCallBack<List<TIMFriendResult>> cb)
```

### 从某分组删除好友

```
/**
 * 从某分组删除好友
 * 
 * @param groupName 好友分组名称
 * @param identifiers 要移除分组的好友列表
 * @param cb 回调
 */
public void deleteFriendsFromFriendGroup(String groupName, List<String> identifiers, @NonNull TIMValueCallBack<List<TIMFriendResult>> cb)
```

### 重命名好友分组

```
/**
 * 重命名好友分组
 * 
 * @param oldName 原来的分组名称
 * @param newName 新的分组名称
 * @param cb 回调
 */
public void renameFriendGroup(String oldName, String newName, @NonNull TIMCallBack cb)
```

### 获取好友分组

```
/**
 * 获取指定的好友分组，传入 null 获得所有分组信息
 * @param groupNames 要获取信息的好友分组名称列表
 * @param cb 回调
 */
public void getFriendGroups(List<String> groupNames, @NonNull TIMValueCallBack<List<TIMFriendGroup>> cb)
```

## 关系链变更系统通知

`TIMMessage` 中 `Elem` 类型 `TIMSNSSystemElem` 为关系链变更系统消息。

```
/**
 * 关系链相关操作后，后台 push 同步下来的消息元素
 *
 */
public class TIMSNSSystemElem extends TIMElem {
    private int subType = 0;
    
    // subType 对应 TIMSNSSystemType.TIM_SNS_SYSTEM_ADD_FRIEND
    private List<String> requestAddFriendUserList = new ArrayList<>();
    
    // subType 对应 TIMSNSSystemType.TIM_SNS_SYSTEM_DEL_FRIEND
    private List<String> delRequestAddFriendUserList = new ArrayList<>();
    
    // subType 对应 TIMSNSSystemType.TIM_SNS_SYSTEM_ADD_BLACKLIST
    private List<String> addBlacklistUserList = new ArrayList<>();
    
    // subType 对应 TIMSNSSystemType.TIM_SNS_SYSTEM_DEL_BLACKLIST
    private List<String> delBlacklistUserList = new ArrayList<>();

    // subType 对应 TIMSNSSystemType.TIM_SNS_SYSTEM_ADD_FRIEND_REQ
    private List<TIMFriendPendencyInfo> friendAddPendencyList = new ArrayList<>();
    
    // subType 对应 TIMSNSSystemType.TIM_SNS_SYSTEM_DEL_FRIEND_REQ
    private List<String> delFriendAddPendencyList = new ArrayList<>();
    
    // subType 对应 TIMSNSSystemType.TIM_SNS_SYSTEM_SNS_PROFILE_CHANGE
    private List<TIMSNSChangeInfo>  changeInfoList = new ArrayList<>();
		
    public TIMSNSSystemElem() { type = TIMElemType.SNSTips; }
    public int getSubType();	
    public List<String> getRequestAddFriendUserList();
    public List<String> getDelRequestAddFriendUserList();
    public List<String> getAddBlacklistUserList();
    public List<String> getDelBlacklistUserList();
    public List<TIMFriendPendencyInfo> getFriendAddPendencyList();
    public List<String> getDelFriendAddPendencyList();
    public List<TIMSNSChangeInfo> getChangeInfoList();
}


/**
 * 关系链变更系统通知类型
 */
public class TIMSNSSystemType {
    /**
     * 增加好友消息
     */
    public static final int TIM_SNS_SYSTEM_ADD_FRIEND         = 0x01;

    /**
     * 删除好友消息
     */
    public static final int TIM_SNS_SYSTEM_DEL_FRIEND         = 0x02;

    /**
     * 增加好友申请
     */
    public static final int TIM_SNS_SYSTEM_ADD_FRIEND_REQ     = 0x03;

    /**
     * 删除未决申请
     */
    public static final int TIM_SNS_SYSTEM_DEL_FRIEND_REQ     = 0x04;
		
		    /**
     * 黑名单添加
     */
    public static final int TIM_SNS_SYSTEM_ADD_BLACKLIST      = 0x05;

    /**
     * 黑名单删除
     */
    public static final int TIM_SNS_SYSTEM_DEL_BLACKLIST      = 0x06;

    /**
     *  未决已读上报
     */
    public static final int TIM_SNS_SYSTEM_PENDENCY_REPORT    = 0x07;

    /**
     *  关系链资料变更
     */
    public static final int TIM_SNS_SYSTEM_SNS_PROFILE_CHANGE = 0x08;
};

/**
 * 关系链变更详细信息
 *
 */
public class TIMSNSChangeInfo {
    /**
     * 变更资料的用户 ID
     */
    private String updateUser = "";

    /**
     * 变更资料信息
     */
    private Map<String, Object> itemMap = new HashMap<>();

    public String getUpdateUser() {
        return updateUser;
    }

    public Map<String, Object> getItemMap() {
        return itemMap;
    }
}
```

### 添加好友系统通知

当两个用户成为好友时，两个用户均可收到添加好友系统消息。

**触发时机：**

当自己的关系链变更，增加好友时，收到消息（如果已经是单向好友，关系链没有变更的一方不会收到）。

**参数说明：**

参数 | 说明
--- | ---
subType | TIM_SNS_SYSTEM_ADD_FRIEND 
requestAddFriendUserList | 成为好友的用户列表 

### 删除好友系统通知

当两个用户解除好友关系时，会收到删除好友系统消息： 

**触发时机：**

当自己的关系链变更，删除好友时，收到消息（如果删除的是单向好友，关系链没有变更的一方不会收到）。

**参数说明：**

参数 | 说明
--- | ---
subType | TIM_SNS_SYSTEM_DEL_FRIEND 
delRequestAddFriendUserList | 删除好友的用户列表 

### 好友申请系统通知

当申请好友时对方需要验证，自己和对方会收到好友申请系统通知。

**触发时机：**

当申请好友时对方需要验证，自己和对方会收到好友申请系统通知，对方可选择同意或者拒绝，自己不能操作，只做信息同步之用。 

**参数说明：**

参数 | 说明
--- | ---
subType | TIM_SNS_SYSTEM_ADD_FRIEND_REQ 
friendAddPendencyList | 申请的好友信息列表

**`TIMFriendPendencyInfo` 参数说明：**

参数 | 说明
--- | ---
fromUser |  添加好友操作者
addSource |  添加好友的来源 
fromUserNickName | 添加好友的操作者的昵称
addWording | 添加好友附言

### 删除未决请求通知

**触发时机：**

当申请对方为好友，申请审核通过或者被拒后，自己会收到删除未决请求消息。

**参数说明：**

参数 | 说明
--- | ---
subType | TIM_SNS_SYSTEM_DEL_FRIEND_REQ 
delFriendAddPendencyList | 被通过或者被拒绝的好友列表

## 用户资料变更系统通知

`TIMMessage` 中 `Elem` 类型 `TIMProfileSystemElem` 为用户资料变更系统消息。

```
/**
 * 自身和好友资料修改，后台 push 下来的消息元素
 */
public class TIMProfileSystemElem extends TIMElem {
    private int subType; //修改资料的类型 TIMProfileSystemType
    private String fromUser; //修改资料的来源（谁修改了）
    private Map<String, Object> itemMap; //用户的资料
  
    public int getSubType();
    public String getFromUser();
    public Map<String, Object> getItemMap();
}

/**
 * 用户资料变更系统通知类型
 */
public class TIMProfileSystemType {
    /**
     * 无效值
     */
    public static final int INVALID = 0;
    
    /**
     * 好友资料变更
     */
    public static final int TIM_PROFILE_SYSTEM_FRIEND_PROFILE_CHANGE = 1;
}

```

当自己的资料或者好友的资料变更时，会收到用户资料变更系统消息。例如好友修改了头像，那么 `TIMProfileSystemElem` 中的 `itemMap` 的 `key` 为`Tag_Profile_IM_Image` ， `value` 值为头像的 `url` 地址，其中 `key` 常量值定义在 `TIMUserProfile` 中。



