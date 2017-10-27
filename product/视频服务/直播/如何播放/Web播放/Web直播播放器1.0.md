## 功能介绍

腾讯云视频直播播放器Web SDK解决方案，可帮助腾讯云视频用户直接使用经过验证的视频播放能力，通过灵活的接口，快速同自有Web应用集成，以实现桌面应用播放功能。同时SDK提供在WEB端上传视频的能力。<br>
该SDK所播放的文件受限于全局防盗链功能定义。详细内容请查看官网FAQ安全功能相关说明。<br>
该文档面向考虑使用腾讯云视频直播播放器Web SDK进行开发并具备Javascript语言基础的开发人员。



## 格式支持


### 播放格式
WEB SDK直播视频格式支持：

|播放格式    | PC浏览器   | 移动端浏览器 |
|-------------|------|--------|
| HLS（m3u8） | 支持 | 支持   |
| RTMP        | 支持 | 不支持 |
| FLV         | 支持 | 不支持   |

> **Android 系统兼容性问题**
> 不像iPhone上只有一个Safari浏览器，Android上的系统标配浏览器有非常多的实现版本，所以Android手机浏览器的兼容是一个业界难题，故此表格中所示的手机浏览器格式支持情况比**不适用于所有Android手机**。


## 准备工作

### Step 1：开通服务
注册腾讯云帐号，并开通**直播**服务
### Step 2：创建频道
进入直播管理控制台并创建直播频道<br>[直播视频管理](https://console.cloud.tencent.com/live)
### Step 3：获取ID
您可以在直播管理控制台查找到直播频道并对该频道进行管理。在控制界面您可以找到app_id。在**基础设置**中，可以查询到该频道的频道id。

![](//mc.qcloudimg.com/static/img/c891d20153fe9e46e1647bd7494ab021/image.png)

### Step 4：页面准备
在需要播放视频的页面（包括PC或H5）中引入初始化脚本


```
<script src="//qzonestyle.gtimg.cn/open/qcloud/video/live/h5/live_connect.js" charset="utf-8"></script>;
```



>注意事项：**<font color="red">播放页面需要挂ip或域名访问，如若直接打开本地静态页面将无法播放</font>**

> 备注：另外可以通过服务端API获取频道ID和APPID，[参考文档链接](https://cloud.tencent.com/doc/api/258/4714)


## API 基础使用方法

### Step 1：添加播放器容器

 在需要展示播放器的页面位置加入播放器容器<span class="anchor" id="step1"><span id="basic_use"></span>

 例如：在index.html中加入如下代码
```
<div id="id_video_container" style="width:100%; height:auto;"></div>
```
容器id以及宽高都可以自定义。

### Step 2：创建Player 对象

接下来在页面底部引入的Javascript脚本中，创建一个播放器对象，这时将使用播放器的构造函数
```
var player = new qcVideo.Player("id_video_container", {
"channel_id": "16093104850682282611",
"app_id": "1251783441",
"width" : 480,
"height" : 320
});
```
调用构造函数将会生成一个播放器对象，并且根据channel\_id和app\_id找到对应的直播视频流进行播放。如果没有channel\_id和app\_id，您也可以使用直播地址的形式进行播放，具体示例如[API使用案例中的case3](#case3)。您可以使用播放器对象player 对播放器进行控制。播放器对象的参数选项下方API方法总览有详细介绍。

### 完整实例代码
```
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1" />
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=0, minimum-scale=1.0, maximum-scale=1.0"/>
    <title>直播</title>
</head>
<body>
<div id="id_video_container" style="width:100%; height:auto;"></div>
<script src="//qzonestyle.gtimg.cn/open/qcloud/video/live/h5/live_connect.js" charset="utf-8"></script>
<script type="text/javascript">
    (function () {
        var player = new qcVideo.Player("id_video_container", {
            "channel_id": "16093104850682282611",
            "app_id": "1251783441",
            "width" : 480,
            "height" : 320
        });
    })()
</script>
</body>
</html>
```

## API 使用案例

>说明：使用API需先完成[第4部分API基础使用方法](#basic_use)中的[step1](#step1)部分，添加播放器容器完成后再进行API使用

### Case 1：在PC或移动端（H5）中播放直播视频

**直播SDK在PC和H5中的使用方式是一样的，SDK会检测平台，自动选择最优的播放方案**。例如在PC平台，SDK会优先使用Flash 播放器以适应多种视频格式的情况（需要flash版本高于10，否则将提示升级flash），而在移动端H5则会使用video标签进行播放（如果浏览器不支持H5，则提示使用QQ浏览器）。SDK同时支持传频道ID或视频文件地址的方式播放，
> 备注：两种播放方式不能混合使用。

### Case 2：使用频道ID播放视频
```
var option = {
"channel_id": "16093425727656143421",
"app_id": "1251132611",
"width" : 480,
"height" : 320

//...可选填其他属性
};

var player = new qcVideo.Player("id_video_container", option);
```
**注意：使用频道ID播放视频不支持直播码的方式**
### Case 3：使用直播视频地址播放视频 
如果没有app_id及channel_id，播放器也支持使用直播视频地址播放视频。<span class="anchor" id="case3">
```
var option = {
"live_url" : "http://2157.liveplay.myqcloud.com/2157_358535a.m3u8",
"live_url2" : "http://2000.liveplay.myqcloud.com/live/2000_2a1.flv",
"width" : 480,
"height" : 320

//...可选填其他属性
};

var player = new qcVideo.Player("id_video_container", option);
```

> 备注：最多支持传入两个播放地址，live\_url，live\_url2 ；如果这两个地址都传了，那么会按平台支持最好的一个地址选择进行播放。例如： 当前环境是pc，那么会优先选择其中为rtmp或flv的格式；当前环境为手机H5，会优先选择 hls格式进行播放。

### Case 4：如何使用"弹幕"功能?
在播放器初始化完成后，调用播放器对象的addBarrage(barrage) 方法，可以为视频添加弹幕。具体参数参考API方法总览的说明。

例子：给正在播放的视频添加两条弹幕

```
var barrage = [
{"type":"content", "content":"hello world", "time":"1"},
{"type":"content", "content":"居中显示", "time":"1", "style":"C64B03;30","position":"center"}
];
player.addBarrage(barrage);
```
>备注：<font color="red">弹幕功能仅在前端实现，后台支持请自行开发。弹幕只在PC Flash播放器中生效，H5暂时不具备弹幕功能</font>


##  API 方法总览

### 1. 构造函数

```
qcVideo.Player(id, option, listener);
```

 **id**: String ;  <font color="red">必选</font>参数; 页面放置播放器的容器ID，可以自由定义。

  **option**: Object ; <font color="red">必选</font>参数; 播放器的参数可设置选项，具体选项：

| 参数             | 类型   | 默认值 | 参数说明   |
|------------------|--------|--------|---------------------------------------------------------------------------------------------------|
| channel\_id      | String | 无     | 用直播视频ID播放方式为<font color="red">必选</font>参数                                                                    |
| app\_id          | String | 无     | 条件同上为<font color="red">必选</font>参数，同一个账户下的视频，该参数是相同的                                            |
| width            | Number | 无     | <font color="red">必选</font>，例如：640，设置播放器宽度，单位为像素                                                       |
| height           | Number | 无     | <font color="red">必选</font>，例如：480，设置播放器高度，单位为像素                                                       |
| cache\_time      | Number | 0.3    | 直播画面开始播放前，最大缓存时间 ; 这个属性可避免有效下行带宽不足导致免rtmp直播卡顿的情况(可选参数)<br> <font color="red">备注：该选项只对PC平台Flash播放器生效</font>   |
| h5\_start\_patch | Object | 无     | h5播放，开始播放前贴片(可选参数)<br>{ <br>url : 图片地址, <br>stretch: false //是否拉伸图片铺面整个播放器，默认false<br>}                                                                                                  |
| wording          | Object | 无     | 直播提示语自定义(可选参数，详细信息可见[错误码](#errorcode))<br>{	<br>	'1' 	: '数据库错误',<br> '2'		: '连接不到直播源，直播源没有推送视频内容(hls)',<br> '3'		: '直播已经结束啦(hls)',<br>'113'	: '连接超时，请稍后再试',<br>'114'	: '连接超时，请稍后再试',<br>'1000'	: 'channelID或者APPID错误',<br>'1001'	: '无效参数，获取bizid失败',<br>'1009'	: '直播源已失效',<br>'10000'	: '请求超时，请检查网络设置',<br> '10008'	: '密码错误，请重新输入', //无效密码<br>'10020'	: '直播账户余额已不足，请及时充值',  <br>'11044'	: '无效请求',<br> '11045'	: '请求参数缺少channelID',<br> '11046'	: '密码错误，请重新输入',<br> '20110'	: '密码错误，请重新输入',<br>'20113'	: '直播已经结束啦，请稍后再来' , //'downstream type is not exist' 拉流不存在<br>'20201'	: '直播已经结束啦，请稍后再来', //get upstream info error'  查询推流错误<br> '20301'	: '直播频道不存在，请确认频道ID',<br>'TipReconnect'	: '重新连接中'<br>'TipRequireSafari'	: '当前浏览器不能支持视频播放,请使用safari打开观看'<br>'TipRequireFlash'	: '当前浏览器不能支持视频播放，可下载最新的QQ浏览器或者安装FLASH即可播放'<br>'TipVideoinfoResolveError'	: '视频信息解析错误，请检查参数是否正确', //接口没有返回json数据，无法解析<br>'TipVideoinfoError'	: '视频信息错误，请检查参数是否正确',<br>'TipConnectError'	: '连接服务失败，请检查网络设置',<br>'TipConnectDeny'	: '连接服务被拒绝', //flash请求触发安全异常<br>'TipLiveEnd'		: '直播已经结束啦，请稍后再来',  // NetStream.Play.Stop 事件, <br>'TipStreamNotFound'	: '直播已经结束啦，请稍后再来' //连接不到直播源，直播源没有推送视频内容<br>}                                                                                                 |
| live\_url        | String | 无     | 直播地址，支持hls/rtmp/flv三种格式<br>用视频地址播放方式为<font color="red">必选参数</font>                                                                       |
| live\_url2       | String | 无     | 直播地址，同上（可选参数）                                                                        |
| volume           | Number | 0.5    | 设置音量初始值0 到 1，默认0.5。（可选参数）<br><font color="red">备注：该选项只对Flash播放器生效</font>                                                                    |
| https             | Number | 0   | 设置对播放页的https支持，0：关闭，1：开启                                                                    |
| hide_volume_tips  | Number | 0   | 是否隐藏音量提示，0：显示，1：隐藏 <br><font color="red">备注：该选项只对Flash播放器生效</font>                                                                    |
| x5_type           | String | 无   | 通过 video 属性“x5-video-player-type”声明启用同层H5播放器，支持的值：h5 (该属性为TBS内核实验性属性，非TBS内核不支持，具体介绍参照 [TBS文档](http://x5.tencent.com/guide?id=4000) )                            |
| x5_fullscreen     | String | 无   | 视频播放时将会进入到全屏模式，支持的值： true:开启 (该属性为TBS内核实验性属性，非TBS内核不支持，具体介绍参照 [TBS文档](http://x5.tencent.com/guide?id=4000) )                                                       |
| WMode             | String  | window | Window 模式不支持其他页面元素覆盖在 Flash 播放器上面，如需要可以修改为 opaque 或其他 flash wmode 的参数值，可以在 Flash 播放器上进行覆盖其他元素。<br> <font color="red">备注：该选项只对PC平台Flash播放器生效  </font>                                                                  |

**listener** : Object ; 可选参数 ; 播放状态变化回调函数列表

| 函数名称                                                 | 类型     | 说明   |
|----------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------|
| playStatus<span id="playstatus" class="anchor"></span> | function | 播放状态变更时触发，回调函数的参数 status：String <br>返回值：<br>ready: “播放器已准备就绪”, playing:”播放中” , playEnd:”播放结束” , error: “播放异常结束或者遇到错误” //由于移动端播放事件触发条件不一致，如果监听播放结束事件建议同时监听error，以免回调不能正确执行。  <br>type：String 在遇到error时返回错误类型 <br>例子：function(status, type){ ... }   |

### 2. 设置和动作

构造函数返回的播放器对象具有以下设置方法

| 方法                 | 说明                          |
|----------------------|-------------------------------|
| resize(width,height) | 参数：width :int；height :int <br>功能：设置当前播放器宽度高度<br>返回：无                       |
| play()                                                  | 功能：开始播放<br>返回：Int(统一返回码)<br><font color="red">备注：该功能仅PC端Flash播放器支持</font>                                                            |
| stop()                                                  | 功能：停止播放<br>返回：Int(统一返回码)<br><font color="red">备注：该功能仅PC端Flash播放器支持</font>                                                                    |
| pause()                                                       | 功能：暂停当前播放的视频 <br>返回：Int(统一返回码)<br><font color="red">备注：该功能仅PC端Flash播放器支持</font>                                                                                   |
| resume()                                                      | 功能：恢复播放视频<br>返回：Int(统一返回码)<br><font color="red">备注：该功能仅PC端Flash播放器支持</font>        |
| addBarrage(barrage) | 参数：barrage://Array 弹幕信息   <br> \[{   <br>"type":"content", //消息类型 ,content:普通文本 <font color="red">(必选)  </font>   <br>"content":"hello world", //文本消息 <font color="red">(必选)  </font>  <br>"time":"1.101",//单位秒 ，表示距离当前调用添加字幕的时间多久后，开始显示该条字幕 <font color="red">(必选)  </font>   <br>"style": "C64B03;35",// 分号分割，第一项颜色值，第二项字体大小 (可选) <br>"postion":"center" //固定位置 <br>center: 居中，bottom: 底部， up: 顶上 (可选) }, ... \]  <br>功能：添加弹幕     <br>返回：Int [返回码](#errorcode) <br> 备注：<font color="red">弹幕仅在前端实现，后台功能请自行开发。该功能只在PC Flash播放器中生效</font>                                                                                   |
| closeBarrage()                                                | 功能：关闭弹幕，关闭后重新调用addBarrage可开启弹幕。 <br>返回：Int [返回码](#errorcode)  <br> 备注：<font color="red">弹幕仅在前端实现，后台功能请自行开发。该功能只在PC Flash播放器中生效</font>                                                                                      |

这些设置方法的统一返回码是：
  
| 错误码<span id="errorcode"></span> | 含义 |
|---------|---------|
| 200 | 操作成功 | 
| 0  | 播放器未完全初始化 | 
| -2 | 未知操作命令 | 


## 问题排查

### 错误码列表

SDK使用过程中出现的异常code对照表<span id="errorcode"></span>

- 前端返回错误

| 提示语  | 说明                                       |
|-------|--------------------------------------------|
|视频信息解析错误，请检查参数是否正确|接口没有返回json数据，无法解析|
|视频信息错误，请检查参数是否正确|视频信息解析错误|
|连接服务失败，请检查网络设置|获取视频频道信息失败|
|连接服务被拒绝   |flash请求触发安全异常|
|缺少视频数据|视频源数据缺失|
|直播已经结束啦，请稍后再来 |NetStream.Play.Stop 事件|
|直播已经结束啦，请稍后再来|连接不到直播源，直播源没有推送视频内容|


- 后台返回错误

| Code  | 提示语|说明                                       |
|-------|-----------|---------------------------------------|
| 1   	|数据库错误|数据库连接超时或者查询错误|
| 2     | 连接不到直播源,直播源没有推送视频内容(hls)|无法获取m3u8文件，连接不到直播源|
| 3     |直播已经结束啦(hls)|Manifest不是合法的m3u8文件，或直播源已结束 |
|113	| 连接超时，请稍后再试|参数错误|
|1000 |channelID或者APPID错误|app_id填写错误（长度错误）|
|1001 |无效参数，获取bizid失败|app_id填写错误（长度正确，内容错误）|                  
| 1009  | 直播源已失效|无效播放地址，直播源已失效                 |
| 10000 | 请求超时|拉取播放器配置信息与视频信息超时，请检查网络重试，超时时间为10s       |
| 10001 | 数据解析失败|拉取播放器配置信息与视频信息获取到的数据解析失败，可能是网络问题或者服务器异常        |
| 10002 | 连接超时，请稍后再试|拉取播放器配置信息与视频信息失败，可能是网络问题或者服务器异常        |
| 10008 |密码错误，请重新输入| 无效密码                            |
|10020 | 直播账户余额已不足，请及时充值| 余额不足|
| 11044 |无效请求| 缺少APPID                                  |
| 11045 |请求参数缺少channelID| 缺少Channel ID                             |
| 11046 | 密码错误，请重新输入|缺少密码                                   |
| 20110 | 密码错误，请重新输入|无效密码                                   |
| 20113 | 直播已经结束啦，请稍后再来|downstream type is not exist 拉流不存在|
|20201  |直播已经结束啦，请稍后再来|get upstream info error   查询推流错误|
|20301  |直播频道不存在，请确认频道ID|channel_id错误（app_id填写正确）|



>备注：如遇到未在列表中的异常code，请联系我们的客服，客服会安排工程师进行解决。

### 常见问题

- **为什么H5播放视频拉伸变形了？**

    解答：H5并不具备拉伸视频的能力，请检查播放器的容器宽高是否设置正确

- **为什么提示“直播已经结束啦，请稍后再来”**

    解答：播放连接视频直播地址，未收到响应，并重试5次后仍未成功将出现这个提示。这时需要确认视频是否在进行推流，网络是否通畅。

-  **QQ浏览器下无法在盖住视频**

    解答：浏览器接管了H5的视频播放功能，X5内核视频播放使用了自研的播放器，考虑用户体验，浏览器使用了统一的播放界面。相关信息参考[QQ浏览器文档说明](http://x5.tencent.com/guide?id=2009)

-  **iOS系统下视频自动全屏播放**

	解答：iOS系统由于webkit设置原因，默认视频全屏播放，如果您的视频需要在APP内实现内联播放，可以设置webkit-playsinline属性。目前iOS10以下版本的Safari无法禁止视频自动全屏。

-  **为什么在 PC Chrome 中Flash播放器会有两个播放按钮？**

	解答：从Chrome 42版本开始将不再自动播放Flash, 只对主要的Flash内容进行自动播放，其它的Flash内容将被暂停播放，除非用户决定去手动点开它。

-  **为什么在 PC 浏览器中可以播放直播视频，移动端却不行**

    解答：在移动端浏览器中播放直播视频，目前只支持hls协议，因此需要确认直播拉流地址是否有hls拉流url。
