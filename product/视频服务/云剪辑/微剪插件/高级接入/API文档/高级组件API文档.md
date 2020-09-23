## 组件API文档

### 1. 播放器: wj-player

wj-player是支持微剪运行的核心组件，它是由轨道数据驱动运行的播放器，并内置了一些常用功能。

* 引入

  step1：配置json文件

  ```
  {
    	"usingComponents": {
     		"wj-player": "plugin://myPlugin/wj-player"
    	}
  }
  ```

  step2：引入组件

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


* 属性

  | 属性名 | 类型 | 默认值 | 说明 | 必填 |
  | -------- | ------ | -------------- | ------------------- | -------- |
  | containerStyleConfig     | Object  | `{height: 1334, width: 750}` | 播放器的尺寸 | 否 |
  | mode     | String  | default | 1. default: video模式 2. offscreen: decoder offscreen模式（导出模式） | 否 |
  | allowSetVolumn     | Boolean  | false | 是否需要调整视频原声音量 | 否 |
  | enableTapPause     | Boolean  | false | 是否启用点击暂停 | 否 |
  | enablePauseIcon     | Boolean  | true | 是否显示暂停按钮 | 否 |
  | preloadFilter     | Boolean  | true | 是否启用滤镜预加载 | 否 |
  | preloadFilterKeys     | Array  | ['key1', 'key2'] | 需要提前加载的滤镜 | 否 |
  | filters     | Array  | [{<br />key: 'lujing',<br />name: '滤镜'<br />src: 'wxfile://xxxxx'<br />}] | 定制化effect列表 | 否 |
  | effects     | Array  | [{<br />name: EffectName,<br />fragment: Shader代码字符串<br />}] | 定制化shader列表 | 否 |
  | status     | String  | playing | 初始播放状态 | 否 |
  | bindready | Function |  | 播放器初始化完成回调 |  |
  | bindplay | Function |  | 播放器开始播放 |  |
  | bindpaused | Function |  | 播放器暂停回调 |  |
  | bindwaiting | Function |  | 播放器加载中的回调 |  |
  | bindloadcomplete | Function |  | 播放器所有Clip加载完毕时触发 |  |
  | binddataupdated | Function |  | 播放器updateData完成时触发<br />e.detail = [Tracks] |  |
  | bindtimeupdate | Function |  | 播放进度变化时触发<br />e.detail = time |  |
  | bindtapped | Function |  | 播放器点击 |  |
  | bindended | Function |  | 播放完成 |  |
  | bindtexttouchstart | Function |  | 文字开始触摸 |  |
  | bindtexttouchend | Function |  | 文字触摸结束 |  |
  | bindtexttouchmove | Function |  | 文字移动 |  |


* 方法

  | 方法名 | 参数 | 返回值 | 说明 |
  | -------- | ------ | -------------- | ------------------- |
  | play | - | - | 播放 |
  | pause | - | - | 暂停 |
  | seek | number | - | 跳转到某一时间播放 |
  | stop | - | - | 停止 |
  | updateData | Object | - | 更新播放轨道，更新播放器内数据 |
  | types | - | player.Types | 返回可供操作tracks的方法 |
  | getFilters | - | Array | 获取所有滤镜列表（默认返回内置滤镜列表） |
  | getEffects | - | Array | 获取所有特效列表（默认返回内置特效列表） |
  | getDuration | - | Number | 获取视频总时长 |
  | getTracks | - | Array | 获取当前轨道 |
  | getPlayStatus | - | String | 获取当前播放状态 |

  播放器围绕`tracks`和`clips`进行视频渲染， 前文数据结构详细介绍了tracks和clips直接的关系。接下来，我们一起来看一下如何对播放器进行渲染。
* 说明
  * 定制滤镜目前只支持 LUT 图滤镜，由于小程序下载文件的限制，LUT图需要先downloadFile到本地
  * 定制特效需要传入特效的片元着色器，详情见【高级功能】-> 【自定义特效和滤镜】

#### 播放器使用示例

以下内容将围绕使用播放器添加各种类型的轨道来描述。

  **1.获取播放器实例**

  如果想调用播放器支持的方法，需要先获取`player`组件的实例。

  **step1** wxml里设置组件id

  ```html
  <wj-player id="my-player"></wj-player>
  ```
    
  **step2** js获取player实例
    
  ```javascript
    let player = this.selectComponent("#my-player")
    this.player = player;
  ```

  **2.添加媒体轨道**

  wj-player的播放必须有一条媒体轨道， 视频或者图片都需要加入到媒体轨道里。

  > 因为图片在播放器中将会默认当做3秒的静态视频播放，类似抖音。所以在播放器中图片和视频都俗属于媒体元素。

    
  **step1** 创建视频轨道`track`
  视频轨道的 type 为 media。


  ```javascript
  this.mediaTrack = new global['wj-types'].Track({
    type: 'media',
    clips: []
  });
  ```
  `global['wj-types']` 是在全局存储的插件暴露出来的对象，方便进行播放器的track和clip的操作。
  
  接下来向 mediaTrack 媒体轨道中添加clip。

  **step2** 添加视频 clip

  视频clip的type为video。
  
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
  参数解释： 

  `info`: tempFilePath字段为视频的本地路径；width，height对应视频的宽高；duration为视频时长。

  `section`: 利用插件提供的ClipSection进行视频的时间范围选择，示例中选择了该视频0-4秒的区间片段。缺省值start为0，end为info的duration值。

  `startAt`: 视频在轨道中的起始位置，也就是基于整个播放时长的起始时间，同一个 media track 中存在多个clip的情况非常有用，它决定了某个clip在整个track中的位置。

  `id`: id可以自定义，如果不传则由播放器内部自动生成。

  前面提到了，clip需要运行在track中，接下来将clip添加进media轨道：

  ```javascript
    this.mediaTrack.clips = [videoClip1];
  ```
  
  **step3** 添加图片clip

  我们已经添加了一个视频片段，假如还想添加一张图片呢？

  图片的clip类型为image。
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

  > 图片类型clip的duration默认值为3（与settings配置项中的imgDisplayDuration属性保持一致即可）

  > 上述clip的startAt值为4，是因为在这之前我们已经加入了一个video clip，其section为4（end-start），即当前clip之前的所有clip的有效section之和。
  
  接下来把图片添加到media轨道：
  ```javascript
    this.mediaTrack.clips = [videoClip1, imageClip1];
  ```

  可以看到此时媒体轨道中已经添加一个视频和一张图片。依次类推，你可以按照这种方式添加更多的视频或者图片。

  **step4** 更新播放器

  播放器一切更新的入口都为`updateData`这个方法。
  
  updateData接受的参数为包含轨道的数组，例如前面创建的媒体轨道，你只需要`updateData([媒体轨道])`即可，依次类推，如果你的播放器中包含视频，音乐，特效等，则 `updateData([媒体轨道，音乐轨道， 特效轨道])`。

  ```javascript
  this.player.updateData([this.mediaTrack]);
  ```

  **step5** 修改视频时长

  假如此时想修改视频片段videoClip1的时长，直接修改videoClip1的section属性即可。

  ```javascript
  videoClip1.section = new global['wj-types'].ClipSection({
    start: 1,
    end: 4
  }),
  ```
  同理，如果你想修改videoClip1基于整体的开始播放时间。

  ```javascript
  videoClip1.startAt = 1;
  ```

  **注意：对clip的section或者startAt进行修改后，会影响到后续clip的startAt值，需要按照上文提到的累加原则将其值更新一下。**

  修改完成后，更新一下播放器即可。
  ```javascript
  this.player.updateData([this.mediaTrack]);
  ```

  **step6** 删除一个视频

  想删除一个视频片段，只需在media轨道中删除对应的clip即可。
  假如要删除videoClip1我们只需要获取到它对应的自定义id `video1`即可进行删除。
  ```javascript
  
  this.mediaTrack.clips.forEach((item, index) => {
    if(item.id === 'video1') {
      this.mediaTrack.clips.splice(index, 1)
    }
  })
  ```
  **同理，更新后续clip的startAt值。**

  删除之后更新下播放器
  ```javascript
  this.player.updateData([this.mediaTrack]);
  ```
  
  
  **3.添加音乐轨道**

  **step1** 添加音乐轨道
  ```javascript
  this.musicTrack = new global['wj-types'].Track({
    type: 'music',
    clips: []
  });
  ```

  **step2** 添加音乐片段

  ```javascript
    let musicClip1 = new global['wj-types'].Clip({
      id: 'music1',
      type: 'music',
      info: {
        tempFilePath: 'wxfile:xxxx',
      },
      section: new global['wj-types'].ClipSection({
        start: 0,
        end: 1000
      }),
      startAt: 0
    })
  ```
  参数解释：
  参数基本和视频的clip一致，不过多解释。
  > section的end值为1000， 一般用于给整个视频添加一段音乐的情况，播放器内部会自动调整为实际的视频时长。
  
  同理，接下来把musicClip1加入到musicTrack中即可。
  
  ```javascript
  this.musicTrack.clips = [musicClip1];
  ```

  将音乐轨道加入播放器轨道
  ```javascript
  this.player.updateData([this.mediaTrack, this.musicTrack]);
  ```
  可以看到此时播放器内拥有了两条轨道，媒体和音乐。

  **step3** 修改音乐

  修改音乐和修改视频clip是一样的，假如需要修改音乐的起始时间。

  ```javascript
  musicClip1.startAt = 8;
  ```
  同样，修改完记得更新播放器。

  音乐有一个比较特殊的属性，`音量`。假如你需要修改音乐的音量，可以这么做
  ```javascript
  musicClip1.volume = 0.5;
  ```
  > 注意： 音乐的音量范围是0-1， 1为最大音量。
  
  然后更新即可。
  ```javascript
  this.player.updateData([this.mediaTrack, this.musicTrack]);
  ```

  **step4** 删除音乐

  想删除音乐，只需要在播放器的轨道中去掉this.musicTrack 音乐轨道即可，所以重新调用`updateData`就能做到删除音乐。

  ```javascript
  this.player.updateData([this.mediaTrack]);
  ```

  **4.添加滤镜轨道**
  
  **step1** 添加滤镜轨道
  ```javascript
  this.filterTrack = new global['wj-types'].Track({
    type: 'filter',
    clips: []
  });
  ```
  **step2** 添加滤镜片段

  播放器内部提供一些默认滤镜，可以通过下述方式获得：
  ```javascript
  const filterList = this.player.getFilters();
  ```

  filterList的数据结构如下所示：

  ```
  [
    {
      key: 'filter1',
      name: '滤镜1'
    },{
      key: 'filter2',
      name: '滤镜2',
    }
  ]
  ```

  创建filter clip

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
  参数解释：
  `key`: 滤镜的关键字，参考`filterList`结构。

  将clip加入轨道
  ```javascript
  this.filterTrack.clips = [filterClip1]
  ``` 

  更新播放器

  ```javascript
  this.player.updateData([this.mediaTrack, this.musicTrack, this.filterTrack]);
  ```
  此时你的播放器中拥有了3条轨道，媒体，音乐和滤镜。

  **step3** 添加多个滤镜片段

  和添加多个视频clip类似， 你需要按照step2创建另一个 filterClip2,然后添加进轨道。
  ```javascript
  this.filterTrack.clips = [filterClip1, filterClip2]
  ``` 
  然后更新播放器即可。

  **step4** 修改和删除滤镜

  修改滤镜和前面一样，不再赘述，修改对应的clip属性，然后更新即可。

  删除这里分为2种情况。

  1. 删除滤镜轨道中的滤镜： 你只需在`this.filterTrack.clips`中通过id找到对应的`clip`进行删除即可。

  ```javascript
  this.filterTrack.clips.forEach((item, index) => {
    if(item.id === 'filter_id') {
      this.filterTrack.clips.splice(index, 1)
    }
  })
  ```
  2. 删除整个滤镜轨道： updateData的数组去掉 `this.filterTrack`即可。


  **5.添加特效轨道**

  **step1** 添加特效轨道
  ```javascript
  this.effectTrack = new global['wj-types'].Track({
    type: 'effect',
    clips: []
  });
  ```
  **step2** 添加滤镜片段

  播放器内部提供一些默认特效，可以通过下述方式获得：
  ```javascript
  const effectList = this.player.getEffects();
  ```

  effectList的数据结构如下：
  
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

  创建effect clip

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
  参数解释：

  `key`: 特效的关键字，参考`effectList`的结构。

  将clip加入轨道
  ```javascript
  this.effectTrack.clips = [effectClip1]
  ``` 

  更新播放器

  ```javascript
  this.player.updateData([this.mediaTrack, this.musicTrack, this.filterTrackm, this.effectTrack]);
  ```
  此时你的播放器中拥有了4条轨道，媒体，音乐，滤镜和特效。

  **step3** 添加多个特效片段

  和前面类似， 你需要按照step2创建另一个 effectClip2,然后添加进轨道。
  ```javascript
  this.effectTrack.clips = [filterClip1, filterClip2, filterClip3...]
  ``` 
  然后更新播放器即可。

  **step4** 修改和删除特效

  这里同样分为两种情况，删除特效轨道和轨道中删除clip，处理方式一致。

  
  **6.添加文字轨道**

  **step1** 添加文字轨道
  ```javascript
  this.textTrack1 = new global['wj-types'].Track({
    type: 'text',
    clips: []
  });
  ```
  **step2** 添加文字clip
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
    })
  ```

  参数解释：
  
  `content`: content为文字的内容，style可以定义文字的颜色和背景颜色。

  > 如何控制文字的位置呢？
  >
  > 文字的位置控制逻辑在播放器内部，所以你只需要把文字添加进播放器就可以进行拖拽了，位置信息不用关心，初始化传入的文字统一位于视频的中心位置。
  
  ```javascript
  this.textTrack.clips = [textClip1]
  ```  
  
  当然，你可以在一个轨道添加多个文字，文字clip的section没有重叠。

  ```javascript
  this.textTrack.clips = [textClip1, textClips2, ...]
  ```  
  
  **step3** 删除和更新

  这里重复了，处理方式和前面一样。
  
  **step4** 多个文字共存

  上文提到过在一个轨道中添加多个文字clip的情况，此时各个clip之间的section是不存在交集的，即某一时刻页面最多显示一个文字。假如需要多个文字同时展示的情况，此时需要通过多个文字track实现，每个轨道中只包含一个文字clip。

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

  ... // 依次类推
  ```
  
  创建完文字轨道后，更新播放器即可。
  ```javascript
    this.player.updateData([this.mediaTrack, this.musicTrack, this.filterTrack, this.textTrack1, this.textTrack2]);
  ```
  
  > 特别注意！： 由于小程序限制，文字最多只能存在5个。 可以添加5个文字轨道，一个轨道中一段文字；或者一个轨道中，5段文字，即文字clip总共不能超过5个。


### 2. 照相机: wj-camera

相机组件提供用户拍摄（前置、后置），访问相册增加Clip（图片、视频），展示已选Clip列表，删除Clip（单个删除、整体删除）等基本功能，是Clip的入口组件。

* 使用方式

  step1：配置json文件

  ```json
  {
	    "usingComponents": {
	      "wj-camera": "plugin://myPlugin/wj-camera"
	    }
  }
  ```

  step2：wxml中引入组件

  ```
  <wj-camera bindmediachanged="onMediaChanged" clips="{{clips}}"></wj-camera>
  ```

* 属性

  | 属性名 | 类型 | 默认值               | 说明 | 是否必填 |
  | -------- | ------ | ---------------- | -------- | -------- |
  | settings     | Object  | 参考下方settings 默认值 | 设置 | 否 |
  | clips     | `Array<clip>`  |  []  | 初始Clip，参考下方clip结构 | 否 |
  | bindready | Function |  | 组件加载完成回调 |  |
  | bindmediachanged | Function |  | 选择Clip的回调<br />e.detail = {track: `Array<Track>`} |  |

	**settings 默认值：**
	
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
	    switchDirectionIcon: './images/switch_camera.png' // 切换按钮
	}
	```
	
	**clip结构：**
	
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

* 说明

  * 主界面底部三个操作按钮，分别为：切换摄像头方向、拍摄、跳转相册
  * 拍摄时长受 **小程序平台限制，最大值为 30**
  * 视频Clip数量最大值为5；Clip（图片+视频）数量最大值为9；
  * Clip展示页展示已选择/拍摄Clip，单击Clip右上角的删除按钮可删除单个Clip；单击空白处可删除全部Clip。
  * 小程序平台限制，无法在插件中直接调用` wx.navigateTo `实现页面跳转，只能使用 [navigator组件](https://developers.weixin.qq.com/miniprogram/dev/component/navigator.html) ，故我们预留了一个`slot插槽`供用户实现个性化跳转需求，使用方式如下：

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

### 3. 裁切器: wj-clipper

裁切器组件接收标准的Track数据，根据一定的规则生成Clip的缩略图，绘制到组件中。裁切器通常与上述wj-player组件搭配使用，实现实时的裁切预览功能。

* 使用方式

 step1：配置json文件

  ```json
  {
		"usingComponents": {
		  "wj-clipper": "plugin://myPlugin/wj-clipper"
		}
  }
  ```

  step2：wxml中引入组件

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

* 属性

  | 属性名 | 类型 | 默认值               | 说明 | 是否必填 |
  | -------- | ------ | ------------------------ | -------- | -------- |
  | trackInfo     |  Track  |  null  | Track数据，参考下方说明 | 是 |
  | time | Number | 0 | 当前展示时间，控制时间轴的位置 | 否 |
  | settings     | Object  | 参考下方settings 默认值 | 设置 | 否 |
  | bindthumbdone | Function |  | 缩略图绘制完成事件| 否 |
  | bindthumbtouchstart | Function |  | 缩略图touch start 事件| 否 |
  | bindthumbscroll | Function |  | 缩略图滚动事件 <br>{<br>time: 当前时间轴指向的时间<br>}| 否 |
  | bindtimerollertouchstart | Function |  | 时间轴touch start 事件| 否 |
  | bindtimerollertouchend | Function |  | 时间轴touch end 事件| 否 |
  | bindtimerollermove | Function |  | 时间轴拖动事件（拖动左右手柄，时间轴跟随手柄的位置移动）<br>{<br>time: 当前时间轴指向的时间<br>actionType: 事件触发类型（拖拽时间轴触发：moveRoller、拖拽手柄触发：moveHandler）<br>}| 否 |
  | bindhandlertouchstart | Function |  | 左右手柄touch start 事件| 否 |
  | bindhandlermove | Function |  | 左右手柄拖动事件<br>{<br>startTime: 左手柄代表时间<br>endTime: 右手柄代表时间<br>} | 否 |
  | bindclipped | Function |  | 裁切发生事件 <br>{<br>innerTrackInfo: 裁切后的Track数据<br>time: 当前时间轴指向时间<br>actionType: 事件触发类型（拖拽缩略图触发：scrollThumb、拖拽手柄触发：moveHandler）<br>}| 否 |
  | bindended | Function |  | 时间轴播放到末尾（右手柄位置）事件| 否 |


 **trackInfo 结构：**

 clipper 组件接受的 trackInfo 数据相比于标准的 Track 多了几个属性，如下所示：

 ```
 {
	 innerStartTime: Number, // 裁切区间开始时间
	 innerEndTime: Number, // 裁切区间结束时间
	 scrollStartTime: Number // 缩略图滚动时间（影响最终的 clipped 数据）
 }
 ```

 **settings 默认值：**
	
	```
	{
		clipMaxDuration: 60, // 裁切时长限制（秒）
		mainColor: "rgba(255,88,76)" // 裁切器主题色
	}
	```
	
* 组件实例属性

  | 属性名 | 类型  | 参数 | 说明 |
  | -------- | ---- | --- |-------- |
  | getValidTrackData   | Function  | ` Array<Track>`  |根据 trackInfo 的 innerStartTime、innerEndTime值获取有效的Track数据 |

* 说明
	*   裁切器涉及两个重要概念：缩略图展示区间、裁切区间；
	* 	缩略图展示区间：与clip对象的section属性的值有关，start、end属性决定单个clip展示的缩略图时间区间；
	*  	裁切区间：与trackInfo的innerStartTime、innerEndTime字段的值有关，决定了整个track裁切区间的起始时间；
	* 	通常来讲，裁切是双向的（缩小区间、放大区间），故提供给clipper组件的track数据应该始终为全量数据，即将希望展示到组件中的数据都通过clip的section体现出来，而不仅限于裁切区间展示的数据；
	*  	不要将裁切后的数据传递给clipper组件，除非你真的只想在此基础上继续裁切出更小的区间；
	*   通过 [获取组件实例](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/events.html) 的方式，可以调用组件暴露的 `getValidTrackData` 方法，将裁切区间外的无效数据过滤掉；
	* 	触发 clipped 事件的操作：左右手柄touch-end、缩略图滚动停止；
 	* 	触发 timerollermove 事件的操作：左右手柄move、时间轴move；


### 4. 导出: wj-export

导出组件提供了视频导出的功能，内部复用了wj-player，针对小程序导出进行了专门处理。

* 使用方式

  Step1：配置json文件

  ```
  {
      "usingComponents": {
        "export": "plugin://myPlugin/wj-export"
      }
    }
  ```
  Step2：wxml中引入组件
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
  
  
  
* 属性

  | 属性名            | 类型                          | 默认值 | 说明                                                         | 必填 |
  | ----------------- | ----------------------------- | ------ | ------------------------------------------------------------ | ---- |
  | tracks            | Array<Track>                  | []     | 导出视频的轨道信息                                           | 是   |
  | quality           | Enum('high', 'medium', 'low') | medium | 导出视频质量选项。提供high, medium, low三个选项。<br />以标准16：9视频为例，<br />high导出分辨率为1080\*1920；<br />medium导出分辨率为720\*1280；<br />low导出分辨率为540\*960； | 否   |
  | showloading       | Boolean                       |        | 是否显示默认的导出进度toast，默认false。                     | 否   |
  | watermark         | String                        |        | 集成简易的水印功能。由于小程序对下载文件域名的限制，请将图片先downloadFile到本地，使用本地临时链接。 | 否   |
  | bindready         | Function                      |        | 导出组件加载完成时触发                                       |      |
  | bindexportstart   | Function                      |        | 导出流程开始                                                 |      |
  | bindprogress      | Function                      |        | 导出进度更新<br />e.detail =  {<br />progress: Number<br />} |      |
  | bindexportsuccess | Function                      |        | 导出成功<br />{<br/>	code: 0, //成功<br/>	tempFilePath: 'wxfile://xxx.mp4',<br/>  coverInfo: {<br/>    path: xxx,<br/>    width: 544,<br/>    height: 960<br/>  }, // 封面信息<br/>  video: {<br/>    width: '544', //视频分辨率<br/>	  height: '960',<br/>	  fps: 30, //帧率<br/>  }<br/>	duration: 3000 //单位 ms<br/>} |      |
  | bindexportfail    | Function                      |        | 导出失败<br />{<br />message: String,<br />error: errorStack<br />} |      |
  | bindthumbready    | Function                      |        | 默认封面图生成<br />{<br />path: String,<br />height:1080,<br />width: 720<br />} |      |

  

* 说明

  * 导出组件提供了`slot插槽`以定制导出组件的实际UI，并监听内部冒泡的tap事件以触发导出流程；如果需要手动触发导出流程，可以使用`wx.selectComponent`获取组件实例并调用实例的`start`方法。

    
### 5. 文字编辑: wj-textEditor

文字编辑组件是一个简单的模拟原生输入框的组件，用于向视频中添加文本贴纸。支持动态修改文本的颜色及背景色，提供实时预览功能。

* 使用方式

  step1：配置json文件

  ```json
  {	
    "usingComponents": {
      "wj-textEditor": "plugin://myPlugin/wj-textEditor"
    }
  }
  ```
  step2：wxml中引入组件

  ```
  <wj-textEditor value="{{textValue}}" bindconfirm="onConfirmText"/>
  ```

* 属性

  | 属性名 | 类型 | 默认值  | 备注 | 必填 |
  | -------- | ------ | ------------------------------------------------- | ------ | -------- |
  | value     | String | 空 | 文本内容 | 否 |
  | color     | String | #fff  | 字体颜色，标准css颜色值，默认白色 | 否 |
  | bgColor     | String | transparent | 背景色，标准css颜色值，默认透明 | 否 |
  | colorList     | Array  | 组件默认颜色集合 | [{key: 唯一标识, value: 标准css颜色值}] | 否 |
  | bindconfirm | Function |  | 用户输入完成。<br />e.detail = { value: 文本内容, <br/>color: 文本颜色, <br/>bgColor: 背景色, <br/>showTextBg: 是否显示背景色 } |  |
  | bindclose | Function |  | 用户取消输入 |  |

* 操作说明

  输入文字，点击颜色列表实时更换文本颜色，点击左侧 T 图标实时更换背景颜色。


