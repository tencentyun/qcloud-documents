## Creating Object
You can create a player object by embedding the &lt;object ID="player" .../&gt; tag into the page.

```html
<!--The clsid of the player object is 99DD15EF-B353-4E47-9BE7-7DB4BC13613C-->
<!--Note: If you directly copy the code, you need to modify the LiteAVAX.cab path and version number.-->
<object ID="player" CLASSID="CLSID:99DD15EF-B353-4E47-9BE7-7DB4BC13613C"
   codebase="./LiteAVAX.cab#version=1,0,0,1" width="640" height="480">
</object>

<!-- Method to call player object >
<script>
  function setRenderWndSize() {
      var vW = 640;
      var vH = 480;
      player.setRenderWndSize(vW, vH );	
  }
</script>
```

## APIs

| Name | Description |
| ---------------------------------------- | ------------- |
| getVersion() | Disables image rendering |
| setRenderWndSize(width, height) | Sets the size of the current video rendering window |
| startPlay(sUrl,streamType) | Starts playback of pulled streams |
| stopPlay() | Stops playback |
| pause() | Pauses playback |
| resume() | Resumes playback |
| isPlaying() | Indicates whether the playback is in progress |
| setMute(bMute) | Enables Mute |
| setRenderMode(modeType) | Sets the rendering (filling) mode of image |
| setRenderYMirror(bool) | Sets the mirroring effect for rendering |
| setRotation(TXEVideoRotation) | Sets the clockwise rotation of image |
| setTXEPlayType(streamType) | Sets the stream type (standard or low-delay streams) |
| captureVideoSnapShot(sFileFullPath,sDirPath) | Captures the screenshot of pushed video image and saves to local device |
| setPlayerEventCallBack(callbackfun, objectid) | Sets callback API |

### 1. getVersion()

Gets plug-in version number, which corresponds to the "version" in the &lt;object ... codebase='...&version=1.0.0.1'/&gt; tag.

- **Returned result**

| Parameter | Type | Description |
| ---- | ------ | ----------- |
| vRet | String | Version No.: x.x.x.x |

- **Sample code** 

```
var vVersionString = player.getVersion()
```

### 2. setRenderWndSize(width, height)

Sets the size of the video playback window. It needs to be aligned with the width and height values in the &lt;object ... width="x", height="x" /&gt; tag and is set before playback starts.

- **Parameter description**

| Parameter | Type | Description |
| ------ | ---- | ------ |
| width | Int | Length of video window |
| height | Int | Width of video window |

- **Sample code** 

```
function setRenderWndSize() {
	player.setRenderWndSize(640, 480);	
}
```

### 3. startPlay(sUrl,streamType)

- **Parameter description**
Starts playback, and sURL is the playback URL. ActiveX plug-ins only support RTMP playback protocol. The push URL is `rtmp://8888.livepush.myqcloud.com/live/8888_teststream?bizid=8888&txSecret=6e18e8db0ff2070a339ab739ff46b957&txTime=5A3E7D7F`.

  The playback URL is: 
`rtmp://8888.liveplay.myqcloud.com/live/8888_teststream`

 streamType: 0 indicates standard live stream, and 1 indicates low-delay stream. Default is 1. For more information, please see AxTXEPlayType definition.

- **Returned result**
 Success or failure. Memory allocation, resource request failure, and other reasons may result in the failure to return response.

| Parameter | Type | Description |
| ---- | ---- | -------- |
| vRet | Int | 0: failed; >0: successful |

- **Sample code** 

```
function doStartPlay(sUrl) {
	var vRetInt = player.startPlay(sUrl, AxTXEBeautyStyle.AX_PLAY_TYPE_LIVE_RTMP_ACC);	
}
```

### 4. stopPlay()

Stops playback.

- **Sample code** 

```
player.stopPlay()
```

### 5. pause()

Pauses playback. Pause does not work in live streaming or real-time video chat scenarios, where pause = stopPlay + retain the last frame of video image.

- **Sample code** 

```
player.pause()
```

### 6. resume()

Resumes playback.

- **Sample code** 

```
player.resume()
```

### 7. isPlaying()

Indicates whether the playback is in progress.

- **Returned result**

| Parameter | Type | Description |
| ---- | ---- | --------- |
| vRet | Int | 0: Not started yet; 1: In progress |

- **Sample code** 

```
var vRetInt = player.isPlaying()
```

### 8. setMute(bMute)

Enables Mute feature (stops playing the sound of the other user).

- **Parameter description**

| Parameter | Type | Description |
| ----- | ---- | -------------- |
| bMute | Int | Indicates whether to enable Mute. 0: disable; 1: enable. |

- **Sample code** 

```
function setMute() {
    player.setMute(1);
}
```

### 9. setRenderMode(modeType)

Sets the rendering (fill) mode of image.

- **Parameter description**

| Parameter | Type | Description |
| -------- | ---- | ---------------------------------------- |
| modeType | Int | 1: Adaption. The video image is displayed in full on the screen, possibly with black edges around it.<br/> 2: Filling. No black edge exists, but the parts beyond the rendering area are trimmed off. <br/>For more information, please see AxTXERenderMode definition. |

- **Sample code** 

```
function setRenderMode() {
    player.setRenderMode(AxTXERenderMode.AX_TXE_RENDER_MODE_ADAPT);
}
```

### 10. setRotation(rotationType)

Sets the clockwise rotation of image.

- **Parameter description**

| Parameter | Type | Description |
| ------------ | ---- | ---------------------------------------- |
| rotationType | Int | 1: No rotation of the image; <br/>2: Rotates the image 90 degrees clockwise, with its width and height interchanged; <br/>3: Rotates the image 180 degrees clockwise, with the image reversed upside down; <br/>4: Rotates the image 270 degrees clockwise, with its width and height interchanged. <br/>For more information, please see AxTXEVideoRotation definition. |

- **Sample code** 

```
function setRotation() {
    player.setRotation(AxTXEVideoRotation.AX_TXE_VIDEO_ROTATION_NONE);
}
```

### 11. setRenderYMirror(bMirror)

Sets the mirroring effect for preview. Boolean type is unavailable in the ActiveX export API, so Int type is used instead.

- **Parameter description**

| Parameter | Type | Description |
| ------- | ---- | ----------------- |
| bMirror | Int | 1: The image is mirrored horizontally; 0: The image remains as it is. |

- **Sample code** 

```
function setRenderYMirror() {
    player.setRenderYMirror(1);
}
```


### 12. setTXEPlayType(streamType)

Sets the mirroring effect for preview. Boolean type is unavailable in the ActiveX export API, so Int type is used instead.

- **Parameter description**

| Parameter | Type | Description |
| ---------- | ---- | ---------------------------------------- |
| streamType | Int | 0: Standard stream; 1: Low-delay stream. Default is 1. For more information, please see AxTXEPlayType definition. |

- **Sample code** 

```
function setRenderYMirror() {
    player.setTXEPlayType(AxTXEBeautyStyle.AX_PLAY_TYPE_LIVE_RTMP_LOC_DELAY);
}
```

### 13. captureVideoSnapShot(sFileFullPath,sDirPath)

Captures snapshot of pulled video image and stores it under sFileFullPath. If sFileFullPath is "", it will be written to the temp directory. Only .jpg file is supported.

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

- **Sample code** 

```
function screenShotplayer() {
	//The first parameter specifies the file and the second specifies the directory. Use "" if you don't need to specify the file.
    //var ret = player.captureVideoSnapShot("", "");
    var ret = player.captureVideoSnapShot("D:\\subTest\\123.jpg", "");
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

### 14. setPlayerEventCallBack(callbackfun, objectid)

Sets callback for playback event.

- **Parameter description**

| Parameter | Type | Description |
| ----------- | ---- | ------ |
| callbackfun | Func | Callback function |
| objectid | Int | Callback object ID |

- **paramJson format**[callback parameter in JSON format]
  - eventId: Int (Event ID. See PlayerCallBackEvent definition.)
  - objectId: Int (Identical to setPlayerEventCallBack::objectid)
  - paramCnt: Int (Number of Key-Value pairs carried by JSON in parameter paramlist.)
  - paramlist: List (Key value pairs expressed in String). If the pull is successful, the stream status information is called back in real time.
    - key: String
    - value: String
  - [paramJson] example: {"eventId":200002,"objectId":1,"paramCnt":9,"paramlist":[{"key":"AUDIO_BITRATE","value":"0"},{"key":"CACHE_SIZE","value":"571"},{"key":"CODEC_CACHE","value":"329"},{"key":"NET_SPEED","value":"0"},{"key":"SERVER_IP","value":""},{"key":"VIDEO_BITRATE","value":"0"},{"key":"VIDEO_FPS","value":"14"},{"key":"VIDEO_HEIGHT","value":"240"},{"key":"VIDEO_WIDTH","value":"320"}]} 
- **Sample code**: 

```javascript
//Called before push.
player.setPlayerEventCallBack(PlayerEventListener, 1);

var PlayerEventListener = function (paramJson) {
    var obj = JSON.parse(paramJson);
    if (parseInt(obj.eventId) == 2002 && parseInt(obj.objectId) == 1) {
    	alert("Pull successful");
    }
    else if (parseInt(obj.eventId) == -2301 && parseInt(obj.objectId) == 1) {
    	alert("The network is disconnected and reconnection attempts failed. Restart the push. ");
    }
    else if (parseInt(obj.eventId) == 200002 && parseInt(obj.objectId) == 1) {
        doUpdatePlayerStatusInfo(paramJson);
    }
};

function doUpdatePlayerStatusInfo(paramJson) {
//See [paramlist:List] for an example of paramJson.
    var obj = JSON.parse(paramJson);
    if (obj.paramCnt != 0) {
        for (var i = 0; i < obj.paramCnt; ++i) {
            if(obj.paramlist[i].key == CBParamJsonKey.KEY_VIDEO_BITRATE)
                document.getElementById('PLAYVIDEO_BITRATEID').innerHTML = obj.paramlist[i].value;
            else if(obj.paramlist[i].key == CBParamJsonKey.KEY_AUDIO_BITRATE)
                document.getElementById('PLAYAUDIO_BITRATEID').innerHTML = obj.paramlist[i].value;
            else if(obj.paramlist[i].key == CBParamJsonKey.KEY_VIDEO_FPS)
                document.getElementById('PLAYVIDEO_FPSID').innerHTML = obj.paramlist[i].value;
            ....
        }
    }
}
```

## Event Handling

### 1. Normal events

| Event ID | Value | Description |
| ---------------------------- | ---- | -------------- |
| PLAY_EVT_CONNECT_SUCC        | 2001 | Connected to the server |
| PLAY_EVT_RTMP_STREAM_BEGIN   | 2002 | Connected to the server. Pull starts. |
| PLAY_EVT_RCV_FIRST_I_FRAME   | 2003 | The first video data packet (IDR) is rendered |
| PLAY_EVT_PLAY_BEGIN          | 2004 | Video playback started |
| PLAY_EVT_PLAY_PROGRESS       | 2005 | Video playback progress |
| PLAY_EVT_PLAY_END            | 2006 | Video playback ended |
| PLAY_EVT_PLAY_LOADING        | 2007 | Video playback loading |
| PLAY_EVT_START_VIDEO_DECODER | 2008 | Decoder started |
| PLAY_EVT_CHANGE_RESOLUTION   | 2009 | Video resolution changed |
| PLAY_EVT_SNAPSHOT_RESULT   | 2010 | Error code returned for screencap |

### 2. Error notifications

Some fatal errors occurred with SDK, such as network disconnection, can cause the failure to continue playback. In this case, you need to deal with these errors accordingly.

| Event ID | Value | Description |
| ------------------------------ | ----- | --------------------- |
| PLAY_ERR_NET_DISCONNECT        | -2301 | The network is disconnected and reconnection attempts failed. This can result in the failure of playback. |
| PLAY_ERR_GET_RTMP_ACC_URL_FAIL | -2302 | Failed to obtain the accelerated pull URL. This can result in the failure of playback. |

### 3. Warning events

Non-fatal errors occurred with SDK generally do not cause the stop of playback, so you can ignore the following events.

**PLAY_WARNING_VIDEO_PLAY_LAG** is an event that SDK throws to indicate the playback stutter. It means the lag between video images (the refresh time between two frames) exceeds 500ms.

| Event ID | Value | Description |
| ------------------------------------- | ---- | ------------------------------- |
| PLAY_WARNING_VIDEO_DECODE_FAIL        | 2101 | Failed to decode the current video frame |
| PLAY_WARNING_AUDIO_DECODE_FAIL        | 2102 | Failed to decode the current audio frame |
| PLAY_WARNING_RECONNECT                | 2103 | Network disconnected. Auto reconnection has been initiated (no more attempts will be made after three failed attempts) |
| PLAY_WARNING_RECV_DATA_LAG            | 2104 | Unstable inbound packet: This may be caused by insufficient downstream bandwidth, or inconsistent outbound stream from the VJ end. |
| PLAY_WARNING_VIDEO_PLAY_LAG           | 2105 | Stutter occurred during the video playback (user experience) |
| PLAY_WARNING_HW_ACCELERATION_FAIL     | 2106 | Failed to start hard decoding. Soft decoding is used instead (not supported) |
| PLAY_WARNING_VIDEO_DISCONTINUITY      | 2107 | Discontinuous sequence of video frames. Some frames may be dropped. |
| PLAY_WARNING_FIRST_IDR_HW_DECODE_FAIL | 2108 | Hard decoding of the first I-frame of current stream failed. Switched to soft decoding automatically. |
| PLAY_WARNING_DNS_FAIL                 | 3001 | RTMP - DNS resolution failed |
| PLAY_WARNING_SEVER_CONN_FAIL          | 3002 |  Failed to connect to RTMP server |
| PLAY_WARNING_SHAKE_FAIL               | 3003 |  Handshake with RTMP server failed |
| PLAY_WARNING_SERVER_DISCONNECT        | 3004 | RTMP server disconnected automatically |


## Enumeration Type

### AxTXERenderMode

- Window rendering method: Rendering a 16:9 video on a 4:3 window
  var AxTXERenderMode = {
  AX_TXE_RENDER_MODE_ADAPT : 1,         // Adaption. The video image is displayed in full on the screen, possibly with black edges around it.
  AX_TXE_RENDER_MODE_FILLSCREEN : 2,        // Filling. No black edge exists, but the parts beyond the rendering area are trimmed off, so that the image is centered on the screen.
  };

### AxTXEVideoRotation
- Rotation of rendered video
  var  AxTXEVideoRotation =  {
  AX_TXE_VIDEO_ROTATION_NONE : 1,            // No rotation of the image
  AX_TXE_VIDEO_ROTATION_90 : 2,              // Rotates the image 90 degrees clockwise, with its width and height interchanged.
  AX_TXE_VIDEO_ROTATION_180 : 3,          // Rotates the image 180 degrees clockwise, with the image reversed upside down.
  AX_TXE_VIDEO_ROTATION_270 : 4,            // Rotates the image 270 degrees clockwise, with its width and height interchanged.
  };
	
### AxTXEPlayType 

- Sets the stream type at viewer end.
  var AxTXEBeautyStyle = {
  AX_PLAY_TYPE_LIVE_RTMP : 0,   //RTMP live streaming. It has a higher delay (about 1s), and is suitable for the scenarios featuring one VJ and a number of viewers (more than 10 users are allowed to request playback of video).

  AX_PLAY_TYPE_LIVE_RTMP_ACC : 1,  // ActiveX uses ACC + RTMP by default to accelerate live streaming. This has a lower delay (about 500ms) and is suitable for the scenarios featuring bi-directional video streaming between two people or multi-directional video streaming between many people.
  };

