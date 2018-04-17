Welcome to Tencent Cloud Game Multimedia Engine (GME) SDK. This document describes project configuration for Cocos2d development so that Cocos2d developers can easily debug and access APIs for Tencent Cloud GME.

## SDK Acquisition
You can contact the staff to obtain the SDK.

### Decompress the SDK resource package.
Decompress the obtained SDK resource package. The following table describes the folders in the package.

|Folder Name     		| Description
| ---------------------- |-----------------------------------	|
| TMG_SDK     		|Game audio-video SDK framework files.	|
| TMGCocosDemo   	|Game audio-video SDK sample project.			|

## OS Requirements
The SDK can be compiled in the Mac OS.

## iOS Xcode Preparation
### 1. Import the SDK framework files. 
Add the required framework to the Xcode project and set the reference location of the header file. The result is shown in the following figure.

![](https://main.qcloudimg.com/raw/3e3b6a7ed89b4665bb8e2eb72214e02e.png)

There are three framework folders in the **TMG_SDK** folder as follows.
>TMGSDK_cocos_audio.framework:

This audio-video SDK is mandatory.
>QAVSDKAuthBuffer.framework:

This SDK is used to generate encryption strings for voice chat room permissions. It can be deployed at the backend during formal deployment. Therefore, this SDK is not mandatory during project configuration.
>QAVSDKTlsSig.framework:

This SDK is used to generate encryption verification strings for PTT. If PTT is not used, this SDK is not required during project configuration.

### 2. Add dependent libraries.  
For more information, see the following figure.  
![](https://main.qcloudimg.com/raw/8241677307d71444c391cfd89d9a8355.png)

## Android Preparation
### 1. Add the **tmgsdk.jar** file to the **libs** folder.
![](https://main.qcloudimg.com/raw/d98214986c57df2ad8a12db7501b642c.png)

### 2. Import SO files into **Activity**.
```
public class AppActivity extends Cocos2dxActivity {
    static final String TAG = "AppActivity";
    static OpensdkGameWrapper gameWrapper ;
    static {
        Log.e(TAG, "Load so begin");
        System.loadLibrary("stlport_shared");
        System.loadLibrary("xplatform");
        System.loadLibrary("UDT");
        System.loadLibrary("qav_authbuff");
        System.loadLibrary("qav_tlssign");
        System.loadLibrary("traeimp-armeabi-v7a");
        System.loadLibrary("qavsdk");
        Log.e(TAG, "Load so end");
    }
}
```

### 3. Initialize the project.
Initialize the project using the onCreate function and pay attention to the sequence.
```
protected void onCreate(Bundle savedInstanceState) {
        super.setEnableVirtualButton(false);
        super.onCreate(savedInstanceState);

        //Pay attention to the sequence during initialization.
        AVLoggerChooser.setUseImsdk(false);
        AVChannelManager.setIMChannelType(AVChannelManager.IMChannelTypeImplementInternal);
        gameWrapper = new OpensdkGameWrapper(this);
        runOnGLThread(new Runnable() {
            @Override
            public void run() {
                gameWrapper.initOpensdk();
            }
        });
}
```
