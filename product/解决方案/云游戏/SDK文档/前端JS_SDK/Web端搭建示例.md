云游戏提供了相关 Web 端搭建 Demo，详情请参见 [demo](https://github.com/tencentyun/cloudgame-js-sdk/tree/master/demo)。

[](id:web)
## Web 端搭建示例（H5）

1. 引入云游戏的 js 文件（ts 声明文件已放在相同目录下）。
```
<script type="text/javascript" src="./tcg-sdk/index.js"></script>
```
2. 在页面内定义一个云游戏显示用的锚点，如下所示。
```
<div id="mount-point"></div>
```
3. 页面内按顺序调用 init、start 接口，接口说明请参见 [JS SDK 接口](https://cloud.tencent.com/document/product/1162/46134)。
4. 修改 `demo.html` 的 `tryLock` 和 `createSession` 请求 URL，指向自行部署好的 [业务后台服务](https://cloud.tencent.com/document/product/1162/47523)。
5. 刷新页面并等待浏览器连接成功。

