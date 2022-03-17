### 配置 NTP 服务后，如何调整 NTP 的同步间隔？
当您在 [配置 NTP 服务](https://cloud.tencent.com/document/product/213/30393) 后，可重启 ntpd 服务来重置 NTP 的同步间隔。如需手动设置 ntpd 同步间隔，可参考以下步骤：
1. 执行以下命令，修改 NTP 配置文件。
```
vi /etc/ntp.conf
```
2. 按 **i** 进入编辑模式，进行以下配置：
  1. 如有 `server time1.tencentyun.com iburst`，请在行首添加 `#` 进行注释。
  2. 添加以下配置，其中 `minpoll 4` 表示最小为2<sup>4</sup>，`maxpoll 5` 表示最大为2<sup>5</sup>。
```
server time1.tencentyun.com minpoll 4 maxpoll 5
```
配置完成后如下图所示，输入 **:wq** 保存更改并退出。
![](https://main.qcloudimg.com/raw/02d6457d29b4c573605e3c79c5ccfc9f.png)
3. 重启 ntpd 服务后，执行 `ntpd -p` 命令，即可查看 poll 值为16（即2<sup>4</sup>）。如下图所示：
![](https://main.qcloudimg.com/raw/9fa0c72751de74d3b6e72cc1ca831952.png)

### 腾讯云提供的 ntpd 时间源服务器所提供的时间是从什么源头获取的？
NTP 时钟上游为北斗时间源。
 
### NTP 服务配置报错 localhost.localdomain timeout 是什么原因，如何修复？
报错信息如下图所示：
![](https://main.qcloudimg.com/raw/1b3158135475e6cfbee28d2373685616.png)
出现该错误可能是您进行了 POSTROUTING，请核实并确认。如是，则请将 `ntp.conf` 配置文件中的源 IP 改为 eth0 的 IP 即可。

### 云下机器是否可与云上机器共用一个 NTP？是否可提供 NTP 同步地址？
内网 NTP 仅腾讯云上实例可用。若云下机器支持外网，则可通过配置外网 NTP 源实现同步。地址如下：
- 内网 NTP 服务器
```
time1.tencentyun.com
time2.tencentyun.com
time3.tencentyun.com
time4.tencentyun.com
time5.tencentyun.com
```
- 外网 NTP 服务器
```
time1.cloud.tencent.com 
time2.cloud.tencent.com 
time3.cloud.tencent.com
time4.cloud.tencent.com
time5.cloud.tencent.com
```

### 为什么使用自定义镜像创建的云服务器与正常时间不一致？
请核实是否开启了 NTP 服务。若后续需使用 NTP 同步功能，请对应实例的操作系统参考以下文档进行 NTP 配置，完成配置后重新创建自定义镜像即可。
 - [Linux 实例：配置 NTP 服务](https://cloud.tencent.com/document/product/213/30393)
 - [Windows 实例：配置 NTP 服务](https://cloud.tencent.com/document/product/213/30394)

### 云服务器无法 ping 通 NTP 服务器，是否影响 NTP 同步？
不影响。NTP 域名禁止 ping，仅需确保您的 NTP 服务正常访问即可。

### 为什么使用自定义镜像创建的云服务器 ntp.conf 内容被还原了？
系统内 Cloud-Init 初始化导致，请您在制作自定义镜像前删除 `/etc/cloud/cloud.cfg` 中 NTP 相关配置。详情请参见 [Cloud-Init 和 Cloudbase-Init 问题](https://cloud.tencent.com/document/product/213/19670)。

### 若改变内网 DNS，会有哪些具体影响？
涉及到腾讯云内部域名解析的业务均会被影响。例如：
- 影响 yum 下载，yum 源默认是腾讯内网的域名。若修改了 DNS 则还需修改 yum 源。
- 影响监控数据上报，该功能依赖内网域名。
- 影响服务器的时间同步 NTP 功能，该功能依赖内网域名。

### Windows 系统实例本地时间设置为美东时间，为什么重启后会被重置为北京时间？
请核实该实例是否开启 windowstime 服务，若该服务未正常启动则需手动开启。服务开启后，实例系统时间会自动同步。建议您将此服务设置为开机自启动。

### 为什么无法使用 ntpq -np 命令查看同步时间？
报错信息如下图所示：
![](https://main.qcloudimg.com/raw/88972a2aeda155c10000e8576d16bbe9.png)
出现该错误通常是 `/etc/ntp.conf` 中的 listen 网络设备未配置 IP 或配置了非实例的内网主 IP，请核实并确认。如是，则更改为主 IP 后重启 ntpd 即可。

### 使用外网 NTP 时间服务器同步时间时，出现报错该如何处理？
使用外网 NTP 时间服务器同步时间时，出现 `no server suitable for synchronization found` 报错。如下图所示：
![](https://main.qcloudimg.com/raw/1909910bc2a86a5f93e09f4601654327.png)
可能原因是实例的公网 IP 在受到 DDOS 攻击时，会触发 NTP 的反射防护策略，针对访问腾讯云的源端口123外网流量全部拦截，导致时间同步异常。建议您在使用实例时尽量使用内网 NTP 时间服务器进行时间同步。



