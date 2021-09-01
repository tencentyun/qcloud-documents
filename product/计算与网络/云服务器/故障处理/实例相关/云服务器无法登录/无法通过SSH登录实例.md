>?
>- 本文来源于社区贡献，仅供参考，与腾讯云相关产品无关。您可前往 [社区](https://cloud.tencent.com/developer/ask) 获取更多帮助和支持。
>- 文中涉及的相关文件操作，请务必谨慎执行。如有必要，可通过创建快照等方式进行数据备份。
> 

## 现象描述
[使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35700) 时，提示无法连接或者连接失败，导致无法正常登录 Linux 实例。
 
## 问题定位及处理[](id:ProcessingSteps)
当使用 SSH 登录 Linux 实例失败，并返回报错信息时，您可记录报错信息，并匹配以下常见的报错信息，快速定位问题并参考步骤进行解决。
 
<dx-accordion>
::: SSH 登录报错 User root not allowed because not listed in AllowUsers

#### 问题原因[](id:userNotListAllowUsers)
该问题通常是由于 SSH 服务启用了用户登录控制参数，对登录用户进行了限制。参数说明如下：
- **AllowUsers**：允许登录的用户白名单，只有该参数标注的用户可以登录。
- **DenyUsers**：拒绝登录的用户黑名单，该参数标注的用户都被拒绝登录。
- **AllowGroups**：允许登录的用户组白名单，只有该参数标注的用户组可以登录。
- **DenyGroups**：拒绝登录的用户组黑名单，该参数标注的用户组都被拒绝登录。

<dx-alert infotype="explain" title="">
拒绝策略优先级高于允许策略。
</dx-alert>


#### 解决思路
1. 参考 [处理步骤](#ProcessingSteps1)，进入 SSH 配置文件 `sshd_config` 检查配置。
2. 删除用户登录控制参数，并重启 SSH 服务即可。


#### 处理步骤[](id:ProcessingSteps1)
1. [使用 VNC 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35701)。
2. 执行以下命令，使用 VIM 编辑器进入 `sshd_config` 配置文件。
```shell
vim /etc/ssh/sshd_config
```
3. 按 **i** 进入编辑模式，找到并删除以下配置，或在每行行首增加 `#` 进行注释。
```shell
AllowUsers root test
DenyUsers test
DenyGroups test
AllowGroups root
```
4. 按 **Esc** 退出编辑模式，输入 **:wq** 保存修改。
5. 对应实际使用的操作系统，执行以下命令，重启 SSH 服务。
  - CentOS
```shell
systemctl restart sshd.service
```
  - Ubuntu
```shell
service sshd restart
```

重启 SSH 服务后，即可使用 SSH 登录。详情请参见 <a href="https://cloud.tencent.com/document/product/213/35700">使用 SSH 登录 Linux 实例</a>。


::: 
::: SSH 登录报错 Disconnected:No supported authentication methods available

#### 现象描述[](id:noSupportesAuthentication)
使用 SSH 登录时，出现如下报错信息：
```
Permission denied (publickey,gssapi-keyex,gssapi-with-mic).
sshd[10826]: Connection closed by xxx.xxx.xxx.xxx.
Disconnected:No supported authentication methods available.
```

#### 问题原因
SSH 服务修改了 `PasswordAuthentication` 参数，禁用了密码验证登录导致。


#### 解决思路
1. 参考 [处理步骤](#ProcessingSteps2)，进入 SSH 配置文件 `sshd_config`。
2. 修改 `PasswordAuthentication` 参数，并重启 SSH 服务即可。


#### 处理步骤[](id:ProcessingSteps2)
1. [使用 VNC 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35701)。
2. 执行以下命令，使用 VIM 编辑器进入 `sshd_config` 配置文件。
```shell
vim /etc/ssh/sshd_config
```
3. 按 **i** 进入编辑模式，将 `PasswordAuthentication no` 修改为 `PasswordAuthentication yes`。
4. 按 **Esc** 退出编辑模式，并输入 **:wq** 保存修改。
5. 对应实际使用的操作系统，执行以下命令，重启 SSH 服务。
  - CentOS
```shell
systemctl restart sshd.service
```
  - Ubuntu
```shell
service sshd restart
```
重启 SSH 服务后，即可使用 SSH 登录。详情请参见 <a href="https://cloud.tencent.com/document/product/213/35700">使用 SSH 登录 Linux 实例</a>。

:::
::: SSH 登录报错 ssh_exchange_identification: read: Connection reset by peer

#### 现象描述[](id:connectionResetByPeer)
使用 SSH 登录时，出现报错信息 “ssh_exchange_identification: read: Connection reset by peer”。或出现以下报错信息：
- “ssh_exchange_identification: Connection closed by remote host”
- “kex_exchange_identification: read: Connection reset by peer”
- “kex_exchange_identification: Connection closed by remote host”


#### 问题原因
导致该类问题的原因较多，常见原因有以下几种：
- 本地访问控制限制了连接
- 某些入侵防御软件更改了防火墙规则，例如 Fail2ban 及 denyhost 等
- sshd 配置中最大连接数限制
- 本地网络存在问题


#### 解决思路
参考 [处理步骤](#ProcessingSteps3)，从访问策略、防火墙规则、sshd 配置及网络环境几方面定位及解决问题。



#### 处理步骤[](id:ProcessingSteps3)
 

#### 检查及调整访问策略设置
Linux 中可以通过 `/etc/hosts.allow` 和 `/etc/hosts.deny` 文件设置访问策略，两个文件分别对应允许和阻止的策略。例如，可以在 `hosts.allow` 文件中设置信任主机规则，在 `hosts.deny` 文件中拒绝所有其他主机。以 `hosts.deny` 为例，阻止策略配置如下：
```
in.sshd:ALL			# 阻止全部ssh连接
in.sshd:218.64.87.0/255.255.255.128	# 阻止218.64.87.0—-127的ssh
ALL:ALL				# 阻止所有TCP连接
```


[使用 VNC 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35701) 后，请检查 `/etc/hosts.deny` 文件及 `/etc/hosts.allow` 文件。并根据检查结果选择以下处理方式：
 - 配置有误，请按需修改，更改即时生效。
 - 未配置或配置无误，请进行下一步。

<dx-alert infotype="explain" title="">
若您未配置访问策略，则默认文件均为空，且允许所有连接。
</dx-alert>


 

#### 检查 iptables 防火墙规则
检查是否 iptables 防火墙规则是否被修改，包括使用某些入侵防御软件，例如 Fail2ban 及 denyhost 等。执行以下命令，查看防火墙是否阻止过 SSH 连接。
```
sudo iptables -L --line-number
```
 - 若 SSH 连接被阻止，请通过对应软件白名单等相关策略自行设置。
 - 若 SSH 连接未被阻止，请进行下一步。


#### 检查及调整 sshd 配置
1. 执行以下命令，使用 VIM 编辑器进入 `sshd_config` 配置文件。
```
vim /etc/ssh/sshd_config
```
2. 检查 `MaxStartups` 值是否需调整。`sshd_config` 配置文件中通过 `MaxStartups` 设置允许的最大连接数，如果短时间需建立较多连接，则需适当调整该值。
 - 若需调整，则请参考以下步骤修改：
    1. 按 **i** 进入编辑模式，修改完成后按 **Esc** 退出编辑模式，并输入 **:wq** 保存修改。
<dx-alert infotype="explain" title="">
MaxStartups 10:30:100为默认配置，指定 SSH 守护进程未经身份验证的并发连接的最大数量。10:30:100表示从第10个连接开始，以30%的概率（递增）拒绝新的连接，直到连接数达到100。
</dx-alert>
    2. 执行以下命令，重启 sshd 服务。
```
service sshd restart
```
 - 若无需调整，请进行下一步。
 

#### 测试网络环境
1. 检查是否使用了 [内网 IP](https://cloud.tencent.com/document/product/213/5225) 进行登录。
  - 是，请切换为 [公网 IP](https://cloud.tencent.com/document/product/213/5224) 后再次进行尝试。
  - 否，请进行下一步。
2. 使用其他网络环境测试是否连接正常。
  - 是，请重启实例后使用 VNC 登录实例。
  - 否，请根据测试结果解决网络环境问题。
 
 
若至此您仍未解决 SSH 登录问题，则可能是由于系统内核出现异常或其他潜在原因导致，请通过 [在线支持](https://cloud.tencent.com/act/event/Online_service?from=doc_213) 联系我们进一步处理问题。
:::
::: SSH 登录报错 Permission denied, please try again

#### 现象描述[](id:permissionDenied)
root 用户使用 SSH 登录 Linux 实例时，出现报错信息 “Permission denied, please try again”。
 

#### 问题原因
系统启用了 SELinux 服务，或是由 SSH 服务修改了 `PermitRootLogin` 配置所致。


#### 解决思路
参考 [处理步骤](#ProcessingSteps4)，检查 SELinux 服务及 SSH 配置文件 `sshd_config` 中的 `PermitRootLogin` 参数，核实问题原因并解决问题。

#### 处理步骤[](id:ProcessingSteps4)


#### 检查及关闭 SELinux 服务
1. [使用 VNC 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35701)。
2. 执行以下命令，查看当前 SELinux 服务状态。
```
/usr/sbin/sestatus -v 
```
若返回参数为 `enabled` 即处于开启状态，`disabled` 即处于关闭状态。如下所示，则为开启状态：
```
SELinux status:       enabled
```
3. 您可结合实际情况，临时或永久关闭 SELinux 服务。
  - 临时关闭 SELinux 服务
执行以下命令，临时关闭 SELinux。修改实时生效，无需重启系统或实例。
```
setenforce 0
```
  - 永久关闭 SELinux 服务
执行以下命令，关闭 SELinux 服务。
```
sed -i 's/SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config
```
<dx-alert infotype="notice" title="">
- 该命令仅适用于 SELinux 服务为 enforcing 状态时。
- 执行命令后需重启系统或实例，使修改生效。
</dx-alert>


#### 检查及调整 sshd 配置
1. [使用 VNC 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35701)。
2. 执行以下命令，使用 VIM 编辑器进入 `sshd_config` 配置文件。
```shell
vim /etc/ssh/sshd_config
```
3. 按 **i** 进入编辑模式，将 `PermitRootLogin no` 修改为 `PermitRootLogin yes`。
>?
>- 若 `sshd_config` 中未配置该参数，则默认允许 root 用户登录。
>- 该参数仅影响 root 用户使用 SSH 登录，不影响 root 用户通过其他方式登录实例。
>
4. 按 **Esc** 退出编辑模式，并输入 **:wq** 保存修改。
5. 执行以下命令，重启 SSH 服务。
```shell
service sshd restart
```
重启 SSH 服务后，即可使用 SSH 登录。详情请参见 <a href="https://cloud.tencent.com/document/product/213/35700">使用 SSH 登录 Linux 实例</a>。
:::
::: SSH 登录时报错 Too many authentication failures for root

#### 现象描述[](id:tooManyFailures)
使用 SSH 登录时，登录时多次输入密码后返回报错信息 “Too many authentication failures for root”，并且连接中断。

#### 问题原因
在多次连续输入错误密码后，触发了 SSH 服务密码重置策略导致。


#### 解决思路
1. 参考 [处理步骤](#ProcessingSteps5)，进入 SSH 配置文件 `sshd_config`。
2. 检查并修改 SSH 服务密码重置策略的 `MaxAuthTries` 参数配置，并重启 SSH 服务即可。


#### 处理步骤[](id:ProcessingSteps5)
1. [使用 VNC 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35701)。
2. 执行以下命令，使用 VIM 编辑器进入 `sshd_config` 配置文件。
```shell
vim /etc/ssh/sshd_config
```
3. 查看是否包含类似如下配置。
```
MaxAuthTries 5
```
<dx-alert infotype="explain" title="">
- 该参数默认未启用，用于限制用户每次使用 SSH 登录时，能够连续输入错误密码的次数。超过设定的次数则会断开 SSH 连接，并显示相关错误信息。但相关账号不会被锁定，仍可重新使用 SSH 登录。
- 请您结合实际情况确定是否需修改配置，如需修改，建议您备份 `sshd_config` 配置文件。
</dx-alert>
4. 按 **i** 进入编辑模式，修改以下配置，或在行首增加 `#` 进行注释。
```
MaxAuthTries <允许输入错误密码的次数>
```
5. 按 **Esc** 退出编辑模式，输入 **:wq** 保存修改。
6. 执行以下命令，重启 SSH 服务。
```shell
service sshd restart
```
重启 SSH 服务后，即可使用 SSH 登录。详情请参见 <a href="https://cloud.tencent.com/document/product/213/35700">使用 SSH 登录 Linux 实例</a>。

:::
::: SSH 启动时报错 error while loading shared libraries

#### 现象描述[](id:errorLibraries)
Linux 实例启动 SSH 服务，在 secure日志文件中，或直接返回类似如下错误信息：
- “error while loading shared libraries： libcrypto.so.10: cannot open shared object file: No such file or directory”
- “PAM unable to dlopen(/usr/lib64/security/pam_tally.so): /usr/lib64/security/pam_tally.so: cannot open shared object file: No such file or directory”


#### 问题原因
SSH 服务运行依赖相关的系统库文件丢失或权限配置等异常所致。


#### 解决思路
参考 [处理步骤](#ProcessingSteps6) 检查系统库文件并进行修复。



#### 处理步骤[](id:ProcessingSteps6)
<dx-alert infotype="explain" title="">
本文以处理 libcrypto.so.10 库文件异常为例，其他库文件异常的处理方法类似，请结合实际情况进行操作。
</dx-alert>



#### 获取库文件信息
1. [使用 VNC 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35701)。
2. 执行以下命令，查看 libcrypto.so.10 库文件信息。
```
ll /usr/lib64/libcrypto.so.10
```
返回类似如下信息，表示 `/usr/lib64/libcrypto.so.10` 是 `libcrypto.so.1.0.2k` 库文件的软链接。
```
lrwxrwxrwx 1 root root 19 Jan 19  2021 /usr/lib64/libcrypto.so.10 -> libcrypto.so.1.0.2k
```
2. 执行以下命令，查看 `libcrypto.so.1.0.2k` 库文件信息。
```
ll /usr/lib64/libcrypto.so.1.0.2k
```
返回类似如下信息：
```
-rwxr-xr-x 1 root root 2520768 Dec 17  2020 /usr/lib64/libcrypto.so.1.0.2k
```
3. 记录正常库文件的路径、权限、属组等信息，并通过以下方式进行处理：
	 - [查找及替换库文件](#findAndReplace)
	 - [外部文件上传](#fileUpload)
	 - [通过快照回滚恢复](#snapshotRollback)



#### 查找及替换库文件[](id:findAndReplace)
1. 执行以下命令，查找 `libcrypto.so.1.0.2k` 文件。
```
find / -name libcrypto.so.1.0.2k
```
2. 根据返回结果，执行以下命令，将库文件拷贝至正常目录。
```
cp <步骤1获取的库文件绝对路径> /usr/lib64/libcrypto.so.1.0.2k
```
3. 依次执行以下命令，修改文件权限、所有者及属组。
```
chmod 755 /usr/lib64/libcrypto.so.1.0.2k
```
```
chown root:root /usr/lib64/libcrypto.so.1.0.2k
```
4. 执行以下命令，创建软链接。
```
ln -s /usr/lib64/libcrypto.so.1.0.2k /usr/lib64/libcrypto.so.10
```
5. 执行以下命令，启动 SSH 服务。
```
service sshd start
```


#### 外部文件上传[](id:fileUpload)
1. 通过 FTP 软件将其他正常服务器上的 `libcrypto.so.1.0.2k` 的库文件上传至目标服务器的 `\tmp` 目录。
<dx-alert infotype="explain" title="">
本文以上传至目标服务器的 `\tmp` 目录为例，您可结合实际情况进行修改。
</dx-alert>
2. 执行以下命令，将库文件拷贝至正常目录。
```
cp /tmp/libcrypto.so.1.0.2k /usr/lib64/libcrypto.so.1.0.2k
```
3. 依次执行以下命令，修改文件权限、所有者及属组。
```
chmod 755 /usr/lib64/libcrypto.so.1.0.2k
```
```
chown root:root /usr/lib64/libcrypto.so.1.0.2k
```
4. 执行以下命令，创建软链接。
```
ln -s /usr/lib64/libcrypto.so.1.0.2k /usr/lib64/libcrypto.so.10
```
5. 执行以下命令，启动 SSH 服务。
```
service sshd start
```


#### 通过快照回滚恢复[](id:snapshotRollback)
可通过回滚实例系统盘的历史快照进行库文件恢复，详情请参见 [从快照回滚数据](https://cloud.tencent.com/document/product/362/5756)。

<dx-alert infotype="notice" title="">
- 快照回滚会导致快照创建后的数据丢失，请谨慎操作。
- 建议按快照创建时间从近到远的顺序逐一尝试回滚，直至 SSH 服务正常运行。若回滚后仍无法正常运行 SSH 服务，则说明该时间点的系统已经出现异常。
</dx-alert>

:::
</dx-accordion>


<br>
若您的问题仍未解决，请通过 <a href="https://cloud.tencent.com/act/event/Online_service?from=doc_213">在线支持</a> 联系我们寻求帮助。






