本文档是介绍腾讯云视立方 Web 超级播放器 Adapter，它可以帮助腾讯云客户通过灵活的接口，快速实现第三方播放器与云点播能力的结合，实现视频播放功能。Web 超级播放器 Adapter 支持获取视频基本信息、视频流信息、关键帧与缩略图信息等，支持私有加密，本文档适合有一定 Javascript 语言基础的开发人员阅读。

## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | -  | -  | -  | -  | &#10003;  | -  |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。

## SDK 集成

Web 超级播放器 Adapter 提供 **CDN 集成**和 **npm 集成**两种集成方式：

#### CDN 集成

在需要播放视频的页面中引入初始化脚本，脚本会在全局下暴露 TcAdapter 变量。

```javascript
<script src="https://cloudcache.tencentcs.com/qcloud/video/dist/tcadapter.1.0.0.min.js"></script>
```

#### npm 集成

```javascript
// npm install
npm install --save tcadapter

// import TcAdapter
import TcAdapter from 'tcadapter';
```



## 放置播放器容器

在需要展示播放器的页面加入容器，TcAdapter 仅需要承载播放视频的容器，播放样式和自定义功能可由第三方播放器或使用者自行实现：

```javascript
<video id="player-container-id">
</video>
```

## SDK 使用说明

### 检测开发环境

检测当前环境是否支持 TcAdapter。

```javascript
TcAdapter.isSupported();
```

### 初始化 Adapter

初始化 Adapter，创建 Adapter 实例。初始化过程会请求腾讯云点播服务器，获取视频文件信息。

**接口**

```javascript
const adapter = new TcAdapter('player-container-id', {
  fileID: string,
  appID: string,
  psign: string,
  hlsConfig: {}
}, callback);
```

**参数说明**

| 参数名    | 类型                  | 描述                                             |
| --------- | --------------------- | ------------------------------------------------ |
| appID     | String                | 点播账号的 APPID                             |
| fileID    | String                | 要播放的视频 fileId                              |
| psign     | String                | 超级播放器签名                                   |
| hlsConfig | HlsConfig             | HLS 相关设置，可使用 `hls.js` 支持的任意参数 |
| callback  | TcAdapterCallBack | 初始化完成回调，可以在此方法之后获取视频基本信息 |

> ! TcAdapter 底层基于 `hls.js` 实现，可以通过 HlsConfig 接收 `hls.js` 支持的任意参数，用于对播放行为的精细调整。

### 获取视频基本信息

获取视频的信息， 必须是在初始化之后才生效。

**接口**

```javascript
VideoBasicInfo adapter.getVideoBasicInfo();
```

**参数说明**

VideoBasicInfo 参数如下：

| 参数名      | 类型   | 描述               |
| ----------- | ------ | ------------------ |
| name        | String | 视频名称           |
| duration    | Float  | 视频时长，单位：秒 |
| description | String | 视频描述           |
| coverUrl    | String | 视频封面           |

### 获取视频流信息

**接口**

```javascript
List<StreamingOutput> adapter.getStreamimgOutputList();
```

**参数说明**

StreamingOutput 参数如下：

| 参数名     | 类型   | 描述                                                         |
| ---------- | ------ | ------------------------------------------------------------ |
| drmType    | String | 自适应码流保护类型，目前取值有 plain 和 simpleAES。plain 表示不加密，simpleAES 表示 HLS 普通加密 |
| playUrl    | String | 播放 URL                                                     |
| subStreams | List   | 自适应码流子流信息，类型为 [SubStreamInfo](#SubStreamInfo)   |

SubStreamInfo 参数如下：[](id:SubStreamInfo)

| 参数名         | 类型   | 描述                                 |
| -------------- | ------ | ------------------------------------ |
| type           | String | 子流的类型，目前可能的取值仅有 video |
| width          | Int    | 子流视频的宽，单位：px               |
| height         | Int    | 子流视频的高，单位：px               |
| resolutionName | String | 子流视频在播放器中展示的规格名     |

### 获取关键帧打点信息

**接口**

```java
List<KeyFrameDescInfo> adapter.getKeyFrameDescInfo();
```

**参数说明**

KeyFrameDescInfo 参数如下：

| 参数名     | 类型   | 描述          |
| ---------- | ------ | ------------- |
| timeOffset | Float  | 1.1           |
| content    | String | "片头开始..." |

### 获取缩略图信息

**接口**

```javascript
ImageSpriteInfo adapter.getImageSpriteInfo();
```

**参数说明**

ImageSpriteInfo 参数如下：

| 参数名    | 类型   | 描述                               |
| --------- | ------ | ---------------------------------- |
| imageUrls | List   | 缩略图下载 URL 数组，类型为 String |
| webVttUrl | String | 缩略图 VTT 文件下载 URL            |

### 监听事件

播放器可以通过初始化返回的对象进行事件监听，示例：

```javascript
const adapter = TcAdapter('player-container-id', options);
adapter.on(TcAdapter.TcAdapterEvents.Error, function(error) {
  // do something
});
```

其中 type 为事件类型，支持的事件包括 HLS 原生的事件以及以下事件，可从 `TcAdapter.TcAdapterEvents` 中访问到事件名称：

| 名称           | 介绍                                                         |
| :------------- | :----------------------------------------------------------- |
| LOADEDMETADATA | 通过 playcgi 获取到了相应的视频信息，在此事件回调中可以获取视频相关信息 |
| HLSREADY       | hls实例创建完成，可以在此时机调用 hls 实例对象上的各种属性和方法 |
| ERROR | 出现错误时触发，可从回调参数中查看失败具体原因 |


### 获取 Hls 实例
adapter 底层基于 hls.js 实现，可以通过 adapter 实例访问到 HLS 实例以及实例上的属性和方法，用于实现对播放流程的精细控制。

```javascript
adapter.on('hlsready', () => {
  const hls = adapter.hls;
  // ...
})
```

> ? 具体请参见 [hls.js](https://github.com/video-dev/hls.js/)。



## 示例

### 例1：在 React 中使用 TcAdapter 

具体示例，请参见 [GitHub](https://github.com/tcplayer/tcadapter-combine-video)。

```javascript
import { useEffect, useRef } from 'react';
import TcAdapter from 'tcadapter';

function App() {
  if (!TcAdapter.isSupported()) {
    throw new Error('current environment can not support TcAdapter');
  }

  const videoRef = useRef(null);
  useEffect(() => {
    const adapter = new TcAdapter(videoRef.current, {
      appID: '1500002611',
      fileID: '5285890813738446783',
      psign: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6MTUwMDAwMjYxMSwiZmlsZUlkIjoiNTI4NTg5MDgxMzczODQ0Njc4MyIsImN1cnJlbnRUaW1lU3RhbXAiOjE2MTU5NTEyMzksImV4cGlyZVRpbWVTdGFtcCI6MjIxNTY1MzYyMywicGNmZyI6ImJhc2ljRHJtUHJlc2V0IiwidXJsQWNjZXNzSW5mbyI6eyJ0IjoiMjIxNTY1MzYyMyJ9fQ.hRrQYvC0UYtcO-ozB35k7LZI6E3ruvow7DC0XzzdYKE',
      hlsConfig: {},
    }, () => {
      console.log('basicInfo', adapter.getVideoBasicInfo());
    });

    adapter.on(TcAdapter.TcAdapterEvents.HLSREADY, () => {
      const hls = adapter.hls;
			// ...
    })
  }, []);
  

  const play = () => {
    videoRef.current.play();
  }

  return (
    <div>	
      <div>
        <video id="player" ref={ videoRef }></video>
      </div>
      <button onClick={play}>play</button>
    </div>
  );
}

export default App;

```

### 例2：TcAdapter 与 videojs 结合

具体示例，请参见 [GitHub](https://github.com/tcplayer/tcadapter-combine-videojs)。

```javascript
// 1. videojs 播放 hls 会使用 @videojs/http-streaming，所以我们开发一套使用 tcadapter 播放的策略覆盖原有逻辑（也可以直接修改 @videojs/http-streaming 内部逻辑）

// src/js/index.js
import videojs from './video';
import '@videojs/http-streaming';
import './tech/tcadapter'; // 新增逻辑
export default videojs;


// src/js/tech/tcadapter.js
import videojs from '../video.js';
import TcAdapter from 'tcadapter';

class Adapter {
  constructor(source, tech, options) {
    const el = tech.el();
    // 获取参数并初始化实例
    const adapter = new TcAdapter(el, {
      appID: '1500002611',
      fileID: '5285890813738446783',
      psign: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6MTUwMDAwMjYxMSwiZmlsZUlkIjoiNTI4NTg5MDgxMzczODQ0Njc4MyIsImN1cnJlbnRUaW1lU3RhbXAiOjE2MTU5NTEyMzksImV4cGlyZVRpbWVTdGFtcCI6MjIxNTY1MzYyMywicGNmZyI6ImJhc2ljRHJtUHJlc2V0IiwidXJsQWNjZXNzSW5mbyI6eyJ0IjoiMjIxNTY1MzYyMyJ9fQ.hRrQYvC0UYtcO-ozB35k7LZI6E3ruvow7DC0XzzdYKE',
      hlsConfig: {},
    });
    adapter.on(TcAdapter.TcAdapterEvents.LEVEL_LOADED, this.onLevelLoaded.bind(this));
  }

  dispose() {
    this.hls.destroy();
  }

  onLevelLoaded(event) {
    this._duration = event.data.details.live ? Infinity : event.data.details.totalduration;
  }

}

let hlsTypeRE = /^application\/(x-mpegURL|vnd\.apple\.mpegURL)$/i;
let hlsExtRE = /\.m3u8/i;

let HlsSourceHandler = {
  name: 'hlsSourceHandler',
  canHandleSource: function (source) {
    // skip hls fairplay, need to use Safari resolve it.
    if (source.skipHlsJs || (source.keySystems && source.keySystems['com.apple.fps.1_0'])) {
      return '';
    } else if (hlsTypeRE.test(source.type)) {
      return 'probably';
    } else if (hlsExtRE.test(source.src)) {
      return 'maybe';
    } else {
      return '';
    }
  },

  handleSource: function (source, tech, options) {
    if (tech.hlsProvider) {
      tech.hlsProvider.dispose();
      tech.hlsProvider = null;
    } else {
      // hls关闭自动加载后，需要手动加载资源
      if (options.hlsConfig && options.hlsConfig.autoStartLoad === false) {
        tech.on('play', function () {
          if (!this.player().hasStarted()) {
            this.hlsProvider.hls.startLoad();
          }
        });
      }
    }
    tech.hlsProvider = new Adapter(source, tech, options);
    return tech.hlsProvider;
  },
  canPlayType: function (type) {
    if (hlsTypeRE.test(type)) {
      return 'probably';
    }
    return '';
  }
};

function mountHlsProvider(enforce) {
  if (TcAdapter && TcAdapter.isSupported() || !!enforce) {
    try {
      let html5Tech = videojs.getTech && videojs.getTech('Html5');
      if (html5Tech) {
        html5Tech.registerSourceHandler(HlsSourceHandler, 0);
      }
    } catch (e) {
      console.error('hls.js init failed');
    }
  } else {
    //没有引入tcadapter 或者 MSE 不可用或者x5内核禁用
  }
}
mountHlsProvider();
export default Adapter;

```

