
### 推流 URL 
云直播控制台的 [地址生成器](https://console.cloud.tencent.com/live/addrgenerator/addrgenerator) 工具可自助生成推流地址和播放地址，当直播间较多时，可通过服务器自行拼接推流和播放地址，只要符合腾讯云标准规范的 URL 就可以用来推流，如下是一条标准的推流 URL，它由四个部分组成：
![](https://main.qcloudimg.com/raw/f94876b78d22d9d90570cac9d4d61eb2.png)
- **Domain**
推流域名，可使用腾讯云直播提供的默认推流域名，亦可使用自有推流域名。
- **AppName**
直播的应用名称，默认为 live，若需要自定义 AppName，可通过 [提交工单](https://console.cloud.tencent.com/workorder/category) 配置。
- **StreamName（流 ID）**
自定义的流名称，用以标识直播流，推荐用随机数字或数字与字母组合鉴权Key：包含 txSecret 和 txTime 两部分，开启推流鉴权后需使用包含鉴权Key 的 URL 进行推流；若未开启推流鉴权，则推流地址中无需 “?” 及其后内容。
- **txTime（地址有效期）** 
表示何时该 URL 会过期，格式支持十六进制的 UNIX 时间戳，例如5867D600代表2017年1月1日0时0点0分过期，我们的客户一般会将 txTime 设置为当前时间24小时以后过期，过期时间不要太短也不要太长，当主播在直播过程中遭遇网络闪断时会重新恢复推流，如果过期时间太短，主播会因为推流 URL 过期而无法恢复推流。
- **txSecret（防盗链签名）**
用以防止攻击者伪造您的后台生成推流 URL，计算方法参见 [最佳实践-防盗链计算](https://cloud.tencent.com/document/product/267/32735)。
- **示例代码**
[【直播控制台】](https://console.cloud.tencent.com/)>【域名管理】，选中事先配置的推流域名，【管理】>【推流配置】页面下半部分有【推流地址示例代码】（PHP 和 Java 两个版本）演示如何生成防盗链地址。


