本文将介绍数字身份管控平台（员工版） (以下简称 EIAM) 为 OIDC 应用系统提供的 API 。通过调用相关 API ，应用可以完成与用户身份相关的各类操作，例如：用户认证、用户信息的获取等。
>!在应用接入前，您需要首先在 [应用管理页面](https://console.cloud.tencent.com/eiam/app-manager) 完成 OIDC 协议类型应用的新建与配置，获取应用的 Client ID 、 Client Secret 等配置信息。
>
## 前提条件
已完成 [创建 OIDC 应用](https://cloud.tencent.com/document/product/1442/62512)。

## 单点登录
对于应用实现用户认证的功能，EIAM 产品提供通过认证门户登录并直接单点登录至应用的能力。基于 OIDC 应用协议，提供授权码模式、PKCE 模式等多种认证授权方式。下面以授权码模式为例展示 OIDC 应用实现用户认证的流程。
1. 登录 [数字身份管控平台（员工版）控制台](https://console.cloud.tencent.com/eiam/app-manager)，在左侧导航栏，单击**应用管理**。
2. 在应用管理页面，选择已创建的 OIDC 应用，单击**应用配置**。
![](https://main.qcloudimg.com/raw/2e87d32dce333b7b5f85dff4a4788cee.png)
3. 在应用信息页面，获取 Authorize URL，此 URL 为用户在应用系统登录时，应用将用户重定向的认证地址，详情请参见 [授权码模式](https://cloud.tencent.com/document/product/1442/62552)。
![](https://main.qcloudimg.com/raw/7c079dfb2523a11f351c7d9dbed45862.png)
4. 首次访问会跳转到登录页面进行用户身份认证，输入账号密码后单击**登录**，认证通过后重定向到指定地址(redirect_uri)，并在URL 中携带 code 参数。
![](https://main.qcloudimg.com/raw/3bb227d96f6a0d2e38e822d155aa182d.png)
5. 使用应用回调地址，接收到回调请求后，可以通过调用 [获取 Token ](https://cloud.tencent.com/document/product/1442/62552)接口，来获取 id_token、access_token 和 refresh_token。
7. 应用建立用户的登录态，将 id_token、access_token 和 refresh_token 与登录态关联起来，完成登录。
>?应用系统可自行选择合适的方法建立并保持登录态，例如：Web 应用可以使用 session cookie ，单页应用可以使用 localStorage 或 sessionStorage 。

## 短信验证码二次认证
针对在 EIAM 控制台开启了二次认证功能的情况下，发起的密码登录场景。
>?二次认证功能在 [安全设置页面](https://console.cloud.tencent.com/eiam/security-setting) 中开启。
>
1. 登录 [数字身份管控平台（员工版）控制台](https://console.cloud.tencent.com/eiam/app-manager)，在左侧导航栏，单击**应用管理**。
2. 调用 [密码模式](https://cloud.tencent.com/document/product/1442/62423)，触发二次认证将会返回 `mfa_required`的错误码并返回 `mfa_token`。
3. 调用 [ MFA 认证因子质询](https://cloud.tencent.com/document/product/1442/62436) 接口，输入 `mfa_token`，该接口会发送短信验证码，并返回 oob 码。
4. 调用 oob 模式的[ 短信验证码模式](https://cloud.tencent.com/document/product/1442/62428)，传入 oob 码和短信验证码，验证通过后返回 id_token、access_token 和 refresh_token。
5. 应用建立用户的登录态，将 id_token、access_token 和 refresh_token 与登录态关联起来，完成登录。
>?应用系统可自行选择合适的方法建立并保持登录态，例如：Web 应用可以使用 session cookie ，单页应用可以使用 localStorage 或 sessionStorage 。

## 其他 API
用户应用系统可调用 [获取 OpenID Provider 配置信息接口](https://cloud.tencent.com/document/product/1442/62560)，获取 OIDC 授权服务器的配置信息。
