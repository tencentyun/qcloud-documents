## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | -  | -  | &#10003;  | -  | -  | &#10003;  |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。



## 录制预处理回调 

<dx-codeblock>
::: java java
public interface VideoCustomProcessListener {
/**

  * 在 OpenGL 线程中回调，在这里可以进行采集图像的二次处理
  * @param textureId 纹理 ID
  * @param width     纹理的宽度
  * @param height    纹理的高度
  * @return 返回给 SDK 的纹理 ID，如果不做任何处理，返回传入的纹理 ID 即可
  * 说明：SDK 回调出来的纹理类型是 GLES20.GL_TEXTURE_2D，接口返回给 SDK 的纹理类型也必须是 GLES20.GL_TEXTURE_2D
    */
    int onTextureCustomProcess(int textureId, int width, int height);

/**
  * 增值版回调人脸坐标
  * @param points 归一化人脸坐标，每两个值表示某点 P 的 X、Y 值。值域[0.f,1.f]
    */
    void onDetectFacePoints(float[] points);

/**
  * 在 OpenGL 线程中回调，可以在这里释放创建的 OpenGL 资源
    */
    void onTextureDestroyed();
    }
    :::
    </dx-codeblock>

## 编辑预处理回调
<dx-codeblock>
::: java java
public interface TXVideoCustomProcessListener {
        /**
         * 在 OpenGL 线程中回调，在这里可以进行采集图像的二次处理
         *
         * @param textureId 纹理 ID
         * @param width     纹理的宽度
         * @param height    纹理的高度
         * @return 返回给 SDK 的纹理 ID，如果不做任何处理，返回传入的纹理 ID 即可
         * <p>
         * 说明：SDK 回调出来的纹理类型是 GLES20.GL_TEXTURE_2D，接口返回给 SDK 的纹理类型也必须是 GLES20.GL_TEXTURE_2D
         */
        int onTextureCustomProcess(int textureId, int width, int height, long timestamp);

        /**
         * 在 OpenGL 线程中回调，可以在这里释放创建的 OpenGL 资源
         */
        void onTextureDestroyed();
    }
:::
</dx-codeblock>
