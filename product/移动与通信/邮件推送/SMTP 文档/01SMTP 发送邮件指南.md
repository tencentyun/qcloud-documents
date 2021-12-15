## 开启 SMTP 发信功能
您需要先开启 SMTP 发信功能才能通过 SMTP 接口发送邮件。
## 操作步骤
### 步骤1：进入发信地址
登录 [邮件推送控制台](https://console.cloud.tencent.com/ses)，单击左侧导航栏中 邮件配置-发信地址，进入发信地址页面。
![](https://qcloudimg.tencent-cloud.cn/raw/3e01a0f31f42f6374ee9935f05b70197.png)
### 步骤2：配置 SMTP 密码
1. 在发信地址列表中，找到您要开启 SMTP 发信功能的发信地址，在对应的操作栏中单击 设置 SMTP 密码。
2. 在弹出对话框中填写 SMTP 密码，然后单击**确定**。



## 使用 SMTP 接口发信
SMTP 调用方法示例，及具体请求参数，返回参数，错误码说明，请参见  [SMTP 调用示例](https://cloud.tencent.com/document/product/1288/65751) 。
>?支持发送带附件的邮件，具体请参见 [SMTP 发送带附件的邮件](https://cloud.tencent.com/document/product/1288/65753) 。

## 使用 SMTP 发信频率
目前 SMTP 接口调用频率限制为：同一个 appId 发信频率为20/1s (appId 即腾讯云账号的 appId)。同时同一发信人对同一收信人发信频率限制为10/1h。

我们将收到邮件后，将尽快的将邮件投递出去，但由于各个邮件系统的限流策略，声誉保护策略不同，为了提供您的邮件递送成功率，请尽量以较低的频率发信。


