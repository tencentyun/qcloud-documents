## 功能介绍

本文档是介绍腾讯云视频点播服务的网页播放器（Web SDK）的使用说明，它可帮助腾讯云客户直接使用经过验证的视频播放能力，通过灵活的接口，快速同自有Web应用集成，以实现桌面应用播放功能。同时本SDK还提供在WEB端上传视频的能力。

该SDK所播放的文件受限于全局防盗链功能定义。详细内容请查看官网FAQ安全功能相关说明。

该文档面向考虑使用腾讯云视频点播播放器Web SDK进行开发并具备Javascript语言基础的开发人员。


## 能力支持

### 播放格式
WEB SDK播放视频格式支持：

| 播放格式    | PC浏览器环境     | 手机浏览器环境 |
|---------------|----------------------|---------------------|
| HLS（m3u8） | 支持   | 支持   |
| MP4              | 支持   | 支持   |
| FLV               | 不支持 | 不支持 |

> **Android 系统兼容性问题**
> 不像iPhone上只有一个Safari浏览器，Android上的系统标配浏览器有非常多的实现版本，所以Android手机浏览器的兼容是一个业界难题，故此表格中所示的手机浏览器格式支持情况比**不适用于所有Android手机**。

 
### 上传格式
SDK上传视频格式支持：

| 标准格式    |   详细格式                                  |
|-------------  | ------------------------------------------|
| 微软格式    | WMV，WM，ASF，ASX                            |
| REAL格式  | RM, RMVB，RA，RAM                            |
| MPEG格式 | MPG，MPEG，MPE，VOB，DAT                     |
| 其他格式    |  MOV，3GP，MP4，MP4V，M4V，MKV，AVI，FLV，F4V |

> **点播平台的转码服务**
> 由于MP4和HLS（m3u8） 是目前在PC浏览器和手机浏览器上支持程度相对较好的格式，所以腾讯云的视频点播平台最终会把上传的视频发布为 MP4和HLS（m3u8） 格式。

### 平台兼容
为手机浏览器和PC浏览器写两套代码是非常吃力的事情，但如果您使用本款播放器，同一段代码可以自动实现PC浏览器和手机浏览器的自适应切换，播放器内部会自动区分平台使用最优的播放方案。例如：PC平台优先使用Flash 播放器以适应多种视频格式的情况，而手机浏览器上会使用HTML5技术实现视频播放。

## 准备工作

### step1 :开通服务
首先您需要注册一个腾讯云账号，然后开通**点播**服务。

### step2 :上传文件
点播服务开通之后，进入 [点播视频管理](http://console.cloud.tencent.com/video/videolist)就可以上传新的视频文件了，因为我们本篇文档主要介绍播放器的使用，所以这样做是为了让您先有个自己的在线视频地址。如果您没有开通点播服务，这个页面是进不去的。


### step3 :获取ID
上传完视频之后，您就可以视频管理页面查到文件的id了，这个是播放器播放视频的最基本信息，与此同时，本款播放器有质量统计功能，在使用之前需要先确认APPID，您的APPID也可以在视频管理页面查看到。

 下图中的两个ID，左边一个是视频文件的ID，另一个就是您的APPID了。
![](//mc.qcloudimg.com/static/img/c181f36d49bfa8532057a32c12b12269/image.jpg)

### step4 :页面准备
在需要播放视频的页面（包括PC或H5）中引入初始化脚本：
```
<script src="//qzonestyle.gtimg.cn/open/qcloud/video/h5/h5connect.js" charset="utf-8"></script>;
```

> **本地文件限制**
>**<font color="red"> 本地文件是不能用这款播放器播放的，因为有跨域问题，播放器一定要挂IP或者域名访问，这也是为什么需要您先上传一个视频文件获取在线播放地址的原因。</font>**

## 添加播放器
经过下面两个简单的步骤，您就可以在您的网页上添加一个视频播放器了。

### step 1 :添加播放器容器
 在需要展示播放器的页面位置加入播放器容器，例如：在index.html中加入如下代码（容器id以及宽高都可以自定义）
```
<div id="id_video_container" style="width:100%; height:auto;"></div>;
```

### step 2 :创建Player 对象
 接下来在页面引入的Javascript脚本中，创建一个播放器对象，这时将使用播放器的构造函数
```
var player = new qcVideo.Player("id_video_container", {
    "file_id": "1465197896261041838",
    "app_id": "125132611",
    "width":640,
    "height":480
});
```
该构造函数将会生成一个播放器对象，并且根据file\_id和app\_id找到对应的视频进行播放，您可以使用播放器对象player 对播放器进行控制。播放器对象的参数选项下方API方法总览有详细介绍。

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
### case 1 :有视频地址但是没有file\_id 及app\_id的情况下怎么播放视频？
这时需要用到传视频播放地址的功能，这时不需要传file\_id 及app\_id。JS用例如下:
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

其中参数third\_video的 urls属性是个Object 可以传多个不同清晰度的视频地址，具体参数说明在API方法总览中，[直达链接](#third_video)。

>备注：urls 中至少包含一个视频地址

### case 2 :如何使用"弹幕"功能?
在播放器初始化完成后，调用播放器对象的addBarrage(barrage) 方法，可以为视频添加弹幕。具体参数[参考API方法总览](#barrage)的说明。

例子：给正在播放的视频添加两条弹幕

```
var barrage = [
{"type":"content", "content":"hello world", "time":"1"},
{"type":"content", "content":"居中显示", "time":"1", "style":"C64B03;30","position":"center"}
];
player.addBarrage(barrage);
```

> 备注：<font color="red">弹幕功能仅在前端实现，后台支持请自行开发。弹幕只在PC Flash播放器中生效，H5暂时不具备弹幕功能</font>

### case 3 :播放结束时做一些操作，如视频推荐，应该怎么做？

使用listener参数，传入playStatus事件的回调函数。当播放状态变更时，会调用此函数。具体回调函数参数的说明参考API总览，[直达链接](#playstatus)

例子：

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

### case 4 :让播放器记住上次观看的时间点，下次从这个时间点继续播放该怎么做？

option中设置remember参数为1，播放器将会记录该视频最后一次未播放完的的时间点，下次播放会从这个时间点继续播。

例子：
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


### case 5 :如何让播放器在网页尺寸变化时跟着变化尺寸

使用播放器对象的resize(width, height)，可以动态修改播放器尺寸。

```
player.resize(640, 480);
```

### case 6 :如何播放在云视频管理里设置了密码的视频？

和播放普通视频一样，SDK会自动显示输入密码对话框，输入密码后即可播放。

> 备注：密码功能只对传视频ID播放方式有效。

### case 7 :如何生成通过二维码或者链接传播的链接？

 例子（请替换链接中的appid和fileid）：

[http://play.video.qcloud.com/qrplayer.html?appid=1251769111&fileid=14651978969211156176147&autoplay=0&sw=640&sh=426&\$def=20&wmode=transparent](http://play.video.qcloud.com/qrplayer.html?appid=1251769111&fileid=14651978969211156176147&autoplay=0&sw=640&sh=426&$def=20&wmode=transparent) …

[http://play.video.qcloud.com/iplayer.html?appid=1251769111&fileid=14651978969211156176147&autoplay=0&sw=1800&sh=1200&def=20&wmode=transparent](http://play.video.qcloud.com/iplayer.html?appid=1251769111&fileid=14651978969211156176147&autoplay=0&sw=1800&sh=1200&def=20&wmode=transparent) …

### case 8 :如何指定播放视频的清晰度？

在确认视频拥有该清晰度的情况下，使用definition参数指定播放视频的清晰度，适用于视频ID和传地址播放两种方式。[参数说明链接](#definition)

例子：
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

### 1.构造函数
```
qcVideo.Player(id, option, listener);
```

**id**: String ; <font color="red">必选</font>参数 ;<span id="constructor"></span>
页面放置播放器的容器ID，可以自由定义。

**option**: Object ; <font color="red">必选</font>选参数 ;
播放器的参数设置选项，具体选项有:

| 参数                                                   | 类型    | 默认值 | 参数说明                                                                                                                                                                                        |
|--------------------------------------------------------|---------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| file\_id                                               | String  | 无     | 用视频ID播放方式为<font color="red">必选</font>参数，为该点播文件的唯一标识                                                                                                                                              |
| app\_id                                                | String  | 无     | 条件同上为<font color="red">必选</font>参数，同一个账户下的视频，该参数是相同的                                                                                                                                          |
| width                                                  | Number  | 无     | <font color="red">必选</font>，例如：640，设置播放器宽度，单位为像素                                                                                                                                                     |
| height                                                 | Number  | 无     | <font color="red">必选</font>，例如：480，设置播放器高度，单位为像素                                                                                                                                                     |
| auto\_play                                             | Number  | 0      | 是否自动播放，0: 不自动，1: 自动播放  <br> <font color="red">备注：该选项只对PC平台Flash播放器生效</font>                                                                                                                                                         |
| disable\_full\_screen                                  | Number  | 0      | 是否允许全屏播放，0: 支持全屏播放，1: 禁用全屏播放       <br> <font color="red">备注：该选项只对PC平台Flash播放器生效</font>                                                                                                                                          |
| disable\_drag                                          | Number  | 0      | 是否允许拖动时间轴，0: 允许拖拽，1: 禁止拖拽         <br> <font color="red">备注：该选项只对PC平台Flash播放器生效</font>                                                                                                                                              |
| stretch\_full                                          | Number  | 0      | 是否等比拉伸视频至铺满播放器0: 不拉伸,1: 拉伸全屏          <br> <font color="red">备注：该选项只对PC平台Flash播放器生效</font>                                                                                                                                        |
| stop\_time                                             | Number  | 无     | 试看功能，例如设置：60，60秒后停止播放，并且触发“playStatus”事件                                                                                                                                |
| remember                                               | Number  | 0      | 是否开启续播功能，0：关闭，1：开启，开启后将会记录这个视频上一次未看完的时间点，下一次继续播放。   <br> <font color="red">备注：该选项只对PC平台Flash播放器生效</font>                                                                                              |
| playbackRate                                           | Number  | 1      | 变速播放，例如设置2表示2倍速度播放，0.5表示慢正常速度一倍播放。      <br> <font color="red">备注：该选项暂时只对H5播放器生效  </font>                                                                                                  |
| hide\_h5\_setting                                      | Boolean | false  | 是否隐藏H5的设置按钮，true：隐藏，false：不隐藏                                                                                                                                                 |
| hide\_h5\_error                                        | Boolean | false  | 是否隐藏H5的错误提示， <br> <font color="red">备注：该选项暂时只对H5播放器生效  </font>                                                                                                                                                     |
| WMode                                                  | String  | window | Window模式不支持其他页面元素覆盖在flash播放器上面，如需要可以修改为opaque 或其他flash wmode的参数值。<br> <font color="red">备注：该选项只对PC平台Flash播放器生效  </font>                                                                  |
| stretch\_patch                                         | Boolean | false  | 设置为true时，支持将开始、暂停、结束时的图片贴片铺满播放器。                                                                                                                                    |
| definition<span id="definition"></span> | Number  | 无     | 可以指定播放视频的清晰度，首先需要视频拥有改清晰度 可选值有： 10、20、30、40、210、220、230、240，具体对应哪种视频可以参考[third\_video](#third_video)的参数说明。                                                                             |
| videos                                                 | Array   | 无     | 开启防盗链后，可以通过设置videos的可访问的视频地址，支持播放器播放；清晰度类型通过url与后台查出的url前缀匹配得到。详情请查看[防盗链功能使用指南](https://cloud.tencent.com/doc/product/266/2875)<br> 例如：\[`http://xxx.myqcloud.com/xxxyy\_f220.m3u8?**sign**=xxx`，<br>...<br>\]                                                                                                                                                                                               |
| third\_video <span id="third_video"></span>                  | Object  | 无     | 该选项只用于视频文件播放地址的情形<br>参数例子：{<br>‘duration’: 20 , //视频时长(单位秒)，可选参数，没有传的情况下在视频加载MetaData后自动更新视频时长。<br><font color="red">注意：如果是播放mp4，这个时长数据是必须的</font><br>‘urls’ : { //(<font color="red">至少包含一个地址，注意对应视频格式</font>)  <br>　　　10 : “mp4手机视频地址”, <br>　　　20 :“mp4标清视频地址”,<br>　　　30 : “mp4高清视频地址”, <br>　　　40 : “mp4超清视频地址”, <br>　　　210 : “hls手机视频地址”, <br>　　　220 : “hls标清视频地址”, <br>　　　230 :“hls高清视频地址”, <br>　　　240 : “hls超清视频地址” <br>　　}<br>}<br> <font color="red">备注：如果在 Chrome 等PC浏览器中模拟移动设备，需要有 mp4 视频地址才可以播放。  </font>|

**listener** : Object ; 可选参数 ; 播放状态变化回调函数列表

| 函数名称                                                 | 类型     | 说明   |
|----------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------|
| fullScreen                                               | function | 全屏/退出全屏时触发，回调函数的参数 isFullScreen:Boolean <br>返回值： true全屏 ; false 退出全屏 <br>例子：```function(isFullScreen){ ... }```  <br> <font color="red">备注：该事件只对PC平台Flash播放器生效  </font>  |
| playStatus<span id="playstatus" class="anchor"></span> | function | 播放状态变更时触发，回调函数的参数 status：String <br>返回值：ready: “播放器已准备就绪”,seeking:”搜索”, suspended:”暂停”, playing:”播放中” , playEnd:”播放结束” , stop: “试看结束触发” , error: “h5播放出现错误时触发”  <br>例子：function(status, msg){ ... }   |
| dragPlay                                                 | function | 拖动播放位置变化时触发 ； second：Number  <br>返回值：拖动播放的位置（单位秒） <br>例子： ```function(second){ ... }```  <br> <font color="red">备注：该事件只对PC平台Flash播放器生效  </font>  |


### 2.获取参数和状态

构造函数返回的播放器对象具有以下获取参数和状态的方法

|   方法名              |         返回值                                                   |       说明                       |
|----------------|------------------------------------------------------------|-----------------------------|
| getVolume      | Number，取值范围（0 到 1）                                 | 获取当前音量                |
| getDuration    | Number，单位秒                                             | 获取当前视频总时长          |
| getCurrentTime | Number，单位秒                                             | 获取当前播放位置            |
| isSeeking      | Boolean ; true 为”加载中”                                  | 当前播放状态是否 “加载中”   |
| isSuspended    | Boolean ; true 为”暂停中”                                  | 当前播放状态是否 “暂停中”   |
| isPlaying      | Boolean ; true 为”播放中”                                  | 当前播放状态是否 “播放中”   |
| isPlayEnd      | Boolean ; true 为”播放结束”                                | 当前播放状态是否 “播放结束” |
| getWidth       | Number(int)                                                | 获取当前播放器宽度          |
| getHeight      | Number(int)                                                | 获取当前播放器高度          |
| getClarity     | Number(int) ( 1:”手机”, 2:“标清”, 3:“高清”, 4:“超清”)      | 获取当前视频的清晰度        |
| getAllClaritys | Array&lt;int&gt; ( 1:”手机”, 2:“标清”, 3:“高清”, 4:“超清”) | 获取当前视频全部的清晰度    |

### 3.设置和动作

构造函数返回的播放器对象具有以下设置方法

| 方法                                                          | 说明                                                                                                                 |
|---------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| resize(width,height)                                          | 参数：width :int；height :int                                            <br>功能：设置当前播放器宽度高度                                         <br>返回：无                                                                                                              |
| play(second)                                                  | 参数：second：int单位秒                                                  <br>功能：开始播放，可以设置开始播放指定时间点 <br>返回：Int [返回码](#errorcode)<br>备注：在传视频地址播放的情况下，second只能传 空值 或者0                                                               |
| pause()                                                       | 功能：暂停当前播放的视频 <br>返回：Int [返回码](#errorcode)                                                                                     |
| resume()                                                      | 功能：恢复播放视频<br>返回：Int [返回码](#errorcode)                                                                                     |
| setClarity(clarity)                                           | 参数：clarity：int 清晰度 取值范围 （1：”手机”,2：”标清”,3：”高清”,4：”超清”）<br>功能：更换视频清晰度 <br>返回：Int [返回码](#errorcode)                            <br>注意：clarity指定的清晰度，请确保当前视频具备该清晰度，否则将按播放器默认规则选择一个清晰度播放                       |
| changeVideo(opt)                                              | 参数： opt Object ; 包含将要播放的视频的基本信息，和构造函数第二个参数基本一致，具体参考[构造函数说明](#constructor); <br>功能：动态更换视频  <br>返回：Int [返回码](#errorcode) |
| addBarrage(barrage) <span id="barrage"></span>| 参数：barrage：Array 弹幕信息   <br> \[{   <br>"type":"content", //消息类型 ,content:普通文本 <font color="red">(必选)  </font>   <br>"content":"hello world", //文本消息 <font color="red">(必选)  </font>  <br>"time":"1.101",//单位秒 ，表示距离当前调用添加字幕的时间多久后，开始显示该条字幕 <font color="red">(必选)  </font>   <br>"style": "C64B03;35",// 分号分割，第一项颜色值，第二项字体大小 (可选) <br>"postion":"center" //固定位置 <br>center: 居中，bottom: 底部， up: 顶上 (可选) }, ... \]  <br>功能：添加弹幕     <br>返回：Int [返回码](#errorcode) <br> 备注：<font color="red">弹幕仅在前端实现，后台功能请自行开发。该功能只在PC Flash播放器中生效</font>                                                                                   |
| closeBarrage()                                                | 功能：关闭弹幕，关闭后重新调用addBarrage可开启弹幕。 <br>返回：Int [返回码](#errorcode)  <br> 备注：<font color="red">弹幕仅在前端实现，后台功能请自行开发。该功能只在PC Flash播放器中生效</font>                                                                                      |
这些设置方法的统一返回码是：
  
| 错误码<span id="errorcode"></span> | 含义 |
|---------|---------|
| 200 | 操作成功 | 
| 0  | 播放器未完全初始化 | 
| -1 | 动态更换失败视频，缺少必要参数 | 
| -2 | 未知操作命令 | 
| -3 | 播放时间超出有效播放范围 | 


## 视频文件上传功能

用户可以使用点播Web SDK上传视频，以帮助腾讯云视频用户通过Web上传视频文件。

该SDK当前支持HTML5上传（不支持HTML5的浏览器暂不支持上传）

具体操作方法请阅：[http://video.qcloud.com/sdk/upload.html](http://video.qcloud.com/sdk/upload.html)



## 问题排查

### 错误码列表

SDK使用过程中出现的异常code对照表，如遇到未在列表中的异常code，请联系我们的客服，客服会安排工程师进行解决。

| Code  | 说明               |
|-------|---------------------|
| 1003  | 密码错误         |
| 10000 | 请求超时(拉取播放器配置信息与视频信息超时，请检查网络重试，超时时间为10s)        |
| 10001 | 数据解析失败(拉取播放器配置信息与视频信息获取到的数据解析失败，可能是网络问题或者服务器异常)        |
| 10002 | 连接超时，请稍后再试(拉取播放器配置信息与视频信息失败，可能是网络问题或者服务器异常)        |
| 10008 | APPID或 File ID错误 |
| 11044 | 缺少APPID     |
| 11045 | 缺少File ID     |
| 11046 | 缺少密码        |


### 常见问题

* **为什么H5播放视频拉伸变形了？**

    解答：H5并不具备拉伸视频的能力，请检查播放器的容器宽高是否设置正确

* **QQ浏览器显示下载视频，怎么屏蔽？**

    解答：手机QQ浏览器的内核限制，JS无法干预，同样在UC等浏览器的内核也提供了自动嗅探视频提供下载的功能。需要联系浏览器开发商进行关闭。

* **QQ浏览器下无法在盖住视频**

    解答：浏览器接管了H5的视频播放功能，X5内核视频播放使用了自研的播放器，考虑用户体验，浏览器使用了统一的播放界面。相关信息参考[QQ浏览器文档说明](http://x5.tencent.com/guide?id=2009)
		
* **在调用isPlaying()等方法时没有获取到正确的状态信息**

	解答：在移动端的某些浏览器和webview中，播放视频会被浏览器自带的内核接管，sdk将无法获得正确的播放状态。

* **设置了自动播放，但在移动端无法自动播放？**
	
	解答：目前大部分手机浏览器由于数据流量等原因，默认不自动加载媒体文件，播放视频时需要用户触发操作。
	
* **iOS系统下视频自动全屏播放**

	解答：iOS系统由于webkit设置原因，默认视频全屏播放，如果您的视频需要在APP内实现内联播放，可以设置webkit-playsinline属性。目前iOS10以下版本的Safari无法禁止视频自动全屏。

* **为什么在 PC Chrome 中Flash播放器会有两个播放按钮？**

	解答：从Chrome 42版本开始将不再自动播放Flash, 只对主要的Flash内容进行自动播放，其它的Flash内容将被暂停播放，除非用户决定去手动点开它。
