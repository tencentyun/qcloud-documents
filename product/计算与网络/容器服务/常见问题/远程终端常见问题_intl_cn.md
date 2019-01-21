## 远程终端常见问题

### 1.我的容器里面没有bash，怎么办？
答：如果发现没有bash，可以在命令行栏输入您想执行的命令，屏幕会显示该命令的返回结果，可以将命令行栏看做一个缺少例如自动补全等其他功能的精简版bash。建议执行命令安装一个bash后再执行后续操作。

### 2.当我登录到容器里面，发现没有vim，netstat 等工具，怎么办？
答：可以通过apt-get install vim， net-tools等命令下载你所需要的工具（centos 下执行 yum install vim）。

### 3.为什么运行apt-get install 说找不到我想要的工具？
答：如果出现这个问题，可以先执行apt-get update 命令升级软件列表，再进行安装（centos 下执行 yum updateinfo）。

### 4.为什么运行apt-get 安装软件如此之慢？
答：如果觉得安装太慢，可能因为机器访问国外软件源速度过慢的原因。

#### Ubuntu 16.04 系统
对于系统为 Ubuntu 16.04 的容器，可以运行以下命令将apt的源设置为腾讯云的源服务器，复制以下命令粘贴到终端执行即可。
```shell
cat << ENDOF > /etc/apt/sources.list
deb http://mirrors.tencentyun.com/ubuntu/ xenial main restricted universe multiverse
deb http://mirrors.tencentyun.com/ubuntu/ xenial-security main restricted universe multiverse
deb http://mirrors.tencentyun.com/ubuntu/ xenial-updates main restricted universe multiverse
deb-src http://mirrors.tencentyun.com/ubuntu/ xenial main restricted universe multiverse
deb-src http://mirrors.tencentyun.com/ubuntu/ xenial-security main restricted universe multiverse
deb-src http://mirrors.tencentyun.com/ubuntu/ xenial-updates main restricted universe multiverse
ENDOF
```

#### CentOS 7 系统
对于系统为CentOS 7的容器，复制并粘贴以下代码至容器内运行：
```shell
cat << ENDOF > /etc/yum.repos.d/CentOS-Base.repo
[os]
name=Qcloud centos os - \$basearch
baseurl=http://mirrors.tencentyun.com/centos1/\$releasever/os/\$basearch/
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

[updates]
name=Qcloud centos updates - \$basearch
baseurl=http://mirrors.tencentyun.com/centos1/\$releasever/updates/\$basearch/
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

#[centosplus]
#name=Qcloud centosplus - \$basearch
#baseurl=http://mirrors.tencentyun.com/centos1/\$releasever/centosplus/\$basearch/
#enabled=1
#gpgcheck=1
#gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

#[cloud]
#name=Qcloud centos contrib - \$basearch
#baseurl=http://mirrors.tencentyun.com/centos1/\$releasever/cloud/$basearch/openstack-kilo/
#enabled=1
#gpgcheck=1
#gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

#[cr]
#name=Qcloud centos cr - \$basearch
#baseurl=http://mirrors.tencentyun.com/centos1/\$releasever/cr/\$basearch/
#enabled=1
#gpgcheck=1
#gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

[extras]
name=Qcloud centos extras - \$basearch
baseurl=http://mirrors.tencentyun.com/centos1/\$releasever/extras/\$basearch/
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

#[fasttrack]
#name=Qcloud centos fasttrack - \basearch
#baseurl=http://mirrors.tencentyun.com/centos1/\$releasever/fasttrack/\$basearch/
#enabled=1
#gpgcheck=1
#gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
ENDOF
```
然后执行命令
yum clean all && yum clean metadata && yum clean dbcache && yum makecache
即可。

直接修改源地址为临时解决方案，当容器被重新调度后，用户所作修改将会失效，所以一劳永逸的解决方案是在创建镜像时解决该问题。方法有以下两种：

修改创建容器镜像的Dockerfile
在Dockerfile的RUN字段根据系统的不同添加直接修改源地址，如在一个基于Ubuntu系统的镜像中，加入以下项：

```shell
RUN cat << ENDOF > /etc/apt/sources.list
deb http://mirrors.tencentyun.com/ubuntu/ xenial main restricted universe multiverse
deb http://mirrors.tencentyun.com/ubuntu/ xenial-security main restricted universe multiverse
deb http://mirrors.tencentyun.com/ubuntu/ xenial-updates main restricted universe multiverse
#deb http://mirrors.tencentyun.com/ubuntu/ xenial-proposed main restricted universe multiverse
#deb http://mirrors.tencentyun.com/ubuntu/ xenial-backports main restricted universe multiverse
deb-src http://mirrors.tencentyun.com/ubuntu/ xenial main restricted universe multiverse
deb-src http://mirrors.tencentyun.com/ubuntu/ xenial-security main restricted universe multiverse
deb-src http://mirrors.tencentyun.com/ubuntu/ xenial-updates main restricted universe multiverse
#deb-src http://mirrors.tencentyun.com/ubuntu/ xenial-proposed main restricted universe multiverse
#deb-src http://mirrors.tencentyun.com/ubuntu/ xenial-backports main restricted universe multiverse
ENDOF
```

对于CentOS系统的镜像类似。


### 5.如果我想用在容器中使用自制的工具，我该怎么办？
答：敬请期待我们后续的一键上传文件至容器功能。

### 6.如果我拷贝现场文件，例如dump或者日志到本地分析，我该怎么办？
答：敬请期待我们后续的容器文件下载功能。

### 7.为什么我用不了文件上传到容器或者下载到本地功能？
答：这可能是因为您的容器镜像里没有安装tar程序，请先安装tar程序再重试（安装方法请参考上面第二条）。

### 8.为什么上一次我安装的工具不见了？
答：这可能是因为kubernetes重新调度您的容器，调度过程中会拉取镜像生成新的容器，如果镜像里面没有您之前安装的工具，新的容器是不会包含这些工具的。建议用户在制作镜像的时候包括一些常用的排错工具。

### 9.我要怎么复制控制台里的文字？
答：只要选中您想复制的内容，即可复制被选中的文字。

### 10.我要怎么粘贴复制好的文字？
答：同时按下 Shift + Insert 即可。

### 11.为什么我会断开链接？
答：这可能是因为您在腾讯云其他页面对容器、云主机进行操作更改了容器的状况，也有可能是长时间(3分钟)不进行任何操作，服务器断开了这个链接。

### 12.运行top 命令等出现 TERM environment variable not set 的错误，我该怎么办？
答：执行命令 export TERM linux 即可。

### 13.为何进入绝对路径较长的目录后，bash提示符只显示 “<”和部分路径？
答：这是因为默认的bash提示符被设置为显示 “用户名@主机名 当前目录”。 如果当前路径长于一定长度，bash默认会显示“<”与路径的最后一部分。
