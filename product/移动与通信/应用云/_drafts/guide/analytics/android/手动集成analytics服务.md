如果您无法通过 gradle 远程依赖的方式来集成 SDK，我们提供了手动的方式来集成服务：

### 1. 下载资源压缩包

下载请点击 [移动开发平台（MobileLine）核心框架资源包](http://tac-android-libs-1253960454.cosgz.myqcloud.com/1.0.0/tac-core-1.0.0.zip)，并解压。

### 2. 集成 jar 包

将解压得到的所有 jar 文件拷贝到您工程或模块的 libs 目录下。

### 3. 修改您工程的 AndroidManifest.xml 文件

请按照下面的示例代码修改您工程下的 AndroidManifest.xml 文件。

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
