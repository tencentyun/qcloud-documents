## 简介
该指引是从 [小微硬件开放平台](https://xiaowei.qcloud.com/hardware.html) 申请到 pid 后到设备能正常进行语音识别请求的接入指引。

#### 方案简介

为了提供更好的智能化设备体验，我们打造了集成腾讯云小微 AI 能力的语音方案。该方案的能力大致分为以下几个部分：

*   ** 唤醒模块 **
*   ** 静音检测 **
*   ** 语音识别 **
*   ** 语义分析 **
*   **Skill 服务 **

为了简化设备对接难度，提升方案的集成度、安全性和灵活性，我们使用设备 SDK 植入的方式进行对接。 同时，大部分整合在云端，设备端 SDK 通过简单有效的接口，提供外部服务：

[![img_main](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/Xiaowei_Device_AIAudio_Request.png)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/Xiaowei_Device_AIAudio_Request.png)

设备开启后，将持续录音检测唤醒词，用户通过唤醒词等途径唤醒设备后，将录制的声音传到云端进行语音识别和静音检测，检测到静音后，进行语义分析，最后从 Skill 后台得到结果并返回给客户端进行播放。

#### 能力说明

| 能力类型   |           |
|:-----------|:---------:|
| 唤醒检测   | 本地 + 云端 |
| 静音检测   |   云端    |
| 语音识别   |   云端    |
| 语义分析   |   云端    |
| 内置 Skills |   云端    |
| 播放控制   |   本地    |

## 接入流程
接入大致分为以下几个步骤：

*   从 [小微硬件开放平台](https://xiaowei.qcloud.com/hardware.html) 申请接入。
*   下载小微设备端 SDK，我们在官网提供了最新的 [Android](https://cloud.tencent.com/document/product/645/14215) 和[Linux](https://cloud.tencent.com/document/product/645/14216)版本的 SDK。
*   参考文档和 demo 实现功能并进行测试。
*   提供体验设备，完成产品体验。

## 接入腾讯云小微硬件开放平台

### 简介概述

腾讯云小微硬件开放平台是一个能将语音交互能力输出给第三方硬件厂商的平台，无论是音箱、电视、玩具、OTT 盒子、投影仪还是汽车，只需要一个 SDK 即可完成接入，为设备赋予人工智能语音能力。

硬件开放平台接入目前支持 Android 和 linux 两大平台接入。

腾讯云小微硬件开放平台将语音唤醒、语音识别、语义分析、信令收发以及众多的内置资源及服务，如音乐、天气、导航等核心能力提供给智能音箱、智能电视、智能玩具、OTT 盒子等传统硬件领域的合作伙伴，实现用户与设备、设备与服务之间的语音联动能力。

我们致力于帮助传统硬件快速转型为具有语音控制能力的智能硬件，帮助合作伙伴降低云端、APP 端等研发成本，提升用户粘性并通过开放腾讯的丰富资源以及服务来给予硬件更多想象空间。

### 硬件开放平台框架

[![硬件开放平台框架](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img / 硬件开放平台框架. png)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img / 硬件开放平台框架. png)

### 硬件设备能力概述（有屏 & 无屏设备）

目前接入硬件开放平台的设备分为有屏和无屏两大类设备，有屏设备相较于无屏设备多了在显示屏上可触摸交互的一部分操作，这部分内容可以详见有屏设备交互规范，在这里不多作赘述。

现在，我们来看一下接入之后的硬件设备所获得的能力：

硬件厂商完成 sdk 接入之后，传统硬件便获得了语音交互的能力，整个产品的使用流程包含以下 5 个步骤，先来看一张概览图：

[![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img / 能力. png)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img / 能力. png)

1：用户可通过语音唤醒音箱（或其他硬件设备，此处以音箱为例），并说出具体的指令；

在这里指令的内容指的是腾讯云小微 skill 的能力（具体 skill 的能力和配置可见 skill 部分 wiki，在这里不多作赘述），包含内置 skill 和第三方 skill 两大块，提供丰富的资源和服务能力，下图是重点能力的概览。

[![腾讯云小微 skill 能力](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img / 腾讯云小微 skill 能力. png)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img / 腾讯云小微 skill 能力. png)

2：音箱将语音内容传送到云端；

基于腾讯云为设备提供快速、安全、稳定的云端环境，让硬件设备开发者更加聚焦在硬件设计与功能创新本身。

3：云端对用户的语音进行识别与分析；

我们具有行业领先的语音语义能力，丰富的数据基础，每天数亿的全自然语音调用量训练，语音识别的准确率高达 97%，从发起语音到内容播出小于 1 秒。

4：分析完成，将内容传输回音箱；

5：音箱播放最终结果给用户。

### 硬件开放平台申请接入流程

开发者申请接入腾讯云小微硬件开放平台需要在 [官网](https://xiaowei.qcloud.com/hardware.html) 递交申请资料，进入腾讯云小微官网 -- 硬件开放开放 -- 点击【申请内测】：

[![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img / 申请内测. jpg)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img / 申请内测. jpg)

点击申请之后需要完善开发者的相关信息:

1. 基本信息：请确保信息准确无误，以免耽误后续审核的过程中的联系失败；

2. 公司信息：请上传公司的营业执照进行资质认证，并确保提交的公司规模信息准确；

3. 技术参数：请根据需求选择符合自己硬件设备的技术参数，如有疑问可参见技术 wiki。

[![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img / 资料填写. jpg)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img / 资料填写. jpg)

以上信息确认填写无误之后，选择提交，会获得您的申请接入单号，腾讯云小微团队会尽快通过邮件反馈审核结果给开发者注册的邮箱地址，开发者也可以在申请页面查看审核进度及反馈。

[![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img / 申请记录. png)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img / 申请记录. png)

当申请通过之后，再次进入官网硬件开放平台，会看到【申请内测】的 button 变成了【开始接入】，此时点击【开始接入】即可进入配置平台进行具体的硬件开发配置。

[![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img / 开始接入. jpg)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img / 开始接入. jpg)

## 配置平台使用说明

### 添加新设备

进入配置平台之后，点击添加设备按钮，填写【设备名称】及选择【设备类型】后即可开始快速注册一个新设备；

设备名称：您可以自由填写，设备名称请尽量用中文并控制长度。

设备类型：必须填写准确，后期无法进行修改，这里我们选择设备类型为音箱。

[![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img / 配置平台 - 添加设备. png)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img / 配置平台 - 添加设备. png)

完成后，我们已经获得了该产品获得重要信息：pid 和 server key，这两个信息非常重要，会在 SDK 登录的时候中用到。

在设备导航栏中，选择进入相应的设备，即可在头部看到这两个信息，请看下图：

[![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img / 配置平台 - pid.jpg)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img / 配置平台 - pid.jpg)

### 填写设备信息

当您完成一个新设备的创建之后，需要继续补充完善设备的信息，这里包含【基础信息】和【设备信息】两部分。

[![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img / 配置平台 - 基本信息. png)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img / 配置平台 - 基本信息. png)

进入到刚刚创建的设备 - 设备信息 tab，补充完整设备的【基本信息】：

设备型号：您可以自由填写，设备名称请尽量用中文并控制长度；

设备图标：请上传 jpg、png 格式的图片，大小为 512*512；

设备描述：请尽量简明扼要的描述您设备的主要功能及特点。

然后需要补充【设备信息】：

操作系统：这里我们支持 androd 和 linux 两大操作系统；

是否带屏幕：请根据您的设备实际情况进行选择；

公钥上传 稍微复杂一点，因为您需要下载一个我们的工具来完成这个步骤，点击 网页上的 “公钥 & 证书工具下载（Win 7 Only）” 链接，然后运行密钥生成工具，点击下图中的生成 KEY 按钮，会在您指定的目录下生成一对非对称密钥文件： ec_key.pem 和 public.pem。之后点击上传按钮上传 public.pem 就可以了。

[![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img / 配置平台 - 公钥. png)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img / 配置平台 - 公钥. png)

### 为设备配置 skill

每一个接入腾讯云小微的硬件都有使用我们强大资源和服务的权限，此处需要使用同一个账号在我们腾讯云小微 skill 平台进行创建，创建完成之后就会显示在这里，开发者可以自行选择该硬件需要使用的 skill。

[![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img / 配置平台 - skill.png)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img / 配置平台 - skill.png)

### OTA 能力管理
OTA 能力配置中分为【正式环境】和【测试环境】两个部分，开发者每上传一个 OTA 包的时候需要先填写相关的版本信息；

在测试环境中允许向指定的设备推送升级，需要上传对应的 sn 包，限制为 100 个。

[![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img / 配置平台 - OTA.png)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img / 配置平台 - OTA.png)

### 样机审核

当产品所有功能均开发完毕后需要将样机寄送至腾讯云小微团队进行测试审核，只有审核通过之后产品才可以正式认证上线。

## 实现指引

下面说明中的部分名词 可以参考 [基本名词解释](https://cloud.tencent.com/document/product/645/14217)。

#### 第一行代码——SDK 登录

下载好 SDK 后，可以创建项目开始写代码了（您可以参考 CommonApplication 中的示例代码）：

```
// 首先设置内部广播的接收权限，可以避免被其余程序接收到内部发出的广播
TXDeviceSDK.setBroadcastPermissionDeviceSdkEvent(“Your_Permission”);

// 设置登录和上线离线事件的全局回调
TXDeviceBaseManager.setOnDeviceSDKEventListener(new TXDeviceBaseManager.OnDeviceLoginEventListener() {
    @Override
    public void onLoginComplete(int error) {
        if (error == 0) {
            showToastMessage("登录成功");
        } else {
            showToastMessage("登录失败");
        }
    }

    @Override
    public void onOnlineSuccess() {
        showToastMessage("上线成功");
    }

    @Override
    public void onOfflineSuccess() {
        showToastMessage("离线");
    }

    @Override
    public void onUploadRegInfo(int error) {
    }

});

// 构造登录信息
TXLoginInfo login = new TXLoginInfo();
login.deviceName = getString(R.string.app_name);
login.license = CommonApplication.licence;
login.serialNumber = CommonApplication.sn;
login.srvPubKey = CommonApplication.srvPubKey;
login.productId = CommonApplication.pid;
login.productVersion = UIUtils.getVersionCode(this);// build.gradle 中的 versionCode，用来检测更新
login.networkType = TXLoginInfo.TYPE_NETWORK_WIFI;
login.runMode = TXLoginInfo.SDK_RUN_MODE_DEFAULT;
login.sysPath = getCacheDir().getAbsolutePath();
login.sysCapacity = 1024000l;
login.appPath = getCacheDir().getAbsolutePath();
login.appCapacity = 1024000l;
login.tmpPath = Environment.getExternalStoragePublicDirectory("tencent") + "/device/file/";
login.tmpCapacity = 1024000l;

// 对设备进行登录
TXDeviceCoreService.init(getApplicationContext(), login, 0);
```

登录是 SDK 运行的第一步，所有操作都需要在登录成功后才能进行。

#### 初始化语音识别 SDK
```
TXAIAudioSDK.getInstance().init(this);
```

#### 监听绑定者列表变化

SDK 运行后，需要使用腾讯云小微 App 对其进行绑定，才可以正常使用所有内置 Skill，所以在登录后，应该对绑定者进行判断，如果没有绑定者，应该提示用户扫描二维码进行绑定。（sn 和 license 等信息是出厂的时候就决定好的，绑定二维码为固定格式，格式为 “[https://xiaowei.tencent.com/device/bind?pid=2100000000&sn=1234567890123456&token=31082E2E16B535A1D8BD73EA877199B6”，其中 token 为 licence 的 md5 值，需要大写。）](https://xiaowei.tencent.com/device/bind?pid=2100000000&sn=1234567890123456&token=31082E2E16B535A1D8BD73EA877199B6”，其中 token 为 licence 的 md5 值，需要大写。）)

```
TXDeviceBaseManager.setOnBinderEventListener(new TXDeviceBaseManager.OnBinderEventListener() {
    @Override
    public void onBindCallback(long tinyId, int error) {
    }

    @Override
    public void onBinderListChange(int error, ArrayList<TXBinderInfo> arrayList) {
        if (error == 0) {
            // 如果 arrayList 长度为 0，说明没绑定者，或者解绑了，需要提示用户进行绑定
            TXAIAudioSDK.getInstance().requestTTS("请先使用腾讯云小微 App 扫描二维码进行绑定");
        }
    }
});
```

#### 开启唤醒模块

唤醒模块的介绍参照 [唤醒模块说明](https://cloud.tencent.com/document/product/645/14218);

#### 语音请求

语音请求相关的接口和回调都定义在 TXAIAudioSDK 中。 和语音请求相关的接口有以下几个：

| 方法名                                    | 说明                                                                                      |
|:------------------------------------------|:------------------------------------------------------------------------------------------|
| onWakeup                                  | 设备已经唤醒，通知 SDK 开启一轮语音识别                                                     |
| onSleep                                   | 设备已经休眠，通知 SDK 取消正在请求的语音识别                                               |
| feedRecordData                            | 填充 pcm 数据进行识别                                                                       |
| feedRecordDataEnd                         | 填充数据结束，仅当不使用静音检测时才需要调用，用于告诉 sdk 已经说话完毕，适用于按住说话场景 |
| DeviceControlListener$onRecordModeChanged | 设备录音模式变化了（唤醒、识别、通话）                                                    |
| DeviceControlListener$onWakeup            | 设备唤醒了                                                                                |
| DeviceControlListener$onState             | 设备的状态变化了，比如正在请求，收到了结果等                                              |
| DeviceControlListener$onVolumeChange      | 设备的音量需要调节                                                                        |
| DeviceControlListener$onVolumeSilence     | 设备的音量需要静音                                                                        |
| DeviceControlListener$onVolumeUnSilence   | 设备的音量需要取消静音                                                                    |
| DeviceControlListener$onControl           | 其余控制，例如获取可见可达词库、获取当前位置                                              |
| RecognizeEventListener$onRecognizeBegin   | 开始识别了                                                                                |
| RecognizeEventListener$onRecognize        | 识别中间过程的文本                                                                        |
| RecognizeEventListener$onRecognizeEnd     | 识别结束了                                                                                |

在初始化后，应该设置 DeviceControlListener：（您可以参照 MainService.java）

```
TXAIAudioSDK.getInstance().setDeviceControlListener(new TXAIAudioSDK.DeviceControlListener() {

    @Override
    public void onRecordModeChanged(int old, int mode) {
        if ((mode & TXAIAudioSDK.STATE_WAKEUP) == TXAIAudioSDK.STATE_WAKEUP) {
            // 需要语音检测唤醒
        }
        if ((mode & TXAIAudioSDK.STATE_RECOGNIZE) == TXAIAudioSDK.STATE_RECOGNIZE) {
            // 需要语音识别
        }
        if ((mode & TXAIAudioSDK.STATE_CALL) == TXAIAudioSDK.STATE_CALL) {
            // 需要语音电话
        }
    }

    /**
     * 唤醒了，此时还不知道是不是连续说话，但是已经检测到唤醒词，这里只包含云端校验结果，不包含多轮对话的自动唤醒
     */
    @Override
    public void onWakeup() {
    }

    /**
     * 唤醒了
     *
     * @param wakeup 唤醒词
     * @param flag   0 按键 1 唤醒失败 2 唤醒成功 3 指令词唤醒（目前仅车机支持） 4 唤醒后连续说话模式
     * @param voiceId 云端校验相关的 voiceId
     */
    @Override
    public void onWakeupEvent(String localWakeup, String wakeup, int flag, String voiceId) {
        if (flag == 0) {
                // 按键唤醒
        } else if (flag == 1) {
            // 云端校验不通过
        } else if (flag == 2) {
            // 唤醒了
        } else if (flag == 3) {
            // 收到结果了
        } else if (flag == 4) {
            // 唤醒了并且连续在说话
        }
    }

    @Override
    public void onState(int event, TXAIAudioEventInfo data) {
    }

    @Override
    public void onVolumeChange(boolean isIncrement, int value) {// isIncrement value is -100->100 , !isIncrement value is 0-100
    }

    @Override
    public void onVolumeSilence() {
    }

    @Override
    public void onVolumeUnSilence() {
    }

    @Override
    public void onControl(int ctlcode, int value) {
    }
});
```

onState 中会返回以下几种状态，在不同的状态可以进行不同的灯光等展示：（定义在 TXAIAudioDef.StateEventDef 中）

| 值 | 定义                                   | 说明                                                       |
|:---|:---------------------------------------|:-----------------------------------------------------------|
| 0  | AI_AUDIO_STATE_IDLE                    | 空闲，在一次请求回来结果并且播放完毕后会回调               |
| 1  | AI_AUDIO_STATE_REQUEST_START           | 语音请求开始（开始唤醒动画，唤醒动画显示事件需要自行去重） |
| 2  | AI_AUDIO_STATE_REQUEST_WAIT            | 等待语音请求响应                                           |
| 3  | AI_AUDIO_STATE_RESPONSE                | 收到语音请求响应，在这时候，UI 的结构化显示数据也会带下来   |
| 4  | AI_AUDIO_STATE_PLAYING                 | 开始播放某个 playId 的资源                                   |
| 5  | AI_AUDIO_STATE_CHANGED                 | 消息盒子中数据变化                                         |
| 7  | AI_AUDIO_STATE_REQUEST_FINISH          | 请求结束或者被取消（结束唤醒动画）                         |
| 8  | AI_AUDIO_STATE_CALL_BEGIN              | 开始电话                                                   |
| 9  | AI_AUDIO_STATE_CALL_RECORDING          | 开始电话并且双方接通了，电话需要声音了                     |
| 10 | AI_AUDIO_STATE_CALL_END                | 结束电话                                                   |
| 11 | AI_AUDIO_STATE_MSG_PLAY_START          | 开始一条消息播放                                           |
| 12 | AI_AUDIO_STATE_MSG_PLAY_STOP           | 结束一条消息播放                                           |
| 13 | AI_AUDIO_STATE_FETCH_DEVICE_BASIC_INFO | 用户询问设备的基础信息                                     |
| 20 | AI_AUDIO_STATE_MSGPROXY_STAT           | 消息代收状态更新的通知                                     |
| 21 | AI_AUDIO_STATE_MSG_SEND                | 发送消息的状态通知                                         |

对于有屏设备，需要关注 AI_AUDIO_STATE_RESPONSE 带下来的结构化数据，进行 UI 展示，具体参照 [UI 模板实现指引](https://cloud.tencent.com/document/product/645/14224)。

当用户对设备进行唤醒后，应该开始进行语音请求：

```
TXAIAudioSDK.getInstance().onWakeup();
```

在开启语音请求的时候，也可以带上一些自定义的参数：

```
TXAIAudioRequestParam  param = new TXAIAudioRequestParam();
param.useLocalVad = true;// 不使用云端静音检测，例如遥控器上 按住按钮说话。
TXAIAudioSDK.getInstance().onWakeup(param);
```

设备应该在 isSdkNeedData 为 true 的时候，对 SDK 进行语音填充，SDK 将语音进行压缩后，发送到后台进行语音识别和语义分析。录制的声音需要 16bit 16KHZ 单声道的 pcm 数据。

```
TXAIAudioSDK.getInstance().feedRecordData(buffer);
```

如果你需要知道识别的中间结果，可以通过设置 RecognizeEventListener 获得：

```
TXAIAudioSDK.getInstance().setRecognizeEventListener(new TXAIAudioSDK.RecognizeEventListener() {
    @Override
    public void onRecognizeBegin(String voiceId) {

    }

    @Override
    public void onRecognize(String voiceId, String text) {
    }

    @Override
    public void onRecognizeEnd(String voiceId) {

    }
});
```

至此，我们已经完成了一次语音请求，当后台返回需要播放的结果后，将使用 SDK 的播放控制进行播放，具体参照 [播放控制说明](https://cloud.tencent.com/document/product/645/14221
);

#### TXAIAudioSDK 的其他接口说明

| 方法名                          | 说明                                                                                                            |
|:--------------------------------|:----------------------------------------------------------------------------------------------------------------|
| requestText                     | 直接使用文本进行语义分析，模拟用户说了这句话。                                                                  |
| requestTTS                      | 播放指定的文本。                                                                                                |
| activeRequestSkill              | 进入指定 Skill。                                                                                                 |
| setAudioWakeupEnable            | 设置唤醒模块是否可用。                                                                                          |
| setLocalAppEvent                | 设置当前本地 App 的状态，例如：进入导航模式，退出导航模式。                                                       |
| getDevStateInfo                 | 获取设备状态信息的接口（暂时只有获取代收状态）。                                                                |
| setMsgboxChatMode               | 消息盒子 - 设置畅聊模式（默认关闭，开启后不再播放 播放消息前的收到 xxx 的消息提示音）。                             |
| setMsgboxActiveAutoPlay         | 消息盒子 - 设置活跃状态自动播放收到的消息开关（默认开启，关闭后不再自动播放收到的消息）。                         |
| setMsgboxLocalNotifyEnable      | 消息盒子 - 设置使用播放本地提示音（默认关闭，长安车机播放网络提示音很慢，改用本地提示音播放）。                   |
| setMsgboxAutoPlayNext           | 消息盒子 - 设置自动播放下一条未读消息的开关（默认开启）。                                                         |
| setMsgboxSingleUinMode          | 消息盒子 - 设置单用户模式，播放消息按第一条主动播放的消息的 uin 来过滤依次播放（默认关闭)。                         |
| onWakeup(TXAIAudioRequestParam) | 开始语音请求的时候带上参数，比如不使用云端静音检测。                                                            |
| feedRecordDataEnd               | 不使用静音检测的时候主动通知 SDK 说完了。                                                                         |
| setOnFriendListChangeListener   | 消息电话代收的联系人变化的监听。                                                                                |
| setVideoCodeParam               | 设置码表参数，如果两端都设置，则以本端为准。                                                                    |
| setVideoEncDecMode              | 设置硬软编解模式, 这个标记只对 Android4.4 以上系统生效。                                                           |
| enableRealtimeWordslist         | 开启关闭可见可达                                                                                                |
| setWordslist                    | 设置可见可达屏幕词表。                                                                                          |
| activeApp                       | 切换播放控制激活的场景，参照 [播放控制说明](https://cloud.tencent.com/document/product/645/14221)。              |
| dataReport                      | 上报事件发生记录，参照 [播放控制说明](https://cloud.tencent.com/document/product/645/14221)。                    |
| fireClockEvent                  | 触发后台闹钟，参照 [Skill 对接](https://cloud.tencent.com/document/product/645/14247)。             |
| getMorePlayList                 | 加载更多播放列表元素，参照 [UI 模板实现指引](https://cloud.tencent.com/document/product/645/14224)。              |
| getPlayDetailInfo               | 加载更多播放列表元素，参照 [UI 模板实现指引](https://cloud.tencent.com/document/product/645/14224)。              |
| setChatParam                    | 设置通话的参数，参照 [音视频通话接入指引](https://cloud.tencent.com/document/product/645/14233)。 |
| setFavorite                     | 收藏或取消收藏指定音乐，参照 [UI 模板实现指引](https://cloud.tencent.com/document/product/645/14224)。            |
| setPlayerEventListener          | 设置播放控制播放器事件监听，参照 [UI 模板实现指引](https://cloud.tencent.com/document/product/645/14224)。        |
| setIPlayerManager               | 设置播放控制的播放器，参照 [播放控制说明](https://cloud.tencent.com/document/product/645/14221)。                |
| setPlayerCurrentState           | 设置播放控制的播放器状态，参照 [播放控制说明](https://cloud.tencent.com/document/product/645/14221)。            |
| setPlayByID                     | 设置当前播放的音乐元素，参照 [UI 模板实现指引](https://cloud.tencent.com/document/product/645/14224)。            |
| getMsgInfo                      | 拉取消息详情接口，参照 [UI 模板实现指引](https://cloud.tencent.com/document/product/645/14224)。                  |
| setMsgCommand                   | 控制指定的消息，参照 [UI 模板实现指引](https://cloud.tencent.com/document/product/645/14224)。                    |
| startAudioVideoChat             | 呼叫指定的用户，参照[音视频通话接入指引](https://cloud.tencent.com/document/product/645/14233)。 |
