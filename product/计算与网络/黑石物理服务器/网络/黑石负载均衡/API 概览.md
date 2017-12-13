## API 概览

可以使用 API 操作来设置和管理 LB：

1.负载均衡实例

<table>
 <tr>
  <th  width="350">接口功能描述</th>
	<th  width="350">Action ID</th>
 </tr>
 <tr>
  <td>创建负载均衡</td>
	<td>CreateBmLoadBalancer</td>
 </tr>
 <tr>
  <td>获取负载均衡实例列表</td>
	<td>DescribeBmLoadBalancers</td>
 </tr>
 <tr>
  <td>修改负载均衡属性信息</td>
	<td>ModifyBmLoadBalancerAttributes</td>
 </tr>
 <tr>
  <td>删除负载均衡</td>
	<td>DeleteBmLoadBalancers</td>
 </tr>
 <tr>
  <td>查询负载均衡价格</td>
	<td>InquiryBmLBPrice</td>
 </tr>

</table>

2.四层监听器

<table >
 <tr>
  <th width="350">接口功能描述</th>
	<th  width="350">Action ID</th>
 </tr>
 <tr>
  <td>创建负载均衡四层监听器</td>
	<td>CreateBmListeners</td>
 </tr>
 <tr>
  <td>获取负载均衡四层监听器</td>
	<td>DescribeBmListeners</td>
 </tr>
 <tr>
  <td>获取负载均衡四层监听器详细信息</td>
	<td>DescribeBmListenerInfo</td>
 </tr>
 <tr>
  <td>修改负载均衡四层监听器</td>
	<td>ModifyBmListener</td>
 </tr>
 <tr>
  <td>绑定物理服务器到四层监听器</td>
	<td>BindBmL4ListenerRs</td>
 </tr>
 <tr>
  <td>绑定虚机IP到负载均衡四层监听器</td>
	<td>BindBmL4ListenerVmIp</td>
 </tr>
 <tr>
  <td>获取负载均衡四层监听器绑定的主机列表</td>
	<td>DescribeBmL4ListenerBackends</td>
 </tr>
 <tr>
  <td>修改负载均衡四层监听器后端实例权重</td>
	<td>ModifyBmL4ListenerBackendWeight</td>
 </tr>
 <tr>
  <td>修改负载均衡四层监听器后端实例端口</td>
	<td>ModifyBmL4ListenerBackendPort</td>
 </tr>
 <tr>
  <td>解绑负载均衡四层监听器物理服务器</td>
	<td>UnbindBmL4ListenerRs</td>
 </tr>
 <tr>
  <td>解绑负载均衡四层监听器虚机IP</td>
	<td>UnbindBmL4ListenerVmIp</td>
 </tr>
 <tr>
  <td>删除负载均衡四层监听器</td>
	<td>DeleteBmListeners</td>
 </tr>
 <tr>
  <td>修改负载均衡四层监听器后端探测端口</td>
	<td>ModifyBmL4ListenerBackendProbePort</td>
 </tr>
</table>

3.七层监听器

<table>
 <tr>
  <th  width="350">接口功能描述</th>
	<th  width="350">Action ID</th>
 </tr>
 <tr>
  <td >创建负载均衡七层监听器</td>
	<td>CreateBmForwardListeners</td>
 </tr>
 <tr>
  <td>获取负载均衡七层监听器</td>
	<td>DescribeBmForwardListeners</td>
 </tr>
 <tr>
  <td>获取负载均衡七层监听器详细信息</td>
	<td>DescribeBmForwardListenerInfo</td>
 </tr>
 <tr>
  <td>修改负载均衡七层监听器</td>
	<td>ModifyBmForwardListener</td>
 </tr>
 <tr>
  <td>创建负载均衡七层转发规则</td>
	<td>CreateBmForwardRules</td>
 </tr>
 <tr>
  <td>获取负载均衡七层转发规则</td>
	<td>DescribeBmForwardRules</td>
 </tr>
 <tr>
  <td>修改负载均衡七层转发路径</td>
	<td>ModifyBmForwardLocation</td>
 </tr>
 <tr>
  <td>绑定物理服务器到七层转发路径</td>
	<td>BindBmLocationInstances</td>
 </tr>
 <tr>
  <td>绑定虚机IP到负载均衡七层转发路径</td>
	<td>BindBmL7LocationVmIp</td>
 </tr>
 <tr>
  <td>获取负载均衡七层转发路径绑定的主机列表</td>
	<td>DescribeBmLocationBackends</td>
 </tr>
 <tr>
  <td>修改负载均衡七层转发路径后端实例权重</td>
	<td>ModifyBmLocationBackendWeight</td>
 </tr>
 <tr>
  <td>修改负载均衡七层转发路径后端实例端口</td>
	<td>ModifyBmLocationBackendPort</td>
 </tr>
 <tr>
  <td>解绑物理服务器到七层转发路径</td>
	<td>UnbindBmLocationInstances</td>
 </tr>
 <tr>
  <td>解绑负载均衡七层转发路径虚机IP</td>
	<td>UnbindBmL7LocationVmIp</td>
 </tr>
 <tr>
  <td>删除负载均衡七层转发规则</td>
	<td>DeleteBmForwardRules</td>
 </tr>
 <tr>
  <td>删除负载均衡七层转发域名</td>
	<td>DeleteBmForwardDomains</td>
 </tr>
</table>

4.HTTPS证书

<table>
 <tr>
  <th  width="350">接口功能描述</th>
	<th  width="350">Action ID</th>
 </tr>
 <tr>
  <td width="350">创建负载均衡证书</td>
	<td width="350">UploadBmCert</td>
 </tr>
 <tr>
  <td width="350">获取负载均衡证书详情</td>
	<td width="350">GetBmCertDetail</td>
 </tr>
 <tr>
  <td width="350">更新负载均衡证书</td>
	<td width="350">ReplaceBmCert</td>
 </tr>
</table>

5.通用接口

<table>
 <tr>
  <th  width="350">接口功能描述</th>
	<th  width="350">Action ID</th>
 </tr>
 <tr>
  <td width="350">查询负载均衡异步任务状态</td>
	<td width="350">DescribeBmLoadBalancersTaskResult</td>
 </tr>
 <tr>
  <td width="350">获取主机的负载均衡的绑定详情</td>
	<td width="350">DescribeBmBindInfo</td>
 </tr>
 <tr>
  <td width="350">获取负载均衡端口信息</td>
	<td width="350">DescribeBmVportInfo</td>
 </tr>
</table>


