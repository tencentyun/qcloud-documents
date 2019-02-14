## 概述
[Beats 平台](https://www.elastic.co/cn/products/beats) 集合了多种单一用途数据采集器。这些采集器安装后可用作轻量型代理，从成百上千或成千上万台机器向目标发送采集数据。
![](https://main.qcloudimg.com/raw/e48ad4b5a9d1d4576bbb5f574125b8aa.png)
Beats 有多种采集器，您可以根据自身的需求下载对应的采集器。
![](https://main.qcloudimg.com/raw/3aa511c2723ba53fbed1b5c6d1e6a228.png)


## 配置文件
```
#======= Filebeat prospectors ==========

filebeat.prospectors:

- input_type: log 

# 此处为监听文件路径
  paths:
    - /var/log/messages

#=======  Outputs =========

#------------------ kafka -------------------------------------
output.kafka:
  # 设置为实例地址
  hosts: ["127.1.2.3:9092"]
  # 设置目标topic
  topic: 'test'
  partition.round_robin:
    reachable_only: false

  required_acks: 1
  compression: none
  max_message_bytes: 1000000

  # sasl需要配置下列信息，如果不需要则下面两个选项可不配置
  username: "instance-will#user"
  password: "password"
```

## 运行
1. 运行以下命令，启动客户端。
`sudo ./filebeat -e -c filebeat.yml `
2. 为监控文件增加数据（示例为写入监听的 testlog 文件）。
```
echo ckafka1 >> testlog
echo ckafka2 >> testlog
echo ckafka3 >> testlog
```
3. 开启 Consumer 消费对应的 Topic，获得以下数据。
```
{"@timestamp":"2017-09-29T10:01:27.936Z","beat":{"hostname":"10.193.9.26","name":"10.193.9.26","version":"5.6.2"},"input_type":"log","message":"ckafka1","offset":500,"source":"/data/ryanyyang/hcmq/beats/filebeat-5.6.2-linux-x86_64/testlog","type":"log"}
{"@timestamp":"2017-09-29T10:01:30.936Z","beat":{"hostname":"10.193.9.26","name":"10.193.9.26","version":"5.6.2"},"input_type":"log","message":"ckafka2","offset":508,"source":"/data/ryanyyang/hcmq/beats/filebeat-5.6.2-linux-x86_64/testlog","type":"log"}
{"@timestamp":"2017-09-29T10:01:33.937Z","beat":{"hostname":"10.193.9.26","name":"10.193.9.26","version":"5.6.2"},"input_type":"log","message":"ckafka3","offset":516,"source":"/data/ryanyyang/hcmq/beats/filebeat-5.6.2-linux-x86_64/testlog","type":"log"}
```


### SASL/PLAINTEXT 模式
如果您需要进行 SALS/PLAINTEXT 配置，则需要配置用户名与密码。 在 Kafka 配置区域新增加 username 和 password 配置即可。
```
# sasl需要配置下列信息，如果不需要则下面两个选项可不配置
  username: "instance-will#user"
  password: "password"
```
