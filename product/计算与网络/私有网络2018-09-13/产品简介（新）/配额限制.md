### 私有网络与子网
<table>
<thead>
<tr>
<th width="70%">资源</th>
<th width="30%">限制（单位：个）</th>
</tr>
</thead>
<tbody><tr>
<td>每个账号每个地域内的私有网络个数</td>
<td align="center">20</td>
</tr>
<tr>
<td>每个私有网络内的子网数</td>
<td align="center">100</td>
</tr>
<tr>
<td>每个私有网络内辅助 CIDR 个数</td>
<td align="center">5</td>
</tr>
<tr>
<td>每个私有网络支持关联的基础网络云服务器个数</td>
<td align="center">100</td>
</tr>
</tbody></table>

### 路由表
<table>
<thead>
<tr>
<th width="70%">资源</th>
<th width="30%">限制（单位：个）</th>
</tr>
</thead>
<tbody><tr>
<td>每个私有网络内的路由表个数</td>
<td align="center">10</td>
</tr>
<tr>
<td>每个子网关联路由表个数</td>
<td align="center">1</td>
</tr>
<tr>
<td>每个路由表的路由策略数</td>
<td align="center">50</td>
</tr>
</tbody></table>

### 弹性网卡
<table>
<tr>
<th width="70%">资源</th>
<th width="30%">限制（单位：个）</th>
</tr>
<tr>
<td>每个私有网络内的辅助弹性网卡个数</td>
<td>1000</td>
</tr>
</table>

### HAVIP
<table >
<thead>
<tr>
<th width="70%">资源</th>
<th width="30%">限制（单位：个）</th>
</tr>
</thead>
<tbody><tr>
<td>每个私有网络的 HAVIP 默认配额数</td>
<td>10</td>
</tr>
</tbody></table>

### 安全组
<table>
<tr><th width="70%">功能描述</th><th width="30%">限制</th></tr>
<tr><td>安全组个数</td><td>50个/地域</td></tr>
<tr><td>安全组规则数</td><td>100条/入站方向，100条/出站方向</td></tr>
<tr><td>单个安全组关联的云服务器实例数</td><td>2000个</td></tr>
<tr><td>每个云服务器实例可以关联的安全组个数</td><td>5个</td></tr>
<tr><td>每个安全组可以引用的安全组ID的个数</td><td>10条</td></tr>
</table>

### 网络 ACL
<table >
<thead>
<tr>
<th width="70%">资源</th>
<th width="30%">限制</th>
</tr>
</thead>
<tbody><tr>
<td>每个私有网络内网络 ACL 数</td>
<td>50个</td>
</tr>
<tr>
<td>每个网络 ACL 中规则数</td>
<td>入站方向：20条<br>出站方向：20条</td>
</tr>
<tr>
<td>每个子网关联的网络 ACL 个数</td>
<td>1个</td>
</tr>
</tbody></table>

### 参数模板
<table>
<thead>
<tr>
<th width="70%">实例</th>
<th width="30%">限制（单位：个）</th>
</tr>
</thead>
<tbody><tr>
<td>IP 地址对象 (ipm)</td>
<td>每个租户上限1000</td>
</tr>
<tr>
<td>IP 地址组对象 (ipmg)</td>
<td>每个租户上限1000</td>
</tr>
<tr>
<td>协议端口对象 (ppm)</td>
<td>每个租户上限1000</td>
</tr>
<tr>
<td>协议端口组对象 (ppmg)</td>
<td>每个租户上限1000</td>
</tr>
<tr>
<td>IP 地址对象 (ipm) 内的 IP 地址成员</td>
<td>每个租户上限20</td>
</tr>
<tr>
<td>IP 地址组对象 (ipmg)内的 IP 地址对象成员 (ipm)</td>
<td>每个租户上限20</td>
</tr>
<tr>
<td>协议端组对象 (ppm)内的协议端口成员</td>
<td>每个租户上限20</td>
</tr>
<tr>
<td>协议端口组对象 (ppmg)内的协议端口对象成员 (ppm)</td>
<td>每个租户上限20</td>
</tr>
<tr>
<td>IP 地址对象 (ipm) 可被多少个 IP 地址组对象 (ipmg)引用</td>
<td>每个租户上限50</td>
</tr>
<tr>
<td>协议端口对象 (ppm)可被多少个协议端口组对象 (ppmg)引用</td>
<td>每个租户上限50</td>
</tr>
</tbody></table>

### 网络探测 
<table >
<thead>
<tr>
<th width="70%">资源</th>
<th width="30%">限制（单位：个）</th>
</tr>
</thead>
<tbody><tr>
<td>每个私有网络内可创建网络探测数</td>
<td>50</td>
</tr>
</tbody></table>
