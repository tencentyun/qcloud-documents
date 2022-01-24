## 集成准备
**文件准备**：
<table>
<tbody><tr><th>文件类型</th><th>说明</th></tr>
<tr>
<td>xmagic-xxx.aar</td><td>SDK，必选</td>
</tr><tr>
<td>../assets/</td><td>算法模型、素材资源包，必选</td>
</tr><tr>
<td>../jniLibs</td><td>so 库，必选</td>
</tr></tbody></table>

## 导入资源

### 资源

- 添加上述文件准备的全部 `.aar` 文件到 app 工程 `libs` 目录下。
- 将 SDK 包内的 assets/ 目录下的全部资源拷贝到 `../src/main/assets` 目录下。
- 将 jniLibs 文件夹拷贝到工程的 `../src/main/jniLibs` 目录下。

### 导入方法
打开 app 模块的 `build.gradle` 添加依赖引用：

```groovy
android{
    ...
    defaultConfig {
        applicationId "修改成与授权lic绑定的appID"
        ....
    }
    packagingOptions {
        pickFirst '**/libc++_shared.so'
    }
}

dependencies{
    ...
    compile fileTree(dir: 'libs', include: ['*.jar','*.aar'])//添加 *.aar
}
```

## 动态下载 assets、so、动效资源指引

为了减少包大小，您可以将 SDK 所需的 assets 资源、so 库、以及动效资源 MotionRes（部分基础版 SDK 无动效资源）改为联网下载。在下载成功后，将上述文件的路径设置给 SDK。

我们建议您复用 Demo 的下载逻辑，当然，也可以使用您已有的下载服务。动态下载的详细指引，请参见 [腾讯特效 SDK 资源动态下载说明（Android）](https://docs.qq.com/doc/DWHRlU0dlcHlGR3V4)。 

## 整体流程

[](id:step1)
### 步骤一：鉴权

> !部分代码与 Demo 工程中的代码有差异，请以本文档描述为准。

1. 申请授权，得到 License URL 和 License KEY，请参见 [License 指引](https://cloud.tencent.com/document/product/616/65879)。
> !**不需要**把 License 文件下载下来放到本地工程里。
2. 在 Application 的 onCreate 或相关业务模块的初始化代码中设置 URL 和 KEY，触发 license 下载，避免在使用前才临时去下载。
```
LicenceCheck.getInstance().setXMagicLicense(context, URL, KEY);
```
3. 然后在真正要使用美颜功能时 ( 例如 Demo 的 LaunchActivity.java )，再去做鉴权：
```java
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

4. 如果鉴权失败，你可以

[查看鉴权结果及错误码详情]: 

，以定位失败原因。

[](id:step2)
### 步骤二：加载腾讯特效 SDK xmagic-xxx.aar
使用腾讯特效 SDK 生命周期大致如下：
1. 构造美颜 UI 数据，可参考 Demo 工程的 `XmagicResParser.java,XmagicPropertyData.java,XmagicUIState.java` 代码。
2. 预览布局中添加 GLSurfaceView。  
```java
<android.opengl.GLSurfaceView
android:id="@+id/camera_gl_surface_view"
android:layout_width="match_parent"
android:layout_height="match_parent" />
```
3. （可选）快速实现相机。
将 Demo 工程中的 com.tencent.demo.camera 目录拷贝到工程中。利用 `PreviewMgr` 类快速实现相机功能。详细实现可参考 Demo 工程的 `MainActivity.java`。
```java
//初始化相机
mPreviewMgr = new PreviewMgr();
//将布局的GlSurfaceView示例传入相机工具类
mPreviewMgr.onCreate(mGlSurfaceView);
//注册预览纹理数据回调函数
mPreviewMgr.setCustomTextureProcessor((textureId, textureWidth, textureHeight) -> {
	if (mXmagicApi == null) {
			return textureId;
	}
	//调用美颜sdk进行渲染
	int outTexture = mXmagicApi.process(textureId, textureWidth, textureHeight);
	return outTexture;
});

//在Activity中的onResume方法中启动相机
mPreviewMgr.onResume(this, 1280, 720);
```
4. 初始化美颜 SDK，建议放在 Activity 的 `onResume()`方法中。
```java
mXmagicApi = new XmagicApi(this, XmagicResParser.getResPath(),                  
new XmagicApi.OnXmagicPropertyErrorListener()); 
```
- **参数**
 <table>
 <tr><th>参数</th><th>含义</th></tr><tr><td>Context context</td><td>上下文</td>
 </tr><tr>
 <td>String resDir</td><td>资源文件目录，V1版本固定写法</td>
 </tr><tr>
 <td>OnXmagicPropertyErrorListener errorListener</td><td>回调函数实现类</td>
 </tr></table>
- **返回**
 错误码含义对照表：
 <table>
 <tr><th>错误码</th><th>含义</th></tr><tr>
 <td>-1</td><td>未知错误</td>
 </tr><tr>
 <td>-100</td><td>3D 引擎资源初始化失败</td>
 </tr><tr>
 <td>-200</td><td>不支持 GAN 素材</td>
 </tr><tr>
 <td>-300</td><td>设备不支持此素材组件</td>
 </tr><tr>
 <td>-400</td><td>模板 JSON 内容为空</td>
 </tr><tr>
 <td>-500</td><td>SDK版本过低</td>
 </tr><tr>
 <td>-600</td><td>不支持分割</td>
 </tr><tr>
 <td>-700</td><td>不支持 OpenGL</td>
 </tr><tr>
 <td>-800</td><td>不支持脚本</td>
 </tr><tr>
 <td>5000</td><td>分割背景图片分辨率超过2160*3840</td>
 </tr><tr>
 <td>5001</td><td>分割背景图片所需内存不足</td>
 </tr><tr>
 <td>5002</td><td>分割背景视频解析失败</td>
 </tr><tr>
 <td>5003</td><td>分割背景视频超过200秒</td>
 </tr><tr>
 <td>5004</td><td>分割背景视频格式不支持</td>
 </tr>
 </tbody></table>
5. 美颜 SDK 处理每帧数据并返回相应处理结果。
```
int outTexture = mXmagicApi.process(textureId, textureWidth, textureHeight);
```
6. 用于更新指定类型的美颜特效数值。
```java
// 可用的入参属性可以从 XmagicResParser.parseRes() 获得
mXmagicApi.updateProperty(XmagicProperty<?> p);
```
7. 释放美颜 SDK，建议与 Activity 的 `onPause()` 生命周期绑定。
```java
//在 Activity 的 onPause 时调用, 需要在 OpenGL 线程调用
mXmagicApi.onPause();
```
8. 添加素材提示语回调函数（方法回调有可能运行在子线程）。
```java
mXmagicApi.setTipsListener(new XmagicTipsListener() {
	final XmagicToast mToast = new XmagicToast();
	@Override
	public void tipsNeedShow(String tips, String tipsIcon, int type, int duration) {
		mToast.show(MainActivity.this, tips, duration);
	}

	@Override
	public void tipsNeedHide(String tips, String tipsIcon, int type) {
		mToast.dismiss();
	}
});
```

完成上述步骤后，用户即可根据自己的实际需求控制展示时机以及其他设备相关环境。
