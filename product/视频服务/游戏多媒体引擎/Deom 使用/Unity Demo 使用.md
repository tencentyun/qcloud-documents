
为方便 Unity 开发者调试和接入腾讯云游戏多媒体引擎产品 API，这里向您介绍适用于 Unity 开发的 DEMO 使用文档。

## 登录

输入 UserId，单击【Login】，系统则会使用设置的 UserId 进行登录。登录后，界面将会新增【Voice Chat】和【Voice Message】两个按钮。
- 单击【Voice Chat】，将会进入 [语音聊天](#test1) 功能。
- 单击【Voice Message】，将会进入 [语音消息](#test2) 功能。

![](https://main.qcloudimg.com/raw/dbacd4455622253ddb07d53e1bc785b8.png)
<span id="test1"></span>
## 语音聊天

语言聊天界面如下所示：
![](https://main.qcloudimg.com/raw/3807e7d6946948c06e47f51ad9e7a2b4.png)
- RoomId：房间号相同的成员会进入同一个房间。
- RoomType：控制语音质量。
  - Fluency：流畅音质。流畅优先、超低延迟实时语音，应用在游戏内开黑场景，适用于 FPS、MOBA 等类型的游戏。
  - Standard：标准音质。音质较好，延时适中，适用于狼人杀、棋牌等休闲游戏的实时通话场景。
  - Hign Quality：高清音质。超高音质，延时相对较大，适用于音乐舞蹈类游戏以及语音社交类 App；适用于播放音乐、线上 K 歌等有高音质要求的场景。
 
单击【JoinRoom】进入房间。
![image](https://main.qcloudimg.com/raw/a2ac816eacd95dfa89c8a5cee4f93f40.png)
- Speaker：打开扬声器。
- Talking Members：房间内正在说话的人。
- 3D Voice Effect：打开 3D 音效。
- Voice Change：修改实时语音音效。
- 3D Voice Effect setting。
  - X：自身 x 轴。
  - Y：自身 y 轴。
  - Z：自身 z 轴。
  - XR：绕 x 坐标轴旋转的方向。
  - YR：绕 y 坐标轴旋转的方向。
  - ZR：绕 z 坐标轴旋转的方向。

<span id="test2"></span>
## 语音消息

语言消息界面如下所示：
![](https://main.qcloudimg.com/raw/c3461b2510032f033f0417890c636f2d.png)
- Language：使用的语言。
- Audio：录制的语音消息和语音时长。单击 ![image](https://main.qcloudimg.com/raw/7d268c4b1bb7e1998792b19a23e7bb63.png) 播放录音，播放过程中再次单击，结束播放。
- Audio-to-Text：语音转换成的文字，按下【Push To Talk】，开始录制；松开【Push To Talk】，结束录制。
