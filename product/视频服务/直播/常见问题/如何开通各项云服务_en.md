## 1. Live Video Broadcasting (LVB)

### 1.1 Activate LVB service
Enter the [LVB Console](https://console.cloud.tencent.com/live). If the service has not been activated yet, the following page will appear:
![](//mc.qcloudimg.com/static/img/c40ff3b85b3ad9c0cb03170948d93555/image.png)
Click "Request for Activation", then go to Tencent Cloud's manual review stage. Upon the approval of Tencent Cloud, the service is activated.


### 1.2 How to configure the LVB Code access?
After activating the LVB service, enter ["LVB Console" -> "LVB Code Access" -> "Access Configuration"](https://console.cloud.tencent.com/live/livecodemanage) to complete relevant configurations, and then enable the LVB Code service:
![](//mc.qcloudimg.com/static/img/32158e398ab9543b5ac3acf5f04aa86e/image.png)

| Configuration Item | Value Range            | Description  |
|----------|----------------------|--------------|
| LVB Recording | Enable OR Disable | After LVB recording is enabled, all LVB videos will be recorded at the background by default. [DOC](https://cloud.tencent.com/document/product/454/7917) |
| Push Hotlink Protection Key | 32-character lowercase string | To ensure security, the push URL needs to be bound to hotlink protection to avoid being grabbed by others. The key is used to calculate the hotlink protection signature. [DOC](https://cloud.tencent.com/document/product/454/7915#.E9.98.B2.E7.9B.97.E9.93.BE.E7.9A.84.E8.AE.A1.E7.AE.97.EF.BC.9F) |
| API authentication key | 32-character lowercase string | Your server needs to provide authentication information when calling the Tencent Cloud backend APIs. The key is used to help Tencent Cloud verify whether the identify of your server is valid. [DOC](https://cloud.tencent.com/document/product/454/7920#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5) |
| Callback URL | HTTP protocol URL | Tencent Cloud sends the notifications of push, push interruption and other events to you via this URL. The HTTPS protocol is not supported currently. [DOC](https://cloud.tencent.com/document/product/267/5957)  |

Click **Confirm Access** button to switch your Tencent Cloud LVB service to the LVB Code mode.

### 1.3 Query the LVB APPID
Each Tencent Cloud account for which the LVB service has been activated is assigned an LVB APPID. The LVB APPID is displayed at the top of [LVB Console](https://console.cloud.tencent.com/live), as shown below:
![](//mc.qcloudimg.com/static/img/1ee6c6c1f9d8fd1e1744107e63040adf/image.png)

### 1.4 Query the LVB BIZID
Each Tencent Cloud account for which the LVB service has been activated is assigned an LVB BIZID. An LVB BIZID is used to join the push URL and playback URL in the LVB Code. Therefore, after the LVB Code mode is enabled, the BIZID will appear at the top of [LVB Console](https://console.cloud.tencent.com/live), as shown below:
![](//mc.qcloudimg.com/static/img/b0b423fb2298f35dc77e359f3b705bd7/image.png)

### 1.5 Query the push hotlink protection key
Push hotlink protection key is a security protection which ensures that only your App users can push streams. The key can be specified when LVB Code is enabled, and can be changed as needed in the [LVB Console](https://console.cloud.tencent.com/live/livecodemanage): 
![](//mc.qcloudimg.com/static/img/6be1d875f1120a16d3692c60bb4485a9/image.png)

### 1.6 Query the API access authentication key
An API access authentication key is needed when your backend server calls [Cloud API](https://cloud.tencent.com/doc/api/258/5956) related to Tencent Cloud LVB key, and is designed to help Tencent Cloud verify the validity of calling. The key can be specified when LVB Code is enabled, and can be changed as needed in the [LVB Console](https://console.cloud.tencent.com/live/livecodemanage):
![](//mc.qcloudimg.com/static/img/e5034b47cead66be46b1f81a1fea8274/image.png)

### 1.7 Query the event callback URL
An event callback URL is an address from your backend server. When Tencent Cloud needs to notify your backend server of some [LVB-related Events](https://cloud.tencent.com/doc/api/258/5957), it will send notifications to this address in the form of HTTP POST. The event callback URL can be specified when LVB Code is enabled, and can be changed as needed in the [LVB Console](https://console.cloud.tencent.com/live).
![](//mc.qcloudimg.com/static/img/b1df74884171a920e37940a17d2edac2/image.png)

## 2. Video on Demand (VOD)
### 2.1 Activate VOD service
Each new Tencent Cloud account that has gone through user identity verification is eligible for a seven-day free trial. Upon the expiration of the trial period, you can buy the package you need in the [VOD Console](http://console.cloud.tencent.com/video).
![](//mc.qcloudimg.com/static/img/07fc20e09b0a527089cc9d48d27669cc/image.png)

### 2.2 Query the VOD APPID
Each Tencent Cloud account has a unique VOD APPID, which is located in a concealed place on the [VOD Console](http://console.cloud.tencent.com/video), and at least an uploaded or recorded video file needs to exist under your account, as shown below:
![](//mc.qcloudimg.com/static/img/7e1ba9d016cb55e3825b980b5de5987a/image.png)


## 3. Instant Messaging (IM) Service
### 3.1 Activate the IM service
Go to [IM Console](https://console.cloud.tencent.com/avc). If you have not activated the service yet, just click **Activate IM** button. For a new Tencent Cloud account, the IM App list is empty, as shown below:
![](//mc.qcloudimg.com/static/img/c033ddba671a514c7b160e1c99a08b55/image.png)

Click the **Create App Access** button to create a new App access, that is, the name of the App for which you want to get the access to Tencent Cloud IM service. Our test App is called "Small LVB Demo", as shown below:
![](//mc.qcloudimg.com/static/img/897bff65af6202322a434b6fa3f8a0bd/image.png)

Click the OK button, then you can see in the App list the item you just added, as shown below:
![](//mc.qcloudimg.com/static/img/1c1cb2c2fa4c6f0dc7be06bf8329dee3/image.png)

### 3.2 IM SDK APPID
In the above figure, the SDKAPPID column displays Tencent Cloud IM service ID, which is used to identify the interfacing App of a Tencent Cloud customer. It is often used when the App is interfaced with the IM SDK.

### 3.3 IM SDK account type
In the list in the above figure, there is an **App Configuration** button. Click it to proceed with configuration, as shown below:
![](//mc.qcloudimg.com/static/img/d52ac3662d5310673a5d6c6a78f50da4/image.png)

There are many configuration items here, most of which are not important. You may choose not to configure them, or modify them as needed at any time. For example:
- ** Account Name**
You can enter any name you like, but avoid using weird characters.

- **Verification Mode**
Currently, only "System-Generated Pubic Key" is available. Therefore, you do not need to configure this item.

- **Account Administrator**
Account administrator is a UserId for debugging. If you are an engineer, you can simply enter a frequently-used account ID. It is only used when the advanced features of IM service are used.

- **SMS Verification Signature**
This is the prefix of the SMS text. You can enter the App name.

- **Integration Mode**
Stand-alone mode is not recommended, unless you are in urgent need of this mode.

| Integration Mode | Scenarios | Interfacing Complexity | Design Goal |
|------------|-------------|-------------| -----------|
| Guest (Hosted) Mode | Suitable for scenarios with a low requirement for **identity verification**, such as LVB chat room scenario that allows all App users to join the chatting.  | You just need to log in to the IM SDK in the guestLogin mode with a low interfacing cost.  | The design goal is to reduce interfacing cost, so that you can use the IM services without interfacing with the account system. Tencent Cloud will generate a <font color='blue'>"Guest Account"</font> for each App user, which is only used to send and receive messages. |
| Standalone (authentication) Mode | Suitable for customers with a high requirement for **identity verification**. For example, only registered users of your App are allowed to send and receive messages.  | The UserSig security signature is required and interfacing cost is relatively high. | The design goal is to assign the permission for sending and receiving messages to customers. In this mode, your login server is required to allocate a signature after verifying the validity of an App user's identity. Only after the Tencent Cloud authenticates the signature can the user receive and send messages. This can ensure that all recipients and senders of messages are accounts in your account system. |

Click **Save** to complete the IM message access configuration for the App. Then, AccountType is generated, as shown below:
![](//mc.qcloudimg.com/static/img/dca3d66810ebc6b767b7af4f234ecf8b/image.png)

## 4. Cloud Object Storage (COS) Service
### 4.1 Activate COS service
Any user who has gone through identity verification for a new Tencent Cloud account can use the Cloud Object Storage (COS) service immediately. You can enable it by entering [COS Console](https://console.cloud.tencent.com/cos) to create a bucket. **Note: Enable CDN acceleration to support HTTPS download (adapt to Apple's ATS)**.
![](//mc.qcloudimg.com/static/img/680aebc55496fe74be3f58102f62dfd5/image.jpg)

### 4.2 What Is Bucket?
Bucket is a technical term that can be simply understood as **disk partition**. For example, the COS service purchased from Tencent Cloud can be compared to a new disk purchased from JD.COM. You often partition and format the disk before storing data on it. A partition you create on the disk is similar to a bucket you create on Tencent Cloud COS.

### 4.3 Query the bucket name
The name that you specify during bucket creation is a bucket name. For example, in Example 4.1, xiaozhibo is a bucket name.

### 4.4 Query the COS APPID
When you click [Key Management](https://console.cloud.tencent.com/cos/project) tab on the COS console, the COS APPID will be displayed, which must be bound to one pair of APIs.
![](//mc.qcloudimg.com/static/img/60a3a35c5a28603a5ef730a2fd436677/image.png)

### 4.5 Query the COS SecretId and SecretKey
When you click [Key Management](https://console.cloud.tencent.com/cos/project) tab on the COS console, SecretId and SecretKey bound to the COS APPID will be displayed. They are used by APIs for accessing COS. Since COS is a cloud service that has very high requirement for security, if an API fails to transfer a correct key, Tencent Cloud will reject the API request.
![](//mc.qcloudimg.com/static/img/17778b870bae9ad8302ce9774430ca7f/image.png)

## 5. Cloud Virtual Machine (CVM) (optional)
You can use your own server as the business server for deploying backend script. But you're recommended to use Tencent Cloud's CVM to deploy the backend script for a higher reliability. In addition, if you select the Tencent Cloud's Cloud Database as the distributed database, you must use Tencent Cloud CVM to access the database.
Go to [CVM Console](https://console.cloud.tencent.com/cvm/overview), and then click "Purchase CVM" to go to the CVM purchase page:
![](//mc.qcloudimg.com/static/img/9e479e479a8a6cc72678881f400eefd4/image.jpg)
Click "Next" to go to the image selection page. You are recommended to select a Linux image with Nginx+PHP+MySQL from the CVM marketplace.
![](//mc.qcloudimg.com/static/img/84b60f7ab5e966aed54325a7a2b71beb/image.jpg)
Complete the subsequent steps as instructed by the system. The CVM becomes available when the image is installed.

## 6. Cloud Database (optional)
### 6.1 Activate Cloud Database
Go to [Cloud Database Console](https://console.cloud.tencent.com/cdb). If you have not activated the CDB (MYSQL) service, click "New".
![](//mc.qcloudimg.com/static/img/138c9dd9d5793920aa539141567e0be6/image.jpg)
![](//mc.qcloudimg.com/static/img/62c41e4dbde3eb4f906955e9ebd5cca6/image.jpg)
**Note: The Tencent Cloud account used to activate Cloud Database service should be same as the one used to activate CVM, and the region selected for Cloud Database should be same as the one selected for CVM.**
After purchase, the instance is displayed in the "Instance List". Click "Initialize" on the right to set a character set and password for the Cloud Database.
![](//mc.qcloudimg.com/static/img/492e4be9784f96a32da8d1c17bc5feb5/image.jpg)
![](//mc.qcloudimg.com/static/img/df45399f3da5f324ff2c9f9876d6ee45/image.jpg)

### 6.2 Use the Database
After initialization of instance, the private IP address of the instance is displayed in the "Instance List".
![](//mc.qcloudimg.com/static/img/fb0fa5be8c1411c24a9bcfb30fc9ee7e/image.jpg)
You can remotely connect to the instance using the mysql command on the CVM and perform database operations, or click "Manage" in the "Instance List" to go to the management page to work with the database:
![](//mc.qcloudimg.com/static/img/3be77388665815bae35b0a496ecac584/image.jpg)

