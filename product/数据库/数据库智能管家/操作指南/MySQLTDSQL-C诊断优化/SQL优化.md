## 功能描述

SQL 优化为用户提供一键优化 SQL 语句功能，并给出对应执行计划解析和优化建议。适用于业务优化慢 SQL、代码上线前审查、自检等场景。

SQL 优化不仅能够为用户提供的专家级别的 SQL 优化建议，同时也涵盖了数据库管理的众多功能，可以实现在线库表结构查看、SQL 执行和变更等，帮助用户完成 SQL 优化的全链路闭环。DBbrain 为用户打造了100%原始数据库终端的交互体验。

您可手动输入 SQL 语句，执行分析得到该语句的性能评估结果以及优化建议。

新增加可视化执行计划能力，帮您解析整个SQL语句执行过程和详情，更轻松掌握语句性能开销点。

>?SQL 优化目前支持云数据库 MySQL（不含单节点 - 基础型）、云原生数据库 TDSQL-C（TDSQL-C for MySQL）、自建数据库 MySQL。

## 优化器执行
1. 登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain/analysis)，在左侧导航选择**诊断优化**，在上方选择对应数据库，然后选择 **SQL 优化**页。
2. 在 SQL 优化页，可以查看数据库表信息、 SQL 详细信息和 SQL 执行信息。
   - 左侧栏展示数据库、表、字段、索引名，可按数据库名筛选数据库，单击表旁的**表结构**可查看表详情。
   - 右侧栏展示 SQL 的详细信息，也可直接筛选数据“库”、“表”、“类型”，支持“表格”和“DDL”两种展示模式。
![](https://main.qcloudimg.com/raw/d736607c8d152f84422ff414b2e0711a.png)
3. 在执行面板，输入或粘贴需要优化或执行的具体 SQL 语句，可以对其进行执行、查看执行计划、查看优化建议、格式化、撤销、重做、清空等操作。
   各操作均可支持快捷键控制，将鼠标悬浮在对应按钮上即可查看。
   ![](https://qcloudimg.tencent-cloud.cn/raw/0e20a75bd43b10b589e9bb091eab4d82.png)
 - 单击**执行**，可以执行输入的 SQL 语句，也可以查看执行结果和执行历史，同时支持清除执行结果的记录。
>?未登录状态只能查看 SQL 执行计划，如需要进行 SQL 优化等操作，请先登录需要执行操作的数据库。
>
![](https://qcloudimg.tencent-cloud.cn/raw/9bd8cb08c809f56f46c039acbae4783e.png)
 - 单击**执行历史**，可以查看 SQL 的执行历史，也可以切换查看当前会话历史和所有会话历史。
   ![](https://qcloudimg.tencent-cloud.cn/raw/e66b88f2a92c37ce058861412ad7100a.png)
 - 单击**执行计划**，可以查看 SQL 的执行计划详情和优化建议，具体请参考 [可视化执行计划](#kshjhxq)。
 - 单击**格式化**，可以对 SQL 语句进行格式化，格式化后的 SQL 语句如下：
    ![](https://qcloudimg.tencent-cloud.cn/raw/687d8e61748b11af9df52e1a22abe69f.png)
 - 单击**优化建议**图标，可以查看 SQL 语句的优化建议。
在优化对比中，可以查看 SQL 的执行计划、索引建议、重写建议、表结构及 SQL 代价，SQL 代价通过可视化图表清晰展示优化前后开销的变化。
   SQL 代价通过分析 SQL 相关库表的统计信息、OPTIMIZER_SWITCH 配置、及索引字段区分度进行估算，对优化后的 SQL 语句代价进行整体估计，使用可视化图表直观呈现 SQL 优化后降低的效果，您也可通过优化前后的执行计划比对进一步验证优化的效果。
    ![](https://main.qcloudimg.com/raw/b6e9431df017f5bbc877d0f5aa149fbc.png)
4. 在执行面板右侧，可查看监控详情、设置 SQL 查询条件、查看历史命令等。
![](https://qcloudimg.tencent-cloud.cn/raw/d41d17eaea471f1a67ec45c20a02f0cb.png)
 - 单击右侧的**监控详情**，可查看数据库的监控信息。
 - 单击右侧的**设置**，可以设置具体的查询条件，包括执行超时时间和最大返回行数。
 - 单击右侧的**我的命令**，可以查看我的收藏、系统运维 SQL 模板，支持常用运维 SQL 快捷执行，包含参数/指标、用户信息、information_schema、其他类的常用运维 SQL 快捷执行。
5. 查看表分析数据。
在左边选择对应的表，然后单击分析页签，右侧即可查看到表分析数据。
![](https://qcloudimg.tencent-cloud.cn/raw/6e545035130197aefbbe365fbe6ee189.png)

## [可视化执行计划](id:kshjhxq)
1. 登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain/analysis)，在左侧导航选择**诊断优化**，在上方选择对应数据库，然后选择 **SQL 优化**页。
2. 在 SQL 优化页，执行面板中，可以看到按钮操作栏。
3. 执行按钮右侧第一个按钮，即为**可视化执行计划**功能唤起按钮。
   - 在执行面板中输入或选中您要进行可视化分析的 SQL 语句。
   - 单击执行计划按钮即可呈现可视化执行计划效果。
   ![](https://qcloudimg.tencent-cloud.cn/raw/f77b52527354cb0736f35442e934146a.png)
   - 基表卡片上的小按钮，可以查看当前表的表结构。
   <img src="https://qcloudimg.tencent-cloud.cn/raw/169c2903cf4f1484111a7bddff4eb296.png" style="zoom: 45%;" />
   - 步骤卡的小按钮，可以获取当前步骤的 SQL 信息。
   <img src="https://qcloudimg.tencent-cloud.cn/raw/b5194b7aac9bc1f3e2d1aa495b461798.png" style="zoom:45%;" />
   - 单击每个卡片主体，可以获得该步骤的节点详情。不同的节点会有不同的信息。
   <img src="https://qcloudimg.tencent-cloud.cn/raw/2cae52cfa8ebe60440615f084a1c7f40.png" style="zoom:45%;" />
   - 根据语句执行情况，可以了解到哪些步骤产生了临时表或者文件排序。<br>
   <img src="https://qcloudimg.tencent-cloud.cn/raw/1b79bfbc4396a72c0585c1242b87a027.png" style="zoom:50%;" />
   - 索引类型，根据您所使用的索引性能的效率高低，这里会呈现不同的色阶。<br>
   <img src="https://qcloudimg.tencent-cloud.cn/raw/b5816ba38dc8f77beaf9b9829b2e5f47.png" style="zoom:50%;" />
   - 根据您语句的复杂程度，会出现不同的可视化矩阵效果，如果可视化图形区域内容过多，您可使用比例调节按钮，自由操控显示比例，或全屏。
   ![](https://qcloudimg.tencent-cloud.cn/raw/c070bb729e50e4a12414f2e17d7bdbd1.png)
   
   
