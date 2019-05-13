为解决软件依赖安装时官方源访问速度慢的问题，腾讯云为一些软件搭建了缓存服务。您可以通过使用腾讯云软件源站来提升依赖包的安装速度，同时没有公网出口的云服务器也可以通过内网使用软件源站，方便用户自由搭建服务架构。

## 使用腾讯云镜像源加速pip
### 临时使用
```
使用前请确保您已安装python
```

运行以下命令以使用腾讯云pypi软件源：
```
pip install -i http://mirrors.tencentyun.com/pypi/simple <some-package>
```
注意：必须加上路径中的`simple`

### 设为默认
修改 `~/.pip/pip.conf` (没有就创建一个)文件，更新`index-url`至腾讯云路径，如：
```
[global]
index-url = http://mirrors.tencentyun.com/pypi/simple
trusted-host = mirrors.tencentyun.com
```
### 同步周期
腾讯云每天从`pypi.python.org`官方同步一次。

## 使用腾讯云镜像源加速maven
```
使用前请确保您已安装JDK及Maven
```

### 设置方法

打开maven的设置文件`settings.xml`，配置如下repository mirror：

    <mirror>
        <id>nexus-tencentyun</id>
        <mirrorOf>*</mirrorOf>
        <name>Nexus tencentyun</name>
        <url>http://mirrors.tencentyun.com/nexus/repository/maven-public/</url>
    </mirror> 

## 使用腾讯云镜像源加速npm
```
使用前请确保您已安装Node.js及npm
```
### 设置方法
运行以下命令：
```
npm config set registry http://mirrors.tencentyun.com/npm/ 
```

## 使用腾讯云镜像源加速docker
### 腾讯云容器服务CCS集群
无需手动配置，CCS集群中的CVM主机在创立节点时会自动安装docker服务并配置腾讯云内网镜像。

### 腾讯云云服务器CVM
```
请确保您已在云主机上安装docker。Docker 1.3.2版本以上才支持Docker Hub Mirror机制，如果您还没有安装Docker或者版本过低，请先执行安装或升级操作。
```
- 适用于 Ubuntu 14.04、Debian、CentOS 6 、Fedora、OpenSUSE等系统，其他版本可能有细微不同：
修改 Docker 配置文件`/etc/default/docker`
```
DOCKER_OPTS="--registry-mirror=https://mirror.ccs.tencentyun.com"
```

- 适用于 Centos 7：
修改 Docker 配置文件`/etc/sysconfig/docker`
```
OPTIONS='--registry-mirror=https://mirror.ccs.tencentyun.com'
```

- 适用于Windows：
在使用Boot2Docker的前提下，进入Boot2Docker Start Shell，并执行
```
sudo su echo "EXTRA_ARGS=\"–registry-mirror=https://mirror.ccs.tencentyun.com\"" >> /var/lib/boot2docker/profile  exit 
```
重启Boot2Docker

## 使用腾讯云镜像加速MariaDB
1. 配置MariaDB的yum repo文件
在`/etc/yum.repos.d/`下创建`MariaDB.repo`文件(以CentOS 7为例，以操作系统yum repos的实际地址为准)：
```
vi /etc/yum.repos.d/MariaDB.repo
```
写入以下内容：
```
# MariaDB 10.2 CentOS7-amd64
[mariadb]  
name = MariaDB  
baseurl = http://mirrors.tencentyun.com/mariadb/yum/10.2/centos7-amd64/
gpgkey = http://mirrors.tencentyun.com/mariadb/yum/RPM-GPG-KEY-MariaDB
gpgcheck=1  
```

2. 执行`yum clean all`命令
3. 使用yum安装MariaDB
执行`yum install MariaDB-client MariaDB-server`

## 使用腾讯云镜像加速MongoDB
### CentOS 及 Redhat系统
```
以安装MongoDB 3.4版本为例，如果需要安装其他版本，请更改mirror路径中的版本号
```
1. 新建 `/etc/yum.repos.d/mongodb.repo`文件，写入以下内容为
```
[mongodb-org-3.4]
name=MongoDB Repository
baseurl=http://mirrors.tencentyun.com/mongodb/yum/redhat/$releasever/mongodb-org/3.4/x86_64/
gpgcheck=0
enabled=1
```
2. 安装mongodb
```
yum install -y mongodb-org
```

### Debian系统
```
以安装MongoDB 3.4版本为例，如果需要安装其他版本，请更改mirror路径中的版本号
```
1. 导入MongoDB GPG 公钥
```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
```

2. 配置mirror路径
```
#Debian7
echo "deb http://mirrors.tencentyun.com/mongodb/apt/debian wheezy/mongodb-org/3.4 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list
#Debian8
echo "deb http://mirrors.tencentyun.com/mongodb/apt/debian jessie/mongodb-org/3.4 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list
```

3. 安装mongodb
```
sudo apt-get install -y mongodb-org
```

### Ubuntu系统
```
以安装MongoDB 3.4版本为例，如果需要安装其他版本，请更改mirror路径中的版本号
```
1. 导入MongoDB GPG 公钥
```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
```

2. 配置mirror路径
```
#Ubuntu 12.04
echo "deb [ arch=amd64 ] http://mirrors.tencentyun.com/mongodb/apt/ubuntu precise/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list
#Ubuntu 14.04
echo "deb [ arch=amd64 ] http://mirrors.tencentyun.com/mongodb/apt/ubuntu trusty/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list
#Ubuntu 16.04
echo "deb [ arch=amd64,arm64 ] http://mirrors.tencentyun.com/mongodb/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list
```
3. 安装mongodb
```
sudo apt-get install -y mongodb-org
```

## 使用腾讯云镜像源加速Rubygems
`请确保您本地已经安装了 Ruby`
### 修改配置
运行以下命令修改 RubyGems 源地址
```
gem source -r https://rubygems.org/
gem source -a http://mirrors.tencentyun.com/rubygems/
```

### 同步周期
腾讯云每天从`https://rubygems.org/`官方同步一次。