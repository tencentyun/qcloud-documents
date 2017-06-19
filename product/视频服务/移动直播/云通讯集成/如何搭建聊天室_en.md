This document describes how to use [Tencent Cloud IM](https://www.qcloud.com/product/im.html) service to build simple chat room features.
(1) Broadcast ordinary text messages
(2) Broadcast on-screen comments
(3) Broadcast likes
(4) Broadcast system notifications, for example "XXX has joined the room" or "The VJ has left".
![](//mc.qcloudimg.com/static/img/d77b0df57a0aa4b102d13868bbdc4cd4/image.png)

### 1. Activate service
To use Tencent Cloud IM service, you need to activate it first by following these steps:

Go to [IM Console](https://console.qcloud.com/avc). If you have not activated the service yet, just click **Activate IM** button. For a new Tencent Cloud account, the IM App list is empty, as shown below:
![](//mc.qcloudimg.com/static/img/c033ddba671a514c7b160e1c99a08b55/image.png)

Click the **Create App Access** button to create a new App access, that is, the name of the App for which you want to get the access to Tencent Cloud IM service. Our test App is called "Mini LVB Demo", as shown below:
![](//mc.qcloudimg.com/static/img/897bff65af6202322a434b6fa3f8a0bd/image.png)

Click the OK button, then you can see in the App list the item you just added, as shown below:
![](//mc.qcloudimg.com/static/img/1c1cb2c2fa4c6f0dc7be06bf8329dee3/image.png)

## 2. App configuration
In the above figure, the SDKAPPID column displays Tencent Cloud IM service ID, which is used to interface with different IM SDKs on various platforms. Click **App Configuration** button on the right side to proceed with configuration, as shown below:
![](//mc.qcloudimg.com/static/img/d52ac3662d5310673a5d6c6a78f50da4/image.png)

There are many configuration items here, most of which are not important. You may choose not to configure them or modify them as needed at any time. For example:

| Configuration Items | Description |
|-------|---------|
| Account Name | You can enter any name you like, but avoid using weird characters.
| Verification Mode | Currently, only "System-Generated Pubic Key" is available. Therefore, you do not need to configure this item.  |
| Account Administrator Name | The UserId for debugging purpose. If you are an engineer, you can simply enter a frequently-used account ID. It is required only when the advanced features of IM service are used.  |
| SMS Verification Signature | It is the prefix of the SMS text. You can simply enter the App name.  |
| Integration Mode | Details are provided below |

After you complete configuration, you only need to click **Save** button.

## 3 Integration mode

### 3.1 Two integration modes
Integration mode refers to the **mode used for account integration**. Different solutions are available to meet different requirements of customers for security:

| Integration Mode | Scenarios | Interfacing Complexity | Design Goal |
|------------|-------------|-------------| -----------|
| Guest (Hosted) Mode | Suitable for scenarios with a low requirement for **identity verification**, such as LVB chat room scenario that allows all App users to join the chatting.  | You just need to log in to the IM SDK in the guestLogin mode with a low interfacing cost.  | The design goal is to reduce interfacing cost, so that you can use the IM services without interfacing with the account system. Tencent Cloud will generate a <font color='blue'>"Guest Account"</font> for each App user. The account is only used to send and receive messages, because it is not associated with your existing account system. |
| Independent (authentication) mode | Suitable for customers with a high requirement for **identity verification**. For example, the identities of all recipients and senders of messages must be bound with IDs in the existing account system in a one-to-one correspondence manner.  | The UserSig security signature is required and interfacing cost is relatively high. | The design goal is to assign the permission for sending and receiving messages to customers. In this mode, your login server is required to allocate a signature after verifying the validity of an App user's identity. Only after the Tencent Cloud authenticates the signature can the user receive and send messages. This can ensure that all recipients and senders of messages are accounts in your account system. |

> Help you understand**
>
> - In **guest mode**: Tencent Cloud IM service is just like a phone booth, which is marketable before mobile phone gets popular in the market. However, we don't pay much attention to the public phone number, and we usually identify each other by saying "hello, this is rex!"
>
> - In **independent mode**: Tencent Cloud IM service is just like a personal mobile phone service. The advantage of having a fixed mobile phone number is that you can identify the caller by reading its caller ID. However, you need to proceed with identity verification when purchasing a mobile phone and bind your ID to the phone.

### 3.2 Guest (hosted) mode
The design goal of guest mode is to reduce interfacing cost, so that you can use the IM services without interfacing with the account system. Tencent Cloud will generate a <font color='blue'>"Guest Account"</font> for each App user. The account is only used to send and receive messages. You can consider these guests accounts as "puppet accounts". The sender's real user information (nickname, profile photo, etc.) is not bound to the guest account, but is sent along with the message body.

The interfacing process for this mode is very simple: You can just click the mouse and write a few lines of interfacing codes.

(1) First, select **hosted mode** for the integration mode in [App Configuration](#2.-.E5.BA.94.E7.94.A8.E9.85.8D.E7.BD.AE), so that Tencent Cloud can provide backend support for guest accounts in the guest mode.
(2) In the client codes, interface with the guest login mode of IM SDK, which involves function calls in TLS (Tencent Login Service, a core component of Tencent IM SDK) and IM SDK.

You can directly use Mini LVB source codes to simplify the process. You only need to call a function (for iOS: the guestLogin function in TCIMPlatform.h; for Android: the guestLogin function in TCLoginMgr.java). Relevant logics have been encapsulated in the function. The source codes are explained below:

- **iOS platform**
   + Query SDKAPPID. For more information on how to obtain the ID, please see Section **1. Activate service** of the reference document.
   + Call the TLSGuestLogin function in the TLSHelper header file, which will request a guest account from Tencent Cloud backend. If the SDKAPPID in the first step is correct and your mobile phone can access the Internet, you will get a TLSUserInfo object. TLSUserInfo.identifier is the ID of this guest account.
   + Call the getTLSUserSig function in TLSHelper to generate a valid UserSig signature for this identifier.
   + Finally, you can construct a TIMLoginParam object with the aforementioned identifier and UserSig. Then call the login function in TIMManager to complete the IM SDK login process.
 
```objective-c
// Sample code 1: Call the guest login mode of TLS (Tencent Login Server)
- (void)guestLogin:(UIButton *)button {
    TLSUserInfo *info = [[TLSHelper getInstance] getGuestIdentifier];
    int ret = [[TLSHelper getInstance] TLSGuestLogin:self];
    if (ret == 0) {
           // During login, a turning chrysanthemum appears
    } else {
           // TLSHelper error occurs. Please check if IMSDK_APPID is correct
    }
}

// Sample code 2: Call the IM SDK login after successful TLS login
- (void)OnGuestLoginSuccess:(TLSUserInfo *)userInfo {
    TIMLoginParam *loginParam = [[TIMLoginParam alloc] init];
    loginParam.appidAt3rd = @"88888888"; // Enter your SDKAPPID
    loginParam.sdkAppId = 88888888       // Enter your SDKAPPID
    loginParam.accountType = @"0";
    loginParam.identifier = userInfo.identifier;
    loginParam.userSig = [[TLSHelper getInstance] getTLSUserSig:userInfo.identifier];

    [[TIMManager sharedInstance] login:loginParam succ:^{
		     // OK. Login is successful and you can send messages now!
    } fail:^(int code, NSString *msg) {
        // IM SDK login failed. Please check if the IMSDK_APPID is correct
    }];
}
```

- **Android Platform**
   + Query SDKAPPID. For more information on how to obtain the ID, please see Section **1. Activate service** of the reference document.
   + Call the TLSGuestLogin function of TLS (Tencent Login Service) to complete guest login. The function will request a guest account from Tencent Cloud backend. If the SDKAPPID in the first step is correct and your mobile phone can access the Internet, you will get a TLSUserInfo object. TLSUserInfo.identifier is the ID of this guest account.
   + Call the getUserSig function of TLS to generate a valid UserSig signature for this identifier.
   + Finally, you can call the login function in TIMManager with the aforementioned identifier and UserSig to complete the IM SDK login process.

```java
// Sample codes: Implement IM SDK guest login on the Android platform
public void guestLogin() {
   //Call the guest login mode of TLS (Tencent Login Server)
   mTLSLoginHelper.TLSGuestLogin(new TLSGuestLoginListener() {
       @Override
       public void OnGuestLoginSuccess(TLSUserInfo tlsUserInfo) {
           //Set SDKAPPID
           TIMUser user = new TIMUser();
           user.setAccountType(String.valueOf(TCConstants.IMSDK_ACCOUNT_TYPE));
           user.setAppIdAt3rd(String.valueOf(TCConstants.IMSDK_APPID));
           user.setIdentifier(tlsUserInfo.identifier);
           String userSig = mTLSLoginHelper.getUserSig(identifier);

            //Initiate the IM SDK login operation. You can send messages after successful login
            TIMManager.getInstance().login(TCConstants.IMSDK_APPID, user, userSig, new TIMCallBack() {
                @Override
                public void onSuccess() {
                    // OK. Login is successful and you can send messages now!
                }
							  @Override
                public void onError(int i, String s) {
                   // IM SDK login failed. Please check if the IMSDK_APPID is correct
                }
            });
        }
    });
}
```

### 3.3 Independent (authentication) mode

### 3.3.1 How does it work
The independent mode is designed to assign the permission for sending and receiving messages to customers: In independent mode, when an App user successfully logs in, your login server needs to assign a UserSig signature (the signature is calculated using a non-symmetric key agreed on with Tencent Cloud backend) required for imLogin (the first operation step for IM SDK). The user is allowed to send and receive messages after Tencent Cloud confirms the validity of UserSig signature.

This ensures that **only users who have passed the verification of your server are able to pass the verification of IM server.** 

More importantly, since users cannot use the IM feature without your confirmation, you don't need to put the user name and nickname in the IM message body. You can directly identify the sender using ID in the IM message header, because IM SDK cannot be forged if the message header is not cracked. In this way **you can identify the sender's identity in a more secure way**.

#### 3.3.2 UserSig signature
UserSig signature is used for mutual authentication between Tencent Cloud IM service backend and your server, to solve the problem that how the servers from two different companies can trust each other. Let's take a vivid example as explanation:

> 1. A beautiful lady logs in to your App using the ID and password she registered before. Her ID is "Flower Fairy".
>
> 2. You proceed with the verification immediately after getting her ID and password, and confirm that she can log in to the App. You also issue a **pass (UserSig)** to her, which says "<font color='blue'>'Flower Fairy' is a law-abiding citizen. Make sure she receives proper treatment in Tencent's territory...</font>". In order to ensure that the pass won't be fabricated, you affixed your signature on it.
>
> 3. Tencent Cloud reads your pass, confirms that the signature is real and provides appropriate services.

This is how interfacing process goes behind message authentication. The core is to prevent users not accepted by your backend server from sending and receiving messages. However, it would be inappropriate to let your server check each one of the messages, so this solution is developed.

UserSig signature uses the most commonly used non-symmetric key encryption technique. When enabling independent mode, you will receive a public and private key pair from Tencent Cloud. You can simply [Encrypt](https://www.qcloud.com/doc/product/269/1510) specified messages with the private key.

#### 3.3.3 Interfacing Process
- **Step 1: Select independent mode**
> Ensure the integration mode in Tencent Cloud [IM Console](https://console.qcloud.com/avc) is **Independent Mode**, and download the public and private keys required to calculate signatures.
> ![](//mc.qcloudimg.com/static/img/4e79ff175d8053f8998e02732468e398/image.png)

- **Step 2: Complete interfacing with the backend**
> This step is performed by the backend engineer in your team. The engineer needs to use the signature key obtained in Step 1 to provide your App with an API used to pull the UserSig signature. After a successful login, the App can obtain the calculated UserSig via this API.

- **Step 3: imLogin(ID, UserSig) **
> After obtaining the UserSig issued by your server, the App can call the IM SDK's imLogin (ID, UserSig) API to activate IM services. Tencent Cloud backend will use the public key in Step 1 to decrypt UserSig and verify whether the current user is accepted by your login server.

- **Step 4: Modify messaging logic**
> When modifying the code of the sending end, you don't need to put the sender ID in the message body. Meanwhile, modify the code of the receiving end. Obtain sender ID with more certainty by using the "sender" attribute of TIMMessage.

The above steps are shown in the following figure:
![](//mc.qcloudimg.com/static/img/1e541b2931d0cb8fb1815f26aa8fb493/image.png)


## 4 Message sending and receiving
Tencent Cloud IM service supports a variety of message formats, such as text, picture, emoji, voice or even small files. You can go to the [IM document zone](https://www.qcloud.com/doc/product/269 ) to learn more about this.

Comparatively, LVB messaging is rather simple, mainly including the following types:
- Ordinary text messages: including the sender's nickname and the message itself.
- On-screen comments: It is a type of text message in nature, but presented in a more fancy manner.
- Likes: When a viewer sends a like to a VJ, it's necessary to ensure that other viewers can see it as well.
- System notifications, for example "XXX has joined the room" or "The VJ has left".

For simple scenarios like this, we use a very simple method in Mini LVB: **Text message channel is used uniformly to send and receive messages. For the demand for assembling multiple fields (for example message type, user profile photo, nickname), we use the json format for data assembly.**

For example: "Flower Fairy" sends to the VJ a message of "Hey hottie, show me a smile". Based on the above method, the text message to be sent will be like this:
```json
{
    "userAction": 1,
	"userId": 27149, 
	"nickName": "Flower Fairy", 
	"headPic": "http: //www.test.com/headpic/27149.png",
	"msg": "Hey hottie, show me a smile"
}
```
**userAction** is the message type we define in Mini LVB. There are five options available:

| userAction | Number | Description |
|---------|---------|---------|
| AVIMCMD_Custom_Text | 1 | Text message |
| AVIMCMD_Custom_EnterLive | 2 | A user joins LVB |
| AVIMCMD_Custom_ExitLive | 3 | A user exits LVB |
| AVIMCMD_Custom_Like | 4 | Like |
| AVIMCMD_Custom_Danmaku | 5 | On-screen comment |

The following is an excerpt of source codes from Mini LVB, which can be used to send an ordinary text message and is provided here for your reference only:

#### 4.1 iOS platform
```
//The source codes are in the TCMsgHandler.m file
- (void)sendMessage:(AVIMCommand)cmd userId:(NSString *)userId
             nickName:(NSString *)nickName 
						 headPic:(NSString *)headPic 
						 msg:(NSString *)msgContent
{
    if ((AVIMCMD_Custom_Text == cmd || AVIMCMD_Custom_Danmaku == cmd) && msgContent.length == 0)
    {
        DebugLog(@"sendMessage failed, msg length is 0");
        return;
    }
    
    NSDictionary* dict = @{@"userAction" : @(cmd),
		@"userId" : TC_PROTECT_STR(userId), 
		@"nickName" : TC_PROTECT_STR(nickName), 
		@"headPic" : TC_PROTECT_STR(headPic), 
		@"msg" : TC_PROTECT_STR(msgContent)};
    
    NSData* data = [TCUtil dictionary2JsonData:dict];
    NSString *content = [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];

    TIMTextElem *textElem = [[TIMTextElem alloc] init];
    [textElem setText:content];

    TIMMessage *timMsg = [[TIMMessage alloc] init];
    [timMsg addElem:textElem];

    [_chatRoomConversation sendMessage:timMsg succ:^{
        DebugLog(@"sendMessage success, cmd:%d", cmd);
    } fail:^(int code, NSString *msg) {
        DebugLog(@"sendMessage failed, cmd:%d, code:%d, errmsg:%@", cmd, code, msg);
    }];
}
```

### 4.2 Android platform
```
//The source codes are in the TCChatRoomMgr.java file
private void sendMessage(int cmd, String param, TIMValueCallBack<TIMMessage> timValueCallBack) 
{
    JSONObject sendJson = new JSONObject();
    try {
		sendJson.put("userAction", cmd);
        sendJson.put("userId", TCUserInfoMgr.getInstance().getUserId());
        sendJson.put("nickName", TCUserInfoMgr.getInstance().getNickname());
        sendJson.put("headPic", TCUserInfoMgr.getInstance().getHeadPic());
        sendJson.put("msg", param);
    } catch (JSONException e) {
        e.printStackTrace();
    }
    
	String cmds = sendJson.toString();
    TIMMessage msg = new TIMMessage();
    TIMTextElem elem = new TIMTextElem();
    elem.setText(cmds);
		
	if (msg.addElement(elem) != 0) {
	    Log.d(TAG, "addElement failed");
        return;
	}
	sendTIMMessage(msg, timValueCallBack);
}
```



