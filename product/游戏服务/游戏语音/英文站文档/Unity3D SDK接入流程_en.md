This document describes the method of connecting to C# API SDK of GVoice. The method is applicable to games developed via Unity3D engine.
## 1 Download SDK
[Download Unity3D SDK package v1.1.2](http://doc-10010986.cos.myqcloud.com/gvoice/gcloud_voice_1_1_2_136114_20161209_Unity3D.zip))  
Download and decompress the SDK package, you will see: 
![](https://mc.qcloudimg.com/static/img/ef63d54941048e51fdaf9c023fa8be2f/image.jpg)
## 2 System Configuration
### 2.1 iOS System Configuration
1. Copy the directory `dist\Unity3D\Plugins\iOS\GCloudVoice.bundle` to your project `MyProj\Assets\Plugins\iOS`.  
2. Link the static library `dist\Unity3D\Plugins\iOS\libGCloudVoice.a` in the package. For `Xcode` projects exported by `Unity3D`, you need to link 6 system libraries as following:
![](https://mc.qcloudimg.com/static/img/a6b6942b66e94582145b89b224ce6f5f/ios.jpg)

### 2.2 Android System

1. In `dist\Unity3D\Plugins\Android`, copy the `GCloudVoice` and `assets` folders to your project `MyProj\Assets\Plugins\Android`.  
2. Copy the `cs` script file under `dist\Unity3D\Scripts\GCloudVoice` to the `Scripts` folder. Please note that the naming space is `gcloud_voice`.  
3. Add `Init` code of Java level in function `OnCreate` of main `Activiy` of game. Import the class: `import com.tencent.gcloud.voice.GCloudVoiceEngine`; call `Init` code:     

![](https://mc.qcloudimg.com/static/img/bdea05411bb37424592d69a76dc595e7/image.jpg)

## 3 Call APIs
1. Basic API: For both Voice Chat and Voice Message features, you need to call basic APIs for initialization at start and deinitialization at the end. You also need to call `Poll` for callbacks of APIs called in the process.
[Call Basic APIs](https://cloud.tencent.com/document/product/556/7675).  
2. Voice Chat API: Used for Voice Chat feature
[Call of instant voice API](https://cloud.tencent.com/document/product/556/7676).   
3. Voice Message API: Used for Voice Message feature
[Call of voice message API](https://cloud.tencent.com/document/product/556/7677)    
![](https://mc.qcloudimg.com/static/img/c2055b982fda95b416144c907dfceed0/1.png) 