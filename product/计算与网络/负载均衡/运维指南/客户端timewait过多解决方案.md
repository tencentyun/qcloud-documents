## 本文背景：
客户压测LB时，常会遇到了一些客户端timewait过多，端口被快速占满，导致connect失败的问题，下面会说明原因和解决方案。

## Linux参数介绍：
**tcp_timestamps ：** 是否开启tcp timestamps选项，timestamps是在tcp三次握手过程中协商的，任意一方不支持，该连接就不会使用timestamps选项。
**tcp_tw_recycle ：**  是否开启tcp time_wait状态回收。
**tcp_tw_resuse ：** 开启后，可直接回收超过1s的time_wait状态的连接。

## 原因分析：
客户端timewait太多，是因为客户端主动断开连接，客户端每断开一个连接，该连接都会进入timewait状态，默认60s超时回收。一般情况下，遇到这种场景时，客户会选择打开`tcp_tw_recycle`和`tcp_tw_resuse`两个参数，便于回收timewait状态连接。
然而当前CLB没有打开`tcp_timestamps`选项，导致客户端打开的`tcp_tw_recycle`和`tcp_tw_resuse`都不会生效，不能快速回收timewait状态连接。下面会解释几个linux参数的含义和LB不能开启`tcp_timestamps`的原因。

1. tcp_tw_recycle 和 tcp_tw_resuse只有在tcp_timestamps打开时才会生效。

2. tcp_timestamps和tcp_tw_recycle是不能同时打开的，因为公网客户端经过NAT网关访问服务器，会存在问题，原因如下：

tcp_tw_recycle/tcp_timestamps都开启的条件下，60s内同一源ip主机的socket connect请求中的timestamp必须是递增的。以2.6.32内核为例，具体实现如下：

![](https://mc.qcloudimg.com/static/img/2199611fec3b323a7b8fd3bb38459913/Linux1.png)

> tmp_opt.saw_tstamp：该socket支持tcp_timestamp
sysctl_tw_recycle：本机系统开启tcp_tw_recycle选项
TCP_PAWS_MSL：60s，该条件判断表示该源ip的上次tcp通讯发生在60s内
TCP_PAWS_WINDOW：1，该条件判断表示该源ip的上次tcp通讯的timestamp 大于 本次tcp

3. LB（7层）关闭了tcp_timestamps原因，因为公网客户端经过NAT网关访问服务器，可能会存在问题，如下例：

a)	某五元组还是time_wait状态。NAT网关对端口的分配策略，2MSL内复用了同个五元组，发来syn包。

b)	在开启tcp_timestamps情况下，同时满足如下两个条件，会丢弃该syn包（因为开启了时间戳选项，认为是老包）。
i.	上次时间戳 > 本次时间戳。
ii.	24天内收过包（时间戳字段是32位，linux默认1ms更新一次时间戳，24天会发生时间戳回绕）。
备注：在移动端该问题更为明显，因为客户端都是在运营商NAT网关下面共享有限的公网ip，五元组还可能在2MSL内被复用，不同客户端传来的时间戳不能保证是递增的。
以2.6.32内核为例，具体实现如下：

![](https://mc.qcloudimg.com/static/img/6228a7dc25c670d4d2fbddc9ea400779/Linux2.png)

> rx_opt->ts_recent：上次的时间戳
rx_opt->rcv_tsval：本次收到的时间戳
get_seconds（）： 当前时间
rx_opt->ts_recent_stamp： 上次收到包的时间

## 解决方案：
客户端Timewait过多问题，有如下解决方案：

**1. HTTP使用短连接（Connection: close），这时由LB主动关闭连接，客户端不会产生timewait**。

**2. 如果场景需要使用长连接，可以打开socket的SO_LINGER选项，使用rst关闭连接，避免进入timewait 状态，达到快速回收端口的目的**。
