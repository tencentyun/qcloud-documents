## 如何调整画面尺寸

通过  TXLivePlayer 的 setSurface(mSurface) 接口将视频数据渲染的 
 mTextureView 绑定到 TXLivePlayer 

```
mTextureView.setSurfaceTextureListener(new TextureView.SurfaceTextureListener() {

    @Override
    public void onSurfaceTextureAvailable(SurfaceTexture texture, int width, int height) {
        //创建Surface
        mSurface = new Surface(texture);
        //设置Surface，mSurface和mTextureView通过texture关联在了一起，
        //所以调用该接口后，解码数据自动渲染到mTextureView上
        mLivePlayer.setSurface(mSurface);
    }
    
    @Override
    public void onSurfaceTextureSizeChanged(SurfaceTexture surface, int width, int height) {
    }

    @Override
    public boolean onSurfaceTextureDestroyed(SurfaceTexture surface) {
        return false;
    }

    @Override
    public void onSurfaceTextureUpdated(SurfaceTexture surface) {
    }
});
```


按照上面的设置，我们已经能够看到播放画面了。但会发现TextureView的尺寸和视频的尺寸不一致，导致界面拉伸。此时我们就需要对TextureView做伸缩处理。


```
ITXLivePlayListener playListener = new ITXLivePlayListener() {
        @Override
        public void onPlayEvent(int event, Bundle param) {
            //...
            if (event == TXLiveConstants.PLAY_EVT_CHANGE_RESOLUTION) {
                //获取视频的宽高
                int width = param.getInt(TXLiveConstants.EVT_PARAM1, 0);
                int height = param.getInt(TXLiveConstants.EVT_PARAM2, 0);
                //根据视频尺寸，对TextureView进行拉伸和旋转
                adjustView(width, height, 0, TXLiveConstants.RENDER_MODE_ADJUST_RESOLUTION);
            }
        }
    
        @Override
        public void onNetStatus(Bundle status) {
        }
    };
    
    
private void adjustView(int videoWidth, int videoHeight, int rotation, int mode) {
    if (0 == videoWidth || 0 == videoHeight) {
        return;
    }
    int viewWidth = mTextureView.getWidth();
    int viewHeight = mTextureView.getHeight();
    int showWidth;
    int showHeight;
    if (rotation == 90 || rotation == 270) {
         //互换宽高
        viewWidth = viewWidth ^ viewHeight;
        viewHeight = viewWidth ^ viewHeight;
        viewWidth = viewWidth ^ viewHeight;
    }

    float xRatio = (float)viewWidth / videoWidth;
    if (mode == TXLiveConstants.RENDER_MODE_ADJUST_RESOLUTION) {
        //自适应模式
        if (viewHeight > videoHeight * xRatio) {
            showWidth = viewWidth;
            showHeight = (int) (videoHeight * xRatio);
        } else {
            showWidth = (videoWidth * viewHeight / videoHeight);
            showHeight = viewHeight;
        }
    } else {
        //填充模式
        if (viewHeight > videoHeight * xRatio) {
            showWidth = (videoWidth * viewHeight / videoHeight);
            showHeight = viewHeight;
        } else {
            showWidth = viewWidth;
            showHeight = (int) (videoHeight * xRatio);
        }
    }
    mTextureView.setRotation(rotation);
    mTextureView.setScaleX((float)showWidth/mTextureView.getWidth());
    mTextureView.setScaleY((float)showHeight/mTextureView.getHeight());
}
```