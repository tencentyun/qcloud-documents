## 简介

Nginx 作为常见的反向代理服务，在实际业务中承载着大量的服务请求。服务在运行过程中会产生大量访问日志，通常使用户面临着集群中日志分散，数据量庞大等问题，因此如何有效地收集管理这些日志数据对业务的运维及运营都有着非常重要的意义。本文以 Nginx 访问日志为例，介绍如何使用日志服务统计分析功能分析 Nginx 日志。

#### Nginx 日志格式

Nginx 访问日志（access.log）的格式可以通过 nginx 配置文件，/etc/nginx/nginx.conf 下的 log_format 字段来定义，如下图所示。

```shell
log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                  '$status $body_bytes_sent $request_time "$http_referer" '
                  '"$http_user_agent" "$http_x_forwarded_for" "$msec"';
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
| msec                 | 日志写入时间，以秒为单位，精度为毫秒的 UNIX 时间戳       |

>!使用日志分析功能，必须在索引配置中，配置待统计字段的键值索引，并开启统计。
>![image-20200817202408930](https://main.qcloudimg.com/raw/c2f6b9608764c2007ee20cb2b7b7016f.png)
修改索引配置后，约有1分钟生效延时。新的索引配置只对后续写入的日志数据生效。



## SQL 分析示例

#### 带宽曲线图

```plaintext
* | select HISTOGRAM(CAST(msec*1000 AS TIMESTAMP), INTERVAL 1 MINUTE) AS dt, round(SUM(body_bytes_sent)*8/1000.0, 2) AS "带宽(Kb/min)" group by dt order by dt limit 50
```

![image-20200911111842113](https://main.qcloudimg.com/raw/ecc05dd9a50e904a3ef8829bdb57e662.png)

#### 平均下载速度

```plaintext
* | select HISTOGRAM(CAST(msec*1000 AS TIMESTAMP), INTERVAL 1 MINUTE) AS dt, round(SUM(body_bytes_sent) * 1.0 / SUM(request_time),2) AS "下载速度(KB/s)" group by dt order by dt limit 50
```

![image-20200911111939250](https://main.qcloudimg.com/raw/5c34c3eaffdaa281fa2b0130e1232ac9.png)

#### uv

```plaintext
* | select HISTOGRAM(CAST(msec*1000 AS TIMESTAMP), INTERVAL 1 MINUTE) AS dt, approx_distinct(remote_addr) as uv group by dt order by dt limit 50
```

![image-20200911112029388](https://main.qcloudimg.com/raw/c0bc1b75b9221487b162cd3aa4c04a27.png)

#### pv

```plaintext
* | select HISTOGRAM(CAST(msec*1000 AS TIMESTAMP), INTERVAL 1 MINUTE) AS dt, count(*) as pv group by dt order by dt limit 50
```

![image-20200911112124848](https://main.qcloudimg.com/raw/7aa705b7c9d4e38f4ec25c8ec72af1bf.png)

#### 请求类型分布

```plaintext
* | select HISTOGRAM(CAST(msec*1000 AS TIMESTAMP), INTERVAL 1 MINUTE) AS dt, count(*) as pv, method group by dt, method order by dt limit 200
```

![image-20200911112536464](https://main.qcloudimg.com/raw/ee19047e3e3802fd80350875acb06832.png)状态码占比

```plaintext
* | select count(*) as count, status where url like 'http://console.cloud.tencent.com/cls/sql/index1%' group by status
```

![image-20200818161708949](https://main.qcloudimg.com/raw/914390feb42a768f2ba7121f70c6a447.png)

#### Top URL

```plaintext
* | select request_url as "t-url", count(*) as count group by request_url order by count desc limit 10
```

![image-20200818161840764](https://main.qcloudimg.com/raw/48f16a7d421dbc1ddd035c6f43a59d40.png)
