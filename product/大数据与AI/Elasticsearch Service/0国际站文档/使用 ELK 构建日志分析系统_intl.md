# Building a Log Analysis System with ELK
Instances provided by Tencent Cloud Elasticsearch Service include Elasticsearch clusters and the Kibana console. The Elasticsearch cluster is accessed through a "VIP address + port" within your VPC, and the Kibana console can be accessed from your browser using a public network address. As for data source, you are only allowed to access the Elasticsearch cluster on your own. Taking the most typical log analysis architecture ELK as an example, the following describes how to import your logs into Elasticsearch and access the Kibana console through your browser for query and analysis.
## Installing and Deploying Logstash

### Environment
* Create a CVM instance in the same VPC as your Elasticsearch cluster. If needed, create multiple CVM instances and deploy the Logstash component in each of them.
* Install Java 8 or above on the created CVMs.

### Deploy Logstash

1. Download the Logstash package and unzip it.

```
wget https://artifacts.elastic.co/downloads/logstash/logstash-5.6.4.tar.gz
tar xvf logstash-5.6.4.tar.gz
```
Note that the Logstash version should be matched with the Elasticsearch version.

2. Configure Logstash

The following example uses the nginx log as the input source, and the output is configured as the private VIP address and port of the Elasticsearch cluster.
Create the test. conf configuration file with the following contents:


```
input {
    file {
        path => "/var/log/nginx/access.log" # nginx  log path
        }
}
filter {
}
output {
  elasticsearch {
    hosts => ["http://172.16.0.89:9200"] # Elasticsearch cluster's private VIP address and port
    index => "nginx_access-%{+YYYY.MM.dd}" # custom index name
 }
}
```

3. Start Logstash

Enter the directory logstash-5.6.4 where you unzip the Logstash package, execute the command and run Logstash in the background. Please enter the path customized by yourself as the path to the configuration file.


```
nohup ./bin/logstash -f ~/test.conf 2>&1 >/dev/null &
```
For more features of Logstash, see its official documentation: [!https://www.elastic.co/products/logstash]

## Query Logs

1. Enter the Kibana console, go to **Management** -> **Index Patterns**, and add an index named "nginx_access*".
![](https://main.qcloudimg.com/raw/8090d4da5785cd17fa802176dbb2c7b1.png)
2. Enter the Discover page and select the index item "nginx_access*". You can then retrieve the nginx's access log.
![](https://main.qcloudimg.com/raw/cfa7444ebde8df0f2b5661e2fc0288b6.png)
For more features of the Kibana console, see its official documentation: [!https://www.elastic.co/products/kibana]

