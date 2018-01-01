## 应用云 Authorization 服务 Android接入指南

### 准备工作

在开始使用应用云 Authorization 服务前，您需要：

 1. 新建或者打开一个 Android 项目。
 2. 配置了应用云服务框架，配置方式请参见[应用云服务框架 Android 配置指南](https://github.com/tencentyun/qcloud-documents/blob/master/product/%E5%AD%98%E5%82%A8%E4%B8%8ECDN/_Drafts/ApplicationBoard/%E9%9B%86%E6%88%90%E6%8C%87%E5%8D%97/Core/Android/%E5%BA%94%E7%94%A8%E4%BA%91%20%E6%9C%8D%E5%8A%A1%E6%A1%86%E6%9E%B6%20Android%E6%8E%A5%E5%85%A5%E6%8C%87%E5%8D%97.md.md)。

### 集成 Authorization 服务到你的应用

#### 通过远程依赖集成 (<font color='red'>推荐</font>)

在你的应用级 build.gradle（\<project\>/\<app-module\>/build.gradle）添加应用云 Authorization 的依赖：

```
dependencies {
    //增加这行
    compile 'com.tencent.tac:authorization:1.0.0'
}
```

#### 本地集成

1. 下载 Authorization 服务资源打包文件，并解压。下载资源文件请点击[这里]()。
2. 将资源文件中的 libs 目录拷贝到您的 module 的根目录下。
4. 打开您自己 module 下的 AndroidManifest.xml 文件，然后按照下载的资源文件中的 AndroidManifest.xml 作为范例来修改。


### 集成第三方登录服务到你的应用

#### 集成微信登录

在你的应用级 build.gradle（\<project\>/\<app-module\>/build.gradle）添加微信 OpenSDK 的依赖：

```
dependencies {
    //增加这行
    compile 'com.tencent.mm.opensdk:wechat-sdk-android-without-mta:+'
}
```

#### 集成QQ登录

将 [QQ互联的Android Jar包](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/Android_SDK_V3.3.0.lite.zip) 拷贝到应用模块的libs文件夹下，同时确保你的应用级 build.gradle（\<project\>/\<app-module\>/build.gradle）文件中已经添加了对libs的依赖：

```
dependencies {
    compile fileTree(dir: 'libs', include: ['*.jar'])
}
```

### 使用QQ登录功能

#### 在登录Activity添加回调处理

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

在用户登录界面，你可以调用以下方法让用户选择用QQ账号登录：

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

QQ获取的凭证有效期是3个月，之后需要用户重新登录授权。


#### 获取用户信息

登录成功后，你可以使用有效的用户凭证，调用 getUserInfo 方法获取QQ用户信息。

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

### 使用微信登录功能

#### 添加微信登录回调处理Activity

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

在用户登录界面，你可以调用以下方法让用户选择用微信账号登录：

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

登录成功后，你可以使用有效的用户凭证，调用 getUserInfo 方法获取微信用户信息。

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


#### 刷新token

微信支持后台刷新access token，access token的生命周期通常只有2个小时，可以通过刷新的方式延长到一个月，之后需要用户重新登录授权。

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

