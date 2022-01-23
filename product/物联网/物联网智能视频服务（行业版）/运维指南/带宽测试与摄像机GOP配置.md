## iperf3 工具使用

>!请在 Linux 和 macOS 平台测试。

### 安装

```shell
//测试的客户端与服务器都需要安装 iperf3 工具
$ tar xzvf iperf-3.9.tar.gz
$ cd iperf-3.9
$ ./configure
$ make && make install
```

### 测试

因 Iot Video 使用的是 tcp 推流，这里只以 tcp 测试为例。

- 服务端
```
iperf3 -p 30000  -s -i 1
# 参数说明： -c : 服务端的ip地址 -p : 端口号 -u : 标示udp协议 -b : 每一次发送的数据大小 -t : 总的发送时间(单位：秒) -i : 发送数据的时间间隔(单位：秒) -P : 表示线程个数，不指定则默认单线程
```

- 客户端
```
iperf3 -c 80.1.1.1 -p 30000  -i 1 
# 参数说明： -c : 服务端的ip地址 -p : 端口号 -u : 标示udp协议 -b : 每一次发送的数据大小 -t : 总的发送时间(单位：秒) -i : 发送数据的时间间隔(单位：秒) -P : 表示线程个数，不指定则默认单线程
```

服务器输出示例：
![](https://qcloudimg.tencent-cloud.cn/raw/444dd7f35d1becbb2d107c6ac1a2a522.png)

客户端输出示例：
![](https://qcloudimg.tencent-cloud.cn/raw/1dd45e05b4ab2d0dbdafa21ca3570493.png)


## MTR 工具使用

### 安装

- macOS
```
$ brew install mtr
# MTR 安装完成之后，没有把程序文件复制到 /usr/local/bin 目录下，我们手动复制一下
$ cd /usr/local/Cellar/mtr/0.92/sbin
$ cp mtr /usr/local/bin/
$ cp mtr-packet /usr/local/bin/


# 启动
$ sudo mtr www.baidu.com
```
如下图：
![](https://qcloudimg.tencent-cloud.cn/raw/afccd9ea8f0403112970a2d7c9ccb714.png)

- Linux
  Linux 下面无须安装，MTR 工具是自带的。

### 网络延时测试

详细使用如下图：
![](https://qcloudimg.tencent-cloud.cn/raw/fce79fb93356afce544b6ae89182e543.png)


以在 macOS 上面测试 `192.168.1.1` 服务器为例：

```
sudo mtr -rw 192.168.1.1
# 也可以直接 sudo mtr 192.168.1.1
```
![](https://qcloudimg.tencent-cloud.cn/raw/0ad46fd5d06e1897e52adf794ec97f75.png)

常见可选参数说明：
- -r 或 --report：以报告模式显示输出。
- -p 或 --split：将每次追踪的结果分别列出来，而非 --report 统计整个结果。
- -s 或 --psize：指定 ping 数据包的大小。
- -n 或 --no-dns：不对 IP 地址做域名反解析。
- -a 或 --address：设置发送数据包的 IP 地址。用于主机有多个 IP 的情况。
- -4：只使用 IPv4 协议。
- -6：只使用 IPv6 协议。
-  --port: 指定端口。

在 MTR 运行过程中，您也可以输入相应字母来快速切换模式，各字母的含义如下：
- ? 或 h：显示帮助菜单。
- d：切换显示模式。
- n：切换启用或禁用 DNS 域名解析。
- u：切换使用 ICMP 或 UDP 数据包进行探测。


默认配置下，返回结果中各数据列的说明如下：
- 第一列（Host）：节点 IP 地址和域名。按  **n**  键可切换显示。
- 第二列（Loss%）：节点丢包率。
- 第三列（Snt）：每秒发送数据包数。默认值是10，可以通过“-c”参数指定。
- 第四列（Last）：最近一次的探测延迟。
- 第五、六、七列（Avg、Best、Worst）：分别是探测延迟的平均值、最小值和最大值。
- 第八列（StDev）：标准偏差。越大说明相应节点越不稳定。

## IPC 设置

### GOP 设置

GOP 设置过大，容易导致延时增大，建议设置1~2s GOP 间隔。
例如：帧率是15帧时，1帧间隔建议设置为15 - 30。
![](https://main.qcloudimg.com/raw/61b1e5d9d4caa5a95882a579b4a53ac9.png)

