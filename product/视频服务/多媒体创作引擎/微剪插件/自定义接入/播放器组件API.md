## 播放器：wj-player

`wj-player` 是支持微剪运行的核心组件，它是由轨道数据驱动运行的播放器，并内置了一些常用功能。

>?
>- v1.4.0后新增功能：
	- 贴纸，详情请参见 [自定义贴纸和文字](https://cloud.tencent.com/document/product/1156/48610)。
	- 文字和贴纸内置编辑控件，详情请参见 [编辑控件](#Plugin)。
>- v1.5.0后新增功能：
转场和动效，详情请参见 [转场和动效](https://cloud.tencent.com/document/product/1156/48610)。
>- v1.6.0之后支持模板。
 
### 使用方式
1. 配置 JSON 文件：
```json
  {
      "usingComponents": {
        "wj-player": "plugin://myPlugin/wj-player"
      }
  }
```
2. 引入组件：
```html
<wj-player
      class="player" 
      id="my-player" 
      mode="default"
      enablePauseIcon="{{showPauseIcon}}"
      bindready="onPreviewerReady"
      binddataupdated="handleDataUpdated"
      allowSetVolumn="{{true}}"
      bindswipeToRight="swipeToRight"
      bindswipeToLeft="swipeToLeft"
      bindtimeupdate="timeupdate"
      bindended="playerEnd">
</wj-player>
```

### 属性说明

| 属性名               | 类型     | 默认值     | 说明       | 必填 |
| -------------------- | -------- | ---------------------- | ---------------------- | ---- |
| containerStyleConfig | Object   | `{height: 1334, width: 750}`                                 | 播放器的尺寸                                                 | 否   |
| mode                 | String   | default    | <li />default：video 模式<li />offscreen：decoder offscreen 模式（导出模式），推荐直接使用 `wj-export` 组件 | 否   |
| allowSetVolumn       | Boolean  | false      | 是否需要调整视频原声音量                                     | 否   |
| enableTapPause       | Boolean  | false      | 是否启用点击暂停                                             | 否   |
| enablePauseIcon      | Boolean  | true       | 是否显示暂停按钮                                             | 否   |
| enableClipEdit      | Boolean  | true       | 是否启用编辑控件，编辑控件请参见 [编辑控件](#Plugin)                        | 否   |
| preloadFilter        | Boolean  | true       | 是否启用滤镜预加载                                           | 否   |
| preloadFilterKeys    | Array    | ['key1', 'key2']                                             | 需要提前加载的滤镜                                           | 否   |
| filters(1.7.0版本废弃，使用initPlugin方法统一注入)     | Array    | [{<br />key: 'lujing',<br />name: '滤镜'<br />src: 'wxfile://xxxxx'<br />}] | 定制化 effect 列表                                           | 否   |
| effects(1.7.0版本废弃，使用initPlugin方法统一注入)              | Array    | [{<br />name: EffectName,<br />fragment: Shader 代码字符串<br />}] | 定制化 shader 列表                                           | 否   |
| status               | String   | playing    | 初始播放状态                                                 | 否   |
| bindready            | Function | -                 | 播放器初始化完成回调                                         | 否   |
| bindplay             | Function | -                 | 播放器开始播放                                               | 否   |
| bindpaused           | Function | -                 | 播放器暂停回调                                               | 否   |
| bindwaiting          | Function | -                 | 播放器加载中的回调                                           | 否   |
| bindloadcomplete     | Function | -                 | 播放器所有 Clip 加载完毕时触发                               | 否   |
| binddataupdated      | Function | -                 | 播放器 updateData 完成时触发<br />e.detail = [Tracks]        | 否   |
| bindtimeupdate       | Function | -                 | 播放进度变化时触发<br />e.detail = time                      | 否   |
| bindtapped           | Function | -                 | 播放器点击                                                   | 否   |
| bindended            | Function | -                 | 播放完成                                                     | 否   |
| bindtexttouchstart   | Function | -                 | 文字开始触摸(v1.4.0后废弃)                                   | 否   |
| bindtexttouchend     | Function | -                 | 文字触摸结束(v1.4.0后废弃)                                   | 否   |
| bindtexttouchmove    | Function | -                 | 文字移动(v1.4.0后废弃)                                       | 否   |
| bindclipedit    | Function | 请参见 [编辑控件](#Plugin)                                                     |clip 位移、旋转、缩放                                   | 否   |
| bindclipoperation   | Function | 请参见 [编辑控件](#Plugin)                                                     |编辑控件按钮点击                                 | 否   |
| bindmaskedit | Function | |蒙版参数变化回调，请参见 [蒙版控件](#Mask)|否|

### 方法说明

| 方法名        | 参数   | 返回值       | 说明                                     |
| ------------- | ------ | ------------ | ---------------------------------------- |
| play          | -      | -            | 播放                                     |
| pause         | -      | -            | 暂停                                     |
| seek          | number | -            | 跳转到某一时间播放                       |
| stop          | -      | -            | 停止                                     |
| reset          | -      | -           | 播放器reset                                     |
| updateData    | Object | -            | 更新播放轨道，更新播放器内数据           |
| types         | -      | player.Types | 返回可供操作 Tracks 的方法               |
| getFilters(1.7.0废弃)    | -      | Array        | 获取所有滤镜列表（默认返回内置滤镜列表） |
| getEffects(1.7.0废弃)    | -      | Array        | 获取所有特效列表（默认返回内置特效列表） |
| getDuration   | -      | Number       | 获取视频总时长                           |
| getTracks     | -      | Array        | 获取当前轨道                             |
| getPlayStatus | -      | String       | 获取当前播放状态                         |
| hideClipControl| -      | -           | 强制隐藏所有的编辑控件                         |
| preloadSticker| String（spritesheet 地址或 key 值）| -       | 异步方法，预加载贴纸       |
| preloadTemplate| String（模板 key 值）| -       | 异步方法，预加载模板       |
| downloadEffect| String（特效 key 值）| -       | 异步方法，预下载 alpha 类型特效的资源       |
| setCoverImage| -| -       | 异步方法，设置封面（seek 到您需要截取封面的位置再调用此方法）       |
| getCoverImage| -| Object (path, width, height)       | 获取封面信息，如果没有先 setCoverImage，则自动获取第一帧的画面       |
| showMaskControl | - | - | 播放器进入蒙版编辑状态，请参见 [蒙版控件](#Mask) |
| hideMaskControl | - | - | 播放器关闭蒙版编辑状态，请参见 [蒙版控件](#Mask) |

播放器围绕 Tracks 和 Clips 进行视频渲染， 前文数据结构详细介绍了 Tracks 和 Clips 直接的关系。接下来，我们一起来看一下如何对播放器进行渲染。

>?
>- 定制滤镜目前只支持 LUT 图滤镜，由于小程序下载文件的限制，LUT 图需要先 downloadFile 到本地。
>- 定制特效需要传入特效的片元着色器，详情见 [自定义特效和滤镜](https://cloud.tencent.com/document/product/1156/48621)。
>- v1.4.0之后支持贴纸渲染，贴纸和文字的位移和缩放，请参见 [自定义贴纸和文字](https://cloud.tencent.com/document/product/1156/49440) 和 [编辑控件](#Plugin)。



[](id:Plugin)
### 编辑控件
微剪播放器内置了编辑控件支持贴纸、文字等元素的位移、缩放和旋转。
- 贴纸和文字类型的 Clip 内置编辑控件的支持，单击即可激活。
- 控件有四个按钮：删除（左上角），修改（右上角），缩放旋转（右下角）和编辑时间段（左下角）。其中缩放旋转为播放器内部完全实现的功能，其余三个按钮只提供回调函数，供开发者自行定制功能交互。

<img src="https://imgcache.qq.com/operation/dianshi/other/WechatIMG68.44d03f21ce477b7877850803a5a7d3f72a90bdd9.jpeg" width=400/>


#### 使用
##### 位移、缩放和旋转
位移、缩放和旋转在播放器内部完全实现，仅提供回调给开发者对更新后的数据进行存储。
1. 绑定事件回调：
```
<wj-player
	bindclipedit="handleClipEdit"
></wj-player>
```
2. 编写回调函数：
<dx-codeblock>
::: javascript javascript
Page({
	handleClipEdit(e) {
		let {
      designSize,
      clipId,
      trackId,
      operation
    } = e.detail
    if (operation === 'transform') {
       // 更新tracks数据
    }
	}
})
:::
</dx-codeblock>
	e.detail 的数据结构如下:
<dx-codeblock>
::: javascript javascript
{
	clipId, // 编辑的clipId
	type, // 编辑的clip类型
	trackId, // clip所属的track的id
	operation: 'transform', // 编辑类型，目前仅有transform
	designSize: {
		x, // 最新的位置
		y, 
		width, // 最新的宽高
		height,
		scale,	// 缩放比例
		rotation, // 旋转角度
	}
}
:::
</dx-codeblock>

##### 点击其他按钮
1. 绑定事件回调：
```
<wj-player
	bindclipoperation="handleClipOperation"
></wj-player>
```
2. 处理回调数据：
<dx-codeblock>
::: javascript javascript
handleClipOperation(e) {
  const operation = e.detail.operation;
  switch (key) {
    case 'duration': // 编辑时间段
      ...
    	break;
    case 'edit': // 修改
      ...
    	break;
    case 'delete': // 删除
      ...
    	break;
    default:
      break;
  }
}
:::
</dx-codeblock>
	e.detail 的数据结构如下:
<dx-codeblock>
::: javascript javascript
{
	clipId: this.container.id,
	type: this.container.type,
	trackId: this.container.parent.id,
	operation: type,
}
:::
</dx-codeblock>




#### 禁用控件
`Clip`中使用`editable`字段标记是否开启`Clip`的编辑功能，设为 false 则关闭。
`Sticker`和`Text`类型的`Clip`默认开启，对于其他的可视化元素，例如`image`或者`video`可手动将`editable`属性设置为`true`开启编辑功能。

```javascript
let editableImage = new global['wj-types'].Clip({
        type: 'image',
        section: {
          start: 0,
          end: 10,
        },
        editable: true,
        startAt: 0,
        info: {
          tempFilePath: 'https://imgcache.qq.com/operation/dianshi/other/WechatIMG6.5360f0efdca11a0977a5dfab2042a22af1cd3e14.jpeg',
          controls: ['delete', 'duration', 'transform'] // 显式传入控件数组可以决定展示部分按钮
        },
        designSize: {
          x: 200,
          y: 200,
          width: 300, 
          height: 300
        }
      })
```

>! 主轨道的视图元素不要开启 editable 功能，否则会导致渲染异常。

[](id:Mask)
### 蒙版控件
v2.1.0 微剪新增蒙版功能，播放器内置蒙版编辑功能。内置蒙版如下：

| 蒙版 | key |
| -- | -- |
| 线性蒙版 | linear |
| 镜面蒙版 | mirror |
| 圆形蒙版 | circle |
| 矩形蒙版 | rect   |
| 星形蒙版 | star   |
| 爱心蒙版 | heart  |

#### 使用 
1. 给某个 Clip 添加蒙版类型的`operation`。
```
let clip = ...
clip.operations = [
  {
    {
          // 蒙版类型, v2.1.0新增
          key: "mirror",  // key为效果的唯一标识
          type: "mask", // 标记操作类型
          id: "my-mask-operation", // id
        }
  }
]
```
更新数据到播放器，蒙版即生效。

2. 开启播放器的蒙版编辑
需要编辑蒙版的情况下，调用，即可在播放器内编辑蒙版。
```
this.player.showMaskControl()
```
蒙版变化后会由回调返回，用户可以接收修改后的蒙版参数并更新到对应`operation`的`params`中。
wxml：
```
<wj-player
			bindmaskedit="handleMaskEdit"
></wj-player>
```
js：
```
Component({
		handleMaskEdit(e) {
			let {clipId, trackId, params} = e.detail
			// 找到对应的clip更新operation.params
		}
})
```
3. 关闭播放器的蒙版编辑
需要编辑蒙版的情况下，调用，即可在播放器内编辑蒙版。
```
this.player.hideMaskControl()
```
