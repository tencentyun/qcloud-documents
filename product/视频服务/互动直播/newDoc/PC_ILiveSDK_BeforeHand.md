## 简介
互动直播SDK for Windows，下文称为ILiveSDK(Windows)，是互动直播在Windows平台上的SDK。通过几个简单的接口调用即可实现互动直播、上麦和基础IM等功能。

## 下载SDK和Demo
在[github](https://github.com/zhaoyang21cn/iLiveSDK_PC_Demos)上将项目clone下来。代其中包含了ILiveSDK(IE)，接口文档，js接口文件和接口调用示例等，具体如下：


文件 | 说明 | 
----|------|
/suixinbo | demo随心播工程源码，可以和其他平台随心播互通  | 
/iLiveSDK | SDK的头文件和库文件  | 
/doc | 接口文档和其他说明文档  | 
suixinbo_run | 可以直接运行的demo程序 | 


## 运行和体验demo
随心播是一款基于腾讯云互动直播SDK的秀场直播类应用。它演示了主播直播，观众连麦互动，消息互通，点赞打赏等业务场景的实现。
### 运行demo程序
suixinbo_run.zip为已经编译好的可执行包，解压后，直接双击suixinbo_Qt.exe即可运行。

### 注册和登录
使用其他功能前必须登录，点击右上角按钮可以进行登录和注册

### 观看直播
选择直播列表tab，然后刷新直播列表可以看到当前正在进行的直播。点击其中一个直播即可开始观看。
![直播列表](https://mc.qcloudimg.com/static/img/170ae5e7bbaf52943c975a8ad79b2fdd/2.png)

### 创建直播
选择我要直播tab，点击按钮开始直播
![主播开播](https://mc.qcloudimg.com/static/img/b6522dc3bad8e79c5709a104781e16c0/suixinbo_kaibo.png)

### 直播间操作
主播和观众可以在直播间内进行设备管理，推流录制，收发消息，连麦互动
![直播房间](https://mc.qcloudimg.com/static/img/aa77c098fe7f2a2885fd817cd2643987/avroom.png)

## 运行demo工程
### 安装Qt环境
vs2010之后的版本，可以直接在VS中进行安装，步骤：工具->扩展和更新

![安装qt步骤1](https://mc.qcloudimg.com/static/img/e669d4451aca22173f8bf2ad67a894ab/pic.png)

联机->搜索qt->点击下载

![安装qt步骤2](https://mc.qcloudimg.com/static/img/da49e7fd3f853bfed5814369811188ed/pic.png)

然后重启vs，菜单栏中将会出现如下Qt菜单项

![安装qt步骤3](https://mc.qcloudimg.com/static/img/cb5b67ec89f573185a5ce7fbbd85ac9a/pic.png)

此时，需要在vs中配置Qt目录，配置方法为"Qt VS Tools"菜单项->Qt Options->add->选择Qt安装目录，如下图，

![安装qt步骤4](https://mc.qcloudimg.com/static/img/a6bfa24ca0c3ef8d39a289a4a120f4c0/pic.png)

增加好后，点击确定，如下图，

![安装qt步骤5](https://mc.qcloudimg.com/static/img/c5aacc84343bb566097960e1dd595339/pic.png)

注意:VS2010下，直接在VS中搜索找不到Qt插件，需要在Qt官网下载Qt插件，或[直接下载Qt5.0.0及vs2010插件](http://dldir1.qq.com/hudongzhibo/git/Qt/Qt_5.0.0.zip) ，然后进行手动安装（先装Qt，再装Qt插件）

### 随心播项目编译
使用vs打开suixinbo\sample目录下的suixinbo.sln，如果是vs2010之后的vs版本，会提示升级项目配置，点击"确定"。然后在项目suixinbo_Qt上右键->Qt Project Settings->配置项目使用的Qt版本，配置好后，如下图

![](https://mc.qcloudimg.com/static/img/1580d6b0287ea3ac8a88d81ee4d917c1/pic.png)
此时即可编译运行随心播了。

## 集成iLive SDK到自己的工程里
- iLive SDK在步骤一下载的iLiveSDK文件夹中，将iLiveSDK整个文件夹复制到解决方案文件(.sln文件)所在的目录;
- 添加include目录:<br/>
	在项目的附加包含目录中添加include目录, $(SolutionDir)iLiveSDK\include,如下图,<br/>
![](http://mc.qcloudimg.com/static/img/3ab82b780f87b8749813f028a904ea0e/image.png)
- 添加库目录:<br/>
	在项目的附加库目录中添加lib文件所在目录,$(SolutionDir)iLiveSDK\libs\$(Configuration),如下图,<br/>
![](http://mc.qcloudimg.com/static/img/0fbd938dbbf189c40e195cb60689baf4/image.png)
- 包含头文件:<br/>
	在项目中包含头文件(通常是预编译头中),并使用相关命名空间，加载动态库的lib文件,代码如下，

```C++
	#include “ilive.h"
	#pragma comment(lib, "ilivesdk.lib")
	using namespace ilive;
```

- 拷贝dll文件到exe所在目录:<br/>
	将libs\Debug目录下的所有dll文件复制到项目的Debug版本运行目录下，libs\Release目录下的所有dll文件复制到项目的Release版本运行目录下;

- 验证是否配置成功:<br/>
	调用GetILive()->getVersion(),返回当前iLiveSDK的版本号;
  
	
	
