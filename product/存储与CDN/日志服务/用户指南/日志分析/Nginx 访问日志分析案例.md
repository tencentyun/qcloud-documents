## 简介

Nginx 作为常见的反向代理服务，在实际业务中承载着大量的服务请求。服务在运行过程中会产生大量访问日志，通常使用户面临着集群中日志分散，数据量庞大等问题，因此如何有效地收集管理这些日志数据对业务的运维及运营都有着非常重要的意义。本文以 Nginx 访问日志为例，介绍如何使用日志服务统计分析功能分析 Nginx 日志。

#### Nginx 日志格式

Nginx 访问日志（access.log）的格式可以通过 log_format 字段来定义。

```shell
log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                  '$status $body_bytes_sent $request_time "$http_referer" '
                  '"$http_user_agent" "$http_x_forwarded_for"';
```

字段含义说明：

| 字段名               | 含义                                                   |
| -------------------- | ------------------------------------------------------ |
| remote_addr          | 客户端 IP 地址                                         |
| remote_user          | 客户端名称                                             |
| time_local           | 服务器本地时间                                         |
| method               | HTTP 请求方法                                          |
| url                  | URL 地址                                               |
| protocol             | 协议类型                                               |
| status               | HTTP 请求状态码                                        |
| body_bytes_sent      | 发送给客户端的字节数                                   |
| request              | 请求响应时间（单位：秒）                               |
| http_referer         | 访问来源的页面链接地址                                 |
| http_user_agent      | 客户端浏览器信息                                       |
| http_x_forwarded_for | 当前端有代理服务器时，追踪记录客户端真实 IP 地址的配置 |

#### 前置条件：配置键值索引规则

1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls/overview?region=ap-guangzhou) 在控制台左侧导航栏中单击【日志集管理】，依次进入到存放该 Nginx 日志所在的日志集和日志主题管理界面。
2. 在日志主题管理页面，单击【索引配置】，按照 Nginx 日志格式的字段定义，在索引配置管理页面设置对应的键值索引字段。
3. 对指定字段开启统计功能（只有开启统计的字段，才能支持 SQL 分析）。
![1569579807531](https://main.qcloudimg.com/raw/284c50f534812847a20f248cd77137c9/1569579807531.png)

>!修改索引配置后，约有1分钟生效延时。新的索引配置只对后续写入的日志数据生效。



## SQL 分析示例

#### 带宽曲线图

```sql
* | select HISTOGRAM(CAST(time_iso8601 AS TIMESTAMP), INTERVAL 1 MINUTE) AS dt, round(SUM(body_bytes_sent)*8/1000.0, 2) AS "带宽(Kb/min)" group by dt order by dt limit 50
```

![image-20200818160959408](https://main.qcloudimg.com/raw/a1a7e87632a29afa79a6f95e2683f115.png)

#### 平均下载速度

```sql
* | select HISTOGRAM(CAST(time_iso8601 AS TIMESTAMP), INTERVAL 1 MINUTE) AS dt, round(SUM(body_bytes_sent) * 1.0 / SUM(request_time),2) AS "下载速度(KB/s)" group by dt order by dt limit 50
```

![image-20200818161033317](https://main.qcloudimg.com/raw/8acbb6646cb9383a0912bbc8684e0898.png)

#### uv

```sql
* | select HISTOGRAM(CAST(time_iso8601 AS TIMESTAMP), INTERVAL 1 MINUTE) AS dt, count(distinct(remote_addr)) as uv group by dt order by dt limit 50
```

![image-20200818161252924](https://main.qcloudimg.com/raw/f3ccbfd8b177f5b7c5fce4e6ee1219da.png)

#### pv

```sql
* | select HISTOGRAM(CAST(time_iso8601 AS TIMESTAMP), INTERVAL 1 MINUTE) AS dt, count(*) as pv group by dt order by dt limit 50
```

![image-20200818161330147](https://main.qcloudimg.com/raw/d6fa7f6f0db7beb1942cc77dca8a746e.png)

#### 请求类型分布

```sql
* | select HISTOGRAM(CAST(time_iso8601 AS TIMESTAMP), INTERVAL 1 MINUTE) AS dt, count(*) as pv, method group by dt, method order by dt limit 200
```

![image-20200818161534819](https://main.qcloudimg.com/raw/0fe81b93734540e91e4e7a58462363bd.png)
状态码占比

```sql
* | select count(*) as count, status where url like 'http://console.cloud.tencent.com/cls/sql/index1%' group by status
```

![image-20200818161708949](https://main.qcloudimg.com/raw/914390feb42a768f2ba7121f70c6a447.png)

#### Top URL

```sql
* | select request_url as "t-url", count(*) as count group by request_url order by count desc limit 10
```

![image-20200818161840764](https://main.qcloudimg.com/raw/48f16a7d421dbc1ddd035c6f43a59d40.png)
