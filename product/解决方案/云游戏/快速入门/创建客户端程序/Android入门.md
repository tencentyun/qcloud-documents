腾讯云云游戏提供  JS SDK、Android SDK 以及 iOS SDK，其中 JS SDK 可支持包括 PC 浏览器、移动端 H5 页面以及小程序内嵌 WebView 等多种落地场景，Android 及 iOS SDK 可分别支持对应设备上业务 APP 的开发。请根据您的需要参考对应客户端的创建指引。

> ? iOS SDK 目前正在内测中，如有需要请联系您的架构师或商务。

腾讯云提供了云渲染终端程序 Android 入门 Demo 供参考，本章演示如何快速配置 Demo 运行简单端游。

## 操作指引
Android 端入门 Demo 提供了基础的云试玩能力，包含简单示例、虚拟键盘和一些常见 API 的使用。您可以在入门 Demo 的基础上运行您自己的游戏，详细使用步骤如下：
1. [下载](https://github.com/tencentyun/cloudgame-android-sdk) 入门 Demo，将工程导入 Android Studio 工具。
2. 集成您自己的游戏。
   1. 将您在 [接入准备 - 步骤4](https://cloud.tencent.com/document/product/1162/65421?!editLang=zh&!preview#step4) 部署的 GAME_ID 拷贝到工程中 Constant 类的手游/端游的 GAME_ID 下（**请注意不要填错位置**）。
   <img src="https://qcloudimg.tencent-cloud.cn/raw/4916b0e037eee3b6dbdfe7fee0376173.png" width=700 />    
   2. 将您在 [创建后台程序 - 导入云函数](https://cloud.tencent.com/document/product/1162/65429?!editLang=zh&!preview) 中获取到的 SERVER 地址拷贝到工程中  CloudGameApi 类的 SERVER 下。
   <img src="https://qcloudimg.tencent-cloud.cn/raw/b6e0a88f5dc616410ddd2cd0f801f74b.png" width=700 />  
3. 编译并运行到手机上，其中前三个是端游的体验（需要您提前部署端游），最后一个是手游的体验（需要您提前部署手游）。
![](https://qcloudimg.tencent-cloud.cn/raw/821db57e335fb3993b7e8d23303836db.png)    

>! 云游戏的进阶使用请参见 [云游戏接入指南](https://github.com/tencentyun/cloudgame-android-sdk)。

