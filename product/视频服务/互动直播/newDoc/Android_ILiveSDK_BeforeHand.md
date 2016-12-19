## 一 下载Demo
点击下载[Android Demo](https://github.com/zhaoyang21cn/ILiveSDK_Android_Demos)的代码。代码里包含两个示例：<br/>

1. tdemolive目录下是一个最简单的互动直播示例，演示了最关键的几个接口的调用。使用方法可以参考github上的说明。
2. 随心播代码在suixinbo目录下。演示了包括界面和后台交互的完整的直播流程。

## 二 修改配置

1. 把随心播代码中的appid和accountType修改成开发者自己的。<br/>
![](https://mc.qcloudimg.com/static/img/62890dee5794a2ce94404ba762624b94/idntype.png)
2. 注释maven.oa.com的引用，改成jcenter库地址。<br/>   
![](https://mc.qcloudimg.com/static/img/8c4c9bf238499dec32aca993d9ff7ad4/respositories.png)
   
   
## 三 运行
编译运行工程，在启动界面选择随心播。

* ![主界面](https://mc.qcloudimg.com/static/img/1be6185cdb0f61756c85e230a9fc0514/2.png)
* ![直播界面](https://mc.qcloudimg.com/static/img/ccf7ca496a22ec0aed9d4446f30ba85f/1.png)


## 四 集成到开发者自己的代码工程里
### 1 引入SDK
* **aar方式集成**,(强烈推荐)<br/>
	如果你使用的Android Studio开发，那么导入iliveSDK非常简单。只需一行代码就可以搞定了 

	compile 'com.tencent.ilivesdk:ilivesdk:X.X.X'  
	
	(X.X.X 替换成对应版本号 比如0.3.7)。同步完成之后可以在build文件夹中找到ilivesdk文件夹。<br /> 
![](https://mc.qcloudimg.com/static/img/ecd51eab082087cd2049a6a06a84ea76/ilivelocation.png)
	
		
* **传统库类方式集成**，<br/>
在腾讯云官网[下载音视频库类](https://console.qcloud.com/avc/avSdkDownload)。需要把so文件和jar包文件分别放到对应jnilibs和libs里面。        
![](https://mc.qcloudimg.com/static/img/e3cc8175676d647dd657beebb11cc2e3/1.png)
### 2 配置服务修改后台server地址
 目前随心播后台主要用来维护直播房间列表。如果复用随心播客户端代码，需要修改随心播后台地址为业务方自己部署的服务器地址。 <br />     
      
| 接口| 说明 |
|---------|---------|
| GET_MYROOMID | 获取自己分配的房间号 |
| NEW_ROOM_INFO | 创建新房间 |
| STOP_ROOM | 退出房间 |
| GET_LIVELIST | 获取房间列表 |
| SEND_HEARTBEAT | 房间心跳 |
| GET_COS_SIG | 图片上传相关 |
 
  ![](https://mc.qcloudimg.com/static/img/06919328fe28d9088170fc2a6b0f7ee9/server.png)

### 3 添加混淆配置
* 混淆相关<br /> 

		-keep class com.tencent.**{*;}
		-dontwarn com.tencent.**

		-keep class tencent.**{*;}
		-dontwarn tencent.**

		-keep class qalsdk.**{*;}
		-dontwarn qalsdk.**
		
### 4 配置service
![](https://mc.qcloudimg.com/static/img/afa18e51202e3e80232841d215d90f7b/qalservice.png)
### 5 配置权限
![](https://mc.qcloudimg.com/static/img/55db2326bef2d0270ab17e81d945da22/rights.png)
### 6 删除非armeabi架构so 
* 由于目前只支持armeabi架构，如果工程(或依赖库)中有多架构，需要在build.gradle中添加以下配置<br /> （如果包含子工程子工程也要加）
<pre>
android{
    defaultConfig{
        ndk{
            abiFilter 'armeabi'
        }
    }
}




