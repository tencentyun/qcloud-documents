
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
![](//mc.qcloudimg.com/static/img/7116376f6f30752ba50f1c8799158c18/image.png)

## DEMO体验
**【界面截图】**
DEMO的整体实现力求简单易懂，适合只对接纯推流和播放服务的客户：
![](//mc.qcloudimg.com/static/img/a39eddc4b5f1ea062355ab865a845fb9/image.png)

**【功能支持】** 
- 推流：RTMP 推流
- 直播：RTMP、FLV格式的在线直播
- 点播：MP4、HLS和FLV格式的在线点播

**【APP安装】**
![](//mc.qcloudimg.com/static/img/6bc7924755771248a95bd02f2e008fce/image.png)

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

## 移动端SDK
- IOS更新新的美颜算法，性能及效果有较大提升。（开启硬件加速后才有效）
- Android更新新的美颜算法，解决部分机型旧美颜算法不生效的问题，同时性能及效果有显著提升。（api 18 以上且开启硬件加速后才有效）
- IOS SDK增加replaykit录屏能力支持。
- 直播播放新增Pause/Resume接口，支持暂停与恢复。
- 解决Android硬编长时间推流之后引起的无数据问题。
- 解决长时间推流时间戳跳变引起的音画不同步等流异常问题。
- 解决AAC解码在某些场景下引起的Crash问题。

**【详细说明】**
- 压缩包中是可以通过编译并运行的DEMO工程，SDK位于DEMO文件夹内。
- 开发环境的工程配置请参考 [IOS平台](https://www.qcloud.com/doc/api/258/5320) & [Android平台](https://www.qcloud.com/doc/api/258/5319)。
- 每个版本的更新情况详见[历史更新记录](https://www.qcloud.com/doc/api/258/6173)

**【测试情况】**
- 总用例数：351，通过用例数：325，不通过用例数：26

**【下载地址】**

| 操作系统 | 版本号 | 更新时间|下载链接 |
| ---- | ----------- | ---- | ---- | 
| IOS  | 1.6.2.945  | 2016-10-21 | [点击下载](http://download-10055601.cos.myqcloud.com/TXRTMPiOSDemo_1.6.2.945.zip)  |
| Android  | 1.6.2.945 | 2016-10-21 | [点击下载](http://download-10055601.cos.myqcloud.com/RTMPAndroidDemo_1.6.2.945.zip)  |

