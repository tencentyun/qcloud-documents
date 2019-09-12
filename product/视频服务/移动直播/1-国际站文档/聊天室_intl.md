There is a close relationship between online LVB and IM chat rooms. Without the interactive messages in the chat rooms, the LVB will become boring and dull. This document describes how to use [**Tencent Cloud Instant Messaging (IM)**](https://cloud.tencent.com/product/im.html) service to build simple chat room features:
(1) Broadcast on-screen comments and likes.
(2) Broadcast system notifications, for example "XXX has joined the room" or "The VJ has left".

![](https://mc.qcloudimg.com/static/img/6c6edc29c61bb4478d774094227125e1/image.png)

<h2 id="IM">1. Tencent Cloud IM Service</h2>

The predecessor of Tencent Cloud IM is QQ's instant messaging system. We remove the QQ message module and change it to IM SDK which is more suitable for mobile access. The message backend has been transformed so that it was unbound with the QQ number, constituting the current IM backend.

IM SDK can be considered as the QQ without user interaction page. Integrating the IM SDK into your App is like integrating a QQ message kernel.

As we all know, QQ can receive and send messages of private chats and group chats, but you need to log in to it before you can use it. Logging in to QQ requires a QQ account and password. Similarly, logging in to IM SDK needs a user-specified username (userid) and password (usersig).

- **User name (userid)**
This can be the user ID in your current application. For example, if the account ID of a user is 27149, then he/she can use 27149 as the userid to log in to the IM SDK.

- **Password (usersig)**
Since you specified that 27149 is your user, how can Tencent Cloud confirm that the user is a valid user you have approved? Usersig is used to solve this problem. Usersig is the asymmetric encryption result of userid, appid, and other information.

 The encryption key and the decryption key used in asymmetric encryption are different. The private key can be kept on your server to asymmetrically encrypt the userid and appid to generate the usersig. At the same time, Tencent Cloud keeps the corresponding public key to verify whether the usersig is valid and is signed by your server.

![](https://mc.qcloudimg.com/static/img/1e218acdf45772973f9f6c363ab55d89/image.jpg)


<h2 id="OPEN">2. Service Activation and Configuration</h2>

Log in to the [IM Console](https://console.cloud.tencent.com/avc). If you have not activated the service, click the **Activate IM** button. For a new Tencent Cloud account, the IM App list is empty, as shown below:
![](//mc.qcloudimg.com/static/img/c033ddba671a514c7b160e1c99a08b55/image.png)

Click the **Create Application Access** button to create a new application access, that is, the name of the application for which you want to get the access to Tencent Cloud IM service. Our test application is called "Small LVB Demo", as shown below:
![](//mc.qcloudimg.com/static/img/897bff65af6202322a434b6fa3f8a0bd/image.png)

Click the **OK** button, and then you can see in the application list the item you just added, as shown below:
![](https://mc.qcloudimg.com/static/img/fff565dc81ba26ca7af4951264b7bb4c/image.png)

Click the **Application Configuration** link, you will enter the application configuration interface, and then click the **Edit** button on the right side of the **Account System Integration**, and you can configure as shown below (The account name and administrator name are recommended in English. You can enter any account name you like. The administrator account will be used when calling IM's REST API).
![](https://mc.qcloudimg.com/static/img/1104e8354d234d949840c9b6c396fd24/image.png)

Click the **Save** button, the page will automatically refresh, and then you can see the **Download Public and Private Keys** button.
![](https://mc.qcloudimg.com/static/img/67810cab51216a813b47edcb960ab67a/image.png)

Click the **Download Public and Private Keys** button to get a zip file called **keys.zip** which has a private_key and a public_key. The **private_key** is the private key used to sign UserSig.
![](https://mc.qcloudimg.com/static/img/615590334ba32627857fdb309176682f/image.png)

You can test whether private_key can perform the signature normally in the **Development Tools**.
![](https://mc.qcloudimg.com/static/img/b7d40f17068d9f6605bcac81e2891b5e/image.png)

<h2 id="SERVER">3. Server Access Guidelines</h2>

### 3.1 Distribute the UserSig
UserSig is distributed to the Client in a simple way through the backend server. By clicking a few mouse clicks in the previous step, we have obtained the public and private keys used to sign UserSig.

 Next, you can read the [DOC](https://cloud.tencent.com/document/product/269/1510) to understand the UserSig generation code for language versions (Java, PHP, C++) and then integrate them into your backend system.

 The recommended practice is to integrate them into the login process, that is, when the user logs in, your backend server returns UserSig to your application in addition to the original information.

### 3.2 Call the REST API
You can also perform secondary development by calling [REST API](https://cloud.tencent.com/document/product/269/1520), such as:

| API | Description | Purpose |
| ---------------------------------------- | ---- | ---------------------------------------- |
| [v4/group_open_http_svc/create_group](https://cloud.tencent.com/document/product/269/1615) | Create groups | The chat room corresponding to an LVB can be created by the VJ on the client side using the IM SDK, or can be created by your server using this API |
| [v4/group_open_http_svc/send_group_msg](https://cloud.tencent.com/document/product/269/1629) | Send messages | Messages can be pushed to each member of the group using this API | 
| [v4/openim_dirty_words/add](https://cloud.tencent.com/document/product/269/2397) | Add dirty words | Used for sensitive words filtering. |


<h2 id="CLIENT">4. Client Access Guidelines</h2>

### 4.1. Download SDK
You can download the latest version of [IM SDK](https://cloud.tencent.com/product/im#sdk) from the IM official website. We advise you to download the v3 version, which is less difficult to access than v2.


### 4.2 IM login (imLogin)
The userSig signed by your server can be returned to the application when the application connects to the server. After the application gets the userid and usersig, you can log in to Tencent Cloud IM service to send and receive messages (Similarly, you can log in to the QQ backend to send and receive messages after entering the correct QQ number and password). The example code is as follows:

```objective-c
// iOS example code: imLogin
//
#import "ImSDK/ImSDK.h"
TIMLoginParam *param = [[TIMLoginParam alloc] init];
// identifier is the user name, userSig is the user login credential, and the calculation results of the server are as follows
param.identifier = _config.userID;
param.userSig = _config.userSig;
param.appidAt3rd = [NSString stringWithFormat:@"%d", _config.appID];

[[TIMManager sharedInstance] login:param succ:^{
//Logged in successfully
} fail:^(int code, NSString *msg) {
//Failed to log in
}];
```

```java
// android example code: imLogin
//
TIMUserConfig timUserConfig = new TIMUserConfig();
TIMManager.getInstance().login(identifier, userSig, timUserConfig, new TIMCallBack() {
	@Override
	public void onError(int code, String desc) {
		//"code" (error code) and "desc" (error description) can be used to locate the reason for the failure
		//For the list of "code" (error code), please see the error codes
		Log.d(tag, "login failed. code: " + code + " errmsg: " + desc);
	}

	@Override
	public void onSuccess() {
		Log.d(tag, "login succ");
	}
});
```

### 4.3 Join a chat room
The IM SDK can only send and receive broadcast messages after joining a specific chat room. The sample code for joining the chat room is as follows:

```objective-c
// iOS example code: Join a chat room
//
[[TIMGroupManager sharedInstance] joinGroup:@"TGID1JYSZEAEQ" msg:@"Apply Join Group" succ:^(){
    NSLog(@"Join Succ");
}fail:^(int code, NSString * err) {
    NSLog(@"code=%d, err=%@", code, err);
}];
```

```java
// Android example code: Join a chat room
//
TIMGroupManager.getInstance().applyJoinGroup(groupID, "" , new TIMCallBack() {
	@Override
	public void onError(int i, String s) {
		Log.d(TAG,"Failed to join the group");
	}

	@Override
	public void onSuccess() {
		Log.d(TAG,"Joined the group"+groupID+" successfully");
	}
});
```

### 4.4 Send group chats

```objective-c
// iOS example code: Send group chats
//
TIMTextElem * text_elem = [[TIMTextElem alloc] init];
[text_elem setText:@"this is a text message"];
TIMMessage * msg = [[TIMMessage alloc] init];
[msg addElem:text_elem];
[conversation sendMessage:msg succ:^(){
    NSLog(@"SendMsg Succ");
}fail:^(int code, NSString * err) {
    NSLog(@"SendMsg Failed:%d->%@", code, err);
}];
```
```java
// Android example code: Send group chats
//
TIMTextElem textElem = new TIMTextElem();
textElem.setText(msgText);
TIMMessage message = new TIMMessage();
message.addElement(textElem);
TIMConversation conversation = TIMManager.getInstance().getConversation(TIMConversationType.Group, groupId);
conversation.sendMessage(message, new TIMValueCallBack<TIMMessage>(){
	@Override
	public void onError(int i, String s) {
		Log.d(TAG, "Failed to send broadcast messages");
	}
	@Override
	public void onSuccess(TIMMessage timMessage) {
		Log.d(TAG, "Broadcast messages sent successfully");
	}
});
```

### 4.5 More APIs
Only the most commonly used APIs are introduced here. For more APIs of IM SDK, please see the [Documentation](https://cloud.tencent.com/document/product/269) of Tencent Cloud IM service.
