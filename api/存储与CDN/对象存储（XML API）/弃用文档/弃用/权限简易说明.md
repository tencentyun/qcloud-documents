## 控制台权限简易说明
您可以登录 [COS 控制台](http://console.cloud.tencent.com/cos5) 设置权限管理。

### 权限维度
腾讯云对象存储支持两种维度的访问权限设置：访问控制策略 ACL、访问策略语言 Policy。
访问控制策略 ACL 基于用户维度，可通过存储桶的「权限管理」菜单设置。权限设置支持存储桶、文件夹、以及文件级别。
访问策略语言 Policy 基于存储桶资源维度，可通过存储桶的「权限管理」菜单设置，有关访问策略语言 Policy 的说明请参阅 [访问策略语言概述]()。
![WechatIMG13](/Users/lyz/Desktop/WechatIMG13.jpeg)

### 访问控制权限

以文件文件夹为例，设置权限：

![WechatIMG11](/Users/lyz/Desktop/WechatIMG11.jpeg)

可授权其他用户访问该文件夹：

![WechatIMG12](/Users/lyz/Desktop/WechatIMG12.jpeg)

如果需要授权其他根账户访问，请直接填写根账户 UIN，如果需要授权子账户访问，请使用「根账户/子账户」的格式来填写 UIN。

上图所示即将 testfile 文件夹授权子账户 14393036（所属根账户 3376437771）的只读许可。

