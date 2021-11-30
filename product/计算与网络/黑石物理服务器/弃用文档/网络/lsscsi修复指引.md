# 说明
尊敬的腾讯云客户，部分黑石物理机操作中，未安装盘位检测工具（lsscsi），不便快速识别故障硬盘槽位，影响硬盘抢修效率。
腾讯云建议尽快修复此问题：

【修复方法】

- 确认使用脚本：详见后文脚本内容部分，请注意不同系统版本对应不同的脚本；
- 执行修复操作：根据黑石OS选择对应的脚本在控制台执行，相关功能为“自定义脚本”。执行方法请参考官网文档: [自定义脚本](https://cloud.tencent.com/document/product/386/12089)。

【返回信息】

- 成功：输出 success；
- 失败：输出其它信息，请联系售后人员协助处理。

【其它信息】

- 脚本安装三个工具，dmidecode与ebtables 为lsscsi 辅助工具。
- 修复工作仅用于补齐，不会覆盖安装，不会更改现网配置与已有工具版本。

给您带来的不便，敬请谅解，非常感谢您对腾讯云的理解与支持。

# 脚本内容
## centos6

``` 
#!/bin/bash
exec 10>&1
exec 11>&2

exec 1>bmOS_init_log
exec 2>bmOS_init_log

date

yum -y install lsscsi && yum -y install dmidecode && yum -y install ebtables
if [ $? -ne 0 ]; then
    echo "app install fail!!!"
    exec 1>&10 10>&-
    exec 2>&11 11>&-
    echo "app install fail!!!"
    exit 1
fi

# drop BPDU packet
# for re-enter script
ebtables -D INPUT -d BGA -j DROP
ebtables -D FORWARD -d BGA -j DROP
ebtables -D OUTPUT -d BGA -j DROP

ebtables -A INPUT -d BGA -j DROP
ebtables -A FORWARD -d BGA -j DROP
ebtables -A OUTPUT -d BGA -j DROP
if [ $? -ne 0 ]; then
    echo "ebtables configure fail!!!"
    exec 1>&10 10>&-
    exec 2>&11 11>&-
    echo "ebtables configure fail!!!"
    exit 2
fi

# restore stdout stderr
exec 1>&10 10>&-
exec 2>&11 11>&-

echo "success"
exit 0
``` 

## centos7

```
#!/bin/bash
exec 10>&1
exec 11>&2

exec 1>bmOS_init_log
exec 2>bmOS_init_log

date

# drop BPDU packet
ebtables -D INPUT -d BGA -j DROP
ebtables -D FORWARD -d BGA -j DROP
ebtables -D OUTPUT -d BGA -j DROP

ebtables -A INPUT -d BGA -j DROP
ebtables -A FORWARD -d BGA -j DROP
ebtables -A OUTPUT -d BGA -j DROP
if [ $? -ne 0 ]; then
    echo "ebtables configure fail!!!"
    exec 1>&10 10>&-
    exec 2>&11 11>&-
    echo "ebtables configure fail!!!"
    exit 2
fi

# restore stdout stderr
exec 1>&10 10>&-
exec 2>&11 11>&-

echo "success"
exit 0
```


## debian7.8

```
#!/bin/bash

# save stdout stderr
exec 10>&1
exec 11>&2

exec 1>bmOS_init_log
exec 2>bmOS_init_log

date

# fixed err print "stdin:is not a tty"
sed -i 's/mesg n/tty -s \&\& mesg n/g' /root/.profile

# fixed grub bug
sed -i 's/set -e$/set -e;exit 0/g'  /var/lib/dpkg/info/grub-efi-amd64.postinst

apt-get update
dpkg --configure -a
apt-get -f -y install

apt-get install -y lsscsi && apt-get install -y ebtables
if [ $? -ne 0 ]; then
    echo "app install fail!!!"
    exec 1>&10 10>&-
    exec 2>&11 11>&-
    echo "app install fail!!!"
    exit 1
fi

# drop BPDU packet
# for re-enter script
ebtables -D INPUT -d BGA -j DROP
ebtables -D FORWARD -d BGA -j DROP
ebtables -D OUTPUT -d BGA -j DROP

ebtables -A INPUT -d BGA -j DROP
ebtables -A FORWARD -d BGA -j DROP
ebtables -A OUTPUT -d BGA -j DROP
if [ $? -ne 0 ]; then
    echo "ebtables configure fail!!!"
    exec 1>&10 10>&-
    exec 2>&11 11>&-
    echo "ebtables configure fail!!!"
    exit 2
fi

# restore stdout stderr. and close bmOS_init_log
exec 1>&10 10>&-
exec 2>&11 11>&-

echo "success"
exit 0
```

## debian8.2

```
#!/bin/bash

# save stdout stderr
exec 10>&1
exec 11>&2

exec 1>bmOS_init_log
exec 2>bmOS_init_log

date

# fixed err print "stdin:is not a tty"
sed -i 's/mesg n/tty -s \&\& mesg n/g' /root/.profile

# fixed grub bug
sed -i 's/set -e$/set -e;exit 0/g'  /var/lib/dpkg/info/grub-efi-amd64.postinst

apt-get update
dpkg --configure -a
apt-get -f -y install

apt-get install -y lsscsi && apt-get install -y ethtool && apt-get install -y ebtables
if [ $? -ne 0 ]; then
    echo "app install fail!!!"
    exec 1>&10 10>&-
    exec 2>&11 11>&-
    echo "app install fail!!!"
    exit 1
fi

# drop BPDU packet
# for re-enter script
ebtables -D INPUT -d BGA -j DROP
ebtables -D FORWARD -d BGA -j DROP
ebtables -D OUTPUT -d BGA -j DROP

ebtables -A INPUT -d BGA -j DROP
ebtables -A FORWARD -d BGA -j DROP
ebtables -A OUTPUT -d BGA -j DROP
if [ $? -ne 0 ]; then
    echo "ebtables configure fail!!!"
    exec 1>&10 10>&-
    exec 2>&11 11>&-
    echo "ebtables configure fail!!!"
    exit 2
fi

# restore stdout stderr. and close bmOS_init_log
exec 1>&10 10>&-
exec 2>&11 11>&-

echo "success"
exit 0
```

## ubuntu14

```
#!/bin/bash

# save stdout stderr
exec 10>&1
exec 11>&2

exec 1>bmOS_init_log
exec 2>bmOS_init_log

date
apt-get update

# fixed grub bug
sed -i 's/set -e$/set -e;exit 0/g'  /var/lib/dpkg/info/grub-efi-amd64.postinst

dpkg --configure -a
apt-get -f -y install

apt-get install -y lsscsi && apt-get install -y ethtool && apt-get install -y ebtables
if [ $? -ne 0 ]; then
    echo "app install fail!!!"
    exec 1>&10 10>&-
    exec 2>&11 11>&-
    echo "app install fail!!!"
    exit 1
fi

# drop BPDU packet
# for re-enter script
ebtables -D INPUT -d BGA -j DROP
ebtables -D FORWARD -d BGA -j DROP
ebtables -D OUTPUT -d BGA -j DROP

ebtables -A INPUT -d BGA -j DROP
ebtables -A FORWARD -d BGA -j DROP
ebtables -A OUTPUT -d BGA -j DROP
if [ $? -ne 0 ]; then
    echo "ebtables configure fail!!!"
    exec 1>&10 10>&-
    exec 2>&11 11>&-
    echo "ebtables configure fail!!!"
    exit 2
fi

# restore stdout stderr. and close bmOS_init_log
exec 1>&10 10>&-
exec 2>&11 11>&-

echo "success"
exit 0
```


## ubuntu16

```
#!/bin/bash

# save stdout stderr
exec 10>&1
exec 11>&2

exec 1>bmOS_init_log
exec 2>bmOS_init_log

date
apt-get update
apt-get -f -y install
apt-get install -y lsscsi && apt-get install -y ethtool && apt-get install -y ebtables
if [ $? -ne 0 ]; then
    echo "app install fail!!!"
    exec 1>&10 10>&-
    exec 2>&11 11>&-
    echo "app install fail!!!"
    exit 1
fi

# drop BPDU packet
# for re-enter script
ebtables -D INPUT -d BGA -j DROP
ebtables -D FORWARD -d BGA -j DROP
ebtables -D OUTPUT -d BGA -j DROP

ebtables -A INPUT -d BGA -j DROP
ebtables -A FORWARD -d BGA -j DROP
ebtables -A OUTPUT -d BGA -j DROP
if [ $? -ne 0 ]; then
    echo "ebtables configure fail!!!"
    exec 1>&10 10>&-
    exec 2>&11 11>&-
    echo "ebtables configure fail!!!"
    exit 2
fi

# restore stdout stderr. and close bmOS_init_log
exec 1>&10 10>&-
exec 2>&11 11>&-

echo "success"
exit 0
```