>?
>- 本文来源于社区贡献，仅供参考，与腾讯云相关产品无关。您可前往 [社区](https://cloud.tencent.com/developer/ask) 获取更多帮助和支持。
>- 文中涉及的相关文件操作，请务必谨慎执行。如有必要，可通过创建快照等方式进行数据备份。
> 
 

## 现象描述
使用 SSH 登录时，出现如下报错信息：
```
Permission denied (publickey,gssapi-keyex,gssapi-with-mic).
sshd[10826]: Connection closed by xxx.xxx.xxx.xxx.
Disconnected:No supported authentication methods available.
```

## 问题原因
SSH 服务修改了 `PasswordAuthentication` 参数，禁用了密码验证登录导致。


## 解决思路
1. 参考 [处理步骤](#ProcessingSteps)，进入 SSH 配置文件 `sshd_config`。
2. 修改 `PasswordAuthentication` 参数，并重启 SSH 服务即可。

## 处理步骤[](id:ProcessingSteps)
1. [使用 VNC 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35701)。
2. 执行以下命令，使用 VIM 编辑器进入 `sshd_config` 配置文件。
```shell
vim /etc/ssh/sshd_config
```
3. 按 **i** 进入编辑模式，将 `PasswordAuthentication no` 修改为 `PasswordAuthentication yes`。
4. 按 **Esc** 退出编辑模式，并输入 **:wq** 保存修改。
4. 对应实际使用的操作系统，执行以下命令，重启 SSH 服务。
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
