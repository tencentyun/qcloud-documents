本文以一个数据示例介绍数据接入平台提供的解析数据内部 JSON 结构的功能。

## 解析内部 JSON 结构

1. 输入带嵌套 JSON 格式的原始数据，以下为一个示例。
<dx-codeblock>
:::  json
{
	 "@timestamp": "2022-02-26T22:25:33.210Z",
	 "beat": {
			 "hostname": "test-server",
			 "ip": "6.6.6.6",
			 "version": "5.6.9"
	 },
	 "input_type": "log",
	 "message": "{\"userId\":888,\"userName\":\"testUser\"}",
	 "offset": 3030131
}
:::
</dx-codeblock>
2. 解析结果如下：
![](https://qcloudimg.tencent-cloud.cn/raw/7f85536c32e9d9772b9fc68bb38d1d6d.png)
3. DIP 处理方式：通过对该字段选择 MAP 操作来对其进行解析，从而把特定字段解析为 JSON 格式：
   ![](https://qcloudimg.tencent-cloud.cn/raw/7bb6eee6f6f780f7d4f3d1c0e7c49502.png)