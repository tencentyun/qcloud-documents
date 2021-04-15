文本为您介绍 P2P 通道数据分别通过 C++ .a  库调用方法和 iOS 库调用方法进行传输的操作步骤。

## C++ .a 库调用方法
使用 C++ .a 库调用方法进行 P2P 数据传输的操作步骤如下，以下示例代码仅根据相应的操作步骤展示了部分代码，完整的示例代码详情请参见 [TIoTCoreXP2PBridge](https://github.com/tencentyun/iot-link-ios/blob/master/Source/SDK/LinkVideo/TIoTCoreXP2PBridge.mm) 。

### 步骤1：P2P 通道初始化

#### 1. 注册回调
```
setUserCallbackToXp2p(XP2PDataMsgHandle, XP2PMsgHandle);
```
#### 2. 配置 IOT_P2P SDK
```
setQcloudApiCred([sec_id UTF8String], [sec_key UTF8String]);
setDeviceInfo([pro_id UTF8String], [dev_name UTF8String]);
setXp2pInfoAttributes("_sys_xp2p_info");
```
#### 3. 启动 p2p 通道
```
//demoapp作为演示需要配置第二步，客户正式发布的app不建议配置第二步，需通过自建业务服务获取xp2pInfo传入第三步的参数中
startServiceWithXp2pInfo("");
```

>!
1.	此处的 pro_id、sec_id 和 sec_key 需替换为您腾讯云 API 的 APPID、SecretId 和 SecretKey，您可登录 [访问管理控制台](https://console.cloud.tencent.com/cam/capi) >【访问密钥】>【API 密钥管理】中获取，**请务必保存好您的信息不被泄露。**
2.	demo app 目的是为了获取您该产品下的所有设备，需要您填写腾讯云 API 密钥（APPID、SecretId 和 SecretKey），不区分 C 端用户；**在实际使用场景中建议获取设备列表的操作在您自建的后台进行，腾讯云 API 的 APPID、SecretId 和 SecretKey 不保存在 App 上，避免泄露风险**。

### 步骤2：P2P 通道传输音视频流

#### 接收裸数据

1. 开始接受裸流数据
```
//参数说明:cmd直播传action=live，回放action=playback
const char *cmd = "action=live"
startAvRecvService(cmd);
```
2. 通过初始化 p2p 回调返回
```
voidXP2PDataMsgHandle(uint8_t* recv_buf, size_t recv_len) {
 ...处理接收到的裸流数据
}
```
3. 结束裸流数据
```
stopAvRecvService(nullptr);
```

#### 接收 FLV 音视频流，使用 ijkplayer 播放
1. 获取 httpflv 的 url、ipc 拼接参数
```
//直接拼接ipc.flv?action=live；本地回看拼接ipc.flv?action=playback
const char *httpflv = delegateHttpFlv();
NSString *videoUrl = [NSString stringWithFormat:@"%@ipc.flv?action=live",httpflv];
```
2. 使用 ijkplayer 播放器播放
```
[IJKFFMoviePlayerController checkIfFFmpegVersionMatch:YES];
IJKFFOptions *options = [IJKFFOptions optionsByDefault];
self.player = [[IJKFFMoviePlayerController alloc] initWithContentURL:[NSURLURLWithString:videoUrl] withOptions:options];
self.player.view.frame = self.view.bounds;
self.player.shouldAutoplay = YES;
[self.view addSubview:self.player.view];
[self.player prepareToPlay];
[self.player play];
```


### 步骤3：发送语音对讲数据


1. 准备开始发送对讲 voice 数据
```
runSendService();
```
2. 开始发送 App 采集到的音频数据
```
//此处demo发送的音频格式为flv
dataSend(pcm, pcm_size);
```

### 步骤4：P2P 通道传输自定义数据

```
NSString *cmd = @"action=user_define&cmd=custom_cmd"；
uint64_t timeout = 2*1000*1000； //2秒超时
char *buf = nullptr; //返回值
size_t len = 0;
getCommandRequestWithSync(cmd.UTF8String,&buf,&len,timeout);
```

### 步骤5：主动关闭 P2P 通道

```
stopService();
```

### 步骤6：P2P 通道关闭回调

```
//type=0:close通知； type=1:日志； type=2:json; type=3:文件开关; type=4:文件路径;type=5:p2p通道断开
char* XP2PMsgHandle(int type, constchar* msg) {
  if(type == 5){
    //断开p2p通道
  }
}
```

## iOS 库调用方法
使用 iOS 库调用方法进行 P2P 数据传输的操作步骤如下，以下示例代码仅根据相应的操作步骤展示了部分代码，完整的示例代码详情请参见 [TIoTPlayMovieVC](https://github.com/tencentyun/iot-link-ios/blob/master/Source/LinkSDKDemo/Home/Controllers/Device/TIoTPlayMovieVC.m) 。

### 步骤1：P2P 通道初始化

```
[[TIoTCoreXP2PBridge sharedInstance] startAppWith:@"" sec_key:@"" pro_id:@"" dev_name:@""];
```

### 步骤2：P2P 通道传输音视频流

####  接收裸数据
1. 开始接受裸流数据
```
//参数说明:cmd直播传action=live，回放action=playback
[[TIoTCoreXP2PBridge sharedInstance] startAvRecvService:@"action=live"];
```
2. 通过 TIoTCoreXP2PBridgeDelegate 返回裸流数据
<dx-codeblock>
:::  Java
[TIoTCoreXP2PBridge sharedInstance].delegate = self
- (void)getVideoPacket:(uint8_t *)data len:(size_t)len{
// ...处理接收到的裸流数据
:::
</dx-codeblock>
3. 结束裸流传输
```
[[TIoTCoreXP2PBridge sharedInstance] stopAvRecvService];
```

#### 接收 FLV 音视频流，使用 ijkplayer 播放

1. 获取 httpflv 的 url、ipc 拼接参数
```
//直接拼接ipc.flv?action=live；本地回看拼接ipc.flv?action=playback
NSString *urlString = [[TIoTCoreXP2PBridge sharedInstance] getUrlForHttpFlv]?:@"";
NSString *videoUrl = [NSString stringWithFormat:@"%@ipc.flv?action=playback",urlString];
```
2. 使用 ijkplayer 播放器播放
```
self.player = [[IJKFFMoviePlayerController alloc] initWithContentURL:[NSURL URLWithString:videoUrl] withOptions:options];
self.player.shouldAutoplay = YES;
[self.player prepareToPlay];
[self.player play];
```

### 步骤3：发送语音对讲数据
```
//开始对讲
[[TIoTCoreXP2PBridge sharedInstance] sendVoiceToServer];
//结束对讲
[[TIoTCoreXP2PBridge sharedInstance] stopVoiceToServer];
```

### 步骤4： P2P  通道传输自定义数据

```
[[TIoTCoreXP2PBridge sharedInstance] getCommandRequestWithAsync:@"action=user_define&cmd=custom_cmd" timeout:2*1000*1000 completion:^(NSString * _Nonnull jsonList) {
 ...处理返回的数据
}];
```

### 步骤5：主动关闭 P2P 通道

```
[[TIoTCoreXP2PBridge sharedInstance] stopService];
```

### 步骤6：P2P 通道关闭回调

```
//type=0:close通知； type=1:日志； type=2:json; type=3:文件开关; type=4:文件路径;type=5:p2p通道断开
char* XP2PMsgHandle(int type, constchar* msg) {
  if(type == 5){
    //断开p2p通道
  }
}
```
>?此步骤示例代码详情请参见 [TIoTCoreXP2PBridge](https://github.com/tencentyun/iot-link-ios/blob/master/Source/SDK/LinkVideo/TIoTCoreXP2PBridge.mm) 。
