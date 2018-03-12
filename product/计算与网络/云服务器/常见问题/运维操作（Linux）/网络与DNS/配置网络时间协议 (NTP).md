保持系统时间的准确性对于许多服务器任务和进程来说是非常重要的，同时也有利于用户快速查看系统日志并准确定位问题。同时如果从实例中调用云服务 API 时，系统时间设置不正确导致签名中的时间与请求时间不匹配，云 API 可能会拒绝请求。默认情况下实例会初始配置网络时间协议 (NTP)，有关 NTP 的更多信息，请访问 http://www.ntp.org/。

## 配置网络时间协议 (NTP)
Important
这些过程适用于 Amazon Linux。有关其他发布版本的更多信息，请参阅其具体文档。
更改时区

默认情况下，Amazon Linux 实例设置为 UTC（协调世界时）时区，但是您可能想将实例上的时间更改为本地时间或网络中的其他时区。

更改实例上的时区

确定将在实例上使用的时区。/usr/share/zoneinfo 目录包含时区数据文件的层次结构。浏览该位置的目录结构，查找针对您的时区的文件。

[ec2-user ~]$ ls /usr/share/zoneinfo
Africa      Chile    GB         Indian       Mideast   posixrules  US
America     CST6CDT  GB-Eire    Iran         MST       PRC         UTC
Antarctica  Cuba     GMT        iso3166.tab  MST7MDT   PST8PDT     WET
Arctic      EET      GMT0       Israel       Navajo    right       W-SU
...
该位置的部分条目是目录（如 America），这些目录包含针对特定城市的时区文件。查找要用于实例的城市（或时区中的一个城市）。在该示例中，您可以使用洛杉矶的时区文件 /usr/share/zoneinfo/America/Los_Angeles。

使用新时区更新 /etc/sysconfig/clock 文件。

使用您常用的文本编辑器（如 vim 或 nano）打开 /etc/sysconfig/clock 文件。您需要在编辑器命令中使用 sudo，因为 /etc/sysconfig/clock 归 root 所有。

查找 ZONE 条目，将其更改为时区文件（省略路径的 /usr/share/zoneinfo 部分）。例如，若要更改为洛杉矶时区，请将 ZONE 条目更改为以下内容。

ZONE="America/Los_Angeles"
Note
请勿将 UTC=true 条目更改为其他值。此条目用于硬件时钟；如果您在实例上设置了其他时区，则无需调整此条目。
保存文件，退出文本编辑器。

在 /etc/localtime 与时区文件之间创建一个符号链接，以便实例在引用本地时间信息时找到此时区文件。

[ec2-user ~]$ sudo ln -sf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime
重启系统，以便所有服务和应用程序接受新时区信息。

[ec2-user ~]$ sudo reboot

## 配置网络时间协议 (NTP)

默认情况下，Amazon Linux 实例上配置网络时间协议 (NTP)；但是，实例需要访问 Internet 才能使标准 NTP 配置工作。此外，您的实例的安全组规则必须允许端口 123 (NTP) 的出站 UDP 流量，您的网络 ACL 规则必须允许端口 123 的入站和出站 UDP 流量。本部分中的过程介绍如何验证默认 NTP 配置是否正常工作。如果您的实例无法访问 Internet，您需要将 NTP 配置为在您的私有网络中查询其他服务器，以便保持准确时间。

验证 NTP 是否正常运行

使用 ntpstat 命令，查看实例上 NTP 服务的状态。

[ec2-user ~]$ ntpstat
如果输出类似于以下输出，则 NTP 在实例上正常运行。

synchronised to NTP server (12.34.56.78) at stratum 3
   time correct to within 399 ms
   polling server every 64 s
如果输出状态为“unsynchronised”，请等待一分钟，然后再试。首次同步可能需要一分钟才能完成。

如果输出状态为“Unable to talk to NTP daemon. Is it running?”，您可能需要启动 NTP 服务，使它在启动时自动启动。

（可选）您可以使用 ntpq -p 命令查看 NTP 服务器已知的对等方的列表及其状态的摘要。

[ec2-user ~]$ ntpq -p
     remote           refid      st t when poll reach   delay   offset  jitter
==============================================================================
+lttleman.deekay 204.9.54.119     2 u   15  128  377   88.649    5.946   6.876
-bittorrent.tomh 91.189.94.4      3 u  133  128  377  182.673    8.001   1.278
*ntp3.junkemailf 216.218.254.202  2 u   68  128  377   29.377    4.726  11.887
+tesla.selinc.co 149.20.64.28     2 u   31  128  377   28.586   -1.215   1.435
如果此命令的输出未显示任何活动，请检查您的安全组、网络 ACL 或防火墙是否已阻止对 NTP 端口的访问。

启动和启用 NTP

使用以下命令启动 NTP 服务。

[ec2-user ~]$ sudo service ntpd start
Starting ntpd:                                             [  OK  ]
利用 chkconfig 命令，启用 NTP，以便在系统启动时启动。

[ec2-user ~]$ sudo chkconfig ntpd on
使用以下命令验证是否启用了 NTP。

[ec2-user ~]$ sudo chkconfig --list ntpd
ntpd           	0:off	1:off	2:on	3:on	4:on	5:on	6:off
在这里，ntpd 在运行级别 2、3、4 和 5 上为启用状态，这是正确的。

更改 NTP 服务器

您可以决定不使用标准 NTP 服务器，或者您可能需要在自己的私有网络中将自己的 NTP 服务器用于无法访问 Internet 的实例。

打开常用文本编辑器（如 vim 或 nano）中的 /etc/ntp.conf 文件。您需要在编辑器命令中使用 sudo，因为 /etc/ntp.conf 由 root 拥有。

查找 server 部分，这里定义了将针对 NTP 配置进行轮询的服务器。

# Use public servers from the pool.ntp.org project.
# Please consider joining the pool (http://www.pool.ntp.org/join.html).
server 0.amazon.pool.ntp.org iburst
server 1.amazon.pool.ntp.org iburst
server 2.amazon.pool.ntp.org iburst
server 3.amazon.pool.ntp.org iburst
Note
n.amazon.pool.ntp.org DNS 记录旨在对来自 AWS NTP 流量进行负载均衡。但是，这些公有 NTP 服务器位于 pool.ntp.org 项目中，不归 AWS 所有和管理。我们不能保证这些服务器位于您的实例附近的地理位置，甚至不能保证它们位于 AWS 网络中。有关更多信息，请参阅 http://www.pool.ntp.org/en/。
通过将“#”字符添加到您不需要使用的服务器定义的开头，注释掉这些服务器。

# Use public servers from the pool.ntp.org project.
# Please consider joining the pool (http://www.pool.ntp.org/join.html).
#server 0.amazon.pool.ntp.org iburst
#server 1.amazon.pool.ntp.org iburst
#server 2.amazon.pool.ntp.org iburst
#server 3.amazon.pool.ntp.org iburst
为每个要进行时间同步轮询的服务器添加一个条目。您可以对此条目使用 DNS 名称，或者点分四节 IP 地址（如 10.0.0.254）。

server my-ntp-server.my-domain.com iburst
重新启动 NTP 服务，以接受这些新服务器。

[ec2-user ~]$ sudo service ntpd start
Starting ntpd:                                             [  OK  ]
验证新设置是否工作，以及 NTP 是否功能正常。

[ec2-user ~]$ ntpstat
synchronised to NTP server (64.246.132.14) at stratum 2
   time correct to within 99 ms