本文档介绍了 GVoice 游戏语音 C++ 接口 SDK 的接入方法，适用于 Cocos2D 引擎，或 iOS、Android 平台直接开发的游戏。

## 1 下载SDK
[Cocos2D SDK 下载](https://cloud.tencent.com/document/product/556/10041)
[Cocos2D Demo 下载](https://cloud.tencent.com/document/product/556/10042)

下载 SDK 包解压后，目录结构如下：  
![](https://mc.qcloudimg.com/static/img/2f7a1f0e63529d18107011635287be2a/ml.png)
## 2 系统配置

### 2.1 iOS系统配置
对于 iOS 的 Xcode 工程，只要将 include 目录和 libs/iOS 目录添加到 Xcode 工程中并设置头文件引用位置即可。  
![](https://mc.qcloudimg.com/static/img/d186e23a1f2db7d43e474be2e0f1ca2e/ios.png)  
在 Xcode 中显示为：  
![](https://mc.qcloudimg.com/static/img/e0d3b66bd24110e3f660a0af924e703f/ios2.png)  
同时需要添加系统库：  
![](https://mc.qcloudimg.com/static/img/e0cdfcc5b722513e1d9816ee09acd768/ios3.png)
然后按照 Cocos 的编译方式编译就可以了。

### 2.2 Android 系统

对于 Android 工程，这里以 proj.android 为例，将压缩包中的 assetes 目录中的 GCloudVoice 目录放到 Cocos 工程的Resource 目录下。接着将 libs/Android/GCloudVoice.jar文件放到 proj.android/libs 目录下。最后将 include 和libs/Android 目录放到合适的目录，比如工程下面建一个 GCloudVoice 目录：  
![](https://mc.qcloudimg.com/static/img/90acaeb06e746d2acd5d07c2f41bc232/a1.png)
    
![](https://mc.qcloudimg.com/static/img/2e44876b63428705d2272969054dfe2f/a2.png)    

在 proj.anroid/jni 的 Android.mk 中添加对库文件和头文件的引用：     
![](https://mc.qcloudimg.com/static/img/1404bf2b0695df38f6c9a384535d38e1/a3.png)
   
![](https://mc.qcloudimg.com/static/img/23e45d00dceb4e5c3579694f302b8def/a4.png)
  
![](https://mc.qcloudimg.com/static/img/f0879d7be78cf030df4bb8e8992ec0ea/a5.png)    

最后在 proj.android/AndroidManifest.xml 添加如下权限即可按照 Cocos 的编译方式编译运行了。    
![](https://mc.qcloudimg.com/static/img/381baf249785146078c5ce1c7f5ef24c/a6.png)  

最后需要在 Java 测进行初始化，比如：  

    public class AppActivity extends Cocos2dxActivity {
    	@Override
    	protected void onCreate(final Bundle savedInstanceState) {
    		super.onCreate(savedInstanceState);
    		GCloudVoiceEngine.getInstance().init(getApplicationContext(), this);
    	}
    }
## 3 接口调用流程
1.基本 API：无论实时语音，还是消息语音功能，都需要调用基本 API,在开始时进行语音的初始化，结束时进行反初始化，以及中间调用 API 时，需要调用 poll 触发处理相关回调，
[基本 API 调用 ](https://cloud.tencent.com/document/product/556/7665)。  
2.实时语音 API：实时语音功能调用，
[实时语音 API 调用](https://cloud.tencent.com/document/product/556/7667)。   
3.语音消息 API：消息语音功能调用，
[语音消息 API 调用](https://cloud.tencent.com/document/product/556/7670)。    
![](https://mc.qcloudimg.com/static/img/c2055b982fda95b416144c907dfceed0/1.png)  


 
