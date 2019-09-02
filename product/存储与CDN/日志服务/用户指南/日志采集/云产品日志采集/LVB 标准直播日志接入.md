# LVB 标准直播日志接入

在借助标准直播（LVB）处理直播业务时，会产生大量的日志数据。标准直播（LVB）实时日志已经和腾讯云的日志服务（CLS）平台打通，将采集的实时日志实时推送至日志服务平台，5分钟快速接入日志服务（CLS），帮助您实现“一站式”的日志管理。
![](https://main.qcloudimg.com/raw/5d8310deca5c97cd7225a297425c6089.png)

## 接入步骤

1. 您可以通过登录[标准直播控制台](https://console.cloud.tencent.com/live)，选择**日志管理->实时日志分析**，进入实时日志分析页面。
2. 如果首次进入实时日志，您需要先进行日志服务（CLS）的相关授权，才能正常使用检索功能。
   ![](https://main.qcloudimg.com/raw/eba038a70504cd72d9afc7f39ef47740.png)
   ![](https://main.qcloudimg.com/raw/cd2a082da92b046a1e8a924b55713497.png)
3. 您需要创建日志主题，并绑定域名。创建成功后，该日志主题将默认创建在日志服务平台的成都地域。
   ![](https://main.qcloudimg.com/raw/7289f0c1bb3b2dbbf8cafc0ff80c9054.png)
4. 创建成功后，单击检索，输入检索语句，可快速检索详细日志数据。日志服务的检索功能支持全文检索和键值检索，详细的检索语法请参考检索[语法与规则](https://cloud.tencent.com/document/product/614/16982)。
   ![](https://main.qcloudimg.com/raw/34d32de296751a997760d365759c2405.png)
   ![](https://main.qcloudimg.com/raw/f121488107009b5103704f23f6b8a553.png)
   ![](https://main.qcloudimg.com/raw/216d6944dda355549e068438408575f5.png)

推送至日志服务平台的日志为标准直播的访问日志，日志字段如下：

| 字段名称           | 类型 | 说明               | 示例             |
| ------------------ | ---- | ------------------ | ---------------- |
| log_time           | long | 请求时间           | 20190527153501   |
| bytes_stream_id    | text | 流 ID              | test             |
| host               | text | 被访问的域名       | test.lvb.xyz     |
| uri                | text | URL                | /live/test.flv   |
| play_size          | long | 本次访问字节数大小 | 556              |
| play_tm            | long | 播放时长           | 311              |
| msg_client_ip      | text | 客户端IP           | 59.37.125.121    |
| client_province_id | long | 省份               | 19               |
| client_isp_id      | long | 运营商             | 1                |
| client_country_id  | long | country_id         | 1                |
| http_method        | text | HTTP Method        | GET              |
| connect_fd         | long | connect_fd         | 34596            |
| http_status        | long | HTTP 状态码        | 200              |
| user_agent         | text | User-Agent 信息    | "Lavf/58.15.100" |
| refer              | text | Refer信息          | "-"              |
| hit                | text | 缓存 HIT/MISS      | miss             |
| msg_self_ip        | text | 节点IP             | 14.215.166.187   |
| oc_country_id      | long | 服务器国家         | 1                |
| oc_area_info       | text | 服务器地区         | 中国             |

注：国家（地区）映射、省份映射、运营商映射以及服务器地区和国家（地区映射）参见[文档](https://cloud.tencent.com/document/product/267/33998)。

## 实时检索示例

例一：检索状态码大于400且流ID为test2的日志数据

```
http_status>400 and bytes_stream_id:test2
```

![](https://main.qcloudimg.com/raw/370c254f7f0462c5568f1091cc990888.png)

例二：检索状态码大于等于200且小于300，同时请求方式为GET的方式（大小写不敏感）

```
http_status>=200 and http_status<300 and http_method:get
```

![](https://main.qcloudimg.com/raw/a674df1bdde1c72fc7c3f5d51832c25b.png)
