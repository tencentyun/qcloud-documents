Welcome to [Tencent Cloud Game Multimedia Engine (GME) SDK](https://cloud.tencent.com/product/tmg?idx=1). This document provides guidance on the access to Tencent Cloud GME SDK, which is applicable to all platforms, so that developers can easily access Tencent Cloud GME.

## Real-Time Audio-Video Service Activation
### 1. Register a Tencent Cloud account.
If you do not have a Tencent Cloud account, you need to register one. For more information about the registration procedure, see the [Tencent Cloud Registration](https://cloud.tencent.com/document/product/378/9603).
If you have a Tencent Cloud account, go to the next step.

### 2. Log in to GME Console.
Open the [home page of the Tencent Cloud official website](https://cloud.tencent.com/). In the top menu bar, click **Products**, and then choose **Video Services** -> **Game Multimedia Engine** to open the [GME introduction page](https://cloud.tencent.com/product/tmg?idx=1).  
![](https://main.qcloudimg.com/raw/907531794d56c48081db773d6db9d7dd.png)

Click **Use Now** on the [GME introduction page](https://cloud.tencent.com/product/tmg?idx=1) and log in to [GME Console](https://console.cloud.tencent.com/gme) with your Tencent Cloud account.
![](https://main.qcloudimg.com/raw/603f2694de75b31ab389ba9d3db9efd0.png)

### 3. Create an application.
After the login, if you do not have any applications, you need to create one. Click **Create Application**. In the pop-up dialog box, enter the information about your new application, select services as required, and click **OK**. After the application is created, it is displayed on the application list.
![](https://main.qcloudimg.com/raw/dde3f2bc0affba796bc77978c7aaa87f.png)

### 4. Finish the application's basic settings.
Click **App Basic Settings**. On the displayed tab page, click **Edit** beside **Account System Integration** to finish the settings.
![](https://main.qcloudimg.com/raw/b5d1b578f5c7034cf51f40e981c4986a.png)
Select an integration mode as required, add a RestApi user account, and click **Save**.
There are two numbers, **accountType** under **Account System Integration** and **SdkAppId** under **Application Information**.
>Note: Remember these two parameters, which will be used for the SetAppInfo API.

![](https://main.qcloudimg.com/raw/f24f18b3735857b6b3e83b7890eebd88.png)

## TLS Signature
Overview: The upload and download of PTT rely on the Tencent Cloud COS platform and require separate authentication. The generation of the signature required for authentication involves the plaintext, key, and algorithm.
### 1. Plaintext
The plaintext includes **appid**, **accountType**, and **openid**.

### 2. Key acquisition
Set the integration mode to **Independent Mode**. Download the public and private key pair .zip file. Select **private_key** as the encryption key of the authentication algorithm.  
![](https://main.qcloudimg.com/raw/c2257d1106ccbe73128d82e8be54853d.png)
Decompress the downloaded .zip file. The following table describes the two files in the package. 

|File Name       |Description    |
| :-----------: | ------------- |
|public_key |Public key.|
|private_key |Private key.|


Open the public key or private key file as required in Notepad, copy the key, and enter the key as a parameter of the relevant function.
>Note: Each time after you download the public and private key pair, you have to wait for one hour before using it.

### 3. Algorithm deployment
It is recommended that you deploy the algorithm on the client during the early access and deploy the algorithm at the application backend later depending on the actual situation.

|Scheme       | Disadvantage        | Description |
| ------------- |:-------------:| ------------- |
| Backend deployment    		|Large workload 				|For more information, see the [TLS Backend API User Manual](https://cloud.tencent.com/document/product/269/1510#1-.E6.A6.82.E8.BF.B0).					|
| Client deployment      	| Large installation package and low security level  		|Two library files **libqav_tlssig.so** (Android) and **QAVSDKTlsSig.framework** (iOS) are added to the project, as well as **QAVSig.cs**. 	|  

For more information, see the documents related to various platforms.

## Audio-Video Key
Tencent Cloud GME provides an audio-video key for the encryption and authentication of ILVB-related features. For more information, see the [Audio-Video Key Instructions](https://cloud.tencent.com/document/product/268/11240).
The generation of the signature required for authentication involves the plaintext, key, and algorithm.
The plaintext is spliced by the following fields in the network byte order.

|Field    		| Type/Length			| Value Description/Remarks|
| ---------------- |------------------- |--------------|
| cVer 				|unsigned char/1 	|Version number/Enter **0**.|
| wAccountLen 		|unsigned short/2 	|Length of the third-party account.	|
| buffAccount 		|wAccountLen 		|Characters of the third-party account.	|
| dwSdkAppid 		|unsigned short/2 	|Value of **SdkAppId**.				|
| dwAuthid 			|unsigned int/4 		|Group number.				|
| dwExpTime 		|unsigned int/4 		|Expiration time (Current time + Validity period [unit: second; recommended value: 300 seconds]).|
| dwPriviegeMap 	|unsigned int/4 		|Permission bit.					|
| dwAccountType 	|unsigned int/4 		|Type of the third-party account.			|


### 1. Key
Obtain the key from [Tencent Cloud Console](https://console.cloud.tencent.com/ilvb?show=2). The **Permission Key** check box is a bug on the page and can be ignored, as it functions regardless of whether it is selected or not.  
![](https://main.qcloudimg.com/raw/28d73b482982b966d6f89e6b241cf5f3.png)

### 2. Algorithm
The TEA symmetric encryption algorithm is used.
It is recommended that you deploy the algorithm on the client during the early access and deploy the algorithm at the game application backend later depending on the actual situation.

|Scheme       		| Disadvantage        				| Description 																															|
| ------------- |:-------------:| ------------- 
| Backend deployment     		|Large workload 				|For more information, see the [Audio-Video Key Instructions](https://cloud.tencent.com/document/product/268/11240).													|
| Client deployment      	| Large installation package and low security level  		|Two library files **libqav_authbuff.so** (Android) and **QAVSDKAuthBuffer.framework** (iOS) are added to the project, as well as **QAVAuthBuffer.cs**. 	|  

For more information, see the documents related to various platforms.
