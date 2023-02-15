# Android 厂商通道参数申请指南

## 小米参数获取

### 注册小米企业开发者账号

小米企业开发者账号的注册方式参考<a href="https://dev.mi.com/console/doc/detail?pId=848">《企业开发者账号注册操作指南》</a>。

### 新建应用

1. 打开小米开放平台，登录**管理控制台**。

   <img src="../../img/android_channel_apply/xiaomi1.png" width=1024x />

2. 在控制台中选择**消息推送**。

   <img src="../../img/android_channel_apply/xiaomi2.png" width=1024x />

3. 点击**创建应用** > **创建手机/平板应用**

   <img src="../../img/android_channel_apply/xiaomi3.png" width=1024x />

4. 在新页面按照指引创建您的应用，输入应用名以及包名，然后点击**创建**。

   <img src="../../img/android_channel_apply/xiaomi4.png" width=1024x />

5. 在完善资料页直接点击**保存**即可。

   <img src="../../img/android_channel_apply/xiaomi5.png" width=1024x />

### 开通推送服务

1. 您将在应用列表中看到一个新的应用，点击**启用推送**。

   <img src="../../img/android_channel_apply/xiaomi6.png" width=1024x />

2. 在新页面选择接受协议并启用。

   > ![注意](./img/caution.png)注意：使用小米推送服务之前请仔细阅读<a href="https://dev.mi.com/console/doc/detail?pId=860">《小米推送技术服务协议》</a>，确保您的应用符合小米服务协议要求。若您的应用未在小米应用商店发布，则可能无法使用小米推送服务。

   <img src="../../img/android_channel_apply/xiaomi7.png" width=1024x />

### 查看应用信息

1. 在应用列表页点击应用后面的**应用信息**。

   <img src="../../img/android_channel_apply/xiaomi8.png" width=1024x />

2. 在新打开的页面点击 AppKey 以及 AppSecret 后的**查看**获取您的 AppKey 以及 AppSecret。

   <img src="../../img/android_channel_apply/xiaomi9.png" width=1024x />

3. 您需要将相关信息配置在 TMF 控制台以及您的 Android 应用中，以便正常使用推送功能。具体方法参见 [使用控制台 - Android 厂商通道配置](./../console-user-manual/use-console.md#android-厂商通道配置) 以及 [接入 Android - 接入厂商推送通道](./../access-android/advanced-usage.md#接入厂商推送通道)。

## 华为参数获取

### 注册华为开发者账号

华为开发者账号的注册方法参考<a href="https://developer.huawei.com/consumer/cn/doc/start/registration-and-verification-0000001053628148">《注册账号》</a>。华为个人开发账号、企业开发账号完成实名认证后均可使用推送服务。个人开发者账号认证参考<a href="https://developer.huawei.com/consumer/cn/doc/start/ht-idrna-0000001200848143">《个人开发者如何实名认证》</a>；如果需要申请企业开发者认证请参考<a href="https://developer.huawei.com/consumer/cn/doc/start/ht-edrna-0000001154848578">《企业开发者如何实名认证》</a>。

### 新建项目

1. 在华为开发者联盟登录开发者账号。

   <img src="../../img/android_channel_apply/huawei1.png" width=1024x />

2. 弹出的隐私申明选择同意即可，点击右上角**管理中心**进入管理界面。

   <img src="../../img/android_channel_apply/huawei2.png" width=1024x />

3. 在管理界面选择**PUSH**。

   <img src="../../img/android_channel_apply/huawei3.png" width=1024x />

4. 进入到 AppGallery Connect，选择**添加项目**。

   <img src="../../img/android_channel_apply/huawei4.png" width=1024x />

5. 按照指引输入项目名称即可。

   <img src="../../img/android_channel_apply/huawei5.png" width=1024x />

### 开通推送服务

1. 打开项目，选择**推送服务** > **立即开通**。

   <img src="../../img/android_channel_apply/huawei6.png" width=1024x />

2. 系统提示选择推送服务适用的地区，点击**确定**即可。

   <img src="../../img/android_channel_apply/huawei7.png" width=1024x />

3. 按照您App的真实情况选择数据处理的地区。

   <img src="../../img/android_channel_apply/huawei8.png" width=1024x />

### 添加应用

1. 点击左侧菜单的**项目设置**打开设置页。

   <img src="../../img/android_channel_apply/huawei9.png" width=1024x />

2. 点击**添加应用**，在新页面按照指引填写您的应用信息。

   <img src="../../img/android_channel_apply/huawei10.png" width=1024x />

3. 按照提示获取 agconnect-services.json 文件并添加到您的Android项目中，然后点击**下一步**至完成即可。

   <img src="../../img/android_channel_apply/huawei11.png" width=1024x />

### 查看应用信息

1. 回到项目设置页面，滚动到页面最底部应用部分（注意不是项目部分），可以看到App的 AppID、ClientID以及ClientSecret。

   <img src="../../img/android_channel_apply/huawei12.png" width=1024x />

2. 您需要将相关信息配置在 TMF 控制台以及您的 Android 应用中，以便正常使用推送功能。具体方法参见 [使用控制台 - Android 厂商通道配置](./../console-user-manual/use-console.md#android-厂商通道配置) 以及 [接入 Android - 接入厂商推送通道](./../access-android/advanced-usage.md#接入厂商推送通道)。

## 荣耀参数获取

### 注册荣耀开发者账号

荣耀开发者账号的注册方法参考<a href="https://developer.hihonor.com/cn/doc/guides/100272">《帐号注册》</a>。荣耀暂不支持注册个人开发者账号，使用推送服务需要进行企业账号实名认证。实名认证方法参考<a href="https://developer.hihonor.com/cn/doc/guides/100273">《实名认证》</a>。

### 新建应用

1. 登录荣耀开发者平台进入**管理中心**。

   <img src="../../img/android_channel_apply/rongyao1.png" width=1024x />

2. 点击左侧菜单**生态服务**，选择**我的应用**。

   <img src="../../img/android_channel_apply/rongyao4.png" width=1024x />

3. 在新页面点击**新建应用**。

   <img src="../../img/android_channel_apply/rongyao5.png" width=1024x />

4. 按照指引填写您的应用信息，点击**创建**即可。

   <img src="../../img/android_channel_apply/rongyao6.png" width=512x />

5. 回到应用列表，找到新创建的应用并点击**应用详情**。

   <img src="../../img/android_channel_apply/rongyao7.png" width=1024x />

6. 点击**添加证书指纹**，填入您App签名的指纹。之后下载 hcs-services.json，并添加到您的Android项目中。然后点击保存退出页面。

   <img src="../../img/android_channel_apply/rongyao8.png" width=1024x />

您可以通过JDK bin目录下的keytool.jar，获取您的签名证书指纹。其中\<keystore-file\>为签名文件的路径。

```bash
keytool -list -v -keystore <keystore-file>
```

从结果中找到对应的证书指纹 - SHA256摘要信息。

<img src="../../img/android_channel_apply/rongyao12.png" width=1024x />

如果没有签名文件或密钥口令，也可以通过应用Apk包获取签名信息。其中\<apk-file\>为Apk文件的路径。

```bash
keytool -list -printcert -jarfile <apk-file>
```

从结果中找到对应的证书指纹 - SHA256摘要信息。

<img src="../../img/android_channel_apply/rongyao13.png" width=1024x />

### 开通推送服务

1. 点击左侧菜单**开放能力**，选择**推送服务**。

   <img src="../../img/android_channel_apply/rongyao2.png" width=1024x />

2. 在推送服务页面，点击**申请推送服务**。

   <img src="../../img/android_channel_apply/rongyao3.png" width=1024x />

3. 此处选择您刚才新建的应用，勾选同意服务并提交。

   <img src="../../img/android_channel_apply/rongyao9.png" width=1024x />

### 查看应用信息

1. 在推送服务的应用列表点击应用后的**查看**。

   <img src="../../img/android_channel_apply/rongyao10.png" width=1024x />

2. 在新页面获取您 App 的 AppID、AppSecret、ClientID以及ClientSecret。

   <img src="../../img/android_channel_apply/rongyao11.png" width=1024x />

3. 您需要将相关信息配置在 TMF 控制台以及您的 Android 应用中，以便正常使用推送功能。具体方法参见 [使用控制台 - Android 厂商通道配置](./../console-user-manual/use-console.md#android-厂商通道配置) 以及 [接入 Android - 接入厂商推送通道](./../access-android/advanced-usage.md#接入厂商推送通道)。

## OPPO 参数获取

### 注册OPPO开发者账号

OPPO开发者账号的注册方法参考<a href="https://open.oppomobile.com/new/developmentDoc/info?id=11476">《开发者帐号注册流程》</a>。您需要注册OPPO企业开发者账号才能使用OPPO推送服务。

### 新建应用

1. 登录OPPO开放平台，进入**管理中心**。

   <img src="../../img/android_channel_apply/OPPO1.png" width=1024x />

2. 打开**应用服务平台**。

   <img src="../../img/android_channel_apply/OPPO2.png" width=1024x />

3. 点击**创建应用**。

   <img src="../../img/android_channel_apply/OPPO3.png" width=1024x />

4. 按照提示选择应用类型。

   <img src="../../img/android_channel_apply/OPPO4.png" width=1024x />

5. 填入您的应用名称以及包名，点击**提交**完成创建。

   <img src="../../img/android_channel_apply/OPPO5.png" width=1024x />

   > ![说明](./img/note.png)说明：在使用正式推送服务之前，您需要完成 OPPO 应用商店的接入，具体方式参考<a href="https://open.oppomobile.com/new/developmentDoc/info?id=11477">《接入软件商店》</a>。

### 开通推送服务

1. 打开管理中心，进入应用服务平台。点击左侧菜单的**开发服务** > **消息推送**，然后选择您的应用。

   <img src="../../img/android_channel_apply/OPPO6.png" width=1024x />

2. 点击**申请开通**，待审核完成即可。

   <img src="../../img/android_channel_apply/OPPO7.png" width=1024x />

   > ![说明](./img/note.png)说明：未上架应用申请权限后仅可用于测试，每个应用每天推送上限为1000条。正式权限需要在应用上架后重新申请通知栏权限。

### 信道配置

为了能够正常展示 TMF 的通知消息，您需要为 TMF 创建推送信道。通信信道分为公信信道以及私信信道：公信信道用于推送热点新闻、新品推广、平台公告、社区话题、有奖活动等，多用户普适性的内容；私信信道用于推送个人订单变化、快递通知、订阅内容更新、评论互动、会员积分变动等，与单个用户信息强相关的内容。公信信道权限默认为开通状态，私信信道权限则需要单独申请。如果未配置私信信道，您将无法正常在 OPPO 平台使用 TMF 的私信推送功能。

#### 私信信道权限申请

关于公信信道以及私信信道的区别，以及私信信道的申请方式，参考 OPPO 文档<a href="https://open.oppomobile.com/new/developmentDoc/info?id=11227">《推送私信通道申请》</a>。

#### 新建信道

1. 在管理中心选择**OPPO PUSH**。

   <img src="../../img/android_channel_apply/OPPO8.png" width=1024x />

2. 在界面上方选择您的应用，然后点击左侧菜单**配置管理** > **新建通道**。

   <img src="../../img/android_channel_apply/OPPO9.png" width=1024x />

3. 创建一个 ID 为 tmf_push_channel 的公信通道。

   <img src="../../img/android_channel_apply/OPPO10.png" width=1024x />

4. 创建一个 ID 为 high_system 的私信通道。

   <img src="../../img/android_channel_apply/OPPO11.png" width=1024x />

### 查看应用信息

1. 在 **管理中心** > **应用服务平台** > **移动应用** > **移动应用列表** 找到您的应用，点击**应用详情**。

   <img src="../../img/android_channel_apply/OPPO12.png" width=1024x />

2. 在详情页找到您的 AppID、AppKey以及AppSecret。

   <img src="../../img/android_channel_apply/OPPO13.png" width=1024x />

3. 您需要将相关信息配置在 TMF 控制台以及您的 Android 应用中，以便正常使用推送功能。具体方法参见 [使用控制台 - Android 厂商通道配置](./../console-user-manual/use-console.md#android-厂商通道配置) 以及 [接入 Android - 接入厂商推送通道](./../access-android/advanced-usage.md#接入厂商推送通道)。

## vivo 参数获取

### 注册vivo开发者账号

vivo开发者账号的注册方式参考<a href="https://dev.vivo.com.cn/documentCenter/doc/2">《企业开发者注册》</a>。vivo目前仅支持企业开发者注册。

### 新建应用

1. 进入 vivo 开放平台，登录账号，进入**管理中心**。

   <img src="../../img/android_channel_apply/VIVO1.png" width=1024x />

2. 点击**应用与游戏**。

   <img src="../../img/android_channel_apply/VIVO2.png" width=1024x />

3. 点击**创建应用**。

   <img src="../../img/android_channel_apply/VIVO3.png" width=1024x />

4. 输入您的应用包名与名称，点击**创建**即可。

   <img src="../../img/android_channel_apply/VIVO4.png" width=1024x />

### 开通推送服务

1. 点击管理中心**消息推送**。

   <img src="../../img/android_channel_apply/VIVO5.png" width=1024x />

2. 点击上方**推送申请**。

   <img src="../../img/android_channel_apply/VIVO6.png" width=1024x />

3. 按照指引选择应用并提交申请。

   <img src="../../img/android_channel_apply/VIVO7.png" width=1024x />

### 查看应用信息

1. 进入 **管理中心** > **消息推送**，点击应用后的应用信息。

   <img src="../../img/android_channel_apply/VIVO8.png" width=1024x />

2. 在此查看您的AppID、AppKey以及AppSecret。

   <img src="../../img/android_channel_apply/VIVO9.png" width=1024x />

3. 您需要将相关信息配置在 TMF 控制台以及您的 Android 应用中，以便正常使用推送功能。具体方法参见 [使用控制台 - Android 厂商通道配置](./../console-user-manual/use-console.md#android-厂商通道配置) 以及 [接入 Android - 接入厂商推送通道](./../access-android/advanced-usage.md#接入厂商推送通道)。

## Firebase Cloud Messaging 参数获取

### 创建 Google 账号

Google账号的注册方式参考<a href="https://support.google.com/accounts/answer/27441?hl=zh-Hans">《创建 Google 帐号》</a>。

### 新建应用

1. 登录 Firebase 官网，点击**转到控制台**。

   <img src="../../img/android_channel_apply/Firebase1.png" width=1024x />

2. 点击**创建项目**新建一个项目。

   <img src="../../img/android_channel_apply/Firebase2.png" width=1024x />

3. 按照指引输入项目名称，创建项目。

   <img src="../../img/android_channel_apply/Firebase3.png" width=1024x />

4. 回到控制台，点击您的项目。

   <img src="../../img/android_channel_apply/Firebase4.png" width=1024x />

5. 点击 Android 的机器人图标添加一个 Android 应用。

   <img src="../../img/android_channel_apply/Firebase5.png" width=1024x />

6. 按照指引输入您的应用信息，注册应用。

   <img src="../../img/android_channel_apply/Firebase6.png" width=1024x />

7. 下载 google-services.json 文件，添加到您的 Android 项目中。

   <img src="../../img/android_channel_apply/Firebase7.png" width=1024x />

### 下载密钥配置文件

1. 回到项目控制台，点击您刚才创建的应用旁边的**设置**。

   <img src="../../img/android_channel_apply/Firebase8.png" width=1024x />

2. 选择上方**云消息传递**选项卡。

   <img src="../../img/android_channel_apply/Firebase9.png" width=1024x />

3. 点击 Cloud Messaging API (旧版) 下的菜单，**在 Google Cloud Console 中管理 API**。

   <img src="../../img/android_channel_apply/Firebase10.png" width=1024x />

4. 点击**启用**。

   <img src="../../img/android_channel_apply/Firebase11.png" width=1024x />

5. 回到项目设置，选择服务账号选项卡，点击**生成新的私钥**。

   <img src="../../img/android_channel_apply/Firebase12.png" width=1024x />

6. 点击**生成密钥**，下载密钥文件。

   <img src="../../img/android_channel_apply/Firebase13.png" width=1024x />

7. 请妥善保存您的密钥配置文件，并上传至 TMF 控制台以完成 FCM 的配置。具体方法参见 [使用控制台 - Android 厂商通道配置](./../console-user-manual/use-console.md#android-厂商通道配置)。