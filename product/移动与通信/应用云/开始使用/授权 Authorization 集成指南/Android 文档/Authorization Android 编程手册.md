
## 使用 QQ 登录功能

### 1. 在登录 Activity 添加回调处理

在启动登录的 Activity 的 onActivityResult 中添加 QQ 登录回调的处理，否则在某些低端机上可能无法正确处理回调：
 
```
@Override
protected void onActivityResult(int requestCode, int resultCode, Intent data) {
    super.onActivityResult(requestCode, resultCode, data);
    if (qqAuthProvider != null) {
        qqAuthProvider.handleActivityResult(requestCode, resultCode, data);
    }
}
```


### 2. 请求 QQ 登录

在用户登录界面，您可以调用以下方法让用户选择用 QQ 账号登录：

```
// 获取实例
TACAuthorizationService service = TACAuthorizationService.getInstance();
QQAuthProvider qqAuthProvider = service.getQQAuthProvider(context);

// 启动登录
qqAuthProvider.signIn(activity, new QCloudResultListener<OAuth2Credentials>() {
            @Override
            public void onSuccess(OAuth2Credentials credentials) {
                // 登录成功，可以拿到QQ的用户凭证
                mOAuth2Credentials = credentials;
                
                String accessToken = credentials.getAccessToken();
                String openId = credentials.getOpenId();
            }

            @Override
            public void onFailure(QCloudClientException clientException, QCloudServiceException serviceException) {
                // 登录失败
            }
        };);
```

QQ 获取的凭证有效期是 3 个月，之后需要用户重新登录授权。


### 3. 获取用户信息

登录成功后，您可以使用有效的用户凭证，调用 getUserInfo 方法获取 QQ 用户信息：
 
```
// 获取实例
TACAuthorizationService service = TACAuthorizationService.getInstance();
QQAuthProvider qqAuthProvider = service.getQQAuthProvider(context);

// 获取用户信息
qqAuthProvider.getUserInfo(mOAuth2Credentials, new QCloudResultListener<TACOpenUserInfo>() {
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

