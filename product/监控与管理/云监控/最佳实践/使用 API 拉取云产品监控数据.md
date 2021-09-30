


本文为您介绍如何使用 API 拉取腾讯云各产品监控数据。


## 接口介绍


#### 云监控提供以下3类接口用于指标类监控数据的查询


| API | 操作名 | 操作描述 |
|---------|---------|---------|
| [DescribeProductList](https://cloud.tencent.com/document/product/248/44374)| 查询产品列表接口|查询云监控支持哪些产品的监控项 |
| [DescribeBaseMetrics](https://cloud.tencent.com/document/product/248/30351) | 查询监控基础指标详情接口 | 查询对应的名字空间下面的监控指标类型 |
| [GetMonitorData](https://cloud.tencent.com/document/product/248/31014) | 拉取指标监控数据 | 对象维度描述和监控指标获取相应的监控数据 |



#### 接口相关限制

- GetMonitorData 接口支持批量获取用户下所有实例的某个指标的数据。
- GetMonitorData 接口默认支持请求频率限制：20次/秒，1200次/分钟。单请求最多可支持批量拉取10个实例的监控数据，单请求的数据点数限制为1440个。
- 监控数据存储时长，不同的监控粒度存储时长不同。详情请参考下列图表：
	<table>
<thead>
<tr>
<th>监控粒度</th>
<th>存储时长</th>
</tr>
</thead>
<tbody><tr>
<td>秒级</td>
<td>1天</td>
</tr>
<tr>
<td>1分钟</td>
<td>15天</td>
</tr>
<tr>
<td>5分钟</td>
<td>31天</td>
</tr>
<tr>
<td>1小时</td>
<td>93天</td>
</tr>
<tr>
<td>1天</td>
<td>186天</td>
</tr>
</tbody></table>
 
>?云服务器包含 CPU、内存、网络相关指标1分钟监控粒度的存储时长为31天。






## 准备工作


### 准备个人密钥[](id:step1)

1. 登录 [API 密钥管理](https://console.cloud.tencent.com/cam/capi)。
2. 若还未创建密钥，则需单击**新建密钥**以创建密钥；若已创建密钥，可单击 SecretKey 的**显示**获取密钥。
![](https://main.qcloudimg.com/raw/dfc5cf24f6d04bcf87a64ec325b6e915.png)


### 准备云产品指标信息[](id:step2)


本文以云服务器 CPU 利用率指标为例。

1.	查看 [云服务器监控指标文档](https://cloud.tencent.com/document/product/248/6843),
2.	找到 CPU 利用率指标，即可查看 CPU 利用率指标名、维度，统计粒度等相关信息。
![](https://main.qcloudimg.com/raw/0140541d15e09a5ae4b41394f4f529e4.png)


## 实践步骤

通过 Demo 演示，为您介绍如何使用 [GetMonitorData](https://cloud.tencent.com/document/product/248/31014) 接口查询 CVM 的 CPU 利用率。

1. 登录 [API Explorer](https://console.cloud.tencent.com/api/explorer?Product=monitor&Version=2018-07-24&Action=GetMonitorData&SignVersion=) 在线调试页面。
2. 将 [准备好的个人密钥](#step1) 对应复制到对应的 SecretId、SecretKey 文本框。
3. 在**输入参数**配置项找到 Region，选择相关地域。
4. 将 [准备好的云产品信息](#step2)，填入对应的**输入参数**配置项文本框。
 - **Namespace**：填入 QCE/CVM。
 - **MetricName**：填入 CPU 利用率指标英文名，即 CPUUsage。
 - **Dimensions.N-Name**：填入支持的维度名称，即 InstanceId。
 - **Dimensions.N-Value**：填入对应的 InstanceId 值（云服务器实例 ID），可通过云服务器 [查询实例列表接口](https://cloud.tencent.com/document/product/213/15728) 获取实例对应的 ID，例如 ins—12345678。
 - **Period**：填入指标支持的统计粒度，例如300。
 - **StartTime**：填入需要查询的起始时间（时间类型为 datetime_iso），格式为 `2020-12-20T19:51:23+08:00`。
 - **EndTime**：填入需要查询的起始时间结束时间（时间类型为 datetime_iso），EndTime 不能小于 StartTime。格式为 `2020-12-20T20:51:23+08:00`。
![](https://main.qcloudimg.com/raw/ad04f8261b114d1482a03abef2eaa658.png)
5. 以上信息填完后，您可以复制**代码生成**中对应语言的代码，将相关的监控数据集成到您的自建监控系统，您还可以使用**在线调用**发送请求进行在线查询监控数据。
