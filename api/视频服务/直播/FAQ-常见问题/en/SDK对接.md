
### 1. How do I export logs output by the SDK?
Logs can help a lot for troubleshooting of push and playing. It is suggested to set the log level to DEBUG in the debugging or test phase. By this level, logs are collected most comprehensively. See below for levels of logs:
![](//mccdn.qcloud.com/static/img/cfe3402e5f9f4bef1f900db2a967e3be/image.png)
You can call the **setLogLevel** API in TXLivePlayer or TxLivePush to set the log level.
For Android devices, logs are stored under "/sdcard/txRtmpLog". You can run the abd command to view and export log files:
![](//mccdn.qcloud.com/static/img/1a38cf482394d8e6ab678d44c4059a63/image.png)
For iPhones, logs are stored in the "Documents" directory. You can use iTools to export log files:
![](//mccdn.qcloud.com/static/img/38ef348f3623dcea65cc4f5a8529dacf/image.png)

### 2. What do I do when a naming conflict occurs (duplicate symbol)?
If a process contains functions with the same name, which will be compiled into symbols, the linker will not be able to recognize them.

If your App uses players like ffplay, please try remove it. Tencent Cloud uses open source modules like ffmpeg to implement the coding/decoding of H.264 video streams. If your project already contains the these open source modules, the duplicate symbol will occur.

If duplicate symbol is caused by other modules, please contact us to rename our functions.
![txc_rtmp_sdk_duplicated_symbol](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/txc_rtmp_sdk_duplicated_symbol.jpg)

### 3. I encountered the ffmpeg conflict but don't want to remove it from my project.
If you've packed ffmpeg in your App, and don't want to remove it, please try the following:
1. Ensure that ffmpeg in your project is updated to the latest version (3.0.2).
2. Check "Other Linker Flags" in the Xcode project. Remove **-all_load** if it exists.

In this way, your App is linked to two ffmpeg libraries. But Xcode linker cannot judge the accurate calling relationship between these two libraries. The calling relationship between these two ffmpeg libraries inside the APP is uncontrollable (functions of the two libraries may be called in an interlaced manner).

Therefore, <font color='red'>if the two ffmpeg libraries are in different versions, you may encounter many crashes. </font>If you check in the stack, these crashes generally occur in internal functions of the ffmpeg library.

### 4. What do I do if a program crash occurs in the Android OS (CRASH)?
- **Obfuscated Code**
  **DO NOT create obfuscated codes for files in the com.tencent**. As the files are packaged using JNI, obfuscation can cause Java fails to locate the expected API function.

- **Project Configuration Error**
  In some cases, you may see the following error, which means that Java is trying to find the getSDKVersion jni function, but it's not implemented. This is because the "so" used to implement this function is not loaded by your project. 
```java
java.lang.UnsatisfiedLinkError: No implementation found for 
int[] com.tencent.rtmp.TXRtmpApi.getSDKVersion() 
(tried Java_com_tencent_rtmp_TXRtmpApi_getSDKVersion and Java_com_tencent_rtmp_TXRtmpApi_getSDKVersion)
```
 
- **Codec conflict**
  If you've integrated multiple players in your App, it may cause codec library conflicts as these players may use the same open source components. You can try block other players to solve this problem.


### 5. What do I do if iOS fails to find function definitions (undefined symbols  )?
This is usually caused by improper project configurations. Please check the instruction architectures (armv7, arm64, and x86 simulator) and the configuration of "Link Binary With Libraries". See below for required libraries of Tencent Cloud SDK:
![txc_rtmp_sdk_link_lib](//mccdn.qcloud.com/static/img/6605e78efb384799b9b4e1c6a5a7aac6/image.jpg)
If the following error occurs:
![](//mccdn.qcloud.com/static/img/8424405ffd2e666c481c1792d8296172/image.jpg)
Check the C++ library configuration of the project:
![](//mccdn.qcloud.com/static/img/07665b7aa7f6495417bb8e2f850f3afa/image.jpg)

### 6. What do I do if a view rendering exception occurs (OpenGL ES Conflict)?
After integrated with Video Cloud SDKs, the App UI rendering is abnormal (the App project uses Cocos2d or OpenGL ES).
- **Reason 1**:
>Both Cocos2D and Video Cloud SDK use OpenGL ES, which calls [EAGLContext setCurrentContext] method.
>
>When Video Cloud SDK is activated, [EAGLContext setCurrentContext] is called. If another module in the App continuously calls this method at the same time, the OpenGL context environment becomes abnormal.
>
>To solve this problem, before the push and play, call [[CCDirectorCaller sharedDirectorCaller] stopMainLoop] to stop the rendering of Cocos2D. And call [[CCDirectorCaller sharedDirectorCaller] startMainLoop] to resume rendering when the push and playing end.

- **Reason 2**:
>Your App does not use Cocos2D but use OpenGL ES. In this case, the iOS console prints "Warning: currentContext != [[AVGLShareInstance shareInstance] context]". This is because Tencent video cloud SDK detects that context of EAGLContext is tampered by other modules, which indicates that other modules in the APP are also calling OpenGL. It is unnecessary to render two OpenGL Views simultaneously.
>
>To solve this problem, please adjust logics in your App to avoid simultaneous running of rendering logic of Video Cloud SDK and the your OpenGL ES logic.
