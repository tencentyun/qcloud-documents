## 现象描述
对操作系统为 CentOS 6.x 的云服务器，进行重启或者执行命令`service network restart`之后，云服务器无法解析域名。
同时，查看配置文件 /etc/resolv.conf，发现 DNS 信息被清空。

## 可能原因
在 CentOS 6.x 操作系统中，因为 grep 版本的不同，initscripts 的版本低于 9.03.49-1 存在缺陷。
## 解决思路
升级 initscripts 到最新的版本，并重新生成 DNS 信息。
## 处理步骤
1. 登录云服务器，执行以下命令，查看 initscripts 的版本情况确认是否存在该问题。
```
$rpm -q initscripts
initscripts-9.03.40-2.e16.centos.x86_64
```
如上例所示，initscripts 版本 initscripts-9.03.40-2 低于存在的问题版本initscripts-9.03.49-1，存在 DNS 被清空的风险。
2.  执行以下命令，将 initscripts 升级到最新的版本，并重新生成 DNS 信息。
```
cat /dev/null > /etc/resolv.conf
service network restart
yum makecache
yum -y update initscripts
```
3.  升级完成后，执行以下命令，检查 initscripts 的版本信息，确认升级是否成功。
```
$rpm -q initscripts
initscripts-9.03.58-1.el6.centos.2.x86_64
```
显示的版本不同于之前版本，且高于 initscripts-9.03.49-1，操作升级成功。