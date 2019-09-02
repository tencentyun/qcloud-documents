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
