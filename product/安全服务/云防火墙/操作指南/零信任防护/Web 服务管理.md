## 功能简介
Web 服务管理基于接入域名实现对 Web 服务的访问，提供了基础防护和高级防护两种防护模式。高级防护支持微信扫码认证，对于 HTTPS 加密协议的 Web 服务增加了微信身份的访问控制。同时，在互联网边界可以封禁掉公网 IP 的访问渠道，避免了 Web 服务的真实 IP 和端口暴露在公网，更好保护了 Web 服务资产。

## 功能特点 
- 提供了简单人机防护，隐匿源站。
- 过滤 Web 攻击、漏洞利用攻击。
- 支持微信认证，实名访问。
- 微信内免扫码，一键认证。
- 全流程、全用户审计。

## 配置步骤
本文介绍 Web  服务接入的配置步骤，以及介绍用户管理和访问日志的操作方法。Web 服务接入大致分为以下几个步骤：
<dx-steps>
-创建 NAT 防火墙
-Web 服务实例添加
-接入防护
-编辑接入
-用户管理
-查看访问日志
</dx-steps>


## 创建 NAT 边界防火墙[](id:NAT)
Web 服务接入云防火墙的载体是 NAT 边界防火墙，基于反代的原理提供来自公网的访问，因此要实现接入，则首先需要在相关地域创建 NAT 防火墙，详细配置参考 [NAT 边界防火墙开关](https://cloud.tencent.com/document/product/1132/46929)。


## Web 服务实例添加
通过资产中心的同步资产手动进行同步或者手动添加的方式，及时将 Web 服务资产同步到资产中心，以便执行接入防护的操作。
1. 登录 [云防火墙控制台](https://console.cloud.tencent.com/cfw/identityauth)，在左侧导航栏中，选择**零信任防护** > **Web 服务管理**。
2. 在 Web 服务管理页面，单击**手动添加**，添加未被资产中心识别到的 Web 资产。
![](https://qcloudimg.tencent-cloud.cn/raw/8f508e4d703db55b9b1e73e8f40ba0fb.png)
3. 在手动添加弹窗中，配置相关参数，单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/5effffa0d83fef65c79f46a32188ff31.png)
参数说明：
 - 关联实例：选择服务部署所在的实例。
 - 服务地址：选择服务绑定的 IP 地址。
 - 服务域名：非必填，服务绑定的域名，请确认服务域名是否解析到所选实例上。注：**若该服务通过域名访问，请务必填写服务域名**。
4. 在 Web 服务管理页面，单击**同步资产**，后台自动同步并更新 Web 资产。

## 接入防护
将 Web 服务接入 NAT 边界防火墙来进行防护，通过接入域名和自定义端口取代公网 IP 或域名、真实端口访问形式，同时在互联网边界阻断公网 IP 的访问，避免业务暴露互联网，从而被 Web 攻击。
1. 在 [Web 服务管理页面](https://console.cloud.tencent.com/cfw/identityauth/webserv)，选择需要接入防护的 Web 服务资产，单击**接入防护**。
![](https://qcloudimg.tencent-cloud.cn/raw/1829ec24b4e3bd72327c5c8bf7e0cebd.png)
2. 资产如果未接入 NAT 边界防火墙，会提示 [创建 NAT 防火墙](#NAT)；已创建好 NAT 边界防火墙的地域，进入接入防护弹窗中。
![](https://qcloudimg.tencent-cloud.cn/raw/a91a8df09e995c4fb7607806aa538878.png)
3. 在接入防护弹窗中，配置相关参数，单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/77ce584f8786673766717cd09294bba7.png)
参数说明：
 - 接入方法：
    - 使用自有域名接入：自行接入需要将您的域名手动解析至 NAT 防火墙实例上，且相同域名仅能接入一个 Web 服务。
    - 使用云防火墙域名：用云防火墙的接入域名去访问。
 - 域名类型：选择一个现有的接入域名或者是新建一个接入域名。
 - 启用 https：启用 https 后，将默认使用云防火墙的 SSL 证书，如需使用高级防护，请选择启用 https 协议。
 - 解析地域：将域名解析到所选地域的 NAT 实例上。
 - 解析实例：将域名解析到所选的 NAT 防火墙实例上。
 - 访问端口：通过指定端口访问域名。
 - 防护方式：分为基础防护和高级防护。
   - 基础防护：提供基于前端对抗和前端挑战的基础防护，对人机、攻击者等进行有效过滤。
   - 高级防护：通过微信身份认证对 Web 服务进行访问控制，高级防护仅支持 https 协议。
5. 接入防护参数配置完成后，根据选择方式的不同，配置步骤有所不同。
   - 如果防护方式选择**基础防护**，单击**确定**即可生成配置。
   - 如果防护方式选择高级防护，则需要选择绑定的用户，单击**确定**即可生成配置。
  ![](https://qcloudimg.tencent-cloud.cn/raw/207177650a12e6af2967c67f50e26a51.png)

## 编辑接入
Web 服务接入防护之后，在 [Web 服务管理页面](https://console.cloud.tencent.com/cfw/identityauth/webserv) 可以单击**编辑接入**来对配置做修改。具体可修改的内容包括：
![](https://qcloudimg.tencent-cloud.cn/raw/e06a328fed220593100230c7dcf0b116.png)
- 取消接入：对已生成防护的 Web 实例，取消对 Web 服务的防护。勾选接入方法一栏的取消接入，单击**确定**。
 ![](https://qcloudimg.tencent-cloud.cn/raw/c058afb2eeb320759e05491a094e53c4.png)
- 修改防护方式：将防护模式切换为基础防护或者是高级防护。
>!如果选择高级防护，则需要勾选启用 https，选择基础防护可不勾选。
>
![](https://qcloudimg.tencent-cloud.cn/raw/7b1ef6c686b7fc4d6b0edba06f78f7f1.png)
- 修改访问端口：访问端口支持自定义修改。
![](https://qcloudimg.tencent-cloud.cn/raw/163c080e0abee75e7add1bfa577e782b.png)


## 用户管理
在 Web 服务防护模式选择高级防护的前提下，支持微信扫码认证，绑定微信用户之后，可通过用户管理执行解绑或者新增绑定用户。
#### 解绑用户
1. 在 [Web 服务管理页面](https://console.cloud.tencent.com/cfw/identityauth/webserv)，将微信用户从 Web 实例解除绑定。选择已生成防护 Web 实例，单击操作列的**用户管理**。
![](https://qcloudimg.tencent-cloud.cn/raw/e3d528d1cbe7043d768a998f254a35ca.png)
2. 在管理授权用户弹窗中，单击![](https://qcloudimg.tencent-cloud.cn/raw/deb23bffd649c85bc41c35eddc6d1c37.png)删除用户，单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/fb915445cdf809cf9e7ae3ccc5353338.png)

#### 新增绑定用户
1. 在 [Web 服务管理页面](https://console.cloud.tencent.com/cfw/identityauth/webserv)，为 Web 实例绑定新的微信用户。选择已生成防护 Web 实例，单击操作列的**用户管理**。
![](https://qcloudimg.tencent-cloud.cn/raw/e3d528d1cbe7043d768a998f254a35ca.png)
2. 在管理授权用户弹窗中，勾选需要新增的用户，单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/e62535851dc4078628bc8901ec7a4825.png)

## 查看访问日志
访问日志记录了 Web 服务的运维记录，便于后续审计，也提高了 Web 服务的安全性。
1. 在 [Web 服务管理页面](https://console.cloud.tencent.com/cfw/identityauth/webserv)，选择已生成防护的 Web 实例，单击操作列的**查看日志**，跳转至零信任防护日志 > Web 服务访问页面。
![](https://qcloudimg.tencent-cloud.cn/raw/a49445a670a3244b105653c5f72aa33b.png)
2. 在 Web 服务访问页面，根据日志信息可以知道访问时间、访问用户、访问者 IP 和归属地、访问的 Web 服务以及是否访问成功等信息。
![](https://qcloudimg.tencent-cloud.cn/raw/88bd3b2899de3fc9299185366acce8b7.png)
