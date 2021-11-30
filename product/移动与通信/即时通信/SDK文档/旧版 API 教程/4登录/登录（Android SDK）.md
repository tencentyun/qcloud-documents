## 登录
用户登录腾讯后台服务器后才能正常收发消息，登录需要用户提供 `UserID`、`UserSig` 等信息，具体含义可参阅 [登录鉴权](https://cloud.tencent.com/document/product/269/31999) 。

>!
>- 如果此用户在其他终端被踢，登录将会失败，返回错误码（`ERR_IMSDK_KICKED_BY_OTHERS：6208`）。开发者必须进行登录错误码 `ERR_IMSDK_KICKED_BY_OTHERS` 的判断。关于被踢的详细描述，请参考 [用户状态变更](https://cloud.tencent.com/document/product/269/9229#.E7.94.A8.E6.88.B7.E7.8A.B6.E6.80.81.E5.8F.98.E6.9B.B4)。
>- 如果用户保存用户票据，可能会存在过期的情况，如果用户票据过期，`login` 将会返回 `70001` 错误码，开发者可根据错误码进行票据更换。

登录为异步过程，通过回调函数返回是否成功，成功后方能进行后续操作。

**原型：**

```
/** 登录
 * @param identifier 用户帐号
 * @param userSig userSig，用户帐号签名，由私钥加密获得，具体请参考文档
 * @param callback 回调接口
 */
public void login(@NonNull String identifier, @NonNull String userSig, @NonNull TIMCallBack callback)
```

**示例：**

```
// identifier 为用户名，userSig 为用户登录凭证
TIMManager.getInstance().login(identifier, userSig, new TIMCallBack() {
	@Override
	public void onError(int code, String desc) {
		//错误码 code 和错误描述 desc，可用于定位请求失败原因
		//错误码 code 列表请参见错误码表
		Log.d(tag, "login failed. code: " + code + " errmsg: " + desc);
	}

	@Override
	public void onSuccess() {
		Log.d(tag, "login succ");
	}
});
```

## 登出

如用户主动注销或需要进行用户的切换，则需要调用注销操作。

**原型：**

```
/**
 * 注销
 * @param callback 回调，不需要可以填 null
 */
public void logout(@Nullable TIMCallBack callback) 
```

**示例：**


```
//登出
TIMManager.getInstance().logout(new TIMCallBack() {
    @Override
    public void onError(int code, String desc) {
 
        //错误码 code 和错误描述 desc，可用于定位请求失败原因
        //错误码 code 列表请参见错误码表
        Log.d(tag, "logout failed. code: " + code + " errmsg: " + desc);
    }
 
    @Override
    public void onSuccess() {
        //登出成功
    }
});
```

## 无网络情况下查看消息

如用当前网络异常，或者想在不调用 `login` 的时候查看用户消息，可调用 `TIMManager` 中的 `initStorage` 方法初始化存储，完成后可获取会话列表和消息。

>!
> * 这个方法仅供登录失败或者没有网络的情况下查看历史消息使用，**如需要收发消息，请务必调用登录接口 `login`**。
> * 如果登录成功，IM SDK 会自动初始化本地存储，无需手动调用这个接口。

**原型：**

```
/** 初始化本地存储，可以在无网络情况下加载本地会话和消息
 * @param identifier 用户 ID
 * @param cb 回调
 */
public int initStorage(@NonNull String identifier, @NonNull TIMCallBack cb) 
```

以下示例中初始化存储，成功后可获取会话列表。

**示例：**

```
//初始化本地存储
TIMManager.getInstance().initStorage(identifier, new TIMCallBack() {
	@Override
	public void onError(int code, String desc) {
		Log.e(tag, "initStorage failed, code: " + code + "|descr: " + desc);
	}

	@Override
	public void onSuccess() {
		Log.i(tag, "initStorage succ");
	}
});

//获取会话实例
TIMConversation conversation = TIMManager.getInstance().getConversation(TIMConversationType.C2C, peer);
//获取本地消息
conversation.getLocalMessage(5, null, new TIMValueCallBack<List<TIMMessage>>() {
	@Override
	public void onError(int code, String desc) {
		Log.e(tag, "get msgs failed, code: " + code + "|msg: " + desc);
	}

	@Override
	public void onSuccess(List<TIMMessage> timMessages) {
		Log.i(tag, "get msgs succ, size: " + timMessages.size());
	}
});
```

## 获取当前登录用户
通过 `TIMManager` 成员方法 `getLoginUser` 可以获取当前用户名，也可以通过这个方法判断是否已经登录。

**原型：**

```
public String getLoginUser()
```

>!返回值为当前登录的用户名，如果是自有帐号登录，用户名与登录所传入的 `identifier` 相同，如果是第三方帐号，例如微信登录，QQ 登录等，登录后会有内部转换过的 `identifier`，后续搜索好友，入群等，都需要使用转换后的 `identifier` 操作。


