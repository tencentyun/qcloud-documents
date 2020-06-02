SQL 优化为用户提供一键优化 SQL 语句功能，并给出对应执行计划解析和优化建议。适用于业务优化慢 SQL、代码上线前审查、自检等场景。优化器使用类命令行的文本输入页面，在为用户提供可视化平台组件服务的同时，尽量还原用户数据库的使用习惯。

您可手动输入 SQL 语句，执行分析得到该语句的性能评估结果以及优化建议。

>?SQL 优化目前仅支持云数据库 MySQL（不含基础版）。

通过如下视频，您可以了解 DBbrain SQL 优化功能的详细操作：
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/1915-22597?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

## 优化器执行
1. 登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain/analysis)，在左侧导航选择【诊断优化】，在上方选择【SQL 优化】页。
2. 在 SQL 优化页，查看数据库表信息和 SQL 详细信息。
 - 左侧栏展示数据库、表、字段、索引名，可按数据库名筛选数据库，单击表旁的【表结构】可查看表详情。
 - 右侧栏展示 SQL 的详细信息，也可直接筛选数据“库”、“表”、“类型”，支持“表格”和“DDL”两种展示模式。
![](https://main.qcloudimg.com/raw/d736607c8d152f84422ff414b2e0711a.png)
3. 在执行面板，输入或粘贴需要优化的具体 SQL 语句：
 - 单击【格式化】可优化格式。
![](https://main.qcloudimg.com/raw/ccc94a5f058115d16da387c4bf240d78.png)
格式化后 SQL 语句如下：
![](https://main.qcloudimg.com/raw/b5ef925a0e6a763895824f0e32e27614.png)
 - 单击【执行计划】，查看 SQL 预执行详情。
![](https://main.qcloudimg.com/raw/e593433f2b4c6a6fdd137dd736892f18.png)
 - 单击【优化建议】，可查看 SQL 的执行计划、索引建议、表结构及 SQL 代价，SQL 代价通过可视化图表清晰展示优化前后开销的变化。
SQL 代价通过分析 SQL 相关库表的统计信息、OPTIMIZER_SWITCH 配置、及索引字段区分度进行估算，对优化后的 SQL 语句待机进行整体代价估计，使用可视化图表直观呈现 SQL 优化后降低的效果，您也可通过优化前后的执行计划比对进一步验证优化的效果。
![](https://main.qcloudimg.com/raw/a6fb122ba26743cd8085515af23b3b03.png)


