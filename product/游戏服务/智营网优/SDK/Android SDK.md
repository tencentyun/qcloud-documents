## 1 接入流程/开发准备

### 1.1 SDK 获取
登录腾讯云控制台,在智营网优管理后台下载 SDK。
>!本产品需要申请通过后才能访问管理后台 

### 1.2 SDK 配置
将下列文件导入到项目中：
- MNA_ANDROID.jar
- beacongsdk_xxx.jar
- libgsdk.so

修改项目中的 AndroidManifest.xml 文件，添加以下权限：
```
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
<uses-permission android:name="android.permission.READ_PHONE_STATE"/>
<uses-permission android:name="android.permission.ACCESS_Wi-Fi_STATE"/>
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>
```

## 2 API 接口接入步骤
![](https://mc.qcloudimg.com/static/img/057c7436f3a4b6ac2a0eeb056548bb01/image.png)
1. 应用启动时，调用初始化`GSDKInit`。
2. 应用登录成功后，需要调用`GSDKSetUserName`设置`openid`。 
3. 应用登录成功后，尽可能早地调用`GSDKStartSpeed`，用户因网络或者其他异常无法连接到服务器，重新进行连接时，为保证加速效果，需要再次调用`GSDKStartSpeed`；当应用切换到前台时，调`GSDKGoFront`; 当应用切换到后台时，调用`GSDKGoBack`；当应用不想进行加速，但依然想保留 SDK 的网络探测功能时可调用`GSDKStopMNA`函数。
4. 应用退出时，先调用`GSDKIsQosWork`函数获取 Qos 保障标识，再调用`GSDKEndSpeed`结束当局加速，并上报网络质量数据。
5. 进入游戏大厅后可通过调用`GSDKQueryKartin`函数来对网络进行诊断。
接入步骤注意事项：见附录1。

## 3 API 介绍
API 接口由`com.tencent.mna`包下的`GSDKPlatform`类提供，该类将所有方法都设计为静态函数，开发者可用类名直接进行调用。

### 3.1 初始化
#### 3.1.1 初始化 SDK
```
public static void GSDKInit(Context context, string qqappid, bool debug, int zoneid, boolean env, boolean useBattery, String tcloudkey)
```

|参数 | 含义 | 
|---------|---------|
| context | 上下文环境或者当前 activity | 
| qqappid | 惟一标识该应用，对应腾讯云加速服务的“游戏ID” | 
| debug | 控制 log 的输出方便联调 | 
| zoneid | 玩家大区 ID | 
| env | 云控正式环境，默认直接填 true 即可 | 
| useBattery | 电量统计信息，默认直接填 false 即可 | 
| tCloudKey | 腾讯云申请的 key 值,即“密钥 KEY” | 

#### 3.1.2 设置用户信息
```
public static void GSDKSetUserName(int userType, string openid)
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

#### 3.1.3 开启加速异步回调
```
public static void GSDKSetObserver(GSDKObserver d)
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

### 3.2 加速
####  3.2.1 开启加速器引擎 StartSpeed
```
public static void GSDKStartSpeed(string vip, int vport, int htype, string hookModules, int zoneid, int stopMNA, int timeout, String pvpid)
```
功能： 本函数被调用后将开始异步对所有加速节点进行测速，判断是否执行加速。整个过程需要5 - 6秒。完成后会回调`GSDKObserver`函数。  

|参数 | 含义 | 
|---------|---------|
| vip | 游戏服务器地址（IP 或域名，强烈建议使用 IP）| 
| vport | 游戏服务器端口 | 
| htype | 本参数决定 HOOK 的函数种类，取值有如下：<li>htype = 1：表示只处理`sendto()`和`recvfrom()`，用于核心协议是 UD 且使用这两个函数的游戏。<li>htype = 3：表示只处理`connect`和`send`函数，用于核心协议时 UDP 且使用这两个函数的游戏。 | 
|  hookModules       |hookModules 指定要 HOOK 的动态链接库，多个库名用英文（半角）逗号分开。若使用 C# 的网络通信模块，则填 libmono.so |
| stopMNA | 默认值为 0 ； 1 表示强制关闭加速功能，保留网络诊断功能 | 
| timeout | 默认值为 0 ；设置启动阶段超时时间，单位为毫秒，当`timeout<=0`时，表示不设置启动超时 | 
| pvpid | 游戏对局唯一 ID，应用直接填`"UNKNOWN"` | 


#### 3.2.2 通知加速引擎：游戏目前在前台
```
public static void GSDKGoFront()
```
当游戏切换到前台时,必须调用此函数，通知加速引擎。

#### 3.2.3 通知加速引擎：游戏目前切换到后台
```
public static void GSDKGoBack()
```
当游戏切换到后台（比如被其它应用遮挡），必须调用此函数，通知加速引擎。

#### 3.2.4 强行关闭加速
```
public static void GSDKStopMNA (string vip, int vport)
//参数： vip、vport 游戏服务器地址,跟 startspeed 保持一致
```
强行关闭加速功能，对局过程中的网络探测功能。

#### 3.2.5 正常结束加速器引擎
```
public static void GSDKEndSpeed(string vip, int vport)
//参数： vip 游戏服务器地址,跟 startspeed 保持一致
//参数： vport 游戏服务器端口
```

#### 3.2.6 查询 4G QoS 是否保障
```
public static int GSDKIsQosWork()
```
返回 QoS 是否有保障成功：
需要把此状态信息在游戏体验数据中记录并上报。4G QOS 在移动 4G 网络下才会生效，一般在结束加速`EndSpeed`时调用，返回值具体含义如下，这个可以用于游戏上线后核对 4G QoS 加速效果。

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
#### 设置实时网络诊断
1. 需要在初始化后设置`GSDKKartinObserver`
```
public static void SetKartinObserver(GSDKKartinObserver d)
```
参数`GSDKKartinObserver`类型如附录2。
2. 调用实时网络诊断
```
public static void GSDKQueryKartin(string tag)
//参数：tag，作为标识每一次查询的 ID 。
```
网络诊断是一个耗时的过程，大概有4 - 8秒钟，因此 GSDK 使用异步返回来实现。调用此函数后，查询结果会通过回调`KartinObserver`返回。

## 4 附录

### 4.1 附录1  接入步骤注意事项
#### 4.1.1 如果游戏过程中客户端 IP 发生改变
由于客户端 IP 改变了（可能是由于用户切换网络等操作导致） ，需要再调用`GSDKStartSpeed`，且传入参数中`stopMNA`设为 1 。启动对局时调用`GSDKStartSpeed`，如果超时未收到回调，可以调用`GSDKStopMNA`接口结束加速功能。
#### 4.1.2 使用`connect->send`方式进行 UDP 通信的注意事项
1. 使用`connect->send`方式进行 UDP 通信时，必须在加速结果回调后才能进行`connect`操作，否则无法正常加速。
2. 此外，如果客户端 IP 改变，导致需要进行重新连接时，可以选择：
1)  再次调用`GSDKStartSpeed`，等待回调后进行`connect`；
2)  调用`GSDKEndSpeed`结束加速。
3. 若使用`Connect`方式进行通信，启动阶段超时处理、网络重连阶段处理可以按照以下流程调用接口：
1) 启动对局时调用`GSDKStartSpeed`，如果超时未收到回调，可以调用`GSDKStopMNA`结束加速。（注意，如果已经收到回调，并且加速成功时，调用`GSDKStopMNA`接口会导致加速停止）
2) 如果网络重连，且`vip:vport`改变，重新`connect`时，必须再次调用`GSDKStartSpeed`；如果此时不希望进行加速（等待加速回调耗时较长，为减少玩家重连等待时间），则`GSDKStartSpeed`的`stopMNA`参数填为 1 即可；如果此时仍希望进行加速，则按照正常流程进行调用。
3) 如果网络重连时，`vip:vport`没有改变，则不需进行操作。

### 4.2 附录2  参数 GSDKKartinObserver 类型定义
```
public delegate void GSDKKartinObserver(KartinRet ret);
public class KartinRet {
	public string tag; // 游戏传入的Tag
	public int flag; // 查询成功标识，若为0则成功
	public string desc; // 查询flag的具体描述
	// 当时网络类型0: 无网络,1: 2G, 2: 3G, 3: 4G, 4: Wi-Fi
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
	public int jump_terminal; // Wi-Fi终端数 
	// terminal状态,0表示绿色终端数少；2表示红色，时延高   
	public int terminal_status = -1; //Wi-Fi终端数状态
	public String terminal_desc = ""; //Wi-Fi终端数描述
	public int jump_terminal; // Wi-Fi终端数
	public int jump_direct; // 直连测速时延
	// 直连状态,0表示绿色时延低；2表示红色，时延高
	public int direct_status; // 直连测速时延状态
	public int direct_desc; // 直连状态的描述
	// 网卡状态, 0表示绿色网卡无问题；2表示红色网卡有问题
	public int netinfo_status; // 网卡状态
	public int netinfo_desc; // 网卡情况具体描述
}
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
| -1 | 仅在 Wi-Fi 模式下支持共享 Wi-Fi 设备查询 | 
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

