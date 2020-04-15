## 简介
为方便开发者调试和接入腾讯云游戏多媒体引擎产品 API，本文主要为您介绍 GME Native Sample Code 的使用文档。


## 操作步骤
Sample Code 实时语音界面截图如下所示：
<img src="https://main.qcloudimg.com/raw/1a65f3e7fe35da963bd48ab5a0f8bb4a.jpg" width="40%">


### 设置账号及 openID
修改实时语音界面中对应的 Appid、Key 及 OpenID 参数，然后单击【Init】。（初始化 SDK 前）
<img src="https://main.qcloudimg.com/raw/2498f0fc3c90eeea5b0cefccaf591f39.png" width="60%">


参数的来源，请参见 [接入指引](https://cloud.tencent.com/document/product/607/10782)。



>?此步可以忽略，默认使用 GME 提供的测试账号进行体验。

#### 使用实时语音的基本流程如下表格

|步骤|按钮名称|相应功能|
|----|----|---|
|1|Init|初始化 SDK|
|2|Enterroom|进入语音房间，房间号为 RoomID 中的号码|
|3|Capture|开启采集设备|
|4|Send|开启音频上行（此时已经能发送音频。同房间的人可以收到实时语音音频）|
|5|Play|开启播放设备|
|6|Rec|开启音频下行（此时若同个房间内其他用户有音频上行，则能听到相应的实时语音音频）|
|7|ExitRoom|退出房间（此时不能听到别人的声音，亦无法将自己的声音发送至别的用户）|
|8|Uninit|反初始化 SDK，彻底退出 GME|

>! 
- 步骤3和步骤5属于硬件操作，具有一定耗时。
- 步骤3和步骤4需同时为开启状态，才有音频上行。同理，步骤5及步骤6需同时为开启状态才能播放声音。


### 更改房间音频类型
1. 进房前，您可以对音频类型进行选择，具体效果请参见 [音质选择](https://cloud.tencent.com/document/product/607/18522)。
<img src="https://main.qcloudimg.com/raw/25929745d76d6e1de3adc16055729d0e/iosSimpleCode_2.png" width="20%">
2. 进房后，可以单击【ChangeRoomType】，进行房间音频类型的更改。


###  设置音量
进房后，拖动滑动条可以设置音量。
- 左边的滑动条设置的是采集设备音量，将影响采集到的声音的音量。
- 右边的滑动条设置的是播放设备的音量，影响的是本机播放设备输出的音量。

<img src="https://main.qcloudimg.com/raw/be4a7063f30e264ac8adf45e95d08598/iosSimpleCode_3.png" width="40%">

### 其他设置
#### 设置是否耳返
单击 Loopback 旁边的按钮，如果开启，将在播放设备听到自己的声音。

#### 设置伴奏
进房后，基本流程中的步骤3、4、5及6同时开启的状态下，单击 Accomp 旁边的按钮，同房间的用户将听到伴奏；如果此时耳返状态为开启，则本机也能听到伴奏。

#### 设置卡拉 OK 效果
在 ChangeKaraoke 按钮旁边的输入框，输入相应的参数，单击【ChangeKaraoke】，则发送的实时音频声音，将有相应的卡拉 OK 效果。效果对应的参数如下：

|参数代表|意义|
|-------------|------------- |
|0	|原声			|
|1	|流行			|
|2	|摇滚			|
|3	|嘻哈			|
|4	|舞曲			|
|5	|空灵			|
|6	|语音合成			|

#### 设置变声效果
在 ChangeVoiceType 按钮旁边的输入框输入相应的参数，点击 ChangeVoiceType 按钮，则发送的实时音频声音会有相应的变声效果。效果对应的参数如下：

|参数代表|意义|
|-------------|------------- |
|0	|原声			|
|1	|萝莉			|
|2	|大叔			|
|3	|空灵			|
|4	|死肥仔			|
|5	|重金属			|
|6	|歪果仁			|
|7	|感冒			|
|8	|困兽			|
|9	|重机器			|
|10	|强电流			|
|11	|幼稚园			|
|12	|小黄人			|


### 特殊说明
Demo 中使用了一些特殊接口，用于测试 SDK，请用户不要调用。
```
SetAppVersion
GetSDKVersion
SetAdvanceParams
SetTestEnv
SetRecvMixStreamCount
```


