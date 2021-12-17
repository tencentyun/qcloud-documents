腾讯云提供了云渲染终端程序 Android 入门  Demo  供参考，本章演示如何快速配置  Demo  运行简单端游。

入门 Demo 提供了基础的云试玩能力，包含简单示例、虚拟键盘和一些常见 API 的使用，您可以在入门 Demo 的基础上运行您自己的游戏，详细使用步骤如下：

## 步骤1：下载 Demo[](id:step1)
单击 [下载](https://github.com/tencentyun/cloudgame-android-sdk) Android  端入门 Demo 工程，将工程导入 AndroidStudio 工具。

## 步骤2：集成游戏[](id:step2)
1. 完成 [接入准备 - 步骤4](https://cloud.tencent.com/document/product/1162/65421#step4) 的部署后,会在**云游戏控制台** > **游戏管理**中生成对应的 GAME_ID。您需将 GAME_ID 拷贝到工程中 Constant 类的手游或者端游的 GAME_ID下（**请注意不要填错位置**）。
![img](https://qcloudimg.tencent-cloud.cn/raw/4916b0e037eee3b6dbdfe7fee0376173.png)
2. 将您在 [创建后台程序 - 导入云函数](https://cloud.tencent.com/document/product/1162/65429#upload) 中获取到的 SERVER 地址拷贝到工程中 CloudGameApi 类的 SERVER 下。
![img](https://qcloudimg.tencent-cloud.cn/raw/b6e0a88f5dc616410ddd2cd0f801f74b.png)
3. 编译并运行到手机上，其中前三个是端游的体验（需要您提前部署端游），最后一个是手游的体验（需要您提前部署手游）。
![img](https://qcloudimg.tencent-cloud.cn/raw/821db57e335fb3993b7e8d23303836db.png)

>! 云游戏的进阶使用，请参见 [云游戏接入指南](https://github.com/tencentyun/cloudgame-android-sdk)。
