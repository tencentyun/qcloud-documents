## 1 概述
使用消息语音，需要先调用[基本API](https://cloud.tencent.com/document/product/556/7675)。

## 2 语音消息API调用流程
 
![](https://mc.qcloudimg.com/static/img/f3de36c0e998cb98d4085ede1879e65d/j3.jpg)

**流程说明**  
1.调用`SetMode`方法设置使用语音消息模式。  
2.调用`ApplyMessageKey()`获取语音消息安全密钥key信息，当申请成功后会通过`OnApplyMessageKeyComplete`进行回调。    
3.当需要录音时，调用`StartRecording()`录制音频到文件中（文件的路径格式是`/your path`）。  
4.如果想取消录制可以调用`StopRecording`接口进行取消。  
5.当录制完成后，调用`UploadRecordedFile()`将文件上传到`GcloudVoice`的服务器上，该过程会通过`OnUploadReccordFileComplete()`回调在上传成功的时候返还一个`ShareFileID`.该ID是这个文件的唯一标识符，用于其他用户收听时候的下载。服务器需要对其进行管理和转发。  
6.当游戏客户端需要收听其他人的录音时，首先从服务器获取转发的`ShareFileID`，然后调用`DownloadRecordedFile`下载该语言文件，下载结果通过`OnDownloadRecordFileComplete`回调来通知。当下载成功时，就可以调用`PlayRecordedFile`播放下载完成的语音数据了。同样的，如果想取消播放，可以调用`StopPlayFile`进行取消。

## 3 语音消息详细API

### 3.1 申请语音消息key
1.接口说明  

在语音消息的模式下，需要先申请许可才可以正常使用

2.函数原型

      GCloudVoiceErr ApplyMessageKey(int msTimeout)
    
  |参数|类型|意义|
  |--|--|--|
  |msTimeout|itn|超时时间，单位毫秒|
    
申请的结果通过delegate void ApplyMessageKeyCompleteHandler(GCloudVoiceCompleteCode code);进行回调  

3.示例代码

      m_voiceengine.OnApplyMessageKeyComplete += (IGCloudVoice.GCloudVoiceCompleteCode code) => {
      	Debug.Log ("OnApplyMessageKeyComplete c# callback");
      	s_strLog += "\r\n"+"OnApplyMessageKeyComplete ret="+code;
      	if (code == IGCloudVoice.GCloudVoiceCompleteCode.GV_ON_MESSAGE_KEY_APPLIED_SUCC) {
      		Debug.Log ("OnApplyMessageKeyComplete succ11");
      	} else {
      		Debug.Log ("OnApplyMessageKeyComplete error");
      	}
      };
4.出错处理

    GCLOUD_VOICE_PARAM_INVALID ： 传入的参数不对，比如超时范围5000ms-60000ms。
    GCLOUD_VOICE_NEED_INIT ： 需要先调用Init进行初始化
    GCLOUD_VOICE_AUTHKEY_ERR ： 请求Key的内部错误，此时需要联系GCloud团队，并提供日志进行定位
### 3.2 限制最大语音消息的长度
1.接口说明 
 
在语音消息的模式下，可以限制最大语音消息的长度，目前默认是2min，最大不超过2min。

2.函数原型

      GCloudVoiceErr SetMaxMessageLength(int msTime)
    
  |参数|类型|意义|
  |--|--|--|
  |msTimeout|itn|最大语音消息长度，单位毫秒|
3.示例代码

      int ret1 = m_voiceengine.SetMaxMessageLength (60000);
      Debug.Log ("SetMaxMessageLength ret==" + ret1);
4.出错处理

    GCLOUD_VOICE_NEED_INIT ： 需要先调用Init进行初始化
    GCLOUD_VOICE_PARAM_INVALID ： 传入的参数不对，时间范围1000ms-1000260ms。
### 3.3 开始录音
1.接口说明  

在语音消息的模式下，开始录音时，需要提供一个录音文件存储的地址路径

2.函数原型

      GCloudVoiceErr StartRecording(string filePath)
    
  |参数|类型|意义|
  |--|--|--|
  |filePath|string|录音文件存储的地址路径，路径中需要"/"作分隔，不能用"\"|
3.示例代码

      public void Click_btnStartRecord()
      {
      	Debug.Log("startrecord btn click, recordpath="+m_recordpath);
      	m_voiceengine.StartRecording (m_recordpath);
    
      }
4.出错处理

    GCLOUD_VOICE_NEED_INIT ： 需要先调用Init进行初始化
    GCLOUD_VOICE_MODE_STATE_ERR ： 当前模式不是离线语音模式
    GCLOUD_VOICE_PARAM_INVALID ： 传入的参数不对，路径为空。
    GCLOUD_VOICE_NEED_AUTHKEY ： 需要先调用GetAuthKey申请许可
    GCLOUD_VOICE_PATH_ACCESS_ERR ： 提供的路径不合法或者不可写
### 3.4 停止录音
1.接口说明  

在语音消息的模式下，调用停止录音接口会

2.函数原型

      GCloudVoiceErr StopRecording()
3.示例代码

      public void Click_btnStopRecord()
      {
      	Debug.Log("stoprecord btn click");
      	m_voiceengine.StopRecording ();
      }
4.出错处理

    GCLOUD_VOICE_NEED_INIT ： 需要先调用Init进行初始化
    GCLOUD_VOICE_MODE_STATE_ERR ： 当前模式不是离线语音模式
    GCLOUD_VOICE_NEED_AUTHKEY ： 需要先调用GetAuthKey申请许可
### 3.5 上传录音的文件
1.接口说明  

录音完成后，通过提供一个录音文件存储的地址路径，将已经录音完的文件进行上传

2.函数原型

      GCloudVoiceErr UploadRecordedFile(string filePath, int msTimeout)
    
  |参数|类型|意义|
  |--|--|--|
  |filePath|string|录音文件存储的地址路径，路径中需要"/"作分隔，不能用"\"|
  |msTimeout|int|上传文件超时时间|
  上传的结果通过delegate void UploadReccordFileCompletehandler(GCloudVoiceCompleteCode code, string filepath, string fileid)进行回调  

3.示例代码
    
      public void Click_btnUploadFile()
      {
      	int ret1 = m_voiceengine.UploadRecordedFile (m_recordpath, 60000);
      	Debug.Log ("Click_btnUploadFile file with ret==" + ret1);
      }
4.出错处理

    GCLOUD_VOICE_NEED_INIT ： 需要先调用Init进行初始化
    GCLOUD_VOICE_MODE_STATE_ERR ： 当前模式不是离线语音模式
    GCLOUD_VOICE_PARAM_INVALID ： 传入的参数不对，路径为空。
    GCLOUD_VOICE_NEED_AUTHKEY ： 需要先调用GetAuthKey申请许可
    GCLOUD_VOICE_PATH_ACCESS_ERR ： 提供的路径不合法或者不可读
    GCLOUD_VOICE_HTTP_BUSY ： 还在上一次上传或者下载中，需要等待后再尝试
### 3.6 下载录音的文件
1.接口说明  

录音完成后，通过提供一个录音文件存储的地址路径，将已经录音完的文件进行上传

2.函数原型
    
      GCloudVoiceErr DownloadRecordedFile(string fileID, string downloadFilePath, int msTimeout);
    
  |参数|类型|意义|
  |--|--|--|
  |fileID| string| 要下载文件的文件ID|
  |downloadFilePath|string|下载录音文件存储的地址路径，路径中需要"/"作分隔，不能用"\"|
  |msTimeout|int|下载文件超时时间|
 下载的结果通过delegate void DownloadRecordFileCompletehandler(GCloudVoiceCompleteCode code, string filepath, string fileid)进行回调   

3.示例代码
    
      public void Click_btnDownloadFile()
      {
      	int ret = m_voiceengine.DownloadRecordedFile (m_fileid, m_downloadpath, 60000);
      	s_strLog += "\r\n download file with ret=="+ret+" fileid="+m_fileid+" downpath"+m_downloadpath;
      }
4.出错处理
    
    GCLOUD_VOICE_NEED_INIT ： 需要先调用Init进行初始化
    GCLOUD_VOICE_MODE_STATE_ERR ： 当前模式不是离线语音模式
    GCLOUD_VOICE_PARAM_INVALID ： 传入的参数不对，路径为空。
    GCLOUD_VOICE_NEED_AUTHKEY ： 需要先调用GetAuthKey申请许可
    GCLOUD_VOICE_PATH_ACCESS_ERR ： 提供的路径不合法或者不可写或者不可读
    GCLOUD_VOICE_HTTP_BUSY ： 还在上一次上传或者下载中，需要等待后再尝试
### 3.7 开始播放下载的音频
1.接口说明    

下载下来的音频文件，需要调用相关接口进行播放

2.函数原型

      GCloudVoiceErr PlayRecordedFile (string downloadFilePath)
  |参数|类型|意义|
  |--|--|--|
  |filePath|string|下载文件存储的地址路径，路径中需要"/"作分隔，不能用"\"|
  
 如果正常播放完，会回调delegate void PlayRecordFilCompletehandler(GCloudVoiceCompleteCode code, string filepath)   

3.示例代码

      public void Click_btnPlayReocrdFile()
      {
    
      	int err;
      	if (m_ShareFileID == null) {
      		err = m_voiceengine.PlayRecordedFile(m_recordpath);
      		PrintLog ("downloadpath is nill, play local record file with ret=" + err);
      		return;
      	}
      	err = m_voiceengine.PlayRecordedFile(m_downloadpath);
      	PrintLog ("playrecord file with ret=" + err);
    
      	//m_voiceengine.PlayRecordedFile (m_downloadpath);
      }
4.出错处理

    GCLOUD_VOICE_NEED_INIT ： 需要先调用Init进行初始化
    GCLOUD_VOICE_MODE_STATE_ERR ： 当前模式不是离线语音模式
    GCLOUD_VOICE_PARAM_INVALID ： 传入的参数不对，路径为空。
    GCLOUD_VOICE_PATH_ACCESS_ERR ： 提供的路径不合法或者不可写
    GCLOUD_VOICE_SPEAKER_ERR : 打开麦克风失败
### 3.8 停止播放下载的音频
1.接口说明  

中断播放动作

2.函数原型

 ` GCloudVoiceErr StopPlayFile() `  

3.示例代码

      public void Click_btnStopPlayRecordFile()
      {
      	m_voiceengine.StopPlayFile ();
      }
4.出错处理

    GCLOUD_VOICE_NEED_INIT ： 需要先调用Init进行初始化
    GCLOUD_VOICE_MODE_STATE_ERR ： 当前模式不是离线语音模式
### 3.9 请求语音消息Key回调
1.接口说明  

请求语音消息许可的时候会回调

2.函数原型

      delegate void ApplyMessageKeyCompleteHandler(GCloudVoiceCompleteCode code)
      public abstract event ApplyMessageKeyCompleteHandler OnApplyMessageKeyComplete
    
  |参数|类型|意义|
  |--|--|--|
  |code|GCloudVoiceCompleteCode| 参见GCloudVoiceCompleteCode定义|
3.示例代码
    
      m_voiceengine.OnApplyMessageKeyComplete += (IGCloudVoice.GCloudVoiceCompleteCode code) => {
      	Debug.Log ("OnApplyMessageKeyComplete c# callback");
      	s_strLog += "\r\n"+"OnApplyMessageKeyComplete ret="+code;
      	if (code == IGCloudVoice.GCloudVoiceCompleteCode.GV_ON_MESSAGE_KEY_APPLIED_SUCC) {
      		Debug.Log ("OnApplyMessageKeyComplete succ11");
      	} else {
      		Debug.Log ("OnApplyMessageKeyComplete error");
      	}
      };
### 3.10 上传完成回调
1.接口说明  

上传语音文件后的结果通过这个进行回调

2.函数原型

      delegate void UploadReccordFileCompletehandler(GCloudVoiceCompleteCode code, string filepath, string fileid)
      public abstract event UploadReccordFileCompletehandler OnUploadReccordFileComplete
    
  |参数|类型|意义|
  |--|--|--|
  |code|GCloudVoiceCompleteCode|参见GCloudVoiceCompleteCode定义|
  |filepath|string| 上传的文件路径|
  |fileid|string|文件的id|
3.示例代码

      m_voiceengine.OnUploadReccordFileComplete += (IGCloudVoice.GCloudVoiceCompleteCode code, string filepath, string fileid) => {
      	Debug.Log ("OnUploadReccordFileComplete c# callback");
      	s_strLog += "\r\n"+" fileid len="+fileid.Length+"OnUploadReccordFileComplete ret="+code+" filepath:"+filepath+" fielid:"+fileid;
      	if (code == IGCloudVoice.GCloudVoiceCompleteCode.GV_ON_UPLOAD_RECORD_DONE) {
      		m_fileid = fileid;
      		s_strLog+="OnUploadReccordFileComplete succ, filepath:" +" fileid len="+fileid.Length+ filepath + " fileid:" + fileid+" fileid len="+fileid.Length;
      		Debug.Log ("OnUploadReccordFileComplete succ, filepath:" + filepath +" fileid len="+fileid.Length+ " fileid:" + fileid+" fileid len="+fileid.Length);
      	} else {
      		s_strLog+="OnUploadReccordFileComplete err, filepath:" + filepath + " fileid:" + fileid;
      		Debug.Log ("OnUploadReccordFileComplete error");
      	}
      };    
### 3.11 下载完成回调
1.接口说明  

下载语音文件后的结果通过这个进行回调

2.函数原型

      delegate void DownloadRecordFileCompletehandler(GCloudVoiceCompleteCode code, string filepath, string fileid)
      public abstract event DownloadRecordFileCompletehandler OnDownloadRecordFileComplete
    
  |参数|类型|意义|
  |--|--|--|
  |code|GCloudVoiceCompleteCode|参见GCloudVoiceCompleteCode定义|
  |filepath|string| 下载的路径|
  |fileid|string|文件的id|
3.示例代码

      m_voiceengine.OnDownloadRecordFileComplete += (IGCloudVoice.GCloudVoiceCompleteCode code, string filepath, string fileid) => {
      	Debug.Log ("OnDownloadRecordFileComplete c# callback");
      	s_strLog += "\r\n"+"OnDownloadRecordFileComplete ret="+code+" filepath:"+filepath+" fielid:"+fileid;
      	if (code == IGCloudVoice.GCloudVoiceCompleteCode.GV_ON_DOWNLOAD_RECORD_DONE) {
      		Debug.Log ("OnDownloadRecordFileComplete succ, filepath:" + filepath + " fileid:" + fileid);
      	} else {
      		Debug.Log ("OnDownloadRecordFileComplete error");
      	}
      };
### 3.12 正常播放完成后回调
1.接口说明  

如果用户没有暂停播放，语音文件已经播放完了，通过这个进行回调

2.函数原型

      delegate void PlayRecordFilCompletehandler(GCloudVoiceCompleteCode code, string filepath)
      public abstract event PlayRecordFilCompletehandler OnPlayRecordFilComplete;
    
  |参数|类型|意义|
  |--|--|--|
  |code|GCloudVoiceCompleteCode|参见GCloudVoiceCompleteCode定义|
  |filepath|string| 播放的文件路径|
3.示例代码

      m_voiceengine.OnPlayRecordFilComplete += (IGCloudVoice.GCloudVoiceCompleteCode code, string filepath) => {
      	Debug.Log ("OnPlayRecordFilComplete c# callback");
      	s_strLog += "\r\n"+"OnPlayRecordFilComplete ret="+code+" filepath:"+filepath;
      	if (code == IGCloudVoice.GCloudVoiceCompleteCode.GV_ON_PLAYFILE_DONE) {
      		Debug.Log ("OnPlayRecordFilComplete succ, filepath:" + filepath);
      	} else {
      		Debug.Log ("OnPlayRecordFilComplete error");
      	}
      };   
