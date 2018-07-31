## 概述
aaa
## 操作指南


###  登录访问管理控制台
登录腾讯云 [访问管理控制台](https://console.cloud.tencent.com/cam)，进入左侧导航【用户管理】页面，可查看用户列表。
![](https://main.qcloudimg.com/raw/b46bf90a7060eec4861e060f1c163404.png)
###  查看是否绑定 MFA
单击列表内的用户名称可查看用户详情（如子用户），在【安全设置】中可查看该用户是否绑定 MFA。
![](https://main.qcloudimg.com/raw/f53b93079898cef719f95df1b399aeb6.png)

### 绑定 MFA

1. 身份验证
通过与根账号绑定的手机号接收验证信息，输入验证码，单击【确定】。
![](https://main.qcloudimg.com/raw/33dfd73f48a83cf26dc9c9bb452d5e0b.png)
2. 分别选择开启登录保护和敏感操作保护的软件 MFA 校验，点击【确定】，完成绑定 MFA 操作

![](https://main.qcloudimg.com/raw/dcfc7c9884e939ade77c81cdfa6cf3ee.png)

>开启**登录保护**后，子用户在登录腾讯云时需要通过 MFA 验证 完成身份验证，这样即使子用户泄露或遗失密码，也无法登录您的账号，能够最大限度地保障您的资产安全。
开启**敏感操作保护**后，在子用户进行敏感操作前，需要先通过 MFA 验证 或 手机号验证 完成身份验证，以保障您的资产安全。
