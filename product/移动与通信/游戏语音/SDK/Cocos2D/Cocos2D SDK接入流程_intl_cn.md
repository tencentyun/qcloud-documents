本文档介绍了GVoice游戏语音C++接口SDK的接入方法，适用于Cocos2D引擎，或iOS、Android平台直接开发的游戏。

## 1 下载SDK
[Cocos2D SDK 下载](https://cloud.tencent.com/document/product/556/10041)
[Cocos2D Demo 下载](https://cloud.tencent.com/document/product/556/10042)

下载SDK包解压后，目录结构如下：  
![](https://mc.qcloudimg.com/static/img/2f7a1f0e63529d18107011635287be2a/ml.png)
## 2 系统配置

### 2.1 iOS系统配置
对于iOS的Xcode工程，只要将include目录和libs/iOS目录添加到Xcode工程中并设置头文件引用位置即可。  
![](https://mc.qcloudimg.com/static/img/d186e23a1f2db7d43e474be2e0f1ca2e/ios.png)  
在Xcode中显示为：  
![](https://mc.qcloudimg.com/static/img/e0d3b66bd24110e3f660a0af924e703f/ios2.png)  
同时需要添加系统库：  
![](https://mc.qcloudimg.com/static/img/e0cdfcc5b722513e1d9816ee09acd768/ios3.png)
然后按照Cocos的编译方式编译就可以了。

### 2.2 Android系统

对于Android工程，这里以proj.android为例，将压缩包中的assetes目录中的GCloudVoice目录放到Cocos工程的Resource目录下。接着讲libs/Android/GCloudVoice.jar文件放到proj.android/libs目录下。最后将include和libs/Android目录放到合适的目录，比如工程下面建一个GCloudVoice目录：  
![](https://mc.qcloudimg.com/static/img/90acaeb06e746d2acd5d07c2f41bc232/a1.png)
    
![](https://mc.qcloudimg.com/static/img/2e44876b63428705d2272969054dfe2f/a2.png)    

在proj.anroid/jni的Android.mk中添加对库文件和头文件的引用：     
![](https://mc.qcloudimg.com/static/img/1404bf2b0695df38f6c9a384535d38e1/a3.png)
   
![](https://mc.qcloudimg.com/static/img/23e45d00dceb4e5c3579694f302b8def/a4.png)
  
![](https://mc.qcloudimg.com/static/img/f0879d7be78cf030df4bb8e8992ec0ea/a5.png)    

最后在proj.android/AndroidManifest.xml添加如下权限即可按照Cocos的编译方式编译运行了。    
![](https://mc.qcloudimg.com/static/img/381baf249785146078c5ce1c7f5ef24c/a6.png)  

最后需要在Java测进行初始化，比如：  

    public class AppActivity extends Cocos2dxActivity {
    	@Override
    	protected void onCreate(final Bundle savedInstanceState) {
    		super.onCreate(savedInstanceState);
    		GCloudVoiceEngine.getInstance().init(getApplicationContext(), this);
    	}
    }
## 3 接口调用流程
1.基本API：无论实时语音，还是消息语音功能，都需要调用基本API,在开始时进行语音的初始化，结束时进行反初始化，以及中间调用API时，需要调用poll触发处理相关回调，
[基本API调用 ](https://cloud.tencent.com/document/product/556/7665)。  
2.实时语音API：实时语音功能调用，
[实时语音API调用](https://cloud.tencent.com/document/product/556/7667)。   
3.语音消息API：消息语音功能调用，
[语音消息API调用](https://cloud.tencent.com/document/product/556/7670)。    
![](https://mc.qcloudimg.com/static/img/c2055b982fda95b416144c907dfceed0/1.png)  


 
