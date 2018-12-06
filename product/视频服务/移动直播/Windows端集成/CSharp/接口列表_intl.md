# API List

## API Document

[Download](https://cloud.tencent.com/document/product/454/7873#Windows) SDK from the Tencent Cloud official website to view the API comments under SDK\include.

The following lists the APIs of Tencent Video Cloud Windows SDK (C++), which are categorized into TXLivePusher and TXLivePlayer APIs, as well as relevant enums and global constants.



## TXLivePusher

##### APIs

| Name | Description |
| --------------------------------------------------------- | ------------------------------------------------------------ |
| setCallback(callback, pUserData)                  | Sets the callback proxy of TXLivePusher |
| enumCameras(camerasName, capacity)  | Enumerates current cameras |
| micDeviceCount()       | Queries the number of available microphones |
| micDeviceName(index,  name[])     | Queries the names of microphones |
| selectMicDevice(index)     | Selects the specified microphone as the recording device |
| micVolume()      | Queries the volume of the selected microphone |
| setMicVolume(volume)       | Sets the volume of the selected microphone |
| enableMic(enable)        | Indicates whether to enable microphone (used with audio mixing) |
| openSystemVoiceInput(szPlayerPath )  | Enables system sound capture |
| closeSystemVoiceInput()     | Disables system sound capture |
| setSystemVoiceInputVolume(value)    | Sets the volume for system sound capture |
| startAudioCapture(srcType)      | Enables audio capture 
| stopAudioCapture()          | Disables audio capture |
| startPreview(rendHwnd, rect, cameraIndex)    | Enables camera preview 
| startPreview(srcType,rendHwnd,rect,dataFormat)   | Enables video preview, including screencap, camera and external data sources |
| updatePreview(rendHwnd, rect)      | Resets camera preview area |
| stopPreview()         | Disables camera preview |
| enumCaptureWindow(windowArray, capacity)   | Enumerates windows available for capture |
| setScreenCaptureParam(captureHwnd, rect)    | Sets screen capture parameters |
| captureVideoSnapShot(filePath, length)    | Captures screenshots of the pushed images and saves to local device |
| startPush(url)        | Start push |
| stopPush()      | Stops push |
| switchCamera(cameraIndex)    | Switches between cameras. Dynamic switching during push is supported. |
| setMute(mute)      | Enables Mute |
| setRenderMode(mode)    | Sets the rendering (fill) mode of image |
| setRotation(rotation)     | Sets the clockwise rotation of image |
| setVideoQualityParamPreset(paramType)    | Sets the preset options for pushed image quality |
| setVideoResolution(resolution)     | Sets video resolution |
| setBeautyStyle(beautyStyle , beautyLevel, whitenessLevel) |Sets beauty filter and whitening effects |
| setRenderYMirror(bMirror)   | Sets the mirroring effect for preview rendering |
| setOutputYMirror(bMirror)   | Sets the mirroring effect of pushed images |
| setVideoBitRate(bitrate)    | Sets video bitrate |
| setAutoAdjustStrategy(adjuststrategy  )   | Sets traffic control policy |
| setVideoBitRateMin(videoBitrateMin)     | The minimum video bitrate of SDK output (used with setAutoAdjustStrategy) |
| setVideoBitRateMax(videoBitrateMax)  | The maximum video bitrate of SDK output (used with setAutoAdjustStrategy) |
| setVideoFPS(fps)     | Sets video frame rate |
| setPauseVideo(bPause)       | Sets video pause |



## TXLivePlayer

##### APIs

| Name | Description |
| ------------------------------------- | -------------------- |
| setCallback(callback, pUserData)  | Sets the callback proxy of TXLivePlayer |
| speakerDeviceCount()  | Queries the number of available speakers |
| speakerDeviceName(index, name) | Queries the names of speakers |
| selectSpeakerDevice(index)   | Selects the specified speaker as the audio playback device |
| speakerVolume()     | Queries the volume for SDK playback |
| setSpeakerVolume(volume)       | Sets the volume for SDK playback |
| setRenderFrame(hWnd, rect)  | Sets video image rendering attributes |
| updateRenderFrame(hWnd, rect)   | Resets image rendering area |
| closeRenderFrame()  | Disables image rendering |
| startPlay(url, type) | Starts playback |
| stopPlay()        | Stops playback |
| pause()      | Pauses playback |
| resume()      | Resumes playback |
| isPlaying()       | Indicates whether the playback is in progress |
| setMute(mute)    | Enables Mute |
| setRenderMode(mode)    | Sets the rendering (fill) mode of image |
| setRotation(TXEVideoRotation)   | Sets the clockwise rotation of image |
| setRenderYMirror(mirror)   | Sets the mirroring effect for rendering |
| setOutputVideoFormat(format)  | Sets the video encoding format |
| captureVideoSnapShot(filePath,length)| Captures screenshots of the pulled images and saves to local device |



## Details of TXLivePusher APIs

#### 1.setCallback(callback, pUserData)

API details: void setCallback(callback, pUserData)
Sets the callback proxy of TXLivePusher for listening on push events.

- **Parameter description**

| Parameter | Type | Description |
| --------- | ---------------------- | ---------------------------------- |
| callback  | TXLivePusherCallback *| Proxy pointer |
| pUserData | void *  | Transparently transfers user data to the callback function of TXLivePusherCallback |

- **Sample code**: 

```
pusher.setCallback(this, reinterpret_cast<void*>(index));
```



#### 2.enumCameras(camerasName, capacity)

API details: int enumCameras(camerasName, capacity)

Enumerates current cameras. If multiple cameras are installed on a Windows machine, you can use this function to get the number and names of the available cameras.

- **Parameter description**

| Parameter | Type | Description |
| ----------- | ---------- | ----------------- |
| camerasName | wchar_t ** | Camera names |
| capacity    | size_t   | Size of camerasName array |

- **Sample code**: 

```
m_cameraCount = pusher.enumCameras();
wchar_t **camerasName = new wchar_t *[m_cameraCount];
for (int i = 0; i < m_cameraCount; ++i)
{
	camerasName[i] = new wchar_t[256];
}
pusher.enumCameras(camerasName, m_cameraCount);
```



#### 3. micDeviceCount()

API details:  int micDeviceCount() const

Queries the number of available microphones.

- **Returned result**

| Parameter | Type | Description |
| ---- | ---- | ----- |
| vRet | int | Number of microphones |

- **Sample code**: 

```
int ret = pusher.micDeviceCount();
```



#### 4. micDeviceName(index,name)

API details: bool micDeviceName(unsigned int index, char name[SPEAKER_DEVICE_NAME_MAX_SIZE])

Queries the names of microphones.

- **Parameter description**

| Parameter | Type | Description |
| ----- | ------ | ------------------ |
| index | int | Index of microphone |
| name | char[] | A string array of microphone names |

- **Sample code**: 

```
int index = 0;
char name[SPEAKER_DEVICE_NAME_MAX_SIZE];
pusher.micDeviceName(index, name);
```



#### 5. selectMicDevice(index)

API details:  void selectMicDevice(unsigned int index)

Selects the specified microphone as the audio recording device. When this API is not called, the microphone with index 0 is selected by default.

- **Parameter description**

| Parameter | Type | Description |
| ----- | ---- | -------- |
| index | int | Index of microphone |

- **Sample code**: 

```
int index = 0;
pusher.selectMicDevice(index);
```



#### 6. micVolume()

API details: unsigned int micVolume()

Queries the volume of the selected microphone.

- **Returned result**

| Parameter | Type | Description |
| ---- | ---- | ------------------ |
| vRet | int | Volume value, which ranges from 0 to 65535. |

- **Sample code**: 

```
int ret = pusher.micVolume();
```



#### 7. setMicVolume(volume)

API details:  void setMicVolume(unsigned int volume)

Sets the volume of the selected microphone.

- **Parameter description**

| Parameter | Type | Description |
| ------ | ---- | --------------------- |
| volume | int | The volume you set, which ranges from 0 to 65535. |

- **Sample code**: 

```
int volume = 100;
pusher.setMicVolume(volume);
```



#### 8. enableMic(enable)

API details: void enableMic(bool enable)

Indicates whether to enable microphone.

- **Parameter description**

| Parameter | Type | Description |
| ------ | ---- | ------------------------------------------- |
| enable | bool | false: Disable microphone capture; true: Enable microphone capture |

- **Sample code**: 

```
pusher.enableMic(true);
```



#### 9. openSystemVoiceInput(szPlayerPath)

API details: void openSystemVoiceInput(const char* szPlayerPath)

Enables system or process sound input for mixing with the microphone sound input.

- **Parameter description**

| Parameter | Type | Description |
| ------------ | ------ | ---------------------------------------- |
| szPlayerPath | string | Player address. If this parameter is left empty or filled with null, all sounds in the system are captured. If the path of the exe program (e.g. Kugou Music or QQ Music) is entered, the program is started and only the sounds from the program are captured. \| |

- **Sample code**: 

```
pusher.openSystemVoiceInput(null);
```



#### 10. closeSystemVoiceInput()

API details: void closeSystemVoiceInput()

Disables system or process sound input for mixing.

- **Sample code**: 

```
pusher.closeSystemVoiceInput();
```



#### 11. setSystemVoiceInputVolume(value)

API details: void setSystemVoiceInputVolume(int value)

Sets the volume for system sound capture.

- **Parameter description**

| Parameter | Type | Description |
| ----- | ---- | ------------------- |
| value | int | Sets the volume you desired. The value ranges from 0 to 100. |

- **Sample code**: 

```
pusher.setSystemVoiceInputVolume(50);

```



#### 12. startAudioCapture(srcType)

API details: void startAudioCapture(TXEAudioCaptureSrcType srcType = TXE_AUDIO_SRC_SDK_DATA)

Enables audio capture. The SDK uses a sampling rate of 48 KHz and 16-bit mono channel to deliver a real-time audio effect with a low delay.

- **Parameter description**

| Parameter | Type | Description |
| ------- | ---- | -------------------------------- |
| srcType | enum | Audio data source: see the definition of TXEAudioCaptureSrcType. |

- **Sample code**: 

```
pusher.startAudioCapture(TXE_AudioSrc_Sdk_Data);
```



#### 13. stopAudioCapture()

API details: void stopAudioCapture()

Disables audio capture.

- **Sample code**: 

```
pusher.stopAudioCapture();
```



#### 14.startPreview(rendHwnd, rect, cameraIndex)

API details: bool startPreview(rendHwnd, rect, cameraIndex)
Enables camera preview. true: API call is successful; false: API call failed.

- **Parameter description**

| Parameter | Type | Description |
| ----------- | ------------ | ------------------- |
| rendHwnd | HWND | The HWND that identifies the preview window. |
| rect | const RECT & | Specifies the rendering area of the video image on the window identified by HWND. |
| cameraIndex | int | Specifies the camera for which the preview is to be enabled. |

- **Sample code**: 

```
pusher.startPreview(m_pushRender, m_pushRect, 0);
```



#### 15.startPreview(srcType,rendHwnd,rect,dataFormat)

API details: bool startPreview(TXEVideoCaptureSrcType srcType, HWND rendHwnd, const RECT &rect, TXEVideoUserDataFormat dataFormat)Enables the video source preview. The SDK supports various preview video sources, such as cameras and videos recorded by using screencap feature and videos specified by users. true: API call is successful; false: API call failed.

- **Parameter description**

| Parameter | Type | Description |
| ---------- | ------------ | ------------------------------------------------------------ |
| srcType | enum | Video source type. See the definition of TXEVideoCaptureSrcType. |
| rendHwnd | HWND | The HWND that identifies the preview window. |
| rect | const RECT & | Specifies the rendering area of the video image on the window identified by HWND. |
| dataFormat | enum | If srcType = TXE_VIDEO_SRC_USER_DATA, specifies the video format of the user data. See the definition of TXEVideoUserDataFormat. |

- **Sample code**: 

```

pusher.startPreview(TXE_VideoSrc_Sdk_Camera, m_pushRender, m_pushRect, TXE_UserData_Undefined);
```



#### 16.updatePreview(rendHwnd, rect)

API details: void updatePreview(rendHwnd, rect)
Resets the preview area for camera. When the size of the window identified by the specified HWND changes, you can resize the video rendering area using this function.

- **Parameter description**

| Parameter | Type | Description |
| -------- | ------------ | ------------------- |
| rendHwnd | HWND | The HWND that identifies the preview window. |
| rect | const RECT & | Specifies the rendering area of the video image on the window identified by HWND. |

- **Sample code**: 

```
pusher.updatePreview(m_pushRender, m_pushRect);
```



#### 17.stopPreview()

API details: void stopPreview()

Disables camera preview. Calling this function before calling stopPush does not stop the push, but can cause the SDK to only push audio data.

- **Sample code**: 

```
pusher.stopPreview();
```



#### 18.enumCaptureWindow(windowArray, capacity)

API details: static int enumCaptureWindow(HWND* windowArray,size_t capacity)

Enumerates the windows available for capture. If there are multiple windows on the desktop at the same time, this function obtains the handles and names of the windows that can be captured.

- **Parameter description**

| Parameter | Type | Description |
| ----------- | ------ | ---------------------------- |
| windowArray | HWND* | Array of handles and names of windows that can be captured |
| capacity | size_t | Size of the windowArray |

- **Sample code**: 

```

```

```
int iCntWnd = m_pusher.enumCaptureWindow();
```

```
HWND *hwndList = new HWND[iCntWnd];
pusher.enumCaptureWindow(hwndList, iCntWnd);
```



#### 19.setScreenCaptureParam(captureHwnd,rect)

API details: void setScreenCaptureParam(HWND captureHwnd, const RECT &rect)

Sets the screen area capture parameters. This API is called before startPreview(srcType = TXE_VIDEO_SRC_SDK_SCREEN..). The entire desktop is captured by default.

- **Parameter description**

| Parameter | Type | Description |
| ----------- | ---------- | ---------------------------------------- |
| captureHwnd | HWND | Specifies the window to be captured. If captureHwnd is not NULL, the window identified by it is captured as a whole, and the captureRect does not take effect. |
| rect | const RECT | Specifies the rectangle for capturing the area on main screen. It only takes effect when captureHwnd is NULL. When captureRect is {0}, the main screen is captured as a whole. |

- **Sample code**: 

```
pusher.setScreenCaptureParam(TXE_AudioSrc_Sdk_Data);
```



#### 20. captureVideoSnapShot(filePath,length)

API details: int captureVideoSnapShot(wchar_t * filePath, unsigned int length)

Captures screenshots of the pushed images and saves to local device

- **Parameter description**

| Parameter | Type | Description |
| -------- | ------------ | ----------------- |
| filePath | wchar_t * | File path. Only .jpg format is supported. |
| length | unsigned int | Length of filePath |

- **Sample code**: 

```
std::wstring path = L"D:\\132.jpg";
pusher.captureVideoSnapShot(path.c_str(), path.size());
```



#### 21.startPush(url)

API details: bool startPush(url)

Starts the push (you need to call startPreview to enable camera preview before calling startPush, otherwise only audio data is pushed)

Note: A push URL is exclusive, that is, a push URL can only be used by one pusher for pushing streams at a time.

true: API call is successful; false: API call failed. Memory allocation, resource request failure, and other reasons may result in the failure to return response.

- **Parameter description**

| Parameter | Type | Description |
| ---- | ------------ | ---------------------------------------- |
| url | const char * | A valid push URL that supports RTMP protocol. The URL starts with "rtmp://". For more information on how to obtain Tencent Cloud push URL, please see [DOC](https://cloud.tencent.com/document/product/454/7915 "腾讯云-推拉流地址Doc"). |

- **Sample code**: 

```
pusher.startPush(m_pushUrl.c_str());
```



#### 22.stopPush()

API details: void stopPush()

Stops push.

- **Sample code**: 

```
pusher.stopPush();
```



#### 23.switchCamera(cameraIndex)

API details: void switchCamera(cameraIndex)

Switches between cameras. Dynamic switching during push is supported.

- **Parameter description**

| Parameter | Type | Description |
| ----------- | ---- | ---------------------------- |
| cameraIndex | int | Camera index. Returned result: 0-(number of cameras-1) |

- **Sample code**: 

```
pusher.switchCamera(0);
```



#### 24.setMute(mute)

API details: void setMute(mute)

Enables Mute.

- **Parameter description**

| Parameter | Type | Description |
| ---- | ---- | ---- |
| mute | bool | Indicates whether to enable Mute |

- **Sample code**: 

```
pusher.setMute(true);
```



#### 25.setRenderMode(mode)

API details: void setRenderMode(mode)

Sets the rendering (fill) mode of image.

- **Parameter description**

| Parameter | Type | Description |
| ---- | ------------- | ---------------------------------------- |
| mode | TXERenderMode | See TXERenderMode's enumerated values defined in TXLiveSDKTypeDef.h |

- **Sample code**: 

```
pusher.setRenderMode(TXE_RENDER_MODE_ADAPT);
```



#### 26.setRotation(rotation )

API details: void setRotation(rotation)

Sets the clockwise rotation of image.

- **Parameter description**

| Parameter | Type | Description |
| -------- | ---------------- | ---------------------------------------- |
| rotation | TXEVideoRotation | See TXEVideoRotation's enumerated values defined in TXLiveSDKTypeDef.h |

- **Sample code**: 

```
pusher.setRotation(TXE_VIDEO_ROTATION_90);
```



#### 27.setVideoQualityParamPreset(paramType)

API details: void setVideoQualityParamPreset(TXEVideoQualityParamPreset paramType)

Sets the preset options for pushed image quality.

- **Parameter description**

| Parameter | Type | Description |
| --------- | -------------------------- | ---------------------------------------- |
| paramType | TXEVideoQualityParamPreset  | See TXEVideoQualityParamPreset's enumerated values defined in TXLiveSDKTypeDef.h |

- **Sample code**: 

```
pusher.setVideoQualityParamPreset(TXE_VIDEO_QUALITY_STANDARD_DEFINITION);
```



#### 28.setVideoResolution(resolution)

API details: void setVideoResolution(resolution)

Sets video resolution.

- **Parameter description**

| Parameter | Type | Description |
| ---------- | ------------------ | ---------------------------------------- |
| resolution | TXEVideoResolution  | See TXEVideoResolution's enumerated values defined in TXLiveSDKTypeDef.h |

- **Sample code**: 

```
pusher.setVideoResolution(TXE_VIDEO_RESOLUTION_640x480);
```



#### 29.setBeautyStyle(beautyStyle , beautyLevel, whitenessLevel)

API details: void setBeautyStyle(beautyStyle, beautyLevel, whitenessLevel)

Sets beauty filter and whitening effects.

- **Parameter description**

| Parameter | Type | Description |
| -------------- | -------------- | ---------------------------------------- |
| beautyStyle    | TXEBeautyStyle | See TXEBeautyStyle's enumerated values defined in TXLiveSDKTypeDef.h |
| beautyLevel | int | Beauty filter level: 1-9. 0 indicates disabling beauty filter. A greater value means a bigger effect. |
| whitenessLevel | Int | Whiteness level: 1-9. 0 indicates disabling whitening. A greater value means a bigger effect. |

- **Sample code**: 

```
pusher.setBeautyStyle(TXE_BEAUTY_STYLE_NATURE, 5, 5);
```



#### 30.setRenderYMirror(mirror)

API details: void setRenderYMirror(mirror)

Sets the mirroring effect for preview rendering.

- **Parameter description**

| Parameter | Type | Description |
| ------ | ---- | ------------------------ |
| mirror | bool | true: the image is mirrored horizontally; false: the image remains as it is. |

- **Sample code**: 

```
pusher.setRenderYMirror(true);
```



#### 31.setOutputYMirror(mirror)

API details: void setOutputYMirror(mirror)

Sets the mirroring effect of pushed image.

- **Parameter description**

| Parameter | Type | Description |
| ------ | ---- | ------------------------ |
| mirror | bool | true: the image is mirrored horizontally; false: the image remains as it is. |

- **Sample code**: 

```
pusher.setOutputYMirror(true);
```



#### 32.setVideoBitRate(bitrate)

API details: void setVideoBitRate(bitrate)

Sets video bitrate. Note: The higher the bitrate, the clearer the image is. But a higher resolution does not necessarily mean a higher image clarity.

- **Parameter description**

| Parameter | Type | Description |
| ------- | ------------- | ---------------------------------------- |
| bitrate | unsigned long | Video bitrate (in Kbps). For example, a resolution of 640x360 is used with a video bitrate of 800 Kbps. |

- **Sample code**: 

```
pusher.setVideoBitRate(800);
```



#### 33.setAutoAdjustStrategy(strategy)

API details: void setAutoAdjustStrategy(strategy)

Sets the traffic control policy, that is, whether to allow SDK to adjust the video bitrate to adapt to the network condition, so as to avoid the stutter caused by slow upload speed.

- **Parameter description**

| Parameter | Type | Description |
| -------- | --------------------- | ---------------------------------------- |
| strategy | TXEAutoAdjustStrategy | See TXEAutoAdjustStrategy's enumerated values defined in TXLiveSDKTypeDef.h |

- **Sample code**: 

```
pusher.setAutoAdjustStrategy(TXE_AUTO_ADJUST_REALTIME_VIDEOCHAT_STRATEGY);
```



#### 34.setVideoBitRateMin(videoBitrateMin) && setVideoBitRateMax(videoBitrateMax)

API details: void setVideoBitRateMin(videoBitrateMin)

​		   void setVideoBitRateMax(videoBitrateMax)

They are used with setAutoAdjustStrategy. If the AutoAdjust policy is specified as TXE_AUTO_ADJUST_NONE, calls of both of the functions are invalid.

- **Parameter description**

| Parameter | Type | Description |
| --------------- | ---- | ---------------------------------------- |
| videoBitrateMin | int | The minimum video bitrate of SDK output. For example, this parameter is set to 300 Kbps for a resolution of 640x360. |
| videoBitrateMax | int | The maximum video bitrate of SDK output. For example, this parameter is set to 1000 Kbps for a resolution of 640x360. |

- **Sample code**: 

```
pusher.setVideoBitRateMin(300);
pusher.setVideoBitRateMax(1000);
```



#### 35.setVideoFPS(fps)

API details: void setVideoFPS(fps)

Sets video frame rate.

- **Parameter description**

| Parameter | Type | Description |
| ---- | ------------- | ----------------- |
| fps | unsigned long | Video frame rate, which takes effect after restart. Default: 15. |

- **Sample code**: 

```
pusher.setVideoFPS(15);
```



#### 36.setPauseVideo(bPause)

API details: void setPauseVideo(bool bPause)

Sets video frame rate.

- **Parameter description**

| Parameter | Type | Description |
| ------ | ---- | -------- |
| bPause | bool | Indicates whether to pause the video. |

- **Sample code**: 

```
pusher.setPauseVideo(true);
```

## 

## TXLivePlayer Object APIs

#### 1.setCallback(callback, pUserData)

API details: void setCallback(callback, pUserData)
Sets the callback proxy of TXLivePlayer for listening on push events.

- **Parameter description**

| Parameter | Type | Description |
| --------- | ---------------------- | ---------------------------------- |
| callback  | TXLivePlayerCallback * | Proxy pointer |
| pUserData | void *  | Transparently transfers user data to the callback function of TXLivePlayerCallback |

- **Sample code**: 

```
player.setCallback(this, reinterpret_cast<void*>(index));
```



#### 2. speakerDeviceCount()

API details: int speakerDeviceCount() const

Queries the number of available speakers.

- **Returned result**

| Parameter | Type | Description |
| ---- | ---- | ----- |
| vRet | int | Number of speakers |

- **Sample code**: 

```
int ret = player.speakerDeviceCount();
```



#### 3. speakerDeviceName(index,name)

API details: bool speakerDeviceName(unsigned int index, char name[SPEAKER_DEVICE_NAME_MAX_SIZE])

Queries the names of speakers.

- **Parameter description**

| Parameter | Type | Description |
| ----- | ------ | ------------------ |
| index | int | Index of speaker |
| name | string | A string array of speaker names |

- **Sample code**: 

```
int index = 0;
char name[SPEAKER_DEVICE_NAME_MAX_SIZE];
player.speakerDeviceName(index, name);
```



#### 4. selectSpeakerDevice(index)

API details: void selectSpeakerDevice(unsigned int index)

Selects the specified speaker as the audio playback device. When this API is not called, the speaker with index 0 is selected by default.

- **Parameter description**

| Parameter | Type | Description |
| ----- | ---- | -------- |
| index | int | Index of speaker |

- **Sample code**: 

```
int index = 0;
player.selectSpeakerDevice(index);
```



#### 5. speakerVolume()

API details: unsigned int speakerVolume()

Queries the playback volume of SDK. The value ranges from 0 to 65535.

- **Returned result**

| Parameter | Type | Description |
| ---- | ---- | ----------------- |
| vRet | int | Volume value, which ranges from 0 to 65535. |

- **Sample code**: 

```
int ret = player.speakerVolume();
```



#### 6. setSpeakerVolume(volume)

API details: void setSpeakerVolume(unsigned int volume);

Sets the playback volume of SDK. Note: This is not the volume of system speaker.

- **Parameter description**

| Parameter | Type | Description |
| ------ | ---- | --------------------- |
| volume | int | The volume you set, which ranges from 0 to 65535. |

- **Sample code**: 

```
int volume = 100;
player.setSpeakerVolume(volume);
```



#### 7.setRenderFrame(hWnd, rect)

API details: void setRenderFrame(hWnd, rect)

Sets video image rendering window and area.

- **Parameter description**

| Parameter | Type | Description |
| ---- | ------------ | ------------------- |
| hWnd | HWND | The HWND that identifies the video image window. |
| rect | const RECT & | Specifies the rendering area of the video image on the window identified by HWND. |

- **Sample code**: 

```
player.setRenderFrame(rendHwnd, rect);
```



#### 8.updateRenderFrame(hWnd, rect)

API details: void updateRenderFrame(hWnd, rect)

Resets the image rendering area. When the size of the window identified by the specified HWND changes, you can resize the video rendering area using this function.

- **Parameter description**

| Parameter | Type | Description |
| ---- | ------------ | ------------------- |
| hWnd | HWND | The HWND that identifies the video image window. |
| rect | const RECT & | Specifies the rendering area of the video image on the window identified by HWND. |

- **Sample code**: 

```
player.updateRenderFrame(rendHwnd, rect);
```



#### 9.closeRenderFrame()

API details: void closeRenderFrame()

Disables image rendering.

- **Sample code**: 

```
player.closeRenderFrame();
```



#### 10.startPlay(url, type)

API details: void startPlay(url, type)
Starts playback. You need to call setRenderFrame before calling startPlay.

- **Parameter description**

| Parameter | Type | Description |
| ---- | ------------ | ---------------------------------------- |
| url | const char * | A valid pull URL, which is the video playback URL. The URL starts with "rtmp://". For more information on how to obtain Tencent Cloud pull URL, please see [DOC](https://cloud.tencent.com/document/product/454/7915 "腾讯云-推拉流地址Doc"). |
| type | TXEPlayType | Playback type. See TXEPlayType's enumerated values defined in TXLiveSDKTypeDef.h |

- **Sample code**: 

```
player.startPlay(playUrl, PLAY_TYPE_LIVE_RTMP_ACC);
```



#### 11.stopPlay()

API details: void stopPlay()

Stops playback.

- **Sample code**: 

```
player.stopPlay();
```



#### 12.pause()

API details: void pause()

Pauses playback.

- **Sample code**: 

```
player.pause()
```



#### 13.resume()

API details: void resume()

Resumes playback.

- **Sample code**: 

```
player.resume()
```



#### 14.isPlaying()

API details: bool isPlaying()

Indicates whether the playback is in progress.

true: in progress; false: not in progress.

- **Sample code**: 

```
bool isPlaying = player.isPlaying();
```



#### 15.setMute(mute)

API details: void setMute(mute)

- **Parameter description**

| Parameter | Type | Description |
| ---- | ---- | ---- |
| mute | bool | Indicates whether to enable Mute |

- **Sample code**: 

```
player.setMute(true);
```



#### 16.setRenderMode(mode)

API details: void setRenderMode(mode)

Sets the rendering (fill) mode of image.

- **Parameter description**

| Parameter | Type | Description |
| ---- | ------------- | ---------------------------------------- |
| mode | TXERenderMode | See TXERenderMode's enumerated values defined in TXLiveSDKTypeDef.h |

- **Sample code**: 

```
player.setRenderMode(AX_TXE_RENDER_MODE_ADAPT);
```



#### 17.setRotation(rotation)

API details: void setRotation(rotation)

Sets the clockwise rotation of image.

- **Parameter description**

| Parameter | Type | Description |
| -------- | ---------------- | ---------------------------------------- |
| rotation | TXEVideoRotation | See TXEVideoRotation's enumerated values defined in TXLiveSDKTypeDef.h |

- **Sample code**: 

```
player.setRotation(TXE_VIDEO_ROTATION_90);
```



#### 18.setRenderYMirror(mirror)

API details: void setRenderYMirror(mirror)

Sets the mirroring effect for preview rendering.

- **Parameter description**

| Parameter | Type | Description |
| ------ | ---- | ------------------------ |
| mirror | bool | true: the image is mirrored horizontally; false: the image remains as it is. |

- **Sample code**: 

```
player.setRenderYMirror(true);
```



#### 19. setOutputVideoFormat(format)

API details:  void setOutputVideoFormat(format)

Sets video encoding format. Default format: TXE_OUTPUT_VIDEO_WITHOUT_OUTPUT

- **Parameter description**

| Parameter | Type | Description |
| ------ | -------------------- | ---------------------------------------- |
| format | TXEOutputVideoFormat | Specifies video encoding format. See TXEOutputVideoFormat's enumerated values defined in TXLiveSDKTypeDef.h |

- **Sample code**: 

```
player.setOutputVideoFormat(TXE_OUTPUT_VIDEO_FORMAT_YUV420);
```



#### 20. captureVideoSnapShot(filePath,length)

API details: int captureVideoSnapShot(wchar_t * filePath, unsigned int length)

Captures screenshots of pulled images and saves to local device.

- **Parameter description**

| Parameter | Type | Description |
| -------- | ------------ | ----------------- |
| filePath | wchar_t * | File path. Only .jpg format is supported. |
| length | unsigned int | Length of filePath |

- **Sample code**: 

```
std::wstring path = L"D:\\132.jpg";
player.captureVideoSnapShot(path.c_str(), path.size());
```



## Enumeration Type Definition - API Parameters

#### TXEAudioCaptureSrcType

Audio data source types

```
	TXE_AUDIO_SRC_SDK_DATA = 1,				     Audio capture source is the sound data from LiteAvSDK, including local microphone, local player, system, etc.
	TXE_AUDIO_SRC_USER_PCM = 1001,				Audio capture source is the PCM raw audio data uploaded by users.
	TXE_AUDIO_SRC_USER_AAC = 1002,				Audio capture source is the AAC audio data uploaded by users.

```

#### TXEVideoCaptureSrcType

Video data source types

```
	TXE_VIDEO_SRC_UNDEFINED = 0,		         No video capture source
	TXE_VIDEO_SRC_SDK_CAMERA = 1,	         Video capture source is LiteAvSDK camera data.
	TXE_VIDEO_SRC_SDK_SCREEN = 2,	         Video capture source is LiteAvSDK screencap data.
	TXE_VIDEO_SRC_USER_DATA = 1001,          Video capture source is the video data uploaded by users.

```

#### TXEVideoUserDataFormat

The formats of videos uploaded by users in several common scenarios

```
	TXE_UserData_Undefined = 0,		  Block all video data uploaded by users
	TXE_UserData_Yuv420P,			  Yuv420P video data
	TXE_UserData_H264Nal,			  H264Nal-encoded video data

```

#### TXEVideoResolution 

Push video resolutions

        // Standard screen 4:3
    TXE_VIDEO_RESOLUTION_320x240 = 1,
    TXE_VIDEO_RESOLUTION_480x360 = 2,
    TXE_VIDEO_RESOLUTION_640x480 = 3,
    TXE_VIDEO_RESOLUTION_960x720 = 4,
    
    // Wide screen 16:9
    TXE_VIDEO_RESOLUTION_320x180 = 101,
    TXE_VIDEO_RESOLUTION_480x272 = 102,
    TXE_VIDEO_RESOLUTION_640x360 = 103,
    TXE_VIDEO_RESOLUTION_960x540 = 104,
    
    // Wide screen 9:16
    TXE_VIDEO_RESOLUTION_180x320 = 201,
    TXE_VIDEO_RESOLUTION_272x480 = 202,
    TXE_VIDEO_RESOLUTION_360x640 = 203,
    TXE_VIDEO_RESOLUTION_540x960 = 204,

#### TXERenderMode

Video rendering mode on window

```
TXE_RENDER_MODE_ADAPT = 1,              // Adaption. The video image is displayed in full on the screen, possibly with black edges around it.
TXE_RENDER_MODE_FILLSCREEN = 2,         // Filling. No black edge exists, but the parts beyond the rendering area are trimmed off, so that the image is centered on the screen.
```

#### TXEVideoRotation 

Rendering video rotation

    TXE_VIDEO_ROTATION_NONE = 1,            // No rotation of the image.
    TXE_VIDEO_ROTATION_90 = 2,              // Rotates the image 90 degrees clockwise, with its width and height interchanged.
    TXE_VIDEO_ROTATION_180 = 3,             // Rotates the image 180 degrees clockwise, with the image reversed upside down.
    TXE_VIDEO_ROTATION_270 = 4,             // Rotates the image 270 degrees clockwise, with its width and height interchanged.
#### TXEAutoAdjustStrategy

Traffic control policy for pushing videos

	TXE_AUTO_ADJUST_NONE = -1,                         // No traffic control. The video bitrate specified by setVideoBitRate is always used.
	TXE_AUTO_ADJUST_LIVEPUSH_STRATEGY = 0,             // Suitable for common push scenarios in LVB. This policy has a lower sensitivity and adapts to the bandwidth change slowly. This is helpful to maintain the image clarity when the bandwidth fluctuates.
	TXE_AUTO_ADJUST_LIVEPUSH_RESOLUTION_STRATEGY = 1,  // Suitable for common push scenarios in LVB. Upgraded from LIVEPUSH_STRATEGY, this policy allows the SDK to adapt the resolution to the bitrate automatically.
	TXE_AUTO_ADJUST_REALTIME_VIDEOCHAT_STRATEGY = 5,   // Suitable for real-time video chats. It is used by VIDEO_QUALITY_REALTIME_VIDEOCHAT.                           
													  // This policy is highly sensitive to network condition and makes adaptive adjustment in case of any network fluctuation.
#### TXEVideoQualityParamPreset

Preset options for SDK push image quality

```
TXE_VIDEO_QUALITY_STANDARD_DEFINITION = 1,      // SD: Suitable for customers who care more about smoothness.
TXE_VIDEO_QUALITY_HIGH_DEFINITION = 2,			// HD: Suitable for customers who care more about image clarity.
TXE_VIDEO_QUALITY_SUPER_DEFINITION = 3,			// SD: Not recommended unless you are watching videos on a large screen.
TXE_VIDEO_QUALITY_LINKMIC_MAIN_PUBLISHER = 4,   // Joint broadcasting with the primary VJ
TXE_VIDEO_QUALITY_LINKMIC_SUB_PUBLISHER = 5,    // Joint broadcasting with a secondary VJ
TXE_VIDEO_QUALITY_REALTIME_VIDEOCHAT = 6,       // Real-time video chats
TXE_VIDEO_QUALITY_STILLIMAGE_DEFINITION = 7,	// Suitable for scenarios featuring static image quality. Generally, the screenshots captured and pushed by users have few dynamic changes. With the algorithm available for adaptive bitrate and resolution, custom settings are not recommended.
```

#### TXEOutputVideoFormat

Sets the video output format

```
TXE_OUTPUT_VIDEO_WITHOUT_OUTPUT = 1,        // No data output
TXE_OUTPUT_VIDEO_FORMAT_YUV420 = 2,         // yuv420 format
TXE_OUTPUT_VIDEO_FORMAT_RGBA = 3,           // RBGA format
```
#### TXEBeautyStyle

Beauty filter style

	TXE_BEAUTY_STYLE_SMOOTH = 0,     // Smooth
	TXE_BEAUTY_STYLE_NATURE = 1,        // Natural
	TXE_BEAUTY_STYLE_BLUR   = 2,        // Hazy
#### TXEPlayType

Playback type

    PLAY_TYPE_LIVE_RTMP = 0,           RTMP LVB
    PLAY_TYPE_LIVE_RTMP_ACC,           Accelerated playback in RTMP LVB



## Definitions of CallBack Event Parameters

#### PushEvent

Push events

```
TXE_STATUS_UPLOAD_EVENT : 200001,                  // Push-related data

PUSH_EVT_CONNECT_SUCC = 1001,                      // Connected to the push server
PUSH_EVT_PUSH_BEGIN = 1002,                        // Handshake with the server completed. Push starts.
PUSH_EVT_OPEN_CAMERA_SUCC = 1003,                  // Camera enabled successfully
PUSH_EVT_CHANGE_RESOLUTION = 1005,	               // Resolution is changed dynamically during push
PUSH_EVT_CHANGE_BITRATE = 1006,                    // Bitrate is changed dynamically during push
PUSH_EVT_FIRST_FRAME_AVAILABLE = 1007,             // The first frame is captured
PUSH_EVT_START_VIDEO_ENCODER = 1008,               // Encoder started
PUSH_EVT_CAMERA_REMOVED = 1009,                    // Camera removed (for PC SDK)
PUSH_EVT_CAMERA_AVAILABLE = 1010,                  // Camera is available again (for PC SDK)
PUSH_EVT_CAMERA_CLOSED = 1011,                     // Camera disabled (for PC SDK)
PUSH_EVT_SNAPSHOT_RESULT = 1012,                     // Error code returned for screencap

PUSH_ERR_OPEN_CAMERA_FAIL = -1301,                 // Failed to enable camera
PUSH_ERR_OPEN_MIC_FAIL = -1302,                    // Failed to enable microphone
PUSH_ERR_VIDEO_ENCODE_FAIL = -1303,                // Video encoding failed
PUSH_ERR_AUDIO_ENCODE_FAIL = -1304,                // Audio encoding failed
PUSH_ERR_UNSUPPORTED_RESOLUTION = -1305,           // Unsupported video resolution
PUSH_ERR_UNSUPPORTED_SAMPLERATE = -1306,           // Unsupported audio sampling rate
PUSH_ERR_NET_DISCONNECT = -1307,                   // Network disconnected. Too many failed reconnection attempts. Restart the push for more retries.
PUSH_ERR_CAMERA_OCCUPY = -1308,                    // The camera is in use. Enable another camera (for PC SDK)

PUSH_WARNING_NET_BUSY = 1101,                      // Bad network condition: data upload is blocked because upstream bandwidth is too small
PUSH_WARNING_RECONNECT = 1102,                     // Network disconnected. Auto reconnection has been initiated (no more attempts will be made after three failed attempts)
PUSH_WARNING_HW_ACCELERATION_FAIL = 1103,          // Failed to start hard-encoding. Soft-encoding is used instead.
PUSH_WARNING_VIDEO_ENCODE_FAIL = 1104,             // Video encoding failed. Non-fatal error. Encoder will be restarted internally.
PUSH_WARNING_BEAUTYSURFACE_VIEW_INIT_FAIL = 1105,  // Video encoding bitrate exception
PUSH_WARNING_VIDEO_ENCODE_BITRATE_OVERFLOW = 1106, // Video encoding bitrate exception
PUSH_WARNING_DNS_FAIL = 3001,                      // RTMP - DNS resolution failed
PUSH_WARNING_SEVER_CONN_FAIL = 3002,               // Failed to connect to RTMP server
PUSH_WARNING_SHAKE_FAIL = 3003,                    // Handshake with RTMP server failed
PUSH_WARNING_SERVER_DISCONNECT = 3004,	           // RTMP server disconnected automatically. Check the validity of push URL or the validity period of the hotlink protection.
PUSH_WARNING_SERVER_NO_DATA = 3005,                // No data was sent within 30 seconds. Server disconnected automatically.
```

#### PlayEvent

Playback events

```
TXE_STATUS_DOWNLOAD_EVENT : 200002,             // Pull-related data

PLAY_EVT_CONNECT_SUCC : 2001,                   // Connected to the server
PLAY_EVT_RTMP_STREAM_BEGIN : 2002,              // Connected to the server. Pull started.
PLAY_EVT_RCV_FIRST_I_FRAME : 2003,              // The first video data packet (IDR) is rendered
PLAY_EVT_PLAY_BEGIN : 2004,                     // Video playback started
PLAY_EVT_PLAY_PROGRESS : 2005,                  // Video playback progress
PLAY_EVT_PLAY_END : 2006,                       // Video playback ended
PLAY_EVT_PLAY_LOADING : 2007,                   // Video playback loading
PLAY_EVT_START_VIDEO_DECODER : 2008,            // Decoder started
PLAY_EVT_CHANGE_RESOLUTION : 2009,              // Video resolution changed
PLAY_EVT_SNAPSHOT_RESULT : 2010,              // Error code returned for screencap

PLAY_ERR_NET_DISCONNECT : -2301,                // Network disconnected. Too many failed reconnection attempts. Restart the playback for more retries.
PLAY_ERR_GET_RTMP_ACC_URL_FAIL : -2302,         // Failed to get the accelerated pull address

PLAY_WARNING_VIDEO_DECODE_FAIL : 2101,          // Failed to decode the current video frame
PLAY_WARNING_AUDIO_DECODE_FAIL : 2102,          // Failed to decode the current audio frame
PLAY_WARNING_RECONNECT : 2103,                  // Network disconnected. Auto reconnection has been initiated (no more attempts will be made after three failed attempts)
PLAY_WARNING_RECV_DATA_LAG : 2104,              // Unstable inbound packet: This may be caused by insufficient downstream bandwidth, or inconsistent outbound stream from the VJ end.
PLAY_WARNING_VIDEO_PLAY_LAG : 2105,             // Stutter occurred during the video playback (user experience)
PLAY_WARNING_HW_ACCELERATION_FAIL : 2106,       // Failed to start hard decoding. Soft decoding is used instead.
PLAY_WARNING_VIDEO_DISCONTINUITY : 2107,        // Discontinuous sequence of video frames. Some frames may be dropped.
PLAY_WARNING_FIRST_IDR_HW_DECODE_FAIL : 2108,   // Hard decoding of the first I-frame of current stream failed. Switched to soft decoding automatically.
PLAY_WARNING_DNS_FAIL : 3001,                   // RTMP - DNS resolution failed
PLAY_WARNING_SEVER_CONN_FAIL : 3002,            // Failed to connect to RTMP server
PLAY_WARNING_SHAKE_FAIL : 3003,                 // Handshake with RTMP server failed
PLAY_WARNING_SERVER_DISCONNECT : 3004,	        // RTMP server disconnected automatically
```



#### TXE_STATUS_UPLOAD_EVENT && TXE_STATUS_DOWNLOAD_EVENT

Definitions of status keys

```
#define NET_STATUS_CPU_USAGE         "CPU_USAGE"        // CPU utilization
#define NET_STATUS_CPU_USAGE_D       "CPU_USAGE_DEVICE" // Total CPU usage of device
#define NET_STATUS_VIDEO_BITRATE     "VIDEO_BITRATE"    // The output bitrate of the current video encoder - the video data bits produced by the encoder per sec (in Kbps).
#define NET_STATUS_AUDIO_BITRATE     "AUDIO_BITRATE"    // The output bitrate of the current audio encoder - the audio data bits produced by the encoder per sec (in Kbps).
#define NET_STATUS_VIDEO_FPS         "VIDEO_FPS"        // Current video frame rate - the number of frames produced by video encoder per sec.
#define NET_STATUS_VIDEO_GOP         "VIDEO_GOP"        // I-frame interval of current video: the interval between I-frames of video encoder (in sec).
#define NET_STATUS_NET_SPEED         "NET_SPEED"        // Current network speed
#define NET_STATUS_NET_JITTER        "NET_JITTER"       // Network jitter. The greater the jitter, the more unstable the network.
#define NET_STATUS_CACHE_SIZE        "CACHE_SIZE"       // Buffer size. A larger buffer indicates the current upstream bandwidth is not enough to consume the video data produced.
#define NET_STATUS_DROP_SIZE         "DROP_SIZE"
#define NET_STATUS_VIDEO_WIDTH       "VIDEO_WIDTH"
#define NET_STATUS_VIDEO_HEIGHT      "VIDEO_HEIGHT"
#define NET_STATUS_SERVER_IP         "SERVER_IP"
#define NET_STATUS_CODEC_CACHE       "CODEC_CACHE"      // Buffer size for encoding/decoding
#define NET_STATUS_CODEC_DROP_CNT    "CODEC_DROP_CNT"   // Encoding/decoding queue DROPCNT
#define NET_STATUS_SET_VIDEO_BITRATE "SET_VIDEO_BITRATE"
```



## TXLivePusherCallback

Listening on push events

| API Definition | Description |
| ---------------------------------------- | ------------------- |
| onEventCallback(eventId, paramCount, paramKeys, paramValues, pUserData) | Push event notification of TXLivePusher |



## TXLivePlayerCallback

Listening on playback events

| API Definition | Description |
| ---------------------------------------- | -------------------- |
| onEventCallback(eventId, paramCount, paramKeys, paramValues, pUserData) | Playback event notification of TXLivePlayer |

