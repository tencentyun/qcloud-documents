>?
>- 本文来源于社区贡献，仅供参考，与腾讯云相关产品无关。您可前往 [社区](https://cloud.tencent.com/developer/ask) 获取更多帮助和支持。
>- 文中涉及的相关文件操作，请务必谨慎执行。如有必要，可通过创建快照等方式进行数据备份。
> 


## 现象描述
使用 SSH 登录时，出现报错信息 “ssh_exchange_identification: read: Connection reset by peer”。或出现以下报错信息：
- “ssh_exchange_identification: Connection closed by remote host”
- “kex_exchange_identification: read: Connection reset by peer”
- “kex_exchange_identification: Connection closed by remote host”


## 问题原因
导致该类问题的原因较多，常见原因有以下几种：
- 本地访问控制限制了连接
- 某些入侵防御软件更改了防火墙规则，例如 Fail2ban 及 denyhost 等
- sshd 配置中最大连接数限制
- 本地网络存在问题


## 解决思路
参考 [处理步骤](#ProcessingSteps)，从访问策略、防火墙规则、sshd 配置及网络环境几方面定位及解决问题。

## 处理步骤[](id:ProcessingSteps)
 

### 检查及调整访问策略设置
Linux 中可以通过 `/etc/hosts.allow` 和 `/etc/hosts.deny` 文件设置访问策略，两个文件分别对应允许和阻止的策略。例如，可以在 `hosts.allow` 文件中设置信任主机规则，在 `hosts.deny` 文件中拒绝所有其他主机。以 `hosts.deny` 为例，阻止策略配置如下：
```
in.sshd:ALL			# 阻止全部ssh连接
in.sshd:218.64.87.0/255.255.255.128	# 阻止218.64.87.0—-127的ssh
ALL:ALL				# 阻止所有TCP连接
```


[使用 VNC 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35701) 后，请检查 `/etc/hosts.deny` 文件及 `/etc/hosts.allow` 文件。并根据检查结果选择以下处理方式：
 - 配置有误，请按需修改，更改即时生效。
 - 未配置或配置无误，请进行下一步。
>?若您未配置访问策略，则默认文件均为空，且允许所有连接。
>
 

### 检查 iptables 防火墙规则
检查是否 iptables 防火墙规则是否被修改，包括使用某些入侵防御软件，例如 Fail2ban 及 denyhost 等。执行以下命令，查看防火墙是否阻止过 SSH 连接。
```
sudo iptables -L --line-number
```
 - 若 SSH 连接被阻止，请通过对应软件白名单等相关策略自行设置。
 - 若 SSH 连接未被阻止，请进行下一步。

### 检查及调整 sshd 配置
1. 执行以下命令，使用 VIM 编辑器进入 `sshd_config` 配置文件。
```
vim /etc/ssh/sshd_config
```
2. 检查 `MaxStartups` 值是否需调整。`sshd_config` 配置文件中通过 `MaxStartups` 设置允许的最大连接数，如果短时间需建立较多连接，则需适当调整该值。
 - 若需调整，则请参考以下步骤修改：
    1. 按 **i** 进入编辑模式，修改完成后按 **Esc** 退出编辑模式，并输入 **:wq** 保存修改。
>?MaxStartups 10:30:100为默认配置，指定 SSH 守护进程未经身份验证的并发连接的最大数量。10:30:100表示从第10个连接开始，以30%的概率（递增）拒绝新的连接，直到连接数达到100。
    2. 执行以下命令，重启 sshd 服务。
```
service sshd restart
```
 - 若无需调整，请进行下一步。

### 测试网络环境
1. 检查是否使用了 [内网 IP](https://cloud.tencent.com/document/product/213/5225) 进行登录。
 - 是，请切换为 [公网 IP](https://cloud.tencent.com/document/product/213/5224) 后再次进行尝试。
 - 否，请进行下一步。
2. 使用其他网络环境测试是否连接正常。
 - 是，请重启实例后使用 VNC 登录实例。
 - 否，请根据测试结果解决网络环境问题。
 
 
若至此您仍未解决 SSH 登录问题，则可能是由于系统内核出现异常或其他潜在原因导致，请通过 [在线支持](https://cloud.tencent.com/act/event/Online_service?from=doc_213) 联系我们进一步处理问题。

