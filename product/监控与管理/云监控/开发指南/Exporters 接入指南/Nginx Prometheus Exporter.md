##  操作场景

Nginx 通过 stub_status 页面暴露了部分监控指标。Nginx Prometheus Exporter 会采集单个 Nginx 实例指标，并将其转化为 Prometheus 可用的监控数据， 最终通过 HTTP 协议暴露给 Prometheus 服务进行采集。我们可以通过 Exporter 上报重点关注的监控指标，用于异常报警和大盘展示。



## 操作步骤

### 使用 Docker 容器运行 Exporter

方式1：使用 [nginx-prometheus-exporter](https://hub.docker.com/r/nginx/nginx-prometheus-exporter) 通过 Docker 容器快速部署 Exporter。执行 Docker 命令如下：
```bash
$ docker run -p 9113:9113 nginx/nginx-prometheus-exporter:0.8.0 -nginx.scrape-uri http://<nginx>:8080/stub_status
```

方式2：使用 [nginx-prometheus-exporter](https://hub.docker.com/r/nginx/nginx-prometheus-exporter) 镜像将服务部署在腾讯云 [容器服务 TKE](https://cloud.tencent.com/document/product/457) 中，通过托管 Prometheus 的监控自发现 CRD PodMonitor 或者 ServiceMonitor 来采集监控数据。

### 使用二进制程序运行 Exporter

#### 下载安装

1. 根据实际运行环境在社区中下载相应的 [Nginx Prometheus Exporter](https://github.com/nginxinc/nginx-prometheus-exporter/releases) 。
2. 安装 Nginx Prometheus Exporter。

#### 开启 NGINX stub_status 功能

1. 开源 Nginx 提供一个简单页面用于展示状态数据，该页面由 [tub_status](http://nginx.org/en/docs/http/ngx_http_stub_status_module.html) 模块提供。执行以下命令检查 Nginx 是否已经开启了该模块：
```bash
nginx -V 2>&1 | grep -o with-http_stub_status_module
```
	- 如果在终端中输出 `with-http_stub_status_module` ，则说明 Nginx 已启用 tub_status 模块。
	- 如果未输出任何结果，则可以使用 `--with-http_stub_status_module` 参数从源码重新配置编译一个 Nginx。示例如下：
```
./configure \
… \
--with-http_stub_status_module
make
sudo make install
```
2. 确认 stub_status 模块启用之后，修改 Nginx 的配置文件指定 status 页面的 URL。示例如下：
```
server {
    location /nginx_status {
        stub_status;

        access_log off;
        allow 127.0.0.1;
        deny all;
    }
}
```
3. 检查并重新加载 nginx 的配置使其生效。
```bash
nginx -t
nginx -s reload
```
4. 完成上述步之后，可以通过配置的 URL 查看 Nginx 的指标：
```plaintext
Active connections: 45
server accepts handled requests
1056958 1156958 4491319
Reading: 0 Writing: 25 Waiting : 7
```



#### 运行 NGINX Prometheus Exporter

执行以下命令启动 NGINX Prometheus Exporter：
```bash
$ nginx-prometheus-exporter -nginx.scrape-uri http://<nginx>:8080/nginx_status
```

#### 上报指标

- `nginxexporter_build_info` -- exporter 编译信息。
- 所有的 [stub_status](http://nginx.org/en/docs/http/ngx_http_stub_status_module.html) 指标。
- `nginx_up` -- 展示上次抓取的状态：1表示抓取成功， 0表示抓取失败。


#### 配置 Prometheus 的抓取 Job

1. Nginx Prometheus Exporter 正常运行后，修改 Nginx 的配置文件，将 Job 添加到 Prometheus 的抓取任务中。
```bash
...
     - job_name: 'nginx_exporter'
       static_configs:
         - targets: ['your_exporter:port']                    
```
2. 通常情况下 ，Exporter 和 Nginx 并非共同运行，所以数据上报的 `instance` 并不能真实描述是哪个实例，为了方便数据的检索和观察，我们可以修改 `instance` 标签，使用真实的 IP 进行替换以便更加直观。示例如下：
```bash
...
  - job_name: 'mysqld_exporter'
    static_configs:
    - targets: ['your_exporter:port']
    relabel_configs:
     - source_labels: [__address__]
       regex: '.*'
       target_label: instance
       replacement: '10.0.0.1:80'
```


### 启用数据库监控大盘


腾讯云 Prometheus 托管服务在 Grafana 中提供预先配置的 Nginx Exporter  Dashboard，您可以根据以下操作步骤查看 Nginx 监控数据。
1. 登录 [云监控 Prometheus 控制台](https://console.cloud.tencent.com/monitor/prometheus)。
2. 单击对应实例 ID 右侧的**<img src="https://main.qcloudimg.com/raw/978c842f0c093a31df8d5240dd01016d.png" width="2%"/>** ，即可查看数据。
![Nginx Exporter dashboard](https://main.qcloudimg.com/raw/80ff106c4553812d083cd21c211ea950.png)
