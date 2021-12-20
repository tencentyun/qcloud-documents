## 操作场景

ntpd（Network Time Protocol daemon）是 Linux 操作系统的一个守护进程，用于校正与时钟源服务器同步的本地系统时间，完整的实现了 NTP 协议。ntpd 与 ntpdate 的区别是 ntpd 是步进式的逐渐校正时间，不会出现时间跳变，而 ntpdate 是断点更新。本文档以 CentOS 7.5 操作系统云服务器为例，介绍如何安装和配置 ntpd。

## 注意事项

- 部分操作系统采用 chrony 作为默认 NTP 服务，请确认 ntpd 正在运行并设置为开机自启动。
 - 使用 `systemctl is-active ntpd.service` 命令，可查看 ntpd 是否正在运行。
 - 使用 `systemctl is-enabled ntpd.service` 命令，可查看 ntpd 是否开机自启动。
- NTP 服务的通信端口为 UDP 123，设置 NTP 服务之前，请确保您已经开放 UDP 123 端口。
若未开放该端口，请参考 [添加安全组规则](https://cloud.tencent.com/document/product/213/39740) 进行放行。

## 操作步骤

### 安装 ntpd

执行以下命令，判断是否安装 ntpd。
```
rpm -qa | grep ntp
```
 - 如果返回类似如下结果，表示已安装 ntpd。
![判断ntpd是否安装](https://main.qcloudimg.com/raw/34073904c49e80ab61da25559c7239e5.png)
 - 如果未安装 ntpd，请使用 `yum install ntp` 安装 ntpd。
```
yum -y install ntp
```
ntpd 默认为客户端运行方式。

### 配置 NTP
1. 执行以下命令，打开 NTP 服务配置文件。
```
vi /etc/ntp.conf
```
2. 按 **i** 切换至编辑模式，找到 server 相关配置，将 server 修改为您需要设置的目标 NTP 时钟源服务器（例如 `time1.tencentyun.com`），并删除暂时不需要的 NTP 时钟源服务器。如下图所示：
![server设置](https://main.qcloudimg.com/raw/643dc5bbd2a42307ec10b5d38f756dda.png)
3. 按 **Esc**，输入 **:wq**，保存文件并返回。

### 启动 ntpd

执行以下命令，重启 ntpd 服务。
```
systemctl restart ntpd.service
```

### 检查 ntpd 状态

根据实际需求，执行以下不同的命令，检查 ntpd 的状态。
- 执行以下命令，查看 NTP 服务端口 UDP 123 端口是否被正常监听。
```
netstat -nupl
```
返回类似如下结果，表示监听正常。
![netstat -nupl](https://main.qcloudimg.com/raw/d7da764d05135959154920b81fa9f1e4.png)
- 执行以下命令，查看 ntpd 状态是否正常。
```
service ntpd status
```
返回类似如下结果，表示 ntpd 状态正常。
![ntpd status](https://main.qcloudimg.com/raw/321e56d0f7797f382d9f6903c0315f96.png)
- 执行以下命令，获取更详细的 NTP 服务信息。
```
ntpq -p
```
返回类似如下结果：
![](https://main.qcloudimg.com/raw/ca9ef4caf98b49ed2c9110198a66e7c3.png)
 - **\*** : 表示目前使用的 NTP 服务器。
 - **remote**：响应这个请求的 NTP 服务器的名称。
 - **refid**：NTP 服务器使用的上一级 NTP 服务器。
 - **st**：remote 远程服务器的级别。服务器从高到低级别设定为1 - 16，为了减缓负荷和网络堵塞，原则上建议避免直接连接到级别为1的服务器。
 - **when**：上一次成功请求之后到现在的秒数。
 - **poll**：本地机和远程服务器多少时间进行一次同步（单位为秒）。初始运行 NTP 时，poll 值会比较小，和服务器同步的频率增加，建议尽快调整到正确的时间范围。调整之后，poll 值会逐渐增大，同步的频率也将会相应减小。
 - **reach**：八进制值，用来测试能否和服务器连接。每成功连接一次，reach 的值将会增加。
 - **delay**：从本地机发送同步要求到 NTP 服务器的 round trip time。
 - **offset**：主机通过 NTP 时钟同步与所同步时间源的时间偏移量，单位为毫秒（ms）。offset 越接近于0，主机和 NTP 服务器的时间越接近。
 - **jitter**：用来做统计的值。统计在特定连续的连接数里 offset 的分布情况。即 jitter 数值的绝对值越小，主机的时间就越精确。

### 设置 ntpd 为开机启动

1. 执行以下命令，将 ntpd 设置为开机自启动。
```
systemctl enable ntpd.service
```
2. 执行以下命令，查看 chrony 是否被设置为开机启动。
```
systemctl is-enabled chronyd.service
```
如果 chrony 被设置为开机启动，请执行以下命令，将 chrony 从开机启动中移除。
chrony 与 ntpd 冲突，可能引起 ntpd 开机启动失败。
```
systemctl disable chronyd.service
```

### 增强 ntpd 安全性

依次执行以下命令，为 `/etc/ntp.conf` 配置文件增加安全性。
```
interface ignore wildcard
```
```
interface listen eth0
```


