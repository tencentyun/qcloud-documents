播放器 **wj-player** 是支持微剪运行的核心组件，它是由轨道数据驱动运行的播放器，并内置了一些常用功能。
>?v1.4.0 后新增功能：
>- 贴纸，详情请参见 [自定义贴纸和文字](https://cloud.tencent.com/document/product/1156/49440)。
>- 文字和贴纸内置编辑控件，详情请参见 [编辑控件](https://cloud.tencent.com/document/product/1156/49441)。
>
>v1.5.0 后新增功能：
>转场和动效，详情请参见 [转场和动效](https://cloud.tencent.com/document/product/1156/50070)。

## 使用方式
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
      bindended="playerEnd"></wj-player>
```

## 属性说明

| 属性名               | 类型     | 默认值                                                       | 说明                                                         | 必填 |
| -------------------- | -------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---- |
| containerStyleConfig | Object   | `{height: 1334, width: 750}`                                 | 播放器的尺寸                                                 | 否   |
| mode                 | String   | default                                                      | <li />default：video 模式<li />offscreen：decoder offscreen 模式（导出模式），推荐直接使用`wj-export`组件 | 否   |
| allowSetVolumn       | Boolean  | false                                                        | 是否需要调整视频原声音量                                     | 否   |
| enableTapPause       | Boolean  | false                                                        | 是否启用点击暂停                                             | 否   |
| enablePauseIcon      | Boolean  | true                                                         | 是否显示暂停按钮                                             | 否   |
| enableClipEdit      | Boolean  | true                                                         | 是否启用编辑控件，编辑控件详见 [编辑控件](https://cloud.tencent.com/document/product/1156/49441)                        | 否   |
| preloadFilter        | Boolean  | true                                                         | 是否启用滤镜预加载                                           | 否   |
| preloadFilterKeys    | Array    | ['key1', 'key2']                                             | 需要提前加载的滤镜                                           | 否   |
| filters              | Array    | [{<br />key: 'lujing',<br />name: '滤镜'<br />src: 'wxfile://xxxxx'<br />}] | 定制化 effect 列表                                           | 否   |
| effects              | Array    | [{<br />name: EffectName,<br />fragment: Shader 代码字符串<br />}] | 定制化 shader 列表                                           | 否   |
| status               | String   | playing                                                      | 初始播放状态                                                 | 否   |
| bindready            | Function | -                                                            | 播放器初始化完成回调                                         | 否   |
| bindplay             | Function | -                                                            | 播放器开始播放                                               | 否   |
| bindpaused           | Function | -                                                            | 播放器暂停回调                                               | 否   |
| bindwaiting          | Function | -                                                            | 播放器加载中的回调                                           | 否   |
| bindloadcomplete     | Function | -                                                            | 播放器所有 Clip 加载完毕时触发                               | 否   |
| binddataupdated      | Function | -                                                            | 播放器 updateData 完成时触发<br />e.detail = [Tracks]        | 否   |
| bindtimeupdate       | Function | -                                                            | 播放进度变化时触发<br />e.detail = time                      | 否   |
| bindtapped           | Function | -                                                            | 播放器点击                                                   | 否   |
| bindended            | Function | -                                                            | 播放完成                                                     | 否   |
| bindtexttouchstart   | Function | -                                                            | 文字开始触摸(v1.4.0后废弃)                                   | 否   |
| bindtexttouchend     | Function | -                                                            | 文字触摸结束(v1.4.0后废弃)                                   | 否   |
| bindtexttouchmove    | Function | -                                                            | 文字移动(v1.4.0后废弃)                                       | 否   |
| bindclipedit    | Function | 详见 [编辑控件](https://cloud.tencent.com/document/product/1156/49441#.E4.BD.8D.E7.A7.BB.E3.80.81.E7.BC.A9.E6.94.BE.E5.92.8C.E6.97.8B.E8.BD.AC)                                                     |clip 位移、旋转、缩放                                   | 否   |
| bindclipoperation   | Function | 详见 [编辑控件](https://cloud.tencent.com/document/product/1156/49441#.E5.85.B6.E4.BB.96.E6.8C.89.E9.92.AE)                                                     |编辑控件按钮点击                                 | 否   |

## 方法说明

| 方法名        | 参数   | 返回值       | 说明                                     |
| ------------- | ------ | ------------ | ---------------------------------------- |
| play          | -      | -            | 播放                                     |
| pause         | -      | -            | 暂停                                     |
| seek          | number | -            | 跳转到某一时间播放                       |
| stop          | -      | -            | 停止                                     |
| updateData    | Object | -            | 更新播放轨道，更新播放器内数据           |
| types         | -      | player.Types | 返回可供操作 Tracks 的方法               |
| getFilters    | -      | Array        | 获取所有滤镜列表（默认返回内置滤镜列表） |
| getEffects    | -      | Array        | 获取所有特效列表（默认返回内置特效列表） |
| getDuration   | -      | Number       | 获取视频总时长                           |
| getTracks     | -      | Array        | 获取当前轨道                             |
| getPlayStatus | -      | String       | 获取当前播放状态                         |
| hideClipControl| -      | -           | 强制隐藏所有的编辑控件                         |
| preloadSticker| String（spritesheet 地址或 key 值）| -       | 异步方法，预加载贴纸       |

播放器围绕 Tracks 和 Clips 进行视频渲染， 前文数据结构详细介绍了 Tracks 和 Clips 直接的关系。接下来，我们一起来看一下如何对播放器进行渲染。
>?
>- 定制滤镜目前只支持 LUT 图滤镜，由于小程序下载文件的限制，LUT 图需要先 downloadFile 到本地。
>- 定制特效需要传入特效的片元着色器，详情见 [自定义特效和滤镜](https://cloud.tencent.com/document/product/1156/48621)。
>- v1.4.0 之后支持贴纸渲染，贴纸和文字的位移和缩放，详见 [自定义贴纸和文字](https://cloud.tencent.com/document/product/1156/49440) 和 [编辑控件](https://cloud.tencent.com/document/product/1156/49441)。

## 播放器使用示例
下述内容为您讲解如何使用播放器添加各种类型的轨道。
### 获取播放器实例
使用调用播放器支持的方法，需要先获取`player`组件的实例。步骤如下：
1.  wxml 里设置组件 id：
```html
<wj-player id="my-player"></wj-player>
```
2. js 获取 player 实例：
```javascript
let player = this.selectComponent("#my-player")
this.player = player;
```

### 媒体轨道使用说明
`wj-player`的播放必须有一条媒体轨道， 视频或者图片都需要加入到媒体轨道里。步骤如下：
>? 因为图片在播放器中将会默认当做3秒的静态视频播放，类似抖音。所以在播放器中图片和视频都属于媒体元素。
>
1. 创建视频轨道 Track，设置视频轨道的 type 为 media。
```javascript
  this.mediaTrack = new global['wj-types'].Track({
    type: 'media',
    clips: []
  });
```
>?`global['wj-types']`是在全局存储的插件暴露出来的对象，方便进行播放器的 Track 和 Clip 的操作。
2. 添加视频 Clip：
	1. 向 mediaTrack 媒体轨道中添加视频 Clip，设置视频 Clip 的 type 为 video。
```javascript
      let videoClip1 = new global['wj-types'].Clip({
        id: 'video1',
        type: 'video',
        info: {
          tempFilePath: 'wxfile:xxxx',
          width: '',
          height: '',
          duration: 5
        },
        section: new global['wj-types'].ClipSection({
          start: 0,
          end: 4
        }),
        startAt: 0
      })
```
<table>
<tr><th id="clip_parameter">参数</th><th>说明</th></tr>
<tr>
<td>info</td>
<td>tempFilePath 为视频的本地路径；width、height 对应视频的宽高；duration 为视频时长。</td>
</tr><tr>
<td>section</td>
<td>利用插件提供的 ClipSection 进行视频的时间范围选择，示例中选择了该视频0秒-4秒的区间片段。缺省值 start 为0，end 为 info 的 duration 值。</td>
</tr><tr>
<td>startAt</td>
<td>视频在轨道中的起始位置，也就是基于整个播放时长的起始时间，同一个 media track 中存在多个 clip 的情况非常有用，它决定了某个 clip 在整个 track 中的位置。</td>
</tr><tr>
<td>id</td>
<td>id 可以自定义，如果不传则由播放器内部自动生成。</td>
</tr></table>
	2. 因为 Clip 需要运行在 Track 中，接下来将 Clip 添加进 media 轨道：
```javascript
      this.mediaTrack.clips = [videoClip1];
```
3. 添加图片 Clip。
  1. 添加图片 Clip，设置图片的 Clip 的 type 为 image。
  ```javascript
      let imageClip1 = new global['wj-types'].Clip({
        id: 'image1',
        type: 'image',
        info: {
          tempFilePath: 'wxfile:xxxx',
          width: '',
          height: '',
          duration: 3
        },
        startAt: 4
      })
  ```
  >? 
  >- 图片类型 Clip 的 duration 默认值为3（与 settings 配置项中的 imgDisplayDuration 属性保持一致即可）。
  >- 上述 Clip 的 startAt 值为4，是因为此前我们已经加入了一个 video Clip，其 section 为4（end-start），即当前 Clip 之前的所有 Clip 的有效 section 之和。
  2. 把图片添加到 media 轨道：
```javascript
    this.mediaTrack.clips = [videoClip1, imageClip1];
```
>? 可以看到此时媒体轨道中已经添加一个视频和一张图片。以此类推，您可以按照这种方式添加更多的视频或者图片。
4. 更新播放器。<span id="updata_play"></span>
播放器均通过`updateData`方法实现更新`updateData`接受的参数为包含轨道的数组。以创建的媒体轨道后更新播放器为例，只需`updateData([媒体轨道])`即可 ：
```javascript
  this.player.updateData([this.mediaTrack]);
```
>? 以此类推，若您的播放器中包含视频，音乐，特效等，则`updateData([媒体轨道，音乐轨道， 特效轨道])`。
5. 修改视频时长。<span id="change_video"></span>
以修改视频片段 videoClip1 时长为例，直接修改 videoClip1 的 section 属性。
```javascript
videoClip1.section = new global['wj-types'].ClipSection({
    start: 1,
    end: 4
}),
```
同理，若您想修改 videoClip1 基于整体的开始播放时间。
```javascript
videoClip1.startAt = 1;
```
>! 对 Clip 的 section 或者 startAt 进行修改后，会影响到后续 Clip 的 startAt 值，需要按照上文提到的累加原则将其值更新一下。
>
修改完成后，更新一下播放器即可。
```javascript
  this.player.updateData([this.mediaTrack]);
```
6. 删除某个视频。<span id="delect_video"></span>
    在 media 轨道中删除对应的 Clip 即可，以删除 videoClip1 为例：
  1. 获取视频对应的 id（`video1`）进行删除。
```javascript 
      this.mediaTrack.clips.forEach((item, index) => {
        if(item.id === 'video1') {
          this.mediaTrack.clips.splice(index, 1)
        }
      })
```
  2. 更新 Clip 的 startAt 值。
  3. 更新播放器。
```javascript
  this.player.updateData([this.mediaTrack]);
```

### 音乐轨道使用说明
1. 添加音乐轨道：
```javascript
  this.musicTrack = new global['wj-types'].Track({
    type: 'music',
    clips: []
  });
```
2. 添加音乐片段：
  1. 添加音乐 Clip，设置音乐 Clip 的 type 为 music。
```javascript
	let musicClip1 = new global['wj-types'].Clip({
		id: 'music1',
		type: 'music',
		info: {
			tempFilePath: 'http://xxx.xxx.mp3',
		},
		section: new global['wj-types'].ClipSection({
			start: 0,
			end: 1000
		}),
		startAt: 0
	})
```
>?
	- `tempFilePath`为在线音乐地址。
	- 参数基本与视频的 Clip 一致，具体详情请参见 [Clip 参数详解](#clip_parameter)。
	- section 的 end 值为1000， 一般用于给整个视频添加一段音乐的情况，播放器内部会自动调整为实际的视频时长。
	- 将 musicClip1 加入到 musicTrack 中：
	```javascript
		this.musicTrack.clips = [musicClip1];
	```
  - 将音乐轨道加入播放器轨道：
```javascript
  this.player.updateData([this.mediaTrack, this.musicTrack]);
```
>? 可以看到此时播放器内拥有了两条轨道，媒体和音乐。
3. 修改音乐。
修改音乐和修改视频 Clip 是一样的，具体详情请参见 [修改视频时长](#change_video)。以修改音乐的起始时间为例：
```javascript
  musicClip1.startAt = 8;
```
音乐有一个比较特殊的属性：**音量**，取值范围为[0，1]，1为最大音量。示例：
```javascript
  musicClip1.audio.volume = 0.5;
```
修改完成后，更新播放器即可。
```javascript
  this.player.updateData([this.mediaTrack, this.musicTrack]);
```
4. 删除音乐。
 在播放器的轨道中去掉`this.musicTrack`音乐轨道，并重新调用`updateData`即可成功删除音乐。
```javascript
  this.player.updateData([this.mediaTrack]);
```


### 滤镜轨道使用说明
1. 添加滤镜轨道。
```javascript
  this.filterTrack = new global['wj-types'].Track({
    type: 'filter',
    clips: []
  });
```
2. 添加滤镜片段。<span id="filter_step2"></span>
  1. 获取播放器内部提供的默认滤镜：
  ```javascript
    const filterList = this.player.getFilters();
  ```
	<span id="filterList"></span>**filterList** 的数据结构如下所示：
  ```
    [
      {
        key: 'effect1',
        name: '特效1'
      },{
        key: 'effect2',
        name: '特效2'
      }
    ]
  ```
  2. 创建 filter clip：
  ```javascript
      let filterClip1 = new global['wj-types'].Clip({
        id: 'filter1',
        type: 'filter',
        key: 'baixi',
        section: new global['wj-types'].ClipSection({
          start: 0,
          end: 3
        }),
        startAt: 0
      })
  ```
  <table>
  <tr><th>参数</th><th>说明</th></tr><tr>
  <td>key</td>
  <td>滤镜的关键字，参考 <a href="#filterList">filterList</a> 结构。</td>
  </tr></table>
  3. 将 Clip 加入轨道：
  ```javascript
    this.filterTrack.clips = [filterClip1]
  ```
  4. 更新播放器：
  ```javascript
  this.player.updateData([this.mediaTrack, this.musicTrack, this.filterTrack]);
  ```
  > ? 此时您的播放器中拥有了3条轨道，媒体，音乐和滤镜。
3. 添加多个滤镜片段。
和添加多个视频 Clip 类似，您需要按照 [添加滤镜片段](#filter_step2) 创建另一个 filterClip2，添加到轨道中，然后更新播放器即可。
```javascript
  this.filterTrack.clips = [filterClip1, filterClip2]
```
4. 修改滤镜。
    修改滤镜对应的 Clip 属性，更新播放即可查看。以修改滤镜的时间信息为例：
```
    filterClip1.section = new global['wj-types'].ClipSection({
      start: 0,
      end: 5
    });
```
更新播放器即可查看效果。
5. 删除滤镜，主要分以下两种情况：
  - **删除滤镜轨道中的滤镜**：只需在`this.filterTrack.clips`中通过 id 找到对应的 Clip 进行删除即可。
```javascript
  this.filterTrack.clips.forEach((item, index) => {
      if(item.id === 'filter_id') {
        this.filterTrack.clips.splice(index, 1)
      }
  })
```
  - **删除整个滤镜轨道**：在 updateData 的数组去掉  `this.filterTrack` 即可。

### 特效轨道使用说明
1. 添加特效轨道。
```javascript
  this.effectTrack = new global['wj-types'].Track({
      type: 'effect',
      clips: []
    });
```
2. 添加滤镜片段。<span id="effect_step2"></span>
  1. 获取播放器内部提供的默认特效：
```javascript
  const effectList = this.player.getEffects();
```
<b id="effectList">effectList</b> 的数据结构如下：
```
    [
      {
        key: 'effect1',
        name: '特效1'
      },{
        key: 'effect2',
        name: '特效2'
      }
    ]
```
  2. 创建 effect Clip：
```javascript
    let effectClip1 = new global['wj-types'].Clip({
        id: 'effect1',
        type: 'effect',
        key: 'effect1',
        section: new global['wj-types'].ClipSection({
          start: 0,
          end: 3
        }),
        startAt: 0
      })
```
<table>
<tr><th>参数</th><th>说明</th></tr><tr>
<td>key</td>
<td>特效的关键字，参见 <a href="#effectList">effectList</a> 结构。</td>
</tr></table>
  3. 将 Clip 加入轨道：
```javascript
  this.effectTrack.clips = [effectClip1]
```
  4.  更新播放器：
```javascript
  this.player.updateData([this.mediaTrack, this.musicTrack, this.filterTrackm, this.effectTrack]);
```
>? 此时您的播放器中拥有了4条轨道：媒体、音乐、滤镜和特效。
3. 添加多个特效片段。
  1. 创建多个 effectClip：
```javascript
      let effectClip2 = new global['wj-types'].Clip({
        id: 'effect2',
        type: 'effect',
        key: 'effect2',
        section: new global['wj-types'].ClipSection({
          start: 0,
          end: 2
        }),
        startAt: 3
      })
      let effectClip3 = ...
```
  2. 将新创建的 effectClip 添加到轨道中：
```javascript
  this.effectTrack.clips = [filterClip1, filterClip2, filterClip3...]
```
更新播放器即可查看效果。
4. 修改特效。
修改特效对应的 Clip 属性，更新播放即可查看。以修改特效的持续时间为例：
```javascript
  effectClip1.section = new global['wj-types'].ClipSection({
    start: 0,
    end: 5
  });
```
5. 删除特效，主要分以下两种情况：
  - **删除轨道中的滤镜**，以删除 effectClip2 为例：
```javascript
    this.effectTrack.clips = [effectClip1, effectClip3...];
    this.player.updateData([this.mediaTrack, this.musicTrack, this.filterTrackm, this.effectTrack]);
```
  - **删除整个特效轨道**：
```javascript
  this.player.updateData([this.mediaTrack, this.musicTrack, this.filterTrack]);
```

<span id = "sss"></span>
### 文字轨道使用说明
1. 添加文字轨道。
```javascript
this.textTrack1 = new global['wj-types'].Track({
		type: 'text',
		clips: []
	});
```
2. 添加文字片段。
	1. 创建 textClip：
```javascript
	let textClip1 = new global['wj-types'].Clip({
			type: 'text',
			startAt: 0,
			section: new global['wj-types'].ClipSection({
				start: 0,
				end: 100
			}),
			content: {
					content: text.value, // 文字内容
					style: {
							type: text.bgColor === 'transparent' ? 'normal' : 'background', // 文字样式
							color: text.color, // 文字颜色
							backgroundColor: text.bgColor
					}
			},
	})```
<table>
<tr><th>参数</th><th>说明</th></tr><tr>
<td>content</td>
<td>content 为文字的内容，可通过 style 自定义文字的颜色和背景颜色。</td>
</tr></table>
 <b>文字的位置控制</b>逻辑在播放器内部，所以您只需要把文字添加进播放器，通过拖拽挪动文字位置，相应的位置信息将初始化传入的文字统一位于视频的中心位置。
 
  2. 将新创建的 textClip 添加到轨道中：
```javascript
this.textTrack.clips = [textClip1]
```
<span id = "more_clip"></span>当然，您也可以在一个轨道添加多个文字，文字 Clip 的 section 没有重叠。
```javascript
this.textTrack.clips = [textClip1, textClips2, ...]
```
3. 更新文字。
前往所需更新的文字修改对应的 Clip 属性即可，以更新 textClip1 的文字颜色为例：
```javascript
textClip1.style.color = 'blue'
```
4. 删除文字，主要分以下两种情况：
 - **删除 Clip**，以删除 textClips2 为例：
```javascript
this.textTrack.clips = [textClip1, textClips3]
```
 - **删除整个文字轨道**：
```javascript
this.player.updateData([this.mediaTrack, this.musicTrack, this.filterTrack]);
```
5. 多个文字共存。
在同一个轨道中添加多个 [文字 Clip](#more_clip) 的情况下，各个文字 Clip 之间的 section 是不存在交集的，即某一时刻页面最多显示一个文字。假设需要多个文字同时展示的情况下，则需要通过多个文字 Track 实现，每个轨道中只包含一个文字 Clip。
```javascript
  this.textTrack1 = new global['wj-types'].Track({
    type: 'text',
    clips: []
  });

  this.textTrack1.clips = [textClip1];

  this.textTrack2 = new global['wj-types'].Track({
    type: 'text',
    clips: []
  });

  this.textTrack1.clips = [textClip2];

 ... // 以此类推
```
  创建完文字轨道后，更新播放器即可。
```javascript
    this.player.updateData([this.mediaTrack, this.musicTrack, this.filterTrack, this.textTrack1, this.textTrack2]);
```
>! **由于小程序限制，最多只能存在5个文字。 可以添加5个文字轨道，一个轨道中一段文字；或者一个轨道中，5段文字，即文字 Clip 总共不能超过5个。**
>
6. 给文字添加字体。
由于小程序插件无法调用 wx.loadFontFace 方法，因此需要小程序手动暴露该接口给插件，或者在小程序内提前加载字体后再传入插件渲染。详情可参考 [自定义贴纸和字体](https://cloud.tencent.com/document/product/1156/49440)。
**加载字体**：
```javascript
loadFontFace({
	family: 'fangzhengyouhei',
  source: "https://fontPath",
  scopes: ['webview','native'],
  success(res) {
    console.log('font success')
    console.log(res.status)
    resolve()
  },
  fail: function(res) {
    console.log('font fail')
    console.log(res.status)
    reject()
  }
});
```
**构造对应的文字 clip**：
```javascript
  let mytext = new global['wj-types'].Clip({
    type: 'text',
    content: {
      content: "文字", // 文字内容
      style: {
        type: 'background', // 文字样式
        color: '#ffffff', // 文字颜色
        backgroundColor: '#ff00ff',
        fontfamily: 'fangzhengyouhei',
        fontloaded: true
      },
      position: {
        x: 50,
        y: 90
      },
    },
    section: {
      start: 0,
      end: 10,
      duration: 10
    },
  })
```
>? 内置字体列表获取请参考 [内置资源](https://cloud.tencent.com/document/product/1156/49439)。

### 贴纸轨道使用说明
1. 创建贴纸轨道
```javascript
   this.stickerTrack = new global['wj-types'].Track({
       type: 'sticker',
       clips: []
   });
```
2. 添加贴纸片段
```javascript
   let stickerclip = new global['wj-types'].Clip({
     id: 'my-sticker',
     type: 'sticker',
     section: {
       start: 0,
       end: 10,
       duration: 10
     },
     designSize: {
        xPercent: 0.20, //初始位置
        yPercent: 0.30,
        rotation: 0.4, // 旋转角度（单位弧度）
        scale: 2 // 缩放尺寸
     },
     startAt: 0,
     key: 'guodong',  // 贴纸key
   })
   this.stickerTrack.clips.push(stickerclip)
   this.player.updateData([this.mediaTrack, this.musicTrack, this.filterTrack, this.stickerTrack]);
```
   >? 内置贴纸列表获取请参考 [内置资源](https://cloud.tencent.com/document/product/1156/49439)。更多属性请参考 [数据结构文档](https://cloud.tencent.com/document/product/1156/48616)。

