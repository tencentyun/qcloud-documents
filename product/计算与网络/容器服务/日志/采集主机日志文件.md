## 文件日志收集

日志收集功能支持收集 kubernetes 集群内所有节点的指定主机路径的日志，用户可以根据自己的需求，灵活的配置所需的路径，日志收集 Agent 会收集集群内所有节点上满足指定路径规则的文件日志。收集到的日志信息将会以 json 格式输出到用户指定的输出端，并会附加用户指定的 metadata，包括日志来源文件的路径和用户自定义的 metadata。


## 配置方法

1. 创建日志收集规则
![][1]

2. 指定文件采集源路径并添加自定义的 Metadata(可选)
![][2]

3. 指定日志接收端
![][3]

4. 查看接收到的日志
![][4]

## 日志收集路径

用户可以通过指定日志文件的路径来收集集群内节点上相应路径的日志文件，路径支持文件路径和通配规则，如 `/var/log/nginx.log` 或 `/var/lib/docker/containers/*/*.log`。


## Metadata 

用户可以为收集到的日志附加用户指定的 Key-Value 形式的 Metadata，用做日志信息的 Metadata 标记，附加 Metadata 将会以 json field 的形式添加到日志记录中。

例如，当不添加 Metadata 时，收集到的日志为
![][5]

当用户指定附加 metadata 时，收集到的日志为
![][6]

[1]:https://mc.qcloudimg.com/static/img/393ad1a2a9575cd89f1f0a38279bf676/image.jpeg
[2]:https://mc.qcloudimg.com/static/img/412208e6d73427f1c4e12002816be730/image.jpeg
[3]:https://mc.qcloudimg.com/static/img/0fe6bed71772b09231771e320a789e9d/image.jpeg
[4]:https://mc.qcloudimg.com/static/img/32f72a65f46f33d67a93d1a9a3f3e3d1/image.jpeg
[5]:https://mc.qcloudimg.com/static/img/8c3e54d7de5023dc10666ea14f5dcadb/hostlog.jpeg
[6]:https://mc.qcloudimg.com/static/img/32f72a65f46f33d67a93d1a9a3f3e3d1/hostlogwithmetadata.jpeg



