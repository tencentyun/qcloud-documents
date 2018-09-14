# 使用 ELK 构建日志分析系统
腾讯云Elasticsearch Service提供的实例包含Elasticsearch集群和Kibana控制台，其中Elasticsearch集群通过在用户VPC内的私有网络vip地址+端口进行访问，Kibana控制台提供外网地址供用户在浏览器端访问，至于数据源，当前只支持用户自行接入Elasticsearch集群。下面以最典型的日志分析架构ELK为例，介绍如何将用户的日志导入到Elasticsearch, 并可以在浏览器访问kibana控制台进行查询与分析。
## 安装部署logstash

### 环境准备
* 用户需要创建和Elasticsearch集群在同一VPC的CVM，根据需要可以创建多台CVM实例，在CVM实例中部署logstash组件
* CVM需要有2G以上内存
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

需要注意的是, 腾讯云Elasticsearch集群默认开启了允许自动创建索引配置，上述test.conf配置文件中的nginx_access-%{+YYYY.MM.dd}索引会自动创建，除非需要提前设置好索引中字段的mapping，否则无需额外调用Elasticsearch的API创建索引。

3  启动logstash

进入logstash压缩包解压目录logstash-5.6.4下，执行一下命令，后台运行logstash, 注意配置文件路径填写为自己创建的路径


```
nohup ./bin/logstash -f ~/test.conf 2>&1 >/dev/null &
```

查看logstash-5.6.4目录下的logs目录，确认logstash已经正常启动，正常启动的情况下会记录如下日志：

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

有关logstash的更多功能，请查看官方文档了解：[!https://www.elastic.co/products/logstash]

## 查询日志

1. 在腾讯云Elasticsearch Service控制台集群列表页中，点击实例右侧的kibana按钮，进入kibana控制台
![](https://main.qcloudimg.com/raw/a99bb629ecefb620669bf5cc649e4e3d.png)
2. 进入Management->Index Patterns, 添加名为"nginx_access*"的索引
![](https://main.qcloudimg.com/raw/b9aca384cf66b074fcfcd3ef4ae62d85.png)
3. 进入Discover页面，选择"nginx_access*"索引项，已经可以检索到nginx的访问日志了
![](https://main.qcloudimg.com/raw/cfa7444ebde8df0f2b5661e2fc0288b6.png)
有关Kibana控制台的更多功能，请查看官方文档了解：[!https://www.elastic.co/products/kibana]
