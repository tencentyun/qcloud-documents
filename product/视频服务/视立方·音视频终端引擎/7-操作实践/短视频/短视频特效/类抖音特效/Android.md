## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | -  | -  | &#10003;  | -  | -  | &#10003;  |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。



## 滤镜特效 

您可以为视频添加多种滤镜特效，我们目前支持11种滤镜特效，每种滤镜您也可以设置视频作用的起始时间和结束时间。如果同一个时间点设置了多种滤镜特效，SDK 会应用最后一种滤镜特效作为当前的滤镜特效。

### 设置方法

<dx-codeblock>
::: android java
/**
  * 设置滤镜特效开始时间
   * @param type      滤镜特效类型 
   * @param startTime 滤镜特效开始时间（ms）
      */
      public void startEffect(int type, long startTime);
      /**
  * 设置滤镜特效结束时间
  * @param type    滤镜特效类型
  * @param endTime 滤镜特效结束时间（ms）
*/
public void stopEffect(int type, long endTime);
:::
</dx-codeblock>

参数说明：@param type 是滤镜特效的类型，在常量 TXVideoEditConstants 中有定义：
``` 
public static final int TXEffectType_SOUL_OUT = 0;                    //滤镜效果1
public static final int TXEffectType_SPLIT_SCREEN = 1;                //滤镜效果2
public static final int TXEffectType_DARK_DRAEM = 2;                  //滤镜效果3
public static final int TXEffectType_ROCK_LIGHT = 3;                  //滤镜效果4
public static final int TXEffectType_WIN_SHADDOW = 4;                 //滤镜效果5
public static final int TXEffectType_GHOST_SHADDOW = 5;               //滤镜效果6
public static final int TXEffectType_PHANTOM_SHADDOW = 6;             //滤镜效果7
public static final int TXEffectType_GHOST = 7;                       //滤镜效果8
public static final int TXEffectType_LIGHTNING = 8;                   //滤镜效果9
public static final int TXEffectType_MIRROR = 9;                      //滤镜效果10
public static final int TXEffectType_ILLUSION = 10;                   //滤镜效果11
```
删除最后一个设置的滤镜特效：
``` 
public void deleteLastEffect();
```
删除所有设置的滤镜特效：
``` 
public void deleteAllEffect();
```

### Demo 示例

在1s - 2s之间应用第一种滤镜特效，在3s - 4s之间应用第2种滤镜特效，删除3s - 4s设置的滤镜特效。

```
//在1-2s之间应用第一种滤镜特效
mTXVideoEditer.startEffect(TXVideoEditConstants.TXEffectType_SOUL_OUT, 1000);
mTXVideoEditer.stopEffect(TXVideoEditConstants.TXEffectType_SOUL_OUT, 2000);
//在3-4s之间应用第2种滤镜特效
mTXVideoEditer.startEffect(TXVideoEditConstants.TXEffectType_SPLIT_SCREEN, 3000);
mTXVideoEditer.stopEffect(TXVideoEditConstants.TXEffectType_SPLIT_SCREEN, 4000);
//删除3-4s设置的滤镜特效
mTXVideoEditer.deleteLastEffect();
```
## 慢/快动作
您可以进行多段视频的慢速/快速播放。

### 设置方法

<dx-codeblock>
::: android java
public void setSpeedList(List speedList)；

//TXSpeed 的参数如下：
public final static class TXSpeed {
    public int speedLevel;                                    // 变速级别
    public long startTime;                                    // 开始时间
    public long endTime;                                      // 结束时间
}

// 目前支持变速速度的几种级别，在常量 TXVideoEditConstants 中有定义：
SPEED_LEVEL_SLOWEST    - 极慢
SPEED_LEVEL_SLOW       - 慢
SPEED_LEVEL_NORMAL     - 正常
SPEED_LEVEL_FAST       - 快
SPEED_LEVEL_FASTEST    - 极快
:::
</dx-codeblock>

### Demo 示例

<dx-codeblock>
::: android java
List<TXVideoEditConstants.TXSpeed> list = new ArrayList<>();
TXVideoEditConstants.TXSpeed speed1 = new TXVideoEditConstants.TXSpeed();
speed1.startTime = 0;                                               
speed1.endTime = 1000;
speed1.speedLevel = TXVideoEditConstants.SPEED_LEVEL_SLOW;                         // 慢速
list.add(speed1);

TXVideoEditConstants.TXSpeed speed2 = new TXVideoEditConstants.TXSpeed();
speed2.startTime = 1000;                                           
speed2.endTime = 2000;
speed2.speedLevel = TXVideoEditConstants.SPEED_LEVEL_SLOWEST;                      // 极慢速
list.add(speed2);

TXVideoEditConstants.TXSpeed speed3 = new TXVideoEditConstants.TXSpeed();
speed3.startTime = 2000;                                      
speed3.endTime = 3000;
speed3.speedLevel = TXVideoEditConstants.SPEED_LEVEL_SLOW;                          //慢速
list.add(speed3);

mTXVideoEditer.setSpeedList(list);
:::
</dx-codeblock>

## 倒放
您可以将视频画面倒序播放。通过调用 **setReverse(true)** 开启倒序播放，调用 **setReverse(false)** 停止倒序播放。
>!**setTXVideoReverseListener()** 老版本（SDK 4.5以前）首次监听需要手动调用，新版本不需要调用即可生效。

### Demo 示例

```
mTXVideoEditer.setTXVideoReverseListener(mTxVideoReverseListener);
mTXVideoEditer.setReverse(true);
```

## 重复视频片段
您可以设置重复播放一段视频画面，声音不会重复播放。目前 Android 只支持设置一段画面重复，重复三次。
如需取消之前设置的重复片段，调用 **setRepeatPlay(null)** 即可。

### 设置方法

<dx-codeblock>
::: android java
public void setRepeatPlay(List repeatList);

//TXRepeat 的参数如下：
public final static class TXRepeat {
    public long startTime;              //重复播放起始时间(ms)
    public long endTime;                //重复播放结束时间(ms)
    public int  repeatTimes;            //重复播放次数
}
:::
</dx-codeblock>

### Demo 示例

<dx-codeblock>
::: android java
long currentPts = mVideoProgressController.getCurrentTimeMs();

List repeatList = new ArrayList<>();
TXVideoEditConstants.TXRepeat repeat = new TXVideoEditConstants.TXRepeat();
repeat.startTime = currentPts;
repeat.endTime = currentPts + DEAULT_DURATION_MS;
repeat.repeatTimes = 3;  //目前只支持重复三次
repeatList.add(repeat);  //目前只支持重复一段时间
mTXVideoEditer.setRepeatPlay(repeatList);
:::
</dx-codeblock>
