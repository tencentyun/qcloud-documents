裁切器 **wj-clipper** 组件接收标准的 Track 数据，根据一定的规则生成 Clip 的缩略图，绘制到组件中。裁切器通常与 [**wj-player** 组件](https://cloud.tencent.com/document/product/1156/50158) 搭配使用，实现实时的裁切预览功能。

## 使用方式
1. 配置 JSON 文件：
```json
  {
    "usingComponents": {
      "wj-clipper": "plugin://myPlugin/wj-clipper"
    }
  }
```
2.  在 wxml 中引入组件：
```html
 <wj-clipper
      trackInfo="{{currentEditMedia}}"
      time="{{currentTime}}"
      settings="{{settings}}"
      bindthumbdone="onThumbDone"
      bindthumbtouchstart="onThumbTouchStart"
      bindthumbscroll="onThumbScroll"
      bindtimerollertouchstart="onTimeRollerTouchStart"
      bindtimerollertouchend="onTimeRollerTouchEnd"
      bindtimerollermove="onTimeRollerMove"
      bindhandlertouchstart="onHandlerTouchStart"
      bindended="onMediaEnded"
      bindclipped="onMediaClipped"/>
```

## 属性说明
| 属性名                   | 类型     | 默认值                  | 说明                                                         | 是否必填 |
| ------------------------ | -------- | ----------------------- | ------------------------------------------------------------ | -------- |
| trackInfo| Track    | null| Track 数据，详情请参见 [trackInfo 结构](#clipper_trackInfo) | 是|
| time                     | Number   | 0| 当前展示时间，控制时间轴的位置| 否|
| settings                 | Object   | 详情请参见 [settings 默认值](#clipper_settings) | 设置| 否|
| bindthumbdone            | Function | -| 缩略图绘制完成事件                                           | 否|
| bindthumbtouchstart      | Function | -| 缩略图 touch start 事件                                       | 否|
| bindthumbscroll          | Function | -| 缩略图滚动事件 <pre style="margin:0">{<br>time：当前时间轴指向的时间<br>}</pre>| 否|
| bindtimerollertouchstart | Function | -| 时间轴 touch start 事件| 否|
| bindtimerollertouchend   | Function | -| 时间轴 touch end 事件                                         | 否       |
| bindtimerollermove       | Function | -| 时间轴拖动事件（拖动左右手柄，时间轴跟随手柄的位置移动）<pre style="margin:0">{<br>time: 当前时间轴指向的时间<br>actionType: 事件触发类型（拖拽时间轴触发：moveRoller、拖拽手柄触发：moveHandler）<br>}</pre> | 否|
| bindhandlertouchstart    | Function | -| 左右手柄 touch start 事件| 否|
| bindhandlermove          | Function | -| 左右手柄拖动事件<pre style="margin:0">{<br>startTime：左手柄代表时间<br>endTime：右手柄代表时间<br>}</pre> | 否|
| bindclipped              | Function | -| 裁切发生事件 <pre style="margin:0">{<br>innerTrackInfo：裁切后的 Track 数据<br>time：当前时间轴指向时间<br>actionType：事件触发类型（拖拽缩略图触发 scrollThumb，拖拽手柄触发 moveHandler）<br>}</pre> | 否       |
| bindended                | Function | -| 时间轴播放到末尾（右手柄位置）事件| 否       |


###  trackInfo 结构<span id="clipper_trackInfo"></span>
clipper 组件接受的 trackInfo 数据相比于标准的 Track 多了几个属性，如下所示：
```
 {
   innerStartTime: Number, // 裁切区间开始时间
   innerEndTime: Number, // 裁切区间结束时间
   scrollStartTime: Number // 缩略图滚动时间（影响最终的 clipped 数据）
 }
```
###  settings 默认值<span id="clipper_settings"></span>
```
  {
    clipMaxDuration: 60, // 裁切时长限制（秒）
    mainColor: "rgba(255,88,76)" // 裁切器主题色
  }
```

## 组件实例属性
| 属性名            | 类型     | 参数            | 说明                                                         |
| ----------------- | -------- | --------------- | ------------------------------------------------------------ |
| getValidTrackData | Function |  Array&lt;Track&gt; | 根据 [trackInfo](#clipper_trackInfo) 的 innerStartTime、innerEndTime 值获取有效的 Track 数据 |
>?
- 裁切器涉及两个重要概念：缩略图展示区间、裁切区间。
  - **缩略图展示区间**：与 Clip 对象的 section 属性的值有关，start、end 属性决定单个 Clip 展示的缩略图时间区间。
  - **裁切区间**：与 trackInfo 的 innerStartTime、innerEndTime 字段的值有关，决定了整个 Track 裁切区间的起始时间。
- 通过 [获取组件实例](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/events.html) 的方式，可以调用组件暴露的`getValidTrackData`方法，将裁切区间外的无效数据过滤掉。
- 触发 clipped 事件的操作：左右手柄 touch-end、缩略图滚动停止。
- 触发 timerollermove 事件的操作：左右手柄 move、时间轴 move。

## 裁剪示例
通过两个示例解释下上述裁切器相关字段的含义，下例默认最大裁切区间都为60s。

### 示例1：单段裁切示例
![](https://main.qcloudimg.com/raw/3c40b1ceaacf4531cf70f6a4f12de377.png)
上述 Track 由一个 Clip 组成，时长为100s，自上而下状态分别对应：初始状态、向左拖动缩略图、向右拖动「左手柄」。
对应的数据结构变化如下：
```
// 初始状态
track={
    ……
    clips:[
      {
        ……
        section:{
          start:0,
          end:100
        }
      }
    ],
    innerStartTime:0,
    innerEndTime:60,
    scrollStartTime:0
  }
```
```
// 向左拖动缩略图、至20s的距离
track={
    ……
    clips:[
      {
        ……
        section:{
          start:0,
          end:100
        }
      }
    ],
    innerStartTime:20,
    innerEndTime:80,
    scrollStartTime:20
  }
```
```
// 向右拖动「左手柄」，至10s的距离
track={
    ……
    clips:[
      {
        ……
        section:{
          start:0,
          end:100
        }
      }
    ],
    innerStartTime:30,
    innerEndTime:80,
    scrollStartTime:20
  }
```
### 示例2：多段裁切示例
![](https://main.qcloudimg.com/raw/403467e0c4a33f975e6a5b82d87e446c.png)
上述 Track 由3个 Clip 组成，时长分别为30s、15s、55s，track 的总时长为100s。对应的 Track 数据如下所示：
```
track={
    ……
    clips:[
      {
        ……
        section:{
          start:0,
          end:30
        }
      },
      {
        ……
        section:{
          start:0,
          end:15
        }
      },
      {
        ……
        section:{
          start:0,
          end:55
        }
      },
    ],
    innerStartTime:20,
    innerEndTime:80,
    scrollStartTime:20
  }
```
