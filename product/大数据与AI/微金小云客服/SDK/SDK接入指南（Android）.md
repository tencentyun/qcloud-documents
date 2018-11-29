管理人员登录 [微金小云客服管理系统](https://ics.webank.com) ，在【系统管理】>【App 接入】单击 Android SDK 接入说明，接入指引如下：
![1](//mc.qcloudimg.com/static/img/e780a5c87f7dd26b80a4fad5ac05ae63/image.png)
### SDK 接入（Android）
接入前请先确保后台接入正常，接入配置为 Android Studio。
云客服 SDK（WeCcsSdk）最低支持到 Android API 14:Android 4.0(ICS)，请在构建项目时注意。
WeCcsSdk 将以 AAR 文件的形式提供。
需要添加下面文档中所示的依赖(将提供的两个 aar 文件加入到 App 工程的'libs'文件夹下面，并且在 **build.gradle** 中添加下面的配置：

```
android{
	//...
	repositories {
		flatDir {
			dirs 'libs' //this way we can find the .aar file in libs folder
		}
	}
}
//添加依赖
dependencies {
	//0. appcompat-v7
	compile 'com.android.support:appcompat-v7:23.1.1'
	//1. 云客服SDK
	compile(name: 'webank-sdk-ccs-openPro-release.aar ', ext: 'aar')
	//2. WeBank图片选择器
	compile(name: 'webank_image_picker-release', ext: 'aar')
	// 3. 依赖的第三方jar包
	compile 'com.google.code.gson:gson:2.3.1' //网络请求json解析
	compile 'com.squareup.okhttp:okhttp:2.4.0' //网络请求
	compile 'com.github.bumptech.glide:glide:3.7.0' //for 图片选择器
}
```
**混淆配置**
将 SDK 中的 webank-ccs-proguard-rules.pro 和 x5_proguard.cfg.pro 拷贝到主工程根目录下，然后通过"-include webank-ccs-proguard-rules.pro" 加入到您的混淆文件中。
### 接口调用
SDK 代码调用的入口为：com.webank.mbank.ccs.WeCcsSdk 这个类。

```
public class WeCcsSdk {
	/**
	* 在Application.onCreate()的时候初始化
	*/
	public void init(Context app);
	...
	/**
	* 需要打开云客服界面时调用此接口，通过Bundle进行参数传递。
	*支持的参数见后面的说明
	*/
	public void launch(Activity ctx, Bundle data) {
	// ...
	}
}
```
WeCcsSdk.launch() 的第二个参数用来传递数据，可以将参数打包到 data(Bundle) 中，必须传递的参数包括：

```
//这些都是WeCcsSdk的成员常量，作为传递数据的key
KEY_USER_ID = "user_id";  //user id                   
KEY_SIGNATURE = "signature";  //签名信息
KEY_NONCE="nonce"; //32位随机字符串
KEY_APP_ID = "app_id";  //APP_ID 
```
其他选填的参数被封装在 com.webank.mbank.ccs.model.User 对象中（它是一个 Parcelable 对象），包括 nickName（昵称），cardNo（证件号码），userName（用户名），sex（性别：男 1 女 2），phoneNum（手机号码）等，可以通过 KEY_USER_INFO 这个名称放到 bundle 中，这些参数可以不传入。
### 接入实例

```
# 自定义Application.onCreate()中：
WeCcsSdk.getInstance().init(this);
# 在MainActivity中点击某个按钮的代码逻辑：
Bundle bundle = new Bundle();
bundle.putString(WeCcsSdk.KEY_NONCE, "随机码xxx");
bundle.putString(WeCcsSdk.KEY_USER_ID, "UserIdxxx");
bundle.putString(WeCcsSdk.KEY_SIGNATURE, "签名信息xxx");
bundle.putString(WeCcsSdk.KEY_APP_ID,"app_id");
WeCcsSdk.getInstance().launch(MainActivity.this, bundle);  
```