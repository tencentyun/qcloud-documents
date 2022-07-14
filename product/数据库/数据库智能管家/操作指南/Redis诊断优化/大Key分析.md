DBbrain 支持 Redis 大 Key 分析，可快速发现实例中的大 Key，动态展示 TOP100 大 Key 统计分析结果，快速帮您定位：大 Key 内存占用、元素信息、过期时间等，避免大 Key 造成服务性能下降，内存不足等问题。

> ? 目前对过大 Redis 集群，或分片数过多的 Redis 集群，不支持大 Key 巡检功能，可通过创建**即时大 Key 分析**进行补充分析。

## 查看大 Key 分析结果
1. 登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain)，在左侧导航选择**诊断优化**，在上方选择对应数据库，然后选择**内存分析**页。
![](https://main.qcloudimg.com/raw/cddbe3b10e08a22499fd450ace79dfbf.png)
2. 在下方选择数据类型，数据类型基于内存、数量和前缀三个维度，对各个数据类型的 TOP100 大 Key 进行分析。
![](https://qcloudimg.tencent-cloud.cn/raw/11794470351e3e8653127508d5249bb9.png)
3. 在**近30天内存使用率**模块，拖动时间轴，可查看历史30天的大 Key 分析/内存情况。
  ![](https://main.qcloudimg.com/raw/fcac15ea328e54c257797934c2def268.png)
  趋势图中会展示近30天的内存使用状况，鼠标单击到历史中的某一天，会固定时间柱，与此同时下方列表中展示相应天的大 Key 情况。
  ![](https://qcloudimg.tencent-cloud.cn/raw/2382e7b19fb5dee6d2f10c2c1b2fc9e6.png)

## 即时大 Key 分析
1. 登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain)，在左侧导航选择**诊断优化**，在上方选择对应数据库，然后选择**内存分析**页，可以看到**即时大 Key 分析**功能。
![](https://main.qcloudimg.com/raw/3e423e9a1b9f23eae36ee451c5e86139.png)
2. 单击**创建**任务，DBbrain 会取得您数据库最近一次备份文件进行自动化分析，您可以通过任务列表进度条，得知分析进展。
3. 分析结束后，可以再任务列表查看分析结果。
![](https://main.qcloudimg.com/raw/48018deceb4b7ddac6b432fce4490762.png)

