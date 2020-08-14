## Web 端 Demo 搭建示例（H5）
1.  引入云游戏的 js 文件。
```html
<script type="text/javascript" src="https://cloud-gaming.myqcloud.com/cloud_gaming_static/tcgsdk.js"></script>
```
2.  在页面内定义一个云游戏显示用的锚点，如：
```html
<div id="mount-point"></div>
```
3.  页面内按顺序调用 init，start 接口，接口文档见 [前端 JS SDK API文档](#)。
4.  修改 `demo.html的get_signature` 请求 url，指向自行部署好的业务后台服务（跳转到### 云游戏demo后端与云 API 对接示例（nodejs）。
5.  刷新页面并等待浏览器连接成功。


## Android 端 Demo 搭建示例
### 混合（JS + 原生 SDK）调用示例

> ? 推荐方式，原生代码更少，更容易热更新实现兼容不同游戏的 UI，并且接口与 JS SDK 保持一致）。

```java
    private TCGWebView _webview;
    ...
    // YourActivity.onCreate {
        _webview = new TCGWebView(this, null, false);// 第二个参数如果native层不需要监听事件就不用设置
        _webview.loadUrl("your html url");// js api对齐js sdk的api，可以参照js sdk的调用示例
        // js sdk、示例和文档下载：https://material-1258550678.cos.ap-guangzhou.myqcloud.com/download/tcgsdk-latest.tar.gz
    // }
```

### 纯原生调用示例
1. 拷贝 `tcgsdk-release.aar` 到 App 项目的 libs 目录下。
2. 修改 `build.gradle`，增加 `'*.aar'`：
```java
   implementation fileTree(dir: 'libs', include: ['*.jar', '*.aar'])
```
3. 编写代码，如下：
```java
    private TcgSdk tcgSdk;
    ...
    // YourActivity.onCreate {
    tcgSdk = new TcgSdk(this, false, true, true, new TcgSdk.EventObserver() {
         @Override
         public void onNetworkChanged(JSONObject json) {
            // TODO
         }

         @Override
         public void onConnectSuccess(JSONObject json) {
            // TODO
         }

         @Override
         public void onConnectFailed(JSONObject json) {
            // TODO
         }

         @Override
         public void onDisconnected(JSONObject json) {
            // TODO
         }

         @Override
         public void onWebrtcStat(JSONObject json) {
            // TODO
         }

         @Override
         public void onInitSuccess(JSONObject json) {
            // TODO
         }

         @Override
         public void onInputStatusChanged(JSONObject json) {
            // TODO
         }

         @Override
         public void onTouchEvent(JSONObject json) {
            // TODO
         }
    });
    // 获取本地session
    String clientSession = tcgsdk.getLocalDescription();
    // 通过请求后端返回serverSession，
    String serverSession = doSomeHttpRequest(clientSession);
    // 开始连接，tcgsdk不关心serverSession怎么拿到的，有这个值，传给start接口就可以开启云游戏
    tcgsdk.start(serverSession);
    // 设置鼠标图片和显示大小, R.drawable.cursor是安卓工程的图片资源id
    tcgSdk.setCursorImage(R.drawable.cursor, 30, 30);
    // }
```

## 云游戏 Demo 后端与云 API 对接示例（Node.js）
1. [cloudapi.js](https://material-1258550678.cos.ap-guangzhou.myqcloud.com/download/cloudapi.js) 是 Node.js 版的云 API 调用实例，自行安装 Node.js 运行环境，替换 cloudapi.js 里面的 SecretId 和 SecretKey，使用您的腾讯云帐号的 [云API](https://console.cloud.tencent.com/cam/capi) 对应的密钥。
2. 使用 express-cli 初始化一个 express 项目。
```
    express myproj
    npm i
```
3. 安装依赖库。
```
    npm install --save express tencentcloud
```
4. `cloudpai.js` 拷贝到项目目录下，修改 `app.js`，在后面加入一行。
```
    app.use('/cloudapi', require('./cloudapi.js'));
```
5. 运行服务。
```
    npm run
```
6. 网页端发送 JSON 格式的 POST 请求 `http://127.0.0.1:3000/cloudapi/get_signature` 接口，返回值里获取 ServerSession 字段，调用 TCGSDK.start(ServerSession) 接口启动云游戏。

