## 一 下载Demo
目前在github上提供了两个示例：<br/>
* [随心播](https://github.com/zhaoyang21cn/ILiveSDK_Android_Demos) 演示了包括界面和后台交互的完整的直播流程
* [简单直播](https://github.com/zhaoyang21cn/iLiveSDK_Android_LiveDemo) 最简单的互动直播示例，演示了最关键的几个接口的调用。

## 二 修改配置

把随心播代码中的appid和accountType修改成开发者自己的。<br/>
![](https://mc.qcloudimg.com/static/img/62890dee5794a2ce94404ba762624b94/idntype.png)

## 三 运行
编译运行工程，在启动界面选择随心播。

* ![主界面](https://mc.qcloudimg.com/static/img/1be6185cdb0f61756c85e230a9fc0514/2.png)
* ![直播界面](https://mc.qcloudimg.com/static/img/ccf7ca496a22ec0aed9d4446f30ba85f/1.png)


## 四 集成到开发者自己的代码工程里
### 1 引入SDK
* **aar方式集成**,(强烈推荐)<br/>
	如果你使用的Android Studio开发，那么导入iliveSDK非常简单。只需两行代码就可以搞定了 


	直播业务功能       
	compile 'com.tencent.livesdk:livesdk:X.X.X'      
	核心功能     
	compile 'com.tencent.ilivesdk:ilivesdk:X.X.X' 

	
	(X.X.X 替换成对应版本号 比如1.0.1)。同步完成之后可以在build文件夹中找到livesdk和ilivesdk文件夹。<br /> 
![](https://mc.qcloudimg.com/static/img/ecd51eab082087cd2049a6a06a84ea76/ilivelocation.png)
	
		
* **传统库类方式集成**，<br/>
在腾讯云官网[下载音视频库类](https://console.qcloud.com/avc/avSdkDownload)。需要把so文件和jar包文件分别放到对应jnilibs和libs里面。        
![](https://mc.qcloudimg.com/static/img/e3cc8175676d647dd657beebb11cc2e3/1.png)
### 2 配置服务修改后台server地址
 目前随心播由业务后台(开源可复用，[源码](https://github.com/zhaoyang21cn/SuiXinBoPHPServer))主要用来维护直播房间列表。<br />
 如果复用随心播客户端代码，需要修改随心播后台地址为业务方自己部署的服务器地址。 <br />    
      
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
* 由于目前只支持armeabi和armeabi-v7a架构，如果工程(或依赖库)中有多架构，需要在build.gradle中添加以下配置<br /> （如果包含子工程子工程也要加）
<pre>
android{
    defaultConfig{
        ndk{
            abiFilters 'armeabi', 'armeabi-v7a'
        }
    }
}
</pre>



