Tencent Cloud SMS service provides voice messaging service in China which is used to send notifications to your users in a way of phone voice. When using voice messaging service, you can configure SMS body template in the console, and call Tencent Cloud voice SMS API to send voice messages.
## Preparations
Voice SMS messages do not need a signature. Text content is automatically transferred to voice content before it is sent to your customers.

### Creating Body Template
Log in to Tencent Cloud [SMS Console](https://console.cloud.tencent.com/sms) and click the name of an project to enter its management page. Click **China Voice Messages** -> **Voice Message Content Configuration** -> **Create Body Template**. In the **Create SMS voice message body template** pop-up box, you can enter the template name and SMS content, and add a brief description of scenario and receiver of template content, then click **Confirm** and wait for approval. The body template can be used only when the status is changed from **Pending Approval** to **Approved**.
>Template example:
> Your login verification code is {1}, which is valid for {2} minutes. If you are not using our service, ignore the message. ({number} is customizable and must be consecutively numbered from 1, such as {1}, {2}, etc.)

![](//mc.qcloudimg.com/static/img/34362d3ccdd7c7df7a4412f12df322ee/image.png)

## Sending SMS Messages
For more information on how to call voice API, please see [Voice API](https://cloud.tencent.com/document/product/382/5812).



