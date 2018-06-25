## 采集容器内路径日志

日志采集服务当前不支持直接采集容器内文件系统的日志文件，当需要采集容器内某路径的日志时，用户需要将指定的日志文件所在目录以 host path volume 的形式挂载至主机的指定路径，然后使用采集主机日志文件的功能采集相应的主机路径。

## 配置方法

例如，应用将日志文件打印至容器内文件系统路径 `/data/app-log/nginx/access.log`，可以如下配置日志收集规则。

1. 创建应用时将容器内日志文件所在路径`/data/app-log/nginx`挂载至主机路径`/var/log/nginx`。
![][1]
![][2]

2. 创建日志收集器并指定采集路径为 `/var/log/nginx/*.log `，并指定附加的 metadata (可选)。
![][3]

3. 指定日志的接收端。
![][4]

4. 消费 kafka 的相关 topic 查看收集到的日志。
![][5]

[1]:https://mc.qcloudimg.com/static/img/f260d93e0c77c2021543a0353b171d7e/image.jpeg
[2]:https://mc.qcloudimg.com/static/img/6a7219a31ac56be11b21fbcc23f6ef88/image.jpeg
[3]:https://mc.qcloudimg.com/static/img/8b5594d5bd36c4ee28f769fe1bc86301/4VA%7D2PX0SYKF%60B2P%7ENTICQG.png
[4]:https://mc.qcloudimg.com/static/img/0fe6bed71772b09231771e320a789e9d/image.jpeg
[5]:https://mc.qcloudimg.com/static/img/32f72a65f46f33d67a93d1a9a3f3e3d1/hostlogwithmetadata.jpeg




