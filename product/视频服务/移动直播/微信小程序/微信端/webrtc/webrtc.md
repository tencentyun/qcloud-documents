## 版本支持
我们在 [LiteAVSDK](https://cloud.tencent.com/document/product/454/7873) 的最新版本里面加入了对 WebRTC 的支持能力，并且已经跟随微信APP的 6.6.6 版本发布出来，此文档主要介绍如何使用原生的 &lt;live-pusher&gt; 和 &lt;live-player&gt; 标签实现 WebRTC 互通能力。

## 接入成本
此文档介绍的方法接入成本偏高，适合喜欢全面定制的同学；我们同步提供了一套封装度更高的自定义组件方案 ——  [&lt;webrtc-room&gt;](https://cloud.tencent.com/document/product/454/16914) ，更加推荐您来使用。

## 接入流程

### step1. 开通云服务

小程序跟 WebRTC 的互通是基于实时音视频（[TRTC](https://cloud.tencent.com/product/trtc)）服务实现的，需要开通该服务。

- 进入实时音视频[管理控制台](https://console.cloud.tencent.com/rav)，如果服务还没有开通，点击申请开通，之后会进入腾讯云人工审核阶段，审核通过后即可开通。

- 服务开通后，进入[管理控制台](https://console.cloud.tencent.com/rav) 创建实时音视频应用，点击【确定】按钮即可。
![](https://main.qcloudimg.com/raw/20d0adeadf23251f857571a65a8dd569.png)

- 从实时音视频控制台获取`sdkAppID、accountType、privateKey`，在 step4 中会用的：
![](https://main.qcloudimg.com/raw/9a5f341883f911cf9b65b9b5487f2f75.png)



### step2. 生成key信息

按照如下表格获取关键的key信息，这是使用腾讯云互通直播服务所必须的几个信息：

| KEY | 示例    | 作用 |获取方案 |
|:--------:|:--------:|:--------:|:--------:|
| sdkappid | 1400087915  | 用于计费和业务区分 |  上文中有介绍 |
| userid   | xiaoming  | 用户名 | 可以由您的服务器指定，或者使用小程序的openid  |
| usersig | 加密字符串  | 相当于 userid 对应的登录密码 | 由您的服务器签发（PHP / JAVA） |
| roomid | 12345  | 房间号 | 可以由您的服务器指定 |
| privateMapKey | 加密字符串  | 进房票据：相当于是进入 roomid 的钥匙 | 由您的服务器签发（PHP / JAVA）|

下载 [sign_src.zip](http://dldir1.qq.com/hudongzhibo/mlvb/sign_src_v1.0.zip) 可以获得服务端签发 usersig 和 privateMapKey 的示例代码。

>生成 usersig 和 privateMapKey 的签名算法是 **ECDSA-SHA256**。

### step3. 获取roomsig
小程序端可以通过如下 url 向腾讯云请求 roomsig，roomsig 是小程序跟 WebRTC 互通必须的关键信息，请求 roomsig 所使用的关键信息已经在 step2 中做了详细描述 （这里的  **identifier** 就是上文中的 **userid** ）: 
```
https://official.opensso.tencent-cloud.com/v4/openim/jsonvideoapp?
       sdkappid=xxx&identifier=xiaoming&usersig=yyy&random=9999&contenttype=json
```

```
body:
{
    "ReqHead":
    {
        "Cmd":1,                               //命令字，固定填1
        "SeqNo":1,                             //请求序列号，uint32
        "BusType": 7,                          //业务类型，固定填7
        "GroupId": 10001                       //群组Id(房间Id)，uint32
    },
    "ReqBody":
    {
        "PrivMap": 255,                        //非必填，明文权限位
        "PrivMapEncrypt": "ed868cdc281d8b",    //必填，权限位加密串
        "IsIpRedirect": 0,                     //非必填，默认0；0非重定向；1是重定向
        "TerminalType": 1,                     //必填，终端类型，对应0x109中的TERMINAL_TYPE；Android：4；ios：2；
        "FromType": 3,                         //必填，请求来源类型：1：avsdk；2：webrtc；3：微信小程序；
        "SdkVersion": 26280566                 //非必填，整型版本号
    }
}
```

> **Attention**:
> 获取roomsig的操作必须在客户端完成，后台完成会引入选路错位问题，导致视频<font color='red'>卡顿严重</font>。



### step4. 拼装URL

如果希望将小程序跟 WebRTC 打通，不能使用普通的 rtmp:// 推流地址，而是使用新的 **room://** 协议的推流地址，该地址的格式如下：

```
room://cloud.tencent.com?sdkappid=xxx&roomid=12345&userid=xiaoming&roomsig=yyy
```

### step5. 加入（或创建）房间
在小程序的 **&lt;live-pusher&gt;** 标签里，指定 url 属性为 step4 中拼装出的url，这相当于进入指定的 roomid， &lt;live-pusher&gt; 的 视频画面会显示本地摄像头的影像。

> 如果您指定的 roomid 是第一次使用，腾讯云后台会自动为您创建一个房间号为 roomid 的房间。

### step6. 远程的视频画面
step5 解决了本地camera画面的问题，远程的画面怎么获取呢？

当 &lt;live-pusher&gt; 开始推流后，腾讯云会通过 onPushEvent (PUSH_EVT_ROOM_USERLIST = 1020) 通知您的小程序代码：房间里还有哪些人？

当有新的人加入房间以后，&lt;live-pusher&gt; 也会重新通知  onPushEvent (PUSH_EVT_ROOM_USERLIST = 1020)，这样客户可以根据 ROOM_USERLIST 的变化，了解房间里有哪些人进入了，或者哪些人离开了。

ROOM_USERLIST 里每一项都是一个二元组（如果是 1v1 的视频通话，ROOM_USERLIST 里只会有一个人）: **userid** 和 **playurl**。  userid 代表是哪个用户， playurl 则是这个用户远程画面的播放地址。

ROOM_USERLIST内容格式如下:

```json
{
    "userlist": [
        {
            "userid": "webrtc11",
            "playurl": "room://183.3.225.15:1935/webrtc/1400037025_107688_webrtc11"
        },
        {
            "userid": "webrtc12",
            "playurl": "room://183.3.225.15:1935/webrtc/1400037025_107688_webrtc12"
        }
    ]
}
```

之后，使用 **&lt;live-player&gt;** 标签，并指定 src 为 ROOM_USERLIST  里的 playurl， 即可看到远程画面了。

![](https://main.qcloudimg.com/raw/4e4ca08614c0b96a26ae19667cd2a8d4.jpg)


### step7. Chrome 对接
 了解腾讯云官网的 [webrtc](https://sxb.qcloud.com/webrtcapi/) 服务，可以对接 Chrome 端的 H5 视频通话，因为不是本文档的重点，此处不做赘述。
