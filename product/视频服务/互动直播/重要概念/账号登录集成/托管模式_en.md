Hosted mode means that TLS provides developers with services of registration, storage and verification of the password for App account. Upon successful verification of the account, the signature encrypted using private key is sent to the client. App business server can decrypt the signature with [downloaded public key](/doc/product/269/下载公钥) for verification.
Note: Currently, hosted mode is only supported for Android and iOS platforms. You can use standalone mode for PC and Web platforms.

## 1. App Self-owned Account
![](//avc.qcloud.com/wiki2.0/im/imgs/20151116095740_64728.png)

**Registration**

(1) Two APIs are provided for the registration of App self-owned account:
(2) (Optional) [API](/doc/product/269/托管模式存量账号导入) is provided for the import of existing accounts.
(3) New account is registered using TLS SDK.

**Login**

(1) Enter account and password on the client and verify in TLS.
(2) After login, you can directly use audio/video or IM cloud service.
(3) (Optional) App server can verify the signature using [TLS Backend API](/doc/product/269/TLS后台API使用手册) to confirm the validity of user.

**Notes**

(1) Quickly complete the integration of registration and login capacities using TLS SDK directly.
(2) Apps that have been launched can also use hosted mode through import of existing accounts.

**Security**

The security level of storage of account and password is the same with that of QQ account, to ensure the account security when database dragging occurs.

**Process**

![](//avc.qcloud.com/wiki2.0/im/imgs/20151116095831_86603.png)

## 2. Download Development Documents

[TLS SDK Development Manual (Android)](http://share.weiyun.com/5354e32c0206943193eb3516173efc5d)
[TLS SDK Development Manual (IOS)](http://share.weiyun.com/c422eeec71523c2d706754ed923b6602)

## 3. Contact Us

In case of any problem, it is recommended to click [here](http://bbs.qcloud.com/thread-8287-1-1.html) first for solutions. If you need further support, please contact TLS Account Support via QQ (3268519604) or email (tls_assistant@tencent.com).

