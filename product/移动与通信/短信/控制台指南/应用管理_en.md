Before sending SMS messages using Tencent Cloud SMS service, you need to create a project first. After the project is created, you can get the SDK AppID and App Key. The former is the unique identifier of the project, and the latter is a password for verifying the validity of the SMS request.
Note: The Appkey for the SdkAppID should be kept confidential.

In addition, you can also set the frequency, add alarm contacts, configure callback and manage blacklist for the SMS project on the project management page.

## Adding Project
Log in to Tencent Cloud [SMS Console](https://console.cloud.tencent.com/sms).
- Complete identity verification for your Tencent Cloud account if you have not already done so. For more information, please see [here](https://cloud.tencent.com/document/product/378/3629). You can skip this step if your Tencent Cloud account has gone through identity verification.

Click **Add Project**. In the **Create Project** pop-up box, choose a creation method, enter the project name and project intro, and select a suitable project type. After this, click **Confirm** and you are directed to the **Project List** page where you can view the information of the new project.
![](//mc.qcloudimg.com/static/img/5c1197ab29531747ba5de8f6b2418ca9/image.png)

## Managing Project
On the **Project List** page of Tencent Cloud [SMS Console](https://console.cloud.tencent.com/sms), you can view the usage of messages in the project, suspend, enable or delete the project.

### Suspending or Deleting Project
Click **Suspend** in the **Operation** column of the project, and click **Confirm** to suspend the project in the pop-up confirmation box. In this case, the dot in front of the project name is changed from green to red, indicating that the project is suspended.
![](//mc.qcloudimg.com/static/img/3e7a941ab81a9da0900ab1af5e351abc/image.png)
If you want to continue using the project, click the **Enable** button of the project, and then click **Confirm** in the pop-up confirmation box. The dot in front of the project name is changed from red to green, indicating that the project is enabled.
If you want to delete the project, click the **Delete** button of the project, and then click **Confirm** in the pop-up confirmation box. This operation cannot be undone. Please proceed with caution.
>Note: A project cannot be deleted if it is running. You need to suspend the project before you can delete it.

![](//mc.qcloudimg.com/static/img/722ab151c99bbb670414d2e7897ff148/image.png)

### Basic Configuration
Click the project name to go to **Project Configuration** -> **Basic Configuration** page, where you can view the SDK AppID and App Key. The former is the unique identifier of the project, and the latter is a password for verifying the validity of the SMS request. Click the **Edit** button in the **Project Information** tab to modify your project's name, type and introduction. After modification, click **Confirm**.
![](//mc.qcloudimg.com/static/img/6a169eb4e3cf6c06a1a04e5283695557/image.png)

### Configuring Frequency Limit
To ensure business and channel security and minimize financial loss caused by malicious call of SMS API, the default frequency limit for sending SMS messages is set as follows:
1. For SMS messages with the same content, a maximum of one such message can be sent to the same phone number within 30 seconds.
2. A maximum of 10 SMS messages can be sent to the same phone number in one calendar day.

>Note: Users who have completed individual verification have no permission to modify the frequency limit. To use this feature, change "Individual Verification" to "Enterprise Verification".

**How to configure:**
In **Project Configuration** -> **Basic Configuration** page, click the **Set** button in the **Delivery Frequency Limit** tab to modify the frequency of sending messages under the project. After modification, click **Confirm**.
![](//mc.qcloudimg.com/static/img/686561248ce3a555e33d13796948ab2a/image.png)

### Alarm for Over-limit Delivery on a Single Day
Tencent Cloud SMS provides an alarm notification service for excessive SMS messages sent each calendar day. If the alarm notification feature is enabled, Tencent Cloud SMS system triggers the alarm to notify the preset alarm recipient when the project sends more SMS messages than the preset limit.
**How to configure:**
In the **Project Configuration** -> **Basic Configuration** page, click the **Set** button in the **Over-limit Delivery Alarm** tab to select alarm condition and enter a corresponding value, and then click **Confirm**.
![](//mc.qcloudimg.com/static/img/4663593afdb4a1d4dede9e1e98b540a9/image.png)

### Configuring Callback
To make it easier for customers to keep good track of the information about the SMS messages sent, Tencent Cloud SMS provides powerful callback capability. For example, if a callback URL for SMS receipt status is configured, after receiving the callback message from operators, Tencent Cloud will push the callback message to the specified callback URL immediately. Tencent Cloud SMS service callbacks for SMS status, SMS reply and voice messages.
**How to configure:**
In **Project Configuration** -> **Basic Configuration** page, click the **Set** button in the **Event Callback Configuration** tab, select the callback as needed and configure the callback URL. After the configuration is completed, click **Confirm**.
![](//mc.qcloudimg.com/static/img/9d795d67207ccca826fa461c14bed18a/image.png)

## Adding Alarm Contact
When added, the alarm contact can receive notifications about approvals for SMS signature and body template as well as alarm for frequency limit in a timely manner:
**How to configure:**
Click the Project name on the **Project List** page of Tencent Cloud [SMS Console](https://console.cloud.tencent.com/sms). In the **Project Configuration** -> **Notifications and Alarms** page, click **Add Alarm Contact**. In the **Add Alarm Contact** pop-up box, enter name, phone number, email address, select frequency limit policy, and then click **Confirm**.
>Note: This feature is strongly recommended so that receivers can receive an alarm when the frequency limit is reached, thus minimizing the financial loss caused by malicious call of SMS API.
>A maximum of 2 alarm contacts can be added for users who have gone through individual verification, and 5 for those who have completed enterprise verification.

![](//mc.qcloudimg.com/static/img/752ebcabffb9825e9b59f59ea2dc3d1a/image.png)
After alarm contacts are added, you are redirected to the alarm contact list, where you can re-edit or delete alarm contacts. Alarm contacts cannot be restored once deleted. Please proceed with caution.
![](//mc.qcloudimg.com/static/img/c612fb0e2bf5cb804ecf78cd7f27dc1b/image.png)

## Blacklist Management
Since SMS platform and operators have put in place blacklist mechanism, you can apply for removing a phone number from the blacklist as needed. You need to query whether the phone number is in the blacklist first.
**How to configure:**
Click the project name on the **Project List** page of Tencent Cloud [SMS Console](https://console.cloud.tencent.com/sms). In the **Project Configuration** -> **Blacklist Management** page, enter the phone number you need to query whether it is in the blacklist. If so, click the phone number, enter the reasons for removing it from the blacklist, and wait for the audit result.
![](//mc.qcloudimg.com/static/img/5aef20461561fff75adf14ea567a8d64/image.png)




