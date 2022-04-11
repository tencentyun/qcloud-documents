在 [CNAME 接入方式](https://cloud.tencent.com/document/product/1552/70787#CNAME) 下，用户无需将 DNS 解析权转移给 EdgeOne，只需添加记录（子域名）并选定相应的代理模式，在 DNS 解析商处添加指定的 CNAME 记录，即可接入 EdgeOne 安全/加速服务。
>?目前边缘安全加速平台控制台仅对部分用户开放，如需访问控制台，请 [联系我们](https://cloud.tencent.com/online-service) 开通权限。


## 添加记录（子域名接入）[](id:add)
在CNAME 接入方式下，通过添加记录来为该站点的子域名接入相应的服务。

1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone)，在左侧菜单栏中，单击 **DNS 服务**。
2. 在 DNS 服务页面，选择所需站点，单击**添加记录**。
![](https://qcloudimg.tencent-cloud.cn/raw/b4d03b29540ebf6fed378c9f153cfa43.png)
3. 填写相关参数，单击**保存**。
![](https://qcloudimg.tencent-cloud.cn/raw/9917f19924f371363e34351cdc57f1b7.png)
**参数说明：**
 - 记录类型：表示源站的类型。
 - 记录值：代表源站地址。
<table>
<thead>
<tr>
<th>记录类型</th>
<th>记录值示例</th>
<th>用途说明</th>
</tr>
</thead>
<tbody><tr>
<td>A</td>
<td>8.8.8.8</td>
<td>对应主机记录（子域名）将回源到一个 IPv4 源站，源站地址为 8.8.8.8</td>
</tr>
<tr>
<td>AAAA</td>
<td>2400:cb00:2049:1::a29f:f9</td>
<td>对应主机记录（子域名）将回源到一个 IPv6 源站，源站地址为 2400:cb00:2049:1::a29f:f9，EdgeOne 默认支持双栈回源</td>
</tr>
<tr>
<td>CNAME</td>
<td>www.origin.com</td>
<td>对应主机记录（子域名）将回源到一个域名源站，源站地址为 www.origin.com</td>
</tr>
</tbody></table>
 - 主机记录：相当于子域名的前缀，假设当前的站点为 `edgeone.com` ，则常见的主机记录如下表所示。
 <table>
<thead>
<tr>
<th>主机记录值</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>@</td>
<td>直接解析根域名 edgeone.com</td>
</tr>
<tr>
<td>www</td>
<td>常见主机记录，解析域名为 www.edgeone.com</td>
</tr>
<tr>
<td>mail</td>
<td>解析域名为 mail.edgeone.com，通常用于邮件服务</td>
</tr>
<tr>
<td>*</td>
<td>泛解析，匹配其他所有域名 *.edgeone.com</td>
</tr>
</tbody></table>
 - 代理模式：CNAME 接入方式支持以下三种服务（代理）模式，更多详情请参见 [代理模式](https://cloud.tencent.com/document/product/1552/70786)。
    - 关闭代理
    - 代理加速
    - 安全加速
 - CNAME：选中不同代理模式，系统将指定不同的 CNAME 后缀，用户需在 DNS 服务商处添加指定的 CNAME 记录。
 - HTTPS 证书：在 CNAME 接入方式下，系统不提供 EdgeOne 通用证书。需要手动为每个子域名关联证书，方可正常使用 HTTPS 服务。

## 切换 NS 接入[](id:change)
在 CNAME 接入页面，点击列表右上角**切换为 NS 接入**，可以切换至 NS 接入模式。切换后用户还需按要求修改 NS 服务器记录，修改生效后系统会通过邮件/短信/站内信通知。切换之后：
- 保留所有 CNAME 接入记录及代理模式，“关闭代理”的记录会变成“仅 DNS”。
- 保留所有子域名的自定义证书。

![](https://qcloudimg.tencent-cloud.cn/raw/837639d68b3d750e22902048ee583fbb.png)
