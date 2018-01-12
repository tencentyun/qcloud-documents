##问题描述
centos 6系统因为initscripts存在缺陷,系统重启或者service network restart 
之后/etc/resolv.conf中的DNS信息被清空. 导致无法解析域名.

##initscripts缺陷版本：
下面的版本存在缺陷
```
initscripts-9.03.40-2.el6.centos.x86_64
initscripts-9.03.40-2.el6.centos.i686
```

##查看当前initscripts的版本
```
#查看当前initscripts的版本
rpm -q initscripts
```
![](https://i.imgur.com/3bcLmHG.png)

##解决方法
执行如下命令,升级initscripts到新版本
```
cat /dev/null > /etc/resolv.conf
service network restart
yum makecache
yum -y update initscripts
```





