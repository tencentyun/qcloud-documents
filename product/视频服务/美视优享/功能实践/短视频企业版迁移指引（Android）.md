目前，短视频企业版已经下线，其中美颜模块解耦升级成为腾讯特效SDK。腾讯特效 SDK 美颜效果更加自然，产品功能更加强大，集成方式更加灵活。本文是短视频企业版升级为腾讯特效（美颜特效）的迁移指引。

## 注意事项
1. 修改 xmagic 模块中的 glide 库的版本号，与实际使用保持一致。
2. 修改 xmagic 模块中的最低版本号，与实际使用保持一致。


## 集成步骤
### 步骤一：解压 Demo 工程
1. 下载集成了腾讯特效 TE 的 [UGSV Demo](https://mediacloud-76607.gzc.vod.tencent-cloud.com/TencentEffect/Android/2.4.1.115.vcube/UGSV_Demo.zip) 工程。本 Demo 基于腾讯特效 SDK S1-04 套餐构建。
2. 替换资源。由于本 Demo 工程使用的 SDK 套餐未必与您实际的套餐一致，因此要将本 Demo 中的相关 SDK 文件替换为您实际使用的套餐的 SDK 文件。具体操作如下：
   - 删除 xmagic 模块中 libs 目录下的 `.aar`文件，将 SDK 中 libs 目录下的 `.aar` 文件拷贝进 xmagic 模块中 libs 目录下。
   - 删除 xmagic 模块中 assets 目录下的所有文件，将 SDK 中的 `assets/` 目录下的全部资源拷贝到 xmagic 模块 `../src/main/assets` 目录下，如果SDK 包中的 MotionRes 文件夹内有资源，将此文件夹也拷贝到 `../src/main/assets` 目录下 。
   - 删除 xmagic 模块中jniLibs目录下的所有 .so 文件，在 SDK 包内的 jniLibs 中找到对应的 .so 文件（由于 SDK 中 jinLibs 文件夹下的 arm64-v8a 和 armeabi-v7a 的 .so 文件在压缩包中，所以需要先解压），拷贝到 xmagic 模块中的 `../src/main/jniLibs` 目录下。
3. 将 Demo ⼯程中的 xmagic 模块引⼊到实际项⽬⼯程中。

### 步骤二：SDK 版本升级
将 SDK 从 Enterprise 版本升级为 Professional 版本。
- **替换前**：`implementation 'com.tencent.liteav:LiteAVSDK_Enterprise:latest.release'`
- **替换后**：`implementation 'com.tencent.liteav:LiteAVSDK_Professional:latest.release'`

### 步骤三：设置美颜 License
1. 在项目中的 application 的 oncreate 方法中调用如下方法：
```java
XMagicImpl.init(this);
XMagicImpl.checkAuth(null);
```
2. 在 XMagicImpl 类中替换成您申请的腾讯特效 **License URL 和 Key**。

### 步骤四：代码实现
以小视频录制界面（TCVideoRecordActivity.java）为例。

1. 在 `TCVideoRecordActivity.java` 类中添加如下变量代码。
```java
private XMagicImpl mXMagic;
private int isPause = 0;//0 非暂停，1暂停，2暂停中 3.表示要销毁
```
2. 在 `TCVideoRecordActivity.java` 类 onCreate 方法后边添加如下代码。
```java
TXUGCRecord instance = TXUGCRecord.getInstance(this);
instance.setVideoProcessListener(new TXUGCRecord.VideoCustomProcessListener() {
	 @Override
	 public int onTextureCustomProcess(int textureId, int width, int height) {
			 if (isPause == 0 && mXMagic != null) {
					 return mXMagic.process(textureId, width, height);
			 }
			 return 0;
	 }

	 @Override
	 public void onDetectFacePoints(float[] floats) {
	 }

	 @Override
	 public void onTextureDestroyed() {
			 if (Looper.getMainLooper() != Looper.myLooper()) {  //非主线程
					 if (isPause == 1) {
							 isPause = 2;
							 if (mXMagic != null) {
									 mXMagic.onDestroy();
							 }
							 initXMagic();
							 isPause = 0;
					 } else if (isPause == 3) {
							 if (mXMagic != null) {
									 mXMagic.onDestroy();
							 }
					 }
			 }
	 }
});
XMagicImpl.checkAuth((errorCode, msg) -> {
	 if (errorCode == TELicenseCheck.ERROR_OK) {
			 loadXmagicRes();
	 } else {
			 TXCLog.e("TAG", "鉴权失败，请检查鉴权url和key" + errorCode + " " + msg);
	 }
});
```
3. 在 onStop 方法中添加如下代码：
```java
isPause = 1;
if (mXMagic != null) {
	 mXMagic.onPause();
}
```
4. 在 onDestroy 方法中添加如下代码：
```java
isPause = 3;
XmagicPanelDataManager.getInstance().clearData();
```
5. 在 onActivityResult 方法最前边添加如下代码：
```java
if (mXMagic != null) {
	 mXMagic.onActivityResult(requestCode, resultCode, data);
}
```
6. 在此类的最后添加如下两个方法：
```java
private void loadXmagicRes() {
	 if (XMagicImpl.isLoadedRes) {
			 XmagicResParser.parseRes(getApplicationContext());
			 initXMagic();
			 return;
	 }
	 new Thread(() -> {
			 XmagicResParser.setResPath(new File(getFilesDir(), "xmagic").getAbsolutePath());
			 XmagicResParser.copyRes(getApplicationContext());
			 XmagicResParser.parseRes(getApplicationContext());
			 XMagicImpl.isLoadedRes = true;
			 new Handler(Looper.getMainLooper()).post(() -> {
					 initXMagic();
			 });
	 }).start();

}
/**
* 初始化美颜SDK
*/
private void initXMagic() {
	 if (mXMagic == null) {
			 mXMagic = new XMagicImpl(this, mUGCKitVideoRecord.getBeautyPanel());
	 }else {
			 mXMagic.onResume();
	 }
}
```

### 步骤五：对其他类的修改

1. 将 AbsVideoRecordUI 类的 mBeautyPanel 类型修改为 RelativeLayout 类型，getBeautyPanel() 方法返回类型也修改为 RelativeLayout，同时修改对应 XML 中的配置，注掉报错的代码。
2. 注释掉 UGCKitVideoRecord 类中报错的代码。
3. 修改 ScrollFilterView 类中的代码，删除 mBeautyPanel 变量，注释掉报错的代码。

### 步骤六：删除对 beautysettingkit 模块的依赖
在 ugckit 模块的 build.gradle 文件中删除对 beautysettingkit 模块的依赖，编译项目将报错的代码注释掉即可。

