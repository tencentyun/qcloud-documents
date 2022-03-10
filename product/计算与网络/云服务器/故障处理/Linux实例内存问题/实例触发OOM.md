## 现象描述
Linux 云服务器在内存使用率未占满的情况下触发了 OOM（Out Of Memory）。如下图所示：
![](https://main.qcloudimg.com/raw/72cbd63ac445a1caa8d82fa1e55ba5a5.png)

## 可能原因
可能是由系统可用内存低于 `min_free_kbytes` 值导致。`min_free_kbytes` 值表示强制 Linux 系统最低保留的空闲内存（Kbytes），如果系统可用内存低于设定的 `min_free_kbytes` 值，则默认系统启动 oom-killer 或强制重启。具体行为由内核参数 `vm.panic_on_oom` 值决定：
 - 若 `vm.panic_on_oom=0`，则系统会提示 OOM，并启动 oom-killer 杀掉占用最高内存的进程。
 - 若 `vm.panic_on_oom =1`，则系统会自动重启。

## 解决思路
1. 参考 [处理步骤](#ProcessingSteps) 进行排查，查看实例内存使用率是否过高及总进程数是否受限。
2. 核实 `min_free_kbytes` 值设置，并修改为正确配置。


## 处理步骤[](id:ProcessingSteps)
1. 参考 [内存使用率过高问题处理](https://cloud.tencent.com/document/product/213/54644#ProcessingSteps) ，查看实例是否内存使用率过高。若实例内存使用率正常，则执行下一步。
2. 参考 [日志报错 fork：Cannot allocate memory](https://cloud.tencent.com/document/product/213/54645)，核实进程数是否超限。若总进程数未超限，则执行下一步。
3. 登录云服务器，执行以下命令查看 `min_free_kbytes` 值。
```
sysctl -a | grep min_free
```
`min_free_kbytes` 值单位为 kbytes，下图所示 `min_free_kbytes = 1024000` 即为1GB。
![](https://main.qcloudimg.com/raw/18ac6c04962abfbf67132eab1a604167.png)
4. 执行以下命令，使用 VIM 编辑器打开 `/etc/sysctl.conf` 配置文件。
```
vim /etc/sysctl.conf
```
5. 按 **i** 进入编辑模式，修改 `vm.min_free_kbytes` 配置项。若该配置项不存在，则直接在配置文件中增加即可。
<dx-alert infotype="explain" title="">
建议修改 `vm.min_free_kbytes` 值为不超过总内存的1%即可。
</dx-alert>
6. 按 **Esc** 并输入 **:wq** 后，按 **Enter** 保存并退出 VIM 编辑器。
7. 执行以下命令，使配置生效即可。
```
sysctl -p
```
