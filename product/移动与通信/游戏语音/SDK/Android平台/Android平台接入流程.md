## 1 使用简述
GcloudVoice 客户端 SDK 可以运行在 iOS 和 Android 两个平台并支持 Cocos/Unreal/Unity 等主流游戏引擎。其在Cocos 和 Unreal 上提供 C++ 接口。本文档描述了 JAVA 接口使用方法（Android 也可以使用 C++ 接口）。

GcloudVoice 客户端 SDK 目前主要有实时语音(Real-Time)、离线语音(Message)两大功能。实时语音主要应用于游戏对局中的实时交流，如 MOBA 类游戏的实时指挥（王者荣耀、全民超神）、FPS类游戏的指挥（穿越火线-枪战王者）用于弥补手机上输入困难不实时的问题。离线语音主要用于留言消息场景，如大厅的全局聊天（三国之刃）、语音留言（邮件通知）。

同时实时语音还分为国战语音（比如 MMORGP 里面的国战，御龙国战）以及小队语音（MOBA 类里面的对局，王者荣耀的 5V5）,如果一个房间里面成员小于 20 人，建议使用小队语音，否则建议使用国战语音，在国战语音中，同时说话人数不得超过 5 人。

GcloudVoice 客户端 SDK 接口主要分成三个部分：基本 API、实时语音 API 以及离线语音 API。

### 1.1 系统配置和基本使用
[Android SDK 下载](https://cloud.tencent.com/document/product/556/10041)  
[Android Demo 下载](https://cloud.tencent.com/document/product/556/10042)  

下载 Android SDK 包后，导入 Jar 包和 SO 文件到 android 工程后。按如下流程即可接入。 主要是导入包
![](https://mc.qcloudimg.com/static/img/6f5adac586a22176e7f27155c2cb095f/1.png) 
然后通过    
![](https://mc.qcloudimg.com/static/img/fc862a3b8de404984c173d6d644fa33a/2.png)
初始化 java. 再完成初始化以及对应的模式设置  
![](https://mc.qcloudimg.com/static/img/ce293ff49f4cf57639f686fc8d6f451c/3.png)  
实现和设置回调： 导入回调接口：  
![](https://mc.qcloudimg.com/static/img/0c1626efd6ccaaf610fa75ee1cdb282c/4.png)
实现回调类：  
![](https://mc.qcloudimg.com/static/img/1396eee7c8ba16d27fcf55635308c317/5.png)  
设置回调：  
![](https://mc.qcloudimg.com/static/img/727f245bc232509203aed2b6013adee2/6.png)  
加入房间：  
![](https://mc.qcloudimg.com/static/img/ce985387539c27a80716ab2303f29148/7.png)  
在回调中查看进房的回调结果：  
![](https://mc.qcloudimg.com/static/img/785a9e54c6c0ec141a936fa5fd64deb8/8.png)  
成功后则可以 OpenMic OpenSpeaker：  
![](https://mc.qcloudimg.com/static/img/d5d36d5bd99d3c09695ef09b489d0e69/9.png)  
  
具体流程接口可以照以下文档的详细说明。

### 1.2 接口调用流程  
![](https://mc.qcloudimg.com/static/img/99e9bffb0f35d7d52d8775cfb47bc6ce/11.png)  
首先实现 IGCloudVoiceNotify 回调，然后调用 GetVoiceEngine 获取 IGCloudVoiceNotify 对象。然后对该对象进行初始化操作并设置回调。接着再根据需要调用实时语音接口或者离线语音接口，然后在系统可以 Tick 的地方（如 Unity3D 的 Update）调用 Poll 驱动处理事务中的回调信息。

### 1.3 实时语音接口调用流程  
![](https://mc.qcloudimg.com/static/img/b36200d498f8ce1c564f37c592bce125/12.png)  
在使用实时语音的时候，首先需要调用 SetMode 方法设置使用实时语音模式。然后根据业务逻辑判断是需要加入小队语音房间或者国战语音房间，分别调用 JoinTeamRoom 和 JoinNationalRoom。

然后需要 tick 的调用 poll 来检查回调，当加入房间成功或者失败时，会回调 OnJoinRoom 方法。

加入房间成功后就可以调用 OpenMic 打开麦克风进行采集并发送到网络，调用 OpenSpeaker 打开扬声器开始接受网络上的音频流并自动进行播放。

当需要退出房间时，调用 QuitRoom 即可，调用成功后会回调 OnQuitRoom 方法。

>**注意：** 
对于国战语音，系统要求说话人数不能超过 5 个人，每个用户多了一个角色信息，在加入房间的时候需要指定是以听众的身份加入还是以主播的身份加入。


### 1.4 离线语音接口调用流程  
![](https://mc.qcloudimg.com/static/img/5ff2e43e498ec6e8216b1a878cf501c3/13.png)  
在使用语音消息的时候，首先需要调用 SetMode 方法设置使用语音消息模式。然后调用 ApplyMessageKey 申请用于离线语音的相关的 key 信息，当申请成功后会通过 OnApplyMessageKey 进行回调。

当需要录音时，调用 StartRecording 接口将音频文件录制到文件中（文件的路径格式是file://your path）。如果想取消录制可以调用 StopRecording 接口进行取消。当录制完成后，调用 UploadRecordedFile 将文件上传到 GcloudVoice 的服务器上，该过程会通过 OnUploadFile 回调在上传成功的时候返还一个 ShareFileID.该 ID 是这个文件的唯一标识符，用于其他用户收听时候的下载。服务器需要对其进行管理和转发

当游戏客户端需要收听其他人的录音时，首先从服务器获取转发的 ShareFileID，然后调用 DownloadRecordedFile 下载该语言文件，下载结果通过 OnDownloadFile 回调来通知。当下载成功时，就可以调用 PlayRecordedFile 播放下载完成的语音数据了。同样的，如果想取消播放，可以调用 StopPlayFile 进行取消。


## 2 接口说明
### 2.1 基本 API
#### 2.1.1 获取 IGcloudVoiceEngine 对象  
 接口：IGCloudVoiceEngine *GetVoiceEngine()   
 参数：无   
 返回值：IGcloudVoiceEngine对象,出错时返回NULL  

#### 2.1.2 设置应用信息

接口：GCloudVoiceErrno SetAppInfo(const char appID,const char appKey, const char *openID)   
参数： appID : 应用的GameID appKey: 应用的GameKey openID: 游戏从QQ、微信等获得到的openID，也可以是游戏侧能标示的唯一玩家的角色ID   
返回值：成功时返回GcloudVoiceErrno::GCLOUD_VOICE_SUCC,否则返回其他错误码


#### 2.1.3 设置应用信息初始化  
接口：GcloudVoiceErrno Init()   
返回值：成功时返回GcloudVoiceErrno::GCLOUD_VOICE_SUCC,否则返回其他错误码

#### 2.1.4 反初始化 
接口： GcloudVoiceErrno Deinit()   
参数：无   
返回值：成功时返回GcloudVoiceErrno::GCLOUD_VOICE_SUCC,否则返回其他错误码

#### 2.1.5 反初始化   
接口： GCloudVoiceErrno SetNotify(IGCloudVoiceNotify *notify)   
参数：notify: 实现的IGCloudVoiceNotify对象   
返回值：成功时返回GcloudVoiceErrno::GCLOUD_VOICE_SUCC,否则返回其他错误码

#### 2.1.6 设置通话模式 
接口：GcloudVoiceErrno SetMode(GcloudVoiceMode mode)   
参数：mode： 通话模式 enum GcloudVoiceMode  

    {
     RealTime,  // 实时语音
     Messages, // 离线语音
    };
     
返回值：成功时返回 GcloudVoiceErrno::GCLOUD_VOICE_SUCC,否则返回其他错误码

#### 2.1.7 系统 Pause 中断 
接口：GcloudVoiceErrno Pause()  
参数：无   
返回值：成功时返回GcloudVoiceErrno::GCLOUD_VOICE_SUCC,否则返回其他错误码  

#### 2.1.8 中断恢复Resume 
接口：GcloudVoiceErrno Resume()   
参数： 无   
返回值：成功时返回GcloudVoiceErrno::GCLOUD_VOICE_SUCC,否则返回其他错误码  

#### 2.1.9 回调驱动Poll 
接口：GcloudVoiceErrno Poll()   
参数：无   
返回值：成功时返回GcloudVoiceErrno::GCLOUD_VOICE_SUCC,否则返回其他错误码  

### 2.2 实时语音 API
#### 2.2.1 加入小队房间 
接口：GcloudVoiceErrno JoinTeamRoom(const char *roomName, int msTimeout)   
参数： roomName: 服务器获得的房间的名称，如果不存在服务器会自动创建，长度限制在511以下。 msTimeout: 加入房间的超时时间   
返回值：成功时返回GcloudVoiceErrno::GCLOUD_VOICE_SUCC,否则返回其他错误码。这里返回成功不一定标示加入房间已经成功，加入房间是否成功会在OnJoinRoom中回调

#### 2.2.2 国战房间 
接口：GcloudVoiceErrno JoinNationalRoom(const char *roomName, GCloudVoiceMemberRole role, int msTimeout)   
参数： roomName: 服务器获得的房间的名称，如果不存在服务器会自动创建 role: 用户的角色，是听众还是主播 msTimeout: 加入房间的超时时间   
返回值：成功时返回GcloudVoiceErrno::GCLOUD_VOICE_SUCC,否则返回其他错误码。这里返回成功不一定标示加入房间已经成功，加入房间是否成功会在OnJoinRoom中回调

#### 2.2.3 退出房间 
接口：GcloudVoiceErrno QuitRoom()   
参数：无   
返回值：成功时返回GcloudVoiceErrno::GCLOUD_VOICE_SUCC,否则返回其他错误码。当前加入的是那种房间（小队或者国战）就退出哪个房间

#### 2.2.4 打开麦克风开始录音 
接口：GcloudVoiceErrno OpenMic()   
参数：无   
返回值：成功时返回GcloudVoiceErrno::GCLOUD_VOICE_SUCC,否则返回其他错误码

#### 2.2.5 关闭麦克风，停止录音 
接口：GcloudVoiceErrno CloseMic()   
参数：无   
返回值：成功时返回GcloudVoiceErrno::GCLOUD_VOICE_SUCC,否则返回其他错误码

#### 2.2.6 打开扬声器开始播放声音 
接口：GcloudVoiceErrno OpenSpeaker()   
参数：无   
返回值：成功时返回GcloudVoiceErrno::GCLOUD_VOICE_SUCC,否则返回其他错误码

#### 2.2.7 关闭扬声器停止播放声音 
接口：GcloudVoiceErrno CloseSpeaker()    
参数：无   
返回值：成功时返回GcloudVoiceErrno::GCLOUD_VOICE_SUCC,否则返回其他错误码

### 2.3 离线语音 API  
### 2.3.1  申请 AuthKey    
接口：GCloudVoiceErrno ApplyMessageKey(int msTimeout)   
参数：msTimeout超时时间   
返回值：成功时返回GcloudVoiceErrno::GCLOUD_VOICE_SUCC,否则返回其他错误码。这里成功不代表已经成功申请了香港key，需要在OnApplyMessageKey中回调  

### 2.3.2 开始录音 
接口：GcloudVoiceErrno StartRecording (const char * filePath)   
参数：filePath:保存文件的位置，格式为 保存至文件”you_dir/your_filename” ：文件路径需要用反斜杠“/”做分隔   
返回值：成功时返回GcloudVoiceErrno::GCLOUD_VOICE_SUCC,否则返回其他错误码  

### 2.3.3 取消录音 
接口：GcloudVoiceErrno StopRecording ()   
参数：无  
返回值：成功时返回GcloudVoiceErrno::GCLOUD_VOICE_SUCC,否则返回其他错误码  

### 2.3.4 发送音频文件 
接口：GcloudVoiceErrno UploadRecordedFile (const char * filePath)   
参数：filePath：为录制时给的路径   
返回值：成功时返回GcloudVoiceErrno::GCLOUD_VOICE_SUCC,否则返回其他错误码  

### 2.3.5 下载音频文件 
接口：GcloudVoiceErrno DownloadRecordedFile (const char fileID, const char downloadFilePath, int msTimeout)     
参数： fileID： 要下载的文件的ID downloadFilePath: 下载的位置，格式如上 msTimeout: 超时时间     
返回值：成功时返回GcloudVoiceErrno::GCLOUD_VOICE_SUCC,否则返回其他错误码  

### 2.3.6 播放下载的音频文件 
GcloudVoiceErrno PlayRecordedFile (const char * downloadFilePath)   
参数：downloadFilePath： 下载的文件的位置   
返回值：成功时返回GcloudVoiceErrno::GCLOUD_VOICE_SUCC,否则返回其他错误码  

### 2.3.7 取消播放 
接口：GcloudVoiceErrno StopPlayFile ()     
参数：无     
返回值：成功时返回GcloudVoiceErrno::GCLOUD_VOICE_SUCC,否则返回其他错误码    

## 2.4 回调接口  

### 2.4.1 加入房间结果 
接口：void OnJoinRoom(GCloudVoiceCompleteCode code, char *roomName, int memberID)    
参数：code: 加入房间的结果 enum GcloudVoiceCompleteCode  
  {
      GV_ON_JOINROOM_SUCC,         // 加入房间成功
      GV_ON_JOINROOM_TIMEOUT,    // 加入房间超时
      GV_ON_JOINROOM_FAIL,        // 加入房间其他错误
  };
roomName: 加入房间的名字 memberID： 成员的ID  
返回值：无  

### 2.4.2 退出房间结果 
接口：void OnQuitRoom(GCloudVoiceCompleteCode code, const char *roomName)   
参数：code: 加入房间的结果 enum GcloudVoiceCompleteCode

  {
      GV_ON_JOINROOM_SUCC,         // 加入房间成功
      GV_ON_JOINROOM_TIMEOUT,    // 加入房间超时
      GV_ON_JOINROOM_FAIL,        // 加入房间其他错误
  };
roomName: 加入房间的名字   
返回值：无

### 2.4.3 其他成员发声状态的变化 
接口：void OnMemberVoice (const int members, int length)   
参数：members: 成员及状态，格式为 memberID,status,memberID,status 成对出现，status值为 0：从发声变成 没有发声 1： 从不发生变成发声 2： 从发声再发声 length: member的个数，2就是member数组的长度。   
返回值：无

### 2.4.4 发送文件状态回调 
接口：void OnUploadFile(GCloudVoiceCompleteCode code, const char filePath, const char fileID)   
参数： filePath： 文件存储的位置，与send的时候一致 fileID： 文件唯一标示的ID code: 如果出错时候的错误码   
返回值：无

### 2.4.5 下载文件状态回调 
接口：void OnDownloadFile(GCloudVoiceCompleteCode code, const char filePath, const char fileID  )   
参数： filePath： 文件存储的位置，与down的时候一致 fileID： 文件唯一标示的ID code: 如果出错时候的错误码   
返回值：无  

### 2.4.6 申请Key的回调   
接口：void OnApplyMessageKey(GCloudVoiceCompleteCode code)   
参数：code: 如果出错时候的错误码   
返回值：无  

### 2.4.7 文件播放结束后的回调   
接口：void OnPlayRecordedFile(GCloudVoiceCompleteCode code,const char *filePath)    
参数： code: 如果出错时候的错误码 filePath: 播放的文件的位置   
返回值：无  


