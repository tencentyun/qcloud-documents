Tencent Cloud supports receiving messages via WeChat! You can receive messages on WeChat after a few simple steps below:
## Step 1: Set WeChat
### Creating a User and Setting WeChat
1. Log in to the Tencent Cloud Console, go to [User Management](https://console.cloud.tencent.com/cam), and select **Create User**.
![](https://mc.qcloudimg.com/static/img/9d1384f8e6129b4b45dc92fc28662035/image.png)
2. Select **Collaborator** or **Message Receiver**.
> **Note:**
> Because sub-users cannot receive messages, receiving messages via WeChat is unavailable to such users.

![](https://mc.qcloudimg.com/static/img/d5dbe653d48e20075557e9664145ef70/image.png)
3. Enter the user information, and enable receiving messages via WeChat.
![](https://mc.qcloudimg.com/static/img/d5cc2e3a4134c735e15e708c94ea81a1/image.png)
4. After completing the information, you will receive an email containing a QR code which is valid for 3 days in the email address you provided.
![](https://mc.qcloudimg.com/static/img/8a96f0b71d70ceb81a3e0e7b764ca63b/image.png)
### Setting WeChat for Existing Users
1. Log in to the Tencent Cloud Console, go to [User Management](https://console.cloud.tencent.com/cam), and click the specific user to enter the user details page.
![](https://mc.qcloudimg.com/static/img/6ba2d3a221ba96969ec8e4779bb8c990/image.png)
2. Click **Edit**.
![](https://mc.qcloudimg.com/static/img/26556f09a8c63b87e02d39765ce60e50/image.png)
3. Enable receiving messages via WeChat.
![](https://mc.qcloudimg.com/static/img/eb4f3071ebaaec89b5c8a8d7297e1216/image.png)
4. After completing the information, you will receive an email containing a QR code which is valid for 3 days in the email address you provided.
![](https://mc.qcloudimg.com/static/img/8a96f0b71d70ceb81a3e0e7b764ca63b/image.png)
## Step 2: Verify WeChat
1. Scan the QR code in the email with WeChat, and follow the Official Account "Tencent Cloud Assistant".
>**Notes:**
>If you do not scan the QR code or do not follow the official account after scanning the QR code, the WeChat verification will fail. Unverified WeChat users cannot receive messages via WeChat.
>Unverified WeChat users can be re-verified on the User Management page.

![](https://mc.qcloudimg.com/static/img/296f79b925ee9c18722e57e41c6801ce/image.png)

## Step 3: Set the message channel to WeChat
1. Go to [Message Subscription](https://console.cloud.tencent.com/messageCenter/messageConfig), select a message type, and then click **Edit**.
>**Notes:**
>The types of WeChat messages supported are account in arrears notifications, balance warning notices, product expiration and withdrawal notifications, and attack notifications.
>Only some of the messages in the attack notification type can be sent to WeChat.

![](https://mc.qcloudimg.com/static/img/2542ec1e464c367569c52892844eace9/image.png)

2. Select **WeChat** as the receiving method.
>**Note:**
 >If the message type does not support WeChat, **WeChat** cannot be selected.

![](https://mc.qcloudimg.com/static/img/277c80b2f9657a0988c459a1a4d4c4e7/image.png)

## Step 4: Set the message recipient
1. Go to [Message Subscription](https://console.cloud.tencent.com/messageCenter/messageConfig), select a message type, and then click **Edit**.
![](https://mc.qcloudimg.com/static/img/2542ec1e464c367569c52892844eace9/image.png)
2. In the edit box, you can add or remove message receivers. If the receiver of the message type has successfully verified WeChat, he/she can receive the WeChat messages.
![](https://mc.qcloudimg.com/static/img/b9012afe25a54d438becab8acbedf9e1/image.png)

