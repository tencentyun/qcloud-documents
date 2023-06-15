## 功能介绍
查看 T-1 天采集时间基于 HDFS 存储的总文件、总存储量、分布信息及近期趋势情况以及大文件、小文件的 top 目录列表。
- 可查看集群内基于 HDFS 存储的总文件数据量、总存储量日变化情况及近期的历史变化趋势图。
- 文件数量分布图和文件存储量分布图可以帮助了解空、小文件的占比及占用存储空间的情况。
- 提供采集时间点的大/小文件 Top1000文件目录信息，方便查询、下载。

## 操作步骤
1. 登录 [EMR 控制台](https://console.cloud.tencent.com/emr)，在集群列表中单击对应的**集群 ID/名称**进入集群详情页。
2. 在集群详情页中单击**集群服务**，然后选择 HDFS 组件右上角**操作 >文件存储分析**，提供基于存储在 **HDFS** 上截止上一次采集时间点的相关文件及目录信息。
3. 统计视图
<ol>
<li>可以查看 HDFS 存储的总文件数量、总存储量的日增量及日环比量。</li>
<li>参照空文件（=0），小文件（&lt;=2M）、其他（2M&lt;文件存储量&lt; 128M）及大文件（&gt;=128M）定义提供文件数量分布和文件存储量分布视图。<br></li>
</ol>
<img src="https://qcloudimg.tencent-cloud.cn/raw/f836dfb8c2449aa9981c2624e5aafca1.png" >
4.	通过视图直观查看各类文件数量和存储量的近期历史变化趋势。
![](https://qcloudimg.tencent-cloud.cn/raw/56292e2d6e50e118f7a35e778dad1a39.png)
5.	查询 DayT-1 采集时间点 Top1000小文件/大文件的相关维度信息，提供文件名称、路径、用户组、所属用户、大小、最近一次访问时间等信息查询及下载.。
![](https://qcloudimg.tencent-cloud.cn/raw/780ee13bffb9514dc6eb455a3ce36026.png)

<dx-alert infotype="alarm" title="风险说明">
文件存储分析依赖的分析数据将于北京时间每天14:00开始采集。
1. 文件存储分析涉及对备份 fsimage 文件采集分析，该分析影响本机内存使用增加（最大增幅4G），若集群内存使用机器总占比连续高位时，可 [工单反馈](https://console.cloud.tencent.com/workorder/category) 关闭该功能。 
2. HA 集群该分析功能执行在 Standby Master 节点，非 HA 集群该分析功能执行在 Master 节点。
</dx-alert>


  
