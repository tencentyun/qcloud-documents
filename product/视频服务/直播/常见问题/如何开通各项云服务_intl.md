<h2 id="LVB"> 1. Live Video Broadcasting (LVB) </h2>

<h3 id="LVB_OPEN">1.1 Activating LVB service</h3>

Log in to the [LVB Console](https://console.cloud.tencent.com/live). If you have not activated the service, the following page appears:
![](//mc.qcloudimg.com/static/img/c40ff3b85b3ad9c0cb03170948d93555/image.png)
Click **Apply**, and then go to the application approval step. The service is activated upon the approval of Tencent Cloud.

<h3 id="LVB_OPEN">1.2 Enabling LVB Code Access</h3>

After activating the LVB service, go to [**LVB Console -> LVB Code Access -> Access Configuration**](https://console.cloud.tencent.com/live/livecodemanage) to complete the configurations, and then activate the LVB Code service:
![](//mc.qcloudimg.com/static/img/32158e398ab9543b5ac3acf5f04aa86e/image.png)

| Configuration Item | Value Range | Description |
|----------|----------------------|--------------|
| LVB Recording | Enable or Disable | If this is enabled, all LVB videos are recorded in background by default. [DOC](https://cloud.tencent.com/document/product/454/7917) |
| Push Hotlink Protection Key | A 32-character lowercase string | To ensure security, the push URL needs to be bound to hotlink protection to avoid being hacked by others. The key is used to calculate the hotlink protection signature. [DOC](https://cloud.tencent.com/document/product/454/7915#.E9.98.B2.E7.9B.97.E9.93.BE.E7.9A.84.E8.AE.A1.E7.AE.97.EF.BC.9F) |
| API Authentication Key | A 32-character lowercase string | Your server needs to provide authentication information when calling the Tencent Cloud backend APIs. The key is used by Tencent Cloud to verify the validity of your server's identity. [DOC](https://cloud.tencent.com/document/product/454/7920#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5) |
| Callback URL | HTTP protocol-based URL | Tencent Cloud sends the notifications of push, push interruption and other events to you via this URL. HTTPS protocol is not supported. [DOC](https://cloud.tencent.com/document/product/267/5957) |

Click **OK** to switch your Tencent Cloud LVB service to the LVB Code mode.

<h3 id="LVB_APPID">1.3 LVB APPID</h3>

Each Tencent Cloud account for which the LVB service has been activated is assigned an LVB APPID, which is displayed at the top of [LVB Console](https://console.cloud.tencent.com/live), as shown below:
![](//mc.qcloudimg.com/static/img/1ee6c6c1f9d8fd1e1744107e63040adf/image.png)

<h3 id="LVB_BIZID">1.4 LVB BIZID</h3>

Each Tencent Cloud account for which the LVB service has been activated is assigned an LVB BIZID. An LVB BIZID is used to construct the push and playback URLs in the LVB Code. After the LVB Code mode is enabled, the BIZID appears at the top of [LVB Console](https://console.cloud.tencent.com/live), as shown below:
![](//mc.qcloudimg.com/static/img/b0b423fb2298f35dc77e359f3b705bd7/image.png)

<h3 id="LVB_PUSH_SECRECT">1.5 Push hotlink protection key</h3>

Push hotlink protection key is a security protection which ensures that only your App users can push streams. The key can be specified when LVB Code is enabled, and can be modified as needed in the [LVB Console](https://console.cloud.tencent.com/live/livecodemanage):
![](//mc.qcloudimg.com/static/img/6be1d875f1120a16d3692c60bb4485a9/image.png)

<h3 id="LVB_API_SECRECT">1.6 API authentication key</h3>

An API access authentication key is required when your backend server calls the [Cloud API](https://cloud.tencent.com/doc/api/258/5956) related to Tencent Cloud LVB Code, and allows Tencent Cloud to verify the validity of the call. The key can be specified when LVB Code is enabled, and can be modified as needed in the [LVB Console](https://console.cloud.tencent.com/live/livecodemanage):
![](//mc.qcloudimg.com/static/img/e5034b47cead66be46b1f81a1fea8274/image.png)

<h3 id="LVB_EVENT_URL">1.7 Event notification URL</h3>

An event callback URL is an address from your backend server. When Tencent Cloud needs to notify your backend server of some [LVB-related Events](https://cloud.tencent.com/doc/api/258/5957), it sends the notifications to this address in the form of HTTP POST. The event callback URL can be specified when LVB Code is enabled, and can be modified as needed in the [LVB Console](https://console.cloud.tencent.com/live).
![](//mc.qcloudimg.com/static/img/b1df74884171a920e37940a17d2edac2/image.png)

## 2. Video on Demand (VOD)
### 2.1 Activating VOD service
Each new Tencent Cloud account that has completed identity verification is eligible for a seven-day free trial. Upon the expiration of the trial period, you can purchase the package as needed on the [VOD Console](http://console.cloud.tencent.com/video).
![](//mc.qcloudimg.com/static/img/07fc20e09b0a527089cc9d48d27669cc/image.png)

### 2.2 VOD APPID
Each Tencent Cloud account has a unique VOD APPID, which is located in an unobvious place on the [VOD Console](http://console.cloud.tencent.com/video). It is only displayed when you have at least one uploaded or recorded video file under your account, as shown below:
![](//mc.qcloudimg.com/static/img/7e1ba9d016cb55e3825b980b5de5987a/image.png)

<h2 id="IM"> 3. Instant Messaging (IM) Service</h2>

<h3 id="IM_OPEN"> 3.1 Activating IM service</h3>

Log in to the [IM Console](https://console.cloud.tencent.com/avc), and then click **Activate IM**.

The IM application list is empty under a new Tencent Cloud account. Click the **New Application** button to create an application:
![](https://mc.qcloudimg.com/static/img/8eff5d50253bc93f6866eaa0905a6a09/image.jpg)

<h3 id="IM_SDKAPPID"> 3.2 SDK APPID</h3>

The ID shown in the figure below is an sdkappid, which identifies a product under your Tencent Cloud account. If there are multiple products under your account, multiple sdkappids are provided.
![](https://mc.qcloudimg.com/static/img/1623a895927342b6c7b7a00c21c98f39/image.jpg)

<h3 id="IM_ACCTYPE"> 3.3 AccountType</h3>

Click **Application Configuration** on the right of the list to proceed with the configuration, as shown below:
![](https://mc.qcloudimg.com/static/img/eac0bf8431fa9ed4653771e46c400b71/image.jpg)

**Account Name** allows letters and numbers. **Account Administrator** is used only when REST API of IM is called.

Click **Save** to complete the IM access configuration for the App. At the same time, AccountType is generated, as shown below:
![](https://mc.qcloudimg.com/static/img/1d6dbd66465e887997dcb6a7b10373cb/image.jpg)

<h3 id="IM_ADMIN"> 3.4 Administrator</h3>

IM provides a set of [REST](https://cloud.tencent.com/document/product/269/1520) APIs for your backend server to call IM service directly, for example, to create a group, send system messages and remove a user from the group. But the IM REST API can only be called by an administrator, that is, you need an administrator username and password (UserSig). For more information, please see [DOC](https://cloud.tencent.com/document/product/269/1519#3-.E8.B0.83.E7.94.A8.E6.96.B9.E6.B3.95).

![](https://mc.qcloudimg.com/static/img/ba88ee27c2ae30d27b9a9170b35cc0d0/image.jpg)

<h3 id="IM_PRIKEY"> 3.5 PrivateKey & PublicKey</h3>

IM SDK can be considered as the QQ without user interaction page. Integrating the IM SDK into your App is like integrating a QQ message kernel.

As we all know, QQ can receive and send messages of private chats and group chats, but you need to log in to it before you can use it. Logging in to QQ requires a QQ account and password. Similarly, logging in to IM SDK needs a user-specified username (userid) and password (usersig).

You can specify any username you like, but Tencent Cloud will verifies its validity with asymmetric encryption technology. The encryption key and the decryption key used in asymmetric encryption are different. The private key can be kept on your server to asymmetrically encrypt the userid and appid to generate the usersig. At the same time, Tencent Cloud keeps the corresponding public key to verify whether the usersig is valid and is signed by your server.

The public and private keys used to calculate the userig signature can be downloaded from the following location:

![](https://mc.qcloudimg.com/static/img/dc4fd954ebc35f73093708607759828e/image.jpg)



## 4. Cloud Object Storage (COS)
### 4.1 Activating COS service
Cloud Object Storage (COS) is available for any new Tencent Cloud account which has completed identity verification. You can enable it by going to [COS Console](https://console.cloud.tencent.com/cos) to create a Bucket. **Note: Enable CDN acceleration to support HTTPS download (adapt to Apple's ATS)**.
![](//mc.qcloudimg.com/static/img/680aebc55496fe74be3f58102f62dfd5/image.jpg)

### 4.2 What is Bucket?
Bucket is a technical term that can be simply understood as **disk partition**. For example, the COS service purchased from Tencent Cloud can be compared to a new disk purchased from JD.COM. Generally, you partition and format the disk before storing data on it. A partition you create on the disk is similar to a bucket you create on Tencent Cloud COS.

### 4.3 Bucket name
The name you specified during bucket creation is a bucket name. For example, in Example 4.1, xiaozhibo is a bucket name.

### 4.4 COS APPID
Click the [Key Management](https://console.cloud.tencent.com/cos/project) tab on the COS console to get the COS APPID, which must be bound with one pair of APIs.
![](//mc.qcloudimg.com/static/img/60a3a35c5a28603a5ef730a2fd436677/image.png)

### 4.5 COS SecretId and SecretKey
Click the [Key Management](https://console.cloud.tencent.com/cos/project) tab on the COS console to get the SecretId and SecretKey bound with your COS APPID. They are used by APIs for accessing COS. Since COS is a cloud service that has a high requirement for security, if an API fails to transfer a correct key, Tencent Cloud will reject the API request.
![](//mc.qcloudimg.com/static/img/17778b870bae9ad8302ce9774430ca7f/image.png)

## 5. Cloud Virtual Machine (CVM) (optional)
You can use your own server as the business server for deploying backend script. But you're recommended to use Tencent Cloud's CVM for a higher reliability. In addition, if you select Tencent Cloud's Cloud Database to use as a distributed database, you must use Tencent Cloud CVM to access the database.
Log in to the [CVM Console](https://console.cloud.tencent.com/cvm/overview), and then click **Purchase CVM** to go to the CVM purchase page:
![](//mc.qcloudimg.com/static/img/9e479e479a8a6cc72678881f400eefd4/image.jpg)
Click **Next** to go to the image selection page. You are recommended to select a Linux image with Nginx+PHP+MySQL from the marketplace.
![](//mc.qcloudimg.com/static/img/84b60f7ab5e966aed54325a7a2b71beb/image.jpg)
Complete the subsequent steps as instructed by the system. The CVM becomes available when the image is installed.

## 6. Cloud Database (optional)
### 6.1 Activating Cloud Database
Log in to the [Cloud Database Console](https://console.cloud.tencent.com/cdb). If you have not activated the CDB (MYSQL) service, click **New**.
![](//mc.qcloudimg.com/static/img/138c9dd9d5793920aa539141567e0be6/image.jpg)
![](//mc.qcloudimg.com/static/img/62c41e4dbde3eb4f906955e9ebd5cca6/image.jpg)
**Note: The Tencent Cloud account used to activate Cloud Database service should be same as the one used to activate CVM, and the region selected for Cloud Database should be same as the one selected for CVM.**
After the purchase, the instance is displayed in the **Instance List**. Click **Initialize** on the right to set a character set and password for the cloud database.
![](//mc.qcloudimg.com/static/img/492e4be9784f96a32da8d1c17bc5feb5/image.jpg)
![](//mc.qcloudimg.com/static/img/df45399f3da5f324ff2c9f9876d6ee45/image.jpg)

### 6.2 Using the cloud database
After initialization of the instance, the private IP of the instance can be found in the **Instance List**.
![](//mc.qcloudimg.com/static/img/fb0fa5be8c1411c24a9bcfb30fc9ee7e/image.jpg)
You can remotely connect to the database instance to perform operations on it using the mysql command on the CVM, or click **Manage** in the **Instance List** to go to the management page to work with the database:
![](//mc.qcloudimg.com/static/img/3be77388665815bae35b0a496ecac584/image.jpg)

