## 背景介绍
用户可以将自己的日志、数据等信息通过多种采集组件输入到 CKafka 等产品中，作为数据源被流计算 Oceanus 来消费和处理。

例如，用户可以通过 Apache Flume 提供的 Agent，将日志、事件等数据源源源不断地从各个节点传输到 CKafka 产品中，整体流程如下图：
![数据导入示意图](https://main.qcloudimg.com/raw/ff2d49211dc0cc01388f88dd14306a43.png)

## Apache Flume 数据采集操作指南

请参见 CKafka 产品文档中 [Flume 接入 CKafka 最佳实践](https://cloud.tencent.com/document/product/597/10777)。

## Logstash 数据采集操作指南

请参见 CKafka 产品文档中 [Logstash 接入 CKafka 最佳实践](https://cloud.tencent.com/document/product/597/11487)。

## Filebeat 数据采集操作指南

这里介绍使用 Filebeat 将日志文件导入 CKafka 的方式。

### 1. 下载 Filebeat 并安装
在官网 [Filebeat 下载](https://www.elastic.co/cn/downloads/beats/filebeat) 页面，选择适合自己操作系统的 Filebeat 安装包，下载并安装到需要采集日志的主机上。以下默认用户使用的是 Linux 版本系统，且使用官方的安装包（rpm、deb）。
### 2. 配置 YAML 文件
对于 Linux 系统，Filebeat 默认安装后的配置文件位于`/etc/filebeat/filebeat.yml`。为了简单起见，我们选择直接编辑这个文件。
1. 采集的文件位于`/var/log/`目录下，以 world- 前缀开头，以 .log 后缀结尾，命令如下：
![日志文件列表](https://main.qcloudimg.com/raw/6c622d3c49bd421e1fcda3c9253c910e.jpg)
2. 日志文件：每条日志可能有多行，但是每行的开头一定是2019-09-23这样的年-月-日数字格式，格式如下：
![](https://main.qcloudimg.com/raw/2c11d552c5e9c1f78c40417660287811.jpg)

那么可以将上述的 `/etc/filebeat/filebeat.yml` 替换为如下内容：

```yaml
filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /var/log/hello/world-*.log 	# 日志文件的路径, 路径支持通配符 *, 自动发现新增的日志
  multiline.pattern: '^\d{4}-\d{2}-\d{2}'	# 每条日志的起始格式（正则表达式）, 根据实际情况进行调整
  multiline.negate: true
  multiline.match: after
  exclude_lines: ['DEBUG']			# 排除含有 DEBUG 字符串的行, 避免采集到大量调试日志
output.kafka:
  enabled: true
  hosts: ["10.0.0.1:9092"]			# CKafka 的上报 IP 和端口，可以在 CKafka 的详情页查看
  topic: '您要导入的 CKafka Topic'	 # 请先在 CKafka 中创建 Topic 并在这里填写
  partition.hash:
    hash: ['beat.hostname']
    reachable_only: false
    random: true
  required_acks: 1
  compression: gzip
  version: 0.10.2.1
  max_message_bytes: 10000
  timeout: 10
```

更多的参数和解释，请参见 Filebeat 官网的 [配置 Kafka 输出](https://www.elastic.co/guide/en/beats/filebeat/master/kafka-output.html)。

配置完成后，运行如下命令来启动 Filebeat 采集服务。随后即可通过消费数据导入的 CKafka Topic 来查看日志是否已经成功被采集。如果采集成功，则可以用于流计算的后续处理。
```bash
service filebeat start
```
查看 Filebeat 的运行日志时，运行如下命令，以判断 Filebeat 的上报是否遇到了问题。
```bash
tail -f /var/log/filebeat/filebeat
```


