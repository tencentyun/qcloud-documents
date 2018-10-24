## Overview

Log collection feature allows users to collect logs in clusters, and send the log files to a specified Kafka Topic or CLS's specified log topic.

Log collection feature is applicable to users who need to store and analyze service logs in the Kubernetes cluster. Users can collect logs in the cluster by configuring log collection rules and send collected logs to a specified Topic of Kafka or CLS's specified log topic for consumption by other infrastructures of users.

You need to enable Log collection feature manually for each cluster. After it's enabled, log collection Agent is running in a form of Daemonset in the cluster. Users can configure the source and consumer of logs using log collection rules. Log collection Agent collects logs from the configured source, and sends these logs to the consumer specified by users.

Please note that to use log collection feature, nodes in the Kubernetes clusters should be able to access log consumer.

## Application Scenarios

- [Collect Standard Output Logs in Container](https://cloud.tencent.com/document/product/457/13662)
- [Collect File Logs in CVM](https://cloud.tencent.com/document/product/457/13660)
- [Collect File Logs in Container](https://cloud.tencent.com/document/product/457/13661)
- [Configure Consumer of Collected Logs](https://cloud.tencent.com/document/product/457/13659)

## Best Practice

Based on log collection feature, you can use Logstash and Elasticsearch to perform a visual retrieval of cluster service logs.

To provide log visualization capability, you are recommended to consume log data of Kafka using Logstash, and send log data to Elasticsearch cluster. View templates for building Elasticsearch and Logstash clusters in [Best Practice for Log Collection](https://cloud.tencent.com/document/product/457/13657).
 
## Concepts

- Log collection Agent: The Agent that TKE used to collect log information. it's developed based on Fluentd and runs in a form of Daemonset.

- Log collection rule: Users can use log collection rules to specify the source of logs and the location to which collected logs are sent. Log collection Agent monitors changes in log collection rules. Changed or new rules take effect within 10 seconds. Configuration of multiple log collection rules cannot lead to the creation of multiple Daemonsets. However, the log collection Agent may take up more resources if too many rules are configured.

- Source: It contains specified container logs and CVM path logs. To collect logs that are printed to standard output from services in the cluster, you can set the source to the specified container log, including setting whether to collect logs of all services or a number of specified service under the Namespace. To collect logs under specific paths in a cluster node, you can set the source to the CVM path log. For example, to collect logs under the paths in the format of `/var/lib/docker/containers/<container-id>/<container-id>.json-log`, you can specify the log collection path to `/var/lib/docker/containers/*/*.json-log`.

- Consumer: Log collection Agent collects logs from the specified source and sends these logs to the consumer specified by users. Log collection service support user-built Kakfa, Tencent Cloud Ckafka and CLS as the consumer of logs. Users only need to configure the consumer Kafka or CLS, and log collection Agent sends collected logs to the specified consumer in the format of json.


## Capabilities

Log collection feature primarily provides the following capabilities:

- Collection of container logs: Collect the standard output logs of specified services in Kubernetes cluster.
![Container Log Collector][1]

- Collection of CVM logs: Collect the file logs under the specified paths on Kubernetes cluster node.
![CVM Log Collector][2]

- Push collected logs to Tencent Cloud CKafka service
![Ckafka Configurations][3]

- Push collected logs to a specified Topic of user-built Kafka
![Kafka Configurations][4]

- Push collected logs to Tencent Cloud CLS
![CLS Configurations][5]

[1]:https://mc.qcloudimg.com/static/img/1876f68db6e7f0282c1289d1a7411211/image.png
[2]:https://mc.qcloudimg.com/static/img/45465494725a520f963be72ae3fb9aca/image.png
[3]:https://mc.qcloudimg.com/static/img/2247389b857b20cceabd0c6dccdbcc8a/ckafa.png
[4]:https://mc.qcloudimg.com/static/img/9fb478a794d258a0609db74ae3ede544/kafka.png
[5]:https://mc.qcloudimg.com/static/img/4d52a836e1c50cbe46fb7d8d4049bf8a/%7BF5CD3AB9-4732-44E0-85BF-1103EB970862%7D.png
