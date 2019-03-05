﻿
 ## 功能介绍
所谓录制回看，是指您可以把用户整个直播过程录制下来，然后作为点播视频用于回看，如下图：
![](//mccdn.qcloud.com/static/img/a8240c996be9eab19d5dc40b9e3df779/image.png)
在APP上线的初期阶段，由于主播数量比较少，所以在直播列表中加入录制回看，能够在一定程度上丰富APP在观众端的信息量。即使到APP成长起来主播数量形成规模以后，好的直播内容的沉淀依然是必不可少的一个部分，每个主播的个人介绍里除了有名字、照片和个人信息，历史直播的视频回看更是不可或缺的一个重要组成部分。

## 服务开通
录制回看功能依托于腾讯云的**点播服务**后台集群支撑，如果您想要对接这个功能，首先需要在腾讯云的管理控制台[开通点播服务](http://console.cloud.tencent.com/video)。

开通点播服务之后，新录制的文件也可以在点播控制台的[视频管理](http://console.cloud.tencent.com/video/videolist)里找到它们。

## 开启录制
腾讯云支持对视频直播过程进行全程录制，您可以使用两种方式开启录制功能：

- **方案一：全局开启**
即指定所有直播的视频流全部开启或者关闭录制，在[直播管理控制台](https://console.cloud.tencent.com/live)中可以对其进行设置，见下图：
![](//mc.qcloudimg.com/static/img/fd4a3e35fdb486d9d9053fe7f29760a8/image.png)

- **方案二：指定开启**
在所有直播的视频流全部关闭录制的情况下，您依然可以对个别重要的视频流开启录制，操作方法是在推流URL后拼接 **&record=flv** 或者 **&record=mp4** 参数，例如：
```
rtmp://2121.livepush.myqcloud.com/live/2121_15919131751?txSecret=aaa&txTime=bbb&record=flv
```

## 文件落地
- **方案一：消息通知**
您可以使用腾讯云的**[事件通知服务](https://cloud.tencent.com/doc/api/258/5957)**：您的服务器注册一个自己的**回调URL**给腾讯云，腾讯云会在一个新的录制文件生成时通过这个URL通知给您。

 如下是一个典型的通知消息，它的含义是：一个id为9192487266581821586的新的flv录制文件已经生成，播放地址为：'http://200025724.vod.myqcloud.com/200025724_ac92b781a22c4a3e937c9e61c2624af7.f0.flv'。
```json
{
    "channel_id": "2121_15919131751",
    "end_time": 1473125627,
    "event_type": 100,
    "file_format": "flv",
    "file_id": "9192487266581821586",
    "file_size": 9749353,
    "sign": "fef79a097458ed80b5f5574cbc13e1fd",
    "start_time": 1473135647,
    "stream_id": "2121_15919131751",
    "t": 1473126233,
    "video_id": "200025724_ac92b781a22c4a3e937c9e61c2624af7",
    "video_url": "http://200025724.vod.myqcloud.com/200025724_ac92b781a22c4a3e937c9e61c2624af7.f0.flv"
}
```

- **方案二：主动查询**
您可以通过腾讯云的文件查询接口（**[Live_Tape_GetFilelist](https://cloud.tencent.com/doc/api/258/5960)**）定时地查看是否有新的录制文件生成，不过这种方案在要查询的频道数特别多的时候，响应速度不理想，同时调用频率也不能太快（仅对刚结束的频道进行调用为宜），这种方案的实时性和可靠性不高，并不推荐频繁使用。

## 视频播放
您的服务器获得录制的文件后，就可以生成播放URL了，APP拿到URL后交给RTMP SDK的点播播放模块就可以观看回放:
- [IOS平台参考文档](https://cloud.tencent.com/doc/api/258/4738)
- [Android平台参考文档](https://cloud.tencent.com/doc/api/258/4739)
- [Web平台参考文档](https://cloud.tencent.com/doc/api/258/5706)