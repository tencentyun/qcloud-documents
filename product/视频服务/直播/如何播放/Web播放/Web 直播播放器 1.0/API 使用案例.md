使用 API 需先完成 API 基础使用方法中的 [添加播放器容器]() 部分，添加完成后再进行 API 使用。

### Case 1：在 PC 或移动端（H5）中播放直播视频

直播 SDK 在 PC 和 H5 中的使用方式是一样的，SDK 会检测平台，自动选择最优的播放方案，例如在 PC 平台，SDK 会优先使用 Flash  播放器以适应多种视频格式的情况（需要 Flash 版本高于 10，否则将提示升级 Flash），而在移动端 H5 则会使用 video 标签进行播放（如果浏览器不支持 H5，则提示使用 QQ 浏览器），SDK 同时支持传频道 ID 或视频文件地址的方式播放。
> **注意：**
> 两种播放方式不能混合使用。

### Case 2：使用频道 ID 播放视频
```
var option = {
"channel_id": "16093425727656143421",
"app_id": "1251132611",
"width" : 480,
"height" : 320

//...可选填其他属性
};

var player = new qcVideo.Player("id_video_container", option);
```
>**注意：**
>使用频道 ID 播放视频不支持直播码的方式。

### Case 3：使用直播视频地址播放视频 
如果没有 app_id 及 channel_id，播放器也支持使用直播视频地址播放视频。
```
var option = {
"live_url" : "http://2157.liveplay.myqcloud.com/2157_358535a.m3u8",
"live_url2" : "http://2000.liveplay.myqcloud.com/live/2000_2a1.flv",
"width" : 480,
"height" : 320

//...可选填其他属性
};

var player = new qcVideo.Player("id_video_container", option);
```

> **注意：**
> 最多支持传入两个播放地址，live\_url、live\_url2 ，如果这两个地址都传了，那么会按平台支持最好的一个地址选择进行播放，例如当前环境是 PC，那么会优先选择其中为 rtmp 或 flv 的格式，当前环境为手机 H5，会优先选择 hls 格式进行播放。

### Case 4：如何使用"弹幕"功能?
在播放器初始化完成后，调用播放器对象的 addBarrage(barrage) 方法，可以为视频添加弹幕，具体参数参考 [API 方法总览]() 的说明，例如，给正在播放的视频添加两条弹幕：

```
var barrage = [
{"type":"content", "content":"hello world", "time":"1"},
{"type":"content", "content":"居中显示", "time":"1", "style":"C64B03;30","position":"center"}
];
player.addBarrage(barrage);
```
>**注意：**
>弹幕功能仅在前端实现，后台支持请自行开发，弹幕只在 PC Flash 播放器中生效，H5 暂时不具备弹幕功能。