本文将介绍您在腾讯云申请免费 SSL 证书时，验证域名所有权中超时导致颁发失败如何排查处理。
>? 免费 SSL 证书颁发时间一般不超过30分钟，若超过您可参考本文自行排查导致超时原因。
>


## 排查 CAA 记录
无论是文件验证或 DNS 验证都需要检查 CAA 记录，无 CAA 记录或 CAA 记录中包含 `0 issuewild "sectigo.com"` 和 `0 issue "sectigo.com"` 均可通过 CAA 记录检查。

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

#### 解决方法
若返回检测结果不为空且不包含 `0 issuewild "sectigo.com"` 和 `0 issue "sectigo.com"`，请前往域名解析处添加以下记录：

|主机记录| 记录类型 | 线路类型 | 记录值 |
|---------|---------|---------|---------|
| @ | CAA | 默认 |0 issuewild "sectigo.com" |
| @ | CAA | 默认 |0 issue "sectigo.com" |


##  排查验证 DNS 记录
检查完 CAA 记录后请确认验证记录是否已经添加，若为自建 NS 或部分存在境外解析限制的 NS 请检查境外解析是否正常，可使用 DNS 诊断工具或 [DNSCHCKER](https://dnschecker.org/#CNAME/) 工具进行检测，一般情况下，所有监测点均能正常返回且返回值相同。
1. 确定检测域名。
检测域名应为`主机记录.域名`，例如，证书主机记录为`_26A56EBADCE479E******5D304C0D8.blog`，域名为 `dnspod.cn`，则要检测域名为 `_26A56EBADCE479E******5D304C0D8.blog.dnspod.cn`。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/5e2ae846c22565468b33a0862c0706f6.png)
2. 前往 [DNS 诊断工具](https://myssl.com/dns_check.html?checking=caa#dns_check)，输入检测域名并选择 CNAME 记录后，单击**检测**，返回值为控制台提示的记录值即为正常。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/20464f9d297d9a2efbc8567f33caadd3.png)

##  排查服务器是否屏蔽验证 IP
使用文件验证方式通过后进入 “等待机构签发” 时，长时间不颁发证书的原因一般为服务器或机房屏蔽了 CA 的验证 IP，请将 CA 验证 IP 加白：`64.78.193.238`、`216.168.247.9`。


