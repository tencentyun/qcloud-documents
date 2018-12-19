Tencent Cloud SMS service contains two types of text message delivery services: China text message and international text message. If the phone number in your number file is a Chinese phone number, click **China SMS Text Messages**, otherwise click **International SMS Text Messages**. The example below describes how to send a text message in China, and you can use the same steps when sending international text messages.
## Preparations
>1. A complete SMS message is composed of a **signature** and **body**. You can configure different body templates based on your business needs, and get a final message by combining the signature and different body templates. That is, **SMS signature + SMS body = Final display**
>2. After the SMS signature and template are submitted, we will complete the review process within half a work day. If necessary, you can set a commonly used phone number and email address to receive notification of review progress.

![](https://mc.qcloudimg.com/static/img/1223b6b179dbbbda7dcda06070eb4360/image.png)
Finally, you will receive an SMS message in the following format:
![](https://mc.qcloudimg.com/static/img/fe223e52477df4de3fec20eeb14ddc8f/image.png)

### Adding Project
Log in to Tencent Cloud [SMS Console](https://console.cloud.tencent.com/sms) and click **Add Project** to configure notifications and alarms of use of SMS messages, and manage SMS blacklist.

### Creating Signature
A complete SMS message is composed of a signature and a body. Click the name of a project to enter its management page, where you can click **China SMS Text Message** -> **SMS Content Configuration** -> **SMS Signature** -> **Create Signature**. In the **Create SMS Signature** pop-up box, you can enter the signature, select signature type, fill in the note, upload certificates, then click **Confirm** and wait for approval. The SMS signature can be used only when the status is changed to **Approved**.
![](//mc.qcloudimg.com/static/img/cd087203f9437da4de62168b99377428/image.png)


### Creating Body Template
Click **China SMS Text Messages** -> **SMS Content Configuration** -> **SMS Body** -> **Create Body Template**. In the **Create SMS Body Template** pop-up box, you can enter the template name and SMS content, add a brief description of scenario and receiver of template content, then click **Confirm** and wait for approval. The body template can be used only when the status is changed from **Pending Approval** to **Approved**.
>Template example:
> Your login verification code is {1}, which is valid for {2} minutes. If you are not using our service, ignore the message. ({number} is customizable and must be consecutively numbered from 1, such as {1}, {2}, etc.)

![](//mc.qcloudimg.com/static/img/17012ece005c847f0433c65d1af2e2df/image.png)

## Sending SMS Messages
After both SMS body template and signature are approved, you can send SMS messages. Click **China SMS Text Messages** -> **Send SMS Messages** to enter the page of sending message, and then click the **Send SMS Message** button.
![](//mc.qcloudimg.com/static/img/5395b8f06969d4917a42bee57e4f3298/image.png)

In the pop-up box, select the names of template and signature to be used. Click **Download Template**, enter customer's phone number and template parameters in a specified format (phone numbers locate in the first column):

>Note: The format of the file of SMS content is:
- The first column is user's phone number
- If no parameter is required in the template, do not enter the information of other columns, otherwise, columns starting from the second one indicate template parameter 1, parameter 2...

![](//mc.qcloudimg.com/static/img/f90a8fbb46ae515a3a7c610a09f965a5/image.png)

**Steps for sending SMS messages:**
1. Select the names of template and signature to be used (only approved templates and signatures are displayed in the drop-down list).
2. Upload user's phone number file. You can view the upload speed and current progress in real time.
3. Select **Send now** or **Send later** as needed.
4. Click **Verification Code** for verification.
5. Click **Send** (only after the file has been uploaded).

![](//mc.qcloudimg.com/static/img/40589dde9926ee55f789d8ced519a316/image.png)

### Viewing SMS Message Delivery Result
After an SMS message is sent successfully, you are automatically redirected to the list of SMS messages you sent where you can view its delivery status. The status is updated once every 10 seconds. During this process, you can select **Suspend** and **Continue** manually.
![](//mc.qcloudimg.com/static/img/d1587c9eb9f17c9eb19320077d735d41/image.png)
![](//mc.qcloudimg.com/static/img/588c44747f98623cc942c7dcf7b69340/image.png)


