Curator 是 Elastic 官方发布的一个管理 Elasticsearch 索引的工具，可以完成许多索引生命周期的管理工作，例如清理创建时间超过7天的索引、每天定时备份指定的索引、定时将索引从热节点迁移至冷节点等等。更多 Curator 支持的操作，可查看官方文档的 [功能](https://www.elastic.co/guide/en/elasticsearch/client/curator/current/actions.html) 列表。

Curator 提供了一个命令行 CLI 工具，可以通过参数配置要执行的任务。Curator 还提供了完善的 Python API，这样就可以和腾讯云无服务云函数做结合，例如 [使用 Curator 在腾讯云 Elasticsearch 中自动删除过期数据](https://cloud.tencent.com/developer/article/1361207)，腾讯云无服务云函数配置了 Curator 的模板，用户应用模板后进行简单的参数配置即可运行。更多的腾讯云无服务器云函数的使用方法可以参考 [云函数](https://cloud.tencent.com/document/product/583)。

## Curator 用法示例
下面将以定时删除历史过期索引为例，展示如何配置运行 Curator。

### 安装
在腾讯云 Elasticsearch 集群对应的 VPC 下购买一台 CVM，通过 pip 安装 curator 包。
```
pip install elasticsearch-curator
```

### 以命令行参数方式运行
下面的命令会过滤索引名称匹配 logstash-20xx-xx-xx 格式且时间为7天前的索引，然后将这些索引删除。
>!示例代码会执行删除操作清除您的数据，请谨慎确认上述语句已经在非生产环境中进行了测试。可以增加 ` --dry-run ` 参数进行测试，避免实际删除数据。
>
```
curator_cli --host 10.0.0.2:9200 --http_auth 'user:passwd' delete-indices --filter_list '[{"filtertype": "pattern", "kind": "prefix", "value": "logstash-"}, {"filtertype": "age", "source": "name", "direction": "older", "timestring": "%Y.%m.%d", "unit": "days", unit_count: 7}]'
```

### 以配置文件方式运行
如您的操作比较复杂，参数太多或不想使用命令行参数，可以将参数放在配置文件中执行。
在指定的 config 目录下，需要编辑 [config.yml](https://www.elastic.co/guide/en/elasticsearch/client/curator/5.6/configfile.html) 和 [action.yml](https://www.elastic.co/guide/en/elasticsearch/client/curator/current/actionfile.html?spm=a2c4g.11186623.2.15.246a2001E6EWcE) 两个配置文件。
```
curator_cli --config PATH
```

### 定时执行
如需要定时执行，可以将命令配置到 Linux 系统的 crontab 中，也可以直接使用上面提到的腾讯云云函数的定时触发功能。

### 使用 API
Python API 的使用可参考 [文档](https://curator.readthedocs.io/en/latest/)。
