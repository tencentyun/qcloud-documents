### 步骤1：修改 NS 服务器记录
NS 接入方式下，用户需先按要求修改 NS 服务器记录，成功修改后站点 DNS 解析服务由 EdgeOne 提供。

### 步骤2：生成 CNAME
在 DNS 服务页面进行记录管理，可以添加主机记录（子域名），并选择不同的代理模式。
1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/teo) ，在左侧菜单栏中，单击 **DNS 服务**。
2. 在 DNS 服务页面，选择所需站点，单击**记录管理** > **添加记录**。
3. 在记录管理页面，填写所需参数，并选择代理模式，单击**保存**。
>?选定代理模式后，系统会以站点为粒度，自动下发站点加速/DDoS 防护的基本配置。同时，用户也可以登录控制台进行相应的证书管理、站点加速、WAF 防护等配置。
>
![](https://qcloudimg.tencent-cloud.cn/raw/dbac73b316137bc22f992456d2966046.png)
**参数说明：**
<table>
<thead>
<tr>
<th>参数名称</th>
<th>参数详情</th>
</tr>
</thead>
<tbody><tr>
<td>记录类型</td>
<td>各个记录类型有不用的用途，一般选择 A 记录。<ul><li>A 记录是最常用类型，将域名指向一个 IPv4 地址，如 <code>8.8.8.8</code>。</li><li>CNAME 将域名指向另一个域名地址，与其保持相同解析，如 <code>www.edgeone.com</code>。</li><li>MX 用于邮件服务器，相关参数一般由邮件注册商提供，默认优先级为 5，可修改。AAAA 将域名指向一个 IPv6 地址，如 <code>2400:cb00:2049:1::a29f:f9</code>。</li><li>TXT 可填写附加文本信息，常用于域名验证。</li><li>NS 域名服务器记录，可将指定域名交由其他 DNS 服务商解析管理。</li></ul></td>
</tr>
<tr>
<td>主机记录</td>
<td>主机记录相当于域名的前缀，如 www。<ul><li>www 常见主机记录，将域名解析为 <code>www.kbchen.com</code>。</li><li>@ 直接解析主域名 kbchen.com。</li><li>mail 将域名解析为 mail.kbchen.com，通常用于邮件服务。</li><li>* 泛解析，匹配其他所有域名 *.kbchen.com。</li></ul></td>
</tr>
<tr>
<td>记录值</td>
<td>请根据您选择的记录类型，按照格式要求填写记录值。</td>
</tr>
<tr>
<td>代理模式</td>
<td>根据实际需求，任意选择如下一种代理模式：<ul><li>安全加速：开启 EdgeOne 安全加速，独享 IP 资源，保证分发性能的同时实现 DDoS 高防。</li><li>代理加速：开启 EdgeOne 代理加速，共享 IP 资源，保证最佳分发性能。</li><li>仅 DNS：EdgeOne 仅提供 DNS 解析服务。</li></ul></td>
</tr>
<tr>
<td>TTL</td>
<td>指解析记录在 DNS 服务器缓存的生存时间，数值越小则生效越快。</td>
</tr>
</tbody></table>

### 步骤3：解析 DNS
在 CNAME 接入方式下，用户在 CNAME 接入界面添加主机记录（子域名）及对应的记录类型（源站类型）、记录值（源站地址），选择具体的代理模式，系统会生成具体的 CNAME。前往用户的 DNS 解析商添加改 CNAME 记录，则代理服务开始生效。

>?NS 接入方式，系统会为根域名 (example.com) 和三级泛域名 (*.example.com) 申请一本免费的 EdgeOne 通用证书。
