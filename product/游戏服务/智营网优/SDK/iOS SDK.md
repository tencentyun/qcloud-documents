>!请先单击 [智营网优申请页](https://cloud.tencent.com/act/apply/ino) 进行申请。

## 接入流程

#### 获取 SDK 
1. 登录 [智营网优控制台](https://console.cloud.tencent.com/ino)，单击左侧菜单【SDK 下载】。  
2. 请按系统平台选择对应版本的 SDK，并单击【下载】。

#### 配置 SDK 
>!iOS SDK 为动态库，仅支持 iOS8 以上。

1. 在 Embedded Binaries 中引入 SDK：
![](https://main.qcloudimg.com/raw/8a63fe600804eaf556b60a4e8f79317d.png)
2. 在 Linked Frameworks and Libraries 中引入 GBeaconAPI_Base.framework。
3. 添加系统库：
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
4. 引入文件：
 - MyMNAObserver.h
 - MyMNAObserver.mm
5. 在 info.plist 中添加如下设置：
```
<key>NSAppTransportSecurity</key>
	<dict>
		<key>NSAllowsArbitraryLoads</key>
		<true/>
	</dict>
```

>!在 NSAppTransportSecurity 下，只需设置 NSAllowsArbitraryLoads 为 YES 即可，请勿再添加其他配置，例如 NSAllowsArbitraryLoadsForMedia

6. 在 AppDelegate.mm 文件中，引入头文件：
```
#import <MNA/MNAPublic.h>
#import “MyMNAObserver.h”
```
并在 application:didFinishLaunchingWithOptions 函数中设置回调函数，即粘帖如下代码：
```
MNAPublic * mna = MNAPublic::GetInstance();
MyMNAObserver * observer = MyMNAObserver::GetInstance();
mna->MNASetObserver(observer);
```
7. 完成后，按照所需调用相应接口即可。

## 接入步骤
![](https://main.qcloudimg.com/raw/ab74542d85ccaada74f1e4677f4e49dd.png)
1. 应用启动时，调用初始化`MNAInit`，并设置回调函数`MNASetObserver`。
2. 应用登录成功后，需要调用`MNASetUserName`设置`openid`，可通过`MNASetZoneId`设置`zone id`。
3. 对局开始前调用`MNAStartDiagnose`当游戏服务器 IP 发生变化时可调用`MNASetGameIp`来设置游戏服务器 IP，不发生变化时不需要调用；当应用切换到前台时，调用`MNAGoFront`;当应用切换到后台时，调用`MNAGoBack`。
4. 对局结束时，先调用`MNAIsQosWork`函数获取 Qos 保障标识，再调用`MNAEndSpeed`结束当局加速，并上报网络质量数据。
5. 进入游戏大厅后可通过调用`MNARealTimeQuery`函数来对网络进行诊断。

## API 介绍
使用单例模式调用，调用示例：
```
MNAPublic* mna = MNAPublic::GetInstance();
mna->MNAInit("appid_test", true, 0, true, false, "");
```

### 初始化

####  初始化 SDK
```
void MNAInit(const char * appid, bool isDebug, int zoneid, bool isReleaseEnv, bool isBatteryNotify, const char * tCloudKey);
```

|参数 | 含义 | 
|---------|---------|
| appid | 惟一标识该应用,即腾讯云控制台加速服务的游戏 ID | 
| isDebug | 控制 log 的输出方便联调 | 
| zoneid | 玩家大区 ID | 
| isReleaseEnv | 云控正式环境，默认直接填 true 即可 | 
| isBatteryNotify | 电量统计信息，默认直接填 false 即可| 
| tCloudKey | 腾讯云申请的 key 值 | 

####  设置回调函数
```
void MNASetObserver(MNAObserver * observer);
//参数：observer，回调函数实例。
```

####  设置用户信息
```
void MNASetUserName(int platform, const char * openId);
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

### 加速
####  开启加速器引擎 MNAStartSpeed
```
 void MNAStartSpeed(const char * vip, int vport, int htype, const char * module, int zoneid, int stopMNA, const char * pvpid, int timeout);
```

|参数 | 含义 | 
|---------|---------|
| vip | 游戏服务器地址（IP 或域名，强烈建议使用 IP）| 
| vport | 游戏服务器端口 | 
| htype | 本参数决定 HOOK 的函数种类，取值有如下：htype = 1：表示只处理 sendto() 和 recvfrom()，用于核心协议是 UD，且使用这两个函数的游戏。 | 
| hookModules| 指定要 HOOK 的动态链接库，填""即可 | 
| stopMNA | 默认值为0；为1表示强制关闭加速功能，保留网络诊断功能。 | 
| pvpid | 对局唯一 ID，用来定位对局的网络问题 | 
|  timeout | 默认值为0；设置启动阶段超时时间，单位为毫秒，当 timeout<=0 时，表示不设置启动超时。 | 

本函数被调用后将开始异步对所有加速节点进行测速，判断是否执行加速。整个过程需要5 - 6秒。完成后会回调 MNAObserver 函数。

#### 设置游戏服务器 IP（选接项）
```
void MNASetGameIp(const char *gameip);
```
|参数 | 含义 | 
|---------|---------|
| gameIp | 游戏服务器地址| 

当游戏在对局中因为网络或者别的原因导致游戏服务器 IP 发生改变时，直接调用该接口设置游戏服务器 IP 即可，当对局中 IP 不会发生变化时不需要接入，目前主要是境外业务需要调用该接口，中国内地（大陆）业务不用接。

#### 通知加速引擎：游戏目前在前台
```
(void)MNAGoFront;
```
当游戏切换到前台时,调用此函数。

#### 通知加速引擎：游戏目前切换到后台
```
(void)MNAGoBack;
```
当游戏切换到后台（例如被其它应用遮挡），必须调用此函数，通知加速引擎。

#### 正常结束加速器引擎
```
void MNAEndSpeed(const char * vip, int vport);
//参数： vip 游戏服务器地址,跟 startspeed 保持一致
//参数： vport 游戏服务器端口
```

#### 查询 4G QoS 是否保障
```
(int)MNAIsQOSWork;
```
返回 QoS 是否有保障成功：需要把此状态信息在游戏体验数据中记录并上报。4G QoS 在移动 4G 网络下才会生效，一般在结束加速 `MNAEndSpeed` 时调用，返回值具体含义如下，这个可以用于游戏上线后核对 4G QOS 加速效果。

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

### 网络诊断
####  设置实时网络诊断
```
void MNARealTimeQuery(const char * tag);
//参数`tag`，作为标识每一次查询的 ID。
```
结果由 MNAObserver 函数的 OnQueryKartinNotify 返回。

返回结果以分号拼接，含义依次如下：
```
tag; // 游戏传入的Tag
flag; // 查询成功标识，若为0则成功
desc; // 查询flag的具体描述
jump_network; // 当时网络类型0: 无网络,1: 2G, 2: 3G, 3: 4G, 4: wifi
jump_signal; // 信号强度
jump_router; // ping路由时延
router_status; // ping状态,0表示绿色，时延低；2表示红色，时延高
router_desc; // ping描述
jump_export; // 宽带或基站出口时延  
export_status; // export状态,0表示绿色，时延低；2表示红色，时延高
export_desc; //宽带出口和基站出口描述
jump_terminal; // wifi终端数 
terminal_status; // terminal状态,0表示绿色终端数少；2表示红色，时延高
terminal_desc; //wifi终端数描述
jump_proxy; // ping代理时延
jump_edge; // ping边缘时延
signal_desc; //信号强度描述
signal_status; //信号强度状态
jump_direct; // 直连测速时延
direct_status; // 直连状态,0表示绿色时延低；2表示红色，时延高
direct_desc; // 直连状态的描述
netinfo_status; // // 网卡状态, 0表示绿色网卡无问题；2表示红色网卡有问题

```

## 附录 
MNAKartinRet 关键参数取值及其说明如下：

- 字段：flag。
- 关键名称：查询结果标识。

| 取值 | 含义 | 
|---------|---------|
| 0 | 查询成功 | 
| -1 | 表明无网络 | 
| -2 | 表明请求云控失败，重新调用一次 | 
| -3 | 表明初始化 SDK 失败 | 
| -4 | 当前网络类型发生了变化，请稍后再试 | 
| -5 | 2G 网络不适合游戏，无法检测 | 

- 字段：jump_network。
- 关键名称：网络类型。

| 取值 | 含义 | 
|---------|---------|
| 0 | 无网络或网络类型无法识别 | 
| 1 | 2G | 
| 2 | 3G | 
| 3 | 4G | 
| 4 | Wi-Fi | 

- 字段：jump_signal。
- 关键名称：信号强度（仅 Wi-Fi）。

| 取值 | 含义 | 
|---------|---------|
| -1 | 获取强度失败，请稍后再试 | 
| 0..4 | Wi-Fi 信号强度 | 

- 字段：jump_router。
- 关键名称：路由器时延（仅 Wi-Fi）。

| 取值 | 含义 | 
|---------|---------|
| -1 | 不支持路由延迟查询 | 
| -2 | 获取路由器延迟失败，请稍后再试 | 
| 0..1000 | 当前路由器的延迟值 | 

- 字段：jump_terminal。
- 关键名称：共享 Wi-Fi 设备数（仅 Wi-Fi）。

| 取值 | 含义 | 
|---------|---------|
| -1 | 仅在WIFI模式下支持共享 Wi-Fi 设备查询 | 
| 0..254 | 链接相同 Wi-Fi 的设备数 | 

- 字段：jump_export。
- 关键名称：宽带出口时延。

| 取值 | 含义 | 
|---------|---------|
| -1 | 获取社区延迟失败，请稍后再试 | 
| -2 | 抱歉，当前所在区域网络不支持社区宽带延迟查询 | 
| 0..500 | 带宽出口时延值 | 

- 字段：jump_direct。
- 关键名称：直连时延。

| 取值 | 含义 | 
|---------|---------|
| -1 | 获取直连延迟失败，请稍后再试 | 
| 0..800 | 网络时延值 | 

- 字段：netinfo_desc。
- 关键名称：直连时延。

| 取值 | 含义 | 
|---------|---------|
| String| 当前网卡有丢包或错包，不适合游戏。 | 

具体设置请参考王者荣耀的示例：（ 红色字体为备注 ）

Wi-Fi 直连环境下图示如下：
![](https://mc.qcloudimg.com/static/img/8be2ccf30041db352caed1d98b524bab/wifi-android.png)

4G 直连环境下图示如下：
![](https://mc.qcloudimg.com/static/img/f62992074419d7e3a8e90c53a7112cf1/4g-android.png)

