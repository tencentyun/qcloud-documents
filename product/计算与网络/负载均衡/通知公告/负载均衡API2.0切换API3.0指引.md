负载均衡 API 已全面升级至3.0版本，基于2.0版本接口访问时延较高和使用复杂的考虑，原负载均衡 API2.0 接口服务将不再提供技术支持，并于北京时间2022年11月30日起下线。如果您的业务还在使用云监控 API2.0 相关接口，建议尽快将服务升级至 API3.0 接口，以免对您的业务造成影响。

- 【推荐】当前负载均衡 API2.0 的接口为传统型负载均衡使用的接口，您可选择将“传统型负载均衡”升级为“负载均衡”类型，升级后资费不变，VIP 不变，可覆盖传统型负载均衡的所有功能，且能提供更多功能和更好的用户体验。升级后支持直接调用 API3.0 接口。传统型负载均衡升级详情请参见 [传统型负载均衡升级公告](https://cloud.tencent.com/document/product/214/75481)。
- 若您暂未从“传统型负载均衡”升级为“负载均衡”类型，则可选择将 API2.0 接口升级为 API3.0。您可参照下方的 [API2.0 切换3.0接口列表](#APIlist) 找到需升级的新接口，完成升级。


## [API2.0 切换3.0接口列表](id:APIlist)

### 实例相关接口
<table>
<thead>
<tr>
<th width="35%">API2.0 接口</th>
<th width="35%">API3.0 接口</th>
<th>备注</th>
</tr>
</thead>
<tbody><tr>
<td ><a href="https://cloud.tencent.com/document/product/214/1254" target="_blank">CreateLoadBalancer</a></br>（购买负载均衡实例）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30692" target="_blank">CreateLoadBalancer</a></br>（购买负载均衡实例）</td>
<td>-</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/1328" target="_blank">InquiryLBPriceAll</a></br>（查询负载均衡实例价格）</td>
<td>/</td>
<td>原有 API 对应的价格查询功能已不再推荐使用。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/1261" target="_blank">DescribeLoadBalancers</a></br>（查询负载均衡实例列表）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30685" target="_blank">DescribeLoadBalancers</a></br>（查询负载均衡实例列表）</td>
<td>-</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/214/1257" target="_blank">DeleteLoadBalancers</a></br>（删除负载均衡实例）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30689" target="_blank">DeleteLoadBalancers</a></br>（删除负载均衡实例）</td>
<td>-</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/37704" target="_blank">CloneLB</a></br>（克隆负载均衡）</td>
<td><a href="https://cloud.tencent.com/document/product/214/64874" target="_blank">CloneLoadBalancer</a></br>（克隆负载均衡实例）</td>
<td>-</td>
</tr><tr>
<td><a href="https://cloud.tencent.com/document/product/214/1263" target="_blank">ModifyLoadBalancerAttributes</a></br>（修改负载均衡属性信息）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30680" target="_blank">ModifyLoadBalancerAttributes</a></br>（修改负载均衡实例的属性）</td>
<td>-</td>
</tr>
</tbody></table>

### 监听器相关接口

<table>
<thead>
<tr>
<th width="35%">API2.0 接口</th>
<th width="35%">API3.0 接口</th>
<th>备注</th>
</tr>
</thead>
<tbody><tr>
<td><a href="https://cloud.tencent.com/document/product/214/1255" target="_blank">CreateLoadBalancerListeners</a></br>（创建负载均衡监听器）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30693" target="_blank">CreateListener</a></br>（创建负载均衡监听器）</td>
<td>-</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/1260" target="_blank">DescribeLoadBalancerListeners</a></br>（获取负载均衡监听器列表）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30686" target="_blank">DescribeListeners</a></br>（查询负载均衡的监听器列表）</td>
<td>-</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/1256" target="_blank">DeleteLoadBalancerListeners</a></br>（删除负载均衡监听器）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30690" target="_blank">DeleteListener</a></br>（删除负载均衡监听器）</td>
<td>-</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/3601" target="_blank">ModifyLoadBalancerListener</a></br>（修改负载均衡监听器属性）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30681" target="_blank">ModifyLoadBalancerListener</a></br>（修改负载均衡监听器属性）</td>
<td>-</td>
</tr>
</tbody></table>

### 后端服务器相关接口
<table>
<thead>
<tr>
<th width="35%">API2.0 接口</th>
<th width="35%">API3.0 接口</th>
<th>备注</th>
</tr>
</thead>
<tbody><tr>
<td><a href="https://cloud.tencent.com/document/api/214/1265" target="_blank">RegisterInstancesWithLoadBalancer</a></br>（绑定后端服务器到负载均衡）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30676" target="_blank">RegisterTargets</a></br>（绑定后端机器到监听器上）</td>
<td>-</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/214/1259" target="_blank">DescribeLoadBalancerBackends</a></br>（获取负载均衡绑定的后端服务器列表）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30684" target="_blank">DescribeTargets</a></br>（查询负载均衡绑定的后端服务列表）</td>
<td>-</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/214/1264" target="_blank">ModifyLoadBalancerBackends</a></br>（修改负载均衡后端服务器权重）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30677" target="_blank">ModifyTargetWeight</a></br>（修改监听器绑定的后端机器的转发权重）</td>
<td>-</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/214/1258" target="_blank">DeregisterInstancesFromLoadBalancer</a></br>（解绑后端服务器）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30687" target="_blank">DeregisterTargets</a></br>（从负载均衡监听器上解绑后端服务）</td>
<td>-</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/1326" target="_blank">DescribeLBHealthStatus</a></br>（查询负载均衡健康检查状态）</td>
<td><a href="https://cloud.tencent.com/document/product/214/34898" target="_blank">DescribeTargetHealth</a></br>（获取负载均衡后端服务的健康检查状态）</td>
<td>-</td>
</tr>
</tbody></table>

### 其他相关接口
<table>
<thead>
<tr>
<th width="35%">API2.0 接口</th>
<th width="35%">API3.0 接口</th>
<th>备注</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/4007" target="_blank">DescribeLoadBalancersTaskResult</a></br>（查询负载均衡异步接口的执行结果）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30683" target="_blank">DescribeTaskStatus</a></br>（查询异步任务状态）</td>
<td >-</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/8801" target="_blank">GetMonitorData</a></br>（负载均衡监控接口）</td>
<td><a href="https://cloud.tencent.com/document/product/214/8801" target="_blank">GetMonitorData</a></br>（拉取指标监控数据）</td>
<td>此接口为云监控 API 接口，升级至 API3.0 接口的方式请参见 <a href="https://cloud.tencent.com/document/product/248/81039#getmonitordata">接口迁移说明</a>。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/6045" target="_blank">ReplaceCert</a></br>（更换 HTTPS 类型负载均衡证书）</td>
<td><a href="https://cloud.tencent.com/document/product/214/36907" target="_blank">ReplaceCertForLoadBalancers</a></br>（替换负载均衡实例所关联的证书）</td>
<td>-</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/6046" target="_blank">GetCertListWithLoadBalancer</a></br>（查询证书关联的负载均衡监听器）</td>
<td><a href="https://cloud.tencent.com/document/product/214/40953" target="_blank">DescribeLoadBalancerListByCertId</a></br>（根据证书ID查询负载均衡）</td>
<td>-</td>
</tr>
</tbody></table>
