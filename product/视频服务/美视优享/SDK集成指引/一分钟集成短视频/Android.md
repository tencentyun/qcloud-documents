[](id:step1)
## 步骤一：解压 Demo 工程
1. 下载集成了腾讯特效 TE 的 [UGSV Demo](https://cloud.tencent.com/document/product/616/65875) 工程。本 Demo 基于腾讯特效 SDK S1-04 套餐构建。
2. 替换资源：由于本 Demo 工程使用的 SDK 套餐未必与您实际的套餐一致，因此要将本 Demo 中的相关 SDK 文件替换为您实际使用的套餐的 SDK 文件。具体操作如下：
   - 在 `xmagickit module` 的 `build.gradle` 文件找到
```groovy
api 'com.tencent.mediacloud:TencentEffect_S1-04:latest.release'
```
	替换为您购买的 [套餐依赖包](https://cloud.tencent.com/document/product/616/65891)。
   - 如果您的套餐包含动效和滤镜功能，那么需要在腾讯特效 [SDK 下载页面](https://cloud.tencent.com/document/product/616/65876) 下载对应的资源，将动效和滤镜素材放置在 `xmagickit module` 下的如下目录：
		- 动效：`../assets/MotionRes`
		- 滤镜：`../assets/lut`
3. 将 Demo ⼯程中的 xmagickit 模块引⼊到实际项⽬⼯程中。

[](id:step2)
## 步骤二：打开 app 模块的 build.gradle
将 applicationId 修改成与申请的测试授权⼀致的包名。

[](id:step3)
## 步骤三：SDK 接口集成
可参考 Demo ⼯程的 UGCKitVideoRecord 类。
1. **授权：**
```java
 //鉴权注意事项及错误码详情，请参考 https://cloud.tencent.com/document/product/616/65891#.E6.AD.A5.E9.AA.A4.E4.B8.80.EF.BC.9A.E9.89.B4.E6.9D.83
 XMagicImpl.checkAuth(new TELicenseCheck.TELicenseCheckListener() {
            @Override
            public void onLicenseCheckFinish(int errorCode, String msg) {
                if (errorCode == TELicenseCheck.ERROR_OK) {
                    loadXmagicRes();
                } else {
                    Log.e("TAG", "auth fail ，please check auth url and key" + errorCode + " " + msg);
                }
            }
        });
```
2. **初始化素材：**
```java
 private void loadXmagicRes() {
        if (XMagicImpl.isLoadedRes) {
            XmagicResParser.parseRes(mActivity.getApplicationContext());
            initXMagic();
            return;
        }
        new Thread(new Runnable() {
            @Override
            public void run() {
                XmagicResParser.copyRes(mActivity.getApplicationContext());
                XmagicResParser.parseRes(mActivity.getApplicationContext());
                XMagicImpl.isLoadedRes = true;
                new Handler(Looper.getMainLooper()).post(new Runnable() {
                    @Override
                    public void run() {
                        initXMagic();
                    }
                });
            }
        }).start();
    }
```
3. **短视频和美颜进行绑定：**
```java
 private void initBeauty() {
        TXUGCRecord instance = TXUGCRecord.getInstance(UGCKit.getAppContext());
        instance.setVideoProcessListener(new TXUGCRecord.VideoCustomProcessListener() {
            @Override
            public int onTextureCustomProcess(int textureId, int width, int height) {
                if (xmagicState == XMagicImpl.XmagicState.STARTED && mXMagic != null) {
                    return mXMagic.process(textureId, width, height);
                }
                return textureId;
            }

            @Override
            public void onDetectFacePoints(float[] floats) {
            }

            @Override
            public void onTextureDestroyed() {
                if (Looper.getMainLooper() != Looper.myLooper()) {  //非主线程
                    boolean stopped = xmagicState == XMagicImpl.XmagicState.STOPPED;
                    if (stopped || xmagicState == XMagicImpl.XmagicState.DESTROYED) {
                        if (mXMagic != null) {
                            mXMagic.onDestroy();
                        }
                    }
                    if (xmagicState == XMagicImpl.XmagicState.DESTROYED) {
                        TXUGCRecord.getInstance(UGCKit.getAppContext()).setVideoProcessListener(null);
                    }
                }
            }
        });
    }
```
4. **暂停/销毁 SDK：**
 `onPause()` 用于暂停美颜效果，可以在 Activity/Fragment 生命周期方法中执行，onDestroy 方法需要在 GL 线程调用（可以在 onTextureDestroyed 方法中调用 XMagicImpl 对象的 `onDestroy()`) ，更多使用请参考视力中 onTextureDestroyed 方法。
```java
            @Override
            public void onTextureDestroyed() {
                if (Looper.getMainLooper() != Looper.myLooper()) {  //非主线程
                    boolean stopped = xmagicState == XMagicImpl.XmagicState.STOPPED;
                    if (stopped || xmagicState == XMagicImpl.XmagicState.DESTROYED) {
                        if (mXMagic != null) {
                            mXMagic.onDestroy();
                        }
                    }
                    if (xmagicState == XMagicImpl.XmagicState.DESTROYED) {
                        TXUGCRecord.getInstance(UGCKit.getAppContext()).setVideoProcessListener(null);
                    }
                }
            }
```
5. **布局中添加承载美颜面板的布局：**
```xml
 <RelativeLayout
        android:id="@+id/panel_layout"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_alignParentBottom="true"
        android:visibility="gone"/>
```
6. **创建美颜对象并添加美颜面板**
```java
   private void initXMagic() {
       if (mXMagic == null) {
           mXMagic = new XMagicImpl(mActivity, getBeautyPanel());
       } else {
           mXMagic.onResume();
       }
   }
```

具体操作请参见 Demo ⼯程的 UGCKitVideoRecord类。

