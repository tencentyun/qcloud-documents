CIAM 支持应用系统基于标准 OpenID Connect (OIDC) 协议接入。CIAM 支持账号密码、短信 OTP、邮箱 OTP、微信 PC 扫码、微信小程序登录、支付宝登录等多种认证方式；支持用户通过表单注册或首次登录自动注册，且通过腾讯云控制台提供了便捷的界面对以上功能进行灵活的定制。

## 步骤1：安装 WordPress OIDC 插件
WordPress 站点将通过标准 OIDC 协议与 CIAM 对接，因此，我们首先安装并启用 WordPress 的 OIDC 插件。
1. 在 WordPress 后台选择**插件** > **安装插件**，搜索并安装 OpenID Connect Generic Client 插件。
![](https://qcloudimg.tencent-cloud.cn/raw/b9bd1074eb2186397902213c8c9a0e1f.jpg)
2. 启用插件，再次访问登录页面时，发现页面上部增加了一个按钮 **Login with OpenID Connect** 。
![](https://qcloudimg.tencent-cloud.cn/raw/debb56803d3d75a380e74255ce6a88f0.jpg)
>!由于还未对 CIAM 进行配置，此功能暂时还不可用，详细操作请参见 [步骤2：配置 CIAM 应用](#step2) 。

## 步骤2：配置 CIAM 应用[](id:step2)
### 前提条件
已完成 [新建用户目录](https://cloud.tencent.com/document/product/1441/60657)。

### 获取用户目录域名
1. 登录 [数字身份管控平台（公众版）控制台](https://console.cloud.tencent.com/ciam)，在左侧导航栏，选择**个性化设置** > **域名设置**，进入域名设置页面。
2. 在域名设置页面，获取用户目录的域名。
>?如需设置自定义域名，可参见 [域名设置](https://cloud.tencent.com/document/product/1441/61161)。
>
![](https://qcloudimg.tencent-cloud.cn/raw/1ee85271202546276574ea6cab5410b1.png)

### 配置应用参数
用户目录是 CIAM 的一个基础“容器”，用户的账号信息、用户访问的应用系统的相关配置、用户的认证方式等都将在用户目录中进行存储与配置。CIAM 需要有一个用户目录中的应用来扮演 WordPress 站点的角色，实现 WordPress 与  CIAM 的对接。
1. 登录 [数字身份管控平台（公众版）控制台](https://console.cloud.tencent.com/ciam)，在左侧导航栏选择**应用管理**，进入应用管理页面。
2. 在应用管理页面，单击操作列的**新建应用**，弹出新建应用弹窗。
![](https://main.qcloudimg.com/raw/39d602e8747cad6d90f0f22d2afd1b19.png)
3. 在新建应用弹窗中，根据要求填写相关信息，其中应用类型需选择 **Web 应用**，单击**确定**，即可创建新应用。
![](https://main.qcloudimg.com/raw/7e02bdb5f71f412b127c05a305b5ac42.png)
4. 在应用管理页面，选择刚刚创建的应用，单击操作列的**配置**，进入应用配置的基本信息页面。
![](https://qcloudimg.tencent-cloud.cn/raw/6f459faed85315fcfbab45c200286f4d.png)
5. 在基本信息页面，可以对应用图标、名称、类型、描述，所属行业进行变更，变更后单击**确定**保存。
![](https://qcloudimg.tencent-cloud.cn/raw/4835821f2fe4c087c771bda0e2f2f3bc.png)
6. 单击**参数配置**，根据要求填写相关信息后，单击**确定**保存。
![](https://main.qcloudimg.com/raw/70cec49c80d36b144b2211729da97fac.png)
参数说明
<table>
<thead>
<tr>
<th align="left">参数名</th>
<th align="left">参数值</th>
</tr>
</thead>
<tbody><tr>
<td align="left">Redirect URI</td>
<td align="left"><code>https://WORDPRESS.SITE/wp-admin/admin-ajax.php?action=openid-connect-authorize</code></td>
</tr>
<tr>
<td align="left">Logout Redirect URI</td>
<td align="left"><code>https://WORDPRESS.SITE</code></td>
</tr>
<tr>
<td align="left">其他参数</td>
<td align="left">使用默认值</td>
</tr>
</tbody></table>
>?请使用您实际的 WordPress 站点根路径替换`https://WORDPRESS.SITE`。
7.  单击**流程配置**，在注册流程处单击**编辑**，配置所需内容，单击**确定**保存。
![](https://qcloudimg.tencent-cloud.cn/raw/1c188356ef017c8c4cd68092df82d2eb.png)
参数说明
<table>
<thead>
<tr>
<th align="left">参数名</th>
<th align="left">参数值</th>
</tr>
</thead>
<tbody><tr>
<td align="left">是否启用</td>
<td align="left">开启</td>
</tr>
<tr>
<td align="left">认证属性</td>
<td align="left">邮箱地址、用户昵称</td>
</tr>
<tr>
<td align="left">普通属性</td>
<td align="left">用户昵称和性别作为必选项</td>
</tr>
<tr>
<td align="left">所属用户组</td>
<td align="left">按照实际需求选择</td>
</tr>
<tr>
<td align="left">自动登录</td>
<td align="left">按照实际需求选择</td>
</tr>
</tbody></table>
8. 单击**流程配置**，在登录流程处单击**编辑**，配置所需内容，单击**确定**保存。
![](https://qcloudimg.tencent-cloud.cn/raw/fbb071d374779e0efb086790226b9657.png)
参数说明
<table>
<thead>
<tr>
<th align="left">参数名</th>
<th align="left">参数值</th>
</tr>
</thead>
<tbody><tr>
<td align="left">是否启用</td>
<td align="left">开启</td>
</tr>
<tr>
<td align="left">首选认证源</td>
<td align="left">账号密码认证</td>
</tr>
<tr>
<td align="left">关联认证源</td>
<td align="left">-</td>
</tr>
<tr>
<td align="left">claims</td>
<td align="left">用户昵称、用户名称、邮箱地址、性别</td>
</tr>
<tr>
<td align="left">记住密码</td>
<td align="left">按照实际需求选择</td>
</tr>
</tbody></table>
9. 完成以上配置后，返回应用管理页面， 单击![](https://qcloudimg.tencent-cloud.cn/raw/8cae7bc49a3e820ccda4290f79669bef.png)启用该应用。
![](https://qcloudimg.tencent-cloud.cn/raw/ac13da683b3f9da92161578b293ee8dc.png)

## 步骤3：配置 WordPress OIDC 插件
在 WordPress 后台选择**设置** > **OpenID Connect Client**，根据参数说明，配置相关参数，单击**确定**保存。
![](https://qcloudimg.tencent-cloud.cn/raw/703ed959edc6093f2bbfe0a95ebbde7a.jpg)

| 参数名                        | 参数值                                                       |
| :---------------------------- | :----------------------------------------------------------- |
| Login Type                    | OpenID Connect button on login form                          |
| Client ID                     | 进入 [应用管理页面](https://console.cloud.tencent.com/ciam/app-management)，单击所需**应用名称**，获取该应用的 clientID |
| Client Secret Key             | 进入 [应用管理页面](https://console.cloud.tencent.com/ciam/app-management)，单击所需**应用名称**，获取该应用的 Secret |
| OpenID Scope                  | openid                                                       |
| Login Endpoint URL            | `https://dev-wordpress.portal.tencentciam.com/oauth2/authorize` |
| Userinfo Endpoint URL         | `ttps://dev-wordpress.portal.tencentciam.com/userinfo`       |
| Token Validation Endpoint URL | `https://dev-wordpress.portal.tencentciam.com/oauth2/token`  |
| End Session Endpoint URL      | ` https://dev-wordpress.portal.tencentciam.com/logout?client_id=CLIENT_ID&logout_redirect_uri=https://WORDPRESS.SITE` |
| Identity Key                  | sub                                                          |
| Nickname Key                  | nickname                                                     |
| Email Formatting              | {email}                                                      |
| 其他参数                      | 使用默认值或留空                                             |
>?
>- 请使用实际的 CIAM 用户目录域名替换掉 `https://dev-wordpress.portal.tencentciam.com`。
>- 请使用实际的 CIAM 应用 Client ID 替换以上的 CLIENT_ID。
>- 请使用实际的 WordPress 站点根路径替换以上的 `https://WORDPRESS.SITE`。 
>



## 步骤4：运行效果
1. 再次访问 WordPress 登录页，单击 **Login with OpenID Connect**，在弹出的 CIAM 登录页上输入账号密码，单击**登录**。
![](https://qcloudimg.tencent-cloud.cn/raw/27c2ab2bd8e8bb6ab11a8ea7d6c529bb.png)
2. 登录成功后，将自动跳转回登录前访问的 WordPress 页面。


## 用户管理和操作日志
使用 CIAM 接管 WordPress 登录后，可以登录数字身份管控平台（公众版）控制台查看相关用户信息和登录日志。
- 在[用户管理页面](https://console.cloud.tencent.com/ciam/user-management)，可查看已注册用户的列表及用户详情，并且可以进行编辑用户详情、重置用户密码或锁定、冻结、删除用户等操作，具体操作详情请参见 [用户管理](https://cloud.tencent.com/document/product/1441/60348)。
![](https://qcloudimg.tencent-cloud.cn/raw/5c950ee3d11f40347a4360aed7d04b1c.jpg)
- 在[审计管理页面](https://console.cloud.tencent.com/ciam/audit-management)，可以查看用户登录的详细情况，详细操作请参见 [审计管理](https://cloud.tencent.com/document/product/1441/61159)。
![](https://qcloudimg.tencent-cloud.cn/raw/94626338777a60a1c20f6ca1003fe40d.jpg)
