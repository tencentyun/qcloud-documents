## Customize Pushed Image

### Solution 1: Modify OpenGL texture
Some customers with a strong R&D capability want to customize images (e.g., adding captions) while reusing the overall process of RTMP SDK. In this case, follow the steps below.

- **Set callback for video processing**
Set the custom video processing callback through the API **setVideoProcessListener** of **TXLivePusher**

```java
public interface VideoCustomProcessListener {
    /**
    * Perform a callback in the OpenGL thread, where you can conduct the secondary processing of captured images
    * @param textureId  Texture ID
    * @param width      Width of texture
    * @param height     Height of texture
    * @return           Texture returned to SDK
    * Note: The texture type called back from the SDK is GLES20.GL_TEXTURE_2D, and the one returned by the API to the SDK must also be GLES20.GL_TEXTURE_2D.
    */
    int onTextureCustomProcess(int textureId, int width, int height);

    /**
    * Perform a callback in the OpenGL thread, where you can release the OpenGL resources created
    */
    void onTextureDestoryed();
}
```

- **Process the video data in the callback function**
Implement onTextureCustomProcess() function of VideoCustomProcessListener to achieve the customized processing of video images. The texture specified by textureId is a texture of type GLES20.GL_TEXTURE_2D.

> To work with texture data, you need to have some basic knowledge about OpenGL. In addition, a huge calculation amount is not recommended. This is because onTextureCustomProcess has the same call frequency as FPS, and too heavy processing is likely to cause the GPU overheating.

### Solution 2: Capture data by yourself
If you only want to use SDK for encoding and push (for example, you have interfaced with SenseTime and other products), bring the audio and video capture and preprocessing (such as beauty filter, filter) under the control of your own code by following the steps below:

- **Step1. Do not call TXLivePusher's startCameraPreview API any longer**
In this way, SDK itself will not capture video and audio data any more, but only start preprocessing, coding, stream control, sending data and other push-related operations.

- **Step2. Use sendCustomVideoData to populate SDK with Video data**
sendCustomVideoData is used to populate the SDK with the captured and processed video data. I420 format is supported now.

- **Step3. Use sendCustomPCMData to populate SDK with Audio data**
SendAudioSampleBuffer is used to populate the SDK with the captured and processed audio data. Please use 16-bit, 48000-Hz PCM mono audio data.


## Customize Playback Data

### Solution 1: Modify OpenGL texture (only applicable to hard decoding playback)

- **Step 1: Add a TextureView**
To display the video images in a player, you need to replace `TXCloudVideoView` with `TextureView` in the layout xml file
```xml
    <TextureView
            android:id="@+id/video_view"
            android:layout_width="match_parent"
            android:layout_height="match_parent"/>
```

- **Step 2: Obtain a TextureView object from the code**
```
mTextureView = (TextureView) findViewById(R.id.video_view);
```

- **Step 3: Bind the object via setSurface**
Bind mTextureView rendered by video data to TXLivePlayer via setSurface (mSurface) of TXLivePlayer
```Java
mTextureView.setSurfaceTextureListener(new TextureView.SurfaceTextureListener() {

        @Override
        public void onSurfaceTextureAvailable(SurfaceTexture texture, int width, int height) {
            //Create Surface
            mSurface = new Surface(texture);
                //Set Surface to associated mSurface with mTextureView via texture.
                //When this API is called, the decoded data is automatically rendered on mTextureView
            mLivePlayer.setSurface(mSurface);
        }
    
        ......
});
```

- **OpenGL related reference codes**
In case of any problem on resizing images, please see the complete sample code in [Resizing Images](https://cloud.tencent.com/document/product/454/9723)
If you have no idea about how to conduct the secondary processing of video data using OpenGL ES, please see the sample code in [Processing Data with OpenGL ES](https://cloud.tencent.com/document/product/454/9724)

### Solution 2: Obtain YUV data (only applicable to soft decoding playback)

If you want to obtain the video data of YUV type decoded by SDK, follow the steps below.

- Listen for the PLAY_EVT_CHANGE_RESOLUTION event

```Java
    public void onPlayEvent(int event, Bundle param) {
        //...
        if (event == TXLiveConstants.PLAY_EVT_CHANGE_RESOLUTION) {
            //Acquire the width and the height of the video
            int width = param.getInt(TXLiveConstants.EVT_PARAM1, 0);
            int height = param.getInt(TXLiveConstants.EVT_PARAM2, 0);
            if (width != 0 && height != 0 && !mHWDecode) {
                //Create a buffer to store yuv data. Now, the output format of yuv is I420
                byte[] buf = new byte[width * height * 3 / 2];
                //Set the buffer into mLivePlayer
                mLivePlayer.addVideoRawData(buf);
            }
        }
    }
```

- Obtain YUV raw data via VideoRawDataListener

```Java
TXVideoRawDataObserver.ITXVideoRawDataListener rawDataListener = new
TXVideoRawDataObserver.ITXVideoRawDataListener() {
    @Override
    public void onVideoRawDataAvailable(byte[] buf, int width, int height, int timestamp) {
        //Decode the data callback after one frame. buf stores the YUV data in I420 format
        if (!mHWDecode) {
            //If you need to continue to obtain the YUV data, call addVideoRawData again
            mLivePlayer.addVideoRawData(buf);
        }
    }
};

mLivePlayer.setVideoRawDataListener(rawDataListener);
```

