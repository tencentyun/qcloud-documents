## 1 Overview of Account Integration

Tencent Login Service (TLS) is a set of generic account login components provided by Tencent for developers to quickly integrate account into audio/video or IM cloud service (hereinafter called the cloud service).  

### 1.1 Introduction

![](//avc.qcloud.com/wiki2.0/im/imgs/20151117034741_42845.png)
The integration of account system is the fourth step of cloud service access procedure. Before integration of account system, you first need to register a Tencent Cloud account, activate service and create an App. For specific method, click "[App Access Guide](/doc/product/269/应用接入指引)". Account integration is described later in this document. Besides, we made a video about what we discussed here. Click [here](https://cloud.tencent.com/course/detail/133) to watch.

## 2 Overview of Two Modes

(1) If your App has been launched and has many users, [Standalone Mode](/doc/product/269/独立模式) can help you quickly integrate cloud service (**Note: Standalone mode of account does not affect the hosting of data, relation chain and group**).
(2) If you don't want to maintain complex user account system, [Hosted Mode](/doc/product/269/托管模式) can help you quickly build a secure App self-owned account system.

## 3 Appendix

### 3.1 Integration Mode

According to developers' application scenarios, we provide two different methods for account integration from which developers can choose based on their needs:
(1) [Standalone Mode](/doc/product/269/独立模式): User's account information and authentication information (such as registration and password verification) are preserved by developers.
(2) [Hosted Mode](/doc/product/269/托管模式): Tencent Cloud provides developers with services of registration, storage and verification of the password for App account, as well as the verification of hosting of third party's openid and token.

>Note: No change is allowed once the account integration mode is selected, so please proceed with caution. If you want to change the integration mode, please create a new App and complete the account integration procedure.

### 3.2 Public and Private Keys

Public and private keys are the concepts in asymmetric encryption algorithm of cryptography. In asymmetric encryption algorithm, public and private keys come in pairs. The former is open to the public, and the latter is kept private. The data encrypted using public key can only be decrypted with private key, and vise versa. For account integration, public and private keys are used to verify the validity of developer's identity. Application scenarios are as follows:
(1) [Standalone Mode](/doc/product/269/独立模式): Private key and public key are preserved by developer and Tencent respectively. Developers use private key to generate user signature (UserSig) which is verified by Tencent using public key.
(2) [Hosted Mode](/doc/product/269/托管模式): Private key and public key are preserved by Tencent and developer respectively. Tencent use private key to generate user signature (UserSig) which is verified by developers using public key. Please note that, public key is not used for the public account of third party.

For standalone mode, to help developers with rapid development, after they complete account integration, they can [download public and private keys](/doc/product/269/下载公私钥) from the App configuration of App list. In addition, we also provide developers with tools for debugging. For more information, please see [TLS Backend API Development Guide](/doc/product/269/TLS后台API使用手册#1-.E6.A6.82.E8.BF.B0).
For more information about asymmetric algorithm, please see this [article](https://zh.wikipedia.org/wiki/%E5%85%AC%E5%BC%80%E5%AF%86%E9%92%A5%E5%8A%A0%E5%AF%86).

### 3.3 How to Generate Public and Private Keys

For more information, please see the chapter [How to use the tool](/doc/product/269/TLS后台API使用手册#3.1-.E5.B7.A5.E5.85.B7.E4.BD.BF.E7.94.A8) in [TLS Backend API Development Guide](/doc/product/269/TLS后台API使用手册#1-.E6.A6.82.E8.BF.B0).

### 3.4 App Admin

Only admin can call the APIs that are open to the public to perform some operations, for example, disbanding the group, sending C2C messages to users, etc. So in developer's account system, some of the accounts can be identified as admin. After the identity is verified by Tencent, admin can perform some special operations on its business.  
App admin has the highest administrative authority to App. Compared with the ordinary accounts:
(1) It has a higher read permission: For example, it can obtain all the groups within the App, and any data of any group.
(2) It has a higher operation permission: For example, it can send messages to any user, and add or delete members in any group.

When App implements server-side integration by calling REST API, App admin account should be used as identifier for calling. App can set several accounts as admin in the account system. For more information about the settings, please see [here](/doc/product/269/设置APP管理员).

### 3.5 SMS Verification Code

When a developer chooses hosted mode for integration of self-owned account, Tencent provides the registration and login services of the account for the developer. During the development of registration service and features, developer can allow users to register and log in by way of [SMS Verification](/doc/product/269/添加短信签名). The format of verification SMS is as follows:
1234 (XXXX is SMS verification code), please do not forward this code to anyone, otherwise the account may be hacked. "Tencent Cloud"
**Note**
(1) Developers can only modify "XXXX" of the SMS, which can be company name or App name, with a length limited to 30 characters.
(2) "1234" is a random 4-digit number. This number can be generated randomly in practice.
(3) "Tencent Cloud" is a default SMS signature (this signature must be attached when sending SMS as required by ISP). If the number of messages is more than 10,000 each month, you can contact the customer service to customize the SMS signature.
(4) If developer does not enter "XXXX", the default verification SMS is used as follows:
1234 (SMS verification code), please do not forward this code to anyone, otherwise the account may be hacked. "Tencent Cloud"

### 3.6 Format of identifier
identifier is user account ID. The format of this parameter is described as below:
Under standalone mode, it is recommended to limit the length of identifier to 32 bytes. Under hosted mode, it is recommended to limit the length of identifier (string) to 4-24 bytes. Letters and underscores are supported. It is not case sensitive, and cannot contain only numbers.

## 4 Contact Us

For any problems, find solutions [here](http://bbs.qcloud.com/thread-8287-1-1.html). For additional support, please contact TLS Account Support. QQ: 3268519604. Email: tls_assistant@tencent.com.

