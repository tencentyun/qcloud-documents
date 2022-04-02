## 什么是 CAA？
CAA（Certification Authority Authorization，证书颁发机构授权）是一项降低 SSL 证书错误颁发的控制措施，由互联网工程任务组（IETF）批准列为 IETF RFC6844 规范。2017年3月，CA 浏览器（CA/Browser Forum）论坛投票通过187号提案，要求 CA 机构从2017年9月8日起执行 CAA 强制性检查。

## CAA 的作用？
域名所有者通过设置 CAA 解析记录来授权指定的 CA 机构为其颁发 SSL 证书，同时 CA 机构根据规范要求，在颁发 SSL 证书时会强制性检查域名 CAA 记录，如果检查发现未获得授权，将拒绝为该域名颁发 SSL 证书，从而防止未授权的 SSL 证书错误颁发，规避安全风险。如果域名所有者没有为其域名设置 CAA 记录，那么任何 CA 机构都可以为其域名颁发证书。

## 为什么要设置 CAA ？
据权威部门统计，全球约有上百个证书颁发机构（CA）有权发放 SSL 证书，以证明您网站的身份，但是证书颁发机构由于某些原因，往往会被浏览器列入 “黑名单”，并被公开宣布将不再信任其签发的 SSL 证书。由于任何 CA 都可以为任何域名颁发证书，这使得 PKI 生态系统较为脆弱。因此，当您的网站部署了不被浏览器信任的证书颁发机构所颁发的证书，用户访问时，部分浏览器将提示 “HTTPS 证书不受信任”，影响您的业务正常使用。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/44b70151126bddef6358ca2632e4e70c.png)
因此，为避免您不被错误的颁发证书，建议您为域名设置授信的 CAA 记录，若您需指定仅支持腾讯云 SSL 证书为其颁发，腾讯云不同品牌 CAA 记录值以下：

<table>
<thead>
  <tr>
    <th>证书品牌</th>
    <th colspan="2">记录值</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>SecureSite</td>
    <td>0 issue "digicert.com"	</td>
    <td>0 issuewild "digicert.com"</td>
  </tr>
  <tr>
    <td>GeoTrust</td>
    <td>0 issue "digicert.com"</td>
    <td>0 issuewild "digicert.com"</td>
  </tr>
  <tr>
    <td>TrustAsia</td>
    <td>0 issue "trust-provider.com"</td>
    <td>0 issuewild "trust-provider.com"</td>
  </tr>
  <tr>
    <td>GlobalSign</td>
    <td>0 issue "globalsign.com"</td>
    <td>0 issuewild "globalsign.com"</td>
  </tr>
  <tr>
    <td>WoTrus</td>
    <td>0 issue "wotrus.com"</td>
    <td>0 issuewild " wotrus.com"</td>
  </tr>
  <tr>
    <td>DNSPod<br>（国密标准（SM2））</td>
    <td>0 issue "wotrus.com"</td>
    <td>0 issuewild " wotrus.com"</td>
  </tr>
</tbody>
</table>

>? `0 issue`表示只有该 CA 机构可以为特定域名颁发证书，`0 issuewild`表示只有该 CA 机构可以为特定域名颁发通配符证书。
>

## CAA 记录格式说明
CAA 记录的格式为：`[flag] [tag] [value]`，是由一个标志字节的 `[flag]` 和一个被称为属性的`[tag]-[value]`（标签-值）对组成。您可以将多个 CAA 字段添加到域名的 DNS 解析记录中。

<table>
<thead>
  <tr>
    <th>字段</th>
    <th>说明</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>flag</td>
    <td>0-255之间的无符号整数，用于标志认证机构。通常情况下填0，表示如果颁发证书机构无法识别本条信息，就忽略。</td>
  </tr>
  <tr>
    <td>tag</td>
    <td>支持 issue、issuewild 和 iodef。<br>issue：CA 授权单个证书颁发机构发布的<b>任何类型域名证书</b>。<br>issuewild：CA 授权单个证书颁发机构发布主机名的<b>通配符证书</b>。<br>iodef：CA 可以将违规的颁发记录 URL 发送给某个电子邮箱。</td>
  </tr>
  <tr>
    <td>value</td>
    <td>CA 的域名或用于违规通知的电子邮箱。</td>
  </tr>
</tbody>
</table>


## 添加 CAA 记录
>? 以腾讯云免费证书为例，为域名添加对应 issue 和 issuewild 记录。
>
1. 登录 [DNSPod 管理控制台](https://console.dnspod.cn/dns/list)。
2. 在 “域名解析列表” 中，选择并单击需要添加 CAA 记录的域名，进入该域名的 DNS 解析记录管理页面。如下图所示：
![](https://main.qcloudimg.com/raw/74d113969f06f1f2d01f58b7af0a07bf.png)
3. 单击**添加记录**，填写以下记录信息。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/3690b1f101e1cc92f6489d2c6458f85a.png)
 - **主机记录**：填写子域名。例如为 `www.dnspod.cn`  添加 CAA 记录，您在 “主机记录” 处填写 “www” 即可。如果想添加 `dnspod.cn` 的 CAA 记录，您在 “主机记录” 处选择 “@” 即可。
 - **记录类型**：选择 “CAA”。
线路类型：选择 “默认” 类型，否则会导致部分 CA 机构无法进行认证。
 - **记录值**：分别  填写 `0 issue "sectigo.com"` 与 `0 issuewild "sectigo.com"`。
 - **权重**：不填写，可忽略。
 - **MX 优先级**：不填写，可忽略。
 - **TTL**：缓存的生存时间，默认600秒。如需修改，可参考 [TTL 如何填写？](https://tcloud-doc.isd.com/document/product/302/3468?!preview&!editLang=zh#ttl-.E5.A6.82.E4.BD.95.E5.A1.AB.E5.86.99.EF.BC.9F)
4. 单击【确定】，完成添加。


## 检查 CAA 记录
可通过以下两种方式检查已添加的 CAA 记录：
### dig 命令
```
dig 域名名称 CAA
```
返回值为空或包含 `0 issuewild "sectigo.com"` 和  `0 issue "sectigo.com"` 即为正常。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/701834cfd1f7ba71c8bf855e52b21550.png)

### DNS 诊断工具
前往 [DNS 诊断工具](https://myssl.com/dns_check.html?checking=caa#dns_check)，输入主域名并选择 CAA 记录后点击检测，返回值为空或包含 `0 issuewild "sectigo.com"` 和 `0 issue "sectigo.com"` 即为正常。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/97efadf3a79cf636da56baf2dabb22cb.png)
>? 若出现检测失败或只有部分地区可以正常检测的情况，请检查域名 DNS 解析设置。
>









