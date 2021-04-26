## Why should I assign a UserSig?

UserSig is a security credential for using Tencent Cloud Instant Messaging ([IM](https://cloud.tencent.com/product/im)). If you want use the chat room feature of Tencent Cloud IM service, you need to ask your backend engineer to generate a UserSig and return it to the terminal APP. If you already have an IM solution (that is, you already have your own chat room), skip this step.

## What is UserSig?
The predecessor of Tencent Cloud IM is QQ's instant messaging system. We remove the QQ message module and change it into IM SDK which is more suitable for mobile access. The message backend has been transformed so that it was unbound with the QQ number, constituting the current IM backend.

IM SDK can be considered as the QQ without user interaction page. Integrating the IM SDK into your App is like integrating a QQ message kernel.

As we all know, QQ can receive and send messages of private chats and group chats, but you need to log in to it before you can use it. Logging in to QQ requires a QQ account and password. Similarly, logging in to IM SDK needs a user-specified username (userid) and password (usersig).

- **User name (userid)**
This can be the user ID in your current application. For example, if the account ID of a user is 27149, then he/she can use 27149 as the userid to log in to the IM SDK.

- **Password (usersig)**
Since you specified that 27149 is your user, how can Tencent Cloud confirm that the user is a valid user you have approved? Usersig is used to solve this problem. Usersig is the asymmetric encryption result of userid, appid, and other information.

 The encryption key and the decryption key used in asymmetric encryption are different. The private key can be kept on your server to asymmetrically encrypt the userid and appid to generate the usersig. At the same time, Tencent Cloud keeps the corresponding public key to verify whether the usersig is valid and is signed by your server.

![](https://mc.qcloudimg.com/static/img/1e218acdf45772973f9f6c363ab55d89/image.jpg)

## How is UserSig generated?

### Step1: Get a private key for issuing UserSig

Log in to the [IM Console](https://console.cloud.tencent.com/avc). If you have not activated the service, click the **Activate IM** button. The application list is empty under a new account. Click the **New Application** button to create an application:
![](//mc.qcloudimg.com/static/img/897bff65af6202322a434b6fa3f8a0bd/image.png)

Click the **OK** button, and then you can see in the application list the item you just added, as shown below:
![](https://mc.qcloudimg.com/static/img/fff565dc81ba26ca7af4951264b7bb4c/image.png)

Click the **Application Configuration** link, you will enter the application configuration interface, and then click the **Edit** button on the right side of the **Account System Integration**, and you can configure as shown below (The account name and administrator name are recommended in English. You can enter any account name you like. The administrator name will be used when calling IM's REST API).
![](https://mc.qcloudimg.com/static/img/1104e8354d234d949840c9b6c396fd24/image.png)

Click the **Save** button, the page will automatically refresh, and then you can see the **Download Public and Private Keys** button.
![](https://mc.qcloudimg.com/static/img/67810cab51216a813b47edcb960ab67a/image.png)

Click the **Download Public and Private Keys** button to get a zip file called **keys.zip** which has a private_key and a public_key. The **private_key** is the private key used to sign UserSig.
![](https://mc.qcloudimg.com/static/img/615590334ba32627857fdb309176682f/image.png)

### Step 2: Test private_key
You can test whether private_key can perform the signature normally in the **Development Tools**.
![](https://mc.qcloudimg.com/static/img/b7d40f17068d9f6605bcac81e2891b5e/image.png)

### Step 3: Integrate and generate code
We provide the source code of java and php versions for calculating UserSig in the SDK download area of​the official website. If you need other versions, please see [DOC](https://cloud.tencent.com/document/product/269/1510).

-[**Download source code of java and php versions**](https://cloud.tencent.com/document/product/454/7873#Server)


## How can I use UserSig?
If you are a backend R&D engineer, you only need to notify the terminal development engineer of reading the IM SDK integration document ([iOS](https://cloud.tencent.com/document/product/269/9149) | [Android](https://cloud.tencent.com/document/product/269/9233)) to complete subsequent integration tasks.


