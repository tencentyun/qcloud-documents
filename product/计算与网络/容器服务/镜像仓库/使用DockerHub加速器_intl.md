## How to Use DockerHub Image Accelerator
### Quick Installation Using Script
Available soon.

### Manual Installation and Configuration
#### Ubuntu
Configure Docker accelerator:

You can use the following script to add the mirror configuration into the launch parameters of Docker Daemon.
- If your system is Ubuntu 12.04 14.04, Docker 1.9 or above.
```shell
echo "DOCKER_OPTS=\"\$DOCKER_OPTS --registry-mirror=https://mirror.ccs.tencentyun.com" | sudo tee -a /etc/default/docker
sudo service docker restart
```
- If your system is Ubuntu 15.04 16.04, Docker 1.9 or above.
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
Configure Docker accelerator:

You can use the following script to add the mirror configuration into the launch parameters of Docker Daemon.
Note: System requirement: CentOS 7 or above, Docker 1.9 or above.
```shell
sudo cp -n /lib/systemd/system/docker.service /etc/systemd/system/docker.service
sudo sed -i "s | ExecStart=/usr/bin/docker daemon | ExecStart=/usr/bin/docker daemon --registry-mirror=https://mirror.ccs.tencentyun.com| g" /etc/systemd/system/docker.service
sudo systemctl daemon-reload
sudo service docker restart
```

