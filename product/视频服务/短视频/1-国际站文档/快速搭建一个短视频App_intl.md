## Activate Service

### Step 1. Sign up and log in
You need to sign up for a Tencent Cloud account if you don't have one. For more information on sign-up, please see [Sign up for Tencent Cloud](https://cloud.tencent.com/document/product/378/9603).

Log in to the Tencent Cloud VOD [Console](https://console.cloud.tencent.com/vod). If this is your first login, you need to complete the identity verification and apply for activating the VOD service first.
If your account has not gone through identity verification, go to [Account Center](https://console.cloud.tencent.com/developer) for identity verification. For more information, please see [Identity Verification Guide](https://cloud.tencent.com/document/product/378/3629).

### Step 2. Activate VOD service
Tencent Cloud Video on Demand (VOD) supports two billing methods: daily settlement (Postpaid) and package (Prepaid). For the purchase guide, please see [Price Overview](https://cloud.tencent.com/document/product/266/2838).

If you have completed identity verification, you can go directly to the VOD [Console](https://console.cloud.tencent.com/vod) to proceed to the next step.
![](https://mc.qcloudimg.com/static/img/dba813de6119f0825762b2d9abed41e6/image.png)

### Step 3. Activate Cloud Object Storage (COS)

#### 3.1 Apply for COS service
Log in to [COS Console](https://console.cloud.tencent.com/cos5). If no bucket has been created, click the **Create Bucket** button as shown below:
![](https://main.qcloudimg.com/raw/caae5820c4b9ab4fa0a9803e7530d263.png)

#### 3.2 Create a bucket and obtain its basic information
Enter the bucket name, select the region to which the bucket belongs, and configure the read and write permissions to create a bucket.
![](https://main.qcloudimg.com/raw/a4bd6a664adb2b80da8a1451620888f9.png)

Click the **OK** button to go to the management page of the bucket you just created. Select **Basic Configuration** to get `COSKEY_APPID`, `COSKEY_BUCKET`, `COSKEY_BUCKET_REGION` and other information used to configure the server later.
![](https://main.qcloudimg.com/raw/06f63e94e4d47d46573d5e6e5b657308.png)

#### 3.3 Obtain Key information
Go to [**COS Console** -> **Keys** -> **Cloud API Key**](https://console.cloud.tencent.com/cam/capi) to get `COSKEY_SECRETID` and `COSKEY_SECRETKEY`.
![](https://main.qcloudimg.com/raw/fa6ad645117118a2027f8e0e76df48d4.png)


## Backend Deployment

#### Step 1: [Create a CVM](https://console.cloud.tencent.com/cvm) 
 ![](http://mc.qcloudimg.com/static/img/53d7df9e5a8bc5141e55231076cbfd74/image.png)

#### Step 2: Go to **Service Marketplace** to select an image. **Mini LVB** image as shown in the figure is recommended. (Note: Mini Video uses the Mini LVB image as a backend service).
 ![](https://main.qcloudimg.com/raw/da14288ee7196c45f0d3fcc4def88567.png)

#### Step 3: Configure the disk, network, and the access password for CVM (keep the password well to avoid leakage), and then configure the security group.
![](https://main.qcloudimg.com/raw/d81d282ab01ce1309ac704c5aa61a544.png)

#### Step 4: Make the payment to generate the CVM. You can click **Log In** to access the CVM via Tencent Cloud's webpage shell, or use **putty** or **SecretCRT** to log in to the CVM via SSH.
![](http://mc.qcloudimg.com/static/img/0f29fd40aae5fdac10d3f6262eb6a03e/image.png)

#### Step 5: Modify CVM configurations

Configure the `COSKEY_BUCKET`, `COSKEY_BUCKET_REGION`, `COSKEY_SECRECTKEY`, `COSKEY_APPID`, `COSKEY_SECRECTID`, `CLOUD_API_SECRETID` and `CLOUD_API_SECRETKEY` in the script below to the values generated in the COS service above and save the script. <font color='red'>Then log in to the CVM and execute the modified script directly on the CVM</font>.

<font color='red'>Note: Modify the following values locally and copy the modified script. Log in to the CVM, paste the script in the console, and then press Enter to execute the script</font>.

```bash
#!/bin/bash
echo "<?php
define('COSKEY_BUCKET','xxxxxxxx'); //Replace with the bucket created in COS
define('COSKEY_BUCKET_REGION','xxxxxxxx'); //Replace with the region of the bucket created in COS
define('COSKEY_SECRECTKEY','xxxxxxxx'); //Replace with secrectkey created in COS
define('COSKEY_APPID',123456); //Replace with the appid generated in COS
define('COSKEY_SECRECTID','xxxxxxxx'); //Replace with the secrectid (paired with secrectkey) generated in COS
define('COSKEY_EXPIRED_TIME',30);
define('CLOUD_API_SECRETID','xxxxxx');  //COS SecretId
define('CLOUD_API_SECRETKEY','xxxxxx');  //COS SecrectKey
?>" > /data/live_demo_service/conf/OutDefine.php;
```

## Integration at terminal

### Step 1. Download Mini Video source code
Click [DOWNLOAD](https://cloud.tencent.com/document/product/584/9366#APP) to download the source code of Mini Video App.

### Step 2. Confirm the project configuration
#### XCode 
- Xcode 9 or above
- OS X 10.10 or above

#### Android Studio
- Android NDK: android-ndk-r12b
- Android SDK Tools: android-sdk_26.0.2
  - minSdkVersion: 15
  - targetSdkVersion: 21
- Android Studio (Android Studio is recommended. You can also use Eclipse+ADT)

### Step 3. Replace the backend address
#### iOS 
After the source code package is decompressed, you can find a **TCConstants.h** file in the TXXiaoShiPinDemo/Classes/App/ directory. Change the `kHttpServerAddr` in the file to the address of your CVM.

#### Android 
After the source code package is decompressed, you can find a **TCConstants.java** file in the app/src/main/java/com/tencent/qcloud/xiaoshipin/common/utils/ directory. Change the `APP_SVR_URL` in the file to the address of your CVM.

`Note: If no certificate is configured for the CVM, http, instead of https, must be used in the CVM address.`
