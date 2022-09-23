## 功能介绍
快速查看 Yarn 作业的提交队列、状态、持续时间等多项明细指标；同时提供统计视图，用于查看队列、用户、作业类型三个维度的指标统计。

## 操作步骤
1. 登录 [EMR 控制台](https://console.cloud.tencent.com/emr)，在集群列表中单击对应的集群 **ID/名称**进入集群详情页。
2. 在集群详情页中单击**集群服务**，然后选择 YARN 组件右上角**操作 > 作业查询**，即可查看作业视图统计，进行相关作业查询、任务信息查看、应用执行结果洞察及应用监控对比等。
![](https://qcloudimg.tencent-cloud.cn/raw/9d260d68607efdfa62b905d57a2d746d.png)
![](https://qcloudimg.tencent-cloud.cn/raw/4b12ef44ccdb6859a78b140e2712ca3e.png)
>! 其中 Spark 类型应用的任务信息、应用洞察、应用对比新功能需 check Spark History 版本是否符合，check 命令如下：`curl "http://localhost:10000/api/v1/applications" | json_pp`，返回数据为非正常的 json 格式数据则 SparkHistory 版本不符合，可通过 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开启相关功能。

3. 在作业列表中单击**更多 > 应用洞察**，查看应用的详细洞察项及相关的洞察规则、结果、建议。
![](https://qcloudimg.tencent-cloud.cn/raw/552c830d64b3269377084084897559d0.png)
4. 在作业列表中单击**更多 > 应用对比**，可需选择当前应用与同类型应用的业务指标对比信息。
![](https://qcloudimg.tencent-cloud.cn/raw/42ab417ba68b76b1dff4fc3fe9bf6ab9.png)
>!  
>- 仅 MR、Spark、Tez 类型且最终状态为 SUCCEEDED 的应用支持应用对比。
>- 默认页面按照同类型相同应用名已做过滤，应用对比的选择筛选范围仅限于同类型应用，筛选支持实时查询后台。

5. 在作业列表中单击**更多 > 任务信息**，查看作业的任务列表、Hosts 对比及任务的运行日志。
![](https://qcloudimg.tencent-cloud.cn/raw/2b9ae779edd5e9e1586bc67866d9dde7.png)
功能的覆盖范围如下：
<table>
<thead>
<tr>
<th>作业类型</th>
<th>任务信息</th>
<th>Hosts 对比</th>
<th>任务日志</th>
</tr>
</thead>
<tbody><tr>
<td>MR</td>
<td>支持</td>
<td>支持</td>
<td>支持</td>
</tr>
<tr>
<td>Spark</td>
<td>支持</td>
<td>不支持</td>
<td>支持</td>
</tr>
<tr>
<td>Tez</td>
<td>支持</td>
<td>支持</td>
<td>不支持</td>
</tr>
<tr>
<td>其他</td>
<td>不支持</td>
<td>不支持</td>
<td>不支持</td>
</tr>
</tbody></table>


