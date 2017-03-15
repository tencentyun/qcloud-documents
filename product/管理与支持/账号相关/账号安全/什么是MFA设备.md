**MFA**(Multi-FactorAuthentication)即多因子认证，是一种安全认证方法，MFA设备（又叫动态口令卡或token卡）是提供这种安全认证方法的设备。目前腾讯云提供两种MFA设备：**硬件MFA设备**和**虚拟MFA设备**。


## 1.硬件MFA设备
![](https://mc.qcloudimg.com/static/img/e5fd0f764b6a40626557beb032a4d6b2/image.png)

硬件MFA设备如上图所示，正面的6位数动态安全码30s更新一次，目前该设备仅开放给内测用户使用。
## 2.虚拟MFA设备

虚拟MFA设备是一个产生动态安全码的应用程序，它遵循基于时间的一次性密码 (TOTP) 标准(RFC 6238),可以安装在不同的移动设备上，方便用户使用。

### 腾讯云支持的虚拟设备

| 手机类型      | 设备名称 |
| --------- | -----:|
| ios     | [google身份验证器](google身份验证器 "https://itunes.apple.com/us/app/google-authenticator/id388497605?mt=8")|
| android         |   [google身份验证器](google身份验证器 "http://sj.qq.com/myapp/detail.htm?apkName=com.google.android.apps.authenticator2") ; [Authy双重身份验证](Authy双重身份验证 "http://sj.qq.com/myapp/detail.htm?apkName=com.authy.authy") |
