## Overview

Log collection feature allows users to collect logs in clusters, and send the log files to a specified Kafka Topic.

Log collection feature is applicable to users who need to store and analyze service logs in the Kubernetes cluster. Users can collect logs in the cluster by configuring log collection rules and send collected logs to a specified Topic of Kafka for consumption by other infrastructures of users.

You need to enable Log collection feature manually for each cluster. After it's enabled, log collection Agent is running in a form of Daemonset in the cluster. Users can configure the source and consumer end of logs using log collection rules. Log collection Agent collects logs from the configured source, and sends these logs to the consumer end specified by users.

## Application Scenarios

- [Collect Standard Output Logs in Container](https://cloud.tencent.com/document/product/457/13662)
- [Collect File Logs in CVM](https://cloud.tencent.com/document/product/457/13660)
- [Collect File Logs in Container](https://cloud.tencent.com/document/product/457/13661)
- [Configure Consumer End of Collected Logs](https://cloud.tencent.com/document/product/457/13659)

## Best Practice

Based on log collection feature, you can use Logstash and Elasticsearch to perform a visual retrieval of cluster service logs.

To provide log visualization capability, you are recommended to consume log data of Kafka using Logstash, and send log data to Elasticsearch cluster. View templates for building Elasticsearch and Logstash clusters in [Best Practice for Log Collection](https://cloud.tencent.com/document/product/457/13657).
 
## Concepts

- Log collection Agent: The Agent that CCS used to collect log information. it's developed based on Fluentd and runs in a form of Daemonset.

- Log collection rule: Users can use log collection rules to specify the source of logs and the location to which collected logs are sent. Log collection Agent monitors changes in log collection rules. Changed or new rules take effect within 10 seconds. Configuration of multiple log collection rules cannot lead to the creation of multiple Daemonsets. However, the log collection Agent may take up more resources if too many rules are configured.

- Source: It contains specified container logs and CVM path logs. To collect logs that are printed to standard output from services in the cluster, you can set the source to the specified container log, including setting whether to collect logs of all services or a number of specified service under the Namespace. To collect logs under specific paths in a cluster node, you can set the source to the CVM path log. For example, to collect logs under the paths in the format of `/var/lib/docker/containers/<container-id>/<container-id>.json-log`, you can specify the log collection path to `/var/lib/docker/containers/*/*.json-log`.

- Consumer end: Log collection Agent collects logs from the specified source and sends these logs to the consumer end specified by users. Log collection service support user-built Kakfa and Tencent Cloud Ckafka service as the consumer end of logs. Users only need to configure the Topic of the consumer end Kafka, and log collection Agent sends collected logs to the Topic specified by users in the format of json.


## Capabilities

Log collection feature primarily provides the following capabilities:

- Collection of container logs: Collect the standard output logs of specified services in Kubernetes cluster.
![Container Log Collector][1]

- Collection of CVM logs: Collect the file logs under the specified paths on Kubernetes cluster node.
![CVM Log Collector][2]

- Push collected logs to Tencent Cloud CKafka service

- Push collected logs to a specified Topic of user-built Kafka
![Illustration - Kafka Deployment Diagram][3]


[1]:https://mc.qcloudimg.com/static/img/11eac7b626d3d84f3b6417d8cbbddad9/image.jpeg
[2]:https://mc.qcloudimg.com/static/img/703ce5242f9d74a6ba40058d265698eb/image.jpeg
[3]:https://mc.qcloudimg.com/static/img/0fe6bed71772b09231771e320a789e9d/image.jpeg

