SQL 优化为用户提供一键优化 SQL 语句功能，并给出对应执行计划解析和优化建议。适用于业务优化慢SQL、代码上线前审查、自检等场景。优化器使用类命令行的文本输入页面，在为用户提供可视化平台组件服务的同时，尽量还原用户数据库的使用习惯。

您可手动输入 SQL 语句，执行分析得到该语句的性能评估结果以及优化建议。

>?SQL 优化目前仅支持云数据库 MySQL（不含基础版）。

通过如下视频，您可以了解 DBbrain SQL 优化功能的详细操作：
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/1915-22597?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

## 优化器执行
1. 登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain/analysis)，在左侧导航选择【诊断优化】，在上方选择【SQL 优化】页。
2. 选择数据库实例、数据库名（Database）。
3. 在输入框输入（或粘贴）需要优化的具体 SQL，可单击【格式化】美化格式。
4. 单击【执行分析】，查看 SQL 预执行详情和优化方案。
>?
>- 需确保输入的 SQL 语法正确，及对应数据库中存在相应 table。
>- 执行分析并不会真实执行 SQL，对数据库实际数据无影响。
>- 目前仅提供 select 语句的优化方案。
>
![](https://main.qcloudimg.com/raw/a482161bc3644fb497fbbb96146008a4.png)


## 优化建议
优化建议中会针对输入的 SQL，提供专业的优化建议，包括但不限于索引建议、SQL 改写建议等。用户可以根据 DBbrain 提供的优化建议，对存在性能问题的 SQL 进行优化。
![](https://main.qcloudimg.com/raw/1b2e5d01d115755f0dbac835bd94dc0b.png)
