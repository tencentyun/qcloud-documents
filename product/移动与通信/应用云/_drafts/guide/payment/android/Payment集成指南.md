在 [MobileLine Android 集成手册](replaceme) 中，我们根据控制台向导提供了最简单的方式来接入 MobileLine 的各种服务，同时您也可以不完全依赖向导来接入我们的计费以及其他服务。

计费服务和其他服务在集成时会有不同，因为计费服务在使用前需要您自己配置好和计费服务交互的服务器，并在 MobileLine 控制台上配置好支付的渠道信息。

## 准备

您首先需要一个 Android 工程，这个工程可以是您现有的工程，也可以是您新建的一个空的工程。

## 第一步：创建 MobileLine 项目和应用

在使用我们的服务前，您必须先在 [MobileLine 控制台](https://console.cloud.tencent.com/tac) 上创建项目，每个项目下可以包含多个应用，如 Android 或者 IOS 应用，当然，您也可以在同一个项目下创建多个 Android 或者 IOS 应用。

### 创建项目

首先登录 [MobileLine 控制台](https://console.cloud.tencent.com/tac) ，然后点击【创建第一个项目】按钮来创建一个新的项目，例如，下图这里创建了一个名为 MyGreatApp 的项目：

![](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/guides/mobileLine/guide/newProject.png)


### 创建应用

创建好项目后，我们在 MyGreatApp 项目下创建应用，点击【创建 IOS 应用】或者【创建 Android 应用】按钮来创建应用，如图这里【创建 Android 应用】：

![](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/guides/mobileLine/guide/newApp.png)

填写好 **应用名称** 和 **应用包名** 后，选择下一步。到此，您便已创建好了一个 MobileLine 应用，此时，您可以点击关闭向导。

![](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/guides/mobileLine/guide/loginApp.png)

> 如果您之前已经创建过 MobileLine 应用了，那么你可以选择使用之前的 MobileLine 应用或者创建一个新的应用。

## 第二步：添加配置文件

在您创建好的应用上点击【下载配置】来下载该应用的配置文件的压缩包：

![](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/guides/mobileLine/guide/downloadConfig2.png)

解压该压缩包，您会得到 `tac_service_configurations.json` 和 `tac_service_configurations_unpackage.json` 两个文件，请您如图所示添加到您自己的工程中去。

<img src="http://tac-android-libs-1253960454.cosgz.myqcloud.com/tac_android_configuration.jpg" width="50%" height="50%">

> 请您按照图示来添加配置文件，`tac_service_configurations_unpackage.json` 文件中包含了不可泄露的机密信息，请不要打包到 apk 文件中，MobileLine SDK 也会对此进行检查，防止由于您误打包造成的机密信息泄露。

## 第三步：集成 SDK

每一个 MobileLine 服务都是一个单独的 SDK，其中 `com.tencent.tac:tac-core` 移动分析服务是其他所有模块的基础模块，`com.tencent.tac:tac-messaging` 是 MobileLine 移动推送服务，因此您在使用我们的移动推送服务时必须同时添加这两个服务。

在您的应用级 build.gradle（通常是 app/build.gradle）添加移动分析和移动推送服务的依赖：

```
dependencies {
    //增加这两行
    compile 'com.tencent.tac:tac-core:1.0.0' 
    compile 'com.tencent.tac:tac-payment:1.0.0' 
}
```

## 第四步：初始化

集成好我们提供的 SDK 后，您需要在您自己的工程中添加初始化代码，从而让 MobileLine 服务在您的应用中进行自动配置。整个初始化的过程很简单，只需要您在 `Application` 的子类中调用 `TACApplication.configure(this)` 语句，然后在 `AndroidManifest.xml` 注册该 `Application` 子类即可。

### 在 `Application` 子类中添加初始代码

如果您自己的应用中已经有了 `Application` 的子类，请在该类的 `onCreate()` 方法中添加配置代码，如果没有，请自行创建：

```
public class MyCustomApp extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    ...
    //增加这行
    TACApplication.configure(this);
  }
}

```
### 在 `AndroidManifest.xml` 文件中注册

在创建好 `Application` 的子类并添加好初始化代码后，您需要在工程的 `AndroidManifest.xml` 文件中注册该 `Application` 类：

```
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
  package="com.example.tac">
  <application
    <!-- 这里替换成你自己的 Application 子类 -->
    android:name="com.example.tac.MyCustomApp"
    ...>
  </application>
</manifest>
```

> 如果该工程之前已经添加过 MobileLine 初始化代码，那么请不要重复添加。

## 第五步：配置支付渠道

支付渠道包括微信支付和 QQ 支付两个渠道，您需要自己在微信开放平台或者腾讯开放平台上申请渠道信息，然后在控制台上进行配置，支付渠道配置请参见 [Payment 支付渠道配置指引](https://cloud.tencent.com/document/product/666/14599)

## 第六步：设置后台服务器

在使用腾讯计费 Payment 服务时，为了保证支付的安全性，Payment 服务器不应该直接和您的 app 进行交互，您需要设置好自己的应用服务器来和我们的 Payment 服务器进行交互，后台服务接口的配置请参见 [后台服务配置](https://cloud.tencent.com/document/product/666/14600)，其中【商品下单】接口和【支付成功回调通知】接口是您的应用服务器中必须配置的两个接口，其他的接口您可以按照自己的需求进行配置。

|接口|作用|备注|
|:--|:--|:--|
|商品下单|在 Payment 后台给商品下单|在您的应用发起支付前，必须先调用商品下单接口来进行下单，并将应答的 pay_info 透传给 Payment SDK，拉起支付|
|支付成功回调通知|用户支付成功后，Payment 后台会将支付结果通知您的应用服务器，支付结果请以这个回调通知为准|支付回调通知的地址需要在 MobileLine 控制台上配置|

> 其他后台服务接口请参考 [后台服务配置](https://cloud.tencent.com/document/product/666/14600)

设置好您的后台服务器后，您必须在 MobileLine 控制台上进行参数配置，首先登录 [MobileLine 控制台](https://console.cloud.tencent.com/tac/)，然后选择您自己的应用，并选择【我的米大师】-> 【参数配置】-> 【修改】：

![](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/guides/payment/A00C563F-1D04-41C6-A037-992B0C6DB080.png)

点击修改后，您需要填写**回调地址**、**应用签名**和**应用包名**参数：

![](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/guides/payment/2AAFE408-47E7-4A5C-B039-E4050501940A.png)

|参数|含义|备注|
|:--|:--|:--|
|主回调地址|当您的应用发布上线后，支付成功回调通知接口的主回调地址|请在您自己的应用服务器上根据支付成功回调通知接口响应该回调。|
|备回调地址|当您的应用发布上线后，支付成功回调通知接口的备用回调地址|请在您自己的应用服务器上根据支付成功回调通知接口响应该回调。|
|沙箱回调地址|当您的应用还未发布上线，处于沙箱测试阶段时，支付成功回调通知接口的回调地址|请在您自己的应用服务器上根据支付成功回调通知接口响应该回调。|
|应用签名|您自己 Android 应用的签名|必须和您 Android 应用的实际签名保持一致，否则会无法拉起支付。|
|应用包名|您自己 Android 应用的包名|请注意必须和您Android 应用的 applicationId 保持一致。|

> 您可以用如下命令生成应用签名，这里假设您的签名文件 alias 为 androiddebugkey，签名文件的示例路径： ~/.android/debug.keystore。
>
> `keytool -exportcert -list -v -alias androiddebugkey -keystore ~/.android/debug.keystore`
>
> 生成的 SHA1 值即为您的应用签名。

填写好所有参数后，请点击【保存 & 预览】按钮将应用发布到沙箱，点击后你可以直接关闭参数配置页并在沙箱中调试应用，当然，您也可以直接发布到线上环境。

|环境|作用|备注|
|:--|:--|:--|
|沙箱环境|Payment 的默认环境，主要用于调试|支付成功后，Payment 服务端会回调控制台上设置的沙箱回调地址。|
|线上环境|当您的应用调试成功后，请您将应用发布上线|上线后，Payment Server 会在您支付成功后回调控制台上设置的主回调地址或者备回调地址。|

> 如果您想详细了解计费 Payment 服务的整个流程，请参考 [Payment 支付流程指南](https://cloud.tencent.com/document/product/666/14879)。


到此您已经成功接入了 MobileLine 移动推送服务。
