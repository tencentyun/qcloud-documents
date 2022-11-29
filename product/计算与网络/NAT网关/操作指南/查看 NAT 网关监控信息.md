创建 NAT 网关后，您可以通过控制台查看监控信息并导出数据。

## 操作步骤
1. 登录 [NAT 网关控制台](https://console.cloud.tencent.com/vpc/nat?fromNav)。
2. 在 NAT 网关列表中，单击需要查看的网关 ID 进入详情页。
3. 单击**监控**选项卡查看监控信息。
![](https://qcloudimg.tencent-cloud.cn/raw/0bde1e73ba44dc40765c49a1cb8809da.png)
 - 单击<img src="https://qcloudimg.tencent-cloud.cn/raw/0839851c629c3b93887eb48e5cfb73c9.png" width="3%">支持**数据导出**或**图片导出**，可将数据保存到本地。
 - 单击<img src="https://qcloudimg.tencent-cloud.cn/raw/facd10f7f25f44e95210e90bb98e4411.png" width="3%">可全屏展示图表。
 - 单击<img src="https://qcloudimg.tencent-cloud.cn/raw/4cd0f1da1c7407cf6652fd010960ef1d.png" width="3%">可配置告警。
具体监控指标如下表所示：
<table>
<tr>
<th>指标名称</th>
<th>指标含义</th>
</tr>
<tr>
<td>外网出带宽(Mbps)</td>
<td>出流量速率，即 NAT 网关每秒发送到公网的流量</td>
</tr>
<tr>
<td>外网入带宽(Mbps)</td>
<td>入流量速率，即公网每秒发送到 NAT 网关的流量</td>
</tr>
<tr>
<td>外网出包量(pps)</td>
<td>NAT 网关每秒发送到公网的数据包数量</td>
</tr>
<tr>
<td>外网入包量(pps)</td>
<td>公网每秒发送到 NAT 网关的数据包数量</td>
</tr>
<tr>
<td>丢包量(个)</td>
<td>超过 NAT 网关最大并发连接数时产生丢包的包量</td>
</tr>
<tr>
<td>并发连接数(个)</td>
<td>NAT 网关可同时容纳的连接数量</td>
</tr>
<tr>
<td>并发连接数使用率(%)</td>
<td>并发连接数使用率</td>
</tr>
<tr>
<td>外网出带宽使用率(%)</td>
<td>出带宽使用率</td>
</tr>
<tr>
<td>外网入带宽使用率(%)</td>
<td>入带宽使用率</td>
</tr>
<tr>
<td> 新建连接数（适用于标准型 NAT 网关）(个/秒)</td>
<td>NAT 网关每秒新建的连接个数</td>
</tr>
<tr>
<td>新建连接数使用率（适用于标准型 NAT 网关）(%)</td>
<td>NAT 网关实际新建连接数与 NAT 网关能够提供的最大新建连接数规格的占比，即新建连接数使用率</td>
</tr>
<tr>
<td>活跃连接数（适用于标准型 NAT 网关）(个)</td>
<td>NAT 网关在统计粒度内，已建立的活跃并发连接数</td>
</tr>
<tr>
<td>非活跃连接数（适用于标准型 NAT 网关）(个)</td>
<td>NAT 网关在统计粒度内，已建立的非活跃并发连接数</td>
</tr>
</table>
<dx-alert infotype="explain" title="">
标准型 NAT 网关正在灰度测试中，如需使用，请提交 [内测申请](https://cloud.tencent.com/apply/p/ojxjirnd5yi)。
</dx-alert>
4. （可选）您也可以在 NAT 网关列表中，单击需要查看的 NAT 网关条目中的监控按钮，即可查看监控信息。
![](https://main.qcloudimg.com/raw/2ae365dd7ca46296ec5d1464d142bd51.png)
