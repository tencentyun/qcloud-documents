## Web 端搭建示例（H5）
1.  引入云游戏的 js 文件。
<dx-codeblock>
::: html html
<script type="text/javascript" src="https://cloud-gaming.myqcloud.com/cloud_gaming_static/tcgsdk.js"></script>
:::
</dx-codeblock>
2.  在页面内定义一个云游戏显示用的锚点，如下所示：
<dx-codeblock>
::: html html
<div id="mount-point"></div>
:::
</dx-codeblock>
3.  页面内按顺序调用 init，start 接口，接口文档见 [前端 JS SDK API 文档](https://cloud.tencent.com/document/product/1162/46134)。
4.  修改 `demo.html` 的 `get_signature` 请求 url，指向自行部署好的 [业务后台服务](https://cloud.tencent.com/document/product/1162/47523)。
5.  刷新页面并等待浏览器连接成功。


## Android 端搭建示例
1. 拷贝 `tcgsdk-release.aar` 到 App 项目的 libs 目录下。
2. 修改 `build.gradle`，增加 `'*.aar'`：
<dx-codeblock>
::: java java
   implementation fileTree(dir: 'libs', include: ['*.jar', '*.aar'])
:::
</dx-codeblock>
3. 编写代码，如下：
<dx-codeblock>
::: java java
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
:::
</dx-codeblock>

