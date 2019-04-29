## Customizing Push Images

### Solution 1: Modify OpenGL texture
Some customers with a strong R&D capability want to customize images (e.g., adding captions) while reusing the overall process of RTMP SDK. In this case, follow the steps below.

- **Set callback for video processing**
You can customize video images by setting **videoProcessDelegate** proxy for **TXLivePush**.

```objectivec
@protocol TXVideoCustomProcessDelegate <NSObject>

/**
 * Perform a callback in the OpenGL thread, where you can conduct the secondary processing of captured images.
 * @param textureId  Texture ID
 * @param width      Width of texture
 * @param height     Height of texture
 * @return           Texture returned to SDK
 * Note: The texture type called back from the SDK is GL_TEXTURE_2D, and the one returned by the API to the SDK must also be GL_TEXTURE_2D.
 */
-(GLuint)onPreProcessTexture:(GLuint)texture width:(CGFloat)width height:(CGFloat)height;
 
/**
 * Perform a callback in the OpenGL thread, where you can release the OpenGL resources created.
 */
-(void)onTextureDestoryed;

@end
```

- **Process the video data in the callback function**
Implement onPreProcessTexture function of TXVideoCustomProcessDelegate to achieve the customized processing of video images. The texture specified by textureId is a texture of type GLES20.GL_TEXTURE_2D.

 To work with texture data, you need to have some basic knowledge about OpenGL. In addition, a huge calculation amount is not recommended. This is because onPreProcessTexture has the same call frequency as FPS, and too heavy processing is likely to cause the GPU overheating.

### Solution 2: Capture data by yourself
If you only want to use SDK for encoding and push (for example, you have interfaced with SenseTime and other products), bring the audio and video capture and preprocessing (such as beauty filter, filter) under the control of your own code by following the steps below:

- **Step1. Do not call TXLivePusher's startPreview API any longer**
In this way, SDK itself does not capture video and audio data any more, but only conducts preprocessing, encoding, traffic control, data delivery and other push-related operations.

- **Step2. Set customModeType via TXLivePushConfig**

```objectiveC
     #define CUSTOM_MODE_AUDIO_CAPTURE          0X001   //Customer captures their own audios.
     #define CUSTOM_MODE_VIDEO_CAPTURE          0X002   //Customer captures their own videos.
		 
	//If both audios and videos need to be captured by customer, the customModeType can be set to 3.
	 @interface TXLivePushConfig : NSObject
	        @property(nonatomic, assign) int customModeType;
	 @end
```

- **Step3. Use sendVideoSampleBuffer to populate SDK with Video data**
SendVideoSampleBuffer is used to populate the SDK with the captured and processed video data. RGBA and NV12 formats are supported currently.

```objectiveC
    TXLivePushConfig* config = [[TXLivePushConfig alloc] init];
    config.customModeType    = CUSTOM_MODE_VIDEO_CAPTURE;  // Customize data capturing
    TXLivePush pusher = [[TXLivePush alloc] initWithConfig:config];
    
	//You can populate the RGBA or NV12 data you captured and processed.
    [pusher sendVideoSampleBuffer:sampleBuffer];
```

- **Step4. Use sendAudioSampleBuffer to populate SDK with Audio data**
SendAudioSampleBuffer is used to populate the SDK with the captured and processed audio data. Please use 16-bit, 48000-Hz PCM mono audio data.

 This function supports two RPSampleBufferTypes: RPSampleBufferTypeAudioApp and RPSampleBufferTypeAudioMic. The former is used for replaykit, and the latter for both general microphone capturing and replaykit.

```objectiveC
    TXLivePushConfig* config = [[TXLivePushConfig alloc] init];
    config.customModeType    = CUSTOM_MODE_AUDIO_CAPTURE;  // Customize data capturing
    TXLivePush pusher = [[TXLivePush alloc] initWithConfig:config];
    
	//You can populate the audio data you captured and processed.
    [s_txLivePublisher sendAudioSampleBuffer:sampleBuffer withType:RPSampleBufferTypeAudioMic];
```


## Customize Playback Data

- **Configure the TXVideoCustomProcessDelegate attribute of TXLivePlayConfig**

 ```objectiveC
  @interface TXLivePlayer : NSObject
  // After configuration, each frame of Player goes through onPlayerPixelBuffer. 
  @property(nonatomic, weak) id <TXVideoCustomProcessDelegate> videoProcessDelegate;
```

- **Capture image data of Player with the onPlayerPixelBuffer callback.**

 The image format of pixelBuffer is **NV12** if Player is in hardware decoding mode, and **i420** if Player is in software decoding mode.

 If onPlayerPixelBuffer returns YES, the SDK stops image rendering, which can solve the OpenGL thread conflict.

 ```objectiveC
 @protocol TXVideoCustomProcessDelegate <NSObject>
 @optional

 /**
 * Video rendering object callback
 * @prarm pixelBuffer   Render the image
 * @return  If YES is returned, the SDK stops rendering; if NO is returned, the SDK rendering module keeps working.
 * Note: the data type of the rendered image is renderPixelFormatType set in config.
 */
-(BOOL)onPlayerPixelBuffer:(CVPixelBufferRef)pixelBuffer;
 @end
 ```

