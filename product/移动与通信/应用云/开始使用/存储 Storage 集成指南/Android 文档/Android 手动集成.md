如果您无法通过 gradle 远程依赖的方式来集成 SDK，我们提供了手动的方式来集成服务：

### 1. 下载服务资源压缩包。

- 下载 [移动开发平台（MobileLine）核心框架资源包](http://tac-android-libs-1253960454.file.myqcloud.com/tac-core.zip)，并解压。
- 下载 [移动开发平台（MobileLine） Storage 资源包](http://tac-android-libs-1253960454.file.myqcloud.com/tac-storage.zip)，并解压。


### 2. 修改您工程的 AndroidManifest.xml 文件

如果您不是通过 aar 集成，请按照下面的示例代码修改您工程下的 AndroidManifest.xml 文件。

```
<!-- 添加 Analytics 需要的权限 -->
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
<uses-permission android:name="android.permission.READ_PHONE_STATE"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
<uses-permission android:name="android.permission.WRITE_SETTINGS"/>

<application>

...

	<!-- 添加 Analytics 的 provider -->
	<provider
		android:name="com.tencent.mid.api.MidProvider"
		android:authorities="你的包名.TENCENT.MID.V3"
		android:exported="true" >
	</provider>

</application>
```