## 操作场景

NTPD（Network Time Protocol daemon）是 Linux 操作系统的一个守护进程，其完整的实现了 NTP 协议，用于校正本地系统与时钟源服务器之前的时间。NTPD 与 NTPDate 的区别是步进式的逐渐校正时间，不会出现时间跳变，而 NTPDate 是断点更新。本文将介绍 NTPD 的安装和使用。

## 注意事项

* 有部分操作操作系统采用 chrony 作为默认 NTP 服务。使用 “systemctl is-active ntpd.service” 查看 NTPD 是否正在运行；使用 "systemctl is-enabled ntpd.service" 查看 NTPD 是否开机自启动。详情请参见下述设置 NTPD 为开机自启动部分。
* NTP 服务的通信端口为 UDP 123，设置 NTP 服务之前请确保您已经打开 UDP 123 端口。您可以通过 netstat -nupl 查看实例是否开通 UDP 123 端口。您可以参考文档 [安全组操作指南](https://cloud.tencent.com/document/product/213/18197) 放行 UDP 123 端口。

> **注意：**
> 本文下述操作均在 CentOS 7.5 64bit 实例上进行。

## 操作步骤
### 安装

- 采用下述命令判断 NTPD 是否安装：
```
rpm -qa | grep ntp
```
![判断ntpd是否安装](https://main.qcloudimg.com/raw/34073904c49e80ab61da25559c7239e5.png)
- 如果未安装，则使用 yum install ntp 进行安装。如果不做任何配置， NTPD 将默认工作于客户端模式。
```
yum -y install ntp
```

### 配置
- 用 vim 打开并编辑 NTP 服务配置文件。
```
vi /etc/ntp.conf
```
- 找到 server 相关配置，将 server 修改为您需要设置的目标 NTP 时钟源服务器，并删除暂时不需要的 NTP 时钟源服务器。
![server设置](	https://main.qcloudimg.com/raw/b21b559ce745ef5c765251a8ee514dca.png)

### 启动
- 使用 “service ntpd start” 启动 NTP 服务，如果 NTP 已经启动，则使用 “service ntpd restart” 进行重启。
```
service ntpd start
```
![启动ntp](https://main.qcloudimg.com/raw/470afd5f311b5ba3ad321ed12d974c88.png)

### 状态检查
- 使用 netstat 查看 NTP 服务端口 udp 123 有没有被正常监听。
```
netstat -nupl
```
![netstat -nupl](https://main.qcloudimg.com/raw/e7eb5ed8529fdc1366210ef76cf09bd3.png)
- 使用下述命令查看 NTPD 状态是否正常：
```
service ntpd status
```
![ntpd status](	https://main.qcloudimg.com/raw/8af337c167f295938f5edbc005032809.png)
- 使用 “ntpstat” 查看 NTPD 有没有正常开启以及配置到正确的 NTP 时钟源服务器。该命令会输出当前 NTP 时钟源服务器的 IP 地址。此 IP 地址应为上述配置的 NTP 时钟源服务器的 IP 地址（可以使用 “nslookup 域名” 获取域名对应的 IP 地址）。
![ntpstat](https://main.qcloudimg.com/raw/83d49c87c485989123acbb9a30d92d0c.png)

- 更详细的 NTP 服务信息可以使用 ntpq -p 进行获取。
![ntpq](https://main.qcloudimg.com/raw/87df34053b422b0c03e038e4e5a9fde0.png)
> remote：响应这个请求的 NTP 服务器的名称。
> refid：NTP 服务器使用的上一级 NTP 服务器。
> st：remote 远程服务器的级别.由于 NTP 是层型结构,有顶端的服务器,多层的 Relay Server 再到客户端.所以服务器从高到低级别可以设定为 1-16。为了减缓负荷和网络堵塞,原则上应该避免直接连接到级别为 1 的服务器的。
> when：上一次成功请求之后到现在的秒数。
> poll：本地机和远程服务器多少时间进行一次同步（单位为秒）。在一开始运行 NTP 的时候这个 poll 值会比较小，那样和服务器同步的频率也就增加了，可以尽快调整到正确的时间范围，之后 poll 值会逐渐增大,同步的频率也就会相应减小。
> reach：这是一个八进制值,用来测试能否和服务器连接。每成功连接一次它的值就会增加。
> delay：从本地机发送同步要求到 NTP 服务器的 round trip time。
> offset：主机通过 NTP 时钟同步与所同步时间源的时间偏移量，单位为毫秒（ms）。offset 越接近于 0，主机和 NTP 服务器的时间越接近。
> jitter：这是一个用来做统计的值。它统计了在特定个连续的连接数里 offset 的分布情况。简单地说这个数值的绝对值越小，主机的时间就越精确。

### 设置 NTPD 为开机启动

- 使用下述命令将 NTPD 设置为开机自启动。
```
systemctl enable ntpd.service
```

- 使用下述命令查看 chrony 是否被设置为开机启动。
```
systemctl is-enabled chronyd.service
```

- chrony 与 NTPD 冲突，可能引起 NTPD 开启启动失败，需要使用下述命令将 chrony 从开机启动中移除。
```
systemctl disable chronyd.service
```


