Curator是Elastic官方发布的一个管理Elasticsearch索引的工具，可以完成许多索引生命周期的管理工作，如清理创建时间超过7天的索引，每天定时备份指定的索引，定时将索引从热节点迁移至冷节点等等。更多支持的操作，可查看官方文档的[Action](https://www.elastic.co/guide/en/elasticsearch/client/curator/current/actions.html)列表。

Curator提供了一个命令行CLI工具，可以通过参数配置要执行的任务。Curator还提供了完善的Python API，这样就可以和腾讯云无服务云函数做结合，例如，[使用Curator在腾讯云Elasticsearch中自动删除过期数据](https://cloud.tencent.com/developer/article/1361207)，腾讯云无服务函数配置了Curator的模板，用户应用模板后进行简单的参数配置即可运行。更多的腾讯云无服务器函数的使用方法可以参考官网[文档](https://cloud.tencent.com/document/product/583)。

# Curator用法示例

下面将以定时删除历史过期索引为例，展示如何配置运行Curator。

## 安装

在腾讯云Elasticsearch集群对应的VPC下购买一台CVM，通过pip安装curator包

```
pip install elasticsearch-curator
```

## 以命令行参数方式运行

```
curator_cli --host 10.0.0.2:9200 --http_auth user:passwd delete_indices --filter_list '[{"filtertype": "pattern", "kind": "prefix", "value": "logstash-"}, {"filtertype": "age", "source": "name", "direction": "older", "timestring": "%Y.%m.%d", "unit": "days", unit_count: 7}]'
```
上述命令会过滤索引名称匹配logstash-20xx-xx-xx格式且时间为7天前的索引，然后将这些索引删除。
> 注意：上述的示例代码会执行删除操作清楚您的数据，请小心的确认上述语句已经在非生产环境中进行了测试。可以增加```--dry-run```参数进行测试，避免实际删除数据。

## 以配置文件方式运行

如您的操作比较复杂，参数太多或不想使用命令行参数，可以将参数放在配置文件中执行。

```
curator_cli --config PATH
```
在指定的config目录下，需要编辑[config.yml](https://www.elastic.co/guide/en/elasticsearch/client/curator/5.6/configfile.html)和[action.yml](https://www.elastic.co/guide/en/elasticsearch/client/curator/current/actionfile.html?spm=a2c4g.11186623.2.15.246a2001E6EWcE)两个配置文件。

## 定时执行

如需要定时执行，可以将命令配置到linux系统的crontab中。另，也可以直接使用上面提到的腾讯云无服务器云函数的定时触发功能。

## 使用API
Python API的使用可参考[文档](https://curator.readthedocs.io/en/latest/)。
