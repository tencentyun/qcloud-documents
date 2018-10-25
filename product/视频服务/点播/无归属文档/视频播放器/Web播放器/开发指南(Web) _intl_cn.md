## 功能介绍

本文档是介绍腾讯云视频点播服务的网页播放器（Web SDK）的使用说明，它可帮助腾讯云客户直接使用经过验证的视频播放能力，通过灵活的接口，快速同自有Web应用集成，以实现桌面应用播放功能。

该SDK所播放的文件受限于全局防盗链功能定义。详细内容请查看官网FAQ安全功能相关说明。

## 能力与平台支持

### 播放格式
WEB SDK播放视频格式支持：

| 播放格式    | PC浏览器环境     | 手机浏览器环境 |
|---------------|----------------------|---------------------|
| HLS（m3u8） | 支持   | 支持   |
| MP4              | 支持   | 支持   |
| FLV               | 不支持 | 不支持 |

> **Android 系统兼容性问题**
> 不像iPhone上只有一个Safari浏览器，Android上的系统标配浏览器有非常多的实现版本，所以Android手机浏览器的兼容是一个业界难题，故此表格中所示的手机浏览器格式支持情况比**不适用于所有Android手机**。

### 平台兼容
为手机浏览器和PC浏览器写两套代码是非常吃力的事情，但如果您使用本款播放器，同一段代码可以自动实现PC浏览器和手机浏览器的自适应切换，播放器内部会自动区分平台使用最优的播放方案。例如：PC平台优先使用Flash 播放器以适应多种视频格式的情况，而手机浏览器上会使用HTML5技术实现视频播放。

## 播放器集成
在需要展示播放器的页面位置加入播放器容器，例如：在index.html中加入如下代码（容器id以及宽高都可以自定义）
```
<div id="id_video_container" style="width:100%; height:auto;"></div>;
```
### 场景1：播放特定FileID的视频文件
在页面引入的Javascript脚本中，创建一个播放器对象，这时将使用播放器的构造函数
```
var player = new qcVideo.Player("id_video_container", {
   "file_id": "1465197896261041838",
   "app_id": "125132611",
   "width":640,
   "height":480
});
```
调用构造函数将会生成一个播放器对象，并且根据file\_id和app\_id找到对应的视频进行播放，您可以使用播放器对象player 对播放器进行控制。播放器对象的参数选项下方API方法总览有详细介绍。

### 场景2：播放指定URL的视频文件

这时需要用到传视频播放地址的功能，这时不需要传file\_id 及app\_id。JS用例如下:
```javascript
var option = {
    "width": 640,
    "height": 480,
    //...可选填其他属性
    "third_video": {
        "urls": {
            20 : "http://208.vod.myqcloud.com/204.mp4" //演示地址，请替换实际地址
        }
    }
};

var player = new qcVideo.Player("id_video_container", option);
```

其中参数third\_video的 urls属性是个Object 可以传多个不同清晰度的视频地址，具体参数说明在API方法总览中，[直达链接](#播放第三方视频)。

>备注：urls 中至少包含一个视频地址


## 更多功能

### 弹幕功能
在播放器初始化完成后，调用播放器对象的addBarrage(barrage) 方法，可以为视频添加弹幕。具体参数[参考API方法总览](#添加弹幕)的说明。

例子：给正在播放的视频添加两条弹幕

```javascript
var barrage = [{
    "type": "content",
    "content": "hello world",
    "time": "1"
},
{
    "type": "content",
    "content": "居中显示",
    "time": "1",
    "style": "C64B03;30",
    "position": "center"
}];

player.addBarrage(barrage);
```

> 备注：弹幕功能仅在前端实现，后台支持请自行开发。弹幕只在PC播放中生效，H5暂时不具备弹幕功能

### 播放事件捕获

有时候我们需要捕获视频事件，并执行某些操作。例如在播放结束时进行视频推荐。

使用listener参数，传入playStatus事件的回调函数。当播放状态变更时，会调用此函数。具体回调函数参数的说明参考API总览，[直达链接](#播放状态变更)

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

### 让播放器记住上次观看的时间点，下次从这个时间点继续播放该怎么做？

option中设置remember参数为1，播放器将会记录该视频最后一次未播放完的的时间点，下次播放会从这个时间点继续播。

例子：
```javascript
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


### 让播放器在网页尺寸变化时跟着变化尺寸

使用播放器对象的resize(width, height)，可以动态修改播放器尺寸。

```
player.resize(640, 480);
```

### 播放在云视频管理里设置了密码的视频

和播放普通视频一样，SDK会自动显示输入密码对话框，输入密码后即可播放。

> 备注：密码功能只对传视频ID播放方式有效。

### 指定播放视频的清晰度

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

## 问题排查

### 错误码列表

SDK使用过程中出现的异常code对照表，如遇到未在列表中的异常code，请联系我们的客服，客服会安排工程师进行解决。

| Code  | 说明               |
|-------|---------------------|
| 1003  | 密码错误         |
| 10000 | 请求超时        |
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
