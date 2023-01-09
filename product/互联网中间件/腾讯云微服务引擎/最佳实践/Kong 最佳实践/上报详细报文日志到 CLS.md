## 操作场景
本文介绍如何通过 CLS Log 插件，将包含详细请求、响应 Body 报文的日志上报到 CLS Topic 中。

## 前置条件
1. 已购买 Kong 网关实例，[操作文档](https://cloud.tencent.com/document/product/1364/72495)。
2. 进入 [TSE 控制台](https://console.cloud.tencent.com/tse/kong)，并找到需要的实例。
3. 进入实例详情页后，找到**自定义插件**。


## 操作步骤

1. 下载 CLS Log 插件安装包 [cls_log.zip](https://kong-doc-1255960573.cos.ap-nanjing.myqcloud.com/cls-log.zip)。
2. 通过 [使用自定义插件](https://cloud.tencent.com/document/product/1364/72498)，在网关实例插件配置中，上传安装 CLS Log 插件，并启用。
![](https://qcloudimg.tencent-cloud.cn/raw/f32c40c394816e9dff344137ddaf0f9f.png)
3. 登录 Konga 控制台，在 PLUGINS 菜单中添加 CLS Log 插件全局开启，参数配置请参见下文中插件参数部分。
![](https://qcloudimg.tencent-cloud.cn/raw/a562f4bf533ef91b8ab86f970cc71e93.png)
4. 通过网关 IP 发起请求，在 CLS 控制台确认日志正确上报到对应的 CLS Topic 中，日志示例如下：
<dx-codeblock>
:::  json
{
    "tries":"[{\"balancer_latency\":0,\"port\":80,\"balancer_start\":1654569xxxxxx,\"ip\":\"172.0.0.2\"}]",
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
    "started_at":"1654569xxxxxx",
    "client_ip":"127.0.0.1",
    "upstream_response_time":"2",
    "resp_size":"10476",
    "route_id":"cca80823-3189-47fb-8a1f-21ebe7xxxxxx",
    "route_name": "",
    "service_id":"17caaef5-dc84-4c93-8148-e63ce1xxxxxx",
    "service_name": "",
    "consumer_id":"",
    "consumer_name": ""
}
:::
</dx-codeblock>


## 插件参数介绍

<table>
<thead>
<tr>
<th><span style="all: unset;"><span style="all: unset;">Form</span><span style="all: unset;"> </span><span style="all: unset;">Parameter</span></span></th>
<th>default</th>
<th>description</th>
</tr>
</thead>
<tbody><tr>
<td><code>cls_host</code></td>
<td>-</td>
<td>CLS API Host，例如：ap-beijing.cls.tencentyun.com。详情请参见 <a href="https://cloud.tencent.com/document/product/614/18940">CLS doc</a></td>
</tr>
<tr>
<td><code><span style="all: unset;"><span style="all: unset;">cls_topic</span></span></code></td>
<td>-</td>
<td>日志上报的目标 CLS Topic</td>
</tr>
<tr>
<td><code>secret_id</code></td>
<td>-</td>
<td>腾讯云账户 SecretID</td>
</tr>
<tr>
<td><code>secret_key</code></td>
<td>-</td>
<td>腾讯云账户 SecretKey</td>
</tr>
<tr>
<td><code>log_req_body</code></td>
<td>false</td>
<td>是否记录请求 Body 日志字段，开启后对网关性能有一定影响</td>
</tr>
<tr>
<td><code>log_resp_body</code></td>
<td>false</td>
<td>是否记录响应 Body 日志字段，开启后对网关性能有一定影响</td>
</tr>
<tr>
<td><code>max_req_body_size</code></td>
<td>10240</td>
<td>最大请求 Body 日志长度（单位字节），超出会被截断</td>
</tr>
<tr>
<td><code>max_resp_body_size</code></td>
<td>10240</td>
<td>最大响应 Body 日志长度（单位字节），超出会被截断</td>
</tr>
<tr>
<td><code>bacth_size</code></td>
<td>100</td>
<td>单次上报日志数量，一批日志大小不建议超过 8 MB。</td>
</tr>
<tr>
<td><code>retry_count</code></td>
<td>3</td>
<td>最大重试次数。</td>
</tr>
<tr>
<td><code>mode</code></td>
<td>memory</td>
<td>memory: 通过 CLS SDK 从内存队列中异步上报日志。access_log: &nbsp;通过 access_log 模块，配合 loglistener 采集上报，受磁盘性能影响，如需使用请工单联系开通。</td>
</tr>
<tr>
<td><code>fallback_to_access_log</code></td>
<td>false</td>
<td>当使用 memory 模式时，上报队列堆积时是否降级到 access_log 上报模式, 如需使用请工单联系开通。</td>
</tr>
</tbody></table>


## 注意事项

1. CLS Log 插件中配置的密钥对需拥有 `cls:UploadLog` 策略权限，详情请参见 [CLS 自定义策略示例](https://cloud.tencent.com/document/product/614/68374) 中使用 API 上传数据部分。
2. 开启 CLS Log 日志插件会对网关性能有少量影响，影响程度和报文日志大小成正比。
3. CLS Log 插件中实现了缓冲队列、分批上报，失败重试等功能，能够在偶发性上报失败时进行重试，但由于缓冲队列大小有限，长时间上报链路故障时仍然有丢失日志的风险。
3. CLS Log 插件包含通用的基本日志字段，如需自定义日志字段，可以基于该插件二次开发。
