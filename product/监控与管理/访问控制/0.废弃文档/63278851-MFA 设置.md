## MFA 简介

### 什么是 MFA

MFA（Multi-FactorAuthentication），即多因子认证，是一种简单有效的安全认证方法。它能够在用户名和密码之外，再增加一层保护。

MFA 设备，又叫动态口令卡或 Token 卡，是提供这种安全认证方法的设备。目前腾讯云提供两种 MFA 设备： 硬件 MFA 设备和虚拟 MFA 设备。腾讯云中国站支持的虚拟 MFA 设备要求绑定腾讯云助手小程序，腾讯云国际站支持的虚拟 MFA 设备需要绑定谷歌身份验证器。

### 支持 MFA 绑定的账号类型

腾讯云账号分为主账号和子账号。子账号类型分为子用户、协作者以及消息接收人。仅 **子用户** 或 **协作者** 可以进行 MFA 绑定，消息接收人不支持绑定。

> MFA 的相关设置关系到云上资产安全，子用户或者协作者只能接受主账号或具有 CAM 管理权限的用户的相关设置。 

如果您对 MFA 还有其他疑问，请参阅 [MFA 常见问题](https://cloud.tencent.com/document/product/378/12036)。  

## 子账号支持的安全设置

>登录保护：子用户在登录腾讯云时需要通过 MFA 验证 完成身份验证，这样即使子用户泄露或遗失密码，也无法登录您的账号，能够最大限度地保障您的资产安全。
>
>操作保护：在子用户进行敏感操作前，需要先通过 MFA 验证 或 手机号验证 完成身份验证，以保障您的资产安全。

### 子用户

CAM 子用户支持设置的操作属性如下：
<table>
<tr>
<th>设置内容</th>
<th>设置项</th>
</tr>
<tr>
<td rowspan="2">操作保护</td>
<td>MFA</td>
</tr>
<tr>
<td>不开启</td>
</tr>
<tr>
<td rowspan="2">登录保护</td>
<td>MFA</td>
</tr>
<tr>
<td>不开启</td>
</tr>
</table>

### 协作者

CAM 协作者支持设置的操作属性如下：
<table>
<tr>
<th>设置内容</th>
<th>设置项</th>
</tr>
<tr>
<td rowspan="2">操作保护</td>
<td>手机验证码</td>
</tr>
<tr>
<td>不开启</td>
</tr>
<tr>
<td rowspan="2">登录保护</td>
<td>MFA</td>
</tr>
<tr>
<td>不开启</td>
</tr>
</table>

## 操作指南

### 主账号绑定/解除 MFA 设备

 - 虚拟 MFA 设备绑定/解除指引，参考：[虚拟 MFA 设备](https://cloud.tencent.com/document/product/378/14498) 


 - 硬件 MFA  设备绑定/解除指引，参考 ：[硬件 MFA 设备](https://cloud.tencent.com/document/product/378/14520) 



### 为子账号开启 MFA
您在安全设置中只能看到 **主账号** 的状态展示，如果您需要变更 MFA 设置，可以请求主账号或者具有 CAM 管理权限的子用户，在 [访问管理控制台](https://console.cloud.tencent.com/cam) 的 **用户管理** 页面，设置 MFA 相关内容。

1. 在控制台的用户管理页面新建子用户时可以设置是否开启登录保护和敏感操作保护。
![](https://main.qcloudimg.com/raw/f8b91c64a5b7be4d4446543581bbcb9f.png)

2. 设置子用户开启 MFA 校验后，子用户在下一次登录时，系统将首先要求进行 MFA 设备关联，关联之后才可以进入控制台进行操作。

### 查看子账号 MFA

1. 登录腾讯云 [访问管理控制台](https://console.cloud.tencent.com/cam)，进入左侧导航【用户管理】页面，可查看用户列表。
   ![](https://main.qcloudimg.com/raw/5349ecbb00bbc527c35037a1ae7a4098.png)
2. 查看子账号是否绑定 MFA
   单击列表内的用户名称可查看用户详情（如子用户），在【安全设置】中可查看该用户是否绑定 MFA。如【安全设置】右侧如果出现警告图标，则是提醒您注意该子账号尚未绑定 MFA 或者7天内有敏感操作。
   ![](https://main.qcloudimg.com/raw/6a835cc9303d0764832a0685a5cb5c8c.png)

### <a id="resetMFA">为子账号重置 MFA</a>
1. 在 [访问管理控制台](https://console.cloud.tencent.com/cam) 用户管理页面，进入子账号（子用户或协作者）详情页面，进入安全设置，单击【MFA 设备】右侧的编辑图标，进入 MFA 管理界面。

2. 管理 MFA 设置项中，可以对子账号（子用户或协作者）的 MFA 设置内容进行管理和配置，选择是否开启登录保护和敏感操作保护。
![img](https://main.qcloudimg.com/raw/278e25f78687a8fd83aa9c738b839843.png) 

3. 子账号（子用户或协作者）的 MFA 开启后，您可以重置该用户的设备状态。重置完成后，子账号（子用户或协作者）下次登录后，将进入重新绑定 MFA 的流程。

>重置 MFA 设备再重新绑定，可以解决当子账号（子用户或协作者）在设备丢失时无法重新关联的问题。


