<h2 id="Why"> 为何要派发URL？</h2>

直播推流需要推流 URL， 直播播放需要播放 URL，不管您的产品是想做单场次的活动直播，还是主播可以随时开播的直播平台，由后台派发 URL 都要比把 URL 写死在 APP 里要灵活的多。

这里说的“派发”指的是：在 APP（主播端）准备推流（[iOS](https://cloud.tencent.com/document/product/454/7879) | [Android](https://cloud.tencent.com/document/product/454/7885)）时返回推流 URL 给 APP，在 APP（观众端）需要播放（[iOS](https://cloud.tencent.com/document/product/454/7880) | [Android](https://cloud.tencent.com/document/product/454/7886)）时返回播放 URL 给 APP。

<h2 id="URL"> URL的组成？ </h2>

### 推流URL的组成

如下是一条标准的推流URL，它由三个部分组成：
 ![url](//mc.qcloudimg.com/static/img/6b4fd09ab2c7d6f1503070f8c994f4e0/image.png)

- **直播码**
也叫房间号，推荐用随机数字或者用户ID，注意一个合法的直播码需要拼接 BIZID 前缀。

- **txTime**
何时该URL会过期，格式是十六进制的UNIX时间戳，比如 5867D600 代表 2017年1月1日0时0点0分过期。  我们的客户一般会将 txTime 设置为当前时间 24 小时以后过期，<font color='red'>过期时间不要太短</font>，当主播在直播过程中遭遇网络闪断时会重新恢复推流，如果过期时间太短，主播会因为推流 URL 过期而无法恢复推流。

- **txSecret**
防盗链签名，防止攻击者伪造您的后台生成推流URL，计算方法参考[防盗链签名的计算](https://cloud.tencent.com/document/product/454/9875)。

- **示例代码**
[直播控制台>>直播码接入>>推流生成器](https://console.cloud.tencent.com/live/livecodemanage)页面下半部分有示例代码（PHP和Java两个版本）演示如何生成防盗链地址。

### 播放URL的组成
播放URL的拼接跟推流URL一样简单，只是需要把子域名从 **livepush** 改成 **<font color='red'>liveplay</font>**：
![](//mc.qcloudimg.com/static/img/b7d8744654af4a174edf47f8998348a4/image.png)


<h2 id="Secret"> 防盗链签名</h2>

### 什么是防盗链签名？
防盗链签名指的是推流 URL 和播放 URL 中的 **txTime** 和 **txSecret** 字段，它的作用是防止攻击者通过伪造您的直播 URL 而盗播您的流量。

![](//mc.qcloudimg.com/static/img/4c0ba5f9993da67ff785f10eb4c85f3d/image.png)

### 防盗链签名的原理？
为了不让攻击者可以伪造您的服务器生成推流URL，我们需要您现在直播管理控制台配置 **防盗链加密KEY**，由于攻击者无法轻易获得加密KEY，也就无法伪造出有效的推流URL，原理如下图所示：
![](//mccdn.qcloud.com/static/img/4ea1512fd335f68f30cca0a01e902966/image.png)

### 防盗链签名的计算？
#### step1 ： 交换KEY
首先，您需要在 [直播控制台](https://console.cloud.tencent.com/live/livecodemanage) 设置一个**加密密钥**，该密钥用于在您的服务器上计算防盗链签名，由于腾讯云跟您持有同样的密钥，所以您生成的防盗链签名，腾讯云可以进行合法性确认。

密钥分为**推流防盗链KEY**和**播放防盗链KEY**，前者用于生成推流防盗链URL，后者用于生成播放防盗链URL。目前在  [直播控制台](https://console.cloud.tencent.com/live/livecodemanage) 上可以自助配置推流防盗链KEY，如下图：
![](//mc.qcloudimg.com/static/img/6be1d875f1120a16d3692c60bb4485a9/image.png)
 >  **播放防盗链不支持自助配置**
 >   
 > 由于播放防盗链KEY的配置需要同步到几千台CDN集群，同步周期一般都很长，不适合调试期频繁修改。如果您需要配置播放防盗链，可以通过客服电话联系我们，正常流程一般需要 1 - 3 天完成全 CDN 集群的配置。

#### step2 ： txTime
签名中明文部分为txTime，含义是该链接的有效期，比如现在我当前的时间是2016-07-29 11:13:45，而且期望新生成的URL是在 24 小时后即作废，那么txTime就可以设置为 2016-07-30 11:13:45。

为了减少 URL 中的字符串长度，要  2016-07-30 11:13:45 转换成Unix时间戳，也就是1469848425 ，然后再转换成16进制以进一步压缩字符长度，也就是 txTime = 1469848425（十进制） = 579C1B69（十六进制）。
 
一般将 txTime 设置为当前时间 12 小时以后过期，<font color='red'>过期时间不要太短</font>，否则当主播在直播过程中遭遇断网重连时，会因为过期时间太短而无法恢复推流。

#### step3 ： txSecret

<table><tr><td style="width: 700px; height: 80px; text-align:center; "> 
<B>txSecret = MD5(KEY+ stream_id + txTime)</B> 
</td></tr></table>

这里的 **KEY** 就是您在 step1 中配置的加密KEY，**stream_id** 为直播码（或称作流ID），**txTime**为刚才计算的 579C1B69，**MD5** 即标准的MD5哈希算法。

#### step4 ： 地址拼接
现在我们有了推流（或者播放）URL，有了用来告知腾讯云该URL过期时间的txTime，有了只有腾讯云才能解密并且验证的txSecret，就可以拼合成一个防盗链的安全URL了。

<table><tr><td style="width: 700px; height: 80px; text-align:center; "> 
rtmp://8888.livepush.myqcloud.com/live/8888_test001?txSecret=xxx&txTime=5C2A3CFF
</td></tr></table>
	
> [直播控制台>>直播码接入>>推流生成器](https://console.cloud.tencent.com/live/livecodemanage) 页面下半部分有示例代码（PHP和Java两个版本）演示如何生成防盗链地址。




