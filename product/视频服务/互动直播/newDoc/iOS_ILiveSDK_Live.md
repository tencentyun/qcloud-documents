# ILiveSDK直播流程图：

![](http://mc.qcloudimg.com/static/img/06d2fb5027be53492249d4b81bd2f5a5/image.png)


# 1 初始化ILiveSDK
在应用启动时初始化ILiveSDK。

|接口名|接口描述|
|---|---|
|initSdk: accountType:|ILiveSDK内部类初始化，告知AppId。内部包含了IMSDK的初始化|

|参数类型|参数名|说明|
|---|---|---|
|int|appId|传入业务方appid|
|int|accountType|传入业务方 accountType|

*示例：
```
[[ILiveSDK getInstance] initSdk:[ShowAppId intValue] accountType:[ShowAccountType intValue]];
```

# 2 帐号登录

## 2.1 托管模式
托管模式：用户帐号系统托管到腾讯云。[ 详情](https://www.qcloud.com/doc/product/269/1509)

|接口名|接口描述|
|---|---|
|tlsLogin: pwd: succ: failed:|托管模式登录到腾讯云后台|

|参数类型|参数名|说明|
|---|---|---|
|NSString|uid|用户在托管模式下注册的帐号|
|NSString|pwd|用户在托管模式下注册帐号的密码|
|TCIVoidBlock|succ|登录成功回调|
|TCIErrorBlock|failed|登录失败回调|

＊示例：
```
[[ILiveLoginManager getInstance] tlsLogin:@"这里是帐号id" pwd:@"这里是登录密码" succ:^{
    NSLog(@"登录成功");
} failed:^(NSString *moudle, int errId, NSString *errMsg) {
    NSLog(@"登录失败");
}];
```

## 2.2 独立模式
独立模式：用户帐号系统由用户自己的服务器维护。独立模式需要业务后台生成Sig，客户端拿到这个Sig再登录腾讯云后台。[详情](https://www.qcloud.com/doc/product/269/1508)

|接口名|接口描述|
|---|---|
|iLiveLogin: sig: succ: failed:|独立模式登录到腾讯云后台|

|参数类型|参数名|说明|
|---|---|---|
|NSString|uid|用户在独立模式下注册的帐号|
|NSString|sig|用户在业务方后台获取到的签名|
|TCIVoidBlock|succ|登录成功回调|
|TCIErrorBlock|failed|登录失败回调|

*示例:
```
[[ILiveLoginManager getInstance] iLiveLogin:@"这里是帐号id" sig:@"这里是签名字符串" succ:^{
    NSLog(@"登录成功");
} failed:^(NSString *moudle, int errId, NSString *errMsg) {
    NSLog(@"登录失败");
}];
```

# 3 创建房间(进入房间)

## 3.1 主播创建房间

|接口名|接口描述|
|---|---|
|createRoom: option: succ: failed:|主播创建直播间，自动渲染本地画面，开始直播|

|参数类型|参数名|说明|
|---|---|---|
|int|roomId|房间号。业务方后台生成的房间号，需保证唯一性|
|ILiveRoomOption|option|主播创建房间时的配置项，使用defaultHostLiveOption接口获取主播默认配置即可|
|TCIVoidBlock|succ|创建房间成功回调|
|TCIErrorBlock|failed|创建房间失败回调|

*示例:
```
ILiveRoomOption *option = [ILiveRoomOption defaultHostLiveOption]; //默认主播配置
TILLiveManager *manager = [TILLiveManager getInstance];
[manager setAVRootView:self.view]; //设置渲染承载的视图
[manager addAVRenderView:self.view.bounds forKey:self.host]; //添加渲染位置

[manager createRoom:self.roomId option:option succ:^{
    NSLog(@"创建房间成功");
} failed:^(NSString *moudle, int errId, NSString *errMsg) {
    NSLog(@"创建房间失败");
}];
```

## 3.2 观众进入房间

|接口名|接口描述|
|---|---|
|joinRoom: option: succ: failed:|观众进入直播间，自动拉去远程画面并渲染，开始观看直播|

|参数类型|参数名|说明|
|---|---|---|
|int|roomId|房间号。业务方后台生成的房间号，需保证唯一性|
|ILiveRoomOption|option|观众进入房间时的配置项，使用defaultGuestLiveOption接口获取观众默认配置即可|
|TCIVoidBlock|succ|进入房间成功回调|
|TCIErrorBlock|failed|进入房间失败回调|

*示例:
```
ILiveRoomOption *option = [ILiveRoomOption defaultGuestLiveOption]; //默认观众配置
TILLiveManager *manager = [TILLiveManager getInstance];
[manager setAVRootView:self.view]; //设置渲染承载的视图
[manager addAVRenderView:self.view.bounds forKey:self.host]; //添加渲染位置

[manager joinRoom:self.roomId option:option succ:^{
    NSLog(@"进入房间成功");
} failed:^(NSString *moudle, int errId, NSString *errMsg) {
    NSLog(@"进入房间失败");
}];
```

若以上步骤均无误，则主播开始直播，观众观看直播的整个流程就结束了。
