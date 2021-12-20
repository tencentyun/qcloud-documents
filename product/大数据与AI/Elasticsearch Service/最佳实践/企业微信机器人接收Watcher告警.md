腾讯云 Elasticsearch Service 白金版中支持了 X-Pack Watcher 特性，通过添加触发器、操作等配置，可以实现当条件满足时执行某些特定操作。例如当检测到索引中出现错误日志时自动发送告警。本文介绍如何配置企业微信机器人接收 Watcher 发出的告警。
>!
- X-Pack Watcher 特性仅在白金版中提供。
- 由于腾讯云 Elasticsearch Service 网络架构调整，仅2020年6月及之后创建的实例支持配置企业微信机器人接收 Watcher 告警。

## 背景信息
一个 Watcher 由4部分组成，具体如下：
- Trigger：定义了何时 Watcher 开始执行，在配置 Watcher 时必须设置。支持的触发器详情参见 [Schedule Trigger](https://www.elastic.co/guide/en/elasticsearch/reference/6.8/trigger-schedule.html)。
- Input：对监控的索引执行的查询条件，同时在触发 Watcher 时，Input 将数据加载到执行上下文中，在后续的 Watcher 执行阶段，可访问这个上下文。详情请参见 [Inputs](https://www.elastic.co/guide/en/elasticsearch/reference/6.8/input.html)。
- Condition：执行 Actions 需要满足的条件。
- Actions：当条件发生时，执行的具体操作。例如本文介绍的 Webhook Action。

## 操作步骤
1. 准备一台与 ES 集群同 VPC 的并且可以访问 Webhook 地址的 CVM（如通过外网访问）。
2. 在 CVM 中安装 Nginx，具体安装方法参见 [Nginx 安装](https://www.runoob.com/linux/nginx-install-setup.html)。
3. 配置 Nginx 代理转发。使用以下配置替换 nginx.conf 文件中 Server 部分的配置。
 - Nginx 服务的默认端口是80，若您需要更改其端口，则需要登录控制台 [安全组](https://console.cloud.tencent.com/cvm/securitygroup) 放行此端口。
 - <企业微信机器人 Webhook 地址>：需替换为接收报警消息的企业微信机器人的 Webhook 地址。
```
server {
			listen       80;
			server_name  localhost;
			index index.html index.htm index.php;
			root /usr/local/nginx/html;
			#charset koi8-r;

			#access_log  logs/host.access.log  main;
			location ~ .*\.(php|php5)?$
			{
				fastcgi_pass 127.0.0.1:9000;
				fastcgi_index index.php;
				include fastcgi.conf;
			}
			location ~ .*\.(gif|jpg|jpeg|png|bmp|swf|ico)$
			{
				expires 30d;
			# access_log off;
			}
			location / {
				proxy_pass <企业微信机器人的wehbook地址>;
			}
			location ~ .*\.(js|css)?$
			{
				expires 15d;
				# access_log off;
			}
			access_log off;

			#error_page  404              /404.html;

			# redirect server error pages to the static page /50x.html

			error_page   500 502 503 504  /50x.html;
			location = /50x.html {
					root   html;
			}
}
```
4. 加载修改后的配置文件并重启 Nginx。
```
/usr/local/webserver/nginx/sbin/nginx -s reload
/usr/local/webserver/nginx/sbin/nginx -s reopen
```
5. 配置 Watcher 报警规则。**此步骤可以在 Kibana 界面【Management】>【Watcher】选项中进行图形化操作。**
![](https://main.qcloudimg.com/raw/125ca1068c3a8905212de5c158dd13c5.png)
 - `Create threshold alert` 在界面进行阈值告警设置。可以针对某索引的特定条件进行监控告警，例如 CPU 使用率、文档个数等，可以在下面的 Condition 选项作更细节的设置，参考如下：
![image](https://main.qcloudimg.com/raw/7035acfff95d603d797fa95d6ed6f9ec.png)
单击右上角的【Add action】, 选择 “Wehhook”，相关设置如下：
![image](https://main.qcloudimg.com/raw/e4d83130fa2405c24722f3f950bb71d0.png)
单击【Send request】可以进行测试，然后单击【Create alert】即可。
 - `Create advanced watch` 通过 API 设置 Watcher 各参数，API 详情请参见 [PUT Watch](https://www.elastic.co/guide/en/elasticsearch/reference/6.8/watcher-api-put-watch.html)。
6. 以上步骤配置完成后，即可在自己创建的企业微信群中接收到机器人发来的告警信息。
![](https://main.qcloudimg.com/raw/7b3bd3d2ab9c94c12f6260ff0a3e0dde.png)
