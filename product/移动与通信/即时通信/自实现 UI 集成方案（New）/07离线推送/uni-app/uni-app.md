## 概述

[TUIOfflinePush](https://ext.dcloud.net.cn/plugin?id=9149) 是腾讯云即时通信 IM Push 插件。目前离线推送支持 Android 和 iOS 平台，设备有：华为、小米、OPPO、vivo、魅族 和 苹果手机。

> !
> 
> - 在没有主动退出登录的情况下，应用退后台、手机锁屏、或者应用进程被用户主动杀掉三种场景下，如果想继续接收到 IM 消息提醒，可以接入即时通信 IM 离线推送。
> - 如果应用主动调用 logout 退出登录，或者多端登录被踢下线，即使接入了 IM 离线推送，也收不到离线推送消息。

## 效果

![](https://qcloudimg.tencent-cloud.cn/raw/ca52cff62e712bbe4e800e4f1e7f0878.png)

## 集成 TUIOfflinePush 跑通离线推送功能

集成 TUIOfflinePush 插件之前，需要申请相关的参数和证书。离线推送功能依赖厂商原始通道，您需要将自己的应用注册到各个厂商的推送平台，得到 AppID 和 AppKey 等参数。

## 条件说明

部分厂商要求必须上架应用市场才可以正常使用推送服务，详情参见下表：

| 厂商通道 | 是否需要上架 | 账号说明 |
| --- | --- | --- |
| 小米  | 是   | 需要注册企业开发者账号 |
| 华为  | 否   | 个人开发者账号即可 |
| 魅族  | 否   | 个人开发者账号即可 |
| vivo | 否   | 需要注册企业开发者账号 |
| OPPO | 是   | 需要注册企业开发者账号 |

## Android 配置


登录腾讯云 [即时通信 IM 控制台](https://console.qcloud.com/avc) ，添加各个厂商推送证书，并将您获取的各厂商的 AppID、AppKey、AppSecret 等参数配置给 IM 控制台的推送证书。
<dx-alert infotype="notice" title="">
由于各大厂商的官网会不定时更新，以下各设备详情流程可能会与官网存在差异，发生差异时，请参见各厂商官网详情：[小米](https://dev.mi.com/console/doc/detail?pId=68)、[华为](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/service-introduction-0000001050040060)、[OPPO](https://open.oppomobile.com/wiki/doc#id=10195)、[vivo](https://dev.vivo.com.cn/documentCenter/doc/281)、[魅族](https://open.flyme.cn/docs?id=8)。
</dx-alert>

<dx-tabs>
::: 小米


#### 步骤1：注册小米开发者账号

进入 [小米开放平台](https://dev.mi.com/console/)，注册小米开发者账号，详情参见 [企业开发者账号注册流程](https://dev.mi.com/console/doc/detail?pId=848)。

#### 步骤2：创建应用
进入**管理控制台**，选择消息推送。
 ![](https://qcloudimg.tencent-cloud.cn/raw/9dedce9bdfa3d158d1fa884ef5b4f823.png)
>!若使用个人账号登录，会显示“抱歉，您当前没有推送/审核权限”。
>
创建应用，完善应用资料界面，单击**保存**。
![](https://qcloudimg.tencent-cloud.cn/raw/a96768040492a8efbdd526aa7e020665.png)
![](https://qcloudimg.tencent-cloud.cn/raw/95a481cc04f7255e103ef463f45716f7.png)
>!应用包名与插件应用包名保持一致。
>

#### 步骤3：启用推送服务

进入**推送运营平台** > **应用列表**页面，在对应的应用名称单击**启用推送**，确定启用。
![](https://qcloudimg.tencent-cloud.cn/raw/5b46e92a85288969842f12dfad29f415.png)

#### 步骤4：获取应用信息

进入**推送运营平台** > **应用信息**页面，即可查看应用信息。
![](https://qcloudimg.tencent-cloud.cn/raw/fb64e566a9195c2c1d4f404d2823025e.png)

#### 步骤5：将应用信息填写到 IM 控制台

<table> 
<tr> 
<th nowrap="nowrap">厂商推送平台</th> 
<th>IM 控制台配置</th> 
</tr> 
<tr> 
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/fbfcba10c2de51e24ff7391c15a5abcd.png" style="zoom:100%;" /></td> 
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/0da9ea0417f941f4fa49cee9cfc8b5f9.png" style="zoom:300%;" /> 
</td> 
</tr> 
</table>

<dx-alert infotype="notice" title="">
- 自动生成**应用内指定界面**链接，不可以修改。
- 该配置用于派发单击后离线推送插件的事件监听，不可以直接配置应用内页面的跳转。
</dx-alert>

:::
::: 华为
#### 步骤1：注册华为开发者账号

进入 [华为开发者联盟](https://developer.huawei.com/consumer/cn/)，注册华为开发者账号，详情参见 [注册账号](https://developer.huawei.com/consumer/cn/doc/start/registration-and-verification-0000001053628148)。

#### 步骤2：创建应用

1. 单击**管理中心**，进入**管理中心**页面。
2. 选择**开发服务** > **PUSH**。
3. 添加一个新的项目，填写项目名称。

![](https://qcloudimg.tencent-cloud.cn/raw/40d50f54b76c478dc640c3059dbcd9f1.png)

#### 步骤3：开通推送服务

1. **项目设置** > **推送服务**页面，单击**立即开通**。
2. 选择数据存储位置。
![](https://qcloudimg.tencent-cloud.cn/raw/155b5cbb80361c18256e35d31e11362c.png)
3. 进入**项目设置** > **API 管理**页面，开启推送服务的权限。
![](https://qcloudimg.tencent-cloud.cn/raw/68679f12fd1f1bbb4a875d4a0596ea72.png)
4. 进入**项目设置** > **常规**页面，单击添加应用。
<dx-alert infotype="notice" title="">
应用包名与插件应用包名保持一致。
</dx-alert>

#### 步骤4：获取应用信息

进入**项目设置** > **常规**页面，即可查看应用信息。
![](https://qcloudimg.tencent-cloud.cn/raw/c4cf1660bc0f42542ca1172f48fea422.png)
<dx-alert infotype="notice" title="">
- 常规页面包含项目和应用的 Client ID 和 Client Secret，两者对应的参数不一致，请下拉至页面底部，获取应用的 Client ID 和 Client Secret。
- 必须添加打包的 [SHA256证书指纹](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/android-config-agc-0000001050170137#section193351110105114)，SHA256 证书指纹需与自己的打包证书一致。
- 下载 agconnect-services.json 文件，放到项目原生插件目录下： nativeplugins/TencentCloud-TUIOfflinePush/android/assets/ 路径下。
- 修改了项目、应用信息、开发服务设置，都需要重新下载配置 agconnect-services.json 文件
  </dx-alert>
	
#### 步骤5：将应用信息填写到 IM 控制台
  ![](https://qcloudimg.tencent-cloud.cn/raw/ec1d06494f7ea33bcf7874ca183423f2.png)
  <dx-alert infotype="notice" title="">
- Client ID 对应 AppID，Client Secret 对应 AppSecret。
- 自动生成**应用内指定界面**链接，不可以修改。
- 该配置用于派发点击后离线推送插件的事件监听，不可以直接配置应用内页面的跳转。
  </dx-alert>
:::
::: OPPO
#### 步骤1：注册 OPPO 开发者账号
  

进入[ OPPO开放平台](https://open.oppomobile.com)，注册 OPPO 开发者账号，详情参见 [OPPO 企业开发者账号注册](https://open.oppomobile.com/new/developmentDoc/info?id=10446)。

#### 步骤2：创建应用

登录 OPPO 企业开发者帐号，并创建应用，详情请参见 [《应用接入流程》](https://open.oppomobile.com/new/developmentDoc/info?id=11476)。

#### 步骤3：开通 PUSH 服务

1. 登录 OPPO 开放平台，依次选择“产品”–“移动服务”–“推送服务”
![](https://qcloudimg.tencent-cloud.cn/raw/cfe2238b64e7e51dab26f1e5caa001e9.png)
2. 进入产品介绍页，点击“申请接入”
3. 进入管理中心界面，为未开启服务的应用申请推送权限：
	- 已开启服务：已申请 PUSH 权限并通过的应用。
	- 未开启服务：可申请 PUSH 权限的应用。
![](https://qcloudimg.tencent-cloud.cn/raw/070051a4512b0af6bf19485d196b2e24.png)
4.单击**申请开通按钮**。在未开启服务中点击需要申请 PUSH 权限的应用，进入 PUSH 服务并点击申请开通。
![](https://qcloudimg.tencent-cloud.cn/raw/b4f551c17a0053729ac4c7cf1be9e020.png)
<dx-alert infotype="notice" title="">

- 通知栏推送：应用需在 OPPO 软件商店上架。
- 通知栏推送测试权限：每天仅可推送1000条消息，限测试使用。应用上架后需重新申请“通知栏推送”权限，以获得正常消息推送数量
- 平台将会在1个工作日内返回审核结果，开发者可以在申请页面查看审核结果，其他问题可咨询开放平台客服。
  
  </dx-alert>
	
#### 步骤4：将应用信息填写到 IM 控制台
<table> 
<tr> 
<th nowrap="nowrap">厂商推送平台</th> 
<th>IM 控制台配置</th> 
</tr> 
<tr> 
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/051de434b51f77711e5a6aa7682abb72.png" style="zoom:100%;" /> </td> 
<td> <img src="https://qcloudimg.tencent-cloud.cn/raw/d13952abf25792258adc97cb3929904f.png" style="zoom:300%;" />
</td> 
</tr> 
</table>
<dx-alert infotype="notice" title="">
- 自动生成**应用内指定界面**链接，不可以修改。
- 该配置用于派发点击后离线推送插件的事件监听，不可以直接配置应用内页面的跳转。
</dx-alert>
:::
::: vivo
#### 步骤1：注册 vivo 开发者账号
  

进入 [vivo开放平台](https://dev.vivo.com.cn/openAbility/pushNews)，注册 vivo 开发者账号，详情参见 [vivo 企业开发者账号注册](https://dev.vivo.com.cn/documentCenter/doc/2)。

#### 步骤2：创建应用

1. 进入**管理中心** > **应用与游戏**页面，单击**创建应用**。详情请见 [《应用创建/更新流程》](https://dev.vivo.com.cn/documentCenter/doc/52)。
![](https://qcloudimg.tencent-cloud.cn/raw/76bd3d95eb24ddca6dc3a42e23eb3b36.png)
2. 填写应用信息后，创建应用。
<dx-alert infotype="notice" title="">
若应用没有上架应用市场，推送权限受限，不可在 vivo 官网的 Web 界面和 API 后台发送正式消息，可在 API 后台向设置的测试设备发送测试消息进行测试。
</dx-alert>

#### 步骤3：申请推送服务

1. 进入**管理中心** > **消息推送**页面。
2. 进入产品介绍页，单击**申请接入**。
3. 单击**推送申请**，选择需要申请的应用名称后提交申请。
![](https://qcloudimg.tencent-cloud.cn/raw/29d2da606eb0b838af44f1ed9e76b85e.png)

#### 步骤4：获取应用信息

进入**推送运营平台** > **应用信息**页面，即可查看应用信息。
![](https://qcloudimg.tencent-cloud.cn/raw/7bb2e921888bdcd495fd9d961a582165.png)

#### 步骤5：将应用信息填写到 IM 控制台

<table> 
<tr> 
<th nowrap="nowrap">厂商推送平台</th> 
<th>IM 控制台配置</th> 
</tr> 
<tr> 
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/a764b271e3ac1de64b3c9342fa9e96b1.png" style="zoom:100%;" /></td> 
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/09757348501da895bb56dc1e7a230bd8.png" style="zoom:300%;" />
</td> 
</tr> 
</table>
<dx-alert infotype="notice" title="">
- 自动生成**应用内指定界面**链接，不可以修改。
- 该配置用于派发点击后离线推送插件的事件监听，不可以直接配置应用内页面的跳转。
</dx-alert>
:::
::: 魅族
#### 步骤1：注册魅族开发者账号

注册魅族开发者账号，详情参见 [开发者注册](http://open-wiki.flyme.cn/doc-wiki/index#id?8)。

#### 步骤2：创建应用

1. 进入**控制台** > **Flyme 推送**页面。
![](https://qcloudimg.tencent-cloud.cn/raw/c61b4f1ae00a99cde3538d0620d64b3c.png)
2. 填写应用信息后，创建应用。
![](https://qcloudimg.tencent-cloud.cn/raw/ab3feeea3690327cbf75bae8768686b7.png)
3. 填写应用信息后点击创建。
<dx-alert infotype="notice" title="">
应用包名与插件应用包名保持一致。
</dx-alert>

#### 步骤3：获取应用信息

在应用列表中选择**打开应用**。进入**配置管理**页面，即可查看应用信息。
![](https://qcloudimg.tencent-cloud.cn/raw/2b32154d617815ed04a18a1430698c6b.png)

#### 步骤4：将应用信息填写到 IM 控制台

<table> 
<tr> 
<th nowrap="nowrap">厂商推送平台</th> 
<th>IM 控制台配置</th> 
</tr> 
<tr> 
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/70ad94d8e843f92247c67a3ae4004c15.png" style="zoom:100%;" /></td> 
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/c4ded9269e0ac59ff58214be1bea89d6.png" style="zoom:300%;" /> 
</td> 
</tr> 
</table>
<dx-alert infotype="notice" title="">
- 自动生成**应用内指定界面**链接，不可以修改。
- 该配置用于派发点击后离线推送插件的事件监听，不可以直接配置应用内页面的跳转。
</dx-alert>
:::
</dx-tabs>

## iOS 配置

### 步骤1：iOS 申请 APNs 证书

向 Apple [申请 APNs 推送证书](https://cloud.tencent.com/document/product/269/75429#.E6.AD.A5.E9.AA.A41.EF.BC.9A.E7.94.B3.E8.AF.B7-apns-.E8.AF.81.E4.B9.A6)。
 ![](https://qcloudimg.tencent-cloud.cn/raw/93f0715b20b258d0b9b6dcb3452fe7d3.png) 

<dx-alert infotype="notice" title="">
- 证书申请推荐同时可支持沙盒开发环境和生产环境。生产环境的证书实际是开发（Sandbox）+ 生产（Production）的合并证书，可以同时作为开发环境和生产环境的证书使用。
- 申请证书开发环境和生产环境可以使用同一个证书，但是 IM 控制台生成的证书 ID 一定是不相同的。请在代码中填写对应的 ID。
- 如果是开发环境和生产环境两个证书，在 IM 控制台请上传至对应的环境下。
</dx-alert>

### 步骤2：上传推送证书到 IM 控制台

1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)。
2. 单击目标应用卡片，进入应用的基础配置页面。
  ![](https://qcloudimg.tencent-cloud.cn/raw/0d9e979448bc73d89cef42bcfed1ef1b.jpeg)
3. 单击 **iOS 原生离线推送设置**右侧的**添加证书**。
4. 选择证书类型，上传 iOS 证书（p.12），设置证书密码，单击 **确认**。
![](https://qcloudimg.tencent-cloud.cn/raw/ec3e35778acc8b2e85022bc7c57f373b.jpeg)

> !
> 
> - 上传证书名请使用全英文（尤其不能使用括号等特殊字符）。
> - 上传证书需要设置密码，无密码收不到推送。
> - 发布 App Store 的证书需要设置为生产环境，否则无法收到推送。
> - 上传的 p12 证书必须是自己申请的真实有效的证书。

### 步骤3：在腾讯云控制台上传第三方推送证书后分配的证书 ID

当您 [上传证书到 IM 控制台](https://cloud.tencent.com/document/product/269/75429#.E6.AD.A5.E9.AA.A42.EF.BC.9A.E4.B8.8A.E4.BC.A0.E8.AF.81.E4.B9.A6.E5.88.B0.E6.8E.A7.E5.88.B6.E5.8F.B0) 后，IM 控制台会为您分配一个证书 ID，见下图。
![](https://qcloudimg.tencent-cloud.cn/raw/15802b097a0347f16a28c1a354ee3ea3.png)

## 集成 TUIOfflinePush 插件

### 步骤1：下载 TUIOfflinePush 插件并本地集成

登录 uni 原生插件市场，在 [ TUIOfflinePush 插件](https://ext.dcloud.net.cn/plugin?id=9149) 详情页面，下载插件或者使用 HBuilderX 导入插件。
 将插件下载到本地，放入项目 nativeplugins 中，在项目 manifest.json --> App 原生插件配置 --> 选择本地插件中勾选 TUIOfflinePush 插件。
 ![](https://qcloudimg.tencent-cloud.cn/raw/09d6b4f0e8d9cfe0d6dd98903f253371.png) 

> !**该插件仅支持本地集成，不支持云端集成方式。**

### 步骤2：项目配置
在项目 manifest.json > **App 模块配置**中勾选 Push 模块，不勾选 unipush。

![](https://qcloudimg.tencent-cloud.cn/raw/b9847502c3bb6623f09a942a7b5af417.jpeg)

### 步骤3：在项目中注册 TUIOfflinePush 插件

集成 IM sdk [2.22.0 版本](https://cloud.tencent.com/document/product/269/38492) 及以上版本，[注册插件 API](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#registerPlugin)。
 <dx-codeblock>
 ::: js
// v2.22.0 起支持 uni-app 打包 native app 时使用离线推送插件
// 请注意！应合规要求，在用户同意隐私协议的前提下，登录成功后 SDK 会通过推送插件获取推送 token，并将推送 token 传递至后台（若获取 token 失败则会导致离线推送无法正常使用
import TIM from 'tim-wx-sdk';

const tim = TIM.create({SDKAppID: xxx})
const TUIOfflinePush = uni.requireNativePlugin("TencentCloud-TUIOfflinePush");
tim.registerPlugin({
    'tim-offline-push-plugin': TUIOfflinePush,
    'offlinePushConfig': {
        // huawei
        'huaweiBusinessID': '', // 在腾讯云控制台上传第三方推送证书后分配的证书 ID
        // xiaomi
        'xiaomiBusinessID': '',// 在腾讯云控制台上传第三方推送证书后分配的证书 ID
        'xiaomiAppID': '',// 小米开放平台分配的应用 APPID
        'xiaomiAppKey': '',// 小米开放平台分配的应用 APPKEY
        // meizu
        'meizuBusinessID': '', // 在腾讯云控制台上传第三方推送证书后分配的证书 ID
        'meizuAppID': '',// 魅族开放平台分配的应用 APPID
        'meizuAppKey': '',// 魅族开放平台分配的应用 APPKEY
        // vivo
        'vivoBusinessID': '', // 在腾讯云控制台上传第三方推送证书后分配的证书 ID
        // oppo
        'oppoBusinessID': '', // 在腾讯云控制台上传第三方推送证书后分配的证书 ID
        'oppoAppKey': '',// oppo 开放平台分配的应用 APPID
        'oppoAppSecret': '',//
        // ios
        'iosBusinessID': '', // 在腾讯云控制台上传第三方推送证书后分配的证书 ID
    }
});
 :::
 </dx-codeblock>

> !
> 
> - 请将 sdk 升级到 [2.23.1 版本](https://cloud.tencent.com/document/product/269/38492), v2.22.0 起支持 uni-app 打包 native app 时使用离线推送插件。
> - vivo 推送需要在项目 manifest.json 本地插件处配置 vivo AppID、AppKey，如果不需要，可以填写为0，否则可能会编译错误。
> - 华为推送需要将官网下载的 agconnect-services.json 文件放到 nativeplugins/TencentCloud-TUIOfflinePush/android/assets/ 路径下。
> - 集成插件后，sdk 会在 im login 时自动上报 deviceToken，无需其他代码的配置。

### 步骤4：发送离线推送消息和透传内容

填写离线推送透传消息，在 [sendMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#sendMessage) 中填写 `offlinePushInfo` 字段相关信息。
![](https://qcloudimg.tencent-cloud.cn/raw/49beaf5e373c1bb5cf88f8cf503c512b.png)
 <dx-codeblock>
 ::: js
tim.sendMessage(message, {
    // 如果接收方不在线，则消息将存入漫游，且进行离线推送（在接收方 App 退后台或者进程被 kill 的情况下）。接入侧可自定义离线推送的标题及内容
    offlinePushInfo: {
        title: '', // 离线推送标题
        description: '', // 离线推送内容
        androidOPPOChannelID: '',// 离线推送设置 OPPO 手机 8.0 系统及以上的渠道 ID
        extension: JSON.stringify({
            entity: { // entity 中的内容可自定义
                nick: '哈哈哈',
                userID: 'user1',
            }
        })
    }
})
:::
</dx-codeblock>

### 步骤5：获取点击透传的内容

在 `App.vue` 文件中获取透传内容，配置指定跳转页面。
<dx-codeblock>
::: js
// 在 App.vue, 生命钩子 onLaunch 中监听
TUIOfflinePush.setOfflinePushListener((data) => {
    // 透传 entity 中的内容，不包含推送的 Message
    console.log('setOfflinePushListener', data);
    const {nick, userID} = data.notification.entity;
    // 跳转到应用内指定界面
    uni.navigateTo({
        url: "/pages/xxx/xxx",
    });
});
:::
</dx-codeblock>
<dx-alert infotype="notice" title="">
- 可在此回调中获取推送时配置的透传内容
- 可在此回调函数中配置应用跳转界面
- 各端互通时，要确保  `extension` 保持一致， `extension` 中需要包含  `entity` 字段
</dx-alert>

### 步骤6：使用自定义基座打包 uni 原生插件 （请使用真机运行自定义基座）

该插件只支持本地集成，原生插件调试一个自定义基座，把需要先将原生插件打到真机运行基座里，然后在本地写代码调用调试。

>?自定义基座不是正式版，真正发布时，需要再打正式包。使用自定义基座是无法正常升级替换 APK 的。

## 常见问题

### 收不到离线推送怎么排查？

#### 1、OPPO 手机收不到推送的可能情况

OPPO 安装应用通知栏显示默认关闭，需要确认下开关状态。

#### 2、设备通知栏设置影响

离线推送的直观表现就是通知栏提示，所以同其他通知一样受设备通知相关设置的影响，以华为为例：

- “手机设置-通知-锁屏通知-隐藏或者不显示通知”，会影响锁屏状态下离线推送通知显示。
- “手机设置-通知-更多通知设置-状态栏显示通知图标”，会影响状态栏下离线推送通知的图标显示。
- “手机设置-通知-应用的通知管理-允许通知”，打开关闭会直接影响离线推送通知显示。
- “手机设置-通知-应用的通知管理-通知铃声” 和 “手机设置-通知-应用的通知管理-静默通知”，会影响离线推送通知铃音的效果。

#### 3、按照流程接入完成，还是收不到离线推送

- 首先在 IM 控制台通过 [离线测试工具](https://console.cloud.tencent.com/im-detail/tool-push-check) 自测下是否可以正常推送。
  推送异常情况，设备状态异常，需要检查下 IM 控制台配置各项参数是否正确，再者需要检查下代码初始化注册逻辑，包括厂商推送服务注册和 IM 设置离线推送配置相关逻辑是否正确设置。
  推送异常情况，设备状态正常，需要看下是否需要正确填写 channel ID 或者后台服务是否正常。
- 离线推送依赖厂商能力，一些简单的字符可能会被厂商过滤不能透传推送。
- 如果离线推送消息出现推送不及时或者偶尔收不到情况，需要看下厂商的推送限制。

#### 4、iOS 普通消息为什么收不到离线推送

- 首先，请检查下 App 的运行环境和证书的环境是否一致，如果不一致，收不到离线推送。
- 其次，检查下 App 和证书的环境是否为生产环境。如果是开发环境，向苹果申请 deviceToken 可能会失败，生产环境暂时没有发现这个问题，请切换到生产环境测试。

#### 5、iOS 开发环境下，注册偶现不返回 deviceToken 或提示 APNs 请求 token 失败？

此问题现象是由于 APNs 服务不稳定导致的，可尝试通过以下方式解决：

1. 给手机插入 SIM 卡后使用4G网络测试。
2. 卸载重装、重启 App、关机重启后测试。
3. 打生产环境的包测试。
4. 更换其它 iOS 系统的手机测试。

#### 6、iOS 没有 token的原因

1. 模拟器，是不产生 token 的
2. 真机，需要在手机上开启推送的权限
3. 真机，需要添加 push notification 的 enetitemenet

### 厂商推送限制

1. 国内厂商都有消息分类机制，不同类型也会有不同的推送策略。如果想要推送及时可靠，需要按照厂商规则设置自己应用的推送类型为高优先级的系统消息类型或者重要消息类型。反之，离线推送消息会受厂商推送消息分类影响，与预期会有差异。
2. 另外，一些厂商对于应用每天的推送数量也是有限制的，可以在厂商控制台查看应用每日限制的推送数量。
如果离线推送消息出现推送不及时或者偶尔收不到情况，需要考虑下这里：
 - 华为：将推送消息分为服务与通讯类和资讯营销类，推送效果和策略不同。另外，消息分类还和自分类权益有关：
    - 无自分类权益，推送消息厂商还会进行二次智能分类 。
    - 有申请自分类权益，消息分类会按照自定义的分类进行推送。
    具体请参见 [厂商描述](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835)。
 - vivo：将推送消息分为系统消息类和运营消息类，推送效果和策略不同。系统消息类型还会进行厂商的智能分类二次修正，若智能分类识别出不是系统消息，会自动修正为运营消息，如果误判可邮件申请反馈。另外，消息推送也受日推总数量限制，日推送量由应用在厂商订阅数统计决定。
  具体请参见 [厂商描述1](https://dev.vivo.com.cn/documentCenter/doc/359) 或 [厂商描述2](https://dev.vivo.com.cn/documentCenter/doc/156)。
 - OPPO：将推送消息分为私信消息类和公信消息类，推送效果和策略不同。其中私信消息是针对用户有一定关注度，且希望能及时接收的信息，私信通道权益需要邮件申请。公信通道推送数量有限制。
  具体请参见 [厂商描述1](https://open.oppomobile.com/wiki/doc#id=11227) 或 [厂商描述2](https://open.oppomobile.com/wiki/doc#id=11210)。
 - 小米：将推送消息分为重要消息类和普通消息类，推送效果和策略不同。其中重要消息类型仅允许即时通讯消息、个人关注动态提醒、个人事项提醒、个人订单状态变化、个人财务提醒、个人状态变化、个人资源变化、个人设备提醒这8类消息推送，可以在厂商控制台申请开通。普通消息类型推送数量有限制。
  具体请参见 [厂商描述1](https://dev.mi.com/console/doc/detail?pId=2422) 或 [厂商描述2](https://dev.mi.com/console/doc/detail?pId=2086)。
 - 魅族：推送消息数量有限制。
  具体请参见 [厂商描述](http://open.res.flyme.cn/fileserver/upload/file/202201/85079f02ac0841da859c1da0ef351970.pdf)。
 - FCM：推送上行消息频率有限制。
  具体请参见 [厂商描述](https://firebase.google.com/docs/cloud-messaging/concept-options?hl=zh-cn#upstream_throttling)。

## 交流与反馈

欢迎加入 QQ 群进行技术交流和反馈问题。 309869925 (技术交流群)
