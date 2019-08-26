## 1 iOS 接入

### 1.1 SDK 获取
登录腾讯云控制台,在智营网优管理后台下载 SDK。  
>!本产品需要申请通过后才能访问管理后台。

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

>!在 NSAppTransportSecurity 下，只需设置 NSAllowsArbitraryLoads 为 YES 即可，请勿再添加其他配置，如 NSAllowsArbitraryLoadsForMedia。

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
| appid | 惟一标识该应用,即腾讯云控制台加速服务的游戏 ID | 
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

返回参数MNAKartinRet类型说明：

```
NSString * tag; // 游戏传入的Tag
int flag; // 查询成功标识，若为0则成功
NSString * desc; // 查询flag的具体描述
int jump_network; // 当时网络类型0: 无网络,1: 2G, 2: 3G, 3: 4G, 4: Wi-Fi
int jump_signal; // 信号强度
int signal_status = -1; // 0表示绿色，信号强；1表示黄色，信号弱；2表示红色，信号极弱
NSString * signal_desc = ""; // 3、信号强度描述
int jump_router; // ping路由时延
int router_status = -1; // ping状态,0表示绿色，时延低；2表示红色，时延高
NSString * router_desc = ""; // ping描述
int jump_export = -1; // 宽带或基站出口时延  
// export状态,0表示绿色，时延低；2表示红色，时延高  
int export_status = -1; // 宽带出口和基站出口状态
NSString * export_desc = ""; //宽带出口和基站出口描述
int jump_proxy; // ping代理时延
int jump_edge; // ping边缘时延
int jump_terminal; // Wi-Fi终端数 
// terminal状态,0表示绿色终端数少；2表示红色，时延高   
int terminal_status = -1; //Wi-Fi终端数状态
NSString * terminal_desc = ""; //Wi-Fi终端数描述
int jump_terminal; // Wi-Fi终端数
int jump_direct; // 直连测速时延
// 直连状态,0表示绿色时延低；2表示红色，时延高
int direct_status; // 直连测速时延状态
int direct_desc; // 直连状态的描述
// 网卡状态, 0表示绿色网卡无问题；2表示红色网卡有问题
int netinfo_status; // 网卡状态
int netinfo_desc; // 网卡情况具体描述

```

### 4.3 附录3  KartinRet 关键参数取值及其说明如下
#### 字段：flag；关键名称：查询结果标识
| 取值 | 含义 | 
|---------|---------|
| 0 | 查询成功 | 
| -1 | 表明无网络 | 
| -2 | 表明请求云控失败，重新调用一次 | 
| -3 | 表明初始化 SDK 失败 | 
| -4 | 当前网络类型发生了变化，请稍后再试 | 
| -5 | 2G 网络不适合游戏，无法检测 | 

#### 字段：jump_network；关键名称：网络类型
| 取值 | 含义 | 
|---------|---------|
| 0 | 无网络或网络类型无法识别 | 
| 1 | 2G | 
| 2 | 3G | 
| 3 | 4G | 
| 4 | Wi-Fi | 

#### 字段：jump_signal；关键名称：信号强度（仅 Wi-Fi）
| 取值 | 含义 | 
|---------|---------|
| -1 | 获取强度失败，请稍后再试 | 
| 0..4 | Wi-Fi 信号强度 | 

#### 字段：jump_router；关键名称：路由器时延（仅 Wi-Fi）
| 取值 | 含义 | 
|---------|---------|
| -1 | 不支持路由延迟查询 | 
| -2 | 获取路由器延迟失败，请稍后再试 | 
| 0..1000 | 当前路由器的延迟值 | 

#### 字段：jump_terminal；关键名称：共享 Wi-Fi 设备数（仅 Wi-Fi）
| 取值 | 含义 | 
|---------|---------|
| -1 | 仅在WIFI模式下支持共享 Wi-Fi 设备查询 | 
| 0..254 | 链接相同 Wi-Fi 的设备数 | 

#### 字段：jump_export；关键名称：宽带出口时延
| 取值 | 含义 | 
|---------|---------|
| -1 | 获取社区延迟失败，请稍后再试 | 
| -2 | 抱歉，当前所在区域网络不支持社区宽带延迟查询 | 
| 0..500 | 带宽出口时延值 | 

#### 字段：jump_direct；关键名称：直连时延
| 取值 | 含义 | 
|---------|---------|
| -1 | 获取直连延迟失败，请稍后再试 | 
| 0..800 | 网络时延值 | 

 

具体设置请参考王者荣耀的示例：（ 红色字体为备注 ）

Wi-Fi 直连环境下图示如下：
![](https://mc.qcloudimg.com/static/img/8be2ccf30041db352caed1d98b524bab/wifi-android.png)

4G 直连环境下图示如下：
![](https://mc.qcloudimg.com/static/img/f62992074419d7e3a8e90c53a7112cf1/4g-android.png)

