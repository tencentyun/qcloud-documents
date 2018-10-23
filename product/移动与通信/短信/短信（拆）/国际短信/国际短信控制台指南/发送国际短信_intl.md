Tencent Cloud SMS service provides two types of text messaging services: CSMS and ISMS. Click **International SMS** if the mobile numbers in your number file are non-Chinese numbers. Follow the procedure below to send an ISMS message.
## Preparations
>1. A complete SMS message consists of **SMS signature** and **SMS body**. You can set different message body templates based on business needs, and then combine the signature and body to form a final display. **SMS signature + SMS body = final display**.
>2. Our review will be completed within half a work day after the SMS signature and template are submitted. If necessary, you can set a mobile number and email address to receive the notification of SMS message content audit for this project.

![](https://main.qcloudimg.com/raw/68eb00daf596eb4bb9d6837a6411035b.png)
The final SMS message sent to users is as follows:
![](https://main.qcloudimg.com/raw/cb7c93a64d0646f552c9d1cabc4e1d63.png)

### Add project
Log in to Tencent Cloud [**SMS Console**](https://console.cloud.tencent.com/sms) and click **Add Project** to configure notification and alarm, and manage blacklist.
![](https://main.qcloudimg.com/raw/1ca800eeba40d444af754ed0106497e5.png)

### Create signature
A complete SMS message consists of SMS signature and message text. Click the name of an project to enter its management page. Click **International SMS** -> **SMS Content Configuration** -> **SMS Signature** -> **Create Signature**. In **Create SMS Signature** pop-up box, enter the signature, select the signature type, enter the remarks, upload certificates, then click **Confirm** and wait for the approval. The SMS signature cannot be used until its status is changed to **Approved**.
![](https://main.qcloudimg.com/raw/575d3dfa752b2c27a4e3d485855e9f6b.png)


### Create body template
Click **International SMS** -> **SMS Content Configuration** -> **SMS Body** -> **Create Body Template**. In the **Create SMS Body Template** pop-up box, enter the template name and SMS Content, select [common message](https://intl.cloud.tencent.com/document/product/382/13444#audit-criteria-for-common-sms-messages) or [marketing message](https://intl.cloud.tencent.com/document/product/382/13444#audit-criteria-for-marketing-sms-messages) as the SMS message type, add a brief description of scenario and object of template content, then click **Confirm** and wait for the approval. The message body template cannot be used until its status is changed from **Pending approval** to **Approved**.


>Template example:
>   Your login verification code is {1}, which is valid for {2} minutes. If you are not using our service, ignore the message. ({number} is customizable and must be numbered consecutively from 1, such as {1}, {2}, and so on.)

![](https://main.qcloudimg.com/raw/3bd35055ed3079cc0defbc25088ceb2c.png)

## Sending SMS Messages
After the SMS body template and SMS signature are approved, you can send SMS messages. Click **International SMS** -> **Send SMS Messages**.
![](
https://main.qcloudimg.com/raw/3d76492f9d059c20dddf8ec70a8fc3c7.png)

In the pop-up box, select the template name and signature name. Click **Download template**, and enter the user mobile numbers (in the first column) and template parameters in the specified format:

>Note: The format of the SMS message content file should be as below:
- User mobile numbers are in the first column.
- If no parameter is in the template, do not enter the information of other columns, otherwise, columns starting from the second one indicate template parameter 1, parameter 2...

![](https://main.qcloudimg.com/raw/5c1b560f8261674cb53facba79c9d561.png)

**Steps for sending SMS messages:**
1. Choose the template name and signature name (only approved templates and signatures are displayed in the drop-down list).
2. Upload user mobile number file. You can view the upload speed and current progress in real time.
3. Select **Send now** or **Send by schedule** as needed.
4. Click **Verification Code** for verification.
5. Click **Send** (only after the file has been uploaded).

![](
https://main.qcloudimg.com/raw/37ed915ae910c7420d8fed8e752758cf.png)

### View SMS message delivery result
After an SMS message is sent successfully, you are automatically redirected to the list of delivered SMS messages where you can view its delivery status. The status is updated every 10 seconds. During this process, you can select **Suspend** and **Continue**.
![](
https://main.qcloudimg.com/raw/de97c100a3b4dd785c00ca747f66862f.png)
![](
https://main.qcloudimg.com/raw/eea2c59651adde7df27d115e6602377e.png)

