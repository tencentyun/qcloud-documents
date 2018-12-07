## Overview

Thank you for using [Tencent Cloud Game Multimedia Engine SDK](https://intl.cloud.tencent.com/product/tmg?idx=2). This document provides a detailed steps  that makes it easy for developers to integrate GME SDK.

Follow the steps below to use GME:
1. [Create a GME service in Tencent Cloud backend](https://intl.cloud.tencent.com/document/product/607/10782#create-a-service);
2. [Download the corresponding version SDK](https://intl.cloud.tencent.com/document/product/607/10782#download-sdk);
3. [Import the SDK to your project by referring to the integration API document](https://intl.cloud.tencent.com/document/product/607/10782#related-sdk-technical-documents);
4. [Check the daily operation backend statistics](https://intl.cloud.tencent.com/document/product/607/10782#usage-statistics-on-the-console);
5. [Troubleshoot special problems during integration and provide feedback](https://intl.cloud.tencent.com/document/product/607/10782#special-problems-handling);


## Create a service
#### 1. After you log in, click **Create Application**.
![](https://main.qcloudimg.com/raw/07aa53fca65f84c4c43ba73417796ce4.png)

#### 2. Enter required information.  
Enter required information on the page, and select the services as needed. 
> The charges vary with different billing modes. The billing mode cannot be modified once set. For more information on the charges, please see [Product Prices](https://intl.cloud.tencent.com/product/tmg?idx=1#price) and consult relevant Tencent Cloud service personnel.
> If you are creating a game application, you need to select the corresponding platform engine, and select an applicable sampling rate according to the solution provided by the technician.
> The setting for voice messaging and voice-to-context conversion services can be modified.

![](https://main.qcloudimg.com/raw/ff4d89cb84137670142535271ddbf2b2.png)


#### 3. After an application is created, the application management list displays the new application.
The AppID in the list will be used as a parameter in the integration of SDK.

![](https://main.qcloudimg.com/raw/664dbdaded600e650ed44b25b18a3ca8.png)


#### 4. Click **Setting** corresponding to the application in the list to enter the application setting page.
![](https://main.qcloudimg.com/raw/ad13c32afec03001858782a3d000ac28.png)
You can click **Modify** to modify the information in the Application Information module.


#### 5. You can obtain the authentication of your application in the Authentication Information module.
![](https://main.qcloudimg.com/raw/bed3c36cdf3fcb421878c64cd5d775ba.png)

 - The permission key in this module will be used as a parameter in the integration of SDK. 
 - The modified key takes effect within 15 minutes to 1 hour. Frequent modification is not recommended.
 - Click **Download Public and Private Keys** to download the public and private keys for the offline voice feature of the application.
 - Only the account creating the game, the main account and the global collaborator can **Reset the Keys**.
 
 ![](https://main.qcloudimg.com/raw/2eb67cb291d211ed6eaa352fd08c10f6.png)

-  **For more information on authentication, please see the [GME key documentation](https://intl.cloud.tencent.com/document/product/607/12218)**.


#### 6. Enable and disable businesses and services

You can enable or disable businesses and services.
![](https://main.qcloudimg.com/raw/b1335c003b6a01a049ca992ed36feec2.png)

![](https://main.qcloudimg.com/raw/cabf597540281e1df1e028944b5dde01.png)

## Download SDK 
#### 1. Download link
Please download applicable Demo and SDK from [Tencent Cloud GME official website](https://intl.cloud.tencent.com/product/tmg?idx=1).

#### 2. Integration preparations
To integrate the SDK, you need to use the AppID and the permission key provided by Tencent Cloud, as mentioned above.
- The permission key in the Authentication Information module is used for the integration of voice chat.
- The downloaded public and private keys in the Authentication Information module are used for the integration of offline voice.

For the configuration for other platforms, please see the project configuration document of relevant platform.

#### 3. Notes for using the official sample code
The sample code provides a Tencent Cloud test account for you to experience features. If you want to use personal or corporate test account, you need to change the Tencent Cloud test account AppID to the AppID obtained in the console on relevant page in the Demo, and modify the permission key for voice chat in the AVChatViewController-GetAuthBuffer function.

## Related SDK Technical Documents
**Unity engine** 
[Unity Project Configuration](https://intl.cloud.tencent.com/document/product/607/10783)     [Unity integration technical document](https://intl.cloud.tencent.com/document/product/607/15228)

**Unreal engine**
[Unreal Engine Project Configuration](https://intl.cloud.tencent.com/document/product/607/17025)     [Unreal Engine integration technical document](https://intl.cloud.tencent.com/document/product/607/15231)

**Cocos2D engine**
[Cocos2D-X Project Configuration](https://intl.cloud.tencent.com/document/product/607/15216)     [Cocos2D-X integration technical document](https://intl.cloud.tencent.com/document/product/607/15218)

**Native application**
[PC (C++) integration technical document](https://intl.cloud.tencent.com/document/product/607/15232)
[iOS Project Configuration](https://intl.cloud.tencent.com/document/product/607/15219)     [iOS integration technical document](https://intl.cloud.tencent.com/document/product/607/15221)
[Android Project Configuration](https://intl.cloud.tencent.com/document/product/607/15203)     [Android integration technical document](https://intl.cloud.tencent.com/document/product/607/15210)


## Usage Statistics on the Console
[Operational Guide](https://intl.cloud.tencent.com/document/product/607/17448)


## Special Problems Handling
[FAQs](https://intl.cloud.tencent.com/document/product/607/17359)    
[Error Codes](https://intl.cloud.tencent.com/document/product/607/15173)

