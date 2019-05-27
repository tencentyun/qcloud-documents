## 对象创建

在页面嵌入 &lt;object ID="pusher" .../&gt; 标签，即创建了 pusher 对象

```html
<!-- 注意 pusher 对象的 clsid 为 01502AEB-675D-4744-8C84-9363788ED6D6 -->
<!--Warning::直接拷贝代码需要修改LiteAVAX.cab路径和版本号-->
<object ID="pusher" CLASSID="CLSID:01502AEB-675D-4744-8C84-9363788ED6D6"
   codebase="./LiteAVAX.cab#version=1,0,0,1" width="640" height="480">
</object>

<!-- 调用pusher对象方法 >
<script>
  function setRenderWndSize() {
      var vW = 640;
      var vH = 480;
      pusher.setRenderWndSize(vW, vH );	
  }
</script>
```

## 接口列表

| 名称                                       | 描述                          |
| ---------------------------------------- | --------------------------- |
| getVersion()                             | 获取插件SDK版本号                  |
| setRenderWndSize(width, height)          | 设置当前视频渲染窗口的大小，              |
| enumCameras():                           | 枚举当前的摄像头，                   |
| startCameraPreview()         | 启动摄像头预览                     |
| stopPreview()                            | 关闭摄像头预览                     |
| startPush(sUrl)                          | 启动推流                        |
| stopPush()                               | 停止推流                        |
| switchCamera(cameraIndex)                | 切换摄像头，支持在推流中动态切换，           |
| setMute(bMute)                           | 静音接口                        |
| setRenderMode(modeType)                  | 设置图像的渲染（填充）模式               |
| setRotation(rotationType )               | 设置图像的顺时针旋转角度                |
| setVideoResolution(resolutionType )      | 设置视频分辨率                     |
| setBeautyStyle(beautyStyle , beautyLevel, whitenessLevel) | 设置美颜和美白效果                   |
| setRenderYMirror(bMirror)                | 设置预览渲染的镜像效果                 |
| setOutputYMirror(bMirror)                | 设置推流画面的镜像效果                 |
| setVideoBitRate(bitrate)                 | 设置视频码率                      |
| setAutoAdjustStrategy(adjuststrategy  )  | 设置流控策略                      |
| setVideoBitRateMin(videoBitrateMin)      | 配合 setAutoAdjustStrategy 使用 |
| setVideoBitRateMax(videoBitrateMax)      | 配合 setAutoAdjustStrategy 使用 |
| setVideoFPS(fps)                         | 设置视频帧率                      |
| openSystemVoiceInput(bOpen)                          | 系统混音开关接口                        |
| startScreenPreview(x,y,width,height)                          | 屏幕捕捉预览接口                        |
| setPauseVideo(bPause)                   | 推流过程中暂停视频，目前是以黑色替换  |
| startAudioCapture()                          | 启动音频采集                        |
| stopAudioCapture()                          | 停止音频采集                        |
| setPusherEventCallBack(callbackfun, objectid) | 设置回调接口                      |
| captureVideoSnapShot(sFileFullPath,sDirPath) | 推流端视频图像快照                      |

### 1.getVersion()

获取插件版本号，和标签 &lt;object ... codebase='...&version=1.0.0.1'&gt; 上的 version 对应。

- **返回值说明**

| 参数   | 类型     | 说明          |
| ---- | ------ | ----------- |
| vRet | String | 版本号:x.x.x.x |

- **示例代码** : 

```
var vVersionString = pusher.getVersion()
```

### 2.setRenderWndSize()

设置当前视频渲染窗口的大小，需要和标签 &lt;object ... width="x", height="x" /&gt;  上的 width 和 height 值对齐。启动推拉流前设置。

- **参数说明**

| 参数     | 类型   | 说明     |
| ------ | ---- | ------ |
| width  | Int  | 视频窗口的长 |
| height | Int  | 视频窗口的宽 |

- **示例代码** : 

```
function setRenderWndSize() {
	var vW = 640;
	var vH = 480;
	pusher.setRenderWndSize(vW, vH );	
}
```

### 3.enumCameras()
枚举当前的摄像头，推流前需要检查当前 PC 是否安装了摄像头，以及安装了几个摄像头。

- **返回值说明**

| 参数       | 类型     | 说明          |
| -------- | ------ | ----------- |
| vRetJson | String | Json格式摄像头列表 |

- **vRetJson样式**
  - camera_cnt :  Int（摄像头个数）
  - cameralist  :   List（摄像头列表）
    - camera_name : String（像头名称）
    - id :  Int （摄像头编号，注意设置可用摄像头时，是设置编号，参考switchCamera接口）
  - 示例 "{\"camera_cnt\":1,\"cameralist\":[{\"camera_name\":\"HD Pro Webcam C920\",\"id\":\"0\"}]}"
- **示例代码** : 

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
        alert("无可用摄像头");
    }
}
```

### 4.startCameraPreview()

启动摄像头预览，接口调用成功（>0） or 失败（0）

- **返回值说明**

| 参数   | 类型   | 说明       |
| ---- | ---- | -------- |
| vRet | Int  | 0失败，>0成功 |

- **示例代码** : 

```
var vRetInt = pusher.startCameraPreview()
```

### 5.stopPreview()

关闭摄像头预览，stopPush 之前调用此函数并不会停止推流，而是让 SDK 只推送音频。

- **示例代码** : 

```
pusher.stopPreview()
```

### 6.startPush(sUrl)

启动推流 (在 startPush 之前需要先 检测查摄像头，否则推流可能失败),

- **参数说明**
  一个合法的推流地址，支持 rtmp 协议（URL 以 “rtmp://” 打头 ，腾讯云推流 URL 的获取方法见 [DOC]( https://cloud.tencent.com/document/product/454/7915)  

| 参数   | 类型     | 说明   |
| ---- | ------ | ---- |
| sUrl | String | 推流链接 |

- **返回值说明**
  成功 or 失败，内存分配、资源申请失败等原因可能会导致返回失败
| 参数   | 类型   | 说明       |
| ---- | ---- | -------- |
| vRet | Int  | 0失败，>0成功 |

- **示例代码** : 

```
function doStartPush(sUrl) {
	var vRetInt = pusher.startPush(sUrl);	
}
```

### 7.stopPush()

停止推流，注意推流 URL 有排他性，也就是一个推流 Url 同时只能有一个推流端向上推流

- **示例代码** : 

```
pusher.stopPush()
```

### 8.switchCamera(cameraIndex)

切换摄像头，支持在推流中动态切换，cameraIndex 可以通过 enumCameras 函数获取。

- **参数说明**

| 参数          | 类型   | 说明                     |
| ----------- | ---- | ---------------------- |
| cameraIndex | Int  | 摄像头编号，默认值-1，第一个摄像头值为0， |

- **示例代码** : 

```
function switchCameraSelect() {
    var obj = document.getElementById('cameralistselect');
    var index = obj.selectedIndex; //序号，取当前选中选项的序号  
    var val = obj.options[index].value;
    pusher.switchCamera(parseInt(val));
}
```

### 8.setMute(bMute)

关闭麦克风，SDK 会停止采集麦克风的数据，当用户不希望自己的声音被对方听到时，可以使用这个功能。

- **参数说明**

| 参数    | 类型   | 说明             |
| ----- | ---- | -------------- |
| bMute | Int  | 是否静音， 0非静音，1静音 |

- **示例代码** : 

```
function setMute() {
    pusher.setMute(1);
}
```

### 9.setRenderMode(modeType)

设置图像的渲染（填充）模式

- **参数说明**

| 参数       | 类型   | 说明                                       |
| -------- | ---- | ---------------------------------------- |
| modeType | Int  | 值为 1：适应，此模式下会显示整个画面的全部内容，但可能有黑边的存在<br/>值为 2：填充，此模式下画面无黑边，但是会裁剪掉一部分超出渲染区域的部分，裁剪<br/>更多可参考：AxTXERenderMode定义 |

- **示例代码** : 

```
function setRenderMode() {
    pusher.setRenderMode(AxTXERenderMode.AX_TXE_RENDER_MODE_ADAPT);
}
```

### 10.setRotation(rotationType )

设置图像的顺时针旋转角度

- **参数说明**

| 参数           | 类型   | 说明                                       |
| ------------ | ---- | ---------------------------------------- |
| rotationType | Int  | 值为 1：保持原图像的角度<br/>值为 2：顺时针旋转90度，最终图像的宽度和高度互换<br/>值为 3 ： 顺时针旋转180度，最终图像颠倒<br/>值为 4 ： 顺时针旋转270度，最终图像的宽度和高度互换<br/>更多可参考:AxTXEVideoRotation定义 |

- **示例代码** : 

```
function setRotation() {
    pusher.setRotation(AxTXEVideoRotation.AX_TXE_VIDEO_ROTATION_NONE);
}
```

### 11.setVideoResolution( )

设置视频分辨率，和码率配合使用，比如 640x360 配合 800kbps 的视频码率，320x240配合 400kbps的视频码率。

- **参数说明**

| 参数           | 类型 | 说明                                                         |
| -------------- | ---- | ------------------------------------------------------------ |
| resolutionType | Int  | 值为 1 ： RESOLUTION_320x240<br/>值为 2 ： RESOLUTION_640x480 <br/>值为 3 ：  RESOLUTION_480x272<br/>值为 4 ： RESOLUTION_960x720<br/>更多可参考:AxTXEVideoResolution定义 |

- **示例代码** : 

```
function setVideoResolution() {
    pusher.setVideoResolution(AxTXEVideoResolution.AX_TXE_VIDEO_RESOLUTION_320x240);
}
```

### 12.setBeautyStyle

设置美颜和美白效果

- **参数说明**

| 参数             | 类型   | 说明                                       |
| -------------- | ---- | ---------------------------------------- |
| beautyStyle    | Int  | 值为 1 ： 光滑<br/>值为 2 ： 自然<br/>值为 3 ： 朦胧<br/>更多可参考:AxTXEBeautyStyle定 |
| beautyLevel    | Int  | 美颜级别取值范围 1 ~ 9； 0 表示关闭，1 ~ 9值越大，效果越明显    |
| whitenessLevel | Int  | 美白级别取值范围 1 ~ 9； 0 表示关闭，1 ~ 9值越大，效果越明显    |

- **示例代码** : 

```
function setBeautyStyle() {
	var vlBeautyLevel = 5;
	var vlWhitenessLevel = 6;
    pusher.setBeautyStyle(AxTXEBeautyStyle.AX_TXE_BEAUTY_STYLE_SMOOTH, vlBeautyLevel, vlWhitenessLevel );
}
```

### 13.setRenderYMirror(bMirror)

设置预览渲染的镜像效果，ActiveX导出接口没有Boolean类型，用Int代替。

- **参数说明**

| 参数      | 类型   | 说明                |
| ------- | ---- | ----------------- |
| bMirror | Int  | 1表示画面左右反转，0表示保持原样 |

- **示例代码** : 

```
function setRenderYMirror() {
    pusher.setRenderYMirror(1);
}
```

### 14.setOutputYMirror(bMirror)

设置推流画面的镜像效果，ActiveX导出接口没有Boolean类型，用Int代替。

- **参数说明**

| 参数      | 类型   | 说明                |
| ------- | ---- | ----------------- |
| bMirror | Int  | 1表示画面左右反转，0表示保持原样 |

- **示例代码** : 

```
function setOutputYMirror() {
    pusher.setOutputYMirror(1);
}
```

### 15.setVideoBitRate(bitrate)

设置视频码率，注意，不是分辨率越高画面越清晰，是码率越高画面越清晰

- **参数说明**

| 参数      | 类型   | 说明                                       |
| ------- | ---- | ---------------------------------------- |
| bitrate | Int  | 视频码率，单位 kbps， 比如 640x360 分辨率需要配合 800kbps 的视频码率 |

- **示例代码** : 

```
function setVideoBitRate() {
    pusher.setVideoBitRate(500);
}
```

### 16.setAutoAdjustStrategy(adjuststrategy )

设置流控策略，即是否允许 SDK 根据当前网络情况调整视频码率，以避免网络上传速度不足导致的画面卡顿

- **参数说明**

| 参数             | 类型   | 说明                                       |
| -------------- | ---- | ---------------------------------------- |
| adjuststrategy | Int  | 值为 -1 ：无流控，恒定使用 setVideoBitRate 指定的视频码率<br/>值为 0 ：  适用于普通直播推流的流控策略，该策略敏感度比较低，会缓慢适应带宽变化，有利于在带宽波动时保持画面的清晰度。<br/>值为 1 ： 适用于普通直播推流的流控策，差别是该模式下 SDK 会根据当前码率自动调整出适合的分辨率<br/> 值为 5 ： 适用于实时音视频通话的流控策略, 该策略敏感度比较高，网络稍有风吹草动就会进行自适应调整<br/>更多可参考:AxTXEAutoAdjustStrategy定义 |

- **示例代码** : 

```
function setAutoAdjustStrategy() {
    pusher.setAutoAdjustStrategy(AxTXEAutoAdjustStrategy.TXE_AUTO_ADJUST_NONE);
}
```

### 17.setVideoBitRateMin & setVideoBitRateMax

配合 setAutoAdjustStrategy 使用，当 AutoAdjust 策略指定为 TXE_AUTO_ADJUST_NONE 时，如下的两个函数调用均视为无效

- **参数说明**

| 参数              | 类型   | 说明                                       |
| --------------- | ---- | ---------------------------------------- |
| videoBitrateMin | Int  | 允许 SDK 输出的最小视频码率，比如 640x360 分辨率下这个值适合设置为 300kbps |
| videoBitrateMax | Int  | 允许 SDK 输出的最小视频码率, 比如 640x360 分辨率下这个值适合设置为 1000kbps |

- **示例代码** : 

```
function setVideoBitRateMin() {
    pusher.setVideoBitRateMin(300);
}
```

### 18.setVideoFPS(fps)

设置视频帧率，请注意：这里的 fps 只是设置最大帧率，具体视频画面的帧率还是由摄像头本身的采集帧率所决定的，不同的摄像头支持的最大帧率有所不同。

- **参数说明**

| 参数   | 类型   | 说明                      |
| ---- | ---- | ----------------------- |
| fps  | Int  | fps - 视频帧率，默认值为15，重启后生效 |

- **示例代码** : 

```
function setVideoFPS() {
    pusher.setVideoFPS(15);
}
```

### 19.openSystemVoiceInput(bOpen)

系统混音接口，推流成功后调用，如果打开开关，系统所有的声音被会被采集并和麦克风混音输出，

- **参数说明**

| 参数   | 类型     | 说明   |
| ---- | ------ | ---- |
| bOpen | Int  | 1表示打开，0表示关闭，默认为0|

- **示例代码** : 

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

### 20.startScreenPreview(x,y,width,height)

屏幕录制，指定区域，或者全部输入0时，录制整个主屏幕

- **参数说明**

| 参数   | 类型     | 说明   |
| ---- | ------ | ---- |
| x | Int  | 左边原点位置|
| y | Int  | 右边原点位置|
| width | Int  | 录屏的长|
| height | Int  | 录屏的宽|

- **示例代码** : 

```
function startScreenPreview() {
	 pusher.startScreenPreview(0,0,0,0);
}
```

### 21.captureVideoSnapShot(sFileFullPath,sDirPath)

推流端视频图像快照，以sFileFullPath路径存储，如果sFileFullPath为""，则会写在temp目录下，目前只支持.jpg的文件格式

- **参数说明**

| 参数   | 类型     | 说明   |
| ---- | ------ | ---- |
| sFileFullPath | String  | 指定存储文件路径，不为null，则直接存储文件|
| sDirPath | String  | 预留参数 |


- **返回值说明**
  成功 or 失败，文件存在、创建文件失败等
| 参数   | 类型   | 说明       |
| ---- | ---- | -------- |
| vRet | Int  | -1:失败，-2路径非法，-3文件存在，-4未推流 |

- **示例代码** : 

```
function screenShotPusher() {
	//第一个参数指定文件， 第二个参数指定路径，如果不需要指定文件，则""
    //var ret = pusher.captureVideoSnapShot("", "");
    var ret = pusher.captureVideoSnapShot("D:\\subTest\\123.jpg", "");
    //-1:失败，-2路径非法，-3文件存在，-4未推流
    if (ret == -1) {
        alert("截图失败");
    }
    else if (ret == -2) {
        alert("路径非法");
    }
    else if (ret == -3) {
        alert("文件存在");
    }
    else if (ret == -4) {
        alert("未推流");
    }
}
```

### 22.setPauseVideo(bPause)

推音视频流过程中，暂停视频，目前是以黑色背景替换

- **参数说明**

| 参数   | 类型     | 说明   |
| ---- | ------ | ---- |
| bOpen | Int  | 1表示打开，0表示关闭，默认为0|

- **示例代码** : 

```
function doPauseVideo(bPause) {
     pusher.setPauseVideo(bPause);
}
```

### 23.startAudioCapture()

启动音频采集

- **示例代码** : 

```
function startAudioCapture(targetURL) {
	   //启动音频推流，没有视频
     pusher.startAudioCapture();
		 pusher.startPush(targetURL);
}
```

### 24.stopAudioCapture()

停止音频采集

- **示例代码** : 

```
function stopAudioCapture() {
	   //启动音频推流，没有视频
     pusher.stopAudioCapture();
}
```

### 25.setPusherEventCallBack(callbackfun, objectid)

设置事件回调，用于接收在推流过程中 SDK 所抛出的各种事件，事件列表详见文档接下来的部分。

- **参数说明**

| 参数          | 类型   | 说明     |
| ----------- | ---- | ------ |
| callbackfun | Func | 回调函数   |
| objectid    | Int  | 回调对象ID |

- **paramJson样式**[回调参数JSON格式]
  - eventId :  Int  （事件ID，参考PusherCallBackEvent定义）
  - objectId  :   Int（和setPusherEventCallBack::objectid一致）
  - paramCnt  :   Int（JSON携带的Key-Value键值对个数）
  - paramlist  :   List（键值对String）推流成功后，实时回调流状态信息
    - key : String
    - value:  String 
  - 【paramlist:List】的示例 {"eventId":200001,"objectId":1,"paramCnt":9,"paramlist":[{"key":"AUDIO_BITRATE","value":"0"},{"key":"CACHE_SIZE","value":"571"},{"key":"CODEC_CACHE","value":"329"},{"key":"NET_SPEED","value":"0"},{"key":"SERVER_IP","value":""},{"key":"VIDEO_BITRATE","value":"0"},{"key":"VIDEO_FPS","value":"14"},{"key":"VIDEO_HEIGHT","value":"240"},{"key":"VIDEO_WIDTH","value":"320"}]} 
  
- 示例代码** : 

```javascript
//推流前调用。
pusher.setPusherEventCallBack(PusherEventListener, 1);

var PusherEventListener = function (paramJson) {
    var obj = JSON.parse(paramJson);
    if (parseInt(obj.eventId) == 1002 && parseInt(obj.objectId) == 1) {
    	alert("推流成功");
    }
    else if (parseInt(obj.eventId) == -1307 && parseInt(obj.objectId) == 1) {
    	alert("网络断开，经过多次重试推流无效，请重新推流");
    }
    else if (parseInt(obj.eventId) == 200001 && parseInt(obj.objectId) == 1) {
        doUpdatePluserStatusInfo(paramJson);
    }
};

function doUpdatePusherStatusInfo(paramJson) {
    //paramJson 参考 【paramlist:List（键值对String）】里面的示例
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

## 事件列表

### 1. 常规事件

| 事件ID                         | 数值   | 含义说明           |
| ---------------------------- | ---- | -------------- |
| PUSH_EVT_CONNECT_SUCC        | 1001 | 已经连接推流服务器        |
| PUSH_EVT_PUSH_BEGIN          | 1002 | 已经与服务器握手完毕,开始推流   |
| PUSH_EVT_OPEN_CAMERA_SUCC    | 1003 | 打开摄像头成功 |
| PUSH_EVT_CHANGE_RESOLUTION   | 1005 | 推流动态调整分辨率         |
| PUSH_EVT_CHANGE_BITRATE      | 1006 | 推流动态调整码率         |
| PUSH_EVT_FIRST_FRAME_AVAILABLE  | 1007 | 首帧画面采集完成         |
| PUSH_EVT_START_VIDEO_ENCODER | 1008 | 编码器启动    |
| PUSH_EVT_CAMERA_REMOVED      | 1009 | 摄像头设备已被移出         |
| PUSH_EVT_CAMERA_AVAILABLE    | 1010 | 摄像头设备重新可用        |
| PUSH_EVT_CAMERA_CLOSED       | 1011 | 关闭摄像头完成        |
| PUSH_EVT_SNAPSHOT_RESULT       | 1012 | 截图快照返回码        |

### 2. 错误通知

SDK发现了一些严重问题，推流无法继续了，比如Camera已被其他程序占用导致摄像头打不开。

| 事件ID                            | 数值    | 含义说明                               |
| ------------------------------- | ----- | ---------------------------------- |
| PUSH_ERR_OPEN_CAMERA_FAIL       | -1301 | 打开摄像头失败                            |
| PUSH_ERR_OPEN_MIC_FAIL          | -1302 | 打开麦克风失败                            |
| PUSH_ERR_VIDEO_ENCODE_FAIL      | -1303 | 视频编码失败                             |
| PUSH_ERR_AUDIO_ENCODE_FAIL      | -1304 | 音频编码失败                             |
| PUSH_ERR_UNSUPPORTED_RESOLUTION | -1305 | 不支持的视频分辨率                          |
| PUSH_ERR_UNSUPPORTED_SAMPLERATE | -1306 | 不支持的音频采样率                          |
| PUSH_ERR_NET_DISCONNECT         | -1307 | 网络断连,且经多次重连抢救无效,可以放弃治疗,更多重试请自行重启推流 |
| PUSH_ERR_CAMERA_OCCUPY          | -1308 | 摄像头正在被占用中，可尝试打开其他摄像头               |


### 3. 警告事件

SDK发现了一些问题，但这并不意味着无可救药，很多 WARNING 都会触发一些重试性的保护逻辑或者恢复逻辑，而且有很大概率能够恢复，所以，千万不要“小题大做”哦。

**WARNING_NET_BUSY**
主播网络不给力，如果您需要UI提示，这个 warning 相对比较有用。

**WARNING_SERVER_DISCONNECT**
推流请求被后台拒绝了，出现这个问题一般是由于推流地址里的 txSecret 计算错了，或者是推流地址被其他人占用了（一个推流URL同时只能有一个端推流）。

| 事件ID                                     | 数值   | 含义说明                            |
| ---------------------------------------- | ---- | ------------------------------- |
| PUSH_WARNING_NET_BUSY                    | 1101 | 网络状况不佳：上行带宽太小，上传数据受阻            |
| PUSH_WARNING_RECONNECT                   | 1102 | 网络断连, 已启动自动重连 (自动重连连续失败超过三次会放弃) |
| PUSH_WARNING_HW_ACCELERATION_FAIL        | 1103 | 硬编码启动失败，采用软编码                   |
| PUSH_WARNING_VIDEO_ENCODE_FAIL           | 1104 | 视频编码失败,非致命错,内部会重启编码器            |
| PUSH_WARNING_BEAUTYSURFACE_VIEW_INIT_FAIL | 1105 | 视频编码码率异常，警告                     |
| PUSH_WARNING_VIDEO_ENCODE_BITRATE_OVERFLOW | 1106 | 视频编码码率异常，警告                     |
| PUSH_WARNING_DNS_FAIL                    | 3001 | RTMP -DNS解析失败 （会触发重试流程）         |
| PUSH_WARNING_SEVER_CONN_FAIL             | 3002 | RTMP服务器连接失败 （会触发重试流程）           |
| PUSH_WARNING_SHAKE_FAIL                  | 3003 | RTMP服务器握手失败 （会触发重试流程）           |
| PUSH_WARNING_SERVER_DISCONNECT           | 3004 | RTMP服务器主动断开，请检查推流地址的合法性或防盗链有效期  |
| PUSH_WARNING_SERVER_NO_DATA              | 3005 | 超过30s没有数据发送，主动断开连接              |


## 枚举类型

### AxTXERenderMode 

- 渲染窗口的渲染方式：4:3的窗口，渲染16:9视频
  var AxTXERenderMode = {
  AX_TXE_RENDER_MODE_ADAPT : 1,              // 适应，此模式下会显示整个画面的全部内容，但可能有黑边的存在
  AX_TXE_RENDER_MODE_FILLSCREEN : 2,      // 填充，此模式下画面无黑边，但是会裁剪掉一部分超出渲染区域的部分，裁剪模式为局中裁剪
  };

### AxTXEVideoRotation 

- 渲染视频旋转
  var  AxTXEVideoRotation =  {
  AX_TXE_VIDEO_ROTATION_NONE : 1,            // 保持原图像的角度
  AX_TXE_VIDEO_ROTATION_90 : 2,              // 顺时针旋转90度，最终图像的宽度和高度互换
  AX_TXE_VIDEO_ROTATION_180 : 3,             // 顺时针旋转180度，最终图像颠倒
  AX_TXE_VIDEO_ROTATION_270 : 4,             // 顺时针旋转270度，最终图像的宽度和高度互换
  };

### AxTXEVideoResolution 

- 推流视频分辨率
  var AxTXEVideoResolution = {
  // 普屏 4:3
  AX_TXE_VIDEO_RESOLUTION_320x240 : 1,
  AX_TXE_VIDEO_RESOLUTION_480x360 : 2,
  AX_TXE_VIDEO_RESOLUTION_640x480 : 3,
  AX_TXE_VIDEO_RESOLUTION_960x720 : 4,
   // 宽屏3:4
  AX_TXE_VIDEO_RESOLUTION_240x320 : 50,
  AX_TXE_VIDEO_RESOLUTION_360x480 : 51,
  AX_TXE_VIDEO_RESOLUTION_480x640 : 52,
  AX_TXE_VIDEO_RESOLUTION_720x960 : 53,

  // 宽屏16:9
  AX_TXE_VIDEO_RESOLUTION_320x180 : 101,
  AX_TXE_VIDEO_RESOLUTION_480x272 : 102,
  AX_TXE_VIDEO_RESOLUTION_640x360 : 103,
  AX_TXE_VIDEO_RESOLUTION_960x540 : 104,
  // 宽屏9:16
  AX_TXE_VIDEO_RESOLUTION_180x320 : 201,
  AX_TXE_VIDEO_RESOLUTION_272x480 : 202,
  AX_TXE_VIDEO_RESOLUTION_360x640 : 203,
  AX_TXE_VIDEO_RESOLUTION_540x960 : 204,

  };

### AxTXEBeautyStyle 

- 设置美颜风格
  var AxTXEBeautyStyle = {
  AX_TXE_BEAUTY_STYLE_SMOOTH : 0,        // 光滑
  AX_TXE_BEAUTY_STYLE_NATURE : 1,        // 自然
  AX_TXE_BEAUTY_STYLE_BLUR : 2,        // 朦胧
  };
