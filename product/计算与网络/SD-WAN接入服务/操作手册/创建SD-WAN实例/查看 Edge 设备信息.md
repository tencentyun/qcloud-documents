购买 Edge 设备后，控制台将自动创建 SD-WAN 接入服务实例，您可以通过该实例查看 SD-WAN 接入服务的基本信息。

## 查看列表信息
1. 登录 [SD-WAN 接入服务控制台](https://console.cloud.tencent.com/sas/edge)。
2. 在实例列表中查看目标实例信息。
	 ![](https://main.qcloudimg.com/raw/f7f65dad0017451d59197a9224ebe431.png)
<table>
<thead>
<tr>
<th>字段</th>
<th>含义</th>
</tr>
</thead>
<tbody><tr>
<td>ID/名称</td>
<td>当前实例 ID 和名称，单击铅笔图标可修改当前实例名称，不超过48个字符。</td>
</tr>
<tr>
<td>监控</td>
<td>设备状态为“运行中”、“离线”的实例可以查看监控信息，具体操作请参见 <a href="https://cloud.tencent.com/document/product/1277/47264">查看监控信息</a>。</td>
</tr>
<tr>
<td>设备状态</td>
<td>当前智能接入网关的状态。<ul><li>发货中：申请 Edge 设备后，2天即可发货，预计7天内到达。</li><li>发货失败：因发货超时或收货信息有误等原因导致。</li><li>物流中：Edge 设备已发货，请等待签收。</li><li>物流失败：因无人签收等原因导致发货失败。</li><li>待激活：Edge 设备为待激活情况，您可以插电开始激活。</li><li>激活失败：请  <a href="https://console.cloud.tencent.com/workorder/category?level1_id=517&level2_id=727&source=0&data_title=%E5%85%B6%E4%BB%96%E8%85%BE%E8%AE%AF%E4%BA%91%E4%BA%A7%E5%93%81&level3_id=729&radio_title=%E6%95%85%E9%9A%9C%E6%8E%92%E6%9F%A5&queue=3232&scene_code=17784&step=2">提交工单</a> 联系腾讯云运维人员进行排查。</li><li>运行中：Edge 设备正常运行。</li><li>升级中：Edge 设备进行升级操作。 </li><li>离线：Edge 设备与中心控制器失联。</li><li>到期隔离：Edge 设备到期后，进入到期隔离状态，7天后释放。</li></ul></td>
</tr>
<tr>
<td>带宽</td>
<td>申请 Edge 设备的带宽，运行中的实例可以提升带宽，具体操作请参见 <a href="https://cloud.tencent.com/document/product/1277/47259">提升带宽</a>。 </td>
</tr>
<tr>
<td>关联云联网</td>
<td>关联的云联网实例，运行中的实例才可以关联云联网，具体操作请参见 <a href="https://cloud.tencent.com/document/product/1277/47262">关联云联网</a>。</td>
</tr>
<tr>
<td>LAN 网段</td>
<td>Edge 设备的 LAN 接口网段。</td>
</tr>
<tr>
<td>链路状态</td>
<td><ul><li>主链路、备用链路及 4G 逃生链路任意一条可用。</li><li>主链路、备用链路及 4G 逃生链路均不可用。</li></ul></td>
</tr>
<tr>
<td>计费时间</td>
<td>当前实例到期时间。</td>
</tr>
</tbody></table>

   

## 查看设备概况
1. 在 [SD-WAN 接入服务实例列表](https://console.cloud.tencent.com/sas/edge) 中，单击目标实例 ID。
2. 在“设备概况”页面，可查看设备基本信息。
   ![](https://main.qcloudimg.com/raw/3ba633084f7392a3ebcd728636fd0d4b.png) 
<table>
<thead>
<tr>
<th>字段</th>
<th>含义</th>
</tr>
</thead>
<tbody>
</tr>
<tr>
<td>带宽</td>
<td>Edge 设备的带宽。</td>
</tr>
<tr>
<td>到期时间</td>
<td>Edge 设备到期时间。</td>
</tr>
<tr>
<td>防火墙</td>
<td>与 SD-WAN 接入服务绑定的防火墙，可单击<b>更换</b>，变更防火墙。</td>
</tr>
<tr>
<td>硬件型号</td>
<td>Edge 设备的型号。</td>
</tr>
<tr>
<td>状态</td>
<td>Edge 设备当前状态。</td>
</tr>
<tr>
<td>S/N 码</td>
<td>与 SD-WAN 接入服务绑定的 Edge 设备，可单击<b>更换</b>，进行变更。</td>
</tr>
</tbody></table>
