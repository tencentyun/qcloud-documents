## 操作场景
本文档将指导您如何在小程序中使用 npm 安装第三方依赖。

## 前提条件
您需要先安装 [Node.js](https://nodejs.org/en/) ，确保安装包含 npm。


## 操作步骤
在云函数中我们可以引入第三方依赖来帮助我们更快的开发。云开发提供了云端安装依赖，免去了在终端手动安装依赖的工作。但如果在您的环境中无法直接使用 `npm install`，比如需要走代理、使用自建的 `npm` 源站、本地调试云函数、使用其他包管理器如 `yarn` 等的情况，则不能使用工具的自动安装依赖，需手工执行相应依赖安装命令。

云函数的运行环境是 Node.js，因此我们可以使用 npm 安装第三方依赖。您只能对每个云函数分别安装依赖。具体操作如下：
1. 打开微信开发者工具，在云函数的根目录下，单击右键需要安装依赖的云函数，单击 【在终端中打开】。 
![](https://main.qcloudimg.com/raw/fd5aad2eec439e3b4f78daa42a147862.png)
2. 在弹出的 cmd 窗口中输入指令，安装所需依赖。
 1. 安装  [wx-server-sdk](https://developers.weixin.qq.com/miniprogram/dev/wxcloud/reference-server-api/) 依赖或 [tcb-admin-node](https://github.com/TencentCloudBase/tcb-admin-node) 依赖。
 `wx-server-sdk` 是基于 `tcb-admin-node`开发的服务端 `SDK`，与小程序端的接口使用方式一致，能获得更一体的开发体验。但如果想获得更高级的功能，可使用 `tcb-admin-node`。示例代码如下：
```text
npm install --save wx-server-sdk
```
```
npm install --save tcb-admin-node
``` 
  2. 除了使用 Node.js 提供的原生 HTTP 接口在云函数中发起网络请求，我们还可以使用常用的网络请求库  [request](https://github.com/request/request) 来更便捷的发起网络请求。要为云函数安装 request 模块，您需要进入您的云函数目录，运行以下代码：
```javascript
npm install request
```
在为运行环境为 Node.js 的云函数安装依赖时，如果是扩展型的 npm 包，要选择运行环境对应的 Node.js 版本并在 Linux 环境下安装。
  
  >!
  - 在 `wx-server-sdk` 依赖中不再兼容 `success`、`fail`、`complete` 回调，总是只会返回 `Promise`。
  - 如果在执行安装命令后出现类似错误提示：`rollbackFailedOptional: verb npm-session ****************`，这是由于`npm`官方库是国外的网站，在访问时可能由于网络原因导致异常。





