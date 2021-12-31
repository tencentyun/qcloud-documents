[](id:step1)
## 步骤一：解压 Demo 工程

1. 下载集成了腾讯特效 TE 的 [TRTC Demo](https://mediacloud-76607.gzc.vod.tencent-cloud.com/TencentEffect/Android/2.4.0.108.vcube/TRTC-xmagic-demo.zip) 工程。
2. 将 Demo ⼯程中的 xmagic 模块引⼊到实际项⽬⼯程中。

[](id:step2)
## 步骤二：授权
- **方法1：**
	1.  在 TRTCApplication 中设置正确的 Key 和 URL，然后在 onCreate 方法中设置 `XMagicLicenseInit.setLicense(context,url,key)` 方法。
	2.  打开 `xmagic/src/main/java/com.tencent.xmagic/XMagicImpl.java` 在 initAuth 方法中获取 licenseInfo 然后把 licenseInfo 添加到 `Auth.authByBase64` 中。
- **方法2：**
	1.  打开 `xmagic/src/main/assets/` 将测试授权的 lic ⽂件添加到该⽬录下。
	2.  打开 `xmagic/src/main/java/com.tencent.xmagic/XMagicImpl.java` 在 initAuth 方法中，将授权⽂件的 lic 添加到接⼝ Auth.auth 中。

[](id:step3)
## 步骤三：打开 app 模块的 build.gradle
1. 将 applicationId 修改成与申请的测试授权⼀致的包名。
2. 添加 gson 依赖设置。
```groovy
configurations{
all*.exclude group:'com.google.code.gson'
}
```

[](id:step4)
## 步骤四：SDK 接口集成
可参考 Demo⼯程的 ThirdBeautyActivity 类。
1. **授权：**
```
XMagicImpl.initAuth(getApplicationContext());
```
2. **初始化素材：**
```java
XmagicLoadAssetsView loadAssetsView = new XmagicLoadAssetsView(this);
loadAssetsView.setOnAssetsLoadFinishListener(new  XmagicLoadAssetsView.OnAssetsLoadFinishListener() {
    @Override
    public void onAssetsLoadFinish() {
        XmagicResParser.parseRes();
        XmagicUIState.initDatas(XmagicResParser.getProperties());
        initXMagic();
    }
}); 
```
3. **开启推流设置：**
```java
mTRTCCloud.setLocalVideoProcessListener(TRTCCloudDef.TRTC_VIDEO_PIXEL_FORMAT_Texture_2D, TRTCCloudDef.TRTC_VIDEO_BUFFER_TYPE_TEXTURE, new TRTCCloudListener.TRTCVideoFrameListener() {
    @Override
    public void onGLContextCreated() {
    }
    @Override
    public int onProcessVideoFrame(TRTCCloudDef.TRTCVideoFrame srcFrame, TRTCCloudDef.TRTCVideoFrame dstFrame) {
    }
    @Override
    public void onGLContextDestory() {
    }
});
```
4. **将 textureId 传入到 SDK 内做渲染处理：**
在 TRTCVideoFrameListener 接口的 `onProcessVideoFrame(TRTCCloudDef.TRTCVideoFrame srcFrame, TRTCCloudDef.TRTCVideoFrame dstFrame)` 方法内添加如下代码： 

```
dstFrame.texture.textureId = mXMagic.process(srcFrame.texture.textureId, srcFrame.width, srcFrame.height);
```
5. **暂停/关闭 SDK：**
> !当调用 onPause 方法后，需要调用 onDestroy 方法销毁，如果需要再次使用，则需要重新创建 mXMagic 对象。
>
```java
mXMagic.onPause();   //暂停，与Activity的onPause方法绑定
mXMagic.onDestroy();  //销毁，与Activity的onDestroy方法绑定
```
6. **布局中添加 SDK 美颜面板**：
```
<include
    android:id="@+id/livepusher_bp_beauty_pannel"
    layout="@layout/xmagic_panel"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:layout_above="@+id/ll_edit_info" />
```
7. **初始化面板与美颜设置回调接口：**
具体操作请参见 Demo⼯程的 `ThirdBeautyActivity.initXMagic();` ⽅法。
