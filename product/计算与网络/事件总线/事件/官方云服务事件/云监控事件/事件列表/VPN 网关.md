
由客户云上购买和使用的资源实例与产品产生的监控事件包括：


<style type="text/css">
.div-table-1 {width:100%;}
.div-table-1 td{white-space:pre-wrap; }
.div-td-el{word-wrap:break-word;word-break:break-all;}
.div-td-1{width:12%}
.div-td-2{width:12%}
.div-td-3{width:8%}
.div-td-4{width:12%}
.div-td-5{width:8%}
.div-td-6{width:20%}
.div-td-7{width:28%}
</style>




<table class="div-table-1">
<thead>
<tr>
<th class="div-td-1">事件<br>中文名</th>
<th class="div-td-2">事件<br>英文名</th>
<th class="div-td-3">事件<br>类型</th>
<th class="div-td-4">从属维度</th>
<th class="div-td-5">有无<br>恢复概念</th>
<th class="div-td-7">事件描述</th>
<th class="div-td-6">处理方法与建议</th>
</tr>
</thead>
<tbody>
<tr>
<td class="div-td-1">外网出带宽超限导致丢包</td>
<td class="div-td-2 div-td-el">PacketDroppedByQosWanOutBandwidth</td>
<td class="div-td-3">异常<br>事件</td>
<td class="div-td-4">VPN 网关实例维度</td>
<td class="div-td-5">有</td>
<td class="div-td-7">VPN 的外网出带宽超过限制导致丢包。带宽毛刺导致的丢包不会体现在带宽图表中，原因：带宽最细统计粒度为 10 级（10 秒内总流量/10 秒）。若常量带宽没有明显超出也可忽略</td>
<td class="div-td-6">提高外网带宽上限</td>
</tr>
<tr>
<td class="div-td-1">连接数超限导致丢包</td>
<td class="div-td-2 div-td-el">PacketDroppedByQosConnectionSession</td>
<td class="div-td-3">异常<br>事件</td>
<td class="div-td-4">VPN 网关实例维度</td>
<td class="div-td-5">有</td>
<td class="div-td-7">VPN 网关实例连接数过多导致丢包</td>
<td class="div-td-6"><a href="https://console.cloud.tencent.com/workorder/category">提交工单</a> 联系我们</td>
</tr>
<tr>
<td class="div-td-1">VPN 通道连接断开</td>
<td class="div-td-2 div-td-el">VpnconnDisconnected</td>
<td class="div-td-3">异常<br>事件</td>
<td class="div-td-4">VPN 网关实例维度</td>
<td class="div-td-5">有</td>
<td class="div-td-7">VPN 网关实例连接数过多导致丢包</td>
<td class="div-td-6"><a href="https://console.cloud.tencent.com/workorder/category">提交工单</a> 联系我们</td>
</tr>
</tbody>
</table>
