
腾讯云 X-P2P 直播解决方案，可帮助用户直接使用经过大规模验证的直播流媒体分发服务。用户可通过 SDK 中简洁的接口快速同自有应用集成，实现 Web 端  P2P 的 H5 直播播放功能。

## 运行条件

### 支持的浏览器

- **SDK 运行浏览器需支持特性**：`Media Source Extention`、`WEB RTC`、`websocket`。
- **SDK 支持以下版本浏览器**：
<table>
<tr><th>浏览器类型</th><th>版本要求</th>
</tr><tr>
<td>chrome</td><td align="center">55+</td>
</tr><tr>
<td>firefox</td><td align="center">50+</td>
</tr><tr>
<td>safari</td><td align="center">11+</td>
</tr><tr>
<td>edge</td><td align="center">16+</td>
</tr><tr>
<td>IE</td><td align="center">不支持</td>
</tr></table>



### 支持的流媒体格式
- RTMP
- HTTP-FLV

## 名词解释
回退/rollback：指当 P2P SDK 不能正常工作后， SDK 会抛出 ROLLBACK 事件，此时您需要考虑使用原有的直播拉流。


## 注意事项
- 如果 SDK 触发回退的话，请自行控制回退后的播放不再使用 P2P SDK。
- 对于一个 QVBP2P 实例，`qvbp2p.loadSource()` 和 `qvbp2p.destroy()` 不能重复调用，如需要再次播放，请重新创建 QVBP2P 实例。
- 每次使用 QVBP2P 实例播放前，请确保上一个 `qvbp2p 实例` 已经调用 `qvbp2p.destroy()` 销毁 SDK。
  > ? 具体使用场景为：切换线路、切换清晰度、回退。


## Demo 示例

-  集成 SDK 到播放器（flv.js）编写 loader 示例代码，请参见 [此处](https://devcenter.qvb.qcloud.com/demo/h5/QVBP2PLoader.html)。
-  集成 SDK 到播放器（flv.js）的 Demo，请参见 [此处](https://devcenter.qvb.qcloud.com/demo/h5/pcdn/v1/p2pdemo.html)。

## 准备工作
在 [提交 X-P2P 开通申请](https://cloud.tencent.com/apply/p/npwwbfakdis) 后，再联系我们的研发工程师，确保 CDN 分发域名及 domain 白名单已完成配置。

## 集成步骤

1. 在 Web 端 H5 播放页加载腾讯云 X-P2P 的 SDK，载方式示例如下（假设 SDK 名称为：`qvbp2p.js`）：
``` javascript
   <script src='qvbp2p.js'></script>
```
2. 根据 SDK 提供的接口调用腾讯云 X-P2P 服务。
SDK 提供的 `window.QVBP2P` 接口是 SDK 的入口类，支持访问一些常量和生成 QVBP2P 实例。QVBP2P 函数详情如下：
<table>
<tr><th>QVBP2P 函数</th><th>说明</th></tr><tr>
<td>QVBP2P.ComEvents</td>
<td>外部可以注册监听的事件，当事件被触发的时候会调用绑定的回调</td>
</tr><tr>
<td>QVBP2P.ComCodes</td>
<td>区分回调事件的状态码</td>
</tr><tr>
<td>QVBP2P.isSupported()</td>
<td>静态方法，判断当前浏览器是否支持 SDK</td>
</tr><tr>
<td>QVBP2P.listen(comEvent, callback)</td>
<td>向 SDK 注册监听的事件</td>
</tr><tr>
<td>QVBP2P.loadSource(config)</td>
<td>开始拉流（不能重复调用）</td>
</tr><tr>
<td>QVBP2P.destroy()</td>
<td>中断拉流，销毁 SDK（不能重复调用）</td>
</tr></table>
3. 编写一个集成到播放器的模拟 loader，将 SDK 集成到播放器。示例代码如下：

```JavaScript
/**
 * 我们通过这个模拟的loader简要介绍了sdk和player的接入方法
 */
class QVBP2PLoader {
  constructor(config) {
    this.config = config;
    
    // 初始化 qvbp2p
    this._initQVBP2P();
 
  }

  destroy() {
    // 关闭sdk, 释放资源
    this._destroyQVBP2P();
  }

  /**
   * 在使用本loader前需要先判断浏览器是否支持sdk
   * QVBP2PLoader.isSupported();
   * @returns {boolean}
   */
  static isSupported() {
    return window.QVBP2P.isSupported();
  }

  /**
   * 创建qvbp2p实例, 并初始化
   * @private
   */
  _initQVBP2P() {
    if (!window.qvbp2p) {
      /**
       * 创建qvbp2p实例
       *
       * 如果需要调试, 可传入参数开启debug log:
       * window.qvbp2p = new window.QVBP2P({debug: true});
       */
      window.qvbp2p = new window.QVBP2P({
            accessKey: '随邮件提供',
            enableHttps: '默认为true, 如播放域名没有配置https,填false',
            liveDomain: '随邮件提供',
            dispatchDomain: '随邮件提供'
      });

      // 绑定事件监听 
      this._bindListener();
    }
  }

  /**
   * 向qvbp2p注册回调
   * @private
   */
  _bindListener() {
    let ql = window.qvbp2p,
      QL = window.QVBP2P;
    if (ql && QL) {
      ql.listen(QL.ComEvents.STATE_CHANGE, this.onStateChange.bind(this));
    }
  }

  /**
   * 销毁qvbp2p实例, 释放资源
   * @private
   */
  _destroyQVBP2P() {
    // 只能调用一次qvbp2p.destroy(), 不可重复调用 
    if (window.qvbp2p) {
      window.qvbp2p.destroy();
      window.qvbp2p = null;
    }
  }

  /**
   * loader工作入口, 由此开始load视频
   * @param src 直播url
   */
  load(src) {
    // 每次load都销毁前一个qvbp2p实例使用新的实例
    if (window.qvbp2p) {
      this._destroyQVBP2P();
    }

    // 创建新的qvbp2p实例
    if (!window.qvbp2p) {
      this._initQVBP2P();
    }

    // 使用sdk加载资源
    let config = {
      videoId: this.config.videoElementId, // video标签的id, 必填
      src: src // 视频地址, 必填
    };
    // 加载资源, 开始播放.
    // 请注意qvbp2p.loadSrouce()不能重复调用
    window.qvbp2p.loadSource(config);
  }



  /**
   * STATE_CHANGE事件触发后的回调
   * @param event 事件名字
   * @param data 传回的数据
   */
  onStateChange(event, data) {
    let CODE = window.QVBP2P.ComCodes;
    let code = data.code;
    switch (code) {
      case CODE.RECEIVE_BUFFER:
        // 接收视频数据
        this._receiveBuffer(data.payload);
        break;
      case CODE.ROLLBACK:
        this._rollback();
        break;
      default:
        break;
    }
  }

  /**
   * 接收flv视频数据分片, 可送入播放器处理
   * @param chunk ArrayBuffer
   * @private
   */
  _receiveBuffer(chunk) {
    // TODO process chunk data
  }

  /**
   * 当sdk不能继续播放的时候, 会抛出事件调用这个方法
   * @private
   */
  _rollback() {
    // TODO
    this._destroyQVBP2P();
  }
}

export default QVBP2PLoader;

```
