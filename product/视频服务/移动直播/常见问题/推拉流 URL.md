### 如何手动生成推拉流 URL？
1. 开通 [腾讯云直播服务](https://console.cloud.tencent.com/live?from=product-banner-use-lvb)，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。
2. 前往【域名管理】，添加您已备案完成的 [自有域名](https://cloud.tencent.com/document/product/267/20381) 或 [添加租赁域名](https://cloud.tencent.com/document/product/267/40367)。
1. 选择进入【辅助工具】>[【地址生成器】](https://console.cloud.tencent.com/live/addrgenerator/addrgenerator)进行如下配置：
	1. 选择生成类型为**推流域名**或**播放域名**。
	2. 选择您已添加到域名管理里对应的域名。
	3. AppName 为区分同一个域名下多个 App 的地址路径，默认为 live。
>! AppName 支持自定义编辑，仅支持英文字母、数字和符号，若要自定义须 [提交工单](https://console.cloud.tencent.com/workorder/category) 开通配置。
	4. 填写自定义的流名称 StreamName，例如：`liveteststream`。
	5. 选择地址过期时间，例如：`2019-11-30 23:59:59`。
	6. 单击【生成地址】即可生成对应的推流/播放 URL。
![](https://main.qcloudimg.com/raw/e447230e5a0254e1b20c7cfa268a2f5e.png)

>?更多直播基础相关问题，请参见 [常见问题-直播基础相关问题](https://cloud.tencent.com/document/product/267/7968)。

### 如何自动拼装推拉流 URL？
实际产品中，您不可能为每一个主播手动创建推流和播放 URL，而是要由您的服务器自行拼装，只要符合腾讯云标准规范的 URL 就可以用来推流，如下是一条标准的推流 URL，它由四个部分组成：
![](https://main.qcloudimg.com/raw/3f943e68618089527695acedb4880c42.png)
- **StreamName（流 ID）：**推荐用随机数字或者用户 ID。
- **txTime（地址有效期）：**何时该 URL 会过期，格式支持十六进制的 UNIX 时间戳。
>?例如`5867D600`代表`2017年01月01日00时00点00分`过期，我们的客户一般会将 txTime 设置为当前时间24小时以后过期。过期时间不要太短，因为当主播在直播过程中遭遇网络闪断时，SDK 会自动重新推流，如果 txTime 的过期时间太短，主播会因为推流 URL 过期而无法恢复推流。
- **txSecret（防盗链签名）：**防止攻击者伪造您的后台生成推流 URL，计算方法参见 [最佳实践 - 防盗链计算](https://cloud.tencent.com/document/product/267/32735)。
- **示例代码：**登录云直播控制台选择[【域名管理】](https://console.cloud.tencent.com/live/domainmanage)，选中之前配置的推流域名，在【管理】中选择【推流配置】，“推流配置”页面的下半部分有【推流地址示例代码】（PHP 和 Java 两个版本），示例代码演示了如何生成防盗链地址。
