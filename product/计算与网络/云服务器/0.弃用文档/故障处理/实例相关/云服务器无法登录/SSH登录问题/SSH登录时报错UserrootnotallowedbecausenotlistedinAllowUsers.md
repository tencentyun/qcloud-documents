>?
>- 本文来源于社区贡献，仅供参考，与腾讯云相关产品无关。您可前往 [社区](https://cloud.tencent.com/developer/ask) 获取更多帮助和支持。
>- 文中涉及的相关文件操作，请务必谨慎执行。如有必要，可通过创建快照等方式进行数据备份。
> 


## 现象描述
使用 SSH 登录时，出现报错信息 “User test from xxx.xxx.xxx.xxx not allowed because not listed in AllowUsers”。

## 问题原因
该问题通常是由于 SSH 服务启用了用户登录控制参数，对登录用户进行了限制。参数说明如下：
- **AllowUsers**：允许登录的用户白名单，只有该参数标注的用户可以登录。
- **DenyUsers**：拒绝登录的用户黑名单，该参数标注的用户都被拒绝登录。
- **AllowGroups**：允许登录的用户组白名单，只有该参数标注的用户组可以登录。
- **DenyGroups**：拒绝登录的用户组黑名单，该参数标注的用户组都被拒绝登录。

>?拒绝策略优先级高于允许策略。

## 解决思路
1. 参考 [处理步骤](#ProcessingSteps)，进入 SSH 配置文件 `sshd_config` 检查配置。
2. 删除用户登录控制参数，并重启 SSH 服务即可。

## 处理步骤[](id:ProcessingSteps)
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
<dx-tabs>
::: CentOS
```shell
systemctl restart sshd.service
```
:::
::: Ubuntu
```shell
service sshd restart
```
:::
</dx-tabs>
重启 SSH 服务后，即可使用 SSH 登录。详情请参见 <a href="https://cloud.tencent.com/document/product/213/35700">使用 SSH 登录 Linux 实例</a>。
