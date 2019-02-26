腾讯云 Elasticsearch Service 提供的实例包含 Elasticsearch 集群和 Kibana 控制台，其中 Elasticsearch 集群通过在用户 VPC 内的私有网络 VIP 地址+端口进行访问，Kibana 控制台提供外网地址供用户在浏览器端访问，至于数据源，当前只支持用户自行接入 Elasticsearch 集群。下面以最典型的日志分析架构 ELK 为例，介绍如何将用户的日志导入到 Elasticsearch, 并可以在浏览器访问 Kibana 控制台进行查询与分析。
## 安装部署 logstash

### 环境准备
* 用户需要创建和 Elasticsearch 集群在同一 VPC 的 CVM，根据需要可以创建多台 CVM 实例，在 CVM 实例中部署 logstash 组件；
* CVM 需要有 2G 以上内存；
* 在创建好的 CVM 中安装 Java8 或以上版本。


### 部署 logstash

1. 下载 logstash 组件包并解压
```
wget https://artifacts.elastic.co/downloads/logstash/logstash-5.6.4.tar.gz
tar xvf logstash-5.6.4.tar.gz
```
**logstash 版本应该与 Elasticsearch 版本保持一致。**

2. 配置 logstash
本示例以 nginx 日志为输入源，输出项配置为 Elasticsearch 集群的内网 VIP 地址和端口，
创建 test.conf 配置文件，文件内容如下：
```
input {
    file {
        path => "/var/log/nginx/access.log" # nginx 访问日志的路径
        start_position => "beginning" # 从文件起始位置读取日志，如果不设置则在文件有写入时才读取，类似于tail -f
        }
}
filter {
}
output {
  elasticsearch {
    hosts => ["http://172.16.0.145:9200"] # Elasticsearch集群的内网VIP地址和端口
    index => "nginx_access-%{+YYYY.MM.dd}" # 索引名称, 按天自动创建索引
 }
}
```
腾讯云 Elasticsearch 集群默认开启了允许自动创建索引配置，上述 test.conf 配置文件中的 nginx_access-%{+YYYY.MM.dd} 索引会自动创建，除非需要提前设置好索引中字段的 mapping，否则无需额外调用 Elasticsearch 的 API 创建索引。

3. 启动 logstash
进入 logstash 压缩包解压目录 logstash-5.6.4 下，执行以下命令，后台运行 logstash，注意配置文件路径填写为自己创建的路径。
```
nohup ./bin/logstash -f ~/test.conf 2>&1 >/dev/null &
```

查看 logstash-5.6.4 目录下的 logs 目录，确认 logstash 已经正常启动，正常启动的情况下会记录如下日志：
```
[2018-09-13T19:49:50,014][WARN ][logstash.runner          ] --config.debug was specified, but log.level was not set to 'debug'! No config info will be logged.
[2018-09-13T19:49:50,022][INFO ][logstash.modules.scaffold] Initializing module {:module_name=>"netflow", :directory=>"/root/logstash-5.6.4/modules/netflow/configuration"}
[2018-09-13T19:49:50,023][INFO ][logstash.modules.scaffold] Initializing module {:module_name=>"fb_apache", :directory=>"/root/logstash-5.6.4/modules/fb_apache/configuration"}
[2018-09-13T19:49:50,475][INFO ][logstash.outputs.elasticsearch] Elasticsearch pool URLs updated {:changes=>{:removed=>[], :added=>[http://172.16.0.145:9200/]}}
[2018-09-13T19:49:50,476][INFO ][logstash.outputs.elasticsearch] Running health check to see if an Elasticsearch connection is working {:healthcheck_url=>http://172.16.0.145:9200/, :path=>"/"}
[2018-09-13T19:49:50,564][WARN ][logstash.outputs.elasticsearch] Restored connection to ES instance {:url=>"http://172.16.0.145:9200/"}
[2018-09-13T19:49:50,604][INFO ][logstash.outputs.elasticsearch] Using mapping template from {:path=>nil}
[2018-09-13T19:49:50,607][INFO ][logstash.outputs.elasticsearch] Attempting to install template {:manage_template=>{"template"=>"logstash-*", "version"=>50001, "settings"=>{"index.refresh_interval"=>"5s"}, "mappings"=>{"_default_"=>{"_all"=>{"enabled"=>true, "norms"=>false}, "dynamic_templates"=>[{"message_field"=>{"path_match"=>"message", "match_mapping_type"=>"string", "mapping"=>{"type"=>"text", "norms"=>false}}}, {"string_fields"=>{"match"=>"*", "match_mapping_type"=>"string", "mapping"=>{"type"=>"text", "norms"=>false, "fields"=>{"keyword"=>{"type"=>"keyword", "ignore_above"=>256}}}}}], "properties"=>{"@timestamp"=>{"type"=>"date", "include_in_all"=>false}, "@version"=>{"type"=>"keyword", "include_in_all"=>false}, "geoip"=>{"dynamic"=>true, "properties"=>{"ip"=>{"type"=>"ip"}, "location"=>{"type"=>"geo_point"}, "latitude"=>{"type"=>"half_float"}, "longitude"=>{"type"=>"half_float"}}}}}}}}
[2018-09-13T19:49:50,618][INFO ][logstash.outputs.elasticsearch] Installing elasticsearch template to _template/logstash
[2018-09-13T19:49:50,666][INFO ][logstash.outputs.elasticsearch] New Elasticsearch output {:class=>"LogStash::Outputs::ElasticSearch", :hosts=>["http://172.16.0.145:9200"]}
[2018-09-13T19:49:50,670][INFO ][logstash.pipeline        ] Starting pipeline {"id"=>"main", "pipeline.workers"=>4, "pipeline.batch.size"=>125, "pipeline.batch.delay"=>5, "pipeline.max_inflight"=>500}
[2018-09-13T19:49:50,807][INFO ][logstash.pipeline        ] Pipeline main started
[2018-09-13T19:49:50,855][INFO ][logstash.agent           ] Successfully started Logstash API endpoint {:port=>9600}

```

有关 logstash 的更多功能，请查看 [elastic 官方文档](https://www.elastic.co/products/logstash)。

## 查询日志

1. 在腾讯云 Elasticsearch Service 控制台集群列表页中，单击实例右侧的 Kibana 按钮，进入  Kibana 控制台。
![](https://main.qcloudimg.com/raw/a99bb629ecefb620669bf5cc649e4e3d.png)

2. 进入 【Management】>【Index Patterns】，添加名为"nginx_access*"的索引。
![](https://main.qcloudimg.com/raw/b9aca384cf66b074fcfcd3ef4ae62d85.png)

3. 进入 Discover 页面，选择"nginx_access*"索引项，已经可以检索到 nginx 的访问日志了。
![](https://main.qcloudimg.com/raw/cfa7444ebde8df0f2b5661e2fc0288b6.png)

有关 Kibana 控制台的更多功能，请查看 [elastic 官方文档](https://www.elastic.co/products/kibana)。
