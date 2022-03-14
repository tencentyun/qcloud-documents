
容器服务 TKE 通过集成日志服务 CLS，提供了全套完整的产品化能力，实现 Nginx-ingress 日志采集、消费能力。

## Nginx-ingress 日志基础

Nginx Controller 需要搜集以下日志并提供给用户：
- **Nginx Controller 日志**：重要。控制面日志，记录了 Nginx Controller 控制面的修改。主要用于控制面排障，例如用户错误配置 Ingress 模板导致同步未进行等。
- **AccessLog 日志**：重要。用户数据面日志，记录了用户的七层请求相关信息。主要用于提供给用户进行数据分析、审计、业务排障等。
- **ErrorLog 日志**：一般。Nginx 的内部错误日志。

默认配置下，AccessLog 和 Nginx Controller 日志会混合到标准输出流，日志采集将遇到困难。本文向您介绍如何对日志路径进行区分后分别收集日志。


## 前提条件 
已在容器服务控制台的 **[功能管理](https://console.cloud.tencent.com/tke2/ops/list?rid=8)**中开启日志采集，详情参见 [开启日志采集](https://cloud.tencent.com/document/product/457/36771)。



## TKE Nginx-ingress 采集日志
### 采集日志步骤
1. 为目标集群 [安装 Nginx-ingress](https://cloud.tencent.com/document/product/457/50503#Nginx-ingress) 组件。
2. 在“组件管理”页面选择已安装的组件名称，进入组件详情页。
3. 在**日志监控**页面中，选择日志配置右侧的**重新设置**。如下图所示：
![](https://main.qcloudimg.com/raw/e614b0ba9e9f50590d4752eecd4a1b71.png)
4. 在弹出的窗口中选择指定的日志集，如不制定将创建新的日志集。如下图所示：
![](https://main.qcloudimg.com/raw/93b4171bf694f97e465f8f3d1baa97e0.png)
5. 单击**立即启用**即可完成日志采集配置。
>! 日志服务具体计费规则和收费标准请参见 [CLS 计费概述](https://cloud.tencent.com/document/product/614/45802)。












### 采集日志指标
采集日志的指标如下所示：
```yaml
apiVersion: cls.cloud.tencent.com/v1
kind: LogConfig
metadata:
  name: nginx-ingress-test
  resourceVersion: "7169042"
  selfLink: /apis/cls.cloud.tencent.com/v1/logconfigs/nginx-ingress-test
  uid: 67c96f86-4160-****-****-f6faf8d544dc
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
    topicId: 56766bad-368e-****-****-ed77ebcdefa8
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

TKE Nginx-ingress 开启日志采集功能将会自动为您创建一个标准的日志仪表盘，您也可以根据业务需要自行在 CLS 控制台配置图表。如下图所示：
![](https://main.qcloudimg.com/raw/28674bb949ed77839b707cf80841e879.png)
