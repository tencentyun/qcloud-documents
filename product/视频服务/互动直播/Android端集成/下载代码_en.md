## Download Demo
Currently, two examples are provided on github.<br/>
* [FreeShow](https://github.com/zhaoyang21cn/ILiveSDK_Android_Demos) demonstrates a complete LVB procedure including interface and backend interaction.
* [QuickShow](https://github.com/zhaoyang21cn/iLiveSDK_Android_LiveDemo) is the simplest ILVB example, demonstrating how to call the most critical APIs.

## Modify Configuration

Change appid and accountType in the code of FreeShow to that of developer.<br/>
![](https://mc.qcloudimg.com/static/img/62890dee5794a2ce94404ba762624b94/idntype.png)

## Run the project
Compile and run project, and select **FreeShow** in startup interface.

* ![Main Interface](https://mc.qcloudimg.com/static/img/1be6185cdb0f61756c85e230a9fc0514/2.png)
* ![LVB Interface](https://mc.qcloudimg.com/static/img/ccf7ca496a22ec0aed9d4446f30ba85f/1.png)


## Integrate into developer's code project
### 1. Introduce SDK
* **aar-type integration** (strongly recommended)<br/>
	If you use Android Studio for development, it is very easy to import iliveSDK. This can be done by writing simple codes. 


	LVB Business Feature       
	compile 'com.tencent.livesdk:livesdk:X.X.X'      
	Core Feature     
	compile 'com.tencent.ilivesdk:ilivesdk:X.X.X' 

	
	(replace X.X.X with corresponding version number, e.g. 1.0.1). livesdk and ilivesdk folders can be found in build folder after synchronization.<br /> 
![](https://mc.qcloudimg.com/static/img/ecd51eab082087cd2049a6a06a84ea76/ilivelocation.png)
	
		
* **Traditional library class-type integration**<br/>
[Download audio and video library classes](https://console.cloud.tencent.com/avc/avSdkDownload) from Tencent Cloud's official website. You should place so folder and jar package file into the corresponding jnilibs and libs.        
![](https://mc.qcloudimg.com/static/img/e3cc8175676d647dd657beebb11cc2e3/1.png)
### 2. Configure Service and Modify Backend Server Address
 Currently, for FreeShow, the live room list is maintained at the business backend ([Source Code](https://github.com/zhaoyang21cn/SuiXinBoPHPServer) can be reused if open sourced).<br />
 If you want to reuse FreeShow client code, you need to modify the backend address of FreeShow to the server address deployed at the business side. <br />    
      
| API | Description |
|---------|---------|
| GET_MYROOMID | Acquire the room number assigned by yourself |
| NEW_ROOM_INFO | Create new room |
| STOP_ROOM | Exit a room |
| GET_LIVELIST | Acquire room list |
| SEND_HEARTBEAT | Room hartbeat |
| GET_COS_SIG | Configuration related to image uploading |
 
  ![](https://mc.qcloudimg.com/static/img/06919328fe28d9088170fc2a6b0f7ee9/server.png)

### 3. Add Proguard Configuration
* Proguard-related<br /> 

		-keep class com.tencent.**{*;}
		-dontwarn com.tencent.**

		-keep class tencent.**{*;}
		-dontwarn tencent.**

		-keep class qalsdk.**{*;}
		-dontwarn qalsdk.**
		
### 4. Configure Service
![](https://mc.qcloudimg.com/static/img/afa18e51202e3e80232841d215d90f7b/qalservice.png)
### 5. Configure Permission
![](https://mc.qcloudimg.com/static/img/55db2326bef2d0270ab17e81d945da22/rights.png)
### 6. Delete Non-armeabi Architecture so 
* Currently, only armeabi and armeabi-v7a architectures are supported. If the project (or dependent library) have multiple architectures, the following configurations are required in build.gradle<br /> (also required for sub-project if any)
<pre>
android{
    defaultConfig{
        ndk{
            abiFilters 'armeabi', 'armeabi-v7a'
        }
    }
}
</pre>




