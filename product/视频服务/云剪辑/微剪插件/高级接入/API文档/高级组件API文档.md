## 播放器：wj-player

`wj-player` 是支持微剪运行的核心组件，它是由轨道数据驱动运行的播放器，并内置了一些常用功能。

>?v1.4.0后新增功能：
>1. 贴纸，详见 [自定义贴纸和文字](https://cloud.tencent.com/document/product/1156/49440)。
2. 文字和贴纸内置编辑控件，详见 [编辑控件](https://cloud.tencent.com/document/product/1156/49441)。

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
      bindended="playerEnd"></wj-player>
```

### 属性说明

| 属性名               | 类型     | 默认值                                                       | 说明                                                         | 必填 |
| -------------------- | -------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---- |
| containerStyleConfig | Object   | `{height: 1334, width: 750}`                                 | 播放器的尺寸                                                 | 否   |
| mode                 | String   | default                                                      | <li />default：video 模式<li />offscreen：decoder offscreen 模式（导出模式），推荐直接使用 `wj-export` 组件 | 否   |
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

### 方法说明

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
>- v1.4.0之后支持贴纸渲染，贴纸和文字的位移和缩放，详见 [自定义贴纸和文字](https://cloud.tencent.com/document/product/1156/49440) 和 [编辑控件](https://cloud.tencent.com/document/product/1156/49441)。

### 播放器使用示例

下述内容为您讲解如何使用播放器添加各种类型的轨道。

#### 获取播放器实例

使用调用播放器支持的方法，需要先获取 `player` 组件的实例。步骤如下：

1.  wxml 里设置组件 id：
```html
<wj-player id="my-player"></wj-player>
```
2. js 获取 player 实例：
```javascript
let player = this.selectComponent("#my-player")
this.player = player;
```

#### 添加媒体轨道
`wj-player` 的播放必须有一条媒体轨道， 视频或者图片都需要加入到媒体轨道里。步骤如下：
>? 因为图片在播放器中将会默认当做3秒的静态视频播放，类似抖音。所以在播放器中图片和视频都俗属于媒体元素。

1. 创建视频轨道 Track，设置视频轨道的 type 为 media。
```javascript
  this.mediaTrack = new global['wj-types'].Track({
    type: 'media',
    clips: []
  });
```
>?`global['wj-types']` 是在全局存储的插件暴露出来的对象，方便进行播放器的 Track 和 Clip 的操作。
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
2. 因为 Clip 需要运行在 Track中，接下来将 Clip 添加进 media 轨道：
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
播放器均通过 `updateData` 方法实现更新，`updateData` 接受的参数为包含轨道的数组。以创建的媒体轨道后更新播放器为例，只需`updateData([媒体轨道])` 即可 ：
```javascript
  this.player.updateData([this.mediaTrack]);
```
>? 以此类推，若您的播放器中包含视频，音乐，特效等，则 `updateData([媒体轨道，音乐轨道， 特效轨道])`。
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

####   添加音乐轨道

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
#### 说明
	- `tempFilePath` 为在线音乐地址。
	- 参数基本与视频的 Clip 一致，具体请参见 [Clip 参数详解](#clip_parameter)。
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
修改音乐和修改视频 Clip 是一样的，具体请参见 [修改视频时长](#change_video)。以修改音乐的起始时间为例：
```javascript
  musicClip1.startAt = 8;
```
音乐有一个比较特殊的属性：**音量**，取值范围为[0，1]，1为最大音量。示例：
```javascript
  musicClip1.volume = 0.5;
```
修改完成后，更新播放器即可。
```javascript
  this.player.updateData([this.mediaTrack, this.musicTrack]);
```
4. 删除音乐。
 在播放器的轨道中去掉 `this.musicTrack` 音乐轨道，并重新调用 `updateData` 即可成功删除音乐。
```javascript
  this.player.updateData([this.mediaTrack]);
```


####  添加滤镜轨道
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
  <b id="filterList">filterList</b> 的数据结构如下所示：
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
  - **删除滤镜轨道中的滤镜**：只需在 `this.filterTrack.clips` 中通过 id 找到对应的  Clip 进行删除即可。
```javascript
  this.filterTrack.clips.forEach((item, index) => {
      if(item.id === 'filter_id') {
        this.filterTrack.clips.splice(index, 1)
      }
  })
```
  - **删除整个滤镜轨道**：在 updateData 的数组去掉  `this.filterTrack` 即可。

#### 添加特效轨道
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
#### 添加文字轨道
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

#### 添加贴纸轨道
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

## 照相机：wj-camera

相机组件提供用户拍摄（前置、后置），访问相册增加 Clip（图片、视频），展示已选 Clip 列表，删除 Clip（单个删除、整体删除）等基本功能，是 Clip 的入口组件。
>?1.4.0版本开始组件支持多段拍摄，设置倒计时等。

### 使用方式
1. 配置 JSON 文件：
```json
  {
      "usingComponents": {
        "wj-camera": "plugin://myPlugin/wj-camera"
      }
  }
```
2. 在 wxml 中引入组件：
```
  <wj-camera bindmediachanged="onMediaChanged" clips="{{clips}}"></wj-camera>
```

### 属性说明

| 属性名           | 类型          | 默认值                  | 说明                                                   | 是否必填 |
| ---------------- | ------------- | ----------------------- | ------------------------------------------------------ | -------- |
| settings         | Object        | 参见 [settings 默认值](#camera_settings) | 设置                                                   | 否       |
| clips            | `Array<clip>` | []  | 初始 Clip，具体请参见 [clip 结构](#camera_clip)                             | 否       |
| mode            | String | 'simple'  | simple: 简单模式 </br> advanced: 高级模式，支持滤镜 | 否       |
| countdown            | Number | 0  | 拍摄倒计时 | 否       |
| filter            | String | 空  | advanced模式下使用的滤镜名称 | 否       |
| bindready        | Function      | -                       | 组件加载完成回调                                       | 否       |
| bindtapstartrecord        | Function      | -                       | 拍摄按钮点击事件                       | 否       |
| bindtapstoprecord       | Function      | -                       | 停止按钮点击事件                       | 否       |
| bindswipetoright       | Function      | -                       | 右划事件（仅advanced模式有效）                       | 否       |
| bindswipetoleft       | Function      | -                       | 左划事件 （仅advanced模式有效）                      | 否       |
| bindmediachanged | Function      | -                       | 选择 Clip 的回调<pre style="margin:0" />`e.detail = {track: Array<Track>`}</pre> | 否       |

#### settings 默认值<span id="camera_settings"></span>
```
  {
      videoMaxDuration: 30, // 拍摄时长限制（秒）
      clipMaxDuration: 60, // 裁切时长限制（秒）
      imgDisplayDuration: 3, // 单张图片默认展示时间（秒）
      allMediaNum: 9, // 可选Clip（图片+视频）数量限制
      videoMediaNum: 5, // 可选Clip（视频）数量限制
      defaultBgColor: '#ff584c', // 录制按钮默认状态背景色
      defaultBdColor: 'rgba(255,88,76,0.5)', // 录制按钮默认状态外边框颜色
      recordBgColor: '#fff', // 录制按钮录制状态外边框颜色
      chooseVideoIcon: './images/choose_video.png', // 选择按钮
      switchDirectionIcon: './images/switch_camera.png', // 切换按钮
      deleteRecord: './images/delete_record.png', // 拍摄界面删除按钮
      completeRecord: './images/complete_record.png' // 完成拍摄按钮
  }
```

####   clip 结构：<span id="camera_clip"></span>
```
  {
    type: "image" // Clip类型：image 、video
    duration: 3 // Clip时长
    height: 200 // Clip尺寸
    width: 200 // Clip尺寸
    tempFilePath: "http://tmp/wx76f1d77827f78beb.o6zAJs6MVPjJua9TiSq8YEZReGyE.awQ1B4forrYi5f8e3e782e61d8c3a6d7b38c77946914.png" // Clip临时地址
    tempThumbPath: "http://tmp/wx76f1d77827f78beb.o6zAJs6MVPjJua9TiSq8YEZReGyE.xROdutgzbxe8f6504bf32111715b890a1eea74f8f8db.jpg" // Clip缩略图地址（可选，video类型Clip必须）
  }
```

#### 说明
- 主界面底部三个操作按钮，分别为：切换摄像头方向、拍摄、跳转相册。
- 1.4.0版本开始支持多段拍摄，中途单击拍摄按钮会暂停并保存，再次单击继续拍摄。单击右侧【删除】可删除已拍摄片段，单击【完成】结束拍摄。
- 拍摄总时长受 **小程序平台限制，最大值为 30s**。
- 视频 Clip 数量最大值为5，Clip（图片+视频）数量最大值为9。
- Clip 展示页展示已选择或已拍摄 Clip，单击 Clip 右上角的【删除】可删除单个 Clip；单击空白处可删除全部 Clip。
- 小程序平台限制，无法在插件中直接调用 `wx.navigateTo` 实现页面跳转，只能使用 [navigator 组件](https://developers.weixin.qq.com/miniprogram/dev/component/navigator.html) ，故我们预留了一个 `slot 插槽` 供用户实现个性化跳转需求，使用方式如下：
```
  <wj-camera bindmediachanged="onMediaChanged" clips="{{clips}}">
      <view 
        class="next-btn" 
        hover-class="hover-btn" 
        catchtap="onClickNext">
          <navigator data-source="jump" url="页面路由" hover-class="none">
            <text>下一步</text>
          </navigator>
      </view>
  </wj-camera>
```

## 裁切器：wj-clipper
裁切器组件接收标准的 Track 数据，根据一定的规则生成 Clip 的缩略图，绘制到组件中。裁切器通常与上述 `wj-player` 组件搭配使用，实现实时的裁切预览功能。

### 使用方式
1. 配置 JSON 文件：
```json
  {
    "usingComponents": {
      "wj-clipper": "plugin://myPlugin/wj-clipper"
    }
  }
```
2.  在 wxml中引入组件：
```
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

### 属性说明
| 属性名                   | 类型     | 默认值                  | 说明                                                         | 是否必填 |
| ------------------------ | -------- | ----------------------- | ------------------------------------------------------------ | -------- |
| trackInfo| Track    | null| Track 数据，请参见 [trackInfo 结构](#clipper_trackInfo)| 是|
| time                     | Number   | 0| 当前展示时间，控制时间轴的位置| 否|
| settings                 | Object   | 请参见 [settings 默认值](#clipper_settings) | 设置| 否|
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


####  trackInfo 结构<span id="clipper_trackInfo"></span>
clipper 组件接受的 trackInfo 数据相比于标准的 Track 多了几个属性，如下所示：
```
 {
   innerStartTime: Number, // 裁切区间开始时间
   innerEndTime: Number, // 裁切区间结束时间
   scrollStartTime: Number // 缩略图滚动时间（影响最终的 clipped 数据）
 }

```
####  settings 默认值<span id="clipper_settings"></span>
```
  {
    clipMaxDuration: 60, // 裁切时长限制（秒）
    mainColor: "rgba(255,88,76)" // 裁切器主题色
  }
```

### 组件实例属性
| 属性名            | 类型     | 参数            | 说明                                                         |
| ----------------- | -------- | --------------- | ------------------------------------------------------------ |
| getValidTrackData | Function |  Array&lt;Track&gt; | 根据 [trackInfo](#clipper_trackInfo) 的 innerStartTime、innerEndTime 值获取有效的 Track 数据 |

#### 说明
- 裁切器涉及两个重要概念：缩略图展示区间、裁切区间。
  - **缩略图展示区间**：与 Clip 对象的 section 属性的值有关，start、end 属性决定单个 Clip 展示的缩略图时间区间。
  - **裁切区间**：与 trackInfo 的 innerStartTime、innerEndTime 字段的值有关，决定了整个 Track 裁切区间的起始时间。
- 通过 [获取组件实例](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/events.html) 的方式，可以调用组件暴露的 `getValidTrackData` 方法，将裁切区间外的无效数据过滤掉。
- 触发 clipped 事件的操作：左右手柄 touch-end、缩略图滚动停止。
- 触发 timerollermove 事件的操作：左右手柄 move、时间轴 move。

### 裁剪示例
通过两个示例解释下上述裁切器相关字段的含义，下例默认最大裁切区间都为60s。

#### 示例1：单段裁切示例
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
#### 示例2：多段裁切示例
![](https://main.qcloudimg.com/raw/403467e0c4a33f975e6a5b82d87e446c.png)
上述 Track 由3个 Clip 组成，时长分别为30s、15s、55s，track 的总时长为100s。

对应的 Track 数据如下所示：
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


## 导出：wj-export
导出组件提供了视频导出的功能，内部复用了 `wj-player`，针对小程序导出进行了专门处理。
>!受微信 Android 客户端 7.0.19 版本策略影响，导出表现偏慢，预计在11月底的版本修复。

### 使用方式
1. 配置 JSON 文件：
```
  {
      "usingComponents": {
        "export": "plugin://myPlugin/wj-export"
      }
    }
```
2. 在 wxml 中引入组件：
```wxml
  <export
      tracks="{{tracks}}"
      bindprogress="handleProgress"
      bindexportsuccess="handleExportSuccess"
      bindexportfail="handleExportFail"
      bindready="handleReady"
      bindthumbready="handleThumbReady"
      watermark="{{watermark}}"
      quality="{{quality}}"
      showloading="{{showloading}}">
      <button bindTap="startExport">导出视频</button>
  </export>
```

### 属性说明

| 属性名            | 类型                          | 默认值 | 说明                                                         | 必填 |
| ----------------- | ----------------------------- | ------ | ------------------------------------------------------------ | ---- |
| tracks            | Array&lt;Track&gt;                 | []     | 导出视频的轨道信息                                           | 是   |
| quality           | Enum('high', 'medium', 'low') | medium | 导出视频质量选项。提供 high，medium，low 三个选项。以标准16：9视频为例：<li/>high 导出分辨率为1080\*1920<li/>medium 导出分辨率为720\*1280<li/>low 导出分辨率为 540\*960 | 否   |
| showloading       | Boolean                       | false  | 是否显示默认的导出进度 toast，默认值：false                    | 否   |
| watermark         | String                        | -      | 水印地址，支持线上链接和本地临时地址 | 否   |
| watermarkX | Number | 15 | 水印基于左上角X偏移量 | 否 |
| watermarkY | Number | 15 | 水印基于左上角Y偏移量 | 否 |
| bindready         | Function                      | -      | 导出组件加载完成时触发                                       | 否   |
| bindexportstart   | Function                      | -      | 导出流程开始                                                 | 否   |
| bindprogress      | Function                      | -      | 导出进度更新<pre style="margin:0">e.detail =  {<br />progress: Number<br />} </pre>| 否   |
| bindexportsuccess | Function                      | -      | 导出成功<pre style="margin:0">{<br/> code: 0, //成功<br/>  tempFilePath: 'wxfile://xxx.mp4',<br/>  coverInfo: {<br/>    path: xxx,<br/>    width: 544,<br/>    height: 960<br/>  }, // 封面信息<br/>  video: {<br/>    width: '544', //视频分辨率<br/>    height: '960',<br/>   fps: 30, //帧率<br/>  }<br/>  duration: 3000 //单位 ms<br/>}</pre> | 否   |
| bindexportfail    | Function                      | -      | 导出失败<pre style="margin:0">{<br/>message: String,<br />error: errorStack<br />}</pre>| 否   |
| bindthumbready    | Function                      | -      | 默认封面图生成<pre style="margin:0">{<br/>path: String,<br/>height:1080,<br />width: 720<br/>}</pre> | 否   |

#### 添加水印
##### 线上地址
如果需要使用在线图片，请按如下步骤配置。
1. 在小程序根目录下引入 index.js，目录：`miniprogram/index.js`。
```
		module.exports = {
			downloadFile:wx.downloadFile
		}
```
2. 	在 `app.json` 中将 downloadFile 方法导出到插件。
      ```json
        "plugins": {
          "myPlugin": {
            "provider": "wx76f1d77827f78beb",
            "version": "xxxx.xxx.xxx",
            "export": "index.js"
          }
        },
      ```
3. 进入小程序管理后台，将在线图片域名配置进 `request` 和 `downloadFile` 白名单即可。

##### 本地地址
传入`wxfile://` 开头的本地临时地址即可。
>?导出组件提供了`slot 插槽`以定制导出组件的实际 UI，并监听内部冒泡的 tap 事件以触发导出流程；如果需要手动触发导出流程，可以使用`wx.selectComponent`获取组件实例并调用实例的`start`方法。


## 文字编辑：wj-textEditor

文字编辑组件是一个简单的模拟原生输入框的组件，用于向视频中添加文本贴纸。支持动态修改文本的颜色、背景色及字体（1.4.0版本新增），提供实时预览功能。

### 使用方式
1. 配置 JSON 文件：
```json
  { 
    "usingComponents": {
      "wj-textEditor": "plugin://myPlugin/wj-textEditor"
    }
  }
```
2. 在 wxml 中引入组件：
```
  <wj-textEditor value="{{textValue}}" bindconfirm="onConfirmText"/>
```

### 属性说明

| 属性名      | 类型     | 默认值           | 备注                                                         | 必填 |
| ----------- | -------- | ---------------- | ------------------------------------------------------------ | ---- |
| show       | Boolean   | false           | 是否显示输入组件                                                    | 是   |
| value       | String   | 空               | 文本内容                                                     | 否   |
| color       | String   | #fff             | 字体颜色，标准 css 颜色值，默认白色                            | 否   |
| bgColor     | String   | transparent      | 背景色，标准 css 颜色值，默认透明                              | 否   |
| fontStyle     | Object   | {fontfamily:'moren',fonturl:''}      |  {fontfamily:字体名称标识（字母）,fonturl:字体文件地址}  | 否   |
| colorList   | Array    | 组件默认颜色集合 | [{key：唯一标识，value：标准 css 颜色值}]                      | 否   |
| fontList   | Array    | 组件默认字体集合 | [{name: 字体名称（汉字）,family: 字体名称标识（字母） ,url: 字体文件地址}]                      | 否   |
| bindconfirm | Function | -                | 用户输入完成：<pre style="margin:0">e.detail = { value: 文本内容, <br/>color: 文本颜色, <br/>bgColor: 背景色, <br/>showTextBg: 是否显示背景色 <br/>family: 字体名称,<br/>fontUrl: 字体文件地址,<br/>fontloaded: 是否已下载字体文件<br/>} </pre>| 否   |
| bindclose   | Function | -                | 用户取消输入                                                 | 否   |

### 操作说明
输入文字，单颜色列表实时更换文本颜色，单击左侧 T 图标实时更换背景颜色。
>?1.4.0版本开始支持修改字体。
1.4.3版本优化了字体缓存的逻辑，请避免使用`wx:if`控制`wj-textEditor`的显示，推荐使用`show`属性来控制以达到更好的加载性能。

