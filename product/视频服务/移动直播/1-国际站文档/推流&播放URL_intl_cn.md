## 快速获得URL
如果您是想要生成一组URL用于测试，那您只需要打开[直播控制台>>直播码接入>>推流生成器](https://console.cloud.tencent.com/live/livecodemanage)，点击**生成推流地址**按钮，即可生成一个推流URL和三种不同播放协议的播放URL。

![](//mc.qcloudimg.com/static/img/98b9b659be67a9ac32384b606ace943f/image.png)


使用我们的 [推流 App](https://cloud.tencent.com/document/product/454/6555) 可以快速测试推流URL和播放URL的有效性。


## 推流URL的组成

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

## 播放URL的组成
播放URL的拼接跟推流URL一样简单，只是需要把子域名从 **livepush** 改成 **<font color='red'>liveplay</font>**：
![](//mc.qcloudimg.com/static/img/b7d8744654af4a174edf47f8998348a4/image.png)



