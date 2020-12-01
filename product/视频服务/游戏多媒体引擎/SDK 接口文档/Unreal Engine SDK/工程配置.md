## 简介
为方便 Unreal Engine 开发者调试和接入腾讯云游戏多媒体引擎产品 API，这里向您介绍适用于 Unreal Engine 开发的工程配置。

## SDK 准备
1. 请在 [下载指引](https://cloud.tencent.com/document/product/607/18521) 下载相关 Demo 及 SDK。
2. 在 Unreal Engine 工程目录下，打开 Plugins 文件夹（如果没有请自行创建），拷贝 SDK 进去，SDK 目录如下图：
![](https://main.qcloudimg.com/raw/751894ab16c5262b7a99370cc7efd52c.png)
3. 导入之后，在 Unreal Engine 引擎中对插件进行编译。
![](https://main.qcloudimg.com/raw/562882f1d39aa0d4fc77e835290d99df.png)
4. 编译完成后，在 VS2015 中会出现以下目录。
![](https://main.qcloudimg.com/raw/3005bc887e0179bdc45719b07a61f778.png)
5. 重新打开 Unreal Engine 引擎，单击【编辑】，单击【Plugins】，即可查看 GME 插件。
![](https://main.qcloudimg.com/raw/60fb6340f6899e2c8fc6f4693193533e.png)
6. 如果是使用 Unreal Engine 4.21及以上版本，下载使用 GME Unreal Engine 示例代码后要添加以下代码：
```
AUEDemoLevelScriptActor::AUEDemoLevelScriptActor()
{
    PrimaryActorTick.bCanEverTick = true;
}
```

>?在默认的情况下，tick 为关闭状态，必须手动开启。

## 导出不同平台
从 Unreal 引擎导出不同平台，需要做相应的工程配置：

|平台       | 工程配置           
| ------------- |:-------------:|
| Android |[Android 工程配置文档](https://cloud.tencent.com/document/product/607/15203)|
| iOS     	|[iOS 工程配置文档](https://cloud.tencent.com/document/product/607/15219)|
| macOS     	|[macOS 工程配置文档](https://cloud.tencent.com/document/product/607/18617)|
  
  
