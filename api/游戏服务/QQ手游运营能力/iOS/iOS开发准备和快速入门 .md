
## 开发准备

### 环境依赖
Xcode 集成开发工具
### 目录结构
iOS SDK 包中：

- TencentOpenApi_iOS_Bundle.bundle 打包了 iOS SDK 需要的资源文件。
- TencentOpenAPI.framework 打包了 iOS SDK 的头文件定义和具体实现。

![](https://mc.qcloudimg.com/static/img/67b5aabeb560054a018c497e4bf4c462/image.png)

### 安装SDK
1. 将 iOS SDK 中的 TencentOpenAPI.framework 和 TencentOpenApi_IOS_Bundle.bundle 两个文件拷贝到应用开发的目录下，然后按下图所示添加到工程中：
![](https://mc.qcloudimg.com/static/img/f709646f850644361d814855ed91fbf1/image.png)
![](https://mc.qcloudimg.com/static/img/f38f0183b8b167d2c81ce1c90932405f/image.png)
2. 添加 SDK 依赖的系统库文件 SystemConfiguration.framework 和 libstdc++.tbd。然后在 Xcode 中打开工程配置文件，添加依赖库。如图所示：
![](https://mc.qcloudimg.com/static/img/e9c540e4b5b35026e226c8f79739e489/image.png)
3. 直接在默认库文件中选择后单击【Add】，下图以添加 SystemConfiguration.framework 为例：
![](https://mc.qcloudimg.com/static/img/31a0aa2d4175dc3b113f1506803c8cf0/image.png)
4. 返回后看到 SystemConfiguration.framework 已经在 Linked Frameworks and Libraries 中出现。如图所示：
![](https://mc.qcloudimg.com/static/img/76f1c8252d61d8db9fced7295fd893d0/image.png)
5. 修改必要的工程配置属性：在工程配置中的【Build Settings】一栏中找到 Linking 配置区，给【Other Linker Flags】配置项添加属性值** -fobjc-arc**。
![](https://mc.qcloudimg.com/static/img/742cddedf0c34de7f0da7b4f2be0147b/image.png)

### 修改必要的代码
- 修改工程配置文件:
在 XCode 中选择你的工程设置项：选中【TARGETS】一栏，在【info】>【URL type】添加一条新的 URL scheme，新的 scheme 是 tencent 和 APPID 的组合。如果您使用的是 XCode3 或者更低的版本，则需要在 plist 文件中添加。Demo 中我们使用的注册 APPID 是 222222。如下图所示：
![](https://mc.qcloudimg.com/static/img/3bcc4ae889d6d5cef121d564b1922d88/image.png)
- 重写 AppDelegate 的 handleOpenURL 和 openURL 方法:
openURL:
```
-(BOOL)application:(UIApplication *)application openURL:(NSURL *)url 
sourceApplication:(NSString *)sourceApplication annotation:(id)annotation{
return [TencentOAuth HandleOpenURL:url];
}
```
handleOpenURL:
```
-(BOOL)application:(UIApplication *)application handleOpenURL:(NSURL *)url{
return [TencentOAuth HandleOpenURL:url];
}
```
- 在代码中实现 TencentSessionDelegate 协议中的方法:
具体协议可以参照 TencentOpenAPI.framework /Headers 中的 TencentOAuth.h 文件。
- 初始化 iOS SDK API 数据对象 TencentOAuth：
 1. 创建 TencentOAuth 并初始化其 appid，demo 为 222222。delegate 为实现 TencentSessionDelegate 的对象：
	```
	//这里delegate不能为空
	_tencentOAuth = [[TencentOAuth alloc] initWithAppId:@"222222",   andDelegate:self];
	```
 2. 初始化 redirectURI（这里需要填写注册 APP 时填写的域名。默认可以不用填写。建议不用填写。demo 可以在这里注册：[demo 注册地址](http://www.qq.com)
```
  _tencentOAuth.redirectURI = @"www.qq.com";
```
 3. 设置应用需要用户授权的 API 列表。 (建议如果授权过多的话，可能会造成用户不愿意授权。这里最好只授权应用需要用户赋予的授权。)：
```
 _permissions =  [[NSArray arrayWithObjects:@"get_user_info", @"get_simple_userinfo", @"add_t", nil] retain];
```

## 快速入门 

登录时，调用 TencetnOAuth 对象的 authorize 方法：

```
[_tencentOAuth authorize:_permissions inSafari:NO]；
```
	
登录完成后，会调用 TencentSessionDelegate 中关于登录的协议方法。

```
[_tencentOAuth authorize:_permissions inSafari:NO]；
```
登录成功：

```
@protocol TencentSessionDelegate <NSObject>
- (void)tencentDidLogin
{
    _labelTitle.text = @"登录完成";
    
    if (_tencentOAuth.accessToken && 0 != [_tencentOAuth.accessToken length])
{
    //  记录登录用户的OpenID、Token以及过期时间
        _labelAccessToken.text = _tencentOAuth.accessToken;
    }
    else
    {
        _labelAccessToken.text = @"登录不成功 没有获取accesstoken";
    }
}
```
非网络错误导致登录失败：

```
@protocol TencentSessionDelegate <NSObject>
-(void)tencentDidNotLogin:(BOOL)cancelled
{
if (cancelled)
{
_labelTitle.text = @"用户取消登录";
	}
	else 
{
	_labelTitle.text = @"登录失败";
	}
}

网络错误导致登录失败：
@protocol TencentSessionDelegate <NSObject>
-(void)tencentDidNotNetWork
{
	_labelTitle.text=@"无网络连接，请设置网络";
}
```
登录成功后，即可获取到 access token 和 openid。accessToken 和 openid 保存在 TencentOAuth 对象中。可以通过相应的属性方法直接获得。

```
[_tencentOAuth accessToken] ;
[_tencentOAuth openId] ;
```

>**注意：**
>- 由于登录是异步过程，这里可能会由于用户的行为导致整个登录的的流程无法正常走完，即有可能由于用户行为导致登录完成后不会有任何登录回调被调用。开发者在使用 SDK 进行开发的时候需要考虑到这点，防止由于一直在同步等待登录的回调而造成应用的卡死，建议在登录的时候将这个实现做成一个异步过程。
- 获取到的 access token 具有三个月有效期，过期后提示用户重新登录授权。
- 第三方应用可存储 access token 信息，以便后续调用 OpenAPI 访问和修改用户信息时使用。如果需要保存授权信息，需要保存登录完成后返回的 accessToken，openid 和 expirationDate 三个数据，下次登录的时候直接将这三个数据是设置到 TencentOAuth 对象中即可。
获得：
```
[_tencentOAuth accessToken] ;
[_tencentOAuth openId] ;
[_tencentOAuth expirationDate] ;
```
设置：
```
[_tencentOAuth setAccessToken:accessToken] ;
[_tencentOAuth setOpenId:openId] ;
[_tencentOAuth setExpirationDate:expirationDate] 
```
- 建议应用在用户登录后，即调用 getUserInfo 接口获得该用户的头像、昵称并显示在界面上，使用户体验统一。
- iOS SDK 支持应用跳转到手机 QQ 进行登录，给用户提供更加安全、快捷的体验 。如果用户没有安装手机 QQ，且开发者具有 webview 权限，则显示登录页；如果开发者没有 webview 权限，SDK 版本高于2.9，则显示登录页，SDK 低于2.9，则显示下载页。由于跳转至下载页在当前苹果 APP 审核有被拒风险，所以，希望开发者尽快升级是用最新版 SDK。
