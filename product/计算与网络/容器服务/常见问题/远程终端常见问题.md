### 容器里面没有 bash，怎么办？

如果发现没有 bash，您可以在命令行中输入您想执行的命令，屏幕会显示该命令的返回结果。您可以将命令行看做一个缺少自动补全等其他功能的精简版 bash。建议您先执行安装 bash 的命令，再执行后续操作。

### 为什么运行 apt-get 安装软件如此之慢？
如果您在使用 `apt-get` 安装软件速度过慢，有可能是因为机器访问国外软件源速度过慢引起。我们根据不同操作系统的容器为您提供对应的提速方案，您可根据实际情况进行操作：

#### 注意事项
选择提速解决方案之前，请您准确识别容器操作系统，避免操作无法正常进行。您可参考以下方式进行识别：
 - Ubuntu 系统：执行命令 `cat /etc/lsb-release` ，验证是否存在 `/etc/lsb-release` 文件。
 - CentOS 系统：执行命令 `cat /etc/redhat-release`，验证是否存在 `/etc/redhat-release` 文件。
 - Debian 系统：执行命令 `cat /etc/debian_version`，验证是否存在 `/etc/debian_version` 文件。

#### 解决方案<span id="solve"></span>

##### Ubuntu 16.04系统
对于系统为 Ubuntu 16.04的容器，您可以在终端运行以下命令，将 apt 的源设置为腾讯云的源服务器：
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

##### CentOS 7系统

对于系统为 CentOS 7的容器，您可以在终端执行以下操作，直接修改源地址提高安装速度：
1. 将以下代码复制并粘贴至容器内运行：
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
2. 执行以下命令，清空并重建 YUM 缓存。
```
yum clean all && yum clean metadata && yum clean dbcache && yum makecache
```

##### Debian 系统

对于系统为 Debian 的容器，您可以在终端运行以下命令，将 apt 的源设置为腾讯云的源服务器：
```shell
cat << ENDOF > /etc/apt/sources.list
deb http://mirrors.tencentyun.com/debian stretch main contrib non-free
deb http://mirrors.tencentyun.com/debian stretch-updates main contrib non-free
deb http://mirrors.tencentyun.com/debian-security stretch/updates main

deb-src http://mirrors.tencentyun.com/debian stretch main contrib non-free
deb-src http://mirrors.tencentyun.com/debian stretch-updates main contrib non-free
deb-src http://mirrors.tencentyun.com/debian-security stretch/updates main
ENDOF
```

#### 问题总结

在容器中直接修改源地址为临时解决方案，当容器被重新调度后，您所作的修改将会失效，建议您在创建镜像时解决该问题。具体的操作方法如下：

修改创建容器镜像的 Dockerfile，在 Dockerfile 的 RUN 字段中，添加对应操作系统 [解决方案](#solve) 中提供的信息修改源地址。例如，在一个基于 Ubuntu 系统的镜像的 Dockerfile 中，加入以下内容：
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



### 当登录容器后，发现没有 vim，netstat 等工具，怎么办？

您可以通过 apt-get install vim， net-tools 等命令下载您所需要的工具（CentOS 下执行 yum install vim）。

### 为什么运行 apt-get install 命令，提示找不到工具？

您可以通过以下操作，安装软件。
1. 执行以下命令，升级软件列表。
```
apt-get update
```
2. 执行以下命令， 安装软件（CentOS 下执行 yum updateinfo）。
```
apt-get install
```

### 如果想在容器中使用自制的工具，怎么办？

您可以在进入远程终端页面后，单击右下方的文件助手，即可进行上传和下载操作。

### 如何拷贝现场文件，例如 dump 或者日志到本地分析？

您可以在进入远程终端页面后，单击右下方的文件助手，即可进行上传和下载操作。

### 为什么用不了文件上传到容器或者下载到本地功能？

可能因为您的容器镜像里没有安装 tar 程序，您可以通过 apt-get install vim， net-tools 等命令（CentOS 下执行 yum install vim）先安装 tar 程序再重试。

### 为什么之前安装的工具不见了？

可能因为 kubernetes 重新调度您的容器，调度过程中会拉取镜像生成新的容器，如果镜像里面没有您之前安装的工具，新的容器是不会包含这些工具的。建议您在制作镜像时，安装一些常用的排错工具。

### 怎么复制控制台里的文字？

只要选中您想复制的内容，即可复制被选中的文字。

### 怎么粘贴复制好的文字？

同时按下 Shift + Insert 即可。

### 为什么会断开链接？

可能因为您在腾讯云其他页面对容器、云服务器进行操作更改了容器的状况，也有可能是长时间（3分钟）不进行任何操作，服务器断开了这个链接。

### 运行 top 命令等出现 TERM environment variable not set 的错误，怎么办？

执行命令 export TERM linux 即可。

### 为何进入绝对路径较长的目录后，bash 提示符只显示 “<” 和部分路径？

因为默认的 bash 提示符被设置为显示 “用户名@主机名 当前目录”。 如果当前路径长于一定长度，bash 默认会显示 “<” 与路径的最后一部分。

