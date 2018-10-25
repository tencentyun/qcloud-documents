接入说明
## 1 开发环境
首先请确认已经配置了Java环境并配置好NDK，由于本项目Android客户端采用Java ADT环境开发，建议开发人员使用Java ADT，并且采用android-ndk-r9d或以上版本NDK，Unity3D版本建议使用4.3以上。

## 2 依赖配置
库文件 将GCloudXXX.unityPackage导入Unity工程中，会自动将GCloud的库文件和C#代码导到Plugins和Scripts的独立目录下。其中Android目录如下：

![](https://mc.qcloudimg.com/static/img/398c7397d5208c607930f949f5beaf56/1.png)

GCloud目录列表：

![](https://mc.qcloudimg.com/static/img/477be8c6bd94c2682d4ca2a23182a84b/2.png)
 
需要指出的是，GCloud作为一个独立的project放在Andriod目录下，建议你们将Plugins/Android目录下的文件按以下目录结构组织，否则可能出现找不到相关库文件的错误：

![](https://mc.qcloudimg.com/static/img/deada46e7cbfbbf08ae5fda4591b0084/3.png)

具体原因可以参考下图：

![](https://mc.qcloudimg.com/static/img/e79eeb1e34d8c64bb775e3b5e427d133/4.png)

权限配置 GCloud所依赖的权限如下，在GCloud/AndroidManifest.xml中已经列出，此处不需要项目设置：

    <!-- TODO GCloud接入必须权限模块 START -->
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
    <!-- TODO GCloud接入必须权限模块 END -->

GameId配置 需要在AndroidManifest.xml的Application节点内添加GCloud的GameId配置，示例如下：

    <!-- GCloud 配置 -->
    <meta-data android:name="GCloud.GCloud.GameId" android:value="@string/gcloud_gameId" />

注： gcloud_gameId需要在res/values/strings.xml中定义，或者将"@string/gcloud_gameId"替换为"\ xxxxxx"。（xxxxxx为gameid）

## 3 修改主Activity
GCloud（Android平台）依赖于Java的一些初始化，这些初始化都封装在GCloudPlayerActivity基类里面。 开发者需要修改自己主Activity的基类

Unity的基类：com.tencent.gcloud.unity.GCloudPlayerActivity。

Cocos的基类：com.tencent.gcloud.cocos.GCloudPlayerActivity

示例代码如下：

    public class ApolloTest extends GCloudPlayerActivity{
    	static
    	{
    		System.loadLibrary("abase");
    		System.loadLibrary("TDataMaster");
    		System.loadLibrary("gcloud");
    	}
    }

注： 三个so加载顺序不能变，否则在个别机型上会出现崩溃。

其中，

Unity需要导入：GCloud.jar和GCloudUntiy.jar，

Cocos需要导入：GCloud.jar GCloudCocos.jar。

## 4 导出到Unity工程(Unity)
注：

Cocos请忽略此章节
在实现了Java层逻辑之后需要Android工程导出到Unity工程具体步骤如下：

将ApolloTest导出为jar包，在Java ADT中右键点击工程，选择Export，选择Java下的Jar File，

![](https://mc.qcloudimg.com/static/img/fbb98648dcd5157bb93f7311608bcd7a/5.png)

在JAR Export页面勾选src和gen文件夹，选择导出class文件和资源文件到指定路径下的jar文件。

![](https://mc.qcloudimg.com/static/img/32e63ad7849311864f844a8d54406482/6.png)

在用户逻辑部分无法完全消除waring的条件下可以勾选Export class files with compile warnings选项，为了确保java程序的正确性，请在导出jar包之前确认无编译错误。

![](https://mc.qcloudimg.com/static/img/7a5856bcc5f31c41e1f329f619904800/7.png)

将导出的ApolloTest.jar和ApolloTest依赖的所有jar包、静态库及动态库拷贝至Plugins/Android目录。

打开Unity工程，选择Android工程，勾选Development Build选项，并进行Player Settings设置，首次进行apk发布要先配置Android开发环境。

![](https://mc.qcloudimg.com/static/img/011dcbad93bc1abe32149408313aca95/8.png)

打开Player Settings中的other Settings，将Bundle Identifier设置为自己的包名。

![](https://mc.qcloudimg.com/static/img/5739877648eac4f8040c9225d96846b3/9.png)

完成上述配置后需要进行AndroidManifest.xml（可以参考这个文件）文件的修改包括：
a. 配置项目包名

![](https://mc.qcloudimg.com/static/img/f961d0a51e91fa1c4ed59d4dbba675ca/10.png)

b. 设置target sdk版本和min sdk 版本

![](https://mc.qcloudimg.com/static/img/33eecbe6c461a92b7594643befd8cc5d/b.png)

c. Application 基本设置，包括设置游戏的icon、label、theme，有其他的设置可以自行追加，但对于访问资源的需要确保资源是存在的，否则会发生闪退。

![](https://mc.qcloudimg.com/static/img/723b4cd1252fb57894ae36d00e0be7f9/c.png)

d. 设置ApolloTest为Main Activity并设置系统从ApolloTest启动

![](https://mc.qcloudimg.com/static/img/d38ab7dd9cd411c8eff7a89614537435/11.png)

e. 游戏业务用到的其他Activity都合入AndroidManifest.xml文件中，包括自己开发或引用外部的Activity

f. 需要适配低端机型请将minSdk版本设为合适值，Apollo建议最低适配机型为sdk=9，google官方建议为15以上。
![](https://mc.qcloudimg.com/static/img/9220264e4838740bddc14cfb016d4b9c/12.png)
![](https://mc.qcloudimg.com/static/img/11965a398daca4b96daccbe79dc45403/13.png)

## 5 打包发布（Unity）
Unity3D可以直接发布apk包，本例程的keystore在Sample目录下，password：123456。使用方法如下：

找到user.keystore，输入password，在Alias下拉菜单中选择要用的Keystore并再次输入密码，build出apk就带上了user.keystore。

![](https://mc.qcloudimg.com/static/img/a84aa549472ccee38095d9817e488c37/14.png)

## 6 常见问题
如何看到调用日志?
在真机测试时只需要将手机连上电脑，运行Java ADT，LogCat可以自动获取手机的全部运行日志，请从中筛选。