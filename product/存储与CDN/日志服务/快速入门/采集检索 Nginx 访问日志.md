
## 简介
Nginx 作为常见的反向代理服务，在实际业务中承载着大量的服务请求。服务在运行过程中会产生大量访问日志，通常使用户面临着集群中日志分散，数据量庞大等问题，因此如何有效地收集管理这些日志数据对业务的运维及运营都有着非常重要的意义。本文以 Nginx 访问日志为例，介绍如何使用日志服务接入 Nginx 日志。

#### Nginx 日志格式

Nginx 访问日志（access.log）的格式可以通过 log_format 命令来定义，以默认格式说明各字段含义及如何配置索引。

```plaintext
log_format  main  '$remote_addr - $remote_user [$time_local] "$request"'
                      '$status $body_bytes_sent "$http_referer"'
                      '"$http_user_agent" "$http_x_forwarded_for"';
```

字段含义说明：

| 字段名               | 含义                                                 |
| -------------------- | ---------------------------------------------------- |
| remote_addr          | 客户端 IP 地址                                         |
| remote_user          | 客户端名称                                           |
| time_local           | 服务器本地时间                                       |
| method               |HTTP 请求方法                                        |
| url                  | url 地址                                             |
| protocol             | 协议类型                                             |
| status               | HTTP 请求状态码                                      |
| body_bytes_sent      | 发送给客户端的字节数                                 |
| http_referer         | 访问来源的页面链接地址                               |
| http_user_agent      | 客户端浏览器信息                                     |
| http_x_forwarded_for | 当前端有代理服务器时，记录客户端真实 IP 地址的配置 |

## 操作步骤

#### 1. 创建日志集和日志主题

（1）登录 [日志服务控制台](https://console.cloud.tencent.com/cls)，在左侧导航栏中单击【日志集管理】，进入日志集管理页面。
（2）在页面顶部选择合适的地域，单击【创建日志集】，开始创建日志集。例如，创建一个名为 nginx_project 的日志集。
（3）单击“日志集名称”，进入到日志主题管理页面。
（4）单击【新增日志主题】，创建日志主题。例如，创建一个名为 nginx_access 的日志主题，创建好的日志主题将会出现在日志主题列表中。


#### 2. 创建机器组

>?推荐使用日志服务采集器采集 Nginx 服务集群的日志，采集器下载安装请参见 [LogListener 安装指南](https://cloud.tencent.com/document/product/614/17414)。

（1）在控制台左侧导航栏中单击【机器组管理】，进入到机器组管理页面。
（2）在页面顶部选择合适的地域，单击【创建机器组】，创建一个名为 nginx_group 的机器组（一个机器组可以填入多个机器 IP 地址（每行一个 IP 地址），若是腾讯云服务器 CVM，直接填写内网 IP 地址即可，更多信息请参见 [机器组管理](https://cloud.tencent.com/document/product/614/17412)）。


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
  log_format  main  '$remote_addr - $remote_user [$time_local] "$request"'
                        '$status $body_bytes_sent "$http_referer"'
                        '"$http_user_agent" "$http_x_forwarded_for"';
  ```

  一条完整的 Nginx 访问日志样例：
  ```shell
  59.x.x.x - - [06/Aug/2019:12:12:19 +0800] "GET /nginx-logo.png HTTP/1.1" 200 368 "http://119.x.x.x/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36" "-"
  ```

  所对应键值提取的正则表达式：
  ```shell
  (\S+)\s\S+\s(\S+)\s\[([^\]]+)\]\s\"([^\"]+)\s(\S+)\s([^\"]+)\"\s(\d+)\s(\d+)\s\"([^\"]+)\"\s\"([^\"]+)\"\s\"([^\"]+)\"$
  ```

  提取正则表达式验证成功后，为每个字段命名对应的键值名称：
	![](https://main.qcloudimg.com/raw/a6e0750e379a0bff82d19040eabea23a.png)

#### 4. 配置索引规则

（1）在控制台左侧导航栏中单击【日志集管理】，依次进入到所创建的日志集和日志主题管理界面。
（2）在日志主题管理页面，单击【索引配置】，按照 Nginx 日志格式的字段定义，在索引配置管理页面设置对应的索引字段。
![](https://main.qcloudimg.com/raw/a2fb95a5055dc5fe47fbdb1140b7e1e6.png)

#### 5. 查询 Nginx 日志

（1）在控制台左侧导航栏中单击【日志检索】，进入到日志检索页，选择对应的日志集和日志主题。
（2）单击【搜索】，即可查询到 Nginx 访问日志内容。
![](https://main.qcloudimg.com/raw/71e82c28ea34781b2893152974e15867.png)
