在 [CNAME 接入方式](https://cloud.tencent.com/document/product/1552/70787#CNAME) 下，用用户无需将 DNS 解析权转移给 EdgeOne，只需添加记录（子域名）并选定相应的代理模式开启代理，在 DNS 解析商处添加指定的 CNAME 记录，即可接入 EdgeOne 安全/加速服务。
>?目前边缘安全加速平台控制台仅对部分用户开放，如需访问控制台，请 [联系我们](https://cloud.tencent.com/online-service) 开通权限。


## 添加记录（子域名接入）[](id:add)
在CNAME 接入方式下，通过添加记录来为该站点的子域名接入相应的服务。

1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone)，在左侧菜单栏中，单击 **域名服务**。
2. 在域名服务页面，选择所需站点，单击**添加域名**。
![](https://qcloudimg.tencent-cloud.cn/raw/f1bdaf680a843aa6af9f13d665c93665.png)
3. 填写相关参数，单击**保存**。
![](https://qcloudimg.tencent-cloud.cn/raw/1ad684425c6fb23bf1399254f04c821a.png)
**参数说明：**
 - 加速域名：填写需开启加速的子域名，仅需输入子域名的前缀。
 - 源站类型：可选择 IPv4/IPv6/域名。
 - 源站地址：源站类型和源站地址示例如下
<table>
<thead>
<tr>
<th>源站类型</th>
<th>源站地址示例</th>
<th>用途说明</th>
</tr>
</thead>
<tbody><tr>
<td>IPv4</td>
<td>8.8.8.8</td>
<td>回源到一个 IPv4 源站，源站地址为 8.8.8.8</td>
</tr>
<tr>
<td>IPv6</td>
<td>2400:cb00:2049:1::a29f:f9</td>
<td>回源到一个 IPv6 源站，源站地址为 2400:cb00:2049:1::a29f:f9。<br>EdgeOne 默认支持双栈回源</td>
</tr>
<tr>
<td>域名</td>
<td>www.origin.com</td>
<td>回源到一个域名源站，源站地址为 www.origin.com</td>
</tr>
</tbody></table>
 - 代理模式：支持开启/关闭代理，更多详情请参见 [代理模式](https://cloud.tencent.com/document/product/1552/70786)。
 - CNAME：开启代理后系统自动生成，用户需在 DNS 服务商处添加该 CNAME 记录。
 - HTTPS 证书：在 CNAME 接入方式下，系统不提供 EdgeOne 通用证书。需要手动为每个子域名关联证书，方可正常使用 HTTPS 服务。

## 切换 NS 接入[](id:change)
在 CNAME 接入页面，点击列表右上角**切换为 NS 接入**，可以切换至 NS 接入模式。切换后用户还需按要求修改 NS 服务器记录，修改生效后系统会通过邮件/短信/站内信通知。切换之后：
- 保留所有 CNAME 接入记录及代理模式，“关闭代理”的记录会变成“仅 DNS”。
- 保留所有子域名的自定义证书。
![](https://qcloudimg.tencent-cloud.cn/raw/0b994e266d330fc04ca34148b3d5db59.png)
