本文介绍云原生 API 网关 Kong 如何将请求日志转存到 Kafka 实例。

## 操作场景
提供自建的 Kafka 以及对应的 topic 或使用腾讯云 [Ckafka](https://cloud.tencent.com/document/product/597) 产品, 根据下述操作，就可以将云原生 API 网关的流量日志落盘到该 Kafka 实例上。 

## 操作步骤
1. 自定义插件的文件目录格式，其中 handler.lua 与 schema.lua 为必要文件。
<img src="https://qcloudimg.tencent-cloud.cn/raw/29fe187a49453e962b30c803cc82ce1a.png" width=400px> 
2. 单击下载 [请求日志转存 Kafka 插件](https://tse-doc-attachments-1306573318.cos.ap-guangzhou.myqcloud.com/kong-kafka-log.zip)。 
3. 访问 [微服务引擎 Kong 控制台](https://console.cloud.tencent.com/tse/kong)，选择需要的网关实例，并单击**自定义插件**。
<img src="https://qcloudimg.tencent-cloud.cn/raw/c62438f2c9dd9e5e0e72888892b5c411.jpg"> 
4. 单击**上传插件**，将下载的压缩包上传并填写版本号等信息，单击**保存**。
<img src="https://qcloudimg.tencent-cloud.cn/raw/5825ec9de2f0a7b1203f57dbbc75e564.png" width=400px> 
5. 完成插件上传后，单击切换至该版本。
<img src="https://qcloudimg.tencent-cloud.cn/raw/dbc7deda6fe526966c4586dc387802a3.png"> 
6. 进入 Kong 实例的**配置管理** > **管理控制台**，查看 Kong 管理控制台地址并进入。
<img src="https://qcloudimg.tencent-cloud.cn/raw/db7e612decce2d072a73a10a0a79054a.jpg"> 
7. 进入 Kong 管理控制台页面后，单击侧边导航栏 SERVICES，选择需要的 service 并进入详情页。
<img src="https://qcloudimg.tencent-cloud.cn/raw/388e2947e6cbf38cd34b229a416adca2.png"> 
8. 选择 Plugins 并单击 **Add Plugin**，在 other 栏中选择添加 Kong Kafka Log。
<img src="https://qcloudimg.tencent-cloud.cn/raw/1a4dde739c2d854afe3b5d3aeaea11c1.png" width=600px> 
9. 填写 kafka server 地址以及 topic，其中 bootstrap servers 填写 kafka 的 server 地址，topic 为希望转存的 topic 必填参数，max size 为记录请求的最大长度，请求与返回的长度最大值，超过部分将截断。
<img src="https://qcloudimg.tencent-cloud.cn/raw/421ccda23f1da655c70ad512f938759c.png" width=600px> 
10. 该插件绑定 route 后，请求 route，消费 kafka 后可以查看消费到当前请求的日志内容（json 格式）。
<img src="https://qcloudimg.tencent-cloud.cn/raw/1d30f64bc3fd79f325b6a11fc885fff9.png" width=600px>
<img src="https://qcloudimg.tencent-cloud.cn/raw/0c2cbdc1fd0f805e0d29ce652dcf3058.png" width=600px>



## 参考

更多相关说明请参见 [Kong 插件文档](https://docs.konghq.com/hub/kong-inc/ip-restriction/)。

