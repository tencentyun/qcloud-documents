Source address of Docker: `https://mirror.ccs.tencentyun.com`

## CCS Cluster CVM
When a node is created, Docker service is installed and image is configured automatically. The configuration items are as follows:
```shell
[root@VM_1_2_centos ~]# cat /etc/docker/dockerd 
IPTABLES="--iptables=false"
STORAGE_DRIVER="--storage-driver=overlay2"
IP_MASQ="--ip-masq=false"
LOG_LEVEL="--log-level=warn"
REGISTRY_MIRROR="--registry-mirror=https://mirror.ccs.tencentyun.com"
```

## CVM Configuration
### Linux:
- Applicable to Ubuntu14.04, Debian, CentOS6, Fedora and OpenSUSE. For other versions, the configuration may be slightly different.
Docker configuration file `/etc/default/docker` is modified as follows:
```shell
DOCKER_OPTS="--registry-mirror=https://mirror.ccs.tencentyun.com"
```
- Applicable to Centos7.
The Docker configuration file `vi /etc/sysconfig/docker` is modified as follows:
```shell
OPTIONS='--registry-mirror=https://mirror.ccs.tencentyun.com'
```
>**Note:**
>Only Docker 1.3.2 or above supports Docker Hub Mirror mechanism. If you have not installed Docker or the installed version is too low, please install it or upgrade your version.

### Windows:
If you are using Boot2Docker, go to Boot2Docker Start Shell and execute the following command:
```shell
sudo su echo "EXTRA_ARGS=\"-registry-mirror=https://mirror.ccs.tencentyun.com"">> /var/lib/boot2docker/profile  exit #  Restart Boot2Docker
```

## Start Docker
Execute the following command:
```shell
sudo service docker start
```

