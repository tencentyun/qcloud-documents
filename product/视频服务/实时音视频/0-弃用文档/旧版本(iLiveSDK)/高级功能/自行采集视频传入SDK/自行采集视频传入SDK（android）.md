本文将指导您如何在客户端采集自定义的视频图像，并将图像上行播放给观众

## 效果图
![](https://main.qcloudimg.com/raw/06f1731f87f01306a149184b244291b0.png)

## 源码下载
在此我们提供以下所讲到的完整 Demo 代码，如有需要请您自行下载。 
[点击下载]()

## 相关说明
自行视频采集是指用户不用ILiveSDK默认的视频采集（目前ILiveSDK）是通过手机的摄像头采集视频的。

某些场景下，应用需要自己控制摄像头采集视频内容，或者需要对ILiveSDK采集的视频加工后（如美颜，添加挂件等）再上行。对此ILiveSDK提供了一套较简洁的方案。

PS:对于屏幕分享，播片，ILiveSDK的视频源拦截等有更简单的方案。参考其它教程或API

## 具体实现

### 实现自定义采集
本文以自行打开摄像头采集来举例说明。
由于指定了摄像头自行来采集视频，所以此处我们要对摄像头及相关的采集显示做一些操作。
这里直接上一份摄像头采集图像显示代码，基本为Android原生知识，就不做过多说明。

创建摄像头操作相关的Activity
```Java
public class CameraActivity extends Activity implements View.OnClickListener {

    //定义摄像头对象
    private Camera mCamera;
    //定义摄像头画面预览控件
    private CameraPreview mPreview;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_camera);
    }

    /**
     * 打开摄像头
     *
     * @return
     */
    private Camera getCameraInstance() {
        Camera c = null;
        try {
            c = Camera.open();
        } catch (Exception e) {
        }
        return c;
    }

    @Override
    public void onClick(View view) {

        if (view.getId() == R.id.btn_camera) {
            mCamera = getCameraInstance();
            mPreview = new CameraPreview(this, mCamera);
            FrameLayout preview = (FrameLayout) findViewById(R.id.camera_preview);
            preview.addView(mPreview);
        }
    }


    /**
     * 摄像头预览界面控件
     */
    public class CameraPreview extends SurfaceView implements SurfaceHolder.Callback {

        private SurfaceHolder mHolder;
        private Camera mCamera;

        private static final String TAG = "CameraPreview";


        public CameraPreview(Context context, Camera camera) {
            super(context);
            mCamera = camera;
            mHolder = getHolder();
            mHolder.addCallback(this);
        }

        @Override
        public void surfaceCreated(SurfaceHolder holder) {
            try {
                if (mCamera == null)
                    return;
                mCamera.setPreviewDisplay(holder);
                mCamera.startPreview();
            } catch (IOException e) {
                Log.d(TAG, "Error setting camera preview: " + e.getMessage());
            }
        }

        @Override
        public void surfaceDestroyed(SurfaceHolder holder) {
        }

        @Override
        public void surfaceChanged(SurfaceHolder holder, int format, int w, int h) {
            if (mCamera == null || mHolder.getSurface() == null) {
                return;
            }
            try {
                mCamera.stopPreview();
                mCamera.setPreviewDisplay(mHolder);
                mCamera.setDisplayOrientation(90);
                mCamera.startPreview();
            } catch (Exception e) {
                Log.d(TAG, "Error starting camera preview: " + e.getMessage());
            }
        }

        public void release() {
            if (mCamera != null) {
                mCamera.release();
            }

        }


    }
}
```

通过上面的代码可以完成自行打开摄像头采集画面的操作，并将图像显示在Activity中

### 开启直播
创建房间，开启直播可参考（[创建房间](创建房间.md)）。
此处需注意，由于采用了自定义采集视频，故创建房间时的无需设置渲染控件，另外需关闭SDK的自动打开摄像头配置
```Java
ILiveRoomOption option = new ILiveRoomOption(ILiveLoginManager.getInstance().getMyUserId())
        .autoCamera(false) //关闭自动打开摄像头功能
        .videoMode(ILiveConstants.VIDEOMODE_NORMAL)
        .controlRole(Constants.ROLE_MASTER);
```

### 上传自定义采集数据
用户在创建房间成功后，先调用接口开启SDK的允许外部采集功能
```Java
/**
 * @param var1 是否允许外部采集
 * @param va2  是否开启本地渲染
 * @param callback 开启操作回调
 */
ILiveSDK.getInstance().getAvVideoCtrl().enableExternalCapture(boolean var1, boolean va2, AVVideoCtrl.EnableExternalCaptureCompleteCallback callback)
```


上面的代码中我们已经打开了摄像头，也打开启了ILiveSDK的外面采集功能。那如何将摄像头采集的图像数据给到SDK进行上传呢？
ILiveSDK提供了图像数据填充接口，用户调用该接口将自行采集的图像给到SDK进行上传
```Java
ILiveSDK.getInstance().getAvVideoCtrl().fillExternalCaptureFrame(byte[] data, int datalen, int byteperRow, int width, int heigh, int rotate, int formatType, int srcType）
```

该接口在什么时机调用呢？以上面说到的自行打开摄像头采集为例，需要对摄像头采集的数据做处理。
我们通过对摄像头的图像预览设置监听，即设置Camera.setPreviewCallback(PreviewCallback callBack)，在Camera预览图像的回调函数中填充摄像头采集的图像数据;
```Java
mCamera.setPreviewCallback(new Camera.PreviewCallback() {
		/**
		 * Camera.PreviewCallback的接口实现
		 * Camera设置了PreviewCallback后，摄像头每一帧的图像预览都会调用了该函数
		 * @param data 预览的图像数据
		 * @param camera 预览的摄像头对象
		 */
		@Override
		public void onPreviewFrame(byte[] data, Camera camera) {
			if (null != camera && !bPreviewInit) {
				Camera.Parameters parameters = camera.getParameters();
                                //获取图像的大小
				mCameraSize = parameters.getPreviewSize();
				bPreviewInit = true;
			}
			//填充图像数据
			if (null != ILiveSDK.getInstance().getAvVideoCtrl()) {			                                                                                                                                    
				ILiveSDK.getInstance().getAvVideoCtrl().fillExternalCaptureFrame(data, data.length, 0, mCameraSize.width, mCameraSize.height, 1, AVVideoCtrl.EXTERNAL_FORMAT_I420, AVView.VIDEO_SRC_TYPE_CAMERA);

			}
		}
});
```

## API说明

### enableExternalCapture
AVVideoCtrl类的方法，开启/关闭外部视频捕获设备。异步返回结果
参数说明

|名称|类型|描述|
|--|--|--|
|isEnable|boolan|true表示开启，false表示关闭|
|shouldRender|boolan|是否渲染输入流视频数据，true表示会，false表示不会|
|callback|VVideoCtrl.EnableExternalCaptureCompleteCallback|开启外部视频采集回调|

### fillExternalCaptureFrame
AVVideoCtrl类的方法，入从外部视频捕获设备获取的视频图像到SDK。SDK将会将数据编码之后发给接收方
参数说明：

|名称|类型|描述|
|--|--|--|
|data|byte[]|图像数据|
|dataLen|int|数据长度，即data的长度|
|stride|int|图像的byteperRow。RGB32图像专用，一般为宽度的4倍，特殊分辨率图像需要注意|
|width|int|图像宽度|
|height|int|图像高度|
|cameraAngle|int|图像角度。角度可以是0, 1, 2, 3. 0,1,2,3的含义为图像需要分别顺时针旋转0*90 1*90、 2*90、 3*90度才能正立|
|colorFormat|int|图像颜色格式，具体值参考AVVideoCtrl.EXTERNAL_FORMAT_I420、EXTERNAL_FORMAT_RGBA等值|
|srcType|int|视频源类型。当前仅支持AVView.VIDEO_SRC_TYPE_CAMERA|

支持的图像类型及对应常量

|类型|常量|
|--|--|
|I420|AVVideoCtrl.EXTERNAL_FORMAT_I420|
|NV21|AVVideoCtrl.EXTERNAL_FORMAT_NV21|
|NV12|AVVideoCtrl.EXTERNAL_FORMAT_NV12|
|RGB565|AVVideoCtrl.EXTERNAL_FORMAT_RGB565|
|RGB24|AVVideoCtrl.EXTERNAL_FORMAT_RGB24|
|ARGB|AVVideoCtrl.EXTERNAL_FORMAT_ARGB|
|RGBA|AVVideoCtrl.EXTERNAL_FORMAT_RGBA|
|ABGR|AVVideoCtrl.EXTERNAL_FORMAT_ABGR|

## 常见问题

- 图像填充接口LiveSDK.getInstance().getAvVideoCtrl().fillExternalCaptureFrame的参数该如何设置？
> 自定义采集需开发者对视频、图像相关知识有一定的了解。主要是colorFormat的配置，采集的图像格式要与该参数相匹配。另外对于RGB32位的图像，需获取图像的byteperRow。

## 联系邮箱
如果对上述文档有不明白的地方，请反馈到trtcfb@qq.com
