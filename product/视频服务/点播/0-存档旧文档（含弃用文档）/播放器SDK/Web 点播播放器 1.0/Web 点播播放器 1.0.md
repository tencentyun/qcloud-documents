## 功能介绍
本文档是介绍腾讯云视频点播服务的网页播放器（Web SDK）的使用说明，它可以帮助腾讯云客户直接使用经过验证的视频播放能力，通过灵活的接口、快速和自有 Web 应用集成，以实现桌面应用播放功能，同时本 SDK 还提供在 Web 端上传视频的能力。

该 SDK 所播放的文件受限于全局防盗链功能定义，详细内容请查看官网 FAQ 安全功能相关说明，该文档面向考虑使用腾讯云视频点播播放器 Web SDK 进行开发并具备 Javascript 语言基础的开发人员。

## 能力支持

#### 播放格式
Web SDK 播放视频格式支持：

| 播放格式    | PC 浏览器环境     | 手机浏览器环境 |
|---------------|----------------------|---------------------|
| HLS（m3u8） | 支持   | 支持   |
| MP4              | 支持   | 支持   |
| FLV               | 不支持 | 不支持 |

>?**Android 系统兼容性问题：**不像 iPhone 上只有一个 Safari 浏览器，Android 上的系统标配浏览器有非常多的实现版本，所以 Android 手机浏览器的兼容是一个业界难题，故此表格中所示的手机浏览器格式支持情况不适用于所有 Android 手机。

#### 上传格式
SDK 上传视频格式支持：

| 标准格式    |   详细格式                                  |
|-------------  | ------------------------------------------|
| 微软格式    | WMV，WM，ASF，ASX                            |
| REAL 格式  | RM, RMVB，RA，RAM                            |
| MPEG 格式 | MPG，MPEG，MPE，VOB，DAT                     |
| 其他格式    |  MOV，3GP，MP4，MP4V，M4V，MKV，AVI，FLV，F4V |

>?**点播平台的转码服务：**由于 MP4 和 HLS（m3u8）是目前在 PC 浏览器和手机浏览器上支持程度相对较好的格式，所以腾讯云的视频点播平台最终会把上传的视频发布为 MP4 和 HLS（m3u8） 格式。

#### 平台兼容
为手机浏览器和 PC 浏览器写两套代码是非常困难的事情，但如果您使用本款播放器，同一段代码可以自动实现 PC 浏览器和手机浏览器的自适应切换，播放器内部会自动区分平台使用最优的播放方案。例如：PC 平台优先使用 Flash 播放器以适应多种视频格式的情况，而手机浏览器上会使用 HTML5 技术实现视频播放。

## 准备工作

#### step 1：开通服务
在 [腾讯云官网](https://cloud.tencent.com/) 注册腾讯云账号，然后开通**点播**服务。

#### step 2：上传文件
点播服务开通之后，进入 [媒资管理](https://console.cloud.tencent.com/vod/media) 就可以上传新的视频文件，因为我们本篇文档主要介绍播放器的使用，所以这一步是为了让您先有个自己的在线视频地址，如果您没有开通点播服务，则无法进入该页面。

#### step 3：获取 fileid 和 APPID
上传完视频之后，您就可以在视频管理页面查到该文件的 ID（fileid） ，与此同时，本款播放器有质量统计功能，在使用之前需要先确认 APPID。
1. 获取 ID（fileid）
在点播视频管理页面，找到您需要获取 ID 的视频，在其操作一栏中单击【管理】，在【基本信息】选项卡下，可查看 ID，如下图所示：
![](https://main.qcloudimg.com/raw/28e0da3aaea156ec0eecb840f2da5350.png)
2. 获取 APPID 
在【腾讯云控制台】>【[账号信息](https://console.cloud.tencent.com/developer)】中查看。

#### step 4：页面准备
在需要播放视频的页面（包括 PC 或 H5）中引入初始化脚本：
```
<script src="//qzonestyle.gtimg.cn/open/qcloud/video/h5/h5connect.js" charset="utf-8"></script>;
```

>?本地文件限制：本地文件是不能用这款播放器播放的，因为有跨域问题，播放器一定要挂 IP 或者域名访问，这也是为什么需要您先上传一个视频文件获取在线播放地址的原因。

## 添加播放器
经过下面两个简单的步骤，您就可以在您的网页上添加一个视频播放器。

#### step 1：添加播放器容器
在需要展示播放器的页面位置加入播放器容器，例如：在 index.html 中加入如下代码（容器 ID 以及宽高都可以自定义）。
```
<div id="id_video_container" style="width:100%; height:auto;"></div>;
```

#### step 2：创建 Player 对象
接下来在页面引入的 Javascript 脚本中创建一个播放器对象，这时将使用播放器的构造函数：
```
var player = new qcVideo.Player("id_video_container", {
    "file_id": "1465197896261041838",
    "app_id": "125132611",
    "width":640,
    "height":480
});
```
该构造函数将会生成一个播放器对象并且根据 file_id 和 app_id 找到对应的视频进行播放，您可以使用播放器对象 player 对播放器进行控制，播放器对象的参数选项 [API 方法总览](#third_video) 有详细介绍。

### 完整实例代码
```
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1" />
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=0, minimum-scale=1.0, maximum-scale=1.0"/>
    <title>点播</title>
</head>
<body>
<div id="id_video_container" style="width:100%; height:auto;"></div>
<script src="//qzonestyle.gtimg.cn/open/qcloud/video/h5/h5connect.js" charset="utf-8"></script>
<script type="text/javascript">
    (function () {
        var player = new qcVideo.Player("id_video_container", {
            "file_id": "1465197896261041838",
            "app_id": "125132611",
            "width":640,
            "height":480
        });
    })()
</script>
</body>
</html>
```

## 更多的情况
#### case 1：有视频地址但是没有 file_id 及app_id 的情况下怎么播放视频？
这时需要用到传视频播放地址的功能，这时不需要传 file_id 及 app_id，JS 用例如下：
```
    var option = {
    "width": 640,
    "height": 480,
    //...可选填其他属性
    "third_video": {
    "urls":{
            20 : "http://208.vod.myqcloud.com/204.mp4"//演示地址，请替换实际地址
        }
    }
};
var player = new qcVideo.Player("id_video_container", option);
```

其中参数 third_video 的 urls 属性是个 Object 可以传多个不同清晰度的视频地址，具体参数说明在 [API 方法总览](#third_video) 中。

>!urls 中至少包含一个视频地址。

#### case 2：如何使用"弹幕"功能?
在播放器初始化完成后调用播放器对象的 addBarrage(barrage) 方法，可以为视频添加弹幕，具体参数请参考 [API 方法总览](#barrage) 的说明，例如，给正在播放的视频添加两条弹幕：

```
var barrage = [
{"type":"content", "content":"hello world", "time":"1"},
{"type":"content", "content":"居中显示", "time":"1", "style":"C64B03;30","position":"center"}
];
player.addBarrage(barrage);
```


>! 弹幕功能仅在前端实现，后台支持请自行开发，弹幕只在 PC Flash 播放器中生效，H5 暂时不具备弹幕功能。

#### case 3：播放结束时做一些操作，如视频推荐，应该怎么做？

使用 listener 参数传入 playStatus 事件的回调函数，当播放状态变更时会调用此函数。具体回调函数参数的说明请参考  [API 总览](#playstatus)。

例如：

```
var option ={
    "file_id":"1465197896261041838",
    "app_id":"125132611",
    "width":800,
    "height":720
    //...可选填其他属性
};
var listener = {
    playStatus: function (status){
        //TODO
        console.log(status);
    }
};
var player = new qcVideo.Player("id_video_container", option, listener);
```

#### case 4：让播放器记住上次观看的时间点，下次从这个时间点继续播放该怎么做？

option 中设置 remember 参数为 1，播放器将会记录该视频最后一次未播放完的的时间点，下次播放会从这个时间点继续播，例如：
```
var option ={
    "file_id":"1465197896261041838",
    "app_id":"125132611",
    "width":800,
    "height":720,
    "remember":1
    //...可选填其他属性
};
var player = new qcVideo.Player("id_video_container", option);
```


#### case 5：如何让播放器在网页尺寸变化时跟着变化尺寸？

使用播放器对象的 resize(width, height) 可以动态修改播放器尺寸。

```
player.resize(640, 480);
```

#### case 6：如何播放在云视频管理里设置了密码的视频？

和播放普通视频一样，SDK 会自动显示输入密码对话框，输入密码后即可播放。


>! 密码功能只对传视频 ID 播放方式有效。

#### case 7：如何生成通过二维码或者链接传播的链接？

 例子（请替换链接中的 appid 和 fileid）：

```
http://play.video.qcloud.com/qrplayer.html?appid=1251769111&fileid=14651978969211156176147&autoplay=0&sw=640&sh=426&$def=20&wmode=transparent
```

```
http://play.video.qcloud.com/iplayer.html?appid=1251769111&fileid=14651978969211156176147&autoplay=0&sw=1800&sh=1200&def=20&wmode=transparent
```

#### case 8：如何指定播放视频的清晰度？

在确认视频拥有该清晰度的情况下，使用 definition 参数指定播放视频的清晰度，适用于视频 ID 和传地址播放两种方式，具体请参考 [参数说明](#definition) 链接，例如：
```
var option ={
    "file_id":"14651978969261415426",
    "app_id":"1251606588",
    "definition":30,
    "width":800,
    "height":700
};

var player = new qcVideo.Player("id_video_container", option);
```

## API方法总览

### 构造函数
```
qcVideo.Player(id, option, listener);
```

**ID**：String，**必选**参数，<span id="constructor"></span>页面放置播放器的容器 ID，可以自由定义；
**option**：Object，**必选**参数。
播放器的参数设置选项，具体选项有：

| 参数                                                   | 类型    | 默认值 | 参数说明                                                                                                                                                                                        |
|--------------------------------------------------------|---------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| file_id                                               | String  | 无     | 用视频 ID 播放方式为**必选**参数，为该点播文件的唯一标识                                                                                                                                              |
| app_id                                                | String  | 无     | 条件同上为**必选**参数，同一个账户下的视频，该参数是相同的                                                                                                                                          |
| width                                                  | Number  | 无     | **必选**，例如：640，设置播放器宽度，单位为像素                                                                                                                                                     |
| height                                                 | Number  | 无     | **必选**，例如：480，设置播放器高度，单位为像素                                                                                                                                                     |
| auto_play                                             | Number  | 0      | 是否自动播放，0：不自动，1：自动播放  <br>**备注：该选项只对 PC 平台 Flash 播放器生效  **                                                                                                                                                  |
| disable_full_screen                                  | Number  | 0      | 是否允许全屏播放，0：支持全屏播放，1：禁用全屏播放       <br>**备注：该选项只对 PC 平台 Flash 播放器生效**                                                                                                                                          |
| disable_drag                                          | Number  | 0      | 是否允许拖动时间轴，0：允许拖拽，1：禁止拖拽         <br> **备注：该选项只对 PC 平台 Flash 播放器生效**                                                                                                                                              |
| stretch_full                                          | Number  | 0      | 是否等比拉伸视频至铺满播放器0：不拉伸，1：拉伸全屏          <br> **备注：该选项只对 PC 平台 Flash 播放器生效   **                                                                                                                                    |
| stop_time                                             | Number  | 无     | 试看功能，例如设置：60，60秒后停止播放，并且触发“playStatus”事件                                                                                                                                |
| remember                                               | Number  | 0      | 是否开启续播功能，0：关闭，1：开启，开启后将会记录这个视频上一次未看完的时间点，下一次继续播放。   <br> **备注：该选项只对 PC 平台 Flash 播放器生效**                                                                                              |
| playbackRate                                           | Number  | 1      | 变速播放，例如设置 2 表示 2 倍速度播放，0.5 表示慢正常速度一倍播放。      <br> **备注：该选项暂时只对 H5 播放器生效 **                                                                                             |
| hide_h5_setting                                      | Boolean | false  | 是否隐藏 H5 的设置按钮，true：隐藏，false：不隐藏                                                                                                                                                 |
| hide_h5_error                                        | Boolean | false  | 是否隐藏 H5 的错误提示， <br> **备注：该选项暂时只对 H5 播放器生效**                                                                                                                                              |
| WMode                                                  | String  | window | Window 模式不支持其他页面元素覆盖在 Flash 播放器上面，如需要可以修改为 opaque 或其他 flash wmode 的参数值。<br>** 备注：该选项只对 PC 平台 Flash 播放器生效**                                                                  |
| stretch_patch                                         | Boolean | false  | 设置为 true 时，支持将开始、暂停、结束时的图片贴片铺满播放器。                                                                                                                                    |
| definition<span id="definition"></span> | Number  | 无     | 可以指定播放视频的清晰度，首先需要视频拥有改清晰度 可选值有： 10、20、30、40、210、220、230、240，具体对应哪种视频可以参考 [third_video](#third_video) 的参数说明。                                                                             |
| videos                                                 | Array   | 无     | 开启防盗链后，可以通过设置 videos 的可访问的视频地址，支持播放器播放；清晰度类型通过 url 与后台查出的 url 前缀匹配得到，详情请查看 [防盗链功能使用指南](https://cloud.tencent.com/doc/product/266/2875)<br> 例如：[`http://xxx.myqcloud.com/xxxyy\_f220.m3u8?**sign**=xxx`，<br>...<br>]                                                                                                                                                                                               |
| third_video <span id="third_video"></span>                  | Object  | 无     | 该选项只用于视频文件播放地址的情形<br>参数例子：{<br>‘duration’: 20 , //视频时长（单位秒），可选参数，没有传的情况下在视频加载 MetaData 后自动更新视频时长。<br>**注意：如果是播放 mp4，这个时长数据是必须的**<br>‘urls’ : { //(**至少包含一个地址，注意对应视频格式**)  <br>　　　10 : “mp4 手机视频地址”, <br>　　　20 :“mp4 标清视频地址”,<br>　　　30 : “mp4 高清视频地址”, <br>　　　40 : “mp4 超清视频地址”, <br>　　　210 : “hls 手机视频地址”, <br>　　　220 : “hls 标清视频地址”, <br>　　　230 :“hls 高清视频地址”, <br>　　　240 : “hls 超清视频地址” <br>　　}<br>}<br>**备注：如果在 Chrome 等 PC 浏览器中模拟移动设备，需要有 mp4 视频地址才可以播放**|

**listener**：Object，可选参数，播放状态变化回调函数列表。

| 函数名称                                                 | 类型     | 说明   |
|----------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------|
| fullScreen                                               | function | 全屏/退出全屏时触发，回调函数的参数 isFullScreen：Boolean <br>返回值： true全屏，false 退出全屏 <br>例子：```function(isFullScreen){ ... }```  <br>**备注：该事件只对 PC 平台 Flash 播放器生效**  |
| playStatus<span id="playstatus" class="anchor"></span> | function | 播放状态变更时触发，回调函数的参数 status：String <br>返回值：ready：“播放器已准备就绪”，seeking：“搜索”，suspended：“暂停”，playing：“播放中” ， playEnd：“播放结束”，stop：“试看结束触发” ，error：“H5 播放出现错误时触发”  <br>例子：function(status, msg){ ... }   |
| dragPlay                                                 | function | 拖动播放位置变化时触发 ；second：Number  <br>返回值：拖动播放的位置（单位秒） <br>例子： ```function(second){ ... }```  <br> **备注：该事件只对 PC 平台 Flash 播放器生效 **   |


### 获取参数和状态

构造函数返回的播放器对象具有以下获取参数和状态的方法：

|   方法名              |         返回值                                                   |       说明                       |
|----------------|------------------------------------------------------------|-----------------------------|
| getVolume      | Number，取值范围（0 到 1）                                 | 获取当前音量                |
| getDuration    | Number，单位秒                                             | 获取当前视频总时长          |
| getCurrentTime | Number，单位秒                                             | 获取当前播放位置            |
| isSeeking      | Boolean，true 为”加载中”                                  | 当前播放状态是否 “加载中”   |
| isSuspended    | Boolean，true 为”暂停中”                                  | 当前播放状态是否 “暂停中”   |
| isPlaying      | Boolean，true 为”播放中”                                  | 当前播放状态是否 “播放中”   |
| isPlayEnd      | Boolean，true 为”播放结束”                                | 当前播放状态是否 “播放结束” |
| getWidth       | Number(int)                                                | 获取当前播放器宽度          |
| getHeight      | Number(int)                                                | 获取当前播放器高度          |
| getClarity     | Number(int) ( 1：”手机”， 2：“标清”， 3：“高清”， 4：“超清”)      | 获取当前视频的清晰度        |
| getAllClaritys | Array&lt;int&gt; ( 1：”手机”， 2：“标清”， 3：“高清”， 4：“超清”) | 获取当前视频全部的清晰度    |

### 设置和动作

构造函数返回的播放器对象具有以下设置方法：

| 方法                                                          | 说明                                                                                                                 |
|---------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| resize(width,height)                                          | 参数：width :int；height :int                                            <br>功能：设置当前播放器宽度高度                                         <br>返回：无                                                                                                              |
| play(second)                                                  | 参数：second：int 单位秒                                                  <br>功能：开始播放，可以设置开始播放指定时间点 <br>返回：int [返回码](https://cloud.tencent.com/document/product/267/13506)<br>备注：在传视频地址播放的情况下，second 只能传 空值 或者 0                                                               |
| pause()                                                       | 功能：暂停当前播放的视频 <br>返回：int [返回码](https://cloud.tencent.com/document/product/267/13506)                                                                                     |
| resume()                                                      | 功能：恢复播放视频<br>返回：int [返回码](https://cloud.tencent.com/document/product/267/13506)                                                                                     |
| setClarity(clarity)                                           | 参数：clarity：int 清晰度 取值范围 （1：”手机”，2：”标清”，3：”高清”，4：”超清”）<br>功能：更换视频清晰度 <br>返回：int [返回码](https://cloud.tencent.com/document/product/267/13506)                            <br>注意：clarity 指定的清晰度，请确保当前视频具备该清晰度，否则将按播放器默认规则选择一个清晰度播放                       |
| changeVideo(opt)                                              | 参数： opt Object，包含将要播放的视频的基本信息和构造函数第二个参数基本一致，具体参考 [构造函数说明](#constructor)<br>功能：动态更换视频  <br>返回：int [返回码](https://cloud.tencent.com/document/product/267/13506) |
| addBarrage(barrage) <span id="barrage"></span>| 参数：barrage：Array 弹幕信息   <br> \[{   <br>"type":"content", //消息类型，content:普通文本（**必选**）  <br>"content":"hello world", //文本消息 （**必选**）  <br>"time":"1.101",//单位秒 ，表示距离当前调用添加字幕的时间多久后，开始显示该条字幕（**必选**）   <br>"style": "C64B03;35",// 分号分割，第一项颜色值，第二项字体大小（可选） <br>"postion":"center" //固定位置 <br>center: 居中，bottom: 底部， up: 顶上 (可选) }, ... \]  <br>功能：添加弹幕     <br>返回：int [返回码](https://cloud.tencent.com/document/product/267/13506) <br> 备注：**弹幕仅在前端实现，后台功能请自行开发，该功能只在 PC Flash 播放器中生效**                                                                                |
| closeBarrage()                                                | 功能：关闭弹幕，关闭后重新调用 addBarrage 可开启弹幕。 <br>返回：int [返回码](https://cloud.tencent.com/document/product/267/13506)  <br> 备注：**弹幕仅在前端实现，后台功能请自行开发，该功能只在 PC Flash 播放器中生效**    |


这些设置方法的统一返回码是：
  
| 错误码<span id="errorcode"></span> | 含义 |
|---------|---------|
| 200 | 操作成功 | 
| 0  | 播放器未完全初始化 | 
| -1 | 动态更换失败视频，缺少必要参数 | 
| -2 | 未知操作命令 | 
| -3 | 播放时间超出有效播放范围 | 


## 视频文件上传功能

用户可以使用点播 Web SDK 上传视频，以帮助腾讯云视频用户通过 Web 上传视频文件，该 SDK 当前支持 HTML5 上传（不支持 HTML5 的浏览器暂不支持上传）。

具体操作方法请查看 [云点播 Web 上传 SDK](http://video.qcloud.com/sdk/upload.html)。
