## 操作场景
容器服务 TKE 集群新增节点可通过在“自定义数据”中填入脚本来进行批量操作，例如统一修改内核参数。但如需对已新增的存量节点进行批量操作，您可参考本文使用开源工具 Ansible 进行操作。


## 原理介绍
Ansible 是一款流行的开源运维工具，可以直接通过 SSH 协议批量操作机器，无需事先进行手动安装依赖等操作，十分便捷。原理示意图如下：
<img style="width:70%" src="https://main.qcloudimg.com/raw/90d1658ff2105497d2ea3a5b54c92bda.png" data-nonescope="true">

## 操作步骤
### 准备 Ansible 控制节点
1. 选取实例作为 Ansible 的控制节点，通过此节点批量发起对存量 TKE 节点的操作。可选择与集群所在私有网络 VPC 中任意实例作为控制节点（包括 TKE 节点）。
2. 选定控制节点后，选择对应方式安装 Ansible：
 - Ubuntu 操作系统安装方式：
``` bash
sudo apt update && sudo apt install software-properties-common -y && sudo apt-add-repository --yes --update ppa:ansible/ansible && sudo apt install ansible -y
```
 - CentOS 操作系统安装方式：
``` bash
sudo yum install ansible -y
```


### 准备配置文件
将所有需要进行配置操作的节点内网 IP 配置到 `host.ini` 文件中，每行一个 IP。示例如下：
```
10.0.3.33
10.0.2.4
```
如需操作所有节点，可通过以下命令一键生成 `hosts.ini` 文件。
``` bash
kubectl get nodes -o jsonpath='{.items[*].status.addresses[?(@.type=="InternalIP")].address}' | tr ' ' '\n' > hosts.ini
```

### 准备批量执行脚本
将需批量执行的操作写入脚本，并保存为脚本文件。示例如下：
自建镜像仓库后没有权威机构颁发证书，直接使用 HTTP 或 HTTPS 自签发的证书，默认情况下 dockerd 拉取镜像时会报错。此时可通过批量修改节点的 dockerd 配置，将自建仓库地址添加到 dockerd 配置的 `insecure-registries` 中使 dockerd 忽略证书校验。脚本文件 `modify-dockerd.sh` 内容如下：
```
# yum install -y jq # centos
apt install -y jq # ubuntu
cat /etc/docker/daemon.json | jq '."insecure-registries" += ["myharbor.com"]' > /tmp/daemon.json
cp /tmp/daemon.json /etc/docker/daemon.json
systemctl restart dockerd
```

### 使用 Ansible 批量执行脚本
通常 TKE 节点在新增时均指向一个 SSH 登录密钥或密码。请按照实际情况执行以下操作：


#### 使用密钥
1. 准备密钥文件，例如 `tke.key`。
2. 执行以下命令，授权密钥文件。
```
chmod 0600 tke.key
```
3. 批量执行脚本：
 - Ubuntu 操作系统节点批量执行示例如下：
```
ansible all -i hosts.ini --ssh-common-args="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" --user ubuntu --become --become-user=root --private-key=tke.key -m script -a "modify-dockerd.sh"
```
 - 其他操作系统节点批量执行示例如下：
```
ansible all -i hosts.ini --ssh-common-args="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" --user root -m script -a "modify-dockerd.sh"
```


#### 使用密码
1. 执行以下命令，将密码输入至 PASS 变量。
```
read -s PASS
```
2. 批量执行脚本：
 - Ubuntu 操作系统节点的 SSH 用户名默认为 ubuntu，批量执行示例如下：
```
ansible all -i hosts.ini --ssh-common-args="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" --user ubuntu --become --become-user=root -e "ansible_password=$PASS" -m script -a "modify-dockerd.sh"
```
 - 其他系统节点的 SSH 用户名默认为 root，批量执行示例如下：
```
ansible all -i hosts.ini --ssh-common-args="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" --user root -e "ansible_password=$PASS" -m script -a "modify-dockerd.sh"
```
