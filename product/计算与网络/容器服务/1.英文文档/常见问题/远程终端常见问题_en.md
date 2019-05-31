## FAQs on Remote Terminal

### 1. What if there is no bash in my container?
You can enter the command you wish to execute in the command line, and the returned result for this command will be displayed on the screen. You may consider the command line as a simplified bash without certain features (such as auto completion). It is recommended that you execute relevant command to install bash before executing other operations.

### 2. What if I can't find certain tools (such as vim, netstat) when I log in to the container?
You can download required tools by using commands such as "apt-get install vim" and "net-tools" (execute ``yum install vim`` in CentOS).

### 3. Why can't I find the tool when executing "apt-get install"?
When this occurs, you can first execute "apt-get update" to update software list, then proceed with the installation (execute ``yum updateinfo`` in CentOS).

### 4. The software installation is too slow when I execute "apt-get".
This may be caused by a slow connection when your machine needs to access a foreign software source.

#### Ubuntu 16.04
For container whose system is Ubuntu 16.04, you can execute the following command to configure the apt source as a Tencent Cloud source server by simply copying the following command to the terminal.
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

#### CentOS 7
For container whose system is CentOS 7, copy the following command into the container and execute:
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
Next, execute command
`yum clean all && yum clean metadata && yum clean dbcache && yum makecache`
to complete the process.

Modifying the source address is only a temporary solution because user modifications become invalid when the container is re-scheduled. Thus, you can permanently address this problem by doing it upon image creation. You can do it in two ways:

Modify the Dockerfile used to create container image
Modify the source address in the RUN field of the Dockerfile, based on different systems. For example, if the image is based on Ubuntu, add the following items:

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

You can do it in a similar way for images based on CentOS.


### 5. How can I use custom tools in containers?
You can use our one-click file upload feature which will become available soon.

### 6. How do I copy on-site files (such as dump or log) to my computer?
You can use our container file download feature which will become available soon.

### 7. I can't upload/download files on Remote Terminal.
The possible reason is that the tar program is not installed in your container image. Please install the tar program and try again (see the second question).

### 8. The tool I previously installed disappeared.
The possible reason is that Kubernetes will pull an image to create a new container when re-scheduling your container. Tools that do not exist in the image will not be contained in new container. It is recommended that users include some commonly used troubleshooting tools when creating images.

### 9. How do I copy text on the remote terminal?
You can just select and copy the text.

### 10. How do I paste copied text?
Press Shift + Insert.

### 11. Why am I disconnected?
One possible reason is that you changed container status by performing actions on the container or CVM in other Tencent Cloud pages. This situation also occurs when you haven't done any actions for a long time (3 minutes), in which case the server will terminate the connection.

### 12. I got the message "TERM environment variable not set" while executing commands such as "top"?
Execute ``export TERM linux``.

### 13. When I enter a directory with a long absolute path, only "<" and a part of the path is displayed after bash prompt?
This is because the bash prompt is configured to display "<User name>@<CVM name> <Current directory>" by default. By default, if the length of the current path exceeds a certain limit, bash will only display "<" and the last part of the path.

