## 操作场景

NTPDate 为断点更新，NTPD 为步进式的逐渐校正时间。对新购实例，您可以使用 NTPDate 同步时间。对已经承载有运行中业务的实例，建议您使用 NTPD 同步时间。本文档以 CentOS 7.5 操作系统云服务器为例，介绍如何将 NTPDate 转换为 NTPD。

## 前提条件
NTP 服务的通信端口为 UDP 123，转换为 NTP 服务之前，请确保您已经开放 UDP 123端口。
若未开放该端口，请参考 [添加安全组规则](https://cloud.tencent.com/document/product/213/39740) 进行放行。

## 操作步骤

### 手动将 NTPDate 转换为 NTPD
#### 关闭 NTPDate
1. 执行以下命令，导出 crontab 配置，并过滤 NTPDate。
```
crontab -l |grep -v ntpupdate > /tmp/cronfile
```
2. 执行以下命令，更新 NTPDate 配置。
```
crontab /tmp/cronfile
```
3. 执行以下命令，修改 `rc.local` 文件。
```
vim rc.local
```
4. 按 “**i**” 切换至编辑模式，删除 ntpupdate 配置行。
5. 按 “**Esc**”，输入 “**:wq**”，保存文件并返回。

#### 配置 NTPD
1. 执行以下命令，打开 NTP 服务配置文件。
```
vi /etc/ntp.conf
```
2. 按 **i** 切换至编辑模式，找到 server 相关配置，将 server 修改为您需要设置的目标 NTP 时钟源服务器（例如 `time1.tencentyun.com`），并删除暂时不需要的 NTP 时钟源服务器。如下图所示：
![server设置](https://main.qcloudimg.com/raw/643dc5bbd2a42307ec10b5d38f756dda.png)
3. 按 **Esc**，输入 **:wq**，保存文件并返回。


### 自动将 NTPDate 转换为 NTPD
1. 下载 `ntpd_enable.sh` 脚本。
```
wget https://image-10023284.cos.ap-shanghai.myqcloud.com/ntpd_enable.sh
```
2. 执行以下命令，使用 `ntpd_enable.sh` 脚本将 NTPDate 转换为 NTPD。
```
sh ntpd_enable.sh
```



