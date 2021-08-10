
### 如何查看 MySQL 实例存储空间使用情况？
登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain)，在左侧导航选择【诊断优化】，在上方选择对应数据库，然后选择【空间分析】页。 
在空间分析页可查看近一周的日均增长量对比、剩余磁盘空间、预计可用天数，以及近一周的磁盘空间趋势表。 同时也可以查看实例中数据库下各表的占用空间详情和碎片情况。
![](https://main.qcloudimg.com/raw/cdbbe7b6f32b829a87f9025d4acc05cd.png)

### 如何分析 MySQL 全量 SQL 执行轨迹？
登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain)，在左侧导航选择【诊断优化】，在上方选择对应数据库，然后选择【审计日志分析】页。
1. 单击【创建分析任务】，选择时间段，单击【确定】。
2. 在任务列表单击【查看 SQL 分析】，进入 SQL 分析页。
![](https://main.qcloudimg.com/raw/60c636949f6bcbafe726256d2a08db5f.png)
3. 在 SQL 分析页，可选择 SQL Type、Host、User 等维度的视图，并可选择时间段拉伸视图来查看具体时间点的数据。
![](https://main.qcloudimg.com/raw/e4a3cf78a8c58e6f5442362c60d3ccbb.png)
4. 单击某行 SQL 模板，在右侧会弹出 SQL 语句的详情。
 - 在分析页，可查看和复制具体 SQL 语句，根据给出的优化建议或说明来优化 SQL 语句。
 - 在统计页，可查看该类 SQL 在 Host、User、SQL Code 维度的统计分析和执行时间轨迹。
 
### MySQL 实例故障或异常时，如何自助诊断优化？
1. 登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain)，在左侧导航选择【诊断优化】，在上方选择对应数据库，然后选择【异常诊断】页。
2. “诊断提示”栏展示诊断事件历史记录的概要信息，包括等级、开始时间、诊断项、持续时长。DBbrain 会定期对实例进行健康巡检。
![](https://main.qcloudimg.com/raw/6616a8f42f7da2808507d464f7d86f75.png)
3. 单击【查看详情】或“诊断提示”栏的诊断项可进入诊断详情页，在视图单击诊断事件，在下方会显示该事件的详情，包括事件概要、现象描述、智能分析以及专家建议，根据专家建议进行优化，即可解决数据库异常，提升实例性能。
 ![](https://main.qcloudimg.com/raw/bd74997165d561b84f4366a902e70d43.png)

### 如何定期获取 MySQL 健康报告？
登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain)，在左侧导航选择【诊断优化】，在上方选择对应数据库，然后选择【健康报告】页，可查看选择时间段的健康得分趋势以及问题概要。 
- 设置报告时间范围，然后单击【创建健康报告】，任务完成后可以查看或下载该时段的健康报告。  
- 单击【定期生成设置】，可配置自动生成健康报告的时间周期。 
 ![](https://main.qcloudimg.com/raw/d3842c7a041d9eb4d07900f953d2abc4.png)

### 如何查看和优化 MySQL 慢日志？
1. 登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain)，在左侧导航选择【诊断优化】，在上方选择对应数据库，然后选择【慢 SQL 分析】页，“SQL 统计”栏展示实例的慢查询数和 CPU 使用率。
2. 单击或拉选 SQL 统计图表的慢查询，下方会显示聚合 SQL 模板以及执行信息，各列数据均支持正序或逆序排序。右侧的耗时分布中会展示所选时间段内的 SQL 总体耗时分布情况。
 ![](https://main.qcloudimg.com/raw/66442e7012ad2baddc8efd8a68a1eae5.png)
3. 单击某条聚合的 SQL 模板行，右侧边会弹出 SQL 的优化建议和统计信息，可根据优化建议改写 SQL 或者增加适当索引，即可提升 SQL 执行效率，提高数据库性能。
 ![](https://main.qcloudimg.com/raw/0c5429de192d731e378bbfb020fdc928.png)
