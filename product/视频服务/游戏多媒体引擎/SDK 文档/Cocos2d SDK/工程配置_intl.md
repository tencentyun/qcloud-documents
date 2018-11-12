Thank you for using Tencent Cloud Game Multimedia Engine SDK. This document provides project configuration that makes it easy for Cocos2D developers to debug and integrate the APIs for Game Multimedia Engine.

## SDK Preparation

Please download applicable Demo and SDK from [Downloading Instructions](/document/product/607/18521).

### Decompressing SDK resources

1. Decompress obtained SDK resources
2. The folders are as follows:

| Folder Name | Description
| ----------------------|-----------------------------------        |
| TMG_SDK                    |Mobile Gaming SDK framework file        |
| TMGCocosDemo          | Mobile Gaming SDK project sample	|

## System Requirement

The SDK can be compiled on Mac.

## iOS Xcode Preparations

### 1. Import SDK related framework file

Add framework to Xcode project and set the reference location of the header file.

GMESDK.framework, the Mobile Gaming SDK framework file in TMG_SDK folder, must be added to the project.

### 2. Add dependent libraries

Refer to the figure below:  
![](https://main.qcloudimg.com/raw/b6156b8c7a596248c148607070e38f67.png)

## Android Preparations

### 1. Add tmgsdk.jar to libs library.

![](https://main.qcloudimg.com/raw/fe1bde45a15f273aa9b9707420bb2696.png)

### 2. Import so file to Activity.

```
public class AppActivity extends Cocos2dxActivity {
    static final String TAG = "AppActivity";
    static OpensdkGameWrapper gameWrapper ;
    static {
        OpensdkGameWrapper.loadSdkLibrary();
    }
}
```

### 3. Initialization

Initialization is in oncreate function and the sequence cannot be wrong.
```
protected void onCreate(Bundle savedInstanceState) {
        super.setEnableVirtualButton(false);
        super.onCreate(savedInstanceState);

        //Initialization, the sequence cannot be wrong
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

