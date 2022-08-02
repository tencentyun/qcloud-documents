为提升非中国大陆地区的业务接入和防护能力配置体验，自2022年6月6日起，Web 应用防火墙（WAF）的产品能力全新升级。升级后，接入更稳定，防护能力更强大、流量管理支持更精细，并支持 BOT 行为管理和日志服务的增值能力。

同时，控制台将增加中国大陆和非中国大陆地区划分，并支持通过“地区切换”来对两个地区实例进行切换，管理不同地区的实例资源。详细如下图，支持在  [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/tea-overview) 进行切换：
![](https://qcloudimg.tencent-cloud.cn/raw/49e3438c06bbbde696f498f1283d402f.png)
具体对不同类型的 WAF 实例影响如下：
<table>
<thead>
<tr>
<th>产品类型</th>
<th>详情</th>
<th>解决办法</th>
</tr>
</thead>
<tbody><tr>
<td>SAAS 型 WAF 实例</td>
<td>WAF 继续保持实例地域属性，系统自动根据地域字段增加地区字段，产品控制台区分地区管理，其他无变化。</td>
<td>-</td>
</tr>
<tr>
<td rowspan=2>负载均衡型 WAF 实例</td>
<td  rowspan=2><li>中国大陆地区的 WAF 实例仅支持中国大陆 CLB 实例的 Web 业务接入防护</li><li>非中国大陆地区的 WAF 实例仅支持非中国大陆 CLB 实例的 Web 业务接入防护</li></td>
<td>若您仅接入非中国大陆 CLB 实例的 Web 业务。系统将根据实例地域自动升级为非中国大陆地区，且后续将仅支持接入非中国大陆的 CLB 实例，升级过程不需要您的参与，也不影响已接入防护的业务。</td>
</tr>
<tr>
<td>若您同时接入非中国大陆和中国大陆 CLB 实例的 Web 业务，请您配合购买非中国大陆实例支持对应地区的 CLB 实例的 Web 业务接入防护。购买后，系统自动将您此前接入的非中国大陆 CLB 实例的 Web 业务升级到新的 WAF 实例中。</td>
</tr>
</tbody></table>
