## 前提条件
已完成 [新建用户目录](https://cloud.tencent.com/document/product/1441/60657)。

## 步骤1：配置回调地址
 1. 在 [应用管理页面](https://console.cloud.tencent.com/ciam/app-management)，选择所需应用，单击操作列的**配置**，进入应用配置的基本信息页面。
![](https://qcloudimg.tencent-cloud.cn/raw/67361297a609ed36b047a3f1b5c8de6a.png)
 2. 单击**参数配置**，输入 Redirect URI、Logout Redirect URI 的参数值，单击**确定**即可保存配置。
 ![](https://qcloudimg.tencent-cloud.cn/raw/6a7d259797dbdb1daba12aa04367c7a0.png)
 **参数说明**
<table>
<thead>
<tr>
<th align="left">参数名</th>
<th align="left">参数值</th>
</tr>
</thead>
<tbody><tr>
<td align="left">Redirect URI</td>
<td align="left">${部署函数生成的网关url}/callback</td>
</tr>
<tr>
<td align="left">Logout Redirect URI</td>
<td align="left">${部署函数生成的网关url}/logout ， ${部署函数生成的网关url}/release/</td>
</tr>
</tbody></table>
>?${部署函数生成的网关url}为 [步骤1：创建 Express 框架模版](https://cloud.tencent.com/document/product/1441/63582) 中所获取的访问路径的值。

## 步骤2：获取初始化参数
Serverless Express 框架模版(Auth)中需要 `Redirect URI、Logout Redirect URI、clientId ID、userDomain` 参数用于为初始化。
- 获取 Redirect URI 和Logout Redirect URI
 1. 在 [应用管理页面](https://console.cloud.tencent.com/ciam/app-management)，选择所需应用，单击操作列的**配置**，进入应用配置的基本信息页面。
 ![](https://qcloudimg.tencent-cloud.cn/raw/364f028a4f59037092f34ae47735b972.png)
 2. 单击**参数配置**，获取 Redirect URI 和Logout Redirect URI 的回调地址。
![](https://qcloudimg.tencent-cloud.cn/raw/c058b89bafa5036935fe3356542c28b8.png)
- 在应用管理页面，选择所需应用，获取该应用的 clientId ID。
![](https://qcloudimg.tencent-cloud.cn/raw/e825c14cd4d8adb1547196cb2d4b2f7b.png)
- 在 [域名设置页面](https://console.cloud.tencent.com/ciam/custom-domain-name)，获取 userDomain 租户域名。
>?如需设置自定义域名，可参见 [域名设置](https://cloud.tencent.com/document/product/1441/61161)。
>
![](https://qcloudimg.tencent-cloud.cn/raw/1ee85271202546276574ea6cab5410b1.png)
