## OBS 功能说明

请先下载腾讯云改造的 [OBS Studio ](http://dldir1.qq.com/hudongzhibo/xiaozhibo/obs_distribute_question.zip) ，定制版 OBS 主要用于冲顶答题模式，具体技术文档可以参考 [直播答题（冲顶模式）](https://cloud.tencent.com/document/product/454/13863) 中的方案一。

**demo 演示效果**
![](https://mc.qcloudimg.com/static/img/c33ead292783bd4061ef069665b78a38/capture.gif)

## 您需要做什么？

- 了解和学习这个定制版本的发题使用方法，这是本文档的主要内容。具体有两种模式可供选择：本地答题文件模式及服务器透传模式。
- 搭建一套答题系统，用于汇总和处理您的用户的答题请求。
- 为您的答题系统增加对应的 HTTP 服务器接口，用来跟我们定制版 OBS 进行通讯，这样可以让我们定制版 OBS 除了可以发题，还可以发布实时的答题结果。同时，我们还支持自定义消息的透传。

## 如何推流？
OBS 的使用方法，我们就不在这里赘述了，但有几个细节需要您注意：
- **1. 推流 URL 要这样填写：**
    比如一个合法的推流 URL `rtmp://3891.livepush.myqcloud.com/live/3891_rexchang?bizid=3891&txSecret=d436dc53e5ab06a12313c736f7d533c91&txTime=5A6B507F`
    ![](https://mc.qcloudimg.com/static/img/5c132c243e2659befd69cae4537aead6/image.jpg)

- **2. GOP（I 帧间隔）要设置为 1**
  ![](https://mc.qcloudimg.com/static/img/204d041289f535ef9355ca8b45780e5d/image.jpg)

- **3. 编码参数追求经济适用**
  ![](https://mc.qcloudimg.com/static/img/3c4a53b596e1663b5d12e4779922045a/image.jpg)
  ![](https://mc.qcloudimg.com/static/img/2516df29225a4e13db1c0a217dc0996c/image.jpg)

| 推荐推荐配置 | 分辨率     | 视频比特率    | 帧率   | 声道数  | 采样率  | 音频比特率  |
| ------ | ------- | -------- | ---- | ---- | ---- | ------ |
| 优先画质   | 540x960 | 1000kbps | 25   | 1    | 48k  | 72kbps |
| 优先成本   | 360x640 | 600kbps  | 20   | 1    | 48k  | 72kbps |

## 如何配置服务器？
我们在 OBS 的**“工具”**菜单栏里面加了一个**“题目分发”**按钮，单击后在弹窗中选择**“服务器设置”**tab 页，设置您的服务器地址：
![](https://mc.qcloudimg.com/static/img/912ebc5bf4ac55cd2bce8aa9cee5f1ba/server.jpg)
单击**“保存配置”**后，将在 obs32.exe 运行目录中生成 config.ini 文件，存储相应配置。下次运行时将直接读取对应配置内容。

```
[config]
distributeInterval=0
distributeNum=1
server=http://jww.qcloud.com/dabaa
```
## 本地答题文件模式怎么用？
- **如何发题？**
  选择**“本地答题文件”**tab 页，可以加载答题的 ini 文件。
  题目可以预先编辑在 ini 文件中，ini （确保是 UTF-8 编码） 文件格式如下：

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

  加载后显示如图：
  ![](https://mc.qcloudimg.com/static/img/f2ae42fdbb886d85c7404755bc836018/ini.jpg)
  在实战场景中，主持人会根据题词板播报题目，位于演播室的导播员负责选中指定的题目，操作 OBS 中的**“分发题目”**按钮，将题目打入音视频流中。
  具体传递格式为：

  ```
  {
  "id" = "1",
  "question": "2008年在北京举行的是第几届夏季奥林匹克运动会？",
  "answer_1": "29",
  "answer_2": "30",
  "answer_3": "31"
  }
  ```
- **如何公布答案？**
  由于腾讯云本身的 PAAS 定位，我们不会具体实现答题系统，这一部分需要由您的业务后台实现，那么这就产生了一个问题，我们的定制版 OBS 如何才能向观众下发每一道题的回答结果呢？
  这就需要您的服务器提供一个 HTTP 接口，然后按照约定的 JSON 格式跟 OBS 进行题目、答案以及人数的通讯。从而实现题目和答案的分发。
  在实战场景中，当导播员需要向观众端派发答题结果时，只需要先选择指定的题目，并单击 **“答题信息”** 按钮，定制版 OBS 会向您的服务器发送如下 HTTP GET 请求（“/subject/statics/1“部分将由 OBS 进行拼接，1 代表题目 id）

  ```
  GET http://jww.qcloud.com/dabaa/subject/statics/1 HTTP/1.1
  ```

  我们期望您的服务器按如下格式向 OBS 发送答案：

  ```
  {
    "id": 1,
    "answer_1": 2334,
    "answer_2": 345,
    "answer_3": 89,
    "conrrect_index": 1
  }
  ```

  不过您也可以自己定制，因为我们定制版 OBS 在这里不会解析其内容，只是简单的把服务器返回的 JSON 塞入音视频流中。

- **如何使用自定义消息？**

  您可能需要向观众端发送自定义消息，我们也支持该方案，您可以选择指定的题目后，单击**“自定义消息”** 按钮，定制版 OBS 会向您的服务器发送如下 HTTP GET 请求（“/subject/custom/1“部分将由 OBS 进行拼接，1 代表题目 id）

  ```
  GET http://jww.qcloud.com/dabaa/subject/custom/1 HTTP/1.1
  ```

  如果您的自定义消息与题目 id 无关，您也可以在不选择题目的情况下，单击**“自定义消息”** 按钮。我们会用 0	代替题目 id，即向您的服务器发送如下 HTTP GET 请求	

  ```
  GET http://jww.qcloud.com/dabaa/subject/custom/0 HTTP/1.1
  ```

  我们会将服务器返回的 JSON 塞入音视频流中。

## 服务器透传模式怎么用？
在该模式下，不需要本地答题 ini 文件。题目内容也由我们的定制版 OBS 从您的服务器拉取后下发。

- **如何发题？**

  切换到**“服务器设置”**tab 页，可以看到有**服务器透传**的内容，如下图：

  ![](https://mc.qcloudimg.com/static/img/73e7af835f437a3c70565d55c50befe4/servermode.jpg)

  该模式需要您的 HTTP 服务器支持。在实战场景中，当导播员需要向观众端派发题目内容时，只需要先调整题目 id 的数值，并单击 **“分发题目”** 按钮，定制版 OBS 会向您的服务器发送如下 HTTP GET 请求（“/subject/question/1“部分将由 OBS 进行拼接，1 代表题目 id）

  ```
  GET http://jww.qcloud.com/dabaa/subject/question/1 HTTP/1.1
  ```

  您可以自己定制具体的题目内容，因为我们定制版 OBS 在这里不会解析其内容，只是简单的把服务器返回的 JSON 塞入音视频流中。


- **如何公布答案？**

  和本地答题文件模式类似，唯一的区别是，在服务器透传模式中，您不需要选择指定的题目，仅需要确保题目 id 的数值正确即可，并单击 **“答题信息”** 按钮，定制版 OBS 会向您的服务器发送如下 HTTP GET 请求（“/subject/statics/1“部分将由 OBS 进行拼接，1 代表题目 id）

  ```
  GET http://jww.qcloud.com/dabaa/subject/statics/1 HTTP/1.1
  ```

  我们会将服务器返回的 JSON 塞入音视频流中。



- **如何使用自定义消息？**

  和本地答题文件模式类似，唯一的区别是，在服务器透传模式中，您不需要选择指定的题目，仅需要确保题目 id 的数值正确即可，并单击**“自定义消息”** 按钮，定制版 OBS 会向您的服务器发送如下 HTTP GET 请求（“/subject/custom/1“部分将由 OBS 进行拼接，1 代表题目 id）

  ```
  GET http://jww.qcloud.com/dabaa/subject/custom/1 HTTP/1.1
  ```

  我们会将服务器返回的 JSON 塞入音视频流中。
  如果您的自定义消息与题目 id 无关，您可以在收到请求后无视该 id 字段即可。

## App 端如何接收题目？

可以参考我们的接入文档（[iOS 平台](https://cloud.tencent.com/document/product/454/7880#Message) | [Android 平台](https://cloud.tencent.com/document/product/454/7886#Message)）

## 题目放在音视频流里靠谱吗？

这个定制版 OBS 的主要功能就是将题目夹在音视频流中，那么如果音视频卡顿会不会有问题？
确实是可能有问题的，所以我们采用的解决办法是定时地将同样的题目均匀的塞入音视频流中，类似雌雄受精中精子的解决方案，只要观众端不是持续卡顿，总是能够拿到题目。
![](https://mc.qcloudimg.com/static/img/3ef35d5f920c7231127128d504775f23/interval.jpg)

 上图中的设置，是指间隔多少时间(单位 ms)发一次题，一共发送多少次，推荐的配置是（500ms + 6 次）。
 如果采用这种方案，App 端需要根据题号**进行剔重**，避免重复的题目多次显示。
