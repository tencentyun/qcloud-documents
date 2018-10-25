## 1 通用说明
客户端连接云缓存Memcached服务失败或者成功率低，可能与客户端所在的服务器环境有关。
本工具用于诊断客户端服务器的tcp连接环境状态。
如有任何疑问，请通过腾讯云[工单系统]( http://console.cloud.tencent.com/ticket )  联系我们。

## 2 工具说明
### 2.1 安装说明
1) 下载auto_test_link工具：

|版本|说明|
|--|--|
|[auto_test_link_v1.0.0.tar.gz](https://mc.qcloudimg.com/static/archive/0d1f32efea8cdf4e2433105ef2c30fe8/auto_test_link_v1.0.0.tar.gz)|诊断客户端服务器环境以及客户端到云缓存Memcached服务之间的连接问题。|

2) 将工具上传到云缓存Memcached客户端所在的服务器（仅限Linux服务器）。解压过程如下所示：
``` 
$ unzip auto_test_link_v1.0.0.zip
```
解压后，会出现2个文件，文件说明如下：
auto_test_link.sh：诊断工具脚本。
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

```

### 2.4 诊断输出说明

| 输出 | 说明 | 
|---------|---------|
|TIME_WAIT link 320|说明当前客户端服务器有320个TCP连接处于TIME_WAIT 状态。TIME_WAIT 过多会造成临时端口不足，无法建立新连接。|
|tcp_tw_reuse=1|必须设置为1，表示允许TIME_WAIT 状态的socket重新用于新的连接，从而减少TIME_WAIT造成端口不足问题的出现。|
|tcp_tw_recycle=1|必须设置为1，表示开启快速回收TIME_WAIT 状态的socket，从而减少TIME_WAIT造成端口不足问题的出现。|

