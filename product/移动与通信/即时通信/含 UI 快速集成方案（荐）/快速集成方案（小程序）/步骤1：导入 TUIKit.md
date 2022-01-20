## 什么是小程序 TUIKit？

小程序 TUIKit 是基于 IM SDK 实现的一套 UI 组件，其包含会话、聊天、群组管理等功能，基于 UI 组件您可以快速的搭建属于自己的业务逻辑。
目前我们推出了在线客服场景并提供了示例客服群、示例好友的基础模板，在线客服场景包括：
- 支持发送文本消息、图片消息、语音消息、视频消息等常见消息。
- 支持常用语、订单、服务评价等自定义消息。
- 支持创建群聊会话、群成员管理等。

## 效果展示 
  <img src="https://sdk-web-1252463788.cos.ap-hongkong.myqcloud.com/component/TUIKit/assets/tuikit-github-1.gif"  height = "400" width = "200">

## 如何集成 TUIKit ？

### 步骤1： 下载源码

TUIKit 支持以原生 js 的方式集成。可从 Github 下载 TUIKit 源码。命令行执行：

<dx-codeblock>
:::  js
 git clone https://github.com/tencentyun/TIMSDK.git
:::
</dx-codeblock>

### 步骤2： 初始化 TUIKit

<dx-codeblock>
  :::  js
  cd TIMSDK/MiniProgram/TUIKit
  :::
</dx-codeblock>

找到并打开 `TUIKit/miniprogram/debug/GenerateTestUserSig.js` 文件，并填写 SDKAppID 以及 SECRETKEY (默认为空字符串，请设置为实际的密钥信息。)
![](https://qcloudimg.tencent-cloud.cn/raw/3f7f6fe1e88e4f01fc0bb3d44b2c8735.png)

### 步骤3： 集成静态资源文件

在自己的项目中集成静态资源文件（工具、图片等）。
  <img src="https://qcloudimg.tencent-cloud.cn/raw/35be6307ecd28c97c11d1a3a7f2c0d26.png"   width = "200">


### 步骤4： 集成所需模块

由于微信对于小程序的主包体积要求不得超过2M，所以 TUIKit 推出分包的解决方案，为客户解决体积超出这一问题。


<dx-tabs>
::: 集成整个分包
1. 客户自己设置主包的内容并放置在 page 文件夹内，建议主包尽可能的只放首页，减少首屏渲染时间以及主包的体积大小。
2. 将分包引入，并和主包置于同一层级。分包内部独立并包含整个模块的逻辑。
  <img src="https://qcloudimg.tencent-cloud.cn/raw/bbefd3eaa58838c9dcb05d29060ba229.png"   width = "200">

 - 在 app.json 中配置分包路径。主包路径为原来的 page 路径不变。
  <dx-codeblock>
  :::  js
   "subPackages":[
    {
      "root":"TUI-CustomerService",
      "name": "TUI-CustomerService",
      "pages": [
         "pages/TUI-Conversation/conversation/conversation",
         "pages/TUI-Chat/chat",
         "pages/TUI-Conversation/create-conversation/create",
         "pages/TUI-Group/create-group/create",
         "pages/TUI-Group/join-group/join",
         "pages/TUI-Group/memberprofile-group/memberprofile"
      ],
      "independent": false
    }
  ],
  :::
</dx-codeblock>

 - 是否启用预加载（启用后，在进入主包后就会预加载分包内的资源，否则，进入分包后才会加载分包内的资源）。
    <dx-codeblock>
  :::  js
   "preloadRule": {
    "pages/TUI-Index/index" :{  
      "network": "all",
      "packages": [
        "TUI-CustomerService"
      ]
    }
  },
  :::
</dx-codeblock>
:::
::: 只集成目标模块
1. 客户自己设置主包的内容并放置在 page 文件夹内，建议主包尽可能的只放首页，减少首屏渲染时间以及主包的体积大小。
2. 将引入的模块设置为分包，并和主包置于同一层级。分包内部独立并包含整个模块的逻辑。

  - 引入模块所需静态资源

  <img src=" https://qcloudimg.tencent-cloud.cn/raw/0b750acf1e04d282e35055fa9125a29f.png"   width = "200">

  - 引入自己所需的模块

  <img src="https://qcloudimg.tencent-cloud.cn/raw/97c8a36611d8bb230099f4d94f6f999e.png"   width = "200">

 - 在 app.json 中配置分包路径。主包路径为原来的 page 路径不变。
    <dx-codeblock>
  :::  js
   "subPackages":[
    {
      "root":"TUI-CustomerService",
      "name": "TUI-CustomerService",
      "pages": [
         "pages/TUI-Conversation/conversation/conversation",
         "pages/TUI-Chat/chat",
         "pages/TUI-Conversation/create-conversation/create"
      ],
      "independent": false
    }
  ],
  :::
</dx-codeblock>

 - 是否启用预加载（启用后，在进入主包后就会预加载分包内的资源，否则，进入分包后才会加载分包内的资源）。
    <dx-codeblock>
  :::  js
   "preloadRule": {
    "pages/TUI-Index/index" :{  
      "network": "all",
      "packages": [
        "TUI-CustomerService"
      ]
    }
  },
  :::
</dx-codeblock>
:::
</dx-tabs>

 

### 常见问题

**1. 小程序如果需要上线或者部署正式环境怎么办？**
请在**微信公众平台**>**开发**>**开发设置**>**服务器域名**中进行域名配置：

将以下域名添加到 **request 合法域名**：

从v2.11.2起 SDK 支持了 WebSocket，WebSocket 版本须添加以下域名：

| 域名 | 说明 |  是否必须 |
|:-------:|---------|----|
|`wss://wss.im.qcloud.com`| Web IM 业务域名 | 必须|
|`wss://wss.tim.qq.com`| Web IM 业务域名 | 必须|
|`https://web.sdk.qcloud.com`| Web IM 业务域名 | 必须|
|`https://webim.tim.qq.com` | Web IM 业务域名 | 必须|

v2.10.2及以下版本使用 HTTP，HTTP 版本须添加以下域名：

| 域名 | 说明 |  是否必须 |
|:-------:|---------|----|
|`https://webim.tim.qq.com` | Web IM 业务域名 | 必须|
|`https://yun.tim.qq.com` | Web IM 业务域名 | 必须|
|`https://events.tim.qq.com` | Web IM 业务域名 | 必须|
|`https://grouptalk.c2c.qq.com`| Web IM 业务域名 | 必须|
|`https://pingtas.qq.com` | Web IM 统计域名 | 必须|

将以下域名添加到 **uploadFile 合法域名**：

| 域名 | 说明 |  是否必须 |
|:-------:|---------|----|
|`https://cos.ap-shanghai.myqcloud.com` | 文件上传域名 | 必须|

将以下域名添加到 **downloadFile 合法域名**：

| 域名 | 说明 |  是否必须 |
|:-------:|---------|----|
|`https://cos.ap-shanghai.myqcloud.com` | 文件下载域名 | 必须|

### 文档：
- [SDK API 手册](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html)
- [SDK 更新日志](https://cloud.tencent.com/document/product/269/38492)
