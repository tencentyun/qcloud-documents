[](id:step1)
## 步骤一：解压 Demo 工程
1. 下载集成了腾讯特效 TE 的 [MLVB Demo](https://mediacloud-76607.gzc.vod.tencent-cloud.com/TencentEffect/Android/2.4.0.108.vcube/MLVB-xmagic-demo.zip) 工程。
2. 将 Demo ⼯程中的 X - magic 模块引⼊到实际项⽬⼯程中。

[](id:step2)
## 步骤二：鉴权
鉴权流程请参考

[https://cloud.tencent.com/document/product/616/65891#.E6.AD.A5.E9.AA.A4.E4.B8.80.EF.BC.9A.E9.89.B4.E6.9D.83](

[](id:step3)
## 步骤三：打开 app 模块的 build.gradle
1. 将 applicationId 修改成与申请的测试授权⼀致的包名。
2. 添加 gson 依赖设置。
```groovy
configurations  {
all*.exclude  group:  'com.google.code.gson'
}
```

[](id:step4)
## 步骤四：SDK 接口集成
可参考 Demo ⼯程的 ThirdBeautyActivity 类。
1. **授权**：
```
XMagicImpl.initAuth(getApplicationContext());
```
2. **初始化素材**：
```java
XmagicLoadAssetsView loadAssetsView = new XmagicLoadAssetsView(this);
loadAssetsView.setOnAssetsLoadFinishListener(new XmagicLoadAssetsView.OnAssetsLoadFinishListener() {
@Override
public void onAssetsLoadFinish() {
XmagicResParser.parseRes();
XmagicUIState.initDatas(XmagicResParser.getProperties());
initXMagic();
}
}); 
```
3. **启动推流设置**：
```java
String userId = String.valueOf(new Random().nextInt(10000));
String pushUrl = AddressUtils.generatePushUrl(streamId, userId, 0);
mLivePusher = new V2TXLivePusherImpl(this, V2TXLiveDef.V2TXLiveMode.TXLiveMode_RTC);
mLivePusher.enableCustomVideoProcess(true, V2TXLivePixelFormatTexture2D, V2TXLiveBufferTypeTexture);
mLivePusher.setObserver(new V2TXLivePusherObserver() {
	@Override
	public void onGLContextCreated() {
	}

	@Override
	public int onProcessVideoFrame(V2TXLiveDef.V2TXLiveVideoFrame srcFrame, V2TXLiveDef.V2TXLiveVideoFrame dstFrame) {
		if (mXMagic != null) {
			dstFrame.texture.textureId = mXMagic.process(srcFrame.texture.textureId, srcFrame.width, srcFrame.height);
		}
		return srcFrame.texture.textureId;
		}

		@Override
		public void onGLContextDestroyed() {
		if (mXMagic != null) {
			mXMagic.onDestroy();
		}
	}
});
mLivePusher.setRenderView(mPushRenderView);
mLivePusher.startCamera(true);
int ret = mLivePusher.startPush(pushUrl);
mLivePusher.startMicrophone();
```
4. **将 textureId 传入到 SDK 内做渲染处理**：
在 V2TXLivePusherObserver 接口的 `onProcessVideoFrame(V2TXLiveDef.V2TXLiveVideoFrame srcFrame, V2TXLiveDef.V2TXLiveVideoFrame dstFrame)` 方法中添加如下代码。
```java
if (mXMagic != null) {
	dstFrame.texture.textureId = mXMagic.process(srcFrame.texture.textureId, srcFrame.width,srcFrame.height);
}
return srcFrame.texture.textureId;
```
5. **暂停/销毁 SDK**：
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
7. **初始化面板与美颜设置回调接口**：
具体操作请参见 Demo⼯程的 `ThirdBeautyActivity.initXMagic();` ⽅法。
