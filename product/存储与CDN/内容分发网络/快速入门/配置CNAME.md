当您在腾讯云 CDN 内成功完成添加域名后，腾讯云 CDN 会为您的域名分配一个专属的 CNAME 地址，您还需要完成 CNAME 配置，才可以将用户的访问指向腾讯云 CDN 节点，使CDN加速生效。
>!
>1. 为避免解析冲突，若域名解析原来有配置 A 记录或 MX 记录，则添加 CNAME 记录时，应当将原 A 或 MX 记录暂停解析或删除。
>2. 因为 DNS 变更解析到实际生效需要一段时间，期间可能会导致网站暂时不可访问，请您留意变更操作对业务的影响。
>3. 为避免业务受到影响，当暂停或停用 CDN 加速时，域名解析应注意从 CDN CNAME 域名改回到源站。
>4. **请注意，CNAME 域名不可以直接作为访问域名使用。**

## 方法一：一键配置 CNAME
如果您当前的域名已托管于腾讯云 DNSPod 内，且当前账号有该域名的解析权限，则可以在添加完域名后，使用一键配置完成域名配置。您可后续前往 [dnspod 控制台](https://console.dnspod.cn/dns/list) 管理解析记录。
>!请确保当前账号有该域名的解析操作权限，若为子账号或协作者账号，请联系主账号授权。例如：授权对应 CDN 加速域名的写权限 + QcloudDNSPodFullAccess 权限。

1. 在添加完域名后，在第二步推荐配置内可选择跳过或提交配置，进入第三步配置 CNAME 界面；如果您已跳过配置返回了域名管理界面，请参考第三步；
2. 在配置 CNAME 界面内，如果当前域名已托管在 DNSPod 内，可单击右上角的一键配置按钮进行 CNAME 配置；
![](https://qcloudimg.tencent-cloud.cn/raw/6ee74c1d3a926551a2ca6a5927420d4b.png)
3. 如果您在添加域名时，第一步完成后直接返回了域名管理界面内，也可以在域名管理列表内，鼠标悬浮在 CNAME 前的图标上，即可看到相关提示，单击一键配置进入 CNAME 配置界面。
![](https://qcloudimg.tencent-cloud.cn/raw/a2488c72e180339a19e761819ce7ea61.png)
4. 腾讯云 CDN 将默认为您在 DNSPod 内针对该域名增加一条 CNAME 解析记录值，TTL 默认值为600。如果您的域名内已有一条 CNAME 解析记录值，为了防止 CNAME 解析冲突，将会为您自动删除原有的 CNAME 解析记录并增加一条新的 CNAME 解析记录值。
<img src="https://qcloudimg.tencent-cloud.cn/raw/95b458748d43d868e4578883ec47d4a5.png" width="80%">
5. 配置完成后，可单击右上方的验证 CNAME 状态，查看当前 CNAME 是否已生效，如果在一键配置后还未生效，请您稍等，CNAME 解析生效根据 TTL 设置需要一定时间。<br>
<img src="https://qcloudimg.tencent-cloud.cn/raw/ec10ce1021d0e45152815a88737bb227.png" width="80%">

## 方法二：手动配置 CNAME 
>! 新增的 CNAME 配置将实时生效，如果是修改 CNAME 配置，根据所设置的 TTL 时长生效时间不一（默认为600s，即10分钟），如果您修改了 CNAME 配置后，控制台内仍显示当前未完成 CNAME 配置，可忽略，通过其他方式判断当前 CNAME 是否生效，参考 [如何判断 CDN 是否生效](https://cloud.tencent.com/document/product/228/11202#.E5.A6.82.E4.BD.95.E5.88.A4.E6.96.AD-cdn-.E6.98.AF.E5.90.A6.E7.94.9F.E6.95.88.EF.BC.9F)。

**腾讯云 DNSPod 控制台配置方法：**
1. 在添加域名后，进入第三步：配置 CNAME 中，在 CNAME 信息内，复制当前域名的 CNAME 值；
![](https://qcloudimg.tencent-cloud.cn/raw/77070669476f264cb4c02e77888d7827.png)
或者在域名管理列表内，可复制对应域名的 CNAME 值；
2. 前往 [DNS 解析 DNSPod 控制台](https://console.cloud.tencent.com/cns)，找到对应的域名，单击**解析**按钮；
![](https://qcloudimg.tencent-cloud.cn/raw/3b207e3fbee797585d3818dd20c64502.png)
3. 单击**添加记录**，为该域名添加一条解析记录，解析记录填写参考如下：
![](https://qcloudimg.tencent-cloud.cn/raw/97dc3f0025481ebc1a119002993e95cd.png)
<table>
<thead>
<tr>
<th>参数</th>
<th>填写说明</th>
</tr>
</thead>
<tbody><tr>
<td>主机记录</td>
<td>可参考如下示例填写：<br>加速域名为<code>www.example.com</code>，主机记录值填写 www；<br>加速域名为<code>example.com</code>，主机记录值填写为@；<br>加速域名为<code>test.example.com</code>，主机记录值填写为 test；<br>加速域名为<code>a.b.example.com</code>，主机记录值填写为 a.b；<br>加速域名为<code>*.example.com</code>，主机记录值填写为*；<br>加速域名为<code>*.test.example.com</code>，主机记录值填写为<code>*.test</code>。</td>
</tr>
<tr>
<td>记录类型</td>
<td>选择 CNAME。</td>
</tr>
<tr>
<td>线路类型</td>
<td>建议保持为默认。</td>
</tr>
<tr>
<td>记录值</td>
<td>填写第一步所复制的 CNAME 信息。</td>
</tr>
<tr>
<td>MX 优先级</td>
<td>无需填写。</td>
</tr>
<tr>
<td>TTL（秒）</td>
<td>建议保持为默认值600s。</td>
</tr>
</tbody></table>
4. 单击**保存**后，即可完成 CNAME 配置。

[](id:m1)
## 如何验证 CNAME 是否生效
1. 在配置完成 CNAME 后，您可以在添加域名的第三步中，单击验证 CNAME 状态，查看当前域名 CNAME 是否生效，如果生效状态显示为已生效，则当前 CNAME 解析已正确生效，域名已启动 CDN 加速，如果当前生效状态未生效，需检查当前是否已完成 CNAME 配置，如果确认当前 CNAME 已正确配置，可能是当前解析生效延迟问题，您也可以选择用第3种方式进行验证。
![](https://qcloudimg.tencent-cloud.cn/raw/4cfd5767d752cfb845d0c31453f0c99f.png)
2. 您可以在控制台的域名管理列表内查看，如果域名的 CNAME 解析已有正确解析提示，表示当前 CDN 域名加速已生效。如果有两条 CNAME 解析的情况下，其中一条生效即可。
![](https://qcloudimg.tencent-cloud.cn/raw/dabe5b18b721e45fc0f12a48eb50a466.png)
3. 您也可以使用 nslookup 或 dig 命令来查看当前域名的解析生效状态。如果您的系统为 Windows 系统，在 Window 系统中打开 cmd 运行程序，以域名`www.test.com`为例，您可以在 cmd 内运行：`nslookup -qt=cname www.test.com`，根据运行的解析结果内，可以查看该域名的 CNAME 信息，如果与腾讯云 CDN 提供的 CNAME 地址一致，即当前 CDN 加速已生效。
![](https://qcloudimg.tencent-cloud.cn/raw/cde32f36a58eed85cc2f521f75a82fd9.png)
如果您的系统为 Mac 系统或 Linux 系统，可以使用 dig 命令进行验证，以域名`www.test.com`为例，您可以在终端内运行命令：`dig www.test.com`，根据运行的解析结果内，可以查看该域名的 CNAME 信息，如果与腾讯云 CDN 提供的 CNAME 地址一致，即当前的 CDN 加速已生效。
![](https://qcloudimg.tencent-cloud.cn/raw/f92fa942ce941a2efbb106b765529be5.png)

## 常见问题：
### 域名的 CNAME 已经修改，为什么控制台上还显示未生效？
新增的 CNAME 配置将实时生效，如果是修改 CNAME 配置，根据所设置的 TTL 时长生效时间不一（默认为600s，即10分钟）。如果您已确定完成了正确的 CNAME 配置，可忽略控制台内提示。

### `example.com`的域名接入后，`www.example.com`有加速效果吗？
没有，`example.com`和`www.example.com`分别属于两个域名，需要在控制台上全部接入才会有 CDN 加速效果。

### CNAME 域名可以当访问域名使用吗？
不可以，CNAME 域名为腾讯云 CDN 分配给每个域名的专属加速地址，不可以直接作为访问域名使用，需要用户将接入的业务域名 CNAME 到该地址上，访问用户的业务域名，即可有 CDN 加速效果。

