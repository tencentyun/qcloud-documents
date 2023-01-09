图表自定义跳转功能，支持单击图表中的数值跳转到设定的URL地址，URL 地址可以引用变量。

## 操作步骤

1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls)。
2. 在左侧导航栏中，进入**检索分析**或**仪表盘**，创建一个表格类型的统计分析图表。
3. 在图表配置里选择**自定义跳转**，单击**+ 添加**。
<img src="https://qcloudimg.tencent-cloud.cn/raw/2d54d1d55bf45c8af9f12ad001fe19dc.png" width="48%">
4. 填写跳转链接的相关配置，可在链接中引用变量，并设置是否在新窗口打开。
<img src="https://qcloudimg.tencent-cloud.cn/raw/ae60f7d322e6e655cf136fd6b2572fe1.png" width="65%">



## 变量说明
- `${__field.Name}`  引用被单击的值的字段名称。
如下图所示，单击 **8.4s** 触发跳转链接，链接中嵌入了 **${__field.Name}** 变量，将会引用该数值所属的字段名称，即 **timecost** 填充到 URL 中。
<img src="https://qcloudimg.tencent-cloud.cn/raw/9d8a8e8f799f2b5b1c7c6a5040b3c8a0.png" width="65%">
- `${__value.raw}`  引用被点击的值（以原始格式填充）。
如下图所示，单击 **8.4s** 触发跳转链接，链接中嵌入了 **${__value.raw}** 变量，将会引用被单击值的原始数据，即没有添加单位与精度处理前的数值 **8.4125**。
<img src="https://qcloudimg.tencent-cloud.cn/raw/5df105178ea53964a91f38bceeb4fa8b.png" width="65%">
- `${__value.Text}`  引用被单击的值（以字符串格式填充）。
如下图所示，单击 **2020-10-27 17:21:00** 触发跳转链接，链接中嵌入了 **${__value.Text}** 变量，将会引用被单击值并转换为字符串格式，即 **2020-10-27%2017:21:00**（其中%20为空格的 URL 编码）。
<img src="https://qcloudimg.tencent-cloud.cn/raw/8335224af1fe9fa117856453360fc20a.png" width="65%">
- `${__value.Numeric}`  引用被单击的值（以数值格式填充）。
如下图所示，单击 **8.4s** 触发跳转链接，链接中嵌入了 **${__value.Numeric}** 变量，将会引用被单击值并转换为数值格式，即**8.4125**。此处时间类型的值会被转换为数值样式的 Unix 时间戳，字符串类型的值则引用失败。
<img src="https://qcloudimg.tencent-cloud.cn/raw/6472842ee24664a5f2f99b0d773a40a2.png" width="65%">
- `${__value.Time}`  被单击的值的时间戳（以 Unix 时间格式填充）。
如下图所示，单击 **8.4s** 触发跳转链接，链接中嵌入了 **${__value.Time}** 变量，将会引用被单击值同行的时间戳，即 analytic_time 的值**2022-10-27 17:21:00**，并转为 Unix 格式填充为**1666891260000**。若所在行无时间戳，则引用失败。
<img src="https://qcloudimg.tencent-cloud.cn/raw/ec3a44ecb721dba8cb0740cd8ad0f510.png" width="65%">
- `${__Fields.具体字段}`  同行该字段的值。
如下图所示，单击 **8.4s** 触发跳转链接，链接中嵌入了 **${__Fields.protocol_type}** 变量，将会引用被单击值同行该字段的值，即 protocol_type 的值 **http2**。

	<img src="https://qcloudimg.tencent-cloud.cn/raw/7a030f3c40c03d6eb52882a5b1a5d6ae.png" width="65%">




## 自定义跳转案例

场景：现已经统计了服务端 IP 的错误率的 TOP 情况，当出现错误率较高的IP时，需要跳转到检索分析页面，查看该 IP 的 status 状态码为 4XX 的日志。
<img src="https://qcloudimg.tencent-cloud.cn/raw/475eae030bf4dbf350276ec933736443.png" width="65%">
配置 URL 跳转链接如下图：
<img src="https://qcloudimg.tencent-cloud.cn/raw/3e81d07780fd0920f7d4c914b57698c1.png" width="65%">
```
https://console.cloud.tencent.com/cls/search?region=xxxxxxx&topic_id=xxxxxxxx&query=server_addr:${__value.text} AND status:[400 TO 499]&time=now-1h,now
```
单击目标IP地址后，自动打开检索页面检索，并显示检索结果。
<img src="https://qcloudimg.tencent-cloud.cn/raw/6eadda1f3554239d141097d0cdf29bf7.png" width="65%">
<img src="https://qcloudimg.tencent-cloud.cn/raw/2bb6b719f37ac80ee2a1c7c71eb4fd4d.png" width="65%">
