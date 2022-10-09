TCPlayerLite 为旧版播放器，仅包含基础直播场景的播放功能，而 TCPlayer 是兼顾直播和点播场景的完整版播放器，包含 TCPlayerLite 全部能力，同时拥有更多更强大的播放以及数据统计等功能。

若您正在使用 TCPlayerLite，建议您升级到 TCPlayer 以享受更多更全面的功能及服务，本文将为您介绍如何从 TCPlayerLite 升级为 TCPlayer。

>?TCPlayerLite 仍将持续维护现有能力，您可继续使用，但后续 Web 端播放器功能迭代将主要在 TCPlayer 内进行，TCPlayerLite不再主动做功能迭代。

## 参见文档
- [TCPlayer](https://cloud.tencent.com/document/product/881/30818)
- [TCPlayerLite](https://cloud.tencent.com/document/product/881/20207)

## 功能展示
更直观的体验 TCPlayer，可以参见 [Web 端播放器体验](https://tcplayer.vcube.tencent.com/)，可体验 TCPlayer 的各项功能并查看相关代码示例。


## 操作步骤

### 1. 替换 SDK 文件

页面引用的样式和 js 文件如下，可以参见 [TCPlayer 接入文档](https://cloud.tencent.com/document/product/881/30818)，引用最新版本的播放器 sdk 及依赖，或从文档中下载所需文件，自行部署使用。

```
<!-- 样式文件 -->
<link href="https://web.sdk.qcloud.com/player/tcplayer/release/v4.5.1/tcplayer.min.css" rel="stylesheet"/>
  
<!-- 依赖文件，按需使用-->  
<!--如果需要在 Chrome 和 Firefox 等现代浏览器中通过 H5 播放 Webrtc 视频，需要在 tcplayer.vx.x.x.min.js 之前引入 TXLivePlayer-x.x.x.min.js。-->
<!--有些浏览器环境不支持 Webrtc，播放器会将 Webrtc 流地址自动转换为 HLS 格式地址，因此快直播场景同样需要引入hls.min.x.xx.xm.js。-->
<script src="https://web.sdk.qcloud.com/player/tcplayer/release/v4.5.1/libs/TXLivePlayer-1.2.0.min.js"></script>
<!--如果需要在 Chrome 和 Firefox 等现代浏览器中通过 H5 播放 HLS 格式的视频，需要在 tcplayer.vx.x.x.min.js 之前引入 hls.min.x.xx.xm.js。-->
<script src="https://web.sdk.qcloud.com/player/tcplayer/release/v4.5.1/libs/hls.min.0.13.2m.js"></script>
<!--如果需要在现代浏览器中播放 FLV 格式的视频，需要在 tcplayer.vx.x.x.min.js 之前引入 flv.min.x.x.js。-->
<script src="https://web.sdk.qcloud.com/player/tcplayer/release/v4.5.1/libs/flv.min.1.5.js"></script>

<!--播放器脚本文件-->
<script src="https://web.sdk.qcloud.com/player/tcplayer/release/v4.5.1/tcplayer.v4.5.1.min.js"></script>
```

### 2. 初始化播放器
1. 在 TCPlayer 中初始化播放器时，可以通过 URL 形式播放，也可以通过 FileID 形式播放。这里对播放 URL 进行举例说明：
 
2. 初始化播放器时，可以通过 sources 字段指定所要播放的 URL，或者在初始化播放器之后，调用播放器实例上的 src 方法进行播放。
```
// 1. 通过 sources 字段播放
var player = TCPlayer('player-container-id',{
  sources: [{
    // 快直播地址
    src: 'webrtc://5664.liveplay.myqcloud.com/live/5664_harchar1?txSecret=f22a813b284137ed10d3259a7b5c224b&txTime=6403f7bb'
  }, {
    // HLS直播地址
    src: 'https://5664.liveplay.myqcloud.com/live/5664_harchar1.m3u8?txSecret=f22a813b284137ed10d3259a7b5c224b&txTime=6403f7bb'
  }],
  // 可配置参数说明 https://cloud.tencent.com/document/product/881/30820#options-.E5.8F.82.E6.95.B0.E5.88.97.E8.A1.A8
});

// 2. 通过 src 方法播放
player.src(url); // url 播放地址
```

3. 如果需要在直播场景设置多清晰度播放，可以参见如下方式：
```
var player = TCPlayer('player-container-id',{
  multiResolution:{
    sources:{
      'SD':[
        {
          src: 'webrtc://5664.liveplay.myqcloud.com/live/5664_harchar1?txSecret=f22a813b284137ed10d3259a7b5c224b&txTime=6403f7bb',
        }
      ],
      'HD':[
        {
          src: 'webrtc://5664.liveplay.myqcloud.com/live/5664_harchar1?txSecret=f22a813b284137ed10d3259a7b5c224b&txTime=6403f7bb',
        }
      ],
      'FHD':[
        {
          src: 'webrtc://5664.liveplay.myqcloud.com/live/5664_harchar1?txSecret=f22a813b284137ed10d3259a7b5c224b&txTime=6403f7bb',
        }
      ]
    },
    // labels:{
    //   'SD':'标清','HD':'高清','FHD':'超清'
    // },
    showOrder:['SD','HD','FHD'],
    defaultRes: 'SD'
  },
});

```

### 3. 事件监听方式
在 TCPlayer 中，监听事件的方式有所区别，所有事件参见 [API 文档](https://cloud.tencent.com/document/product/881/30820#.E4.BA.8B.E4.BB.B6)。
```
  var player = TCPlayer('player-container-id', options);
  // player.on(type, function);
  player.on('error', function(error) {
    // 做一些处理
  });
```











