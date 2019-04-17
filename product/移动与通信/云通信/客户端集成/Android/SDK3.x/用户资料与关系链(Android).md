
IM 通讯云提供了**用户资料托管**，App 开发者使用简单的接口就可实现用户资料存储功能。另外，为了方便不同用户定制化资料，也提供用户资料的自定义字段。

## 用户资料介绍

用户资料保存用户的信息（如昵称、头像等）。

## 设置自己的资料

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

通过 `profileMap` 可以一次设置多个字段，比如同时设置昵称和性别的代码如下：

```
HashMap<String, Object> profileMap = new HashMap<>();
profileMap.put(TIMUserProfile.TIM_PROFILE_TYPE_KEY_NICK, "我的昵称");
profileMap.put(TIMUserProfile.TIM_PROFILE_TYPE_KEY_GENDER, TIMFriendGenderType.Male.value());
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
| `TIM_PROFILE_TYPE_KEY_ALLOWTYPE`     | int         | 好友申请       |
| `TIM_PROFILE_TYPE_KEY_GENDER`        | int         | 性别           |
| `TIM_PROFILE_TYPE_KEY_BIRTHDAY`      | int         | 生日           |
| `TIM_PROFILE_TYPE_KEY_LOCATION`      | String      | 位置           |
| `TIM_PROFILE_TYPE_KEY_LANGUAGE`      | int         | 语言           |
| `TIM_PROFILE_TYPE_KEY_LEVEL`         | int         | 等级           |
| `TIM_PROFILE_TYPE_KEY_ROLE`          | int         | 角色           |
| `TIM_PROFILE_TYPE_KEY_SELFSIGNATURE` | String      | 签名           |
| `TIM_PROFILE_TYPE_KEY_CUSTOM_PREFIX` | String, int | 自定义字段前缀 |

自定义字段需要您加上我们的前缀。比如后台有一个自定义字段`Blood`，类型为整数，设置代码如下：

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


## 获取资料

### 获取自己的资料 

可通过 `TIMFriendshipManager` 的 `getSelfProfile` 方法获取用户自己的资料。

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
* 获取用户自定义信息
* @return 自定义信息 Map
*/
public Map<String, Long> getCustomInfoUint()

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

可通过 `TIMFriendshipManager` 的 `getUsersProfile` 方法获取好友的资料。该方法支持从缓存和后台两种方式获取：
- 当 `forceUpdate = true` 时，会强制从后台拉取数据，并把返回的数据缓存下来。
- 当 `forceUpdate = NO` 时，则先在本地查找，如果本地没有数据则再向后台请求数据。
 建议只在显示资料时强制拉取，以减少等待时间。

**原型：**

```
/**
 * 获取指定好友资料（不包括：备注，好友分组）
 * @param users 要获取资料的用户 identifier 列表
 * @param forceUpdate 强制从后台拉取
 * @param cb 回调，OnSuccess 函数的参数中返回包含相应用户的{@see TIMUserProfile}列表
 */
public void getUsersProfile(@NonNull List<String> users, boolean forceUpdate, @NonNull TIMValueCallBack<List<TIMUserProfile>> cb) 
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
	        Log.e(tag, "identifier: " + res.getIdentifier() + " nickName: " + res.getNickName() 
	        		+ " remark: " + res.getRemark());
		}
	}
});
```

缓存的时间可通过 `TIMFriendProfileOption` 的 `setExpiredSeconds` 接口设置，默认缓存时间一天。

```
TIMUserConfig config = new TIMUserConfig();
TIMFriendProfileOption timFriendProfileOption = new TIMFriendProfileOption();
timFriendProfileOption.setExpiredSeconds(60 * 60); // 1小时
config.setTIMFriendProfileOption(timFriendProfileOption);
TIMManager.getInstance().setUserConfig(config);
```

