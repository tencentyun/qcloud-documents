云监控于**2022年09月01日00:00:00**开始对部分 API 接口的请求进行计费，每个主账号的免费请求额度为100万次/月，超出免费额度后如需继续使用API接口请求监控数据，请在开通页手动开通“API 请求按量付费”，开通后系统将按照0.25元/万次请求进行计费。 如需查看 API 请求量，请进入控制台 > [资源消耗页](https://console.cloud.tencent.com/monitor/consumer/products)。
计费相关接口：[GetMonitorData](https://cloud.tencent.com/document/product/248/31014)




### 免费额度
每个主账号的免费请求额度为100万次/月。超过免费额度后将无法继续使用 [GetMonitorData](https://cloud.tencent.com/document/product/248/31014) 接口请求监控数据。如需继续调用接口需要手动开通“API请求按量付费”。

### 计费开通操作
进入 [API 后付费开通页](https://buy.cloud.tencent.com/APIRequestBuy) 可手动开通 **API 请求按量付费**，开通后您将可以在免费额度外正常调用 API 接。也可以在资源消耗页进行 **API 请求按量付费**的开通和关闭操作，或在该页面查看 API 请求量。
![](https://qcloudimg.tencent-cloud.cn/raw/c8557bad5bb63a9bcd56db7e45aa07e4.png)

### 计费规则
超过免费额度后，将按照下列模式进行计费。
**计费单价：** 0.25元/万次请求。
**计费公式：**若当月累计请求次数超过100万次，则每小时的计费金额为：计费单价 × 每小时实际请求次数/10000
>? 
- 开通“API 请求按量付费”后，系统将优先使用提供给主账号的100万次免费请求额度，额度用尽后系统将按小时统计 API 接口的请求次数并计费。
- 仅对用户使用 GetMonitorData 主动请求数据次数进行计量计费，不包含通过控制台操作产生的接口请求量。
- 使用自建 Prometheus，通过 tencentcloud-exporter 调用 GetMonitorData 接口产生的接口请求次数需要计费。
- 使用腾讯云 Prometheus 监控服务控制台的集成云监控功能，所产生的接口请求只会 Prometheus 数据上报的费用，不再额外收 GetMonitorData 接口的 API 调用费用。

### 计费示例
**示例**【免费额度已用尽】：

假设某用户当月请求次数为200万次（>100万次免费额度），某小时请求次数为2万次。

某小时的费用：0.25元/万次请求 ×20000次/10000 =0.5元

 
