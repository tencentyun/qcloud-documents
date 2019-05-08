本教程将手把手地指导您如何使用云点播的 DRM 功能，包括视频上传，视频加密，部署鉴权服务，播放器解密播放的全部流程。

开始教程前，您需要准备以下工具：

* Python 2.7 运行环境
* Chrome 浏览器

现在，您可以开始本次教程了。

## 注册与登录

使用腾讯云点播服务，您需要先 [注册腾讯云账号](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2Fdocument%2Fproduct%2F266)。

完成注册后，请登录 [腾讯云控制台](https://console.cloud.tencent.com)。选择左上角 【云产品】>【视频服务】>【云点播】，进入云点播控制台。

![](https://main.qcloudimg.com/raw/38c85e14bc8c3332e5face6ea6c33cad.png)

经过这个步骤，您已经注册了腾讯云账号，并可以使用云点播服务了。

## 上传视频

请下载 [Wildlife.wmv](http://1255566954.vod2.myqcloud.com/ca75586fvodgzp1255566954/484c46995285890788305672872/xUCHV5kOGyIA.wmv) 到您的本地，用于入门教学的演示视频。

登录 [腾讯云控制台](https://console.cloud.tencent.com)，单击左侧菜单栏的【媒资管理】，选择【已上传】页签，点击【上传视频】按钮。

![](https://main.qcloudimg.com/raw/bbbbc39b295157b9dee12a6841b712d3.png)

弹出【上传视频】的对话框后，选择【本地上传】，点击【选择视频】，将“Wildlife.wmv”上传到云点播平台。

 ![](https://main.qcloudimg.com/raw/e52b179050923d6c98c979994063d0ce.png)
 
执行上传之后，您将在【正在上传】栏看到视频的上传进度。

![](https://main.qcloudimg.com/raw/8a2579f87d5ea0ca5181550f7d4eaca4.png)
 
上传完成之后，在【已上传】栏的视频列表中，将看到上传完成的视频，以及视频对应的 ID（即 FileId）。

![](https://main.qcloudimg.com/raw/69b347af5d260d31ed9eb16617388a3b.png)
 
经过这个步骤，您已经在上传了一个视频到云点播平台，并获取到了上传视频的 ID。
 
## 转加密的自适应码流
 
您可以通过 [API 工具](https://cloud.tencent.com/document/product/266/33427#API-Explorer) 执行`ProcessMedia`命令，对上传的视频发起“转加密的自适应码流”任务，具体步骤如下。
 
首先，进入 [云点播 ProcessMedia 命令的 API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=vod&Version=2018-07-17&Action=ProcessMedia&SignVersion=)，填写您的【个人密钥】（密钥可点击【查看密钥】从 [API 密钥管理控制台](https://console.cloud.tencent.com/cam/capi) 获取）。

![](https://main.qcloudimg.com/raw/33c4e3dc16a0677782ab517e9a912bc0.png)
 
【FileId】输入框中，填写您上传的视频的 ID。

![](https://main.qcloudimg.com/raw/ba89291239caccaedfd040693df711dc.png)

【AdaptiveDynamicStreamingTaskSet.N】输入框中，【Definition】填写 21。

>?此处填写的 21 是 [预置转自适应码流模板](https://cloud.tencent.com/document/product/266/33476#.E9.A2.84.E7.BD.AE.E8.BD.AC.E8.87.AA.E9.80.82.E5.BA.94.E7.A0.81.E6.B5.81.E6.A8.A1.E6.9D.BF) 的模板 ID，表示转出 Widevine 方式加密的 Dash 输出。
 
 ![](https://main.qcloudimg.com/raw/62cd534ab9b462055d96b0b5f4c4f96e.png)
 
在右边栏中选择【在线调用】标签，并点击【发送请求】按钮。发送请求后，从返回结果中获取`TaskId`参数的值，并记录下来。

![](https://main.qcloudimg.com/raw/7ebb02d8db6ae72bab215b6bada17f11.png)
 
经过这个步骤，您已经对视频发起了转自适应码流任务，目标是 Widevine 方式加密的 Dash。
 
## 查询任务结果

您可以通过 [API 工具](https://cloud.tencent.com/document/product/266/33427#API-Explorer) 执行`DescribeTaskDetail`命令，查询“转加密的自适应码流”任务的执行状态，具体步骤如下。

首先，进入 [云点播 DescribeTaskDetail 命令的 API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=vod&Version=2018-07-17&Action=DescribeTaskDetail&SignVersion=)，填写您的【个人密钥】。

![](https://main.qcloudimg.com/raw/24c6a87a239248ce88b026d4d2f85fd7.png)

【TaskId】输入框中，填写您发起任务后获取的 TaskId。

![](https://main.qcloudimg.com/raw/006e1462b20417eff77256e650044290.png)

在右边栏中选择【在线调用】标签，并点击【发送请求】按钮。

![](https://main.qcloudimg.com/raw/872db32401479cb6a7afa7d29fb6d4b2.png)
 
发送请求后，观察返回结果中的任务状态`Status`。当任务状态为`PROCESSING`时，表示任务仍然在执行中，您需要隔一段时间后再调用 API 状态；当任务状态为`FINISH`时，表示任务执行完毕。

![](https://main.qcloudimg.com/raw/20c42b4343a3224220c328babe145c31.png)

任务执行完毕后，您可以在`MediaProcessResultSet`的类型为`AdaptiveDynamicStreaming`的结果中找到带加密的转自适应码流的输出，其中`Url`对应的是播放地址。

![](https://main.qcloudimg.com/raw/073cba331c699a36e339bb95526ebc8d.png)

因为转出的自适应码流被以 Widevine 方式加密，所以无法直接使用该 Url 播放，下面的步骤将介绍如何解密播放。

经过这个步骤，您可以查询“转加密的自适应码流”任务的执行结果。

## 部署鉴权服务

播放 DRM 加密的视频，播放器需要先从鉴权服务获取 Token，这里讲介绍如何如何部署一个派发 Token 的鉴权服务。

首先，请下载 [源码压缩包](http://document-1251659802.coscd.myqcloud.com/DrmTuition.zip)，并解压到您的工作目录。

修改 AuthenticationServer.py 文件，填写您的 SECRET_ID 和 SECRET_KEY。

![](https://main.qcloudimg.com/raw/c323e2b6cfaec4c2638fe63a8d2f7e58.png)

在工作目录下执行命令:

```
python AuthenticationServer.py
```

![](https://main.qcloudimg.com/raw/76f68bf77d6ca283af0e10ef25fcdddd.png)

在浏览器中输入 http://localhost:8081/?fileId=5285xxx5672872 ，其中5285xxx5672872 是您上传视频的 fileId。输入链接后，您将在应答的结果中获得解密播放视频时需要的 Token。

![](https://main.qcloudimg.com/raw/79d473f4349cd175be01ae4e505c3cfc.png)

经过这个步骤，您在本地部署了一个鉴权服务，为指定视频 ID 派发解密播放需要使用的 Token。

## 部署 Web 播放器

这里介绍如何使用 Web 播放器，播放加密后的自适应码流。

首先，修改解压文件中的 Player.html 文件，fileId 填写您的视频 ID，appId 填写您的 AppId。

>?Player.html 中的 playDefinition 保持为 20，是 [播放模板](https://cloud.tencent.com/document/product/266/34101#.E6.92.AD.E6.94.BE.E6.A8.A1.E6.9D.BF)  ID，表示仅播放加密后的自适应码流。

![](https://main.qcloudimg.com/raw/d392603910330e90c9ab5228141e3a7c.png)

在工作目录下执行命令:

```
python PlayerServer.py
```

![](https://main.qcloudimg.com/raw/0e50dd7cf035c89d763119422e03fa78.png)

在浏览器中输入 http://localhost:8082 ，您将看到演示视频的播放页面。点击播放器，视频即开始解密播放。

![](https://main.qcloudimg.com/raw/0fb9789545d48085f7e9c460eb3b97c9.png)

打开 Chrome 的调试模式，您可以看到播放器在播放前，先从 localhost:8081 获取了要播放视频的 Token。

![](https://main.qcloudimg.com/raw/9d929a49b9b62d7d0c9c806ff9ee6d9c.png)

接着，播放器从点播 License 派发服务获取了播放 Widevine 加密视频所需要的 License。

![](https://main.qcloudimg.com/raw/13af38b82ac77d7096ecf83997a9aafe.png)

经过这个步骤，您在本地部署了播放演示视频的 Web 播放器，点击播放器即可解密播放视频。