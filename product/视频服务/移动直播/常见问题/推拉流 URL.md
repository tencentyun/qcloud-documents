<h2 id="PushURL">推流 URL </h2>

### 手动生成

1. 开通腾讯云直播服务：如果您尚未开通云直播服务，请单击 [申请开通](https://cloud.tencent.com/product/lvb)。
2. 添加直播加速域名：如果您要使用云直播服务，则须要提供一个备案过的域名，并在云直播控制台中添加直播加速域名，详细请参见 [域名管理](https://cloud.tencent.com/document/product/267/30559)。
3. 生成推流地址：首先登录腾讯云直播控制台，选择左上角【云产品】>【云直播】>【域名管理】，选择添加过的推流域名，在【管理】中选择【推流配置】 ，在“推流地址生成器”中单击【生成推流地址】来生成一个推流地址。其中 `rtmp://domain/live/test?xxx` 即为推流 URL。
![](https://main.qcloudimg.com/raw/8655758da7ba987edaee2a0fe6ec8fca.png)

### 自动拼装

实际产品中，您不可能为每一个主播手工创建推流和播放 URL，而是要由您的服务器自行拼装，只要符合腾讯云标准规范的 URL 就可以用来推流，如下是一条标准的推流 URL，它由四个部分组成：
![](https://main.qcloudimg.com/raw/8eae7d54b8cc5e26f41d4e70b453f924.png)
- **StreamName（流 ID）：**推荐用随机数字或者用户 ID。
- **txTime（地址有效期）：**何时该 URL 会过期，格式支持十六进制的 UNIX 时间戳。

	例如`5867D600`代表`2017年01月01日00时00点00分`过期，我们的客户一般会将 txTime 设置为当前时间24小时以后过期。过期时间不要太短，因为当主播在直播过程中遭遇网络闪断时，SDK 会自动重新推流，如果 txTime 的过期时间太短，主播会因为推流 URL 过期而无法恢复推流。
- **txSecret（防盗链签名）：**防止攻击者伪造您的后台生成推流 URL，计算方法参见 [最佳实践 - 防盗链计算](https://cloud.tencent.com/document/product/267/32735)。
- **示例代码：**登录[【云直播控制台】](https://console.cloud.tencent.com/)，选择左上角【云产品】>【云直播】>【域名管理】，选中之前配置的推流域名，在【管理】中选择【推流配置】，“推流配置”页面的下半部分有【推流地址示例代码】（PHP 和 Java 两个版本），示例代码演示了如何生成防盗链地址。



<h2 id="PlayURL">拉流 URL </h2>

腾讯云播放地址主要由播放前缀、播放域名（domain）、应用名称（AppName）、流名称（StreamName）、播放协议后缀、鉴权参数以及其他自定义参数组成。例如：
```
http://domain/AppName/StreamName.flv?txSecret=xxxxxxxx&txTime=xxxxxx 
rtmp://domain/AppName/StreamName?txSecret=xxxxxxxx&txTime=xxxxxx
http://domain/AppName/StreamName.m3u8?txSecret=xxxxxxxx&txTime=xxxxxx
https://domain/AppName/StreamName.m3u8?txSecret=xxxxxxxx&txTime=xxxxxx
https://domain/AppName/StreamName.flv?txSecret=xxxxxxxx&txTime=xxxxxx
```

- **播放前缀**
 - RTMP 播放协议：`rtmp://`。
 - HTTP - FLV 播放协议：`http://` 或者 `https://`。
 - HLS（m3u8） 播放协议：`http://` 或者 `https://`。
 
- **播放域名**
 - 如果您没有播放域名，您可以单击 [域名注册](https://dnspod.cloud.tencent.com/?from=qcloudProductDns) 申请域名，并在 [域名管理](https://console.cloud.tencent.com/live/domainmanage) 中添加域名。
 - 如果您已有播放域名，您可以先进行 [域名备案](https://cloud.tencent.com/product/ba)，然后在 [域名管理](https://console.cloud.tencent.com/live/domainmanage) 中添加域名。
 - 关于域名 CNAME，详细请参见 [CNAME 配置](https://cloud.tencent.com/document/product/267/19908)。
 
- **应用名称（AppName）**
应用名称指的是直播流媒体文件存放路径，云直播默认会分配一个路径：`live`。

- **<span id="streamname">流名称（StreamName）</span>**
流名称（StreamName）是指每路直播流的唯一标识符。

- **鉴权参数（非必需）**
鉴权参数：`txSecret=xxxxxxxx&txTime=xxxxxx`。

>! 鉴权参数非必需项目，主要用于防范自己的直播内容被恶意盗播。
