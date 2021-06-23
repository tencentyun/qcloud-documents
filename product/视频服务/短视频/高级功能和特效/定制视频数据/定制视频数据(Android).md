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
