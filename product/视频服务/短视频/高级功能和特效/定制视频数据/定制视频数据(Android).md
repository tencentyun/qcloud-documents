## 录制预处理回调

``` 
public interface VideoCustomProcessListener {
/**
  * 在OpenGL线程中回调，在这里可以进行采集图像的二次处理
  * @param textureId 纹理ID
  * @param width     纹理的宽度
  * @param height    纹理的高度
  * @return 返回给SDK的纹理ID，如果不做任何处理，返回传入的纹理ID即可
  * 说明：SDK回调出来的纹理类型是GLES20.GL_TEXTURE_2D，接口返回给SDK的纹理类型也必须是GLES20.GL_TEXTURE_2D
  */
int onTextureCustomProcess(int textureId, int width, int height);

/**
  * 增值版回调人脸坐标
  * @param points 归一化人脸坐标，每两个值表示某点P的X,Y值。值域[0.f,1.f]
  */
void onDetectFacePoints(float[] points);

/**
  * 在OpenGL线程中回调，可以在这里释放创建的OpenGL资源
  */
void onTextureDestroyed();
}
```

## 编辑预处理回调
``` 
public interface TXVideoCustomProcessListener {
        /**
         * 在OpenGL线程中回调，在这里可以进行采集图像的二次处理
         *
         * @param textureId 纹理ID
         * @param width     纹理的宽度
         * @param height    纹理的高度
         * @return 返回给SDK的纹理ID，如果不做任何处理，返回传入的纹理ID即可
         * <p>
         * 说明：SDK回调出来的纹理类型是GLES20.GL_TEXTURE_2D，接口返回给SDK的纹理类型也必须是GLES20.GL_TEXTURE_2D
         */
        int onTextureCustomProcess(int textureId, int width, int height, long timestamp);

        /**
         * 在OpenGL线程中回调，可以在这里释放创建的OpenGL资源
         */
        void onTextureDestroyed();
    }

```