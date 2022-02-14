NAT 网关提供流日志采集功能，通过对 NAT 网关流量的采集分析，并形成日志记录和图表分析，以便您能及时了解跨域通信情况，根据日志快速定位问题并解决，从而提升业务可用性及运维效率。
>?
>+ 目前网络流日志处于内测中，如有需要，请 [在线咨询](https://cloud.tencent.com/online-service?from=sales&source=PRESALE)。
>+ 流日志本身不会产生费用，数据存储在日志服务中，将按日志服务的 [标准收费](https://cloud.tencent.com/document/product/614/11323)。
>+ 流日志数据存储在日志服务 CLS 中，请确保已完成 [授权流日志访问 CLS 权限](https://cloud.tencent.com/document/product/682/63357)，否则无法在 CLS 上查询到日志数据。
>

## 操作步骤
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)，在左侧导航栏中单击**流日志** > **日志列表**。
2. 在“流日志”页面左上角选择地域，然后单击 **+新建**。
3. 在“新建流日志”对话框中配置如下参数。
<img src="https://qcloudimg.tencent-cloud.cn/raw/0cb8bf34661237feae5b330bc6b61e6f.png" width="80%">
<table>
<tr>
<th width="15%">字段</th>
<th>含义</th>
</tr>
<tr>
<td>名称</td>
<td>该流日志的名称。</td>
</tr>
<tr>
<td>采集范围</td>
<td>目前支持多个采集范围，此处选择“云联网跨地域流量”。</td>
</tr>
<tr>
<td>NAT 网关</td>
<td>NAT 网关的信息。</td>
</tr>
<tr>
<td>采集类型</td>
<td>指定流日志应捕获被安全组或 ACL 已拒绝流量、已接受流量、或所有流量。</td>
</tr>
<tr>
<td>日志集</td>
<td>指定流日志在日志服务内的存储集合。如已有日志集，请直接选择；如无，可保持“系统默认创建”，由系统帮您创建，或单击“<b>新建</b>”前往日志服务控制台自行创建。</td>
</tr>
<tr>
<td>日志主题</td>
<td>指定日志存储的最小维度，用于区别不同类型日志，例如 Accept 日志等。 如已有日志主题，请直接选择；如无，可保持“系统默认创建”，由系统帮您创建，或前往日志服务控制台自行创建。
<p>
<dx-alert infotype="explain" title="">
日志集和日志主题及索引的配置请参见 <a href="https://cloud.tencent.com/document/product/682/18967">创建日志集和日志主题</a>。
</dx-alert>
</td>
</tr>
<tr>
<td>标签键</td>
<td>单击<b>高级选项</b>，您可以新建（直接输入）或选择已有标签键，用于流日志查找和管理。</td>
</tr>
<tr>
<td>标签值</td>
<td>单击<b>高级选项</b>，您可以新建（直接输入）或选择已有标签值，也可以为空值。</td>
</tr>
</table>
4. 单击**确定**，即可完成流日志的创建。
   <dx-alert infotype="explain" title="">
首次创建流日志需要约6分钟后（1分钟捕获窗口，5分钟数据推送时间），方可在日志服务中查看流日志。
</dx-alert>
5. 等待约6分钟后，单击“**存储位置**”，或“**查看**”进入日志服务的“检索分析”界面，选择要查看日志的地域，时间段等，单击检索分析，查看日志记录。
    ![](https://qcloudimg.tencent-cloud.cn/raw/9af877c85bb0664c790e412cadea7a70.png)
	日志记录举例如下：
![](https://qcloudimg.tencent-cloud.cn/raw/5ea7f89601a0e8ab626ed5f066bf5fe7.png)
>?字段解释请参见[ 流日志记录](https://cloud.tencent.com/document/product/682/18933#.E6.B5.81.E6.97.A5.E5.BF.97.E8.AE.B0.E5.BD.95)，日志分析请参见[ 快速分析](https://cloud.tencent.com/document/product/614/59015)。