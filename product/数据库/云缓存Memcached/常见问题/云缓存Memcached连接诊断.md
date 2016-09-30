## 1 通用说明
客户端连接云缓存Memcached服务失败或者成功率低，可能与客户端所在的服务器或者客户端到云缓存Memcached服务之间的网络环境有关。
本工具用于诊断客户端服务器环境以及客户端到云缓存Memcached服务之间的连接问题。
如有任何疑问，请通过腾讯云[工单系统]( http://console.qcloud.com/ticket )  联系我们。

## 2 工具说明
### 2.1 安装说明
1) 下载auto_test_link工具：

|版本|说明|
|--|--|
|[auto_test_link_v1.0.0.zip](https://mccdn.qcloud.com/static/archive/b037b3a255f10d3264bd8eca4dc81c8b/auto_test_link_v1.0.0.zip)|诊断客户端服务器环境以及客户端到云缓存Memcached服务之间的连接问题。|

2) 将工具上传到云缓存Memcached客户端所在的服务器（仅限Linux服务器）。解压过程如下所示：
``` 
$ unzip auto_test_link_v1.0.0.zip
```
解压后，会出现3个文件，文件说明如下：
auto_test_link.sh：诊断工具脚本。
LinkTest：测试网络连接工具。
readme.txt：使用说明。

3) 解压后，无需安装，直接进入解压后的目录运行auto_test_link.sh脚本即可。

### 2.2 命令说明
``` 
$ ./auto_test_link.sh [ip] [port]
```

|参数名称|	可选|	类型|	说明|
|--|--|--|--|
|ip|	必选|	string（例如：10.1.2.3）|	云缓存Memcached服务的IP。|
|port|	必选|	string (例如：4321)|	云缓存Memcached服务的端口。|

### 2.3 命令示例
```
$./auto_test_link.sh 10.1.2.3 4321 
TIME_WAIT link 320
tcp_tw_reuse=1 
tcp_tw_recycle=1 
10000 packets transmitted, 10000 received, 0% packet loss, time 1915ms 
CPU 0.0 0.0 0.0 0.2 5.5
DISK 79% 1% 74% 65% 26%
Connect to 10.1.2.3:4321 success 
```

### 2.4 诊断输出说明

| 输出 | 说明 | 
|---------|---------|
|TIME_WAIT link 320|说明当前客户端服务器有320个TCP连接处于TIME_WAIT 状态。TIME_WAIT 过多会造成临时端口不足，无法建立新连接。|
|tcp_tw_reuse=1|必须设置为1，表示允许TIME_WAIT 状态的socket重新用于新的连接，从而减少TIME_WAIT造成端口不足问题的出现。|
|tcp_tw_recycle=1|必须设置为1，表示开启快速回收TIME_WAIT 状态的socket，从而减少TIME_WAIT造成端口不足问题的出现。|
|10000 packets transmitted, 10000 received, 0% packet loss, time 1915ms|发送了10000个ping包，用于分析丢包率和延时情况。有些服务器不支持发ping flood，可以使用慢ping进行分析。|
|CPU 0.0 0.0 0.0 0.2 5.5|服务器上CPU使用率最高的5个进程的CPU使用率。|
|DISK 79% 1% 74% 65% 26%|服务器上所有磁盘的使用率情况。|
|Connect to 10.1.2.3:4321 success|如果成功连接到IP和端口所指向的云缓存Memcached服务，则返回success；否则返回failed。|
