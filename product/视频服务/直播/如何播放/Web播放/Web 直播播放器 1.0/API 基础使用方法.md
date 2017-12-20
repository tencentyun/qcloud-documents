### 添加播放器容器

 在需要展示播放器的页面位置加入播放器容器，例如：在 index.html 中加入如下代码：
```
<div id="id_video_container" style="width:100%; height:auto;"></div>
```
容器 ID 以及宽高都可以自定义。

### 创建 Player 对象

接下来在页面底部引入的 Javascript 脚本中创建一个播放器对象，这时将使用播放器的构造函数：
```
var player = new qcVideo.Player("id_video_container", {
"channel_id": "16093104850682282611",
"app_id": "1251783441",
"width" : 480,
"height" : 320
});
```
调用构造函数将会生成一个播放器对象，并且根据 channel_id 和 app_id 找到对应的直播视频流进行播放，如果没有 channel_id 和 app_id，您也可以使用直播地址的形式进行播放，具体示例如 [API 使用案例中的 case3]()，您可以使用播放器对象 player 对播放器进行控制，播放器对象的参数选项下方 API 方法总览有详细介绍。

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