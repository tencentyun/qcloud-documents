## 准备工作

请确保您已经通过 gradle 配置或者手动将 QQ SDK 集成到工程中，并配置好 App ID。

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
