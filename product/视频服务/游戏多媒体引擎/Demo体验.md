
<table>
  <tbody><tr>
    <th style="text-align:center;" width="150px"><b>Android<br></b>使用摄像机扫码</th>
    <th style="text-align:center;" width="150px"><b>iOS<br></b>使用摄像机扫码</th>
  </tr>
  <tr>
    <td style="
    text-align: center;
"><img style="width:150px; max-width: inherit;" src="https://main.qcloudimg.com/raw/17b2a65547432f5d81391fce1fa17a90.png" class="zoom-img-hover"></td>
    <td style="
    text-align: center;
"><img style="width:150px; max-width: inherit;" src="https://main.qcloudimg.com/raw/17b2a65547432f5d81391fce1fa17a90.png" class="zoom-img-hover"></td>
  </tr>
</tbody></table>

## Android/iOS Unity Demo 基本功能演示


<span id="test"></span>

### 登录

输入 UserId，单击 **Login**，系统则会使用设置的 UserId 进行登录。登录后，界面将会新增 **Voice Chat** 和 **Voice Message** 两个按钮。
<img src="https://main.qcloudimg.com/raw/dbacd4455622253ddb07d53e1bc785b8.png"  width="80%" /></img><br>
- 单击 **Voice Chat**，将会进入 [语音聊天](#test1) 功能。
- 单击 **Voice Message**，将会进入 [语音消息](#test2) 功能。

<span id="test1"></span>

### 语音聊天


1. [登录](#test) 之后，单击 **Voice Chat** 进入语音聊天界面：
<img src="https://gme-public-1256590279.cos.ap-nanjing.myqcloud.com/GMEResource/IMB_KuI8ov.gif"    width="80%"/></img><br>
 - RoomId：房间号 ID，房间号相同的成员会进入同一个房间。
 - RoomType：用于控制语音质量。
    - Fluency：流畅音质。流畅优先、超低延迟实时语音，应用在游戏内开黑场景，适用于 FPS、MOBA 等类型的游戏。
    - Standard：标准音质。音质较好，延时适中，适用于狼人杀、棋牌等休闲游戏的实时通话场景。
    - Hign Quality：高清音质。超高音质，延时相对较大，适用于音乐舞蹈类游戏以及语音社交类 App；适用于播放音乐、线上 K 歌等有高音质要求的场景。


2. 在语音聊天界面，单击 **JoinRoom** 进入房间：
<img src="https://gme-public-1256590279.cos.ap-nanjing.myqcloud.com/GMEResource/IMB_8zP4w2.gif"  width="80%"/><br>
 - Talking Members：房间内正在说话的成员，界面将会显示正在说话的成员 ID。
 - Mic：麦克风，勾选表示打开。 
 - Speaker：扬声器，勾选表示打开。
 - 3D Voice Effect：3D 音效，勾选表示打开，可通过设置以下参数进行配置：
    - Range：设置语音接收范围，单位为游戏引擎单位。
    - X：自身 X 轴。
    - Y：自身 Y 轴。
    - Z：自身 Z 轴。
    - XR：绕 X 坐标轴旋转的方向。
    - YR：绕 Y 坐标轴旋转的方向。
    - ZR：绕 Z 坐标轴旋转的方向。
 - Voice Change：实时语音音效，可通过选择不同的参数类型，改变播放音效特性，详情可参考 [实时语音音效](https://cloud.tencent.com/document/product/607/34378#k-.E6.AD.8C.E9.9F.B3.E6.95.88.E7.89.B9.E6.95.88)。


<span id="test2"></span>

### 使用语音消息转文本

[登录](#test) 之后，单击 **Voice Message** 进入语言消息界面：
<img src="https://gme-public-1256590279.cos.ap-nanjing.myqcloud.com/GMEResource/IMB_DsvaLv.gif"  width="80%"/></img><br>
- Language：使用的语言。
- Audio：录制的语音消息和语音时长。单击<img src="https://main.qcloudimg.com/raw/7d268c4b1bb7e1998792b19a23e7bb63.png" width="3%"></img>播放录音，播放过程中再次单击，结束播放。
- Audio-to-Text：语音转换成的文字，鼠标单击长按 **Push To Talk**，开始录制；鼠标松开 **Push To Talk**，结束录制。


## Windows 平台 3D 语音体验 Demo


### 前提条件
- 此演示程序需要在 Windows 平台运行。
- 演示程序需要在同一机器上双开程序，或者同一局域网下的两台机器分别开一个程序。
- 请确保电脑耳机及麦克风是可用状态。

### 1. 下载

单击下载 [3D语音演示程序](https://picture-1256313114.cos.ap-beijing.myqcloud.com/GMEDemo.zip)，下载完后进行解压。

### 2. 打开 Demo

双击打开标题为**GMEDemo.exe**的可执行文件，即 Demo 程序。可在同一机器上同时打开两个演示程序。

### 3. 初始化

初始化程序需要填入 [游戏多媒体引擎控制台](https://console.cloud.tencent.com/gamegme/detail/1400391524) 服务管理中的 AppID 以及权限密钥。申请 GME 服务，详情请参见 [接入指引](https://cloud.tencent.com/document/product/607/10782)。**appId 对应控制台的 AppID，authKey 对应控制台的权限密钥。**


<dx-alert infotype="explain" title="">
- 请务必注意保存 AppID 以及权限密钥不被泄露。
- 请注意此时的 userId 数字，请确保打开的另一个演示程序中的 userId 与此 userId 不同。
</dx-alert>



<img src="https://main.qcloudimg.com/raw/33540519cd5c2bdde6139f8a4af537a6.png"  width="80%"><br>
填写完成后单击**初始化**>**实时语音**，进入实时语音房间填写界面。

### 4. 进入语音房间

此时进入语音房间选择界面，可以填写进入的房间号。如果此时打开了另一个演示程序，也请填写相同的房间号，单击 **JoinRoom** 进入**同一语音房间**。

<img src="https://main.qcloudimg.com/raw/7393dbb31007299894586205cb8b6f9c.jpg"  width="80%">

### 5. 游戏界面介绍

界面信息说明如下：
- 退出按钮：单击后退出到语音房间选择界面。
- 打开/关闭麦克风：默认进房是关闭麦克风状态，需要打开麦克风才可以进行通话。
- 使用帮助：单击后打开使用帮助界面。
- 打开伴奏：单击后开始播放伴奏。
- 界面右下角：房间日志信息，显示进入和退出语音房间的用户。
- 界面左边：本地连接按钮。需要配置后才会正式开始游戏。
<img src="https://main.qcloudimg.com/raw/0e451b80402caeb31cf6bd932acee127.png"  width="80%"/></img>

### 6. 本地连接

**此演示程序需要本地局域网连接基础**。
<img src="https://main.qcloudimg.com/raw/670b24a1133dc07bdc9892ffa12b159f.png" width="80%" /></img>
- 第一个进房间的人
第一个进房间的人是需要作为网络连接的 Host，所以需要单击 **LAN Host(H)**。单击之后会将人物生成在金币旁边。
<img src="https://gme-public-1256590279.cos.ap-nanjing.myqcloud.com/GMEResource/master.gif"  width="80%"/></img>

- 非首位进房间的人
非首位进房间的人需要与 Host 连通，所以需要单击 **LAN Client(C)**。单击之后会将人物生成在金币旁边，此时可以见到第一个进入房间的人。
<img src="https://gme-public-1256590279.cos.ap-nanjing.myqcloud.com/GMEResource/client.gif"  width="80%"/></img>

### 7. 打开麦克风

单击<img src="https://main.qcloudimg.com/raw/1fd9f4e3f35cfc166e04bd26fb520abf.png" width="3%"></img>可以打开麦克风，此时可以与房间里面的人通话。

### 8. 操作方式

键盘上的"W"、"S"、"A"、"D"分别对应“前进”、“后退”、“左转”、“右转”，鼠标转动可以调整视角。连接后的客户端上可以看到另一个客户端上所操作的角色。
<img src="https://gme-public-1256590279.cos.ap-nanjing.myqcloud.com/GMEResource/linaji.gif"  width="80%"/></img>

### 9. 如何体验

如果是本地双开演示程序，可以先把其中一个演示程序的视角移动到金币旁边，打开麦克风，另一个演示程序的小人尽可能的跑远，期间不停说话，便可以体验3D的语音效果，跑到地图边界，此时的声音会衰减到几乎听不到。
<img src="https://gme-public-1256590279.cos.ap-nanjing.myqcloud.com/GMEResource/yuan.gif"  width="80%"/></img>


