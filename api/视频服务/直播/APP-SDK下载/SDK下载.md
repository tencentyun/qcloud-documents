
## DEMO体验
**【界面截图】**
DEMO的整体实现力求简单易懂，适合只对接纯推流和播放服务的客户：
![](//mc.qcloudimg.com/static/img/a39eddc4b5f1ea062355ab865a845fb9/image.png)

**【功能支持】** 
- 推流：RTMP 推流
- 直播：RTMP、FLV格式的在线直播
- 点播：MP4、HLS和FLV格式的在线点播

**【APP安装】**

| 操作系统 | 版本号 | 更新时间|下载链接 |
| ---- | ----------- | ---- | ---- | 
| IOS  | 1.5.1.301(最新版本苹果审核中)  | 2016-08-04 | ![qr](//mc.qcloudimg.com/static/img/5961cfb63a93a001b8861db2a2269496/image.png)|
| Android  | 1.6.0.475 | 2016-09-02 | [点击下载](http://sdk-10065671.cos.myqcloud.com/rtmpdemo-1.6.0.475.apk)  |

**【体验地址】**
RTMP推流具有排它性：同一时间、同一URL，<font color='red'>只能有一个主播</font>在推流中。所以如果您体验推流总是断开（被后台拒绝），说明地址已经被其他的体验者占用，推荐您直接[开通腾讯云直播服务](https://console.qcloud.com/live)并创建自己的频道进行体验。

如下是3组测试地址：

```
//第一组地址：
PUSH(RTMP): rtmp://2000.livepush.myqcloud.com/live/2000_1f4652b179af11e69776e435c87f075e?bizid=2000
PLAY(FLV) : http://2000.liveplay.myqcloud.com/live/2000_1f4652b179af11e69776e435c87f075e.flv
PLAY(HLS) : http://2000.liveplay.myqcloud.com/2000_1f4652b179af11e69776e435c87f075e.m3u8
```

```
//第二组地址：
PUSH(RTMP): rtmp://2000.livepush.myqcloud.com/live/2000_44c6e64e79af11e69776e435c87f075e?bizid=2000
PLAY(FLV) : http://2000.liveplay.myqcloud.com/live/2000_44c6e64e79af11e69776e435c87f075e.flv
PLAY(HLS) : http://2000.liveplay.myqcloud.com/2000_44c6e64e79af11e69776e435c87f075e.m3u8
```

```
//第三组地址：
PUSH(RTMP): rtmp://2000.livepush.myqcloud.com/live/2000_4eb4da7079af11e69776e435c87f075e?bizid=2000
PLAY(FLV) : http://2000.liveplay.myqcloud.com/live/2000_4eb4da7079af11e69776e435c87f075e.flv
PLAY(HLS) : http://2000.liveplay.myqcloud.com/2000_4eb4da7079af11e69776e435c87f075e.m3u8
```



## 小直播体验
**【界面截图】**
小直播是基于腾讯视频云服务实现的一个直播APP的原型软件，开放终端和后台的实现源码，适合零基础的客户进行参考和评估之用：
![](//mc.qcloudimg.com/static/img/05d2e651ff6c9332211eaf7fea167cfa/image.png)

**【功能支持】** 
- 直播：支持实时直播和观看，延迟3s以内，视频秒开体验。
- 互动：支持互动消息、弹幕、点赞等互动体验。
- 回看：超过一分钟的直播内容会自动进入录播列表，提供回看能力。

**【后台服务】**
小直播的后台服务目前部署于一台普通的腾讯云虚拟主机上，基于PHP技术构建，提供源码下载和参考。

**【APP安装】**

| 操作系统 | 版本号 | 更新时间|下载链接 |
| ---- | ----------- | ---- | ---- | 
| IOS  | 苹果审核中...  | 苹果审核中... | 苹果审核中...|
| Android  | 1.1.1.493 | 2016-09-13 | [点击下载](http://sdk-10065671.cos.myqcloud.com/xiaozhibo_1.1.1.493.apk)  |

## 移动端SDK

**【最新特性】**
- 增加音频数据加速处理能力，提升速播体验，用户无感知降低播放延迟；
- 针对推流后台主动拒绝的情况，增加了PUSH_WARNING_SERVER_DISCONNECT通知；
- 优化首次打开黑屏问题，首帧展示之前OpenGL渲染层不展示；
- IOS增加横屏推流及本地播放支持，使用详见接口变更。
- 支持短时间内切到后台后可以保持rtmp推流连接（70s以内不断链，IOS需要支持后台运行才可使用此特性）
- 引入openGL冲突检查机制，避免player释放问题引起的IOS闪屏；
- 优化log性能，增加对外log回调接口 (setLogLevel接口不影响LOG回调函数的行为)；

**【详细说明】**
- 压缩包中是可以通过编译并运行的DEMO工程，SDK位于DEMO文件夹内。
- 开发环境的工程配置请参考 [IOS平台](https://www.qcloud.com/doc/api/258/5320) & [Android平台](https://www.qcloud.com/doc/api/258/5319)。
- 每个版本的更新情况详见[历史更新记录](https://www.qcloud.com/doc/api/258/6173)

**【测试情况】**
- 总用例数：259 通过用例数：245 不通过用例数：14

【**接口变更**】
- IOS 中的 TXLivePush类增加新的接口函数：
```
//IOS Push 新增旋转接口，用于解决本地横屏推流时画面旋转方向错误问题，使用方式请参考接口文档注释；
-(void) setRenderRotation:(int)rotation;
```

**【下载地址】**

| 操作系统 | 版本号 | 更新时间|下载链接 |
| ---- | ----------- | ---- | ---- | 
| IOS  | 1.6.0.475  | 2016-09-02 | [点击下载](http://sdk-10065671.cos.myqcloud.com/TX_RTMPSDK_IOS_1.6.0.475.zip)  |
| Android  | 1.6.0.475 | 2016-09-02 | [点击下载](http://sdk-10065671.cos.myqcloud.com/TX_RTMPSDK_Android_1.6.0.475.zip)  |

