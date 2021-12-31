## 操作场景
本文为您介绍如何创建 OIDC 应用，并对其进行授权。

## 操作步骤
1. 登录 [数字身份管控平台（员工版）控制台](https://console.cloud.tencent.com/eiam)，在左侧导航栏，单击**应用管理**。
2. 在应用管理页面，单击**应用协议新建**，选择应用协议模板 **OIDC**，单击**下一步：配置参数信息**。
![](https://main.qcloudimg.com/raw/d4ebaf4b8371be193b9803f394b7aecd.png)
3. 在应用协议新建页面，登记接入应用的相关信息，如下图所示：
>?
>- Redirect_URI：为应用系统的重定向地址，用于接收 EIAM 以重定向的方式返回的授权码或 access_token 等参数。
>- SP Home Page URL	：为应用系统的登录首页地址。
>- GrantType	：为应用系统获取用户授权的方式，OIDC 应用仅支持 authorization_code 模式，授权成功后返回 code；该配置只针对从EIAM 门户发起登录的场景。
>- Access_token有效期：为 access_token 的有效时长（单位：秒），默认为7200（2小时）。
>- Refresh_token：是否开启 refresh_token，该配置只对授权码模式和密码模式有效；如使用其他模式，即使将该配置设置为“开启”，也默认不返回 refresh_token。
>- ID_Token有效期：为 refresh_token 的有效时长（单位: 秒），默认为604800（7天）。
>- Claims：为用户自定义 id_token 中的属性，目前可定义属性包括用户名称、用户昵称、手机号码、邮箱地址。
>
![](https://main.qcloudimg.com/raw/8138078ab82547bf2b925eeaad015260.png)
4. 配置完成后，单击**下一步：完成**，即可创建应用。
>?创建完成后，需要对应用进行授权操作，具体操作请参见 [授权管理](https://cloud.tencent.com/document/product/1442/55069)。

