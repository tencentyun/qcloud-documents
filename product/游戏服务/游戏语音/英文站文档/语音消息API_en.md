## 1 Overview
To use Voice Message, you need to call [Basic API](https://cloud.tencent.com/document/product/556/7665) at first.

## 2 Call APIs for Voice Message 
![](https://mc.qcloudimg.com/static/img/28ec9bf0eab80c06c7883219fbd7604a/jj3.png)  
**How-To**   
1. Call `SetMode()` to enable Voice Message mode.  
2. Call `ApplyMessageKey()` to obtain security key information of voice message, and callback may be conducted via `OnApplyMessageKeyComplete` after successful application.  
3. Call `StartRecording()` to start recording and save the recorded file to `/your path`.  
4. Call `StopRecording` to cancel recording 
5. After recording, call `UploadRecordedFile` to upload the file to `GcloudVoice` server. Meanwhile `OnUploadReccordFileComplete` will be called back and return `ShareFileID` if operation succeeds. The returned ID is the unique ID of this file and may be downloaded by other users for listening. Server needs to manage and forward it.  
6. To play voice messages from others on the game client, please first obtain `ShareFileID` transferred from server and then call `DownloadRecordedFile` to download the recorded file. The result of downloading will be returned by callback of `OnDownloadRecordFileComplete`. When downloading succeeds, call `PlayRecordedFile` to play the file. Call `StopPlayFile` to cancel playing if necessary.   
 
## 3 APIs for Voice Messages
### 3.1 Apply for Voice Message Key

1.API Description  

	For Voice Message mode, call this API to apply for permission first

2.Function Prototype

`GCloudVoiceErrno ApplyMessageKey(int msTimeout)`

  	|Parameter|Type|Meaning|
  	|--|--|--|
  	|msTimeout|int|Timeout setting (unit:ms)
	The application result will be called back via `void OnApplyMessageKey(GCloudVoiceCompleteCode code)`.

3.Sample Code
  
    void Click_btnApplyMessageKey()
    {
    gcloud_voice::GetVoiceEngine()->ApplyMessageKey (6000);
    } 
    
4.Error Codes

GCLOUD_VOICE_PARAM_INVALID: Parameters transferred in are incorrect, such as timeout of 5000ms-60000ms     
GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization    
GCLOUD_VOICE_AUTHKEY_ERR: Internal error while applying for a Key. Please contact GCloud team and provide log for positioning.



### 3.2. Set the max length of a voice message
1.API Description
 
	For Voice Message mode, call this API to set the max length of voice message (up to 2 min)

2.Function Prototype

`GCloudVoiceErrno SetMaxMessageLength(int msTime)`  
  
  	|Parameter|Type|Meaning|
  	|--|--|--|
  	|msTimeout|int|Maximum length of voice message (unit: ms)|

3.Sample Code

    int ret1 = gcloud_voice::GetVoiceEngine()->SetMaxMessageLength (60000);

4.Error Codes

GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization  
GCLOUD_VOICE_PARAM_INVALID: Invalid parameters. E.g. the time setting should be 1000ms to 1000260ms

### 3.3 Start Recording
1.API Description    
For Voice Message mode, call this API to specify a storage path for the recorded file while starting recording.

2.Function Prototype

`GCloudVoiceErrno StartRecording(const char * filePath)`  

  	|Parameter|Type|Meaning|
  	|--|--|--|
  	|filePath|const char*| Storage path of recorded files (separated by "/" but not "\").

3.Sample Code

      public void Click_btnStartRecord()
      {
      	gcloud_voice::GetVoiceEngine()->StartRecording (m_recordpath);
    
      }

4.Error Codes

GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization  
GCLOUD_VOICE_MODE_STATE_ERR: Not in Voice Message mode 
GCLOUD_VOICE_PARAM_INVALID: Invalid parameters: the path is empty.  
GCLOUD_VOICE_NEED_AUTHKEY: Need to call `GetAuthKey` first to get permission 
GCLOUD_VOICE_PATH_ACCESS_ERR : The path provided is invalid or not writable 


### 3.4 Stop Recording
1.API Description  

	For Voice Message mode, call this API to stop recording

2.Function Prototype

  	`GCloudVoiceErrno StopRecording()`

3.Sample Code

      public void Click_btnStopRecord()
      {
      	gcloud_voice::GetVoiceEngine()->StopRecording ();
      }
4.Error Codes

GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization  
GCLOUD_VOICE_MODE_STATE_ERR: Not in Voice Message mode 
GCLOUD_VOICE_NEED_AUTHKEY: Need to call `GetAuthKey` first to get permission 
### 3.5 Upload the Recorded File
1.API Description  

After recording, call this API to upload the recorded file to the specified storage path.

2.Function Prototype

`GCloudVoiceErrno UploadRecordedFile(const char * filePath, int msTimeout = 60000)`

  	|Parameter|Type|Meaning|
  	|--|--|--|
  	|filePath|const char*| Storage path of recorded files (separated by "/" but not "\").
  	|msTimeout|int|File uploading timed out
	The uploading result is called back via `void OnUploadFile(GCloudVoiceCompleteCode code, const char *filePath, const char *fileID)`.

3.Sample Code

      public void Click_btnUploadFile()
      {
      	int ret1 = gcloud_voice::GetVoiceEngine()->UploadRecordedFile (m_recordpath, 60000);
      }
4.Error Codes

GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization  
GCLOUD_VOICE_MODE_STATE_ERR: Not in Voice Message mode 
GCLOUD_VOICE_PARAM_INVALID: Invalid parameters: the path is empty.  
GCLOUD_VOICE_NEED_AUTHKEY: Need to call `GetAuthKey` first to get permission 
GCLOUD_VOICE_PATH_ACCESS_ERR: The path provided is invalid or not accessible.  
GCLOUD_VOICE_HTTP_BUSY: Last uploading or downloading is still ongoing, please retry later.  

### 3.6 Download the recorded file
1.API Description  

	After recording, call this API to upload the recorded file to the specified storage path.

2.Function Prototype


`GCloudVoiceErrno DownloadRecordedFile (const char *fileID, const char * downloadFilePath, int msTimeout = 60000);`
    
  	|Parameter|Type|Meaning|
  	|--|--|--|
  	|fileID| const char *| ID of files to be downloaded
  	|downloadFilePath|const char *| Storage path of downloaded recording files (separated by "/" but not "\")
  	|msTimeout|int|File downloading timed out
	The downloading result is called back via `void OnDownloadFile(GCloudVoiceCompleteCode code, const char *filePath, const char *fileID)`.


3.Sample Code

      public void Click_btnDownloadFile()
      {
      	int ret = gcloud_voice::GetVoiceEngine()->DownloadRecordedFile (m_fileid, m_downloadpath, 60000);
      }
4.Error Codes

GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization  
GCLOUD_VOICE_MODE_STATE_ERR: Not in Voice Message mode 
GCLOUD_VOICE_PARAM_INVALID: Invalid parameters: the path is empty.  
GCLOUD_VOICE_NEED_AUTHKEY: Need to call `GetAuthKey` first to get permission 
GCLOUD_VOICE_PATH_ACCESS_ERR : The path provided is invalid or not accessible.  
GCLOUD_VOICE_HTTP_BUSY: Last uploading or downloading is still ongoing, please retry later.  

### 3.7 Start playing the recording file downloaded
1.API Description    

	Call this API to play downloaded recording files.

2.Function Prototype  
`GCloudVoiceErrno PlayRecordedFile (const char * downloadFilePath)`

  	|Parameter|Type|Meaning|
  	|--|--|--|
  	|filePath|const char*| Storage path of downloaded files (separated by "/" but not "\")
	For successful playback, `void OnPlayRecordedFile(GCloudVoiceCompleteCode code,const char *filePath)` will be called back.

3.Sample Code

      public void Click_btnPlayReocrdFile()
      {
      	int err;
      	err = gcloud_voice::GetVoiceEngine()->PlayRecordedFile(m_downloadpath);
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
   `GCloudVoiceErrno StopPlayFile() `

3.Sample Code

    public void Click_btnStopPlayRecordFile()
    {
    gcloud_voice::GetVoiceEngine()->StopPlayFile ();
    } 
 
4.Error Codes  
GCLOUD_VOICE_NEED_INIT: Need to call `Init` first for initialization  
GCLOUD_VOICE_MODE_STATE_ERR: Not in Voice Message mode 


### 3.9 Callback of Request for Voice Message Key

1.API Description
allback may occur when applying for voice message.

2.Function Prototype  
   `void OnApplyMessageKey(GCloudVoiceCompleteCode code) ;`

    |Parameter|Type|Meaning|
    |--|--|--|
    |code|GCloudVoiceCompleteCode| Refer to definition of GCloudVoiceCompleteCode|

3.Sample Code

      void MessageNotify::OnApplyMessageKey(gcloud_voice::GCloudVoiceCompleteCode code)
      {
      	std::string msg;
      	if (code == gcloud_voice::GV_ON_MESSAGE_KEY_APPLIED_SUCC) {
     		 msg = "OnApplyMessageKey success";
      	} else {
      		msg = "OnApplyMessageKey error " + code;
      	}
      	_section->setText(msg);
      }
### 3.10 Callback of Successful Uploading

1.API Description  

  	Call this API to callback the result of file uploading.

2.Function Prototype  

  `void OnUploadFile(GCloudVoiceCompleteCode code, const char *filePath, const char *fileID) `

   	|Parameter|Type|Meaning|
   	|--|--|--|
   	|code|GCloudVoiceCompleteCode| Refer to definition of GCloudVoiceCompleteCode|
   	|filepath|const char *| Path of files to be uploaded|
   	|fileid|const char *|File ID|

3.Sample Code

      void MessageNotify::OnUploadFile(gcloud_voice::GCloudVoiceCompleteCode code, const char *filePath, const char *fileID)
      {
      	if (code == gcloud_voice::GV_ON_UPLOAD_RECORD_DONE) {
     		 _section->setText("OnUploadFile success");
     		 _section->setFileID((char *)fileID);
      	} else {
      		_section->setText("OnUploadFile error");
      	}
      }

### 3.11 Callback of Downloading

1.API Description  

	Call this API to callback the result of file downloading.

2.Function Prototype

 `void OnDownloadFile(GCloudVoiceCompleteCode code, const char *filePath, const char *fileID) ;`

  	|Parameter|Type|Meaning|
  	|--|--|--|
  	|code|GCloudVoiceCompleteCode| Refer to definition of GCloudVoiceCompleteCode|
  	|filepath|const char *| Downloading path|
  	|fileid|const char *|File ID|

3.Sample Code
    
      void MessageNotify::OnDownloadFile(gcloud_voice::GCloudVoiceCompleteCode code, const char *filePath, const char *fileID)
      {
      	if (code == gcloud_voice::GV_ON_DOWNLOAD_RECORD_DONE) {
     		_section->setText("OnDownloadFile success");
     	 } else {
     		 _section->setText("OnDownloadFile error");
      	}
      }

### 3.12 Callback after normal playback

1.API Description  

	If users do not suspend the play and the voice recording document has been played, then the callback may be executed via this function.

2.Function Prototype

  `void OnPlayRecordedFile(GCloudVoiceCompleteCode code,const char *filePath) `

  	|Parameter|Type|Meaning|
 	 |--|--|--|
 	 |code|GCloudVoiceCompleteCode| Refer to definition of GCloudVoiceCompleteCode|
  	|filepath|const char *| Path of files to be played|

3.Sample Code

      void MessageNotify::OnPlayRecordedFile(gcloud_voice::GCloudVoiceCompleteCode code,const char *filePath)
      {
      	string str="play file end";
      }       


