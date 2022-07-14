## 现象描述[](id:FaultPhenomenon1)
**现象**：Web 超级播放器接入报错 “Error Code：4”。如下图所示：
![](https://main.qcloudimg.com/raw/002f3e422a7fc06170496e3a0ca1c2b0.png)

## 可能原因

- [获取不到视频资源](#video)
- [视频格式不支持](#format)
- [当前播放环境不支持](#enviroment)
- [Js 顺序加载失败](#js)

## 处理步骤

### 获取不到视频资源[](id:video)
1. 首先需要检查对应视频资源是否被删除，本地网络环境是否良好，可以通过使用其他播放器如 ffplay、VLC 等播放对应视频，判断视频资源和网络环境是否正常。
 - 若是，请执行 [步骤2](#A_step2)。
 - 若否，请恢复视频资源，修复网络环境，若仍无法正常播放，请执行 [步骤2](#A_step2)。
2. [](id:A_step2)检查对应 appid 是否开通 key 防盗链等配置，则需要在播放过程中代入对应字段进行播放信息的获取。如下图播放带 psign 示例：
![](https://main.qcloudimg.com/raw/7f3c3086664c8ecd5f0ddb74d8907399.png)
>?超级播放器是根据页面代码中 appid 和 fileid 发送请求至点播后台，后台会根据 appid 和 fileid 返回对应的视频信息，播放器收到视频信息再去请求视频。

### 视频格式不支持[](id:format)
1. 播放器是依赖浏览器自身解码能力解析视频进行播放，如果上传的视频没有执行转码，或视频本身的文件编码信息与当前播放环境不兼容，则会导致播放异常。
 - 若是，将视频执行转码操作，请参见 [如何对视频进行转码](https://cloud.tencent.com/document/product/266/33478)。
 - 若否，请执行 [步骤2](#B_step2)。
2. [](id:B_step2)对比 Demo 查看是否正常播放，请参见 [使用 Demo 体验](https://cloud.tencent.com/document/product/266/46217#.E6.AD.A5.E9.AA.A43.EF.BC.9A.E4.BD.BF.E7.94.A8-demo-.E4.BD.93.E9.AA.8C)。
![](https://main.qcloudimg.com/raw/0f7c57a5ac2c59e8991e9e9706a664f1.png)

### 当前播放环境不支持[](id:enviroment)
可以通过模拟环境来播放测试，由于 PC 端 Chrome 浏览器播放 m3u8 格式是通过 MSE 转封装实现的，而 iOS 具有直接播放 m3u8 的能力，所以在 PC 端模拟 iOS 的环境，播放器获取环境为 iOS 时，会直接播放 m3u8，而不是像其他 PC 端通过调用 MSE 来播放 m3u8。

但模拟环境并不是真实的 iOS，并没有直接播放 m3u8 的能力，所以如果使用模拟 iOS 环境来播放对应视频，这里有可能会导致报错。如下图 Chrome 模拟展示：

![](https://main.qcloudimg.com/raw/34b5386618c9984af39ad1449a653c77.png)

### Js 顺序加载失败[](id:js)
检查 hls.js 是否在 tcplayer.js 前引入，需要保证 hls.js 在 tcplayer.js 前引用，tcplayer.js 加载并初始化播放器后，需要通过 hls.js 来播放 hls 视频。

如果 hls.js 在 tcplayer.js 之后引入，播放器初始化成功并调用 hls.js 进行视频播放器的时候，hls.js 可能并未加载成功，导致播放失败，所以用户播放失败是 Js 顺序没有调整好。
>?有些情况下，通过动态加载 js，虽然 hls.js 在 tcplayer.js 前，但是动态加载并不能保证加载顺序按照对应的顺序加载，hls.js 可能也会在 tcplayer.js 后加载，导致偶现报错 code4。
>
**错误示例**：
![](https://main.qcloudimg.com/raw/121531f464d1498ce2286125ac67e3ad.png)

**正确示例**：
![](https://main.qcloudimg.com/raw/792463eff0787fb119b442b55c7848d8.png)

如果您通过以上方法仍未解决超级播放器报错 Error Code:4 的问题，请可以 [提交工单](https://console.cloud.tencent.com/workorder/category) 反馈。
