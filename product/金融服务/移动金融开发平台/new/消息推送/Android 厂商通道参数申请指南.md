## 小米参数获取[](id:xiaomi)

### 注册小米企业开发者账号
小米企业开发者账号的注册方式参考<a href="https://dev.mi.com/console/doc/detail?pId=848">《企业开发者账号注册操作指南》</a>。

### 新建应用
1. 打开 [小米开放平台](https://dev.mi.com/platform)，登录**管理控制台**。
![](https://qcloudimg.tencent-cloud.cn/raw/ff53fd99144553d20002eebf4c65d86a.png)
2. 在控制台中选择**消息推送**。
![](https://qcloudimg.tencent-cloud.cn/raw/d711129526a76e6ed286faa8d3ccbbe4.png)
3. 单击**创建应用** > **创建手机/平板应用**。
![](https://qcloudimg.tencent-cloud.cn/raw/41bdfbd263c33caf0fe6577dc61ebfd8.png)
4. 在新页面按照指引创建您的应用，输入应用名以及包名，然后单击**创建**。
![](https://qcloudimg.tencent-cloud.cn/raw/b19c5cdaddf18f9dd1e77b23563cbc40.png)
5. 在完善资料页直接单击**保存**即可。
![](https://qcloudimg.tencent-cloud.cn/raw/92369a2ea09fe6d55a9a0c9181611e25.png)


### 开通推送服务
1. 您将在应用列表中看到一个新的应用，单击**启用推送**。
![](https://qcloudimg.tencent-cloud.cn/raw/ccdaf7d20ef63989f1b01f7097e82f95.png)
2. 在新页面选择接受协议并启用。
>?使用小米推送服务之前请仔细阅读<a href="https://dev.mi.com/console/doc/detail?pId=860">《小米推送技术服务协议》</a>，确保您的应用符合小米服务协议要求。若您的应用未在小米应用商店发布，则可能无法使用小米推送服务。
>
![](https://qcloudimg.tencent-cloud.cn/raw/16ce68ff6c4619d0a0cf53e15562bdad.png)


### 查看应用信息
1. 在应用列表页单击应用后面的**应用信息**。
![](https://qcloudimg.tencent-cloud.cn/raw/b1a039fc030bec31aa736a03e821719f.png)
2. 在新打开的页面单击 AppKey 以及 AppSecret 后的**查看**获取您的 AppKey 以及 AppSecret。
![](https://qcloudimg.tencent-cloud.cn/raw/c25a78d20008ea831c4dce74802f005f.png)
3. 您需要将相关信息配置在 TMF 控制台以及您的 Android 应用中，以便正常使用推送功能。

## 华为参数获取[](id:huawei)

### 注册华为开发者账号
华为开发者账号的注册方法参考<a href="https://developer.huawei.com/consumer/cn/doc/start/registration-and-verification-0000001053628148">《注册账号》</a>。华为个人开发账号、企业开发账号完成实名认证后均可使用推送服务。个人开发者账号认证参考<a href="https://developer.huawei.com/consumer/cn/doc/start/ht-idrna-0000001200848143">《个人开发者如何实名认证》</a>；如果需要申请企业开发者认证请参考<a href="https://developer.huawei.com/consumer/cn/doc/start/ht-edrna-0000001154848578">《企业开发者如何实名认证》</a>。

### 新建项目
1. 在[ 华为开发者联盟 ](https://developer.huawei.com/consumer/cn/)登录开发者账号。
![](https://qcloudimg.tencent-cloud.cn/raw/817028c56090519dc2ee0f5842c5e5f2.png)
2. 弹出的隐私申明选择同意即可，单击右上角**管理中心**进入管理界面。
![](https://qcloudimg.tencent-cloud.cn/raw/ad316b898dfc86b162966184195a4da9.png)
3. 在管理界面选择 **PUSH**。
![](https://qcloudimg.tencent-cloud.cn/raw/de24152127188a2736173669241a4d7d.png)
4. 进入到 AppGallery Connect，选择**添加项目**。
![](https://qcloudimg.tencent-cloud.cn/raw/9b752ac96719a22eda6f18ddae8ffbd8.png)
5. 按照指引输入项目名称即可。
![](https://qcloudimg.tencent-cloud.cn/raw/c8a665d04e636b84cdfbc0be1c63c7de.png)


### 开通推送服务
1. 打开项目，选择**推送服务** > **立即开通**。
![](https://qcloudimg.tencent-cloud.cn/raw/967ac430285723d03865e70db847e8e6.png)
2. 系统提示选择推送服务适用的地区，单击**确定**即可。
![](https://qcloudimg.tencent-cloud.cn/raw/a7685123aa9d2467d902736b2463f9fa.png)
3. 按照您 App 的真实情况选择数据处理的地区。
![](https://qcloudimg.tencent-cloud.cn/raw/e9f9ae371009a0f84de93f65ee04a1a8.png)


### 添加应用
1. 单击左侧菜单的**项目设置**打开设置页。
![](https://qcloudimg.tencent-cloud.cn/raw/248fc9d85b324ff93b7ab945e01c53c9.png)
2. 单击**添加应用**，在新页面按照指引填写您的应用信息。
![](https://qcloudimg.tencent-cloud.cn/raw/af26ceeb9924b4ae0bb833703855a54e.png)
3. 按照提示获取 `agconnect-services.json` 文件并添加到您的 Android 项目中，然后单击**下一步**至完成即可。
![](https://qcloudimg.tencent-cloud.cn/raw/5850c9fcac1c66d924a47b36d1f8e92b.png)


### 查看应用信息
1. 回到项目设置页面，滚动到页面最底部应用部分（注意不是项目部分），可以看到App的 AppID、ClientID以及ClientSecret。
![](https://qcloudimg.tencent-cloud.cn/raw/ac01d3ce8b63a750dc6f6283def0a559.png)
2. 您需要将相关信息配置在 TMF 控制台以及您的 Android 应用中，以便正常使用推送功能。

## 荣耀参数获取[](id:honor)

### 注册荣耀开发者账号
荣耀开发者账号的注册方法参考<a href="https://developer.hihonor.com/cn/doc/guides/100272">《帐号注册》</a>。荣耀暂不支持注册个人开发者账号，使用推送服务需要进行企业账号实名认证。实名认证方法参考<a href="https://developer.hihonor.com/cn/doc/guides/100273">《实名认证》</a>。

### 新建应用
1. 登录 [荣耀开发者平台](https://developer.hihonor.com/cn/) 进入**管理中心**。
![](https://qcloudimg.tencent-cloud.cn/raw/3abe34d9e5afff0b80100a4832739321.png)
2. 单击左侧菜单**生态服务**，选择**我的应用**。
![](https://qcloudimg.tencent-cloud.cn/raw/12e553b069f854791be01b4bc71a8c24.png)
3. 在新页面单击**新建应用**。
![](https://qcloudimg.tencent-cloud.cn/raw/f00c9202f99db4ac0e568f3d7eab3a99.png)
4. 按照指引填写您的应用信息，单击**创建**即可。
![](https://qcloudimg.tencent-cloud.cn/raw/8254f757db9949bc64702bca64cf7326.png)
5. 回到应用列表，找到新创建的应用并单击**应用详情**。
![](https://qcloudimg.tencent-cloud.cn/raw/41e37985654d4517749ee10c9ce739c3.png)
6. 单击**添加证书指纹**，填入您 App 签名的指纹。之后下载 hcs-services.json，并添加到您的 Android 项目中。然后单击保存退出页面。
![](https://qcloudimg.tencent-cloud.cn/raw/2a996827af1060d5464da5fcb13d13a9.png)
您可以通过 JDK bin 目录下的 keytool.jar，获取您的签名证书指纹。其中`\<keystore-file\>`为签名文件的路径。
```bash
keytool -list -v -keystore <keystore-file>
```
从结果中找到对应的证书指纹 - SHA256摘要信息。
![](https://qcloudimg.tencent-cloud.cn/raw/d45d1d61978ed941d5ea12c37ffb8507.png)
如果没有签名文件或密钥口令，也可以通过应用 Apk 包获取签名信息。其中`\<apk-file\>`为 Apk 文件的路径。
```bash
keytool -list -printcert -jarfile <apk-file>
```
从结果中找到对应的证书指纹 - SHA256摘要信息。
![](https://qcloudimg.tencent-cloud.cn/raw/757b6d24d1141311fe9b941561894e7a.png)


### 开通推送服务
1. 单击左侧菜单**开放能力**，选择**推送服务**。
![](https://qcloudimg.tencent-cloud.cn/raw/d2da1fdc8767dd18fd85a3fc6d78fd3d.png)
2. 在推送服务页面，单击**申请推送服务**。
![](https://qcloudimg.tencent-cloud.cn/raw/0c5a1ca0908f0c7dd9f61e7dfc1b0081.png)
3. 此处选择您刚才新建的应用，勾选同意服务并提交。
![](https://qcloudimg.tencent-cloud.cn/raw/f4902d9fef0945c6db0c5faf726b21ee.png)


### 查看应用信息
1. 在推送服务的应用列表单击应用后的**查看**。
![](https://qcloudimg.tencent-cloud.cn/raw/6fb184d156ac5fdeb9e471174378d214.png)
2. 在新页面获取您 App 的 AppID、AppSecret、ClientID 以及 ClientSecret。
![](https://qcloudimg.tencent-cloud.cn/raw/bd261d434de9624874ab25e1cc35ca28.png)
3. 您需要将相关信息配置在 TMF 控制台以及您的 Android 应用中，以便正常使用推送功能。

## OPPO 参数获取[](id:OPPO)

### 注册OPPO开发者账号
OPPO 开发者账号的注册方法参考<a href="https://open.oppomobile.com/new/developmentDoc/info?id=11476">《开发者帐号注册流程》</a>。您需要注册 OPPO 企业开发者账号才能使用 OPPO 推送服务。

### 新建应用
1. 登录[ OPPO 开放平台](https://open.oppomobile.com/)，进入**管理中心**。
![](https://qcloudimg.tencent-cloud.cn/raw/eae4ee831382a1e14cde09245415bbc6.png)
2. 打开**应用服务平台**。
![](https://qcloudimg.tencent-cloud.cn/raw/1c4f02e7685268cc578fd8d30ffc53bc.png)
3. 单击**创建应用**。
![](https://qcloudimg.tencent-cloud.cn/raw/4e4f53d18b1e55615f08dbfc53a8bd8d.png)
4. 按照提示选择应用类型。
![](https://qcloudimg.tencent-cloud.cn/raw/219767a547b79d2aa228338e8523802c.png)
5. 填入您的应用名称以及包名，单击**提交**完成创建。
![](https://qcloudimg.tencent-cloud.cn/raw/8ea3972bc7f2dc06a83759cf1b24be51.png)
>?在使用正式推送服务之前，您需要完成 OPPO 应用商店的接入，具体方式参考<a href="https://open.oppomobile.com/new/developmentDoc/info?id=11477">《接入软件商店》</a>。
>


### 开通推送服务
1. 打开管理中心，进入应用服务平台。单击左侧菜单的**开发服务** > **消息推送**，然后选择您的应用。
![](https://qcloudimg.tencent-cloud.cn/raw/042c44e14e6ad5720fdb2571d445cab5.png)
2. 单击**申请开通**，待审核完成即可。
![](https://qcloudimg.tencent-cloud.cn/raw/06064862c8d4e4ac0e51086d923f4215.png)
>?未上架应用申请权限后仅可用于测试，每个应用每天推送上限为1000条。正式权限需要在应用上架后重新申请通知栏权限。
>


### 信道配置
为了能够正常展示 TMF 的通知消息，您需要为 TMF 创建推送信道。通信信道分为公信信道以及私信信道：公信信道用于推送热点新闻、新品推广、平台公告、社区话题、有奖活动等，多用户普适性的内容；私信信道用于推送个人订单变化、快递通知、订阅内容更新、评论互动、会员积分变动等，与单个用户信息强相关的内容。公信信道权限默认为开通状态，私信信道权限则需要单独申请。如果未配置私信信道，您将无法正常在 OPPO 平台使用 TMF 的私信推送功能。

#### 私信信道权限申请
关于公信信道以及私信信道的区别，以及私信信道的申请方式，参考 OPPO 文档<a href="https://open.oppomobile.com/new/developmentDoc/info?id=11227">《推送私信通道申请》</a>。

#### 新建信道
1. 在管理中心选择 **OPPO PUSH**。
![](https://qcloudimg.tencent-cloud.cn/raw/3c68e4b9c64ffb67e50909ab30b0ab81.png)
2. 在界面上方选择您的应用，然后单击左侧菜单**配置管理** > **新建通道**。
![](https://qcloudimg.tencent-cloud.cn/raw/63512cf9323c0656bca8730ea60840cd.png)
3. 创建一个 ID 为 tmf_push_channel 的公信通道。
![](https://qcloudimg.tencent-cloud.cn/raw/70992b1f94ee480488a860379008de5c.png)
4. 创建一个 ID 为 high_system 的私信通道。
![](https://qcloudimg.tencent-cloud.cn/raw/96280bd558f24db4044afc2372f69ea8.png)


### 查看应用信息
1. 在 **管理中心** > **应用服务平台** > **移动应用** > **移动应用列表** 找到您的应用，单击**应用详情**。
![](https://qcloudimg.tencent-cloud.cn/raw/5f4c678962e549192de5037ae39a73cd.png)
2. 在详情页找到您的 AppID、AppKey 以及 AppSecret。
![](https://qcloudimg.tencent-cloud.cn/raw/75d1543a69e0cfcc9a7b05f8a1f9b0a2.png)
3. 您需要将相关信息配置在 TMF 控制台以及您的 Android 应用中，以便正常使用推送功能。

## vivo 参数获取[](id:vivo)

### 注册 vivo 开发者账号
vivo开发者账号的注册方式参考<a href="https://dev.vivo.com.cn/documentCenter/doc/2">《企业开发者注册》</a>。vivo目前仅支持企业开发者注册。

### 新建应用
1. 进入 [vivo 开放平台](https://dev.vivo.com.cn/documentCenter/doc/2)，登录账号，进入**管理中心**。
![](https://qcloudimg.tencent-cloud.cn/raw/dd178c55cf1b7d732d14ddd0fe04fb99.png)
2. 单击**应用与游戏**。
![](https://qcloudimg.tencent-cloud.cn/raw/8437df5773cef2a2df94908013e9c679.png)
3. 单击**创建应用**。
![](https://qcloudimg.tencent-cloud.cn/raw/dd4b61d0b81cc99dfd5ee2685f53b660.png)
4. 输入您的应用包名与名称，单击**创建**即可。
![](https://qcloudimg.tencent-cloud.cn/raw/7be5b57a3fc572356c9ac72676cccfea.png)

### 开通推送服务
1. 单击管理中心**消息推送**。
![](https://qcloudimg.tencent-cloud.cn/raw/716f44af2767cfac5fd510d6c09b2f74.png)
2. 单击上方**推送申请**。
![](https://qcloudimg.tencent-cloud.cn/raw/96c4c1dcac344a6c4d528f968c3de31d.png)
3. 按照指引选择应用并提交申请。
![](https://qcloudimg.tencent-cloud.cn/raw/8dfdb25d9adcf3ca860908f787c18064.png)


### 查看应用信息
1. 进入 **管理中心** > **消息推送**，单击应用后的应用信息。
![](https://qcloudimg.tencent-cloud.cn/raw/e7bc73543afd7834656cd2710a8556eb.png)
2. 在此查看您的 AppID、AppKey 以及 AppSecret。
![](https://qcloudimg.tencent-cloud.cn/raw/c16e9a0ac0bd97f0a942df91b7bcb566.png)
3. 您需要将相关信息配置在 TMF 控制台以及您的 Android 应用中，以便正常使用推送功能。


### 下载密钥配置文件
1. 回到项目控制台，单击您刚才创建的应用旁边的**设置**。
![](https://qcloudimg.tencent-cloud.cn/raw/7d097270df858c17bad312cd79ce08df.png)
2. 选择上方**云消息传递**选项卡。
![](https://qcloudimg.tencent-cloud.cn/raw/eab254dd81d550163353e5ad25d7fb03.png)
3. 单击 Cloud Messaging API (旧版) 下的菜单，**在 Google Cloud Console 中管理 API**。
![](https://qcloudimg.tencent-cloud.cn/raw/cb459641e313f2576ec9e32f9eec8a67.png)
4. 单击**启用**。
![](https://qcloudimg.tencent-cloud.cn/raw/85d6a5da0a126be22ac1e89fcae01819.png)
5. 回到项目设置，选择服务账号选项卡，单击**生成新的私钥**。
![](https://qcloudimg.tencent-cloud.cn/raw/6e384fe2436032c6f7a3b58a49b428b5.png)
6. 单击**生成密钥**，下载密钥文件。
![](https://qcloudimg.tencent-cloud.cn/raw/912b64442d5a27d8716707ae634e6b2e.png)
7. 请妥善保存您的密钥配置文件，并上传至 TMF 控制台以完成 FCM 的配置。
