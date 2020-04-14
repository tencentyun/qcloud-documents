### 如何手动生成直播 URL？
1. 开通 [腾讯云直播服务](https://cloud.tencent.com/product/lvb)。	
2. 前往【[域名管理](https://console.cloud.tencent.com/live/domainmanage)】，添加您已备案完成的域名。
3. 选择进入【辅助工具】>[【地址生成器】](https://console.cloud.tencent.com/live/addrgenerator/addrgenerator)，进入如下配置：
	1. 按需选择生成类型。
	2. 选择您已添加到域名管理里对应的域名。
	3. 按需编辑 AppName。AppName 为区分同一个域名下多个 App 的地址路径，默认为 live。
	3. 填写自定义的流名称 StreamName。
	4. 选择地址过期时间。
4. 单击【生成地址】即可生成您需要的推流/播放地址。
![](https://main.qcloudimg.com/raw/b92179a1020d676d5e93e7ea4bfd6c37.png)
 >? 
 >- AppName 可自定义，仅支持英文字母、数字和符号。
 >- 除上述方法，您还可以在云直播控制台的【[域名管理](https://console.cloud.tencent.com/live/domainmanage)】中，选择推流域名单击【管理】，选择【推流配置】，输入推流地址的过期时间和自定义的流名称 StreamName，单击【生成推流地址】即可生成推流地址。


### 如何自主拼装直播 URL？
实际产品中，当直播间较多时，您不可能为每一个主播手工创建推流和播放 URL，您可通过服务器**自行拼装**推流和播放地址，只要符合腾讯云标准规范的 URL 就可以用来推流/播放，如下是一条标准的直播 URL，它由四个部分组成：
![](https://main.qcloudimg.com/raw/095b7c120b62ac8a171603d4fff67cb2.png)
- **Domain**
自有域名，可使用腾讯云直播提供的默认推流域名，也可以用已添加的自有域名。
- **AppName**
直播的应用名称，默认为 live，可自定义。
- **StreamName（流 ID）**
自定义的流名称，用以标识直播流，推荐用随机数字或数字与字母组合
- **鉴权 Key（非必需）**
包含 txSecret 和 txTime 两部分，开启推流鉴权后需使用包含鉴权Key 的 URL 进行推流。若未开启推流鉴权，则推流地址中无需 “?” 及其后内容。
 - **txTime（地址有效期）** 
表示何时该 URL 会过期，格式支持十六进制的 UNIX 时间戳。
	>?例如`5867D600`代表2017年1月1日0时0点0分过期，我们的客户一般会将 txTime 设置为当前时间24小时以后过期，过期时间不要太短也不要太长，当主播在直播过程中遭遇网络闪断时会重新恢复推流，如果过期时间太短，主播会因为推流 URL 过期而无法恢复推流。
 - **txSecret（防盗链签名）**
用以防止攻击者伪造您的后台生成直播 URL，计算方法参见 [最佳实践-防盗链计算](https://cloud.tencent.com/document/product/267/32735)。

>!
>- RTMP 播放资源不足，架构平台只有少量的集群支持 RTMP 播放，且 RTMP 播放秒开效果很差。所以推流地址协议可以使用 `rtmp://`，但是播放地址协议推荐使用 `http://` 或者 `https://`。
>- 了解更多播放地址相关信息，请参见 [播放地址由什么组成？](https://cloud.tencent.com/document/product/454/7937#Que6)

### 如何查看推流查看示例代码？
进入【云直播控制台】>[【域名管理】](https://console.cloud.tencent.com/live/domainmanage)，选中事先配置的推流域名，【管理】>【推流配置】页面下半部分有【推流地址示例代码】（PHP 和 Java 两个版本）演示如何生成防盗链地址。更多详情操作请参见 [推流配置](https://cloud.tencent.com/document/product/267/32833#.E6.8E.A8.E6.B5.81.E5.9C.B0.E5.9D.80.E7.A4.BA.E4.BE.8B.E4.BB.A3.E7.A0.81)。


