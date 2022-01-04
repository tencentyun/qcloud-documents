## 集成准备[](id:ready)

- **文件准备**
<table>
<tr><th>文件类型</th><th>说明</th></tr>
<tr>
<td>xmagic.aar</td><td>sdk，必选</td>
</tr><tr>
<td>../assets/</td><td>算法模型、素材资源包，必选</td>
</tr><tr>
<td>../jniLibs</td><td>so 库，必选</td>
</tr><tr>
<td>lic</td><td>授权文件，必选</td>
</tr></table>
- **获取鉴权证书**


## 导入资源[](id:upload)
### 资源
- 添加上述 `.aar` 文件到 app 工程 `libs` 目录下。
- 将 lic 文件添加到 `src/main/assets/` 目录下。
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

为了减少包大小，您可以将 SDK 所需的 assets 资源、so库、以及动效资源 MotionRes（部分基础版 SDK 无动效资源）改为联网下载。在下载成功后，将上述文件的路径设置给 SDK。

我们建议您复用 Demo 的下载逻辑，当然，也可以使用您已有的下载服务。动态下载的详细指引，请参见 [腾讯特效 SDK 资源动态下载说明（Android）](https://docs.qq.com/doc/DWHRlU0dlcHlGR3V4)。 

## 整体流程

### 步骤一：鉴权
1. 获取鉴权证书，将授权文件放入 `../app/src/main/assets/` 目录下。
2. 调用 `Auth.auth(...)`  对 SDK 进行鉴权。
```java
//初始化优图授权
AuthResult result = Auth.auth(this, "传入lic文件名", "", "");
String msg = Json.toJsonStr(result);
Log.d(TAG, msg);
```

### 步骤二：加载腾讯特效 SDK xmagic-xxx.aar
使用腾讯特效 SDK 生命周期大致如下：
1. 构造美颜 UI 数据，可参考 Demo 工程的 `XmagicResParser.java,XmagicPropertyData.java,XmagicUIState.java` 代码。
2. 预览布局中添加 GLSurfaceView。 
```
<android.opengl.GLSurfaceView
	android:id="@+id/camera_gl_surface_view"
	android:layout_width="match_parent"
	android:layout_height="match_parent" />
```
3. （可选）快速实现相机。
将 Demo 工程中的 `com.tencent.demo.camera` 目录拷贝到工程中。利用 `PreviewMgr` 类快速实现相机功能。详细实现可参考 Demo 工程的 `MainActivity.java`。
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
//调用腾讯特效 SDK进行渲染
int outTexture = mXmagicApi.process(textureId, textureWidth, textureHeight);
	return outTexture;
});

//在Activity中的onResume方法中启动相机
mPreviewMgr.onResume(this, 1280, 720);
```
4. 初始化腾讯特效 SDK，建议放在 Activity 的 `onResume()`方法中。
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
5. 腾讯特效 SDK 处理每帧数据并返回相应处理结果。
```
int outTexture = mXmagicApi.process(textureId, textureWidth, textureHeight);
```
6. 用于更新指定类型的腾讯特效数值。
```java
// 可用的入参属性可以从 XmagicResParser.parseRes() 获得
mXmagicApi.updateProperty(XmagicProperty<?> p);
```
7. 释放腾讯特效 SDK，建议与 Activity 的 `onPause()` 生命周期绑定。
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
