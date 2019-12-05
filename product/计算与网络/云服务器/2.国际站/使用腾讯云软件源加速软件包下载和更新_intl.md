To solve the problem that the access to the official source is too slow during software dependencies installation, Tencent Cloud has built cache service for some software. You can accelerate the installation of dependency packages using Tencent Cloud software origin server, and CVM without public network egress can use a software origin server via a private network to facilitate construction of service architecture. Tencent Cloud software origin server supports public network access and private network access.

Public network domain name

```
http://mirrors.cloud.tencent.com/
```

Private network domain name

```
http://mirrors.tencentyun.com/
```

The following are example illustrations based on private network domain names. If you access these software sources via a public network, replace the private network domain name with a public network domain name.

## Accelerating pip Using Tencent Cloud Image Source
### Temporary Use
```
Before use, make sure you have installed python.
```

Execute the following command to use Tencent Cloud pypi software source:
```
pip install -i http://mirrors.tencentyun.com/pypi/simple <some-package>
```
Note: `simple` in the path must be added.

### Set as Default
Modify the file `~/.pip/pip.conf` (create one if it does not exist). Update `index-url` to Tencent Cloud path, for example:
```
[global]
index-url = http://mirrors.tencentyun.com/pypi/simple
trusted-host = mirrors.tencentyun.com
```
### Synchronization Period
Tencent Cloud makes synchronization from `pypi.python.org` official website every day.

## Accelerating Maven Using Tencent Cloud Image Source
```
Before use, make sure you have installed JDK and Maven
```

### Setting Method

Open Maven setting file `settings.xml` and configure the following repository mirror:

    <mirror>
        <id>nexus-tencentyun</id>
        <mirrorOf>*</mirrorOf>
        <name>Nexus tencentyun</name>
        <url>http://mirrors.tencentyun.com/nexus/repository/maven-public/</url>
    </mirror> 

## Accelerating npm Using Tencent Cloud Image Source
```
Before use, make sure you have installed Node.js and npm.
```
### Setting Method
Execute the following command:
```
npm config set registry http://mirrors.tencentyun.com/npm/ 
```

## Accelerating docker Using Tencent Cloud Image Source
### Tencent Cloud Container Service (CCS) Cluster
When creating a node, the CVM in CCS cluster automatically installs docker service and configure Tencent Cloud private network image, without the need of manual configuration.

### Tencent Cloud CVM
```
Make sure you have installed docker on CVM. Only Docker 1.3.2 and above support Docker Hub Mirror mechanism. If you have not installed Docker or the installed version is too low, please install it or upgrade your version.
```
- For such systems as Ubuntu 14.04, Debian, CentOS 6, Fedora, OpenSUSE. The configuration may be slightly different in other versions:
Modify Docker configuration file `/etc/default/docker`
```
DOCKER_OPTS="--registry-mirror=https://mirror.ccs.tencentyun.com"
```

- For Centos 7:
Modify Docker configuration file `/etc/sysconfig/docker`
```
OPTIONS='--registry-mirror=https://mirror.ccs.tencentyun.com'
```

- For Windows:
When using Boot2Docker, enter Boot2Docker Start Shell and execute:
```
sudo su echo "EXTRA_ARGS=\"-registry-mirror=https://mirror.ccs.tencentyun.com\"" >> /var/lib/boot2docker/profile  exit 
```
Restart Boot2Docker

## Accelerating MariaDB Using Tencent Cloud Image
1. Configure MariaDB yum repo file
Create `MariaDB.repo` file under `/etc/yum.repos.d/` (CentOS 7 is taken as an example and the actual address of operating system yum repos prevails):
```
vi /etc/yum.repos.d/MariaDB.repo
```
Write the following:
```
# MariaDB 10.2 CentOS7-amd64
[mariadb]  
name = MariaDB  
baseurl = http://mirrors.tencentyun.com/mariadb/yum/10.2/centos7-amd64/
gpgkey = http://mirrors.tencentyun.com/mariadb/yum/RPM-GPG-KEY-MariaDB
gpgcheck=1  
```

2. Execute command `yum clean all`
3. Install MariaDB with yum
Execute `yum install MariaDB-client MariaDB-server`

## Accelerating MongoDB Using Tencent Cloud Image
### CentOS and Redhat Systems
```
In the example, MongoDB V3.4 is installed. If you need to install another version, change the version number in the mirror path.
```
1. Create file `/etc/yum.repos.d/mongodb.repo` and write the following content:
```
[mongodb-org-3.4]
name=MongoDB Repository
baseurl=http://mirrors.tencentyun.com/mongodb/yum/redhat/$releasever/3.4/
gpgcheck=0
enabled=1
```
2. Install mongodb
```
yum install -y mongodb-org
```

### Debian System
```
In the example, MongoDB V3.4 is installed. If you need to install another version, change the version number in the mirror path.
```
1. Import MongoDB GPG public key
```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
```

2. Configure mirror path
```
#Debian7
echo "deb http://mirrors.tencentyun.com/mongodb/apt/debian wheezy/mongodb-org/3.4 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list
#Debian8
echo "deb http://mirrors.tencentyun.com/mongodb/apt/debian jessie/mongodb-org/3.4 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list
```

3. Install mongodb
```
sudo apt-get install -y mongodb-org
```

### Ubuntu System
```
In the example, MongoDB V3.4 is installed. If you need to install another version, change the version number in the mirror path.
```
1. Import MongoDB GPG public key
```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
```

2. Configure mirror path
```
#Ubuntu 12.04
echo "deb [ arch=amd64 ] http://mirrors.tencentyun.com/mongodb/apt/ubuntu precise/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list
#Ubuntu 14.04
echo "deb [ arch=amd64 ] http://mirrors.tencentyun.com/mongodb/apt/ubuntu trusty/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list
#Ubuntu 16.04
echo "deb [ arch=amd64,arm64 ] http://mirrors.tencentyun.com/mongodb/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list
```
3. Install mongodb
```
sudo apt-get install -y mongodb-org
```

## Accelerating Rubygems Using Tencent Cloud Image Source
`Make sure that you have installed Ruby locally`
### Modifying Configuration
Execute the following command to modify RubyGems source address.
```
gem source -r https://rubygems.org/
gem source -a http://mirrors.tencentyun.com/rubygems/
```

### Synchronization Period
Tencent Cloud makes synchronization from `https://rubygems.org/` official website every day.
