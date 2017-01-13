## SDK
- Fixing the problem of interface response failure when flashlight is touched on Android;
- Fixing the problem of inaccurate FPS encoded by some Android models;
- Fixing the problem of abnormal exit at a small probability when HLS/MP4 playing ends on Android;

**Details**
- The DEMO project that can be compiled and operated is contained in the compressed package, and the SDK is in the DEMO folder.
- For the engineering configuration of the development environment, please refer to [iOS Platform](https://www.qcloud.com/doc/api/258/5320) & [Android Platform](https://www.qcloud.com/doc/api/258/5319).
- For the update details of each version, refer to [History Update Record](https://www.qcloud.com/doc/api/258/6173)

**Test Result**
- Total cases: 351; Passed cases: 325; Failed cases: 26

**[Download Address]**

| OS | Version | Update Time | Download Link |
| ---- | ----------- | ---- | ---- | 
| iOS | 1.8.0.1459 | 2016-12-09 | [Click to download](http://download-10055601.cos.myqcloud.com/RTMPIOSSDK1.8.0.1459.zip)  |
| Android | 1.8.0.1459 | 2016-12-09 | [Click to download](http://download-10055601.cos.myqcloud.com/RTMPAndroidSDK1.8.0.1459.zip)  |


## DEMO
**Screenshots**
![](//mc.qcloudimg.com/static/img/a39eddc4b5f1ea062355ab865a845fb9/image.png)

**Features** 
- Push: RTMP push
- LVB: Online LVB in RTMP and FLV formats
- VOD: Online VOD in MP4, HLS and FLV formats

**App Installation**
![](//mc.qcloudimg.com/static/img/ab0875058708003998c3830f7329b887/image.png)

**Test Addresses**
Three groups of test addresses are provided below, and RTMP push is exclusive; <font color='red'>only one VJ can</font> implement push at the same time for the same URL. Therefore, if the push you are experiencing is frequently disconnected (rejected by the background), it indicates that the address has been by used by other experimenter(s).
```
// Address group 1:
PUSH(RTMP): rtmp://2000.livepush.myqcloud.com/live/2000_1f4652b179af11e69776e435c87f075e?bizid=2000
PLAY(FLV) : http://2000.liveplay.myqcloud.com/live/2000_1f4652b179af11e69776e435c87f075e.flv
PLAY(HLS) : http://2000.liveplay.myqcloud.com/2000_1f4652b179af11e69776e435c87f075e.m3u8
```

```
// Address group 2:
PUSH(RTMP): rtmp://2000.livepush.myqcloud.com/live/2000_44c6e64e79af11e69776e435c87f075e?bizid=2000
PLAY(FLV) : http://2000.liveplay.myqcloud.com/live/2000_44c6e64e79af11e69776e435c87f075e.flv
PLAY(HLS) : http://2000.liveplay.myqcloud.com/2000_44c6e64e79af11e69776e435c87f075e.m3u8
```

```
// Address group 3:
PUSH(RTMP): rtmp://2000.livepush.myqcloud.com/live/2000_4eb4da7079af11e69776e435c87f075e?bizid=2000
PLAY(FLV) : http://2000.liveplay.myqcloud.com/live/2000_4eb4da7079af11e69776e435c87f075e.flv
PLAY(HLS) : http://2000.liveplay.myqcloud.com/2000_4eb4da7079af11e69776e435c87f075e.m3u8
```

If all the above three groups of addresses are occupied, you are recommended to directly install our Demo - Little Live APP and experience the LVB service capabilities of Tencent Cloud.

## Little Live APP
**Screenshots**
![](//mc.qcloudimg.com/static/img/05d2e651ff6c9332211eaf7fea167cfa/image.png)

**Features** 
- LVB: Supports real-time LVB and watching, with a delay not exceeding 3s; video can be opened in seconds.
- Interaction: Supports interaction experience including interaction message, bullet screen and liking.
- Playback: Allows for automatic storage of the LVB content exceeding 1 minute in the recording and broadcasting list, and provides the playback feature.

**App Installation**
![](//mc.qcloudimg.com/static/img/0fbc0caa7f9e5a45d92e50f7cf4e6f0f/image.png)


