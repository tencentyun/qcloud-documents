该指引会对后台返回的结构化数据进行说明，便于有屏设备收到结果后进行展示。
其中主要包括以下模块：

* **音乐**
* **天气**
* **闹钟**
* **纯文本**
* **QQ 消息**
* **QQ 电话**

收到 onState 后，如果 event 为 AI_AUDIO_STATE_RESPONSE，将会有结构化数据。

#### TXAIAudioEventInfo 结构说明

| 属性       |  说明 | 
| --------       | --------   | 
| appName        |    当前请求识别出的场景名称，例如音乐、天气    |  
| appID        |   当前请求识别出的场景 id    |  
| textQuestion        |   用户说的话    |  
| textAnswer        |  后台返回的TTS结果    | 
| errorCode       |   错误码，定义在 TXAIAudioDef.ERROR\_CODE\_DEF 中   | 
| extendBufType      |   结构化数据的类型，定义在 TXAIAudioDef.StructMsgType    | 
| extendBuf|   结构化数据的内容    | 

### 音乐
您可以参照 MainService.java 和 MusicActivity 中的实现。

**appName** 为“音乐”、“互动-笑话”、包含“流媒体”。
```
String data = new String(eventInfo.extendBuf);
```
data 的结构定义为：
```
public class TXMusicListInfo {
    public boolean needClear;
    public ArrayList<TXMusicInfo> data;
}

public class TXMusicInfo {
    public String name;
    public String artist;
    public String album;
    public String cover;
    public String playId;
    public int duration;
    public boolean isFavorite;
    public String lyric;
}

```

其中 needClear 表示是否需要清空之前的播放列表，TXMusicInfo 中随着语音请求结果返回的字段只有 name、artist、album、cover、playId 这几个基本字段，其余字段需要额外调用获取播放元素详情的接口进行查询。

***getPlayDetailInfo***

```
TXAIAudioSDK.getInstance().getPlayDetailInfo(new String[]{mTXMusicInfo.playId}, new TXAIAudioSDK.DeviceResponseListener() {
    @Override
    public void onRsp(int errCode, int rspType, TXAIAudioAppInfo data) {
        if (data == null || data.extendBuf == null) {
            return;
        }
        TXMusicListInfo info = com.tencent.device.util.JsonUtil.getObject(new String(data.extendBuf), TXMusicListInfo.class);
        TXMusicInfo musicInfo = info.data.get(0);// 这个元素有duration、isFavorite、lyric等详细字段
    }
});
```

***getMorePlayList***
当播放到最后一个元素的时候，播放控制会自动去请求更多，如果想提前拉取更多播放列表元素，可以调用该接口：

```
TXAIAudioSDK.getInstance().getMorePlayList();
```

***setFavorite***
如果希望单击 UI 上的按钮进行音乐收藏，可以调用该接口：

```
TXAIAudioSDK.getInstance().setFavorite("音乐", playId, true);
TXAIAudioSDK.getInstance().setFavorite("音乐", playId, false);
```


***setPlayByID***
如果希望切换到播放列表中的某一首歌，可以调用该接口：

```
int result = TXAIAudioSDK.getInstance().setPlayByID(playId);// 0 表示调用成功 ，如果失败，可能是播放控制的列表中没有这个playId，也可能是播放控制的栈顶场景中不包含这个playId。
```

***TXAIAudioSDK$PlayerEventListener***
如果希望知道播放相关的状态变化，可以调用***setPlayerEventListener***：

```
TXAIAudioSDK.getInstance().setPlayerEventListener(new TXAIAudioSDK.PlayerEventListener() {

    @Override
    public void onPlay(int playerId, final String playId, boolean fromUser) {
        mPlayer = PlayerManager.getInstance().getPlayer(playerId);// 保存当前正在播放的playId对应的播放器
    }


    @Override
    public void onPause(int playerId) {
        if (mPlayer != null && mPlayer.getPlayerId() == playerId) {
            Log.e(TAG, "onPause");
        }
    }

    @Override
    public void onResume(int playerId) {
        if (mPlayer != null && mPlayer.getPlayerId() == playerId) {
            Log.e(TAG, "onResume");
        }
    }

    @Override
    public void onSetPlayMode(int playMode) {// 定义在TXAIAudioDef.PLAY_MODE_DEF
        Log.e(TAG, "onSetPlayMode " + playMode);
    }

    @Override
    public void onShared(String playId, TXContactInfo to) {
        Log.e(TAG, "onShared " + playId + " " + to);
    }

    @Override
    public void onKeep(String playId) {
        Log.e(TAG, "onKeep " + playId);
    }

    @Override
    public void onUnKeep(String playId) {
        Log.e(TAG, "onUnKeep " + playId);
    }

    @Override
    public void onStop(int playerId) {
        if (mPlayer != null && mPlayer.getPlayerId() == playerId) {
            Log.e(TAG, "onStop " + playerId);
        }
    }
});
```

### 天气
用户询问了天气后，后台会返回当天天气的 TTS 和最近几天的结构化数据。您可以参照 WeatherActivity.java 对数据进行解析。

```
class Weather {
    String loc;
    ArrayList<WeatherItem> data;
}

class WeatherItem {
    String condition;
    String date;
    String max_tp;
    String min_tp;
    String pm25;
    String quality;
    String tp;
    String wind_direct;
    String wind_lv;
}
```
    
### 闹钟
具体参照 [Skill 对接](https://cloud.tencent.com/document/product/645/13451)。

### 纯文本
您可以参考 OtherActivity.java 的实现。
纯文本的场景包含百科、计算器、闲聊等等，后台只会返回用户说的话 *textQuestion* 和后台的回答文本 *textAnswer*。

### QQ 消息
收到 QQ 消息后，播放控制会维护一个消息盒子列表，在消息有变化的时候会通过 onState 通知外面，event 为`AI_AUDIO_STATE_CHANGED`；当开始和结束播放一条消息的时候，event 分别为 `AI_AUDIO_STATE_MSG_PLAY_START`、`AI_AUDIO_STATE_MSG_PLAY_STOP`。
      
根据现有的产品定义，消息盒子包括以下内容：

>* 支持所有收到消息的向上通知，形式为 `msg id` 的列表；
>* 支持接入层主动查询现有消息list，形式为 `msg id` 的列表；
>* 支持通过 `msg id` 批量查询消息详情 `TXAIAudioMsgInfo`；
>* 支持接入层控制任意一条消息的播放和停止；
>* 消息详情 `TXAIAudioMsgInfo` 中的 `peer id` 可以用来关联 `TXDeviceSDK.getTXContactInfo(peer id)`，以实现用户昵称和头像的显示。

同时，为了方便理解，针对现有的产品细节进行描述：

>* 消息列表只包含收到消息，不包含发出消息；
>* 语音控制`播放消息`时，只会顺序播放`未读消息`，如果没有，播放提示`没有更多消息了`；
>* 指令控制播放一条消息时，如果操作的是`未读消息`，播放完成后会播放下一条`未读消息`，直至结束，使用和语音控制相同的规则；
>* 指令控制播放一条消息时，如果操作的是`已读消息`，播放当前一条后，结束播放；

3 种事件的 json 格式是一致的，数据结构为：

```
// extendBuf字段中JSON数据格式
{  
   "data":[  
      {  
         "unReaded":3,
         "readed":0,
         "listMsgID":[6530,6531]
      }
   ]
}
```
listMsgID 是 msgid 的列表，unReaded 和 readed 分别是未读和已读消息数量。
`AI_AUDIO_STATE_CHANGED` 事件，会在接入层主动查询、收到新消息、或消息从未读切换成已读时回调。
回调时，listMsgID 为当前所有 msgid 的列表，unReaded 和 readed 分别是当前未读和已读消息数量。
`AI_AUDIO_STATE_MSG_PLAY_START` 和 `AI_AUDIO_STATE_MSG_PLAY_STOP` 是消息播放回调的，用来方便接入层展示当前的播放状态。
消息播放的触发分为两种：语音触发和指令接口调用触发。

#### 1. 消息详情查询
`TXAIAudioSDK.getMsgInfo`接口支持使用`msg id`批量查询消息详情`TXAIAudioMsgInfo`
```
TXAIAudioMsgInfo[] listMsgInfo = TXAIAudioSDK.getInstance().getMsgInfo(listMsgID);
```
其中 TXAIAudioMsgInfo 的结构定义如下：

| 属性       |  说明 | 
| --------       | --------   | 
| msg_id        |    消息 ID    |  
| peer_id        |   对方的 id    |  
| timestamp        |   消息事件    |  
| isreaded        |  是否已读    | 
| type       |   消息类型   | 
| detail      |   消息数据    | 

其中 type 从 1 到 8 分别为 小微 App 语音消息、小微 App 文本消息、*QQ 文本消息*、*QQ 语音消息*、*QQ 位置分享*、QQ 图片、QQ 视频、QQ 音乐。目前仅支持3、4、5。
其中 detail 为 json 格式字符串，对应的数据结构示例为：

| type       |  detail | 
| --------       | --------   | 
| 3        |    {"text":"消息文本"}    |  
| 4        |   {"localurl":"the location to audio file", "duration":100}    |  
| 5        |   {"longitude":0.0, "latitude":0.0, "description":"the location description"}    |  

#### 2. 指令接口
`TXAIAudioSDK.setMsgCommand`

`cmd`参数是`TXAIAudioMsgInfo.Control_TYPE`的值，
- 当 cmd=`Control_TYPE_QUERYALL` 时，SDK 会主动触发一次 AI_AUDIO_STATE_CHANGED 事件，上报当前最新的消息盒子信息。
- 当 cmd=`AI_AUDIO_STATE_MSG_PLAY_START` 时，会开始指定 msgid 的播放。
- 当 cmd=`AI_AUDIO_STATE_MSG_PLAY_STOP` 时，如果当前正在消息播放状态，SDK 会停止播放。

### QQ 电话
具体参照 [音视频通话接入指引](https://cloud.tencent.com/document/product/645/14233)。
