## 概述

腾讯云 H5-P2P 直播解决方案，可帮助用户直接使用经过大规模验证的直播流媒体分发服务。用户可通过 SDK 中简洁的接口快速同自有应用集成，实现 H5 P2P 直播功能。



## 运行条件

### 1. sdk 运行需要浏览器支持以下特性:

- Media Source Extention
- WEB RTC
- websocket

| 浏览器版本要求 |  桌面  |
| -------------- | :----: |
| chrome         |  55+   |
| firefox        |  65+   |
| safari         |  11+   |
| edge           |  16+   |
| IE             | 不支持 |

> ? 您可 [点击此处](https://xp2p-1258344699.cos.ap-nanjing.myqcloud.com/demo/h5-support/index.html) 查看浏览器是否支持以上特性

### 2. 支持的流媒体格式

- http-flv

## Demo 示例

- 集成 SDK 到播放器（flv.js）编写 loader 示例代码，请参见 [此处](https://xp2p-1258344699.cos.ap-nanjing.myqcloud.com/demo/h5_flv_p2p/index.html)。
- 集成 SDK 到播放器（flv.js）的 Demo，请参见 [为播放器编写loader](#m1)一节。

## 准备工作

在 [提交 X-P2P 开通申请](https://cloud.tencent.com/apply/p/npwwbfakdis) 后，再联系我们的研发工程师，确保 CDN 分发域名及 domain 白名单已完成配置。

## 接口说明

### `QVBP2P`

QVBP2P 是 sdk lib 名称, 可以访问到一些常量和生成 qvbp2p 实例, 如下 `qvbp2p` 表示 sdk 实例

#### `构造函数`

QVBP2P 构造函数

##### 语法

```typescript
new QVBP2P(config);
```

##### 参数

```typescript
type config = {
  debug?: boolean;   // true打开debug日志
  pcdnMixed: string; // 拉流域名, 邮件给出 
  partner: string; // 邮件给出
  appId: number;    // 邮件给出
  bizId: string; // 邮件给出
}
```

##### 返回值

```
sdk 实例
```

##### 例子

```typescript
const { pcdnMixed, partner, domain, appId, bizId } = p2pClientConfig;
const qvbp2p = new QVBP2P({
     pcdnMixed,
     partner,
     domain,
     appId,
     bizId,
})
```

### 常量

#### `QVBP2P.version`

查看当前sdk版本

#### `QVBP2P.ComEvents`

SDK 会抛出的事件,客户端需监听处理

##### 定义

```typescript
enum ComEvents {
  STATE_CHANGE // 目前sdk仅抛出了这一个事件, 客户需要监听这个事件,并处理对应的消息,消息码见 QVBP2P.ComCode
}
```

##### 例子

```typescript
见listen()和demo

```



#### `QVBP2P.ComCodes`

QVBP2P.ComEvents.STATE_CHANGE 事件对对应多种消息, 通过此处的消息码区分处理

##### 定义

```typescript
enum ComCodes {
  ROLLBACK, // 回退
  RECEIVE_BUFFER, // 接收flv chunk数据
}
```

- 回退说明: 当 sdk 拉流失败,播放长时间卡顿等异常情况时候, 会抛出此事件, 客户播放器此时需要使用原有方式重新尝试拉流，不使用 P2P

##### 例子

```typescript
见listen()和demo

```

### 方法

#### `QVBP2P.isSupported()`

静态方法,判断当前浏览器是否支持sdk

##### 语法

```typescript
QVBP2P.isSupported()
```

##### 返回值

```typescript
type boolean  // true表示支持sdk
```

##### 例子

```typescript
if (QVBP2P.isSupported()) {
  // 支持sdk,可以使用
}
```



#### `listen()`

向 sdk 注册监听的事件

##### 语法

```typescript
qvbp2p.listen(event, callback)
```

##### 参数

```typescript
type event = QVBP2P.ComEvents.STATE_CHANGE;
type callback = (event: QVBP2P.ComEvents.STATE_CHANGE, data: CallbackData) => void;

type ReceiveBufferCallbackData = { 
    code: ComCodes.RECEIVE_BUFFER, // 接收数据
    payload: ArrayBuffer; // flv chunk数据
}

type RollbackCallbackData = {
    code: ComCodes.ROLLBACK
};

type CallbackData = ReceiveBufferCallbackData | RollbackCallbackData;
  
  
```

##### 返回值

```
void
```

##### 例子

```
见demo
```

#### `setMediaElement()`

给 sdk 传入当前的 videoElement, sdk 使用 videoElement 进行事件监控，buffer 查询.请在播放前后尽快设置

##### 语法

```typescript
qvbp2p.setMediaElement(videoElement)
```

##### 参数

```typescript
type videoElement: HTMLVideoElement;
```

##### 返回值

```
void
```

##### 例子

```typescript
const videoEl = document.getElementById('your-video-id')
qvbp2p.setMediaElement(videoEl);
```

#### `loadSource()`

启动 sdk 拉流功能, 此时 sdk 会向 cdn 和 p2p 节点进行请求数据，并通过事件返回，此方法(不能重复调用)

##### 语法

```typescript
qvbp2p.loadSource(config)
```

##### 参数

```typescript
type config = {
  src: string; // 原始flv流的url. sdk会进行解析, 然后拼出sdk内部使用的url进行拉流
}
```

##### 返回值

```
void
```

##### 例子

```typescript
qvbp2p.loadSource({
  src: 'https://xxxx.xxx.xxx/live/teststrea.flv?xxxx'
})
```

#### `destroy()`

中断拉流, 销毁 sdk(不能重复调用).销毁后的sdk也不能继续使用.需要重新创建 sdk 实例

##### 语法

```typescript
qvbp2p.destroy();
```



## 集成工作

### 1. 首先加载 sdk

```html
<script src='qvbp2p_common.js'></script>
```

[](id:m1)

### 2. 为播放器编写 loader / 集成 sdk 到播放器

通常H5 FLV player有不同的loader用于下载, 例如flv.js有如下loader

```
fetch-stream-loader.js
websocket-loader.js
xhr-moz-chunked-loader.js
```

而集成 XP2P SDK 的过程, 即为播放器编写 P2P-loader，在 loader 中对 sdk 进行生命周期管理, 并接收 sdk 抛出的 flv 数据和事件

如下通过集成到flv.js, 来演示sdk接口的使用方法和注意事项

```typescript
import { BaseLoader } from './loader.js';
// QVBP2P默认挂在window上
// 不支持多实例

/**
 * 为flv.js编写的p2p loader,继承了flv.js Loader接口, 可以将我们的p2p sdk集成到flv.js
 */
class QVBP2PLoader extends BaseLoader {
    /**
     * 确定当前环境是否支持sdk
     * @returns {boolean}
     */
    static isSupported() {
        return window.QVBP2P && window.QVBP2P.isSupported();
    }

    constructor(seekHander, config) {
        super();
        this._qvbp2p = null;
        // flv.js成员,非sdk必须
        this._receivedLength = 0;
        this._config = config;
    }

    /**
     * @public
     */
    destroy() {
        this._destroyQVBP2P();
        super.destroy();
    }

    /**
     * 通过p2p sdk播放一个url
     * @public
     * @param {object} dataSource
     * @param {string} dataSource.url
     */
    open(dataSource) {
        // 初始化sdk实例
        this._createQVBP2P();

        // 监听sdk事件
        this._qvbp2p.listen(
            window.QVBP2P.ComEvents.STATE_CHANGE,
            this._onQVBP2PStateChange.bind(this)
        );

        // @todo 绑定video元素到sdk, 需要替换为客户实际的videoEl
        const videoEl = document.getElementById(this._config.videoId);
        this._qvbp2p.setMediaElement(videoEl);

        // @todo 开始拉流, 注意对于一个sdk实例,loadSource不能重复调用
        const config = {
            src: dataSource.url,
        };
        this._qvbp2p.loadSource(config);
    }

    /**
     * @public
     */
    abort() {
        this._destroyQVBP2P();
    }

    /**
     * 接收sdk抛出的事件,针对不同事件类型有不同的处理
     *
     * 详细事件名称见 `QVBP2P.ComCodes`
     * @param {string} event 事件名称
     * @param {*} data
     */
    _onQVBP2PStateChange(event, data) {
        const { ComCodes } = window.QVBP2P;
        const { code } = data;
        switch (code) {
            case ComCodes.RECEIVE_BUFFER:
                this._receiveBuffer_need_to_implement(data.payload);
                break;
            case ComCodes.ROLLBACK:
                this._rollback_need_to_implement();
                break;
            default:
                break;
        }
    }

    /**
     * 接收sdk下载回来的flv chunk数据, 送给播放器
     *
     * @todo 此处需要客户根据播放器情况自行实现
     *
     * @param {ArrayBuffer} chunk flv chunk
     */
    _receiveBuffer_need_to_implement(chunk) {
        const byteStart = this._receivedLength;
        this._receivedLength += chunk.byteLength;
        if (this._onDataArrival) {
            this._onDataArrival(chunk, byteStart, this._receivedLength);
        }
    }

    /**
     * 当sdk发生错误或不能继续播放时, 会抛出此事件, 需要客户使用原来的flv流程重新播放
     *
     * @todo 此处需要客户根据播放器情况自行实现
     */
    _rollback_need_to_implement() {
        window.player.loadWithoutQVBP2P();
    }

    /**
     * 创建sdk实例
     */
    _createQVBP2P() {
        if (this._qvbp2p) {
            this._destroyQVBP2P();
        }

        // 随邮件提供 @todo
        const { pcdnMixed, partner, domain, appId, bizId } = window.p2pClientConfig;
        this._qvbp2p = new window.QVBP2P({
            // 内部调试用 start
            debug: true,
            xStreamId: this._config.xStreamId,
            // end

            pcdnMixed,
            partner,
            domain,
            appId,
            bizId,
        });
        window.qvbp2p = this._qvbp2p;
    }

    /**
     * 销毁sdk实例
     */
    _destroyQVBP2P() {
        if (this._qvbp2p) {
            this._qvbp2p.destroy();
            this._qvbp2p = null;
            window.qvbp2p = null;
        }
    }
}
window.QVBP2PLoader = QVBP2PLoader;
export default QVBP2PLoader;

```

### 3. 开发注意事项

- 需重点关注示例中 `todo`,需要您来实现
- 如果 sdk 触发回退的话, 请自行控制回退后的播放不再使用 p2p sdk
- qvbp2p 实例一次性使用， `qvbp2p.loadSource()` 和 `qvbp2p.destroy()` 不能重复调用, 如需要再次播放, 请重新创建 qvbp2p 实例
- 每次使用 qvbp2p 实例播放前, 请确保上一个`qvbp2p实例`已经调用`qvbp2p.destroy()` (如下场景需要: 切换线路,切换清晰度,回退). 
