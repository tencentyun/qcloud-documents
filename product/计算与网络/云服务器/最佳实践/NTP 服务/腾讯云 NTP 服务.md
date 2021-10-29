网络时间协议（Network Time Protocol，NTP），用于同步网络中各个计算机的时间的协议。其用途是将计算机的时钟同步到世界协调时 UTC。

腾讯云提供了内网 NTP 服务器供腾讯云内网设备使用，对于非腾讯云设备，可以使用腾讯云提供的公网 NTP 服务器。

### 内网 NTP 服务器

```
time1.tencentyun.com
time2.tencentyun.com
time3.tencentyun.com
time4.tencentyun.com
time5.tencentyun.com
```

### 外网 NTP 服务器

```
time1.cloud.tencent.com 
time2.cloud.tencent.com 
time3.cloud.tencent.com
time4.cloud.tencent.com
time5.cloud.tencent.com
```

Linux 系统设置 NTP 时钟源服务器详见[《Linux 实例设置 NTP 服务》](https://cloud.tencent.com/document/product/213/30393)。
Windows 系统设置 NTP 时钟源服务器详见[《Windows 实例设置 NTP 服务》](https://cloud.tencent.com/document/product/213/30394)。



