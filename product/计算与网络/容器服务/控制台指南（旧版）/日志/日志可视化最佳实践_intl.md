## Best Practice for Log Visualization

You can use Logstash to consume log data of Kafka, and send the log data to Elasticsearch cluster for visual retrieval and analysis of logs. Here, we provide a tutorial on how to build Elasticsearch cluster.

## Building Elasticsearch Cluster (make sure that there are sufficient resources available in the cluster)

You can directly use the basic template of Elasticsearch provided by TKE to build Elasticsearch cluster and Kibana. The following command can be used directly on the node in the cluster.

	git clone https://github.com/tencentyun/ccs-elasticsearch-template.git /tmp/kubernetes-elasticsearch
	cd kubernetes-elasticsearch
	kubectl create -f es-svc.yaml
	kubectl create -f es-client.yaml
	kubectl create -f es-data.yaml
	kubectl create -f es-discovery-svc.yaml
	kubectl create -f es-master.yaml
	kubectl create -f kibana-svc.yaml
	kubectl create -f kibana.yaml


## Building Logstash to Consume Data in the Specified Topic of Kafka

You can directly use the basic template of Logstash provided by TKE to build Logstash to consume data of Kafka and send the data to Elasticsearch. Before building, you need to change `bootstrap_servers` in `/tmp/kubernetes-elasticsearch/logstash-config.yaml` and `hosts` in `elasticsearch` to the addresses of Kafka and Elasticsearch, respectively.

	kubectl create -f logstash-consumer.yaml


## Creating Elasticsearch Index

Before performing log retrieval using Kibana, you need to create an index first.

![][1]

## Viewing Log Data

![][2]

[1]:https://mc.qcloudimg.com/static/img/da4ea19aa75ffbf94b38e39a6e781082/ccs-log.jpeg
[2]:https://mc.qcloudimg.com/static/img/a233130efb256ef5836b294e9ec65a35/ccs-log-visual.jpeg
