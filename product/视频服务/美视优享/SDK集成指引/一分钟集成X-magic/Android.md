## 集成准备
1. 准备文件：[](id:file)
<table>
<tr><th>文件类型</th><th>说明</th></tr>
<tr>
<td>xmagic.aar</td><td>sdk，必选</td>
</tr><tr>
<td>libauth.aar</td><td>鉴权模块，必选</td>
</tr><tr>
<td>../assets/</td><td>算法模型、素材资源包，必选</td>
</tr><tr>
<td>../jniLibs</td><td>so 库，必选</td>
</tr><tr>
<td>lic</td><td>授权文件，必选</td>
</tr></table>
2. 获取鉴权证书。

## 导入资源[](id:import)
### 资源
- 添加上述 [文件](#file) 准备的全部 `.aar` 文件到 app 工程 libs 目录下。
- 将 lic 文件添加到 `src/main/assets/` 目录下。
- 将 SDK 包内的 assets/ 目录下的全部资源拷贝到 `../src/main/assets` 目录下。
- 将 jniLibs 文件夹拷贝到工程的 `../src/main/` 目录下。

### 导入方法
打开 app 模块的` build.gradle` 添加依赖引用：
```
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
为了减少包大小，你可以将 SDK 所需的 assets 资源、so库、以及动效资源 MotionRes（部分基础版 SDK 无动效资源）改为联网下载。在下载成功后，将上述文件的路径设置给 SDK。

建议您复用 [Demo]() 的下载逻辑，可以使用您已有的下载服务。动态下载的详细指引，请参见 [腾讯特效 SDK 资源动态下载说明（Android）](https://docs.qq.com/doc/DWHRlU0dlcHlGR3V4)。 


## 集成步骤
### 步骤1：鉴权[](id:step1)
1. 获取鉴权证书，将授权文件放入 `../app/src/main/assets/` 目录下。
2. 调用 `Auth.auth(...)`  对 SDK 进行鉴权。
```
//初始化优图授权
AuthResult result = Auth.auth(this, "传入lic文件名", "", "");
String msg = Json.toJsonStr(result);
Log.d(TAG, msg);
```

### 步骤二：加载美颜 SDK：xmagic-xxx.aar[](id:step2)
使用美颜SDK生命周期大致如下：
1. 构造美颜 UI 数据，可参考 Demo 工程的 `XmagicResParser.java,XmagicPropertyData.java,XmagicUIState.java` 代码。
2. 预览布局中添加 GLSurfaceView。
```
<android.opengl.GLSurfaceView
	android:id="@+id/camera_gl_surface_view"
	android:layout_width="match_parent"
	android:layout_height="match_parent" />
```
3. （可选）快速实现相机：将 Demo 工程中的 `com.tencent.demo.camera` 目录拷贝到工程中。利用 PreviewMgr 类快速实现相机功能。详细实现可参考 [Demo]() 工程的 `MainActivity.java`。
```
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
4. 初始化腾讯特效 SDK，建议与 Activity 的 `onResume()` 生命周期绑定。
```
mXmagicApi = new XmagicApi(this, XmagicResParser.getResPath()); 
```
5. 腾讯特效 SDK 处理每帧数据并返回相应处理结果。
```
int outTexture = mXmagicApi.process(textureId, textureWidth, textureHeight);
```
6. 用于更新指定类型的美颜特效数值。
```
// 可用的入参属性可以从 XmagicResParser.parseRes() 获得
mXmagicApi.updateProperty(XmagicProperty<?> p);
```
7. 释放美颜 SDK，建议与 Activity 的 onPause() 生命周期绑定。
```
//在 Activity 的 onPause 时调用, 需要在 OpenGL 线程调用
mXmagicApi.onPause();
```
8. 添加素材提示语回调函数。
```
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