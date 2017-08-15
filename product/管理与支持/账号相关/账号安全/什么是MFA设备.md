MFA (Multi-FactorAuthentication)即多因子认证，是一种简单有效的安全认证方法，它能够实现在用户名和密码之外再增加一层保护。MFA 设备（又叫动态口令卡或token卡）是提供这种安全认证方法的设备。目前腾讯云提供两种MFA设备： **硬件 MFA 设备** 和 **虚拟 MFA 设备** 。


## 硬件MFA设备
![](https://mc.qcloudimg.com/static/img/e5fd0f764b6a40626557beb032a4d6b2/image.png)

硬件 MFA 设备如上图所示，正面的6位数动态安全码30s更新一次，背面有该硬件 MFA 设备的序列号。目前该设备仅开放给内测用户使用。
### 绑定硬件 MFA 设备
1. 登录腾讯云控制台，进入[安全设置](https://console.qcloud.com/developer/security)，在 MFA 设备那一栏上，单击【绑定】。
![](https://mc.qcloudimg.com/static/img/63c17fdf2fc1913927ad669c86dcafcd/image.png)
2. 在弹出来的页面中，单击【发送验证码】，收到验证码后，将6位数字验证码输入框内。
![](https://mc.qcloudimg.com/static/img/b96da083ba830fdaeab02785fdcd7625/image.png)
3. 在序列号那一栏填写上 MFA 设备 背面的系列号。
![](https://mc.qcloudimg.com/static/img/ca226004b24b2aeefd24a18bfa04bad0/image.png)
4. 在安全码那一栏填写上 MFA 设备正面上动态变化的6位数字。
![](https://mc.qcloudimg.com/static/img/3b0acf08008730d46e57e2150fac9059/image.png)
5. 选择您想启用的范围，您可以选择登录保护，也可以选择操作保护，只需要在你想选择的范围前面勾选出来即可，可多选。选择完之后，单击【提交】。
![](https://mc.qcloudimg.com/static/img/c9992d92e521e804a51075ca1414ef43/image.png)


### 解绑硬件 MFA 设备

1. 登录腾讯云控制台，进入[账号中心](https://console.qcloud.com/developer/security)，在 MFA 设备那一栏上，单击【解绑】。
![](https://mc.qcloudimg.com/static/img/5a6fbe99163c47d960f5481d2d29bf09/%7BD096D4A6-7497-42C8-9968-66EC048E870B%7D.png)
2. 单击【确定解绑】。
![](https://mc.qcloudimg.com/static/img/41e8f092c9710d0cbda8d96b3ac4c08b/image.png)
## 虚拟MFA设备

虚拟 MFA 设备是一个产生动态安全码的应用程序，它遵循基于时间的一次性密码 (TOTP) 标准(RFC 6238)，可以将虚拟 MFA 设备安装在不同的移动设备上，如智能手机。因此方便用户使用虚拟 MFA 设备。

### 绑定虚拟 MFA 设备
1. 登录腾讯云控制台，进入[安全设置](https://console.qcloud.com/developer/security)，在 MFA 设备那一栏上，单击【绑定】。
![](https://mc.qcloudimg.com/static/img/63c17fdf2fc1913927ad669c86dcafcd/image.png)
2. 在弹出来的页面中，单击【发送验证码】，收到验证码后，将6位数字验证码输入框内。
![](https://mc.qcloudimg.com/static/img/b96da083ba830fdaeab02785fdcd7625/image.png)
3. 在弹出来的页面中，依次按照图片中的步骤进行操作。
![](https://mc.qcloudimg.com/static/img/0e9169e02f094677636e0cd4943f8cc0/image.png)
4. 将手机中的应用程序出现的连续的安全码输入到框内，安全码每30秒更新一次。
![](https://mc.qcloudimg.com/static/img/7bc667296b7c147154ad265f15e9677c/image.png)
5. 选择您想启用的范围，您可以选择登录保护，也可以选择操作保护，只需要在你想选择的范围前面勾选出来即可，可多选。选择完之后，单击【提交】。
![](https://mc.qcloudimg.com/static/img/c9992d92e521e804a51075ca1414ef43/image.png)



### 解绑虚拟 MFA 设备



1. 登录腾讯云控制台，进入[账号中心](https://console.qcloud.com/developer/security)，在 MFA 设备那一栏上，单击【解绑】。
![](https://mc.qcloudimg.com/static/img/31eac4c6f2e90dac10d941ba9fd3181f/image.png)
2. 单击【确定解绑】。
![](https://mc.qcloudimg.com/static/img/41e8f092c9710d0cbda8d96b3ac4c08b/image.png)

### 腾讯云支持的虚拟设备


| 手机类型      | 应用程序 |
| --------- | -----:|
| ios  / Android    | 微信小程序-腾讯云助手小程序|


