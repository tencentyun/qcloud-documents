### 使用限制
- 每个私有网络的默认路由表无法删除。 
- 创建私有网络后，系统会在路由表中自动添加一条默认路由，表示此私有网络内所有资源均内网互通，该路由策略无法修改和删除。
<table><tbody>
<tr><th>目的端</th><th>下一跳类型</th><th>下一跳</th></tr>
<tr><td>Local</td><td>Local</td><td>Local</td></tr>
</tbody> </table>
- 不支持 BGP 和 OSPF 等动态路由协议。
- 不同类型路由支持ECMP的情况说明。
<table><tbody>
<tr><th>下一跳类型</th><th>是否支持同类型形成 ECMP</th><th>是否支持与其他类型形成 ECMP</th><th>ECMP 支持的最大数量</th</tr>
<tr><td>NAT 网关</td><td>是</td><td>是，支持与云服务器公网 IP 形成 ECMP</td><td>同类型最多8个，不同类型最多1个</td></tr>
<tr><td>对等连接（同地域）</td><td>否</td><td>否</td><td>N/A</td></tr>
<tr><td>对等连接（跨地域）</td><td>否</td><td>是，支持与云联网形成 ECMP</td><td>不同类型最多1个</td></tr>
<tr><td>专线网关</td><td>否</td><td>是，支持与云联网形成 ECMP</td><td>不同类型最多1个</td></tr>
<tr><td>高可用虚拟 IP</td><td>否</td><td>否</td><td>N/A</td></tr>
<tr><td>VPN 网关</td><td>否</td><td>否</td><td>N/A</td></tr>
<tr><td>云服务器公网 IP</td><td>否</td><td>是，支持与云服务器 / NAT 网关形成 ECMP</td><td>不同类型最多1个</td></tr>
<tr><td>云服务器</td><td>是</td><td>是，支持与云服务器公网IP形成 ECMP</td><td>同类型最多8个，不同类型最多1个</td></tr>
<tr><td>云联网</td><td>否</td><td>是，支持与专线网关 / 对等连接（跨地域）形成 ECMP</td><td>不同类型最多1个</td></tr>
</tbody> </table>

 >?
>+ ECMP（Equal Cost Multi-path，等价多路径），是指存在多条到达同一个目的地址的相同代价的路径。
>+ 当目的地址相同时，云服务器公网 IP 优先级比 NAT 网关高。
>+ 专线网关、云联网可以形成 ECMP，但是不会主动探测和自动收敛。
>+ 多条NAT网关路由可以形成 ECMP，但是不会主动探测和自动收敛。
>+ 多条云服务器路由可以形成 ECMP，但是不会主动探测和自动收敛。


### 配额限制
<table>
<tr>
<th>资源</th>
<th>限制（单位：个）</th>
</tr>
<tr>
<td>每个私有网络内的路由表个数</td>
<td>10</td>
</tr>
<tr>
<td>每个子网关联路由表个数</td>
<td>1</td>
</tr>
<tr>
<td>每个路由表的路由策略数</td>
<td>50</td>
</tr>
</table>
