[](id:step1)
## 步骤一：解压 Demo 工程
1. 下载集成了腾讯特效 TE 的 [UGSV Demo](https://mediacloud-76607.gzc.vod.tencent-cloud.com/TencentEffect/Android/2.4.0.108.vcube/UGSV-xmagic-demo.zip) 工程。
2. 将 Demo ⼯程中的 xmagic 模块引⼊到实际项⽬⼯程中。

[](id:step2)
## 步骤二：授权
> !部分代码与 Demo 工程中的代码有差异，请问本文档描述为准。

1. 申请 License URL 和 License KEY，请参见 [License 指引](https://cloud.tencent.com/document/product/616/65879)。
> !**不需要**把 License 文件下载下来放到本地工程里。
2. 在 TCApplication 的 onCreate 方法中调用下面这个方法 ，触发 License 下载，避免在使用前才临时去下载。
```
import com.tencent.xmagic.license.LicenceCheck;
LicenceCheck.getInstance().setXMagicLicense(context, URL, KEY);
```

3. 然后在真正要使用美颜功能时（例如 XMagicImpl.java 中），再去做鉴权：

```
private void auth() {
	 LicenceCheck.getInstance().setListener(new LicenceCheck.LicenceCheckListener() {
		 @Override
		 public void onLicenceLoaded(int result, String reason) {
			 //在2.4.0版本，如果无需下载，或者下载失败，不会回调这个方法。（后续版本会补齐）
			 //如果有下载，且下载成功，会回调。result为LicenceCheck.ERROR_OK表示下载下来的license文件是有效的
			 if (result == LicenceCheck.ERROR_OK) {
					 checkAuth(context);
			 }
		 }
	 });
	 //再次触发下载（因为有可能之前在onCreate那里触发下载没有成功）
	 LicenceCheck.getInstance().setXMagicLicense(context,URL,KEY);

	 checkAuth(context);
}

private boolean authorized = false;
private synchronized void checkAuth(Context context) {
	 Log.d(TAG, "checkAuth: authorized=" + authorized);
	 if (authorized) {
		 return;
	 }
	 LicenceCheck mLicenceCheck = LicenceCheck.getInstance();
	 String licenseInfo = mLicenceCheck.getBase64Licence();
	 if (TextUtils.isEmpty(licenseInfo)) {
		 licenseInfo = mLicenceCheck.getLicensePathBase64();
	 }
	 if (TextUtils.isEmpty(licenseInfo)) {
		 Log.d(TAG, "licenseInfo is empty");
		 authorized = false;
	 } else {
		 Auth.AuthResult result = Auth.authByBase64(context, licenseInfo, "");

		 String msg = Json.toJsonStr(result);
		 Log.d(TAG, "isSucceed=" + result.isSucceed);
		 Log.d(TAG, "msg=" + msg);
		 authorized = result.isSucceed;
	 }

	 if (authorized) {
		 //TODO 鉴权成功，在这里通知UI刷新、执行下一步操作之类的事情
	 }
}
```

>? 如果鉴权失败，您可参考 [查看鉴权结果及错误码说明](https://cloud.tencent.com/document/product/616/68760) 定位失败原因。

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
可参考 Demo ⼯程的 TCVideoRecoredActivity 类。
1. **授权：**
```
XMagicImpl.initAuth(getApplicationContext());
```
2. **初始化素材：**
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
3. **开启推流设置：**
```
TXUGCRecord instance = TXUGCRecord.getInstance(this);
instance.setVideoProcessListener(new TXUGCRecord.VideoCustomProcessListener() {
    @Override
    public int onTextureCustomProcess(int textureId, int width, int height) {
        if (isPause == 0 && mXMagic !=null) {
            return mXMagic.process(textureId, width, height);
        }
        return 0;
    }
    @Override
    public void onDetectFacePoints(float[] floats) {
    }
    @Override
    public void onTextureDestroyed() {
        ...
    }
});
```
4. **将 textureId 传入到 SDK 内做渲染处理：**
在 VideoCustomProcessListener 接口的 `onTextureCustomProcess(int textureId, int width, int height)` 方法内添加如下代码。
```java
if (isPause == 0 && mXMagic !=null) {
    return mXMagic.process(textureId, width, height);
}
return 0;
```
5. **暂停/销毁 SDK：**
> !当调用onPause方法后，需要调用 onDestroy 方法销毁，如果需要再次使用，则需要重新创建 mXMagic 对象。
>
```java
mXMagic.onPause();   //暂停，与Activity的onPause方法绑定
mXMagic.onDestroy();  //销毁，与Activity的onDestroy方法绑定
```
6. **布局中添加 SDK 美颜面板：**
```xml
<include
    layout="@layout/xmagic_panel"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:layout_alignParentBottom="true"
    android:visibility="gone"/>
```
7. **初始化面板与美颜设置回调接口：**
具体操作请参见 Demo ⼯程的 `TCVideoRecoredActivity.initXMagic();` ⽅法。
