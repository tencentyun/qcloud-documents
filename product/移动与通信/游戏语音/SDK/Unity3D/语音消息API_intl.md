## 1 Overview
To use Voice Messages, you need to call [Basic APIs](https://cloud.tencent.com/document/product/556/7675).

## 2 Call APIs for Voice Message 
 
![](https://mc.qcloudimg.com/static/img/f3de36c0e998cb98d4085ede1879e65d/j3.jpg)

**How-To**  
1.Call `SetMode()` to enable Voice Message mode.   
2.Call ApplyMessageKey() to obtain security key information of voice message, and callback may be conducted via "OnApplyMessageKeyComplete" after successful application.   
3.Call `StartRecording()` to start recording and save the recorded file to `/your path`.  
4.Call `StopRecording` to cancel recording  
5.After recording, call `UploadRecordedFile()` to upload the file to   `GcloudVoice` server.This process is called back via `OnUploadReccordFileComplete()`.For successful uploading, `ShareFileID` will be returned.This is the unique ID of this file.Others can download and listen to this file via this ID.The server will manage and forward this ID.   
6.To play voice messages from others on the game client, please first obtain `ShareFileID` transferred from server and then call `DownloadRecordedFile` to download the recorded file.The result of downloading will be returned by callback of `OnDownloadRecordFileComplete`.When downloading succeeds, call `PlayRecordedFile` to play the file.Call `StopPlayFile` to cancel playing if necessary.  

## 3 APIs for Voice Message

### 3.1 Apply for Voice Message Key
1.API Description  

For Voice Message mode, call this API to apply for permission first

2.Function Prototype

      GCloudVoiceErr ApplyMessageKey(int msTimeout)
    
  |Parameter|Type|Meaning|
  |--|--|--|
  |msTimeout|int|Timeout setting (unit:ms)
    
The request result is called back via delegate void ApplyMessageKeyCompleteHandler(GCloudVoiceCompleteCode code). 

3.Sample Code

      m_voiceengine.OnApplyMessageKeyComplete += (IGCloudVoice.GCloudVoiceCompleteCode code) => {
      	Debug.Log ("OnApplyMessageKeyComplete c# callback");
      	s_strLog += "\r\n"+"OnApplyMessageKeyComplete ret="+code;
      	if (code == IGCloudVoice.GCloudVoiceCompleteCode.GV_ON_MESSAGE_KEY_APPLIED_SUCC) {
      		Debug.Log ("OnApplyMessageKeyComplete succ11");
      	} else {
      		Debug.Log ("OnApplyMessageKeyComplete error");
      	}
      };
4.Error Codes

    GCLOUD_VOICE_PARAM_INVALID: Parameters transferred in are incorrect, such as timeout of 5000ms-60000ms
    GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization
    GCLOUD_VOICE_AUTHKEY_ERR: Apply for internal errors of Key.Now it is necessary to contact GCloud team and provide log for positioning.
### 3.2.Set the max length of a voice message
1.API Description 
 
For Voice Message mode, call this API to set the max length of voice message (up to 2 min)

2.Function Prototype

      GCloudVoiceErr SetMaxMessageLength(int msTime)
    
  |Parameter|Type|Meaning|
  |--|--|--|
  |msTimeout|itn|Maximum length of voice message (unit: ms)|
3.Sample Code

      int ret1 = m_voiceengine.SetMaxMessageLength (60000);
      Debug.Log ("SetMaxMessageLength ret==" + ret1);
4.Error Codes

    GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization
    GCLOUD_VOICE_PARAM_INVALID: Parameters transferred in are incorrect, such as time period of 1000ms-1000260ms
### 3.3 Start Recording
1.API Description  

For Voice Message mode, call this API to specify a storage path for the recorded file while starting recording.

2.Function Prototype

      GCloudVoiceErr StartRecording(string filePath)
    
  |Parameter|Type|Meaning|
  |--|--|--|
  |filePath|string| Storage path of recorded files (separated by "/" but not "\"
3.Sample Code

      public void Click_btnStartRecord()
      {
      	Debug.Log("startrecord btn click, recordpath="+m_recordpath);
      	m_voiceengine.StartRecording (m_recordpath);
    
      }
4.Error Codes

    GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization
    GCLOUD_VOICE_MODE_STATE_ERR: Not in Voice Message mode
    GCLOUD_VOICE_PARAM_INVALID: Parameters transferred are incorrect, and the path is empty.
    GCLOUD_VOICE_NEED_AUTHKEY: Need to call `GetAuthKey` first to get permission
    GCLOUD_VOICE_PATH_ACCESS_ERR : The path provided is invalid or not writable
### 3.4 Stop Recording
1.API Description  

For Voice Message mode, call this API to stop recording

2.Function Prototype

      GCloudVoiceErr StopRecording()
3.Sample Code

      public void Click_btnStopRecord()
      {
      	Debug.Log("stoprecord btn click");
      	m_voiceengine.StopRecording ();
      }
4.Error Codes

    GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization
    GCLOUD_VOICE_MODE_STATE_ERR: Not in Voice Message mode
    GCLOUD_VOICE_NEED_AUTHKEY: Need to call `GetAuthKey` first to get permission
### 3.5 Upload the Recorded File
1.API Description  

After recording, call this API to upload the recorded file to the specified storage path.

2.Function Prototype

      GCloudVoiceErr UploadRecordedFile(string filePath, int msTimeout)
    
  |Parameter|Type|Meaning|
  |--|--|--|
  |filePath|string| Storage path of recorded files (separated by "/" but not "\"
  |msTimeout|int|File uploading timed out
  The uploading result is called back via `delegate void UploadReccordFileCompletehandler(GCloudVoiceCompleteCode code, string filepath, string fileid)`. 

3.Sample Code
    
      public void Click_btnUploadFile()
      {
      	int ret1 = m_voiceengine.UploadRecordedFile (m_recordpath, 60000);
      	Debug.Log ("Click_btnUploadFile file with ret==" + ret1);
      }
4.Error Codes

    GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization
    GCLOUD_VOICE_MODE_STATE_ERR: Not in Voice Message mode
    GCLOUD_VOICE_PARAM_INVALID: Parameters transferred are incorrect, and the path is empty.
    GCLOUD_VOICE_NEED_AUTHKEY: Need to call `GetAuthKey` first to get permission
    GCLOUD_VOICE_PATH_ACCESS_ERR : The path provided is invalid or cannot be read.
    GCLOUD_VOICE_HTTP_BUSY: Last uploading or downloading is still ongoing, please retry later.
### 3.6 Download the recorded file
1.API Description  

After recording, call this API to upload the recorded file to the specified storage path.

2.Function Prototype
    
      GCloudVoiceErr DownloadRecordedFile(string fileID, string downloadFilePath, int msTimeout);
    
  |Parameter|Type|Meaning|
  |--|--|--|
  |fileID| string| ID of files to be downloaded
  |downloadFilePath|string|Storage path of downloaded recording files (separated by "/" but not "\")
  |msTimeout|int|File downloading timed out
 The downloading result is called back via delegate void DownloadRecordFileCompletehandler(GCloudVoiceCompleteCode code, string filepath, string fileid).  

3.Sample Code
    
      public void Click_btnDownloadFile()
      {
      	int ret = m_voiceengine.DownloadRecordedFile (m_fileid, m_downloadpath, 60000);
      	s_strLog += "\r\n download file with ret=="+ret+" fileid="+m_fileid+" downpath"+m_downloadpath;
      }
4.Error Codes
    
    GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization
    GCLOUD_VOICE_MODE_STATE_ERR: Not in Voice Message mode
    GCLOUD_VOICE_PARAM_INVALID: Parameters transferred are incorrect, and the path is empty.
    GCLOUD_VOICE_NEED_AUTHKEY: Need to call `GetAuthKey` first to get permission
    GCLOUD_VOICE_PATH_ACCESS_ERR : The path provided is invalid or not writable, or cannot be read.
    GCLOUD_VOICE_HTTP_BUSY: Last uploading or downloading is still ongoing, please retry later.
### 3.7 Start playing the recording file downloaded
1.API Description    

Call this API to play downloaded recording files.

2.Function Prototype

      GCloudVoiceErr PlayRecordedFile (string downloadFilePath)
  |Parameter|Type|Meaning|
  |--|--|--|
  |filePath|string| Storage path of downloaded files (separated by "/" but not "\")
  
 For successful playback, `delegate void PlayRecordFilCompletehandler(GCloudVoiceCompleteCode code, string filepath)` will be called back.  

3.Sample Code

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
4.Error Codes

    GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization
    GCLOUD_VOICE_MODE_STATE_ERR: Not in Voice Message mode
    GCLOUD_VOICE_PARAM_INVALID: Parameters transferred are incorrect, and the path is empty.
    GCLOUD_VOICE_PATH_ACCESS_ERR : The path provided is invalid or not writable
    GCLOUD_VOICE_SPEAKER_ERR: Failed to enable microphone.
### 3.8 Stop playing the recording file downloaded
1.API Description  

Call this API to suspend playing

2.Function Prototype

 ` GCloudVoiceErr StopPlayFile() `  

3.Sample Code

      public void Click_btnStopPlayRecordFile()
      {
      	m_voiceengine.StopPlayFile ();
      }
4.Error Codes

    GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization
    GCLOUD_VOICE_MODE_STATE_ERR: Not in Voice Message mode
### 3.9 Callback of Request for Voice Message Key
1.API Description  

Callback may occur when applying for voice message.

2.Function Prototype

      delegate void ApplyMessageKeyCompleteHandler(GCloudVoiceCompleteCode code)
      public abstract event ApplyMessageKeyCompleteHandler OnApplyMessageKeyComplete
    
  |Parameter|Type|Meaning|
  |--|--|--|
  |code|GCloudVoiceCompleteCode| Refer to definition of GCloudVoiceCompleteCode|
3.Sample Code
    
      m_voiceengine.OnApplyMessageKeyComplete += (IGCloudVoice.GCloudVoiceCompleteCode code) => {
      	Debug.Log ("OnApplyMessageKeyComplete c# callback");
      	s_strLog += "\r\n"+"OnApplyMessageKeyComplete ret="+code;
      	if (code == IGCloudVoice.GCloudVoiceCompleteCode.GV_ON_MESSAGE_KEY_APPLIED_SUCC) {
      		Debug.Log ("OnApplyMessageKeyComplete succ11");
      	} else {
      		Debug.Log ("OnApplyMessageKeyComplete error");
      	}
      };
### 3.10 Callback of Successful Uploading
1.API Description  

Call this API to callback the result of file uploading.

2.Function Prototype

      delegate void UploadReccordFileCompletehandler(GCloudVoiceCompleteCode code, string filepath, string fileid)
      public abstract event UploadReccordFileCompletehandler OnUploadReccordFileComplete
    
  |Parameter|Type|Meaning|
  |--|--|--|
  |code|GCloudVoiceCompleteCode| Refer to definition of GCloudVoiceCompleteCode|
  |filepath|string| Path of files to be uploaded|
  |fileid|string|File ID
3.Sample Code

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
### 3.11 Callback of Downloading
1.API Description  

Call this API to callback the result of file downloading.

2.Function Prototype

      delegate void DownloadRecordFileCompletehandler(GCloudVoiceCompleteCode code, string filepath, string fileid)
      public abstract event DownloadRecordFileCompletehandler OnDownloadRecordFileComplete
    
  |Parameter|Type|Meaning|
  |--|--|--|
  |code|GCloudVoiceCompleteCode| Refer to definition of GCloudVoiceCompleteCode|
  |filepath|string| Downloading path|
  |fileid|string|File ID
3.Sample Code

      m_voiceengine.OnDownloadRecordFileComplete += (IGCloudVoice.GCloudVoiceCompleteCode code, string filepath, string fileid) => {
      	Debug.Log ("OnDownloadRecordFileComplete c# callback");
      	s_strLog += "\r\n"+"OnDownloadRecordFileComplete ret="+code+" filepath:"+filepath+" fielid:"+fileid;
      	if (code == IGCloudVoice.GCloudVoiceCompleteCode.GV_ON_DOWNLOAD_RECORD_DONE) {
      		Debug.Log ("OnDownloadRecordFileComplete succ, filepath:" + filepath + " fileid:" + fileid);
      	} else {
      		Debug.Log ("OnDownloadRecordFileComplete error");
      	}
      };
### 3.12 Callback after normal playback
1.API Description  

If users do not suspend the play and the voice recording document has been played, then the callback may be executed via this function.

2.Function Prototype

      delegate void PlayRecordFilCompletehandler(GCloudVoiceCompleteCode code, string filepath)
      public abstract event PlayRecordFilCompletehandler OnPlayRecordFilComplete;
    
  |Parameter|Type|Meaning|
  |--|--|--|
  |code|GCloudVoiceCompleteCode| Refer to definition of GCloudVoiceCompleteCode|
  |filepath|string| Path of files to be played|
3.Sample Code

      m_voiceengine.OnPlayRecordFilComplete += (IGCloudVoice.GCloudVoiceCompleteCode code, string filepath) => {
      	Debug.Log ("OnPlayRecordFilComplete c# callback");
      	s_strLog += "\r\n"+"OnPlayRecordFilComplete ret="+code+" filepath:"+filepath;
      	if (code == IGCloudVoice.GCloudVoiceCompleteCode.GV_ON_PLAYFILE_DONE) {
      		Debug.Log ("OnPlayRecordFilComplete succ, filepath:" + filepath);
      	} else {
      		Debug.Log ("OnPlayRecordFilComplete error");
      	}
      };   
