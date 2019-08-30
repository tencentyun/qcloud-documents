### 在执行计算任务过程中抛出异常信息 com.qcloud.cos.exception: CosServiceException: Reduce your request rate. (Status Code: 503; Error Code: SlowDown; Request ID: NWXXXXXXXXXX，该如何处理？

大数据计算任务通常会并行地读取 COS 存储桶中的数据，因而触发了访问频率的限制。COS 默认对每个账号有1200QPS的操作限制，建议增加`fs.cosn.maxRetries`配置值，使其通过多次重试来保证作业的正常运行。

### 在执行计算任务过程中抛出异常信息 java.net.ConnectException: Cannot assign requested address (connect failed) (state=42000,code=40000)，该如何处理？

出现 Cannot assign requested address 错误一般是因为用户在短时间内建立了大量的 TCP 短连接，而连接关闭后，本地端口并不会被立即回收，而是默认经过一个60秒的超时阶段，因此导致客户端在这段时间内，没有可用端口用于与 Server 端建立 Socket 连接。

解决方法：修改`/etc/sysctl.conf`文件，调整如下内核参数进行规避：
```conf
net.ipv4.tcp_timestamps = 1     #打开 TCP 时间戳的支持
net.ipv4.tcp_tw_reuse = 1       #支持将处于 TIME_WAIT 状态的 socket 用于新的 TCP 连接
net.ipv4.tcp_tw_recycle = 1     #启用处于 TIME-WAIT 状态的 socket 的快速回收
net.ipv4.tcp_syncookies=1       
net.ipv4.tcp_fin_timeout = 10              #端口释放后的等待时间
net.ipv4.tcp_keepalive_time = 1200           #TCP 发送 KeepAlive 消息的频度。缺省是2小时，改为20分钟
net.ipv4.ip_local_port_range = 1024 65000    #对外连接的端口范围。默认是32768至61000，改为1024至65000
net.ipv4.tcp_max_tw_buckets = 10240          #TIME_WAIT 状态 Socket 的数量限制，如果超过了这个数量，新来的 TIME_WAIT 套接字会被直接释放，默认值是180000。适当地降低该参数可以减小处于 TIME_WAIT 状态 Socket 的数量
```

