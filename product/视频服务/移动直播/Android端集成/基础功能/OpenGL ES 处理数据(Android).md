## 在OpenGL ES环境下的使用示例


```
public class MyGLSurfaceView extends GLSurfaceView implements GLSurfaceView.Renderer, SurfaceTexture.OnFrameAvailableListener {
	public GlRemoteDisplayView(Context context, AttributeSet attrs) {
        super(context, attrs);
        setEGLContextClientVersion(2);
        setRenderer(this);
        //设置渲染模式，只有在调用requestRender接口时才进行刷新界面
        setRenderMode(RENDERMODE_WHEN_DIRTY);
    }
}

@Override
public void onSurfaceCreated(GL10 gl, EGLConfig config) {
	//初始化OpenGL，并创建textureIds(纹理ID)
	//创建SurfaceTexture
	surfaceTexture = new SurfaceTexture(textureIds[0]);
	surfaceTexture.setOnFrameAvailableListener(this);
	
	//创建Surface
	Surface surface = new Surface(surfaceTexture);
	//设置Surface
	mLivePlayer.setSurface(surface);
}

@Override
public void onDrawFrame(GL10 gl) {
	//对解码数据进行二次处理和渲染到GLSurfaceView
}

@Override
public void onFrameAvailable(SurfaceTexture surfaceTexture) {
	//收到解码数据，请求渲染到GLSurfaceView
	requestRender();
}
```