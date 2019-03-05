## Activating Cloud Services

### Activate LVB

#### 1. Apply for LVB service
Log in to the [LVB Console](https://console.cloud.tencent.com/live). If the service has not been activated yet, the following page will appear:
![](https://mc.qcloudimg.com/static/img/c40ff3b85b3ad9c0cb03170948d93555/image.png)
Click **Apply**, and then go to the application approval step. The service is activated upon the approval of Tencent Cloud.


#### 2. Configure LVB Code
After the LVB service is activated, enter [**LVB Console** -> **LVB Code Access** -> **Access Configuration**](https://console.cloud.tencent.com/live/livecodemanage) to complete configurations, and then activate the LVB Code service:
![](https://mc.qcloudimg.com/static/img/32158e398ab9543b5ac3acf5f04aa86e/image.png)
Click **Confirm Access**.

#### 3. Obtain LVB configuration information
On the LVB console, get `APP_ID`, `APP_BIZID` and `API_KEY` used to configure the server later.
![](https://main.qcloudimg.com/raw/b958c4d3ad29fd6114f92e0c8f7ca458.png)

### Activate Instant Messaging (IM)
#### 1. Apply for IM service
Log in to the [IM Console](https://console.cloud.tencent.com/avc). If you have not activated the service, click the **Activate IM** button. For a new Tencent Cloud account, the IM App list is empty, as shown below:
![](https://mc.qcloudimg.com/static/img/c033ddba671a514c7b160e1c99a08b55/image.png)

Click the **Create Application Access** button to create a new application access, that is, the name of the application for which you want to get the access to Tencent Cloud IM service, as shown below:
![](https://main.qcloudimg.com/raw/fef0a15ebab000272cd74339d4e38c18.png)

Click **OK**, and then you can see in the application list the item you just added, as shown below:
![](https://main.qcloudimg.com/raw/3d522dff19265a5d508ceddf64f15d0e.png)

#### 2. Configure the standalone mode
Click the **Application Configuration** button in the list in the above figure to proceed with the configuration, as shown below.
![](https://mc.qcloudimg.com/static/img/3e9cd34ca195036e21cb487014cc2c81/yuntongxing3.png)

#### 3. Obtain IM configuration information
On the IM console, get `IM_SDKAPPID`, `IM_ACCOUNTTYPE`, `ADMINISTRATOR`, `PRIVATEKEY`, `PUBLICKEY` used to configure the server later.
![](https://main.qcloudimg.com/raw/13ea29f1692106bafd9895e7624e167a.png)

Download and decompress the public and private keys from the Verification Method, and open private_key with a text editor, for example:

```bash
-----BEGIN PRIVATE KEY-----
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
-----END PRIVATE KEY-----
```
Copy the above content directly to the following configuration script to generate an IM signature in the backend of Mini LVB.
Then, convert it to strings as follows, which will be used in the configuration file (config.js) of the server. <font color='red'>Note: Add \r\n at the end of each line</font>:

```bash
"-----BEGIN PRIVATE KEY-----\r\n"+
"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\n"+
"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\n"+
"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\n"+
"-----END PRIVATE KEY-----\r\n"
```

### Activate Cloud Object Storage (COS)
#### 1. Apply for COS service
Log in to the [COS Console](https://console.cloud.tencent.com/cos5). If no bucket has been created, click the **Create Bucket** button as shown below:
![](https://main.qcloudimg.com/raw/caae5820c4b9ab4fa0a9803e7530d263.png)

#### 2. Create a bucket and obtain its basic information
Enter the bucket name, select the region to which the bucket belongs, and configure the read and write permissions to create a bucket.
![](https://main.qcloudimg.com/raw/e2ba00ee3b3b9fd3ab40b67cfd0564c0.jpg)

Click **OK** to go to the management page of the bucket you just created. Select **Basic Configuration** to get `COSKEY_APPID`, `COSKEY_BUCKET`, `COSKEY_BUCKET_REGION` and other information used to configure the server later.
![](https://main.qcloudimg.com/raw/4a9bd0154fa2820887e1a0c79a7d7f0b.jpg)

#### 3. Obtain key information
Go to [**COS Console** -> **Keys** -> **Cloud API Key**](https://console.cloud.tencent.com/cam/capi) to get `COSKEY_SECRETID` and `COSKEY_SECRETKEY`.
![](https://main.qcloudimg.com/raw/b5c6e9471d22d20591d23464dbf717a6.jpg)

## Integration and Deployment at Backend

### Deploy a Tencent Cloud CVM image

**Step 1**: [Create a CVM](https://console.cloud.tencent.com/cvm) 
 ![](http://mc.qcloudimg.com/static/img/53d7df9e5a8bc5141e55231076cbfd74/image.png)

**Step 2**: Go to the **Service Marketplace** to select an image. **Mini LVB** image as shown in the figure is recommended.
 ![](https://main.qcloudimg.com/raw/da14288ee7196c45f0d3fcc4def88567.png)
 
**Step 3**: Configure the disk, network, and the access password for CVM (keep the password well to avoid leakage), and then configure the security group.
![](https://main.qcloudimg.com/raw/c265b5c870f6a7ecb2f15f83f7c508c4.jpg)

**Step 4**: Make the payment to generate the CVM. You can click **Log In** to access the CVM via Tencent Cloud's webpage shell, or use **putty** or **SecretCRT** to log in to the CVM via SSH.
![](http://mc.qcloudimg.com/static/img/0f29fd40aae5fdac10d3f6262eb6a03e/image.png)

**Step 5**: Modify CVM configurations

Configure the `APP_ID`, `APP_BIZID`, `API_KEY`, `COSKEY_BUCKET`, `COSKEY_BUCKET_REGION`, `COSKEY_SECRECTKEY`, `COSKEY_APPID`, `COSKEY_SECRECTID`, `IM_SDKAPPID`, `IM_ACCOUNTTYPE` in the script below to the values generated in the COS service above and save the script.<font color='red'> Then log in to the CVM and execute the modified script directly on the CVM</font>.
The content in double quotation marks following the first echo in the code below is the IM private key. Open the IM private_key with a text editor tool and then copy it into the double quotation marks.

<font color='red'>Note: Modify the following values locally and copy the modified script. Log in to the CVM, paste the script in the console, and then press Enter to execute the script</font>.

```bash
#!/bin/bash
echo "-----BEGIN PRIVATE KEY-----
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
-----END PRIVATE KEY-----" > /data/live_demo_service/deps/sig/private_key;
echo "<?php
define('APP_ID',123456);  //Replace with the appid of the LVB service you applied for
define('APP_BIZID',1234);  //Replace with the bizid of the LVB service you applied for
define('API_KEY','xxxxxxxx'); //api key

define('COSKEY_BUCKET','xxxxxxxx'); //Replace with the bucket created in COS
define('COSKEY_BUCKET_REGION','xxxxxxxx'); //Replace with the region of the bucket created in COS
define('COSKEY_SECRECTKEY','xxxxxxxx'); //Replace with the secrectkey created in COS
define('COSKEY_APPID',123456); //Replace with the appid generated in COS
define('COSKEY_SECRECTID','xxxxxxxx'); //Replace with the secrectid (paired with secrectkey) generated in COS
define('COSKEY_EXPIRED_TIME',30);

define('IM_SDKAPPID',123456);   //IM SDK
define('IM_ACCOUNTTYPE', '1234');  //IM account integration type
?>" > /data/live_demo_service/conf/OutDefine.php;
```

**Now, the deployment at the backend is completed.**

## Configuring RoomService Service

Download the [RoomTool](http://download-1252463788.file.myqcloud.com/RoomTool/RoomTool.zip) first and decompress it.

**Step 1**: Install Nodejs environment
![](https://main.qcloudimg.com/raw/cc2d675ae964e524a5375494b1ed4a7d.png)

**Step 2**: Replace the parameters in the config.js file under the root directory of the toolkit with the values generated in the above LVB and IM services.

 ![](https://main.qcloudimg.com/raw/7e8db26c6384433396df233ab5870e80.png)


**Step 3**: Submit configuration parameters

Go to the RoomTool directory and execute the following command to submit configuration parameters:

```bash
node setConfigInfo.js 1   //1 means to send the private key to the backend of Tencent Cloud RoomService
```

 ![](https://main.qcloudimg.com/raw/8306b0aac96fbe65b320fb07a83a8c8d.png)

After the submission succeeds, execute the node genLoginInfo.js command to verify whether the parameters are configured successfully.

## Integration at Mobile End and Callback Setting

The integration at mobile end mainly refers to the integration of Mini LVB source code and involves the following steps:
### Download Mini LVB source code
[Click here](https://cloud.tencent.com/document/product/454/7873#Xiaozhibo) to download **Mini LVB IOS** and **Mini LVB Android** source codes.

### Change the address of Mini LVB backend server
- iOS

> After the source code package is decompressed, you can find a **TCConstants.h** file in the TCLVBIMDemo/Classes/LVB/Base directory. Change the `kHttpServerAddr` in the file to the address of your CVM.

- Android 

> After the source code package is decompressed, you can find a **TCConstants.java** file in the app/src/main/java/com/tencent/qcloud/xiaozhibo/common/utils directory. Change the `APP_SVR_URL` in the file to the address of your CVM.

`Note: If no certificate is configured for the CVM, then HTTP, instead of HTTPS, must be used in the CVM address. `

### Set a callback address
Set a callback address on the LVB console. When such event as stream status change, video recording completion, screenshot completion occurs, the Tencent Cloud backend gives a callback to the business server via this address for handling the event. For more information, please see [Event Notification Messages](https://cloud.tencent.com/document/product/267/5957).
Go to [**LVB Console** -> **LVB Code Access** -> **Access Configuration**](https://console.cloud.tencent.com/live/livecodemanage) to configure the callback URL. If you do not modify the code of Mini LVB business server, the callback URL format is:

```bash
http://您的云主机服务器地址/callback/tape_callback.php
```

![](http://mc.qcloudimg.com/static/img/b0a78a4b974824940abe811d42fb0561/image.jpg)


