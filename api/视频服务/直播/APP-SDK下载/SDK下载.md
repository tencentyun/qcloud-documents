## SDK开发包
- IOS、Android新增ZoomIn、ZoomOut接口
- 新增点播 MPEG4 v3解码支持
- 新增智能控速模式，根据网速自适应调整码率及分辨率
- 修复HLS、MP4录制快进问题，及多种异常模式下录制的HLS、MP4播放问题
- IOS 采集优化，彻底修复闪屏等相关问题
- Android JNI优化，修复偶现回调失败问题

**【详细说明】**
- 压缩包中是可以通过编译并运行的DEMO工程，SDK位于DEMO文件夹内。
- 开发环境的工程配置请参考 [IOS平台](https://www.qcloud.com/doc/api/258/5320) & [Android平台](https://www.qcloud.com/doc/api/258/5319)。
- 每个版本的更新情况详见[历史更新记录](https://www.qcloud.com/doc/api/258/6173)

**【测试情况】**
- 总用例数：351，通过用例数：325，不通过用例数：26

**【下载地址】**

| 操作系统 | 版本号 | 更新时间|下载链接 |
| ---- | ----------- | ---- | ---- | 
| IOS  | 1.7.0.1156  | 2016-11-11 | [点击下载](http://download-10055601.cos.myqcloud.com/TXRTMPiOSDemoSrc_1.7.0.1156.zip)  |
| Android  | 1.7.0.1156 | 2016-11-11 | [点击下载](http://download-10055601.cos.myqcloud.com/RTMPAndroidDemoSrc_1.7.0.1156.zip)  |


## DEMO体验
**【界面截图】**
![](//mc.qcloudimg.com/static/img/a39eddc4b5f1ea062355ab865a845fb9/image.png)

**【功能支持】** 
- 推流：RTMP 推流
- 直播：RTMP、FLV格式的在线直播
- 点播：MP4、HLS和FLV格式的在线点播

**【APP安装】**
![](//mc.qcloudimg.com/static/img/ab0875058708003998c3830f7329b887/image.png)

**【体验地址】**
如下是3组测试地址，RTMP推流具有排它性：同一时间、同一URL，<font color='red'>只能有一个主播</font>在推流中。所以如果您体验推流总是断开（被后台拒绝），说明地址已经被其他的体验者占用。
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

如果以上三组地址都被占用，建议您直接安装我们的演示Demo - 小直播APP，体验腾讯云的直播服务能力。

## 小直播APP
**【界面截图】**
![](//mc.qcloudimg.com/static/img/05d2e651ff6c9332211eaf7fea167cfa/image.png)

**【功能支持】** 
- 直播：支持实时直播和观看，延迟3s以内，视频秒开体验。
- 互动：支持互动消息、弹幕、点赞等互动体验。
- 回放：超过一分钟的直播内容会自动进入录播列表，提供回看能力。

**【APP安装】**
![](//mc.qcloudimg.com/static/img/0fbc0caa7f9e5a45d92e50f7cf4e6f0f/image.png)


