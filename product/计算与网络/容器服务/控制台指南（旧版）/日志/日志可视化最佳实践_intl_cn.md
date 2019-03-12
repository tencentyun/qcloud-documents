## 日志可视化最佳实践

为提供日志的可视化能力，用户可以使用 logstash 消费 kafka 的日志数据，并将日志数据发送到 elasticsearch 集群，以进行可视化检索和分析，此处提供 elasticsearch 集群的搭建教程.

## 搭建 Elasticsearch 集群（请保证集群有足够的可用资源）

用户可以直接使用容器服务提供的 elasticsearch 基础模板搭建 elasticsearch 集群和 kibana，直接在集群内节点上使用如下命令即可。

	git clone https://github.com/tencentyun/ccs-elasticsearch-template.git /tmp/kubernetes-elasticsearch
	cd kubernetes-elasticsearch
	kubectl create -f es-svc.yaml
	kubectl create -f es-client.yaml
	kubectl create -f es-data.yaml
	kubectl create -f es-discovery-svc.yaml
	kubectl create -f es-master.yaml
	kubectl create -f kibana-svc.yaml
	kubectl create -f kibana.yaml


## 搭建 Logstash 消费 Kafka 指定 Topic 数据

可以直接使用容器服务提供的 logstash 基础模板搭建 logstash 消费 kafka 数据并将数据发送至 elasticsearch，搭建前请先将 /tmp/kubernetes-elasticsearch/logstash-config.yaml 中的 `bootstrap_servers` 以及 `elasticsearch` 中的 `hosts` 修改为 kafka 和 elasticsearch 的地址。

	kubectl create -f logstash-consumer.yaml


## 创建 elasticsearch 索引

使用 kibana 进行日志检索前，需要先创建索引。

![][1]

## 查看日志数据

![][2]

[1]:https://mc.qcloudimg.com/static/img/da4ea19aa75ffbf94b38e39a6e781082/ccs-log.jpeg
[2]:https://mc.qcloudimg.com/static/img/a233130efb256ef5836b294e9ec65a35/ccs-log-visual.jpeg