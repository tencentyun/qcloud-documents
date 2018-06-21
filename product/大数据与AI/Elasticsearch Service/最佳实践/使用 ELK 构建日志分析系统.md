# 使用 ELK 构建日志分析系统
腾讯云Elasticsearch Service提供的实例包含Elasticsearch集群和Kibana控制台，其中Elasticsearch集群通过在用户VPC内的私有网络vip地址+端口进行访问，Kibana控制台提供外网地址供用户在浏览器端访问，至于数据源，当前只支持用户自行接入Elasticsearch集群。下面以最典型的日志分析架构ELK为例，介绍如何将用户的日志导入到Elasticsearch, 并可以在浏览器访问kibana控制台进行查询与分析。
## 安装部署logstash

### 环境准备
* 用户需要创建和Elasticsearch集群在同一VPC的CVM，根据需要可以创建多台CVM实例，在CVM实例中部署logstash组件
* 在创建好的CVM中安装Java8或以上版本

### 部署logstash

1  下载logstash组件包并解压

```
wget https://artifacts.elastic.co/downloads/logstash/logstash-5.6.4.tar.gz
tar xvf logstash-5.6.4.tar.gz
```
需要注意logstash版本应该与Elasticsearch版本保持一致

2  配置logstash

本示例以nginx日志为输入源，输出项配置为Elasticsearch集群的内网VIP地址和端口，
创建test.conf配置文件，文件内容如下：


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
    index => "nginx_access-%{+YYYY.MM.dd}" # 自定义索引名称
 }
}
```

3  启动logstash

进入logstash压缩包解压目录logstash-5.6.4下，执行一下命令，后台运行logstash, 注意配置文件路径填写为自己创建的路径


```
nohup ./bin/logstash -f ~/test.conf 2>&1 >/dev/null &
```
有关logstash的更多功能，请查看官方文档了解：[!https://www.elastic.co/products/logstash]

## 查询日志

1. 进入kibana控制台，进入Management->Index Patterns, 添加名为"nginx_access*"的索引
![](https://main.qcloudimg.com/raw/8090d4da5785cd17fa802176dbb2c7b1.png)
2. 进入Discover页面，选择"nginx_access*"索引项，已经可以检索到nginx的访问日志了
![](https://main.qcloudimg.com/raw/cfa7444ebde8df0f2b5661e2fc0288b6.png)
有关Kibana控制台的更多功能，请查看官方文档了解：[!https://www.elastic.co/products/kibana]
