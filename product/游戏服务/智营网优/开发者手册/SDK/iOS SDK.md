## 1 iOS 接入

### 1.1 SDK 获取
智营网优 iOS SDK 下载地址：[iOS SDK](https://mc.qcloudimg.com/static/archive/12b7fd970dd3791d6a83fd5c4618fb33/archive.zip).

### 1.2 SDK 配置
#### 1.2.1 安装包结构

| MNA.framework | 适用于“Build Setting->C++ Language Dialect”配置为 GNU++98，“Build Setting->C++ Standard Library”为“libstdc++(GNU C++ standard library)”的工程。 | 
|---------|---------|
| MNA.framework | 适用于以上两项配置分别为“GNU++11”和“libc++(LLVM C++ standard library with C++11 support)”的工程。 | 

#### 1.2.2 步骤

1) 引入 SDK

- MNA.framework/MNA_C11.framework
- GBeaconAPI_Base.framework

2) 添加系统库

- SystemConfiguration.framework
- libz.dylib 
- libstdc++.dylib （或 libc++.dylib ）
- libsqlite3.dylib
- CoreTelephoney.framework
- Security.framework
- AdSupport.framework
- CoreLocation.framework
- MobileCoreService.framework
- UIKit.framework

3) 在 Other linker flag 里加入 -ObjC 标志。

4) 在info.plist中添加如下设置：
```
<key>NSAppTransportSecurity</key>
<dict>
	<key>NSAllowsArbitraryLoads</key>
	<true/>
</dict>
```
注意：在 NSAppTransportSecurity 下，只需设置 NSAllowsArbitraryLoads 为 YES 即可，请勿再添加其他配置，如 NSAllowsArbitraryLoadsForMedia。
5) 完成，按照所需调用相应接口即可。

## 2 API 接口接入步骤
![](https://mc.qcloudimg.com/static/img/a88e299383eb7d9aae1e848a500e0486/image.png)
1. 应用启动时，调用初始化`MNAInit`。
2. 应用登录成功后，需要调用`MNASetUserName`设置`openid`。 
3. 对局开始前调用`MNAStartDiagnose`；当应用切换到前台时，调用`MNAGoFront`; 当应用切换到后台时，调用`MNAGoBack`。
4. 对局结束时，先调用`MNAIsQosWork`函数获取 QoS 保障标识，再调用`MNAEndDiagnose`结束当局加速，并上报网络质量数据。
5. 进入游戏大厅后可通过调用`MNARealTimeQuery`函数来对网络进行诊断。

## 3  API 介绍
调用示例：`[[MNAPublic sharedInstance] XXXXXXXX];`

### 3.1 初始化

####  3.1.1 初始化 SDK
```
- (void)MNAInit:(NSString *)appid Debug:(BOOL)isDebug Zoneid:(int)zoneid IsReleaseEnv:(BOOL)isReleaseEnv IsUseBatteryNotify:(BOOL)isBatteryNotify TCloudKey:(NSString *)tCloudKey;
```

|参数 | 含义 | 
|---------|---------|
| appid | 惟一标识该应用 | 
| isDebug | 控制 log 的输出方便联调 | 
| zoneid | 玩家大区 ID | 
| isReleaseEnv | 云控正式环境，默认直接填 YES 即可 | 
| isBatteryNotify | 电量统计信息，默认直接填 NO 即可 | 
| tCloudKey | 腾讯云申请的 key 值 | 

####  3.1.2 设置用户信息
```
- (void)MNASetUserName:(int)platform OpenId:(NSString *)openId;
//platform：此参数为 int 型，与 MSDK 中定义账号类型一致
//openiId：用户的 openid
```

| 类型 | 取值 | 
|---------|---------|
| ePlatform_None | 0 | 
| ePlatform_Weixin | 1 | 
| ePlatform_QQ | 2 | 
| ePlatfrom_WTLogin | 3 | 
| ePlatform_QQHall | 4 | 
| ePlatform_Guest | 5 | 

### 3.2 加速
####  3.2.1 开启加速器引擎 MNAStartDiagnose
```
 - (void)MNAStartDiagnose:(NSString *)vip Vport:(int)vport Htype:(int)htype Zoneid:(int)zoneid PVPid:(NSString *) pvpid;
```

|参数 | 含义 | 
|---------|---------|
| vip | 游戏服务器地址（IP 或域名，强烈建议使用 IP）| 
| vport | 游戏服务器端口 | 
| htype | 填 0 | 
| zoneid | 玩家大区 ID | 
| pvpid | 对局唯一 ID | 

功能： 本函数被调用后将开始网络诊断。

#### 3.2.2 通知加速引擎：游戏目前在前台
```
- (void)MNAGoFront;
```
当游戏切换到前台时,调用此函数。

#### 3.2.3 通知加速引擎：游戏目前切换到后台
```
- (void)MNAGoBack;
```
当游戏切换到后台（比如被其它应用遮挡），必须调用此函数，通知加速引擎。

#### 3.2.4 强行关闭加速
```
- (void)MNAEndDiagnose:(NSString *)vip Vport:(int)vport;
//参数： vip 游戏服务器地址,跟 startspeed 保持一致
//参数： vport 游戏服务器端口
```

#### 3.2.5 查询 4G QoS 是否保障
```
- (int)MNAIsQOSWork;
```
返回 QoS 是否有保障成功：需要把此状态信息在游戏体验数据中记录并上报。4G QoS 在移动 4G 网络下才会生效，一般在结束加速 MNAEndDiagnose 时调用，返回值具体含义如下，这个可以用于游戏上线后核对 4G QOS 加速效果。

| 返回值 | 具体含义 | 
|---------|---------|
| 1 | 保障成功 | 
| 0 | 保障失败（默认值）| 
| -1 | 非 4G | 
| -2 | 不满足保障条件 | 
| -3 | 云控配置关闭 | 
| -4 | 云控返回 errno 非 0 | 
| -5 | 解析云控数据失败 | 
| -6 | 获取本地 IP 失败 | 
| -7 | 运营商返回 errno 非 0 | 
| -8 | 解析运营商数据失败 | 

### 3.3 网络诊断
####  设置实时网络诊断
```
-(void)MNARealTimeQuery:(NSString *)tag withGhCompletionHandler:(void (^)(MNAKartinRet *))handler;
```
参数`tag`，作为标识每一次查询的 ID。

