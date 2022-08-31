## JS SDK 相关问题
### 浏览器控制台报 setServerDescription 失败?
通常是 CreateSession 请求获取 ServerSession 的结构层次不对，把返回结果打印下就可以知道如何获取。 

### 打开数据通道为什么返回失败（code≠0）？
需要收到 SDK 回调的 onConnectSuccess 再创建数据通道。

### 移动端如何实现自动横竖屏？
因为云端推流是固定横屏，移动端要竖屏展示需要旋转操作。可传 init 参数，autoRotateContainer（旋转容器），autoRotateMountPoint（旋转挂载节点）。

### 微信上自动播放为什么受限？
微信 WebView 限制，需要有 User Action 才会播放，也可以监听 WeixinJSBridgeReady 回调后 init SDK。

### 鼠标模式有哪些？
目前有 3 种模式。
- 鼠标模式 0 无鼠标下发
- 鼠标模式 1 下发鼠标由 SDK 进行鼠标绘制
- 鼠标模式 2 为云端绘制鼠标延迟比 1 大

建议优先用鼠标模式 0 或 1。默认鼠标模式 0，具体实现请参见 [JS SDK 接口说明](https://cloud.tencent.com/document/product/1547/72694)。

## SDK Plugin 相关问题
### 摇杆按钮点击方向为什么不对？
建议创建摇杆在 connectSuccess 之后再操作。
