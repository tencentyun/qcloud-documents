## 现象描述
使用 SSH 登录 Linux 实例时，出现 “ssh_exchange_identification: Connection closed by remote host” 或 “no hostkey alg”。


## 可能原因
sshd 配置文件权限被修改，可能导致无法使用 SSH 登录。例如 `/var/empty/sshd` 及 `/etc/ssh/ssh_host_rsa_key` 配置文件权限被修改。


## 解决思路
结合实际报错信息，选择对应步骤修改配置文件权限：
 - 报错信息为 “ssh_exchange_identification: Connection closed by remote host”，请参考 [修改 /var/empty/sshd 文件权限](#sshd) 步骤。
 - 报错信息为“no hostkey alg”，请参考 [修改  /etc/ssh/ssh_host_rsa_key 文件权限](#rsa_key) 步骤。



## 处理步骤

### 修改 /var/empty/sshd 文件权限[](id:sshd)
1. [使用 VNC 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35701)。
2. 执行以下命令，查看报错原因。
```
sshd -t
```
返回类似如下信息：
```plaintext
“/var/empty/sshd must be owned by root and not group or world-writable.”
```
3. 执行以下命令，修改 `/var/empty/sshd/` 文件权限。
```
chmod 711 /var/empty/sshd/
```



### 修改  /etc/ssh/ssh_host_rsa_key 文件权限[](id:rsa_key)
1. [使用 VNC 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35701)。
2. 执行以下命令，查看报错原因。
```
sshd -t
```
返回信息中包含如下字段：
```plaintext
“/etc/ssh/ssh_host_rsa_key are too open”
```
3. 执行以下命令，修改 `/etc/ssh/ssh_host_rsa_key` 文件权限。
```
chmod 600 /etc/ssh/ssh_host_rsa_key
```
