Tencent Cloud SMS service provides two types of text messaging services: CSMS and ISMS. Click **International SMS** if the mobile numbers in your number file are non-Chinese numbers. Follow the procedure below to send an ISMS message.
## Preparations
>1. A complete SMS message consists of **SMS signature** and **SMS body**. You can set different message body templates based on business needs, and then combine the signature and body to form a final display. **SMS signature + SMS body = final display**.
>2. Our review will be completed within half a work day after the SMS signature and template are submitted. If necessary, you can set a mobile number and email address to receive the notification of SMS message content audit for this project.

![](https://mc.qcloudimg.com/static/img/1223b6b179dbbbda7dcda06070eb4360/image.png)
The final SMS message sent to users is as follows:
![](https://mc.qcloudimg.com/static/img/fe223e52477df4de3fec20eeb14ddc8f/image.png)

### Add project
Log in to Tencent Cloud [**SMS Console**](https://console.cloud.tencent.com/sms) and click **Add Project** to configure notification and alarm, and manage blacklist.
![](https://main.qcloudimg.com/raw/9e0957c8d1d0811fe9de421bfa7d30a0.png)

### Create signature
A complete SMS message consists of SMS signature and message text. Click the name of an project to enter its management page. Click **International SMS** -> **SMS Content Configuration** -> **SMS Signature** -> **Create Signature**. In **Create SMS Signature** pop-up box, enter the signature, select the signature type, enter the remarks, upload certificates, then click **Confirm** and wait for the approval. The SMS signature cannot be used until its status is changed to **Approved**.
![](https://main.qcloudimg.com/raw/cac4c2a038a847509977ee95a41ef113.png)


### Create body template
Click **International SMS** -> **SMS Content Configuration** -> **SMS Body** -> **Create Body Template**. In the **Create SMS Body Template** pop-up box, enter the template name and SMS Content, select [common message](https://cloud.tencent.com/document/product/382/13444#.E6.99.AE.E9.80.9A.E7.9F.AD.E4.BF.A1.E5.AE.A1.E6.A0.B8.E6.A0.87.E5.87.86) or [marketing message](https://cloud.tencent.com/document/product/382/13444#.E8.90.A5.E9.94.80.E7.9F.AD.E4.BF.A1.E5.AE.A1.E6.A0.B8.E6.A0.87.E5.87.86) as the SMS message type, add a brief description of scenario and object of template content, then click **Confirm** and wait for the approval. The message body template cannot be used until its status is changed from **Pending approval** to **Approved**.


>Template example:
>   Your login verification code is {1}, which is valid for {2} minutes. If you are not using our service, ignore the message. ({number} is customizable and must be numbered consecutively from 1, such as {1}, {2}, and so on.)

![](https://main.qcloudimg.com/raw/e0d4eadf63a8975825fc03165153ecd2.png)

## Sending SMS Messages
After the SMS body template and SMS signature are approved, you can send SMS messages. Click **International SMS** -> **Send SMS Messages**.
![](//mc.qcloudimg.com/static/img/5395b8f06969d4917a42bee57e4f3298/image.png)

In the pop-up box, select the template name and signature name. Click **Download template**, and enter the user mobile numbers (in the first column) and template parameters in the specified format:

>Note: The format of the SMS message content file should be as below:
- User mobile numbers are in the first column.
- If no parameter is in the template, do not enter the information of other columns, otherwise, columns starting from the second one indicate template parameter 1, parameter 2...

![](//mc.qcloudimg.com/static/img/f90a8fbb46ae515a3a7c610a09f965a5/image.png)

**Steps for sending SMS messages:**
1. Choose the template name and signature name (only approved templates and signatures are displayed in the drop-down list).
2. Upload user mobile number file. You can view the upload speed and current progress in real time.
3. Select **Send now** or **Send by schedule** as needed.
4. Click **Verification Code** for verification.
5. Click **Send** (only after the file has been uploaded).

![](//mc.qcloudimg.com/static/img/40589dde9926ee55f789d8ced519a316/image.png)

### View SMS message delivery result
After an SMS message is sent successfully, you are automatically redirected to the list of delivered SMS messages where you can view its delivery status. The status is updated every 10 seconds. During this process, you can select **Suspend** and **Continue**.
![](//mc.qcloudimg.com/static/img/d1587c9eb9f17c9eb19320077d735d41/image.png)
![](//mc.qcloudimg.com/static/img/588c44747f98623cc942c7dcf7b69340/image.png)

