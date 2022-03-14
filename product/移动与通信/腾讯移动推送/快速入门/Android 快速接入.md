## 简介

本文档提供移动推送 TPNS  Android 应用快速接入指引。只需按照如下步骤，即可在您的 Android 应用上面使用移动推送 TPNS 服务。

>! 为了避免您的 App 被监管部门通报或下架，请您在接入 SDK 之前务必按照 [Android 合规指南](https://cloud.tencent.com/document/product/548/57361) 在《隐私政策》中增加 TPNS 相关说明，并且在用户同意《隐私政策》后再初始化 TPNS SDK。 
>

## 接入前准备

### 创建 Android 平台应用
1. 接入 SDK 之前，需要您前往移动推送 TPNS  [控制台](https://console.cloud.tencent.com/tpns) 创建产品和 Android 应用，详情请参见 [创建产品和应用](https://cloud.tencent.com/document/product/548/37241) 文档。
   ![](https://main.qcloudimg.com/raw/6c410b88409bb658e3920ec1b764c5c0.png)
2. 完成以上步骤后，进入应用的【配置管理】页面，准备接入。
   ![](https://main.qcloudimg.com/raw/fa8bc3c2c4fdf67cd5b837232fc9457b.png)

## 步骤1：开始接入

1. 在【配置管理】页面中， 单击【快速接入】。
![](https://main.qcloudimg.com/raw/26118ca32c232eae530cd290f9aa2195.png)
2. 按照接入指引的操作顺序完成配置，然后单击【点击验证】。
![](https://main.qcloudimg.com/raw/7c4cf6eddf838d55a4dfa858ac3d6e3f.png)
3. 若出现以下提示，则表示 SDK 接入成功 。
![](https://main.qcloudimg.com/raw/393d62182039f2164517d18b86cdb52a.png)
	若出现以下提示，请确认 App 是否成功注册推送服务，可参见 [接入结果验证](#jierujieguo)。
	![](https://main.qcloudimg.com/raw/b234996ccd14cd5681bda3c5afcb5f30.png)
>!为提升离线抵达率，TPNS SDK 默认开启联合保活能力，开发者可手动关闭，详情请参见 [关闭 TPNS 保活功能](https://cloud.tencent.com/document/product/548/36674#.E5.A6.82.E4.BD.95.E5.85.B3.E9.97.AD-tpns-.E7.9A.84.E4.BF.9D.E6.B4.BB.E5.8A.9F.E8.83.BD.EF.BC.9F)。



<span id="jierujieguo"></span>

## 步骤2：接入结果验证

1. 运行 App，过滤“TPush”关键字，查看相关日志：
   ![](https://main.qcloudimg.com/raw/3534e6c05ab9f6959e6e19d4272dc48b.png)
   如出现有类似上图日志，则表明 TPNS-SDK 的插件集成方式已经成功。
2. 推送服务注册成功的日志如下：
```plaintext
XG register push success with token:6ed8af8d7b18049d9fed116a9db9c71ab4aabb65
```
若未搜索到 Token，请查看注册接口返回的错误码，根据 [错误码对照表](https://cloud.tencent.com/document/product/548/36660) 排查。

## 步骤3：厂商通道快速接入

1. 在配置管理页面打开厂商推送通道开关并配置好应用的 AppId、SecretKey 等信息，申请方式可查看各厂商通道的说明文档。
 - 单击【查看说明文档】，可查看厂商通道说明。
 - 在右侧 AppId、AppKey、AppSecret 处可配置厂商通道信息。
   ![](https://main.qcloudimg.com/raw/054128d0cbc0304e512cc67e36999138.png)
2. 厂商通道信息配置完成后，单击页面上方【配置文件下载】，下载包含厂商通道配置信息的配置文件，然后用该配置文件替换工程文件中旧的配置文件即可。
 ![](https://main.qcloudimg.com/raw/4dfa37ac471c1c3b18cc559d5780a6be.png)

## 问题排查指引

1. 查看插件日志。
 如果集成出现异常，则将 tpns-configs.json 文件中的 “debug” 字段置为 true，运行命令： 
```
./gradlew --rerun-tasks :app:processReleaseManifest 
```
并通过“TpnsPlugin”关键字进行分析。
2. sync projects。
 ![](https://main.qcloudimg.com/raw/30368ed3cb4a25f3c33be46e3c1f2f5d.png)
3. 在项目的 External Libraries 中查看是否有相关依赖。
 ![](https://main.qcloudimg.com/raw/1de82d05f351939883e1870ae7300c44.png)
4. 如果日志显示 `Execution failed for task ':Paracraft:checkTPNS'`，说明检查到有新版本的 TPNS Android SDK 可以升级。如果不希望检查更新，可以在 tpns-configs.json 文件中添加 `"upgrade": false`，效果如下图：
<img src="https://main.qcloudimg.com/raw/9eb6a2e108a7a4d1abdd10ef5c1cffdd.png" width="70%"></img>
5. 使用插件过程中，遇到 Android Gradle 插件版本跟 Gradle 版本不匹配的问题，可以参考 [Android Gradle 插件版本说明](https://developer.android.google.cn/studio/releases/gradle-plugin) 进行版本升级，下图列出了当前各个 Android Gradle 插件版本所需的 Gradle 版本：
![](https://main.qcloudimg.com/raw/3b5fa0267d2a051bf55c9f4521cff844.png)
