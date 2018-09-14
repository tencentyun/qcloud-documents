本地 Skill 是指用户的语音请求，经过后台处理返回的语义分析结果需要由设备进行完全接管和处理的 Skill。在这种场景下，SDK 会将语义分析结果以结构化的数据进行返回。本地 Skill 和普通的 Skill 的区别往往在于：普通 Skill 在用户进行一次输入后直接返回了播放和展示的资源，而本地 Skill 需要自行解析返回的意图，并操作设备进行对应的反应。本地 Skill 可用于闹钟、拍照、视频、导航等。

## 本地 Skill 接口
### Linux
Linux 的头文件为 `OuterSkillMgr.h`，其中定义了 `tcx_xwei_outer_skill_callback` 结构：

```
struct tcx_xwei_outer_skill_callback
{
    // 当内部的几个基础 skill 无法处理，将回调它，应用层如果可以处理这个响应，返回 true，将收到 send_txca_response
    bool (*start_outer_skill)(int session_id, const char *skill_name, const char *skill_id);
    // 回调 cRsp，由外面进行处理，例如：闹钟 skill
    bool (*send_txca_response)(int session_id, TXCA_PARAM_RESPONSE *cRsp);
};

// 外部处理响应的回调
SDK_API extern tcx_xwei_outer_skill_callback outer_skill_callback;
```

`outer_skill_callback` 中有两个回调，其中`start_outer_skill`会将 Skill 的信息进行回调，由实现者判断这个 Skill 外面能否处理，如果可以处理，返回`true`，否则控制层内部会有一个通用的处理——如果有资源则进行处理。

当`outer_skill_callback`返回`true`以后，会收到`send_txca_response`回调，这里会把整个响应（包含意图等信息）都回调给外面处理。如果处理失败，返回`false`，控制层内部会有一个通用的处理——如果有资源则进行处理。
```
	#include "OuterSkillMgr.h"
	
	bool start_outer_skill(int sessionId, const char *skillName, const char *skillId) {
		// 通过 skillName 和 skillId 判断能否处理这个 Skill 的响应
		return true;
	}
	
	bool send_txca_response(int sessionId, TXCA_PARAM_RESPONSE *pRsp) {
		return true;
	}
	
   outer_skill_callback.start_outer_skill = start_outer_skill;
   outer_skill_callback.send_txca_response = send_txca_response;
```
    
### Android
Android 的 jni 实现在 `XWeiOuterSkill_jni.cpp` 中，Java  层的接口在 `XWeiOuterSkill.java` 中。
```
XWeiOuterSkill.java

public void registerSkillIdOrSkillName(String skillIdOrName, OuterSkillHandler handler);
public void unRegisterSkillIdOrSkillName(String skillIdOrName);

public interface OuterSkillHandler {
    boolean handleResponse(int sessionId, XWResponseInfo responseInfo);
}

```

如果开发者实现了某个 Skill 的功能，需要调用接口`registerSkillIdOrSkillName(String skillIdOrName, OuterSkillHandler handler)` 进行注册，对于同时有 SkillId 和 SkillName 的 Skill，我们建议优先使用 SkillId 来处理，在收到相应 Skill 的响应后，`OuterSkillHandler. handleResponse` 将被回调。

## 闹钟/提醒 Skill 接入
用户可以使用语音设置闹钟或提醒。设置成功后，后台会返回一段 TTS 提示设置成功。同时会返回关于这个闹钟的结构化数据。之后由客户端自行响起闹钟。

### 结构说明
闹钟的结构化数据存在于 XWResponseInfo.responseData 字段中，是一个 json 格式的数据。结构如下：
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

解析完闹钟数据后，请注意每个闹钟数据中的 *opt* 字段，您需要根据该字段不同的值进行相应的处理：
1. 新增：将该闹钟存入到本地数据库，并根据闹钟数据在设备上设置一个闹钟用于触发这个闹钟；
2. 更新：将该闹钟的更新存入到本地数据库中，并在设备上取消该闹钟重新进行设置；
3. 删除：将闹钟从本地数据库中删除，并在设备上取消该闹钟。

上述相关逻辑，您可以参考 Demo 中 `DeviceSkillAlarmManager.java` 和 `SkillAlarmManager.java` 中的相关逻辑。当一个闹钟到达最近的一次触发时间时，您需要根据闹钟数据中设置的事件提醒用户，具体提醒交互方式由您自行处理。需要注意的是，由于 Android 设备有视频通话功能，当设备处于视频通话状态时，您需要延迟触发该闹钟。除此语音操作方式，用户还会通过小微 App 操作闹钟，您也会收到相应操作对应的结构化数据，处理方式与语音操作拿到的数据一样。

此外，在有屏设备上，用户还需要屏幕手动操作闹钟列表，为此我们提供了一些通用接口，这些接口的使用您可以参考`EditAlarmActivity.java`和`AlarmEventActivity.java`：

### 语音操作闹钟/提醒
1. 新增闹钟/提醒
 - 设定准确时间的闹钟/提醒，如：“明天早上八点提醒我开会”；
 - 设定泛时间的闹钟/提醒，如：“明天八点提醒我开会，此时会有二轮问答确认上午还是下午”；
 - 设定倒计时类的闹钟/提醒，如：“一分钟后提醒我喝水”；
 - 设定循环闹钟/提醒，如：“每天早上八点提醒我起床”。

2. 查询闹钟/提醒
  - 当前闹钟列表只有一个提醒，查询“我的闹钟/提醒”时，返回对应的闹钟/提醒时间；
  - 当前闹钟列表有多个提醒，查询“我的闹钟/提醒”时，返回【您共有X条提醒】+【时间1+事件名1】+【时间2+事件名2】+【时间X+事件名X】按顺序播报；
  - 当前闹钟列表中没有提醒，查询“我的闹钟/提醒”时，返回【您当前没有设置提醒】。

3. 删除闹钟/提醒
 - 当前闹钟列表只有一个提醒，删除“我的闹钟/提醒”时，直接删除，返回【删除提醒成功】；
 - 当前闹钟列表有多个提醒，删除“我的闹钟/提醒”时，返回【您共有X条提醒】+【时间1+事件名1】+【时间2+事件名2】+【时间X+事件名X】+【请问您要删除哪一个】，回答：【删除第X个闹钟】即可删除闹钟；
 - 当前闹钟列表中没有提醒，删除“我的闹钟/提醒”时，返回【您当前没有设置提醒】。

### Android SDK 闹钟增删改查接口
Android 的接口在`XWSDK.java`中。
```
/**
 * 获取提醒列表
 *
 * @param listener 响应回调接口 定义请参考{@link XWSDK.GetAlarmListRspListener}
 * @return 接口调用结果，请参考{@link XWCommonDef.ErrorCode}
 */
public int getDeviceAlarmList(GetAlarmListRspListener listener);

/**
 * 闹钟/提醒操作类型定义
 */
public interface AlarmOptType {
    /**
     * 新增闹钟
     */
    int ALARM_OPT_TYPE_ADD    = 1;
    /**
     * 更新闹钟
     */
    int ALARM_OPT_TYPE_UPDATE = 2;
    /**
     * 删除闹钟
     */
    int ALARM_OPT_TYPE_DELETE = 3;
}
    
/**
 * 设置闹钟或提醒
 *
 * @param opType       操作类型 1.增加 2.修改 3.删除 {@link XWCommonDef.AlarmOptType}
 * @param strAlarmJson 操作对应的json结构
 * @param listener     设置结果的回调通知 定义请参考{@link XWSDK.SetAlarmRspListener}
 * @return 接口调用返回结果 请参考{@link XWCommonDef.ErrorCode}
 */
public int setDeviceAlarmInfo(int opType, String strAlarmJson, SetAlarmRspListener listener);
```

### Linux SDK 闹钟增删改查接口
Linux 的头文件为 `TXCAudioRemind.h`。
```
/**
 * 获取闹钟提醒列表
 * @param voice_id 返回的请求id
 * @param callback 闹钟提醒结果回调
 */
SDK_API int txca_get_alarm_list(char *voice_id, on_get_alarm_list callback);

/**
 * 设置/更新闹钟提醒
 * @param voice_id 返回的请求id
 * @param optType 操作类型 1.增加 2.修改 3.删除 4.修改闹钟类型
 * @param alarm_info_json 操作对应的json结构
 * @param notify 结果返回
 */
SDK_API int txca_set_alarm_info(char *voice_id, int optType, const char *alarm_info_json, on_set_alarm_result notify);
```

###  业务逻辑示例
闹钟作为一个本地 Skill，当控制层将响应交给应用层的时候，需要做以下这些事情：
* **播放设置成功的 TTS。**
* **为闹钟计时。**
* **到了对应的时间，需要响起闹钟，显示 UI。**
* **播放闹钟的时候上报播放状态。**

在 AndroidDemo 中，*ControlService.java* 中注册了闹钟 Skill 的处理回调，收到响应后，交给了 *DeviceSkillAlarmManager.java* 设置闹钟计时，然后请求音频焦点，播放了设置成功的 TTS。闹钟时间到后，会打开 *AlarmActivity.java*。

在 Activity 中，会请求音频焦点，请求事件 TTS 并播放闹钟铃声。用户关闭界面的时候会释放焦点停止播放。在这里需要特别注意，用户在播放闹钟过程中，可能会用语音操作“停止播放”等，这时候我们会把“停止播放”的这个通用控制回调给当前在播放的 Skill。所以为了能正确的将这个控制指令交给闹钟 Skill，我们需要在播放闹钟的时候进行播放状态上报，告诉小微当前在播放闹钟。

```
XWPlayStateInfo stateInfo = new XWPlayStateInfo();
stateInfo.appInfo = new XWAppInfo();
stateInfo.appInfo.ID = Constants.SkillIdDef.SKILL_ID_ALARM;
stateInfo.appInfo.name = Constants.SKILL_NAME.SKILL_NAME_ALARM;
stateInfo.state = XWCommonDef.PlayState.START;
XWSDK.getInstance().reportPlayState(stateInfo);
```

## 定时播放 Skill

定时播放 Skill 与闹钟/提醒 Skill 基本是一致的，唯一的区别是定时播放 Skill 到了用户设置的最近一次触发时间点后，您需要调用 `XWSDK(). getTimingSkillResource()` 接口请求后台下发用户之前设置的播放资源。`getTimingSkillResource `接口定义说明如下所示：

```
/**
 * 拉取定时播放任务资源
 *
 * @param strAlarmId 定时
 * @param listener   响应回调
 * @return 接口调用返回结果 请参考{@link XWCommonDef.ErrorCode}
 */
public int getTimingSkillResource(String strAlarmId, RequestListener listener);

```

Linux SDK 中相同功能的接口定义如下所示：

```
/**
 * 拉取定时Skill的播放资源
 * @param voice_id 返回的请求id
 * @param clock_id 定时Skill任务的id
 */
SDK_API int txca_get_timing_skill_resources(char *voice_id, const char *alarm_id);

```

## 通用本地 Skill 接入

本地 Skill 的意图信息一般都是如下格式：

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

### 导航

导航场景目前是作为一种本地 Skill 来处理。在导航场景中，存在很多不同的用户意图，根据不同的用户意图进行相应的处理，下面的内容是总结了在导航场景不同用户意图下`XWResponseInfo.responseData `结构化数据的内容：

#### 进入导航

```
{  
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"打开地图"
}
```

#### 退出导航

```
{  
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"退出导航"
}
```

#### 定位当前地点

```
{  
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"当前位置查询"
}
```

#### 导航到家

```
{  
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"导航回家"
}
```

#### 导航到公司

```
{  
   "confirmStatus":"",
   "dialogState":"COMPLETE",
   "intentName":"导航去公司"
}

```

#### 前面路线查看

```
{  
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"前方怎么走(前提在导航场景下)"
}

```

#### 导航到某地

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

#### 中途更新路线

```
{  
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"中途更新路线"
}
```

#### 导航到某类型地点-周边导航

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

#### 放大地图

```
{  
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"放大地图"
}
```

#### 缩小地图

```
{  
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"缩小地图"
}
```

#### 路况打开

```
{  
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"路况打开"
}
```

#### 路况关闭

```
{  
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"路况关闭"
}
```

#### 视图切换

```
{  
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"视图切换"
}
```

#### 切换到2D视图

```
{  
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"切换到2d视图"
}
```

#### 切换到3D视图

```
{  
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"切换为3d视图"
}
```

#### 视图切换-正北朝上

```

{  
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"视图切换 -  正北朝上"
}
```

#### 视图切换-车头超前

```
{  
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"视图切换 - 车头朝前"
}
```

#### 路况查询

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

#### 离终点有多远

```
{  
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"离终点有多远"
}
```

#### 查询到终点的剩余时间

```
{  
   "confirmStatus":"NONE",
   "dialogState":"COMPLETE",
   "intentName":"查询到达终点的剩余时间"
}
```

#### 前方多少公里怎么走

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

#### 通用控制

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
