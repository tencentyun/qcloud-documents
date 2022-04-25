## 集成准备
1. [下载 SDK](https://cloud.tencent.com/document/product/616/65876)，并解压。
2. **准备下列文件**：
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
- 将 SDK 包内的 assets/ 目录下的全部资源拷贝到 `../src/main/assets` 目录下，如果 SDK 包中的 MotionRes 文件夹内有资源，将此文件夹也拷贝到 `../src/main/assets` 目录下 。
- 将 jniLibs 文件夹拷贝到工程的 `../src/main/jniLibs` 目录下。

### 导入方法
打开 app 模块的 `build.gradle` 添加依赖引用：

```groovy
android{
    ...
    defaultConfig {
        applicationId "修改成与授权lic绑定的包名"
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

[](id:download)
## 包体大小瘦身：动态下载 assets、so、动效资源指引

为了减少包大小，您可以将 SDK 所需的 assets 资源、so 库、以及动效资源 MotionRes（部分基础版 SDK 无动效资源）改为联网下载。在下载成功后，将上述文件的路径设置给 SDK。

我们建议您复用 Demo 的下载逻辑，当然，也可以使用您已有的下载服务。动态下载的详细指引，请参见 [SDK 包体瘦身（Android）](https://cloud.tencent.com/document/product/616/73016)。

## 整体流程

[](id:step1)
### 步骤一：鉴权

1. 申请授权，得到 License URL 和 License KEY，请参见 [License 指引](https://cloud.tencent.com/document/product/616/65879)。
> !正常情况下，只要 App成功联网一次，就能完成鉴权流程，因此您**不需要**把 License 文件放到工程的 assets 目录里。但是如果您的 App 在从未联网的情况下也需要使用 SDK 相关功能，那么您可以把 License 文件下载下来放到 assets 目录，作为保底方案，此时 License文件名必须是 `v_cube.license`。
2. 在相关业务模块的初始化代码中设置 URL 和 KEY，触发 License 下载，避免在使用前才临时去下载。也可以在 Application 的 onCreate 方法里触发下载，但不建议，因为此时可能没有网络权限或联网失败率较高。
```
//如果仅仅是为了触发下载或更新license，而不关心鉴权结果，则第4个参数传入null。
TELicenseCheck.getInstance().setXMagicLicense(context, URL, KEY, null);
```
3. 然后在真正要使用美颜功能前( 例如 Demo 的 `LaunchActivity.java`)，再去做鉴权：
```java
// 如果您的so库是从网络下载的，那么请在调用TELicenseCheck.getInstance().setTELicense之前，先设置so的路径，否则鉴权会失败。
// XmagicApi.setLibPathAndLoad(validLibsDirectory);
// 如果您的so内置在apk包内，则无需调用上面的方法。
TELicenseCheck.getInstance().setTELicense(context, URL, KEY, new TELicenseCheckListener() {

            @Override
            public void onLicenseCheckFinish(int errorCode, String msg) {
                //注意：此回调不一定在调用线程
                if (errorCode == TELicenseCheck.ERROR_OK) {
                    //鉴权成功
                } else {
                    //鉴权失败
                }
            }
        });
```
**鉴权 errorCode 说明：**
<table>
<thead>
<tr>
<th>错误码</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>0</td>
<td>成功。Success</td>
</tr>
<tr>
<td>-1</td>
<td>输入参数无效，例如 URL 或 KEY 为空</td>
</tr>
<tr>
<td>-3</td>
<td>下载环节失败，请检查网络设置</td>
</tr>
<tr>
<td>-4</td>
<td>从本地读取的 TE 授权信息为空，可能是 IO 失败引起</td>
</tr>
<tr>
<td>-5</td>
<td>读取 VCUBE TEMP License文件内容为空，可能是 IO 失败引起</td>
</tr>
<tr>
<td>-6</td>
<td><code>v_cube.license</code> 文件 JSON 字段不对。请联系腾讯云团队处理</td>
</tr>
<tr>
<td>-7</td>
<td>签名校验失败。请联系腾讯云团队处理</td>
</tr>
<tr>
<td>-8</td>
<td>解密失败。请联系腾讯云团队处理</td>
</tr>
<tr>
<td>-9</td>
<td>TELicense 字段里的 JSON 字段不对。请联系腾讯云团队处理</td>
</tr>
<tr>
<td>-10</td>
<td>从网络解析的 TE 授权信息为空。请联系腾讯云团队处理</td>
</tr>
<tr>
<td>-11</td>
<td>把TE授权信息写到本地文件时失败，可能是 IO 失败引起</td>
</tr>
<tr>
<td>-12</td>
<td>下载失败，解析本地 asset 也失败</td>
</tr>
<tr>
<td>-13</td>
<td>鉴权失败，请检查 so 是否在包里，或者已正确设置 so 路径</td>
</tr>
<tr>
<td>3004/3005</td>
<td>无效授权。请联系腾讯云团队处理</td>
</tr>
<tr>
<td>3015</td>
<td>Bundle Id / Package Name 不匹配。检查您的 App 使用的 Bundle Id / Package Name 和申请的是否一致，检查是否使用了正确的授权文件</td>
</tr>
<tr>
<td>3018</td>
<td>授权文件已过期，需要向腾讯云申请续期</td>
</tr>
<tr>
<td>其他</td>
<td>请联系腾讯云团队处理</td>
</tr>
</tbody></table>

[](id:step2)
### 步骤二：资源拷贝
1. 如果您的资源文件是内置在 assets 目录的，那么使用前需要 copy 到 app 的私有目录。您可以提前 copy 好，或者在上一步鉴权成功的回调里执行拷贝操作。示例代码在 Demo 的 `LaunchActivity.java`。
```
XmagicResParser.setResPath(new File(getFilesDir(), "xmagic").getAbsolutePath());
//loading

//copy资源文件到私有目录，只需要做一次
XmagicResParser.copyRes(getApplicationContext());
```
2. 如果您的资源文件是从 [网络动态下载](#download) 的，下载成功后，需要设置资源文件路径。示例代码在 Demo 的 `LaunchActivity.java`。
```
XmagicResParser.setResPath(下载的资源文件本地路径);
```

[](id:step3)
### 步骤三：SDK 初始化及使用方法

使用腾讯特效 SDK 生命周期大致如下：
1. 构造美颜 UI 数据，可参考 Demo 工程的。 `XmagicResParser.java,XmagicUIProperty.java,XmagicPanelDataManager.java` 代码。
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
mPreviewMgr.onCreate(mGlSurfaceView,false);
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
mXmagicApi = new XmagicApi(this, XmagicResParser.getResPath(),new XmagicApi.OnXmagicPropertyErrorListener()); 
```
	- **参数**
 <table>
 <tr><th>参数</th><th>含义</th></tr><tr><td>Context context</td><td>上下文</td>
 </tr><tr>
 <td>String resDir</td><td>资源文件目录，详见请参见 <a href="#step2">步骤二</a></td>
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
5. 添加素材提示语回调函数（方法回调有可能运行在子线程），部分素材会提示用户：点点头、伸出手掌、比心，这个回调就是用于展示类似的提示语。
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
6. 美颜 SDK 处理每帧数据并返回相应处理结果。
```
int outTexture = mXmagicApi.process(textureId, textureWidth, textureHeight);
```
7. 更新指定类型的美颜特效数值。
```java
// 可用的入参属性可以从 XmagicResParser.parseRes() 获得
mXmagicApi.updateProperty(XmagicProperty<?> p);
```
8. Pause美颜 SDK，建议与 Activity 的 `onPause()` 生命周期绑定。
```java
//在 Activity 的 onPause 时调用, 需要在 OpenGL 线程调用
mXmagicApi.onPause();
```
9. 释放美颜 SDK，建议与 Activity 的 `onDestroy() `生命周期绑定。
```java
//注意，此方法需要在GL线程中调用
mXmagicApi.onDestroy()
```

