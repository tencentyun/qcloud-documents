### How to solve the problem of timeout that occurs when I join a room?
This may be caused by the following reasons. Solve the problem accordingly:
1. Game Key does not match game ID.
2. The service is not activated at GCloud official website.
3. Network is not connected.
4. In testing environment, DAU exceeds the limit of 100.

### On Editor and PC, what if x86 can be canceled but dll cannot be found when cancelling x86_64?
Configure x86 for x86 and x64 for x64. Unity 64-bit locates dll 64-bit by default, which cannot be canceled, otherwise "dllnotfound" is returned when Editor runs.

### Why does the volume of game background music decrease after the microphone is enabled?
This is normal. To eliminate echoes and optimize the experience of real-time communication, you may enter VoIP chat mode after the microphone is enabled, thus the volume of game background music decreases.

### What if Android OpenMic is failed or `GCLOUD_VOICE_INTERNAL_TVE_ERR = 0x5001, //20481, internal TVE err, our used` and `GCLOUD_VOICE_PERMISSION_MIC_ERR = 0x3003, //12291, you have not right to access micphone in android` are returned?
1. Confirm whether "init" method of GCloudVoiceEngine is called in Java, as shown below:
![](//mc.qcloudimg.com/static/img/6659545095ee63582ba1490195c7c60b/image.png)
2. Confirm the version of android.support.v4.jar. Since the related function is used in the voice engine to check the permission of microphone, you have to make sure the version of jar package is higher than 6.0, otherwise the error code `GCLOUD_VOICE_PERMISSION_MIC_ERR` may be returned when the microphone is enabled on Android 6.0.

### Why am I prompted that the implementation of function in SDK cannot be found and prompted of x86 when Xcode is connected?
Xcode emulator cannot be used for debugging in SDK. You need to plug it into a physical device or choose **Generic iOS Device**.

### Why does the error `cant find library` occur on some older generations of Android phones?
"System.loadLibrary("GCloudVoice")" needs to be performed in ApplicationAvtivity. Sample codes are as follows:
```
static {
            try {
                 System.loadLibrary("GCloudVoice");
       } catch (UnsatisfiedLinkError e) {
              System.err.println("load library failed!!!");
       }
     }
```

### Why does the log `Cant find method ApolloVoiceUUID` appear on Android phones?
Check whether the jar package and `.so` file of SDK are downloaded from the same version of system.

### Why does an exceptional log `Can't Read config files` appear on Android phones?
For Android, check whether the Assets directory is added normally. For iOS, check whether the Bundle file is added to Xcode project.

### Is the voice feature affected if AudioSession is modified by users?
Yes. AudioSession is a single instance of App, so the feature may be affected.

### How to carry out the second step of connection of Unity in the document: modify Java files?
Choose one of the following two solutions:
- Export an Android project from Unity, and modify the Java code in it.
- According to the format of Unity plug-in, place an ApplicationActiviy class integrated with UnityPlayerActivity under Plugins/Android directory, and modify Java code in it.

### What if an error `dumplicate symbol * in: /libGCloudVoice.a(.o)` on iOS connection is returned?
Do not use all_load for "other link flag" in project settings. If it is needed in other libraries, use force_load to connect relevant libraries.

### Why does iOS crash after being connected?
For iOS 10.0 or above, the permission of "Privacy - Microphone Useage DescriptioniOS" needs to be added in the project "Info.plist". If it is connected to a static library where functions may have the same name as those in related voice components, an error may occur when they are called. Therefore, it is recommended to check whether the components connected previously have been deleted during the process of connection. 

### Why can't two users in the same room hear each other?
1. Confirm whether they join the same room.
2. Confirm whether the microphone is enabled for the speaker and the speaker is enabled for the listener.
3. Check whether two users who join the same room use the same OpenId (set in SetAppInfo)? Make sure that users who join the same room have different OpenId.

### What if the upload of recording is failed?
Check the logs. If the length of file is 0, check whether the specified path exists, and make sure the directory has been created. The path should be specific to file name, such as `/sdcard/com.qq.gcloud/voice/11.dat`.

### What if I join the room successfully through Unity and call the Poll on iOS, but cannot receive callback message?
This problem occurs on Unity5.5 due to Poll failure caused by the changes of Unity5.5 platform. You can directly upgrade GVoice to the newest version.

### Why is callback message not received after functions such as JoinRoom, QuitRoom, ApplyMessageKey are called?
Check whether Poll function is called continuously to help obtain the callback message.

### Why does an error occur when DownloadRecordFile is called and why does `response status = 400 Bad Request` appear in log?
It is probably because the passed FileID is invalid. Verify using a valid FileID encoded with HardCode.

### Why does the error DLlNotFound occur when I directly run Unity Editor in Mac.
You are not allowed to run Unity Editor in Mac directly for debugging, but instead you can use Unity Editor in Windows.

### What if the error DllNotFound occurs when I run Unity Editor in Windows for debugging?
Check whether x86 and x86_64 files are added in the directory of Unity project, whether dll file is in it, and whether the dll file is configured as follows:
![dll1](//mc.qcloudimg.com/static/img/dada03674e32bf003258554e823f6bb2/image.png)
![dll2](//mc.qcloudimg.com/static/img/c6719cb0b45017f3d7e4e4792b279cb7/image.png)

### What if the error `findclass error` occurs when program crashes?
Decompile the Apk to determine GCloudVoice.jar has been compiled in it.

### How to deal with the error of iOS compilation?
Check whether a link system library exists:
![Link System Library](//mc.qcloudimg.com/static/img/9d9364f9ef6a78d4e35f835386bf32d1/image.png)

### Why does iOS crash after being connected?
For iOS 10.0 or above, the permission of "Privacy - Microphone Useage DescriptioniOS" needs to be added in the project "Info.plist". If it is connected to a static library where functions may have the same name as those in related voice components, an error may occur when they are called. Therefore, it is recommended to check whether the components connected previously have been deleted during the process of connection.
![Access Plug-in 1](//mc.qcloudimg.com/static/img/3b1950068bf4a896e8efe1a48af031ff/image.png)
![Access Plug-in 2](//mc.qcloudimg.com/static/img/c85deea010d529b2822e4ed5f6baca38/image.png)

### `GV_ON_STT_APIERR` is returned through callback when SpeechToText is called
1. Make sure the translated recording file was recorded under SetMode(GCloudVoiceMode.Translation) mode.
2. If the error still exists, export the log and send it to us to locate the problem.

### The screenshot of the problem `libGCloudVoice.so not found` is taken as follows, how to solve it? 
![](//mc.qcloudimg.com/static/img/f3a3acc3af2fd85cd4a06a8f73e992ba/image.png)
1. Add "system.loadlibrary" into Activity before "libMyGame.so" is loaded. The code is as follows:
```
static {
    System.loadLibrary("GCloudVoice");
    }
```

### Why does the error `no such file or direcory` occur?
The error `no such file or direcory:xxxxx` means that no related file exists or related file is missing. Check whether the path of a related file is correct.

### The length of time obtained using `gcloud_voice.GCloudVoiceEngine.GetFileParam` is 0 when Unity is compiled with il2cpp, why is that?
It may be caused by the following 3 reasons:
1. You are not authorized to access Microphone
2. No record permission in Androidmanifest.xml
3. Incorrect path

### What if recording is failed or microphone cannot be enabled?
Make sure to enable these two permissions: MODIFY_AUDIO_SETTINGS and RECORD_AUDIO

### What does the error code 200 returned for OpenMic mean?
The microphone is not enabled

### What is applymessagekey timeout error?
When applymessagekey timeout error occurs, first check whether the voice service is enabled for the configured APPID and Key. If it is enabled but the error still exits, check whether the network is running normally.

