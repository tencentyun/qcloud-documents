## SDK 概览

### 生命周期相关接口

| 接口名称                           | 接口描述                |
| ------------------------------------------------------------ | -------------------------------------- |
| [TcgSdk.TcgSdk(params)](#tcgsdk.tcgsdk(params)) | 云游戏前端初始化            |
| [TCGWebView.loadUrl(url)](#tcgwebview.loadurl(url)) | 安卓加载云游页面            |
| [TcgSdk.getLocalDescription()](#tcgsdk.getlocaldescription()) | 获取本地 session，用于请求云游戏服务端 |
| [TcgSdk.start(session)](#tcgsdk.start(session)) | 启动云游戏               |
| [TcgSdk.destroy(msg)](#tcgsdk.destroy()) | 立即停止云游戏             |

### 安卓前端实现接口

| 接口名称                           | 接口描述                        |
| ------------------------------------------------------------ | ------------------------------------------------------- |
| [TcgSdk.addEventObserver(EventObserver)](#tcgsdk.addeventobserver(eventobserver)) | 添加事件监听                      |
| [TcgSdk.getTcgSdk()](#tcgsdk.gettcgsdk()) | 获取 webview 内置的 TCGSDK 对象，用于 native 层调用接口 |
| [TCGWebView.tcgWebView(container, outsideCallback, nativeGamepad)](#tcgwebview.tcgwebview(container.2C-outsidecallback.2C-nativegamepad)) | 云游戏安卓容器初始化                  |
| [RenderWebView.renderWebView(ctx)](#renderwebview.renderwebview(ctx)) | 云游戏 webview 初始化                  |
| [TCGWebView.setWebView(view)](#tcgwebview.setwebview(view)) | 设置网页渲染的 webview                 |
| [TCGWebView.getWebView()](#tcgwebview.getwebview()) | 获取网页渲染的 webview                 |
| [TCGWebView.eval(String jsStr)](#tcgwebview.eval(string-jsstr)) | 安卓 native 层执行 js 代码的接口            |
| [TcgSdk.EventObserver](#tcgsdk.eventobserver)        | 接口用于监听前端事件                  |


## 云游戏生命周期相关接口

### TcgSdk.TcgSdk(params)

云游戏前端初始化。具体调用方式与 JS SDK 相同，请参见[TCGSDK.init(params)](https://cloud.tencent.com/document/product/1162/46134#tcgsdk.init(params)) 函数。

### TCGWebView.loadUrl(url)

安卓加载云游页面。

| 参数 | 参数类型 | 说明    |
| ---- | -------- | ---------- |
| url | string  | 启动云游戏 |


### TcgSdk.getLocalDescription()

获取本地 session，用于请求云游戏服务端。

### TcgSdk.start(session)

请求云 API 返回的 serverSession 后调用该接口启动云游戏。
  

### TcgSdk.destroy()

断开云游戏连接。


## 云游戏安卓前端实现接口

### TcgSdk.addEventObserver(EventObserver)

添加事件监听。

### TcgSdk.getTcgSdk()

获取 webview 内置的 TcgSdk 对象，用于 native 层调用接口。


### TCGWebView.tcgWebView(container, outsideCallback, nativeGamepad)

云游戏安卓容器初始化。

| 参数      | 参数类型         | 说明                             |
| --------------- | ------------------------- | ------------------------------------------------------------ |
| container    | Activity 类        | view 的容器                         |
| outsideCallback | [TcgSdk.EventObserver](#tcgsdk.eventobserver) 接口 | 如果 native 层需要事件回调，可以设置这个回调接口，不需要则设为 null |
| nativeGamepad  | boolean          | 设置手柄事件，true 使用原生的手柄事件，false 使用网页的手柄事件 |


### RenderWebView.renderWebView(ctx)

云游戏 webview 初始化。

| 参数 | 参数类型 | 说明   |
| ---- | -------- | --------- |
| ctx | Context | UI 上下文 |


### TCGWebView.setWebView(view)

设置网页渲染的 webview。

| 参数 | 参数类型     | 说明                             |
| ---- | ---------------- | ------------------------------------------------------------ |
| view | RenderWebView 类 | 基类必须为 RenderWebView，用户有特殊需求需要外部创建 webview 的情况可以自行派生 RenderWebView |


### TCGWebView.getWebView()

获取网页渲染的 webview。


### TCGWebView.eval(String jsStr)

安卓 native 层执行 js 代码的接口。

| 参数 | 参数类型 | 说明        |
| ----- | -------- | ------------------ |
| jsStr | String  | 需要执行的 js 代码 |



### TcgSdk.EventObserver

EventObserver 接口用于监听前端事件。待实现的回调函数如下：

| 函数原型                  | 必选 | 描述                  |
| ------------------------------------------ | ---- | -------------------------------------- |
| void onNetworkChanged(JSONObject json)   | 是  | 网络状态改变              |
| void onConnectSuccess(JSONObject json)   | 是  | 云游连接成功              |
| void onConnectFailed(JSONObject json)   | 是  | 云游连接失败              |
| void onDisconnected(JSONObject json)    | 是  | SDK 断开销毁              |
| void onWebrtcStat(JSONObject json)     | 是  | serverSession 设置是否成功       |
| void onInitSuccess(JSONObject json)    | 是  | SDK 初始化成功             |
| void onInputStatusChanged(JSONObject json) | 是  | 输入状态改变，例如点击到输入框     |
| void onTouchEvent(JSONObject json)     | 是  | 触摸事件回调              |
| void onResolutionChanged(JSONObject json) | 是  | 分辨率变更，连接成功后会触发一次    |
| void onDisplayRectChanged(JSONObject json) | 是  | 本地显示区域变更，连接成功后会触发一次 |
