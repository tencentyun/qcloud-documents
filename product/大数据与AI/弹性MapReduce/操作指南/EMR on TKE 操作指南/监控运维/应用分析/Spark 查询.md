## 操作场景
提供快速查看 Spark 作业的提交用户、状态、持续时间等多项明细指标，并支持作业级历史任务对比、作业洞察、任务执行信息等。
## 操作步骤
1. 登录 [EMR 控制台](https://console.cloud.tencent.com/emr)，在集群列表中单击对应的**集群 ID/名称**进入集群详情页。
2. 在集群详情页选择**作业管理 > Spark**，即可查看查询管理，查询相关 Spark 作业信息、任务信息查看、应用执行结果洞察及应用监控对比等。
作业级别提供用户、应用名、队列名、作业类型、持续时间及相关吞吐资源等多维信息筛查。
![](https://qcloudimg.tencent-cloud.cn/raw/c1abd70d6e2a6a194f1f3967584940c5.png)
>! 
>- 其中 Spark 类型应用的任务信息、应用洞察、应用对比新功能需 check Spark History 版本是否符合，check 命令如下：`curl "http://localhost:10000/api/v1/applications" | json_pp`，返回数据为非正常的 json 格式数据则 SparkHistory 版本不符合，可 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开启相关功能。
>- 作业查询将每30s采集一次 ResourceManager 数据，采集操作对集群业务影响微小可忽略。
>
3. 在作业列表中单击**更多 > 应用洞察**，查看应用的详细洞察项及相关的洞察规则、结果、建议。
![](https://qcloudimg.tencent-cloud.cn/raw/9d8ca32b78310c34b0261ca0348c2c18.png)
4. 在作业列表中单击**更多 > 应用对比**，可按需选择当前应用与同类型应用的业务指标对比信息。
>! 
>- 应用最终状态为 SUCCEEDED 的应用支持应用对比。
>- 默认页面按照同类型相同应用名已做过滤，筛选支持实时查询后台。
>
5. 在作业列表中单击**更多 > 任务信息**，查看作业的任务列表及任务的运行日志。
![](https://qcloudimg.tencent-cloud.cn/raw/91a9c713c9558234d6c225c16fce06ff.png)
