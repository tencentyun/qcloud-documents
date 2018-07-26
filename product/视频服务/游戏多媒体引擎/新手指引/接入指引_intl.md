## Overview

Thank you for using [Tencent Cloud Game Multimedia Engine SDK](https://cloud.tencent.com/product/tmg?idx=1). This document provides a detailed description that makes it easy for developers to integrate GME SDK.

Follow the steps below to use GME:
1. [Create a GME service in Tencent Cloud backend](#.E6.96.B0.E5.BB.BA.E6.9C.8D.E5.8A.A1);
2. [Download the client SDK of applicable version](#.E4.B8.8B.E8.BD.BD-sdk);
3. [Port the SDK to your project by referring to the integration API document](#.E7.9B.B8.E5.85.B3-sdk-.E6.8A.80.E6.9C.AF.E6.96.87.E6.A1.A3);
4. [Check the daily operation backend statistics](#.E6.8E.A7.E5.88.B6.E5.8F.B0.E7.94.A8.E9.87.8F.E7.BB.9F.E8.AE.A1);
5. [Troubleshoot special problems during integration and provide feedback](#.E7.89.B9.E6.AE.8A.E9.97.AE.E9.A2.98.E5.A4.84.E7.90.86);


## Create a service
#### 1. After you log in, click **Create Application**.
![](https://main.qcloudimg.com/raw/a4b3dbd8aefd9dd032f8c3ce4154b227.png)

#### 2. Enter required information.  
Enter required information on the page, and select the services as needed. 
> The charges vary with different billing modes. The billing mode cannot be modified once set. For more information on the charges, please see [Product Prices](https://cloud.tencent.com/product/tmg?idx=1#price) and consult relevant Tencent Cloud service personnel.
> If you are creating a game application, you need to select the corresponding platform engine, and select an applicable sampling rate according to the solution provided by the technician.
> The setting for voice messaging and voice-to-context conversion services can be modified.

![](https://main.qcloudimg.com/raw/9b5d501b1dc70a850a1a99b533bb22e2.png)


#### 3. After an application is created, the application management list displays the new application.
The AppID in the list will be used as a parameter in the integration of SDK.

![](https://main.qcloudimg.com/raw/9e78b27c75b9bfcd2ce02ae1d02b7046.png)


#### 4. Click **Setting** corresponding to the application in the list to enter the application setting page.
![](https://main.qcloudimg.com/raw/ac27c53e9a07fa819344f668978fe019.png)
You can click **Modify** to modify the information in the Application Information module.


#### 5. You can obtain the authentication of your application in the Authentication Information module.
![](https://main.qcloudimg.com/raw/5642579a36a7df2df90595a518444eb1.png)

 - The permission key in this module will be used as a parameter in the integration of SDK. 
 - The modified key takes effect within 15 minutes to 1 hour. Frequent modification is not recommended.
 - Click **Download Public and Private Keys** to download the public and private keys for the offline voice feature of the application.
 - Only the account creating the game, the main account and the global collaborator can **Reset the Keys**.
 
 ![](https://main.qcloudimg.com/raw/df3f92e2eb50aea9d8dde32f252045f6.png)

-  **For more information on authentication, please see the [GME key documentation](https://cloud.tencent.com/document/product/607/12218)**.


#### 6. Enable and disable businesses and services

You can enable or disable businesses and services.
![](https://main.qcloudimg.com/raw/0de52670541b46347c5d686c89b1ba7c.png)

![](https://main.qcloudimg.com/raw/7dfac502bfbb68bd856cda1b03d77514.png)

## Download SDK 
#### 1. Download link
Please download applicable Demo and SDK from [Tencent Cloud GME official website](https://cloud.tencent.com/product/tmg?idx=1).

#### 2. Integration preparations
To integrate the SDK, you need to use the AppID and the permission key provided by Tencent Cloud, as mentioned above.
- The permission key in the Authentication Information module is used for the integration of voice chat.
- The downloaded public and private keys in the Authentication Information module are used for the integration of offline voice.

For the configuration for other platforms, please see the project configuration document of relevant platform.

#### 3. Notes for using the official Demo
The Demo provides a Tencent Cloud test account for you to experience features. If you want to use personal or corporate test account, you need to change the Tencent Cloud test account AppID to the AppID obtained in the console on relevant page in the Demo, and modify the permission key for voice chat in the AVChatViewController-GetAuthBuffer function.

## Related SDK Technical Documents
**Unity engine** 
[Unity Project Configuration](https://cloud.tencent.com/document/product/607/10783)     [Unity integration technical document](https://cloud.tencent.com/document/product/607/15228)

**Unreal engine**
[Unreal Engine Project Configuration](https://cloud.tencent.com/document/product/607/17025)     [Unreal Engine integration technical document](https://cloud.tencent.com/document/product/607/15231)

**Cocos2D engine**
[Cocos2D-X Project Configuration](https://cloud.tencent.com/document/product/607/15216)     [Cocos2D-X integration technical document](https://cloud.tencent.com/document/product/607/15218)

**Native application**
[PC (C++) integration technical document](https://cloud.tencent.com/document/product/607/15232)
[iOS Project Configuration](https://cloud.tencent.com/document/product/607/15219)     [iOS integration technical document](https://cloud.tencent.com/document/product/607/15221)
[Android Project Configuration](https://cloud.tencent.com/document/product/607/15203)     [Android integration technical document](https://cloud.tencent.com/document/product/607/15210)


## Usage Statistics on the Console
[Operational Guide](https://cloud.tencent.com/document/product/607/17448)


## Special Problems Handling
[FAQs](https://github.com/TencentMediaLab/GME/blob/master/GME%20Developer%20Manual/GME%20FAQ%20Manual.md)     [Error Codes](https://cloud.tencent.com/document/product/607/15173)

