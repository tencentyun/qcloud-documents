Before sending SMS messages using Tencent Cloud SMS service, you need to create a project first. After the project is created, you can get the SDK AppID and App Key. The former is the unique identifier of the project, and the latter is a password for verifying the validity of the SMS request.
Note: The Appkey for the SdkAppID should be kept confidential.

In addition, you can also set the frequency, configure callback  for the SMS project on the project management page.

## Adding Project
Log in to Tencent Cloud [SMS Console](https://console.cloud.tencent.com/sms).
- Complete identity verification for your Tencent Cloud account if you have not already done so. For more information, please see [here](https://intl.cloud.tencent.com/document/product/378/3629). You can skip this step if your Tencent Cloud account has gone through identity verification.

Click **Add Project**. In the **Create Project** pop-up box, choose a creation method, enter the project name and project intro, and select a suitable project type. After this, click **Confirm** and you are directed to the **Project List** page where you can view the information of the new project.
![](
https://main.qcloudimg.com/raw/e39ef8893a95573753ac90554f68ed20.png)

## Managing Project
On the **Project List** page of Tencent Cloud [SMS Console](https://console.cloud.tencent.com/sms), you can view the usage of messages in the project, suspend, enable or delete the project.

### Suspending or Deleting Project
Click **Suspend** in the **Operation** column of the project, and click **Confirm** to suspend the project in the pop-up confirmation box. In this case, the dot in front of the project name is changed from green to red, indicating that the project is suspended.
![](
https://main.qcloudimg.com/raw/c9a3fc2b67eecd70b36118149e0d124b.png)
If you want to continue using the project, click the **Enable** button of the project, and then click **Confirm** in the pop-up confirmation box. The dot in front of the project name is changed from red to green, indicating that the project is enabled.
If you want to delete the project, click the **Delete** button of the project, and then click **Confirm** in the pop-up confirmation box. This operation cannot be undone. Please proceed with caution.
>Note: A project cannot be deleted if it is running. You need to suspend the project before you can delete it.

![](
https://main.qcloudimg.com/raw/ac41d3c5ed174dc1303292d9fcdf0e90.png)

### Basic Configuration
Click the project name to go to **Project Configuration** -> **Basic Configuration** page, where you can view the SDK AppID and App Key. The former is the unique identifier of the project, and the latter is a password for verifying the validity of the SMS request. Click the **Edit** button in the **Project Information** tab to modify your project's name, type and introduction. After modification, click **Confirm**.
![](
https://main.qcloudimg.com/raw/fc39c6d00cd18b5b373f6fdb938b7bc5.png)

### Configuring Frequency Limit
To ensure business and channel security and minimize financial loss caused by malicious call of SMS API, the default frequency limit for sending SMS messages is set as follows:
1. For SMS messages with the same content, a maximum of one such message can be sent to the same phone number within 30 seconds.
2. A maximum of 10 SMS messages can be sent to the same phone number in one calendar day.

>Note: Users who have completed individual verification have no permission to modify the frequency limit. To use this feature, change "Individual Verification" to "Enterprise Verification".

**How to configure:**
In **Project Configuration** -> **Basic Configuration** page, click the **Set** button in the **Delivery Frequency Limit** tab to modify the frequency of sending messages under the project. After modification, click **Confirm**.
![](
https://main.qcloudimg.com/raw/42e83338582d16d3b480da65dbc90422.png)

### Configuring Callback
To make it easier for customers to keep good track of the information about the SMS messages sent, Tencent Cloud SMS provides powerful callback capability. For example, if a callback URL for SMS receipt status is configured, after receiving the callback message from operators, Tencent Cloud will push the callback message to the specified callback URL immediately. Tencent Cloud SMS service callbacks for SMS status, SMS reply and voice messages.
**How to configure:**
In **Project Configuration** -> **Basic Configuration** page, click the **Set** button in the **Event Callback Configuration** tab, select the callback as needed and configure the callback URL. After the configuration is completed, click **Confirm**.
![](
https://main.qcloudimg.com/raw/bb25eae4f28961cbce814e64fa44c977.png)





