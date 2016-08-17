## 1 登录
用户登录腾讯后台服务器后才能正常收发消息，登录需要用户提供accountType、identifier、userSig等信息，具体含义可参阅[帐号集成文档](/doc/product/269/账号登录集成说明)。

>注意：如果此用户在其他终端被踢，登录将会失败，返回错误码（ERR_IMSDK_KICKED_BY_OTHERS：6208）。开发者必须进行登录错误码ERR_IMSDK_KICKED_BY_OTHERS的判断。关于被踢的详细描述，参见2.6 用户状态变更。
如果用户保存用户票据，可能会存在过期的情况，如果用户票据过期，login将会返回 70001 错误码，开发者可根据错误码进行票据更换。

登录为异步过程，通过回调函数返回是否成功，成功后方能进行后续操作。

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
sdkAppId | 用于标识接入SDK的应用Id，由腾讯分配。
user | 用户帐号：<br>accountType，帐号类型，由腾讯分配。<br>appIdAt3rd，使用自有帐号或腾讯开放帐号时，填写为与sdkAppId相同的字符串。<br>identifier，用户帐号。
userSig | userSig，用户帐号签名，由私钥加密获得，具体请参考帐号相关文档。
callback | 回调接口。

在自有帐号情况下：appidAt3rd字段与sdkAppId相同，其他字段sdkAppId、accountType、identifier、userSig填写相应内容。

**示例：**


```
// accountType 和 sdkAppId 通讯云管理平台分配
// identifier为用户名，userSig 为用户登录凭证
// appidAt3rd 在私有帐号情况下，填写与sdkAppId 一样
 
TIMUser user = new TIMUser();
user.setAccountType(accountType);
user.setAppIdAt3rd(appIdAt3rd);
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
 
                //错误码code和错误描述desc，可用于定位请求失败原因
                //错误码code含义请参见错误码表
                Log.d(tag, "login failed. code: " + code + " errmsg: " + desc);
            }
});
```

## 2 登出

如用户主动注销或需要进行用户的切换，则需要调用注销操作：

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
 
        //错误码code和错误描述desc，可用于定位请求失败原因
        //错误码code列表请参见错误码表
        Log.d(tag, "logout failed. code: " + code + " errmsg: " + desc);
    }
 
    @Override
    public void onSuccess() {
        //登出成功
    }
});
```

## 3 无网络情况下查看消息

如用当前网络异常，或者想在不调用login的时候查看用户消息，可调用initStorage方法初始化存储，完成后可获取会话列表和消息：

**原型：**

```
public void initStorage(int sdkAppId,
               TIMUser user,
               java.lang.String userSig,
               TIMCallBack cb)
```

初始化存储，仅查看历史消息时使用，如果要收发消息等操作，如login成功，不需要调用此函数。


**参数说明：**

参数|说明
---|---
sdkAppId | 用于标识接入SDK的应用Id，由腾讯分配。
user | 用户帐号：<br>accountType，帐号类型，由腾讯分配。<br>appIdAt3rd，使用自有帐号或腾讯开放帐号时，填写为与sdkAppId相同的字符串。<br>identifier，用户帐号。
userSig | 用户帐号签名，由私钥加密获得，这里可以不填。
cb | 回调接口。

**示例：**


```
// accountType 和 sdkAppId 通讯云管理平台分配
// identifier为用户名，userSig 为用户登录凭证
// appidAt3rd 在私有帐号情况下，填写与sdkAppId 一样
 
TIMUser user = new TIMUser();
user.setAccountType(accountType);
user.setAppIdAt3rd(appIdAt3rd);
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
 
                //错误码code和错误描述desc，可用于定位请求失败原因
                //错误码code含义请参见错误码表
                Log.d(tag, "init failed. code: " + code + " errmsg: " + desc);
            }
});
```

示例中初始化存储，成功后可获取会话列表。

## 4 获取当前登录用户
通过TIMManager成员方法getLoginUser可以获取当前用户名，也可以通过这个方法判断是否已经登陆。

**原型：**

```
public String getLoginUser()
```
获取当前登陆的用户。

>说明：
返回值为当前登陆的用户名，需要注意的是，如果是自有账号登陆，用户名与登陆所传入的identifier相同，如果是第三方账号，如微信登陆，QQ登陆等，登陆后会有内部转换过的identifer，后续搜索好友，入群等，都需要使用转换后的identifier操作。

## 5 ImSDK同步离线消息

ImSDK 启动后会同步离线消息和最近联系人，最近联系人可通过接口禁用： [禁用最近联系人](/doc/product/269/消息收发（iOS%20SDK）#4.2-.E6.9C.80.E8.BF.91.E8.81.94.E7.B3.BB.E4.BA.BA.E6.BC.AB.E6.B8.B8) 。如果不需要离线消息，可以再发消息时使用：[发送在线消息](/doc/product/269/消息收发（iOS%20SDK）#1.11-.E5.9C.A8.E7.BA.BF.E6.B6.88.E6.81.AF)。

默认登陆后会异步获取离线消息以及同步资料数据（如果有开启ImSDK存储，可参见关系链资料章节），同步完成后会通过onRefresh回调通知更新界面，用户得到这个消息时，可以刷新界面，比如会话列表的未读等等：

**原型：**

```
public void setRefreshListener(TIMRefreshListener listener)
```
设置数据刷新通知监听器。

**参数说明：**

参数|说明
---|---
listener|数据刷新通知监听器。
