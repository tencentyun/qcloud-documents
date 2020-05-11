## 简介
Nginx 作为常见的反向代理服务，在实际业务中承载着大量的服务请求。服务在运行过程中会产生大量访问日志，通常使用户面临着集群中日志分散，数据量庞大等问题，因此如何有效地收集管理这些日志数据对业务的运维及运营都有着非常重要的意义。本文以 Nginx 访问日志为例，介绍如何使用日志服务接入 Nginx 日志。

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
| remote_addr          | 客户端 IP 地址                                           |
| remote_user          | 客户端名称                                             |
| time_local | 服务器本地时间                                         |
| method               | HTTP 请求方法                                          |
| url                  | URL 地址                                               |
| protocol             | 协议类型                                               |
| status               | HTTP 请求状态码                                        |
| body_bytes_sent      | 发送给客户端的字节数                                   |
| request      | 请求响应时间（单位：秒）                                 |
| http_referer         | 访问来源的页面链接地址                                 |
| http_user_agent      | 客户端浏览器信息                                       |
| http_x_forwarded_for | 当前端有代理服务器时，追踪记录客户端真实 IP 地址的配置 |

## 操作步骤

#### 1. 创建日志集和日志主题

（1）登录 [日志服务控制台](https://console.cloud.tencent.com/cls)，在左侧导航栏中单击【日志集管理】，进入日志集管理页面。
（2）在页面顶部选择合适的地域，单击【创建日志集】，开始创建日志集。例如，创建一个名为 nginx_project 的日志集。
（3）单击“日志集名称”，进入到日志主题管理页面。
（4）单击【新增日志主题】，创建日志主题。例如，创建一个名为 nginx_access 的日志主题，创建好的日志主题将会出现在日志主题列表中。


#### 2. 创建机器组

>?推荐使用日志服务采集器采集 Nginx 服务集群的日志，采集器下载安装请参见 [LogListener 安装指南](https://cloud.tencent.com/document/product/614/17414)。

（1）在控制台左侧导航栏中单击【机器组管理】，进入到机器组管理页面。
（2）在页面顶部选择合适的地域，单击【创建机器组】，创建一个名为 nginx_group 的机器组，一个机器组可以填入多个机器 IP 地址（每行一个 IP 地址），若是腾讯云服务器 CVM，直接填写内网 IP 地址即可，更多信息请参见 [机器组管理](https://cloud.tencent.com/document/product/614/17412)。


#### 3. 配置采集规则

（1）在控制台左侧导航栏中单击【日志集管理】，依次进入到所创建的日志集和日志主题管理界面。
（2）在日志主题管理页面，单击【采集配置】，为该日志主题指定采集路径、解析模式、绑定机器组。
- 设置日志路径并绑定机器组
  例如，将本地日志路径`/usr/local/webserver/nginx/logs/access.log`设置为采集目标路径，并绑定 nginx_group 机器组，相关设置如图所示：
  ![](https://main.qcloudimg.com/raw/e208071c005f765e2ad55a3693c8b208.png)
- 提取 key-value 键值
  键值提取模式选择 [完全正则](https://cloud.tencent.com/document/product/614/32817) 模式，输入日志样例后，验证提取规则的正则表达式。
  例如，Nginx 访问日志的日志格式 log_format 定义如下：  
  ```shell
  log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                  '$status $body_bytes_sent $request_time "$http_referer" '
                  '"$http_user_agent" "$http_x_forwarded_for"';
  ```
  一条完整的 Nginx 访问日志样例：
  ```shell
  101.86.17.56 - - [2019-09-27T18:16:04+08:00] "GET /phpMyAdmin/themes/pmahomme/img/sprites.png HTTP/1.1" 200 46795 0.066 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36" "-"
  ```
  所对应键值提取的正则表达式：
  ```shell
(\S+)\s\S+\s(\S+)\s\[([^\]]+)\]\s\"([^\"]+)\s(\S+)\s([^\"]+)\"\s(\d+)\s(\d+)\s([\d,.]+)\s\"([^\"]+)\"\s\"([^\"]+)\"\s\"([^\"]+)\"$
  ```
	提取正则表达式验证成功后，为每个字段命名对应的键值名称：
	![1569579711295](https://main.qcloudimg.com/raw/a691908bb996457e7ce859870c9cc11e/1569579711295.png)
	![1569576940882](https://main.qcloudimg.com/raw/3d7c471cc87ffdd8386d91fb08904948/1569576940882.png)


#### 4. 配置索引规则

（1）在控制台左侧导航栏中单击【日志集管理】，依次进入到所创建的日志集和日志主题管理界面。
（2）在日志主题管理页面，单击【索引配置】，按照 Nginx 日志格式的字段定义，在索引配置管理页面设置对应的索引字段。
（3）对指定字段开启统计功能（只有开启统计的字段，才能支持 SQL 分析）。
![1569579807531](https://main.qcloudimg.com/raw/284c50f534812847a20f248cd77137c9/1569579807531.png)

#### 5. 查询 Nginx 日志

（1）在控制台左侧导航栏中单击【日志检索】，进入到日志检索页，选择对应的日志集和日志主题。
（2）单击【搜索】，即可查询到 Nginx 访问日志内容。
![](https://main.qcloudimg.com/raw/71e82c28ea34781b2893152974e15867.png)

#### 6. 快速分析

在【原始数据】的子页面中，在左侧【快速分析】菜单栏中，点击对应日志字段（只有在索引配置页面中开启统计功能后，才能在快速分析字段列表中展现），可以查看字段值的分布情况。

如下图所示，单击【status】字段后，可以看到 Nginx 的 TOP 10 的状态码分布，以及各状态的日志数占比。

![1569575061762](https://main.qcloudimg.com/raw/acd010bd498919477cd67457fcc80007/1569575061762.png)

点击具体字段值，会自动生成对应的检索语句，并返回关键字检索结果，达到快速分析的目的。

如下图所示，单击 status 字段的 404 字段值，前端自动生成 status:404 的检索语句，并返回命中的日志详情。
![1569575315340](https://main.qcloudimg.com/raw/0938c7a7d54c7cd273eeef1b5c79a09f/1569575315340.png)

#### 7. SQL 分析

##### 带宽曲线图

```sql
select HISTOGRAM(CAST(time_iso8601 AS TIMESTAMP), INTERVAL 1 MINUTE) AS dt, round(SUM(body_bytes_sent)*8/1000.0, 2) AS "带宽(Kb/min)" group by dt order by dt limit 50
```

![1569747594824](https://main.qcloudimg.com/raw/84aa686b3561ebc43ae8b33a51d41021/1569747594824.png)

#### 平均下载速度

```sql
select HISTOGRAM(CAST(time_iso8601 AS TIMESTAMP), INTERVAL 1 MINUTE) AS dt, round(SUM(body_bytes_sent) * 1.0 / SUM(request_time),2) AS "下载速度(KB/s)" group by dt order by dt limit 50
```

![1569747685161](https://main.qcloudimg.com/raw/e37748dd21b8e0377414a3e9c43a57b4/1569747685161.png)

#### uv

```sql
select HISTOGRAM(CAST(time_iso8601 AS TIMESTAMP), INTERVAL 1 MINUTE) AS dt, count(distinct(remote_addr)) as uv group by dt order by dt limit 50
```

![1569746108594](https://main.qcloudimg.com/raw/a06b54867464a07d9d26aee21b250d44/1569746108594.png)

#### pv

```sql
select HISTOGRAM(CAST(time_iso8601 AS TIMESTAMP), INTERVAL 1 MINUTE) AS dt, count(*) as pv group by dt order by dt limit 50
```
![1569747161199](https://main.qcloudimg.com/raw/ef04598445753eaf56cff065139c70dd/1569747161199.png)

#### 请求类型分布

```sql
select HISTOGRAM(CAST(time_iso8601 AS TIMESTAMP), INTERVAL 1 MINUTE) AS dt, count(*) as pv, method group by dt, method order by dt limit 200
```

![1569746979626](https://main.qcloudimg.com/raw/7baba456563a491496f1219d4d6a9396/1569746979626.png)
![1569747329971](https://main.qcloudimg.com/raw/52534652d6c705ee6b069190fc9abbfd/1569747329971.png)

#### 状态码占比

```sql
select count(*) as count, status where url like 'http://console.cloud.tencent.com/cls/sql/index1%' group by status
```

![1569748333783](https://main.qcloudimg.com/raw/daaebf4a9a100aa4abefa45ee9ea3531/1569748333783.png)

#### Top URL

```sql
select url as "t-url", count(*) as uc group by url order by uc desc limit 10
```
![1569827430826](https://main.qcloudimg.com/raw/cdf13ed943c9fedc7b30eefb234c6811/1569827430826.png)

