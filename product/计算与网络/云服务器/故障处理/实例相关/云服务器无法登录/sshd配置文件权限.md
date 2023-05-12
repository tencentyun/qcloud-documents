## 现象描述
使用 SSH 登录 Linux 实例时，报错 **ssh_exchange_identification: Connection closed by remote host** 或 **no hostkey alg**。


## 可能原因
<table>
<thead>
  <tr>
    <th>可能原因</th>
    <th>处理措施</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>/var/empty/sshd 文件权限未修改</td>
    <td ><a href="#sshd">检查 /var/empty/sshd 文件权限是否已修改</a></td>
  </tr>
  <tr>
    <td> /etc/ssh/ssh_host_rsa_key 文件权限未修改</td>
    <td><a href="#rsa_key"> 检查  /etc/ssh/ssh_host_rsa_key 文件权限是否已修改</a></td>
  </tr>
</tbody>
</table>

## 故障处理

### 检查 /var/empty/sshd 文件权限是否已修改[](id:sshd)
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



###  检查  /etc/ssh/ssh_host_rsa_key 文件权限是否已修改[](id:rsa_key)
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
