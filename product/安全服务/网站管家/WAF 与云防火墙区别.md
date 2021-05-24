### Web 应用防火墙（WAF）与云防火墙区别是什么？
Web 应用防火墙（WAF）与云防火墙的区别如下：
<table>
<thead>
<tr>
<th style ="width:95px;height:45px;position:relative;text-align:left;padding:5px 7px;font-weight:900;" valign="top" rowspan="2"><div style="position:absolute;width:1px;height:130px;top:0;left:0;background-color: #d9d9d9;display:block;transform:rotate(-55deg);transform-origin:top;valign=top;"  ></div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;产品<br><br>对比项</th>
<th colspan="2" style ="text-align:center">腾讯云 Web 应用防火墙（WAF）</th>
<th rowspan="2" style ="text-align:center">腾讯云防火墙（CFW）</th>
</tr>
<tr>
<th style ="text-align:center">SAAS 型 WAF</th>
<th style ="text-align:center">负载均衡型 WAF（CLB WAF）</th>
</tr>
</thead>
<tbody>
<tr>
<th>防护对象</th>
<td>网站和 API 服务。</td>
<td>网站和 API 服务。</td>
<td>全部暴露到互联网的业务。</td>
</tr>
<tr>
<th>适用场景</th>
<td>有等保或重保需求的客户，关注 Web 和 API 安全防护，关注应用层防护和机器防刷。</td>
<td>有等保或重保需求的客户，关注 Web 和 API 安全防护，关注应用层防护和机器防刷，且腾讯云上已使用或计划使用七层负载均衡的客户。</td>
<td>有等保或重保需求客户，或关注 CVM 主机及网络安全的客户。</td>
</tr>
<tr>
<th>核心防护能力</th>
<td><ul><li>Web 漏洞和未知威胁防护，自助漏报和误报处理。 </li><li>CC 攻击防护。 </li><li>BOT 行为管理/爬虫防护。</li><li>API 安全和业务安全防护。 </li><li>防泄漏/防篡改。</li></td>
<td><ul><li>Web 漏洞和未知威胁防护，自助漏报和误报处理。 </li><li>CC 攻击防护 。 </li><li>BOT 行为管理。 </li><li>API 安全和业务安全防护。 </li><li>网站 IPv6 防护。 </li></td>
<td><ul><li>IPS 的虚拟补丁能力，无需 CVM 安装实体补丁，无需重启。含 OWASP TOP 10 Web 基础漏洞防护。</li><li>自动发现失陷主机，对 CVM 的恶意外联行为进行自动阻断。</li><li>支持基于域名的主动外联控制。</li></td>
</tr>
<tr>
<th>核心优势</th>
<td>适用范围广阔，广泛覆盖腾讯云上和非腾讯云上用户。</td>
<td>云原生接入，接入无需要调整现有的网络架构。 网站业务转发和安全防护分离，一键 bypass，保障网站业务安全、稳定可靠，支持多地域接入，仅覆盖腾讯云上用户。</td>
<td>云原生防火墙，一键开启，对客户业务无任何影响。 集成了 IPS、威胁情报、漏扫等安全能力，等保及重保场景必备，仅覆盖腾讯云上用户。</td>
</tr>
<tr>
<th>如何选择</th>
<td>云上和本地 IDC 均有网站和 API 防护需求的客户，推荐使用 SAAS 型 WAF。</td>
<td>腾讯云上已使用或计划使用七层负载均衡的用户，推荐使用负载均衡型 WAF。</td>
<td>对于关注 CVM 的防护效果，关注 CVM 是否失陷，特别是业务对外除了 Web 服务，还暴露了其他公网服务，推荐选择云防火墙。</td>
</tr>
</tbody></table>
