## 功能介绍
提供查看用户粒度提交量、Memory 量和 Vcore 消耗量等信息，快速查看 Yarn 作业的提交队列、状态、持续时间等多项明细指标，并支持作业级历史任务对比、作业洞察、任务执行信息等。
## 操作步骤
1. 登录 [EMR 控制台](https://console.cloud.tencent.com/emr)，在集群列表中单击对应的集群 **ID/名称**进入集群详情页。
2. 在集群详情页中单击**集群服务**，然后选择 YARN 组件右上角**操作 > 作业查询**，即可查看作业统计视图、资源消耗趋势，查询相关作业信息、任务信息查看、应用执行结果洞察及应用监控对比等。
	1. 用户粒度的提交量、Memory、VCore 的消耗量视图及分布，支持近期内的相关趋势查看。
![](https://qcloudimg.tencent-cloud.cn/raw/82fcd7ea4fa9bc56be3dcca098906d7b.png)
![](https://qcloudimg.tencent-cloud.cn/raw/e5f61921666da3c3c48a53a4629045e4.png)
	2. 作业级别提供用户、应用名、队列名、作业类型、持续时间及相关吞吐资源等多维信息筛查。
![](https://qcloudimg.tencent-cloud.cn/raw/638988895213d6c57369da1259d71904.png)
	3. 统计列表可按照指定的用户、队列等信息统计其资源消耗量，帮助统计资源开销情况辅助成本核查（接口同步支持）。
![](https://qcloudimg.tencent-cloud.cn/raw/8e9584f6c4ec3486fbdda41de2ba2108.png)
>! 
>- 其中 Spark 类型应用的任务信息、应用洞察、应用对比新功能需 check Spark History 版本是否符合，check 命令如下：`curl "http://localhost:10000/api/v1/applications" | json_pp`，返回数据为非正常的 json 格式数据则 SparkHistory 版本不符合，可通过 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开启相关功能。
>- 作业查询将每30s采集一次 ResourceManager 数据，采集操作对集群业务影响微小可忽略。

3. 在作业列表中单击**更多 > 应用洞察**，查看应用的详细洞察项及相关的洞察规则、结果、建议。
![](https://qcloudimg.tencent-cloud.cn/raw/552c830d64b3269377084084897559d0.png)
>! 
>- 为保障集群稳定运行，洞察功能采集策略满足以下任一规则将被降级忽略采集：
>  1. 运行时长小于10min的 App 将被降级忽略。
>  2. 采集时子任务大于3W的 App 将被降级忽略。
>  3. 延迟采集时间大于24h的 App 将被降级忽略。
>
>- 洞察采集降级策略的相关参数可通过 [提交工单](https://console.cloud.tencent.com/workorder/category) 评估修改。
<dx-alert infotype="alarm" title="风险说明">
Yarn 应用洞察会分别采集 Spark History、Job History、Timeline Server 相关应用数据进行分析，如若发现上述服务请求量持续突破负载瓶颈可 [提交工单](https://console.cloud.tencent.com/workorder/category) 关闭该功能。
</dx-alert>


4. 在作业列表中单击**更多 > 应用对比**，可以选择当前应用与同类型应用的业务指标对比信息。
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


