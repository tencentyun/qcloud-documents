

## 概述

当客户端向某个地址发起访问时，通常会查询本地 DNS 缓存中是否有相关记录，有则会直接访问对应 IP 地址，如果没有则会委托递归服务器进行全球查询。

由于 DNS 域名解析采用 UDP 协议通讯，受网络环境影响较大，极端情况下域名解析可能有数秒的延时。在云函数的使用场景下，域名解析延时有可能导致函数执行超时失败，影响正常的业务逻辑；在函数高频调用的情况下，有可能导致 DNS 服务器解析超出频率限制，同样导致函数执行失败。

云函数提供了 DNS 缓存配置来解决上述问题。DNS 缓存可以提升域名解析效率，缓解网络抖动等因素对域名解析成功率的影响。

## 适用场景
 适用于在函数代码中请求了某个地址，且函数被高频调用的场景。

## 操作步骤

由于实现机制的不同，代码部署的事件函数、Web 函数、镜像部署的函数请分别参考以下步骤开启 DNS 缓存。

### 代码部署的事件函数

1. 登录 [云函数控制台](https://console.cloud.tencent.com/scf/list?rid=1&ns=default)，选择需要启用 DNS 缓存配置的函数，进入函数详情页。
2. 在函数配置页面，单击右上角**编辑**，在编辑状态中勾选**启用 DNS 缓存**。如下图所示： 
![](https://qcloudimg.tencent-cloud.cn/raw/4519731b49e5b363f6423d038c14b9b6.png)
3. 单击**保存**完成函数配置更新。

   

### Web 函数

1. 在 Web 函数的启动文件 [scf_bootstrap](https://cloud.tencent.com/document/product/583/56126) 中添加下述命令，以启动 nscd 进程开启 DNS 缓存。
``` shell
/var/lang/bin/nscd -f /var/lang/conf/nscd.conf
```
2. 将更新后的 `scf_bootstrap` 同函数代码一起部署到云上，函数代码更新后的调用即可使用 DNS 缓存功能。

### 镜像部署函数

1. 在镜像制作过程中安装 nscd。以 centos 为例，可执行以下命令安装 nscd。
```
yum install nscd -y
```
2. 将默认的 `/etc/nscd.conf` 更新为以下内容：
``` 
\#
\# /etc/nscd.conf
\#
\# An example Name Service Cache config file. This file is needed by nscd.
\#
\# WARNING: Running nscd with a secondary caching service like sssd may lead to
\# unexpected behaviour, especially with how long entries are cached.
\#
\# Legal entries are:
\#
\# logfile <file>
\# debug-level <level>
\# threads <initial #threads to use>
\# max-threads <maximum #threads to use>
\# server-user <user to run server as instead of root>
\# server-user is ignored if nscd is started with -S parameters
\# stat-user <user who is allowed to request statistics>
\# reload-count unlimited|<number>
\# paranoia <yes|no>
\# restart-interval <time in seconds>
\#
\# enable-cache <service> <yes|no>
\# positive-time-to-live <service> <time in seconds>
\# negative-time-to-live <service> <time in seconds>
\# suggested-size <service> <prime number>
\# check-files <service> <yes|no>
\# persistent <service> <yes|no>
\# shared <service> <yes|no>
\# NOTE: Setting 'shared' to a value of 'yes' will accelerate the lookup,
\# but those lookups will not be counted as cache hits
\# i.e. 'nscd -g' may show '0%'.
\# max-db-size <service> <number bytes>
\# auto-propagate <service> <yes|no>
\#
\# Currently supported cache names (services): passwd, group, hosts, services
\#

\# logfile /var/log/nscd.log
\# threads 4
\# max-threads 32
server-user root
\# stat-user somebody
debug-level 0
reload-count 2
paranoia no
\# restart-interval 3600

enable-cache passwd no
positive-time-to-live passwd 600
negative-time-to-live passwd 20
suggested-size passwd 211
check-files passwd yes
persistent passwd yes
shared passwd yes
max-db-size passwd 33554432
auto-propagate passwd yes

enable-cache group no
positive-time-to-live group 3600
negative-time-to-live group 60
suggested-size group 211
check-files group yes
persistent group yes
shared group yes
max-db-size group 33554432
auto-propagate group yes

enable-cache hosts yes
positive-time-to-live hosts 300
negative-time-to-live hosts 0
suggested-size hosts 211
check-files hosts no
persistent hosts no
shared hosts yes
max-db-size hosts 8388608

enable-cache services no
positive-time-to-live services 600
negative-time-to-live services 3
suggested-size services 211
check-files services yes
persistent services yes
shared services yes
max-db-size services 33554432

enable-cache netgroup no
positive-time-to-live n etgroup 28800
negative-time-to-live netgroup 20
suggested-size netgroup 211
check-files netgroup yes
persistent netgroup yes
shared netgroup yes
max-db-size netgroup 33554432
```
3. 在启动文件 `scf_bootstrap` 中添加下述命令，以启动 nscd 进程开启 DNS 缓存。
 以 centos 为例，将下述命令添加到启动文件中：
```shell
${PATH}/nscd -f /etc/nscd.conf 
```
>! `${PATH}` 为 nscd 安装的绝对路径。
>
