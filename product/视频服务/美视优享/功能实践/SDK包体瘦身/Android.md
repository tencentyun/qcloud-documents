为了减少包体大小，您可将 SDK 所需的 assets 资源、so 库、以及动效资源 MotionRes（部分基础版 SDK 无动效资源）改为联网下载。在下载成功后，将上述文件的路径设置给 SDK 。

我们建议您复用 Demo 的下载逻辑，当然，也可以使用您已有的下载服务。

如果复用 Demo 的下载逻辑，请注意一点： Demo 中默认是开启断点续传功能的，可以确保在下载异常中断后，下次继续从中断点接着下载。如果您也想开启断点续传，请确保您的下载服务器支持断点续传能力。 

**检测方法**

```java
判断服务器是否支持断点续传，看Web服务器是否支持Range请求即可。测试方法是在命令行中执行curl命令：
curl -i --range 0-9 https://您的服务器地址/待下载的文件名
例如：
curl -i --range 0-9 https://mediacloud-76607.gzc.vod.tencent-cloud.com/TencentEffect/Android/2.4.1.119/xmagic_S1-04_android_2.4.1.119.zip
如果返回的内容有Content-Range 字段，则表示服务器支持断点续传。
```

[](id:so)
## 动态下载 so
so 压缩包位于` jniLibs/arm64-v8a` 和 `jniLibs/armeabi-v7a`，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/785d9f1a64b556343ea8959f14fec646.png)


<dx-tabs>
::: 如果您想复用 Demo 中的下载服务
1. 计算出这两个 ZIP 包的 MD5 值，Mac 上可以直接在命令行使用 `md5 文件路径/文件名` 算出 MD5，或者使用其他工具软件计算出来。
2. 将压缩包上传到您的服务器，得到下载 URL。
3. 更新 Demo 工程里的 ResDownloadConfig 里的这几个常量值：
![](https://qcloudimg.tencent-cloud.cn/raw/66501abfb08e5722e443740e0f190613.png)
4. 调用 `ResDownloadUtil.checkOrDownloadFiles` 即可启动下载。
:::
::: 如果您想自己做下载服务
1. 下载完成并解压后，把解压后的路径设置给 SDK 即可。例如解压完成后：`so 的 path = /data/data/com.tencent.pitumotionDemo.effects/files/xmagic_libs`
<img src="https://qcloudimg.tencent-cloud.cn/raw/c4ee096758d599be54310d740c5026d4.png" width=400px>
>! 强烈建议您将 so 下载到 App 的私有目录，而不是外部存储，以防 so 被清理软件误删。同时，建议您根据用户手机的 CPU 类型按需下载 v8a 或 v7a 的 so，以加快下载速度，这里可以参考 Demo 工程的 LaunchActivity 的做法。
2. 调用下述代码，即可完成 so 的加载以及 Licence 认证。
```java
XmagicApi.setLibPathAndLoad(path);
auth();
```
:::
</dx-tabs>

>! 
>- 当 SDK 版本更新时，对应的 so 可能会发生变化，您需要重新下载这些 so。建议参考 Demo 中的方式，利用 MD5 进行校验。
>- 无论是您自行下载 so，还是复用 Demo 中的下载服务，在调用 SDK 的 auth 接口之前，请先检查 so 是否已下载好 ，ResDownloadUtil 提供了如下方法进行检查。如果已下载好，则将路径设置给 SDK ，如下所示：
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


## 动态下载 assets 资源
如果要动态下载 assets 资源，具体操作如下：

1. 在本地工程的 assets 里进行配置：
     - **2.4.0及更高版本**：本地 assets 目录不需要保留任何文件。
     - **2.4.0以下版本**：需保留 License 文件和这4个 JSON 配置文件：`brand_name.json`、`device_config.json`、`phone_info.json`、`score_phone.json`。
2. 找到 SDK 中已经打包好的 `download_assets.zip`。
![](https://qcloudimg.tencent-cloud.cn/raw/b04e8d991a4aef086229a8610ad8f883.png)
3. 与 [上文 so 文件](#so) 的处理方法一样，计算这个 ZIP 包的 MD5，将它上传到服务器得到下载地址。
<dx-tabs>
::: 如果您想复用 Demo 中的下载服务
1. 更新下图中的下载地址和 MD5。
![](https://qcloudimg.tencent-cloud.cn/raw/5a53c116e2dd4ad8f12891cdd1627820.png)
2. 调用 `ResDownloadUtil.checkOrDownloadFiles` 启动下载，调用 `ResDownloadUtil.getValidAssetsDirectory` 得到下载好的 assets 的 path ，具体用法请参考 `LaunchActivity.java`。
:::
::: 如果您想要自己做下载服务
把上面的 ZIP 包下载解压之后，需要重新组织一下包内文件的结构，最终的文件结构如下：
<img src="https://qcloudimg.tencent-cloud.cn/raw/8ad5eeb526671bea433967c91aa377bc.png" width=400px>
其中，红框内的 light_assets、light_material 等命名不可随意更改。建议直接复用 ResDownloadUtill 里的organizeAssetsDirectory 方法完成整理。
:::
</dx-tabs>

>! 
>- 当 SDK 版本更新时，对应的 assets 可能会发生变化，为确保兼容性，您需要重新下载这些 assets。建议参考 Demo 中的方式，利用 MD5 进行校验 。
>- 无论是您自行下载 assets，还是复用 Demo 中的下载服务，在进入拍摄之前，请先检查 assets 是否已下载好 ，ResDownloadUtil 提供了如下方法进行检查。如果已下载好，则将路径设置给 XmagicResParser。具体用法请参考 `LaunchActivity.java`。
```java
String validAssetsDirectory = ResDownloadUtil.getValidAssetsDirectory(LaunchActivity.this,ResDownloadConfig.DOWNLOAD_MD5_ASSETS);
if (validAssetsDirectory == null) {
      Toast.makeText(LaunchActivity.this,"assets没有下载好，请先下载",Toast.LENGTH_LONG).show();
      return;
}
XmagicResParser.setResPath(validAssetsDirectory);
startActivity(intent);
```

## 动效资源 MotionRes 下载
部分基础套餐没有动效资源，可以忽略这一小节。

动效分为六大类，每一类中有若干个 ZIP 包，每个 ZIP 包是一种动效。根据您购买的套餐类型，这里的文件内容会有所不同。
![](https://qcloudimg.tencent-cloud.cn/raw/e289586793242d7a9b363b42cacb0f38.png)
动效资源可以按需下载，例如等用户进入到相关功能页面，或者单击了某个动效的图标之后，再下载。

您需要将这些 ZIP 包都上传到服务器，得到每一个 ZIP 包的下载地址。
>!**动效资源下载后的目录 MotionRes 需要和上一小节的 light_assets 以及 light_material 的在同一个层级** 。并且每一个特效都需要解压，而不能直接放一个 ZIP 包，如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/2e0951f796b68013d2540891269ddf53.png" width=400px>

MotionRes 的下载可参考 ResDownloadUtil.checkOrDownloadMotions 方法，建议按需一个个下载。

**如果您想复用 Demo 中的下载服务，那么将 ResDownloadConfig 中的 MOTION_RES_DOWNLOAD_PREFIX 常量值替换为您自己的下载 URL 前缀即可。**
