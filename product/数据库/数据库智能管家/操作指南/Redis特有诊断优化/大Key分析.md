### 大Key分析
DBbrain 支持Redis 大Key分析，可快速发现实例中的大Key，动态展示TOP100大Key统计分析结果，快速帮您定位，大Key 内存占用、元素信息、过期时间等，避免大Key造成服务性能下降，内存不足等问题；

### 如何查看大Key分析结果？
登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain)，在左侧导航选择【诊断优化】，在上方选择对应数据库，然后选择【内存分析】页。

![](https://main.qcloudimg.com/raw/0eeef362adc53215448881662be47fd7.png)
1. 先选数据类型，基于内存和数量两个维度，对各个数据类型的TOP100大Key进行发现、分析

![](https://main.qcloudimg.com/raw/e4c0d81f3dd81693f43d56b1cbcb2c26.png)

2. 支持时间轴历史回放，查看历史30天的大key分析/内存情况
![](https://main.qcloudimg.com/raw/fcac15ea328e54c257797934c2def268.png)


3. 趋势图中展示近30天的内存使用状况，鼠标点击到历史中的某一天，会固定时间柱，与此同时下方列表中展示相应天的大Key情况。
![](https://main.qcloudimg.com/raw/eab8f8787beb6d617b9fa90517cde4c2.png)




