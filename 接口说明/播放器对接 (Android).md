## 简介

播放控制接口主要分三类， 包括了完整的语音下行数据处理方式 1\. 基础接口 2\. TTS接口 3\. 音乐接口(url类型)

## 基础接口

基础接口包括 创建、控制、状态同步

播放器管理类需要通过 `TXAIAudioSDK.setIPlayerManager` 来设置 实现 IPlayerManager.createIPlayer 返回一个播放器实例

**IPlayerManager.createIPlayer** SDK在恰当时机会调用该方法, SDK内部将以pid作为控制播放器的唯一标志，

> 在实现IPlayerManager.createIPlayer时，可以自行决定是否创建真实的播放器。 一个pid对应的是一个播放器的控制权，实现时可以根据需要(如设备性能等)， 创建少数或单个播放器，并将不同的pid映射到同一个实体播放器， 在实现控制时，诸如暂停、继续等动作将资源独立保存， 切换pid后将对应的资源重新按照指定的规则播放即可

**IAIPlayer.control(int cmd, int value)** 控制播放器行为，cmd和value分别表示控制指令和对应的数据，如下

| cmd | value | 说明 |
| --- | --- | --- |
| AIPlayerDef.CMD_STOP | 0 | 停止播放 |
| AIPlayerDef.CMD_START | 0 | 开始播放, 需要清空对应播放器的资源并准备新的一次播放 |
| AIPlayerDef.CMD_PAUSE | 0 | 暂停播放 |
| AIPlayerDef.CMD_RESUME | 0 | 继续播放 |
| AIPlayerDef.CMD_SET_VOLUME | 0~100 | 调节音量, 在全局音量的基础上， 调整当前播放器音量为 value%，如value=50, 则调整为 50% |

**TXAIAudioSDK.setPlayerCurrentState(int playerID, int state)** 在播放资源完成后， 需要通知sdk，当前播放器资源已播放完毕 state=`3`

## TTS接口

tts接口用于播放tts语音资源，数据将以流的形式提供

**IAIPlayer.playTTSBegin(int pcmSample)** 收到tts参数, 包括 pcmSample: pcm采样率

**IAIPlayer.playTTS(int seq, byte[] data)** 开始收到 pcm数据, 可直接用于播放或保存成pcm文件 seq: 收到的第几个数据包 data: pcm数据

**IAIPlayer.playTTSEnd()** tts数据接收完毕

## 音乐接口(url类型)

**IAIPlayer.playRes(int type, String res)** 播放type类型的资源

| type | res | 说明 |
| --- | --- | --- |
| AIPlayerDef.RES_TYPE_URL | url | url类型资源， 下载后播放 |
| AIPlayerDef.RES_TYPE_FILE | 文件路径 | 从本地加载后播放 |
| AIPlayerDef.RES_TYPE_OTHER | 其它资源类型 | 暂无， 目前可当做url播放 |
