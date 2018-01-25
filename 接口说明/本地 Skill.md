该指引会对后台返回的结构化数据进行说明，有些场景 Skill 的结果需要本地进行相关处理，其中主要包括以下模块：

*   **本地 Skill**
*   **闹钟/提醒 Skill**
*   **定时播放 Skill**

收到`onState`后，如果 event 为`AI_AUDIO_STATE_RESPONSE`，将会有结构化数据。

## TXAIAudioEventInfo 结构说明

| 属性 | 说明 |
| --- | --- |
| appName | 当前请求识别出的场景名称，例如 音乐、天气 |
| appID | 当前请求识别出的场景 id |
| textQuestion | 用户说的话 |
| textAnswer | 后台返回的 TTS 结果 |
| errorCode | 错误码，定义在TXAIAudioDef.ERROR_CODE_DEF中 |
| extendBufType | 结构化数据的类型，定义在TXAIAudioDef.StructMsgType |
| extendBuf | 结构化数据的内容 |

## 本地 Skill

所谓本地 Skill 是指用户的语音请求，经过后台处理返回的语义分析结果需要由设备完成接管和处理的 Skill。在这种场景下，SDK 会将语义分析结果以结构化的数据进行返回( extendBufType 的值为`EXTEND_BUF_TYPE_LOCAL_SKILL`)，具体数据内容如下所示：

```
{
   "confirmStatus":"NONE",
   "intentName":"intent_name_value", // 意图名
   "dialogState":"COMPLETED",
   "slots":[
      {
         "confirmStatus":"NONE",
         "slot_name_1":"slot_value_1" // 槽位键值对1
      },
      {
         "confirmStatus":"NONE",
         "slot_name_2":"slot_value_2" // 槽位键值对2
      }
   ]
}
```

其中，`intentName`表示在某个场景下用户的意图信息，`slots`表示在这个意图下所包含的槽位信息。

下面将以导航场景为例，说明如何接入本地 Skill，假设用户说“我想去北京”，此时后台会识别出导航场景，即 appName的值为“导航”，同时结构化数据的内容为：

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

如上所示，通过 appName、intentName 以及槽位信息，我们就可以知道用户现在想做什么，这种情况我们就可以调起导航 App 提供的相关接口进行下一步的处理。关于导航场景处理，您可以参考`TXAILocationManager`中的实现。

## 闹钟/提醒 Skill

用户可以使用语音设置闹钟或提醒。设置成功后，后台会返回一段 TTS 提示设置成功。同时会返回关于这个闹钟的结构化数据。您可以参照`DeviceSkillAlarmManager.instance().operationAlarmSkill(TXAIAudioEventInfo eventInfo)`中的逻辑对数据进行解析。

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
    private String clock_id;   // 闹钟id
    private int clock_type;    // 闹钟类型，0：提醒，1：闹钟，2：循环闹钟
    private String event;      // 闹钟事件
    private int opt;           // 操作类型，1：新增，2：更新，3：删除
    /**
     * 按天循环，则为天的间隔，比如，"1"：每隔一天，"2"：每隔2天
     * 按周循环，则为周几，比如，"1":每周一，"1,2":每周一，每周二
     */
    private String repeat_interval; // 循环间隔
    private int repeat_type;   // 循环类型，1：按天循环（每天，每隔几天），2：按周循环（每周几）
    private int service_type;   // 是否为定时播放，0：非定时播放，1：定时播放
    private String trig_time;   // 闹钟触发的时间点，循环闹钟为最近一次触发时间点
}
```

解析完闹钟数据后，请注意每个闹钟数据中的`opt`字段，您需要根据该字段不同的值进行相应的处理：

1.  新增：将该闹钟存入到本地数据库，并根据闹钟数据在设备上设置一个闹钟用于触发这个闹钟；
2.  更新：将该闹钟的更新存入到本地数据库中，并在设备上取消该闹钟重新进行设置；
3.  删除：将闹钟从本地数据库中删除，并在设备上取消该闹钟。

上述相关逻辑，您可以参考 Demo 中`DeviceSkillAlarmManager.java`和`SkillAlarmManager.java`中的相关逻辑。当一个闹钟到达最近的一次触发时间时，您需要根据闹钟数据中设置的事件提醒用户，具体提醒交互方式由您自行处理。需要注意的是，由于 Android 设备有视频通话功能，当设备处于视频通话状态时，您需要延迟触发该闹钟，通过调用接口`TXDeviceSDK.isServiceRunning(context, AVService.class.getName())`您可以判断当前是否处于视频通话状态。除此语音操作方式，用户还会通过小微 App 操作闹钟，您也会从`onState`接口中收到相应操作对应的结构化数据，处理方式与语音操作拿到的数据一样。

此外，在有屏设备上，用户还需要屏幕手动操作闹钟列表，为此我们提供了一些通用接口，这些接口的使用您可以参考`EditAlarmActivity.java`和`AlarmEventActivity.java`：

### 语音操作闹钟/提醒

1.  新增闹钟/提醒：设定准确时间的闹钟/提醒，如：“明天早上八点提醒我开会”；设定泛时间的闹钟/提醒，如：“明天八点提醒我开会，此时会有二轮问答确认上午还是下午”；设定倒计时类的闹钟/提醒，如：“一分钟后提醒我喝水”；设定循环闹钟/提醒，如：“每天早上八点提醒我起床”

2.  查询闹钟/提醒：当前闹钟列表只有一个提醒，查询“我的闹钟/提醒”时，返回对应的闹钟/提醒时间；当前闹钟列表有多个提醒，查询“我的闹钟/提醒”时，返回【您共有X条提醒】+【时间1+事件名1】+【时间2+事件名2】+【时间X+事件名X】按顺序播报；当前闹钟列表中没有提醒，查询“我的闹钟/提醒”时，返回【您当前没有设置提醒】

3.  删除闹钟/提醒：当前闹钟列表只有一个提醒，删除“我的闹钟/提醒”时，直接删除，返回【删除提醒成功】；当前闹钟列表有多个提醒，删除“我的闹钟/提醒”时，返回【您共有X条提醒】+【时间1+事件名1】+【时间2+事件名2】+【时间X+事件名X】+【请问您要删除哪一个】，回答：【删除第X个闹钟】即可删除闹钟；当前闹钟列表中没有提醒，删除“我的闹钟/提醒”时，返回【您当前没有设置提醒】

### Android SDK 闹钟增删改查接口

```
/**
 * 拉取设备闹钟/定时Skill任务列表
 * @param listener 响应监听器
 * @return 0 表示执行成功，返回码参考 {@link com.tencent.device.TXCommonDef.ErrorCode}
 */
public int getDeviceAlarmList(DeviceResponseListener listener)

/**
 * 新增设备闹钟
 *
 * @param strAlarmJson 一个闹钟项的JSON表示
 * @param listener 响应回调
 * @return 0 表示执行成功，返回码参考 {@link com.tencent.device.TXCommonDef.ErrorCode}
 */
public int addDeviceAlarm(String strAlarmJson, DeviceResponseListener listener)

/**
 * 更新设备闹钟
 *
 * @param strAlarmJson 一个闹钟项的JSON表示
 * @param listener 响应回调
 * @return 0 表示执行成功，返回码参考 {@link com.tencent.device.TXCommonDef.ErrorCode}
 */
public int updateDeviceAlarm(String strAlarmJson, DeviceResponseListener listener)

/**
 * 删除设备闹钟
 *
 * @param strAlarmJson 一个闹钟项的JSON表示
 * @param listener 响应回调
 * @return 0 表示执行成功，返回码参考 {@link com.tencent.device.TXCommonDef.ErrorCode}
 */
public int deleteDeviceAlarm(String strAlarmJson, DeviceResponseListener listener)
```

### Linux SDK 闹钟增删改查接口

```
/**
 * 接口说明：拉取闹钟/定时Skill任务列表
 * ret: 0成功，非0失败
 */
SDK_API int tx_ai_audio_get_device_alarm_list(char* voice_id);

/**
 * 接口说明：新增/修改闹钟
 * opt_type: 操作类型 请参考tx_ai_audio_alarm_opt_type中的取值
 * clock_info_json: 闹钟信息
 * ret: 0成功 非0失败
 */
SDK_API int tx_ai_audio_update_device_alarm(char* voice_id, int opt_type, const char* alarm_info_json);
```

## 定时播放 Skill

定时播放 Skill 与闹钟/提醒 Skill 基本是一致的，唯一的区别是定时播放 Skill 到了用户设置的最近一次触发时间点后，您需要调用`TXAIAudioSDK.getInstance().triggerTimingSkill()`接口请求后台下发用户之前设置的播放资源，相应的播放资源将通过`onState`回调出来，请参考[标准UI模板](/wiki/#AccessFlow_ui_template_impl)中的说明。`TXAIAudioSDK.getInstance().triggerTimingSkill()`接口定义说明如下所示：

```
/**
 * 请求后台下发定时Skill任务播放资源
 *
 * @param clockId 定时Skill任务标识id，不能为空
 * @return 0 表示执行成功，返回码参考 {@link com.tencent.device.TXCommonDef.ErrorCode}
 */
public int triggerTimingSkill(String clockId, DeviceResponseListener listener)
```

Linux SDK 中相同功能的接口定义如下所示：

```
/**
 * 接口说明: 触发定时Skill任务，请求后台下发播放资源
 * clock_id: 定时Skill任务的标识id
 * ret: 0成功 非0失败
 */
SDK_API int tx_ai_audio_trigger_timing_skill(char* voice_id, const char* clock_id);
```

## 本地Skill——导航场景

导航场景目前就是作为一种本地 Skill 处理，所以需要厂商处理相关的业务逻辑：

(1) 当进入或退出导航，需要通过`TXAIAudioSDK.getInstance().setLocalAppEvent()`接口通知 SDK 当前设备当前所处的状态

```
/**
 * 设置当前App的状态，例如：进入导航模式，退出导航模式
 * @param event 请参考{@link com.tencent.device.info.TXAIAudioDef.LocalAppEvent}
 * @return 0 表示执行成功
 */
public int setLocalAppEvent(int event)
```

(2) 在导航场景中，存在很多不同的用户意图，根据不同的用户意图进行相应的处理，下面的内容是总结了在导航场景不同用户意图下`extendBuf`结构化数据的内容：

### 进入导航

```
{
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"打开地图"
}
```

### 退出导航

```
{
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"退出导航"
}
```

### 定位当前地点

```
{
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"当前位置查询"
}
```

### 导航到家

```
{
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"导航回家"
}
```

### 导航到公司

```
{
   "confirmStatus":"",
   "dialogState":"COMPLETE",
   "intentName":"导航去公司"
}
```

### 前面路线查看

```
{
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"前方怎么走(前提在导航场景下)"
}
```

### 导航到某地

```
{
   "confirmStatus":"",
   "dialogState":"COMPLETE",
   "intentName":"导航到某地",
   "slots":[
      {
         "confirmStatus":"NONE",
         "key":"route_highway",
         "route_highway":"",
         "value":""
      },
      {
         "confirmStatus":"NONE",
         "key":"route_nojam",
         "route_nojam":"",
         "value":""
      },
      {
         "confirmStatus":"NONE",
         "key":"route_savemoney",
         "route_savemoney":"",
         "value":""
      },
      {
         "confirmStatus":"NONE",
         "key":"to_loc",
         "to_loc":"北京",
         "value":"北京"
      },
      {
         "confirmStatus":"NONE",
         "key":"to_loc_norm",
         "to_loc_norm":"北京",
         "value":"北京"
      }
   ]
}
```

### 中途更新路线

```
{
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"中途更新路线"
}
```

### 导航到某类型地点-周边导航

```
{
   "confirmStatus":"",
   "dialogState":"COMPLETE",
   "intentName":"周边导航",
   "slots":[
      {
         "confirmStatus":"NONE",
         "key":"nearby_type",
         "nearby_type":"星巴克",
         "value":"星巴克"
      },
      {
         "confirmStatus":"NONE",
         "key":"nearby_type_norm",
         "nearby_type_norm":"星巴克",
         "value":"星巴克"
      },
      {
         "confirmStatus":"NONE",
         "key":"to_loc",
         "to_loc":"",
         "value":""
      }
   ]
}
```

### 放大地图

```
{
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"放大地图"
}
```

### 缩小地图

```
{
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"缩小地图"
}
```

### 路况打开

```
{
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"路况打开"
}
```

### 路况关闭

```
{
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"路况关闭"
}
```

### 视图切换

```
{
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"视图切换"
}
```

### 切换到2D视图
```
{
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"切换到2d视图"
}
```

### 切换到3D视图
```
{
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"切换为3d视图"
}
```

### 视图切换-正北朝上

```

{
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"视图切换 -  正北朝上"
}
```

### 视图切换-车头超前

```
{
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"视图切换 - 车头朝前"
}
```

### 限号查询

```
// 暂不支持
```

### 路况查询

```
{
   "confirmStatus":"",
   "dialogState":"COMPLETE",
   "intentName":"路况查询",
   "slots":[
      {
         "confirmStatus":"NONE",
         "key":"traffic_loc",
         "traffic_loc":"",
         "value":""
      }
   ]
}
```

### 离终点有多远
```
{
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"离终点有多远"
}
```

### 查询到终点的剩余时间

```
{
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"查询到达终点的剩余时间"
}
```

### 前方多少公里怎么走

```
{
   "confirmStatus":"",
   "dialogState":"COMPLETE",
   "intentName":"前方多少公里怎么走",
   "slots":[
      {
         "confirmStatus":"NONE",
         "key":"数字",
         "value":"五",
         "数字":"五"
      },
      {
         "confirmStatus":"NONE",
         "key":"数字_norm",
         "value":"raw_weight",
         "数字_norm":"raw_weight"
      }
   ]
}
```

### 通用控制

```
{
   "intentName":"通用控制",
   "slots":[
      {
         "key":"id",
         "value":"700145"
      },
      {
         "key":"value",
         "value":"1"
      }
   ]
}
```

当 id 为700006时，表示下一页；为700005时，表示上一页；为700142时，表示确定，为700143时，表示取消，为700144时，表示返回；为700145时，表示选项确认，此时的 value 表示列表中的第几个。
