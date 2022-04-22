## SDK包体瘦身（Android）

为了减少包体大小，您可将SDK所需的assets资源、so库、以及动效资源MotionRes（部分基础版SDK无动效资源）改为联网下载。在下载成功后，将上述文件的路径设置给SDK。

我们建议你复用demo的下载逻辑，当然，也可以使用你已有的下载服务。

如果复用demo的下载逻辑，请注意一点：demo中默认是开启断点续传功能的，可以确保在下载异常中断后，下次继续从中断点接着下载。如果你也想开启断点续传，请确保你的下载服务器支持断点续传能力。 

**检测方法**

```java
判断服务器是否支持断点续传，看Web服务器是否支持Range请求即可。测试方法是在命令行中执行curl命令：
curl -i --range 0-9 https://你的服务器地址/待下载的文件名
例如：
curl -i --range 0-9 https://mediacloud-76607.gzc.vod.tencent-cloud.com/TencentEffect/Android/2.4.1.119/xmagic_S1-04_android_2.4.1.119.zip
如果返回的内容有Content-Range 字段，则表示服务器支持断点续传。
```

## 1. 动态下载so

so压缩包位于 jniLibs/arm64-v8a 和 jniLibs/armeabi-v7a，如下图所示：

​                 ![img](https://docimg8.docs.qq.com/image/PqkvOfEuWCa40NScdRdY8Q.png?w=1082&h=230)        

**如果你想复用demo中的下载服务** ，步骤如下：

首先计算出这两个zip包的MD5值，Mac上可以直接在命令行使用 "md5 文件路径/文件名"算出MD5，或者使用其他工具软件计算出来。

然后将压缩包上传到你的服务器，得到下载URL。

然后更新demo工程里的ResDownloadConfig里的这几个常量值：

​                 ![img](https://docimg5.docs.qq.com/image/KY7kPjzUb7pAtqjflLqsHQ.png?w=1280&h=434.26310583580613)        

调用 ResDownloadUtil.checkOrDownloadFiles 即可启动下载。

**如果你想要自己做下载服务** ，那么下载完成并解压后，把解压后的路径设置给SDK即可。例如解压完成后so的path = /data/data/com.tencent.pitumotiondemo.effects/files/xmagic_libs

​                 ![img](https://docimg3.docs.qq.com/image/jZHyPD70ByTYVuHWbuUDKg.png?w=586&h=758)        

（我们强烈建议您将so下载到app的私有目录，而不是外部存储，以防so被清理软件误删。同时，建议你根据用户手机的CPU类型按需下载v8a 或 v7a 的so，以加快下载速度，这里可以参考demo工程的LaunchActivity的做法）

接下来调用

```java
XmagicApi.setLibPathAndLoad(path);
auth();
```

即可完成so的加载以及licence的认证。

**当SDK版本更新时，对应的so可能会发生变化，你需要重新下载这些so。建议参考demo中的方式，利用md5进行校验。**

**无论是你自行下载so，还是复用demo中的下载服务，在调用SDK的 auth 接口之前，请先检查so是否已下载好** ，ResDownloadUtil提供了如下方法进行检查。如果已下载好，则将路径设置给SDK，如下所示：

```java
String validLibsDirectory = ResDownloadUtil.getValidLibsDirectory(LaunchActivity.this,

isCpuV8a() ? ResDownloadConfig.DOWNLOAD_MD5_LIBS_V8A : ResDownloadConfig.DOWNLOAD_MD5_LIBS_V7A);
if (validLibsDirectory == null) {
     Toast.makeText(LaunchActivity.this,"libs没有下载好，请先下载",Toast.LENGTH_LONG).show();
     return;
}
XmagicApi.setLibPathAndLoad(validLibsDirectory);
auth();
```



## 2. 动态下载assets资源

如果要动态下载assets资源，那么本地工程的assets里面配置如下：

（1）如果是2.4.0及更高版本，本地assets目录不需要保留任何文件。

（2）如果是2.4.0以下版本，需保留license文件和这4个json配置文件：brand_name.json、device_config.json、phone_info.json、score_phone.json。

接下来，找到SDK中已经打包好的 download_assets.zip：

​                 ![img](https://docimg7.docs.qq.com/image/urx93zCT9DT5RmGk_izuaw.png?w=766&h=240)        

与上文 so 文件的处理方法一样，计算这个 zip 包的MD5，将它上传到服务器得到下载地址。

**如果你想复用demo中的下载服务** ，只需更新下图中的下载地址和MD5

​                 ![img](https://docimg4.docs.qq.com/image/dN-LfZeb0zMUD8wunr9hjQ.png?w=1280&h=433.77777777777777)        

然后调用 ResDownloadUtil.checkOrDownloadFiles 启动下载，调用 ResDownloadUtil.getValidAssetsDirectory 得到下载好的 assets 的 path ，详情请参考 请参考 LaunchActivity.java。

**如果你想要自己做下载服务** ，那么把上面的zip包下载解压之后，需要重新组织一下包内文件的结构，最终的文件结构如下：

​                 ![img](https://docimg1.docs.qq.com/image/9ibLyxei6GXBI0iAWBS3wQ.png?w=486&h=680)        

其中，红框内的 light_assets、light_material 等命名不可随意更改。建议直接复用 ResDownloadUtill里的organizeAssetsDirectory 方法完成整理。

**当SDK版本更新时，对应的 assets 可能会发生变化，为确保兼容性，你需要重新下载这些assets。建议参考demo中的方式，利用md5进行校验** 。

**无论是你自行下载assets，还是复用demo中的下载服务，在进入拍摄之前，请先检查assets是否已下载好** ，ResDownloadUtil提供了如下方法进行检查。如果已下载好，则将路径设置给 XmagicResParser。具体用法请参考 LaunchActivity.java

```java
String validAssetsDirectory = ResDownloadUtil.getValidAssetsDirectory(LaunchActivity.this,ResDownloadConfig.DOWNLOAD_MD5_ASSETS);
if (validAssetsDirectory == null) {
      Toast.makeText(LaunchActivity.this,"assets没有下载好，请先下载",Toast.LENGTH_LONG).show();
      return;
}
XmagicResParser.setResPath(validAssetsDirectory);
startActivity(intent);
```

## 3. 动效资源MotionRes下载

部分基础套餐没有动效资源，可以忽略这一小节。

动效分为六大类，每一类中有若干个zip包，每个zip包是一种动效。根据你购买的套餐类型，这里的文件内容会有所不同。

​                 ![img](https://docimg4.docs.qq.com/image/IWjwSKVNipuA_KhbNLD0CA.png?w=1224&h=416)        

动效资源可以按需下载，比如等用户进入到相关功能页面，或者点击了某个动效的图标之后，再下载。

你需要将这些zip包都上传到服务器，得到每一个zip包的下载地址。

**特别注意：动效资源下载后的目录 MotionRes 需要和上一小节的 light_assets 以及 light_material 的在同一个层级** 。并且每一个特效都需要解压，而不能直接放一个zip包，如下图所示：

​                 ![img](https://docimg8.docs.qq.com/image/vZOx14Pj38GHlDDpVR8Ygw.png?w=682&h=708)        

MotionRes的下载可参考 ResDownloadUtil.checkOrDownloadMotions 方法，建议按需一个个下载。

**如果你想复用demo中的下载服务，那么将 ResDownloadConfig 中的 MOTION_RES_DOWNLOAD_PREFIX 常量值替换为你自己的下载URL前缀即可。**