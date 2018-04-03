
## 手动集成

如果您无法通过 gradle 远程依赖的方式来集成 SDK，我们提供了手动的方式来集成服务：


#### 1. 下载服务资源压缩包

1. 下载 [移动开发平台（MobileLine）核心框架资源包](http://tac-android-libs-1253960454.cosgz.myqcloud.com/1.0.0/tac-core-1.0.0.zip)，并解压。
2. 下载 [移动开发平台（MobileLine） Authorization 资源包](http://tac-android-libs-1253960454.cosgz.myqcloud.com/1.0.0/tac-authorization-1.0.0.zip)，并解压。

#### 2. 集成 jar 包

将资源文件中的所有 jar 包拷贝到您工程的 `libs` 目录。

## 配置服务

Authorization 服务使用默认参数即可，不需要额外配置。如果您已经配置好 TACApplication 单例，这个过程已经自动完成。

**Authorization 服务需要配合微信或者 QQ 登录才能工作**，您可以根据业务需要，自行选择同时集成两种登录方式，或者选择其中一种。


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

## 集成 QQ 登录

### 1. 注册应用

如果您还没有在 [QQ 互联平台](https://connect.qq.com/) 注册应用，请先移步注册您的应用。

### 2. 配置应用

在您的应用模块的 assets 文件夹下，新建一个名为 `tac\_service\_configurations\_qq.json` 的文件，内容如下：

```
{
  "services": {
    "social": {
      "qq": {
        "appId": "您的QQ互联平台的app id"
      }
    }
  }
}
```


### 3. 下载 SDK 

下载 [jar 包](http://tac-android-libs-1253960454.cosgz.myqcloud.com/jars/open_sdk_r5923_lite.jar) ，并拷贝到应用模块的 `libs` 文件夹下。


### 4. 添加 SDK 依赖

#### 通过 gradle 远程依赖集成

如果您是采用 gradle 编译系统，确保应用级 build.gradle（\<project\>/\<app-module\>/build.gradle）文件中已经包含了对 libs 目录的依赖：

```
dependencies {
    compile fileTree(dir: 'libs', include: ['*.jar'])
}
```

#### 手动集成

请把下载的 QQ open jar 包添加到 classpath 中，并在 AndroidManifest.xml 文件中添加以下权限和 Activity：

```
	<uses-permission android:name="android.permission.INTERNET" />
   	<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />

    <application>
    	...
    	
        <activity
            android:name="com.tencent.tauth.AuthActivity"
            android:launchMode="singleTask"
            android:noHistory="true">
            <intent-filter>
                <action android:name="android.intent.action.VIEW" />

                <category android:name="android.intent.category.DEFAULT" />
                <category android:name="android.intent.category.BROWSABLE" />

                <!--<data android:scheme="${tencentOpenAppId}" />-->
            </intent-filter>
        </activity>

        <activity
            android:name="com.tencent.connect.common.AssistActivity"
            android:screenOrientation="behind"
            android:theme="@android:style/Theme.Translucent.NoTitleBar"
            android:configChanges="orientation|keyboardHidden">
        </activity>
    </application>
```

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

