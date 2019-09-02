## 集成微信登录


### 1. 注册应用

如果您还没有在 [微信开放平台](https://open.weixin.qq.com/cgi-bin/index?t=home/index&lang=zh_CN) 注册您的应用，请先移步注册您的应用，并且获取应用登录能力。

### 2. 配置应用

在您的应用模块的 assets 文件夹下，新建一个名为 tac\_service\_configurations\_wechat.json 的文件，内容如下：

```
{
  "services": {
    "social": {
      "wechat": {
        "appId": "您的微信开放平台app id"
      }
    }
  }
}
```

### 3. 添加 SDK

#### 通过 gradle 远程依赖集成

如果您是采用 gradle 编译系统，Authorization 库已经包含了微信所需要的库文件，您不需要做任何设置。

#### 手动集成

移动开发平台（MobileLine） Authorization 资源包已经包含了微信的 SDK，您不需要另外下载。

然后，在您的 AndroidManifest.xml 文件中添加以下 SDK 需要的权限：

```
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```

## 使用微信登录功能

### 1. 添加微信登录回调处理 Activity

在您的应用包名下新建一个 wxapi 的包，然后新建一个名为 WXEntryActivity 的类，该类直接继承基类 WeChatBaseSignInActivity 即可，不需要增加任何逻辑，这个 Activity 主要是为了接收微信的登录回调：
 
```
package com.tencent.openmidas.sample.wxapi;

import com.tencent.tac.authorization.oauth2.WeChatBaseSignInActivity;

public class WXEntryActivity extends WeChatBaseSignInActivity {
}
```

### 2. 请求微信登录

在用户登录界面，您可以调用以下方法让用户选择用微信账号登录：

```
// 获取实例
TACAuthorizationService service = TACAuthorizationService.getInstance();
WeChatAuthProvider weChatAuthProvider = service.getWeChatAuthProvider(context);

// 启动登录
weChatAuthProvider.signIn(activity, new QCloudResultListener<OAuth2Credentials>() {
      	@Override
      	public void onSuccess(OAuth2Credentials credentials) {
           // 登录成功，可以拿到微信登录的authorization code
           String authorizationCode = credentials.getAuthorizationCode();
       }

       @Override
       public void onFailure(QCloudClientException clientException, QCloudServiceException serviceException) {
           // 登录失败
 });
```

在用户登录成功之后，通过 authorization code 和 secret key 可以获取真正的 access token，出于安全的考虑，secret key 不建议明文存放在客户端，所以建议把这个请求的过程放到后端服务器中进行。详细的接口可以参考：
[微信接口说明](https://open.weixin.qq.com/cgi-bin/showdocument?action=dir_list&t=resource/res_list&verify=1&id=open1419317853&token=&lang=zh_CN)

### 3. 获取用户信息

登录成功后，您可以使用有效的用户凭证，调用 getUserInfo 方法获取微信用户信息：
 
```
// 获取实例
TACAuthorizationService service = TACAuthorizationService.getInstance();
WeChatAuthProvider weChatAuthProvider = service.getWeChatAuthProvider(context);

// 获取用户信息
weChatAuthProvider.getUserInfo(mOAuth2Credentials, new QCloudResultListener<TACOpenUserInfo>() {
      	@Override
      	public void onSuccess(TACOpenUserInfo result) {
      		userInfoView.setText(result.toString());
      	}

       @Override
       public void onFailure(QCloudClientException clientException, QCloudServiceException serviceException) {
          // 获取出错
       }
});
```


### 4. 刷新 token

微信支持后台刷新 access token，access token 的生命周期通常只有 2 个小时，可以通过刷新的方式延长到一个月，之后需要用户重新登录授权：
 
```
// 获取实例
TACAuthorizationService service = TACAuthorizationService.getInstance();
WeChatAuthProvider weChatAuthProvider = service.getWeChatAuthProvider(context);

// 刷新token
weChatAuthProvider.refreshCredentialInBackground(mOAuth2Credentials,
        new QCloudResultListener<OAuth2Credentials>() {
        		@Override
             	public void onSuccess(OAuth2Credentials result) {
             		//token刷新成功
             	}

             	@Override
             	public void onFailure(QCloudClientException clientException,
                                                  QCloudServiceException serviceException) {
                	if (WeChatAuthProvider.isUserNeedSignIn(serviceException)) {
                       // 刷新失败，需要用户重新登录微信授权               
                 } else {
                       // 其他原因导致刷新失败，可以再次重试
                 }
             }
});
```

