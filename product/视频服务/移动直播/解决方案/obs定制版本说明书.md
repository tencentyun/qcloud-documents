## OBS功能说明

请先下载腾讯云改造的 [OBS Studio ](http://dldir1.qq.com/hudongzhibo/xiaozhibo/obs_distribute_question.zip) ，定制版 OBS 主要用于冲顶答题模式，具体技术文档可以参考 [直播答题（冲顶模式）](https://cloud.tencent.com/document/product/454/13863) 中的方案一。

**demo演示效果**
![](https://mc.qcloudimg.com/static/img/8b3e1148736f748414f68d1306cbbafa/image.gif)

## 您需要做什么？
- 了解和学习这个定制版本的发题使用方法，这是本文档的主要内容。

- 搭建一套答题系统，用于汇总和处理您的用户的答题请求。

- 为您的答题系统增加一个http服务器接口，用来跟我们定制版 OBS 进行通讯，这样可以让我们定制版 OBS 除了可以发题，还可以发布实时的答题结果。

## 如何推流？
OBS的使用方法，我们就不在这里赘述了，但有几个细节需要您注意：
- **1. 推流 URL要这样填写：**
    比如一个合法的推流 URL `rtmp://3891.livepush.myqcloud.com/live/3891_rexchang?bizid=3891&txSecret=d436dc53e5ab06a12313c736f7d533c91&txTime=5A6B507F`
![](https://mc.qcloudimg.com/static/img/5c132c243e2659befd69cae4537aead6/image.jpg)

- **2. GOP（I帧间隔）要设置为1**
![](https://mc.qcloudimg.com/static/img/204d041289f535ef9355ca8b45780e5d/image.jpg)

- **3. 编码参数追求经济适用**
![](https://mc.qcloudimg.com/static/img/3c4a53b596e1663b5d12e4779922045a/image.jpg)
![](https://mc.qcloudimg.com/static/img/2516df29225a4e13db1c0a217dc0996c/image.jpg)

|推荐推荐配置| 分辨率 | 视频比特率 | 帧率 | 声道数| 采样率| 音频比特率|
|----------------|---------|---------|---------| --------|----|----|
|优先画质| 540x960   | 1000kbps | 25 | 1|48k| 72kbps|
|优先成本| 360x640| 600kbps|20|1|48k| 72kbps|

## 如何发题？

- **这个OBS怎么用？**
我们在OBS的“工具”菜单栏里面加了一个“题目分发”按钮，可以直接将题目打入直播流中。题目可以预先编辑在 ini 文件中，ini （确保是 UTF-8 编码） 文件格式如下：
```
  [1] 
  question="2008年在北京举行的是第几届夏季奥林匹克运动会？"
  answer_1="29"
  answer_2="30"
  answer_3="31"

  [2]
  question="26个英文字母表按顺序，S后面是什么？"
  answer_1="R"
  answer_2="T"
  answer_3="X"
```

在实战场景中，主持人会根据题词板播报题目，位于演播室的导播员负责操作OBS中的“发题”按钮，将题目打入音视频流中。

-  **APP端如何接收题目？**
可以参考我们的接入文档（[iOS平台](https://cloud.tencent.com/document/product/454/7880#Message) | [Android平台](https://cloud.tencent.com/document/product/454/7886#Message)）

-  **题目放在音视频流里靠谱吗？**
这个定制版 OBS 的主要功能就是将题目夹在音视频流中，那么如果音视频卡顿会不会有问题？

 确实是可能有问题的，所以我们采用的解决办法是定时地将同样的题目均匀的塞入音视频流中，类似雌雄受精中精子的解决方案，只要观众端不是持续卡顿，总是能够拿到题目。
![](https://mc.qcloudimg.com/static/img/43b21ea507d14414930052c84d3d3afd/image.jpg)

 上图中的设置，是指间隔多少时间(单位ms)发一次题，一共发送多少次，推荐的配置是（500ms + 6次）。

 如果采用这种方案，APP端需要根据题号**进行剔重**，避免重复的题目多次显示。

## 如何公布答案？
由于腾讯云本身的 PAAS 定位，我们不会具体实现答题系统，这一部分需要由您的业务后台实现，那么这就产生了一个问题，我们的定制版 OBS 如何才能向观众下发每一道题的回答结果呢？

这就需要您的服务器提供一个 http 接口，然后按照约定的 json 格式跟 OBS 进行题目、答案以及人数的通讯。从而实现题目和答案的分发。

点击**配置**tab页，设置您的服务器地址：

![](https://mc.qcloudimg.com/static/img/e5953c50717e1a0fe1f63679938df254/config.jpg)

点击**保存配置**后，将在obs32.exe运行目录中生成config.ini文件，存储相应配置。下次运行时将直接读取对应配置内容。

```
[config]
distributeInterval=0
distributeNum=1
server=http://jww.qcloud.com/sub-answer
```

在实战场景中，当导播员需要向观众端派发答题结果时，只需要先选择指定的题目，并点击 **“显示答案”** 按钮，定制版 OBS 会向您的服务器发送如下 HTTP GET 请求（“/subject/1“部分将由OBS进行拼接，1 代表题目 id）

```
GET http://jww.qcloud.com/sub-answer/subject/1 HTTP/1.1
```

我们期望您的服务器按如下格式向OBS会送答案，不过您也可以自己定制，因为我们定制版OBS在这里不会解析其内容，只是简单的把服务器返回的json塞入音视频流中。

```
{
  "id": 1,
  "answer_1": 2334,
  "answer_2": 345,
  "answer_3": 89,
  "conrrect_index": 1
}
```

![](https://mc.qcloudimg.com/static/img/06841d7c43918d4d31fcb27eb0445630/answerinfo.jpg)
