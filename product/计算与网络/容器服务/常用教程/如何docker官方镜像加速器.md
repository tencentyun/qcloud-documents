## 如何使用DockerHub镜像加速器
### 使用脚本快速安装
敬请期待。

### 手动安装配置
#### Ubuntu
配置Docker加速器：

您可以使用如下的脚本将mirror的配置添加到docker daemon的启动参数中。
- 如果您的系统是 Ubuntu 12.04 14.04，Docker 1.9 以上。
```shell
echo "DOCKER_OPTS=\"\$DOCKER_OPTS --registry-mirror=https://mirror.ccs.tencentyun.com" | sudo tee -a /etc/default/docker
sudo service docker restart
```
- 如果您的系统是 Ubuntu 15.04 16.04，Docker 1.9 以上。
```shell
sudo mkdir -p /etc/systemd/system/docker.service.d
sudo tee /etc/systemd/system/docker.service.d/mirror.conf <<-'EOF'
[Service]
ExecStart=
ExecStart=/usr/bin/docker daemon -H fd:// --registry-mirror=https://mirror.ccs.tencentyun.com
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker
```

#### CentOS
配置Docker加速器：

您可以使用如下的脚本将mirror的配置添加到docker daemon的启动参数中。
注意：系统要求 CentOS 7 以上，Docker 1.9 以上。
```shell
sudo cp -n /lib/systemd/system/docker.service /etc/systemd/system/docker.service
sudo sed -i "s | ExecStart=/usr/bin/docker daemon | ExecStart=/usr/bin/docker daemon --registry-mirror=https://mirror.ccs.tencentyun.com| g" /etc/systemd/system/docker.service
sudo systemctl daemon-reload
sudo service docker restart
```
