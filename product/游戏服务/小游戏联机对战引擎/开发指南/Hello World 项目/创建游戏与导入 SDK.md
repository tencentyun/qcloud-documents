## 操作场景
本文档主要介绍如何创建一个 Hello World 的小游戏项目和如何导入 SDK 的操作说明。


## 前提条件
- 已在小游戏联机对战引擎控制台创建小游戏实例，并开通联机对战服务。
- 已获取游戏 gameID 和 secretKey。SDK 需要对这两个参数进行校验。


## 操作步骤
### 创建一个微信小游戏项目
1. 打开微信开发者工具，创建一个名为 HelloWorld 的小游戏项目。
>!注意不要选择快速启动模板，直接创建空项目，从零开始完成项目。详细操作请参考 [小游戏开发文档](https://developers.weixin.qq.com/minigame/dev/index.html) 。

 ![创建一个微信小游戏项目](https://main.qcloudimg.com/raw/97cd731bfad0493f14984866cd6bc712.png)

2. 进入编辑界面后，在根目录创建 game.js 和 game.json 文件，如下图所示：
 >!在开发过程中可以先跳过微信的域名检查。微信开发者工具上可以通过右侧【详情】设置，手机预览小程序/小游戏时可以打开调试功能跳过检查。
 
 ![game.json 文件](https://main.qcloudimg.com/raw/c0046c611acf7eaf939bd6418d56b891.png)
3. 在新创建的 game.json 文件中，添加如下代码：
```
{
  "deviceOrientation": "portrait"
}
```





### 导入 MGOBE SDK
1. 将 MGOBE.js 添加到项目根目录。
2. 在 game.js 中添加如下代码，完成导入 MGOBE SDK。
```
// 导入 MGOBE.js
import "./MGOBE.js";
// 获取 Room、Listener 对象
const { Room, Listener, ErrCode, ENUM } = MGOBE;
```


