当前服务网格 TCM 支持按照网格粒度配置数据面 Access Log，您可以在创建网格时配置 Access Log，网格创建后您也可以在基本信息页面修改 Access Log 配置。

当前支持的 Access Log 配置如下表：

| 配置项 | 描述 |
| ----- | ----- |
| 日志输出路径 | Access Log 文件输出路径，当前默认填写容器标准输出路径 `/dev/stdout` 。填写其他路径需配置容器 Volume，详情参见 [TKE 存储管理概述](https://cloud.tencent.com/document/product/457/46962) |
| 日志输出格式 | Access Log输出的格式定义字符串，设置为空则为默认输出格式，详情参见 [Istio Default Access Log Format](https://istio.io/latest/docs/tasks/observability/logs/access-log/#default-access-log-format) |
| 日志编码格式 | 当前支持 JSON 和 TEXT 两种编码格式 |

- 创建网格时配置 Access Log：
![](https://main.qcloudimg.com/raw/a8721b459a159c1da1b6e8b5964b9502.png)
- 网格创建完成后配置 Access Log：
![](https://main.qcloudimg.com/raw/5ee7c1e2d45b569677092ace9feb3a50.png)
