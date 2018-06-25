## Background
Replacing the account system is the first task for most customers when they obtain their Mini LVB code, since they can't afford to change their own App account system without a good reason.

We have already taken this into consideration when we designed Mini LVB. All relevant features of Mini LVB were designed **without strongly relying on account system**, making it easier for you to replace the account system.

Still, the features more or less rely on account system, thus we need to adjust and modify the following modules:
- **Chat room module**: Once you replaced the account system, modify this module to change the names of participants into users from your account system.
- **UserInfo module**: Adjustment is required for this module, since all information (such as VJ's profile photo, nickname and cover image) is bound to the account.

## Chat Room Module
You can use **Simple Replacement** mode if you don't want to put up too many restrictions for the chat room participants. For example, to allow any App user to participate;
If you wish to strong-bind every individual in the chat room with an ID in your account system, to ensure that the identity of each participant is confirmed by your server, you can choose **Secure Interface** mode.

### 1. Simple Replacement
With Simple Replacement mode, you simply need to modify several lines of code to replace the participants in the Mini LVB chat room into individuals of your current account system. This mode imposes few security restrictions on the participants.

[Guest Mode](https://cloud.tencent.com/document/product/454/7980#3.2-.E8.AE.BF.E5.AE.A2.EF.BC.88.E6.89.98.E7.AE.A1.EF.BC.89.E6.A8.A1.E5.BC.8F): This is one of the Tencent Cloud IM service operation modes. In this mode, Tencent Cloud assigns a "guest account" for each of the message senders/receivers in the backend, avoiding the need for the IM service to be strongly coupled with your current account system, while also satisfying the restriction where IM service must have an account to send or receive messages.

Each message sender in the chat room sends his or her user information (nickname, profile photo and so on) in the message body as a package, while other receivers in the chat room also resolve the user information from the message body.

- **Step 1: Choose Host Mode**
> Make sure the integration mode in Tencent Cloud [IM Console](https://console.cloud.tencent.com/avc) is **Host Mode**. This mode allows Tencent Cloud to provide backend support to guest accounts in guest mode.
> ![](//mc.qcloudimg.com/static/img/d52ac3662d5310673a5d6c6a78f50da4/image.png)

- **Step 2: Block TLS regular login logic**
> iOS platform: TCLoginViewController##viewDidLoad is used to achieve the "auto login" logic in Mini LVB which uses user name and password.
> Android platform: Calling the userNameLoginViewInit function in TCLoginActivity##onCreate can be considered as "auto login".

- **Step 3: Interface with guest mode only**
> iOS platform: The code used to launch IM SDK in guest mode is located in guestLogin in TCIMPlatform.h.
> Android platform: The code used to launch IM SDK in guest mode is located in the guestLogin function in TCLoginMgr.java.

### 2. Secure Interface
Choose this mode if you need to strong-bind every individual in the chat room with an ID in your account system to ensure that the identity of each participant is confirmed by your server. For more information about the interface method of this mode, please see [How to Bind IM Identity](https://cloud.tencent.com/document/product/454/6562#.E7.BB.91.E5.AE.9Aim.E8.BA.AB.E4.BB.BD).

## UserInfo Module
The "user information" we mentioned here refers to information of the VJ (such as nickname, profile photo), that is, information of the current App user. The VJ information seen by the viewers is already obtained when pulling the list of LVB rooms.

Mini LVB uses Tencent Cloud's account hosting service by default, therefore the default user information is stored in the data system of Tencent Cloud account hosting service. For this reason, the user information needs to be adjusted accordingly when the account is replaced.

### 1. iOS Platform
- **Block previous logic**:
Block the logic which automatically pulls user information from Tencent server. Mini LVB will automatically pull user information from the server upon successful login, you need to block this logic if the information already exists on your own server. Delete the setIdentifier call in TCIMPlatform.m to block the logic:
![](//mc.qcloudimg.com/static/img/6942eb366e524855e8a2a898e6689cf5/image.jpg)
	 
- **Interface with new information**:
The recommended approach is to call the setUserProfile API in TCUserInfoMgr to configure new user information (nickname, profile photo, cover image and so on). The user information will be obtained from the user information management class TCUserInfoMgr when Mini LVB requires such information, which will minimize your adaptation workload:
![](//mc.qcloudimg.com/static/img/e78f80670d85478432e4fe5d932d2430/image.jpg)

### 2. Android Platform
Mini LVB will call the queryUserInfo() function in TCUserInfoMgr upon successful login, according to its default logic. This function is used to pull user information from Tencent Cloud account system and set the information into the member variable "mUserInfo", thus modifying this function is the simplest and fastest adaptation solution:
![](//mc.qcloudimg.com/static/img/3cc88fb62c6b7fac4215c034806f8d06/image.jpg)






