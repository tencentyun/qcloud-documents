## Nginx-ingress日志配置

### Nginx-ingress日志基础
Nginx Controller 有以下日志需要搜集提供给用户

Nginx Controller 日志：重要。控制面日志，记录了Nginx Controller控制面的修改。主要用于控制面排障。比如用户错误配置Ingress模板同步未进行等。
AccessLog 日志：重要。用户数据面日志，记录了用户的七层请求相关信息。主要用于提供给用户进行数据分析、审计、业务排障等等。
ErrorLog 日志：一般。Nginx的内部错误日志

默认配置下，AccessLog和Nginx Controller日志会混合到标准输出流，采集将遇到困难。这里应该对日志路径进行区分分别收集。

### TKE Nginx-ingress 日志介绍
补充开启日志采集的截图：

TKE 通过集成腾讯云日志服务CLS， 提供了全套完整的产品化能力，实现nginx-ingress日志采集、消费能力。
1. 前置要求：集群开启日志采集功能
2. 在nginx-ingress组件配置日志采集到用户指定的日志集，如不制定将创建新的日志集。
3. 计费说明：[CLS计费概述](https://cloud.tencent.com/document/product/614/45802)
4. 采集的日志的指标如下：

```yaml
apiVersion: cls.cloud.tencent.com/v1
kind: LogConfig
metadata:
  name: nginx-ingress-test
  resourceVersion: "7169042"
  selfLink: /apis/cls.cloud.tencent.com/v1/logconfigs/nginx-ingress-test
  uid: 67c96f86-4160-40a8-843a-f6faf8d544dc
spec:
  clsDetail:
    extractRule:
      beginningRegex: (\S+)\s-\s(\S+)\s\[(\S+)\]\s(\S+)\s\"(\w+)\s(\S+)\s([^\"]+)\"\s(\S+)\s(\S+)\s\"([^"]*)\"\s\"([^"]*)\"\s(\S+)\s(\S+)\s\[([^\]]*)\]\s\[([^\]]*)\]\s\[([^\]]*)\]\s\[([^\]]*)\]\s\[([^\]]*)\]\s\[([^\]]*)\]\s(\S+)
      keys:
      - remote_addr
      - remote_user
      - time_local
      - timestamp
      - method
      - url
      - version
      - status
      - body_bytes_sent
      - http_referer
      - http_user_agent
      - request_length
      - request_time
      - proxy_upstream_name
      - proxy_alternative_upstream_name
      - upstream_addr
      - upstream_response_length
      - upstream_response_time
      - upstream_status
      - req_id
      logRegex: (\S+)\s-\s(\S+)\s\[(\S+)\]\s(\S+)\s\"(\w+)\s(\S+)\s([^\"]+)\"\s(\S+)\s(\S+)\s\"([^"]*)\"\s\"([^"]*)\"\s(\S+)\s(\S+)\s\[([^\]]*)\]\s\[([^\]]*)\]\s\[([^\]]*)\]\s\[([^\]]*)\]\s\[([^\]]*)\]\s\[([^\]]*)\]\s(\S+)
    logType: fullregex_log
    topicId: 56766bad-368e-4a94-afed-ed77ebcdefa8
  inputDetail:
    containerFile:
      container: controller
      filePattern: nginx_access.log
      logPath: /var/log/nginx
      namespace: default
      workload:
        kind: deployment
        name: nginx-ingress-nginx-controller
    type: container_file
```

### Nginx-ingress 日志仪表盘
TKE Nginx-ingress 开启日志采集功能会自动为您创建一个标准的日志仪表盘，如下。 您也可以根据您业务需要自行在CLS控制台配置图表。

补充CLS仪表盘设置。


