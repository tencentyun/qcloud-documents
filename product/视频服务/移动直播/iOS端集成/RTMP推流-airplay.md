## AirPlay介绍

AirPlay 是苹果开发的一种无线技术，能把 iPhone 上的屏幕内容（包括系统 UI）直接投影到其它设备，因此也成为 AirPlay 镜像。

相比于 [ReplayKit](https://www.qcloud.com/document/product/454/7883) , Airplay 的优势就是不要求目标 App 的支持，因为它可以在任何情况下获取到当前屏幕的内容，不管是一款游戏，还是系统界面。

有得必有失，如此强大的能力必然受到苹果的限制，所以使用此套方案的 APP 有可能** <font color='red'>无法通过 </font>** AppStore 的审核，如无法上架应用商店，可以考虑使用企业证书签名的方式签发 ipa 安装包。

## 版本要求
最低 iOS **9.0** 及以上系统才能支持。
	
## 特别说明

| 包名    | 功能   | 相关说明 | 下载 |
|--------|-------|---------|---------|
| TXAirPlayService.framework | Airplay核心模块 | / | 暂不提供下载 |
| CocoaAsyncSocket.framework ( >= 1.0)  | 第三方开源库 |[访问 github 地址](https://github.com/robbiehanson/CocoaAsyncSocket) | [点击下载](https://mc.qcloudimg.com/static/archive/b286354677e2b74cef7cc6d7fbb75b88/CocoaAsyncSocket-master.zip) |
| TXRTMPSDK.framework ( >= 1.8.1)  | RTMP SDK | [查看说明文档](https://www.qcloud.com/document/product/454/7873) |[查看下载地址](https://www.qcloud.com/document/product/454/7873#.E4.B8.8B.E8.BD.BD.E5.9C.B0.E5.9D.806)|

> 由于受公司内产品独占使用要求限制，最近这个月 TXAirPlayService 开发包暂不提供下载，我们在努力争取尽快放开下载。

## 接入流程
### 1. 配置参数
LAAirPlayManager是AirPlay的管理类，不配置它也可以正常使用。

LAAirPlayManager可以设置AirPlay的分辨率、服务名（即在AirPlay菜单中看到的名字）、TXLivePushConfig等。典型的配置代码如下：

```objective-c
TXLivePushConfig* config = [[TXLivePushConfig alloc] init];
// TODO: set fps、bitrate
[LAAirPlayManager manager].config = config;
[LAAirPlayManager manager].qualityWidth = 720;
[LAAirPlayManager manager].qualityHeight = 1280;
```
您可以在 TXLivePushConfig 里指定 FPS、码率、横屏等参数，如果您有相关领域的经验基础，需要对这些默认配置进行调整，可以阅读 [深度使用](https://www.qcloud.com/document/product/454/7884) 中的内容。

### 2. 启动录屏
```
[LAAirPlayManager manager].rtmpUrl = @"rtmp://2157.livepush.myqcloud.com/live/xxxxxx";
[[LAAirPlayManager manager] runServer];
```

启动AirPlay服务后，需要等待用户连接，SDK在连接的过程中会抛出通知并修改`airplayConState`状态。App可以监听这些通知，以调整 UI 显示：

| 状态 | 状态说明 | 
|---------|---------|
| LAAirPlayServerPublished | AirPlay服务已启动，可以在系统的AirPlay界面中选择此设备 | 
| LAAirPlayServerConnected | AirPlay服务已连接，此时已经开始录屏 | 
| LAAirPlayServerConnectFailed | 选择了AirPlay服务，超过30s仍未连上，会有此通知 | 

从AirPlay启动到连接成功，大约需要 **2～5秒** 时间。连接成功后，手机status bar的位置会出现蓝条，表示此时屏幕已被AirPlay镜像。

### 3. 事件处理

通过调用`-[LAirPlayManager setDelegate:]`设置回调，即可监听 RTMP SDK 推流事件。关于推流事件列表，请参考 [RTMP推流-事件处理](https://www.qcloud.com/document/product/454/7879#.E4.BA.8B.E4.BB.B6.E5.A4.84.E7.90.86)

### 4. 结束录屏
```
[[LAAirPlayManager manager] stopServer];
```

## 常见问题

### 1. AppStore上架

AirPlay是苹果的私有协议，因而无法通过审核，强行上架有一定风险。SDK没有使用任何私有API，请放心使用。

### 2. 启动服务后，长时间没有收到连接成功通知

请检查网络是否异常，或提示用户手动选择AirPlay设备。自动连接随系统升级可能发生改变，请参考最新小直播代码。

### 3. 码率选择

录屏画面变化波动比摄像头要大，相同分辨率和帧率下，达到同样的清晰度往往需要更高的码率，关于码率的选择请参考[如何实现好的画质](https://www.qcloud.com/document/product/454/7955)。

### 4. 直播出现帧率降低

SDK录屏多数时间都是在后台运行，iOS 限制了后台运行 App 的 CPU 使用率，以保证前台App的流畅。

如果当前手机配置较低，且有在运行大型游戏，有可能影响推流的流畅。您可以监听 `[TXLivePushDelegate onNetStatus:]` 的状态回调的 NET_STATUS_CODEC_CACHE 的值，理想情况 CACHE 的大小为0，如果大于100，则有必要通知用户先暂时回到App，待Cache降低后再玩。
