在[ NS 接入方式](https://cloud.tencent.com/document/product/1552/70787#NS) 下，支持通过修改 NS 记录，将 DNS 解析权转移给 EdgeOne，实现稳定专业的解析服务的同时，一键开启 EdgeOne 安全/加速服务。
>?目前边缘安全加速平台控制台仅对部分用户开放，如需访问控制台，请 [联系我们](https://cloud.tencent.com/online-service) 开通权限。

## 记录管理[](id:record)
EdgeOne DNS 支持多种记录类型的智能解析服务，根据用户所在地理位置及运营商智能返回最佳解析线路。
1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone)，在左侧菜单栏中，单击 **DNS 服务**。
2. 在 DNS 服务页面，选择所需站点，单击**记录管理** 。
3. 在记录管理页面，选择所需记录，单击**编辑**，编辑相关参数，单击**保存**。
![](https://qcloudimg.tencent-cloud.cn/raw/51099ccc2bed87d3919e781ad520a712.png)
**参数说明：**
 - 记录类型及记录值：不同的记录类型有不同的用途。
<table>
<thead>
<tr>
<th align="left">记录类型</th>
<th align="left">记录值示例</th>
<th align="left">用途说明</th>
</tr>
</thead>
<tbody><tr>
<td align="left">A</td>
<td align="left">8.8.8.8</td>
<td align="left">将域名指向一个外网 IPv4 地址，如 8.8.8.8</td>
</tr>
<tr>
<td align="left">AAAA</td>
<td align="left">2400:cb00:2049:1::a29f:f9</td>
<td align="left">将域名指向一个外网 IPv6 地址</td>
</tr>
<tr>
<td align="left">CNAME</td>
<td align="left">cname.edgeone.com</td>
<td align="left">将域名指向另一个域名，再由该域名解析出最终 IP 地址</td>
</tr>
<tr>
<td align="left">MX</td>
<td align="left">优先级：10 记录值：mail.edgeone.com</td>
<td align="left">用于邮箱服务器，相关记录值/优先级参数有邮件注册商提供。存在多条 MX 记录时，优先级越低越优先</td>
</tr>
<tr>
<td align="left">TXT</td>
<td align="left">ba21a62exxxxxxxxxxcf5f06e</td>
<td align="left">对域名进行标识和说明，常用于域名验证和 SPF 记录（反垃圾邮件）</td>
</tr>
<tr>
<td align="left">NS</td>
<td align="left">ns01.edgeone.com</td>
<td align="left">如果需要将子域名交给其他 DNS 服务商解析，则需要添加 NS 记录。根域名无法添加 NS 记录</td>
</tr>
</tbody></table>
>?A/AAAA/CNAME 记录类型，在开启 [代理加速/安全加速](https://cloud.tencent.com/document/product/1552/70786) 时，其对应记录值就是经过代理后最终回源的源站地址。
 - 主机记录：相当于子域名的前缀，假设当前的站点为 `edgeone.com` ，则常见的主机记录如下表所示。
<table>
<thead>
<tr>
<th align="left">主机记录值</th>
<th align="left">说明</th>
</tr>
</thead>
<tbody><tr>
<td align="left">@</td>
<td align="left">直接解析根域名 <code>edgeone.com</code></td>
</tr>
<tr>
<td align="left">www</td>
<td align="left">常见主机记录，解析域名为 <code>www.edgeone.com</code></td>
</tr>
<tr>
<td align="left">mail</td>
<td align="left">解析域名为 <code>mail.edgeone.com</code>，通常用于邮件服务</td>
</tr>
<tr>
<td align="left">*</td>
<td align="left">泛解析，匹配其他所有域名 <code>*.edgeone.com</code></td>
</tr>
</tbody></table>
 同一个主机记录可创建多条记录类型，其共存关系：
<table>
<thead>
<tr>
<th>记录类型</th>
<th>A</th>
<th>AAAA</th>
<th>CNAME</th>
<th>MX</th>
<th>NS</th>
<th>TXT</th>
</tr>
</thead>
<tbody><tr>
<th>A</th>
<td>&#10003;</td>
<td>&#10003;</td>
<td>×</td>
<td>&#10003;</td>
<td>×</td>
<td>&#10003;</td>
</tr>
<tr>
<th>AAAA</th>
<td>&#10003;</td>
<td>&#10003;</td>
<td>×</td>
<td>&#10003;</td>
<td>×</td>
<td>&#10003;</td>
</tr>
<tr>
<th>CNAME</th>
<td>×</td>
<td>×</td>
<td>×</td>
<td>×</td>
<td>×</td>
<td>×</td>
</tr>
<tr>
<th>MX</th>
<td>&#10003;</td>
<td>&#10003;</td>
<td>×</td>
<td>&#10003;</td>
<td>×</td>
<td>&#10003;</td>
</tr>
<tr>
<th>NS</th>
<td>×</td>
<td>×</td>
<td>×</td>
<td>×</td>
<td>&#10003;</td>
<td>×</td>
</tr>
<tr>
<th>TXT</th>
<td>&#10003;</td>
<td>&#10003;</td>
<td>×</td>
<td>&#10003;</td>
<td>×</td>
<td>&#10003;</td>
</tr>
</tbody></table>
 - 代理模式：可选择**仅 DNS/代理加速/安全加速**三种代理模式，各记录类型可开启的代理模式不同。
<table>
<thead>
<tr>
<th align="left">记录类型</th>
<th align="left">代理模式</th>
</tr>
</thead>
<tbody><tr>
<td align="left">A/AAAA/CNAME</td>
<td align="left">可选择<strong>仅 DNS/代理加速/安全加速</strong>，默认为安全加速</td>
</tr>
<tr>
<td align="left">MX/TXT/NS</td>
<td align="left">只能选择<strong>仅 DNS</strong></td>
</tr>
</tbody></table>
>?
>- 对于同一个主机记录（子域名），一旦开启代理加速/安全加速，其他未开启代理的记录类型将失效。
>- 对于同一个主机记录（子域名），允许多个 A/AAAA 记录同时开启代理加速/安全加速；但如果是 CNAME 类型，不管处于任何代理模式，都仅允许一个记录存在。
 - TTL：指解析记录的缓存指导时间，一般来讲 TTL 越短，则解析记录缓存时间越短，记录值更新时生效也越快，但对解析速度略有影响。
    - 当前可选择的 TTL 值为：自动/1分钟/2分钟/5分钟/10分钟/15分钟/30分钟/1小时/2小时/5小时/12小时/1天，选中自动时系统配置 TTL 为300秒。
    - TTL 配置原则为：
      - 记录值较少变动时，建议选择 1 小时及以上，有利于提升解析速度。
      - 记录值频繁变动，可选择较短 TTL 值如 1 分钟，但解析速度可能略受影响。
>?
> - 代理加速/安全加速下，TTL 默认为自动，无法选择。
>- 实际情况一般 LDNS 缓存配置不一定遵循 TTL，导致解析记录更新生效时间经常远大于 TTL。


## 切换 CNAME 接入[](id:change)
在 NS 接入页面，单击列表右上角的**切换为 CNAME 接入**，可以切换至 CNAME 接入模式。首次切换需要进行 [站点验证](https://cloud.tencent.com/document/product/1552/70789)，如站点之前已经验证过，则会跳过验证，直接完成切换。切换之后：
- 保留原有的 DNS 记录，A/AAAA/CNAME 记录可以编辑/删除，MX/NS/TXT 记录无法编辑只能删除。
- 继承所有记录原有的代理模式，其中代理模式为“仅 DNS”的记录，切换后会变成“关闭代理”的状态。
- 保留 EdgeOne 通用证书，但 CNAME 模式下证书无法自动更新，过期后将自动删除。
- 保留所有子域名的自定义证书。

![](https://qcloudimg.tencent-cloud.cn/raw/a4325ae0876db1179a574be6f6775042.png)


## 高级配置
支持 DNSSEC、自定义 NS 服务器、CNAME 加速等高级配置。

### DNSSEC[](id:dnsses)
DNSSEC (DNS Security Extension，DNS 安全扩展) 通过数字签名对 DNS 数据来源进行认证，有效保护解析结果的安全性与完整性，常用于应对 DNS 欺骗和 DNS 缓存污染。

1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone) ，在左侧菜单栏中，单击 **DNS 服务**。
2. 在 DNS 服务页面，选择所需站点，单击**高级配置**。
3. 在高级配置页面，单击 DNSSEC 模块的![](https://qcloudimg.tencent-cloud.cn/raw/20efaa7f4ecc99b93da623f1c61784ac.png)，经过二次确认后，开启 DNSSEC 功能并生成 DS 信息。
![](https://qcloudimg.tencent-cloud.cn/raw/80d1829fa50c81075caa075677f95240.png)
![](https://qcloudimg.tencent-cloud.cn/raw/61663e5e8ba50eec690a4d46c34b04af.png)
4. 根据上述信息，在域名注册商处添加 DS 记录，部分域名注册商的相关操作可参见如下文档。
 - [DNSimple](https://support.dnsimple.com/articles/cloudflare-ds-record/)
 - [GoDaddy](https://ph.godaddy.com/help/add-a-ds-record-23865)
 - [Google Domains](https://support.google.com/domains/answer/6387342?hl=en)
 - [name.com](https://www.name.com/support/articles/205439058-Managing-DNSSEC)
 - [Public Domain Registry](http://manage.publicdomainregistry.com/kb/answer/1909)

### 自定义 NS 服务器[](id:customize)
自定义名称服务器允许您创建自己站点专属的名称服务器，以替代所分配默认名称服务器。创建后 EdgeOne 会自动为自定义 NS 分配对应的 IP 地址。
>?自定义 NS 服务器有如下限制：
>- 只能以当前站点 (example.com) 的子域名 (ns.example.com) 作为自定义 NS。
>- 自定义 NS 需至少有 2 个，最多可添加 5 个。
>- 首次开启需添加两个自定义 NS 域名，自定义名称不能和现有 DNS 记录冲突。

1. 在 [DNS 服务页面](https://console.cloud.tencent.com/edgeone/dns?tab=config)，选择所需站点，单击**高级配置**。
2. 在高级配置页面，单击自定义 NS 服务模块的![](https://qcloudimg.tencent-cloud.cn/raw/20efaa7f4ecc99b93da623f1c61784ac.png)，输入自定义 NS 域名，单击**添加**。
3. 添加成功后，**需要在域名注册商添加该自定义 NS 的胶水记录，才能真正生效**。

### CNAME 加速[](id:up)
开启后可有效提升解析速度，当域名在 EdgeOne DNS 设置多级 CNAME 记录时，系统将直接给出最终 IP 解析结果，减少解析次数。此功能默认开启。

1. 在 [DNS 服务页面](https://console.cloud.tencent.com/edgeone/dns?tab=config)，选择所需站点，单击**高级配置**。
2. 在高级配置页面，单击 CNAME 加速模块的“开关”，可关闭或开启 CNAME 加速功能。
>?多级 CNAME 必须全部在 EdgeOne DNS，才能实现 IP 直出。


