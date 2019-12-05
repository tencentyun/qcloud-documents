
## 小直播体验
**【界面截图】**
小直播是基于腾讯视频云服务实现的一个直播APP的原型软件，开放终端和后台的实现源码，适合零基础的客户进行参考和评估之用：
![](//mc.qcloudimg.com/static/img/05d2e651ff6c9332211eaf7fea167cfa/image.png)

**【功能支持】** 
- 直播：支持实时直播和观看，延迟3s以内，视频秒开体验，支持游戏录屏和背景混音。
- 互动：支持互动消息、弹幕、点赞等互动体验。
- 回看：超过一分钟的直播内容会自动进入录播列表，提供回看能力。

**【后台服务】**
小直播的后台服务目前部署于一台普通的腾讯云虚拟主机上，基于PHP技术构建，提供源码下载和参考。

**【APP安装】**
![](//mc.qcloudimg.com/static/img/864ed43be9cf7ab4dc912faab8eb4d61/image.png)

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

RTMP推流具有排它性：同一时间、同一URL，<font color='red'>只能有一个主播</font>在推流中。所以如果您体验推流总是断开（被后台拒绝），说明地址已经被其他的体验者占用，推荐您直接开通腾讯云直播服务并创建自己的频道进行体验，具体方法如下：

**【新的地址】**

1. 登录[直播管理控制台](https://console.cloud.tencent.com/live)，如果您曾经开通过直播服务，将直接进入到频道管理页面，如果您是第一次登录，系统将引导您开通直播服务，并为您分配10G的免费流量供您体验。

2. 如果您已经开通直播服务，进入[直播管理](https://console.cloud.tencent.com/live/livemanage)，点击**创建频道**：
 
3. 按要求填入频道名称、频道描述、直播源名称，“实时转码”只勾选“原始视频”，“水印设置”选择“不使用水印”，“接收方设置”中选中RTMP/FLV。

4. 保存之后，页面直接跳转到刚刚创建的频道详情页，复制推流地址和播放地址，分别生成二维码待用：

![](//mc.qcloudimg.com/static/img/ba5c15d70ff977a7a4288c7fdfe066b4/image.png)


