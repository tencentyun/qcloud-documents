## 概述

TKE 新加的节点可以通过在 `自定义数据` 里填入脚本来进行批量操作，比如统一修改内核参数。但是对于已经添加过的存量节点，如何进行批量操作呢？本文将介绍如何使用开源工具 Ansible 对存量 TKE 节点进行批量操作。

## 原理介绍

Ansible 是 RedHat 开源的一款运维工具，可以直接通过 SSH 协议批量操作机器，不需要事先手动登录每台机器安装依赖什么的，非常方便:

<img style="width:80%" src="https://main.qcloudimg.com/raw/90d1658ff2105497d2ea3a5b54c92bda.png">

## 操作步骤

### 准备 Ansible 控制节点

首先我们需要选取一台机器作为 Ansible 的控制节点，通过这台机器批量发起对存量 TKE 节点的操作。可以选取与集群所在 VPC 中任意一台机器作为控制节点 (包括 TKE 节点)，然后在这台机器上安装 Ansible。

Ubuntu 安装方法:

``` bash
sudo apt update && sudo apt install software-properties-common -y && sudo apt-add-repository --yes --update ppa:ansible/ansible && sudo apt install ansible -y
```

CentOS 安装方法:

``` bash
sudo yum install ansible -y
```

### 准备 hosts.ini

将所有需要进行配置操作的节点内网 IP 配置到 `host.ini` 文件中，每行一个 IP，比如:

```
10.0.3.33
10.0.2.4
```

如果要操作所有节点，可以通过此命令直接一键生成 `hosts.ini`:

``` bash
kubectl get nodes -o jsonpath='{.items[*].status.addresses[?(@.type=="InternalIP")].address}' | tr ' ' '\n' > hosts.ini
```

### 准备要批量执行的脚本

将要批量执行的操作写成脚本，保存成脚本文件。比如自建了镜像仓库，没有权威机构颁发证书，直接使用 HTTP 或 使用 HTTPS 但证书是自签发的，默认情况下 dockerd 拉取镜像时会报错，可以通过批量修改节点 dockerd 配置，将自建仓库地址添加到 dockerd 配置的 `insecure-registries` 中来让 dockerd 忽略证书校验。准备 `modify-dockerd.sh`:

```
# yum install -y jq # centos
apt install -y jq # ubuntu
cat /etc/docker/daemon.json | jq '."insecure-registries" += ["myharbor.com"]' > /tmp/daemon.json
cp /tmp/daemon.json /etc/docker/daemon.json
systemctl restart dockerd
```

### 使用 Ansible 批量执行脚本

通常我们的 TKE 节点在添加时都指定同一个 ssh 登录密钥或者密码，如果使用密钥，先准备好密钥文件，比如保存成 `tke.key`，然后 `chmod 0600 tke.key` 一下。

如果是使用密码登录，先将密码输入到 PASS 变量:

```
read -s PASS
```

Ubuntu 节点的 ssh 用户名默认为 ubuntu，批量执行示例:

```
ansible all -i hosts.ini --ssh-common-args="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" --user ubuntu --become --become-user=root -e "ansible_password=$PASS" -m script -a "modify-dockerd.sh"
```

其它系统节点的 ssh 用户名默认为 root，批量执行示例:

```
ansible all -i hosts.ini --ssh-common-args="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" --user root -e "ansible_password=$PASS" -m script -a "modify-dockerd.sh"
```

如果是使用密钥登录，Ubuntu 节点批量执行示例:

```
ansible all -i hosts.ini --ssh-common-args="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" --user ubuntu --become --become-user=root --private-key=tke.key -m script -a "modify-dockerd.sh"
```

其它系统的节点使用密钥登录批量执行示例:

```
ansible all -i hosts.ini --ssh-common-args="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" --user root -m script -a "modify-dockerd.sh"
```