本文档介绍了GVoice游戏语音C#接口SDK的接入方法，适用于Unity3D引擎开发的游戏。
## 1 下载SDK
[Unity3D SDK 下载](https://cloud.tencent.com/document/product/556/10041)
[Unity3D Demo 下载](https://cloud.tencent.com/document/product/556/10042)

下载SDK包解压后，目录结构如下： 
![](https://mc.qcloudimg.com/static/img/ef63d54941048e51fdaf9c023fa8be2f/image.jpg)
## 2 系统配置
### 2.1 iOS系统配置
1.将压缩包中的 `dist\Unity3D\Plugins\iOS\ GCloudVoice.bundle` 整个文件夹拷贝到自己的工程 `MyProj\Assets\Plugins\iOS` 目录下。  
2.链接发布包中静态库`dist\Unity3D\Plugins\iOS\libGCloudVoice.a`，在`Unity3d`导出的`Xcode`工程中，同时需要链接如下6个系统库：

![](https://mc.qcloudimg.com/static/img/a6b6942b66e94582145b89b224ce6f5f/ios.jpg)

### 2.2 Android系统

1.将压缩包中的 `dist\Unity3D\Plugins\Android` 目录下的 `GCloudVoice`、`assets`两个文件夹拷贝到自己的工程`MyProj\Assets\Plugins\Android`目录下。  
2.将压缩包中的 `dist\Unity3D\Scripts\GCloudVoice` 目录下的`cs`脚本文件，拷贝到工程`Scripts`文件夹中，使用即可。注意，使用时命名空间为`gcloud_voice`。  
3.在游戏主`Activiy`的`OnCreate`函数处，添加`Java`层的`Init`代码。 导入类：`import com.tencent.gcloud.voice.GCloudVoiceEngine;` 调用`Init`代码：     

![](https://mc.qcloudimg.com/static/img/bdea05411bb37424592d69a76dc595e7/image.jpg)

## 3 接口调用流程
1.基本API：无论实时语音，还是消息语音功能，都需要调用基本API,在开始时进行语音的初始化，结束时进行反初始化，以及中间调用API时，需要调用poll触发处理相关回调，
[基本API调用 ](https://cloud.tencent.com/document/product/556/7675)。  
2.实时语音API：实时语音功能调用，
[实时语音API调用](https://cloud.tencent.com/document/product/556/7676)。   
3.语音消息API：消息语音功能调用，
[语音消息API调用](https://cloud.tencent.com/document/product/556/7677)。    
![](https://mc.qcloudimg.com/static/img/c2055b982fda95b416144c907dfceed0/1.png) 