## 登录

用户登录腾讯后台服务器后才能正常收发消息，登录需要用户提供 `accountType`、`identifier`、`userSig` 等信息，具体含义可参阅 [帐号集成文档](/doc/product/269/帐号登录集成说明)。登录为异步过程，通过回调函数返回是否成功，成功后方能进行后续操作。

>**注意：**
>- 如果此用户在其他终端被踢，登录将会失败，返回错误码（`ERR_IMSDK_KICKED_BY_OTHERS：6208`）。开发者必须进行登录错误码 `ERR_IMSDK_KICKED_BY_OTHERS` 的判断。关于被踢的详细描述，参见 [用户状态变更](/doc/product/269/1559#.E7.94.A8.E6.88.B7.E7.8A.B6.E6.80.81.E5.8F.98.E6.9B.B4)。
>- 如果用户保存用户票据，可能会存在过期的情况，如果用户票据过期，`login` 将会返回 `70001` 错误码，开发者可根据错误码进行票据更换。

**原型：**

```
public void login(int sdkAppId,
         TIMUser user,
         java.lang.String userSig,
         TIMCallBack callback)
```

**参数说明：**

参数|说明
---|---
sdkAppId | 用于标识接入 SDK 的应用 ID，由腾讯分配。
user | 用户帐号：<br>accountType，帐号类型，由腾讯分配。<br>appIdAt3rd，使用自有帐号或腾讯开放帐号时，填写为与 sdkAppId 相同的字符串。<br>identifier，用户帐号。
userSig | userSig，用户帐号签名，由私钥加密获得，具体请参考帐号相关文档。
callback | 回调接口。

>注：在自有帐号情况下：`appidAt3rd` 字段与 `sdkAppId` 相同，其他字段 `sdkAppId`、`accountType`、`identifier`、`userSig` 填写相应内容。

**示例：**

```
// identifier 为用户名，userSig 为用户登录凭证
TIMUser user = new TIMUser();
user.setIdentifier(identifier);
//发起登录请求
TIMManager.getInstance().login(
        sdkAppId,                   //sdkAppId，由腾讯分配
        user,
        userSig,                    //用户帐号签名，由私钥加密获得，具体请参考文档
        new TIMCallBack() {//回调接口
 
            @Override
            public void onSuccess() {//登录成功
                Log.d(tag, "login succ");
            }
            @Override
            public void onError(int code, String desc) {//登录失败
 
                //错误码 code 和错误描述 desc，可用于定位请求失败原因
                //错误码 code 含义请参见错误码表
                Log.d(tag, "login failed. code: " + code + " errmsg: " + desc);
            }
});
```

## 登出

如用户主动注销或需要进行用户的切换，则需要调用注销操作。

**原型：**

```
// 登出
public void logout(TIMCallBack callback)
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

如用当前网络异常，或者想在不调用 `login` 的时候查看用户消息，可调用 `initStorage` 方法初始化存储，完成后可获取会话列表和消息。初始化存储在仅查看历史消息时使用，如 `login` 成功，则不需要调用此函数

**初始化存储原型：**

```
public void initStorage(int sdkAppId,
               TIMUser user,
               java.lang.String userSig,
               TIMCallBack cb)
```

**参数说明：**

参数|说明
---|---
sdkAppId | 用于标识接入 SDK 的应用 ID，由腾讯分配。
user | 用户帐号：identifier
userSig | 用户帐号签名，由私钥加密获得，这里可以不填。
cb | 回调接口。

初始化存储成功后可获取会话列表。**示例：**

```
// identifier 为用户名，userSig 为用户登录凭证
TIMUser user = new TIMUser();
user.setIdentifier(identifier);
//发起登录请求
TIMManager.getInstance().initStorage(
        sdkAppId,                   //sdkAppId，由腾讯分配
        user,
        userSig,                    //用户帐号签名，由私钥加密获得，具体请参考文档
        new TIMCallBack() {//回调接口
            @Override
            public void onSuccess() {//登录成功
                Log.d(tag, "init succ");
            }
            @Override
            public void onError(int code, String desc) {//登录失败
                //错误码 code 和错误描述 desc，可用于定位请求失败原因
                //错误码 code 含义请参见错误码表
                Log.d(tag, "init failed. code: " + code + " errmsg: " + desc);
            }
});
```



## 获取当前登录用户
通过 `TIMManager` 成员方法 `getLoginUser` 可以获取当前登录用户名，也可以通过这个方法判断是否已经登录。返回值为当前登录的用户名。

>**注意：**
>- 如果是自有帐号登录，用户名与登录所传入的 `identifier` 相同。
>- 如果是第三方帐号（如微信登录，QQ 登录等），登录后会有内部转换过的 `identifer`，后续搜索好友，入群等，都需要使用转换后的 `identifier` 操作。

**原型：**

```
public String getLoginUser()
```

## ImSDK 同步离线消息

ImSDK 启动后会同步离线消息和最近联系人，最近联系人可通过 [禁用最近联系人](/doc/product/269/消息收发（iOS%20SDK）#.E6.9C.80.E8.BF.91.E8.81.94.E7.B3.BB.E4.BA.BA.E6.BC.AB.E6.B8.B8) 接口禁用 。如果不需要离线消息，可以在发消息时使用 [发送在线消息](/doc/product/269/消息收发（iOS%20SDK）#.E5.9C.A8.E7.BA.BF.E6.B6.88.E6.81.AF)。

>注：默认登录后会异步获取离线消息以及同步资料数据（如果有开启 ImSDK 存储，可参见关系链资料章节），同步完成后会通过 `onRefresh` 回调通知更新界面，用户得到这个消息时，可以刷新界面（如会话列表的未读等）。

**设置数据刷新通知监听器原型：**

```
public void setRefreshListener(TIMRefreshListener listener)
```

**参数说明：**

参数|说明
---|---
listener|数据刷新通知监听器。
