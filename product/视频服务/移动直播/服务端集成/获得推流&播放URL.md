## 快速获得地址？
如果您是想要生成一组URL用于测试，那您只需要打开[直播控制台>>直播码接入>>推流生成器](https://console.qcloud.com/live/livecodemanage)，点击**生成推流地址**按钮，即可生成一个推流URL和三种不同播放协议的播放URL。
![](//mc.qcloudimg.com/static/img/98b9b659be67a9ac32384b606ace943f/image.png)


使用[RTMP SDK DEMO](https://www.qcloud.com/document/product/454/6555) 可以快速测试推流URL和播放URL的有效性。


## 后台自动拼装？

### 推流URL 
实际产品中，您不可能为每一个主播手工创建推流和播放URL，而是要由您的服务器自行拼装，只要符合腾讯云标准规范的URL 就可以用来推流，如下是一条标准的推流URL，它由三个部分组成：
 ![url](//mc.qcloudimg.com/static/img/6b4fd09ab2c7d6f1503070f8c994f4e0/image.png)

- **直播码**
也叫房间号，推荐用随机数字或者用户ID，注意一个合法的直播码需要拼接 BIZID 前缀。

- **txTime**
何时该URL会过期，格式是十六进制的UNIX时间戳，比如 5867D600 代表 2017年1月1日0时0点0分过期。

- **txSecret**
防盗链签名，防止攻击者伪造您的后台生成推流URL，计算方法参考[防盗链的计算](#.E9.98.B2.E7.9B.97.E9.93.BE.E7.9A.84.E8.AE.A1.E7.AE.97.EF.BC.9F)。

- **示例代码**
[直播控制台>>直播码接入>>推流生成器](https://console.qcloud.com/live/livecodemanage)页面下半部分有示例代码（PHP和Java两个版本）演示如何生成防盗链地址。

### 播放URL
播放URL的拼接跟推流URL一样简单，只是需要把子域名从 **livepush** 改成 **<font color='red'>liveplay</font>**：
![](//mc.qcloudimg.com/static/img/b7d8744654af4a174edf47f8998348a4/image.png)

## 防盗链的计算？
安全防盗链指的是推流和播放URL中的 **txSecret** 字段，它的作用是防止攻击者伪造您的后台生成推流URL，或者非法盗取您的播放地址为自己谋利。

### 安全原理
为了不让攻击者可以伪造您的服务器生成推流URL，我们需要您现在直播管理控制台配置 **防盗链加密KEY**，由于攻击者无法轻易获得加密KEY，也就无法伪造出有效的推流URL，如下图所示：
![](//mccdn.qcloud.com/static/img/4ea1512fd335f68f30cca0a01e902966/image.png)


### 计算过程
- **step1 ： 交换秘钥**
首先，您需要在官网的控制台，协商一个**加密密钥**，这个加密密钥用于在您的服务器上生成防盗链签名，由于腾讯云跟您持有同样的密钥，所以您生成的防盗链签名，腾讯云是可以进行解密确认的。

 加密秘钥分为**推流防盗链KEY**和**播放防盗链KEY**，前者用于生成推流防盗链URL，后者用于生成播放防盗链URL。目前在[直播管理控制台](https://console.qcloud.com/live)上可以自助配置推流防盗链KEY，如下图：
![](//mc.qcloudimg.com/static/img/6be1d875f1120a16d3692c60bb4485a9/image.png)
 >  **<font color='red'>默认不开播放防盗链</font>**
 >   
 > 由于播放防盗链KEY的配置需要同步到几千台CDN集群，同步周期一般都很长，不适合调试期频繁修改。如果您需要配置播放防盗链，可以通过客服电话联系我们，正常流程一般需要 1 - 3 天完成全集群的同步。

- **step2 ： 生成txTime**
签名中明文部分为txTime，含义是该链接的有效期，比如现在我当前的时间是2016-07-29 11:13:45，而且期望新生成的URL是在5分钟后即作废，那么txTime就可以设置为 2016-07-29 11:18:45。

 不过这么长一串时间字符串放在URL里显然 **“不太经济”**，实际使用中，我们是把  2016-07-29 11:18:45 转换成Unix时间戳，也就是1469762325 （转换方式各种后台编程语言都由直接可用的时间函数来处理），然后转换成16进制，也就是 txTime=579ACB15。

- **step3 - 生成txSecret**
txSecret的生成方法是 = **MD5(KEY+ stream_id + txTime)**，这里的 **KEY** 就是您在 step1 中配置的加密KEY，stream_id在本例中为 8888_test001，txTime为刚才计算的579ACB15，**MD5** 即标准的MD5单向不可逆哈希算法。

- **step4 - 合成防盗链地址**
  现在我们有了推流（或者播放）URL，有了用来告知腾讯云该URL过期时间的txTime，有了只有腾讯云才能解密并且验证的txSecret，就可以拼合成一个防盗链的安全URL了。
	
### 示例代码
[直播控制台>>直播码接入>>推流生成器](https://console.qcloud.com/live/livecodemanage)页面下半部分有示例代码（PHP和Java两个版本）演示如何生成防盗链地址。




