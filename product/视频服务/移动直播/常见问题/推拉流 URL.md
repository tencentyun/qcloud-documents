## 前提条件
- 已注册腾讯云账号，并开通 [腾讯云直播服务](https://cloud.tencent.com/product/lvb)。
- 已在 [域名注册](https://dnspod.cloud.tencent.com/?from=qcloudProductDns) 申请域名，并备案成功。
- 已在**云直播控制台**>**[域名管理](https://console.cloud.tencent.com/live/domainmanage)**中添加推流/播放域名，具体操作请参见 [添加自有域名](https://cloud.tencent.com/document/product/267/20381)。
- 成功 [配置域名 CNAME](https://cloud.tencent.com/document/product/267/19908)。

## RTMP 协议推流（不支持连麦）[](id:manual)
直播 SDK 支持 RTMP（不支持连麦） 和 RTC（支持连麦） 两种推流协议，本章节介绍 RTMP 推拉流 URL 的生成。

### 控制台生成推流 URL[](id:console)
1. 登录云直播控制台。  
2. 选择进入**直播工具箱** > [**地址生成器**](https://console.cloud.tencent.com/live/addrgenerator/addrgenerator)，进入如下配置：
	- 按需选择生成类型。
	- 选择您已添加到域名管理里对应的域名。
	- 按需编辑 AppName。AppName 为区分同一个域名下多个 App 的地址路径，默认为 live。
	- 填写自定义的流名称 StreamName。
	- 选择地址过期时间。
3. 单击**生成地址**即可生成您需要的推流/播放地址。
![](https://main.qcloudimg.com/raw/b92179a1020d676d5e93e7ea4bfd6c37.png)
>? 
>- AppName 可自定义，仅支持英文字母、数字和符号。
>- 除上述方法，您还可以在云直播控制台的**[域名管理](https://console.cloud.tencent.com/live/domainmanage)**中，选择推流域名单击**管理**，选择**推流配置**，输入推流地址的过期时间和自定义的流名称 StreamName，单击**生成推流地址**即可生成推流地址。

### 推流 URL 拼接规则 [](id:assemble_push) [](id:push)
实际产品中，当直播间较多时，您不可能为每一个主播手工创建推流和播放 URL，您可通过服务器**自行拼装**推流和播放地址，只要符合腾讯云标准规范的 URL 就可以用来推流，如下是一条标准的推流 URL，它由四个部分组成：
![](https://main.qcloudimg.com/raw/095b7c120b62ac8a171603d4fff67cb2.png)
- **Domain**
推流域名，可使用腾讯云直播提供的默认推流域名，也可以用自有已备案且 CNAME 配置成功的推流域名。
- **AppName**
直播的应用名称，默认为 live，可自定义。
- **StreamName（流 ID）**
自定义的流名称，每路直播流的唯一标识符，推荐用随机数字或数字与字母组合。
- **鉴权 Key（非必需）**
包含 txSecret 和 txTime 两部分：`txSecret=Md5(key+StreamName+hex(time))&amp;txTime=hex(time)`。
开启推流鉴权后需使用包含鉴权 Key 的 URL 进行推流。若未开启推流鉴权，则推流地址中无需 “?” 及其后内容。
 - **txTime（地址有效期）** 
表示何时该 URL 会过期，格式支持十六进制的 UNIX 时间戳。
>?例如`5867D600`代表2017年1月1日0时0点0分过期，我们的客户一般会将 txTime 设置为当前时间24小时以后过期，过期时间不要太短也不要太长，当主播在直播过程中遭遇网络闪断时会重新恢复推流，如果过期时间太短，主播会因为推流 URL 过期而无法恢复推流。
 - **txSecret（防盗链签名）**
用以防止攻击者伪造您的后台生成推流 URL，计算方法参见 [最佳实践-防盗链计算](https://cloud.tencent.com/document/product/267/32735)。

### 查看推流地址示例代码 [](id:example)
进入**云直播控制台**>[**域名管理**](https://console.cloud.tencent.com/live/domainmanage)，选中事先配置的推流域名，**管理**>**推流配置**页面下半部分有**推流地址示例代码**（PHP 和 Java 两个版本）演示如何生成防盗链地址。更多详情操作请参见 [推流配置](https://cloud.tencent.com/document/product/267/32833#.E6.8E.A8.E6.B5.81.E5.9C.B0.E5.9D.80.E7.A4.BA.E4.BE.8B.E4.BB.A3.E7.A0.81)。

### 播放 URL 拼接规则 [](id:rtmp_play)
播放地址主要由播放前缀、播放域名（domain）、应用名称（AppName）、流名称（StreamName）、播放协议后缀、鉴权参数以及其他自定义参数组成。例如： 

``` 
webrtc://domain/AppName/StreamName?txSecret=Md5(key+StreamName+hex(time))&txTime=hex(time)
http://domain/AppName/StreamName.flv?txSecret=Md5(key+StreamName+hex(time))&txTime=hex(time)
rtmp://domain/AppName/StreamName?txSecret=Md5(key+StreamName+hex(time))&txTime=hex(time)
http://domain/AppName/StreamName.m3u8?txSecret=Md5(key+StreamName+hex(time))&txTime=hex(time)
```

- **播放前缀**  
<table>
    <tr><th>播放协议</th><th>播放前缀</th><th>备注</th></tr>
<tr>
        <td>WebRTC</td>
        <td><code>webrtc://</code> </td>
        <td>强烈推荐，秒开效果最好，支持超高并发。</td>
    </tr><tr>
        <td>HTTP-FLV </td>
        <td><code>http://</code> 或 <code>https://</code> </td>
        <td>推荐，秒开效果好，支持超高并发。</td>
    </tr><tr>
<td>RTMP</td>
        <td><code>rtmp://</code> </td>
        <td>不推荐，秒开效果差，不支持高并发</td>
    </tr><tr>
        <td>HLS（m3u8）</td>
        <td><code>http://</code>  或 <code>https://</code> </td>
        <td>手机端和 Mac safari 浏览器推荐的播放协议。</td>
    </tr>
</table>
- **Domain**  
  播放域名，自有已备案且 CNAME 配置成功的播放域名。
- **AppName** 
  直播的应用名称，用于区分直播流媒体文件存放路径，默认为 live，可自定义。
- **StreamName（流名称）**  [](id:streamname)
  自定义的流名称，每路直播流的唯一标识符，推荐用随机数字或数字与字母组合。
- **鉴权参数（非必需）** 
  包含 txSecret 和 txTime 两部分：`txSecret=Md5(key+StreamName+hex(time))&amp;txTime=hex(time)`。
开启播放鉴权后需使用包含鉴权 Key 的 URL 进行播放。若未开启播放鉴权，则播放地址中无需 “?” 及其后内容。
 - **txTime（地址有效期）：** 表示何时该 URL 会过期，格式支持十六进制的 UNIX 时间戳。
 - **txSecret（防盗链签名）：**用以防止攻击者伪造您的后台生成播放 URL，计算方法参见 [最佳实践-防盗链计算](https://cloud.tencent.com/document/product/267/32735)。

[](id:rtc)
##  RTC 协议推流（支持连麦）[](id:rtc)
直播 SDK 支持 RTMP（不支持连麦） 和 RTC（支持连麦） 两种推流协议，本章节介绍 RTC 推拉流 URL 的生成。
如果您有 [观众连麦](https://cloud.tencent.com/document/product/454/52751#step_live1) 或者 [直播 PK](https://cloud.tencent.com/document/product/454/60980#step1) 的需求，需要使用支持更低延迟、更好弱网抗性的 RTC 协议进行推拉流。

### 控制台生成推流 URL [](id:rtc_push_manual)
1. 登录登录云直播控制台。  
2. 选择进入**连麦管理**>[**地址生成器**](https://console.cloud.tencent.com/live/micro/address)，进入如下配置：
	- 按需选择连麦应用。如果您当前没有连麦应用，可以在 [连麦应用](https://console.cloud.tencent.com/live/micro/appmanage) > **新建连麦应用**新建一个。
	- 填写**主播 Stream Id** 和**主播 User Id**，这一步骤是为了生成主播的推流和播放地址。
	- 按需填写**连麦观众 Stream Id** 和**连麦观众 User Id**，这一步骤是为了生成连麦观众的推流和播放地址，如果您当前没有连麦观众，暂时可以随意填写。
	- 选择域名，这一步骤是为了生成 CDN 观看地址。
	- 按需编辑 AppName。AppName 为区分同一个域名下多个 App 的地址路径，默认为 live。
	- 选择地址过期时间。
3. 单击**生成地址**即可生成您需要的推流/播放地址。
>? 更多使用手动生成 URL 的介绍请参见 [控制台指南](https://cloud.tencent.com/document/product/1449/68081#.E7.94.9F.E6.88.90.E5.9C.B0.E5.9D.80)。

### 推流 URL 拼接规则 [](id:rtc_push)
实际产品中，当直播间较多时，您不可能为每一个主播手工创建推流和播放 URL，您可以按照如下规范在工程代码中自动拼接 URL，如下是一条标准的推流 URL，示例如下：
```http
trtc://cloud.tencent.com/push/streamid?sdkappid=1400188888&userId=A&usersig=xxxxx
```
   在上述的 URL 中，存在一些关键字段，关于其中关键字段的含义信息，详见下表：
<table>
<tr><th>字段名称</th><th>字段含义</th></tr><tr>
<td>trtc://</td>
<td>互动直播推流 URL 的前缀字段</td>
</tr><tr>
<td>cloud.tencent.com</td>
<td>互动直播特定域名，<b>请勿修改</b></td>
</tr><tr>
<td>push</td>
<td>标识位，表示推流</td>
</tr><tr>
<td>streamid</td>
<td>流 ID，需要由开发者自定义</td>
</tr><tr>
<td>sdkappid</td>
<td>对应 <a href="https://cloud.tencent.com/document/product/454/60985#step41">服务开通</a> 一节中生成的 SDKAppID</td>
</tr><tr>
<td>userId</td>
<td>主播 ID，需要由开发者自定义</td>
</tr><tr>
<td>usersig</td>
<td>由 <a href="https://cloud.tencent.com/document/product/454/60985#step41">服务开通</a> 一节中获取的密钥计算得出</td>
</tr></table>

[](id:assemble_play)[](id:play)
### 播放 URL 拼接规则 [](id:rtc_play)
- 在连麦过程中，主播与连麦者相互之间的观看都要用 RTC来播放，播放的 URL 字符串与推流 URL 只有一个字段的差别，把 `push` 换成 `play` 即可，示例如下：
```http
trtc://cloud.tencent.com/play/streamid?sdkappid=1400188888&userId=A&usersig=xxxxx
```
   在上述的 URL 中，存在一些关键字段，关于其中关键字段的含义信息，详见下表：
<table>
<tr><th>字段名称</th><th>字段含义</th></tr>
<tr>
<td>trtc://</td>
<td>互动直播拉流 URL 的前缀字段</td>
</tr><tr>
<td>cloud.tencent.com</td>
<td>互动直播特定域名，<b>请勿修改</b></td>
</tr><tr>
<td>play</td>
<td>标识位，表示拉流</td>
</tr><tr>
<td>streamid</td>
<td>流 ID，需要由开发者自定义</td>
</tr><tr>
<td>sdkappid</td>
<td>对应 <a href="https://cloud.tencent.com/document/product/454/60985#step41">服务开通</a> 一节中生成的 SDKAppID</td>
</tr><tr>
<td>userId</td>
<td>主播 ID，需要由开发者自定义</td>
</tr><tr>
<td>usersig</td>
<td>由 <a href="https://cloud.tencent.com/document/product/454/60985#step41">服务开通</a> 一节中获取的密钥计算得出</td>
</tr></table>
- CDN 的观看地址与前文中的 [播放 URL](#id:rtmp_play) 规则一致。
