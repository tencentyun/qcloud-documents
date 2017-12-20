## 应用云 Authorization服务 Android接入指南

### 集成SDK到你的应用

在你的应用级 build.gradle（\<project\>/\<app-module\>/build.gradle）添加 应用云 Analytics 的依赖：

```
dependencies {
    //增加这行
    compile 'com.tencent.tac:authorization:1.0.0'
}
```

如果你需要集成QQ登录，将 [jar包]() 拷贝到应用模块的libs文件夹下，同时确保 build.gradle文件中已经添加了依赖：

```
dependencies {
    compile fileTree(dir: 'libs', include: ['*.jar'])
}
```

### QQ登录

#### 添加回调处理

在启动登录的Activity的 onActivityResult 中添加qq登录回调的处理，否则在某些低端机上可能无法正确处理回调。

```
@Override
protected void onActivityResult(int requestCode, int resultCode, Intent data) {
    super.onActivityResult(requestCode, resultCode, data);
    if (qqAuthProvider != null) {
        qqAuthProvider.handleActivityResult(requestCode, resultCode, data);
    }
}
```


#### 请求QQ登录

QQ获取的凭证有效期是3个月，之后需要用户重新登录授权。

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


#### 获取用户信息

你可以调用 getUserInfo 方法获取QQ用户信息，需要提供之前登录返回的凭证。

```
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

### 微信登录

#### 添加回调处理

在app包名下新建一个wxapi的包，然后新建一个名为 WXEntryActivity 的类，该类直接继承此基类即可，不需要增加任何逻辑。

```
public class WXEntryActivity extends WeChatBaseSignInActivity {
}
```

然后在AndroidManifest.xml中注册该Activity，设置 export = true。

```
<activity android:name=".wxapi.WXEntryActivity"
            android:exported="true" />
```

#### 请求微信登录

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

在用户登录成功之后，通过authorization code 和 secret key 可以获取真正的 access token。出于安全的考虑，secret key不建议明文存放在客户端，所以建议把这个请求的过程放到后端服务器中进行。详细的接口可以参考：
[微信接口说明](https://open.weixin.qq.com/cgi-bin/showdocument?action=dir_list&t=resource/res_list&verify=1&id=open1419317853&token=&lang=zh_CN)

#### 获取用户信息

你可以调用 getUserInfo 方法获取微信用户信息，需要提供一个有效的用户凭证。

```
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


#### 刷新token

微信支持后台刷新access token，access token的生命周期通常只有2个小时，可以通过刷新的方式延长到一个月，之后需要用户重新登录授权。

```
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

