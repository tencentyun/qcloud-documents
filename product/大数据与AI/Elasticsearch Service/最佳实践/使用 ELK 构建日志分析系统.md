Elasticsearch Service 提供了 Elasticsearch 集群和 Kibana 控制台，Elasticsearch 集群可以通过 VPC 内的内网地址（私有网络 VIP 地址+端口）进行访问，Kibana 控制台可以通过浏览器在公网访问，用户可以在同一 VPC 内的设备上部署 Logstash 将数据接入 Elasticsearch 集群。

## 安装部署 logstash
### 环境准备
- 用户需要创建和 Elasticsearch 集群在同一 VPC 的 CVM，根据需要可以创建多台 CVM 实例，在 CVM 实例中部署 logstash 组件；
- 在创建好的CVM中安装Java8或以上版本。

### 部署 logstash
**1. 下载 logstash 组件包**（logstash 版本应该与 Elasticsearch 版本保持一致）
`wget https://artifacts.elastic.co/downloads/logstash/logstash-5.6.4.tar.gz`
**2. 解压 logstash 组件包**
`tar xvf logstash-5.6.4.tar.gz`
**3. 配置 logstash**
本示例以 nginx 日志为输入源，输出项配置为 Elasticsearch 集群的内网 VIP 地址和端口，
创建 test.conf 配置文件，文件内容如下：
```
input {
file {
path => "/var/log/nginx/access.log" # nginx 访问日志的路径
}
}
filter {
}
output {
elasticsearch {
hosts => ["http://172.16.0.89:9200"] # Elasticsearch集群的内网VIP地址和端口
index => "nginx_access-%{+YYYY.MM.dd}" # 自定义索引名称, 以日期为后缀，每天生成一个索引
}
}
```
**4. 启动 logstash**
进入 logstash 压缩包解压目录 logstash-5.6.4 下，执行以下命令，后台运行 logstash：
`nohup ./bin/logstash -f ~/test.conf 2>&1 >/dev/null &`

>**注意：**配置文件路径填写为自己创建的路径。

有关 logstash 的更多功能，请查看 [logstash 官方文档](https://www.elastic.co/products/logstash) 。
## 查询日志
1. 登录 Kibana 控制台；
2. 单击【Management】>【Index Patterns】， 添加名为`nginx_access*`的索引，Time Filter field name选择 `@timestamp`, 以实现根据时间搜索日志；

3. 进入 Discover 页面，选择`nginx_access*`索引项，即可检索到 nginx 的访问日志。

有关 Kibana 控制台的更多功能，请查看 [Kibana 官方文档](https://www.elastic.co/cn/products/kibana)。
