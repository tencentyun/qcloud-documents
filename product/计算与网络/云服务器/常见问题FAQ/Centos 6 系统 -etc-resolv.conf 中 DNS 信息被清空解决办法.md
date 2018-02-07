## 问题描述
centos 6.x 系统中由于 initscripts 部分版本存在缺陷，对操作系统进行重启或者执行命令`service network restart`之后`/etc/resolv.conf`配置文件中的 DNS 信息被清空，导致无法解析域名。

## 如何排查
### 存在的缺陷版本
因为系统 grep 版本的不同, initscripts 低于`initscripts-9.03.49-1`的版本存在缺陷。

### 查看initscripts版本
可以登录云服务器查看 initscripts 的版本情况确认是否存在该问题。

查看的方式：
```
$rpm -q initscripts
initscripts-9.03.40-2.e16.centos.x86_64
```
当前例子输出的 initscripts 版本`initscripts-9.03.40-2`低于存在的问题版本`initscripts-9.03.49-1`，存在DNS被清空的风险。
## 解决方法
### 升级版本
推荐升级 initscripts 到最新的版本，并重新生成 DNS 信息，命令如下：

```
cat /dev/null > /etc/resolv.conf
service network restart
yum makecache
yum -y update initscripts
```
等待升级完成后，可以再次检查 initscripts 的版本信息，确认升级是否成功，执行命令：
```
$rpm -q initscripts
initscripts-9.03.58-1.el6.centos.2.x86_64
```
例子打印的版本不同于之前版本，且高于`initscripts-9.03.49-1`，操作升级成功。




