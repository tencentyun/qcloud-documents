### 如何登录云服务器？

登录实例相关文档指引参考：

- [登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)
- [登录 Windows 实例](https://cloud.tencent.com/document/product/213/5435)

### 如何设置初始密码？

在购买云服务器时，您可以设置自定义密码或选择系统自动生成密码。

#### 设置自定义密码

1. [创建实例](https://cloud.tencent.com/doc/product/213/4855) 时，在设置实例名称及登录方式部分可以选择登录方式，默认为 **设置密码**。

2. 按照规定的密码字符限制，输入密码和确认密码，确认配置信息后单击【立即购买】，待云服务器实例分配成功。便可以使用设置的密码登录实例。

#### 系统自动生成密码

您也可以选择【自动生成密码】，单击【立即购买】待实例分配成功后在 [站内信](https://console.cloud.tencent.com/message) 中即可获取 CVM 实例初始密码。

> **注意：**
> 设置密码的字符限制：
>   - Linux 云服务器密码需 8 到 16 位， ```a-z 和 A-Z 和 0-9 和 ( ) ` ~ ! @ # $ % ^ & * - + = _ | { } [ ] : ; ' < > , . ? / ``` 中至少包括两项。
>   - Windows 云服务器密码需 12 到 16 位， ```a-z 和 A-Z 和 0-9 和 ( ) ` ~ ! @ # $ % ^ & * - + = _ | { } [ ] : ; ' < > , . ? / ``` 中至少包括三项。

### 如何重置密码？重置密码失败怎么办？

#### 重置密码操作：

> **注意：**
>
> 只有关机状态下才可以对云服务器进行重置密码操作，如果机器处于运行中请先对主机进行关机。

1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/) 。
2. 重置密码。不能重置密码的实例会显示不能重置密码的原因。
   1. 单个关机的实例，在右侧操作栏中，单击【更多】>【重置密码】。
   2. 批量关机的实例，勾选所有需要重置密码的主机，在列表顶部，单击【重置密码】，即可批量修改主机登录密码。
3. 在重置密码弹出框中输入新密码、确认密码以及验证码，单击【确认重置】。
4. 等待重置成功，您将收到重置成功的站内信，即可使用新密码开机使用云服务器。

#### 重置密码失败

若您确保实例已关机，还是无法重置密码，请 [提交工单](https://console.cloud.tencent.com/workorder/category)，工程师将协助您解决问题。

### Linux 实例关联 SSH 密钥后，使用用户名密码登录报错，无法登录?
云服务器关联 SSH 密钥后，SSH 服务 **默认关闭** 用户名密码登录，请使用 SSH 密钥登录云服务器。 

Linux 云服务器登录指引：[登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)

### 使用 SSH 密钥无法登录 Linux 实例，如何排查？

您可以参考以下解决方案：

1. 在 [控制台](https://console.cloud.tencent.com/cvm/securitygroup) 取消或者修改安全组策略。参考：[安全组操作指南](https://cloud.tencent.com/document/product/213/12450)

2. 在 [控制台](https://console.cloud.tencent.com/cvm/sshkey) 取消密钥登录方式，或根据指导正确设置密钥验证登录机器。参考：[SSH 密钥操作指南](https://cloud.tencent.com/document/product/213/16691)

3. 使用 VNC 登录实例，查看网卡状态及 IP 配置信息是否正确。参考：[登录 Linux 实例操作指南](https://cloud.tencent.com/document/product/213/5436)

   ![](https://main.qcloudimg.com/raw/17fa30409db52577fc8fed99a43264d2.png)

4. 确认实例是否正确地运行在模式 3 或模式 5：
   ![](https://main.qcloudimg.com/raw/0371d6b8c5a0b89ac70cff6b56adf3be.png)

5. 确认机器的 sshd 服务运行 OK，且端口等配置文件没有问题。
   ![](https://main.qcloudimg.com/raw/32364a0beac01cc63c82d61ebadf89c2.png)
6. 确认机器的 iptables 防火墙是否拦截，检查其策略是否 OK。![](https://main.qcloudimg.com/raw/9dbc3baa79c24673e59fb228cc57afad.png)
7. 确认机器的 tcp_wrappers 是否有对 ssh 访问的拦截控制。
   ![](https://main.qcloudimg.com/raw/76ac9f09b606cbd7f2121f4306ff3bc8.png)

8. 确认是否 ssh 登录机器的用户被 PAM 模块拦截登录（不常见）：
   ![](https://main.qcloudimg.com/raw/c7af6184b32867d0eb77cdfe1c362d04.png)

### 如何使用 VNC 登录云服务器？

VNC 登录是腾讯云为用户提供的一种通过 Web 浏览器远程连接云服务器的方式。在没有安装远程登录客户端或者客户端远程登录无法使用的情况下，用户可以通过 VNC 登录连接到云服务器，观察云服务器状态，并且可通过云服务器账户进行基本的云服务器管理操作。相关操作指引请参考以下文档的相关部分：

- [登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)
- [登录 Windows 实例](https://cloud.tencent.com/document/product/213/5435)

### Windows 服务器如何配置多用户远程登录？

Windows 服务器可以支持同时多人远程登录，具体登录方法如下： 

1. 请打开【控制面板】>【管理工具】>【终端服务】>【终端服务配置】 　　 
2. 右键单击 RDP-Tcp 连接，【属性】>【网络适配器】>【最大连接数】
3. 默认情况下，若您不添加终端服务功能，最大连接数只能调整为 2。 终端服务器授权模式设置，【属性】>【常规】，**取消勾选 **限制每个用户只能使用一个会话。就可以实现多登录了。若设置未生效，请重启后再尝试登录。

![](https://main.qcloudimg.com/raw/771ba6c304fea14aa1159073d6f0af0c.png)

### 本地为 Windows 时，如何使用远程桌面连接登录 Windows 实例？

操作指引参考：[登录 Windows 实例](https://cloud.tencent.com/document/product/213/5435#.E6.9C.AC.E5.9C.B0.E4.B8.BA-windows-.E8.AE.A1.E7.AE.97.E6.9C.BA) 相关章节。

### 本地为 Linux 时，如何使用 rdesktop 登录 Windows 实例？

操作指引参考：[登录 Windows 实例](https://cloud.tencent.com/document/product/213/5435#.E6.9C.AC.E5.9C.B0.E4.B8.BA-linux-.E8.AE.A1.E7.AE.97.E6.9C.BA) 相关章节。

### 本地为 Mac OS 时，如何使用 Microsoft Remote Desktop Connection Client for Mac 登录 Windows 实例？

操作指引参考：[登录 Windows 实例](https://cloud.tencent.com/document/product/213/5435#.E6.9C.AC.E5.9C.B0.E4.B8.BA-mac-os-.E8.AE.A1.E7.AE.97.E6.9C.BA) 相关章节。

### Ubuntu 系统如何使用 root 用户来登录？

Ubuntu系统的默认用户名是 ubuntu，并在安装过程中默认不设置 root 账户和密码。若有需要，在设置开启允许 root 用户登录即可。方法如下：
1. 修改 root 密码。输入以下命令，然后输入密码。

  ```
  sudo passwd root
  ```
因为 root 用户默认没有密码，无法使用。想用 root 用户时，需要先为 root 用户设置一个密码。
![](https://main.qcloudimg.com/raw/39577876c773f35904c87538bf18b6fa.png)

2. 修改 ssh 配置。将 PermitRootLogin 这项改为 yes，保存退出。
  ```
  sudo vi /etc/ssh/sshd_config 
  ```
  ![](https://main.qcloudimg.com/raw/53180728677a3c4cad46821485e82437.png)

 3. 重启 ssh 服务。
    ```
    sudo service ssh restart
    ```
4. 最后验证是否可以使用 root 用户远程登录。

### 如何批量重置在线 Linux 实例的密码？

若您需要在不关机的情况下，批量进行 Linux 实例重置密码操作，您可以单击下载 [批量重置脚本](http://batchchpasswd-10016717.file.myqcloud.com/batch-chpasswd.tgz?_ga=1.165307193.726382295.1500898081)，运行脚本。脚本使用方法如下：

> **注意：**
> - 若您在公网机器上运行该脚本，填到 hosts.txt 文件的 IP 需为实例的公网 IP，
> - 若您在内网机器上运行该脚本，则可以填写实例的内网 IP。

将需要操作的实例 IP，SSH 端口，账号，旧密码和新密码填写到 hosts.txt 文件中，每一行代表一个主机，例如：
```
10.0.0.1 22 root old_passwd new_passwd 
10.0.0.2 22 root old_passwd new_passwd
```
执行如下代码：
```
./batch-chpasswd.py
```

返回示例:
```
change password for root@10.0.0.1
spawn ssh root@10.0.0.1 -p 22
root's password: 
Authentication successful.
Last login: Tue Nov 17 20:22:25 2017 from 10.181.225.39
[root@VM_18_18_centos ~]# echo root:root | chpasswd
[root@VM_18_18_centos ~]# exit
logout
```

```
change password for root@10.0.0.2
spawn ssh root@10.0.0.2 -p 22
root's password: 
Authentication successful.
Last login: Mon Nov  9 15:19:22 2017 from 10.181.225.39
[root@VM_19_150_centos ~]# echo root:root | chpasswd
[root@VM_19_150_centos ~]# exit
logout
```
