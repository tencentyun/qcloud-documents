## Common problems of connecting to SDK
### 1. iOS compilation errors
Check whether it is connected to system libraries  
![](https://mc.qcloudimg.com/static/img/a6b6942b66e94582145b89b224ce6f5f/faq.jpg)

### 2. Android OpenMic failure

(1) Check whether the `init` method of `GCloudVoiceEngine` is called in Java. 
![](https://mc.qcloudimg.com/static/img/bdea05411bb37424592d69a76dc595e7/dc8f3e667738b047bf2cf777f5d209a4.jpg)
(2) Make sure you're using android.support.v6.jar and later. The voice engine of GVoice uses functions are used in voice engine to check the permission of microphone, bove 6.0. Otherwise `GCLOUD_VOICE_PERMISSION_MIC_ERR` will be returned if microphone is opened via Android 6.0.
### 3. I call `SpeechToText`, but get `GV_ON_STT_APIERR`

(1) Make sure that the file is recorded with the mode `ofSetMode(GCloudVoiceMode.Translation)`.

(2) If the errors persists, please send us the log. We'll look into it ASAP.

### 4. No callbacks after calling `JoinRoom`, `QuitRoom` and `ApplyMessageKey` 

Check whether `Poll` is constantly called. This function is used to drive obtaining of callback information

### 5. Get time length of recorded files

You can obtain it via `GetFileParam` API. See below for C# :

    int [] bytes = new int[1];
    bytes [0] = 0;
    float [] seconds = new float[1];
    seconds [0] = 0;
    m_voiceengine.GetFileParam (m_recordpath, bytes, seconds);
### 6. Players in the same room cannot hear from each other

(1) Check whether the two players are really in the same room.

(2) Make sure that the speaker has opened the microphone and the listener has opened the speaker.

(3) Check whether the two players enter the same room with the same OpenID (set in `SetAppInfo`). Players in the same room should have different OpenID.

### 7. `DownloadRecordFile` error, `response status = 400 Bad Request` appears in log.

It may be caused by invalid FileID. Please hardcode a valid fileid to check.

