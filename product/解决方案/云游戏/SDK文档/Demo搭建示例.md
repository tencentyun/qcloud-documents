[](id:web)
## Web 端搭建示例（H5）
1. 引入云游戏的 js 文件。
<dx-codeblock>
::: html html
<script type="text/javascript" src="https://cloud-gaming.myqcloud.com/cloud_gaming_static/tcgsdk.js"></script>
:::
</dx-codeblock>
2. 在页面内定义一个云游戏显示用的锚点，如下所示：
<dx-codeblock>
::: html html
<div id="mount-point"></div>
:::
</dx-codeblock>
3. 页面内按顺序调用 init，start 接口，接口文档见 [前端 JS SDK API 文档](https://cloud.tencent.com/document/product/1162/46134)。
4. 修改 `demo.html` 的 `get_signature` 请求 url，指向自行部署好的 [业务后台服务](https://cloud.tencent.com/document/product/1162/47523)。
5. 刷新页面并等待浏览器连接成功。

[](id:android)
## Android 端搭建示例
### 接入步骤
1. 将 `tcgsdk-1.1.0.1009506_202011262251_release.aar` 拷贝到 libs 目录下。
2. 在应用模块的 `build.gradle` 中加入：
<dx-codeblock>
::: java java
repositories {
 flatDir {dirs 'libs'}
}
dependencies {
 implementation fileTree(include: ['*.jar'], dir: 'libs')
 implementation(name: "tcgsdk-1.1.0.1009506_202011262251_release", ext: 'aar')
}
:::
</dx-codeblock>
3. 进行混淆配置。
由于 native 层代码需要反射调回 java，需要确保 SDK 内的代码都不被混淆，请在 proguard 中添加以下配置：
<dx-codeblock>
::: java java
-keep class org.twebrtc.** {*;}
-keep class com.tencent.tcgsdk.** {*;}
:::
</dx-codeblock>
4. AndroidManifest 配置：
<dx-codeblock>
::: java java
<uses-feature android:name="android.hardware.camera" />
<uses-feature android:name="android.hardware.camera.autofocus" />
<uses-feature
android:glEsVersion="0x00020000"
android:required="true" />
:::
</dx-codeblock>

### 调用示例
<dx-codeblock>
::: java java
private void init() {
	// 1.创建sdk实例并初始化
	TcgSdk2.Builder builder = new TcgSdk2.Builder(this, APP_ID, this, mGameView.getSurfaceRenderer());
	mSDK = builder.timeout(10000)
			.lowFpsThreshold(25, 5)
			.autoReconnect(true)
			.build(); // 初始化
}

// 3.通过客户端clientSession获取serverSession启动游戏
private void start(String clientSession) {
	final RequestQueue queue = Volley.newRequestQueue(this);
	final String param = new Gson().toJson(new GameInfo(clientSession));

	// TODO
	// 客户端业务后台通过param请求云API: 锁定机器 & 创建会话, 获取serverSession
	// API详见: https://cloud.tencent.com/document/product/1162/40738
	// 业务后台返回Base64.decode后的serverSession
	
	String serverSessionDecoded;
	mSDK.start(serverSessionDecoded);
}

// 2.初始化完成后回调得到客户端clientSession
@Override
public void onInitSuccess(String clientSession) {
	// 初始化成功
	start(clientSession);
}
:::
</dx-codeblock>

>? 
- 客户端获取的 clientSession 作为参数传递给 App 后台（传递方式业务方可以自行实现），业务后台请求云 API 锁定机器并创建会话，拿到 serverSession。
- 客户端通过 serverSession 启动游戏。其中，客户端传递 clientSession，App 后台返回 serverSession，传递方式 App 可自行实现。
- SDK 启动游戏之后会通过 ITcgListener 接口把启动过程中的回调告知给客户端，游戏启动后与远端的交互可通过 ITcgSdk 进行。
