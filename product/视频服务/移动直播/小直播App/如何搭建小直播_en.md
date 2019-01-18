## 1. Frontend and Backend Architectures of Mini LVB

![](//mc.qcloudimg.com/static/img/491b2ff7a8dcd38948d2ad1fd02a90f2/image.png)

- **Tencent Cloud:** Provide **Cloud Live Video Broadcasting (LVB)**, **Video On-Demand (VOD)**, **Instant Messaging (IM)**, **Cloud Object Storage (COS)**, **Cloud Virtual Machine (CVM)** and other cloud products.
- **Business Server:** Also known as customer backend server, which is used to meet customers' own business needs. It serves as the "glue" between mobile devices and Tencent Cloud.
- **Mobile Device:** Integrated features include text interaction, on-screen comment, giving a like with floating heart animation, beauty filter, skin effect, joint broadcasting, authentication, etc. SDKs for **iOS** and **Android** platforms have been provided for development and integration.


| Relationship | Interactions | 
|:--------:|:---------:|
| Business Server - Tencent Cloud | Tencent Cloud makes a callback to business server to notify status, such as a notification on recording completion. |
| Business Server - Mobile Device | LVB/Replay list management; IM room management; generation of signature for COS upload; and generation of push URLs. |
| Mobile Device - Tencent Cloud | Push and pull of audio and video streams; sending and receipt of IM messages | 


## 2. Relevant Cloud Services and Activation Methods

### 2.1 Overview of Cloud Services for Mini LVB:

| Link to Activation Method | Short Name | Description | Availability for Trial| Replaceable |
|:--------:|:---------:|---------|:-----: |:----:|
| [LVB](https://cloud.tencent.com/document/product/454/7953#1.1-.E5.A6.82.E4.BD.95.E5.BC.80.E9.80.9A.E8.A7.86.E9.A2.91.E7.9B.B4.E6.92.AD.E6.9C.8D.E5.8A.A1) | LVB | A service required for both push and viewing videos. It is the only service that requires users to go through Tencent Cloud's **manual audit**. | 20 CNY voucher | Yes |
| [Video on-demand](https://cloud.tencent.com/document/product/454/7953#2.1-.E5.A6.82.E4.BD.95.E5.BC.80.E9.80.9A.E8.A7.86.E9.A2.91.E7.82.B9.E6.92.AD.E6.9C.8D.E5.8A.A1) | VOD | Mini LVB allows the LVB content to be recorded and presented in the form of playback list, and the storage of video files is achieved through Tencent Cloud's VOD service. | 30 CNY voucher | Yes |
| [Instant Messaging](https://cloud.tencent.com/document/product/454/7953#3.-.E4.BA.91.E9.80.9A.E8.AE.AF.E6.9C.8D.E5.8A.A1.EF.BC.88im.EF.BC.89) | IM | Provide basic messaging services such as sending and receipt of messages, online and offline status display, offline message caching, chatroom, etc. Such features as interactive messages, on-screen comment and giving a like in Mini LVB are built on these basic messaging services. | Free of charge if number of daily active users is below 100K | Yes |
| [Cloud Object Storage](https://cloud.tencent.com/document/product/454/7953#4.-.E5.AF.B9.E8.B1.A1.E5.AD.98.E5.82.A8.E6.9C.8D.E5.8A.A1.EF.BC.88cos.EF.BC.89) | COS | Used to upload and download images in Mini LVB such as LVB covers and user profile photos. You can also use your own file server instead. | 50 GB of free space | Yes |

### 2.2 Activating Cloud Services
Please see [How to Activate Cloud Services](https://cloud.tencent.com/document/product/454/7953)


	Notes:
	
	When Tencent Cloud makes a callback to business server, it implements callback logic through the API Live_callback.php on the server. 
	
	The callback URL of LVB Console needs to be configured as: `http://IP or domain name of business server/callback/Live_callback.php`

## 3. Integration and Deployment at Backend
### 3.1. Steps and Methods for Deployment at Backend
**Deployment Steps**
- **Step 1: Get the server and network ready**
- **Step 2: Deploy an environment**
- **Step 3: Configure Tencent Cloud service parameters**
- **Step 4: Verify whether the deployment is completed**

**Deployment Methods**
- **Method 1: Self-owned server - Integration-based deployment**
If you have both backend R&D capabilities and backend server resources and want an integration with your existing businesses at backend, Method 1 is recommended.

- **Method 2: Tencent Cloud CVM - Quick deployment**
If you have no backend development resources (or the features of Mini LVB are sufficient to meet your needs), and you want to get started with the service quickly, Method 2 is recommended.

### 3.2. Deployment Environment
We provide a set of **Nginx + PHP + MySQL** backend source codes, which are recommended to be deployed on a **CentOS 64-bit** system. It is the set of source codes that are used for building the backend of Mini LVB for trial on AppStore.


| Environment | Description | Recommended Version | Learn More |
|--|--|:--|:--:|--:|
| **Nginx** | A lightweight Web server/reverse proxy server featuring **a low memory usage** and **high concurrence capability**. | Latest stable version | [Official Website](http://nginx.org/) |
| **PHP** | A common open-source scripting language. **Easy to grasp** and **widely used**, it features a **high execution efficiency** and is suitable for Web development. | Latest stable version | [Official Website](http://www.php.net/) |
| **MySQL** | As **the most popular** relational database management system, MySQL is one of the best RDBMS applications in terms of Web application. | 5.6 and above | [Official Website](http://www.mysql.com/) |

### 3.3. Tencent Cloud Service Parameters
 Tencent Cloud services such as LVB, IM, VOD and COS are independent of each other, with each having a set of calls to achieve feature integration internally and a set of APIs to be called by customers' services externally. In essence, VOD has a dependency on COS. Cloud service parameters are divided into the following three categories:
 - **Parameters for identification**: Various IDs used to identify applications, businesses, customers, etc.
 - **Parameters for secure calls**: Various keys. The access security of API call is based on digital signature or symmetric encryption + MD5 technologies.
 - **Parameters for internal systems**: The bucket parameter of COS is a typical example. A bucket is like a hard drive, on which the VOD files are stored in COS.

**Overview of Cloud Service Parameters for Mini LVB**

| Service | Parameter | Description | How to Acquire |
|--| :-------------------------- |: ----------------- | ---- |
| LVB | bizid | Identify Cloud LVB businesses. The ID generally contains 4 digits | [DOC](https://cloud.tencent.com/document/product/454/7953#1.4-.E6.9F.A5.E8.AF.A2.E6.88.91.E7.9A.84.E7.9B.B4.E6.92.ADbizid) |
| LVB | appid | Identify Cloud LVB applications. The ID generally contains 10 digits | [DOC](https://cloud.tencent.com/document/product/454/7953#1.3-.E6.9F.A5.E8.AF.A2.E6.88.91.E7.9A.84.E7.9B.B4.E6.92.ADappid) |
| LVB | Push hotlink protection KEY | Used to ensure the validity of the source of push URL | [DOC](https://cloud.tencent.com/document/product/454/7953#1.5-.E6.9F.A5.E8.AF.A2.E6.8E.A8.E6.B5.81.E9.98.B2.E7.9B.97.E9.93.BEkey) |
| LVB | API Authentication KEY | Used by backend to authenticate the validity of URL callback | [DOC](https://cloud.tencent.com/document/product/454/7953#1.6-.E6.9F.A5.E8.AF.A2api.E8.AE.BF.E9.97.AE.E9.89.B4.E6.9D.83key) |
| COS | APPID | Identify COS applications | [DOC](https://cloud.tencent.com/document/product/454/7953#4.4-.E6.9F.A5.E8.AF.A2.E6.88.91.E7.9A.84cos-appid) |
| COS | Bucket Name | Specify the location for storing the files in COS | [DOC](https://cloud.tencent.com/document/product/454/7953#4.3-.E6.9F.A5.E8.AF.A2.E6.88.91.E7.9A.84bucketname) |
| COS | SecretId | COS API. This is a Keychain ID, which is generally available in a pair | [DOC](https://cloud.tencent.com/document/product/454/7953#4.5-.E6.9F.A5.E8.AF.A2.E6.88.91.E7.9A.84cos-secretid-.E5.92.8C-secretkey) |
| COS | SecretKey | COS API. This is a Keychain Key used with the Keychain ID to ensure the validity of API call requests | [DOC](https://cloud.tencent.com/document/product/454/7953#4.5-.E6.9F.A5.E8.AF.A2.E6.88.91.E7.9A.84cos-secretid-.E5.92.8C-secretkey) |

### 3.4. Self-owned Server - Integration-based Deployment
- **Step 1. Get the server and network ready**
> When the recording or LVB is finished, Tencent Cloud will notify your business server using the callback URL parameter you specified on LVB Console. Therefore, it is necessary to ensure the server has a public IP that **can be accessed from the public network**.
- **Step 2. Deploy an environment**
> - Download and install the software such as Nginx, PHP and MySQL as well as the software they are dependent on, and then start MySQL.
> - Download [PHP source code for Mini LVB](https://cloud.tencent.com/document/product/454/6991), and upload it to the business server.
> - Decompress the source code, and then execute createDB.sh to create a database. Ensure MySQL service is running before the execution.
> ![](//mc.qcloudimg.com/static/img/c35c3ddb8c1204cba4d4cfa1e4870a88/image.png)
- **Step 3. Configure Tencent Cloud service parameters**
> - Locate OutDefine.php file under the directory live_demo_service/conf of the zip file, modify the relevant parameters, and then save the modifications.
> ![](//mc.qcloudimg.com/static/img/fb1623bc86f24257f470414a3c1715ae/image.png)
> ![](//mc.qcloudimg.com/static/img/52f024b246a9d329cec083184c64acab/image.png)
> ![](//mc.qcloudimg.com/static/img/134809e0b53e2ee3e07a1c37066ccd09/image.png)
> - In the zip file, you can find two files - live_demo.nginx and nginx.conf - copy live_demo.nginx to the directory /etc/nginx/, and copy live_demo_service to the directory /data. Under the directory /etc/nginx, there is a file called nginx.conf. Modify it by referring to the nginx.conf file in the zip file and verify whether **"include live_demo.nginx;"** exists under the HTTP configuration option. Ensure the root parameters and Mini LVB source code in live_demo.nginx have the same path.
> ![](//mc.qcloudimg.com/static/img/83a38d5cd81059642eb381270dec6d35/image.png)
> - Start PHP and then start Nginx.
> 
- **Step 4. Verify deployment completion**
> Enter `http://your server IP/interface.php` on your browser. The returned result of "{"returnValue":4001,"returnMsg":"json format error","returnData":[]}" indicates PHP is in a running status and the API can be accessed from the public network. Now, the deployment at backend is completed.
> The reason for receiving **"json format error"** is the request is initiated without parameter. After being wrapped by the mobile device source code for Mini LVB, the API request becomes normal. For more information about the APIs, please see [Analysis of Frontend and Backend Protocols for Mini LVB](https://cloud.tencent.com/document/product/454/7895).


### 3.5. Tencent Cloud CVM - Quick Deployment
The last two steps of this deployment method are same as those of **Self-owned server - Integration-based deployment**. But this method simplifies the first two steps. Combined with **Image Marketplace** service, [Tencent Cloud CVM](https://cloud.tencent.com/document/product/213/495) allows you to achieve a quick deployment with ease.

**Prepare a CVM:**
- **Step 1**: [Create a CVM](https://console.cloud.tencent.com/cvm) 
> ![](//mc.qcloudimg.com/static/img/53d7df9e5a8bc5141e55231076cbfd74/image.png)

- **Step 2**: Go to the service marketplace to select images. The **PHP running environment (CentOS 64-bit PHP5.4 Niginx)** shown in the figure is recommended.
> ![](//mc.qcloudimg.com/static/img/568a25630c61d22f43171b2df59c213a/image.png)
> 
- **Step 3**: Configure the disk and network, and set the access password for CVM (keep the password well).

- **Step 4** Make the payment to generate the CVM. You can click "Log In" to access the CVM through Tencent Cloud's webpage shell, or use SSH to log in to the CVM through **putty** or **SecretCRT**.
> ![](//mc.qcloudimg.com/static/img/0f29fd40aae5fdac10d3f6262eb6a03e/image.png)

The remaining steps are same as those of **Self-owned Server - Integration-based Deployment** as described above.

**The completion of backend deployment means the large part of integration has been completed. The integration at mobile device that needs to be done next is relatively simple.**

## 4. Integration at Mobile End and Callback Setting

The integration at mobile end mainly refers to the integration of Mini LVB source code and involves the following steps:
### 4.1. Downloading Mini LVB Source Code
For download links for **Mini LVB IOS** and **Mini LVB Android** source codes, click [Mini LVB source code download](https://cloud.tencent.com/document/product/454/6991).

### 4.2. Overview of Mobile Device Parameters
**Parameters and their definitions** 

| Parameter Name | Android Variable Name | IOS Variable Name | Definition |
|------------|----------|----------|----------|
| **SdkAppId**| IMSDK_APPID | kTCIMSDKAppId | Identify an IM application |
| **AccountType** | IMSDK_ACCOUNT_TYPE | kTCIMSDKAccountType | Account type related to IM. Mini LVB uses the [Hosted Mode](https://cloud.tencent.com/document/product/269/1509), which should be selected upon the creation of an IM application. Another mode is [Standalone Mode](https://cloud.tencent.com/document/product/269/1508), which is used for the integration with your exist account system.
| **APPID** | COS_APPID | kTCCOSAppId | Identify COS applications |
| **Bucket Name** | COS_BUCKET | kTCCOSBucket | Specify the location where the file is stored on COS |
| **Region Code** | COS_REGION | kTCCOSRegion | Related to COS and used to specify the region where the Bucket resides in, the actual DC of COS. Three regions are available, East China (sh), North China (tj) and South China (gz). |
| **ServerAddr** | SVR_POST_URL | kHttpServerAddr | The request address of business server at backend: `http://your server IP or domain name/interface.php` |

### 4.3. Replacement of Mobile Device Parameters
After the Android source code package is decompressed, there is a **TCConstants.java** file under the directory app/src/main/java/com/tencent/qcloud/xiaozhibo/base. Similarly, after the IOS source code package is decompressed, there is a **TCConstants.h** file under the directory TCLVBIMDemo/Classes/LVB/Base. Replace the default field values in source code (**null or 0**) with the relevant field values.
**Parameter acquisition:**
[SdkAppId Acquisition](https://cloud.tencent.com/document/product/454/7953#3.2-im-sdk-appid), [AccountType Acquisition](https://cloud.tencent.com/document/product/454/7953#3.3-im-sdk-.E8.B4.A6.E5.8F.B7.E7.B1.BB.E5.9E.8B), [COS Region Acquisition](https://cloud.tencent.com/document/product/454/7953#4.-.E5.AF.B9.E8.B1.A1.E5.AD.98.E5.82.A8.E6.9C.8D.E5.8A.A1.EF.BC.88cos.EF.BC.89).

### 4.4. Setting Callback Address
Set a callback address on the LVB management console. When such event as stream status change, video recording completion, screenshot completion occurs, Tencent Cloud backend gives a callback to the business server via this address for handling the event. For more information, please see [Event Notification Messages](https://cloud.tencent.com/document/product/267/5957).
Configuration method:
Go to ["LVB Console" -> "LVB Code Access" -> "Access Configuration"](https://console.cloud.tencent.com/live/livecodemanage) to configure the callback URL. If you do not modify the code of Mini LVB business server, the callback URL format is: `http://your server IP or domain name/callback/Live_callback.php`.
![](//mc.qcloudimg.com/static/img/b0a78a4b974824940abe811d42fb0561/image.jpg)

### 4.5. Prepared Execution on Physical Machine
For Android, **Android Studio 2.2** is recommended. For IOS, **XCode8.1** is recommended.
For more information on source code structure, please see [Android Code Description](https://cloud.tencent.com/document/product/454/7892) and [iOS Code Description](https://cloud.tencent.com/document/product/454/7894).

### 4.6. Verifying Features
- Sign in
- Start LVB and push
- Pull the playlist
- Play LVB and **replay**
	> 
	> **Note: The replay feature of Mini LVB uses transcoded recording, with the fee for each channel being 30 CNY per month. The number of channels refers to the number of concurrent pushes. For example, if your maximum number of concurrent pushes within a month is 2, the recording fee billed for this month is 30*2=60 CNY.**
	> 
	During the test period, you're recommended to use a single channel to save cost. If you want to achieve multi-channel debugging while saving the recording cost as much as possible, modify the **RequestLVBAddr.php** file at the Mini LVB backend by removing the joined URL parameter **record=flv|hls**. Alternatively, you can remove the parameter **record=flv|hls** in the push address requested in the mobile device code so as to temporarily disable the recording feature, and then enable it after going online. For more information on how to use push address with parameters to start recording, please see [Recording and Replay](https://cloud.tencent.com/document/product/454/6852)
 

- Modify profile photo
- Upload cover
- Comment
- On-screen Comment
- Give "Like"
- Beauty filter
- **Joint Broadcasting**: supported by Mini LVB 1.8.2. ([How to Achieve Joint Broadcasting](https://cloud.tencent.com/document/product/454/8092).
- **Dynamic Effect**: Not included in source code. An agreement is needed for the paid use of this feature.

**Now, the frontend and backend integration of Mini LVB is completed. For any problems encountered during the verification process, please see the Problems And Solutions During The Integration.**

## 5. Problems and Solutions During the Integration
### 5.1. Apple ATS Support
Apple's new policy requires the use of ATS for IOS applications. The original implementation date is January 1, 2017, but it has been put off. ATS could affect the communication between iOS Mini LVB and business server at backend.
To support ATS, two preconditions should be met:
- The backend server supports **HTTPS**.
> HTTPS requires that the business server has a DV certificate issued by CA for domain name verification. If you do not have a certificate, you can [apply for a free certificate of Tencent Cloud](https://console.cloud.tencent.com/ssl), of which the validity period is 1 year. Before applying for the certificate, you need to get your domain name ready. You can [buy a domain name](https://buy.cloud.tencent.com/domain?tlds=.cn) from Tencent Cloud in advance. The domain name purchased in this example is tcmlvb.cn (25 CNY/year). You need to bind cgi.tcmlvb.cn to the certificate. Make sure that the domain name cgi.tcmlvb.cn points to the public IP of the CVM you purchased.
> **Step 1. Apply for a free certificate:**
> ![](//mc.qcloudimg.com/static/img/603afe4ae7fa1aba61f2aad11e8d2fbc/image.png)
> 
> ![](//mc.qcloudimg.com/static/img/028bae9f244a013b13b1a7c003f67930/image.png)
> 
> ![](//mc.qcloudimg.com/static/img/7274fefc07fe6b16bbb9eb61a944ca4f/image.png)
> **Step 2. Deploy the certificate on the backend server after your application is approved:**
> First, [download the certificate](https://console.cloud.tencent.com/ssl). Find the certificate and click the "Download" button, and then upload it to the business server using WinScp or other tools. Next, modify the configuration of live_demo.nginx by referring to [Certificate Deployment](https://cloud.tencent.com/document/product/400/4143#2.-nginx-.E8.AF.81.E4.B9.A6.E9.83.A8.E7.BD.B2). Save the modification and restart (Shell command: **nginx -s reload**)
> **Step 3. Verify the completion of certificate deployment:**
> Enter https://cgi.tcmlvb.cn/interface.php in the browser's address bar. A returned result indicates the successful deployment of HTTPS.
> 
> ![](//mc.qcloudimg.com/static/img/d3e3d8bf476b03ce86989740c760b25f/image.png)
- **kHttpServerAddr** switches to HTTPS protocol: `https://business server domain name/interface.php.

### 5.2. How to Use your Own Account System?
Please see [How to Use your Own Account System](https://cloud.tencent.com/document/product/454/7981)

### 5.3. How to Strengthen Login Authentication Check?
Please see [How to Strengthen Login Authentication Check](https://cloud.tencent.com/document/product/454/6562)

### 5.4. Other Problems
Please see [Troubleshooting](https://cloud.tencent.com/document/product/454/8110)



