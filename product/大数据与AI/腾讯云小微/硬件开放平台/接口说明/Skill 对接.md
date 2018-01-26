该指引会对后台返回的结构化数据进行说明，有些场景 Skill 的结果需要本地进行相关处理，其中主要包括以下模块：

*   ** 本地 Skill**
*   ** 闹钟 / 定时 Skill**

收到 `onState` 后，如果 event 为 `AI_AUDIO_STATE_RESPONSE`，将会有结构化数据。

## TXAIAudioEventInfo 结构说明

| 属性 | 说明 |
| --- | --- |
| appName | 当前请求识别出的场景名称，例如 音乐、天气 |
| appID | 当前请求识别出的场景 id |
| textQuestion | 用户说的话 |
| textAnswer | 后台返回的 TTS 结果 |
| errorCode | 错误码，定义在 TXAIAudioDef.ERROR_CODE_DEF 中 |
| extendBufType | 结构化数据的类型，定义在 TXAIAudioDef.StructMsgType |
| extendBuf | 结构化数据的内容 |

## 本地 Skill

所谓本地 Skill 是指用户的语音请求，经过后台处理返回的语义分析结果需要由设备完成接管和处理的 Skill。在这种场景下，SDK 会将语义分析结果以结构化的数据进行返回 (extendBufType 的值为 `EXTEND_BUF_TYPE_LOCAL_SKILL`)，具体数据内容如下所示：

```
{
   "confirmStatus":"NONE",
   "intentName":"intent_name_value", // 意图名
   "dialogState":"COMPLETED",
   "slots":[
      {
         "confirmStatus":"NONE",
         "slot_name_1":"slot_value_1" // 槽位键值对 1
      },
      {
         "confirmStatus":"NONE",
         "slot_name_2":"slot_value_2" // 槽位键值对 2
      }
   ]
}
```

其中，`intentName` 表示在某个场景下用户的意图信息，`slots` 表示在这个意图下所包含的槽位信息。

下面将以导航场景为例，说明如何接入本地 Skill，假设用户说 “我想去北京”，此时后台会识别出导航场景，即 appName 的值为 “导航”，同时结构化数据的内容为：

```
{
   "confirmStatus":"NONE",
   "intentName":"导航到某地",
   "dialogState":"COMPLETED",
   "slots":[
      {
         "confirmStatus":"NONE",
         "目的地":"北京"
      }
   ]
}
```

如上所示，通过 appName、intentName 以及槽位信息，我们就可以知道用户现在想做什么，这种情况我们就可以调起导航 App 提供的相关接口进行下一步的处理。关于导航场景处理，您可以参考 `TXAILocationManager` 中的实现。

## 闹钟 / 定时 Skill

用户可以使用语音设置闹钟或定时播放。设置成功后，后台会返回一段 TTS 提示设置成功。同时会返回关于这个闹钟的结构化数据。您可以参照 `DeviceSkillAlarmManager.instance().addAlarmItem(TXAIAudioEventInfo eventInfo)` 中的逻辑对数据进行解析。

```
class ClockListBean {
    private List<ClockInfoBean> clock_info;
}

class ClockInfoBean {
    /**
     * clock_id : 598
     * clock_type : 0
     * event : 喝水
     * opt : 1
     * repeat_interval :
     * repeat_type : 0
     * service_type : 0
     * trig_time : 1502193827
     */
    private String clock_id;   // 闹钟 id
    private int clock_type;    // 闹钟类型，0：提醒，1：闹钟，2：循环闹钟
    private String event;      // 闹钟事件
    private int opt;           // 操作类型
    /**
     * 按天循环，则为天的间隔，比如，"1"：每隔一天，"2"：每隔 2 天
     * 按周循环，则为周几，比如，"1": 每周一，"1,2": 每周一，每周 2
     */
    private String repeat_interval; // 循环间隔
    private int repeat_type;   // 循环类型，1：按天循环（每天，每隔几天），2：按周循环（每周几）
    private int service_type;   // 是否为定时播放，0：非定时播放，1：定时播放
    private String trig_time;   // 闹钟触发的时间点，循环闹钟为最近一次触发时间点
}
```

解析完闹钟数据后，需要将闹钟存入到本地数据库，并根据闹钟数据在设备上设置一个闹钟用于触发这个闹钟，您可以参考 `DeviceSkillAlarmManager` 和 `SkillAlarmManager` 中的相关逻辑。当一个闹钟到达最近的一次触发时间时，您需要调用 `TXAIAudioSDK.fireClockEvent(clockId)` 通知后台触发该闹钟，后台会下发相应的资源 (TTS 和其他播放资源) 到设备。

```
/**
 * 触发后台闹钟
 *
 * @param clockID 闹钟 key
 * @return 0 表示成功
 */
public int fireClockEvent(String clockID);
```
