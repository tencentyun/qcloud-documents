<span id="PushURL"></span>
## 推流 URL
### 手动生成

1. 开通腾讯云直播服务：如果您尚未开通，请先 [ 申请开通](https://cloud.tencent.com/product/lvb) 云直播服务。
2. 添加直播加速域名：您需要直播服务则需要提供一个已备案的域名，并且在直播控制台中添加直播加速域名，详细操作请参考 [域名管理](https://cloud.tencent.com/document/product/267/30559)。
3. 开始直播前需生成推流地址：登录腾讯云直播控制台，选择【域名管理】，选择已添加的推流域名，选择【管理】>【推流配置】 ，使用【推流地址生成器】生成推流地址。其中 rtmp://domain/live/test?xxx  即为推流 URL。
![](https://main.qcloudimg.com/raw/9ddfbdf5d0174e24580f1ce0fcdb0225.jpg)

### 自动拼装

实际产品中，您不可能为每一个主播手工创建推流和播放 URL，而是要由您的服务器自行拼装，只要符合腾讯云标准规范的 URL 就可以用来推流。
**推流 URL 的组成**
标准的推流 URL 由四个部分组成：
![](https://main.qcloudimg.com/raw/8eae7d54b8cc5e26f41d4e70b453f924.png)

- **StreamName（流 ID）**
推荐用随机数字或者用户 ID。
- **txSecret（防盗链签名）**
防止攻击者伪造您的后台生成推流 URL，计算方法参考 [最佳实践-防盗链计算](https://cloud.tencent.com/document/product/267/32735)。
- **txTime（地址有效期）**
URL 的有效期，格式支持十六进制的 UNIX 时间戳，比如`5867D600`代表`2017年1月1日0时0点0分`过期，我们的客户一般会将 txTime 设置为当前时间24小时以后过期。建议有效期不要太短，因为当主播在直播过程中遭遇网络闪断时，SDK 会自动重新推流，如果 txTime 太短，主播会因为推流 URL 过期而无法恢复推流。

**示例代码**
选择【[直播控制台](https://console.cloud.tencent.com/)】>【域名管理】，选中事先配置的推流域名，选择【管理】>【推流配置】，可以查看【推流地址示例代码】（PHP 和 Java 两个版本）演示如何生成防盗链地址。

<span id="PlayURL"></span>
## 拉流 URL

腾讯云播放地址主要由播放前缀、播放域名（domain）、应用名称（AppName）、流名称（StreamName）、播放协议后缀、鉴权参数以及其他自定义参数组成。例如：
```
http://domain/AppName/StreamName.flv?txSecret=xxxxxxxx&txTime=xxxxxx 
rtmp://domain/AppName/StreamName?txSecret=xxxxxxxx&txTime=xxxxxx
http://domain/AppName/StreamName.m3u8?txSecret=xxxxxxxx&txTime=xxxxxx
https://domain/AppName/StreamName.m3u8?txSecret=xxxxxxxx&txTime=xxxxxx
https://domain/AppName/StreamName.flv?txSecret=xxxxxxxx&txTime=xxxxxx
```

- **播放前缀**
 - RTMP 播放协议：**rtmp://**
 - HTTP-FLV 播放协议：**http://** 或者 **https://**
 - HLS（m3u8） 播放协议：**http://** 或者 **https://**
- **播放域名**
 - 假如您没有自己的播放域名，您可以先 [申请域名](https://dnspod.cloud.tencent.com/?from=qcloudProductDns) ，然后在 [域名管理](https://console.cloud.tencent.com/live/domainmanage) 页面添加域名。
 - 假如您已有自己的播放域名，您可以先进行 [域名备案](https://cloud.tencent.com/product/ba)，然后在 [域名管理](https://console.cloud.tencent.com/live/domainmanage) 页面添加域名。
 - 关于域名 CNAME，更多详情请参考 [CNAME 配置](https://cloud.tencent.com/document/product/267/19908)。
- **应用名称（AppName）**
应用名称指直播流媒体文件存放路径，默认云直播会分配一个路径：**live**。
- **<span id="streamname">流名称（StreamName）</span>**
流名称（StreamName）是指每路直播流唯一的标识符。
- **鉴权参数（非必需）**
鉴权参数：**txSecret=xxxxxxxx&txTime=xxxxxx**非必需项目，主要用于防范自己的直播内容被恶意盗播。
