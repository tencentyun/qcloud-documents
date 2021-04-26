## 1 Overview
Client fails to or cannot always connect to Cloud Memcached possibly due to the server environment of client.
This tool is used to diagnose the TCP connection environment status on the client server.
For any questions, contact us via Tencent Cloud [Ticket System](http://console.cloud.tencent.com/ticket).

## 2. How to use the tool
### 2.1 Installation steps
1) Download auto_test_link tool:

| Version | Description |
|--|--|
| [auto_test_link_v1.0.0.tar.gz](https://mc.qcloudimg.com/static/archive/0d1f32efea8cdf4e2433105ef2c30fe8/auto_test_link_v1.0.0.tar.gz) | Diagnose the server environment of client and the connection problems between the client and Cloud Memcached. |

2) Upload the tool to the server (Linux CVM only) where Cloud Memcached client resides in. The tool is decompressed as follows:
``` 
$ unzip auto_test_link_v1.0.0.zip
```
After decompression, you can get the following two files:
auto_test_link.sh: Diagnose tool script.
readme.txt: Instructions.

3) After decompression, you can directly run the script auto_test_link.sh in the directory, without the need for installation.

### 2.2 Command Description
``` 
$ ./auto_test_link.sh [ip] [port]
```

| Parameter Name |	Optional |	Type |	Description |
|--|--|--|--|
| ip |	Required |	string (e.g. 10.1.2.3) |	Cloud Memcached service IP. |
| port |	Required |	string (e.g. 4321) |	Cloud Memcached service port. |

### 2.3 Command example
```
$./auto_test_link.sh 10.1.2.3 4321 
TIME_WAIT link 320
tcp_tw_reuse=1 
tcp_tw_recycle=1 

```

### 2.4 Diagnostic output

| Output | Description | 
|---------|---------|
| TIME_WAIT link 320 | Currently, 320 TCP connections on the client CVM are in a state of TIME_WAIT. Too many connections in TIME_WAIT state will cause insufficient temporary ports, therefore, new connections cannot be established. |
| tcp_tw_reuse=1 | This value must be set to 1, which means the socket in TIME_WAIT state can be reused for new connection, to avoid the problem of insufficient temporary ports due to TIME_WAIT. |
| tcp_tw_recycle=1 | This value must be set to 1, which means to enable the quick reclaim of sockets in TIME_WAIT state, to avoid the problem of insufficient temporary ports due to TIME_WAIT. |


