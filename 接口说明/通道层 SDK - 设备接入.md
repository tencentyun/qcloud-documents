## 方案简介
为了提供更好的智能化设备体验，我们打造了集成腾讯云AI能力的语音方案。本文档就方案的接入进行分析说明，为设备对接提供指导和帮助。

智能语音方案[channel版本]的能力大致分为以下几个部分（详细说明，请参见章节：**能力说明**）：

> *   静音检测
> *   语音识别
> *   语义分析
> *   语音Skills服务

为了简化设备对接难度，提升方案的集成度、安全性，我们提供设备SDK植入的方式进行对接。

同时，绝大部分能力整合在云端，设备端SDK通过简单有效的接口，提供外部服务：

[![img_main](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/xiaowei_main.jpg)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/xiaowei_main.jpg)

我们在设备SDK端，提供了一条通用的语音通道，用于上传语音指令，云端会对语音进行一系列的处理，返回处理结果和资源列表，SDK处理后，会把语音状态和其他数据回调给接入层：

[![img_channel](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/Channel_interface.png)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/Channel_interface.png)

## 能力说明
| 能力类型 |  | 是否支持通道层对接 | 说明 |
| --- | :-: | :-: | :-- |
| 静音检测 | 云端 | 是 | 也支持使用设备自有本地静音检测的能力 |
| 语音识别 | 云端 | 是 |  |
| 语义分析 | 云端 | 是 |  |
| 小微自有Skills | 云端 | 是 |  |
| 第三方Skills | 云端 | 否 | 目前只支持全功能SDK |

## 接入流程

接入大致分为以下几个步骤：

*   从[小微硬件开放平台](https://xiaowei.qcloud.com/hardware.html)申请接入，具体可以参考[接入流程指引](/wiki/#hardware_product_intro)。
*   下载小微设备端SDK，小微目前具备Android和Linux两个平台的SDK。[获取通道层SDK](/wiki/#APIDesc_tunnel_interface)
*   参考文档和demo实现功能并进行测试。
*   提供体验设备，完成产品体验。

## 接入腾讯云小微硬件开放平台

### 简介概述

腾讯云小微硬件开放平台是一个能将语音交互能力输出给第三方硬件厂商的平台，无论是音箱、电视、玩具、OTT盒子、投影仪还是汽车，只需要一个SDK即可完成接入，为设备赋予人工智能语音能力。

硬件开放平台接入目前支持Android和linux两大平台接入。

腾讯云小微硬件开放平台将语音唤醒、语音识别、语义分析、信令收发以及众多的内置资源及服务，如音乐、天气、导航等核心能力提供给智能音箱、智能电视、智能玩具、OTT盒子等传统硬件领域的合作伙伴，实现用户与设备、设备与服务之间的语音联动能力。

我们致力于帮助传统硬件快速转型为具有语音控制能力的智能硬件，帮助合作伙伴降低云端、APP端等研发成本，提升用户粘性并通过开放腾讯的丰富资源以及服务来给予硬件更多想象空间。

### 硬件开放平台框架

[![硬件开放平台框架](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/硬件开放平台框架.png)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/硬件开放平台框架.png)

### 硬件设备能力概述（有屏 & 无屏设备）

目前接入硬件开放平台的设备分为有屏和无屏两大类设备，有屏设备相较于无屏设备多了在显示屏上可触摸交互的一部分操作，这部分内容可以详见有屏设备交互规范，在这里不多作赘述。

现在，我们来看一下接入之后的硬件设备所获得的能力：

硬件厂商完成sdk接入之后，传统硬件便获得了语音交互的能力，整个产品的使用流程包含以下5个步骤，先来看一张概览图：

[![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/能力.png)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/能力.png)

1：用户可通过语音唤醒音箱（或其他硬件设备，此处以音箱为例），并说出具体的指令；

在这里指令的内容指的是腾讯云小微skill的能力（具体skill的能力和配置可见skill部分wiki，在这里不多作赘述），包含内置skill和第三方skill两大块，提供丰富的资源和服务能力，下图是重点能力的概览。

[![腾讯云小微skill能力](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/腾讯云小微skill能力.png)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/腾讯云小微skill能力.png)

2：音箱将语音内容传送到云端；

基于腾讯云为设备提供快速、安全、稳定的云端环境，让硬件设备开发者更加聚焦在硬件设计与功能创新本身。

3：云端对用户的语音进行识别与分析；

我们具有行业领先的语音语义能力，丰富的数据基础，每天数亿的全自然语音调用量训练，语音识别的准确率高达97%，从发起语音到内容播出小于1秒。

4：分析完成，将内容传输回音箱；

5：音箱播放最终结果给用户。

### 硬件开放平台申请接入流程

开发者申请接入腾讯云小微硬件开放平台需要在[官网](https://xiaowei.qcloud.com/hardware.html)递交申请资料，进入腾讯云小微官网--硬件开放开放--点击【申请内测】：

[![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/申请内测.jpg)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/申请内测.jpg)

点击申请之后需要完善开发者的相关信息:

1.基本信息：请确保信息准确无误，以免耽误后续审核的过程中的联系失败；

2.公司信息：请上传公司的营业执照进行资质认证，并确保提交的公司规模信息准确；

3.技术参数：请根据需求选择符合自己硬件设备的技术参数，如有疑问可参见技术wiki。

[![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/资料填写.jpg)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/资料填写.jpg)

以上信息确认填写无误之后，选择提交，会获得您的申请接入单号，腾讯云小微团队会尽快通过邮件反馈审核结果给开发者注册的邮箱地址，开发者也可以在申请页面查看审核进度及反馈。

[![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/申请记录.png)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/申请记录.png)

当申请通过之后，再次进入官网硬件开放平台，会看到【申请内测】的button变成了【开始接入】，此时点击【开始接入】即可进入配置平台进行具体的硬件开发配置。

[![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/开始接入.jpg)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/开始接入.jpg)

## 配置平台使用说明

### 添加新设备

进入配置平台之后，点击添加设备按钮，填写【设备名称】及选择【设备类型】后即可开始快速注册一个新设备；

设备名称：您可以自由填写，设备名称请尽量用中文并控制长度。

设备类型：必须填写准确，后期无法进行修改，这里我们选择设备类型为音箱。

[![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/配置平台-添加设备.png)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/配置平台-添加设备.png)

完成后，我们已经获得了该产品获得重要信息：pid和server key，这两个信息非常重要，会在SDK登录的时候中用到。

在设备导航栏中，选择进入相应的设备，即可在头部看到这两个信息，请看下图：

[![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/配置平台-pid.jpg)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/配置平台-pid.jpg)

### 填写设备信息

当您完成一个新设备的创建之后，需要继续补充完善设备的信息，这里包含【基础信息】和【设备信息】两部分。

[![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/配置平台-基本信息.png)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/配置平台-基本信息.png)

进入到刚刚创建的设备-设备信息tab，补充完整设备的【基本信息】：

设备型号：您可以自由填写，设备名称请尽量用中文并控制长度；

设备图标：请上传jpg、png格式的图片，大小为512*512；

设备描述：请尽量简明扼要的描述您设备的主要功能及特点。

然后需要补充【设备信息】：

操作系统：这里我们支持androd和linux两大操作系统；

是否带屏幕：请根据您的设备实际情况进行选择；

公钥上传 稍微复杂一点，因为您需要下载一个我们的工具来完成这个步骤，点击 网页上的“公钥&证书工具下载（Win 7 Only）” 链接，然后运行密钥生成工具，点击下图中的生成KEY按钮，会在您指定的目录下生成一对非对称密钥文件： ec_key.pem 和 public.pem。之后点击上传按钮上传public.pem 就可以了。

[![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/配置平台-公钥.png)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/配置平台-公钥.png)

### 为设备配置skill

每一个接入腾讯云小微的硬件都有使用我们强大资源和服务的权限，此处需要使用同一个账号在我们腾讯云小微skill平台进行创建，创建完成之后就会显示在这里，开发者可以自行选择该硬件需要使用的skill。

[![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/配置平台-skill.png)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/配置平台-skill.png)

### OTA能力管理

OTA能力配置中分为【正式环境】和【测试环境】两个部分，开发者每上传一个OTA包的时候需要先填写相关的版本信息；

在测试环境中允许向指定的设备推送升级，需要上传对应的sn包，限制为100个。

[![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/配置平台-OTA.png)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/配置平台-OTA.png)

### 样机审核

当产品所有功能均开发完毕后需要将样机寄送至腾讯云小微团队进行测试审核，只有审核通过之后产品才可以正式认证上线。

## 实现指引

我们提供linux和Android两个平台的SDK，接下来对这两个平台的接入实现分别做说明。

> 下面说明中的部分名词 可以参考[名词解释](/wiki/#NoviceGuide_glossary)。

### 实现指引-android

Android SDK文件为tx_device_android_sdk-release.aar，可以使用Android Studio引入到您的项目中。

详细API请参照AndroidDoc目录下的index.html。

对接实现建议分为以下几个步骤：

**1.语音模块初始化**

语音模块的初始化要保证在 设备收到SDK登录成功的事件`TXDeviceBaseManager.OnDeviceLoginEventListener.onLoginComplete`后：

```
TXAudioManager.getInstance().init(context, deviceInfo, accountData);
```

其中，deviceInfo中的properties可以参考CommonDef中的txca_device_定义来添加设备具备的本地能力

目前支持的主要是txca_device_local_vad，当使用本地静音检测后，降不再做云端静音检测

accountData参数为预留参数，置空即可

**2.请求接口对接**

该步骤要完成请求接口的调用：

<1> 当设备设备唤醒后(暂不提供唤醒模块，唤醒功能需要自行实现)，即可调用`TXAudioManager.request`方法开始请求。

```
TXAudioManager.getInstance().request(type, requestData, contextinfo, new TXAudioManager.RequestListener(){...});
```

其中，type表示请求类型，目前支持音频`txca_chat_via_voice`、文本`txca_chat_via_text`两种请求方式。

requestData为请求数据，音频请求时，需要携带音频数据；文本请求时，携带请求字符串。

contextinfo用来携带请求的上下文信息，包括上一次RequestListener返回的contextinfo结果，和是否为首包`voiceRequestBegin`或尾包`voiceRequestEnd`。

当进行语音请求时，数据要求为:`单声道`、`16k采样率`、`16bit采样位宽`，且不做编码。

语音请求，调用request方法的频率要求每秒不低于8次，保证数据流的实时和持续。

如果使用云端vad，在收到`TXAudioManager.RequestListener.onRequest`且`event==CommonDef.txca_event_on_silent`后，停止请求。

如果使用本地vad，根据本地检测情况，在本地静音后，`TXAudioManager.request`的`contextinfo.voiceRequestEnd`需要置成`true`，通知请求结束。

<2> 当设备需要主动/强制终止一次会话时(如按键操作)，调用`TXAudioManager.requestCancel`方法。

```
TXAudioManager.getInstance().requestCancel();
```

**3.状态上报接口对接**

当响应中的播放资源，进行播放时，需要把状态通过`TXAudioManager.reportState`接口传入SDK，以保证请求的正常处理（如：收藏音乐）。

状态包括：

```
public static final int txca_playstate_preload           = 0;        // 预加载
public static final int txca_playstate_resume            = 1;        // 继续
public static final int txca_playstate_paused            = 2;        // 暂停
public static final int txca_playstate_stopped           = 3;        // 一首歌播放完毕
public static final int txca_playstate_finished          = 4;        // 歌单播放结束，停止播放了
public static final int txca_playstate_idle              = 5;        // 空闲
public static final int txca_playstate_start             = 6;        // 一首歌开始播放
```

其中最主要的有：`txca_playstate_start`、`txca_playstate_idle`。

**4.请求响应处理**

当拿到请求的响应结果后，需要根据Response中的`hasMorePlaylist`、`isRecovery`、`playBehavior`对播放资源进行处理。

同时，需要根据播放资源`Resource`的`format`来处理对应的字段，下表为不同的格式，对应的字段内容：

| format | ID | content | extendInfo |
| --- | :-: | :-: | :-: |
| txca_resource_url | playID | url | 歌曲信息json |
| txca_resource_notify | null | url | null |
| txca_resource_text | resID | 文本 | null |
| txca_resource_command | propID | propValue | null |

*   propID和propValue的具体解释，请咨询小微开发人员

context需要保存下来，在下一次请求时带上，如果context的ID非空，表示存在下一轮询问，需要自动启动下一次请求。

**5.播放资源获取**

<1> 当前正在处理的资源列表`hasMorePlaylist==true`时，说明有更多分页，当播放到列表的最后几首时，可以使用`TXAudioManager.getPlaylist`来拉取下一分页的资源。

```
TXAudioManager.getInstance().getPlaylist(appInfo, playid, 6, new TXAudioManager.RequestListener(){...});
```

playid为当前正在播放的资源ID，appInfo为当前资源对应的场景信息。

<2> 当设备需要获取某一个资源的详细信息时：音乐的歌词和收藏，可以使用`TXAudioManager.getPlayDetailInfo`来进行获取，获取的结果会在`TXAudioManager.RequestListener.onRequest`的extendData字段中，以json的形式提供。

```
{
   "data":[
      {
         "album":"The One演唱会",
         "artist":"周杰伦",
         "cover":"http:\/\/y.gtimg.cn\/music\/photo_new\/T002R120x120M000001O06fF2b3W8P.jpg",
         "duration":209,
         "isFavorite":false,
         "lyric":"[ti:上海一九四三(live版)]\n[ar:周杰伦]\n[al:The One演唱会]\n[by:]\n[offset:0]\n[00:01.52]上海一九四三 (Live) - 周杰伦\n[00:03.37]词：方文山\n[00:04.24]曲：周杰伦\n[00:05.12]编曲：林迈可\n[00:06.31]\n[00:12.67]依稀可见几个字岁岁平安\n[00:16.76]在我没回去过的老家米缸\n[00:20.64]爷爷用楷书写一个满\n[00:24.48]黄金葛爬满了雕花的门窗\n[00:28.93]夕阳斜斜映在斑驳的砖墙\n[00:33.37]举着木板生锈的老家门口\n[00:37.57]爷爷用楷书写一个满\n[00:41.67]我对着黑白照片开始想像\n[00:45.48]爸和妈当年的模样\n[00:50.63]说着一口吴侬软语的姑娘缓缓走过外滩\n[00:59.51]消失的 旧时光 一九四三\n[01:02.71]一九四三\n[01:04.01]\n[01:04.63]在回忆 的路上 时间变好慢\n[01:07.62]时间变好慢\n[01:09.38]老街坊 小弄堂\n[01:11.15]消失的 旧时光 一九四三\n[01:18.37]回头看 的片段 有一些风霜\n[01:21.99]老唱盘 旧皮箱\n[01:24.17]\n[01:24.73]装满了明信片的铁盒里藏着一片玫瑰花瓣\n[01:49.38]黄金葛爬满了雕花的门窗\n[01:52.72]夕阳斜斜映在斑驳的砖墙\n[01:56.73]铺着榉木板的屋内还弥漫\n[02:01.11]爷爷在街口那等着\n[02:05.56]我对着黑白照片开始想像\n[02:09.17]爸和妈当年的模样\n[02:13.82]\n[02:14.92]说着一口吴侬软语的姑娘缓缓走过外滩\n[02:23.96]消失的 旧时光 一九四三\n[02:27.85]在回忆 的路上 时间变好慢\n[02:32.33]老街坊 小弄堂\n[02:34.35]是属于那年代白墙黑瓦的淡淡的忧伤\n[02:40.17]消失的 旧时光 一九四三\n[02:44.63]回头看 的片段 有一些风霜\n[02:49.66]老唱盘 旧皮箱\n[02:50.50]装满了明信片的铁盒里藏着一片玫瑰花瓣\n[03:04.56]一九四三 三 一九四三",
         "name":"上海一九四三",
         "playId":"p=1&uuid=8203&unique_id=7098056"
      }
   ]
}
```

### 接入细节

上文讲解了每个功能的对接，部分重要细节可能不够详细，对于部分方面的接入细节，我们准备了以下几篇文档，供参考：

[多轮对话](/wiki/#TechMisc_multi_round_chat)

[静音检测](/wiki/#TechMisc_mute_detect)

[状态上报](/wiki/#TechMisc_status_report)

### 流程调试

完成以上的实现步骤后，即可开始完整的流程调试。

整个会话过程，可以参考`方案简介`中的流程图：

[![img_channel](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/Channel_interface.png)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/Channel_interface.png)

## 其他

对接过程中碰到问题，建议阅读接入文档 & 查阅 FAQ 尝试解决。

如果无法解决，请和我们的技术客服**QQ:xiaowei_helper@tencent.com**取得联系。
