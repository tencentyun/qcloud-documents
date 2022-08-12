## 功能相关问题
### 使用云呼叫中心需要准备哪些软硬件设备？[](id:hardware)
硬件：使用云呼叫中心需要一台电脑、耳机、麦克风。
软件：版本70以上的谷歌 Chrome 浏览器。
### 云呼叫中心通话录音支持通过接口拉取吗？[](id:interface)
支持。具体请参考 API 文档 [获取电话服务记录与录音](https://cloud.tencent.com/document/product/679/47714#1.-.E6.8E.A5.E5.8F.A3.E6.8F.8F.E8.BF.B0)。
###  云呼叫中心电话来电支持转接到客服手机接听吗？[](id:service)
支持。具体请参考文档 [手机接听](https://cloud.tencent.com/document/product/679/48046)。
###  使用云呼叫中心电话客服，用户电话呼入后，是否支持呼叫中心平台直接回访呢？
支持。具体请参考文档电话服务 [电话呼出功能](https://cloud.tencent.com/document/product/679/48045#.E7.94.B5.E8.AF.9D.E5.91.BC.E5.87.BA)。
###  云呼叫中心支持查看电话、文字、图片等历史记录吗？[](id:history)
云呼叫中心电话录音支持在线播放与下载，同时支持接口拉取。图文记录支持在线查看。

### Chrome 无来电铃声的问题[](id:noring)
- 首先检查音频设备是否有问题，音量是否设置为0。
- 检查浏览器设置，浏览器地址栏输入`chrome://settings/content/siteDetails?site=https%3A%2F%2Ftccc.qcloud.com`。把**摄像头**、**麦克风**、**通知**、**后台同步**、**声音**设置为允许。
![](https://qcloudimg.tencent-cloud.cn/raw/506d6c31d2db427460bd919c231d2557.png)

- 如果上面检查都没有问题，则为浏览器防止网页自动播放音视频对用户造成干扰，对音视频的自动播放功能做了限制。这种情况需要执行下面步骤：
  1. 下载 [chrome_policy.reg.zip](https://upload-dianshi-1255598498.file.myqcloud.com/chrome_policy-2fad0f85195e7bf4101fb90f92ce1fa5234b41d2.reg.zip)，并且解压。
  - 双击执行刚刚解压的文件，选择**是**。
    ![](https://qcloudimg.tencent-cloud.cn/raw/ac3b10a90e72b42b6e0b0ccfbc1bd217.png)
  - 关闭 Chrome 浏览器，重新打开浏览器，在地址栏输入 `chrome://media-engagement/`
    ![](https://qcloudimg.tencent-cloud.cn/raw/e835ca89eee86578aa44e85c265fa4ac.png)
  - 查看**Autoplay disable settings**的值是否为**Disabled**，并且**Autoplay Policy**的值是否为**no-user-gesture-required**。如果不是，请关闭杀毒软件重新双击执行前面下载的 [文件](https://upload-dianshi-1255598498.file.myqcloud.com/chrome_policy-2fad0f85195e7bf4101fb90f92ce1fa5234b41d2.reg.zip)。
  - 重新打开浏览器，进入 [腾讯云呼叫中心](https://tccc.qcloud.com/login) 观察来电声音是否正常。

## 计费相关问题[](id:service)
### 云呼叫中心的客服包月费用是否包含电话客服、在线客服、全媒体客服功能呢？
包含。您在购买客服服务后可以使用电话、在线、和全媒体三种客服功能。
### 云呼叫中心一个账号可以添加几个坐席使用？
无限制。如需添加更多，请参考 [购买指引](https://cloud.tencent.com/document/product/679/48025)。
## 审核相关问题[](id:audit)
### 请问云呼叫中心的企业资质审核时效是多久呢？
我们将会在1个工作日内完成审核。
审核时间：周一至周日9:00至23:00（法定节假日顺延）。
## 小程序音视频接入问题[](id:miniprogram)
### 头像不存在，该如何处理？
需要把 UserInfo 存入 globalData 中。
```
getApp().globalData.userInfo = userInfo
```
### 调用 requestLogin 失败，该如何处理？
请确保 wx.login() 返回的临时登录凭证未过期且未被使用。
### 提示获取 roomSig 失败，该如何处理？
请参考 [调试指引](https://developers.weixin.qq.com/miniprogram/dev/framework/usability/debug.html) 打开调试面板，查看报错 log。
如无法定位并解决问题，可提供报错 log 截图等相关信息 提交工单 或联系我们（QQ：2982200247）协助处理。


