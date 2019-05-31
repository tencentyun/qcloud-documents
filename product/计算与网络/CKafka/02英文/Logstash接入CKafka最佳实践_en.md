## Introduction to Logstash
Logstash, an open-source log processing tool, is used to collect data from multiple sources, filter the collected data, and store the data for other purposes.

Logstash is highly flexible and features a powerful syntax analysis capability with a variety of plugs-ins. It also supports multiple input/output sources. In addition, as a horizontally scalable data pipeline, it is powerful in log collection and retrieval by coordinating with Elasticsearch and Kibana.

### How Does Logstash Work
Logstash data processing can be divided into three stages: inputs → filters → outputs.
1. inputs - Generate data sources, such as file, syslog, redis, and beats.
2. filter - Modify and filter data, which belongs to the intermediate process in Logstash data pipeline. You can change events based on specific conditions. Some common filters include grok, mutate, drop and clone.
3. outputs - Transfer data to other locations. An event can be transferred to multiple outputs, and it ends when the transfer is completed. Elasticsearch is the most common output.

Besides, Logstash supports encoding/decoding, and you can specify the format on the inputs/outputs side.

![](https://mc.qcloudimg.com/static/img/17f1ac23a158b043091ebf48071f3a78/00.png)

## Why Logstash + Kafka

![](https://mc.qcloudimg.com/static/img/bb8a396b1953ed487776281ef616a5c8/11.png)

1. You can asynchronously process data to prevent burst traffic.
2. In the process of decoupling, when an exception occurs in Elasticsearch, the upstream work is not affected.
3. Filtering data using Logstash consumes resources. The performance of Logstash may be affected if it is deployed on the production server.

## Connecting CKafka
### Supported Version
#### inputs
The compatibility of official version is described below:
![](https://mc.qcloudimg.com/static/img/7a25c5c3381a9f615701e88964ee8204/22.png)

The latest version for now is v5.1.8, which uses 0.10 Consumer API to read data.

For more information on parameter configuration, please see https://www.elastic.co/guide/en/logstash/current/plugins-inputs-kafka.html.
#### outputs
The compatibility of official version is described below:

![](https://mc.qcloudimg.com/static/img/bd2ca98c3b0d392abe77a337450bb132/33.png)

The latest version for now is v5.1.7, which uses 0.10 Consumer API to produce data.

For more information on parameter configuration, please see https://www.elastic.co/guide/en/logstash/current/plugins-outputs-kafka.html.
### Preparations
- Java version: java 8
- Logstash version: 5.5.2 (August 17, 2017)
- Apply for a Ckafka instance, and create a corresponding topic
### Creation of CKafka
1. After the application for instance is approved, you can see the information of your instance from the console.
![](https://mc.qcloudimg.com/static/img/67f19ef17a73e768fba188d58ae08f9a/44.png)
2. By clicking the instance name, you can see the specific information of assigned instance.
![](https://mc.qcloudimg.com/static/img/3841d4eb19ad992d35e60196b38498ce/55.png)
3. Click "Topic Management" to create a topic, where the name is **logstash_test**.
![](https://mc.qcloudimg.com/static/img/30a006c20b8a9ba0a644336d5ddc501a/66.png)

Now, the operating environment of CKafka has been created.

### Connecting CKafka as "inputs"
1. Run bin/logstash-plugin list to check whether logstash-input-kafka is contained in the supported plugs-in.
![](https://mc.qcloudimg.com/static/img/c5c876ea5ae5ce75307a5e307357e622/input1.png)

2. Write the configuration file "input.conf".

*Here, standard output is taken as the key data, and Kafka is used as the data source*

![](https://mc.qcloudimg.com/static/img/06110a14d01ef395424acf4403188ce3/input2.png)

3. Launch Logstash to consume message.
![](https://mc.qcloudimg.com/static/img/5c58f08f2fd0fff052cab655d00d4133/input3.png)

*You can see that the data in the topic above has been consumed out now.*

For more information on parameter configuration when Kafka is used as output, please see https://www.elastic.co/guide/en/logstash/current/plugins-inputs-kafka.html#plugins-inputs-kafka-auto_offset_reset.

### Connecting CKafka as "outputs"
1. Run bin/logstash-plugin list to check whether logstash-output-kafka is contained in the supported plugs-in.
![](https://mc.qcloudimg.com/static/img/c5c876ea5ae5ce75307a5e307357e622/77.png)

2. Write the configuration file "output.conf".

*Here, standard input is taken as the data source, and Kafka is used as the data destination.*

![](https://mc.qcloudimg.com/static/img/661484fed328739fd12bedda0f5e2e67/88.png)

3. Launch Logstash to produce message.
![](https://mc.qcloudimg.com/static/img/c95bbc69c3f0ca36fa42efbb911b0a36/99.png)

4. Verify the data produced just now.
![](https://mc.qcloudimg.com/static/img/ae85758a90a497235a90511770f959d2/10.png)

For more information on parameter configuration when Kafka is used as output, please see https://www.elastic.co/guide/en/logstash/current/plugins-outputs-kafka.html.





