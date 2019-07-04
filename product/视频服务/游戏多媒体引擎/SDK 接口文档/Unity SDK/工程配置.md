## 操作场景
为方便 Unity 开发者调试和接入腾讯云游戏多媒体引擎产品 API，这里向您介绍适用于 Unity 开发的工程配置。


## 操作步骤
### 下载 SDK
1. 请先下载相关 Demo 及 SDK。详细下载链接请查看  [SDK 下载指引](https://cloud.tencent.com/document/product/607/18521)。
2. 在界面中找到 Unity 版本的 SDK 资源。
3. 单击【下载】。下载完的 SDK 资源解压后有以下几个部分。文件说明如下表：
![](https://main.qcloudimg.com/raw/55494d9bb9145938f0594416f73b29f7.png)

|文件名       | 说明           
| ------------- |:-------------:|
| Plugins   	|SDK 库文件|
| Scripts     	|SDK 代码文件|

### 预备工作
#### 1. 导入 Plugins 文件
将开发工具包中 Plugins 文件夹中的文件复制在 Unity 工程中 Assets 下的 Plugins 文件夹中，如图所示：  
![](https://main.qcloudimg.com/raw/1221a25f62cedd3831cf2bb27bb1ea45.png)
#### 2. 导入代码文件
将开发工具包中 Scripts 文件夹中的文件复制在 Unity 工程中存放代码的文件夹中，如图所示：  
![](https://main.qcloudimg.com/raw/8904a83c6173fa7c5b04ddb0e48138ca.png)
#### 3. 音频设置
在 Unity 编辑器中，Edit-Project Setting-Audio 使用系统默认即可。如果进行修改，Unity 播放音效会因为在 iOS 上设置硬件缓存区受影响，表现为音效被打断。如图所示：
![](https://main.qcloudimg.com/raw/3cc4595336bda52c733d8c641a293c51.png)
如果设置为下图这种模式，Unity 播放音效会因为在 iOS 上设置硬件缓存区受影响，表现为音效被打断。如图所示：
![](https://main.qcloudimg.com/raw/c1b7d75b98a664ff25ec97c025a754cf.png)


### 导出不同平台
从 Unity 引擎导出不同平台，需要做相应的工程配置：

|平台       | 工程配置           
| ------------- |:-------------:|
| Android |[Android 工程配置文档](https://cloud.tencent.com/document/product/607/15203)|
| iOS     	|[iOS 工程配置文档](https://cloud.tencent.com/document/product/607/15219)|
| Mac     	|[Mac 工程配置文档](https://cloud.tencent.com/document/product/607/18617)|
