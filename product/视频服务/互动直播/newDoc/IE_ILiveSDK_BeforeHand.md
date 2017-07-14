# 下载代码

## 简介
互动直播SDK for IE，下文称为ILiveSDK(IE)，是互动直播在IE平台上的SDK。通过ActiveX实现了在IE上进行互动直播、上麦和基础IM的能力。

## 支持的浏览器
32位IE9，32位IE10，IE11

## 下载SDK和DEMO
demo工程是基于ILiveSDK(IE)开发的互动直播应用。应用名为随心播，可以与其他终端的随心播互通。   
您可以直接在这里[在线体验](https://sxb.qcloud.com/webdemo/index.html)其效果。   
也可以在[github](https://github.com/zhaoyang21cn/ILiveSDK_Web_Demos)下载ILiveSDK(IE)及其demo。其中包含了ILiveSDK(IE)，接口文档，js接口文件和接口调用示例等，具体如下：
  

文件 | 说明 | 
----|------|
/suixinbo | demo随心播工程，可以用IE打开index.html  | 
iLiveSDK/iLiveSDK.cab | 互动直播组件，业务层不会直接与此文件交互  | 
iLiveSDK/iLiveSDK.js | 互动直播接口，封装了iLiveSDK.cab的接口供业务层调用  | 
/doc | 相关文档  | 
/tools | 开发者工具 | 


## demo运行及其注意事项
运行demo可以对ILiveSDK(IE)具备的能力有个直观的印象。您可以参照如下步骤运行demo：

 1. 把随心播代码中的appid和accountType修改成开发者自己的。即在demo.js中找到OnInit方法，找到`sdk = new ILiveSDK(1400027849, 11656, "iLiveSDKCom")`语句，用自己的`SDKAppID`和`accountType`替换前两个参数。如何获取这两个参数，可以参考[快速参数配置](https://www.qcloud.com/document/product/268/7599)。
 2. 将[随心播后台代码](https://github.com/zhaoyang21cn/SuiXinBoPHPServer)部署到自己服务器上，并按照文档修改后台的秘钥。
 2. 用IE打开index.html，并允许activeX控件，可以看到注册和登录界面。
 ![登录界面](http://mc.qcloudimg.com/static/img/cf9dec67f37159dc9fec9d529dcf47f1/image.png)
 3. 登录成功后可以看到当前正在直播的房间列表（房间是ILiveSDK的概念，后文详述）。您也可以自己创建一个直播。![房间列表界面](http://mc.qcloudimg.com/static/img/82fcdb2dfad54efd80d3c9ed4b5c5d8a/image.png)
 4. 进入一个房间，可以看到直播的视频、群消息，当前房间成员等。您可以打开摄像头进行直播，给其他房间成员发消息等。![房间](http://mc.qcloudimg.com/static/img/43f1047c1d00f70de63b9a287ff55973/image.png)

## 将iLiveSDK(IE)集成入自己的工程
集成ILiveSDK(IE)仅需使用javastript。将SDK引入工程的步骤如下：

 1. 将cab文件和iLiveSDK.js放入电脑任意位置
 2. 在html页面中添加`
<object id="iLiveSDK" classid="CLSID:54E71417-216D-47A2-9224-C991A099C531" codebase="路径/iLiveSDK.cab#version=版本号"></object>`
 3. 在html页面中添加js接口文件<script type="text/javascript" src="路径/iLiveSDK.js"></script>
 4. 调用iLiveSDK中的接口实现业务需求

## SDK日志位置
日志地址：%appdata%\Tencent\iLiveSDK（在开始菜单运行中执行）
