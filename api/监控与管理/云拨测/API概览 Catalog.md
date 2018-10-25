####API 概览

最近更新时间: 2017-06-02 14:51:00



## 1. 拨测任务 相关接口

| 接口功能 | 接口名称                | 功能描述          |
| ---- | ------------------- | ------------- |
| 验证任务 | SimpleVerifyCatTask | 验证拨测任务，发起请求   |
| 验证结果 | VerifyCatResult     | 验证拨测任务，结果验证查询 |
| 创建任务 | CreateCatTask       | 创建或修改 拨测任务    |
| 运行任务 | RunCatTask          | 运行拨测任务        |
| 暂停任务 | PauseCatTask        | 暂停拨测任务        |
| 删除任务 | DeleteCatTask       | 删除拨测任务        |
| 查询任务 | DescribeCatTaskList | 查询拨测任务列表      |
| 查询详情 | DescribeCatTask     | 查询拨测任务详情      |



## 2. 拨测告警 相关接口

| 接口功能   | 接口名称                   | 功能描述         |
| ------ | ---------------------- | ------------ |
| 创建策略   | CreateCatAlarmPloicy   | 为拨测任务创建告警策略  |
| 修改策略   | UpdateCatAlarmPloicy   | 为拨测任务修改告警策略  |
| 查告警接收组 | DescribeAlarmGroupList | 查询用户的告警接收组列表 |
| 查告警列表  | DescirbeCatAlarmList   | 查询拨测告警列表     |



## 3.拨测分组 相关接口

| 接口功能   | 接口名称                      | 功能描述          |
| ------ | ------------------------- | ------------- |
| 添加分组   | CreateCatAgentGroup       | 添加拨测分组        |
| 修改分组   | UpdateCatAgentGroup       | 修改拨测分组        |
| 删除分组   | DeleteCatAgentGroup       | 删除拨测分组        |
| 查询分组   | DescribeCatAgentGroup     | 查询拨测分组详情      |
| 查询拨测点  | DescribeAgentList         | 查询本用户可选的拨测点列表 |
| 查询分组列表 | DescribeCatAgentGroupList | 查询拨测分组列表      |



## 4.拨测结果 相关接口 

| 接口功能   | 接口名称                    | 功能描述           |
| ------ | ----------------------- | -------------- |
| 查询统计数据 | GetCatRespTimeTrend     | 查询拨测任务的统计数据    |
| 查询返回码  | GetCatReturnCodeHistory | 查询拨测任务的历史返回码信息 |





