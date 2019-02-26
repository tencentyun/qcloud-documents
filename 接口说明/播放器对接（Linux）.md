## 简介
播放控制接口主要分三类， 包括了完整的语音下行数据处理方式 1\. 基础接口 2\. TTS接口 3\. 音乐接口(url类型)

## 基础接口

基础接口包括 创建、销毁、控制、状态同步

播放器需要通过 `tx_ai_audio_configservice_with_player_callback` 来设置

```

//播放器回调
typedef struct _tx_ai_audio_player
{
    int  (*create)(int type);   //type as ai_audio_player_type
    void (*destory)(int pid);
    void (*controll)(int pid, const int ctrlcode, int value);

    void (*play_res)(int pid, int type, const char *content);
    void (*tts_push_start)(int pid, int sample, int channel, int pcmSample);
    void (*tts_push)(int pid, int seq, const char * data, int len);
    void (*tts_push_end)(int pid);
} tx_ai_audio_player;

tx_ai_audio_player player = {0};
player.create = on_player_create;
player.destory = on_player_destroy;
player.play_res = on_player_play_res;
player.controll = on_player_control;
player.tts_push_start = on_player_tts_push_start;
player.tts_push = on_player_tts_push;
player.tts_push_end = on_player_tts_push_end;

tx_ai_audio_configservice_with_player_callback(&player, .., ..);
```

**on_player_create** SDK在恰当时机会调用该方法， 需要返回pid 即`player id`, SDK内部将以pid作为控制播放器的唯一标志，因此要保证唯一

> 在实现on_player_create时，可以自行决定是否创建真实的播放器。 一个pid对应的是一个播放器的控制权，实现时可以根据需要(如设备性能等)， 创建少数或单个播放器，并将不同的pid映射到同一个实体播放器， 在实现控制时，诸如暂停、继续等动作将资源独立保存， 切换pid后将对应的资源重新按照指定的规则播放即可

**on_player_destory** 播放器销毁时调用

**on_player_control(int pid, const int ctrlcode, int value)** 控制播放器行为，ctrlcode和value分别表示控制指令和对应的数据，如下

| ctrlcode | value | 说明 |
| --- | --- | --- |
| tx_ai_audio_player_control_code_stop | 0 | 停止播放 |
| tx_ai_audio_player_control_code_start | 0 | 开始播放, 需要清空对应播放器的资源并准备新的一次播放 |
| tx_ai_audio_player_control_code_pause | 0 | 暂停播放 |
| tx_ai_audio_player_control_code_resume | 0 | 继续播放 |
| tx_ai_audio_player_control_code_volume | 0~100 | 调节音量, 在全局音量的基础上， 调整当前播放器音量为 value%，如value=50, 则调整为 50% |

**tx_ai_audio_player_statechange(int pid, int state)** 在播放资源完成后， 需要通知sdk，当前播放器资源已播放完毕 `tx_ai_audio_player_state_complete`

## TTS接口

tts接口用于播放tts语音资源，数据将以流的形式提供

**on_player_tts_push_start(int pid, int sample, int channel, int pcmSample)** 收到tts参数, 包括 pid: player id， 即使用哪个播放器播放, sample: 采样率 channel, 通道数, 目前为单通道 pcmSample: pcm采样率， 目前和sample一致

**on_player_tts_push(int pid, int seq, const char * data, int len)** 开始收到 pcm数据, 可直接用于播放或保存成pcm文件 seq: 收到的第几个数据包 data: pcm数据 len: 当次数据长度

**on_player_tts_push_end** tts数据接收完毕

## 音乐接口(url类型)

**on_player_play_res(int pid, int type, const char *content)** 播放type类型的资源 pid： 指定播放器

| type | content | 说明 |
| --- | --- | --- |
| ai_audio_content_type_url | url | url类型资源， 下载后播放 |
| ai_audio_content_type_file | 文件路径 | 从本地加载后播放 |
| ai_audio_content_type_other | 其它资源类型 | 暂无， 目前可当做url播放 |
