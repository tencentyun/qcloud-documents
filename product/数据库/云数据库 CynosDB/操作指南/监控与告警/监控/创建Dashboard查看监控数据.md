本文为您介绍通过创建云监控 Dashboard 查看监控数据。

## 操作步骤
1. 登录 [云监控控制台](https://console.cloud.tencent.com/monitor/dashboard2/dashboards)。
2. 在左侧导航栏选择 **Dashboard > Dashboard 列表**。
3. 在 Dashboard 列表下单击**新建 Dashboard**。
![](https://qcloudimg.tencent-cloud.cn/raw/78bf8590eb1f1dc4308178fb5b7a937b.png)
4. 在弹出的窗口下选择**新建图表**，或选择**新建图表组**然后在图表组里**新建图表**。
![](https://qcloudimg.tencent-cloud.cn/raw/91c86db690707e0bb90ef03ccaf2b3e8.png)
5. 在图表编辑页面，配置如下参数，单击右上侧的**保存**。
<table>
<thead><tr><th>参数</th><th>说明</th></tr></thead>
<tbody><tr>
<td>选择产品</td><td>云产品监控</td></tr>
<tr>
<td>指标</td><td>选择云数据库 &gt; TDSQL-C &gt; MySQL，然后选择目标监控指标</td></tr>
<tr>
<td>筛选</td>
<td>选择筛选条件，过滤出符合条件的数据在图表上展示。增加多个筛选条件，图表仅展示符合所有条件的数据。筛选对象支持按实例、标签、模板变量进行筛选</td></tr>
<tr>
<td>group by</td><td>选择标签，进行分组聚合展示（选填项）</td></tr>
<tr>
<td>对比</td><td>可选择环比（昨天同时段）、同比（上周同时段）、自定义日期对比</td></tr>
<tr>
<td>别名</td><td>填写图例别名</td></tr>
<tr>
<td>开启排序功能</td><td>开启后可设置排序规则</td></tr>
<tr>
<td>排序规则</td>
<td>支持选择最大最小值、平均值、求和值，按照升序或降序排序</td></tr>
<tr>
<td>展示数量</td><td>设置指标展示的实例数量</td></tr>
</tbody></table>
6. 保存成功后，即可查看所创建指标的监控数据。
![](https://qcloudimg.tencent-cloud.cn/raw/648f30aaf59a3d43a9c95a4ce81f7d78.png)
>?此方法为创建单项监控指标，如需创建多项不同的监控指标，可重复此操作。

