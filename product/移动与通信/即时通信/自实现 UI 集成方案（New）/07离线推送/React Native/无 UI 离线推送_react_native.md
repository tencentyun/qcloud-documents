## 概述

即时通信 IM 的终端用户需要随时都能够得知最新的消息，而由于移动端设备的性能与电量有限，当 App 处于后台时，为了避免维持长连接而导致的过多资源消耗，即时通信 IM 推荐您使用各厂商提供的系统级推送通道来进行消息通知，系统级的推送通道相比第三方推送拥有更稳定的系统级长连接，可以做到随时接受推送消息，且资源消耗大幅降低。

> !
>
> - 在没有主动退出登录的情况下，应用退后台、手机锁屏、或者应用进程被用户主动杀掉三种场景下，如果想继续接收到 IM 消息提醒，可以接入即时通信 IM 离线推送。
> - 如果应用主动调用 logout 退出登录，或者多端登录被踢下线，即使接入了 IM 离线推送，也收不到离线推送消息。

## 集成 react-native-tim-push 跑通离线推送功能

集成 `react-native-tim-push` 之前，请您先 [注册应用到厂商推送平台](https://cloud.tencent.com/document/product/269/75430#.E6.8E.A5.E5.85.A5.E5.87.86.E5.A4.87.EF.BC.88.E6.B3.A8.E5.86.8C.E5.8E.82.E5.95.86.EF.BC.89.3Ca-id.3D.22firstone.22.3E.3C.2Fa.3E)，登录腾讯云账号进行 [IM 控制台配置](https://console.cloud.tencent.com/avc) 和 [配置离线推送跳转界面](https://cloud.tencent.com/document/product/269/75428#.E6.AD.A5.E9.AA.A43.EF.BC.9A.E9.85.8D.E7.BD.AE.E7.A6.BB.E7.BA.BF.E6.8E.A8.E9.80.81.E8.B7.B3.E8.BD.AC.E7.95.8C.E9.9D.A2)。之后按照如下步骤操作即可快速接入 IM 离线推送。

> !
>
> - 请在[登录](https://cloud.tencent.com/document/product/269/77538)后初始化插件。
> - 组件支持的厂商有：小米、华为、OPPO、vivo、魅族和 Google FCM。
> - 苹果请参考官方插件：[react-native-push-notification](https://github.com/react-native-push-notification/ios)。

### 步骤1：安装依赖

```
// using npm
npm i react-native-tim-push --save

// using yarn
yarn add react-native-tim-push
```

- **vivo 适配**
根据 vivo 厂商接入指引，需要将 APPID 和 APPKEY 添加到清单文件中，否则会出现编译问题：
<dx-tabs>
::: 方法 1
```
android {
    ...
    defaultConfig {
		    ...
        manifestPlaceholders = [
                "VIVO_APPKEY" : "您应用分配的证书 APPKEY",
                "VIVO_APPID" : "您应用分配的证书 APPID"
        ]
    }
}
```
:::
::: 方法2

```
<receiver android:name="com.tencent.qcloud.tim.demo.thirdpush.VIVOPushMessageReceiverImpl">
    <intent-filter>
        <!-- 接收push消息 -->
        <action android:name="com.vivo.pushclient.action.RECEIVE" />
    </intent-filter>
</receiver>

<meta-data tools:replace="android:value"
    android:name="com.vivo.push.api_key"
    android:value="您应用分配的证书 APPKEY" />
<meta-data tools:replace="android:value"
    android:name="com.vivo.push.app_id"
    android:value="您应用分配的证书 APPID" />

```
:::
</dx-tabs>

-  **华为和 Google FCM 适配**
华为和 Google FCM 需要按照厂商方法，集成对应的 plugin 和 json 配置文件。

 1. 下载配置文件添加到工程根目录。
 <dx-tabs>
::: 华为
<table>
<tr>
<img src="https://qcloudimg.tencent-cloud.cn/raw/220264120cdadd154c581e8164c21515.png" style="zoom:60%;" />
</tr>
</table>
:::
::: Google FCM
<table>
<tr>
<img src="https://qcloudimg.tencent-cloud.cn/raw/1bfbfc52fb60440c192d7bddd372f99d.png" style="zoom:60%;" />
</tr>
</table>
:::
</dx-tabs>

 2. 在项目级 build.gradle 文件中 buildscript -> dependencies 下添加以下配置：
```
repositories {
...
// 配置 HMS Core SDK 的 Maven 仓地址。
maven {url 'https://developer.huawei.com/repo/'}
}

dependencies {
...
classpath 'com.google.gms:google-services:4.2.0'
classpath 'com.huawei.agconnect:agcp:1.4.1.300'
}
```

 3. 在应用级 build.gradle 文件中添加下方配置。
```

apply plugin: 'com.google.gms.google-services'
apply plugin: 'com.huawei.agconnect'
```

### 步骤2：推送参数配置
推送证书添加成功之后，IM 控制台会为您分配一个证书 ID，请您在初始化插件时传入，该证书 ID 会在注册推送服务和上报 token 时使用, 以小米为例：

**推送证书 ID 如下：**
![](https://qcloudimg.tencent-cloud.cn/raw/772536e8a3f474572f5b85bfb2597fe1.png)

**填充的参数如下：**

```javascript
import { TimPushPlugin } from 'react-native-tim-push';
import { LogLevelEnum, TencentImSDKPlugin } from 'react-native-tim-js';

const cPush = new TimPushPlugin();

const login = () => {
    const userID = ""; // userID
    const userSig = ""; // userSig
    const res = await TencentImSDKPlugin.v2TIMManager.login(userID, userSig);
    // 判断是否登录成功
    if (res.code === 0) {
        // 初始化离线推送插件
        initPushPlugin();
    }

}

const initPushPlugin = () => {
    cPush.init({
        mi_buz_id: 5218, // 在腾讯云控制台分配的证书ID
        mi_push_app_id: '', //小米开放平台分配的应用APPID
        mi_push_app_key: '', //小米开放平台分配的应用APPKEY
    });
}
```

以上步骤完成后，就可以收到离线推送通知了。

### 步骤3：发消息时设置离线推送参数

发送消息时，请您设置离线推送参数，具体请参见 [发消息时设置离线推送参数](https://comm.qq.com/im/doc/RN/zh/Api/V2TIMMessageManager/sendMessage.html)。

```javascript
import { TencentImSDKPlugin } from 'react-native-tim-js';

// 创建文本消息
const createTextMessage = await TencentImSDKPlugin.v2TIMManager.getMessageManager().createTextMessage("test");
 if(createTextMessage.code == 0){
    String id =  createTextMessage.data.id;

   	// 发送文本消息
   const sendMessageRes = await TencentImSDKPlugin.v2TIMManager.getMessageManager().sendMessage(id: id, receiver: "userID", groupID: "", offlinePushInfo: {
        title = '', // 推送通知标题。留空字符串时，按照优先级，IM后台自动替换成 sender的昵称 => sender ID。因此，如无特殊需求，该字段议留空，可达到和微信一致的效果
        desc = '', // 推送第二行小字部分
        disablePush = false,
        ext = '', // 推送内额外信息，对方可于单击通知跳转时拿到。建议传含Conversation信息的JSON，用于收件方跳转至对应Chat。可参见下方TUIKit的实例代码。
        androidOPPOChannelID = '', // OPPO的channel ID
   });
    if(sendMessageRes.code == 0){
      // 发送成功
    }
  }
```

## 交流与反馈

如果您在接入使用过程中有任何疑问，请扫码加入微信群，或加入QQ群：437955475 咨询。

![](https://qcloudimg.tencent-cloud.cn/raw/095e39d0943d3670585659251c5a3b6d.png)

## 常见问题

### 收不到离线推送怎么排查？

#### 1、OPPO 手机

OPPO 手机收不到推送一般有以下几种情况：

- 按照 OPPO 推送官网要求，在 Android 8.0 及以上系统版本的 OPPO 手机上必须配置 ChannelID，否则推送消息无法展示。配置方法可以参见 [setAndroidOPPOChannelID](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html#a32d340e95395bb64cc3e8f62321aafe1)。
- OPPO 安装应用通知栏显示默认关闭，需要确认下开关状态。

#### 2、发送消息为自定义消息

自定义消息的离线推送和普通消息不太一样，自定义消息的内容我们无法解析，不能确定推送的内容，所以默认不推送，如果您有推送需求，需要您在 [sendMessage](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a318c40c8547cb9e8a0de7b0e871fdbfe) 的时候设置 [offlinePushInfo](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html) 的 [desc](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html#a78c8e202aa4e0859468ce40bde6fd602) 字段，推送的时候会默认展示 desc 信息。

#### 3、设备通知栏设置影响

离线推送的直观表现就是通知栏提示，所以同其他通知一样受设备通知相关设置的影响，以华为为例：

- “手机设置-通知-锁屏通知-隐藏或者不显示通知”，会影响锁屏状态下离线推送通知显示。
- “手机设置-通知-更多通知设置-状态栏显示通知图标”，会影响状态栏下离线推送通知的图标显示。
- “手机设置-通知-应用的通知管理-允许通知”，打开关闭会直接影响离线推送通知显示。
- “手机设置-通知-应用的通知管理-通知铃声” 和 “手机设置-通知-应用的通知管理-静默通知”，会影响离线推送通知铃音的效果。

#### 4、按照流程接入完成，还是收不到离线推送

- 首先在 IM 控制台通过 [离线测试工具](https://console.cloud.tencent.com/im/tool-push-check) 自测下是否可以正常推送。
  推送异常情况，设备状态异常，需要检查下 IM 控制台配置各项参数是否正确，再者需要检查下代码初始化注册逻辑，包括厂商推送服务注册和 IM 设置离线推送配置相关逻辑是否正确设置。
  推送异常情况，设备状态正常，需要看下是否需要正确填写 channel ID 或者后台服务是否正常。
- 离线推送依赖厂商能力，一些简单的字符可能会被厂商过滤不能透传推送。
- 如果离线推送消息出现推送不及时或者偶尔收不到情况，需要看下厂商的推送限制。

### 厂商推送限制

1. 国内厂商都有消息分类机制，不同类型也会有不同的推送策略。如果想要推送及时可靠，需要按照厂商规则设置自己应用的推送类型为高优先级的系统消息类型或者重要消息类型。反之，离线推送消息会受厂商推送消息分类影响，与预期会有差异。
2. 另外，一些厂商对于应用每天的推送数量也是有限制的，可以在厂商控制台查看应用每日限制的推送数量。
如果离线推送消息出现推送不及时或者偶尔收不到情况，需要考虑下这里：
 - 华为：将推送消息分为服务与通讯类和资讯营销类，推送效果和策略不同。另外，消息分类还和自分类权益有关：
    - 无自分类权益，推送消息厂商还会进行二次智能分类 。
    - 有申请自分类权益，消息分类会按照自定义的分类进行推送。
    具体请参见 [厂商描述](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835)。
 - vivo：将推送消息分为系统消息类和运营消息类，推送效果和策略不同。系统消息类型还会进行厂商的智能分类二次修正，若智能分类识别出不是系统消息，会自动修正为运营消息，如果误判可邮件申请反馈。另外，消息推送也受日推总数量限制，日推送量由应用在厂商订阅数统计决定。
  具体请参见 [厂商描述 1](https://dev.vivo.com.cn/documentCenter/doc/359) 或 [厂商描述 2](https://dev.vivo.com.cn/documentCenter/doc/156)。
 - OPPO：将推送消息分为私信消息类和公信消息类，推送效果和策略不同。其中私信消息是针对用户有一定关注度，且希望能及时接收的信息，私信通道权益需要邮件申请。公信通道推送数量有限制。
  具体请参见 [厂商描述 1](https://open.oppomobile.com/wiki/doc#id=11227) 或 [厂商描述 2](https://open.oppomobile.com/wiki/doc#id=11210)。
 - 小米：将推送消息分为重要消息类和普通消息类，推送效果和策略不同。其中重要消息类型仅允许即时通讯消息、个人关注动态提醒、个人事项提醒、个人订单状态变化、个人财务提醒、个人状态变化、个人资源变化、个人设备提醒这 8 类消息推送，可以在厂商控制台申请开通。普通消息类型推送数量有限制。
  具体请参见 [厂商描述 1](https://dev.mi.com/console/doc/detail?pId=2422) 或 [厂商描述 2](https://dev.mi.com/console/doc/detail?pId=2086)。
 - 魅族：推送消息数量有限制。
  具体请参见 [厂商描述](http://open.res.flyme.cn/fileserver/upload/file/202201/85079f02ac0841da859c1da0ef351970.pdf)。
 - FCM：推送上行消息频率有限制。
  具体请参见 [厂商描述](https://firebase.google.com/docs/cloud-messaging/concept-options?hl=zh-cn#upstream_throttling)。

