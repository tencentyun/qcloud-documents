设置好 MFA 后，在您登录腾讯云或者在腾讯云进行敏感操作时，需要进行二次认证。由于这些操作的设置，关系到您账号的安全性，如果您是子用户或者协作者，只能接受主账号或者是具有 CAM 管理权限的用户对这些安全属性的设置。
## 子用户支持的安全属性设置
CAM 子用户可以设置的操作属性如下：
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

## 协作者支持的安全属性设置
CAM 协作者可以设置的操作属性如下：
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

## 为子用户开启 MFA
您在安全设置中只能看到 **主账号** 的状态展示，如果您需要变更设置，可以请求主账号或者具有 CAM 管理权限的子用户，在 [访问管理控制台](https://console.cloud.tencent.com/cam) 的 **用户管理** 中，设置相关内容。

1. 在控制台的用户管理页面新建子用户时可以设置是否开启登录保护和敏感操作保护。
![](https://main.qcloudimg.com/raw/086d82025e720830d57c2824180a8e98.png)

2. 设置子用户开启 MFA 校验后，子用户在下一次登录时，系统将首先要求进行 MFA 设备关联，关联之后才可以进入控制台进行操作。



## 为子用户（协作者）重置 MFA
1. 在 [访问管理控制台](https://console.cloud.tencent.com/cam) 用户管理页面，进入子用户（协作者）详情页面，进入安全设置，找到 MFA 设置项。
![img](https://main.qcloudimg.com/raw/7e15061c3e6d8032e0e711fde84585ad.png) 
2. 管理 MFA 设置项中，可以对子用户（协作者）的 MFA 设置内容进行管理和配置，选择是否开启登录保护和敏感操作保护。
![img](https://main.qcloudimg.com/raw/005403ec1dc438cf3d7194c15afa53d8.png) 

3. 子用户（协作者）的 MFA 开启后，您可以重置该用户的设备状态。重置完成后，子用户（协作者）下次登录后，将进入重新绑定 MFA 的流程。
重置 MFA 设备再重新绑定，可以解决当子用户（协作者）在设备丢失时无法重新关联的问题。

## 常见问题
#### 子账号（协作者）忘记 MFA 设备如何处理？
请主账号（或具有管理权限的用户）在 [访问管理控制台](https://console.cloud.tencent.com/cam) 中重置 MFA，具体操作请参考 [为子用户（协作者）重置 MFA](#.E4.B8.BA.E5.AD.90.E7.94.A8.E6.88.B7.EF.BC.88.E5.8D.8F.E4.BD.9C.E8.80.85.EF.BC.89.E9.87.8D.E7.BD.AE-mfa)。
