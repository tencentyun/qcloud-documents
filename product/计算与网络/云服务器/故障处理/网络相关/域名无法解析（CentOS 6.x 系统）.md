## 现象描述
操作系统为 CentOS 6.x 的云服务器进行重启或者执行命令 `service network restart` 后，云服务器出现无法解析域名的情况。同时，查看 `/etc/resolv.conf` 配置文件时，发现 DNS 信息被清空。

## 可能原因
在 CentOS 6.x 操作系统中，因为 grep 版本的不同，initscripts 的版本低于 9.03.49-1 存在缺陷。

## 解决思路
升级 initscripts 到最新的版本，并重新生成 DNS 信息。

## 处理步骤
1. 登录云服务器。
2. 执行以下命令，查看 initscripts 的版本，确认 initscripts 是否存在因版本低于 9.03.49-1 而存在缺陷的问题。
```
rpm -q initscripts
```
返回类似如下信息：
```
initscripts-9.03.40-2.e16.centos.x86_64
```
可得知，initscripts 版本 initscripts-9.03.40-2 低于存在的问题版本（initscripts-9.03.49-1），存在 DNS 被清空的风险。
3. 依次执行以下命令，将 initscripts 升级到最新的版本，并重新生成 DNS 信息。
```
yum makecache
yum -y update initscripts
service network restart
```
3. 完成升级后，执行以下命令，检查 initscripts 的版本信息，确认升级是否成功。
```
rpm -q initscripts
```
返回类似如下信息：
```
initscripts-9.03.58-1.el6.centos.2.x86_64
```
可得知，显示的版本不同于之前版本，且高于 initscripts-9.03.49-1，操作升级成功。




