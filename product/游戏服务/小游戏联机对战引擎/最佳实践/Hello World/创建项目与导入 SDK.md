
## 操作场景
本文档主要介绍如何创建一个 Hello World 的小游戏项目和如何导入 SDK 的操作步骤。


## 前提条件
- 已在游戏联机对战引擎控制台创建游戏，并开通联机对战服务，详情可参考 [开通服务](https://cloud.tencent.com/document/product/1038/33299)。
- 已获取游戏 gameID 和 secretKey，您可在游戏概览的基本信息里查看。SDK 需要对这两个参数进行校验。


## 操作步骤
### 创建一个微信小游戏项目
1. 打开微信开发者工具，创建一个名为 HelloWorld 的小游戏项目。
![创建一个微信小游戏项目](https://main.qcloudimg.com/raw/13b462d7fc7eabbfabd5816265ffca0a.png)
2. 进入编辑界面后，删除多余的文件，只保留 game.js、game.json、project.config.json 三个文件，并清空 game.js 文件内容，如下图所示：

<dx-alert infotype="notice" title="">
在开发过程中可以先跳过微信的域名检查。微信开发者工具上通过右侧**详情**设置，手机预览小程序/小游戏时打开调试功能跳过检查。
</dx-alert>

 ![清空game](https://main.qcloudimg.com/raw/76539f74648393dd234dd39755e9b4e8.png)



### 导入 MGOBE SDK
1. 将 MGOBE.js 添加到项目根目录。
2. 在 game.js 中添加如下代码，完成导入 MGOBE SDK。
```http
// 导入 MGOBE.js
import "./MGOBE.js";
// 获取 Room、Listener 对象
const { Room, Listener, ErrCode, ENUM } = MGOBE;
```
