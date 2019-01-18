可以使用 API 操作来设置和管理 LB：

## 1.负载均衡实例

<table>
 <tr>
  <th  width="350">接口功能描述</th>
	<th  width="350">Action ID</th>
 </tr>
 <tr>
  <td>创建负载均衡</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9303">CreateBmLoadBalancer</a></td>
 </tr>
 <tr>
  <td>获取负载均衡实例列表</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9306">DescribeBmLoadBalancers</a></td>
 </tr>
 <tr>
  <td>修改负载均衡属性信息</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9302">ModifyBmLoadBalancerAttributes</a></td>
 </tr>
 <tr>
  <td>删除负载均衡</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9304">DeleteBmLoadBalancers</a></td>
 </tr>
 <tr>
  <td>查询负载均衡价格</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9305">InquiryBmLBPrice</a></td>
 </tr>

</table>

## 2.四层监听器

<table >
 <tr>
  <th width="350">接口功能描述</th>
	<th  width="350">Action ID</th>
 </tr>
 <tr>
  <td>创建负载均衡四层监听器</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9292">CreateBmListeners</a></td>
 </tr>
 <tr>
  <td>获取负载均衡四层监听器</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9296">DescribeBmListeners</a></td>
 </tr>
 <tr>
  <td>获取负载均衡四层监听器详细信息</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9298">DescribeBmListenerInfo</a></td>
 </tr>
 <tr>
  <td>修改负载均衡四层监听器</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9289">ModifyBmListener</a></td>
 </tr>
 <tr>
  <td>绑定物理服务器到四层监听器</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9294">BindBmL4ListenerRs</a></td>
 </tr>
 <tr>
  <td>绑定虚机IP到负载均衡四层监听器</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9295">BindBmL4ListenerVmIp</a></td>
 </tr>
 <tr>
  <td>获取负载均衡四层监听器绑定的主机列表</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9297">DescribeBmL4ListenerBackends</a></td>
 </tr>
 <tr>
  <td>修改负载均衡四层监听器后端实例权重</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9290">ModifyBmL4ListenerBackendWeight</a></td>
 </tr>
 <tr>
  <td>修改负载均衡四层监听器后端实例端口</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9291">ModifyBmL4ListenerBackendPort</a></td>
 </tr>
 <tr>
  <td>解绑负载均衡四层监听器物理服务器</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9299">UnbindBmL4ListenerRs</a></td>
 </tr>
 <tr>
  <td>解绑负载均衡四层监听器虚机IP</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9300">UnbindBmL4ListenerVmIp</a></td>
 </tr>
 <tr>
  <td>删除负载均衡四层监听器</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9293">DeleteBmListeners</a></td>
 </tr>
 <tr>
  <td>修改负载均衡四层监听器后端探测端口</td>
	<td><a href="https://cloud.tencent.com/document/product/386/12529">ModifyBmL4ListenerBackendProbePort</a></td>
 </tr>
</table>

## 3.七层监听器

<table>
 <tr>
  <th  width="350">接口功能描述</th>
	<th  width="350">Action ID</th>
 </tr>
 <tr>
  <td >创建负载均衡七层监听器</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9277">CreateBmForwardListeners</a></td>
 </tr>
 <tr>
  <td>获取负载均衡七层监听器</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9283">DescribeBmForwardListeners</a></td>
 </tr>
 <tr>
  <td>获取负载均衡七层监听器详细信息</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9284">DescribeBmForwardListenerInfo</a></td>
 </tr>
 <tr>
  <td>修改负载均衡七层监听器</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9273">ModifyBmForwardListener</a></td>
 </tr>
 <tr>
  <td>创建负载均衡七层转发规则</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9278">CreateBmForwardRules</a></td>
 </tr>
 <tr>
  <td>获取负载均衡七层转发规则</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9285">DescribeBmForwardRules</a></td>
 </tr>
 <tr>
  <td>修改负载均衡七层转发路径</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9274">ModifyBmForwardLocation</a></td>
 </tr>
 <tr>
  <td>绑定物理服务器到七层转发路径</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9281">BindBmLocationInstances</a></td>
 </tr>
 <tr>
  <td>绑定虚机IP到负载均衡七层转发路径</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9282">BindBmL7LocationVmIp</a></td>
 </tr>
 <tr>
  <td>获取负载均衡七层转发路径绑定的主机列表</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9286">DescribeBmLocationBackends</a></td>
 </tr>
 <tr>
  <td>修改负载均衡七层转发路径后端实例权重</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9275">ModifyBmLocationBackendWeight</a></td>
 </tr>
 <tr>
  <td>修改负载均衡七层转发路径后端实例端口</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9276">ModifyBmLocationBackendPort</a></td>
 </tr>
 <tr>
  <td>解绑物理服务器到七层转发路径</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9287">UnbindBmLocationInstances</a></td>
 </tr>
 <tr>
  <td>解绑负载均衡七层转发路径虚机IP</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9288">UnbindBmL7LocationVmIp</a></td>
 </tr>
 <tr>
  <td>删除负载均衡七层转发规则</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9280">DeleteBmForwardRules</a></td>
 </tr>
 <tr>
  <td>删除负载均衡七层转发域名</td>
	<td><a href="https://cloud.tencent.com/document/product/386/9279">DeleteBmForwardDomains</a></td>
 </tr>
</table>

## 4.HTTPS 证书

<table>
 <tr>
  <th  width="350">接口功能描述</th>
	<th  width="350">Action ID</th>
 </tr>
 <tr>
  <td width="350">创建负载均衡证书</td>
	<td width="350"><a href="https://cloud.tencent.com/document/product/386/9312">UploadBmCert</a></td>
 </tr>
 <tr>
  <td width="350">获取负载均衡证书详情</td>
	<td width="350"><a href="https://cloud.tencent.com/document/product/386/9314">GetBmCertDetail</a></td>
 </tr>
 <tr>
  <td width="350">更新负载均衡证书</td>
	<td width="350"><a href="https://cloud.tencent.com/document/product/386/9313">ReplaceBmCert</a></td>
 </tr>
</table>

## 5.通用接口

<table>
 <tr>
  <th  width="350">接口功能描述</th>
	<th  width="350">Action ID</th>
 </tr>
 <tr>
  <td width="350">查询负载均衡异步任务状态</td>
	<td width="350"><a href="https://cloud.tencent.com/document/product/386/9308">DescribeBmLoadBalancersTaskResult</a></td>
 </tr>
 <tr>
  <td width="350">获取主机的负载均衡的绑定详情</td>
	<td width="350"><a href="https://cloud.tencent.com/document/product/386/9309">DescribeBmBindInfo</a></td>
 </tr>
 <tr>
  <td width="350">获取负载均衡端口信息</td>
	<td width="350"><a href="https://cloud.tencent.com/document/product/386/9310">DescribeBmVportInfo</a></td>
 </tr>
</table>


