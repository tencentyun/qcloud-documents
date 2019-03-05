## 接入SDK常见问题
### 1. ios编译错误
查看是否有链接系统库：  
![](https://mc.qcloudimg.com/static/img/a6b6942b66e94582145b89b224ce6f5f/faq.jpg)

### 2. Android OpenMic失败

(1)看下java中有没调用GCloudVoiceEngine的init方法，如下图所示： 
![](https://mc.qcloudimg.com/static/img/bdea05411bb37424592d69a76dc595e7/dc8f3e667738b047bf2cf777f5d209a4.jpg)
(2)确认下android.support.v4.jar的版本，因为语音引擎中使用了相关函数检查麦克风权限，因此需要确保该jar包版本在6.0以上，否则，在Android 6.0上开麦克风会返回GCLOUD_VOICE_PERMISSION_MIC_ERR失败码。
### 3. 调用SpeechToText，回调返回GV_ON_STT_APIERR结果

(1)请确认翻译的录音文件是在SetMode(GCloudVoiceMode.Translation)模式下录制的。

(2)若还是返回错误，请取下log联系并发送给我们定位问题。

### 4. 调用JoinRoom、QuitRoom、ApplyMessageKey等相关函数后，没有回调

检查是否有持续调用Poll函数，来驱动获取回调消息。

### 5. 获取录音文件时长方法

通过GetFileParam接口来获取 C#用法如下：

    int [] bytes = new int[1];
    bytes [0] = 0;
    float [] seconds = new float[1];
    seconds [0] = 0;
    m_voiceengine.GetFileParam (m_recordpath, bytes, seconds);
### 6. 两人加入同一房间后听不到对方说话

(1)确认两人加入的是同一个房间。

(2)确认说话方打开了麦克风和收听方打开了扬声器。

(3)两个加入同一房间是否用了同样的OpenId(在SetAppInfo中设置），请确保进入同一房间的用户具有不同的OpenId。

### 7. DownloadRecordFile出错， log出现response status = 400 Bad Request

很大可能是你传入的FileID非法，可通过HardCode一个合法的fileid来验证。

