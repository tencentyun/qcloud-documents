# 操作场景
本文介绍如何通过 CLS Log 插件，将包含详细请求、响应 Body 报文的日志上报到 CLS Topic 中。

# 前置条件
已购买 Kong 网关实例，[操作文档](https://cloud.tencent.com/document/product/1364/72495)。


# 操作步骤

1. 下载 CLS Log 插件安装包 [cls_log.zip](TODO)
2. 参考[产品文档](https://cloud.tencent.com/document/product/1364/72498)，在网关实例插件配置中，上传安装 CLS Log 插件，并启用。

![](https://qcloudimg.tencent-cloud.cn/raw/f32c40c394816e9dff344137ddaf0f9f.png)

3. 登陆 Konga 控制台，在 PLUGINS 菜单中添加 CLS Log 插件全局开启，参数配置请参考下文中插件参数部分。

![](https://qcloudimg.tencent-cloud.cn/raw/ad9ce0af8835e2dab199528acd91ebfc.png)

4. 通过网关 IP 发起请求，在 CLS 控制台确认日志正确上报到对应的 CLS Topic 中，日志示例如下

```
{
    "tries":"[{\"balancer_latency\":0,\"port\":80,\"balancer_start\":1654569255504,\"ip\":\"172.0.0.2\"}]",
    "upstream_uri":"/10k",
    "querystring":"{}",
    "req_url":"http://172.0.0.3/test",
    "latency_kong":"1",
    "req_method":"GET",
    "resp_headers":"{\"x-kong-upstream-latency\":\"2\",\"date\":\"Tue, 07 Jun 2022 02:34:15 GMT\"}",
    "req_uri":"/test",
    "resp_status":"200",
    "request_time":"3",
    "req_body":"",
    "resp_body":"some response body",
    "latency_proxy":"2",
    "req_headers":"{\"host\":\"172.16.0.37\"}",
    "started_at":"1654569255503",
    "client_ip":"127.0.0.1",
    "upstream_response_time":"2",
    "resp_size":"10476",
    "route_id":"cca80823-3189-47fb-8a1f-21ebe7cd224f",
    "route_name": "",
    "service_id":"17caaef5-dc84-4c93-8148-e63ce190d333",
    "service_name": "",
    "consumer_id":"",
    "consumer_name": ""
}
```

# 插件参数介绍

| Form Parameter | default | description |
| --- 						| --- | --- |
| `cls_host` 	                    |       | CLS API Host，例如：ap-beijing.cls.tencentyun.com。参考文档 [CLS doc](https://cloud.tencent.com/document/product/614/18940) |
| `cls_topic`  |  | 日志上报的目标 CLS Topic |
| `secret_id` 			                        |       | 腾讯云账户 SecretID |
| `secret_key`    |  | 腾讯云账户 SecretKey |
| `log_req_body`   | false       | 是否记录请求 Body 日志字段，开启后对网关性能有一定影响 |
| `log_resp_body`   | false       | 是否记录响应 Body 日志字段，开启后对网关性能有一定影响 |
| `max_req_body_size`   | 10240       | 最大请求 Body 日志长度（单位字节），超出会被截断 |
| `max_resp_body_size`   | 10240       | 最大响应 Body 日志长度（单位字节），超出会被截断 |
| `bacth_size`   | 100       | 单次上报日志数量，一批日志大小不建议超过 8 MB。  |
| `retry_count`   | 3       | 最大重试次数。  |
| `mode`   | memory       | memory: 通过 CLS SDK 从内存队列中异步上报日志。access_log:  通过 access_log 模块，配合 loglistener 采集上报，受磁盘性能影响，如需使用请工单联系开通。 |
| `fallback_to_access_log`   | false       | 当使用 memory 模式时，上报队列堆积时是否降级到 access_log 上报模式, 如需使用请工单联系开通。 |


# 注意事项

1. CLS Log 插件中配置的秘钥对需拥有 `cls:UploadLog` 策略权限，详细请参考[CLS自定义策略示例](https://cloud.tencent.com/document/product/614/68374)中使用 API 上传数据部分。
2. 开启 CLS Log 日志插件会对网关性能有少量影响，影响程度和报文日志大小成正比。
3. CLS Log 插件中实现了缓冲队列、分批上报，失败重试等功能，能够在偶发性上报失败时进行重试，但由于缓冲队列大小有限，长时间上报链路故障时仍然有丢失日志的风险。
3. CLS Log 插件包含通用的基本日志字段，如需自定义日志字段，可以基于该插件二次开发。
