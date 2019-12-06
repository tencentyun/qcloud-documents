>!请先单击 [智营网优申请页](https://cloud.tencent.com/act/apply/ino) 进行申请。

## 接入流程
#### 获取 SDK
1. 登录 [智营网优控制台](https://console.cloud.tencent.com/ino)，单击左侧菜单【SDK 下载】。
2. 请按系统平台选择对应版本的 SDK，并单击【下载】。


#### 配置 SDK
1. 将下列文件导入到项目中：
 - MNA_ANDROID.jar
 - beacongsdk_android_v2.7.0_gsdk_cover.aar
 - libgsdk.so
2. 将Assets/Plugins/Scripts下的脚本拷贝到项目中；
![](https://main.qcloudimg.com/raw/5154c91d4a6beedf6427ae2459e2b3d4.png)
3. 修改项目中的 AndroidManifest.xml 文件，添加以下权限：
```
android:permission.INTERNET
android:permission:ACCESS_NETWORK_STATE
android:permission:READ_PHONE_STATE
android:permission:ACCESS_WIFI_STATE
android.permission.ACCESS_FINE_LOCATION
```

#### 安装包结构

| 目录| 说明| 
|---------|---------|
| MNA\MNA.framework | 适用“Build Setting->C++ Language Dialect”配置为 GNU++98，“Build Setting->C++ Standard Library”为“libstdc++(GNU C++ standard library)”的工程。 | 
| MNA_C11\MNA.framework | 适用于该两项配置分别为“GNU++11”和“libc++(LLVM C++ standard library with C++11 support)”的工程。 | 

#### 操作步骤
 
1. 在 Linked Frameworks and Libraries 中引入 MNA\MNA.framework 或 MNA_C11\MNA.framework。
>!腾讯云客户还需引入GBeaconAPI_Base.framework。
2. 添加系统库：
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
3. 在 Other linker flag 里加入 -ObjC 标志。
4. 在 info.plist 中添加如下设置： 
```
<key>NSAppTransportSecurity</key>
	<dict>
		<key>NSAllowsArbitraryLoads</key>
		<true/>
	</dict>
```
>!在 NSAppTransportSecurity 下，只需设置 NSAllowsArbitraryLoads 为 YES 即可，请勿再添加其他配置，如 NSAllowsArbitraryLoadsForMedia。
5. 引入文件：
  - MyMNAObserver.h 
  - MyMNAObserver.mm
6. 在 AppDelegate.mm 或者 Classes/UnityAppController.mm 文件中，引入头文件：
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
7. 完成后，按照所需在 Unity 调用相应接口即可。

## 接入步骤
![](https://main.qcloudimg.com/raw/9dc44c0ad0efc306925fd50c70642da0.png)
1. 游戏启动时，调用初始化`Init`。
2. 游戏登录成功后，需要调用`SetUserName`设置`openid`；并设置加速结果回调`SetObserver`；使用`SetZoneId`来设置用户的zone id；如果需要接入诊断部分，则还需要调用`SetKartinObserver`函数。
3. 游戏对局开始时，获取到对局中所使用到的域名或 IP 后，尽可能早的调用`StartSpeed`，玩家因网络或者其他异常无法连接到游戏，重新进行连接时，为保证加速效果，需要再次调用`StartSpeed`；当游戏切换到前台时，调用`GoFront`; 当游戏切换到后台时，调用`GoBack`；当游戏不想进行加速，但依然想保留 SDK 的网络探测功能时可调用`StopMNA`函数。
4. 游戏退出对局时，先调用`IsQosWork`函数获取 QoS 保障标识，再调用`EndSpeed`结束当局加速，并上报游戏网络质量数据。
5. 进入游戏大厅后可通过调用`QueryKartin`函数来对网络进行诊断。
接入步骤注意事项请参见下文 [附录1](#附录1)。

## API 介绍
API 接口由 com.tencent.mna 包下的 MNA 类提供，该类将所有方法都设计为静态函数，开发者可用类名直接进行调用。

### 初始化

####  初始化 SDK
```
public static void Init(string qqappid, bool debug, int zoneid, bool isReleaseEnv, bool useBatteryNotify, string tCloudKey)
```

|参数 | 含义 | 
|---------|---------|
| qqappid | 惟一标识该应用,即腾讯云控制台加速服务对应的游戏 ID | 
| debug | 控制 log 的输出方便联调，默认直接填 false 即可 | 
| zoneid | 玩家大区 ID | 
| isReleaseEnv | 云控正式环境，默认直接填 true 即可 | 
| useBatteryNotify | 电量统计信息，默认直接填 false 即可 | 
| tCloudKey | 腾讯云申请的 key 值 | 

####  设置用户信息
```
public static void SetUserName(int userType, string openid)
//userType：此参数为 int 型，与 MSDK 中定义账号类型一致
//openid：用户的 openid
```

| 类型 | 取值 | 
|---------|---------|
| ePlatform_None | 0 | 
| ePlatform_Weixin | 1 | 
| ePlatform_QQ | 2 | 
| ePlatfrom_WTLogin | 3 | 
| ePlatform_QQHall | 4 | 
| ePlatform_Guest | 5 | 

####  开启加速异步回调
```
public static void SetObserver(GSDKObserver d)
```
需要在初始化后设置`GSDKObserver`参数，参数为委托类型，定义如下：
```
public delegate void GSDKObserver(StartSpeedRet ret);
public class StartSpeedRet {
	public int flag; // 启动加速结果返回值
	public string desc; // 启动加速结果描述
	public int type; // hook 类型
}
```
其中 flag 值及对应描述如下：

| 错误码 | 具体含义 | 
|---------|---------|
| 2 | 无需开启加速 | 
| 1 | 正在执行 startspeed | 
| 0 | 成功 | 
| -1 | 初始化时获取 JVM 失败 | 
| -2 | unknown/2G 或者无网络下 | 
| -3 | 请求中控失败 | 
| -4 | 未达到加速条件 | 
| -5 | hook 失败 | 
| -6 | GameServer DNS 请求失败 | 
| -7 | 没有成功加载 so 库 | 
| -8 | 中控域名 DNS 解析失败 | 
| -9 | StartSpeed 请求阶段超时 | 
| -10 | StartSpeed 测速阶段超时 | 
| -11 | 请求调度失败 | 
| -12 | 请求协商失败 |

### 加速
####  开启加速器引擎 StartSpeed
```
public static void StartSpeed(string vip, int vport, int htype, string hookModules, int zoneid, int stopWlanAcc, string pvpid, int timeout)
```

|参数 | 含义 | 
|---------|---------|
| vip | 游戏服务器地址（IP 或域名，强烈建议使用 IP）| 
| vport | 游戏服务器端口 | 
| htype | 本参数决定 HOOK 的函数种类，取值有如下：<li>htype = 1：表示只处理`sendto()`和`recvfrom()`，用于核心协议是 UD 且使用这两个函数的游戏。<li>htype = 3：表示只处理`connect`和`send`函数，用于核心协议时 UDP 且使用这两个函数的游戏。 | 
|  hookModules       |hookModules 指定要HOOK的动态链接库，多个库名用英文（半角）逗号分开。若使用 apollo 的网络通信模块，则填 libapollo.so；若使用 C# 的网络通信模块，则填 libmono.so。|
| stopWlanAcc | 默认值为0；为1表示强制关闭公网加速功能，4G QOS加速功能、网络诊断功能不受影响。 | 
| pvpid | 对局唯一 ID，用来定位对局的网络问题； | 
| timeout |默认值为0；设置启动阶段超时时间，单位为毫秒，当 timeout<=0 时，表示不设置启动超时。| 

本函数被调用后将开始异步对所有加速节点进行测速，判断是否执行加速。整个过程需要5 - 6秒。完成后会回调`GSDKObserver`函数。

#### 通知加速引擎：游戏目前在前台
```
public static void GoFront()
```
当游戏切换到前台时,必须调用此函数，通知加速引擎。

#### 通知加速引擎：游戏目前切换到后台
```
public static void GoBack()
```
当游戏切换到后台（例如被其它应用遮挡），必须调用此函数，通知加速引擎。

#### 强行关闭加速
```
public static void StopMNA (string vip, int vport)
//参数： vip 游戏服务器地址,跟 startspeed 保持一致
//参数： vport 游戏服务器端口
```
强行关闭加速功能，对局过程中的网络探测功能。

#### 正常结束加速器引擎
```
public static void EndSpeed(string vip, int vport)
//参数： vip 游戏服务器地址,跟 startspeed 保持一致
//参数： vport 游戏服务器端口
```
#### 正常结束加速器引擎（选接项）
```
public static void GSDKEndSpeed(string vip, int vport，string extrainfo)
//参数： vip游戏服务器地址,跟startspeed保持一致
//参数： vport 游戏服务器端口
//参数：extrainfo传入网络质量统计等任意业务希望上报的参数，做上报使用
```
#### 查询 4G QoS 是否保障
```
public static int IsQosWork()
```
返回 QoS 是否有保障成功：需要把此状态信息在游戏体验数据中记录并上报。4G QoS 在移动 4G 网络下才会生效，一般在结束加速 EndSpeed 时调用，返回值具体含义如下，这个可以用于游戏上线后核对 4G QOS 加速效果。

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
1. 需要在初始化后设置`GSDKKartinObserver`
```
public static void SetKartinObserver(GSDKKartinObserver d)
```
参数`GSDKKartinObserver`类型如 [附录1](#附录1)。
2. 调用实时网络诊断
```
public static void QueryKartin(string tag)
//参数：tag，作为标识每一次查询的 ID。
```
网络诊断是一个耗时的过程，大概有4 - 8秒钟，因此 GSDK 使用异步返回来实现。调用此函数后，查询结果会通过回调`KartinObserver`返回。

## 数据上报
1. 为了更好的衡量网络加速效果，需要从游戏客户端，把游戏过程的网络质量数据来进行统计后上报到灯塔，智营网优服务端会进行分析，上报的内容参考以下表格。
2. 客户端上报需要使用灯塔 SDK，已接入 msdk 的业务可以直接使用 [msdk 的灯塔接口](http://wiki.msdk.qq.com/Unity/stat.html) 上报。

##  附录
<span id="附录1"></span>
### 附录1 
参数 GSDKKartinObserver 类型定义：
```
public delegate void GSDKKartinObserver(KartinRet ret);
public class KartinRet {
	public string tag; // 游戏传入的Tag
	public int flag; // 查询成功标识，若为0则成功
	public string desc; // 查询flag的具体描述
// 当时网络类型0: 无网络,1: 2G, 2: 3G, 3: 4G, 4: wifi
	public int jump_network;
	public int jump_signal; // 信号强度
   // 0表示绿色，信号强；1表示黄色，信号弱；2表示红色，信号极弱
   public int signal_status = -1;
   public String signal_desc = ""; // 3、信号强度描述
	public int jump_router; // ping路由时延
   // ping状态,0表示绿色，时延低；2表示红色，时延高
   public int router_status = -1;
   public String router_desc = ""; // ping描述
   public int jump_export = -1; // 宽带或基站出口时延  
   // export状态,0表示绿色，时延低；2表示红色，时延高  
public int export_status = -1; // 宽带出口和基站出口状态
   public String export_desc = ""; //宽带出口和基站出口描述
   public int jump_proxy; // ping代理时延
   public int jump_edge; // ping边缘时延
   public int jump_terminal; // wifi终端数 
// terminal状态,0表示绿色终端数少；2表示红色，时延高   
   public int terminal_status = -1; //wifi终端数状态
   public String terminal_desc = ""; //wifi终端数描述
   public int jump_terminal; // wifi终端数
   public int jump_direct; // 直连测速时延
// 直连状态,0表示绿色时延低；2表示红色，时延高
   public int direct_status; // 直连测速时延状态
   public int direct_desc; // 直连状态的描述
   // 网卡状态, 0表示绿色网卡无问题；2表示红色网卡有问题
   public int netinfo_status; // 网卡状态
   public int netinfo_desc; // 网卡情况具体描述
}
```

### 附录2 
KartinRet 关键参数取值及其说明如下：
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

WIFI 直连环境下图示如下：
![](https://mc.qcloudimg.com/static/img/8be2ccf30041db352caed1d98b524bab/wifi-android.png)

4G 直连环境下图示如下：
![](https://mc.qcloudimg.com/static/img/f62992074419d7e3a8e90c53a7112cf1/4g-android.png)
