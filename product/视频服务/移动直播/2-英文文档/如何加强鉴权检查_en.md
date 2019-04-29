This document mainly describes how to further increase security based on existing Mini LVB code. Customers with different security demands may have different standards, you may simply read through the concepts without actually following them, if you do not desire an extremely strong security.

## Backend Protocol Authentication
### 1. What is Authentication?
Authentication (permission authentication) means the server will verify if the current user has logged in when the App interacts with the backend server. Does the user have permission to execute the current operation?

Considering that you will use the native account system, we didn't implement authentication-related security measures in Mini LVB by default because authentication mechanism must be bound with the account system. In other words, Mini LVB **does not authenticate** login status by default.

Current frontend-backend interaction protocols for Mini LVB are listed below:

| Protocol   | Description | Whether login check is required | Reason for login check |
|---------|---------|:---------------------------:| ------------|
| RequestLVBAddr| App requests for push address | Yes| Prevent unauthorized App users from broadcasting |
| ChangeStatus| Change push status of the LVB room| Yes | Prevent malicious users from cancelling normal LVB pushes |
| ChangeCount | Change count items such as number of likes, number of viewers | No | Public information |
| FetchList       | Pull LVB or rewatch list | No | Public information |
| GetCOSSign  | Acquire upload signature of COS file | Yes | Files uploaded by non-logged in users cannot be associated with accounts |
| GetUserInfo  | Acquire detailed information of specified VJ | No | Public information |

- **Viewer end**
It's usually not necessary to check the login status of ordinary viewers, as this will affect the liveliness of LVB.

- **Push end**
It's mandatory to check the login status of VJs, especially when authorities are becoming more strict about verifying the identity of VJs. More and more LVB platforms now require that only verified users may broadcast, in addition to being registered.

Therefore, the main interaction protocols we need to protect are RequestLVBAddr, ChangeStatus and GetCOSSign. The first and second protocols are necessary when creating LVB rooms and are applicable for VJs. GetCOSSign is used to upload information such as cover image of the LVB room. It's login-based, since the information belongs to personal data.


### 2. Standard Solution

It's not difficult to add login session check for backend protocols if the current login and permission verification systems on your backend are already completed. However in this section we still take RequestLVBAddr as example to present a simple explanation:

![](//mc.qcloudimg.com/static/img/1a9e97f735c89d3557c3e76db15bc7e5/image.png)

1. The App encrypts the user name and password using MD5 one-way irreversible encryption method and sends them to the server alongside with user name and time stamp. More secure login protocol calls for a more complex process, such as using password space transposition to prevent rainbow table hack.

2. Once the server verifies that the user is validated registered user, it will assign a short-lived sessionkey to the user and the App will store the sessionkey on the mobile phone.

3. When the VJ taps the "Start LVB" button, the App will initiate a RequestLVBAddr request to the backend. The header of the request needs to include sessionkey (usually placed in the cookie field for HTTP requests)

4. The backend checks the sessionkey, then assign room number and push URL to the App if the sessionkey is valid and unexpired.


## Binding TM Identity

### 1. What to Bind?
The default messaging solution for Mini LVB places identity information of the sender (such as user name, nickname and profile photo) inside the message body in JSON format. This solution is relatively simple and is suitable for chat rooms with low security demands.

If you require higher security, such as strong-bind the identity of the message sender to your account system, which is to say, to make sure the sender's identity corresponds to an existing ID in your account system, you will need to interface with the [**Independent Mode**](https://cloud.tencent.com/document/product/454/7980#3.3-.E7.8B.AC.E7.AB.8B.EF.BC.88.E9.89.B4.E6.9D.83.EF.BC.89.E6.A8.A1.E5.BC.8F) of the IM service.

### 2. Independent Mode 
In independent mode, when an App user successfully logs in, your login server needs to assign a UserSig signature (the signature is calculated using a non-symmetric key agreed on with Tencent Cloud backend) required for imLogin (the first operation step for IM SDK). The user is allowed to send and receive messages after Tencent Cloud confirms the validity of UserSig signature.

This ensures that **only users who have passed the verification of your server are able to pass the verification of IM server.** 

More importantly, since users cannot use the IM feature without your confirmation, you don't need to put the user name and nickname in the IM message body. You can directly identify the sender using the ID in the IM message header, because IM SDK cannot be fabricated if the message header is not cracked. In this way **you can identify the sender's identity in a more secure way**, as mentioned before, to make sure that the sender's identity is strongly bound to your current account system.


### 3. UserSig Signature
UserSig signature is used for mutual authentication between Tencent Cloud IM service backend and your server, to solve the problem that how the servers from two different companies can trust each other. Let's explain with the following example:

> 1. A beautiful lady logs in to your App using the ID and password she registered before. Her ID is "Flower Fairy".
>
> 2. You proceed with the verification immediately after getting her ID and password, and confirm that she can log in to the App. You also issue a **pass (UserSig)** to her, which says "<font color='blue'>'Flower Fairy' is a law-abiding citizen. Make sure she receives proper treatment in Tencent's territory...</font>". In order to ensure that the pass won't be fabricated, you affixed your signature on it.
>
> 3. After reading your pass, Tencent Cloud confirms that the signature is real and provides appropriate services.

This is how interfacing process goes behind message authentication. The core is to prevent users not accepted by your backend server from sending and receiving messages. However, it would be inappropriate to let your server check each one of the messages, so this solution is developed.

UserSig signature uses the most commonly used non-symmetric key encryption technique. When enabling independent mode, you will receive a public and private key pair from Tencent Cloud. You can simply [Encrypt](https://cloud.tencent.com/doc/product/269/1510) specified messages with the private key.


### 4. Interfacing Process
- **Step 1: Select independent mode**
> Ensure the integration mode in Tencent Cloud [IM Console](https://console.cloud.tencent.com/avc) is **Independent Mode**, and download the public and private keys required to calculate signatures.
> ![](//mc.qcloudimg.com/static/img/4e79ff175d8053f8998e02732468e398/image.png)

- **Step 2: Complete interfacing with the backend**
> This step is performed by the backend engineer in your team. The engineer needs to use the signature key obtained in Step 1 to provide your App with an API used to pull the UserSig signature. After a successful login, the App can obtain the calculated UserSig via this API.

- **Step 3: imLogin(ID, UserSig) **
> After obtaining the UserSig issued by your server, the App can call the IM SDK's imLogin (ID, UserSig) API to activate IM services. Tencent Cloud backend will use the public key in Step 1 to decrypt UserSig and verify whether the current user is accepted by your login server.

- **Step 4: Modify messaging logic**
> When modifying the code of the sending end, you don't need to put the sender ID in the message body. Meanwhile, modify the code of the receiving end. Obtain sender ID with more certainty by using the "sender" attribute of TIMMessage.

The above steps are shown in the following figure:
![](//mc.qcloudimg.com/static/img/1e541b2931d0cb8fb1815f26aa8fb493/image.png)



