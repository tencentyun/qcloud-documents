## 一 下载Demo
点击下载[PC Demo](https://github.com/zhaoyang21cn/iLiveSDK_PC_Demos)的代码。代码里包含一个示例：<br/>
1. 随心播代码在suixinbo目录下。演示了包括界面和后台交互的完整的直播流程。

## 二 安装Qt环境
随心播使用的是QT做界面库,在vs2010下开发的，所以需要先安装Qt 5.0.0,方可编译运行；可以去Qt的官网下载，也可以[点击这里下载](http://dldir1.qq.com/hudongzhibo/git/Qt/Qt_5.0.0.zip);下载解压后，文件目录如下，<br/>
![](http://mc.qcloudimg.com/static/img/00d8b25ddf3160c0673327568cd559fc/image.png)<br/>
先安装Qt5.0.0，再安装vs2010的Qt开发插件;安装完成后，重启VS2010，即可在vs的菜单栏中看到Qt菜单,如下图,<br/>
![](http://mc.qcloudimg.com/static/img/3422fe8496cd39d1b7d6c2b418460765/image.png)<br/>
此时,在Qt-->Qt Option菜单中可以查看本机已经安装的Qt版本，如下图,<br/>
![](http://mc.qcloudimg.com/static/img/435adc9eeb163e34bc4e602acfc900a1/image.png)<br/>
如果没有任何可用版本，点击add添加前面安装的Qt目录即可;至此，Qt安装完成;

## 三 运行
suixinbo_run.zip为已经编译好的可执行包，解压后，直接双击suixinbo_Qt.exe即可运行;如果用户需要自己编译，需要按照上面第二步所示先安装vs2010及Qt环境;
* 直播房间列表<br/>
![直播列表](https://mc.qcloudimg.com/static/img/170ae5e7bbaf52943c975a8ad79b2fdd/2.png)
* 直播界面<br/>
![直播房间](https://mc.qcloudimg.com/static/img/170071f70b13d09af4acd323df351420/3.png)

## 四 集成iLive SDK到开发者自己的代码工程里
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
	#include <ilivesdk/ilivesdk.h>
	#pragma comment(lib, "ilivesdk.lib")
	using namespace imcore;
	using namespace tencent::av;
	using namespace ilivesdk;
```

- 拷贝dll文件到exe所在目录:<br/>
	将libs\Debug目录下的所有dll文件复制到项目的Debug版本运行目录下，libs\Release目录下的所有dll文件复制到项目的Release版本运行目录下;

- 验证是否配置成功:<br/>
	调用iLiveSDK::getInstance()->getVersion(),输出返回值，查看当前iLiveSDK的版本号;
  
	
	
