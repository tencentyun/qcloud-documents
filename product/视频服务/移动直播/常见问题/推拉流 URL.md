<h3 id="PushURL">如何生成推流 URL？ </h3>	


#### 方法1：手动生成	
1. 开通 [腾讯云直播服务](https://cloud.tencent.com/product/lvb)。	
2. 前往【[域名管理](https://console.cloud.tencent.com/live/domainmanage)】，添加您已备案完成的域名。
3. 选择进入【辅助工具】>[【地址生成器】](https://console.cloud.tencent.com/live/addrgenerator/addrgenerator)，选择生成类型为**推流域名**，选择对应的域名，填写自定义的流名称 StreamName，选择地址过期时间单击【生成地址】即可。其中`rtmp://domain/live/test?xxx`即为推流 URL。
![](https://main.qcloudimg.com/raw/b92179a1020d676d5e93e7ea4bfd6c37.png)
 >? 
 >- AppName 为区分同一个域名下多个 App 的地址路径，默认为 live。若要自定义须 [提交工单](https://console.cloud.tencent.com/workorder/category) 开通配置，AppName 仅支持英文字母、数字和符号。
 >- 除上述方法，您还可以在云直播控制台的【[域名管理](https://console.cloud.tencent.com/live/domainmanage)】中，选择推流域名单击【管理】，选择【推流配置】，输入推流地址的过期时间和自定义的流名称 StreamName，单击【生成推流地址】即可生成推流地址。

#### 方法2：自动拼装	
实际产品中，您不可能为每一个主播手动创建推流和播放 URL，而是要由您的服务器自行拼装，只要符合腾讯云标准规范的 URL 就可以用来推流，如下是一条标准的推流 URL，它由四个部分组成：	
![](https://main.qcloudimg.com/raw/3f943e68618089527695acedb4880c42.png)	
- **StreamName（流 ID）：**推荐用随机数字或者用户 ID。	
- **txTime（地址有效期）：**何时该 URL 会过期，格式支持十六进制的 UNIX 时间戳。	
	>?例如`5867D600`代表`2017年01月01日00时00点00分`过期，我们的客户一般会将 txTime 设置为当前时间24小时以后过期。过期时间不要太短，因为当主播在直播过程中遭遇网络闪断时，SDK 会自动重新推流，如果 txTime 的过期时间太短，主播会因为推流 URL 过期而无法恢复推流。	
- **txSecret（防盗链签名）：**防止攻击者伪造您的后台生成推流 URL，计算方法参见 [最佳实践 - 防盗链计算](https://cloud.tencent.com/document/product/267/32735)。	
- **示例代码：**登录云直播控制台选择[【域名管理】](https://console.cloud.tencent.com/live/domainmanage)，选中之前配置的推流域名，在【管理】中选择【推流配置】，“推流配置”页面的下半部分有【推流地址示例代码】（PHP 和 Java 两个版本），示例代码演示了如何生成防盗链地址。	

<h3 id="PlayURL">如何生成拉流 URL？ </h3>	

腾讯云播放地址主要由播放前缀、播放域名（domain）、应用名称（AppName）、流名称（StreamName）、播放协议后缀、鉴权参数以及其他自定义参数组成。例如：	
```	
http://domain/AppName/StreamName.flv?txSecret=Md5(key+StreamName+hex(time))&txTime=hex(time) 	
rtmp://domain/AppName/StreamName?txSecret=Md5(key+StreamName+hex(time))&txTime=hex(time)	
http://domain/AppName/StreamName.m3u8?txSecret=Md5(key+StreamName+hex(time))&txTime=hex(time)	
https://domain/AppName/StreamName.m3u8?txSecret=Md5(key+StreamName+hex(time))&txTime=hex(time)	
https://domain/AppName/StreamName.flv?txSecret=Md5(key+StreamName+hex(time))&txTime=hex(time)	
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
鉴权参数：`txSecret=Md5(key+StreamName+hex(time))&txTime=hex(time)`。	

>! 鉴权参数非必需项目，主要用于防范自己的直播内容被恶意盗播。
