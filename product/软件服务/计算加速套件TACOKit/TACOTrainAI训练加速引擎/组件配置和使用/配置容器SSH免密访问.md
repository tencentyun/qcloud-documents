## 操作场景
本文介绍如何配置服务器间的容器 SSH 免密访问。

## 操作步骤


<dx-alert infotype="explain" title="">
本文以两台机器间容器 SSH 免密访问为例，配置步骤需在两台机器上同步。
</dx-alert>

1. 参考 [使用标准登录方式登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)，登录实例。
2. 执行以下命令，允许 root 使用 ssh 服务，并启动服务（默认端口：22）。
```plaintext
sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
```
2. 依次执行以下命令，修改容器内 ssh 默认端口为2222，防止与 host 所使用的22端口冲突。
```plaintext
sed -i 's/#Port 22/Port 2222/' /etc/ssh/sshd_config
```
```plaintext
service ssh restart && netstat -tulpn
```
3. 执行以下命令，设置 root 密码。
```plaintext
passwd root
```
4. 执行以下命令，产生 SSH Key。
```plaintext
ssh-keygen
```
5. 创建 `~/.ssh/config`，并添加以下内容。
```plaintext
# ！注意：
# 如果是CVM机型，则ip是两台机器`ifconfig eth0`显示的ip
# 如果是黑石RDMA机型，则ip是两台机器`ifconfig bond0`显示的ip
Host gpu1
 hostname 10.0.2.8
 port 2222
Host gpu2
 hostname 10.0.2.9
 port 2222
```
6. 保存并退出，完成 host alias 配置。
此时两台机器已互相免密，同时本机自身也免密。您可执行以下命令验证：
```plaintext
ssh-copy-id gpu1
ssh-copy-id gpu2
```


