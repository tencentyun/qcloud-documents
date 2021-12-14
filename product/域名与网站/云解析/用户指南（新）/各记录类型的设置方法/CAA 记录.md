## 操作场景
如果您需要授权指定 CA 机构为您的域名签发 SSL 证书，以防止 SSL 证书错误签发，则需要添加 CAA 记录。本文档指导您如何添加 CAA 记录。
>!CAA 解析记录请前往 [DNSPod 管理控制台](https://console.dnspod.cn/dns/list) 进行设置。

## 操作步骤
1. 登录 [DNSPod 管理控制台](https://console.dnspod.cn/dns/list)。
2. 在 “域名解析列表” 中，选择并单击需要添加 CAA 记录的域名，进入该域名的 DNS 解析记录管理页面。如下图所示：
![](https://main.qcloudimg.com/raw/74d113969f06f1f2d01f58b7af0a07bf.png)
3. 单击【添加记录】，填写以下记录信息。如下图所示：
![](https://main.qcloudimg.com/raw/96a458f327c431c8e8f0988f3bb2503c.png)
 - **主机记录**：填写子域名。例如，添加 `www.dnspod.cn` 的解析，您在 “主机记录” 处填写 “www” 即可。如果只是想添加 `dnspod.cn` 的解析，您在 “主机记录” 处选择 “@” 即可。
 - **记录类型**：选择 “CAA”。
线路类型：选择 “默认” 类型，否则会导致部分 CA 机构无法进行认证。
 - **记录值**：
CAA 记录的格式为：[flag] [tag] [value]，是由一个标志字节的 [flag] 和一个被称为属性的 [tag]-[value]（标签-值）对组成。您可以将多个 CAA 字段添加到域名的 DNS 记录中。
<table>
<thead>
<tr>
<th width="10%">字段</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>flag</td>
<td>0-255之间的无符号整数，用于标志认证机构。默认情况下填写0，表示如果颁发证书机构无法识别本条信息，进行忽略。</td>
</tr>
<tr>
<td>tag</td>
<td>支持 issue、issuewild 和 iodef。</td>
</tr>
<tr>
<td>value</td>
<td>CA 的域名或用于违规通知的电子邮箱。</td>
</tr>
</tbody></table>
tag 字段说明：
<table>
<thead>
<tr>
<th width="10%">字段</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>issue</td>
<td>CA 授权单个证书颁发机构发布的 任何类型域名证书。</td>
</tr>
<tr>
<td>issuewild</td>
<td>CA 授权单个证书颁发机构发布主机名的通配符证书。</td>
</tr>
<tr>
<td>iodef</td>
<td>CA 可以将违规的颁发记录 URL 发送给某个电子邮箱。</td>
</tr>
</tbody></table>
 - **权重**：不需要填写。
 - **MX 优先级**：不需要填写。
 - **TTL**：为缓存时间，数值越小，修改记录各地生效时间越快，默认为600秒。
4. 单击【确定】，完成添加。


