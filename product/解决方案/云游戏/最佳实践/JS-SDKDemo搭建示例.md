云游戏提供了相关 Web 端搭建 Demo，详情请参见 [demo.zip](https://ex.cloud-gaming.myqcloud.com/lib/demo/demo.zip)。

[](id:web)

## Web 端搭建示例（H5）
1.  引入云游戏的 js 文件。
```
<script type="text/javascript" src="https://ex.cloud-gaming.myqcloud.com/cloud_gaming_web_sdk/tcg-sdk/latest/index.js"></script>
```
2.  在页面内定义一个云游戏显示用的锚点，如下所示。
```
<div id="mount-point"></div>
```
3.  页面内按顺序调用 init、start 接口，接口文档见 [前端 JS SDK API 文档](https://cloud.tencent.com/document/product/1162/46134)。
4.  修改 `demo.html` 的 `tryLock` 和 `createSession` 请求 URL，指向自行部署好的 [业务后台服务](https://cloud.tencent.com/document/product/1162/47523)。
5.  刷新页面并等待浏览器连接成功。

