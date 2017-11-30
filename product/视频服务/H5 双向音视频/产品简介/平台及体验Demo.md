## H5 支持的平台
1. Android 微信、 手机 QQ
```javascript
//判断终端及tbs版本号来确定当前用户的tbs的版本是否支持
function checkTBSVersion(ua) {
    var list = ua.split(" ");
    for (var i = 0; i < list.length; i++) {
        var item = list[i];
        if (item.indexOf("TBS") !== -1 || item.indexOf("tbs") !== -1) {
            var versionStr = item.split("/")[1];
            var version = parseInt(versionStr) || 0;
            if (version < 43600) {
                alert("您的TBS版本号(" + versionStr + ")过低，不支持WebRTC，请升级!");
            }
        }else{
            //不是tbs内核
            //do something here to ensure current browser supports webrtc
        }
    }
}
```
2. 手机端 Chrome:（需支持 H264）Version >= 60
3. PC、Mac 的 Chrome:（需支持 H264）Version >= 52
4. iOS 和 Mac 的 Safari 正在适配中

## 体验 Demo
1. 微信或者手 Q 请先升级 tbs (预计 10 月 tbs 正式发布后就可以跳过此步骤)；
![tbs升级](http://docs-1253488539.picsh.myqcloud.com/tbs.png)
2. 微信或者手 Q 扫码，进入 demo；
![扫码界面](http://docs-1253488539.picsh.myqcloud.com/demo.png)
3. 用 pc 或者 mac 的 Chrome 打开 [体验地址](https://sxb.qcloud.com/quick/index.html)，体验音视频互通。
