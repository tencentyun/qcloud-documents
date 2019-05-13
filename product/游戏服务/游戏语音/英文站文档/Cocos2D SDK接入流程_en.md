This document introduces how to access C++ API SDK of GVoice. The method is applicable to games developed using Cocos2D engine, and developed on iOS and Android platforms.
## 1 Download SDK
[Download Cocos SDK package v1.1.2] (http://doc-10010986.cos.myqcloud.com/gvoice/gcloud_voice_1_1_2_136114_20161209_Cocos.zip)  
Download and decompress the SDK package, you will see:  
![](https://mc.qcloudimg.com/static/img/2f7a1f0e63529d18107011635287be2a/ml.png)
## 2 System Configuration
### 2.1 iOS System Configuration
For Xcode projects of iOS, add `include` and `libs/iOS` directory to the Xcode project, and set the quote location of header file.  
![](https://mc.qcloudimg.com/static/img/d186e23a1f2db7d43e474be2e0f1ca2e/ios.png)  
In Xcode, it will be displayed as follows:  
![](https://mc.qcloudimg.com/static/img/e0d3b66bd24110e3f660a0af924e703f/ios2.png)  
Link system libraries as below:  
![](https://mc.qcloudimg.com/static/img/e0cdfcc5b722513e1d9816ee09acd768/ios3.png)
Then compile in Cocos method .

### 2.2 Android System

For Android projects, take `Proj.android` for example. Copy `assetes/GCloudVoice` to the `Resource` directory of Cocos project. And copy `libs/Android/GCloudVoice.jar` to `proj.android/libs`. Finally save `include` and `libs/Android` directories to the location you want (e.g. create a `GCloudVoice` directory under the project).  
![](https://mc.qcloudimg.com/static/img/90acaeb06e746d2acd5d07c2f41bc232/a1.png)
    
![](https://mc.qcloudimg.com/static/img/2e44876b63428705d2272969054dfe2f/a2.png)    

Refer library file and header file in Android.mk of `proj.anroid/jni`:     
![](https://mc.qcloudimg.com/static/img/1404bf2b0695df38f6c9a384535d38e1/a3.png)
   
![](https://mc.qcloudimg.com/static/img/23e45d00dceb4e5c3579694f302b8def/a4.png)
  
![](https://mc.qcloudimg.com/static/img/f0879d7be78cf030df4bb8e8992ec0ea/a5.png)    

Add the following permissions to `proj.android/AndroidManifest.xml`, and compile in Cocos method.    
![](https://mc.qcloudimg.com/static/img/381baf249785146078c5ce1c7f5ef24c/a6.png)  

Conduct initialization in Java. See below:  

    public class AppActivity extends Cocos2dxActivity {
    	@Override
    	protected void onCreate(final Bundle savedInstanceState) {
    		super.onCreate(savedInstanceState);
    		GCloudVoiceEngine.getInstance().init(getApplicationContext(), this);
    	}
    }
## 3 Call APIs
1. Basic API: For both Voice Chat and Voice Message features, you need to call basic APIs for initialization at start and deinitialization at the end. You also need to call `Poll` for callbacks of APIs called in the process.
[Call Basic APIs](https://cloud.tencent.com/document/product/556/7665).  
2. Voice Chat API: Used for Voice Chat feature
[Call Voice Chat APIs](https://cloud.tencent.com/document/product/556/7667).   
3. Voice Message API: Used for Voice Message feature
[Call Voice Message APIs](https://cloud.tencent.com/document/product/556/7670)    
![](https://mc.qcloudimg.com/static/img/c2055b982fda95b416144c907dfceed0/1.png)  


 
