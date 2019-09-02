## Creating Object

You can create a pusher object by embedding the &lt;object ID="pusher" .../&gt; tag into the page.

```html
<!--The clsid of the pusher object is 01502AEB-675D-4744-8C84-9363788ED6D6-->
<!--Note: If you directly copy the code, you need to modify the LiteAVAX.cab path and version number.-->
<object ID="pusher" CLASSID="CLSID:01502AEB-675D-4744-8C84-9363788ED6D6"
   codebase="./LiteAVAX.cab#version=1,0,0,1" width="640" height="480">
</object>

<!-- Method to call pusher object >
<script>
  function setRenderWndSize() {
      var vW = 640;
      var vH = 480;
      pusher.setRenderWndSize(vW, vH );	
  }
</script>
```

## APIs

| Name | Description |
| ---------------------------------------- | --------------------------- |
| getVersion() | Gets plug-in SDK version number |
| setRenderWndSize(width, height) | Sets the size of the current video rendering window |
| enumCameras(): | Enumerates current cameras |
| startCameraPreview() | Enables camera preview |
| stopPreview() | Disables camera preview |
| startPush(sUrl) | Starts push |
| stopPush() | Stops push |
| switchCamera(cameraIndex) | Switches between cameras. Dynamic switching is supported during push |
| setMute(bMute) | Enables Mute |
| setRenderMode(modeType) | Sets the rendering (filling) mode of image |
| setRotation(rotationType ) | Sets the clockwise rotation of image |
| setVideoResolution(resolutionType ) | Sets video resolution |
| setBeautyStyle(beautyStyle , beautyLevel, whitenessLevel) | Sets beauty filter and whitening effects |
| setRenderYMirror(bMirror) | Sets the mirroring effect for preview rendering |
| setOutputYMirror(bMirror) | Sets the mirroring effect of pushed image |
| setVideoBitRate(bitrate) | Sets video bitrate |
| setAutoAdjustStrategy(adjuststrategy) | Sets traffic control policy |
| setVideoBitRateMin(videoBitrateMin) | Used with setAutoAdjustStrategy |
| setVideoBitRateMax(videoBitrateMax) | Used with setAutoAdjustStrategy |
| setVideoFPS(fps) | Sets video frame rate |
| openSystemVoiceInput(bOpen) | Enables system sound input for mixing |
| startScreenPreview(x,y,width,height) | Sets the area for screen capture preview |
| setPauseVideo(bPause) | Pauses video during push (a black background is displayed instead) |
| startAudioCapture() | Enables audio capture |
| stopAudioCapture() | Disables audio capture |
| setPusherEventCallBack(callbackfun, objectid) | Sets callback API |
| captureVideoSnapShot(sFileFullPath,sDirPath) | Captures snapshot of video image at pusher end |

### 1. getVersion()

Gets plug-in version number, which corresponds to the "version" in the &lt;object ... codebase='...&version=1.0.0.1'&gt tag.

- **Returned result**

| Parameter | Type | Description |
| ---- | ------ | ----------- |
| vRet | String | Version No.: x.x.x.x |

- **Sample code** 

```
var vVersionString = pusher.getVersion()
```

### 2. setRenderWndSize()

Sets the size of the video rendering window. It needs to be aligned with the width and height values in the &lt;object ... width="x", height="x" /&gt; tag and is set before the start of push and pull.

- **Parameter description**

| Parameter | Type | Description |
| ------ | ---- | ------ |
| width | Int | Length of video window |
| height | Int | Width of video window |

- **Sample code** 

```
function setRenderWndSize() {
	var vW = 640;
	var vH = 480;
	pusher.setRenderWndSize(vW, vH );	
}
```

### 3. enumCameras()
Enumerates current cameras. Before push, check whether cameras have been installed on your PC and how many cameras are installed.

- **Returned result**

| Parameter | Type | Description |
| -------- | ------ | ----------- |
| vRetJson | String | Json format camera list |

- **vRetJson Style**
  - camera_cnt: Int (Number of cameras)
  - cameralist: List (Camera list)
    - camera_name: String (Camera name)
    - id: Int (Camera index. Note: When setting available cameras, set the camera indexes. See the description of API switchCamera.)
  - Example "{\"camera_cnt\":1,\"cameralist\":[{\"camera_name\":\"HD Pro Webcam C920\",\"id\":\"0\"}]}"
- **Sample code** 

```
function refreshCamera() {
    var vRetString = pusher.enumCameras();
    var obj = JSON.parse(vRetString);
    if (obj.camera_cnt != 0) {
        for (var i = 0; i < obj.camera_cnt; ++i) {
            var objSelect = document.getElementById('cameralistselect');
            objSelect.add(new Option(obj.cameralist[i].camera_name, obj.cameralist[i].id));
        }
    }
    else {
        alert("No camera available");
    }
}
```

### 4.startCameraPreview()

Enables camera preview. >0: API call is successful; (>0: API call failed.

- **Returned result**

| Parameter | Type | Description |
| ---- | ---- | -------- |
| vRet | Int | 0: Failed; >0: Successful |

- **Sample code** 

```
var vRetInt = pusher.startCameraPreview()
```

### 5. stopPreview()

Disables camera preview. Calling this function before calling stopPush does not stop the push, but can cause the SDK to only push audio data.

- **Sample code** 

```
pusher.stopPreview()
```

### 6. startPush(sUrl)

Starts the push (you need to check the camera before calling startPush, otherwise the push may fail).

- **Parameter description**
  A valid push URL, which supports RTMP protocol. The URL starts with "rtmp://". For more information on how to obtain Tencent Cloud push URL, please see [DOC](https://cloud.tencent.com/document/product/454/7915).  

| Parameter | Type | Description |
| ---- | ------ | ---- |
| sUrl | String | Push URL |

- **Returned result**
  Success or failure. Memory allocation, resource request failure, and other reasons may result in the failure to return response.
| Parameter | Type | Description |
| ---- | ---- | -------- |
| vRet | Int | 0: Failed; >0: Successful |

- **Sample code** 

```
function doStartPush(sUrl) {
	var vRetInt = pusher.startPush(sUrl);	
}
```

### 7. stopPush()

Stops push. Note: A push URL is exclusive, that is, a push URL can only be used by one pusher for pushing streams at a time.

- **Sample code**: 

```
pusher.stopPush()
```

### 8. switchCamera(cameraIndex)

Switches between cameras. Dynamic switching is supported during push. The parameter cameraIndex can be obtained via enumCameras.

- **Parameter description**

| Parameter | Type | Description |
| ----------- | ---- | ---------------------- |
| cameraIndex | Int | Camera index. Default is 1. The index of the first camera is 0. |

- **Sample code**: 

```
function switchCameraSelect() {
    var obj = document.getElementById('cameralistselect');
    var index = obj.selectedIndex; //The sequence number of the selected camera.  
    var val = obj.options[index].value;
    pusher.switchCamera(parseInt(val));
}
```

### 8. setMute(bMute)

Disables microphone to allow the SDK to stop capturing microphone sound input. This can be used when you do not want your voice to be heard by others.

- **Parameter description**

| Parameter | Type | Description |
| ----- | ---- | -------------- |
| bMute | Int | Indicates whether to enable Mute. 0: Disable; 1: Enable. |

- **Sample code**: 

```
function setMute() {
    pusher.setMute(1);
}
```

### 9. setRenderMode(modeType)

Sets the rendering (fill) mode of image.

- **Parameter description**

| Parameter | Type | Description |
| -------- | ---- | ---------------------------------------- |
| modeType | Int | 1: Adaption. The video image is displayed in full on the screen, possibly with black edges around it.<br/> 2: Filling. No black edge exists, but the parts beyond the rendering area are trimmed off.<br/> For more information, please see AxTXERenderMode definition. |

- **Sample code**: 

```
function setRenderMode() {
    pusher.setRenderMode(AxTXERenderMode.AX_TXE_RENDER_MODE_ADAPT);
}
```

### 10. setRotation(rotationType)

Sets the clockwise rotation of image.

- **Parameter description**

| Parameter | Type | Description |
| ------------ | ---- | ---------------------------------------- |
| rotationType | Int | 1: No rotation of the image; <br/>2: Rotates the image 90 degrees clockwise, with its width and height interchanged; <br/>3: Rotates the image 180 degrees clockwise, with the image reversed upside down; <br/>4: Rotates the image 270 degrees clockwise, with its width and height interchanged. <br/>For more information, please see AxTXEVideoRotation definition. |

- **Sample code**: 

```
function setRotation() {
    pusher.setRotation(AxTXEVideoRotation.AX_TXE_VIDEO_ROTATION_NONE);
}
```

### 11. setVideoResolution( )

Sets the video resolution to be used with bitrate. For example, use a resolution of 640x360 with a bitrate of 800 Kbps, or 320x240 with 400 Kbps.

- **Parameter description**

| Parameter | Type | Description |
| -------------- | ---- | ------------------------------------------------------------ |
| resolutionType | Int | 1: RESOLUTION_320x240;<br/> 2: RESOLUTION_640x480;<br/> 3: RESOLUTION_480x272;<br/> 4: RESOLUTION_960x720.<br/> For more information, please see AxTXEVideoResolution definition. |

- **Sample code**: 

```
function setVideoResolution() {
    pusher.setVideoResolution(AxTXEVideoResolution.AX_TXE_VIDEO_RESOLUTION_320x240);
}
```

### 12. setBeautyStyle

Sets beauty filter and whitening effects.

- **Parameter description**

| Parameter | Type | Description |
| -------------- | ---- | ---------------------------------------- |
| beautyStyle | Int | 1: Smooth; <br/>2: Natural;<br/> 3: Hazy.<br/> For more information, please see AxTXEBeautyStyle definition. |
| beautyLevel | Int | Beauty filter level ranges from 1 to 9. 0 indicates disabling beauty filter. A greater value means a bigger effect. |
| whitenessLevel | Int | Whiteness level ranges from 1 to 9. 0 indicates disabling whitening. A greater value means a bigger effect. |

- **Sample code**: 

```
function setBeautyStyle() {
	var vlBeautyLevel = 5;
	var vlWhitenessLevel = 6;
    pusher.setBeautyStyle(AxTXEBeautyStyle.AX_TXE_BEAUTY_STYLE_SMOOTH, vlBeautyLevel, vlWhitenessLevel );
}
```

### 13. setRenderYMirror(bMirror)

Sets the mirroring effect for preview. Boolean type is unavailable in the ActiveX export API, so Int type is used instead.

- **Parameter description**

| Parameter | Type | Description |
| ------- | ---- | ----------------- |
| bMirror | Int | 1: The image is mirrored horizontally; 0: The image remains as it is. |

- **Sample code**: 

```
function setRenderYMirror() {
    pusher.setRenderYMirror(1);
}
```

### 14. setOutputYMirror(bMirror)

Sets the mirroring effect for pushed image. Boolean type is unavailable in the ActiveX export API, so Int type is used instead.

- **Parameter description**

| Parameter | Type | Description |
| ------- | ---- | ----------------- |
| bMirror | Int | 1: The image is mirrored horizontally; 0: The image remains as it is. |

- **Sample code**: 

```
function setOutputYMirror() {
    pusher.setOutputYMirror(1);
}
```

### 15. setVideoBitRate(bitrate)

Sets video bitrate. Note: The higher the bitrate, the clearer the image is. But a higher resolution does not necessarily mean a higher image clarity.

- **Parameter description**

| Parameter | Type | Description |
| ------- | ---- | ---------------------------------------- |
| bitrate | Int | Video bitrate (in Kbps). For example, a resolution of 640x360 is used with a video bitrate of 800 Kbps. |

- **Sample code**: 

```
function setVideoBitRate() {
    pusher.setVideoBitRate(500);
}
```

### 16.setAutoAdjustStrategy(adjuststrategy)

Sets the traffic control policy, that is, whether to allow SDK to adjust the video bitrate to adapt to the network condition, so as to avoid the stutter caused by slow upload speed.

- **Parameter description**

| Parameter | Type | Description |
| -------------- | ---- | ---------------------------------------- |
| adjuststrategy | Int | 1: No traffic control. The video bitrate specified by setVideoBitRate is always used;<br/> 0: Suitable for common push scenarios in LVB. This policy has a lower sensitivity and adapts to the bandwidth change slowly. This is helpful to maintain the image clarity when the bandwidth fluctuates.<br/> 1: Suitable for common push scenarios in LVB. This policy allows the SDK to adapt the resolution to the bitrate automatically.<br/> 5: Suitable for real-time video chats. This policy is highly sensitive to network condition and makes adaptive adjustment in case of any network fluctuation. <br/>For more information, please see AxTXEAutoAdjustStrategy definition. |

- **Sample code**: 

```
function setAutoAdjustStrategy() {
    pusher.setAutoAdjustStrategy(AxTXEAutoAdjustStrategy.TXE_AUTO_ADJUST_NONE);
}
```

### 17. setVideoBitRateMin & setVideoBitRateMax

They are used with setAutoAdjustStrategy. When the AutoAdjust policy is specified as TXE_AUTO_ADJUST_NONE, calls of both of the functions are invalid.

- **Parameter description**

| Parameter | Type | Description |
| --------------- | ---- | ---------------------------------------- |
| videoBitrateMin | Int | The minimum video bitrate of SDK output. For example, this parameter is set to 300 Kbps for a resolution of 640x360. |
| videoBitrateMax | Int | The maximum video bitrate of SDK output. For example, this parameter is set to 1000 Kbps for a resolution of 640x360. |

- **Sample code**: 

```
function setVideoBitRateMin() {
    pusher.setVideoBitRateMin(300);
}
```

### 18. setVideoFPS(fps)

Sets video frame rate. Note: This fps value sets the maximum frame rate. The frame rate of a video image depends on the camera's frame rate for capture. The supported maximum frame rate varies with different cameras.

- **Parameter description**

| Parameter | Type | Description |
| ---- | ---- | ----------------------- |
| fps | Int | Video frame rate. Default is 15. It takes effect after restart. |

- **Sample code**: 

```
function setVideoFPS() {
    pusher.setVideoFPS(15);
}
```

### 19. openSystemVoiceInput(bOpen)

Enables system sound input for mixing. This API is called when the push is successful. If it is enabled, all sounds of the system are captured for mixing with the microphone sound.

- **Parameter description**

| Parameter | Type | Description |
| ---- | ------ | ---- |
| bOpen | Int | 1: Enable; 0: Disable. Default is 0. |

- **Sample code**: 

```
function doPushOpenSystemAudioMuxer(ckbox) {
    var ckbox = document.getElementById(ckbox.id);
    if (ckbox.checked){
        pusher.openSystemVoiceInput(1);
    }
    else{
        pusher.openSystemVoiceInput(0);
    }
}
```

### 20. startScreenPreview(x,y,width,height)

Specifies the area for screencap. If all attributes are 0, the main screen is captured as a whole.

- **Parameter description**

| Parameter | Type | Description |
| ---- | ------ | ---- |
| x | Int | Position relative to the origin (left) |
| y | Int | Position relative to the origin (right) |
| width | Int | Length of the area for screencap |
| height | Int | Width of the area for screencap |

- **Sample code**: 

```
function startScreenPreview() {
	 pusher.startScreenPreview(0,0,0,0);
}
```

### 21.captureVideoSnapShot(sFileFullPath,sDirPath)

Captures snapshot of pushed video image and stores it under sFileFullPath. If sFileFullPath is "", it will be written to the temp directory. Only .jpg file is supported.

- **Parameter description**

| Parameter | Type | Description |
| ---- | ------ | ---- |
| sFileFullPath | String | Specifies the directory to store the file. A non-null value indicates that the file is directly stored. |
| sDirPath | String | Reserved parameter |


- **Returned result**
  Success or failure. Possible reasons include "File already exists", "Failed to create file", etc.
| Parameter | Type | Description |
| ---- | ---- | -------- |
| vRet | Int | -1: Failed; -2: Invalid path; -3 File already exists; -4: Not pushed |

- **Sample code**: 

```
function screenShotPusher() {
	//The first parameter specifies the file and the second specifies the directory. Use "" if you don't need to specify the file.
    //var ret = pusher.captureVideoSnapShot("", "");
    var ret = pusher.captureVideoSnapShot("D:\\subTest\\123.jpg", "");
    // -1: Failed; -2: Invalid path; -3: File already exists; -4: Not pushed.
    if (ret == -1) {
        alert("Failed to capture screenshot");
    }
    else if (ret == -2) {
        alert("Invalid path");
    }
    else if (ret == -3) {
        alert("File already exists");
    }
    else if (ret == -4) {
        alert("Not pushed");
    }
}
```

### 22. setPauseVideo(bPause)

Pauses video during push (a black background is displayed instead) |

- **Parameter description**

| Parameter | Type | Description |
| ---- | ------ | ---- |
| bOpen | Int | 1: Enable; 0: Disable. Default is 0. |

- **Sample code**: 

```
function doPauseVideo(bPause) {
     pusher.setPauseVideo(bPause);
}
```

### 23. startAudioCapture()

Enables audio capture.

- **Sample code**: 

```
function startAudioCapture(targetURL) {
	    //Starts audio push without video.
     pusher.startAudioCapture();
		 pusher.startPush(targetURL);
}
```

### 24. stopAudioCapture()

Stops audio capture.

- **Sample code**: 

```
function stopAudioCapture() {
	    //Stops audio push.
     pusher.stopAudioCapture();
}
```

### 25. setPusherEventCallBack(callbackfun, objectid)

Sets event callback to receive events thrown by SDK during push. The events are listed below.

- **Parameter description**

| Parameter | Type | Description |
| ----------- | ---- | ------ |
| callbackfun | Func | Callback function |
| objectid | Int | Callback object ID |

- **paramJson format**[callback parameter in JSON format]
  - eventId: Int (Event ID. See PusherCallBackEvent definition.)
  - objectId: Int (Identical to setPusherEventCallBack::objectid)
  - paramCnt: Int (Number of Key-Value pairs carried by JSON)
  - paramlist: List (Key value pairs expressed in String). If the pull is successful, the stream status information is called back in real time.
    - key: String
    - value: String 
  - [paramlist:List] example: {"eventId":200001,"objectId":1,"paramCnt":9,"paramlist":[{"key":"AUDIO_BITRATE","value":"0"},{"key":"CACHE_SIZE","value":"571"},{"key":"CODEC_CACHE","value":"329"},{"key":"NET_SPEED","value":"0"},{"key":"SERVER_IP","value":""},{"key":"VIDEO_BITRATE","value":"0"},{"key":"VIDEO_FPS","value":"14"},{"key":"VIDEO_HEIGHT","value":"240"},{"key":"VIDEO_WIDTH","value":"320"}]} 
  
- **Sample code**: 

```javascript
//Called before push.
pusher.setPusherEventCallBack(PusherEventListener, 1);

var PusherEventListener = function (paramJson) {
    var obj = JSON.parse(paramJson);
    if (parseInt(obj.eventId) == 1002 && parseInt(obj.objectId) == 1) {
    	alert("Push is successful");
    }
    else if (parseInt(obj.eventId) == -1307 && parseInt(obj.objectId) == 1) {
    	alert("Network disconnected. Reconnection attempts have failed for many times. Push the stream again. ");
    }
    else if (parseInt(obj.eventId) == 200001 && parseInt(obj.objectId) == 1) {
        doUpdatePluserStatusInfo(paramJson);
    }
};

function doUpdatePusherStatusInfo(paramJson) {
    //See [paramlist:List (Key Value Pair String)] for an example of paramJson.
    var obj = JSON.parse(paramJson);
    if (obj.paramCnt != 0) {
        for (var i = 0; i < obj.paramCnt; ++i) {
            if(obj.paramlist[i].key == "VIDEO_BITRATE")
                document.getElementById('PUSHVIDEO_BITRATEID').innerHTML = obj.paramlist[i].value;
            else if(obj.paramlist[i].key == "AUDIO_BITRATE")
                document.getElementById('PUSHAUDIO_BITRATEID').innerHTML = obj.paramlist[i].value;
            else if(obj.paramlist[i].key == "VIDEO_FPS")
                document.getElementById('PUSHVIDEO_FPSID').innerHTML = obj.paramlist[i].value;
            ....
        }
    }
}
```

## Events

### 1. Normal events

| Event ID | Value | Description |
| ---------------------------- | ---- | -------------- |
| PUSH_EVT_CONNECT_SUCC | 1001 | Successfully connected to push server |
| PUSH_EVT_PUSH_BEGIN | 1002 | Handshake with the server completed, and push starts |
| PUSH_EVT_OPEN_CAMERA_SUCC | 1003 | Camera enabled successfully |
| PUSH_EVT_CHANGE_RESOLUTION | 1005 | Resolution is changed dynamically during push |
| PUSH_EVT_CHANGE_BITRATE | 1006 | Bitrate is changed dynamically during push |
| PUSH_EVT_FIRST_FRAME_AVAILABLE | 1007 | The first frame is captured |
| PUSH_EVT_START_VIDEO_ENCODER | 1008 | Encoder started |
| PUSH_EVT_CAMERA_REMOVED | 1009 | Camera removed |
| PUSH_EVT_CAMERA_AVAILABLE | 1010 | Camera is available again |
| PUSH_EVT_CAMERA_CLOSED | 1011 | Camera disabled |
| PUSH_EVT_SNAPSHOT_RESULT | 1012 | Error code returned for screencap |

### 2. Error notifications

Some fatal errors occurred with SDK can cause the failure to continue playback, for example, the failure to enable camera because it is already in use.

| Event ID | Value | Description |
| ------------------------------- | ----- | ---------------------------------- |
| PUSH_ERR_OPEN_CAMERA_FAIL | -1301 | Failed to enable camera |
| PUSH_ERR_OPEN_MIC_FAIL | -1302 | Failed to enable microphone |
| PUSH_ERR_VIDEO_ENCODE_FAIL | -1303 | Video encoding failed |
| PUSH_ERR_AUDIO_ENCODE_FAIL | -1304 | Audio encoding failed |
| PUSH_ERR_UNSUPPORTED_RESOLUTION | -1305 | Unsupported video resolution |
| PUSH_ERR_UNSUPPORTED_SAMPLERATE | -1306 | Unsupported audio sampling rate |
| PUSH_ERR_NET_DISCONNECT | -1307 | Network disconnected. Too many failed reconnection attempts. Restart the push for more retries. |
| PUSH_ERR_CAMERA_OCCUPY | -1308 | The camera is in use. Enable another one. |


### 3. Warning events

Some non-fatal errors occurred with SDK can be solved in most cases by throwing warning events to trigger protection or recovery logics. 

**WARNING_NET_BUSY**
VJ's network is busy. This warning can be used as a UI message for users.

**WARNING_SERVER_DISCONNECT**
Push request rejected by backend. This is usually caused by the miscalculated txSecret in the push URL, or because the push URL is already in use (a push URL can only be used by one pusher at a time).

| Event ID | Value | Description |
| ---------------------------------------- | ---- | ------------------------------- |
| PUSH_WARNING_NET_BUSY | 1101 | Bad network connection: data upload is blocked because upstream bandwidth is too small |
| PUSH_WARNING_RECONNECT | 1102 | Network disconnected. Auto reconnection has been initiated (no more attempts will be made after three failed attempts) |
| PUSH_WARNING_HW_ACCELERATION_FAIL | 1103 | Failed to start hard encoding. Soft encoding is used instead. |
| PUSH_WARNING_VIDEO_ENCODE_FAIL | 1104 | Video encoding failed. Non-fatal error. Encoder will be restarted internally. |
| PUSH_WARNING_BEAUTYSURFACE_VIEW_INIT_FAIL | 1105 | Video encoding bitrate error |
| PUSH_WARNING_VIDEO_ENCODE_BITRATE_OVERFLOW | 1106 | Video encoding bitrate error |
| PUSH_WARNING_DNS_FAIL | 3001 | RTMP - DNS resolution failed (this triggers retries) |
| PUSH_WARNING_SEVER_CONN_FAIL | 3002 | Failed to connect to RTMP server (this triggers retries) |
| PUSH_WARNING_SHAKE_FAIL | 3003 | Handshake with RTMP server failed (this triggers retries) |
| PUSH_WARNING_SERVER_DISCONNECT | 3004 | RTMP server disconnected automatically. Check the validity of push URL or the validity period of hotlink protection |
| PUSH_WARNING_SERVER_NO_DATA | 3005 | No data was sent within 30 seconds. Server disconnected automatically. |


## Enumeration Type

### AxTXERenderMode 

- Window rendering method: Rendering a 16:9 video on a 4:3 window
  var AxTXERenderMode = {
  AX_TXE_RENDER_MODE_ADAPT: 1,              //Adaption. The video image is displayed in full on the screen, possibly with black edges around it.
  AX_TXE_RENDER_MODE_FILLSCREEN: 2,      //Filling. No black edge exists, but the parts beyond the rendering area are trimmed off, so that the image is centered on the screen.
  };

### AxTXEVideoRotation 

- Rotation of rendered video
  var  AxTXEVideoRotation =  {
  AX_TXE_VIDEO_ROTATION_NONE: 1,            // No rotation of the image
  AX_TXE_VIDEO_ROTATION_90: 2,            // Rotates the image 90 degrees clockwise, with its width and height interchanged.
  AX_TXE_VIDEO_ROTATION_180 : 3,          // Rotates the image 180 degrees clockwise, with the image reversed upside down.
  AX_TXE_VIDEO_ROTATION_270 : 4,            // Rotates the image 270 degrees clockwise, with its width and height interchanged.
  };

### AxTXEVideoResolution 

- Resolution of pushed video
  var AxTXEVideoResolution = {
  // Standard screen 4:3
  AX_TXE_VIDEO_RESOLUTION_320x240 : 1,
  AX_TXE_VIDEO_RESOLUTION_480x360 : 2,
  AX_TXE_VIDEO_RESOLUTION_640x480 : 3,
  AX_TXE_VIDEO_RESOLUTION_960x720 : 4,
   // Wide screen 3:4
  AX_TXE_VIDEO_RESOLUTION_240x320 : 50,
  AX_TXE_VIDEO_RESOLUTION_360x480 : 51,
  AX_TXE_VIDEO_RESOLUTION_480x640 : 52,
  AX_TXE_VIDEO_RESOLUTION_720x960 : 53,

  // Wide screen 16:9
  AX_TXE_VIDEO_RESOLUTION_320x180 : 101,
  AX_TXE_VIDEO_RESOLUTION_480x272 : 102,
  AX_TXE_VIDEO_RESOLUTION_640x360 : 103,
  AX_TXE_VIDEO_RESOLUTION_960x540 : 104,
  // Wide screen 9:16
  AX_TXE_VIDEO_RESOLUTION_180x320 : 201,
  AX_TXE_VIDEO_RESOLUTION_272x480 : 202,
  AX_TXE_VIDEO_RESOLUTION_360x640 : 203,
  AX_TXE_VIDEO_RESOLUTION_540x960 : 204,

  };

### AxTXEBeautyStyle 

- Sets the style of beauty filter
  var AxTXEBeautyStyle = {
  AX_TXE_BEAUTY_STYLE_SMOOTH : 0,        // Smooth
  AX_TXE_BEAUTY_STYLE_NATURE : 1,      // Natural
  AX_TXE_BEAUTY_STYLE_BLUR : 2,       // Hazy
  };

